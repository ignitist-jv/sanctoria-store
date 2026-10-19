<?php
// Sanctoria Store: ClickBank INS (v7) -> Kit (ConvertKit) buyer sync.
// Receives ClickBank Instant Notifications, decrypts them with the vendor
// secret key, and syncs SALE / TEST_SALE buyers into Kit with tier tags.
// Always answers 200 so ClickBank can verify the URL and does not retry-storm.

header('Content-Type: text/plain');

$config = require __DIR__ . '/config.php';

function ins_log(string $line): void
{
    $path = __DIR__ . '/log.txt';
    @file_put_contents($path, date('c') . ' ' . $line . "\n", FILE_APPEND | LOCK_EX);
}

function kit_post(string $url, array $body, string $apiKey): array
{
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => json_encode($body),
        CURLOPT_HTTPHEADER => [
            'Content-Type: application/json',
            'X-Kit-Api-Key: ' . $apiKey,
        ],
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT => 15,
    ]);
    $resp = curl_exec($ch);
    $code = curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
    curl_close($ch);
    return [$code, (string) $resp];
}

$raw = file_get_contents('php://input');
if ($raw === '' || $raw === false) {
    echo 'ok';
    exit;
}

$payload = json_decode($raw, true);
if (!is_array($payload) || empty($payload['notification']) || empty($payload['iv'])) {
    // ClickBank URL verification or malformed input: acknowledge and stop.
    ins_log('non-ins request acknowledged');
    echo 'ok';
    exit;
}

$key = substr(sha1($config['cb_secret_key']), 0, 32);
$plain = openssl_decrypt(
    base64_decode($payload['notification']),
    'AES-256-CBC',
    $key,
    OPENSSL_RAW_DATA,
    base64_decode($payload['iv'])
);

if ($plain === false) {
    ins_log('DECRYPT FAILED (wrong secret key?)');
    echo 'ok';
    exit;
}

$plain = trim($plain, "\x00..\x1F");
$n = json_decode($plain, true);
if (!is_array($n)) {
    ins_log('DECRYPTED BUT NOT JSON');
    echo 'ok';
    exit;
}

$type = strtoupper((string) ($n['transactionType'] ?? ''));
$email = (string) ($n['customer']['billing']['email'] ?? '');
$fullName = trim((string) ($n['customer']['billing']['fullName'] ?? ''));
$firstName = $fullName !== '' ? explode(' ', $fullName)[0] : '';
$receipt = (string) ($n['receipt'] ?? '');

$items = [];
foreach (($n['lineItems'] ?? []) as $li) {
    if (!empty($li['itemNo'])) {
        $items[] = (string) $li['itemNo'];
    }
}

if (!in_array($type, ['SALE', 'TEST_SALE', 'TEST'], true)) {
    ins_log("skipped type=$type receipt=$receipt items=" . implode(',', $items));
    echo 'ok';
    exit;
}

if ($email === '') {
    ins_log("SALE WITHOUT EMAIL receipt=$receipt");
    echo 'ok';
    exit;
}

$apiKey = $config['kit_api_key'];
if ($apiKey === '' || $apiKey === 'PASTE_KIT_V4_API_KEY_HERE') {
    ins_log("KIT KEY NOT CONFIGURED, sale not synced: receipt=$receipt email=$email");
    echo 'ok';
    exit;
}

$results = [];

// 1. Create (or find) the subscriber
[$code, ] = kit_post('https://api.kit.com/v4/subscribers', array_filter([
    'email_address' => $email,
    'first_name' => $firstName,
]), $apiKey);
$results[] = "sub:$code";

// 2. Optional form subscribe
if (!empty($config['kit_form_id'])) {
    [$code, ] = kit_post(
        'https://api.kit.com/v4/forms/' . $config['kit_form_id'] . '/subscribers',
        ['email_address' => $email],
        $apiKey
    );
    $results[] = "form:$code";
}

// 3. Master buyer tag
[$code, ] = kit_post(
    'https://api.kit.com/v4/tags/' . $config['kit_tag_all'] . '/subscribers',
    ['email_address' => $email],
    $apiKey
);
$results[] = "tag-all:$code";

// 4. Per-item tier tags
foreach ($items as $item) {
    if (isset($config['kit_tag_by_item'][$item])) {
        [$code, ] = kit_post(
            'https://api.kit.com/v4/tags/' . $config['kit_tag_by_item'][$item] . '/subscribers',
            ['email_address' => $email],
            $apiKey
        );
        $results[] = "tag-$item:$code";
    } else {
        $results[] = "tag-$item:unmapped";
    }
}

ins_log("synced type=$type receipt=$receipt email=$email items=" . implode(',', $items) . ' ' . implode(' ', $results));
echo 'ok';
