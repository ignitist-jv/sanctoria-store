# Angle Ledger: sanctoria-store

Maintained by the daily research bot. Last updated 2026-10-14. Verdicts use Meta-reported purchase ROAS.

Profit line: 1.2x. Meta ad account `act_462874384767571` (Sanctoria Store, timezone Asia/Singapore).

Nothing in this file has been deleted. Entries whose numbers changed with the window roll are annotated, not removed.

---

## Account state, 2026-10-14

Two window conventions are shown because they disagree on two verdicts. **Complete-day** ends 2026-10-13 and is the primary convention today, because today is only a few hours old on this account and every ad with today's spend is too early to classify either way. **Inclusive** ends 2026-10-14 and is shown because the window roll moved a purchase out of 28d.

| Window | Convention | Ads | Spend | Purchases | Value | Meta ROAS |
|---|---|---|---|---|---|---|
| 7d | 2026-10-07 to 10-13 | 3 | **$38.15** | **0** | **$0.00** | **0.00x** |
| 14d | 2026-09-30 to 10-13 | 22 | $351.79 | 1 | $33.06 | 0.09x |
| 28d | 2026-09-16 to 10-13 | 48 | **$982.62** | **10** | **$376.16** | **0.38x** |
| 7d | 2026-10-08 to 10-14 | 6 | $56.32 | 0 | $0.00 | 0.00x |
| 14d | 2026-10-01 to 10-14 | 25 | $279.26 | 1 | $33.06 | 0.12x |
| 28d | 2026-09-17 to 10-14 | 48 | $911.80 | **9** | $324.70 | 0.36x |
| Today | 2026-10-14 partial | 5 | $17.21 | 0 | $0.00 | 0.00x |

**The account's last front-end sale was 2026-10-01. That is thirteen days ago.** Every dollar of 7d spend is Prayer Song spend. The 28d window keeps shedding sales as it rolls: 12 on 2026-10-10, 11, then 10, and **9 on the inclusive window today**.

### What is live, and it changed twice since yesterday

| Campaign | Status | Ad sets | Starts | Today's spend | State |
|---|---|---|---|---|---|
| `SungByName_UGC_2026-10-10` | **CAMPAIGN_PAUSED** | 3 | 2026-10-12 | $2.14 trickle | **Paused since yesterday.** Ran two days, $38.15, 0 purchases, 29 link clicks |
| `SungForTheHolySouls_PHOTO_2026-10-12` | **ACTIVE** | 3 at $5/day | **2026-10-14** | **$16.03** | **Started today.** 308 impressions, 32 clicks, 10 outbound, 0 purchases |
| `SungByName_VID_2026-10-13` | **ACTIVE** | 4 at $5/day | **2026-10-15** | $0.00 | **Self-starts tomorrow.** Ad sets `GodmothersPromise`, `HoldThemNear`, `NobodySaysHers`, `FontAndTheName` |

From tomorrow this account carries **seven live ad sets at $5/day, about $35/day**, on an offer with zero sales to date. Both new campaigns carry `locales: [6, 24]`, English (US) or English (UK), which satisfies the English-only rule. The three paused `SungByName_UGC` ad sets carry no `locales` at all.

### ⚠️ Flag A: both new campaigns are ACTIVE, not PAUSED

`SungForTheHolySouls_PHOTO_2026-10-12` and `SungByName_VID_2026-10-13` have campaign status ACTIVE. The standing build rule is campaign PAUSED, ad set and ads active underneath, with TS turning the campaign on as his single publish action. Either TS published them himself, which is fine and is the intended flow, or they were built active, which is not. **This ledger cannot change ad state and does not.** Flagging so the record is accurate: the Holy Souls campaign is spending today and the VID campaign will spend tomorrow with no further action from anyone.

### ✅ Tracking is sound. The zero is real, not a measurement failure

ClickBank `karmacc` for 2026-10-10 to 2026-10-13 returned **five rows and not one of them is a sale**: five `bump-blessing` rebills ($17.00 to $19.92, `processedPayments` 7 to 13, all legacy subscribers). **No new front-end SALE row of any kind, and no `prayersong-1` sale.** That matches Meta's zero purchases exactly. **No verdict below is discounted for broken tracking.**

### ✅ New today: the Prayer Song checkout is verified working end to end

