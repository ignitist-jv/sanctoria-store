<?php
// The link in the unfinished-order reminders: GET resume.php?l=<lead id>. Returns her saved answers so the form can reopen
// at the Pay step, or her song page if she has already bought. The lead id is a long random token, like a song link.

declare(strict_types=1);
require_once __DIR__ . '/lib.php';

header('Cache-Control: no-store');
$lid = (string) ($_GET['l'] ?? '');
$l = ps_is_token($lid) ? ps_read(ps_data("leads/$lid.json")) : null;
if (!$l) {
    ps_json_out(['ok' => false], 404);
}
if ($o = ps_lead_order($l)) {
    ps_json_out(['ok' => true, 'song' => ps_song_url($o['token'])]);
}
$a = $l['answers'];
ps_json_out(['ok' => true, 'lead' => $lid, 'email' => $l['email'], 'buyer' => $l['buyer'] ?? '',
    'who' => $a['who'] ?? '', 'name' => $a['name'] ?? '', 'phon' => $a['name_phonetic'] ?? '', 'name2' => $a['name2'] ?? '',
    'who2' => $a['who2'] ?? '', 'intention' => $a['intention'] ?? '', 'note' => $a['note'] ?? '', 'style' => $a['style'] ?? '',
    'voice' => $a['voice'] ?? '']);
