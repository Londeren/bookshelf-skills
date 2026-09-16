# Улов фазы 1 — $100M Series: Lost Chapters (2025) with $100M Leads: 2 Bonus Chapters (2023) as a second copy of Section A (ярус 2), тип D: антипаттерны и границы

Группа `tier2-lost-chapters`, слаг `lost-chapters`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **87** (экстрактор вернул 87, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-series-lost-chapters.md` | 1–4810 | 6 | 86 |
| `100m-leads-bonus-chapters.md` | 1–568 | 1 | 1 |

## Как собран файл

Экстрактор D (Antipatterns and boundaries) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-lost-chapters.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-lost-chapters-D.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: D-lost-chapters-001
  type: antipattern
  name: >-
    Selling to anyone who does not meet the ideal customer requirements
  statement: >-
    Keeping on selling to prospects who fail your stated customer requirements after you have defined the avatar, instead of stopping and being up front about the requirements in all advertising.
  why: >-
    Spelling the requirements out repels the bad customers and attracts the good ones; keeping the bad ones in the funnel defeats the avatar work.
  applies_when: >-
    Step 4a of the avatar process, once the survey has shown what the top 20 percent have in common.
  anchor: >-
    and attract the good ones Stop selling anyone who does not meet your
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, line 289
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:289"
- id: D-lost-chapters-002
  type: antipattern
  name: >-
    Anyone with a pulse and a credit card
  statement: >-
    Accepting every buyer who can pay, rather than selectively pursuing and catering to the highest value customers.
  why: >-
    It forces high customer churn, high costs of acquisition, low retention rates, lower satisfaction scores and generic advice; the same market with different customer segmentation produced 70x less profit for the competitor.
  anchor: >-
    The difference They accepted anyone with a pulse and a credit card As a result, they
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, line 378
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:378"
- id: D-lost-chapters-003
  type: antipattern
  name: >-
    Cutting qualification steps to get more volume
  statement: >-
    Panicking about lead volume and removing steps from the buyer journey to get more leads.
  why: >-
    Every time the author removed qualification steps the lead volume increased but the business made less money; the fix was merging marketing and sales into one acquisition department.
  authors_caveat: >-
    The goal is the optimal number of steps for the highest return on advertising over the long haul, not the maximum number of steps.
  anchor: >-
    every time we removed qualification steps, our lead volume increased, but we made less
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, line 390
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:390"
- id: D-lost-chapters-004
  type: antipattern
  name: >-
    The business as a widget to be sold to as many people as possible
  statement: >-
    Thinking of the business as a widget to be sold to as many people as possible instead of seeing it holistically through the ideal buyer journey.
  why: >-
    The author names it as how small newbie entrepreneurs think; he would rather pay $5,000 to acquire $45,000 than $1,000 to acquire $5,000.
  anchor: >-
    rather than as a widget to be sold to as many people as possible The ladder is how small
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, line 403
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:403"
- id: D-lost-chapters-005
  type: rule
  name: >-
    Narrowing costs revenue in the short term
  statement: >-
    Expect to serve fewer customers and to see a short-term decrease in revenue when you narrow the avatar, and make the long-term call anyway.
  why: >-
    The cost of change shows up immediately while the higher retention and profitability show up over the long haul.
  boundary: >-
    The author states this as the cost of his own method: narrowing the avatar reduces the number of customers served in the short term and may reduce revenue because of the cost of change.
  anchor: >-
    may mean a short-term decrease in revenue (due to the cost of change) But over the long
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, line 415
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:415"
- id: D-lost-chapters-006
  type: rule
  name: >-
    What To Do If You Have No Customers - Start With What You Know
  statement: >-
    With no customers to survey, start with the industry you know the most about, create a narrow target and serve them first, and rerun the customer analysis once you have customers to survey.
  why: >-
    There is a lot of in-depth knowledge that takes time to learn, and most people have some inside knowledge from friends, family or past jobs.
  boundary: >-
    The four-step survey process requires existing customers; this is the author's stated substitute for a business that has none.
  anchor: >-
    the most. Create a narrow target, then serve them first. Don’t get fancy. Start
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, Pro Tip, line 327
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:327"
- id: D-lost-chapters-007
  type: antipattern
  name: >-
    The cart before the horse
  statement: >-
    Figuring out monetization before generating demand, instead of generating demand first and working out how to make money on it afterwards.
  why: >-
    The author's order is Get Flow, Monetize Flow, Then Add Friction; he keeps the front end as low as possible to keep lead flow cranking.
  anchor: >-
    how to make money on it I feel like too many people try to put the cart before the horse
  source: >-
    100m-series-lost-chapters.md, Section A: Attract, Get Flow Monetize Flow Then Add Friction, line 556
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:556"
- id: D-lost-chapters-008
  type: antipattern
  name: >-
    A promotion that changes the Grand Slam Offer
  statement: >-
    Letting a free or discount promotion change the underlying Grand Slam Offer instead of wrapping it.
  why: >-
    A promotion is wrapping paper: what is inside stays the same and only the attractiveness to a cold audience changes.
  anchor: >-
    Important: The point of creating a promotion is to enhance your Grand Slam Offer, not
  source: >-
    100m-series-lost-chapters.md, Section A: Attract, line 567
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:567"
- id: D-lost-chapters-009
  type: rule
  name: >-
    If I Lost Everything And Had To Start Over
  statement: >-
    Do not lead with a premium offer when starting over or starting out; add a free or discount money model first, prove results, then restructure to premium.
  why: >-
    Reputation is what lets you drop the free or discount wrapper later; in the beginning the wrapper is essential for most.
  boundary: >-
    Premium offers as a standalone front end are for businesses that already have reputation, volume and a bearable cost of acquisition; if you are just starting out, or your volume is not high enough, or your cost of acquisition is higher than you can bear, wrap the premium offer.
  anchor: >-
    If I needed to make money, or make a business owner money, I would not start with
  source: >-
    100m-series-lost-chapters.md, Premium Promotions, lines 638, 805-807
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:638"
- id: D-lost-chapters-010
  type: rule
  name: >-
    Premium offers need a proven process or cash to build one
  statement: >-
    Lead with premium offers only if you already have a proven conversion process end-to-end or cash set aside to work one out.
  why: >-
    Each opportunity costs so much more that there is less room for error, and it takes time to get the sales process down when starting out.
  boundary: >-
    The author's stated precondition for a premium-led offer: a proven end-to-end conversion process, or a decent amount of money to burn learning.
  anchor: >-
    we want to lead with premium offers, we should already have a proven process or have some
  source: >-
    100m-series-lost-chapters.md, Premium Promotions, Cons #1 and #3, lines 759, 712-724
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:759"
- id: D-lost-chapters-011
  type: rule
  name: >-
    Premium as the second offer only works after demonstrated value
  statement: >-
    A premium offer placed as the second offer after a free offer only works if value was demonstrated in the first offer.
  boundary: >-
    The author's explicit condition on layering premium behind free.
  anchor: >-
    work well as the “second” offer you give after a free offer. But they'll only work if you demonstrated
  source: >-
    100m-leads-bonus-chapters.md, Premium Promotions, line 169 = Lost Chapters line 657
  confirmations: 1
  anchor_at: "100m-leads-bonus-chapters.md:169"
- id: D-lost-chapters-012
  type: rule
  name: >-
    Premium offers demand copy built on a known avatar
  statement: >-
    Do not lead with a premium offer in a market whose avatar you do not know well, because without specificity the copy cannot make them bite.
  why: >-
    Specificity is what gives copy its edge; free and discount offers give more margin for error on copy because the offer can push people on the fence over the edge.
  boundary: >-
    A new market whose inner workings, deep desires, fears and everyday struggles you do not yet know is the case where the premium wrapper fails and the free or discount wrapper is needed.
  anchor: >-
    yet again ” Specificity is what gives copy its edge Unless you know the real world of your
  source: >-
    100m-series-lost-chapters.md, Premium Promotions, Cons #2, line 736
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:736"
- id: D-lost-chapters-013
  type: antipattern
  name: >-
    Least Efficient Way to Capture a Marketplace
  statement: >-
    Using a straight premium offer when the goal is volume or market capture.
  why: >-
    A straight premium offer has to hit a lot of eyeballs before getting a bite: the ads go to more people for a smaller volume of results, a more valuable result but lower volume nonetheless.
  anchor: >-
    You: If we are looking for volume, a straight premium offer is going to have to hit a lot
  source: >-
    100m-series-lost-chapters.md, Premium Promotions, Cons #4, line 770
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:770"
- id: D-lost-chapters-014
  type: antipattern
  name: >-
    Three reasons a free offer fails
  statement: >-
    Reading a failed free offer as proof that free does not work, instead of as one of three diagnoses: they do not want your thing, they do not believe you, or they are not seeing it because you are fishing in the wrong pond.
  why: >-
    A free offer is the fastest way to see if anyone wants your thing, so its failure is information about the thing, the believability or the targeting.
  anchor: >-
    3) Aren’t actually seeing it because you are fishing in the wrong pond This can be a
  source: >-
    100m-series-lost-chapters.md, Free Promotions, line 831
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:831"
- id: D-lost-chapters-015
  type: antipattern
  name: >-
    An offer so good it is unbelievable
  statement: >-
    Making a crazy offer without answering the question Why, so that the offer reads as too good to be true.
  why: >-
    The famous marketer who advertised $1,000 back for every $100 got no responses at all; give a good enough reason and people will believe you.
  applies_when: >-
    Whenever you give a crazy free or discount offer away.
  authors_caveat: >-
    The reason must be true.
  anchor: >-
    of believability It’s an amazing offer But it was so good, it was unbelievable That’s why
  source: >-
    100m-series-lost-chapters.md, Free Promotions, line 842
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:842"
- id: D-lost-chapters-016
  type: antipattern
  name: >-
    A bare discount with no reason
  statement: >-
    Advertising a big discount with no stated reason, such as 90 percent off all products with nothing attached.
  why: >-
    Going out of business, all products must go in 30 days is a very good reason for 90 percent off; without the reason you would likely not get the same response.
  anchor: >-
    just said 90% off all products, you likely wouldn’t get the same response So—as long as it’s
  source: >-
    100m-series-lost-chapters.md, Free Promotions, line 846
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:846"
- id: D-lost-chapters-017
  type: antipattern
  name: >-
    Volume Can Be A Double-Edged Sword
  statement: >-
    Running a free offer with manual processes or operations that cannot absorb the volume it brings.
  why: >-
    Free can attract too many prospects; the offer then has to be made less appealing or friction added, and the key with free is finding the sweet spot on friction to maximize quality volume.
  anchor: >-
    You: For some businesses, free can attract “too many” prospects So we may need to add
  source: >-
    100m-series-lost-chapters.md, Free Promotions, Cons #1, line 933
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:933"
- id: D-lost-chapters-018
  type: antipattern
  name: >-
    Losing the lazy whales to friction
  statement: >-
    Adding so many steps and qualifications that otherwise qualified prospects drop out.
  why: >-
    Prospects drop off at each point, so you get fewer higher quality people but may lose otherwise qualified people; you want just enough friction to weed out the weirdos but not so much that you lose some lazy whales.
  anchor: >-
    quality people And you may lose otherwise qualified people For example: a one-step
  source: >-
    100m-series-lost-chapters.md, Free Promotions, Examples of Friction #3, line 966
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:966"
- id: D-lost-chapters-019
  type: rule
  name: >-
    Forced Consumption needs cheap eyeballs
  statement: >-
    Use forced consumption, such as a 40-minute video before any call to action, only where you advertise to a large audience and eyeballs are cheap.
  why: >-
    Forcing consumption cuts volume but increases lead quality; in other settings the volume is just too low to justify the friction.
  boundary: >-
    The author's own limit: in settings without a large cheap audience the volume is too low to justify this friction, though the same friction can be added later between steps.
  anchor: >-
    said, in other settings the volume is just too low to justify this friction You can also
  source: >-
    100m-series-lost-chapters.md, Free Promotions, Examples of Friction #4, line 978
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:978"
- id: D-lost-chapters-020
  type: antipattern
  name: >-
    Judging a campaign by the percentage of qualified leads
  statement: >-
    Picking the campaign whose leads feel more qualified over the campaign that produces more qualified leads in absolute numbers.
  why: >-
    500 leads at half qualified beats 200 leads at 80 percent qualified on pure dollars and cents, even though the team feels better about the second.
  anchor: >-
    Which campaign was better? Our team may feel better about #2, but according to
  source: >-
    100m-series-lost-chapters.md, Free Promotions, Free Money Math, line 1023
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1023"
- id: D-lost-chapters-021
  type: antipattern
  name: >-
    Free Brings Broke People Myth
  statement: >-
    Refusing free offers on the belief that free respondents are freebie seekers who will not close.
  why: >-
    Four independent split tests of free versus premium offers, each over 10 representative markets, showed the same closing percentage and the same average ticket size; what differed was volume and lead cost, with free front ends cutting lead costs five times or more.
  authors_caveat: >-
    Right and wrong: the author does not claim free is for every offer, every time.
  anchor: >-
    was the same So being “non-free” offered no advantage in close rates or average ticket size
  source: >-
    100m-series-lost-chapters.md, Free Promotions, Free Brings Broke People Myth, line 1048
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1048"
- id: D-lost-chapters-022
  type: antipattern
  name: >-
    The #1 mistake: a premium offer sold at free-offer prices
  statement: >-
    Comparing free and premium offers while running a premium offer at free-offer prices, that is, mixing and matching the Price, Prospect, Process, Promotion and Product of the two structures.
  why: >-
    They are entirely different acquisition strategies and the comparison is not a fair one; if lead cost is 5-10x higher for a premium offer, prices should be at least 5-10x higher.
  applies_when: >-
    Whenever a free and a premium structure are being compared or tested against each other.
  anchor: >-
    premium offers. It is the #1 mistake I see when people are comparing them.
  source: >-
    100m-series-lost-chapters.md, Free Promotions, Pro Tip: Free Makes More Money, line 1060
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1060"
- id: D-lost-chapters-023
  type: rule
  name: >-
    Free beats premium unless high-ticket selling is mastered
  statement: >-
    At the same price point free beats premium hands down, unless the seller has truly mastered the art of high-ticket selling.
  boundary: >-
    The author's own exception to his preference for free: mastery of high-ticket selling.
  anchor: >-
    premium hands down unless they’ve truly mastered the art of high-ticket selling.
  source: >-
    100m-series-lost-chapters.md, Free Promotions, Pro Tip: Free Makes More Money, line 1065
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1065"
- id: D-lost-chapters-024
  type: rule
  name: >-
    Free is not for every offer, every time
  statement: >-
    Do not read the author's preference for free as a rule that every offer should be free.
  boundary: >-
    The author limits his own claim: free is not for every offer, every time; the claim is only that free can be layered into a powerful money model.
  anchor: >-
    That being said, I’m not saying free is for every offer, every time But, I am saying that if
  source: >-
    100m-series-lost-chapters.md, Free Promotions, line 1066
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1066"
- id: D-lost-chapters-025
  type: antipattern
  name: >-
    Marginal discounts
  statement: >-
    Running marginal discounts of roughly 5 to 25 percent off.
  why: >-
    They are not enough to drive real behavior and basically just cut into margin; only massive discounts of 50 percent or more drive action from a population that would not otherwise act.
  anchor: >-
    action That being said, I personally am not a big believer in “marginal” discounts (say 5 to
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Understanding Discount Offers, line 1080
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1080"
- id: D-lost-chapters-026
  type: rule
  name: >-
    A discount offer is a piece of the thing, not the entire thing
  statement: >-
    A discount offer should make up a component of your offering rather than the whole of it.
  boundary: >-
    Most of the time, with a handful of notable exceptions, a discount offer is a piece of the thing, not the entire thing.
  anchor: >-
    Note: most of the time when talking about discount offers, they will only make up
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, line 1093
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1093"
- id: D-lost-chapters-027
  type: rule
  name: >-
    Use Absolute Prices When Talking about Understood Products and Services
  statement: >-
    Discount the price only of a service people already understand and already have a price expectation for; discounting something people do not understand does not work.
  why: >-
    If a customer does not know what they are getting, a discount on it makes no sense because they have nothing to compare it to.
  boundary: >-
    The author's stated limit of discount offers: 50 percent off an agency retainer would not work because nobody knows what the agency does or what it costs. The only way around it is to state the price and then state the discount.
  applies_when: >-
    Front-end discount offers in well-understood categories: dentists, chiropractors, gyms, haircuts.
  anchor: >-
    costs. This is where discounts do well. If you discount something that people
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Pro Tip and Conclusion, lines 1163, 1408-1415
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1163"
- id: D-lost-chapters-028
  type: rule
  name: >-
    Lots of Cheap Leads Within the Law
  statement: >-
    Where free offers with stipulations or creative conditions are forbidden, use a discount offer to advertise compliantly instead.
  boundary: >-
    In some countries free offers carrying stipulations are forbidden; if you are in a heavily regulated industry, state or country, a discount offer may be right for your business.
  anchor: >-
    You: Of course not, but in some countries if you have any stipulations or creative
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Pros #1, line 1190
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1190"
- id: D-lost-chapters-029
  type: antipattern
  name: >-
    Funding marketing off discount cash
  statement: >-
    Building the business so that the money collected on the discount offer is the real way acquisition costs get liquidated.
  why: >-
    The money collected on a discount will not amount to much; it can help liquidate acquisition costs but the discount is only the first way to attract and transact with a customer.
  anchor: >-
    costs But we will never build our business to use this money as the real way we are liquidating
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Pros #2, line 1213
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1213"
- id: D-lost-chapters-030
  type: antipattern
  name: >-
    Believing discount leads are inherently more willing to buy
  statement: >-
    Attributing the higher close rate on discount leads to the prospects being inherently more willing to spend.
  why: >-
    It is mostly the conviction of the salesperson; a good salesman will sell the same percentage of free versus non-free leads when the funnels and sales environment are the same, which the author has tested four separate times.
  authors_caveat: >-
    It still makes people feel better about selling, which is fine and especially important with a small business owner who has limiting beliefs; sometimes you have to meet them halfway.
  anchor: >-
    This is mostly due to the conviction of the salesperson, not because people are
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Pro Tip after Pros #3, line 1242
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1242"
- id: D-lost-chapters-031
  type: antipattern
  name: >-
    Add Steps As Price And Complexity Increase
  statement: >-
    Asking for the sale after spending too little time with the prospect relative to the price and complexity of what you sell.
  why: >-
    The more complex or expensive the thing, the more time a prospect needs to spend with you in order to buy, whether all at once in a weekend seminar or over multiple sales calls.
  applies_when: >-
    Diagnosing a conversion problem.
  anchor: >-
    you’re having a conversion issue, you may simply be spending too little time with
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Author Note, line 1330
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1330"
- id: D-lost-chapters-032
  type: antipattern
  name: >-
    Giving away the doctor's time
  statement: >-
    Spending the expensive practitioner's time on the discounted first visit rather than on the most-qualified candidates.
  why: >-
    The first visit can be fixed operationally so a front desk admin or assistant handles it, which pre-qualifies candidates and eliminates the cost of no-shows while reserving the practitioner's time.
  applies_when: >-
    Services where the time and cost of the individual delivering is real, such as a doctor's time.
  anchor: >-
    The other way of solving this problem (my preference) is to not give away the
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Pro Tip: Give Away Lower Cost Time If You Can, line 1336
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1336"
- id: D-lost-chapters-033
  type: antipattern
  name: >-
    Giving Away The Farm
  statement: >-
    Discounting the core offer as a habit rather than splintering the offer and discounting one core component.
  why: >-
    People become trained to buy only at discounted times; the discount is a way to acquire customers, not a business model.
  boundary: >-
    True discounts on the core offer work only where the pricing model is to raise prices wildly during the regular season and live off the discounting, as clothing retailers do, and even then it is a double-edged sword.
  anchor: >-
    then people will become trained to buy only at discounted times No bueno This is why we
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Cons #1, line 1372
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1372"
- id: D-lost-chapters-034
  type: antipattern
  name: >-
    Bargain Hoppers
  statement: >-
    Treating people who bought the discount as customers instead of as qualified leads, and blaming them for not buying the main thing.
  why: >-
    That was the issue with Groupon, but most of the businesses that complained did not know how to structure their offers to automatically qualify prospects into customers of the core service.
  anchor: >-
    core service We shouldn’t see people as customers if they buy the discount We should see
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Cons #2, line 1395
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1395"
- id: D-lost-chapters-035
  type: antipattern
  name: >-
    Taking loans and investors too early
  statement: >-
    Reaching for loans and investors early instead of getting customers to pay fast enough to finance acquisition.
  why: >-
    Loans and investors are great moves at the right time, but doing it too early will probably bite you later; the author prefers to be profitable day one and take capital on his own terms.
  anchor: >-
    time But doing it too early will probably bite you in the butt later For that reason, I prefer
  source: >-
    100m-series-lost-chapters.md, Section B: The Expensive Customer Problem, Customer Financed Acquisition, line 1456
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1456"
- id: D-lost-chapters-036
  type: antipattern
  name: >-
    Never calculating actual CAC
  statement: >-
    Reporting ad spend per customer as CAC while treating content leads as free and leaving the outbound team, salaries, software and supporting activities out of the number.
  why: >-
    A $1,000 sale you thought cost $200 really costs $500, and in some businesses that difference is the difference between $1,000,000 and $10,000,000 per month; people are then surprised at month end when they are not making money.
  applies_when: >-
    Unlike LTGP, CAC is a hard science: it can and should be known exactly, each month, by channel.
  anchor: >-
    Here’s the problem: most entrepreneurs have never calculated their actual CAC They
  source: >-
    100m-series-lost-chapters.md, Cost To Acquire a Customer = CAC, line 1579
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1579"
- id: D-lost-chapters-037
  type: antipattern
  name: >-
    Mixing up Gross Profit and Net Profit
  statement: >-
    Using net profit where the money math calls for gross profit.
  why: >-
    Gross Profit is what is left after subtracting only the costs of making and delivering the product or service; Net Profit is what is left after subtracting all costs, and the business is run on the gross profit.
  anchor: >-
    from a purchase after you deliver the goods or service Note: this isn’t net profit (which is what’s
  source: >-
    100m-series-lost-chapters.md, Lifetime Gross Profit (LTGP), Author Note, line 1682
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1682"
- id: D-lost-chapters-038
  type: antipattern
  name: >-
    Trusting the CRM on lifetime transactions
  statement: >-
    Taking the average number of lifetime transactions straight from the CRM without knowing how to compute it by hand.
  why: >-
    CRMs often do not report it, and even when they do the figures are often wrong because data tracking can be a mess, especially when starting out.
  boundary: >-
    Figuring out how many transactions a customer makes on average is always an estimate, because customers keep buying and lifetime transactions always increase as a business gets older.
  anchor: >-
    they’re often wrong because data tracking can be a mess (especially if you’re starting out)
  source: >-
    100m-series-lost-chapters.md, Lifetime Gross Profit (LTGP), LTGP Step Two, line 1727
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1727"
- id: D-lost-chapters-039
  type: antipattern
  name: >-
    Letting new signups move the churn number
  statement: >-
    Counting new clients signed up during the period when calculating churn.
  why: >-
    Churn is the share of the original cohort that left: sign up zero or 1,000 new clients in the month and the five lost out of the original hundred still make churn 5 percent.
  anchor: >-
    Note: People get this twisted Don’t be one If you sign up new clients during this time
  source: >-
    100m-series-lost-chapters.md, Lifetime Gross Profit (LTGP), Note on churn, line 1767
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1767"
- id: D-lost-chapters-040
  type: rule
  name: >-
    CFA Level 1
  statement: >-
    Do not start a business at CFA Level 1, where 30-day gross profit from a customer is less than CAC, because it means floating the business on life savings, loans and lines of credit.
  why: >-
    You eventually come out ahead but it takes longer, and it is a big risk.
  boundary: >-
    The author's own limit: you can absolutely make money this way over the long term and many big businesses make all their money this way, but you have to already have lots of money to do it, and most young bootstrapped businesses do not.
  anchor: >-
    businesses make all their money this way But you have to already have lots of money to do it
  source: >-
    100m-series-lost-chapters.md, Levels of Customer Financed Acquisition, CFA Level 1, line 2140
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2140"
- id: D-lost-chapters-041
  type: rule
  name: >-
    CFA Level 2 is capped by the credit limit
  statement: >-
    At CFA Level 2 the credit limit becomes the advertising budget and therefore caps how many customers can be acquired.
  boundary: >-
    The stated ceiling of Level 2: it can only be raised by paying the balance off early, asking for a higher limit or getting another card; the rest of the section exists to get to Level 3.
  anchor: >-
    advertising budget This means it caps how many customers you can get So if you have a
  source: >-
    100m-series-lost-chapters.md, Levels of Customer Financed Acquisition, CFA Level 2, line 2148
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2148"
- id: D-lost-chapters-042
  type: rule
  name: >-
    Something else will bottleneck growth
  statement: >-
    CFA removes cash as the growth constraint and nothing more; expect another bottleneck, usually servicing customers rather than acquiring them.
  boundary: >-
    The author states the limit of his own method twice: something else will eventually bottleneck growth and that is fine, but the bottleneck must never be cash for getting customers; how to scale a company past that point is explicitly not in this book.
  anchor: >-
    will eventually bottleneck your growth And that’s OK. That’s life But you never want that
  source: >-
    100m-series-lost-chapters.md, Levels of Customer Financed Acquisition, lines 2201, 2217-2220
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:2201"
- id: D-lost-chapters-043
  type: antipattern
  name: >-
    Settling for 2:1 returns on advertising
  statement: >-
    Accepting 2:1 returns on advertising as good enough.
  why: >-
    With a few tweaks the same business could stop spending its own money on advertising altogether and let customers pay for growth; the author frames the belief that a great business is out of reach as the real constraint.
  anchor: >-
    believe they can have a great business They expect 2:1 returns on advertising to be “good
  source: >-
    100m-series-lost-chapters.md, Levels of Customer Financed Acquisition, Solution Explained, line 2236
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2236"
- id: D-lost-chapters-044
  type: antipattern
  name: >-
    Relying on a better product instead of outspending
  statement: >-
    Counting on product quality rather than on the ability to outspend competitors for a customer.
  why: >-
    You can make a product as good as you want, but if you cannot outspend your competition, the competition will steal your product and your potential customers.
  anchor: >-
    want, but if you can’t outspend your competition, your competition will steal your product
  source: >-
    100m-series-lost-chapters.md, Back End: The Value Grid, line 2307
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2307"
- id: D-lost-chapters-045
  type: antipattern
  name: >-
    The stair step
  statement: >-
    Modelling lifetime value as a sequence or stair step of ascending offers, which makes the relationship look linear and implies a customer must buy the first offer to buy the second.
  why: >-
    Not all customers follow it: many buy offer #1 then skip to offer #4, or skip #1 and #2 and buy #3 and #5; they buy the offers that solve their needs, and the ladder ignores multiple offers at the same price point solving different needs.
  authors_caveat: >-
    The stair step is still a great place to start to get ideas down, and all models have limits; once you have metrics the grid becomes the invaluable tool.
  anchor: >-
    first, with a stair step, the visual depiction makes your brain think that all customers must
  source: >-
    100m-series-lost-chapters.md, Back End: The Value Grid, line 2337
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2337"
- id: D-lost-chapters-046
  type: antipattern
  name: >-
    It costs too much money to acquire customers
  statement: >-
    Concluding that customers cost too much to acquire once the real cost of working and selling the leads is counted.
  why: >-
    Acquisition never costs too much or too little, it just costs what it costs; the job is to design the business to make more money from the same customers.
  anchor: >-
    it never costs “too much” or “too little” It just costs what it costs It’s up to us to design our
  source: >-
    100m-series-lost-chapters.md, Back End: The Value Grid, line 2378
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2378"
- id: D-lost-chapters-047
  type: antipattern
  name: >-
    Stacking offers that add operational complexity
  statement: >-
    Adding offers and services that bring operational complexity out of proportion to what they earn.
  why: >-
    Adding more offers and services is a fast track to adding operational complexity, which makes business hard; look for revenue that adds little to no cost in time, money or complexity.
  authors_caveat: >-
    If something is going to add complexity, it had better be worth it, in lots of profit or very little cost: keep that ratio high.
  anchor: >-
    Before we dive into this, there is one strong warning I must make Adding more offers
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, line 2423
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2423"
- id: D-lost-chapters-048
  type: rule
  name: >-
    Downsell ladders need a one-on-one setting
  statement: >-
    The step-by-step downsell ladder can be run effortlessly in person, over the phone or in any one-on-one setting, but not when selling off a page digitally.
  why: >-
    One-on-one selling affords the flexibility to match the buying power of the prospect with your ability to solve their needs on their budget.
  boundary: >-
    Selling off a page digitally you do not have this luxury; the author names it as the reason he is such a big fan of one-on-one sales.
  anchor: >-
    things that you can do effortlessly Selling off a page digitally, you will not have this luxury,
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, Sample Weight Loss Offer Flow, line 2536
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2536"
- id: D-lost-chapters-049
  type: rule
  name: >-
    A no after every downsell is a trust problem
  statement: >-
    When the prospect says no through the whole downsell ladder, treat it as a trust and sales problem rather than an offer problem.
  boundary: >-
    The author marks sales skill itself as beyond the scope of this book.
  anchor: >-
    no payment plan If they still say no, then they probably don’t trust you and you need to
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, Sale #1, line 2555
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2555"
- id: D-lost-chapters-050
  type: antipattern
  name: >-
    Convincing people your way is the right way
  statement: >-
    Trying to convince a customer that your way of solving the problem is the right way instead of presenting effective options they already want.
  why: >-
    Most times they will just go to someone who solves the problem the way they want it solved.
  applies_when: >-
    The Right Way step of picking an offer for the money model.
  anchor: >-
    their food You can try to convince people your way is the right way But most times, they’re
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, Four Steps To Picking The Right Offer, line 2661
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2661"
- id: D-lost-chapters-051
  type: antipattern
  name: >-
    Making the offer when it is convenient for you
  statement: >-
    Making the offer at the time that suits the business rather than at the customer's moment of greatest need.
  why: >-
    Someone may be hungry, but ask them if they want another steak after they are full and they will say no.
  anchor: >-
    like it, at the moment they need it the most—not when it’s convenient for you
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, Right Time and Summary, line 2671
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:2671"
- id: D-lost-chapters-052
  type: antipattern
  name: >-
    Leading with the pitch instead of the presentation
  statement: >-
    Opening with the offer, as in come buy my website designer for $2,000, instead of educating first and making the offer at the end.
  why: >-
    Opened that way, no one would have bought; sixty minutes into the presentation the author estimates a third of the room would have taken out their credit cards.
  anchor: >-
    If he had started with “Hey everyone, come buy my website designer for $2,000,” no
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, line 2698
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2698"
- id: D-lost-chapters-053
  type: rule
  name: >-
    High-ticket offers to cold audiences
  statement: >-
    Treat a high-ticket offer made to a cold audience as one of the hardest things in business and plan the long game on the front end.
  why: >-
    The more expensive the offer the more audiences want to learn about it before buying, and the colder the audience the more exposure it takes to build trust.
  boundary: >-
    The author names high-ticket to cold as the hardest combination; the free-education-with-offer format exists to force as much exposure as it can into as short a window as reasonable.
  anchor: >-
    a brand, business, or person it takes to build trust This makes high-ticket offers to cold
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, Summary, line 2910
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2910"
- id: D-lost-chapters-054
  type: rule
  name: >-
    Freemium fits businesses with near-100 percent incremental margins
  statement: >-
    Freemium fits a software or media business, meaning any business with close to 100 percent incremental margins, and is a dangerous but effective money model there.
  boundary: >-
    The author's own stated scope for freemium, given as his reason for cutting the chapter: it did not apply to enough businesses.
  anchor: >-
    (any business that has close to 100% incremental margins) this is a dangerous
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Freemium, Lost Chapter Author Note, line 2937
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2937"
- id: D-lost-chapters-055
  type: rule
  name: >-
    Steer clear of freemium without capital
  statement: >-
    Do not use the freemium structure without investors and large amounts of capital; use it only if you have something so valuable that lots of people come to you without marketing.
  why: >-
    Almost every company in the examples section has funding, and the free product must cost $0 to get people to use it, or just enough advertising for it to spread virally.
  boundary: >-
    The author's explicit exclusion: no investors and no large capital means do not use this structure; otherwise, steer clear.
  anchor: >-
    do not have investors and large amounts of capital, I would not recommend this structure
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Freemium, line 2942
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2942"
- id: D-lost-chapters-056
  type: antipattern
  name: >-
    Treating freemium as a business model
  statement: >-
    Treating freemium as a business model rather than as an acquisition strategy.
  why: >-
    The author calls the distinction very important: the free thing has to be free and valuable enough to spread but not so valuable that customers use it without upgrading.
  authors_caveat: >-
    Freemium is one of the most dangerous acquisition strategies and a definitely advanced move; the author has seen it done incorrectly by really smart people more often than he has seen it done correctly.
  anchor: >-
    points to understand about freemium is that it is not a business model, it is an acquisition
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Freemium, Description and Summary Points, lines 2953, 3041-3043
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:2953"
- id: D-lost-chapters-057
  type: rule
  name: >-
    The three conditions on what freemium gives away
  statement: >-
    The freemium giveaway must cost almost nothing to fulfill, provide continuous rather than one-time value, and not give away so much of the farm that people never want to buy anything else.
  why: >-
    The author calls it a very difficult balance and names designing it as the incredibly challenging part.
  boundary: >-
    All three conditions have to hold at once; software fits because it is virtually free per additional user and is intended to provide continuous value, leaving only how much and exactly what to give away.
  anchor: >-
    provides continuous value (not one-time), and 3) doesn’t give away so much of the farm that
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Freemium, Details, line 2996
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2996"
- id: D-lost-chapters-058
  type: antipattern
  name: >-
    Freemium done wrong
  statement: >-
    Giving away your core thing for free, so people use it and then do not want to buy the next thing.
  why: >-
    You end up running a business that loses money servicing customers for free.
  anchor: >-
    Here’s what it looks like when done wrong: You give away your core thing People use it
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Freemium, line 3022
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3022"
- id: D-lost-chapters-059
  type: antipattern
  name: >-
    Roadblocks
  statement: >-
    Freemium fails in three named ways: a Conversion Problem where too few free users upgrade, a Value Problem where the free thing is not valuable enough for people to tell others about, and a Cost Problem where people do spread it but servicing them for free costs too much relative to what paid customers bring.
  anchor: >-
    #1 Conversion Problem: Conversion percentage from free to paid is too low.
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Freemium, Roadblocks, line 3027
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3027"
- id: D-lost-chapters-060
  type: rule
  name: >-
    Freemium is not a first rodeo
  statement: >-
    Do not attempt freemium as a first acquisition strategy or without knowing everything there is to know about it.
  boundary: >-
    The author's explicit precondition: be a seasoned pro and know your numbers like you know your children's names; the chapter is included mostly for completeness.
  anchor: >-
    powerful If it’s your first rodeo, and you don’t know everything there is to know about a
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Freemium, Summary Points, line 3036
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3036"
- id: D-lost-chapters-061
  type: rule
  name: >-
    Freemium only works with 100 percent free
  statement: >-
    The freemium offer works only as a fully free strategy and has no discount variation.
  boundary: >-
    Stated by the author in the Free Versus Discount Note of the chapter.
  anchor: >-
    This offer only works with 100% free strategies. It does not work with a discount
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Freemium, Free Versus Discount Note, line 2982
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2982"
- id: D-lost-chapters-062
  type: rule
  name: >-
    Free Pick Your Price does not work with a discount wrapper
  statement: >-
    The Free Pick Your Price offer works only wrapped as free, not as a discount.
  boundary: >-
    Stated by the author in the Free Versus Discount Note of the chapter.
  anchor: >-
    This offer does not work with a discount wrapper
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Pick Your Price, Free Versus Discount Note, line 3141
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3141"
- id: D-lost-chapters-063
  type: rule
  name: >-
    Free Pick Your Price depends on closing the upsell
  statement: >-
    Do not run Free Pick Your Price unless you can close the upsell that makes it profitable.
  boundary: >-
    The author's stated reason for removing the chapter: some businesses might lose money doing it because they would not be able to close the upsell that makes it profitable. With skill it is a goodwill play that also makes money and generates leads.
  anchor: >-
    lose money doing it since they wouldn’t be able to close the upsell that makes this profitable.
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Pick Your Price, Lost Chapter Author Note, line 3048
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3048"
- id: D-lost-chapters-064
  type: rule
  name: >-
    Give away only what has low operational cost
  statement: >-
    What you give away free must have low operational cost, so you can hand it to everyone without burning out staff; the higher operational cost work is saved for the people who choose to pay.
  boundary: >-
    The same constraint governs Free With Alternate Revenue Stream: if you market thing A for free you must actually be able to give it away, so what you give away has to have low incremental costs.
  anchor: >-
    Make sure that the thing you are giving away for free has low operational costs so you
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Pick Your Price, Details, lines 3175, and Upsell Offer: Free With Alternate Revenue Stream, lines 3325-3328
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3175"
- id: D-lost-chapters-065
  type: rule
  name: >-
    The $0 rung has to be honoured
  statement: >-
    In a pick-your-price offer, if someone does not want to pay for the first thing you must give them the basic level for free.
  authors_caveat: >-
    You can and should still upsell them on other products and services during their time with you.
  anchor: >-
    someone doesn’t want to pay for the first thing, you must give them the basic level for free
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Pick Your Price, Details, line 3149
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3149"
- id: D-lost-chapters-066
  type: rule
  name: >-
    Free With Alternate Revenue Stream needs a high-margin second stream
  statement: >-
    Use this offer only where the business already has an alternative revenue stream whose margins are high enough to fund fulfilling both the free thing and the paid thing.
  boundary: >-
    The offer depends strongly on the types of monetization and revenue streams available to a business; the author removed the chapter because he did not think enough businesses would be able to use it.
  anchor: >-
    recurring services, provided the alternative revenue stream has sufficiently high margins to
  source: >-
    100m-series-lost-chapters.md, Upsell Offer: Free With Alternate Revenue Stream, lines 3253, 3201-3202
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3253"
- id: D-lost-chapters-067
  type: antipattern
  name: >-
    Selling the product before the trial on cold traffic
  statement: >-
    Running the free-plus-upsell play on cold traffic without closing a trial and a credit card on the first transaction.
  why: >-
    Without the card on the first transaction you get a lot of no-shows; the product upsell belongs on the second transaction.
  applies_when: >-
    Cold traffic, as opposed to marketing the same offer to an existing audience.
  anchor: >-
    trial + credit card on the first transaction, then upsell product on the second, otherwise you
  source: >-
    100m-series-lost-chapters.md, Upsell Offer: Free With Alternate Revenue Stream, line 3380
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3380"
- id: D-lost-chapters-068
  type: rule
  name: >-
    No upsell, no stick
  statement: >-
    Treat the first upsell as a must-have rather than a nice-to-have, because a customer who does not buy it is unlikely to stay.
  why: >-
    It is the greatest predictor of back-end conversion, so however minor the sale looks it is the most important one for the long-term value of the customer.
  anchor: >-
    NOTE: If someone does not buy the upsell, they are unlikely to stay It’s the greatest
  source: >-
    100m-series-lost-chapters.md, Upsell Offer: Free With Alternate Revenue Stream, NOTE, line 3383
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3383"
- id: D-lost-chapters-069
  type: rule
  name: >-
    Lifetime Upgrades fit a continuity service business
  statement: >-
    Use the lifetime-versus-one-time bonus model where the business already sells continuity.
  boundary: >-
    The author's stated reason for cutting the chapter: too many people would struggle to fit it into their business; but for a continuity service business the model can be very effective, and a continuity offer can be made on anything that provides continuous value.
  anchor: >-
    bonuses. I thought too many people would struggle to fit it into their business. But
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, Lost Chapter Author Note, lines 3399, 3504-3506
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3399"
- id: D-lost-chapters-070
  type: antipattern
  name: >-
    A bonus the customer does not know about
  statement: >-
    Holding bonuses that customers have not been told exist.
  why: >-
    They can only get excited enough to stay longer for a bonus if they know it exists; tell them whether they are just signing up or a year in, and after each recurring bonus tell them about the next one.
  authors_caveat: >-
    Let customers know the type of bonus they get but keep the bonus itself a surprise; that keeps flexibility and makes the bonus more valuable.
  anchor: >-
    Make sure customers know about your bonuses They can only get excited enough to
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, Important Notes, line 3553
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3553"
- id: D-lost-chapters-071
  type: rule
  name: >-
    Keep bonuses variable unless the upgrade is huge and permanent
  statement: >-
    Choose a Lifetime Upgrade over a variable bonus only when the bonus gives a huge and permanent improvement; otherwise keep it variable.
  why: >-
    However good the thing is, customers get used to it, so giving new stuff more often, even if less valuable, keeps more customers interested longer.
  boundary: >-
    The author's stated condition for using the Lifetime Upgrade form at all.
  anchor: >-
    variable bonuses or Lifetime Upgrades Unless your bonus gives a huge and permanent
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, Important Notes, line 3565
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3565"
- id: D-lost-chapters-072
  type: rule
  name: >-
    Lifetime Discounts cut prices too far
  statement: >-
    Treat Lifetime Discounts as the offer most likely to be misused by cutting prices too much and damaging the business.
  boundary: >-
    This is the author's stated reason for cutting the chapter from an earlier version of $100M Money Models: a lot of people would cut their prices too much and ultimately damage their business.
  anchor: >-
    was in an earlier version of $100M Money Models, but I cut it out since I think a lot of people
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, Lost Chapter Author Note, line 3627
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3627"
- id: D-lost-chapters-073
  type: antipattern
  name: >-
    A discount you never charge more than
  statement: >-
    Calling a price a Lifetime Discount when the price never goes up after the offer ends, so you are just listing the price and pretending it is a discount.
  why: >-
    The author calls it gross; a Lifetime Discount only works if you actually charge more when the offer ends.
  boundary: >-
    Offering a Lifetime Discount implies you have a higher retail price.
  anchor: >-
    A Lifetime Discount only works if you actually charge more when this offer ends
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, Description, line 3677
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3677"
- id: D-lost-chapters-074
  type: antipattern
  name: >-
    A locked-in rate without knowing your numbers
  statement: >-
    Granting a locked-in discounted rate for as long as the customer pays without knowing your numbers.
  why: >-
    The cost of getting customers and the cost of delivering will change; if those costs rise above the profit while the customer holds a locked-in rate, you have problems.
  authors_caveat: >-
    Know your numbers, preserve your margins, deliver a killer product; when giving a Lifetime Discount or any other discount, make sure you still make a profit after the discount and have a healthy LTGP.
  anchor: >-
    Lifetime Discounts come with a big fat warning: know your numbers. Lifetime
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, Important Notes, lines 3761, 3685-3686, 3885
  confirmations: 3
  anchor_at: "100m-series-lost-chapters.md:3761"
- id: D-lost-chapters-075
  type: antipattern
  name: >-
    A fixed price for life
  statement: >-
    Displaying the lifetime discount as a fixed price rather than a percentage or a dollar amount off retail, and giving that one price forever.
  why: >-
    Percentage and dollar forms are far more flexible: things always change, and with them you can adjust the retail price while lifetime discount customers keep their discount. One price forever limits you.
  authors_caveat: >-
    The author's own reconciliation is to offer price protection for a fixed period rather than forever, for example $20 a month for the next 36 months on a $50 a month service.
  anchor: >-
    and lifetime discount customers still keep their discount. So if you decide to offer a fixed price
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, Important Notes, line 3773
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3773"
- id: D-lost-chapters-076
  type: antipattern
  name: >-
    Selling the one-time-only thing twice
  statement: >-
    Saying a discount is offered once and never again and then selling the same thing at that rate again, or offering two different prices to two different people at the same time for the same thing.
  why: >-
    The promise has to be kept; the flexibility comes from changing what is included in the offer, not from repeating the same one-time-only deal.
  authors_caveat: >-
    Businesses test price points all the time; the limit is on the same thing at the same time to different people.
  anchor: >-
    If you say you will only offer this discount once and never again, stay true to it To
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, Important Notes, line 3797
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3797"
- id: D-lost-chapters-077
  type: antipattern
  name: >-
    Giving a cancelled customer their Lifetime Discount back
  statement: >-
    Restoring a Lifetime Discount to a customer who cancelled and wants to return.
  why: >-
    You will lose credibility with everyone else; instead offer a downsell that meets the same price but has different features, which works best for price-sensitive people.
  anchor: >-
    If a customer wants to return after canceling a Lifetime Discount First, don’t give it
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, Important Notes, line 3812
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3812"
- id: D-lost-chapters-078
  type: antipattern
  name: >-
    A generic discount across both offers
  statement: >-
    Running two mid-priced offers or a generic 25 percent off the top of both, instead of a steep founder's discount on one complementary service with the other paid at retail.
  why: >-
    The insane founder's deal attracts leads and the profit is made on the upsell, which often works better than the generic version.
  anchor: >-
    on the upsell This often works better than two mid-priced offers or a generic 25% off the
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, Important Notes, line 3808
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3808"
- id: D-lost-chapters-079
  type: antipattern
  name: >-
    Not recognising the Sunk Cost Fallacy in yourself
  statement: >-
    Using the sunk cost effect on customers without recognising the same bias in your own decisions.
  why: >-
    Unrecognised, it exposes you to far more risk than you otherwise should take and makes you stick with things longer than you would otherwise, across partnerships, memberships, investments and gambling.
  anchor: >-
    This psychological principle is dangerous If you don’t recognize it in yourself, you
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, The Bigger The Head The Longer The Tail, line 3863
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3863"
- id: D-lost-chapters-080
  type: antipattern
  name: >-
    Back-loading the big payment
  statement: >-
    Scheduling small payments first and the large payment at the end.
  why: >-
    The likelihood the last payment goes through is lower; $1,000 today followed by five monthly payments of $100 collects, while $100 a month for five months followed by $1,000 does not.
  applies_when: >-
    Any payment plan; the risk is accounted for by adding more to the up front payment, creating a paid in full discount, or increasing the cost of ending the discount.
  anchor: >-
    I ask for $100 per month for five months, and $1,000 at the end, the likelihood that the
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, line 3874
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3874"
- id: D-lost-chapters-081
  type: antipattern
  name: >-
    A business that only makes money with you in it
  statement: >-
    Running a business that produces its profit only while the owner works around the clock in it.
  why: >-
    If the business only makes money with you in it, it is a bad investment for anyone else, so it is worth almost nothing; the same revenue and profit produced without you turns a risky job into an asset that an investor could buy for many times the annual profit.
  anchor: >-
    Sure, you make a bit of money, but your business isn’t worth much. If the business only
  source: >-
    100m-series-lost-chapters.md, Section D: Expanded Employees Chapter, Why Employees Make You Wealthy, line 4113
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4113"
- id: D-lost-chapters-082
  type: antipattern
  name: >-
    Pointing the finger at the employee
  statement: >-
    Answering a performance drop with how can you not know your own job, instead of checking whether the expectation was actually communicated.
  why: >-
    If an employee did not know you wanted something done, you did not communicate it properly, even if you think you did; the author's business improved a lot when he believed them and pointed the finger at himself.
  applies_when: >-
    Communication, the first of the four reasons employee performance drops in the performance diamond.
  anchor: >-
    Don’t blow this off It’s so easy to point the finger and say “How can you not know your
  source: >-
    100m-series-lost-chapters.md, Section D, The Performance Diamond, line 4372
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:4372"
- id: D-lost-chapters-083
  type: antipattern
  name: >-
    Taking yes for understanding
  statement: >-
    Asking do you understand this, taking the yes as proof of training, and holding it against the person later.
  why: >-
    People are often conditioned to say yes out of fear of saying no; instead have them demonstrate the checklist as they did in training.
  applies_when: >-
    Training, the second of the four reasons employee performance drops.
  anchor: >-
    Often, we think we taught somebody something if we ask “do you understand this?”
  source: >-
    100m-series-lost-chapters.md, Section D, The Performance Diamond, line 4400
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4400"
- id: D-lost-chapters-084
  type: antipattern
  name: >-
    Expecting employees to solve problems you should have prevented
  statement: >-
    Treating a blocked employee as making excuses when something concrete is stopping them, such as no beef to grill, an internet connection too slow to download the file, or a broken phone.
  why: >-
    Business owners tend to expect employees to solve problems they should have prevented; these are some of the easiest problems to fix, but you have to ask to find out.
  applies_when: >-
    Circumstances, the fourth of the four reasons employee performance drops, once communication, training and motivation are ruled out.
  anchor: >-
    business owners (me included) tend to expect employees to solve problems we should
  source: >-
    100m-series-lost-chapters.md, Section D, The Performance Diamond, line 4455
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4455"
- id: D-lost-chapters-085
  type: antipattern
  name: >-
    Firing the wrong employee
  statement: >-
    Firing the sales person when the problem is advertising, or the advertising people when the problem is sales.
  why: >-
    One question separates them: do my engaged leads have the problem I solve and the money to spend? If no, they are not qualified and it is an advertising problem; if yes and they are buying but too few, it is still advertising; if yes and they are not buying, it is sales.
  applies_when: >-
    When CAC is more than 3x the industry average; within 3x of industry average the author calls it good enough and moves on to raising LTGP.
  anchor: >-
    Don’t fire your sales guy if you’ve got advertising problems And equally, don’t fire your
  source: >-
    100m-series-lost-chapters.md, Section D, How To Know Which Employees To Focus On, line 4514
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4514"
- id: D-lost-chapters-086
  type: rule
  name: >-
    This is how I do it, not what you have to do
  statement: >-
    Read the free-and-discount-first sequence as the author's own practice rather than as a requirement.
  boundary: >-
    The author limits his own prescription: he is not saying you have to do this, only that this is how he does it and it has served him well.
  anchor: >-
    I’m not saying you have to do this I’m saying this is how I do it, and it has served me
  source: >-
    100m-series-lost-chapters.md, Section A: Attract, line 563
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:563"
- id: D-lost-chapters-087
  type: rule
  name: >-
    Ways to increase lifetime value are out of scope
  statement: >-
    Of the many ways to increase lifetime value, this text covers only one, stacking offers.
  boundary: >-
    The author states that the many other ways to increase lifetime value are the subject of a future book he has not written.
  anchor: >-
    I’m not going to get into the many, many, many ways to increase lifetime value That
  source: >-
    100m-series-lost-chapters.md, Back End: The Value Grid, line 2328
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2328"
```
