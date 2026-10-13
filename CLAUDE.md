# Sanctoria Store

## Product
- **Offer:** The St Benedict Marian Bracelet (blessed devotional bracelet)
- **Site:** sanctoriastore.com (successor domain; the previous bracelet domain is banned on Facebook)
- **Brand:** Sanctoria, subtitle "Blessed Devotionals"
- **ClickBank ID:** Karmacc (checkout: karmacc.pay.clickbank.net, items bracelet-1 / bracelet-2 / bracelet-3)
- **Pricing:** Single $37 (was $42) | Family 2-pack $47 (was $84) | Household 3-pack $57 (was $126). Free US shipping, 30-day full refund including shipping.
- **Traffic:** Facebook Ads cold, NEW ads account (the previous account/domain pairing is retired)
- **Funnel:** sales page moved to `site/bracelet/index.html` (2026-07-20): narrow single-column advertorial page with tiered pricing accordion; ALL ads and the ClickBank pitch URL point to /bracelet/. Root `site/index.html` is now a calm brand homepage with presell (indexable, no checkout links, routes to /bracelet/); built for domain credibility during ad review. Plus privacy.html, terms.html, contact.html
- **Post-purchase funnel (built 2026-07-19, ported from DGG, live since 2026-07-20):** upsell `site/special-offer/` (bracelet-6, $97 6-pack) -> downsell `site/last-chance/` (bracelet-3-ds, $47 3-pack since 2026-07-20; $10 under the front-end 3-pack so the step-down is real). Thank-you pages keep the original DGG slugs so ClickBank config only needs a domain swap: `site/members-page/gifts-single-k8n2r7q4/` (bracelet-1), `site/members-page/gifts-family-p3w9j5x8/` (bracelet-2), `site/members-page/gifts-kingdom-v7t2m1b6/` (bracelet-3). Bonus PDFs served from `site/members-page/downloads/` (user also keeps copies in AWS), sources in `bonuses/`, build script `scripts/build_bonus_pdfs.py` (venv at scripts/.venv). All pages noindex. ClickBank must map each item's thank-you URL to its tier folder and chain the upsell flow.
- **Support email:** support@sanctoriastore.com
- **Second offer, The Benedict Triptych (built 2026-08-29):** a three-medal Saint Benedict bracelet, ungendered protection angle (WornNotStored: the blessed medal in the drawer; protection you do not have to remember). Sales page `site/guard/index.html` at /guard/. ClickBank items medal-1 $37 / medal-2 $47 / medal-3 $57 on template=order-3 with upsell flow cbfid=63893; upsell `site/triptych-offer/` (medal-6, $97 six-pack) -> downsell `site/triptych-last-chance/` (medal-3-ds, $47 three-pack, $10 under the front-end 3-pack). ClickMagick: full tracker on the /guard/ lander, bare cmc.js on the two mid-flow pages, none on thank-you pages; all checkout links use vtid=[cmc_vid] (verified rewriting live). Thank-you pages: `site/members-page/triptych-single-79943f44/` (medal-1, 2 gifts), `triptych-pair-60ef18d9/` (medal-2, 3 gifts), `triptych-household-4a69bb17/` (medal-3, 4 gifts); bonus ladder escalates by tier, matching bracelet-v2. Product images guard-1..guard-band are AI-generated pending real photography; construction reference: three flat medals joined as ONE connected gold plate by tiny narrow tabs, no beads between medals, no black bezels.
- **Triptych reorder page (built 2026-09-01):** `site/more-triptychs/` at /more-triptychs/, the Triptych equivalent of /more-blessings/ (which sells the bracelet). All three triptych thank-you pages now link here instead of /more-blessings/, which was a cross-product leak sending Triptych buyers to a bracelet page. Two tiers only: medal-1 $37 and **medal-3-ds $47 for three** (the downsell item, verified to work standalone outside the upsell flow). The 2-pack is deliberately omitted because medal-2 is also $47, which would be strictly dominated by three-for-$47. Full ClickMagick tracker (it is a lander), noindex, no cbfid so reorders do not re-enter the upsell chain.
- **Third offer, The Benedict Double Protection Necklace (built 2026-08-31, renamed from "The Benedict Pair" 2026-09-05):** a cross-and-medal necklace. Gold-tone DOUBLE-STRAND FINE ROUND SNAKE CHAIN (about 1.2mm, delicate, NOT a flat band and NOT a mesh rope). Both strands terminate at the FRONT in exactly TWO slim tapered end caps joined by ONE small lobster clasp and small 4mm jump rings; there is NO large O-ring. The two pendants hang from adjacent jump rings at that front junction: a plain Latin cross (~35mm, no Christ figure, it is a cross NOT a crucifix) and a round Saint Benedict medal (~18mm, plain polished gold edge, NO black bezel, medal smaller than the cross). Ships with a printed Saint Benedict prayer card. Angle **HandToHeart**: the hand-to-chest reflex, "when the phone rings at the wrong hour your hand goes straight to your chest, this is what it should find when it gets there." Mechanism: the devotion you do not have to remember because your own body reaches for it first. The necklace beats the bracelet because a wrist is not where a frightened woman puts her hand. Sales page `site/necklace/index.html` at /necklace/ (renamed from /pair/ on 2026-09-01; a 301 in site/.htaccess redirects the old URL), modelled on /guard/. Pricing Single $47 / Pair $57 / Household $67 (raised $10 per tier on 2026-09-10; was-anchors $52 / $104 / $156), bonus ladder 2/3/4 by tier. **Checkout links are LIVE:** karmacc items `necklace-1/2/3` on template=order-4 with upsell flow cbfid=63921 and the vtid token; items approved and every price verified by rendering the live checkout. Copy doc v2 (LIVE): `output/copy/2026-09-01-benedict-pair-salespage-copy-v2.md`; v1 archived at `output/copy/2026-08-31-benedict-pair-salespage-copy.md`. **V2 (2026-09-01) removed all six fabricated testimonials, the fabricated pull quote and the "Customer quotes shared with permission" line, replacing them with an honest proof block that states plainly there are no reviews yet; removed the invented "92% Reserved" batch figure; rewrote every second-person assertion about the reader's faith into third-person/community framing for Meta personal-attributes compliance; moved the hero CTA above the image so it clears a 375px fold (CTA y=425, was 918); gave the multi-pack discount a stated reason (batch blessing economics); and stripped the priced bonus stack down to one companion line per tier.** Upsell `site/necklace-offer/` (six for $97) and downsell `site/necklace-last-chance/` (three for $47) built 2026-09-01 off the triptych templates, with three audit fixes applied: an order-confirmation reassurance line at the top, an accept/decline pair high on the page as well as at the bottom, and dignified decline wording replacing "I do not want this super discounted bracelet". Upsell item `necklace-6` $97 and downsell item `necklace-3-ds` $47 are live; their anchors were raised to $282 and $141 when the single rose to $47. Thank-you pages `site/members-page/pair-single-ea8d9620/` (necklace-1), `pair-duo-260393c3/` (necklace-2), `pair-household-2af24fd0/` (necklace-3). Kit tags mapped in site/ins/config.php on 2026-09-11: necklace-1 23298586, necklace-2 23298590, necklace-3 23298591, necklace-6 23298598, necklace-3-ds 23298599. The three older `sanctoria-pair-*` tags (22965832 to 22965834) are unused and deliberately left in place. **Product images REGENERATED 2026-09-09 from real supplier photographs** (archived at images-originals/necklace-real/, Higgsfield renders at images-originals/necklace-v2/). All 11 page images were replaced because the originals showed a thick woven mesh rope or a wide flat herringbone ribbon with a large O-ring, none of which the product has, and pair-3 had the supplier card reading "Spiritual Jewelry Collection" legible on the live page. See LEARNINGS.md for the corrected geometry and the prompting technique that fixed it (anchor dimensions to in-frame ratios, never millimetres). Older images: 3 real supplier photos (pair-1/2/3) plus 9 generated (pair-hand, pair-worn, pair-macro, pair-collar, pair-everyday, pair-blessing, pair-gift, pair-product, pair-hero1); references in `images-originals/cross-ref/`.
- **Fourth offer, The Saint Benedict Cord Rosary (built 2026-09-03):** a port of the proven DGG `/new-rosary/` page (5.44x ROAS angle) onto Sanctoria at `site/rosary-necklace/` → /rosary-necklace/. Angle **InheritedByDaughters** (heirloom, faith handed down). **PRODUCT CHANGED from the source page:** black matte WOODEN beads on knotted braided black cord (NOT lava stone), silver-tone Saint Benedict medals along the whole length, oval Saint Benedict centerpiece (NOT Our Lady of Guadalupe), pale Our Father beads, black WOOD crucifix with silver corpus + INRI + silver Saint Benedict medal inset. Ships with drawstring pouch + prayer card. **Checkout links are LIVE:** karmacc items `rosary-1` $37 / `rosary-2` $47 / `rosary-3` $57 (repriced from $67/$87 on 2026-09-04), template=order-5 (switched from order-3 on 2026-09-11), upsell flow cbfid=63426, vtid token. Upsell `site/rosary-offer/` (rosary-6, $97 six-pack) -> downsell `site/rosary-last-chance/` (rosary-3-ds, $47 three-pack), built 2026-09-07 off the triptych templates with the reassurance line, top accept/decline pair and dignified decline wording. Thank-you pages `site/members-page/rosary-single-6b19b599/` (rosary-1), `rosary-family-26afa7c1/` (rosary-2), `rosary-household-efac885b/` (rosary-3), gift ladder 2/3/4. Kit tags mapped in site/ins/config.php: rosary-1 23162403, rosary-2 23162404, rosary-3 23162405, rosary-6 23162406, rosary-3-ds 23162407. All item prices verified by rendering the live checkout. Full ClickMagick tracker (it is a lander), 3 real supplier photos rosary-1/2/3. Copy doc: `output/copy/2026-09-03-rosary-necklace-salespage-copy.md`. **Deliberately NOT ported from the source page:** the 4.9 star rating, "2,000+ Blessed Families", "23 Reservations Remaining", "94% Reserved", the Verified Reviews block and the named testimonial (all fabricated); and "Blessed in Rome" / "the abbey's mission" / "the chaplain's blessing", downgraded to the claim Sanctoria actually makes everywhere else, hand-blessed in the Benedictine tradition.
- **Kit buyer sync (built 2026-08-19):** ClickBank INS v7 -> `site/ins/clickbank.php` on sanctoriastore.com -> Kit account "Ignitist Pte Ltd". Decrypts with the CB vendor secret, creates the subscriber, applies tag `sanctoria-buyer` + per-item tags (bracelet-1/2/3/6/3-ds, tag ids 22564421-26). Secrets in `site/ins/config.php` (gitignored, HTTP-403). Log at site/ins/log.txt (403; readable via FTPS). Replaces the old divinegracegift.com INS scripts; the clkmg.com INS URL (ClickMagick sales feed) must stay in ClickBank. Verified end to end with a synthetic encrypted TEST_SALE.

