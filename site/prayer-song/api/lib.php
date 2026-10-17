<?php
/**
 * Sanctoria Prayer Song: shared back end library.
 *
 * One order = one unguessable token. The token is the only way to reach a
 * song: it names the order record, the audio file and the private page.
 *
 *   survey  -> lead.php   -> leads/<lid>.json            (answers, before payment)
 *   payment -> ins.php    -> orders/<token>.json + queue  (ClickBank notification)
 *           -> thanks.php -> same order, found by receipt (buyer's browser)
 *   cron    -> worker.php -> lyrics, render, check, songs/<token>.mp3, email
 *   buyer   -> /prayer-song/s/?k=<token>                  (play + download)
 *
 * Nothing here is reachable over HTTP: api/.htaccess denies this file, and the
 * data directory lives outside the web root when the host allows it.
 */

declare(strict_types=1);

const PS_RELATIONS  = ['husband', 'wife', 'son', 'daughter', 'grandchild', 'mother', 'father', 'friend', 'myself', 'passed'];
const PS_INTENTIONS = ['healing', 'protection', 'strength', 'peace', 'return', 'marriage', 'grief', 'thanksgiving'];
const PS_STYLES     = ['hymn', 'acoustic', 'gospel', 'country', 'lullaby', 'piano', 'folk', 'choir'];
const PS_VOICES     = ['female', 'male', 'either'];

