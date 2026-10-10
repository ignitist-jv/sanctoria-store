# Your Prayer Song: ad batch 1, visual creative briefs and generation prompts

Written 2026-10-08. Visual concepts, shot lists, layouts and generation prompts only.
Primary text and headlines are written separately by the copywriter.

Three formats, each reverse engineered from one of the market leader's three
(page 689255950933095, about 1,000 active ads, US only, all video, 2 to 3.5 minutes).

## THE STRATEGIC REFRAME

The competitor's payoff is always the recipient's reaction. A reaction shot is not the
product. It is a PROXY for a claim the viewer cannot otherwise check: this song is good
enough to make someone cry. They need the proxy because a 2 minute video cannot otherwise
prove a song is worth $39.

Sanctoria has the thing the proxy stands in for: seven real finished songs, renderable and
playable today. So the batch does not imitate the reaction. It imitates the ATTENTION
MECHANICS of all three formats (the caption bar, the offer panel, the text setup, big
burned-in lyric captions, the raw phone look) and swaps the payoff from a stranger's face
to the song itself, heard, with the name landing in the chorus.

That is not a compromise forced by the constraint. It is a better fit:
1. It is checkable. A face is an assertion; audio is evidence.
2. It is congruent. The landing page already leads with samples and states plainly that
   there are no reviews yet. A reaction-led ad would set an expectation the page refuses.
3. The lyric caption carries the emotion, so no human has to perform it.

**The name on screen is the pattern interrupt.** Nobody scrolling expects to see a specific
first name sung inside a hymn. That is the batch's single strongest visual asset and all
three formats are built around it.

## HARD RULES FOR THIS BATCH

- Audio is always a REAL rendered song from `creative/test-songs/`. Never write new lyrics
  for an ad. Burned-in lyric captions must be verbatim from the verified transcript.
- **Do NOT use `06_four_minute` (Lay Your Hand On Siobhan) in any ad.** Its verified
  transcript contains "You said You would restore her health", "Heal her body, ease her
  pain" and "give the doctors steady hands". As burned-in ad captions those read as health
  claims and are banned for this account. It stays on the sales page; it stays out of ads.
- Every lyric line that becomes a caption gets screened before build against (a) the banned
  fear vocabulary, (b) any health or healing claim, (c) any promised outcome. Only the
  Siobhan transcript has been verified so far. Screen the Daniel and Nevaeh transcripts
  line by line before cutting.
- "A prayer of protection" is allowed. "This protects her" is not.
- Every creative carries a sample label. Exact wording and position are specified per format.
- No face in a product reaction. See the honesty verdicts per format.
- No testimonial, rating, review count, customer number or scarcity figure anywhere.
- No readable text inside any generated frame. This is a logged failure mode for this
  project. Lyric sheets and screens are photographed or screen-recorded, never generated.
- All dimensions in generation prompts are anchored to ratios of things in the frame,
  never to real units. See LEARNINGS.md, the necklace image fix.

## FORMAT SUMMARY

| # | Name | Format code | Maps to competitor | Humans in frame | Generation needed | Length |
|---|---|---|---|---|---|---|
| 1 | LyricPlayer | VID | Reaction + offer panel | none | none, or 1 plate | 2:30 + 45s cut |
| 2 | QuietDevotionSung | UGC | Story hook over raw reaction | faceless only | 3 stills + 3 loops | 75s |
| 3 | TheNameGoesIn | SCR | Text meme + deadpan hold | none | none | 35s |

`SCR` is a new format code (screen recording). Log it in LEARNINGS.md alongside IG, VID,
DX, PHOTO, MACRO, POSTER, UGC, ADV, ILLUS.

---

# FORMAT 1: LyricPlayer (VID)

## (a) Concept and what it tests

**Concept:** the top half is the song playing, as an honest artifact (title, waveform,
advancing lyric caption, the name landing in the chorus) over a still kitchen table that
barely moves. The bottom half is the competitor's static offer panel, lifted wholesale.

**What it tests:** whether the song alone can carry an ad with no human being in frame at
all. This is the control for the whole offer. If it works, every future creative for this
product gets cheaper and safer, because the asset is the audio and the audio already exists.
It also isolates the competitor's offer panel as a reusable bottom-half component.

Creative angle: Mechanism / Discovery. Emotion: recognition, then tenderness.

## (b) Layout and shot list

Canvas 1080 x 1350 (4:5). Panel A is footage, Panel B is a flat cream card.

| Element | x | y | Notes |
|---|---|---|---|
| Panel A, footage | 0 to 1080 | 0 to 810 | the tabletop loop, 4:3 landscape plate |
| Hook line (copywriter) | 72 to 1008 | 60 to 230 | max 2 lines, left aligned, white, 4px dark shadow |
| Song title strip | centred | 560 to 605 | small caps, 30px, cream at 85%, letter-spaced |
| Waveform bar | 72 to 1008 | 630 to 668 | amber #F2C230 played, cream at 30% unplayed, 6px radius |
| Lyric caption | 72 to 1008 | 690 to 790 | 1 to 2 lines, centred, white Inter SemiBold 54px, 4px dark shadow, advances with the audio |
| Panel B, cream card | 0 to 1080 | 810 to 1350 | solid #F7F3EC, 1px bronze #9A7B4F hairline along y=810 |
| Panel B eyebrow | centred | 858 to 898 | 26px bronze #9A7B4F, small caps |
| Panel B main line (copywriter) | 90 to 990 | 912 to 1072 | max 2 lines, Fraunces 64px, #2B2118, centred |
| Panel B support line (copywriter) | 120 to 960 | 1092 to 1146 | 1 line, Inter 32px, #5A4A38, centred |
| CTA affordance bar | 130 to 950 | 1178 to 1286 | gold #F2C230, 24px radius, Inter SemiBold 40px #2B2118, centred |
| Sample label (mandatory) | centred | 1306 to 1338 | 22px, bronze #9A7B4F at 70% |

Sample label wording, fixed, not the copywriter's to change:
`A sample prayer song made by Sanctoria. Not a customer's song.`

**Audio:** `creative/test-songs/demo_Lead_Daniel_Home.mp3` (son, a return to the faith,
gentle guitar). Starts at 0:00 of the ad with the instrumental intro already running, so
the first frame has sound. Enter the song at the top of verse 1, not the intro, for the
45s cut.

**Timeline, 2:30 cut:**

| Time | Panel A | Lyric caption |
|---|---|---|
| 0:00 to 0:02 | plate live, candle flickering | empty. The HOOK line is the only text. Hook must land inside 2s |
| 0:02 to 0:26 | unchanged | verse 1, one line at a time |
| 0:26 to 0:54 | unchanged | chorus. **The name gets its own caption card, alone on screen, 1.2s, 96px** |
| 0:54 onward | unchanged | verse 2, chorus, bridge, verse 3, final chorus |
| last 6s | unchanged | final chorus closing lines, then hold on the outro word |

Panel B never changes for the whole 2:30. That is the competitor's own structure and it is
what makes the format cheap: one static card, any audio, any length.

**45s cut:** verse 1 plus the first chorus, ending on the name card. Same layout.

**9:16 cutdown:** same two panels, Panel A 0 to 1180, Panel B 1180 to 1920. Keep all text
inside y 260 to 1500 for Reels and Stories safe area.

