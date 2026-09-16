# Улов фазы 1 — $100M Playbooks: Pricing, Price Raise, Lifetime Value (2025) (ярус 2), тип B: правила и критерии

Группа `tier2-playbooks-price`, слаг `playbooks-price`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **64** (экстрактор вернул 64, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `playbook-pricing.md` | 1–1381 | 2 | 31 |
| `playbook-price-raise.md` | 1–758 | 2 | 18 |
| `playbook-lifetime-value.md` | 1–613 | 1 | 15 |

## Как собран файл

Экстрактор B (Rules and criteria) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-playbooks-price.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-playbooks-price-B.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: B-playbooks-price-001
  type: rule
  name: >-
    value Based Pricing
  statement: >-
    The price is set on what the customer is willing to pay for the value delivered, not on your costs plus a margin and not on the average of what competitors charge.
  why: >-
    Costs change, are not known in advance and mean nothing to the customer; competitor pricing is built on someone else's business and customers. Willingness to pay rises as you make the product more valuable, so a value-based price can be raised continuously.
  anchor: >-
    Value-based pricing is where we want to be.
  source: >-
    playbook-pricing.md, Three Models Of Pricing, lines 336–377
  confirmations: 1
  authors_caveat: >-
    It focuses on value per customer rather than on getting the most customers, so it takes a different kind of work than most people are used to.
  anchor_at: "playbook-pricing.md:376"
- id: B-playbooks-price-002
  type: rule
  name: >-
    The perfect price
  statement: >-
    Of the prices you have data on, the chosen price is the one that makes the most money, not the one that gets the most customers.
  why: >-
    The goal is not to sell the most stuff, it is to make the most money, which is what keeps you in business and able to help people longer.
  applies_when: >-
    Any price decision, unless you are running a different short term strategy.
  anchor: >-
    Unless you have a different short term strategy, the perfect price is the
  source: >-
    playbook-pricing.md, Three Metrics To Determine value-Driven Pricing, lines 384–385
  confirmations: 3
  anchor_at: "playbook-pricing.md:384"
- id: B-playbooks-price-003
  type: rule
  name: >-
    Bottom Line of the price table
  statement: >-
    A price is judged on total return, conversion rate multiplied by lifetime gross profit, rather than on conversion rate or price alone.
  why: >-
    Price affects both conversion rate and churn, and both suffer as price goes up, but not always proportionally; you may lose some, but often not as much as you gain.
  applies_when: >-
    You have conversion rate, churn and lifetime value recorded for several tested price points.
  anchor: >-
    Bottom Line: I want the thing that converts the highest number of people at the high-
  source: >-
    playbook-pricing.md, Three Metrics To Determine value-Driven Pricing, lines 395–397
  confirmations: 2
  anchor_at: "playbook-pricing.md:395"
- id: B-playbooks-price-004
  type: rule
  name: >-
    Price to make the most money, not to maximize the first purchase
  statement: >-
    The price is chosen to make the most money over the lifetime of the customer, not the highest price obtainable on their first purchase.
  why: >-
    If customers buy different things from you, or buy the same thing several times, pricing has to account for that; the aim is the price people will keep paying at, not the highest price you can get them to buy at once.
  applies_when: >-
    Any business where customers buy more than once.
  anchor: >-
    Price to make the most money, not sell the most customers, or to maximize the first
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 412–417
  confirmations: 2
  anchor_at: "playbook-pricing.md:412"
- id: B-playbooks-price-005
  type: rule
  name: >-
    High close rate = prices too low
  statement: >-
    If you consistently close more than 50% of sales and want to make more money, the price is raised.
  why: >-
    A close rate that high is evidence there is room in the price; higher prices get fewer new customers but often make the business more money.
  applies_when: >-
    You want to make more money and close over 50% of sales consistently.
  anchor: >-
    High close rate = prices too low . If want to make more money, and you close over 50%
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 421–422
  confirmations: 1
  anchor_at: "playbook-pricing.md:421"
- id: B-playbooks-price-006
  type: rule
  name: >-
    Full capacity = prices too low
  statement: >-
    If you have hit capacity, and especially if capacity is fixed and sells out every period, the price is raised.
  why: >-
    With no room to serve more customers, more money can only come from charging more for the same capacity.
  applies_when: >-
    You want to make more money and you are already full.
  anchor: >-
    Full capacity = prices too low . Like the above, if you want to make more money but
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 423–427
  confirmations: 2
  anchor_at: "playbook-pricing.md:423"
- id: B-playbooks-price-007
  type: rule
  name: >-
    Keep raising prices until the extra money no longer offsets the loss in sales
  statement: >-
    Prices keep going up until the extra money made from the remaining sales no longer offsets the sales lost, and the price is not changed back at the first no.
  why: >-
    Going from a 50% close rate to a 30% close rate while doubling the price makes more money, even though you hear no 40% more often; 9 times out of 10 raising prices makes more profit than is lost in sales.
  applies_when: >-
    Any price test where you are willing to stomach a higher rate of rejection.
  anchor: >-
    Keep raising prices until the amount of extra money you make from new sales no
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 428–438
  confirmations: 1
  authors_caveat: >-
    Some markets are price sensitive and others less so; the 9-out-of-10 rate is the author's experience, not a guarantee.
  anchor_at: "playbook-pricing.md:428"
- id: B-playbooks-price-008
  type: rule
  name: >-
    Raising your prices usually means raising the value
  statement: >-
    Every price increase is paired with a matching increase in the value of the product, and the bigger the price increase the bigger the value increase.
  why: >-
    The product is made better to justify the price increase, which is what lets the price be raised again later.
  applies_when: >-
    Any deliberate price increase.
  anchor: >-
    Raising your prices usually means raising the value . If I want to sell something for a
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 439–441
  confirmations: 2
  anchor_at: "playbook-pricing.md:439"
- id: B-playbooks-price-009
  type: rule
  name: >-
    How to know you raised your prices too much
  statement: >-
    The price has gone too far when sales stop, or when customers start complaining about the value for the cost, measured objectively with NPS scores.
  why: >-
    These are the two observable signals that the price has passed what the market will bear, as opposed to simply hearing more nos.
  applies_when: >-
    After a price increase has been rolled out.
  anchor: >-
    How to know you raised your prices too much . You stop making sales. Or, people start
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 449–450
  confirmations: 1
  anchor_at: "playbook-pricing.md:449"
- id: B-playbooks-price-010
  type: rule
  name: >-
    Different customers, different prices
  statement: >-
    If the business has more than one type of customer, it carries a different price and level of service for each of them.
  why: >-
    Different customers have different pricing thresholds, and it is not uncommon for one avatar to have 5-10x the willingness to pay of another; separate prices maximize revenue across the whole customer base.
  applies_when: >-
    You have 2-3 customer avatars within the business.
  anchor: >-
    If you have more than one type of customer, you need to have different prices for
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 451–460
  confirmations: 1
  authors_caveat: >-
    The author calls this a more advanced strategy that requires the operational chops to deliver at different levels.
  anchor_at: "playbook-pricing.md:451"
- id: B-playbooks-price-011
  type: rule
  name: >-
    Name pricing tiers after an aspirational title
  statement: >-
    Each pricing tier is named after an aspirational title the customer wants for themselves, and the customer is told which tier is for them.
  why: >-
    With multiple tiers the customer has to be able to see which one is theirs.
  applies_when: >-
    The offer has multiple pricing tiers.
  anchor: >-
    Name pricing tiers after an aspirational title that a customer
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 458–460
  confirmations: 1
  anchor_at: "playbook-pricing.md:459"
- id: B-playbooks-price-012
  type: rule
  name: >-
    Believe in your price
  statement: >-
    You either believe the product is worth the price you would have to charge to make the money you want, or you make the product better until you do.
  why: >-
    Conviction in the price is a precondition for charging it; without it, owners cave and go back to charging less.
  anchor: >-
    Believe in your price . You have to believe your product is worth the price you’d have to
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 461–462
  confirmations: 1
  anchor_at: "playbook-pricing.md:461"
- id: B-playbooks-price-013
  type: rule
  name: >-
    Bill less frequently to have lower churn
  statement: >-
    Billing is set as far out as the business can push it, because each billing cycle is an opportunity to cancel.
  why: >-
    The more often you bill the more often people cancel, and the longer between billing cycles the longer you have to provide value; value is judged inside the lookback window of the last billing cycle, not the whole relationship. Profitwell data in the book shows 2% monthly churn on annual billing against 10.7% on monthly (2025).
  anchor: >-
    Bill less frequently to have lower churn . The more often you bill the more often peo-
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 463–466
  confirmations: 3
  authors_caveat: >-
    The lookback-window explanation is flagged by the author as his theory, not established fact.
  anchor_at: "playbook-pricing.md:463"
- id: B-playbooks-price-014
  type: rule
  name: >-
    Display price in the smallest increment, bill on the longest increment
  statement: >-
    The price is displayed in the smallest time increment and billed on the longest one, since the two do not have to match.
  why: >-
    The small increment gives the lowest perceived price while the long billing cycle gives the profit and the lower churn.
  applies_when: >-
    Any recurring offer where the display price and the billing cycle can differ.
  anchor: >-
    Display price in the smallest increment, bill on the longest increment . How you dis-
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 480–482
  confirmations: 2
  anchor_at: "playbook-pricing.md:480"
- id: B-playbooks-price-015
  type: rule
  name: >-
    Match how you bill with how you provide value
  statement: >-
    One-time value is billed as a one-time fee and ongoing value as a separate, smaller recurring fee, rather than being mixed into a single price.
  why: >-
    Mixed pricing underprices the one-time part and overprices the ongoing part; the day after someone learns something, access to that information is worth close to zero, so they stop paying. Pricing should be tied to value created.
  applies_when: >-
    The offer contains both a one-time component and an ongoing one.
  anchor: >-
    Match how you bill with how you provide value . One-Time vs On-Going Value Pric-
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 483–492
  confirmations: 1
  anchor_at: "playbook-pricing.md:483"
- id: B-playbooks-price-016
  type: rule
  name: >-
    Customer Surplus
  statement: >-
    You bill as much as you can while still leaving the customer more value than they paid for.
  why: >-
    The difference between price and value is customer surplus, and it dictates word of mouth and repurchase rate; a premium price funds the gross profit needed to make a far superior product, which produces surplus for them and net profit for you.
  anchor: >-
    Bill as much as you can while keeping customers happy . Customer Surplus. The dif-
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 493–498
  confirmations: 1
  anchor_at: "playbook-pricing.md:493"
- id: B-playbooks-price-017
  type: rule
  name: >-
    Pricing Play #1: Monthly to 28 Day Billing Cycles
  statement: >-
    Recurring billing runs on 4-week (28 day) or 12-week cycles rather than calendar months, with the price displayed weekly.
  why: >-
    Monthly billing gives 12 cycles a year, every 28 days gives 13, and the extra cycle is pure profit at the same conversion rate: an instant and permanent 8.3% increase in revenue, which on a 20% net margin business raises net profit by 41.5% (2025).
  applies_when: >-
    Any subscription or membership.
  anchor: >-
    Switch to billing every 4 weeks. It gives you the best of all worlds. Theoretically weekly,
  source: >-
    playbook-pricing.md, Pricing Play #1: Monthly to 28 Day Billing Cycles, lines 586–612
  confirmations: 1
  authors_caveat: >-
    Weekly and bi-weekly billing yields the same benefit in theory but in practice caused billing hassles because people wanted short pauses, so the author sticks to 4 weeks or longer.
  anchor_at: "playbook-pricing.md:608"
- id: B-playbooks-price-018
  type: rule
  name: >-
    Pricing Play #2: Processing Fees & Second Form of Payment
  statement: >-
    After the customer agrees to the price, a card processing fee of about 3.99% is added at the payment step, and it is waived for anyone who puts a second form of payment on file.
  why: >-
    The fee adds 3-4% of revenue for no extra work and the author has never seen a sale lost over it; the waiver buys a second card, which removes the 1.2%-1.7% monthly involuntary churn caused by card declines, worth far more in LTV than the fee.
  applies_when: >-
    Any recurring billing taken by card.
  anchor: >-
    1) After the customer agrees to the price, ask, “How did you want to pay?”
  source: >-
    playbook-pricing.md, Pricing Play #2: Processing Fees & Second Form of Payment, lines 628–672
  confirmations: 1
  anchor_at: "playbook-pricing.md:630"
