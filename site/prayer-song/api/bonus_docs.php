<?php
// The three printables that come with every song, drawn from the order and the copy:
//   sheet      The Keepsake Lyric Sheet        her song's own lyrics            (made per order)
//   card       The Daily Prayer Card           her loved one's name, her verse  (made per order)
//   companion  The Nine Day Prayer Companion   the same for every buyer
// Every word comes from prayer-song/copy/04-bonuses.md (through api/copy.json) or from the order.
declare(strict_types=1);
require_once __DIR__ . '/lib.php';
require_once __DIR__ . '/lyrics.php';
require_once __DIR__ . '/pdf.php';

const PS_INK    = '#2A1F1A';
const PS_SOFT   = '#5C4F45';
const PS_MUTED  = '#857A6E';
const PS_BRONZE = '#9A7B4F';
const PS_DEEP   = '#7A5F3A';
const PS_GOLD   = '#C9A86A';       // a printable gold: the screen gold is too bright for a hairline on paper

function ps_bonus_copy(): array
{
    return ps_copy()['bonus'] ?? [];
}

/** Double rule around the page, and the brand at the foot. */
function ps_doc_frame(PsPdf $p, bool $brand = true): void
{
    $p->rect(30, 30, PsPdf::W - 60, PsPdf::H - 60, PS_BRONZE, 1.1);
    $p->rect(35, 35, PsPdf::W - 70, PsPdf::H - 70, PS_GOLD, 0.45);
    if ($brand) {
        $p->text(PsPdf::W / 2, 746, 'R', 7.5, 'SANCTORIA', 'C', PS_BRONZE, 2.4);
    }
}

/** The window mark: an arch inside an arch. */
function ps_doc_mark(PsPdf $p, float $cx, float $baseY, float $w = 30, float $h = 44): void
{
    $p->arch($cx, $baseY, $w, $h, PS_BRONZE, 0.9);
    $p->arch($cx, $baseY, $w * 0.56, $h * 0.72, PS_GOLD, 0.6);
}

function ps_doc_rule(PsPdf $p, float $cx, float $y, float $half = 34): void
{
    $p->line($cx - $half, $y, $cx - 6, $y, PS_GOLD, 0.6);
    $p->line($cx + 6, $y, $cx + $half, $y, PS_GOLD, 0.6);
    $p->diamond($cx, $y, 2.4, PS_GOLD);
}

function ps_doc_name(array $o): string
{
    return ps_names_text($o['answers'] ?? []);
}

// ------------------------------------------------------------------ the lyric sheet

function ps_pdf_sheet(array $o): string
{
    $c = ps_bonus_copy()['sheet'] ?? [];
    $name = ps_doc_name($o);
    $self = ($o['answers']['who'] ?? '') === 'myself';
    $title = (string) ($o['title'] ?? ($o['lyrics']['title'] ?? 'Prayer Song'));
    $p = new PsPdf($title);
    $p->page();
    ps_doc_frame($p);
    $cx = PsPdf::W / 2;

    ps_doc_mark($p, $cx, 108);
    $kicker = ps_fill((string) ($self && !empty($c['kicker_self']) ? $c['kicker_self'] : ($c['kicker'] ?? '')), $o);
    $p->fit($cx, 132, 'R', 9, mb_strtoupper($kicker), 460, 'C', PS_BRONZE, 2.2);
    $p->fit($cx, 166, 'B', 28, $title, 470, 'C', PS_INK);
    ps_doc_rule($p, $cx, 184);

    // Stanzas. The bridge is set in italic. Long songs go in two columns.
    $stanzas = [];
    $count = 0;
    foreach (($o['lyrics']['sections'] ?? []) as $sec) {
        $lines = array_values(array_filter(array_map('strval', $sec['lines'] ?? []), fn ($l) => trim($l) !== ''));
        if ($lines) {
            $stanzas[] = ['font' => stripos((string) ($sec['tag'] ?? ''), 'bridge') !== false ? 'I' : 'R', 'lines' => $lines];
            $count += count($lines);
        }
    }
    $top = 208.0;
    $bottom = 692.0;
    $cols = [$stanzas];
    $centres = [$cx];
    $colW = 440.0;
    if ($count > 24 && count($stanzas) > 1) {
        // split at the stanza boundary that leaves the two columns closest in length
        $best = 1;
        $bestDiff = PHP_INT_MAX;
        $run = 0;
        foreach ($stanzas as $i => $s) {
            $run += count($s['lines']);
            if ($i < count($stanzas) - 1 && abs($count - 2 * $run) < $bestDiff) {
                $bestDiff = abs($count - 2 * $run);
                $best = $i + 1;
            }
        }
        $cols = [array_slice($stanzas, 0, $best), array_slice($stanzas, $best)];
        $centres = [$cx - 132, $cx + 132];
        $colW = 236.0;
    }
    // the largest type at which every column fits the space
    for ($size = 13.0; $size >= 8.0; $size -= 0.25) {
        $lead = $size * 1.45;
        $gap = $size * 0.95;
        $laid = [];
        $tallest = 0.0;
        $broken = false;                 // a sung line that had to be split over two printed lines
        foreach ($cols as $col) {
            $rows = [];
            $h = 0.0;
            foreach ($col as $si => $s) {
                if ($si > 0) {
                    $h += $gap;
                }
                foreach ($s['lines'] as $l) {
                    $pieces = $p->wrap($s['font'], $size, $l, $colW);
                    $broken = $broken || count($pieces) > 1;
                    foreach ($pieces as $piece) {
                        $rows[] = [$h, $s['font'], $piece];
                        $h += $lead;
                    }
                }
            }
            $laid[] = $rows;
            $tallest = max($tallest, $h);
        }
        if ($tallest <= $bottom - $top && (!$broken || $size <= 10.0)) {
            break;                       // below 10 point a split line is better than smaller type
        }
    }
    $y0 = $top + max(0.0, ($bottom - $top - ($tallest - $lead + $size)) / 2) + $size;
    foreach ($laid as $ci => $rows) {
        foreach ($rows as [$dy, $font, $piece]) {
            $p->put($centres[$ci], $y0 + $dy, $font, $size, $piece, 'C', PS_INK);
        }
    }
    if (count($cols) === 2) {
        $p->line($cx, $y0 - $size, $cx, $y0 + $tallest - $lead, PS_GOLD, 0.4);
    }

    $ref = (string) ($o['lyrics']['verse'] ?? '');
    if ($ref !== '') {
        $p->text($cx, 712, 'I', 10, $ref, 'C', PS_DEEP);
    }
    $p->fit($cx, 728, 'I', 10, ps_fill((string) ($c['footer'] ?? ''), $o), 460, 'C', PS_MUTED);
    return $p->output();
}