function ps_config(): array
{
    static $c = null;
    if ($c !== null) {
        return $c;
    }
    $defaults = [
        'base_url'       => 'https://sanctoriastore.com/prayer-song',
        'data_dir'       => null,          // null = pick automatically, outside the web root if possible
        'items'          => ['prayersong-1' => 'song'],   // ClickBank item number => product
        'cb_secret_key'  => null,          // null = reuse site/ins/config.php
        'elevenlabs_key' => '',
        'music_model'    => 'music_v2_5',
        'mock'           => false,         // true = no ElevenLabs calls, placeholder audio (testing only)
        'anthropic_key'  => '',            // Claude API key: writes the lyrics. Without it no real song can be made
        'lyric_model'    => 'claude-opus-5-5',
        'credit_floor'   => 30000,         // ElevenLabs credits (about 10 songs): alert TS when the balance falls below this
        'max_attempts'   => 3,
        'slots'          => 2,             // songs rendered at the same time
        'delay_after'    => 900,           // seconds before the "taking a little longer" email
        // A finished song is not sent the minute it is made (TS, 2026-10-08): the page and the email wait until this
        // long after the order. The song itself is still made straight away, so a problem shows up early.
        'send_after'         => 7200,      // seconds after the order, standard
        'send_after_express' => 3600,      // seconds after the order when she added Express Song Delivery
        'express_items'      => ['express-1'],   // ClickBank item numbers of the express order bump
        // Stripe (TS, 2026-10-16): Payment Links send the buyer to Stripe, Stripe sends her back to api/paid.php
        // and notifies api/stripe.php. Keys live only in config.php on the server. A Stripe order is filed under
        // the ClickBank item "prayersong-1" so everything after payment is the same for both.
        'stripe'         => ['secret_key' => '', 'webhook_secret' => '', 'api_version' => '2024-06-20',
                             'links' => [],            // payment link id => 'song' | 'express'
                             'item' => 'prayersong-1',
                             'price_song' => 3900, 'price_express' => 995],   // US cents, for the payment step inside the form (api/pay.php)
        'mail'           => ['driver' => 'log', 'api_key' => '', 'from' => 'Sanctoria <songs@sanctoriastore.com>',
                             'reply_to' => 'support@sanctoriastore.com'],
        'admin_email'    => '',
        'admin_hash'     => '',            // password_hash() of the admin page password. Empty = the admin page does not exist
        // ClickMagick: each Stripe sale is reported server to server with the buyer's visitor id, so ClickMagick (and the
        // Meta conversions it sends) know which ad made it. ClickBank sales reach ClickMagick by ClickBank's own feed instead.
        // The Sales Endpoint URL from ClickMagick, Tools, Webhooks, Incoming (confirmed by TS's screenshot 2026-10-17).
        'clickmagick'    => ['postback' => 'https://www.clkmg.com/api/s/post/', 'uid' => '92654', 'ref' => 'sale', 'project' => 'Sanctoria Store'],
        'kit'            => ['api_key' => null, 'tag_lead' => null, 'tag_buyer' => 24391266,   // Kit tag sanctoria-prayersong-1
                             'tag_all_buyers' => 22564421,                                     // Kit tag sanctoria-buyer, shared by every Sanctoria offer
                             // Unfinished orders (TS, 2026-10-17): someone who reached the Pay step and did not pay gets up to three
                             // reminders. The worker sends each one only while she still has no order, so a buyer never gets a later one.
                             // One single-email sequence per reminder; the tag marks who has been reminded.
                             'abandon' => ['after' => [3600, 86400, 259200], 'seqs' => [2932904, 2932905, 2932907],
                                           'tag' => 24734384, 'field_resume' => 'prayer_song_resume_link', 'max_age' => 345600,
                                           'since' => 0],     // 0 = off. Set to a time (in config.php) to remind only forms filled in after it
                             'seq_ready' => 2917156, 'seq_delay' => 2917157,
                             'from_email' => 'admin@sanctoriastore.com',        // the address the Kit emails are sent from: shown to the buyer so she can look for it          // Kit sequence ids, used when mail driver is "kit"
                             'fields' => ['url' => 'prayer_song_link', 'title' => 'prayer_song_title',
                                          'name' => 'prayer_song_for', 'intention' => 'prayer_song_intention']],
    ];
    $file = __DIR__ . '/config.php';
    $c = array_replace_recursive($defaults, is_file($file) ? (array) require $file : []);
    $c['kit']['tag_buyer'] = $c['kit']['tag_buyer'] ?? $defaults['kit']['tag_buyer'];   // a null in config.php means "the usual one"

    // Environment overrides, used by the local test run.
    if (($v = getenv('PS_DATA_DIR')) !== false && $v !== '') { $c['data_dir'] = $v; }
    if (($v = getenv('PS_BASE_URL')) !== false && $v !== '') { $c['base_url'] = $v; }
    if (($v = getenv('PS_MOCK')) !== false && $v !== '')     { $c['mock'] = $v === '1'; }
    if (($v = getenv('PS_CB_SECRET')) !== false && $v !== '') { $c['cb_secret_key'] = $v; }
    if (($v = getenv('PS_ELEVENLABS_KEY')) !== false && $v !== '') { $c['elevenlabs_key'] = $v; }
    if (($v = getenv('PS_ANTHROPIC_KEY')) !== false && $v !== '') { $c['anthropic_key'] = $v; }
    if (($v = getenv('PS_ADMIN_HASH')) !== false && $v !== '') { $c['admin_hash'] = $v; }
    if (($v = getenv('PS_ABANDON_SINCE')) !== false && $v !== '') { $c['kit']['abandon']['since'] = (int) $v; }
    if (($v = getenv('PS_ABANDON_AFTER')) !== false && $v !== '') { $c['kit']['abandon']['after'] = array_map('intval', explode(',', $v)); }
    if (($v = getenv('PS_CM_POSTBACK')) !== false && $v !== '') { $c['clickmagick']['postback'] = $v; }
    if (($v = getenv('PS_STRIPE_SK')) !== false && $v !== '') { $c['stripe']['secret_key'] = $v; }
    if (($v = getenv('PS_STRIPE_WHSEC')) !== false && $v !== '') { $c['stripe']['webhook_secret'] = $v; }
    if (($v = getenv('PS_STRIPE_LINKS')) !== false && $v !== '') { $c['stripe']['links'] = (array) json_decode($v, true); }
    if (($v = getenv('PS_SEND_AFTER')) !== false && $v !== '') { $c['send_after'] = (int) $v; $c['send_after_express'] = (int) ((int) $v / 2); }

    if ($c['cb_secret_key'] === null || $c['kit']['api_key'] === null) {
        $shared = __DIR__ . '/../../ins/config.php';
        $s = is_file($shared) ? (array) require $shared : [];
        $c['cb_secret_key']  = $c['cb_secret_key'] ?? ($s['cb_secret_key'] ?? '');
        $c['kit']['api_key'] = $c['kit']['api_key'] ?? ($s['kit_api_key'] ?? '');
    }
    $c['base_url'] = rtrim((string) $c['base_url'], '/');
    return $c;
}

