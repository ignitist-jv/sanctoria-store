# Proven Angle Refresh (2026-10-01)

Five new creatives on the three angles that actually produced sales between 2026-09-01 and
2026-10-01. Nothing here is a new angle. Every one is a fresh scene on a mechanism that has
already converted on this account.

## What the 30-day data says

9 ads produced 16 sales on $572.02 for $715.96 (1.25x blended). Grouped by angle:

| Angle | Ads | Sales | Spend | Revenue | ROAS | Refreshed here |
|---|---|---|---|---|---|---|
| **AQuietDevotion** | 3 | **7** | $200.70 | $290.85 | **1.45x** | ✅ 2 new scenes |
| **MenWhoPray (PHOTO)** | 1 | 1 | $15.27 | $55.45 | **3.63x** | ✅ 2 new scenes |
| **NovemberNames** | 1 | 1 | $17.28 | $32.99 | **1.91x** | ✅ 1 new scene |
| DaughterPack | 2 | 4 | $226.20 | $219.09 | 0.97x | ❌ below the 1.2 line |
| SistersThreePack | 1 | 2 | $76.56 | $84.52 | 1.10x | ❌ below the 1.2 line |
| ThreeGenerations | 1 | 1 | $36.01 | $33.06 | 0.92x | ❌ below the 1.2 line |

**The family multi-pack angles are the ones with volume and the ones losing money.** Four sales
on DaughterPack returned 0.97x. They are not refreshed here.

## Two things the pull surfaced that the daily checks missed

**1. `01_QuietMansFaith` (`120256163362400051`) is the highest-ROAS ad in the account at 3.63x,
and it is paused.** It is a men's angle in PHOTO format. Every men's angle in UGC format has
died, which is why LEARNINGS records men's angles as dead. **The variable is format, not
audience.** One sale on 29 outbound clicks is a thin sample and that caveat stands, but the
angle has never been refreshed once. Two of the five ads here test it properly.

**2. `02_ParkedAndEarlyRosary` (`120256490331090051`) returned 2.74x.** That is AQuietDevotion
ported from the bracelet to the rosary funnel on 09-26. **The mechanism travels across
products.** It is not bracelet-specific.

## The mechanism being refreshed

Per the 2026-09-28 correction in LEARNINGS: a small, private, ordinary moment that already
exists in her day, plus an object that gives her hands something to do in it. Every scene below
is a real stolen minute. None of them is a devotional set piece.

## Build spec

- Square 1:1, 1080x1080, destination **https://sanctoriastore.com/bracelet**, CTA **Shop Now**
- Clean AI photographs, **no text baked into any image**, no overlays
- Product rendered from the real store reference so beads are matte black ebony and all metal
  is **antique bronze**, never silver
- $5/day per ad set, scheduled start **2026-10-03T03:00:00+08:00**
- **CAMPAIGN PAUSED.** Ad sets and ads built ACTIVE underneath it so nothing delivers or spends
  until TS turns the campaign on. That one switch is the only step left.
- 5 ad sets, exactly 1 ad each, so every creative is isolated

## Image rejected before build

`01_BeforeIGetDressed` (edge of an unmade bed, early light) was generated and **discarded**. It
rendered with bare legs in a dim bedroom, which is an adult-content rejection risk on a
devotional ad, and the bracelet was too small to read at thumbnail size. Replaced with the
staircase scene, fully clothed, bracelet prominent.

## URL parameters (mandatory, still outstanding)

Website URL and URL parameters are separate fields. The link stays clean:

```
https://sanctoriastore.com/bracelet
```

URL parameters field:

```
utm_source={{site_source_name}}&utm_medium={{placement}}&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&cmc_adid=fb_{{ad.id}}
```

## Naming and live IDs (built 2026-10-01)

**Campaign `ProvenRefresh_PHOTO_2026-10-01` = `120256577692480051`, set to PAUSED.**

