# Sanctoria: four sales pages, audit and copy plan
Date: 2026-09-09

## Section 0. Two live bugs that outrank every copy fix here

### 0.1 The necklace page underprices itself by $10 on every tier

Verified by loading each ClickBank order form in a browser and reading the cart.
USD figures converted at the rate calibrated from bracelet-1, which the page and
the form agree is $37 (SGD 51.94).

| Item | Page says | Order form | Match |
|---|---|---|---|
| bracelet-1 | $37 | $37 | yes |
| bracelet-3 | $57 | $57 | yes |
| medal-1 | $37 | $37 | yes |
| medal-3 | $57 | $57 | yes |
| rosary-1 | $37 | $37 | yes |
| rosary-2 | $47 | $47 | yes |
| rosary-3 | $57 | $57 | yes |
| **necklace-1** | **$37** | **$47** | **NO, +$10** |
| **necklace-2** | **$47** | **$57** | **NO, +$10** |
| **necklace-3** | **$57** | **$67** | **NO, +$10** |

Every visitor to /necklace/ clicks a button that says $37 and lands on a form that
charges $47. The necklace is the only product on the site with this problem, and it
is on all three tiers.

Two ways to fix it, and they are not equivalent:

1. Change the ClickBank items to $37 / $47 / $57 so they match the page. Keeps the
   advertised price, keeps the page copy, loses $10 of AOV per order.
2. Change the page to $47 / $57 / $67 so it matches the items. Keeps the AOV, but
   every price, strikethrough, per-unit figure and "From $37" line on the page has
   to move, and the necklace stops being price-consistent with the other three
   products.

Recommendation: option 1. The other three products all sit at $37 / $47 / $57 and
the ads and the brand are built around $37 as the entry point.

### 0.2 A monthly subscription is attached to every rosary order form

The three rosary order forms carry a recurring item, "Mother Mary Daily Blessings",
listed at SGD 0.00 today with:

> Future Payment: Monthly payment of SGD 26.01
> Next payment will be billed on October 9, 2026. Payments are billed every month.

That is roughly $18.50 per month, recurring, presented on the order form of a $37
rosary. It does not appear on bracelet, medal or necklace forms, only rosary.

Confirm this is intentional. A devotional buyer aged 45+ who finds an unexpected
$18.50 monthly charge is a refund, a chargeback and a ClickBank complaint, and the
refunds land against the same nickname that carries your two proven offers.

### 0.3 Product naming does not match between page and checkout

The rosary page sells "The Saint Benedict Cord Rosary". The order form says
"Saint Benedict Protection Rosary". Small, but it lands at the highest-friction
moment on the page with the least copy supporting it.

---

## Section 1. Microsoft Clarity is not usable yet

The Clarity MCP in this session is authenticated against a different property. It
returns data for getbirthcode.com and reports zero sessions for anything matching
sanctoriastore.com over the last three days.

Sanctoria's own Clarity tag IS installed and correct, project id `ydd7lw8hiu`, and
it is present on all 30 pages under site/, sales pages and thank-you pages alike.
Data is being collected. This session simply cannot read it.

To unblock: generate a Data Export API token inside the Clarity project `ydd7lw8hiu`
(Settings, then Data export) and connect that token to the Clarity MCP in place of
the getbirthcode.com one. Once connected, the questions worth asking first are
scroll depth by page, rage clicks and dead clicks on the pricing tiers, and the
exit page for sessions that reached a checkout link but did not click it.

Every recommendation below is therefore based on the copy itself, not on behaviour.
Treat it as a hypothesis list to validate against Clarity once the token is in.

---

## Section 2. What the four pages actually are

| Page | Words | Images | Tier prices | Proof honesty | Batch dates |
|---|---|---|---|---|---|
| /bracelet/ | 1,449 | 28 | $37/$47/$57 | fabricated | HARDCODED, STALE |
| /guard/ | 2,649 | 25 | $37/$47/$57 | fabricated | auto-rolling |
| /necklace/ | 3,461 | 18 | $37/$47/$57 page, $47/$57/$67 charged | clean | auto-rolling |
| /rosary-necklace/ | 391 | 34 | $37/$47/$57 | clean but a fake-looking photo wall | auto-rolling |

Length runs from 391 to 3,461 words, a 9x spread, with no relationship to price or
to how much explaining the product needs.