Previous entries flagged the `songform` template as unverified. Checked directly today:

- The live page `https://sanctoriastore.com/prayer-song/` returns HTTP 200 and carries a real checkout link: `karmacc.pay.clickbank.net/?cbitems=prayersong-1&template=songform&vtid=[cmc_vid]`, with the ClickMagick token present and the page set to `noindex`.
- That link follows through to `orders.clickbank.net` and renders **ClickBank Secure Checkout** with `prayersong-1` on it. The item is live and buyable.

**So the offer can be bought, and nobody has bought it.** 46 link clicks across five Prayer Song ads and zero sales is not yet a verdict (see the sample-size note below), but it removes the most comfortable explanation.

### ⚠️ Still open, sixth consecutive flag: the order bump is not attaching

Four days of new buyers, zero `bump-blessing` first payments, and every rebill in the window belongs to a legacy subscriber on payment 7 to 13. The $17/month line is still a closed book.

**One new piece of evidence, and it is a lead rather than an answer.** The rendered `songform` checkout contains order-bump markup: `bump-container`, `bump-item`, `bump-copy`, `bump-image`, `bump-payment`, `bump-disclaimer-dof`. The rendered total also carried a second priced line beyond the product. The template therefore has a bump slot and appears to be populating it. **Whether a bump product is correctly attached and crediting cannot be settled from the rendered page, and it is not claimed here.** It needs checking on the ClickBank side, which this bot does not do. The observed legacy cohorts ran 4 to 14 payments, so a bump that attaches is worth roughly $70 to $230 of back-end LTV per buyer against a front end that nets about $37.

### Sample size: why five Prayer Song ads with no sales is not five verdicts

LEARNINGS' funnel audit of 2026-09-23 stands: at this account's click economics, **$15 buys about 12 outbound clicks, and an ad performing exactly at account average shows zero sales 69% of the time.** Roughly 75 outbound clicks, about $95, is needed for a 90% read. Every Prayer Song ad is between 1 and 13 link clicks. The dead-execution rule still fires at $15 with no purchase and is applied below, but the diagnosis column says so where the number cannot support one.

**Fatigue is ruled out account-wide.** Frequency runs 1.00 to 1.69 across all 48 ads, and the only ad above 1.5 (`02_QuietMinute`, 1.66) has been paused for days.

---

## Locked Winners

**None. Fifth consecutive day.** The bar is at or above 1.2x on **both** 14d and 28d with **10 or more purchases in 28d**. **No ad in this account's history has ever carried 10 purchases in a 28d window; the highest is 2.** Every ad with 7d spend has produced zero purchases.

## Potential Winners

**None. Fifth consecutive day.** The bar requires at or above 1.2x on 7d with 2 or more purchases. **7d spend is $38.15 to $56.32 depending on convention and 7d purchases are zero on both.**

### Watch list (not ledger-eligible, recorded for context only)

- **`02_ParkedAndEarlyRosary`** `120256490331090051` reads **1.44x on 14d** on the inclusive window ($22.88, 1 purchase, $33.06). It is the only above-line reading anywhere in the account today. It has **no 7d spend**, so it cannot be a Potential Winner, and it is paused. It remains a dead execution on 28d at 1.09x. Recorded because it is the last ad on this account that made money.
- **The three `SungForTheHolySouls_PHOTO` ads**, first partial day: `03_NamesReadAloud_v2` $4.85 at 12.50% CTR, `02_CemeteryGate_v2` $4.72 at 10.38%, `01_BookAtTheBack_v2` $5.50 at 7.78%. Ten outbound clicks between them. **TOO EARLY, no verdict.** On this account's own read requirement the first honest look is around 2026-10-17 and a real verdict is two to three weeks out at $5/day.
- **The four `SungByName_VID` ad sets** start tomorrow with no data.

---

## Dead Angles (do not repeat)

### SistersThreePack
**Date declared: 2026-10-14. NEW TODAY.**

**Evidence (28d inclusive, to 2026-10-14): 4 executions, $92.18 spent, 0 purchases, 0.00x pooled.**

