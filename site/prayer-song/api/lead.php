<?php
// Survey answers arrive here before checkout. Stored under a lead id that rides
// through ClickBank and comes back with the sale, so the right answers meet the
// right order. With an order token instead, the answers complete an order that
// was paid for without them.

declare(strict_types=1);
require_once __DIR__ . '/lib.php';

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    ps_json_out(['ok' => false, 'error' => 'method'], 405);
}
$in = json_decode((string) file_get_contents('php://input'), true);
if (!is_array($in)) {
    ps_json_out(['ok' => false, 'error' => 'body'], 400);
}

// Light throttle: 20 submissions per address per hour.
$ip = (string) ($_SERVER['REMOTE_ADDR'] ?? 'x');
$bucket = ps_data('idx/rate-' . sha1($ip . date('YmdH')));
$count = (int) @file_get_contents($bucket);
if ($count >= 20) {
    ps_json_out(['ok' => false, 'error' => 'slow down'], 429);
}
@file_put_contents($bucket, (string) ($count + 1), LOCK_EX);

[$answers, $bad] = ps_answers($in);
if ($answers === null) {
    ps_json_out(['ok' => false, 'error' => "missing $bad"], 422);
}
$email = strtolower(trim((string) ($in['email'] ?? '')));
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    ps_json_out(['ok' => false, 'error' => 'email'], 422);
}
$buyer = (string) ($in['buyer'] ?? '');
$lid = ps_save_lead($answers, $email, $buyer);

// Completing an order that was paid for before the survey was filled in.
$order = (string) ($in['order'] ?? '');
if (ps_is_token($order)) {
    $done = ps_locked("order-$order", function () use ($order, $answers, $lid, $buyer) {
        $o = ps_order($order);
        if (!$o || $o['status'] !== 'needs_answers') {
            return false;
        }
        $o['answers'] = $answers;
        $o['lid'] = $lid;
        $o['buyer'] = $o['buyer'] ?: ps_clean($buyer, 40);
        $o['status'] = 'queued';
        ps_note($o, 'answers added after purchase');
        ps_save_order($o);
        ps_enqueue($order);
        return true;
    });
    ps_json_out(['ok' => true, 'lead' => $lid, 'song' => $done ? ps_song_url($order) : null]);
}

// Tell Kit about the lead (optional, and never allowed to fail the request).
$kit = ps_config()['kit'];
if (!empty($kit['api_key']) && !empty($kit['tag_lead'])) {
    $h = ['Content-Type: application/json', 'Accept: application/json', 'X-Kit-Api-Key: ' . $kit['api_key']];
    ps_http('POST', 'https://api.kit.com/v4/subscribers', $h, json_encode(array_filter(['email_address' => $email, 'first_name' => ps_clean($buyer, 40)])), 10);
    ps_http('POST', "https://api.kit.com/v4/tags/{$kit['tag_lead']}/subscribers", $h, json_encode(['email_address' => $email]), 10);
}

setcookie('ps_lid', $lid, ['expires' => time() + 7 * 86400, 'path' => '/prayer-song/', 'secure' => !empty($_SERVER['HTTPS']), 'httponly' => true, 'samesite' => 'Lax']);
ps_json_out(['ok' => true, 'lead' => $lid]);
