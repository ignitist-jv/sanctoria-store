## STEP: basics
H: First, the name
SUB: Each prayer song is sung by first name. Whose will this one carry?
LABEL_WHO: The one being prayed for
OPTION: Husband | husband
OPTION: Wife | wife
OPTION: Son | son
OPTION: Daughter | daughter
OPTION: Grandchild | grandchild
OPTION: Mother | mother
OPTION: Father | father
OPTION: Friend | friend
OPTION: Myself | myself
OPTION: Someone who has passed | passed
LABEL_NAME: The name to be sung
LABEL_NAME_MYSELF: Your first name
PLACEHOLDER_NAME: First name only
TIP: A first name is all we need. No surname.
LABEL_PHON: How the name is said (optional)
PLACEHOLDER_PHON: e.g. hwah-KEEN for Joaquin
TIP_PHON: Only needed when a name is not said the way it is spelled. It helps the name be sung correctly.
LABEL_NAME2: A second name to be sung (optional)
PLACEHOLDER_NAME2: First name only
LABEL_WHO2: Who the second person is
OPTION_WHO2_BLANK: Choose one
TIP_NAME2: Both names will be sung in the song. Two is the most a song can carry.
ERROR: Please choose who the song is for and enter a first name.

## STEP: prayer
H: The prayer for {name}
SUB: Choose the one intention the song will carry.
LABEL_INTENTION: What is the prayer for?
OPTION: Healing | healing
OPTION: Protection | protection
OPTION: Strength | strength
OPTION: Peace | peace
OPTION: A return to the faith | return
OPTION: A marriage | marriage
OPTION: Comfort in grief | grief
OPTION: Thanksgiving | thanksgiving
LABEL_NOTE: One thing the song should say (optional)
PLACEHOLDER_NOTE: Something about them, or a few words to include
TIP_NOTE: A line or two is plenty. No private or medical details are needed.
ERROR: Please choose what the prayer is for.

## STEP: sound
H: How it should sound
SUB: Choose the music that suits them. Every style is prayerful and unhurried.
LABEL_STYLE: The music
OPTION: Traditional hymn | hymn
OPTION: Gentle guitar | acoustic
OPTION: Gospel choir | gospel
OPTION: Country gospel | country
OPTION: Lullaby | lullaby
OPTION: Piano ballad | piano
OPTION: Folk hymn | folk
OPTION: Sacred choir | choir
LABEL_VOICE: The singing voice
VOICE: A woman's voice | female
VOICE: A man's voice | male
VOICE: Choose for me | either
TIP: Not sure? A traditional hymn suits almost any prayer. The voice is made for the song. It is not a copy of any real person's voice.
ERROR: Please choose the music and the voice.

## STEP: send
H: Almost there
SUB: One step from the prayer song for {name}.
DELIVERY_PILL: Sent within 24 hours, usually sooner
ORDER_TITLE: Your prayer song order
ROW_FOR: Song for
ROW_PRAYER: The prayer
ROW_SOUND: The sound
ROW_DELIVERY: Delivery
ROW_DELIVERY_VALUE: Within 24 hours
GUAR_TITLE: 100% money back guarantee
GUAR_BODY: Love it, or every cent comes back. Covered for 30 days, no questions asked.
LABEL_EMAIL: Send the song to
PLACEHOLDER_EMAIL: name@example.com
LABEL_BUYER: Your own first name
PLACEHOLDER_BUYER: First name
MICRO: Used to send the song and occasional notes from Sanctoria. Unsubscribe any time.
ERROR: That address does not look right. Please check for a small typo.
SUMMARY_TITLE: The prayer song
SUMMARY_LINE: For {name}. A prayer for {intention_phrase}, sung as {style_phrase}.
SUMMARY_LINE_TWO: For {name}, both by name. A prayer for {intention_phrase}, sung as {style_phrase}.
BUTTON: Continue To Checkout
PRICE_BADGE: 70% off today
PRICE_WAS: $129
PRICE_NOW: $39
MICRO2: One time. Nothing recurring. Sent within 24 hours, 30 day full refund.

## UI
BACK: Back
NEXT: Continue
STEP_NAMES: Who | Prayer | Sound | Send
STEP_OF: Step {n} of {total}
COMPLETE: {pct}% Complete
AGREE: By continuing, you agree to the Terms and Privacy Policy.

## PHRASES
husband: your husband
wife: your wife
son: your son
daughter: your daughter
grandchild: your grandchild
mother: your mother
father: your father
friend: your friend
myself: yourself
passed: the one you are remembering
healing: healing
protection: protection
strength: strength
peace: peace
return: a return to the faith
marriage: grace in marriage
grief: comfort in grief
thanksgiving: thanksgiving
hymn: a traditional hymn
acoustic: a gentle guitar song
gospel: a gospel choir song
country: a country gospel song
lullaby: a lullaby
piano: a piano ballad
folk: a folk hymn
choir: a sacred choir hymn

=== NOTES ===

1. Headings are 19, 21 (before the name is filled), 19 and 16 characters. "The prayer for {name}" grows with the name; a 12 letter name gives 27 characters, still under 34. In the myself branch it reads "The prayer for Mary", which works without a variant.

