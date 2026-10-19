<?php
// A small PDF writer for the three printables, with no library behind it (the host has no Composer).
// US Letter pages, the four built in Times faces, lines and curves. Coordinates are in points
// measured from the TOP left of the page, which is easier to lay out than PDF's bottom left.
declare(strict_types=1);

final class PsPdf
{
    public const W = 612.0;
    public const H = 792.0;
    private const FONTS = ['R' => 'Times-Roman', 'I' => 'Times-Italic', 'B' => 'Times-Bold', 'BI' => 'Times-BoldItalic'];

    /** @var string[] one content stream per page */
    private array $pages = [];
    private array $widths;
    private string $title;

    public function __construct(string $title)
    {
        $this->widths = require __DIR__ . '/pdf_widths.php';
        $this->title = $title;
    }

    public function page(): void
    {
        $this->pages[] = '';
    }

    public function pageCount(): int
    {
        return count($this->pages);
    }

    /** UTF-8 in, Windows-1252 bytes out (the encoding the built in fonts are set to). */
    public static function enc(string $s): string
    {
        $s = strtr($s, ["\u{2014}" => ', ', "\u{2013}" => ' to ', "\u{00A0}" => ' ', "\u{2009}" => ' ']);
        $out = function_exists('iconv') ? @iconv('UTF-8', 'Windows-1252//TRANSLIT//IGNORE', $s) : false;
        if ($out === false || $out === '') {
            $out = function_exists('mb_convert_encoding') ? mb_convert_encoding($s, 'Windows-1252', 'UTF-8') : preg_replace('/[^\x20-\x7E]/', '', $s);
        }
        return (string) preg_replace('/[\x00-\x1F]/', ' ', (string) $out);
    }

    /** Width in points of already encoded bytes. */
    public function width(string $font, float $size, string $bytes, float $spacing = 0.0): float
    {
        $w = $this->widths[self::FONTS[$font]];
        $sum = 0;
        $n = strlen($bytes);
        for ($i = 0; $i < $n; $i++) {
            $c = ord($bytes[$i]);
            $sum += $c >= 32 ? $w[$c - 32] : 0;
        }
        return $sum * $size / 1000 + $spacing * $n;
    }

    /** Break text into lines no wider than $max. Returns encoded lines. */
    public function wrap(string $font, float $size, string $text, float $max): array
    {
        $lines = [];
        $line = '';
        foreach (preg_split('/ +/', trim(self::enc($text))) as $word) {
            $try = $line === '' ? $word : "$line $word";
            if ($line !== '' && $this->width($font, $size, $try) > $max) {
                $lines[] = $line;
                $line = $word;
            } else {
                $line = $try;
            }
        }
        if ($line !== '') {
            $lines[] = $line;
        }
        return $lines;
    }

    private static function rgb(string $hex): string
    {
        $hex = ltrim($hex, '#');
        return sprintf('%.3F %.3F %.3F', hexdec(substr($hex, 0, 2)) / 255, hexdec(substr($hex, 2, 2)) / 255, hexdec(substr($hex, 4, 2)) / 255);
    }

    private function op(string $s): void
    {
        $this->pages[count($this->pages) - 1] .= $s . "\n";
    }

    /** Draw encoded bytes. $align: L, C or R, relative to $x. $y is the baseline. */
    public function put(float $x, float $y, string $font, float $size, string $bytes, string $align = 'L', string $color = '#2A1F1A', float $spacing = 0.0): void
    {
        if ($bytes === '') {
            return;
        }
        $w = $this->width($font, $size, $bytes, $spacing) - $spacing;      // no trailing gap after the last letter
        $x -= $align === 'C' ? $w / 2 : ($align === 'R' ? $w : 0);
        $esc = strtr($bytes, ['\\' => '\\\\', '(' => '\\(', ')' => '\\)']);
        $n = array_search($font, array_keys(self::FONTS), true) + 1;
        $this->op(sprintf('BT /F%d %.2F Tf %s rg %.3F Tc %.2F %.2F Td (%s) Tj ET', $n, $size, self::rgb($color), $spacing, $x, self::H - $y, $esc));
    }

    /** Draw UTF-8 text on one line. */
    public function text(float $x, float $y, string $font, float $size, string $text, string $align = 'L', string $color = '#2A1F1A', float $spacing = 0.0): void
    {
        $this->put($x, $y, $font, $size, self::enc($text), $align, $color, $spacing);
    }

    /** One line that shrinks until it fits $max. Returns the size used. */
    public function fit(float $x, float $y, string $font, float $size, string $text, float $max, string $align = 'C', string $color = '#2A1F1A', float $spacing = 0.0): float
    {
        $b = self::enc($text);
        while ($size > 8 && $this->width($font, $size, $b, $spacing) > $max) {
            $size -= 0.5;
        }
        $this->put($x, $y, $font, $size, $b, $align, $color, $spacing);
        return $size;
    }

    /** Wrapped paragraph. Returns the baseline y after the last line. */
    public function para(float $x, float $y, string $font, float $size, float $lead, string $text, float $max, string $align = 'L', string $color = '#2A1F1A'): float
    {
        foreach ($this->wrap($font, $size, $text, $max) as $line) {
            $this->put($x, $y, $font, $size, $line, $align, $color);
            $y += $lead;
        }
        return $y;
    }

