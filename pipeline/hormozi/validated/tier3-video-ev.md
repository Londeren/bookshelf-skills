# Enterprise Value: fragments of four video transcripts — ярус 3, группа `tier3-video-ev`, единиц после валидации: 26

Часть `pipeline/hormozi/validated.md` (там шапка, гейт, список валидаторов и правила обращения с якорем). Блоки перенесены из `pipeline/hormozi/catch/tier3-video-ev-<X>.md` байт в байт; фазой 2 дописаны `tier`, `merged_from` и поднятое `confirmations`. Проверка: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/validated/tier3-video-ev.md`.


## A. Фреймворки — 15

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
  confirmations: 4
  authors_caveat: >-
    The author walks the steps as a live lecture and recaps them twice in different words; the fourth step is the stress test rather than a fifth activity.
  anchor_at: "video-business-that-runs-without-you.md@9154"
  tier: 3
  merged_from: [B-video-ev-023, D-video-ev-021]
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
  confirmations: 4
  authors_caveat: >-
    The author gives the elements as he walks through them and only lists them as a sequence in the closing recap, which is the anchor used here.
  anchor_at: "video-business-that-runs-without-you.md@38587"
  tier: 3
  merged_from: [B-video-ev-001, E-video-ev-003]
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
  confirmations: 3
  authors_caveat: >-
    The author says he thinks he should do this every single week and doesn't; no technology beyond a spreadsheet and a timer is required.
  anchor_at: "video-business-that-runs-without-you.md@9784"
  tier: 3
  merged_from: [B-video-ev-002, E-video-ev-004]
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
  confirmations: 3
  anchor_at: "video-business-that-runs-without-you.md@10973"
  tier: 3
  merged_from: [B-video-ev-003, E-video-ev-005]
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
  confirmations: 4
  anchor_at: "video-business-that-runs-without-you.md@11806"
  tier: 3
  merged_from: [B-video-ev-004, E-video-ev-006]
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
  confirmations: 10
  authors_caveat: >-
    The thresholds the author names ($500, $1,000, $10,000, sometimes $100,000) depend on the size of your company, and he expects a feedback loop with mistakes in it: his own team ran $250,000 a month of five-star client dinners before the monthly bill caught it.
  anchor_at: "video-business-that-runs-without-you.md@12401"
  tier: 3
  merged_from: [B-video-ev-005, B-video-ev-006, C-video-ev-003, C-video-ev-004, D-video-ev-005, D-video-ev-006, D-video-ev-007, E-video-ev-007]
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
  confirmations: 6
  authors_caveat: >-
    The author warns that many of your team will not be able to answer the question and that this will frighten you; he works the example live on the camera operator standing in front of him.
  anchor_at: "video-business-that-runs-without-you.md@16037"
  tier: 3
  merged_from: [B-video-ev-007, B-video-ev-008, C-video-ev-005, D-video-ev-008]
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
  confirmations: 5
  authors_caveat: >-
    The author is doing the arithmetic aloud and his own numbers slip inside the sentence (200 hours a month becomes "you go from 50 to five"); the ratio of leverage, not the figures, is what he is asserting.
  anchor_at: "video-business-that-runs-without-you.md@21240"
  tier: 3
  merged_from: [B-video-ev-010, C-video-ev-006, D-video-ev-004]
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
  confirmations: 5
  authors_caveat: >-
    The author allows an exception for a super capped market where there is no way the business can grow, and warns that a business that is merely flat can go down as soon as the owner's attention moves, leaving double the liability and half the talent.
  anchor_at: "video-business-that-runs-without-you.md@21965"
  tier: 3
  merged_from: [B-video-ev-013, B-video-ev-014, D-video-ev-013]
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
  confirmations: 8
  authors_caveat: >-
    The author names the ways as he goes rather than reading a numbered list, and counts "six or seven" himself at the end, so this list is assembled from the walkthrough. He adds an affiliate program and whitelisted TikTok shop ads as further options beyond the seven.
  anchor_at: "video-business-that-runs-without-you.md@33830"
  tier: 3
  merged_from: [B-video-ev-020, B-video-ev-021, C-video-ev-010, C-video-ev-011, D-video-ev-019, D-video-ev-020, E-video-ev-011]
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
  confirmations: 4
  authors_caveat: >-
    The author's point is that the raw material already exists in the business; he does not say how the timeline is cut.
  anchor_at: "video-business-that-runs-without-you.md@34875"
  tier: 3
  merged_from: [B-video-ev-022, C-video-ev-009, E-video-ev-012]
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
  confirmations: 2
  anchor_at: "video-13-years-no-bs-business-advice.md@72319"
  tier: 3
  merged_from: [B-video-ev-033]
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
  confirmations: 5
  authors_caveat: >-
    The author is calculating live on a whiteboard and the arithmetic in the transcript slips ("$122,000" and "worth1 120 million" where his own chain gives $12,000 per customer and $120 million), and EBITDA is transcribed as "eida". He stresses the multiple depends on the vehicle: the same $900 permanent CAC and $1,200 a year is worth 10x topline in software and about 7x profit in a business valued on the bottom line. This is a transcript, tier 3: it does not override the books.
  anchor_at: "video-make-money-so-fast.md@34536"
  tier: 3
  merged_from: [C-video-ev-015, D-video-ev-029, E-video-ev-016]
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
  confirmations: 9
  authors_caveat: >-
    The author warns the test is void if you keep working in the day-to-day through it: "you just didn't change what you did at all". The name "the phone test" is given in the business-that-runs-without-you lecture, where he promises to explain it later and never returns to it; the mechanics come from the later stream.
  anchor_at: "video-no-bs-business-advice-2026.md@71719"
  tier: 3
  merged_from: [B-video-ev-036, B-video-ev-037, C-video-ev-023, D-video-ev-038, D-video-ev-039, E-video-ev-010, E-video-ev-027]
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
  confirmations: 4
  anchor_at: "video-no-bs-business-advice-2026.md@69134"
  tier: 3
  merged_from: [B-video-ev-038, E-video-ev-024]
```


