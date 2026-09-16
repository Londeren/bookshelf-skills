# Улов фазы 1 — $100M Playbooks: Pricing, Price Raise, Lifetime Value (2025) (ярус 2), тип C: разборы (кейсы)

Группа `tier2-playbooks-price`, слаг `playbooks-price`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **46** (экстрактор вернул 46, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `playbook-pricing.md` | 1–1381 | 2 | 25 |
| `playbook-price-raise.md` | 1–758 | 2 | 8 |
| `playbook-lifetime-value.md` | 1–613 | 1 | 13 |

## Как собран файл

Экстрактор C (Application cases) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-playbooks-price.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-playbooks-price-C.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: C-playbooks-price-001
  type: case
  name: >-
    The genie, Option #1: double the number of new customers
  statement: >-
    From a baseline of 30 new clients a month, 33% churn (3 months), $100/mo price, 100 total clients, 20%
    net margins, $10,000 revenue and $2,000 profit: doubling new customers to 60 a month halves CAC from
    $100 to $50, stabilises the base at 200 clients (60 divided by 33% churn), doubles revenue to $20,000 a
    month and, because $3,000 of CAC is saved, lifts net margins to 35% and profit to $7,000 — 3.5x profit.
    (The summary table of the section prints Profit/mo = $4,000 while the walkthrough says $7,000.)
  why: >-
    Doubling customers for the same advertising spend saves the money that would have been spent to double
    the business, and that saving drops straight to the bottom line.
  anchor: >-
    vi) And since we went from $2000 in profit to $7000 in profit, we 3.5x profit!
  source: >-
    playbook-pricing.md, Pricing To Make The Most Money, Option #1, lines 156-199
  confirmations: 1
  demonstrates: >-
    That the three growth levers are not equal on profit: halving the cost to acquire a customer is worth
    3.5x profit, not the 2x revenue it looks like.
  authors_caveat: >-
    The author states he included only the costs of advertising and delivering, to avoid complexity.
  anchor_at: "playbook-pricing.md:181"
- id: C-playbooks-price-002
  type: case
  name: >-
    The genie, Option #2: double the number of purchases
  statement: >-
    From the same baseline, doubling how many times customers buy cuts churn from 33% to 16.5% (three months
    to six), doubles lifetime revenue from $300 to $600 while lifetime delivery cost doubles from $150 to
    $300, grows the base to 200 clients (30 divided by 16.5%) and revenue to $20,000 a month; against
    $10,000 of delivery cost and $3,000 of monthly CAC that is $7,000 of profit at 35% net margins — 3.5x
    profit, the same result as doubling new customers.
  why: >-
    Doubling how long customers stay doubles what each is worth and saves the advertising that would
    otherwise be needed to double the business.
  anchor: >-
    $20,000 in revenue, $13,000 in costs, so we profit $7,000. 3.5x our original profit.
  source: >-
    playbook-pricing.md, Pricing To Make The Most Money, Option #2, lines 210-255
  confirmations: 1
  demonstrates: >-
    That retention and acquisition are equal levers on profit (3.5x each), and that both are beaten by
    price.
  anchor_at: "playbook-pricing.md:238"
- id: C-playbooks-price-003
  type: case
  name: >-
    The genie, Option #3: double your prices
  statement: >-
    From the same baseline, doubling the price with nothing else changed triples gross profit per customer
    ($150 to $450), takes gross margin from 50% to 75%, doubles revenue to $20,000 a month while costs stay
    at $8,000, and leaves $12,000 a month of profit at 60% net margins — 6x profit against 3.5x for either
    of the other two options, so the answer to the genie is to double the price.
  why: >-
    Neither the cost to acquire a customer nor the cost to deliver moves when the price moves, so the whole
    increase lands in profit.
  anchor: >-
    margins 60% ($12,000 / $20,000). Which 6x’d our profit!
  source: >-
    playbook-pricing.md, Pricing To Make The Most Money, Option #3, lines 261-303
  confirmations: 1
  demonstrates: >-
    That price is the strongest of the three levers on profit; also cited as the reason the whole playbook
    exists.
  anchor_at: "playbook-pricing.md:276"
- id: C-playbooks-price-004
  type: case
  name: >-
    Tripling the gym price from $99 to $299
  statement: >-
    The author tripled the price at his gym from $99 to $299 and lost 30% of the customers: 200 x $99 became
    140 x $299, so revenue more than doubled while the cost to deliver fell by about 30%.
  why: >-
    Raising prices increases revenue and decreases costs at the same time, which has a much larger effect on
    profit than either alone.
  anchor: >-
    from $99 to $299 and I lost 30% of my customers. So I went from 200 x 99 to 140 x $299.
  source: >-
    playbook-pricing.md, My Rules For Pricing, Rules of Pricing I Follow, line 409
  confirmations: 1
  demonstrates: >-
    The rule that raising prices makes money in two ways: more gross profit per customer and less cost to
    deliver because there are fewer customers.
  anchor_at: "playbook-pricing.md:409"
- id: C-playbooks-price-005
  type: case
  name: >-
    The Lookback Window of Value
  statement: >-
    A client who pays $5,000 a month and is made $60,000 in the first month judges that return inside the
    last billing cycle rather than the whole relationship; if the next month makes them $0 they cancel, even
    though the first month paid for the year. The author draws from this that longer billing cycles create
    less churn and attract more qualified customers, because they have to pay for longer periods up front.
  applies_when: >-
    Choosing the billing cycle for an ongoing service.
  anchor: >-
    If  someone  pays  you  $5000  per  month  for  services,  and  in  your  first  month
  source: >-
    playbook-pricing.md, My Rules For Pricing, Author Note: The Lookback Window of Value, lines 471-479
  confirmations: 1
  demonstrates: >-
    The rule to bill less frequently to have lower churn: the more often you bill, the more often people
    cancel.
  authors_caveat: >-
    The author marks it as unproven — to be clear, this is just his theory.
  anchor_at: "playbook-pricing.md:472"
