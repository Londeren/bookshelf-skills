# Улов фазы 1 — $100M Playbooks: Pricing, Price Raise, Lifetime Value (2025) (ярус 2), тип D: антипаттерны и границы

Группа `tier2-playbooks-price`, слаг `playbooks-price`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **69** (экстрактор вернул 69, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `playbook-pricing.md` | 1–1381 | 2 | 37 |
| `playbook-price-raise.md` | 1–758 | 2 | 23 |
| `playbook-lifetime-value.md` | 1–613 | 1 | 9 |

## Как собран файл

Экстрактор D (Antipatterns and boundaries) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-playbooks-price.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-playbooks-price-D.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: D-playbooks-price-001
  type: rule
  name: >-
    Author Note: Avoiding Complexity The Best I Can
  statement: >-
    The genie model that compares doubling customers, purchases and price counts only the cost of advertising and the cost of delivering, so its exact multiples do not transfer to a business with a different cost structure.
  why: >-
    Different businesses have different costs for different things; the model is kept simple to show where profit is maximized, not to reproduce anyone's P&L.
  boundary: >-
    Only advertising and delivery costs are in the model; any other cost line is outside it.
  anchor: >-
    To simplify stuff, I have only included costs of advertising and delivering. Different
  source: >-
    playbook-pricing.md, Pricing To Make The Most Money, Author Note: Avoiding Complexity The Best I Can, lines 202-205
  confirmations: 1
  anchor_at: "playbook-pricing.md:203"
- id: D-playbooks-price-002
  type: antipattern
  name: >-
    Pricing by looking at what everyone charges
  statement: >-
    Setting your price by looking at what everyone else charges and landing somewhere in the middle.
  why: >-
    It is the recipe for break even and burnout - you run a nonprofit with none of the benefits - and the people you are copying are broke.
  anchor: >-
    People usually price by simply looking at what everyone charges. This is the recipe for
  source: >-
    playbook-pricing.md, Three Models Of Pricing, lines 337-338
  confirmations: 2
  anchor_at: "playbook-pricing.md:337"
- id: D-playbooks-price-003
  type: antipattern
  name: >-
    Cost Plus Pricing
  statement: >-
    Pricing at whatever your costs are plus an arbitrarily added margin.
  why: >-
    You never capture the people who would have paid more because they need it more, costs change and are not all known ahead of time, and the customer has no idea what it costs you anyway.
  anchor: >-
    customers have no idea what it costs you, so your costs don’t matter to them.
  source: >-
    playbook-pricing.md, Three Models Of Pricing, 1) Cost Plus Pricing, lines 342-346
  confirmations: 1
  anchor_at: "playbook-pricing.md:346"
- id: D-playbooks-price-004
  type: antipattern
  name: >-
    Competitor Based Pricing
  statement: >-
    Pricing at the average of what everyone else is charging.
  why: >-
    You are a copycat running a pricing strategy built on someone else's business and someone else's customers; it is hard to make a shoe fit when it is not yours.
  anchor: >-
    b) Cons: You’re a copycat. You’re using a pricing strategy that isn’t based on your busi-
  source: >-
    playbook-pricing.md, Three Models Of Pricing, 2) Competitor Based Pricing, lines 351-355
  confirmations: 1
  anchor_at: "playbook-pricing.md:353"
- id: D-playbooks-price-005
  type: rule
  name: >-
    Cons of value Based Pricing
  statement: >-
    Value based pricing is the model to use, but the author states its cost himself: it shifts the work from getting the most customers to providing the most value to each customer.
  why: >-
    That is a different type of work than most people are used to; it requires a brain to think and hands to work.
  boundary: >-
    Only for an owner prepared to do the different work of raising the value of the product rather than chasing volume.
  anchor: >-
    b) Cons: This focuses less on trying to get the most customers possible and more on
  source: >-
    playbook-pricing.md, Three Models Of Pricing, 3) value Based Pricing, lines 372-375
  confirmations: 1
  anchor_at: "playbook-pricing.md:372"
