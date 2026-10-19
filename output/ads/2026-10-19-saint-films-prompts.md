# Saint Films: image and motion prompts (Your Prayer Song)

Date: 2026-10-19. Status: **prompts only, nothing generated.** Generating the 15 stills and 15 clips needs a costed brief and TS's GO.

Look cloned from `output/ads/2026-10-16-oil-devotional/` (hero: `P2_SaintCecilia.png`, the only Prayer Song ad with a sale; `SaintCecilia_VID_FeastDay` also leads the batch on CTR). Each film is 28 seconds: 5 clips at about 5.6s, 3 new figure clips plus 2 existing generic clips. Video model: Higgsfield Happy Horse Video, image-to-video, about 5s each.

These are illustrations of saints and biblical figures. They are never presented as customers, and no ad built on them may claim a real or human singer.

Machine-readable copy: `output/ads/2026-10-19-saint-films-prompts.json`.

## Shared style anchor (already appended to every still prompt)

> Classical Baroque 17th-century academic religious oil painting on canvas, in the manner of the Italian and Spanish devotional masters, warm candle-and-gold chiaroscuro light, deep dark umber background, soft luminous golden halo, rich lapis blue, crimson and ochre drapery, visible brushwork, glazed skin tones, fine craquelure across the whole surface, museum-quality aged varnish, portrait 4:5 composition. No text, no lettering, no inscriptions, no signature, no frame, no border, no modern objects, no logos.

## Shared negative prompt

> text, lettering, letters, words, writing, inscription, legible script, readable musical notation, numbers, signature, watermark, logo, picture frame, border, modern clothing, modern objects, electric light, photograph, photorealistic photo, 3D render, CGI, anime, cartoon, digital painting look, plastic skin, airbrushed, oversaturated neon colours, looking at the viewer, eye contact with camera, extra fingers, fused fingers, deformed hands, extra limbs, distorted face, blood, wounds, stigmata wounds, gore, violence, weapons raised, nudity, cropped head, blurry, low resolution

## Shared motion clause (already appended to every motion prompt)

> Keep it a still classical oil painting throughout with brushwork and craquelure intact, one continuous shot with no cuts, no new figures entering, faces and hands keep their exact features with no morphing.

## Generic clip allocation

| Film | Generic pair | Clip order (slot 1 to 5) |
|---|---|---|
| Gregory | M7_MonksChanting + M3_MaryCrowned | G1_GregoryDove > M7_MonksChanting > G2_GregoryChoirBook > M3_MaryCrowned > G3_GregoryPrayer |
| Hildegard | M2_AngelChoir + M5_MaryListening | H3_HildegardLivingLight > M2_AngelChoir > H1_HildegardTablet > M5_MaryListening > H2_HildegardChapel |
| Francis | M1_MaryInPrayer + M2_AngelChoir | F1_FrancisBrotherSun > M1_MaryInPrayer > F2_FrancisBirds > M2_AngelChoir > F3_FrancisSunlitFace |
| David | M7_MonksChanting + M1_MaryInPrayer | D2_DavidCrownedPsalmist > M7_MonksChanting > D1_DavidBeforeSaul > M1_MaryInPrayer > D3_DavidHarpHands |
| Magnificat | M2_AngelChoir + M3_MaryCrowned | MG3_MaryInSong > M2_AngelChoir > MG1_Visitation > M3_MaryCrowned > MG2_MaryArmsLifted |

Every pair is unique; M4, M6 and M8 are not used. Pattern: strongest figure clip first, generic clips in slots 2 and 4 as breathers, a figure clip closes. Magnificat avoids M1 and M5 so its new Mary clips are not cut against near-identical frontal Madonnas.


---

## Film: Gregory

Saint Gregory the Great, pope and Doctor of the Church, namesake of Gregorian chant.

| Level | Name |
|---|---|
| Campaign | `SaintGregory_VID_YYYY-MM-DD` |
| Ad Set | `T1_MF_35-65+_SaintGregory_VID_GregoryDove` |
| Ad | `01_GregoryDove` |