## B. Правила и критерии — 7

```yaml
- id: B-video-ev-009
  type: rule
  name: >-
    The 80% test
  statement: >-
    A person is graduated onto a role only by passing a test showing that at 80% of the owner's skill they still produce 100% of the result.
  why: >-
    Nobody does it as well as you with one tenth of the reps, but someone who learns only the right way without your bad mistakes can start at half your level; if you can do it right with part of your time, someone else can do it better with all of theirs.
  anchor: >-
    The next thing is we have to have some sort of test to graduate the person which is can someone 80% as you get 100% of the result.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 3
  authors_caveat: >-
    At the start the author accepts 80% and sometimes 60% as good, as long as there is a clear path to the person getting better.
  anchor_at: "video-business-that-runs-without-you.md@18926"
  tier: 3
  merged_from: [D-video-ev-003, D-video-ev-009]
- id: B-video-ev-026
  type: rule
  name: >-
    Cash flow first, then enterprise value
  statement: >-
    Enterprise value is the goal only once the business already covers the owner's cash needs; if you do not know where next month's rent comes from, it is not your game yet.
  why: >-
    By the time a business actually has enterprise value it has already generated more than sufficient cash flow for the owner, and the excess cash flow it keeps transferring to the owner is taxed inefficiently.
  applies_when: >-
    The author addresses business owners trying to get bigger and scale; the bigger you get and the more the needs around you are satisfied, the more enterprise value matters.
  anchor: >-
    Once a business actually has enterprise value, it usually has already generated or had the ability to generate more than sufficient cash flow for the owner.
  source: >-
    video-business-that-runs-without-you.md, EV answer
  confirmations: 4
  anchor_at: "video-business-that-runs-without-you.md@45148"
  tier: 3
  merged_from: [C-video-ev-013, D-video-ev-026, D-video-ev-028]
- id: B-video-ev-027
  type: rule
  name: >-
    Enterprise value as the wealth vehicle
  statement: >-
    Wealth is accumulated by growing the value of what you own rather than by taking profit as income, and profit is reinvested into the business instead of being chased through tax strategy.
  why: >-
    Income is taxed to oblivion with zero multiplication, while growth in enterprise value is untaxed until sale and compounds; the same extra $500,000 of profit adds $250,000 after tax to one owner and $3 million of net worth at a 6x multiple to the other; a high-value enterprise can also be borrowed against, used for lines of credit and raised on.
  anchor: >-
    Then you want the most efficient tax vehicle for building wealth, which is your enterprise value.
  source: >-
    video-business-that-runs-without-you.md, EV answer
  confirmations: 8
  anchor_at: "video-business-that-runs-without-you.md@46051"
  tier: 3
  merged_from: [C-video-ev-021, D-video-ev-002, D-video-ev-027, D-video-ev-033, E-video-ev-013]
- id: B-video-ev-030
  type: rule
  name: >-
    Pick the opportunity vehicle by the multiple
  statement: >-
    Choose the business vehicle by what a dollar of its revenue is worth at exit, since identical acquisition cost and identical annual revenue produce very different enterprise value under a topline multiple than under a profit multiple.
  why: >-
    In the author's worked comparison the same $900 permanent CAC and $1,200 a year of revenue is worth ten times topline in a B2B SaaS with good retention and roughly 7x EBITDA in a business valued on profit, so the same effort buys a far larger asset in the first vehicle.
  applies_when: >-
    Topline multiples of that size assume good retention metrics, which is why permanent customers matter to the choice.
  anchor: >-
    this is why picking a good opportunity vehicle because in both of these situations you still spent the $900 per customer
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 4
  authors_caveat: >-
    Worked live with round numbers; EBITDA appears in the transcript as eida.
  anchor_at: "video-make-money-so-fast.md@35791"
  tier: 3
  merged_from: [C-video-ev-016, D-video-ev-030, E-video-ev-018]
- id: B-video-ev-031
  type: rule
  name: >-
    Advertise to the avatar that stays
  statement: >-
    Advertising is re-aimed at the avatar that actually becomes permanent, even at a higher cost per customer, as long as the cost per permanent customer falls.
  why: >-
    Changing the advertising to attract only those customers raises the hit rate: a CAC that doubles but converts one in three instead of one in ten costs $600 per permanent customer instead of $1,000.
  applies_when: >-
    You have measured which share of customers become permanent and can see how the permanent ones differ from the other nine.
  anchor: >-
    if we changed our advertising and attracted only those types of customers we would be able to get a higher hit rate on that
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 2
  anchor_at: "video-make-money-so-fast.md@41306"
  tier: 3
  merged_from: [C-video-ev-020]
- id: B-video-ev-032
  type: rule
  name: >-
    Operations is a vendor to the other two legs
  statement: >-
    The internal operations leader supports acquisition and delivery and never makes the big decisions of the business.
  why: >-
    Operations exists to support the other two functions, the things that keep you out of prison and keep the machine running, and its decisions should be the ones that let the business get more customers or deliver on them better.
  applies_when: >-
    A business with the three functional leaders in place: acquisition, delivery, and internal operations.
  anchor: >-
    that person should never be making the big decisions in the business
  source: >-
    video-13-years-no-bs-business-advice.md, point 16
  confirmations: 2
  anchor_at: "video-13-years-no-bs-business-advice.md@72105"
  tier: 3
  merged_from: [D-video-ev-034]
- id: B-video-ev-034
  type: rule
  name: >-
    Overextension is a who problem
  statement: >-
    Before adding a second unit, check that a person good enough to run the existing one without you is already in place; if not, the expansion is a who problem and is not made.
  why: >-
    Opening the second location while the first is not really running well drops the first location's revenue, splits the star person and the owner across two sites, and leaves the same profit with twice the risk; opening a third compounds it.
  applies_when: >-
    The author sees it most in the $1M to $3M range, where the owner is already out of selling and delivery and therefore assumes wrongly that the business does not need them.
  anchor: >-
    overextension is typically a who problem which is you don't have enough good people that you left behind who can actually run it without you
  source: >-
    video-no-bs-business-advice-2026.md, overextension
  confirmations: 7
  anchor_at: "video-no-bs-business-advice-2026.md@69476"
  tier: 3
  merged_from: [B-video-ev-015, C-video-ev-022, D-video-ev-011, D-video-ev-012, D-video-ev-035, E-video-ev-025]
```


