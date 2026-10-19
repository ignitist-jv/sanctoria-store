# Prayer Song: how everything connects

Written 2026-10-05. The whole chain is built and passes its tests on this machine in practice mode.
Nothing is uploaded: `site/prayer-song/HOLD` stops `deploy/deploy.sh` from sending the folder.

## LIVE STATE (2026-10-07)

TS said "ship". The prayer song folder is on the server and public at https://sanctoriastore.com/prayer-song/ :

- Uploaded with `python3 deploy/deploy.py --only prayer-song` (48 files; no other page on the site was touched). The `HOLD` file is gone.
- The page is a `--soft` build (`python3 prayer-song/tools/build_landing.py --soft`): no preview bar, form works and saves answers, but there is NO checkout link yet, so the last button says checkout is not open. It is `noindex`.
- `api/config.php` was placed by hand over FTPS (keys, Kit as the mail driver, admin password hash). A copy is in `prayer-song/demo-data/server-config.php` and the admin password in `prayer-song/demo-data/ADMIN-PASSWORD-LIVE.txt` (neither is in git).
- `tools/check_live.py` passes: every private file answers 403, every public page 200. PHP 8.1 runs the code. A test form submission was saved, and buyer data is stored outside the web folder.
- NOT yet done, so no song can be sold or made on the live site: (1) the cron job in cPanel, (2) the ClickBank item and checkout link, then a `--live` build and a second `--only prayer-song` deploy, (3) a real test purchase.
- One test lead exists on the server from launch-check@example.com.

## The chain

```
Landing page  /prayer-song/
   │  four step form
   ▼
api/lead.php ───────────────► answers saved under a lead id (lid), cookie set
   │  checkout link carries &lid=...
   ▼
ClickBank checkout ($39)
   ├─ notification ─► api/ins.php ────┐
   └─ buyer's browser ► api/thanks.php ┴► ONE order per receipt, one 32 character token
                                           │
                        cron, every minute ▼
                                    api/worker.php
                                      1. Claude writes the lyrics        (api/lyrics.php)
                                      2. ElevenLabs sings them           (api/pipeline.php)
                                      3. the song is transcribed and checked: name sung, words intact, nothing added
                                      4. the MP3 is stored where no web address points
                                      5. Kit: her record gets the link, she is added to the delivery sequence
                                           │
                                           ▼
                        /prayer-song/s/?k=<token>   play, download, lyrics, share
```

## What is connected, and what is waiting

| Piece | State | Waiting on |
|---|---|---|
| Landing page, form, download page | Built, previewed | TS to say ship |
| Order and token logic, ClickBank decrypt and proof of purchase | Built, tested with a forged test sale | A real ClickBank item |
| Music (ElevenLabs) | Working: 7 real songs made | Key copied into the server config |
| Lyrics (Claude) | Working: one real order run 2026-10-06 ("Call Daniel Home", lyrics passed the structure check first time, song 3:54, name sung 7 of 7, 58 seconds start to finish) | Key copied into the server config |
| Email (Kit) | Working: "song is ready" email published and sent for real to TS on 2026-10-06, about 30 to 55 seconds after the hand-off. A second send to the same person also went out (repeat works). Bug found and fixed that day: Kit stores custom fields only when they are sent by KEY (prayer_song_link), by label it answers 200 and stores nothing; the code now reads the stored link back before adding to the sequence | "Taking a little longer" email still unpublished |
| Find my song, remake, review tools, credit alert | Built, tested in practice mode | |
| Bonuses (three printables) | Built 2026-10-06, as PDFs made on request by `api/bonus.php?k=<token>&f=sheet|card|companion`. The lyric sheet and prayer card are made from the order (name, lyrics, verse); the companion is the same for everyone. Words in `copy/04-bonuses.md`, all nine verses checked against drbo.org. Three download rows on the song page. Samples in `creative/bonus-samples/` | TS to read them |
| Server (LiquidWeb) | Nothing uploaded | The checks below |

