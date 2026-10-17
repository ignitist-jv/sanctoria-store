#!/usr/bin/env python3
"""
End to end test of the Prayer Song delivery chain, on this machine, in practice mode.

No ElevenLabs, no ClickBank, no email provider: the render is a placeholder tone, the
ClickBank notification is forged with a test secret, and emails are written to disk.
What it proves is the plumbing: every buyer gets their own token, and only their own song.

  python3 prayer-song/tools/test_delivery.py           # run, then clean up
  python3 prayer-song/tools/test_delivery.py --keep    # leave the server running to click around
"""

import hashlib
import hmac
import html
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parents[2]
PORT = 4176
BASE = f"http://localhost:{PORT}/prayer-song"
SECRET = "TESTSECRETKEY123"
DATA = Path(tempfile.mkdtemp(prefix="ps-test-data-"))
ENV = {**os.environ, "PS_DATA_DIR": str(DATA), "PS_MOCK": "1", "PS_BASE_URL": BASE, "PS_CB_SECRET": SECRET, "PS_SEND_AFTER": "0"}
WHSEC = "whsec_test_not_a_real_secret"
# the ClickMagick report is pointed back at this test server, which needs a second worker to answer while it waits
ENV.update({"PHP_CLI_SERVER_WORKERS": "4", "PS_CM_POSTBACK": BASE + "/api/status.php?health=1", "PS_STRIPE_WHSEC": WHSEC, "PS_STRIPE_LINKS": json.dumps({"plink_song": "song", "plink_express": "express"})})


def stripe_event(etype, obj, secret=WHSEC, age=0):
    """POST a webhook signed the way Stripe signs it: HMAC-SHA256 of "<t>.<payload>" with the endpoint secret."""
    payload = json.dumps({"id": "evt_" + str(time.time_ns()), "type": etype, "data": {"object": obj}})
    t = str(int(time.time()) - age)
    sig = hmac.new(secret.encode(), f"{t}.{payload}".encode(), hashlib.sha256).hexdigest()
    return requests.post(f"{BASE}/api/stripe.php", data=payload, headers={"Stripe-Signature": f"t={t},v1={sig}", "Content-Type": "application/json"})


def paid_session(sid, pi, lid, email, link="plink_song", status="paid"):
    return {"id": sid, "object": "checkout.session", "payment_link": link, "payment_status": status, "payment_intent": pi,
            "client_reference_id": lid, "customer_details": {"email": email, "name": "Mary Stripe"}}   # 0: the rest of the run does not sit out the send delay
ADMIN_PW = "test-password-not-used-anywhere-real"
ENV["PS_ADMIN_HASH"] = subprocess.run(["php", "-r", "echo password_hash($argv[1], PASSWORD_DEFAULT);", ADMIN_PW], capture_output=True, text=True).stdout

results = []


def check(name, ok, detail=""):
    results.append(ok)
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"   [{detail}]" if detail and not ok else ""))


def ins_body(notification):
    """Encrypt the way ClickBank INS v6+ does: AES-256-CBC, key = first 32 chars of sha1(secret)."""
    php = ('$k=substr(sha1($argv[1]),0,32);$iv=random_bytes(16);'
           'echo json_encode(["notification"=>base64_encode(openssl_encrypt($argv[2],"AES-256-CBC",$k,OPENSSL_RAW_DATA,$iv)),'
           '"iv"=>base64_encode($iv)]);')
    return subprocess.run(["php", "-r", php, SECRET, json.dumps(notification)], capture_output=True, text=True).stdout


def sale(receipt, email, lid=None, item="prayersong-1", kind="SALE"):
    n = {"transactionType": kind, "receipt": receipt, "customer": {"billing": {"email": email, "fullName": "Mary Test"}},
         "lineItems": [{"itemNo": item}], "vendorVariables": {"lid": lid} if lid else {}}
    return requests.post(f"{BASE}/api/ins.php", data=ins_body(n)).text


def cbpop(receipt, t, item):
    return hashlib.sha1(f"{SECRET}|{receipt}|{t}|{item}".encode()).hexdigest()[:8].upper()


def thanks(receipt, item="prayersong-1", pop=None, lid=None):
    t = str(int(time.time()))
    q = {"cbreceipt": receipt, "item": item, "time": t, "cbpop": pop or cbpop(receipt, t, item), "cemail": "", "cname": "Mary"}
    if lid:
        q["lid"] = lid
    r = requests.get(f"{BASE}/api/thanks.php", params=q, allow_redirects=False)
    m = re.search(r"k=([a-f0-9]{32})", r.headers.get("Location", ""))
    return m.group(1) if m else None