- id: C-playbooks-price-006
  type: case
  name: >-
    The mall restaurant's 4% processing fee
  statement: >-
    A sit-down restaurant in a mall, owned by private equity, put a line at the very bottom of the menu
    saying all prices were subject to a 4% processing fee at check out from a stated date. On a
    statistically average single-location restaurant at $1,000,000 of revenue and 9% net margins, the fee
    adds $40,000 of revenue and takes profit from $90,000 to $130,000, a 44% increase, for the cost of
    printing new menus and one automated addition to the checkout process.
  why: >-
    The increase costs nothing to deliver, so the whole of it is profit; few things can raise profit 50%+
    overnight with no major change in operations.
  anchor: >-
    would take revenue from $1,000,000 to $1,040,000 but it would take profit from $90,000
  source: >-
    playbook-pricing.md, Just Raise It, A few years ago..., lines 506-526
  confirmations: 1
  demonstrates: >-
    That a small percentage added on top of the price drops straight to the bottom line; the menu-footnote
    way of disclosing fees.
  anchor_at: "playbook-pricing.md:522"
- id: C-playbooks-price-007
  type: case
  name: >-
    Small Percentages. Big Changes.
  statement: >-
    On the same $1,000,000 business at 9% margins, applying 26.8% of pricing optimisation — the low end of
    what the ten plays together provide (26.8% to 63.8%) — takes revenue to $1,268,000 and profit from
    $90,000 to about $358,000, roughly 4x. The general form the author gives is that a 10% price rise on a
    business running 10% margins doubles profit, and that the average US small business in 2024 runs 7-10%
    net margins (Investopedia).
  anchor: >-
    increase your revenue to $1,268,000...and...increase your profit from $90,000 to $358,000
  source: >-
    playbook-pricing.md, Just Raise It, Small Percentages . Big Changes ., lines 534-545
  confirmations: 1
  demonstrates: >-
    That the plays are chosen to affect sales minimally and compound; the arithmetic of why small pricing
    changes matter on thin margins.
  anchor_at: "playbook-pricing.md:544"
- id: C-playbooks-price-008
  type: case
  name: >-
    Pricing Play #1: monthly to 28 day billing cycles
  statement: >-
    Billing every 28 days gives 13 cycles a year instead of 12 at the same conversion rate: an instant and
    permanent 8.3% revenue increase, which on a 20% net margin business means 26.1% net margins and 41.5%
    more net profit. The author took it from a gym owner who programmed in four-week meso cycles and ran
    payroll every two weeks. Implementation: change contracts for new customers immediately, set a date for
    everyone else, be upfront and call it a price increase if needed, explain it as reinvestment.
  anchor: >-
    net margin business, implementing this would take you from 20% to 26.1% net margins
  source: >-
    playbook-pricing.md, Pricing Play #1: Monthly to 28 Day Billing Cycles, lines 578-613
  confirmations: 1
  demonstrates: >-
    The extra-billing-cycle play, and the rule to display the price in the smallest increment while billing
    on the longest.
  authors_caveat: >-
    Weekly and bi-weekly billing yield the same benefit in theory but caused billing hassles because people
    wanted short pauses, so the author sticks to 4 weeks, 12 weeks or longer and displays the price weekly.
  anchor_at: "playbook-pricing.md:589"
- id: C-playbooks-price-009
  type: case
  name: >-
    Pricing Play #2: the processing fee script and the second form of payment
  statement: >-
    After the customer has agreed the price you ask how they wanted to pay, then say it is just a 3.99% card
    processing fee. If they hesitate you offer the alternative: they can save the 3.99% by giving a second
    form of payment, because the fee exists to cover the resources spent chasing new card details when about
    7% of cards decline every month, and the saving is passed on to them. The author took the fee itself
    from an agency friend who said it added 33% to his profit.
  why: >-
    Either the fee sticks, which is 4% more revenue for no extra work, or you get the second card, which is
    worth far more than the fee.
  anchor: >-
    2) Then say, “Great, it’s just a 3.99% card processing fee.”
  source: >-
    playbook-pricing.md, Pricing Play #2: Processing Fees & Second Form of Payment, How It Works, lines
    628-640
  confirmations: 1
  demonstrates: >-
    Trading the fee for a backup card; the author notes he has never seen a sale lost over a processing fee.
  anchor_at: "playbook-pricing.md:631"
- id: C-playbooks-price-010
  type: case
  name: >-
    What a second card does to LTV
  statement: >-
    Recurring payments lose 1.2-1.7% a month to involuntary churn from card information changing, which on a
    business with 5% monthly churn is 24-34% of all churn. On a $100/mo service at 5% churn, LTV is $2,000;
    accepting the fee at $104/mo gives $2,080 (+4%), while a second card that saves 1.2 points of churn
    gives $2,631 (+31%) and one that saves 1.7 points gives $3,030 (+51%). At 10% churn the same three moves
    give +4%, +14% and +20%.
  anchor: >-
    Why does this matter? Recurring payments get 1.2%-1.7% monthly involuntary churn
  source: >-
    playbook-pricing.md, Pricing Play #2, How It Works / Examples, lines 645-665
  confirmations: 1
  demonstrates: >-
    Why the second form of payment is worth more than the processing fee it replaces; failed transactions
    are re-run the next day on the other card.
  anchor_at: "playbook-pricing.md:645"
- id: C-playbooks-price-011
  type: case
  name: >-
    The Canadian marketer's invoice
  statement: >-
    A Canadian marketer charging $25,000 a month invoiced $27,000, showing the arithmetic of his province's
    8% sales tax on the invoice, and when asked said he does not cover taxes — his price is what he gets.
    The author paid without argument and took note. The cost of the opposite habit: on 20% margins, paying a
    5% sales tax for customers gives away 25% of profit.
  anchor: >-
    there clear as day: $25,000 x 1.08 = $27,000. When I asked him about it he said, “I don’t
  source: >-
    playbook-pricing.md, Pricing Play #3: Sales Tax, How I Learned This, lines 685-692
  confirmations: 1
  demonstrates: >-
    Quote the price net of tax and put the tax as a separate line item before the total; sales tax comes off
    the top line, so absorbing it is a straight cut of profit.
  authors_caveat: >-
    If you are not charged the tax you cannot charge it; the author also suggests incorporating in a state
    that does not charge it, after checking with lawyers.
  anchor_at: "playbook-pricing.md:687"
