## STEP: open
BOT: Let us begin. Three short questions, and then where to send it.

## STEP: who
BOT: Who is this prayer song for?
OPTION: My husband | husband
OPTION: My wife | wife
OPTION: My son | son
OPTION: My daughter | daughter
OPTION: A grandchild | grandchild
OPTION: My mother | mother
OPTION: My father | father
OPTION: A friend | friend
OPTION: Myself | myself
OPTION: Someone who has passed | passed

## STEP: name
BOT: What first name should we sing for {who}?
PLACEHOLDER: First name
BUTTON: Continue
BOT_AFTER: {name}. Thank you. That name will be sung in every chorus.
BOT: Some names are said differently than they are spelled. If {name} is one of them, type how it sounds.
PLACEHOLDER: Sounds like (optional)
BUTTON: Continue
SKIP: It is said as it is spelled

## STEP: intention
BOT: And what is the prayer for {name}?
OPTION: Healing | healing
OPTION: Protection | protection
OPTION: Strength for what is ahead | strength
OPTION: Peace | peace
OPTION: A return to the faith | return
OPTION: A marriage | marriage
OPTION: Comfort in grief | grief
OPTION: Thanksgiving | thanksgiving

## STEP: email
BOT: A prayer for {intention_phrase}, with {name} named in every chorus. That is everything we need.
BOT: Where should we send {name}'s prayer song?
PLACEHOLDER: Email address
BUTTON: Send It Here
MICRO: Used to send the song and occasional notes from Sanctoria. Unsubscribe any time.
ERROR: That address did not go through. It may be a small typo.

## STEP: handoff
BOT: Thank you. The last step is the secure checkout: $37, one time.
BOT: {name}'s prayer song arrives by email within 24 hours, with a 60 day full refund behind it.
BUTTON: Continue To Checkout
MICRO: Secure checkout through ClickBank. No subscription.

## PHRASES
healing: healing
protection: protection
strength: strength
peace: peace
return: a return to the faith
marriage: grace in marriage
grief: comfort in grief
thanksgiving: thanksgiving
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

=== NOTES ===

1. Message count. One opening message, then the first question. She reaches her first tap after two bot bubbles. If the landing page button already says "Begin My Prayer Song", the open line can be dropped entirely and the chat can start on "Who is this prayer song for?".

2. The {who} sentence. "What first name should we sing for {who}?" was written so every relationship phrase reads naturally, including the two awkward ones: "for yourself" and "for the one you are remembering". Do not change the sentence to a possessive form ("your son's first name") without rewriting those two phrases.

3. Reflecting her answers back. The chat repeats only what she has just tapped or typed ("your son", the name, the intention). It never adds a condition she did not give (no "your sick husband", no "you are grieving"). This is a site chat, not ad copy, but it is kept inside the personal attributes rule anyway.

4. The "passed" branch. The builder shows only grief, peace and thanksgiving. The intention question and the option labels read correctly as written. The reflection line ("A prayer for peace, with Margaret named in every chorus") also works. If the builder can swap phrases for this branch, these memorial versions read better:
   peace: eternal rest and peace
   grief: comfort for those who miss them
   thanksgiving: thanksgiving for a life
   They are listed here and not under PHRASES so the parser does not see duplicate keys.

5. The spec sentence "a prayer for {intention_phrase} over {name}" works with every phrase above except in the passed branch with grief ("comfort in grief over Margaret" reads as grief about her, which is acceptable but not ideal). The email step uses "with {name} named in every chorus" to avoid this.

6. The "myself" branch. BOT_AFTER and the email line still work with her own name. "A marriage" is offered for every relationship, including son, daughter and friend, where it means their marriage; the label was kept neutral ("A marriage", not "Our marriage") for that reason. The builder may want to hide "A return to the faith" for the myself branch, since choosing it there is unlikely and slightly odd. Left in by default.

7. "Healing" is a prayer intention only. The chat never asks what the illness is, and the bible lists diagnosis under "never asked". No line implies the song heals.

8. The pronunciation step is optional and has a skip chip, so a common name costs one tap. The placeholder shows no example spelling on purpose: an example name inside the field tends to get submitted by mistake.

9. Email MICRO. It says the address is used for the song and "occasional notes from Sanctoria", because the flow plans a non buyer sequence. If TS decides the address is used for delivery only, change it to "Used only to send the song." Do not promise delivery only while a follow up sequence exists.

10. The handoff button is 20 characters. "Send It Here" is 12.

11. No persona. Nothing in the chat claims a person is typing, reading or writing. "We" is the brand throughout.
