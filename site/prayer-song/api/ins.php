<?php
// ClickBank Instant Notification endpoint for the Prayer Song only.
// Add as an extra INS URL (version 6.0 or later):
//   https://sanctoriastore.com/prayer-song/api/ins.php
// The existing /ins/clickbank.php keeps doing the Kit buyer tagging for every
// Sanctoria product and is not touched. This one only creates song orders, and
// ignores every item that is not in config 'items'.

declare(strict_types=1);
require_once __DIR__ . '/lib.php';

$n = ps_ins_decrypt((string) file_get_contents('php://input'));
if ($n === null) {
    echo 'ok';                 // URL verification ping, or not for us
    exit;
}
$type    = strtoupper((string) ($n['transactionType'] ?? ''));
$receipt = (string) ($n['receipt'] ?? '');
$email   = (string) ($n['customer']['billing']['email'] ?? '');
$name    = (string) ($n['customer']['billing']['fullName'] ?? '');
$lid     = (string) ($n['vendorVariables']['lid'] ?? '');
$items   = ps_config()['items'];

// Express Song Delivery is an order bump: it arrives as a second line on the same receipt, or on its own.
if ($receipt !== '' && in_array($type, ['SALE', 'TEST_SALE', 'TEST'], true)) {
    foreach (($n['lineItems'] ?? []) as $li) {
        if (in_array((string) ($li['itemNo'] ?? ''), ps_config()['express_items'], true)) {
            ps_mark_express($receipt);
            ps_log("express receipt=$receipt");
            break;
        }
    }
}

foreach (($n['lineItems'] ?? []) as $li) {
    $item = (string) ($li['itemNo'] ?? '');
    if (!isset($items[$item]) || $receipt === '') {
        continue;
    }
    if (in_array($type, ['SALE', 'TEST_SALE', 'TEST'], true)) {
        ps_order_for_receipt($receipt, $item, $email, $name, $lid ?: null, 'ins');
    } elseif (in_array($type, ['RFND', 'CGBK', 'TEST_RFND'], true)) {
        ps_mark_refunded(explode('-', $receipt)[0], $item, "refund notification $type");
    }
}
echo 'ok';