- id: C-playbooks-price-012
  type: case
  name: >-
    Get in the angry boat with them
  statement: >-
    The four moves for adding sales tax: get agreement on the price first, then put the tax on the invoice
    or at point of sale with a dry, matter-of-fact citation of the state tax code, as if the customer
    already knew; put it as a separate line item before the total; and if they balk, get angrier about the
    tax than they are — you do not even keep it, you hand it straight to Uncle Sam and it only makes your
    life harder.
  anchor: >-
    “Think I like charging this tax? I don’t even get it! I hand it right over to Uncle Sam.
  source: >-
    playbook-pricing.md, Pricing Play #3: Sales Tax, Steps To Implement It, lines 714-724
  confirmations: 1
  demonstrates: >-
    Handling the objection to a fee you did not invent by taking the customer's side against it.
  anchor_at: "playbook-pricing.md:723"
- id: C-playbooks-price-013
  type: case
  name: >-
    Pricing Play #4: contracted annual price increases
  statement: >-
    A contract carrying a fixed 5% annual increase takes $100/mo to $105, $110, $116 and $122 over four
    years, 22% in absolute terms; at 12% a year the same $100 becomes $112, $125, $140 and $157. Against
    that, a service priced at $100 in 2017 and never changed has about 21% less spending power by 2024 ($100
    in 2024 was $79 in 2017), and a business on 20% margins in 2017 selling the same number of customers in
    2024 would have no profit seven years later. The scripting is that prices are kept standard with the CPI
    so there is no incentive to cut quality, mentioned while filling out paperwork rather than during the
    sale.
  why: >-
    Costs and inflation rise whether or not you act, so the choice is a proactive increase or an eroding
    margin.
  anchor: >-
    Yes, with your prices jumping 22% over that time period. And here’s a different chart
  source: >-
    playbook-pricing.md, Pricing Play #4: Annual Price Increases, How It Works & Examples, lines 754-810
  confirmations: 1
  demonstrates: >-
    Writing the right to raise rates annually into contracts; 5-15% is the range at which few people balk.
  anchor_at: "playbook-pricing.md:771"
- id: C-playbooks-price-014
  type: case
  name: >-
    Warren Buffett raised See's Candies prices over 50 times
  statement: >-
    Buffett let the managers of See's Candies run the business and control every decision except price,
    sending them the year's pricing for all candies himself; over the fifty-one years since the purchase he
    raised prices more than 50 times, sometimes as much as 17% in a single year, which the author values at
    over $1B of profit. The Price Raise playbook tells the same case as an average of about 10% a year.
  anchor: >-
    sends them the year’s pricing for all candies. He’s raised prices at See’s over 50
  source: >-
    playbook-pricing.md, Pricing Play #4, Fun Fact: Warren Buffett Raised See's Candies Prices 50 Times!,
    lines 792-800 (also playbook-price-raise.md, My Rules For Raising Prices, lines 227-233)
  confirmations: 2
  demonstrates: >-
    The rule to raise prices at least once per year: with a good product and a loyal customer base there is
    usually more room than you think.
  anchor_at: "playbook-pricing.md:794"
- id: C-playbooks-price-015
  type: case
  name: >-
    Pricing Play #5: billing cycle against churn (Profitwell data)
  statement: >-
    Data from Profitwell — Patrick Campbell's company, sold for $250M in 2022, with 14,000 active
    memberships on its analytics tool — gives, at a $100 price: annual billing 2% monthly churn and $5,000
    LTV; quarterly 5% and $2,000; monthly 10.7% and $935. That is 5.35x and 2.14x the LTV of monthly
    billing, so getting customers to pay annually can 5x LTV. It also drops conversions, because the price
    asked is 12x the monthly rate.
  anchor: >-
    You can 5x your LTV by simply getting customers to pay annually. So why doesn’t ev-
  source: >-
    playbook-pricing.md, Pricing Play #5: Annual Billing, How I Learned This / How It Works, lines 814-836
  confirmations: 1
  demonstrates: >-
    That churn is directly correlated with billing frequency — the less often you bill, the less churn you
    have, which matches the author's own move from weekly to 28-day billing.
  authors_caveat: >-
    Whether annual billing drops conversions by as much as 5x is untested — the author says he does not know
    and that you would have to test it yourself.
  anchor_at: "playbook-pricing.md:833"
- id: C-playbooks-price-016
  type: case
  name: >-
    The annual prepay ladder and the $370 first transaction
  statement: >-
    In the author's companies, with a 16% discount for annual (buy 10 months get 2 free), 10-15% choose
    annual on a sales page, 30% if it is the default option, and 35-40% over the phone depending on spending
    power. At 30% prepaying a year, $100 normally collected up front becomes an average first transaction of
    $370. The sale runs top down: offer the full $1,200 year first, then ask if they want a discount and
    offer 17% off for prepaying the year, then 8% off for prepaying the quarter ($275 instead of $300), then
    standard monthly at no discount.
  anchor: >-
    If you normally collect $100 upfront, but 30% of people pay $1000, then your average first
  source: >-
    playbook-pricing.md, Pricing Play #5: Annual Billing, lines 847-885
  confirmations: 1
  demonstrates: >-
    The Pro Tip to always start with the highest price: the first number out of your mouth anchors the
    conversation, so prepayment reads as a benefit rather than monthly reading as a penalty.
  authors_caveat: >-
    Selling only on this cadence is called a pretty advanced move; the author's advice is to offer the
    options alongside standard pricing, which risks nothing because you can revert.
  anchor_at: "playbook-pricing.md:852"
