<?php
// A buyer's own review of her song, sent from her private page. Kept on her order.
// Her words are only ever shown publicly if she ticked the permission box ('share'),
// and never automatically: TS reads them in the admin page and decides.
declare(strict_types=1);
require_once __DIR__ . '/pipeline.php';

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    ps_json_out(['ok' => false], 405);
}
$in = json_decode((string) file_get_contents('php://input'), true);
$token = (string) ($in['k'] ?? '');
$stars = (int) ($in['stars'] ?? 0);
if (!ps_order($token)) {
    ps_json_out(['ok' => false], 404);
}
if ($stars < 1 || $stars > 5) {
    ps_json_out(['ok' => false, 'error' => 'stars'], 422);
}
$text = trim((string) preg_replace('/[ \t]+/', ' ', preg_replace('/[^\P{C}\n]+/u', '', mb_substr((string) ($in['text'] ?? ''), 0, 1500)) ?? ''));
$text = (string) preg_replace('/\n{3,}/', "\n\n", $text);
$name = ps_clean((string) ($in['name'] ?? ''), 60);

$res = ps_locked("order-$token", function () use ($token, $stars, $text, $name, $in) {
    $o = ps_order($token);
    if (!$o || $o['status'] !== 'ready') {
        return [404, false];
    }
    $old = $o['review'] ?? null;
    if ($old && (int) ($old['edits'] ?? 0) >= 10) {              // a review can be changed, but not endlessly
        return [429, false];
    }
    $share = !empty($in['share']);
    if ($share && $name === '') {
        $name = ps_clean((string) ($o['buyer'] ?? ''), 60);          // permission given but no name typed: her first name from the order
    }
    $o['review'] = [
        'stars' => $stars, 'text' => $text, 'name' => $name, 'share' => $share,
        'at' => $old['at'] ?? time(), 'updated' => time(), 'edits' => $old ? (int) ($old['edits'] ?? 0) + 1 : 0,
    ];
    if ($share) {
        // keep what she agreed to, and when: the exact sentence beside the box at the time
        $o['review']['share_at'] = !empty($old['share']) ? ($old['share_at'] ?? time()) : time();
        $o['review']['share_text'] = (string) (ps_copy()['page']['feedback']['share'] ?? '');
    } elseif (!empty($old['share'])) {
        $o['review']['share_withdrawn'] = time();                    // she unticked it: take her words down wherever they are shown
    }
    // a changed review goes back to unread: it is not public again until TS has read the new words
    $wasPublic = !empty($old['approved']);
    ps_note($o, ($old ? 'review changed' : 'review left') . ": $stars stars, " . ($o['review']['share'] ? 'may be shared' : 'private'));
    ps_save_order($o);
    if ($wasPublic) {
        ps_public_reviews_rebuild();
        ps_alert('A published review was changed', "It has been taken off the reviews page until it is read again.\n\n$text");
    }
    return [200, !$old];
});
if ($res[0] !== 200) {
    ps_json_out(['ok' => false], $res[0]);
}
if ($res[1]) {
    ps_alert('A buyer left a review', "$stars stars" . ($name !== '' ? " from $name" : '') . ".\n\n$text\n\n" . (!empty($in['share']) ? 'She gave permission to share it.' : 'Private: no permission to share.'));
}
ps_json_out(['ok' => true]);
