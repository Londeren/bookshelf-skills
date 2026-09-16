# Улов фазы 1 — $100M Playbooks: Pricing, Price Raise, Lifetime Value (2025) (ярус 2), тип A: фреймворки

Группа `tier2-playbooks-price`, слаг `playbooks-price`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **32** (экстрактор вернул 32, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `playbook-pricing.md` | 1–1381 | 2 | 14 |
| `playbook-price-raise.md` | 1–758 | 2 | 7 |
| `playbook-lifetime-value.md` | 1–613 | 1 | 11 |

## Как собран файл

Экстрактор A (Frameworks) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-playbooks-price.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-playbooks-price-A.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: A-playbooks-price-001
  type: framework
  name: >-
    The genie's three options (2x customers, 2x purchases, 2x price)
  statement: >-
    Before choosing where to put effort, compare the three ways to double a business - double new customers, double the number of purchases, or double the price - by their effect on profit, not on revenue: on the same stats the first two give 3.5x profit and doubling price gives 6x.
  why: >-
    All three double hypothetical max revenue, but doubling price adds no cost to acquire and no cost to deliver, so the whole increase drops to the bottom line, while the other two bring twice the delivery load.
  applies_when: >-
    Deciding which lever of the business to work on first.
  structure:
    - >-
      Option #1: 2x # of new customers x 1x price x 1x # of purchases = 3 .5x PROFIT
    - >-
      Option #2: 1x # of new customers x 1x price x 2x # of purchases = 3 .5x PROFIT
    - >-
      Option #3: 1x # of new customers x 2x price x 1x # of purchases = 6x PROFIT
  anchor: >-
    Since we know the first option 3.5x our profit, the second option 3.5x our profit, and
  source: >-
    playbook-pricing.md, Pricing To Make The Most Money, lines 126–309
  confirmations: 1
  authors_caveat: >-
    The walkthrough is run on one set of stats (30 new clients/mo, 33% churn, $100/mo, 20% net margins) and only advertising and delivery costs are counted: To simplify stuff, I have only included costs of advertising and delivering.
  anchor_at: "playbook-pricing.md:305"
- id: A-playbooks-price-002
  type: framework
  name: >-
    Here Are The Three Big Pricing Models
  statement: >-
    A price is set by one of three models - cost plus, competitor based, or value based - and value based pricing, set on what a customer is willing to pay, is the one to use.
  why: >-
    Costs change and customers have no idea what it costs you; competitor based pricing is built on someone else's business and customers; value based pricing lets you charge 2,3,4,5 x market rates and keep raising prices as you keep adding value.
  applies_when: >-
    Setting or resetting the price of a product or service.
  structure:
    - >-
      1) Cost Plus Pricing: whatever your costs are plus an arbitrarily added margin
    - >-
      2) Competitor Based Pricing: whatever the average of what everyone else is charging
    - >-
      3) value Based Pricing
  anchor: >-
    We’ve got: 1) cost plus pricing, 2) competitor based pricing, and 3) value based pricing.
  source: >-
    playbook-pricing.md, Three Models Of Pricing, lines 336–377
  confirmations: 1
  authors_caveat: >-
    Value based pricing focuses less on getting the most customers and more on value per customer: it takes more of a different type of work than most people are used to.
  anchor_at: "playbook-pricing.md:340"
- id: A-playbooks-price-003
  type: framework
  name: >-
    Three Metrics To Determine value-Driven Pricing
  statement: >-
    To find the price that makes the most money, test price points and record for each one conversion rate, churn and lifetime value in one table, then pick the row with the highest total return.
  why: >-
    When you increase the price for non-luxury goods, people buy less often and repurchase less often, so a price can only be judged on total lifetime gross profit rather than on conversion alone.
  applies_when: >-
    Adjusting a price, and before rolling a raise out to the whole base.
  structure:
    - >-
      1) How many people buy at the current price (Aka - Conversion rate)
    - >-
      2) How many times they buy, or how long they stay at the current price ( Aka - Churn)
    - >-
      PriceClicksConv RateSalesChurnLT VTotal ReturnDifference
  anchor: >-
    one that makes you the most money (not gets you the most customers). I make a little table like
  source: >-
    playbook-pricing.md, Three Metrics To Determine value-Driven Pricing, lines 378–397
  confirmations: 1
  authors_caveat: >-
    The section is headed Three Metrics but only two are listed in the text; price itself appears only as the first column of the table. The same table with the same $10/$20/$100 rows recurs in playbook-price-raise.md lines 267–300 (How To Pick Your Price), which the build map counts as one place, not two.
  anchor_at: "playbook-pricing.md:385"
- id: A-playbooks-price-004
  type: framework
  name: >-
    The *Instant Profit* Pricing Playbook
  statement: >-
    Ten pricing plays that raise revenue with minimal or no change in conversion; stacked they add 26.8% to 63.8% to revenue, and one of them is enough to make more money immediately.
  why: >-
    The average small business in the U.S. in 2024 runs 7-10% net profit margins, so a 26.8%-63.8% revenue increase from pricing can multiply profit several times over; the plays were picked because they are designed to affect sales minimally (if at all).
  applies_when: >-
    Looking for profit that can be added overnight without a major change in operations.
  structure:
    - >-
      Pricing Play #1: Monthly to 28 Day Billing Cycles (8.3%)
    - >-
      Pricing Play #2: Processing Fees & Second Form of Payment (3-4%)
    - >-
      Pricing Play #3: Sales Tax (0% - 10%)
    - >-
      Pricing Play #4: Annual Price Increases / Annual CPI Increase (3% - 10%)
    - >-
      Pricing Play #5: Annual Billing / Longer Duration Billing Options (10-15%)
    - >-
      Pricing Play #6: Round Up (1-3%)
    - >-
      Pricing Play #7: Annual Renewal Fee On Top Of Monthly (10%)
    - >-
      Pricing Play #8: Automatic Continuity / Continued Access (10%)
    - >-
      Pricing Play #9: Ultra High Ticket Anchor / Ultra High Option (10-15%)
    - >-
      Pricing Play #10: Guarantee and Warranty Upsells / Priced Guarantee or Warranty (5 - 20%)
  anchor: >-
    I picked these instant profit hacks because they take so little effort and they can instantly
  source: >-
    playbook-pricing.md, The *Instant Profit* Pricing Playbook, lines 1350–1374; the same index at lines 550–575
  confirmations: 2
  authors_caveat: >-
    There  are  other  pricing  strategies  that  create  bigger  swings,  but  they  require more work/change/risk, so they were excluded; some plays will not be a direct fit for a given business.
  anchor_at: "playbook-pricing.md:1351"
