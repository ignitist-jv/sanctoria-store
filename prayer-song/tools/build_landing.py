#!/usr/bin/env python3
"""
Build the Prayer Song landing page and survey form from the copy files.

  prayer-song/copy/01-landing-page.md  +  prayer-song/copy/02-survey.md
      + prayer-song/tools/landing-template.html
      -> site/prayer-song/index.html

The page is generated. Never hand edit it: change the copy or this builder and rebuild.

Usage:
  python3 prayer-song/tools/build_landing.py          # preview build (review bar on)
  python3 prayer-song/tools/build_landing.py --live   # production build, refuses if anything is missing

Every run reports: word count, banned dashes, unknown markers, button lengths, and what is still missing.
"""

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # prayer-song/
SITE = ROOT.parent / "site" / "prayer-song"
COPY_PAGE = ROOT / "copy" / "01-landing-page.md"
COPY_SURVEY = ROOT / "copy" / "02-survey.md"
COPY_DELIVERY = ROOT / "copy" / "03-delivery.md"
COPY_BONUS = ROOT / "copy" / "04-bonuses.md"
TEMPLATE = ROOT / "tools" / "landing-template.html"

# ---- live settings. Filled in during phase 8 (wiring). None means "not connected yet". ----
# How she pays (TS, 2026-10-16). "stripe": two Stripe payment links (song, song + express) from prayer-song/stripe-<STRIPE_MODE>.json.
# "clickbank": CHECKOUT_URL below, unchanged, kept so switching back is this one line.
# "embed" = Stripe's card and wallet fields inside the form's own Pay step (api/pay.php), the way TS chose on 2026-10-17.
PAYMENT = "clickbank" if "--clickbank" in sys.argv else ("stripe" if "--stripe" in sys.argv else "embed")   # live on Stripe since 2026-10-17
STRIPE_MODE = "test" if "--stripe-test" in sys.argv else "live"     # which keys and prayer-song/stripe-<mode>.json the build uses
CHECKOUT_URL = "https://karmacc.pay.clickbank.net/?cbitems=prayersong-1&template=songform&vtid=[cmc_vid]"      # e.g. "https://karmacc.pay.clickbank.net/?cbitems=prayersong-1&template=...&cbfid=...&vtid=[cmc_vid]"
LEAD_ENDPOINT = "api/lead.php"   # relative to /prayer-song/. Stores the answers under a lead id.
HERO_IMAGE = None        # e.g. "img/hero.webp" (relative to site/prayer-song/)
HERO_VIDEO = "video/hero.mp4"   # the three sample clips as one silent loop; used at the top of the page when the file exists
PAGE_COPY = {}           # the parsed landing copy, set in main() so one section can quote another
SAMPLE_FILES = ["sample-1.mp3", "sample-2.mp3", "sample-3.mp3"]   # under site/prayer-song/audio/, in the order of the SAMPLE lines
CLIP_SLUGS = ["son", "mother", "grandchild"]    # video/sample-<slug>.mp4 (+ .webp first frame), in the order of the SAMPLE lines. Optional
TILE_SLUGS = ["husband", "son", "daughter", "grandchild", "mother", "father", "marriage", "friend", "passed", "herself"]   # img/for-<slug>.webp, in CHIP order
CTA_DEFAULT = ""         # set from the hero CTA at build time, for sections that have no CTA line of their own
BUTTON_MAX = 26
# Order follows the reference page (prayersong.com): hero, how it works, samples, who it is for, what you get.
SECTION_ORDER = ["hero", "devotion", "promise", "how", "sample", "for", "get", "mechanism", "bonuses", "proof", "offer", "guarantee", "faq", "final"]
RELATIONS = ["husband", "wife", "son", "daughter", "grandchild", "mother", "father", "friend", "myself", "passed"]
INTENTIONS = ["healing", "protection", "strength", "peace", "return", "marriage", "grief", "thanksgiving"]
STYLES = ["hymn", "acoustic", "gospel", "country", "lullaby", "piano", "folk", "choir"]
VOICES = ["female", "male", "either"]

problems, missing, notes = [], [], []
DELIVERY = None


def e(s):
    return html.escape(s.strip(), quote=True)


def body_of(path):
    text = path.read_text()
    return text.split("=== NOTES ===", 1)[0]


def parse(path, head):
    """-> {id: [(KEY, value), ...]} in file order."""
    out, cur = {}, None
    for raw in body_of(path).splitlines():
        line = raw.strip()
        if not line or line.startswith("(") and line.endswith(")"):
            continue
        m = re.match(rf"##\s*{head}:\s*(\S+)", line)
        if m:
            cur = m.group(1).lower()
            out[cur] = []
            continue
        if line.startswith("## "):
            cur = line[3:].strip().lower()        # e.g. "## PHRASES"
            out[cur] = []
            continue
        if cur is None:
            continue
        m = re.match(r"([A-Z][A-Z_0-9]*):\s*(.*)", line)
        if m:
            out[cur].append((m.group(1), m.group(2).strip()))
        elif cur == "phrases" and ":" in line:
            k, v = line.split(":", 1)
            out[cur].append((k.strip().lower(), v.strip()))
        elif out[cur]:
            k, v = out[cur][-1]                    # continuation line of the previous value
            out[cur][-1] = (k, (v + " " + line).strip())
        else:
            problems.append(f"unparsed line in {cur}: {line[:60]}")
    return out