| Ad Set | Ad Set ID | Ad | Ad ID | Creative ID |
|---|---|---|---|---|
| `T1_MF_35-65+_AQuietDevotion_PHOTO_ThirdStair` | `120256577693150051` | `01_ThirdStairFromTheBottom` | `120256577694600051` | `4683680645286166` |
| `T1_MF_35-65+_AQuietDevotion_PHOTO_BackStep` | `120256577697020051` | `02_TheBackStep` | `120256577697710051` | `1632045675315999` |
| `T1_MF_35-65+_MenWhoPray_PHOTO_Workbench` | `120256577698550051` | `03_HisHandsOnTheBench` | `120256577699860051` | `29036735822586594` |
| `T1_MF_35-65+_MenWhoPray_PHOTO_FiveAM` | `120256577701490051` | `04_FiveInTheMorning` | `120256578666800051` | `1087291547016056` |
| `T1_MF_35-65+_NovemberNames_PHOTO_CandleRack` | `120256578823440051` | `05_TheNamesInNovember` | `120256578828520051` | `2047773295908580` |

Every one of the 10 entities returned `active_errors: []`.

### Image hashes (reuse these, do not re-upload)

| Image | Meta image_hash |
|---|---|
| 01_ThirdStairFromTheBottom | `39a5d023d82dd7aac5c9d272cc519f75` |
| 02_TheBackStep | `6aad931036ff99ca4f2579f01b30a640` |
| 03_HisHandsOnTheBench | `49354d6d9c62d79c28efa74e4be7cf98` |
| 04_FiveInTheMorning | `f4d02ed7448690a99ed7a720dfb338cd` |
| 05_TheNamesInNovember | `10207801d995964c4260d42096691c4f` |

### Dead entities to ignore or archive

Two abandoned drafts were produced before the working method was found. Neither has ads worth
keeping. `120256577277040051` (first attempt, destroyed by a mid-chain pause) and
`120256577668730051` (second attempt, ad `120256577676740051` carries the
`ObjectStorySpecRedundant` error). Also five superseded `CR_*` creatives built from `image_url`:
`1142017138526390`, `1418900190443976`, `2939711983073498`, `1736176120989999`,
`3561900540640010`. The live ads use the `CRH_*` set instead.

## Meta API method that actually works on this account

1. `ads_creative_upload_image` is dead here (Authorization Error). The two newer upload tools are
   not rolled out to this account. **Do not waste calls on them.**
2. Pass `image_url` to `ads_create_creative`. Meta fetches the jsDelivr JPG and mints a hash.
3. Read the hash back: `ads_get_creatives` with field `image_hash`.
4. Rebuild the real creative with `image_hash`. **A creative made from `image_url` cannot publish**
   because link_data then holds both `picture` and `image_hash`, which fails validation with
   `ObjectStorySpecRedundant` (1443051).
5. **Build campaign, ad sets and ads in one uninterrupted pass.** Calling `ads_update_entity` on a
   draft campaign before its children exist destroys the entire draft.
6. `ads_create_campaign` has no `status` argument, so drafts always spec ACTIVE. Pause the campaign
   only after the full chain is built. The 2-day scheduled start is the safety margin.

---

## 01 · AQuietDevotion · `01_ThirdStairFromTheBottom`

**Image:** `01_ThirdStairFromTheBottom.jpg` · **Format:** PHOTO · **Funnel:** /bracelet
**Hook:** I sit on the stairs for two minutes before I leave the house.
**Headline:** Two minutes on the stairs

```
I sit on the stairs for about two minutes before I leave the house.

Coat on. Bag by my feet. Door shut.

It is not a holy thing. It is just the only two minutes in the day nobody wants anything from me.

I used to spend them staring at the carpet.

Now my thumb goes round the beads and I get through four or five names before I stand up.

Matte black ebony wood, a bronze Saint Benedict medal, a small crucifix, a second small medal.

It is plainer in person than it looks here. I prefer it that way.

$37 for one. $47 for two. $57 for three.

Free US shipping, 30 days to send it back.
```

---

## 02 · AQuietDevotion · `02_TheBackStep`

**Image:** `02_TheBackStep.jpg` · **Format:** PHOTO · **Funnel:** /bracelet
**Hook:** My whole prayer life is a back doorstep and a cup of tea.
**Headline:** The back step, most mornings

```
My whole prayer life is a back doorstep and a cup of tea.

That is it. That is the routine.

I am out there in a cardigan over my pyjamas most mornings, looking at a garden I keep meaning to deal with.

For years I thought that did not really count, and then I decided it was the only part that did.

The beads were the one thing that changed. My hands used to just hold the mug. Now one of them is doing something.

Matte black ebony wood, a bronze Saint Benedict medal, a small crucifix, a second small medal on a short chain.

Mine has been rained on, dropped on concrete and worn in the shower. It looks the same.

$37 for one, and $10 for each one after that.

Free US shipping, 30 days to send it back.
```