**1:1 static cutdown (per the standing square + CTA rule):** 1080 x 1080. Panel A 0 to 648,
Panel B 648 to 1080, gold CTA bar at y 900 to 1000, x 140 to 940. The lyric caption freezes
on the name line.

## (c) Generation prompts

### PRIMARY ROUTE: no generation at all

Print `creative/bonus-samples/Call Daniel Home Lyric Sheet.pdf` on plain cream paper and
photograph it. This is the recommended route and not a shortcut:

- The real artifact is more honest than any render.
- Readable text inside a generated frame is a logged failure mode for this project. A lyric
  sheet with legible words cannot be generated reliably, so photographing the real print is
  the only dependable way to get it.
- It costs one sheet of paper.

**Phone photo brief.** Shoot 4:3 landscape on a recent phone, held about 50cm above a worn
wooden kitchen table, angled about 30 degrees off vertical so the sheet is seen obliquely.
On the table: the printed lyric sheet lying flat and slightly askew, one plain white mug, a
dark wooden rosary loosely coiled, one small lit votive candle, a pair of reading glasses
folded. Light: one window to the left plus the candle, ceiling light OFF, early morning
grey. Do not style it. Leave crumbs, a ring mark, a crease in the paper. Expose for the
candle so the shadows go a little grainy. Shoot 20 frames, pick the one where the sheet's
heading is legible but the body text has gone soft, because the heading carries the title
and the body carries nothing.

Keep the lower third of the frame calm and dark (table edge, shadow) because the waveform
and lyric caption sit there.

Then make it move: feed the chosen photo to `seedance_2_5` with the motion prompt below so
the candle flickers. A dead-still plate under a 2:30 audio bed reads as a broken video.

### FALLBACK: generated plate, no readable text

Only if printing is not possible. The lyric sheet is turned FACE DOWN so no words exist in
the frame, and the title is supplied later as an overlay instead.

**Still prompt (Step A, `gpt_image_2_5`, aspect 4:3 landscape):**

```
SCENE: The corner of a worn wooden kitchen table in an ordinary family home, early on a grey morning, seen from above and slightly to the side. On the table, arranged the way things actually get left rather than styled: one plain white ceramic mug, empty, with a faint brown ring dried on the table beside it. A dark wooden rosary with small round matte black beads and a small dark wooden crucifix, lying loosely coiled and tangled, not laid out neatly. One small clear glass votive candle, lit, the flame small and steady. A pair of reading glasses folded, one arm resting on the other. A single sheet of plain cream paper lying FACE DOWN and slightly askew, so the camera sees only its blank reverse side and there is no writing of any kind visible on it. A few crumbs. SIZES, all anchored to the frame: the mug is about one fifth of the frame width. The candle glass is about half the mug's height, and its flame is about one fortieth of the frame height. Each rosary bead is about one eightieth of the frame width. The sheet of paper is about two fifths of the frame width. CAMERA POSITION: filmed by someone standing at the table holding a phone sideways about an arm's length above the surface, tilted roughly thirty degrees off vertical, so the table top fills the frame and a short stretch of the far table edge and a plain cream wall cut across the top fifth of the frame. The objects sit in the upper and middle thirds. THE LOWER THIRD OF THE FRAME IS CALM AND DARK: bare shadowed table wood and the near table edge only, with no object, no bright spot and no busy grain pattern there, because a caption will be placed over it. LIGHT: soft grey daylight from a window out of frame to the left, plus a small warm pool from the candle. The ceiling light is off. Shadows are open, a little grainy, and fall to the right. LOOK: A single frame taken from an ordinary home video, filmed on a phone held sideways by someone in the room. It must look like amateur family footage, not a professional photograph and not an advertisement. Phone camera character: a slightly wide lens and deep focus, so the near objects, the far objects and the back wall are all acceptably sharp at once, with no blurred background and no bokeh. Slightly flat contrast, ordinary automatic exposure, the candle flame a little blown out, fine sensor noise visible in the shadows, plain and slightly muted colour with the mixed white balance of a real room. Available light only, exactly as described above. No flash, no studio light, no rim light, no glow, no colour grade, no film look. Framing is imperfect the way a real handheld clip is: the picture tilted very slightly off level, the objects a little off centre, something ordinary cutting into one edge of the frame. A lived in home with everyday clutter. Landscape orientation, aspect ratio 4:3, full frame. WHAT THIS IS NOT: No person, no hand, no arm and no part of a body anywhere in the frame. There is no text anywhere in the frame: no captions, no subtitles, no usernames, no social media interface, no record indicator, no timestamp, no battery or signal icons, no watermark, no logo, no star rating, no border, no black bars, and no writing, printing, lettering or numerals on any object, on the paper, on the mug, on a magnet, on a book spine or on a picture. The paper is face down and blank. The image is the raw camera picture only. It is not a screenshot, and no phone, screen or hand is held up in the foreground. There is no phone, no screen and no headphone anywhere in the scene. No halos, no light rays, no glowing figures, no shafts of divine light. No flowers, no linen runner, no styled flat lay, no symmetrical arrangement. Not cinematic, not an illustration, not a painting, not a 3D render, not glossy advertising.
```

**Negative prompt:**

```
person, hand, arm, finger, face, body, text, letters, numbers, words, writing, printing, caption, subtitle, logo, watermark, signage, UI, button, border, frame, black bars, phone, screen, headphones, earbuds, flowers, bouquet, linen runner, styled flat lay, symmetrical arrangement, neat, tidy, props, studio lighting, flash, softbox, bokeh, blurred background, shallow depth of field, oversaturated, HDR, glossy, teal and orange grade, cinematic, illustration, painting, 3D render, cartoon, halo, light rays, glowing figure, bright or busy lower third
```

**Motion prompt (Step B, `seedance_2_5`, image to video, the approved still as BOTH start
and end image, 5 seconds, 4:3, audio off). Use this for the photographed plate too.**

```
Continue the supplied image as one unbroken amateur phone video, 5 seconds, real time, silent. CAMERA: held sideways in the hand by someone standing still. It barely moves: only a faint natural sway and breathing drift, never more than one fiftieth of the frame width, with the framing otherwise unchanged. ACTION: The candle flame flickers gently and leans a little, the way a real flame does in still air, and the small warm pool of light it throws on the table breathes very slightly with it. A single thin thread of steam, if any is present, drifts upward and fades. NOTHING ELSE IN THE FRAME MOVES AT ALL: the mug, the rosary, the glasses, the sheet of paper, the crumbs and the table all stay perfectly still in exactly their starting positions. MUST NOT HAPPEN: No person, hand, arm or animal enters the frame or appears at any point. Nothing is picked up, put down, moved, turned over, opened or slid. The sheet of paper does not turn over, lift, curl or show its other side. No new object appears and nothing disappears. No text, captions, subtitles, icons, logos or watermark appear at any point. No zoom, no push in, no pull back, no pan, no tilt, no orbit, no refocus. No scene change, no cut, no fade, no change of light or colour beyond the flame's own flicker, no slow motion, no speed change, no added background blur. The candle does not go out and does not flare up. LOOP: by the last frame the flame and the camera have settled back to match the first frame, so the clip repeats without a visible jump. Silent, no audio.
```

