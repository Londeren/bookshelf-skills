# Улов фазы 1 — $100M Playbooks: Pricing, Price Raise, Lifetime Value (2025) (ярус 2), тип E: глоссарий

Группа `tier2-playbooks-price`, слаг `playbooks-price`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **34** (экстрактор вернул 34, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `playbook-pricing.md` | 1–1381 | 2 | 16 |
| `playbook-price-raise.md` | 1–758 | 2 | 6 |
| `playbook-lifetime-value.md` | 1–613 | 1 | 12 |

## Как собран файл

Экстрактор E (Glossary) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-playbooks-price.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-playbooks-price-E.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: E-playbooks-price-001
  type: term
  name: >-
    Cost Plus Pricing
  definition: >-
    Cost Plus Pricing: whatever your costs are plus an arbitrarily added margin.
  statement: >-
    Cost plus pricing is the model that sets the price at your own costs plus a margin chosen arbitrarily.
  why: >-
    Your customers have no idea what it costs you, so your costs don't matter to them; costs change, you don't always know all the costs ahead of time, and every person who would pay more because they need it more you don't net on.
  anchor: >-
    Cost Plus Pricing: whatever your costs are plus an arbitrarily added margin
  source: >-
    playbook-pricing.md, Three Models Of Pricing, line 342
  confirmations: 1
  anchor_at: "playbook-pricing.md:342"
- id: E-playbooks-price-002
  type: term
  name: >-
    Competitor Based Pricing
  definition: >-
    Competitor Based Pricing: whatever the average of what everyone else is charging.
  statement: >-
    Competitor based pricing is the model that sets the price at the average of what everyone else charges.
  why: >-
    You're a copycat: you're using a pricing strategy that isn't based on your business or your customers, it's based on their business and their customers.
  anchor: >-
    Competitor Based Pricing: whatever the average of what everyone else is charging
  source: >-
    playbook-pricing.md, Three Models Of Pricing, line 351
  confirmations: 1
  anchor_at: "playbook-pricing.md:351"
- id: E-playbooks-price-003
  type: term
  name: >-
    value Based Pricing
  definition: >-
    You base it on what a customer is willing to pay (WTP) rather than what "the competition" is willing to charge.
  statement: >-
    Value based pricing sets the price from the customer's willingness to pay, and the price rises as the product is made more valuable to them.
  not_to_confuse_with: >-
    Competitor based pricing: value based pricing is built on what the customer is willing to pay, not on what the competition is willing to charge.
  why: >-
    You can charge 2,3,4,5 x market rates or more if you make something a customer actually wants rather than just charging more for something they can get somewhere else for less, and you can continuously raise prices if you continuously add value.
  anchor: >-
    You base it on what a customer is willing to pay (WTP) rather than what
  source: >-
    playbook-pricing.md, Three Models Of Pricing, lines 356–377
  confirmations: 1
  anchor_at: "playbook-pricing.md:357"
- id: E-playbooks-price-004
  type: term
  name: >-
    The *perfect* price
  definition: >-
    The perfect price is the one that makes you the most money (not gets you the most customers).
  statement: >-
    In this method the perfect price is the price that maximizes money made over the lifetime of the customer, not the price that maximizes the number of customers.
  anchor: >-
    Unless you have a different short term strategy, the perfect price is the
  source: >-
    playbook-pricing.md, Three Metrics To Determine value-Driven Pricing, lines 384–385
  confirmations: 3
  authors_caveat: >-
    Unless you have a different short term strategy.
  anchor_at: "playbook-pricing.md:384"
- id: E-playbooks-price-005
  type: term
  name: >-
    Fixed Capacity
  definition: >-
    If you have a fixed capacity, and you are full, raise your prices. For example, if you are an artist and physically can't paint more than 10 paintings per month, then you have fixed capacity.
  statement: >-
    Fixed capacity is a business that physically cannot deliver more units in a period, so selling out every period is a signal the price is too low.
  anchor: >-
    Fixed Capacity . If you have a fixed capacity, and you are full, raise your prices.
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, line 425
  confirmations: 1
  anchor_at: "playbook-pricing.md:425"
- id: E-playbooks-price-006
  type: term
  name: >-
    The Lookback Window of Value
  definition: >-
    That $60,000 will be compared within the 'lookback window' of your last billing cycle, not the relationship.
  statement: >-
    The lookback window is the period a customer judges your value over, and it is the last billing cycle rather than the whole relationship.
  why: >-
    This is why longer billing cycles create less churn; they also get more qualified customers because they have to pay for longer periods up front.
  anchor: >-
    ‘lookback  window’  of  your  last  billing  cycle,  not  the  relationship.
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, Author Note: The Lookback Window of Value, line 476
  confirmations: 1
  authors_caveat: >-
    To be clear - this is just my theory.
  anchor_at: "playbook-pricing.md:476"
- id: E-playbooks-price-007
  type: term
  name: >-
    One-Time vs On-Going Value Pricing
  definition: >-
    Pricing should separate one time value from on-going value. Many mistakes happen when business owners mix them.
  statement: >-
    One time value and on-going value are two different things to bill for: a one time fee for what is delivered once, a smaller on-going fee that reflects the smaller on-going value.
  why: >-
    Sold as one price, the information is underpriced and the accountability overpriced; the day after you learn something, access to the information declines to close to zero, and a customer still paying a price based on not knowing it will likely stop paying.
  anchor: >-
    Match how you bill with how you provide value . One-Time vs On-Going Value Pric-
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 483–492
  confirmations: 1
  anchor_at: "playbook-pricing.md:483"
- id: E-playbooks-price-008
  type: term
  name: >-
    Customer Surplus
  definition: >-
    The difference between price and value is customer surplus. Some people call it goodwill.
  statement: >-
    Customer surplus is the gap between what a customer pays and the value they receive.
  why: >-
    The amount of customer surplus typically dictates how good your word of mouth is and how many times they repurchase; the author's preferred handling is a premium price that funds a far superior product, leaving surplus for them and net profit for him.
  anchor: >-
    between  price  and  value  is  customer  surplus.  Some  people  call  it  goodwill.
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 493–498
  confirmations: 1
  anchor_at: "playbook-pricing.md:494"
- id: E-playbooks-price-009
  type: term
  name: >-
    The *Instant Profit* Pricing Playbook
  definition: >-
    This list is all based on things that are designed to affect sales minimally (if at all). That way, you get the max increase with no change or minimal change in conversion rates.
  statement: >-
    The Instant Profit Pricing Playbook is the author's set of ten pricing plays selected because they take almost no work and are designed not to move conversion, together worth 26.8% to 63.8% added revenue (2025).
  anchor: >-
    And the best part, this list is all based on things that are designed to affect
  source: >-
    playbook-pricing.md, Small Percentages . Big Changes ., line 539
  confirmations: 2
  authors_caveat: >-
    There are other pricing strategies that create bigger swings, but they require more work/change/risk, so they were excluded from this text.
  anchor_at: "playbook-pricing.md:539"
- id: E-playbooks-price-010
  type: term
  name: >-
    Involuntary churn
  definition: >-
    Recurring payments get 1.2%-1.7% monthly involuntary churn due to card info changes.
  statement: >-
    Involuntary churn is the part of recurring revenue lost to card information changes rather than to a customer's decision, 1.2%-1.7% per month in 2025.
  why: >-
    If you have 5% monthly churn, this could be 24-34% of your total churn, which is why a second form of payment on file lifts LTV more than the processing fee itself.
  anchor: >-
    Recurring payments get 1.2%-1.7% monthly involuntary churn
  source: >-
    playbook-pricing.md, Pricing Play #2: Processing Fees & Second Form of Payment, How It Works, lines 645–647
  confirmations: 1
  anchor_at: "playbook-pricing.md:645"
- id: E-playbooks-price-011
  type: term
  name: >-
    Premium (as against luxury)
  definition: >-
    Premium does not mean luxury. Luxury goods become more valuable because of their price. Whereas with premium goods, the price reflects the value of the product itself.
  statement: >-
    Premium and luxury are two different categories in this method: a luxury good gains value from being expensive, a premium good's price reflects the value of the product.
  not_to_confuse_with: >-
    Luxury: luxury items often end on a round number because people who buy luxury goods want not to get a deal, so .99 endings and turning 7s into 9s are not for them, while premium goods can take both.
  anchor: >-
    Premium does not mean luxury. Luxury goods become more valuable because of their
  source: >-
    playbook-pricing.md, Pricing Play #6: Round Up, My Advice, lines 961–963
  confirmations: 2
  anchor_at: "playbook-pricing.md:961"
- id: E-playbooks-price-012
  type: term
  name: >-
    Effective monthly rate
  definition: >-
    Whatever the annual renewal fee is, you can divide by 12 and add that to your effective monthly rate.
  statement: >-
    The effective monthly rate is the advertised monthly price plus one twelfth of any annual fee, which is what the business actually collects per month.
  why: >-
    People focus on the monthly price but rarely consider the annualized cost, so you get the benefit of the low advertised price for sales and the higher effective rate for profits.
  anchor: >-
    And if you do the math, whatever the annual renewal fee is, you can divide by 12 and
  source: >-
    playbook-pricing.md, Pricing Play #7: Annual Renewal Fee On Top of Monthly, How It Works, lines 1003–1004
  confirmations: 2
  anchor_at: "playbook-pricing.md:1003"
- id: E-playbooks-price-013
  type: term
  name: >-
    Automatic Continuity / Continued Access
  definition: >-
    Whatever you sell, you create the most paired down, zero work version of your thing. You price it at 5% to 20% of the main thing. Then, you simply 'tack it' at the end of whatever you sell on the front end.
  statement: >-
    Automatic continuity is a stripped, very high margin version of what you sell that the front end buyer agrees to up front and that starts automatically at 5-20% of the main price when the main term ends.
  not_to_confuse_with: >-
    'Undisclosed' or 'forced' continuity: this is continuity they must agree to up front, so you are clear about what happens after X time period.
  why: >-
    In comparison the price seems small and people suffer from sunk cost fallacy - they already spent x on the thing, they might as well pay 5-10% to keep it; it is the 'storage' for services businesses, and it builds a pool of lower ticket customers you can advertise to and ascend.
  anchor: >-
    Whatever you sell, you create the most paired down, zero work version of your thing.
  source: >-
    playbook-pricing.md, Pricing Play #8: Automatic Continuity, How It Works, lines 1056–1096
  confirmations: 2
  anchor_at: "playbook-pricing.md:1056"
- id: E-playbooks-price-014
  type: term
  name: >-
    Ultra High Ticket Anchor ('mac daddy' version)
  definition: >-
    All you have to do is add something to your suite of products or services that's 10x or more expensive than your core offer. Think of it like the 'mac daddy' version.
  statement: >-
    An ultra high ticket anchor is an item 10x or more expensive than the core offer, added to the menu and presented first so it anchors the price in the prospect's mind.
  why: >-
    Price anchors anchor the price in the prospect's mind, so you often close more people on the core offer because the anchor now makes it appear more affordable, and you make more money on the few who can afford the top item.
  anchor: >-
    add something to your suite of products or services that’s 10x or more expensive than
  source: >-
    playbook-pricing.md, Pricing Play #9: Ultra High Ticket Anchor, How It Works, lines 1141–1144
  confirmations: 1
  authors_caveat: >-
    Make sure you are actually willing to do the thing you sell for a lot of money; if you feel stressed when people buy it, keep raising the price until it makes you smile when they buy.
  anchor_at: "playbook-pricing.md:1143"
- id: E-playbooks-price-015
  type: term
  name: >-
    Priced Guarantee or Warranty
  definition: >-
    You sell your thing. Then, after the person agrees to buy, you offer a guarantee for 5-30% of the price of the product.
  statement: >-
    A priced guarantee or warranty is the guarantee you already give, sold as a paid add-on at 5-30% of the product price once the purchase is agreed.
  why: >-
    You are buying and selling risk: if you have high margins you can set the price of the guarantee equal to your cost of goods and never lose a dollar, and you keep the revenue and cover the cost of delivering again instead of refunding.
  anchor: >-
    offer a guarantee for 5-30% of the price of the product.
  source: >-
    playbook-pricing.md, Pricing Play #10: Guarantee and Warranty Upsells, How It Works, lines 1203–1226
  confirmations: 1
  anchor_at: "playbook-pricing.md:1204"
- id: E-playbooks-price-016
  type: term
  name: >-
    Price terrorists
  definition: >-
    Poor pricing forces you to run discounts all the time, which hurts your brand and turns customers into price terrorists. Always negotiating.
  statement: >-
    Price terrorists are the always-negotiating customers a business breeds in itself by constant discounting.
  anchor: >-
    hurts your brand and turns customers into price terrorists. Always negotiating.
  source: >-
    playbook-pricing.md, Why You Should Actually Do This, line 1325
  confirmations: 1
  anchor_at: "playbook-pricing.md:1325"
- id: E-playbooks-price-017
  type: term
  name: >-
    vicious price cycle
  definition: >-
    As you DECREASE your prices: your clients' emotional investment DECREASES, the perceived value of your service DECREASES, results DECREASE as a result of decreased investment and perceived value, clients INCREASE their demandingness, clients get LESS service because you have less money to spend on them.
  statement: >-
    The vicious price cycle is the chain that lowering prices sets off in the customers and in the business, ending in less profit per customer, less ability to create results and less conviction in the sales process.
  anchor: >-
    Here’s how the **vicious price cycle** works (which MOST businesses use).
  source: >-
    playbook-price-raise.md, Why Raising Prices Is A Good Idea, lines 155–170
  confirmations: 1
  anchor_at: "playbook-price-raise.md:155"
- id: E-playbooks-price-018
  type: term
  name: >-
    virtuous price cycle
  definition: >-
    When you INCREASE your prices: your clients' emotional investment INCREASES, the perceived value of your service INCREASES, results INCREASE, your clients DECREASE their demandingness, your clients get MORE service because you have MORE money to spend on them (race to the top).
  statement: >-
    The virtuous price cycle is the chain that raising prices sets off: more emotional investment and perceived value, better results, easier clients and a higher level of service paid for out of the extra profit.
  anchor: >-
    Here’s how the **virtuous price cycle** works (which is what raising prices does):
  source: >-
    playbook-price-raise.md, Why Raising Prices Is A Good Idea, lines 175–193
  confirmations: 1
  anchor_at: "playbook-price-raise.md:175"
- id: E-playbooks-price-019
  type: term
  name: >-
    RAISE
  definition: >-
    R - Remind them of the value they've gotten. A - Address the price change directly. I - Invest in their future. S - Soften the news with a loyalty discount. E - Explain away their concerns.
  statement: >-
    RAISE is the author's acronym for the five sections of a price raise letter; he credits Patrick Campbell of Profitwell, who oversaw 100 price increases directly and analyzed over 500, with collaborating on this concise version.
  anchor: >-
    My price raise letters have five sections. I use the acronym RAISE to remember it.
  source: >-
    playbook-price-raise.md, The Perfect Price Raise Letter, lines 332–337 (attribution lines 524–526)
  confirmations: 1
  anchor_at: "playbook-price-raise.md:332"
- id: E-playbooks-price-020
  type: term
  name: >-
    vanishing discount (loyalty reward)
  definition: >-
    We raise the price now and then immediately offer a discount that expires 3 to 6 months from now.
  statement: >-
    A vanishing discount is an expiring credit handed to existing customers at the moment of a price raise, so the announcement reads as a gift now rather than as a raise.
  why: >-
    People are more 'okay' with a vanishing discount than they are a raise in price, and they mind even less when another discount appears in the future.
  anchor: >-
    People are more ‘okay’ with a vanishing discount than they are a raise in price.
  source: >-
    playbook-price-raise.md, Section #4 - S: Soften the news with a loyalty reward., lines 408–414
  confirmations: 1
  anchor_at: "playbook-price-raise.md:409"
- id: E-playbooks-price-021
  type: term
  name: >-
    "pulled forward" churn
  definition: >-
    You simply "pulled forward" churn. Meaning, people who were going to cancel or not buy next month, just decide to do it a month sooner.
  statement: >-
    Pulled forward churn is the cancellation spike in the first month after a price raise that comes from people who were going to leave anyway, followed by a below-normal second month and a return to baseline in month three.
  why: >-
    Read this way, the spike costs only one month of revenue from that tiny slice rather than signalling that the price raise failed.
  anchor: >-
    you simply “pulled forward” churn. Meaning, people who were going to cancel or
  source: >-
    playbook-price-raise.md, Section #5 - E: Explain away their concerns., Type #3, lines 444–449
  confirmations: 1
  anchor_at: "playbook-price-raise.md:447"
- id: E-playbooks-price-022
  type: term
  name: >-
    Stair step discount
  definition: >-
    Drop off the discount at 6 month intervals to accomplish 2-3 mini jumps in price.
  statement: >-
    A stair step discount delivers one large price raise as two or three smaller jumps by letting parts of a discount expire at intervals.
  why: >-
    People have an easier time handling disappearing discounts rather than raised prices.
  applies_when: >-
    If the price raise is a lot.
  anchor: >-
    Stair step discount: If the price raise is a lot, you can “stair step” - aka - drop off the dis-
  source: >-
    playbook-price-raise.md, Price Raise Checklist, lines 720–722
  confirmations: 2
  anchor_at: "playbook-price-raise.md:720"
- id: E-playbooks-price-023
  type: term
  name: >-
    back end product
  definition: >-
    A back end product would do two things. It would stabilize and grow the revenue.
  statement: >-
    A back end product is a second thing to sell to customers you already have: it stabilizes revenue when fewer new customers come in and grows it when they do.
  why: >-
    Even if they had fewer customers coming in, their current customers could still spend; so best case they made more, and worst case they stayed the same, and priced right it would only need one out of five customers to buy it to double the revenue.
  anchor: >-
    We both agreed we needed to add a back end product. A back end product would do
  source: >-
    playbook-lifetime-value.md, Increasing Lifetime Value: The Crazy 8, lines 66–72
  confirmations: 1
  anchor_at: "playbook-lifetime-value.md:66"
- id: E-playbooks-price-024
  type: term
  name: >-
    LTV / lifetime gross profit (LTGP) / customer lifetime value (CLV)
  definition: >-
    Lifetime value (LTV) is the gross profit collected over the lifespan of a customer. In other words, how much total money you make from a customer minus everything it costs you to deliver it. I sometimes call it lifetime gross profit (LTGP). Some places refer to it as customer lifetime value (CLV). Gross profit x average transactions per customer = LTGP; Gross profit / Churn = LTGP.
  statement: >-
    LTV in this method is lifetime gross profit - the money from a customer minus the cost of delivering to them - and LTGP and CLV are the author's names for the same number.
  not_to_confuse_with: >-
    Lifetime revenue: the pricing playbook spells out what is wanted as the highest total lifetime value "(specifically, lifetime gross profit)", and its tables carry Lifetime Revenue as a separate line from Gross Profit.
  why: >-
    If advertising is the machine that makes a business grow, LTV is the fuel: the owner who can make a customer more valuable to his business than to his competition can outbid everyone in every auction for attention.
  anchor: >-
    Lifetime value (LTV) is the gross profit collected over the lifespan of a customer.
  source: >-
    playbook-lifetime-value.md, What Is LTV?, lines 121–124
  confirmations: 2
  anchor_at: "playbook-lifetime-value.md:121"
- id: E-playbooks-price-025
  type: term
  name: >-
    Gross Profit
  definition: >-
    Gross Profit is what's leftover from a purchase after you deliver the goods or service.
  statement: >-
    Gross profit is what a sale leaves after the cost of delivering it, and it is the figure every LTV calculation in this method is built from.
  not_to_confuse_with: >-
    Net profit, which is what's left over after you paid all expenses; you use gross profit to pay the rest of your bills.
  anchor: >-
    Profit is what’s leftover from a purchase after you deliver the goods or service. Note: this isn’t net
  source: >-
    playbook-lifetime-value.md, How To Calculate LTV, Step One: Gross Profit, lines 156–159
  confirmations: 1
  anchor_at: "playbook-lifetime-value.md:157"
- id: E-playbooks-price-026
  type: term
  name: >-
    Churn
  definition: >-
    Churn is the percentage of customers that leave between time periods. Churn = people who left divided by original amount.
  statement: >-
    Churn is the share of the customers you began a period with who left during it.
  not_to_confuse_with: >-
    Net change in customer count: if you sign up new clients during the time period, it does not affect churn - the same number of original people left, whether you signed up zero or 1,000 new clients.
  anchor: >-
    to introduce a new concept - churn. Churn is the percentage of customers that leave
  source: >-
    playbook-lifetime-value.md, How To Calculate LTV, Step Two, lines 193–207
  confirmations: 1
  anchor_at: "playbook-lifetime-value.md:193"
- id: E-playbooks-price-027
  type: term
  name: >-
    The Crazy Eight
  definition: >-
    1) Raise prices 2) Lower the cost of delivering the thing 3) Upsell Frequency: Get them to buy more again later 4) Upsell Quantity: Get them to buy more now 5) Upsell Quality: Get them to buy a premium version 6) Downsell Quantity: Get them to buy fewer things rather than nothing 7) Downsell Quality: Get them to buy lower-cost things rather than nothing 8) Cross-Sell: Get them to buy a different thing on top.
  statement: >-
    The Crazy Eight is the author's name for the eight ways to make a customer worth more.
  why: >-
    "There are only two ways to make a customer more valuable...you can increase average order value, or increase the number of times they buy" felt 'too broad' to make actionable, so he broke it into smaller chunks he could apply to any business.
  anchor: >-
    The crazy eight are as follows:
  source: >-
    playbook-lifetime-value.md, The Crazy Eight, lines 238–246
  confirmations: 2
  anchor_at: "playbook-lifetime-value.md:238"