| Execution | Ad id | Spend | Sales | CTR |
|---|---|---|---|---|
| `01_SistersThreeStates` | `120256241056050051` | **$52.60** | **0** | 7.34% |
| `03_NotMyRealSister` | `120256381145030051` | $13.87 | 0 | 13.79% |
| `01_TookOneThingEach` | `120256381144980051` | $13.41 | 0 | 14.19% |
| `02_ElevenYearsOfTexts` | `120256381144970051` | $12.30 | 0 | 5.03% |

**Why it died.** `01_SistersThreeStates` has crossed **$50 of spend with zero purchases on today's window**, which is the single-execution angle-kill test. Three further executions spent $39.58 between them for nothing. LEARNINGS already killed this angle at 1.10x on 2026-09-28 and this ledger has carried it as "not yet dead, but spent" since 2026-10-10. Today it is formally dead.

**Window dependency, stated plainly.** On the complete-day window ending 2026-10-13 the same ad reads **$58.02 with 1 purchase at 0.89x**, which does not satisfy the zero-purchase test. **The $50-with-zero test is met on one convention and not the other.** The declaration does not rest on that cent-level coin flip alone: on both conventions the angle is 0 or 1 sale across four executions on $92 to $98, it has never been above the line, and it has been retired by LEARNINGS for a fortnight. The ad also remains mislabelled under ad set `T1_MF_35-65+_StoppedHidingIt_UGC_ParkingLot`, so `utm_term` has written the wrong angle to ClickMagick since launch.

**This also closes the oscillation.** `01_SistersThreeStates` has now read 1.10x, 1.21x, 0.81x, 0.89x and 0.00x on five consecutive checks, purely on window convention. It is not promotable under any of them: 0 to 2 purchases against a 10-purchase bar, no 14d or 7d spend, paused.

### AQuietDevotion
**Date declared:** 2026-10-10. **Numbers refreshed:** 2026-10-14.
**Evidence (28d inclusive to 2026-10-14):** the angle's full footprint is **11 executions, $288.76 spent, 5 purchases, $192.55 returned, 0.67x pooled.** Strictly-dead executions: `02_QuietMinute` ($92.05, 2 purchases, 0.82x), `01_TenMinutes` ($83.12, 2 purchases, 1.01x), `02_ParkedAndEarlyRosary` ($30.37, 1 purchase, 1.09x on 28d), `02_LastOneAwake` ($16.25, 0), `03_TenMinutesEarlyToMass` ($15.82, 0).
**Window-sensitivity notes retained from 2026-10-12, now more pronounced:** `01_CardiganMorning` ($4.30), `01_KitchenMorning` ($3.53) and `01_CouchMorning` ($3.15) have fallen far below the $15 zero-purchase threshold on the inclusive window and no longer meet the test they were recorded under. `01_TheDrivewayMinute` ($14.15 complete-day, $5.94 inclusive) likewise. Per the no-delete rule the entries stand, annotated. **This changes nothing about the angle**, which still carries five strictly-dead executions against a two-execution bar.
**Why it died:** the hooks still earn clicks, with CTRs from 8.81% to 24.34%, and the clicks do not buy. The angle was tested to exhaustion: eleven scene variations of one stolen-ten-minutes mechanism with no scene outperforming another, which is what a saturated mechanism looks like rather than a hunt for the right execution.
**Correction to LEARNINGS.md stands:** the 2026-09-28 entry calls this angle "the account's franchise" and "the only consistently above-line performer," and the 2026-10-01 entry records it at 1.45x pooled. It is 0.67x pooled today with every funded execution dead.

### DaughterPack
**Date declared:** 2026-10-10. **Numbers refreshed:** 2026-10-14.
**Evidence (28d inclusive to 2026-10-14):** 4 executions, **$184.49 spent, 2 purchases, $66.10 returned, 0.36x pooled.** Two dead executions: `04_DaughterTwoPack` `120256178585990051` ($117.54, 1 purchase, **0.28x** on 28d, no 14d spend, CTR 19.32%) and `03_SheNoticedMine` `120256381145000051` ($38.59, 1 purchase, 0.86x on 28d, CTR 19.69%). Two further executions failed under the $15 threshold: `02_TheLastBox` ($14.57, 0) and `01_IDontPushIt` ($13.79, 0).
**Why it died:** `04_DaughterTwoPack` is the single largest loss in the account, $117.54 to $143.40 depending on window, for one sale. Its CTR is excellent and it bought almost nothing, so the diagnosis is **good click and no sale, a page or offer mismatch.** LEARNINGS already flagged this ad as paying $1.96 per outbound click against a $1.27 blend because long line-broken primary text burns clicks on photo expands and "see more" taps. It kept spending after that finding.

