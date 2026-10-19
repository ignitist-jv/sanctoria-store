# SERIES A: buyers (tag prayer-song-buyer)

## EMAIL: A1
SEND: 1 day after purchase
SUBJECT: Four ways to keep {{ subscriber.prayer_song_for }}'s song close
PREVIEW: Play it, keep it, send it, and pray along with every word.
P: {% if subscriber.first_name != blank and subscriber.first_name != subscriber.prayer_song_for %}{{ subscriber.first_name }}, {% endif %}{{ subscriber.prayer_song_for }}'s prayer song is on your private page, and it is yours to keep. Here are four simple ways to live with it.
P: Play it at a set time. The morning coffee, the drive home, the last minutes before sleep.
P: Download it. The MP3 plays on any phone or computer, and once it is saved it needs no internet.
P: Send the link to family. Anyone with it can listen, so the same prayer is prayed in more than one house.
P: Pray along with the lyrics. Every word is on the page, to read slowly or sing quietly with the chorus.
BUTTON: Open My Song Page
BUTTON_LINK: {{ subscriber.prayer_song_link }}
P_AFTER: If the name is not sung right, reply and tell us how it should sound. We will remake the song at no charge.
SIGNOFF: With our prayers, Sanctoria

## EMAIL: A2
SEND: 3 days after purchase
SUBJECT: Nine days beside {{ subscriber.prayer_song_for }}'s song
PREVIEW: One page a day, about ten minutes, with the song at the heart of each day.
P: {% if subscriber.first_name != blank and subscriber.first_name != subscriber.prayer_song_for %}{{ subscriber.first_name }}, {% endif %}{{ subscriber.prayer_song_for }}'s song page also holds the Nine Day Prayer Companion, a printable made to be prayed alongside the song.
P: Each day is one page: a verse of Scripture, a short reflection, and a prayer with a line for the name. Then the song is played, and the day closes with an Our Father, a Hail Mary and a Glory Be. It asks about ten minutes.
P: Choose a time that can be kept: the kitchen table before the house wakes, or the bedside at night.
P: If a day is missed, nothing is lost. Pick it up again where it was left.
BUTTON: Find The Companion
BUTTON_LINK: {{ subscriber.prayer_song_link }}
P_AFTER: When the nine days end, the prayer does not. They can be begun again whenever there is need.
SIGNOFF: With our prayers, Sanctoria

## EMAIL: A3
SEND: 7 days after purchase
SUBJECT: A small question about {{ subscriber.prayer_song_for }}'s song
PREVIEW: Only if you would like to. A sentence is enough, and nothing is shared without asking.
P: {% if subscriber.first_name != blank and subscriber.first_name != subscriber.prayer_song_for %}{{ subscriber.first_name }}, {% endif %}{{ subscriber.prayer_song_for }}'s prayer song has been yours for a week. We would be glad to hear what it has meant, in your own honest words.
P: At the foot of your song page is a short form. A rating and a sentence is enough: where it was first played, or what stayed with you. Whatever is true.
P: It is entirely optional, and nothing is given in exchange. Nothing is shared without your permission. The form asks first, and if that box is left unticked, your words are read only by us. They can be changed or withdrawn at any time.
P: If something is not right, we would rather hear that too.
BUTTON: Leave A Few Words
BUTTON_LINK: {{ subscriber.prayer_song_link }}
SIGNOFF: With our prayers, Sanctoria

## EMAIL: A4
SEND: 14 days after purchase
SUBJECT: Another name in your prayers
PREVIEW: A prayer song can be made for someone else, in just the same way.
P: {% if subscriber.first_name != blank and subscriber.first_name != subscriber.prayer_song_for %}{{ subscriber.first_name }}, {% endif %}{{ subscriber.prayer_song_for }}'s prayer song carries one name. Most hearts carry several.
P: A husband, prayed for across the kitchen table each morning. A grandchild growing up faster than seems possible. A mother or a friend who has passed, and is still prayed for every day.
P: A second song is made the same way: the name, the prayer, the sound, and a verse of Scripture at its heart, with the name sung in every chorus. The same three printables come with it.
P: It is $39, one time, sent by email within 24 hours, with the same 30 day refund.
BUTTON: Begin Another Song
BUTTON_LINK: https://sanctoriastore.com/prayer-song/
P_AFTER: There is no hurry. When a name comes to mind, the page will be there.
SIGNOFF: With our prayers, Sanctoria

