# Улов фазы 1 — ACQ Closer Handbook (2025) (ярус 2), тип D: антипаттерны и границы

Группа `tier2-closer`, слаг `closer`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **55** (экстрактор вернул 55, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `acq-closer-handbook.md` | 1–4125 | 5 | 55 |

## Как собран файл

Экстрактор D (Antipatterns and boundaries) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-closer.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-closer-D.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: D-closer-001
  type: antipattern
  name: >-
    Winging it instead of following the process
  statement: >-
    Reading the method and then improvising on the call instead of running its process daily is the default failure; the material only pays when it is used every day.
  why: >-
    The author says every day it is not used is money left on the table, and that winging it is an active choice to stay a worse version of yourself.
  anchor: >-
    Every time you wing it instead of following its process is a choice you make to stay a worse version of yourself.
  source: >-
    acq-closer-handbook.md, The Truth About This Handbook, line 427
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:427"
- id: D-closer-002
  type: rule
  name: >-
    Nobody closes at 100%
  statement: >-
    No closer converts every call, so training never stops even for a team performing well.
  why: >-
    Because a 100% close rate does not exist, there is always room left to improve.
  boundary: >-
    The author states the ceiling of his own method: it maximizes the likelihood of a sale, it does not guarantee one on any given call.
  anchor: >-
    Nobody closes at 100%. So there's always room to improve, and we intend to do so.
  source: >-
    acq-closer-handbook.md, Onboarding: Schedule & Training, line 765
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:765"
- id: D-closer-003
  type: rule
  name: >-
    Only work leads you still have permission to call
  statement: >-
    Pipeline work covers only no-shows and declines that you still have permission to call, and anyone who asks not to be contacted is opted out of the list.
  why: >-
    Every lead counts as opted in until they opt out, so the opt-out has to be recorded the moment it is given.
  boundary: >-
    The author's own limit on working the pipeline: permission to call, withdrawn by the prospect at any time.
  anchor: >-
    Anyone that no-showed or declined our offer but who *we still have permission to call*.
  source: >-
    acq-closer-handbook.md, Hunt Mode #2 Work Your List, line 1304
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1304"
- id: D-closer-004
  type: antipattern
  name: >-
    Typing out paragraphs over text
  statement: >-
    Handling an objection by writing out paragraphs in a text thread instead of using the text to book an appointment.
  why: >-
    The author's instruction is that objections over text are handled by setting appointments, not by typing; an ongoing thread is converted into a call after one or two replies.
  applies_when: >-
    Any text conversation with a prospect who raises an objection.
  anchor: >-
    Handle objections over text by setting appts rather than typing out paragraphs.
  source: >-
    acq-closer-handbook.md, Hunt Mode #2 Work Your List, Texting Guidelines, line 1342
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1342"
- id: D-closer-005
  type: rule
  name: >-
    Only qualified prospects
  statement: >-
    The claim that controlling the conditions makes a prospect sellable is made about qualified prospects, not about everyone who picks up the phone.
  why: >-
    Every condition you control raises the chance someone buys; controlling all of them, all the time, is what makes a closer unbeatable.
  boundary: >-
    The author restricts the premise of Kill Mode to the qualified prospect.
  anchor: >-
    Every qualified prospect is sellable if we control the conditions.
  source: >-
    acq-closer-handbook.md, Kill Mode, line 1433
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1433"
- id: D-closer-006
  type: antipattern
  name: >-
    Expecting the script to do the work
  statement: >-
    Treating the closing script as the thing that produces the sale, rather than as a tool through which a skill is applied.
  why: >-
    The author states the script does no work at all: the closer does, and a script is not a skill.
  anchor: >-
    The Closing Script doesn’t do any work. YOU DO. Again, there’s nothing magic here. Just skills.
  source: >-
    acq-closer-handbook.md, Kill Mode, Kill Skills, line 1457
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1457"
- id: D-closer-007
  type: antipattern
  name: >-
    Don't be cute
  statement: >-
    Building elaborate schemes on the belief that complex methods beat basic ones, instead of executing the fundamentals.
  why: >-
    The author says the elaborate schemes get no results, while the basics work every time when executed properly.
  anchor: >-
    See, most people think basic methods get basic results. This leads them to believe complex methods get better results. So they make up these elaborate schemes and get… no results.
  source: >-
    acq-closer-handbook.md, Breathe the Script, Don't Be Cute, line 1482
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1482"
- id: D-closer-008
  type: antipattern
  name: >-
    Confusing memorizing with breathing the script
  statement: >-
    Taking breathe the script to mean reading it, memorizing it, or using similar words in about the same order, instead of delivering it word-for-word and naturally.
  why: >-
    The author calls that reading of the phrase wrong: delivery has to be word-for-word, with your eyes closed, naturally.
  anchor: >-
    Most people think “breathe the script” means “use similar words in about the same order”. *This is wrong*.
  source: >-
    acq-closer-handbook.md, Breathe the Script, Important Note, line 1522
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1522"
- id: D-closer-009
  type: antipattern
  name: >-
    Putting your own spin on it
  statement: >-
    Improving the proven script with your own wording, which the author names as the biggest single source of lost sales.
  why: >-
    Whoever puts their own spin on it disrespects tens of thousands of hours of work other salesmen did, because they think they can do better; nobody is above the script.
  anchor: >-
    More sales are lost from people putting their own spin on things. Getting cute instead of following the proven process.
  source: >-
    acq-closer-handbook.md, Breathe the Script, Important Note, line 1522
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1522"
- id: D-closer-010
  type: antipattern
  name: >-
    Recalling the script instead of listening
  statement: >-
    Any state in which you are remembering, searching for, or reading your words means you are not paying attention to the prospect.
  why: >-
    Without attention on the prospect the quality of the script stops mattering, because you will say the wrong stuff, and saying the wrong stuff loses the close.
  anchor: >-
    If you’re not paying attention to the prospect, then it doesn’t matter how good of a script you have—you’ll say the wrong stuff.
  source: >-
    acq-closer-handbook.md, Breathe the Script, line 1509
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1509"
- id: D-closer-011
  type: antipattern
  name: >-
    Speeding up when excited or stressed
  statement: >-
    Talking at the trained speed in practice and then accelerating on live calls under excitement or stress.
  why: >-
    Worst case the prospect attends to your stress rather than your words and you lose trust, attention and the sale; best case they cannot keep track of what you say and you still lose the sale.
  applies_when: >-
    Live calls, where the author sets the target range at about 150-170 words per minute.
  anchor: >-
    This is because amateur sales reps talk at the right speed during training, but speed up when they get excited or stressed. This loses sales.
  source: >-
    acq-closer-handbook.md, Tone, Talk Slower (Speed), line 1569
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1569"
- id: D-closer-012
  type: antipattern
  name: >-
    Talking too much on the call
  statement: >-
    Occupying most of the call with your own talking; on a perfect fifteen-minute close the closer speaks about three minutes and the prospect twelve.
  why: >-
    At 150-170 words per minute a 500-word script takes just over three minutes, so anything beyond that share of the call is the closer talking too much.
  anchor: >-
    if a call goes perfect on your side and takes 15 minutes to close, then the prospect spoke for 12 minutes and you spoke for three
  source: >-
    acq-closer-handbook.md, Tone, Talk Slower (Speed), line 1573
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1573"
- id: D-closer-013
  type: rule
  name: >-
    Talking quieter works in person, not on the phone
  statement: >-
    The tactic of lowering your voice so people listen harder is accepted for in-person selling and rejected for phone selling.
  why: >-
    Over the phone they turn the volume up anyway, or ask you to repeat yourself, or strain to hear — which annoys business owners rather than persuading them.
  boundary: >-
    The author grants the opposing tactic inside its medium and limits his own rule to the phone.
  anchor: >-
    Some people argue that if you talk quieter then people will listen harder. And I agree, *in-person*.
  source: >-
    acq-closer-handbook.md, Tone, Talk Louder (Volume), line 1575
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1575"
- id: D-closer-014
  type: antipattern
  name: >-
    The forgotten-script pause
  statement: >-
    Forgetting a part of the script produces a long unplanned pause, and then stuttering, stopping and starting, or rambling at high speed.
  why: >-
    The pause focuses maximum attention on the words around it and gives them the worst job possible, telling the prospect the closer does not know what he is saying; the author calls this catastrophic rather than awkward, and says it is avoided by breathing the script.
  anchor: >-
    For example, if a closer forgets part of the script, it creates a pause. A long pause.
  source: >-
    acq-closer-handbook.md, Tone, Awkward Pauses Are Not Awkward, line 1700
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1700"
- id: D-closer-015
  type: antipattern
  name: >-
    Training to speak naturally
  statement: >-
    Practising a natural-sounding delivery, which the author calls getting good at pretending to speak naturally and one of the dumbest things a closer can do.
  why: >-
    The way not to sound like someone reading a script is to know the script so well it becomes natural, not to rehearse the impression of naturalness.
  anchor: >-
    Training to speak naturally is another way of saying you try to get good at pretending to speak naturally. This is one of the dumbest things you can do.
  source: >-
    acq-closer-handbook.md, Tone, Advanced Tone Tactics, line 1710
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1710"
- id: D-closer-016
  type: antipattern
  name: >-
    Talking after the buying question
  statement: >-
    Filling the silence after you ask for the sale instead of holding the longest pause of the call there.
  why: >-
    The author puts the loss at up to 40% of deals, and says that without being forced to address the buying question head on the prospect will avoid it.
  anchor: >-
    You will lose up to 40% of your deals if you don't shut the fuck up
  source: >-
    acq-closer-handbook.md, Tone, Bottom Line, line 1720
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1720"
- id: D-closer-017
  type: antipattern
  name: >-
    Blowing the call in the intro
  statement: >-
    Treating the first 30-60 seconds as a low-stakes part of the call because it is the shortest.
  why: >-
    The intro frames the whole call and a thirty-minute call can be destroyed in thirty seconds; you cannot close what you do not open.
  anchor: >-
    And you can blow a 30 minute call in 30 seconds.
  source: >-
    acq-closer-handbook.md, Introduction, line 1735
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1735"
- id: D-closer-018
  type: antipattern
  name: >-
    Dropping the required opening so it does not sound like a sales call
  statement: >-
    Leaving out the name, the company, the recording notice or the reason for the call because other salespeople say it sounds like a sales call, or using illegal ways around it.
  why: >-
    The author calls that small time advice and points out the omission breaks the law; the format also sounds like a legitimate business, and every large publicly traded company in the US uses it.
  boundary: >-
    A legal requirement rather than a tactic: the four elements are said on every call regardless of their effect on conversion.
  applies_when: >-
    Every recorded outbound and close call.
  anchor: >-
    You start every call with those four things because, if you don’t—you break the law.
  source: >-
    acq-closer-handbook.md, Introduction, lines 1744-1746
  confirmations: 3
  authors_caveat: >-
    Instead of illegal workarounds the author invests in the prospect liking and trusting the brand, the product and the team, which he says makes the legal methods work better than the sketchy ones.
  anchor_at: "acq-closer-handbook.md:1746"
- id: D-closer-019
  type: antipattern
  name: >-
    Long, clunky, forced intro
  statement: >-
    Stretching the introduction, which either loses the prospect outright or spends the minutes you will need at the end of the call.
  why: >-
    Taking too long can cost the sale and the referral that sale would have produced, so one undisciplined intro costs two sales.
  anchor: >-
    Long, clunky, forced intros do kill calls. And if you don't lose the prospect, the minutes you waste at the beginning are minutes you'll wish for at the end.
  source: >-
    acq-closer-handbook.md, Introduction, line 1806
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1806"
- id: D-closer-020
  type: antipattern
  name: >-
    What the intro is not
  statement: >-
    Using the introduction for small talk, for a pitch, or as a place to lie, skip parts, or talk fast.
  why: >-
    The intro exists to ask the minimum required questions with the minimum required words in the proper tone, and that is what gets you through it fast.
  anchor: >-
    The intro is not a place to lie, skip parts, or talk fast. No place is.
  source: >-
    acq-closer-handbook.md, Introduction, lines 1808-1810
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1810"
- id: D-closer-021
  type: antipattern
  name: >-
    Waiting for the prospect to hand you the problem
  statement: >-
    Expecting business owners to state their problems already labelled, urgent and funded; they never do, so the problems have to be pulled out of them.
  why: >-
    Because the prospect will not volunteer it, the author replaces waiting with the 9 Steps of Discovery.
  anchor: >-
    But... that never happens. So, we have to pull it out of them.
  source: >-
    acq-closer-handbook.md, Discovery, line 1834
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1834"
- id: D-closer-022
  type: antipattern
  name: >-
    Skipping current and desired
  statement: >-
    Entering the Pain Cycle without first establishing the gap between where the prospect is now and where they want to be.
  why: >-
    It takes only a minute, and without knowing where someone wants to go you cannot give them directions.
  anchor: >-
    This typically only takes a minute but you cannot skip it.
  source: >-
    acq-closer-handbook.md, Discovery, Steps 1-2: Current and Desired, line 1863
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1863"
- id: D-closer-023
  type: rule
  name: >-
    Only problems we can solve
  statement: >-
    Discovery asks about results only in the areas where the offer can produce good results, and a problem that is not big enough is replaced by another one through a further Pain Cycle.
  why: >-
    Every good result the company offers becomes a result of the prospect's that can be asked about; problems outside that set are not pursued.
  boundary: >-
    The author's own limit on the scope of discovery: the method does not reach for pain it cannot sell against.
  anchor: >-
    We only care about problems we can solve. This means one simple thing: we only ask the prospect about results in areas we can get good results.
  source: >-
    acq-closer-handbook.md, Discovery, Step 3: Obstacle, line 1881
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1881"
- id: D-closer-024
  type: antipattern
  name: >-
    Making pulling teeth complicated
  statement: >-
    Inventing elaborate handling for vague, confusing or incomplete answers instead of the same two moves every time: ask them to tell you more, then ask for an example.
  why: >-
    Only two things are wanted from the answer, more information about the problem and a mapping to the solution; the author says salespeople make this so complex it is hilarious.
  anchor: >-
    This is something salespeople make so complex it's hilarious. Don't be cute.
  source: >-
    acq-closer-handbook.md, Discovery, Step 5: Pull Teeth, line 1912
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1912"
- id: D-closer-025
  type: antipattern
  name: >-
    Going straight to pitching
  statement: >-
    Moving from discovery into a pitch, or making the offer a list of benefits followed by a request for money, instead of mapping the collected problems to solutions first.
  why: >-
    Collecting pain points and then abandoning them wastes the discovery; the offer is a personalized one built on the spot from what was just recapped.
  anchor: >-
    I say "kind of" because typical salespeople go right to "pitching". Don't do that.
  source: >-
    acq-closer-handbook.md, Offer, line 1985
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1985"
- id: D-closer-026
  type: rule
  name: >-
    Two minutes and about 320 words for the offer
  statement: >-
    The offer gets two minutes, which at 150-170 words per minute is about 320 words, so every word has to count.
  why: >-
    The author says that if two minutes does not sound like enough, the closer is wasting time and, more precisely, wasting words.
  boundary: >-
    A hard budget the author sets on the offer section of the call.
  anchor: >-
    Remember, talking between 150–170 words per minute gives you about 320 words to make your offer.
  source: >-
    acq-closer-handbook.md, Offer, line 1989
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1989"
- id: D-closer-027
  type: antipattern
  name: >-
    Coming up with the offer on the fly
  statement: >-
    Improvising labels, assurances or benefits during the call instead of preparing them in advance and plugging them in.
  why: >-
    Prospects change but the solutions stay the same, so labels, assurances and benefits can all be prepared; improvising risks saying something dumb, wrecking your tone, or both.
  anchor: >-
    You should never have to come up with anything on the fly and risk saying something dumb, screwing up your tone, or both.
  source: >-
    acq-closer-handbook.md, Offer, line 2024
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2024"
- id: D-closer-028
  type: antipattern
  name: >-
    Asking do you have any questions
  statement: >-
    Asking the prospect whether they have any questions, which the author treats as asking them for reasons not to buy.
  why: >-
    The author states the consequence for the rep directly: being benched and made an example of.
  anchor: >-
    If you ever ask “do you have any questions?” you will be benched and made an example of. I do not recommend asking prospects for reasons not to buy.
  source: >-
    acq-closer-handbook.md, Offer, PRO TIP, line 2063
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2063"
- id: D-closer-029
  type: antipattern
  name: >-
    Taking the time objection at face value
  statement: >-
    Accepting a lack of time as a real constraint instead of treating it as a priority problem.
  why: >-
    The author's position is that not enough time is never an objection, only a not high-enough priority; it is solved by finding lower-value uses of their time and getting them to agree those are worth less.
  anchor: >-
    not enough time is never an objection, only not a high-enough priority.
  source: >-
    acq-closer-handbook.md, Objections, The 5 Objections to Buying, line 2084
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2084"
- id: D-closer-030
  type: rule
  name: >-
    Which objections come cannot be predicted
  statement: >-
    Unlike the closing script, objection handling cannot be rehearsed in a fixed order: which objections arrive, how many, and in what order is unknowable in advance.
  why: >-
    Guessing is only a guess and a single slip costs the close, so the only preparation that works is being prepared for all objections all the time.
  boundary: >-
    The author marks the limit of the predictability his scripts otherwise rely on.
  anchor: >-
    nobody can really know which objections you'll have to handle, how many you'll have to handle, or the order you'll have to handle them.
  source: >-
    acq-closer-handbook.md, Objections, Preparing for Objections, line 2166
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2166"
- id: D-closer-031
  type: antipattern
  name: >-
    Answering the objection and stopping there
  statement: >-
    Producing a good response to an objection without looping the prospect back to the offer and asking again.
  why: >-
    Knowing how to respond only matters if the prospect buys, so the response has to return to the offer.
  anchor: >-
    Knowing how to respond to an objection only matters if the prospect buys. So to truly handle an objection, you must loop it back to the offer.
  source: >-
    acq-closer-handbook.md, Objections, Preparing for Objections, line 2170
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2170"
- id: D-closer-032
  type: antipattern
  name: >-
    The gotcha
  statement: >-
    Catching the prospect out on their stated objection by pointing at evidence that contradicts it, which feels clever only to the closer.
  why: >-
    The prospect is made to feel foolish and attacked and the conversation ends; even when people use an excuse, you do not challenge them on it directly.
  anchor: >-
    The lesson was clear: catching prospects in their objections feels clever, but the only one who thinks so is you.
  source: >-
    acq-closer-handbook.md, Looping, The “Gotcha” Moment, line 2199
  confirmations: 2
  authors_caveat: >-
    The author's replacement move, given in the same story, is to grant the point and ask what would need to happen for it to make sense financially — same goal, no confrontation.
  anchor_at: "acq-closer-handbook.md:2199"
- id: D-closer-033
  type: antipattern
  name: >-
    The wrong way to handle objections
  statement: >-
    Getting the prospect to concede that their reason was a bad one and leaving it there, as the author says a vast majority of salespeople do.
  why: >-
    The expected chain — closer says the smart thing, prospect thanks him and buys — belongs to fantasy land; in reality the prospect is embarrassed, gets angry at being made to feel stupid, and acquires a genuinely good objection, that the closer is an asshole.
  anchor: >-
    But, that's only *one* part of proper objection handling. And a vast majority of salespeople just leave it there.
  source: >-
    acq-closer-handbook.md, Looping, The Wrong Way to Handle Objections, line 2208
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2208"
- id: D-closer-034
  type: antipattern
  name: >-
    Winning the argument
  statement: >-
    Treating objection handling as a debate to be won against the prospect.
  why: >-
    If you try to win arguments with prospects everyone loses; the goal is to close them, and agreement is what buys the further chances to ask.
  anchor: >-
    You're not on the debate team. You're on the ACQ sales team. If you try to win arguments with prospects, *everyone loses*.
  source: >-
    acq-closer-handbook.md, Looping, The Wrong Way to Handle Objections, line 2239
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:2239"
- id: D-closer-035
  type: antipattern
  name: >-
    Expecting the catch to force the buy
  statement: >-
    Catching a prospect in a weak excuse is fine; expecting them to buy because you caught them is worse than letting them walk.
  why: >-
    It makes the company look like a bunch of assholes, which costs more than the lost deal.
  anchor: >-
    Catching a prospect in a silly excuse is good. Expecting them to magically buy *because* you caught them in a silly excuse is *worse than letting them walk*.
  source: >-
    acq-closer-handbook.md, Looping, Bottom Line, line 2244
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2244"
- id: D-closer-036
  type: antipattern
  name: >-
    Insulting the objection
  statement: >-
    Attacking the objection itself, however silly it is, instead of addressing only its content.
  why: >-
    With tone controlled the prospect never feels insulted or embarrassed and does not call off the deal; nobody likes someone who makes them feel dumb, stupid, inconsistent or like a liar.
  applies_when: >-
    Every loop; the author says tone matters more here than anywhere else on the call.
  anchor: >-
    no matter how silly the objection, you must *never ever* insult the objection itself. You will *only address its content*.
  source: >-
    acq-closer-handbook.md, Looping, The Right Way to Handle Objections, line 2252
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2252"
- id: D-closer-037
  type: antipattern
  name: >-
    Wanting to be right
  statement: >-
    Pursuing correctness with the prospect rather than agreement.
  why: >-
    The closers who ask for the buy most often get the most closes, and only agreeable interactions produce enough chances to ask.
  anchor: >-
    To be clear, the goal is not to “win” an argument. If you want to be right, don’t get into sales.
  source: >-
    acq-closer-handbook.md, Looping, The Right Way to Handle Objections, line 2260
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2260"
- id: D-closer-038
  type: rule
  name: >-
    Any response short of a clear no is fear
  statement: >-
    A prospect who genuinely did not want the offer would say so, so every other response is read as the normal fear of doing something new.
  why: >-
    The product is new to them and not to us, so the closer's job is to help them past that fear rather than to corner them.
  boundary: >-
    The author's own premise for looping, and the one case it excludes: a prospect who says outright they do not want it.
  anchor: >-
    if they truly didn’t want what we offered, they would say so. This means any other response is just their natural fear of doing something new.
  source: >-
    acq-closer-handbook.md, Looping, The Right Way to Handle Objections, line 2262
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2262"
- id: D-closer-039
  type: antipattern
  name: >-
    Objection whack-a-mole
  statement: >-
    Handling the first objection as stated, instead of ignoring it, confirming the product's value and asking a triage question to isolate the objection worth handling.
  why: >-
    Before anything else you need to know whether they think the product is valuable; the triage question gets them to abandon their reflex objection.
  anchor: >-
    Before getting into objection whack-a-mole, we need to know something very important: Do they think our product is valuable?
  source: >-
    acq-closer-handbook.md, Looping, Handling the First Objection, line 2270
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2270"
- id: D-closer-040
  type: rule
  name: >-
    Looping stops on the buy or on the clock
  statement: >-
    Looping continues until the prospect buys or the call runs out of time, and every loop ends with asking for the sale again.
  why: >-
    Prospects eventually run out of objections while the closer never runs out of loops, so each successful loop moves closer to the close.
  boundary: >-
    The author's stop conditions for looping; running out of time is handled by a BAMFAM rather than by more loops.
  anchor: >-
    you keep looping until one of two things happen. They buy or you run out of time.
  source: >-
    acq-closer-handbook.md, Looping, The Second Objection and Beyond, line 2316
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2316"
- id: D-closer-041
  type: antipattern
  name: >-
    Overcoming a vague jumble of words
  statement: >-
    Trying to answer an objection as it was first stated, instead of breaking it into specific examples that can be tackled one at a time.
  why: >-
    Asking them to tell you more and to give an example buys you time and makes the prospect do the thinking; the author attributes the habit to every advanced closer he has met.
  anchor: >-
    which allows you to tackle them individually rather than trying to overcome some vague jumble of words.
  source: >-
    acq-closer-handbook.md, Looping, Pro Tip: Isolating Objections & Buying Time, line 2357
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2357"
- id: D-closer-042
  type: antipattern
  name: >-
    And, never But
  statement: >-
    Joining the acknowledgement to your addition with but, which erases everything said before it, instead of with and.
  why: >-
    But means ignore all the words before it, which disrespects the prospect and will cost the sale; the acknowledgements disarm because prospects expect an argument and never get one.
  anchor: >-
    Think of “But” like a big fat eraser. It means ignore all the words before it. Do not disrespect prospects like that.
  source: >-
    acq-closer-handbook.md, Looping, line 2369
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2369"
- id: D-closer-043
  type: rule
  name: >-
    The content of the answer matters almost not at all
  statement: >-
    The author holds that the specific response given to an objection matters far less than being able to ask again, and that logic matters almost not at all.
  why: >-
    His top closes can follow any reason a prospect gives and do not answer the objection at all: they agree and ask again; if the prospect feels good, they buy.
  boundary: >-
    The author flags this himself as a personal note and as controversial, and states his aim as making the closer rich rather than right.
  anchor: >-
    The more I’ve studied sales and persuasion, the less I think the response you give matters.
  source: >-
    acq-closer-handbook.md, Looping, On a personal note, line 2384
  confirmations: 2
  authors_caveat: >-
    Marked by the author as controversial and as his own view rather than a team standard.
  anchor_at: "acq-closer-handbook.md:2384"
- id: D-closer-044
  type: antipattern
  name: >-
    Looping a lot
  statement: >-
    A call that needs many loops is a symptom of mistakes earlier in the script, not of good objection handling.
  why: >-
    The vast majority of sales close on the first and second ask, not the fifth.
  anchor: >-
    If you are looping a lot, it means you are messing up earlier in the script.
  source: >-
    acq-closer-handbook.md, Looping, Helpful Points About Looping, line 2441
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2441"
- id: D-closer-045
  type: rule
  name: >-
    Looping can reveal a bad fit
  statement: >-
    Sometimes looping shows the prospect is genuinely a bad fit; that goes into the notes and the manager decides whether they stay in the pipeline.
  why: >-
    The decision about keeping the prospect is taken out of the closer's hands and passed to the manager.
  boundary: >-
    The author's own exception to looping until the buy: not every prospect in the loop is a prospect to keep.
  anchor: >-
    Sometimes looping reveals that the prospect is actually a bad fit.
  source: >-
    acq-closer-handbook.md, Looping, Helpful Points About Looping, line 2446
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2446"
- id: D-closer-046
  type: antipattern
  name: >-
    Changing your tone in the close
  statement: >-
    Shifting tone once the close is on the line, which the author names as the place where most salespeople fail.
  why: >-
    The best closers sound exactly the same during loops as before them; tone has the least room for error here, so adrenaline has to be met with breathing, slowing down and training.
  anchor: >-
    They change their tone in the close—when their game is on the line. Don't do that.
  source: >-
    acq-closer-handbook.md, Looping, Helpful Points About Looping, line 2447
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2447"
- id: D-closer-047
  type: antipattern
  name: >-
    We'll follow up offline
  statement: >-
    Ending a call that did not close without booking the next one on that same call.
  why: >-
    Both parties are on the call now; if you will not book a call while on a call, the chances over text afterwards are worse.
  applies_when: >-
    Closes that need a second call: time constraint, a decision-maker, or banking delay on high ticket.
  anchor: >-
    You must secure the next call on the current call. Do not say "we'll follow up offline".
  source: >-
    acq-closer-handbook.md, BAMFAM, Time Constraint BAMFAM, line 2466
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2466"
- id: D-closer-048
  type: antipattern
  name: >-
    Not asking for the referral
  statement: >-
    Skipping the referral ask out of fear of sounding like a douche, although it is the cheapest and highest-converting opportunity available.
  why: >-
    Business owners know what you are doing and wish their own team did it; nobody is offended by the ask, especially when it comes with a compliment, and the author puts over 30% of sales on this channel.
  anchor: >-
    Yet, few salespeople do it because they are afraid of sounding like a douche.
  source: >-
    acq-closer-handbook.md, Referrals, line 2503
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2503"
- id: D-closer-049
  type: rule
  name: >-
    The shipped scripts bend the rules on purpose
  statement: >-
    Some of the scripts in the appendix visibly break rules stated in the method, and the author names three reasons rather than treating them as errors.
  why: >-
    The philosophy is general and the scripts are tailored to one company's use cases, so a script is read against its process, its brand and its product.
  boundary: >-
    The author's own warning that his scripts are not a faithful rendering of his principles.
  anchor: >-
    Some of them appear to bend or break the rules we went over.
  source: >-
    acq-closer-handbook.md, Appendix: Script Bank, line 2638
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2638"
- id: D-closer-050
  type: rule
  name: >-
    A script is one part of a larger process
  statement: >-
    An element missing from one script is usually covered elsewhere in the process, so a single script is not evaluated on its own.
  why: >-
    The inbound closing script is light on the pain cycle because the prospect has to watch one or two videos before the call, so that section was trimmed without hurting close rates.
  boundary: >-
    A script may be copied only together with the process around it; lifting one out of that process removes the compensating steps.
  anchor: >-
    These scripts operate together as part of a larger sales process. So variables that aren’t covered in one are likely covered in another part of the process.
  source: >-
    acq-closer-handbook.md, Appendix: Script Bank, line 2640
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2640"
- id: D-closer-051
  type: rule
  name: >-
    The brand has already done some of the selling
  statement: >-
    These scripts assume many prospects already know the company, so part of the selling has happened before the call and the scripting accommodates that.
  why: >-
    Other variables have already made the horse more likely to drink, so the script does not have to do that work.
  boundary: >-
    The author's explicit caveat that his scripts suit a known brand and are not calibrated for a company the prospect has never heard of.
  anchor: >-
    Our brand is different from many companies. We have many prospects who already know who we are. This means that some selling has already occurred.
  source: >-
    acq-closer-handbook.md, Appendix: Script Bank, line 2641
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2641"
- id: D-closer-052
  type: rule
  name: >-
    Different products need different scripting
  statement: >-
    Just as different prospects require different scripting, so do different products, which is why all the elements are worth knowing even when a given script omits them.
  why: >-
    A script is fitted to its product; the elements are what transfer to future products and services.
  boundary: >-
    The author limits the transferability of a finished script and transfers the elements instead.
  anchor: >-
    Just as different prospects may require different scripting, so too do different products.
  source: >-
    acq-closer-handbook.md, Appendix: Script Bank, line 2642
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2642"
- id: D-closer-053
  type: rule
  name: >-
    A cash threshold before the appointment is set
  statement: >-
    When a budget objection turns into financial questions, the script continues to a booked consultant call only above a stated cash-on-hand or monthly cash-flow level.
  why: >-
    The rep is told upfront he would not be calling if the prospect did not meet the minimum revenue mark, and the financial questions confirm that a deal is possible at all.
  boundary: >-
    A qualification floor written into the script: below it the call does not proceed to a set.
  anchor: >-
    IF THEY HAVE $15K+ CASH OR $10K/MO CASH FLOW:
  source: >-
    acq-closer-handbook.md, ACQ Outbound Set Phone Script, OBSTACLES TO BOOK A MEETING, line 2847
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2847"
- id: D-closer-054
  type: rule
  name: >-
    No promises, no guarantees
  statement: >-
    The close call states before discovery that no rate of return or specific result is promised and that results will vary because the buyer does the work.
  why: >-
    The buyer, not the seller, does the work, so the outcome cannot be guaranteed; the same disclaimer is repeated inside the money-objection overcome.
  boundary: >-
    A claim limit the author writes into the script itself rather than leaving to the closer's discretion.
  anchor: >-
    we make no promises or guarantees of any rate of return or specific result.
  source: >-
    acq-closer-handbook.md, ACQ Closing Script, INTRO, line 3276
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3276"
- id: D-closer-055
  type: rule
  name: >-
    Stop pushing payment and BAMFAM
  statement: >-
    When every payment route has been offered and refused, the money objection is dropped and the call is converted into a booked next meeting.
  why: >-
    The author frames the exhausted attempts as covering all the bases; with no way to pay, the next step is a timeline, not another ask.
  boundary: >-
    The author's stop condition on the money objection, against the general rule of looping until the buy.
  anchor: >-
    IF NO AGAIN → All good haha— just wanted to cover all the bases. BAMFAM.
  source: >-
    acq-closer-handbook.md, Money Objections, line 3656
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3656"
```