---

## Dead Executions (do not reuse this hook or visual)

Figures are the 28d **inclusive** window to 2026-10-14 unless a cell says otherwise. Diagnosis key: **no-sale** means CTR was healthy and nothing converted, pointing at the page or offer rather than the hook; **weak-hook** means CTR was low for this account, whose kills run 4.31% to 24.34%; **decay** means the ad converted earlier and its sales have rolled out of the measurement window; **undiagnosable** means the rule fired but the click count cannot support a diagnosis.

| Angle | Ad name | Ad id | Date | Spend | Sales | CTR | Diagnosis |
|---|---|---|---|---|---|---|---|
| DaughterPack | 04_DaughterTwoPack | `120256178585990051` | 2026-10-10 | $117.54 | 1 | 19.32% | no-sale at scale; largest single loss in the account. 0.28x |
| AQuietDevotion | 02_QuietMinute | `120256136639850051` | 2026-10-12 | $92.05 | 2 | 6.69% | below the line on both 14d (0.00x) and 28d (0.82x). Decay, not a bad hook: took 2 sales early and nothing since. Its CTR is also the low end for this account |
| AQuietDevotion | 01_TenMinutes | `120256381145130051` | 2026-10-10 | $83.12 | 2 | 17.22% | below line on 14d (0.00x) and 28d (1.01x); was logged 2.83x on 2026-09-28, so decay, not a bad hook |
| SistersThreePack | 01_SistersThreeStates | `120256241056050051` | 2026-10-10 | **$52.60** | **0** | 7.34% | **Updated 2026-10-14. Now reads 0 purchases on the inclusive window and crosses $50 with zero sales, which declared the angle dead above.** Fifth reading in five checks (1.10x, 1.21x, 0.81x, 0.89x, 0.00x). Still mislabelled under ad set `..._StoppedHidingIt_UGC_ParkingLot` |
| DaughterPack | 03_SheNoticedMine | `120256381145000051` | 2026-10-10 | $38.59 | 1 | 19.69% | no-sale, 0.86x on 28d and no 14d spend |
| NovemberNames | 02_NovemberNames | `120256502344660051` | 2026-10-10 | $35.22 | 1 | 9.35% | 0.94x on 28d, 0.00x on 14d. **The execution is dead, the angle is not** (one execution, under $50, and it did convert). All Souls is Monday 2026-11-02, so this angle is in season within three weeks. The retired assets were a candle rack plus a long handwritten list of names; rebuild the execution, do not retire the angle |
| AQuietDevotion | 02_ParkedAndEarlyRosary | `120256490331090051` | 2026-10-10 | $30.37 | 1 | 16.31% | marginal, 1.09x on 28d against a 1.2x line. **Annotated 2026-10-14: now reads 1.44x on 14d, above the line.** Entry retained; the 28d verdict stands and the ad is paused with no 7d spend |
| ThreeGenerations | 03_OneEachThreeOfUs | `120256276845640051` | 2026-10-10 | $23.04 | 1 | 9.26% | recorded at 0.92x. **Annotated 2026-10-14: now reads 1.43x on 28d as spend rolled out of the window, so it no longer strictly meets its test.** Entry retained per the no-delete rule. Paused, no 14d or 7d spend |
| NeverLearnedItProperly | 02_LoseMyPlace | `120256276845620051` | 2026-10-10 | $18.14 at record, $3.62 now | 0 | 9.68% | no-sale. Far below threshold on the current window; entry retained, verdict no longer strictly met |
| InheritedByDaughters | 01_GloveCompartmentBuick | `120256276845600051` | 2026-10-10 | $17.53 at record, $4.06 now | 0 | 12.20% | no-sale. Below threshold now; entry retained, verdict no longer strictly met |
| TheOneThingIPrayFor | 01_OnlyOneThing | `120256502344680051` | 2026-10-10 | $17.45 | 0 | 5.82% | weak-hook for this account, plus no sale |
| MenWhoWearIt | 02_EngineGrease | `120256276845750051` | 2026-10-10 | $17.16 at record, $4.50 now | 0 | 13.75% | no-sale; male-recipient angles have never converted in UGC here. Below threshold now; entry retained |
| TheDrawerOne | 01_DrawerDish | `120256276845740051` | 2026-10-10 | $16.86 at record, $4.41 now | 0 | 20.00% | no-sale, Triptych funnel. Below threshold now; entry retained |
| KeepOneGiveOne | 03_GaveMineAway | `120256276845760051` | 2026-10-10 | $16.49 at record, $5.14 now | 0 | 6.62% | no-sale, Triptych funnel. Below threshold now; entry retained |
| AQuietDevotion | 01_CardiganMorning | `120256150053220051` | 2026-10-10 | $16.27 at record, $4.30 now | 0 | 13.16% | no-sale. Below threshold now; entry retained, verdict no longer strictly met |
| AQuietDevotion | 02_LastOneAwake | `120256490331130051` | 2026-10-10 | $16.25 | 0 | 8.81% | no-sale |
| WhatIsOnIt | 03_WhatYouAreWearing | `120256502344700051` | 2026-10-10 | $16.23 | 0 | 6.56% | weak-hook, product-feature framing |
| AQuietDevotion | 03_TenMinutesEarlyToMass | `120256490331140051` | 2026-10-10 | $15.82 | 0 | 21.24% | no-sale, highest CTR of the angle and zero purchases |
| ThreeForThree | 01_OneForEachOfThem | `120256493204990051` | 2026-10-10 | $15.71 | 0 | 5.14% | weak-hook, lowest CTR of the Guard wave |
| WhyThree | 03_WhyThereAreThree | `120256493205000051` | 2026-10-10 | $15.44 | 0 | 6.02% | weak-hook, product-feature framing |
| **SungByName** | **01_SonOpen_v2** | `120256732898630051` | **2026-10-14** | **$15.10** | **0** | **10.50%** | **NEW TODAY. Undiagnosable.** The rule fires at $15 with no purchase and it is met at ten cents over, on **13 link clicks**. At this account's own read requirement of about 75 outbound clicks, 13 clicks cannot distinguish a bad hook from an ordinary run of bad luck, and an average ad shows zero sales 69% of the time at this spend. **Recorded because the rule requires it. The hook is not condemned and the visual is not condemned.** The angle is alive and its VID rebuild starts tomorrow |
| AQuietDevotion | 01_KitchenMorning | `120256150053230051` | 2026-10-10 | $14.53 at record, $3.53 now | 0 | 12.07% | no-sale when recorded at $19.26. Below threshold; entry retained, verdict no longer strictly met |
| AQuietDevotion | 01_CouchMorning | `120256150053280051` | 2026-10-10 | $14.32 at record, $3.15 now | 0 | 9.09% | no-sale when recorded at $18.93. Below threshold; entry retained, verdict no longer strictly met |

