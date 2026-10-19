<?php
// ClickBank sends the buyer here after payment (set as the item's Thank You
// URL). The purchase is proven by ClickBank's cbpop signature, the order is
// created or found by its receipt, and she is sent to her private song page.
// Nothing is shown to anyone who cannot prove a purchase.

declare(strict_types=1);
require_once __DIR__ . '/lib.php';

$receipt = (string) ($_GET['cbreceipt'] ?? '');
$item    = (string) ($_GET['item'] ?? '');
$ok = ps_cbpop_ok($receipt, (string) ($_GET['time'] ?? ''), $item, (string) ($_GET['cbpop'] ?? ''));

if ($ok && isset(ps_config()['items'][$item])) {
    $lid = (string) ($_GET['lid'] ?? ($_COOKIE['ps_lid'] ?? ''));
    $token = ps_order_for_receipt($receipt, $item, (string) ($_GET['cemail'] ?? ''), (string) ($_GET['cname'] ?? ''), $lid ?: null, 'thanks');
    header('Cache-Control: no-store');
    header('Location: ' . ps_song_url($token), true, 302);
    exit;
}
header('Cache-Control: no-store');
if ($receipt !== '' && isset($_GET['cbpop'])) {
    // She came from the ClickBank checkout, but the purchase could not be confirmed here (a setting is wrong, or the item
    // is not one of ours). She must not be met with "not found" after paying: she gets a plain thank you that tells her to
    // watch for the email, and TS is told at once, because without a confirmed purchase no order has been made for her
    // unless ClickBank's notification also arrives.
    require_once __DIR__ . '/pipeline.php';
    $ref = preg_replace('/[^A-Za-z0-9-]/', '', $receipt);
    $stamp = ps_data('idx/unproven-' . sha1($ref));
    if (!is_file($stamp)) {
        touch($stamp);
        ps_log("thanks: purchase NOT confirmed receipt=$ref item=" . substr($item, 0, 30));
        ps_alert('A buyer reached the thank you page but the purchase could not be confirmed',
            "Receipt $ref, item \"" . substr($item, 0, 30) . "\", email " . substr((string) ($_GET['cemail'] ?? ''), 0, 120)
            . ".\nShe was shown a thank you page. Check the ClickBank secret key in the server settings, then look for her order in the admin page.");
    }
    header('Location: ' . ps_config()['base_url'] . '/s/?thanks=1&r=' . rawurlencode(substr($ref, 0, 24)), true, 302);
    exit;
}
// Nobody is sent here except by the checkout. A stray visitor gets the page that sends a song link again.
header('Location: ' . ps_config()['base_url'] . '/s/?find=1', true, 302);