- id: B-playbooks-price-019
  type: rule
  name: >-
    Pricing Play #3: Sales Tax
  statement: >-
    Sales tax is charged on top of the agreed price and shown as a separate line item before the total, instead of being absorbed out of your margin.
  why: >-
    Sales tax comes off the top line, so a business with 20% margins that pays 5% sales tax for its customers gives away 25% of its profit; customers are not offended by tax at a restaurant checkout and are not offended by it here either.
  applies_when: >-
    Your state or country charges sales tax on what you sell.
  anchor: >-
    3) Put the tax as a separate line item before the total
  source: >-
    playbook-pricing.md, Pricing Play #3: Sales Tax, lines 714–724
  confirmations: 1
  authors_caveat: >-
    Pro Tip at line 702: if you do not get charged taxes, you cannot charge them.
  anchor_at: "playbook-pricing.md:721"
- id: B-playbooks-price-020
  type: rule
  name: >-
    Pro Tip: Menu Pricing
  statement: >-
    Publicly displayed prices and menus carry a line at the bottom stating that all prices are subject to sales tax and an additional processing fee.
  why: >-
    It is the one change that lets a published price list take both the tax and the fee without renegotiating each sale.
  applies_when: >-
    You have a menu or publicly displayed pricing.
  anchor: >-
    If you have a menu or publicly displayed pricing, just add a line at the bottom
  source: >-
    playbook-pricing.md, Pricing Play #3: Sales Tax, Pro Tip: Menu Pricing, lines 729–732
  confirmations: 1
  anchor_at: "playbook-pricing.md:730"
