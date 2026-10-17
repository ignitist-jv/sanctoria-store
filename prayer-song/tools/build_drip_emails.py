"""Build the Drip email series from prayer-song/copy/08-drip-series.md into branded HTML.

Writes prayer-song/emails/drip/<ID>.html (one per email, ready to paste into Drip's HTML editor),
emails.json (subject, preview, timing, html) and preview.html (all ten, for review).
Generated files are never hand-edited: fix the copy or this builder and rebuild.
"""
import html, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "copy" / "08-drip-series.md"
OUT = ROOT / "emails" / "drip"
LOGO = "https://sanctoriastore.com/images/logo.png"
CREAM, PAPER, INK, SOFT, BRONZE, GOLD, GOLD_EDGE, HAIR = "#F7F3EC", "#FFFDF9", "#2A1F1A", "#5B4A40", "#9A7B4F", "#F2C230", "#D9A415", "#E6DCCA"
SERIF = "Georgia, 'Times New Roman', serif"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"


def esc(t):
    """Escape for HTML but leave Drip Liquid ({{ }} and {% %}) untouched."""
    parts = re.split(r"({{.*?}}|{%.*?%})", t)
    return "".join(p if p.startswith(("{{", "{%")) else html.escape(p, quote=False) for p in parts)


def parse():
    text = SRC.read_text().split("=== NOTES ===")[0]
    emails = []
    for blk in re.split(r"^## EMAIL: ", text, flags=re.M)[1:]:
        eid, body = blk.split("\n", 1)
        d = {"id": eid.strip(), "P": [], "P_AFTER": []}
        for line in body.splitlines():
            m = re.match(r"([A-Z_]+): (.*)", line)
            if not m:
                continue
            k, v = m.groups()
            if k in ("P", "P_AFTER"):
                d[k].append(v.strip())
            else:
                d[k] = v.strip()
        emails.append(d)
    return emails


def para(t, size=17, color=INK, extra=""):
    return (f'<p style="margin:0 0 18px 0;font-family:{SANS};font-size:{size}px;line-height:1.65;color:{color};{extra}">{esc(t)}</p>')


def render(e):
    so = e.get("SIGNOFF", "With our prayers, Sanctoria").split(", ", 1)
    sign = esc(so[0]) + ",<br>" + esc(so[1]) if len(so) == 2 else esc(so[0])
    body = "".join(para(p) for p in e["P"])
    button = (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:8px 0 22px 0"><tr><td align="center">'
              f'<a href="{e["BUTTON_LINK"]}" target="_blank" style="display:block;background:{GOLD};border:1px solid {GOLD_EDGE};border-radius:12px;'
              f'padding:16px 20px;font-family:{SANS};font-size:17px;font-weight:700;color:{INK};text-decoration:none;text-align:center">{esc(e["BUTTON"])}</a>'
              f'</td></tr></table>')
    after = "".join(para(p, 15.5, SOFT) for p in e["P_AFTER"])
    pre = esc(e.get("PREVIEW", ""))
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light"><title>{esc(e.get("SUBJECT", ""))}</title></head>
<body style="margin:0;padding:0;background:{CREAM}">
<div style="display:none;max-height:0;overflow:hidden;opacity:0">{pre}&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{CREAM}"><tr><td align="center" style="padding:28px 14px 36px 14px">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:560px">
<tr><td align="center" style="padding:0 0 22px 0"><img src="{LOGO}" width="150" alt="Sanctoria" style="display:block;width:150px;height:auto;border:0"></td></tr>
<tr><td style="background:{PAPER};border:1px solid {HAIR};border-radius:18px;padding:34px 30px 18px 30px">
<div style="width:38px;height:2px;background:{BRONZE};margin:0 0 22px 0;font-size:0;line-height:0">&nbsp;</div>
{body}{button}{after}
<p style="margin:6px 0 16px 0;font-family:{SERIF};font-size:18px;line-height:1.5;color:{INK};font-style:italic">{sign}</p>
</td></tr>
<tr><td align="center" style="padding:22px 10px 0 10px;font-family:{SANS};font-size:12px;line-height:1.6;color:#9A8B79">
Sanctoria &middot; <a href="https://sanctoriastore.com/prayer-song/" style="color:#9A8B79">sanctoriastore.com</a> &middot; support@sanctoriastore.com<br>
{{{{ inline_postal_address }}}}<br>
<a href="{{{{ unsubscribe_url }}}}" style="color:#9A8B79">Unsubscribe</a>
</td></tr></table></td></tr></table></body></html>"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    emails = parse()
    banned = [e["id"] for e in emails if any(c in json.dumps(e) for c in ("–", "—"))]
    assert not banned, f"banned dash in {banned}"
    data = []
    for e in emails:
        h = render(e)
        (OUT / f'{e["id"]}.html').write_text(h)
        data.append({"id": e["id"], "send": e.get("SEND", ""), "subject": e.get("SUBJECT", ""), "preview": e.get("PREVIEW", ""), "html": h})
    (OUT / "emails.json").write_text(json.dumps(data, indent=1, ensure_ascii=False))
    sample = {"subscriber.first_name": "Mary", "subscriber.prayer_song_for": "Daniel", "subscriber.prayer_song_link": "https://sanctoriastore.com/prayer-song/",
              "subscriber.prayer_song_resume_link": "https://sanctoriastore.com/prayer-song/", "inline_postal_address": "Ignitist Pte Ltd, Singapore",
              "unsubscribe_url": "#"}
    def fill(t):
        t = re.sub(r"{%.*?%}", "", t)
        return re.sub(r"{{\s*([a-z_.]+)\s*}}", lambda m: sample.get(m.group(1), m.group(0)), t)
    cards = "".join(f'<section><h2>{d["id"]} &middot; {html.escape(d["send"])}</h2><p class="s"><b>{html.escape(fill(d["subject"]))}</b><br>{html.escape(fill(d["preview"]))}</p>'
                    f'<iframe srcdoc="{html.escape(fill(d["html"]))}"></iframe></section>' for d in data)
    (OUT / "preview.html").write_text(f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Drip emails</title><style>body{{margin:0;background:#EFE8DB;font-family:{SANS};color:{INK}}}main{{max-width:1240px;margin:0 auto;padding:24px 16px;display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:22px}}
section{{background:#fff;border-radius:14px;padding:14px}}h2{{font-size:14px;margin:0 0 6px;color:{BRONZE}}}.s{{font-size:13px;margin:0 0 10px;line-height:1.45}}
iframe{{width:100%;height:760px;border:1px solid {HAIR};border-radius:10px}}</style></head><body><main>{cards}</main></body></html>""")
    print(f"{len(data)} emails written to {OUT}")


if __name__ == "__main__":
    main()