AngleName `SaintGregory` is new; log it in LEARNINGS.md and ANGLE_LEDGER.md at launch. One campaign per angle, to avoid the drift flagged on 2026-10-18. Date = launch date.

**Clip order:** G1_GregoryDove > M7_MonksChanting > G2_GregoryChoirBook > M3_MaryCrowned > G3_GregoryPrayer


### G1_GregoryDove

- **Film:** Gregory
- **Aspect ratio:** 4:5
- **Image model:** GPT Image 2.5 (Higgsfield). Multi-element scene (desk, quill, dove at the ear, tiara); GPT Image holds layout and object logic best.

**Still prompt**

```
Saint Gregory the Great seated at a heavy carved oak desk in a dim papal study, an elderly bearded pope in a white alb, a rich crimson and gold-embroidered cope and a white skullcap, the papal tiara resting on the desk beside him. A small radiant white dove, the Holy Spirit, hovers just at his right ear with wings half spread, glowing softly. He holds a goose quill poised above a blank sheet of cream parchment, his eyes lowered and turned slightly toward the dove as if listening. A single beeswax candle and a shaft of warm gold light fall from the upper left across his face and hands; heavy books with plain leather spines stacked in shadow behind. Soft gold halo around his head, deep umber background. Classical Baroque 17th-century academic religious oil painting on canvas, in the manner of the Italian and Spanish devotional masters, warm candle-and-gold chiaroscuro light, deep dark umber background, soft luminous golden halo, rich lapis blue, crimson and ochre drapery, visible brushwork, glazed skin tones, fine craquelure across the whole surface, museum-quality aged varnish, portrait 4:5 composition. No text, no lettering, no inscriptions, no signature, no frame, no border, no modern objects, no logos.
```

**Negative prompt:** shared negative (above).

**Motion prompt**

```
Slow gentle push-in toward Gregory's face and the dove; the dove's wings flutter very softly in place, the candle flame flickers and the quill trembles slightly as his lips move as if murmuring a chant. Keep it a still classical oil painting throughout with brushwork and craquelure intact, one continuous shot with no cuts, no new figures entering, faces and hands keep their exact features with no morphing.
```

### G2_GregoryChoirBook

- **Film:** Gregory
- **Aspect ratio:** 4:5
- **Image model:** GPT Image 2.5 (Higgsfield). Group scene with a pope plus several monks around a lectern; GPT Image keeps figure count and hands cleaner.

**Still prompt**

```
Saint Gregory the Great in white and gold papal vestments with a soft gold halo, standing at the center of a candlelit Romanesque choir, one hand resting on a huge open illuminated choir book on a carved wooden lectern, the pages seen at a steep oblique angle so only blurred red and black blocks and gilded initials show, no readable notation. Around him five tonsured Benedictine monks in black habits sing with lips parted and eyes lowered to the book; Gregory's own gaze rises toward a shaft of golden light falling from a high arched window. Tall candles, incense haze, deep umber shadows in the vaulting. Classical Baroque 17th-century academic religious oil painting on canvas, in the manner of the Italian and Spanish devotional masters, warm candle-and-gold chiaroscuro light, deep dark umber background, soft luminous golden halo, rich lapis blue, crimson and ochre drapery, visible brushwork, glazed skin tones, fine craquelure across the whole surface, museum-quality aged varnish, portrait 4:5 composition. No text, no lettering, no inscriptions, no signature, no frame, no border, no modern objects, no logos.
```

**Negative prompt:** shared negative (above).

**Motion prompt**

```
Slow push-in on Gregory and the open choir book; the monks' lips move softly in unison as in chant, candle flames flicker and thin incense haze drifts through the light shaft. Keep it a still classical oil painting throughout with brushwork and craquelure intact, one continuous shot with no cuts, no new figures entering, faces and hands keep their exact features with no morphing.
```

### G3_GregoryPrayer

