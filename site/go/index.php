<?php
// A/B splitter: instant server-side 302, sticky via cookie, query string preserved.
$variants = ['/bracelet/', '/bracelet-v2/'];
$v = $_COOKIE['sanctoria_bracelet_variant'] ?? null;
if ($v !== '0' && $v !== '1') {
    $v = (string) random_int(0, 1);
    setcookie('sanctoria_bracelet_variant', $v, time() + 60*60*24*90, '/');
}
$qs = $_SERVER['QUERY_STRING'] ?? '';
header('Location: ' . $variants[(int)$v] . ($qs !== '' ? '?' . $qs : ''), true, 302);
exit;
