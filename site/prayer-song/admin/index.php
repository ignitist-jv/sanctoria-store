<?php
// The owner's page: see every order, listen to a song that was held, release it, remake it with the
// name spelled as it sounds, make it again, or send the email again. One password, set as a hash in
// api/config.php ('admin_hash'). With no hash set, this page does not exist (404).
//
// Nothing slow happens here: a remake only puts the order back in the queue, and the worker (cron)
// makes the song within a minute or two.
declare(strict_types=1);
require_once __DIR__ . '/../api/pipeline.php';

header('X-Robots-Tag: noindex, nofollow');
header('Cache-Control: no-store');
header('Referrer-Policy: no-referrer');
header('X-Frame-Options: DENY');

$cfg = ps_config();
$hash = (string) ($cfg['admin_hash'] ?? '');
if ($hash === '') {
    http_response_code(404);
    exit;
}
$e = fn($s) => htmlspecialchars((string) $s, ENT_QUOTES, 'UTF-8');
$self = strtok((string) $_SERVER['REQUEST_URI'], '?');
$https = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off') || (($_SERVER['HTTP_X_FORWARDED_PROTO'] ?? '') === 'https');

session_name('psadm');
session_set_cookie_params(['lifetime' => 0, 'path' => rtrim(dirname((string) $_SERVER['SCRIPT_NAME']), '/') . '/', 'httponly' => true, 'secure' => $https, 'samesite' => 'Strict']);
session_start();
if (!empty($_SESSION['ok']) && time() - (int) $_SESSION['seen'] > 7200) {          // two hours idle
    $_SESSION = [];
}
$in = !empty($_SESSION['ok']);
if ($in) {
    $_SESSION['seen'] = time();
}

// ------------------------------------------------------------------ signing in
$ip = (string) ($_SERVER['HTTP_CF_CONNECTING_IP'] ?? $_SERVER['REMOTE_ADDR'] ?? '?');
$failFile = ps_data('idx/admin-fails.json');
$fails = function () use ($failFile): array {
    $all = array_filter(ps_read($failFile) ?? [], fn($f) => time() - (int) $f[0] < 900);      // the last fifteen minutes
    return array_values($all);
};
$locked = function () use ($fails, $ip): bool {
    $all = $fails();
    return count($all) >= 30 || count(array_filter($all, fn($f) => $f[1] === $ip)) >= 5;
};
$error = '';
if (!$in && $_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['password'])) {
    if ($locked()) {
        $error = 'Too many wrong tries. Wait fifteen minutes.';
    } elseif (password_verify((string) $_POST['password'], $hash)) {
        session_regenerate_id(true);
        $_SESSION = ['ok' => true, 'seen' => time(), 'csrf' => bin2hex(random_bytes(16))];
        header("Location: $self");
        exit;
    } else {
        ps_locked('admin-fails', function () use ($fails, $failFile, $ip) {
            $all = $fails();
            $all[] = [time(), $ip];
            ps_write($failFile, $all);
        });
        ps_log("admin: wrong password from $ip");
        usleep(600000);
        $error = 'That password is not right.';
    }
}