## Fifth offer: Your Prayer Song (started 2026-10-01, soft-published 2026-10-07)
A personalised sung prayer carrying one or two first names, digital, $39 on ClickBank with a 30 day refund. Public at https://sanctoriastore.com/prayer-song/ since 2026-10-07 as a SOFT build: page, form, private song page, admin page (`/prayer-song/admin/`), reviews page and legal pages are live and `noindex`, but there is no ClickBank checkout link and no cron job yet, so nothing can be bought or made on the live site. Deploy only this folder with `python3 deploy/deploy.py --only prayer-song`; `api/config.php` lives only on the server. Everything else is in `prayer-song/`: read `prayer-song/CONNECT.md` (its "LIVE STATE" section first) and `prayer-song/PRODUCT-BIBLE.md`. Built with `/playbook` (shape QUIZ + PERSONAL). The top-of-page film and sample clips are generated illustrations and are labelled as such on the page; never use them in ads as customers.

## History (important)
This offer migrated from the Divine Grace Gift project (bracelet.divinegracegift.com, domain banned on Facebook, cause unknown, assumed content-related). The page copy and offer structure are a faithful port of that proven page. Never mention "Divine Grace Gift" in any customer-facing output for this brand. No visible old-brand imagery (the branded pouch photo was removed from the page).