2. Pill labels on step 1 drop "My" so nine of the ten are one word and wrap evenly. "Someone who has passed" is the one long pill and should be allowed to take a full row.

3. Pronunciation now has its own optional field (LABEL_PHON). The placeholder example uses Joaquin, one of the names in tools/test_songs.json. Whatever she types there is guidance for the render only and must never be sung or printed in the lyrics as part of the name. TIP_PHON says "be sung correctly" and not "helps the singer", so nothing implies a human singer.

4. For the passed branch the builder shows only grief, peace and thanksgiving. Optional memorial phrases for the summary line, kept out of PHRASES to avoid duplicate keys: peace: eternal rest and peace. grief: comfort for those who miss them. thanksgiving: thanksgiving for a life.

5. The open note box is new input from buyers and goes into lyrics. It needs the safety check in PRODUCT-FLOW (step b) before rendering. The tip tells her medical details are not needed, in line with the bible's "never asked" list, but she may type them anyway; the lyric writer must not turn a diagnosis into a line of the song or into any claim about healing.

6. The bible's "What she chooses" lists four things and puts style under "later". This survey now asks style and voice up front, and an optional note, and her own first name. The bible should be updated to match.

7. Style labels. "Gentle guitar" stands in for acoustic worship and "Gospel choir" for gospel, since those are the words a Catholic woman of 60 would use. The sub line promises every style is "prayerful and unhurried", so the gospel and country renders must actually be slow; if the render test produces upbeat tracks for those keys, change the sub or drop the style. The landing page FAQ says each song is checked, and nothing there names the styles, so no landing page line conflicts.

8. The voice tip states the voice is not a copy of a real person's voice, which keeps the bible rule (never imply a loved one's voice or a named artist) visible at the point of choice. "Choose for me" maps to either.

9. AGREE uses "you" as a plain legal instruction, not a personal attribute. LABEL_NAME_MYSELF reads "Your first name" and LABEL_BUYER reads "Your own first name"; in the myself branch the builder could prefill the buyer name on step 4 from step 1.

10. MICRO under the email says "occasional notes from Sanctoria" because a non-buyer sequence is planned. Change to "Used only to send the song." only if that sequence is dropped.

11. The checkout button is 20 characters. Delivery wording is "within 24 hours" throughout. No line claims a person writes or reads the answers.

12. Revision of 2026-10-05, to move the form away from the reference site. Step 1 heading, sub and labels rewritten; pronunciation split into its own optional field; the email and buyer name labels reworded; a four name step tracker added (STEP_NAMES); NEXT is now one full width button and BACK a text link. COMPLETE is kept for the parser but is no longer shown. The step 3 labels and the step 4 heading were checked against the reference wording and left as they were, since none of them echoes it.

13. 2026-10-07: one or two names. TS decided a song may carry one or two first names, never more. Step 1 gains a second fold-away link under the pronunciation one, opening a box for a second first name and a dropdown for who that second person is.
   New keys in the basics step: LABEL_NAME2 (7 words with "(optional)"; the link the form builds from it reads "+ A second name to be sung"), PLACEHOLDER_NAME2 (3 words), LABEL_WHO2 (5 words), OPTION_WHO2_BLANK (2 words), TIP_NAME2 (15 words). TIP_NAME2 says both names "will be sung in the song" and does not say "in every chorus", because the song structure in the bible gives the chorus "the name, twice" and it is not yet proven that two names both fit every chorus. Tighten it only after a two name render passes.
   New key in the send step: SUMMARY_LINE_TWO, used when two names are given. It uses {name}, {intention_phrase} and {style_phrase} only, and reads "For Daniel and Mary, both by name. A prayer for peace, sung as a traditional hymn."
   Changed lines, with the old wording to restore:
   H (basics): One person, by name
   SUB (basics): Each prayer song carries a single name. Whose will this one be?
   STEP_NAMES: Person | Prayer | Sound | Send
   The new H is 15 characters (note 1 gave 19 for the old one). "Person" became "Who" in the step tracker because the step can now hold two people; if the tracker looks unbalanced with a three letter first label, "Person" can go back without harm.
   Checked and left alone: in this file {name} is never the subject of a verb. "The prayer for {name}" (prayer H), "The prayer song for {name} is sent" (send SUB, where the song is the subject) and "For {name}." (SUMMARY_LINE) all read correctly with "Daniel and Mary". "Choose the one intention the song will carry" still holds: two names share one intention. LABEL_NAME, TIP, ERROR and the pronunciation lines speak of the first name box and stay singular on purpose.
   SUMMARY_LINE in this file has no {who} token ("For {name}. A prayer for {intention_phrase}, sung as {style_phrase}."). If the built form adds {who} itself, nothing here needs to change; if the string in the build differs from this file, the file should be brought into line.
   Open points for the build: the pronunciation box covers only the first name, so a second name that is not said as spelled has no field (see the report to TS). The Myself and Someone who has passed branches need a rule for whether the second name link is shown.
