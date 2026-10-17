<?php
/**
 * Sanctoria Prayer Song: the steps that turn one order into one song.
 *
 *   ps_write_lyrics()  answers            -> title + sections
 *   ps_build_plan()    lyrics + style     -> ElevenLabs composition plan
 *   ps_render()        plan               -> MP3 bytes
 *   ps_verify()        MP3 + lyrics       -> was the name sung, did the words survive
 *   ps_send_mail()     the delivery email, through whichever provider is configured
 */

declare(strict_types=1);

require_once __DIR__ . '/lib.php';
require_once __DIR__ . '/lyrics.php';

// ---------------------------------------------------------------- lyrics

/**
 * PLACEHOLDER lyric writer, used ONLY in practice mode ('mock'). One plain lyric
 * with the name set in, so the plumbing can be tested without spending anything.
 * Real orders are written by ps_claude_lyrics() in lyrics.php, and a real order
 * is never given this placeholder: without a Claude key it is held for review.
 */
function ps_write_lyrics(array $o): array
{
    $a = $o['answers'];
    $n = ps_names_text($a);
    $phr = ps_copy()['phrases'] ?? [];
    $for = $phr[$a['intention']] ?? $a['intention'];
    $chorus = ["Lord, hear this prayer for $n", "Hold $n close in Your care", "By name we bring $n before You", "$n, known and loved, held in prayer"];
    return [
        'title' => "A Prayer for $n",
        'placeholder' => true,
        'sections' => [
            ['tag' => 'Verse 1', 'lines' => ["Before the morning light has come", "We lift one name to You", "A prayer for $for, quietly said", "As faithful hearts will do"]],
            ['tag' => 'Chorus', 'lines' => $chorus],
            ['tag' => 'Verse 2', 'lines' => ["Through every hour of every day", "Be near and be their guide", "In all the roads that lie ahead", "Stay, Lord, at their side"]],
            ['tag' => 'Chorus', 'lines' => $chorus],
            ['tag' => 'Outro', 'lines' => ["Amen, amen", "For $n, amen"]],
        ],
    ];
}

function ps_lyrics_text(array $lyrics): string
{
    $out = [];
    foreach ($lyrics['sections'] as $s) {
        $out[] = implode("\n", $s['lines']);
    }
    return implode("\n\n", $out);
}

// ---------------------------------------------------------------- composition plan

const PS_STYLE_PRESETS = [
    'hymn'     => ['traditional Catholic hymn', 'pipe organ', 'soft church choir', 'reverent', '66 BPM'],
    'acoustic' => ['gentle acoustic worship ballad', 'fingerpicked acoustic guitar', 'light strings', 'intimate', '72 BPM'],
    'gospel'   => ['soulful gospel ballad', 'piano led', 'soft hammond organ', 'gentle choir on the chorus', '70 BPM'],
    'country'  => ['heartfelt country gospel ballad', 'acoustic guitar', 'pedal steel guitar', 'soft piano', '74 BPM'],
    'lullaby'  => ['gentle Christian lullaby', 'music box accents', 'soft strings', 'fingerpicked guitar', '64 BPM'],
    // Added 2026-10-05 from the style clips TS approved (prayer-song/tools/style_samples.py).
    'piano'    => ['tender Christian piano ballad', 'solo grand piano', 'soft string pad', 'intimate', '68 BPM'],
    'folk'     => ['1970s folk Mass hymn', 'two strummed acoustic guitars', 'small group of voices singing together in unison on the chorus', 'warm and simple', 'flute', '76 BPM'],
    'choir'    => ['sacred choral anthem', 'cathedral choir of mixed voices singing the lyrics clearly in English', 'pipe organ', 'cathedral reverb', 'solemn and beautiful', '60 BPM'],
];
const PS_VOICE_PRESETS = [
    'female' => 'warm female lead vocalist, clear diction, every word easy to understand',
    'male'   => 'warm male baritone lead vocalist, clear diction, every word easy to understand',
];

/** Length in ms and arrangement note for each part of the locked structure (PRODUCT-BIBLE, "Song structure"). */
const PS_PARTS = [
    'verse 1'      => [26000, 'intimate vocal, sparse arrangement'],
    'chorus'       => [28000, 'fuller arrangement, emotional lift'],
    'verse 2'      => [26000, 'warm vocal, light accompaniment'],
    'bridge'       => [24000, 'stripped back, prayerful, voice and one instrument'],
    'verse 3'      => [26000, 'building gently'],
    'final chorus' => [40000, 'full arrangement, peak emotion, lead and harmony together'],
    'outro'        => [14000, 'soft and slow, gentle ending, fade'],
];