- id: A-playbooks-price-005
  type: framework
  name: >-
    Pricing Play #1: Monthly to 28 Day Billing Cycles
  statement: >-
    Switch subscription billing from monthly to every 28 days, which turns 12 billing cycles a year into 13 and adds an instant and permanent 8.3% to revenue at the same conversion rate.
  why: >-
    The extra cycle is pure profit and people convert at the same rates; on a 20% net margin business it takes margins from 20% to 26.1% and net profit up 41.5%.
  applies_when: >-
    Any subscription or membership billed monthly.
  structure:
    - >-
      1) Change contracts for new customers immediately
    - >-
      2) Set a date to change for everyone else
    - >-
      3) Be upfront - call it a price increase if needed
    - >-
      4) Explain it as reinvestment in your business
  anchor: >-
    Monthly billing gives you 12 cycles a year. Weekly (or every 28 days) gives you 13. That
  source: >-
    playbook-pricing.md, Pricing Play #1: Monthly to 28 Day Billing Cycles, lines 578–613
  confirmations: 1
  authors_caveat: >-
    Weekly and bi-weekly billing yield the same benefit in theory but caused a lot of billing hassles because people wanted short pauses; stick with 4 weeks, 12 weeks, or longer, and display the price weekly while billing every four weeks.
  anchor_at: "playbook-pricing.md:586"
- id: A-playbooks-price-006
  type: framework
  name: >-
    Pricing Play #2: Processing Fees & Second Form of Payment
  statement: >-
    After the customer agrees to the price, add a card processing fee of about 3.99%, and if they hesitate, offer to waive it in exchange for a second form of payment.
  why: >-
    Either branch pays: the fee adds 3-4% of revenue for no extra work, and a second card removes the 1.2%-1.7% monthly involuntary churn from card info changes, which can be 24-34% of total churn at 5% monthly churn, lifting LTV by 31-51%.
  applies_when: >-
    Any sale taken by card, especially recurring billing.
  structure:
    - >-
      1) After the customer agrees to the price, ask, “How did you want to pay?”
    - >-
      2) Then say, “Great, it’s just a 3.99% card processing fee.”
    - >-
      If they hesitate, offer an alternative: you can save the 3.99% by providing a second form of payment
    - >-
      Change  your  scripting.  Accept  a  second  form  of  payment.  Have  them  authorize  both forms of payment. Re-run all failed transactions the next day on the new card.
  anchor: >-
    1) After the customer agrees to the price, ask, “How did you want to pay?”
  source: >-
    playbook-pricing.md, Pricing Play #2: Processing Fees & Second Form of Payment, lines 617–677
  confirmations: 1
  anchor_at: "playbook-pricing.md:630"
- id: A-playbooks-price-007
  type: framework
  name: >-
    Pricing Play #3: Sales Tax
  statement: >-
    Charge sales tax on top of the agreed price instead of absorbing it, adding it as a separate line item on the invoice with a matter-of-fact reference to the tax code.
  why: >-
    Sales tax comes off the top line, so paying it for customers with 20% margins and 5% sales tax gives away 25% of profit; customers are not offended by tax at a restaurant checkout either.
  applies_when: >-
    Your state or country does charge sales tax specifically for your thing.
  structure:
    - >-
      1) Get agreement on the price
    - >-
      2) Then send invoice or at point of sale put the script below ON THE INvOICE:
    - >-
      “State tax code [1030a.o] mandates that personal services are subject to 6% sales tax.” - keep it dry and matter of fact
    - >-
      3) Put the tax as a separate line item before the total
    - >-
      4) Get in the angry boat with them...If they balk, get more angry about it than them.
  anchor: >-
    Taxes are a huge cost in business, and sales tax comes off the top line. If you’re simply
  source: >-
    playbook-pricing.md, Pricing Play #3: Sales Tax, lines 681–735
  confirmations: 1
  authors_caveat: >-
    To be clear, if you do not get charged taxes, you cannot charge them; the alternative given is to incorporate in a state that doesn't charge sales tax, checking with lawyers first.
  anchor_at: "playbook-pricing.md:690"
- id: A-playbooks-price-008
  type: framework
  name: >-
    Pricing Play #4: Annual Price Increases
  statement: >-
    Write a fixed annual price increase of 5 to 15 percent into new contracts so prices rise every year by right rather than by negotiation.
  why: >-
    Costs of doing business and inflation go up either way, so a price left alone erodes margins - $100 in 2024 was $79 in 2017 - and companies that continually optimize and test pricing make way more money than companies that don't.
  applies_when: >-
    Any contract signed with a new customer.
  structure:
    - >-
      Pick a reasonable percentage 5 to 15 percent is a good place to start.
    - >-
      Simply add it to new contracts and customers.
    - >-
      Scripting for the sales team: we keep our prices standard with the CPI, so we don't have any incentive to cut on the quality of what you get
    - >-
      Note: You don’t mention this during the sale, you can bring it up when you’re filling out paperwork.
  anchor: >-
    Pick a reasonable percentage 5 to 15 percent is a good place to start. Simply add it to
  source: >-
    playbook-pricing.md, Pricing Play #4: Annual Price Increases, lines 739–810
  confirmations: 1
  authors_caveat: >-
    Few people will balk if you keep it under 15%.
  anchor_at: "playbook-pricing.md:802"
