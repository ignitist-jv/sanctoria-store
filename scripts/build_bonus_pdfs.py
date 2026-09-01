"""
Build beautifully designed PDFs for the 4 Sanctoria digital bonuses.
Output: print-friendly (cream background, charcoal text, bronze + soft gold accents).

Sanctoria / sanctoriastore.com
"""
import os
import re
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.pagesizes import LETTER, inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    PageBreak, HRFlowable, KeepTogether, Flowable
)

# ------------------------------ Brand palette ------------------------------
# Sanctoria: cream #F7F3EC, bronze #9A7B4F accents, gold #F2C230 (sparingly),
# dark charcoal text.
CREAM      = HexColor('#F7F3EC')       # page background
CHARCOAL   = HexColor('#1C1C1E')       # body text (headlines)
INK        = HexColor('#2A2620')       # slightly softer body ink
BRONZE     = HexColor('#9A7B4F')       # primary accent (labels, rules, scripture)
GOLD       = HexColor('#F2C230')       # bright gold, used sparingly for ornaments
MUTED      = HexColor('#6B635A')       # muted text (captions)
RULE_GOLD  = HexColor('#9A7B4F')       # bronze rules

BRAND = 'Sanctoria'
BRAND_KICKER = 'SANCTORIA'

# Fonts. Use Times (serif) and Helvetica-Bold as fallbacks. Try to register
# Georgia if present (Windows) for a slightly warmer serif.
SERIF = 'Times-Roman'
SERIF_BOLD = 'Times-Bold'
SERIF_ITALIC = 'Times-Italic'
SERIF_BOLD_ITALIC = 'Times-BoldItalic'
SANS_BOLD = 'Helvetica-Bold'
SANS = 'Helvetica'

def try_register_georgia():
    global SERIF, SERIF_BOLD, SERIF_ITALIC, SERIF_BOLD_ITALIC
    candidates = [
        (r'C:\Windows\Fonts\georgia.ttf',     'Georgia',      'serif'),
        (r'C:\Windows\Fonts\georgiab.ttf',    'Georgia-Bold', 'serif_bold'),
        (r'C:\Windows\Fonts\georgiai.ttf',    'Georgia-Italic','serif_italic'),
        (r'C:\Windows\Fonts\georgiaz.ttf',    'Georgia-BoldItalic','serif_bold_italic'),
        # macOS common serif
        ('/Library/Fonts/Georgia.ttf',        'Georgia',      'serif'),
    ]
    registered = {}
    for path, name, key in candidates:
        if os.path.exists(path):
            try:
                pdfmetrics.registerFont(TTFont(name, path))
                registered[key] = name
            except Exception:
                pass
    if 'serif' in registered:
        SERIF = registered['serif']
    if 'serif_bold' in registered:
        SERIF_BOLD = registered['serif_bold']
    if 'serif_italic' in registered:
        SERIF_ITALIC = registered['serif_italic']
    if 'serif_bold_italic' in registered:
        SERIF_BOLD_ITALIC = registered['serif_bold_italic']

try_register_georgia()