- id: E-playbooks-price-028
  type: term
  name: >-
    Upsell Frequency (#3 Increase # of Purchases)
  definition: >-
    Upsell Frequency: Get them to buy more again later. You get people to buy the same thing more times.
  statement: >-
    Upsell frequency raises how many times a customer buys the same thing, and there are only three ways to do it: add recurring, decrease churn, and make regular follow up offers.
  not_to_confuse_with: >-
    Upsell quantity - buying more at once - which the author explicitly sets aside here ("rather than buying more at once, which I'll cover later").
  anchor: >-
    You  get  people  to  buy  the  same  thing  more  times  (rather  than  buying  more  at  once,
  source: >-
    playbook-lifetime-value.md, #3 Increase # of Purchases, lines 347–351
  confirmations: 2
  anchor_at: "playbook-lifetime-value.md:348"
- id: E-playbooks-price-029
  type: term
  name: >-
    Cross-Sell
  definition: >-
    You sell another product that complements - or goes with - your first product. Cross-Sell: Get them to buy a different thing on top.
  statement: >-
    A cross-sell is a different, complementary product sold on top of the first one, and what it adds to LTV is the conversion rate x gross profit of that product.
  not_to_confuse_with: >-
    An upsell: a cross-sell is a different thing on top, not more, bigger or better of the same thing.
  anchor: >-
    You  sell  another  product  that  complements  -  or  goes  with  -  your  first  product.  I  talk
  source: >-
    playbook-lifetime-value.md, #4 Cross-Sell Something Different, lines 403–410
  confirmations: 2
  authors_caveat: >-
    Pick one that does not dramatically change who you serve or what you do every day: you don't wanna break your business to pick up some extra change.
  anchor_at: "playbook-lifetime-value.md:404"
- id: E-playbooks-price-030
  type: term
  name: >-
    Sell More (Increase Quantity)
  definition: >-
    You sell more of the same thing at once. First, you can sell more of the same thing, think "bulk" purchasing. Second, you can sell increased frequency of delivery, think "more often." Third, you can sell more in the same package, think "bigger."
  statement: >-
    A quantity upsell sells more of the same thing at once - in bulk, more often, or bigger.
  why: >-
    Offered first on sales calls, with the standard offer as the downsell, the author reports you may see 20%+ lifts in cash collected overnight.
  anchor: >-
    You sell more of the same thing at once. This happens in three main ways. And I like
  source: >-
    playbook-lifetime-value.md, #5 Sell More (Increase Quantity), lines 423–438
  confirmations: 2
  anchor_at: "playbook-lifetime-value.md:424"
- id: E-playbooks-price-031
  type: term
  name: >-
    Sell Better (Increase Quality)
  definition: >-
    You sell a better version of the same thing. The better version comes at a higher price. First, a newer version of the same thing. Second, a premium version of the same thing (think better ingredients, better materials, or better people).
  statement: >-
    A quality upsell sells a newer or premium version of the same thing at a higher price, built from levers such as speed of response, service ratio, availability, personalization and provider qualifications.
  anchor: >-
    You sell a better version of the same thing. The better version comes at a higher price.
  source: >-
    playbook-lifetime-value.md, #6 Sell Better (Increase Quality), lines 443–486
  confirmations: 2
  anchor_at: "playbook-lifetime-value.md:444"
- id: E-playbooks-price-032
  type: term
  name: >-
    DIY, DWY, DFY
  definition: >-
    DIY, DWY, DFY: Do It Yourself vs. Done With You vs. Done For You.
  statement: >-
    DIY, DWY and DFY name the three levels at which the same result can be delivered, and they serve as a quality lever upward, a downsell lever downward and a cost lever at the same time.
  why: >-
    If you switch what you sell from "I'll do it for you" to "I'll help you do it" you can dramatically increase your ratio of customers to your employees, and if this only incurs a minor decrease in price, it can be a very profitable switch.
  anchor: >-
    DIY, DWY, DFY: Do It Yourself vs. Done With You vs. Done For You.
  source: >-
    playbook-lifetime-value.md, #6 Sell Better (Increase Quality), line 472
  confirmations: 3
  anchor_at: "playbook-lifetime-value.md:472"
- id: E-playbooks-price-033
  type: term
  name: >-
    Downsell Fewer (Lower Quantity)
  definition: >-
    You sell a smaller amount of the same thing. You can sell fewer of the same thing, you can sell a smaller version, or less frequent 'doses'. Downsell Quantity: Get them to buy fewer things rather than nothing.
  statement: >-
    A quantity downsell offers fewer, smaller or less frequent units of the same thing to someone who would otherwise buy nothing.
  why: >-
    If it means this or nothing, then this beats nothing; but you lose money on downsells when people who would've bought the $5 thing now opt for the $2.50 thing.
  applies_when: >-
    Begin offering it only to customers who do not qualify for your main offer.
  anchor: >-
    You sell a smaller amount of the same thing. This works the same way as the quantity
  source: >-
    playbook-lifetime-value.md, #7 Downsell Fewer (Lower Quantity), lines 491–521
  confirmations: 2
  anchor_at: "playbook-lifetime-value.md:492"
- id: E-playbooks-price-034
  type: term
  name: >-
    Downsell Lower Quality
  definition: >-
    You downsell something that gets the same result for the customer as your main offer but with a lower quality experience. It might take longer, have higher risk, or they incur more hassles by downgrading. All we do is take the list for a quality upsell and reverse it.
  statement: >-
    A quality downsell gets the customer the same result through a worse experience - slower, riskier, more hassle - and is built by reversing the quality upsell list.
  applies_when: >-
    Begin offering it only to customers who do not qualify for your main offer.
  anchor: >-
    You downsell something that gets the same result for the customer as your main offer
  source: >-
    playbook-lifetime-value.md, #8 Downsell Lower Quality, lines 526–556
  confirmations: 2
  anchor_at: "playbook-lifetime-value.md:527"
```
