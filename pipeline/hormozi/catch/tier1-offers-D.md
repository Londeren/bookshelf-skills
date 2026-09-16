# Улов фазы 1 — $100M Offers (2021) (ярус 1), тип D: антипаттерны и границы

Группа `tier1-offers`, слаг `offers`, ярус 1. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **62** (экстрактор вернул 62, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-offers.md` | 1–2973 | 6 | 62 |

## Как собран файл

Экстрактор D (Antipatterns and boundaries) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier1-offers.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier1-offers-D.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: D-offers-001
  type: antipattern
  name: >-
    Believing charging “too much” is bad
  statement: >-
    The entrepreneur holds the price down because charging “too much” feels unfair, instead of pricing far above what fulfilment costs.
  why: >-
    A large discrepancy between what something costs you and what you charge for it is the only way to be unreasonably successful; with enough value delivered the high price is still a steal for the prospect.
  boundary: >-
    You should never charge more than your product is worth; what you must charge far more than is the cost to fulfil it.
  anchor: >-
    Many entrepreneurs believe that charging “too much” is bad. The reality is that, yes, you should never charge more than your product is *worth*.
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 17
  confirmations: 1
  anchor_at: "100m-offers.md:17"
- id: D-offers-002
  type: antipattern
  name: >-
    Bigger and bigger claims
  statement: >-
    The marketer puts all attention on the top of the value equation — dream outcome and perceived likelihood — by making ever larger claims.
  why: >-
    Larger-than-life claims are the easiest to establish and therefore the least unique, since anyone can make a promise; the harder and more competitive side is time delay and effort and sacrifice, which the best companies focus on.
  anchor: >-
    That’s where beginner marketers make bigger and bigger claims. It’s easy, and it’s lazy.
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 47
  confirmations: 2
  anchor_at: "100m-offers.md:47"
- id: D-offers-003
  type: antipattern
  name: >-
    Improving what the prospect never perceives
  statement: >-
    The business raises the real likelihood of success, or cuts the real time delay and effort, without the prospect perceiving any of it.
  why: >-
    The increase in itself is not valuable — many times the prospect will have no idea; the offer only becomes valuable once the prospect perceives the increase in likelihood and the decrease in time delay and effort.
  anchor: >-
    It’s not about how much you increase your prospect’s likelihood of success, or decrease the time delay to achievement, or decrease their effort and sacrifice. That in itself is *not* valuable.
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 61
  confirmations: 1
  anchor_at: "100m-offers.md:61"
- id: D-offers-004
  type: antipattern
  name: >-
    Logical vs Psychological Solutions
  statement: >-
    The owner reaches for the logical solution to a business problem (make it faster, make it cheaper) rather than a psychological one.
  why: >-
    Logical solutions have usually already been tried, because they are what everyone would try; if a logical solution existed the problem would already be solved, so what is left are the psychological problems.
  anchor: >-
    Most people naturally try and solve problems using *logical* solutions. But the logical solutions have usually been tried...because they’re logical (it’s what everyone would try and do).
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 67
  confirmations: 1
  anchor_at: "100m-offers.md:67"
- id: D-offers-005
  type: antipattern
  name: >-
    Trying to create demand instead of channelling it
  statement: >-
    The business sets out to create desire or demand for what it sells rather than channelling desire that already exists.
  why: >-
    People have deep, unchanging desires; the job is to channel that desire through the offer and the monetization vehicle, and the author marks the distinction between creating and channelling demand as a very important one.
  anchor: >-
    We are not trying to *create* demand. We are trying to *channel* it. That is a very important distinction.
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market, line 1621
  confirmations: 2
  anchor_at: "100m-offers.md:1621"
- id: D-offers-006
  type: rule
  name: >-
    Dream outcomes cancel out
  statement: >-
    Between two products that satisfy the same desire, the dream outcome cannot differentiate the offers; only likelihood of achievement, time delay and effort and sacrifice can.
  why: >-
    The value from identical dream outcomes cancels out, so it is the other three variables that drive the difference in perceived value and ultimately price — why one thing that makes someone beautiful is worth $50,000 and another $5.
  boundary: >-
    The dream outcome driver only decides value when comparing two different desires being satisfied, not two vehicles for the same desire.
  anchor: >-
    That being said, when comparing two products or services that satisfy the *same* desire, the value from the dream outcomes will cancel out (since they are the same).
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 155
  confirmations: 1
  anchor_at: "100m-offers.md:155"
- id: D-offers-007
  type: antipattern
  name: >-
    Arguing with what people value
  statement: >-
    The owner complains about how people ought to value things instead of building on what people actually value.
  why: >-
    What is better is not what is perceived as more valuable — meditation is better than Xanax yet Xanax is the multi-billion dollar product; you can be right or you can be rich, and knowing what people value versus what is good for them is what lets you monetize and still give them what they need.
  anchor: >-
    And you can either sit there and make “complain” posts about how people “ought” to be a certain way.
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 249
  confirmations: 3
  anchor_at: "100m-offers.md:249"
- id: D-offers-008
  type: rule
  name: >-
    Bonus timing is for one-on-one selling
  statement: >-
    The rules given for when to present bonuses — ask for the sale first one-on-one, then reveal the bonuses — are stated for one-on-one selling only.
  why: >-
    There are key differences between pitching to a group and to a single person, and the author addresses only when a bonus would be brought up in a 1-1 selling scenario.
  boundary: >-
    Group selling is beyond the scope of this book.
  anchor: >-
    Group selling is beyond the scope of this book.
  source: >-
    100m-offers.md, ch. 14 Bonuses, line 295
  confirmations: 1
  anchor_at: "100m-offers.md:295"
- id: D-offers-009
  type: antipattern
  name: >-
    Valuable nuggets lost in the mix
  statement: >-
    Everything the business fulfils is left inside the core offer, so the most distinct, high-value pieces are never pulled out and highlighted as bonuses.
  why: >-
    When you provide so much stuff, valuable nuggets get lost in the mix; items that are short in length but high in value, such as checklists or infographics, are perceived as very valuable as bonuses even when no one would pay much for them on their own.
  applies_when: >-
    Deciding what should be a bonus versus part of the core offer when you are the one fulfilling it.
  anchor: >-
    Many times you have so much “stuff” you will be providing your customers (good thing) that valuable nuggets can get lost in the mix.
  source: >-
    100m-offers.md, ch. 14 Bonuses, line 409
  confirmations: 1
  anchor_at: "100m-offers.md:409"
- id: D-offers-010
  type: rule
  name: >-
    Partner bonuses only from non-competitors
  statement: >-
    Other businesses' products and services are taken into your bonus stack in exchange for exposure only where those businesses are not direct competitors.
  why: >-
    On that condition the arrangement earns goodwill, future referral IOUs and a more valuable offer at no cost, because you give them free exposure to the highest quality prospects — your customers.
  boundary: >-
    Applies as long as the other business is not a direct competitor.
  anchor: >-
    As long as they are not direct competitors, you can get some brownie points, secure some future referral IOUs, and make your offer more valuable at the same time.
  source: >-
    100m-offers.md, ch. 14 Bonuses, line 351
  confirmations: 1
  anchor_at: "100m-offers.md:351"
- id: D-offers-011
  type: antipattern
  name: >-
    Fear of losing sales by turning business away
  statement: >-
    The owner refuses to cap intake or run a deadline because he is afraid of losing sales he would otherwise have made.
  why: >-
    The author calls the fear unfounded: the biggest sales of a week-long campaign happen in the last four hours of the last day (up to 50-60%), so you make more money from the many people pushed to act than you lose to people who missed out, who in reality were never going to buy.
  anchor: >-
    Just like guarantees, there is always a fear that you will make less money by employing this strategy. We are afraid that we will lose sales we would have otherwise made. Every experienced marketer on the planet will tell you - it is a fear, and it is unfounded.
  source: >-
    100m-offers.md, ch. 13 Urgency, line 451
  confirmations: 1
  anchor_at: "100m-offers.md:451"
- id: D-offers-012
  type: antipattern
  name: >-
    Fake deadlines and countdowns
  statement: >-
    The business runs sign-up countdowns and promotion dates that are not real.
  why: >-
    If they are not real you lose credibility and just look like every other wannabe marketer.
  applies_when: >-
    Rolling seasonal urgency and date countdowns in a digital setting.
  anchor: >-
    But make sure they are real. If they aren’t, you’ll lose credibility and just look *like every other wannabe marketer*.
  source: >-
    100m-offers.md, ch. 13 Urgency, line 459
  confirmations: 1
  anchor_at: "100m-offers.md:459"
- id: D-offers-013
  type: rule
  name: >-
    Attach urgency to the promotion, not to the service
  statement: >-
    For a business that sells year round, urgency is created around the promotion, price or bonuses that expire, never around a claim that the service will be refused after the date.
  why: >-
    It would be a lie to say a roofing business will not service someone who buys after the date; talking about the promotion elicits the same urgency while maintaining your integrity.
  boundary: >-
    Applies to businesses that serve clients all year round, where the service itself cannot honestly be withdrawn at a deadline.
  anchor: >-
    It would be a lie to say that if you own a roofing business you won’t service them if they buy after the date.
  source: >-
    100m-offers.md, ch. 13 Urgency, line 477
  confirmations: 1
  anchor_at: "100m-offers.md:477"
- id: D-offers-014
  type: antipattern
  name: >-
    Raising prices silently
  statement: >-
    The business raises its prices without telling the people already in its pipeline.
  why: >-
    Announcing the raise shows a position of strength and gives an influx of cash from the people in the pipeline who were on the fence.
  anchor: >-
    Never raise your prices without letting people know.
  source: >-
    100m-offers.md, ch. 13 Urgency, line 479
  confirmations: 1
  anchor_at: "100m-offers.md:479"
- id: D-offers-015
  type: antipattern
  name: >-
    Over-ordering and failing to sell out
  statement: >-
    A limited release is stocked with more units than will sell, so the release does not sell out — and the tactic is repeated too often.
  why: >-
    It is better to sell out consistently than to over order and fail at creating that scarcity; the method stacks in effectiveness only when repeated over time and not too often, with about once a month the sweet spot.
  applies_when: >-
    Limited releases of physical products.
  anchor: >-
    it’s better to sell out consistently than over order and fail at creating that scarcity. This method stacks in effectiveness if it is done repeatedly over time (just not too often).
  source: >-
    100m-offers.md, ch. 12 Scarcity, line 565
  confirmations: 2
  anchor_at: "100m-offers.md:565"
- id: D-offers-016
  type: antipattern
  name: >-
    Offering more spots than you can sell
  statement: >-
    A workshop, event or higher-ticket upsell is opened with as many or more seats than you think you can sell.
  why: >-
    You must have fewer spots available than you think you can sell, so that next time everyone remembers you sold out fast; this is a compounding strategy that increases in effectiveness over time.
  applies_when: >-
    Higher-ticket upsells such as one-off workshops, trainings, events, seminars and consulting.
  anchor: >-
    But always remember *have less spots available than you think you can sell*
  source: >-
    100m-offers.md, ch. 12 Scarcity, line 585
  confirmations: 1
  anchor_at: "100m-offers.md:585"
- id: D-offers-017
  type: rule
  name: >-
    Once you’re out, you can never come back
  statement: >-
    Capping a service level and telling members that if they leave they can never return makes people think hard about leaving.
  why: >-
    The author reports it worked in his gyms, in a mastermind he was in and in his higher level of Gym Lords, but that as groups become much bigger the tactic loses some teeth.
  boundary: >-
    Works best with small groups; it loses teeth as the group becomes much bigger.
  anchor: >-
    This works best with small groups (like the above example). As groups become much bigger, the tactic loses some teeth (speaking from experience).
  source: >-
    100m-offers.md, ch. 12 Scarcity, line 611
  confirmations: 1
  anchor_at: "100m-offers.md:611"
- id: D-offers-018
  type: rule
  name: >-
    Scarcity is trickier in services
  statement: >-
    In services, where you want customers consistently, scarcity has to be built through a deliberate cap — total business cap, growth rate cap or cohort cap — rather than a limited release.
  why: >-
    With services it is a little trickier to use scarcity than with physical products, so the author enumerates the capped variants because one may fit a given business model better than another.
  boundary: >-
    Applies to service businesses that want to get customers consistently, unlike physical products where limited releases do the work.
  anchor: >-
    With services, especially if you want to consistently get customers, it can be a little trickier to use scarcity.
  source: >-
    100m-offers.md, ch. 12 Scarcity, line 573
  confirmations: 1
  anchor_at: "100m-offers.md:573"
- id: D-offers-019
  type: antipattern
  name: >-
    A guarantee with no “or what”
  statement: >-
    The guarantee names a result but never says what you will do if the client does not get it — "We will get you 20 clients guaranteed."
  why: >-
    Without the "or what" portion the guarantee sounds weak and diluted; what gives a guarantee power is the conditional statement: if you do not get X result in Y time period, we will Z.
  anchor: >-
    Without the “or what” portion of the guarantee, it sounds weak and diluted.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 666
  confirmations: 2
  anchor_at: "100m-offers.md:666"
- id: D-offers-020
  type: antipattern
  name: >-
    Deciding about a guarantee emotionally
  statement: >-
    The owner refuses a strong guarantee out of fear that people will take advantage of it, instead of doing the math on sales and refunds.
  why: >-
    For a guarantee not to be worth it, the increase in sales would have to be 100 percent offset by refunds; closing 130 percent as many people with refunds doubling from 5 to 10 percent still leaves 1.23x the money, all of it to the bottom line.
  anchor: >-
    For a guarantee to *not* be worth it, the increase in sales would have to be 100 percent offset by people who refunded.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 650
  confirmations: 1
  anchor_at: "100m-offers.md:650"
- id: D-offers-021
  type: antipattern
  name: >-
    Guarantee-driven buyers
  statement: >-
    The offer wins customers who buy because of the guarantee itself.
  why: >-
    A person who only buys because of a guarantee may not be willing to put in the work needed to succeed with the product or service, and becomes a very bad customer.
  authors_caveat: >-
    The author's fix is to tie the guarantee to the things the client needs to do to be successful, which serves both risk reversal and the client's outcome.
  anchor: >-
    Warning: While guarantees can be effective sellers, people who buy *because* of guarantees can become very shitty customers.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 652
  confirmations: 1
  anchor_at: "100m-offers.md:652"
- id: D-offers-022
  type: rule
  name: >-
    High Cost Services Warning
  statement: >-
    A business with a tremendous amount of cost in its product or service uses a conditional guarantee or an anti-guarantee rather than an unconditional one.
  why: >-
    On a refund you eat the cost of the refund and the cost of fulfilling.
  boundary: >-
    Applies where the cost of fulfilment is high; unconditional guarantees are for cases where that cost is not.
  anchor: >-
    If you have a tremendous amount of cost associated with your product or service, you will likely want to employ a conditional guarantee or an ANTI guarantee, as you will have to eat the cost of the refund AND the cost of fulfilling.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 656
  confirmations: 2
  anchor_at: "100m-offers.md:656"
- id: D-offers-023
  type: antipattern
  name: >-
    Piling conditions onto an unconditional guarantee
  statement: >-
    Conditions are added to a no-questions-asked refund guarantee to make it safer.
  why: >-
    The more conditions you add, the faster this guarantee loses its teeth.
  anchor: >-
    You can add conditions, but the more conditions you add, the faster this guarantee loses its teeth.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 708
  confirmations: 1
  anchor_at: "100m-offers.md:708"
- id: D-offers-024
  type: rule
  name: >-
    Satisfaction guarantee belongs to lower ticket
  statement: >-
    The satisfaction / no-questions-asked guarantee is used in lower-ticket situations and by a business that is good at fulfilling its promises.
  why: >-
    It is the highest form of guarantee — you could do everything right and still be asked for the money back — and you typically make up the refunds through higher and faster closing, but it becomes very risky as you move into higher-ticket services with higher costs of fulfilment.
  boundary: >-
    Works much better in lower-ticket situations; very risky in higher-ticket services with high fulfilment costs, and not to be used at all if you are not good at fulfilling your promises.
  anchor: >-
    I believe this offer works much better in lower-ticket situations. It becomes very risky as you go into higher-ticket services with higher costs of fulfillment.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 732
  confirmations: 2
  anchor_at: "100m-offers.md:732"
- id: D-offers-025
  type: rule
  name: >-
    Unconditional vs Conditional Based on Business Type
  statement: >-
    Broad guarantees go with lower ticket B2C; the higher the ticket and the more business-oriented the buyer, the more specific and conditional the guarantee.
  why: >-
    With lower ticket B2C many people just will not bother taking the time to claim; higher ticket business buyers call for specific guarantees, which may or may not include refunds and may or may not have conditions.
  boundary: >-
    The choice is set by ticket size and B2C versus B2B, not by preference.
  anchor: >-
    Bigger broader guarantees work better with lower ticket B2C businesses (many people just won't bother taking the time). The higher the ticket, and the more business oriented it is, the more you want to steer towards specific guarantees.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 736
  confirmations: 1
  anchor_at: "100m-offers.md:736"
- id: D-offers-026
  type: rule
  name: >-
    Implied guarantees need measurement and collection
  statement: >-
    Performance, revshare and profit-share structures are used only where the outcome is transparent to measure and you have the trust or control needed to be paid when you perform.
  why: >-
    Without that transparency and trust the structure cannot work; the drawbacks the author names are tracking and collection, and these offers work well when you have quantifiable outcomes.
  boundary: >-
    Only in situations with transparency for measuring the outcome and trust or control over getting compensated.
  anchor: >-
    These only work in situations where you have transparency for measuring the outcome and trust (or control) that you will get compensated when you do perform.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 690
  confirmations: 2
  anchor_at: "100m-offers.md:690"
- id: D-offers-027
  type: antipattern
  name: >-
    Vanilla guarantee naming
  statement: >-
    The guarantee is named with a generic word — "30 Day Money Back Satisfaction Guarantee".
  why: >-
    The author marks the generic version as bad and the creative-imagery versions as good and great; a named, vividly described guarantee is stronger than a "satisfaction" or other vanilla word.
  anchor: >-
    Instead of using “satisfaction” or some other “vanilla” word, describe it more strongly.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 716
  confirmations: 1
  anchor_at: "100m-offers.md:716"
- id: D-offers-028
  type: antipattern
  name: >-
    Guarantee as cover for a poor product
  statement: >-
    A guarantee is used to compensate for a poor sales team or a poor product.
  why: >-
    It backfires into lots of refunds; guarantees are enhancers that can enhance the attraction of any offer but cannot make a business.
  boundary: >-
    A guarantee enhances an offer; it cannot make a business.
  anchor: >-
    They can enhance the magnetism or attraction of any offer, but they cannot make a business. If a guarantee is used to cover up a poor sales team or a poor product, it will backfire into lots of refunds.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 851
  confirmations: 1
  anchor_at: "100m-offers.md:851"
- id: D-offers-029
  type: antipattern
  name: >-
    Slashing prices to get more customers
  statement: >-
    Prices are cut to fill the client load, and the business ends up full but barely making it on thin margins.
  why: >-
    Competition becomes a race to the bottom; more clients cost more money and time, and that money comes out of the margins, so both of the two big problems get worse at once.
  anchor: >-
    Let’s say you’ve slashed prices to get more customers. You may even have a full client load. But here you are, barely making it because profit margins are too thin.
  source: >-
    100m-offers.md, ch. 2 Grand Slam Offers, line 984
  confirmations: 1
  anchor_at: "100m-offers.md:984"
- id: D-offers-030
  type: antipattern
  name: >-
    Copying models built for funded companies
  statement: >-
    The owner runs the typical business model of his industry, which was never designed for profit maximization.
  why: >-
    Those models were designed by companies with boatloads of funding that can operate at a loss for years; used in the real world they leave owners barely getting by, buying themselves a job and working 100 hours a week to avoid working 40.
  anchor: >-
    Typical models weren’t designed for profit maximization. They were designed by companies who have boatloads of funding and can operate at a loss for *years*.
  source: >-
    100m-offers.md, ch. 2 Grand Slam Offers, line 990
  confirmations: 1
  anchor_at: "100m-offers.md:990"
- id: D-offers-031
  type: antipattern
  name: >-
    Widening the price-to-value gap by lowering the price
  statement: >-
    The gap between price and value is opened by cutting the price rather than by raising the value.
  why: >-
    It is most of the time the wrong decision: price can only go down to zero while value can go infinitely high in the other direction, and lowering price cuts emotional investment, perceived value, client results, client quality and the margin needed to deliver an exceptional service.
  boundary: >-
    Do not compete on price unless you have a revolutionary way of decreasing your costs to 1/10th of your competition.
  anchor: >-
    The simplest way to increase the gap between price to value is by lowering the price. It’s also, most of the time, the wrong decision for the business.
  source: >-
    100m-offers.md, ch. 5 Pricing: Charge What It’s Worth, line 1137
  confirmations: 2
  anchor_at: "100m-offers.md:1137"
- id: D-offers-032
  type: antipattern
  name: >-
    Optimizing for customers instead of money
  statement: >-
    The business treats getting people to buy — the number of customers — as its objective.
  why: >-
    Getting people to buy is not the objective of a business, making money is; the goal is not the most customers but the most money.
  anchor: >-
    Getting people to buy is NOT the objective of a business. Making money is.
  source: >-
    100m-offers.md, ch. 5 Pricing: Charge What It’s Worth, line 1139
  confirmations: 2
  anchor_at: "100m-offers.md:1139"
- id: D-offers-033
  type: antipattern
  name: >-
    Pricing off the market average
  statement: >-
    The owner looks at the marketplace, takes the average, goes slightly below it to stay "competitive" and offers a little more for a little less.
  why: >-
    That is pricing for market efficiency: competitors keep entering with a little more for a little less until no one can provide any more for any less and owners make just enough to keep going; and the competitors being copied are dead broke.
  anchor: >-
    Pricing where the market is means you’re pricing for market *efficiency*. Over time, in an efficient marketplace, more competitors enter offering “a little more for a little less,” until eventually no one can provide any more for any less.
  source: >-
    100m-offers.md, ch. 5 Pricing: Charge What It’s Worth, line 1162
  confirmations: 2
  anchor_at: "100m-offers.md:1162"
- id: D-offers-034
  type: antipattern
  name: >-
    Pricing slightly above the market
  statement: >-
    The premium is set just a little above the market price.
  why: >-
    The goal is to be so much higher that the consumer concludes there must be something entirely different going on here, which is what creates a category of one and monopoly profits; a small premium does not trigger that.
  anchor: >-
    And the goal isn’t just to be slightly above the market price
  source: >-
    100m-offers.md, ch. 5 Pricing: Charge What It’s Worth, line 1210
  confirmations: 1
  anchor_at: "100m-offers.md:1210"
- id: D-offers-035
  type: rule
  name: >-
    Premium pricing demands delivery
  statement: >-
    Charging big-ticket prices requires a product that delivers and conviction built by having done it many times; there is no shortcut around the real work.
  why: >-
    Those who wish to shortcut the real work will fail; experience is what gives the conviction to ask for someone's entire year's salary as payment.
  boundary: >-
    Premium pricing holds only where the product delivers — a precondition the author states before the tactics.
  anchor: >-
    Your product must *deliver*. So many wish to shortcut the real work. Do that and you *will* fail.
  source: >-
    100m-offers.md, ch. 5 Pricing: Charge What It’s Worth, line 1216
  confirmations: 1
  anchor_at: "100m-offers.md:1216"
- id: D-offers-036
  type: rule
  name: >-
    Scope of the enhancers
  statement: >-
    Of the persuasion tools at work in a sale, this book breaks down only scarcity, urgency, bonuses and guarantees, which belong to the offer rather than to the selling.
  why: >-
    Commitment and consistency, status, peer pressure, goodwill, celebrity endorsements and competition were also at play in the author's example, but he places them with the actual selling, treated in a different volume.
  boundary: >-
    Only the offer-side levers are in scope; selling itself is out of scope of this book.
  anchor: >-
    However, scarcity, urgency, and bonuses are the only three I will be breaking down in this book as I believe they belong more with the “offer” and less with the actual “selling,”
  source: >-
    100m-offers.md, ch. 11 Enhancing The Offer, line 1516
  confirmations: 1
  anchor_at: "100m-offers.md:1516"
- id: D-offers-037
  type: rule
  name: >-
    The supply-restriction assumption
  statement: >-
    Deliberately selling fewer units than you can to keep demand above supply assumes a regular business that is not pursuing mass market penetration.
  why: >-
    The author states the assumption directly beside the supply-and-demand model of enhancing an offer.
  boundary: >-
    Does not apply to a business trying to gain mass market penetration for some other strategic advantage.
  anchor: >-
    This assumes a regular business who is not trying to gain mass market penetration for some other strategic advantage.
  source: >-
    100m-offers.md, ch. 11 Enhancing The Offer, line 1528
  confirmations: 1
  anchor_at: "100m-offers.md:1528"
- id: D-offers-038
  type: antipattern
  name: >-
    Pulling the trigger too early
  statement: >-
    The promotion satisfies all the demand it generated — everyone who wants in gets in at the low price.
  why: >-
    With no pent up demand each successive promotion sells fewer units until there is not enough demand for a single sale; this is the state of businesses always trying to generate more demand for another quick sale.
  boundary: >-
    The opposite extreme also fails: satisfying zero desire makes no money and eventually leaves people feeling rejected, so supply is kept under demand rather than at zero.
  anchor: >-
    When you “pull the trigger too early,” each successive instance we promote, we sell even fewer.
  source: >-
    100m-offers.md, ch. 11 Enhancing The Offer, line 1551
  confirmations: 3
  anchor_at: "100m-offers.md:1551"
- id: D-offers-039
  type: rule
  name: >-
    The market assumption under the whole book
  statement: >-
    Everything in the book assumes at least a normal market — one growing at the rate of the marketplace with unmet needs in health, wealth or relationships; with no market for the offer, nothing that follows works.
  why: >-
    The author's friend Lloyd could have gone through the entire book and nothing would have worked, because he was targeting newspapers, a dying market; you cannot be in a bad market or nothing will work, and a Grand Slam Offer given to the wrong audience falls on deaf ears.
  boundary: >-
    The method presupposes a normal or better market; it does not repair a bad or dying one.
  anchor: >-
    If you don’t have a market for your offer, nothing that follows will work. This entire book sits atop the assumption that you have at least a “normal” market
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market, line 1621
  confirmations: 3
  anchor_at: "100m-offers.md:1621"
- id: D-offers-040
  type: antipattern
  name: >-
    Fixing everything except the market
  statement: >-
    A struggling owner works the product, the offer, the sales and the team while the market itself is shrinking.
  why: >-
    In the author's example the product was great, the offer was a zero-risk revshare and the owner was a natural salesman, but the market was shrinking 25 percent every year; entrepreneurs keep ramming their heads into the wall because they hate quitting, and everyone is affected by their market.
  anchor: >-
    It wasn’t his sales skills — he was a natural salesman. So, then what was the problem? *He was selling to newspapers!*
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market, line 1609
  confirmations: 2
  anchor_at: "100m-offers.md:1609"
- id: D-offers-041
  type: antipattern
  name: >-
    Being romantic about your audience
  statement: >-
    The market is chosen out of attachment to a particular audience rather than by pain, purchasing power, targeting and growth.
  why: >-
    Picking a market is always a choice, and the ones to serve are the people who can pay you what you are worth.
  anchor: >-
    Don’t be romantic about your audience. Serve the people who can pay you what you’re worth.
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market, line 1619
  confirmations: 1
  anchor_at: "100m-offers.md:1619"
- id: D-offers-042
  type: antipattern
  name: >-
    A market in pain with no purchasing power
  statement: >-
    A market is picked because it is in massive pain, plentiful and easy to target, while its members cannot afford the service — the resume expert selling to the unemployed.
  why: >-
    The audience needs to be able to afford the service you charge them for; the targets must have the money, or access to the money, needed to buy at the prices you require to make it worth your time.
  anchor: >-
    He just forgot a crucial point: your audience needs to be able to afford the service you’re charging them for.
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market, line 1651
  confirmations: 1
  anchor_at: "100m-offers.md:1651"
- id: D-offers-043
  type: antipattern
  name: >-
    A market you cannot target
  statement: >-
    The desired audience has no association, list, group or channel through which it can be reached, so the promotion is served to the wrong people.
  why: >-
    If your ads are displayed to nursing students when you want rich doctors, the offer falls on deaf ears no matter how good it is; if finding them is like finding needles in a haystack the offer never reaches interested eyes.
  anchor: >-
    But if your ads are being displayed to nursing students, your offer will fall on deaf ears, no matter how good it is.
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market, line 1657
  confirmations: 1
  anchor_at: "100m-offers.md:1657"
- id: D-offers-044
  type: antipattern
  name: >-
    Niche slap
  statement: >-
    The entrepreneur half-heartedly tries one offer in one market, does not make a million dollars, concludes the market is bad and hops to the next niche.
  why: >-
    Most times it is not a bad market, they just have not found a Grand Slam Offer for it; all markets have unpleasant characteristics, and hopping means starting over from the beginning each time, so you fail far longer.
  authors_caveat: >-
    The fix the author states is to pick one and commit long enough to have trial and error — you must pick one, no one can serve two masters.
  anchor: >-
    If you keep hopping from niche to niche, hoping that the market will solve your problems, you deserve to be *niche slapped.*
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market, line 1697
  confirmations: 2
  anchor_at: "100m-offers.md:1697"
- id: D-offers-045
  type: rule
  name: >-
    When To Broaden (Advice For Most People)
  statement: >-
    Below $10M per year, niching down makes more money; above it, whether to broaden depends on how narrow the niche is and on the total addressable market.
  why: >-
    A business can really only grow to meet its TAM, so beyond that point you may have to go up market, down market or into an adjacent market; but many companies expanded past $30M per year serving a single niche, and an owner at $1M or $3M who thinks he has capped is wrong.
  boundary: >-
    The niching advice is bounded by revenue: it holds for the 99.6 percent of readers under $10M per year, and above that TAM decides.
  anchor: >-
    For most, if you are under $10M per year, niching down will make you more money. After that, it will depend on how narrow the niche is, or, what is called TAM (total addressable market).
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market, line 1709
  confirmations: 1
  anchor_at: "100m-offers.md:1709"
- id: D-offers-046
  type: antipattern
  name: >-
    Taking a failed offer personally
  statement: >-
    A failed offer is read as a verdict on the person, and the attempt is abandoned after one failure.
  why: >-
    If the offer does not work it means the offer sucks, not that you suck; most people never try anything and others fail once then give up, while trying one hundred offers is what the author promises will succeed.
  anchor: >-
    If your offer doesn’t work, it doesn’t mean you suck. It means your offer sucks.
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market, line 1753
  confirmations: 1
  anchor_at: "100m-offers.md:1753"
- id: D-offers-047
  type: antipattern
  name: >-
    Declaring an offer fatigued too early
  statement: >-
    The offer is treated as burnt out after the audience has been reached once.
  why: >-
    Reaching an audience one time in no way means an offer is fatigued — most people do not even notice an offer on the first mention; offers can be used for years, and what is changed first is creative, hooks, stories and copy around the same offer.
  boundary: >-
    Real fatigue is a matter of years of use, not months, and comes faster in local markets.
  anchor: >-
    Important disclaimer: reaching an audience one time in *no way* means an offer is fatigued. Most people don’t even notice an offer on the first mention.
  source: >-
    100m-offers.md, ch. 16 Naming, line 1969
  confirmations: 2
  anchor_at: "100m-offers.md:1969"
- id: D-offers-048
  type: rule
  name: >-
    Three to five M-A-G-I-C components
  statement: >-
    A name uses three to five of the M-A-G-I-C components, not all of them, and not necessarily in that order.
  why: >-
    Not all the components are mandatory; fitting them all in is likely to make the name too long, and the balance wanted is between brevity and specificity.
  boundary: >-
    The formula is a set of optional components, not a mandatory template.
  anchor: >-
    Important Note: Not all these components are mandatory. You will typically use three to five of them in naming a program or service. If you can fit them all in, great, but it’s likely the name will become too long.
  source: >-
    100m-offers.md, ch. 16 Naming, line 1981
  confirmations: 2
  anchor_at: "100m-offers.md:1981"
- id: D-offers-049
  type: rule
  name: >-
    Duration with a quantifiable claim
  statement: >-
    A quantifiable claim such as income gain or weight loss is not combined with a stated duration to achievement unless the platform allows it.
  why: >-
    Most platforms will not approve that messaging because a duration implies a guarantee, which goes against their rules; where the goal is not a claim per se, the time interval should absolutely be used.
  boundary: >-
    A platform-compliance limit: use duration freely anywhere you do not have to deal with compliance.
  anchor: >-
    Note: If you’re making any sort of quantifiable claim (like income gain or weight loss) most platforms will *not* approve this type of messaging *with* a stated duration to achievement because it implies a guarantee.
  source: >-
    100m-offers.md, ch. 16 Naming, line 2021
  confirmations: 1
  anchor_at: "100m-offers.md:2021"
- id: D-offers-050
  type: rule
  name: >-
    Why names win is not knowable in advance
  statement: >-
    Which names take off cannot be predicted; two to three of the best names are run in the campaign, the winner is noted and used as the control to test new names against.
  why: >-
    The author states he honestly has no idea why some names win and others do not, so the only way to know what works is to write the names out and test them.
  boundary: >-
    The author marks the limit of his own knowledge here, and warns against being emotional about a name that loses.
  anchor: >-
    I honestly have no idea why some names win and others do not. So, don’t be emotional about it.
  source: >-
    100m-offers.md, ch. 16 Naming, line 2081
  confirmations: 2
  anchor_at: "100m-offers.md:2081"
- id: D-offers-051
  type: antipattern
  name: >-
    Changing the machine instead of the wrapper
  statement: >-
    When results dip, the business changes the offer itself — or keeps changing an offer that is already monetized — instead of the creative, the copy and the headline.
  why: >-
    The lower on the variation list you go, the more operationally heavy it is; change there usually just creates inefficiency and operational drag, costing you money, and entrepreneurs do it because they love change.
  authors_caveat: >-
    The author's order is creative, then body copy, then the headline or wrapper, then seasonality, then duration, then the free or discount component, and the whole machine only as a last resort and for a darn good reason.
  anchor: >-
    Change here usually just creates inefficiency and operational drag, costing you money.
  source: >-
    100m-offers.md, ch. 16 Naming, line 2108
  confirmations: 3
  anchor_at: "100m-offers.md:2108"
- id: D-offers-052
  type: rule
  name: >-
    Local markets fatigue offers fast
  statement: >-
    A local business has to vary its marketing far more frequently than a national advertiser, changing the look of the offer rather than its value stack.
  why: >-
    The total addressable market of a brick and mortar is only its immediate radius, so the smaller the radius the faster offers fatigue; local is easier to get working because of trust in the familiar, and harder to keep working.
  boundary: >-
    A limit set by geography: it applies to local and brick-and-mortar businesses, not to national advertising.
  anchor: >-
    The downside of local marketing is that offers fatigue rapidly because there is only a limited radius that a local business can serve.
  source: >-
    100m-offers.md, ch. 16 Naming, line 2120
  confirmations: 2
  anchor_at: "100m-offers.md:2120"
- id: D-offers-053
  type: antipattern
  name: >-
    Lazy naming
  statement: >-
    The product or offer is named half-heartedly.
  why: >-
    Half-ass naming can ruin conversions; people do judge a book by its cover, and proper naming can get the same offer 2x, 3x or 10x the response rate.
  anchor: >-
    Half-ass naming your product or offering can ruin conversions. Don’t fall victim to lazy naming.
  source: >-
    100m-offers.md, ch. 16 Naming, line 2126
  confirmations: 1
  anchor_at: "100m-offers.md:2126"
- id: D-offers-054
  type: antipattern
  name: >-
    Maintenance is a myth
  statement: >-
    The business aims to maintain its current size rather than grow.
  why: >-
    Every person, company and organism is either growing or dying; the market grows about 9 percent a year, so flat means falling behind, and in a growing marketplace you may have to grow 20-30 percent a year just to keep up.
  anchor: >-
    We believe every person, every company, and every organism is either growing or dying. Maintenance is a myth.
  source: >-
    100m-offers.md, ch. 3 Pricing: The Commodity Problem, line 2174
  confirmations: 1
  anchor_at: "100m-offers.md:2174"
- id: D-offers-055
  type: antipattern
  name: >-
    Letting the prospect commoditize you
  statement: >-
    The offer is close enough to the alternatives that the prospect concludes they are pretty much the same and buys the cheaper one.
  why: >-
    Commodities are valued at the point of market efficiency: the marketplace drives price down until margins are just enough to keep the lights on; commoditized marketing also gets fewer responses because it all looks the same, since everyone is making the same offer.
  anchor: >-
    if a prospect compares your product to another and thinks “these are pretty much the same, I’ll buy the cheaper one,” then they commoditized you.
  source: >-
    100m-offers.md, ch. 3 Pricing: The Commodity Problem, line 2230
  confirmations: 2
  anchor_at: "100m-offers.md:2230"
- id: D-offers-056
  type: rule
  name: >-
    The offer rests on a valuable product
  statement: >-
    The enhancers and the rest of the book are less actionable without a valuable product or service underneath them.
  why: >-
    The author calls the trim-and-stack chapter the meatiest and most important in the book for exactly that reason, and the offer must be both incredibly attractive and profitable.
  boundary: >-
    A precondition on the whole method: no valuable product, no actionable offer.
  anchor: >-
    Without a valuable product or service, the rest of the book won’t be as actionable
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, line 2379
  confirmations: 1
  anchor_at: "100m-offers.md:2379"
- id: D-offers-057
  type: rule
  name: >-
    Over-deliver on the first offer
  statement: >-
    On a first Grand Slam Offer the business over-delivers like crazy, even doing things that will not scale, and only fixes operations afterwards out of the cash flow.
  why: >-
    You want the client to think "I get all this, for only that?"; the author flew out to gyms at his own cost at the start, then used the cash flow to make the business efficient.
  boundary: >-
    A stage boundary: this holds for the first offer, not as the permanent operating model.
  anchor: >-
    That being said, if this is your first Grand Slam Offer, it’s important to over-deliver like crazy.
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, line 2381
  confirmations: 1
  anchor_at: "100m-offers.md:2381"
- id: D-offers-058
  type: antipattern
  name: >-
    Adding friction before flow
  statement: >-
    The business optimizes what it delivers — offering less for the same price — before demand is flowing.
  why: >-
    If you cannot get demand flowing in you have no idea whether what you have is good; the author would rather do more for every customer with cash coming in than run an optimized business with none, and no idea what to adjust.
  authors_caveat: >-
    The author's order is his mantra: create flow, monetize flow, then add friction.
  anchor: >-
    If you can’t get demand flowing in, then you have no idea whether what you have is good.
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, line 2397
  confirmations: 1
  anchor_at: "100m-offers.md:2397"
- id: D-offers-059
  type: antipattern
  name: >-
    Getting romantic about how you solve the problem
  statement: >-
    An obstacle a prospect raises is met with "do it my way or not at all" instead of a solution built for it — the author insisting clients never eat out.
  why: >-
    He lost many sales over that one thing; one single item becomes the reason someone does not buy, and if only one of the four value-driver needs is missing in a solution it can stop the purchase.
  authors_caveat: >-
    Not resolving every obstacle does not mean you will sell no one; it means you will not sell as many people as you otherwise could have.
  anchor: >-
    Don’t get romantic about *how* you want to solve the problem. Find a way to solve every problem a prospect presents with.
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, line 2483
  confirmations: 3
  anchor_at: "100m-offers.md:2483"
- id: D-offers-060
  type: antipattern
  name: >-
    Keeping high-cost items that are not big value adds
  statement: >-
    Expensive one-on-one or small-group delivery is kept in the bundle for things a cheaper vehicle could deliver just as well.
  why: >-
    High cost items are saved for big value adds only; if the same value can be accomplished with a lower cost alternative, do that instead, and the biggest discrepancy between cost and value sits in high value one-to-many solutions.
  anchor: >-
    You just want to make sure you save those high cost items for *big* value adds only.
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, line 2510
  confirmations: 2
  anchor_at: "100m-offers.md:2510"
- id: D-offers-061
  type: antipattern
  name: >-
    Letting the four problem buckets constrain the list
  statement: >-
    The problem list is limited to the four value-driver buckets instead of everything the prospect might think.
  why: >-
    The buckets are only meant to get your brain going; the more problems you think of, the more problems you get to solve, and if it is easier you should just list everything you can possibly think of.
  anchor: >-
    Don’t let these buckets, which are just meant to get your brain going, constrain you.
  source: >-
    100m-offers.md, ch. 9 Creating Your Grand Slam Offer Part I, line 2907
  confirmations: 1
  anchor_at: "100m-offers.md:2907"
- id: D-offers-062
  type: rule
  name: >-
    Copywriting is out of scope
  statement: >-
    Turning problems into solutions uses a minimal device — add "how to" and reverse the problem — because the copywriting behind it is not taught here.
  why: >-
    The author marks copywriting 101 as beyond the scope of the book and gives the reversal as a starting place for people new to the process.
  boundary: >-
    Copywriting itself is out of scope of this book.
  anchor: >-
    This is copywriting 101. It’s beyond the scope of this book to get into
  source: >-
    100m-offers.md, ch. 9 Creating Your Grand Slam Offer Part I, line 2919
  confirmations: 1
  anchor_at: "100m-offers.md:2919"
```