# --------------------------- Styles -------------------------------------------
def make_styles():
    S = {}
    S['body'] = ParagraphStyle('body', fontName=SERIF, fontSize=11.5,
        textColor=INK, leading=17.5, spaceAfter=10, alignment=TA_LEFT,
        firstLineIndent=0)
    S['body_justify'] = ParagraphStyle('body_justify', parent=S['body'],
        alignment=TA_JUSTIFY)
    S['body_center'] = ParagraphStyle('body_center', parent=S['body'],
        alignment=TA_CENTER)
    S['italic'] = ParagraphStyle('italic', parent=S['body'],
        fontName=SERIF_ITALIC, textColor=MUTED)
    S['italic_center'] = ParagraphStyle('italic_center', parent=S['italic'],
        alignment=TA_CENTER)
    S['prayer'] = ParagraphStyle('prayer', parent=S['body'],
        fontName=SERIF_ITALIC, fontSize=12.5, leading=19,
        textColor=INK, leftIndent=18, rightIndent=18, spaceAfter=11)
    S['prayer_center'] = ParagraphStyle('prayer_center', parent=S['prayer'],
        alignment=TA_CENTER, leftIndent=0, rightIndent=0)
    S['declaration'] = ParagraphStyle('declaration', parent=S['body'],
        fontName=SERIF_BOLD, fontSize=12, leading=18,
        textColor=BRONZE, leftIndent=20, rightIndent=20, spaceAfter=11,
        alignment=TA_CENTER)
    S['scripture'] = ParagraphStyle('scripture', parent=S['body'],
        fontName=SERIF_ITALIC, fontSize=11.5, leading=18,
        textColor=INK, leftIndent=22, rightIndent=22, spaceAfter=6)
    S['scripture_attr'] = ParagraphStyle('scripture_attr', parent=S['body'],
        fontName=SERIF_BOLD, fontSize=10, textColor=BRONZE,
        leftIndent=22, rightIndent=22, spaceAfter=11, alignment=TA_LEFT)
    S['latin'] = ParagraphStyle('latin', parent=S['body'],
        fontName=SERIF_ITALIC, fontSize=12, leading=17.5,
        textColor=BRONZE, alignment=TA_CENTER, spaceAfter=4)
    S['h1'] = ParagraphStyle('h1', fontName=SANS_BOLD, fontSize=22,
        textColor=CHARCOAL, leading=28, alignment=TA_CENTER,
        spaceBefore=12, spaceAfter=8)
    S['h1_gold'] = ParagraphStyle('h1_gold', parent=S['h1'], textColor=BRONZE,
        fontSize=13, leading=17, spaceAfter=6)
    S['h2'] = ParagraphStyle('h2', fontName=SANS_BOLD, fontSize=16,
        textColor=CHARCOAL, leading=22, alignment=TA_LEFT,
        spaceBefore=18, spaceAfter=10)
    S['h2_center'] = ParagraphStyle('h2_center', parent=S['h2'],
        alignment=TA_CENTER)
    S['h3'] = ParagraphStyle('h3', fontName=SANS_BOLD, fontSize=11,
        textColor=BRONZE, leading=15, alignment=TA_LEFT,
        spaceBefore=14, spaceAfter=6)
    S['h3_center'] = ParagraphStyle('h3_center', parent=S['h3'],
        alignment=TA_CENTER)
    S['day_number'] = ParagraphStyle('day_number', fontName=SANS_BOLD,
        fontSize=11, textColor=BRONZE, leading=14, alignment=TA_CENTER,
        spaceAfter=4)
    S['day_title'] = ParagraphStyle('day_title', fontName=SERIF_BOLD,
        fontSize=22, textColor=CHARCOAL, leading=26, alignment=TA_CENTER,
        spaceAfter=10)
    S['cover_title'] = ParagraphStyle('cover_title', fontName=SERIF_BOLD,
        fontSize=34, textColor=CHARCOAL, leading=40, alignment=TA_CENTER)
    S['cover_subtitle'] = ParagraphStyle('cover_subtitle', fontName=SERIF_ITALIC,
        fontSize=15, textColor=MUTED, leading=22, alignment=TA_CENTER,
        spaceBefore=14)
    S['cover_kicker'] = ParagraphStyle('cover_kicker', fontName=SANS_BOLD,
        fontSize=10, textColor=BRONZE, leading=14, alignment=TA_CENTER)
    S['cover_brand'] = ParagraphStyle('cover_brand', fontName=SANS_BOLD,
        fontSize=11, textColor=CHARCOAL, leading=14, alignment=TA_CENTER)
    S['label'] = ParagraphStyle('label', fontName=SANS_BOLD, fontSize=9.5,
        textColor=BRONZE, leading=13, alignment=TA_LEFT, spaceAfter=6,
        spaceBefore=4)
    return S


STYLES = make_styles()


# --------------------------- Decorative flowables -----------------------------

class GoldRule(Flowable):
    """Thin bronze rule with optional ornament in the middle."""
    def __init__(self, width, thickness=0.8, ornament=True, color=RULE_GOLD,
                 space_before=6, space_after=6):
        super().__init__()
        self.width = width
        self.thickness = thickness
        self.ornament = ornament
        self.color = color
        self.space_before = space_before
        self.space_after = space_after
        self.height = self.space_before + 8 + self.space_after

    def draw(self):
        c = self.canv
        y = self.space_after + 4
        c.setStrokeColor(self.color)
        c.setLineWidth(self.thickness)
        if self.ornament:
            gap = 12
            mid = self.width / 2.0
            c.line(0, y, mid - gap, y)
            c.line(mid + gap, y, self.width, y)
            c.setFillColor(self.color)
            c.setFont(SERIF, 10)
            c.drawCentredString(mid, y - 3, '✦')
        else:
            c.line(0, y, self.width, y)