- id: A-playbooks-price-009
  type: framework
  name: >-
    Pricing Play #5: Annual Billing
  statement: >-
    Offer longer-duration billing options and sell them as a descending ladder: full annual price first, then a prepaid annual discount, then a prepaid quarter, then standard monthly.
  why: >-
    Churn is directly correlated with billing frequency (2% monthly churn at 1x per year against 10.7% at 12x per year, a 5.35x gain in LTV), and the first number out of your mouth anchors the entire conversation, so the cheaper prepayment reads as a benefit rather than monthly reading as a penalty.
  applies_when: >-
    Any recurring offer; the play risks nothing since you can always revert back to your standard pricing.
  structure:
    - >-
      1) Add it to your pricing options
    - >-
      2) Offer the full price $1200 first (assuming the length of term)
    - >-
      3) Then ask if they’d like to receive a discount
    - >-
      4) If they say yes, you offer the prepaid discount of 17% off
    - >-
      5) If they say no, you could offer a prepaid discount of 8% if they prepay the quarter.
    - >-
      6) If they still say no, yo offer the standard monthly with no discount.
  anchor: >-
    You can 5x your LTV by simply getting customers to pay annually.
  source: >-
    playbook-pricing.md, Pricing Play #5: Annual Billing, lines 814–889
  confirmations: 1
  authors_caveat: >-
    Requiring annual only drops conversions because the price is 12x the monthly rate, and whether it drops them 5x is untested: I don’t know. You’d have to test it for you. A stated workaround is to sell six to twelve weeks first and upsell the prepaid year after trust is built. Benchmarks: with a 16% annual discount on a sales page 10-15% select annual, 30% if it is the default, 35-40% over the phone.
  anchor_at: "playbook-pricing.md:833"
- id: A-playbooks-price-010
  type: framework
  name: >-
    Pricing Play #6: Round Up
  statement: >-
    Nudge every price upward to the nearest 9: change 7s to 9s and add .99 to all fees, on new contracts immediately.
  why: >-
    In the author's gyms the change added $104 to $155.48 per client per year - 4.25% to 11.1% price increases - with no change in conversion, on a business type that runs 12.5% net margins.
  applies_when: >-
    Premium and ordinary goods, where price reflects the value of the product itself.
  structure:
    - >-
      Change 7s to 9s.
    - >-
      Add .99 to all fees.
    - >-
      Change contracts for new customers immediately.
  anchor: >-
    Change 7s to 9s. Add .99 to all fees. This takes so little time, and the only thing easier
  source: >-
    playbook-pricing.md, Pricing Play #6: Round Up, lines 893–964
  confirmations: 1
  authors_caveat: >-
    Pro Tip: When NOT To Add .99 or change 7s to 9s - luxury items often end on a round number, because people who buy luxury goods want not to get a deal; premium does not mean luxury, and the author still says to test it.
  anchor_at: "playbook-pricing.md:958"
- id: A-playbooks-price-011
  type: framework
  name: >-
    Pricing Play #7: Annual Renewal Fee On Top of Monthly
  statement: >-
    Keep the advertised monthly rate and add a once-a-year renewal fee of 1-3x the monthly rate on the anniversary of the contract, with a benefit-framed reason why.
  why: >-
    People focus on the monthly price but rarely consider the annualized cost, so $39 x 12 plus a $99 annual fee is an effective $47/mo and a 20% revenue lift with the low advertised price intact.
  applies_when: >-
    Markets too price conscious to bill annually outright.
  structure:
    - >-
      Step #1: Pick a renewal fee that’s 1-3x your monthly rate.
    - >-
      Step #2: Add a beneficial “reason why.” - “You pay this for rate protection. If you don’t agree to the fee, you’ll be subject to any price changes we make.”
    - >-
      Step #3: Add to contracts and have them initial next to it. Both the rate, and the annual renewal fee.
  anchor: >-
    Step #1: Pick a renewal fee that’s 1-3x your monthly rate. This adds a big increase to
  source: >-
    playbook-pricing.md, Pricing Play #7: Annual Renewal Fee On Top of Monthly, lines 968–1037
  confirmations: 1
  authors_caveat: >-
    If you can bill annually, by all means do it; this play is for markets where you can't. If they balk at the fee you just drop it, and they don't get the benefit. Pro Tip: have both a setup fee and a renewal fee so you can waive one to get the other.
  anchor_at: "playbook-pricing.md:1014"
- id: A-playbooks-price-012
  type: framework
  name: >-
    Pricing Play #8: Automatic Continuity
  statement: >-
    Bolt a stripped-down, high-margin version of what you sell onto the back of every front-end purchase at 5-20% of the main price, agreed upfront and recurring automatically when the front-end term ends.
  why: >-
    Against the main purchase the price seems small and people suffer from sunk cost fallacy - they already spent x, they might as well pay 5-10% to keep it - which on the worked example adds 32% to LTV and $1800 of profit per customer, and builds a pool of low-ticket customers to sell to later.
  applies_when: >-
    Any front-end product or service, including businesses that only have one time transactions - fix a time on the back end and start the continuity after that period.
  structure:
    - >-
      Step#1 : Pull up every product and service you sell on the front end
    - >-
      Step#2 : Find the features(s) that have value but don’t cost much to deliver on from each service
    - >-
      Step#3 : Pick a price 5-20% of your normal price
    - >-
      Step#4 : Bolt it onto every front end purchase and say they only earn that rate after they’ve gone thru x time
    - >-
      Step#5 : Collect a very high profit source in the meantime and remarket to those people to sell them more stuff over time
  anchor: >-
    Whatever you sell, you create the most paired down, zero work version of your thing.
  source: >-
    playbook-pricing.md, Pricing Play #8: Automatic Continuity, lines 1041–1129
  confirmations: 1
  authors_caveat: >-
    Pro Tip: Don’t Be A Sneak - this isn’t ‘undisclosed’ or ‘forced’ continuity, it is continuity they must agree to up front, so be clear about what happens after X time period.
  anchor_at: "playbook-pricing.md:1056"