def one(sec, key, default=""):
    for k, v in sec:
        if k == key:
            return v
    return default


def many(sec, key):
    return [v for k, v in sec if k == key]


def pair(v):
    a, _, b = v.partition("|")
    return a.strip(), b.strip()


ICO_GIFT = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7"/>'
            '<path d="M7.5 8a2.5 2.5 0 0 1 0-5C10 3 12 8 12 8s2-5 4.5-5a2.5 2.5 0 0 1 0 5"/></svg>')
ICO_PLAY = ('<svg class="ico-play" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>'
            '<svg class="ico-pause" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg>')
ICO_CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
ICO_PREV = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6 5h2v14H6zM20 6v12l-10-6z"/></svg>'
ICO_NEXT = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16 5h2v14h-2zM4 6v12l10-6z"/></svg>'


def disc(which, label="Sanctoria"):
    """The record. A generated photograph (img/record.webp) that turns while its track plays, with a fixed
    light sheen laid over it so the highlight stays put as the disc spins. data-disc ties it to a track.
    Falls back to a drawn record if the image is missing."""
    if (SITE / "img" / "record.webp").exists():
        return (f'<span class="disc" data-disc="{which}"><img class="rec" src="img/record.webp" alt="" width="640" height="640" decoding="async">'
                '<i class="sheen"></i></span>')
    rings = "".join(f'<circle cx="100" cy="100" r="{r}" fill="none" stroke="#2B2B2E" stroke-width="0.6"/>' for r in range(44, 98, 6))
    return (f'<span class="disc" data-disc="{which}"><svg class="rec" viewBox="0 0 200 200" aria-hidden="true"><circle cx="100" cy="100" r="99" fill="#151517"/>{rings}'
            f'<circle cx="100" cy="100" r="36" fill="#F3EDE4" stroke="#B9C6F2" stroke-width="2"/>'
            f'<text x="100" y="92" text-anchor="middle" font-family="Playfair Display,Georgia,serif" font-style="italic" font-size="13" fill="#1B1B22">{label}</text>'
            f'<circle cx="100" cy="100" r="2.5" fill="#151517"/></svg></span>')


def btn(label, icon=True):
    if len(label) > BUTTON_MAX:
        problems.append(f'button "{label}" is {len(label)} characters, max {BUTTON_MAX}')
    return f'<button class="btn" type="button" data-start>{ICO_GIFT if icon else ""}<span>{e(label)}</span></button>'


def paras(sec, cls=""):
    attr = f' class="{cls}"' if cls else ""
    out = []
    for k, v in sec:
        if k == "P":
            out.append(f"<p{attr}>{e(v)}</p>")
        elif k == "PULL":
            out.append(f'<div class="pull">{e(v)}</div>')
    return "\n".join(out)


def micro(sec):
    m = one(sec, "MICRO")
    return f'<p class="micro">{e(m)}</p>' if m else ""


TRACKS = []          # filled from the sample section: [{src, title, line}]


def load_tracks(sec):
    for i, v in enumerate(many(sec, "SAMPLE")):
        title, line = pair(v)
        fn = SAMPLE_FILES[i] if i < len(SAMPLE_FILES) else None
        if fn and (SITE / "audio" / fn).exists():
            TRACKS.append({"src": f"audio/{fn}", "title": title, "line": line})
    if not TRACKS:
        missing.append("sample songs in site/prayer-song/audio/ (the players are left out until they exist)")


