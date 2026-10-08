<?php
// The buyer's private page: /prayer-song/s/?k=<token>
// One page, six states: making, ready (play + download), review, needs (answers), notfound, find.
// All wording comes from api/copy.json, built from prayer-song/copy/03-delivery.md.
// The look is the landing page's: cream, bronze, gold, the arch, the record that turns while it plays.

declare(strict_types=1);
require_once __DIR__ . '/../api/lib.php';

header('X-Robots-Tag: noindex, nofollow');
header('Referrer-Policy: no-referrer');          // the private link is never passed on to another site
header('Cache-Control: no-store');

$token = (string) ($_GET['k'] ?? '');
$o = ps_order($token);
if (isset($_GET['find'])) {
    $state = 'find';
} elseif (isset($_GET['thanks']) && !$o) {
    $state = 'thanks';          // came from the checkout, but the purchase could not be matched to an order yet (see api/thanks.php)
} elseif (!$o) {
    $state = 'notfound';
    http_response_code($token === '' ? 200 : 404);
} else {
    $state = in_array($o['status'], ['queued', 'working', 'waiting'], true) ? 'making'
           : ($o['status'] === 'needs_answers' ? 'needs' : ($o['status'] === 'ready' ? 'ready' : 'review'));
}
$copy = ps_copy()['page'] ?? [];
$c = $copy[$state] ?? [];
$o = $o ?? [];
$e = fn($s) => htmlspecialchars((string) $s, ENT_QUOTES, 'UTF-8');
$t = fn($key) => $e(ps_fill((string) ($c[$key] ?? ''), $o));
$base = ps_config()['base_url'];
$paras = function () use ($c, $o, $e) {
    foreach (($c['p'] ?? []) as $p) {
        echo '<p>' . $e(ps_fill($p, $o)) . "</p>\n";
    }
};
$lyrics = function (string $heading) use ($o, $e) {
    if (empty($o['lyrics']['sections']) || !ps_lyrics_visible($o)) {
        return;
    }
    echo '<section class="lyrics"><span class="kick"></span><h2>' . $heading . "</h2>\n";
    foreach ($o['lyrics']['sections'] as $s) {
        echo '<p class="stanza">' . implode("<br>\n", array_map($e, $s['lines'])) . "</p>\n";
    }
    if (!empty($o['lyrics']['verse'])) {
        echo '<p class="verse">' . $e($o['lyrics']['verse']) . "</p>\n";
    }
    echo "</section>\n";
};
$record = fn(string $cls = '') => '<span class="disc ' . $cls . '" id="disc"><img class="rec" src="../img/record.webp" alt="" width="640" height="640"><i class="sheen"></i></span>';
$audio = '../api/audio.php?k=' . $e($token);
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title><?= $state === 'ready' ? $e($o['title'] ?? 'Your prayer song') : 'Your prayer song' ?> | Sanctoria</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root{--cream:#F7F3EC;--cream-2:#EFE8DB;--paper:#FFFDF9;--ink:#2A1F1A;--ink-soft:#5B4A40;--muted:#9A8B79;--bronze:#9A7B4F;--bronze-deep:#7A5F39;
        --gold:#F2C230;--gold-edge:#D9A415;--green:#2E9E4F;--green-deep:#257F3F;--hair:#E6DCCA;--deep:#2B1E19;--deep-2:#3A2A22;
        --serif:'Fraunces',Georgia,serif;--sans:'Inter',system-ui,sans-serif}
  *{box-sizing:border-box}
  body{margin:0;color:var(--ink);font-family:var(--sans);-webkit-font-smoothing:antialiased;background:#E8E0D2}
  [hidden]{display:none !important}
  .app{max-width:520px;margin:0 auto;min-height:100dvh;background:var(--cream);box-shadow:0 0 60px rgba(42,31,26,.1)}
  .head{display:flex;justify-content:center;padding:14px 16px;border-bottom:1px solid var(--hair);background:var(--cream)}
  .head img{height:32px;width:auto}
  .top{background:radial-gradient(420px 300px at 50% 20%,var(--deep-2) 0%,var(--deep) 80%);padding:28px 20px 30px;text-align:center;color:#F3EADB}
  .eyebrow{font-size:11px;letter-spacing:.18em;text-transform:uppercase;font-weight:700;color:var(--gold);margin-bottom:12px}
  h1{font-family:var(--serif);font-weight:600;font-size:29px;line-height:1.18;margin:0 0 12px;text-wrap:balance;color:#FBF4E6}
  .top p{font-size:16px;line-height:1.62;color:#DCCFBB;margin:0 0 12px}
  .top p:last-of-type{margin-bottom:0}
  .body{padding:0 20px 44px}
  .plain{padding:38px 20px 44px;text-align:center}
  .plain h1{color:var(--ink)}
  .plain p{font-size:16.5px;line-height:1.7;color:var(--ink-soft);margin:0 0 14px}
  h2{font-family:var(--serif);font-weight:600;font-size:22px;line-height:1.25;margin:0 0 10px;text-wrap:balance}
  p{font-size:16px;line-height:1.7;color:var(--ink-soft);margin:0 0 14px}
  .kick{display:block;width:34px;height:2px;background:var(--bronze);margin:0 0 14px}
  section{border-top:1px solid var(--hair);padding:28px 0 6px;margin-top:26px}

  /* the player card overlaps the dark top, so the song is the first thing she sees */
  .rplayer{background:var(--paper);border-radius:18px;padding:24px 22px 22px;margin:-18px 0 0;position:relative;box-shadow:0 18px 40px rgba(42,31,26,.16)}
  .wrap{position:relative;width:66%;margin:0 auto 20px;aspect-ratio:1}
  .disc{position:absolute;inset:0;display:block;border-radius:50%;box-shadow:0 14px 30px rgba(42,31,26,.3)}
  .disc .rec{display:block;width:100%;height:100%;border-radius:50%;animation:spin 3.4s linear infinite;animation-play-state:paused}
  .disc.spin .rec{animation-play-state:running}
  .disc .sheen{position:absolute;inset:0;border-radius:50%;pointer-events:none;
    background:conic-gradient(from 28deg,rgba(255,255,255,0) 0deg,rgba(255,255,255,.2) 24deg,rgba(255,255,255,0) 52deg,rgba(255,255,255,0) 180deg,rgba(255,255,255,.13) 204deg,rgba(255,255,255,0) 232deg,rgba(255,255,255,0) 360deg);
    -webkit-mask:radial-gradient(circle,transparent 0 24%,#000 25% 70%,transparent 71%);mask:radial-gradient(circle,transparent 0 24%,#000 25% 70%,transparent 71%)}
  @keyframes spin{to{transform:rotate(360deg)}}
  .track{height:6px;border-radius:3px;background:#E6DCCA;position:relative;cursor:pointer;touch-action:none}
  .track i{position:absolute;left:0;top:0;bottom:0;width:0%;border-radius:3px;background:var(--bronze)}
  .track i::after{content:"";position:absolute;right:-7px;top:-4px;width:14px;height:14px;border-radius:50%;background:var(--bronze-deep)}
  .times{display:flex;justify-content:space-between;font-size:12.5px;font-weight:600;color:var(--muted);margin-top:9px}
  .ctrl{display:flex;align-items:center;justify-content:center;gap:26px;margin-top:8px}
  .ctrl button{border:0;background:none;cursor:pointer;color:var(--muted);padding:8px;font-family:var(--sans);font-size:12px;font-weight:700}
  .play{width:66px;height:66px;border-radius:50%;border:1px solid var(--gold-edge) !important;background:linear-gradient(180deg,#F7CE4A 0%,var(--gold) 100%) !important;
        color:var(--ink) !important;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 20px rgba(217,164,21,.34)}
  .play svg{width:22px;height:22px}
  .ico-pause{display:none}
  .on .ico-play{display:none}
  .on .ico-pause{display:block}
  .btn{display:flex;align-items:center;justify-content:center;gap:10px;width:100%;border:1px solid var(--gold-edge);border-radius:14px;padding:17px 14px;cursor:pointer;
       background:linear-gradient(180deg,#F7CE4A 0%,var(--gold) 100%);color:var(--ink);font-family:var(--sans);font-size:17px;font-weight:700;text-decoration:none;
       white-space:nowrap;box-shadow:0 1px 0 rgba(255,255,255,.55) inset,0 8px 22px rgba(217,164,21,.3)}
  .btn:hover{background:linear-gradient(180deg,var(--green) 0%,var(--green-deep) 100%);color:#FBFDF9;border-color:var(--green-deep)}
  .btn svg{width:18px;height:18px}
  .btn.quiet{background:var(--paper);border-color:#D2C3A6;box-shadow:none;font-weight:600;font-size:16px}
  .btn.quiet:hover{background:var(--cream-2);color:var(--ink);border-color:var(--bronze)}
  .btn:focus-visible,.play:focus-visible,.sin:focus-visible{outline:2px solid var(--bronze-deep);outline-offset:3px}
  .dl{margin-top:20px}
  .micro{font-size:13px;color:var(--muted);text-align:center;line-height:1.5;margin:11px 0 0}
  .two{display:grid;grid-template-columns:1fr 1fr;gap:10px}
  .stanza{font-family:var(--serif);font-size:17.5px;line-height:1.75;color:var(--ink);margin:0 0 18px}
  .verse{font-size:12px;letter-spacing:.12em;text-transform:uppercase;font-weight:700;color:var(--bronze)}
  .status{display:flex;align-items:center;justify-content:center;gap:11px;margin:22px 0 0;padding:14px;border:1px solid rgba(233,216,183,.35);border-radius:12px;
          font-size:15px;font-weight:600;color:#F3EADB}
  .spinner{width:18px;height:18px;border-radius:50%;border:2px solid rgba(242,194,48,.3);border-top-color:var(--gold);animation:spin 1.1s linear infinite;flex:none}
  .arch{position:relative;margin:0 auto 22px;width:56%;aspect-ratio:1/.9;border-radius:999px 999px 0 0;overflow:hidden;border:1px solid rgba(233,216,183,.4);border-bottom:0;
        background:radial-gradient(300px 240px at 50% 60%,#5A4233 0%,#33241D 78%)}
  .arch .disc{inset:auto;left:50%;top:60%;width:84%;aspect-ratio:1;transform:translate(-50%,-50%);box-shadow:0 14px 30px rgba(0,0,0,.5)}
  .sin{width:100%;background:var(--paper);border:1px solid #D9CFC0;border-radius:12px;padding:15px 14px;font-family:var(--sans);font-size:16px;color:var(--ink);margin:6px 0 12px}
  .sin:focus{outline:none;border-color:var(--bronze-deep)}
  .err{color:#B0321F;font-size:14px;margin:0 0 12px}
  .link{color:var(--bronze-deep);font-weight:600}
  .fb fieldset{border:0;padding:0;margin:14px 0 4px}
  .fb legend,.fb .fl{display:block;font-weight:600;font-size:15px;margin:16px 0 7px;padding:0}
  .starrow{display:inline-flex;flex-direction:row-reverse;gap:4px}
  .starrow input{position:absolute;opacity:0;width:1px;height:1px}
  .starrow label{cursor:pointer;padding:3px;line-height:0}
  .starrow svg{width:38px;height:38px;fill:#E7DCC6;stroke:#C9B48A;stroke-width:1;transition:fill .12s}
  .starrow input:checked ~ label svg,.starrow label:hover svg,.starrow label:hover ~ label svg{fill:var(--gold);stroke:var(--gold-edge)}
  .starrow input:focus-visible + label{outline:2px solid var(--bronze-deep);outline-offset:2px;border-radius:6px}
  .fb textarea,.fb input[type=text]{width:100%;font-family:var(--sans);font-size:16px;line-height:1.5;color:var(--ink);background:#fff;border:1px solid #D2C3A6;border-radius:12px;padding:13px 14px}
  .fb textarea{resize:vertical;min-height:110px}
  .fbshare{display:flex;gap:11px;align-items:flex-start;margin:16px 0 18px;font-size:14.5px;line-height:1.5;color:var(--ink-soft);cursor:pointer}
  .fbshare input{flex:none;width:20px;height:20px;margin:1px 0 0;accent-color:var(--bronze-deep)}
  .fberr{color:#A23B2A;font-weight:600;font-size:14.5px;margin:0 0 12px}
  .fbthanks{margin:0 0 6px}
  .linkbtn{border:0;background:none;padding:4px 0;cursor:pointer;font-family:var(--sans);font-size:14.5px;font-weight:600;color:var(--bronze-deep);text-decoration:underline;text-underline-offset:3px}
  .top a.link{color:#F2C230}
  .watch{background:var(--paper);border:1px solid #E8DCC6;border-radius:14px;padding:16px 18px;margin:18px 0 4px;text-align:left}
  .watch b{display:block;font-family:var(--serif);font-size:17px;font-weight:600;color:var(--ink);margin-bottom:6px}
  .watch p{font-size:15px;line-height:1.55;color:var(--ink-soft);margin:0 0 8px}
  .watch p:last-child{margin-bottom:0}
  .rcpt{padding:22px 22px 30px;border-top:1px solid var(--hair);background:var(--cream-2);text-align:center}
  .rcpt p{margin:0 0 6px;font-size:13px;line-height:1.5;color:var(--ink-soft)}
  .rcpt p.cb{margin-top:14px;font-size:10.5px;color:var(--muted)}
  .rcpt a{color:var(--bronze-deep)}
  .brow{border-top:1px solid var(--hair);padding:16px 0 4px}
  .brow:first-of-type{border-top:0;padding-top:4px}
  .brow b{display:block;font-family:var(--serif);font-weight:600;font-size:17.5px;line-height:1.3}
  .brow > span{display:block;color:var(--ink-soft);font-size:15px;line-height:1.45;margin:3px 0 12px}
  .bonus .micro{margin-top:14px}
  @media (max-width:340px){ h1{font-size:25px} .btn{font-size:15.5px} .two{grid-template-columns:1fr} }
  @media (prefers-reduced-motion:reduce){ .disc .rec,.spinner{animation:none} }
</style>
</head>
<body>
<div class="app">
  <div class="head"><a href="<?= $e($base) ?>/"><img src="/images/logo.png" alt="Sanctoria, Blessed Devotionals" height="32"></a></div>

<?php if ($state === 'making'): ?>
  <div class="top">
    <div class="arch"><?= $record() ?></div>
    <div class="eyebrow"><?= $t('eyebrow') ?></div>
    <h1><?= $t('h') ?></h1>
    <?php $paras(); ?>
    <?php if (!empty($c['email_p'])):
        $from = (string) (ps_config()['kit']['from_email'] ?? 'support@sanctoriastore.com');
        $subject = ps_fill((string) (ps_copy()['email']['ready']['subject'] ?? ''), $o); ?>
    <div class="watch">
      <b><?= $t('email_h') ?></b>
      <p><?= $e(strtr(ps_fill((string) $c['email_p'], $o), ['{from}' => $from, '{subject}' => $subject])) ?></p>
      <?php if (!empty($c['keep'])): ?><p><?= $t('keep') ?></p><?php endif; ?>
    </div>
    <?php endif; ?>
    <div class="status" role="status"><span class="spinner" aria-hidden="true"></span><span><?= $t('status') ?></span></div>
  </div>
  <div class="body"><?php $lyrics($t('lyrics_h')); ?></div>
  <script>
    (function(){
      var hadLyrics = <?= ps_lyrics_visible($o) ? 'true' : 'false' ?>;
      setInterval(function(){
        fetch('../api/status.php?k=<?= $e($token) ?>', {cache:'no-store'}).then(function(r){ return r.json(); }).then(function(j){
          if (j.status !== 'making' || (j.has_lyrics && !hadLyrics)) { location.reload(); }
        }).catch(function(){});
      }, 5000);
    })();
  </script>

<?php elseif ($state === 'ready'): ?>
  <div class="top" style="padding-bottom:44px">
    <div class="eyebrow"><?= $t('eyebrow') ?></div>
    <h1><?= $t('h') ?></h1>
    <p><?= $t('sub') ?></p>
  </div>
  <div class="body">
    <div class="rplayer">
      <div class="wrap"><?= $record() ?></div>
      <div class="track" id="track"><i id="fill"></i></div>
      <div class="times"><span id="now">0:00</span><span id="dur">0:00</span></div>
      <div class="ctrl">
        <button type="button" id="back15" aria-label="Back 15 seconds">&minus;15s</button>
        <button class="play" type="button" id="play" aria-label="Play or pause">
          <svg class="ico-play" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>
          <svg class="ico-pause" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg>
        </button>
        <button type="button" id="fwd15" aria-label="Forward 15 seconds">+15s</button>
      </div>
      <audio id="au" preload="metadata" src="<?= $audio ?>"></audio>
      <a class="btn dl" href="<?= $audio ?>&amp;dl=1" download>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4v11M7 11l5 5 5-5M5 20h14"/></svg>
        <span><?= $t('download') ?></span></a>
      <p class="micro"><?= $t('download_note') ?></p>
    </div>

    <?php $lyrics($t('lyrics_h')); ?>
    <?php $bp = ps_copy()['bonus']['page'] ?? null; if ($bp && !empty($bp['items'])): ?>
    <section class="bonus">
      <span class="kick"></span><h2><?= $e($bp['h']) ?></h2>
      <?php foreach ($bp['items'] as $it): ?>
      <div class="brow">
        <b><?= $e($it['title']) ?></b>
        <span><?= $e($it['desc']) ?></span>
        <a class="btn quiet" href="../api/bonus.php?k=<?= $e($token) ?>&amp;f=<?= $e($it['f']) ?>" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4v11M7 11l5 5 5-5M5 20h14"/></svg>
          <span><?= $e($it['button']) ?></span></a>
      </div>
      <?php endforeach; ?>
      <p class="micro"><?= $e($bp['print']) ?></p>
    </section>
    <?php endif; ?>
    <?php $fb = $copy['feedback'] ?? null; $rv = $o['review'] ?? null; if ($fb && !empty($fb['h'])):
          $f = fn($k) => $e(ps_fill((string) (is_array($fb[$k] ?? '') ? implode(' ', $fb[$k]) : ($fb[$k] ?? '')), $o)); ?>
    <section class="fb" id="review">
      <span class="kick"></span><h2><?= $f('h') ?></h2>
      <div id="fbdone"<?= $rv ? '' : ' hidden' ?>>
        <p class="fbthanks"><b><?= $f('thanks_h') ?></b> <?= $f('thanks_p') ?></p>
        <button class="linkbtn" type="button" id="fbedit"><?= $f('edit') ?></button>
      </div>
      <form id="fbform" novalidate<?= $rv ? ' hidden' : '' ?>>
        <p><?= $f('p') ?></p>
        <fieldset class="stars">
          <legend><?= $f('stars_label') ?></legend>
          <div class="starrow">
          <?php for ($i = 5; $i >= 1; $i--): ?>
            <input type="radio" name="stars" id="st<?= $i ?>" value="<?= $i ?>"<?= $rv && (int) $rv['stars'] === $i ? ' checked' : '' ?>>
            <label for="st<?= $i ?>" aria-label="<?= $i ?> of 5"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.6l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.5l-5.9 3.1 1.2-6.5L2.5 9.5l6.6-.9z"/></svg></label>
          <?php endfor; ?>
          </div>
        </fieldset>
        <label class="fl" for="fbtext"><?= $f('text_label') ?></label>
        <textarea id="fbtext" maxlength="1500" rows="4" placeholder="<?= $f('text_hint') ?>"><?= $e($rv['text'] ?? '') ?></textarea>
        <label class="fl" for="fbname"><?= $f('name_label') ?></label>
        <input id="fbname" type="text" maxlength="60" placeholder="<?= $f('name_hint') ?>" value="<?= $e($rv['name'] ?? ($o['buyer'] ?? '')) ?>">
        <label class="fbshare"><input type="checkbox" id="fbshare"<?= !empty($rv['share']) ? ' checked' : '' ?>><span><?= $f('share') ?></span></label>
        <p class="fberr" id="fberr" role="alert" hidden data-stars="<?= $f('error_stars') ?>" data-fail="<?= $f('error') ?>"></p>
        <button class="btn" type="submit"><?= $f('button') ?></button>
      </form>
    </section>
    <?php endif; ?>
    <section>
      <span class="kick"></span><h2><?= $t('share_h') ?></h2>
      <p><?= $t('share_p') ?></p>
      <div class="two">
        <button class="btn quiet" type="button" id="copy" data-done="<?= $t('copied') ?>"><?= $t('copy') ?></button>
        <button class="btn quiet" type="button" id="share" hidden>Share</button>
      </div>
    </section>
    <section>
      <span class="kick"></span><h2><?= $t('remake_h') ?></h2>
      <p><?= $t('remake_p') ?></p>
    </section>
    <section>
      <span class="kick"></span><h2><?= $t('another_h') ?></h2>
      <p><?= $t('another_p') ?></p>
      <a class="btn quiet" href="<?= $e($base) ?>/#create"><?= $t('another_button') ?></a>
    </section>
  </div>
  <script>
    (function(){
      function $(id){ return document.getElementById(id); }
      var A=$('au'), P=$('play'), D=$('disc');
      function fmt(s){ s=Math.max(0,Math.floor(s||0)); return Math.floor(s/60)+':'+('0'+(s%60)).slice(-2); }
      function paint(){ var on=!A.paused; P.classList.toggle('on',on); D.classList.toggle('spin',on); }
      P.addEventListener('click', function(){ if(A.paused){ A.play().catch(function(){}); } else { A.pause(); } });
      A.addEventListener('play',paint); A.addEventListener('pause',paint); A.addEventListener('ended',paint);
      A.addEventListener('loadedmetadata', function(){ $('dur').textContent=fmt(A.duration); });
      A.addEventListener('timeupdate', function(){ $('fill').style.width=(A.duration?A.currentTime/A.duration*100:0)+'%'; $('now').textContent=fmt(A.currentTime); });
      function seek(e){ if(!A.duration) return; var r=$('track').getBoundingClientRect(); A.currentTime=Math.min(1,Math.max(0,(e.clientX-r.left)/r.width))*A.duration; }
      $('track').addEventListener('pointerdown', function(e){ seek(e); $('track').setPointerCapture(e.pointerId); $('track').onpointermove=seek; });
      $('track').addEventListener('pointerup', function(){ $('track').onpointermove=null; });
      $('back15').addEventListener('click', function(){ A.currentTime=Math.max(0,A.currentTime-15); });
      $('fwd15').addEventListener('click', function(){ if(A.duration) A.currentTime=Math.min(A.duration,A.currentTime+15); });
      var F=$('fbform');
      if(F){
        $('fbedit').addEventListener('click', function(){ $('fbdone').hidden=true; F.hidden=false; });
        F.addEventListener('submit', function(ev){
          ev.preventDefault();
          var st=F.querySelector('input[name=stars]:checked'), err=$('fberr'), btn=F.querySelector('button[type=submit]');
          if(!st){ err.textContent=err.getAttribute('data-stars'); err.hidden=false; return; }
          err.hidden=true; btn.disabled=true;
          fetch('../api/review.php',{method:'POST',headers:{'Content-Type':'application/json'},
            body:JSON.stringify({k:<?= json_encode($token) ?>,stars:+st.value,text:$('fbtext').value,name:$('fbname').value,share:$('fbshare').checked})})
            .then(function(r){ if(!r.ok) throw 0; F.hidden=true; $('fbdone').hidden=false; $('review').scrollIntoView({block:'center'}); })
            .catch(function(){ err.textContent=err.getAttribute('data-fail'); err.hidden=false; })
            .then(function(){ btn.disabled=false; });
        });
      }
      var url=location.href;
      $('copy').addEventListener('click', function(){ var b=this; function done(){ b.textContent=b.getAttribute('data-done'); }
        if(navigator.clipboard){ navigator.clipboard.writeText(url).then(done,function(){ prompt('',url); }); } else { prompt('',url); } });
      if(navigator.share){ $('share').hidden=false; $('share').addEventListener('click', function(){ navigator.share({title:document.title,url:url}).catch(function(){}); }); }
    })();
  </script>

<?php elseif ($state === 'needs'): ?>
  <div class="plain">
    <h1><?= $t('h') ?></h1>
    <?php $paras(); ?>
    <a class="btn" href="<?= $e($base) ?>/?order=<?= $e($token) ?>#create"><?= $t('button') ?></a>
  </div>

<?php elseif ($state === 'find'): ?>
  <div class="plain">
    <h1><?= $t('h') ?></h1>
    <?php $paras(); ?>
    <form id="find" novalidate>
      <input class="sin" id="fe" type="email" inputmode="email" autocomplete="email" placeholder="<?= $t('placeholder') ?>">
      <p class="err" id="ferr" hidden><?= $t('error') ?></p>
      <button class="btn" type="submit"><?= $t('button') ?></button>
    </form>
    <p id="fdone" hidden><?= $t('done') ?></p>
  </div>
  <script>
    document.getElementById('find').addEventListener('submit', function(ev){
      ev.preventDefault();
      var v=document.getElementById('fe').value.trim(), err=document.getElementById('ferr'), f=this;
      if(!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v)){ err.hidden=false; return; }
      err.hidden=true;
      function done(){ f.hidden=true; document.getElementById('fdone').hidden=false; }
      fetch('../api/find.php', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({email:v})}).then(done, done);
    });
  </script>

<?php elseif ($state === 'thanks'):
    $from = (string) (ps_config()['kit']['from_email'] ?? 'support@sanctoriastore.com');
    $rc = $copy['receipt'] ?? [];
    $ref = preg_replace('/[^A-Za-z0-9-]/', '', (string) ($_GET['r'] ?? '')); ?>
  <div class="top">
    <div class="arch"><?= $record() ?></div>
    <div class="eyebrow"><?= $t('eyebrow') ?></div>
    <h1><?= $t('h') ?></h1>
    <?php foreach (($c['p'] ?? []) as $p): ?>
    <p><?= str_replace('support@sanctoriastore.com', '<a class="link" href="mailto:support@sanctoriastore.com">support@sanctoriastore.com</a>', $e(str_replace('{from}', $from, (string) $p))) ?></p>
    <?php endforeach; ?>
    <?php if (!empty($c['find'])): ?><p><a class="link" href="?find=1"><?= $t('find') ?></a></p><?php endif; ?>
  </div>
  <div class="rcpt">
    <?php if ($ref !== ''): ?><p><?= $e(str_replace('{receipt}', $ref, (string) ($rc['order'] ?? ''))) ?></p><?php endif; ?>
    <p><?= $e($rc['statement'] ?? '') ?></p>
    <p class="cb">ClickBank is the retailer of products on this site. CLICKBANK&reg; is a registered trademark of Click Sales Inc., a Delaware corporation located at 1444 S. Entertainment Ave., Suite 410 Boise, ID 83709, USA and used by permission. ClickBank's role as retailer does not constitute an endorsement, approval or review of these products or any claim, statement or opinion used in promotion of these products.</p>
  </div>

<?php else: /* review, notfound */ ?>
  <div class="plain">
    <h1><?= $t('h') ?></h1>
    <?php $paras(); ?>
    <?php if ($state === 'notfound' && !empty($c['find'])): ?>
      <p><a class="link" href="?find=1"><?= $t('find') ?></a></p>
    <?php endif; ?>
  </div>
  <?php if ($state === 'review'): ?><div class="body"><?php $lyrics($e(ps_fill((string) ($copy['making']['lyrics_h'] ?? ''), $o))); ?></div><?php endif; ?>
<?php endif; ?>
<?php $rc = $copy['receipt'] ?? null; if ($rc && !empty($o['receipt']) && in_array($state, ['making', 'ready', 'review', 'needs'], true)): ?>
  <div class="rcpt">
    <p><?= $e(str_replace('{receipt}', (string) $o['receipt'], (string) ($rc['order'] ?? ''))) ?></p>
    <p><?= $e($rc['statement'] ?? '') ?></p>
    <p><?= str_replace('support@sanctoriastore.com', '<a href="mailto:support@sanctoriastore.com">support@sanctoriastore.com</a>', $e($rc['help'] ?? '')) ?></p>
    <p class="cb">ClickBank is the retailer of products on this site. CLICKBANK&reg; is a registered trademark of Click Sales Inc., a Delaware corporation located at 1444 S. Entertainment Ave., Suite 410 Boise, ID 83709, USA and used by permission. ClickBank's role as retailer does not constitute an endorsement, approval or review of these products or any claim, statement or opinion used in promotion of these products.</p>
  </div>
<?php endif; ?>
</div>
</body>
</html>