- **Film:** Gregory
- **Aspect ratio:** 4:5
- **Image model:** Nano Banana Pro (Higgsfield). Single close portrait; Nano Banana Pro gives the most painterly face and glazed skin.

**Still prompt**

```
Close half-length portrait of Saint Gregory the Great in prayer, an aged pope with a short grey beard and gentle lined face, hands joined at his chest, wearing a white alb under a deep crimson mozzetta with gold embroidery, a large soft gold halo behind his head. His eyes are lifted upward and to the side toward an unseen warm light, lips slightly parted as if beginning to sing. Strong warm candlelight from the left sculpts his face, the background falls to near-black umber. Classical Baroque 17th-century academic religious oil painting on canvas, in the manner of the Italian and Spanish devotional masters, warm candle-and-gold chiaroscuro light, deep dark umber background, soft luminous golden halo, rich lapis blue, crimson and ochre drapery, visible brushwork, glazed skin tones, fine craquelure across the whole surface, museum-quality aged varnish, portrait 4:5 composition. No text, no lettering, no inscriptions, no signature, no frame, no border, no modern objects, no logos.
```

**Negative prompt:** shared negative (above).

**Motion prompt**

```
Very slow push-in on his face; his lips move softly as in quiet chant, warm light gently brightens across his brow and the halo glows faintly. Keep it a still classical oil painting throughout with brushwork and craquelure intact, one continuous shot with no cuts, no new figures entering, faces and hands keep their exact features with no morphing.
```

---

## Film: Hildegard

Saint Hildegard of Bingen, 12th-century Benedictine abbess, composer and visionary of the living light.

| Level | Name |
|---|---|
| Campaign | `SaintHildegard_VID_YYYY-MM-DD` |
| Ad Set | `T1_MF_35-65+_SaintHildegard_VID_HildegardLivingLight` |
| Ad | `01_HildegardLivingLight` |

AngleName `SaintHildegard` is new; log it in LEARNINGS.md and ANGLE_LEDGER.md at launch. One campaign per angle, to avoid the drift flagged on 2026-10-18. Date = launch date.

**Clip order:** H3_HildegardLivingLight > M2_AngelChoir > H1_HildegardTablet > M5_MaryListening > H2_HildegardChapel


### H1_HildegardTablet

- **Film:** Hildegard
- **Aspect ratio:** 4:5
- **Image model:** Nano Banana Pro (Higgsfield). Single seated figure with strong light play; Nano Banana Pro renders the luminous painterly light best.

**Still prompt**

```
Saint Hildegard of Bingen, a serene middle-aged Benedictine abbess in a black habit with a white wimple and black veil, seated on a simple wooden bench in a stone cell. She holds a plain wooden-framed wax tablet on her knee and a stylus in her other hand, the tablet face tilted away and blank. Her face is lifted toward a high small window from which a column of golden light streams down onto her, with tongue-like flickers of gold flame softly descending within the light. Soft gold halo, abbess's staff leaning against the wall, deep umber shadows. Classical Baroque 17th-century academic religious oil painting on canvas, in the manner of the Italian and Spanish devotional masters, warm candle-and-gold chiaroscuro light, deep dark umber background, soft luminous golden halo, rich lapis blue, crimson and ochre drapery, visible brushwork, glazed skin tones, fine craquelure across the whole surface, museum-quality aged varnish, portrait 4:5 composition. No text, no lettering, no inscriptions, no signature, no frame, no border, no modern objects, no logos.
```

**Negative prompt:** shared negative (above).

**Motion prompt**

```
Slow push-in on Hildegard; the column of light drifts and shimmers with soft flickers of gold descending, her veil stirs faintly and the stylus hand moves a little. Keep it a still classical oil painting throughout with brushwork and craquelure intact, one continuous shot with no cuts, no new figures entering, faces and hands keep their exact features with no morphing.
```

### H2_HildegardChapel