- id: D-playbooks-price-006
  type: rule
  name: >-
    Price elasticity holds for non-luxury goods
  statement: >-
    The rule that people buy less often and repurchase less often as the price goes up is stated for non-luxury goods.
  why: >-
    Luxury is the exception the author names: for luxury goods the expense itself is what makes the thing valuable.
  boundary: >-
    Non-luxury goods.
  anchor: >-
    When  you  increase  the  price  for  non-luxury  goods,  people  buy  less  often  (and  repur-
  source: >-
    playbook-pricing.md, Three Metrics To Determine value-Driven Pricing, lines 382-383
  confirmations: 2
  anchor_at: "playbook-pricing.md:382"
- id: D-playbooks-price-007
  type: rule
  name: >-
    The perfect price is the one that makes the most money
  statement: >-
    The perfect price is the one that makes the most money, not the one that gets the most customers - unless you are running a different short term strategy.
  why: >-
    The thing you want is the highest number of people converting at the highest total lifetime value, the total return column of the table, not the biggest customer count.
  boundary: >-
    Holds unless you have a different short term strategy.
  anchor: >-
    price for your product. Unless you have a different short term strategy, the perfect price is the
  source: >-
    playbook-pricing.md, Three Metrics To Determine value-Driven Pricing, lines 384-385
  confirmations: 3
  anchor_at: "playbook-pricing.md:384"
- id: D-playbooks-price-008
  type: antipattern
  name: >-
    Pricing to maximize the first purchase
  statement: >-
    Setting the highest price you can get people to buy at once, instead of the price they will keep paying.
  why: >-
    If customers buy different things from you or buy the same thing repeatedly, the money is made over the lifetime of the customer, so a price optimized for the first purchase leaves the rest behind.
  anchor: >-
    price I could get people to buy at. But now I want the price that people will keep paying at.
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 412-417
  confirmations: 2
  anchor_at: "playbook-pricing.md:417"
- id: D-playbooks-price-009
  type: antipattern
  name: >-
    Changing your price back at the first no
  statement: >-
    Reverting a price increase as soon as you get your first no.
  why: >-
    You have to keep raising until the extra money from new sales no longer offsets the lost sales; going from a 50% to a 30% close rate on double the price makes more money even though you hear no about 40% more often.
  applies_when: >-
    Right after a price increase, when the first refusals arrive.
  anchor: >-
    to delay changing your price back when you get your first no. If you go from 50% close rate
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 428-431
  confirmations: 1
  anchor_at: "playbook-pricing.md:430"
- id: D-playbooks-price-010
  type: rule
  name: >-
    Some markets are price sensitive
  statement: >-
    Raising prices yields more profit than it loses in sales about nine times out of ten, but some markets are price sensitive and others less so.
  why: >-
    The rule is a probability, not a guarantee; the owner has to be willing to stomach the extra refusals.
  boundary: >-
    Price-sensitive markets are the tenth case where the raise does not pay.
  anchor: >-
    price sensitive. Others less so. But 9 times out of 10, when you raise your prices, you make
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 436-438
  confirmations: 1
  anchor_at: "playbook-pricing.md:437"
- id: D-playbooks-price-011
  type: antipattern
  name: >-
    Caving to get more yesses
  statement: >-
    Going back to charging less just to get more yesses after a price raise makes you hear more nos.
  why: >-
    Hearing no sucks so much that owners cave and optimize for yesses rather than for money; on paper they know fewer customers at a higher price makes more money, and they still revert.
  anchor: >-
    that they often cave and go back to charging less just to get more yesses (rather than to make
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 442-448
  confirmations: 1
  anchor_at: "playbook-pricing.md:447"
- id: D-playbooks-price-012
  type: rule
  name: >-
    How to know you raised your prices too much
  statement: >-
    You have raised prices too far when you stop making sales, or when people start complaining about the value for the cost.
  why: >-
    These are the two observable signals of overshooting; the complaint signal is measured objectively with NPS scores.
  boundary: >-
    The upper limit of the raise-until-it-hurts rule.
  anchor: >-
    How to know you raised your prices too much . You stop making sales. Or, people start
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 449-450
  confirmations: 1
  anchor_at: "playbook-pricing.md:449"
- id: D-playbooks-price-013
  type: rule
  name: >-
    Different prices per customer avatar is an advanced strategy
  statement: >-
    Charging different prices to different customer avatars requires the operational chops to deliver at different levels.
  why: >-
    One avatar can have 5-10x the willingness to pay of another, but capturing that means more prices and more levels of service to actually deliver.
  boundary: >-
    A more advanced strategy; only for a business that can operate several levels of service, and if there are tiers the customer must know which one is for them.
  anchor: >-
    spending power. To be clear, this is a more advanced strategy that requires the operational
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 451-460
  confirmations: 1
  anchor_at: "playbook-pricing.md:457"
- id: D-playbooks-price-014
  type: rule
  name: >-
    Author Note: The Lookback Window of Value
  statement: >-
    Customers judge the value they got inside the lookback window of the last billing cycle rather than over the whole relationship, which is why longer billing cycles create less churn.
  why: >-
    A client you made $60,000 in month one will still cancel if month two makes them $0, because the comparison runs against the last cycle, not the relationship.
  anchor: >-
    why longer billing cycles, in my opinion, create less churn. They also get more
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, Author Note: The Lookback Window of Value, lines 471-479
  confirmations: 1
  authors_caveat: >-
    The author marks this explicitly as unverified: To be clear - this is just my theory.
  anchor_at: "playbook-pricing.md:477"
- id: D-playbooks-price-015
  type: antipattern
  name: >-
    Mixing one time value and on-going value in one price
  statement: >-
    Selling one-time value and on-going value under a single price.
  why: >-
    The one-time part ends up underpriced and the on-going part overpriced; access to information declines to near zero the day after you learn it, so a customer still paying a price set for not knowing it stops paying.
  applies_when: >-
    Whenever the offer contains both a one-time component such as information and an on-going one such as accountability; the author's fix is a one time fee for access plus a smaller on-going fee.
  anchor: >-
    Let’s say I sell information and I sell accountability. If I sell that as one price, my infor-
  source: >-
    playbook-pricing.md, Rules of Pricing I Follow, lines 483-492
  confirmations: 1
  anchor_at: "playbook-pricing.md:486"
- id: D-playbooks-price-016
  type: rule
  name: >-
    The play percentages are estimates
  statement: >-
    The 26.8% to 63.8% revenue lift of the ten pricing plays is an estimate, not a measured figure.
  why: >-
    The author states it outright while showing how large the effect would be against the 7-10% net margins of the average U.S. small business in 2024.
  boundary: >-
    Treat the totals as estimates when planning on them.
  anchor: >-
    to be clear, they’re estimates. But, the average small business in the U.S. in 2024 runs 7-10%
  source: >-
    playbook-pricing.md, Small Percentages . Big Changes ., lines 535-538
  confirmations: 1
  anchor_at: "playbook-pricing.md:537"
- id: D-playbooks-price-017
  type: rule
  name: >-
    Author Note: Are There More Pricing Hacks?
  statement: >-
    Pricing strategies that create bigger swings exist but are deliberately excluded from this playbook because they require more work, more change and more risk.
  why: >-
    The playbook is scoped to instant-profit moves designed to affect sales minimally or not at all.
  boundary: >-
    The ten plays are the low-effort subset; bigger pricing moves are out of scope of this text.
  anchor: >-
    more work/change/risk. So, I excluded them from this text. This is the *instant
  source: >-
    playbook-pricing.md, The *Instant Profit* Pricing Playbook, Author Note: Are There More Pricing Hacks?, lines 564-567
  confirmations: 1
  anchor_at: "playbook-pricing.md:566"
- id: D-playbooks-price-018
  type: rule
  name: >-
    Not every play fits every business
  statement: >-
    Some of the ten plays will not be a direct fit for a given business, and only one implemented play is needed to make more money.
  why: >-
    The plays are a menu to select from, not a checklist to complete.
  boundary: >-
    Pick the one or two with the biggest impact for the least work and risk rather than applying all ten.
  anchor: >-
    Some of these you will be able to immediately use. Some of them won’t be a direct fit for
  source: >-
    playbook-pricing.md, The *Instant Profit* Pricing Playbook, lines 568-569
  confirmations: 2
  anchor_at: "playbook-pricing.md:568"
- id: D-playbooks-price-019
  type: antipattern
  name: >-
    Weekly and bi-weekly billing
  statement: >-
    Billing weekly or bi-weekly to get the extra cycles, although the theoretical benefit is the same as every four weeks.
  why: >-
    In reality weekly and bi-weekly caused a lot of billing hassles because people wanted to go on short pauses.
  applies_when: >-
    The author's fix: stick with 4 weeks, 12 weeks or longer, and display the price weekly for the lowest perceived price while billing every four weeks.
  anchor: >-
    ly and bi-weekly caused a lot of billing hassles because people wanted to go on short pauses.
  source: >-
    playbook-pricing.md, PRICING PLAY #1: MONTHLY TO 28 DAY BILLING CYCLES, My Advice, lines 608-613
  confirmations: 1
  anchor_at: "playbook-pricing.md:610"
- id: D-playbooks-price-020
  type: antipattern
  name: >-
    Paying the sales tax for your customers
  statement: >-
    Absorbing sales tax instead of adding it to the price.
  why: >-
    Sales tax comes off the top line, so a business on 20% margins paying 5% sales tax gives away 25% of its profit.
  anchor: >-
    paying sales tax for your customers, you’re taking a massive hit. Think about it - if you have
  source: >-
    playbook-pricing.md, PRICING PLAY #3: SALES TAX, How It Works, lines 690-693
  confirmations: 1
  anchor_at: "playbook-pricing.md:691"
- id: D-playbooks-price-021
  type: rule
  name: >-
    Pro Tip: You Cannot Charge Taxes You Do Not Pay
  statement: >-
    If you do not get charged taxes, you cannot charge them to the customer.
  why: >-
    The play only recoups a cost you actually carry; where there is no tax there is nothing to pass on.
  boundary: >-
    The sales tax play applies only where your state or country actually charges tax for your thing.
  anchor: >-
    To be clear, if you do not get charged taxes, you cannot charge them. But, if you
  source: >-
    playbook-pricing.md, PRICING PLAY #3: SALES TAX, Pro Tip: You Cannot Charge Taxes You Do Not Pay, lines 701-707
  confirmations: 1
  anchor_at: "playbook-pricing.md:702"
- id: D-playbooks-price-022
  type: rule
  name: >-
    Reincorporating in a tax friendly state
  statement: >-
    Incorporating in a different state that does not charge sales tax is an alternative to passing tax on, and it is to be checked with lawyers first.
  why: >-
    It takes administrative work and touches huge chunks of the bottom line; the point is not to make money but to keep it.
  boundary: >-
    Check with lawyers before doing it.
  anchor: >-
    money it’s to keep it. And, of course, check with lawyers etc. before you do it.
  source: >-
    playbook-pricing.md, PRICING PLAY #3: SALES TAX, Pro Tip: Incorporate in a Different State, lines 708-713
  confirmations: 1
  anchor_at: "playbook-pricing.md:713"
- id: D-playbooks-price-023
  type: antipattern
  name: >-
    That’s not gonna make a difference in my business
  statement: >-
    Dismissing annual price increases as immaterial while leaving prices untouched for years.
  why: >-
    Inflation already moved the price, in the other direction: a service priced at $100 in 2017 and never changed has around 21% less spending power by 2024, and at 20% margins the same customer count leaves no profit seven years later.
  anchor: >-
    business.” Except, they haven’t adjusted their prices in five years...so it already has...just in
  source: >-
    playbook-pricing.md, PRICING PLAY #4: ANNUAL PRICE INCREASES, How It Works & Examples, lines 754-786
  confirmations: 2
  anchor_at: "playbook-pricing.md:758"
- id: D-playbooks-price-024
  type: antipattern
  name: >-
    Raising the CPI clause during the sale
  statement: >-
    Bringing up the annual price increase clause during the sale itself.
  why: >-
    The author's instruction is to keep it out of the sale and raise it while filling out the paperwork.
  anchor: >-
    goes up.” Note: You don’t mention this during the sale, you can bring it up when you’re fill-
  source: >-
    playbook-pricing.md, PRICING PLAY #4: ANNUAL PRICE INCREASES, Steps To Implement It, lines 804-808
  confirmations: 1
  anchor_at: "playbook-pricing.md:807"
- id: D-playbooks-price-025
  type: rule
  name: >-
    Keep the annual increase under 15%
  statement: >-
    Few people balk at a contractual annual price increase as long as it is kept under 15%.
  why: >-
    Even at that ceiling the compounding is enormous - a 57% price increase over the long term.
  boundary: >-
    Under 15% per year; 5 to 15 percent is the starting range.
  anchor: >-
    Few people will balk if you keep it under 15% (which...a 57% increase in prices over
  source: >-
    playbook-pricing.md, PRICING PLAY #4: ANNUAL PRICE INCREASES, Steps To Implement It, lines 801-810
  confirmations: 1
  anchor_at: "playbook-pricing.md:809"
- id: D-playbooks-price-026
  type: rule
  name: >-
    Annual billing drops conversions by an unknown amount
  statement: >-
    Requiring annual prepayment can 5x LTV but sells fewer customers because the price is 12x the monthly rate, and whether the conversion drop is worth it is unknown and has to be tested per business.
  why: >-
    The author states plainly that he does not know whether it drops conversions 5x.
  boundary: >-
    Test it for your own business before requiring annual billing.
  anchor: >-
    monthly  rate.  So  this  drops  conversions.  The  question  is  -  does  it  drop  conversions  5x?  I
  source: >-
    playbook-pricing.md, PRICING PLAY #5: ANNUAL BILLING, How It Works, lines 833-836
  confirmations: 1
  anchor_at: "playbook-pricing.md:835"
- id: D-playbooks-price-027
  type: rule
  name: >-
    Offering only the annual cadence is an advanced move
  statement: >-
    Offering annual billing as the only pricing cadence is a pretty advanced move; the ordinary version is to offer the option with an incentive.
  why: >-
    Simply adding the option with a discount or prepay bonuses makes a lot more money and risks nothing, since you can always revert to standard pricing.
  boundary: >-
    Annual-only pricing is advanced; adding annual and quarterly options is the zero-risk version.
  anchor: >-
    Now, I’m not saying you should only offer this pricing cadence. That’s a pretty advanced
  source: >-
    playbook-pricing.md, PRICING PLAY #5: ANNUAL BILLING, Steps To Implement It, lines 865-868
  confirmations: 1
  anchor_at: "playbook-pricing.md:866"
- id: D-playbooks-price-028
  type: rule
  name: >-
    Pro Tip: When NOT To Add .99 or change 7s to 9s
  statement: >-
    Do not round prices to .99 or turn 7s into 9s on luxury items, which usually end on a round number.
  why: >-
    People who buy luxury goods want not to get a deal; the fact that it is expensive and not a bargain is what makes luxury inherently valuable.
  boundary: >-
    Luxury goods only; for everything else the .99 endings work.
  anchor: >-
    Here’s a quick tip: Luxury items often end on a round number of typically 0 or
  source: >-
    playbook-pricing.md, PRICING PLAY #6: ROUND UP, Pro Tip: When NOT To Add .99 or change 7s to 9s, lines 946-952
  confirmations: 1
  authors_caveat: >-
    Of course, test it out. Sometimes shorter numbers do better.
  anchor_at: "playbook-pricing.md:947"
- id: D-playbooks-price-029
  type: antipattern
  name: >-
    Premium does not mean luxury
  statement: >-
    Treating a premium product as if it were a luxury one and therefore skipping the .99 and 9-ending price endings.
  why: >-
    Luxury goods become more valuable because of their price, whereas with premium goods the price reflects the value of the product itself, so the luxury exception does not cover them.
  anchor: >-
    Premium does not mean luxury. Luxury goods become more valuable because of their
  source: >-
    playbook-pricing.md, PRICING PLAY #6: ROUND UP, My Advice, lines 961-964
  confirmations: 1
  anchor_at: "playbook-pricing.md:961"
- id: D-playbooks-price-030
  type: rule
  name: >-
    Author Note: Conflict With Billing Annually?
  statement: >-
    If you can bill annually, do that; the annual renewal fee on top of a monthly rate is for markets where customers are more price conscious.
  why: >-
    In those markets the fee lifts annual revenue per customer significantly without impacting sales conversions, which annual billing would.
  boundary: >-
    Play #7 is the fallback where annual billing is not sellable, not an addition to it.
  anchor: >-
    If you can bill annually, by all means do it. But in some markets, customers are
  source: >-
    playbook-pricing.md, PRICING PLAY #7: ANNUAL RENEWAL FEE ON TOP OF MONTHLY, Author Note: Conflict With Billing Annually?, lines 994-998
  confirmations: 1
  anchor_at: "playbook-pricing.md:995"
- id: D-playbooks-price-031
  type: antipattern
  name: >-
    Pro Tip: Don’t Be A Sneak
  statement: >-
    Running automatic continuity as undisclosed or forced continuity instead of continuity the customer agrees to up front.
  why: >-
    The play requires being clear about what happens after the stated period; in the author's experience people like knowing there is a more cost effective version at the end.
  anchor: >-
    For avoidance of confusion. This isn’t ‘undisclosed’ or ‘forced’ continuity. This
  source: >-
    playbook-pricing.md, PRICING PLAY #8: AUTOMATIC CONTINUITY, Pro Tip: Don’t Be A Sneak, lines 1092-1096
  confirmations: 1
  anchor_at: "playbook-pricing.md:1093"
- id: D-playbooks-price-032
  type: rule
  name: >-
    Only anchor with something you are willing to deliver
  statement: >-
    The ultra high ticket anchor must be something you are actually willing to do for the money, and if a purchase of it stresses you, raise its price until a purchase makes you smile.
  why: >-
    You can offer whatever you want as the anchor, but you have to be excited when someone buys it.
  boundary: >-
    The anchor is a real offer you must be able and willing to fulfil, not a decoy.
  anchor: >-
    Make sure you are actually willing to do the thing you sell for a lot of money. And if
  source: >-
    playbook-pricing.md, PRICING PLAY #9: ULTRA HIGH TICKET ANCHOR, My Advice, lines 1182-1184
  confirmations: 2
  anchor_at: "playbook-pricing.md:1182"
- id: D-playbooks-price-033
  type: rule
  name: >-
    The guarantee must out-earn the cost of honoring it
  statement: >-
    The revenue of a priced guarantee or warranty has to exceed the cost of fixing or replacing the product.
  why: >-
    You are buying and selling risk, so it comes down to knowing your numbers; with a known low claim rate the 10% is pure profit, and you cover the cost of delivering again rather than refunding.
  boundary: >-
    Only price a guarantee where you know your claim rate and cost to replace.
  anchor: >-
    You  want  the  revenue  of  the  guarantee  to  exceed  the  cost  of  fixing  the  product.  And  the
  source: >-
    playbook-pricing.md, PRICING PLAY #10: GUARANTEE AND WARRANTY UPSELLS, How It Works, lines 1202-1227
  confirmations: 2
  anchor_at: "playbook-pricing.md:1208"
- id: D-playbooks-price-034
  type: rule
  name: >-
    Where the guarantee upsell works best
  statement: >-
    The one-line guarantee upsell at checkout works especially well with main street and traditional businesses.
  why: >-
    It costs nothing to deliver besides doing the math upfront.
  boundary: >-
    Named field of best fit: main street and traditional businesses.
  anchor: >-
    This little one-line upsell at checkout works especially well with ‘main street’ and ‘tradi-
  source: >-
    playbook-pricing.md, PRICING PLAY #10: GUARANTEE AND WARRANTY UPSELLS, My Advice, lines 1289-1291
  confirmations: 1
  anchor_at: "playbook-pricing.md:1290"
- id: D-playbooks-price-035
  type: antipattern
  name: >-
    Adjusting prices only when you have to
  statement: >-
    Raising prices only when forced to, instead of when you choose to.
  why: >-
    Inflation erodes profit in every economy, so the raise happens either way; doing it only under pressure forfeits all the benefits of doing it deliberately.
  anchor: >-
    survive you must raise prices. But only adjusting prices when you have to avoids all benefits
  source: >-
    playbook-pricing.md, Why You Should Actually Do This, lines 1292-1295
  confirmations: 2
  anchor_at: "playbook-pricing.md:1294"
- id: D-playbooks-price-036
  type: antipattern
  name: >-
    Prices that are too cheap
  statement: >-
    Charging too little drives good customers away.
  why: >-
    Prices that are too cheap make good buyers go elsewhere, and underpricing devalues the product.
  anchor: >-
    Drive away good customers - Prices that are too cheap make good buyers go else-
  source: >-
    playbook-pricing.md, Why You Should Actually Do This, lines 1319-1329
  confirmations: 2
  anchor_at: "playbook-pricing.md:1322"
- id: D-playbooks-price-037
  type: antipattern
  name: >-
    Constant discounting
  statement: >-
    Compensating for bad pricing by running discounts all the time.
  why: >-
    It hurts your brand and turns customers into price terrorists who always negotiate.
  anchor: >-
    hurts your brand and turns customers into price terrorists. Always negotiating.
  source: >-
    playbook-pricing.md, Why You Should Actually Do This, lines 1324-1325
  confirmations: 1
  anchor_at: "playbook-pricing.md:1325"
- id: D-playbooks-price-038
  type: antipattern
  name: >-
    Dirt cheap rates to be generous
  statement: >-
    Pricing insanely cheap in the belief that customers who come in at dirt cheap rates will be the most grateful.
  why: >-
    Those were the absolute worst customers Trey ever had and created a customer service nightmare, while more customers still meant losing money every month.
  anchor: >-
    And Trey thought the customers coming in at dirt cheap rates would also feel the most
  source: >-
    playbook-price-raise.md, Raise Prices, lines 66-83
  confirmations: 2
  anchor_at: "playbook-price-raise.md:69"
- id: D-playbooks-price-039
  type: antipattern
  name: >-
    Waiting until disaster strikes
  statement: >-
    Waiting until the business is in distress before making the moves that raise profit fast.
  why: >-
    Feeding the fear of losing some customers ends in losing all of them when the business goes under; the universe forces your hand in a mad scramble to exist.
  anchor: >-
    business owners wait until disaster strikes before trying to make a bunch of money fast...
  source: >-
    playbook-price-raise.md, Raise Prices, lines 109-110
  confirmations: 2
  anchor_at: "playbook-price-raise.md:110"
- id: D-playbooks-price-040
  type: rule
  name: >-
    A price raise done wrong can kill the business
  statement: >-
    Raising prices can be a death sentence to a business that does it wrong and a miracle to one that does it right.
  why: >-
    It is one of the most important profit-building decisions, which is why the rules, the price pick and the letter come before the action.
  boundary: >-
    The upside is conditional on following the procedure; the same move done wrong destroys the business.
  anchor: >-
    can make - raising prices. This can be a death sentence to a business that does it wrong, or
  source: >-
    playbook-price-raise.md, Outline of This Playbook, lines 116-118
  confirmations: 1
  anchor_at: "playbook-price-raise.md:117"
- id: D-playbooks-price-041
  type: antipattern
  name: >-
    ‘Poor people’ thinking about price
  statement: >-
    Refusing to raise prices out of fear of angry messages, of falling sales, or of not being worth the money.
  why: >-
    Over the long term it becomes a race to the bottom, with you and every other poor business owner competing to have the lowest price.
  anchor: >-
    money. It’s ‘poor people’ thinking. And over the long term, it becomes a race to the bottom.
  source: >-
    playbook-price-raise.md, Why Raising Prices Is A Good Idea, lines 138-141
  confirmations: 1
  anchor_at: "playbook-price-raise.md:140"
- id: D-playbooks-price-042
  type: antipattern
  name: >-
    Being the second lowest price
  statement: >-
    Competing on being cheap without being the cheapest.
  why: >-
    There is no strategic advantage to being the second lowest price in a marketplace, but there is for being the highest.
  anchor: >-
    This quote by Dan Kennedy captures the sentiment well: “There’s no strategic advantage
  source: >-
    playbook-price-raise.md, Why Raising Prices Is A Good Idea, lines 142-143
  confirmations: 1
  authors_caveat: >-
    Attributed by the author to Dan Kennedy.
  anchor_at: "playbook-price-raise.md:142"
- id: D-playbooks-price-043
  type: antipattern
  name: >-
    The vicious price cycle
  statement: >-
    Decreasing prices, which most businesses do, starts a cycle: client emotional investment, perceived value and results all decrease, clients become more demanding, and they get less service because there is less money to spend on them.
  why: >-
    On the business side profit per customer, perceived self-value, the ability to create results, conviction in the sales process and gratitude for customers all decrease; the cheapest customers ask for the most.
  anchor: >-
    Here’s how the **vicious price cycle** works (which MOST businesses use).
  source: >-
    playbook-price-raise.md, Why Raising Prices Is A Good Idea, lines 155-170
  confirmations: 1
  anchor_at: "playbook-price-raise.md:155"
- id: D-playbooks-price-044
  type: antipattern
  name: >-
    Don’t grandfather existing customers . Don’t do lifetime deals .
  statement: >-
    Locking existing customers into a price, by grandfathering them or by a lifetime deal.
  why: >-
    Value depends on price, so if value goes up the price should too; you never know what you will want to do or deliver in the future and locking a price limits your options.
  anchor: >-
    price. If your value goes up, so should your price. Never lock your customers into a price if
  source: >-
    playbook-price-raise.md, My Rules For Raising Prices, lines 211-214
  confirmations: 1
  anchor_at: "playbook-price-raise.md:212"
- id: D-playbooks-price-045
  type: antipattern
  name: >-
    Never sell a “one time price” for lifetime access
  statement: >-
    Selling lifetime access for a one time price, unless fulfilment truly costs you zero dollars.
  why: >-
    Forever lasts a lot longer than what they paid once; you end up with upset customers when the money runs out and the commitment remains, and every owner who started this way ends up fixing it.
  boundary: >-
    Unless it truly costs you zero dollars to fulfill.
  anchor: >-
    Never sell a “one time price” for lifetime access . Unless it truly costs you zero dollars
  source: >-
    playbook-price-raise.md, My Rules For Raising Prices, lines 215-222
  confirmations: 1
  authors_caveat: >-
    Theoretically it works if LTV on lifetime access exceeds what you normally make, but no large company offers lifetime access for a one time payment; model success not failure.
  anchor_at: "playbook-price-raise.md:215"
- id: D-playbooks-price-046
  type: antipattern
  name: >-
    Resenting early adopters
  statement: >-
    Resenting early adopters for paying early adoption prices instead of raising the price as the product and brand improve.
  why: >-
    Being insecure and cheap at the beginning is fine because you probably suck for now; hating your own customers over it is bad for them and for you.
  anchor: >-
    early adopters paying early adoption prices. Don’t be the entrepreneur who hates their cus-
  source: >-
    playbook-price-raise.md, My Rules For Raising Prices, lines 223-226
  confirmations: 1
  anchor_at: "playbook-price-raise.md:225"
- id: D-playbooks-price-047
  type: rule
  name: >-
    Meet with people if you raise prices more than 50%
  statement: >-
    A price raise above 50% is delivered by talking to customers individually, on top of everything else in the letter procedure.
  why: >-
    A raise that large usually happens because of a big mistake made early on, so it needs a conversation rather than only an announcement.
  boundary: >-
    Above 50%, and only where you can manage the call volume.
  anchor: >-
    Meet with people if you raise prices more than 50% . If you raise prices *a lot* - which
  source: >-
    playbook-price-raise.md, My Rules For Raising Prices, lines 243-245
  confirmations: 2
  anchor_at: "playbook-price-raise.md:243"
- id: D-playbooks-price-048
  type: antipattern
  name: >-
    A price that does not scale with the cost to fulfil
  statement: >-
    Charging a flat low price where the cost to fulfil grows with the customer's success.
  why: >-
    In the Shopify competitor case the more sales their customers made the more it cost to fulfil, so their biggest customers lost them the most money; the choice was to fire them or raise prices, and a raise from $30 to $3000 lost exactly one of 300.
  anchor: >-
    more sales their customers made the more it cost to fulfill for them.  This means their biggest
  source: >-
    playbook-price-raise.md, My Rules For Raising Prices, Fear not, lines 246-253
  confirmations: 1
  anchor_at: "playbook-price-raise.md:249"
- id: D-playbooks-price-049
  type: rule
  name: >-
    Do the math before you raise
  statement: >-
    Before raising prices you must know what percentage of customers you can lose and still make money.
  why: >-
    With that number, and with the price already tested on new customers, you make more money eventually no matter what.
  boundary: >-
    A precondition of the raise, not a step after it.
  anchor: >-
    Do  the  math.  You  should  know  what  percentage  of  customers  you  can  lose  and  still
  source: >-
    playbook-price-raise.md, My Rules For Raising Prices, lines 258-260
  confirmations: 1
  anchor_at: "playbook-price-raise.md:258"
- id: D-playbooks-price-050
  type: antipattern
  name: >-
    Getting greedy with a 10x price
  statement: >-
    Assuming the gain from doubling the price scales, so that 10x-ing the price multiplies profit accordingly.
  why: >-
    In the table a 10x price cut conversion 60% and tripled churn; LTV rose 3x but not enough to cover the lost conversion, so the $100 price made less than the $20 price.
  applies_when: >-
    The author's next move is to test prices between the two that worked, $39 to $59 in that example.
  anchor: >-
    Now, let’s say we get greedy and think “If doubling raised my profits by 80%...10x’ing
  source: >-
    playbook-price-raise.md, How To Pick Your Price, lines 295-307
  confirmations: 1
  anchor_at: "playbook-price-raise.md:295"
- id: D-playbooks-price-051
  type: rule
  name: >-
    Conversion and churn suffer, but not proportionally
  statement: >-
    A price rise hurts both conversion rate and churn rate, but not always in proportion to the rise, which is why each price has to be tested rather than derived.
  why: >-
    You may lose some, but often not as much as you gain; that non-proportionality is the whole point of the exercise.
  boundary: >-
    The relationship is not linear, so no price can be predicted from another without a test.
  anchor: >-
    version rate and churn rate, which both suffer as prices go up, but not always proportionally.
  source: >-
    playbook-price-raise.md, How To Pick Your Price, lines 316-321
  confirmations: 1
  anchor_at: "playbook-price-raise.md:317"
- id: D-playbooks-price-052
  type: antipattern
  name: >-
    Saying things you are not going to do
  statement: >-
    Listing investments in the price raise letter that you do not intend to make.
  why: >-
    That is lying; every investment named has to be one you were already going to make, framed as value for the customer.
  applies_when: >-
    Section I of the RAISE letter, whose concise template the author built with Patrick Campbell of Profitwell.
  anchor: >-
    Note: 1) Don’t say things you’re not going to do (that’s lying) 2) Frame all investments
  source: >-
    playbook-price-raise.md, The Perfect Price Raise Letter, Section #3 - I: Invest in their future, lines 387-389
  confirmations: 2
  anchor_at: "playbook-price-raise.md:387"
- id: D-playbooks-price-053
  type: antipattern
  name: >-
    Adding expenses to justify the raise
  statement: >-
    Deciding to incur expenses you had not planned in order to justify the price increase.
  why: >-
    It negates the benefit of the price raise to begin with - the extra profit you would have got.
  applies_when: >-
    Section I of the RAISE letter, whose concise template the author built with Patrick Campbell of Profitwell.
  anchor: >-
    you make as value for them 3) Don’t decide to add expenses you didn’t plan on incurring -
  source: >-
    playbook-price-raise.md, The Perfect Price Raise Letter, Section #3 - I: Invest in their future, lines 387-389
  confirmations: 2
  anchor_at: "playbook-price-raise.md:388"