- id: A-playbooks-price-013
  type: framework
  name: >-
    Pricing Play #9: Ultra High Ticket Anchor
  statement: >-
    Add one product to the suite that is 10x or more expensive than the core offer and present it first, then move to the core offer for those who can't take it.
  why: >-
    The high price anchors the conversation, so the core offer looks more affordable and closes better, while the few who take the anchor lift LTV sharply - in the worked example from $440 to $890 per customer at a 10% take rate.
  applies_when: >-
    Any suite of products or services; the anchor must be something you are excited to deliver if someone buys it.
  structure:
    - >-
      Think of the most absurd version of your thing.
    - >-
      Think of the price you’d happily do it for.
    - >-
      Now, start offering that first.
    - >-
      And if they can’t, act like the tailor and find something better suited for them your main offer.
  anchor: >-
    add something to your suite of products or services that’s 10x or more expensive than
  source: >-
    playbook-pricing.md, Pricing Play #9: Ultra High Ticket Anchor, lines 1133–1184
  confirmations: 1
  authors_caveat: >-
    Make sure you are actually willing to do the thing you sell for a lot of money. And if you feel stressed when people buy it, keep raising the price until it makes you smile when they buy.
  anchor_at: "playbook-pricing.md:1143"
- id: A-playbooks-price-014
  type: framework
  name: >-
    Pricing Play #10: Guarantee and Warranty Upsells
  statement: >-
    After the customer has agreed to buy, sell a guarantee or warranty priced at 5-30% of the product price as a separate checkout upsell.
  why: >-
    You are buying and selling risk: if the guarantee revenue exceeds the cost of fixing the product, the upsell is nearly all profit with zero new operations, and it also lets you honour claims by replacing rather than refunding.
  applies_when: >-
    Any product or service, at any price point; it works especially well with ‘main street’ and ‘traditional’ businesses.
  structure:
    - >-
      You sell your thing.
    - >-
      Then, after the person agrees to buy, you offer a guarantee for 5-30% of the price of the product.
    - >-
      if you have high margins, you can make the price of the guarantee equal to your cost of goods so you literally never lose money
    - >-
      You  just  ask  after  they’ve  purchased  “You  just  want  the  standard  warranty  on  that?”
    - >-
      And if they reach out for an exchange, or to use their guarantee, you just check to see if they bought it.
  anchor: >-
    Here’s how the play works. You sell your thing. Then, after the person agrees to buy, you
  source: >-
    playbook-pricing.md, Pricing Play #10: Guarantee and Warranty Upsells, lines 1188–1291
  confirmations: 1
  authors_caveat: >-
    You  want  the  revenue  of  the  guarantee  to  exceed  the  cost  of  fixing  the  product - it comes down to knowing your numbers.
  anchor_at: "playbook-pricing.md:1203"
- id: A-playbooks-price-015
  type: framework
  name: >-
    The vicious price cycle
  statement: >-
    Cutting prices runs a self-reinforcing loop: emotional investment, perceived value and results fall while demandingness rises, and the business loses profit per customer, self-value, its ability to create results, conviction in the sales process and gratitude for customers.
  why: >-
    Lower price lowers the client's emotional investment and the perceived value, which lowers results, and the shrinking profit per customer leaves less money to spend on service, which lowers results again - a race to the bottom.
  applies_when: >-
    Deciding whether to compete on lower price.
  structure:
    - >-
      Your clients’ emotional investment DECREASES.
    - >-
      The perceived value of your service DECREASES.
    - >-
      Results DECREASE as a result of decreased investment and perceived value.
    - >-
      Clients  INCREASE  their  demandingness.
    - >-
      Clients get LESS service because you have less money to spend on them
    - >-
      DECREASES in profit per customer
    - >-
      DECREASES in perceived self-value*
    - >-
      DECREASES its ability to create results for customers
    - >-
      DECREASES your conviction in the sales process
    - >-
      DECREASES your gratitude for customers because you feel underappreciated
  anchor: >-
    Here’s how the **vicious price cycle** works (which MOST businesses use).
  source: >-
    playbook-price-raise.md, Why Raising Prices Is A Good Idea, lines 155–170
  confirmations: 1
  anchor_at: "playbook-price-raise.md:155"
- id: A-playbooks-price-016
  type: framework
  name: >-
    The virtuous price cycle
  statement: >-
    Raising prices runs the same loop in reverse: emotional investment, perceived value and results rise while demandingness falls, and the business gains profit per customer, self-value, ability to create results, level of service and conviction in the sales process.
  why: >-
    The extra money is what makes it worth the extra money: smart owners spend it on better advertising, constant product improvements and pampering customers, so clients get more service and better results.
  applies_when: >-
    Deciding whether to raise prices.
  structure:
    - >-
      Your clients’ emotional investment INCREASES.
    - >-
      The perceived value of your service INCREASES.
    - >-
      Results INCREASE as a result of increased investment and perceived value.
    - >-
      Your  clients  DECREASE  their  demandingness.
    - >-
      Your clients get MORE service because you have MORE money to spend on them
    - >-
      INCREASES in terms of profit per customer.
    - >-
      INCREASES in perceived self-value.
    - >-
      INCREASES its ability to create results for customers
    - >-
      INCREASES the level of service you render for each customer.
    - >-
      INCREASES your conviction in the sales process
  anchor: >-
    Here’s how the **virtuous price cycle** works (which is what raising prices does):
  source: >-
    playbook-price-raise.md, Why Raising Prices Is A Good Idea, lines 175–193
  confirmations: 1
  anchor_at: "playbook-price-raise.md:175"