### 2.1 The fabricated proof problem, and why it is now urgent

/necklace/ and /rosary-necklace/ were built clean. /bracelet/ and /guard/, the two
pages that actually carry ad traffic, were not.

/bracelet/ currently runs:
- "4.9 · Loved by 1,800+ Blessed Families"
- "1,847 verified reviews from over 1,800 blessed families"
- "95% Reserved" and "23 Reservations Remaining"
- twelve named testimonials, each marked "verified"

/guard/ currently runs:
- a "% Reserved" figure generated in JavaScript as `88 + (baseSeed % 9)`
- four named testimonials
- the line "Customer quotes shared with permission. First name and city only."

The part that turns this from a policy question into a live risk: **Rosa V.,
Kathleen O. and Patricia L. appear on both /bracelet/ and /guard/**, with the same
cities, reviewing two different products. Anyone comparing the two pages, including
a platform reviewer working a complaint, sees the same four women reviewing both.
The "shared with permission" line on /guard/ makes it worse, because it is an
explicit provenance claim about quotes that have no provenance.

This sits on a domain that already replaced one banned by Facebook.

### 2.2 The batch mechanic is broken in two different directions

- /bracelet/ hardcodes JUN 29 Sold Out, JUL 21 95% Reserved, AUG 10 Upcoming, with
  no updater. On a September 9 visit the "upcoming" batch closed a month ago. This
  is the one thing on the site a visitor can catch in a single glance.
- /guard/, /necklace/ and /rosary-necklace/ auto-roll their dates nightly, which is
  the opposite failure: a deadline that resets every morning and never arrives.

Recommendation: drop dated scarcity everywhere. You have a true urgency you are not
using, which is that the batch on the table right now is already blessed. One block,
true on all four pages, nothing to maintain:

> ### Blessed In Batches, Not One At A Time
> A batch is set out, prayed over together, and only then packed and sent. It means
> there is sometimes a short wait between batches. It also means the one that
> reaches your door was blessed before the box was ever sealed. Reserving now holds
> one from the batch already on the table.

### 2.3 Positioning collision

/bracelet/ and /guard/ are two Saint Benedict bracelets at identical price tiers,
aimed at the same avatar, from the same ad account, currently sharing testimonial
names and overlapping on the drawer mechanism. /bracelet/ and /rosary-necklace/ are
also running near-identical headlines: "Worn by Mothers. Inherited by Daughters."
against "Prayed by Mothers. Inherited by Daughters."

Proposed split, enforced in the copy:
- /guard/ owns "never comes off": waterproof, three medals, one-second adjust.
- /bracelet/ owns the object and the craft: real ebony, real bronze, knotted, made
  to be handed on.
- /rosary-necklace/ owns the heirloom lane its angle is actually named after.
- /necklace/ owns the hand-to-heart reflex, which nothing else competes with.

### 2.4 The blessing claim is inconsistent

/guard/, /necklace/ and /rosary-necklace/ all say "hand-blessed in the Benedictine
tradition". /bracelet/ still says "blessed by Benedictine monks at the abbey" in the
hero and the FAQ. LEARNINGS.md records that this exact class of claim was
deliberately downgraded when the rosary was ported. /bracelet/ is the last page
making the stronger version. Meta requires ad claims to match the landing page, and
right now the landing pages do not match each other.

---

## Section 3. Page by page

### 3.1 /bracelet/ , 1,449 words

**Biggest problem:** the fabricated proof stack is about a third of the body copy and
occupies the two highest-value slots on the page, directly under the H1 and directly
above the pricing.

**Rewritten hero.** Give the heirloom line to the rosary and give this page the object.

> Eyebrow: A Marian devotion, worn daily
>
> H1: Worn by the mother. Inherited by the daughter. Blessed before either one puts it on.
>
> Subhead: Real ebony wood beads with an antique bronze Saint Benedict medal and
> crucifix, hand-knotted one bead at a time and hand-blessed in the Benedictine
> tradition. Not the thin one that ends up in a dish on the dresser. The one that
> gets handed on.
>
> Trust line, replacing the star rating in that exact slot: Hand-blessed before
> shipping · Free US shipping · 30 days, refund includes your shipping

The trust line matters as much as the headline, because the fake rating currently
occupies the credibility beat under the H1. Remove it with no replacement and the
hero loses its second-line reassurance. This is proven copy, so run it as an A/B
rather than a straight swap.

**Fix 1, replace the proof stack.** Cut the hero rating, the four named testimonials,
the ratings breakdown bars and the eight photo reviews. Replace with an honest proof
block. The full drop-in version is in section 4.

Then start collecting the real thing. There have been ClickBank orders on
bracelet-1/2/3 since July and a Kit list tagged `sanctoria-buyer`. A review request
at day ten post-delivery produces genuine quotes within a month. Until they exist,
state no customer count and no rating anywhere.

**Fix 2, give the page a mechanism.** It answers "why Saint Benedict" but never "why
this one and not the nine dollar one on Amazon". /guard/ has "The Never-Off
Standard", the strongest section on any of the four pages. Build the parallel:

> ### The Heirloom Standard
> **Four things it had to pass before we would put a blessed medal on it.**
>
> **Real ebony, not stained hardwood.** Dense enough to have weight in the hand, dark
> all the way through, so it does not go pale at the knot after a year of wear.
>
> **Knotted between every bead.** Not strung on elastic. Elastic is why cheap
> bracelets end up as loose beads in the bottom of a purse. A knot on both sides of
> every bead means one failure never becomes thirty.
>
> **Bronze that ages instead of flaking.** Solid antique bronze, not plated coating
> over pot metal. Plating lifts at the edges within a season. Bronze goes deeper and
> warmer with the years, which is the point of a thing you intend to hand on.
>
> **Blessed before it ships, never after.** It arrives ready to put on or ready to
> give exactly as it comes out of the box. You never have to arrange anything.

**Fix 3, kill the frozen dates and invented numbers.** Delete "23 Reservations
Remaining", "95% Reserved" and the three hardcoded date pills. Use the batch block
from section 2.2.

**Cut outright:** the eight-item photo review grid and rating bars, which are also
off-brand internally ("Faster shipping than Amazon", "brass medal" where the page
elsewhere says bronze). "Loved by 1,800+ Blessed Families". "1,847 verified reviews".
All four named testimonials. The abbey claim, in both the hero and the FAQ. The
footer line "Made and blessed for the Circle", which is orphan language from a
previous brand.

**Length:** 1,449 is about right for a $37 sacramental. Stripping the fake proof
takes out roughly 480 words, leaving it thin at 970. The Heirloom Standard plus the
honest proof block puts back about 400. Target 1,350 to 1,450. Same length,
different composition.

### 3.2 /guard/ , 2,649 words

**Biggest problem:** the page makes one point five times before it asks for anything.
WornNotStored is stated in full in five consecutive sections: "Worn, Not Stored",
"The Drawer", "The Never-Off Standard", "The Whole Point", "The Names You Say". That
is roughly 1,100 words spending a single idea, and it is why the page runs 2,649
words for a $37 bracelet.

**Rewritten hero.** The current one opens on a riddle and does not name the product
for forty words, so the mobile fold shows a question and no object.

> Eyebrow: The Benedict Triptych · A three-medal Saint Benedict bracelet
>
> H1: The medal that was blessed for you is in a drawer somewhere in this house.
>
> Subhead: This one does not come off. Three Saint Benedict medals on a black braided
> cord, waterproof, adjustable in one second, hand-blessed before it ships. On at six
> in the morning, still on at midnight, and you never once had to remember it.
>
> CTA: Reserve Yours · From $37
>
> Trust line: Hand-blessed before shipping · Free US shipping · 30-day full refund

**Fix 1, replace "92% Reserved" and the testimonials.** Delete the percentage element
and the JS that generates it. Delete the Denise R. pull quote, the "In Their Words"
block, and the "shared with permission" line. Three of those four names are also on
/bracelet/. Use the honest proof block from section 4, with the two product-specific
items given there.

**Fix 2, collapse five sections into two.** Keep "Worn, Not Stored" as the pain, keep
"The Never-Off Standard" as the differentiator, fold "The Drawer" in as two lines,
delete "The Whole Point" entirely and delete the restatement inside "The Names You
Say". Merged opening, roughly 190 words replacing about 700:

> ### Worn, Not Stored
> **You ask for protection every morning. Then you leave it on the dresser.**
>
> You say the prayer before the house wakes up. Kitchen table, first cup of coffee,
> the names you always say. Then the day starts. Keys, purse, the drive, the list,
> the phone. By ten o'clock the prayer is behind you.
>
> That is not small faith. That is a busy day.
>
> And you already own blessed things. Where are they right now? The medal from your
> confirmation, in the small dish on the dresser. A rosary in the car console. A holy
> card behind a photograph. A scapular in the top drawer with the good jewelry. You
> never stopped believing in a single one of them. They simply stopped coming with
> you.
>
> The problem was never how much you believe. It is that every holy thing you own has
> to be picked up, carried and put back, and a day like yours does not leave a free
> hand.
>
> **So this one was built to never come off.** Flat and quiet under a sleeve. Into the
> shower, the sink, the rain, the hospital waiting room, and back out again. Then you
> glance down in the middle of an ordinary Tuesday, and the three medals are right
> there.

**Fix 3, put a buy option mid-page.** The reader currently passes eight sections
before seeing a price. Insert immediately after "Why Three Medals", where the product
is fully explained:

> **Three medals, on at six in the morning, still on at midnight.**
> From $37, hand-blessed before it ships, free US shipping, and thirty days to decide.
> **Reserve Yours · From $37 →**
> *Keep reading if you want to know why the second one costs almost nothing.*

**Cut outright:** "The Whole Point" in its entirety. The Denise R. quote and the whole
"In Their Words" block. The "% Reserved" element and its generator function. The
duplicated letters explanation, which appears as a star box and again in "What
Arrives At Your Door". The closing "Everything That Comes With It" recap, which
repeats the arrival list item for item 150 words from the buy button.

**Length:** roughly 700 words too long, all of it in the middle. Target 1,900 to
2,000. Cut the loop, not the specificity. The twelve-question FAQ is genuinely good,
leave it.

### 3.3 /necklace/ , 3,461 words

**Biggest problem, after the $10 pricing bug in section 0.1:** the page is written
about the customer instead of to her. The v2 compliance rewrite pushed every second
person line into third person and over-corrected. Meta's personal attributes policy
governs ad copy, and even there it prohibits asserting you know an attribute, not
addressing the reader. On a landing page it does not apply at all.

Compare the same emotional beat on the two pages:

> /necklace/: "Nobody needs to be told to try harder. These women have carried these
> people for years, and tomorrow will be as full as today was."
>
> /guard/: "Nobody is asking you to try harder. You have been carrying these people
> for years."

The second is far stronger. The pattern repeats throughout: "Most people who wear one
have been carrying a name for years", "Ask around a parish rosary group. Every woman
in the room has one". The reader is shown a study of women like her rather than being
spoken to, and across 3,461 words that temperature drop compounds.

**Rewritten hero.** The current one is the best writing on the site. Keep the idea,
put the reader inside it.

> Eyebrow: The Benedict Double Protection Necklace
>
> H1: When the phone rings at the wrong hour, your hand goes straight to your chest.
>
> Subhead: Give it something to find when it gets there. A blessed Latin cross and a
> Saint Benedict medal on one chain, worn at the center of the chest where your hand
> already goes. Waterproof, hand-blessed before it ships, and nothing in an ordinary
> day is a reason to take it off.
>
> Trust line: Hand-blessed · Waterproof · 30 days, refund includes your shipping

**Fix 1, restore second person** across "The Reflex", "Where Holy Things End Up",
"The Names" and "The Second One". Model rewrite for "The Names":

> ### The Names
> **You have been carrying the same name for years**
>
> Every woman in your rosary group has one. Usually more than one, and usually the
> same ones she had ten years ago. You know exactly which of yours is which.
>
> One of them stopped going to Mass and will not talk about it. One is in a marriage
> that has gone quiet in a way you recognize, because your mother's did the same. One
> is waiting on results and keeps telling you he feels fine. One is still small enough
> to climb into your lap, and you cannot follow her everywhere.
>
> You said their names at the kitchen table this morning. By ten o'clock you were
> thinking about the electric bill. You meant to come back to it. You will mean to
> again tomorrow.
>
> **Nobody is asking you to try harder.** You have carried these people for years, and
> tomorrow will be as full as today was. The distance does not close because somebody
> pushed.
>
> Your mother wore something every day. A medal, a scapular, something small under her
> collar. She never had to decide to. It was just there.
>
> Then one afternoon at a red light your hand lands at the center of your chest, thumb
> on the medal, and you have said their names again without ever deciding to.
>
> **Something that keeps asking after the day takes over.**

Keep the ads in third-person community framing. The page should not be.

**Fix 2, make the product description match the photographs.** LEARNINGS.md records
that the real product is a fine round snake chain of about 1.2mm with two pendants on
adjacent jump rings and no large O-ring, and that all eleven images were regenerated
against real supplier photos on 2026-09-09. The copy still describes the old wrong
object: "two flat woven strands of equal length, about 2.5mm each", "on one shared
ring", "a double-strand flat woven chain". A reader looking at the photograph while
reading that paragraph catches you being wrong about your own product inside your
honesty section. Replacement:

> **✦ What it is made of, and why that matters.** 18K gold plated over stainless
> steel. Not brass, not a soft alloy, not a plating that lifts at the edges. The chain
> is two fine round strands of equal length, delicate enough to disappear under a
> collar, gathered into slim tapered gold end caps that meet a small lobster clasp at
> the front, where the closure is meant to be seen rather than hidden at the back of
> the neck. The cross and the medal hang from that same front junction, side by side,
> so one palm covers both. The cross is a plain Latin cross with no figure on it,
> about twice the height of the medal. The medal has a plain polished gold edge and no
> black enamel ring. Every one of those choices exists for the same reason: something
> you take off to shower is something that ends up in a dish on the dresser by
> Thursday. This one is waterproof and tarnish resistant, so there is never a reason
> to take it off.

**Fix 3, consolidate the batch and pricing explainers,** which currently run three
times: "Why Two Cost Barely More Than One", the pricing intro, and "Why We Ship In
Batches". Keep one, immediately above the pricing grid where the objection fires:

> ### Why The Second One Costs So Much Less
> They are blessed together, not one at a time as orders come in. A batch is set out,
> prayed over, packed and sent. So a second and a third go into the same blessing, the
> same box and the same shipping label as the first, and preparing three together
> costs us very little more than preparing one. That saving is not ours to keep, so it
> comes off the second and the third instead of the first.

**Cut outright:** "Why We Ship In Batches" and the pricing intro paragraph. The "What
The Letters Mean" star box, duplicated at greater length 300 words later. The closing
"Everything That Comes With It" recap. The third repetition of the bonus list in
"What Comes By Email". The single-tier anchor, a ten percent strikethrough that is too
small to move anyone and which sitting beside the Household anchor makes both look
invented.

**Length:** too long for a $47 necklace on cold traffic, but the waste is not evenly
spread. The first third, through "Why Two", is the best copy on the site and earns
every word. The excess is administrative repetition in the middle: three batch
explainers, two letter explanations, three bonus lists, one full recap. Cut about 900
words of that and target 2,400 to 2,600. Do not cut the emotional sections, make them
second person instead.

### 3.4 /rosary-necklace/ , 391 words

**Biggest problem:** there is no argument on the page. Hero, batch tracker, pricing
table, wall of photographs. It asks a cold visitor from a Facebook ad for $37 to $57
having made one claim, in the subhead, and having given zero reasons.

The clearest single offense is the block sitting in the proof slot:

> **Prayed By Catholic Mothers**
> **Across every state, in every quiet hour.**

followed by ten image tags, every one of them `<img src="/images/rosary-3.jpg" alt="">`.
It is a customer-photo wall with no customers in it: the same product shot, ten
times, exactly where proof belongs. It reads as broken or dishonest.

**Rewritten hero.** This page should own the heirloom lane outright.

> Eyebrow: A Saint Benedict cord rosary, hand-assembled and hand-blessed
>
> H1: Your grandmother's rosary went to somebody. Decide now who gets yours.
>
> Subhead: Black matte wooden beads knotted onto braided cord, silver Saint Benedict
> medals down the whole length, and a wooden crucifix with his medal set where the
> beams cross. Built heavy enough to be prayed with every night for thirty years and
> still be worth handing on.
>
> Trust line: Hand-blessed before shipping · Free shipping · 30 days, refund includes
> your shipping

**Fix 1, write the missing page.** Four sections between hero and pricing. The two
load-bearing ones:

> ### The One That Gets Handed On
> **The rosary in your drawer came from somewhere**
>
> Most Catholic homes have one that came down. Your mother's, or her mother's, and you
> can probably picture it. Worn smooth in one place. A crucifix that has been repaired
> at least once. You know exactly which drawer it is in.
>
> Nobody in that line chose it as an heirloom. It became one because it was prayed
> with every night for forty years, and because it was made well enough to survive
> being prayed with every night for forty years. That is the whole of it. There is no
> other qualification.
>
> Now look at what you would actually hand on today. A rosary from the parish gift
> shop, on a chain that has already caught twice. Something that came free in an
> envelope with an appeal letter. A plastic one from a first Communion, in the same
> drawer.
>
> **The thing about an heirloom is that you have to buy it long before it becomes
> one.** Forty years early, in fact. Somebody in your family did that for you, and did
> not know at the time that was what they were doing.
>
> This is that rosary, at the beginning of its life instead of the end of it.

> ### Why Cord And Wood
> **Three decisions that determine whether a rosary lasts a generation or a season**
>
> **Knotted cord, not chain.** Almost every rosary that breaks breaks at a link. A
> chain has as many failure points as it has beads, and the moment one opens the whole
> decade goes. This one is braided cord, knotted on both sides of every single bead.
> If it ever gave way you would lose one bead, not the rosary. It is also silent in
> the hand, which matters at Mass and at two in the morning.
>
> **Wood, not glass or plastic.** Black matte wood, sanded rather than polished,
> because a bead you touch five decades a night should feel like something. Wood warms
> in the hand. Glass stays cold and chips. Plastic goes cloudy and tells everybody
> exactly what it is. Wood is what the monks used and it is what the years improve.
>
> **His medal all the way down.** A silver-tone Saint Benedict medal spaced along the
> whole length, an oval Saint Benedict centerpiece at the join, and his medal set
> again into the wooden crucifix where the beams cross. Wherever your fingers land in
> the decade, you are touching it.

Then two shorter ones: "What The Letters Mean", adapted from /necklace/, and "Why We
Say Offering And Not Price", which the page already has and should keep as written.
That is roughly 700 to 800 new words, and at a $57 top tier it is the cheapest money
on the site.

**Fix 2, replace the ten-identical-photo wall** with the honest proof block from
section 4, using the rosary-specific items given there. If you want photographs in
that slot, use real shots of the actual product from different angles, captioned with
what each one shows. Ten copies of one file is worse than three honest ones.

**Fix 3, un-date the batch tracker** per section 2.2.

**Cut outright:** the ten-image wall. The three date rows and the auto-update script.
"Save up to 67%" in the hero, which is only true at the top tier while the hero shows
"From $37", so the number and the price the eye lands on do not describe the same
thing. The footer line "Made and blessed for the Circle". The Certificate of
Authenticity image, unless a certificate genuinely ships in the pouch; verify before
writing it in.

**Length:** far too short, and inverted, since this carries the least argument and is
sold on the same tiers as everything else. Target 1,200 to 1,400, almost all of it
above the pricing grid.

---

## Section 4. The honest proof block

This replaces the fabricated proof on /bracelet/ and /guard/ and the photo wall on
/rosary-necklace/. Swap the two product-specific bullets per page.

> ### What There Is Instead Of Reviews
>
> **There are no customer quotes on this page. Here is why, and what there is
> instead.**
>
> Quotes are the easiest thing in the world to write, which is exactly why they are
> worth nothing. We are not putting words on this page that nobody said. When there
> are real ones, they will go here with the name of the person who said them, and not
> one minute before.
>
> What follows is everything about this that can be checked.
>
> **✦ Fifteen centuries, not fifteen months.** Benedict of Nursia founded his
> monastery at Monte Cassino in the sixth century. The medal that carries his name has
> been struck, worn and blessed by the Church for centuries since, set into the
> foundations of houses, hung over cribs, carried in the pockets of soldiers. It is
> one of the oldest sacramentals still in daily use, and it is older than every
> country it ships to.
>
> **✦ What the letters actually say.** The letters ringing the medal are initials, one
> letter per word, of the traditional Latin prayer of Saint Benedict. Among them is the
> line the Church renders in English as "May the holy cross be my light." The full
> Latin and the full English are on the card in the box. Read it once and you can
> explain it to a grandchild at Sunday dinner without reaching for a phone.
>
> **✦ [PRODUCT-SPECIFIC: what it is made of]**
>
> **✦ The blessing, and what it is not.** Each batch is hand-blessed in the Benedictine
> tradition before any of it ships, at no cost, because a blessing is not something to
> charge for. And it is worth being plain about the rest: a sacramental is not a charm.
> It has no power of its own. It is a blessed sign that turns the heart toward God and
> keeps the asking going. The grace belongs to God.
>
> **✦ [PRODUCT-SPECIFIC: the thirty-day test]**
>
> *The only review that counts here is the one you make at your own kitchen table on
> day thirty.*

Product-specific bullets:

**/bracelet/ , what it is made of:** Genuine ebony wood beads, an antique bronze Saint
Benedict medal, a bronze crucifix charm, hand-knotted between every bead with an
adjustable chain extender. Not plastic. Not a printed disc. Pick it up and the weight
tells you before you read anything.
**/bracelet/ , thirty days:** Wear it. Pray with it. If it is not right, one email to
support@sanctoriastore.com returns every cent, your shipping included. That promise is
the one piece of proof on this page that does not need anybody else's word for it.

