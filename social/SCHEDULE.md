# Sanctoria Social · Week 1 run sheet

Paste-in-order sheet for one scheduling session in **Meta Business Suite Planner**, which posts to Facebook and Instagram from the same screen.

Captions: `social/2026-10-08-week-01.md`
Images: `social/images/`

---

## Recommended time: 07:00 America/New_York, every day

Three reasons, not a guess.

**It matches the content.** These prayers are about the first part of the day. "Four minutes in a parked car." "One decade before the kettle boils." "At a red light." A prayer about the morning that arrives at 9pm has already missed.

**It matches the list.** Your Kit buyer prayer series already sends at 06:00 America/New_York to this exact avatar. Same woman, same hour, one hour apart. The page and the inbox start reinforcing each other instead of competing.

**It puts you at the keyboard for the first hour.** 07:00 EDT is **19:00 Singapore**. The first sixty minutes of a post decide its reach, and that is the window where replying to comments matters most. You would be at dinner, not asleep.

---

## The order

**Run Saturday's post first, not Tuesday's.** The reasoning is in the captions file. Short version: the engagement post needs a page with a pulse, and right now there is not one.

| # | Date | Day | Image | Opens with |
|---|---|---|---|---|
| 1 | Thu 8 Oct | Thursday | `01-thu-reopening.jpg` | Our Lady of the Rosary, this month is yours. |
| 2 | Fri 9 Oct | Friday | `02-fri-prayer.jpg` | Jesus, mercy. |
| 3 | **Sat 10 Oct** | Saturday | `03-sat-our-lady.jpg` | Blessed Mother Mary, some of us have asked so long |
| 4 | Sun 11 Oct | Sunday | `04-sun-sunday.jpg` | Lord, bless this house and everyone who comes through its door. |
| 5 | Mon 12 Oct | Monday | `05-mon-joyful.jpg` | Blessed Mother, today we pray the Joyful Mysteries with you. |
| 6 | Tue 13 Oct | Tuesday | `06-tue-engagement.jpg` | Who are you praying for this week? First names only. |
| 7 | Wed 14 Oct | Wednesday | `07-wed-cord-rosary.jpg` | Lord, there is someone missing from this table. |

**Post 1 is dated today.** If today has already got away, start at post 2 tomorrow and let post 1 go out next Thursday. Do not post two on one day to catch up; a page returning from eleven weeks of silence should return once.

---

## Before the session, three things

- [ ] **Page category.** Still *Arts and crafts shop*. Change to **Religious organisation**, which is what The Divine Mercy (505,000 followers) uses. Category feeds who Meta shows the page to, so this affects all seven.
- [ ] **Instagram bio.** Still blank. Post 7 depends on it.
      > Blessed devotionals, hand-blessed in the Benedictine tradition.
      > Worn daily. Passed down.
      > Free US shipping · 30-day refund
      > ↓ Find the one that fits

      Link: `sanctoriastore.com/chat/`
- [ ] **Instagram connected to the Page.** This is what makes Planner post to both at once. It is a different link from the ad-account assignment, which is still not showing through the API.

---

## During the session

1. Open Business Suite, Planner, Create post.
2. Select **both** Facebook and Instagram.
3. Upload the image for that day.
4. Paste the Facebook caption.
5. Switch to the Instagram tab and paste the Instagram caption, which is the same prayer plus hashtags. **Instagram cannot click a link in a caption**, so post 7's Instagram version says "Link in bio" rather than the URL.
6. Set 07:00, that day's date.
7. Repeat seven times.

Budget about twenty minutes.

---

## Afterwards

**The first hour of each post is the part that matters.** Reply to every comment that is a name or an Amen, briefly and in the same register. "Amen" back is enough. On a prayer page that reply is the product.

**Harvest Tuesday's thread.** Every first name and every phrase goes into `LEARNINGS.md` as real voice-of-customer language. That is the second product of that post and it is worth as much as the reach.

**What not to do.** Do not reply with "we are praying for them", on any post. Sanctoria does not pray for anyone by name, the captions are carefully written never to imply it, and a reply can undo in four words what the whole week was built to protect.

---

## What I could not do

I have no tool in this session that publishes or schedules to Facebook or Instagram. Everything Meta-side here is ads-only: campaigns, ad sets, creatives, and boosting a post that already exists.

**To hand this over properly**, see `social/SETUP.md` Phase 1: a second System User token scoped to `pages_manage_posts` and `instagram_content_publish`. With that in `.env` I publish on a schedule from an approved queue, the same way I already drive your Kit sequences, and this run sheet becomes a cron job instead of twenty minutes of your Tuesday.