/**
 * $sung maps each name to the spelling handed to the singer: the name itself, or its
 * phonetic spelling on a retry. An instrumental intro opens the song and an instrumental
 * interlude is placed before the bridge, which brings it to about four minutes.
 */
function ps_build_plan(array $lyrics, array $answers, array $sung): array
{
    $style = PS_STYLE_PRESETS[$answers['style']] ?? PS_STYLE_PRESETS['hymn'];
    $voiceKey = $answers['voice'] === 'male' ? 'male' : 'female';       // "either" sings as a woman
    $voice = PS_VOICE_PRESETS[$voiceKey];
    $global = array_merge($style, [$voice, 'prayerful and unhurried', 'polished radio quality production']);
    $neg = ['rap', 'electronic dance', 'aggressive', 'distorted', 'mumbled vocals', 'heavy drums', 'upbeat party'];
    $chunk = fn(string $text, int $ms, array $styles) => [
        'text' => $text, 'duration_ms' => $ms, 'positive_styles' => $styles, 'negative_styles' => $neg, 'context_adherence' => 'high',
    ];

    $chunks = [$chunk('[Intro]', 10000, array_merge($global, ['instrumental opening']))];
    foreach ($lyrics['sections'] as $s) {
        $key = strtolower($s['tag']);
        [$ms, $note] = PS_PARTS[$key] ?? [max(8000, min(60000, count($s['lines']) * 6000 + 2000)), 'gentle and intimate'];
        if ($key === 'bridge') {
            $chunks[] = $chunk("[Interlude]\n{instrumental break}", 12000, ['instrumental, no vocals', 'reflective']);
        }
        $lines = array_map(fn($l) => strtr($l, $sung), $s['lines']);
        $chunks[] = $chunk('[' . $s['tag'] . "]\n" . implode("\n", $lines), $ms, [$voice, $note]);
    }
    return ['chunks' => $chunks];
}

// ---------------------------------------------------------------- render

/** Returns [mp3 bytes, error]. */
function ps_render(array $plan): array
{
    $cfg = ps_config();
    if ($cfg['mock']) {
        return [ps_mock_audio(), null];
    }
    if ($cfg['elevenlabs_key'] === '') {
        return [null, 'elevenlabs_key not configured'];
    }
    [$code, $body, $err] = ps_http('POST', 'https://api.elevenlabs.io/v1/music?output_format=mp3_44100_128',
        ['xi-api-key: ' . $cfg['elevenlabs_key'], 'Content-Type: application/json'],
        json_encode(['composition_plan' => $plan, 'model_id' => $cfg['music_model']]), 600);
    if ($code !== 200 || strlen($body) < 2000) {
        return [null, "music $code " . ($err ?: substr($body, 0, 300))];
    }
    return [$body, null];
}

/** Test audio: a few seconds of soft tone from ffmpeg when it is installed, else a tiny silent MP3 frame. */
function ps_mock_audio(): string
{
    $tmp = tempnam(sys_get_temp_dir(), 'ps') . '.mp3';
    @exec('ffmpeg -loglevel error -y -f lavfi -i "sine=frequency=330:duration=6" -af "volume=0.2,afade=t=out:st=5:d=1" -b:a 64k ' . escapeshellarg($tmp) . ' 2>/dev/null');
    $bytes = is_file($tmp) ? (string) file_get_contents($tmp) : '';
    @unlink($tmp);
    return $bytes !== '' ? $bytes : str_repeat("\xFF\xFB\x90\x00" . str_repeat("\x00", 413), 40);
}

// ---------------------------------------------------------------- verify

