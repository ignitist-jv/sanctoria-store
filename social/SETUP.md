# Sanctoria Social: Automation Setup

**Goal:** daily content on the Sanctoria Facebook Page and Instagram, produced and published automatically, with one weekly human review.

**Written:** 2026-10-08
**Status:** nothing built yet. Phase 0 can be done today with no credentials.

## The assets, confirmed

| Asset | ID | State |
|---|---|---|
| Business portfolio | Ignitist Pte Ltd, `845129699547973` | ✓ |
| Facebook Page | Sanctoria Store, `292317240635888` (public profile `61558968825748`) | ✓ 632 followers, silent since 20 July |
| Instagram | `@sanctoria_store` | 44 followers, no bio, not visible to the API |
| Ad account | `462874384767571` | ✓ Page assigned |

**Do not use** the page "Mother Mary's Voice" (`634692279729668`). It carries the Divine Grace Gift logo, `admin@divinegracegift.com` and `divinegracegift.com/rosary`, which is the domain Facebook banned. Keep it away from the new ad account. Strip the dead domain off it when convenient.

---

## PHASE 0 · Today, no credentials needed

Everything here is free, takes under 30 minutes, and none of it depends on the automation.

- [ ] **0.1 Fix the Facebook Page category.** It is set to "Arts and crafts shop". Change it to **Religious goods shop**. Category feeds who Meta shows the page to, so this affects every post after it.
      *Where:* Page settings, Page info, Category.
      *Done when:* the Intro block reads "Page · Religious goods shop".

- [ ] **0.2 Fill the Instagram bio.** It is blank. This is the only copy on the profile that works unattended.
      ```
      Blessed devotionals, hand-blessed in the Benedictine tradition.
      Worn daily. Passed down.
      Free US shipping · 30-day refund
      ↓ Find the one that fits
      ```
      *Link:* `sanctoriastore.com/chat/`, not the homepage. The chat was built to answer "which of these four is mine", which is the question a stranger arrives with.
      *Done when:* the bio and link show on the public profile.

- [ ] **0.3 Post once, by hand.** Breaks the eleven-week silence and gives the page a pulse before any automation starts. Claude drafts, you paste.
      *Done when:* one post is live on the Page.

- [ ] **0.4 Ask real buyers for recommendations.** The Page shows "0 reviews". You have 15 buyers in Kit plus more through ClickBank. Real recommendations are the one form of proof this brand is allowed, and the opposite of the fabricated reviews stripped off four sales pages.
      *Done when:* the request has gone out.

---

## PHASE 1 · Credentials, so Claude can publish

Roughly 30 minutes. This is the only phase that genuinely needs you.

- [ ] **1.1 Create a NEW System User, separate from the ads one.**
      *Why separate:* the existing System User token is read-only by your own standing rule. Keep it that way. This new one publishes and nothing else, so the two never blur.
      *Where:* business.facebook.com, Business settings, Users, System users, Add.
      *Name it:* `sanctoria-social-publisher`.

- [ ] **1.2 Assign the three assets to that System User.** Not one, all three, each explicitly.
      - Page `292317240635888`, full control
      - Instagram `@sanctoria_store`
      - Ad account `462874384767571`

- [ ] **1.3 Generate the token with exactly these scopes.**

      | Scope | What it buys |
      |---|---|
      | `pages_manage_posts` | Publish to the Page |
      | `pages_read_engagement` | Read posts and comments |
      | `pages_manage_engagement` | Reply to comments |
      | `pages_show_list` | Resolve the Page to its Instagram account |
      | `instagram_basic` | See the Instagram account |
      | `instagram_content_publish` | Publish to Instagram |
      | `instagram_manage_comments` | Reply on Instagram |

      System user tokens do not expire. A plain user token dies in 60 days, which is why it is the wrong kind here.

- [ ] **1.4 Put it in `.env`.**
      ```
      FB_SOCIAL_TOKEN=...
      ```
      Gitignored, same as the FTP credentials. Never commit it, never paste it into chat.

- [ ] **1.5 Tell Claude.** Verification is automated from here:
      - every scope present
      - Page token resolves
      - Instagram Business account ID resolves from the Page
      - one test post to the Page, shown to you, then deleted

