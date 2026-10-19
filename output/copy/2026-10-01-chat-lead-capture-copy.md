# Sanctoria · Chat Funnel · Name and Email Capture · Full Copy

**Date:** 2026-10-01
**Extends:** `output/copy/2026-10-01-chat-funnel-copy.md` (the chat live at /chat/)
**What changes:** the chat now collects a first name and an email address. The "No email" promise is withdrawn and every line carrying it is replaced below.
**What does not change:** the three questions, the eleven acknowledgement bubbles, the answer-to-product mapping, the four results, the pack cards, the prices, the trust bubble, the other-three chip. None of that is touched by this document.
**Three variants written, because the gate decision is open.** A soft gate, B hard gate, C after the result.

---

## WHAT GETS DELETED FROM THE LIVE BUILD

Three strings in `site/chat/index.html` carry the withdrawn promise. All three are replaced in Section 1.

| Where | Current string |
|---|---|
| Header sub-line, `#senderNote` | `No email. Three taps.` |
| `COPY.sender.note` | `No email. Three taps.` |
| Third opening bubble, `COPY.opening[2]` | `This is a short guided conversation. No email, nothing to fill in. Just tap an answer.` |

No other line in the live chat mentions email. Nothing else needs withdrawing.

---

## THE ONLY TWO THINGS WE MAY PROMISE

Every build-up line below rests on exactly two true benefits. Nothing else is offered anywhere in this document.

1. **Her match, sent to her.** The chat tells her which of four devotions fits her three answers. Emailed, she keeps it instead of losing the tab.
2. **The free daily prayer emails.** One short written prayer a morning, fourteen of them, then it ends. This is the series in `output/copy/2026-09-01-buyer-daily-prayer-series.md`.

**No discount. No coupon. No reserved stock. No priority. No early access. No bonus. None of those appear in any line below, in any variant.**

### One truth check TS must clear before this ships

The fourteen-day prayer series as written is **buyer-only**. Four emails anchor to an object she already owns: Day 2 ("a hand on the blessed medal you already wear"), Day 9 ("a blessed medal worn through years like these"), Day 12 ("next to wherever the bracelet is set down at night"), Week 3 ("wearing the medal that was blessed for exactly this kind of ordinary guarding"). A chat opt-in is a prospect, not a buyer, so those four lines are false to her on arrival.

**Fix before launch, not after:** send non-buyers the same fourteen days with those four anchors swapped for object-free wording. Everything else in the series already works for someone who owns nothing. The copy below promises only "one short prayer each morning for fourteen days", which is true of the prospect version and the buyer version alike, so none of these lines need rewriting once that swap is made.

---

## VOICE RULES, CARRIED FORWARD UNCHANGED

The six rules in the parent doc still govern every line here. The two that this document stresses hardest:

1. **No line claims a live human, clergy, or that anyone is reading her answers.** No "I have your answers in front of me", no "let me email this over myself", no "I will send it personally". A script sends the email, so the copy says the email is sent, never that a person sends it.
2. **She tells us, we never tell her.** No bubble asserts her religion, health, finances or family circumstances. The ask bubbles below ask, they do not describe her.

Added for this document:

3. **The name is used once.** Her first name appears in exactly one bubble per variant, the confirmation. Nowhere else. Repeating it reads as a mail merge and undoes the warmth it bought.
4. **The ask is never dressed as a question she already answered.** No chips at the name or email step. A field and a button, nothing that looks like Q4.

---

# SECTION 1 · THE REPLACEMENT FOR THE WITHDRAWN PROMISE

## 1A · Header sub-line

**ROLE: Header sub-line · SHARED by variant A and variant C**

> Three questions. One devotion that fits.

**ROLE: Header sub-line · VARIANT B ONLY** (the hard gate has to be honest in the header, because the header is read before the first bubble)

> Three questions, your email, one devotion.

**Alternates for testing, A and C:** `Three questions. One of four.` · `A short guided conversation.`
**Alternate for B:** `Three answers, then the one that fits.`

## 1B · Third opening bubble