## C. Разборы (кейсы) — 1

```yaml
- id: C-video-ev-001
  type: case
  name: >-
    Frustrated Fred and Wealthy William
  statement: >-
    Two businesses are identical on paper, $10 million topline and $2 million bottom line, but Fred is required at work 80 hours a week while William's team runs his day to day; Fred pays 50% tax and living expenses and adds about $500,000 a year to his net worth, William's business trades at six times profit and is therefore worth $12 million, so the absentee owner is far richer on the same profit and loss.
  why: >-
    A business that runs without its owner is valuable to anyone rather than only to the owner, which makes it something other people will buy, and only what can be bought carries a multiple; income accumulates linearly and is taxed, ownership does not.
  demonstrates: >-
    A business that requires you is not a business; the same profit is worth a multiple once the owner is not required.
  anchor: >-
    And so of these two guys, this guy adds $500,000 to his net worth every year. This guy has a business that is worth $12 million. This guy's way richer.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 3
  authors_caveat: >-
    The author builds the figures live on a board and tells the listener to remove zeros if the scale is uncomfortable; the six times multiple is his illustration, not a stated benchmark.
  anchor_at: "video-business-that-runs-without-you.md@7563"
  tier: 3
  merged_from: [C-video-ev-002, E-video-ev-002]
```


