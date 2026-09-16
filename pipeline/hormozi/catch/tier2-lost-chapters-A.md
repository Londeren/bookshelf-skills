# Улов фазы 1 — $100M Series: Lost Chapters (2025) with $100M Leads: 2 Bonus Chapters (2023) as a second copy of Section A (ярус 2), тип A: фреймворки

Группа `tier2-lost-chapters`, слаг `lost-chapters`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **41** (экстрактор вернул 41, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-series-lost-chapters.md` | 1–4810 | 6 | 40 |
| `100m-leads-bonus-chapters.md` | 1–568 | 1 | 1 |

## Как собран файл

Экстрактор A (Frameworks) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-lost-chapters.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-lost-chapters-A.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: A-lost-chapters-001
  type: framework
  name: >-
    The process Vista used to grow companies
  statement: >-
    Score a business's current customers by how long they stay and how much they pay, then cut the channels that brought in the low-value customers and double down on the channels that brought in the best ones.
  why: >-
    It is Pareto's principle on steroids: 20% of customers bring in 80% of revenue, so replacing the other 80% with high spenders grows the business 5x.
  structure:
    - >-
      They analyze the company's current customers
    - >-
      They look for the customers who stay the longest and pay the most
    - >-
      Then, they score them according to this value
    - >-
      Cut channels that brought the low-value customers
    - >-
      Then, they double down on the channels that brought in the best ones
  applies_when: >-
    Deciding which customers a business should keep serving and which acquisition channels to keep paying for.
  anchor: >-
    Once they buy a company, they’d cut channels that brought the low-value customers
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, lines 213–230
  confirmations: 1
  authors_caveat: >-
    The author presents this as the method a Vista speaker broke down from the stage, which he then adapted; he says only that it became a pillar of our value acceleration method (VAM) at acquisition com and never lays out VAM itself. The steps are taken from his retelling, not from a list he published.
  anchor_at: "100m-series-lost-chapters.md:220"
- id: A-lost-chapters-002
  type: framework
  name: >-
    Your First Avatar — four steps
  statement: >-
    To pick the avatar, survey your customers, sort for the biggest spenders and keep the top 20%, find the fewest qualifiers they all share, then execute by speaking to that avatar in all advertising and re-engineering the sales process the best customers went through.
  why: >-
    Growing a business comes down to selling more customers or making them worth more, and this process accomplishes both: marketing gets more tailored, and the clients you do sell are the highest-value people.
  structure:
    - >-
      1) Survey your customers: Set up a form with the questions below and send it out
    - >-
      2) Find your biggest spenders: Sort the replies by the customers you like the most, spent the most, and stayed the longest Focus on the top 20% Ignore the rest
    - >-
      3) See what they have in common: Come up with the fewest qualifiers they all have in common Usually there are three to five qualifiers
    - >-
      4a) Speak your new avatar. Be up front about your customer requirements Get all advertising to speak directly to them
    - >-
      4b) Re-engineer the sales process. Reverse-engineer the buying process your best customers went through
  applies_when: >-
    Choosing exactly who you serve and who you do not — a subset of the larger decision of picking the right market.
  anchor: >-
    There are four steps to installing this process I outline them below Then, I share what
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, lines 238–296
  confirmations: 2
  authors_caveat: >-
    The process is not a beginner concept; with no customers yet, start with the industry you know most about, create a narrow target and run the customer analysis again once you have customers to survey.
  anchor_at: "100m-series-lost-chapters.md:238"
- id: A-lost-chapters-003
  type: framework
  name: >-
    The four categories of avatar survey questions
  statement: >-
    The customer survey asks in four blocks: demographics, business stats before and current, aspirations, and buying process.
  why: >-
    The answers are what let you see what your most successful customers have in common and what caused them to buy, so you can repel the bad customers and reverse-engineer the buying process on purpose.
  structure:
    - >-
      a) Demographics: Who are they? Age? Gender? Political affiliation? Geographic location? Digital Location? Single/Divorced? Partnered in business or solopreneur?
    - >-
      b) Business Stats Before & Current: Revenue? Profit? # of employees? Churn? Pricing? Products? Customer lifetime value? # of customers? Niche? How long in business?
    - >-
      c) Aspirations: What was their goal upon purchasing your services/products? What problem were they trying to solve?
    - >-
      d) Buying Process: What’s the single biggest reason they bought? Was there a trigger event that caused them to buy? Did they consume any specific piece of content? Where did they first see us? Did someone refer them?
  applies_when: >-
    Step one of Your First Avatar, running the survey; the example given is for business services customers.
  anchor: >-
    you’d want to know Here’s an example of questions I would ask business services
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, lines 245–269
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:245"
- id: A-lost-chapters-004
  type: framework
  name: >-
    Get Flow. Monetize Flow. Then Add Friction.
  statement: >-
    Generate demand first, then monetize it, and only then increase friction — in that order.
  why: >-
    Understanding how to promote the offer is core to getting initial traction and the first leads; from there you can add friction and monetize more aggressively. Too many people put the cart before the horse.
  structure:
    - >-
      Generate Flow
    - >-
      Monetize Flow
    - >-
      Increase Friction
  applies_when: >-
    Entering a new market or adding an acquisition channel, whether it is your first or an additional one.
  anchor: >-
    Always remember - Generate Flow-->Monetize Flow-->Increase Friction. In that order. As I said in
  source: >-
    100m-leads-bonus-chapters.md, Attract Section Conclusion: Brass Tacks, line 561 = Lost Chapters line 1424
  confirmations: 2
  anchor_at: "100m-leads-bonus-chapters.md:561"
- id: A-lost-chapters-005
  type: framework
  name: >-
    Premium, Free, and Discount offers
  statement: >-
    Every promotion is one of three types — a standalone premium offer, a free offer, or a discount offer — and free and discount are wrappers around the core premium offer rather than a different offer.
  why: >-
    The point of a promotion is to enhance your Grand Slam Offer, not change it: the wrapper makes the same thing more inherently attractive to a cold audience that needs a reason to move towards you.
  structure:
    - >-
      Premium — presenting your Grand Slam Offer on its own
    - >-
      Free
    - >-
      Discount
  applies_when: >-
    Choosing how to present the core offer when you must generate demand flow, especially in cold markets.
  anchor: >-
    Over the next three chapters we will break down Premium, Free, and Discount offers in
  source: >-
    100m-series-lost-chapters.md, Section A: Attract, lines 557–578
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:576"
- id: A-lost-chapters-006
  type: framework
  name: >-
    Pros and cons of Premium Offers
  statement: >-
    A premium offer buys three advantages — simplest math, only quality customers, no discounts needed — at the price of five costs: the most expensive leads, a demand for copywriting and avatar knowledge, a demand for sales skill, the least efficient way to capture a marketplace, and the need for an extremely compelling offer.
  why: >-
    The goal of premium offers is to sell the client the best outcome available for themselves; it is not better or worse than the other offer options, it is just different, so the choice is made on these tradeoffs.
  structure:
    - >-
      Pro #1 Simplest Math & Fewest Moving Parts
    - >-
      Pro #2 Only “Quality” Customers: Decreases Operational Drag
    - >-
      Pro #3 No Discounts or Incentives: High Lead Quality
    - >-
      Con #1 Most Expensive Cost Per Lead/Can Take More Time To Break Even
    - >-
      Con #2 Must Be a Good Copywriter and Understand Your Avatar Well
    - >-
      Con #3 Must Be Good at Sales Because This Is a Good Old Fashioned Sale
    - >-
      Con #4 Least Efficient Way to Capture a Marketplace
    - >-
      Con #5 Must Have an Extremely Compelling Offer of a Result
  applies_when: >-
    Deciding whether to lead with a premium offer on its own or wrap it in a free or discount front end.
  anchor: >-
    teach me the pros and cons of a premium offer as though we were working together Thanks
  source: >-
    100m-series-lost-chapters.md, Premium Promotions, lines 664–797
  confirmations: 1
  authors_caveat: >-
    If the author had to make a business owner money from scratch he would not start with a premium offer; start with free or discount, prove results, then restructure to premium afterwards.
  anchor_at: "100m-series-lost-chapters.md:665"
- id: A-lost-chapters-007
  type: framework
  name: >-
    The three reasons a free offer does not work
  statement: >-
    When a free offer fails, the prospects either do not want the thing, do not believe you, or are not seeing it because you are fishing in the wrong pond.
  why: >-
    A free offer is the fastest way to see if anyone wants your thing, so its failure is a diagnostic: each of the three reasons points at a different fix — change what you give away or how you describe it, give a believable reason why, or fix targeting.
  structure:
    - >-
      1) Don’t want your thing—which means you should change what you are giving away for free (or how you describe it)
    - >-
      2) Don’t believe you
    - >-
      3) Aren’t actually seeing it because you are fishing in the wrong pond This can be a targeting issue
  applies_when: >-
    A free offer is running and not converting.
  anchor: >-
    fastest way to see if anyone wants your thing Because if your free offer doesn’t work, it just
  source: >-
    100m-series-lost-chapters.md, Free Promotions, lines 817–849
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:819"
- id: A-lost-chapters-008
  type: framework
  name: >-
    Pros and cons of Free Offers
  statement: >-
    Free buys the highest lead volume, the lowest lead cost, and the viral monetization model of the biggest companies, at the price of volume being a double-edged sword operationally and of some people having no intention of buying.
  why: >-
    Free gets the most leads per eyeball, which matters most in a small marketplace where there are only X eyeballs; the downsides are both handled with friction and offer design rather than by abandoning free.
  structure:
    - >-
      Pro #1 Highest Lead Volume
    - >-
      Pro #2 Lowest Lead Cost
    - >-
      Pro #3 Massive Companies Become Massive & Viral By Learning To Monetize “Free”
    - >-
      Con #1 Volume Can Be A Double-Edged Sword
    - >-
      Con #2 Some People Have No Intention of Buying
  applies_when: >-
    Choosing the front-end wrapper, especially in a small or local market.
  anchor: >-
    Now, let’s break down some of the pros and cons of free offers We’re gonna flip the
  source: >-
    100m-series-lost-chapters.md, Free Promotions, lines 851–1002
  confirmations: 1
  authors_caveat: >-
    The author is not saying free is for every offer, every time.
  anchor_at: "100m-series-lost-chapters.md:851"
- id: A-lost-chapters-009
  type: framework
  name: >-
    Examples of Friction
  statement: >-
    Five kinds of friction raise lead quality at the cost of volume: increased qualifications, increased information requirement and types of questions, increased number of steps, forced consumption, and advertisement length.
  why: >-
    Friction increases lead quality — the more hoops someone has to go through the higher the quality becomes — so the key with free is finding the sweet spot on friction that maximizes quality volume.
  structure:
    - >-
      1) Increased Qualifications
    - >-
      2) Increased Information Requirement & Types of Questions
    - >-
      3) Increased Number of Steps
    - >-
      4) Forced Consumption
    - >-
      5) Advertisement Length
  applies_when: >-
    A free offer attracts too many prospects, or the business cannot handle the volume operationally.
  anchor: >-
    per day, it could be a problem So we add friction Friction increases lead quality The more
  source: >-
    100m-series-lost-chapters.md, Free Promotions, Cons #1, lines 933–990
  confirmations: 1
  authors_caveat: >-
    You want just enough to weed out the weirdos but not so much that you lose some lazy whales; forced consumption is only a good strategy when you advertise to a large audience and eyeballs are cheap.
  anchor_at: "100m-series-lost-chapters.md:937"
- id: A-lost-chapters-010
  type: framework
  name: >-
    Four Ways To Display Discounts
  statement: >-
    The same discount can be displayed four ways — percentage off, absolute amount off, relative equivalent off (said in the negative or the positive), or simply the discounted price — and you cycle through all four to test which resonates.
  why: >-
    People will respond differently to the same discount displayed differently, so cycling through all four shows which one fits; and if you find multiple winners it gives you more bullets in the chamber when a promotion fatigues.
  structure:
    - >-
      1) Percentage Off — “New Client Special,” 87% off first visit
    - >-
      2) Absolute Amounts Off — “$181 Off First Week” (Normally $210)
    - >-
      3) Relative Equivalent Off — “Save A Steak Dinner,” said in negative, or “Less Than Going Out To Lunch,” said in positive
    - >-
      4) Simply the Discounted Price — $29 New Client Special
  applies_when: >-
    Testing how to present a discount offer; the price of the offer many times informs which display makes the most sense.
  anchor: >-
    “You see, there are four ways you can display a discount Knowing them is important
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Four Ways To Display Discounts, lines 1098–1154
  confirmations: 1
  authors_caveat: >-
    For the discounted price to be effective the service usually has to be one that is well understood and whose cost people already have an idea of; otherwise state the price first, then the discount.
  anchor_at: "100m-series-lost-chapters.md:1105"
- id: A-lost-chapters-011
  type: framework
  name: >-
    Pros and cons of Discount Offers
  statement: >-
    A discount buys cheap leads within the law, some money collected up front, prospects who expect to spend, the two-step sale, and smooth upsells off a card on file, at the price of training customers to buy only at a discount and of attracting bargain hoppers.
  why: >-
    There are benefits that discounts get that free offers don't provide — you must match the right tool for the job — and the two-step sale is, in the author's opinion, probably the primary reason he would use discounts.
  structure:
    - >-
      Pro #1 Lots of Cheap Leads Within the Law
    - >-
      Pro #2 You Actually Collect Some Money
    - >-
      Pro #3 People Come in Expecting to Spend Some Sort of Money
    - >-
      Pro #4 The Two-Step Sale (Probably the Biggest Benefit)
    - >-
      Pro #5 Discount Offers Make Upsells Smooth As Buttaaa
    - >-
      Con #1 Giving Away The Farm
    - >-
      Con #2 Bargain Hoppers
  applies_when: >-
    Choosing a discount over a free front end — in a heavily regulated industry, state or country, or where no-shows cost real time such as a doctor's.
  anchor: >-
    Just like before, we’re gonna flip roles and have you explain the pros and cons of discounts
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, lines 1174–1403
  confirmations: 1
  authors_caveat: >-
    Pro #3 is more of a mental benefit than anything: a good salesman will sell the same % of free vs non-free leads; the author has tested it four separate times.
  anchor_at: "100m-series-lost-chapters.md:1174"
- id: A-lost-chapters-012
  type: framework
  name: >-
    The Three Levers of CFA
  statement: >-
    Customer Financed Acquisition is worked with three levers: lower the cost of acquiring customers, increase lifetime gross profit, and decrease the payback period.
  why: >-
    To grow a business you get more customers or make them worth more; the author adds speed as the third variable, because a customer who pays for themselves today lets you get another one tomorrow instead of in thirty days.
  structure:
    - >-
      1) Get More Customers→Lower The Cost of Acquiring Customers (↓CAC)
    - >-
      2) Make Them Worth More→Increase Lifetime Gross Profit (↑LTGP)
    - >-
      3) Do It Fast→Decrease Payback Period (↓PPD)
  applies_when: >-
    Making Customer Financed Acquisition work — getting 30 day gross profit above CAC, and ideally above 2x CAC.
  anchor: >-
    customers, make them worth more, and do it fast And those three elements create the three
  source: >-
    100m-series-lost-chapters.md, The Three Levers of CFA, lines 1485–1556
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1490"
- id: A-lost-chapters-013
  type: framework
  name: >-
    The three steps to calculating LTGP
  statement: >-
    Lifetime gross profit is built in three steps: figure your gross profit, figure the average number of transactions over a customer's lifetime (or your churn), then multiply gross profit by transactions for a products business or divide gross profit by churn for a recurring one.
  why: >-
    LTGP is easy to understand but hard to figure out without a CRM, and data tracking is often a mess even with one, so these back-of-napkin steps let you get the number anyway.
  structure:
    - >-
      LTGP Step One: Gross Profit
    - >-
      LTGP Step Two: Figure the average number of transactions a customer makes over their lifetime
    - >-
      LTGP Step Three: If you have a physical products business, multiply average gross profit by # of transactions Or, if you have a recurring business, divide gross profit by churn percentage
  applies_when: >-
    Working the second lever of CFA — knowing how much a customer is worth so you know how much you can spend to get one.
  anchor: >-
    figured out, all we have to do is put steps one and two together to get our lifetime gross profit
  source: >-
    100m-series-lost-chapters.md, Lifetime Gross Profit (LTGP), lines 1679–1783
  confirmations: 1
  authors_caveat: >-
    Gross profit is not net profit: it is what is left over on the core thing you sell, before the rest of your expenses.
  anchor_at: "100m-series-lost-chapters.md:1773"
- id: A-lost-chapters-014
  type: framework
  name: >-
    Two back-of-napkin ways to estimate lifetime transactions
  statement: >-
    Estimate the average number of transactions either by exporting lifetime customer data, sorting by number of transactions and averaging that column, or — for a recurring revenue business — by computing churn as the customers who left divided by the original amount.
  why: >-
    CRMs often do not report this, and even when they do they are often wrong because data tracking can be a mess, so it is good to know how to do the money math yourself.
  structure:
    - >-
      1) Export your lifetime customer data Sort by number of transactions Average out that column
    - >-
      2) If you have a recurring revenue business, you figure it out differently — churn, the percentage of customers that leave between time periods
  applies_when: >-
    Step two of the LTGP calculation.
  anchor: >-
    So it’s good to understand how to do this money math I’m gonna give you a few “back of
  source: >-
    100m-series-lost-chapters.md, Lifetime Gross Profit (LTGP), lines 1725–1771
  confirmations: 1
  authors_caveat: >-
    Figuring out how many transactions a customer makes on average is always an estimate, and lifetime transactions always increase as a business gets older; new clients signed during the period do not affect churn.
  anchor_at: "100m-series-lost-chapters.md:1729"
- id: A-lost-chapters-015
  type: framework
  name: >-
    Levels of Customer Financed Acquisition
  statement: >-
    There are three levels of CFA by what the first thirty days of gross profit from a customer cover: less than CAC (level 1), the same as CAC (level 2), or more than double CAC (level 3).
  why: >-
    Thirty days is the window any business can get interest-free money in the form of a credit card, so at level 2 your credit limit becomes your advertising budget and at level 3 all customers pay for themselves and cash stops constraining growth.
  structure:
    - >-
      CFA Level 1: You make less profit (GP) from a customer than it costs you to get one (CAC) in the first thirty days
    - >-
      CFA Level 2: You make the same profit from a customer as it costs you to get one in the first thirty days
    - >-
      CFA Level 3: You make more than double the profit from a customer than it costs you to get one in the first thirty days
  applies_when: >-
    Judging whether a business can bootstrap its growth: you must pass level one to stay in business, level two comes from a decent product and a good offer, level three from mastering money models.
  anchor: >-
    By connecting GP and speed with CAC, I see three levels of CFA
  source: >-
    100m-series-lost-chapters.md, Levels of Customer Financed Acquisition, lines 2132–2199
  confirmations: 1
  authors_caveat: >-
    You can absolutely make money at level 1 over the long term and many big businesses make all their money that way, but you have to already have lots of money to do it, so the author avoids it when starting out.
  anchor_at: "100m-series-lost-chapters.md:2132"
- id: A-lost-chapters-016
  type: framework
  name: >-
    Back End: The Value Grid
  statement: >-
    Instead of a value ladder or stair step, lay the offers out as a grid: prospects entering at the bottom, each offer with the percentage of people who take it, revenue per client down the right, and totals and averages at the bottom, which give lifetime value and 30D Cash.
  why: >-
    A stair step makes your brain think customers must buy the first offer to buy the second and depicts the relationship as linear, which has not been the author's experience — many people buy offer #1 then skip to offer #4; the grid also makes the numbers visual so you can read CAC and 30D cash off it.
  structure:
    - >-
      The prospects coming into the business
    - >-
      Each offer, with the percentage of them who take it
    - >-
      All the way to the right you can see the revenue per client
    - >-
      At the bottom you can see the totals and averages
    - >-
      Add up all the revenue from all the clients in the grid, and divide it by how many people came in, and you know your lifetime value
  applies_when: >-
    Once you have metrics — the stair step is a great place to start to get ideas down, the grid becomes invaluable after that.
  anchor: >-
    point…not all customers follow it So, I think of it more as a grid For two primary reasons:
  source: >-
    100m-series-lost-chapters.md, Back End: The Value Grid, lines 2331–2400
  confirmations: 1
  authors_caveat: >-
    The grid itself is an image that did not survive into the text; its columns are reconstructed from the prose that describes the two worked grids (30D Cash = $75 versus 30D Cash = $1,763).
  anchor_at: "100m-series-lost-chapters.md:2336"
- id: A-lost-chapters-017
  type: framework
  name: >-
    Ultimate Offer Stacking Process
  statement: >-
    After figuring out all the needs you can monetize, choreograph the sales process to weave one of each core offer type together: Attract, then Up Front Cash, then Upsell/Downsell, then Continuity — and then repeat the cycle with a second continuity and a second up front cash offer.
  why: >-
    It gives the best of all worlds: the Up Front Money Model acquires customers profitably, upsells and downsells squeeze the most juice per prospect by getting the whales to buy big and the minnows into your world, and continuity creates consistent cash flow. Each pass increases the LTV of the customer and therefore how much you can spend to acquire them.
  structure:
    - >-
      1) Attract
    - >-
      2) Up Front Cash
    - >-
      3) Upsell/Downsell
    - >-
      4) Continuity
    - >-
      5) Continuity #2
    - >-
      6) Up front Cash #2
  applies_when: >-
    Building the money model of almost any business, after obviously using a free or discount hook; which up front model, upsell and continuity to use depends on the business and its typical customer-buying journey.
  anchor: >-
    Next, we decide how we are going to choreograph the sales process I use this framework
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, lines 2482–2522
  confirmations: 2
  authors_caveat: >-
    Adding more offers and services is a fast track to adding operational complexity; if something is going to add complexity, it had better be worth it. Start by adding the one conversion opportunity that adds the most money at the lowest cost, then add the next.
  anchor_at: "100m-series-lost-chapters.md:2484"
- id: A-lost-chapters-018
  type: framework
  name: >-
    The four-sale offer flow
  statement: >-
    The stack is run as four sales over the customer's first weeks — the service sale, the physical products sale, the more-services sale, and the prepay or last-chance sale — with a downsell ladder inside each and every prospect advanced to the next stage even after a no.
  why: >-
    The big high-value offer may have got them in the door, but not everyone says yes, so having another Grand Slam Offer in your back pocket dramatically increases your closing percentage; advancing prospects who said no gives another opportunity to provide value and monetize the person.
  structure:
    - >-
      Sale #1: Service Sale (Up Front Cash)
    - >-
      Sale #2: Physical Products Sale (Upsell Offer)
    - >-
      Sales #3: More Services Sale (Continuity) — positioned as a “Feedback” meeting
    - >-
      Sale #4: Prepay Sale or Last Chance (Up Front Cash, Downsell Continuity)
  applies_when: >-
    One-on-one selling in person or over the phone, over a span of 6 to 12 weeks; selling off a page digitally you will not have the luxury of the downsells.
  anchor: >-
    In the example above, we are selling services, then products Then we are selling them
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, Sample Weight Loss Offer Flow, lines 2528–2640
  confirmations: 1
  authors_caveat: >-
    The four sales are the labels of a worked weight-loss example rather than a list the author states as a general framework; the diagram it refers to is not in the text.
  anchor_at: "100m-series-lost-chapters.md:2543"
- id: A-lost-chapters-019
  type: framework
  name: >-
    Four Steps To Picking The Right Offer For Your Money Model
  statement: >-
    Before adding an offer, check it in the same order every time: right stage, right problem, right way, right time.
  why: >-
    Each stage of the money model has different offer types that fit its goal; and even a fitting offer fails if it solves a problem you cannot solve with existing resources, solves it in a way the customer does not want, or arrives after the moment of greatest need.
  structure:
    - >-
      Right Stage First, I make sure the offer fits the stage of the Money Model
    - >-
      Right Problem I prefer to pick problems that make sense for my business, that I can solve with existing resources, and that provide customers big value when solved
    - >-
      Right Way Third, I solve based on the customer’s preference
    - >-
      Right Time Fourth, and most importantly, I offer to solve their problem at the right time
  applies_when: >-
    Adding any new offer to a money model.
  anchor: >-
    offer, I follow the same process when adding a new offer to my Money Model It goes like
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, Four Steps To Picking The Right Offer, lines 2641–2671
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:2646"
- id: A-lost-chapters-020
  type: framework
  name: >-
    The attraction, upsell and continuity offers cut from $100M Money Models
  statement: >-
    Section C carries seven offers — three attraction offers (Free Presentations, Freemium, Free Pick Your Price), one upsell offer (Free With Alternate Revenue Stream) and three continuity offers (Lifetime Upgrades, Lifetime Discounts, Discount + One-Time Fee) — each usable independently of the others.
  why: >-
    They were cut from $100M Money Models as too hard or too niched for a wide array of businesses; the author keeps them as more bullets to add to your potential $100M Money Model, to be skipped around and picked from by description.
  structure:
    - >-
      Attraction Offer: Free Presentations
    - >-
      Attraction Offer: Freemium
    - >-
      Attraction Offer: Free Pick Your Price
    - >-
      Upsell Offer: Free With Alternate Revenue Stream
    - >-
      Continuity Offer: Lifetime Upgrades
    - >-
      Continuity Offer: Lifetime Discounts
    - >-
      Continuity Offer: Discount + One-Time Fee
  applies_when: >-
    Filling a stage of the money model once the Ultimate Offer Stacking Process has told you which stage needs an offer.
  anchor: >-
    are a hodgepodge of attraction offers, upsell offers, and continuity offers that didn’t make
  source: >-
    100m-series-lost-chapters.md, Section C: Advanced Offer Stacking, author note, lines 2245–2253
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2248"
- id: A-lost-chapters-021
  type: framework
  name: >-
    The three reasons presentations sell complex and expensive things
  statement: >-
    A presentation works on expensive and complex offers for three reasons: it gives you a captive audience, it keeps them long enough to explain the thing and provide value, and it lets you make your offer when they are the most motivated to take it.
  why: >-
    Buyers need to know enough stuff about your product to buy, and the more expensive or complex the thing, the more information they need; a presentation bridges that information gap and ends at the moment people see a fast, easy, low-risk way to solve their problem.
  structure:
    - >-
      1) You have a captive audience
    - >-
      2) You keep them for a long enough time to explain the thing and provide value
    - >-
      3) You make your offer when they’re the most motivated to take it
  applies_when: >-
    Selling complex and expensive stuff; the amount of time you take educating the consumer is directly related to the price and the amount of trust needed.
  anchor: >-
    They work especially well for complex and expensive stuff for three reasons:
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, lines 2702–2749
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2706"
- id: A-lost-chapters-022
  type: framework
  name: >-
    Free Education with Offer Examples
  statement: >-
    The free education-with-offer formats run from shortest to longest — free dinner, free 90-minute masterclass, free 5 day challenge, free 3 day virtual summit, free strategy call — and each carries its own conversion benchmark.
  why: >-
    The more expensive the offer the more audiences want to learn about it before buying, and the colder the audience the more exposure it takes to build trust; the free education-with-offer forces as much exposure as it can in as short a window as reasonable.
  structure:
    - >-
      Free XYZ Dinner / Free Neuropathy Dinner / Free Diabetic Dinner — Benchmark: a quarter of the room to the lower offer, a third of those to the higher offer
    - >-
      Free 90-minute Masterclass — Benchmark: Convert 10% of those on the call when an offer is presented
    - >-
      Free 5 Day Challenge — Benchmark: Convert 2 to 5% of people who sign up
    - >-
      Free 3 Day virtual Summit — Benchmark: Aim to convert 10% of those attending the final day
    - >-
      Free Strategy Call — Benchmark: Convert 25% of those who make it to the second call
  applies_when: >-
    Picking an attraction offer format: presentations can last anywhere from 15 seconds to 15 days, and the more expensive and complicated the thing, the longer they tend to get.
  anchor: >-
    Presentations can last anywhere from 15 seconds to 15 days The exact length of the
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, Free Education with Offer Examples, lines 2734–2845
  confirmations: 1
  authors_caveat: >-
    Benchmarks as published in 2025.
  anchor_at: "100m-series-lost-chapters.md:2734"
- id: A-lost-chapters-023
  type: framework
  name: >-
    Free XYZ Dinner
  statement: >-
    Get people in the door with a free dinner, present for 60 to 90 minutes during the meal, make an offer at the end for a product that covers the cost of getting everyone there, and set individual appointments with the buyers to offer a much higher ticket item.
  why: >-
    The lower offer pays for the room, and the buyers of the lower offer are the pool for the high-ticket sale — a 100-person audience gives 25 or so at the lower offer and eight or so at the higher one.
  structure:
    - >-
      Free dinner gets people in the door
    - >-
      During the meal you make a presentation between 60 and 90 minutes
    - >-
      At the end of the presentation, you make an offer for a product that covers the cost of getting everyone to the dinner
    - >-
      Of those who buy, you set up individual appointments to offer a much higher ticket item
    - >-
      Benchmark: convert a quarter of the room to the lower offer, and at least a third of those to the higher offer
  anchor: >-
    Free dinner gets people in the door, and during the meal you make a presentation
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, lines 2751–2761
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2752"
- id: A-lost-chapters-024
  type: framework
  name: >-
    Free 5 Day Challenge
  statement: >-
    Give four live 60–90 minute presentations Monday through Thursday, each covering a core belief that prevents them from buying plus content they can apply today, then make the offer on Friday.
  why: >-
    It converts ice-cold audiences for lower cost and very high-cost offers alike, and even those who do not buy get real value, so the worst case is goodwill with the marketplace.
  structure:
    - >-
      Give four live 60–90 minute presentations Monday through Thursday
    - >-
      Each presentation covers some useful aspect of the problem they want to solve or result they want to achieve
    - >-
      Each day focus on some core belief that prevents them from buying, and provide enough useful content they can apply today
    - >-
      Then, make your offer on Friday
    - >-
      Benchmark: Convert 2 to 5% of people who sign up for the free multi-day challenge
  applies_when: >-
    Converting ice-cold audiences.
  anchor: >-
    Give four live 60–90 minute presentations Monday through Thursday Each presentation
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, lines 2770–2795
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2771"
- id: A-lost-chapters-025
  type: framework
  name: >-
    Free 3 Day virtual Summit
  statement: >-
    Run three full days of speakers, each day's 4+ presentations structured around one of the core beliefs, pitch at the end of day two, repitch on day three, and end the event with inspiration to take action.
  why: >-
    It sets up the highest ticket offers of all because it has the most possible content for any reasonable person to consume in a row.
  structure:
    - >-
      Come see speakers over three full days talk about their topics of expertise, each topic covering one aspect of their problem or goal
    - >-
      Structure each of the days (4+ presentations) around one of the core beliefs
    - >-
      Then make a pitch at the end of day two
    - >-
      Repitch on day three
    - >-
      Ending the event with some inspiration to take action tends to work well
    - >-
      Benchmark: Aim to convert 10% of those attending the final day
  anchor: >-
    Structure each of the days (4+ presentations) around one of the core beliefs (found
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, lines 2800–2823
  confirmations: 1
  authors_caveat: >-
    As a personally surprising finding, the days of the week do not matter — do them whenever is most convenient for you and your team.
  anchor_at: "100m-series-lost-chapters.md:2816"
- id: A-lost-chapters-026
  type: framework
  name: >-
    BANT: Budget, Authority, Need, Timing
  statement: >-
    On a free strategy call you triage the person on four points — that they have the budget, the authority to make a buying decision, that they want what you are selling, and that they want to start within the timeframe you deem optimal.
  why: >-
    The free strategy call is step one of a two-step sales process, so it acts as a pre-qualification call for the later sale; you provide value on it by listening, identifying needs and offering solutions, and only then make an offer.
  structure:
    - >-
      1) Has the budget for what you are selling
    - >-
      2) Has the authority to make a buying decision (or will have those people on the next call)
    - >-
      3) Wants what you are selling
    - >-
      4) Wants to start within the timeframe you deem optimal
  applies_when: >-
    A free strategy call used as the first step of a two-step sale.
  anchor: >-
    acronym for this is BANT: Budget, Authority, Need, Timing You provide value on this
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, Free Strategy Call, lines 2825–2844
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2840"
- id: A-lost-chapters-027
  type: framework
  name: >-
    Three core limiting beliefs
  statement: >-
    Every presentation, from one 60–90 minute session to a dozen, plays on the same three core limiting beliefs: the results must come easy, I must get the best results possible, and results must lead to attention and approval.
  why: >-
    The better the messaging is at aligning and playing to the three core beliefs the better your conversion will get; more and longer presentations just let you go deeper into the same three.
  structure:
    - >-
      1) The results must come easy
    - >-
      2) I must get the best results possible
    - >-
      3) Results must lead to attention and approval - aka - status
  applies_when: >-
    Structuring the content of any presentation-based offer, including which belief each day of a multi-day format attacks.
  anchor: >-
    minutes (like the summit) all serve to play on the three core limiting beliefs. The
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, Pro Tips, lines 2846–2893
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:2851"
- id: A-lost-chapters-028
  type: framework
  name: >-
    The three requirements of a freemium give-away
  statement: >-
    What you give away free must cost you almost nothing to fulfill, provide continuous value rather than one-time value, and not give away so much of the farm that they will never want to buy something else.
  why: >-
    Freemium is not a business model, it is an acquisition strategy: the free thing must be good enough that people come by word of mouth and keep using it, while still leaving a paid thing worth upgrading to. That is a very difficult balance.
  structure:
    - >-
      1) costs you almost nothing to fulfill
    - >-
      2) provides continuous value (not one-time)
    - >-
      3) doesn’t give away so much of the farm that they’ll never want to buy something else
  applies_when: >-
    Software or media businesses with close to 100% incremental margins; in B2B, give away something that exposes a hole in their business that your next paid product solves.
  anchor: >-
    challenging You must give something away that 1) costs you almost nothing to fulfill, 2)
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Freemium, lines 2985–3012
  confirmations: 1
  authors_caveat: >-
    Almost every company in the examples has funding; without investors and large amounts of capital the author would not recommend this structure — steer clear unless you have something so valuable that lots of people come towards you without marketing.
  anchor_at: "100m-series-lost-chapters.md:2993"
- id: A-lost-chapters-029
  type: framework
  name: >-
    Freemium Roadblocks
  statement: >-
    Freemium fails in three ways: a conversion problem (too few free users upgrade), a value problem (the free thing is not worth telling others about), or a cost problem (people want it and share it, but servicing them free costs too much relative to what paid customers bring).
  why: >-
    Your true cost of acquisition on this model is the cost of servicing a free customer divided by the percentage who upgrade, so each of the three roadblocks breaks that equation in a different place.
  structure:
    - >-
      #1 Conversion Problem: Conversion percentage from free to paid is too low.
    - >-
      #2 Value Problem: You give away something that people don’t find valuable enough to tell other people about.
    - >-
      #3 Cost Problem: People want it. They tell their friends about it, but your costs of fulfilling them for free are too high relative to what you make from paid customers.
  applies_when: >-
    Diagnosing a freemium acquisition strategy that is not profitable.
  anchor: >-
    Here are just a handful of the problems you can encounter with this model.
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Freemium, Roadblocks, lines 3025–3033
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3026"
- id: A-lost-chapters-030
  type: framework
  name: >-
    Attraction Offer: Free Pick Your Price
  statement: >-
    Market the offer as free, pre-frame at the start of the sale that there is a pick-your-price setup with bonuses at different levels and no obligation to pay anything, then at checkout let them pick their own price with bonuses at three levels of payment, and close by naming the payment methods and shutting up.
  why: >-
    People feel 100% in control of their own destiny and it pulls on their generosity, so it generates goodwill and works well in low-trust environments; and the more they pay, the more they will pay attention to the results.
  structure:
    - >-
      You market the promotional offer as free
    - >-
      Explain at the beginning of the sale that you have a pick-your-price type setup and that the staff is offering different bonuses at different levels, but they are not obligated to pay anything
    - >-
      Hit the prospect hard with confrontational questions to ensure they would be a good long-term candidate
    - >-
      When the person gets to the checkout, you give them an offer to pick their own price, explaining the benefits of investing more
    - >-
      You offer bonuses for three levels of payment (think small, medium, large)
    - >-
      Outline what they get at each level, then say we accept Visa, Mastercard, or XYZ payment, which would you prefer to use? Then shut up
  applies_when: >-
    Low-trust environments, and only where the free thing has low operational costs; the conversion rate is very high although the average ticket is typically lower.
  anchor: >-
    You market the promotional offer as free When the person gets to the checkout, you
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Pick Your Price, lines 3085–3191
  confirmations: 1
  authors_caveat: >-
    This offer does not work with a discount wrapper; and if someone does not want to pay, you must give them the basic level for free.
  anchor_at: "100m-series-lost-chapters.md:3086"
- id: A-lost-chapters-031
  type: framework
  name: >-
    Paired Upsell and Independent Upsell
  statement: >-
    Free With Alternate Revenue Stream comes in two buckets: the paired upsell, where thing A is free in exchange for buying thing B, and the independent upsell, where thing A is free and you encourage them to buy thing B.
  why: >-
    The offer depends on the revenue streams available to the business — you provide one type of service or product for free and monetize something else — and the two buckets are the two ways that dependency can be structured.
  structure:
    - >-
      Paired Upsell: I give you thing A for free, in exchange for buying thing B
    - >-
      Independent Upsell: I give you thing A for free, and I will encourage you to buy thing B
  applies_when: >-
    Businesses with an alternative revenue stream whose margins are high enough to afford both fulfillment types; usable as a downsell, as a front-end offer, or as the whole business model.
  anchor: >-
    Paired Upsell: I give you thing A for free, in exchange for buying thing B
  source: >-
    100m-series-lost-chapters.md, Upsell Offer: Free With Alternate Revenue Stream, lines 3243–3262
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3255"
- id: A-lost-chapters-032
  type: framework
  name: >-
    The two factors the Free With Alternate Revenue Stream play runs on
  statement: >-
    The play's effectiveness rests on how essential or required the prospect perceives the next thing to be, and on how seamless the upsell process is for them.
  why: >-
    If you make the upsell frictionless you can get 90% plus take rates on these offers — they should feel like it makes total sense to buy it — and a high take rate up front is what liquidates the acquisition cost.
  structure:
    - >-
      1) The prospect’s perception of how essential/required the next thing is (like the lock in the storage unit scenario)
    - >-
      2) How seamless the upsell process is for the prospect
  applies_when: >-
    Designing what to upsell after the free thing; the next thing you sell should be the next natural thing the prospect would need.
  anchor: >-
    The effectiveness of this play is based on:
  source: >-
    100m-series-lost-chapters.md, Upsell Offer: Free With Alternate Revenue Stream, lines 3344–3355
  confirmations: 1
  authors_caveat: >-
    If someone does not buy the upsell they are unlikely to stay — it is the greatest predictor of back-end conversion, so that sale is a must-have rather than a nice-to-have.
  anchor_at: "100m-series-lost-chapters.md:3344"
- id: A-lost-chapters-033
  type: framework
  name: >-
    The “when” and “what” of continuity bonuses
  statement: >-
    Every stick bonus is one “when” paired with one “what”: the when is a delay or a milestone, the what is a one-time bonus, a variable bonus, or a lifetime upgrade.
  why: >-
    A good offer gets them to start, good bonuses get them to stick: the time to the first bonus extends their stay once, and if you keep giving them bonuses you extend their stay more times.
  structure:
    - >-
      “When”: delays — how long they have to wait
    - >-
      “When”: milestones — what they have to do or achieve to get the thing
    - >-
      “What”: a one-time bonus, you give one time
    - >-
      “What”: a variable bonus, you give on a schedule, but it changes each time
    - >-
      “What”: a lifetime upgrade — a permanent high-value change in continuity status
  applies_when: >-
    Anything that provides continuous value, once people have already started the continuity program and the job is getting them to stick.
  anchor: >-
    When I make a bonus, I think of “when” and “what” For the “when” part, I use delays
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, lines 3477–3620
  confirmations: 2
  authors_caveat: >-
    Unless your bonus gives a huge and permanent improvement, keep it variable: no matter how good you make your thing, customers will get used to it. Make milestones things that make the customer more successful or that advertise on your behalf, ideally both.
  anchor_at: "100m-series-lost-chapters.md:3480"
- id: A-lost-chapters-034
  type: framework
  name: >-
    Continuity Offer: Lifetime Discounts
  statement: >-
    A lifetime discount gives a cheaper price for as long as the customer stays on recurring payments, and is made attractive by adding urgency (limited time), scarcity (limited number) and believable reasons for both.
  why: >-
    Customers take it now because they get value at a discount now, and they stick because if they leave they cannot get it back; urgency and scarcity are what make them act on it in the first place.
  structure:
    - >-
      Retail Price
    - >-
      Offer — the discount, given as long as they stay on recurring payments
    - >-
      Discount Price
    - >-
      Reason (ex: new location, it will have bugs, we want your feedback)
    - >-
      Urgency (limited time)
    - >-
      Scarcity (limited number)
  applies_when: >-
    Recurring services, digital products and recurring physical products; used by the author as an upsell (a Rollover Upsell discount kept only if they finish the credited payments) rather than as the attraction offer.
  anchor: >-
    To make Lifetime Discounts even more attractive, add urgency (limited time), scarcity
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, lines 3658–3758
  confirmations: 1
  authors_caveat: >-
    A Lifetime Discount only works if you actually charge more when this offer ends, and comes with a big fat warning: know your numbers, because the costs of getting and delivering will change while their rate is locked in.
  anchor_at: "100m-series-lost-chapters.md:3664"
- id: A-lost-chapters-035
  type: framework
  name: >-
    Three ways to display your lifetime discount
  statement: >-
    A lifetime discount is displayed as a percentage off retail, a dollar amount off retail, or a fixed price (price protection).
  why: >-
    The first two are far more flexible: if things change you can adjust your retail price and lifetime discount customers still keep their discount, whereas a fixed price for life locks you in.
  structure:
    - >-
      a percentage off retail (50% off)
    - >-
      a dollar amount off retail ($20 off)
    - >-
      a fixed price (price protection)
  applies_when: >-
    Setting the form of a lifetime discount; if you decide to offer a fixed price for life — know your numbers.
  anchor: >-
    Three ways to display your lifetime discount You can offer a percentage off retail
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, Important Notes, lines 3766–3779
  confirmations: 1
  authors_caveat: >-
    The author prefers to limit price protection to a fixed period rather than forever — normally $50/mo but you can pay $20/mo for the next 36 months.
  anchor_at: "100m-series-lost-chapters.md:3766"
- id: A-lost-chapters-036
  type: framework
  name: >-
    The four steps to creating your one-time fee(s)
  statement: >-
    Build a one-time fee by picking its name, picking its price, picking its reason why, and then charging it, discounting it, or waiving it.
  why: >-
    The higher the one-time startup fee, the lower the churn — the higher the barrier to entry, so too becomes the higher the barrier to exit — and the fee offsets the acquisition costs of marketing and sales while the discount attracts the interest.
  structure:
    - >-
      1) Pick Your Fee Name
    - >-
      2) Pick Your Fee Price
    - >-
      3) Pick Your “Reason Why”
    - >-
      4) Start Charging It, Discounting It, Or Waiving It
  applies_when: >-
    The Discount + One-Time Fee continuity offer, and especially services that require the customer to do something — give information, fill out forms, show up, change behavior — to succeed.
  anchor: >-
    So here are the four steps to creating your one-time fee(s):
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Discount + One-Time Fee, lines 3971–4021
  confirmations: 1
  authors_caveat: >-
    Be clear about what the reason for the one-time fee is, even though it is made up; it is not a fee to be taken lightly.
  anchor_at: "100m-series-lost-chapters.md:4008"
- id: A-lost-chapters-037
  type: framework
  name: >-
    The lead-getter meeting cadence
  statement: >-
    Meet each lead-getting employee six to 11 times per week: one 30 to 45 minute weekly meeting for coaching, feedback and praise, plus a short daily huddle at the beginning of each shift for expectations and goals and one at the end of each shift to report on them.
  why: >-
    It creates faster feedback cycles for building skills and morale, and gives a daily opportunity to praise and reward their efforts; recurring problems raised in the huddles go into the training checklist for the next hire.
  structure:
    - >-
      One 30 to 45 minute meeting per week for coaching, feedback, and praising success
    - >-
      A “daily huddle” at the beginning of each shift to discuss expectations and goals
    - >-
      A “daily huddle” at the end of each shift so they can report on them
  applies_when: >-
    After an employee has been trained and the job is keeping them doing it.
  anchor: >-
    on the business, I or my managers meet with each lead-getting employee six to 11 times per
  source: >-
    100m-series-lost-chapters.md, Keep Your Employees Getting You Leads—The Performance Diamond, lines 4333–4352
  confirmations: 1
  authors_caveat: >-
    Over time a team leader or manager takes over the huddles and eventually the one-on-ones, provided performance stays the same or improves.
  anchor_at: "100m-series-lost-chapters.md:4335"
- id: A-lost-chapters-038
  type: framework
  name: >-
    The performance diamond
  statement: >-
    When an employee's performance drops, work through four causes in order: communication (they don't know THAT we want it), training (they don't know HOW), motivation (they don't WANT to), and circumstances (something is stopping them).
  why: >-
    Approaching performance this way shows whether it is truly the employee's problem or, more often, something the owner messed up along the way — and most times both you and they want them to succeed, so once you find the cause you fix it.
  structure:
    - >-
      1) Communication—Employees don’t know THAT we want them to do it
    - >-
      2) Training—Employees don’t know HOW to do it
    - >-
      3) Motivation—Employees don’t WANT to do it
    - >-
      4) Circumstances—Something is stopping them
  applies_when: >-
    Diagnosing performance problems in a lead-getting employee who has stopped doing a good job.
  anchor: >-
    This is the performance diamond I use for diagnosing performance problems If I
  source: >-
    100m-series-lost-chapters.md, Keep Your Employees Getting You Leads—The Performance Diamond, lines 4354–4470
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:4466"
- id: A-lost-chapters-039
  type: framework
  name: >-
    The three reasons people don't want to do things
  statement: >-
    Motivation fails for three reasons: the reward comes at the wrong time, frequency, intensity or source; they have an aversion to the work, environment, leadership, coworkers or consumers; or events and lifestyle outside work are killing their performance.
  why: >-
    Solving it comes from asking questions with these three levers in mind — change the reward's frequency, intensity or source; look for systemic issues in the workplace; or ask open-ended questions to find what is eating their attention outside work.
  structure:
    - >-
      “Reward” comes at: the wrong time, wrong frequency, wrong intensity, or the wrong source
    - >-
      They have an aversion to: the work itself, environment, leadership, coworkers, consumers
    - >-
      They have events or other lifestyle stuff outside work killing their performance
  applies_when: >-
    The motivation branch of the performance diamond, once you have established they know that you want it done and how to do it.
  anchor: >-
    them to do it, and how to do it, they might not want to do it And people don’t want to
  source: >-
    100m-series-lost-chapters.md, Keep Your Employees Getting You Leads—The Performance Diamond, lines 4407–4433
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4409"
- id: A-lost-chapters-040
  type: framework
  name: >-
    How to calculate returns from lead-getting employees
  statement: >-
    Divide total payroll by total engaged leads to get cost per engaged lead, multiply by the engaged leads needed per customer to get CAC, then divide LTGP by CAC to get the LTGP : CAC ratio.
  why: >-
    Excluding paid ad spend, the cost of advertising with employees is almost entirely the money you pay them to do it, so comparing payroll with what the engaged leads they get bring in is the whole calculation.
  structure:
    - >-
      Total Payroll / Total Engaged Leads = Cost per engaged lead
    - >-
      (Cost per engaged lead) x (engaged leads per customer) = CAC
    - >-
      (LTGP) / (CAC) = LTGP : CAC
  applies_when: >-
    Any advertising method staffed by employees rather than paid media — outreach, content and so on.
  anchor: >-
    simplify this by just comparing how much money we spend on payroll to how much money
  source: >-
    100m-series-lost-chapters.md, How to Calculate Returns From Lead-Getting Employees, lines 4475–4500
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4480"
- id: A-lost-chapters-041
  type: framework
  name: >-
    Advertising problem or sales problem
  statement: >-
    If CAC is more than 3x industry average, ask one question — do my engaged leads have the problem I solve and the money to spend? If no, it is an advertising problem; if yes and they are buying but there are not enough of them, it is an advertising problem; if yes and they are not buying, it is a sales problem.
  why: >-
    It tells you which employees to focus on: don't fire your sales guy if you've got advertising problems, and equally don't fire your advertising employees if you've got a sales problem.
  structure:
    - >-
      If no, then they’re not qualified—that’s an advertising problem
    - >-
      They’re buying but you don’t have enough of them—advertising problem
    - >-
      They’re qualified but not buying—sales problem
  applies_when: >-
    Only once CAC is more than 3x industry average; within 3x of industry average you are doing good enough and should focus on bumping up LTGP instead.
  anchor: >-
    Do my engaged leads have the problem I solve and the money to spend?
  source: >-
    100m-series-lost-chapters.md, How To Know Which Employees To Focus On To Maximize Returns, lines 4501–4516
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4507"
```
