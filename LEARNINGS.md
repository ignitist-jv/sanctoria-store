# divine-grace-gift — Learnings Log

Project metadata, test results, customer insights, and accumulated wisdom for this offer.
Updated continuously. Claude reads this at the start of every session in this folder.

---

## Project Snapshot

- **Site/URL:** divinegracegift.com
- **Audience:** Catholic women 45+, prayer-driven, traditional/devotional
- **Product:** Blessed rosary + devotional bundle
- **Notes:** Main DGG offer. Active funnels: prayer-rosary-v4-love, v5 direct-sale, v6-bracelet variant.

---

## Winning Angles (top performers)

> What's outperformed. Include ad name, ROAS/CVR, why it worked.

- **Old Ads 4 New Page / "New Rosary - 4"** (Ad Set `120245963291750135`, Ad `120245963291670135`, campaign `120245962916110135`) — **ROAS 5.44x (14d) / 4.72x (7d), CTR ~21%, 4 sales, $50 spend.** A proven legacy rosary ad repointed to the new `/new-rosary/` direct-sale page. The relaunch thesis is working: old winning angle + new page = top ROAS in the account. (Confirmed 2026-06-25; scale gradually, sample still only 4 sales.)
- **"The Pattern Ends With You" / `AS4`** (Ad Set `120245116749090135`, Ad `120245116749100135`, campaign `120245116592460135`) — **ROAS 1.50x (28d) / 1.48x (14d) / 1.76x (7d), 9 sales, $168 spend, CTR ~5.4%, freq ~2.0.** Established, consistent profit over the meaningful window. Generational "pattern ends with you" angle. Scale candidate. (Confirmed 2026-06-25.)
- **Old Ads 2 New Page / "New Rosary - 2"** (Ad Set `120245963291600135`) — **ROAS 3.27x (14d/28d), 4 sales**, repointed legacy ad on the new page. 7d dipped to 0.82x on a 2-sale sample (variance, low freq 1.33, not fatigue); kept, not killed, because 14d/28d are well above the line.

### Sanctoria account `462874384767571` (2026-09)

**CORRECTED 2026-09-28. THE MECHANISM IS AQUIETDEVOTION, NOT FAMILY MULTI-PACK.**

The 09-17 finding below was wrong and cost about ten days of misdirected creative. The claim was
that "a woman buying for female relatives, always a multi-pack" was the winning mechanism. By
end of September the family angles had all faded (SistersThreePack killed at 1.10x, DaughterPack
killed at 1.08x) while **AQuietDevotion, a SOLO-wearer angle, became the account's franchise:
9+ sales across four campaigns, and the only consistently above-line performer.**

The real mechanism: **a small, private, ordinary moment that already exists in her day, plus an
object that gives her hands something to do in it.** Not gifting. Not family. The stolen ten
minutes. Winning scenes: before the house wakes, the school car park, the driveway.
Its refresh `BeforeTheHouseWakes` `120256381145120051` ran 2.83x on 14d/28d.

**Why I got it wrong:** the family angles converted first and loudly (2 to 3 sales each in a
short window), which looked like a mechanism. They were early-sample noise on a thin-margin
account. See the kill-threshold statistics under Dead Angles: at $15 per test this account
cannot distinguish an average ad from a bad one, so early wins and early losses both mislead.

**Superseded (2026-09-17, kept for the record):** "every ad set that has ever converted runs one
mechanism: a woman buying for the other women in her family, with the multi-pack as the thing
that makes it easy." True of the first 8 sales. Did not hold.

**UNEXPLOITED (found 2026-09-27):** the VOC file's pain point #10 is *"Asking God directly and
feeling unheard. Catholic women hit this wall and start looking for intercession (Mary,
saints)."* The product is the St Benedict **Marian** Bracelet and carries the **Miraculous
Medal**. Across ~40 ads written for this account, **exactly one headline has referenced Mary,
Mother, intercession or novena.** The Vocabulary Map DO-USE list names all four. This is the
largest untested fit in the account. First test built 2026-09-27: `01_AskingHisMother`
ad `120256503429940051`, paused.

- **SistersThreePack** (Ad Set `120256241056110051`, Ad `01_SistersThreeStates` `120256241056050051`)
  — **2.30x all-in, 2.52x 14d/28d, 2 sales on $36.78, CTR 7.6%, freq 1.18.** Best ROAS in the
  account. Three sisters in three states, ordered the 3-pack, posted them with no note.
  **⚠️ THE AD SET IS MISLABELLED** `T1_MF_35-65+_StoppedHidingIt_UGC_ParkingLot`, a name reused
  from the paused video batch. It does NOT run StoppedHidingIt. `utm_term` has been writing the
  wrong angle to ClickMagick since launch. Rename recommended 5 times, not yet done.
- **DaughterPack** (Ad Set `120256178585970051`, Ad `04_DaughterTwoPack` `120256178585990051`)
  — **2.11x all-in, 2.11x 14d/28d, 3 sales on $88.37, CTR 14.55%, freq 1.25.** Highest absolute
  profit in the account ($186.03 returned). Mother gives one to her adult daughter, 2-pack.
  Originally produced the account's best AOV at $76.50.
- **ThreeGenerations** (Ad Set `120256276845670051`, Rosary funnel) — **1.38x all-in, 1.43x
  14d/28d, 1 sale on $23.97, CTR 9.24%.** The ONLY ad set on any of the three new funnels
  (Triptych, Necklace, Rosary) that has ever converted. Grandmother / mother / daughter, 3-pack.
- **AQuietDevotion_PHOTO_Quiet** (Ad Set `120256136639870051`) — **1.41x all-in, 1.45x 14d/28d,
  2 sales on $69.90, CTR 5.30%.** The one solo-wearer winner, and the weakest of the four.
  Declining steadily every check: 2.15x, 1.91x, 1.75x, 1.61x, 1.41x. Treat as the control, not
  a seam to multiply.

---

## Dead Angles (don't repeat)

> What flopped. Save future time by not retrying these.

- 2026-07-10: **TheStreakThatWontBreak `120247196159960135`** (Jul-8 bracelet spinoff cohort) KILLED. ~$15.7 spent, 0 sales, CTR 3.06% (weakest of its cohort), freq 1.64. Failure = **audience/offer problem, not hook** — its sibling ad set `120247196162630135` runs the same "Streak" angle at 11.3% CTR and stays live. Don't retry this exact audience/placement mix for the Streak angle.

### ⚠️ THE $15 KILL THRESHOLD CANNOT PRODUCE A VALID VERDICT (funnel audit, 2026-09-23)

Unit economics measured on **outbound clicks**, not raw clicks: **$1.27 cost per outbound
click, 3.07% site conversion, $50.24 AOV**, giving $1.54 revenue per click against $1.27 cost.
Real but very thin.

**$15 of spend buys about 12 outbound clicks. At the account's own 3.07% CVR, an ad performing
exactly at average shows ZERO sales 69% of the time.** The kill rule has therefore been
discarding roughly two thirds of average ads as failures. Roughly 90% confidence needs about
**75 outbound clicks, or $95 per test**. Judge at the mechanism level by pooling 3 ads, or raise
the per-ad threshold to $30. Do not read a single $15 test as a verdict.

**Also corrected by that audit:** reported CTR is inflated. Only **31 to 51%** of Meta's counted
clicks are outbound; the rest are photo expands and "see more" taps on long copy. True link CTR
is 3 to 7%, not the 10 to 20% previously reported. **Long line-broken primary text is the cause**,
and it is a real cost problem: `UGCEveryday_DaughterPack` lost 69% of its clicks that way and
paid $1.96 per outbound click against the $1.27 blend, which is what killed it despite an
above-average 3.4% CVR.

### Sanctoria `462874384767571` (2026-09): the funnel, not the creative

**THE PATTERN: every single kill in this account has good CTR and no sale.** Across roughly
20 killed ad sets the CTRs run 5% to 20%, against a 1 to 2% Meta norm. Not one kill has ever
been a creative problem. The hooks work; the pages do not convert the clicks. `/funnel-audit`
has been recommended on 7 consecutive checks and never run. **Stop diagnosing creative.**

- 2026-09-17: **The Triptych funnel `/guard/` is 0 for 3.** `TheDrawerOne_DrawerDish`
  `120256276845770051` ($16.86, CTR 14.98%), `MenWhoWearIt_EngineGrease` `120256276845780051`
  ($16.70, CTR 12.88%), `KeepOneGiveOne_TwoWrists` `120256276845790051` ($16.49, CTR 10.90%).
  Three angles, $50, zero sales, CTRs up to 15%. **Audience/offer problem. The page is the
  suspect, not the angles.** Do not rework Triptych creative before auditing `/guard/`.