def render(sid, sec):
    # Structure and behaviour follow the reference page section for section (TS, 2026-10-05):
    # media hero, numbered steps on a dark ground, a swipeable row of song cards, a three across grid of
    # labelled pictures on a dark ground, then the player card with a checklist and a button.
    # The look (colours, type, the arch, gold buttons) is Sanctoria's own.
    kick = '<span class="kick"></span>'
    h2 = f"{kick}<h2>{e(one(sec, 'H2'))}</h2>" if one(sec, "H2") else ""
    if sid == "hero":
        trust = "".join(f"<li>{e(t)}</li>" for t in one(sec, "TRUST").split("|") if t.strip())
        g1, g2 = pair(one(sec, "GUARANTEE_CARD"))
        # The seal is a stamp: a big figure over a small word (GUARANTEE_SEAL: "100% | Guaranteed"). Without that line it
        # falls back to the number of days the card promises.
        s1, s2 = pair(one(sec, "GUARANTEE_SEAL")) if one(sec, "GUARANTEE_SEAL") else ("", "")
        if not s1:
            m = re.search(r"\d+", g2)
            s1 = m.group(0) if m else ""
        if not s1:
            problems.append("the guarantee card has nothing for its seal: add GUARANTEE_SEAL or a number of days")
        seal_html = f"<i>{e(s1)}</i>" + (f"<small>{e(s2)}</small>" if s2 else "")
        # the opening phrase of the card's heading, up to its first comma, is set in italic
        head, comma, tail = g1.partition(",")
        g1_html = f"<em>{e(head)},</em> {e(tail)}" if comma and tail.strip() else e(g1)
        listen = ""
        if TRACKS:
            listen = (f'<button class="listen" type="button" data-play="0"><span class="dot">{ICO_PLAY}</span>'
                      f'{e(one(sec, "LISTEN"))}</button>')
        photo = f'<img class="photo" src="{HERO_IMAGE}" alt="" width="900" height="972">' if HERO_IMAGE else disc(0)
        film, film_note = "", ""
        if HERO_VIDEO and (SITE / HERO_VIDEO).exists():
            poster = HERO_VIDEO.rsplit(".", 1)[0] + ".webp"
            photo = (f'<video class="photo" data-clip src="{HERO_VIDEO}"' + (f' poster="{poster}"' if (SITE / poster).exists() else "") +
                     ' muted loop playsinline preload="metadata" aria-label="Families at home, listening together"></video>')
            film = " film"
            # the plain statement that the people in the film are illustrations, right under it (hero FILM_NOTE)
            if one(sec, "FILM_NOTE"):
                film_note = f'<p class="filmnote">{e(one(sec, "FILM_NOTE"))}</p>'
            else:
                # TS took the line under the film off (2026-10-09). The page must still say it once: the sample section does.
                said = " ".join(v for k, v in PAGE_COPY.get("sample", []) if k == "P")
                if "illustrations" not in said or one(PAGE_COPY.get("sample", []), "HIDE"):
                    problems.append("the hero film is on the page but nothing says the scenes are illustrations "
                                    "(hero FILM_NOTE, or a P in the sample section)")
        return "\n".join([
            f'<div class="topbar">{e(one(sec, "TOPBAR"))}</div>',
            '<div class="head">',
            '  <img src="/images/logo.png" alt="Sanctoria, Blessed Devotionals" height="34">',
            # TS 2026-10-18: no nav links and no second button in the header, so each screen has one button.
            # "Find my song" stays in the footer for buyers.
            '</div>',
            '<section class="hero">',
            f'  <div class="hmedia{" wide" if film else ""}"><div class="arch{film}">{photo}{listen if film else ""}</div>{"" if film else listen}{film_note}</div>',
            '  <div class="hbody">',
            f'    <div class="eyebrow">{e(one(sec, "EYEBROW"))}</div>',
            f'    <h1>{e(one(sec, "H1"))}</h1>',
            f'    <p class="sub">{e(one(sec, "SUB"))}</p>',
            f'    {btn(one(sec, "CTA"))}',
            f'    {micro(sec)}',
            f'    <div class="gline"><div class="seal" aria-hidden="true">{seal_html}</div><div><b>{g1_html}</b><span>{e(g2)}</span></div></div>',
            f'    <ul class="trust">{trust}</ul>',
            '  </div>',
            '</section>',
        ])
    if sid == "how":
        steps = "".join(f'<li><span class="n">{i}</span><div><b>{e(t)}</b><span>{e(d)}</span></div></li>'
                        for i, (t, d) in enumerate(map(pair, many(sec, "STEP")), 1))
        return f'<section class="deep">{h2}<ol class="timeline">{steps}</ol>{btn(one(sec, "CTA"))}</section>'
    if sid == "sample":
        if not TRACKS:
            if LIVE:
                return ""
            return (f'<section class="alt">{h2}{paras(sec, "lead")}<div class="slot"><b>Preview only.</b> Sample song cards go here. '
                    'This section is left out of a live build until the audio files exist.</div></section>')
        tag = e(one(sec, "TAG", "A Sample Prayer Song"))
        cards = []
        alts = {}
        prompts = ROOT / "creative" / "sample-clip-prompts.json"
        if prompts.exists():
            alts = {c["slug"]: c.get("alt", "") for c in json.loads(prompts.read_text())}
        for i, t in enumerate(TRACKS):
            slug = CLIP_SLUGS[i] if i < len(CLIP_SLUGS) else ""
            art = f'<div class="sart">{disc(i)}</div>'
            if slug and (SITE / "video" / f"sample-{slug}.mp4").exists():
                # an illustration clip: silent, looping, and only playing while it is on screen (see the template script)
                poster = f' poster="video/sample-{slug}.webp"' if (SITE / "video" / f"sample-{slug}.webp").exists() else ""
                art = (f'<div class="sart vid"><video data-clip src="video/sample-{slug}.mp4"{poster} muted loop playsinline preload="none" '
                       f'aria-label="{e(alts.get(slug, ""))}"></video></div>')
            cards.append(
                f'<div class="scard">{art}<div class="srow"><div><span class="tag">{tag}</span>'
                f'<b>{e(t["title"])}</b><span class="ln">{e(t["line"])}</span></div>'
                f'<button class="play" type="button" data-play="{i}" aria-label="Play: {e(t["title"])}">{ICO_PLAY}</button></div></div>')
        dots = "".join(f'<i{" class=\"on\"" if i == 0 else ""}></i>' for i in range(len(TRACKS)))
        return (f'<section class="alt" id="samples">{h2}{paras(sec, "lead")}<div class="cards" id="cards">{"".join(cards)}</div>'
                f'<div class="dots" id="dots">{dots}</div>' + (f'<p class="note">{e(one(sec, "SAMPLE_NOTE"))}</p>' if one(sec, "SAMPLE_NOTE") else "") + '</section>')
    if sid == "devotion":
        return f'<section class="devo">{h2}<div class="mt left">{paras(sec)}</div></section>'
    if sid == "promise":
        # the lyric excerpt is quoted word for word from the first sample; its name is picked out in gold
        nm = TRACKS[0]["title"].split()[1] if TRACKS and len(TRACKS[0]["title"].split()) > 1 else "Daniel"
        lines = "".join(f"<span>{e(l).replace(e(nm), f'<mark>{e(nm)}</mark>')}</span>" for l in many(sec, "EXCERPT"))
        lyric = (f'<figure class="lyric"><blockquote>{lines}</blockquote>'
                 + (f'<figcaption>{e(one(sec, "EXCERPT_CAPTION"))}</figcaption>' if one(sec, "EXCERPT_CAPTION") else "")
                 + "</figure>") if lines else ""
        facts = "".join(f'<li><b>{e(a)}</b><span>{e(b)}</span></li>' for a, b in map(pair, many(sec, "FACT")))
        return (f'<section class="promise">{h2}<div class="mt left">{paras(sec)}</div>{lyric}'
                + (f'<ul class="facts">{facts}</ul>' if facts else "") + '</section>')
    if sid == "mechanism":
        return f'<section>{h2}<div class="mt left">{paras(sec)}</div></section>'
    if sid == "for":
        tiles, plain = [], 0
        for i, c in enumerate(many(sec, "CHIP")):
            slug = TILE_SLUGS[i] if i < len(TILE_SLUGS) else ""
            img = ""
            if slug and (SITE / "img" / f"for-{slug}.webp").exists():
                img = f'<img src="img/for-{slug}.webp" alt="" width="360" height="450" loading="lazy" decoding="async">'
            else:
                plain += 1
            tiles.append(f'<figure class="tile">{img}<figcaption>{e(c)}</figcaption></figure>')
        if plain:
            missing.append(f"{plain} occasion picture(s) in site/prayer-song/img/ (a plain bronze window is shown instead)")
        return (f'<section class="deep">{h2}{paras(sec, "lead")}<div class="tiles">{"".join(tiles)}</div>'
                f'{btn(one(sec, "CTA") or CTA_DEFAULT)}</section>')
    if sid == "get":
        player = ""
        if TRACKS:
            player = "".join([
                '<div class="rplayer">',
                f'<div class="wrap">{disc("cur")}</div>',
                '<div class="track" id="rtrack"><i id="rfill"></i></div>',
                '<div class="times"><span id="rnow">0:00</span><span id="rdur">1:00</span></div>',
                '<p class="rtitle" id="rtitle"></p><p class="rline" id="rline"></p>',
                '<div class="ctrl">',
                f'<button class="skip" type="button" data-skip="-1" aria-label="Previous">{ICO_PREV}</button>',
                f'<button class="play big" type="button" data-play="cur" aria-label="Play or pause">{ICO_PLAY}</button>',
                f'<button class="skip" type="button" data-skip="1" aria-label="Next">{ICO_NEXT}</button>',
                '</div></div>',
            ])
        gets = "".join(f'<li><span class="ck">{ICO_CHECK}</span><b>{e(t)}</b><span>{e(d)}</span></li>' for t, d in map(pair, many(sec, "ITEM")))
        return (f'<section class="alt">{h2}{paras(sec, "lead")}{player}<ul class="gets">{gets}</ul>'
                f'{btn(one(sec, "CTA") or CTA_DEFAULT, False)}</section>')
    if sid == "bonuses":
        items = "".join(f"<li><b>{e(t)}</b><span>{e(d)}</span></li>" for t, d in map(pair, many(sec, "ITEM")))
        return f'<section class="alt">{h2}{paras(sec, "lead")}<ol class="items">{items}</ol></section>'
    if sid == "proof":
        return f'<section class="alt">{h2}<div class="mt left">{paras(sec)}</div></section>'
    if sid == "offer":
        risk = f'<p class="risk">{e(one(sec, "RISK"))}</p>' if one(sec, "RISK") else ""
        badge = one(sec, "PRICE_BADGE")
        was = one(sec, "PRICE_WAS")
        anchor = ""
        if badge or was:
            anchor = ('<div class="panchor">'
                      + (f'<span class="pbadge">{e(badge)}</span>' if badge else "")
                      + (f'<span class="pwas">{e(was)}</span>' if was else "")
                      + "</div>")
        return (f'<section>{h2}{paras(sec, "lead")}<div class="pricecard">{anchor}<div class="price">{e(one(sec, "PRICE"))}</div>'
                f'<p class="pnote">{e(one(sec, "PRICE_NOTE"))}</p>{btn(one(sec, "CTA"))}{micro(sec)}</div>{risk}</section>')
    if sid == "guarantee":
        return f'<section class="alt"><div class="guar">{h2}<div class="mt left">{paras(sec)}</div></div></section>'
    if sid == "faq":
        qa, q = [], None
        for k, v in sec:
            if k == "Q":
                q = v
            elif k == "A" and q:
                qa.append(f"<details><summary>{e(q)}</summary><p>{e(v)}</p></details>")
                q = None
        return f'<section class="faq">{kick}<h2>{e(one(sec, "H2", "Frequently Asked Questions"))}</h2>{"".join(qa)}</section>'
    if sid == "final":
        return f'<section class="deep">{h2}<div class="mt">{paras(sec, "lead")}</div><div class="mt">{btn(one(sec, "CTA"))}</div>{micro(sec)}</section>'
    problems.append(f"unknown section: {sid}")
    return ""