/** Fold accented letters to plain ones ("Tomás" to "Tomas"), the same way on every system. */
function ps_fold(string $t): string
{
    static $map = ['á' => 'a', 'à' => 'a', 'â' => 'a', 'ä' => 'a', 'ã' => 'a', 'å' => 'a', 'ą' => 'a', 'é' => 'e', 'è' => 'e', 'ê' => 'e', 'ë' => 'e', 'ę' => 'e',
        'í' => 'i', 'ì' => 'i', 'ï' => 'i', 'î' => 'i', 'ó' => 'o', 'ò' => 'o', 'ö' => 'o', 'ô' => 'o', 'õ' => 'o', 'ø' => 'o', 'ú' => 'u', 'ù' => 'u', 'ü' => 'u', 'û' => 'u',
        'ñ' => 'n', 'ń' => 'n', 'ç' => 'c', 'ć' => 'c', 'ł' => 'l', 'ś' => 's', 'š' => 's', 'ż' => 'z', 'ź' => 'z', 'ž' => 'z', 'ý' => 'y', 'ß' => 'ss',
        'Á' => 'A', 'É' => 'E', 'Í' => 'I', 'Ó' => 'O', 'Ú' => 'U', 'Ñ' => 'N', 'Ł' => 'L', 'Ś' => 'S', 'Ż' => 'Z', 'Ç' => 'C', 'Ö' => 'O', 'Ü' => 'U', 'Ä' => 'A'];
    return strtr($t, $map);
}

/**
 * Transcribe the song and check it. Returns
 *   ['pass' => bool, 'name_heard' => n, 'name_expected' => n, 'recall' => 0..1, 'heard_as' => [...], 'error' => ?string]
 */
function ps_verify(string $mp3, array $lyrics, array $names): array
{
    $cfg = ps_config();
    $text = strtolower(ps_lyrics_text($lyrics));
    $want_n = [];                                    // how often each name is written in the lyrics
    foreach ($names as $n) {
        $want_n[strtolower($n)] = preg_match_all('/\b' . preg_quote(strtolower($n), '/') . '\b/u', $text);
    }
    $expected = array_sum($want_n);
    if ($cfg['mock']) {
        return ['pass' => true, 'name_heard' => $expected, 'name_expected' => $expected, 'recall' => 1.0, 'heard_as' => [], 'error' => null, 'mock' => true];
    }
    $tmp = tempnam(sys_get_temp_dir(), 'ps') . '.mp3';
    file_put_contents($tmp, $mp3);
    $transcript = null;
    $last = '';
    foreach (['scribe_v2', 'scribe_v1'] as $model) {
        [$code, $body, $err] = ps_http('POST', 'https://api.elevenlabs.io/v1/speech-to-text', ['xi-api-key: ' . $cfg['elevenlabs_key']],
            ['model_id' => $model, 'language_code' => 'en', 'file' => new CURLFile($tmp, 'audio/mpeg', 'song.mp3')], 300);
        if ($code === 200) {
            $transcript = (string) (json_decode($body, true)['text'] ?? '');
            break;
        }
        $last = "stt $model $code " . ($err ?: substr($body, 0, 200));
    }
    @unlink($tmp);
    if ($transcript === null) {
        return ['pass' => false, 'error' => $last, 'name_heard' => 0, 'name_expected' => $expected, 'recall' => 0.0, 'heard_as' => []];
    }
    // The transcriber marks music as [gentle music] and (humming): not sung words.
    // The transcriber spells by ear ("Tomás" for Tomasz), so accents are folded before words are compared.
    $plain = preg_replace('/\[[^\]]*\]|\([^)]*\)/', ' ', $transcript) ?? $transcript;
    $plain = ps_fold($plain);
    preg_match_all("/[a-z']+/", strtolower($plain), $m);
    $heard = $m[0];
    // Every name is checked on its own: with two names, both must be heard.
    $exact = 0;
    $close = [];
    $each = [];
    $namesOk = true;
    foreach ($want_n as $lname => $n) {
        $got = 0;
        $sound = strtolower(ps_fold($lname));
        foreach (preg_split('/[^a-z\']+/', $sound, -1, PREG_SPLIT_NO_EMPTY) as $part) {      // "mary ann" is heard as two words
            // Heard as the name: the same word, or one that starts with the same letter and is at least 85% the same
            // letters. A song checks the SOUND of a name; the transcriber's spelling of an unusual name rarely matches.
            $part = str_replace("'", '', $part);
            $got = max($got, count(array_filter($heard, function ($w) use ($part) {
                $w = str_replace("'", '', $w);
                if ($w === $part) { return true; }
                if ($w === '' || $w[0] !== $part[0] || strlen($w) < 3) { return false; }
                similar_text($w, $part, $pct);
                return $pct >= 85;
            })));
        }
        $exact += $got;
        $each[$lname] = [$got, $n];
        $namesOk = $namesOk && $got >= max(1, intdiv($n, 2));
        foreach (array_unique($heard) as $w) {
            if ($w !== $lname && !isset($want_n[$w]) && strlen($w) > 2) {
                similar_text($w, $lname, $pct);
                if ($pct >= 75) { $close[] = $w; }
            }
        }
    }
    preg_match_all("/[a-z']+/", $text, $lm);
    $want = array_unique($lm[0]);
    $recall = count($want) ? count(array_intersect($want, $heard)) / count($want) : 0.0;
    // Words sung that are nowhere in the lyrics: the singer improvising.
    $extra = count($heard) ? count(array_filter($heard, fn($w) => !in_array($w, $want, true))) / count($heard) : 0.0;
    return [
        'pass' => $namesOk && $recall >= 0.6 && $extra <= 0.12,
        'name_heard' => $exact, 'name_expected' => $expected, 'each' => $each, 'recall' => round($recall, 2), 'extra' => round($extra, 2),
        'heard_as' => array_values($close), 'error' => null, 'transcript' => $transcript,
    ];
}

