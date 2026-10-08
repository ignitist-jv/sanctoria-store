<?php
// The song page asks this every few seconds while the song is being made.
declare(strict_types=1);
require_once __DIR__ . '/lib.php';

// ?health=1 : is the song maker being run by cron? Says only how long ago it last ran. No order or buyer data.
if (isset($_GET['health'])) {
    $ran = @filemtime(ps_data('idx/worker-ran'));
    header('Cache-Control: no-store');
    ps_json_out(['worker_ran_seconds_ago' => $ran ? time() - $ran : null]);
}
$o = ps_order((string) ($_GET['k'] ?? ''));
if (!$o) {
    ps_json_out(['status' => 'notfound'], 404);
}
$public = in_array($o['status'], ['queued', 'working', 'waiting'], true) ? 'making' : $o['status'];
ps_json_out(['status' => $public, 'has_lyrics' => ps_lyrics_visible($o)]);
