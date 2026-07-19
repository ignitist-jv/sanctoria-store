# Sanctoria Store

## Product
- **Offer:** The St Benedict Marian Bracelet (blessed devotional bracelet)
- **Site:** sanctoriastore.com (successor domain; the previous bracelet domain is banned on Facebook)
- **Brand:** Sanctoria, subtitle "Blessed Devotionals"
- **ClickBank ID:** Karmacc (checkout: karmacc.pay.clickbank.net, items bracelet-1 / bracelet-2 / bracelet-3)
- **Pricing:** Single $37 (was $42) | Family 2-pack $47 (was $84) | Household 3-pack $57 (was $126). Free US shipping, 30-day full refund including shipping.
- **Traffic:** Facebook Ads cold, NEW ads account (the previous account/domain pairing is retired)
- **Funnel:** narrow single-column advertorial sales page in `site/index.html` with tiered pricing accordion, plus privacy.html, terms.html, contact.html
- **Support email:** support@sanctoriastore.com

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

## Launch checklist state
- [x] Sales page ported (verbatim proven copy, real product photos, wired ClickBank links)
- [x] Privacy / Terms / Contact pages
- [ ] Register sanctoriastore.com + Cloudflare DNS (user action)
- [ ] Deploy site/ to LiquidWeb
- [ ] Update ClickBank pitch + thank-you URLs to new domain
- [ ] Fresh ClickMagick tracking ID (current links carry old vtid=cmc1018254479)
- [ ] New Meta pixel on new ad account
- [ ] Campaign built PAUSED for user to launch

## Project Learnings
`LEARNINGS.md` and `CREATIVE_HISTORY.md` are carried over from the Divine Grace Gift project and remain the source of truth for winning/dead angles, customer language, and creative history. Read LEARNINGS.md before any ad or copy work. Update it here going forward; the copy in the old project folder is frozen history.

## Media Buyer Account Mapping
When pulling performance data via the media-buyer MCP for this project:
- **Facebook Ads:** the NEW account for Sanctoria (confirm account number with TS before first pull; do NOT assume the old Account 1 / 1091652249458429 mapping)
- **ClickBank nickname:** `karmacc`

## Writing Style: Banned Punctuation (Global Rule)
NEVER use em-dashes or en-dashes in any output. Hyphens only for compound words. Replace with period, comma, semicolon, colon, or rephrase. Applies to all deliverables including this repo's files, commit messages, and chat.

## Meta Ads Naming Convention (MANDATORY)
```
CAMPAIGN:  [AngleName]_[YYYY-MM-DD]
AD SET:    [CountryTier]_[Gender]_[AgeRange]_[AngleName]
AD:        [NN]_[CreativeName]
```
AngleName PascalCase matching LEARNINGS.md; T1 = US/UK/CA/AU/NZ; present every ad concept with a naming table. No spaces, no em/en dashes.

## Ads Rules (inherited, non-negotiable)
Create campaigns PAUSED with ad set + ads active underneath ($5/day default, start_time = creation + 2 days 03:00 SGT). NEVER publish, activate, or un-pause a campaign; that is always TS's action. Mandatory url_tags on every ad:
```
utm_source={{site_source_name}}&utm_medium={{placement}}&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&cmc_adid=fb_{{ad.id}}
```
