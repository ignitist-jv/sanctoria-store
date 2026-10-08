# Delivery Plan: how each buyer gets their own song

Drafted 2026-10-03. Not built yet. Depends on the render test passing first.

## The principle

Every order gets one private page of its own, at an unguessable link:

    https://<domain>/s/<22 character key>/

That page is the product. Everything else (the thank you page, the email, the lookup page) is just a
way of getting the buyer to their link. Same idea as the Eastern Star `/d/<key>/` folders, but made
by the server the moment the sale comes in, instead of by hand.

## Three ways the buyer reaches it

1. **Straight after paying.** ClickBank sends them to their private page. It shows their full written
   lyrics at once and a "your prayer song is being sung" status. The page checks every few seconds
   and turns into the player when the song is ready, usually in 2 to 5 minutes.
2. **By email.** When the song passes its checks, Kit sends "Your prayer song for [name] is ready"
   with their own link. Works by setting three custom fields on the subscriber (`song_url`,
   `song_title`, `recipient_name`) and then adding a "song ready" tag that triggers the email.
3. **Find my song.** A page where they type their email and we send the link again. The link is
   emailed, never shown on screen, so nobody can look up someone else's song.

## What is on the private page

- The player, the download button (MP3), the full lyrics
- Share buttons (Facebook, WhatsApp, copy link) and "make one for someone you love"
- The bonuses, and anything else they bought (keepsake print, 30 days, second song, lyric video)

## How one order becomes one song

| Step | What happens |
|---|---|
| 1 | Chat questions answered on the landing page. Saved on our server under a lead id |
| 2 | Checkout link carries the lead id to ClickBank |
| 3 | Buyer pays. ClickBank notifies our server with the receipt, email, items and the lead id |
| 4 | Server creates the order: receipt, lead id, a new private key, status "queued". Tags the buyer in Kit |
| 5 | Worker (runs every minute) picks it up: lyrics, safety check, render, name check |
| 6 | MP3 saved into the buyer's private folder. Status "ready" |
| 7 | Kit fields set and "song ready" tag added. Email goes out |

**Matching the answers to the sale:** lead id first, buyer email second. If neither matches (they paid
with a different email, or came through an affiliate link straight to checkout), their private page
asks the questions there and the song is made as soon as they answer. No order is ever left with
nothing to make.

## Timing and the 24 hour promise

| When | Event |
|---|---|
| 0 min | Paid. Private page shows the lyrics and the status |
| 2 to 5 min | Song ready on the page, email sent |
| 15 min, not ready | Buyer gets a short "we are giving it one more pass" email. TS gets an alert |
| 3 failed renders | Order moves to the review page. TS alerted at once |
| 12 hours, still open | Second alert, marked urgent |
| 24 hours | ClickBank's limit. Nothing should ever get this far |

## When something goes wrong

- **Render or name check fails:** automatic retry, up to 3, switching to the phonetic spelling on retry 2.
- **Still failing:** review page. TS can listen, re-render, edit a lyric line, or approve as is.
- **Email bounces or lands in spam:** the page link from the thank you step still works, and "find my song" resends.
- **ElevenLabs is down or rate limited:** jobs wait in the queue and run when it is back.
- **Refund:** tagged in Kit. The link stays alive.

## Where it runs

Same cPanel hosting as Eastern Star. A PHP endpoint receives ClickBank's notification (copied from
Eastern Star), and a scheduled job does the rendering. Each song is about 3 to 4 MB, so 1,000 songs
is about 4 GB.

**To confirm on the host before promising anything:** scheduled jobs can run every minute, a job
can run for 3 to 5 minutes without being cut off, and there is enough disk space. If any of those
fail, the rendering moves to a small separate server and the rest stays the same.

## Privacy

- Order records hold names, emails and personal stories. They live outside the public web folder and
  are never uploaded by the deploy script.
- The key is the only thing protecting a song page, so it is long and random.
- Keys and credentials stay in `.env` and the config file, never printed.

## Build order

1. Render test passes and TS approves the sound.
2. One command locally: answers in, finished song page out.
3. Move it to the server behind the ClickBank notification.
4. Kit fields, tags and the delivery email (copy by /ai-copywriter).
5. A real test purchase: pay, receive, refund. Then a second with a deliberately broken name to see the failure path.

---

## Built 2026-10-05 (practice mode only, nothing deployed)

Code lives in `site/prayer-song/api/` and `site/prayer-song/s/`. Tested by
`python3 prayer-song/tools/test_delivery.py` (31 checks, all passing).

| File | Job |
|---|---|
| `api/lib.php` | Tokens, storage, order creation by receipt, ClickBank decrypt and proof of purchase |
| `api/lead.php` | Saves the survey answers under a lead id (`lid`) before checkout |
| `api/ins.php` | ClickBank notification: creates the order. A NEW, separate INS URL; `/ins/clickbank.php` is untouched |
| `api/thanks.php` | ClickBank Thank You URL: proves the purchase (`cbpop`), sends her to her song page |
| `api/worker.php` | Cron, every minute: lyrics, render, check, save, email. Command line only |
| `api/pipeline.php` | The steps the worker runs, and the email providers |
| `api/status.php`, `api/audio.php` | Page polling, and play / download by token |
| `s/index.php` | The private song page: `/prayer-song/s/?k=<token>` |
| `api/config.sample.php` | Copy to `config.php` on the server (gitignored, denied over HTTP) |

**The token.** 128 random bits, made when the order is created. It names the order record, the MP3
and the page. One receipt always maps to one token, however many times ClickBank repeats itself.

**Still to do before a real sale:**
1. Real lyric writer. `ps_write_lyrics()` is a placeholder lyric for testing, not the product.
2. ElevenLabs key in `api/config.php`, and the render test passed.
3. Email provider account (Resend or Postmark), key in config, and the sending domain verified in DNS.
4. ClickBank: create item `prayersong-1`, set its Thank You URL to `/prayer-song/api/thanks.php`,
   add `/prayer-song/api/ins.php` as an INS URL, confirm `lid` comes back in `vendorVariables`.
5. On the host: confirm cron every minute, command line run time, and that the data folder lands outside the web root.
6. Confirm on the live server that `api/lib.php`, `api/config.php` and the data folder return 403.
7. The three bonus printables, a review page for stuck songs, and "find my song" (resend the link).
8. A real test purchase and refund.