- id: D-playbooks-price-054
  type: antipattern
  name: >-
    “It’s not scalable” talk
  statement: >-
    Answering customer concerns about the price raise with scalability arguments instead of replying personally.
  why: >-
    The point of the section is to take their concerns seriously and personally; fewer will reply negatively than you think because of the PS statement.
  applies_when: >-
    Section E of the RAISE letter, whose concise template the author built with Patrick Campbell of Profitwell.
  anchor: >-
    is not the time for “it’s not scalable” talk. Get ready to roll your sleeves up and respond to
  source: >-
    playbook-price-raise.md, The Perfect Price Raise Letter, Section #5 - E: Explain away their concerns, lines 425-431
  confirmations: 1
  anchor_at: "playbook-price-raise.md:427"
- id: D-playbooks-price-055
  type: rule
  name: >-
    Type #3: People who were gonna cancel anyways
  statement: >-
    The churn spike in the first month after a price raise is pulled-forward churn, not lost customers: month two churns below normal and month three returns to baseline.
  why: >-
    People who were going to cancel or not buy next month simply decide to do it a month sooner, so you only miss one month of revenue from that slice.
  boundary: >-
    Read the first-month spike against months two and three before treating a raise as failed.
  anchor: >-
    Type #3: People who were gonna cancel anyways. You will get an increase in churn
  source: >-
    playbook-price-raise.md, The Perfect Price Raise Letter, Section #5 - E, lines 438-455
  confirmations: 1
  anchor_at: "playbook-price-raise.md:444"
