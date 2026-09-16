# Улов фазы 1 — $100M Leads (2023), from #4 Run Paid Ads to the end (lines 6901–14623) (ярус 1), тип D: антипаттерны и границы

Группа `tier1-leads-2`, слаг `leads-2`, ярус 1. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **70** (экстрактор вернул 70, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-leads.md` | 6901–14623 | 7 | 70 |

## Как собран файл

Экстрактор D (Antipatterns and boundaries) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier1-leads-2.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier1-leads-2-D.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: D-leads-2-001
  type: antipattern
  name: >-
    Blaming the ad when the right people never saw it
  statement: >-
    Treating an unprofitable ad as a copy or creative failure, when most of the time the cause is that the right people never saw it.
  why: >-
    Paid ads go to colder, lower-trust audiences, so a smaller percentage of people respond; the way over that hurdle is putting the offer in front of more of the right people, which is what keeps ads efficient.
  anchor: >-
    in front of more people. And if an ad isn't profitable, most of the
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, lines 7071–7078
  confirmations: 1
  anchor_at: "100m-leads.md:7074"
- id: D-leads-2-002
  type: rule
  name: >-
    Ads get less efficient as the audience grows
  statement: >-
    When you expand from a small audience to a bigger one, expect the ratio between what you spend and what they buy to get worse while the total money you make goes up.
  why: >-
    A bigger audience holds more of the wrong people, but also more of the right ones; the ratio goes down, the total profit goes up, and the risk rises because you spend more.
  boundary: >-
    The drop in efficiency is only acceptable at the point where you can afford the higher spend; the aim is the largest audience that still turns a profit, not the best ratio.
  applies_when: >-
    Scaling a paid-ad audience from a puddle to a pond, a lake and an ocean; the author pads a scaled budget by twenty percent for the same reason.
  anchor: >-
    right ones too. So ads decrease in efficiency, but at that point you can
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, lines 7096–7106
  confirmations: 2
  anchor_at: "100m-leads.md:7099"
- id: D-leads-2-003
  type: antipattern
  name: >-
    The right message to the wrong audience
  statement: >-
    Running a good ad at an audience that cannot buy - wrong place, wrong language, wrong filter.
  why: >-
    The right message to the wrong audience falls on deaf ears no matter how good the ads are: marketing to Florida residents about a local business in Iowa is probably not gonna work.
  applies_when: >-
    Targeting, where the single goal is to get the highest number of people you think will buy your stuff to see your ad.
  anchor: >-
    The right message to the wrong audience will fall on deaf ears. It
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, lines 7203–7207
  confirmations: 1
  anchor_at: "100m-leads.md:7203"
- id: D-leads-2-004
  type: antipattern
  name: >-
    The Frankenstein experience
  statement: >-
    Sending ad traffic to a landing page whose look, language and promise do not match the ad that produced the click.
  why: >-
    People click because you promised them a benefit; when the page does not deliver the same promise, a lot of people forget this and waste money until they remember it. The goal is a continuous experience from click to close.
  anchor: >-
    with some Frankenstein experience where everything looks different. You
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, lines 7930–7936
  confirmations: 1
  anchor_at: "100m-leads.md:7935"
- id: D-leads-2-005
  type: rule
  name: >-
    The ad is not selling
  statement: >-
    The ad and its landing page do not sell the product; they ask whether the person is interested, and what they exchange for is contact information.
  why: >-
    A person who is interested gives you a way to tell them more, and at that moment becomes an engaged lead.
  not_to_confuse_with: >-
    Selling the offer inside the ad or on the landing page.
  anchor: >-
    [To be clear, we aren't selling anything. We are asking if they're
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, lines 7951–7954
  confirmations: 1
  anchor_at: "100m-leads.md:7951"
- id: D-leads-2-006
  type: antipattern
  name: >-
    Tweaking the creative instead of the return
  statement: >-
    Getting hyper-focused on making copy, creative and media perfect instead of on the return the ad spend produces.
  why: >-
    All advertising works; the only thing that differs is how well. Paid ads are about the money you put in against the money you get out, so a machine only has to get good enough to scale - good enough is good enough.
  anchor: >-
    that stuff "perfect" (as if you can). You can tweak all day and night...
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8026–8039
  confirmations: 2
  anchor_at: "100m-leads.md:8032"
- id: D-leads-2-007
  type: antipattern
  name: >-
    Spending before tracking
  statement: >-
    Putting a dollar into ads before the tracking of returns is set up.
  why: >-
    Without tracking you get cleaned out - it is like playing a casino game for as long as you feel like rather than as long as you can afford; with tracking you do more of what makes money and less of what does not.
  applies_when: >-
    Phase One of scaling paid ads (Track Money), before the Lose Money and Print Money phases.
  anchor: >-
    so you can accurately track your returns. If you don't track, you're
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8094–8103
  confirmations: 1
  anchor_at: "100m-leads.md:8096"
- id: D-leads-2-008
  type: antipattern
  name: >-
    Stopping at the loss instead of scaling the winner
  statement: >-
    Reading the total loss across a batch of tested ads as a failure and stopping, instead of finding the one winner in the batch and putting far more money behind it.
  why: >-
    In a batch of ten ads, nine can lose while one returns five to one; the aggregate still shows a loss, but the winner is there to be scaled by doubling, tripling, quadrupling, 10x-ing down on it. You might lose nine or ninety-nine times in a row before you win big.
  anchor: >-
    still down \$500. Many people stop here because they see a \$500 dollar
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8126–8140
  confirmations: 2
  anchor_at: "100m-leads.md:8128"
- id: D-leads-2-009
  type: antipattern
  name: >-
    Letting an ad run too long, or giving up on it too early
  statement: >-
    Both leaving a bad ad running until the money is gone and killing an ad before it had a chance are the author's own expensive mistakes.
  why: >-
    He wasted tons of money letting ads run too long before realising they sucked, and lost even more by giving up on ads before he gave them a chance.
  applies_when: >-
    Testing a new ad: budget two times the cash collected from a new customer in the first thirty days (not LTGP) before shutting it off, as long as leads are coming; if an ad brings no leads at all, shut it off before 1x thirty-day cash.
  anchor: >-
    ads.]{.calibre11}[ I wasted tons of money letting ads run too long
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8146–8157
  confirmations: 1
  anchor_at: "100m-leads.md:8148"
- id: D-leads-2-010
  type: rule
  name: >-
    Measure the returns over a long time horizon
  statement: >-
    Judging paid ads by next week's numbers instead of over a long time horizon.
  why: >-
    It costs money to build an advertising machine and that is normal - one business took a year to get paid ads profitable and made the whole year of wasted money back the next month.
  boundary: >-
    The author's own case: a full year of unprofitable spend can still be the right investment when other businesses in the space run profitable ads, which proves it is possible.
  anchor: >-
    returns over a long time horizon, not next week. Can you think of
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8161–8172
  confirmations: 1
  anchor_at: "100m-leads.md:8169"
- id: D-leads-2-011
  type: antipattern
  name: >-
    Not committing to the budget you reversed from your goal
  statement: >-
    Backing away from the daily ad budget that follows from your customer goal because the number is frightening.
  why: >-
    Once ads break even or better, the budget is reversed from the number of customers you can handle (padded by twenty percent for scaling losses) and then committed to. If the number terrifies you, you are doing it right - trusting the data is how you scale, and that is why most people never do.
  applies_when: >-
    Phase Three (Print Money), when ads already make back more than they cost.
  anchor: >-
    right. Trust the data. This is how you scale. And that's why most people
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8187–8198
  confirmations: 1
  anchor_at: "100m-leads.md:8197"
- id: D-leads-2-012
  type: rule
  name: >-
    3 to 1 LTGP to CAC is an observed pattern
  statement: >-
    The 3:1 lifetime-gross-profit-to-CAC threshold is what the author observed across the businesses he invests in, not a law.
  why: >-
    Every business he invests in that struggles to scale has an LTGP to CAC ratio below 3 to 1, and they take off as soon as it goes above 3 to 1, by lowering CAC or raising LTGP.
  boundary: >-
    The author marks the ratio himself as a pattern he personally observed, not a rule.
  anchor: >-
    LTGP), they take off. ]{.calibre3}[This is a pattern I personally
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8248–8253
  confirmations: 1
  anchor_at: "100m-leads.md:8252"
- id: D-leads-2-013
  type: antipattern
  name: >-
    Crappy ads or a crappy business model
  statement: >-
    Concluding you have bad ads (high CAC) when what you actually have is a bad business model (low LTGP).
  why: >-
    The cost to acquire customers between competitors in the same industry is much closer than you would think; the difference between the winners and the losers is how much they make off each customer.
  applies_when: >-
    Use the industry average CAC as the guide: if your CAC is below 3x the industry average, work on the business model (LTGP); if it is above 3x, work on the advertising (CAC).
  anchor: >-
    month. They often think they have crappy ads (high CAC) when, in
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8288–8305
  confirmations: 2
  anchor_at: "100m-leads.md:8289"
- id: D-leads-2-014
  type: rule
  name: >-
    Costs can only approach zero
  statement: >-
    Pushing advertising efficiency past the point where cutting the cost of a customer by $100 takes more work than making an extra $100 from them.
  why: >-
    Costs can only approach zero while how much you make can go up to infinity, so efficiency beyond that point is like trying to save your way to a billion dollars - you feel like you are making progress and you are never going to get there.
  boundary: >-
    Once the cost of getting a customer is low enough, the work moves to the business model; there is a floor under CAC and no ceiling over LTGP.
  anchor: >-
    infinity. Increasing advertising efficiency beyond a certain point is
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8309–8316
  confirmations: 1
  anchor_at: "100m-leads.md:8314"
- id: D-leads-2-015
  type: antipattern
  name: >-
    Don't Confuse Sales Problems With Advertising Problems
  statement: >-
    Declaring that advertising does not work when the right leads are getting on the phone and the sales are what fail.
  why: >-
    A company spent twelve weeks and $150,000, got the right leads on the phone, blamed the ads and quit six inches from gold; confusing an advertising problem with a sales problem cost them an estimated ~$30M in enterprise value.
  applies_when: >-
    If your engaged leads have the problem you solve and the money to spend and they are not buying, then the ads work fine and you have a sales problem.
  anchor: >-
    Confusing an advertising problem with a sales problem cost them an
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8463–8475
  confirmations: 2
  anchor_at: "100m-leads.md:8471"
- id: D-leads-2-016
  type: antipattern
  name: >-
    If You Say You Suck At Something, You Will Probably Suck At It
  statement: >-
    Declaring yourself bad at part of the job - "I'm not techy", "I hate tech stuff" - and outsourcing it on that ground.
  why: >-
    It just keeps you poorer than you should be: the author said it for four years, then reversed four years of wasted time and lost money with four hours of concentrated effort. He also spent four years too scared to build a landing page and finished the first one before lunch.
  anchor: >-
    It.]{.calibre11}[ Never say "I'm not techy" or "I hate tech stuff."
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8463–8497
  confirmations: 2
  anchor_at: "100m-leads.md:8491"
- id: D-leads-2-017
  type: antipattern
  name: >-
    Chickening out before the money is spent
  statement: >-
    Setting up a first ad and stopping short of actually spending the money.
  why: >-
    The hundred dollars buys the lesson that running ads is easier than you think; until you spend it you are an observer rather than in the game.
  anchor: >-
    Don't go all the way to the end then chicken out. Spend the gosh darn
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8515–8518
  confirmations: 1
  anchor_at: "100m-leads.md:8516"
- id: D-leads-2-018
  type: rule
  name: >-
    Do paid ads last
  statement: >-
    Paid ads are recommended as the last of the core four to take up, not the first.
  why: >-
    The skills from the other three methods transfer into paid ads, which shortens the learning curve, and paid ads cost money - money you will have if you start with the other three.
  boundary: >-
    Paid ads presuppose money to lose and skills earned elsewhere; a business without either is not the place for them yet.
  anchor: >-
    one. And second, paid ads cost money. Money you will have if you start
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8555–8560
  confirmations: 1
  anchor_at: "100m-leads.md:8557"
- id: D-leads-2-019
  type: rule
  name: >-
    Cold advertising means lower response rates
  statement: >-
    Any cold advertising should be planned around lower response rates, which is why the volume is carried by automation.
  why: >-
    The author states it as a property of all cold advertising when applying the rule of 100 to cold reach outs.
  boundary: >-
    Holds for cold advertising specifically, as against warm reach outs and content to an audience that already knows you.
  anchor: >-
    [As with all cold advertising, expect lower response rates, so use
  source: >-
    100m-leads.md, Core Four On Steroids: More Better New, lines 8865–8866
  confirmations: 1
  anchor_at: "100m-leads.md:8865"
- id: D-leads-2-020
  type: antipattern
  name: >-
    Testing several things at once on one platform
  statement: >-
    Changing more than one thing at a time on a platform, so that the result of the test cannot be read.
  why: >-
    You never really learn what worked; steps also affect each other - a change at step one can raise optins and lower applications, and with several changes at once, good luck figuring out what worked or didn't.
  applies_when: >-
    The author's schedule: one split test per platform every Monday, the result written into a log of all tests so the next test starts a zillion improvements later rather than at square one.
  anchor: >-
    one platform you never really learn what worked.
  source: >-
    100m-leads.md, Core Four On Steroids: More Better New, lines 8980–8991
  confirmations: 2
  anchor_at: "100m-leads.md:8981"
- id: D-leads-2-021
  type: antipattern
  name: >-
    Spending a test on a trivial change
  statement: >-
    Burning the one big test of the week on something like a colour change from red to bright red.
  why: >-
    You can run an infinite number of tests but time is limited, so the one test per week per platform has to be spent on what will get the most engaged leads.
  anchor: >-
    you only do one "big" test per week per platform, don't waste it on a
  source: >-
    100m-leads.md, Core Four On Steroids: More Better New, lines 8994–8999
  confirmations: 1
  anchor_at: "100m-leads.md:8997"
- id: D-leads-2-022
  type: rule
  name: >-
    One week per test is calibrated to the team and the spend
  statement: >-
    A test has to run long enough to show a real improvement - too short and there is not enough data, too long and you waste time you could spend on the next constraint.
  why: >-
    The author names one week as typically long enough for him, and ties that length to the size of his team and the amount of money he spends on advertising.
  boundary: >-
    The one-week window is the author's own calibration for his team size and ad spend, not a universal test length.
  anchor: >-
    and the amount of money I spend on advertising, one week is typically
  source: >-
    100m-leads.md, Core Four On Steroids: More Better New, lines 9001–9007
  confirmations: 1
  anchor_at: "100m-leads.md:9005"
- id: D-leads-2-023
  type: rule
  name: >-
    Four tries, then move to the next constraint
  statement: >-
    If a new test cannot beat the version currently running within four tries, or one month, the work moves to the next constraint.
  why: >-
    Effort spent on making one thing better eventually brings lower and lower returns, and at that point it makes more sense to put the effort where the returns are higher.
  boundary: >-
    A stopping rule for optimisation: the constraint is abandoned on a count of tries and a calendar limit, not on a feeling that it is exhausted.
  anchor: >-
    current 'best' version. If we can't beat the version we're currently
  source: >-
    100m-leads.md, Core Four On Steroids: More Better New, lines 9025–9029
  confirmations: 2
  anchor_at: "100m-leads.md:9026"
- id: D-leads-2-024
  type: antipattern
  name: >-
    The Size Of The Pie Fallacy
  statement: >-
    Mistaking the tiny slice of the universe you advertise to - one core four activity, on one platform, in one way, to one targeted audience - for the entire available market.
  why: >-
    This is why most businesses stay small: when they plateau they believe there are no more leads to get, because saying "I'm as big as I can get" is much easier than saying "I'm not as good at advertising as I thought", and this false argument keeps entrepreneurs poorer than they should be.
  applies_when: >-
    The diagnostic in the chapter's opening: a $2M chiropractic business spending $30k a month on one platform, doing no content and no cold outreach, declaring a $15.1B industry saturated.
  anchor: >-
    universe they advertise to is the entire available market! This is why
  source: >-
    100m-leads.md, Core Four On Steroids: More Better New, lines 9093–9100
  confirmations: 3
  anchor_at: "100m-leads.md:9094"
- id: D-leads-2-025
  type: rule
  name: >-
    When to do new
  statement: >-
    You move to new placements, new platforms or a new core four activity only when the returns from doing more and better are lower than what a new placement or way of advertising would return.
  why: >-
    New is much harder in practice, which is why the author exhausts more and better first; the effort put into making something better brings lower and lower returns at a certain point.
  boundary: >-
    The trigger is comparative returns, not boredom with the current channel; the rough order is new placement, then new platform, then new core four activity.
  anchor: >-
    from doing more↔better are lower than what you could get from a new
  source: >-
    100m-leads.md, Core Four On Steroids: More Better New, lines 9104–9106
  confirmations: 3
  anchor_at: "100m-leads.md:9105"
- id: D-leads-2-026
  type: rule
  name: >-
    Lead getters are not part of the core four
  statement: >-
    Customer referrals, employees, agencies and affiliates are not core four activities, because they are not things you do; you do the core four to get them, and then they do it for you.
  why: >-
    The core four stacks: once to get the lead getter, and a second time when the lead getter gets engaged leads on your behalf, and lead getters can go get lead getters.
  not_to_confuse_with: >-
    The core four activities themselves (warm outreach, post content, cold outreach, paid ads) - you do not do affiliates or do customer referrals.
  anchor: >-
    [The lead getters aren't part of the "core four" because they're not
  source: >-
    100m-leads.md, Section IV: Get Lead Getters, lines 9432–9437
  confirmations: 1
  anchor_at: "100m-leads.md:9432"
- id: D-leads-2-027
  type: antipattern
  name: >-
    Losing customers faster than referrals come in
  statement: >-
    Trying to scale on word of mouth while churn runs ahead of referrals.
  why: >-
    Referrals minus churned customers is the referral growth equation: above churn you grow with no other advertising, equal to churn you need other advertising, below churn you advertise just to break even, which is where most businesses sit - a hamster wheel of death.
  anchor: >-
    few people scale by word of mouth? They lose customers faster than they
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, lines 9813–9816
  confirmations: 1
  anchor_at: "100m-leads.md:9814"
- id: D-leads-2-028
  type: antipattern
  name: >-
    Two Reasons Most Businesses Don't Get Referrals
  statement: >-
    Businesses get few referrals for two reasons: the product is not as good as they think it is, and they never ask for referrals.
  why: >-
    Both causes are inside the business: goodwill is what produces word of mouth, and customers, like any audience, can only know what to do if you tell them.
  anchor: >-
    [Most businesses don't get referrals for two reasons. First, their
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, lines 9860–9862
  confirmations: 2
  anchor_at: "100m-leads.md:9860"
- id: D-leads-2-029
  type: antipattern
  name: >-
    Everyone loves our stuff, we just need to get the word out
  statement: >-
    Explaining a lack of referrals by lack of exposure rather than by the product.
  why: >-
    If the product were exceptional people would already know about it and you would have more business than you could handle; a product nobody talks about may be okay, but it is unremarkable - not worthy of remark.
  applies_when: >-
    Direct-to-consumer businesses whose customers are not bringing them more customers; the author's own question is "Why are my customers too embarrassed to tell everyone they know about my product?"
  anchor: >-
    out!"]{.calibre24}[ - says every small business owner with a product
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, lines 9874–9884
  confirmations: 2
  anchor_at: "100m-leads.md:9875"
- id: D-leads-2-030
  type: antipattern
  name: >-
    Lowering the price to build goodwill
  statement: >-
    Creating the gap between price and value by cutting the price rather than by giving more value.
  why: >-
    Lower the price far enough and people line up, but you would probably lose money; it is a temporary solution at best, and you can only lower the price so much for so long. As Rory Sutherland says, "Any fool can sell something for less."
  applies_when: >-
    Building the goodwill that produces word of mouth: the question is not how to lower the price but how to give more value.
  anchor: >-
    probably lose money. So, lowering the price is, at best, a temporary
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, lines 9927–9933
  confirmations: 1
  anchor_at: "100m-leads.md:9930"
- id: D-leads-2-031
  type: antipattern
  name: >-
    Promising everything and the kitchen sink
  statement: >-
    Raising the promises in the offer to close more deals, which leaves no room to overdeliver.
  why: >-
    The author promised everything to get people to buy and fulfilling on it turned into a nightmare; expectations shape the experience itself, and goodwill comes from setting them low enough to exceed.
  applies_when: >-
    Slowly lower the promises you make when making offers, and keep lowering them until your close rates lower - at that point, stop.
  anchor: >-
    [In the beginning, I promised everything and the kitchen sink to get
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, lines 10048–10061
  confirmations: 2
  anchor_at: "100m-leads.md:10048"
- id: D-leads-2-032
  type: antipattern
  name: >-
    Leaving a customer in no man's land
  statement: >-
    Ending a contact without the customer knowing the next time they will hear from you.
  why: >-
    They should always know what happens next; the author's answer is BAMFAM - Book-A-Meeting-From-A-Meeting.
  anchor: >-
    Book-A-Meeting-From-A-Meeting. Again, never leave a customer in no
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, lines 10168–10190
  confirmations: 1
  anchor_at: "100m-leads.md:10183"
- id: D-leads-2-033
  type: antipattern
  name: >-
    Expecting customers to forgive you
  statement: >-
    Delivering late on the assumption that the customer will forgive it.
  why: >-
    Never expect customers to forgive you, ever, so act like it: you can deliver early but never late. The author adds fifty percent to his timelines so that on time for him is early for them.
  anchor: >-
    5.  [Never expect customers to forgive you. Ever. So act like it. For
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, lines 10168–10190
  confirmations: 1
  anchor_at: "100m-leads.md:10187"
- id: D-leads-2-034
  type: antipattern
  name: >-
    Obsessing over the front end and neglecting the back end
  statement: >-
    Polishing the front end offer while leaving the customer nothing else to buy afterwards.
  why: >-
    Customers fall off the product when there is nothing more to buy, and customers who fall off are unlikely to refer; if you do not satisfy their desire to buy, they will still buy - from someone else.
  anchor: >-
    [In my experience, people obsess over their front end offers. And that
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, lines 10259–10282
  confirmations: 2
  anchor_at: "100m-leads.md:10278"
- id: D-leads-2-035
  type: rule
  name: >-
    Asking for referrals only works when you treat it like an offer
  statement: >-
    A referral ask works only when it is built as an offer that shows the customer the value they get for referring.
  why: >-
    The author tried a lot of referral strategies and most failed until this; Dropbox and PayPal both paid value to the referrer and to the friend.
  boundary: >-
    Referral tactics that are not built as an offer are the ones that failed for the author; the referral programme has three components - how you give the incentive, what you incentivise with, and how you ask.
  anchor: >-
    Asking for referrals only works when you treat it like an
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, lines 10354–10360
  confirmations: 1
  anchor_at: "100m-leads.md:10356"
- id: D-leads-2-036
  type: rule
  name: >-
    Referrals aren't an advertising method you can do
  statement: >-
    Referrals are not an advertising activity to be performed, they are a way of doing business that starts with the owner.
  why: >-
    It is not one trick or hack; goodwill is built by the six ways of giving more value, and only then capitalised on by the seven ways of asking.
  not_to_confuse_with: >-
    The core four activities; the same holds for affiliates, who are also not an advertising method you can do.
  anchor: >-
    [Referrals aren't an advertising method you can "do."]{.calibre3}[
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, lines 10594–10598
  confirmations: 2
  anchor_at: "100m-leads.md:10594"
- id: D-leads-2-037
  type: rule
  name: >-
    Customers only refer when the risk to the friendship is outweighed
  statement: >-
    A customer refers only when they think it very likely their friend will have a good experience - when the benefit to them personally outweighs the risk of hurting the relationship.
  why: >-
    Referring is always a risk for the customer: they stake their own goodwill with their friend in the hope of getting more of it by showing them something good.
  boundary: >-
    Incentives raise the benefit side, but the risk side is lowered only by goodwill - by showing you deliver on your promises.
  anchor: >-
    ]{.calibre3}[only]{.calibre24}[ refer when they think it's very likely
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, lines 10602–10616
  confirmations: 1
  anchor_at: "100m-leads.md:10606"
- id: D-leads-2-038
  type: rule
  name: >-
    Employees take work
  statement: >-
    Hiring lead-getting employees does not remove work; it trades a larger amount of doing for a smaller amount of managing.
  why: >-
    Trading forty hours of doing for four hours of managing leaves you thirty-six hours ahead, and the trade can be made again - 200 hours of work for twenty hours of management, then those twenty for a manager who costs four.
  boundary: >-
    The author states the caveat himself: employees take work, they just take less time and work than doing everything on your own.
  anchor: >-
    They just take less time and work than doing everything on your
  source: >-
    100m-leads.md, #2 Employees, lines 10819–10827
  confirmations: 1
  anchor_at: "100m-leads.md:10820"
- id: D-leads-2-039
  type: antipattern
  name: >-
    A business that only makes money with you in it
  statement: >-
    Running a profitable business that requires you around the clock, which leaves you with a high paying job rather than an asset.
  why: >-
    If the business only makes money with you in it, it is a bad investment for anyone else, so it is worth almost nothing; the same $2,000,000 of profit in a business that runs without you could easily be worth $10,000,000+ right now. You turned a liability that relied on you into an asset you can rely on.
  applies_when: >-
    The author's reminder: you get rich from what you make, you become wealthy from what you own.
  anchor: >-
    worth much. ]{.calibre24}[If the business only makes money with you in
  source: >-
    100m-leads.md, #2 Employees, lines 10850–10899
  confirmations: 2
  anchor_at: "100m-leads.md:10861"
- id: D-leads-2-040
  type: antipattern
  name: >-
    If you want it done right you gotta do it yourself
  statement: >-
    Holding the beliefs "nobody can do it but me" and "if you want it done right you gotta do it yourself" about your own business.
  why: >-
    They are not facts, they are false: somebody did similar stuff before you and will after you, and everyone is replaceable - by multiple people, by technology, or later in time. The author lived this belief for years and it never made him more money.
  applies_when: >-
    The replacements he adopted instead: "If you want it done right, get someone to spend all their time doing it", "If I can do it, someone else can do it better", "Everyone is replaceable, especially me."
  anchor: >-
    done right you gotta do it yourself" aren't facts... they're false.
  source: >-
    100m-leads.md, #2 Employees, lines 10939–10947
  confirmations: 1
  anchor_at: "100m-leads.md:10940"
- id: D-leads-2-041
  type: antipattern
  name: >-
    Outcompeting your own employees
  statement: >-
    Comparing what a new hire can do against what you can do, and treating the team as a contest you have to win.
  why: >-
    The more the author tried to outcompete his employees, the more distracted he became and the worse his business got; he could do anything better than any one of them but could not do everything better than all of them, and it was his fault they sucked - he hired and trained them.
  anchor: >-
    [The more I tried to outcompete my employees, the more distracted I
  source: >-
    100m-leads.md, #2 Employees, lines 10951–10975
  confirmations: 2
  anchor_at: "100m-leads.md:10968"
- id: D-leads-2-042
  type: antipattern
  name: >-
    Blaming the trainee for a bad checklist
  statement: >-
    Treating a trainee's confusion or wrong result as the trainee's failure rather than as a defect in the checklist.
  why: >-
    If they get it wrong or get confused then we got it wrong or made it confusing; having to explain what a step means means the step is too complicated, or several steps were packed into one. Train them to follow directions, and when they follow directions and get the wrong result, you know it is the directions - and that you control.
  anchor: >-
    they get it wrong or get confused then we got it wrong or made it
  source: >-
    100m-leads.md, #2 Employees, lines 11145–11199
  confirmations: 2
  anchor_at: "100m-leads.md:11146"
- id: D-leads-2-043
  type: antipattern
  name: >-
    Forcing an inferior checklist to work
  statement: >-
    Keeping a checklist that only lands after a long explanation or several demonstrations, and pushing it through anyway.
  why: >-
    Business owners who ignore this run into chronic training problems; you can probably force an inferior checklist to work, but it turns into a nightmare when somebody else takes over your training for you.
  anchor: >-
    Business owners that ignore this run into chronic training problems.
  source: >-
    100m-leads.md, #2 Employees, lines 11145–11199
  confirmations: 1
  anchor_at: "100m-leads.md:11153"
- id: D-leads-2-044
  type: rule
  name: >-
    Competence is not performance
  statement: >-
    When a trainee knows exactly what to do but is not good at it yet, the instructions are fine and what they need is practice.
  why: >-
    Slow then smooth then fast - nothing has to change in the checklist, they just need more reps.
  boundary: >-
    This is the case where the checklist rule does not apply: a weak result is only evidence of a bad checklist when the trainee does not know what to do.
  anchor: >-
    There is a difference between competence and performance. In other
  source: >-
    100m-leads.md, #2 Employees, lines 11145–11199
  confirmations: 1
  anchor_at: "100m-leads.md:11158"
- id: D-leads-2-045
  type: antipattern
  name: >-
    Punishing mistakes during training
  statement: >-
    Penalising a trainee for doing something wrong while they are learning, or taking the task over from them when they mess up.
  why: >-
    Learning a new skill is punishing enough; reward the good stuff you want more of and they will do more of it. When they goof, pause, step back and let them try again - fast feedback cycles make people learn faster.
  applies_when: >-
    Even when they follow the directions exactly and get the wrong result, praise them for following the directions, then correct the checklist on the spot.
  anchor: >-
    Avoid punishment or penalties of any type for doing stuff wrong
  source: >-
    100m-leads.md, #2 Employees, lines 11145–11199
  confirmations: 2
  anchor_at: "100m-leads.md:11186"
- id: D-leads-2-046
  type: antipattern
  name: >-
    Fixing several things at once in training
  statement: >-
    Giving a trainee feedback on more than one step, or more than one piece of feedback at a time.
  why: >-
    It is hard to fix multiple things when you have never done something before; give one piece of feedback, practise until they get it right, then move to the next step.
  anchor: >-
    time. Give one piece of feedback at a time. Practice until they get
  source: >-
    100m-leads.md, #2 Employees, lines 11145–11199
  confirmations: 1
  anchor_at: "100m-leads.md:11193"
- id: D-leads-2-047
  type: antipattern
  name: >-
    Firing the wrong person
  statement: >-
    Firing the sales people over an advertising problem, or the advertising people over a sales problem.
  why: >-
    The single diagnostic question - do my engaged leads have the problem I solve and the money to spend? - separates the two: unqualified leads are an advertising problem; qualified leads that buy but are too few are an advertising problem; qualified leads that do not buy are a sales problem.
  applies_when: >-
    When CAC is more than 3x the industry average; within 3x, the work moves to raising LTGP instead.
  anchor: >-
    [Don't fire your sales guy if you've got advertising problems. And
  source: >-
    100m-leads.md, #2 Employees, lines 11266–11291
  confirmations: 1
  anchor_at: "100m-leads.md:11288"
- id: D-leads-2-048
  type: rule
  name: >-
    Who you pick matters less than how you train
  statement: >-
    For ground-level advertising jobs, who you hire is not as important as how you train the ones you do hire.
  why: >-
    The author believes anyone can be taught to do ground level jobs for any business, advertising or otherwise, and you cannot know anything about a person until you have trained them well and given them a fighting chance in the field.
  boundary: >-
    Scoped to low level jobs, where there is never a shortage of labour; getting picky belongs to massive investments in hyper-specific multiple-six-figure C-suite employees.
  anchor: >-
    pick is not as important as how you train the ones you do.
  source: >-
    100m-leads.md, #2 Employees, lines 11317–11345
  confirmations: 2
  anchor_at: "100m-leads.md:11319"
- id: D-leads-2-049
  type: antipattern
  name: >-
    The agency cycle of insanity
  statement: >-
    Buying an agency's standard arrangement: excitement, onboarding, the best senior rep, some results, the senior rep moved to the newest customer, a junior rep, worse results, complaints, cancellation, and the search for the next agency.
  why: >-
    You only ever get a fraction of the agency's attention, so results get worse whenever they take on new clients, while your own team would get better because they stay focused on you full-time. Agencies can play a valuable role in growth, but not the way they want you to.
  anchor: >-
    [Step 10: I'd search for another agency and repeat the cycle of
  source: >-
    100m-leads.md, #3 Agencies, lines 11560–11598
  confirmations: 2
  anchor_at: "100m-leads.md:11593"
- id: D-leads-2-050
  type: antipattern
  name: >-
    Believing you never have to learn this stuff
  statement: >-
    Hiring an agency on the belief that you will never have to learn what they do because they can do it for you.
  why: >-
    The author calls it a lie; instead he opens every agency relationship with a purpose and a deadline - work together roughly six months, pay extra for them to break down why they make the decisions they make, train the team on it, then move to a lower cost consulting arrangement.
  applies_when: >-
    Run both teams until yours beats theirs regularly, then cancel and put the money into scaling what you learned.
  anchor: >-
    that "I'll never have to learn this stuff because they can do it," I
  source: >-
    100m-leads.md, #3 Agencies, lines 11680–11695
  confirmations: 1
  anchor_at: "100m-leads.md:11682"
- id: D-leads-2-051
  type: rule
  name: >-
    No money, no agencies
  statement: >-
    With no money, agencies are out of the question and the skills have to be learned by trial and error.
  why: >-
    Good agencies cost money; with money, the author uses them for two things - learning new methods and learning new platforms, so he skips the trial and error and goes straight to the make-money part.
  boundary: >-
    The author's own limit on when an agency is even a candidate: no money at all rules it out, and that is no big deal because we all start that way.
  anchor: >-
    you have no money, then agencies are out of the question. You've gotta
  source: >-
    100m-leads.md, #3 Agencies, lines 11635–11640
  confirmations: 1
  anchor_at: "100m-leads.md:11636"
- id: D-leads-2-052
  type: rule
  name: >-
    You only get a fraction of an agency's attention
  statement: >-
    An agency's results for you get worse every time they take on new clients, because you hold only a fraction of their attention.
  why: >-
    Meanwhile your own team gets better and better because they stay focused on you full-time, which is why the comparison to run is your team's results against the agency's.
  boundary: >-
    Sets the ceiling on what an agency relationship can deliver over time and the moment to end it - when your team beats theirs.
  anchor: >-
    agency's attention, so results get worse whenever they get new clients.
  source: >-
    100m-leads.md, #3 Agencies, lines 11733–11738
  confirmations: 1
  anchor_at: "100m-leads.md:11734"
- id: D-leads-2-053
  type: antipattern
  name: >-
    Reading price as proof of an agency
  statement: >-
    Taking an agency's high price, or the ads it runs for itself, as evidence that it is good.
  why: >-
    All good agencies are expensive, but not all expensive agencies are good; and an agency you only know from its own paid ads or cold outreach is probably not as good as the ones that rely solely on word of mouth, which the best ones do.
  applies_when: >-
    Talk with as many agencies as it takes and score them against the ten-point list (known results, prominent clients, a waiting list, realistic expectations, no short term hacks, clear asks, a meeting schedule, simple tracking, a good offer, expensive).
  anchor: >-
    agencies are expensive... but not all expensive agencies are good. So
  source: >-
    100m-leads.md, #3 Agencies, lines 11774–11833
  confirmations: 2
  anchor_at: "100m-leads.md:11830"
- id: D-leads-2-054
  type: rule
  name: >-
    The agency method costs double for a while
  statement: >-
    Making the learn-from-the-agency method work at scale means paying the agency and your own team to do the same stuff for a good amount of time.
  why: >-
    You have to give yourself breathing room to get results from the agency, learn what they do and train your team on it all at once; it costs a lot of money and is worth it when you get it right.
  boundary: >-
    The author's own cost of entry for this method, and the reason it is out of reach without money to spare; it took him a year at first to get a team better than an agency, later ten months, then eight, and now under six.
  anchor: >-
    [And to make this agency method work at scale, you have to count on a
  source: >-
    100m-leads.md, #3 Agencies, lines 11866–11883
  confirmations: 2
  anchor_at: "100m-leads.md:11866"
- id: D-leads-2-055
  type: rule
  name: >-
    Affiliates are not referrals
  statement: >-
    Affiliates look like referrals from the outside but differ under the hood: they are independent businesses that do their own advertising and agree to offer your stuff to their engaged leads for money, free stuff, or both.
  why: >-
    Because they are businesses, the offer you make them is a way to make commissions rather than the product itself, which is what makes them one of the highest-leverage lead getters.
  not_to_confuse_with: >-
    Customer referrals, where the referrer is your customer and has no business or audience of their own.
  anchor: >-
    the outside, but are much different under the hood. First, they have
  source: >-
    100m-leads.md, #4 Affiliates and Partners, lines 12068–12075
  confirmations: 1
  anchor_at: "100m-leads.md:12071"
- id: D-leads-2-056
  type: antipattern
  name: >-
    Offering affiliates your product instead of a way to make money
  statement: >-
    Advertising your product to potential affiliates the way you would to customers, instead of offering them a fast, simple and easy way to make commissions promoting it.
  why: >-
    Affiliates demand a unique type of offer and will only sign up with a strong reason; since they are businesses, or start one by signing up, the reason is a new way to make money.
  applies_when: >-
    The affiliate offer is still built the same way as any other - call out, value elements, call to action - with affiliates as the customer you advertise to.
  anchor: >-
    affiliates demand a unique type of offer. Instead of offering your
  source: >-
    100m-leads.md, #4 Affiliates and Partners, lines 12079–12085
  confirmations: 1
  anchor_at: "100m-leads.md:12081"
- id: D-leads-2-057
  type: rule
  name: >-
    An affiliate who will not buy it should not sell it
  statement: >-
    Affiliates are made to buy, and preferably use, the product to keep affiliate status.
  why: >-
    The more money an affiliate invests in your product the more money they make, and if they do not believe in your stuff enough to buy it, they probably should not sell it. Nine times out of ten, if they pay, they'll pay attention.
  boundary: >-
    This is the lowest barrier investment that worked for the author; the other is making them pay for the certification that makes them a product expert.
  anchor: >-
    the more money they make. This should make sense. If they don't believe
  source: >-
    100m-leads.md, #4 Affiliates and Partners, lines 12386–12405
  confirmations: 2
  anchor_at: "100m-leads.md:12403"
- id: D-leads-2-058
  type: rule
  name: >-
    Too low and they are not invested, too high and there are not enough
  statement: >-
    The onboarding and certification fee for affiliates is set at 10-20% of what the average active affiliate makes in the first twelve months.
  why: >-
    Too low and you will not get them invested; too high and you will not get enough affiliates. The author found 10-20% maximises the number of people who become active affiliates.
  boundary: >-
    A two-sided limit, not a floor: the fee has an upper bound set by recruitment volume and a lower bound set by commitment.
  applies_when: >-
    If you are just starting with physical products, use the bulk purchasing strategy; otherwise raise the minimum investment every five sign ups until you hit the sweet spot.
  anchor: >-
    get them invested. Too high and you won't get enough affiliates. I found
  source: >-
    100m-leads.md, #4 Affiliates and Partners, lines 12429–12439
  confirmations: 1
  anchor_at: "100m-leads.md:12433"
- id: D-leads-2-059
  type: antipattern
  name: >-
    Giving away the farm to every affiliate
  statement: >-
    Paying the whole maximum allowable CAC to every affiliate regardless of what they have done.
  why: >-
    Not all affiliates are created equal; a three-tier payout (on agreeing, on activating, on sustaining performance) makes the average payout much less than the maximum allowable CAC, and the leftover funds contests, recruiting and rising stars - in one example the blended payout of $30 against a $40 maximum moves LTGP:CAC from 3:1 to 4:1.
  anchor: >-
    [But here's where things get interesting. I used to give away the farm
  source: >-
    100m-leads.md, #4 Affiliates and Partners, lines 12516–12572
  confirmations: 2
  anchor_at: "100m-leads.md:12516"
- id: D-leads-2-060
  type: antipattern
  name: >-
    Affiliates can't work for my business
  statement: >-
    Deciding that affiliates do not work for your kind of business, instead of taking it as your job to make them work.
  why: >-
    The author states it as the difference between the loser and the winner: "I have to make affiliates work for my business" the winner said.
  anchor: >-
    ["Affiliates can't work for my business" the loser said.]{.calibre24}
  source: >-
    100m-leads.md, #4 Affiliates and Partners, line 13057
  confirmations: 1
  anchor_at: "100m-leads.md:13057"
- id: D-leads-2-061
  type: rule
  name: >-
    Affiliate returns are not measured against money from affiliates
  statement: >-
    You do not compare the cost of getting an affiliate with money made from the affiliate; you compare it with the gross profit of all the customers they send you.
  why: >-
    You spend money to get affiliates but do not make much back from them directly - the money comes back from the customers they bring.
  not_to_confuse_with: >-
    The LTGP to CAC calculation for customers, where the money comes back from the same person you paid to acquire.
  anchor: >-
    We spend money to get affiliates, sure. But we don't really make much
  source: >-
    100m-leads.md, #4 Affiliates and Partners, lines 13066–13076
  confirmations: 1
  anchor_at: "100m-leads.md:13070"
- id: D-leads-2-062
  type: antipattern
  name: >-
    Shortcuts, and switching methods after a few losses
  statement: >-
    Chasing quick wins and changing advertising methods after a few losses, instead of picking one and sticking with it.
  why: >-
    People try shortcuts for a decade until they realise they should have picked a strategy and stuck with it for a decade; an obsession with getting rich quick will likely ensure it never happens, and it is normal to lose in the beginning. You have to forget the idea that everything is going to work out the first time.
  anchor: >-
    People try shortcuts for a decade until they realize they should have
  source: >-
    100m-leads.md, Section IV Conclusion: Get Lead Getters, lines 13294–13321
  confirmations: 3
  anchor_at: "100m-leads.md:13309"
- id: D-leads-2-063
  type: rule
  name: >-
    Three to six months to crack a new lead source
  statement: >-
    The author expects to crack a new lead source in three to six months, and this is not his first rodeo.
  why: >-
    He offers it as the yardstick for judging your own expectations: if yours are faster than that, ask whether they are reasonable.
  boundary: >-
    A timing boundary on every method in the book: a few losses inside that window are not evidence that the method failed.
  anchor: >-
    in three to six months (and this isn't my first rodeo). So if your
  source: >-
    100m-leads.md, Section IV Conclusion: Get Lead Getters, lines 13306–13321
  confirmations: 1
  anchor_at: "100m-leads.md:13318"
- id: D-leads-2-064
  type: antipattern
  name: >-
    A test too small to read
  statement: >-
    Running a test at a volume where even a good response rate cannot be distinguished from noise - 300 flyers instead of the 5000 the mentor tested with.
  why: >-
    At half a percent, 300 flyers would be one and a half people, which makes it pretty hard to know whether you got a winner; half a percent is decent and one percent is a winner, and the mentor tested 5000 in a single day, then ran 5000 per day for a month once he found a winner.
  anchor: >-
    ["Shoot, you only put out 300? Hard to know if anything works with such
  source: >-
    100m-leads.md, Advertising in Real Life: Open To Goal, lines 13695–13714
  confirmations: 2
  anchor_at: "100m-leads.md:13695"
- id: D-leads-2-065
  type: antipattern
  name: >-
    Underestimating the volume
  statement: >-
    Concluding a method does not work after doing a fraction of the volume it requires - counting reach outs over weeks when the number was per day.
  why: >-
    The right action in the wrong amount still fails; most people stop too soon and are not doing half or a third of what is required but dramatically less. The author was doing 1/1500th of the effort a flyer campaign needs; "I reached out to 100 people over the last six weeks" is 1/42 of the work, because it was 100 per day, not 100 over time.
  applies_when: >-
    Advertising is an inputs and outputs game: you input advertising effort, your output is engaged leads.
  anchor: >-
    [Most people dramatically underestimate the volume it takes to make
  source: >-
    100m-leads.md, Advertising in Real Life: Open To Goal, lines 13738–13763
  confirmations: 3
  anchor_at: "100m-leads.md:13746"
- id: D-leads-2-066
  type: antipattern
  name: >-
    Doing your best instead of what is required
  statement: >-
    Measuring a day's advertising by effort given rather than by the outcome that had to be hit.
  why: >-
    Open to goal means working until the job is done: give up the idea of doing your best and instead do what is required - and sometimes that means your best just needs to get better.
  applies_when: >-
    Open To Goal is the next level above the rule of 100: you commit to the work until you hit a specific number of outcomes, no matter what.
  anchor: >-
    of 'doing your best.' Instead, do what is required. And sometimes that
  source: >-
    100m-leads.md, Advertising in Real Life: Open To Goal, lines 13801–13804
  confirmations: 1
  anchor_at: "100m-leads.md:13803"
- id: D-leads-2-067
  type: antipattern
  name: >-
    Skipping the plan, or writing a hundred-page one
  statement: >-
    Either doing no planning at all or writing a one hundred page plan that never gets used.
  why: >-
    The power is in laying the action steps out on a single page, which leaves little room for excuses, distractions and delusions - you either did the stuff or you didn't - and the one page advertising checklist takes about five minutes to fill out.
  anchor: >-
    [Many skip planning, or worse, they write a one hundred page plan that
  source: >-
    100m-leads.md, Advertising in Real Life: Open To Goal, lines 13954–13961
  confirmations: 1
  anchor_at: "100m-leads.md:13954"
- id: D-leads-2-068
  type: antipattern
  name: >-
    Letting the product slip while scaling advertising
  statement: >-
    Going back to scaling advertising with a bigger team while the product slides, instead of holding the product until referrals are consistent.
  why: >-
    This is where most people mess up - they let their product slip and never recover. At level 4 the work is the product until 25% or more of customers come from referrals, and only then the advertising ramps again.
  applies_when: >-
    Level 4 of the roadmap, after employees are already doing advertising on your behalf.
  anchor: >-
    bigger team. This is where most people mess up. They let their product
  source: >-
    100m-leads.md, The Roadmap - Putting it All Together, lines 14070–14073
  confirmations: 1
  anchor_at: "100m-leads.md:14072"
- id: D-leads-2-069
  type: rule
  name: >-
    The roadmap looks clean, real business is messy
  statement: >-
    The seven levels are presented as a clean sequence, and the author states they never run that way in reality.
  why: >-
    It takes a lot to find which audiences, lead magnets, methods and platforms work best, and you can only find out by trying a lot of different things, a lot of different ways, for long enough to know. Nobody can ever know the absolute best thing to do.
  boundary: >-
    An explicit limit on his own roadmap: it orders what tends to happen, it does not predict what will happen in a particular business.
  anchor: >-
    [Last Points]{.calibre41}[: I know this looks clean. But it never is.
  source: >-
    100m-leads.md, The Roadmap - Putting it All Together, lines 14134–14147
  confirmations: 2
  anchor_at: "100m-leads.md:14134"
- id: D-leads-2-070
  type: rule
  name: >-
    Five to ten years to the $100M lead machine
  statement: >-
    For business owners who know what to do, building the $100M lead machine takes anywhere from five to ten years.
  why: >-
    Building something great takes time even when you know exactly what to do; behind the overnight success stories the curtain tells a different story, and it took the author and his wife more than ten years of their best effort to cross the first $100M in net worth.
  boundary: >-
    A timing boundary on the whole book: the bigger the goal, the longer the time horizon has to be.
  anchor: >-
    [How long does this take? For business owners who know what to
  source: >-
    100m-leads.md, The Roadmap - Putting it All Together, lines 14199–14206
  confirmations: 2
  anchor_at: "100m-leads.md:14199"
```
