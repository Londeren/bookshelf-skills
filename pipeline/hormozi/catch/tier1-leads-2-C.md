# Улов фазы 1 — $100M Leads (2023), from #4 Run Paid Ads to the end (lines 6901–14623) (ярус 1), тип C: разборы (кейсы)

Группа `tier1-leads-2`, слаг `leads-2`, ярус 1. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **46** (экстрактор вернул 46, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-leads.md` | 6901–14623 | 7 | 46 |

## Как собран файл

Экстрактор C (Application cases) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier1-leads-2.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier1-leads-2-C.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: C-leads-2-001
  type: case
  name: >-
    The ugliest ad: the Chino Hills 6 week challenge
  statement: >-
    A text-only all-caps Facebook ad named the town and the number of spots (5 Chino Hills residents), offered a free 6 week challenge, stated the price of entry as before and after pictures, and ended with a single explicit instruction plus a link; leads came within hours, were called and reminded by text an hour before the appointment, and 19 sold at $299 each, turning $1000 of ad spend into just under $5700.
  why: >-
    The ad had no images, no video and no frills, so its whole effect came from a local callout, a concrete offer and a spelled-out next step; conviction made up for the lack of sales skill.
  demonstrates: >-
    The three chunks of an ad (callout, value, CTA); the Label callout with LOCAL AREA + TYPE OF PERSON; a lead magnet that asks for something in exchange; spelling out the next step.
  anchor: >-
    I'M LOOKING FOR 5 CHINO HILLS RESIDENTS TO TAKE PLACE IN A FREE 6 WEEK
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, lines 6975–7006
  confirmations: 1
  anchor_at: "100m-leads.md:6979"
- id: C-leads-2-002
  type: case
  name: >-
    The Who lens run over a business audience
  statement: >-
    The claim risk free is expanded through the people around the prospect: the spouse who will not nag about the purchase, the kids who notice the parent is less stressed about work, the competitors whose phones stop ringing, the business owner buddies who say business must be good at the golf range.
  why: >-
    Humans are status driven and status comes from how other people treat them, so every value element gains extra benefits when it is shown from someone else's perspective; those benefits are missed if the offer is only described from the prospect's own point of view.
  demonstrates: >-
    The Who lens of the What-Who-When framework: apply each who perspective to each value driver.
  anchor: >-
    Let's do business examples. If I said something was risk free, I want
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, lines 7687–7696
  confirmations: 1
  anchor_at: "100m-leads.md:7687"
- id: C-leads-2-003
  type: case
  name: >-
    Weight loss run through What-Who-When
  statement: >-
    The same weight loss offer is written out along a timeline from the prospect's view (teased as a kid — past, struggling to button favourite jeans — present, moving up another belt loop — future), then along the same timeline from other people's view (the kid asking why other kids make fun of them, kids complaining that other dads join practice, the doctor saying he may not walk his daughter down the aisle), and finally as combined copy lines that tag WHO, WHAT and WHEN in one sentence.
  why: >-
    People only think of how decisions affect the here and now; running the past, present and future through their own and other people's perspectives makes them see the consequence of their decision or indecision right now, and produces many different angles from one offer.
  demonstrates: >-
    The What-Who-When framework: value elements plus perspectives plus timeline; the bad stuff first, then contrasted with the good stuff if they buy.
  anchor: >-
    struggling to button their favorite pair of jeans (present) or moving up
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, lines 7728–7776
  confirmations: 1
  anchor_at: "100m-leads.md:7730"
- id: C-leads-2-004
  type: case
  name: >-
    Before and after: the web address in a CTA
  statement: >-
    Instead of alexsprivateequityfirm.com/free-book-and-course2782, use acquisition.com/training.
  why: >-
    A common CTA sends the audience to a website, so the address has to be short and memorable; CTAs must be quick and easy — easy phone numbers, obvious buttons, simple websites.
  demonstrates: >-
    The CTA chunk of an ad: make the next step quick and easy.
  anchor: >-
    audience to a website. So make your web address short and memorable:
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, lines 7870–7882
  confirmations: 1
  authors_caveat: >-
    The author notes he spent $370,000 on the single word domain Acquisition.com and may overvalue easy domains.
  anchor_at: "100m-leads.md:7872"
- id: C-leads-2-005
  type: case
  name: >-
    Ten ads, nine losers, 100x down on the winner
  statement: >-
    $100 goes into each of ten ads ($1,000 total); nine lose the full $100 and one returns $500 on its $100, leaving the account $500 down — most people stop at the loss, but the $500 return marks a winner, so $10,000 goes into that one ad and returns $50,000.
  why: >-
    The number of losses is high but each loss is small because the author knows when to shut an ad down, and the number of wins is low but each win is large because he knows when to hit the gas; to win big you have to see the winners and double, triple, quadruple, 10x down on them.
  demonstrates: >-
    Phase Two Lose Money of the three phases of scaling paid ads; scaling the winner rather than mourning the losers.
  anchor: >-
    Imagine I spend \$100 on ten ads - \$1,000 in total. Nine of them lose
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8126–8130
  confirmations: 1
  anchor_at: "100m-leads.md:8126"
- id: C-leads-2-006
  type: case
  name: >-
    Test budget = two times thirty-day cash
  statement: >-
    If a customer produces $100 of profit in the first thirty days, a new ad is allowed to run to $200 of spend before it is switched off, as long as it is producing leads; if the ad produces no leads at all it is shut off before 1x thirty-day cash, that is $100.
  why: >-
    The author wasted money letting bad ads run too long and lost even more by killing ads before they had a chance; two times the thirty-day cash collected turned out to be the sweet spot.
  applies_when: >-
    Testing a new ad.
  demonstrates: >-
    Budgeting a test off cash collected in thirty days, not off LTGP.
  anchor: >-
    For example, if I know I make \$100 in profit from a customer in the
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8146–8156
  confirmations: 1
  anchor_at: "100m-leads.md:8153"
- id: C-leads-2-007
  type: case
  name: >-
    Reversing the daily budget from the customer goal
  statement: >-
    The question is not how much to spend but how many customers can be handled: 100 customers next month at $100 each requires $10,000, padded twenty percent because ads get less efficient as they scale, giving $12,000 over thirty days or $400 per day — and then the number is committed to.
  why: >-
    Once ads break even or better the constraint is the business, not the budget; if the number terrifies you, you are doing it right — trust the data.
  applies_when: >-
    Phase Three, once ads make back more money than they cost.
  demonstrates: >-
    Reverse the ad budget from the sales goal rather than picking a spend.
  anchor: >-
    next month, and customers cost me \$100 to get, I'd need to spend
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8187–8196
  confirmations: 1
  anchor_at: "100m-leads.md:8191"
- id: C-leads-2-008
  type: case
  name: >-
    Client financed acquisition on a $15 membership
  statement: >-
    A $15 per month membership costing $5 to deliver leaves $10 gross profit a month; at ten months average tenure that is $100 LTGP against a $30 CAC, a 3.3:1 ratio — profitable but with a cash flow problem, since only $10 comes back in month one. A $100 upsell at 100% margins taken by one in five customers adds $20 average per customer, so $10 + $20 = $30 collected inside thirty days and the customer is free.
  why: >-
    Any business can get interest free money for thirty days on a credit card, so covering the cost to get and fulfil a customer within thirty days squares the balance, removes money as the bottleneck and lets the cash be recycled into the next customer.
  demonstrates: >-
    Client financed acquisition; fixing a cash flow problem by immediately selling more rather than by cutting CAC.
  anchor: >-
    Say we have a \$15 per month membership that costs us \$5 to
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8363–8431
  confirmations: 1
  anchor_at: "100m-leads.md:8363"
- id: C-leads-2-009
  type: case
  name: >-
    Twelve weeks and $150,000: an advertising problem that was a sales problem
  statement: >-
    A portfolio company spent twelve weeks and $150,000 on paid ads and got the right leads on the phone, but they did not buy; the owner concluded advertising did not work and quit, when in fact the ads worked and the sales did not — an estimated ~$30M in enterprise value lost to the misdiagnosis.
  why: >-
    If engaged leads have the problem you solve and the money to spend and they are not buying, the ads are fine and the problem is sales; the cost to get customers does not come only from advertising.
  demonstrates: >-
    Don't Confuse Sales Problems With Advertising Problems; the diagnostic question about problem and money.
  anchor: >-
    invested in spent twelve weeks and \$150,000 to run paid ads. They
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, Personal Lessons from Paid Ads, lines 8463–8474
  confirmations: 2
  anchor_at: "100m-leads.md:8466"
- id: C-leads-2-010
  type: case
  name: >-
    The saturated chiropractor niche (Q&A)
  statement: >-
    An owner claiming his chiropractor niche was saturated is questioned in sequence: $2,000,000 a year in revenue; $30,000 a month on Facebook; no idea of the click-to-close conversion rate and no throughput tracking; no other platforms; no content; no cold outreach — against a $15.1B industry. A second owner in the same niche then says he spent $30k across four platforms last week.
  why: >-
    Owners who get to $1M–$3M from one platform hit a wall and assume they have tapped the market; the questions expose how small a slice of the available advertising they actually do.
  demonstrates: >-
    The Size Of The Pie Fallacy; More Better New as the three questions — could you advertise more, better, somewhere new.
  anchor: >-
    And the \$30k you spend, on one platform, for a two million dollar
  source: >-
    100m-leads.md, Core Four On Steroids: More Better New, lines 8608–8688
  confirmations: 2
  anchor_at: "100m-leads.md:8670"
- id: C-leads-2-011
  type: case
  name: >-
    $40,000 a month on a platform with 1B daily users
  statement: >-
    An entrepreneur making about $3,000,000 a year in weight loss worried that pushing ad spend past $40,000 per month would saturate his platform — a platform with over 1B active daily users, selling weight loss in America, a $60B industry.
  demonstrates: >-
    The Size Of The Pie Fallacy: mistaking the tiny slice you advertise to for the entire available market.
  anchor: >-
    about \$3,000,000 per year in the weight loss space. He worried
  source: >-
    100m-leads.md, Core Four On Steroids: More Better New, lines 8703–8707
  confirmations: 1
  anchor_at: "100m-leads.md:8704"
- id: C-leads-2-012
  type: case
  name: >-
    Five points on each step: why the constraint wins
  statement: >-
    A three-step process of 30% optin, 5% apply, 50% schedule is improved by five percentage points at each step separately: optin 30→35% is a 16% increase in leads (1.16x), apply 5→10% is a 100% increase (2x), schedule 50→55% is a 10% increase (1.1x) — the step with the biggest drop-off gives by far the biggest result.
  why: >-
    Constraints are the points where the smallest improvements create the biggest boost in results, which is why testing effort goes to whatever step the most leads drop off.
  demonstrates: >-
    Better: find the constraint by the biggest drop-off and test there.
  anchor: >-
    But let's ignore the constraint for a moment. Imagine we improve each
  source: >-
    100m-leads.md, Core Four On Steroids: More Better New, Better, lines 8934–8966
  confirmations: 1
  anchor_at: "100m-leads.md:8947"
- id: C-leads-2-013
  type: case
  name: >-
    From 4 to 1 to 12 to 1 on referrals
  statement: >-
    At an LTGP to CAC ratio of 4 to 1 it costs twenty-five percent of one customer's lifetime gross profit to get another; if every customer brings two more the ratio becomes 12 to 1, just over 8.3% of lifetime gross profit per new customer — three customers for the price of one.
  why: >-
    Referrals are worth more (higher LTGP) and cost less (lower CAC), and unlike the core four they are exponential rather than linear: one customer brings two, two bring four, four bring eight.
  demonstrates: >-
    Why referrals are the lowest cost, highest profit leads; the referral growth equation of referrals in minus churn out.
  anchor: >-
    an LTGP to CAC ratio of 4 to 1. That means it costs twenty-five percent
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, lines 9784–9790
  confirmations: 1
  anchor_at: "100m-leads.md:9785"
- id: C-leads-2-014
  type: case
  name: >-
    The PR company that renarrowed its call outs
  statement: >-
    A portfolio company doing public relations for generic small businesses had plenty of sales, heavy churn and years of plateau; its lowest churning customers all turned out to be in one specific niche and looking to raise funding from investors — only fifteen percent of the business, so retargeting risked the other eighty-five percent. The advertising call outs were changed to match that narrower perfect fit customer: the plateau broke, growth resumed toward millions per month, advertising cost fell because the messaging could be more specific, and the new customers started referring like clockwork.
  why: >-
    Increase the quality of the prospect and you increase the quality of the product: customers who get the most value have the most goodwill, and the customers with the most goodwill are the most likely to refer.
  demonstrates: >-
    Call Outs → Sell Better Customers, the first of the six ways to get more referrals by giving more value.
  anchor: >-
    To see what we could do, we looked at their lowest churning customers
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, lines 9982–10009
  confirmations: 1
  anchor_at: "100m-leads.md:9988"
- id: C-leads-2-015
  type: case
  name: >-
    Gym Launch: paid ad and a sale in the first seven days
  statement: >-
    Gym Launch tracked customer activities — speed to running the first paid ad, speed to the first sale, attendance on calls — and compared average customers with the best ones; gym owners who ran paid ads and made a sale in the first seven days had triple the LTGP, so the company forced everyone to launch ads and sell inside seven days, and average results, testimonials and referrals all rose.
  why: >-
    The customers with the best results get the most value from the product, so finding what they did and making everyone else do it raises the results of the average customer.
  demonstrates: >-
    Increase Perceived Likelihood of Achievement → Get More People Better Results; the six-step survey-interview-common actions-force-measure-guarantee process.
  anchor: >-
    We found out something huge. If a gym owner ran paid ads and
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, lines 10082–10092
  confirmations: 1
  anchor_at: "100m-leads.md:10087"
- id: C-leads-2-016
  type: case
  name: >-
    Case Study #1: Dropbox
  statement: >-
    Dropbox gave free storage to the customer and free storage to the friend they referred; the referral program went viral and the business grew 39x in fifteen months.
  demonstrates: >-
    Two-Sided Referral Benefits: pay the CAC to both parties.
  anchor: >-
    Dropbox gave free storage to customers
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, Referrals: Ask For Them, lines 10364–10367
  confirmations: 1
  anchor_at: "100m-leads.md:10364"
- id: C-leads-2-017
  type: case
  name: >-
    Case Study #2: Paypal
  statement: >-
    Paypal gave $10 in credit to the customer and $10 to the friend they referred; within two years the program helped them reach a million users, and six years later a hundred million — and they still use it.
  demonstrates: >-
    Two-Sided Referral Benefits; asking for referrals treated as an offer.
  anchor: >-
    two years, the program helped them reach a million users, and six years
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, Referrals: Ask For Them, lines 10377–10380
  confirmations: 1
  anchor_at: "100m-leads.md:10379"
- id: C-leads-2-018
  type: case
  name: >-
    The salesman who asked who else they'd bring
  statement: >-
    A new salesman shattered the ticket sales records of a portfolio company doing nothing different except one move: he asked each buyer who else they would want to come with them, then asked to be introduced. Half his sales were referrals. The scripted form is: people who do our program with someone else tend to get 3x the results — who else could you do this program with?
  why: >-
    Customers can only know what to do if you tell them, and the ask works when it shows the value the customer gets by referring — here, better results from doing the program with a friend.
  applies_when: >-
    On the sales contract or checkout page, right when they buy.
  demonstrates: >-
    Ask For A Referral Right When They Buy; showing how they get better results doing it with a friend.
  anchor: >-
    ask them who else they'd want to have come with them. Then ask them to
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, Seven Ways To Ask For Referrals, lines 10448–10460
  confirmations: 1
  anchor_at: "100m-leads.md:10453"
- id: C-leads-2-019
  type: case
  name: >-
    Referrals as a negotiation chip, and the Stacy answer
  statement: >-
    Against a $500 price and a prospect at $400, the discount is traded for introductions: I can't do anything less than $500 down, but if you make a 3-way text introduction to a few of your friends right now, I'd be happy to cut that initiation fee. When a full-priced customer finds out, the answer is that Stacy got $100 off because she referred three friends and the same $100 is available to them for three friends — who do you have in mind?
  why: >-
    You can ethically charge a different price for the same thing because you changed the terms of the sale; the objection ends either way — they back off or they give you three friends.
  demonstrates: >-
    Add Referrals As A Negotiation Chip; handling the discount objection from other customers.
  anchor: >-
    Ex: "I can't do anything less than \$500 down, but if you make a 3-way
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, Seven Ways To Ask For Referrals, lines 10469–10489
  confirmations: 1
  anchor_at: "100m-leads.md:10478"
- id: C-leads-2-020
  type: case
  name: >-
    The gift card referral promotion
  statement: >-
    Every customer is given a gift card worth one third of the cost of their program to hand to a friend who signs up, with an expiry seven to fourteen days out to force use; the referrer then says I got this gift card for $2000, do you want it, I don't want to waste it, rather than join my program for $2000 off. It combines with the three-way introduction — text a picture of the card with the friend's name written on it, which also gives a reason to ask for the name — and the cards can be sold at ninety percent off to friends of customers, so the referrer looks generous and you get paid to acquire.
  why: >-
    Handing over a gift card gives the referrer status with their friend and makes the offer feel like a much bigger deal than a discount.
  demonstrates: >-
    Combining several of the seven ways to ask: one-sided benefit, three-way introduction, scarcity by expiry.
  anchor: >-
    Give everyone a gift card for one-third the cost of their program. Tell
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, You're Only Limited By Your Creativity, lines 10557–10579
  confirmations: 1
  anchor_at: "100m-leads.md:10557"
- id: C-leads-2-021
  type: case
  name: >-
    Forty interviews per frontline hire (the cold outreach miss)
  statement: >-
    A cold outreach goal missed two quarters running is traced back through a chain of questions: a rep is lost every four weeks; churn is below industry average for the position; one of every four candidates from HR is hired; one qualified candidate comes per ten screening interviews — forty interviews for a single low-skill frontline worker, which caps hiring at about one a week. The fix was to stop one-on-one screening, interview in groups, screen only for crazies there and push everyone with a good work ethic and basic social skills to sales. Within six weeks hiring outpaced churn and by quarter end cold outreach sales had doubled to more than half of total sales.
  why: >-
    The issue was not the cold outreach method, skills or offer — there were simply not enough people doing cold outreach; to advertise more you need more workers.
  demonstrates: >-
    Finding the constraint and testing at it; employees as the way to do more of a core four activity.
  anchor: >-
    We get one qualified candidate per ten screening interviews, give or
  source: >-
    100m-leads.md, #2 Employees, lines 10684–10780
  confirmations: 1
  anchor_at: "100m-leads.md:10751"
- id: C-leads-2-022
  type: case
  name: >-
    Trading forty hours of doing for four hours of managing
  statement: >-
    Forty hours of doing traded for four hours of managing saves thirty-six hours, and the trade repeats: 200 hours of work per week become twenty hours of management, and those twenty hours are traded to a manager who costs four hours per week to lead — four hours of work for 200 hours of lead-getting.
  why: >-
    Employees take work, but less time and work than doing everything yourself; the trade compounds because it can be made over and over.
  demonstrates: >-
    Why employees are leverage; lead-getting employees do the core four you train them to do.
  anchor: >-
    You can swap 200 hours of work per week for twenty hours of
  source: >-
    100m-leads.md, #2 Employees, How Employees Work, lines 10821–10826
  confirmations: 1
  anchor_at: "100m-leads.md:10824"
- id: C-leads-2-023
  type: case
  name: >-
    Two businesses at $5,000,000 revenue: with you and without you
  statement: >-
    Scenario #1 is a business making $5,000,000 in revenue and $2,000,000 in profit that requires the owner around the clock — a high paying job whose business is worth almost nothing to anyone else. Scenario #2 has the same revenue and profit but runs without the owner: the owner gets time back, and because the asset makes millions without him it is a good investment for someone else, so $2,000,000 in profit, especially if climbing, could easily be worth $10,000,000+ right now — a $10,000,000 difference in net worth from learning to get other people to do it.
  why: >-
    If the business only makes money with you in it, it is a bad investment for anyone else; you get rich from what you make, you become wealthy from what you own.
  demonstrates: >-
    Why employees make you wealthy: turning a liability that relies on you into an asset you can rely on.
  anchor: >-
    year, especially if it's climbing, could easily be worth \$10,000,000+,
  source: >-
    100m-leads.md, #2 Employees, Why Employees Make You Wealthy, lines 10850–10903
  confirmations: 1
  anchor_at: "100m-leads.md:10894"
- id: C-leads-2-024
  type: case
  name: >-
    $3.33 per engaged lead at Acquisition.com
  statement: >-
    At the time of writing Acquisition.com got about 30,000 engaged leads per month with no paid ads and no outreach; the team creating the content cost about $100,000 per month, so payroll per engaged lead was roughly $3.33 ($100,000 / 30,000), far below what a lead is worth to the business.
  why: >-
    Excluding paid ad spend, the cost of advertising with employees is almost entirely what you pay them, so total payroll divided by total engaged leads gives the cost per engaged lead and the same math applies to any advertising method.
  demonstrates: >-
    Total Payroll / Total Engaged Leads = Cost per engaged lead, and the chain on to CAC and LTGP:CAC.
  anchor: >-
    For example: at the time of this writing, I get about 30,000 engaged
  source: >-
    100m-leads.md, #2 Employees, How to Calculate Returns From Lead-Getting Employees, lines 11241–11247
  confirmations: 1
  authors_caveat: >-
    Figures are as of the book, 2023.
  anchor_at: "100m-leads.md:11241"
- id: C-leads-2-025
  type: case
  name: >-
    Buying the agency owner's time at $750 an hour
  statement: >-
    Unable to afford either agency, the author asked the second one to show him in a few hours how they would run ads on his account; the owner refused — my time's not for sale — then priced it at $750 an hour, with the first four hours paid up front, $3,000. The arrangement was one hour a week with homework between calls, every call recorded and rewatched: calls one and two the agency drove and he watched, calls three and four he drove, by five and six he understood how the decisions were made and what data was tracked, and by seven and eight he no longer needed help. Eight hours and $6000 bought a skill that made millions.
  why: >-
    Hiring an agency is investing in a skill you cannot learn anywhere else short of all the trial and error, and learning it from a pro is what made the difference.
  demonstrates: >-
    Using an agency to learn a platform or method rather than to outsource it; paying extra to have decisions explained.
  anchor: >-
    Can you just show me in a few hours how you would run ads on my
  source: >-
    100m-leads.md, #3 Agencies, lines 11444–11520 and 11856–11862
  confirmations: 2
  anchor_at: "100m-leads.md:11444"
- id: C-leads-2-026
  type: case
  name: >-
    The opening the author uses with every agency
  statement: >-
    Every agency relationship is opened with a purpose and a deadline, in one speech: I want to do what you do but don't know how; work with me for six months so I can learn it; I'll pay extra for you to break down why you make the decisions you do and the steps you take; then I'll train my team, and once they can do it well enough we move to a lower cost consulting arrangement so you can still help if we run into problems — are you opposed to this?
  why: >-
    Most agencies are not opposed; if one is, move on, but be willing to negotiate, because at some price it is worth it for both parties.
  demonstrates: >-
    How to use agencies now: upfront intentions, a deadline, a planned move to consulting.
  anchor: >-
    I want to do what you do in my business, but I don't know how. I'd
  source: >-
    100m-leads.md, #3 Agencies, How I Use Agencies Now. And How You Can Too., lines 11688–11695
  confirmations: 1
  anchor_at: "100m-leads.md:11688"
- id: C-leads-2-027
  type: case
  name: >-
    Two agencies to learn YouTube
  statement: >-
    To learn YouTube the author hired two agencies at once: the first to keep him committed to making videos while doing some legwork on the platform, the second at 4x the price to teach the in-depth ideas behind making the best content possible; once his own videos beat the agency's videos, the relationship dropped to consulting only.
  why: >-
    You only get a fraction of an agency's attention and their results get worse as they take on clients, while your own team stays focused on you full time and keeps improving — so compare your team's results to theirs until you beat them, then cancel and put the money into scaling what you learned.
  demonstrates: >-
    Hire one good enough agency to learn the ropes of a new platform, then a more elite agency to learn to maximise it.
  anchor: >-
    hired to keep me committed to making videos while they did some legwork
  source: >-
    100m-leads.md, #3 Agencies, How I Use Agencies Now. And How You Can Too., lines 11707–11712
  confirmations: 1
  anchor_at: "100m-leads.md:11709"
- id: C-leads-2-028
  type: case
  name: >-
    Selling ten customers a month versus selling ten affiliates a month
  statement: >-
    Scenario #1: ten customers a month at $10,000 each caps the business at $100,000 a month, $1.2 million over twelve months, and with no other advertising it plateaus. Scenario #2: for the same effort, ten affiliates a month, each bringing one $10,000 customer per month, adds an extra $100,000 of revenue every month — $7.8 million over twelve months, and growing every month thereafter.
  why: >-
    Each affiliate adds another stream of leads and customers, so the same work compounds instead of capping.
  demonstrates: >-
    Why you want an affiliate army: affiliates are high-leverage lead getters.
  anchor: >-
    business caps at \$100,000 per month. In twelve months you've made 1.2
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Why You Want An Affiliate Army, lines 12110–12128
  confirmations: 1
  anchor_at: "100m-leads.md:12112"
- id: C-leads-2-029
  type: case
  name: >-
    ALAN's three levels of affiliates
  statement: >-
    ALAN grew through agency super-affiliates who brought agencies, agencies who brought local businesses, and local businesses who brought consumer leads: one super-affiliate added ten agencies a month, those ten brought about fifty local businesses a month, and those businesses brought about 2500 leads a month worked at roughly $5 each — $12,500 a month. Because each super-affiliate kept adding, one produced $12,500 in the first month, $25,000 in the second, $37,500 in the third; with only a few of them the company reached $1,700,000 a month within six months of launching.
  demonstrates: >-
    Layered affiliates and super-affiliates; a lead getter who gets lead getters (the highest leverage scenario).
  anchor: >-
    One super-affiliate added ten agencies per month. The ten agencies
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Why You Want An Affiliate Army, lines 12154–12168
  confirmations: 1
  anchor_at: "100m-leads.md:12154"
- id: C-leads-2-030
  type: case
  name: >-
    The list of 200 that started ALAN
  statement: >-
    With agency owners as the ideal affiliate, the author listed 200 products and services for agencies and the businesses delivering them; they fell into categories he now starts every affiliate hit list with — softwares, products, equipment, services, groups they belong to, and events they attended. A business landing in several categories is likely to hold lots of good leads and make a great affiliate.
  why: >-
    The ideal affiliate is a business with a warm audience full of people like your customers, so the work is answering who's got my leads and then putting the advertising effort there.
  demonstrates: >-
    Step 1: Find Your Ideal Affiliate — the questions about what your best customers buy, where they go and what they like to do.
  anchor: >-
    So I made a list of 200 products and services
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 1: Find Your Ideal Affiliate, lines 12264–12273
  confirmations: 1
  anchor_at: "100m-leads.md:12265"
- id: C-leads-2-031
  type: case
  name: >-
    Five callouts at one affiliate target (spa owners)
  statement: >-
    The same potential affiliate is called out five ways: the business owners themselves (ATTENTION SPA OWNERS); their customers (Do you work with busy professionals who spend all day in meetings?); the result they promise (To the heroes who heal the stress of others...); the products and services they deliver (If you sell lotions or scented oils this is for you...); and your own customers (Do you know anyone who owns a spa?).
  why: >-
    The affiliate offer is advertised the same way as any other offer — call out the audience, show the value elements, call to action — with affiliates as the customer you are advertising to.
  demonstrates: >-
    Step 2: Make Them An Offer, the call out; callouts as labels, yes-questions and if-then statements applied to affiliates.
  anchor: >-
    The affiliate's customers - ]{.calibre3}[Do you work with busy
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 2: Make Them An Offer, lines 12310–12328
  confirmations: 1
  anchor_at: "100m-leads.md:12318"
- id: C-leads-2-032
  type: case
  name: >-
    The affiliate money-making offer, labelled by value element
  statement: >-
    The standard affiliate offer is written out with its value elements tagged: make more money from your current customers and get more leads than your current offer (dream outcome), with a high chance of working since your customers already want the product (perceived likelihood of achievement), without needing to build, deliver or provide customer support for the product yourself (effort and sacrifice), so you can start selling it tomorrow (time delay).
  why: >-
    Affiliates demand a unique type of offer: instead of offering your product you offer a fast, simple and easy way to make commissions promoting it.
  demonstrates: >-
    The value equation applied to affiliates; all money making offers follow a similar structure.
  anchor: >-
    Make more money from your current customers and get more leads than
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 2: Make Them An Offer, lines 12350–12356
  confirmations: 1
  anchor_at: "100m-leads.md:12350"
- id: C-leads-2-033
  type: case
  name: >-
    Pricing the affiliate certification at 10-20%
  statement: >-
    Onboarding and training that certifies an affiliate as a product expert is charged at 10-20% of what the average active affiliate makes in the first twelve months: if the average affiliate makes $40,000 a year selling your stuff, charge $4000-$8000. Too low and they are not invested; too high and you do not get enough affiliates.
  why: >-
    Nine times out of ten, if they pay they'll pay attention; the fee also covers some of the cost of advertising and makes proper onboarding and training of every affiliate affordable.
  demonstrates: >-
    Step 3: Qualify Them — Way #2 Make Them An Expert.
  anchor: >-
    average affiliate makes \$40,000 per year selling your stuff, then
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 3: Qualify Them, lines 12429–12434
  confirmations: 1
  anchor_at: "100m-leads.md:12431"
- id: C-leads-2-034
  type: case
  name: >-
    Deriving the maximum allowable CAC for an affiliate payout
  statement: >-
    A single-use product sells for $200 and costs $40 to fulfil, leaving $160 to pay the affiliate and run the business; at a target LTGP:CAC of 3:1, three parts ($120) go to the business and one part ($40) to the affiliate — so up to $40 is paid for an affiliate to bring a new customer.
  demonstrates: >-
    Step 4: Figure Out What To Pay Them — pay affiliates off your maximum allowable CAC.
  anchor: >-
    we sell a single-use product for \$200 and it costs \$40 to fulfill.
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 4: Figure Out What To Pay Them, lines 12507–12511
  confirmations: 1
  anchor_at: "100m-leads.md:12507"
- id: C-leads-2-035
  type: case
  name: >-
    The three-tier payout and its blended cost
  statement: >-
    Against a $40 maximum allowable CAC the payout is tiered: Tier 1, 25% CAC = $10, for anyone who agrees to the initial terms (signs up, buys products or a certification); Tier 2, 50% CAC = $20, once they activate (finish the certification they bought, do a set number of posts and outreach, run a launch); Tier 3, 100% CAC = $40, once they sustain performance, for example five customers a month on subscription. With 20% of sales from tier 1, 20% from tier 2 and 60% from tier 3 the blended payout is $30 rather than $40, so LTGP:CAC moves from 3:1 to 4:1 — and cutting marketing costs by 33% can translate into 10% to 20% more net profit at the end of the year.
  why: >-
    Not all affiliates are created equal; reserving the maximum payout for top affiliates leaves the difference free to run contests, advertise for more affiliates or reward rising stars.
  demonstrates: >-
    Step 4: paying for what you want the affiliate to do — agree, activate, sustain.
  anchor: >-
    For example, if 20% of sales come from tier 1, 20% from tier 2, and 60%
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 4: Figure Out What To Pay Them, lines 12525–12571
  confirmations: 1
  anchor_at: "100m-leads.md:12567"
- id: C-leads-2-036
  type: case
  name: >-
    The author's book launch as whisper-tease-shout
  statement: >-
    Whisper (think call outs, curiosity): posted content, reached out to friends, emailed the list and told potential affiliates about major updates, showed which draft he was on, photographed printing out drafts, showed the many versions of the frameworks he drew and shared videos of himself editing early and late. Tease (think elements of value): revealed the product and the launch date, got specific with hard information, advertised the dream outcome of limitless leads with less work and faster, showed dozens of examples of the book used to its potential. Shout (think call to action): short, clear reminders to register, plus the exclusive bonuses only for people who bought during the launch.
  why: >-
    The longer something appears to take, the more an audience values it, so the work is shown; curiosity comes from wanting to know what happens next, so questions are planted and then answered only later.
  applies_when: >-
    Launching anything, not only an affiliate launch — the author put it in the affiliates section because he has found no better way to activate affiliates.
  demonstrates: >-
    Step 5: Get Them Advertising — the whisper-tease-shout launch and its cadence.
  anchor: >-
    draft I was on. I took pictures behind the scenes of me printing out
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 5: Get Them Advertising -- Launch, lines 12659–12720
  confirmations: 1
  anchor_at: "100m-leads.md:12662"
- id: C-leads-2-037
  type: case
  name: >-
    One massage business, three forms of lead magnet
  statement: >-
    A massage business recruits the personal training studio next door as an affiliate and gives every personal training buyer a free massage — a sample or trial that makes the studio's offer stronger and chargeable for more while producing massage leads. The reveal-a-problem version replaces the massage with a free or discounted posture assessment, which adds less value to the affiliate's offer but still sells, and after assessing you make an offer to fix what you revealed. The one-step version gives away step one of a three-part plan of massage, stretching and adjustments, so the value of the first step makes the customer fear missing the rest.
  why: >-
    The lead magnet has to make the affiliate's offer more valuable, so they can charge more and get more leads than they could without it — and you get the leads to upsell.
  demonstrates: >-
    Step 6: Keep Them Advertising — integration strategy 1, affiliates give your lead magnet away; the three best lead magnet types.
  anchor: >-
    personal training studio next door as an affiliate. Now, everyone who
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 6: Keep Them Advertising, lines 12787–12810
  confirmations: 1
  anchor_at: "100m-leads.md:12788"
- id: C-leads-2-038
  type: case
  name: >-
    The same nutrition consult at all three integration levels
  statement: >-
    Strategy 1: gym affiliates give away a free nutrition consult to every new member, the gym markets the included consult and charges more, and the supplements are upsold at the consult. Strategy 2: the gym sells the same nutrition consult for $99 or $199 and keeps all the money — letting them keep it makes them send even more leads — and the products are upsold during the consult. Strategy 3: gyms are taught to hold nutrition consultations with white labeled products and upsell the supplements to their members directly, with the money split.
  why: >-
    Giving affiliates all the cash from a lead magnet you fulfil makes it all profit and no work for them; your money comes from selling the main thing for more than the lead magnet cost to deliver.
  demonstrates: >-
    Step 6: the three integration strategies — give the lead magnet away, sell the lead magnet, sell the core offer.
  anchor: >-
    We'd get gym affiliates to give away a free
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 6: Keep Them Advertising, lines 12815–12893
  confirmations: 1
  authors_caveat: >-
    After testing, the author's companies kept Strategy 1 twice a year as a big event and Strategy 3 ongoing; many similar portfolio businesses use Strategy 2 — I'm just sharing what worked for us.
  anchor_at: "100m-leads.md:12815"
- id: C-leads-2-039
  type: case
  name: >-
    Service Business Case Study #1: National Tax Preparation Services
  statement: >-
    A $50M business preparing LLCs, bank accounts and articles of incorporation does not compete with Legalzoom; it partners with people who train new entrepreneurs and offers every affiliate's customer a free LLC setup — a high cost lead magnet. Launch: a big blast off seminar to the affiliates' audiences, where people take the free LLC. Integrate: once affiliates see the launch work, they build the free LLC into their own core offer, and the company's team then phones the customers the affiliates send for free and sells what they need next — bookkeeping, tax preparation. No money is spent on paid ads; the only advertising costs are delivering the lead magnet and a percentage of every first sale.
  demonstrates: >-
    Launch then integrate; a high cost lead magnet carried by affiliates; monetising on the back end.
  anchor: >-
    My friend\'s \$50M business prepares LLCs, bank accounts, and articles
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Three Case Studies You Can Model, lines 12938–12966
  confirmations: 1
  anchor_at: "100m-leads.md:12938"
- id: C-leads-2-040
  type: case
  name: >-
    Physical Products Case Study #2: Prestige Labs
  statement: >-
    Gym Launch, which sells and trains gym owners, is the affiliate for Prestige Labs supplements because its community of gym owners has active adult customers. Launch: gym owners get advertising materials to re-engage current and former customers with warm outreach and free content for a free 28 day challenge, and sell supplements to the people who come in. Integrate: they are then taught to sell supplements to every new member through a nutrition orientation worth $50-$1000 — a gym signing twenty clients a month with seventy percent buying yields fourteen new customers per gym per month, and 4000 gyms x 14 sales x $200 average order is a lot of money every month.
  demonstrates: >-
    Launch then integrate; recruiting as affiliates the businesses that already own your end customers.
  anchor: >-
    \$50-\$1000 of supplements. So if a gym signs up twenty clients per
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Three Case Studies You Can Model, lines 12976–13003
  confirmations: 1
  anchor_at: "100m-leads.md:12999"
- id: C-leads-2-041
  type: case
  name: >-
    Local Business Case Study #3: Chiropractors
  statement: >-
    Chiropractors go to high volume businesses whose people need adjustments — a gym. Launch: the gym owner promotes a three hour workshop on correct exercises and posture, free or at $29-$99 a head, and the money is split — give the gym 100% and they want to run it again, so thirty people at $99 makes the gym $2970 for a few emails and posts, while the chiropractor soft pitches at the workshop and collects patients. Integrate: long term the chiropractor gets one to two adjustments included with every new gym membership, which raises the value of the membership against the gym down the street and signals the gym cares about member safety, so every new member becomes a lead — repeated across thirty gyms.
  demonstrates: >-
    Launch then integrate for a local business; paying the affiliate all of the launch money to buy repetition.
  anchor: >-
    workshop where they show correct exercises and posture to get more from
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Three Case Studies You Can Model, lines 13011–13038
  confirmations: 1
  anchor_at: "100m-leads.md:13020"
- id: C-leads-2-042
  type: case
  name: >-
    The widget company's affiliate LTGP to CAC
  statement: >-
    A widget company pays $4000 in advertising per affiliate; the average affiliate sells $10,000 a month for twelve months, $120,000 of sales, at 75% gross margins leaving $90,000 of gross profit from all the customers that affiliate brought; a 40% payout is $36,000, leaving $54,000, so $54,000 / $4000 gives a 12.5:1 ratio.
  why: >-
    Affiliates work differently from other methods: you do not make much back from the affiliate itself, so returns are calculated against the gross profit of all the customers they send.
  demonstrates: >-
    Costs and returns on affiliates; the 3:1 floor and the three fixes — lower CAC, get more to activate, make them worth more by integration.
  anchor: >-
    Let's say we own a widget company that grows with
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Costs and Returns, lines 13084–13135
  confirmations: 1
  anchor_at: "100m-leads.md:13084"
- id: C-leads-2-043
  type: case
  name: >-
    Tripling the ad budget: $400,000 to $4M a month
  statement: >-
    After being told to set aside a percentage of the advertising budget for tests with no expectation of return, the author tripled his ad budget the next week: revenue went from $400,000 in June to $780,000 in July; when CAC rose he tried new audiences, most failed, one hit, and revenue passed $1M, $1.2M, $1.5M; following up engaged leads was tested by email (nothing) and phone calls (nothing) before text blasts took it to $1.8M; more paid ads with higher production value took it past $2.5M; then the affiliate program stacked another $1.5M a month on top, past $4M.
  why: >-
    You either win or you learn — test until you find something that works, take massive action, double down until it breaks, then test until you find the next thing and double down on that.
  demonstrates: >-
    More Better New in sequence: more spend, better follow-up at the constraint, then a new lead getter.
  anchor: >-
    Our business went from \$400,000 in June to \$780,000 in July. From
  source: >-
    100m-leads.md, Section V: Get Started, lines 13493–13520
  confirmations: 1
  anchor_at: "100m-leads.md:13499"
- id: C-leads-2-044
  type: case
  name: >-
    300 flyers versus 5000 a day
  statement: >-
    The author printed 300 flyers, put them on cars near the gym and got exactly one call — from a man whose Mercedes had been scratched. The mentor who suggested flyers asked the test size: he tests with 5000, and on a winner puts out 5000 a day, every day, for a month; half a percent response is decent and one percent is a winner, so 300 flyers at half a percent is one and a half people and cannot tell you anything. The author had been running about 1/1500th of the effort a flyer campaign requires.
  why: >-
    The right action in the wrong amount still fails; most people dramatically underestimate the volume it takes to make advertising work and stop too soon.
  demonstrates: >-
    Volume as the precondition of any test; the Rule of 100.
  anchor: >-
    Shoot, you only put out 300? Hard to know if anything works with such
  source: >-
    100m-leads.md, Advertising in Real Life: Open To Goal, lines 13615–13749
  confirmations: 1
  anchor_at: "100m-leads.md:13695"
- id: C-leads-2-045
  type: case
  name: >-
    100 reach outs over six weeks is 1/42 of the work
  statement: >-
    To the complaint that 100 reach outs over the last six weeks produced one customer so outreach does not work, the answer is that it was 1/42 of the work required: 100 per day, not 100 over time.
  why: >-
    Advertising is an inputs and outputs game; low effort inputs produce a low and unreliable output of engaged leads.
  demonstrates: >-
    The Rule of 100 read as a daily rate, not a total.
  anchor: >-
    I hear this all the time. "Alex, I reached out to 100 people over the
  source: >-
    100m-leads.md, Advertising in Real Life: Open To Goal, lines 13754–13756
  confirmations: 1
  anchor_at: "100m-leads.md:13754"
- id: C-leads-2-046
  type: case
  name: >-
    The gym chain's open-to-goal schedule
  statement: >-
    A successful gym chain let sales managers set their own schedules on one condition: five new members signed per day no matter what — done by lunch, they could leave early; if it took 18 hours, so be it.
  why: >-
    Open to goal commits you to the work until a number of outcomes is hit rather than to a number of actions, which unlocks a level of effort you did not know you had.
  demonstrates: >-
    Open To Goal as the Rule of 100 on steroids: work until the job is done rather than doing your best.
  anchor: >-
    own schedules. But there was a catch--they had to sign up five new
  source: >-
    100m-leads.md, Advertising in Real Life: Open To Goal, lines 13780–13785
  confirmations: 1
  anchor_at: "100m-leads.md:13781"
```