- **Film:** Hildegard
- **Aspect ratio:** 4:5
- **Image model:** GPT Image 2.5 (Higgsfield). Abbess leading a group of singing nuns; GPT Image keeps the group composition and faces consistent.

**Still prompt**

```
Saint Hildegard of Bingen in a black Benedictine habit and white wimple, soft gold halo, standing before a group of six nuns in black habits and white wimples inside a candlelit Romanesque chapel with round arches and thick stone columns. She lifts one hand gently as if guiding their singing; the nuns sing with lips parted and eyes lowered or raised toward the altar. Rows of beeswax candles glow on the altar, warm gold light against deep umber vaults. No books with readable pages. Classical Baroque 17th-century academic religious oil painting on canvas, in the manner of the Italian and Spanish devotional masters, warm candle-and-gold chiaroscuro light, deep dark umber background, soft luminous golden halo, rich lapis blue, crimson and ochre drapery, visible brushwork, glazed skin tones, fine craquelure across the whole surface, museum-quality aged varnish, portrait 4:5 composition. No text, no lettering, no inscriptions, no signature, no frame, no border, no modern objects, no logos.
```

**Negative prompt:** shared negative (above).

**Motion prompt**

```
Slow push-in toward Hildegard; the nuns' lips move together in song, her raised hand sways slightly in time and the altar candles flicker warmly. Keep it a still classical oil painting throughout with brushwork and craquelure intact, one continuous shot with no cuts, no new figures entering, faces and hands keep their exact features with no morphing.
```

### H3_HildegardLivingLight

- **Film:** Hildegard
- **Aspect ratio:** 4:5
- **Image model:** Nano Banana Pro (Higgsfield). Hero close portrait with flames of light; Nano Banana Pro produced the closest match to the winning Cecilia face quality.

**Still prompt**

```
Close half-length portrait of Saint Hildegard of Bingen, a radiant abbess in a black veil and crisp white wimple, eyes lifted upward in quiet wonder, lips softly parted as if singing. Around her head and shoulders small gentle tongues of golden fire and glowing light descend from above like a living flame, reflecting warm gold on her cheeks, with a luminous gold halo behind her head. Hands joined lightly at her chest. Background falls to deep umber darkness. Classical Baroque 17th-century academic religious oil painting on canvas, in the manner of the Italian and Spanish devotional masters, warm candle-and-gold chiaroscuro light, deep dark umber background, soft luminous golden halo, rich lapis blue, crimson and ochre drapery, visible brushwork, glazed skin tones, fine craquelure across the whole surface, museum-quality aged varnish, portrait 4:5 composition. No text, no lettering, no inscriptions, no signature, no frame, no border, no modern objects, no logos.
```

**Negative prompt:** shared negative (above).

**Motion prompt**

```
Very slow push-in on her face; the gentle tongues of golden light drift downward and flicker around her, her lips move softly as in singing and the light pulses warmly on her cheeks. Keep it a still classical oil painting throughout with brushwork and craquelure intact, one continuous shot with no cuts, no new figures entering, faces and hands keep their exact features with no morphing.
```

---

## Film: Francis

Saint Francis of Assisi and the Canticle of Brother Sun.

| Level | Name |
|---|---|
| Campaign | `SaintFrancis_VID_YYYY-MM-DD` |
| Ad Set | `T1_MF_35-65+_SaintFrancis_VID_FrancisBrotherSun` |
| Ad | `01_FrancisBrotherSun` |

AngleName `SaintFrancis` is new; log it in LEARNINGS.md and ANGLE_LEDGER.md at launch. One campaign per angle, to avoid the drift flagged on 2026-10-18. Date = launch date.

**Clip order:** F1_FrancisBrotherSun > M1_MaryInPrayer > F2_FrancisBirds > M2_AngelChoir > F3_FrancisSunlitFace


### F1_FrancisBrotherSun

- **Film:** Francis
- **Aspect ratio:** 4:5
- **Image model:** GPT Image 2.5 (Higgsfield). Landscape plus figure with large sky; GPT Image handles wide compositions and horizon light cleanly.