// ---------------------------------------------------------------- email

function ps_email_html(array $paras, ?string $button, ?string $link, array $after, string $signoff, string $preheader = ''): string
{
    $e = fn($s) => htmlspecialchars($s, ENT_QUOTES, 'UTF-8');
    $p = fn($s) => '<p style="margin:0 0 16px;font:16px/1.65 Georgia,serif;color:#2A1F1A">' . $e($s) . '</p>';
    $h = '<div style="display:none;max-height:0;overflow:hidden;opacity:0">' . $e($preheader) . '</div>';
    $h .= '<div style="background:#F2ECE1;padding:24px 12px"><div style="max-width:520px;margin:0 auto;background:#FFFDF9;border:1px solid #E6DCCA;border-radius:14px;padding:28px 24px">';
    $h .= '<p style="margin:0 0 22px;font:600 13px/1 Arial,sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#9A7B4F">Sanctoria</p>';
    $h .= implode('', array_map($p, $paras));
    if ($button && $link) {
        $h .= '<p style="margin:26px 0;text-align:center"><a href="' . $e($link) . '" style="display:inline-block;background:#F2C230;border:1px solid #D9A415;border-radius:28px;padding:16px 30px;font:700 16px/1 Arial,sans-serif;color:#2A1F1A;text-decoration:none">' . $e($button) . '</a></p>';
        $h .= '<p style="margin:0 0 20px;font:13px/1.6 Arial,sans-serif;color:#9A8B79;word-break:break-all">' . $e($link) . '</p>';
    }
    $h .= implode('', array_map($p, $after));
    $h .= $p($signoff);
    $h .= '</div><p style="max-width:520px;margin:14px auto 0;font:11.5px/1.6 Arial,sans-serif;color:#9A8B79;text-align:center">Sanctoria &middot; support@sanctoriastore.com</p></div>';
    return $h;
}

/** $kind is "ready" or "delay". Returns [ok, detail]. */
function ps_send_order_mail(array $o, string $kind): array
{
    $c = ps_copy()['email'][$kind] ?? null;
    if (!$c) {
        return [false, 'no email copy'];
    }
    if (($o['answers']['who'] ?? '') === 'myself') {
        $o['buyer'] = '';                      // "Mary, Mary's prayer song" reads wrongly
    }
    $f = fn($s) => ucfirst(ps_fill((string) $s, $o));
    $link = ps_song_url($o['token']);
    if (ps_config()['mail']['driver'] === 'kit') {
        return ps_send_via_kit($o, $kind);
    }
    $paras = array_map($f, $c['p'] ?? []);
    $after = array_map($f, $c['p_after'] ?? []);
    $html = ps_email_html($paras, isset($c['button']) ? $f($c['button']) : null, $link, $after, $f($c['signoff'] ?? ''), $f($c['preheader'] ?? ''));
    $text = implode("\n\n", array_merge($paras, [$link], $after, [$f($c['signoff'] ?? '')]));
    return ps_send_mail($o['email'], $f($c['subject']), $html, $text, "{$kind}-{$o['token']}");
}

/**
 * Kit delivery. Kit has no "send this one email now" call, so the email is a
 * one email sequence that reads the buyer's own custom fields:
 *   1. make sure she is a subscriber (also puts the buyer back on the list)
 *   2. write her song link, title and the loved one's name onto her record
 *   3. add her to the "ready" (or "delay") sequence, which sends the email
 * The sequence must be set to repeat, or a second song would send nothing.
 * Kit will not send to anyone who has unsubscribed: her page link from the
 * thank you step and "find my song" are the safety net for that case.
 */
