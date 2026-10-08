# Personalized Prayer Song: Product Flow

Shape: `QUIZ` + `PERSONAL`
Drafted 2026-10-01. Working document. **Read README.md first: it holds the locked decisions. The 7 step quiz below is superseded by the short chat box flow, and the offer now lives under Sanctoria.** Decisions marked **OPEN** need TS before the bible is locked.

Reference competitor: prayersong.com (survey funnel, 7 day human assisted delivery, $59 rush upsell,
30 day refund). Our edge: a sung prayer, not a gift song, delivered within 24 hours, fully automated.

---

## 0. The flow on one screen

```
Meta ad (a real sample song playing, name on screen in the lyrics)
  │
  ▼
[1] Lander: hook + sample player + "Start your prayer song"
  │
  ▼
[2] Quiz, 7 steps (answers saved after every step)
  │
  ▼
[3] "Writing your prayer song..." (Claude writes the preview lyrics, 10 to 20 sec)
  │
  ▼
[4] Preview page: their title, verse 1 and chorus with the name, rest redacted
  │    + a sample in the style they picked
  ▼
[5] Sales section → ClickBank checkout (+ order bump)
  │
  ├──► INS "SALE" ──► render pipeline (section 4) ──► song ready email
  ▼
[6] Upsell 1 -- decline --► Downsell 1
  ▼
[7] Upsell 2 -- decline --► Downsell 2
  ▼
[8] Upsell 3 -- decline --► Downsell 3
  ▼
[9] Thank you / "My Prayer Songs" hub: live status, then players for everything bought
```

Non buyers leave at [4] or [5] with their email captured and drop into the non buyer sequence.

---

## 1. Front end

### [1] Lander
- One screen: headline, a 30 to 60 sec sample song with lyrics scrolling, one button.
- Occasion chips under it (Healing, Protection, Grief, Marriage, Children, Breakthrough) that
  start the quiz with step 3 prefilled.
- Trust strip: guarantee, delivery window, "made for faithful families". No reviews until real ones exist.

### [2] Quiz (7 steps, progress bar, one question per screen on mobile)

| # | Question | Field | Notes |
|---|---|---|---|
| 1 | Who is this prayer song for? | `relationship` | Wife, Husband, Son, Daughter, Grandchild, Mother, Father, Friend, Myself, Someone in heaven |
| 2 | Their first name, and how to say it | `name`, `name_phonetic` | Phonetic optional but encouraged ("Alicia: ah-lee-sha"). Skipped if Myself |
| 3 | What are you praying for? | `intention[]` | Pick up to 2: Healing, Protection, Strength, Peace, Breakthrough, Provision, Marriage, Grief, Salvation, Gratitude |
| 4 | Tell us about them | `story_quality`, `story_memory`, `story_hope` | 3 short boxes, each skippable: one word that describes them, one memory, one thing you hope for them |
| 5 | A verse to build it on | `verse` | Dropdown filtered by intention, or "Choose one for me" |
| 6 | The sound | `style`, `voice` | Hymn, Gospel, Acoustic Worship, Country Gospel, Lullaby. Female, Male, Duet. 10 sec sample on each tile |
| 7 | Where should we send it? | `email`, `buyer_name` | Buyer's own first name used for the "from" line |

Answers post to our server after each step (so a drop at step 6 still gives us a partial lead),
and the email posts to Kit at step 7 with custom fields created first.

### [3] Writing screen
- Animated "your prayer song is being written" while Claude generates the preview. Real work, not a fake timer.

### [4] Preview page (the free payoff)
- Song title with their name, verse 1 and chorus in full, name highlighted, bridge and final verse
  redacted. A sample in their chosen style plays beside it.
- Lyrics only, no free audio: a sung preview would cost about $0.30 to $1 per lead, buyer or not.
- Ends on the button to hear it sung.

### [5] Sales section and checkout
- Opens on the lyrics they just read, then the offer, then the guarantee.
- ClickBank checkout. The lead id rides through the checkout link so the sale matches the quiz answers.
- **Order bump:** Keepsake lyric print, a framed style printable PDF of their lyrics. Costs nothing to render.

---

## 2. Price ladder (draft, OPEN)

| Step | Product | Price | Downsell | Built from data held? | Render cost |
|---|---|---|---|---|---|
| Front end | Their Prayer Song (close to 4 min, MP3 + private player) | $37 | | yes | ~$1 to $1.50 |
| Bump | Keepsake lyric print (PDF) | $9 | | yes | ~$0 |
| Upsell 1 | 30 Days of Sung Prayer: a 60 sec sung prayer over the same person every morning for 30 days, each on a different verse | $47 | $37 | yes | ~$5 to $7 |
| Upsell 2 | A prayer song for one more loved one | $37 | $27 | one short form after the click (name, relationship, intention). The only step that asks anything new | ~$1 to $1.50 |
| Upsell 3 | Lyric video of their song, scripture scenery, ready to share on Facebook | $27 | $17 | yes (optional photo upload later) | ~$0, rendered with ffmpeg |

