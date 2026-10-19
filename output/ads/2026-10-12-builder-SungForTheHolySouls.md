# SungForTheHolySouls, 3 static photo ads

Built by the ad builder on 2026-10-12 from `AD_BRIEF.md` item 1. **REHEARSAL RUN: no images were
generated and nothing was created in Ads Manager.** This file is the copy of record if TS wants it
built for real.

Offer: Your Prayer Song, $39 one time, digital, `https://sanctoriastore.com/prayer-song/`.
Format: static PHOTO, not UGC. Angle: `SungForTheHolySouls`.

## Why this angle

Every November the parish writes the names of the dead in a book and reads them aloud at Mass.
This is the same act she already performs, except the name is sung, and it is hers to keep and
replay rather than read once and closed. The dominant emotion is grief and the consolation of
having done something for someone she can no longer do anything for, which is a different emotion
from every ad currently live in the account (all three run on maternal worry about a living child).

The occasion is fixed and 21 days out: All Souls Day is Monday 2026-11-02, the whole of November is
the Church's month of the Holy Souls, and the cemetery indulgence window runs 2026-11-01 to 11-08.
`NovemberNames` is the one seasonal angle LEARNINGS records above the line (1.91x on $17.28). The
product mechanically supports this: the landing form's "who it is for" options include "someone who
has passed" and its intention options include "comfort in grief".

PHOTO was chosen on the account's own evidence. The highest-ROAS ad in account history is
`01_QuietMansFaith` at 3.63x in PHOTO, and the overwhelming majority of the 22 dead executions are
UGC. The 3.63x is 1 sale on 29 outbound clicks, so it is a lead, not a proven finding.

## Naming

| Level | Name |
|---|---|
| Campaign | `SungForTheHolySouls_2026-10-12` |
| Ad Set | `T1_MF_35-65+_SungForTheHolySouls` |
| Ad 01 | `01_TheBookAtTheBack` |
| Ad 02 | `02_TheWalkBackToTheCar` |
| Ad 03 | `03_AThinThingToLeaveAChild` |

Note for TS: the run instruction for this builder specified the campaign name as
`<AngleName>_<date>` and the ad set as `<CountryTier>_<Gender>_<AgeRange>_<AngleName>`, with no
format code. The project convention in `CLAUDE.md` adds a format segment
(`SungForTheHolySouls_PHOTO_2026-10-12`). The run instruction was followed. If you want the format
code back for traceability, say so and it is a one line change.

## Ad set config, cloned from the live Prayer Song reference

Reference ad: `01_SonOpen_v2` `120256732898630051`, ad set `T1_MF_35-65+_SungByName_UGC_SonOpen`
`120256729273120051`, campaign `SungByName_UGC_2026-10-10`. Same offer, same page, same pixel, so
it is the right thing to clone. Read only, nothing about it was touched.

| Setting | Value |
|---|---|
| Objective | OUTCOME_SALES |
| Optimisation | OFFSITE_CONVERSIONS, PURCHASE |
| Pixel / dataset | `1162659081276679` (Sanctoria Store, CAPI only) |
| Billing | IMPRESSIONS, highest volume |
| Budget | $5.00/day (`daily_budget=500`) |
| Targeting | US, GB, CA, AU, NZ. All genders. Age 35 to 65+ |
| Page | `292317240635888` |
| Destination | `https://sanctoriastore.com/prayer-song/` |
| CTA | SEE_DETAILS |
| Link description | `$39, one time. Sent within 24 hours.` |
| Start time | `2026-10-14T03:00:00+08:00` (creation plus 2 days, 03:00 SGT) |
| Campaign status | PAUSED, and it stays paused. TS turns it on |

Mandatory `url_tags` on every ad:

```
utm_source={{site_source_name}}&utm_medium={{placement}}&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&cmc_adid=fb_{{ad.id}}
```

---

## 01 · `01_TheBookAtTheBack`

**Headline:** Four minutes, not four seconds

**Primary text:**

