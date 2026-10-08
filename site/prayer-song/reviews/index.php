<?php
// The public reviews page. It shows only what buyers wrote on their own private song page, and only
// where the buyer gave permission AND TS has approved it (see ps_public_reviews_rebuild in api/pipeline.php).
// With none yet, it says so plainly. Nothing here is written by Sanctoria, and no ratings or counts are shown.
// Words: prayer-song/copy/03-delivery.md, PAGE: reviews_public.
declare(strict_types=1);
require_once __DIR__ . '/../api/lib.php';

$c = ps_copy()['page']['reviews_public'] ?? [];
if (!$c) {
    http_response_code(404);
    exit;
}
$e = fn($s) => htmlspecialchars((string) $s, ENT_QUOTES, 'UTF-8');
$t = fn(string $k) => $e(is_array($c[$k] ?? '') ? implode(' ', $c[$k]) : ($c[$k] ?? ''));
$reviews = ps_read(ps_data('idx/public-reviews.json')) ?? [];
$has = count($reviews) > 0;
if (isset($_GET['count'])) {                     // the sales page asks this to decide whether to show its Reviews link
    header('Content-Type: application/json');
    header('Cache-Control: public, max-age=300');
    echo json_encode(['n' => count($reviews)]);
    exit;
}
header('Cache-Control: public, max-age=300');
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title><?= $t('title') ?> | Sanctoria</title>
<?php if (!$has): ?><meta name="robots" content="noindex"><?php endif; ?>
<link rel="icon" href="/images/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root{--cream:#F7F3EC;--cream-2:#EFE8DB;--paper:#FFFDF9;--ink:#2A1F1A;--ink-soft:#5B4A40;--muted:#9A8B79;--bronze:#9A7B4F;--bronze-deep:#7A5F39;
        --gold:#F2C230;--gold-edge:#D9A415;--hair:#E6DCCA;--deep:#2B1E19;--serif:'Fraunces',Georgia,serif;--sans:'Inter',system-ui,sans-serif;
        --gut:max(20px,calc((100vw - 1120px)/2))}
  *{box-sizing:border-box}
  body{margin:0;background:var(--cream);color:var(--ink);font-family:var(--sans);-webkit-font-smoothing:antialiased}
  a{color:var(--bronze-deep)}
  .head{position:sticky;top:0;z-index:5;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:10px;padding:10px var(--gut);
        background:rgba(247,243,236,.96);backdrop-filter:blur(6px);border-bottom:1px solid var(--hair)}
  .head img{height:34px;width:auto;display:block}
  .navlinks{order:3;flex:0 0 100%;display:flex;justify-content:center;gap:26px;padding:7px 0 0;margin-top:8px;border-top:1px solid var(--hair)}
  .navlinks a{font-size:13px;font-weight:600;color:var(--ink-soft);text-decoration:none}
  .navlinks a:hover,.navlinks a[aria-current]{color:var(--bronze-deep);text-decoration:underline;text-underline-offset:3px}
  .navbtn{border:1px solid var(--bronze);border-radius:10px;color:var(--bronze-deep);font-weight:700;font-size:14px;padding:10px 15px;text-decoration:none;white-space:nowrap}
  .navbtn,.navbtn:hover{border-color:var(--gold-edge);background:linear-gradient(180deg,#F6CF52,var(--gold));color:var(--ink);box-shadow:0 4px 12px rgba(217,164,21,.22)}
  .navbtn:hover{filter:brightness(1.04)}
  main{padding:44px var(--gut) 56px}
  .top{max-width:760px;margin:0 auto;text-align:center}
  .kick{display:block;width:38px;height:2px;background:var(--bronze);margin:0 auto 16px}
  h1{font-family:var(--serif);font-weight:600;font-size:30px;line-height:1.15;margin:0 0 14px;text-wrap:balance}
  .top p{font-size:17px;line-height:1.65;color:var(--ink-soft);margin:0 auto;max-width:640px}
  .grid{columns:1;column-gap:22px;margin:34px auto 0;max-width:1120px}
  .rv{break-inside:avoid;background:var(--paper);border:1px solid var(--hair);border-radius:16px;padding:24px 22px 20px;margin:0 0 22px}
  .rv blockquote{margin:0;font-family:var(--serif);font-size:18.5px;line-height:1.6;color:var(--ink);white-space:pre-line}
  .rv blockquote::before{content:"\201C";display:block;font-size:44px;line-height:.6;color:var(--bronze);margin:6px 0 10px}
  .rv footer{margin-top:16px;padding-top:14px;border-top:1px solid var(--hair);font-size:14px;color:var(--ink-soft)}
  .rv footer b{color:var(--ink);font-weight:600}
  .rv footer span{color:var(--muted)}
  .how{max-width:760px;margin:34px auto 0;background:var(--cream-2);border-radius:16px;padding:24px 24px 22px}
  .how h2{font-family:var(--serif);font-weight:600;font-size:19px;margin:0 0 8px}
  .how p{font-size:15.5px;line-height:1.65;color:var(--ink-soft);margin:0}
  .go{max-width:420px;margin:34px auto 0;text-align:center}
  .btn{display:block;border:1px solid var(--gold-edge);border-radius:14px;background:linear-gradient(180deg,#F6CF52,var(--gold));color:var(--ink);font-weight:700;font-size:17px;
       padding:18px 14px;text-decoration:none;box-shadow:0 10px 22px rgba(217,164,21,.26)}
  .btn:hover{filter:brightness(1.03)}
  .go .alt{display:inline-block;margin-top:16px;font-size:15px;font-weight:600}
  footer.site{padding:26px var(--gut) 34px;background:var(--cream-2);border-top:1px solid var(--hair);text-align:center;font-size:12px;color:var(--muted);line-height:1.6}
  footer.site a{color:var(--ink-soft)}
  @media (min-width:700px){ .grid{columns:2} }
  @media (min-width:960px){
    :root{--gut:max(40px,calc((100vw - 1120px)/2))}
    .head{flex-wrap:nowrap;padding:14px var(--gut)}
    .head img{height:42px}
    .navlinks{order:0;flex:0 1 auto;margin:0 22px 0 auto;padding:0;border:0;gap:30px}
    .navlinks a{font-size:15px}
    .navbtn{font-size:15px;padding:12px 20px}
    main{padding:76px var(--gut) 90px}
    h1{font-size:44px}
    .top p{font-size:19px}
    .grid{columns:3;margin-top:50px}
  }
</style>
</head>
<body>
<div class="head">
  <a href="../"><img src="/images/logo.png" alt="Sanctoria, Blessed Devotionals" height="34"></a>
  <nav class="navlinks" aria-label="Your order and reviews"><a href="../s/?find"><?= $t('nav_track') ?></a><?php if ($has): ?><a href="./" aria-current="page"><?= $t('nav_reviews') ?></a><?php endif; ?></nav>
  <a class="navbtn" href="../#create"><?= $t('cta') ?></a>
</div>
<main>
  <div class="top">
    <span class="kick"></span>
    <h1><?= $has ? $t('h') : $t('empty_h') ?></h1>
    <p><?= $has ? $t('p') : $t('empty_p') ?></p>
  </div>
  <?php if ($has): ?>
  <div class="grid">
    <?php foreach ($reviews as $r):
        $when = date('F Y', (int) $r['at']);
        $prefix = trim((string) ($c['date_prefix'] ?? '')); ?>
    <article class="rv">
      <blockquote><?= $e($r['text']) ?></blockquote>
      <footer><?php if (trim((string) $r['name']) !== ''): ?><b><?= $e($r['name']) ?></b> &middot; <?php endif; ?><span><?= $e(trim("$prefix $when")) ?></span></footer>
    </article>
    <?php endforeach; ?>
  </div>
  <?php endif; ?>
  <div class="how">
    <h2><?= $t('how_h') ?></h2>
    <p><?= $t('how_p') ?></p>
  </div>
  <div class="go">
    <a class="btn" href="../#create"><?= $t('cta') ?></a>
    <a class="alt" href="../#samples"><?= $t('samples') ?></a>
  </div>
</main>
<footer class="site">
  <a href="../privacy.html">Privacy</a> &nbsp;&middot;&nbsp; <a href="../terms.html">Terms</a> &nbsp;&middot;&nbsp; <a href="/contact.html">Contact</a> &nbsp;&middot;&nbsp; support@sanctoriastore.com<br>
  &copy; Sanctoria. All rights reserved.
</footer>
</body>
</html>