## Avatar
Catholic women 45+. Faith-driven. Worried about family, adult children drifting from the Church, marriages under strain, grandchildren. Believes in the protective power of prayer, saints, and sacred objects. Motivated by love of family and desire for spiritual protection and peace.

## Ad Angle Policy (relaunch rule)
Reframe fear angles to peace/protection/blessing for ads pointing at this domain. Avoid on ads AND page: bad luck, curse, evil, hex, Jezebel, spiritual attack, spiritual warfare. Use: peace, blessed, blessing, grace, protection, guard your family, faith, sacred, devotion. The proven mechanisms (CRDN-4 bad-luck 8.75x ROAS, CHEAT-7-S4 Jezebel 4.97x ROAS) live in LEARNINGS.md; carry their mechanism, not their banned vocabulary.

## Design System
Match `site/index.html`: cream #F7F3EC, white cards, bronze #9A7B4F accents, gold CTAs #F2C230 (green hover #2E9E4F), Fraunces headlines + Inter body, narrow 520px single-column layout, logo at `site/images/logo.png` (transparent background).

## Dev / Preview
- `.claude/launch.json` name `sanctoria` serves `site/` on port 4173
- The site is static, self-contained HTML/CSS/JS, deployed by uploading `site/` contents to the LiquidWeb server (same server as before, Cloudflare proxy recommended on DNS)
- Deploy: `deploy/deploy.sh` uploads site/ over explicit FTPS using FTP_* credentials in `.env` (gitignored). `--dry-run` previews. Account ship@sanctoriastore.com is chrooted to the docroot, so FTP_REMOTE_DIR=/