- 2026-09-17: **Rosary funnel 1 for 3.** `InheritedByDaughters_GloveBox` `120256276845650051`
  ($17.53, CTR 15.55%) and `NeverLearnedItProperly_LostMyPlace` `120256276845660051` ($17.72,
  CTR 16.26%) both killed dry. Only the 3-pack angle (ThreeGenerations) converted, which is the
  mechanism finding again.
- 2026-09-17: **The whole AQuietDevotion_UGC trio died together**, all audience/offer:
  `Couch` `120256150053270051` (0.87x final, $48.74, CTR 14.58%), `Cardigan` `120256150053240051`
  (0.92x, $50.55, CTR 12.81%), `Kitchen` `120256150053250051` (1.07x, $47.90, CTR 11.61%).
  Three solo-wearer angles, ~$147 spent, 3 sales total. Solo angles underperform family angles
  roughly two to one on this account.
- 2026-09-14: **Five of six gifting angles died at the page.** `BoughtOneForMyself`
  `120256241056150051`, `MyDadWearsIt` `120256241056140051`, `ForMySonLeavingHome`
  `120256241056120051`, and the ad set labelled `MenWhoPray` `120256241056130051` (which
  actually ran TheGodmotherGift). All $8 to $11, zero sales, CTRs 5.33% to 14.77%. The only
  survivor was the 3-pack sisters angle. **Male-recipient and solo gifting angles have never
  converted here; female-relative multi-pack angles have.**
- **Necklace funnel `/necklace/` is untested.** Three ad sets got $15.10 of partial delivery on
  2026-09-16 and were stopped mid-test. No verdict earned. Do not record as dead.

---

## Customer Language to USE

> Verbatim phrases from customers (Reddit, reviews, emails, replies).
> Steal these into ads, headlines, emails.

### Top 10 Verbatim Phrases (from Reddit, 2026-05-12 + 2026-05-26 scrapes)

1. "You don't need to push harder you need to feel safer." (r/NevilleGoddard, 1,908 upv) https://www.reddit.com/r/NevilleGoddard/comments/1oiyemx/i_finally_found_out_why_living_in_the_end_felt_so/
2. "It wasn't my mind that was resisting. It was my nervous system." (r/NevilleGoddard, 1,908 upv) same source
3. "How will I pay this bill? Oh wait, I am abundant. It'll be taken care of." (r/NevilleGoddard, 1,475 upv) https://www.reddit.com/r/NevilleGoddard/comments/1mu970e/i_manifested_5000_today_heres_how_you_will_do_it/
4. "I resent my parents for teaching me nothing about money and then judging me for struggling with it." (r/AdultChildren, 88 upv) https://www.reddit.com/r/AdultChildren/comments/1pgpikq/i_resent_my_parents_for_teaching_me_nothing_about/
5. "Well- the cycle stops with me." (r/AdultChildren, 52 upv) https://www.reddit.com/r/AdultChildren/comments/1oxi0yw/i_feel_like_no_one_can_understand_the_pain_of/noxpg8i/
6. "Ask and you shall RECEIVE 🙌" (top comment on $5K manifestation post, 119 upv) https://www.reddit.com/r/lawofattraction/comments/1rjzil8/major_cheat_code_in_life/o8hbib4/
7. "Turn your life into 'already done' mode. Pretend you've had everything you want for so long it's boring now." (r/NevilleGoddard, 2,183 upv) https://www.reddit.com/r/NevilleGoddard/comments/1mimpfb/i_affirmed_robotically_for_15_weeks_heres_what/
8. "I had bills I couldn't pay, my skin was breaking out so bad I didn't want to look in the mirror, and I felt invisible in every area of my life." (r/NevilleGoddard, 1,489 upv) https://www.reddit.com/r/NevilleGoddard/comments/1ntyj9z/how_to_make_yourself_believe_when_you_really_dont/
9. "I don't trust any of them tbh. All of them are either trying to sell you something, or just repeating the same tired information you can find anywhere else (for free)." (r/Manifestation, 123 upv) https://www.reddit.com/r/Manifestation/comments/1t0dt3g/youtube_manifestation_coaches_you_swear_by/oj8dm71/
10. "Inheritance ruins families." (r/witchcraft, 408 upv) https://www.reddit.com/r/witchcraft/comments/1pb51gz/first_money_bowl_was_a_success/nrpzesw/

### Top 10 Pain Points (ranked by frequency across the wealth-manifestation + ancestral Reddit scrapes)

1. **Bills they can't pay; 3 AM panic attacks about money.** ~200 mentions across "broke", "debt", "bills", "can't afford".
2. **Inherited financial illiteracy plus active shame from parents.** "Parents taught me nothing about money, then judge me for struggling." 88-upv thread; recurring across r/AdultChildren and r/povertyfinance.
3. **Nervous-system exhaustion from forcing prayer or visualization to "work".** Body refuses to relax into belief while 3D reality contradicts the wish. ~180 mentions.
4. **Watching adult children repeat the family's money pattern.** "The cycle stops with me." Strong matriarch / legacy motivation.
5. **Method confusion / "HOW exactly?"** "We need to know exactly what to do." Audience wants a specific named pathway, not vague advice. ~230 mentions.
6. **Distrust of selling gurus + manifestation YouTubers.** "Either trying to sell you something, or just repeating the same tired information." Big trust gap.
7. **Feeling unworthy or "not good enough for this life".** "People like us don't have money." Starting point in nearly every breakthrough story.
8. **Praying for the same loved one for 10+ years with no answer.** Sick spouse, prodigal child, wayward sibling. High emotional commitment.
9. **Carrying both the damage and the blame.** Parentified adult children who cleaned up parents' financial mess and now get judged for their own struggles.
10. **Asking God directly and feeling unheard.** Catholic women hit this wall and start looking for intercession (Mary, saints) or another way in.

### Customer Vocabulary Map (for DGG ad/sales-page copy)

- **DO use:** receive, ask, pray, rosary, Mary, Mother, novena, blessed, handcrafted, weight in your hand, drawer, kitchen table, grandmother, daughter, granddaughter, 800 years, peace first, intercession, grace, mercy, family, line, bloodline.
- **DO NOT use:** manifest, attract, vibration, energy, universe, frequency, quantum, vibe, raise your vibe, seed faith, name it and claim it, breakthrough anointing, unlock, magic, lucky, generational curse (Catholic posters reject this term, use "family tree healing" or "praying for ancestors" instead).

---

## Customer Language to AVOID

> Phrases that misfire for this audience (wrong vocabulary, wrong vibe).

- *(none yet)*

---

## Objections Encountered + How We Answer Them

> Each objection and the response that lifted conversion.

- *(none yet)*

---

## Active Tests

### 2026-09-09 - /bracelet-v2/ hero + offer-clarity test  [OPEN, REVIEW 2026-09-12]

**Page:** https://sanctoriastore.com/bracelet-v2/ . This is the ONLY page taking paid traffic and it produced 38 of 39 front-end sales between Aug 10 and Sep 7. Note ads point at /bracelet-v2/, not /bracelet/; CLAUDE.md was stale on this.

**FIVE changes shipped the same day. A lift is the sum of all five, not the hero alone.**

1. Hero rebuilt on the PatternEndsWithYou angle (peaked 6.6x on this SKU, then 1.50x steady over 9 sales).
   - eyebrow: `Three Generations - One Decision`
   - h1: `Worry runs in families. / So does devotion. / It stops with you.`
   - sub: `A blessed medal in a dish. A rosary in a drawer. In most Catholic homes they stopped being carried. This one is hand-knotted in ebony to stay on, blessed in Rome.`
   - Thesis: the control sold provenance and bequest; every angle that has won for this offer sells intervening for someone struggling NOW. The sub supplies the missing bridge, the drawer mechanism, so "stops with you" has a physical answer.
   - Control and the first sub draft are both preserved in an HTML comment above the hero for a one-step revert.
2. Checkout-button anchors aligned to the tier cards. Buttons had shown $76/$129/$184 while the cards showed $42/$84/$126, a visible contradiction at the click.
3. "Save up to 35%" corrected to 55%, the real maximum against those anchors.
4. Per-tier savings added to the CTAs: `You Save 12% / 44% / 55% Today`.
5. Sticky buy bar added, appearing once the batch card scrolls past, hiding while the open tier's real button is on screen. The page previously had no persistent CTA.

**BASELINE TO BEAT** (Aug 10 to Sep 7, Meta acct 462874384767571, ClickBank nickname karmacc):