```
Every November there is a book open on a table at the back of our church.

People write the names of their dead in it, and the priest reads them out at Mass.

I have written the same two names in that book for nine years. It takes about four seconds for them to go by.

Four seconds never feels like much for a whole person.

So we make something longer. One original song, close to four minutes, with a first name sung in every chorus.

The book closes at the end of the month. This one does not.

$39, one time. Sent within 24 hours. 30 day full refund.
```

**Visual: `TheNamesReadAloud`.** Overlay YES. Headline on a bottom scrim, centered:
"In November, the names are read aloud." Gold CTA pill: "See How It Works". Small SANCTORIA
wordmark top left.

**Image prompt:**

> Photographic documentary realism, square 1:1, 1080x1080. Subject: a Catholic woman in her late fifties standing in the fourth pew of a small ordinary parish church during a November remembrance Mass, winter coat still on over a plain knit, head inclined slightly forward, eyes lowered, entirely still, listening as names are read from a lectern far ahead of her. Both of her hands are lowered in front of her and a single small folded slip of cream paper is held between the fingers of one hand, the writing on it soft and not legible. Around her, six or seven other parishioners stand in the same and neighbouring pews, rendered as backs, shoulders and coat collars only, soft and out of focus, coats folded over the pale oak pew backs. Deep in the background, very soft and unidentifiable, a lay reader stands at a simple wooden lectern, the open book on it indistinct with no readable text. Setting: a modest parish interior with chalk white plaster and pale limestone, clear glazed windows rather than coloured glass, bare November branches visible through them, a plaster statue in a far niche fully out of focus. Lighting: flat cool overcast daylight entering high from camera left, soft and even across the nave, with one weak low shaft of November sun crossing the air behind her and warming the dust, highlights protected on her cheek, no candlelight, no chiaroscuro, no pools of warm glow. Camera: 35mm lens at f2.8, chest height, slight three quarter angle from the pew directly behind her so the viewer reads her cheek and jaw in near profile with the nave receding ahead, subject placed in the right third, focus on her face and the folded slip, the congregation and nave falling off into gentle softness, mild foreground pew edge blur. Palette: cool grey blue daylight, chalk white and pale limestone, warm oatmeal and bronze 9A7B4F in her coat and scarf, cream F7F3EC highlights, muted olive and charcoal in the coats around her. Styling and wardrobe: navy wool coat, soft bronze wool scarf, modest and completely unstyled, grey hair pinned back, reading glasses pushed up on her head, no jewellery except a plain worn wedding band, no makeup finish. Era: contemporary, 2020s, northern hemisphere late autumn. Mood: reverent, quiet, warm and consoled, grief held steadily and not performed, never bleak, never theatrical. Deliberately absent from frame: no candles, votives, candle racks or tapers of any kind; no rosary, bracelet, medal, necklace, triptych or any devotional object; no handwritten list of names, no family tree, no ledger or book turned toward camera; no stained glass colour; no legible parish name, surname, signage, noticeboard or screen; no brand marks; no face turned to camera; no tears. Photographic realism cues: true skin texture with fine lines and open pores, visible wool fibre and coat nap, natural colour with no grade, full frame digital capture around ISO 800, faint organic grain, mild lens vignette, no HDR, no beauty retouching, no studio lighting, no stock photo expression, editorial documentary frame. Overlay: bottom 38 percent linear gradient scrim from transparent to 14110F at 82 percent opacity, headline in Fraunces semibold cream F7F3EC centered reading "In November, the names are read aloud.", below it a gold F2C230 pill button with dark 14110F Inter semibold label "See How It Works", and a small cream SANCTORIA wordmark top left in letterspaced Inter caps at 70 percent opacity.

**Distinct because:** the only execution built on the parish book itself, and its tension is
duration, four seconds read aloud at Mass against four minutes she keeps. The dead
`02_NovemberNames` ran on losing her place in a long list at home, which is a different idea.

---

## 02 · `02_TheWalkBackToTheCar`

**Headline:** Something to play on the drive home

**Primary text:**

```
The first week of November I drive up to the cemetery.

I bring flowers the wind takes by the weekend. I say a decade. I stand there a while not knowing what to do with my hands.

Then I walk back to the car, and on the drive home I would rather have something to play than the radio.

So that is what we make. One original song, close to four minutes, with a first name sung in every chorus, and the verse of scripture it is built on.

Nothing to tidy away afterwards, and nothing the wind can take.

$39, one time. Sent within 24 hours. 30 day full refund.
```