## Kit, created 2026-10-05

- Custom fields: `Prayer Song Link`, `Prayer Song Title`, `Prayer Song For`, `Prayer Song Intention`
- Sequence 2917156 "Sanctoria Prayer Song: delivery (song is ready) DRAFT": one email, unpublished, sends immediately on entry
- Sequence 2917157 "Sanctoria Prayer Song: taking a little longer DRAFT": one email, unpublished
- Both repeat, so a second song for the same buyer sends again. Sender admin@sanctoriastore.com, "Text only" template.
- To go live: read them at https://app.kit.com/sequences/2917156 and /2917157, publish each email, and drop "DRAFT" from the names.
- Kit never emails someone who has unsubscribed. Her page after checkout and "find my song" cover that case.

## Going live, in order (ClickBank last, as TS asked)

1. **Claude API key.** console.anthropic.com. Then one real order end to end on this machine: `python3 prayer-song/tools/demo_order.py` (it will use Claude once the key is in `.env` as `ANTHROPIC_API_KEY`).
2. **Publish the two Kit emails.**
3. **Server config.** On the server, copy `api/config.sample.php` to `api/config.php` and fill in: `elevenlabs_key`, `anthropic_key`, `admin_email`, `admin_hash` (TS chooses the admin password), `mail.driver = kit`. The ClickBank secret and Kit key are read from the existing `/ins/config.php`.
4. **Ship.** TS says ship; delete `site/prayer-song/HOLD`; run `deploy/deploy.sh`.
5. **Cron** in cPanel (Advanced, Cron Jobs), Common Settings "Once Per Minute", command: `/usr/local/bin/ea-php81 /home/sanctoriastore/public_html/prayer-song/api/worker.php >/dev/null 2>&1`
6. **Check the server:** `php api/doctor.php --live` on the server, and `python3 prayer-song/tools/check_live.py` from here (confirms the private files return 403).
7. **ClickBank:** create item `prayersong-1` titled "Your Prayer Song" at $39, digital, Thank You URL `https://sanctoriastore.com/prayer-song/api/thanks.php`; add `https://sanctoriastore.com/prayer-song/api/ins.php` as an extra INS URL (version 6.0 or later; leave the existing two in place); put the checkout link in `CHECKOUT_URL` in `tools/build_landing.py` and rebuild.
8. **A real test purchase**, then a refund. Confirm `lid` arrives in the notification (`php worker.php --show <token>` shows "created via ins" with her answers attached).
9. ElevenLabs: move from Starter to Creator before ads run.

## The admin page (built 2026-10-06)

`https://sanctoriastore.com/prayer-song/admin/` . The server has no Terminal, so this page is how a held song is released and how a remake is asked for.

- One password. Its hash goes in `api/config.php` as `admin_hash`; with no hash the page answers 404.
- Lists every order, with "Needs you" first: songs held after failing their check, songs whose email did not go out, songs waiting too long.
- On an order: listen to each recording, **Send attempt N** (release a held song and email the buyer), **Remake** with the name typed as it sounds, **Make again** (optionally with new lyrics), **Send again** (the email).
- A remake only puts the order back in the queue; cron makes the song a minute or two later.
- Five wrong passwords from one address locks sign in for fifteen minutes. Signed in sessions end after two hours idle.
- Local preview: `prayer-song/tools/demo_server.sh`, then http://localhost:4174/prayer-song/admin/ . The preview password is in `prayer-song/demo-data/ADMIN-PASSWORD.txt` (not in git, never uploaded).

## Sample clips on the sales page (made 2026-10-06)