- id: A-playbooks-price-017
  type: framework
  name: >-
    RAISE (The Perfect Price Raise Letter)
  statement: >-
    A price raise letter has five sections in this order: Remind them of the value they've gotten, Address the price change directly, Invest in their future, Soften the news with a loyalty discount, Explain away their concerns.
  why: >-
    The value reminder makes it about them, the direct statement rips off the bandaid while the rest of the letter softens the blow, the investments keep you from looking greedy, the vanishing discount is easier to accept than a raise, and the PS invitation to reply keeps objections out of public threads and off the churn line. The concise version was built with Patrick Campbell of Profitwell, who oversaw 100 price increases directly and analyzed over 500.
  applies_when: >-
    Raising prices on an existing customer base.
  structure:
    - >-
      R - Remind them of the value they’ve gotten.
    - >-
      A - Address the price change directly.
    - >-
      I - Invest in their future.
    - >-
      S - Soften the news with a loyalty discount
    - >-
      E - Explain away their concerns.
  anchor: >-
    My price raise letters have five sections. I use the acronym RAISE to remember it.
  source: >-
    playbook-price-raise.md, The Perfect Price Raise Letter, lines 331–459
  confirmations: 2
  authors_caveat: >-
    Section E is not scalable by design: Get ready to roll your sleeves up and respond to customers. If there is a community, post it as a video with comments turned off and refer questions to you directly.
  anchor_at: "playbook-price-raise.md:332"
- id: A-playbooks-price-018
  type: framework
  name: >-
    Investment categories paired with more good stuff / less bad stuff
  statement: >-
    In the Invest section of a price raise letter, name three investments drawn from the standing categories - people, training, equipment, technology, facility, level of service - and pair each one with more good stuff or less bad stuff for the customer.
  why: >-
    Framing the raise as investment rather than greed shows the customer better bang for their buck; the investments are things you were already going to do over the next 12 months, so they cost nothing extra.
  applies_when: >-
    Writing section I of the price raise letter.
  structure:
    - >-
      Hiring better people
    - >-
      Training the people you have
    - >-
      Better Equipment
    - >-
      Better Technology/Software
    - >-
      Facility Upgrades
    - >-
      Higher level of service
    - >-
      More good stuff: more aligned with their desired outcome, faster, easier, risk free.
    - >-
      Less bad stuff: misaligned with their desired outcome, slower, harder, riskier.
  anchor: >-
    You want to make this about investments. Basically just tell them the stuff you already
  source: >-
    playbook-price-raise.md, Section #3 - I: Invest in their future, lines 361–407
  confirmations: 2
  authors_caveat: >-
    Note: 1) Don’t say things you’re not going to do (that’s lying) 2) Frame all investments you make as value for them 3) Don’t decide to add expenses you didn’t plan on incurring - this negates the benefits of the price raise to begin with.
  anchor_at: "playbook-price-raise.md:373"
- id: A-playbooks-price-019
  type: framework
  name: >-
    Three types of people who answer a price raise
  statement: >-
    Replies to a price raise sort into three types - those who see the value, those actually affected, and those who were going to cancel anyway - and each gets its own handling.
  why: >-
    Type #2 gives you optionality: you can extend their discount another 6 months. Type #3 produces a spike in churn the first month, a dip below normal the month after and a return to baseline in month three, which indicates you simply pulled forward churn and lost only one month of revenue.
  applies_when: >-
    Reading the responses after a price raise letter goes out.
  structure:
    - >-
      Type #1: People who see the value.
    - >-
      Type #2: People actually affected.
    - >-
      Type #3: People who were gonna cancel anyways.
  anchor: >-
    You’ll find there are three types of people:
  source: >-
    playbook-price-raise.md, Section #5 - E: Explain away their concerns, lines 438–459
  confirmations: 1
  anchor_at: "playbook-price-raise.md:438"
- id: A-playbooks-price-020
  type: framework
  name: >-
    Two ways to roll out a big raise (all the way up, or stair step)
  statement: >-
    A large raise goes out either in one move or in one to three increments, positioned as a discount that falls off in stages rather than as a price that rises.
  why: >-
    People have an easier time handling disappearing discounts rather than raised prices, and the staged fall-off eases customers into the new price.
  applies_when: >-
    You have reservations because of how big a price raise you need.
  structure:
    - >-
      1) You can just go all the way up.
    - >-
      2) You can do it in one to three increments. You position the discount as a stair step up.
    - >-
      Some portion of it falls off every X months or quarters.
  anchor: >-
    2) You can do it in one to three increments. You position the discount as a stair step up.
  source: >-
    playbook-price-raise.md, What to Do Next, lines 494–502; Price Raise Checklist, lines 720–722
  confirmations: 2
  anchor_at: "playbook-price-raise.md:499"
