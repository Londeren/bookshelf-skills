# Улов фазы 1 — ACQ Closer Handbook (2025) (ярус 2), тип A: фреймворки

Группа `tier2-closer`, слаг `closer`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **53** (экстрактор вернул 53, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `acq-closer-handbook.md` | 1–4125 | 5 | 53 |

## Как собран файл

Экстрактор A (Frameworks) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-closer.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-closer-A.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: A-closer-001
  type: framework
  name: >-
    The two objectives of the ideal salesperson
  statement: >-
    A salesperson works on exactly two objectives at once: applying the sales process perfectly to every prospect, and applying it to as many prospects as possible.
  why: >-
    Ideal selling raises the likelihood of buying towards 100% for as many prospects as possible, so both the quality of the process and the number of prospects put through it are levers on the same result.
  structure:
    - >-
      To apply the sales process perfectly to *maximize his chances of making the sale*.
    - >-
      To apply the sales process to as many prospects as possible to *maximize his opportunities to sell*.
  anchor: >-
    So if *ideal selling* increases the likelihood of buying to 100% for as many prospects as possible, then the *ideal salesperson* has two objectives:
  source: >-
    acq-closer-handbook.md, What is Selling?, lines 489–492
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:489"
- id: A-closer-002
  type: framework
  name: >-
    Memorizing the Script
  statement: >-
    The script is memorized by printing two copies, reading it aloud, blacking out one random word at a time and rereading until the whole script is blacked out, checking against the clean copy.
  why: >-
    The reader needs to breathe the script rather than read it, and letting memory fill each blacked-out gap forces recall instead of recognition.
  applies_when: >-
    The first days on the job, before going live on the phones.
  structure:
    - >-
      Print out *at least* two copies of the script.
    - >-
      Read the script out loud.
    - >-
      Use a marker to black out one random word.
    - >-
      Read it out loud again and let your memory fill in the gap.
    - >-
      Continue until you black out the whole script.
  anchor: >-
    **Memorizing the Script.** You will memorize the script. Here's how to do it:
  source: >-
    acq-closer-handbook.md, Onboarding: Schedule & Training, lines 670–677
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:670"
- id: A-closer-003
  type: framework
  name: >-
    Roleplay the ACQ way (five steps)
  statement: >-
    A roleplay runs in five fixed steps: the manager frames what to practise and why, models it, has the rep copy it, has the rep practise until it is right, then recaps and moves to the next one.
  why: >-
    Repetition with feedback is how the skill is acquired; the rep keeps trying until he does it right rather than being corrected once.
  applies_when: >-
    Practising a sales conversation, in onboarding and in ongoing team training alike.
  structure:
    - >-
      **Frame it:** The manager explains what to practice, how to do it, and why.
    - >-
      **Model it:** Then, he will show you.
    - >-
      **Copy it:** Then, you will copy him.
    - >-
      **Practice it:** Then, you will roleplay until you get it.
    - >-
      **Recap it:** Then he will recap the roleplay and move on to the next one.
  anchor: >-
    Roleplaying is when you act out a sales conversation. One person plays the prospect and the other practices selling them.
  source: >-
    acq-closer-handbook.md, Onboarding: Schedule & Training, lines 684–691; repeated On-Going: Training, lines 785–798
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:684"
- id: A-closer-004
  type: framework
  name: >-
    The four parts of the closing script
  statement: >-
    The closing script is trained and worked in four parts — Introduction, Discovery, Offer, Looping — one part per training day.
  why: >-
    Splitting the script into four parts gives one focus per day instead of rehearsing the whole thing at once.
  structure:
    - >-
      Introduction
    - >-
      Discovery
    - >-
      Offer
    - >-
      Looping
  anchor: >-
    We train the closing script in four parts: Introduction, Discovery, Offer, and Looping.
  source: >-
    acq-closer-handbook.md, On-Going: Training, lines 777–783
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:777"
- id: A-closer-005
  type: framework
  name: >-
    Max Opportunities x Max Conversion = Maximum Sales
  statement: >-
    A closer has two objectives, maximizing opportunities and maximizing conversion, and sales are the product of the two rather than either one alone.
  why: >-
    Empty slots today are used to get full slots tomorrow, so the two objectives feed each other instead of competing.
  structure:
    - >-
      Maximize Opportunities
    - >-
      Maximize Conversion
  anchor: >-
    Max Opportunities x Max Conversion = Maximum Sales
  source: >-
    acq-closer-handbook.md, On-Going: Schedule, lines 1020–1024
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1024"
- id: A-closer-006
  type: framework
  name: >-
    Hunt Mode and Kill Mode
  statement: >-
    All selling time is spent in one of two modes: Hunt Mode, everything done to get prospects on the phone, and Kill Mode, everything done while on the phone to get the sale.
  why: >-
    Hunting maximizes opportunities and increases conversion; killing maximizes conversion and increases opportunities, so a closer is always working one of the two objectives.
  structure:
    - >-
      **Hunt Mode:** Everything you do to get prospects on the phone. This is where you sharpen your tools, lay your snares, and track your targets.
    - >-
      **Kill Mode:** Everything you do while on the phone to get the sale. This is where you bring the pain, make your offer, loop any objections, and go for the kill.
  anchor: >-
    ACQ Closers do this in two modes: Hunt Mode and Kill Mode.
  source: >-
    acq-closer-handbook.md, On-Going: Schedule, lines 1026–1032
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1026"
- id: A-closer-007
  type: framework
  name: >-
    The four activities of hunting
  statement: >-
    Hunting consists of four activities, done in this order through the day: call notes, working your list, outbound, and the end of day checklist.
  why: >-
    You cannot take a shot without something to shoot, so the hours away from calls are spent lining up as many calls as possible.
  structure:
    - >-
      Call Notes
    - >-
      Working Your List
    - >-
      Outbound
    - >-
      End of Day Checklist
  anchor: >-
    In this section, you will see exactly what to do, every hour of the day, to line up as many kills as possible.
  source: >-
    acq-closer-handbook.md, Hunt Mode, lines 1221–1230
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1221"
- id: A-closer-008
  type: framework
  name: >-
    Call Notes
  statement: >-
    Before a call the prospect is written up against a fixed list of fields, updated the night before and the morning of the call, with setters extracting what they can and closers filling the gaps.
  why: >-
    Knowing the prospect tells you which offer is best for them and lets you prepare for their objections ahead of time.
  applies_when: >-
    Every scheduled close call, the night before and the morning of.
  structure:
    - >-
      Owner Name:
    - >-
      Business Name:
    - >-
      Business Industry:
    - >-
      Years in Business:
    - >-
      Revenue:
    - >-
      Profit:
    - >-
      What They Sell:
    - >-
      How They Get Customers:
    - >-
      Needs Help With (Constraint):
    - >-
      Potential Objections:
  anchor: >-
    Call notes really increase conversion. If you know your prospect, then you know what offer is best for them and how to prepare for any objections ahead of time.
  source: >-
    acq-closer-handbook.md, Hunt Mode #1 Call Notes, lines 1236–1283
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1236"
- id: A-closer-009
  type: framework
  name: >-
    Work Your List: the three priorities
  statement: >-
    Prospects are worked in the order they are most likely to buy, in three groups: inbound sets first, then BAMFAMs, then pipeline.
  why: >-
    Newest, freshest appointments are the highest value, so they are called immediately; the other groups are worked in descending likelihood of buying.
  applies_when: >-
    Every hour of the day that is not a close call.
  structure:
    - >-
      **Priority 1: Inbound Sets.** These are prospects who have booked an appointment but have not spoken to a closer yet.
    - >-
      **Priority 2: BAMFAMs.** "Booked A Meeting From A Meeting." BAMFAMs have already spoken to a closer, have not bought yet, and have another close call scheduled.
    - >-
      **Priority 3: Pipeline.** Anyone that no-showed or declined our offer but who *we still have permission to call*.
  anchor: >-
    You work the prospects in the order they are most likely to buy. To make it simple, we split them into three groups. Each is explained below.
  source: >-
    acq-closer-handbook.md, Hunt Mode #2 Work Your List, lines 1289–1312
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1289"
- id: A-closer-010
  type: framework
  name: >-
    Color Code Your Reachouts
  statement: >-
    Every reachout is color coded by its state so the whole list can be read at a glance, each color carrying one prescribed action.
  why: >-
    You will have trouble remembering everything, so the code carries the state instead of your memory.
  structure:
    - >-
      **Yellow - Unclosed & No Response** — Action → Pipeline Text Script Sent
    - >-
      **Green - Unclosed & Responded** — Action → Lead responded to Pipeline Text Script
    - >-
      **Purple - Closed** — Action → Referral Text Script Sent
    - >-
      **Grey - BAMFAM** — Action → BAMFAM Script Sent
    - >-
      **Red - Deliberate Opt Out** — Action → Opt Them Out
  anchor: >-
    You will have trouble remembering everything. Color code it so you don't have to:
  source: >-
    acq-closer-handbook.md, Hunt Mode #2 Work Your List, lines 1314–1336
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1316"
- id: A-closer-011
  type: framework
  name: >-
    Working Inbound Sets: The Full Process
  statement: >-
    An inbound set is taken to a close call through a fixed branching sequence: double dial to validate the contact, then three text blocks, with non-response steps and a cancel at twelve hours out.
  why: >-
    The process makes sure none of these precious prospects slip through the cracks.
  applies_when: >-
    From the moment an inbound lead books an appointment until the close call happens.
  structure:
    - >-
      **Double Dial to Validate Contact Info** — If Fake → Cancel and Opt Out; If they pick up → Pull Forward
    - >-
      Business (Block 1) — If response → [Why Us (Block 2)]
    - >-
      If no response after 12 hours → Non-Response 1
    - >-
      If no response after 24 hrs → Non-Response 2
    - >-
      Wait until 12 hrs before call → Cancel
    - >-
      Why Us (Block 2) — If response → [Pull Forward (Block 3)]; If not → Send Night Before/Morning of texts
    - >-
      Pull Forward (Block 3) — If Pulled Forward Same Day → Close; If not → Send Night Before/Morning of texts
  anchor: >-
    This process breaks down taking an Inbound Set all the way to a Close call. You need to know this very well.
  source: >-
    acq-closer-handbook.md, Hunt Mode, Working Inbound Sets: The Full Process, lines 1347–1388
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1367"
- id: A-closer-012
  type: framework
  name: >-
    The two outbound priorities
  statement: >-
    Outbound time goes first to referrals from existing customers and only then, with the remainder, to opted-in leads worked from newest to oldest.
  why: >-
    Referrals are the best leads you can get and should net an extra deal a day; opt-ins at roughly two sets per hour produce at least one more close.
  applies_when: >-
    After the list is worked, and during the two-hour Pickup Primetime block at the end of the day.
  structure:
    - >-
      **Outbound Priority 1: Getting Referrals.** Referrals are customers that come from our customers.
    - >-
      **Outbound Priority 2: Opt-Ins.** With the remainder of your outbound block, you double dial and text unscheduled leads who opted into our marketing list—from newest to oldest.
  anchor: >-
    You create your own opportunities by making outbound calls to set your own appointments. First, you will do outbound after working your list. Second, you will do outbound during Pickup Primetime.
  source: >-
    acq-closer-handbook.md, Hunt Mode #3 Outbound, lines 1397–1409
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1397"
- id: A-closer-013
  type: framework
  name: >-
    End of Day Checklist
  statement: >-
    The day closes with five fixed items: record call outcomes, update call notes, update opt-outs, submit your worst call for review, and clear the inbox.
  why: >-
    You win tomorrow today; marking outcomes sorts tomorrow's leads by priority, and the worst call becomes training material.
  structure:
    - >-
      **Record Call Outcomes:** Mark the outcome in the CRM. Mark them as Closed, BAMFAM, Pipeline, and Opt-Out.
    - >-
      **Update Call Notes:** Add any new and useful information you learned about your prospects to your call notes.
    - >-
      **Update Opt-Outs:** If someone says: “Please don’t contact me or try to sell me anymore.” Then opt them out of the list.
    - >-
      **Submit Your Worst Call For Review:** This is the call you had the most trouble with that day.
    - >-
      **Inbox Zero:** Respond to all lead messages across all channels that built up during the day.
  anchor: >-
    You win tomorrow today. So at the end of your day, you close up shop by finishing this checklist:
  source: >-
    acq-closer-handbook.md, Hunt Mode #4 End of Day Checklist, lines 1418–1424
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1418"
- id: A-closer-014
  type: framework
  name: >-
    The nine Kill Skills
  statement: >-
    Everything done on a call reduces to nine skills, learned in this order: Breathe the Script, Tone, Introduction, Discovery, Offer, Objections, Looping, BAMFAM, Referrals.
  why: >-
    Every qualified prospect is sellable if the conditions are controlled, and the conditions are controlled with skill; the hard part is doing them all, correctly, every time.
  structure:
    - >-
      Breathe the Script
    - >-
      Tone
    - >-
      Introduction
    - >-
      Discovery
    - >-
      Offer
    - >-
      Objections
    - >-
      Looping
    - >-
      BAMFAM
    - >-
      Referrals
  anchor: >-
    We don't beat other sales teams because we do mysterious and magical things nobody else knows.
  source: >-
    acq-closer-handbook.md, Kill Mode / Kill Skills, lines 1437–1457
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1439"
- id: A-closer-015
  type: framework
  name: >-
    The two buckets of tone
  statement: >-
    Tone splits into what stays the same on every call — speed, volume, enunciation — and what changes on cue from the script — pauses and pitch.
  why: >-
    The script assigns a job to each word and tone makes sure the word does that job; a word doing the right job means fewer words are needed to close.
  structure:
    - >-
      How **slow** you talk: Prospects need to **keep track** of your words.
    - >-
      How **loud** you talk: Prospects need to **hear** your words.
    - >-
      How **clear** you talk: Prospects need to **understand** your words.
    - >-
      When you **don't talk**: Prospects need to **focus on specific words**.
    - >-
      When you **get them to talk**: Prospects need to **say words back**.
  anchor: >-
    Your script assigns a job to each word. Your tone makes sure the word does that job. So to make tone as simple and easy as possible, I break it down into two buckets.
  source: >-
    acq-closer-handbook.md, Tone, lines 1548–1565
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1548"
- id: A-closer-016
  type: framework
  name: >-
    The three types of pauses
  statement: >-
    Pauses come in three marked lengths — short, medium and long — and the script notation says which one to use where.
  why: >-
    Pauses focus attention on what you just said, longer pauses focus more attention, and the more attention on a word the more important it becomes.
  applies_when: >-
    Wherever the script marks a pause; the longest pause always goes after the buying question.
  structure:
    - >-
      (…) → Short. Pauses that draw words out just enough to put more attention on or around that word.
    - >-
      (.) → Medium. Your normal pause. Like you’d use at the end of a sentence.
    - >-
      (—) → Long. Much longer than you’d normally use. These focus the most attention.
  anchor: >-
    We use three types of pauses. Short, medium, and long:
  source: >-
    acq-closer-handbook.md, Tone, lines 1654–1658; notation repeated ACQ Closing Script, lines 3247–3249
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1654"
- id: A-closer-017
  type: framework
  name: >-
    The four things every introduction must have
  statement: >-
    Every call opens with the rep's name, the company he calls from, that the call is recorded and the reason for the call, followed by a one-sentence agenda for the call.
  why: >-
    Those four are required by law, they sound like a legitimate business, and the introduction's single purpose is to frame the rest of the call.
  applies_when: >-
    The first 30–60 seconds of every call.
  structure:
    - >-
      Your name.
    - >-
      That you call from ACQ.
    - >-
      That the call is recorded.
    - >-
      The reason you're calling.
    - >-
      Then, after you get confirmation of the big four required by law, you state the agenda for the call.
  anchor: >-
    The start of every sale must have these four things:
  source: >-
    acq-closer-handbook.md, Introduction, lines 1735–1779
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1737"
- id: A-closer-018
  type: framework
  name: >-
    Discovery and Offer as two halves
  statement: >-
    Discovery raises awareness of more bad stuff and less good stuff if the prospect does nothing; the offer shows more good stuff and less bad stuff if they buy.
  why: >-
    Discovery heightens awareness of all the bad things happening and the good things not happening that not buying has caused, which is what the offer is then mapped against.
  structure:
    - >-
      **DISCOVERY:** MORE BAD STUFF LESS GOOD STUFF ... IF YOU DO NOTHING
    - >-
      **OFFER:** MORE GOOD STUFF LESS BAD STUFF ... IF YOU BUY
  anchor: >-
    we use it to discover things about the prospect. And in doing so, for a short period of time, heighten their awareness to all the bad things that are happening and all the good things that are not happening that not buying has caused.
  source: >-
    acq-closer-handbook.md, Discovery, lines 1820–1828; repeated Offer, lines 1979–1983
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1828"
- id: A-closer-019
  type: framework
  name: >-
    The 9 Steps of Discovery
  statement: >-
    Discovery runs nine steps — current, desired, then the pain cycle of obstacle, reason, pull teeth, recap, label, confirm — repeating the cycle until there are enough problems you can solve.
  why: >-
    Business owners never volunteer clearly labelled problems, so they have to be pulled out; every reason they cannot get results is another reason for them to buy.
  applies_when: >-
    After the introduction and before making the offer.
  structure:
    - >-
      **Current** - Establish where they are now
    - >-
      **Desired** - Establish where they want to be
    - >-
      **Obstacle** - Identify what's blocking them
    - >-
      **Reason** - Understand why it's not working
    - >-
      **Pull Teeth** - Get specific details when answers are vague, confusing, or incomplete
    - >-
      **Recap** - Restate their problem in their words
    - >-
      **Label** - Map their problem to your solution categories
    - >-
      **Confirm** - Verify you understood correctly
    - >-
      **Repeat** - Cycle back to steps 3-8 until you have enough problems you can solve
  anchor: >-
    Discovery follows a nine-step process that cycles through identifying problems until you have enough to make your offer:
  source: >-
    acq-closer-handbook.md, Discovery, The 9 Steps of Discovery, lines 1836–1868
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1838"
- id: A-closer-020
  type: framework
  name: >-
    The Pain Cycle
  statement: >-
    Once current and desired results are stated, steps three to eight run as a cycle — obstacle, reason, pull teeth, recap, label, confirm — and the cycle is repeated on the next problem if one is not enough.
  why: >-
    Ideally the cycle runs once, but more problems mean more reasons to buy, so the closer keeps a list of results to ask about ready to go.
  applies_when: >-
    After the gap between current and desired results has been established.
  structure:
    - >-
      **Obstacle** - Identify what's blocking them
    - >-
      **Reason** - Understand why it's not working
    - >-
      **Pull Teeth** - Get specific details when answers are vague, confusing, or incomplete
    - >-
      **Recap** - Restate their problem in their words
    - >-
      **Label** - Map their problem to your solution categories
    - >-
      **Confirm** - Verify you understood correctly
  anchor: >-
    Once we get the prospect to state their current and desired results, we start the Pain Cycle:
  source: >-
    acq-closer-handbook.md, Discovery, lines 1849–1857 and 1944–1950
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1849"
- id: A-closer-021
  type: framework
  name: >-
    Pull Teeth
  statement: >-
    Whenever an answer is vague, confusing or incomplete, the response is the same two questions in the same order: ask them to tell you more, then ask for an example.
  why: >-
    Only two things matter — getting more information about the problem and mapping it to our solution — and asking for an example tends to make them connect it to a life experience.
  applies_when: >-
    Any vague, confusing or incomplete answer in discovery; also used on any objection the closer is unsure how to answer.
  structure:
    - >-
      **Vague:** I see. Can you tell me more about that?
    - >-
      Ok, cool. Can you give me an example?
  anchor: >-
    You'll note, no matter the type of bad answer, *you respond the same way*. You ask them to tell you more, and then you ask them to give an example.
  source: >-
    acq-closer-handbook.md, Discovery, Step 5: Pull Teeth, lines 1889–1912; reused Looping, lines 2352–2357
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1907"
- id: A-closer-022
  type: framework
  name: >-
    Recap, Label & Confirm
  statement: >-
    A problem is closed out in three moves: repeat it in their words, state it in our words, then ask whether you got it right.
  why: >-
    Recapping lays out their problem plainly and frames it in a way we can solve it, and the label is the word that will be mapped to the solution in the offer.
  applies_when: >-
    After the first steps of the Pain Cycle, and again on every later cycle.
  structure:
    - >-
      **Recap** - Repeat their problem in their words.
    - >-
      **Label** - State the problem in our words.
    - >-
      **Confirm** - Ask if you got it correct.
  anchor: >-
    Once you successfully go through the first steps of the Pain Cycle, it's time to recap. Recapping lays out their problem plainly and frames it in a way we can solve it.
  source: >-
    acq-closer-handbook.md, Discovery, Steps 6–8, lines 1914–1942
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1916"
- id: A-closer-023
  type: framework
  name: >-
    The five labels
  statement: >-
    However a business owner describes a problem, it is labelled into one of five categories — marketing, sales, product/delivery, people, profit — and it is those labels that get mapped to the offer.
  why: >-
    Business owners describe their problems in a million ways but every problem they have can and should be mapped to a solution we offer, so five labels are enough.
  structure:
    - >-
      **Marketing** → no views/reach, no ad conversions, too few leads, bad quality leads, personal brand not growing, etc.
    - >-
      **Sales** → can't close, no one can afford our stuff, no one can close like me, can't find good sales people, sales are inconsistent, etc.
    - >-
      **Product/Delivery** → churn is high, lifetime value is low, can't get people to buy again or come back, can't make enough to service customers.
    - >-
      **People** → my team sucks, I have no help, I'm overwhelmed, I can't find [insert role].
    - >-
      **Profit** → we're just not making as much money as we want, we are cash-flow constrained.
  anchor: >-
    Thankfully, we only describe them in five—and these five, listed below, are the labels we use to map to our offer later.
  source: >-
    acq-closer-handbook.md, Discovery, Steps 6–8, lines 1924–1942
  confirmations: 3
  authors_caveat: >-
    The scripts read the list back to the prospect in shorter and slightly different forms: marketing, sales, people, profit, or operations in the Outbound Set Phone Script (line 2857), and Marketing? Sales? People? Profit?...Something crazy? in the Closing Script (line 3351).
  anchor_at: "acq-closer-handbook.md:1924"
- id: A-closer-024
  type: framework
  name: >-
    Final Recap (Stacking the Pain)
  statement: >-
    When the pain cycles are done, all the recaps are put together and said again as one, given a single label, and confirmed.
  why: >-
    You are just sharing what you learned and then making sure they agree, which is what the offer is then built on.
  applies_when: >-
    Once the pain cycles are complete and before the transition to the offer.
  structure:
    - >-
      **Recap** - To make sure I understand. You tried three different marketing agencies, spent $50K, got leads that didn’t convert, and now you’re hesitant to invest again.
    - >-
      **Label** - So it sounds like the real issue isn’t just vendors, ads, and leads - it’s that you need an entirely new marketing and sales process.
    - >-
      **Confirm** - Does that sound right?
  anchor: >-
    Once you’ve completed your Pain Cycles, you need to stack the pain. To stack the pain, get your Recaps together and say them all again.
  source: >-
    acq-closer-handbook.md, Discovery, Final Recap (Stacking the Pain), lines 1956–1966
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1958"
- id: A-closer-025
  type: framework
  name: >-
    The offer making process
  statement: >-
    The offer runs five steps: transition with permission to share, map the problems to three solutions, stack the solution and benefit pairs, ask for the sale, then drop the price and stop talking.
  why: >-
    Typical salespeople go straight to pitching and abandon the pain points they just collected; mapping them instead crafts a personalized offer on the spot.
  applies_when: >-
    After all the problems have been recapped; the offer itself has two minutes, about 320 words.
  structure:
    - >-
      **Transition:** Tell them you think we can help. Then ask if they'd like to hear how.
    - >-
      **Map:** Connect their problems to our solutions, assurances, benefits, then confirm that it would help.
    - >-
      **Stack:** List all solution and benefit pairs up to this point. You do this three times.
    - >-
      **Ask:** Ask if they are ready to buy/move forward.
    - >-
      **Drop Price & STFU:** Then you state the price and shut the fuck up.
  anchor: >-
    To make the offer, we have to transition from discovery smoothly. We do this after we recapped all the problems.
  source: >-
    acq-closer-handbook.md, Offer, How to Make The Offer, lines 1991–2060
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1993"
- id: A-closer-026
  type: framework
  name: >-
    Map: Problem, Solution, Assure, Benefit, Confirm
  statement: >-
    Each problem is mapped in five beats — remind them of the problem, name the solution, assure it, state the benefit, ask for confirmation — and this is repeated for three solutions.
  why: >-
    Prospects change but the solutions stay the same, so labels, assurances and benefits can all be prepared ahead of time and the closer never has to invent anything on the fly.
  applies_when: >-
    Inside the offer; one problem is broken into micro problems to fill three solutions, more than three problems are grouped so one solution solves several.
  structure:
    - >-
      **Problem:** Remind them of their problem.
    - >-
      **Solution:** Tell them how we'll solve it specifically (think feature).
    - >-
      **Assure:** Tell them why that thing is great (decrease risk).
    - >-
      **Benefit:** Tell them the good stuff the solution gets them.
    - >-
      **Confirm:** Ask for confirmation.
  anchor: >-
    Connect their problems to our solutions, assurances, benefits, then confirm that it would help.
  source: >-
    acq-closer-handbook.md, Offer, How to Make The Offer, lines 2003–2024
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2003"
- id: A-closer-027
  type: framework
  name: >-
    The 5 Objections to Buying
  statement: >-
    Every reason not to buy chunks into five buckets — time, money, decision-maker, preference, stall — each with its own way of being solved.
  why: >-
    People may say a million different things to avoid buying, but five buckets can be prepared for and a million cannot.
  applies_when: >-
    Whenever the prospect is asked to buy and does anything other than buy.
  structure:
    - >-
      **#1 Time** - The prospect says they will not buy because they do not have the time to get the value.
    - >-
      #2 Money - The prospect says they are not able or not willing to pay the price.
    - >-
      #3 Decision-Maker - The prospect says they must get permission from somebody else before they can buy.
    - >-
      #4 Preference - The prospect says they expected something different or that they'd rather do something else.
    - >-
      #5 Stall - The prospect says they must wait before they will buy.
  anchor: >-
    People may say a million different things to avoid buying. But when you chunk it up there are only *five we care about*.
  source: >-
    acq-closer-handbook.md, Objections, The 5 Objections to Buying, lines 2080–2160
  confirmations: 1
  authors_caveat: >-
    Money accounts for roughly 50% of objections, by the author's own count at line 2101.
  anchor_at: "acq-closer-handbook.md:2080"
- id: A-closer-028
  type: framework
  name: >-
    The three steps for a Decision-Maker objection
  statement: >-
    A decision-maker objection is solved in three steps: find out ahead of time whether permission is needed and get that person on the call, ask whether they would approve based on past approvals and encourage deciding now, and book a follow up call with the decision-maker.
  why: >-
    If they would get approval anyway there is no reason to wait, and if they would not, the decision-maker has to be in the conversation.
  applies_when: >-
    The prospect says they must get permission from somebody else before they can buy.
  structure:
    - >-
      First, we figure out if they need permission ahead of time. If so, we get the decision-maker on the call.
    - >-
      Second, we ask if they think the decision-maker would feel ok with this based on past approvals. And if they'd get approval anyway, we encourage them to decide now.
    - >-
      Third, we book a follow up call with the decision-maker.
  anchor: >-
    We solve this in three steps. First, we figure out if they need permission ahead of time. If so, we get the decision-maker on the call.
  source: >-
    acq-closer-handbook.md, Objections, #3 Decision-Maker, lines 2113–2128
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2113"
- id: A-closer-029
  type: framework
  name: >-
    The three steps for a Preference objection
  statement: >-
    A preference objection is solved in three steps: remind them of the problem they want solved, pull out the short-, medium- and long-term consequences of their current ways, then explain why our way is ultimately to their benefit.
  why: >-
    The aim is to get them to realize that if we change the variables that create the outcome, we change the outcome.
  applies_when: >-
    The prospect says they expected something different or would rather do something else.
  structure:
    - >-
      first we remind them of the problem they want solved
    - >-
      Second, we pull out the short-, medium-, and long-term consequences of their current ways.
    - >-
      Third, we explain why the way we do it is ultimately to their benefit.
  anchor: >-
    To solve this, first we remind them of the problem they want solved. Second, we pull out the short-, medium-, and long-term consequences of their current ways.
  source: >-
    acq-closer-handbook.md, Objections, #4 Preference, lines 2130–2141
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2130"
- id: A-closer-030
  type: framework
  name: >-
    The Objection Loop
  statement: >-
    An objection is handled in three moves — acknowledge and agree with it, address it, ask for the sale again immediately — and the loop repeats on every further objection until they buy or time runs out.
  why: >-
    Adding to their reasoning and immediately giving them the chance to buy again saves them embarrassment; the salespeople who ask for the buy the most times get the most closes.
  applies_when: >-
    Every objection after the value of the product has been confirmed.
  structure:
    - >-
      **Acknowledge/Agree** with the objection.
    - >-
      **Address** the objection.
    - >-
      **Ask** for the sale *again. Immediately.*
    - >-
      Loop 4: ...Until you close
  anchor: >-
    Looping is a technique to overcome objections by acknowledging their objection, presenting your additions, and then *looping* the prospect back to the offer.
  source: >-
    acq-closer-handbook.md, Looping, The Right Way to Handle Objections, lines 2250–2343
  confirmations: 2
  authors_caveat: >-
    The objection itself is never insulted, only its content addressed; and if you are looping a lot it means you are messing up earlier in the script, since most sales close on the first and second asks.
  anchor_at: "acq-closer-handbook.md:2250"
- id: A-closer-031
  type: framework
  name: >-
    Handling the First Objection
  statement: >-
    The first objection is ignored: the closer first asks whether the product could get them closer to their goal, then asks a triage question to surface the real concern, and only then starts looping.
  why: >-
    Before getting into objection whack-a-mole you need to know whether they think the product is valuable; the triage question makes them abandon their reflex objection and isolates the one worth handling.
  applies_when: >-
    The first objection on a call, before any loop.
  structure:
    - >-
      Verify: Objection → (Acknowledge → Confirm Value)
    - >-
      **Confirming Value** — I completely hear you… do you mind if I ask you a question… Do you think doing [Product] is something that can help get you closer to [Goal]?
    - >-
      **Triage Question** — *Super helpful. What's the biggest thing holding you back... Tell me your main concern?*
  anchor: >-
    Before getting into objection whack-a-mole, we need to know something very important: Do they think our product is valuable?
  source: >-
    acq-closer-handbook.md, Looping, Handling the First Objection, lines 2264–2308
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2270"
- id: A-closer-032
  type: framework
  name: >-
    BAMFAM (Book A Meeting From A Meeting)
  statement: >-
    A call that does not close ends by booking the next call while still on this one, for one of three reasons: time constraint, dependence on a decision-maker, or banking delay.
  why: >-
    Sometimes closing takes more than one call; if you will not book a call while on a call, you have no chance of booking it by text afterwards.
  applies_when: >-
    Any call that runs out of time or cannot close today; give yourself a three minute buffer for it.
  structure:
    - >-
      Time Constraint
    - >-
      Prospect depends on Decision-Maker
    - >-
      Banking Delay (For very high ticket)
  anchor: >-
    And that's totally okay. Sometimes closing takes more than one call. When it does, secure a time for the next call while on the current call.
  source: >-
    acq-closer-handbook.md, BAMFAM, lines 2454–2466
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2458"
- id: A-closer-033
  type: framework
  name: >-
    Time Constraint BAMFAM In Action
  statement: >-
    The BAMFAM is booked in five beats: name the time problem and the value, offer two times, restate the day and objective, send the invite on the call and confirm receipt, then send a follow-up text right after.
  why: >-
    Both parties are there now, so the next meeting is secured on the spot instead of being left to follow up offline.
  applies_when: >-
    The last three minutes of a call that is running long, or when a decision-maker or banking delay blocks the close.
  structure:
    - >-
      We covered a lot of ground and our call's running long... I think this could really help you.
    - >-
      If Ran Out of Time: Let's pick this up tomorrow. Does [Time1] or [Time2] work?
    - >-
      Alright so on [DAY/TIME] we'll figure everything out.
    - >-
      I'm sending you an invite now. [Send invite] Let me know if you got it.
    - >-
      Immediate follow-up text: “Thank you for your time. Excited to talk soon 😊”
  anchor: >-
    When you start running out of time... You must secure the next call on the current call.
  source: >-
    acq-closer-handbook.md, BAMFAM, Time Constraint BAMFAM, lines 2464–2489
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2466"
- id: A-closer-034
  type: framework
  name: >-
    The Referral Process
  statement: >-
    Referrals are asked for in four steps: compliment the customer, ask who they know as successful as them, give them the exact words and a group chat, then ask for more.
  why: >-
    This is the least work per sale of anything in the handbook and the highest return on time; asking with a compliment means nobody is offended by it.
  applies_when: >-
    Right after closing and collecting payment, and whenever a customer sends anything positive by text.
  structure:
    - >-
      **Compliment them** - Tell them they're amazing to work with.
    - >-
      **Get introduction** - Then ask who they know as successful as them (a second compliment) that they'd want to come with them, which also improves their experience. Win-win.
    - >-
      **Give them words to use**: If they say yes, ask them to start a group chat.
    - >-
      Get more introductions – If you get one. Ask for more.
  anchor: >-
    Asking for referrals gets you the simplest, cheapest, fastest, easiest, highest-converting opportunities.
  source: >-
    acq-closer-handbook.md, Referrals, Referral Process, lines 2496–2524
  confirmations: 2
  authors_caveat: >-
    The author's own figures for this section: it should net one extra deal per day and over 30% of your sales come from it.
  anchor_at: "acq-closer-handbook.md:2503"
- id: A-closer-035
  type: framework
  name: >-
    The Script Bank (eleven scripts)
  statement: >-
    The method ships as eleven situation scripts covering outbound, inbound, the close, looping, the rebook, referrals, no-shows and the pipeline; the words are not edited, only performed.
  why: >-
    The scripts are the philosophy of the first part of the book tailored to specific use cases, and they operate together as parts of one larger sales process.
  structure:
    - >-
      Outbound Set Phone Script
    - >-
      Outbound No Pick Up Text Script
    - >-
      Outbound Reminder Text Script
    - >-
      Inbound Set Phone Script
    - >-
      Inbound Set Text Script
    - >-
      Closing Script
    - >-
      Looping Script
    - >-
      BAMFAM Script
    - >-
      Referral Text Script
    - >-
      No Show Script
    - >-
      Pipeline Phone & Text Script
  anchor: >-
    Learn them. Breathe them. And you’ll do great. The appendix includes the following scripts.
  source: >-
    acq-closer-handbook.md, Appendix: Script Bank, lines 2636–2663
  confirmations: 2
  authors_caveat: >-
    The author warns that some scripts appear to bend or break the rules of the first part: other parts of the process cover the missing variables, the brand has already done some of the selling, and different products need different scripting.
  anchor_at: "acq-closer-handbook.md:2646"
- id: A-closer-036
  type: framework
  name: >-
    ACQ Outbound Set Phone Script
  statement: >-
    A cold call to an opted-in lead runs intro, discovery of the constraint, a short offer of the appointment, and a close on a specific time, with a bank of prepared answers for the obstacles to booking.
  why: >-
    The setter's product is the appointment, so discovery chunks the problem and the offer is the twenty-minute call with a consultant rather than the product itself.
  applies_when: >-
    Outbound calls to unscheduled leads who opted into the marketing list.
  structure:
    - >-
      INTRO — [NAME]? ... Yeah this is [REP] getting back to you from [COMPANY NAME] on a recorded line
    - >-
      DISCOVERY — what...what had you kinda checking out... [LEAD MAGNET]?
    - >-
      [CHUNK UP PROBLEM #1] (?) ... Did I get that right?
    - >-
      Great. I guess out of those? if you could only tackle one of those opportunities...Which will have the most impact on the business?
    - >-
      OFFER — at a high level you get to work with [TEAM THAT HELPS SOLVE X PROBLEM]
    - >-
      CLOSE — would tomorrow morning? or afternoon? be better for you?
    - >-
      and just to confirm, can you be in a quiet spot? in front of a computer? at that time?
    - >-
      OBSTACLES TO BOOK A MEETING
  anchor: >-
    Yeah this is [REP] getting back to you from [COMPANY NAME] on a recorded line ... How've ya been?
  source: >-
    acq-closer-handbook.md, ACQ Outbound Set Phone Script, lines 2668–2993
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2678"
- id: A-closer-037
  type: framework
  name: >-
    Obstacles To Book A Meeting
  statement: >-
    Eight recurring reasons not to take the appointment each have a prepared answer that ends in asking again for the meeting.
  why: >-
    The setter's objections are known in advance, so the closer is never inventing an answer on the call.
  applies_when: >-
    A prospect resists booking the appointment on an outbound set call.
  structure:
    - >-
      "TOO EXPENSIVE"
    - >-
      "I DON'T KNOW MY CONSTRAINT"
    - >-
      **"MY BUSINESS IS NOT A GOOD FIT"**
    - >-
      **"THIS IS A BAD TIME" OR "CAN YOU SEND ME AN EMAIL?"**
    - >-
      **"I CAN'T LEAVE MY BUSINESS"**
    - >-
      I NEED TO SOLVE A BUSINESS PROBLEM FIRST
    - >-
      **BUSINESS IS BUSY RIGHT NOW**
    - >-
      **I ALREADY HAVE A SOLUTION**
  anchor: >-
    I hear ya... to be upfront—I wouldn’t be calling you if you did not meet the minimum—revenue mark.
  source: >-
    acq-closer-handbook.md, ACQ Outbound Set Phone Script, OBSTACLES TO BOOK A MEETING, lines 2822–2988
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2878"
- id: A-closer-038
  type: framework
  name: >-
    ACQ Outbound No Pick Up Text Script
  statement: >-
    After a double dial with no pickup, five text messages run in sequence — greeting and why they downloaded, a numbered bottleneck menu, recap and specifics, what they tried, a resource with a read confirmation — followed by three bumps.
  why: >-
    Texting continues the same discovery the call would have run, and the numbered menu makes a reply cheap for the prospect.
  applies_when: >-
    After you double dial and the prospect doesn't pick up.
  structure:
    - >-
      Message 1 — Hey [prospect name]! It's [name] from [company name]. What had you download the [lead magnet]?
    - >-
      Message 2 — What is the biggest bottleneck to growth? 1) Marketing 2) Sales 3) People 4) Profit 5) Something crazy
    - >-
      Message 3 — [recap] Why did you pick [problem category]? Be specific
    - >-
      Message 4 — Makes sense. [recap]. What have you tried so far to fix it? All the details help.
    - >-
      Message 5 — I have this resource here. I think it will help. [SALES LETTER PDF]
    - >-
      Follow up #1 — Any questions about this ^
    - >-
      Follow up #2 — Bumping ^
    - >-
      Follow up #3 — Did you see this video from Alex? Thought of you when I saw it.
  anchor: >-
    AFTER YOU DOUBLE DIAL AND THE PROSPECT DOESN'T PICKUP
  source: >-
    acq-closer-handbook.md, ACQ Outbound No Pick Up Text Script, lines 2994–3057
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2996"
- id: A-closer-039
  type: framework
  name: >-
    ACQ Outbound Reminder Text Script
  statement: >-
    A booked appointment is nurtured in a group chat opened by the setter and maintained by the closer, with a video hand-off, an end-of-day check, a morning-of message with a testimonial, an hour-before note and a scarcity nudge if there is no reply.
  why: >-
    Manual nurture has boosted show rates more than anything the author has seen across the portfolio.
  applies_when: >-
    Between the set and the close call.
  structure:
    - >-
      SDR starts a group chat; Closer is in charge of maintaining group chat after intro
    - >-
      SDR Intro Script — Here's the video as promised (it will help save time on your call tomorrow)
    - >-
      BC: (texts immediately after SDR) — Hey Name! Nice to meet you.
    - >-
      If no response (EOD): Hey name! Prepping for my meetings tomorrow. Did you have a chance to check out the video?
    - >-
      Morning of: Good morning X! Excited to talk today. ... TESTIMONIAL LINK
    - >-
      1 hour before: Talk soon.
    - >-
      If no reply: I have a few people who would like to take the X slot. Could you send a quick thumbs up if you want to keep it?
  anchor: >-
    Manual nurture has boosted show rates more than anything I have seen across our portfolio.
  source: >-
    acq-closer-handbook.md, ACQ Outbound Reminder Text Script, lines 3060–3124
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3064"
- id: A-closer-040
  type: framework
  name: >-
    ACQ Inbound Set Phone Script
  statement: >-
    As soon as an inbound lead books, they are double dialled and asked to hold the call right now; if they cannot, the rep takes thirty seconds of qualifying questions and confirms the video, and if they do not answer at all the texting script takes over.
  why: >-
    Pulling the call forward turns the freshest appointment into a close immediately, and the thirty-second questions make the scheduled call efficient.
  applies_when: >-
    The moment an inbound lead books a call.
  structure:
    - >-
      Double dial the lead when they opt-in.
    - >-
      Try to pull up the appointment, if they are able to have the meeting now. Transition into the close script.
    - >-
      If they do not answer, transition to the texting script.
    - >-
      IF THEY DON’T HAVE TIME: a quick 30 seconds — What type of business do you own? What’s revenue roughly? What has you interested in coming out to Vegas?
    - >-
      oh btw did you see that quick video from Alex after you booked?
    - >-
      After the call wraps, text: Hey Name! Great talking to you.
  anchor: >-
    I actually have some time now…would it be absolutely crazy if we just had our call now?
  source: >-
    acq-closer-handbook.md, ACQ Inbound Set Phone Script, lines 3130–3166
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3146"
- id: A-closer-041
  type: framework
  name: >-
    ACQ Inbound Set Text Script
  statement: >-
    When an inbound set does not pick up, three text blocks run — business, video, pull forward — each sent and waited on, followed by two non-response bumps, a cancel twelve hours out, and night-before and morning-of reminders.
  why: >-
    Each block is sent and waited on so the thread keeps the prospect answering, and the cancel text recovers the ones who never replied.
  applies_when: >-
    An inbound set that did not pick up the double dial.
  structure:
    - >-
      Block 1 — Excited to speak with you about the [PRODUCT]...what type of business do you own?
    - >-
      Block 2 — Btw - did you have a chance to check out the video from Alex?
    - >-
      Block 3 — I did actually have some time slots open today at X or Y if you're free?
    - >-
      NON-RESPONSE 1 — Just prepping for your meeting....could you check my previous message when you have a sec?
    - >-
      NON-RESPONSE 2 — I have someone requesting that time. Could you please send a quick bell so I can hold the spot?
    - >-
      CANCEL/RESCHEDULE TEXT — since I did not hear back, I've canceled our meeting. But, I know business owner life is busy...would you be free tomorrow by chance?
    - >-
      NIGHT BEFORE — Prepping for my meetings tomorrow.
    - >-
      MORNING OF — Talk today.
  anchor: >-
    Excited to speak with you about the [PRODUCT]...what type of business do you own?
  source: >-
    acq-closer-handbook.md, ACQ Inbound Set Text Script, lines 3170–3237
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3178"
- id: A-closer-042
  type: framework
  name: >-
    ACQ Closing Script
  statement: >-
    The close call runs intro with agenda and disclaimer, discovery of the business and its constraint, a stacked offer from three sources, one buying question, and then either the referral ask on a win or a BAMFAM on a loss.
  why: >-
    The script is the tool the kill skills are applied through: the same words in the same order get predictable responses.
  applies_when: >-
    Every scheduled close call.
  structure:
    - >-
      INTRO — [PROSPECT]! Hey it's [MYNAME] from [MYCOMPANY] calling about [PRODUCT] on a recorded line
    - >-
      we make no promises or guarantees of any rate of return or specific result
    - >-
      DISCOVERY — What had you book the call for [OUR PRODUCT]?
    - >-
      What's the biggest thing holding back growth? Marketing? Sales? People? Profit?...Something crazy?
    - >-
      OFFER — You're gonna get help solving. The key challenges. Of [CATEGORY]. And [CATEGORY]. From three different sources
    - >-
      CLOSE — Cool. So. Last question for you—you ready to come out to Vegas?
    - >-
      CLOSE WON: ASK FOR A REFERRAL
    - >-
      CLOSE LOST: BAMFAM - ONCE YOU COMPLETE LOOPS.
  anchor: >-
    [PROSPECT]! Hey it's [MYNAME] from [MYCOMPANY] calling about [PRODUCT] on a recorded line—how's it going?
  source: >-
    acq-closer-handbook.md, ACQ Closing Script, lines 3243–3429
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3253"
- id: A-closer-043
  type: framework
  name: >-
    The rapid fire metrics questions
  statement: >-
    After permission is asked, the metrics half of discovery runs as a fixed list of questions, each answer recapped before the next question is asked, ending with the constraint question.
  why: >-
    The block is announced as rapid fire to better understand the business and see if it is a fit, and every answer is recapped so the prospect keeps confirming.
  applies_when: >-
    The discovery phase of a close call, before the constraint question.
  structure:
    - >-
      Perfect. What's annual revenue?
    - >-
      Got it so [RECAP]. How about profit on that?
    - >-
      OK so [RECAP] and what's your main offer?
    - >-
      [RECAP]. Very cool. How are you currently getting clients for [RECAP]?
    - >-
      OK. Got it got it. So [RECAP]. How many new clients are you getting. Per month. On average?
    - >-
      OK so [RECAP]. And ballpark. How much do your clients spend with you?
    - >-
      OK so [RECAP] and how long have you owned [Business name]?
    - >-
      What's the biggest thing holding back growth? Marketing? Sales? People? Profit?...Something crazy?
  anchor: >-
    Great OK so I'm gonna rapid fire through a list of questions. Just to better understand the Business.
  source: >-
    acq-closer-handbook.md, ACQ Closing Script, DISCOVERY, lines 3317–3355
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3317"
- id: A-closer-044
  type: framework
  name: >-
    ACQ Looping Script
  statement: >-
    The looping script runs two steps: whatever they say, confirm the product can get them closer to their goal; then isolate and filter by confirming the real objection and asking whether anything else is holding them back, branching on how certain their answer sounded.
  why: >-
    Isolating one objection at a time is what makes it possible to move to a prepared overcome instead of arguing with a vague jumble.
  applies_when: >-
    Any objection on a close call.
  structure:
    - >-
      STEP #1: NO MATTER WHAT THEY SAY — Do you think doing [PRODUCT]? Is something that can help? get closer to [GOAL]?
    - >-
      STEP #2: ISOLATE THEN FILTER
    - >-
      "Yes I do, but [new objection]" — CONFIRM then ISOLATE, → Move to overcome in the script.
    - >-
      "Yeah.." (very uncertain tone) — PROBE: Hmm...you don't seem super confident—
    - >-
      IF THEY DON'T GIVE A SPECIFIC OBJECTION: PROBE: Well, what's your main— concern?
    - >-
      "Yes I do" (certain tone) — Love it…I’m curious…what makes you say that?
    - >-
      "I'M NOT SURE" — PROBE then ISOLATE, → Move to overcome below
  anchor: >-
    Other than [NEW OBJECTION]... is there anything else holding you back?
  source: >-
    acq-closer-handbook.md, ACQ Looping Script, lines 3433–3518
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3447"
- id: A-closer-045
  type: framework
  name: >-
    Timing Objections script
  statement: >-
    Two timing objections have prepared overcomes: feeling overwhelmed is met by naming the feeling, showing how the product deletes work, and asking again; needing to confirm a timeline is met by isolating it and letting them book now with the date movable later.
  why: >-
    The design of each step is presented as creating clarity by deleting what does not matter, which answers the time objection with time saved rather than time spent.
  applies_when: >-
    The prospect says they cannot find time to do what is required to get the outcome you promise.
  structure:
    - >-
      “I am overwhelmed/I have a lot going on right now”
    - >-
      What makes you feel overwhelmed?
    - >-
      We think of it as ‘how much can we delete?’ vs ‘how much can we add?’ Does that make sense?
    - >-
      “I need to confirm the timeline”
    - >-
      Other than confirming dates—is there anything else holding you back?
    - >-
      And if we need to move the date on the backend, we can 100% do that.
  anchor: >-
    The prospect says they cannot find time to do what is required to get the outcome you promise.
  source: >-
    acq-closer-handbook.md, Timing Objections, lines 3524–3559
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3526"
- id: A-closer-046
  type: framework
  name: >-
    Money Objections script
  statement: >-
    Five money objections have prepared overcomes, each starting by isolating the money as the only obstacle and then either running financial questions, reframing the price, offering another payment route, or returning to value.
  why: >-
    A high price is reframed as the reason they will take action, and the financial questions establish whether the money actually exists before the ask is repeated.
  applies_when: >-
    The prospect says they cannot afford what you're offering or don't see the value.
  structure:
    - >-
      "I see the value in it...I just don't have the money" — So if you had the money today. Would anything else prevent you from getting started?
    - >-
      What's monthly cash flow—give or take? ... and what's cash on hand again?
    - >-
      “It’s really expensive” — I think it’s good that it’s a lot...it means you’ll actually care and be more likely to take action.
    - >-
      “I need to get another card OR I need to wait until payroll is clear” — IF they have money → ASK FOR THE SALE; IF they don't → What's the timeline look like for you? BAMFAM
    - >-
      “I don’t have the card I want to use with me” — do you ever use tap to pay? ... we can also do a quick bank transfer
    - >-
      “I just don’t know if I see the value” — earlier you mentioned you consumed [CONTENT]— what has that done for you so far?
  anchor: >-
    The prospect says they cannot afford what you're offering or don't see the value.
  source: >-
    acq-closer-handbook.md, Money Objections, lines 3564–3684
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3566"
- id: A-closer-047
  type: framework
  name: >-
    Decision-Maker script
  statement: >-
    The spouse or partner objection is worked by isolating it, asking what the other person's biggest concern would be, looping that concern, offering a personal guarantee to handle it, asking for the order, and falling back to a BAMFAM with the decision-maker.
  why: >-
    The concern behind the permission is itself an objection that can be looped, so the closer handles it rather than waiting for a conversation he is not part of.
  applies_when: >-
    The prospect says they cannot make the decision without someone else's permission or input.
  structure:
    - >-
      Got it...other than talking with her/him....is there anything holding you back?
    - >-
      Got it, just out of curiosity—what would be their biggest concern?
    - >-
      → IDENTIFY & GO THROUGH SPECIFIC OBJECTION LOOP
    - >-
      Then if your [SPOUSE/BUSINESS PARTNER] absolutely hates the idea ... then you can give me a call and I will make sure you are taken care of—fair enough? → ASK FOR ORDER
    - >-
      IF STILL A NO → Well, what if she/he says no?
    - >-
      IF "I need to talk to them" → ...When would you be able to chat with them? (BAMFAM)
  anchor: >-
    The prospect says they cannot make the decision without someone else's permission or input.
  source: >-
    acq-closer-handbook.md, Decision-Maker, lines 3689–3734
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3691"
- id: A-closer-048
  type: framework
  name: >-
    Preferences script
  statement: >-
    Five preference objections are each answered by asking permission to explain how the product is structured and then showing that the structure already solves their preference, ending in the ask.
  why: >-
    The answer to a preference is a change of the variables that create the outcome, which here means describing the format rather than arguing with the preference.
  applies_when: >-
    The prospect says they don't like something specific about your product, service, or approach.
  structure:
    - >-
      “I don’t think I can learn in that big of a group” — Do you mind if I share how we structure the [PRODUCT]?
    - >-
      “How is this different than the free content?” — free content tells you what to do; the [PRODUCT] shows you how to do it—specifically for your business
    - >-
      "I went to a similar [PRODUCT] and I didn't like it" — how many people were at those events? ... did you get to work with and get personalized help from the speakers?
    - >-
      "I'm too small for this" — we group you with businesses of similar size, so everything is directly relevant
    - >-
      "I'm too big for this" — Long story short. We group you by revenue.
  anchor: >-
    The prospect says they don't like something specific about your product, service, or approach.
  source: >-
    acq-closer-handbook.md, Preferences, lines 3739–3823
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3741"
- id: A-closer-049
  type: framework
  name: >-
    Stall Objections script
  statement: >-
    A stall is answered by being upfront that a stall is really one of two reasons, value or logistics, by contrasting how decisive buyers make quick logical decisions when they see value, or by naming the nervousness and turning it into a reason to start.
  why: >-
    Naming the two real reasons forces the prospect to pick one, and a prospect who is nervous about the size of the commitment is the one most likely to take it seriously.
  applies_when: >-
    The prospect says they need more time to consider the decision without giving a specific reason.
  structure:
    - >-
      “I need to think about it” — Do you mind if I’m upfront with you?
    - >-
      They don’t see the value… I mean do you see it? Cool I’m confident this will help.
    - >-
      Logistically they need to make sure it will work…
    - >-
      “I always take 24 hours to make a decision” — is there any new information that’s making you reconsider?
    - >-
      Exactly, and so because we do see the value. Would it be absolutely crazy if we break the rule?
    - >-
      “I just need some time to think about it…it’s a big commitment/decision” — do you feel maybe a bit nervous…it being a big decision?
  anchor: >-
    The prospect says they need more time to consider the decision without giving a specific reason.
  source: >-
    acq-closer-handbook.md, Stall Objections, lines 3829–3875
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3831"
- id: A-closer-050
  type: framework
  name: >-
    ACQ BAMFAM Script
  statement: >-
    A booked follow-up is nurtured with three texts — five minutes after the call, the night before, the morning of — plus a value message if the meeting is more than three days out.
  why: >-
    The five-minute text leaves a positive feeling after the conversation, and a long gap is filled with proof rather than silence.
  applies_when: >-
    Between a BAMFAM being booked and the follow-up meeting.
  structure:
    - >-
      Text #1: 5 min follow up — so great talking with you. Excited to continue the conversation & potentially do business together. We can help.
    - >-
      Text #2: Night before — Looking forward to our meeting tomorrow.
    - >-
      Text #3: Morning of — Talk today :)
    - >-
      IF BOOKED MORE THAN 3-DAYS — 1) Testimonial 2) 3rd party video review 3) Value video from YouTube
  anchor: >-
    When you BAMFAM a meeting. Use this to nurture the appointment in between meetings.
  source: >-
    acq-closer-handbook.md, ACQ BAMFAM Script, lines 3880–3916
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3882"
- id: A-closer-051
  type: framework
  name: >-
    ACQ Referral Text Script
  statement: >-
    The referral is followed up the day after the sale with one question, a group chat if they say yes, and a two-message opener in the chat that ends by offering the referral two times.
  why: >-
    The group chat is the easiest way for the customer to make the introduction, and the chat opener goes straight to booking.
  applies_when: >-
    The day after someone signs up, or whenever the referral ask was missed on the call.
  structure:
    - >-
      Post-Sale Script — did you know any other amazing business owners who might benefit from [PRODUCT]?
    - >-
      IF YES: Do you mind putting us in a group chat together? That's typically the easiest way.
    - >-
      IF NO: No worries!! Feel free to holler at me when you do :)
    - >-
      Referral Group Chat Script — Thanks for connecting us! Great to meet you [REFERRAL NAME].
    - >-
      Do you have time this afternoon at [X TIME] or tomorrow at [Y TIME]?
  anchor: >-
    Day after someone signs up & they agreed to give a referral OR if you did not ask and need to follow up.
  source: >-
    acq-closer-handbook.md, ACQ Referral Text Script, lines 3921–3941
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3923"
- id: A-closer-052
  type: framework
  name: >-
    ACQ No Show Script
  statement: >-
    A no-show is worked in three steps: a text immediately after the double dial, a second text with two reschedule times five minutes later, and the lead moved into the end-of-day outbound block if there is still no answer.
  why: >-
    The missed slot is recovered the same day rather than written off, and a pickup drops straight back into the outbound set script.
  applies_when: >-
    After you double dial with no response at the scheduled time.
  structure:
    - >-
      Immediately send: "Hey [NAME], just tried your cell. Ready to rock?"
    - >-
      If no response in 5min, send "I know business owner life is busy...Happy to find another time. I have some openings tomorrow at [TIME] or [TIME]? Either of those work to reschedule?"
    - >-
      Add these to your outbound block at the end of the day if you do not get responses. If they pick up → OUTBOUND SET PHONE SCRIPT
  anchor: >-
    AFTER YOU DOUBLE DIAL WITH NO RESPONSE AT SCHEDULED TIME.
  source: >-
    acq-closer-handbook.md, ACQ No Show Script, lines 3970–3980
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3972"
- id: A-closer-053
  type: framework
  name: >-
    ACQ Pipeline Phone & Text Script
  statement: >-
    A stalled or ghosting prospect is called first and then texted in five escalating steps: the five-minute follow up, value messages, check-ins, bumps, and a re-offer.
  why: >-
    The goal is to close the deal or agree on a timeline to touch base again, so each step gives the prospect a new reason to reply rather than repeating the ask.
  applies_when: >-
    A deal waiting on something off the call with no BAMFAM secured, or a prospect who has ghosted.
  structure:
    - >-
      Phone Script — wanted to touch base around [OBSTACLE THAT IS PREVENTING THE DEAL FROM MOVING FORWARD] How’s it going there? → Transition into objection overcomes/looping.
    - >-
      STEP #0: 5-MIN FOLLOW UP
    - >-
      STEP #1: VALUE MESSAGES — just saw this case study of [COMPANY SIMILAR TO THEIRS] who solved [THEIR SPECIFIC PROBLEM]
    - >-
      STEP #2: CHECK-INS — how are you feeling about [next steps/decision]?
    - >-
      STEP #3: BUMPING — should I assume this isn't a priority right now?
    - >-
      STEP 4: RE-OFFER/RE-ENGAGE — just had 3 spots open up for [DATES]. Want first dibs before I announce it?
  anchor: >-
    Start by calling. If they do not answer, transition to text. The goal is to close the deal or agree on a timeline to touch base again.
  source: >-
    acq-closer-handbook.md, ACQ Pipeline Phone & Text Script, lines 3987–4052
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3994"
```