function ps_send_via_kit(array $o, string $kind): array
{
    $k = ps_config()['kit'];
    $seq = $k[$kind === 'ready' ? 'seq_ready' : 'seq_delay'] ?? null;
    if (empty($k['api_key']) || empty($seq)) {
        return [false, "kit not configured for $kind"];
    }
    $h = ['Content-Type: application/json', 'Accept: application/json', 'X-Kit-Api-Key: ' . $k['api_key']];
    $buyer = ($o['answers']['who'] ?? '') === 'myself' ? '' : (string) $o['buyer'];
    [$c1, $b1] = ps_http('POST', 'https://api.kit.com/v4/subscribers', $h,
        json_encode(array_filter(['email_address' => $o['email'], 'first_name' => $buyer])), 20);
    $id = json_decode($b1, true)['subscriber']['id'] ?? null;
    if (!$id) {
        return [false, "kit subscriber $c1 " . substr($b1, 0, 120)];
    }
    $phr = ps_copy()['phrases'] ?? [];
    // Kit matches custom fields by KEY (prayer_song_link). Sent by label it answers 200 and stores nothing,
    // so the stored link is read back and checked before she is added to the sequence.
    $keys = $k['fields'] ?? [];
    $kUrl = $keys['url'] ?? 'prayer_song_link';
    $fields = [
        $kUrl                                              => ps_song_url($o['token']),
        ($keys['title'] ?? 'prayer_song_title')            => (string) ($o['title'] ?? ''),
        ($keys['name'] ?? 'prayer_song_for')               => ps_names_text($o['answers'] ?? []),
        ($keys['intention'] ?? 'prayer_song_intention')    => (string) ($phr[$o['answers']['intention'] ?? ''] ?? ''),
    ];
    [$c2, $b2] = ps_http('PUT', "https://api.kit.com/v4/subscribers/$id", $h, json_encode(['fields' => $fields]), 20);
    $stored = json_decode($b2, true)['subscriber']['fields'][$kUrl] ?? null;
    if ($c2 < 200 || $c2 >= 300 || $stored !== $fields[$kUrl]) {
        return [false, "kit fields $c2, link not stored " . substr($b2, 0, 80)];        // never send an email with an empty link
    }
    if ($kind === 'ready' && !empty($k['tag_buyer'])) {
        ps_http('POST', "https://api.kit.com/v4/tags/{$k['tag_buyer']}/subscribers", $h, json_encode(['email_address' => $o['email']]), 20);
    }
    if ($kind === 'ready' && !empty($k['tag_all_buyers']) && strpos((string) ($o['receipt'] ?? ''), 'pi_') === 0) {
        // ClickBank buyers get sanctoria-buyer from /ins/clickbank.php; Stripe buyers get it here
        ps_http('POST', "https://api.kit.com/v4/tags/{$k['tag_all_buyers']}/subscribers", $h, json_encode(['email_address' => $o['email']]), 20);
    }
    [$c3, $b3] = ps_http('POST', "https://api.kit.com/v4/sequences/$seq/subscribers", $h, json_encode(['email_address' => $o['email']]), 20);
    return [$c3 >= 200 && $c3 < 300, "kit sequence $seq $c3 " . substr($b3, 0, 120)];
}

function ps_send_mail(string $to, string $subject, string $html, string $text, string $ref): array
{
    $m = ps_config()['mail'];
    if ($to === '') {
        return [false, 'no recipient'];
    }
    switch ($m['driver']) {
        case 'log':        // testing: write the email to disk instead of sending it
            file_put_contents(ps_data("outbox/$ref.html"), "<!-- To: $to | Subject: $subject -->\n$html");
            file_put_contents(ps_data("outbox/$ref.txt"), "To: $to\nSubject: $subject\n\n$text\n");
            return [true, 'logged'];
        case 'resend':
            [$code, $body] = ps_http('POST', 'https://api.resend.com/emails',
                ['Authorization: Bearer ' . $m['api_key'], 'Content-Type: application/json'],
                json_encode(['from' => $m['from'], 'to' => [$to], 'reply_to' => $m['reply_to'], 'subject' => $subject, 'html' => $html, 'text' => $text]));
            return [$code >= 200 && $code < 300, "resend $code " . substr($body, 0, 160)];
        case 'postmark':
            [$code, $body] = ps_http('POST', 'https://api.postmarkapp.com/email',
                ['X-Postmark-Server-Token: ' . $m['api_key'], 'Content-Type: application/json', 'Accept: application/json'],
                json_encode(['From' => $m['from'], 'To' => $to, 'ReplyTo' => $m['reply_to'], 'Subject' => $subject, 'HtmlBody' => $html, 'TextBody' => $text, 'MessageStream' => 'outbound']));
            return [$code === 200, "postmark $code " . substr($body, 0, 160)];
    }
    return [false, 'unknown mail driver'];
}

