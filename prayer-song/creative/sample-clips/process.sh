#!/bin/sh
# raw <slug>.mp4 from Higgsfield -> site/prayer-song/video/sample-<slug>.mp4 (silent, small, starts instantly) and its first frame as .webp
# usage: ./process.sh son mother grandchild
cd "$(dirname "$0")" || exit 1
OUT=../../../site/prayer-song/video
mkdir -p "$OUT"
for s in "$@"; do
  ffmpeg -loglevel error -y -i "raw-$s.mp4" -an -vf "scale=600:-2:flags=lanczos,format=yuv420p" -c:v libx264 -profile:v main -crf 27 -preset slow -movflags +faststart "$OUT/sample-$s.mp4"
  ffmpeg -loglevel error -y -i "raw-$s.mp4" -frames:v 1 -vf "scale=600:-2:flags=lanczos" "frame-$s.png" && cwebp -quiet -q 78 "frame-$s.png" -o "$OUT/sample-$s.webp" && rm "frame-$s.png"
  ls -la "$OUT/sample-$s.mp4" "$OUT/sample-$s.webp" | awk '{print $5, $9}'
done