**Still prompt**

```
Saint Francis of Assisi in a patched brown Franciscan habit tied with a knotted white cord, barefoot, standing on a rocky hillside with arms opened wide and palms up, face lifted toward a great golden sun rising over the soft blue Umbrian hills and a distant hill town. Warm gold dawn light rims his tonsured head and beard and a soft gold halo glows behind him; the sky shades from deep umber at the top into ochre and gold. Olive trees in shadow at the edges. His hands are gentle and unmarked. Classical Baroque 17th-century academic religious oil painting on canvas, in the manner of the Italian and Spanish devotional masters, warm candle-and-gold chiaroscuro light, deep dark umber background, soft luminous golden halo, rich lapis blue, crimson and ochre drapery, visible brushwork, glazed skin tones, fine craquelure across the whole surface, museum-quality aged varnish, portrait 4:5 composition. No text, no lettering, no inscriptions, no signature, no frame, no border, no modern objects, no logos.
```

**Negative prompt:** shared negative (above).

**Motion prompt**

```
Slow push-in toward Francis; sunrise light slowly intensifies and rays drift across the hills, his habit stirs in a light breeze and his lips move softly as in song. Keep it a still classical oil painting throughout with brushwork and craquelure intact, one continuous shot with no cuts, no new figures entering, faces and hands keep their exact features with no morphing.
```

### F2_FrancisBirds

- **Film:** Francis
- **Aspect ratio:** 4:5
- **Image model:** GPT Image 2.5 (Higgsfield). Many small birds plus hands; GPT Image is more reliable on counts and anatomy.

**Still prompt**

```
Saint Francis of Assisi in a brown habit with a white cord, kneeling at the edge of a grove at golden hour, small birds (sparrows, finches, a white dove) perched on his outstretched hand, his shoulder and the branches around him, more resting on the ground at his feet. His face is turned down tenderly toward the birds, lips parted as if singing to them, soft gold halo. Warm amber light falls through the trees, deep umber shadows behind. His hands are gentle and unmarked. Classical Baroque 17th-century academic religious oil painting on canvas, in the manner of the Italian and Spanish devotional masters, warm candle-and-gold chiaroscuro light, deep dark umber background, soft luminous golden halo, rich lapis blue, crimson and ochre drapery, visible brushwork, glazed skin tones, fine craquelure across the whole surface, museum-quality aged varnish, portrait 4:5 composition. No text, no lettering, no inscriptions, no signature, no frame, no border, no modern objects, no logos.
```

**Negative prompt:** shared negative (above).

**Motion prompt**

```
Slow push-in on Francis and the birds; the birds hop and flutter lightly in place without flying off frame, leaves stir and his lips move softly as in singing. Keep it a still classical oil painting throughout with brushwork and craquelure intact, one continuous shot with no cuts, no new figures entering, faces and hands keep their exact features with no morphing.
```

### F3_FrancisSunlitFace

- **Film:** Francis
- **Aspect ratio:** 4:5
- **Image model:** Nano Banana Pro (Higgsfield). Close portrait with warm light on the face; Nano Banana Pro gives the strongest painterly skin.

**Still prompt**

```
Close half-length portrait of Saint Francis of Assisi, a thin gentle man with a short dark beard and tonsure, brown hooded habit, eyes lifted upward with quiet joy, lips slightly parted in song, hands joined at his chest. Warm golden sunlight falls across one side of his face from the upper right, a soft gold halo behind, the background dissolving into deep umber with a hint of ochre sky. Classical Baroque 17th-century academic religious oil painting on canvas, in the manner of the Italian and Spanish devotional masters, warm candle-and-gold chiaroscuro light, deep dark umber background, soft luminous golden halo, rich lapis blue, crimson and ochre drapery, visible brushwork, glazed skin tones, fine craquelure across the whole surface, museum-quality aged varnish, portrait 4:5 composition. No text, no lettering, no inscriptions, no signature, no frame, no border, no modern objects, no logos.
```