| Metric | Baseline |
|---|---|
| Spend | $2,839.35 |
| Link clicks | 2,730 at $1.04 CPC |
| Purchases | 43 at $66.03 CPA |
| Meta ROAS | 0.67 |
| ClickBank product revenue | $2,828.41 |
| Product revenue per link click | $1.04, i.e. exact break-even before the rebill |
| Front-end AOV | $49.91 |
| AOV per order | $62.85 |
| Pack mix | single 44.7% / pair 39.5% / household 15.8% |
| Upsell take | 10.3% of front-end |
| Downsell take | 5.7% of decliners |
| Order-bump attach | 15.4% |

**WHAT TO CHECK ON REVIEW**
- ROAS and CPA against the table above.
- **Pack mix, not just ROAS.** The replaced hero was built on the logged `InheritedByDaughters` angle, explicitly aimed at driving the Family and Household tiers, and those tiers are 55% of sales. If Option A lifts conversion but shifts buyers to the single, you can win CVR and lose revenue. Option A argues three generations, so household share is the specific number to watch.
- CTR, and whether the anchor and savings changes moved the pair-versus-household split.
- Landing page views are NOT reliable on this account (CAPI only, browser pixel deliberately removed 2026-07-20). Meta showed 2,730 link clicks against 203 landing page views for the baseline window, which is almost certainly a measurement gap rather than a 93% bounce. Trust ClickBank actuals. Microsoft Clarity would settle it, but the Clarity MCP is currently authenticated against a different property (getbirthcode.com); the Sanctoria project is `ydd7lw8hiu` and needs its own Data Export token connected.
- `cb_get_orders` caps at 100 rows, so pull a narrow window and aggregate SALE rows yourself. The `cb_get_sales` summary undercounts badly.

**KNOWN CONFOUNDS AND OPEN ISSUES ON THIS PAGE**
- Fabricated proof still live and untouched by choice: "4.9", "1,847 verified reviews", "Angela D., Brooklyn", "94% Reserved", "23 Reservations Remaining". These are the same class of figures deliberately excluded from the Triptych and rosary pages.
- Metal named inconsistently across the site: "brass" 12 times on /bracelet-v2/, "bronze" 29 times on /bracelet/, same physical product. Unresolved.
- "Blessed in Rome" and "blessed by the chaplain" here versus "hand-blessed in the Benedictine tradition" on the other three product pages. User confirmed 2026-09-09 that the Rome claim is accurate, so it was kept, but the pages do not match each other.
- The $17/month `bump-blessing` rebill carries the account's entire margin ($813.64 across 41 active subs in the baseline window, 22% of revenue) and also generated 3 of the 4 refunds and chargebacks in that window. Making its terms explicit at the point of consent is the highest-value fix outside the page itself.

## Key Data Points

- **AOV:** TBD
- **Email CTR:** TBD
- **Best audience:** TBD
- **CVR baseline:** TBD

---

## Locked Product Specifications

> Use these exact specs in every image prompt, ad image brief, photographer brief, and sales page description. Do not improvise. Do not substitute.

### ⚠️ SUPERSEDED FOR THE 2026-09 ROSARY: read this first