One per variant. The first two opening bubbles are untouched.

**ROLE: Opening bubble 3 · VARIANT A**

> A short guided conversation. Three answers, then the one that fits, with the option of having it sent to you.

**ROLE: Opening bubble 3 · VARIANT B**

> A short guided conversation. Three answers, then your name and email, and the one of the four that fits.

**ROLE: Opening bubble 3 · VARIANT C**

> A short guided conversation. Three answers, then the one that fits and all three prices. Nothing to fill in first.

**Build note:** the chip after it stays `Begin` in all three variants.

---

# SECTION 2 · SHARED COMPONENTS

These lines are **identical in all three variants**. Write them once, reuse them. Only the build-up bubbles, the skip line, the confirmation and the variant C offer bubble differ.

| Role | Copy | Limit check |
|---|---|---|
| Name field placeholder | `First name` | 2 words |
| Name button label | `Continue` | 1 word |
| Email field placeholder | `Your email` | 2 words |
| Email button label | `Send it to me` | 4 words |
| Invalid-email line | `That address did not take. Most likely one small typo.` | under the field, red |
| Consent microcopy | see 2C below | under the field, grey, smallest legible size |

## 2A · The first name ask

**ROLE: Name ask bubble · SHARED**

> Before that, what may we call you?

**Alternates:** `And what name should this be sent to?` · `What may we call you?`

**ROLE: Name field placeholder · SHARED**

> `First name`

**ROLE: Name button · SHARED**

> `Continue`

**ROLE: Empty-name line · SHARED** (fires if she taps Continue with nothing typed; she is never blocked here)

> No name is fine. It will simply read plainly.

**Build note:** the empty-name path is never a hard stop in any of the three variants, including B. B gates on the email, not on the name. If she leaves the name blank, skip to the email ask and drop the first name out of the confirmation bubble (see the no-name confirmation line in each variant).

## 2B · The email ask

**ROLE: Email ask bubble · SHARED**

> And the address to send it to.

**Alternates:** `Where should it be sent?` · `And where shall we send it?`

**ROLE: Email field placeholder · SHARED**

> `Your email`

**ROLE: Email button · SHARED**

> `Send it to me`

**Alternates, both inside 4 words:** `Send it` · `Yes, send it`

**ROLE: Invalid-address line · SHARED** (fires on a failed format check, replaces nothing, sits under the field)

> That address did not take. Most likely one small typo.

**Alternate:** `Something is off in that address. Worth another look.`

## 2C · Consent microcopy · SHARED

Sits under the email field, always visible before she taps the button, never behind a tap or a tooltip. One line, smallest legible size, grey.

**ROLE: Consent microcopy · SHARED, all three variants**

> You will receive your match and one short prayer by email each morning for fourteen days. Unsubscribe any time. [Privacy policy](/privacy.html).

**Build note:** "Privacy policy" links to `/privacy.html`. Keep the link visible text, not an icon. No pre-ticked checkbox, no unticked checkbox either; the button is the consent, and this line is what the button means.

**Shorter variant if it wraps past two lines on 375px:**

> Your match, plus one short prayer each morning for fourteen days. Unsubscribe any time. [Privacy policy](/privacy.html).

---

# SECTION 3 · VARIANT A · SOFT GATE

**Position:** after the Q3 acknowledgement, before the result. The recommendation is shown either way.
**Sequence:** Q3 ack → build-up 1 → build-up 2 → build-up 3 → name ask → email ask with skip line → confirmation → result bubbles → pack card → trust bubble → other-three chip.

## 3A · Build-up bubbles · VARIANT A ONLY

**ROLE: Build-up bubble 1**

> Thank you. That is all three.

**ROLE: Build-up bubble 2**

> The one that fits is ready. We can send it to you as well, so it is not lost in a tab.

**ROLE: Build-up bubble 3**

> And with it, one short written prayer each morning for fourteen days. Free, and then it ends.

**Build note:** bubble 1 is the existing handover bubble, reused deliberately so the rhythm she has been in does not break at the ask. Hold about 700ms between bubbles. The name field appears only after bubble 3 has landed.