## EMAIL: A5
SEND: 30 days after purchase
SUBJECT: Thinking of {{ subscriber.prayer_song_for }}'s song today
PREVIEW: A month on, one small thing to keep beside it.
P: {% if subscriber.first_name != blank and subscriber.first_name != subscriber.prayer_song_for %}{{ subscriber.first_name }}, {% endif %}{{ subscriber.prayer_song_for }}'s prayer song has been with you for a month. We hope it has found a place in the day, in the car, at the sink, or in the quiet before sleep.
P: If it has slipped from the routine, that is all right. Prayer has its seasons.
P: One small thing can help: the Daily Prayer Card on your song page. It is one short prayer with the name on it, made to print for the fridge door or the bedside, so the prayer is seen even on the days the song is not played.
P: The page is still there, and the song is still yours.
BUTTON: Open My Song Page
BUTTON_LINK: {{ subscriber.prayer_song_link }}
P_AFTER: If anything is ever wrong, or you simply want to tell us something, reply to this email. Every reply is read.
SIGNOFF: With our prayers, Sanctoria

# SERIES B: reached payment, did not buy (tag prayer-song-lead; removed on purchase)

## EMAIL: B1
SEND: 1 hour after reaching payment
SUBJECT: Your answers for {{ subscriber.prayer_song_for }}'s song are saved
PREVIEW: The order was not finished, so the song has not been started yet.
P: {% if subscriber.first_name != blank and subscriber.first_name != subscriber.prayer_song_for %}{{ subscriber.first_name }}, {% endif %}{{ subscriber.prayer_song_for }}'s prayer song has not been started yet, because the order was not finished.
P: Nothing you wrote has been lost. The name, the prayer and the sound you chose are saved, just as you left them.
P: One tap opens the form again at the last step, where the order can be finished.
BUTTON: Return To My Prayer Song
BUTTON_LINK: {{ subscriber.prayer_song_resume_link }}
P_AFTER: If something went wrong at checkout, or a question came up, reply to this email and we will help.
P_AFTER: If now is not the right time, there is nothing you need to do. Your answers will keep.
SIGNOFF: With our prayers, Sanctoria

## EMAIL: B2
SEND: 1 day after reaching payment
SUBJECT: A prayer for {{ subscriber.prayer_song_for }}, set to music
PREVIEW: What the song is, what it costs, and how the refund works.
P: {% if subscriber.first_name != blank and subscriber.first_name != subscriber.prayer_song_for %}{{ subscriber.first_name }}, {% endif %}{{ subscriber.prayer_song_for }}'s prayer song would be an original prayer set to music, built on a verse of Scripture, with the name sung in every chorus.
P: A spoken prayer is said once. A song can be played in the car, in a quiet room, or sent to the family, and each time someone listens and means it, the prayer is prayed again.
P: With it come a keepsake lyric sheet, a nine day prayer companion and a daily prayer card, ready to print.
P: It is $39, one time, with no subscription. It arrives by email within 24 hours, usually in about two. If it is not right, one email to support@sanctoriastore.com within 30 days brings a full refund.
P: Sample songs can be heard first on our page, sanctoriastore.com/prayer-song.
BUTTON: Finish My Prayer Song
BUTTON_LINK: {{ subscriber.prayer_song_resume_link }}
SIGNOFF: With our prayers, Sanctoria

## EMAIL: B3
SEND: 3 days after reaching payment
SUBJECT: {{ subscriber.prayer_song_for }}'s song can wait for the right day
PREVIEW: Your answers stay saved. There is nothing you need to do today.
P: {% if subscriber.first_name != blank and subscriber.first_name != subscriber.prayer_song_for %}{{ subscriber.first_name }}, {% endif %}{{ subscriber.prayer_song_for }}'s prayer song is still waiting to be made.
P: Sometimes a prayer waits for the right day. That is all right.
P: Your answers stay saved. If you come back to them, the form opens at the last step, and the song is sent within 24 hours of the order.
P: Thank you for bringing {{ subscriber.prayer_song_for }} to us.
BUTTON: Finish My Prayer Song
BUTTON_LINK: {{ subscriber.prayer_song_resume_link }}
P_AFTER: If a question comes up, reply to this email and we will answer.
SIGNOFF: With our prayers, Sanctoria