**One new dead execution today, `01_SonOpen_v2`, and it is a threshold-edge call.** The total stands at **23 across 15 angles**. Ten of the 23 no longer strictly meet their test on the current window and are annotated; all are retained.

### Data hygiene note on five of the above
LEARNINGS.md logged `InheritedByDaughters_GloveBox`, `NeverLearnedItProperly_LostMyPlace`, `TheDrawerOne_DrawerDish`, `MenWhoWearIt_EngineGrease` and `KeepOneGiveOne_TwoWrists` as killed on 2026-09-17 against ad ids differing from today's in their trailing digits while reporting near-identical spend. These are almost certainly the same ads recorded against neighbouring ids. They are counted **once** here, so none is credited with a second death and no angle is declared dead on a double count.

### Too early, for the record (not classified)
Carried spend under $15 with no purchase on the inclusive window, so no verdict earned: `02_TheLastBox` ($14.57), `03_ThreeWeeksBeforeIOrdered` ($14.24), `01_TheDrivewayMinute` ($14.15), `03_NotMyRealSister` ($13.87), `01_IDontPushIt` ($13.79), `02_TheDrawerByTheSink` ($13.62), `02_ParkedAndEarly` ($13.52), `04_BottomOfMyBag` ($13.50), `01_CameInAtFortyOne` ($13.46), `01_TookOneThingEach` ($13.41), `02_ItSitsFlat` ($13.35), **`04_NameFirst` ($13.03)**, `02_ElevenYearsOfTexts` ($12.30), **`02_DaughterOpen` ($12.16)**, `02_TheThirdOneIsTen` ($11.89), `02_ThePrayerOnTheMedal` ($11.83), `01_WornSoftInThreeSpots` ($11.82), `03_FourYearsOfWear` ($11.68), `01_AskingHisMother` ($11.59), `01_TenMinutesRosary` ($11.36), `06_AnyWeightToIt` ($10.23), `05_IWearItInTheShower` ($9.16), `03_SecondBoxOnCounter` ($6.14), `01_HandAlreadyKnows` ($4.91), `02_NineteenYears` ($4.54), and the three `SungForTheHolySouls_PHOTO` ads at $4.93 to $5.77.