/** The data directory. Outside the web root when writable, otherwise api/data (denied by .htaccess). */
function ps_data(string $sub = ''): string
{
    static $root = null;
    if ($root === null) {
        $cfg = ps_config();
        $candidates = array_filter([
            $cfg['data_dir'],
            !empty($_SERVER['DOCUMENT_ROOT']) ? dirname((string) $_SERVER['DOCUMENT_ROOT']) . '/prayer-song-data' : null,
            dirname(__DIR__, 3) . '/prayer-song-data',
            __DIR__ . '/data',
        ]);
        foreach ($candidates as $dir) {
            if ((is_dir($dir) || @mkdir($dir, 0700, true)) && is_writable($dir)) {
                $root = $dir;
                break;
            }
        }
        if ($root === null) {
            throw new RuntimeException('no writable data directory');
        }
        foreach (['leads', 'orders', 'songs', 'queue', 'wait', 'idx', 'outbox', 'locks'] as $d) {
            if (!is_dir("$root/$d")) {
                @mkdir("$root/$d", 0700, true);
            }
        }
        if (!is_file("$root/.htaccess")) {
            @file_put_contents("$root/.htaccess", "Require all denied\n");
        }
    }
    return $sub === '' ? $root : "$root/$sub";
}

function ps_log(string $line): void
{
    @file_put_contents(ps_data('log.txt'), date('c') . ' ' . $line . PHP_EOL, FILE_APPEND | LOCK_EX);
}

function ps_token(): string
{
    return bin2hex(random_bytes(16));       // 128 bits: cannot be guessed or enumerated
}

function ps_is_token(?string $t): bool
{
    return is_string($t) && preg_match('/^[a-f0-9]{32}$/', $t) === 1;
}

function ps_read(string $path): ?array
{
    if (!is_file($path)) {
        return null;
    }
    $j = json_decode((string) file_get_contents($path), true);
    return is_array($j) ? $j : null;
}

/** Atomic write: a reader never sees half a file. */
function ps_write(string $path, array $data): void
{
    $tmp = $path . '.' . bin2hex(random_bytes(4)) . '.tmp';
    file_put_contents($tmp, json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES), LOCK_EX);
    rename($tmp, $path);
}

/** Run $fn while holding an exclusive lock named $name. Returns $fn's result. */
function ps_locked(string $name, callable $fn)
{
    $h = fopen(ps_data('locks/' . preg_replace('/[^a-z0-9_-]/i', '_', $name) . '.lock'), 'c');
    flock($h, LOCK_EX);
    try {
        return $fn();
    } finally {
        flock($h, LOCK_UN);
        fclose($h);
    }
}

function ps_clean(string $s, int $max): string
{
    $s = preg_replace('/[\x00-\x1F\x7F<>]/u', ' ', $s) ?? '';
    $s = trim(preg_replace('/\s+/u', ' ', $s) ?? '');
    return mb_substr($s, 0, $max);
}

function ps_song_url(string $token): string
{
    return ps_config()['base_url'] . '/s/?k=' . $token;
}

// ---------------------------------------------------------------- leads

/** Validate the survey answers. Returns [answers, error]. */
/** A name typed all in small letters or all in capitals is given normal capitals ("daniel" => "Daniel"). Mixed case is hers and is kept ("McKenna"). */
function ps_name_case(string $n): string
{
    if ($n !== '' && ($n === mb_strtolower($n) || $n === mb_strtoupper($n))) {
        return mb_convert_case($n, MB_CASE_TITLE, 'UTF-8');
    }
    return $n;
}

