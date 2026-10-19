# Prayer Song, ad batch 1: copy
Date: 2026-10-08. Visual brief: `prayer-song/creative/ad-batch-1-prompts.md`

Copy is held CONSTANT across all seven ads. The creative is the only variable,
matching how the market leader runs (about 1,000 active US ads, one headline and
one body across every one of them).

## Ship this

**Primary text** (107 chars, one paragraph, no line breaks, no emoji, renders
with no "See more" link):

    A spoken prayer is said once. A sung one gets played again. Have a loved one's name set into a prayer song.

**Headline** (28 chars): `Their Name, Sung As A Prayer`
**Link description** (36 chars): `$39, one time. Sent within 24 hours.`
**CTA:** Shop Now

Nothing here depends on a discount, a percentage, a deadline, a review, a count
or an outcome, so it survives the pricing-anchor decision either way.

### Alternates, not for this batch
1. `An original prayer song, sung by name, built on a verse of Scripture. Sent within 24 hours. $39, one time.` / `A Prayer Song, Sung By Name`
2. `Some names have been prayed for years. A prayer song sets one down, so it can be played and prayed again.` / `Their Name In Every Chorus`

## Format 1, LyricPlayer (VID)

Hook, max 2 lines:

    A prayer song for a son.
    His name is in the chorus.

Offer panel, version A, ships today:

| Slot | Text |
|---|---|
| Eyebrow | THIRTY DAYS TO DECIDE |
| Main | Every cent back if it is not right. |
| Support | One email is all it takes. No questions. |
| CTA bar | Begin My Prayer Song |

Version B swaps the support line to `And the song stays on its page, to keep.`
BLOCKED pending a written policy decision: after a ClickBank refund, does the
token page at /s/?k= keep serving and the MP3 keep downloading, as policy rather
than because nobody revokes it. Default to A.

## Format 2, QuietDevotionSung (UGC)

Hook bars, about 38 chars a line, three scenes that read as one argument (the
same song in three places in one day):

    01_BeforeTheHouseWakes
    Up first. Kettle on. House dark.
    One earbud in, a prayer song on.
    A grandchild's name sung in it.

    02_SchoolCarPark
    Parked early at the school gates.
    Engine off. The same song again.
    Her name is in every chorus.

    03_BedsideLamp
    Last thing at night, lamp still on.
    A prayer song playing low.
    The name in it, prayed once more.

Mandatory two line disclosure, burned in:

    An illustration made by Sanctoria. Not a customer.
    A sample prayer song. Not a customer's song.

### Lyric caption rules
The audio is the product speaking; burned-in text is the advertiser speaking.
A sung line and the same line in 56px type are not the same claim.

1. Verbatim from a verified transcript. No paraphrase, no ellipses.
2. No quotation marks, ever. Quote marks make a lyric card read as a testimonial.
3. One lyric line per card, two only if the sense breaks across them.
4. The name in amber #F2C230 so it reads as the variable, not part of the hymn.
5. The name card is the name alone, 96px, 1.2s, no punctuation.
6. Cover test: read the card alone. If it asserts something will happen, or that
   anything is protected, healed, kept or promised, it is cut. Audio may keep it.
7. Never run a card whose "you" has no antecedent unless the name is on that card
   or the one immediately before it.

CUT from cards, audio only: The Lord will light your way / Angels watching over
you / Keeping you in all your ways / You are covered by the Son / For He shall
give His angels charge over thee / To keep thee in all thy ways / He will hold
you all your days.

## Format 3, TheNameGoesIn (SCR)

Setup:

    This is the box the name goes in.
    Wait for what comes out of it.

Payoff band, entering at 0:12 with the chorus, Daniel only:

| Time | Card |
|---|---|
| 0:12 to 0:16 | Lead Daniel home, Lord, lead him home |
| 0:16 to 0:22 | Daniel, You have called him by his name |
| 0:22 to 0:30 | I'm not asking for a miracle by morning |
| 0:30 to 0:35 | For Daniel, amen |

