#!/usr/bin/env python3
"""
One made-up customer, start to finish, with a REAL song from ElevenLabs.

  survey answers -> simulated ClickBank payment -> order + token -> real render
  -> real name check -> private song page -> delivery email (written to disk, not sent)

Not real: the payment (forged with a test secret) and the email send. The lyrics
are written by hand for this one customer, because the automatic lyric writer is
not built yet. Uses about 3,000 ElevenLabs credits.

  python3 prayer-song/tools/demo_order.py          # run and leave the page up to look at
"""

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).parent))
import test_delivery as td                      # reuse the forged-payment helpers
td.PORT = 4174
td.BASE = f"http://localhost:{td.PORT}/prayer-song"

REPO = td.REPO
DATA = REPO / "prayer-song" / "demo-data"       # gitignored, outside site/, never uploaded
KEY = re.search(r"^ELEVENLABS_API_KEY=(.+)$", (REPO / ".env").read_text(), re.M).group(1).strip()
_m = re.search(r"^ANTHROPIC_API_KEY=(.+)$", (REPO / ".env").read_text(), re.M)
CLAUDE = _m.group(1).strip() if _m else ""          # with a Claude key the lyrics are written by the real lyric writer
td.DATA = DATA
td.ENV = {**os.environ, "PS_DATA_DIR": str(DATA), "PS_MOCK": "0", "PS_BASE_URL": td.BASE,
          "PS_CB_SECRET": td.SECRET, "PS_ELEVENLABS_KEY": KEY, "PS_ANTHROPIC_KEY": CLAUDE}

CUSTOMER = {
    "email": "margaret.doyle@example.com", "buyer": "Margaret",
    "who": "son", "name": "Daniel", "name_phonetic": "",
    "intention": "return", "style": "acoustic", "voice": "female",
    "note": "He was an altar boy at Saint Brigid's and he still calls me every Sunday.",
}
RECEIPT = "DEMO" + str(int(time.time()))[-6:]

# Hand written for this customer, in the locked ten part structure. Bridge: Luke 15:20, Douay-Rheims.
CHORUS = ["Lead Daniel home, Lord, lead him home", "Down whatever road he's on", "Leave the light on in Your house for Daniel",
          "And walk him back where he belongs", "Daniel, You have called him by his name", "Lead Daniel home"]
LYRICS = {
    "title": "Lead Daniel Home", "verse": "Luke 15:20", "written_by": "hand, for the demo",
    "sections": [
        {"tag": "Verse 1", "lines": ["Lord, You knew him before I held him", "You knew the boy he used to be",
                                     "Daniel in his Sunday collar", "Serving at the altar, proud as he could be"]},
        {"tag": "Chorus", "lines": CHORUS},
        {"tag": "Verse 2", "lines": ["He still calls me every Sunday", "And I can hear the miles between",
                                     "I don't have the words to reach him", "So I'm asking You to say what I mean"]},
        {"tag": "Chorus", "lines": CHORUS},
        {"tag": "Bridge", "lines": ["When he was yet a great way off", "His father saw him, and was moved",
                                    "And running to him, fell upon his neck", "Lord, be that Father to my son"]},
        {"tag": "Verse 3", "lines": ["I'm not asking for a miracle by morning", "I'm not asking You to make him who he's not",
                                     "Just stay close in the place where he is standing", "And remind him of the faith that he forgot"]},
        {"tag": "Final Chorus", "lines": CHORUS + ["Lead Daniel home, Lord, in Your time", "I will leave him in Your hands"]},
        {"tag": "Outro", "lines": ["Amen, amen", "For Daniel, amen"]},
    ],
}


def step(n, text):
    print(f"\n[{n}] {text}", flush=True)


def main():
    subprocess.run(["pkill", "-f", f"php -S localhost:{td.PORT}"])
    DATA.mkdir(exist_ok=True)
    server = subprocess.Popen(["php", "-S", f"localhost:{td.PORT}", "-t", str(REPO / "site")], env=td.ENV,
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(40):
        try:
            requests.get(f"{td.BASE}/s/", timeout=1)
            break
        except requests.ConnectionError:
            time.sleep(0.15)

    step(1, "Margaret fills in the form")
    lead = requests.post(f"{td.BASE}/api/lead.php", json=CUSTOMER).json()
    print(f"    answers saved, lead id {lead['lead'][:8]}...")

    step(2, f"She pays (simulated ClickBank sale, receipt {RECEIPT})")
    print("    notification:", td.sale(RECEIPT, CUSTOMER["email"], lead["lead"]))
    token = td.thanks(RECEIPT, lid=lead["lead"])
    url = f"{td.BASE}/s/?k={token}"
    print(f"    order created, token {token[:8]}... ({len(token)} characters)")
    print(f"    her private page: {url}")
    status = requests.get(f"{td.BASE}/api/status.php", params={"k": token}).json()
    print(f"    page status right after paying: {status['status']}")

    order_file = DATA / "orders" / f"{token}.json"
    if CLAUDE:
        step(3, "Lyrics: left to the real lyric writer (Claude), as on the live server")
    else:
        step(3, "Lyrics (no Claude key in .env, so hand written lyrics are placed on the order)")
        o = json.loads(order_file.read_text())
        o["lyrics"], o["title"] = LYRICS, LYRICS["title"]
        order_file.write_text(json.dumps(o, indent=1))
        print(f"    \"{LYRICS['title']}\", {sum(len(s['lines']) for s in LYRICS['sections'])} lines")

    step(4, "The worker makes the song (real ElevenLabs render and name check)")
    t0 = time.time()
    out = subprocess.run(["php", str(REPO / "site/prayer-song/api/worker.php")], env=td.ENV, capture_output=True, text=True)
    print(f"    worker: {out.stdout.strip() or out.stderr.strip()}   ({time.time() - t0:.0f}s)")

    o = json.loads(order_file.read_text())
    c = o.get("check") or {}
    step(5, "Result")
    print(f"    status: {o['status']}, attempts: {o['attempts']}")
    if o.get("lyrics"):
        print(f"    title: {o['lyrics']['title']}   written by: {o['lyrics'].get('written_by')}")
        for sec in o["lyrics"]["sections"]:
            print(f"      [{sec['tag']}] " + " / ".join(sec["lines"]))
    if o.get("hold_reason"):
        print(f"    HELD: {o['hold_reason']}")
    print(f"    name sung: {c.get('name_heard')}/{c.get('name_expected')}, lyrics kept: {c.get('recall')}, "
          f"added words: {c.get('extra')}, misheard as: {c.get('heard_as')}")
    mp3 = DATA / "songs" / f"{token}.mp3"
    if mp3.exists():
        dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp3)],
                             capture_output=True, text=True).stdout.strip()
        print(f"    song file: {mp3.stat().st_size / 1e6:.1f} MB, {float(dur):.0f}s")
    au = requests.get(f"{td.BASE}/api/audio.php", params={"k": token})
    print(f"    plays from her page: {au.status_code == 200}")
    mail = DATA / "outbox" / f"ready-{token}.txt"
    print(f"    email written: {mail.exists()}  (emailed flag: {o['emailed']})")
    if mail.exists():
        print("\n" + "-" * 60 + "\n" + mail.read_text() + "-" * 60)
    for line in o["log"]:
        print("    log:", line[:230])
    print(f"\nPAGE  {url}\nTOKEN {token}\nSONG  {mp3}\nserver pid {server.pid}")


if __name__ == "__main__":
    main()