## Launch checklist state
- [x] Sales page ported (verbatim proven copy, real product photos, wired ClickBank links)
- [x] Privacy / Terms / Contact pages
- [x] Register sanctoriastore.com + DNS (live, resolves to LiquidWeb 69.16.254.34)
- [x] Deploy site/ to LiquidWeb (2026-07-19, via deploy/deploy.sh, FTPS account ship@sanctoriastore.com rooted at public_html)
- [x] ClickBank wired and test-purchased end to end (2026-07-20): pitch /bracelet/, per-item thank-you URLs, flow 63684 upsell chain, order-2 template
- [x] ClickMagick fixed and verified live (2026-07-20): full cmc tracker (uid 92654, hid 1214314307, project 'Sanctoria Store', vid_info on, utm_source 'organic' default) on the landers /bracelet/ and /more-blessings/; bare cmc.js on /special-offer/ and /last-chance/; all checkout links use vtid=[cmc_vid] tokens which cmc.js rewrites per visitor (verified: lander link got a real cmc id and the upsell links inherited the cookie vid). No CM code on homepage or thank-you pages. Never hardcode a vtid value in links.
- [x] Meta tracking is CAPI-ONLY (since 2026-07-20): browser pixel code was installed then deliberately REMOVED site-wide at TS's direction because events are sent server-side via CAPI to dataset 1162659081276679; do NOT re-add fbq browser code (it would double-fire). Verified zero fbq on all live pages.
- [ ] Campaign built PAUSED for user to launch

## Project Learnings
`LEARNINGS.md` and `CREATIVE_HISTORY.md` are carried over from the Divine Grace Gift project and remain the source of truth for winning/dead angles, customer language, and creative history. Read LEARNINGS.md before any ad or copy work. Update it here going forward; the copy in the old project folder is frozen history.

