# Улов фазы 1 — $100M Series: Lost Chapters (2025) with $100M Leads: 2 Bonus Chapters (2023) as a second copy of Section A (ярус 2), тип E: глоссарий

Группа `tier2-lost-chapters`, слаг `lost-chapters`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **48** (экстрактор вернул 48, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-series-lost-chapters.md` | 1–4810 | 6 | 48 |
| `100m-leads-bonus-chapters.md` | 1–568 | 1 | 0 |

## Как собран файл

Экстрактор E (Glossary) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-lost-chapters.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-lost-chapters-E.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: E-lost-chapters-001
  type: term
  name: >-
    Avatar
  statement: >-
    The avatar is the narrowed decision of exactly which customers inside an already chosen market you serve and, more importantly, which you do not.
  definition: >-
    Choosing the perfect avatar is a subset of that larger decision This is where we become more nuanced about exactly who we serve, and more importantly, who we do not
  not_to_confuse_with: >-
    Picking the right market — the author calls market choice the larger strategic decision and the avatar a subset of it.
  anchor: >-
    Choosing the perfect avatar is a subset of that larger decision This is where we
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, line 236
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:236"
- id: E-lost-chapters-002
  type: term
  name: >-
    Wrapper (free or discount promotion)
  statement: >-
    A free or discount promotion is a wrapper placed around the unchanged core premium offer to make it more attractive to a cold audience.
  definition: >-
    free and discount are wrappers around the core premium offer we created … The point of creating a promotion is to enhance your Grand Slam Offer, not change it Think of these like wrapping paper
  not_to_confuse_with: >-
    Changing the offer itself — What’s inside may be the same, but we are making it more inherently attractive That is the reason for our promotional wrapper
  why: >-
    This is especially important when entering cold markets when you must give people a reason to move towards you It must answer the critical question—what’s in it for me
  anchor: >-
    wrappers around the core premium offer we created
  source: >-
    100m-series-lost-chapters.md, SECTION A: ATTRACT, line 560
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:560"
- id: E-lost-chapters-003
  type: term
  name: >-
    Premium offer (Premium Promotion)
  statement: >-
    A premium promotion presents the Grand Slam Offer on its own, with no free or discount wrapper, and asks the client to buy the thing most likely to produce their greatest outcome.
  definition: >-
    The goal of premium offers is to sell the client the best outcome available for themselves You ask the client to buy the thing that will most likely result in them achieving the greatest outcome
  not_to_confuse_with: >-
    A better or worse offer type — That being said, this is not “better” or “worse” than any of the other offer options It’s just different
  authors_caveat: >-
    But if you’re just starting out, or your volume isn’t high enough, or your cost of acquisition is higher than you can bear currently, then you will likely want to wrap your premium offer with a free or discount wrapper.
  anchor: >-
    The goal of premium offers is to sell the client the best outcome available for themselves
  source: >-
    100m-series-lost-chapters.md, Premium Promotions, line 660
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:660"
- id: E-lost-chapters-004
  type: term
  name: >-
    Free offer
  statement: >-
    A free offer is at bottom something for nothing, or value in advance, and is the offer that produces the highest lead volume at the lowest lead cost.
  definition: >-
    Free is the most powerful offer of all time and will never expire Why? At its base it is “something for nothing” or “value in advance”
  authors_caveat: >-
    That being said, I’m not saying free is for every offer, every time But, I am saying that if you learn how to harness it, there are some ways to layer “free” into a powerful money model.
  anchor: >-
    Free is the most powerful offer of all time and will never expire Why? At its base it
  source: >-
    100m-series-lost-chapters.md, Free Promotions, line 812
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:812"
- id: E-lost-chapters-005
  type: term
  name: >-
    Penny gap
  statement: >-
    The penny gap, from researcher Dr Dan Ariely, is the collapse in take-up as soon as a price stops being zero: 9x more people take a free item than the same item priced at a penny.
  definition: >-
    researcher Dr Dan Ariely demonstrated something he called the “penny gap” Basically, he showed that 9x more people would take a free Hershey kiss than one sold for a penny
  why: >-
    Imagine getting 9x more leads by lowering your discount from 01 to free That’s a big difference And we’re gonna harness it
  anchor: >-
    demonstrated something he called the “penny gap” Basically, he showed that 9x more people
  source: >-
    100m-series-lost-chapters.md, Free Promotions, line 814
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:814"
- id: E-lost-chapters-006
  type: term
  name: >-
    Friction
  statement: >-
    Friction is every hoop a prospect must go through before they can take the offer; it cuts lead volume and raises lead quality.
  definition: >-
    So we add friction Friction increases lead quality The more hoops someone has to go through the higher the quality becomes
  why: >-
    So the key with free is learning to find the sweet spot on friction to maximize quality volume.
  applies_when: >-
    For some businesses, free can attract “too many” prospects So we may need to add friction or make the offer less appealing.
  anchor: >-
    So we add friction Friction increases lead quality The more
  source: >-
    100m-series-lost-chapters.md, Free Promotions, line 937
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:937"
- id: E-lost-chapters-007
  type: term
  name: >-
    Massive discount
  statement: >-
    In this method a discount offer means 50% or more off, the size that drives action from a population that would not otherwise act.
  definition: >-
    Instead, we’re going to be talking about massive discounts (50% or more) Those are the types of numbers that people respond to And they drive action from a population that wouldn’t otherwise act.
  not_to_confuse_with: >-
    “marginal” discounts (say 5 to 25% off) — It’s just not enough to drive real behavior in my opinion, and basically just cuts into margin
  anchor: >-
    Instead, we’re going to be talking about massive discounts (50% or more) Those are
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, line 1087
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1087"
- id: E-lost-chapters-008
  type: term
  name: >-
    The Two-Step Sale
  statement: >-
    A two-step sale gives away something valuable that is not the core offer at an insane discount to get the lead and a card on file, then upsells the far more expensive core offer at a designated second appointment.
  definition: >-
    the whole point is we offer something valuable that’s not our core offer away for an insane discount with the intention of getting leads and getting a card over the phone to get the “thing” at a designated time The prospect then comes in at that designated time and is upsold something far more expensive after receiving the initial “thing”
  why: >-
    We can use this strategy as a part of a two-step sales process beautifully (which in my opinion is probably the primary reason I would use discounts).
  anchor: >-
    An example of a two-step sale would be us giving away a heavy metals test consultation
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, line 1299
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1299"
- id: E-lost-chapters-009
  type: term
  name: >-
    Proprietary 5 min Appointment Method
  statement: >-
    The Proprietary 5 min Appointment Method has the expensive practitioner drop in for five minutes between appointments to greet the prospect and set the in-depth appointment where the treatment plan is recommended and sold.
  definition: >-
    I call this strategy the Proprietary 5 min Appointment Method (feel free to swipe it) If desired, the doc can squeeze the person in between appointments for 5min just to say hello and set up the next in-depth appointment where a treatment plan would be recommended and sold
  why: >-
    Increasing the available time slots for appointments will improve the percentage of people who schedule more than just about anything else.
  anchor: >-
    I call this strategy the Proprietary 5 min Appointment Method (feel free to
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, line 1353
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1353"
- id: E-lost-chapters-010
  type: term
  name: >-
    Splinter (the offer)
  statement: >-
    To splinter an offer is to break it into tiny pieces and discount one core component of it instead of discounting the core offer itself.
  definition: >-
    That’s why we’re going to “splinter” our offer into tiny pieces and just give a core component at a discount—not the whole farm
  why: >-
    If we always discount our core offer, then people will become trained to buy only at discounted times No bueno.
  anchor: >-
    “splinter” our offer into tiny pieces and just give a core component at a discount—not the
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, line 1379
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1379"
- id: E-lost-chapters-011
  type: term
  name: >-
    Qualified lead (buyer of a discount front end)
  statement: >-
    Someone who buys the discounted front end counts as a qualified lead, not as a customer of the core service.
  definition: >-
    We shouldn’t see people as customers if they buy the discount We should see them as qualified leads
  not_to_confuse_with: >-
    Customers — most of the businesses that complained about Groupon-style buyers did not know how to structure their offers to automatically qualify prospects to become customers of their core service.
  anchor: >-
    We shouldn’t see people as customers if they buy the discount We should see
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, line 1395
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1395"
- id: E-lost-chapters-012
  type: term
  name: >-
    Information advantage
  statement: >-
    The information advantage is knowing your business, your product and your customers’ problems better than the customers do, which is what every business capitalizes on.
  definition: >-
    all businesses capitalize on an information advantage As in, we know more about our customers’ problems than they do
  why: >-
    We capitalize on this advantage by making them aware of all the other problems they are going to encounter on their journey, then capitalizing on that through upsells This is how you design a winning acquisition strategy.
  anchor: >-
    information advantage As in, we know more about our customers’ problems than they do
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Attract Section Conclusion: Brass Tacks, line 1430
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1430"
- id: E-lost-chapters-013
  type: term
  name: >-
    Customer Financed Acquisition (CFA)
  statement: >-
    CFA is the state where 30 days of gross profit from a customer exceeds the cost of acquiring that customer, so the customers themselves finance the next customers.
  definition: >-
    Customer Financed Acquisition (CFA) is when 30 days of GP (gross profit) from a customer is greater than the CAC—the Cost of Acquiring the Customer. In plain English, it solves your cash flow problems … 30 Day Gross Profit > CAC
  why: >-
    It costs money to get customers You wanna make the money you spent to get that customer back as profit in the first thirty days That way you can use that money again to get another customer.
  authors_caveat: >-
    And 2x is my “real life” minimum standard In practice, I want customers to more than just pay for themselves I want a 2x or more.
  anchor: >-
    Customer Financed Acquisition (CFA) is when 30 days of GP (gross profit) from a
  source: >-
    100m-series-lost-chapters.md, SECTION B: THE EXPENSIVE CUSTOMER PROBLEM, line 1461
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1461"
- id: E-lost-chapters-014
  type: term
  name: >-
    Gross Profit (GP)
  statement: >-
    Gross profit is what is left of what a customer pays after only the cost of making and delivering the thing they bought, and it is the money the business is then run on.
  definition: >-
    Gross Profit (GP): This is how much you make from a customer after factoring in the cost of giving them the thing they bought You find it by subtracting the price customers pay for your thing minus the cost of fulfillment
  not_to_confuse_with: >-
    Net Profit is money left over after subtracting all costs.
  why: >-
    Many entrepreneurs mix up Gross Profit and Net Profit.
  anchor: >-
    Gross Profit (GP): This is how much you make from a customer after factoring in the
  source: >-
    100m-series-lost-chapters.md, The Three Levers of CFA, line 1524
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1524"
- id: E-lost-chapters-015
  type: term
  name: >-
    Cost of Acquiring a Customer (CAC)
  statement: >-
    CAC is everything spent to get a new customer — advertising, the payroll of the media and sales people, software and commissions — divided by the customers acquired, tracked monthly and by channel.
  definition: >-
    Cost of Acquiring a Customer (CAC): The cost to get a new customer: advertising dollars, payroll to a media buyer, creative team, software, sales commissions and salaries, etc
  not_to_confuse_with: >-
    Ad spend per customer — most entrepreneurs report on how much ad spend it costs them to get a customer Or they think that their content leads are “free” Or, their outbound team they don’t consider, only the commissions.
  why: >-
    That $1,000 sale you thought cost you $200 to make, really costs $500 And as small of a difference as that may seem, in some businesses that can be the difference between $1,000,000 per month and $10,000,000 per month It’s that important Unlike LTGP, CAC is a hard science.
  anchor: >-
    Cost of Acquiring a Customer (CAC): The cost to get a new customer: advertising dollars,
  source: >-
    100m-series-lost-chapters.md, Cost To Acquire a Customer = CAC, line 1591
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1591"
- id: E-lost-chapters-016
  type: term
  name: >-
    Lifetime Gross Profit (LTGP)
  statement: >-
    LTGP is all the gross profit a business collects over the lifespan of a customer: total money from that customer minus everything it costs to deliver.
  definition: >-
    LTGP: The amount of gross profit a business collects over the lifespan of a customer In other words, how much total money you make from a customer minus everything it costs you to deliver it
  not_to_confuse_with: >-
    CAC — CAC is about getting customers LTGP is about keeping customers.
  why: >-
    LTGP is the arms race of business … you can only get CAC to zero, but LTGP can go infinitely high.
  anchor: >-
    LTGP: The amount of gross profit a business collects over the lifespan of a customer In other
  source: >-
    100m-series-lost-chapters.md, Lifetime Gross Profit (LTGP), line 1670
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1670"
- id: E-lost-chapters-017
  type: term
  name: >-
    Gross Margin
  statement: >-
    Gross margin is the same quantity as gross profit, expressed as a percentage of the total price charged instead of in dollars.
  definition: >-
    Also, Gross Margin is your gross profit expressed as a percentage of the total price you charge … Gross profit is expressed in an absolute dollar amount while gross margin is the same concept expressed as a percentage
  not_to_confuse_with: >-
    Gross profit — Gross margin and gross profit get used in a lot of similar situations Don’t let it confuse you It’s the same concept.
  anchor: >-
    Also, Gross Margin is your gross profit expressed as a percentage of the total price you
  source: >-
    100m-series-lost-chapters.md, Lifetime Gross Profit (LTGP), line 1698
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1698"
- id: E-lost-chapters-018
  type: term
  name: >-
    Churn
  statement: >-
    Churn is the percentage of the customers you started a period with who left by the end of it.
  definition: >-
    Churn is the percentage of customers that leave between time periods So, if on the first of last month we had 100 customers and this month, of those 100 customers, we lost five, our churn is 5%
  not_to_confuse_with: >-
    Net change in customer count — If you sign up new clients during this time period, it does not affect churn The same number of original people left.
  why: >-
    People get this twisted Don’t be one.
  anchor: >-
    to introduce a new concept—churn Churn is the percentage of customers that leave
  source: >-
    100m-series-lost-chapters.md, Lifetime Gross Profit (LTGP), line 1747
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1747"
- id: E-lost-chapters-019
  type: term
  name: >-
    Payback Period (PPD)
  statement: >-
    The payback period is how long it takes the gross profit from a new customer to exceed what was spent to acquire them, that is, when GP>CAC.
  definition: >-
    Payback Period: the time it takes to break even on what you spent to get a new customer
  why: >-
    Payback period is important because it will increase the speed of the cycles in which you can multiply your cash.
  anchor: >-
    Payback Period: the time it takes to break even on what you spent to get a new customer
  source: >-
    100m-series-lost-chapters.md, Payback Period = PPD, line 1804
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1804"
- id: E-lost-chapters-020
  type: term
  name: >-
    30 Day Cash (30D Cash)
  statement: >-
    30D Cash is the gross profit that can be extracted from a new customer within their first 30 days, and it is the metric compared against CAC.
  definition: >-
    30D Cash is the amount of gross profit I can extract from a new customer in their first 30 days
  why: >-
    The reason 30 days is so critical for small businesses is that 30 days is typically the amount of time any business can get interest-free financing—credit cards being a prime example If I can increase my 30D Cash above my CAC, then it means that I can get free customers using other people’s money.
  anchor: >-
    30D Cash is the amount of gross profit I can extract from a new customer in their first 30
  source: >-
    100m-series-lost-chapters.md, Payback Period = PPD, Alex’s Most Prized Metric: 30 Day Cash (30D Cash), line 1909
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1909"
- id: E-lost-chapters-021
  type: term
  name: >-
    Offer stacking (“the back end”)
  statement: >-
    Offer stacking is layering Grand Slam Offers one after another to raise what a client is worth; that accumulated lifetime value is what the author calls the back end.
  definition: >-
    I will show you how to layer or “stack” Grand Slam Offers on top of one another to create higher lifetime value, aka “the back end” So this is making a series of Grand Slam Offers in a row in order to increase how much a client is worth to the business
  why: >-
    The back end informs the front end That means the more money you make per customer, the more you can spend to acquire customers.
  anchor: >-
    higher lifetime value, aka “the back end” So this is making a series of Grand Slam Offers in
  source: >-
    100m-series-lost-chapters.md, SECTION C: ADVANCED OFFER STACKING, line 2272
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:2272"
- id: E-lost-chapters-022
  type: term
  name: >-
    The Value Grid
  statement: >-
    The value grid lays every offer against every prospect so the numbers become visible: total revenue from the grid divided by the people who came in gives lifetime value and 30D Cash.
  definition: >-
    The second reason I like the grid is that it makes the numbers visual You can actually visualize all your prospects And when you add up all the revenue from all the clients in the grid, and divide it by how many people came in, you know your lifetime value
  not_to_confuse_with: >-
    The value ladder or stair step — with a stair step, the visual depiction makes your brain think that all customers must buy the first in order to buy the second It depicts the relationship as linear This has not been my experience.
  anchor: >-
    The second reason I like the grid is that it makes the numbers visual You can actually
  source: >-
    100m-series-lost-chapters.md, Back End: The value Grid, line 2354
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2354"
- id: E-lost-chapters-023
  type: term
  name: >-
    Free With Alternate Revenue Stream
  statement: >-
    Free With Alternate Revenue Stream gives one type of service or product away free and monetizes a different revenue stream on top of it.
  definition: >-
    In the simplest terms, we are providing one type of service (or product) for free, and upselling something else
  anchor: >-
    offer I call “Free With Alternate Revenue Stream” I break it down in depth a few chapters
  source: >-
    100m-series-lost-chapters.md, Back End: The value Grid, line 2404
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:2404"
- id: E-lost-chapters-024
  type: term
  name: >-
    Affiliate relationship
  statement: >-
    An affiliate relationship is one where another business owner pays you for sending them customers.
  definition: >-
    affiliate relationships (a relationship where another business owner pays you to send them customers)
  anchor: >-
    Then see if I can create affiliate relationships (a relationship where another business
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, line 2448
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2448"
- id: E-lost-chapters-025
  type: term
  name: >-
    Money Model
  statement: >-
    A money model is a series of offers where each offer, or series of offers, satisfies one stage: lower CAC, maximize 30-Day GP, then maximize lifetime GP.
  definition: >-
    Money models are built off a series of offers Each offer—or series of offers—satisfies a stage of your Money Models We lower CAC We maximize 30-Day GP Then, we maximize lifetime GP
  anchor: >-
    Money models are built off a series of offers Each offer—or series of offers—satisfies a
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, line 2642
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2642"
- id: E-lost-chapters-026
  type: term
  name: >-
    Attraction Offer
  statement: >-
    An Attraction Offer is the offer used at the money-model stage whose goal is getting new customers at a reasonable price.
  definition: >-
    If I want to get new customers at a reasonable price, I focus on Attraction Offers If I want to increase 30-Day GP, I add upsells and downsell offers
  anchor: >-
    get new customers at a reasonable price, I focus on Attraction Offers If I want to increase
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, line 2653
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2653"
- id: E-lost-chapters-027
  type: term
  name: >-
    Free presentation (education with offer)
  statement: >-
    A presentation is an attraction offer that educates an audience with the intention of converting them, bridging the information gap before the offer is made.
  definition: >-
    Presentations that educate the audience with the intention of converting them into customers excel at bridging this information gap … Presentations can last anywhere from 15 seconds to 15 days
  why: >-
    The amount of time you take educating the consumer is directly related to the price and the amount of trust needed.
  anchor: >-
    Presentations can last anywhere from 15 seconds to 15 days The exact length of the
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, line 2734
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2734"
- id: E-lost-chapters-028
  type: term
  name: >-
    Freemium
  statement: >-
    Freemium gives away a core product valuable enough that people come for it and keep using it for free, so a sales team can upsell that pool of free users.
  definition: >-
    The idea is, you give something away that is so valuable that people come to get it and continually use it for free They must come from word of mouth because the product is so good It must cost $0 to get them to use it
  not_to_confuse_with: >-
    A business model — one of the key points to understand about freemium is that it is not a business model, it is an acquisition strategy That’s a very important distinction.
  authors_caveat: >-
    If you do not have investors and large amounts of capital, I would not recommend this structure … Otherwise, steer clear.
  anchor: >-
    It’s important to remember that this isn’t a business model It’s an acquisition strategy
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Freemium, line 3041
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3041"
- id: E-lost-chapters-029
  type: term
  name: >-
    Free Pick Your Price
  statement: >-
    Free Pick Your Price markets the offer as free and, at checkout, invites the person to choose their own price, with bonuses attached to three levels of payment.
  definition: >-
    You market the promotional offer as free When the person gets to the checkout, you give them an offer to pick their own price You will explain the benefits of investing more equating to higher investment in their own results
  not_to_confuse_with: >-
    A limited free offer — This is similar to a limited free offer except instead of “either or,” you have a sliding scale with no predetermined amounts, only rungs It also has no max.
  authors_caveat: >-
    This offer does not work with a discount wrapper.
  anchor: >-
    You market the promotional offer as free When the person gets to the checkout, you
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Pick Your Price, line 3086
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3086"
- id: E-lost-chapters-030
  type: term
  name: >-
    The no sale sale
  statement: >-
    The no sale sale is monetizing the prospect who said no to the main offer by handing them something free and booking them into an orientation where a different product is sold.
  definition: >-
    Everyone around here calls it “the no sale sale” Perfect name, right? I’m selling to people who think they aren’t buying anything
  why: >-
    Almost 100% of the people who said no to my gym membership end up in these nutrition orientations And guess what? During these orientations, we sell them supplements instead of workout programs.
  anchor: >-
    Everyone around here calls it “the no sale sale” Perfect name, right? I’m selling to people
  source: >-
    100m-series-lost-chapters.md, Upsell Offer: Free With Alternate Revenue Stream, line 3229 (the author names it a rough paraphrasing of a gym owner’s story, line 3205)
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3229"
- id: E-lost-chapters-031
  type: term
  name: >-
    Paired Upsell
  statement: >-
    A paired upsell gives thing A for free in exchange for the customer buying thing B.
  definition: >-
    Paired Upsell: I give you thing A for free, in exchange for buying thing B
  anchor: >-
    Paired Upsell: I give you thing A for free, in exchange for buying thing B
  source: >-
    100m-series-lost-chapters.md, Upsell Offer: Free With Alternate Revenue Stream, line 3255
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3255"
- id: E-lost-chapters-032
  type: term
  name: >-
    Independent Upsell
  statement: >-
    An independent upsell gives thing A for free and then encourages, but does not require, the purchase of thing B.
  definition: >-
    Independent Upsell: I give you thing A for free, and I will encourage you to buy thing B
  not_to_confuse_with: >-
    Paired Upsell — where the free thing is given in exchange for buying thing B.
  anchor: >-
    Independent Upsell: I give you thing A for free, and I will encourage you to buy
  source: >-
    100m-series-lost-chapters.md, Upsell Offer: Free With Alternate Revenue Stream, line 3259
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3259"
- id: E-lost-chapters-033
  type: term
  name: >-
    One-time bonus
  statement: >-
    A one-time bonus is given once — one thing, one use, one activity or one-time access — and extends a customer’s tenure once.
  definition: >-
    A one-time bonus, you give one time. Think of one thing, one use, one activity, or one-time access
  why: >-
    One-time bonuses happen once and extend the duration of a customer’s tenure once So, you may need to give lots of one-time bonuses over time to keep them staying…over time.
  anchor: >-
    A one-time bonus, you give one time. Think of one thing, one use, one activity, or one-time
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, line 3488
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3488"
- id: E-lost-chapters-034
  type: term
  name: >-
    Variable bonus
  statement: >-
    A variable bonus is given on a schedule but is a different thing each time.
  definition: >-
    A variable bonus, you give on a schedule, but it changes each time
  why: >-
    No matter how good you make your thing, customers will get used to it So giving new stuff more often (even if less valuable) frequently keeps more customers interested longer.
  anchor: >-
    A variable bonus, you give on a schedule, but it changes each time And a lifetime
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, line 3489
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3489"
- id: E-lost-chapters-035
  type: term
  name: >-
    Continuity offer
  statement: >-
    A continuity offer is the recurring offer used to maximize lifetime gross profit, and it can be built on anything that provides continuous value.
  definition: >-
    All in all, you can probably make a continuity offer on anything that provides continuous value You can get them to stick to that continuity offer longer by adding bonus value well after their first payment, and often
  applies_when: >-
    If I need to maximize lifetime GP, I focus on Continuity Offers.
  anchor: >-
    All in all, you can probably make a continuity offer on anything that provides continuous
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, line 3504
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3504"
- id: E-lost-chapters-036
  type: term
  name: >-
    Delayed bonus
  statement: >-
    A delayed bonus is one whose “when” is a wait: it is given after a specified number of payments or amount of time has passed.
  definition: >-
    Delayed bonuses you give after a specified number of payments or time has passed
  anchor: >-
    Delayed bonuses you give after a specified number of payments or time has passed
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, line 3609
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3609"
- id: E-lost-chapters-037
  type: term
  name: >-
    Milestone bonus
  statement: >-
    A milestone bonus is one whose “when” is an action: it is given after the customer does something or achieves a result.
  definition: >-
    Milestone bonuses you give after the customer does something or achieves a result
  why: >-
    I try to make all my milestones either: things that make my customer more successful—think activation points Or, things that make me successful—advertising on my behalf Ideally, things that do both.
  anchor: >-
    Milestone bonuses you give after the customer does something or achieves a result
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, line 3610
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3610"
- id: E-lost-chapters-038
  type: term
  name: >-
    Lifetime upgrade
  statement: >-
    A lifetime upgrade is a permanent high-value change in continuity status — an entire additional feature or service kept for as long as the customer stays.
  definition: >-
    a lifetime upgrade means a permanent high-value change in continuity status—think an entire feature or service
  authors_caveat: >-
    Unless your bonus gives a huge and permanent improvement, keep it variable.
  anchor: >-
    Lifetime upgrade bonuses give additional features or services
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, line 3616
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3616"
- id: E-lost-chapters-039
  type: term
  name: >-
    Lifetime Discount
  statement: >-
    A Lifetime Discount gives a customer a cheaper price for as long as they stay on recurring payments, and they stick because leaving means they cannot get it back.
  definition: >-
    Lifetime Discount offers, at least the way I use them, give customers a cheaper price as long as they stay on recurring payments. Customers get incentivized to take the offer now because they get value at a discount now
  authors_caveat: >-
    A Lifetime Discount only works if you actually charge more when this offer ends Otherwise you just list the price and “pretend” it’s a discount Gross.
  anchor: >-
    Lifetime Discount offers, at least the way I use them, give customers a cheaper price
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, line 3659
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3659"
- id: E-lost-chapters-040
  type: term
  name: >-
    Rollover Upsell
  statement: >-
    A Rollover Upsell is a lifetime discount used as an upsell: the customer keeps the discounted rate only if they finish out the credited payments.
  definition: >-
    I let people keep a “Rollover Upsell” discount only if they finish out the credited payments This gets them to buy and gets them to stick Think of it like “price protection” where you keep it so long as you keep paying for it
  not_to_confuse_with: >-
    Lifetime Discounts used as an attraction offer — The Opener used Lifetime Discounts as an attraction offer I prefer to use them as upsells.
  anchor: >-
    I let people keep a “Rollover Upsell” discount only if they finish out the credited payments
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, line 3682
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3682"
- id: E-lost-chapters-041
  type: term
  name: >-
    The Bigger The Head, The Longer The Tail
  statement: >-
    The bigger the head, the longer the tail names the effect of initiation fees: the more a customer commits up front, the longer they stay.
  definition: >-
    the thought that the bigger the head, the longer the tail came to my mind … That’s when I learned the power of initiation fees for continuity
  why: >-
    The more you can get people to commit up front the longer they’ll stick (John, the tanning empire king, on initiation fees).
  anchor: >-
    Being a little slow on the uptake, the thought that the bigger the head, the longer the tail
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, The Bigger The Head, The Longer The Tail, line 3841
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3841"
- id: E-lost-chapters-042
  type: term
  name: >-
    Discount + One-Time Fee
  statement: >-
    Discount + One-Time Fee charges a discounted rate for the first term of service plus one or more made-up fees that can each be charged, discounted or waived.
  definition: >-
    You charge a discounted rate for your first term or period of service You then charge one or more additional fees that you have “made up,” just like the Free with Fee structure You can waive some and charge others, waive them all, or charge them all
  why: >-
    This offer will tend to surprise fewer people since they already came in expecting to pay something, which is one of the key benefits of using Discounts over Free.
  anchor: >-
    You charge a discounted rate for your first term or period of service You then charge one
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Discount + One-Time Fee, line 3942
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3942"
- id: E-lost-chapters-043
  type: term
  name: >-
    Rich versus wealthy
  statement: >-
    Being rich comes from what the business pays you; being wealthy comes from owning a business that runs without you and is therefore worth something to someone else.
  definition: >-
    You get rich from what you make. You become wealthy from what you own.
  not_to_confuse_with: >-
    A business that only makes money with you in it — If the business only makes money with you in it, then it’s a bad investment for anyone else.
  anchor: >-
    You get rich from what you make. You become wealthy from what you own. And it took me
  source: >-
    100m-series-lost-chapters.md, SECTION D: EXPANDED EMPLOYEES CHAPTER, Why Employees Make You Wealthy, line 4132
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4132"
- id: E-lost-chapters-044
  type: term
  name: >-
    Daily huddles
  statement: >-
    Daily huddles are short group meetings of a few minutes held at the start of each shift to set expectations and goals and at the end of each shift to report on them.
  definition: >-
    The other times are short group meetings that only last a few minutes. We call them “daily huddles”—and all my lead-getting employees have them We have one at the beginning of each shift to discuss expectations and goals Then, we have one at the end of each shift so they can report on them
  why: >-
    This creates faster feedback cycles for building skills and morale.
  anchor: >-
    “daily huddles”—and all my lead-getting employees have them We have one at the beginning
  source: >-
    100m-series-lost-chapters.md, SECTION D: EXPANDED EMPLOYEES CHAPTER, Keep Your Employees Getting You Leads—The Performance Diamond, line 4339
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4339"
- id: E-lost-chapters-045
  type: term
  name: >-
    The Best Diamond Hard Feedback Question
  statement: >-
    The Diamond Hard Feedback Question is the line, taken from Leila, used in a weekly one-on-one when performance has been dropping for a week or two.
  definition: >-
    “Over the last (length of time) your (task performance) has changed from the norm. What do you think has gotten in the way and how can I help?”
  why: >-
    This question sets the stage for a collaborative problem-solving conversation rather than a character-blaming one.
  applies_when: >-
    If an employee’s performance has been dropping for a little while (a week or two).
  anchor: >-
    “Over the last (length of time) your (task performance) has changed from the norm.
  source: >-
    100m-series-lost-chapters.md, SECTION D: EXPANDED EMPLOYEES CHAPTER, Pro Tip: The Best Diamond Hard Feedback Question, line 4445 (attributed to Leila, line 4441)
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4445"
- id: E-lost-chapters-046
  type: term
  name: >-
    The Performance Diamond
  statement: >-
    The performance diamond is the author’s diagnostic for a drop in employee performance across four reasons: Communication, Training, Motivation and Circumstances.
  definition: >-
    This is the performance diamond I use for diagnosing performance problems … there are four reasons employee performance drops: Communication—Employees don’t know THAT we want them to do it; Training—Employees don’t know HOW to do it; Motivation—Employees don’t WANT to do it; Circumstances—Something is stopping them
  why: >-
    If I approach performance with that perspective it goes a long way to figuring out whether it’s truly the employee’s problem or, more often, something I messed up along the way.
  anchor: >-
    This is the performance diamond I use for diagnosing performance problems If I
  source: >-
    100m-series-lost-chapters.md, SECTION D: EXPANDED EMPLOYEES CHAPTER, Keep Your Employees Getting You Leads—The Performance Diamond, line 4466
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:4466"
- id: E-lost-chapters-047
  type: term
  name: >-
    Cost per engaged lead
  statement: >-
    Cost per engaged lead is total payroll of the lead-getting employees divided by the total engaged leads they produce, excluding paid-ad spend.
  definition: >-
    Total Payroll / Total Engaged Leads = Cost per engaged lead … Ex: $100,000 / 1,000 leads = $100 per engaged lead
  why: >-
    Excluding the cost of running paid ads, the cost of advertising (outreach, content, etc ) with employees is almost entirely based on the amount of money you pay them to do it.
  anchor: >-
    Total Payroll / Total Engaged Leads = Cost per engaged lead
  source: >-
    100m-series-lost-chapters.md, SECTION D: EXPANDED EMPLOYEES CHAPTER, How to Calculate Returns From Lead-Getting Employees, line 4482
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4482"
- id: E-lost-chapters-048
  type: term
  name: >-
    Advertising problem versus sales problem
  statement: >-
    An advertising problem means the engaged leads are not qualified or there are too few of them; a sales problem means the leads are qualified but not buying.
  definition: >-
    Do my engaged leads have the problem I solve and the money to spend? If no, then they’re not qualified—that’s an advertising problem … They’re buying but you don’t have enough of them—advertising problem … They’re qualified but not buying—sales problem
  not_to_confuse_with: >-
    Each other — Don’t fire your sales guy if you’ve got advertising problems And equally, don’t fire your advertising employees if you’ve got a sales problem.
  applies_when: >-
    If your CAC is more than 3x industry average then you have a sales problem or an advertising problem.
  anchor: >-
    Do my engaged leads have the problem I solve and the money to spend?
  source: >-
    100m-series-lost-chapters.md, SECTION D: EXPANDED EMPLOYEES CHAPTER, How To Know Which Employees To Focus On To Maximize Returns, line 4507
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4507"
```