- id: D-playbooks-price-056
  type: antipattern
  name: >-
    Leaving comments open on the announcement
  statement: >-
    Announcing the price raise in a community and leaving the comments open.
  why: >-
    You do not want a fight in the comments; concerns are referred to you directly through the PS statement instead.
  applies_when: >-
    When the members congregate in a community and the announcement is made as a video, as Trey did.
  anchor: >-
    ments, do so. You don’t want a b*tch fest in the comments. This is why we refer them to talk
  source: >-
    playbook-price-raise.md, What to Do Next, lines 503-506
  confirmations: 1
  anchor_at: "playbook-price-raise.md:505"
- id: D-playbooks-price-057
  type: rule
  name: >-
    New customers pay the new price immediately
  statement: >-
    The loyalty discount and the staged increase are for existing customers only; incoming customers go to the new price immediately.
  why: >-
    New customers have no context, so there is no point in delaying; the sales answer to a complaint is that the value keeps improving and this is the cheapest it will ever be.
  boundary: >-
    The softening part of the procedure does not apply to new customers.
  anchor: >-
    To be clear, get new customers up to the new price immediately. No point in delaying
  source: >-
    playbook-price-raise.md, What To Do About Incoming Customers, lines 507-519
  confirmations: 1
  anchor_at: "playbook-price-raise.md:508"