    public function line(float $x1, float $y1, float $x2, float $y2, string $color = '#9A7B4F', float $w = 0.6): void
    {
        $this->op(sprintf('%s RG %.2F w %.2F %.2F m %.2F %.2F l S', self::rgb($color), $w, $x1, self::H - $y1, $x2, self::H - $y2));
    }

    public function rect(float $x, float $y, float $w, float $h, string $color = '#9A7B4F', float $lw = 0.8, ?array $dash = null, ?string $fill = null): void
    {
        $d = $dash ? sprintf('[%s] 0 d ', implode(' ', $dash)) : '';
        $box = sprintf('%.2F %.2F %.2F %.2F re', $x, self::H - $y - $h, $w, $h);
        if ($fill !== null) {
            $this->op(sprintf('%s rg %s f', self::rgb($fill), $box));
        }
        $this->op(sprintf('q %s%s RG %.2F w %s S Q', $d, self::rgb($color), $lw, $box));
    }

    /** A small diamond, used as a divider mark. */
    public function diamond(float $cx, float $cy, float $r, string $color = '#C9A86A'): void
    {
        $y = self::H - $cy;
        $this->op(sprintf('%s rg %.2F %.2F m %.2F %.2F l %.2F %.2F l %.2F %.2F l f', self::rgb($color), $cx - $r, $y, $cx, $y + $r, $cx + $r, $y, $cx, $y - $r));
    }

    /** The Sanctoria church window: a pointed arch standing on $baseY, $w wide and $h tall. */
    public function arch(float $cx, float $baseY, float $w, float $h, string $color = '#9A7B4F', float $lw = 0.9): void
    {
        $l = $cx - $w / 2;
        $r = $cx + $w / 2;
        $b = self::H - $baseY;
        $s = $b + $h * 0.42;            // where the straight sides end
        $t = $b + $h;                   // the point
        $this->op(sprintf(
            '%s RG %.2F w 1 j %.2F %.2F m %.2F %.2F l %.2F %.2F %.2F %.2F %.2F %.2F c %.2F %.2F %.2F %.2F %.2F %.2F c %.2F %.2F l S',
            self::rgb($color), $lw,
            $l, $b, $l, $s,
            $l, $s + ($t - $s) * 0.62, $cx - $w * 0.16, $t - ($t - $s) * 0.12, $cx, $t,
            $cx + $w * 0.16, $t - ($t - $s) * 0.12, $r, $s + ($t - $s) * 0.62, $r, $s,
            $r, $b
        ));
    }

    public function output(): string
    {
        $objs = [];
        $objs[1] = '<< /Type /Catalog /Pages 2 0 R >>';
        $objs[2] = '';                                                           // filled in below
        $fontRefs = '';
        $n = 3;
        foreach (array_values(self::FONTS) as $i => $base) {
            $objs[$n] = "<< /Type /Font /Subtype /Type1 /BaseFont /$base /Encoding /WinAnsiEncoding >>";
            $fontRefs .= sprintf('/F%d %d 0 R ', $i + 1, $n);
            $n++;
        }
        $kids = [];
        foreach ($this->pages as $stream) {
            $filter = '';
            if (function_exists('gzcompress')) {
                $stream = gzcompress($stream, 6);
                $filter = ' /Filter /FlateDecode';
            }
            $objs[$n] = sprintf("<< /Length %d%s >>\nstream\n%s\nendstream", strlen($stream), $filter, $stream);
            $objs[$n + 1] = sprintf('<< /Type /Page /Parent 2 0 R /MediaBox [0 0 %d %d] /Resources << /Font << %s>> >> /Contents %d 0 R >>', self::W, self::H, $fontRefs, $n);
            $kids[] = ($n + 1) . ' 0 R';
            $n += 2;
        }
        $objs[2] = sprintf('<< /Type /Pages /Kids [%s] /Count %d >>', implode(' ', $kids), count($kids));
        $info = $n;
        $objs[$info] = sprintf('<< /Title (%s) /Author (Sanctoria) /Creator (Sanctoria) >>', strtr(self::enc($this->title), ['\\' => '\\\\', '(' => '\\(', ')' => '\\)']));

        ksort($objs);
        $pdf = "%PDF-1.4\n%\xE2\xE3\xCF\xD3\n";
        $offsets = [];
        foreach ($objs as $id => $body) {
            $offsets[$id] = strlen($pdf);
            $pdf .= "$id 0 obj\n$body\nendobj\n";
        }
        $xref = strlen($pdf);
        $pdf .= sprintf("xref\n0 %d\n0000000000 65535 f \n", count($objs) + 1);
        foreach ($offsets as $off) {
            $pdf .= sprintf("%010d 00000 n \n", $off);
        }
        $pdf .= sprintf("trailer\n<< /Size %d /Root 1 0 R /Info %d 0 R >>\nstartxref\n%d\n%%%%EOF\n", count($objs) + 1, $info, $xref);
        return $pdf;
    }
}