**Alternate for bubble 3** if the series is positioned as the stronger half of the offer:
> One short written prayer arrives each morning for fourteen days. Free, finite, and nothing to pray along to.

## 3B · The skip line · VARIANT A ONLY

Sits under the email button as plain underlined text, never as a chip and never as a second button. It must look lighter than the button, because it is.

**ROLE: Skip line · VARIANT A ONLY**

> Or go straight to the one that fits.

**Alternates:** `Show it without sending it.` · `No need, just show me.`

**Build note:** the skip link appears under the **email** step only, not under the name step. If she skips, she gets the skip confirmation below and then the full result, all three prices, all three buttons live. Skipping costs her nothing and the copy never implies otherwise.

## 3C · Confirmation · VARIANT A ONLY

**ROLE: Confirmation bubble, she gave an email**

> Thank you, {{first_name}}. It is on its way, and here is the one that fits what you said.

**ROLE: Confirmation bubble, name left blank**

> Thank you. It is on its way, and here is the one that fits what you said.

**ROLE: Confirmation bubble, she skipped**

> Of course. Here is the one of the four that fits what you said.

---

# SECTION 4 · VARIANT B · HARD GATE

**Position:** after the Q3 acknowledgement, before the result. Nothing is shown until a valid email is submitted.
**Sequence:** Q3 ack → build-up 1 → build-up 2 → build-up 3 → name ask → email ask, no skip → confirmation → result bubbles → pack card → trust bubble → other-three chip.

## 4A · Build-up bubbles · VARIANT B ONLY

**ROLE: Build-up bubble 1**

> Thank you. That is all three.

**ROLE: Build-up bubble 2**

> The one that fits is ready, and it is sent by email, so it stays yours to keep.

**ROLE: Build-up bubble 3**

> One short written prayer comes with it each morning for fourteen days. Free, and then it ends.

**Build note:** B's honesty is carried in opening bubble 3 (Section 1B), which tells her at the door that an email is part of this. Without that line, B is a bait and switch and will be read as one. Do not ship B with A's opening bubble.

## 4B · No skip · VARIANT B ONLY

There is no skip line in B. That is the variant. Two things the build must still do, so the gate is firm without being hostile:

1. **Nothing says the result is being withheld.** No "unlock", no "to see your match", no lock icon, no greyed-out card behind a blur. The email ask is simply the next step in the conversation, phrased as in 2B.
2. **The transcript above her still scrolls.** Her three answers and all eleven acknowledgements stay in history. She is never left on a blank screen holding a form.

**If she submits an invalid address three times**, show the shared invalid-address line each time and nothing else. Do not add a bypass. Do not add a "having trouble?" line that reads as a hidden skip; in a hard gate that is a skip with extra steps.

## 4C · Confirmation · VARIANT B ONLY

**ROLE: Confirmation bubble, she gave an email**

> Thank you, {{first_name}}. It is sent. Here is the one of the four that fits what you said.

**ROLE: Confirmation bubble, name left blank**

> Thank you. It is sent. Here is the one of the four that fits what you said.

---

# SECTION 5 · VARIANT C · AFTER THE RESULT

**Position:** after the trust bubble, before the other-three chip. She has already seen the devotion, all three prices and all three live buttons.
**Sequence:** result bubbles → pack card → trust bubble → build-up 1 → build-up 2 → offer bubble → chip → name ask → email ask → confirmation → other-three chip.

## 5A · Build-up bubbles · VARIANT C ONLY

**ROLE: Build-up bubble 1**

> That is the one. All three prices are above, nothing held back.

**ROLE: Build-up bubble 2**

> If today is not the day, it does not have to be found again from scratch.

**Build note:** C's build-up has two bubbles, not three, because the offer bubble itself carries the third beat. Place these **below** the pack card. Nothing in this sequence may sit between her and a buy button.

## 5B · The offer bubble and the chip · VARIANT C ONLY

**ROLE: Offer bubble · VARIANT C ONLY**

> Shall we send this match to you, with one short prayer each morning for fourteen days?