class CrossOrnament(Flowable):
    """A centered cross ornament with short flanking bronze rules."""
    def __init__(self, width, space_before=12, space_after=12):
        super().__init__()
        self.width = width
        self.space_before = space_before
        self.space_after = space_after
        self.height = self.space_before + 18 + self.space_after

    def draw(self):
        c = self.canv
        y = self.space_after + 9
        c.setStrokeColor(RULE_GOLD)
        c.setLineWidth(0.6)
        line_len = 60
        mid = self.width / 2.0
        c.line(mid - line_len - 12, y, mid - 10, y)
        c.line(mid + 10, y, mid + line_len + 12, y)
        c.setFillColor(GOLD)
        c.setFont(SERIF_BOLD, 14)
        c.drawCentredString(mid, y - 5, '✝')


# --------------------------- Markdown to Flowables ----------------------------

def escape(text):
    """Escape XML-special characters for ReportLab's Paragraph mini-language,
    then convert **bold** and *italic* to <b>/<i>. Never emit em/en dashes."""
    # Convert & first
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    # Bold: **...**
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Italic: *...* (non-greedy)
    text = re.sub(r'(?<!\*)\*([^*\n]+?)\*(?!\*)', r'<i>\1</i>', text)
    # NOTE: no dash substitution. Hyphens stay hyphens; the source never uses
    # inline double-hyphens, and em/en dashes are banned brand-wide.
    return text


def p(text, style):
    """Shortcut to build a Paragraph with escaping (for user markdown)."""
    return Paragraph(escape(text), STYLES[style])


def praw(text, style):
    """Build a Paragraph with trusted HTML (cover pages / content WE control)."""
    return Paragraph(text, STYLES[style])


def parse_blocks(md_text):
    """Split markdown into logical blocks separated by blank lines, preserving
    `---` as its own block (horizontal rule)."""
    lines = md_text.splitlines()
    blocks = []
    current = []
    for line in lines:
        stripped = line.strip()
        if stripped == '---':
            if current:
                blocks.append(current)
                current = []
            blocks.append(['---'])
            continue
        if stripped == '':
            if current:
                blocks.append(current)
                current = []
        else:
            current.append(line)
    if current:
        blocks.append(current)
    return blocks


def classify_block(block, filename):
    first = block[0].lstrip()
    if first == '---':
        return 'hr'
    if first.startswith('# '):
        return 'h1'
    if first.startswith('## '):
        return 'h2'
    if first.startswith('### '):
        return 'h3'
    if first.startswith('#### '):
        return 'h4'
    if re.match(r'^[-*]\s', first) or re.match(r'^\d+\.\s', first):
        return 'list'
    return 'para'


def strip_heading(line):
    return re.sub(r'^#+\s+', '', line.strip())


# Matches "Day 3:", "Movement 1:", "Part 2." etc. so the renderer can split a
# small kicker from the title. Uses only hyphen/colon/period separators.
DAY_SPLIT = re.compile(r'^(Day\s+\d+|Movement\s+\d+|Part\s+\d+)\s*[:.\-]\s*(.*)$',
                       re.IGNORECASE)


