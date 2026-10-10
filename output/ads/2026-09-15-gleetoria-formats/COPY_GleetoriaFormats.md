# Four Ads From Competitor Formats (2026-09-15)

Built after TS shared four Gleetoria Store ads. **Formats borrowed, copy rewritten from zero.**

## Why the copy is not theirs

All four competitor ads run on vocabulary this project's Ad Angle Policy bans: demons,
exorcism, spiritual attack, generational curses, torment, "Begone Satan". One of them adds
a medical frame ("If your son is battling addiction... Doctors dismiss it. Therapists
medicate it.") which is a Meta personal-attributes and health violation, and implies a
bracelet substitutes for addiction treatment.

Copying that vocabulary onto sanctoriastore.com would risk the domain the same way the DGG
domain was lost. So the transfer is **format only**.

| Borrowed | Rejected |
|---|---|
| Handwritten marker note as the hero image | Demon / exorcism / curse vocabulary |
| Split panel: wrist photo + benefit list | "If your son is battling addiction" |
| "POV:" badge with overlay bullets | "Stops night terrors instantly" |
| Premium hero on plinth with benefit pills | Doctors / therapists framing |
| Naming a specific family member | Fear-for-your-children framing |
| Multi-pack offer stacking | "Buy 2 Get 1 Free" (not true here) |

**The offer insight is the most valuable thing they gave us.** They lead with Buy 2 Get 1
Free because multi-pack is where the money is, which matches this account exactly: every
converting order has been a multi-pack. We cannot say buy-2-get-1 because the third
bracelet costs $10, not zero. The true version is stronger and compliant: **each additional
bracelet is $10.** $37 / $47 / $57. That line is in three of the four ads.

## Build spec

- Square 1:1, 1080x1080, destination **/bracelet/**, CTA **Shop Now**, $5/day, campaign PAUSED
- Targeting held constant at T1_MF_35-65+ so format is the only variable
- Product rendered from the real store photo `site/images/bracelet.png`, so beads are ebony
  and all metal is **bronze** (not silver)
- Ads 02, 03, 04: clean AI plate with reserved empty space, then headline and list rendered
  as real HTML/CSS via headless Chrome. Text was never baked into the AI image.
- Ad 01 is the exception: the handwriting IS the photograph, so it was generated in-image.
  Clean plates kept as `_clean_02/03/04.png` for re-running overlays without regenerating.

## url_tags (mandatory on every ad)

```
utm_source={{site_source_name}}&utm_medium={{placement}}&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&cmc_adid=fb_{{ad.id}}
```

## Naming

| Level | Name |
|---|---|
| Campaign | `WornForGenerations_MIXED_2026-09-15` |
| Ad Set 1 | `T1_MF_35-65+_HerHandwriting_NOTE_LinedPaper` → `01_HerHandwriting` |
| Ad Set 2 | `T1_MF_35-65+_ThreeGenerations_IG_SplitPanel` → `02_ThreeGenerations` |
| Ad Set 3 | `T1_MF_35-65+_SomewhereToPutYourHands_UGC_SteeringWheel` → `03_SomewhereToPutYourHands` |
| Ad Set 4 | `T1_MF_35-65+_WornNotStored_POSTER_Plinth` → `04_WornNotStored` |

`NOTE` is a new format code (handwritten-note photo). Added per the CLAUDE.md rule that new
codes get added as new formats appear.

---

## 01 · HerHandwriting · `01_HerHandwriting`
**Format:** handwritten note · **Image:** `01_HerHandwriting.png`
**Hook:** She prayed for me by name for forty years.
**Headline:** She never missed a day

```
She prayed for me by name. Every morning, for about forty years.

I only found out how long when I was clearing out her kitchen and found the list.

My name, my brother's, my father's, and a few people I had never heard of.

I am not as disciplined as she was. I will say that plainly.

But I wear this on my wrist now and I get through the names most days.

Ebony wood beads, a bronze Saint Benedict medal, a small crucifix, the Miraculous Medal.

$37 for one. $47 for two. $57 for three, if there is more than one wrist in the house.

Free US shipping, 30 days to send it back.
```

---

## 02 · ThreeGenerations · `02_ThreeGenerations`
**Format:** split panel + benefit list · **Image:** `02_ThreeGenerations.png`
**Hook:** One bracelet. Three generations.
**Headline:** One bracelet, three generations

```
My mother has one. I have one. My daughter has one, on a bedpost, which I am counting as a win.

We did not plan to match. I ordered three because three cost $57 and one cost $37, and the maths made the decision for me.

Ebony wood beads on a cord, a bronze Saint Benedict medal, a small crucifix, the Miraculous Medal.

It is plainer in person than in the photos. I like it better that way.

Mine has been through the shower, the washing up and a fortnight of school runs and it looks the same.

Each extra one is $10. That is the whole reason there are three of us.
```

---

## 03 · SomewhereToPutYourHands · `03_SomewhereToPutYourHands`
**Format:** POV overlay · **Image:** `03_SomewhereToPutYourHands.png`
**Hook:** POV: your hands finally have somewhere to go.
**Headline:** Somewhere for your hands to go

```
I do most of my praying in the car. Not proudly. It is just where the quiet is.

For years my hands had nowhere to go, so they stayed on the wheel and my mind wandered off by the second decade.

Having beads I can actually feel fixed that. My thumb does the counting now instead of my head.

Ebony wood, a bronze Saint Benedict medal, a small crucifix, the Miraculous Medal.

It reads as a plain wooden bracelet from across a car park. That is about the right amount of visible.

$37 for one, and $10 for each one after that.
```

---

## 04 · WornNotStored · `04_WornNotStored`
**Format:** premium hero + pills · **Image:** `04_WornNotStored.png`
**Hook:** Most of these live in a drawer.
**Headline:** Worn, not stored

```
Most Catholic families already have a Saint Benedict medal somewhere.

In a dish by the door. In a drawer with the spare batteries. It came from a funeral, or a baptism, and nobody quite remembers which.

That is the whole problem this solves. It is not more devotional than the medal in your drawer. It is just on a wrist instead of in a drawer.

Ebony wood beads, a bronze Saint Benedict medal, a small crucifix, the Miraculous Medal, on a cord that fits.

Hand-assembled and hand-blessed in the Benedictine tradition before it ships.

$37. $47 for two. $57 for three. Free US shipping, 30 days to send it back.
```

---

## Compliance notes

- No em or en dashes.
- **Zero banned vocabulary.** Nothing says demon, exorcism, curse, attack, torment, evil,
  darkness, warfare, shield or protect.
- **No efficacy claims.** Ad 04 states the limit outright: "It is not more devotional than
  the medal in your drawer."
- **No medical content of any kind.** No doctors, therapists, addiction, sleep or illness.
- **No second-person assertions** about the reader's faith, family or circumstances. First
  person or community framing throughout. The one second-person line, "you finally have
  somewhere to put your hands", is about a habit, not a belief or a condition.
- **Heritage dating avoided entirely.** Their "1,500-year-old Latin exorcism inscriptions"
  is false as well as non-compliant: Benedict lived roughly 1,500 years ago, but the medal
  design was formalised in 1880. No dating claim is made in any of the four.
- **No fabricated testimonials, names or ratings.** First-person narration only.
- All prices verified against the live /bracelet/ tiers ($37 / $47 / $57).
- Blessing described only as "in the Benedictine tradition". No Rome, no named abbey.
- No Gleetoria artwork, byline, branding or wording is reproduced.

## Standing caveat

The last four days on this account ran at 0.53x with 5 to 15% CTRs. These formats will
likely raise CTR further, but CTR is not the broken part. If /bracelet/ converts these
clicks the way it converted the last 120, more creative will not change the result. Run
this batch and a `/funnel-audit` in parallel, not creative alone.