- id: B-playbooks-price-021
  type: rule
  name: >-
    Pricing Play #4: Annual Price Increases
  statement: >-
    New contracts contain a fixed annual price increase of 5 to 15 percent, raised at paperwork rather than pitched during the sale.
  why: >-
    Costs and inflation go up whether you act or not, so a business that has not adjusted prices in five years has already changed its prices, in the wrong direction; $100 in 2024 bought what $79 bought in 2017, and a 5% annual step compounds to 22% over four years (2025).
  applies_when: >-
    Any contract or subscription that renews over years.
  anchor: >-
    Pick a reasonable percentage 5 to 15 percent is a good place to start. Simply add it to
  source: >-
    playbook-pricing.md, Pricing Play #4: Annual Price Increases, lines 760–810
  confirmations: 2
  authors_caveat: >-
    Few people balk if you keep it under 15%.
  anchor_at: "playbook-pricing.md:802"
- id: B-playbooks-price-022
  type: rule
  name: >-
    Pricing Play #5: Annual Billing
  statement: >-
    Longer-duration payment options (annual, quarterly) are offered alongside the monthly price, each with a discount or prepayment bonus.
  why: >-
    Churn is directly correlated with billing frequency, so getting customers to pay annually can 5x LTV; offering the option risks nothing because you can always revert to standard pricing. With a 16% annual discount the author sees 10-15% take it on a page, 30% when it is the default, 35-40% over the phone (2025).
  applies_when: >-
    Any recurring offer, as an added option rather than the only cadence.
  anchor: >-
    But, simply offering either payment option with some incentive (either a discount or
  source: >-
    playbook-pricing.md, Pricing Play #5: Annual Billing, lines 826–889
  confirmations: 1
  authors_caveat: >-
    Requiring annual billing only is called a pretty advanced move; it drops conversions because the price is 12x the monthly rate, and whether it drops them 5x has to be tested.
  anchor_at: "playbook-pricing.md:867"
- id: B-playbooks-price-023
  type: rule
  name: >-
    Pro Tip: Always Start With Highest Price
  statement: >-
    You say the highest number first — the monthly payments added up over the full term with no discount — and then present the prepayment discounts as downsells.
  why: >-
    The first number out of your mouth anchors the entire conversation, and this positions the cheaper prepayment as a benefit rather than making monthly payments look like a penalty.
  applies_when: >-
    Presenting payment options in a sales conversation.
  anchor: >-
    The first number that comes out of your mouth anchors the entire conversation.
  source: >-
    playbook-pricing.md, Pricing Play #5: Annual Billing, Pro Tip: Always Start With Highest Price, lines 878–885
  confirmations: 2
  anchor_at: "playbook-pricing.md:879"
- id: B-playbooks-price-024
  type: rule
  name: >-
    Pricing Play #6: Round Up
  statement: >-
    Prices ending in 7 are changed to 9 and .99 is added to every fee, on new contracts immediately.
  why: >-
    In the author's gyms this added $104 to $155.48 per client per year, a 4.25% to 11.1% price increase, with no change in closing rate; on a gym's 12.5% net margins that nearly doubles profit (2025).
  applies_when: >-
    Non-luxury and premium goods.
  anchor: >-
    Change 7s to 9s. Add .99 to all fees. This takes so little time, and the only thing easier
  source: >-
    playbook-pricing.md, Pricing Play #6: Round Up, lines 946–963
  confirmations: 1
  authors_caveat: >-
    Not for luxury items, which end on a round number because buyers of luxury want not to get a deal; premium is not luxury, so premium goods still take the .99. Test it: sometimes shorter numbers do better.
  anchor_at: "playbook-pricing.md:958"
- id: B-playbooks-price-025
  type: rule
  name: >-
    Pro Tip: Have A Setup Fee And An Annual Renewal Fee
  statement: >-
    The contract carries both a setup fee and an annual renewal fee, so that one can be waived to get the other.
  why: >-
    Having both gives you something to give away when a customer needs an incentive to take action.
  applies_when: >-
    You need to incentivise a customer to sign.
  anchor: >-
    Having both a setup fee and a renewal fee allows you to waive one of them to
  source: >-
    playbook-pricing.md, Pricing Play #7: Annual Renewal Fee On Top of Monthly, lines 1009–1012
  confirmations: 1
  anchor_at: "playbook-pricing.md:1010"
- id: B-playbooks-price-026
  type: rule
  name: >-
    Pricing Play #7: Annual Renewal Fee On Top of Monthly
  statement: >-
    An annual renewal fee of 1-3x the monthly rate sits on top of the advertised monthly price, carries a benefit-framed reason why, and is initialled separately in the contract.
  why: >-
    People focus on the monthly price and rarely consider the annualized cost, so the fee lifts annual revenue per customer (1x monthly = +8.3%, 3x = +24.9%) without affecting sales conversions, and you keep the low advertised price for marketing.
  applies_when: >-
    Markets that are price conscious enough that you cannot simply bill annually.
  anchor: >-
    Step #1: Pick a renewal fee that’s 1-3x your monthly rate. This adds a big increase to
  source: >-
    playbook-pricing.md, Pricing Play #7: Annual Renewal Fee On Top of Monthly, lines 1013–1029
  confirmations: 1
  authors_caveat: >-
    If the customer balks at the fee you drop it and they do not get the benefit it was attached to; if you can bill annually instead, do that.
  anchor_at: "playbook-pricing.md:1014"
- id: B-playbooks-price-027
  type: rule
  name: >-
    Pricing Play #8: Automatic Continuity
  statement: >-
    Every front-end offer has a stripped-down, near-zero-work version priced at 5-20% of the main price bolted onto the end of the purchase, recurring automatically.
  why: >-
    Against the main price the continuity price seems small and sunk cost makes people keep it; in the author's example it adds 32% to LTV and $1800 of profit per customer, and it builds a pool of low-ticket customers to remarket to instead of losing them.
  applies_when: >-
    Anything you sell on the front end, including one-time transactions, where the continuity starts after a fixed period.
  anchor: >-
    You price it at 5% to 20% of the main thing. Then, you simply ‘tack it’ at the end of
  source: >-
    playbook-pricing.md, Pricing Play #8: Automatic Continuity, lines 1055–1124
  confirmations: 2
  anchor_at: "playbook-pricing.md:1061"
- id: B-playbooks-price-028
  type: rule
  name: >-
    Pro Tip: Don’t Be A Sneak
  statement: >-
    Continuity is agreed to up front and what happens after the initial term is stated clearly; it is never undisclosed or forced.
  why: >-
    In the author's experience people like knowing there is a more cost effective version at the end, and everyone knows they have the term to cancel, which is why disclosed continuity does not affect sales.
  anchor: >-
    is continuity they must agree to up front. So, be clear about what happens after
  source: >-
    playbook-pricing.md, Pricing Play #8: Automatic Continuity, Pro Tip: Don’t Be A Sneak, lines 1092–1096
  confirmations: 1
  anchor_at: "playbook-pricing.md:1094"
- id: B-playbooks-price-029
  type: rule
  name: >-
    Pricing Play #9: Ultra High Ticket Anchor
  statement: >-
    The product suite contains an offer priced at 10x or more of the core offer, and it is presented first.
  why: >-
    The high price anchors the prospect, so the core offer looks affordable and closes more often, while the few who take the anchor lift LTV sharply (from $440 to $890 per customer in the book's example at a 10% take rate).
  anchor: >-
    do is add something to your suite of products or services that’s 10x or more expensive than
  source: >-
    playbook-pricing.md, Pricing Play #9: Ultra High Ticket Anchor, lines 1140–1184
  confirmations: 1
  authors_caveat: >-
    Only offer what you are actually willing to deliver: if someone buying it stresses you, keep raising the price until it makes you smile when they buy.
  anchor_at: "playbook-pricing.md:1143"
- id: B-playbooks-price-030
  type: rule
  name: >-
    Pricing Play #10: Guarantee and Warranty Upsells
  statement: >-
    After the customer has agreed to buy, a paid guarantee or warranty is offered at 5-30% of the product price, priced so that its revenue exceeds the cost of honouring it.
  why: >-
    You are buying and selling risk, so with known claim rates the fee is nearly pure profit and you cover the cost of delivering again rather than refunding; if cost of goods is 10% of price, pricing the guarantee at 10% means you never lose a dollar.
  applies_when: >-
    Products or services at any price point, added as one line to the sales script after purchase.
  anchor: >-
    offer a guarantee for 5-30% of the price of the product.
  source: >-
    playbook-pricing.md, Pricing Play #10: Guarantee and Warranty Upsells, lines 1202–1227
  confirmations: 1
  anchor_at: "playbook-pricing.md:1204"
- id: B-playbooks-price-031
  type: rule
  name: >-
    Pick one or two plays
  statement: >-
    From the ten pricing plays you implement the one or two with the biggest impact for the least work and risk, rather than all of them.
  why: >-
    Some plays will not be a direct fit for your business, and you only need one to make more money immediately.
  anchor: >-
    For now, pick the one or two that could make the biggest impact in your business for
  source: >-
    playbook-pricing.md, The *Instant Profit* Pricing Playbook, lines 1375–1378
  confirmations: 2
  anchor_at: "playbook-pricing.md:1377"
- id: B-playbooks-price-032
  type: rule
  name: >-
    Don’t grandfather existing customers. Don’t do lifetime deals.
  statement: >-
    Existing customers are not locked into their old price and no lifetime deals are sold; when value goes up, their price goes up too.
  why: >-
    Value depends on price, and locking a price limits your options because you never know what you will want to deliver in the future.
  anchor: >-
    If your value goes up, so should your price. Never lock your customers into a price if
  source: >-
    playbook-price-raise.md, My Rules For Raising Prices, lines 211–214
  confirmations: 1
  anchor_at: "playbook-price-raise.md:212"
- id: B-playbooks-price-033
  type: rule
  name: >-
    Never sell a “one time price” for lifetime access
  statement: >-
    A one-time price for lifetime access is never sold unless fulfilment truly costs zero dollars.
  why: >-
    Forever lasts a lot longer than what they paid once, so you end up with upset customers when the money runs out but the commitment remains; no large company offers lifetime access for a one-time payment, so model success, not failure.
  applies_when: >-
    Designing access terms for any product with ongoing delivery cost.
  anchor: >-
    Never sell a “one time price” for lifetime access . Unless it truly costs you zero dollars
  source: >-
    playbook-price-raise.md, My Rules For Raising Prices, lines 215–222
  confirmations: 2
  anchor_at: "playbook-price-raise.md:215"
- id: B-playbooks-price-034
  type: rule
  name: >-
    Raise prices at least once per year
  statement: >-
    Pricing is revisited at least annually, first to cover inflation and then to cover other costs that have gone up.
  why: >-
    Warren Buffett kept price as the only decision he controlled at See's Candies, raising them on average 10% per year and up to 17% in some years over 50+ years; costs rise whether or not you act.
  anchor: >-
    For that reason, you should absolutely revisit your pricing at least annually. First, make
  source: >-
    playbook-price-raise.md, Why You Should Actually Do This, lines 669–671
  confirmations: 3
  anchor_at: "playbook-price-raise.md:669"
- id: B-playbooks-price-035
  type: rule
  name: >-
    Test price raises on new customers before rolling out to your entire customer base
  statement: >-
    A price raise is tested on new customers first, and only rolled out to the existing base once churn has not spiked and sales have not collapsed at the new rate.
  why: >-
    It gives you data on whether the new price actually makes more money, it gives you confidence when you present it to the base, and it shows the base that the marketplace has already agreed with the new value.
  applies_when: >-
    Any price raise on an existing customer base.
  anchor: >-
    Test price raises on new customers before rolling out to your entire customer base .
  source: >-
    playbook-price-raise.md, My Rules For Raising Prices, lines 234–238
  confirmations: 3
  anchor_at: "playbook-price-raise.md:234"
- id: B-playbooks-price-036
  type: rule
  name: >-
    Meet with people if you raise prices more than 50%
  statement: >-
    A price raise of 50% or more is delivered in individual conversations with customers, on top of everything else in the playbook.
  why: >-
    A raise that large usually follows a big early pricing mistake, and those customers need to be spoken to rather than only written to.
  applies_when: >-
    The raise is 50% or more and you can manage the call volume.
  anchor: >-
    Meet with people if you raise prices more than 50% . If you raise prices *a lot* - which
  source: >-
    playbook-price-raise.md, My Rules For Raising Prices, lines 243–245
  confirmations: 2
  anchor_at: "playbook-price-raise.md:243"
- id: B-playbooks-price-037
  type: rule
  name: >-
    Pair a price raise within 90 days of a launch
  statement: >-
    A price raise is timed inside the same quarter as a product launch or promotion and framed as early adopter pricing.
  why: >-
    It lets the raise draft off the momentum of the launch.
  applies_when: >-
    You have a new product or promotion launching.
  anchor: >-
    If you can, pair a price raise within 90 days of a launch . Every business has new prod-
  source: >-
    playbook-price-raise.md, My Rules For Raising Prices, lines 254–257
  confirmations: 1
  anchor_at: "playbook-price-raise.md:254"
- id: B-playbooks-price-038
  type: rule
  name: >-
    Do the math
  statement: >-
    Before raising prices you know what percentage of customers you can lose and still make money.
  why: >-
    With the break-even loss known, and with the price already tested on new customers, you will make more money eventually no matter what happens to the base.
  applies_when: >-
    Before any price raise is announced.
  anchor: >-
    You  should  know  what  percentage  of  customers  you  can  lose  and  still
  source: >-
    playbook-price-raise.md, My Rules For Raising Prices, lines 258–260
  confirmations: 2
  anchor_at: "playbook-price-raise.md:258"
- id: B-playbooks-price-039
  type: rule
  name: >-
    Test, test, test
  statement: >-
    A price change is decided on tested numbers, and a price that doubles while losing only about 20% of closes with everything else equal is taken.
  why: >-
    Pricing affects both conversion rate and churn, and both suffer as prices go up but not always proportionally; in the book's table $20 at a 4% conversion returns 60% more than $10 at 5%, while a 10x price returns less than the $20 price.
  applies_when: >-
    Choosing between tested price points; the next tests go between the winner and the price that failed.
  anchor: >-
    If you can double your price and close 20% fewer deals, with all else staying the same...
  source: >-
    playbook-price-raise.md, How To Pick Your Price, lines 316–324
  confirmations: 1
  anchor_at: "playbook-price-raise.md:319"
- id: B-playbooks-price-040
  type: rule
  name: >-
    Section #1 - R: Remind them of the value you provided them already
  statement: >-
    The price raise letter opens with a personalized, quantified list of the value the customer has already received — calls attended, deliverables used, revenue generated.
  why: >-
    It makes the letter about them rather than about you; the more you can personalize, the better.
  applies_when: >-
    Writing the price raise letter or email to existing customers.
  anchor: >-
    Start by reminding them of all the stuff you do - and the subsequent value they have
  source: >-
    playbook-price-raise.md, The Perfect Price Raise Letter, Section #1 - R, lines 339–350; template built with Patrick Campbell / Profitwell (lines 524–526)
  confirmations: 2
  anchor_at: "playbook-price-raise.md:340"
- id: B-playbooks-price-041
  type: rule
  name: >-
    Section #2 - A: Address the price change directly
  statement: >-
    The price change itself is stated directly, in a single sentence, with no delay or preamble.
  why: >-
    Rip off the bandaid: the rest of the letter is what softens the blow, so the announcement does not need to.
  applies_when: >-
    Writing the price raise letter or email to existing customers.
  anchor: >-
    Rip off the bandaid. Don’t waste time. The rest of the letter will soften the blow. It’s usu-
  source: >-
    playbook-price-raise.md, The Perfect Price Raise Letter, Section #2 - A, lines 351–360; template built with Patrick Campbell / Profitwell (lines 524–526)
  confirmations: 2
  anchor_at: "playbook-price-raise.md:352"
- id: B-playbooks-price-042
  type: rule
  name: >-
    Section #3 - I: Invest in their future
  statement: >-
    The investments named in the letter are things you were already going to do, each one tied to more good stuff or less bad stuff for the customer, and no new expense is added to justify the raise.
  why: >-
    Saying things you will not do is lying; adding expenses you had not planned negates the benefit of the price raise in the first place.
  applies_when: >-
    Writing the investment section of the price raise letter; three bullets is the checklist's count.
  anchor: >-
    Note: 1) Don’t say things you’re not going to do (that’s lying) 2) Frame all investments
  source: >-
    playbook-price-raise.md, The Perfect Price Raise Letter, Section #3 - I, lines 361–407
  confirmations: 2
  anchor_at: "playbook-price-raise.md:387"