Build the 2:30 by looping this 5s clip with a 10 frame crossfade at each join. A candle loop
hides its own seam, which is why the plate was chosen over a human scene for this format.

## (d) Honesty verdict

**Works fully with generated footage, and better with no footage at all. No disclosure
beyond the sample label is needed.**

Every element is either the real product (the audio, the lyrics, the title, the printed
bonus sheet) or an inanimate table. There is no human being, so there is nobody who could
be mistaken for a customer and nothing that could be read as a testimonial. The only claim
the creative makes is "this is what one sounds like", and the ad plays the actual sound
while saying it. This is the most defensible creative in the batch and the only one that
could survive a Meta reviewer reading every pixel as an assertion.

The sample label is still mandatory, because a viewer could otherwise assume the song was
made for a real Daniel.

## (e) Naming

| Level | Name |
|---|---|
| Campaign | `SungKeepsBeingPrayed_VID_2026-10-08` |
| Ad Set | `T1_MF_45-65+_SungKeepsBeingPrayed_VID_LyricPlayer` |
| Ad | `01_LyricPlayerLong` |
| Ad | `02_LyricPlayerShort` |

Ad 01 is the 2:30 cut, ad 02 the 45s cut. Same ad set so the length test is clean.

---

# FORMAT 2: QuietDevotionSung (UGC)

## (a) Concept and what it tests

**Concept:** the competitor's white hook bar sits on top, exactly where theirs sits. Under
it is not a reaction but a FACELESS ordinary moment: a woman's hands and shoulder, one
earbud in, a phone face down on the table, the song's lyric captions carrying the name. The
raw phone look, the bad light, the lived-in room, the big captions. Everything the
competitor's format 2 does, with the face removed and the emotion moved into the caption.

**What it tests:** whether the account's one proven franchise mechanism transfers to this
product. LEARNINGS is explicit: AQuietDevotion is the account's only consistent winner, and
the mechanism is "a small, private, ordinary moment that already exists in her day, plus an
object that gives her hands something to do in it." The prayer song is the purest possible
version of that mechanism, because it gives the moment something to PLAY rather than
something to hold. The three scenes are the logged winning scenes.

It also tests the faceless constraint itself, which is reusable on every future digital
offer in this account.

Creative angle: Pain Point / Problem, resolved into Belonging. Emotion: recognition.

**Why faceless is a creative choice and not just a compliance dodge.** A face plus an
emotional beat plus a song will be read as a customer no matter what small print sits
underneath; the inference cannot be undone by a disclosure. Remove the face and two things
happen. The testimonial reading becomes impossible, and the viewer inserts herself into the
frame. For an audience who already prays for people by name, being the woman at the table
is stronger than watching one.

## (b) Layout and shot list

Canvas 1080 x 1350 (4:5).

| Element | x | y | Notes |
|---|---|---|---|
| Hook bar, cream block | 0 to 1080 | 0 to 310 | solid #F7F3EC, full bleed |
| Hook text (copywriter) | 64 to 1016 | 44 to 266 | max 3 lines, Inter SemiBold 48px, #2B2118, left aligned |
| Footage | 0 to 1080 | 310 to 1350 | the clip, cropped to fill |
| Lyric caption | 72 to 1008 | 1068 to 1196 | 1 to 2 lines, centred, white Inter SemiBold 56px, 4px dark shadow, advances with audio |
| Disclosure line (mandatory) | centred | 1240 to 1290 | 2 lines, 24px, white at 70%, centred |

Disclosure wording, fixed, not the copywriter's to change:
line 1 `An illustration made by Sanctoria. Not a customer.`
line 2 `A sample prayer song. Not a customer's song.`

No CTA inside the video frame; the Meta UI carries it. The 1:1 static cutdown gets the gold
bar at y 900 to 1000, x 140 to 940.

**Audio:** the grandchild protection song (`Angels Watching Over Nevaeh`, lullaby). Screen
its full transcript line by line before cutting. Enter on the instrumental intro so there is
sound on frame 1, but place the first lyric caption no later than 0:02.

**Timeline, 75s cut, three scenes:**

| Time | Scene | Lyric caption |
|---|---|---|
| 0:00 to 0:02 | A, BeforeTheHouseWakes | empty. Hook bar only. Hook must land inside 2s |
| 0:02 to 0:26 | A, looping | verse 1 |
| 0:26 to 0:30 | cross-dissolve A to B, 12 frames | the name, alone, 96px, 1.2s |
| 0:30 to 0:54 | B, SchoolCarPark, looping | chorus |
| 0:54 to 0:58 | cross-dissolve B to C, 12 frames | verse 2 first line |
| 0:58 to 1:15 | C, TheBedsideLamp, looping | verse 2, into the chorus, hold on the last line |

**Note on the three scenes.** LEARNINGS logs the winning AQuietDevotion scenes as before the
house wakes, the school car park and the driveway. I have swapped the driveway for a bedside
lamp. Reason: the driveway scene is also shot inside a parked car, so two of three variants
would look near identical in a feed and the format test would really be a one-scene test.
The bedside is named in the page copy ("At a bedside") and gives a third light source and a
third time of day. If literal fidelity to the logged scenes matters more, the driveway
prompt is a trivial edit of scene B: evening light, a house and porch light beyond the
windscreen, engine off.

**Casting across the set,** so the three do not read as one poster: scene A white, scene B
Hispanic, scene C Black. Faceless means this shows only in hands, forearms and hair.

## (c) Generation prompts

Pipeline, same as the proven page clips:
1. **Step A, the still.** `gpt_image_2_5`, aspect 4:5. Paste the still prompt whole.
2. **Step B, the motion.** `seedance_2_5`, image to video, the approved still as BOTH start
   and end image, 5 seconds, 4:5, audio off. Paste the motion prompt whole.

The LOOK and WHAT THIS IS NOT blocks below are the blocks from `sample-clip-prompts.md`
that generated cleanly on the first pass. Only the orientation sentence was changed, from
3:4 to 4:5, plus the no-face clauses. Do not edit them per scene or the set will drift.

**Approval checklist for every still in this format:**
- No face. No eyes, no mouth, no nose, no full cheek. The jaw and ear in profile are the
  most that may show, and only in scene A.
- Exactly one clearly visible hand, five fingers, natural knuckles and nails.
- The phone shows its blank back or its blank underside only. No screen visible anywhere.
- Background sharp, not blurred. Plain colour, no golden glow.
- One Catholic cue, small, in the background.
- No letters, numbers, icons or interface anywhere, including mugs, magnets, book spines
  and the Bible's cover and pages.
- The band at y 1068 to 1290 (the lower 17 percent) is calm and low in detail, because the
  caption and disclosure sit there.

### Scene A: BeforeTheHouseWakes

**Slug:** `wakes`. **Alt text:** A woman's hands at the kitchen table before dawn, one
earbud in, a song playing.

**The idea:** the house is still dark. She is up first, which is the only ten minutes of the
day that belong to her. The earbud is the whole mechanism: it says something is playing
without putting a screen in frame. Her face is out of the picture because the camera is
behind her shoulder, which is also the angle a family member would actually film from.

