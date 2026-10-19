#!/usr/bin/env python3
"""
Phase 0 render test for the Personalized Prayer Song.

Renders each case in tools/test_songs.json with ElevenLabs Music (composition
plan, music_v2_5), transcribes the result with ElevenLabs Speech to Text, and
checks the two things the product lives or dies on:

  1. Is the buyer's name actually sung, and heard as that name?
  2. Do the lyrics survive, or does the model drift off script?

Usage:
  python3 prayer-song/tools/song_test.py --dry              # plan + cost estimate, no API calls
  python3 prayer-song/tools/song_test.py                    # render all cases
  python3 prayer-song/tools/song_test.py --only 01_healing_mother
  python3 prayer-song/tools/song_test.py --phonetic         # sing the phonetic spelling instead

Needs ELEVENLABS_API_KEY in sanctoria-store/.env. The key is never printed.
Output: creative/test-songs/*.mp3 plus report.md and report.json.
"""

import argparse
import difflib
import json
import re
import sys
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
CASES = ROOT / "tools" / "test_songs.json"
OUT = ROOT / "creative" / "test-songs"
API = "https://api.elevenlabs.io/v1"
MUSIC_MODEL = "music_v2_5"
STT_MODELS = ["scribe_v2", "scribe_v1"]  # first one the account accepts wins
PRICE_PER_MIN = 0.15  # USD, ElevenLabs API pricing page, 2026-10-01


def load_key():
    # The key lives in the Sanctoria project .env (one level up), with the other credentials.
    for env in (ROOT.parent / ".env", ROOT / ".env"):
        if not env.exists():
            continue
        for line in env.read_text().splitlines():
            if line.strip().startswith("ELEVENLABS_API_KEY="):
                key = line.split("=", 1)[1].strip().strip('"').strip("'")
                if key:
                    return key
    sys.exit("ELEVENLABS_API_KEY missing or empty. Add it to sanctoria-store/.env and rerun.")


def build_plan(case, phonetic):
    sung = case["name_phonetic"] if phonetic else case["name"]
    voice = case["styles"][1]  # carry the vocal description into every chunk
    chunks = []
    for i, (text, ms, extra) in enumerate(case["sections"]):
        text = text.replace(case["name"], sung)
        styles = (case["styles"] + extra) if i == 0 else (extra + [voice])
        chunks.append({
            "text": text,
            "duration_ms": ms,
            "positive_styles": styles[:50],
            "negative_styles": case["negative"][:50],
            "context_adherence": "high",
        })
    return {"chunks": chunks}


def lyric_text(case):
    lines = []
    for text, _, _ in case["sections"]:
        for ln in text.split("\n"):
            if ln.startswith("[") or ln.startswith("("):
                continue
            lines.append(ln)
    return " ".join(lines)


def words(s):
    return re.findall(r"[a-z']+", s.lower())


def compose(key, plan, dest):
    r = requests.post(
        f"{API}/music",
        params={"output_format": "mp3_44100_128"},
        headers={"xi-api-key": key, "Content-Type": "application/json"},
        json={"composition_plan": plan, "model_id": MUSIC_MODEL},
        timeout=600,
    )
    if r.status_code != 200:
        raise RuntimeError(f"music {r.status_code}: {r.text[:400]}")
    dest.write_bytes(r.content)
    return r.headers.get("song-id", "")


def transcribe(key, mp3):
    last = ""
    for model in STT_MODELS:
        with open(mp3, "rb") as f:
            r = requests.post(
                f"{API}/speech-to-text",
                headers={"xi-api-key": key},
                data={"model_id": model, "language_code": "en"},
                files={"file": (mp3.name, f, "audio/mpeg")},
                timeout=600,
            )
        if r.status_code == 200:
            return r.json().get("text", ""), model
        last = f"stt {model} {r.status_code}: {r.text[:300]}"
    raise RuntimeError(last)