function ps_answers(array $in): array
{
    $a = [
        'who'           => (string) ($in['who'] ?? ''),
        'name'          => ps_name_case(ps_clean((string) ($in['name'] ?? ''), 40)),
        'name_phonetic' => ps_clean((string) ($in['name_phonetic'] ?? ''), 60),
        // a song may carry a second first name (TS, 2026-10-07): never more than two
        'name2'         => ps_name_case(ps_clean((string) ($in['name2'] ?? ''), 40)),
        'who2'          => (string) ($in['who2'] ?? ''),
        'name2_phonetic' => ps_clean((string) ($in['name2_phonetic'] ?? ''), 60),
        'intention'     => (string) ($in['intention'] ?? ''),
        'note'          => ps_clean((string) ($in['note'] ?? ''), 400),
        'style'         => (string) ($in['style'] ?? ''),
        'voice'         => (string) ($in['voice'] ?? ''),
    ];
    if (!in_array($a['who'], PS_RELATIONS, true))        { return [null, 'who']; }
    if ($a['name'] === '')                               { return [null, 'name']; }
    if (!in_array($a['intention'], PS_INTENTIONS, true)) { return [null, 'intention']; }
    if (!in_array($a['style'], PS_STYLES, true))         { $a['style'] = 'hymn'; }
    if (!in_array($a['voice'], PS_VOICES, true))         { $a['voice'] = 'either'; }
    // A second name is not offered when the song is for the buyer herself or for someone who has died.
    if (in_array($a['who'], ['myself', 'passed'], true) || mb_strtolower($a['name2']) === mb_strtolower($a['name'])) {
        $a['name2'] = '';
    }
    if ($a['name2'] === '') {
        $a['who2'] = '';
        $a['name2_phonetic'] = '';
    } elseif (!in_array($a['who2'], PS_RELATIONS, true) || $a['who2'] === 'passed' || ($a['who2'] === 'myself' && $a['who'] === 'myself')) {
        $a['who2'] = '';
    }
    if ($a['who'] === 'passed' && !in_array($a['intention'], ['grief', 'peace', 'thanksgiving'], true)) {
        $a['intention'] = 'peace';
    }
    return [$a, null];
}

function ps_email_key(string $email): string
{
    return sha1(strtolower(trim($email)));
}

function ps_save_lead(array $answers, string $email, string $buyer, string $vid = ''): string
{
    $lid = ps_token();
    ps_write(ps_data("leads/$lid.json"), [
        'lid' => $lid, 'created' => time(), 'email' => strtolower(trim($email)),
        'buyer' => ps_clean($buyer, 40), 'answers' => $answers,
        'vid' => preg_match('/^cmc[A-Za-z0-9]{1,40}$/', $vid) ? $vid : null,     // ClickMagick visitor id, for sale attribution
    ]);
    if ($email !== '') {
        file_put_contents(ps_data('idx/email-' . ps_email_key($email)), $lid, LOCK_EX);   // latest lead for this address
    }
    return $lid;
}

function ps_find_lead(?string $lid, string $email): ?array
{
    if (ps_is_token($lid) && ($l = ps_read(ps_data("leads/$lid.json")))) {
        return $l;
    }
    $idx = ps_data('idx/email-' . ps_email_key($email));
    if ($email !== '' && is_file($idx)) {
        $lid = trim((string) file_get_contents($idx));
        if (ps_is_token($lid)) {
            return ps_read(ps_data("leads/$lid.json"));
        }
    }
    return null;
}

// ---------------------------------------------------------------- orders

function ps_order(string $token): ?array
{
    return ps_is_token($token) ? ps_read(ps_data("orders/$token.json")) : null;
}

function ps_save_order(array $o): void
{
    $o['updated'] = time();
    ps_write(ps_data("orders/{$o['token']}.json"), $o);
}

function ps_note(array &$o, string $msg): void
{
    $o['log'][] = date('c') . ' ' . $msg;
}

function ps_enqueue(string $token): void
{
    touch(ps_data("queue/$token"));
}

/**
 * Create the order for a ClickBank receipt, or return the one that already
 * exists. Both the notification (ins.php) and the buyer's browser (thanks.php)
 * call this, in either order, and always land on the same token.
 */