That third card is the most valuable line in the batch: the product's own lyric
disclaims the outcome, in the customer's voice, inside the thing being sold.

## First money

`01_BeforeTheHouseWakes`, 40% of batch budget. It is the only ad running a
mechanism this account has already paid for: AQuietDevotion is the one
consistently above-line family, the BeforeTheHouseWakes refresh ran 2.83x on
14d/28d, and the angle returned 2.74x when ported from bracelet to rosary, which
is direct evidence it travels across products here.

Counter-signal, which must be logged: on this account the UGC FORMAT is what
keeps dying while PHOTO wins the same angle. The AQuietDevotion_UGC trio died
together on about $147; the survivor was AQuietDevotion_PHOTO_Quiet.

Insurance, recommended: add a fourth leg, one clean PHOTO static of the scene A
still with NO burned-in text, same primary text and headline. Every format in
this batch bakes text into the frame; every proven winner in this account is a
clean photograph with no overlay.

## Naming

| Format | Campaign | Ad Set | Ads |
|---|---|---|---|
| 1 VID | SungKeepsBeingPrayed_VID_2026-10-08 | T1_MF_45-65+_SungKeepsBeingPrayed_VID_LyricPlayer | 01_LyricPlayerLong, 02_LyricPlayerShort |
| 2 UGC | QuietDevotionSung_UGC_2026-10-08 | T1_MF_45-65+_QuietDevotionSung_UGC_BeforeTheHouseWakes | 01_BeforeTheHouseWakes, 02_SchoolCarPark, 03_BedsideLamp |
| 3 SCR | TheNameGoesIn_SCR_2026-10-08 | T1_MF_45-65+_TheNameGoesIn_SCR_NameTyped | 01_NameTyped, 02_NameTypedStatic |
| 4 PHOTO | QuietDevotionSung_PHOTO_2026-10-08 | T1_MF_45-65+_QuietDevotionSung_PHOTO_WakesNoText | 01_WakesNoText |

SCR is a new format code to add to the convention in CLAUDE.md.

## Blockers and flags

1. CHECKOUT. No ClickBank item and no cron on /prayer-song/. Ads can be built
   paused but nothing can be bought. This gates launch, not the build.
2. PRICING ANCHOR. The live page carries "70% off today" and a struck "$129".
   PRODUCT-BIBLE.md line 14 says "Anchor: None invented ... No 'was' price" and
   line 104 says "No invented urgency". The page contradicts its own bible. No ad
   copy above depends on it either way.
3. DEMO SONGS ARE KJV. All three test songs are tagged KJV (Jeremiah 30:17,
   Psalm 91:11, Revelation 21:4) while the page promises Douay-Rheims in seven
   places. The LIVE generator is correct: api/lyrics.php carries a hardcoded
   Douay-Rheims table from drbo.org and instructs exact wording. So production is
   fine and only the old demos are KJV, as the README already records. The
   consequence for ads: any caption quoting Nevaeh or Siobhan quotes KJV. Caption
   Daniel only (Luke 15:20, Douay-Rheims), or regenerate the demos first.
4. SIOBHAN EXCLUDED from all ads. Verified lyrics contain "You said You would
   restore her health", "Heal her body, ease her pain", "Give the doctors steady
   hands". Health claims.
5. "AND YOU KEEP IT" needs the written policy decision above before Panel B runs.
6. BATCH 2 UNLOCK. One line in the delivery email asking for a phone clip plus a
   written release. About twenty buyers unlocks the real-reaction format this
   batch cannot run, and fills the proof block the page deliberately holds empty.

Build rules: campaign PAUSED, ad set and ads ACTIVE underneath, $5/day,
start_time 2026-10-10T03:00:00+08:00, mandatory url_tags on every creative.
Break-even is near 1.1x reported ROAS on this offer, not the bracelet's 1.2x,
because contribution is about $35 on a $39 digital sale.