- id: B-playbooks-price-043
  type: rule
  name: >-
    Section #4 - S: Soften the news with a loyalty reward
  statement: >-
    The price is raised now and existing customers immediately receive a loyalty discount or credit that expires in 3 to 6 months, shown on their invoices where possible.
  why: >-
    People are more okay with a vanishing discount than with a raise in price, and mind even less when another discount may appear later; it feels like being given credit rather than being charged more.
  applies_when: >-
    Announcing a raise to existing customers while new customers pay full price today.
  anchor: >-
    and then immediately offer a discount that expires 3 to 6 months from now. Bonus points: if
  source: >-
    playbook-price-raise.md, The Perfect Price Raise Letter, Section #4 - S, lines 408–424
  confirmations: 2
  anchor_at: "playbook-price-raise.md:411"
- id: B-playbooks-price-044
  type: rule
  name: >-
    Section #5 - E: Explain away their concerns
  statement: >-
    The letter ends with a PS inviting anyone the raise would materially affect to reply, and all replies go directly to the owner.
  why: >-
    The PS is why far fewer people reply negatively than you expect, and it gives you optionality with the customers actually affected — you can extend their discount another six months instead of losing them.
  applies_when: >-
    Any price raise letter; B2C wording is about buying groceries, B2B about their business.
  anchor: >-
    Add in a line that says basically “If this is gonna make you
  source: >-
    playbook-price-raise.md, The Perfect Price Raise Letter, Section #5 - E, lines 425–459
  confirmations: 2
  anchor_at: "playbook-price-raise.md:429"