- id: C-playbooks-price-017
  type: case
  name: >-
    Pricing Play #6: Round Up
  statement: >-
    Running gyms with three weekly tiers, the author moved $47 to $49, $37 to $39 and $27 to $29 — an extra
    $104 per client a year, 4.25% to 7.4% depending on the tier, with no change in closing rate. Pushing
    further to $49.99, $39.99 and $29.99 added $155.48 a year per client, 6.36% to 11.1%, again with no
    change in conversion. Against the average gym's 12.5% net margins that is close to double the profit,
    and it came from changing 7s to 9s and adding .99.
  anchor: >-
    That tiny change added an extra $104 per client, annually. We’re talking 4.25% to 7.4%
  source: >-
    playbook-pricing.md, Pricing Play #6: Round Up, How It Works & Examples, lines 911-945
  confirmations: 1
  demonstrates: >-
    That there is more room in the last digits of a price than owners assume, at zero operational cost.
  authors_caveat: >-
    Luxury items typically end on a round number because their buyers do not want a deal; premium is not
    luxury, so .99 endings still work there. The author says to test it, since shorter numbers sometimes do
    better.
  anchor_at: "playbook-pricing.md:927"
- id: C-playbooks-price-018
  type: case
  name: >-
    Pricing Play #7: the tanning chain's annual renewal fee
  statement: >-
    A 22-location tanning salon chain signed members to annual contracts carrying three things: a start-up
    fee, a monthly rate and an annual renewal fee. At $39 a month plus a $99 fee once a year, $468 of annual
    revenue per customer became $567 — an effective $47 a month, a 20% increase — while the chain still
    advertised $39 a month. Members heard $468 a year and ran, but $39 a month sounded affordable.
  applies_when: >-
    Markets too price-conscious to bill annually, where the author says this play shines.
  anchor: >-
    This allowed them to advertise $39 per month then still have a $99 annual fee on top
  source: >-
    playbook-pricing.md, Pricing Play #7: Annual Renewal Fee On Top of Monthly, How I Learned This, lines
    970-989
  confirmations: 1
  demonstrates: >-
    That people focus on the monthly price and rarely consider the annualised cost, so the advertised price
    and the collected price need not be the same.
  anchor_at: "playbook-pricing.md:981"
- id: C-playbooks-price-019
  type: case
  name: >-
    The renewal fee's reason why
  statement: >-
    Pick a renewal fee of 1-3x the monthly rate — 0.5x monthly adds 4.15% of revenue, 1x adds 8.3%, 2x adds
    16.6%, 3x adds 24.9% — then attach a beneficial reason why: the fee buys rate protection against future
    price changes, or it lets the customer go month to month after the year without paying a cancellation
    fee. Add both the rate and the fee to the contract and have the customer initial next to each, calling
    it rate protection or cancellation fee prepayment; if they balk, drop it and they lose the benefit.
  anchor: >-
    Here’s the easiest one I know: “You pay this for rate protection. If you don’t agree to the fee,
  source: >-
    playbook-pricing.md, Pricing Play #7, Steps To Implement It & Examples, lines 1013-1029
  confirmations: 1
  demonstrates: >-
    Attaching a reason why to a fee so that the fee protects the sale instead of risking it; pairing a setup
    fee with a renewal fee so one can be waived to win the other.
  anchor_at: "playbook-pricing.md:1022"
- id: C-playbooks-price-020
  type: case
  name: >-
    Pricing Play #8: Continued Access automatic continuity
  statement: >-
    An education seller doing $5,000,000 a year stopped selling lifetime access and sold one year of access
    that rolls automatically into $99 a month, agreed up front; it made him $750,000 in a year off one line
    in the contract and did not affect sales, because everyone knows they have a year to cancel. The author
    copied it for $150,000 a month of near-passive profit. The math: a $2,000/mo, 4-month, 70%-margin
    service has $5,600 LTV; bolting on a $200/mo continuity (10% of the rate) at 90% margins that 50% of
    buyers keep for 20 months adds $1,800, taking LTV to $7,400, a 32% increase.
  anchor: >-
    into a much smaller monthly payment of $99 per month. They agree to it upfront. And the
  source: >-
    playbook-pricing.md, Pricing Play #8: Automatic Continuity, lines 1043-1087
  confirmations: 1
  demonstrates: >-
    Selling a stripped-down, high-margin version at 5-20% of the main price and tacking it onto the back of
    every front-end purchase, so that the customer keeps rather than loses what they already paid for.
  authors_caveat: >-
    This is not undisclosed or forced continuity: the customer must agree to it up front and be told clearly
    what happens after the period.
  anchor_at: "playbook-pricing.md:1048"
- id: C-playbooks-price-021
  type: case
  name: >-
    Pricing Play #9: the tailor's $16,000 suit
  statement: >-
    A tailor fitted the author, who had told himself he would spend no more than $500, into a $16,000 suit
    first; he almost gasped at the price, and the tailor immediately brought out a $2,000 suit, at which the
    author felt relief. The play is to add something 10x or more expensive than the core offer to the menu
    and to offer that first — get the gasp, then find something better suited to them.
  anchor: >-
    I learned this from a tailor. I was getting fitted for a suit. The first one he had me try on
  source: >-
    playbook-pricing.md, Pricing Play #9: Ultra High Ticket Anchor, How I Learned This, lines 1135-1145
  confirmations: 1
  demonstrates: >-
    The price anchor: the first price shown sets what every later price feels like.
  authors_caveat: >-
    Only offer what you would be excited to deliver if it sold; if you feel stressed when people buy it,
    keep raising the price until it makes you smile.
  anchor_at: "playbook-pricing.md:1135"
- id: C-playbooks-price-022
  type: case
  name: >-
    What an ultra high ticket option does to LTV
  statement: >-
    A business selling a $500 main product to 80% of buyers and a $200 downsell to 20% has an LTV of $440.
    Adding a $5,000 option that only 10% take gives $500 plus $350 plus $40 — an LTV of $890. On top of that
    the anchor closes more of the $500 sales, because the expensive option makes the core offer look
    affordable.
  anchor: >-
    Your LTV per customer jumps from $440 to $890. That’s massive! All by simply having
  source: >-
    playbook-pricing.md, Pricing Play #9, Examples, lines 1146-1172
  confirmations: 1
  demonstrates: >-
    That a high anchor pays twice: on the few who buy it and on the many who now find the core offer cheap.
  anchor_at: "playbook-pricing.md:1167"