**Still prompt (Step A, `gpt_image_2_5`, 4:5):**

```
SCENE: An ordinary family kitchen before dawn, almost dark, lit by one small lamp. A white American woman about 62 sits at a worn wooden kitchen table, seen from BEHIND AND SLIGHTLY TO HER LEFT, so the camera looks over her left shoulder at the table in front of her. Her face is NOT visible: the camera sees the back and left side of her head, her grey hair pinned up in a loose clip with strands escaping at the nape, her ear, the line of her jaw in profile at the very edge of the frame, and her left shoulder in a soft pale dressing gown over a cotton nightdress. No eye, no mouth and no nose is visible from this angle. Her left hand rests flat on the table ahead of her, palm down, five fingers together and relaxed, the skin on the back of her hand loose and freckled with age spots, a plain thin wedding band on it. Her other arm is out of frame. A single small white wired earbud sits in her visible ear, and its thin pale cord falls down past her shoulder and across the table to a phone lying FACE DOWN and flat on the table beside her hand, so the camera sees only its plain dark back in a matte case with no logo and no markings. The phone is about as long as her hand from wrist to fingertip. Also on the table: one plain white mug with a little coffee left in it, a dark wooden rosary with small round matte black beads loosely coiled near her hand, and a small clear glass votive candle, lit, its flame small. SIZES, anchored to the frame: her visible hand spans about one quarter of the frame width. Each rosary bead is about one eightieth of the frame width. The candle flame is about one fiftieth of the frame height. Behind the table the kitchen is fully in focus and dim: a window above the sink showing a dark blue pre dawn sky with no sun, a dish rack with two plates, a refrigerator with a few plain coloured magnets and nothing pinned to it. High on the wall beside the window hangs one small plain wooden crucifix, about half the height of her visible hand as drawn, unlit and unremarkable, never the focus. CAMERA POSITION: filmed by someone standing a few feet behind her and a little to her left, phone held upright at chest height. She is seen from behind, head and shoulder in the upper left third of the frame, with the table top and her hand across the middle. THE LOWER SIXTH OF THE FRAME IS CALM AND LOW IN DETAIL: the near table edge and bare shadowed wood only, with no object, no bright spot and no busy pattern there, because captions will be placed over it. LIGHT: one warm kitchen lamp out of frame to the right, plus the small candle, and the faint cold blue of the window. The ceiling light is off. The room is genuinely dim, the shadows deep but still holding detail, and visibly grainy. LOOK: A single frame taken from an ordinary home video, filmed on a phone held upright by a family member in the same room. It must look like amateur family footage, not a professional photograph and not an advertisement. Phone camera character: a slightly wide lens and deep focus, so the person, the furniture and the back wall are all acceptably sharp at once, with no blurred background and no bokeh. Slightly flat contrast, ordinary automatic exposure, the lamp and the candle flame a little blown out, heavy fine sensor noise visible in the shadows because the room is dark, plain and slightly muted colour with the mixed white balance of a real room. Available light only, exactly as described above. No flash, no studio light, no rim light, no glow, no colour grade, no film look. Framing is imperfect the way a real handheld clip is: the picture tilted very slightly off level, the person a little off centre, something ordinary cutting into one edge of the frame. A real person, not a model: natural skin with pores, lines, age spots and uneven tone, unstyled hair, ordinary slightly worn clothes with no printing on them, a lived in home with everyday clutter. Anatomy is natural and correct. Every visible hand has five fingers with natural knuckles and nails. Portrait orientation, aspect ratio 4:5, full frame. WHAT THIS IS NOT: Her face is not visible and she never turns toward the camera. Nobody looks at the camera or is aware of it. Nobody speaks: no mouth is visible and none is open. Nobody poses, holds anything up, points, waves or gives a thumbs up. Quiet stillness only, with no tears, no hand over the face, no hand to the chest and no gesture of surprise, recognition or emotion of any kind. There is no text anywhere in the frame: no captions, no subtitles, no usernames, no social media interface, no record indicator, no timestamp, no battery or signal icons, no watermark, no logo, no star rating, no border, no black bars, and no writing on any object, packaging, magnet, mug, book spine, picture or clothing. The image is the raw camera picture only. It is not a screenshot, and no phone or hand is held up in the foreground. The only phone in the scene is the one described, lying face down, and its screen cannot be seen. No second person, no child, no animal. No priest, no nun, no church, no hospital, no medical equipment, no pills, no wheelchair, no walking frame, no sick bed. No halos, no light rays, no glowing figures. Not cinematic, not an illustration, not a painting, not a 3D render.
```

**Negative prompt:**

```
face, eyes, mouth, nose, cheek, portrait, front view, looking at camera, turning around, smiling, crying, tears, hand over face, hand on chest, emotional gesture, second person, child, pet, text, letters, numbers, words, caption, logo, watermark, signage, UI, button, border, frame, black bars, phone screen, visible screen, screen glow, bright phone, studio lighting, flash, softbox, bokeh, blurred background, shallow depth of field, oversaturated, HDR, glossy, cinematic, illustration, painting, 3D render, cartoon, plastic skin, airbrushed skin, young woman, model, extra fingers, deformed hands, halo, light rays, glowing figure, church, priest, hospital, medical equipment, bright or busy lower sixth, daylight, sunny, sunrise glow
```

**Motion prompt (Step B, `seedance_2_5`, 5 seconds, 4:5, no audio):**

```
Continue the supplied image as one unbroken amateur phone video, 5 seconds, real time, silent. CAMERA: held upright in the hand by someone standing still. It barely moves: only a faint natural sway and breathing drift, never more than one fiftieth of the frame width, with the framing otherwise unchanged. ACTION: She breathes slowly, so her shoulder rises and falls very slightly twice. Her flat hand on the table stays exactly where it is, and once, very slowly, her index and middle fingers lift about the width of a fingernail and settle back down, the smallest keeping of time. A few loose strands of hair at her nape stir faintly. The candle flame flickers gently. NOTHING ELSE MOVES: the phone, the earbud cord, the mug, the rosary and everything in the kitchen stay perfectly still in exactly their starting positions. MUST NOT HAPPEN: Her face does not become visible at any point. She does not turn her head toward the camera, turn around, look back, stand up or lean. No mouth appears and nobody speaks, sings, mouths words, laughs or sighs audibly. She does not raise a hand to her face, to her chest or to her ear, does not wipe an eye, does not cry, and makes no gesture of surprise, recognition or emotion. Her hand does not pick anything up, put anything down or move across the table. No new person, hand, object or animal enters the frame. Nothing in the room appears, disappears, moves or changes. The phone does not move, turn over, light up or show its screen. The earbud does not fall out. No text, captions, subtitles, icons, logos or watermark appear at any point. No zoom, no push in, no pull back, no pan, no orbit, no refocus. No scene change, no cut, no fade, no change of light or colour beyond the flame's own flicker, no slow motion, no speed change, no added background blur. The window does not brighten and no sunrise appears. Hands keep five fingers and their natural shape throughout. LOOP: by the last frame she, the flame and the camera have settled back to exactly where they were in the first frame, so the clip repeats without a visible jump. Silent, no audio.
```

### Scene B: SchoolCarPark

**Slug:** `carpark`. **Alt text:** A woman's hands on the steering wheel while she waits at
the school gate, a song playing.

