<?php
// Makes the songs. Run by cron every minute:
//   * * * * * php /home/<user>/public_html/prayer-song/api/worker.php >/dev/null 2>&1
// Command line only. Each run takes one free slot and works through the queue
// until it is empty or about ten minutes have passed, so several runs overlap
// safely and no more than 'slots' songs are ever being made at once.
//
//   php worker.php            process the queue
//   php worker.php --list                 every order that is not finished
//   php worker.php --show <token>         one order: answers, lyrics, checks, log
//   php worker.php --retry <token>        make the song again from scratch (new lyrics too with --new-lyrics)
//   php worker.php --remake <token> "say-it-like-this"   a buyer says the name is sung wrong: sing this spelling
//   php worker.php --approve <token> [n]  release attempt n (default the last) although it failed the check

declare(strict_types=1);
// Never over the web. Some cPanel PHP binaries used by cron identify themselves as CGI rather than "cli", so the test is
// "was this reached by a web request", not the name of the binary.
if (PHP_SAPI !== 'cli' && (isset($_SERVER['REMOTE_ADDR']) || isset($_SERVER['HTTP_HOST']) || isset($_SERVER['REQUEST_METHOD']))) {
    http_response_code(403);
    exit;
}
$argv = $argv ?? ($_SERVER['argv'] ?? [__FILE__]);
require_once __DIR__ . '/pipeline.php';
set_time_limit(0);
$cfg = ps_config();

if (in_array('--list', $argv, true)) {
    foreach (glob(ps_data('orders/*.json')) as $f) {
        $o = ps_read($f);
        if ($o && $o['status'] !== 'ready') {
            echo "{$o['status']}\t{$o['token']}\t{$o['receipt']}\tattempts={$o['attempts']}\t" . date('c', $o['created']) . "\n";
        }
    }
    exit;
}

$cmd = $argv[1] ?? '';
if (in_array($cmd, ['--show', '--retry', '--remake', '--approve'], true)) {
    $t = (string) ($argv[2] ?? '');
    $o = ps_order($t);
    if (!$o) { fwrite(STDERR, "no such order\n"); exit(1); }
    if ($cmd === '--show') {
        echo json_encode(array_diff_key($o, ['check' => 1]), JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES), "\n";
        exit;
    }
    if ($cmd === '--approve') {
        [$ok, $msg] = ps_admin_approve($o, (int) ($argv[3] ?? 0));
    } elseif ($cmd === '--remake') {
        [$ok, $msg] = ps_admin_requeue($o, (string) ($argv[3] ?? ''));
    } else {
        [$ok, $msg] = ps_admin_requeue($o, null, in_array('--new-lyrics', $argv, true));
    }
    if (!$ok) { fwrite(STDERR, "$msg\n"); exit(1); }
    echo $msg === 'queued' ? "queued. Run: php worker.php\n" : "$msg\n";
    exit;
}

// "Taking a little longer" email, once, for orders that have waited too long.
foreach (glob(ps_data('queue/*')) as $q) {
    $t = basename($q);
    ps_locked("order-$t", function () use ($t, $cfg) {
        $o = ps_order($t);
        if ($o && !$o['delay_sent'] && in_array($o['status'], ['queued', 'working'], true) && time() - $o['created'] > $cfg['delay_after']) {
            [$sent, $d] = ps_send_order_mail($o, 'delay');
            $o['delay_sent'] = true;
            ps_note($o, "delay email: $d");
            ps_save_order($o);
            ps_alert('Song is slow', "Order $t has waited " . (int) ((time() - $o['created']) / 60) . ' minutes.');
        }
    });
}

// Songs that are made and waiting for their time: show and email the ones that are due.
foreach (glob(ps_data('wait/*')) as $w) {
    $t = basename($w);
    ps_locked("order-$t", function () use ($t, $w) {
        $o = ps_order($t);
        if (!$o || $o['status'] !== 'waiting') {
            @unlink($w);
        } elseif (time() >= ps_send_at($o)) {
            echo "$t " . ps_release($o) . "\n";
        }
    });
}

// Unfinished orders: reminders for people who reached the Pay step and did not pay (see 'abandon' in lib.php).
ps_abandon_pass();

touch(ps_data('idx/worker-ran'));          // lets doctor.php see that cron is calling us

// Take a slot, or leave if all are busy.
$slot = null;
for ($i = 1; $i <= (int) $cfg['slots']; $i++) {
    $h = fopen(ps_data("locks/slot-$i.lock"), 'c');
    if (flock($h, LOCK_EX | LOCK_NB)) {
        $slot = $h;
        break;
    }
    fclose($h);
}
if ($slot === null) {
    exit;
}

$deadline = time() + 600;
while (time() < $deadline) {
    $picked = null;
    $queue = glob(ps_data('queue/*'));
    usort($queue, fn($a, $b) => filemtime($a) <=> filemtime($b));     // oldest first
    foreach ($queue as $q) {
        $t = basename($q);
        $lock = fopen(ps_data("locks/work-$t.lock"), 'c');
        if (flock($lock, LOCK_EX | LOCK_NB)) {
            $picked = [$t, $lock];
            break;
        }
        fclose($lock);
    }
    if ($picked === null) {
        break;
    }
    [$t, $lock] = $picked;
    try {
        $status = ps_process($t);
        echo "$t $status\n";
    } catch (Throwable $e) {
        ps_log("worker error $t: " . $e->getMessage());
        ps_alert('Worker error', "Order $t: " . $e->getMessage());
        @unlink(ps_data("queue/$t"));
    }
    flock($lock, LOCK_UN);
    fclose($lock);
    @unlink(ps_data("locks/work-$t.lock"));
}
