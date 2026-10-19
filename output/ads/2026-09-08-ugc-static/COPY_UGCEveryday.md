# UGC STATIC ads — 4 variants (2026-09-08)

Static image ads written and shot in UGC voice. Cheap and fast to produce compared to video,
and not dependent on the HeyGen quota that is currently exhausted.

## Why

The UGC talking-head videos produced **2 sales on day one at roughly 10x ROAS** on ~$14.47
of spend, both multi-pack orders. The UGC *voice and look* is what is working, not one
specific face. This ports that to static.

## The two deliberate choices

**1. NO brand text overlay on these images.** Every other ad in this account carries the
eyebrow plus headline plus gold CTA button treatment. That treatment is exactly what makes an
ad look like an ad. A UGC static earns its lift by looking like a real person's photo in the
feed, so these ship as clean photos and the primary text does the selling. If a variant wins
and you want a branded version for comparison, that is a separate test, not a fix.

**2. The photography is deliberately amateur.** Phone-camera framing, mixed and unflattering
household lighting, real domestic clutter left in frame, mild sensor noise, no shallow
cinematic bokeh, ordinary unretouched people. If any of these looked professionally lit or
styled, it would have failed its job.

## Build spec

- Format code: **UGC** · SQUARE 1:1, 1080x1080
- Destination **/bracelet/** · CTA button **Shop Now**
- Targeting held constant at T1_MF_35-65+ so the creative is the only variable
- Images generated from the real store product photo, so the ad matches the page

| Level | Name |
|---|---|
| Campaign | `UGCEveryday_UGC_2026-09-08` |
| Ad Set 1 | `T1_MF_35-65+_UGCEveryday_UGC_KitchenTable` → ad `01_KitchenTableCoffee` |
| Ad Set 2 | `T1_MF_35-65+_UGCEveryday_UGC_NotAJewelryMan` → ad `02_NotAJewelryMan` |
| Ad Set 3 | `T1_MF_35-65+_UGCEveryday_UGC_Nightstand` → ad `03_NightstandSpot` |
| Ad Set 4 | `T1_MF_35-65+_UGCEveryday_UGC_DaughterPack` → ad `04_DaughterTwoPack` |

4 ad sets, 1 ad each, $5/day, campaign PAUSED.

```
utm_source={{site_source_name}}&utm_medium={{placement}}&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&cmc_adid=fb_{{ad.id}}
```

---

## 01 · KitchenTableCoffee
**Image:** `01_KitchenTableCoffee.png` — a woman in her 50s at a cluttered kitchen table, mail
and a charging cable and a dish towel left out, coffee mug, bracelet on her wrist.
**Headline:** Something to hold while praying

```
I almost didn't order it, because I'm 54 and I don't really wear jewellery.

But my morning prayer time had quietly turned into me sitting at the kitchen table with coffee, thinking about the grocery list.

Quiet house. Radio off. Mind three rooms away.

So I got the St Benedict bracelet. Real ebony wood beads, a bronze Benedict medal, a small crucifix, the Miraculous Medal.

Honest bit: it's plainer than I pictured. The medal is smaller. I like it better that way, as it turns out.

Now I turn the beads while I pray and my hands have something to do.

That's the whole thing. It just keeps me sitting there a bit longer.
```

---

## 02 · NotAJewelryMan
**Image:** `02_NotAJewelryMan.png` — a man in his 60s in a plaid shirt on the sofa, caught
mid-word looking off camera, family photos on the wall, bracelet on his wrist.
**Headline:** He actually wears it

```
I bought it for my husband fully expecting it to end up in a drawer.

He's 61. No ring, no watch, no chain, ever. Not a jewellery man in the slightest.

But he's been going to morning Mass on his own since he retired, and I wanted to mark that somehow without making a speech about it.

So: the St Benedict bracelet. Ebony wood, bronze Benedict medal, little crucifix, Miraculous Medal. Dark and plain, which is the only reason I risked it.

He put it on at the kitchen counter, said "huh", and has worn it every day since.

Wore it to his brother's. Wore it to the hardware store.

That's the most reaction I'm getting out of him, and honestly it's plenty.
```

---

## 03 · NightstandSpot
**Image:** `03_NightstandSpot.png` — the bracelet on a real nightstand at night beside a lamp,
reading glasses, a phone charging, a glass of water and a dog-eared paperback. Lamp-only light.
**Headline:** It stays on my nightstand

```
It lives on my nightstand, next to my reading glasses and a glass of water.

I'm 47 and I wake up around 3 most nights. Have done for years. Nothing dramatic, my brain just starts filing things.

I used to lie there and scroll, which never once improved anything.

Now I reach over, put the bracelet on, and pray a decade in the dark. Some nights I get all the way through it. Some nights I lose count around the fourth bead and start again.

The beads are real ebony, so they're warm in your hand instead of cold like metal. Mattered more than I expected.

Small caveat: took about two weeks to come. I'd nearly forgotten I ordered it.

It goes back on the nightstand every morning. Same spot.
```

---

## 04 · DaughterTwoPack
**Image:** `04_DaughterTwoPack.png` — a mother in her 60s and her adult daughter squeezed into
an arm's-length couch selfie, both wearing the bracelet, laundry on a chair behind them.
**Headline:** Gave one to my daughter

```
I ordered the 2-pack and gave one to my daughter without making a whole thing of it.

She's 34. Christmas and Easter, mostly. I stopped commenting on that about ten years ago, because commenting never once worked with her.

So I handed it to her in the car and said it made me think of her. That was the entire speech.

She turned it over, said the wood was nicer than she expected, and put it on.

Ebony beads, a bronze Saint Benedict medal, a small crucifix, the Miraculous Medal. Nothing flashy, which is why I thought she might keep it.

She still had it on at dinner Sunday. I noticed and said nothing.

I'm 66. That's how it goes with grown children. You hand them something small and you leave it alone.
```

---

## Compliance notes

- No em or en dashes.
- **No efficacy or supernatural claims.** This was the biggest risk in UGC voice, because real
  people naturally write things like "I feel safer since I got it". Nothing here credits the
  bracelet with protecting, healing, warding anything off, or making prayers work. In
  `03_NightstandSpot` the 3am waking is explicitly framed as a long-standing habit and the
  bracelet is NOT credited with changing it.
- No fear, curse or spiritual-warfare vocabulary.
- No fabricated scarcity or urgency.
- No second-person assertions about the reader's faith or practice. Every claim sits inside
  the speaker's own experience, or is about her own husband or daughter.
- **Not framed as customer reviews.** No names, no star ratings, no "verified buyer" badges.
  These are first-person persona narration, the same construction as the UGC videos already
  running. There are still no real customer reviews.
- The honest caveats ("it's plainer than I pictured", "took about two weeks to come") are
  deliberate. They raise believability, and they are also truthful rather than flattering,
  which keeps the ads clean.