`01_AskingHisMother` ($11.59) is the Mary and intercession test that LEARNINGS calls the largest untested fit in the account; it has still never been given enough spend to say anything.

---

## Change Log

- **2026-10-10** Ledger created. Recorded 0 Locked and 0 Potential Winners; the account ran at 0.36x on $1,242.59 over 28 days with 12 purchases.
- **2026-10-10** Declared **AQuietDevotion** a dead angle on 7 dead executions, $218.35, 3 purchases, best 1.09x. This reverses the 2026-09-28 LEARNINGS finding that named it the account's franchise.
- **2026-10-10** Declared **DaughterPack** a dead angle on 2 dead executions, $209.85, 2 purchases, 0.31x pooled.
- **2026-10-10** Recorded 21 dead executions across 14 angles, every one with healthy CTR or a near-line ROAS rather than a hook failure.
- **2026-10-10** Verified Meta attribution against ClickBank on the 14d window. No verdict discounted for broken tracking.
- **2026-10-10** Flagged that the `bump-blessing` $17/month subscription produced rebills from a legacy cohort only, with zero first payments on new sales.
- **2026-10-10** Noted `02_NovemberNames` as a dead execution whose **angle remains live and is about to be in season** (All Souls, 2026-11-02).
- **2026-10-10** Noted the ad set `T1_MF_35-65+_StoppedHidingIt_UGC_ParkingLot` is mislabelled and still running SistersThreePack creative, so `utm_term` writes the wrong angle to ClickMagick.
- **2026-10-11** Refreshed all 21 dead-execution figures. Added no new dead executions or angles, because nothing had delivered since 2026-10-05.
- **2026-10-11** Established the account went dark on 2026-10-06 and upgraded the tracking verification to the full 28d window, matching Meta's 12 purchases / $442.20 against ClickBank's 12 rows / $442.32.
- **2026-10-11** Settled the order-bump question: 12 new buyers, zero bump first payments, all rebills from subscribers with 4 to 14 prior payments.
- **2026-10-11** Recorded the new ACTIVE campaign `SungByName_UGC_2026-10-10` with no spend and no verdict possible.
- **2026-10-12 (morning)** The blackout ended. `SungByName_UGC_2026-10-10` started at 03:00 SGT and had spent $14.51 for 277 impressions, 11 outbound clicks, 0 purchases.
- **2026-10-12 (morning)** Re-verified tracking to 4 cents: ClickBank 11 SALE rows at $409.26 against Meta's 11 purchases at $409.22. Confirmed no `prayersong-1` sale yet.
- **2026-10-12 (morning)** Added `02_QuietMinute` as a dead execution, the AQuietDevotion angle's 8th and the second-largest loss in the account.
- **2026-10-12 (morning)** Annotated `01_SistersThreeStates` as no longer meeting its dead-execution test at 1.21x on 28d. **Reversed the same evening at 0.81x and again today at 0.00x.**
- **2026-10-12 (morning)** Withdrew the practice of predicting window rolls after two wrong predictions in opposite directions.
- **2026-10-12 (evening)** Refreshed every window: 28d $1,070.26, 10 purchases, 0.35x. 7d $17.47, 0 purchases, and all of it Prayer Song spend.
- **2026-10-12 (evening)** Recorded the Prayer Song campaign's first full day, $17.47 for 14 outbound clicks and 0 purchases, all three ads TOO EARLY.
- **2026-10-12 (evening)** Recorded 0 Locked and 0 Potential Winners for the fourth consecutive day. Added no new dead executions or angles; refreshed all 22 entries and both dead-angle evidence blocks.
- **2026-10-12 (evening)** Annotated `01_KitchenMorning` and `01_CouchMorning` as having dropped below the $15 threshold. Recorded that `01_SistersThreeStates` had oscillated across the profit line three times on window convention alone.
- **2026-10-12 (evening)** Order bump flagged for the fourth consecutive day with no change. Noted the Meta Ad Library API was permission-blocked, leaving the project without competitor evidence for four days.
- **2026-10-14** **Competitor evidence is available again.** The Ad Library **API** is still permission-blocked, but the public Ad Library **website** reader produced a fresh pull dated 2026-10-14 covering "catholic rosary gift" (about 98 active ads), "catholic prayer bracelet" (about 48) and "personalized prayer song" (about 590), plus a one-off search on "personalized song gift" (about 1,700). The four-day evidence blackout is over.
- **2026-10-14** **DECLARED A NEW DEAD ANGLE: SistersThreePack.** 4 executions, $92.18 on the inclusive window, 0 purchases, after `01_SistersThreeStates` crossed $50 with zero sales. Recorded the window dependency honestly: on the complete-day window the same ad reads $58.02 with 1 purchase, which does not meet the test. The declaration rests on the four-execution record and LEARNINGS' 2026-09-28 kill, not on the cent-level flip alone. This also closes a five-reading oscillation.
- **2026-10-14** **Added one new dead execution, `01_SonOpen_v2` ($15.10, 0 purchases, CTR 10.50%), and marked its diagnosis undiagnosable.** The rule fires at ten cents over the threshold on 13 link clicks. The hook and visual are explicitly not condemned. Total is now 23 across 15 angles, ten of them annotated as no longer strictly meeting their test.
- **2026-10-14** **Annotated two dead executions that have risen above the line on today's window**: `03_OneEachThreeOfUs` now 1.43x on 28d (recorded at 0.92x) and `02_ParkedAndEarlyRosary` now 1.44x on 14d (recorded at 1.09x). Both retained, both paused, neither promotable.
- **2026-10-14** Recorded 0 Locked and 0 Potential Winners for the **fifth** consecutive day, and that **the account's last sale was 2026-10-01, thirteen days ago.**
- **2026-10-14** **Recorded that `SungByName_UGC_2026-10-10` is now CAMPAIGN_PAUSED** after two days, $38.15 and 0 purchases on 29 link clicks.
- **2026-10-14** **Recorded `SungForTheHolySouls_PHOTO_2026-10-12` live from today**, 3 ad sets at $5/day, first partial day $16.03 for 308 impressions, 32 clicks, 10 outbound clicks and 0 purchases. All three ads TOO EARLY.
- **2026-10-14** **Recorded `SungByName_VID_2026-10-13` as ACTIVE and self-starting 2026-10-15** with four ad sets, `GodmothersPromise`, `HoldThemNear`, `NobodySaysHers`, `FontAndTheName`. From tomorrow the account carries seven live ad sets at about $35/day on an offer with no sales.
- **2026-10-14** **FLAG A: both new campaigns have campaign status ACTIVE rather than PAUSED.** Either TS published them, which is the intended flow, or they were built active, which breaks the standing rule. Flagged only; no ad state was changed.
- **2026-10-14** Confirmed both new campaigns carry `locales: [6, 24]`, English (US) or English (UK), satisfying the English-only rule. The three paused `SungByName_UGC` ad sets carry no `locales`.
- **2026-10-14** **VERIFIED THE PRAYER SONG CHECKOUT WORKS.** The live page returns HTTP 200 with a real `prayersong-1` / `template=songform` checkout link carrying the `vtid=[cmc_vid]` token, and that link renders ClickBank Secure Checkout. **The offer is buyable and has sold nothing.**
- **2026-10-14** **New evidence on the order bump, sixth flag.** The rendered `songform` checkout contains order-bump markup (`bump-container`, `bump-item`, `bump-copy`, `bump-image`, `bump-payment`, `bump-disclaimer-dof`) and a second priced line. **Whether a bump product is attached and crediting is not settled and is not claimed**; it needs checking on the ClickBank side.
- **2026-10-14** Re-verified tracking: ClickBank `karmacc` 2026-10-10 to 10-13 returned five rows, all `bump-blessing` rebills from legacy subscribers, and **zero SALE rows of any kind.** Meta's zero is real.