- id: C-playbooks-price-023
  type: case
  name: >-
    Pricing Play #10: selling the warranty you already give away
  statement: >-
    A portfolio company selling high-end physical products already shipped a ten-year warranty as standard;
    asked whether it could be sold for 10% of the product price, the founder saw no reason why not, and a
    huge share of buyers opted in. The math on a $1,000 product with a $100 guarantee and a $100 cost to
    replace: twenty warranties sold against one claim is $1,900 of pure guarantee profit, and the profit on
    the honoured unit falls from $900 to $800. Price the guarantee at 5-30% of the price, or at your cost of
    goods so you can never lose money, and replace rather than refund.
  why: >-
    People hate risk and will pay you to take it; replacing instead of refunding keeps the revenue and costs
    only the price of delivering again.
  anchor: >-
    You add (20 warranties x $100 price) - $100 Cost to fix one = $1900 pure ‘guarantee’ profit.
  source: >-
    playbook-pricing.md, Pricing Play #10: Guarantee and Warranty Upsells, How It Works, lines 1197-1227
  confirmations: 1
  demonstrates: >-
    That you are buying and selling risk, so the play comes down to knowing your claim rate; the author's
    own products business had almost no warranty claims, making the extra 10% pure profit with zero new
    operations.
  anchor_at: "playbook-pricing.md:1221"
- id: C-playbooks-price-024
  type: case
  name: >-
    The one-line warranty upsell at checkout
  statement: >-
    After the purchase you ask whether they just want the standard warranty on that. When they ask what it
    is, you say it is for anyone who likes that extra bit of peace of mind, that they are covered if
    anything happens or it does not go as planned, and that a lot of people take it. Then you ring it up as
    an extra invisible product, and at claim time you check whether they bought it — which also lets you
    refund the ones who did not, as you probably do for free already.
  anchor: >-
    You  just  ask  after  they’ve  purchased  “You  just  want  the  standard  warranty  on  that?”
  source: >-
    playbook-pricing.md, Pricing Play #10, Steps To Implement It, lines 1275-1284
  confirmations: 1
  demonstrates: >-
    That the guarantee upsell is one line in the sales script with no operational change behind it; it works
    especially well in main street and traditional businesses.
  anchor_at: "playbook-pricing.md:1276"
- id: C-playbooks-price-025
  type: case
  name: >-
    The warranty upsell covering sales commissions
  statement: >-
    The warranty was rolled out hoping to recoup as much of the sales commissions as possible, and a huge
    share of customers took it — enough to cover almost half the sales team's commissions. The arithmetic:
    if half the customers take an upsell priced at 10% of the product, you get 5% of revenue back, which for
    a company paying reps 10% is half their pay.
  anchor: >-
    if half the customers take an upsell that’s 10% of the price, then you get 5% of
  source: >-
    playbook-pricing.md, Pricing Play #10, Pro Tip: Cover Your Commissions, lines 1234-1240
  confirmations: 1
  demonstrates: >-
    Pricing a guarantee against a known cost line rather than arbitrarily; the same concept works at any
    price point, as shipping insurance shows.
  anchor_at: "playbook-pricing.md:1238"
- id: C-playbooks-price-026
  type: case
  name: >-
    Trey's gym: tripling $49 memberships in a week
  statement: >-
    Trey priced group fitness and personal training at $49 a month believing cheap customers would be the
    most grateful, and ended up with the worst customers he had ever had, losses despite more customers,
    savings gone and no money for paid ads. The fix: a letter, used as the script for an explainer video
    posted in the gym community with comments turned off and all questions referred to him directly,
    announcing that prices were tripling for every member. He lost members, but not close to all of them,
    and the gym went from bleeding $2,000 a month to pocketing $4,000 of profit, rolled out in a week.
  anchor: >-
    The result? Trey’s business went from bleeding $2,000 a month to pocketing $4,000 in
  source: >-
    playbook-price-raise.md, Raise Prices, lines 64-107
  confirmations: 1
  demonstrates: >-
    The price raise letter delivered as a video to a community; the option of going all the way up at once
    when the business is not profitable; the rule not to wait until the universe forces your hand.
  anchor_at: "playbook-price-raise.md:106"
- id: C-playbooks-price-027
  type: case
  name: >-
    $30 to $3,000 across 300 customers
  statement: >-
    A Shopify competitor charged $30 a month while hundreds of its customers made over $1,000,000 a year on
    the software; the more sales those customers made, the more they cost to fulfil, so the biggest
    customers lost the company the most money. The choice was to fire them or reprice them: the CEO phoned
    all 300, took prices to $3,000 on average, and lost one.
  anchor: >-
    300 of them - and they took their prices from $30 to $3000 on average (a 100x increase!).
  source: >-
    playbook-price-raise.md, My Rules For Raising Prices, Fear not ., lines 246-253
  confirmations: 1
  demonstrates: >-
    The rule Fear not, and the rule to meet with people when the raise is more than 50%; if people see the
    value, they will stay.
  anchor_at: "playbook-price-raise.md:252"
- id: C-playbooks-price-028
  type: case
  name: >-
    The price test table: $10, $20 and $100
  statement: >-
    At $10, 100 clicks convert at 5% to 5 sales with 10% churn and $100 LTV — $500 in total return. Doubling
    to $20 drops conversion by 20% to 4 sales, leaves churn unchanged and doubles LTV to $200 — $800, 60%
    more from the same 100 clicks, which triples profit for a business on 30% margins. Taking the price to
    $100 drops conversion 60% to 2 sales and triples churn to 33%, giving $300 LTV and $600 — still better
    than $10, worse than $20. So the best price of those tested is $20, and the next tests are $39-$59.
  why: >-
    You lose some conversions, but often not as much as you gain in lifetime value.
  applies_when: >-
    Picking a price from data rather than from what competitors charge.
  anchor: >-
    When we double the price to $20 (a 100% increase), our conversion rate drops 20%
  source: >-
    playbook-price-raise.md, How To Pick Your Price, lines 263-321 (the same table appears in playbook-
    pricing.md, Three Metrics To Determine value-Driven Pricing, lines 387-390)
  confirmations: 1
  demonstrates: >-
    That price moves both conversion rate and churn, but not proportionally; the perfect price is the one
    that makes the most money, not the one that gets the most customers.
  anchor_at: "playbook-price-raise.md:285"