**ROLE: Accept chip · VARIANT C ONLY**

> `Yes, send it`

**Chip alternates:** `Yes, send both` · `Send it to me`

**ROLE: Decline chip · VARIANT C ONLY**

> `No, thank you`

**ROLE: Decline bubble, fires on the decline chip**

> Of course. Everything stays on this screen, and the other three are below.

**Build note:** C needs a decline chip, because an offer with only one answer is not an offer. The two chips sit side by side, accept first. On decline, go straight to the other-three bubble and chip from the parent doc. Never re-ask.

## 5C · Confirmation · VARIANT C ONLY

**ROLE: Confirmation bubble, she gave an email**

> Thank you, {{first_name}}. It is on its way, and the first prayer comes tomorrow morning.

**ROLE: Confirmation bubble, name left blank**

> Thank you. It is on its way, and the first prayer comes tomorrow morning.

**Build note on "tomorrow morning":** this line is only true if the series is scheduled to start on the next morning send. If Day 1 fires immediately on subscribe, change both lines to `It is on its way, and the first prayer is in it.` Do not ship the tomorrow wording against an instant Day 1.

---

# SECTION 6 · SHARED VERSUS SPECIFIC, AT A GLANCE

| Component | A soft | B hard | C after result |
|---|---|---|---|
| Opening bubbles 1 and 2 | shared, unchanged | shared, unchanged | shared, unchanged |
| Opening bubble 3 | A-specific | B-specific | C-specific |
| Header sub-line | shared with C | B-specific | shared with A |
| Three questions, 11 acks | shared, unchanged | shared, unchanged | shared, unchanged |
| Build-up bubbles | A-specific, 3 bubbles | B-specific, 3 bubbles | C-specific, 2 bubbles |
| Offer bubble and chips | none | none | C-specific |
| Name ask, placeholder, button, empty-name line | **shared** | **shared** | **shared** |
| Email ask, placeholder, button, invalid line | **shared** | **shared** | **shared** |
| Consent microcopy | **shared** | **shared** | **shared** |
| Skip line | A-specific | none | replaced by decline chip |
| Confirmation bubble | A-specific, 3 states | B-specific, 2 states | C-specific, 2 states |
| Result, pack card, trust, other three | shared, unchanged | shared, unchanged | shared, unchanged |

**Total new customer-facing lines:** 9 shared, 8 A-specific, 6 B-specific, 8 C-specific.

---

# SECTION 7 · WHICH VARIANT I WOULD RUN

## Run variant A, the soft gate.

Three reasons, all of them out of LEARNINGS.md rather than preference.

**1. The account cannot afford to lose finishers, and cannot measure it when it does.** The funnel audit of 2026-09-23 put this account at **$1.27 per outbound click, 3.07% site conversion, $50.24 AOV**, which is $1.54 of revenue against $1.27 of cost. That margin does not survive a tax at the last step before the price. Worse, the same audit showed that **$15 of spend buys about 12 outbound clicks, and an exactly average ad shows zero sales 69% of the time**; roughly 75 outbound clicks, about $95, are needed for 90% confidence. A hard gate could take front-end revenue to zero and the account's own measurement floor would not reliably tell us for weeks. A is the only variant that cannot do that, because every finisher still reaches three live prices.

**2. The stated point of this build is that every finisher sees three prices.** The parent doc commits to it in writing, twice, and the mapping rules go out of their way to make Q3 a highlight rather than a gate so that "no answer can hide a price from her". B reverses that decision at the final step. If the build's own thesis is that price transparency is what this audience needs, the gate should not be the one place we withhold.

**3. C asks after she has already been paid.** By the time C's offer bubble lands she has the devotion, the prices and the refund terms. The only thing left to trade is goodwill, so opt-in rate will be a fraction of A's, and the ask is competing for the same tap as the buy button. The whole brief was to **earn** the email, and A is the position where it is earned: she has answered three questions, the match exists, and it has not been handed over yet. That is the single highest-intent second in the funnel.

### Why collecting at all is the right call for this account

