<?php
// "Find my song": she types the email used for the order and her private link is
// sent to that inbox again. The answer shown on screen is always the same, so the
// form can never be used to learn whether an address has an order, and a link is
// never shown on screen: it only ever goes to the inbox that owns it.

declare(strict_types=1);
require_once __DIR__ . '/pipeline.php';

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    ps_json_out(['ok' => false], 405);
}
$in = json_decode((string) file_get_contents('php://input'), true);
$email = strtolower(trim((string) ($in['email'] ?? '')));
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    ps_json_out(['ok' => false, 'error' => 'email'], 422);
}

// Five tries an hour per visitor, and one resend per address every ten minutes.
$bucket = ps_data('idx/find-' . sha1((string) ($_SERVER['REMOTE_ADDR'] ?? 'x') . date('YmdH')));
$n = (int) @file_get_contents($bucket);
@file_put_contents($bucket, (string) ($n + 1), LOCK_EX);
$stamp = ps_data('idx/found-' . ps_email_key($email));
$recent = is_file($stamp) && time() - filemtime($stamp) < 600;

if ($n < 5 && !$recent) {
    $sent = 0;
    foreach (ps_orders_for_email($email) as $o) {
        if ($o['status'] === 'ready' && $sent < 5) {       // one email per finished song, newest first
            [$ok, $d] = ps_send_order_mail($o, 'ready');
            ps_log("find: resent {$o['token']} " . ($ok ? 'ok' : "FAILED $d"));
            $sent++;
        }
    }
    if ($sent) { touch($stamp); }
}
ps_json_out(['ok' => true]);