- id: B-playbooks-price-045
  type: rule
  name: >-
    Stair step discount
  statement: >-
    A large price raise is delivered in one to three increments by dropping part of the discount every few months, rather than in a single jump.
  why: >-
    People have an easier time handling disappearing discounts than raised prices, and it eases customers into the new price.
  applies_when: >-
    The raise is large enough that you have reservations about going all the way up at once.
  anchor: >-
    2) You can do it in one to three increments. You position the discount as a stair step up.
  source: >-
    playbook-price-raise.md, What to Do Next, lines 494–502
  confirmations: 2
  anchor_at: "playbook-price-raise.md:499"
- id: B-playbooks-price-046
  type: rule
  name: >-
    Announce in the community with comments off
  statement: >-
    When the raise is announced to a community, comments on the post are turned off and all questions are referred to the owner directly.
  why: >-
    You do not want the complaints to compound in a public thread; the PS statement is what routes those conversations one on one.
  applies_when: >-
    You have a community or group where members congregate and the platform allows comments to be disabled.
  anchor: >-
    You don’t want a b*tch fest in the comments. This is why we refer them to talk
  source: >-
    playbook-price-raise.md, What to Do Next, lines 503–506
  confirmations: 2
  anchor_at: "playbook-price-raise.md:505"
- id: B-playbooks-price-047
  type: rule
  name: >-
    What To Do About Incoming Customers
  statement: >-
    New customers go onto the new price immediately, while existing customers get a separate date.
  why: >-
    New customers have no context on the old price, so there is no point delaying; and a sales team can answer the objection with the fact that existing customers agreed and that this is the cheapest the price will ever be.
  anchor: >-
    To be clear, get new customers up to the new price immediately. No point in delaying
  source: >-
    playbook-price-raise.md, What To Do About Incoming Customers, lines 507–519
  confirmations: 2
  anchor_at: "playbook-price-raise.md:508"
