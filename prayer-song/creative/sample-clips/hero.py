#!/usr/bin/env python3
"""
Join the raw scene clips into the one silent loop at the top of the sales page.

  python3 hero.py son couple mother herself grandchild father     # slugs in playing order: raw-<slug>.mp4 in this folder

Every clip is brought to a wide 4:3 picture (tall clips are cropped to their upper part, where the faces are),
cross-faded into the next, and the last one cross-fades back into the start of the first. The output is trimmed so
its last frame is its first frame: the loop has no cut and never passes through black.
Writes site/prayer-song/video/hero.mp4 and hero.webp (the first frame, shown while the video loads).
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parents[2] / "site" / "prayer-song" / "video"
FADE = 0.5
W, H = 600, 450


def length(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)], capture_output=True, text=True)
    return float(out.stdout.strip())


def main():
    slugs = sys.argv[1:]
    if len(slugs) < 2:
        sys.exit(__doc__)
    files = [HERE / f"raw-{s}.mp4" for s in slugs]
    for f in files:
        if not f.exists():
            sys.exit(f"missing {f.name}")
    fit = (f"crop='min(iw,ih*4/3)':'min(ih,iw*3/4)':'(iw-ow)/2':'(ih-oh)*0.22',scale={W}:{H}:flags=lanczos,fps=24,format=yuv420p,setsar=1")
    cmd = ["ffmpeg", "-loglevel", "error", "-y"]
    for f in files:
        cmd += ["-i", str(f)]
    cmd += ["-t", "1", "-i", str(files[0])]                       # the start of the first clip again, to fade back into
    n = len(files)
    parts = [f"[{i}:v]{fit}[v{i}]" for i in range(n + 1)]
    run = length(files[0])
    prev = "v0"
    for i in range(1, n + 1):
        parts.append(f"[{prev}][v{i}]xfade=transition=fade:duration={FADE}:offset={run - FADE:.3f}[x{i}]")
        prev = f"x{i}"
        if i < n:
            run += length(files[i]) - FADE
    end = run                                                      # where the fade back into clip one completes
    parts.append(f"[{prev}]trim=start={FADE}:end={end:.3f},setpts=PTS-STARTPTS,format=yuv420p[v]")
    OUT.mkdir(parents=True, exist_ok=True)
    cmd += ["-filter_complex", ";".join(parts), "-map", "[v]", "-an", "-c:v", "libx264", "-profile:v", "main", "-crf", "27",
            "-preset", "slow", "-movflags", "+faststart", str(OUT / "hero.mp4")]
    subprocess.run(cmd, check=True)
    frame = HERE / "hero-frame.png"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(OUT / "hero.mp4"), "-frames:v", "1", str(frame)], check=True)
    subprocess.run(["cwebp", "-quiet", "-q", "78", str(frame), "-o", str(OUT / "hero.webp")], check=True)
    frame.unlink()
    print(f"hero.mp4: {len(slugs)} scenes, {length(OUT / 'hero.mp4'):.1f}s, {(OUT / 'hero.mp4').stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