function ps_order_for_receipt(string $receipt, string $item, string $email, string $buyer, ?string $lid, string $via): string
{
    $key = 'receipt-' . sha1($receipt . '|' . $item);
    return ps_locked($key, function () use ($key, $receipt, $item, $email, $buyer, $lid, $via) {
        $idx = ps_data("idx/$key");
        if (is_file($idx)) {
            $token = trim((string) file_get_contents($idx));
            $o = ps_order($token);
            if ($o) {
                $changed = false;
                if ($o['email'] === '' && $email !== '') { $o['email'] = strtolower($email); ps_index_order($o); $changed = true; }
                if ($o['status'] === 'needs_answers' && ($lead = ps_find_lead($lid, $email))) {
                    $o['answers'] = $lead['answers'];
                    $o['lid'] = $lead['lid'];
                    $o['buyer'] = $o['buyer'] ?: $lead['buyer'];
                    $o['status'] = 'queued';
                    ps_enqueue($token);
                    $changed = true;
                }
                if ($changed) {
                    ps_note($o, "updated via $via");
                    ps_save_order($o);
                }
                return $token;
            }
        }
        $lead  = ps_find_lead($lid, $email);
        $token = ps_token();
        $o = [
            'token' => $token, 'receipt' => $receipt, 'item' => $item,
            'product' => ps_config()['items'][$item] ?? 'song',
            'email' => strtolower(trim($email ?: ($lead['email'] ?? ''))),
            'buyer' => ps_clean($lead['buyer'] ?? '' ?: explode(' ', trim($buyer))[0], 40),
            'lid' => $lead['lid'] ?? null,
            'vid' => $lead['vid'] ?? null,
            'answers' => $lead['answers'] ?? null,
            'status' => $lead ? 'queued' : 'needs_answers',
            'created' => time(), 'attempts' => 0, 'lyrics' => null, 'title' => null,
            'emailed' => false, 'delay_sent' => false, 'refunded' => false, 'log' => [],
            'express' => is_file(ps_data('idx/express-' . sha1(explode('-', $receipt)[0]))),
        ];
        ps_note($o, "created via $via" . ($lead ? '' : ' (no survey answers matched)'));
        ps_save_order($o);
        file_put_contents($idx, $token, LOCK_EX);
        ps_index_order($o);
        if ($lead) {
            ps_enqueue($token);
        }
        ps_log("order $token receipt=$receipt item=$item status={$o['status']} via=$via");
        return $token;
    });
}

/** A refund is recorded on the order. The song link is left working. */
function ps_mark_refunded(string $receipt, string $item, string $why): void
{
    $idx = ps_data('idx/receipt-' . sha1($receipt . '|' . $item));
    $token = is_file($idx) ? trim((string) file_get_contents($idx)) : '';
    if ($token !== '') {
        ps_locked("order-$token", function () use ($token, $why) {
            if ($o = ps_order($token)) {
                $o['refunded'] = true;
                ps_note($o, $why);
                ps_save_order($o);
            }
        });
    }
    ps_log("refund receipt=$receipt item=$item: $why");
}

// ---------------------------------------------------------------- Stripe

/** Call the Stripe API. Returns the decoded body, or null on any failure. */
function ps_stripe(string $method, string $path, array $data = []): ?array
{
    $s = ps_config()['stripe'];
    if ($s['secret_key'] === '') {
        return null;
    }
    $url = 'https://api.stripe.com/v1/' . $path;
    $body = null;
    if ($method === 'GET' && $data) { $url .= '?' . http_build_query($data); } elseif ($data) { $body = http_build_query($data); }
    $r = ps_http($method, $url, ['Authorization: Bearer ' . $s['secret_key'], 'Stripe-Version: ' . $s['api_version'],
                                 'Content-Type: application/x-www-form-urlencoded'], $body, 30);
    [$code, $resp] = $r;
    $j = json_decode((string) $resp, true);
    return $code === 200 && is_array($j) ? $j : null;
}

