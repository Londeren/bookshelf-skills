# Улов фазы 1 — ACQ Closer Handbook (2025) (ярус 2), тип B: правила и критерии

Группа `tier2-closer`, слаг `closer`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **90** (экстрактор вернул 90, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `acq-closer-handbook.md` | 1–4125 | 5 | 90 |

## Как собран файл

Экстрактор B (Rules and criteria) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-closer.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-closer-B.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 1; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: B-closer-001
  type: rule
  name: >-
    Roleplay until it is right
  statement: >-
    A roleplay repetition is repeated until the rep performs it correctly, however many attempts and however much feedback that takes.
  why: >-
    The rep should be grateful for as many reps as mastery needs; frustration at repetition is the wrong reaction.
  applies_when: >-
    Roleplay training, in onboarding and after it.
  anchor: >-
    He will let you keep trying until you do it right. Expect lots of feedback. Do not get frustrated.
  source: >-
    acq-closer-handbook.md, Onboarding: Schedule & Training, Roleplay, line 690 (repeated verbatim at line 796 in On-Going: Training)
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:690"
- id: B-closer-002
  type: rule
  name: >-
    Three tests before the phones
  statement: >-
    A new rep does not take live prospects until they have passed three skill tests: Tone, Recaps and Objection Looping.
  why: >-
    Once each test is passed the rep starts going live with prospects; the tests are the gate, not the calendar.
  applies_when: >-
    Onboarding, before the first live call (ACQ, 2025).
  anchor: >-
    Before you start on the phones, you must pass three skill tests: Tone, Recaps, and Objection Looping.
  source: >-
    acq-closer-handbook.md, Onboarding: Schedule & Training, Tests, line 693
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:693"
- id: B-closer-003
  type: rule
  name: >-
    Gametape is sold along with, not watched
  statement: >-
    Call recordings are studied with the script in hand, selling along with the salesman out loud, pausing and rewatching the hard parts until they are nailed.
  why: >-
    Watching only collects the words; the results come from roleplaying the recording rather than listening to it.
  applies_when: >-
    Gametape review, on your own or with the team.
  anchor: >-
    Have your script with you and sell along with the salesman. This is not about just getting the words. To maximize the results, you must also roleplay it.
  source: >-
    acq-closer-handbook.md, Onboarding: Schedule & Training, Gametape, line 697
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:697"
- id: B-closer-004
  type: rule
  name: >-
    Call notes the night before and the morning of
  statement: >-
    Call notes for every scheduled call are updated and reviewed the night before and again the morning of the call.
  why: >-
    Knowing the prospect tells you which offer fits them and lets you prepare for their objections ahead of time, which raises conversion.
  applies_when: >-
    Every prospect with a booked close call.
  anchor: >-
    You will update and review call notes the night before and the morning of your calls. So get to the office early to update and review.
  source: >-
    acq-closer-handbook.md, Hunt Mode, #1 Call Notes, line 1240
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1240"
- id: B-closer-005
  type: rule
  name: >-
    Work the list in order of likelihood to buy
  statement: >-
    Prospects are worked in the order they are most likely to buy: Inbound Sets first, then BAMFAMs, then Pipeline.
  why: >-
    Any hour not spent on a close call is spent getting prospects onto close calls, so the order of the list decides the yield of the day.
  applies_when: >-
    Every hour of Hunt Mode that is not a live call.
  anchor: >-
    You work the prospects in the order they are most likely to buy. To make it simple, we split them into three groups.
  source: >-
    acq-closer-handbook.md, Hunt Mode, #2 Work Your List, line 1289
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1289"
- id: B-closer-006
  type: rule
  name: >-
    Call an inbound set immediately
  statement: >-
    A prospect who has just booked an appointment is called immediately on the notification, before anything else on the list.
  why: >-
    Inbound Sets are the newest, freshest and therefore highest value appointments; they have booked but not yet spoken to a closer.
  applies_when: >-
    An inbound booking notification arrives while you are not on a live call.
  anchor: >-
    If you get an inbound notification, call them immediately.
  source: >-
    acq-closer-handbook.md, Hunt Mode, Priority 1: Inbound Sets, line 1291
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1291"
- id: B-closer-007
  type: rule
  name: >-
    Pull the close call forward
  statement: >-
    On contact with an inbound set the objective is to pull the close call forward to right now, and failing that to later the same day.
  why: >-
    The appointment is at its most valuable before the prospect cools; same-day is the fallback, not a later date.
  applies_when: >-
    Working an Inbound Set that already has a future appointment.
  anchor: >-
    Your objective is to pull the close call forward. Ideally, to *right now*. And if not now, then later that day.
  source: >-
    acq-closer-handbook.md, Hunt Mode, Priority 1: Inbound Sets, line 1293
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1293"
- id: B-closer-008
  type: rule
  name: >-
    Double dial before you text
  statement: >-
    Every text to a prospect or customer is preceded by a double dial; texting is what you do after the call did not connect.
  why: >-
    A live conversation beats a text thread, so the phone attempt always comes first.
  applies_when: >-
    Inbound Sets, Pipeline prospects, referral outreach and opt-in outbound.
  anchor: >-
    Use the Inbound Set Phone Script and Inbound Set Text Script when working Inbound Set prospects. *Remember to double dial before you text.*
  source: >-
    acq-closer-handbook.md, Hunt Mode, Priority 1: Inbound Sets, line 1295
  confirmations: 4
  anchor_at: "acq-closer-handbook.md:1295"
- id: B-closer-009
  type: rule
  name: >-
    BAMFAM prospects are kept engaged to the call
  statement: >-
    A prospect who has a second close call booked is worked with the aim of keeping them engaged so that they show up, not of selling them over text.
  why: >-
    They have already spoken to a closer and have not bought; the value of the BAMFAM is the appointment being kept.
  applies_when: >-
    Priority 2 of the list: prospects with a booked follow-up close call.
  anchor: >-
    Your objective is to keep them engaged to make sure they show up to their close call.
  source: >-
    acq-closer-handbook.md, Hunt Mode, Priority 2: BAMFAMs, line 1302
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1302"
- id: B-closer-010
  type: rule
  name: >-
    Pipeline: newest to oldest, back 60 days
  statement: >-
    Prospects who declined or no-showed and have not opted out are contacted from newest to oldest, starting with today's, and going back no further than 60 days.
  why: >-
    The newest declines and no-shows are the likeliest to convert, and 60 days bounds how far back the pipeline is worth working.
  applies_when: >-
    Priority 3 of the list, for anyone you still have permission to call (ACQ, 2025).
  anchor: >-
    You will continue going "back in time," until you've contacted everyone who declined or no-showed in the past 60 days.
  source: >-
    acq-closer-handbook.md, Hunt Mode, Priority 3: Pipeline, line 1308
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1308"
- id: B-closer-011
  type: rule
  name: >-
    Texting starts after the Inbound Sets
  statement: >-
    Text outreach begins only once the Inbound Sets have been worked.
  applies_when: >-
    The texting block of a Hunt Mode day.
  anchor: >-
    Begin texting after you finish your Inbound Sets.
  source: >-
    acq-closer-handbook.md, Hunt Mode, Texting Guidelines, line 1339
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1339"
- id: B-closer-012
  type: rule
  name: >-
    A text back is answered with a call
  statement: >-
    When a prospect texts back, they are called immediately rather than answered by text.
  why: >-
    The point of the text is to get a conversation; if they do not pick up you text them back.
  applies_when: >-
    Any inbound text from a prospect during the day.
  anchor: >-
    When they text back, call them immediately.
  source: >-
    acq-closer-handbook.md, Hunt Mode, Texting Guidelines, line 1340
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1340"
- id: B-closer-013
  type: rule
  name: >-
    Objections over text are answered with an appointment
  statement: >-
    An objection raised over text is handled by setting an appointment, not by typing out paragraphs of argument.
  applies_when: >-
    Text threads with prospects during Hunt Mode.
  anchor: >-
    Handle objections over text by setting appts rather than typing out paragraphs.
  source: >-
    acq-closer-handbook.md, Hunt Mode, Texting Guidelines, line 1342
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1342"
- id: B-closer-014
  type: rule
  name: >-
    Team training is sacred
  statement: >-
    No call is scheduled over a training block, and the only thing that may run into it is an existing close call that has run long.
  why: >-
    Closing a call already in progress takes priority; nothing else does.
  applies_when: >-
    Scheduling calls around daily and weekly team training.
  anchor: >-
    You may not schedule calls during training. But, if an existing close call runs long, closing it takes priority. This is the only exception.
  source: >-
    acq-closer-handbook.md, Hunt Mode, Team Training is Sacred, line 1345
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1345"
- id: B-closer-015
  type: rule
  name: >-
    Non-response clock on an inbound set
  statement: >-
    A booked prospect who does not answer the first text block gets a non-response message at 12 hours and another at 24 hours, and the appointment is cancelled if nothing has come back 12 hours before the call.
  why: >-
    The cadence keeps prospects from slipping through the cracks and frees the slot before the call time is wasted.
  applies_when: >-
    Texting Inbound Sets between the booking and the call (ACQ, 2025).
  anchor: >-
    If no response after 12 hours → Non-Response 1
  source: >-
    acq-closer-handbook.md, Hunt Mode, Working Inbound Sets: The Full Process, lines 1377-1379
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1377"
- id: B-closer-016
  type: rule
  name: >-
    Two replies and a typing bubble means call
  statement: >-
    An ongoing text conversation is converted to a phone call after one or two replies, especially when the prospect is visibly typing.
  why: >-
    Either they pick up and you can close, pull forward or confirm them, or they say they cannot talk and the thread continues; always go for the phone call if you can.
  applies_when: >-
    Any live text exchange with a prospect.
  anchor: >-
    If you get into an ongoing text conversation with a prospect, after 1–2 replies, and a “…” on their side, call them.
  source: >-
    acq-closer-handbook.md, Hunt Mode, Working Inbound Sets: The Full Process, line 1388
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1388"
- id: B-closer-017
  type: rule
  name: >-
    Pickup Primetime
  statement: >-
    At Pickup Primetime everything except a live call is dropped for two hours of outbound.
  why: >-
    Pickup Primetime falls at the end of the day because that is when pick up rates are highest, which maximizes the return on that time.
  applies_when: >-
    The end-of-day outbound block (ACQ, 2025).
  anchor: >-
    When Pickup Primetime occurs, you drop everything (except for a live call) to do outbound for the next two hours.
  source: >-
    acq-closer-handbook.md, Hunt Mode, #3 Outbound, line 1399
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1399"
- id: B-closer-018
  type: rule
  name: >-
    Two triggers for a referral reach-out
  statement: >-
    A customer is called back for referrals in two cases: you closed them but ran out of time to ask, and anyone who sends you a nice text out of the blue.
  applies_when: >-
    Outbound Priority 1.
  anchor: >-
    You'll reach back out to customers for referrals when: 1) You closed a prospect but ran out of time to ask for a referral.
  source: >-
    acq-closer-handbook.md, Hunt Mode, Outbound Priority 1: Getting Referrals, line 1401
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1401"
- id: B-closer-019
  type: rule
  name: >-
    Compliment, then ask for people like them
  statement: >-
    A referral ask double-dials and texts a current or previous customer, pays them a compliment, and asks for other people like them.
  why: >-
    Referrals are the best leads you can get; doing this should net an extra deal a day.
  applies_when: >-
    Outbound Priority 1, with the Referral Script.
  anchor: >-
    To get the referrals, double-dial and text current or previous customers, pay them a compliment, and ask for other people like them.
  source: >-
    acq-closer-handbook.md, Hunt Mode, Outbound Priority 1: Getting Referrals, line 1403
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1403"
- id: B-closer-020
  type: rule
  name: >-
    Opt-ins newest to oldest
  statement: >-
    The remainder of the outbound block double dials and texts unscheduled leads who opted into the marketing list, from newest to oldest.
  applies_when: >-
    Outbound Priority 2, after referrals.
  anchor: >-
    With the remainder of your outbound block, you double dial and text unscheduled leads who opted into our marketing list—from newest to oldest.
  source: >-
    acq-closer-handbook.md, Hunt Mode, Outbound Priority 2: Opt-Ins, line 1405
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1405"
- id: B-closer-021
  type: rule
  name: >-
    Two hours of outbound is the floor
  statement: >-
    Every hour left over after the list is worked goes to setting your own appointments, and two hours of outbound is the minimum, not the target.
  why: >-
    Closers who do more outbound get more deals; opt-in calling should produce about two sets per hour, and four sets should yield at least one close.
  applies_when: >-
    Any day with availability after the priority list (ACQ, 2025).
  anchor: >-
    Any availability you have after working your list is dedicated to setting your own appointments. The two hour block is the minimum.
  source: >-
    acq-closer-handbook.md, Hunt Mode, #3 Outbound, line 1409
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1409"
- id: B-closer-022
  type: rule
  name: >-
    Record every call outcome
  statement: >-
    At the end of the day every call is marked in the CRM as Closed, BAMFAM, Pipeline or Opt-Out.
  why: >-
    The marking is what sorts tomorrow's leads by priority for you.
  applies_when: >-
    The End of Day Checklist.
  anchor: >-
    Mark the outcome in the CRM. Mark them as Closed, BAMFAM, Pipeline, and Opt-Out.
  source: >-
    acq-closer-handbook.md, Hunt Mode, #4 End of Day Checklist, line 1420
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1420"
- id: B-closer-023
  type: rule
  name: >-
    Every lead is opted in until they opt out
  statement: >-
    A lead stays on the list until they ask not to be contacted, and when they do ask they are opted out the same day.
  applies_when: >-
    The End of Day Checklist, on any explicit request to stop contact.
  anchor: >-
    Then opt them out of the list. Every lead is opted in until they opt out. But if they opt out, make sure to opt them out.
  source: >-
    acq-closer-handbook.md, Hunt Mode, #4 End of Day Checklist, line 1422
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1422"
- id: B-closer-024
  type: rule
  name: >-
    Submit your worst call for review
  statement: >-
    Each day the rep submits the call they had the most trouble with for review, which is five calls per week.
  why: >-
    The manager uses it for team training and 1-on-1s, and reviewing it yourself makes you better faster.
  applies_when: >-
    The End of Day Checklist, every day on the phones.
  anchor: >-
    This is the call you had the most trouble with that day. Your manager will use it for team training and 1-on-1 sessions.
  source: >-
    acq-closer-handbook.md, Hunt Mode, #4 End of Day Checklist, line 1423
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1423"
- id: B-closer-025
  type: rule
  name: >-
    Inbox zero across channels
  statement: >-
    The day ends with every lead message on every channel answered, each with the script that fits that lead.
  applies_when: >-
    The End of Day Checklist.
  anchor: >-
    Respond to all lead messages across all channels that built up during the day. Use the right script for each lead.
  source: >-
    acq-closer-handbook.md, Hunt Mode, #4 End of Day Checklist, line 1424
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1424"
- id: B-closer-026
  type: rule
  name: >-
    Breathe the script
  statement: >-
    The script is rehearsed until it is delivered as naturally as breathing; short of dreaming the script, it has not been rehearsed enough.
  why: >-
    A rep who cannot remember what to say, has to look for it, or reads it, is not paying attention to the prospect, and then says the wrong stuff and does not close.
  applies_when: >-
    Every script the rep uses on the phone.
  anchor: >-
    Until you have dreams of saying the script, you have not done it enough times.
  source: >-
    acq-closer-handbook.md, Breathe the Script, line 1501
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1501"
- id: B-closer-027
  type: rule
  name: >-
    Word-for-word, not "similar words in about the same order"
  statement: >-
    The script is delivered word-for-word and naturally, with no personal spin, paraphrase or improvised reordering.
  why: >-
    More sales are lost from people putting their own spin on things than from the script itself; the wording came from more calls than one closer could have in a lifetime.
  applies_when: >-
    Every call, at every level of seniority.
  anchor: >-
    You need to deliver the script word-for-word, with your eyes closed, *naturally*. More sales are lost from people putting their own spin on things.
  source: >-
    acq-closer-handbook.md, Breathe the Script, Important Note, line 1522
  confirmations: 3
  authors_caveat: >-
    The scripts in the appendix sometimes appear to bend the rules of the handbook because the missing variables are covered elsewhere in the process or by the brand.
  anchor_at: "acq-closer-handbook.md:1522"
- id: B-closer-028
  type: rule
  name: >-
    150-170 words per minute
  statement: >-
    Speaking speed on a call stays in the range of about 150 to 170 words per minute, a little slower than normal conversation.
  why: >-
    Too fast and the prospect cannot track you or senses your stress; too slow and you sound drunk; the range is easy to measure as an average and leaves room for natural shifts.
  applies_when: >-
    Every phone call.
  anchor: >-
    The ideal range is about 150–170 words per minute.
  source: >-
    acq-closer-handbook.md, Tone, Talk Slower (Speed), line 1571
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1571"
- id: B-closer-029
  type: rule
  name: >-
    The prospect does four fifths of the talking
  statement: >-
    On a call that goes perfectly the closer talks about a fifth of the time, roughly three minutes of a fifteen-minute close.
  why: >-
    At 150-170 words per minute a 500-word script takes just over three minutes, so more talking than that means you are talking too much.
  applies_when: >-
    Reviewing your own call length and talk ratio.
  anchor: >-
    if a call goes perfect on your side and takes 15 minutes to close, then the prospect spoke for 12 minutes and you spoke for three.
  source: >-
    acq-closer-handbook.md, Tone, Talk Slower (Speed), line 1573
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1573"
- id: B-closer-030
  type: rule
  name: >-
    Slower, louder, clearer never change
  statement: >-
    Speed, volume and enunciation stay constant for the whole call: slow enough to track, loud enough to hear, clear enough to understand.
  why: >-
    These are the basics that win games, and clear beats clever every time; a prospect who cannot hear or follow you will not buy.
  applies_when: >-
    Every call, including the close and the loops.
  anchor: >-
    You are a more effective closer when you: *slow down enough* so prospects can track what you say
  source: >-
    acq-closer-handbook.md, Tone, Bottom Line, line 1600
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1600"
- id: B-closer-031
  type: rule
  name: >-
    A question mark means pitch up
  statement: >-
    Wherever the script prints a question mark, the pitch rises at the end of that word, whatever position it holds in the sentence.
  why: >-
    A group of words does not become a question by itself; the rising pitch is what signals that you asked for information, and packs many words into one.
  applies_when: >-
    Every script that uses the (?) notation.
  anchor: >-
    So when you see question marks (?) in the script then say that word, no matter where it is, *as if you are asking a question.*
  source: >-
    acq-closer-handbook.md, Tone, Getting Prospects to Talk (Pitch), line 1617
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1617"
- id: B-closer-032
  type: rule
  name: >-
    The longest pause goes after the buying question
  statement: >-
    After asking for the sale the closer stays silent, giving the buying question the longest pause of the call, eight seconds or more.
  why: >-
    Five mega studies showed a 23 to 40% increase in close rates from pausing 8+ seconds after asking for the sale; if the prospect is not forced to address the buying question head on, they will avoid it.
  applies_when: >-
    Every ask for the sale, and every re-ask inside a loop.
  anchor: >-
    Five mega studies by Harvard, UCLA, and other fancy places showed a 23 to 40% increase in close rates by pausing for 8+ seconds after asking for the sale.
  source: >-
    acq-closer-handbook.md, Tone, When You Don't Talk (Pauses), lines 1667-1712
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1667"
- id: B-closer-033
  type: rule
  name: >-
    Pauses and pitch only where the script says
  statement: >-
    Pitch is raised only to ask a question and a pause is inserted only where the script marks one, with the three marked lengths short (...), medium (.) and long (—).
  why: >-
    A pause focuses attention on what was just said, so an unplanned pause gives the wrong words the most important job; a forgotten line creates exactly that pause.
  applies_when: >-
    Delivering any ACQ script.
  anchor: >-
    And you only need to raise your pitch to ask a question, or insert a pause to focus attention—when the script tells you to.
  source: >-
    acq-closer-handbook.md, Tone, Bottom Line, line 1712
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1712"
- id: B-closer-034
  type: rule
  name: >-
    Do not train to sound natural
  statement: >-
    Naturalness is reached by knowing the script well enough that it becomes natural, never by practising an imitation of natural speech.
  why: >-
    Training to speak naturally is training to pretend; if you do not want to sound like you are reading a script, do not read a script.
  applies_when: >-
    Tone practice and roleplay.
  anchor: >-
    Instead of pretending to speak naturally, know the script so well it becomes natural.
  source: >-
    acq-closer-handbook.md, Tone, Advanced Tone Tactics, line 1710
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1710"
- id: B-closer-035
  type: rule
  name: >-
    The four things every call opens with
  statement: >-
    Every call opens with the rep's name, the company they call from, the fact that the call is recorded, and the reason for the call.
  why: >-
    Leaving any of the four out breaks the law; every large public company opens this way and it sounds like a legitimate business.
  applies_when: >-
    The first 30-60 seconds of every call, inbound and outbound (US, 2025).
  anchor: >-
    You start every call with those four things because, if you don’t—you break the law. So if you want to work at ACQ, you will follow the law.
  source: >-
    acq-closer-handbook.md, Introduction, lines 1737-1746
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1746"
- id: B-closer-036
  type: rule
  name: >-
    State the agenda after the big four
  statement: >-
    Once the four required elements are confirmed, the closer states the agenda for the call: why they opted in, what will be covered, and that at the end you will see if it makes sense to move forward.
  applies_when: >-
    Immediately after the opening of a close call.
  anchor: >-
    Then, after you get confirmation of the big four required by law, you state the agenda for the call.
  source: >-
    acq-closer-handbook.md, Introduction, line 1777
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1777"
- id: B-closer-037
  type: rule
  name: >-
    Minimum questions, minimum words
  statement: >-
    The introduction contains only the required questions in the fewest possible words, delivered in the proper tone, and no small talk, pitch or filler.
  why: >-
    The minutes wasted at the beginning are the minutes you will wish for at the end, and a long intro can cost the sale and the referral that would have come with it.
  applies_when: >-
    The opening of every close call.
  anchor: >-
    The intro is a place to ask the minimum required questions, with the minimum required words, delivered in the proper tone.
  source: >-
    acq-closer-handbook.md, Introduction, line 1812
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1812"
- id: B-closer-038
  type: rule
  name: >-
    Establish current and desired before any pain
  statement: >-
    Before the Pain Cycle begins, the call establishes where the prospect is now and where they want to be; this step takes about a minute and is never skipped.
  why: >-
    If you do not know where someone wants to go you cannot give them directions, and there is no gap to work with.
  applies_when: >-
    Steps 1-2 of Discovery, on every close call.
  anchor: >-
    This typically only takes a minute but you cannot skip it. If you don't know where someone wants to go, how can you expect to give them directions?
  source: >-
    acq-closer-handbook.md, Discovery, Steps 1-2: Current and Desired, line 1863
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1863"
- id: B-closer-039
  type: rule
  name: >-
    Collect as many reasons as they will give
  statement: >-
    The obstacle step asks why they do not have the results they want, and keeps collecting reasons rather than stopping at the first one.
  why: >-
    Every reason they cannot get results is another reason for them to buy.
  applies_when: >-
    Step 3 of Discovery.
  anchor: >-
    We discover the prospect's problems by getting them to answer one question: "Why don't you have the results you want?" And the more reasons they give us, the better.
  source: >-
    acq-closer-handbook.md, Discovery, Step 3: Obstacle, line 1872
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1872"
- id: B-closer-040
  type: rule
  name: >-
    Only ask about results you can deliver
  statement: >-
    Discovery asks the prospect only about results in areas where the offer can produce good results, and moves to another area when the problem found is not big enough.
  why: >-
    Only problems you can solve are worth surfacing; every good result you offer becomes a result of theirs you can ask about.
  applies_when: >-
    Choosing which problems to open in Discovery.
  anchor: >-
    We only care about problems we can solve. This means one simple thing: we only ask the prospect about results in areas we can get good results.
  source: >-
    acq-closer-handbook.md, Discovery, Step 3: Obstacle, line 1881
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1881"
- id: B-closer-041
  type: rule
  name: >-
    Pull Teeth: tell me more, then give me an example
  statement: >-
    A vague, confusing or incomplete answer is met with the same two moves in the same order: ask them to tell you more, then ask for an example.
  why: >-
    Asking for more usually does the job, and asking for an example makes them connect the problem to a lived experience; the aim is only more information and a mapping to the solution.
  applies_when: >-
    Step 5 of Discovery, and any point in looping where you are unsure how to respond.
  anchor: >-
    You'll note, no matter the type of bad answer, *you respond the same way*. You ask them to tell you more, and then you ask them to give an example.
  source: >-
    acq-closer-handbook.md, Discovery, Step 5: Pull Teeth, line 1907
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1907"
- id: B-closer-042
  type: rule
  name: >-
    Recap in their words, label in ours, confirm
  statement: >-
    Every problem surfaced is repeated back in the prospect's own words, labelled in one of the five categories of the offer, and confirmed as correct with the prospect.
  why: >-
    The label is what gets mapped to the solution and benefits in the offer, so it has to be right before the offer is built on it.
  applies_when: >-
    Steps 6-8 of Discovery, after each Pain Cycle.
  anchor: >-
    Using this setup is important because every problem they have can and should be mapped to a solution we offer. Once you label it, just make sure you got it right.
  source: >-
    acq-closer-handbook.md, Discovery, Steps 6-8: Recap, Label, & Confirm, line 1942
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1942"
- id: B-closer-043
  type: rule
  name: >-
    When Discovery is allowed to end
  statement: >-
    Discovery ends only once you hold either one label built from several related problems or several labels from several different problems, all stated in the prospect's own words and mapped to your solution categories.
  why: >-
    Ideally one Pain Cycle is enough, but the cycle repeats until there are enough problems you can solve; have a list of results to ask about ready.
  applies_when: >-
    Step 9 of Discovery, deciding whether to cycle again or move to the offer.
  anchor: >-
    Once we have one label from multiple related problems, or multiple labels from multiple different problems, we have what we need to move on.
  source: >-
    acq-closer-handbook.md, Discovery, Step 9: Repeat Until Complete, lines 1950-1970
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1950"
- id: B-closer-044
  type: rule
  name: >-
    Stack the pain before the offer
  statement: >-
    Before any offer is made, all the recaps from all the Pain Cycles are said again together as one final recap and confirmed with the prospect.
  why: >-
    It is only sharing back what you learned and making sure they agree, and their agreement is what the offer is then built on.
  applies_when: >-
    The transition from Discovery to Offer.
  anchor: >-
    Once you’ve completed your Pain Cycles, you need to stack the pain. To stack the pain, get your Recaps together and say them all again.
  source: >-
    acq-closer-handbook.md, Discovery, Final Recap (Stacking the Pain), line 1958
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1958"
- id: B-closer-045
  type: rule
  name: >-
    Map the problems before asking for money
  statement: >-
    The offer maps every problem raised in discovery to a solution you provide before the price is ever mentioned; it is never a list of benefits followed by an ask.
  why: >-
    Gathering pain points and then abandoning them wastes the discovery; a personalized offer built on the spot from their own words crushes.
  applies_when: >-
    Every offer on a close call.
  anchor: >-
    First, we map all the problems in the discovery phase to solutions we provide—then we ask for money. In other words, we craft a personalized offer on the spot.
  source: >-
    acq-closer-handbook.md, Offer, line 1987
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1987"
- id: B-closer-046
  type: rule
  name: >-
    Two minutes, about 320 words
  statement: >-
    The whole offer is delivered in about two minutes, which at 150-170 words per minute is roughly 320 words.
  why: >-
    That is plenty of words if you know what you are doing; needing more means you are wasting words.
  applies_when: >-
    The offer section of a close call.
  anchor: >-
    Remember, talking between 150–170 words per minute gives you about 320 words to make your offer.
  source: >-
    acq-closer-handbook.md, Offer, lines 1987-1989
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1989"
- id: B-closer-047
  type: rule
  name: >-
    Three solutions, asked for by permission
  statement: >-
    After telling the prospect you think you can help and asking permission to share, exactly three of your solutions are chosen and their problems mapped onto those three.
  applies_when: >-
    The transition from the final recap into the offer.
  anchor: >-
    So choose three of our solutions and map their problems to those.
  source: >-
    acq-closer-handbook.md, Offer, How to Make The Offer, line 1993
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1993"
- id: B-closer-048
  type: rule
  name: >-
    Fit any number of problems to three solutions
  statement: >-
    One problem is broken into micro problems in discovery so that it maps to all three solutions, and more than three problems are grouped so that one solution answers several.
  applies_when: >-
    Building the map step of the offer.
  anchor: >-
    If they have one problem, then map it to all three solutions by breaking it into micro problems in the discovery phase.
  source: >-
    acq-closer-handbook.md, Offer, How to Make The Offer, line 2003
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2003"
- id: B-closer-049
  type: rule
  name: >-
    Stack three times, then ask
  statement: >-
    Every solution-and-benefit pair delivered so far is listed again at each step, three times in all, and only after the third stack and its confirmation is the sale asked for.
  applies_when: >-
    The stack step of the offer.
  anchor: >-
    List all solution and benefit pairs up to this point. You do this three times. After the third time (and confirmation), you ask for the sale.
  source: >-
    acq-closer-handbook.md, Offer, How to Make The Offer, line 2015
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2015"
- id: B-closer-050
  type: rule
  name: >-
    Drop price and stop talking
  statement: >-
    The price is stated last and followed by silence from the closer.
  why: >-
    The buying question demands the most attention, and the pause after it is what forces the prospect to address it; up to 40% of deals are lost by talking through it.
  applies_when: >-
    The final step of the offer.
  anchor: >-
    Then you state the price and shut the fuck up.
  source: >-
    acq-closer-handbook.md, Offer, How to Make The Offer, line 2017
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2017"
- id: B-closer-051
  type: rule
  name: >-
    Plug and chug: nothing invented on the call
  statement: >-
    Labels, solutions, assurances and benefits are written out before the call, so that nothing in the offer is composed live.
  why: >-
    Prospects change but the solutions stay the same; improvising risks saying something dumb, wrecking your tone, or both.
  applies_when: >-
    Preparation for close calls.
  anchor: >-
    With proper preparation you need only to “plug and chug”. You should never have to come up with anything on the fly and risk saying something dumb, screwing up your tone, or both.
  source: >-
    acq-closer-handbook.md, Offer, line 2024
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2024"
- id: B-closer-052
  type: rule
  name: >-
    Collect payment, then ask for the referral
  statement: >-
    When the prospect agrees, payment is collected and the call moves straight into the referral ask.
  applies_when: >-
    Immediately after a yes on a close call.
  anchor: >-
    If the prospect agrees then you closed ‘em. Excellent. Collect payment, move to the referral section, and get their friends on board.
  source: >-
    acq-closer-handbook.md, Offer, line 2065
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:2065"
- id: B-closer-053
  type: rule
  name: >-
    A time objection is a priority objection
  statement: >-
    A time objection is answered by finding lower-value things the prospect spends time on and getting them to agree those are less valuable than what is being offered.
  why: >-
    Not enough time is never an objection, only not a high-enough priority.
  applies_when: >-
    Objection type 1 of 5, Time.
  anchor: >-
    This is solved by finding lower value things they spend time on... and *getting them to agree they're not as valuable as taking the time to do what we're offering*.
  source: >-
    acq-closer-handbook.md, Objections, The 5 Objections to Buying, line 2084
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2084"
- id: B-closer-054
  type: rule
  name: >-
    A money objection is answered with the cost of the problem
  statement: >-
    A money objection is answered by showing what the problem costs compared with what the solution costs.
  why: >-
    Money accounts for roughly half of all objections, so this is the response that gets the most use.
  applies_when: >-
    Objection type 2 of 5, Money (ACQ, 2025).
  anchor: >-
    This is solved by showing how much the problem costs compared to the solution. This accounts for roughly 50% of objections.
  source: >-
    acq-closer-handbook.md, Objections, The 5 Objections to Buying, line 2101
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2101"
- id: B-closer-055
  type: rule
  name: >-
    Decision-maker: find out first, get them on the call
  statement: >-
    A decision-maker objection is worked in three steps: establish ahead of time whether permission is needed and get that person on the call, ask whether they would approve based on past approvals and push for a decision now if they would, and otherwise book a follow-up call with the decision-maker.
  applies_when: >-
    Objection type 3 of 5, Decision-Maker.
  anchor: >-
    First, we figure out if they need permission ahead of time. If so, we get the decision-maker on the call.
  source: >-
    acq-closer-handbook.md, Objections, The 5 Objections to Buying, line 2113
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2113"
- id: B-closer-056
  type: rule
  name: >-
    Preference: consequences, then why it is done this way
  statement: >-
    A preference objection is answered by reminding them of the problem they want solved, drawing out the short-, medium- and long-term consequences of their current way, and explaining why your way serves them better.
  why: >-
    The prospect has to see that changing the variables that create the outcome changes the outcome.
  applies_when: >-
    Objection type 4 of 5, Preference.
  anchor: >-
    Second, we pull out the short-, medium-, and long-term consequences of their current ways. Third, we explain why the way we do it is ultimately to their benefit.
  source: >-
    acq-closer-handbook.md, Objections, The 5 Objections to Buying, line 2130
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2130"
- id: B-closer-057
  type: rule
  name: >-
    Stall: a decision framework plus the cost of waiting
  statement: >-
    A stall is answered by walking the prospect through a decision-making framework and then spelling out the cost of waiting, both the good they miss and the bad they keep.
  applies_when: >-
    Objection type 5 of 5, Stall.
  anchor: >-
    To solve this, we walk them through a decision-making framework and then explain the cost of waiting
  source: >-
    acq-closer-handbook.md, Objections, The 5 Objections to Buying, line 2143
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2143"
- id: B-closer-058
  type: rule
  name: >-
    Prepared for all objections all the time
  statement: >-
    The rep prepares responses to all five objection types before every call, because which ones come, how many and in what order cannot be predicted.
  why: >-
    You can guess, but a guess is all it is, and a single slip costs the close.
  applies_when: >-
    Preparation for any close call.
  anchor: >-
    You must be prepared for all objections all the time.
  source: >-
    acq-closer-handbook.md, Objections, Preparing for Objections, line 2168
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2168"
- id: B-closer-059
  type: rule
  name: >-
    An objection is not handled until it loops back to the offer
  statement: >-
    Answering an objection counts as handled only when the prospect has been brought back to the offer and asked to buy again.
  why: >-
    Knowing how to respond to an objection only matters if the prospect buys.
  applies_when: >-
    Every objection on a close call.
  anchor: >-
    Knowing how to respond to an objection only matters if the prospect buys. So to truly handle an objection, you must loop it back to the offer.
  source: >-
    acq-closer-handbook.md, Objections, Preparing for Objections, line 2170
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2170"
- id: B-closer-060
  type: rule
  name: >-
    Address the content, never the objection itself
  statement: >-
    However weak the objection, the closer never insults or challenges the objection and addresses only its content.
  why: >-
    A prospect made to feel stupid, cornered or caught out acquires a better objection, that the closer is an asshole, and calls off the deal.
  applies_when: >-
    Every loop, with tone tightly controlled.
  anchor: >-
    no matter how silly the objection, you must *never ever* insult the objection itself. You will *only address its content*.
  source: >-
    acq-closer-handbook.md, Looping, The Right Way to Handle Objections, line 2252
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:2252"
- id: B-closer-061
  type: rule
  name: >-
    Agree and add, never contradict
  statement: >-
    Each loop carefully agrees with the prospect and adds a line of reasoning to theirs rather than contradicting it.
  why: >-
    The salespeople who ask for the buy the most times get the most closes, and only agreeable interactions buy you more chances to ask.
  applies_when: >-
    Every objection, whatever its content.
  anchor: >-
    So, we have to carefully agree with the prospect and add to their thinking rather than contradict it.
  source: >-
    acq-closer-handbook.md, Looping, The Right Way to Handle Objections, line 2260
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:2260"
- id: B-closer-062
  type: rule
  name: >-
    Ignore the first objection and confirm value
  statement: >-
    The first objection is not answered; the closer first asks whether the prospect believes the product would get them closer to their goal.
  why: >-
    Before playing objection whack-a-mole you have to know whether they think the product is valuable at all.
  applies_when: >-
    The first objection after the ask, before any loop.
  anchor: >-
    Before getting into objection whack-a-mole, we need to know something very important: Do they think our product is valuable?
  source: >-
    acq-closer-handbook.md, Looping, Handling the First Objection, line 2270
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2270"
- id: B-closer-063
  type: rule
  name: >-
    Triage question after confirming value
  statement: >-
    Whatever the answer to the value question, it is followed by a triage question asking for the single biggest thing holding them back.
  why: >-
    It makes them abandon the reflex objection, which isolates the objection actually worth handling.
  applies_when: >-
    Immediately after confirming value, before the first loop.
  anchor: >-
    And no matter what they say you follow up with → a triage question. The main objective is to get them to abandon their “reflex” objection.
  source: >-
    acq-closer-handbook.md, Looping, Handling the First Objection, line 2282
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2282"
- id: B-closer-064
  type: rule
  name: >-
    Every loop ends in an ask
  statement: >-
    Each loop acknowledges, addresses, and then asks for the sale again immediately; a loop that does not end in an ask is incomplete.
  applies_when: >-
    Every objection from the second one onward.
  anchor: >-
    Also, remember that the loop includes asking for the sale.
  source: >-
    acq-closer-handbook.md, Looping, The Second Objection and Beyond, line 2316
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:2316"
- id: B-closer-065
  type: rule
  name: >-
    Loop until they buy or time runs out
  statement: >-
    Looping continues until one of exactly two things happens: the prospect buys, or the call runs out of time.
  why: >-
    They will eventually run out of objections and you will never run out of loops, so every successful loop moves you closer to the close.
  applies_when: >-
    Any close call that reaches objections.
  anchor: >-
    This means you keep looping until one of two things happen. They buy or you run out of time.
  source: >-
    acq-closer-handbook.md, Looping, The Second Objection and Beyond, line 2316
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2316"
- id: B-closer-066
  type: rule
  name: >-
    "And," never "But"
  statement: >-
    The acknowledgement is joined to your addition with "and"; the word "but" never appears.
  why: >-
    "But" works like a big fat eraser telling the prospect to ignore everything before it, which disrespects them and costs the sale.
  applies_when: >-
    Every acknowledge step of every loop.
  anchor: >-
    “And,” never “But”. Think of “But” like a big fat eraser. It means ignore all the words before it.
  source: >-
    acq-closer-handbook.md, Looping, line 2369
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2369"
- id: B-closer-067
  type: rule
  name: >-
    On a yes, tell them what to do
  statement: >-
    As soon as the prospect agrees, the closer gives a command that assumes the close rather than asking another question.
  why: >-
    A command assumes the close and moves the conversation directly to it.
  applies_when: >-
    The moment of agreement inside or after a loop.
  anchor: >-
    someone tells you they agree, *tell them what to do.* This assumes the close and moves the conversation directly to the close.
  source: >-
    acq-closer-handbook.md, Looping, line 2403
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2403"
- id: B-closer-068
  type: rule
  name: >-
    Heavy looping is a symptom, not a skill
  statement: >-
    A call that needs many loops is read as a failure earlier in the script, not as good closing; the great majority of sales close on the first and second ask.
  applies_when: >-
    Reviewing your own calls and gametape.
  anchor: >-
    If you are looping a lot, it means you are messing up earlier in the script.
  source: >-
    acq-closer-handbook.md, Looping, Helpful Points About Looping, line 2441
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2441"
- id: B-closer-069
  type: rule
  name: >-
    Three-minute buffer before the next call
  statement: >-
    When another call follows immediately, the closer keeps three minutes free and spends them booking a time to finish closing this prospect.
  applies_when: >-
    A loop still running as the next appointment approaches.
  anchor: >-
    If you have a call right after this one, then give yourself a three minute buffer. Use that three minutes to book a time to finish closing them.
  source: >-
    acq-closer-handbook.md, Looping, Helpful Points About Looping, line 2445
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2445"
- id: B-closer-070
  type: rule
  name: >-
    A bad fit found in looping goes into the notes
  statement: >-
    When looping reveals the prospect is actually a bad fit, that is written into the notes and the manager decides whether they stay in the pipeline.
  applies_when: >-
    After a call where the loops exposed a mismatch.
  anchor: >-
    Sometimes looping reveals that the prospect is actually a bad fit. Make sure to add that information to your notes.
  source: >-
    acq-closer-handbook.md, Looping, Helpful Points About Looping, line 2446
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2446"
- id: B-closer-071
  type: rule
  name: >-
    Same tone in the loops as before them
  statement: >-
    Speed, volume, enunciation, pitch and pauses in the close and the loops are indistinguishable from the rest of the call.
  why: >-
    This is where most salespeople fail, changing their tone when the game is on the line; tone matters more here than anywhere else and leaves very little room for error.
  applies_when: >-
    The close and every loop; the part to roleplay most.
  anchor: >-
    The best closers sound exactly the same during loops as they do before.
  source: >-
    acq-closer-handbook.md, Looping, Stay Calm in The Close, line 2447
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2447"
- id: B-closer-072
  type: rule
  name: >-
    Book the next meeting from the meeting
  statement: >-
    A call that does not close ends with the next call booked while still on this call, with a specific day and time and an invite sent; "we'll follow up offline" is never said.
  why: >-
    You are both there now, and if you will not book a call while on a call, you have no chance of booking one over text afterwards.
  applies_when: >-
    Running out of time, a decision-maker to consult, or a banking delay on a high ticket.
  anchor: >-
    When you start running out of time... You must secure the next call on the current call. Do not say "we'll follow up offline".
  source: >-
    acq-closer-handbook.md, BAMFAM, Time Constraint BAMFAM, lines 2458-2466
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:2466"
- id: B-closer-073
  type: rule
  name: >-
    Ask for referrals right after payment
  statement: >-
    The referral ask comes immediately after the close and the payment details, and is adapted to text only if the call ran out of time.
  applies_when: >-
    Every closed sale.
  anchor: >-
    Right after you close them and collect payment information. If you run out of time on the call, adapt this to text.
  source: >-
    acq-closer-handbook.md, Referrals, line 2500
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:2500"
- id: B-closer-074
  type: rule
  name: >-
    A positive text is a referral cue
  statement: >-
    Any time a customer opens a text thread with something positive, that is treated as the moment to ask for an introduction.
  why: >-
    Customers text after coming to HQ or getting results from something you helped them implement, and they text because they want you to sell them.
  applies_when: >-
    Any unprompted positive message from a customer.
  anchor: >-
    After they start a text thread with you and share anything positive. This is a *very* good time.
  source: >-
    acq-closer-handbook.md, Referrals, line 2501
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2501"
- id: B-closer-075
  type: rule
  name: >-
    Give them the words and the group chat
  statement: >-
    When a customer agrees to introduce someone, they are asked to start a group chat and handed the exact wording to paste.
  applies_when: >-
    Step 3 of the Referral Process, on a yes.
  anchor: >-
    **Give them words to use**: If they say yes, ask them to start a group chat.
  source: >-
    acq-closer-handbook.md, Referrals, Referral Process, line 2509
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:2509"
- id: B-closer-076
  type: rule
  name: >-
    Referrals are the top priority of outbound time
  statement: >-
    Referral work is placed ahead of every other use of outbound time.
  why: >-
    Nothing nets more money per second, it is the least work per sale in the handbook, and over 30% of sales come from it.
  applies_when: >-
    Planning the outbound block (ACQ, 2025).
  anchor: >-
    Nothing will net you more money per second than referrals. It is your *highest* return on time.
  source: >-
    acq-closer-handbook.md, Referrals, Make Referrals Your Top Priority, lines 2520-2524
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:2520"
- id: B-closer-077
  type: rule
  name: >-
    Cash thresholds that keep a set alive
  statement: >-
    When a price objection on a setting call turns out to be budget rather than value, financial questions are asked, and the appointment is set when the prospect has $15K or more cash on hand or $10K a month of cash flow.
  applies_when: >-
    The "too expensive" obstacle on the Outbound Set Phone Script (ACQ, 2025).
  anchor: >-
    IF THEY HAVE $15K+ CASH OR $10K/MO CASH FLOW
  source: >-
    acq-closer-handbook.md, ACQ Outbound Set Phone Script, Obstacles to Book a Meeting, line 2847
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2847"
- id: B-closer-078
  type: rule
  name: >-
    Name the constraint from a closed list
  statement: >-
    A prospect who cannot name their constraint is given the closed list to choose from: marketing, sales, people, profit or operations.
  why: >-
    A chosen category can be recapped and labelled; an open question leaves nothing to map to a solution.
  applies_when: >-
    Discovery on setting and closing calls when the answer is vague or "I don't know".
  anchor: >-
    Hmm....If you had to say it was one of— marketing, sales, people, profit, or operations... which would it be?
  source: >-
    acq-closer-handbook.md, ACQ Outbound Set Phone Script, "I DON'T KNOW MY CONSTRAINT", line 2857
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:2857"
- id: B-closer-079
  type: rule
  name: >-
    Every booked appointment is manually nurtured
  statement: >-
    Between the set and the call the prospect gets a manual text sequence: an intro, the pre-call video, a night-before message and a morning-of message.
  why: >-
    Manual nurture has raised show rates more than anything the author has seen across the portfolio.
  applies_when: >-
    Every appointment between the set and the close call (ACQ, 2025).
  anchor: >-
    Manual nurture has boosted show rates more than anything I have seen across our portfolio.
  source: >-
    acq-closer-handbook.md, ACQ Outbound Reminder Text Script, Why this is important, line 3064
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3064"
- id: B-closer-080
  type: rule
  name: >-
    International leads move to WhatsApp
  statement: >-
    When the lead is international, the nurture group chat is created on WhatsApp.
  applies_when: >-
    Rules of Engagement for the reminder group chat.
  anchor: >-
    If a lead is international, then use WhatsApp to create the groupchat
  source: >-
    acq-closer-handbook.md, ACQ Outbound Reminder Text Script, Rules of Engagement, line 3071
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3071"
- id: B-closer-081
  type: rule
  name: >-
    A long answer over text is pushed to the call
  statement: >-
    A text question that would need a long answer is not answered in writing; it is carried over to the call, while short questions are answered as soon as possible.
  applies_when: >-
    Text threads with a booked prospect before the call.
  anchor: >-
    If the response requires a long answer, push to the call
  source: >-
    acq-closer-handbook.md, ACQ Inbound Set Text Script, line 3237
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3237"
- id: B-closer-082
  type: rule
  name: >-
    State the length of the call and get permission to start
  statement: >-
    The opening states how long the call will take and asks permission to jump in before anything else happens.
  applies_when: >-
    The introduction of a close call.
  anchor: >-
    We only have 20 min for our call today. Cool if we jump right in?
  source: >-
    acq-closer-handbook.md, ACQ Closing Script, INTRO, line 3257
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3257"
- id: B-closer-083
  type: rule
  name: >-
    An unwatched pre-call video is watched on the call
  statement: >-
    A prospect who did not watch the pre-call video is asked to watch it during the call while the closer goes on mute, rather than being talked through it.
  why: >-
    The five-minute video saves about twenty minutes of the call.
  applies_when: >-
    The introduction, when the prospect confirms they have not seen the video.
  anchor: >-
    that's the video, it's just 5 min and will save us about 20 here today. Do you mind giving that a quick watch, I'll go on mute and we can jump in once you finish?
  source: >-
    acq-closer-handbook.md, ACQ Closing Script, INTRO, line 3268
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3268"
- id: B-closer-084
  type: rule
  name: >-
    No promises or guarantees, said out loud
  statement: >-
    Before discovery begins the closer states that no promise or guarantee of any rate of return or specific result is made and that results will vary.
  why: >-
    The prospect is the one doing the work, not you.
  applies_when: >-
    Every close call, immediately after the agenda (ACQ, 2025).
  anchor: >-
    we make no promises or guarantees of any rate of return or specific result. And that's because you're the one doing the work.
  source: >-
    acq-closer-handbook.md, ACQ Closing Script, INTRO, line 3276
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3276"
- id: B-closer-085
  type: rule
  name: >-
    Money objection: check the funds, then ask or book
  statement: >-
    After a money objection is isolated, the closer asks what cash on hand and card situation looks like; if the funds are there the sale is asked for, and if they are not the next step is a timeline and a BAMFAM.
  applies_when: >-
    Money objections on a close call.
  anchor: >-
    IF they don't → What's the timeline look like for you? BAMFAM
  source: >-
    acq-closer-handbook.md, Money Objections, lines 3629-3631
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3631"
- id: B-closer-086
  type: rule
  name: >-
    More than three days out means value messages
  statement: >-
    When the booked meeting is more than three days away, the gap is filled with value-based messages: a testimonial, a third-party review or a value video.
  applies_when: >-
    Nurturing a BAMFAM booked far out.
  anchor: >-
    Send a value-based message with one of the following:
  source: >-
    acq-closer-handbook.md, ACQ BAMFAM Script, IF BOOKED MORE THAN 3-DAYS, line 3908
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3908"
- id: B-closer-087
  type: rule
  name: >-
    Referral text goes out the day after the sale
  statement: >-
    The referral text is sent the day after someone signs up, both when they agreed to give a referral and when you never got to ask.
  applies_when: >-
    The day after any closed sale.
  anchor: >-
    Day after someone signs up & they agreed to give a referral OR if you did not ask and need to follow up.
  source: >-
    acq-closer-handbook.md, ACQ Referral Text Script, line 3923
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3923"
- id: B-closer-088
  type: rule
  name: >-
    No-show cadence: text now, again at five minutes, then outbound
  statement: >-
    A no-show is double dialled, texted immediately, texted again with two reschedule times if nothing comes back within five minutes, and added to the end-of-day outbound block if there is still no response.
  applies_when: >-
    A prospect who does not pick up at the scheduled time.
  anchor: >-
    Add these to your outbound block at the end of the day if you do not get responses. If they pick up → OUTBOUND SET PHONE SCRIPT
  source: >-
    acq-closer-handbook.md, ACQ No Show Script, lines 3972-3980
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3980"
- id: B-closer-089
  type: rule
  name: >-
    Pipeline work starts with a call and ends with a date
  statement: >-
    A pipeline prospect is called first and texted only if they do not answer, and the contact is finished either with the deal closed or with an agreed time to touch base again.
  applies_when: >-
    Prospects waiting on an off-call obstacle or who have gone quiet.
  anchor: >-
    Start by calling. If they do not answer, transition to text. The goal is to close the deal or agree on a timeline to touch base again.
  source: >-
    acq-closer-handbook.md, ACQ Pipeline Phone & Text Script, line 3994
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3994"
- id: B-closer-090
  type: rule
  name: >-
    Five-minute follow-up after an unclosed call
  statement: >-
    Within five minutes of a call that did not close, a short positive text is sent thanking them and saying you can help.
  why: >-
    The goal is to leave a positive feeling after the conversation.
  applies_when: >-
    Right after the first call with a prospect who did not buy.
  anchor: >-
    Note: This takes place right after this first call you have with them. The goal is to leave a positive feeling post-conversation.
  source: >-
    acq-closer-handbook.md, ACQ Pipeline Phone & Text Script, STEP #0, line 4016
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:4016"
```
