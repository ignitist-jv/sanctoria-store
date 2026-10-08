# Sanctoria Prayer Song (working title)

Fifth Sanctoria offer, and the first digital one. Everything decided so far, in one place.
Last collated 2026-10-05. Status: **planning, nothing built or live. Blocked on the song render test.**

## Decisions locked

| Decision | Value | Set |
|---|---|---|
| Shape | `QUIZ` (survey form, not a chat) + `PERSONAL` | 2026-10-01 |
| Home | Under Sanctoria: sanctoriastore.com, this repo | 2026-10-05 |
| Checkout | ClickBank (karmacc), new digital items | 2026-10-01 |
| Front end price | $39 (was planned at $37) | 2026-10-06 |
| Persona | None. The brand speaks | 2026-10-01 |
| Reference funnel | prayersong.com, followed closely | 2026-10-01 |
| Music engine | ElevenLabs Music API (`music_v2_5`), Creator plan | 2026-10-01 |
| Order of work | Render test first, then bible, then copy | 2026-10-01 |

## The offer in one paragraph

A prayer, sung over the person you love, by name. The buyer tells us who it is for and what they are
praying for, and receives a radio quality song with that person's name and that prayer in the
lyrics, on their own private page, within 24 hours (usually minutes). prayersong.com sells the same
idea as a sentimental gift with a 7 day wait; ours is a prayer, delivered the same day, automated.

## The funnel (TS's brief, 2026-10-01)

    Ad
     → Landing page: the pitch, what they get, the bonuses          (like prayersong.com home)
     → Chat box: who is the song for, their name, what is it for    (like prayersong.com /create, as a chat)
     → Opt in: where to send your personalized prayer song
     → Checkout (ClickBank, $39) → upsells
     → Private song page + "your song is ready" email

Keep the questions few. Detail in PRODUCT-FLOW.md (written before the chat brief: its 7 step quiz is
superseded by the short chat above; the price ladder, tokens and back end still stand as drafts).

## What Sanctoria already gives us

| Need | Already here |
|---|---|
| Brand, domain, design system | Sanctoria, sanctoriastore.com, cream and bronze, Fraunces + Inter (see ../CLAUDE.md) |
| Chat funnel | `site/chat/` (Find Your Devotion) and `site/ins/lead.php` posting leads to Kit. Template for our chat box |
| ClickBank to Kit buyer sync | `site/ins/clickbank.php`, add the new items to its config |
| Hosting and deploy | LiquidWeb, `deploy/deploy.sh` over FTPS. PHP runs on the host |
| Tracking | ClickMagick tracker and `vtid=[cmc_vid]` on checkout links. Meta is CAPI only, no browser pixel |
| Legal pages, support email | privacy, terms, contact, support@sanctoriastore.com |
| Ads | Sanctoria ad account 462874384767571, naming convention with format code |
| Audience and learnings | Catholic women 45+, ../LEARNINGS.md, the peace and protection angle policy |
| Bonus material | `../bonuses/` (prayer card, novena, devotional) as candidates |

## What changes because it is Sanctoria

- **Catholic audience.** Scripture from a Catholic public domain translation (Douay-Rheims), not KJV.
  Styles should include traditional hymn and Marian. Saints can be invoked (Saint Benedict, Our Lady).
  The three test songs were written before this decision and use KJV; fine for testing the sound.
- **Angle policy applies.** Peace, protection, blessing, grace. None of the banned vocabulary.
- **Buyers already exist.** Bracelet, necklace and rosary buyers in Kit are a warm list for launch.
- **Digital product on a physical goods account.** New ClickBank items need digital delivery set, and
  the 24 hour delivery rule applies (see below).
- **No fabricated proof**, same as every Sanctoria page: no reviews until real ones exist.

## Facts checked

- **Higgsfield cannot make the songs** (speech only; its music model is locked to its game builder).
- **ElevenLabs Music:** $0.15 per minute of audio, 900 credits per minute, 5 concurrent on Creator,
  commercial use from Starter up. A 2.5 minute song is about $0.40 a render, $1 to $1.50 with retries.
- **Plan:** Creator ($11 first month, then $22, 121k credits, about 35 songs, can buy more). Pro at ~30 sales a month.
- **ClickBank policy:** digital delivery within 24 hours required; AI rule only bans likeness and
  voice clones; professional services banned, personalised products not mentioned. Low risk, final
  word is their product review. prayersong.com's 7 day delivery would not pass; ours does.
- **Competitor:** prayersong.com: 5 step survey, price hidden until the end, 7 day delivery, $59 rush
  upsell, 30 day refund, discloses AI assisted production.

## Files

| File | What |
|---|---|
| PRODUCT-FLOW.md | Full flow draft: pages, price ladder, tokens, back end, unit economics |
| DELIVERY-PLAN.md | How each buyer gets their own song: private page, email, find my song, failure paths |
| CHECKLIST.md | The playbook checklist for QUIZ + PERSONAL, with phase 0 on top |
| tools/song_test.py | Renders the test songs, transcribes them, scores name and lyric accuracy |
| tools/test_songs.json | Three test songs with hard names: Siobhan, Nevaeh, Joaquin |

Site pages will live in `../site/prayer-song/` when phase 3 starts. Buyer data never goes in git.

## Draft, not yet agreed

- Price ladder: bump $9 keepsake print; upsell 1 $47 thirty days of sung prayer; upsell 2 $37 a
  second song; upsell 3 $27 lyric video. Each with a downsell.
- Bonuses on the landing page.
- (decided 2026-10-06) Product name: Your Prayer Song.

## Open, in order

1. **ElevenLabs key** into `sanctoria-store/.env` as `ELEVENLABS_API_KEY=`, then run the test:
   `python3 prayer-song/tools/song_test.py`
2. **TS listens** to the three songs: good enough to sell, yes or no.
3. Product name, bonuses, price ladder.
4. A Claude API key for writing lyrics per buyer.
5. Confirm the LiquidWeb host allows a scheduled job every minute and long enough run time.
6. Then phase 1: PRODUCT-BIBLE.md. Then copy by /ai-copywriter, starting with the landing page and the chat.