- id: B-playbooks-price-048
  type: rule
  name: >-
    Segment out ‘old’ customers
  statement: >-
    Customers who bought before the raise are segmented out of the base and handled as their own group.
  why: >-
    They are the only ones who need the letter, the loyalty discount and the personalized value list; new customers simply pay the new price.
  anchor: >-
    ☐Segment out ‘old’ customers that came before the price raise.
  source: >-
    playbook-price-raise.md, Price Raise Checklist, line 704
  confirmations: 1
  anchor_at: "playbook-price-raise.md:704"
- id: B-playbooks-price-049
  type: rule
  name: >-
    Sign in ink
  statement: >-
    The price raise letter is hand-signed in ink where it is physical mail, and personally signed where it is email.
  why: >-
    It is part of making the announcement personal rather than corporate, alongside replies going directly to the owner.
  anchor: >-
    ☐Sign in ink if possible . If not, sign the email personally.
  source: >-
    playbook-price-raise.md, Price Raise Checklist, line 715
  confirmations: 2
  anchor_at: "playbook-price-raise.md:715"
- id: B-playbooks-price-050
  type: rule
  name: >-
    Solve the customer’s next problem
  statement: >-
    A new thing to sell to existing customers solves their next problem and stays close to what they already bought, rather than reflecting the founder's own passion.
  why: >-
    If customers like your stuff, they want to buy more stuff like it; a product far from the core is a marketing, branding and sales nightmare. When the founders surveyed their customers, the vast majority chose the adjacent offer, and the upsell that won 2.2x'd LTV per customer.
  applies_when: >-
    Choosing a back end product, upsell or cross-sell for an existing customer base.
  anchor: >-
    I firmly opposed it because it didn’t solve our customers’ next problem. If customers like your
  source: >-
    playbook-lifetime-value.md, Increasing Lifetime Value: The Crazy 8, lines 78–109
  confirmations: 2
  anchor_at: "playbook-lifetime-value.md:81"
