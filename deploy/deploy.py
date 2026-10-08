#!/usr/bin/env python3
"""Deploy site/ to the LiquidWeb server over explicit FTPS (FTP over TLS, port 21).

Reads credentials from the repo-root .env (FTP_HOST, FTP_PORT, FTP_USER,
FTP_PASS, FTP_REMOTE_DIR). Uploads every file under site/ preserving the
directory structure. Uses only the Python standard library.

    python3 deploy/deploy.py [--dry-run] [--only <folder under site/>]
"""

import posixpath
import sys
from ftplib import FTP_TLS, error_perm
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SITE_DIR = REPO_ROOT / "site"
ENV_FILE = REPO_ROOT / ".env"

SKIP_NAMES = {".DS_Store", "Thumbs.db"}

PLACEHOLDERS = {"your.server.com", "youruser", "yourpassword"}


def load_env(path: Path) -> dict:
    env = {}
    if not path.exists():
        sys.exit(f"ERROR: {path} not found. Create it with the FTP_* variables.")
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        env[key.strip()] = value.strip()
    return env


def main() -> None:
    dry_run = "--dry-run" in sys.argv
    # --only prayer-song : upload just that folder of site/, leaving every other page on the server untouched
    only = sys.argv[sys.argv.index("--only") + 1].strip("/") if "--only" in sys.argv else None

    env = load_env(ENV_FILE)
    missing = [k for k in ("FTP_HOST", "FTP_USER", "FTP_PASS", "FTP_REMOTE_DIR") if not env.get(k)]
    if missing:
        sys.exit(f"ERROR: missing in .env: {', '.join(missing)}")

    placeholder = [k for k in ("FTP_HOST", "FTP_USER") if env[k] in PLACEHOLDERS]
    if placeholder and not dry_run:
        sys.exit(
            "ERROR: these .env values are still placeholders: "
            + ", ".join(placeholder)
            + "\nFill in the real LiquidWeb credentials first."
        )

    if env["FTP_PASS"] in PLACEHOLDERS and not dry_run:
        import getpass
        env["FTP_PASS"] = getpass.getpass(f"FTP password for {env['FTP_USER']}@{env['FTP_HOST']}: ")
        if not env["FTP_PASS"]:
            sys.exit("ERROR: no password entered.")

    host = env["FTP_HOST"]
    port = int(env.get("FTP_PORT", "21"))
    user = env["FTP_USER"]
    password = env["FTP_PASS"]
    remote_dir = env["FTP_REMOTE_DIR"].rstrip("/") or "/"

    if not SITE_DIR.is_dir():
        sys.exit(f"ERROR: {SITE_DIR} not found.")

    # A folder holding a file named HOLD is not uploaded. It marks work that TS has not said "ship" for yet
    # (delete the HOLD file to release it). The server's own config and buyer data are never uploaded either.
    held = sorted({h.parent for h in SITE_DIR.rglob("HOLD")})
    def blocked(path: Path) -> bool:
        if any(h == path.parent or h in path.parents for h in held):
            return True
        rel = path.relative_to(SITE_DIR).as_posix()
        return rel == "prayer-song/api/config.php" or rel.startswith("prayer-song/api/data/")
    for h in held:
        print(f"HELD, not uploading: site/{h.relative_to(SITE_DIR)}/  (remove its HOLD file to release)")

    files = sorted(
        p for p in SITE_DIR.rglob("*")
        if p.is_file() and p.name not in SKIP_NAMES and not blocked(p)
        and (only is None or p.relative_to(SITE_DIR).as_posix().startswith(only + "/"))
    )
    if not files:
        sys.exit("ERROR: no files found under site/.")

    print(f"Deploying {len(files)} files from site/ to {user}@{host}:{port}{remote_dir} (explicit FTPS)")
    if dry_run:
        for f in files:
            print(f"  would upload {f.relative_to(SITE_DIR)}")
        print("Dry run only; nothing uploaded.")
        return

    ftps = FTP_TLS()
    ftps.connect(host, port, timeout=30)
    try:
        ftps.login(user, password)
        ftps.prot_p()  # encrypt the data channel too

        made_dirs = set()

        def ensure_remote_dir(path: str) -> None:
            if path in ("", "/", ".") or path in made_dirs:
                return
            ensure_remote_dir(posixpath.dirname(path))
            try:
                ftps.mkd(path)
            except error_perm:
                pass  # already exists
            made_dirs.add(path)

        ensure_remote_dir(remote_dir)
        uploaded = 0
        for local in files:
            rel = local.relative_to(SITE_DIR)
            remote = posixpath.join(remote_dir, rel.as_posix()) if remote_dir != "/" else "/" + rel.as_posix()
            ensure_remote_dir(posixpath.dirname(remote))
            with open(local, "rb") as fh:
                ftps.storbinary(f"STOR {remote}", fh)
            uploaded += 1
            print(f"  uploaded {rel}")
        print(f"Done: {uploaded} files uploaded to {remote_dir}")
    finally:
        try:
            ftps.quit()
        except Exception:
            ftps.close()


if __name__ == "__main__":
    main()
