<?php
// Serves one of the three printables as a PDF, to someone holding the order's token.
//   bonus.php?k=<token>&f=sheet|card|companion      add &dl=1 to save instead of opening
// Nothing is stored: each PDF is drawn from the order when it is asked for, so a remade
// song always gets a lyric sheet that matches it.
declare(strict_types=1);
require_once __DIR__ . '/bonus_docs.php';

$o = ps_order((string) ($_GET['k'] ?? ''));
$f = (string) ($_GET['f'] ?? '');
if (!$o || $o['status'] !== 'ready' || !in_array($f, ['sheet', 'card', 'companion'], true) || empty(ps_copy()['bonus'])) {
    http_response_code(404);
    exit;
}
$title = trim((string) preg_replace('/[^A-Za-z0-9 ]+/', '', (string) ($o['title'] ?? 'Prayer Song'))) ?: 'Prayer Song';
$name = trim((string) preg_replace('/[^A-Za-z0-9 ]+/', '', ps_names_text($o['answers'] ?? [])));
switch ($f) {
    case 'sheet':
        $pdf = ps_pdf_sheet($o);
        $file = "$title Lyric Sheet.pdf";
        break;
    case 'card':
        $pdf = ps_pdf_card($o);
        $file = trim("Daily Prayer Card $name") . '.pdf';
        break;
    default:
        $pdf = ps_pdf_companion();
        $file = 'Nine Day Prayer Companion.pdf';
}
header('Content-Type: application/pdf');
header('Content-Length: ' . strlen($pdf));
header('Content-Disposition: ' . (empty($_GET['dl']) ? 'inline' : 'attachment') . '; filename="' . $file . '"');
header('Cache-Control: private, max-age=300');
header('X-Robots-Tag: noindex');
echo $pdf;
