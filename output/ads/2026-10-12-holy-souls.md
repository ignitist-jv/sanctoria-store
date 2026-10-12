# SungForTheHolySouls, Prayer Song seasonal batch
Date: 2026-10-12. Format: static PHOTO. Three ads, one per ad set.

## Why this angle, and why now

Taken from `AD_BRIEF.md` (2026-10-12 evening), where it is the number one ranked
build and the only time-pressured item on the account.

**Mechanism.** Every November the parish writes the names of the dead in a book
and reads them aloud at Mass. This is the same act she already performs, except
the name is sung, and it is hers to keep and replay rather than read once and
closed.

**Dominant emotion.** Grief, and the consolation of having done something for
someone she can no longer do anything for. Deliberately different from every
live execution, which all run on maternal worry about a living child.

**Fixed date.** All Souls Day is Monday 2026-11-02. Holy Souls month runs all
November. Cemetery indulgence window 2026-11-01 to 11-08.

**Why PHOTO, not UGC.** The single highest-ROAS ad in account history is
`01_QuietMansFaith` at 3.63x in PHOTO, and LEARNINGS records the correction
that the men's angles which died, died in UGC. Caveat: that 3.63x is 1 sale on
29 outbound clicks, so it is a lead, not a proven finding.

**Product fit confirmed, not assumed.** The order form has a dedicated "passed"
branch offering only grief, peace and thanksgiving; the summary line reads
"A prayer for eternal rest and peace, sung over Margaret by name";
`api/lyrics.php` maps grief to Apocalypse 21:4; and the terms and FAQ already
permit playing the song at a funeral or memorial. This case was designed in.

**Confidence: medium.** High on the occasion, medium on product fit, because
the Prayer Song has never been sold to a grieving buyer and has sold nothing
at all yet.

---

## Constant across all three

| Field | Value |
|---|---|
| Headline | `Create Your Custom Prayer Song Now` |
| Description | `$39, one time. Sent within 24 hours.` |
| CTA | Shop Now |
| URL | `https://sanctoriastore.com/prayer-song/` |
| URL parameters | `utm_source={{site_source_name}}&utm_medium={{placement}}&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&cmc_adid=fb_{{ad.id}}` |
| Overlay text | NO on all three. Argued below. |

**Overlay decision.** Every dead execution in `ANGLE_LEDGER.md` carries a
headline plus gold CTA overlay; the one 3.63x ad is a clean PHOTO. More
importantly, this angle works by being recognised as a real moment before it is
recognised as an advertisement, and a gold CTA button welded onto a photograph
of a grave is the single most damaging thing this brand could print in November.

---

## 01_BookAtTheBack
Recipient: a husband. Image: `2026-10-12-holy-souls-images/01_BookAtTheBack.png`

```
Every November a book goes out at the back of the church. A pen on a string. A widow writing her husband's name in it again.

This one sings his name instead. Hers to keep, and to play again long after the book is closed.
```
221 characters.

Opens on the remembrance book and the pen on a string, an object she has
physically touched every November. The turn is the line she has never been
offered: the book closes at the end of the month, and this does not.

## 02_CemeteryGate
Recipient: a mother. Image: `2026-10-12-holy-souls-images/02_CemeteryGate.png`

```
November. The cemetery gate, the prayers said over a mother's grave, the flowers left, the drive home.

There is one more thing that can still be done for her. A prayer for eternal rest, sung over her name, and kept.
```
216 characters.

The scroll stop is the drive home, not the grave. "One more thing that can
still be done" is the consolation with no suggestion that what she already does
is insufficient.

## 03_NamesReadAloud
Recipient: a brother. Image: `2026-10-12-holy-souls-images/03_NamesReadAloud.png`

```
At the All Souls Mass the names of the dead are read aloud, one after another, and a sister hears her brother's among them.

This one sings his name slowly. And sings it again any evening she wants to hear it.
```
209 characters.

Names the exact liturgical moment she waits through every year. "Slowly" and
"any evening" carry the whole mechanism with no product word. The sibling
relationship fishes a pond the account has never touched.

---

## Naming

| Level | Name |
|---|---|
| Campaign | `SungForTheHolySouls_PHOTO_2026-10-12` |
| Ad Set 1 | `T1_MF_45-65+_SungForTheHolySouls_PHOTO_BookAtTheBack` |
| Ad 1 | `01_BookAtTheBack` |
| Ad Set 2 | `T1_MF_45-65+_SungForTheHolySouls_PHOTO_CemeteryGate` |
| Ad 2 | `02_CemeteryGate` |
| Ad Set 3 | `T1_MF_45-65+_SungForTheHolySouls_PHOTO_NamesReadAloud` |
| Ad 3 | `03_NamesReadAloud` |

One ad per ad set per the standing rule. Three ad sets at $5/day is **$15/day**,
on top of the $15/day the live SungByName campaign is already spending.

---

## Creative direction, and what was rejected

The creative pass read all 409 lines of `CREATIVE_HISTORY.md` and found the
account has one visual language used roughly forty times: warm candlelight as
key, deep brown and gold, shallow macro on an object, interior, undated.
Zero hits for cemetery, grave, headstone, narthex, overcast, congregation or
umbrella. **There is not one cold, outdoor or public-crowd frame in the account's
entire history.** All three of these run cold available daylight with no candle
as key, which is both a genuine pattern interrupt and simply what November
looks like.

**One render was rejected and reshot.** The first `02_CemeteryGate` placed a car
at the right edge whose badge rendered as garbled chrome lettering, "ESRV.D2".
Kept as `02_CemeteryGate_REJECTED_car_badge.png` for reference. The reshoot
removes the car entirely; the keys in her hand already carry "drove here,
driving home".

**Every image was checked at pixel level for legible text**, which is the
failure mode that killed `02_NovemberNames`. Headstone inscriptions, the
remembrance book, the Mass leaflet and the hymn board were each zoomed and
confirmed to resolve as soft texture with no letterforms.

**Hard constraint honoured:** nothing here reuses the retired
`02_NovemberNames` list-photo execution or its hook.

---

## Status

Images generated, checked and posted to Discord. **Nothing has been built in
Ads Manager.** The brief's sequencing still applies: no more SungByName creative
until an ad clears roughly 75 outbound clicks, currently 14. This angle is the
stated exception only because All Souls has a fixed date. Build by roughly
2026-10-26 to get a week of learning first.