**The idea:** the ten minutes of waiting in the car before the children come out. Dead time
that already exists in her day. The phone is clipped to the air vent facing her, so the
camera behind her right shoulder sees only its blank back. Her hands are at the bottom of
the wheel, which is where hands actually rest while waiting, and it keeps both of them in
one simple shape.

**Still prompt (Step A, `gpt_image_2_5`, 4:5):**

```
SCENE: The inside of an ordinary older family car, parked and switched off, on a grey weekday afternoon. A Hispanic American woman about 58 sits in the driver's seat, seen from BEHIND HER RIGHT SHOULDER from the back seat, so the camera looks forward past her at the windscreen. Her face is NOT visible: the camera sees the back of her head, dark hair streaked with grey gathered in a low twist, the curve of her right shoulder in a plain navy cardigan, and a sliver of her right cheek edge at most. No eye, no mouth and no nose is visible from this angle. Her right hand rests on the lower right of the steering wheel, fingers curled loosely over the rim, five fingers, the skin a little weathered, a plain thin ring on one finger. Her left hand is on the lower left of the wheel and mostly hidden behind the wheel's rim and her own forearm. A single small white wired earbud sits in her right ear, its thin pale cord falling down past her shoulder toward a phone clipped to the car's central air vent, angled to face her, so the camera behind her sees only the phone's plain dark back in a matte case with no logo and no markings. The phone is about as long as her hand from wrist to fingertip. On the passenger seat beside her: a cloth shopping bag slumped over, a folded grey cardigan. Hanging from the rear view mirror, one small dark wooden rosary with small round matte black beads, swaying slightly, about one eighth of the frame height long. SIZES, anchored to the frame: her visible hand spans about one fifth of the frame width. Each rosary bead is about one hundredth of the frame width. Through the windscreen, fully in focus: an ordinary school pick up kerb on an overcast day, a low chain link fence, a strip of grass, the plain brick end wall of a school building, two other parked cars, bare trees, and no people. CAMERA POSITION: filmed by someone sitting in the back seat behind the passenger side, phone held upright at chest height. She is seen from behind, her head and shoulder filling the left half of the frame, the windscreen and the wheel across the middle. THE LOWER SIXTH OF THE FRAME IS CALM AND LOW IN DETAIL: the dark plastic of the lower dashboard, the bottom of the steering wheel and shadowed seat fabric only, with no object, no bright spot and no busy pattern there, because captions will be placed over it. LIGHT: flat grey overcast daylight through the windscreen and side windows only. No sun, no sunbeam, no lens flare. The car's interior lights are off. Shadows are open, soft and a little grainy. LOOK: A single frame taken from an ordinary home video, filmed on a phone held upright by a family member in the same car. It must look like amateur family footage, not a professional photograph and not an advertisement. Phone camera character: a slightly wide lens and deep focus, so the person, the car interior and the view through the windscreen are all acceptably sharp at once, with no blurred background and no bokeh. Slightly flat contrast, ordinary automatic exposure, the windscreen a little blown out, fine sensor noise visible in the shadows, plain and slightly muted colour with the mixed white balance of a real car. Available light only, exactly as described above. No flash, no studio light, no rim light, no glow, no colour grade, no film look. Framing is imperfect the way a real handheld clip is: the picture tilted very slightly off level, the person a little off centre, something ordinary cutting into one edge of the frame. A real person, not a model: natural skin with pores, lines, age spots and uneven tone, unstyled hair, ordinary slightly worn clothes with no printing on them, a lived in car with everyday clutter. Anatomy is natural and correct. Every visible hand has five fingers with natural knuckles and nails. Portrait orientation, aspect ratio 4:5, full frame. WHAT THIS IS NOT: Her face is not visible and she never turns toward the camera. Nobody looks at the camera or is aware of it. Nobody speaks: no mouth is visible and none is open. Nobody poses, holds anything up, points, waves or gives a thumbs up. Quiet stillness only, with no tears, no hand over the face, no hand to the chest and no gesture of surprise, recognition or emotion of any kind. There is no text anywhere in the frame: no captions, no subtitles, no usernames, no social media interface, no record indicator, no timestamp, no battery or signal icons, no watermark, no logo, no star rating, no border, no black bars, and no writing on any object, no number plate, no road sign, no school sign, no shop sign, no sticker, no dashboard lettering and no printing on any clothing. The image is the raw camera picture only. It is not a screenshot, and no phone or hand is held up in the foreground. The only phone in the scene is the one described, and its screen cannot be seen from where the camera is. No second person, no child, no animal, and nobody visible through the windscreen or the windows. No priest, no nun, no church, no hospital, no medical equipment. No halos, no light rays, no glowing figures. Not cinematic, not an illustration, not a painting, not a 3D render.
```

**Negative prompt:**

```
face, eyes, mouth, nose, cheek, portrait, front view, looking at camera, turning around, rear view mirror reflection of face, smiling, crying, tears, hand over face, hand on chest, emotional gesture, second person, child, pedestrian, pet, text, letters, numbers, words, caption, number plate, road sign, school sign, logo, watermark, signage, UI, button, border, frame, black bars, phone screen, visible screen, screen glow, dashboard lights, studio lighting, flash, bokeh, blurred background, shallow depth of field, oversaturated, HDR, glossy, cinematic, sunbeam, lens flare, golden hour, illustration, painting, 3D render, cartoon, plastic skin, young woman, model, extra fingers, deformed hands, halo, light rays, bright or busy lower sixth
```

**Motion prompt (Step B, `seedance_2_5`, 5 seconds, 4:5, no audio):**

```
Continue the supplied image as one unbroken amateur phone video, 5 seconds, real time, silent. CAMERA: held upright in the hand by someone sitting still in the back seat. It barely moves: only a faint natural sway and breathing drift, never more than one fiftieth of the frame width, with the framing otherwise unchanged. ACTION: She breathes slowly, so her shoulder rises and falls very slightly twice. Her right hand stays curled on the wheel, and once her thumb taps the rim twice, very lightly, keeping time, then rests again exactly where it began. The rosary hanging from the mirror sways gently through a small arc and returns. A few loose strands of her hair stir faintly. NOTHING ELSE MOVES: the phone, the earbud cord, the bag, the cardigan, the car and everything beyond the windscreen stay perfectly still. MUST NOT HAPPEN: Her face does not become visible at any point. She does not turn her head toward the camera, turn around, look back, check the mirror, lean or get out. Her face does not appear reflected in the rear view mirror, the windscreen or any window. No mouth appears and nobody speaks, sings, mouths words, laughs or sighs audibly. She does not raise a hand to her face, to her chest or to her ear, does not wipe an eye, does not cry, and makes no gesture of surprise, recognition or emotion. Her hands do not leave the wheel. The car does not start, move or roll. No new person, hand, object or animal enters the frame, and nobody walks past or appears through the windscreen or the windows. Nothing in the car appears, disappears or changes. The phone does not move, light up or show its screen. The earbud does not fall out. No text, captions, subtitles, icons, logos or watermark appear at any point. No zoom, no push in, no pull back, no pan, no orbit, no refocus. No scene change, no cut, no fade, no change of light or colour, no sun breaking through, no slow motion, no speed change, no added background blur. Hands keep five fingers and their natural shape throughout. LOOP: by the last frame she, the rosary and the camera have settled back to exactly where they were in the first frame, so the clip repeats without a visible jump. Silent, no audio.
```