function ps_alert(string $subject, string $text): void
{
    ps_log("ALERT $subject: $text");
    $to = ps_config()['admin_email'];
    if ($to === '') {
        return;
    }
    $driver = ps_config()['mail']['driver'];
    if (in_array($driver, ['resend', 'postmark', 'log'], true)) {
        ps_send_mail($to, "[Prayer Song] $subject", '<pre>' . htmlspecialchars($text) . '</pre>', $text, 'alert-' . time() . '-' . bin2hex(random_bytes(2)));
    } else {        // buyers' mail goes through Kit, which cannot send a one off note: use the server's own mail for alerts
        @mail($to, "[Prayer Song] $subject", $text, 'From: Sanctoria Prayer Song <no-reply@sanctoriastore.com>');
    }
}

/** Move an order to the review list, tell TS, and stop working on it. */
function ps_hold(array $o, string $why): string
{
    $o['status'] = 'review';
    $o['hold_reason'] = $why;
    ps_note($o, "moved to review: $why");
    ps_save_order($o);
    @unlink(ps_data("queue/{$o['token']}"));
    ps_alert('Song needs review', "Order {$o['token']} (receipt {$o['receipt']}, {$o['email']}).\nWhy: $why\n" . ps_song_url($o['token'])
        . "\n\nOn the server:\n  php worker.php --show {$o['token']}\n  php worker.php --retry {$o['token']}");
    return 'review';
}

/**
 * Is there enough ElevenLabs credit to make a song? Checked at most once every ten minutes.
 * Below 'credit_floor' TS is alerted once a day; below one song's worth, songs wait in the queue.
 */
function ps_credits_ok(): bool
{
    $cfg = ps_config();
    $cache = ps_data('idx/credits.json');
    $c = ps_read($cache);
    if (!$c || time() - ($c['at'] ?? 0) > 600) {
        [$code, $body] = ps_http('GET', 'https://api.elevenlabs.io/v1/user/subscription', ['xi-api-key: ' . $cfg['elevenlabs_key']], null, 20);
        $j = json_decode($body, true);
        if ($code !== 200 || !isset($j['character_limit'])) {
            return true;                        // cannot tell: try the render and let it report its own error
        }
        $c = ['at' => time(), 'left' => (int) $j['character_limit'] - (int) $j['character_count'], 'alerted' => $c['alerted'] ?? ''];
    }
    if ($c['left'] < $cfg['credit_floor'] && ($c['alerted'] ?? '') !== date('Y-m-d')) {
        $c['alerted'] = date('Y-m-d');
        ps_alert('ElevenLabs credits are low', "About {$c['left']} credits left, enough for roughly " . intdiv($c['left'], 3000) . ' more songs.');
    }
    ps_write($cache, $c);
    return $c['left'] >= 3500;
}

// ---------------------------------------------------------------- one order, start to finish

// ---------------------------------------------------------------- putting a song right by hand
// Used by the command line (worker.php) and by the admin page (admin/index.php). Each returns [ok, message].

/** Release attempt $n of a song that failed the automatic check, after someone has listened to it. */
function ps_admin_approve(array $o, int $n = 0): array
{
    $t = $o['token'];
    $n = $n > 0 ? $n : (int) $o['attempts'];
    $src = ps_data("songs/$t.attempt$n.mp3");
    if (!is_file($src)) {
        return [false, "no audio for attempt $n"];
    }
    copy($src, ps_data("songs/$t.mp3"));
    $o['status'] = 'ready';
    $o['ready_at'] = time();
    unset($o['hold_reason']);
    ps_note($o, "attempt $n approved by hand");
    [$sent, $d] = ps_send_order_mail($o, 'ready');
    $o['emailed'] = $sent;
    ps_note($o, "ready email: $d");
    ps_save_order($o);
    @unlink(ps_data("queue/$t"));
    return [true, 'released, email: ' . ($sent ? 'sent' : "NOT sent ($d)")];
}