/** Check a webhook's Stripe-Signature header (t=...,v1=...) against the endpoint secret, within five minutes. */
function ps_stripe_signed(string $payload, string $header): bool
{
    $secret = ps_config()['stripe']['webhook_secret'];
    if ($secret === '' || $header === '') {
        return false;
    }
    $t = null; $sigs = [];
    foreach (explode(',', $header) as $part) {
        [$k, $v] = array_pad(explode('=', trim($part), 2), 2, '');
        if ($k === 't') { $t = $v; } elseif ($k === 'v1') { $sigs[] = $v; }
    }
    if (!ctype_digit((string) $t) || abs(time() - (int) $t) > 300) {
        return false;
    }
    $want = hash_hmac('sha256', "$t.$payload", $secret);
    foreach ($sigs as $s) {
        if (hash_equals($want, $s)) {
            return true;
        }
    }
    return false;
}

/**
 * Tell ClickMagick about a Stripe sale, once per order: GET <postback>?uid=..&s1=<visitor id>&amt=<dollars>&ref=sale.
 * Without a visitor id (no tracker, blocked cookies) there is nothing to attribute it to, and that is noted on the order.
 */
function ps_report_sale(string $token, int $cents): void
{
    ps_locked("order-$token", function () use ($token, $cents) {
        $o = ps_order($token);
        if (!$o || !empty($o['cm_reported'])) {
            return;
        }
        $cm = ps_config()['clickmagick'];
        // s1 is the visitor id, or her email when there is none; cmc_project files an unmatched sale as organic
        // instead of dropping it (ClickMagick KB 793).
        $vid = (string) ($o['vid'] ?? '');
        $s1 = $vid !== '' ? $vid : (string) ($o['email'] ?? '');
        if ($s1 === '') {
            $o['cm_reported'] = 'no visitor id or email';
            ps_note($o, 'ClickMagick: not reported, no visitor id or email');
        } else {
            $url = $cm['postback'] . (strpos($cm['postback'], '?') === false ? '?' : '&')
                 . http_build_query(['uid' => $cm['uid'], 's1' => $s1, 'ref' => $cm['ref'], 'amt' => number_format($cents / 100, 2, '.', ''),
                                     'cmc_currency' => 'USD', 'cmc_project' => $cm['project']]);
            [$code] = ps_http('GET', $url, [], null, 15);
            $o['cm_reported'] = ($code >= 200 && $code < 300 ? 'yes' : "failed ($code)") . ($vid === '' ? ', by email' : '');
            ps_note($o, "ClickMagick sale report: {$o['cm_reported']}, " . number_format($cents / 100, 2));
        }
        ps_save_order($o);
    });
}

/**
 * A paid Stripe Checkout session becomes an order, or finds the one it already made. Both the return page and the
 * webhook call this, in either order. Returns the token, or null if the session is not a paid Prayer Song purchase.
 */
function ps_order_for_stripe_session(array $cs, string $via): ?string
{
    $s = ps_config()['stripe'];
    $kind = $s['links'][(string) ($cs['payment_link'] ?? '')] ?? null;
    if ($kind === null || ($cs['payment_status'] ?? '') !== 'paid' || empty($cs['payment_intent'])) {
        return null;
    }
    $receipt = (string) (is_array($cs['payment_intent']) ? ($cs['payment_intent']['id'] ?? '') : $cs['payment_intent']);
    if ($kind === 'express') {
        ps_mark_express($receipt);
    }
    $lid = (string) ($cs['client_reference_id'] ?? '');
    $email = (string) ($cs['customer_details']['email'] ?? ($cs['customer_email'] ?? ''));
    $name = (string) ($cs['customer_details']['name'] ?? '');
    $token = ps_order_for_receipt($receipt, $s['item'], $email, $name, $lid !== '' ? $lid : null, $via);
    ps_report_sale($token, (int) ($cs['amount_total'] ?? 0));
    return $token;
}

/**
 * A succeeded PaymentIntent from the payment step inside the form (api/pay.php made it) becomes an order, or finds the
 * one it already made. Called by the return page and by the webhook. Returns the token, or null if it is not ours.
 */