- id: A-playbooks-price-021
  type: framework
  name: >-
    Price Raise Checklist
  statement: >-
    A price raise runs as a fixed sequence: decide the increase, test it on new customers, segment the old base, write the value bullets, state the raise, write three investment bullets and their benefit, give an expiring loyalty discount, promise a personal reply, sign in ink, close with the PS.
  why: >-
    Testing on new customers first proves the raise makes money and gives confidence when presenting it to the base; the expiring discount softens the blow; the PS statement gives them a way to voice concerns privately.
  applies_when: >-
    Executing a price raise on an existing base.
  structure:
    - >-
      Decide on price increase
    - >-
      Test with new customers first. If they buy and stay at rates that increase how much money you make, continue to the next step.
    - >-
      Segment out ‘old’ customers that came before the price raise.
    - >-
      Write out 1-5 bullets of current value
    - >-
      Tell them the price raise happens now
    - >-
      Write  out  3  bullets  of  the  biggest  investments  you’ll  make  with  the  profit  from  the price increase.
    - >-
      Explain how these investments benefit them.
    - >-
      Give them an expiring discount as a reward for being a loyal customer.
    - >-
      Tell them you respond personally if they have any issues.
    - >-
      Sign in ink if possible . If not, sign the email personally.
    - >-
      Finish with a strong PS statement telling them to reach out again if this is going to ruin their lives or business.
    - >-
      Do this individually if the price raise is 50% or more and you can manage the call volume.
    - >-
      Stair step discount: If the price raise is a lot, you can “stair step”
  anchor: >-
    have included a price raise checklist to make this easy for you. Well...easy to do. Maybe not
  source: >-
    playbook-price-raise.md, Price Raise Checklist, lines 700–722
  confirmations: 1
  anchor_at: "playbook-price-raise.md:671"
- id: A-playbooks-price-022
  type: framework
  name: >-
    My favorite upsell of all time
  statement: >-
    The default back-end offer is more of - or more help with - what the customer just bought, delivered with faster results, less risk, less effort and less hassle, for more money.
  why: >-
    If customers like your stuff, they want to buy more stuff like it; an offer far from the core product is a marketing, branding, and sales nightmare, and when the two were put to a customer survey the near offer won by a wide margin and went on to 2.2x LTV per customer.
  applies_when: >-
    Choosing what back end product to add to a business that is one and done.
  structure:
    - >-
      More of  - or more help with - what they just bought
    - >-
      faster results
    - >-
      less risk
    - >-
      less effort
    - >-
      less hassle
    - >-
      for more money
  anchor: >-
    or more help with - what they just bought... but with faster results, less risk, less
  source: >-
    playbook-lifetime-value.md, Increasing Lifetime Value: The Crazy 8, lines 114–118
  confirmations: 1
  anchor_at: "playbook-lifetime-value.md:116"
- id: A-playbooks-price-023
  type: framework
  name: >-
    How To Calculate LTV (Step One - Three)
  statement: >-
    Establish the LTV baseline in three steps: work out gross profit and gross profit percentage per thing you sell, then the average number of transactions per customer or the churn rate, then multiply gross profit by transactions for a transactional business or divide it by churn for a recurring one.
  why: >-
    LTV is the gross profit collected over the lifespan of a customer, and he who can make his customer more valuable than his competition wins, because the cost of getting a customer can only hit zero while how much you make from each can go infinitely high.
  applies_when: >-
    Before trying to increase LTV, to have a baseline number.
  structure:
    - >-
      Step One: Gross Profit . The first thing you have to figure out is your gross profit.
    - >-
      Step Two: Figure the average number of transactions a customer makes over their lifetime.
    - >-
      Step Three: If you have a product or transactional business, multiply the average gross profit  by  #  of  transactions.  Or,  if  you  have  a  recurring  business,  divide  gross  profit  by churn percentage.
    - >-
      Gross profit x average transactions per customer = LTGP
    - >-
      Gross profit / Churn = LTGP
  anchor: >-
    Step One: Gross Profit . The first thing you have to figure out is your gross profit. Gross
  source: >-
    playbook-lifetime-value.md, How To Calculate LTV, lines 154–226
  confirmations: 1
  authors_caveat: >-
    Figuring  out  average  customer  transactions  is  always  an  estimate  because customers come, leave, and come back; lifetime transactions always increase as a business gets older. Churn counts only the original cohort - new signups during the period do not affect it. LTV here is gross profit, sometimes called LTGP or CLV, not net profit.
  anchor_at: "playbook-lifetime-value.md:156"
- id: A-playbooks-price-024
  type: framework
  name: >-
    The two ways to make a customer more valuable (AOV and frequency)
  statement: >-
    The received frame says a customer can be made more valuable in only two ways - increase average order value, or increase the number of times they buy.
  why: >-
    Both are true, which is why the author keeps them as the roof over the eight levers.
  applies_when: >-
    Thinking about monetization at the highest level.
  structure:
    - >-
      you can increase average order value
    - >-
      or increase the number of times they buy
  anchor: >-
    valuable...you can increase average order value, or increase the number of times they buy.”
  source: >-
    playbook-lifetime-value.md, The Crazy Eight, lines 231–237
  confirmations: 1
  authors_caveat: >-
    The author quotes this frame only to reject it as unusable: And although those are both true, it felt ‘too broad’ to make actionable. So, I broke it into smaller chunks - the crazy eight.
  anchor_at: "playbook-lifetime-value.md:232"
- id: A-playbooks-price-025
  type: framework
  name: >-
    The Crazy Eight
  statement: >-
    There are eight ways to make a customer worth more, and any product or service is run through all eight: raise prices, lower delivery cost, upsell frequency, upsell quantity, upsell quality, downsell quantity, downsell quality, cross-sell.
  why: >-
    If you make more than anyone else does from the same customer then you can spend more than anyone else to get them; the eight are small enough chunks to apply to any business, unlike the two-way frame they replace.
  applies_when: >-
    Whenever LTV has to go up; the author runs the list in almost every business he encounters and drills his team on it.
  structure:
    - >-
      1) Raise prices
    - >-
      2) Lower the cost of delivering the thing
    - >-
      3) Upsell Frequency: Get them to buy more again later
    - >-
      4) Upsell Quantity: Get them to buy more now
    - >-
      5) Upsell Quality: Get them to buy a premium version
    - >-
      6) Downsell Quantity: Get them to buy fewer things rather than nothing
    - >-
      7) Downsell Quality: Get them to buy lower-cost things rather than nothing
    - >-
      8) Cross-Sell: Get them to buy a different thing on top
  anchor: >-
    smaller chunks so I could apply them to any business. I actually drill my team on this stuff
  source: >-
    playbook-lifetime-value.md, The Crazy Eight, lines 229–253
  confirmations: 3
  authors_caveat: >-
    The same eight are listed in a different order in the table of contents (lines 43–50) and in the closing worksheet (lines 589–613), where cross-sell comes third and decrease costs second; the numbered list at 239–246 is the canonical one and the body sections #1–#8 follow the table of contents order. Each section ends with an Action Step, and the author recommends going through each of the crazy eight and writing down the action steps.
  anchor_at: "playbook-lifetime-value.md:234"