## EMAIL: B4
SEND: 7 days after reaching payment
SUBJECT: Why a sung prayer is prayed again
PREVIEW: The hymns we still know by heart, and what they have to do with a name.
P: {% if subscriber.first_name != blank and subscriber.first_name != subscriber.prayer_song_for %}{{ subscriber.first_name }}, {% endif %}{{ subscriber.prayer_song_for }} was brought to us a week ago, with a prayer and a sound chosen with care. There is something worth saying about why that prayer would be sung.
P: Think of a hymn learned as a child. Decades later the words still come back: at a funeral, in the car, over the kitchen sink. A prayer said once is easily lost. A prayer that is sung stays. The Church has always sung what it most wanted to keep.
P: Each time the song plays, and someone listens and means it, the prayer for {{ subscriber.prayer_song_for }} is prayed again, in every house the link is sent to.
P: One sample can be heard at sanctoriastore.com/prayer-song.
BUTTON: Finish My Prayer Song
BUTTON_LINK: {{ subscriber.prayer_song_resume_link }}
P_AFTER: Your answers are still saved, and the button opens them at the last step.
SIGNOFF: With our prayers, Sanctoria

## EMAIL: B5
SEND: 14 days after reaching payment
SUBJECT: The last note about {{ subscriber.prayer_song_for }}'s song
PREVIEW: We will not write about this order again. Your answers stay saved.
P: {% if subscriber.first_name != blank and subscriber.first_name != subscriber.prayer_song_for %}{{ subscriber.first_name }}, {% endif %}{{ subscriber.prayer_song_for }}'s prayer song is still waiting, and this is the last note we will send about it.
P: Your answers stay saved. If you come back to them, the form opens at the last step, and the song is sent within 24 hours of the order.
P: If the time is not right, or the prayer has changed, that is all right too. A prayer can wait for its day.
P: Thank you for bringing {{ subscriber.prayer_song_for }} to us.
BUTTON: Finish My Prayer Song
BUTTON_LINK: {{ subscriber.prayer_song_resume_link }}
P_AFTER: There will be no more emails about this order. If a question ever comes up, reply and we will answer.
SIGNOFF: With our prayers, Sanctoria

=== NOTES ===

1. Greeting. Every email opens with the same Liquid test as 07-abandoned-checkout.md: the brief's `{% if subscriber.first_name != blank %}` plus `and subscriber.first_name != subscriber.prayer_song_for`, so a woman who made the song for herself never reads "Mary, Mary's prayer song". Each opening sentence begins with the song name, which is already capitalised, so it reads correctly with or without the greeting. If Drip rejects the compound condition, drop the second test and accept the rare doubled name.
2. Myself and passed branches. Nothing in either series says the person is alive, ill or present. A4 names "someone who has passed" only as an example of another person to pray for.
3. One name or two. The brief says a song carries one first name; the product bible (2026-10-07) allows two. All lines are written so either reads correctly: `prayer_song_for` is only ever possessive, an object, or after "for"/"about". A4's "carries one name" would be wrong for a two name song; if two name songs are still sold, change it to "carries the names it was made for."
4. B1 to B3 changes from 07-abandoned-checkout.md: added SEND and BUTTON_LINK lines to all three; B2 adds "usually in about two" to the delivery sentence (drop it if the two hour typical time is not reliable); B3 has a new subject and preview, loses "and this is the last reminder we will send about it" from the first paragraph, and its P_AFTER no longer says there will be no more reminders. The "last note" wording moved to B5.
5. Sample links. B2 and B4 name the page in plain text because every button goes to the resume link. Hyperlink that text to the sample anchor on the landing page in Drip. If the sample section is ever removed, cut those lines.
6. `{{ subscriber.prayer_song_intention }}` is not used, by design: it may be empty and the copy reads fully without it.
7. Express Song Delivery is not mentioned anywhere. A4 could carry "Express Song Delivery, within 1 hour, is offered at checkout for $9.95." as a P_AFTER if wanted; I left it out so the email shows a single price.
8. A5 lands on day 30, the last day of the refund window. It deliberately does not mention the refund, but its reply line gives a route if something is wrong.
9. Build dependencies: "your answers stay saved" (B1, B3, B4, B5) is only true while the resume link keeps working; state a period if saved answers expire. "Reply to this email" assumes replies reach support@sanctoriastore.com. A3 assumes the review form sits at the foot of the song page and keeps the permission tick, as in 03-delivery.md.
10. Rules checked: no deadline, discount or countdown; no testimonial, review count or popularity claim; no singer or songwriter; nothing blessed or prayed over; no outcome promised; no "Catholic"; the product name never run together as one word; no em or en dashes. Body word counts, buttons and previews were measured by script after writing; all bodies under 130 words, buttons under 28 characters, previews under 90 characters.