**Visual: `OneEarbudAtTheGraves`.** Overlay YES. Headline on a bottom scrim, centered:
"November is the month of the Holy Souls." Gold CTA pill: "Hear A Sample". Small SANCTORIA
wordmark top left.

**Image prompt:**

> Photographic documentary realism, square 1:1, 1080x1080. Subject: a woman in her early sixties standing on the grass verge of an ordinary parish cemetery on an overcast November afternoon, coat buttoned against the cold, a single plain beige earbud in her right ear with its thin pale cable running down into her coat pocket, her other hand holding a small unbranded dark phone low and forgotten at her hip with the screen dark and completely unreadable. Her chin is lifted very slightly, eyes closed, mouth relaxed into the faintest consoled half smile, shoulders dropped, breath just visible in the cold air. She is listening and nothing else is happening. Setting: three or four weathered grey headstones in the near and middle distance, deliberately soft and wholly illegible with no readable names, dates, surnames or portrait plaques, a low iron railing, a wet gravel path, bare lime and beech trees with the last rust leaves, soaked fallen leaves on clipped grass, and a small plain bunch of white chrysanthemums laid at the base of the nearest stone. Lighting: broad soft overcast daylight as the ambient, with one thin break of low sun arriving from behind the trees at camera left to rake a warm rim along her shoulder, jaw and loose hair, cool fill everywhere else, gentle and never dramatic, no candles, no artificial source, no shaft effect. Camera: 50mm lens at f2.0, waist height, medium shot from a front three quarter position, subject slightly left of centre and occupying roughly the middle third, headstones and railing falling away into soft bokeh behind her, focus held on her closed eyes and the earbud. Palette: cool slate grey and damp moss green, bronze 9A7B4F and camel in her coat and scarf, cream F7F3EC chrysanthemums, muted rust in the leaves, one faint warm gold rim. Styling and wardrobe: camel or charcoal wool overcoat, bronze scarf, plain leather gloves tucked in a pocket, sensible shoes, grey hair loose and wind moved, no jewellery, no handbag staged, modest and ordinary. Era: contemporary, 2020s, a plain municipal or parish cemetery in Britain, Ireland, the United States, Canada, Australia or New Zealand. Mood: grief, and the consolation of having done something, quiet, warm and private, never mournful, never melodramatic, never bleak. Deliberately absent from frame: no candles, grave lanterns, votives or candle racks; no rosary, bracelet, medal, necklace or devotional object; no legible surnames, dates, inscriptions, photographs on stones or cemetery signage; no handwritten names on paper; no visible phone interface, app, logo or branding of any kind; no crying, no hand on a headstone, no kneeling; no other people. Photographic realism cues: real skin texture with cold flush at the nose and cheek, fine lines and pores intact, individual hair strands caught by the light, natural untouched colour, full frame digital capture around ISO 400, faint organic grain, slight atmospheric haze, no HDR, no retouching, no studio light, no stock photo posing, editorial documentary frame. Overlay: bottom 38 percent linear gradient scrim from transparent to 14110F at 82 percent opacity, headline in Fraunces semibold cream F7F3EC centered reading "November is the month of the Holy Souls.", below it a gold F2C230 pill button with dark 14110F Inter semibold label "Hear A Sample", and a small cream SANCTORIA wordmark top left in letterspaced Inter caps at 70 percent opacity.

**Distinct because:** it is outdoors at the grave inside the indulgence week, and the mechanism is
the drive home rather than the church building. The consolation is having something to carry away,
which the flowers-and-wind image sets up and neither other ad touches.

**One note on the overlay CTA.** "Hear A Sample" is honest, the page does carry sample clips, but
those clips are generated illustrations and are labelled as such on the page. The Meta CTA button
stays SEE_DETAILS to match the reference ad. If that overlay wording makes TS uneasy, swap it for
"See How It Works" and nothing else changes.

---

## 03 · `03_AThinThingToLeaveAChild`