**Negative prompt:** shared negative (above).

**Motion prompt**

```
Very slow push-in on his face; warm sunlight drifts slowly across his cheek and brow, his lips move softly as in singing and the halo glows faintly. Keep it a still classical oil painting throughout with brushwork and craquelure intact, one continuous shot with no cuts, no new figures entering, faces and hands keep their exact features with no morphing.
```

---

## Film: David

King David, the psalmist with his harp.

| Level | Name |
|---|---|
| Campaign | `KingDavid_VID_YYYY-MM-DD` |
| Ad Set | `T1_MF_35-65+_KingDavid_VID_DavidCrownedPsalmist` |
| Ad | `01_DavidCrownedPsalmist` |

AngleName `KingDavid` is new; log it in LEARNINGS.md and ANGLE_LEDGER.md at launch. One campaign per angle, to avoid the drift flagged on 2026-10-18. Date = launch date.

**Clip order:** D2_DavidCrownedPsalmist > M7_MonksChanting > D1_DavidBeforeSaul > M1_MaryInPrayer > D3_DavidHarpHands


### D1_DavidBeforeSaul

- **Film:** David
- **Aspect ratio:** 4:5
- **Image model:** GPT Image 2.5 (Higgsfield). Two-figure narrative scene with an instrument; GPT Image keeps the staging and harp structure coherent.

**Still prompt**

```
Young David, a shepherd youth with auburn curls in a simple ochre tunic and a crimson cloak, seated on a low stool playing a small wooden lyre-harp in a dark palace hall, eyes lowered to the strings. To the right in shadow King Saul sits on a carved throne in deep blue and gold robes, chin resting on his hand, eyes closed, his troubled face beginning to soften. A single bronze oil lamp and candlelight cast warm gold on both figures; columns and heavy curtains fall into deep umber. No weapons. No halo on Saul; a faint soft gold glow around David's head. Classical Baroque 17th-century academic religious oil painting on canvas, in the manner of the Italian and Spanish devotional masters, warm candle-and-gold chiaroscuro light, deep dark umber background, soft luminous golden halo, rich lapis blue, crimson and ochre drapery, visible brushwork, glazed skin tones, fine craquelure across the whole surface, museum-quality aged varnish, portrait 4:5 composition. No text, no lettering, no inscriptions, no signature, no frame, no border, no modern objects, no logos.
```

**Negative prompt:** shared negative (above).

**Motion prompt**

```
Slow push-in on David and the lyre; his fingers move gently across the strings which shimmer slightly, the lamp flame flickers and Saul's face eases very slightly. Keep it a still classical oil painting throughout with brushwork and craquelure intact, one continuous shot with no cuts, no new figures entering, faces and hands keep their exact features with no morphing.
```

### D2_DavidCrownedPsalmist

- **Film:** David
- **Aspect ratio:** 4:5
- **Image model:** Nano Banana Pro (Higgsfield). Hero figure with crown, beard and harp in rich light; Nano Banana Pro gives the richest painterly finish.

**Still prompt**

```
King David the psalmist, an older bearded king with silver-streaked hair wearing a simple gold crown, a deep crimson mantle with an ermine edge over a blue robe, holding an ornate gilded harp against his shoulder with one hand on the strings. His eyes are raised upward toward a warm shaft of golden light, lips parted as if singing a psalm, soft gold halo behind his crown. Candlelit chiaroscuro, deep umber background. Classical Baroque 17th-century academic religious oil painting on canvas, in the manner of the Italian and Spanish devotional masters, warm candle-and-gold chiaroscuro light, deep dark umber background, soft luminous golden halo, rich lapis blue, crimson and ochre drapery, visible brushwork, glazed skin tones, fine craquelure across the whole surface, museum-quality aged varnish, portrait 4:5 composition. No text, no lettering, no inscriptions, no signature, no frame, no border, no modern objects, no logos.
```