## E. Глоссарий — 3

```yaml
- id: E-video-ev-014
  type: term
  name: >-
    Permanent customer
  statement: >-
    A permanent customer is one who, once acquired, never leaves — in practice the author counts anyone who has been with you two plus years as permanent.
  definition: >-
    One out of three customers becomes a permanent customer, meaning once they get on our subscription they never leave; within the context of what we're talking about, somebody who's been with you two plus years is a permanent customer.
  why: >-
    The recurring base built from permanent customers is what the business is valued on, so every acquisition dollar should be measured against it rather than against a first sale.
  anchor: >-
    now let's say that we know one out of three customers becomes a permanent customer meaning once they get on our subscription they never leave
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 2
  anchor_at: "video-make-money-so-fast.md@32054"
  tier: 3
- id: E-video-ev-015
  type: term
  name: >-
    Permanent CAC
  statement: >-
    Permanent CAC is the cost of acquiring one permanent customer — the ordinary cost per customer divided by the share of customers who stay permanently.
  definition: >-
    If a customer costs $300 and one out of three becomes permanent, the permanent CAC is somewhere close to $900; more generally, take how much it costs to get a customer and multiply it by the number of customers it takes to get one that stays.
  why: >-
    It is the number the enterprise value arbitrage is computed against, and knowing it lets you accept a higher CAC for an avatar that converts to permanent at a better rate — a $600 permanent CAC at one in three beats a cheaper customer at one in ten.
  not_to_confuse_with: >-
    Plain CAC, the cost of acquiring a customer who may churn; the author builds permanent CAC out of it in two multiplications.
  anchor: >-
    which would mean that our permanent CAC is somewhere close to $900
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 5
  authors_caveat: >-
    Calculated live on a whiteboard with round illustration numbers; one of the enterprise value figures in this passage is garbled in the transcript.
  anchor_at: "video-make-money-so-fast.md@32196"
  tier: 3
  merged_from: [B-video-ev-029, C-video-ev-014, C-video-ev-019]
- id: E-video-ev-026
  type: term
  name: >-
    Owner is not CEO
  statement: >-
    Owner and CEO are two different roles that one person happens to hold: the owner holds the asset, the CEO operates it, and a business only runs without you once someone else is backfilled into the CEO half.
  definition: >-
    A lot of owners will mistakenly think that CEO and owner mean the same thing; you happen to be both, but they are not the same.
  why: >-
    If you work every hour of the day and you are not selling and not delivering, then the other stuff you are doing is very much operating the business — so when you leave, the business stops running as well because the CEO is gone.
  not_to_confuse_with: >-
    Each other — this is the confusion the author names outright.
  anchor: >-
    a lot of owners will mistakenly think that CEO and owner mean the same thing you happen to be both but they are not the same
  source: >-
    video-no-bs-business-advice-2026.md, overextension
  confirmations: 4
  anchor_at: "video-no-bs-business-advice-2026.md@70330"
  tier: 3
  merged_from: [B-video-ev-035, D-video-ev-036, D-video-ev-037]
```