**/guard/ , what it is made of:** Three detailed Saint Benedict medals in high-grade
tarnish-resistant stainless steel with a gold-tone finish, on heavy-duty braided black
nylon cord, closed with a sliding knot that adjusts in one second. No plating that
flakes, no cheap alloy, no clasp to fumble. Every one of those choices exists for the
same reason: something you take off to shower is something that ends up in a dish on
the dresser by Thursday.
**/guard/ , thirty days:** Wear it in the shower. Wear it to sleep. Wear it every day
for thirty days. If it does not hold up the way you expect, one email to
support@sanctoriastore.com returns every cent, your shipping included. That is the only
honest test of a bracelet whose entire claim is that it stays on.

**/rosary-necklace/ , what it is made of:** Black matte wooden beads, sanded rather
than polished, knotted onto braided black cord on both sides of every bead.
Silver-tone Saint Benedict medals along the full length, an oval Saint Benedict
centerpiece at the join, pale Our Father beads at the head of each decade, and a black
wooden crucifix with a silver corpus, the INRI plaque, and a small Saint Benedict medal
set where the beams cross. It ships in a drawstring pouch with a printed prayer card.
**/rosary-necklace/ , thirty days:** Pray a full rosary on it every night for thirty
days. That is the only way anybody has ever known whether a rosary is the one. If it is
not, one email to support@sanctoriastore.com returns every cent, your shipping
included.

