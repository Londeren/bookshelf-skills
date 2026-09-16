# Улов фазы 1 — $100M Series: Lost Chapters (2025) with $100M Leads: 2 Bonus Chapters (2023) as a second copy of Section A (ярус 2), тип C: разборы (кейсы)

Группа `tier2-lost-chapters`, слаг `lost-chapters`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **66** (экстрактор вернул 66, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-series-lost-chapters.md` | 1–4810 | 6 | 66 |
| `100m-leads-bonus-chapters.md` | 1–568 | 1 | 0 |

## Как собран файл

Экстрактор C (Application cases) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-lost-chapters.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-lost-chapters-C.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: C-lost-chapters-001
  type: case
  name: >-
    The Vista method of buying a company and re-cutting its customer base
  statement: >-
    A private equity speaker breaks down how Vista grows an acquisition: score the existing customers by who stays the longest and pays the most, buy the company if there is a vein of underserved valuable customers, then cut the channels that brought the low-value customers and double down on the channels that brought the best ones.
  why: >-
    The author's reading of the math: it is Pareto on steroids — 20% of customers bring in 80% of revenue, so replacing the other 80% with high spenders grows the business 5x.
  demonstrates: >-
    Choosing the avatar by the value of existing customers, and moving ad spend onto the channels that produce them.
  anchor: >-
    Once they buy a company, they’d cut channels that brought the low-value customers
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, lines 215–231
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:220"
- id: C-lost-chapters-002
  type: case
  name: >-
    The sales page designer: same work, two customers
  statement: >-
    A designer lifts a sales page from 5% to 7% conversion. For company A, doing $100,000 per month from the page, that is $140,000; for company B, doing $10,000,000, it is $14,000,000. At a fee of 10% of growth the same work pays $40,000 per year from A and $4,000,000 per year from B.
  why: >-
    The profit comes from the premium you can charge, and the premium reflects the value delivered; selling to better customers means more value for identical work — you charge more because of who they are, not who you are.
  demonstrates: >-
    Pro Tip: You Make More Because of Who They Are, Not Because of Who You Are.
  anchor: >-
    make $40,000 per year. Not bad. From company B, you’d make $4,000,000 per
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, lines 304–316
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:314"
- id: C-lost-chapters-003
  type: case
  name: >-
    Gym Launch: the redefined avatar from steps one through three
  statement: >-
    Surveying customers and sorting for the top 20% produced four sets of qualifiers — demographics (right leaning/conservative, married, 25–45, male, gym owner, US-based), business requirements (signed lease, 1+ employees, $10,000+ per month revenue at the start, minimum 30 existing clients), aspirations ($1M+ gym, not work so much, open more locations) and buying reasons (not enough leads, bad market, bad pricing, can't find good employees). Step 4a: concentrate on audiences dense in those owners, spell the requirements out in ads and pages, and speak only to the problems and aspirations of the best customers rather than all customers.
  why: >-
    Advertising written to the requirements repels the bad customers and attracts the good ones; the qualifiers are the leading indicators of a high-value customer.
  demonstrates: >-
    The four steps of Your First Avatar — survey, find the biggest spenders, find what they have in common, execute.
  anchor: >-
    Demographics: Right leaning/conservative, married, 25–45, male, gym owner,
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, lines 330–350
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:335"
- id: C-lost-chapters-004
  type: case
  name: >-
    Gym Launch: reverse-engineering the buying process off the 78% finding
  statement: >-
    The survey data showed 78% of top customers had consumed at least two pieces of long-form content before buying, so the team injected two long-form high-value pieces into every lead's journey, raised total content output, and armed the sales team with an all-time greatest hits list from which reps hand-pick two or three pieces per prospect — forcing prospects through the same buying process the best customers went through.
  why: >-
    If a prospect on the phone had not consumed that content, the chance of selling them was lower; recreating the ideal buying experience on purpose raises the odds. The author notes the pieces were not disguised sales pitches but genuine value-in-advance content.
  demonstrates: >-
    Step 4b — look at what caused the better customers to buy, then make it happen on purpose.
  anchor: >-
    After looking at the data, we found that 78% of our top customers had consumed
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, lines 353–366 (repeated in Attraction Offer: Free Presentations, lines 2737–2741)
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:354"
- id: C-lost-chapters-005
  type: case
  name: >-
    70x less profit in the same vertical
  statement: >-
    A business services company serving fitness business owners made the same number of total sales as the author's company in the same vertical, yet 70x less profit. The difference: they accepted anyone with a pulse and a credit card and got high churn, high acquisition costs, low retention and lower satisfaction scores, with advice that had to stay generic; the author's company selectively pursued the highest-value customers and ignored all others, getting higher retention, higher gross margins, premium pricing and repeat business.
  why: >-
    Same market, different customer segmentation, monstrously different results — figuring out the most valuable customers to sell to works.
  demonstrates: >-
    Selecting the avatar rather than selling everyone; the cost of accepting all comers.
  anchor: >-
    the same vertical as me, and making the same number of total sales, he was making 70x less
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, lines 369–384
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:373"
- id: C-lost-chapters-006
  type: case
  name: >-
    Removing qualification steps: more leads, less money
  statement: >-
    Competitors copying the author's buyer journey panicked and cut steps to get volume. In the author's own tests, every time qualification steps were removed lead volume went up but the business made less money; merging marketing and sales into one acquisition department ended the problem — marketing stopped complaining that sales wasn't closing, sales stopped asking for more leads, and both focused on closing valuable deals.
  why: >-
    Knowing the ideal buyer journey forces patience and makes you optimise the return on advertising over the long haul instead of treating the business as a widget to be sold to as many people as possible.
  demonstrates: >-
    Keep the optimal number of qualification steps; quality over quantity in the buyer journey.
  anchor: >-
    every time we removed qualification steps, our lead volume increased, but we made less
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, lines 386–400
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:390"
- id: C-lost-chapters-007
  type: case
  name: >-
    Gym Launch LTGP against the competitors' LTGP
  statement: >-
    The average Gym Launch competitor has a lifetime gross profit of around $6,000–$8,000, a figure the author knows from looking at buying their businesses; Gym Launch's LTGP is north of $45,000. Only 6–8x on LTGP, but the resulting profit is breathtakingly different — imagine 8x your price with costs unchanged.
  why: >-
    Narrowing the focus means fewer customers in the short term and a possible short-term revenue dip from the cost of change, but a long term of higher retention and profitability.
  demonstrates: >-
    Serving only the highest-value customers as the lever on lifetime gross profit.
  anchor: >-
    Our LTGP is north of $45,000 Now despite the LTGP being *only* 6–8x higher, the
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, lines 405–418
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:409"
- id: C-lost-chapters-008
  type: case
  name: >-
    The first Gym Launch offer: giving away me
  statement: >-
    With no course and no program, the author made the first offer by giving himself away: fly out to the gym, spend his own money on marketing, work and close the leads, keep the cash he collects and give the gym the customers for free, plus show them how to sell supplements, hand over the nutrition program, show fulfilment and conversion into memberships — all free, with the author making only what he sells. Run for 33 gyms over 18 months, it was easy to sell because it was free, and it made his first million dollars outside the gyms.
  why: >-
    Entering a new market the author starts free or massively discounted: he does not yet know what he is doing and does not want to sell until it is exceptional, free buys testimonials fastest, free covers a lack of conviction on something never done before, and free makes referrals and demand easy to generate.
  demonstrates: >-
    The free promotion as the way into a new market; a Grand Slam Offer with the risk carried by the seller.
  anchor: >-
    I’ll fly out to your gym. I’ll spend my own money on marketing, I’ll work your leads. I’ll close
  source: >-
    100m-series-lost-chapters.md, SECTION A: ATTRACT, lines 520–546
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:525"
- id: C-lost-chapters-009
  type: case
  name: >-
    The $50,000 burger and the two hourly rates
  statement: >-
    A hedge fund manager making $50 million a year works out at $25,000 an hour over 2,000 hours, so a $50,000 burger costs him two hours of his time; at the author's own wage of $6.75 an hour, a burger, fries and a soda with tax next door — $13.50 — cost exactly the same two hours. Premium offers work the same way: while everyone buys traffic on a $6.75 budget, you buy it on a $25,000 budget, and you need nowhere near the volume.
  why: >-
    The power of infinite returns — there is no cap on the upside in pricing, but you can only go down to zero.
  demonstrates: >-
    Why a premium offer changes what you can afford to pay for traffic.
  anchor: >-
    Then I did the math on my own income of $6 75/hr It would cost me the same two hours
  source: >-
    100m-series-lost-chapters.md, Premium Promotions, lines 591–607
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:600"
- id: C-lost-chapters-010
  type: case
  name: >-
    190 sales at $50 profit against 9.5 sales at $9,500
  statement: >-
    Business #1 makes $100 per sale ($50 profit) and business #2 makes $10,000 per sale ($9,500 profit), so #1 needs 190 sales to match one sale of #2. Offer the same 190 people the $10,000 offer instead and you would likely close about 5%: 5% x 190 = 9.5 sales, 9.5 x $9,500 = $90,250 against $9,500 — 9.5x as profitable on the same advertising, with nine or ten clients to serve instead of 190.
  why: >-
    Even at far lower volume the high-value offer makes far more when normalised, and life is easier with a tenth of the clients.
  applies_when: >-
    Only with something very valuable to provide (a Grand Slam Offer) and a selling process that demonstrates that value.
  demonstrates: >-
    The arithmetic behind premium promotions.
  anchor: >-
    If you spoke to those same 190 sales that business #1 closed and offered them all the $10,000
  source: >-
    100m-series-lost-chapters.md, Premium Promotions, lines 608–636
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:616"
- id: C-lost-chapters-011
  type: case
  name: >-
    Copy specificity: working hard against cleaning the bathrooms yet again
  statement: >-
    A two-second rewrite inside the premium-offer dialogue: instead of saying working hard in your business, say cleaning the bathrooms yet again. The dialogue carries the same move to the lemonade example — the prospect must understand why the lemonade has to come from our orchards with our alkalinity profile, or they will just think we are overpriced Minute Maid.
  why: >-
    Specificity is what gives copy its edge; unless you know the real world of your avatar it is hard to get them to bite without a compelling offer and great copy — and free and discount offers give more margin for error on the copy because the offer pushes people on the fence over the edge.
  applies_when: >-
    Leading with a premium offer, where there is no discount to carry weak copy.
  demonstrates: >-
    Con #2 of premium offers — you must be a good copywriter and understand your avatar well.
  anchor: >-
    example: I wouldn’t say “working hard” in your business, I’d say “cleaning the bathrooms
  source: >-
    100m-series-lost-chapters.md, Premium Promotions, lines 725–749
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:734"
- id: C-lost-chapters-012
  type: case
  name: >-
    The penny gap
  statement: >-
    Researcher Dr Dan Ariely showed that 9x more people would take a free Hershey kiss than one sold for a penny — the same move as lowering a price from $0.01 to free and getting 9x the leads. The author adds that getting a page to convert on a $1 offer versus a free offer can be a landslide of a difference.
  why: >-
    Free is something for nothing, or value in advance, which is why it is the most powerful offer of all time and will never expire.
  demonstrates: >-
    Why free, not cheap, is the front end that maximises lead volume.
  anchor: >-
    demonstrated something he called the “penny gap” Basically, he showed that 9x more people
  source: >-
    100m-series-lost-chapters.md, Free Promotions, lines 812–818
  confirmations: 1
  authors_caveat: >-
    Attribution: the penny gap is Dr Dan Ariely's, named in the text.
  anchor_at: "100m-series-lost-chapters.md:814"
- id: C-lost-chapters-013
  type: case
  name: >-
    The newspaper offer nobody answered
  statement: >-
    A famous marketer ran an offer in the newspaper every few years reading, for every $100 you give me I will give you $1,000 back, with a phone number. No one ever responded. He ran it to illustrate believability: the offer is amazing, and it was so good it was unbelievable.
  why: >-
    A free offer that fails tells you one of three things — they don't want your thing, they don't believe you, or they aren't seeing it because you are fishing in the wrong pond. This test isolates the second.
  demonstrates: >-
    The three reasons a free offer fails; why a crazy offer must answer the question Why?
  anchor: >-
    would run an offer in the newspaper that said, “For every $100 you give me I will give you
  source: >-
    100m-series-lost-chapters.md, Free Promotions, lines 839–843
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:840"
- id: C-lost-chapters-014
  type: case
  name: >-
    90% off with and without the reason
  statement: >-
    Going out of business, all products must go in 30 days is a very good reason to have 90% off all products; saying only 90% off all products would likely not get the same response.
  why: >-
    Whenever you give a crazy free or discounted offer away you will always have to answer the next question — Why? Give a good enough reason and people will believe you.
  applies_when: >-
    The reason has to be true.
  demonstrates: >-
    The reason-why that makes a big discount believable.
  anchor: >-
    products must go in 30 days” is a very good reason to have “90% off all products” If you
  source: >-
    100m-series-lost-chapters.md, Free Promotions, lines 843–849
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:845"
- id: C-lost-chapters-015
  type: case
  name: >-
    Free Money Math: 500 leads half qualified against 200 leads 80% qualified
  statement: >-
    Campaign #1 spends $1,000 on ads and gets 500 leads, half unqualified (250) and half qualified (250). Campaign #2 spends the same $1,000 and gets 200 leads, 80% qualified (160) and 20% unqualified (40). The team feels better about #2, but on pure dollars and cents #1 is better.
  why: >-
    The higher volume is what you want, with friction skimming the cream off the top; that is how the power of free is harnessed, provided the free thing does not overextend you.
  demonstrates: >-
    Judging a free front end on total qualified leads rather than on lead quality percentages.
  anchor: >-
    Which campaign was better? Our team may feel better about #2, but according to
  source: >-
    100m-series-lost-chapters.md, Free Promotions, lines 1003–1026
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1023"
- id: C-lost-chapters-016
  type: case
  name: >-
    Four split tests of free against premium offers
  statement: >-
    Four independent split tests of free versus premium offers, each across 10 representative markets, found the gyms' closing percentage identical — 10 free respondents closed at the same rate as 10 non-free respondents, with no advantage in close rate or average ticket size for non-free. What differed was volume and lead cost: going from a non-free to a free front end most times cut lead costs by five times or more.
  why: >-
    It kills the objection that free brings freebie seekers who are not your ideal customer; the close rate does not move, only the cost per lead.
  demonstrates: >-
    The Free Brings Broke People Myth.
  anchor: >-
    We’ve run four independent split tests of free versus premium offers Each test had 10
  source: >-
    100m-series-lost-chapters.md, Free Promotions, lines 1039–1052
  confirmations: 1
  authors_caveat: >-
    The author states the same tests, run four separate times, as the reason discount leads only feel easier to sell: a good salesman sells the same percentage of free and non-free leads when funnel and sales environment are the same (Discount Promotions, lines 1241–1251).
  anchor_at: "100m-series-lost-chapters.md:1042"
- id: C-lost-chapters-017
  type: case
  name: >-
    Four Ways To Display Discounts on one lemonade bundle
  statement: >-
    One promotion — a first week of an ultimate lemonade bundle normally $210, offered at $29 — written four ways: percentage off (New Client Special, 87% off first visit); absolute amount off ($181 Off First Week, normally $210); relative equivalent off (Save A Steak Dinner, stated negatively, or Less Than Going Out To Lunch, stated positively); and simply the discounted price ($29 New Client Special).
  why: >-
    People respond differently to the same discount displayed differently, so cycling through all four shows which resonates in your audience; multiple winners give you more bullets in the chamber when a promotion fatigues.
  applies_when: >-
    Whether the offer is premium or high volume, its price often informs which display makes most sense.
  demonstrates: >-
    Four Ways To Display Discounts.
  anchor: >-
    a) Absolute Amount Off: “$181 Off First Week” (Normally $210)
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, lines 1113–1154
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1128"
- id: C-lost-chapters-018
  type: case
  name: >-
    The $19 heavy metals test into a $2,100 detox
  statement: >-
    A two-step sale: give away a heavy metals test consultation for $19, then upsell the prospect into a $2,100 ten-week detox plan when you meet. The flow is written out as ad, opt-in, phone call for the $19 promo with the appointment set, show up for the $19 appointment, get value, schedule a follow-up appointment for the $2,100 treatment program sale, show up at the second appointment and be sold.
  why: >-
    Taking the card on the first small transaction means the upsell can be closed with do you want to use the card on file — the author cites Amazon's one-click purchasing and Disney's money wristbands as businesses eliminating the same friction because they know they sell less with it.
  demonstrates: >-
    Discount offers as the front end of a two-step sale; card on file makes the upsell smooth.
  anchor: >-
    An example of a two-step sale would be us giving away a heavy metals test consultation
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, lines 1294–1312
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1299"
- id: C-lost-chapters-019
  type: case
  name: >-
    Proprietary 5 min Appointment Method
  statement: >-
    Rather than give away the doctor's time on a first visit, fix the first visit operationally so a front desk admin or assistant handles it — the prospect comes in for braces, fills out all the required information, has X-rays taken, applies for financing pre-approval and everything else that needs doing; the follow-up appointment is then set for the sale, and a card can be closed in person for a no-show fee. The doctor may squeeze in for five minutes to say hello and set up the in-depth appointment where the treatment plan is recommended and sold.
  why: >-
    It spends the doctor's time only on the most qualified candidates, eliminates the cost of no-shows, pre-qualifies everyone and puts them in the best position to say yes next time; opening appointments all day instead of a tiny new-patient window improves the percentage who schedule more than almost anything else.
  applies_when: >-
    Services where the time or cost of the individual delivering is real, such as a doctor's time.
  demonstrates: >-
    Using a discount front end to eliminate no-shows without giving away expensive fulfilment time.
  anchor: >-
    I call this strategy the Proprietary 5 min Appointment Method (feel free to
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, lines 1334–1363
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1353"
- id: C-lost-chapters-020
  type: case
  name: >-
    Three CAC calculations: outreach, content marketing, paid ads
  statement: >-
    Outreach — $3,000 emailer plus $200 software plus $800 of commissions on eight sales at $100 = $4,000 over 8 customers = $500 CAC. Content marketing — two media staff at $5,000 each plus $1,000 of commissions on ten sales = $11,000 over 10 customers = $1,100 CAC. Paid ads — $4,000 media buyer plus $20,000 media spend plus $1,000 tracking software plus $10,000 of commissions = $35,000 over 10 customers = $3,500 CAC.
  why: >-
    Most entrepreneurs report only ad spend per customer, treat content leads as free, or leave the outbound team out and count only commissions; a $1,000 sale they thought cost $200 really costs $500, and in some businesses that gap is the difference between $1,000,000 and $10,000,000 per month.
  applies_when: >-
    Calculate CAC monthly and by channel — when the author's firm invests in a company, half the time a full acquisition diagnostic finds one channel doing significantly better, and they do more of it.
  demonstrates: >-
    Cost to Acquire a Customer includes advertising dollars, payroll to a media buyer, creative team, software, sales commissions and salaries.
  anchor: >-
    $3,000 Emailer + $200 Software + $800 Commissions (8 x $100) = $4,000
  source: >-
    100m-series-lost-chapters.md, Cost To Acquire a Customer = CAC, lines 1591–1655
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1603"
- id: C-lost-chapters-021
  type: case
  name: >-
    Gross profit for a product and for a service
  statement: >-
    Product: a widget sells for $100 and costs $20 to make and ship, so gross profit is $80. Service: ten packages sold at $1,000 each with one employee paid $2,000 to service them gives total GP of $8,000 and $800 per customer.
  why: >-
    Gross profit is what is left after the cost of delivering the thing, not net profit; the more you make per customer, the more you can spend to get them.
  demonstrates: >-
    CFA Lever #2 — make them worth more by raising lifetime gross profit.
  anchor: >-
    Service Example: You sell 10 service packages at $1,000 each You pay one
  source: >-
    100m-series-lost-chapters.md, The Three Levers of CFA, lines 1524–1536
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1533"
- id: C-lost-chapters-022
  type: case
  name: >-
    LTGP for a service business, back of napkin
  statement: >-
    One account rep per 10 clients, clients paying $3,000 per month, reps costing $6,000 per month: $30,000 of monthly revenue per rep minus $6,000 = $24,000 gross profit, an 80% gross margin, so $2,400 gross profit on a single customer. Divided by 5% churn that gives an LTGP of $48,000. For a physical product the same two steps multiply instead: the source's worked line reads gross profit $80 times four average transactions.
  why: >-
    A CRM often does not report lifetime transactions, and when it does the data is frequently wrong, so the author gives back-of-napkin methods: multiply gross profit by transactions for products, divide gross profit by churn for recurring businesses.
  demonstrates: >-
    The three LTGP steps — gross profit, average transactions or churn, then combine.
  anchor: >-
    Cost = $24,000 My gross margin is $24,000/$30,000 = 80% So my gross profit on a
  source: >-
    100m-series-lost-chapters.md, Lifetime Gross Profit (LTGP), lines 1708–1784
  confirmations: 1
  authors_caveat: >-
    The author calls lifetime transactions always an estimate, since customers keep buying and lifetime transactions rise as a business gets older.
  anchor_at: "100m-series-lost-chapters.md:1717"
- id: C-lost-chapters-023
  type: case
  name: >-
    Churn on 100 customers, and the mistake that follows
  statement: >-
    100 customers on the first of last month, 95 this month, difference five, so churn is 5 divided by 100 = 5%. The trap: signing up new clients in the same period does not change it — sign up zero or 1,000 and you still lost five of the original hundred, so churn is still 5%.
  why: >-
    Churn is the percentage of the original customers that leave between time periods, and it is the divisor of lifetime gross profit in a recurring business.
  demonstrates: >-
    LTGP Step Two for a recurring revenue business.
  anchor: >-
    between time periods So, if on the first of last month we had 100 customers and this
  source: >-
    100m-series-lost-chapters.md, Lifetime Gross Profit (LTGP), lines 1745–1771
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1748"
- id: C-lost-chapters-024
  type: case
  name: >-
    A 31-day payback period
  statement: >-
    A new customer produces $50 per month in gross profit and cost $100 to acquire. The first payment arrives day 1, returning $50 of the $100; the second arrives on day 31, returning the rest. The payback period is therefore 31 days.
  why: >-
    Payback period is the time it takes to break even on what you spent to get a new customer — mathematically, when GP exceeds CAC.
  demonstrates: >-
    CFA Lever #3 — decrease payback period, because a customer who pays for themselves today lets you buy another tomorrow.
  anchor: >-
    $100 to acquire that customer You get your first payment day 1, so you get $50 of your
  source: >-
    100m-series-lost-chapters.md, Payback Period = PPD, lines 1804–1810
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1808"
- id: C-lost-chapters-025
  type: case
  name: >-
    30 Day Cash on a credit card, in five steps
  statement: >-
    Day 0, borrow $40 to acquire the first customer. Days 1–30, make $50 in revenue at $10 cost to fulfil, leaving $40 gross profit. Day 30, repay the $40 so the balance is zero, and re-borrow $40 for another customer. Days 30–60, pocket another $40 from the first customer. Day 60, the second customer's $40 repays the debt again — two customers paying $80 gross profit per month and zero debt.
  why: >-
    Thirty days is typically the length of interest-free financing any business can get, the credit card being the prime example; if 30D Cash exceeds CAC you acquire customers with other people's money and clear the card each month.
  demonstrates: >-
    30 Day Cash (30D Cash) — the gross profit extracted from a new customer in their first 30 days.
  anchor: >-
    1) Day 0: We borrow $40 to acquire our first customer
  source: >-
    100m-series-lost-chapters.md, Payback Period = PPD, lines 1929–1962
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1934"
- id: C-lost-chapters-026
  type: case
  name: >-
    Normal Lemonade Business, day by day
  statement: >-
    A channel that acquires customers at $20 CAC with a two-month payback and $40 of LTGP: day 0 minus $20 on marketing, day 30 minus $12, day 60 minus $4, day 90 plus $4 (the first money made), day 120 plus $12, day 150 plus $20 and then the client cancels. Cash does not come back until month three while the business still has to pay rent, utilities, software and the owners.
  why: >-
    It shows why this very common shape of business is hard to grow: how much you make (LTGP), how fast you make it (payback period) and what it costs to make it (CAC) together decide whether the business is wonderful.
  demonstrates: >-
    The expensive customer problem — the three levers acting together on cash flow.
  anchor: >-
    Day 30 (-$12): We make $10, $8 in gross profit, but it goes towards recouping CAC
  source: >-
    100m-series-lost-chapters.md, Payback Period = PPD, lines 1980–2034
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2002"
- id: C-lost-chapters-027
  type: case
  name: >-
    Wonderful Lemonade Business, day by day
  statement: >-
    Same prices and margins, but CAC of $1 and a seven-day payback: day 0 minus $1; day 7 a customer pays $10 for $8 gross profit, covering CAC with $7 left; day 8 spend the $7 on marketing; day 14 seven customers at $1 each produce $56; day 15 hold at seven more customers rather than the 49 affordable; day 22 another seven and $105; day 37 the first renewal at $8; day 44 the next seven renew for $56; day 51 another $56, total $225. Total money taken out of pocket for marketing across the whole run: $1.
  why: >-
    With CAC low and payback fast, the first transaction's gross profit buys the next customers, and the business crowdfunds its own growth with customers' money rather than outside capital.
  demonstrates: >-
    Customer Financed Acquisition once CAC and payback period are attacked together.
  anchor: >-
    Day 14 ($56): We acquire seven more customers at $1 each Each pays $10 for a total of
  source: >-
    100m-series-lost-chapters.md, Payback Period = PPD, lines 2036–2126
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2074"
- id: C-lost-chapters-028
  type: case
  name: >-
    Twelve months at CFA Level 3
  statement: >-
    Put all extra profit back into getting customers at CFA Level 3 (gross profit at twice CAC within thirty days) and the table runs 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048 new customers per month — 4,095 customers in twelve months, of which only the first was paid for out of pocket.
  why: >-
    At twice CAC you can double the business every month; the customers finance the acquisition of the next customers, which is where the name Customer Financed Acquisition comes from.
  demonstrates: >-
    CFA Level 3.
  anchor: >-
    you would go from one lonely customer to… an army of 4,095 customers Best of all, you’d
  source: >-
    100m-series-lost-chapters.md, Levels of Customer Financed Acquisition, lines 2181–2202
  confirmations: 1
  authors_caveat: >-
    The author states that something else will eventually bottleneck growth and that this is fine — but the bottleneck should never be cash for getting customers.
  anchor_at: "100m-series-lost-chapters.md:2183"
- id: C-lost-chapters-029
  type: case
  name: >-
    The $50,000 consulting day: twice the sales, 56x less profit
  statement: >-
    A client on pace for about $3M a year, profitable but unable to scale, opened with the line that he sells twice as many people per month yet makes 56x less profit. Reviewing his numbers showed marketing and sales were fine; the issue was that he did not make enough per customer — one offer that was not irresistible, no upsell and no continuity — so it cost him about 50% more to acquire a customer while the author made ten times more from the same customer.
  why: >-
    LTGP is the arms race of business: the higher that number, the more you can spend to acquire, the more damage you can inflict on competitors, and eventually you can starve them out of the marketplace.
  demonstrates: >-
    Diagnosing a scaling problem as a back-end problem rather than a marketing or sales problem.
  anchor: >-
    “Wait, so you sell twice as many people as I do every month, but you make 56x more
  source: >-
    100m-series-lost-chapters.md, Back End: The value Grid, lines 2286–2308
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2287"
- id: C-lost-chapters-030
  type: case
  name: >-
    The first value grid: $600 from ten prospects, and $0 per lead
  statement: >-
    From 10 prospects, eight take a simple trial offer and three convert on the back end to a paid offer, generating $600 in total — $60 affordable per show, and $75 collected per trial in the first 30 days, which is the 30D Cash / 30D LTV. Putting $600 on a credit card to buy ads for 50 leads to get 10 in the door means breaking even at $12 per lead; but working and selling those leads realistically costs $600–$1,000 in labour, so at $600 of labour the business can now pay $0 per lead.
  why: >-
    The author's reading: it never costs too much or too little to acquire customers, it just costs what it costs — the job is to design the business so the same customers are worth more.
  demonstrates: >-
    The value grid as a tool for seeing 30D Cash, lifetime value and what you can afford per lead.
  anchor: >-
    of illustration That would mean that I would now only be able to pay $0/lead, because all
  source: >-
    100m-series-lost-chapters.md, Back End: The value Grid, lines 2361–2380
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2375"
- id: C-lost-chapters-031
  type: case
  name: >-
    The same business after stacking: 30D Cash from $75 to $1,763
  statement: >-
    The second grid is the same type of business with a high-ticket front-end offer, downsells, and a series of upsell offers across the first 30 days; not everyone takes every offer but the percentages add up. Top example 30D Cash $75, bottom example 30D Cash $1,763 — a revenue difference of about 14–15x, which in the real world means a competitor who can pay $100 per lead is up against a business that could pay $1,500 per lead and stay just as profitable.
  why: >-
    An upsell framework like this gives enormous margin for error on marketing: with a series of Grand Slam Offers raising lifetime value you can crush competitors even with mediocre marketing.
  demonstrates: >-
    Advanced offer stacking measured through the value grid.
  anchor: >-
    Look at the difference in those numbers between the top example (30D Cash = $75) and
  source: >-
    100m-series-lost-chapters.md, Back End: The value Grid, lines 2386–2416
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2393"
- id: C-lost-chapters-032
  type: case
  name: >-
    Affiliate commissions on a small business owner's take-home
  statement: >-
    A small business owner takes home $35,280 a year off $282,240 of revenue. Adding $2,000 a month in retail sales commissions looks small next to the $23,520 the business makes selling services, but it moves take-home income from $35,280 to $59,280.
  why: >-
    Most businesses refer out lots of revenue by recommending complementary products and services; commissions are pure profit and go straight to the bottom line. The author reports having made more than $3,000,000 in affiliate commissions directly.
  applies_when: >-
    When looking for revenue that adds little or no cost in time, money or complexity; if what you refer out makes even more money, it is sometimes worth buying or incorporating that business.
  demonstrates: >-
    Identify Adjacent Customer Needs/Opportunities — monetising need streams through affiliate relationships.
  anchor: >-
    For example, take a small business owner who makes $35,280 per year take-home off of
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, lines 2444–2470
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2464"
- id: C-lost-chapters-033
  type: case
  name: >-
    Free Onboarding paid for by affiliate links
  statement: >-
    Adding one extra call to the onboarding process for new clients paid for the entire onboarding and customer support team: clients appreciated the extra support, and the call guaranteed every customer clicked the author's affiliate links when signing up for the solutions they needed. Only the first month of the added role came out of pocket; after that the affiliate commissions paid for the team.
  why: >-
    These little tricks add up to an unbeatable business while providing unmatched service to customers.
  demonstrates: >-
    Adding revenue that costs almost nothing in operations, inside a step the customer already goes through.
  anchor: >-
    I was able to pay for my entire onboarding team and customer support team
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, lines 2473–2481
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2474"
- id: C-lost-chapters-034
  type: case
  name: >-
    Sale #1, the service downsell ladder
  statement: >-
    Offer the high-ticket solution first; on a no, move to a half-down version of the same offer with a different payment plan; then a quarter down with a slightly higher payment plan over time; then a shorter program at the quarter payment with no payment plan; then a free trial with the card on file and a commitment to consume the service; and if they still say no, a complimentary nutrition orientation 24 to 72 hours later, where the next series of offers begins.
  why: >-
    Every prospect is advanced to the next stage even after a no, which gives another opportunity to provide value and monetise the person; layering offers with downsells is what makes the conversion process efficient and lets no dollar of spending power go to waste.
  applies_when: >-
    Selling in person or over the phone — one-on-one settings allow this effortlessly, selling off a page digitally does not.
  demonstrates: >-
    Up Front Cash inside the Ultimate Offer Stacking Process, with downsells at each step.
  anchor: >-
    customers will take that big ticket offer But if they say no, totally fine We transition to a
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, lines 2548–2560
  confirmations: 1
  authors_caveat: >-
    If they still say no after the last step, the author's reading is that they don't trust you and you need to work on sales — beyond the scope of the book.
  anchor_at: "100m-series-lost-chapters.md:2551"
- id: C-lost-chapters-035
  type: case
  name: >-
    Sale #2, the physical products downsell ladder at orientation
  statement: >-
    At the orientation, after individual support and value, sell a three-month bundle of a full stack of supplements solving the same main need a different way; on a no, offer one month on a subscription at a discount; on another no, cross out a handful of products and sell the essentials; on another, the one or two products they absolutely should take; then ask if they need help preparing food and sell meal plans from a food prep company you have a relationship with.
  why: >-
    It helps the customer get results, saves them time and makes the business money — the author's phrase is everyone wins; and people want the same problem solved in different ways.
  demonstrates: >-
    The Upsell Offer stage of the Ultimate Offer Stacking Process.
  anchor: >-
    main need…just in a different way If they said no, we would offer just a one-month supply
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, lines 2562–2572
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2566"
- id: C-lost-chapters-036
  type: case
  name: >-
    Product sales at orientation paying for one-on-one onboarding
  statement: >-
    The cash from products sold at orientation covered the payroll for onboarding every customer one-on-one; the trainers ended up making more per hour than they did taking personal training clients, so they were happy to do it, customers loved the added service, and the product sales alone still covered the entire cost of acquisition — advertising, commissions and payroll — most times. The contrast drawn is the operator down the street cutting costs and afraid to make more offers: worse-paid employees, so he cannot keep the best talent; worse service and less spend, so customers get worse results; less money, so he cannot expand or market as much.
  why: >-
    People like having problems solved for them in advance, so solve them and profit.
  demonstrates: >-
    Stacking an upsell into a fulfilment step so the step pays for itself.
  anchor: >-
    The cash I made from the products I sold at orientation covered my payroll to
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, lines 2575–2593
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2576"
- id: C-lost-chapters-037
  type: case
  name: >-
    Sale #3, the feedback meeting and the VIP upsell
  statement: >-
    A few weeks in, meet the customer as a Feedback meeting. If they are enjoying it, start with a high-ticket prepayment and downsell to plain continuity. If they are not, sell a higher level program with more support, offering to message them every morning and check in weekly, starting free today and crediting the entire cost of the first program to the VIP program because their experience was not the best.
  why: >-
    A feedback meeting gives information to improve, saves an unhappy customer, and provides an upsell opportunity — every problem is an upsell opportunity, and you simply turn around and sell the next Grand Slam Offer.
  demonstrates: >-
    The Continuity stage of the Ultimate Offer Stacking Process.
  anchor: >-
    opportunity “Oh, you feel like we haven’t given you enough support, then how would
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, lines 2595–2623
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2607"
- id: C-lost-chapters-038
  type: case
  name: >-
    The Ferrari presentation, taken apart
  statement: >-
    A conference talk titled How My Weird Niche Funnel is Making Me $17,137 Per Day…And How You Can Ethically Copy It In Under 10min Or Less opened by giving away the speaker's Ferrari to someone in the room, with an opt-in at a website to find out more, then taught the mechanism and showed the audience how to build it. The author's reading: opening with come buy my website designer for $2,000 would have sold no one, but sixty minutes in he estimates a third of the room would have taken out their credit cards.
  why: >-
    Buyers need to know enough about a product to buy, and the more expensive or complex it is the more information they need; a presentation gives a captive audience, enough time to explain and provide value, and lets you make the offer at the moment they are most motivated to take it.
  demonstrates: >-
    Free Presentations as an attraction offer — the offer lands at the end, not the start.
  anchor: >-
    If he had started with “Hey everyone, come buy my website designer for $2,000,” no
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, lines 2677–2733
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2698"
- id: C-lost-chapters-039
  type: case
  name: >-
    The free dinner, with its benchmark
  statement: >-
    A free dinner (Free XYZ Dinner, Free Neuropathy Dinner, Free Diabetic Dinner) gets people in the door; during the meal you present for 60 to 90 minutes, then offer a product that covers the cost of getting everyone there, ideally more; buyers are booked into individual appointments for a much higher ticket item. Benchmark: convert about a quarter of the room to the lower offer and at least a third of those to the higher one — a 100-person audience gives roughly 25 lower-offer buyers and about eight higher-offer buyers.
  why: >-
    The amount of time spent educating the consumer is directly related to the price and the amount of trust needed — the bigger the plane, the longer the runway.
  demonstrates: >-
    Free Education with Offer, and the benchmark that tells you whether the format is working.
  anchor: >-
    a 100-person audience would have 25 or so people taking the lower offer and eight or so
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, lines 2750–2761
  confirmations: 1
  authors_caveat: >-
    Benchmarks are as of the source, 2025.
  anchor_at: "100m-series-lost-chapters.md:2760"
- id: C-lost-chapters-040
  type: case
  name: >-
    Free 5 Day Challenge named for eight industries
  statement: >-
    Four live 60–90 minute presentations Monday through Thursday, each breaking one core belief that prevents buying while giving usable content, with the offer made on Friday. The same format named per industry: Free Find Your Niche Entrepreneurship Challenge; Free Find Your First Real Estate Deal; Free 5 Day Buy A Business with $0 Down Challenge; Free 5 Day Make Your First High Ticket Sale; Free 5 Day Plateau Buster for weight loss; Free 5 Days To Freedom Challenge for addiction; Free 5 Day Pain Release Challenge; Free 5 Days to Get Unstuck Challenge for life coaching. Benchmark: convert 2 to 5% of those who sign up.
  why: >-
    It works for converting ice-cold audiences at both low and very high price points, and in the worst case you deliver real value and build goodwill with the marketplace even with people who never buy.
  demonstrates: >-
    Naming a free presentation offer after the prospect's outcome, one industry at a time.
  anchor: >-
    Business Flipping Opportunity: Free 5 Day “Buy A Business with $0 Down”
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, lines 2770–2795
  confirmations: 1
  authors_caveat: >-
    Benchmarks are as of the source, 2025.
  anchor_at: "100m-series-lost-chapters.md:2784"
- id: C-lost-chapters-041
  type: case
  name: >-
    Four freemium products and where each puts the wall
  statement: >-
    Dropbox gives free storage up to a point, then you pay. Spotify gives free music forever with ads, removed for a fee. Wistia gives free video uploads, then charges after a certain amount. Gmail gives free email, then asks you to upgrade for more inbox space or start having emails deleted — fear of loss makes you upgrade.
  why: >-
    The free thing must cost almost nothing to fulfil, provide continuous rather than one-time value, and not give away so much of the farm that nobody buys anything else; consumer versions limit use so that anyone using it regularly needs more.
  applies_when: >-
    Software and media businesses with close to 100% incremental margins; the author would not recommend the structure without investors and large capital.
  demonstrates: >-
    Freemium as an acquisition strategy — not a business model.
  anchor: >-
    Free email After a certain period, upgrade for more inbox space or start having your emails
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Freemium, lines 2963–3012
  confirmations: 1
  authors_caveat: >-
    The author calls freemium one of the most dangerous acquisition strategies and says he has seen it done incorrectly by really smart people more often than correctly; if it is your first rodeo, steer clear.
  anchor_at: "100m-series-lost-chapters.md:2977"
- id: C-lost-chapters-042
  type: case
  name: >-
    What a freemium customer really costs
  statement: >-
    True cost of acquisition under freemium is the cost of servicing a free customer divided by the percentage who upgrade: at a cost of $0.50 per month to service a free customer and a 1% upsell rate, CAC is $5 per month, so an average revenue per paid user of $15 per month or more leaves a profitable business that can grow.
  why: >-
    You still have the costs of doing business before you start to profit, so the conversion percentage and the servicing cost are what decide whether the free pool pays.
  demonstrates: >-
    The three freemium roadblocks — conversion too low, the free thing not worth telling people about, or fulfilment cost too high relative to paid revenue.
  anchor: >-
    example, if it costs you 05/mo to service a free customer, and you upsell 1% of customers,
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Freemium, lines 3014–3019
  confirmations: 1
  authors_caveat: >-
    The source file has lost the decimal points: the figures read 05/mo and 01 on the line.
  anchor_at: "100m-series-lost-chapters.md:3016"
- id: C-lost-chapters-043
  type: case
  name: >-
    The free car wash and the donation script
  statement: >-
    A car wash advertised Free Car Wash by the roadside; at the window the attendant pointed at the pricing chart and said the standard wash is 100% free but they are accepting donations on behalf of the staff to help the guys feed their families and get through this, that they would all be very appreciative, and that they accept cash, credit and Venmo — then shut up and said nothing. The author paid $20, more than the most expensive automated wash they charged for in normal conditions. His gyms took the scripting into their sales process during COVID and people who could not normally close got an average ticket of about $99, more than the average low-barrier offer.
  why: >-
    Goodwill, lots of new business and cash flow on a high-margin service at once; the purchase feels like funding something, which is a different feel from a normal transaction.
  demonstrates: >-
    Free Pick Your Price as an attraction offer, including the silence after the ask.
  anchor: >-
    “The standard wash is 100% free but we’re accepting donations on behalf of the staff to
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Pick Your Price, lines 3058–3084
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3067"
- id: C-lost-chapters-044
  type: case
  name: >-
    Pick Your Price with three rungs of bonuses
  statement: >-
    The same structure across five businesses: free lemonade cup, with hand-squeezed lemonade over $5, a pitcher to take home over $25 and three months of shipments over $99. Free machine car wash, with a wax over $30, a hand buff over $67 and the entire interior over $99. Free 21-day weight loss where most people pay $99, which adds a 1-1 call, over $199 adds the supplement handbook, and $499 adds a guarantee of 10lbs lost or credit towards any service. Free dental cleaning and free coaching follow the same shape, the $0 price on coaching coming only with group access.
  why: >-
    Bonuses at three levels of payment — small, medium, large — encourage people to pay something more than $0, while the basic level still has to be given free to anyone who will not pay.
  applies_when: >-
    The free thing must have low operational costs so staff are not burned out; the higher operational cost items are saved for the people who choose to pay. It does not work with a discount wrapper.
  demonstrates: >-
    Free Pick Your Price — a sliding scale with rungs rather than either-or, with no maximum.
  anchor: >-
    If you pick $99 we’ll give you an extra 1–1 call If you pay over $199 we will also
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Pick Your Price, lines 3092–3154
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3119"
- id: C-lost-chapters-045
  type: case
  name: >-
    The pick-your-price sequence: pre-frame, hard questions, then the card
  statement: >-
    Explain at the start of the sale that there is a pick-your-price setup, that staff are offering bonuses at different levels and that nobody is obliged to pay anything. Then hit the prospect with confrontational questions to test whether they are a long-term candidate — are you willing to change the way you do X, are you willing to stop doing Y, what if life gets busy, will you stop showing up, will you attend all of these appointments. At the end of the pitch, outline what they get at each level, ask which of Visa, Mastercard or another payment they prefer to use, then shut up; they take out their card and name their level.
  why: >-
    Declaring the pick-your-price frame up front avoids awkwardness at the end and earns the prospect's goodwill; the questions work as a mini-interview for commitment, for their good and yours, since the clients you want are the ones who willingly pay and are appreciative.
  demonstrates: >-
    Free Pick Your Price in the room — the pre-frame, the qualification and the close.
  anchor: >-
    you do X? Are you willing to stop doing Y? What if life gets busy, will you stop showing up? Will
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Pick Your Price, lines 3155–3183
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3173"
- id: C-lost-chapters-046
  type: case
  name: >-
    PAID VERSION of Pick Your Price: the art gallery price range
  statement: >-
    An art gallery put a price range on every piece and told buyers they could choose how much to support the artist — for example, this painting is between $149 and $299. The owner reported that most people pay more than the halfway point because they don't want to seem cheap or unsupportive.
  why: >-
    The author's reading: this version is half goodwill, half capitalism.
  demonstrates: >-
    A paid variant of the pick-your-price mechanism, where the floor is above zero.
  anchor: >-
    For example, “this painting is between $149 and $299”. I asked the owner how
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Pick Your Price, lines 3192–3198
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3195"
- id: C-lost-chapters-047
  type: case
  name: >-
    The no sale sale
  statement: >-
    A gym owner stopped escorting non-buyers out and instead handed them a USB drive with everything needed to do the program at home, absolutely free, then added an invitation to book a nutrition orientation on the house so they could see results. Almost 100% of the people who said no to membership took the orientation, where supplements were sold instead of workout programs; those people spent 50% more on supplements than his regular clients. He then ran the free USB as a front end, upselling an in-person version or ongoing supplement purchases.
  why: >-
    People want the same problem solved in different ways, so offering multiple ways to solve it gives more at-bats and turns every prospect into a sale; the sales team liked it because they help everyone who walks in.
  demonstrates: >-
    Free With Alternate Revenue Stream, used as a downsell and then as a primary offer.
  anchor: >-
    “To get you a head start, let’s book you for a nutrition orientation so you can see the
  source: >-
    100m-series-lost-chapters.md, Upsell Offer: Free With Alternate Revenue Stream, lines 3205–3241 (same play named at Back End: The value Grid, line 2401)
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3218"
- id: C-lost-chapters-048
  type: case
  name: >-
    Paired and independent upsells across four businesses
  statement: >-
    Storage gives a free month and pairs it with the lock for the unit, the only locks that fit their doors and unavailable anywhere else. A weight loss clinic gives a free 28-day program and at the nutrition orientation sells a $400 supplement package independently. A physical therapist gives four free treatments and sells orthotics, bands, braces, oils and athletic tape to maximise them. An agency coach coaches free indefinitely as long as you use their software, monetising on the software. The money model does not stop there: storage upsells boxes, bigger units and commitment; the weight loss clinic upsells continuity of service and supplements, done-for-you meals, bars and hormone treatment, and closes a card so the free service is also a Free Trial + Penalty.
  why: >-
    Effectiveness rests on how essential the prospect perceives the next thing to be — like the lock in the storage scenario — and on how seamless the upsell is; frictionless upsells of this kind can get take rates above 90%.
  applies_when: >-
    Give away something with low incremental costs, use a multi-step sales process, and make the next thing the natural next thing the prospect needs.
  demonstrates: >-
    Paired Upsell (thing A free in exchange for buying thing B) against Independent Upsell (thing A free, then encouraged to buy thing B).
  anchor: >-
    Paired Upsell: Do you want to buy a lock for your storage unit? (The only locks that fit our
  source: >-
    100m-series-lost-chapters.md, Upsell Offer: Free With Alternate Revenue Stream, lines 3255–3355
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3270"
- id: C-lost-chapters-049
  type: case
  name: >-
    The free real estate book and its five upsells
  statement: >-
    A real estate book given away free, with upsell #1 shipping cost, #2 the audio version, #3 deal contract templates, #4 training on where to find deals, and #5 how to find financing with no money. Each is a necessary requisite for succeeding with the strategies in the book.
  why: >-
    The hardest sale is the first sale — the opportunity vehicle, the book — and the rest of the upsells are the things the buyer will need along the journey.
  demonstrates: >-
    Free With Alternate Revenue Stream used as a front end, with the upsell stack built from the prospect's own next problems.
  anchor: >-
    outlined in the book The hardest sale is the first sale—the opportunity vehicle—the book
  source: >-
    100m-series-lost-chapters.md, Upsell Offer: Free With Alternate Revenue Stream, lines 3297–3307
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3306"
- id: C-lost-chapters-050
  type: case
  name: >-
    200+ weight loss clinics at $5 a month
  statement: >-
    A chain of more than 200 weight loss clinics grew on one offer: $5 per month of weight loss services for a year, if and only if the client used their supplements, bars, shakes and meal program, with the guarantee also contingent on that continued purchasing. They employed doctors and nurses and still gave the service away because the consumable products made so much.
  why: >-
    The insight the author draws: people were more willing to pay for the products than for the service from white-coated medical professionals — people love tangible goods, which he tries to incorporate with services wherever convenient.
  demonstrates: >-
    Free With Alternate Revenue Stream in its discount-wrapper variant — service at $5/mo instead of free, contingent on buying the products.
  anchor: >-
    services for a year if and only if the client used their supplements, bars, shakes,
  source: >-
    100m-series-lost-chapters.md, Upsell Offer: Free With Alternate Revenue Stream, lines 3308–3323
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3315"
- id: C-lost-chapters-051
  type: case
  name: >-
    What a free thing is worth when 80% take a $300 upsell
  statement: >-
    You make $0 on the free thing, but if 80% take a $300 upsell at 80% margins you are making $300 x 80% x 80% = $192 per free thing given away — and that is only the first upsell.
  why: >-
    Because the take rate is high and the money arrives up front, it is one of the easiest ways to generate cash early with little or no operational drag; the biggest benefit of a free front end of this kind is liquidating acquisition cost.
  demonstrates: >-
    Pricing a free front end by the liquidation it produces rather than by its own revenue.
  anchor: >-
    $300 upsell with 80% margins, then you know you are making $300 x 80% x 80% = $192
  source: >-
    100m-series-lost-chapters.md, Upsell Offer: Free With Alternate Revenue Stream, lines 3356–3365
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3360"
- id: C-lost-chapters-052
  type: case
  name: >-
    Thirty $99 sales against a hundred free plus eighty $300 upsells
  statement: >-
    Meet 100 people and sell 30 of them a $99 thing, or meet the same 100, give all 100 the free thing and upsell 80 of them on $300 of products. The second ends with more money and more customers, plus the referrals.
  why: >-
    Since most clients take the free offer, free plus upsell can make more money than selling something moderately priced up front, and it almost always gets a lot of volume in the door.
  applies_when: >-
    With cold traffic, close a trial plus a credit card on the first transaction and upsell the product on the second, or you will get a lot of no-shows.
  demonstrates: >-
    Free front end plus upsell against a mid-priced front end.
  anchor: >-
    people a $99 thing versus meeting with the same 100 folks and selling all 100 a free thing,
  source: >-
    100m-series-lost-chapters.md, Upsell Offer: Free With Alternate Revenue Stream, lines 3369–3387
  confirmations: 1
  authors_caveat: >-
    The author flags that a prospect who does not buy the upsell is unlikely to stay: it is the greatest predictor of back-end conversion, so that seemingly minor sale is a must-have.
  anchor_at: "100m-series-lost-chapters.md:3374"
- id: C-lost-chapters-053
  type: case
  name: >-
    Selling the continuity offer that did not exist yet
  statement: >-
    A customer called to buy the next thing sight unseen after making $55k in six weeks. The author probed for the bottleneck — semi-private training, supplements, churn, hiring, internal plays — found all of them missing, then asked whether the owner wanted to get out of the daily grind and scale a legit chain of gyms. He priced it as a way higher price with a longer stay, $42,000 per year for three years, and when the customer went silent added access before the first payment as a bonus. The customer did the arithmetic himself — $3,200 per month, 20% cheaper monthly than Gym Launch — and bought. The deliverable agreed on the call was to find the bottleneck and deliver a new play every two weeks.
  why: >-
    The author's problem was that a one-time licensing product could only be sold to a customer once, so continuity kept money coming in even when all the cash from the first purchase went into getting more customers.
  demonstrates: >-
    Downselling the upsell — raising price and term, then adding a bonus and letting the buyer reframe the price per month.
  anchor: >-
    “It’s…” punching numbers into my calculator “ $42,000 per year For three years ”
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, lines 3420–3457
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3448"
- id: C-lost-chapters-054
  type: case
  name: >-
    A new play every fourteen days
  statement: >-
    The continuity offer delivered one new money-making play every fourteen days, kept up for almost two years. Gym Launch's revenue went up more than 13X, from around $300,000 per month to around $4,000,000+ per month — not because more customers were sold but because they were given good reasons to keep paying.
  why: >-
    Customers will start any offer if it is made tasty enough, but they only stick if they have good reasons to: a good offer gets them to start, and good bonuses get them to stick.
  demonstrates: >-
    Recurring bonuses on top of a continuity product as the retention lever.
  anchor: >-
    it tasty enough But, they’d only stick if they had good reasons to So I gave them one…every
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, lines 3459–3471
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3467"
- id: C-lost-chapters-055
  type: case
  name: >-
    When and what, paired: six worked bonuses
  statement: >-
    Delayed one-time bonus, local service — stay four months in a row and become an advanced member, getting access to the Annual Customer Appreciation Palooza. Delayed recurring bonus — stay four months and on the fifth get VIP first-in-line access to in-demand timeslots. Milestone bonus, digital product — for every friend referred, one more module. Recurring bonus, consumables — a new dog treat, toy or book every month for staying a dog food customer; lifetime free bacon with every butcher box order, lost if you cancel. Continuous use physical — every 3,000 miles or every six months, free servicing on a car lease.
  why: >-
    Time to the first bonus extends the stay once, and continuing to give bonuses extends it more times; the when is a delay or a milestone, the what is a one-time bonus, a variable bonus or a lifetime upgrade.
  demonstrates: >-
    Pairing a when with a what to build stick into a continuity offer.
  anchor: >-
    What: Lifetime free bacon with every order (if you cancel, you lose it)
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, lines 3480–3550
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3543"
- id: C-lost-chapters-056
  type: case
  name: >-
    Telling customers the type of bonus and keeping the bonus a surprise
  statement: >-
    Gym Launch customers knew they would get a new play from the author every month, but the exact play was kept a surprise; the bonus sat on top of the licensing material they already had, which made it both recurring and valuable.
  why: >-
    Announcing the type rather than the item gives the business flexibility and makes the bonus more valuable; customers can only get excited enough to stay for a bonus they know exists, so they must be told — at signup, a year in, and right after each recurring bonus about the next one.
  demonstrates: >-
    How to tell customers about upcoming bonuses.
  anchor: >-
    bonus more valuable In the Gym Launch example, customers knew they would get a new
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, lines 3552–3562
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3559"
- id: C-lost-chapters-057
  type: case
  name: >-
    The Opener: opening a gym with 400+ recurring members
  statement: >-
    A grand-opening specialist for a billion-dollar gym franchise opens every location with 400+ recurring members or does not open. The offer: advertise a 14-day trial into a lifetime discount on the membership, offered only to members who sign up before opening — the founding member discount. His numbers: after the 14-day trial 80% sign up, so 500 trials give 400 billing on day 15 and a profit in month one, and most stick because they do not want to lose their lifetime discount.
  why: >-
    The discount lasts for life and the window to get it is short, so a lot of people want it; and because leaving means losing it, the same offer that attracts also retains.
  demonstrates: >-
    A Lifetime Discount used as an attraction offer, with urgency and a believable reason (grand opening).
  anchor: >-
    “We know our numbers—after the 14-day trial 80% sign up So if we get 500 trials, 400
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, lines 3641–3657
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3653"
- id: C-lost-chapters-058
  type: case
  name: >-
    Four lifetime discounts with their reason, urgency and scarcity
  statement: >-
    Recurring local service: retail $400/mo, 50% off retail for life, $200/mo, reason new location, urgency until we open, scarcity classes fill up. Digital product early access: retail $39/mo, $20 off retail for life, $19/mo, reason it will have bugs, urgency until we launch it, scarcity only taking on X for feedback. Recurring physical product: retail $19.99/mo, $14.99/mo for life, reason we want your feedback, urgency until a date, scarcity until this batch runs out. The alternate version of the same product: $5 off per month for life after you stay for five months, reason rewarding loyalty, no urgency and no scarcity.
  why: >-
    Customers take the offer now because they get value at a discount now, and they stick because if they leave they cannot get it back; urgency, scarcity and a believable reason for both make it work like magic.
  applies_when: >-
    A Lifetime Discount only works if you actually charge more when the offer ends, and you must still make a profit after the discount.
  demonstrates: >-
    Building a Lifetime Discount out of retail price, offer, discounted price, reason, urgency and scarcity.
  anchor: >-
    Offer: $5 off per month for life after you stay for five months
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, lines 3659–3758
  confirmations: 1
  authors_caveat: >-
    Lifetime Discounts come with a big fat warning to know your numbers: acquisition and delivery costs change, and a locked-in rate below those costs is trouble. Percentage off and dollars off stay flexible; a fixed price for life does not.
  anchor_at: "100m-series-lost-chapters.md:3746"
- id: C-lost-chapters-059
  type: case
  name: >-
    John the tanning king on which membership sticks longest
  statement: >-
    Asked which membership has the longest stick rate, the author guessed the cheapest one; the answer was the one where they pay the most up front. John's numbers: get someone to pay $100 to sign up and lower their rate from $18 to $10 a month, and you never lose that person — they will call before their card changes to keep the lower rate. They buy a lower rate and by doing so extend their stay by a ton.
  why: >-
    Paying more up front triggers the Sunk Cost Fallacy — people disproportionately keep investing in a choice they have already put time or money into. The author's note to self: the bigger the head, the longer the tail.
  demonstrates: >-
    Initiation fees as a retention device for continuity.
  anchor: >-
    $100 to sign up, and lower their rate from $18 to $10/mo, I’m never losing that person
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, lines 3824–3860
  confirmations: 1
  authors_caveat: >-
    The author flags the same bias as dangerous in yourself: unrecognised, it keeps you in partnerships, memberships, investments and gambling longer than you should be.
  anchor_at: "100m-series-lost-chapters.md:3837"
- id: C-lost-chapters-060
  type: case
  name: >-
    Waiving the initiation fee for a commitment, and what happens on cancel
  statement: >-
    The two options given to the prospect: pay $100 today and go month-to-month at $10/mo, cancelling whenever you like; or start today for $10 and commit to the year, in which case the $100 initiation fee is waived. If someone takes the second and then tries to cancel early, the line is absolutely, no problem, we just switch you to month-to-month — cover the $100 initiation fee we waived and we will switch you right over.
  why: >-
    With that bigger head the back end sticks: many will choose to finish out the contract rather than pay the steep fee.
  demonstrates: >-
    Using a made-up one-time fee, waived against commitment, to lengthen the customer's stay.
  anchor: >-
    either pay $100 today, then go into month-to-month at $10/mo, cancel whenever you like,
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, lines 3844–3855
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3846"
- id: C-lost-chapters-061
  type: case
  name: >-
    Owen's pitch: a discounted month plus an enrollment fee
  statement: >-
    A personal training manager pitched the author's gym: a self-sufficient team of trainers doing about $100,000 a month in PT sales, who would monetise the gym's dead space at no cost, get their own leads, not talk to the gym's customers, and ask only that the gym give those leads a discounted month up front while the team charged an enrollment fee paid straight to the closer as commission. The author declined the partnership over unvetted people representing his brand, but noted the structure — a discount plus a fee — which both attracted customers with the discount and liquidated commissions and acquisition costs through the fee.
  why: >-
    The author's objections were stated in the same terms: it would cost him time and attention and, most importantly, the goodwill he had accrued with his customer base.
  demonstrates: >-
    Discount + One-Time Fee, read off someone else's offer.
  anchor: >-
    And we charge an enrollment fee, which I just give to my guy as commission for the sale
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Discount + One-Time Fee, lines 3917–3940
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3931"
- id: C-lost-chapters-062
  type: case
  name: >-
    Discount + One-Time Fee, worked two ways
  statement: >-
    Any recurring service: offer 95% off the first month, or $1,900 off the first month, or the first month for $100 — they come in for $100 and are still charged a $1,900 setup fee, so they pay $2,000 in the first month and go straight into recurring at $2,000 thereafter. Any defined-end service: a 12-week program at $3,000 sold as $1,000/mo for three months with 88% off the first month ($120) plus a $1,000 setup fee, so they pay $1,120 first, then two payments of $1,000.
  why: >-
    The higher the one-time startup fee, the lower the churn — the higher the barrier to entry, the higher the barrier to exit; the fee also offsets acquisition costs and gets the customer invested. When people pay, they pay attention.
  applies_when: >-
    Especially where the customer has to do something for the result — send information, fill out forms, show up at set times, make selections, change behaviour.
  demonstrates: >-
    The four steps of creating a one-time fee: pick the name, the price, the reason why, then charge, discount or waive it.
  anchor: >-
    Monetization: They come in for the first month for $100, but still get charged a $1,900 setup
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Discount + One-Time Fee, lines 3950–4021
  confirmations: 1
  authors_caveat: >-
    Be clear about the reason for the one-time fee even though it is made up, and bring it up with every customer — you are doing the work, so tell them what it is for.
  anchor_at: "100m-series-lost-chapters.md:3956"
- id: C-lost-chapters-063
  type: case
  name: >-
    Two tanning memberships, two churn rates
  statement: >-
    In John's tanning empire, clients on a $100 sign-up fee with a $10/mo membership churned at next to nothing, while clients who signed up for $19 down and $19/mo churned at a higher rate.
  why: >-
    Made-up fees can be used to actively decrease churn and increase the prospect's investment, which helps them and you in the long run.
  demonstrates: >-
    The higher the one-time startup fee, the lower the churn.
  anchor: >-
    John told me that when his tanning empire had a $100 sign-up fee for a $10/mo
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Discount + One-Time Fee, lines 3972–3979
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3974"
- id: C-lost-chapters-064
  type: case
  name: >-
    $5,000 to start, $267 a month, two years of lifespan
  statement: >-
    A multi-million dollar online weight loss coaching business charges $5,000 to start and only $267 per month afterwards; its average client lifespan is more than two years, against a normal fitness client's four months. If they leave and want to come back, they pay the start fee again.
  why: >-
    The large up-front sum gets the client invested in the process and makes leaving almost insane — which matters most when the client has to do part of the work to get the result they were sold.
  demonstrates: >-
    A massive disparity between setup fee and recurring fee as a retention structure.
  anchor: >-
    to start and only $267/mo thereafter His average client lifespan is more than two years
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Discount + One-Time Fee, lines 3985–3998
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3987"
- id: C-lost-chapters-065
  type: case
  name: >-
    The same $5,000,000 business, with and without you in it
  statement: >-
    Scenario #1: a business making $5,000,000 in revenue and $2,000,000 in profit that requires you to work around the clock — a high-paying job, and worth little to anyone else, because a business that only makes money with you in it is a bad investment. Scenario #2: the same $5,000,000 and $2,000,000, but the business runs without you — you get your time back, and the $2,000,000 of annual profit, especially if it is climbing, could easily be worth $10,000,000+ right now. The business went from almost zero value to $10,000,000 of value.
  why: >-
    If an asset makes millions without you, somebody else could use it to make millions without them, which is what makes it a good investment and what investors buy. You get rich from what you make, you become wealthy from what you own.
  demonstrates: >-
    Why employees make you wealthy — turning a liability that relies on you into an asset you can rely on.
  anchor: >-
    it’s climbing, could easily be worth $10,000,000+, right now So your business went from
  source: >-
    100m-series-lost-chapters.md, SECTION D: EXPANDED EMPLOYEES CHAPTER, lines 4113–4132
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4130"
- id: C-lost-chapters-066
  type: case
  name: >-
    The cost of a lead-getting employee, worked through to LTGP:CAC
  statement: >-
    Total payroll divided by total engaged leads gives cost per engaged lead: $100,000 over 1,000 leads is $100 per engaged lead. If one in ten engaged leads becomes a customer, CAC is $1,000; at an LTGP of $4,000 that is an LTGP:CAC of 4:1. The author's own figure at the time of writing: about 30,000 engaged leads a month at Acquisition.com with no paid ads and no outreach, from a content team costing about $100,000 a month — roughly $3.33 per engaged lead in payroll.
  why: >-
    Excluding paid media, the cost of advertising with employees is almost entirely what you pay them to do it, so payroll against engaged leads is the whole calculation; you are profitable as long as you make more per lead than that.
  demonstrates: >-
    Calculating returns from lead-getting employees, and the rule that total acquisition cost should be at most a third of lifetime profit.
  anchor: >-
    it costs me roughly $3 33 per engaged lead ($100,000 / 30,000 leads) in payroll to generate
  source: >-
    100m-series-lost-chapters.md, SECTION D: EXPANDED EMPLOYEES CHAPTER, lines 4475–4519
  confirmations: 1
  authors_caveat: >-
    Figures are as of the source, 2025.
  anchor_at: "100m-series-lost-chapters.md:4497"
```