- id: D-playbooks-price-058
  type: antipattern
  name: >-
    Reading complaints as lost sales
  statement: >-
    Treating customer grumbling about the new price as proof that they will not buy.
  why: >-
    People moan, but they still buy; wanting something for less does not mean they will not buy it for more.
  anchor: >-
    ter time to get started.” People moan, but they still buy. Just because someone wants something
  source: >-
    playbook-price-raise.md, What To Do About Incoming Customers, lines 516-519
  confirmations: 1
  anchor_at: "playbook-price-raise.md:518"
- id: D-playbooks-price-059
  type: rule
  name: >-
    The letter does not need to be perfect
  statement: >-
    A price raise letter that only covers the main points still works; the author's own longer gym letter worked for hundreds of gyms although he prefers the shorter template.
  why: >-
    Cover the main points, be bold, and follow the rules of raising prices; the profit comes from sending it, not from polishing it.
  boundary: >-
    Perfection is not a precondition for sending the letter.
  anchor: >-
    don’t need to be perfect. This letter worked just fine for hundreds of gyms.
  source: >-
    playbook-price-raise.md, My Gym Price Increase Letter, lines 638-641
  confirmations: 1
  anchor_at: "playbook-price-raise.md:639"
- id: D-playbooks-price-060
  type: antipattern
  name: >-
    Letting competitors grind your price down
  statement: >-
    Allowing competitors to slowly grind your price down until you cannot offer any more for any less.
  why: >-
    Doing it wrong or never changing prices brings in the wrong customers, erodes profits, stops reinvestment, and loses the best talent to competitors who can pay more.
  anchor: >-
    Lose the best talent to competitors who can pay more
  source: >-
    playbook-price-raise.md, Why You Should Actually Do This, lines 650-668
  confirmations: 2
  anchor_at: "playbook-price-raise.md:668"