- id: C-playbooks-price-029
  type: case
  name: >-
    The gym price increase letter Trey sent
  statement: >-
    The long version, close to word for word what Trey sent: the anniversary and thanks for the patronage;
    WHAT WE CURRENTLY DO (hire and retain coaches, continued education for them, new and replaced
    equipment); WHAT IS COMING (facility improvements, member events, specialty programs, and a massive
    service upgrade from come whenever you can to a standing appointment with a trainer 3x per week in
    smaller classes); then the billing change — unlimited monthly becomes weekly billing, about $10-$15 a
    week more, landing at $39 a week from a stated effective date, broken down weekly on an attached chart;
    then a refer-a-friend program giving a free month per signup to offset the increase; then a demand that
    every question be asked in person rather than in the Facebook group; hand-signed, with a PS.
  anchor: >-
    come whenever you want,» we will be switching to weekly billing. This switch will be an in-
  source: >-
    playbook-price-raise.md, My Gym Price Increase Letter, lines 523-636
  confirmations: 1
  demonstrates: >-
    The RAISE elements in a real artifact: value first, the increase second, an offset, and a single channel
    for objections.
  authors_caveat: >-
    The author prefers the shorter template he built with Patrick Campbell of Profitwell, saying his own
    letter covers the same basic tenets but takes longer to get to the point; this one still worked for
    hundreds of gyms.
  anchor_at: "playbook-price-raise.md:602"
- id: C-playbooks-price-030
  type: case
  name: >-
    Soften the price raise with a vanishing loyalty discount
  statement: >-
    The S of RAISE in its concrete wording: new customers pay the new price from today, but the loyal
    customer is kept on the existing plan for three to six months and given a credit as a thank-you, after
    which they are bumped to the new price — shown as a credit on their invoices where possible, so it reads
    as a gift rather than a raise. In the assembled template this sits between the value recap, the one-
    sentence announcement that prices must rise, the list of investments, and a PS inviting anyone
    materially affected to write back (groceries for B2C, the business for B2B). The concise template was
    built with Patrick Campbell of Profitwell.
  why: >-
    People are more okay with a vanishing discount than with a raise in price, and mind even less when
    another discount appears in the future.
  anchor: >-
    “You’ve been insanely loyal to us the past X months/years. As of today we’re raising prices on
  source: >-
    playbook-price-raise.md, The Perfect Price Raise Letter, Section #4 - S: Soften the news with a loyalty
    reward, line 419
  confirmations: 1
  demonstrates: >-
    That a price raise is easier to deliver as a discount that will vanish than as a price that has risen.
  anchor_at: "playbook-price-raise.md:419"
- id: C-playbooks-price-031
  type: case
  name: >-
    The three types of reply to a price raise
  statement: >-
    After the letter, three kinds of customer appear. Those who see the value comply without liking it.
    Those actually affected write sob stories, which gives you optionality: the reply is to extend their
    discount another six months and reach out again then. Those who were going to cancel anyway leave now —
    churn rises in the first month, falls below normal in the second and returns to baseline in the third,
    which means the churn was pulled forward rather than created, costing one month of revenue from that
    slice.
  anchor: >-
    don’t we extend your discount another 6 months, then reach out then. Is that fair?”
  source: >-
    playbook-price-raise.md, Section #5 - E: Explain away their concerns, lines 438-459
  confirmations: 1
  demonstrates: >-
    The E of RAISE: the PS invites the objections, and you must be ready to answer customers one by one
    rather than reach for what is scalable.
  anchor_at: "playbook-price-raise.md:443"
- id: C-playbooks-price-032
  type: case
  name: >-
    What the sales team says to new customers about the higher price
  statement: >-
    Incoming customers go to the new price immediately, with no delay, because they have no context. If one
    has heard a cheaper number from a friend, the rebuttal is that it feels like bad news but is good news:
    the value keeps improving, 96% of existing customers agreed to the new price and they are the ones
    already using it, and this is the cheapest it will ever be, so there will never be a better time to
    start.
  anchor: >-
    confidence, 96% of our customers agreed. And they should know - they’re already using it.
  source: >-
    playbook-price-raise.md, What To Do About Incoming Customers, lines 507-519
  confirmations: 1
  demonstrates: >-
    That existing customers are not grandfathered and new ones are never sold at the old price; people moan
    and still buy.
  anchor_at: "playbook-price-raise.md:516"
- id: C-playbooks-price-033
  type: case
  name: >-
    The stair-step discount for a large raise
  statement: >-
    Where the raise is too big to take in one go, it is delivered in one to three increments by positioning
    the discount as a stair step that falls off in stages — $200 a month off for the first four months, then
    $100 a month off, then $50 a month off for the last three — at six-month intervals in the checklist
    version. The alternative, which worked for Trey, is to go all the way up at once when you are not
    profitable and need the move.
  anchor: >-
    off for the first 4 months, then $100/mo off, then $50/mo off last three months.” This
  source: >-
    playbook-price-raise.md, What to Do Next, lines 494-502 (repeated in the Price Raise Checklist, lines
    720-722)
  confirmations: 1
  demonstrates: >-
    That people have an easier time handling disappearing discounts than raised prices; fewer bigger jumps
    can be replaced by more smaller ones.
  anchor_at: "playbook-price-raise.md:501"