---

## Section 5. Order of work

**Today, before any copy:**
1. Fix the necklace price mismatch, section 0.1. Every necklace visitor is currently
   quoted $37 and charged $47.
2. Confirm or remove the $18.50 monthly subscription on the rosary order forms,
   section 0.2.
3. Connect the Clarity token for project ydd7lw8hiu, section 1, so the rest of this
   can be measured instead of argued.

**This week:**
4. /bracelet/. Ranked first on urgency, not on lift. Be clear-eyed: fabricated social
   proof does convert, so removing it may cost conversion rate short term. It comes out
   because the same four named women review two different products on two live pages,
   on a domain that replaced one already banned. What genuinely lifts here is the
   Heirloom Standard, which the page lacks entirely, and killing the stale dates, which
   are the only thing a visitor can catch in one glance. About two hours.

**Then, by expected lift per hour:**
5. /rosary-necklace/. Highest ceiling by a distance. No argument, a fake-looking proof
   wall, and the same tier prices as everything else. About three hours takes it from a
   product page to a sales page.
6. /guard/. A good page carrying 700 words of its own echo and burying the price behind
   eight sections. Two to three hours, mostly a mobile-scroll gain. The proof swap comes
   free once written for /bracelet/.
7. /necklace/. Best-written page, least in need of rescue, which is why it ranks last on
   lift per hour. The second-person restoration is real money on the strongest angle but
   it is four hours of line editing across 3,461 words. The chain description mismatch is
   a correctness repair worth an hour on its own.

**Ongoing:** start the day-ten review request to the `sanctoria-buyer` Kit list so real
testimonials exist within a month and the honest proof block can start filling in.