def survey_data(c):
    def opts(sec, marker, allowed, what):
        out = []
        for v in many(sec, marker):
            label, key = pair(v)
            if key not in allowed:
                problems.append(f"survey {what} option has unknown key: {key!r}")
            out.append({"label": label, "key": key})
        for k in allowed:
            if k not in [o["key"] for o in out]:
                problems.append(f"survey {what} is missing option: {k}")
        return out

    def need(step, sec, keys):
        d = {}
        for k in keys:
            v = one(sec, k)
            if not v:
                problems.append(f"survey step {step} is missing {k}")
            d[k.lower()] = v
        return d

    g = lambda s: c.get(s, [])
    basics = need("basics", g("basics"), ["H", "SUB", "LABEL_WHO", "LABEL_NAME", "LABEL_NAME_MYSELF", "PLACEHOLDER_NAME", "ERROR"])
    basics["options"] = opts(g("basics"), "OPTION", RELATIONS, "who")
    for k in ("LABEL_PHON", "PLACEHOLDER_PHON", "TIP_PHON"):      # the separate "how the name is said" box
        basics[k.lower()] = one(g("basics"), k)
    for k in ("LABEL_NAME2", "PLACEHOLDER_NAME2", "LABEL_WHO2", "OPTION_WHO2_BLANK", "TIP_NAME2"):   # the optional second name
        basics[k.lower()] = one(g("basics"), k)
    prayer = need("prayer", g("prayer"), ["H", "SUB", "LABEL_INTENTION", "LABEL_NOTE", "PLACEHOLDER_NOTE", "TIP_NOTE", "ERROR"])
    prayer["options"] = opts(g("prayer"), "OPTION", INTENTIONS, "intention")
    sound = need("sound", g("sound"), ["H", "SUB", "LABEL_STYLE", "LABEL_VOICE", "TIP", "ERROR"])
    sound["options"] = opts(g("sound"), "OPTION", STYLES, "style")
    sound["voices"] = opts(g("sound"), "VOICE", VOICES, "voice")
    for k in ("SOUND_DEFAULT", "CHANGE_SOUND"):      # the sound comes pre-chosen on screen 2, with a link to change it
        sound[k.lower()] = one(g("sound"), k)
    send = need("send", g("send"), ["H", "SUB", "LABEL_EMAIL", "PLACEHOLDER_EMAIL", "LABEL_BUYER", "PLACEHOLDER_BUYER",
                                    "MICRO", "ERROR", "SUMMARY_TITLE", "SUMMARY_LINE", "BUTTON"])
    if len(send["button"]) > BUTTON_MAX:
        problems.append(f'checkout button "{send["button"]}" is {len(send["button"])} characters, max {BUTTON_MAX}')
    basics["tip"] = one(g("basics"), "TIP")
    for k in ("DELIVERY_PILL", "ORDER_TITLE", "ROW_FOR", "ROW_PRAYER", "ROW_SOUND",
              "ROW_DELIVERY", "ROW_DELIVERY_VALUE", "GUAR_TITLE", "GUAR_BODY"):   # the order summary card
        send[k.lower()] = one(g("send"), k)
    for k in ("PRICE_BADGE", "PRICE_WAS", "PRICE_NOW"):      # the price block on the last step
        send[k.lower()] = one(g("send"), k)
    for k in ("EXPRESS_LABEL", "EXPRESS_NOTE", "ROW_DELIVERY_EXPRESS", "PRICE_TOTAL_LABEL"):   # the express tick box (Stripe)
        send[k.lower()] = one(g("send"), k)
    if PAYMENT == "stripe" and not send["express_label"]:
        problems.append("survey step send needs EXPRESS_LABEL for the express tick box")
    send["summary_line_two"] = one(g("send"), "SUMMARY_LINE_TWO") or send["summary_line"]
    if basics["label_name2"] and not one(g("send"), "SUMMARY_LINE_TWO"):
        problems.append("survey step send needs SUMMARY_LINE_TWO now that a second name can be given")
    ui = need("ui", g("ui"), ["BACK", "NEXT", "STEP_OF", "AGREE"])
    ui["step_names"] = [x.strip() for x in one(g("ui"), "STEP_NAMES").split("|") if x.strip()]
    if len(ui["step_names"]) not in (3, 4, 5):
        problems.append("survey UI STEP_NAMES must list four names (five with the Pay step)")
    pay = {k.lower(): one(g("pay"), k) for k in ("H", "SUB", "DIVIDER", "BUTTON", "BUTTON_BUSY", "SECURE", "ERROR", "ERROR_LOAD", "SAMPLE_LABEL")}
    if PAYMENT == "embed":
        pay = need("pay", g("pay"), ["H", "SUB", "DIVIDER", "BUTTON", "BUTTON_BUSY", "SECURE", "ERROR", "ERROR_LOAD"])
        if "{price}" not in pay["button"]:
            problems.append("survey step pay BUTTON must contain {price}")
        # three screens since 2026-10-18: name and prayer | sound and email | pay
        if len(ui["step_names"]) != 3:
            problems.append("the embedded form has three screens: STEP_NAMES needs three names")
        for k in ("SOUND_DEFAULT", "CHANGE_SOUND"):
            if not sound[k.lower()]:
                problems.append(f"survey step sound is missing {k} (screen 2 shows the default sound)")
    if len(ui["next"]) > BUTTON_MAX:
        problems.append(f'form continue button "{ui["next"]}" is over {BUTTON_MAX} characters')
    for word in ("Terms", "Privacy Policy"):
        if word not in ui["agree"]:
            problems.append(f'survey UI AGREE line must contain "{word}" so it can be linked')
    for step, d in (("basics", basics), ("prayer", prayer), ("sound", sound), ("send", send)):
        if len(d["h"].replace("{name}", "Bernadette")) > 34:
            notes.append(f'survey heading "{d["h"]}" may wrap to three lines at 320px')
    phrases = dict(g("phrases"))
    for k in RELATIONS + INTENTIONS + STYLES:
        if k not in phrases:
            problems.append(f"survey PHRASES missing: {k}")
    return {"basics": basics, "prayer": prayer, "sound": sound, "send": send, "pay": pay, "ui": ui, "phrases": phrases,
            "sample_tag": one(PAGE_COPY.get("sample", []), "TAG")}