**Headline:** More than a photograph and four stories

**Primary text:**

```
My granddaughter was three when my husband died. She asks me what he was like.

I have a photograph on the hall shelf and about four stories I tell the same way every time.

November is the month our parish prays for the dead. A photograph and four stories is a thin thing to leave a child.

I would like there to be more than that.

So that is what we make. One original song, close to four minutes, with a first name sung in every chorus, and the verse of scripture it is built on.

$39, one time. Sent within 24 hours. 30 day full refund.
```

**Visual: `TheBottomStair`.** Overlay YES. Headline on a bottom scrim, centered:
"Hers to keep, and to play again." Gold CTA pill: "Request A Song". Small SANCTORIA wordmark top
left.

**Image prompt:**

> Photographic documentary realism, square 1:1, 1080x1080. Subject: a woman in her mid sixties sitting on the second step from the bottom of a narrow carpeted staircase in a modest home hallway, still in her outdoor coat with only the top two buttons undone, handbag set down on the floor beside her feet, her forearms resting on her knees and hands loosely clasped. A small unbranded dark phone lies face up on the step beside her hip, playing aloud, its screen dim and angled away from the lens so nothing on it is legible. Her head is tilted a little toward the phone, eyes open and unfocused on the middle distance, a small worn smile, shoulders let down in relief. She has come in from outside and stopped halfway to taking her coat off because the song started. Setting: an ordinary hallway with pale painted walls, a coat rail holding two coats, a front door with a frosted glass panel at frame right, a worn doormat, one pair of men's brown leather shoes placed neatly by the door and softly out of focus, a folded newspaper at the edge of a small hall table. Lighting: cool flat grey afternoon daylight through the frosted door panel as the key from camera right, balanced by a warm low lamp spill from an open doorway at camera left at roughly one third of the key, soft, domestic and unremarkable, no candle, no shaft, no chiaroscuro, no glamour. Camera: 35mm lens at f2.2, low position near floor level at the far end of the hall so the lens sits at her eye level, subject at centre right, the staircase lines running up and out of the top of frame, shallow depth of field with the door, shoes and coat rail softening, focus on her clasped hands and face. Palette: warm oatmeal and dusty rose walls, bronze 9A7B4F stair runner, cream F7F3EC paintwork and skirting, cool grey light at the door, charcoal coat, one small olive accent in the hall table. Styling and wardrobe: charcoal or heather wool coat, bronze scarf still knotted, plain dark trousers, flat shoes, short grey hair, a plain wedding band, no makeup finish, nothing styled, a real home that is tidy but lived in. Era: contemporary, 2020s, modest suburban home in Britain, Ireland, the United States, Canada, Australia or New Zealand, late autumn afternoon. Mood: quiet, warm, consoled, the relief of having done something, intimate and ordinary, never bleak, never sentimental, never staged. Deliberately absent from frame: no candles, votives or candle racks; no rosary, bracelet, medal, necklace, triptych or devotional object; no framed photographs, no portraits of any person on any surface; no handwritten list of names, no family tree, no open Bible; no home altar or prayer shelf; no mug, teacup or kettle; no legible phone interface, app, album art, logo or branding; no legible surnames or addresses on the newspaper or post; no tears, no face to camera. Photographic realism cues: genuine skin texture with fine lines, slack and pores intact, wool coat nap and carpet pile resolved, natural mixed colour temperature left uncorrected between the cool door light and the warm lamp, full frame digital capture around ISO 1250, faint organic grain in the shadows, mild lens vignette, no HDR, no retouching, no studio light, no stock photo expression, editorial documentary frame. Overlay: bottom 38 percent linear gradient scrim from transparent to 14110F at 82 percent opacity, headline in Fraunces semibold cream F7F3EC centered reading "Hers to keep, and to play again.", below it a gold F2C230 pill button with dark 14110F Inter semibold label "Request A Song", and a small cream SANCTORIA wordmark top left in letterspaced Inter caps at 70 percent opacity.

**Distinct because:** it is the only one that looks forward instead of back. The consolation is
framed as something that could be left to a grandchild who never knew him, rather than an act she
performs at the book or at the grave in November.