The spec immediately below (lava stone beads, Our Lady of Guadalupe centerpiece, silver + gunmetal, "never gold") describes the OLD DGG rosary and is **wrong for the rosary now selling at /rosary-necklace/**. Do not use it for image prompts or ad briefs for that product.

**The Saint Benedict Cord Rosary (LOCKED 2026-09-03), the current product:**
- **Beads:** black matte WOOD, round, sanded not polished. NOT lava stone, NOT porous, NOT glossy.
- **Stringing:** black braided CORD, knotted on both sides of every bead. NOT a metal chain.
- **Our Father beads:** a few pale/white beads at the head of each decade.
- **Medals:** silver-tone SAINT BENEDICT medals spaced along the whole length, plus one larger OVAL Saint Benedict centerpiece at the join. There is NO Guadalupe medallion on this product.
- **Crucifix:** BLACK WOOD, silver Christ corpus, INRI plaque, and a small silver Saint Benedict medal inset where the beams cross.
- **Palette:** matte black + silver only. Rustic and monastic, never ornate or shiny.
- **Ships with:** drawstring pouch + printed Saint Benedict prayer card.

---

### St Benedict Rosary Necklace (LOCKED 2026-05-27)

**Form factor:** Full rosary necklace, worn around the neck, Y-drop format with crucifix dangling at solar plexus / heart level. Total length falls to roughly mid-chest.

**Beads:** Black LAVA STONE. 6mm to 8mm round. Porous, volcanic texture (visible pores). Matte black, no gloss. The natural roughness of lava stone is a key visual differentiator. NOT ebony wood, NOT plastic, NOT hematite.

**Metal:** Polished SILVER (medals and crucifix) + dark gunmetal / oxidized pewter chain. Visual contrast = dark chain + bright silver accents. NOT brass, NOT gold, NOT antique brass, NOT bronze.

**Centerpiece (the visual focal point in most shots):** OUR LADY OF GUADALUPE medallion. Tall oval shape, approximately 25mm x 35mm. Bright polished silver, raised relief showing the Virgin of Guadalupe figure with halo rays radiating outward, hands folded in prayer, traditional Guadalupe pose with stars on her cloak. Connects to the chain via two small loops at the top.

**Chain accents (throughout):** Multiple smaller Saint Benedict medal beads integrated as bead links along the chain. Approximately 8 to 10 visible. Each ~7mm round. Shows the Saint Benedict figure on the front. "VRSNSMV SMQLIVB" exorcism initials around the rim. Polished silver finish, contrasting with the black lava stone.

**Crucifix (hangs at the bottom of the Y-drop):** Ornate filigree silver crucifix, approximately 40mm tall. Detailed Christ figure with crown of thorns in raised relief. INRI titulus banner at the top. Decorative scrollwork on all four arms of the cross. Hangs from a final small Saint Benedict medal bead at the bottom of the Y-drop.

**Color palette for image prompts (use these hex codes):**
- Polished silver: #C9CBD1
- Dark gunmetal / oxidized chain: #5A5A60
- Lava stone black: #14110F
- Cream / linen background: #F5F0E8
- Warm accent (light only, not metal): #D4AF37 used very sparingly, candle glow only
- Deep coffee shadow: #3D2817

**Positioning note:** The Our Lady of Guadalupe centerpiece IS the visual proof of the Marian devotion claim ("Blessed in Rome. Worn by Mothers. Inherited by Daughters."). Foreground the Guadalupe medallion as the visual focal point whenever possible.

**Image-prompt rules going forward:**
- Foreground the Guadalupe medallion in product shots (it does the Marian positioning work no copy can match)
- Show the chain integration of Saint Benedict medals (it's a brand differentiator)
- Show the Y-drop layout with crucifix at the bottom (it's clearly a necklace, not a bracelet or pendant alone)
- Lava stone texture must read as porous and natural, not smooth or polished
- Metal palette is SILVER + GUNMETAL, never brass or gold
- NO CTA buttons rendered into image prompts. Headline text only. Buttons live in the ad platform UI, not in the image.

---

### The Benedict Double Protection Necklace: CORRECTED FROM REAL PHOTOS 2026-09-09

The spec below SUPERSEDES the 2026-08-31 lock. Real supplier photographs arrived on 2026-09-09
(archived at images-originals/necklace-real/) and the shipped images were materially wrong.
All 11 page images were regenerated against those photos and replaced.

TRUE GEOMETRY, from the photographs:
- CHAIN: a FINE ROUND SNAKE CHAIN, about 1.2mm, TWO strands. Delicate, drapes softly.
  It is NOT a flat snake band, NOT a woven mesh rope, NOT a herringbone ribbon.
- FRONT JUNCTION: both strands terminate at the FRONT. Exactly TWO slim tapered end caps,
  ONE small lobster clasp, a few 4mm jump rings. There is NO large O-ring. The cross hangs
  from one ring and the medal from an adjacent ring.
- CROSS: slim Latin cross about 34mm, FLAT-FACED bars, softly rounded edges and tips.
  Not chunky, not puffy, not tubular. No corpus.
- MEDAL: round, about 17mm, plain flat rim, no beading, no bezel, small integrated loop bail.
- RATIOS: cross about 2x the medal's height. Medal about 14x one chain strand's thickness.
- FINISH: warm satin yellow gold, darker in the medal's recesses. Not mirror chrome.

WHAT WAS WRONG ON THE LIVE PAGE BEFORE THIS FIX:
1. pair-hero1 rendered the chain as a THICK WOVEN MESH ROPE, staged coiled at bracelet scale.
2. pair-worn, pair-collar and pair-everyday rendered it as a WIDE FLAT HERRINGBONE RIBBON
   hanging from a single large O-ring, with no end caps and no clasp.
3. pair-3 showed the supplier's card with "SPIRITUAL JEWELRY COLLECTION" legible on it,
   a third party brand name sitting on our own sales page.
Root cause: the chain and the junction were left to the model to invent, so it fell back on
generic stock jewellery shapes every time.

THE FIX THAT WORKED, reusable for any product:
- Attach the real product photos as generation references. Without them the model will never
  guess an unusual construction like a front-mounted clasp junction.
- NEVER specify a dimension in millimetres. An image model has no absolute scale, so "1.2mm"
  is ignored. Anchor every dimension to something else IN THE FRAME instead:
     "each chain strand is one fourteenth the diameter of the medal"
     "if the medal is drawn 140 pixels wide, each strand is about 10 pixels"
     "each strand is one sixth the width of the cross's vertical bar"
  The first pass used millimetres and came back at roughly twice the true thickness.
  The ratio wording cut the error by more than half in a single retry.
- Add a self-check the model can see: "because the chain is so fine, the end caps look
  noticeably wider than the chain they finish".
- State a direction to err in: "err on the side of too thin", and "if the chain looks
  substantial or ropey it is WRONG".
- Keep a STRICT HARDWARE COUNT naming the specific phantom part to exclude, by name.
  "NO large O-ring" was necessary; a generic "no extra hardware" had not worked.

### The Benedict Double Protection Necklace (LOCKED 2026-08-31, renamed from "The Benedict Pair" 2026-09-05)

**Form factor:** Necklace. Double-strand flat snake chain (two parallel smooth ~2mm strands of EQUAL length lying together as one pair), gathered into slim polished gold end caps meeting a lobster clasp with a round jump ring. Sits at the center of the chest, high enough to disappear under a collar.

**Metal:** Warm yellow GOLD tone, polished, 18K gold plated over stainless steel. NEVER silver, NEVER rose gold, NEVER antique or oxidized brass.

**Pendants (both hang from ONE shared larger gold ring, on small round jump rings):**
1. **Plain Latin cross**, smooth polished rounded-square section arms tapering slightly, ~35mm tall. NO Christ figure. It is a CROSS, not a crucifix. No engraving, no texture. Hangs lower and slightly in front.
2. **Round Saint Benedict medal**, flat disc 16mm (1.6cm / 0.63in, confirmed from a supplier dimension diagram), raised relief of Saint Benedict standing with a staff and a book, letters ringing the rim, PLAIN POLISHED GOLD EDGE. Absolutely NO black enamel, NO black bezel, NO dark outline ring. Sits beside the cross, slightly overlapping and slightly behind.
3. The medal is clearly SMALLER than the cross.

**THE FRONT JUNCTION (corrected 2026-08-31 after a supplier macro; earlier renders got this wrong):**
The closure is at the FRONT CENTER as a visible design feature, immediately beside the pendants. It is NOT hidden at the back of the neck and it is NOT a single plain ring. Render all four parts:
1. Each doubled chain strand terminates in a LONG SLIM TAPERED POLISHED GOLD END CAP, an elongated cone roughly 12mm long narrowing to a point where the chain enters. Not a short stubby ferrule.
2. The LEFT end cap connects to a small round jump ring. From that small ring the two pendants hang, EACH ON ITS OWN SEPARATE SMALL JUMP RING (not both on one shared ring).
3. A POLISHED GOLD LOBSTER CLASP lies roughly horizontally at that same junction.
4. The RIGHT end cap connects to a LARGE THICK ROUND OPEN GOLD RING about 11mm across with a visibly round cross-section. The lobster clasp hooks INTO that large ring.

**Chain texture:** each strand is a flat woven chain about 2.5mm wide with a fine flat WOVEN MESH weave showing a close crosshatch texture. It is not a smooth mirror ribbon and not a beaded or cable chain.

**Ships with:** a printed Saint Benedict prayer card (Latin prayer plus English translation).

**Image-prompt rules (three failure modes that got renders rejected on 2026-08-31):**
- **Layered chains.** The model defaults to a stack of 2 to 3 necklaces at different lengths with the pendants split across them. Every prompt must say ONE SINGLE NECKLACE, two strands of the SAME length, both pendants on ONE shared ring, and negative-prompt layered necklaces.
- **Floating necklace.** Lifestyle scenes rendered the necklace detached and oversized in the foreground. State that it is worn on the body at realistic jewelry scale and negative-prompt floating/giant/detached jewelry.
- **Readable text.** Never allow a prayer card, book title, or packaging with words in a generated frame; describe the medal rim letters as "tiny softly abstracted indistinct letterforms that are not legible".
- Attaching a clean generated product render as a SECOND reference alongside the supplier photo fixed the chain geometry immediately. Do that for any further shots.

**Two more junction failure modes (found 2026-09-01, cost three regeneration passes):**
- **Chain renders as a thick mesh rope.** Asking for a "woven mesh" chain makes the model produce a chunky bracelet-weight band and merge the two strands. Fix: state the chain is DELICATE, that the strands are SEPARATE with a visible gap, and give a proportion rule ("the cross is about fourteen times wider than a single chain strand"). Negative-prompt thick chain, chunky mesh rope, wide band, strands merged.
- **A phantom third end cap appears.** Once the prompt describes tapered end caps, the model often renders a spare one floating in frame. Fix: state "HARDWARE COUNT IS STRICT: exactly TWO tapered end caps in the whole image, one per chain end, no third cap and no spare floating fitting", and negative-prompt third end cap / duplicate hardware.
- **Cheapest reliable macro:** do not generate the junction macro separately. Crop it out of the approved 2048px hero render. It is guaranteed consistent with the hero and costs nothing.

**Angle:** `HandToHeart` (see CLAUDE.md). Format code for ad naming: use the standard codes, e.g. `HandToHeart_PHOTO_YYYY-MM-DD`.

## Update Log

- 2026-10-14: **/scale-or-kill. No executable actions; the finding is downstream of the ads.** Holy Souls PHOTO launched today 03:00 SGT, 3 ad sets at $5/day: `BookAtTheBack` `120256761707940051` $7.47/7 outbound/$1.07 CPOC/12.20% CTR, `NamesReadAloud` `120256761711490051` $7.41/5/$1.48/12.75%, `CemeteryGate` `120256761709810051` $6.46/4/$1.62/11.41%. All day 1, all LEARNING with 0 conversions, all TOO EARLY. No early kill: the trigger is CTR under 0.5% and these run 11.4 to 12.8%. Recheck 2026-10-16.
  **SungByName_UGC stopped at $38.15 lifetime, 0 sales.** `01_SonOpen_v2` $15.10/13 outbound/$1.16 CPOC/10.50% CTR; `04_NameFirst` $11.76/11/$1.07/10.40%; `02_DaughterOpen` $11.29/5/**$2.26**/4.48%. **DaughterOpen is a creative problem**, cost per outbound click double its siblings on less than half the CTR, the same profile as `04_DaughterTwoPack` at $1.96 which was the account's largest single loss. **The daughter recipient has now failed twice; do not give it a third slot without a different mechanism.**
  **The ads are not the problem so far.** SonOpen, NameFirst and BookAtTheBack all beat the account's $1.27 blended cost per outbound click. Clicks are being bought cheaply; nothing is converting.
  **ClickBank reconciled to Meta exactly: zero Prayer Song sales, ever.** The only `prayersong-1` row is TS's own TEST_SALE, 2026-10-08, $43.04, SG. Last real front-end sale account-wide was **2026-09-30** (bracelet-1, $39.22), 14 days ago.
  **Order bump still not attaching, fifth consecutive flag.** 31 `bump-blessing` rebills worth $562.21 in the 28d window, every one with processedPayments 4 to 14, **zero first payments**, despite the express bump being configured on the songform checkout on 2026-10-12. If both are true, the ClickBank item number likely does not read exactly `express-1`, which is what `lib.php` matches on.
  **Open caveat on all of this:** the 3.07% site conversion rate used for sample-size maths is the BRACELET funnel's. Prayer Song has no CVR baseline of its own, so every "expected sales" figure is borrowed. Raw pull: output/ads/_data/2026-10-14-rawpull-clickbank.json
> Quick changelog so we can see velocity.

