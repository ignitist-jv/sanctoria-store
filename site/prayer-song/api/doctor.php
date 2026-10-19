<?php
// Checks that everything this offer depends on is in place on this server.
// Command line only:  php doctor.php          (add --live to also make one tiny call to each service)
// Prints one line per check and exits 1 if anything a real order needs is missing.

declare(strict_types=1);
if (PHP_SAPI !== 'cli') { http_response_code(403); exit; }
require_once __DIR__ . '/pipeline.php';

$cfg = ps_config();
$live = in_array('--live', $argv, true);
$bad = 0;
function line(string $state, string $what, string $detail = ''): void { echo str_pad($state, 6), $what, $detail !== '' ? "  ($detail)" : '', "\n"; }
function need(bool $ok, string $what, string $detail = ''): void { global $bad; if (!$ok) { $bad++; } line($ok ? 'ok' : 'FAIL', $what, $detail); }
function note(bool $ok, string $what, string $detail = ''): void { line($ok ? 'ok' : 'todo', $what, $detail); }

need(version_compare(PHP_VERSION, '8.0', '>='), 'PHP 8.0 or newer', PHP_VERSION);
foreach (['curl', 'openssl', 'json', 'mbstring'] as $ext) { need(extension_loaded($ext), "PHP extension: $ext"); }
$data = ps_data();
need(is_writable($data), 'data folder is writable', $data);
$root = realpath((string) ($_SERVER['DOCUMENT_ROOT'] ?? dirname(__DIR__, 2))) ?: '';
$outside = $root === '' || !str_starts_with((string) realpath($data), $root);
note($outside, 'data folder is outside the web root', $outside ? '' : 'inside the web root: its .htaccess must return 403, check with tools/check_live.py');
need(is_file(__DIR__ . '/copy.json'), 'copy.json is built');
need(is_file(__DIR__ . '/config.php'), 'config.php exists');
need(!$cfg['mock'], 'practice mode is OFF', $cfg['mock'] ? 'mock is true: no real songs will be made' : '');
need($cfg['cb_secret_key'] !== '', 'ClickBank secret key');
need($cfg['elevenlabs_key'] !== '', 'ElevenLabs key (music)');
need($cfg['anthropic_key'] !== '', 'Claude key (lyrics)');
need(str_starts_with($cfg['base_url'], 'https://'), 'base_url is https', $cfg['base_url']);
$m = $cfg['mail']['driver'];
if ($m === 'kit') {
    need(!empty($cfg['kit']['api_key']), 'Kit API key');
    need(!empty($cfg['kit']['seq_ready']), 'Kit "song is ready" sequence id');
    note(!empty($cfg['kit']['seq_delay']), 'Kit "taking a little longer" sequence id');
} else {
    need($m !== 'log', 'a real email sender is chosen', "mail driver is \"$m\"");
}
note($cfg['admin_email'] !== '', 'admin_email for alerts');
note(count($cfg['items']) > 0, 'ClickBank items mapped', implode(', ', array_keys($cfg['items'])));
$last = @filemtime(ps_data('idx/worker-ran'));
note($last && time() - $last < 180, 'the worker has run in the last 3 minutes (cron)', $last ? date('c', $last) : 'never');
echo 'queue: ', count(glob(ps_data('queue/*'))), ' waiting, ', count(glob(ps_data('orders/*.json'))), " orders in all\n";

if ($live) {
    [$c, $b] = ps_http('GET', 'https://api.elevenlabs.io/v1/user/subscription', ['xi-api-key: ' . $cfg['elevenlabs_key']], null, 20);
    $j = json_decode($b, true);
    need($c === 200, 'ElevenLabs answers', $c === 200 ? ($j['tier'] ?? '?') . ', ' . (($j['character_limit'] ?? 0) - ($j['character_count'] ?? 0)) . ' credits left' : "HTTP $c");
    [$c, $b] = ps_http('GET', 'https://api.anthropic.com/v1/models/' . $cfg['lyric_model'], ['x-api-key: ' . $cfg['anthropic_key'], 'anthropic-version: 2023-06-01'], null, 20);
    need($c === 200, 'Claude answers and has the lyric model', "HTTP $c");
    if ($m === 'kit') {
        [$c] = ps_http('GET', 'https://api.kit.com/v4/sequences/' . $cfg['kit']['seq_ready'] . '/subscribers?per_page=1', ['Accept: application/json', 'X-Kit-Api-Key: ' . $cfg['kit']['api_key']], null, 20);
        need($c === 200, 'Kit answers and has the "ready" sequence', "HTTP $c");
    }
}
echo $bad ? "\n$bad thing(s) must be fixed before a real order.\n" : "\nReady for a real order.\n";
exit($bad ? 1 : 0);