// ------------------------------------------------------------------ the prayer card

function ps_pdf_card(array $o): string
{
    $c = ps_bonus_copy()['card'] ?? [];
    $a = $o['answers'] ?? [];
    $name = ps_doc_name($o);
    $who = (string) ($a['who'] ?? '');
    $prayer = (string) ($c['prayer'] ?? '');
    $heading = (string) ($c['heading'] ?? '');
    if ($who === 'passed' && !empty($c['prayer_memorial'])) {
        $prayer = (string) $c['prayer_memorial'];
    } elseif ($who === 'myself') {
        $prayer = (string) ($c['prayer_self'] ?? $prayer);
        $heading = (string) ($c['heading_self'] ?? $heading);
    }
    [$ref, $verse] = $who === 'passed' ? PS_VERSES['grief'] : (PS_VERSES[$a['intention'] ?? ''] ?? PS_VERSES['peace']);
    $heading = ps_fill($heading, $o);
    $prayer = ps_fill($prayer, $o);

    $p = new PsPdf($heading !== '' ? $heading : 'Daily Prayer Card');
    $p->page();
    $cx = PsPdf::W / 2;
    $w = 360.0;                      // a five by seven inch card in the middle of the sheet
    $h = 504.0;
    $x = ($p::W - $w) / 2;
    $y = 132.0;
    $p->rect($x, $y, $w, $h, PS_MUTED, 0.5, [3, 3]);                      // the cut line
    $p->rect($x + 12, $y + 12, $w - 24, $h - 24, PS_BRONZE, 1.0);
    $p->rect($x + 16, $y + 16, $w - 32, $h - 32, PS_GOLD, 0.45);
    $p->text($cx, $y + $h + 16, 'R', 8, 'Cut along the dotted line.', 'C', PS_MUTED);

    ps_doc_mark($p, $cx, $y + 84, 28, 42);
    $p->fit($cx, $y + 122, 'B', 21, $heading, $w - 70, 'C', PS_INK);
    ps_doc_rule($p, $cx, $y + 140, 30);

    $inner = $w - 84;
    $verseLines = $p->wrap('I', 11, $verse, $inner);
    $room = ($y + $h - 50) - ($y + 166) - (count($verseLines) * 15 + 54);      // what is left for the prayer
    for ($size = 15.0; $size > 10.5; $size -= 0.5) {
        $lines = $p->wrap('R', $size, $prayer, $inner);
        if (count($lines) * $size * 1.46 <= $room) {
            break;
        }
    }
    $lead = $size * 1.46;
    $yy = $y + 166 + $size + max(0.0, ($room - count($lines) * $lead) / 2);
    foreach ($lines as $l) {
        $p->put($cx, $yy, 'R', $size, $l, 'C', PS_INK);
        $yy += $lead;
    }
    $vy = $y + $h - 50 - count($verseLines) * 15 - 30;
    ps_doc_rule($p, $cx, $vy, 22);
    $vy += 22;
    foreach ($verseLines as $l) {
        $p->put($cx, $vy, 'I', 11, $l, 'C', PS_SOFT);
        $vy += 15;
    }
    $p->text($cx, $vy + 2, 'R', 7.5, mb_strtoupper($ref), 'C', PS_BRONZE, 1.8);
    $p->fit($cx, $y + $h - 30, 'I', 9, ps_fill((string) ($c['footer'] ?? ''), $o), $w - 70, 'C', PS_MUTED);
    return $p->output();
}

