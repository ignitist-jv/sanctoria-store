<?php
// Streams one song, to play or (with dl=1) to download. The file lives outside
// the web root and is only ever served to someone holding its token.
declare(strict_types=1);
require_once __DIR__ . '/lib.php';

$token = (string) ($_GET['k'] ?? '');
$o = ps_order($token);
$file = ps_data("songs/$token.mp3");
if (!$o || $o['status'] !== 'ready' || !is_file($file)) {
    http_response_code(404);
    exit;
}
$size = filesize($file);
$start = 0;
$end = $size - 1;
header('Content-Type: audio/mpeg');
header('Accept-Ranges: bytes');
header('Cache-Control: private, max-age=3600');
header('X-Robots-Tag: noindex');
if (!empty($_GET['dl'])) {
    $nice = preg_replace('/[^A-Za-z0-9 ]+/', '', (string) ($o['title'] ?? 'Prayer Song')) ?: 'Prayer Song';
    header('Content-Disposition: attachment; filename="' . trim($nice) . '.mp3"');
}
if (isset($_SERVER['HTTP_RANGE']) && preg_match('/bytes=(\d*)-(\d*)/', (string) $_SERVER['HTTP_RANGE'], $m)) {   // seeking, and iPhone playback
    if ($m[1] !== '') { $start = (int) $m[1]; }
    if ($m[2] !== '') { $end = min($size - 1, (int) $m[2]); }
    if ($start > $end || $start >= $size) {
        http_response_code(416);
        header("Content-Range: bytes */$size");
        exit;
    }
    http_response_code(206);
    header("Content-Range: bytes $start-$end/$size");
}
header('Content-Length: ' . ($end - $start + 1));
$h = fopen($file, 'rb');
fseek($h, $start);
$left = $end - $start + 1;
while ($left > 0 && !feof($h)) {
    $chunk = fread($h, (int) min(65536, $left));
    echo $chunk;
    $left -= strlen($chunk);
    flush();
}
fclose($h);
