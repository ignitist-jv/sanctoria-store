# The order bump: verified diagnosis and what to configure
2026-10-12. Closes the flag that has been open four days in ANGLE_LEDGER.md and AD_BRIEF.md.

## Verified, by rendering each live checkout

**No order bump renders on ANY template.** Not one of the five.

| Template | Item tested | Bump renders? |
|---|---|---|
| order-2 | bracelet-1 | NO |
| order-3 | medal-1 | NO |
| order-4 | necklace-1 | NO |
| order-5 | rosary-1 | NO |
| songform | prayersong-1 | NO |

ClickBank's React bundle ships bump scaffolding in the HTML (`bump-container`,
`bump-copy`, `BumpId`) on every template, so grepping the source is misleading.
Nothing is configured, so nothing paints. That is the whole explanation for
zero `bump-blessing` first payments against 11 new buyers.

## The brief is chasing the wrong bump for Prayer Song

There are TWO different bumps in this project and they have been conflated.

**1. `bump-blessing`, $17/month subscription.** The bracelet-side bump. The
ledger tracks it and asks for it to be verified on `songform`.

**2. `express-1`, "Express Song Delivery".** The Prayer Song bump. It is
ALREADY BUILT in the back end and has been since the offer was made:

- `site/prayer-song/api/lib.php:49`  `'express_items' => ['express-1']`
- `site/prayer-song/api/lib.php:48`  `'send_after_express' => 3600`
- `site/prayer-song/api/ins.php:24`  detects it on the receipt line items and
  calls `ps_mark_express()`
- Effect: delivery drops from 2 hours to 1 hour.

So for Prayer Song the code is finished and waiting. ClickBank simply has no
`express-1` item, and no bump attached to the `songform` template.

## Do NOT put bump-blessing on the Prayer Song checkout

Two reasons, both from this project's own records.

1. `LEARNINGS.md` line 235: the $17/month rebill "generated 3 of the 4 refunds
   and chargebacks in that window". It carries the margin and it carries the
   complaints.
2. It does not fit the purchase. The buyer is giving one named song to one
   person as a gift. A recurring monthly devotional subscription bolted to a
   one-off gift is a mismatch, and on this audience a trust problem.

## Three candidates, your call

**A. `express-1` Express Song Delivery. Recommended.**
Back end already built, zero marginal cost, fits the buyer (a gift giver who
wants it sooner). Nothing in the repo sets a price, so that is the one
decision: suggest $9 to $14.

**B. Keepsake Lyric Sheet, $9.**
`PRODUCT-FLOW.md:90` lists it as a $9 bump, but `copy/04-bonuses.md`, the
landing page and `copy/05-legal.md` all promise it FREE with every order. Your
own copy notes flag this contradiction twice and it is still unresolved
(`04-bonuses.md:152`, `01-landing-page.md:172`). Using it as a bump means
changing the page, the FAQ and the legal text first.

**C. `bump-blessing` $17/month.** Not recommended, see above.

## What you have to do (I have no ClickBank write access)

1. ClickBank, create the item: `express-1`, "Express Song Delivery", one time,
   price set.
2. Attach it as an order bump on the `songform` template.
3. Do the same review for order-2, order-3, order-4, order-5. Those four are
   all paused product lines right now, so Prayer Song is the only urgent one.

## What I do after

Re-render every template and confirm the bump actually paints. That render
check is exactly what has been missing for four days; the flag kept being
raised from sales data rather than from looking at the page.

## Note on sequencing

AD_BRIEF.md says to verify the bump "before any further creative spend", and
ANGLE_LEDGER.md says not to build more creative on the SungByName angle until
one ad clears ~75 outbound clicks. Current state is 14 outbound clicks across
three ads. The six PHOTO ads are on hold behind both of those.