def delivery_copy(d, phrases):
    """03-delivery.md -> api/copy.json, read by the song page (s/index.php) and the emails (api/pipeline.php)."""
    def block(sec, lists=("P", "P_AFTER")):
        out = {}
        for k, v in sec:
            if k in lists:
                out.setdefault(k.lower(), []).append(v)
            else:
                out[k.lower()] = v
        return out

    pages = {k: block(v) for k, v in d.items() if not k.startswith("email:")}
    # The receipt carries both statement names (STATEMENT for Stripe, STATEMENT_CLICKBANK); the song page picks by the order.
    emails = {k.split(":", 1)[1].strip(): block(v) for k, v in d.items() if k.startswith("email:")}
    for name in ("making", "ready", "review", "needs", "notfound"):
        if name not in pages:
            problems.append(f"delivery copy is missing PAGE: {name}")
    for name in ("ready", "delay"):
        if name not in emails:
            problems.append(f"delivery copy is missing EMAIL: {name}")
        elif "subject" not in emails[name]:
            problems.append(f"EMAIL {name} has no SUBJECT")
    fb = pages.get("feedback")
    if fb is None:
        notes.append("no PAGE: feedback in the delivery copy, so the song page does not ask for a review")
    else:
        fb["p"] = " ".join(fb.get("p", []))
        for k in ("h", "p", "stars_label", "text_label", "text_hint", "name_label", "name_hint", "share", "button", "thanks_h", "thanks_p", "edit", "error_stars", "error"):
            if not fb.get(k):
                problems.append(f"delivery copy: PAGE feedback has no {k.upper()}")
        if len(fb.get("button", "")) > BUTTON_MAX:
            problems.append(f'review button "{fb["button"]}" is over {BUTTON_MAX} characters')
    rp = pages.get("reviews_public")
    if rp is None:
        notes.append("no PAGE: reviews_public in the delivery copy, so there are no header links and no reviews page")
    else:
        rp["p"] = " ".join(rp.get("p", []))
        for k in ("nav_track", "nav_reviews", "title", "h", "p", "empty_h", "empty_p", "how_h", "how_p", "samples", "cta"):
            if not rp.get(k):
                problems.append(f"delivery copy: PAGE reviews_public has no {k.upper()}")
        if len(rp.get("cta", "")) > BUTTON_MAX:
            problems.append(f'reviews page button "{rp["cta"]}" is over {BUTTON_MAX} characters')
    for key in ("download", "another_button"):
        v = pages.get("ready", {}).get(key, "")
        if len(v) > BUTTON_MAX:
            problems.append(f'song page button "{v}" is over {BUTTON_MAX} characters')
    return {"page": pages, "email": emails, "phrases": phrases}