- 2026-10-01: **30-day converting-ad inventory + proven-angle refresh built.** Pulled ad-level data for 09-01 to 10-01: **9 ads produced 16 sales on $572.02 for $715.96, blended 1.25x.** Only three angle families clear the 1.2 line: **AQuietDevotion (3 ads, 7 sales, $200.70, 1.45x)**, **MenWhoPray PHOTO (1 ad, 1 sale, $15.27, 3.63x)** and **NovemberNames (1 ad, 1 sale, $17.28, 1.91x)**. The family multi-pack angles have the volume and lose money: DaughterPack 4 sales at 0.97x, SistersThreePack 2 at 1.10x, ThreeGenerations 1 at 0.92x. **Two corrections to this file.** (1) **Men's angles are not dead, the UGC FORMAT is.** `01_QuietMansFaith` `120256163362400051` (MenWhoPray_PHOTO, father's hands) is **the highest-ROAS ad in account history at 3.63x** and has been sitting paused, never refreshed. Every men's angle recorded in Dead Angles died in UGC; the one PHOTO version converted. The variable is format, not audience. Sample is 1 sale on 29 outbound clicks, so this is a lead to test, not a proven finding. (2) **The AQuietDevotion mechanism travels across products.** `02_ParkedAndEarlyRosary` `120256490331090051`, the 09-26 port of the angle from the bracelet to the rosary funnel, returned **2.74x**. It is not bracelet-specific. Built: campaign `ProvenRefresh_PHOTO_2026-10-01` `120256577692480051` set to PAUSED, 5 ad sets at $5/day, start 2026-10-03T03:00 SGT, 1 ad each, 2 AQuietDevotion + 2 MenWhoPray PHOTO + 1 NovemberNames. All 10 entities returned `active_errors: []`. **TWO NEW API LESSONS, both cost a full rebuild.** (1) **`ads_creative_upload_image` is dead on this account** ("Authorization Error", 6 tries; `ads_creative_upload_media` and `ads_creative_upload_local_image` both answer "gradually rolling out"; media-buyer `propose_upload_image` is classifier-blocked). **The workaround: pass `image_url` straight to `ads_create_creative`** and Meta ingests the image and mints a hash itself. (2) **But a creative built from `image_url` cannot publish** because link_data then carries both `picture` and `image_hash`, which trips `ObjectStorySpecRedundant` (error 1443051) at publish time. **The correct two-step: create a throwaway creative with `image_url` to mint the hash, read the hash back via `ads_get_creatives` with field `image_hash`, then build the real creative with `image_hash`.** (3) **Never call `ads_update_entity` mid-chain on an MCP draft.** Pausing the campaign before the ad sets and ads existed silently destroyed the whole draft (campaign `120256577277040051` and its 5 ad sets became unresolvable). Build campaign to ad sets to ads in one uninterrupted pass, pause only at the end. Also note `ads_create_campaign` accepts no `status` argument, so every MCP draft specs ACTIVE and must be paused after the chain completes; the 2-day scheduled start is what keeps that safe. Images rendered, product-verified and CDN-hosted. One image discarded pre-build (`01_BeforeIGetDressed`, bare legs in a dim bedroom, adult-content rejection risk) and replaced with a clothed staircase scene. ClickBank `karmacc` still unreconciled (13th consecutive session). Copy: output/ads/2026-10-01-proven-refresh/COPY_ProvenRefresh.md.
- 2026-09-28: /scale-or-kill run. 4 active, blended 1.35x on $353.40. **Two major corrections written into this file.** (1) **The 09-17 "family multi-pack" mechanism finding was WRONG.** Both family angles are now dead (SistersThreePack killed 09-27 at 1.10x final, DaughterPack killed today at 1.08x) while the solo AQuietDevotion angle became the franchise at 9+ sales. Real mechanism: a small private moment plus something for her hands. (2) **The $15 kill threshold cannot produce a valid verdict** on this account's economics: it buys ~12 outbound clicks, and an average ad goes dry 69% of the time at that sample. Also recorded: reported CTR is inflated 2 to 3x because only 31-51% of clicks are outbound, and long line-broken copy is the cause. Today: 1 KILL (UGCEveryday `120256178585970051`, below line on 14d and 28d, diagnosed as a CPC problem at $1.96 per outbound click, not a CVR or angle problem), 3 WATCH, 0 scale. TS executed yesterday's Sisters kill and the BeforeTheHouseWakes scale to $6.50. **Largest unexploited opportunity identified 09-27: Mary and intercession**, named in the VOC file as pain point #10 and in the DO-USE vocabulary, referenced in exactly one headline out of ~40. ClickBank still unreconciled. Raw pull: output/ads/_data/2026-09-28-rawpull.json.
- 2026-09-19: /scale-or-kill run (Sanctoria `462874384767571`, profit line 1.2x). 4 active ad sets, blended 1.84x on $219.02. **Backfilled 2026-09-13 to 2026-09-17, which had not been logged.** Added the Sanctoria winners block (SistersThreePack 2.30x, DaughterPack 2.11x, ThreeGenerations 1.43x, AQuietDevotion_PHOTO 1.41x) and **the mechanism finding: every converting ad set is a woman buying for female relatives, always a multi-pack.** Added Dead Angles block covering ~13 kills from 09-14 and 09-17 (Triptych 0 for 3 at $50, Rosary 1 for 3, AQuietDevotion UGC trio, five of six gifting angles) with the cross-cutting pattern that **every kill in account history has good CTR and no sale, so it is audience/offer, never creative.** Today: 1 SCALE (Sisters $5 to $6.50, recommended 4 checks running and still not applied), 1 REDUCE (AQuietDevotion_PHOTO $5 to $4, five straight checks of decline), 2 WATCH. No kills. 2026-09-18 was a zero-sale day across all four. **ClickBank NOT reconciled for the sixth consecutive day** (`cb_get_orders` only has `wealthapa`, returns 401; `karmacc` not configured) so all ROAS above is Meta CAPI only. Unresolved: the SistersThreePack ad set is still mislabelled `StoppedHidingIt_UGC_ParkingLot`, corrupting `utm_term`. Raw pull: output/ads/_data/2026-09-19-rawpull.json.
- 2026-05-27: LEARNINGS.md initialized
- 2026-05-27: Added top 10 verbatim phrases and top 10 pain points under Customer Language, sourced from outputs/wealth-manifestation/findings-2026-05-12-general-reddit.md and findings-2026-05-26-reddit-ancestral.md. Added vocabulary map (do/don't word list) at end of Customer Language section.
- 2026-05-27: Added Locked Product Specifications section. St Benedict Rosary Necklace spec locked: lava stone beads, polished silver + gunmetal chain, Our Lady of Guadalupe centerpiece, multiple Saint Benedict medal accents through chain, ornate silver crucifix, Y-drop necklace format. Image-prompt rules: no CTA buttons rendered into image, foreground Guadalupe, silver palette only (no brass/gold). Replaces incorrect spec used in image-prompts v1 (which assumed ebony wood + antique brass + Saint Benedict centerpiece).
- 2026-06-25: /scale-or-kill run (account 1091652249458429, profit line 1.2x). Added 3 winners to Winning Angles: "New Rosary - 4" (5.44x, the relaunch proof), "The Pattern Ends With You / AS4" (1.50x, 9 sales, established), "New Rosary - 2" (3.27x 14d, kept despite 7d dip via override rule). 6 newer ad sets too-early (StoodInTheDoorway, KnotInTheThread, LastNameOnTheList, Pattern 1/2/3). No kills. ClickBank not reconciled this session. Raw pull: output/ads/_data/2026-06-25-rawpull.json.
- 2026-06-27: /scale-or-kill recheck. Winners strengthened: AS4 now 1.66x/11 sales (28d), Old Ads 4 now 5.04x/5 sales, Old Ads 2 held at 2.66x (14/28d). Both AS4 and Old Ads 4 moved to SCALE + refresh-worthy. User had paused the prior too-early sets (StoodInTheDoorway/KnotInTheThread/LastNameOnTheList + Pattern 1/2/3). New too-early tests live: Mary* angle (2 cohorts, ~6 sets, CTR 13-42% but 0 sales yet) and Pattern 4/5/6. No kills. ClickBank still not reconciled. Raw pull: output/ads/_data/2026-06-27-rawpull.json.
- 2026-07-13: /scale-or-kill run (account 1091652249458429, profit line 1.2x). **1 KILL executed:** TheShield `120247314301570135` (Jul-11 static, ~$12, 0 sales, today CTR 1.27% + freq 6.32 = tiny audience saturating, audience/offer problem) → paused, confirmed. **1 SCALE (TS applies):** Pattern 5 `120246534503760135` $22→$28 (3d jumped to 3.32x, still $22). **KEY CHANGE:** ArchMichaelCenturion `120246969841060135` dropped from SCALE to WATCH (14d/28d 3.26x protected, but 3d cooled to 0.86x, don't scale into dip). **New tests converting (WATCH↗, scale-ready on 2nd sale):** TheName `120247314300340135` (14.2x today), Name_NextGen `120247314616580135` (3d 3.16x), MaryNeverStoppedPraying `120247315179480135` (3d 4.68x, first Mother Mary campaign winner), Streak `120247196162630135` (3d 2.83x), TheNameYouAlmostGaveHer `120247196164380135` (2.66x). **WATCH established:** AS4 (28d 1.23x, recent dry), Old Ads 4 (28d 1.95x). Note: paused BeforeYouCouldName booked a late 3.59x (lag confirmed again). ClickBank NOT reconciled (MCP offline). Raw pull: output/ads/_data/2026-07-13-rawpull.json.
- 2026-07-12: /scale-or-kill run (account 1091652249458429, profit line 1.2x). 18 active ad sets, **0 kills**. Two new batches live: Jul-11 statics (day 2) + Jul-12 UGC video campaign & Mother Mary bracelet statics (day 1, TS turned on). **2 SCALE re-recommended (Jul-11 raises not yet applied):** Pattern 5 `120246534503760135` $22→$28 (3d 2.75x/7d 1.51x/14d 1.87x/28d 1.82x, winner every window) and ArchMichaelCenturion `120246969841060135` $6→$8 (7d 1.37x/14d+28d 3.26x). **WATCH↗ scale-ready (thin sample):** TheNameYouAlmostGaveHer `120247196164380135` (2.66x 7/14/28d, 3d quiet) and Streak `120247196162630135` (3d 2.77x/7d 1.71x, survivor of Jul-10 kill). **WATCH protected:** AS4 (28d 1.23x, 3d recovered 1.71x), Old Ads 4 (28d 1.95x despite 14d 0.56x, CTR 21%). **TOO EARLY:** 6 Jul-11 (weak pair TheShield `120247314301570135` 6.7% CTR + GuardHome `120247314611560135` 5.6%, recheck ~$15) + 6 Jul-12 day-1 (Mary statics strong 20-26% CTR; UGC TheShieldYouSend `120247315974880135` weakest at 4.8%). ClickBank NOT reconciled (media-buyer MCP offline all session). Raw pull: output/ads/_data/2026-07-12-rawpull.json.
- 2026-07-11: /scale-or-kill run (account 1091652249458429, profit line 1.2x). 12 active ad sets, **0 kills** (nothing at threshold). **2 SCALE (TS applies budgets):** Pattern 5 `120246534503760135` $22→$28 (fully recovered: 7d 1.34x / 14d 1.86x / 28d 1.83x / today 2.09x, above line every window, refresh-worthy) and ArchMichaelCenturion `120246969841060135` $6→$8 (7d 1.38x / 14d 3.50x / 28d 3.50x, CTR 13.5%, the hidden winner flagged Jul-10). **WATCH:** AS4 (28d 1.22x, 3d recovered 1.34x, known lag), Old Ads 4 (28d 2.01x despite 14d 0.57x, CTR 21%), TheNameYouAlmostGaveHer `120247196164380135` (3.07x held 2 days, 1 sale = too thin to scale), Streak `120247196162630135` (booked sale, 2.12x — sibling of the Jul-10 kill, angle survived). **6 NEW Jul-11 ad sets** (multiply-winners + Mother Mary bracelet: Name_NextGen, TheName, ArchMichael, MotherMaryBlessing, TheShield, ArchMichael_GuardHome) TOO EARLY day 1; watch TheShield (CTR 6.9%) + GuardHome (5.3%) for early-kill by ~$15 if dry. Yesterday's kill `120247196159960135` confirmed still PAUSED. ClickBank NOT reconciled (MCP offline). Raw pull: output/ads/_data/2026-07-11-rawpull.json.
- 2026-07-10: /scale-or-kill run (account 1091652249458429, profit line 1.2x). 11 active ad sets. **1 KILL executed:** TheStreakThatWontBreak `120247196159960135` (~$15.7, 0 sales, CTR 3.06%, audience/offer problem) → paused, confirmed. **1 REDUCE recommended (TS to apply):** Pattern 5 `120246534503760135` $22→$16/day (14d/28d 1.41x above line so NOT killed despite 7d 0.66x; freq 1.77 = variance not fatigue; today bounced 2.59x). **Held as WATCH via 14/28d strength / attribution lag:** Old Ads 4 (28d 2.13x, 21% CTR), AS4 (28d 1.23x, known lagging-sales set), ArchMichaelCenturion (14d 1.36x/28d 3.83x proven winner, next SCALE candidate if CB confirms), BeforeYouCouldName (hovering 0.99-1.14x), TheNameYouAlmostGaveHer `120247196164380135` (early 4.02x/17.7% CTR, 1 sale = too thin to scale). Jul-8 spinoffs (StBenedict x2, Streak dup, TheName dup) TOO EARLY, healthy CTR, recheck ~$20/day 3-4. ClickBank NOT reconciled (media-buyer/karmacc MCP offline). Raw pull: output/ads/_data/2026-07-10-rawpull.json.
- 2026-06-29: /scale-or-kill recheck. Only 4 active ad sets now (all T1_MF_35-65+, 1 ad each). AS4 "The Pattern Ends With You" (120245116749090135) = SCALE: 1.57x/1.36x/1.47x on 7/14/30d, 11 sales, freq 2.0, $14/day. Old Ads 4 "New Rosary-4" (120245963291750135) WATCH: 4.27x 14/30d but last 3d 0 Meta sales (likely lag), CTR 28.6%, $7/day. Old Ads 2 "New Rosary-2" (120245963291600135) WATCH: 2.28x 14/30d, kept via override rule, but 0 sales last 7d on $36 — flag to kill if still dry by Jul 1-2 (offer/page problem, CTR fine at 22%). Pattern5 v5 (120246534503760135) TOO EARLY: ~4d, ~$24, 3.16x, recheck Jul 1. No kills. ClickBank not reconciled (karmacc MCP offline). Raw pull: output/ads/_data/2026-06-29-rawpull.json.
- 2026-07-05: /scale-or-kill, FIRST run with execution-on-approval. EXECUTED (user approved): SCALE Pattern 5 (120246534503760135) 2.42x/7d, 2.27x/14d, 8 sales -> budget set $24 to $30/day; KILL Old Ads 2 (120245963291600135) below line 7d 0.88x AND 14d 0.65x (audience/offer, CTR fine ~20%) -> PAUSED. NOTE: ads_update_entity FORCE-PAUSES on any edit, so Pattern 5 was auto-paused by the budget change and needs TS to re-activate (learning will reset). REDUCE AS4 (120245116749090135, $14) HELD pending TS decision (protected: 14d 1.37x/6 sales, 30d ~1.49x, but 7d crashed to 0.72x) - either apply $14->$10 (will also pause it) or TS sets manually. WATCH (protected, not kills): Old Ads 4 (120245963291750135) 0 sales 7d but 14d 1.60x/30d 3.20x -> hold $9; ArchMichaelCenturion rosary (120246969841060135) 7.30x/2 sales/$20.50 -> scale $5->$8 on 3rd sale; BeforeYouCouldName image (120247029103140135) 2.38x/1 sale -> watch 2nd sale. TOO EARLY: copy tests SomethingToHold/StrongAndTired/EveryoneButThis 0 sales $8-10 high CTR 17-27% -> kill ~$15 if dry; new active set 120247190528750135 zero delivery (poss. missing location_types). Draft Archangel ad sets likely lack location_types too -> may fail publish. ClickBank not reconciled (offline). Raw: output/ads/_data/2026-07-05-rawpull.json.
- 2026-07-09: /scale-or-kill. TS turned ON the Jul-8 Rosary + Bracelet spinoff campaigns (all 6 spinoff ad sets now live, TOO EARLY ~$8-11 each). EXECUTED (TS applied manually in Ads Manager, in-place, no learning reset): REDUCE Pattern 5 (120246534503760135) $30->$22 (protected 14d/28d 1.57x but 7d 0.68x bleed, freq 1.74); REDUCE AS4 (120245116749090135) $10->$7 — NOT killed: booked a 7.04x sale TODAY after a week of "0 sales", proving attribution UNDER-COUNT/lag not death; still fatigued (freq 1.89), under line 14d 0.81/28d 1.10; REDUCE BeforeYouCouldName (120247029103140135) $6->$5 (below 1.2 all windows, 3d 0.66; kill in 2d if still dry+CB confirms none). HOLD (proven, recent dip, bumped recently): Old Ads 4 (120245963291750135) $11 (28d 2.27x but 14d 1.06/3d dry -> reduce to $8 if dry persists); ArchMichaelCenturion (120246969841060135) $6 (28d 4.20x/14d 1.35x, 3d cooled). WATCH: PatternEndsWithYou (120247190528750135) ~$13.5/0 sales -> kill ~$15 if dry. TOO EARLY spinoffs: Bracelet TheNameYouAlmostGaveHer (120247196164380135) PROMISING 7.08x on $7; Rosary TheStreakThatWontBreak (120247196159960135) weak CTR 2.3% (early-kill watch); other 4 recheck Jul 11. KEY LESSON: AS4's today-sale confirms the ClickMagick->ClickBank attribution gap (clicks/cmc_vid track but sales post late or never); trust ClickBank actuals over Meta/ClickMagick for kill calls. Funnel check: both bracelet+rosary have ClickMagick cmc.js installed + vtid=[cmc_vid] on checkout (good), but utm_source is hardcoded 'organic' and both share hid 1214314307 (reporting hygiene). ClickBank not reconciled (MCP offline). (07-07 run was recommend-only, not executed.) See [[clickmagick-clickbank-attribution-gap]].
- 2026-07-06: /scale-or-kill (execution-on-approval, kills only; TS applying budgets manually). EXECUTED KILL x3 (user approved): zero-Meta-sale copy tests, ~$15 spent since Jul 1 at $5/day, past the $15/3-day window -> SomethingToHold (120247056251690135), StrongAndTired (120247056251680135), EveryoneButThis (120247056223740135) all PAUSED. High CTR (26/28/18%) so the HOOKS work = audience/offer/landing-page problem, NOT creative (these were the copy tests flagged "kill ~$15 if dry" on Jul 5). RECOMMENDED budgets for TS to apply MANUALLY (my Meta tool force-pauses on any budget edit, so TS does these in Ads Manager to avoid a learning reset): SCALE Old Ads 4 (120245963291750135) above 1.2 every window (2.93x/28d, 1.31x/14d, 1.26x/7d, 2.99x/3d) -> $9->$11; SCALE ArchMichaelCenturion (120246969841060135) 7.47x but tiny sample ($28) -> $5->$6, don't multiply yet; SCALE BeforeYouCouldName (120247029103140135) 1.82x/2.75x on $18 -> $5->$6; REDUCE AS4 (120245116749090135) protected by 14d/28d 1.22x/1.21x but 7d crashed 0.72x and last 3d $40.74/0 sales, freq 1.95 -> $14->$10 (kill next run if still dry). WATCH Pattern 5 (120246534503760135) $30/day (bumped Jul 5, no daily re-bump): 14d 1.83x / 7d 1.70x / today 2.65x but 3d sagged to 0.39x -> hold, reduce to $24 if another sub-1.2 day. NOTE: the 12 new spinoff ads (Rosary_SpinoffAngles + Bracelet_SpinoffAngles, campaigns paused, launch Jul 8) sit dormant and were not judged. ClickBank NOT reconciled (MCP offline) so kills are Meta-attributed only. Raw pull: in-context this run.
- 2026-07-04: /scale-playbook for Pattern 5 (120246534503760135, bracelet, ad v5 120246534503730135). Scale-ready (2.77x 7d / 4.06x 30d, 8 sales, freq 1.63) BUT ROAS decaying with budget (4.75->4.06->2.77) = audience saturating, so horizontal > vertical. Vertical ladder $24 -> $30 -> $37 -> $45 (+25% every 2-3d, gate on 7d >=1.8x not just 1.2x, hold if CPM spikes/freq>2.5). Horizontal (seed LAL from ATC/page-viewers, pixel thin at 8 sales): LAL1% $12, Broad/Advantage+ $15 (parallel), LAL2-3% $12, LAL4-10% $14, interest stack (Catholic/Rosary/StBenedict/Guadalupe) $10, Reels-only $10; each must hold >=1.8x 3d before next. Protect: refresh bench already deep (Archangel Centurion + 5 images + 6 copy tests). STRUCTURAL: once 1-2 horizontals prove, roll Pattern5 + winners into a CBO to pool purchases and escape learning-limited. Reconcile ClickBank before aggressive rungs.
- 2026-07-04: /scale-or-kill. SCALE: Pattern 5 (120246534503760135) 2.77x/7d (decaying from 4x as it scales), 8 sales -> raise $24 to $30 (watch decay). WATCH (protected, not kills): AS4 (120245116749090135) delivery FIXED by reduce to $14 (spending again), isolated 14d=1.43x/6 sales, 30d=1.49x -> hold $14 hands-off; Old Ads 4 (120245963291750135) 0 sales 7d but isolated 14d=1.63x/30d=3.20x -> hold $9; ArchMichaelCenturion rosary (120246969841060135) 2 sales/$16/9.24x, scale if 3rd sale by ~$30. KILL x3: Old Ads 2 (120245963291600135, still live) 7d 0.87x + 14d 0.41x; ArchMichaelRadiant rosary (120246969841050135) $14.27/0 sales; ArchMichaelDesert rosary (120246969841000135) $15.52/0 sales - both audience/offer. User had killed ArchMichaelDesert bracelet already. KEY STRATEGIC FLAG: ~15 of 20 ad sets show high CTR (8-34%) + 0 sales. Root cause likely (a) $5/day test budget too thin for ~$20 CPP (can't afford 1 sale) AND/OR (b) pixel under-reporting (CLAUDE.md logs prior high-CTR/zero-purchase incident). Winners DO show sales so not total pixel failure. RECOMMEND: reconcile ClickBank before killing borderline sets; consolidate into fewer better-funded Pattern ad sets. ClickBank still not reconciled. Raw: output/ads/_data/2026-07-04-rawpull.json.
- 2026-07-03: /scale-or-kill. SCALE: Pattern 5 (120246534503760135) 3.09x/7d, 4.06x/30d, 7 sales +1 today -> raise $19 to $24. REDUCE (delivery): AS4 (120245116749090135) still learning-limited ($0.32 today), 7d collapsed to 0.71x BUT isolated 14d=1.45x/6 sales, 30d=1.49x/12 sales so protected -> drop $18 to $14, leave alone. WATCH: Old Ads 4 (120245963291750135) 0 sales last 7d but isolated 14d=1.68x/30d=3.20x protected -> hold $9. ArchMichaelCenturion rosary (120246969841060135) WATCH 2 sales/$14/13.8x -> scale to $8-10 if 1-2 more sales by ~$25. KILL x2: Old Ads 2 (120245963291600135) still below line 7d 0.86x + 14d 0.41x, audience/offer (reaffirm, still running); ArchMichaelDesert bracelet (120246967901430135) $13.91/0 sales at ~$15 no-sale threshold, CTR 15.5% = audience/offer. TOO EARLY: BeforeYouCouldName image (120247029103140135) 1st sale today 14x promising; 6 copy tests day1 (rosary SomethingToHold/StrongAndTired CTR ~30%; bracelet UnderYourSleeve CTR 0.91% early-kill-watch). ClickBank not reconciled. Raw: output/ads/_data/2026-07-03-rawpull.json.
- 2026-07-02: /scale-or-kill. SCALE: Pattern 5 (120246534503760135) 4.06x/4.32x, 7 sales -> raise $19 to $24. REDUCE (delivery fix): AS4 (120245116749090135) still learning_exit_unsuccessfully, $0.16 spend today; profitable 1.48x/1.49x/12 sales so NOT a kill -> drop $18 to $14 to re-stabilize, then leave alone. WATCH: Old Ads 4 (120245963291750135) protected, isolated 14d=2.61x/30d=3.20x, 7d soft 1.12x, hold $9. KILL: Old Ads 2 New Page (120245963291600135, ad 120245963291740135) -> isolated 14d dropped to 0.41x AND 7d=0 sales/$38; 30d 1.84x is stale (all sales >14d old); CTR fine 18% = audience/offer problem not creative. Hit the kill trigger set Jun30/Jul1. TOO EARLY: ArchMichaelCenturion rosary (120246969841060135) 2 sales/$8/26.7x promising (recheck ~$25); other archangels 0 sales on $6-8 (watch Desert-bracelet 120246967901430135 for early-kill ~$15); 5 Pattern image sets + 6 copy-test sets all day-1. ClickBank not reconciled. Raw: output/ads/_data/2026-07-02-rawpull.json.
- 2026-07-01: /scale-or-kill. SCALE x3: Pattern 5 (120246534503760135) 4.75x/5.81x, 5 sales -> raise $15 to $19; AS4 (120245116749090135) 1.31x/1.50x, 12 sales -> ladder $18 to $22 BUT flagged abnormal $0.66 spend today (check delivery first); Old Ads 4 (120245963291750135) 1.23x/3.59x, 5 sales -> nudge $7 to $9. WATCH: Old Ads 2 (120245963291600135) still protected, isolated 14d=2.11x/30d=1.97x/4 sales, but dry ~$45 since ~Jun22; recheck Jul 3, kill when 14d<1.2 or dry>$60. TOO EARLY: 6 Archangel video sets now delivering -> ArchMichaelCenturion rosary (120246969841060135) standout with 2 sales on $2.32 / CTR 14.6% today (watch daily); ArchMichaelDesert rosary soft CTR 2.86%. Also launched the 5 new Pattern refresh image sets (07-11: WhatSheCarried 120247029103110135, FirstToSayEnough ...130, BeforeYouCouldName ...140, ForTheOnesAfter ...040, TwoWordsAtTheSink ...080), $5/day, no spend yet, recheck Jul 4. Pattern angle compounding hard across Pattern5 + AS4 + Archangel videos + 5 new images. ClickBank not reconciled. Raw: output/ads/_data/2026-07-01-rawpull.json.
- 2026-06-30: /scale-or-kill. SCALE x3: Pattern 5 (120246534503760135) breakout 6.6x 7/14/30d, 4-5 sales, freq 1.3 -> raise $12 to $15; AS4 (120245116749090135) 1.67/1.58/1.57x, 12 sales -> ladder $14 to $18; Old Ads 4 (120245963291750135) 1.30/3.89/3.89x, 5 sales, CTR 24% -> nudge $7 to $9. Old Ads 2 New Page (120245963291600135): CORRECTED after double-check -> NOT a kill. Bulk pull glitch had shown 14d=0 sales; isolated pull confirms 14d=30d=2.09x/4 sales (ad set only started Jun 16, ~14d old, so 14d/30d are the same window). All 4 sales in its first week (Jun 16-22); last 7d dry (0 sales/$37.53) but no fatigue (freq 1.4, CTR 18%). Verdict WATCH at $5/day, recheck Jul 3; kill only if dry spend passes ~$55-60 with still no sales + ClickBank confirms none. Lesson: verify a kill on an isolated per-adset pull; the bulk multi-adset pull can return "Not available" for a window that actually has sales. TOO EARLY: 6 ArchMichael video ad sets launched today at $5/day (Centurion/Radiant/Desert x2 each), recheck Jul 3; flagged possible accidental duplicate pairs. Pattern angle now compounding across AS4 + Pattern 5 + Archangel videos. ClickBank not reconciled (offline). Raw: output/ads/_data/2026-06-30-rawpull.json.
- 2026-06-29: Produced 6 Archangel Michael talking-head videos for the PatternEndsWithYou angle (3 faces + 3 vestments x Rosary + Bracelet). Michael chosen as the winning angel from the Jun-19 Witness batch (TheWitnessGuard = only ad with a sale; GuardWorn = highest CTR 19.55%). Files in output/ads/videos/Michael_Pattern_*.mp4 (+srt); avatars _avatar_michael_v1/2/3. Voice: HeyGen William Prescott Broadcaster (deep authoritative), 4:5, ~46-49s. Scripts: output/ads/2026-06-29-archangel-PatternEndsWithYou-scripts.md. To launch into AS4 / bracelet Pattern ad set (TS does manually).
- 2026-06-29: /scale-playbook started for AS4 "The Pattern Ends With You" (120245116749090135). Entered active scaling at $14/day. Vertical ladder $14 -> $18 -> $22 -> $27 -> $33/day (+~25% every 2-3d, hold if ROAS dips below 1.2 or freq > 3). Horizontal: LAL1% (seed page viewers/ATC, purchase pixel thin at 11 sales), then LAL2-3%, LAL4-10%, Broad/Advantage+, interest stack (Catholic/Rosary/Prayer), Reels-only — one at a time, each must hold >=1.2x for 3d before next. Refresh bench = Pattern5 (v5 same angle, 3.16x). Scaling deliberately due to thin margin (1.47x vs 1.2 break-even).
- 2026-07-20: Produced 5 relaunch ads (Phase 3 /generate-ads) for Sanctoria bracelet on new domain sanctoriastore.com/bracelet/ + new ad account. Angles: PatternEndsWithYou, InheritedByDaughters, ArchMichaelCenturion, MaryNeverStoppedPraying, QuietSignsChecklist (8.75x checklist mechanism rebuilt compliant, third-person framing). Spec: output/ads/2026-07-20-sanctoria-relaunch-5-ads.md.

- 2026-07-30: /scale-or-kill + /generate-ads run. Live winners: AQuietDevotion (120255189519530051) 2.98x / 2 sales, Chiaroscuro (120255292457450051) 2.74x / 1 sale ($50.68 higher-tier). Recently paused (cooldown to ~2026-09-27): EveryDetailHasMeaning, CarryYourFaith, Minimalist (kill-pending), BoldEditorial, PassItDown, HandcraftedWithDevotion, AGiftOfFaith, PrayerYouWear, WhyIWearItDaily; SacredHeritage took 1 sale (2.76x) before pausing. Built /bracelet-v2/ (rebranded exact replica of the DGG original page) + /go/ 50/50 rotator, deployed live 2026-07-30 for a landing-page split test vs the current /bracelet/ advertorial (same pixel, ClickMagick, and order-2/cbfid checkout). Generated a new HERITAGE/MEANING cold batch (5 ads): TheManBehindTheMedal, WhatTheLettersMean, WhyTheMonksNeverTookItOff, NotTheDrawerMedal, WhereThisMedalHasBeen. Spec: output/ads/2026-07-30-heritage-meaning-batch.md. All point at /go/.

## Cloning a proven page: what a static HTML audit will NOT catch (2026-09-03)

Cloning `divinegracegift.com/new-rosary/` for `/rosary-necklace/` dragged in contamination at three
depths. The first two are visible to a grep of the HTML. The third is not, and it is the dangerous one.

1. **Visible in HTML** (caught immediately): `template=Divine2&cbfid=62440` on every checkout link,
   which would have routed Sanctoria buyers into the banned domain's upsell flow. A Judge.me block
   carrying the Shopify domain and PUBLIC_TOKEN. Fabricated stars, "2,000+ Blessed Families",
   "23 Reservations Remaining", "94% Reserved".

2. **Visible but easy to miss**: UGC review photos identified only by `alt="Customer..."`, and a
   testimonial in a `<blockquote>`. A regex written to kill these also clobbered the legitimate bonus
   PDF thumbnails; those had to be restored by matching alt text.

3. **NOT visible in the HTML at all.** Two separate items, both injected by JavaScript at runtime:
   - A date-seeded fake scarcity function computing `88 + (seed % 9)` and writing `"<pct>% Reserved"`
     into `#batch-reserve-pct`, silently OVERWRITING the honest "Now Reserving" label after load.
   - A 9.5KB `REVIEWS` array of **28 fabricated named reviewers** with "✓ Verified Buyer" badges and
     a pagination renderer. The reviews *section* had been stripped from the HTML, so the code was
     dead and nothing rendered, but it sat in the deployed source one `<div id="reviews-grid">` away
     from going live, and was readable by anyone viewing source.

**Rule: after cloning any page, audit the rendered DOM, not the source.** A grep for `4.9`,
`Verified`, `% Reserved` or `alt="Customer` passed clean on this file while both items above were
still present. What caught them was reading the `<script>` blocks and checking `document.body.innerText`
in a browser. Specifically:
  - Extract every `<script>` block and read it. Look for `textContent =` / `innerHTML =` writes.
  - Check whether the DOM ids the JS targets still exist. If they do not, the code is dead: delete it,
    do not leave it deployed.
  - Test `/(Verified Buyer|% Reserved|\d\.\d stars)/.test(document.body.innerText)` in the live page.
  - Diff the orphaned CSS too. 28 rules for `.review-*` / `.hero-rating` / `.breakdown-*` survived the
    HTML strip; removing the dead JS plus that CSS cut the file 46.5KB -> 33.9KB.

Same fake-percentage JS is also present in `site/guard/index.html` (hardcoded "92% Reserved") and
`site/bracelet-v2/index.html` ("94% Reserved"), both live and both pre-existing. Left alone pending
TS's decision; flagged, not changed.
