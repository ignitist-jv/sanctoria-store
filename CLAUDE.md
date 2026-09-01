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
- **Third offer, The Benedict Pair (built 2026-08-31):** a cross-and-medal necklace. Gold-tone double-strand flat snake chain, lobster clasp, TWO pendants on ONE shared ring: a plain Latin cross (~35mm, no Christ figure, it is a cross NOT a crucifix) and a round Saint Benedict medal (~18mm, plain polished gold edge, NO black bezel, medal smaller than the cross). Ships with a printed Saint Benedict prayer card. Angle **HandToHeart**: the hand-to-chest reflex, "when the phone rings at the wrong hour your hand goes straight to your chest, this is what it should find when it gets there." Mechanism: the devotion you do not have to remember because your own body reaches for it first. The necklace beats the bracelet because a wrist is not where a frightened woman puts her hand. Sales page `site/pair/index.html` at /pair/, modelled on /guard/. Pricing Single $37 / Pair $47 / Household $57, bonus ladder 2/3/4 by tier (up to $58). **CHECKOUT LINKS ARE PLACEHOLDERS** (`#CHECKOUT-TIER-1/2/3`) pending ClickBank items and flow id; ClickMagick full tracker is already on the page and all checkout links must end in `&vtid=[cmc_vid]` when wired. Copy doc: `output/copy/2026-08-31-benedict-pair-salespage-copy.md`. Images: 3 real supplier photos (pair-1/2/3) plus 9 generated (pair-hand, pair-worn, pair-macro, pair-collar, pair-everyday, pair-blessing, pair-gift, pair-product, pair-hero1); references in `images-originals/cross-ref/`.
- **Kit buyer sync (built 2026-08-19):** ClickBank INS v7 -> `site/ins/clickbank.php` on sanctoriastore.com -> Kit account "Ignitist Pte Ltd". Decrypts with the CB vendor secret, creates the subscriber, applies tag `sanctoria-buyer` + per-item tags (bracelet-1/2/3/6/3-ds, tag ids 22564421-26). Secrets in `site/ins/config.php` (gitignored, HTTP-403). Log at site/ins/log.txt (403; readable via FTPS). Replaces the old divinegracegift.com INS scripts; the clkmg.com INS URL (ClickMagick sales feed) must stay in ClickBank. Verified end to end with a synthetic encrypted TEST_SALE.

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
Create campaigns PAUSED with ad set + ads active underneath ($5/day default, start_time = creation + 2 days 03:00 SGT). NEVER publish, activate, or un-pause a campaign; that is always TS's action. Mandatory url_tags on every ad:
```
utm_source={{site_source_name}}&utm_medium={{placement}}&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&cmc_adid=fb_{{ad.id}}
```