### Scene C: TheBedsideLamp

**Slug:** `bedside`. **Alt text:** A hand resting on an open Bible on a bedside table at
night, a song playing.

**The idea:** the last ten minutes of the day. This is the most faceless of the three: no
head at all, only a forearm and a hand entering the frame. That makes it the safest variant
and also the one most likely to be mistaken for genuine phone footage, because framing this
badly is something only a real person does.

**Still prompt (Step A, `gpt_image_2_5`, 4:5):**

```
SCENE: A bedside table in an ordinary bedroom late at night, lit by one small lamp. A Black woman's left forearm and hand enter the frame from the lower right, reaching across to rest on an open book that lies on the table. Her face, head, shoulder and body are NOT in the frame at all: the camera sees only her forearm from about the middle of the forearm to the fingertips. The sleeve of a soft dark dressing gown covers her arm to just below the elbow. Her hand rests flat and open on the left hand page of the open book, palm down, five fingers slightly spread and relaxed, the skin on the back of her hand showing natural texture, raised veins and a plain thin wedding band. The open book is a well worn Bible with soft rounded corners, a dark leather cover, and thin gilt edged pages, open near the middle. ITS PAGES ARE SEEN AT A SHALLOW ANGLE AND ARE COMPLETELY BLANK AND OFF WHITE, with no printing, no lines of type, no words, no letters, no numbers, no headings and no page numbers visible anywhere, and its cover shows no lettering of any kind. Also on the table: a small lamp with a warm fabric shade at the left edge of the frame, partly cut off; a plain white mug; a small clear glass votive candle, lit, its flame small; a dark wooden rosary with small round matte black beads, loosely coiled; and a phone lying FACE DOWN and flat beside the book, so the camera sees only its plain dark back in a matte case with no logo and no markings, with a thin pale earbud cord trailing from it off the edge of the table into darkness. SIZES, anchored to the frame: her hand spans about one third of the frame width. The open book spans about two thirds of the frame width. Each rosary bead is about one eightieth of the frame width. The candle flame is about one fiftieth of the frame height. Behind the table, fully in focus but dim: a plain painted bedroom wall, the corner of a bed with a rumpled dark blanket, and one small plain wooden crucifix hanging on the wall, about half the length of her hand as drawn, unlit and unremarkable, never the focus. CAMERA POSITION: filmed by someone standing beside the bed holding a phone upright and looking down at the table at about forty five degrees, close in, about two feet away. The table top fills most of the frame. THE LOWER SIXTH OF THE FRAME IS CALM AND LOW IN DETAIL: bare shadowed table wood and dark blanket only, with no object, no bright spot and no busy pattern there, because captions will be placed over it. LIGHT: one warm lamp at the left edge of frame plus the small candle, everything else in the room dark. The ceiling light is off. The pool of light falls across the book and her hand, and the shadows go deep but still hold detail, visibly grainy. LOOK: A single frame taken from an ordinary home video, filmed on a phone held upright by a family member in the same room. It must look like amateur family footage, not a professional photograph and not an advertisement. Phone camera character: a slightly wide lens and deep focus, so the hand, the table and the back wall are all acceptably sharp at once, with no blurred background and no bokeh. Slightly flat contrast, ordinary automatic exposure, the lamp shade and the candle flame a little blown out, heavy fine sensor noise visible in the shadows because the room is dark, plain and slightly muted colour with the mixed white balance of a real room. Available light only, exactly as described above. No flash, no studio light, no rim light, no glow, no colour grade, no film look. Framing is imperfect the way a real handheld clip is: the picture tilted very slightly off level, the hand a little off centre, something ordinary cutting into one edge of the frame. A real person's hand, not a model's: natural skin with pores, lines, raised veins, knuckle creases and uneven tone, no manicure. Anatomy is natural and correct. The hand has five fingers with natural knuckles and nails. Portrait orientation, aspect ratio 4:5, full frame. WHAT THIS IS NOT: No face, head, hair, shoulder or torso is visible anywhere in the frame. Only one forearm and one hand. Nobody looks at the camera or is aware of it. Nobody speaks. The hand does not point, wave, give a thumbs up, clasp in prayer, press to a chest or hold anything up. Quiet stillness only, with no gesture of surprise, recognition or emotion. There is no text anywhere in the frame: no captions, no subtitles, no usernames, no social media interface, no record indicator, no timestamp, no battery or signal icons, no watermark, no logo, no star rating, no border, no black bars, and no writing, printing or lettering on the book's pages, on the book's cover, on the mug, on any picture or on any object. The Bible's pages are blank. The image is the raw camera picture only. It is not a screenshot, and no phone or hand is held up in the foreground. The only phone in the scene is the one described, lying face down, and its screen cannot be seen. No second person, no child, no animal. No priest, no nun, no church, no hospital, no medical equipment, no pills, no sick bed. No halos, no light rays, no glowing figures, no shaft of light on the book. Not cinematic, not an illustration, not a painting, not a 3D render.
```

**Negative prompt:**

```
face, head, hair, shoulder, torso, person, portrait, two hands, praying hands, clasped hands, pointing, thumbs up, text, letters, numbers, words, printed page, lines of type, page numbers, book title, lettering on cover, caption, logo, watermark, signage, UI, button, border, frame, black bars, phone screen, visible screen, screen glow, studio lighting, flash, softbox, bokeh, blurred background, shallow depth of field, oversaturated, HDR, glossy, cinematic, illustration, painting, 3D render, cartoon, plastic skin, airbrushed skin, manicure, young hand, model hand, extra fingers, deformed hands, halo, light rays, glowing figure, shaft of light, church, priest, hospital, medical equipment, pills, bright or busy lower sixth, daylight, window light
```

**Motion prompt (Step B, `seedance_2_5`, 5 seconds, 4:5, no audio):**

```
Continue the supplied image as one unbroken amateur phone video, 5 seconds, real time, silent. CAMERA: held upright in the hand by someone standing still. It barely moves: only a faint natural sway and breathing drift, never more than one fiftieth of the frame width, with the framing otherwise unchanged. ACTION: The hand resting on the open book stays where it is. Once, very slowly, its fingers press down a fraction and relax again, the smallest settling. The candle flame flickers gently, and the pool of warm light it throws across the page breathes very slightly with it. NOTHING ELSE MOVES: the book, its pages, the phone, the earbud cord, the mug, the rosary, the lamp and the bed stay perfectly still in exactly their starting positions. MUST NOT HAPPEN: No face, head, hair, shoulder or torso appears at any point. No second hand enters the frame. The hand does not lift off the book, slide, turn over, point, wave, clasp, press to anything or pick anything up. The book's pages do not turn, lift, curl or show any printing, and no words, letters or numbers appear on them at any point. No new person, hand, object or animal enters the frame. Nothing in the room appears, disappears, moves or changes. The phone does not move, turn over, light up or show its screen. No text, captions, subtitles, icons, logos or watermark appear at any point. No zoom, no push in, no pull back, no pan, no tilt, no orbit, no refocus. No scene change, no cut, no fade, no change of light or colour beyond the flame's own flicker, no slow motion, no speed change, no added background blur. The candle does not go out and does not flare up. The lamp does not brighten or dim. The hand keeps five fingers and its natural shape throughout. LOOP: by the last frame the hand, the flame and the camera have settled back to exactly where they were in the first frame, so the clip repeats without a visible jump. Silent, no audio.
```