- id: B-playbooks-price-051
  type: rule
  name: >-
    My favorite upsell of all time
  statement: >-
    The default upsell is more of — or more help with — what the customer just bought, delivered with faster results, less risk, less effort and less hassle, for more money.
  why: >-
    It is the offer customers chose over an unrelated one when asked directly, because it is closest to what they already know and like.
  anchor: >-
    what they just bought... but with faster results, less risk, less
  source: >-
    playbook-lifetime-value.md, Increasing Lifetime Value: The Crazy 8, lines 115–117
  confirmations: 1
  anchor_at: "playbook-lifetime-value.md:116"
- id: B-playbooks-price-052
  type: rule
  name: >-
    Establish the LTGP baseline
  statement: >-
    Before any LTV lever is pulled, lifetime gross profit is computed: gross profit multiplied by average transactions for a transactional business, gross profit divided by churn for a recurring one.
  why: >-
    LTV is gross profit over the lifespan of a customer, not revenue, so every lever has to be measured against a baseline; the exercise also shows which products you spend a lot of time on without making the profit you thought.
  applies_when: >-
    Before working through the crazy eight on any business.
  anchor: >-
    Step Three: If you have a product or transactional business, multiply the average gross
  source: >-
    playbook-lifetime-value.md, How To Calculate LTV, lines 154–219
  confirmations: 1
  anchor_at: "playbook-lifetime-value.md:210"
- id: B-playbooks-price-053
  type: rule
  name: >-
    Churn is measured on the original cohort
  statement: >-
    Churn is the share of the customers you started the period with who left during it, and new signups in that period are excluded from the calculation.
  why: >-
    The same number of original people left whether you signed up zero or 1,000 new clients, so counting new signups hides the real churn.
  applies_when: >-
    Calculating churn for a recurring revenue business.
  anchor: >-
    it does not affect churn. The same number of original people left. You could
  source: >-
    playbook-lifetime-value.md, How To Calculate LTV, Step Two, lines 192–207
  confirmations: 1
  anchor_at: "playbook-lifetime-value.md:205"
- id: B-playbooks-price-054
  type: rule
  name: >-
    Test prices every quarter
  statement: >-
    Pricing is tested every quarter rather than set once.
  why: >-
    A Profitwell study found a tight relationship between how frequently a company tested pricing and its profitability, and companies that test more grow continually faster (2025).
  anchor: >-
    We  test  prices  every  quarter.  A  research  study  done  by  Profitwell  suggested  a
  source: >-
    playbook-lifetime-value.md, The Crazy Eight, #1 Increase Prices, lines 265–274
  confirmations: 2
  anchor_at: "playbook-lifetime-value.md:270"
- id: B-playbooks-price-055
  type: rule
  name: >-
    Break even conversion rate
  statement: >-
    Each price test is judged against a break-even conversion rate computed in advance, and prices keep being raised until conversion rate multiplied by LTGP drops.
  why: >-
    The price that gets the most people to buy with the highest gross profit is the price that maximizes profit, so the conversion rate alone cannot tell you whether the new price won.
  applies_when: >-
    Running a price test on a live offer.
  anchor: >-
    If it’s above your break even point, you have a winner.
  source: >-
    playbook-lifetime-value.md, #1 Increase Prices, Action Step, lines 275–279
  confirmations: 2
  anchor_at: "playbook-lifetime-value.md:278"
- id: B-playbooks-price-056
  type: rule
  name: >-
    Pro Tip: Start Low Then Go Up.
  statement: >-
    A new offer starts at a low price and the price is nudged up about 20% every 10 sales until sales drop dramatically, then moved back to the sweet spot.
  why: >-
    You need sales to confirm people actually want the thing and to run water through the pipes to find the leaks; testing price is expensive for a few months, but being under-monetized for life is more expensive.
  applies_when: >-
    A new or unproven offer.
  anchor: >-
    things are humming, you nudge up the price. I recommend nudging the price by
  source: >-
    playbook-lifetime-value.md, #1 Increase Prices, Pro Tip: Start Low Then Go Up., lines 280–290
  confirmations: 1
  authors_caveat: >-
    If you find you sold someone at too high a price, add bonuses or refund the difference.
  anchor_at: "playbook-lifetime-value.md:283"
