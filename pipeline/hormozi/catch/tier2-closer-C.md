# Улов фазы 1 — ACQ Closer Handbook (2025) (ярус 2), тип C: разборы (кейсы)

Группа `tier2-closer`, слаг `closer`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **59** (экстрактор вернул 59, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `acq-closer-handbook.md` | 1–4125 | 5 | 59 |

## Как собран файл

Экстрактор C (Application cases) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-closer.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-closer-C.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 1; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: C-closer-001
  type: case
  name: >-
    "John." versus "John?"
  statement: >-
    The same single word is run twice, once as a flat statement and once with the pitch raised at the end, and the raised-pitch version is shown to carry the work of a whole sentence ("Hello, am I speaking with John?") while the flat version leaves the meaning to the prospect.
  why: >-
    Tone gives a word its job; a group of words does not become a question on its own, the rise in pitch at the end is what makes it one, and packing many words' job into one word is what makes a closer efficient.
  demonstrates: >-
    The tone rule that pitch rises at the end wherever the script shows a question mark; "Better Jobs = Fewer Words = Efficient Closing".
  anchor: >-
    Ex: “John?” —This is more than just a name. You also know *exactly* what it means.
  source: >-
    acq-closer-handbook.md, Tone, lines 1619-1625
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1621"
- id: C-closer-002
  type: case
  name: >-
    "I didn't say he hit his wife" pause exercise
  statement: >-
    One identical seven-word sentence is written out seven times, each time with the pause placed after a different word, and each placement is given its changed meaning ("Somebody else said it", "I did nothing of the sort", and so on).
  why: >-
    Nothing changes but where the closer stops talking, so the exercise proves that pauses alone reassign the job of the words around them and focus attention on what was just said.
  applies_when: >-
    Practising pauses; the reader is told to read each sentence out loud, pause after the dashed word, and soak in what happened.
  demonstrates: >-
    The three pause lengths (short, medium, long) and the claim that pauses focus attention on the word just said.
  anchor: >-
    I—didn’t say he hit his wife. → Somebody else said it
  source: >-
    acq-closer-handbook.md, Tone, lines 1629-1646
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1638"
- id: C-closer-003
  type: case
  name: >-
    Pauses In Action — the fit line
  statement: >-
    One line of the opening frame is printed with its pauses marked, then broken down clause by clause: the pauses after FIT, AND and IF SO are shown to say "we will make you an offer only if you are a fit" without the closer ever saying it.
  why: >-
    Placing the pauses makes the point as obvious as screaming it while the closer stays professional and chill.
  demonstrates: >-
    Pauses focus attention; the conditional frame of the introduction.
  anchor: >-
    I just want to make sure our product is a fit...And—if so—I’m happy to walk you through it.
  source: >-
    acq-closer-handbook.md, Tone, lines 1680-1696
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1682"
- id: C-closer-004
  type: case
  name: >-
    The girl that got away
  statement: >-
    A deliberately absurd four-line opening ("This is the girl that got away / Calling from my bed / Because I know we had something special / I've set up a camera for us to watch later... you got 20 minutes?") is dissected to show it contains exactly the four elements the law requires — identity, where the call comes from, the reason for the call, and that it is recorded — and that the format therefore cannot be what kills calls.
  why: >-
    If the same four elements work in that opening, then bad experiences with the compliant opening come from the prospect not liking or trusting the rep, the company or the reason for the call, not from the format itself.
  demonstrates: >-
    The four things every call must open with; the rejection of "it sounds like a sales call" as a reason to skip them.
  anchor: >-
    I guarantee he'd continue into the discovery phase (Ahem.) But, more importantly it has her identity, where she calls from, the reason she calls, and that the call is recorded.
  source: >-
    acq-closer-handbook.md, Introduction, lines 1752-1775
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1765"
- id: C-closer-005
  type: case
  name: >-
    INTRO IN ACTION
  statement: >-
    The whole introduction is shown as three beats: name plus company plus product plus recorded line plus "how's it going?", then the time box ("We only have 20 minutes though. Cool if we jump in?"), then the agenda — metrics to check fit, walk through the product if a fit, set up if it makes sense — each closed with a confirmation question.
  why: >-
    The intro frames the rest of the call and can be blown in thirty seconds; minutes wasted at the start are minutes wanted at the end, and a long intro can cost the sale and the referral with it.
  applies_when: >-
    The first 30-60 seconds of every call.
  demonstrates: >-
    Minimum required questions, minimum required words, proper tone; the conditional fit frame.
  anchor: >-
    We'll just spend a couple minutes diving through your metrics to make sure you're a fit... And—if so—happy to walk you through [PRODUCT]... and if things make sense we can get you all set up.
  source: >-
    acq-closer-handbook.md, Introduction, lines 1786-1804
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1801"
- id: C-closer-006
  type: case
  name: >-
    Recapping, Labeling, and Confirming Put Together
  statement: >-
    One worked line shows the three steps in a row: the problem repeated in the prospect's words ("not getting as many leads as you want"), then stated in the seller's label ("some marketing issues"), then checked ("Does that sound about right?").
  why: >-
    Every problem the prospect has should be mapped to a solution the seller offers, and the label is the word that will be carried into the offer, so it has to be confirmed as correct before the offer is built on it.
  demonstrates: >-
    Steps 6-8 of the 9 Steps of Discovery and the five labels (Marketing, Sales, Product/Delivery, People, Profit).
  anchor: >-
    So you're [not getting as many leads as you want] **Label** - It sounds like you've got some marketing issues. **Confirm** - Does that sound about right?
  source: >-
    acq-closer-handbook.md, Discovery, line 1940
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1940"
- id: C-closer-007
  type: case
  name: >-
    Final Recap (Stacking the Pain)
  statement: >-
    The stacked recap is shown with real material — three agencies tried, $50K spent, leads that did not convert, hesitancy to invest again — then relabelled one level up ("the real issue isn't just vendors, ads, and leads - it's that you need an entirely new marketing and sales process") and confirmed.
  why: >-
    The closer is just sharing what was learned and making sure the prospect agrees; agreement on the stacked pain is what makes it time to offer.
  applies_when: >-
    After the Pain Cycles are complete and before the offer.
  demonstrates: >-
    Stacking the pain; Recap-Label-Confirm applied to several problems at once.
  anchor: >-
    To make sure I understand. You tried three different marketing agencies, spent $50K, got leads that didn’t convert, and now you’re hesitant to invest again.
  source: >-
    acq-closer-handbook.md, Discovery, lines 1956-1964
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1960"
- id: C-closer-008
  type: case
  name: >-
    Mapping one problem: "Not enough leads"
  statement: >-
    A single labelled problem is carried through the five sub-steps with concrete wording for each: Problem ("For your 'Not enough leads' issue..."), Solution (you get to ask questions of our director of marketing), Assure (he leads ad and content strategy for the companies we advise), Benefit (he can help you improve your funnel conversion, content, ads), Confirm ("Do you think that would help?").
  why: >-
    Listing benefits and asking for money abandons the pain points the discovery produced; mapping each problem to a named solution with an assurance and a benefit is what makes the offer personal on the spot.
  demonstrates: >-
    Step 2 (Map) of the offer-making process: Problem, Solution, Assure, Benefit, Confirm.
  anchor: >-
    **Solution:** Tell them how we'll solve it specifically (think feature). Ex: *When you come out, you'll get to ask questions to our director of marketing.*
  source: >-
    acq-closer-handbook.md, Offer, lines 2005-2013
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2007"
- id: C-closer-009
  type: case
  name: >-
    A COMPLETELY STACKED OFFER: PLUG AND CHUG
  statement: >-
    The full offer is laid out as a fill-in template: transition and permission, then solution 1 with assurance and benefit and a confirmation question, then solutions 1+2 restated, then 1+2+3 restated, then the whole stack repeated from three angles, then the buying question, then the price and the card menu.
  why: >-
    Labels, solutions, assurances and benefits are all known in advance, so a prepared closer never has to invent anything on the fly and risk saying something dumb or wrecking the tone.
  applies_when: >-
    Roughly two minutes and about 320 words at 150-170 words per minute.
  demonstrates: >-
    Transition, Map, Stack (three times), Ask, Drop Price & STFU.
  anchor: >-
    So given [Problem(s)]... it looks like you’ll get the most from [Solution1]. It’s [Assurance1] so you can [Benefit1]... How does that sound?
  source: >-
    acq-closer-handbook.md, Offer, lines 2026-2057
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2044"
- id: C-closer-010
  type: case
  name: >-
    The "Gotcha" Moment
  statement: >-
    A door-to-door dialogue is run to failure — the rep answers "can't afford it" by pointing at the BMW and the new deck, the prospect says "I think we're done here", the door slams — and the manager then supplies the replacement line, "That's a fair point. What would need to happen for this to make sense financially?", as the same goal with no confrontation.
  why: >-
    Even when the excuse is false, challenging it directly calls the prospect a liar to his face; he feels foolish and attacked and now has a good objection, so catching prospects in their objections feels clever but the only one who thinks so is the closer.
  demonstrates: >-
    The wrong way to handle objections; agree and add rather than contradict.
  anchor: >-
    You made him feel foolish and attacked. You could have said, ‘That’s a fair point. What would need to happen for this to make sense financially?’
  source: >-
    acq-closer-handbook.md, Looping, lines 2179-2199
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2197"
- id: C-closer-011
  type: case
  name: >-
    Confirming Value
  statement: >-
    The first objection is answered by ignoring its content: the closer acknowledges, asks permission for one question, and asks whether doing the product is something that can help get the prospect closer to their stated goal.
  why: >-
    Before playing objection whack-a-mole the closer has to know whether the prospect thinks the product is valuable at all; the reflex objection gets abandoned and the objection worth handling is isolated.
  applies_when: >-
    The first objection of the call, whatever it is.
  demonstrates: >-
    Verify: Objection -> (Acknowledge -> Confirm Value) in the Objection Looping Framework.
  anchor: >-
    I completely hear you… do you mind if I ask you a question… Do you think doing [Product] is something that can help get you closer to [Goal]?
  source: >-
    acq-closer-handbook.md, Looping, lines 2272-2280
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2277"
- id: C-closer-012
  type: case
  name: >-
    Triage Question
  statement: >-
    Whatever the prospect answers to the value question, the closer follows with one triage question that asks for the biggest thing holding them back and their main concern.
  why: >-
    The main objective is to get the prospect to abandon the reflex objection so the objection actually worth handling is isolated.
  demonstrates: >-
    Isolating the objection before looping.
  anchor: >-
    *Super helpful. What's the biggest thing holding you back... Tell me your main concern?*
  source: >-
    acq-closer-handbook.md, Looping, lines 2282-2293
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2291"
- id: C-closer-013
  type: case
  name: >-
    Objection Looping In Action, Loop 1 (timing)
  statement: >-
    Objection "This isn't a good time" is met with "That makes sense", then addressed by restructuring the commitment ("What if we structured this so it only took 30 minutes a day? Would that work for you?"), then immediately followed by the ask, "Great, let's do that."
  why: >-
    The loop is not finished until the sale is asked for again; agreement buys the closer another opportunity to ask.
  demonstrates: >-
    Loop: Objection -> (Acknowledge/Agree -> Address -> Ask); the Time objection solved by making it a priority question rather than a quantity-of-time question.
  anchor: >-
    **Address:** What if we structured this so it only took 30 minutes a day? Would that work for you? [They agree]
  source: >-
    acq-closer-handbook.md, OBJECTION LOOPING IN ACTION, lines 2325-2329
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2328"
- id: C-closer-014
  type: case
  name: >-
    Objection Looping In Action, Loop 2 (money)
  statement: >-
    Objection "This is just too expensive" is met with "Super reasonable", then addressed by weighing the cost against a year of trial and error, then closed with "Perfect, let's get started then."
  why: >-
    A money objection is solved by showing how much the problem costs compared with the solution, and the ask follows immediately so the prospect is never left in the objection.
  demonstrates: >-
    Acknowledge -> Address -> Ask on the Money objection.
  anchor: >-
    **Address:** If talking to our team of experts saves you a year of trial and error, would it be worth it? [They agree]
  source: >-
    acq-closer-handbook.md, OBJECTION LOOPING IN ACTION, lines 2331-2335
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2334"
- id: C-closer-015
  type: case
  name: >-
    Objection Looping In Action, Loop 3 (decision-maker)
  statement: >-
    Objection "I have to ask my wife. She's the boss around here" is met with "Makes sense about your wife", then addressed by including her in the onboarding call, then closed with "Excellent, let's get you all set up."
  why: >-
    Top closers handle five, ten, even fifteen objections in a single call because they agree and add rather than contradict, and stay in the loop until they reach agreement.
  demonstrates: >-
    Acknowledge -> Address -> Ask on the Decision-Maker objection.
  anchor: >-
    **Address:** What if we included her in the onboarding call so she's fully informed? Would that address her concerns? [They agree]
  source: >-
    acq-closer-handbook.md, OBJECTION LOOPING IN ACTION, lines 2337-2343
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2340"
- id: C-closer-016
  type: case
  name: >-
    Breaking a vague objection into examples
  statement: >-
    "I don't think this will work for me" is answered with the two stalling questions — tell me more about that, give me an example — and the specific answer that comes back is then corrected as a misunderstanding and closed with "Does that clear that up?".
  why: >-
    The two questions buy the closer time and force the prospect to do the thinking, and they break a vague jumble of words into specific objections that can be tackled one at a time.
  applies_when: >-
    Whenever a prospect says something the closer is not sure how to respond to.
  demonstrates: >-
    Pull Teeth applied to objections; isolating objections and buying time.
  anchor: >-
    *I don't think this will work for me → Can you tell me more about that? Can you give me an example?
  source: >-
    acq-closer-handbook.md, Looping, Pro Tip, line 2357
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2357"
- id: C-closer-017
  type: case
  name: >-
    AGREE... AND... worked three ways
  statement: >-
    Three objections are answered in the same shape — price ("It's a lot... I agree... and... I think it'll be totally worth it for your business... do you agree?"), time (too much going on is turned into the best reason to come), format (the group objection is answered with six chances to ask individual questions) — each ending in a confirmation question.
  why: >-
    The acknowledgement shows the closer heard them and sees a nugget of truth in their reason, which disarms a prospect who expects an argument; "and" keeps the prospect's words standing, where "but" works like a big fat eraser on everything said before it.
  demonstrates: >-
    Acknowledge/Agree with "and", never "but"; add to their reasoning, then ask again.
  anchor: >-
    I’ve got too much going on… super fair… and… that’s probably the best reason for coming out—so we can help you get less busy… hows that sound?
  source: >-
    acq-closer-handbook.md, Looping, lines 2359-2380
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2378"
- id: C-closer-018
  type: case
  name: >-
    Three closes that answer nothing
  statement: >-
    Three lines are given that can follow any reason a prospect gives — that is the exact reason you should come; most people just make it work anyways; best case you xyz, worst case you zyw — and the author points out they do not answer the objection at all, they only agree and ask again.
  why: >-
    On the author's own account the response given matters almost not at all; what matters is being able to ask again, which is why agreement is the point.
  authors_caveat: >-
    The author marks this as controversial and frames it as wanting the reader to be rich rather than right.
  demonstrates: >-
    Agreement exists to buy more opportunities to ask for the sale.
  anchor: >-
    … let’s just think about it like this “best case” you xyz, worst case you zyw. How’s that sound?
  source: >-
    acq-closer-handbook.md, Looping, lines 2384-2394
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2392"
- id: C-closer-019
  type: case
  name: >-
    Time Constraint BAMFAM In Action
  statement: >-
    The unclosed call is ended in five moves: name the time overrun and say it could really help, offer two named times (branching on whether the block was time, a decision-maker or a banking delay), restate the agreed day and time, send the invite while still on the call and have them confirm receipt, then send an immediate follow-up text.
  why: >-
    Both parties are on the call now, so a closer who will not book a call while on a call has no chance of booking one by text afterwards; "do not say we'll follow up offline".
  applies_when: >-
    The close needs more than one call because of a time constraint, a decision-maker or a banking delay; give yourself a three minute buffer.
  demonstrates: >-
    BAMFAM — Book A Meeting From A Meeting.
  anchor: >-
    If Decision-Maker or Banking Delay: Do you think you'll get that taken care of today or tomorrow? Great. Let's pick this up then.
  source: >-
    acq-closer-handbook.md, BAMFAM, lines 2473-2483
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2479"
- id: C-closer-020
  type: case
  name: >-
    Time Constraint Overcomes
  statement: >-
    Three evasions about scheduling are each given a reply that keeps a specific time on the table: "I'm not sure when I'll be free" is answered by working around their morning, "I'll have to see" by asking for fifteen minutes tomorrow, "Let me call you back" by offering today or tomorrow at X and Y.
  why: >-
    Securing the next call on the current call is what keeps the deal moving; a vague agreement to follow up later is not a booking.
  demonstrates: >-
    BAMFAM; offering two named times rather than asking for availability in the abstract.
  anchor: >-
    “Let me call you back” → “Totally... when do you want to do that... today or tomorrow... I’ve got time at X & Y.”
  source: >-
    acq-closer-handbook.md, BAMFAM, lines 2485-2489
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2489"
- id: C-closer-021
  type: case
  name: >-
    Give them words to use
  statement: >-
    Instead of leaving the introduction to the customer, the closer dictates the exact message for the group chat, naming the event, the invitation and the rep, and ending with "I'll let you guys take it from here."
  why: >-
    Handing the customer a line to copy and paste removes the work of composing an introduction and keeps the rep's credibility inside the referrer's own words.
  applies_when: >-
    Step 3 of the referral process, once the customer has agreed to introduce someone.
  demonstrates: >-
    The four-step Referral Process: compliment, get introduction, give them words to use, get more introductions.
  anchor: >-
    Tell them to say: “I’m going to Alex Hormozi’s scaling workshop in Vegas. Thought you might want to come. This is [Salesman name] - he’s been great.
  source: >-
    acq-closer-handbook.md, Referrals, lines 2505-2518
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2516"
- id: C-closer-022
  type: case
  name: >-
    Referrals In Action
  statement: >-
    Straight after payment the ask runs as compliment ("you're the exact type of business owner we love to work with"), then the introduction request phrased as a second compliment ("who else do you know who's as successful as you"), backed by a reason — a few spots left on that date — then the group text, then "anyone else come to mind?".
  why: >-
    Referrals are the simplest, cheapest, fastest, easiest, highest-converting opportunities and should net an extra deal a day; business owners are not offended by the ask, especially when it comes with a compliment.
  applies_when: >-
    Right after closing and collecting payment, or after a customer sends anything positive by text.
  demonstrates: >-
    The Referral Process and the claim that over 30% of sales come from referrals.
  anchor: >-
    **Get Introduction:** Who else do you know who’s as successful as you that would benefit from this? I ask because we have a few spots left on that date and I’d love to fill it with a couple people you know.
  source: >-
    acq-closer-handbook.md, Referrals, lines 2526-2535
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2530"
- id: C-closer-023
  type: case
  name: >-
    The downgrade ask after a no
  statement: >-
    When the customer cannot think of anyone as successful as them, the closer blames the founder for making him ask and lowers the bar to a business owner less successful than them, before moving on.
  why: >-
    One refusal to name a peer does not end the referral attempt; a second, easier ask costs nothing because the compliment has already been paid.
  demonstrates: >-
    Step 4 of the Referral Process, keep asking for more introductions.
  anchor: >-
    **IF NO:** Alright—and you know Alex would kill me if I didn’t ask… so how about a business owner less successful than you? (haha)”
  source: >-
    acq-closer-handbook.md, Referrals, line 2534
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2534"
- id: C-closer-024
  type: case
  name: >-
    ACQ Outbound Set Phone Script
  statement: >-
    Skeleton for calling an opted-in lead: intro (name, company, recorded line, how've ya been), permission ("Is now a terrible time for a quick chat?"), discovery on the lead magnet and the biggest focus point, chunk up and confirm the problems, pick the one with most impact, dig into what has been tried and what solving it unlocks, confirm revenue, ask permission to share, a high-level offer of a 20 minute call with a consultant, then time zone, two time options, confirmation that they will be in a quiet spot at a computer, the text permission and the pre-call video.
  why: >-
    Outbound is how a closer creates opportunities; the appointment, not the sale, is the objective of this call and the script keeps it to about three minutes of the prospect's time.
  applies_when: >-
    Outbound Priority 2, calling unscheduled opt-ins from newest to oldest, two sets an hour.
  demonstrates: >-
    Intro, Discovery, Offer, Close sequence applied to setting rather than closing.
  anchor: >-
    I saw that you had checked out [lead magnet] [today/this week/this month]? Is now a terrible time for a quick chat?
  source: >-
    acq-closer-handbook.md, ACQ Outbound Set Phone Script, lines 2668-2820
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2682"
- id: C-closer-025
  type: case
  name: >-
    Chunking up three problems on a set call
  statement: >-
    A prospect's scattered answers are read back as a numbered list with a label on each — more leads becomes a marketing constraint, not having the right people on the bus becomes a people constraint, compressing margin is lumped as strategy — checked with "did I get that right?", then narrowed by asking which one, if only one could be tackled, would have the most impact on the business.
  why: >-
    Business owners describe problems in a million ways, and the seller describes them in a handful of labels that map to what is offered; confirming the labels is what makes the recap usable later.
  demonstrates: >-
    Recap, Label, Confirm on several problems at once, then prioritising one.
  anchor: >-
    Example: "So it sounds like you are dealing with a few things...number 1...you need more leads...so a marketing constraint...
  source: >-
    acq-closer-handbook.md, ACQ Outbound Set Phone Script, lines 2716-2730
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2727"
- id: C-closer-026
  type: case
  name: >-
    "TOO EXPENSIVE" on a set call
  statement: >-
    The objection is first split into budget or value ("is it more of a budget thing? ...or if you saw the value... would you consider it?"); a value answer continues the script, a budget answer opens permission for financial questions — monthly cash flow, then cash on hand — and at $15K cash or $10K a month of cash flow the rep says there might be a way to make it work and asks to set the consultant call.
  why: >-
    Splitting the objection turns an unanswerable "too expensive" into either a value conversation the script already handles or a factual question about money that has a threshold answer.
  demonstrates: >-
    Isolating an objection before overcoming it; the Money objection.
  anchor: >-
    hmmm, is it more of a budget thing? ...or if you saw the value in the [PRODUCT]... would you consider it?
  source: >-
    acq-closer-handbook.md, ACQ Outbound Set Phone Script, OBSTACLES TO BOOK A MEETING, lines 2824-2853
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2826"
- id: C-closer-027
  type: case
  name: >-
    "I DON'T KNOW MY CONSTRAINT"
  statement: >-
    A prospect who cannot name their problem is handed a closed menu — marketing, sales, people, profit, or operations — and if they still say they are not sure, asked which single fix in the business would drive the most growth.
  why: >-
    A forced choice from a short list produces the labelled problem the rest of the script needs, where an open question produced nothing.
  demonstrates: >-
    Labelling the problem; the same five-way menu used in the Closing Script's constraint question.
  anchor: >-
    Hmm....If you had to say it was one of— marketing, sales, people, profit, or operations... which would it be?
  source: >-
    acq-closer-handbook.md, ACQ Outbound Set Phone Script, lines 2855-2867
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2857"
- id: C-closer-028
  type: case
  name: >-
    "MY BUSINESS IS NOT A GOOD FIT"
  statement: >-
    The rep answers the fit doubt with the fact that the call would not be happening below the minimum revenue mark, then hands the fit decision to the consultant call and asks permission to explore it.
  why: >-
    The prospect's self-disqualification is replaced with a criterion he has already met, and the judgement is moved to the next step instead of being argued on the call.
  demonstrates: >-
    Agree and add, then ask again; the appointment as the objective of a set call.
  anchor: >-
    I hear ya... to be upfront—I wouldn’t be calling you if you did not meet the minimum—revenue mark.
  source: >-
    acq-closer-handbook.md, ACQ Outbound Set Phone Script, line 2878
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2878"
- id: C-closer-029
  type: case
  name: >-
    "THIS IS A BAD TIME" or "CAN YOU SEND ME AN EMAIL?"
  statement: >-
    The rep concedes the later option, then prices the call in time ("this call only takes about 3 minutes") and asks to knock it out now; a yes continues the script, a no becomes a BAMFAM with a specific callback time.
  why: >-
    Naming a small, specific length turns an open-ended request for attention into a decision the prospect can say yes to immediately.
  demonstrates: >-
    Agree and add, then ask again; BAMFAM as the fallback.
  anchor: >-
    We can totally do it later...for context this call only takes about 3 minutes?...do you mind if we knock it out now?
  source: >-
    acq-closer-handbook.md, ACQ Outbound Set Phone Script, lines 2882-2890
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2884"
- id: C-closer-030
  type: case
  name: >-
    "I CAN'T LEAVE MY BUSINESS"
  statement: >-
    The rep normalises the problem among other attendees, names it key man risk, asks permission to offer a perspective, states that the product exists to save time by solving the problem faster, and reframes the trade as reallocating time rather than taking it away before asking again.
  why: >-
    The objection is treated as the very problem the product addresses, so agreeing with it strengthens rather than weakens the ask.
  demonstrates: >-
    The Time objection reframed as priority; agree, add, ask again with permission questions at each step.
  anchor: >-
    So, it’s not about taking time away…just allocating it differently ?…Would you be totally against exploring how we could help?
  source: >-
    acq-closer-handbook.md, ACQ Outbound Set Phone Script, lines 2892-2908
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2906"
- id: C-closer-031
  type: case
  name: >-
    Play out both scenarios
  statement: >-
    For "I need to solve a business problem first", the rep asks permission to play out both futures: if the problem is solved, the lead time (booked out at least six weeks) means the timing works and the next set of problems is next; if it is not solved by then, the team helps break past it — so either way the meeting is a win-win, closed with "would it be crazy just to have a conversation about it?".
  why: >-
    Both branches of the prospect's own reasoning are made to end in the same action, which removes the reason to wait without contradicting him.
  applies_when: >-
    Also used verbatim against "I ALREADY HAVE A SOLUTION", with the advisor in place of the prospect solving it.
  demonstrates: >-
    Agree and add rather than contradict; the Stall objection answered with the cost of waiting.
  anchor: >-
    Got it. So you solve that and we get you out… and get you out here…I think we are booked out at least 6 weeks anyways?…so it actually works well…(haha) then we can tackle the next set of problems…
  source: >-
    acq-closer-handbook.md, ACQ Outbound Set Phone Script, lines 2910-2932
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2921"
- id: C-closer-032
  type: case
  name: >-
    Your younger self is too busy for advice
  statement: >-
    If the scenario play-out fails, the rep asks to share one more perspective: imagine travelling back to when you started, meeting your younger self and offering everything you know now, and hearing him say he is too busy right now to get advice — you would think, stop being silly and let me help you.
  why: >-
    The prospect is put in the position of the adviser he is refusing, so he supplies the judgement himself rather than being told he is wrong.
  applies_when: >-
    After a negative answer to the win-win scenario ask.
  demonstrates: >-
    Add to their reasoning instead of contradicting it, then ask again ("would it be worth a quick chat?").
  anchor: >-
    So, imagine—you could travel back in time... to when you first started your business? and meet with your younger self...And you could tell them everything you know now....
  source: >-
    acq-closer-handbook.md, ACQ Outbound Set Phone Script, lines 2936-2950
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2944"
- id: C-closer-033
  type: case
  name: >-
    "BUSINESS IS BUSY RIGHT NOW"
  statement: >-
    The rep asks permission to share two cents, says other owners come out during their busy season precisely to maximise their top revenue-generating months, then poses the cost of waiting — one or two easy tweaks that drive revenue, missed for a season — with an explicit no promises or guarantees, and asks again.
  why: >-
    The cost of waiting is made concrete and compared with the cost of acting now, which is how the Stall objection is solved.
  demonstrates: >-
    The Stall objection answered with the good stuff missed and the bad stuff continued; disclaimers kept inside the pitch.
  anchor: >-
    imagine the cost of waiting to get that information...no promises or guarantees...it could be far higher... than the cost of doing it later. Would it be crazy to talk to one of our business consultants about it?
  source: >-
    acq-closer-handbook.md, ACQ Outbound Set Phone Script, lines 2952-2965
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2963"
- id: C-closer-034
  type: case
  name: >-
    ACQ Outbound No Pick Up Text Script
  statement: >-
    Skeleton for the text after a double dial with no answer: greeting plus one question about what made them download the lead magnet; then a reason to answer more questions and a numbered menu of bottlenecks (marketing, sales, people, profit, something crazy) answered by number; then recap plus "why did you pick that? Be specific"; then recap plus what they have tried; then a resource sent with a thumbs-up request; then three escalating follow-ups ending with a value video.
  why: >-
    Objections are handled over text by setting appointments rather than typing out paragraphs, and each message asks one thing the prospect can answer in a word or a number.
  applies_when: >-
    After a double dial when the prospect does not pick up.
  demonstrates: >-
    Discovery by text; the labelled-constraint menu; recap before every new question.
  anchor: >-
    [founder] has more resources to help you scale faster. I have a few questions to see what would be best for you.
  source: >-
    acq-closer-handbook.md, ACQ Outbound No Pick Up Text Script, lines 2994-3057
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3007"
- id: C-closer-035
  type: case
  name: >-
    ACQ Outbound Reminder Text Script
  statement: >-
    Skeleton for nurturing a booked appointment: the setter opens a group chat, introduces the closer and sends the pre-call video with a request to check it out; the closer texts immediately after; end of day, night before and morning of touches; a testimonial from someone in the prospect's industry; a one hour before "talk soon"; and a spot-holding nudge if there is no reply.
  why: >-
    Manual nurture has boosted show rates more than anything the author has seen across the portfolio, and this is named as the work that separates winners.
  applies_when: >-
    Between a set appointment and the close call; international leads use WhatsApp, and rescheduling stays with the setter.
  demonstrates: >-
    Show rate as an owned metric; the closer taking over the chat after the introduction.
  anchor: >-
    Hey name! Prepping for my meetings tomorrow. Did you have a chance to check out the video?
  source: >-
    acq-closer-handbook.md, ACQ Outbound Reminder Text Script, lines 3060-3124
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3102"
- id: C-closer-036
  type: case
  name: >-
    The hold-the-spot nudge
  statement: >-
    A silent prospect is not chased with another reminder but told someone else wants the slot and asked for a one-character reply — a thumbs up or a bell emoji — to keep it.
  why: >-
    A request that costs one tap gets an answer where a question does not, and the scarcity of the slot supplies the reason to answer now.
  applies_when: >-
    No reply to the reminder or to the second non-response text before a booked call.
  demonstrates: >-
    Escalating non-response texts before cancelling the appointment.
  anchor: >-
    Hey [Name], I finished prepping for our meeting, though I have someone requesting that time. Could you please send a quick &lt;img&gt;bell emoji&lt;/img&gt; so I can hold the spot?
  source: >-
    acq-closer-handbook.md, ACQ Inbound Set Text Script, line 3207
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3207"
- id: C-closer-037
  type: case
  name: >-
    ACQ Inbound Set Phone Script
  statement: >-
    Skeleton for the call made as soon as an inbound lead books: double dial on the opt-in, name, company and recorded line, confirm the invite, then try to pull the appointment up to right now ("would it be absolutely crazy if we just had our call now?"); if they have no time, ask for thirty seconds of qualifying questions — business type, rough revenue, what has them interested — check the video, and close with a reminder promise.
  why: >-
    Inbound sets are the newest, freshest and highest value appointments, so the objective is to pull the close call forward, ideally to right now.
  applies_when: >-
    Priority 1 of working the list; if they do not answer, transition to the texting script.
  demonstrates: >-
    Pull forward; double dial before you text.
  anchor: >-
    I actually have some time now…would it be absolutely crazy if we just had our call now?
  source: >-
    acq-closer-handbook.md, ACQ Inbound Set Phone Script, lines 3130-3165
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3146"
- id: C-closer-038
  type: case
  name: >-
    ACQ Inbound Set Text Script
  statement: >-
    Skeleton for texting an inbound set that did not pick up, in three send-and-wait blocks — business type, then the video check, then the pull-forward offer of today's open slots with the booked time as the fallback — followed by two non-response nudges, a cancel-and-rebook text twelve hours out, and night-before and morning-of reminders that branch on whether the video was confirmed.
  why: >-
    The blocks make sure no prospect slips through the cracks, and a quick text reply is a signal to call immediately rather than keep typing.
  applies_when: >-
    After the inbound double dial goes unanswered.
  demonstrates: >-
    Block 1 Business, Block 2 Why Us, Block 3 Pull Forward of the inbound workflow.
  anchor: >-
    Btw, I did actually have some time slots open today at X or Y if you're free? (If not our scheduled time works great too)
  source: >-
    acq-closer-handbook.md, ACQ Inbound Set Text Script, lines 3170-3237
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3188"
- id: C-closer-039
  type: case
  name: >-
    Cancel and rebook after silence
  statement: >-
    Twelve hours before a call the prospect has not answered about, the appointment is cancelled in writing, the silence is excused as busy business-owner life, and a new date is proposed in the same message.
  why: >-
    Cancelling frees the slot while the excuse and the immediate re-offer keep the lead from being lost to the cancellation.
  applies_when: >-
    No responses at all up to twelve hours out from the scheduled call.
  demonstrates: >-
    The cancel/reschedule branch of the inbound workflow.
  anchor: >-
    Hey [Name], since I did not hear back, I've canceled our meeting. But, I know business owner life is busy...would you be free tomorrow by chance?
  source: >-
    acq-closer-handbook.md, ACQ Inbound Set Text Script, line 3213
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3213"
- id: C-closer-040
  type: case
  name: >-
    ACQ Closing Script
  statement: >-
    Skeleton of the close call: intro with recorded line and the twenty minute box; if the video was not watched, send it and go on mute; the agenda and fit frame; an explicit no promises or guarantees disclaimer; discovery on why they booked and their takeaways from the video; a recap; a rapid-fire metrics block (revenue, profit, main offer, how they get clients, new clients a month, client spend, years owned) each answer recapped; the constraint question (marketing, sales, people, profit, something crazy) plus "is that the only thing"; the offer mapping two categories to three features with benefits; the buying question; then either the referral ask or the BAMFAM.
  why: >-
    The script came from the results of more calls than any single closer could have in a lifetime, so it is delivered word for word; the closer's job is to apply the skills to it.
  demonstrates: >-
    Introduction, Discovery, Offer, Close, and the branch into Referrals or BAMFAM.
  anchor: >-
    Let's do it. And before we jump in. Just want to be clear...we make no promises or guarantees of any rate of return or specific result.
  source: >-
    acq-closer-handbook.md, ACQ Closing Script, lines 3243-3429
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3276"
- id: C-closer-041
  type: case
  name: >-
    ACQ Looping Script
  statement: >-
    Skeleton of the first loop: step 1 is the same line whatever they say — acknowledge, ask permission, confirm the product can get them closer to their goal; step 2 branches on the answer, a yes with a new objection is confirmed then isolated, an uncertain yes is probed ("you don't seem super confident"), a confident yes is turned into their own reasons plus credibility, and "I'm not sure" is probed for the main concern — every branch ending in the isolating question before moving to the overcome.
  why: >-
    Knowing how to respond to an objection only matters if the prospect buys, so every branch must return to the offer; the isolating question makes sure the objection being answered is the only one left.
  demonstrates: >-
    Verify then Loop; Confirm, Probe, Isolate as named steps.
  anchor: >-
    **ISOLATE:** Other than [NEW OBJECTION]... is there anything else holding you back?
  source: >-
    acq-closer-handbook.md, ACQ Looping Script, lines 3433-3518
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:3447"
- id: C-closer-042
  type: case
  name: >-
    "I am overwhelmed / I have a lot going on right now"
  statement: >-
    The rep asks what makes them feel overwhelmed, confirms it back, says most owners join feeling exactly the same way and get the time benefit, asks permission to give context, then describes the first feature as the one that creates clarity and deletes what does not matter ("how much can we delete?" vs "how much can we add?"), and closes with "so why don't we just get you out to Vegas?".
  why: >-
    The objection is answered by making the product the cure for the state the objection describes, and the design principle of deletion is offered as the evidence.
  demonstrates: >-
    The Time objection; agree and add, then ask again.
  anchor: >-
    So most business owners join [PROGRAM] feeling the same exact way—but get [TIME BENEFIT] so the good news is…you are in the same spot. Mind if I share some context on that?
  source: >-
    acq-closer-handbook.md, Timing Objections, lines 3528-3542
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3536"
- id: C-closer-043
  type: case
  name: >-
    "I need to confirm the timeline"
  statement: >-
    The rep isolates the objection ("other than confirming dates—is there anything else holding you back?"), asks permission to share what others do, and describes the normal path: set up the ticket now, dates, hotel recommendations, itinerary and logistics to follow, and the date movable on the back end at any time.
  why: >-
    Removing the irreversibility of the decision removes the reason to wait, so the commitment can be made before the logistics are settled.
  demonstrates: >-
    Isolate then overcome; the Stall objection answered by shrinking the risk of deciding now.
  anchor: >-
    And if we need to move the date on the backend, we can 100% do that.
  source: >-
    acq-closer-handbook.md, Timing Objections, lines 3548-3557
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3557"
- id: C-closer-044
  type: case
  name: >-
    "I see the value in it... I just don't have the money"
  statement: >-
    The rep confirms it is only about the finances, isolates it with a hypothetical ("if you had the money today, would anything else prevent you from getting started?"), asks permission for a financial question, takes monthly cash flow and cash on hand with a recap in between, and then proposes setting everything up to hold the date.
  why: >-
    The hypothetical proves money is the only remaining objection before any work is done on it, and the money objection is then a matter of facts rather than feelings.
  demonstrates: >-
    Isolating the objection; the Money objection.
  anchor: >-
    So if you had the money today. Would anything else prevent you from getting started?
  source: >-
    acq-closer-handbook.md, Money Objections, lines 3568-3594
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3577"
- id: C-closer-045
  type: case
  name: >-
    "It's really expensive"
  statement: >-
    The rep agrees the price is high and turns it into a reason it will work — a high price makes the buyer care and act — tests it against a $500 version they would not believe in, then quotes Warren Buffet on price versus value, asks whether they see the value, and closes.
  why: >-
    The price is reframed as the mechanism of the result rather than as a cost to be justified.
  demonstrates: >-
    The Money objection solved by comparing what the problem costs with what the solution costs; agree and add.
  anchor: >-
    I think it’s good that it’s a lot...it means you’ll actually care and be more likely to take action. I mean if it were only $500—would you even believe it was valuable?
  source: >-
    acq-closer-handbook.md, Money Objections, lines 3598-3608
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3600"
- id: C-closer-046
  type: case
  name: >-
    "I don't have the card I want to use with me"
  statement: >-
    The rep isolates the card as the only blocker, then walks the payment options one at a time — tap to pay, Apple Pay, a quick bank transfer — and only after a third no drops it with a joke and books a BAMFAM.
  why: >-
    A logistical objection is exhausted by offering every mechanism before the meeting is rescheduled, so nothing is lost to an obstacle that was only about a piece of plastic.
  demonstrates: >-
    Isolate then overcome; BAMFAM as the exit when the loop is out of moves.
  anchor: >-
    Got it, so other than not having your card on you we’re good to rock n roll?
  source: >-
    acq-closer-handbook.md, Money Objections, lines 3633-3656
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3635"
- id: C-closer-047
  type: case
  name: >-
    "I just don't know if I see the value"
  statement: >-
    The rep turns to the free content the prospect already consumed and asks what it has done for them, then branches: growth from the content proves the source works and the product is the tactical version of it; no growth is attributed to not being able to apply it, which is exactly what the product supplies — both branches ending in an ask, with the no-guarantees line repeated.
  why: >-
    The prospect's own history with the material supplies the evidence, so either answer becomes a reason to buy rather than a point to argue.
  demonstrates: >-
    Agree and add rather than contradict; asking for the sale again at the end of every branch.
  anchor: >-
    Got it—Well let me ask you this…earlier you mentioned you consumed [CONTENT]— what has that done for you so far?
  source: >-
    acq-closer-handbook.md, Money Objections, lines 3658-3683
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3660"
- id: C-closer-048
  type: case
  name: >-
    "I need to talk to my spouse or business partner"
  statement: >-
    The rep isolates the other person as the only blocker, asks what their biggest concern would be, loops that concern as its own objection, then offers the reversal — if the partner hates the idea, call me and I will make sure you are taken care of — and asks for the order; a persistent no is met with "what if she/he says no?", an "I would go anyways" with the order, and an "I need to talk to them" with a BAMFAM for the conversation.
  why: >-
    The absent decision-maker's objection is the one that actually has to be handled, and the reversal removes the risk of deciding without them.
  demonstrates: >-
    The Decision-Maker objection; isolate, loop the real objection, ask for the order, BAMFAM as the fallback.
  anchor: >-
    Cool so typically what we do in this situation...because it's [INSERT REASON WHY]—Then if your [SPOUSE/BUSINESS PARTNER] absolutely hates the idea of you [RIDICULOUS BENEFIT #1] AND [RIDICULOUS BENEFIT #2]...then you can give me a call and I will make sure you are taken care of—fair enough?
  source: >-
    acq-closer-handbook.md, Decision-Maker, lines 3693-3734
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3728"
- id: C-closer-049
  type: case
  name: >-
    "I don't think I can learn in that big of a group"
  statement: >-
    The rep asks permission to describe the structure and answers the preference with mechanics: pre-work before arrival, no broad theories, direct work on the prospect's own bottlenecks in small groups with the directors, and three to five tactical steps to leave with — then asks whether that gives more context and confidence.
  why: >-
    A preference objection is answered by changing the variables that create the outcome the prospect fears, not by disputing the preference.
  demonstrates: >-
    The Preference objection: remind them of the problem, show the consequences, explain why the way it is done is to their benefit.
  anchor: >-
    It actually starts before you even arrive—we send you pre-work to understand your business—and make sure you’re prepped to get the most out of it—
  source: >-
    acq-closer-handbook.md, Preferences, lines 3743-3751
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3749"
- id: C-closer-050
  type: case
  name: >-
    "How is this different than the free content?"
  statement: >-
    The rep concedes that everything needed to scale is already online, then draws the line — free content tells you what to do, the product shows you how, specifically for your business, and you cannot ask a book a question about your business — names speed as the reason people choose it, asks for the order, and if still a no, prices the alternative in time spent searching.
  why: >-
    The comparison is granted rather than denied, and the difference is placed in specificity and time, which the free alternative cannot supply.
  demonstrates: >-
    The Preference objection; ask for the order after every overcome.
  anchor: >-
    The difference is that free content tells you what to do; the [PRODUCT] shows you how to do it—specifically for your business.
  source: >-
    acq-closer-handbook.md, Preferences, lines 3753-3770
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3755"
- id: C-closer-051
  type: case
  name: >-
    "I went to a similar [PRODUCT] and I didn't like it"
  statement: >-
    The rep diagnoses the bad experience first — how many people were there, did you get personalised help from the speakers, were they just not tactical enough — and only then asks permission to describe the structure, starting by ruling out the thing they disliked ("if you're looking for a RARA event, this isn't that") before the pre-work, small groups and three to five tactical steps, closing with a confidence check and "Is there any reason we shouldn't do this?".
  why: >-
    The prospect's objection is to a different thing, and that can only be shown after the difference has been established from their own answers.
  demonstrates: >-
    Pull Teeth applied to a preference objection; agree and add, then ask again.
  anchor: >-
    First off, if you're looking for a RARA event, this isn't that.
  source: >-
    acq-closer-handbook.md, Preferences, lines 3772-3801
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3782"
- id: C-closer-052
  type: case
  name: >-
    "I'm too small for this" and "I'm too big for this"
  statement: >-
    Both opposite objections get the same answer: yes, there will be larger (or smaller) businesses here, but we group you by revenue with businesses at a similar scale, so everything is directly relevant, with a step ahead to see around the corner and a step behind for perspective.
  why: >-
    One structural fact answers both directions of the same fit objection, so the closer never has to argue about size.
  demonstrates: >-
    The Preference objection answered with the mechanics of delivery.
  anchor: >-
    And yes there will be larger businesses here, BUT we group you with businesses of similar size, so everything is directly relevant.
  source: >-
    acq-closer-handbook.md, Preferences, lines 3803-3823
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3807"
- id: C-closer-053
  type: case
  name: >-
    "I need to think about it"
  statement: >-
    The rep asks permission to be upfront, states that almost everyone locks in their spot and the exceptions come down to one of two reasons — they do not see the value, or logistics — checks the value in passing, and asks the prospect to pick number two or something crazy.
  why: >-
    A stall with no stated reason is converted into a forced choice from a short list, which produces the real objection the loop can handle.
  demonstrates: >-
    The Stall objection; isolating the objection worth handling.
  anchor: >-
    Yeah so typically almost everyone is ready to lock in their spot… and if not it’s really because of 1 or 2 reasons.
  source: >-
    acq-closer-handbook.md, Stall Objections, lines 3833-3842
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3837"
- id: C-closer-054
  type: case
  name: >-
    "I always take 24 hours to make a decision"
  statement: >-
    The rep respects the rule, asks whether any new information is making them reconsider, asks permission to share a perspective, reports that the large owners he watches make quick logical decisions when they see value, confirms the prospect sees the value, and asks whether it would be absolutely crazy to break the rule.
  why: >-
    The prospect's own rule is not attacked; a model of how decision makers he admires behave is offered instead, and breaking the rule becomes his choice.
  demonstrates: >-
    The Stall objection; agree and add, then ask again.
  anchor: >-
    The cool part of my job is I get to see the decision making process of Alex and Leila and other large business owners. They make quick logical decisions when they see value.
  source: >-
    acq-closer-handbook.md, Stall Objections, lines 3844-3859
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3855"
- id: C-closer-055
  type: case
  name: >-
    "It's a big commitment / I need time"
  statement: >-
    The rep names the decision as big, then names the nervousness, then turns it into the reason to start — people who start nervous do great — and tests it by asking whether, having paid, they would let things fall through the cracks or come in, ask their questions and implement; the answer confirms nervousness predicts taking it seriously, then value and action are confirmed and the card menu closes it.
  why: >-
    The emotion behind the stall is made into evidence for buying rather than something to be talked out of, and the prospect states the commitment himself.
  demonstrates: >-
    The Stall objection; agree and add; asking for the sale immediately after agreement.
  anchor: >-
    If you put down [PROGRAM COST], do you think you would just let things fall through the cracks? Or do you feel you would come in, ask all your questions, implement everything we give you, and make the most out of your time here?
  source: >-
    acq-closer-handbook.md, Stall Objections, lines 3861-3875
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3869"
- id: C-closer-056
  type: case
  name: >-
    ACQ BAMFAM Script
  statement: >-
    Skeleton for nurturing a booked second meeting: a five minute follow-up text that thanks them and states we can help, an optional video matched to their business, size, problem or objection, a night-before text, a morning-of text, and for meetings booked more than three days out a value message — a testimonial, a third party review, or a case study of a similar company that solved their specific problem.
  why: >-
    The gap between the two calls is where the deal is lost, so the same follow-up cadence that gets prospects to a first call is run against the second.
  applies_when: >-
    After a BAMFAM is booked, to nurture the appointment in between meetings.
  demonstrates: >-
    BAMFAM; value-based touches before a call.
  anchor: >-
    Hey [NAME], so great talking with you. Excited to continue the conversation & potentially do business together. We can help.
  source: >-
    acq-closer-handbook.md, ACQ BAMFAM Script, lines 3880-3917
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3888"
- id: C-closer-057
  type: case
  name: >-
    ACQ Referral Text Script
  statement: >-
    Skeleton for the referral by text: the day after signup, an excited opener plus the question about other amazing business owners who might benefit; a yes goes to a group chat as the easiest way; a no is left open ("holler at me when you do"); and in the group chat the rep thanks the referrer, greets the referral, ties the invitation to the customer, and offers two specific times.
  why: >-
    The referral ask is adapted to text when the call ran out of time or the ask was missed, and the group chat is the mechanism that turns the yes into a conversation.
  applies_when: >-
    The day after someone signs up and agreed to give a referral, or as a follow-up when the ask was not made.
  demonstrates: >-
    The Referral Process carried over to text; two named times as the ask.
  anchor: >-
    Hey Name! Excited to have you out here soon. Curious - did you know any other amazing business owners who might benefit from [PRODUCT]?
  source: >-
    acq-closer-handbook.md, ACQ Referral Text Script, lines 3921-3941
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3927"
- id: C-closer-058
  type: case
  name: >-
    ACQ No Show Script
  statement: >-
    Skeleton for a no-show: after the double dial at the scheduled time, an immediate text ("just tried your cell. Ready to rock?"); five minutes later, the busy-owner excuse plus two named times to reschedule; and if there is still no response, the lead goes into the end-of-day outbound block, with a pickup routed into the Outbound Set Phone Script.
  why: >-
    A no-show is not a lost lead but an unworked one, so it is kept in a cadence and returned to the outbound block rather than dropped.
  applies_when: >-
    After a double dial with no response at the scheduled time.
  demonstrates: >-
    Working the list by priority; two named times as the reschedule ask.
  anchor: >-
    "I know business owner life is busy...Happy to find another time. I have some openings tomorrow at [TIME] or [TIME]? Either of those work to reschedule?"
  source: >-
    acq-closer-handbook.md, ACQ No Show Script, lines 3970-3980
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3979"
- id: C-closer-059
  type: case
  name: >-
    ACQ Pipeline Phone & Text Script
  statement: >-
    Skeleton for the pipeline: call first, and open on the specific obstacle that is holding the deal up before transitioning into the overcomes; if there is no answer, text in four steps — a five minute follow-up to leave a positive feeling, value messages tied to their named problem, check-ins on how they feel about next steps, bumps that escalate to "should I assume this isn't a priority right now?", and re-offers such as spots opening on a date.
  why: >-
    The goal with a stalled or ghosting prospect is to close the deal or agree on a timeline to touch base again, so every message either revives the obstacle conversation or earns a reply.
  applies_when: >-
    Priority 3 of the list: anyone who no-showed or declined and can still be called, worked newest to oldest back through 60 days.
  demonstrates: >-
    Double dial before you text; working the pipeline by priority.
  anchor: >-
    Great- just had a few minutes [BETWEEN MEETINGS/BEFORE I WRAPPED MY DAY] wanted to touch base around [OBSTACLE THAT IS PREVENTING THE DEAL FROM MOVING FORWARD] How’s it going there?
  source: >-
    acq-closer-handbook.md, ACQ Pipeline Phone & Text Script, lines 3987-4052
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:4002"
```