def render_blocks(md_text, filename, avail_width, day_break_pattern=None):
    """Convert a markdown string to a list of flowables."""
    flow = []
    blocks = parse_blocks(md_text)
    first_h1_seen = False

    for block in blocks:
        kind = classify_block(block, filename)

        if kind == 'hr':
            flow.append(Spacer(1, 4))
            flow.append(GoldRule(avail_width))
            flow.append(Spacer(1, 4))
            continue

        if kind == 'h1':
            title = strip_heading(block[0])
            rest = [strip_heading(b) for b in block[1:]]
            if not first_h1_seen:
                first_h1_seen = True
                continue
            if day_break_pattern and day_break_pattern(title):
                flow.append(PageBreak())
                flow.append(Spacer(1, 20))
                m = DAY_SPLIT.match(title)
                if m:
                    flow.append(p(m.group(1).upper(), 'day_number'))
                    flow.append(Spacer(1, 2))
                    subtitle = m.group(2).strip().strip('"“”')
                    flow.append(p(subtitle, 'day_title'))
                else:
                    flow.append(p(title, 'day_title'))
                flow.append(Spacer(1, 4))
                flow.append(GoldRule(avail_width))
                flow.append(Spacer(1, 10))
            else:
                flow.append(Spacer(1, 14))
                flow.append(p(title, 'h2_center'))
                flow.append(GoldRule(avail_width))
                flow.append(Spacer(1, 6))
            for extra in rest:
                flow.append(p(extra, 'body'))
            continue

        if kind == 'h2':
            title = strip_heading(block[0])
            if '=====' in title or re.match(r'side\s+\d', title, re.IGNORECASE):
                clean = title.replace('=', '').strip()
                flow.append(PageBreak())
                flow.append(Spacer(1, 16))
                flow.append(p(clean.upper(), 'cover_kicker'))
                flow.append(Spacer(1, 6))
                flow.append(GoldRule(avail_width))
                continue
            if day_break_pattern and day_break_pattern(title):
                flow.append(PageBreak())
                flow.append(Spacer(1, 20))
                m = DAY_SPLIT.match(title)
                if m:
                    flow.append(p(m.group(1).upper(), 'day_number'))
                    flow.append(Spacer(1, 2))
                    subtitle = m.group(2).strip().strip('"“”')
                    flow.append(p(subtitle, 'day_title'))
                else:
                    flow.append(p(title, 'day_title'))
                flow.append(Spacer(1, 4))
                flow.append(GoldRule(avail_width))
                flow.append(Spacer(1, 10))
                for extra in block[1:]:
                    flow.append(p(extra.strip(), 'body'))
                continue
            flow.append(Spacer(1, 14))
            flow.append(p(title, 'h2_center'))
            flow.append(Spacer(1, 4))
            for extra in block[1:]:
                flow.append(p(extra.strip(), 'body'))
            continue

        if kind == 'h3':
            title = strip_heading(block[0])
            flow.append(Spacer(1, 10))
            flow.append(p(title.upper(), 'h3_center'))
            flow.append(GoldRule(avail_width, ornament=False,
                                 space_before=2, space_after=4))
            for extra in block[1:]:
                flow.append(p(extra.strip(), 'body'))
            continue

        if kind == 'h4':
            title = strip_heading(block[0])
            flow.append(p(title, 'label'))
            continue

        if kind == 'list':
            for line in block:
                line = line.rstrip()
                m = re.match(r'^(\s*)([-*]|\d+\.)\s+(.*)$', line)
                if not m:
                    flow.append(p(line.strip(), 'body'))
                    continue
                marker = m.group(2)
                content = m.group(3)
                bullet = '•' if marker in ('-', '*') else marker
                flow.append(Paragraph(
                    f'<font color="#9A7B4F"><b>{bullet}</b></font>&nbsp;&nbsp;{escape(content)}',
                    ParagraphStyle('li', parent=STYLES['body'],
                                   leftIndent=18, bulletIndent=4, spaceAfter=3)
                ))
            continue

        # default paragraph
        text = ' '.join(l.strip() for l in block)

        inline_label = re.match(r'^\*\*([^*]+):\*\*\s+(.+)$', text)
        if inline_label:
            label_text = inline_label.group(1).strip()
            rest_text = inline_label.group(2).strip()
            flow.append(Spacer(1, 6))
            flow.append(p(label_text.upper(), 'label'))
            flow.append(p(rest_text, 'body'))
            continue

        bold_only_label = re.match(r'^\*\*([^*]+):\*\*\s*$', text)
        if bold_only_label and len(block) == 1:
            flow.append(Spacer(1, 6))
            flow.append(p(bold_only_label.group(1).upper(), 'label'))
            continue

        if text.startswith('**') and text.endswith('**'):
            stripped = text[2:-2]
            if '**' not in stripped:
                flow.append(Spacer(1, 4))
                flow.append(p(stripped, 'declaration'))
                continue

        lower = text.lower()
        if ('vade retro satana' in lower or 'crux sacra' in lower or
                'non draco' in lower or 'nunquam suade' in lower) \
                and len(text) < 400 and '*' in text:
            clean = re.sub(r'\*+', '', text)
            flow.append(p(clean, 'latin'))
            continue

        if len(block) == 1 and text.startswith('*') and text.endswith('*') \
                and not text.startswith('**'):
            inner = text[1:-1]
            if inner.startswith('"') or inner.startswith('“'):
                flow.append(p(inner, 'scripture'))
            else:
                flow.append(p(inner, 'italic_center'))
            continue

        if len(text) < 95 and (text.startswith('*') and text.endswith('*')):
            flow.append(p(text.strip('*'), 'italic_center'))
            continue

        flow.append(p(text, 'body'))

    return flow