/** Make the song again. With $say the name is sung from that spelling; with $newLyrics the words are rewritten too. */
function ps_admin_requeue(array $o, ?string $say = null, bool $newLyrics = false, ?string $say2 = null): array
{
    $t = $o['token'];
    if (empty($o['answers'])) {
        return [false, 'this order has no answers yet'];
    }
    if ($say !== null) {
        $say = ps_clean($say, 60);
        if ($say === '') {
            return [false, 'give the sounds-like spelling'];
        }
        $o['answers']['name_phonetic'] = $say;
        if (!empty($o['answers']['name2']) && $say2 !== null && ps_clean($say2, 60) !== '') {
            $o['answers']['name2_phonetic'] = ps_clean($say2, 60);
        }
        $o['phonetic_first'] = true;
        ps_note($o, "remake asked for, name to be sung as \"$say\"");
    } else {
        ps_note($o, 'retry asked for' . ($newLyrics ? ', with new lyrics' : ''));
    }
    if ($newLyrics) {
        $o['lyrics'] = null;
        $o['lyric_tries'] = 0;
    }
    @unlink(ps_data("songs/$t.mp3"));
    $o['status'] = 'queued';
    $o['attempts'] = 0;
    $o['emailed'] = false;
    unset($o['hold_reason']);
    ps_save_order($o);
    ps_enqueue($t);
    return [true, 'queued'];
}

/**
 * The public reviews page reads one small file, rebuilt here whenever a review is approved, taken down,
 * changed or withdrawn. A review is public only if the buyer ticked the permission box AND TS approved it.
 * Only her words, the name she chose, and the date are published: never her email, the order or the song.
 */
function ps_public_reviews_rebuild(): int
{
    $out = [];
    foreach (glob(ps_data('orders/*.json')) ?: [] as $f) {
        $o = ps_read($f);
        $r = $o['review'] ?? null;
        if ($r && !empty($r['share']) && !empty($r['approved']) && trim((string) $r['text']) !== '') {       // a refunded buyer's review is not dropped automatically: that would hide the unhappy ones
            $out[] = ['text' => (string) $r['text'], 'name' => (string) $r['name'], 'at' => (int) ($r['updated'] ?? $r['at'])];
        }
    }
    usort($out, fn($x, $y) => $y['at'] <=> $x['at']);
    ps_write(ps_data('idx/public-reviews.json'), $out);
    return count($out);
}

/** Put a buyer's review on the public page, or take it down. */
function ps_admin_review_public(array $o, bool $show): array
{
    $r = $o['review'] ?? null;
    if (!$r) {
        return [false, 'this order has no review'];
    }
    if ($show && empty($r['share'])) {
        return [false, 'she did not give permission to share it'];
    }
    if ($show && trim((string) $r['text']) === '') {
        return [false, 'there are no words to show, only stars'];
    }
    $o['review']['approved'] = $show;
    ps_note($o, $show ? 'review put on the public page' : 'review taken off the public page');
    ps_save_order($o);
    $n = ps_public_reviews_rebuild();
    return [true, ($show ? 'now on the reviews page' : 'taken off the reviews page') . " ($n showing)"];
}

/** Send a made song now instead of waiting for its time. */
function ps_admin_send_now(array $o): array
{
    if ($o['status'] !== 'waiting' || !is_file(ps_data("songs/{$o['token']}.mp3"))) {
        return [false, 'this song is not waiting to be sent'];
    }
    ps_note($o, 'sent early by hand');
    ps_release($o);
    $o = ps_order($o['token']);
    return [true, 'released, email: ' . (!empty($o['emailed']) ? 'sent' : 'NOT sent')];
}

/** Send the "your song is ready" email again. */
function ps_admin_resend(array $o): array
{
    if ($o['status'] !== 'ready') {
        return [false, 'the song is not ready yet'];
    }
    [$sent, $d] = ps_send_order_mail($o, 'ready');
    $o['emailed'] = $o['emailed'] || $sent;
    ps_note($o, "ready email sent again: $d");
    ps_save_order($o);
    return [$sent, $sent ? 'email sent' : "email NOT sent ($d)"];
}