- id: A-playbooks-price-026
  type: framework
  name: >-
    Crazy Eight #1 Increase Prices
  statement: >-
    Find the price that maximizes sales conversion rate x lifetime gross profit, set it, calculate the break-even conversion rate against the old price, track the new conversion rate, and test again until conversion rate x LTGP drops.
  why: >-
    Pricing affects gross profit more than any of the eight and all the extra drops straight to the bottom line - a 10% profit business that raises prices 20% with sales held flat triples; a research study by Profitwell suggested a tight relationship between profitability and how frequently a company tested pricing.
  applies_when: >-
    Any offer, tested every quarter; for a brand new offer, start low then go up.
  structure:
    - >-
      a) Sales conversion rate x lifetime gross profit.
    - >-
      b) We  test  prices  every  quarter.
    - >-
      Action Step: Set a new price. Let your sales team know (or update it on your site).
    - >-
      Calculate what the difference in gross profit per unit will be.
    - >-
      Figure out what conversion rate would be your ‘break even’ point from your old price to the new higher price.
    - >-
      Track the conversion rate with the new price. If it’s above your break even point, you have a winner.
    - >-
      Then, test again until the conversion rate x LTGP drops.
  anchor: >-
    a) Sales conversion rate x lifetime gross profit. The price that gets the most people to
  source: >-
    playbook-lifetime-value.md, #1 Increase Prices, lines 254–290
  confirmations: 1
  authors_caveat: >-
    Pro Tip: Start Low Then Go Up - you need sales first to check people want the thing; nudge the price by 20% every 10 sales or so until you notice a dramatic drop in sales, then go back to the sweet spot. Testing price is expensive for a few months, but the only thing more expensive is not testing at all.
  anchor_at: "playbook-lifetime-value.md:266"
- id: A-playbooks-price-027
  type: framework
  name: >-
    Crazy Eight #2 Decrease Costs
  statement: >-
    Raise gross profit by cutting the cost of delivering the same thing, choosing from nine standing tactics, and pick the top two you could implement.
  why: >-
    Lowering delivery cost increases gross profit and makes the business more scalable, though unlike price it can only go down to zero.
  applies_when: >-
    Any business where delivery cost is a meaningful share of price.
  structure:
    - >-
      i) Increase the ratio of employees to customers .
    - >-
      ii) Offshore talent .
    - >-
      iii) Sell more similar customers to productize your delivery .
    - >-
      iv) Done  for  you  to  Done  with  you .
    - >-
      v) Cap usage .
    - >-
      vi) Lifetime  to  annual .
    - >-
      vii) In-person to remote .
    - >-
      viii) Cut meeting times .
    - >-
      ix) Buy in bulk & prepay .
  anchor: >-
    You decrease your costs to deliver the same thing. This increases gross profit. Contrary to
  source: >-
    playbook-lifetime-value.md, #2 Decrease Costs, lines 295–342
  confirmations: 1
  anchor_at: "playbook-lifetime-value.md:296"
- id: A-playbooks-price-028
  type: framework
  name: >-
    Crazy Eight #3 Increase # of Purchases
  statement: >-
    There are three ways to get people to buy the same thing more times - add recurring, decrease churn, follow up - and at least one has to be picked.
  why: >-
    Even with high churn, moving someone from buying once to buying three times triples how many times they buy; and if churn goes from 10% per month to 5% per month, you double LTV (Price/Churn= Lifetime revenue).
  applies_when: >-
    Any business whose customers are one and done or churn fast; pick one to prioritize over the next quarter.
  structure:
    - >-
      a) Add recurring .
    - >-
      b) Decrease churn .
    - >-
      c) Follow Up .
  anchor: >-
    purchases (without doing other crazy eight stuff at the same time). You can add recurring,
  source: >-
    playbook-lifetime-value.md, #3 Increase # of Purchases, lines 347–398
  confirmations: 1
  authors_caveat: >-
    The steps for decreasing churn are deliberately not given here - The Churn Checklist Playbook covers the steps to make this happen in insane depth so I won’t go over it here. The author's preferred long term follow up is a quarterly promotion, with value to the list the rest of the time to balance the give:ask ratio.
  anchor_at: "playbook-lifetime-value.md:350"
- id: A-playbooks-price-029
  type: framework
  name: >-
    Crazy Eight #5 Sell More (Increase Quantity)
  statement: >-
    Selling more of the same thing at once happens in three ways - bulk, more often, bigger - and the quantity upsell is offered first, with the standard offer as the downsell.
  why: >-
    Offering the larger version first and downselling the standard one can produce 20%+ lifts in cash collected overnight.
  applies_when: >-
    Any product or service; one or more of the three will apply to a given business.
  structure:
    - >-
      i) Bulk: You get the client to prepay for a year. (12x)
    - >-
      ii) More often: You upsell how often you service from monthly to every three weeks (1.33x)
    - >-
      iii) Bigger: You go from working 1 hour each time to 3 hours each time. (3x)
  anchor: >-
    of delivery, think “more often.” Third, you can sell more in the same package, think “bigger.”
  source: >-
    playbook-lifetime-value.md, #5 Sell More (Increase Quantity), lines 423–438
  confirmations: 1
  authors_caveat: >-
    More often is marked N/A for physical products on this.
  anchor_at: "playbook-lifetime-value.md:427"