# --------------------------- Page decoration ----------------------------------

class PageDecor:
    def __init__(self, brand=BRAND, page_size=LETTER,
                 show_page_numbers=True, with_corners=False):
        self.brand = brand
        self.page_size = page_size
        self.show_page_numbers = show_page_numbers
        self.with_corners = with_corners

    def __call__(self, canvas, doc):
        canvas.saveState()
        pw, ph = self.page_size

        # Cream background
        canvas.setFillColor(CREAM)
        canvas.rect(0, 0, pw, ph, stroke=0, fill=1)

        # Corner flourishes (prayer card only)
        if self.with_corners:
            m = 0.35 * inch
            L = 16
            canvas.setStrokeColor(BRONZE)
            canvas.setLineWidth(0.9)
            canvas.line(m, ph - m, m + L, ph - m)
            canvas.line(m, ph - m, m, ph - m - L)
            canvas.line(pw - m, ph - m, pw - m - L, ph - m)
            canvas.line(pw - m, ph - m, pw - m, ph - m - L)
            canvas.line(m, m, m + L, m)
            canvas.line(m, m, m, m + L)
            canvas.line(pw - m, m, pw - m - L, m)
            canvas.line(pw - m, m, pw - m, m + L)

        # Clean pages. No footer, no page numbers, no brand line.
        canvas.restoreState()


# --------------------------- Cover pages --------------------------------------

def workbook_cover(avail_width):
    return [
        Spacer(1, 1.0 * inch),
        praw(BRAND_KICKER, 'cover_kicker'),
        Spacer(1, 14),
        GoldRule(avail_width),
        Spacer(1, 30),
        praw('The Covenant', 'cover_title'),
        praw('Restored Workbook', 'cover_title'),
        Spacer(1, 20),
        praw("Seven movements to renew your family's<br/>covenant with God",
             'cover_subtitle'),
        Spacer(1, 50),
        praw('<font size="18" color="#F2C230">&#10013;</font>', 'body_center'),
        Spacer(1, 44),
        GoldRule(avail_width, ornament=False),
        Spacer(1, 10),
        praw('<i>Your home belongs to God.<br/>Today you remember it.</i>',
             'italic_center'),
        PageBreak(),
    ]


def novena_cover(avail_width):
    return [
        Spacer(1, 1.0 * inch),
        praw(BRAND_KICKER, 'cover_kicker'),
        Spacer(1, 14),
        GoldRule(avail_width),
        Spacer(1, 30),
        praw('The 30-Day', 'cover_title'),
        praw('Saint Benedict Novena', 'cover_title'),
        Spacer(1, 20),
        praw('A daily prayer plan for peace and protection with<br/>'
             'your blessed St. Benedict Marian Bracelet',
             'cover_subtitle'),
        Spacer(1, 56),
        praw('<font size="18" color="#F2C230">&#10013;</font>', 'body_center'),
        Spacer(1, 40),
        GoldRule(avail_width, ornament=False),
        Spacer(1, 10),
        praw('<i>Thirty days to pray. One heart at peace.<br/>'
             'One God who never stops listening.</i>',
             'italic_center'),
        PageBreak(),
    ]


def devotional_cover(avail_width):
    return [
        Spacer(1, 1.0 * inch),
        praw(BRAND_KICKER, 'cover_kicker'),
        Spacer(1, 14),
        GoldRule(avail_width),
        Spacer(1, 30),
        praw('Breaking the Pattern', 'cover_title'),
        Spacer(1, 10),
        praw('A 7-Day Devotional to Restore Peace', 'cover_subtitle'),
        Spacer(1, 40),
        praw('<font size="18" color="#F2C230">&#10013;</font>', 'body_center'),
        Spacer(1, 56),
        praw("<b>How to Recognize Where Peace Has Slipped,<br/>"
             "and Invite God's Blessing Back In</b>",
             'h2_center'),
        Spacer(1, 40),
        GoldRule(avail_width, ornament=False),
        Spacer(1, 10),
        praw('<i>Seven days. Seven parts of your life.<br/>'
             'One peace to welcome home.</i>',
             'italic_center'),
        PageBreak(),
    ]