## (d) Honesty verdict

**Works with generated footage, but ONLY with the two line disclosure burned into the
creative, and only because the footage is faceless and carries no reaction beat.**

The reasoning matters more than the verdict. A disclosure does not make a reaction shot
honest. If a face listens to a song and is visibly moved, the viewer concludes a customer
was filmed, and no small print at the bottom of the frame reverses that conclusion. So the
disclosure is not what makes this format acceptable. Three structural choices are:

1. **No face.** There is no person who could be the customer.
2. **No reaction beat.** The specified motion is breathing, a thumb keeping time, a candle.
   No tears, no hand to the face, no hand to the chest, no moment of recognition. The clip
   illustrates a moment of prayer, not a response to a purchase.
3. **The emotional load sits in the lyric caption,** which is real product, verbatim.

With those three in place the creative asserts only "this is the kind of moment this is
for", which is exactly what the sales page already says about the same footage, in almost
the same words. The disclosure then does its proper, narrow job: it stops a viewer assuming
the woman ordered one.

**A face version is permissible** under the project rule, with disclosure, and I advise
against it for batch 1. It buys scroll-stop and spends the one thing this offer has instead
of proof, which is that nothing on the page or in the ads is pretending.

## (e) Naming

| Level | Name |
|---|---|
| Campaign | `QuietDevotionSung_UGC_2026-10-08` |
| Ad Set | `T1_MF_45-65+_QuietDevotionSung_UGC_BeforeTheHouseWakes` |
| Ad | `01_BeforeTheHouseWakes` |
| Ad | `02_SchoolCarPark` |
| Ad | `03_BedsideLamp` |

AngleName traces to the logged `AQuietDevotion` franchise. One ad set, three ads, so the
three scenes pool into one mechanism verdict instead of three invalid ones.

---

# FORMAT 3: TheNameGoesIn (SCR)

## (a) Concept and what it tests

**Concept:** two lines of setup text, exactly where the competitor puts their meme setup.
Underneath, instead of a deadpan face, a screen recording of the REAL form at
/prayer-song/: the relationship pill tapped, then a first name typed into the box one
letter at a time, then the intention pill tapped. The held beat is the cursor blinking after
the last letter. Then the song enters and that exact name is sung in the chorus.

**What it tests:** the sharpest curiosity mechanic available to this offer. The competitor's
meme format withholds a punchline; this withholds a sound. A viewer who watches a name get
typed has an open loop that only the chorus can close.

It is also the most congruent creative possible. The ad shows the literal first thing she
will do after the click, so the landing page cannot disappoint the expectation the ad set.
Congruence is the cheapest conversion lever available to an offer with no proof.

Creative angle: Curiosity / Open Loop, with Mechanism underneath. Emotion: curiosity into
surprise.

## (b) Layout and shot list

Canvas 1080 x 1350 (4:5). Zero generated assets.

| Element | x | y | Notes |
|---|---|---|---|
| Setup bar, cream block | 0 to 1080 | 0 to 340 | solid #F7F3EC, full bleed |
| Setup line 1 (copywriter) | 64 to 1016 | 54 to 170 | 1 to 2 lines, Inter SemiBold 46px, #2B2118, left aligned |
| Setup line 2 (copywriter) | 64 to 1016 | 186 to 302 | 1 to 2 lines, Inter 44px, #5A4A38, left aligned, visually subordinate |
| Screen recording | 0 to 1080 | 340 to 1140 | the form card region, cropped and scaled to 1080 wide |
| Payoff caption band | 72 to 1008 | 1164 to 1288 | 1 to 2 lines, centred, white Inter SemiBold 54px on a #2B2118 bar, enters only when the song enters |
| Label (mandatory) | centred | 1306 to 1338 | 22px, cream at 70% |

Label wording, fixed: `A sample prayer song made by Sanctoria. Not a customer's song.`

**Audio:** `creative/test-songs/demo_Lead_Daniel_Home.mp3`. Silent until 0:12. The silence
is the format's main weapon: a muted-looking ad that suddenly has a voice in it.

**Timeline, 35s:**

| Time | Screen | Audio | Caption |
|---|---|---|---|
| 0:00 to 0:02 | the form's step 1, pills visible, nothing selected | silent | setup bar only. Hook lands inside 2s |
| 0:02 to 0:05 | the "a son" pill is tapped, its state changes | silent | none |
| 0:05 to 0:11 | the name field focuses, D A N I E L typed one letter at a time, about one letter per 0.8s | silent | none |
| 0:11 to 0:12 | **hold. Cursor blinking after the L. Nothing else moves.** | silent | none |
| 0:12 to 0:16 | screen holds, very slow 2 percent push in only | the chorus enters, mid phrase, at full volume | the lyric line appears, with the word Daniel set in amber #F2C230 |
| 0:16 to 0:30 | the intention pill "a return to the faith" is tapped, then step 3's style pills | chorus continues | lyric lines advance |
| 0:30 to 0:35 | hold on the completed step | chorus resolves | final lyric line, then the label alone |

**Recording brief.** Record on a real phone at 1080 wide, portrait, on the live page at
https://sanctoriastore.com/prayer-song/ . Then:

- Crop to the form card only. Do not show the browser chrome, the URL bar, the clock, the
  battery or the signal icons. Those are the things that make a screen recording read as
  software rather than as the product.
- Use the name **Daniel**, which is the page's own sample name and matches the audio.
- Type at a human pace, about one letter every 0.8 seconds, with one small hesitation
  before the last letter. A machine-fast type kills the format.
- **Never record a real buyer's name, email or lead data.** Use the fictional sample only.
  If the live form is in its soft state, record it anyway; nothing about the form's checkout
  state appears in the crop.
- Keep the finger out of frame. A visible thumb invites the viewer to read the hand as a
  real customer's, which is the one inference this format is built to avoid.

**9:16 cutdown:** setup bar 0 to 520, recording 520 to 1400, caption band 1430 to 1610,
label at 1660. All inside the Reels safe area.

**1:1 static cutdown (per the standing square + CTA rule):** 1080 x 1080. Setup bar 0 to
300. A freeze of the typed name field, 300 to 760. Gold CTA bar #F2C230 at y 860 to 960,
x 140 to 940. Label at y 1040. This is the one static in the batch and it is the cheapest
asset of all: one screenshot and two bars.

## (c) Generation prompts

**None. This format requires no generation of any kind.** That is the point of including it:
it is a one hour build, it carries zero AI-imagery risk, zero compliance exposure on a human
likeness, and it can be rebuilt for any name, any intention and any style in minutes once
the recording exists. If the batch has to ship tomorrow, this is the one that ships.

For the 1:1 static's background, if a plate is wanted behind the field instead of flat cream,
reuse Format 1's photographed or generated tabletop plate. No second asset.

## (d) Honesty verdict

