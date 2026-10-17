## EMAIL: abandon1
SUBJECT: Your answers for {{ subscriber.prayer_song_for }}'s song are saved
PREVIEW: The order was not finished, so the song has not been started yet.
P: {% if subscriber.first_name != blank and subscriber.first_name != subscriber.prayer_song_for %}{{ subscriber.first_name }}, {% endif %}{{ subscriber.prayer_song_for }}'s prayer song has not been started yet, because the order was not finished.
P: Nothing you wrote has been lost. The name, the prayer and the sound you chose are saved, just as you left them.
P: One tap opens the form again at the last step, where the order can be finished.
BUTTON: Return To My Prayer Song
P_AFTER: If something went wrong at checkout, or a question came up, reply to this email and we will help.
P_AFTER: If now is not the right time, there is nothing you need to do. Your answers will keep.
SIGNOFF: With our prayers, Sanctoria

## EMAIL: abandon2
SUBJECT: A prayer for {{ subscriber.prayer_song_for }}, set to music
PREVIEW: What the song is, what it costs, and how the refund works.
P: {% if subscriber.first_name != blank and subscriber.first_name != subscriber.prayer_song_for %}{{ subscriber.first_name }}, {% endif %}{{ subscriber.prayer_song_for }}'s prayer song would be an original prayer set to music, built on a verse of Scripture, with the name sung in every chorus.
P: A spoken prayer is said once. A song can be played in the car, in a quiet room, or sent to the family, and each time someone listens and means it, the prayer is prayed again.
P: With it come a keepsake lyric sheet, a nine day prayer companion and a daily prayer card, ready to print.
P: It is $39, one time, with no subscription. It arrives by email within 24 hours. If it is not right, one email to support@sanctoriastore.com within 30 days brings a full refund.
P: Sample songs can be heard first on our page, sanctoriastore.com/prayer-song.
BUTTON: Finish My Prayer Song
SIGNOFF: With our prayers, Sanctoria

## EMAIL: abandon3
SUBJECT: One last note about {{ subscriber.prayer_song_for }}'s song
PREVIEW: This is the last reminder. Your answers stay saved either way.
P: {% if subscriber.first_name != blank and subscriber.first_name != subscriber.prayer_song_for %}{{ subscriber.first_name }}, {% endif %}{{ subscriber.prayer_song_for }}'s prayer song is still waiting to be made, and this is the last reminder we will send about it.
P: Sometimes a prayer waits for the right day. That is all right.
P: Your answers stay saved. If you come back to them, the form opens at the last step, and the song is sent within 24 hours of the order.
P: Thank you for bringing {{ subscriber.prayer_song_for }} to us.
BUTTON: Finish My Prayer Song
P_AFTER: There will be no more reminders about this order. If a question ever comes up, reply to this email and we will answer.
SIGNOFF: With our prayers, Sanctoria

=== NOTES ===

1. Her own first name. Each email opens with a Liquid condition instead of a default. The greeting "Mary, " appears only when her first name is present AND differs from the song name; otherwise the sentence simply begins with the song name, which is already capitalised, so it reads correctly either way. That second test handles the myself branch, so she never gets "Mary, Mary's prayer song". I did not use a "friend" default because "Friend, Daniel's prayer song..." reads like a form letter. If the email builder does not accept a Liquid if, swap in "{{ subscriber.first_name | default: "" }}" and accept a stray comma risk, or drop the greeting entirely: every email still reads well without it.
2. One name or two. {{ subscriber.prayer_song_for }} may be "Daniel and Mary", so it is never the subject of a singular verb. It only appears as a possessive ("Daniel and Mary's prayer song"), after "for", after "about", or as an object. Checked against both forms. "The name sung in every chorus" (email 2) is true of a two name song, as with the singular "the name" in 03-delivery.md.
3. Myself and passed branches. When the song is for herself, the body speaks of "Mary's prayer song" in the third person; that is not wrong, and the greeting is suppressed. For someone who has died, nothing assumes the person is alive or ill: no bedside, no hospital, "a quiet room" instead.
4. The sample link. Every button goes to the resume link, as asked, which opens at the payment step, not the sample section. Email 2 therefore names the page in plain text. Better: hyperlink that line to the sample anchor on the landing page (e.g. sanctoriastore.com/prayer-song/#sample, whatever the real anchor is). If the sample section is ever dropped from the page (see 01-landing-page.md note 14), cut that line.
5. Express Song Delivery is deliberately not mentioned. It is offered at the payment step she returns to, and adding it here would put a second price in a reassurance email. If you want it in, the cleanest spot is a P_AFTER in email 2: "At checkout, Express Song Delivery sends it within 1 hour, for $9.95 more."
6. Promises that depend on the build. "Your answers are saved / will keep / stay saved" and "the form opens at the last step" are only true if the resume link keeps working. If saved answers expire (say after 30 days), soften email 3 to "Your answers are saved for now" or state the period. "Reply to this email" assumes replies reach support@sanctoriastore.com, as the delivery emails already assume.
7. Rules checked: no deadline, no discount, no countdown, no reviews or numbers, no singer or songwriter, nothing blessed or prayed over by us (the sign-off "With our prayers" matches the existing emails), no outcome promised, no "Catholic", no "PrayerSong", no em or en dashes. Body word counts (P and P_AFTER, merge fields counted as one word, Liquid tags excluded): abandon1 90, abandon2 122, abandon3 91, all under 130. Buttons: 24, 21, 21 characters. Previews: 65, 58, 62 characters.
8. Alternative subject lines, if you want to test: "{{ subscriber.prayer_song_for }}'s prayer song, not started yet" (email 1); "Before you decide about {{ subscriber.prayer_song_for }}'s song" (email 2); "The last reminder about the prayer song" (email 3).