- id: D-playbooks-price-061
  type: antipattern
  name: >-
    Building the back end you are passionate about
  statement: >-
    Choosing the next product by what the founders have a passion for rather than by the customer's next problem.
  why: >-
    A product far from the core is a marketing, branding and sales nightmare - you may as well have started another business; customers who like your stuff want to buy more stuff like it, and the survey of the base chose the near offer by a wide margin.
  applies_when: >-
    The author's test when the team cannot agree: offer both to the customers and let them choose.
  anchor: >-
    I firmly opposed it because it didn’t solve our customers’ next problem. If customers like your
  source: >-
    playbook-lifetime-value.md, Increasing Lifetime Value: The Crazy 8, lines 78-105
  confirmations: 2
  anchor_at: "playbook-lifetime-value.md:81"
- id: D-playbooks-price-062
  type: rule
  name: >-
    Disclaimer on average customer transactions
  statement: >-
    The average number of transactions per customer is always an estimate, and it rises as the business gets older because old customers keep buying.
  why: >-
    Customers come, leave and come back all the time, so no single figure is stable.
  boundary: >-
    Treat every LTV built on lifetime transactions as an estimate, and check the CRM figure against a back-of-napkin one.
  anchor: >-
    customers come, leave, and come back, all the time. As such, lifetime transactions always
  source: >-
    playbook-lifetime-value.md, How To Calculate LTV, Step Two, lines 185-188
  confirmations: 1
  anchor_at: "playbook-lifetime-value.md:186"
