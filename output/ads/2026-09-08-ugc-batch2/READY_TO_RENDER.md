# UGC Batch 2 — READY TO RENDER (blocked on HeyGen quota, 2026-09-08)

## Status

**BLOCKED.** All three videos failed to render:
`AVATAR_IV_VIDEO_GENERATION_DURATION_LIMIT_REACHED` — "You've reached your Avatar IV
monthly limit". A 1080p attempt first failed with `RESOLUTION_NOT_ALLOWED`; the 720p retry
then surfaced the real cause. Everything below is finished and ready; only the HeyGen render
step remains.

To unblock: upgrade the HeyGen plan or wait for the monthly quota reset. Alternative: render
via Higgsfield instead (available now, lip-sync slightly softer than HeyGen).

## Why this batch

The first UGC video batch produced **2 sales on day one** at roughly 10x ROAS on ~$14.47 of
spend, both multi-pack orders:

| UGC Ad Set | Spend | Sales | ROAS | CTR |
|---|---|---|---|---|
| Kitchen (Face B) `120256150053250051` | $5.12 | 1 ($51.43) | 10.04x | 19.57% |
| Cardigan (Face A) `120256150053240051` | $4.77 | 1 ($46.72) | 9.79x | 1.92% |
| Couch (Face C) `120256150053270051` | $4.58 | 0 | — | 20.00% |

~6.8x blended. Note Cardigan converted at 1.92% CTR while Couch has 20% CTR and no sale, so
CTR is not predicting sales on this format.

This batch expands the winning FORMAT with a different person AND a different angle in each.

## Build spec

- Format: UGC talking-head video, 4:5, ~35s, HeyGen `create_video_from_image`
- Destination /bracelet/ · CTA Shop Now
- Captions burned in BELOW THE CHIN (never over the face or mouth)
- B-roll cut in on the product line, synced to the VO's own silence gaps
- Resolution: 720p (1080p is blocked on the current plan)

| Level | Name |
|---|---|
| Campaign | `UGCAngles_UGC_2026-09-08` |
| Ad Set 1 | `T1_MF_35-65+_MenWhoPray_UGC_WeddingRingOnly` → ad `01_WeddingRingOnly` |
| Ad Set 2 | `T1_MF_35-65+_TheWayBack_UGC_TwelveYears` → ad `01_TwelveYears` |
| Ad Set 3 | `T1_MF_35-65+_StoppedHidingIt_UGC_ParkingLot` → ad `01_ParkingLot` |

url_tags (every ad):
```
utm_source={{site_source_name}}&utm_medium={{placement}}&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&cmc_adid=fb_{{ad.id}}
```

---

## 1. MenWhoPray · `01_WeddingRingOnly`
**Speaker:** man, about 55, greying, green work shirt, at his kitchen table (`faceD_man.png`).
**Voice:** HeyGen "Adam Stone" `88bb9ee1c81b466eb2a08fdde86d3619`, speed 0.93.
**Why it is new:** every ad and every video this brand has run has been a woman. This opens
the Catholic-men audience on the format that is converting.

```
I've never worn jewelry in my life. Wedding ring, that's it.

I'm not the sort of man who talks about any of this out loud. I don't carry a rosary. I'm not going to wear a scapular.

But I'll wear something on my wrist.

Real ebony wood. A Saint Benedict medal, a small crucifix, and the Miraculous Medal.

Nobody asks me about it. Suits me fine.

Most mornings I put it on and say a short prayer in the truck. That's between me and God.

It's called the St Benedict Marian bracelet, from Sanctoria. Quiet thing. Made well. That's all I'll say about it.
```

Caption beats: "I've never worn jewelry in my life." / "I don't carry a rosary." / "But I'll
wear something on my wrist." / "Real ebony wood. Saint Benedict." / "That's between me and
God." / "Quiet thing. Made well."

**B-roll: MALE hands required** (the existing b-roll is female and would break the illusion).
Two male frames generated: `mbroll1_wheel.png` (wrist on a truck steering wheel at dawn,
matching his "prayer in the truck" line) and `mbroll2_puton.png` (putting it on at the
kitchen counter).

---

## 2. TheWayBack · `01_TwelveYears`
**Speaker:** woman, about 50, auburn wavy hair, grey sweatshirt, bedroom (`faceE_wayback.png`).
**Voice:** HeyGen "Rose - UGC" `0495e14c2bd74eb3aeeef03583e0bce5`, speed 0.96. A UGC voice
clone rather than polished TTS, for authenticity.
**Why it is new:** every existing angle assumes an already-devout daily pray-er. This one
explicitly does not.

```
I hadn't been inside a church in about twelve years.

Nothing happened. I didn't get angry. I didn't decide anything. I missed one Sunday, then another, and then it was a decade.

I'm going back now. Slowly. I'm not good at it yet.

I bought a bracelet before I bought anything else. Ebony wood beads, a Saint Benedict medal, a little crucifix, the Miraculous Medal. Something small I could hold onto.

Most days I just turn it around my wrist and that's the whole prayer. That's honestly all it is so far.

It's from Sanctoria. It was an easy place to start again.
```

Caption beats: "About twelve years." / "I didn't get angry. I just drifted." / "I'm going
back. Slowly." / "Something small I could hold onto." / "That's the whole prayer." / "An easy
place to start again."

B-roll: reuse the existing female clips `fixA_thumb.mp4` and `broll2_hands.mp4`.

---

## 3. StoppedHidingIt · `01_ParkingLot`
**Speaker:** woman, about 45, dark ponytail, black top, home office (`faceF_hiding.png`).
**Voice:** HeyGen "Autumn - UGC" `03dca9ebfca441dba55fb14afa0791b7`, speed 0.97.
**Why it is new:** identity and public witness, a different psychological driver from comfort
or devotion.

```
I used to take it off in the parking lot before a meeting.

I'd do the math in my head. Who's in the room, what they'll think, whether I want to explain myself. Then I'd slide it up under my sleeve and walk in.

I don't remember deciding to stop doing that. I just got tired of making myself smaller over a bracelet.

Ebony wood. A Saint Benedict medal, a small crucifix, the Miraculous Medal. It sits on my wrist and it says what it says.

Someone noticed last month. I told her it was my grandmother's devotion. That was the whole conversation.

Sanctoria makes it. It stays on now.
```

Caption beats: "I used to take it off in the parking lot." / "I'd do the math in my head." /
"I got tired of making myself smaller." / "It says what it says." / "My grandmother's
devotion." / "It stays on now."

B-roll: reuse the existing female clips.

---

## Compliance notes

- No em or en dashes.
- No efficacy or supernatural claims anywhere; the bracelet is only a companion to devotion.
- No fear, curse or spiritual-warfare vocabulary.
- No fabricated scarcity or urgency.
- **No second-person assertions about the viewer's faith or practice.** This mattered most in
  TheWayBack: every mention of drifting is about the SPEAKER's own twelve years, never the
  viewer's. Same in StoppedHidingIt, which is her own habit, not an accusation.
- All three are first-person persona voices, consistent with the UGC videos already running,
  and none is presented as a named customer review with a rating.
