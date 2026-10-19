<?php
// Prepares the payment for the Pay step inside the form. The page sends {lid, express}; the amount is decided here,
// never by the page, and the answers must already be saved under that lead id. Returns a PaymentIntent client secret,
// which Stripe's card and wallet fields on the page use to take the payment. Card details never reach this server.

declare(strict_types=1);
require_once __DIR__ . '/lib.php';

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    ps_json_out(['ok' => false, 'error' => 'method'], 405);
}
$ip = (string) ($_SERVER['REMOTE_ADDR'] ?? 'x');
$bucket = ps_data('idx/payrate-' . sha1($ip . date('YmdH')));
$count = (int) @file_get_contents($bucket);
if ($count >= 30) {
    ps_json_out(['ok' => false, 'error' => 'slow down'], 429);
}
@file_put_contents($bucket, (string) ($count + 1), LOCK_EX);

$in = json_decode((string) file_get_contents('php://input'), true);
$lid = (string) ($in['lid'] ?? '');
$lead = ps_is_token($lid) ? ps_read(ps_data("leads/$lid.json")) : null;
if (!$lead) {
    ps_json_out(['ok' => false, 'error' => 'answers'], 422);
}
$s = ps_config()['stripe'];
$express = !empty($in['express']);
$pi = ps_stripe('POST', 'payment_intents', [
    'amount' => (int) $s['price_song'] + ($express ? (int) $s['price_express'] : 0),
    'currency' => 'usd',
    'payment_method_types[0]' => 'card',     // cards, which Apple Pay and Google Pay ride on; no Link sign-up box under the card fields
    'receipt_email' => (string) $lead['email'],
    'description' => 'Your Prayer Song' . ($express ? ' with Express Song Delivery' : ''),
    'metadata[offer]' => 'prayersong', 'metadata[flow]' => 'embed', 'metadata[lid]' => $lid,
    'metadata[express]' => $express ? '1' : '0', 'metadata[vid]' => (string) ($lead['vid'] ?? ''),
]);
if (!$pi || empty($pi['client_secret'])) {
    ps_log('pay: could not create a PaymentIntent for lead ' . $lid);
    ps_json_out(['ok' => false, 'error' => 'stripe'], 502);
}
ps_json_out(['ok' => true, 'client_secret' => $pi['client_secret']]);