- id: B-playbooks-price-057
  type: rule
  name: >-
    Buy in bulk & prepay
  statement: >-
    Where the cash is there, vendor spend is prepaid or bought in bulk to lock in 10-20% discounts.
  why: >-
    A locked-in discount is a guaranteed return on the money, and you would take a guaranteed 20% return anywhere else.
  applies_when: >-
    You have the cash and recurring vendor or inventory spend.
  anchor: >-
    ix) Buy in bulk & prepay . If you have the cash you can lock in 10-20% dis-
  source: >-
    playbook-lifetime-value.md, #2 Decrease Costs, lines 335–340
  confirmations: 1
  anchor_at: "playbook-lifetime-value.md:335"
- id: B-playbooks-price-058
  type: rule
  name: >-
    Pick the top two cost levers
  statement: >-
    Of the listed delivery-cost levers, the top two that can actually be implemented in your business are picked and written down.
  why: >-
    Costs can only fall to zero while prices can go infinitely high, but cutting delivery cost raises gross profit and makes the business more scalable.
  anchor: >-
    Action Step: Write down or circle the top two you think you could implement within
  source: >-
    playbook-lifetime-value.md, #2 Decrease Costs, lines 295–342
  confirmations: 1
  anchor_at: "playbook-lifetime-value.md:341"
- id: B-playbooks-price-059
  type: rule
  name: >-
    Pick at least one way to increase purchases
  statement: >-
    To increase the number of purchases you implement at least one of three things: add a recurring offer, decrease churn, or run regular follow-up offers.
  why: >-
    These are the only three ways the author knows to increase the number of purchases without pulling other crazy eight levers at the same time.
  applies_when: >-
    Working the #3 Increase # of Purchases lever, over the next quarter.
  anchor: >-
    decrease churn, and make regular follow up offers. You’re going to want to pick at least one.
  source: >-
    playbook-lifetime-value.md, #3 Increase # of Purchases, lines 347–398
  confirmations: 1
  anchor_at: "playbook-lifetime-value.md:351"
- id: B-playbooks-price-060
  type: rule
  name: >-
    Follow Up
  statement: >-
    Long term follow up to the list runs as a quarterly promotion, with value provided the rest of the time.
  why: >-
    It balances the give:ask ratio and keeps the business top of mind, so that when it is finally the right time for someone to buy, they buy from you.
  applies_when: >-
    Any list or audience of former customers and leads.
  anchor: >-
    follow up is to run a quarterly promotion. The remainder of the time, I simply
  source: >-
    playbook-lifetime-value.md, #3 Increase # of Purchases, lines 383–389
  confirmations: 1
  anchor_at: "playbook-lifetime-value.md:385"
- id: B-playbooks-price-061
  type: rule
  name: >-
    The cross-sell must fit the business you already run
  statement: >-
    A cross-sell is only added if it slots into existing infrastructure, resources and expertise and does not dramatically change who you serve or what you do every day.
  why: >-
    You do not want to break the business to pick up some extra change.
  anchor: >-
    that does not dramatically change who you serve or what you do every day.
  source: >-
    playbook-lifetime-value.md, #4 Cross-Sell Something Different, lines 403–418
  confirmations: 1
  anchor_at: "playbook-lifetime-value.md:415"
- id: B-playbooks-price-062
  type: rule
  name: >-
    Offer the upsell first, then downsell the standard offer
  statement: >-
    Quantity and quality upsells are offered first on the sales call, with the standard offer presented afterwards as the downsell.
  why: >-
    The author routinely sees 20%+ lifts in cash collected upfront and in LTV overall from making the bigger or better version the first thing presented.
  applies_when: >-
    Any sales call where a larger or premium version of the offer exists.
  anchor: >-
    and begin offering it first on your sales calls. Then, downsell your standard offer. You may see
  source: >-
    playbook-lifetime-value.md, #5 Sell More (Increase Quantity) and #6 Sell Better (Increase Quality), lines 436–486
  confirmations: 3
  anchor_at: "playbook-lifetime-value.md:437"
- id: B-playbooks-price-063
  type: rule
  name: >-
    Downsell only the unqualified
  statement: >-
    A downsell is offered only to prospects who do not qualify for the main offer; a qualified buyer is never sold a downsell.
  why: >-
    You lose money when people who would have bought the $5 thing take the $2.50 thing instead, so restricting downsells to unqualified prospects avoids cannibalizing the main offer while still collecting the extra cash.
  applies_when: >-
    Any quantity or quality downsell, offered by you or by a sales team.
  anchor: >-
    Downsell people who otherwise don’t qualify for your other offers. In other words, I forbid
  source: >-
    playbook-lifetime-value.md, #7 Downsell Fewer (Lower Quantity) and #8 Downsell Lower Quality, lines 504–556
  confirmations: 3
  anchor_at: "playbook-lifetime-value.md:507"
- id: B-playbooks-price-064
  type: rule
  name: >-
    Run the whole crazy eight and write the action steps
  statement: >-
    Every product or service is run through all eight LTV levers with the action step for each written down, rather than waiting for a good idea.
  why: >-
    The author's highest converting upsells have rarely come from moments of inspiration; they come from getting into the zone and following a process known to work.
  applies_when: >-
    Whenever LTV needs to be increased.
  anchor: >-
    I strongly recommend going through each of the crazy eight and writing down the action
  source: >-
    playbook-lifetime-value.md, Putting It All Together, lines 560–570
  confirmations: 2
  anchor_at: "playbook-lifetime-value.md:568"
```