**Works fully, with nothing we do not already have. No human, no generated footage, no
disclosure beyond the sample label.**

Every frame is the real product: the real form, the real pills, the real field, a real
rendered song, its real lyrics. The one invented element is the name Daniel, which is the
sample name already published on the page and labelled there. Nothing is asserted that the
viewer cannot verify by clicking through and typing a name themselves, which is precisely
what the ad is asking them to do.

## (e) Naming

| Level | Name |
|---|---|
| Campaign | `TheNameGoesIn_SCR_2026-10-08` |
| Ad Set | `T1_MF_45-65+_TheNameGoesIn_SCR_NameTyped` |
| Ad | `01_NameTyped` |
| Ad | `02_NameTypedStatic` |

Ad 02 is the 1:1 static. `SCR` is a new format code to log in LEARNINGS.md.

---

# WHAT GENUINELY REQUIRES FOOTAGE WE DO NOT HAVE

One thing, and it is the competitor's entire engine: **a real recipient hearing their own
name sung for the first time.** No generated clip can substitute for it honestly, and the
honest substitutes in this batch (the song, the lyric, the name typed) are evidence of
quality, not evidence of effect on a human being. That second thing is a different and more
powerful claim, and batch 1 simply cannot make it.

It is acquirable, cheaply, and it should be treated as the batch 2 unlock:

1. Add one line to the delivery email that goes to every buyer: an offer to feature their
   song, and an invitation to send a phone clip of the moment it was played, with a written
   release for ads and the page.
2. Ask for the release explicitly and in plain words. A clip with no release is unusable and
   collecting it is the whole point.
3. Twenty buyers is enough. The competitor runs about 1,000 ads on a handful of clips.
4. The first real clip that arrives is worth more than every generated frame in this brief,
   because it unlocks the one format Sanctoria currently cannot run, and it also unlocks the
   proof block the sales page is deliberately holding empty.

Until then, the batch's honest position is strong on its own terms: the product can be heard
before it is bought. Very few $39 offers can say that.

---

# BATCH STRUCTURE AND LAUNCH

## Hold copy constant. Test only creative.

The competitor runs ONE headline and ONE body across roughly 1,000 ads. That is not laziness,
it is a deliberate design: they have isolated creative as the only variable and they iterate
it forever. Batch 1 should copy the method, not just the formats.

So: the copywriter supplies ONE primary text and ONE headline, and the identical pair runs on
all three formats and all seven ads. Targeting is identical too, T1 MF 45-65+ across every
ad set. The only thing that differs between ad sets is the format. Anything else and the
batch answers no question at all.

## Judge at the mechanism level, not per ad

LEARNINGS is unambiguous on this account: $15 buys about 12 outbound clicks, and at the
account's own conversion rate an ad performing exactly at average shows zero sales 69 percent
of the time. Roughly 75 outbound clicks are needed for a real verdict. Every single kill in
this account has had good CTR and no sale, across about 20 ad sets.

So do not sequence the three formats as single $15 tests. Run all three concurrently and
judge the batch on pooled outbound clicks:

- Do not kill any format before about **75 outbound clicks on that format.**
- Read the batch at about **225 pooled outbound clicks.**
- Measure outbound clicks, not clicks. Only 31 to 51 percent of Meta's counted clicks on
  this account have been outbound; the rest are photo expands and "see more" taps. Which is
  also why the copywriter should be told to keep the primary text short and unbroken:
  long line-broken copy cost one ad set 69 percent of its clicks.

## The economics are not the bracelet's

The bracelet account ran at 0.67x Meta ROAS on a product that only survived through a $17
rebill. This offer is different in kind. At $39 with a render cost of about $0.59 and
ClickBank's cut, contribution per sale is roughly $35, so break-even sits near **1.1x
reported ROAS**. Treat that as the line, confirm the exact ClickBank fee before setting
rules, and do not import the bracelet's thresholds. A format reading 1.4x here is working,
where the same number on the bracelet was not.

## Build rules

Per the standing project rules: campaign PAUSED, ad set and ads ACTIVE underneath,
$5/day (`daily_budget=500`), `start_time` = build date + 2 days at 03:00 Asia/Singapore.
TS turns the campaign on. Nothing ships without this exact `url_tags` string:

```
utm_source={{site_source_name}}&utm_medium={{placement}}&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&cmc_adid=fb_{{ad.id}}
```

**Blocker:** /prayer-song/ has no ClickBank checkout link and no cron job yet. Ads can be
built and left paused, but there is nothing to buy at the other end. The checkout, the cron,
a `--live` build and a real test purchase all have to land before the campaign is turned on.

## Ranking: where the money goes first

**1. QuietDevotionSung (UGC).** Highest ceiling, and the only one carrying a mechanism this
account has already proven pays. It is also the only format that keeps the competitor's
actual scroll-stop, a real-looking home with a human presence in it, which is what their
roughly 1,000 ads are spending to defend. Facelessness is what makes that available honestly.
Most expensive to build (three stills, three loops) and worth it.

**2. LyricPlayer (VID).** The control, and the most valuable single thing to learn. If the
song alone can carry an ad with no human in frame, every future creative for this product
gets cheaper, faster and safer, and the offer stops depending on footage it does not have.
Build it second because it is near free: one photograph of a sheet already in the repo, one
candle loop, one static card, and it then takes any song at any length.

**3. TheNameGoesIn (SCR).** Sharpest hook, weakest clothing. A form on a screen is a
software aesthetic and this audience is not a software audience, so expect the lowest
scroll-stop of the three. Rank it third on expected performance, build it FIRST on expected
effort, because it needs no generation and costs about an hour. It is the cheap third leg
that makes the pooled read possible.

**The ranking is a budget weighting, not a sequence.** Launch all three together, split
roughly 40 / 35 / 25, and read them against pooled outbound clicks. Sequencing them as
single $15 tests is the exact mistake the account has already made about twenty times.

---

# FLAGS FOR TS AND THE COPYWRITER

1. **Exclude the Siobhan song from all ads.** Its verified transcript carries health-claim
   language. Page only.
2. **Screen the Daniel and Nevaeh transcripts line by line** before any caption is cut.
   Only Siobhan's has been checked.
3. **The live page carries an invented anchor.** `PRICE_BADGE: 70% off today` and
   `PRICE_WAS: $129` contradict PRODUCT-BIBLE.md, which states "No 'was' price" and "No
   anchor invented". Ad claims must match the landing page, so this needs a decision before
   launch: either the anchor goes, or the bible changes. It is also the only fabricated
   figure on an otherwise scrupulously honest page.
4. **The competitor's strongest offer-panel line is "and you keep it."** It is available to
   Sanctoria truthfully if the private song page stays live after a refund. TS needs to
   confirm that behaviour, and the copywriter needs the answer before writing Format 1's
   Panel B.
5. **Largest untested fit in the account, for batch 2.** LEARNINGS flags that across about
   40 ads, exactly one headline has referenced Mary, Mother, intercession or a novena, while
   the VOC file's pain point #10 is asking God directly and feeling unheard. This product
   ships a Nine Day Prayer Companion. That is a Marian intercession angle sitting unused on
   a product built to carry it.
6. **Log the new format code `SCR`** in LEARNINGS.md so winners trace by format.
