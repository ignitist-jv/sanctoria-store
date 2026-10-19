<?php
// Stripe sends the buyer here after paying (the payment links' "after payment" address):
//   paid.php?session_id=cs_...
// The session is read back from Stripe with the secret key, so nobody can fake a purchase by
// typing an address. A paid session becomes her order and she goes straight to her song page.
// The webhook (stripe.php) makes the same order if she closes the tab first.

declare(strict_types=1);
require_once __DIR__ . '/lib.php';

header('Cache-Control: no-store');
// The payment step inside the form comes back with ?payment_intent=pi_... (and Stripe's own redirect_status).
$pid = (string) ($_GET['payment_intent'] ?? '');
if (preg_match('/^pi_[A-Za-z0-9]{10,200}$/', $pid)) {
    $pi = ps_stripe('GET', 'payment_intents/' . $pid);
    $token = $pi ? ps_order_for_stripe_pi($pi, 'stripe return') : null;
    if ($token !== null) {
        header('Location: ' . ps_song_url($token) . '&paid=1', true, 302);
        exit;
    }
    if (($pi['status'] ?? '') !== 'succeeded' && $pi !== null) {     // not paid after all (declined after a redirect): back to the form
        header('Location: ' . ps_config()['base_url'] . '/?pay=retry#create', true, 302);
        exit;
    }
    $sid = $pid;
} else {
    $sid = (string) ($_GET['session_id'] ?? '');
}
if (strpos($sid, 'pi_') !== 0 && !preg_match('/^cs_(test|live)_[A-Za-z0-9]{10,200}$/', $sid)) {
    header('Location: ' . ps_config()['base_url'] . '/s/?find=1', true, 302);
    exit;
}
$cs = strpos($sid, 'cs_') === 0 ? ps_stripe('GET', 'checkout/sessions/' . $sid) : null;
$token = $cs ? ps_order_for_stripe_session($cs, 'stripe return') : null;
if ($token !== null) {
    header('Location: ' . ps_song_url($token) . '&paid=1', true, 302);
    exit;
}
// Paid but not confirmed here (Stripe slow to answer, or a setting is wrong): never "not found" after paying.
require_once __DIR__ . '/pipeline.php';
$stamp = ps_data('idx/unproven-' . sha1($sid));
if (!is_file($stamp)) {
    touch($stamp);
    ps_log("paid: session NOT confirmed $sid");
    ps_alert('A buyer came back from Stripe but the payment could not be confirmed',
        "Stripe session $sid.\nShe was shown a thank you page. If Stripe shows this payment, the webhook should still make her order; check the admin page.");
}
header('Location: ' . ps_config()['base_url'] . '/s/?thanks=1&via=stripe', true, 302);