/** Returns the final status. Safe to run again on the same order. */
function ps_process(string $token): string
{
    $cfg = ps_config();
    $o = ps_order($token);
    if (!$o || !in_array($o['status'], ['queued', 'working'], true) || empty($o['answers'])) {
        @unlink(ps_data("queue/$token"));
        return $o['status'] ?? 'missing';
    }
    $o['status'] = 'working';
    if (empty($o['lyrics'])) {
        if ($cfg['mock']) {
            $o['lyrics'] = ps_write_lyrics($o);
        } elseif ($cfg['anthropic_key'] === '') {
            return ps_hold($o, 'no Claude key is configured, so the lyrics cannot be written');
        } else {
            $r = ps_claude_lyrics($o);
            if (isset($r['hold'])) {
                return ps_hold($o, $r['hold']);
            }
            if (isset($r['error'])) {                       // a passing fault: leave it queued and try again next minute
                $o['lyric_tries'] = ($o['lyric_tries'] ?? 0) + 1;
                ps_note($o, "lyrics attempt {$o['lyric_tries']} failed: {$r['error']}");
                if ($o['lyric_tries'] >= 5) {
                    return ps_hold($o, 'the lyric writer failed five times: ' . $r['error']);
                }
                $o['status'] = 'queued';
                ps_save_order($o);
                return 'queued';
            }
            $o['lyrics'] = $r['lyrics'];
        }
        $o['title']  = $o['lyrics']['title'];
        ps_note($o, 'lyrics written' . (isset($o['lyrics']['tokens']) ? ' ' . json_encode($o['lyrics']['tokens']) : ''));
    }
    ps_save_order($o);                          // the page can show the lyrics while the music is made

    if (!$cfg['mock'] && !ps_credits_ok()) {    // out of ElevenLabs credits: wait in the queue, TS has been alerted
        $o['status'] = 'queued';
        ps_note($o, 'waiting: not enough ElevenLabs credits');
        ps_save_order($o);
        return 'queued';
    }

    $a = $o['answers'];
    $ok = false;
    while ($o['attempts'] < $cfg['max_attempts'] && !$ok) {
        $o['attempts']++;
        // attempt 2 sings the phonetic spelling if she gave one; attempt 3 simply tries again
        $phon = $o['attempts'] === 2 || !empty($o['phonetic_first']);
        $map = [$a['name'] => $phon && $a['name_phonetic'] !== '' ? $a['name_phonetic'] : $a['name']];
        if (($a['name2'] ?? '') !== '') {
            $map[$a['name2']] = $phon && ($a['name2_phonetic'] ?? '') !== '' ? $a['name2_phonetic'] : $a['name2'];
        }
        $sung = implode(' and ', $map);
        [$mp3, $err] = ps_render(ps_build_plan($o['lyrics'], $a, $map));
        if ($mp3 === null) {
            ps_note($o, "attempt {$o['attempts']}: render failed: $err");
            ps_save_order($o);
            continue;
        }
        $v = ps_verify($mp3, $o['lyrics'], ps_names($a));
        ps_note($o, "attempt {$o['attempts']} (sung as \"$sung\"): " . json_encode($v));
        $o['check'] = $v;
        if ($v['pass']) {
            file_put_contents(ps_data("songs/$token.mp3"), $mp3, LOCK_EX);
            $ok = true;
        } else {
            file_put_contents(ps_data("songs/$token.attempt{$o['attempts']}.mp3"), $mp3, LOCK_EX);   // kept for review
        }
        ps_save_order($o);
    }

    if (!$ok) {
        return ps_hold($o, "the song failed its check {$o['attempts']} times");
    }

    @unlink(ps_data("queue/$token"));
    if (time() < ps_send_at($o)) {              // made, but not shown or emailed until its time: the worker releases it
        $o['status'] = 'waiting';
        $o['made_at'] = time();
        ps_note($o, 'song made, to be sent at ' . date('c', ps_send_at($o)));
        ps_save_order($o);
        touch(ps_data("wait/$token"));
        ps_log("made $token attempts={$o['attempts']}, waiting until " . date('c', ps_send_at($o)));
        return 'waiting';
    }
    return ps_release($o);
}

/** Show the finished song on her page and send the "ready" email. */
function ps_release(array $o): string
{
    $token = $o['token'];
    $o['status'] = 'ready';
    $o['ready_at'] = time();
    ps_save_order($o);
    @unlink(ps_data("wait/$token"));
    [$sent, $detail] = ps_send_order_mail($o, 'ready');
    $o['emailed'] = $sent;
    ps_note($o, 'ready email: ' . $detail);
    ps_save_order($o);
    if (!$sent) {
        ps_alert('Delivery email failed', "Order $token: $detail");
    }
    ps_log("ready $token attempts={$o['attempts']} emailed=" . ($sent ? 'yes' : 'no'));
    return 'ready';
}