function ps_order_for_stripe_pi(array $pi, string $via): ?string
{
    $m = $pi['metadata'] ?? [];
    if (($m['offer'] ?? '') !== 'prayersong' || ($m['flow'] ?? '') !== 'embed' || ($pi['status'] ?? '') !== 'succeeded' || empty($pi['id'])) {
        return null;
    }
    if (($m['express'] ?? '') === '1') {
        ps_mark_express((string) $pi['id']);
    }
    $lid = (string) ($m['lid'] ?? '');
    $token = ps_order_for_receipt((string) $pi['id'], ps_config()['stripe']['item'], (string) ($pi['receipt_email'] ?? ''), '',
        $lid !== '' ? $lid : null, $via);
    ps_report_sale($token, (int) ($pi['amount_received'] ?? ($pi['amount'] ?? 0)));
    return $token;
}

/** When this order's song may be shown and emailed: so long after the order, sooner with express delivery. */
function ps_send_at(array $o): int
{
    $c = ps_config();
    return (int) $o['created'] + (int) (ps_is_express($o) ? $c['send_after_express'] : $c['send_after']);
}

/** The flag on the order, or the mark left by the notification (which can land while the song is being made). */
function ps_is_express(array $o): bool
{
    return !empty($o['express']) || is_file(ps_data('idx/express-' . sha1(explode('-', (string) ($o['receipt'] ?? ''))[0])));
}

/** The words are shown on her page from halfway through the wait, the song at the end of it. */
function ps_lyrics_visible(array $o): bool
{
    if (empty($o['lyrics'])) {
        return false;
    }
    return !in_array($o['status'], ['queued', 'working', 'waiting'], true) || time() >= (int) (((int) $o['created'] + ps_send_at($o)) / 2);
}

/** She added Express Song Delivery. Called from the ClickBank notification, before or after the order exists. */
function ps_mark_express(string $receipt): void
{
    $base = explode('-', $receipt)[0];
    @touch(ps_data('idx/express-' . sha1($base)));
    foreach (array_keys(ps_config()['items']) as $item) {
        $idx = ps_data('idx/receipt-' . sha1($base . '|' . $item));
        $token = is_file($idx) ? trim((string) file_get_contents($idx)) : '';
        if ($token !== '') {
            ps_locked("order-$token", function () use ($token) {
                $o = ps_order($token);
                if ($o && empty($o['express'])) {
                    $o['express'] = true;
                    ps_note($o, 'express delivery added');
                    ps_save_order($o);
                }
            });
        }
    }
}

/** The order made from this lead, or any order for her email since she filled the form in. Null if she has not bought. */
function ps_lead_order(array $lead): ?array
{
    foreach (ps_orders_for_email((string) ($lead['email'] ?? '')) as $o) {
        if (($o['lid'] ?? '') === ($lead['lid'] ?? '-') || (int) $o['created'] >= (int) $lead['created'] - 86400) {
            return $o;
        }
    }
    return null;
}

/** The link in the reminder emails: opens the form with her saved answers, straight at the Pay step. */
function ps_resume_url(string $lid): string
{
    return ps_config()['base_url'] . '/?resume=' . $lid;
}

/** List an order under its buyer's email, so "find my song" can resend her links. */
function ps_index_order(array $o): void
{
    if (($o['email'] ?? '') !== '') {
        file_put_contents(ps_data('idx/orders-' . ps_email_key($o['email'])), $o['token'] . "\n", FILE_APPEND | LOCK_EX);
    }
}

/** Every order placed with this email address, newest first. */
function ps_orders_for_email(string $email): array
{
    $f = ps_data('idx/orders-' . ps_email_key($email));
    $out = [];
    foreach (is_file($f) ? array_unique(array_filter(array_map('trim', file($f)))) : [] as $t) {
        if ($o = ps_order($t)) { $out[] = $o; }
    }
    usort($out, fn($a, $b) => $b['created'] <=> $a['created']);
    return $out;
}

// ---------------------------------------------------------------- ClickBank