def bonus_copy(d):
    """04-bonuses.md -> the "bonus" part of api/copy.json, read by api/bonus_docs.php (the PDFs) and the song page."""
    def block(key, lists=()):
        out = {}
        for k, v in d.get(key, []):
            if k in lists:
                out.setdefault(k.lower(), []).append(v)
            else:
                out[k.lower()] = v
        return out

    days = []
    for n in range(1, 10):
        day = block(f"day: {n}")
        for k in ("title", "verse", "ref", "reflection", "prayer", "practice"):
            if not day.get(k):
                problems.append(f"bonus copy: day {n} has no {k.upper()}")
        if day.get("prayer", "").count("{blank}") != 1:
            problems.append(f"bonus copy: day {n} prayer must contain {{blank}} exactly once")
        if "verify" in day:
            problems.append(f"bonus copy: day {n} verse {day.get('ref')} is still marked VERIFY. Check it against drbo.org, "
                            "then change the line to VERIFIED")
        day.pop("verified", None)
        days.append(day)
    companion = block("companion", ("INTRO_P",))
    close = block("companion-close", ("P",))
    card = block("card")
    sheet = block("lyric-sheet")
    page = block("page: bonuses", ("ITEM",))
    for name, blk, keys in (("companion", companion, ("cover_title", "intro_h", "intro_p")), ("card", card, ("heading", "prayer", "prayer_memorial", "prayer_self")),
                            ("lyric-sheet", sheet, ("kicker",)), ("PAGE bonuses", page, ("h", "item"))):
        for k in keys:
            if not blk.get(k):
                problems.append(f"bonus copy: {name} has no {k.upper()}")
    items = []
    for f, raw in zip(("sheet", "companion", "card"), page.get("item", [])):
        parts = [x.strip() for x in raw.split("|")]
        if len(parts) != 3:
            problems.append(f"bonus copy: ITEM needs title | description | button: {raw[:40]}")
            continue
        if len(parts[2]) > BUTTON_MAX:
            problems.append(f'bonus button "{parts[2]}" is over {BUTTON_MAX} characters')
        items.append({"f": f, "title": parts[0], "desc": parts[1], "button": parts[2]})
    if len(items) != 3:
        problems.append("bonus copy: PAGE bonuses needs three ITEM lines, in the order lyric sheet, companion, card")
    return {"companion": companion, "days": days, "close": close, "card": card, "sheet": sheet,
            "page": {"h": page.get("h", ""), "print": page.get("print", ""), "items": items}}


