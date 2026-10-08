#!/usr/bin/env python3
"""
Short clips (about 32 seconds: one verse and one chorus) of candidate music styles,
so the style menu on the form can be chosen by ear. Same lyric in every clip, so
only the style differs. About 400 ElevenLabs credits per clip.

  python3 prayer-song/tools/style_samples.py            # all candidates
  python3 prayer-song/tools/style_samples.py celtic     # one
Output: prayer-song/creative/style-samples/<key>.mp3 and report.md
"""

import re
import sys
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "creative" / "style-samples"
KEY = re.search(r"^ELEVENLABS_API_KEY=(.+)$", (ROOT.parent / ".env").read_text(), re.M).group(1).strip()
API = "https://api.elevenlabs.io/v1"

FEMALE = "warm female lead vocalist, clear diction, every word easy to understand"
MALE = "warm male baritone lead vocalist, clear diction, every word easy to understand"
COMMON = ["prayerful and unhurried", "polished radio quality production"]
NEG = ["rap", "electronic dance", "aggressive", "distorted", "mumbled vocals", "heavy drums", "upbeat party"]

VERSE = "[Verse]\nLord, You knew him before I held him\nYou knew the boy he used to be\nDaniel in his Sunday collar\nServing at the altar, proud as he could be"
CHORUS = "[Chorus]\nLead Daniel home, Lord, lead him home\nDown whatever road he's on\nLeave the light on in Your house for Daniel\nAnd walk him back where he belongs"

# key: (label for the form, voice, style descriptors)
CANDIDATES = {
    "piano":        ("Piano ballad", FEMALE, ["tender Christian piano ballad", "solo grand piano", "soft string pad", "intimate", "68 BPM"]),
    "folk_mass":    ("Folk hymn", FEMALE, ["1970s folk Mass hymn", "two strummed acoustic guitars", "small group of voices singing together in unison on the chorus", "warm and simple", "flute", "76 BPM"]),
    "celtic":       ("Celtic hymn", FEMALE, ["Irish Celtic hymn", "harp", "tin whistle", "soft fiddle", "airy and tender", "66 BPM"]),
    "sacred_choir": ("Sacred choir", FEMALE, ["sacred choral anthem", "cathedral choir of mixed voices singing the lyrics clearly in English", "pipe organ", "cathedral reverb", "solemn and beautiful", "60 BPM"]),
    "classical":    ("Classical soprano", "classically trained soprano soloist, clear diction, every word easy to understand", ["classical sacred aria", "string quartet", "harp", "graceful", "62 BPM"]),
    "worship":      ("Modern worship", MALE, ["contemporary Christian worship ballad", "soft electric guitar swells", "piano", "gentle build", "light drums only on the chorus", "72 BPM"]),
    "spanish":      ("Spanish guitar", MALE, ["Spanish classical guitar hymn", "nylon string guitar", "soft upright bass", "warm and devotional", "70 BPM"]),
}


def words(s):
    return re.findall(r"[a-z']+", re.sub(r"\[[^\]]*\]|\([^)]*\)", " ", s.lower()))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    keys = sys.argv[1:] or list(CANDIDATES)
    want = set(words(VERSE + " " + CHORUS)) - {"verse", "chorus"}
    rows = []
    for k in keys:
        label, voice, style = CANDIDATES[k]
        plan = {"chunks": [
            {"text": "[Intro]", "duration_ms": 4000, "positive_styles": style + [voice] + COMMON + ["instrumental opening"], "negative_styles": NEG, "context_adherence": "high"},
            {"text": VERSE, "duration_ms": 14000, "positive_styles": [voice, "intimate vocal"], "negative_styles": NEG, "context_adherence": "high"},
            {"text": CHORUS, "duration_ms": 14000, "positive_styles": [voice, "fuller arrangement, emotional lift, gentle ending"], "negative_styles": NEG, "context_adherence": "high"},
        ]}
        t0 = time.time()
        r = requests.post(f"{API}/music", params={"output_format": "mp3_44100_128"}, headers={"xi-api-key": KEY},
                          json={"composition_plan": plan, "model_id": "music_v2_5"}, timeout=600)
        if r.status_code != 200:
            print(f"{k}: FAILED {r.status_code} {r.text[:200]}", flush=True)
            rows.append(f"| {label} | {k} | FAILED | | | {r.text[:80]} |")
            continue
        mp3 = OUT / f"{k}.mp3"
        mp3.write_bytes(r.content)
        with open(mp3, "rb") as f:
            s = requests.post(f"{API}/speech-to-text", headers={"xi-api-key": KEY}, data={"model_id": "scribe_v2", "language_code": "en"},
                              files={"file": (mp3.name, f, "audio/mpeg")}, timeout=300)
        text = s.json().get("text", "") if s.status_code == 200 else ""
        heard = words(text)
        recall = len(want & set(heard)) / len(want)
        name = heard.count("daniel")
        print(f"{k}: name {name}/3, words understood {recall:.0%}, {time.time() - t0:.0f}s", flush=True)
        rows.append(f"| {label} | {k} | {name}/3 | {recall:.0%} | {text[:110]} |")
    (OUT / "report.md").write_text("# Style samples\n\n| Style | Key | Name heard | Words understood | Transcript |\n|---|---|---|---|---|\n" + "\n".join(rows) + "\n")


if __name__ == "__main__":
    main()