- id: C-playbooks-price-034
  type: case
  name: >-
    Letting the customers pick the back end product
  statement: >-
    A company acquired in 2020 had a front-end product that got customers but nothing else to sell, no
    recurring revenue and one marketing channel. The founders wanted a back end they were passionate about
    but which had nothing to do with the current business; the author wanted more of — or more help with —
    what customers had just bought. Deadlocked, they put both offers to the customers in a survey; the vast
    majority chose the adjacent offer. The upsell they built 2.2x'd LTV per customer, which allowed 5x the
    advertising across all channels profitably and took revenue from a few million a month to a few million
    a week.
  why: >-
    If customers like your stuff, they want to buy more stuff like it; the business serves the customer, not
    the other way around.
  anchor: >-
    deal. In a last ditch effort I said, “Why don’t we just ask the customers? Offer both and see
  source: >-
    playbook-lifetime-value.md, Increasing Lifetime Value: The Crazy 8, lines 59-117
  confirmations: 1
  demonstrates: >-
    The author's favourite upsell — more of, or more help with, what they just bought, with faster results,
    less risk, less effort and less hassle, for more money; and LTV as the fuel that lets you outbid
    competitors for attention.
  anchor_at: "playbook-lifetime-value.md:86"
- id: C-playbooks-price-035
  type: case
  name: >-
    Working out gross profit: the widget and the account rep
  statement: >-
    A widget sold at $100 that costs $20 to manufacture and ship leaves $80 of gross profit. A service where
    one account representative handles ten clients paying $3,000 a month bills $30,000 a month per rep
    against a $6,000 rep cost: $24,000 of gross profit, 80%, so $3,000 x 80% = $2,400 of gross profit per
    customer. Do this for every product and for the business overall, because some products you spend a lot
    of time on make less than you thought.
  anchor: >-
    Product Example: I sell a widget for $100. It costs me $20 to manufacture and ship the
  source: >-
    playbook-lifetime-value.md, How To Calculate LTV, Step One: Gross Profit, lines 156-180
  confirmations: 1
  demonstrates: >-
    Step One of the LTV calculation, and the distinction between gross profit and net profit.
  anchor_at: "playbook-lifetime-value.md:160"
- id: C-playbooks-price-036
  type: case
  name: >-
    Turning gross profit into LTGP
  statement: >-
    For a product or transactional business, multiply average gross profit by transactions per customer: the
    source prints $80 x 4 = $360 LTGP. For a recurring business, divide gross profit by churn: $2,400 / 5% =
    $48,000. The transaction count is always an estimate, because customers come, leave and come back, and
    lifetime transactions rise as a business gets older.
  anchor: >-
    Step Three: If you have a product or transactional business, multiply the average gross
  source: >-
    playbook-lifetime-value.md, How To Calculate LTV, Step Three, lines 210-220
  confirmations: 1
  demonstrates: >-
    Step Three of the LTV calculation, and the two different formulas for transactional and recurring
    businesses.
  anchor_at: "playbook-lifetime-value.md:210"
- id: C-playbooks-price-037
  type: case
  name: >-
    Calculating churn from one month to the next
  statement: >-
    A hundred customers on the first of last month, of whom five are gone this month, is five percent churn:
    people who left divided by the original amount. Customers signed up during the period do not enter it —
    you could sign zero or 1,000 new clients that month and churn would still be five percent, because the
    same five of the original hundred left.
  anchor: >-
    month, of those 100 customers, we lost five, our churn is five percent.
  source: >-
    playbook-lifetime-value.md, How To Calculate LTV, Step Two, lines 192-207
  confirmations: 1
  demonstrates: >-
    Step Two of the LTV calculation for a recurring business, and the common mistake of letting new signups
    mask churn.
  anchor_at: "playbook-lifetime-value.md:195"
- id: C-playbooks-price-038
  type: case
  name: >-
    A 20% price rise on a 10% profit business
  statement: >-
    Raising prices by 20% on a business running 10% profit, with sales unchanged, does not grow the business
    by 20% — it triples it, because the extra drops straight to the bottom line. Pricing affects gross
    profit more than any of the other seven levers, which is why it is first of the Crazy Eight, and the
    sweet spot is found by taking sales conversion rate times lifetime gross profit: the price that gets the
    most people to buy at the highest gross profit.
  anchor: >-
    ness. If you take a 10% profit business, raise the prices by 20%, and keep sales the same...
  source: >-
    playbook-lifetime-value.md, The Crazy Eight, #1 Increase Prices, lines 254-269
  confirmations: 1
  demonstrates: >-
    Crazy Eight #1 Increase Prices, and the rule that the goal is not to sell the most stuff but to make the
    most money.
  anchor_at: "playbook-lifetime-value.md:257"
- id: C-playbooks-price-039
  type: case
  name: >-
    Doubling the price of a company after buying it
  statement: >-
    Having bought a company and reviewed everything in it, the author simply doubled the price, did nothing
    else, and tripled the business. He tests prices every quarter, following Profitwell's finding of a tight
    relationship between a company's profitability and how frequently it tested pricing.
  anchor: >-
    thing, simply doubled the price. That’s it. And by doing so, tripled the business.
  source: >-
    playbook-lifetime-value.md, #1 Increase Prices, lines 270-274
  confirmations: 1
  demonstrates: >-
    That price should be tested continually and is usually higher than you think; the action step is to set
    a price, work out the break-even conversion rate and track the new one against it.
  authors_caveat: >-
    The author's Pro Tip is to start low and nudge up 20% every ten sales or so until sales drop
    dramatically, then go back to the sweet spot; testing price is expensive for a few months, but not
    testing it leaves a business under-monetised for life.
  anchor_at: "playbook-lifetime-value.md:273"
