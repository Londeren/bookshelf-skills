# Улов фазы 1 — ACQ Closer Handbook (2025) (ярус 2), тип E: глоссарий

Группа `tier2-closer`, слаг `closer`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **49** (экстрактор вернул 49, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `acq-closer-handbook.md` | 1–4125 | 5 | 49 |

## Как собран файл

Экстрактор E (Glossary) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-closer.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-closer-E.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: E-closer-001
  type: term
  name: >-
    Selling
  statement: >-
    Selling means maximizing the likelihood a prospect buys, nothing more.
  definition: >-
    First, **selling** means *maximizing the likelihood a prospect buys*. That's it.
  not_to_confuse_with: >-
    Persuading or convincing a single prospect by argument; the author frames selling as arranging conditions so that buying becomes the most likely response, the way a horse is made to drink.
  why: >-
    If selling is a matter of likelihood, then every condition you control moves the odds, and nothing is left to whether the prospect was in the mood.
  anchor: >-
    First, **selling** means *maximizing the likelihood a prospect buys*. That’s it.
  source: >-
    acq-closer-handbook.md, What is Selling?, line 483
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:483"
- id: E-closer-002
  type: term
  name: >-
    Sales process
  statement: >-
    A sales process is the arrangement of conditions that maximizes the likelihood a prospect buys.
  definition: >-
    Second, a **sales process** *arranges conditions* to *maximize the likelihood a prospect buys*—(like how salty food makes drinking more likely).
  anchor: >-
    Second, a **sales process** *arranges conditions* to *maximize the likelihood a prospect buys*
  source: >-
    acq-closer-handbook.md, What is Selling?, line 485
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:485"
- id: E-closer-003
  type: term
  name: >-
    Salesperson
  statement: >-
    A salesperson is the person who goes through the sales process in order to maximize the likelihood a prospect buys.
  definition: >-
    Third, a **salesperson** *goes through the sales process* to *maximize the likelihood a prospect buys*.
  anchor: >-
    Third, a **salesperson** *goes through the sales process* to *maximize the likelihood a prospect buys*.
  source: >-
    acq-closer-handbook.md, What is Selling?, line 487
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:487"
- id: E-closer-004
  type: term
  name: >-
    Two-A-Days
  statement: >-
    Two-A-Days are the two daily one-on-ones with the manager, one to set expectations at the beginning of the day and one to review the day's work at the end.
  definition: >-
    **Two-A-Days.** Two 1-on-1s with your manager to set expectations and give feedback.
  anchor: >-
    **Two-A-Days.** Two 1-on-1s with your manager to set expectations and give feedback.
  source: >-
    acq-closer-handbook.md, Onboarding: Schedule & Training, line 658
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:658"
- id: E-closer-005
  type: term
  name: >-
    Roleplay
  statement: >-
    A roleplay is an acted-out sales conversation in which one person plays the prospect and gives the same problems a real call would, while the other practices the scripts and techniques.
  definition: >-
    **Roleplay.** Roleplaying is when you act out a sales conversation. One person plays the prospect and the other practices selling them.
  anchor: >-
    **Roleplay.** Roleplaying is when you act out a sales conversation. One person plays the prospect and the other practices selling them.
  source: >-
    acq-closer-handbook.md, Onboarding: Schedule & Training, line 684
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:684"
- id: E-closer-006
  type: term
  name: >-
    Shadowing
  statement: >-
    Shadowing is observing other salespeople sell live in order to learn how calls work and hear live customers.
  definition: >-
    **Shadowing.** You will observe ACQ salespeople sell. You will learn how calls work, hear live customers, and get to know the team.
  anchor: >-
    **Shadowing.** You will observe ACQ salespeople sell. You will learn how calls work, hear live customers, and get to know the team.
  source: >-
    acq-closer-handbook.md, Onboarding: Schedule & Training, line 695
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:695"
- id: E-closer-007
  type: term
  name: >-
    Gametape
  statement: >-
    Gametape is the study of call recordings with the script in hand, selling along with the salesman and roleplaying the hard parts rather than just listening.
  definition: >-
    **Gametape.** This is where you study call recordings. You'll start specific, then expand as you master the script.
  not_to_confuse_with: >-
    Merely listening to a recording for the words: the author says it is not about just getting the words, the recording must also be roleplayed, paused and rewatched.
  anchor: >-
    **Gametape.** This is where you study call recordings. You’ll start specific, then expand as you master the script.
  source: >-
    acq-closer-handbook.md, Onboarding: Schedule & Training, line 697
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:697"
- id: E-closer-008
  type: term
  name: >-
    Hunt Mode
  statement: >-
    Hunt Mode is everything a closer does to get prospects on the phone, and it maximizes opportunities while increasing conversion.
  definition: >-
    **Hunt Mode:** Everything you do to get prospects on the phone. This is where you sharpen your tools, lay your snares, and track your targets. Hunting maximizes opportunities and increases conversion.
  why: >-
    Hunting is more important than killing because you cannot take a shot without something to shoot.
  anchor: >-
    **Hunt Mode:** Everything you do to get prospects on the phone. This is where you sharpen your tools, lay your snares, and track your targets.
  source: >-
    acq-closer-handbook.md, On-Going: Schedule, line 1028
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1028"
- id: E-closer-009
  type: term
  name: >-
    Kill Mode
  statement: >-
    Kill Mode is everything a closer does while on the phone to get the sale, and it maximizes conversion while increasing opportunities.
  definition: >-
    **Kill Mode:** Everything you do while on the phone to get the sale. This is where you bring the pain, make your offer, loop any objections, and go for the kill.
  not_to_confuse_with: >-
    Hunt Mode, everything done to get prospects on the phone; a closer is always in one of the two modes.
  anchor: >-
    **Kill Mode:** Everything you do while on the phone to get the sale. This is where you bring the pain, make your offer, loop any objections, and go for the kill.
  source: >-
    acq-closer-handbook.md, On-Going: Schedule, line 1030
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1030"
- id: E-closer-010
  type: term
  name: >-
    Call notes
  statement: >-
    Call notes are the pre-call record of a prospect's business and likely objections, filled in jointly by the setter and then the closer, and reviewed the night before and the morning of the call.
  definition: >-
    Call notes are a combined effort between setters and closers. Setters extract what they can, and then closers fill whatever gaps they need to fill.
  why: >-
    If you know your prospect, then you know what offer is best for them and how to prepare for any objections ahead of time.
  anchor: >-
    Call notes are a combined effort between setters and closers. Setters extract what they can, and then closers fill whatever gaps they need to fill.
  source: >-
    acq-closer-handbook.md, Hunt Mode, #1 Call Notes, line 1238
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1238"
- id: E-closer-011
  type: term
  name: >-
    Inbound Set
  statement: >-
    An Inbound Set is a prospect who has booked an appointment but has not yet spoken to a closer, and is therefore the highest-value prospect on the list.
  definition: >-
    **Priority 1: Inbound Sets.** These are prospects who have booked an appointment but have not spoken to a closer yet. These are your newest, freshest, and therefore highest value appointments.
  applies_when: >-
    Priority 1 when working the list: on an inbound notification the closer calls immediately and tries to pull the close call forward.
  anchor: >-
    **Priority 1: Inbound Sets.** These are prospects who have booked an appointment but have not spoken to a closer yet.
  source: >-
    acq-closer-handbook.md, Hunt Mode, #2 Work Your List, line 1291
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1291"
- id: E-closer-012
  type: term
  name: >-
    BAMFAM
  statement: >-
    BAMFAM stands for Book A Meeting From A Meeting: securing the time of the next call while still on the current one, and the prospects so booked are Priority 2 on the list.
  definition: >-
    *BAMFAM stands for Book A Meeting From A Meeting.*
  not_to_confuse_with: >-
    Following up offline: the author forbids saying we'll follow up offline, because both parties are on the phone now.
  applies_when: >-
    When a close takes more than one call, for three reasons: Time Constraint, Prospect depends on Decision-Maker, Banking Delay (for very high ticket).
  anchor: >-
    *BAMFAM stands for Book A Meeting From A Meeting.*
  source: >-
    acq-closer-handbook.md, BAMFAM, line 2454
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:2454"
- id: E-closer-013
  type: term
  name: >-
    Pipeline
  statement: >-
    Pipeline is anyone who no-showed or declined the offer but whom there is still permission to call, worked newest to oldest back through the past 60 days.
  definition: >-
    **Priority 3: Pipeline.** Anyone that no-showed or declined our offer but who *we still have permission to call*.
  applies_when: >-
    Priority 3 on the list; the primary objective with a Pipeline prospect is to book them for a close call.
  anchor: >-
    **Priority 3: Pipeline.** Anyone that no-showed or declined our offer but who *we still have permission to call*.
  source: >-
    acq-closer-handbook.md, Hunt Mode, #2 Work Your List, line 1304
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1304"
- id: E-closer-014
  type: term
  name: >-
    Outbound
  statement: >-
    Outbound is making calls to create your own opportunities by setting your own appointments, done after the list is worked and during Pickup Primetime.
  definition: >-
    You create your own opportunities by making outbound calls to set your own appointments.
  anchor: >-
    You create your own opportunities by making outbound calls to set your own appointments.
  source: >-
    acq-closer-handbook.md, Hunt Mode, #3 Outbound, line 1397
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1397"
- id: E-closer-015
  type: term
  name: >-
    Pickup Primetime
  statement: >-
    Pickup Primetime is the end-of-day two-hour window when pick-up rates are highest, during which everything except a live call is dropped for outbound.
  definition: >-
    When Pickup Primetime occurs, you drop everything (except for a live call) to do outbound for the next two hours. Pickup Primetime happens at the end of the day because that's when our pick up rates are highest.
  why: >-
    It maximizes your return on time and maximizes your opportunities.
  anchor: >-
    When Pickup Primetime occurs, you drop everything (except for a live call) to do outbound for the next two hours.
  source: >-
    acq-closer-handbook.md, Hunt Mode, #3 Outbound, line 1399
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1399"
- id: E-closer-016
  type: term
  name: >-
    Referrals
  statement: >-
    Referrals are customers who come from our customers, asked for rather than waited for.
  definition: >-
    Referrals are when our customers send us more customers. We want lots of referrals. Customers *do* send referrals on their own, but it works even better if we just ask for them...
  why: >-
    Asking for referrals gets the simplest, cheapest, fastest, easiest, highest-converting opportunities, the least work per sale in the handbook, and should net one extra deal per day.
  anchor: >-
    Referrals are when our customers send us more customers. We want lots of referrals.
  source: >-
    acq-closer-handbook.md, Referrals, line 2496
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:2496"
- id: E-closer-017
  type: term
  name: >-
    Opt-Ins
  statement: >-
    Opt-ins are unscheduled leads who opted into the marketing list, called and texted newest to oldest with the remainder of the outbound block.
  definition: >-
    **Outbound Priority 2: Opt-Ins.** With the remainder of your outbound block, you double dial and text unscheduled leads who opted into our marketing list—from newest to oldest.
  not_to_confuse_with: >-
    Referrals, which are Outbound Priority 1 and come from existing customers.
  anchor: >-
    **Outbound Priority 2: Opt-Ins.** With the remainder of your outbound block, you double dial and text unscheduled leads who opted into our marketing list—from newest to oldest.
  source: >-
    acq-closer-handbook.md, Hunt Mode, #3 Outbound, line 1405
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1405"
- id: E-closer-018
  type: term
  name: >-
    Opt-out
  statement: >-
    A lead is opted in by default and becomes opted out only when they say to stop contacting them, at which point they are removed from the list.
  definition: >-
    If someone says: "Please don't contact me or try to sell me anymore." Then opt them out of the list. Every lead is opted in until they opt out.
  anchor: >-
    Every lead is opted in until they opt out.
  source: >-
    acq-closer-handbook.md, #4 End of Day Checklist, line 1422
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1422"
- id: E-closer-019
  type: term
  name: >-
    Inbox Zero
  statement: >-
    Inbox Zero is the end-of-day requirement to answer every lead message that built up across all channels, using the right script for each lead.
  definition: >-
    **Inbox Zero:** Respond to all lead messages across all channels that built up during the day. Use the right script for each lead.
  anchor: >-
    **Inbox Zero:** Respond to all lead messages across all channels that built up during the day.
  source: >-
    acq-closer-handbook.md, #4 End of Day Checklist, line 1424
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1424"
- id: E-closer-020
  type: term
  name: >-
    Script
  statement: >-
    A script is not a skill but a tool used to apply skill, and it does no work by itself.
  definition: >-
    And a script is not a skill—it is a tool you use to apply your skill.
  not_to_confuse_with: >-
    A skill: the author states the Closing Script doesn't do any work, YOU DO, and that the script on its own doesn't matter much without the skills applied to it.
  anchor: >-
    And a script is not a skill—it is a tool you use to apply your skill.
  source: >-
    acq-closer-handbook.md, Kill Mode, line 1457
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1457"
- id: E-closer-021
  type: term
  name: >-
    Breathe the script
  statement: >-
    Breathing the script means delivering it word-for-word, with your eyes closed, naturally, so knowing it costs no attention.
  definition: >-
    You need to deliver the script word-for-word, with your eyes closed, *naturally*.
  not_to_confuse_with: >-
    Reading it, or merely memorizing it, or using similar words in about the same order, which the author calls wrong.
  why: >-
    If you cannot remember what to say, have to look for it, or read it, you are not paying attention to the prospect, and then you say the wrong stuff and do not close.
  anchor: >-
    Most people think “breathe the script” means “use similar words in about the same order”. *This is wrong*. You need to deliver the script word-for-word, with your eyes closed, *naturally*.
  source: >-
    acq-closer-handbook.md, Breathe the Script, line 1522
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1522"
- id: E-closer-022
  type: term
  name: >-
    Tone
  statement: >-
    Tone is how the words are said, as opposed to the script which is what to say, and its job is to make every word do the job the script assigned it.
  definition: >-
    The script is what to say. Tone is how to say it.
  why: >-
    Tone gives a word its job, so changing tone changes what the word means; when every word does the right job you need fewer of them, and a closer who takes fewer words is more persuasive.
  anchor: >-
    The script is what to say. Tone is how to say it.
  source: >-
    acq-closer-handbook.md, Tone, line 1540
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1540"
- id: E-closer-023
  type: term
  name: >-
    Enunciation
  statement: >-
    Enunciation is saying words correctly and distinctly, with each sound and syllable clearly defined, and it is one of the three parts of tone that never change.
  definition: >-
    **Talk Clearer (Enunciation)** - saying words correctly and distinctly. Each sound and syllable is clearly defined.
  why: >-
    Enunciating keeps you talking at the right speed, displays more confidence and intelligence than a mumbler, and makes you easier to understand.
  anchor: >-
    **Talk Clearer (Enunciation)** - saying words correctly and distinctly. Each sound and syllable is clearly defined.
  source: >-
    acq-closer-handbook.md, Tone, line 1588
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1588"
- id: E-closer-024
  type: term
  name: >-
    Pitch
  statement: >-
    Pitch is the highness or lowness of the voice, used for one purpose only: raising it a little at the end of a group of words so the prospect knows a question was asked.
  definition: >-
    **Getting Prospects to Talk (Pitch)** - *Highness or lowness of your voice.* To clarify, we aren't singing here. *We want to make sure prospects know when we ask a question.*
  applies_when: >-
    Wherever a question mark (?) appears in the script, no matter where it sits in the sentence.
  anchor: >-
    **Getting Prospects to Talk (Pitch)** - *Highness or lowness of your voice.*
  source: >-
    acq-closer-handbook.md, Tone, line 1604
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1604"
- id: E-closer-025
  type: term
  name: >-
    Pauses
  statement: >-
    A pause is where and how long you do not talk, and it is the tone skill that focuses the prospect's attention on the words just said.
  definition: >-
    When You Don't Talk (Pauses) - Where and how long you *don't talk.* I think pauses are the most powerful tone skill of all.
  why: >-
    Pauses focus attention on what you just said, longer pauses focus more attention than shorter ones, and the more attention on a word the more important you make it.
  anchor: >-
    When You Don’t Talk (Pauses) - Where and how long you *don’t talk.* I think pauses are the most powerful tone skill of all.
  source: >-
    acq-closer-handbook.md, Tone, line 1627
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1627"
- id: E-closer-026
  type: term
  name: >-
    Short, medium and long pause — (…) (.) (—)
  statement: >-
    The scripts mark three pause lengths: (…) short, drawing a word out; (.) medium, a normal end-of-sentence pause placed mid-sentence; (—) long, much longer than normal and focusing the most attention.
  definition: >-
    3) (—) → Long. Much longer than you'd normally use. These focus the most attention. They won't feel natural at first. That's normal.
  anchor: >-
    3) (—) → Long. Much longer than you’d normally use. These focus the most attention.
  source: >-
    acq-closer-handbook.md, Tone, lines 1656–1658
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1658"
- id: E-closer-027
  type: term
  name: >-
    Introduction (intro)
  statement: >-
    The introduction is the first 30–60 seconds of the call, whose single purpose is to frame the rest of it.
  definition: >-
    The introduction is the first 30–60 seconds of every call. And it serves one purpose, to frame the rest of the call.
  not_to_confuse_with: >-
    Small talk ("How's the weather?"), a pitch, or a place to lie, skip parts or talk fast; the intro is a place to ask the minimum required questions, with the minimum required words, delivered in the proper tone.
  why: >-
    You can blow a 30 minute call in 30 seconds, and the minutes wasted at the beginning are the minutes you will wish for at the end.
  anchor: >-
    The introduction is the first 30–60 seconds of every call. And it serves one purpose, to frame the rest of the call.
  source: >-
    acq-closer-handbook.md, Introduction, line 1735
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1735"
- id: E-closer-028
  type: term
  name: >-
    Discovery
  statement: >-
    Discovery is the phase between the introduction and the offer in which the prospect's problems are drawn out in their own words and mapped to the categories the offer solves.
  definition: >-
    The Discovery phase of a close call happens after the introduction and before making the offer. And like the name suggests, we use it to discover things about the prospect.
  why: >-
    It heightens their awareness, for a short period, to all the bad things happening and all the good things not happening that not buying has caused.
  anchor: >-
    The Discovery phase of a close call happens after the introduction and before making the offer.
  source: >-
    acq-closer-handbook.md, Discovery, line 1828
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1828"
- id: E-closer-029
  type: term
  name: >-
    Pain Cycle
  statement: >-
    The Pain Cycle is steps 3–8 of discovery — Obstacle, Reason, Pull Teeth, Recap, Label, Confirm — run after the current and desired results are established and repeated until there are enough solvable problems.
  definition: >-
    Once we get the prospect to state their current and desired results, we start the Pain Cycle:
  applies_when: >-
    Ideally run once; repeated when a problem is not big enough, with a list of results ready to ask about.
  anchor: >-
    Once we get the prospect to state their current and desired results, we start the Pain Cycle:
  source: >-
    acq-closer-handbook.md, Discovery, line 1849
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1849"
- id: E-closer-030
  type: term
  name: >-
    Pull Teeth
  statement: >-
    Pulling teeth is step 5 of discovery: getting specific details when the prospect's answers are vague, confusing or incomplete, by asking them to tell you more and then for an example.
  definition: >-
    5) **Pull Teeth** - Get specific details when answers are vague, confusing, or incomplete
  why: >-
    Asking for more information and then an example connects the problem to a life experience and gives material to map to our solution; the response is the same whatever type of bad answer it was.
  anchor: >-
    5) **Pull Teeth** - Get specific details when answers are vague, confusing, or incomplete
  source: >-
    acq-closer-handbook.md, Discovery, line 1853
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1853"
- id: E-closer-031
  type: term
  name: >-
    Recap
  statement: >-
    A Recap repeats the prospect's problem back in the prospect's own words; in the scripts it appears as the notation [RECAP].
  definition: >-
    6) **Recap** - Repeat their problem in their words.
  not_to_confuse_with: >-
    Label, which states the same problem in our words; the Recap keeps the prospect's wording.
  anchor: >-
    6) **Recap** - Repeat their problem in their words.
  source: >-
    acq-closer-handbook.md, Discovery, line 1918
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1918"
- id: E-closer-032
  type: term
  name: >-
    Label
  statement: >-
    A Label states the prospect's problem in our words, using one of five categories — Marketing, Sales, Product/Delivery, People, Profit — that map to the solutions offered later.
  definition: >-
    Thankfully, we only describe them in five—and these five, listed below, are the labels we use to map to our offer later.
  why: >-
    Business owners describe their problems in a million ways, and the label is what the solution and benefits in the offer are mapped to.
  anchor: >-
    Thankfully, we only describe them in five—and these five, listed below, are the labels we use to map to our offer later.
  source: >-
    acq-closer-handbook.md, Discovery, lines 1919–1936
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1924"
- id: E-closer-033
  type: term
  name: >-
    Confirm
  statement: >-
    To Confirm is to ask the prospect whether the recap and label were got right.
  definition: >-
    8) **Confirm** - Ask if you got it correct.
  anchor: >-
    8) **Confirm** - Ask if you got it correct.
  source: >-
    acq-closer-handbook.md, Discovery, line 1920
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1920"
- id: E-closer-034
  type: term
  name: >-
    Stack the pain (Final Recap)
  statement: >-
    Stacking the pain is the final recap: saying all the collected Recaps again together, labelling the whole, and asking the prospect to confirm.
  definition: >-
    Once you've completed your Pain Cycles, you need to stack the pain. To stack the pain, get your Recaps together and say them all again. Then, as before, ask the prospect if you got it right.
  anchor: >-
    Once you’ve completed your Pain Cycles, you need to stack the pain. To stack the pain, get your Recaps together and say them all again.
  source: >-
    acq-closer-handbook.md, Discovery, line 1958
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1958"
- id: E-closer-035
  type: term
  name: >-
    Solution stack
  statement: >-
    The solution stack is the set of solution-and-benefit pairs mapped to the prospect's problems, listed again after each mapping and three times in total before asking for the sale.
  definition: >-
    So what words should you say? Your solution stack.
  applies_when: >-
    In the offer, which lasts two minutes, about 320 words at 150–170 words per minute.
  anchor: >-
    It just means... you must make every word count. So what words should you say? Your solution stack.
  source: >-
    acq-closer-handbook.md, Offer, lines 1989–2015
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1989"
- id: E-closer-036
  type: term
  name: >-
    Assure
  statement: >-
    To Assure is to tell the prospect why the named solution is great, which decreases their risk, and it sits between Solution and Benefit in the offer mapping.
  definition: >-
    c) **Assure:** Tell them why that thing is great (decrease risk).
  anchor: >-
    c) **Assure:** Tell them why that thing is great (decrease risk).
  source: >-
    acq-closer-handbook.md, Offer, line 2009
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2009"
- id: E-closer-037
  type: term
  name: >-
    Plug and chug
  statement: >-
    Plug and chug is making the offer entirely from labels, solutions, assurances and benefits prepared in advance, so nothing is invented on the call.
  definition: >-
    With proper preparation you need only to "plug and chug".
  why: >-
    Prospects change but the solutions provided stay the same, so you should never have to come up with anything on the fly and risk saying something dumb, screwing up your tone, or both.
  anchor: >-
    With proper preparation you need only to “plug and chug”.
  source: >-
    acq-closer-handbook.md, Offer, line 2024
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2024"
- id: E-closer-038
  type: term
  name: >-
    Drop Price & STFU
  statement: >-
    Drop Price & STFU is the last step of the offer: state the price and then stop talking.
  definition: >-
    5) **Drop Price & STFU:** Then you state the price and shut the fuck up.
  why: >-
    The longest pause always goes after the buying question, because it forces the prospect to address it head on instead of avoiding it.
  anchor: >-
    5) **Drop Price & STFU:** Then you state the price and shut the fuck up.
  source: >-
    acq-closer-handbook.md, Offer, line 2017
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2017"
- id: E-closer-039
  type: term
  name: >-
    Objection
  statement: >-
    An objection is the prospect's reason for not doing what you asked, and a prospect can object to any request, not only to buying.
  definition: >-
    An *Objection* refers to their *reason* they don't. This means prospects can object to *any* request.
  anchor: >-
    An *Objection* refers to their *reason* they don't. This means prospects can object to *any* request.
  source: >-
    acq-closer-handbook.md, Objections, line 2074
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2074"
- id: E-closer-040
  type: term
  name: >-
    Buying Objection
  statement: >-
    A Buying Objection is anything the prospect does other than buy after being asked to buy, and they all chunk up into five types.
  definition: >-
    When you ask a prospect to buy and they do anything other than buy, it lands us here.
  not_to_confuse_with: >-
    Objections to any other request; buying objections are where a majority of attention goes.
  anchor: >-
    When you ask a prospect to buy and they do anything other than buy, it lands us here.
  source: >-
    acq-closer-handbook.md, Objections, line 2078
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2078"
- id: E-closer-041
  type: term
  name: >-
    Time objection
  statement: >-
    A Time objection is the prospect saying they will not buy because they do not have the time to get the value.
  definition: >-
    **#1 Time** - The prospect says they will not buy because they do not have the time to get the value.
  not_to_confuse_with: >-
    A genuine shortage of time: in the author's words, not enough time is never an objection, only not a high-enough priority.
  anchor: >-
    **#1 Time** - The prospect says they will not buy because they do not have the time to get the value.
  source: >-
    acq-closer-handbook.md, Objections, line 2084
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2084"
- id: E-closer-042
  type: term
  name: >-
    Money objection
  statement: >-
    A Money objection is the prospect saying they are not able or not willing to pay the price, and it is roughly half of all objections.
  definition: >-
    #2 Money - The prospect says they are not able or not willing to pay the price. This is solved by showing how much the problem costs compared to the solution. This accounts for roughly 50% of objections.
  anchor: >-
    #2 Money - The prospect says they are not able or not willing to pay the price.
  source: >-
    acq-closer-handbook.md, Objections, line 2101
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2101"
- id: E-closer-043
  type: term
  name: >-
    Decision-Maker objection
  statement: >-
    A Decision-Maker objection is the prospect saying they must get permission from somebody else before they can buy.
  definition: >-
    #3 Decision-Maker - The prospect says they must get permission from somebody else before they can buy.
  anchor: >-
    #3 Decision-Maker - The prospect says they must get permission from somebody else before they can buy.
  source: >-
    acq-closer-handbook.md, Objections, line 2113
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2113"
- id: E-closer-044
  type: term
  name: >-
    Preference objection
  statement: >-
    A Preference objection is the prospect saying they expected something different or would rather do something else.
  definition: >-
    #4 Preference - The prospect says they expected something different or that they'd rather do something else.
  anchor: >-
    #4 Preference - The prospect says they expected something different or that they'd rather do something else.
  source: >-
    acq-closer-handbook.md, Objections, line 2130
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2130"
- id: E-closer-045
  type: term
  name: >-
    Stall objection
  statement: >-
    A Stall objection is the prospect saying they must wait before they will buy, without a specific reason.
  definition: >-
    #5 Stall - The prospect says they must wait before they will buy.
  not_to_confuse_with: >-
    A Time objection, which is about not having time to get the value; a stall is about needing more time to consider the decision.
  anchor: >-
    #5 Stall - The prospect says they must wait before they will buy.
  source: >-
    acq-closer-handbook.md, Objections, line 2143
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2143"
- id: E-closer-046
  type: term
  name: >-
    Looping
  statement: >-
    Looping is overcoming an objection by acknowledging it, adding to the prospect's reasoning, and immediately asking for the sale again, repeated until they buy or time runs out.
  definition: >-
    Looping is a technique to overcome objections by acknowledging their objection, presenting your additions, and then *looping* the prospect back to the offer.
  not_to_confuse_with: >-
    Winning an argument or catching the prospect in a silly excuse; the author says expecting them to buy because you caught them is worse than letting them walk.
  why: >-
    The salespeople who ask for the buy the most times get the most closes, and only agreeable interactions give you enough opportunities to ask.
  anchor: >-
    Looping is a technique to overcome objections by acknowledging their objection, presenting your additions, and then *looping* the prospect back to the offer.
  source: >-
    acq-closer-handbook.md, Looping, line 2250
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2250"
- id: E-closer-047
  type: term
  name: >-
    Confirming Value
  statement: >-
    Confirming value is the step before any looping: ignore the first objection and ask whether the prospect thinks the product can help get them closer to their goal.
  definition: >-
    Do they think our product is valuable? To get that information we must confirm the value.
  applies_when: >-
    On the first objection, before getting into objection whack-a-mole.
  anchor: >-
    Do they think our product is valuable? To get that information we must confirm the value.
  source: >-
    acq-closer-handbook.md, Looping, line 2270
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2270"
- id: E-closer-048
  type: term
  name: >-
    Triage question / reflex objection
  statement: >-
    The triage question follows the value confirmation whatever the answer, and gets the prospect to abandon their reflex objection so the objection actually worth handling is isolated.
  definition: >-
    The main objective is to get them to abandon their "reflex" objection. This way, you isolate the objection worth handling.
  anchor: >-
    The main objective is to get them to abandon their “reflex” objection. This way, you isolate the objection worth handling.
  source: >-
    acq-closer-handbook.md, Looping, lines 2282–2291
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2282"
- id: E-closer-049
  type: term
  name: >-
    AGREE… AND…
  statement: >-
    AGREE… AND… is the acknowledgement formula that opens every loop: agree with the objection, then add the line of reasoning with and, never but.
  definition: >-
    What comes after the "AGREE… AND…" will be the line of reasoning we add to their own, depending on their reason.
  not_to_confuse_with: >-
    Agree… but…: the author calls But a big fat eraser that means ignore all the words before it, and says using it will cost the sale.
  why: >-
    The acknowledgement is disarming because prospects expect an argument, and agreement buys you more opportunities to ask again.
  anchor: >-
    What comes after the “AGREE… AND…” will be the line of reasoning we add to their own, depending on their reason.
  source: >-
    acq-closer-handbook.md, Looping, lines 2369–2382
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2382"
```
