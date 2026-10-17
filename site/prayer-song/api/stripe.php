<?php
// Stripe webhook for the Prayer Song. Register in Stripe (Developers, Webhooks) as
//   https://sanctoriastore.com/prayer-song/api/stripe.php
// with the events checkout.session.completed, checkout.session.async_payment_succeeded, payment_intent.succeeded
// and charge.refunded.
// Every event is checked against the endpoint's signing secret before anything is done with it.

declare(strict_types=1);
require_once __DIR__ . '/lib.php';

$payload = (string) file_get_contents('php://input');
if (!ps_stripe_signed($payload, (string) ($_SERVER['HTTP_STRIPE_SIGNATURE'] ?? ''))) {
    http_response_code(400);
    echo 'bad signature';
    exit;
}
$ev = json_decode($payload, true);
$type = (string) ($ev['type'] ?? '');
$obj = $ev['data']['object'] ?? [];

if (in_array($type, ['checkout.session.completed', 'checkout.session.async_payment_succeeded'], true)) {
    $token = ps_order_for_stripe_session($obj, 'stripe webhook');
    ps_log("stripe $type session=" . substr((string) ($obj['id'] ?? ''), 0, 80) . ' order=' . ($token ?? 'none (not ours, or not paid yet)'));
} elseif ($type === 'payment_intent.succeeded') {        // the payment step inside the form
    $token = ps_order_for_stripe_pi($obj, 'stripe webhook');
    if ($token !== null) {
        ps_log('stripe payment_intent.succeeded ' . substr((string) ($obj['id'] ?? ''), 0, 80) . " order=$token");
    }
} elseif ($type === 'charge.refunded') {
    $pi = (string) ($obj['payment_intent'] ?? '');
    if ($pi !== '') {
        ps_mark_refunded($pi, ps_config()['stripe']['item'], 'refunded in Stripe' . (empty($obj['refunded']) ? ' (part)' : ''));
    }
}
http_response_code(200);
echo 'ok';
