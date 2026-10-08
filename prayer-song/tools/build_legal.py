#!/usr/bin/env python3
"""
copy/05-legal.md -> site/prayer-song/terms.html and privacy.html.

The pages borrow their look from the site's own site/terms.html (head, styles, header, footer),
so they stay in step with the rest of sanctoriastore.com. Only the words come from the copy file.

  python3 prayer-song/tools/build_legal.py
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT.parent / "site"
SRC = ROOT / "copy" / "05-legal.md"
SHELL = SITE / "terms.html"
OUT = SITE / "prayer-song"
EMAIL = "support@sanctoriastore.com"


def e(s):
    s = html.escape(s.strip(), quote=False)
    return s.replace(EMAIL, f'<a class="inline" href="mailto:{EMAIL}">{EMAIL}</a>')


def pages():
    out, cur = {}, None
    for raw in SRC.read_text().splitlines():
        line = raw.strip()
        if not line or (line.startswith("(") and line.endswith(")")):
            continue
        m = re.match(r"#\s*PAGE:\s*(\S+)", line)
        if m:
            cur = out.setdefault(m.group(1).lower(), {"meta": {}, "body": []})
            continue
        if cur is None:
            continue
        m = re.match(r"(TITLE|DESC|EFFECTIVE|INTRO):\s*(.*)", line)
        if m and not cur["body"]:
            cur["meta"][m.group(1).lower()] = m.group(2).strip()
        elif line.startswith("## "):
            cur["body"].append(("h2", line[3:]))
        elif line.startswith("- "):
            cur["body"].append(("li", line[2:]))
        else:
            cur["body"].append(("p", line))
    return out


def render(body):
    out, in_list = [], False
    for kind, text in body:
        if kind == "li" and not in_list:
            out.append("      <ul>")
            in_list = True
        if kind != "li" and in_list:
            out.append("      </ul>")
            in_list = False
        if kind == "li":
            out.append(f"        <li>{e(text)}</li>")
        else:
            out.append(f"      <{kind}>{e(text)}</{kind}>")
    if in_list:
        out.append("      </ul>")
    return "\n".join(out)


def main():
    shell = SHELL.read_text()
    head = shell[:shell.index("<body>")]
    foot = shell[shell.index("<!-- Footer -->"):]
    problems = []
    for name, pg in pages().items():
        m = pg["meta"]
        for k in ("title", "desc", "effective", "intro"):
            if not m.get(k):
                problems.append(f"{name}: no {k.upper()}")
        h = re.sub(r"<title>.*?</title>", f"<title>{html.escape(m.get('title', ''))} | Sanctoria</title>", head, flags=re.S)
        h = re.sub(r'<meta name="description" content="[^"]*">',
                   f'<meta name="description" content="{html.escape(m.get("desc", ""), quote=True)}">\n<meta name="robots" content="noindex">', h)
        f = (foot.replace('href="contact.html"', 'href="/contact.html"').replace('href="privacy.html"', 'href="privacy.html"')
                 .replace("Copyright 2026 Sanctoria. Made and blessed for the Circle.", "Copyright 2026 Sanctoria."))
        page = "\n".join([
            h + "<body>", "",
            '<nav class="sticky">', '  <div class="wrap navrow">',
            '    <a href="./" class="brand">', '      <span class="name">SANCTORIA</span>', '      <span class="sub">Blessed Devotionals</span>', "    </a>",
            '    <a href="./" class="btn small">Your Prayer Song</a>', "  </div>", "</nav>", "",
            '<main class="legal">', '  <div class="wrap">', '    <div class="legal-card">',
            '      <span class="eyebrow">Sanctoria</span>',
            f"      <h1>{html.escape(m.get('title', ''))}</h1>",
            f'      <div class="eff">Effective date: {html.escape(m.get("effective", ""))}</div>',
            f'      <p class="intro">{e(m.get("intro", ""))}</p>', "",
            render(pg["body"]),
            "    </div>", "  </div>", "</main>", "", f,
        ])
        if "—" in page.split("<body>")[1] or "–" in page.split("<body>")[1]:
            problems.append(f"{name}: a banned dash is on the page")
        (OUT / f"{name}.html").write_text(page)
        words = len(re.sub(r"<[^>]+>", " ", render(pg["body"])).split())
        print(f"  wrote site/prayer-song/{name}.html  ({words} words, {sum(1 for k, _ in pg['body'] if k == 'h2')} sections)")
    for p in problems:
        print("  PROBLEM:", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