// ------------------------------------------------------------------ the nine day companion

function ps_pdf_companion(): string
{
    $b = ps_bonus_copy();
    $c = $b['companion'] ?? [];
    $days = $b['days'] ?? [];
    $close = $b['close'] ?? [];
    $blank = str_repeat('_', 16);
    $cx = PsPdf::W / 2;
    $left = 92.0;
    $textW = PsPdf::W - 2 * $left;
    $p = new PsPdf((string) ($c['cover_title'] ?? 'Nine Day Prayer Companion'));

    // cover
    $p->page();
    ps_doc_frame($p);
    $p->arch($cx, 330, 132, 196, PS_BRONZE, 1.2);
    $p->arch($cx, 330, 104, 164, PS_GOLD, 0.6);
    $p->arch($cx, 330, 40, 84, PS_BRONZE, 0.7);
    $p->line($cx - 86, 330, $cx + 86, 330, PS_BRONZE, 1.2);
    $p->fit($cx, 386, 'R', 9.5, mb_strtoupper((string) ($c['cover_kicker'] ?? '')), 440, 'C', PS_BRONZE, 2.6);
    $y = 432.0;
    foreach ($p->wrap('B', 34, (string) ($c['cover_title'] ?? ''), 430) as $l) {
        $p->put($cx, $y, 'B', 34, $l, 'C', PS_INK);
        $y += 40;
    }
    ps_doc_rule($p, $cx, $y - 14, 40);
    $p->para($cx, $y + 16, 'I', 14, 20, (string) ($c['cover_sub'] ?? ''), 380, 'C', PS_SOFT);

    // how to pray these nine days
    $p->page();
    ps_doc_frame($p);
    ps_doc_mark($p, $cx, 112);
    $p->fit($cx, 152, 'B', 23, (string) ($c['intro_h'] ?? ''), $textW, 'C', PS_INK);
    ps_doc_rule($p, $cx, 170);
    $y = 212.0;
    foreach ((array) ($c['intro_p'] ?? []) as $para) {
        $y = $p->para($left, $y, 'R', 14, 21.5, (string) $para, $textW, 'L', PS_INK) + 11;
    }

    // one page a day
    $total = count($days);
    foreach ($days as $i => $d) {
        $p->page();
        ps_doc_frame($p);
        $p->text($cx, 92, 'R', 9, sprintf('DAY %d OF %d', $i + 1, $total), 'C', PS_BRONZE, 2.6);
        $p->fit($cx, 128, 'B', 25, (string) ($d['title'] ?? ''), $textW, 'C', PS_INK);
        ps_doc_rule($p, $cx, 146);
        $y = 186.0;
        foreach ($p->wrap('I', 15, (string) ($d['verse'] ?? ''), 410) as $l) {
            $p->put($cx, $y, 'I', 15, $l, 'C', PS_SOFT);
            $y += 21.5;
        }
        $p->text($cx, $y + 3, 'R', 8, mb_strtoupper((string) ($d['ref'] ?? '')), 'C', PS_BRONZE, 2.0);
        $y += 44;
        $y = $p->para($left, $y, 'R', 14, 21.5, (string) ($d['reflection'] ?? ''), $textW, 'L', PS_INK) + 18;
        // the prayer: italic, set in from a bronze bar
        $start = $y - 13;
        $y = $p->para($left + 20, $y, 'I', 14.5, 22, str_replace('{blank}', $blank, (string) ($d['prayer'] ?? '')), $textW - 20, 'L', PS_INK);
        $p->line($left + 4, $start, $left + 4, $y - 22 + 5, PS_BRONZE, 1.4);
        // the practice for the day, in a ruled box near the foot
        $lines = $p->wrap('R', 12.5, (string) ($d['practice'] ?? ''), $textW - 44);
        $boxH = count($lines) * 17 + 24;
        $boxY = max($y + 14, 690 - $boxH);
        $p->rect($left, $boxY, $textW, $boxH, PS_GOLD, 0.6);
        $ly = $boxY + 12 + 12;
        foreach ($lines as $l) {
            $p->put($cx, $ly, 'R', 12.5, $l, 'C', PS_DEEP);
            $ly += 17;
        }
    }

    // closing page
    if ($close) {
        $p->page();
        ps_doc_frame($p);
        ps_doc_mark($p, $cx, 250, 36, 54);
        $p->fit($cx, 296, 'B', 23, (string) ($close['h'] ?? ''), $textW, 'C', PS_INK);
        ps_doc_rule($p, $cx, 314);
        $y = 356.0;
        foreach ((array) ($close['p'] ?? []) as $para) {
            $y = $p->para($cx, $y, 'R', 14, 21.5, (string) $para, $textW - 30, 'C', PS_INK) + 11;
        }
    }
    return $p->output();
}