Why this order: upsell 1 deepens the same prayer over the same person, upsell 2 extends it to the
family, upsell 3 is a new format of something they already own. No two steps repeat.
Same guarantee on every step. Copy says "within 24 hours", and most arrive in minutes.

Upsell 1 is delivered as a daily Kit email with that day's song, which doubles as the buyer engagement series.

---

## 3. Personalisation tokens

**Collected:** relationship, name, name_phonetic, intention (up to 2), story_quality, story_memory,
story_hope, verse, style, voice, buyer_name, email.

**Derived:** pronouns (from relationship), song title, verse when "choose for me", tempo and key
(from style), the prayer arc (from intention), memorial mode (when "Someone in heaven").

**Never asked:** surnames, date of birth, address, diagnosis or medical details, money amounts.

---

## 4. The automated back end

```
ClickBank INS (SALE, per item)
  │  reuse the Eastern Star clickbank-ins.php, new item map
  ▼
Order record (lead id → quiz answers)  ──► Kit tags: buyer + one per item
  ▼
Job queue (one job per product bought)
  ▼  cron worker, every minute
[a] Claude writes full lyrics from the layered template + answers
[b] Claude safety check on inputs and lyrics ──fail──► review list
[c] ElevenLabs Music renders (lyrics + style + voice)
[d] Speech to text check: name sung? lyrics intact? ──fail──► retry, max 3 ──► review list
[e] Store MP3 behind an unguessable key
[f] Kit: set the song link field, apply the "song ready" tag → delivery email fires
  ▼
Daily summary to TS: orders, delivered, stuck, refunds
```

- **Hosting:** the same cPanel setup as Eastern Star. PHP endpoint for INS, PHP cron worker for jobs.
  No new server needed. The speech to text check uses ElevenLabs STT so it can run on the host.
- **Refund INS:** tag the refund, keep the link alive (no clawback drama).
- **Review list:** a private page where TS sees stuck jobs and can re-render or edit a lyric line. Target under 3%.
- **Concurrency:** jobs wait in line if ElevenLabs rate limits; the 24 hour promise has huge slack.

### Lyric template (write once, render many)
1. **Spine** per intention: address to God, name the person, the petition, the verse, the blessing, amen.
2. **Branch** per relationship: how the singer speaks of them (my wife, our boy, Mama in heaven).
3. **Slots** filled from the story answers.
4. Rules: the name sung in every chorus, at least 3 times; no promise of healing or money; no
   dashes; scripture quoted only from a public domain translation (KJV or WEB).

---

## 5. Emails (Kit)

| Sequence | Trigger | Content |
|---|---|---|
| Non buyer | quiz email, no buyer tag | 5 to 7 emails over 10 days, each reminding them their lyrics are written and waiting |
| Song ready | song ready tag | the player link, how to share it, the keepsake print if bought |
| 30 Days | upsell 1 tag | one sung prayer a day for 30 days |
| Buyer engagement | buyer tag | day 3 "who else needs a prayer song" (upsell 2 link), day 7 feedback request (real testimonials) |

**Share loop:** every song player page has "Make a prayer song for someone you love", which starts the quiz.
Shared songs are free traffic.

---

## 6. Unit economics at the draft prices (per 100 front end buyers)

| Item | Assumed take rate | Revenue | Render cost |
|---|---|---|---|
| Front end $37 | 100% | $3,700 | ~$150 |
| Bump $9 | 30% | $270 | $0 |
| Upsell 1 $47 | 20% | $940 | ~$120 |
| Upsell 2 $37 | 15% | $555 | ~$20 |
| Upsell 3 $27 | 15% | $405 | $0 |

Render cost stays under 5% of revenue. Ad cost is the real number, decided in phase 10.
Take rates are placeholders, not data.

---

## 7. Open decisions for TS

1. **Checkout:** ClickBank (assumed above: reuses INS, Kit tagging, affiliates) or Stripe. Also confirm
   ClickBank accepts an AI generated personalised product delivered within 24 hours.
2. **Prices:** front end $37 vs $47, and the ladder above.
3. **Brand and domain:** prayersong.com is taken. Name to be chosen.
4. **Persona:** none (like Wealth Ancestry), or a named worship leader or songwriting team.
5. **Disclosure line:** where we say the songs are made with AI assisted music production (FAQ and terms).
6. **The 3 song test** on ElevenLabs before any copy is written.