## Media Buyer Account Mapping
When pulling performance data via the media-buyer MCP for this project:
- **Facebook Ads:** Sanctoria Store account ID 462874384767571 (Ignitist Pte Ltd, USD; confirmed by TS 2026-07-20). Pixel/dataset: "Sanctoria Store" 1162659081276679, installed site-wide. The old Divine Grace Gift account 1091652249458429 is DISABLED; never use it.
- **ClickBank nickname:** `karmacc`. WARNING: the media-buyer `cb_get_sales` summary undercounts badly (reported 4 sales for a window with 22 real orders on 2026-08-22); always use `cb_get_orders` and aggregate SALE rows yourself. Orders carry the ClickMagick visitor id in the `promo` field (cmc...), which is how CM and the Meta CAPI attribute sales; an order with promo nil is invisible to both.

## Writing Style: Banned Punctuation (Global Rule)
NEVER use em-dashes or en-dashes in any output. Hyphens only for compound words. Replace with period, comma, semicolon, colon, or rephrase. Applies to all deliverables including this repo's files, commit messages, and chat.

## Meta Ads Naming Convention (MANDATORY) — updated 2026-08-15: FORMAT CODE added
```
CAMPAIGN:  [AngleName]_[Format]_[YYYY-MM-DD]
AD SET:    [CountryTier]_[Gender]_[AgeRange]_[AngleName]_[Format]_[Variant]
AD:        [NN]_[CreativeName]
```
- **Format** (design/creative type, so winners trace by angle AND format): `IG`=infographic, `VID`=video, `DX`=double-exposure, `PHOTO`=lifestyle photo, `MACRO`=macro, `POSTER`=typographic, `UGC`=ugc, `ADV`=advertorial, `ILLUS`=illustration. Add new codes as new formats appear.
- **Variant** = short design/scene label (e.g. Bento, Dawn, RadialAmber). PascalCase.
- AngleName PascalCase matching LEARNINGS.md; T1 = US/UK/CA/AU/NZ; present every ad concept with a naming table. No spaces, no em/en dashes.
- Example: Campaign `WornInFaith_IG_2026-08-15` / Ad Set `T1_MF_35-65+_WornInFaith_IG_Bento` / Ad `01_Bento`.

## Ads Rules (inherited, non-negotiable)
Create campaigns PAUSED with ad set + ads active underneath ($5/day default, start_time = creation + 2 days 03:00 SGT). NEVER publish, activate, or un-pause a campaign; that is always TS's action.

**LANGUAGE: every ad set targets English only.** In Ads Manager set
Audience > Languages to **English (All)**. This applies to every campaign on
this account without exception; the offers are English-only and the landing
pages have no translations, so an unrestricted ad set buys impressions that
cannot convert.

Checking and setting it:
- Ads Manager is the source of truth. The field is `locales` in the API.
- **CONFIRMED on this account 2026-10-13, from the account activity log:
  `6` = English (US) and `24` = English (UK).** An ad set carrying
  `locales: [6, 24]` reads in the change log as "English (US) or English (UK)".
  This is NOT the same as "English (All)", which is a separate and broader
  option in the Ads Manager UI whose id is still unknown.
- **Do not hardcode any other locale ID from memory.** This MCP exposes no
  targeting-search tool, so the only reliable method is to set the language in
  Ads Manager, then read `targeting.locales` back with `ads_get_ad_entities`
  and reuse the id observed. `ads_account_get_activity_logs` with
  `event_category: targeting` prints the human-readable language name, which is
  how the mapping above was settled.
- State as of 2026-10-13: the three SungForTheHolySouls ad sets carry
  `locales: [6, 24]`, so English (US) or English (UK), not English (All). The
  three live SungByName ad sets carry no `locales` at all and are unrestricted.
- Changing `locales` on a LIVE ad set is a targeting edit and resets the
  learning phase. On an ad set still gathering its first read, that throws the
  data away. Prefer setting it at build time; retrofit a live ad set only when
  TS accepts the reset.

Mandatory url_tags on every ad:
```
utm_source={{site_source_name}}&utm_medium={{placement}}&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&cmc_adid=fb_{{ad.id}}
```