LIVE = "--live" in sys.argv
# --soft: the page as visitors will see it (no preview bar), published BEFORE the ClickBank link exists, so TS can look at
# it on the real domain. The form works and saves answers; its last button says plainly that checkout is not open yet.
SOFT = "--soft" in sys.argv


def main():
    for p in (COPY_PAGE, COPY_SURVEY, COPY_DELIVERY, TEMPLATE):
        if not p.exists():
            sys.exit(f"Missing: {p.relative_to(ROOT.parent)}")
    page = parse(COPY_PAGE, "SECTION")
    PAGE_COPY.update(page)
    survey = parse(COPY_SURVEY, "STEP")

    for sid in page:
        if sid not in SECTION_ORDER and sid != "footer":           # the footer is not a page section: its words fill the template's footer
            problems.append(f"unknown section in copy: {sid}")
    for sid in SECTION_ORDER:
        if sid not in page:
            problems.append(f"section missing from copy: {sid}")
    global CTA_DEFAULT
    CTA_DEFAULT = one(page.get("hero", []), "CTA")
    load_tracks(page.get("sample", []))
    hidden = [sid for sid in SECTION_ORDER if sid in page and one(page[sid], "HIDE")]     # a section with "HIDE: yes" stays in the copy but off the page
    for sid in hidden:
        notes.append(f"section hidden by HIDE in the copy: {sid}")
    # each section carries its name (data-s), which the wide desktop layout uses
    sections = "\n\n".join(re.sub(r"<section(?=[ >])", f'<section data-s="{sid}"', render(sid, page[sid]), count=1)
                           for sid in SECTION_ORDER if sid in page and sid not in hidden)

    stripe_cfg = {}
    if PAYMENT == "embed":
        sj = ROOT / f"stripe-{STRIPE_MODE}.json"
        st = json.loads(sj.read_text()) if sj.exists() else {}
        envf = ROOT.parent / ".env"
        envv = dict(l.split("=", 1) for l in envf.read_text().splitlines() if "=" in l and not l.startswith("#")) if envf.exists() else {}
        pk = envv.get(f"STRIPE_PK_{STRIPE_MODE.upper()}", "").strip().strip('"\'')
        if not pk.startswith(f"pk_{STRIPE_MODE}_"):
            problems.append(f"PAYMENT is embed but .env has no STRIPE_PK_{STRIPE_MODE.upper()} (a pk_{STRIPE_MODE}_ key)")
        if LIVE and STRIPE_MODE != "live" and "--test-payments" not in sys.argv:
            problems.append("PAYMENT is embed with the TEST key; a live build needs STRIPE_MODE = \"live\" (or --test-payments for a deliberate test on the live site)")
        cents = st.get("amounts", {"song": 3900, "express": 995})
        stripe_cfg = {"pk": pk, "price_song": cents["song"], "price_express": cents["express"],
                      "name_song": "Your Prayer Song", "name_express": "Express Song Delivery", "pay_endpoint": "api/pay.php",
}     # the Stripe product names
        link = '<a id="lnk-checkout" href="#pay">checkout</a><a id="lnk-vid" href="https://sanctoriastore.com/prayer-song/?vtid=[cmc_vid]">v</a>'
    elif PAYMENT == "stripe":
        sj = ROOT / f"stripe-{STRIPE_MODE}.json"
        st = json.loads(sj.read_text()) if sj.exists() else {}
        links = st.get("links", {})
        if not (links.get("song") and links.get("song_express")):
            problems.append(f"PAYMENT is stripe but {sj.name} has no song and song_express payment links")
        if LIVE and STRIPE_MODE != "live" and "--test-payments" not in sys.argv:
            # a live page that takes test payments takes no money at all: refuse unless asked for on purpose
            problems.append("PAYMENT is stripe with TEST payment links; a live build needs STRIPE_MODE = \"live\" (or --test-payments for a deliberate test on the live site)")
        cents = st.get("amounts", {"song": 3900, "express": 995})
        money = lambda c: f"${c // 100}" if c % 100 == 0 else f"${c / 100:.2f}"
        stripe_cfg = {"express_price": money(cents["express"]), "total_express": money(cents["song"] + cents["express"])}
        # the vid link is only there so ClickMagick's cmc.js fills in the visitor id, which the form passes on with her answers
        link = (f'<a id="lnk-checkout" href="{html.escape(links.get("song", {}).get("url", ""))}">checkout</a>'
                f'<a id="lnk-checkout-express" href="{html.escape(links.get("song_express", {}).get("url", ""))}">checkout</a>'
                '<a id="lnk-vid" href="https://sanctoriastore.com/prayer-song/?vtid=[cmc_vid]">v</a>')
    elif CHECKOUT_URL:
        link = f'<a id="lnk-checkout" href="{html.escape(CHECKOUT_URL)}">checkout</a>'
    else:
        link = ""
        missing.append("ClickBank checkout link (phase 8, wiring)")
    if not LEAD_ENDPOINT:
        missing.append("lead capture endpoint, so the survey answers reach Kit and the server (phase 8, wiring)")

    global DELIVERY
    sd = survey_data(survey)
    DELIVERY = delivery_copy(parse(COPY_DELIVERY, "PAGE"), sd["phrases"])
    if COPY_BONUS.exists():
        DELIVERY["bonus"] = bonus_copy(parse(COPY_BONUS, "DOC"))
    else:
        missing.append("the bonus copy (copy/04-bonuses.md). Without it the song page leaves the three printables out")
    blob = json.dumps(DELIVERY, ensure_ascii=False)
    if any(ch in blob for ch in (chr(0x2013), chr(0x2014))):
        problems.append("banned dash in the delivery copy")

    hero = page.get("hero", [])
    nav_labels = {k.lower(): v for k, v in parse(COPY_DELIVERY, "PAGE").get("reviews_public", [])}
    if not one(page.get("footer", []), "MISSION"):
        problems.append("the footer has no MISSION line (SECTION: footer in the landing copy)")
    preview = ('<div class="pvbar"><b>PREVIEW.</b> Not live. Checkout and email capture are not connected. '
               'Built from prayer-song/copy.</div>') if not (LIVE or SOFT) else ""
    out = TEMPLATE.read_text()
    for token, value in {
        "{{TITLE}}": e(one(hero, "H1")) + " | Sanctoria",
        "{{DESCRIPTION}}": e(one(hero, "SUB")),
        "{{CHECKOUT_LINK}}": link,
        "{{PREVIEW_BAR}}": preview,
        "{{SECTIONS}}": sections,
        "{{SURVEY_JSON}}": json.dumps(sd, ensure_ascii=False),
        "{{FOOTER_MISSION}}": e(one(page.get("footer", []), "MISSION")),
        "{{FOOTER_FIND}}": f'<a href="s/?find">{e(nav_labels.get("nav_track", ""))}</a>' if nav_labels.get("nav_track") else "",
        "{{FOOTER_REVIEWS}}": f'<a href="reviews/" data-reviews hidden>{e(nav_labels.get("nav_reviews", ""))}</a>' if nav_labels.get("nav_reviews") else "",
        "{{CFG_JSON}}": json.dumps({"lead_endpoint": LEAD_ENDPOINT, "soft": SOFT, "pay": PAYMENT, **stripe_cfg}),
        "{{TRACKS_JSON}}": json.dumps(TRACKS, ensure_ascii=False),
    }.items():
        out = out.replace(token, value)

    left = re.findall(r"\{\{[A-Z_]+\}\}", out)
    if left:
        problems.append(f"unfilled template tokens: {sorted(set(left))}")
    dashes = sum(out.count(ch) for ch in (chr(0x2013), chr(0x2014)))
    if dashes:
        problems.append(f"{dashes} banned dash character(s) in the built page")
    stray = re.findall(r"\[[A-Z][A-Z _]+\]", re.sub(r"\[cmc_vid\]", "", sections))
    if stray:
        problems.append(f"unrendered placeholders: {sorted(set(stray))}")

    words = len(re.findall(r"[A-Za-z0-9$']+", re.sub(r"<[^>]+>", " ", sections)))
    print(f"{'LIVE' if LIVE else ('SOFT (no checkout yet)' if SOFT else 'PREVIEW')} build")
    print(f"  words on page: {words}")
    print(f"  sections: {len([s for s in SECTION_ORDER if s in page])}/{len(SECTION_ORDER)}, FAQ pairs: {len(many(page.get('faq', []), 'Q'))}")
    print(f"  banned dashes: {dashes}")
    print(f"  problems: {len(problems)}")
    for p in problems:
        print(f"    ! {p}")
    print(f"  still missing: {len(missing)}")
    for m in missing:
        print(f"    - {m}")
    for n in notes:
        print(f"    note: {n}")

    if SOFT and problems:
        sys.exit("REFUSED: a soft build needs zero problems.")
    if LIVE and (problems or [m for m in missing if "sample" not in m and "hero image" not in m]):
        sys.exit("REFUSED: a live build needs zero problems, a checkout link and a lead endpoint.")
    SITE.mkdir(parents=True, exist_ok=True)
    (SITE / "index.html").write_text(out)
    (SITE / "api").mkdir(exist_ok=True)
    (SITE / "api" / "copy.json").write_text(json.dumps(DELIVERY, ensure_ascii=False, indent=1))
    print(f"  wrote site/prayer-song/index.html ({len(out)//1024} KB)")


if __name__ == "__main__":
    main()