- id: A-playbooks-price-030
  type: framework
  name: >-
    Crazy Eight #6 Sell Better (Increase Quality)
  statement: >-
    A better version of the same thing at a higher price comes in two forms - newer, or premium - and premium is built by moving any of the standing service dimensions up a level.
  why: >-
    Offering the premium version first and downselling the standard one, or upgrading an existing customer in a second meeting, routinely produces 20%+ lifts in cash collected upfront and LTV overall.
  applies_when: >-
    Any service or physical product; the same dimension list reversed becomes the quality downsell of #8.
  structure:
    - >-
      First, a newer version of the same thing.
    - >-
      Second, a premium version of the same thing (think better ingredients, better materials, or better people).
    - >-
      i) Faster response times.
    - >-
      ii) Time Availability: Come/call specific times vs. whenever you want.
    - >-
      iii) Days of the week: Mon/Wed/Fri vs. All Days.
    - >-
      iv) Times of day: 9 to 5 vs. 24hrs.
    - >-
      v) Amount of time: 15min Support Calls vs. 60min Support Calls.
    - >-
      vi) Location Availability: This one location vs. all locations we own.
    - >-
      vii) Cancellations: Reschedule fees vs. free.
    - >-
      viii) Speed Of Response: Reply in minutes vs. hours vs days etc.
    - >-
      ix) Speed Of Delivery: Wait in line vs. priority, same day/next day vs. next week.
    - >-
      x) Service Ratio: One-on-one vs. one-to-many vs. many-to-one.
    - >-
      xi) Communication Method: Text vs. Chat Support vs. Video Call Support etc.
    - >-
      xii) Provider  Qualifications:  You  vs.  long-time  employee  vs.  new  employee, etc.
    - >-
      xiii) Live vs. Recorded: Watch it happening now vs. watch it after it happens later.
    - >-
      xiv) In-Person  vs.  Remote:  Watch  where  it  happens  vs.  watch  it  somewhere else.
    - >-
      xv) DIY, DWY, DFY: Do It Yourself vs. Done With You vs. Done For You.
    - >-
      xvi) Expirations: Works forever vs. works for X time vs. works at specific times.
    - >-
      xvii) Personalization: Generic vs. 3-5 avatars vs. made just for you.
  anchor: >-
    I think about it in two ways. First, a newer version of the same thing. Second, a premium
  source: >-
    playbook-lifetime-value.md, #6 Sell Better (Increase Quality), lines 443–486
  confirmations: 1
  anchor_at: "playbook-lifetime-value.md:445"
- id: A-playbooks-price-031
  type: framework
  name: >-
    Crazy Eight #7 Downsell Fewer (Lower Quantity)
  statement: >-
    Sell a smaller amount of the same thing - fewer, less often, or smaller - to people who would otherwise buy nothing.
  why: >-
    If it means this or nothing, then this beats nothing: the measure is what you make per person who walks in the door, and in the worked example the downsell makes 50% more per visitor even though the extra sales are at a lower price.
  applies_when: >-
    Only for customers who do not qualify for your main offer; these tend to incur little operational drag since you already do or make the stuff.
  structure:
    - >-
      i) Quantity: You get the client to buy three months upfront instead of twelve.
    - >-
      ii) Less  often:  You  downsell  the  client  to  buy  one  visit  every  other  month rather than nothing at all.
    - >-
      iii) Smaller: You go from working 1 hour each time to 30min each time. (.5x)
  anchor: >-
    You sell a smaller amount of the same thing. This works the same way as the quantity
  source: >-
    playbook-lifetime-value.md, #7 Downsell Fewer (Lower Quantity), lines 491–521
  confirmations: 1
  authors_caveat: >-
    You lose money on downsells when people who would’ve bought the $5 thing now opt for the $2.50 thing: Downsell people who otherwise don’t qualify for your other offers. In other words, I forbid my sales team from selling a qualified person a downsell.
  anchor_at: "playbook-lifetime-value.md:492"
- id: A-playbooks-price-032
  type: framework
  name: >-
    Crazy Eight #8 Downsell Lower Quality
  statement: >-
    Offer a version that gets the same result with a lower quality experience - longer, riskier, more hassle - built by taking the quality upsell list and reversing it.
  why: >-
    It reaches buyers who would otherwise buy nothing, and since you already do or make the stuff it incurs little operational drag.
  applies_when: >-
    Only to customers who do not qualify for your main offer.
  structure:
    - >-
      All we do is take the list for a quality upsell and reverse it.
    - >-
      i) Slower response times. They wait in line.
    - >-
      ii) Less availability for meetings
    - >-
      iii) Fewer locations for them to access
    - >-
      iv) Fewer days per week to service them
    - >-
      v) More limited hours to service them
    - >-
      vi) Less flexibility for rescheduling
    - >-
      vii) More junior employees helping them
    - >-
      viii) Higher customer to employee ratio
    - >-
      ix) Less convenient communication methods
    - >-
      x) More recorded, less live
    - >-
      xi) More remote, less in person
    - >-
      xii) Done for you to Done with you. Done with you to Do it yourself.
    - >-
      xiii) Less personalization.
    - >-
      xiv) No guarantee or worse guarantee.
    - >-
      Physical products: Lower quality ingredients or materials in construction. Worse or zero warranty/guarantee. Longer wait times.
  anchor: >-
    You downsell something that gets the same result for the customer as your main offer
  source: >-
    playbook-lifetime-value.md, #8 Downsell Lower Quality, lines 526–556
  confirmations: 1
  anchor_at: "playbook-lifetime-value.md:527"
```