/** Decrypt an INS v6+ body. Returns the notification array, or null. */
function ps_ins_decrypt(string $raw): ?array
{
    $p = json_decode($raw, true);
    if (!is_array($p) || empty($p['notification']) || empty($p['iv'])) {
        return null;
    }
    $key = substr(sha1(ps_config()['cb_secret_key']), 0, 32);
    $iv = base64_decode((string) $p['iv'], true);
    $data = base64_decode((string) $p['notification'], true);
    if ($iv === false || strlen($iv) !== 16 || $data === false) {
        return null;
    }
    $plain = @openssl_decrypt($data, 'AES-256-CBC', $key, OPENSSL_RAW_DATA, $iv);
    if ($plain === false) {
        return null;
    }
    $n = json_decode(trim($plain, "\x00..\x1F"), true);
    return is_array($n) ? $n : null;
}

/** ClickBank's proof of purchase on the thank you URL: first 8 of sha1(secret|receipt|time|item), upper case. */
function ps_cbpop_ok(string $receipt, string $time, string $item, string $cbpop): bool
{
    $secret = ps_config()['cb_secret_key'];
    if ($secret === '' || $receipt === '' || $cbpop === '') {
        return false;
    }
    $expect = strtoupper(substr(sha1("$secret|$receipt|$time|$item"), 0, 8));
    return hash_equals($expect, strtoupper($cbpop));
}

// ---------------------------------------------------------------- HTTP

function ps_http(string $method, string $url, array $headers, $body = null, int $timeout = 60): array
{
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_CUSTOMREQUEST => $method, CURLOPT_HTTPHEADER => $headers,
        CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => $timeout, CURLOPT_CONNECTTIMEOUT => 15,
    ]);
    if ($body !== null) {
        curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
    }
    $resp = curl_exec($ch);
    $code = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $err  = curl_error($ch);
    return [$code, $resp === false ? '' : (string) $resp, $err];
}

/** Send an MP3 to the browser, honouring Range so that seeking and iPhone playback work. */
function ps_stream_mp3(string $file, ?string $downloadName = null): void
{
    $size = filesize($file);
    $start = 0;
    $end = $size - 1;
    header('Content-Type: audio/mpeg');
    header('Accept-Ranges: bytes');
    if ($downloadName !== null) {
        header('Content-Disposition: attachment; filename="' . $downloadName . '"');
    }
    if (isset($_SERVER['HTTP_RANGE']) && preg_match('/bytes=(\d*)-(\d*)/', (string) $_SERVER['HTTP_RANGE'], $m)) {
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
    }
    fclose($h);
    exit;
}

function ps_json_out(array $data, int $status = 200): void
{
    http_response_code($status);
    header('Content-Type: application/json');
    header('Cache-Control: no-store');
    echo json_encode($data);
    exit;
}

// ---------------------------------------------------------------- copy

function ps_copy(): array
{
    static $c = null;
    return $c ??= (ps_read(__DIR__ . '/copy.json') ?? []);
}

/** Fill {name} {buyer} {title} {intention_phrase} {link}. An empty {buyer} takes its comma with it. */
/** The first names a song carries: one, or two. */
function ps_names(array $a): array
{
    return array_values(array_filter([trim((string) ($a['name'] ?? '')), trim((string) ($a['name2'] ?? ''))], fn($n) => $n !== ''));
}

/** "Daniel", or "Daniel and Mary". */
function ps_names_text(array $a): string
{
    return implode(' and ', ps_names($a));
}

function ps_fill(string $t, array $o): string
{
    $phr = ps_copy()['phrases'] ?? [];
    $a = $o['answers'] ?? [];
    $buyer = (string) ($o['buyer'] ?? '');
    if ($buyer === '') {
        $t = preg_replace('/,?\s*\{buyer\}\s*,?\s*/', ' ', $t) ?? $t;
    }
    $t = strtr($t, [
        '{name}' => ps_names_text($a), '{buyer}' => $buyer, '{title}' => (string) ($o['title'] ?? ''),
        '{intention_phrase}' => (string) ($phr[$a['intention'] ?? ''] ?? ($a['intention'] ?? '')),
        '{link}' => ps_song_url((string) ($o['token'] ?? '')),
    ]);
    return trim(preg_replace('/\s{2,}/', ' ', $t) ?? $t);
}