- id: D-playbooks-price-063
  type: antipattern
  name: >-
    Counting new signups into churn
  statement: >-
    Letting new customers signed up during the period change the churn figure.
  why: >-
    Churn is the share of the original cohort that left; you could sign up zero or 1,000 new clients in the month and still have lost five of the original hundred, so churn is still five percent.
  anchor: >-
    time period, it does not affect churn. The same number of original people left. You could
  source: >-
    playbook-lifetime-value.md, How To Calculate LTV, Step Two, lines 204-207
  confirmations: 1
  anchor_at: "playbook-lifetime-value.md:205"
- id: D-playbooks-price-064
  type: rule
  name: >-
    Pro Tip: Start Low Then Go Up
  statement: >-
    Before the offer has proven that people want it, start at a low price and only nudge it up once things are humming - about 20% every ten sales until sales drop dramatically, then back to the sweet spot.
  why: >-
    You need sales to confirm people actually want the thing and to run some water through the pipes to see where the leaks are.
  boundary: >-
    The exception to raise-the-price-first: it applies at the start of an untested offer.
  anchor: >-
    You need to make sales to make sure people actually want your thing. It also
  source: >-
    playbook-lifetime-value.md, The Crazy Eight, #1 Increase Prices, Pro Tip: Start Low Then Go Up., lines 280-285
  confirmations: 1
  anchor_at: "playbook-lifetime-value.md:281"