def prayer_card_cover(avail_width):
    return [
        Spacer(1, 0.6 * inch),
        praw(BRAND_KICKER, 'cover_kicker'),
        Spacer(1, 12),
        praw('<font size="22" color="#F2C230">&#10013;</font>', 'body_center'),
        Spacer(1, 20),
        praw('Daily Prayer<br/>Companion Card', 'cover_title'),
        Spacer(1, 14),
        praw('To be printed, folded, or kept<br/>alongside your blessed bracelet.',
             'italic_center'),
    ]


# --------------------------- Build PDFs ---------------------------------------

def build_pdf(source_md, out_pdf, doc_kind, page_size=LETTER,
              margin=0.9*inch, with_corners=False):
    out_pdf = str(out_pdf)
    os.makedirs(os.path.dirname(out_pdf), exist_ok=True)

    pw, ph = page_size
    frame = Frame(margin, margin, pw - 2 * margin, ph - 2 * margin,
                  id='body', showBoundary=0,
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    decor = PageDecor(page_size=page_size,
                      show_page_numbers=(doc_kind != 'card'),
                      with_corners=with_corners)
    template = PageTemplate(id='main', frames=[frame], onPage=decor)

    doc = BaseDocTemplate(out_pdf, pagesize=page_size,
                          leftMargin=margin, rightMargin=margin,
                          topMargin=margin, bottomMargin=margin,
                          title=Path(out_pdf).stem.replace('-', ' ').title(),
                          author=BRAND)
    doc.addPageTemplates([template])

    avail_width = pw - 2 * margin

    md = Path(source_md).read_text(encoding='utf-8')
    flow = []

    if doc_kind == 'workbook':
        flow.extend(workbook_cover(avail_width))
        def is_section(title):
            return bool(re.match(r'^(Movement\s+\d+|How to Use|A Final Word)',
                                 title, re.IGNORECASE))
        flow.extend(render_blocks(md, source_md, avail_width,
                                  day_break_pattern=is_section))
    elif doc_kind == 'novena':
        flow.extend(novena_cover(avail_width))
        def is_day(title):
            return bool(re.match(r'^(Day\s+\d+|How to Use|After Day)',
                                 title, re.IGNORECASE))
        flow.extend(render_blocks(md, source_md, avail_width,
                                  day_break_pattern=is_day))
    elif doc_kind == 'devotional':
        flow.extend(devotional_cover(avail_width))
        def is_day(title):
            return bool(re.match(r'^(Day\s+\d+|Introduction|What Now)',
                                 title, re.IGNORECASE))
        flow.extend(render_blocks(md, source_md, avail_width,
                                  day_break_pattern=is_day))
    elif doc_kind == 'card':
        flow.extend(prayer_card_cover(avail_width))
        flow.extend(render_blocks(md, source_md, avail_width,
                                  day_break_pattern=lambda t: False))
    else:
        flow.extend(render_blocks(md, source_md, avail_width,
                                  day_break_pattern=lambda t: False))

    doc.build(flow)
    print(f'  -> Wrote {out_pdf}')


def main():
    here = Path(__file__).resolve().parent
    root = here.parent
    src_dir = root / 'bonuses'
    out_dir = root / 'site' / 'downloads'

    pdfs = [
        ('workbook',   src_dir / 'bonus-1-covenant-restored-workbook.md',
         out_dir / 'covenant-restored-workbook.pdf'),
        ('card',       src_dir / 'bonus-2-daily-prayer-card.md',
         out_dir / 'daily-prayer-card.pdf'),
        ('novena',     src_dir / 'bonus-3-30-day-saint-benedict-novena.md',
         out_dir / '30-day-saint-benedict-novena.pdf'),
        ('devotional', src_dir / 'bonus-4-breaking-the-pattern-7-day-devotional.md',
         out_dir / 'breaking-the-pattern-7-day-devotional.pdf'),
    ]

    for kind, src, dst in pdfs:
        print(f'Building {kind}: {src.name}')
        if kind == 'card':
            card_size = (5 * inch, 7 * inch)
            build_pdf(src, dst, kind, page_size=card_size,
                      margin=0.42 * inch, with_corners=True)
        else:
            build_pdf(src, dst, kind)


if __name__ == '__main__':
    main()