$css = <<<'CSS'
:root{--cream:#F7F3EC;--paper:#FFFDF9;--ink:#2A1F1A;--soft:#5B4A40;--muted:#93846F;--bronze:#9A7B4F;--deep:#7A5F39;--gold:#F2C230;--edge:#D9A415;--hair:#E6DCCA;--red:#A23B2A;--green:#2E7D4F}
*{box-sizing:border-box}
body{margin:0;background:var(--cream);color:var(--ink);font:16px/1.5 Inter,system-ui,-apple-system,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--deep)}
.wrap{max-width:760px;margin:0 auto;padding:0 16px 60px}
header{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:16px 0 12px;border-bottom:1px solid var(--hair);margin-bottom:16px}
header b{font-family:Fraunces,Georgia,serif;font-size:20px}
header form{margin:0}
h1{font-family:Fraunces,Georgia,serif;font-size:24px;line-height:1.2;margin:14px 0 4px}
h2{font-family:Fraunces,Georgia,serif;font-size:18px;margin:26px 0 8px}
.sub{color:var(--soft);margin:0 0 14px}
.card{background:var(--paper);border:1px solid var(--hair);border-radius:14px;padding:16px;margin:0 0 14px}
.btn{display:inline-block;border:1px solid var(--edge);background:var(--gold);color:var(--ink);font:600 16px/1 Inter,system-ui,sans-serif;border-radius:12px;padding:14px 18px;cursor:pointer;text-decoration:none}
.btn.q{background:var(--paper);border-color:#D2C3A6}
.btn.sm{padding:9px 12px;font-size:14px;border-radius:10px}
input[type=text],input[type=password],input[type=search]{width:100%;font:16px Inter,system-ui,sans-serif;padding:13px;border:1px solid #D2C3A6;border-radius:10px;background:#fff;color:var(--ink)}
label{display:block;font-weight:600;font-size:14px;margin:0 0 6px}
.tabs{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 12px}
.tabs a{border:1px solid #D2C3A6;border-radius:999px;padding:8px 14px;text-decoration:none;color:var(--ink);font-weight:600;font-size:14px;background:var(--paper)}
.tabs a.on{background:var(--deep);border-color:var(--deep);color:#fff}
.row{display:block;text-decoration:none;color:inherit;background:var(--paper);border:1px solid var(--hair);border-radius:12px;padding:12px 14px;margin:0 0 8px}
.row:hover{border-color:var(--bronze)}
.row b{font-size:16px}
.row small{display:block;color:var(--soft);font-size:13.5px;margin-top:2px;overflow-wrap:anywhere}
.pill{display:inline-block;font-size:12px;font-weight:700;letter-spacing:.03em;border-radius:999px;padding:3px 9px;margin-left:6px;vertical-align:2px;background:#EDE5D6;color:var(--soft)}
.pill.bad{background:#F6DDD7;color:var(--red)}
.pill.ok{background:#DCEFE3;color:var(--green)}
.pill.wait{background:#FBEFC4;color:#7A5B00}
.note{border-radius:12px;padding:12px 14px;margin:0 0 14px;font-weight:600}
.note.ok{background:#DCEFE3;color:#1F5C39}
.note.bad{background:#F6DDD7;color:var(--red)}
.note.warn{background:#FBEFC4;color:#6B5000}
dl{display:grid;grid-template-columns:118px 1fr;gap:6px 12px;margin:0}
dt{color:var(--muted);font-size:14px}
dd{margin:0;overflow-wrap:anywhere}
audio{width:100%;margin:6px 0 2px}
.lyr{white-space:pre-line;color:var(--soft);font-size:15px;line-height:1.6}
.lyr b{display:block;color:var(--bronze);font-size:12px;letter-spacing:.08em;text-transform:uppercase;margin:12px 0 2px}
.log{font:12.5px/1.5 ui-monospace,Menlo,monospace;color:var(--soft);white-space:pre-wrap;overflow-wrap:anywhere;margin:0}
.act{border-top:1px solid var(--hair);padding:14px 0 2px;margin-top:14px}
.act:first-child{border-top:0;padding-top:0;margin-top:0}
.act p{margin:0 0 10px;color:var(--soft);font-size:14.5px}
.act form{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:0}
.act input[type=text]{flex:1;min-width:170px}
.chk{font-weight:500;font-size:14.5px;display:flex;gap:8px;align-items:center;margin:0}
.muted{color:var(--muted);font-size:13.5px}
.starsline{color:#D9A415;letter-spacing:1px}
.starsline i{color:#DDD2BD;font-style:normal}
CSS;
$page = function (string $title, string $body) use ($css, $e): void {
    echo '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        . '<meta name="robots" content="noindex,nofollow"><title>' . $e($title) . '</title>'
        . '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        . '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
        . "<style>$css</style></head><body><div class=\"wrap\">$body</div></body></html>";
    exit;
};

if (!$in) {
    $page('Sign in', '<header><b>Your Prayer Song</b><span class="muted">Owner</span></header>'
        . '<div class="card" style="max-width:420px;margin:40px auto"><h1 style="margin-top:0">Sign in</h1>'
        . ($error !== '' ? '<div class="note bad">' . $e($error) . '</div>' : '')
        . '<form method="post" autocomplete="off"><label for="pw">Password</label>'
        . '<input id="pw" name="password" type="password" autocomplete="current-password" autofocus required>'
        . '<p style="margin:14px 0 0"><button class="btn" type="submit">Sign in</button></p></form></div>');
}

$csrf = (string) $_SESSION['csrf'];
$tz = new DateTimeZone('Asia/Singapore');
$when = fn(?int $ts) => $ts ? (new DateTime("@$ts"))->setTimezone($tz)->format('j M, g:ia') : '';
$ago = function (int $ts): string {
    $d = max(0, time() - $ts);
    return $d < 90 ? "{$d}s" : ($d < 5400 ? round($d / 60) . ' min' : ($d < 172800 ? round($d / 3600) . ' hr' : round($d / 86400) . ' days'));
};
$attempts = function (string $t): array {
    $out = [];
    foreach (glob(ps_data("songs/$t.attempt*.mp3")) ?: [] as $f) {
        if (preg_match('/attempt(\d+)\.mp3$/', $f, $m)) {
            $out[(int) $m[1]] = $f;
        }
    }
    ksort($out);
    return $out;
};
/** Does this order need a person? Returns the reason, or ''. */
$needs = function (array $o) use ($cfg): string {
    if ($o['status'] === 'review') {
        return 'Held: ' . ($o['hold_reason'] ?? 'needs a listen');
    }
    if ($o['status'] === 'ready' && empty($o['emailed'])) {
        return 'Ready, but the email did not go out';
    }
    if (in_array($o['status'], ['queued', 'working'], true) && time() - (int) ($o['updated'] ?? $o['created']) > (int) $cfg['delay_after']) {
        return 'Waiting too long to be made';
    }
    return '';
};

// ------------------------------------------------------------------ actions (POST)
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!hash_equals($csrf, (string) ($_POST['csrf'] ?? ''))) {
        http_response_code(400);
        $page('Expired', '<div class="note bad">That page had expired. <a href="' . $e($self) . '">Go back</a> and try again.</div>');
    }
    $act = (string) ($_POST['act'] ?? '');
    if ($act === 'logout') {
        $_SESSION = [];
        session_destroy();
        header("Location: $self");
        exit;
    }
    $t = (string) ($_POST['o'] ?? '');
    $o = ps_order($t);
    $res = [false, 'no such order'];
    if ($o) {
        $res = ps_locked("order-$t", function () use ($act, $t) {
            $o = ps_order($t);
            switch ($act) {
                case 'approve': return ps_admin_approve($o, (int) ($_POST['n'] ?? 0));
                case 'remake':  return ps_admin_requeue($o, (string) ($_POST['say'] ?? ''), false, isset($_POST['say2']) ? (string) $_POST['say2'] : null);
                case 'retry':   return ps_admin_requeue($o, null, !empty($_POST['new_lyrics']));
                case 'resend':  return ps_admin_resend($o);
                case 'sendnow': return ps_admin_send_now($o);
                case 'publish':   return ps_admin_review_public($o, true);
                case 'unpublish': return ps_admin_review_public($o, false);
            }
            return [false, 'unknown action'];
        });
        ps_log("admin: $act $t => " . ($res[0] ? 'ok' : 'failed') . " {$res[1]}");
    }
    $_SESSION['flash'] = $res;
    header('Location: ' . $self . ($o ? '?o=' . rawurlencode($t) : ''));
    exit;
}

$flash = $_SESSION['flash'] ?? null;
unset($_SESSION['flash']);
$flashHtml = '';
if ($flash) {
    $msg = $flash[1] === 'queued' ? 'Back in the queue. The new song is usually ready within two minutes; refresh this page to see it.' : ucfirst((string) $flash[1]);
    $flashHtml = '<div class="note ' . ($flash[0] ? 'ok' : 'bad') . '">' . $e($msg) . '</div>';
}
$head = '<header><a href="' . $e($self) . '" style="text-decoration:none;color:inherit"><b>Your Prayer Song</b></a>'
    . '<form method="post"><input type="hidden" name="csrf" value="' . $e($csrf) . '"><input type="hidden" name="act" value="logout">'
    . '<button class="btn q sm" type="submit">Sign out</button></form></header>';

// ------------------------------------------------------------------ one order
$t = (string) ($_GET['o'] ?? '');
if ($t !== '') {
    $o = ps_order($t);
    if (!$o) {
        http_response_code(404);
        $page('Not found', $head . '<div class="note bad">No order with that code.</div>');
    }
    $tries = $attempts($t);
    $final = ps_data("songs/$t.mp3");
    if (isset($_GET['audio'])) {                                   // listen, signed in only
        $n = (string) $_GET['audio'];
        $file = $n === 'final' ? $final : ($tries[(int) $n] ?? '');
        if ($file === '' || !is_file($file)) {
            http_response_code(404);
            exit;
        }
        session_write_close();
        ps_stream_mp3($file);
    }
    $a = $o['answers'] ?? [];
    $phr = ps_copy()['phrases'] ?? [];
    $say = fn($k) => $e($phr[$k] ?? $k);
    $why = $needs($o);
    $hidden = '<input type="hidden" name="csrf" value="' . $e($csrf) . '"><input type="hidden" name="o" value="' . $e($t) . '">';
    $b = $head . $flashHtml . '<p style="margin:0"><a href="' . $e($self) . '">&larr; All orders</a></p>';
    $b .= '<h1>' . $e($o['title'] ?? ('Song for ' . (ps_names_text($a) ?: 'someone'))) . '</h1><p class="sub">'
        . ($a ? 'For ' . $e($a['name'] ?? '') . ', ' . $say($a['who'] ?? '') . (!empty($a['name2']) ? ', and ' . $e($a['name2']) . (!empty($a['who2']) ? ', ' . $say($a['who2']) : '') : '') . '. A prayer for ' . $say($a['intention'] ?? '') . '.' : 'Paid, but the form was never filled in.') . '</p>';
    if ($why !== '') {
        $b .= '<div class="note warn">' . $e($why) . '</div>';
    }
    if (!empty($o['refunded'])) {
        $b .= '<div class="note bad">This order was refunded.</div>';
    }

    // listen
    $b .= '<div class="card"><h2 style="margin-top:0">Listen</h2>';
    if (is_file($final)) {
        $b .= '<div class="muted">The song the buyer has</div><audio controls preload="none" src="?o=' . $e($t) . '&amp;audio=final"></audio>';
    }
    foreach ($tries as $n => $f) {
        $b .= '<div class="muted" style="margin-top:8px">Attempt ' . $n . ' (failed the automatic check)</div><audio controls preload="none" src="?o=' . $e($t) . '&amp;audio=' . $n . '"></audio>';
    }
    if (!is_file($final) && !$tries) {
        $b .= '<p class="muted" style="margin:0">No recording yet.</p>';
    }
    $c = $o['check'] ?? null;
    if ($c) {
        $b .= '<p class="muted" style="margin:10px 0 0">Last check: name heard ' . $e($c['name_heard'] ?? '?') . ' of ' . $e($c['name_expected'] ?? '?')
            . ' times, ' . $e(round(100 * (float) ($c['recall'] ?? 0))) . '% of the words sung'
            . (!empty($c['heard_as']) ? ', name heard as: ' . $e(implode(', ', (array) $c['heard_as'])) : '') . '.</p>';
    }
    $b .= '</div>';

    // what can be done
    $b .= '<div class="card">';
    if ($o['status'] === 'review' && $tries) {
        $last = array_key_last($tries);
        $b .= '<div class="act"><p><b>It sounds fine.</b> Send the buyer this recording.</p><form method="post">' . $hidden . '<input type="hidden" name="act" value="approve">';
        foreach (array_keys($tries) as $n) {
            $b .= '<button class="btn' . ($n === $last ? '' : ' q') . '" type="submit" name="n" value="' . $n . '">Send attempt ' . $n . '</button>';
        }
        $b .= '</form></div>';
    }
    if ($a) {
        $b .= '<div class="act"><p><b>The name is sung wrong.</b> Type it the way it sounds, for example hwah-KEEN. The song is made again and the buyer is emailed when it is ready.</p>'
            . '<form method="post">' . $hidden . '<input type="hidden" name="act" value="remake">'
            . '<input type="text" name="say" maxlength="60" placeholder="How ' . $e($a['name'] ?? 'the name') . ' should sound" value="' . $e(($a['name_phonetic'] ?? '') !== '' ? $a['name_phonetic'] : (!empty($a['name2']) ? ($a['name'] ?? '') : '')) . '" required>'
            . (!empty($a['name2']) ? '<input type="text" name="say2" maxlength="60" placeholder="How ' . $e($a['name2']) . ' should sound (leave as it is if fine)" value="' . $e($a['name2_phonetic'] ?? '') . '">' : '')
            . '<button class="btn q" type="submit">Remake</button></form></div>';
        $b .= '<div class="act"><p><b>Make it again</b> with the same name. The buyer is emailed when it is ready.</p>'
            . '<form method="post">' . $hidden . '<input type="hidden" name="act" value="retry">'
            . '<label class="chk"><input type="checkbox" name="new_lyrics" value="1"> Write new lyrics too</label>'
            . '<button class="btn q" type="submit">Make again</button></form></div>';
    }
    if ($o['status'] === 'waiting') {
        $b .= '<div class="act"><p><b>The song is made.</b> It is shown and emailed at ' . $e(date('j M, g:i a', ps_send_at($o))) . (ps_is_express($o) ? ' (express)' : '')
            . '. Send it now instead?</p><form method="post">' . $hidden
            . '<input type="hidden" name="act" value="sendnow"><button class="btn q" type="submit">Send now</button></form></div>';
    }
    if ($o['status'] === 'ready') {
        $b .= '<div class="act"><p><b>Send the email again</b> to ' . $e($o['email']) . '.</p><form method="post">' . $hidden
            . '<input type="hidden" name="act" value="resend"><button class="btn q" type="submit">Send again</button></form></div>';
    }
    $b .= '</div>';

    if (!empty($o['review'])) {
        $r = $o['review'];
        $b .= '<div class="card"><h2 style="margin-top:0">Her review</h2><p style="margin:0 0 6px"><span class="starsline">' . str_repeat('&#9733;', (int) $r['stars']) . '<i>' . str_repeat('&#9733;', 5 - (int) $r['stars']) . '</i></span>'
            . ' <span class="pill ' . (!empty($r['share']) ? 'ok">may be shared' : '">private') . '</span></p>'
            . ($r['text'] !== '' ? '<p class="lyr" style="margin:0 0 6px">' . $e($r['text']) . '</p>' : '<p class="muted" style="margin:0 0 6px">Stars only, no words.</p>')
            . '<p class="muted" style="margin:0 0 12px">' . $e($r['name'] !== '' ? $r['name'] : 'No name given') . ' &middot; ' . $e($when((int) $r['updated'])) . ' SGT</p>';
        $hid = '<input type="hidden" name="csrf" value="' . $e($csrf) . '"><input type="hidden" name="o" value="' . $e($t) . '">';
        if (!empty($r['approved'])) {
            $b .= '<form method="post" style="margin:0"><span class="pill ok" style="margin:0 10px 0 0">on the reviews page</span>' . $hid
                . '<input type="hidden" name="act" value="unpublish"><button class="btn q sm" type="submit">Take it down</button></form>';
        } elseif (!empty($r['share']) && trim((string) $r['text']) !== '') {
            $b .= '<form method="post" style="margin:0">' . $hid . '<input type="hidden" name="act" value="publish">'
                . '<button class="btn sm" type="submit">Show on the reviews page</button></form>'
                . '<p class="muted" style="margin:8px 0 0">Shows her words, this name and the month. Not her stars, her email or the song.</p>';
        } else {
            $b .= '<p class="muted" style="margin:0">' . (empty($r['share']) ? 'She did not give permission, so this cannot be shown publicly.' : 'Stars only, so there is nothing to show publicly.') . '</p>';
        }
        $b .= '</div>';
    }

    // details
    $url = ps_song_url($t);
    $b .= '<div class="card"><dl>'
        . '<dt>Status</dt><dd>' . $e($o['status']) . ', ' . (int) $o['attempts'] . ' attempt(s)</dd>'
        . '<dt>Buyer</dt><dd>' . $e(trim(($o['buyer'] ?? '') . ' ' . $o['email'])) . '</dd>'
        . '<dt>Receipt</dt><dd>' . $e($o['receipt']) . '</dd>'
        . '<dt>Paid</dt><dd>' . $e($when((int) $o['created'])) . ' SGT</dd>'
        . (!empty($o['ready_at']) ? '<dt>Ready</dt><dd>' . $e($when((int) $o['ready_at'])) . ' SGT</dd>' : '')
        . '<dt>Email sent</dt><dd>' . (!empty($o['emailed']) ? 'yes' : 'no') . '</dd>'
        . ($a ? '<dt>Sound</dt><dd>' . $say($a['style'] ?? '') . ', ' . $say($a['voice'] ?? '') . ' voice</dd>'
              . (!empty($a['name_phonetic']) || !empty($a['name2_phonetic']) ? '<dt>Said as</dt><dd>' . $e(trim(($a['name_phonetic'] ?? '') . ' ' . ($a['name2_phonetic'] ?? ''))) . '</dd>' : '')
              . (!empty($a['note']) ? '<dt>Her note</dt><dd>' . $e($a['note']) . '</dd>' : '') : '')
        . '<dt>Buyer\'s page</dt><dd><a href="' . $e($url) . '" target="_blank" rel="noopener">' . $e($url) . '</a></dd>'
        . '</dl></div>';

    if (!empty($o['lyrics']['sections'])) {
        $b .= '<div class="card"><h2 style="margin-top:0">Lyrics</h2><div class="lyr">';
        foreach ($o['lyrics']['sections'] as $sec) {
            $b .= '<b>' . $e($sec['tag'] ?? '') . '</b>' . $e(implode("\n", $sec['lines'] ?? []));
        }
        $b .= '</div></div>';
    }
    $b .= '<div class="card"><h2 style="margin-top:0">History</h2><pre class="log">' . $e(implode("\n", array_map(fn($l) => mb_substr((string) $l, 0, 400), $o['log'] ?? []))) . '</pre></div>';
    $page(($o['title'] ?? 'Order') . ' | Owner', $b);
}

// ------------------------------------------------------------------ every order
$orders = [];
foreach (glob(ps_data('orders/*.json')) ?: [] as $f) {
    $o = ps_read($f);
    if ($o && !empty($o['token'])) {
        $o['_why'] = $needs($o);
        $orders[] = $o;
    }
}
usort($orders, fn($x, $y) => (int) $y['created'] <=> (int) $x['created']);
$groups = [
    'attention' => array_filter($orders, fn($o) => $o['_why'] !== ''),
    'making'    => array_filter($orders, fn($o) => $o['_why'] === '' && in_array($o['status'], ['queued', 'working', 'waiting', 'needs_answers'], true)),
    'done'      => array_filter($orders, fn($o) => $o['_why'] === '' && $o['status'] === 'ready'),
    'reviews'   => array_filter($orders, fn($o) => !empty($o['review'])),
    'all'       => $orders,
];
$labels = ['attention' => 'Needs you', 'making' => 'Being made', 'done' => 'Delivered', 'reviews' => 'Reviews', 'all' => 'All'];
$view = (string) ($_GET['view'] ?? ($groups['attention'] ? 'attention' : 'all'));
$view = isset($groups[$view]) ? $view : 'all';
$q = trim((string) ($_GET['q'] ?? ''));
$rows = $groups[$view];
if ($q !== '') {
    $needle = mb_strtolower($q);
    $rows = array_filter($orders, fn($o) => str_contains(mb_strtolower(implode(' ', [$o['email'], $o['receipt'], $o['buyer'] ?? '', ps_names_text($o['answers'] ?? []), $o['title'] ?? '', $o['token']])), $needle));
}

$b = $head . $flashHtml;
$ran = @filemtime(ps_data('idx/worker-ran'));
if (!empty($cfg['mock'])) {
    $b .= '<div class="note warn">Practice mode is on: songs are placeholders, not real recordings.</div>';
}
if (!$ran || time() - $ran > 300) {
    $b .= '<div class="note bad">The song maker has not run ' . ($ran ? 'for ' . $e($ago($ran)) : 'yet') . '. Check the cron job in cPanel.</div>';
} else {
    $b .= '<p class="muted" style="margin:0 0 12px">Song maker last ran ' . $e($ago($ran)) . ' ago.</p>';
}
$b .= '<form method="get" style="margin:0 0 12px"><input type="search" name="q" value="' . $e($q) . '" placeholder="Search by email, receipt or name"></form><div class="tabs">';
foreach ($labels as $k => $label) {
    $b .= '<a class="' . ($q === '' && $k === $view ? 'on' : '') . '" href="?view=' . $k . '">' . $e($label) . ' ' . count($groups[$k]) . '</a>';
}
$b .= '</div>';
if (!$rows) {
    $b .= '<div class="card muted">' . ($view === 'attention' && $q === '' ? 'Nothing needs you right now.' : 'Nothing here.') . '</div>';
}
foreach (array_slice($rows, 0, 300) as $o) {
    $a = $o['answers'] ?? [];
    $pill = $o['_why'] !== '' ? '<span class="pill bad">' . ($o['status'] === 'review' ? 'held' : 'check') . '</span>'
        : ($o['status'] === 'ready' ? '<span class="pill ok">delivered</span>' : '<span class="pill wait">' . $e(str_replace('_', ' ', $o['status'])) . '</span>');
    $b .= '<a class="row" href="?o=' . $e($o['token']) . '"><b>' . $e($o['title'] ?? ('For ' . (ps_names_text($a) ?: 'someone, form not filled in'))) . '</b>' . $pill
        . (!empty($o['refunded']) ? '<span class="pill bad">refunded</span>' : '')
        . '<small>' . $e(trim(($o['buyer'] ?? '') . ' ' . $o['email'])) . ' &middot; ' . $e($when((int) $o['created'])) . '</small>'
        . ($o['_why'] !== '' ? '<small style="color:var(--red)">' . $e($o['_why']) . '</small>' : '')
        . (!empty($o['review']) ? '<small><span class="starsline">' . str_repeat('&#9733;', (int) $o['review']['stars']) . '<i>' . str_repeat('&#9733;', 5 - (int) $o['review']['stars']) . '</i></span> '
            . $e(mb_substr((string) $o['review']['text'], 0, $view === 'reviews' ? 600 : 90)) . (!empty($o['review']['share']) ? ' <span class="pill ok">may be shared</span>' : ' <span class="pill">private</span>') . '</small>' : '')
        . '</a>';
}
$page('Orders | Owner', $b);
