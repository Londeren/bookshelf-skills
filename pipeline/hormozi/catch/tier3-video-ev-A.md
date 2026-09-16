# Улов фазы 1 — Enterprise Value: fragments of four video transcripts (ярус 3), тип A: фреймворки

Группа `tier3-video-ev`, слаг `video-ev`, ярус 3. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **20** (экстрактор вернул 20, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `video-business-that-runs-without-you.md`, lecture | символы 4000–39500 | 1 | — |
| `video-business-that-runs-without-you.md`, zoom-out | символы 40321–44137 | 1 | — |
| `video-business-that-runs-without-you.md`, EV answer | символы 44492–47170 | 1 | — |
| `video-make-money-so-fast.md`, wealth alchemy | символы 31313–44384 | 1 | — |
| `video-13-years-no-bs-business-advice.md`, point 16 | символы 71372–73000 | 1 | — |
| `video-no-bs-business-advice-2026.md`, overextension | символы 67605–72500 | 1 | — |
| `video-13-years-no-bs-business-advice.md` (итого по файлу) | | | 2 |
| `video-business-that-runs-without-you.md` (итого по файлу) | | | 14 |
| `video-make-money-so-fast.md` (итого по файлу) | | | 2 |
| `video-no-bs-business-advice-2026.md` (итого по файлу) | | | 2 |

## Как собран файл

Экстрактор A (Frameworks) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier3-video-ev.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier3-video-ev-A.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: A-video-ev-001
  type: framework
  name: >-
    From frustrated Fred to wealthy William: the four steps
  statement: >-
    To turn a business that requires you into one that runs without you, work four steps in this order: a self-inventory of everything you do, trading doing for managing and leading, removing yourself from marketing, and then actually taking your 90 days off.
  structure:
    - >-
      do a self-inventory: list out everything you do, literally all of it
    - >-
      start trading doing for managing and leading
    - >-
      remove yourself from marketing, which fundamentally is acquisition
    - >-
      actually take your 90 days off, and something will break
  why: >-
    The author: a business that is valuable only to you is valueless to anyone else, and once it can make the profit without you it becomes something other people would want to buy, so the owner's wealth grows at the business multiple instead of at post-tax savings.
  applies_when: >-
    An owner-operated business whose owner wants to be able to leave it or sell it.
  anchor: >-
    So the first step of actually taking it from frustrated Fred to wealthy William is you do a self-inventory.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 2
  authors_caveat: >-
    The author walks the steps as a live lecture and recaps them twice in different words; the fourth step is the stress test rather than a fifth activity.
  anchor_at: "video-business-that-runs-without-you.md@9154"
- id: A-video-ev-002
  type: framework
  name: >-
    Step one: the self-inventory
  statement: >-
    Step one is a granular list of everything you do, with a project, a process or a person slotted against each item, the list red/yellow/greened, decision trees written, a money box drawn around the decisions, a scorecard and KPIs built, and a pass/fail test at the end.
  structure:
    - >-
      run a time study first, if you don't even know what you do
    - >-
      list out everything you do, literally all of it, as granular as humanly possible
    - >-
      slot a project, a process or a person against each item
    - >-
      red, yellow, green the list and solve greens first, then yellows, then reds
    - >-
      turn the decisions you make into if-this-then-that decision trees
    - >-
      create a box around how much money they are able to make decisions on
    - >-
      build the scorecard and the KPIs for the role
    - >-
      test them to make sure that they actually pass the KPI
  why: >-
    The author: turning each checklist item into something someone else can do, as granular as humanly possible, is how you get out of the day-to-day without breaking the machine.
  anchor: >-
    we put our big list together. We red, yellow, greened it. We then created a decision tree.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 2
  authors_caveat: >-
    The author gives the elements as he walks through them and only lists them as a sequence in the closing recap, which is the anchor used here.
  anchor_at: "video-business-that-runs-without-you.md@38587"
- id: A-video-ev-003
  type: framework
  name: >-
    Time study
  statement: >-
    Before you can delegate, run a time study: an Excel sheet with times down one side in 15-minute increments, a timer, and one word noted every 15 minutes about what you did.
  structure:
    - >-
      take an Excel sheet and write times on one side every 15 minutes
    - >-
      simply put in a timer
    - >-
      every 15 minutes just note what you did, one word
    - >-
      run it for a week
    - >-
      run the same study on a key person you have too much dependency on
  why: >-
    The author: it produces the list of stuff you then break into component parts, and it will be the most productive week of your life because you are proving to yourself that you are productive.
  applies_when: >-
    When you don't even know what you do, or when you have key man risk on a person who is super valuable to the business.
  anchor: >-
    You just take an Excel sheet and you write times on one side every 15 minutes and you simply put in a timer.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    The author says he thinks he should do this every single week and doesn't; no technology beyond a spreadsheet and a timer is required.
  anchor_at: "video-business-that-runs-without-you.md@9784"
- id: A-video-ev-004
  type: framework
  name: >-
    Project, process or person
  statement: >-
    Against every item on the inventory, install one of three things: a project, a process, or a person.
  structure:
    - >-
      a project: a onetime thing which sometimes creates a process
    - >-
      a process
    - >-
      a person who does this thing on a continuous basis
  why: >-
    The author: you probably already have people on your team who are underutilized, so some of the slots can simply be handed to a named person right away.
  anchor: >-
    So it's either a project, a process or a person that's going to installed in each of these little slots next to it.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@10973"
- id: A-video-ev-005
  type: framework
  name: >-
    Red, yellow, green
  statement: >-
    Colour-code every inventory item — green if you can hand it to somebody and teach them, yellow if it needs a one-time project or process you already know how to build, red if you don't know how or lack the person — and clear greens first, then yellows, then reds.
  structure:
    - >-
      green: I can give this to somebody, teach them how to do it, and they get this
    - >-
      yellow: there is a one-time project or process that I have to install here, but I can do it and I know how to do it
    - >-
      red: something I either don't know how to do, or a person that I know I need to have but don't have
    - >-
      solve these in green to reds: the greens you can get out quickly, the yellows take a little more time, the reds come once greens and yellows are done
  why: >-
    The author: the greens can be got out quickly, so the order is what makes the hand-off move rather than stall on the hardest items.
  anchor: >-
    The red is where it's something that I either don't know how to do or there's a person that I know I need to have, but I don't have. And so I solve these in green to reds because the greens you can get out quickly.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 2
  anchor_at: "video-business-that-runs-without-you.md@11806"
- id: A-video-ev-006
  type: framework
  name: >-
    If this then that: decision trees and the money box
  statement: >-
    Document the decisions as well as the tasks: write if-this-then-that rules of behaviour for the common scenarios, then set the money amount, with a total cap, under which the person can act independently, and use the monthly financials as the feedback loop.
  structure:
    - >-
      as the documentation comes up, start saying if this then that: rules of behavior, decision trees for common scenarios
    - >-
      somebody comes in and says they would like to change their card, their flavor, their billing cadence — this is how you do each
    - >-
      of the questions that come in, some require approval: decide the amount under which this person can act independently without your supervision
    - >-
      you can also put a cap on it, so they get a set number of shots to fix something in the business
    - >-
      you still have financials, and at the end of the month something that looks out of whack you can go check out
  why: >-
    The author: the more duplicatable the job and the more people in a function, the more standardized the questions become, so the common scenarios can be decided once in advance instead of escalated each time.
  applies_when: >-
    Duplicatable roles with recurring questions; the more complex the role, the more one-off the scenario and the less this applies.
  anchor: >-
    we want to start saying if this then that these are rules of behavior right they're decision trees for common scenarios
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 2
  authors_caveat: >-
    The thresholds the author names ($500, $1,000, $10,000, sometimes $100,000) depend on the size of your company, and he expects a feedback loop with mistakes in it: his own team ran $250,000 a month of five-star client dinners before the monthly bill caught it.
  anchor_at: "video-business-that-runs-without-you.md@12401"
- id: A-video-ev-007
  type: framework
  name: >-
    How do you and your role make the company money?
  statement: >-
    Build a role's scorecard from one question — how do you and your role make the company money — and for non-sales roles work it out by listing what bad work would cost, reversing each mistake into something that has to be done right, and measuring what percentage of the time it was.
  structure:
    - >-
      ask anybody in the business: how do you and your role make the company money
    - >-
      for an ancillary role, ask what the bad version of that work would cost the business
    - >-
      reverse each of these potential mistakes into the things that we have to do right
    - >-
      measure what percentage of the time each of them was done correctly
    - >-
      if that's 100% of the time, the person is making the company money, and here's how
  why: >-
    The author: if we are going to unlock some sort of decision tree we want to make sure it is unlocking value, and when people understand how what they do relates to how the company makes money it gives meaning to the impact they already have.
  anchor: >-
    And so, I'll give you a really powerful frame that you can talk to anybody in the business with. You can say, how do you and your role make the company money?
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 2
  authors_caveat: >-
    The author warns that many of your team will not be able to answer the question and that this will frighten you; he works the example live on the camera operator standing in front of him.
  anchor_at: "video-business-that-runs-without-you.md@16037"
- id: A-video-ev-008
  type: framework
  name: >-
    Shadow train, supervise, support their independence
  statement: >-
    Hand a task over in three steps — they watch you do it, they do it in front of you, then you support their independence, available but not involved — until the ad hoc consults fade and they own it completely.
  structure:
    - >-
      shadow train: this is where they watch you do it
    - >-
      you supervise them doing it: they do it in front of you
    - >-
      you support their independence: you're available but not involved
    - >-
      in the beginning there are a little more ad hoc calls, consults, help
    - >-
      over time those decisions get automated back down to them, and that's when the full handoff occurs: they own it completely
  why: >-
    The author: the handoff is only complete when they own it completely, and until then you are still the one the decisions come back to.
  anchor: >-
    So you'll shadow train. So this is where they watch you do it. The next is you supervise them doing it.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    The author accepts 80%, sometimes 60% as good as him at the point of handoff, as long as he has a clear path to the person getting better; his stated belief is that if he can do it right with part of his time, someone else can do it better with all of theirs.
  anchor_at: "video-business-that-runs-without-you.md@22699"
- id: A-video-ev-009
  type: framework
  name: >-
    Trading doing for managing and leading
  statement: >-
    Swap a month of doing hours for a fraction of that in managing hours, then replace yourself again by hiring a manager, until your job is recruiting A players, strategy and prioritisation, attracting talent and aligning incentives rather than doing the work.
  structure:
    - >-
      swap 200 hours a month of doing for 20 hours of managing: a tenth, a 10x improvement in leverage
    - >-
      replace yourself again by hiring a manager the next time, and trade the four hours for one hour
    - >-
      focus on recruiting A players, not on doing A player work
    - >-
      focus on the business, aka strategy and prioritization, not on the tactics of what we need to do today
    - >-
      your job becomes attracting talent and aligning incentives
  why: >-
    The author: you can outwork anyone in your business but you will not be able to outwork everyone — "I can do a mountain of work but I can't do Mount Everest. That requires more hands and more shovels."
  anchor: >-
    So you want to start trading doing for managing and leading. So here's the simple math behind this.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 2
  authors_caveat: >-
    The author is doing the arithmetic aloud and his own numbers slip inside the sentence (200 hours a month becomes "you go from 50 to five"); the ratio of leverage, not the figures, is what he is asserting.
  anchor_at: "video-business-that-runs-without-you.md@21240"
- id: A-video-ev-010
  type: framework
  name: >-
    The litmus tests of a business that runs without you
  statement: >-
    Test the business against an escalating ladder: does it burn down without me; can I leave for a month and come back to it intact; do I come back to it in a better position than I left it; can I take three months off and have it grow.
  structure:
    - >-
      the baseline: does it burn down without me
    - >-
      I can actually leave for a month and come back and it didn't burn down
    - >-
      you leave for a month and when you come back it's in a better position than it was when you left
    - >-
      the ultimate test: can you take three months off and have the business grow
  why: >-
    The author: a business that grows while you are away functions as a faster growing annuity for an investor, which gives them a big multiple, which is why they pay you lots of money for it.
  applies_when: >-
    The author calls this the simplest litmus test for brick and mortar owners deciding whether to open a second or third location.
  anchor: >-
    And that's kind of my my litmus test is the baseline is does it burn down without me.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 2
  authors_caveat: >-
    The author allows an exception for a super capped market where there is no way the business can grow, and warns that a business that is merely flat can go down as soon as the owner's attention moves, leaving double the liability and half the talent.
  anchor_at: "video-business-that-runs-without-you.md@21965"
- id: A-video-ev-011
  type: framework
  name: >-
    Seven ways to install marketing systems instead of founder ads
  statement: >-
    Replace direct-to-camera founder ads with standing processes that harvest marketing material the business already produces: community screenshots, incentivised testimonials, life cycle ads, documented delivery moments, paid support-chat testimonials, existing review sites, and the funny one-star reviews.
  structure:
    - >-
      a standard process weekly where you screenshot people saying nice things about you in the place where your customers gather
    - >-
      incentives for customers to leave testimonials: unlockables, a certain amount of credit, trials of a higher tier of service
    - >-
      life cycle ads: pull the existing recordings of a customer's journey and compress them into a timeline
    - >-
      key moments of client deliverable: a ribbon cutting, a reveal of their new kitchen, them getting on the scale, monthly financials
    - >-
      pay a customer support person five bucks for every mini testimonial they get in chat format
    - >-
      turn your existing Google reviews, Yelp reviews, trust advisor reviews and Amazon reviews into marketing
    - >-
      take the hilarious one stars and say: if you're one of these people, you won't like our stuff
  why: >-
    The author: if your face gets the customers you are the key man, the revenue drops when you leave, and to make an important business you have to become less important.
  applies_when: >-
    Founder-led companies where the owner is the breadwinner, the promoter and the one who brings the business in.
  anchor: >-
    There are seven different ways that you can install systems into the business to capture media and marketing on your behalf without it having kind of quote direct to camera founder ads.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    The author names the ways as he goes rather than reading a numbered list, and counts "six or seven" himself at the end, so this list is assembled from the walkthrough. He adds an affiliate program and whitelisted TikTok shop ads as further options beyond the seven.
  anchor_at: "video-business-that-runs-without-you.md@33830"
- id: A-video-ev-012
  type: framework
  name: >-
    Life cycle ads
  statement: >-
    When a customer gives a testimonial, pull the recordings your business already makes — sales call, onboarding, delivery checkpoints — and compress their journey into a timeline that becomes the advertisement.
  structure:
    - >-
      you probably record your sales calls
    - >-
      hopefully you record your onboarding calls for a new customer
    - >-
      you record delivery checkpoints
    - >-
      if they have a good experience, you record some sort of testimonial from them
    - >-
      when a testimonial comes in, look back through the CRM and the scheduling and pull the recordings from their sales call to their onboarding to each of their touch points
    - >-
      compress that into a timeline that also becomes another advertisement
  why: >-
    The author: instead of the customer saying "I was here and now I'm here", it shows them actually being scared, not sure, hesitating before signing up, and then getting the outcome.
  anchor: >-
    the next one is something I call life cycle ads, which basically you probably already have functions in the business that already occur, which is you probably record your sales calls.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    The author's point is that the raw material already exists in the business; he does not say how the timeline is cut.
  anchor_at: "video-business-that-runs-without-you.md@34875"
- id: A-video-ev-013
  type: framework
  name: >-
    Three legs to the stool
  statement: >-
    Every business needs three big functional leaders: one in charge of acquisition, one in charge of delivery, and one running the internal operations that support the other two.
  structure:
    - >-
      one person who's in charge of getting customers: acquisition
    - >-
      a second person who's in charge of delivery and getting those customers exactly what was promised
    - >-
      a third to run the internal operations of the business: the day-to-day, legal, HR, contracts, paying people on time, the CRM that collects all this information
  why: >-
    The author: operations functions as a vendor to the other two heads and should never be making the big decisions in the business, only supporting the decisions that let us get more customers or deliver on them better; and having one throat to choke, one chest to poke per function is what makes each function owned.
  anchor: >-
    number 16 there are three legs to the stool and so every business needs three big functional leaders
  source: >-
    video-13-years-no-bs-business-advice.md, point 16
  confirmations: 1
  authors_caveat: >-
    Stated once, as point 16 of a numbered list in a talk; the author notes the picture is different "in the beginning", but the fragment cuts off before he says how.
  anchor_at: "video-13-years-no-bs-business-advice.md@71372"
- id: A-video-ev-014
  type: framework
  name: >-
    The only three things you can do to increase Enterprise Value
  statement: >-
    There are exactly three levers on enterprise value — get more customers, make them worth more, and decrease risk in the business — and they map one to one onto acquisition, delivery and operations.
  structure:
    - >-
      you can get more customers: acquisition
    - >-
      you can make them worth more: delivery
    - >-
      you can decrease risk in the business: operations
  why: >-
    The author: if everything is completely dialed, there is no massive risk, we can get as many customers as we please and our LTV can continue to scale, that is a valuable business.
  anchor: >-
    those three legs of the stool roll up to the only three things that you can do to increase Enterprise Value in business you can get more customers you can make them worth more
  source: >-
    video-13-years-no-bs-business-advice.md, point 16
  confirmations: 1
  anchor_at: "video-13-years-no-bs-business-advice.md@72319"
- id: A-video-ev-015
  type: framework
  name: >-
    Wealth alchemy
  statement: >-
    Wealth alchemy is the arbitrage chain from the cost of a permanent customer through the annual recurring revenue that customer produces to the enterprise value multiple the business trades at: the cash and the enterprise value both accrue, and the enterprise value grows untaxed until you sell.
  structure:
    - >-
      what it costs to get someone to start a free trial
    - >-
      the rate at which trials become customers, which gives the cost to get a customer
    - >-
      the rate at which customers become permanent customers, which gives the permanent CAC
    - >-
      the annual revenue or annual recurring revenue that customer produces
    - >-
      the multiple the business trades at, for example 10 times topline for a B2B SaaS business with good retention metrics
    - >-
      the arbitrage between the permanent cost of acquiring customers, the annual value, and the enterprise value multiple
  why: >-
    The author: it's not either or, it's an and — you get the cash and the enterprise value, and the enterprise value is tax free until the day you sell, which is how a software company goes from nothing to a multi-billion dollar thing in four years.
  applies_when: >-
    A business with a permanent, recurring or reoccurring customer base, where the permanent conversion rate can be measured.
  anchor: >-
    it's literally just a massive Arbitrage between the permanent cost of acquiring customers relative to the annual value relative to the Enterprise Value multiple
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 2
  authors_caveat: >-
    The author is calculating live on a whiteboard and the arithmetic in the transcript slips ("$122,000" and "worth1 120 million" where his own chain gives $12,000 per customer and $120 million), and EBITDA is transcribed as "eida". He stresses the multiple depends on the vehicle: the same $900 permanent CAC and $1,200 a year is worth 10x topline in software and about 7x profit in a business valued on the bottom line. This is a transcript, tier 3: it does not override the books.
  anchor_at: "video-make-money-so-fast.md@34536"
- id: A-video-ev-016
  type: framework
  name: >-
    The big picture in three: value, cash forward, wealth alchemy
  statement: >-
    The whole game in three moves: sell off value with the value equation so you are out of the price war; pull the cash forward and speed the cash conversion cycle so customers finance acquisition; then play wealth alchemy on the permanent customers you keep.
  structure:
    - >-
      we have to sell off a value, use the value equation to make things less risky, faster and easier for the customers, so we are decoupled from a race to the bottom price war
    - >-
      once we know what our premium price is, pull that cash forward and speed up the cash conversion cycle so that capital is not the limiter of the business and we get customers on demand, profitably — customer financed acquisition
    - >-
      understand the game of wealth alchemy: what percentage of the customers we acquire become permanent, that reoccurring base is what we are valued on, and then the arbitrage between what a permanent customer costs and the enterprise value multiple
  why: >-
    The author: what an investor values is the same value equation the customer buys on — how likely this is to occur, how much effort and sacrifice it takes, and the time delay before the outcome — so a business that keeps customers is a far less risky business and carries the multiple.
  anchor: >-
    so the big picture here is that number one we have to sell off a value we have to use the value equation to make things less risky faster and easier for the customers
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 1
  authors_caveat: >-
    The first two moves are named here as a recap of the video; they are worked through outside this fragment, so only the third is developed in the source read here.
  anchor_at: "video-make-money-so-fast.md@41608"
- id: A-video-ev-017
  type: framework
  name: >-
    The phone test and the six-month test
  statement: >-
    Backfill yourself with an operator, hand them your phone for a month against an override or equity on the deal that it does not ring, role-play the scenarios until they stop calling you, and then run the real test — six straight months in which the business maintains or grows without your direct involvement.
  structure:
    - >-
      you have to have somebody who's going to operate behind you: backfill yourself
    - >-
      at the very least do a one-month test: go away for a month
    - >-
      show your phone to your operator: you get this override on the business, a little profit share or some stock, in exchange for this not ringing
    - >-
      role play it out: a pipe bursts, you call the plumber directly; if it's an emergency call 911; either way don't call me
    - >-
      the six-month test: the business has to either maintain or grow for six straight months without your direct involvement
  why: >-
    The author: owners mistakenly think CEO and owner mean the same thing — you happen to be both, but they are not the same — and when the CEO leaves the business stops running as well, so somebody has to operate behind you.
  applies_when: >-
    An owner who has pulled himself out of selling, customer service and delivery and yet still works every hour of the day, which means the other stuff he does is operating the business.
  anchor: >-
    and the six-month test I was alluding to is the business has to either maintain or grow for six straight months without your direct involvement
  source: >-
    video-no-bs-business-advice-2026.md, overextension
  confirmations: 2
  authors_caveat: >-
    The author warns the test is void if you keep working in the day-to-day through it: "you just didn't change what you did at all". The name "the phone test" is given in the business-that-runs-without-you lecture, where he promises to explain it later and never returns to it; the mechanics come from the later stream.
  anchor_at: "video-no-bs-business-advice-2026.md@71719"
- id: A-video-ev-018
  type: framework
  name: >-
    The two solutions to overextension
  statement: >-
    An overextended owner has exactly two ways out: hire incredibly impressive people, giving up your own income to bring them on, or prune the tree — cut the losses, reconcentrate, get it right, and scale back out again the right way.
  structure:
    - >-
      you either have to hire incredibly impressive people, which means you're going to probably give up your income in order to bring this person on
    - >-
      or you cut your losses, prune the tree, reconcentrate, get it right, and then scale back out again the right way
  why: >-
    The author: overextension is typically a who problem — you don't have enough good people that you left behind who can actually run it without you.
  applies_when: >-
    The author sees it a lot in the $1 to $3 million range, though it happens at all ranges, because that is where the owner has pulled himself out of the day-to-day but not out of operating.
  anchor: >-
    so what do you do honestly you have two solutions you either have to hire incredibly impressive people which means that you're going to probably give up your income in order to bring this person on
  source: >-
    video-no-bs-business-advice-2026.md, overextension
  confirmations: 2
  anchor_at: "video-no-bs-business-advice-2026.md@69134"
- id: A-video-ev-019
  type: framework
  name: >-
    There's levels to this game
  statement: >-
    Enterprise value becomes the objective only once cash flow has covered the owner's own needs, in a set order — rent, the house, the parents' house, the cars, the kids' schools, the upgrades, the vacation — and if you don't know where next month's rent is coming from it is the wrong game to play.
  structure:
    - >-
      pay your rent
    - >-
      pay your house off
    - >-
      pay for your parents house
    - >-
      pay for their cars and your cars and your kids' schools
    - >-
      upgrade all my cars
    - >-
      then the vacation
    - >-
      then the most efficient tax vehicle for building wealth, which is your enterprise value
  why: >-
    The author: by the time a business actually has enterprise value it has usually already generated more than sufficient cash flow for the owner, and all the excess is transferred to him in a tax inefficient manner; a high value enterprise can also be borrowed against, gives lines of credit, becomes an asset and lets you raise capital on it.
  applies_when: >-
    Business owners who are trying to get bigger and trying to scale; explicitly not someone who does not know where next month's rent is coming from.
  anchor: >-
    And so said differently, there's levels to this game. If you want to move up levels, you need to play a different game.
  source: >-
    video-business-that-runs-without-you.md, EV answer
  confirmations: 1
  authors_caveat: >-
    Said once, as a live answer to a commenter who preferred hard cash to enterprise value; the ladder is assembled from the author's spoken enumeration rather than given by him as a list. He adds that this is not the only game in life worth winning, only that in the game of business net worth is the objective measure.
  anchor_at: "video-business-that-runs-without-you.md@46329"
- id: A-video-ev-020
  type: framework
  name: >-
    Experience and track record, and the ability to sell the future
  statement: >-
    The level of talent you can attract, and therefore the size of business that can run without you, rests on two things — your experience and track record, and your ability to sell the future — and where the track record is missing you generalise to traits or go and build the proof first.
  structure:
    - >-
      your experience and track record
    - >-
      your ability to sell the future
    - >-
      an amazing ability to sell the future can outsell the fact that they don't have a crazy track record
    - >-
      with no specific track record, generalize to traits — valedictorian, president of three different things, proving you are generically ambitious — and then get specific again on the business
    - >-
      for mere mortals: show the proof first, build the smaller company to prove you can build something a hundred times as big
  why: >-
    The author: no really big business can have one person involved in everything, so you have to decentralize decision-making to very smart, very capable people — and the problem is that those people don't want to work for you unless you are someone they would want to follow.
  anchor: >-
    And that's going to be a combination of two things. Your experience and track record and your ability to sell the future.
  source: >-
    video-business-that-runs-without-you.md, zoom-out
  confirmations: 1
  authors_caveat: >-
    Said once, as the closing zoom-out behind all the tactics of the lecture; the author's own evidence is that he had to build Gym Launch before the talent he can attract at acquisition.com became possible, and that developing that reputation takes time.
  anchor_at: "video-business-that-runs-without-you.md@42182"
```