def score(case, transcript):
    heard = words(transcript)
    name = case["name"].lower()
    expected = len(re.findall(rf"\b{re.escape(name)}\b", lyric_text(case).lower()))
    exact = sum(1 for w in heard if w == name)
    close = [w for w in heard if w != name and difflib.SequenceMatcher(None, w, name).ratio() >= 0.75]
    lyric = set(words(lyric_text(case)))
    recall = len(lyric & set(heard)) / max(1, len(lyric))
    return {
        "name_expected": expected,
        "name_exact": exact,
        "name_close": len(close),
        "name_heard_as": sorted(set(close)),
        "lyric_recall": round(recall, 2),
        "pass": exact >= max(1, expected // 2) and recall >= 0.6,
    }


def duration_s(mp3):
    import subprocess
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp3)],
        capture_output=True, text=True,
    ).stdout.strip()
    return float(out) if out else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--only")
    ap.add_argument("--phonetic", action="store_true")
    a = ap.parse_args()

    cases = json.loads(CASES.read_text())
    if a.only:
        cases = [c for c in cases if c["id"] == a.only]
        if not cases:
            sys.exit(f"No case {a.only}")

    total_ms = sum(ms for c in cases for _, ms, _ in c["sections"])
    est = total_ms / 60000 * PRICE_PER_MIN
    print(f"{len(cases)} song(s), {total_ms/1000:.0f}s of audio, est ${est:.2f} music + small STT cost")
    for c in cases:
        secs = sum(ms for _, ms, _ in c["sections"]) / 1000
        bad = [ch for ch in json.dumps(c) if ord(ch) in (0x2013, 0x2014)]
        print(f"  {c['id']}: {c['name']} ({c['name_phonetic']}), {secs:.0f}s, dashes={len(bad)}")
    if a.dry:
        print(json.dumps(build_plan(cases[0], a.phonetic), indent=2)[:1500])
        return

    key = load_key()
    OUT.mkdir(parents=True, exist_ok=True)
    tag = "_phonetic" if a.phonetic else ""
    results = []
    for c in cases:
        mp3 = OUT / f"{c['id']}{tag}.mp3"
        print(f"\n> {c['id']}: rendering...", flush=True)
        t0 = time.time()
        try:
            song_id = compose(key, build_plan(c, a.phonetic), mp3)
            render_s = time.time() - t0
            text, stt_model = transcribe(key, mp3)
            s = score(c, text)
            dur = duration_s(mp3)
        except Exception as e:  # report and keep going, one bad render must not kill the test
            print(f"  FAILED: {e}")
            results.append({"id": c["id"], "error": str(e)})
            continue
        r = {"id": c["id"], "file": mp3.name, "song_id": song_id, "render_s": round(render_s),
             "duration_s": round(dur), "cost_usd": round(dur / 60 * PRICE_PER_MIN, 2),
             "stt_model": stt_model, "transcript": text, **s}
        results.append(r)
        print(f"  {'PASS' if s['pass'] else 'FAIL'}  name {s['name_exact']}/{s['name_expected']} exact, "
              f"{s['name_close']} close {s['name_heard_as']}, lyric recall {s['lyric_recall']}, "
              f"{r['duration_s']}s audio in {r['render_s']}s, ${r['cost_usd']}")

    (OUT / f"report{tag}.json").write_text(json.dumps(results, indent=2))
    md = [f"# Song render test{tag}", "", "| Song | Pass | Name exact | Heard as | Lyric recall | Length | Render time | Cost |",
          "|---|---|---|---|---|---|---|---|"]
    for r in results:
        if "error" in r:
            md.append(f"| {r['id']} | ERROR | | | | | | {r['error'][:60]} |")
            continue
        md.append(f"| {r['id']} | {'yes' if r['pass'] else 'no'} | {r['name_exact']}/{r['name_expected']} | "
                  f"{', '.join(r['name_heard_as']) or ''} | {r['lyric_recall']} | {r['duration_s']}s | "
                  f"{r['render_s']}s | ${r['cost_usd']} |")
    md += ["", "## Transcripts", ""]
    for r in results:
        if "transcript" in r:
            md += [f"### {r['id']}", "", r["transcript"], ""]
    (OUT / f"report{tag}.md").write_text("\n".join(md))
    print(f"\nReport: prayer-song/creative/test-songs/report{tag}.md")


if __name__ == "__main__":
    main()