**Negative prompt:** shared negative (above).

**Motion prompt**

```
Slow push-in on David's face and harp; his lips move softly as in singing, his fingers pluck the strings lightly and the shaft of gold light drifts and brightens. Keep it a still classical oil painting throughout with brushwork and craquelure intact, one continuous shot with no cuts, no new figures entering, faces and hands keep their exact features with no morphing.
```

### D3_DavidHarpHands

- **Film:** David
- **Aspect ratio:** 4:5
- **Image model:** GPT Image 2.5 (Higgsfield). Close detail of hands and strings; GPT Image is more reliable on finger count and string geometry.

**Still prompt**

```
Close detail of King David's hands on the strings of a gilded wooden harp in candlelight, a jeweled gold ring on one finger, crimson and ermine sleeve at the edge of the frame, the carved harp neck glowing gold. A single beeswax candle burns in the background, everything else falling into deep umber shadow. Exactly five fingers on each hand, relaxed and natural. Classical Baroque 17th-century academic religious oil painting on canvas, in the manner of the Italian and Spanish devotional masters, warm candle-and-gold chiaroscuro light, deep dark umber background, soft luminous golden halo, rich lapis blue, crimson and ochre drapery, visible brushwork, glazed skin tones, fine craquelure across the whole surface, museum-quality aged varnish, portrait 4:5 composition. No text, no lettering, no inscriptions, no signature, no frame, no border, no modern objects, no logos.
```

**Negative prompt:** shared negative (above).

**Motion prompt**

```
Slow push-in on the hands; the fingers pluck the strings gently and the strings vibrate softly, the candle flame flickers and warm light shifts along the harp. Keep it a still classical oil painting throughout with brushwork and craquelure intact, one continuous shot with no cuts, no new figures entering, faces and hands keep their exact features with no morphing.
```

---

## Film: Magnificat

Our Lady's song, the Magnificat (Luke 1). Deliberately distinct from the existing Mary clips: exterior and dawn settings, a white veil under the blue, profile and lifted views instead of frontal downcast.

| Level | Name |
|---|---|
| Campaign | `Magnificat_VID_YYYY-MM-DD` |
| Ad Set | `T1_MF_35-65+_Magnificat_VID_MaryInSong` |
| Ad | `01_MaryInSong` |

AngleName `Magnificat` is new; log it in LEARNINGS.md and ANGLE_LEDGER.md at launch. One campaign per angle, to avoid the drift flagged on 2026-10-18. Date = launch date.

**Clip order:** MG3_MaryInSong > M2_AngelChoir > MG1_Visitation > M3_MaryCrowned > MG2_MaryArmsLifted


### MG1_Visitation

- **Film:** Magnificat
- **Aspect ratio:** 4:5
- **Image model:** GPT Image 2.5 (Higgsfield). Two-figure embrace; GPT Image is cleaner on interlocking arms and hands.

**Still prompt**

```
The Visitation: the young Virgin Mary, in a white veil under a lapis blue mantle and rose-red gown, embracing her older cousin Saint Elizabeth, in an ochre and olive mantle with a white headcloth, in the stone doorway of a hill-country house at dawn. Their cheeks nearly touch, Elizabeth's eyes closed in joy, Mary's eyes lowered and smiling softly. Warm gold morning light spills from the left across both faces; soft gold halos; a glimpse of pale gold sky and hills behind, the doorway interior in deep umber shadow. Both women are fully clothed and modest. Classical Baroque 17th-century academic religious oil painting on canvas, in the manner of the Italian and Spanish devotional masters, warm candle-and-gold chiaroscuro light, deep dark umber background, soft luminous golden halo, rich lapis blue, crimson and ochre drapery, visible brushwork, glazed skin tones, fine craquelure across the whole surface, museum-quality aged varnish, portrait 4:5 composition. No text, no lettering, no inscriptions, no signature, no frame, no border, no modern objects, no logos.
```

**Negative prompt:** shared negative (above).