**The gotcha most likely to bite:** `pages_manage_posts` and `instagram_content_publish` usually require Meta App Review. The exception is a System User from the business that *owns* the assets posting to those same assets, which should cover you since Ignitist owns all three. If Meta demands App Review anyway, that is a few days of waiting, not a dead end. Claude will say so the moment it hits rather than letting you find out later.

---

## PHASE 2 · What Claude builds

No action from you. Listed so you know what exists afterwards.

- [ ] **2.1 `social/publish.py`** Posts to the Page and Instagram, logs every result.
      Facebook is one call. Instagram is two: create a media container, then publish it.

- [ ] **2.2 `social/queue.yaml`** The approved content queue. Date, platform, caption, image, status. The single source of truth for what goes out and when.

- [ ] **2.3 Image pipeline.** Images generated here, written as **JPEG** (Instagram rejects PNG), uploaded to `sanctoriastore.com/social/` through the existing FTPS deploy, then referenced by public URL, which is what Instagram's API requires.

- [ ] **2.4 Two scheduled tasks.**
      - Weekly: draft next week into the queue for your review
      - Daily: publish whatever the queue has approved for today

- [ ] **2.5 `social/CALENDAR.md`** The posting rhythm and the liturgical dates worth planning around.

---

## PHASE 3 · First live run

- [ ] **3.1 Claude drafts week one.** Seven posts, captions, images, in the queue.
- [ ] **3.2 You review once.** One sitting. Approve, edit, or cut.
- [ ] **3.3 Claude publishes day one and shows you the live post.**
- [ ] **3.4 Watch for a week**, then let the daily task run unattended.

---

## PHASE 4 · Engagement, and the line Claude will not cross

Posting is the easy half. Engagement is where a devotional page actually lives.

- [ ] **4.1 Automated comment triage.** Claude reads new comments daily and sorts them: needs a human, a simple thank you, or nothing. You see a short list instead of a notifications tab.

- [ ] **4.2 Drafted replies, sent by you.** Claude writes them. You press send.

**Why not fully automatic.** On a page about prayer, people write that their daughter has stopped speaking to them, or that their husband has surgery on Tuesday. A machine answering a stranger's grief at scale is the one thing that would genuinely damage this brand. Claude drafts and flags; a person means it.

---

## The approval model

**You approve the queue, not each post.**

Once a week you read seven posts in one sitting. From then on Claude publishes on schedule without asking. Autonomous day to day, human-reviewed before anything is public. Anything off-schedule gets asked about.

Claude will not publish unreviewed content to a public page in your brand's name, and that limit stays whatever the token allows.

---

## The weekly rhythm

| Day | Post | Why |
|---|---|---|
| Mon | A short prayer for the week | From the bank of 18 already written for this avatar |
| Tue | Saint or feast of the day | Dated, searchable, sells nothing |
| Wed | One line of Scripture, Douay-Rheims | Catholic translation, consistent with the Prayer Song decision |
| Thu | **"Who are you praying for this week? First names only."** | The engagement engine |
| Fri | A devotion in use, quiet product presence | Not a sales post |
| Sat | Our Lady | The strongest thread in this avatar |
| Sun | Mass, rest, the week ahead | Highest organic reach day for this audience |

**Thursday is the one that matters.** Asking Catholic women to name who they are praying for is the highest-engagement format in this niche, it is honest, it is the premise the whole brand rests on, and the replies become real voice-of-customer language for `LEARNINGS.md`. One post a week doing that will outperform the other six combined.

**Content you already own:** 18 original prayers sitting in the Kit buyer sequence that 15 people will ever see, `LEARNINGS.md` full of her real language, four products, and the liturgical calendar. That is a year of posts before anyone writes a new word.

**Angle policy applies throughout.** Peace, blessing, grace, protection. None of the banned vocabulary. No fabricated proof. No em-dashes.

---

## Facebook first, Instagram second

Catholic women 45 and over live on Facebook. Instagram skews a decade younger and is a visual-discovery platform rather than a devotional-community one. You have 632 of the right people on the Page and 44 on Instagram. Weight the effort accordingly and let Instagram take the same content cross-posted, which costs almost nothing once the two are linked.

---

## Known limits

- Instagram publishing: 50 posts per rolling 24 hours. You will never approach it.
- Instagram images: public HTTPS URL, JPEG, between 4:5 and 1.91:1.
- Instagram cannot publish Stories through the API. Feed posts and Reels only.
- The Graph API version moves; use the current one rather than pinning an old one.
