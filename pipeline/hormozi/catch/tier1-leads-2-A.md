# Улов фазы 1 — $100M Leads (2023), from #4 Run Paid Ads to the end (lines 6901–14623) (ярус 1), тип A: фреймворки

Группа `tier1-leads-2`, слаг `leads-2`, ярус 1. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **49** (экстрактор вернул 49, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-leads.md` | 6901–14623 | 7 | 49 |

## Как собран файл

Экстрактор A (Frameworks) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier1-leads-2.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier1-leads-2-A.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: A-leads-2-001
  type: framework
  name: >-
    The four problems paid ads give us to solve
  statement: >-
    A paid ad campaign is built by solving four problems in order: knowing where to advertise, getting the right audience to see it, making the best ad for them to see, and getting permission to contact them.
  why: >-
    If an ad isn't profitable, most of the time it's because the right people never saw it, so each step narrows who sees the ad until the highest possible share of viewers are the right people.
  applies_when: >-
    Setting up paid advertising on any platform.
  structure:
    - >-
      Knowing where to advertise
    - >-
      Getting the right audience to see it
    - >-
      Making the best ad for them to see
    - >-
      Getting permission to contact them
  anchor: >-
    Paid ads give us four new problems to solve. Let's break them down
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, lines 7110–7127
  confirmations: 2
  anchor_at: "100m-leads.md:7110"
- id: A-leads-2-002
  type: framework
  name: >-
    Find a platform where these four things are true
  statement: >-
    A platform is worth advertising on when all four hold: you have used it and got value from it as a consumer, you can target people on it interested in your stuff, you know how to format ads specific to it, and you have the minimum amount of money to place an ad.
  why: >-
    Having used the platform yourself means you have some idea how it works, and the four conditions together are what stay constant while the platforms themselves keep changing.
  applies_when: >-
    Choosing the first platform to advertise on; start with one platform that meets the four requirements.
  structure:
    - >-
      I've used it and gotten value from it as a consumer. So I have some idea how it works.
    - >-
      I can target people on the platform interested in my stuff.
    - >-
      I know how to format ads specific to the platform.
    - >-
      I have the minimum amount of money to spend to place an ad.
  anchor: >-
    what I look for in a platform I want to advertise on:
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step 1, lines 7133–7167
  confirmations: 1
  authors_caveat: >-
    ...And yes, platforms change all the time, but these principles stay the same.
  anchor_at: "100m-leads.md:7148"
- id: A-leads-2-003
  type: framework
  name: >-
    Two ways to target inside a platform
  statement: >-
    Within the chosen platform there are two targeting methods, usable separately or combined: a lookalike audience built from a list you upload, and filters of your own choosing (age, income, gender, interests, time, location).
  why: >-
    The more filters you use, the more specific the list; the more specific the list, the more efficient the ads but the faster you burn through it, and the wins from smaller specific audiences fund advertising to larger, broader audiences later.
  applies_when: >-
    After the platform is picked — the second round of targeting.
  structure:
    - >-
      Target a lookalike audience. Start with your list of current and previous customers; if it's not big enough add your warm reach out list, then your cold reach out leads to hit the platform minimum.
    - >-
      Target with factors of your choosing. Targeting options include: age, income, gender, interests, time, location, etc.
  anchor: >-
    Modern advertising platforms have two ways to target. You can use them
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #2, lines 7211–7269
  confirmations: 1
  anchor_at: "100m-leads.md:7213"
- id: A-leads-2-004
  type: framework
  name: >-
    The three chunks of an ad: Call Out + Value + Call to Action
  statement: >-
    Every ad is made of three chunks in this order: a call out so they notice it, value elements so they get interested, and a call to action so they know what to do next.
  why: >-
    Those three things have to happen for advertising to work — they have to notice the ad, get a reason to act now rather than later, and have a way to give permission to be contacted — so they became the three core elements of every ad the author creates.
  applies_when: >-
    Writing any ad, paid or not; the only difference between long and short ads is how many angles the value chunk covers, while callouts and CTAs stay the same.
  structure:
    - >-
      Call Outs - I need to get them to notice my ad
    - >-
      Value - I need to get them interested in what I have to offer
    - >-
      Calls to Action - I need to tell them what to do next
  anchor: >-
    Let's use the three chunks to make an ad.
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #3, lines 7275–7309; restated lines 7990–8004
  confirmations: 2
  anchor_at: "100m-leads.md:7295"
- id: A-leads-2-005
  type: framework
  name: >-
    Four verbal callouts
  statement: >-
    Verbal callouts — using words to get attention — come in four kinds: Labels, Yes-Questions, If-Then Statements and Ridiculous Results.
  why: >-
    Callouts harness the cocktail party effect and cut through the noise; if they never notice your ad, nothing else matters, and the first impression is the part of the ad the author tests the most.
  applies_when: >-
    Writing the headline or first five seconds of an ad; make callouts specific enough to get the right people and broad enough to get as many of them as you can.
  structure:
    - >-
      Labels: A word or set of words putting people into a group — features, traits, titles, places and other descriptors the ideal customer identifies with (LOCAL AREA + TYPE OF PERSON for local ads).
    - >-
      Yes-Questions: Questions where if people answer "yes, that's me" they qualify themselves for the offer.
    - >-
      If-Then Statements: If they meet your conditions then you help them make a decision.
    - >-
      Ridiculous Results: Bizarre, rare, or out of the ordinary stuff someone would want.
  anchor: >-
    Here's what I look for with verbal callouts-
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #3 Call Out, lines 7359–7404
  confirmations: 1
  authors_caveat: >-
    Now, this isn't an exhaustive list. Far from it. I show you these to pull back the curtain.
  anchor_at: "100m-leads.md:7359"
- id: A-leads-2-006
  type: framework
  name: >-
    Three nonverbal callouts
  statement: >-
    Nonverbal callouts — using the setting and spokesperson to get attention — come in three kinds: Contrast, Likeness and The Scene.
  why: >-
    Callouts don't have to be just words; they can be noises or visuals in the environment, and if the platform allows, good advertisers use verbal and nonverbal callouts together.
  applies_when: >-
    Any ad format that carries images, video or sound.
  structure:
    - >-
      Contrast: Any stuff that "sticks out" in the first few seconds. The colors. The sounds. The movements etc.
    - >-
      Likeness: Think visually showing labels — features, traits, titles, places, and other descriptors that people identify with. Quack like a duck.
    - >-
      The Scene: Think showing the Yes-Questions and If-Then statements.
  anchor: >-
    Here's what I look for with nonverbal callouts-
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #3 Call Out, lines 7420–7517
  confirmations: 1
  authors_caveat: >-
    Now, this isn't an exhaustive list. Far from it.
  anchor_at: "100m-leads.md:7420"
- id: A-leads-2-007
  type: framework
  name: >-
    The What-Who-When Framework
  statement: >-
    To answer why a prospect should be interested, run the offer through three lenses in order: The What (the eight key elements of value and their opposites), The Who (whose perspective experiences them), and The When (past, present and future).
  why: >-
    Putting the What, the Who and the When together answers WHY they should be interested; each new who-perspective applied to each value driver produces a fresh angle, and the more angles you cover, the more interested they become.
  applies_when: >-
    Writing the value chunk of an ad, once the callout has their attention; it hinges on knowing the value equation forwards and backwards.
  structure:
    - >-
      The What: Eight Key Elements — how the offer fulfills each element of value and how it helps avoid their hidden costs.
    - >-
      The Who: show how the eight key things change your prospect's status, and how the people they know give status to them or take it away.
    - >-
      The When: get the prospect to see the consequences of buying and not buying through their past, present, and future.
  anchor: >-
    share with you my What-Who-When Framework. This mental framework hinges
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #3 Get Them Interested, lines 7539–7841
  confirmations: 2
  anchor_at: "100m-leads.md:7553"
- id: A-leads-2-008
  type: framework
  name: >-
    The What: Eight Key Elements
  statement: >-
    Know eight things about your product: the four value elements and the four opposites — Dream Outcome / Nightmare, Perceived Likelihood of Achievement / Risk, Time Delay / Speed, Effort and Sacrifice / Ease — and show both in the ad.
  why: >-
    The best ads make the benefits look as big as possible and the costs look as small as possible; carrots and sticks, how your offer delivers more good stuff and less bad stuff.
  applies_when: >-
    The What lens of the What-Who-When framework.
  structure:
    - >-
      Dream Outcome: show and tell the maximum benefit the prospect can achieve using the thing you sell.
    - >-
      Opposite - Nightmare: show the worst possible hassles, pain, etc. of going without your solution.
    - >-
      Perceived Likelihood of Achievement: lower perceived risk with success of people like them, authority, guarantees.
    - >-
      Opposite - Risk: show how risky it is to not act, how they will repeat their past failures.
    - >-
      Time Delay: show how slow their current trajectory is or that they'll never get what they want at their current rate.
    - >-
      Opposite - Speed: show and tell how much faster they will get the thing they want.
    - >-
      Effort and Sacrifice: show the work and skill they'll need to get the result without your solution.
    - >-
      Opposite - Ease: tell and show how you can avoid the stuff you hate doing without working hard, or having a lot of skill, and still get the dream outcome.
  anchor: >-
    Those are the 8 key elements. Now we fully understand
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, The What, lines 7580–7656
  confirmations: 2
  anchor_at: "100m-leads.md:7653"
- id: A-leads-2-009
  type: framework
  name: >-
    The Who: two groups of people
  statement: >-
    Outline two groups: the people gaining status (your customers) and the people giving it to them — Spouse, Kids, Parents, Extended Family, Colleagues, Bosses, Friends, Rivals, Competitors — then talk about the value elements from each of their perspectives.
  why: >-
    Humans are primarily status driven, and the status of one human comes from how the other humans treat them; talking about the value elements from someone else's perspective shows all the ways the product improves the customer's status and surfaces bonus benefits you'd miss looking only from their own perspective.
  applies_when: >-
    The Who lens of the What-Who-When framework; apply each new who-perspective to each value driver.
  structure:
    - >-
      The first group is the people gaining status, your customers.
    - >-
      The second group is the people giving it to them: Spouse, Kids, Parents, Extended Family, Colleagues, Bosses, Friends, Rivals, Competitors, etc.
  anchor: >-
    outline two groups of people. The first group is the people gaining
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Who, lines 7664–7703
  confirmations: 1
  anchor_at: "100m-leads.md:7670"
- id: A-leads-2-010
  type: framework
  name: >-
    The When: past, present, future
  statement: >-
    Run each value element and each who-perspective through the prospect's own timeline — what their decisions led to in the past, what they live with in the present, and what their decisions could lead to in the future.
  why: >-
    People often only think of how their decisions affect the here and now; visualizing the whole timeline helps them see the consequences of their decision, or indecision, right now.
  applies_when: >-
    The When lens of the What-Who-When framework; the same timeline can also be run through someone else's perspective.
  structure:
    - >-
      past
    - >-
      present
    - >-
      future
  anchor: >-
    getting them to visualize through their own timeline
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, When, lines 7716–7752
  confirmations: 2
  anchor_at: "100m-leads.md:7721"
- id: A-leads-2-011
  type: framework
  name: >-
    The Three Phases of Scaling Paid Ads
  statement: >-
    Spending on ads goes through three phases in order: Track Money (set up accurate tracking before spending a dollar), Lose Money (budget losses while you find a winner), Print Money (once you make back more than you spend, reverse the budget from your sales goals).
  why: >-
    Without tracking you get cleaned out, like playing a casino game for as long as you feel like rather than as long as you can afford; the number of losses is high but small because you know when to shut it down, and the wins are few but big because you know when to hit the gas.
  applies_when: >-
    Deciding how much to spend on paid ads.
  structure:
    - >-
      Phase One: Track Money
    - >-
      Phase Two: Lose Money
    - >-
      Phase Three: Print Money
  anchor: >-
    There are three stages to spending money on ads as I see
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8066–8198
  confirmations: 1
  authors_caveat: >-
    In the Lose Money phase the author budgets two times the cash he collects from a customer in thirty days (not LTGP) to test a new ad, and shuts an ad off before 1x thirty-day cash if it produces no leads at all.
  anchor_at: "100m-leads.md:8071"
- id: A-leads-2-012
  type: framework
  name: >-
    Two big levers to improving LTGP:CAC
  statement: >-
    There are only two levers on the LTGP-to-CAC ratio: make CAC lower by getting cheaper customers through more efficient ads, and make LTGP higher by increasing how much you make per customer through a better business model.
  why: >-
    Entrepreneurs often think they have crappy ads (high CAC) when in reality they have a crappy business model (low LTGP); costs can only approach zero but how much you make can go up to infinity.
  applies_when: >-
    Use the industry average CAC as the guide: if your CAC is below 3x your industry average, focus on your business model (LTGP); if it is above 3x the average, focus on your advertising (CAC).
  structure:
    - >-
      Make CAC lower - Get cheaper customers. We do this with more efficient ads.
    - >-
      Make LTGP higher - Increase how much you make per customer. We do this with a better business model.
  anchor: >-
    You have two big levers to improving LTGP:CAC:
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, Cost & Returns, lines 8261–8316
  confirmations: 2
  authors_caveat: >-
    Every business the author invests in that struggles to scale had an LTGP to CAC ratio below 3 to 1 — "This is a pattern I personally observed, not a rule." (2023 figures)
  anchor_at: "100m-leads.md:8261"
- id: A-leads-2-013
  type: framework
  name: >-
    More, Better, New
  statement: >-
    Any of the core four can be boosted in three ways, in this order: do more of what you're currently doing, do what you're currently doing better, and do it somewhere new.
  why: >-
    Even with no improvements, doubling the inputs gets more engaged leads, and the biggest increases often come from advertising more; better and more work with each other, and only once more–better are exhausted do the real returns come from new.
  applies_when: >-
    You are already doing the core four and still not getting as many engaged leads as you want.
  structure:
    - >-
      You can do more of what you're currently doing.
    - >-
      You can do what you're currently doing better.
    - >-
      You can do it somewhere new.
  anchor: >-
    you advertise more? Could you advertise better? Could you advertise
  source: >-
    100m-leads.md, Core Four On Steroids: More Better New, lines 8720–8771; summary lines 9163–9190
  confirmations: 3
  anchor_at: "100m-leads.md:8762"
- id: A-leads-2-014
  type: framework
  name: >-
    The Rule of 100
  statement: >-
    Do 100 primary actions every day, for one hundred days in a row, in whichever of the core four you have chosen.
  why: >-
    The author's one promise: if you do 100 primary actions per day for 100 days straight, you will get more engaged leads; most people dramatically underestimate the volume it takes to make advertising work.
  applies_when: >-
    The "More" of More Better New; step #2 of the one page advertising checklist offers a choice between the Rule of 100 and Open To Goal.
  structure:
    - >-
      Warm Reach Outs: 100 reach outs per day (email, text, direct message, calls, etc.)
    - >-
      Post Content: 100 minutes per day making content, releasing at least one per day on a platform.
    - >-
      Cold Reach Outs: 100 reach outs per day (email, text, direct message, cold call, flyers, etc.); expect lower response rates, so use automation.
    - >-
      Paid Ads: 100 minutes per day making paid ads, and 100 days straight of running those paid ads.
  anchor: >-
    The rule of 100 is simple. You advertise your stuff by doing 100
  source: >-
    100m-leads.md, Core Four On Steroids, More, lines 8805–8887
  confirmations: 2
  anchor_at: "100m-leads.md:8810"
- id: A-leads-2-015
  type: framework
  name: >-
    One test per week per platform — the Monday testing schedule
  statement: >-
    Every Monday run one split test per platform, give it a week, and the next Monday do three things: pick the winners, write the result into a log of all tests, and design the next test to beat the current best version.
  why: >-
    Testing several things at once on one platform means you never learn what worked, steps affect each other, one test per week forces you to prioritise, and a week is long enough to see whether the improvement is real.
  applies_when: >-
    The "Better" of More Better New; do the most testing at whatever step the most leads drop off — the constraint.
  structure:
    - >-
      Every Monday we run one split test per platform.
    - >-
      Look at the results, and pick the winners for each platform test.
    - >-
      Then (important), we write down the results of the test in a log of all tests.
    - >-
      Come up with our next test to beat our current 'best' version.
  anchor: >-
    In every company I own, I set up a testing schedule. Every Monday we
  source: >-
    100m-leads.md, Core Four On Steroids, Better, lines 8912–9035
  confirmations: 1
  authors_caveat: >-
    If we can't beat the version we're currently running in four tries (or one month), we move onto the next constraint; one week is long enough given the size of the author's team and ad spend.
  anchor_at: "100m-leads.md:9009"
- id: A-leads-2-016
  type: framework
  name: >-
    New placements → New Platforms → New Core Four
  statement: >-
    When you go "new", expand in this rough order: new placements on a platform you know, then a new platform, then an entirely new core four activity.
  why: >-
    The order comes down to one thing — what will get the most leads for the amount of work; nine times out of ten that is placements first, platforms second, a new core four activity last.
  applies_when: >-
    When the returns you get from doing more and better are lower than what you could get from a new placement or new way of advertising.
  structure:
    - >-
      New placements
    - >-
      New Platforms
    - >-
      New Core Four
  anchor: >-
    ]{.calibre3}[new]{.calibre24}[. Use this rough order: new placement, new
  source: >-
    100m-leads.md, Core Four On Steroids, New, lines 9104–9157 (the order itself at line 9130)
  confirmations: 2
  anchor_at: "100m-leads.md:9154"
- id: A-leads-2-017
  type: framework
  name: >-
    Four scenarios of leverage
  statement: >-
    Leverage in advertising comes in four scenarios: you are the lead getter; you get a lead getter; you get lots of lead getters; you get a lead getter who gets lead getters.
  why: >-
    Leverage boils down to how much you get for the time you spend getting it; when other people do the core four for you, you get more engaged leads for less work, and a lead getter who recruits lead getters keeps leads climbing without you working.
  applies_when: >-
    Deciding how to grow lead flow beyond your own capacity.
  structure:
    - >-
      Scenario #1: You are the lead getter. Work: HIGH Leads: LOW Leverage: LOW
    - >-
      Scenario #2: You get a lead getter. Work: LOW. Leads: LOW. Leverage: HIGH.
    - >-
      Scenario #3: You get lots of lead getters. Work: HIGH. Leads: HIGH. Leverage: HIGHER.
    - >-
      Scenario #4: You get a lead getter who gets lead getters. Work: LOW. Leads: HIGH. Leverage: HIGHEST.
  anchor: >-
    Scenario #4: You get a lead getter who gets lead getters.
  source: >-
    100m-leads.md, Section IV: Get Lead Getters, lines 9351–9420
  confirmations: 1
  anchor_at: "100m-leads.md:9402"
- id: A-leads-2-018
  type: framework
  name: >-
    The four lead getters
  statement: >-
    Four kinds of other people advertise your stuff for you: Customers, Employees, Agencies and Affiliates; you do the core four to get them, and then they do the core four on your behalf.
  why: >-
    All four let other people know about your stuff, so all four are higher leverage than doing it on your own; the core four stacks — once to get them, and a second time when the lead getters get engaged leads for you.
  applies_when: >-
    Scaling past what one person can advertise; the author puts them in the order they arise naturally — referrals, employees, agencies, affiliates.
  structure:
    - >-
      #1 Customers - they buy your stuff then tell other people about it to get you leads. Biggest potential for low-cost exponential growth.
    - >-
      #2 Employees - people in your business that get you leads. They have your direct influence and run your business on your behalf.
    - >-
      #3 Agencies - businesses with services that get you leads. They teach skills you keep forever and can transfer to your team.
    - >-
      #4 Affiliates - businesses who tell their audiences about your stuff to get you leads. Once you get them going, they can operate entirely on their own.
  anchor: >-
    [#1 Customers]{.calibre11}[- they buy your stuff then tell other people
  source: >-
    100m-leads.md, Section IV: Get Lead Getters, lines 9464–9486; restated Section IV Conclusion, lines 13259–13278
  confirmations: 2
  anchor_at: "100m-leads.md:9464"
- id: A-leads-2-019
  type: framework
  name: >-
    The referral growth equation
  statement: >-
    Referrals (in) minus churned customers (out) decides whether word of mouth grows the business: referrals greater than churn means you grow without any other advertising, equal means you need other advertising, less means you advertise just to break even.
  why: >-
    With the core four, inputs and outputs are roughly linear; with word of mouth one customer brings two, two bring four, so growth is exponential and can be maintained no matter how big you get — which is why so few scale on word of mouth: they lose customers faster than they get them.
  applies_when: >-
    Measuring whether your product can grow the business on referrals alone; figure out your referral percentages and churn percentages to set a baseline.
  structure:
    - >-
      If referrals are greater than churn: you grow without any other advertising (yay!)
    - >-
      If referrals are equal to churn: you need other advertising to grow your business (meh)
    - >-
      If referrals are less than churn: you've got to advertise to break even (boo - most folks)
  anchor: >-
    get them. Look at the referral growth equation to see it in action.
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, lines 9813–9842
  confirmations: 1
  anchor_at: "100m-leads.md:9815"
- id: A-leads-2-020
  type: framework
  name: >-
    Two Reasons Most Businesses Don't Get Referrals
  statement: >-
    Most businesses don't get referrals for two reasons: their product isn't as good as they think it is, and they don't ask for them.
  why: >-
    If your product were exceptional, people would already know about it and you'd have more business than you could handle; and customers, like any audience, can only know what to do if you tell them.
  applies_when: >-
    Diagnosing why word of mouth is not producing leads; the two reasons map onto the chapter's two remedies — six ways to give more value, and seven ways to ask.
  structure:
    - >-
      Problem #1: The Product Isn't Good Enough
    - >-
      They never ask for them
  anchor: >-
    Most businesses don't get referrals for two reasons. First, their
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 9856–9862; conclusion lines 10602–10616
  confirmations: 2
  anchor_at: "100m-leads.md:9860"
- id: A-leads-2-021
  type: framework
  name: >-
    Six Ways To Get More Referrals By Giving More Value
  statement: >-
    Six ways to build the goodwill that produces referrals, mapped one-to-one onto the parts of an ad: sell better customers, set better expectations, get more people better results, get faster results, keep making your stuff better, and tell them what to buy next.
  why: >-
    The difference between price and value is goodwill; lots of goodwill creates word of mouth, and word of mouth means referrals — and since you can only lower price so far for so long, the question is not how to lower price but how to give more value.
  applies_when: >-
    Before or alongside asking for referrals; building goodwill does a fantastic job of getting referrals on its own.
  structure:
    - >-
      Call Outs → Sell Better Customers
    - >-
      Dream Outcome → Set Better Expectations
    - >-
      Increase Perceived Likelihood of Achievement → Get More People Better Results
    - >-
      Decrease Time Delay → Get Faster Results
    - >-
      Decrease Effort and Sacrifice → Keep Making Your Stuff Better
    - >-
      Call to Action → Tell Them What To Buy Next
  anchor: >-
    There are six ways I get referrals by giving more value. And it just so
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 9944–10291
  confirmations: 2
  anchor_at: "100m-leads.md:9949"
- id: A-leads-2-022
  type: framework
  name: >-
    The process to get more people better results (six steps)
  statement: >-
    Find what your best customers did and make everyone do it: survey, interview, find the common actions, force new customers to repeat them, measure the improvement, and match your guarantee's conditions to those actions.
  why: >-
    The customers with the best results get the most value from your product; at Gym Launch, gym owners who ran paid ads and made a sale in the first seven days tripled their LTGP, so getting everyone to do that lifted average results, testimonials and referrals.
  applies_when: >-
    Way #3 of the six ways to give more value (Increase Perceived Likelihood of Achievement).
  structure:
    - >-
      Step #1: Survey customers to find the ones who got the best results.
    - >-
      Step #2: Interview them to find out what they did differently.
    - >-
      Step #3: Look at the actions they had in common.
    - >-
      Step #4: Force new customers to repeat the actions that got the best results.
    - >-
      Step #5: Measure the improvement in average customer results (speed and outcome)
    - >-
      Step #6: Match the conditions of your guarantee to the actions that get the best results to get more people to do them.
  anchor: >-
    Here's the process I use to get more people better results:
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10069–10141
  confirmations: 1
  anchor_at: "100m-leads.md:10097"
- id: A-leads-2-023
  type: framework
  name: >-
    Five ways to make wins happen faster
  statement: >-
    To make wins feel faster, give them more often: split deliverables into shorter intervals, treat updates as wins, force wins in the first forty-eight hours, always book the next contact, and set timelines with breathing room so you deliver early.
  why: >-
    Faster wins increase their perception of speed, increase the likelihood they'll stick, and increase how much they trust you; if someone said seven things would happen and all seven do, referring a friend becomes lower risk.
  applies_when: >-
    Way #4 of the six ways to give more value (Decrease Time Delay).
  structure:
    - >-
      If I have seven small things to deliver, I deliver them at shorter intervals rather than all at once.
    - >-
      Updates are wins. If it's a bigger project, I share progress updates as frequently as possible.
    - >-
      Customers form their lasting impression of a business within the first forty-eight hours after they buy. Force as many wins as you can in that window.
    - >-
      They should always know the next time they'll hear from you. BAMFAM: Book-A-Meeting-From-A-Meeting.
    - >-
      Never expect customers to forgive you. You can deliver early, but never late. I add fifty percent to my timelines so I always deliver early.
  anchor: >-
    Here's five ways I make wins happen faster in the real
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10147–10198
  confirmations: 1
  anchor_at: "100m-leads.md:10164"
- id: A-leads-2-024
  type: framework
  name: >-
    The process to keep making your stuff better (six steps)
  statement: >-
    Run a recurring monthly loop on the product: find the most common problem from service data, surveys and reviews; design the fix with feedback from customers who made it work anyway; implement; release to a small group of struggling customers; re-test; then move to the next most common problem.
  why: >-
    There's no such thing as a perfect product — you can always make it better, and the easier you make it for customers to benefit, the more goodwill you get and the more likely they'll refer.
  applies_when: >-
    Way #5 of the six ways to give more value (Decrease Effort & Sacrifice); set it as a recurring monthly process.
  structure:
    - >-
      Step #1: Use customer service data, surveys, and reviews to find the most common problem with your product.
    - >-
      Step #2: Figure out your fix. Get feedback from the customers who made your product work for them despite the problem it has.
    - >-
      Step #3: Use that feedback to improve your product.
    - >-
      Step #4: Give the new version to a small group of your (struggling) customers.
    - >-
      Step #5: Get your next round of feedback. If you solved the original problem, roll it out to all customers. If it didn't, go back to step #2.
    - >-
      Step #6: Move to the next most common problem and repeat the process. Do this until the end of time.
  anchor: >-
    the more likely they'll refer. Here's my process to keep making
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10206–10251
  confirmations: 1
  anchor_at: "100m-leads.md:10213"
- id: A-leads-2-025
  type: framework
  name: >-
    Three components of a referral program
  statement: >-
    Every referral program is built from three components: how you give the incentive, what you incentivize with, and how you ask.
  why: >-
    Asking for referrals only works when you treat it like an offer — the referrals come when you show the value the customer gets when they refer their friends.
  applies_when: >-
    Designing a referral program; the author's seven ways to ask are combinations of these three components.
  structure:
    - >-
      how you give the incentive
    - >-
      what you incentivize with
    - >-
      how you ask
  anchor: >-
    There are three components to a referral program: how you give the
  source: >-
    100m-leads.md, #1 Customer Referrals, Referrals: Ask For Them, lines 10394–10397
  confirmations: 1
  anchor_at: "100m-leads.md:10394"
- id: A-leads-2-026
  type: framework
  name: >-
    Seven Ways To Ask For Referrals
  statement: >-
    Seven combinations of incentive, currency and ask that worked best: one-sided referral benefit, two-sided referral benefits, ask right when they buy, referrals as a negotiation chip, referral events, ongoing referral programs, and unlockable referral bonuses.
  why: >-
    Referring is always a risk for the customer — they risk their goodwill with their friend — so you add benefits for them and their friends with incentives and lower the risk by building goodwill; done this way Dropbox 39x'd in fifteen months and PayPal reached a million users in two years.
  applies_when: >-
    After building goodwill with the six ways to give more value — capitalize on that goodwill by asking.
  structure:
    - >-
      One-Sided Referral Benefit: pay your average CAC to the referrer or the friend, and ask for an actual three-way introduction right when they buy.
    - >-
      Two-Sided Referral Benefits: pay the CAC to both parties, half to the referrer and half to the friend (what Dropbox and PayPal used).
    - >-
      Ask For A Referral Right When They Buy: on the sales contract or checkout page, ask for names and phone numbers of people they'd like to do this with.
    - >-
      Add Referrals As A Negotiation Chip: give a discount in exchange for an introduction to three friends — you changed the terms of the sale.
    - >-
      Referral Events: points, credits, dollars or bragging rights for bringing friends within an explicit time period, typically one to four weeks.
    - >-
      Ongoing Referral Programs: talk about the benefits of doing things with others all the time, in free content, outreach, paid ads, etc.
    - >-
      Unlockable Referral Bonuses: bonuses for people who 1) refer and 2) leave a testimonial — VIP bonuses, courses, tokens, status, training, merchandise, premium support.
  anchor: >-
    you a hundred variations that may or may not work, here are the seven
  source: >-
    100m-leads.md, #1 Customer Referrals, Seven Ways To Ask For Referrals, lines 10389–10542
  confirmations: 1
  anchor_at: "100m-leads.md:10396"
- id: A-leads-2-027
  type: framework
  name: >-
    The Internal Core Four
  statement: >-
    Getting employees is the same advertising you already do, with the frame changed from potential customers to potential employees: warm outreach becomes asking your network, cold outreach becomes recruiting, posting content becomes posting job openings, paid ads become promoting job postings, and the lead getters map across too.
  why: >-
    Employees are just other people you let know about your stuff, so the actions to get employees line up with the actions to get customers — and like getting customers, you can build a reliable process, and when you need more you do more.
  applies_when: >-
    You need more workers in order to advertise more; you need both processes to scale.
  structure:
    - >-
      Warm Outreach→Asking Your Network
    - >-
      Cold Outreach→ Recruiting
    - >-
      Post Content→Posting Job Openings
    - >-
      Paid Ads→Promoting Job Postings
    - >-
      Customer Referrals→Employee Referrals
    - >-
      Affiliates→ Associations, Guilds, Listservs etc.
    - >-
      Agencies→ Staffing firms etc.
    - >-
      Employees→Employees (unchanged)
  anchor: >-
    Remember the core four? Well, they work for getting employees too.
  source: >-
    100m-leads.md, #2 Employees, How To Get Employee Leads, lines 11003–11058
  confirmations: 1
  anchor_at: "100m-leads.md:11007"
- id: A-leads-2-028
  type: framework
  name: >-
    The 3Ds: document, demonstrate, duplicate
  statement: >-
    Train an employee to get leads in three steps: document the job as a checklist written exactly as you do it, demonstrate by walking them through the checklist step by step, then have them duplicate it while you observe and fix the checklist.
  why: >-
    If the checklist is right, the outcome will be the same, and if it's off you'll find out fast; the level of clarity to shoot for is that a stranger could get your results if they only followed your checklist.
  applies_when: >-
    Turning a hired employee into a lead-getter, when you cannot afford people who already know how.
  structure:
    - >-
      Step One - Document. You make a checklist. Follow it yourself on a work block and see if you can do an A+ job following only your own directions — that's the first draft.
    - >-
      Step Two - Demonstrate: You do it in front of them. Walk them through the checklist step by step, adjusting it wherever they stop or slow you down — the second draft.
    - >-
      Step Three - Duplicate: They do it in front of you. They follow the same checklist while you observe; fix the checklist until it's right, then have them follow it until they get it right.
  anchor: >-
    activities. I think about and actually approach training with this 3Ds
  source: >-
    100m-leads.md, #2 Employees, How To Get Employees To Get You Leads, lines 11074–11137
  confirmations: 1
  authors_caveat: >-
    If they get it wrong or get confused then we got it wrong or made it confusing; but there is a difference between competence and performance — if the instructions are fine they just need practice.
  anchor_at: "100m-leads.md:11080"
- id: A-leads-2-029
  type: framework
  name: >-
    How to Calculate Returns From Lead-Getting Employees
  statement: >-
    Excluding paid ad spend, compare payroll with what the leads bring: total payroll divided by total engaged leads gives cost per engaged lead, multiplied by engaged leads per customer gives CAC, and LTGP divided by CAC gives the ratio.
  why: >-
    The cost of advertising with employees (outreach, content, etc.) is almost entirely the money you pay them to do it, so payroll against engaged leads is the whole calculation.
  applies_when: >-
    Measuring employee lead-getting; as long as your total costs of getting a customer are at least one-third of the lifetime profit, you're in good shape.
  structure:
    - >-
      Total Payroll / Total Engaged Leads = Cost per engaged lead.
    - >-
      (cost per engaged lead) x (engaged leads per customer) = CAC
    - >-
      (LTGP) / (CAC) = your LTGP : CAC ratio
  anchor: >-
    this by just comparing how much money we spend on payroll to how much
  source: >-
    100m-leads.md, #2 Employees, How to Calculate Returns, lines 11205–11248
  confirmations: 1
  anchor_at: "100m-leads.md:11212"
- id: A-leads-2-030
  type: framework
  name: >-
    Advertising problem or sales problem — one diagnostic question
  statement: >-
    When CAC is more than 3x industry average, ask one question — do my engaged leads have the problem I solve and the money to spend? — and branch: not qualified is an advertising problem; qualified and buying but too few is an advertising problem; qualified and not buying is a sales problem.
  why: >-
    Don't fire your sales guy if you've got advertising problems, and don't fire your advertising employees if you've got a sales problem; one company spent twelve weeks and $150,000 on ads that worked fine, blamed advertising, and the confusion cost an estimated ~$30M in enterprise value.
  applies_when: >-
    Your cost to get a customer is more than 3x the industry average; within 3x means you're doing good enough and should bump up LTGP instead.
  structure:
    - >-
      If no, then they're not qualified--that's an advertising problem.
    - >-
      They're buying but you don't have enough of them--advertising problem.
    - >-
      They're qualified but not buying--sales problem.
  anchor: >-
    Do my engaged leads have the problem I solve and the money to
  source: >-
    100m-leads.md, #2 Employees, Which Employees to Focus On, lines 11259–11291; Personal Lessons from Paid Ads, lines 8463–8475
  confirmations: 2
  anchor_at: "100m-leads.md:11272"
- id: A-leads-2-031
  type: framework
  name: >-
    How I Use Agencies Now — buy the skill, then leave
  statement: >-
    Start every agency relationship with a stated purpose and a deadline: work with them for about six months to learn how they do it, pay extra for them to explain their decisions, train your team on it, run both teams until yours beats theirs, then drop to a lower-cost consulting arrangement and finally cut them loose.
  why: >-
    You get better short-term results because they probably know more than you, and better long-term results because you or your team learn to do it; you only get a fraction of the agency's attention and results get worse whenever they take on new clients, while your team stays focused on you full-time.
  applies_when: >-
    As soon as you have enough money for a good agency, and specifically for two things: learning new methods and learning new platforms.
  structure:
    - >-
      Decide if using an agency makes sense for you right now.
    - >-
      Talk to a lot of agencies to get a feel for the market. Don't be cheap.
    - >-
      Use the agreement framework I outlined.
    - >-
      Set a clear deadline to force you (and your team) to learn the skills.
    - >-
      Use both teams until yours beats theirs regularly.
    - >-
      Switch to discounted consulting until you feel like you're teaching them instead of them teaching you...then cut 'em loose.
  anchor: >-
    start every agency relationship with a purpose and a deadline to fulfill
  source: >-
    100m-leads.md, #3 Agencies, lines 11676–11745; Next Steps, lines 11894–11921
  confirmations: 2
  authors_caveat: >-
    To make it work at scale you have to count on a good amount of time where you pay the agency and your team to do the same stuff; the author's time to get a team as good as an agency went from about a year down to six months or less.
  anchor_at: "100m-leads.md:11683"
- id: A-leads-2-032
  type: framework
  name: >-
    What I look for in a good agency (ten checks)
  statement: >-
    A list of ten things all the good agencies had in common — word-of-mouth referrals, recognisable clients, a waiting list, a clear sales process with realistic expectations, long-term strategy over hacks, clarity about what they need from you, a regular meeting schedule, simple tracked reporting, a good offer by the four value elements, and a high price.
  why: >-
    If you only know about an agency from their paid ads or cold outreach, they probably aren't as good as the ones who rely solely on word of mouth; and all good agencies are expensive, but not all expensive agencies are good.
  applies_when: >-
    Comparing agencies before signing; talk with a few more even if one already agrees to your terms.
  structure:
    - >-
      Somebody I know got good results working with them.
    - >-
      Prominent companies got good results working with them.
    - >-
      A waiting list. When demand for a service exceeds the supply, they are probably pretty good.
    - >-
      A clear sales process that makes a point to set realistic expectations. No funny business.
    - >-
      No short term hacks. They keep the talk on long term strategy, with clear timelines for setup, scaling, and results.
    - >-
      They tell me exactly what they need from me, when they need it, and how they use it.
    - >-
      They suggest a regular schedule of meetings and offer several ways to update me on their progress.
    - >-
      They give updates in simple terms and have clear ways to track so I know how costs compare with results.
    - >-
      They make a good offer: dream outcome, perceived likelihood of achievement, time delay, effort and sacrifice.
    - >-
      They are expensive. All good agencies are expensive... but not all expensive agencies are good.
  anchor: >-
    After working with tons of bad agencies, and a handful of good ones, I
  source: >-
    100m-leads.md, #3 Agencies, How to Pick The Right Agency, lines 11763–11836
  confirmations: 1
  authors_caveat: >-
    Now it isn't the last word on what makes a good agency, but it is useful stuff that's worked for me.
  anchor_at: "100m-leads.md:11763"
- id: A-leads-2-033
  type: framework
  name: >-
    How To Build An Affiliate Army in Six Steps
  statement: >-
    Building an affiliate army runs through six steps in order: find your ideal affiliates, make them an offer, qualify them, figure out what to pay them, get them advertising, and keep them advertising.
  why: >-
    Affiliates are among the most advanced ways to get engaged leads — first you have to convince them to advertise someone else's stuff, second to advertise yours, third to keep advertising so they become a long-term lead source.
  applies_when: >-
    Recruiting other businesses to tell their audiences about your stuff; the author built ALAN and Prestige Labs this way, together more than $75,000,000 in revenue from over 5000+ affiliates.
  structure:
    - >-
      Step 1: Find Your Ideal Affiliates
    - >-
      Step 2: Make Them an Offer
    - >-
      Step 3: Qualify Them
    - >-
      Step 4: Figure Out What To Pay Them
    - >-
      Step 5: Get Them Advertising
    - >-
      Step 6: Keep Them Advertising
  anchor: >-
    How To Build An Affiliate Army in Six Steps
  source: >-
    100m-leads.md, #4 Affiliates and Partners, lines 12174–12215
  confirmations: 1
  anchor_at: "100m-leads.md:12174"
- id: A-leads-2-034
  type: framework
  name: >-
    Find Your Ideal Affiliate — the questions
  statement: >-
    The ideal affiliate has a business with a warm audience full of people like your customers; find them by asking, about your best customers, what they buy, where they go, what they like to do, and — if you sell direct to consumer — what businesses they work for.
  why: >-
    In a nutshell the question is "Who's got my leads!?" — once you know the businesses that have your leads, you know exactly where to put your advertising efforts.
  applies_when: >-
    Step 1 of building an affiliate army; if none come to mind, answer these questions about your best customers, and if you struggle, call up your customers and ask them.
  structure:
    - >-
      What do they buy? → Who provides that stuff?
    - >-
      Where do they go? → What businesses are in those surrounding areas?
    - >-
      What do they like to do? → Who provides those services?
    - >-
      If direct to consumer: What types of businesses do they work for? What kinds of jobs do they have?
  anchor: >-
    The ideal affiliate has a business with a warm audience full of people
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 1, lines 12226–12286
  confirmations: 1
  anchor_at: "100m-leads.md:12230"
- id: A-leads-2-035
  type: framework
  name: >-
    The six affiliate hit list categories
  statement: >-
    Every new affiliate hit list starts from six categories of business around your customer: softwares, products, equipment, services, groups they belong to, and events they attended.
  why: >-
    If you find a business that falls into multiple categories, there's a high chance they've got lots of good leads for you and that they'd make a great affiliate.
  applies_when: >-
    Building the affiliate lead list in Step 1; the author made a list of 200 products and services for agencies when starting ALAN and they fit neatly into these categories.
  structure:
    - >-
      softwares
    - >-
      products
    - >-
      equipment
    - >-
      services
    - >-
      groups they belong to
    - >-
      events they attended
  anchor: >-
    Every time I create a new affiliate "hit list" I start with these
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 1, lines 12264–12273
  confirmations: 1
  anchor_at: "100m-leads.md:12270"
- id: A-leads-2-036
  type: framework
  name: >-
    Two ways to get affiliates invested: make them a customer, make them an expert
  statement: >-
    Qualify a potential affiliate by getting them to invest — make them buy and preferably use the product to keep affiliate status, and make them pay for the onboarding and training that certifies them as a product expert.
  why: >-
    Nine times out of ten, if they pay, they'll pay attention; the more money an affiliate invests in your product the more money they make, and certification covers some of the advertising cost and pays for proper onboarding of every single affiliate.
  applies_when: >-
    Step 3 of building an affiliate army. If you don't get enough people to start, lower the commitment; if you don't get enough people to follow through, raise it.
  structure:
    - >-
      Way #1: Make Them A Customer — make them buy and preferably use the product to keep affiliate status.
    - >-
      Way #2: Make Them An Expert — they pay for the onboarding and training that certifies them as a product expert; charge 10-20% of what the average active affiliate makes in the first twelve months.
  anchor: >-
    invested and winning: make them a customer, and make them an expert.
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 3: Qualify Them, lines 12375–12446
  confirmations: 1
  anchor_at: "100m-leads.md:12390"
- id: A-leads-2-037
  type: framework
  name: >-
    What affiliates get paid for and how much
  statement: >-
    Affiliate payouts are decided by answering two things: what exactly you want the affiliate to do (that is what you pay for — new customers, repeat customers, or tracked steps before the sale), and how much, set from your maximum allowable CAC.
  why: >-
    Once you figure out exactly what you want the affiliate to do, how much and how often they get paid nearly solve themselves.
  applies_when: >-
    Step 4 of building an affiliate army.
  structure:
    - >-
      1. What They Get Paid For — new customers, and repeat customers; over time, steps before someone becomes a customer such as lead magnets downloaded or appointments set.
    - >-
      2. How Much They Get Paid — based on your maximum allowable cost to acquire a customer (CAC).
  anchor: >-
    When I figure out ways to pay affiliates I look at two basic
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 4, lines 12460–12512
  confirmations: 1
  anchor_at: "100m-leads.md:12470"
- id: A-leads-2-038
  type: framework
  name: >-
    The three-tier affiliate payout structure
  statement: >-
    Split the maximum allowable CAC into three payout tiers: 25% for anyone who agrees to your initial terms, 50% once they activate, and 100% once they sustain a level of performance.
  why: >-
    Not all affiliates are created equal, and the tiered method has a hidden and very profitable side effect — the average payout is much less than your maximum allowable CAC, and the leftover funds contests, recruiting more affiliates, or profit.
  applies_when: >-
    Setting affiliate compensation in Step 4; the author's worked example has a $40 maximum allowable CAC and a blended payout of $30, moving LTGP : CAC from 3:1 to 4:1.
  structure:
    - >-
      Tier 1: 25% CAC - Anyone who agrees to my initial terms qualifies. Example: They sign up and buy products or a certification.
    - >-
      Tier 2: 50% CAC - Once they activate. Example: actually finishing the certification they bought, doing a specific number of posts and outreach, doing a launch, etc.
    - >-
      Tier 3: 100% CAC - Once they sustain a level of performance. Example: They maintain five customers per month on subscription.
  anchor: >-
    I give it to. Not all affiliates are created equal. So, I suggest having
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 4, lines 12516–12572
  confirmations: 1
  anchor_at: "100m-leads.md:12518"
- id: A-leads-2-039
  type: framework
  name: >-
    The whisper-tease-shout method
  statement: >-
    A launch has three phases that mirror the three chunks of an ad: whisper (think call outs — curiosity, keep the product mysterious), tease (think elements of value — reveal the product, make the date public, use the What-Who-When framework), shout (think call to action — specific actions, bonuses, scarcity, urgency, guarantees).
  why: >-
    Curiosity comes from wanting to know what happens next, so whispers plant questions and teases satisfy them; the longer something appears to take, the more an audience will value it, which is why the whisper phase can start years out.
  applies_when: >-
    Activating affiliates through launches — but this is how you launch anything, not just affiliates; good launches have the work done ahead of time, so do all the work for the affiliates and let them plug and play.
  structure:
    - >-
      Whisper: Think "Call Outs." The key is curiosity. Keep the product itself mysterious and hint at how big of a deal it is.
    - >-
      Tease: Think "Elements Of Value." Reveal your product, make the date of the launch public, and start showing the elements of value.
    - >-
      Shout: Think "Call to Action." Give specific actions for the audience to take when the product launches; bonuses, scarcity, urgency, and guarantees around being "the first ones."
  anchor: >-
    should, you may as well do them right. I use the whisper-tease-shout
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 5: Get Them Advertising -- Launch, lines 12588–12738
  confirmations: 1
  authors_caveat: >-
    I can't remember where I first heard this, but the name stuck.
  anchor_at: "100m-leads.md:12614"
- id: A-leads-2-040
  type: framework
  name: >-
    The launch cadence for whisper, tease and shout
  statement: >-
    The launch has a fixed schedule: whisper every four to six weeks until sixty days out then every two to three weeks until thirty days out; tease once per week until fourteen days out then twice per week until three days out; shout at least twice a day from three days out, every few hours on the day, then every thirty minutes until launch.
  why: >-
    The cadence tightens as the launch nears so that curiosity built early is converted into exposure at the moment the product becomes available — you shout to get as many people exposed to your offer as you can.
  applies_when: >-
    Running a launch with or for affiliates.
  structure:
    - >-
      Start whispering every four to six weeks until you get sixty days out. Then whisper every two to three weeks until you get thirty days out.
    - >-
      Start teasing once per week until fourteen days out. Then tease twice per week until three days out.
    - >-
      Shout at least twice a day starting three days out. On the day of, start shouting every few hours until two hours out. Then shout every thirty minutes until you launch.
  anchor: >-
    [Action Step]{.calibre11}[: Start whispering every four to six weeks
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 5, lines 12671–12727
  confirmations: 1
  anchor_at: "100m-leads.md:12671"
- id: A-leads-2-041
  type: framework
  name: >-
    Three ways to integrate your product into an affiliate's offer
  statement: >-
    Integration comes in three forms, ordered from easiest to hardest: the affiliate gives away your lead magnet with every purchase of their stuff, sells your lead magnet separately to their audience, or directly sells your core offer.
  why: >-
    The strategy to start them advertising differs from the one to keep them advertising; integration is what turns a single affiliate sale into engaged leads for life.
  applies_when: >-
    Step 6 of building an affiliate army — keeping affiliates advertising long term.
  structure:
    - >-
      You can get them to give away your lead magnet with every purchase of their stuff.
    - >-
      You can get them to sell your lead magnet separately to their audience.
    - >-
      You can get them to directly sell your core offer.
  anchor: >-
    I've got three ways you can integrate your product into their offer. I
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 6: Keep Them Advertising, lines 12744–12917
  confirmations: 1
  authors_caveat: >-
    All three strategies work. They're just different. After testing, the author's companies continue to do Strategy 1 twice per year as a big event and Strategy 3 on an ongoing basis.
  anchor_at: "100m-leads.md:12756"
- id: A-leads-2-042
  type: framework
  name: >-
    Three forms of lead magnet an affiliate can hand out
  statement: >-
    The lead magnet an affiliate gives away or sells takes one of three forms: samples and trials, reveal a problem, or one step in a multi-step process.
  why: >-
    The lead magnet makes the affiliate's offer more valuable, which lets them charge more for it and get more leads than they could without it, while you get the leads to upsell — everybody wins.
  applies_when: >-
    Choosing what the affiliate hands to their customers in Step 6 integration.
  structure:
    - >-
      Samples And Trials: a free massage from me with every personal training package they sell.
    - >-
      Reveal a Problem: a free or discounted posture assessment with every training package; after assessing, you make them an offer to solve the problems you revealed.
    - >-
      One Step In A Multi-Step Process: the affiliate gives away step one of your multi-step process for free and you upsell the leads from there.
  anchor: >-
    Remember, the best lead magnets give away a free trial or sample of
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 6, lines 12778–12819
  confirmations: 1
  anchor_at: "100m-leads.md:12782"
- id: A-leads-2-043
  type: framework
  name: >-
    Three ways to improve an affiliate LTGP : CAC below 3
  statement: >-
    When the affiliate LTGP : CAC is under 3, there are three fixes: lower CAC by improving your ads, offer and sales process; get more affiliates to activate with a launch process; and make each affiliate worth more by improving your integration process.
  why: >-
    With affiliates you don't make money back from the affiliates themselves — the money spent to get an affiliate comes back from the customers they bring, so returns are the cost of an affiliate against the gross profit of all the customers they send.
  applies_when: >-
    Measuring affiliate returns; the author wants the ratio well above the 3:1 minimum (5:1, 10:1+), and if the numbers are already there, just do more.
  structure:
    - >-
      Lower CAC: We get affiliates for less (by improving our ads, offer, and sales process).
    - >-
      Increase LTGP & Decrease CAC: Get more to activate (by creating a launch process).
    - >-
      Increase LTGP: We make them worth more (by improving our integration process).
  anchor: >-
    your actual LTGP : CAC is less than 3, here are the three ways to
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Costs and Returns, lines 13066–13165
  confirmations: 1
  anchor_at: "100m-leads.md:13148"
- id: A-leads-2-044
  type: framework
  name: >-
    Two ways to create a compounding business
  statement: >-
    A business compounds in one of two ways: you find more people that never stop buying your stuff, or you find more people who never stop selling it for you — referrals are the former, affiliates are the latter.
  why: >-
    Affiliates aren't an advertising method you can do; they're people who advertise your stuff to benefit you both, and in theory once you build an affiliate army you never need to advertise again.
  applies_when: >-
    Choosing which lead getter to build for compounding growth.
  structure:
    - >-
      You can find more people that never stop buying your stuff — Referrals.
    - >-
      You can find more people who never stop selling it for you — Affiliates.
  anchor: >-
    a compounding business. You can find more people that never stop buying
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Conclusion, lines 13198–13202
  confirmations: 1
  anchor_at: "100m-leads.md:13199"
- id: A-leads-2-045
  type: framework
  name: >-
    The three habits that make Open To Goal work
  statement: >-
    Three habits carry the daily advertising block: wake up early (4-5 am), get right to work with no rituals or routines, and hold no meetings until noon.
  why: >-
    There's no magic in waking up early, but there is magic in a long stretch of uninterrupted work immediately after a long stretch of uninterrupted sleep — the most productive hours in a row of the most productive work you can do.
  applies_when: >-
    Making Open To Goal work for yourself; only after the dedicated block does the author go put out fires and deal with day-to-day stuff.
  structure:
    - >-
      Waking up early (4-5 am) -- Pro tip, this actually means going to bed early
    - >-
      Getting right to work -- No rituals. No routines. I drink coffee and get to work.
    - >-
      No meetings until noon -- No interruptions. Nothing. Fully focused work time.
  anchor: >-
    If I had to pick the three habits that best served me in my life - they
  source: >-
    100m-leads.md, Advertising in Real Life: Open To Goal, lines 13810–13866
  confirmations: 1
  authors_caveat: >-
    "That's more than twelve hours of work a day!" You're right. I'm playing to win. But if it overwhelms you at first, just throttle it back a few hours and then work your way up.
  anchor_at: "100m-leads.md:13818"
- id: A-leads-2-046
  type: framework
  name: >-
    One Page Advertising Checklist
  statement: >-
    The whole advertising plan fits on one page in five steps: pick the type of engaged lead to get, pick Rule of 100 or Open To Goal and commit to the daily actions, fill out the advertising checklist for that daily action, do it daily until you can afford to pay someone else, then go back to step 1 with employees as the new target lead type.
  why: >-
    Laying the action steps out on a single page leaves little room for excuses, distractions and delusions — you either did the stuff or you didn't — and it can be filled out in about five minutes.
  applies_when: >-
    Starting or resetting daily advertising work; the checklist is filled out for one daily action at a time.
  structure:
    - >-
      Step #1: Pick The Type Of Engaged Lead To Get: Customers, Affiliates, Employees, or Agencies
    - >-
      Step #2: Pick Rule of 100 or Open To Goal. Commit To Your Daily Advertising Actions
    - >-
      Step #3: Fill Out The Advertising Checklist For That Daily Action
    - >-
      Step #4: Do this daily action until you have enough money to afford paying someone else to do it.
    - >-
      Step #5: When you do, go back to step 1. Make employees your new target lead type. And repeat steps 1-4 until you have the help you need. Then, scale again.
  anchor: >-
    [Step #1:]{.calibre11}[ Pick The Type Of Engaged Lead To Get: Customers,
  source: >-
    100m-leads.md, Advertising in Real Life: Open To Goal, One Page Advertising Checklist, lines 13887–13921
  confirmations: 1
  authors_caveat: >-
    The content of steps #2 and #3 is given in the book only as images, so the checklist's own fields are not in the text.
  anchor_at: "100m-leads.md:13891"
- id: A-leads-2-047
  type: framework
  name: >-
    The Roadmap — seven levels of advertisers
  statement: >-
    Scaling advertising runs through levels, each with one primary action: warm outreach; consistent warm outreach plus content; hiring employees to advertise; a product good enough for consistent referrals; advertising in more places, more ways, with more people; hiring battle-hardened executives; and a seventh level the author has not reached.
  why: >-
    Acquisition.com uses this roadmap to scale portfolio companies from a few million a year to $100,000,000+, and the levels let you identify where you are on the advertising totem pole so you know what to do to get to the next one.
  applies_when: >-
    Diagnosing which advertising problem to work on next at your current size.
  structure:
    - >-
      Level 1: Your friends know about the stuff you sell. Primary Action: Warm outreach.
    - >-
      Level 2: You consistently let everyone you know about the stuff you sell. Primary Actions: Do as much warm outreach and post as much content as you can consistently.
    - >-
      Level 3: You get employees to help you do more advertising. Primary Action: You hire people to advertise profitably on your behalf.
    - >-
      Level 4: Your product is good enough to get consistent referrals. Primary Actions: Focus on your product until you get consistent referrals (25% or more of customers), then go back to scaling advertising with a bigger team.
    - >-
      Level 5: You advertise in more places in more ways with more people. Primary Action: Advertise profitably using at least two methods on multiple platforms.
    - >-
      Level 6: You hire killers. Primary Action: Get battle-hardened executives and department heads to take over new advertising activities and channels.
    - >-
      Level 7: I'll come back and edit this chapter once I cross a billion.
  anchor: >-
    this chapter, I describe the phases you will go through as you scale
  source: >-
    100m-leads.md, The Roadmap - Putting it All Together, lines 13996–14130
  confirmations: 2
  authors_caveat: >-
    Last Points: I know this looks clean. But it never is. Real business is messy. Level 7 is not written — the author had not crossed a billion at the time of writing (2023).
  anchor_at: "100m-leads.md:13997"
- id: A-leads-2-048
  type: framework
  name: >-
    The $100M+ Lead Machine
  statement: >-
    A $100,000,000+ advertising operation fires on all cylinders at once: a media team scaling free content in all media types on many platforms, regular offers to a warm audience, launches that are immediately profitable, teams running paid ads on multiple platforms, a cold outreach team, an affiliate manager launching and integrating affiliates, recruiters and recruiting agencies bringing in lead getters, a product so good a third of customers bring more customers, and an executive team driving it without you.
  why: >-
    It's great to have a clear picture of what the $100M machine looks like, so you know what you are building toward — the end state is more engaged leads than you can possibly handle.
  applies_when: >-
    Setting the long-horizon target for a lead machine; for business owners who know what to do this takes anywhere from five to ten years.
  structure:
    - >-
      Your media team scales tons of free content, in all media types, on many platforms.
    - >-
      You regularly make offers to your warm audience to get more customers or affiliates.
    - >-
      Your ravenous audience makes anything you launch immediately profitable.
    - >-
      You have teams running and scaling profitable paid ads across multiple platforms.
    - >-
      Your cold outreach team gets you more customers.
    - >-
      You have an affiliate manager launching and integrating all new affiliates.
    - >-
      You have recruiters and recruiting agencies bringing in more lead getters.
    - >-
      Your product is so good that a third of your customers bring you more customers.
    - >-
      Your executive team drives all this growth without you.
    - >-
      And...you have more engaged leads than you can possibly handle.
  anchor: >-
    revenue. It's great to have a clear picture of what the \$100M machine
  source: >-
    100m-leads.md, The Roadmap, The $100M+ Lead Machine, lines 14161–14206
  confirmations: 1
  anchor_at: "100m-leads.md:14162"
- id: A-leads-2-049
  type: framework
  name: >-
    The Core Four, one line each
  statement: >-
    The core four — the only four ways we can let people know about the stuff we sell — compress to one line apiece: warm outreach is asking people who know you if they know anybody; posting publicly is hook, retain, reward and give until they ask; cold outreach is lists, personalization, big fast value, volume; paid ads are targeting, callouts, What-Who-Whens, CTAs, client financed acquisition.
  why: >-
    The author's own back-of-the-napkin recap of everything covered, organized into one place so it sinks in.
  applies_when: >-
    Recalling which method to run and what each one's essentials are.
  structure:
    - >-
      How to reach out to people who know us: ask them if they know anybody
    - >-
      How to post publicly: hook, retain, reward. Give until they ask.
    - >-
      How to reach out to strangers: lists, personalization, big fast value, volume
    - >-
      How to run paid ads to strangers: targeting, callouts, What-Who-Whens, CTAs, client financed acquisition
  anchor: >-
    Four]{.calibre24}[ - the only four ways we can let people know about the
  source: >-
    100m-leads.md, A Decade in a Page, lines 14249–14269
  confirmations: 1
  authors_caveat: >-
    This is the author's one-line compression; the Core Four itself is set out in full in Section III (lines 2786–2929), outside this group.
  anchor_at: "100m-leads.md:14250"
```