---

## 03 · MenWhoPray · `03_HisHandsOnTheBench`

**Image:** `03_HisHandsOnTheBench.jpg` · **Format:** PHOTO · **Funnel:** /bracelet
**Hook:** My father never once said a prayer out loud in front of me.
**Headline:** He never said one out loud

```
My father never once said a prayer out loud in front of me.

Not at the table. Not at a funeral. Not in forty one years.

But he was out in that garage every evening after dinner and he was not always working.

I used to think he just liked the quiet out there.

I got him this last year, half expecting it to end up in a drawer with the fuses.

He put it on at the bench and has not taken it off since. He has never mentioned it. Not once.

That is a rave review from him.

Matte black ebony wood, a bronze Saint Benedict medal, a small crucifix, a second small medal.

$37. Free US shipping, 30 days to send it back.
```

---

## 04 · MenWhoPray · `04_FiveInTheMorning`

**Image:** `04_FiveInTheMorning.jpg` · **Format:** PHOTO · **Funnel:** /bracelet
**Hook:** He is up at five. The kettle, the paper, and four minutes where he does not move.
**Headline:** Four minutes before the van

```
He is up at five. Kettle, paper, van keys on the table.

And then about four minutes where he does not move and does not read anything.

I asked him once what he was doing. He said "nothing" in a way that meant leave it.

Twenty six years of that and I have never asked again.

The bracelet was a Christmas thing. I genuinely thought he would hate it.

It has been on his wrist through two winters of work and it still looks like itself.

Matte black ebony wood, a bronze Saint Benedict medal, a small crucifix, a second small medal on a short chain.

Not shiny. Reads as a plain wooden band from across a yard, which is about the right amount of visible for him.

$37 for one. $47 for two. Free US shipping.
```

---

## 05 · NovemberNames · `05_TheNamesInNovember`

**Image:** `05_TheNamesInNovember.jpg` · **Format:** PHOTO · **Funnel:** /bracelet
**Hook:** Every November I light a candle and try to get through all the names.
**Headline:** The names I say in November

```
Every November I light a candle and try to get through all the names.

I never manage the whole list in one go.

My grandmother. My father. A neighbour I was fonder of than I ever told her.

A few I only know as a surname because my mother used to say them and now I say them instead.

Somewhere around the sixth or seventh I lose the thread and have to start again.

Having something to count on helped more than I expected. One bead, one name, keep going.

Matte black ebony wood, a bronze Saint Benedict medal, a small crucifix, a second small medal on a short chain.

$37 for one. $47 for two, if there is someone else in the house with their own list.

Free US shipping, 30 days to send it back.
```

---

## Compliance notes

- **No em or en dashes.**
- **Zero banned vocabulary.** Nothing says demon, exorcism, curse, attack, torment, evil,
  darkness, warfare, shield, guard or protect, despite three of the five being Saint Benedict
  medal ads.
- **No efficacy or supernatural claims.** Nothing in any of the five claims the object does
  anything. `01` states the limit directly: "It is not a holy thing."
- **No claims about the dead.** `05` is the sensitive one and is written so the bracelet only
  ever helps the speaker keep her place in a list. It never suggests the object affects, reaches
  or benefits anyone who has died. The practice described is ordinary All Souls remembrance.
- **No medical content.** No illness, no grief counselling framing, no doctors.
- **No second-person assertions** about the reader's faith, family or circumstances. All five
  are first-person narration.
- **No fabricated testimonials, names or ratings.** No star counts, no customer quotes.
- **No fabricated scarcity.** No countdowns, no "reserve yours", no stock claims.
- No heritage dating claim. The medal design was formalised in 1880, so no "1,500 year old"
  framing appears.
- Blessing is not mentioned in these five at all, so there is nothing to qualify.
- **All prices verified against the live /bracelet page** ($37 / $47 / $57).
- `03` and `04` describe a third party's private devotion observationally, from the speaker's own
  side, never asserting what he believes.

## Standing caveat on reading the results

Per the 2026-09-23 funnel audit, **$15 of spend buys about 12 outbound clicks at $1.27 each, and
at the account's 3.07% site conversion rate an ad performing exactly at average shows zero sales
69% of the time.** The $15 kill threshold cannot produce a valid verdict on these. Judge them on
outbound CTR and cost per outbound click first, and give any that look alive enough spend to
reach roughly 35 to 40 outbound clicks before calling a sale verdict.