- id: D-playbooks-price-065
  type: antipattern
  name: >-
    Not testing price at all
  statement: >-
    Avoiding price tests because testing costs money.
  why: >-
    Testing price is expensive for a few months, but the only thing more expensive is not testing at all and having a business that is under-monetized for life; a mispriced sale can be fixed with extra bonuses or by refunding the difference.
  anchor: >-
    a few months. But the only thing more expensive is not testing price at all and
  source: >-
    playbook-lifetime-value.md, The Crazy Eight, #1 Increase Prices, Pro Tip: Start Low Then Go Up., lines 286-290
  confirmations: 1
  anchor_at: "playbook-lifetime-value.md:289"
- id: D-playbooks-price-066
  type: rule
  name: >-
    Costs can only go down to zero
  statement: >-
    Cutting the cost to deliver raises gross profit, but unlike price, which can go infinitely high, costs can only go down to zero.
  why: >-
    The cost of getting a customer can only hit zero, while how much money you make from each customer can go infinitely high, which is why pricing comes first among the crazy eight.
  boundary: >-
    The ceiling on the cost lever; it cannot substitute for the price lever.
  anchor: >-
    pricing where you can go infinitely high, with costs, you can only go down to zero. But, the
  source: >-
    playbook-lifetime-value.md, The Crazy Eight, #2 Decrease Costs, lines 295-298
  confirmations: 2
  anchor_at: "playbook-lifetime-value.md:297"
- id: D-playbooks-price-067
  type: antipattern
  name: >-
    A cross-sell that breaks the business
  statement: >-
    Adding a cross-sell that dramatically changes who you serve or what you do every day.
  why: >-
    You do not want to break your business to pick up some extra change; the cross-sell should be the easiest thing to add seamlessly with your existing infrastructure, resources and expertise.
  anchor: >-
    Note: you don’t wanna break your business to pick up some extra change. You want it to
  source: >-
    playbook-lifetime-value.md, The Crazy Eight, #4 Cross-Sell Something Different, Action Step, lines 414-418
  confirmations: 1
  anchor_at: "playbook-lifetime-value.md:416"
- id: D-playbooks-price-068
  type: antipattern
  name: >-
    Selling a downsell to a qualified buyer
  statement: >-
    Offering the downsell to someone who would have bought the main offer.
  why: >-
    You lose money when people who would have bought the $5 thing take the $2.50 thing; the author forbids his sales team from selling a qualified person a downsell, which keeps the main offer from being cannibalized while still collecting the extra cash.
  applies_when: >-
    Downsells, of quantity or of quality, go only to customers who do not qualify for the main offer.
  anchor: >-
    on downsells when people who would’ve bought the $5 thing now opt for the $2.50 thing.
  source: >-
    playbook-lifetime-value.md, The Crazy Eight, #7 Downsell Fewer (Lower Quantity), lines 504-510
  confirmations: 3
  anchor_at: "playbook-lifetime-value.md:506"
- id: D-playbooks-price-069
  type: antipattern
  name: >-
    Waiting for inspiration for an upsell
  statement: >-
    Waiting for a moment of inspiration to produce the next upsell instead of working through the crazy eight and writing down the action steps.
  why: >-
    The author's highest converting upsells have rarely come from moments of inspiration; they come from getting into the zone and following a process he knows works.
  anchor: >-
    steps. My highest converting upsells have rarely come from moments of inspiration. They
  source: >-
    playbook-lifetime-value.md, Putting It All Together, lines 568-570
  confirmations: 1
  anchor_at: "playbook-lifetime-value.md:569"
```
