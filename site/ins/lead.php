<?php
// Sanctoria Store: chat funnel lead capture -> Kit (ConvertKit).
// Receives {first_name, email, match} from /chat/, creates the subscriber,
// applies the master lead tag plus the tag for whichever devotion she matched.
// The Kit API key stays here on the server and is never exposed to the page.

declare(strict_types=1);

header('Content-Type: application/json');

$config = require __DIR__ . '/config.php';

function lead_log(string $line): void
{
    @file_put_contents(__DIR__ . '/lead_log.txt', date('c') . ' ' . $line . PHP_EOL, FILE_APPEND);
}

function fail(int $status, string $publicMessage, string $logLine = ''): void
{
    if ($logLine !== '') { lead_log($logLine); }
    http_response_code($status);
    echo json_encode(['ok' => false, 'error' => $publicMessage]);
    exit;
}

function kit_post(string $url, array $body, string $apiKey): array
{
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => json_encode($body),
        CURLOPT_HTTPHEADER => [
            'Content-Type: application/json',
            'Accept: application/json',
            'X-Kit-Api-Key: ' . $apiKey,
        ],
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT => 15,
    ]);
    $resp = curl_exec($ch);
    $code = (int) curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
    curl_close($ch);
    return [$code, $resp];
}

// ---------------------------------------------------------------- guards

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    fail(405, 'Method not allowed');
}

$raw = file_get_contents('php://input');
if ($raw === false || strlen($raw) > 2000) {
    fail(400, 'Bad request', 'REJECT oversized or unreadable body');
}

$in = json_decode($raw, true);
if (!is_array($in)) {
    fail(400, 'Bad request', 'REJECT not json');
}

// Honeypot. Real visitors never fill this; bots fill everything.
if (!empty($in['company'])) {
    lead_log('REJECT honeypot');
    echo json_encode(['ok' => true]);   // answer as if fine, tell the bot nothing
    exit;
}

// Simple per-IP throttle so the endpoint cannot be used to spam the list.
$ip = substr((string) ($_SERVER['REMOTE_ADDR'] ?? 'unknown'), 0, 45);
$throttleFile = __DIR__ . '/lead_throttle.json';
$now = time();
$throttle = [];
if (is_readable($throttleFile)) {
    $decoded = json_decode((string) @file_get_contents($throttleFile), true);
    if (is_array($decoded)) { $throttle = $decoded; }
}
foreach ($throttle as $k => $stamps) {                       // drop anything older than an hour
    $throttle[$k] = array_values(array_filter($stamps, static fn($t) => $t > $now - 3600));
    if (!$throttle[$k]) { unset($throttle[$k]); }
}
if (count($throttle[$ip] ?? []) >= 12) {
    fail(429, 'Too many requests', "THROTTLED ip=$ip");
}
$throttle[$ip][] = $now;
@file_put_contents($throttleFile, json_encode($throttle), LOCK_EX);

// ---------------------------------------------------------------- input

$email = trim((string) ($in['email'] ?? ''));
$first = trim((string) ($in['first_name'] ?? ''));
$match = (string) ($in['match'] ?? '');

if (!filter_var($email, FILTER_VALIDATE_EMAIL) || strlen($email) > 160) {
    fail(422, 'That address does not look right');
}
$first = preg_replace('/[^\p{L}\p{M}\'\- ]/u', '', $first) ?? '';
$first = trim(mb_substr($first, 0, 60));

$leadTags = $config['kit_lead_tag_by_match'] ?? [];
if (!array_key_exists($match, $leadTags)) {
    $match = '';                                             // unknown match, master tag only
}

// ---------------------------------------------------------------- Kit

$apiKey = (string) ($config['kit_api_key'] ?? '');
if ($apiKey === '') {
    fail(500, 'Not configured', 'MISSING kit_api_key');
}

$results = [];

[$code, ] = kit_post('https://api.kit.com/v4/subscribers', array_filter([
    'email_address' => $email,
    'first_name'    => $first !== '' ? $first : null,
]), $apiKey);
$results[] = "sub:$code";

if (!empty($config['kit_tag_lead'])) {
    [$code, ] = kit_post(
        'https://api.kit.com/v4/tags/' . $config['kit_tag_lead'] . '/subscribers',
        ['email_address' => $email],
        $apiKey
    );
    $results[] = "tag-lead:$code";
}

if ($match !== '') {
    [$code, ] = kit_post(
        'https://api.kit.com/v4/tags/' . $leadTags[$match] . '/subscribers',
        ['email_address' => $email],
        $apiKey
    );
    $results[] = "tag-$match:$code";
}

lead_log('lead email=' . $email . ' match=' . ($match !== '' ? $match : 'none') . ' ' . implode(' ', $results));

echo json_encode(['ok' => true]);