**Pairing note.** The copy names a photograph on the hall shelf and the image deliberately contains
no photograph of any person. That is on purpose: the home altar with a framed elder portrait is a
used up visual in `CREATIVE_HISTORY.md`, and a legible portrait of a dead man is a beat this
account should not buy clicks with. The hallway setting still matches the copy's world.

---

## My own compliance pass

Checked by the builder, not only by the writing agents.

- **Dashes.** Zero em-dashes and zero en-dashes in any primary text, headline, overlay, ad name or
  anywhere in this file. Verified by character scan, not by eye.
- **Personal attributes.** No ad contains the word "you" or "your" at all. Every ad is first person
  narration of the narrator's own devotional practice, or third person about parishes. No "are
  you", no "your grief", no assertion about the reader's faith, family or losses. This matters more
  here than anywhere: this domain replaced one that was banned on Facebook for unknown, assumed
  content related reasons.
- **No claims about the dead.** In all three the song is only ever something the living make, keep
  or play. Nothing says or implies it reaches, affects, releases or benefits anyone who has died.
- **No outcome, health, financial or efficacy claims.** The only promises are the offer's own
  verifiable facts: $39 one time, about four minutes, sent within 24 hours, 30 day refund.
- **No invented testimonials, results or buyers.** Each narrator describes a practice she already
  performs and then states a wish. None of them owns, plays, receives or hands down a song, so
  nothing in the set reads as a customer report. **Ad 03 was sent back once for exactly this.** Its
  first draft ended "Something she can still play when the stories run out", which put the finished
  song in the narrator's family's hands and made her an implied buyer. It was rewritten to end on a
  wish and the offer's own facts.
- **No banned vocabulary.** Every term on the Ad Angle Policy's banned list was checked for by
  scan and none appears. The copy sits entirely in the allowed lane: peace, blessed, grace, faith,
  sacred, devotion, comfort, remembrance.
- **No competitor wording.** No line is lifted from any competitor. Ad 02's first headline draft
  duplicated the headline running on all three live ads and was replaced.
- **No old brand.** The predecessor brand is not named anywhere and no old brand imagery appears.
- **Dead executions avoided.** The dead `02_NovemberNames` hook, its candle rack and its long
  handwritten list of names are all absent. Checked against all 22 dead executions and both dead
  angles (`AQuietDevotion`, `DaughterPack`). No bracelet, triptych, necklace or rosary creative,
  per the standing rule that the bracelet side is finished.
- **Format.** All three are static photo. No video, no UGC.
- **Length.** 99 to 106 words each in six short paragraphs. LEARNINGS blames long line broken
  primary text for the account's largest single loss, $143.40 for one sale at $1.96 per outbound
  click against a $1.27 blend.

## What TS should know

1. **This was a rehearsal. Nothing exists.** No images were generated and no campaign, ad set, ad
   or creative was created. The copy above is ready to build.
2. **The order bump is still the most expensive open item and no ad fixes it.** 11 new front end
   buyers in the 28d window, zero `bump-blessing` first payments. A bump that attaches is worth
   roughly $70 to $230 of back end LTV per buyer against a front end netting about $37. The new
   `songform` Prayer Song checkout template needs verifying before further creative spend. Every
   Prayer Song buyer acquired without it is a permanent loss of the recurring line.
3. **The seasonal clock.** All Souls Day is Monday 2026-11-02 and the Holy Souls month runs all
   November. With the creation plus two days start rule, a build landing by roughly 2026-10-26 gets
   a week of learning before the date. This is the only time pressured item on the account.
4. **The live checkout was verified open.** `https://sanctoriastore.com/prayer-song/` now serves
   `soft: false` with a live `prayersong-1` checkout link on `template=songform`, so the funnel can
   actually take an order. Worth knowing, because `CLAUDE.md` still describes the page as a soft
   build with no checkout.
5. **This spends against a starved account on purpose.** The live `SungByName` angle has 14
   outbound clicks and will not be readable until roughly 2026-10-25. The brief builds this one
   anyway only because All Souls has a fixed date that will not wait for the data.