def worker():
    return subprocess.run(["php", str(REPO / "site/prayer-song/api/worker.php")], env=ENV, capture_output=True, text=True).stdout


def lead(email, name, **kw):
    body = {"email": email, "buyer": "Mary", "who": "mother", "name": name, "intention": "healing", "style": "hymn", "voice": "female", **kw}
    return requests.post(f"{BASE}/api/lead.php", json=body).json()


def main():
    server = subprocess.Popen(["php", "-S", f"localhost:{PORT}", "-t", str(REPO / "site")], env=ENV,
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        for _ in range(40):
            try:
                requests.get(f"{BASE}/s/", timeout=1)
                break
            except requests.ConnectionError:
                time.sleep(0.15)

        print("\n1. Survey, payment, song, email")
        a = lead("mary@example.com", "Siobhan", name_phonetic="shiv-AWN")
        check("survey answers saved under a lead id", a.get("ok") and re.fullmatch(r"[a-f0-9]{32}", a.get("lead", "")) is not None, str(a))
        check("ClickBank notification accepted", sale("RCPT1001", "mary@example.com", a["lead"]) == "ok")
        tok_a = thanks("RCPT1001", lid=a["lead"])
        check("thank you page sends her to her own token", tok_a is not None)
        page = requests.get(f"{BASE}/s/", params={"k": tok_a})
        check("song page says the song is being made", "Siobhan's prayer song is being made" in html.unescape(page.text))
        mk = html.unescape(page.text)
        check("the being-made page tells her the exact subject line and sender to watch for",
              'with the subject "Siobhan\'s prayer song is ready"' in mk and "admin@sanctoriastore.com" in mk and "yours to keep" in mk)
        check("no audio before it is ready", requests.get(f"{BASE}/api/audio.php", params={"k": tok_a}).status_code == 404)
        check("no printables before it is ready", requests.get(f"{BASE}/api/bonus.php", params={"k": tok_a, "f": "sheet"}).status_code == 404)
        out = worker()
        check("worker made the song", f"{tok_a} ready" in out, out)
        page = requests.get(f"{BASE}/s/", params={"k": tok_a})
        check("song page now has the player and the name", "<audio" in page.text and "Siobhan" in page.text)
        check("her page states how the charge appears and where to get help (statement name and help)",
              "bank statement as" in page.text and "RCPT1001" in page.text and "support@sanctoriastore.com" in page.text)
        check("song page shows the lyrics", "Hold Siobhan close" in page.text)
        au = requests.get(f"{BASE}/api/audio.php", params={"k": tok_a})
        check("song plays (audio served)", au.status_code == 200 and au.headers["Content-Type"] == "audio/mpeg" and len(au.content) > 500)
        rng = requests.get(f"{BASE}/api/audio.php", params={"k": tok_a}, headers={"Range": "bytes=0-99"})
        check("seeking works (needed for iPhone)", rng.status_code == 206 and len(rng.content) == 100)
        for f in ("sheet", "card", "companion"):
            pdf = requests.get(f"{BASE}/api/bonus.php", params={"k": tok_a, "f": f})
            check(f"printable '{f}' is a real PDF", pdf.status_code == 200 and pdf.content[:5] == b"%PDF-" and pdf.content.rstrip().endswith(b"%%EOF")
                  and pdf.headers.get("Content-Type") == "application/pdf", f"{pdf.status_code} {len(pdf.content)} bytes")
        check("a made up token gets no printable", requests.get(f"{BASE}/api/bonus.php", params={"k": "f" * 32, "f": "sheet"}).status_code == 404)
        check("an unknown printable is refused", requests.get(f"{BASE}/api/bonus.php", params={"k": tok_a, "f": "../lib"}).status_code == 404)
        check("the song page lists the three printables", requests.get(f"{BASE}/s/", params={"k": tok_a}).text.count("api/bonus.php?k=") == 3)
        dl = requests.get(f"{BASE}/api/audio.php", params={"k": tok_a, "dl": 1})
        check("download button gives an MP3 file", 'attachment; filename="A Prayer for Siobhan.mp3"' in dl.headers.get("Content-Disposition", ""),
              dl.headers.get("Content-Disposition", ""))
        mail = (DATA / "outbox" / f"ready-{tok_a}.txt")
        txt = mail.read_text() if mail.exists() else ""
        check("ready email written, to her address", "To: mary@example.com" in txt and "Subject: Siobhan's prayer song is ready" in txt, txt[:200])
        check("email carries her private link", f"{BASE}/s/?k={tok_a}" in txt)

        print("\n2. Each buyer gets only their own song")
        b = lead("anne@example.com", "Joaquin", who="passed", intention="grief")
        sale("RCPT2002", "anne@example.com", b["lead"])
        tok_b = thanks("RCPT2002")
        worker()
        pb = requests.get(f"{BASE}/s/", params={"k": tok_b}).text
        check("second buyer has a different token", tok_b and tok_b != tok_a)
        check("second page names Joaquin, never Siobhan", "Joaquin" in pb and "Siobhan" not in pb)
        check("first page still names Siobhan, never Joaquin", "Joaquin" not in requests.get(f"{BASE}/s/", params={"k": tok_a}).text)
        txt_b = (DATA / "outbox" / f"ready-{tok_b}.txt").read_text()
        check("second email goes to the second buyer with the second link", "To: anne@example.com" in txt_b and tok_b in txt_b and tok_a not in txt_b)

        print("\n3. The same payment never makes two songs")
        sale("RCPT1001", "mary@example.com", a["lead"])
        sale("RCPT1001", "mary@example.com", a["lead"])
        check("repeated notification returns the same token", thanks("RCPT1001") == tok_a)
        check("still exactly two orders", len(list((DATA / "orders").glob("*.json"))) == 2)

        print("\n4. Paid without filling in the survey")
        sale("RCPT3003", "stranger@example.com")
        tok_c = thanks("RCPT3003")
        pc = requests.get(f"{BASE}/s/", params={"k": tok_c}).text
        check("page asks for the answers", "One thing is still needed" in pc and f"order={tok_c}" in pc)
        r = lead("stranger@example.com", "Nevaeh", who="grandchild", intention="protection", order=tok_c)
        check("answers attach to the paid order", r.get("song", "").endswith(tok_c), str(r))
        worker()
        check("that song is then made", "Nevaeh" in requests.get(f"{BASE}/s/", params={"k": tok_c}).text and
              (DATA / "songs" / f"{tok_c}.mp3").exists())

        print("\n5. Nobody else can get in")
        check("a made up token finds nothing", requests.get(f"{BASE}/s/", params={"k": "0" * 32}).status_code == 404)
        check("a made up token gets no audio", requests.get(f"{BASE}/api/audio.php", params={"k": "f" * 32}).status_code == 404)
        check("thank you page refuses a forged proof of purchase", thanks("RCPT9999", pop="DEADBEEF") is None)
        check("forged proof created no order", len(list((DATA / "orders").glob("*.json"))) == 3)
        check("a notification with the wrong secret is ignored",
              requests.post(f"{BASE}/api/ins.php", data='{"notification":"AAAA","iv":"AAAA"}').text == "ok" and
              len(list((DATA / "orders").glob("*.json"))) == 3)
        check("other Sanctoria products are ignored", sale("RCPT7777", "x@example.com", item="bracelet-1") == "ok" and
              len(list((DATA / "orders").glob("*.json"))) == 3)
        bad = requests.post(f"{BASE}/api/lead.php", json={"email": "not-an-email", "who": "mother", "name": "A", "intention": "healing"})
        check("bad email is rejected", bad.status_code == 422)
        hack = lead("h@example.com", "<script>alert(1)</script>Ann")
        sale("RCPT4004", "h@example.com", hack["lead"])
        tok_h = thanks("RCPT4004")
        check("typed code cannot run on the page", "<script>alert" not in requests.get(f"{BASE}/s/", params={"k": tok_h}).text)

        print("\n5b. Arriving from checkout when the purchase cannot be confirmed")
        r = requests.get(f"{BASE}/api/thanks.php", params={"cbreceipt": "RCPT9999", "item": "prayersong-1", "time": "1", "cbpop": "BADBAD00", "cemail": "x@example.com"}, allow_redirects=True)
        tx = html.unescape(r.text)
        check("she is thanked and told to watch for the email, never shown 'not found'",
              "Your prayer song is on its way" in tx and "prayer song is ready" in tx and "could not find" not in tx and "bank statement as" in tx and "RCPT9999" in tx)
        check("no order is created from an unconfirmed purchase", not any("RCPT9999" in f.read_text() for f in (DATA / "orders").glob("*.json")))
        check("a stray visit to the thank you address goes to 'send my link again'",
              "Send the song link again" in html.unescape(requests.get(f"{BASE}/api/thanks.php", allow_redirects=True).text))

        print("\n6. Refund")
        sale("RCPT1001", "mary@example.com", kind="RFND")
        o = json.loads((DATA / "orders" / f"{tok_a}.json").read_text())
        check("refund is recorded and the song still plays", o["refunded"] is True and
              requests.get(f"{BASE}/api/audio.php", params={"k": tok_a}).status_code == 200)

        print("\n7. Find my song (lost link)")
        mail_a = DATA / "outbox" / f"ready-{tok_a}.txt"
        mail_a.unlink()
        r1 = requests.post(f"{BASE}/api/find.php", json={"email": "Mary@Example.com"})
        check("her link is sent to her inbox again", r1.json() == {"ok": True} and mail_a.exists() and tok_a in mail_a.read_text())
        r2 = requests.post(f"{BASE}/api/find.php", json={"email": "nobody@example.com"})
        check("an unknown address gets the very same answer", r2.status_code == 200 and r2.json() == r1.json())
        check("the link itself is never shown on screen", tok_a not in r1.text)
        check("not an email address is refused", requests.post(f"{BASE}/api/find.php", json={"email": "x"}).status_code == 422)
        check("the find page opens", "Send the song link again" in requests.get(f"{BASE}/s/", params={"find": 1}).text)

        print("\n8. Putting a song right by hand")
        wk = str(REPO / "site/prayer-song/api/worker.php")
        out = subprocess.run(["php", wk, "--remake", tok_a, "shiv-AWN"], env=ENV, capture_output=True, text=True).stdout
        o = json.loads((DATA / "orders" / f"{tok_a}.json").read_text())
        check("a remake request puts the song back in the queue", "queued" in out and o["status"] == "queued" and
              o["answers"]["name_phonetic"] == "shiv-AWN")
        check("while it is remade the page says so, and no audio is served",
              requests.get(f"{BASE}/api/audio.php", params={"k": tok_a}).status_code == 404)
        worker()
        o = json.loads((DATA / "orders" / f"{tok_a}.json").read_text())
        check("the remade song is delivered again", o["status"] == "ready" and o["emailed"] is True and
              any('sung as \"shiv-AWN\"' in line for line in o["log"]))
        shown = subprocess.run(["php", wk, "--show", tok_a], env=ENV, capture_output=True, text=True).stdout
        check("an order can be inspected", '"receipt": "RCPT1001"' in shown)

        print("\n9. A real order is never given the practice lyric")
        z = lead("zoe@example.com", "Agnes")
        sale("RCPT5005", "zoe@example.com", z["lead"])
        tok_z = thanks("RCPT5005")
        real = {**ENV, "PS_MOCK": "0", "PS_ANTHROPIC_KEY": "", "PS_ELEVENLABS_KEY": ""}
        subprocess.run(["php", wk], env=real, capture_output=True, text=True)
        o = json.loads((DATA / "orders" / f"{tok_z}.json").read_text())
        check("with no lyric writer connected the order is held for review, not faked",
              o["status"] == "review" and o["lyrics"] is None and "Claude key" in o.get("hold_reason", ""))
        pz = html.unescape(requests.get(f"{BASE}/s/", params={"k": tok_z}).text)
        check("the buyer sees the honest 'taking longer' page", "taking longer" in pz and "<audio" not in pz)

        print("\n9a. A song for two names")
        t2 = lead("two@example.com", "Anna", name2="Tomasz", who2="husband", who="daughter", intention="marriage")
        sale("RCPT7007", "two@example.com", t2["lead"])
        tok_2 = thanks("RCPT7007")
        worker()
        o = json.loads((DATA / "orders" / f"{tok_2}.json").read_text())
        words = " ".join(l for sec in o["lyrics"]["sections"] for l in sec["lines"])
        check("both names are kept on the order and written into the song", o["answers"]["name2"] == "Tomasz" and o["answers"]["who2"] == "husband"
              and "Anna" in words and "Tomasz" in words and o["status"] == "ready")
        check("the check counts each name on its own", o["check"]["pass"] is True and o["check"]["name_expected"] >= 2)
        mail2 = (DATA / "outbox" / f"ready-{tok_2}.txt").read_text()
        check("her email and page name both people", "Anna and Tomasz" in mail2 and "Anna and Tomasz" in html.unescape(requests.get(f"{BASE}/s/", params={"k": tok_2}).text))
        check("the printables are made for two names", requests.get(f"{BASE}/api/bonus.php", params={"k": tok_2, "f": "card"}).content[:5] == b"%PDF-")
        solo = lead("solo@example.com", "Bernadette", who="myself", name2="Someone", who2="friend")
        sale("RCPT7008", "solo@example.com", solo["lead"])
        o = json.loads((DATA / "orders" / f"{thanks('RCPT7008')}.json").read_text())
        check("a song for herself, or for someone who has passed, carries one name only", o["answers"]["name2"] == "" and o["answers"]["who2"] == "")

        print("\n9b. A buyer leaves a review")
        rv = f"{BASE}/api/review.php"
        page = requests.get(f"{BASE}/s/", params={"k": tok_a}).text
        check("the song page asks for a review, with the permission box unticked", 'id="fbform"' in page and 'id="fbshare">' in page and "Send My Words" in page)
        check("a review needs stars", requests.post(rv, json={"k": tok_a, "stars": 0, "text": "x"}).status_code == 422)
        check("a made up token cannot leave a review", requests.post(rv, json={"k": "f" * 32, "stars": 5}).status_code == 404)
        check("no review on a song that is not ready", requests.post(rv, json={"k": tok_z, "stars": 5}).status_code == 404)
        ok = requests.post(rv, json={"k": tok_a, "stars": 5, "text": "Played it at the kitchen table. <b>Lovely</b>", "name": "Mary, Ohio", "share": False})
        o = json.loads((DATA / "orders" / f"{tok_a}.json").read_text())
        check("a review is saved on her order, private by default", ok.status_code == 200 and o["review"]["stars"] == 5 and o["review"]["share"] is False
              and "share_at" not in o["review"])
        page = requests.get(f"{BASE}/s/", params={"k": tok_a}).text
        check("her page then thanks her, and shows her words safely for changing", 'id="fbform" novalidate hidden' in page and "&lt;b&gt;Lovely&lt;/b&gt;" in page and "<b>Lovely</b>" not in page)
        requests.post(rv, json={"k": tok_a, "stars": 4, "text": "Changed my mind a little.", "name": "", "share": True})
        o = json.loads((DATA / "orders" / f"{tok_a}.json").read_text())
        check("she can change it and give permission, which is recorded with its wording and date",
              o["review"]["stars"] == 4 and o["review"]["share"] is True and o["review"]["share_at"] > 0 and "Sanctoria may show" in o["review"]["share_text"])
        check("permission without a typed name uses her first name from the order", o["review"]["name"] == (o.get("buyer") or ""))
        requests.post(rv, json={"k": tok_a, "stars": 4, "text": "Changed my mind a little.", "share": False})
        check("unticking the box is recorded as a withdrawal", "share_withdrawn" in json.loads((DATA / "orders" / f"{tok_a}.json").read_text())["review"])

        print("\n10. The owner's admin page")
        adm = f"{BASE}/admin/"
        csrf_of = lambda text: re.search(r'name="csrf" value="([a-f0-9]{32})"', text).group(1)
        bare = subprocess.Popen(["php", "-S", f"localhost:{PORT + 1}", "-t", str(REPO / "site")], env={**ENV, "PS_ADMIN_HASH": ""},
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(0.8)
        check("with no password set the admin page does not exist", requests.get(f"http://localhost:{PORT + 1}/prayer-song/admin/").status_code == 404)
        bare.terminate()
        anon = requests.get(adm)
        check("a visitor sees only a sign in box, no orders", "Sign in" in anon.text and "mary@example.com" not in anon.text and "RCPT1001" not in anon.text)
        check("a held song cannot be heard without signing in",
              "audio/mpeg" not in requests.get(adm, params={"o": tok_a, "audio": "final"}).headers.get("Content-Type", ""))
        check("an action without signing in changes nothing",
              requests.post(adm, data={"act": "retry", "o": tok_a, "csrf": "0" * 32}).status_code == 200 and
              json.loads((DATA / "orders" / f"{tok_a}.json").read_text())["status"] == "ready")
        S = requests.Session()
        check("a wrong password is refused", "not right" in S.post(adm, data={"password": "guess"}).text)
        home = S.post(adm, data={"password": ADMIN_PW})
        check("the right password opens the list of orders", "Sign out" in home.text and "zoe@example.com" in home.text and
              "mary@example.com" in S.get(adm, params={"view": "all"}).text)
        check("the held order is under 'Needs you'", "Needs you 1" in re.sub(r"\s+", " ", home.text) and "Claude key" in html.unescape(home.text))
        one = S.get(adm, params={"o": tok_a})
        check("an order page shows the buyer, the lyrics and the player", "RCPT1001" in one.text and "Hold Siobhan close" in one.text and "audio=final" in one.text)
        check("the owner sees her review, and that it is private", "Her review" in one.text and "private" in one.text and
              "Reviews 1" in re.sub(r"\s+", " ", S.get(adm, params={"view": "reviews"}).text))
        au = S.get(adm, params={"o": tok_a, "audio": "final"})
        check("the owner can listen", au.status_code == 200 and au.headers["Content-Type"] == "audio/mpeg" and len(au.content) > 500)
        bad = S.post(adm, data={"act": "remake", "o": tok_a, "say": "SHIV-awn", "csrf": "f" * 32})
        check("a forged request is refused", bad.status_code == 400 and json.loads((DATA / "orders" / f"{tok_a}.json").read_text())["status"] == "ready")
        S.post(adm, data={"act": "remake", "o": tok_a, "say": "SHIV-awn", "csrf": csrf_of(one.text)})
        o = json.loads((DATA / "orders" / f"{tok_a}.json").read_text())
        check("Remake puts the song back in the queue with the new spelling", o["status"] == "queued" and o["answers"]["name_phonetic"] == "SHIV-awn")
        worker()
        o = json.loads((DATA / "orders" / f"{tok_a}.json").read_text())
        check("the remade song is delivered", o["status"] == "ready" and o["emailed"] is True)
        # a song held after failing its check: an attempt recording exists, and the owner releases it
        o["status"], o["hold_reason"], o["emailed"], o["attempts"] = "review", "the song failed its check 3 times", False, 3
        (DATA / "orders" / f"{tok_a}.json").write_text(json.dumps(o))
        os.replace(DATA / "songs" / f"{tok_a}.mp3", DATA / "songs" / f"{tok_a}.attempt3.mp3")
        held = S.get(adm, params={"o": tok_a})
        check("a held song offers 'Send attempt 3' and can be heard", "Send attempt 3" in held.text and
              S.get(adm, params={"o": tok_a, "audio": "3"}).headers.get("Content-Type") == "audio/mpeg")
        check("the buyer cannot hear a held song", requests.get(f"{BASE}/api/audio.php", params={"k": tok_a}).status_code == 404)
        S.post(adm, data={"act": "approve", "o": tok_a, "n": "3", "csrf": csrf_of(held.text)})
        o = json.loads((DATA / "orders" / f"{tok_a}.json").read_text())
        check("releasing it delivers the song and the email", o["status"] == "ready" and o["emailed"] is True and
              requests.get(f"{BASE}/api/audio.php", params={"k": tok_a}).status_code == 200)
        print("\n11. The public reviews page")
        pub = f"{BASE}/reviews/"
        check("with no approved review the page says so, and counts none", "There are no reviews here yet" in requests.get(pub).text and
              requests.get(pub, params={"count": 1}).json() == {"n": 0})
        requests.post(f"{BASE}/api/review.php", json={"k": tok_a, "stars": 5, "text": "It was played at the kitchen table.", "name": "Mary, Ohio", "share": False})
        one = S.get(adm, params={"o": tok_a})
        S.post(adm, data={"act": "publish", "o": tok_a, "csrf": csrf_of(one.text)})
        check("a review without permission cannot be put on the public page", requests.get(pub, params={"count": 1}).json() == {"n": 0})
        requests.post(f"{BASE}/api/review.php", json={"k": tok_a, "stars": 5, "text": "It was played at the kitchen table.", "name": "Mary, Ohio", "share": True})
        check("permission alone does not publish it: TS must approve", requests.get(pub, params={"count": 1}).json() == {"n": 0})
        one = S.get(adm, params={"o": tok_a})
        S.post(adm, data={"act": "publish", "o": tok_a, "csrf": csrf_of(one.text)})
        page = requests.get(pub).text
        check("once approved it shows her words and chosen name, and nothing else of hers",
              "It was played at the kitchen table." in page and "Mary, Ohio" in page and "mary@example.com" not in page and "RCPT1001" not in page
              and tok_a not in page and "Siobhan" not in page and requests.get(pub, params={"count": 1}).json() == {"n": 1})
        requests.post(f"{BASE}/api/review.php", json={"k": tok_a, "stars": 5, "text": "Changed words.", "name": "Mary, Ohio", "share": True})
        check("if she changes it, it comes off the page until it is read again", requests.get(pub, params={"count": 1}).json() == {"n": 0})
        one = S.get(adm, params={"o": tok_a})
        S.post(adm, data={"act": "publish", "o": tok_a, "csrf": csrf_of(one.text)})
        requests.post(f"{BASE}/api/review.php", json={"k": tok_a, "stars": 5, "text": "Changed words.", "name": "Mary, Ohio", "share": False})
        check("if she withdraws permission, it comes off the page", requests.get(pub, params={"count": 1}).json() == {"n": 0} and "Changed words." not in requests.get(pub).text)
        print("\n13. The send delay: made at once, shown and emailed later (sooner with express)")
        slow = {**ENV, "PS_SEND_AFTER": "7200"}                       # standard 2 hours, express 1 hour
        wk = lambda: subprocess.run(["php", str(REPO / "site/prayer-song/api/worker.php")], env=slow, capture_output=True, text=True).stdout
        od = lambda t: json.loads((DATA / "orders" / f"{t}.json").read_text())
        def back(t, secs):
            o = od(t); o["created"] -= secs; (DATA / "orders" / f"{t}.json").write_text(json.dumps(o))
        w1 = lead("wait1@example.com", "daniel")
        sale("RCPT7001", "wait1@example.com", w1["lead"])
        t1 = thanks("RCPT7001", lid=w1["lead"])
        w2 = lead("wait2@example.com", "ANNA")
        n = {"transactionType": "SALE", "receipt": "RCPT7002", "customer": {"billing": {"email": "wait2@example.com", "fullName": "Mary Test"}},
             "lineItems": [{"itemNo": "prayersong-1"}, {"itemNo": "express-1"}], "vendorVariables": {"lid": w2["lead"]}}
        requests.post(f"{BASE}/api/ins.php", data=ins_body(n))
        t2 = thanks("RCPT7002", lid=w2["lead"])
        check("a name typed in small letters or capitals is given normal capitals", od(t1)["answers"]["name"] == "Daniel" and od(t2)["answers"]["name"] == "Anna")
        check("the express order bump marks the order express", od(t2).get("express") is True and not od(t1).get("express"))
        wk()
        check("the song is made at once but held: not ready, not emailed", od(t1)["status"] == "waiting" and od(t1)["emailed"] is False
              and (DATA / "songs" / f"{t1}.mp3").is_file())
        check("while it waits her page still says it is being made, with no audio",
              "prayer song is being made" in html.unescape(requests.get(f"{BASE}/s/", params={"k": t1}).text)
              and requests.get(f"{BASE}/api/audio.php", params={"k": t1}).status_code == 404
              and requests.get(f"{BASE}/api/status.php", params={"k": t1}).json()["status"] == "making")
        back(t1, 3700); back(t2, 3700)                                # 1 hour 2 minutes after the order
        wk()
        check("after an hour the express song is sent and the standard one still waits",
              od(t2)["status"] == "ready" and od(t2)["emailed"] is True and od(t1)["status"] == "waiting")
        back(t1, 3600)
        wk()
        check("after two hours the standard song is sent", od(t1)["status"] == "ready" and od(t1)["emailed"] is True
              and requests.get(f"{BASE}/api/audio.php", params={"k": t1}).status_code == 200)
        w3 = lead("wait3@example.com", "Peter")
        sale("RCPT7003", "wait3@example.com", w3["lead"])
        t3 = thanks("RCPT7003", lid=w3["lead"])
        wk()
        one = S.get(adm, params={"o": t3})
        S.post(adm, data={"act": "sendnow", "o": t3, "csrf": csrf_of(one.text)})
        check("the owner can send a waiting song now from the admin page", "Send now" in one.text and od(t3)["status"] == "ready" and od(t3)["emailed"] is True)

        print("\n14. Stripe: payment links, webhook, express and refunds")
        od = lambda t: json.loads((DATA / "orders" / f"{t}.json").read_text())
        tok_of = lambda pi: (DATA / "idx" / ("receipt-" + hashlib.sha1(f"{pi}|prayersong-1".encode()).hexdigest())).read_text().strip()
        s1 = lead("stripe1@example.com", "Bernadette")
        r = stripe_event("checkout.session.completed", paid_session("cs_test_aaa111", "pi_test_111", s1["lead"], "stripe1@example.com"))
        check("a signed paid session is accepted", r.status_code == 200 and r.text == "ok", r.text)
        t1 = tok_of("pi_test_111")
        check("it becomes an order with her form answers, queued to be made", od(t1)["status"] == "queued"
              and od(t1)["answers"]["name"] == "Bernadette" and od(t1)["email"] == "stripe1@example.com" and not od(t1).get("express"))
        stripe_event("checkout.session.completed", paid_session("cs_test_aaa111", "pi_test_111", s1["lead"], "stripe1@example.com"))
        check("the same payment sent twice makes one order", tok_of("pi_test_111") == t1
              and len([f for f in (DATA / "orders").glob("*.json") if json.loads(f.read_text()).get("receipt") == "pi_test_111"]) == 1)
        bad = stripe_event("checkout.session.completed", paid_session("cs_test_bad", "pi_test_bad", s1["lead"], "x@example.com"), secret="whsec_wrong")
        old = stripe_event("checkout.session.completed", paid_session("cs_test_old", "pi_test_old", s1["lead"], "x@example.com"), age=900)
        check("a forged or stale signature is refused and makes nothing", bad.status_code == 400 and old.status_code == 400
              and not (DATA / "idx" / ("receipt-" + hashlib.sha1(b"pi_test_bad|prayersong-1").hexdigest())).exists())
        stripe_event("checkout.session.completed", paid_session("cs_test_ccc", "pi_test_other", s1["lead"], "x@example.com", link="plink_someone_else"))
        stripe_event("checkout.session.completed", paid_session("cs_test_ddd", "pi_test_unpaid", s1["lead"], "x@example.com", status="unpaid"))
        check("a session from another payment link, or not paid yet, makes no order",
              not (DATA / "idx" / ("receipt-" + hashlib.sha1(b"pi_test_other|prayersong-1").hexdigest())).exists()
              and not (DATA / "idx" / ("receipt-" + hashlib.sha1(b"pi_test_unpaid|prayersong-1").hexdigest())).exists())
        s2 = lead("stripe2@example.com", "Kateri")
        stripe_event("checkout.session.completed", paid_session("cs_test_eee", "pi_test_222", s2["lead"], "stripe2@example.com", link="plink_express"))
        check("the express payment link marks the order express", od(tok_of("pi_test_222")).get("express") is True)
        sp = html.unescape(requests.get(f"{BASE}/s/", params={"k": t1}).text)
        cp = html.unescape(requests.get(f"{BASE}/s/", params={"k": tok_a}).text)
        check("a Stripe order's page names SANCTORIA PRAYER and no ClickBank; a ClickBank order's page keeps CLKBANK*COM and its notice",
              "SANCTORIA PRAYER" in sp and "ClickBank" not in sp and "CLKBANK*COM" in cp and "ClickBank is the retailer" in cp)
        stripe_event("charge.refunded", {"object": "charge", "payment_intent": "pi_test_111", "refunded": True})
        check("a refund in Stripe is recorded on the order, and the song link keeps working", od(t1).get("refunded") is True
              and requests.get(f"{BASE}/s/", params={"k": t1}).status_code == 200)
        s3 = lead("stripe3@example.com", "Jude", vid="cmc1234567890")
        stripe_event("checkout.session.completed", paid_session("cs_test_fff", "pi_test_333", "", "stripe3@example.com"))
        check("with no lead id her answers are found by email, and the ClickMagick visitor id travels with them",
              od(tok_of("pi_test_333"))["answers"]["name"] == "Jude" and od(tok_of("pi_test_333")).get("vid") == "cmc1234567890")
        s4 = lead("stripe4@example.com", "Monica")
        pi = {"id": "pi_test_embed444", "object": "payment_intent", "status": "succeeded", "receipt_email": "stripe4@example.com",
              "metadata": {"offer": "prayersong", "flow": "embed", "lid": s4["lead"], "express": "1", "vid": ""}}
        stripe_event("payment_intent.succeeded", pi)
        check("each Stripe sale is reported to ClickMagick once when there is a visitor id, and noted when there is none",
              od(tok_of("pi_test_333")).get("cm_reported") == "yes" and od(tok_of("pi_test_111")).get("cm_reported") == "no visitor id")
        check("a payment made in the form's own Pay step becomes an express order with her answers",
              od(tok_of("pi_test_embed444"))["answers"]["name"] == "Monica" and od(tok_of("pi_test_embed444")).get("express") is True)
        stripe_event("payment_intent.succeeded", {**pi, "id": "pi_test_link555", "metadata": {"offer": "prayersong"}})
        check("a payment-link payment is not handled twice through its PaymentIntent",
              not (DATA / "idx" / ("receipt-" + hashlib.sha1(b"pi_test_link555|prayersong-1").hexdigest())).exists())
        bad_pay = requests.post(f"{BASE}/api/pay.php", json={"lid": "0" * 32, "express": True})
        check("the Pay step refuses to prepare a payment without saved answers", bad_pay.status_code == 422)
        pr = requests.get(f"{BASE}/api/paid.php", params={"session_id": "cs_test_notreal1234567"}, allow_redirects=False)
        junk = requests.get(f"{BASE}/api/paid.php", params={"session_id": "nonsense"}, allow_redirects=False)
        check("back from Stripe with a session that cannot be confirmed: a thank you page, never 'not found'",
              pr.status_code == 302 and "/s/?thanks=1" in pr.headers.get("Location", "") and "find=1" in junk.headers.get("Location", ""))

        held = S.get(adm, params={"o": tok_a})

        S.post(adm, data={"act": "logout", "csrf": csrf_of(held.text)})
        check("after signing out the orders are hidden again", "Sign in" in S.get(adm).text and "mary@example.com" not in S.get(adm).text)
        for _ in range(5):
            requests.post(adm, data={"password": "guess"})
        check("after five wrong passwords sign in is locked", "Too many wrong tries" in requests.post(adm, data={"password": ADMIN_PW}).text)

        print(f"\n{sum(results)}/{len(results)} checks passed")
        if "--keep" in sys.argv:
            print(f"\nServer left running. Song page: {BASE}/s/?k={tok_a}\nData: {DATA}\nCtrl+C to stop.")
            server.wait()
    finally:
        server.terminate()
        if "--keep" not in sys.argv:
            subprocess.run(["rm", "-rf", str(DATA)])
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