**Motion prompt**

```
Slow push-in on the two faces; the embrace tightens very slightly, their veils stir in a soft breeze and the dawn light slowly warms across the doorway. Keep it a still classical oil painting throughout with brushwork and craquelure intact, one continuous shot with no cuts, no new figures entering, faces and hands keep their exact features with no morphing.
```

### MG2_MaryArmsLifted

- **Film:** Magnificat
- **Aspect ratio:** 4:5
- **Image model:** Nano Banana Pro (Higgsfield). Single standing figure with sky and light rays; Nano Banana Pro gives the most luminous painterly sky.

**Still prompt**

```
The young Virgin Mary standing on a hillside at dawn, arms lifted in the ancient orans gesture of praise with palms open, face raised to the sky, lips parted in song. She wears a white veil, a rose-red gown and a lapis blue mantle that billows gently, with a soft gold halo. Behind her the sky glows ochre and gold with soft rays of light, the hills below in umber shadow. Hands natural with five fingers each. Classical Baroque 17th-century academic religious oil painting on canvas, in the manner of the Italian and Spanish devotional masters, warm candle-and-gold chiaroscuro light, deep dark umber background, soft luminous golden halo, rich lapis blue, crimson and ochre drapery, visible brushwork, glazed skin tones, fine craquelure across the whole surface, museum-quality aged varnish, portrait 4:5 composition. No text, no lettering, no inscriptions, no signature, no frame, no border, no modern objects, no logos.
```

**Negative prompt:** shared negative (above).

**Motion prompt**

```
Slow push-in on Mary; her lips move softly as in singing, her mantle and veil stir in the breeze and soft rays of dawn light drift across the sky behind her. Keep it a still classical oil painting throughout with brushwork and craquelure intact, one continuous shot with no cuts, no new figures entering, faces and hands keep their exact features with no morphing.
```

### MG3_MaryInSong

- **Film:** Magnificat
- **Aspect ratio:** 4:5
- **Image model:** Nano Banana Pro (Higgsfield). Hero close portrait; same model family as the winning Cecilia-style face.

**Still prompt**

```
Close three-quarter profile portrait of the young Virgin Mary turned to the right, chin slightly lifted, eyes raised toward a warm light, lips parted in song, one hand resting over her heart. She wears a fine white veil with a lapis blue mantle drawn over it, a rose-red gown at the neckline, and a soft gold halo. Warm rose-gold light falls across her face from the upper right; the background is deep umber. Different from a frontal downcast Madonna: she is singing, joyful and lifted. Classical Baroque 17th-century academic religious oil painting on canvas, in the manner of the Italian and Spanish devotional masters, warm candle-and-gold chiaroscuro light, deep dark umber background, soft luminous golden halo, rich lapis blue, crimson and ochre drapery, visible brushwork, glazed skin tones, fine craquelure across the whole surface, museum-quality aged varnish, portrait 4:5 composition. No text, no lettering, no inscriptions, no signature, no frame, no border, no modern objects, no logos.
```

**Negative prompt:** shared negative (above).

**Motion prompt**

```
Very slow push-in on her face; her lips move softly as in singing, the hand over her heart rises slightly with her breath and warm light glows across her cheek. Keep it a still classical oil painting throughout with brushwork and craquelure intact, one continuous shot with no cuts, no new figures entering, faces and hands keep their exact features with no morphing.
```

---

## Notes for the build

- Ad creative format note: these are 4:5 video films, so the image rule of 1:1 plus an overlaid CTA button does not apply; the CTA comes from the Meta button and the end card in the build script.
- Watch for: legible text creeping onto the parchment (G1), choir book (G2) and wax tablet (H1); reroll any still with readable marks. Check finger counts on D3, F2 and MG2.
- Francis is shown without stigmata wounds to keep the no-gore rule; Saul is shown without a spear.
- Compliance check: imagery is devotional only (saints, candles, light, chant); no money, no before/after, no health claims, no figure addresses the viewer.