Each of the three sample cards shows a silent 5 second looping clip above its play button: `site/prayer-song/video/sample-{son,mother,grandchild}.mp4` plus a first frame `.webp`. They are generated illustrations in a home video style, NOT customers: nobody speaks to camera, there is no text on them, and the section says so twice ("The scenes are illustrations made by Sanctoria and do not show customers"). Prompts: `creative/sample-clip-prompts.{md,json}` (creative specialist). Stills from gpt_image_2_5, video from seedance_2_5 with the still as both first and last frame; job ids in `creative/sample-clips/jobs.json`; `creative/sample-clips/process.sh` makes the web files. At the top of the sales page, twelve scenes play as one silent, seamless loop of about 54 seconds, shown full width (`video/hero.mp4`, 600x450): the three sample scenes plus nine made for the top (prompts in `creative/hero-clip-prompts.{md,json}` and `hero-clip-prompts-2.{md,json}`). Playing order: couple, daughter, grandfather, herself, table, friends, marriage, father, car, grandchild, son, mother. `creative/sample-clips/hero.py <slugs in order>` joins them; job ids are in `creative/sample-clips/jobs.json`. The sentence "The scenes are illustrations made by Sanctoria and do not show customers." sits directly under it (it is the hero FILM_NOTE line; the small print under the sample cards was removed at TS's request on 2026-10-07). Delete `video/hero.mp4` and rebuild to get the record back. If the clips are ever removed, restore the two earlier lines in the sample section (note 20 in the landing copy). Do not use these clips in ads as if they were customers.

## Reviews (built 2026-10-06)

The song page asks every buyer for a review, below the lyrics and the printables: five stars, her words, the name to show, and an UNTICKED box giving permission to share. `api/review.php` saves it on her order (`review`), with the exact permission sentence and its date when she ticks the box, and a `share_withdrawn` date if she later unticks it. She can change it from her page. TS gets an email for each new review and reads them all under "Reviews" in the admin page. Nothing is published automatically: the sales page still has no reviews, and its proof section stays hidden until TS chooses real, permitted ones. Words in `copy/03-delivery.md` (PAGE: feedback).

## Header links, the reviews page and the desktop layout (built 2026-10-07)

- **Header.** Beside the main button: "Find My Song" (goes to `s/?find`, where a buyer types her email and her link is sent again) and "Reviews" (goes to `reviews/`). The Reviews link is in the page but hidden; a small script asks `reviews/?count=1` and shows it only when at least one review is public. TS asked for it to stay hidden until there are real reviews.
- **Reviews page** `site/prayer-song/reviews/index.php`. Shows a buyer's words, the name she chose and the month. Never stars, counts, her email, the order or the song. A review is public only if she ticked the permission box AND TS pressed "Show on the reviews page" on her order in the admin page. If she changes it, it comes down until it is read again; if she unticks permission, it comes down. With none, the page says so plainly and is marked noindex. The list is one file, `idx/public-reviews.json`, rebuilt by `ps_public_reviews_rebuild()`.
- **Do not hold back a permitted review because it is unfavourable.** The page says reviews appear "after we have read it"; that reading is for private details, abuse, or an outcome claim (which the no-outcome rule keeps off the funnel), never for sentiment. Refunded buyers' reviews are not excluded automatically for the same reason.
- **Desktop.** From 960px wide the sales page uses the full width: film beside the headline, steps and sample cards side by side, pictures five across, the form as a centred card. The phone layout is unchanged. Rules are at the end of `tools/landing-template.html`; each section carries `data-s="<name>"` for them.

## Legal pages (built 2026-10-06)

`site/prayer-song/terms.html` and `privacy.html`, built by `tools/build_legal.py` from `copy/05-legal.md`. The landing page and the form link to these, not to the site's bracelet terms. They state that the song is made with software including AI, name the services that receive the buyer's answers, and set out the free remake and the 30 day refund. Not reviewed by a lawyer.

## Day to day, on the server (command line; this host has no Terminal, so use the admin page)

| Command | What it does |
|---|---|
| `php worker.php --list` | Every order that is not finished |
| `php worker.php --show <token>` | One order: answers, lyrics, checks, log |
| `php worker.php --retry <token>` | Make the song again (add `--new-lyrics` for new words too) |
| `php worker.php --remake <token> "hwah-KEEN"` | A buyer says the name is sung wrong: sing this spelling, and deliver again |
| `php worker.php --approve <token>` | Release a song that failed the automatic check, after listening to it |
| `php doctor.php --live` | Is everything connected |

Alerts go to `admin_email`: a song held for review, a delivery email that failed, a song waiting more than 15 minutes, credits running low.

## Not verified yet

- Checked 2026-10-06: the host runs PHP 8.1 (cPanel, ea-php81), home folder /home/sanctoriastore, Cron Jobs is available with free schedule fields and no jobs set, no Terminal. Still open: that a one minute schedule is accepted on save, and how long a command line PHP job may run (a song takes about 30 seconds). The first real cron run settles both.
- That ClickBank returns `lid` in `vendorVariables`. If it does not, orders still match by email, and if that fails too the buyer's page asks for her answers.

## Send delay and express (built 2026-10-08, at TS's direction)
- A song is still made the minute the order is paid, so problems surface early, but it is not shown or emailed until **2 hours after the order** (`send_after`), or **1 hour** when the buyer added the order bump `express-1` "Express Song Delivery" (`send_after_express`, `express_items`). Until then the order has status `waiting`, her page says the song is being made, and audio and printables are refused.
- The words appear on her page from halfway through the wait. The worker (cron, every minute) releases what is due. A remake after delivery is not delayed again.
- Admin page: a waiting order shows its send time and a "Send now" button.
- Kit buyer tag `sanctoria-prayersong-1` (id 24391266) is applied when the ready email goes out; it is the default in `lib.php`, so the server's `config.php` needs no change.
- A name typed all in small letters or all in capitals is given normal capitals.

## Stripe switch (in progress, started 2026-10-16)
TS chose Stripe instead of ClickBank for this product only. Stripe account: Ignitist Pte Ltd (shared with the old astrology site; statement descriptor changed to SANCTORIA PRAYER by TS). The account's default API version is 2019-12-03, so every call pins `Stripe-Version: 2024-06-20`.
- Test mode objects: `prayer-song/stripe-test.json` (products, prices, two payment links: song $39, song + express $48.95). Live ones will go in `stripe-live.json`.
- Flow: form step 4 (express tick box) -> payment link with `client_reference_id=<lead id>` and `prefilled_email` -> Stripe -> `api/paid.php?session_id=` reads the session back with the secret key, makes the order, sends her to her song page. `api/stripe.php` (webhook, signature checked) makes the same order if she never comes back, and records refunds. Order receipt = the PaymentIntent id, item `prayersong-1`, so everything after payment is unchanged.
- The ClickMagick visitor id is read from a hidden `vtid=[cmc_vid]` link and stored on the lead and the order (`vid`), for attribution.
- Builder: ClickBank stays the default until go-live. `--stripe` builds the Stripe version; a live build refuses Stripe TEST links unless `--test-payments` is given. Delivery copy has STATEMENT (Stripe) and STATEMENT_CLICKBANK; the builder picks by payment mode.
- Legal pages: the Stripe versions are parked in `prayer-song/legal-stripe/`; the live ClickBank versions stay in `site/prayer-song/` until the switch (then run `tools/build_legal.py`).
- Server config still needs a `stripe` block: secret_key, webhook_secret, links (payment link id => song | express). Not placed yet.
- Open points from the copywriter: terms name US governing law but the seller is now a Singapore company (needs a decision); whether a refund includes the $9.95 express fee; express-specific wording on the making, thanks and delay pages.

### Live on Stripe (2026-10-17)
- TS said ship; the server config now holds the LIVE secret key and live webhook secret (`links` empty: no payment links are used live). Backups of the server config before each change are in `prayer-song/demo-data/server-config-before-*.php`.
- The checkout is the Pay step inside the form (PAYMENT = "embed", STRIPE_MODE = "live" are the builder defaults). `--clickbank` rebuilds the old ClickBank checkout; `--stripe-test` builds with test keys (a live build refuses that unless `--test-payments`).
- Live webhook: same address, events checkout.session.completed, checkout.session.async_payment_succeeded, payment_intent.succeeded, charge.refunded. Live payment method domain sanctoriastore.com active for Apple Pay and Google Pay.
- Terms (Singapore law, express fee refunded too) and privacy (Stripe) are live; the hidden test page was removed.
- ClickMagick: each Stripe sale is posted to `https://www.clkmg.com/api/s/post/?uid=92654&s1=<cmc visitor id>&amt=<dollars>&ref=sale` once per order (`cm_reported` on the order). ClickMagick's own Stripe integration only covers subscriptions. Refunds are not reported to ClickMagick (no documented refund postback found).
- Stripe buyers get both Kit tags at delivery: sanctoria-prayersong-1 and sanctoria-buyer.
- Not yet proven live: a real purchase and refund (TS to do one), and that ClickMagick forwards the ref=sale conversions to Meta.

### Unfinished order reminders in Kit (OFF since 2026-10-17 22:05 SGT; Drip sends them now)
- Someone who reaches the Pay step and does not pay gets up to three emails: 1 hour, 1 day, 3 days after. The worker sends each by adding her to a single-email Kit sequence (2932904, 2932905, 2932907) only while she still has no order; a newer form for the same email replaces the old one. Copy: `copy/07-abandoned-checkout.md`.
- Kit: tag `sanctoria-prayersong-lead` (24734384) marks who was reminded; field `prayer_song_resume_link` holds `https://sanctoriastore.com/prayer-song/?resume=<lead id>`, which reopens her saved answers at the Pay step (`api/resume.php`), or her song page if she has bought.
- On/off: `kit.abandon.since` in the server's config.php (0 = off). Only forms filled in after that time are reminded.

### Drip (from 2026-10-17)
- Drip account 4334334 "Sanctoria store". The token is only in the server's config.php (`drip.token`) and `.env` (DRIP_API_TOKEN).
- Every new lead (form reaches the Pay step) is copied to Drip with tag `prayer-song-lead` and fields prayer_song_for, prayer_song_intention, prayer_song_resume_link. Every Stripe buyer gets tag `prayer-song-buyer` and field prayer_song_link. Non-buyers = tag prayer-song-lead without prayer-song-buyer.
- Done by the worker each minute from marker files (idx/drip-lead-*, idx/drip-buyer-*); retried until Drip accepts, dropped after a day.
- Two workflows, both ON since 2026-10-17 22:05 SGT, emails A1 to B5 from `emails/drip/` (built by `tools/build_drip_emails.py` from `copy/08-drip-series.md`), From "Sanctoria" <admin@sanctoriastore.com>:
  - "Prayer Song: buyers follow-up" (138913844): tag prayer-song-buyer, A1 to A5 on days 1, 3, 7, 14, 30 at 2 pm UTC.
  - "Prayer Song: unfinished order follow-up" (616463631): tag prayer-song-lead, B1 after 1 hour (TS: keep it at 1 hour), B2 at 1 day, B3 to B5 on days 3, 7, 14 at 2 pm UTC. A Goal on tag prayer-song-buyer pulls a buyer out at any step.
- Kit reminders are OFF (kit.abandon.since = 0) so nobody gets two sets. Do not switch them back on while the Drip workflow runs.
- Proven live 2026-10-17 with two test leads: a lead reached Drip in about 15 seconds with every field, entered the workflow, and B1 rendered with the names and the resume link; a lead given the buyer tag exited at once.
- Leads from before 2026-10-17 were never copied to Drip; TS decided not to backfill them (only new people need to go through).
