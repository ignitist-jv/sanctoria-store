#!/usr/bin/env python3
"""
After a deploy: confirm from the outside that the private parts of the Prayer Song back end
cannot be opened, and the public parts answer. Read only. Run from this machine:

  python3 prayer-song/tools/check_live.py [https://sanctoriastore.com/prayer-song]
"""
import sys
import requests

BASE = (sys.argv[1] if len(sys.argv) > 1 else "https://sanctoriastore.com/prayer-song").rstrip("/")
bad = 0


def check(path, want, why, method="GET"):
    global bad
    try:
        r = requests.request(method, BASE + path, timeout=20, allow_redirects=False)
        code = r.status_code
    except requests.RequestException as e:
        code = f"error {e.__class__.__name__}"
    ok = code in want
    bad += not ok
    print(f"{'ok  ' if ok else 'FAIL'} {path:38} {code}   {why}")


print(f"Checking {BASE}\n")
try:
    age = requests.get(BASE + "/api/status.php?health=1", timeout=20).json().get("worker_ran_seconds_ago")
    ok = age is not None and age < 180
    bad += not ok
    print(f"{'ok  ' if ok else 'FAIL'} cron: the song maker last ran {age} seconds ago" if age is not None else "FAIL cron: the song maker has never run (add the cron job in cPanel)")
except Exception as ex:
    print("FAIL cron: could not ask the server", ex.__class__.__name__); bad += 1
for f in ("lib.php", "pipeline.php", "lyrics.php", "worker.php", "doctor.php", "config.php", "config.sample.php", "pdf.php", "pdf_widths.php", "bonus_docs.php", "copy.json", "data/", "data/log.txt"):
    check(f"/api/{f}", (403, 404), "private: must not open")
check("/HOLD", (403, 404), "the hold marker should not be uploaded")
check("/", (200,), "landing page")
check("/s/", (200,), "song page with no token: the plain 'not found' page")
check("/s/?k=" + "0" * 32, (404,), "a made up token finds nothing")
check("/api/audio.php?k=" + "0" * 32, (404,), "a made up token gets no audio")
check("/api/status.php?k=" + "0" * 32, (404,), "a made up token has no status")
check("/api/bonus.php?f=sheet&k=" + "0" * 32, (404,), "a made up token gets no printable")
check("/admin/", (200,), "admin page: the sign in box (404 means no admin password is set yet)")
check("/admin/?o=" + "0" * 32, (200,), "admin page without signing in: still only the sign in box")
check("/reviews/", (200,), "public reviews page")
check("/s/?find", (200,), "find my song page")
check("/terms.html", (200,), "terms")
check("/privacy.html", (200,), "privacy")
check("/api/ins.php", (200,), "ClickBank can reach the notification endpoint", "POST")
check("/api/lead.php", (405,), "the form endpoint refuses a plain visit")
check("/api/thanks.php", (302,), "thank you page sends an unproven visitor away")
print("\nAll good." if not bad else f"\n{bad} problem(s). Do not take orders until these are fixed.")
sys.exit(1 if bad else 0)