- id: C-playbooks-price-040
  type: case
  name: >-
    What a cross-sell adds to LTV
  statement: >-
    Add the upsell's conversion rate times its gross profit to the existing LTV: a $100 LTV plus 20% of
    buyers taking a $100 upsell that is all profit gives $120. The three worked examples are lawn care
    cross-selling snow blowing in the winter, burgers cross-selling fries and a soda, and a course cross-
    selling a community on top.
  anchor: >-
    Ex: So if your LTV was $100 to start and you get 20% of people to buy a $100 upsell
  source: >-
    playbook-lifetime-value.md, #4 Cross-Sell Something Different, lines 403-418
  confirmations: 1
  demonstrates: >-
    Crazy Eight #4 Cross-Sell; the cross-sell must not dramatically change who you serve or what you do
    every day, and should fit existing infrastructure, resources and expertise.
  anchor_at: "playbook-lifetime-value.md:408"
- id: C-playbooks-price-041
  type: case
  name: >-
    Adding recurring across three business types
  statement: >-
    Plumbing services upsell a plumbing membership covering all the customer's plumbing needs, which 20%
    take; a mug seller creates a funny mug of the month membership, which 10% take and keep for five months;
    a course adds accountability calls as an ongoing service paid monthly. Even at very high churn, taking
    someone from buying once to buying three times triples how many times they buy.
  anchor: >-
    ii) Physical Products: You sell mugs. You create a funny mug of the month
  source: >-
    playbook-lifetime-value.md, #3 Increase # of Purchases, tactic (a) Add recurring, lines 352-363
  confirmations: 1
  demonstrates: >-
    Crazy Eight #3 Increase # of Purchases: adding recurring is one of only three ways the author knows to
    raise the number of purchases.
  anchor_at: "playbook-lifetime-value.md:360"
- id: C-playbooks-price-042
  type: case
  name: >-
    Decreasing churn across three business types
  statement: >-
    A lawn care company holds a local customer appreciation event invited by handwritten letter and people
    cancel less often because they like the company more; a meat membership lets customers change quantity
    and delivery frequency by text, which keeps them longer; a course adds a community feature that keeps
    people engaged longer. Halving churn from 10% to 5% a month doubles LTV, since lifetime revenue is price
    divided by churn.
  anchor: >-
    ii) Physical Products: You sell a meat membership. You allow customers to
  source: >-
    playbook-lifetime-value.md, #3 Increase # of Purchases, tactic (b) Decrease churn, lines 364-382
  confirmations: 1
  demonstrates: >-
    Crazy Eight #3: once revenue recurs, the lever is churn, which the author says the Churn Checklist
    Playbook covers in depth.
  anchor_at: "playbook-lifetime-value.md:378"
- id: C-playbooks-price-043
  type: case
  name: >-
    Quarterly follow-up across three business types
  statement: >-
    Lawn care runs a quarterly best lawn competition to reactivate old customers; a supplement seller runs a
    quarterly weight loss challenge; a course runs a quarterly promotion for a cohort that gets more
    attention, or adds one new module and promotes the improved version as a launch. Between promotions the
    author only gives value to the list of former customers and leads, which balances the give:ask ratio and
    keeps the business top of mind for whenever they are ready to move.
  anchor: >-
    ii) Physical Products: You sell supplements. You run a quarterly weight loss
  source: >-
    playbook-lifetime-value.md, #3 Increase # of Purchases, tactic (c) Follow Up, lines 383-396
  confirmations: 1
  demonstrates: >-
    Crazy Eight #3: reactivation campaigns and long-term follow-up as the third way to raise purchase count.
  anchor_at: "playbook-lifetime-value.md:392"
- id: C-playbooks-price-044
  type: case
  name: >-
    The three quantity upsells on a pest control account
  statement: >-
    On pest control serviced once a month: bulk is getting the client to prepay a year (12x); more often is
    moving service from monthly to every three weeks (1.33x); bigger is going from one hour per visit to
    three (3x). For physical products the same three are two burgers instead of one and a bigger burger,
    with more often not applying. Offer the quantity upsell first on the sales call and then downsell the
    standard offer, which the author says can lift cash collected 20%+ overnight.
  anchor: >-
    iii) Bigger: You go from working 1 hour each time to 3 hours each time. (3x)
  source: >-
    playbook-lifetime-value.md, #5 Sell More (Increase Quantity), lines 423-438
  confirmations: 1
  demonstrates: >-
    Crazy Eight #5 Sell More: the three forms of a quantity upsell — bulk, more often, bigger.
  anchor_at: "playbook-lifetime-value.md:434"
- id: C-playbooks-price-045
  type: case
  name: >-
    Why a downsell makes money per visitor
  statement: >-
    Comparing what four people through the door, on the phone or at the checkout page are worth before and
    after a downsell, the business makes 50% more per person even though the extra sales happen at a lower
    price. You lose money only when someone who would have bought the $5 thing takes the $2.50 thing
    instead, so the author forbids his sales team from selling a downsell to a qualified person: the main
    offer is not cannibalised and the extra cash is still collected.
  applies_when: >-
    Only for prospects who do not qualify for the main offer.
  anchor: >-
    So, if we make 50% more per person who walks in the door, we make more money, even
  source: >-
    playbook-lifetime-value.md, #7 Downsell Fewer (Lower Quantity), lines 491-510
  confirmations: 1
  demonstrates: >-
    Crazy Eight #7 Downsell Fewer: a downsell raises LTV because the right price is picked with the
    conversion rate in view, and because this beats nothing.
  anchor_at: "playbook-lifetime-value.md:504"
- id: C-playbooks-price-046
  type: case
  name: >-
    The three quantity downsells on a home service account
  statement: >-
    On a home service delivered once a month: quantity is getting the client to buy three months upfront
    instead of twelve; less often is one visit every other month rather than nothing at all; smaller is
    thirty minutes per visit instead of an hour (0.5x). For physical products the same three are one burger
    instead of two and a smaller burger. These carry little operational drag, because you already do or make
    the thing.
  anchor: >-
    i) Quantity: You get the client to buy three months upfront instead of twelve.
  source: >-
    playbook-lifetime-value.md, #7 Downsell Fewer (Lower Quantity), lines 511-521
  confirmations: 1
  demonstrates: >-
    Crazy Eight #7 as the mirror image of the quantity upsell, offered only to prospects who do not qualify
    for the main offer.
  anchor_at: "playbook-lifetime-value.md:512"
```
