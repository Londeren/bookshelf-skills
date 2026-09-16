# Улов фазы 1 — $100M Leads (2023), from #4 Run Paid Ads to the end (lines 6901–14623) (ярус 1), тип E: глоссарий

Группа `tier1-leads-2`, слаг `leads-2`, ярус 1. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **42** (экстрактор вернул 42, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-leads.md` | 6901–14623 | 7 | 42 |

## Как собран файл

Экстрактор E (Glossary) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier1-leads-2.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier1-leads-2-E.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: E-leads-2-001
  type: term
  name: >-
    Paid ads
  statement: >-
    Paid ads are one-to-many advertising to cold audiences, bought by paying another person or business to put your offer in front of their audience.
  definition: >-
    Paid ads are a way to advertise one-to-many to cold audiences. People who don't know you. Paid ads work by paying another person or business to put your offer in front of their audience. Think of it like renting eyeballs or earballs.
  why: >-
    Because you don't need to spend time building an audience, paid ads are the fastest way to get the most people to see your stuff - you trade money for reach. The reach is guaranteed, but getting your money back isn't, so paid ads are a game of efficiency rather than reach.
  anchor: >-
    [Paid ads are a way to advertise one-to-many to cold audiences. People
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, lines 7041–7058
  confirmations: 1
  anchor_at: "100m-leads.md:7041"
- id: E-leads-2-002
  type: term
  name: >-
    Cocktail party effect
  statement: >-
    The cocktail party effect is the fact that even in a room full of noise one single thing can still catch and hold attention, which is the mechanism a callout harnesses.
  definition: >-
    Scientists call it the 'cocktail party effect'. In simple terms, even when there's tons of stuff going on, a single thing can still catch and hold our attention. So our goal with callouts is to harness the cocktail party effect and cut through all the noise.
  why: >-
    After all, if they never notice your ad, nothing else matters.
  anchor: >-
    [Scientists call it the 'cocktail party effect'. In simple terms, even
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, Step #3 Call Out, lines 7328–7341 (the author attributes the name to scientists)
  confirmations: 1
  anchor_at: "100m-leads.md:7336"
- id: E-leads-2-003
  type: term
  name: >-
    Callout
  statement: >-
    A callout is whatever you do to get the attention of your audience, made specific enough to get the right people and broad enough to get as many of them as you can.
  definition: >-
    A callout is whatever you do to get the attention of your audience. Call outs go from hyperspecific - to get one person's attention - to not at all specific - to get everyone's attention.
  why: >-
    People noticing your ad is the most important part of the ad...by a lot; the callout is the first of the three core elements of every ad the author makes (callouts, value elements, calls to action).
  anchor: >-
    [A ]{.calibre3}[callout]{.calibre11}[ ]{.calibre3}[is whatever you do to
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, Step #3 Call Out, lines 7345–7355
  confirmations: 2
  anchor_at: "100m-leads.md:7345"
- id: E-leads-2-004
  type: term
  name: >-
    Verbal callouts
  statement: >-
    Verbal callouts are the words used to get attention, of four kinds: Labels, Yes-Questions, If-Then Statements and Ridiculous Results.
  definition: >-
    Here's what I look for with verbal callouts- using words to get attention. Labels: a word or set of words putting people into a group (features, traits, titles, places and other descriptors), and to be most effective your ideal customers need to identify with the label. Yes-Questions: questions where if people answer "yes, that's me" they qualify themselves for the offer. If-Then Statements: if they meet your conditions then you help them make a decision. Ridiculous Results: bizarre, rare, or out of the ordinary stuff someone would want.
  anchor: >-
    [Here's what I look for with verbal callouts- ]{.calibre3}[using words
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, Step #3 Call Out, lines 7359–7404
  confirmations: 1
  anchor_at: "100m-leads.md:7359"
- id: E-leads-2-005
  type: term
  name: >-
    Nonverbal callouts
  statement: >-
    Nonverbal callouts are the setting and the spokesperson used to get attention, of three kinds: Contrast, Likeness and The Scene.
  definition: >-
    Here's what I look for with nonverbal callouts- using the setting and spokesperson to get attention. Contrast: any stuff that "sticks out" in the first few seconds - the colors, the sounds, the movements. Likeness: visually showing labels - features, traits, titles, places, and other descriptors that people identify with. The Scene: showing the Yes-Questions and If-Then statements.
  why: >-
    So if the platform allows, good advertisers use verbal and nonverbal callouts together.
  anchor: >-
    [Here's what I look for with nonverbal callouts- ]{.calibre3}[using the
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, Step #3 Call Out, lines 7407–7512
  confirmations: 1
  anchor_at: "100m-leads.md:7420"
- id: E-leads-2-006
  type: term
  name: >-
    What-Who-When Framework
  statement: >-
    The What-Who-When Framework is the author's way of producing advertising angles: the eight key elements of value (What), the people whose treatment gives the customer status (Who), and the prospect's past-present-future (When).
  definition: >-
    This mental framework hinges on knowing the value equation forwards and backwards. So all you have to do is know eight key things about your own product or service: how it fulfills each element of value for your prospect, and how it helps them avoid their hidden costs. Then think of the perspectives of the people who would experience them (Who). And finally, what time period (When) they'd have these experiences (positive or negative).
  why: >-
    Putting the What, the Who, and the When together, we answer WHY they should be interested; the more angles we cover, the more interested they'll become, and the only difference between long ads and short ads is how many angles we have time to cover.
  anchor: >-
    share with you my What-Who-When Framework. This mental framework hinges
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, Step #3 Get Them Interested, lines 7549–7563
  confirmations: 3
  anchor_at: "100m-leads.md:7553"
- id: E-leads-2-007
  type: term
  name: >-
    Status
  statement: >-
    Status is what other humans give a person by how they treat them, so the value of your product is shown through the eyes of the people around the customer.
  definition: >-
    Humans are primarily status driven. And the status of one human comes from how the other humans treat them. So if your product or service changes how other people treat your customer, which it does in some way, it pays to show how.
  why: >-
    Talking about the value elements from someone else's perspective shows all the ways it'll improve the status of your customer and gives a ton of bonus benefits you'd miss if you only looked at it from their own perspective.
  anchor: >-
    [Who]{.calibre11}[: Humans are primarily status driven. And the status
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, The Who, lines 7664–7673
  confirmations: 2
  anchor_at: "100m-leads.md:7664"
- id: E-leads-2-008
  type: term
  name: >-
    Engaged lead
  statement: >-
    An engaged lead is someone who has shown interest in the stuff you sell by giving you permission to contact them.
  definition: >-
    To be clear, we aren't selling anything. We are asking if they're interested in the stuff we sell. And if they're interested, they'll give us a way to tell them more about it. And when they do, they become engaged leads.
  not_to_confuse_with: >-
    A lead who has not yet shown interest: Lead getters start out as leads, then get interested in the stuff you sell and become engaged leads like anyone else.
  why: >-
    Once they have a reason to take action, they have to have a way to give us permission to contact them. That action turns them into an engaged lead.
  anchor: >-
    interested in the stuff we sell. And if they're interested, they'll give
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, Step #4 Get Permission To Contact Them, lines 7951–7954
  confirmations: 3
  anchor_at: "100m-leads.md:7952"
- id: E-leads-2-009
  type: term
  name: >-
    Lifetime gross profit (LTGP)
  statement: >-
    Lifetime gross profit is all the money a customer ever spends with you minus all the money it takes to deliver it.
  definition: >-
    Lifetime gross profit is all the money a customer ever spends on your stuff minus all the money it takes to deliver it. For example, if a customer buys something for $15 and it costs $5 to deliver it, your gross profit is $10. So if that customer buys ten things over their lifetime, then they bought a total of $150 in stuff. But it cost you a total of $50 to deliver that stuff. That makes the lifetime gross profit $100.
  not_to_confuse_with: >-
    "Lifetime Value" or "LTV" - the author's heading is "I Measure LTGP Instead of 'Lifetime Value' or 'LTV'", because gross profit is the actual money you use to acquire customers, pay rent, cover payroll, and everything else to run your business.
  anchor: >-
    [Lifetime gross profit]{.calibre11}[ is all the money a customer ever
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8217–8233
  confirmations: 2
  anchor_at: "100m-leads.md:8221"
- id: E-leads-2-010
  type: term
  name: >-
    LTGP to CAC
  statement: >-
    LTGP to CAC is the author's measure of advertising efficiency: the lifetime gross profit of a customer compared with the cost to acquire one.
  definition: >-
    I measure paid ad efficiency by comparing the lifetime gross profit of a customer (LTGP) with the cost to acquire a customer (CAC). I express this ratio as LTGP to CAC.
  why: >-
    So if LTGP is greater than CAC, you have profitable advertising. If it's lower than CAC, you're losing money. Every business the author invests in that struggles to scale has an LTGP to CAC ratio of less than 3 to 1, and takes off as soon as it goes above 3 to 1.
  anchor: >-
    (LTGP) with the cost to acquire a customer (CAC). I express this ratio
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, Cost & Returns, lines 8209–8253
  confirmations: 3
  authors_caveat: >-
    On the 3 to 1 threshold: This is a pattern I personally observed, not a rule.
  anchor_at: "100m-leads.md:8212"
- id: E-leads-2-011
  type: term
  name: >-
    Client financed acquisition
  statement: >-
    Client financed acquisition is when the customer pays you more than it costs to get and fulfill them within the first thirty days, so the same cash can be recycled into the next customer.
  definition: >-
    But... if your customer spends more than it costs you to get and fulfill them--in the first 30 days--then you have the funds to scale now and forever. I call this client financed acquisition.
  why: >-
    I pick thirty days because any business can get interest free money for thirty days in the form of a credit card. And if we make more than the cost to get and fulfill the customer in the first thirty days, we square our balance. Money is no longer your bottleneck. This is the key to limitless scale.
  anchor: >-
    [But... if your customer spends more than it costs you to get
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, Client Financed Acquisition, lines 8337–8351
  confirmations: 3
  anchor_at: "100m-leads.md:8337"
- id: E-leads-2-012
  type: term
  name: >-
    Sales problem (as opposed to an advertising problem)
  statement: >-
    If engaged leads have the problem you solve and the money to spend and still do not buy, that is a sales problem, not an advertising problem.
  definition: >-
    If your engaged leads have the problem you solve and the money to spend, and they're not buying, then your ads work fine--you have a sales problem. The diagnostic question is: Do my engaged leads have the problem I solve and the money to spend?
  not_to_confuse_with: >-
    An advertising problem: if the leads are not qualified, that's an advertising problem; if they are qualified and buying but there aren't enough of them, that's also an advertising problem.
  why: >-
    A company the author invested in spent twelve weeks and $150,000 on ads, blamed advertising, and gave up; confusing an advertising problem with a sales problem cost them an estimated ~$30M in enterprise value. Don't fire your sales guy if you've got advertising problems, and don't fire your advertising employees if you've got a sales problem.
  anchor: >-
    the problem you solve and the money to spend, and they're not
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, Personal Lessons from Paid Ads, lines 8463–8475
  confirmations: 2
  anchor_at: "100m-leads.md:8473"
- id: E-leads-2-013
  type: term
  name: >-
    The core four
  statement: >-
    The core four are the only four ways a single person can let other people know about their stuff: warm outreach, posting free content, cold outreach and paid ads.
  definition: >-
    First, you reach out to people who know you. Then, you start making free content. Then you start reaching out to people who don't know you. Then you start running paid ads. This is how you do the core four to get engaged leads. And there's really nothing else a single person can do on their own to get them.
  why: >-
    You only need to do one to get engaged leads, but all the advertising methods compound together: every combination of the core four advertising activities boosts each other in some way.
  anchor: >-
    [First, you reach out to people who know you. Then, you start making
  source: >-
    100m-leads.md, Core Four On Steroids: More Better New, lines 8724–8729
  confirmations: 3
  anchor_at: "100m-leads.md:8724"
- id: E-leads-2-014
  type: term
  name: >-
    More, Better, New
  statement: >-
    More Better New are the three ways to boost any of the core four on your own: do more of what you're currently doing, do what you're currently doing better, or do it somewhere new.
  definition: >-
    You can do more of what you're currently doing. You can do what you're currently doing better. You can do it somewhere new. Could you advertise more? Could you advertise better? Could you advertise somewhere new?
  applies_when: >-
    Exhaust more better first. When to do new: when the returns you get from doing more and better are lower than what you could get from a new placement or new way of advertising. Use this rough order: new placement, new platform, new core four activity.
  anchor: >-
    you advertise more? Could you advertise better? Could you advertise
  source: >-
    100m-leads.md, Core Four On Steroids: More Better New, lines 8738–8763
  confirmations: 3
  anchor_at: "100m-leads.md:8762"
- id: E-leads-2-015
  type: term
  name: >-
    The Rule of 100
  statement: >-
    The rule of 100 is doing 100 primary advertising actions, or 100 minutes of making content or ads, every day for one hundred days in a row.
  definition: >-
    The rule of 100 is simple. You advertise your stuff by doing 100 primary actions every day, for one hundred days in a row. Applied to the core four: 100 warm reach outs per day; 100 minutes per day making content, with at least one release per day; 100 cold reach outs per day; 100 minutes per day making paid ads and 100 days straight of running them.
  why: >-
    If you do 100 primary actions per day, and you do it for 100 days straight, you will get more engaged leads. Commit to the rule of 100 and you will never go hungry again.
  anchor: >-
    [The rule of 100 is simple. You advertise your stuff by doing 100
  source: >-
    100m-leads.md, Core Four On Steroids: More Better New, Here's how I do more: The Rule of 100, lines 8805–8885
  confirmations: 3
  anchor_at: "100m-leads.md:8810"
- id: E-leads-2-016
  type: term
  name: >-
    Constraints
  statement: >-
    Constraints are the steps where the most leads drop off, the points where the smallest improvement creates the biggest boost in results.
  definition: >-
    Every action a lead takes before they become a customer is a potential "drop-off" point. So I do the most testing at whatever step the most leads drop off. I call these "constraints." Constraints are the points where the smallest improvements create the biggest boost in results.
  applies_when: >-
    If you're not sure which step is the biggest constraint, find the step where the most leads drop off. You'll get the biggest reward for the smallest improvement.
  anchor: >-
    Constraints are the points where the smallest improvements create the
  source: >-
    100m-leads.md, Core Four On Steroids: More Better New, Better, lines 8924–8970
  confirmations: 2
  anchor_at: "100m-leads.md:8927"
- id: E-leads-2-017
  type: term
  name: >-
    The Size Of The Pie Fallacy
  statement: >-
    The Size Of The Pie Fallacy is mistaking the tiny slice of the market you currently advertise to for the entire available market.
  definition: >-
    A small business uses one of the core four, on one platform, in one specific way, with a very targeted audience. And in that same space, advertising the same way, there may only be a handful of other competitors. They mistakenly assume the tiny slice of the universe they advertise to is the entire available market!
  why: >-
    This is why most businesses stay small. When they plateau, they think there's no more leads to get. For many, saying "I'm as big as I can get" is much easier than saying "I'm not as good at advertising as I thought."
  anchor: >-
    universe they advertise to is the entire available market! This is why
  source: >-
    100m-leads.md, Core Four On Steroids: More Better New, New, lines 9068–9100
  confirmations: 1
  anchor_at: "100m-leads.md:9094"
- id: E-leads-2-018
  type: term
  name: >-
    Advertising
  statement: >-
    Advertising is the process of making known - what you do to let strangers know about the stuff you sell.
  definition: >-
    Advertising is the process of making known. It's what we do to let strangers know about the stuff we sell.
  anchor: >-
    [Advertising]{.calibre11}[ is ]{.calibre3}[the process of making
  source: >-
    100m-leads.md, Core Four On Steroids: More Better New, Conclusion, lines 9200–9201
  confirmations: 1
  anchor_at: "100m-leads.md:9200"
- id: E-leads-2-019
  type: term
  name: >-
    Leverage
  statement: >-
    Leverage is how much you get for the time you spend getting it.
  definition: >-
    That means leverage boils down to how much we get for the time we spend getting it. So we want to use higher leverage activities to get what we want. More stuff we want. Less time getting it.
  anchor: >-
    [That means leverage boils down to how much we get for the time we spend
  source: >-
    100m-leads.md, Section IV: Get Lead Getters, lines 9294–9315
  confirmations: 2
  anchor_at: "100m-leads.md:9313"
- id: E-leads-2-020
  type: term
  name: >-
    Lead getters
  statement: >-
    Lead getters are other people who do the core four on your behalf - customers, employees, agencies and affiliates.
  definition: >-
    People can find out about the stuff we sell from two sources. We can let them know using the core four. Or, other people can let them know using the core four. I call these other people lead getters. Customers buy your stuff then tell other people about it; employees are people in your business that get you leads; agencies are businesses with services that get you leads; affiliates are businesses who tell their audiences about your stuff to get you leads.
  not_to_confuse_with: >-
    A core four activity: The lead getters aren't part of the "core four" because they're not things you do. You do not 'do' affiliates or 'do' customer referrals or 'do' agencies or 'do' employees. But, you have to do the core four to get them.
  why: >-
    When other people do it for us, we save time. That means we get more engaged leads for less work.
  anchor: >-
    four. I call these other people ]{.calibre3}[lead getters]{.calibre11}[.
  source: >-
    100m-leads.md, Section IV: Get Lead Getters, lines 9340–9345
  confirmations: 3
  anchor_at: "100m-leads.md:9343"
- id: E-leads-2-021
  type: term
  name: >-
    Referral
  statement: >-
    A referral happens when a referrer sends an engaged lead to your business, and the best referrals come from your customers.
  definition: >-
    A referral happens when somebody, a referrer, sends an engaged lead to your business. Anyone can refer, but the best referrals come from your customers.
  why: >-
    Referrals grow the business in two ways: they're worth more (higher LTGP) and they cost less (lower CAC). And unlike the core four, whose inputs and outputs are linear, referrals are exponential - one customer brings two, two bring four.
  anchor: >-
    [A referral happens when somebody, a referrer, sends an engaged lead to
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, How Referrals Work, lines 9758–9761
  confirmations: 1
  anchor_at: "100m-leads.md:9758"
- id: E-leads-2-022
  type: term
  name: >-
    Referral growth equation
  statement: >-
    The referral growth equation is referrals in minus churned customers out.
  definition: >-
    Look at the referral growth equation to see it in action. Referrals (in) minus churned customers (out).
  why: >-
    If referrals are greater than churn you grow without any other advertising; if they equal churn you need other advertising to grow; if they are less than churn you have to advertise just to break even. With referrals, you can maintain growth no matter how big you get.
  anchor: >-
    get them. Look at the referral growth equation to see it in action.
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, How Referrals Grow Your Business, lines 9813–9832
  confirmations: 1
  anchor_at: "100m-leads.md:9815"
- id: E-leads-2-023
  type: term
  name: >-
    Goodwill
  statement: >-
    Goodwill is the difference between the price you charge and the value the customer gets.
  definition: >-
    Price is what you charge. Value is what they get. The difference between price and value is goodwill.
  not_to_confuse_with: >-
    The economists' term: Economics dorks call it 'customer surplus'. But I'm just gonna call it goodwill.
  why: >-
    You want lots of goodwill. Lots of goodwill creates word of mouth. Word of mouth means referrals. There are two ways to build it - lower your price or give more value - and lowering the price is at best a temporary solution.
  anchor: >-
    [Price is what you charge. Value is what they get. ]{.calibre3}[The
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, Problem #1 The Product Isn't Good Enough, lines 9913–9938
  confirmations: 2
  anchor_at: "100m-leads.md:9913"
- id: E-leads-2-024
  type: term
  name: >-
    Win
  statement: >-
    A win is any positive experience a customer has, and wins are made to feel faster by giving them more often rather than by delivering faster.
  definition: >-
    I define a "win" as any positive experience a customer has. Faster wins increase their perception of speed, increase the likelihood they'll stick, and increase how much they trust you. Triple win. To make wins feel faster, we give them wins more often.
  anchor: >-
    "win" as any positive experience a customer has. Faster wins
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, Decrease Time Delay, lines 10147–10160
  confirmations: 1
  anchor_at: "100m-leads.md:10148"
- id: E-leads-2-025
  type: term
  name: >-
    BAMFAM
  statement: >-
    BAMFAM means Book-A-Meeting-From-A-Meeting: the customer always leaves knowing the next time they will hear from you.
  definition: >-
    They should always know the next time they'll hear from you. I got a slick saying from a public CEO friend of mine - BAMFAM: Book-A-Meeting-From-A-Meeting. Again, never leave a customer in no man's land. They should always know what happens...next.
  anchor: >-
    a slick saying from a public CEO friend of mine - BAMFAM:
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, Decrease Time Delay, lines 10181–10185 (the author credits a public CEO friend for the saying)
  confirmations: 1
  anchor_at: "100m-leads.md:10182"
- id: E-leads-2-026
  type: term
  name: >-
    Lead-getting employees
  statement: >-
    Lead-getting employees are people working in your business whom you train to get you leads the same way you got your own.
  definition: >-
    Lead-getting employees are people working in your business that you train to get you leads. They get you leads the exact same way you got your own leads in the beginning. They can run ads, they can make and post content, and they can do outreach. They can do any advertising you train them to do.
  why: >-
    Employees take work, they just take less time and work than doing everything on your own: if you trade forty hours of doing for four hours of managing, you work thirty-six hours less. Employees make a fully functioning enterprise that grows without you.
  anchor: >-
    your business that you train to get you leads. They get you leads the
  source: >-
    100m-leads.md, #2 Employees, How Employees Work, lines 10807–10833
  confirmations: 1
  anchor_at: "100m-leads.md:10808"
- id: E-leads-2-027
  type: term
  name: >-
    Asset (a business that runs without you)
  statement: >-
    A business that makes money without you is an asset someone else can buy; a business that only makes money with you in it is a liability worth almost nothing.
  definition: >-
    If you have an asset that makes millions of dollars without you then that means somebody else could use it to make millions of dollars without them. In other words, your business is now a good investment. You turned a liability that relied on you into an asset you can rely on.
  why: >-
    If the business only makes money with you in it, then it's a bad investment for anyone else. The same $2,000,000 of profit per year, especially if it's climbing, could easily be worth $10,000,000+ right now, so learning how to get other people to do it for you makes a $10,000,000 difference to your net worth.
  anchor: >-
    [If you have an asset that makes millions of dollars
  source: >-
    100m-leads.md, #2 Employees, Why Employees Make You Wealthy, lines 10869–10899
  confirmations: 1
  anchor_at: "100m-leads.md:10887"
- id: E-leads-2-028
  type: term
  name: >-
    Rich versus wealthy
  statement: >-
    You get rich from what you make and you become wealthy from what you own.
  definition: >-
    Reminder: You get rich from what you make. You become wealthy from what you own.
  not_to_confuse_with: >-
    Being rich: a business that pays you $2,000,000 a year while requiring you around the clock is a high paying job, not wealth - the business itself isn't worth much.
  anchor: >-
    [Reminder: ]{.calibre3}[You get rich from what you make. You become
  source: >-
    100m-leads.md, #2 Employees, Why Employees Make You Wealthy, lines 10903–10905
  confirmations: 1
  anchor_at: "100m-leads.md:10903"
- id: E-leads-2-029
  type: term
  name: >-
    The Internal Core Four
  statement: >-
    The internal core four is the core four aimed at potential employees instead of potential customers.
  definition: >-
    Remember the core four? Well, they work for getting employees too. Warm Outreach becomes Asking Your Network; Cold Outreach becomes Recruiting; Post Content becomes Posting Job Openings; Paid Ads becomes Promoting Job Postings. Customer Referrals become Employee Referrals; Affiliates become associations, guilds, listservs; Agencies become staffing firms.
  why: >-
    Employees are just other people you let know about your stuff. So you do the same thing! When you need to get new talent, you just advertise to get it, and when you need more, you do more.
  anchor: >-
    [Remember the core four? Well, they work for getting employees too.
  source: >-
    100m-leads.md, #2 Employees, How To Get Employee Leads: The Internal Core Four, lines 11003–11058
  confirmations: 1
  anchor_at: "100m-leads.md:11007"
- id: E-leads-2-030
  type: term
  name: >-
    The 3Ds: document, demonstrate, duplicate
  statement: >-
    The 3Ds are the author's training model: you document the job as a checklist, you demonstrate it in front of the employee, then they duplicate it in front of you.
  definition: >-
    I think about and actually approach training with this 3Ds mental model: document, demonstrate, duplicate. Step One - Document: you make a checklist. Step Two - Demonstrate: you do it in front of them. Step Three - Duplicate: they do it in front of you.
  why: >-
    If the checklist is right, the outcome will be the same. And if the checklist is off - you'll find out fast. The level of clarity to shoot for: if you vanished tomorrow, could a stranger get the results you get if they only followed your checklist?
  anchor: >-
    activities. I think about and actually approach training with this 3Ds
  source: >-
    100m-leads.md, #2 Employees, How To Get Employees To Get You Leads, lines 11074–11137
  confirmations: 1
  anchor_at: "100m-leads.md:11080"
- id: E-leads-2-031
  type: term
  name: >-
    Competence versus performance
  statement: >-
    Competence is knowing exactly what to do; performance is being good at it, and a gap between them calls for practice rather than a new checklist.
  definition: >-
    There is a difference between competence and performance. In other words, they can know exactly what to do and not be that good at it yet. If that's the case, then your instructions are fine and they just need practice.
  why: >-
    You don't need to change anything, they just need more reps - as opposed to the case where a confused trainee means we got the checklist wrong or made it confusing.
  anchor: >-
    There is a difference between competence and performance. In other
  source: >-
    100m-leads.md, #2 Employees, Some helpful notes on training, lines 11158–11164
  confirmations: 1
  anchor_at: "100m-leads.md:11158"
- id: E-leads-2-032
  type: term
  name: >-
    Advertising agency
  statement: >-
    Advertising agencies are lead-getting service businesses you pay to run paid ads, do outreach, or package and distribute content.
  definition: >-
    Advertising agencies are lead-getting service businesses. You pay them to run paid ads, do outreach, or package and distribute content.
  applies_when: >-
    If you do have some money, I suggest using agencies for two things: learning new methods and learning new platforms. Hiring an agency is all about investing in important skills you can't really learn anywhere else.
  anchor: >-
    [Advertising agencies are lead-getting service businesses. You pay them
  source: >-
    100m-leads.md, #3 Agencies, How Agencies Want You To Think They Work, lines 11536–11538
  confirmations: 1
  anchor_at: "100m-leads.md:11536"
- id: E-leads-2-033
  type: term
  name: >-
    Affiliate
  statement: >-
    An affiliate is an independent business that tells its own audience to buy your stuff in exchange for money, free stuff, or both.
  definition: >-
    An affiliate is a lead-getter. They are an independent business that tells their audience to buy your stuff. First, they have their own businesses and do their own advertising. Second, they agree to offer your stuff to their engaged leads in exchange for money, free stuff, or both.
  not_to_confuse_with: >-
    Referrals: Affiliates seem like referrals on the outside, but are much different under the hood - affiliates have their own businesses and do their own advertising.
  why: >-
    You get affiliates by advertising and then making them offers just like you would customers. But affiliates demand a unique type of offer: instead of offering your product, you offer a fast, simple, and easy way to make commissions promoting it.
  anchor: >-
    [An ]{.calibre3}[affiliate]{.calibre11}[ is a lead-getter. They are an
  source: >-
    100m-leads.md, #4 Affiliates and Partners, How Affiliates Work, lines 12068–12085
  confirmations: 2
  anchor_at: "100m-leads.md:12068"
- id: E-leads-2-034
  type: term
  name: >-
    Maximum allowable CAC
  statement: >-
    The maximum allowable CAC is the slice of gross profit you can hand over to get one customer while keeping your target LTGP to CAC ratio.
  definition: >-
    I suggest paying affiliates based on your maximum allowable cost to acquire a customer (CAC). Example: we sell a single-use product for $200 and it costs $40 to fulfill. This gives us $160 to pay the affiliate and run the business. If we want an LTGP:CAC ratio of 3:1 then three parts goes to the business - $120. And one part, $40, goes to the affiliate.
  anchor: >-
    [I suggest paying affiliates based on your maximum allowable cost to
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 4: Figure Out What To Pay Them, lines 12501–12512
  confirmations: 2
  anchor_at: "100m-leads.md:12501"
- id: E-leads-2-035
  type: term
  name: >-
    Three-tier payout structure
  statement: >-
    A three-tier payout structure pays affiliates a rising share of the maximum allowable CAC as they agree to the terms, then activate, then sustain performance.
  definition: >-
    Not all affiliates are created equal. So, I suggest having a three-tier payout structure. Tier 1: 25% CAC - anyone who agrees to my initial terms qualifies. Tier 2: 50% CAC - once they activate (actually finishing the certification they bought, doing a number of posts and outreach, doing a launch). Tier 3: 100% CAC - once they sustain a level of performance.
  why: >-
    The average payout is much less than your maximum allowable CAC. If 20% of sales come from tier 1, 20% from tier 2 and 60% from tier 3, your blended payout is $30 instead of a maximum allowable CAC of $40, which moves the LTGP:CAC ratio from 3:1 to 4:1 and leaves money for contests, recruiting more affiliates and rising stars.
  anchor: >-
    a ]{.calibre3}[three-tier]{.calibre41}[ payout structure. Using the
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 4: Figure Out What To Pay Them, lines 12516–12572
  confirmations: 1
  anchor_at: "100m-leads.md:12519"
- id: E-leads-2-036
  type: term
  name: >-
    Launch
  statement: >-
    A launch is affiliates advertising your lead magnet or core offer to their audience before it can be bought, then selling it on launch day to the engaged leads they assembled.
  definition: >-
    Affiliates advertise your lead magnet or core offer to their audience before they can buy it. They post. They do warm outreach. They run paid ads. They may even do cold outreach. They do as much advertising as they can until the day of launch. When the product is available, they sell it to all the engaged leads they assembled.
  applies_when: >-
    Good launches have the work done ahead of time - do all the work for the affiliates so they can plug and play. Note: this is how you launch anything, not just affiliates; the author puts it in the affiliates section because he hasn't found a better way to activate affiliates than launches.
  anchor: >-
    [Affiliates advertise your lead magnet or core offer to their audience
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 5: Get Them Advertising -- Launch, lines 12599–12630
  confirmations: 2
  anchor_at: "100m-leads.md:12603"
- id: E-leads-2-037
  type: term
  name: >-
    Whisper-tease-shout
  statement: >-
    Whisper-tease-shout is the three-phase launch sequence: whisper to build curiosity, tease the elements of value, then shout the call to action.
  definition: >-
    I use the whisper-tease-shout method. Whisper: think "Call Outs" - the key to the whisper phase is curiosity; keep the product mysterious and hint at how big a deal it is. Tease: think "Elements Of Value" - reveal the product, make the launch date public and use the What-Who-When Framework. Shout: think "Call to Action" - give specific actions and pound the audience with bonuses, scarcity, urgency and guarantees.
  applies_when: >-
    Whisper every four to six weeks until sixty days out, then every two to three weeks until thirty days out; tease once per week until fourteen days out, then twice per week until three days out; shout at least twice a day from three days out, every few hours on the day, then every thirty minutes in the last two hours.
  anchor: >-
    should, you may as well do them right. I use the whisper-tease-shout
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 5: Get Them Advertising -- Launch, lines 12613–12727
  confirmations: 1
  anchor_at: "100m-leads.md:12614"
- id: E-leads-2-038
  type: term
  name: >-
    Lead magnet
  statement: >-
    The best lead magnets give away a free trial or sample of your thing, reveal a problem, or offer a single step of a multi-step solution.
  definition: >-
    Remember, the best lead magnets give away a free trial or sample of your thing, reveal a problem, or offer a single step of a multi-step solution. Samples and trials: everyone who buys from the affiliate gets a free massage from you. Reveal a problem: a free or discounted posture assessment, after which you make them an offer to solve the problems you revealed. One step in a multi-step process: the affiliate gives away step one of your three-part plan for free and you upsell the leads from there.
  anchor: >-
    it. Remember, the best lead magnets give away a free trial or sample of
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 6: Keep Them Advertising, lines 12778–12812
  confirmations: 1
  anchor_at: "100m-leads.md:12782"
- id: E-leads-2-039
  type: term
  name: >-
    Integration (with affiliates)
  statement: >-
    Integration is building your product into the affiliate's own offer so they keep sending leads: they give away your lead magnet, sell your lead magnet, or sell your core offer.
  definition: >-
    The strategy we use to start them advertising differs from the one we use to keep them advertising. In an ideal world, you sell an affiliate once and they send engaged leads for life. Integration gets us there. Integration is the long term strategy for using affiliates to get enduring lead flow.
  not_to_confuse_with: >-
    The launch, which is what starts them advertising; integration is what keeps them advertising.
  anchor: >-
    [Bottom Line]{.calibre41}[: Integration is the long term strategy for
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 6: Keep Them Advertising, lines 12744–12917
  confirmations: 2
  anchor_at: "100m-leads.md:12908"
- id: E-leads-2-040
  type: term
  name: >-
    Affiliate LTGP to CAC
  statement: >-
    With affiliates the return compares what it costs to get an affiliate with the gross profit of all the customers that affiliate sends you.
  definition: >-
    So to calculate returns, we compare how much it costs us to get an affiliate with the gross profit of all the customers they send to our business.
  why: >-
    We spend money to get affiliates, but we don't really make much back from affiliates themselves; the money we spend to get an affiliate comes back from the customers they bring us.
  anchor: >-
    compare how much it costs us to get an affiliate with the gross profit
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Costs and Returns, lines 13066–13138
  confirmations: 1
  anchor_at: "100m-leads.md:13074"
- id: E-leads-2-041
  type: term
  name: >-
    Super-affiliate
  statement: >-
    A super-affiliate is an affiliate who brings you other affiliates - the people who get you the people who get you customers.
  definition: >-
    With affiliates, you now have at least two layers of customers. Your customers, and the people who get you customers. And if you've got super-affiliates you add a third, the people who get you the people who get you customers! At ALAN, one super-affiliate added ten agencies per month, those agencies brought in about fifty local businesses per month, and those local businesses brought in about 2500 leads per month.
  anchor: >-
    super-affiliates you add a third, the people who get you the people who
  source: >-
    100m-leads.md, #4 Affiliates and Partners, lines 13170–13173 (with the ALAN example at lines 12154–12169)
  confirmations: 2
  anchor_at: "100m-leads.md:13172"
- id: E-leads-2-042
  type: term
  name: >-
    Open To Goal
  statement: >-
    Open to goal means working until you hit a set number of outcomes that day, no matter how long it takes.
  definition: >-
    A very successful gym chain allowed their sales managers to make their own schedules. But there was a catch--they had to sign up five new members per day no matter what. So if they did it by lunch, they could cut out early. But if it took 18 hours, so be it. They called this type of work schedule 'open-to-goal'.
  not_to_confuse_with: >-
    The rule of 100: You don't just commit to doing something a specific number of times... you commit to the work until you hit a specific number of outcomes--no matter what.
  why: >-
    It means you unlock a whole new level of effort you never even realized you had: give up the idea of 'doing your best' and instead do what is required.
  anchor: >-
    a specific number of times... you commit to the work until you hit a
  source: >-
    100m-leads.md, Advertising in Real Life: Open To Goal, lines 13780–13804
  confirmations: 2
  anchor_at: "100m-leads.md:13792"
```