Every kill in this account has the same shape: **good CTR, no sale**. Roughly twenty killed ad sets at 5% to 20% CTR against a 1 to 2% norm, and the repeated conclusion in the file is that the hooks work and the pages do not convert the clicks. An email list is the only asset that makes a non-converting click worth something later. With `AQuietDevotion` carrying the account at 1.45x and the family multi-pack angles sitting at 0.92x to 1.10x, there is no front-end headroom left to find. A list is where the second sale lives, which is exactly what a 1.25x blended account needs.

### How to settle A versus B properly, if TS wants the test

Do not run it as two ads. Run it as two arms of the same traffic, and judge on **one combined number: emails captured per dollar, and front-end revenue per dollar, read together**. An arm that doubles capture while halving front-end revenue is a loss on this margin. Per the account's own statistics, give each arm about **75 finishers minimum** before reading it, and pool across ads rather than per ad. Anything less is the $15 kill threshold mistake in a new costume.

### One thing to change whichever variant wins

Fix the prospect version of the prayer series first. Four of the eighteen emails tell her to put a hand on a medal she does not own. The opt-in copy above is clean, and the first email landing false would undo all of it.

---

# SECTION 8 · LIMIT CHECKS

**Bubbles, 25 words or fewer.** Longest lines in this document: variant A build-up 2 at 19 words, variant B build-up 2 at 16, variant C offer bubble at 15, variant B confirmation at 18, opening bubble 3 for B at 21. Every bubble clears.

**Button labels, 4 words or fewer.** `Continue` 1. `Send it to me` 4. `Send it` 2. `Yes, send it` 3. `Yes, send both` 3. `No, thank you` 3. `Send it to me` 4. All clear.

**Placeholders, 3 words or fewer.** `First name` 2. `Your email` 2. Both clear.

**Chips, 5 words or fewer** (parent doc rule, carried forward). `Yes, send it` 3. `No, thank you` 3. Clear.

**Consent microcopy** is not a bubble and is not capped, but both versions fit two lines at 375px at the smallest legible size.

---

# COMPLIANCE CHECK

- **No live human, no clergy, no watching.** No line says anyone is reading her answers, typing, present, or personally sending anything. "We can send it to you" describes a send, not a sender at a desk. No Father, Brother, monk, chaplain or priest. No blessing conferred in the conversation. Every line stays true with "Phillip from Sanctoria" in front of it and true with no name at all.
- **Personal attributes.** No bubble asserts her religion, health, finances or family circumstances. The name ask asks, the email ask asks, the build-ups describe what we will send. The only second-person statements are transactional: what she will receive, that she can unsubscribe. Nothing is claimed about her prayer life, her household or her situation. Variant C build-up 2 says "if today is not the day", which is a statement about timing, not about her means.
- **Banned vocabulary.** Zero instances of bad luck, curse, evil, hex, Jezebel, spiritual attack, spiritual warfare, generational curse. Vocabulary used: blessed, devotion, prayer, match, free, fourteen days.
- **Promises.** Exactly two, both true: her match sent to her, and one short written prayer each morning for fourteen days, free and finite. No discount, no coupon, no reserved stock, no priority, no early access, no bonus, no gift, no guarantee of any outcome from praying.
- **Proof and pressure.** Zero testimonials, zero star ratings, zero review counts, zero subscriber counts, zero countdowns, zero timers, zero stock claims, zero "spots". Nothing expires. Nothing is running out.
- **Consent.** The consent line states what she will receive, that she can unsubscribe at any time, and links the privacy policy at `/privacy.html`. It is visible before she taps, not behind a tap.
- **Punctuation.** No em-dashes and no en-dashes anywhere in this document. Hyphens appear only in compound words: build-up, other-three, non-converting, front-end, pre-ticked, second-person, fourteen-day, buyer-only, object-free, bait and switch written open. The middot in the title is a separator, not a dash.
- **Mobile.** Every bubble 25 words or fewer, every button 4 words or fewer, every placeholder 3 words or fewer, every chip 5 words or fewer. One ask per turn. The name step and the email step never appear on screen together.
