# $100M Playbooks: Pricing, Price Raise, Lifetime Value (2025) — ярус 2, группа `tier2-playbooks-price`, единиц после валидации: 53

Часть `pipeline/hormozi/validated.md` (там шапка, гейт, список валидаторов и правила обращения с якорем). Блоки перенесены из `pipeline/hormozi/catch/tier2-playbooks-price-<X>.md` байт в байт; фазой 2 дописаны `tier`, `merged_from` и поднятое `confirmations`. Проверка: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/validated/tier2-playbooks-price.md`.


## A. Фреймворки — 22

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
  confirmations: 2
  authors_caveat: >-
    The walkthrough is run on one set of stats (30 new clients/mo, 33% churn, $100/mo, 20% net margins) and only advertising and delivery costs are counted: To simplify stuff, I have only included costs of advertising and delivering.
  anchor_at: "playbook-pricing.md:305"
  tier: 2
  merged_from: [D-playbooks-price-001]
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
  confirmations: 4
  authors_caveat: >-
    The section is headed Three Metrics but only two are listed in the text; price itself appears only as the first column of the table. The same table with the same $10/$20/$100 rows recurs in playbook-price-raise.md lines 267–300 (How To Pick Your Price), which the build map counts as one place, not two.
  anchor_at: "playbook-pricing.md:385"
  tier: 2
  merged_from: [B-playbooks-price-003, C-playbooks-price-028, D-playbooks-price-006]
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
  confirmations: 4
  authors_caveat: >-
    There  are  other  pricing  strategies  that  create  bigger  swings,  but  they  require more work/change/risk, so they were excluded; some plays will not be a direct fit for a given business.
  anchor_at: "playbook-pricing.md:1351"
  tier: 2
  merged_from: [D-playbooks-price-016, E-playbooks-price-009]
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
  confirmations: 5
  authors_caveat: >-
    To be clear, if you do not get charged taxes, you cannot charge them; the alternative given is to incorporate in a state that doesn't charge sales tax, checking with lawyers first.
  anchor_at: "playbook-pricing.md:690"
  tier: 2
  merged_from: [B-playbooks-price-019, C-playbooks-price-012, D-playbooks-price-020, D-playbooks-price-021]
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
  confirmations: 5
  authors_caveat: >-
    Few people will balk if you keep it under 15%.
  anchor_at: "playbook-pricing.md:802"
  tier: 2
  merged_from: [B-playbooks-price-021, D-playbooks-price-023, D-playbooks-price-024, D-playbooks-price-025]
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
  confirmations: 5
  authors_caveat: >-
    Requiring annual only drops conversions because the price is 12x the monthly rate, and whether it drops them 5x is untested: I don’t know. You’d have to test it for you. A stated workaround is to sell six to twelve weeks first and upsell the prepaid year after trust is built. Benchmarks: with a 16% annual discount on a sales page 10-15% select annual, 30% if it is the default, 35-40% over the phone.
  anchor_at: "playbook-pricing.md:833"
  tier: 2
  merged_from: [B-playbooks-price-022, C-playbooks-price-016, D-playbooks-price-026, D-playbooks-price-027]
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
  confirmations: 2
  authors_caveat: >-
    Pro Tip: When NOT To Add .99 or change 7s to 9s - luxury items often end on a round number, because people who buy luxury goods want not to get a deal; premium does not mean luxury, and the author still says to test it.
  anchor_at: "playbook-pricing.md:958"
  tier: 2
  merged_from: [B-playbooks-price-024]
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
  confirmations: 5
  authors_caveat: >-
    If you can bill annually, by all means do it; this play is for markets where you can't. If they balk at the fee you just drop it, and they don't get the benefit. Pro Tip: have both a setup fee and a renewal fee so you can waive one to get the other.
  anchor_at: "playbook-pricing.md:1014"
  tier: 2
  merged_from: [B-playbooks-price-026, C-playbooks-price-019, D-playbooks-price-030, E-playbooks-price-012]
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
  confirmations: 3
  authors_caveat: >-
    Pro Tip: Don’t Be A Sneak - this isn’t ‘undisclosed’ or ‘forced’ continuity, it is continuity they must agree to up front, so be clear about what happens after X time period.
  anchor_at: "playbook-pricing.md:1056"
  tier: 2
  merged_from: [B-playbooks-price-027, E-playbooks-price-013]
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
  confirmations: 3
  authors_caveat: >-
    Section E is not scalable by design: Get ready to roll your sleeves up and respond to customers. If there is a community, post it as a video with comments turned off and refer questions to you directly.
  anchor_at: "playbook-price-raise.md:332"
  tier: 2
  merged_from: [E-playbooks-price-019]
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
  confirmations: 3
  authors_caveat: >-
    Note: 1) Don’t say things you’re not going to do (that’s lying) 2) Frame all investments you make as value for them 3) Don’t decide to add expenses you didn’t plan on incurring - this negates the benefits of the price raise to begin with.
  anchor_at: "playbook-price-raise.md:373"
  tier: 2
  merged_from: [B-playbooks-price-042]
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
  confirmations: 4
  anchor_at: "playbook-price-raise.md:438"
  tier: 2
  merged_from: [C-playbooks-price-031, D-playbooks-price-055, E-playbooks-price-021]
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
  confirmations: 5
  anchor_at: "playbook-price-raise.md:499"
  tier: 2
  merged_from: [B-playbooks-price-045, C-playbooks-price-033, E-playbooks-price-022]
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
  confirmations: 3
  anchor_at: "playbook-price-raise.md:671"
  tier: 2
  merged_from: [B-playbooks-price-048, B-playbooks-price-049]
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
  confirmations: 5
  anchor_at: "playbook-lifetime-value.md:116"
  tier: 2
  merged_from: [B-playbooks-price-050, B-playbooks-price-051, D-playbooks-price-061, E-playbooks-price-023]
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
  confirmations: 5
  authors_caveat: >-
    The same eight are listed in a different order in the table of contents (lines 43–50) and in the closing worksheet (lines 589–613), where cross-sell comes third and decrease costs second; the numbered list at 239–246 is the canonical one and the body sections #1–#8 follow the table of contents order. Each section ends with an Action Step, and the author recommends going through each of the crazy eight and writing down the action steps.
  anchor_at: "playbook-lifetime-value.md:234"
  tier: 2
  merged_from: [E-playbooks-price-027, E-playbooks-price-029]
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
  confirmations: 4
  authors_caveat: >-
    Pro Tip: Start Low Then Go Up - you need sales first to check people want the thing; nudge the price by 20% every 10 sales or so until you notice a dramatic drop in sales, then go back to the sweet spot. Testing price is expensive for a few months, but the only thing more expensive is not testing at all.
  anchor_at: "playbook-lifetime-value.md:266"
  tier: 2
  merged_from: [B-playbooks-price-054, B-playbooks-price-055, D-playbooks-price-065]
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
  confirmations: 3
  anchor_at: "playbook-lifetime-value.md:296"
  tier: 2
  merged_from: [B-playbooks-price-057, B-playbooks-price-058]
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
  confirmations: 3
  authors_caveat: >-
    More often is marked N/A for physical products on this.
  anchor_at: "playbook-lifetime-value.md:427"
  tier: 2
  merged_from: [C-playbooks-price-044, E-playbooks-price-030]
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
  confirmations: 2
  anchor_at: "playbook-lifetime-value.md:445"
  tier: 2
  merged_from: [E-playbooks-price-031]
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
  confirmations: 2
  authors_caveat: >-
    You lose money on downsells when people who would’ve bought the $5 thing now opt for the $2.50 thing: Downsell people who otherwise don’t qualify for your other offers. In other words, I forbid my sales team from selling a qualified person a downsell.
  anchor_at: "playbook-lifetime-value.md:492"
  tier: 2
  merged_from: [E-playbooks-price-033]
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
  confirmations: 2
  anchor_at: "playbook-lifetime-value.md:527"
  tier: 2
  merged_from: [E-playbooks-price-034]
```


## B. Правила и критерии — 23

```yaml
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
  confirmations: 3
  anchor_at: "playbook-pricing.md:412"
  tier: 2
  merged_from: [D-playbooks-price-008]
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
  tier: 2
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
  confirmations: 4
  authors_caveat: >-
    Some markets are price sensitive and others less so; the 9-out-of-10 rate is the author's experience, not a guarantee.
  anchor_at: "playbook-pricing.md:428"
  tier: 2
  merged_from: [D-playbooks-price-009, D-playbooks-price-010, D-playbooks-price-011]
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
  confirmations: 7
  authors_caveat: >-
    The lookback-window explanation is flagged by the author as his theory, not established fact.
  anchor_at: "playbook-pricing.md:463"
  tier: 2
  merged_from: [C-playbooks-price-005, C-playbooks-price-015, D-playbooks-price-014, E-playbooks-price-006]
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
  tier: 2
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
  confirmations: 3
  anchor_at: "playbook-pricing.md:483"
  tier: 2
  merged_from: [D-playbooks-price-015, E-playbooks-price-007]
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
  confirmations: 2
  anchor_at: "playbook-pricing.md:493"
  tier: 2
  merged_from: [E-playbooks-price-008]
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
  tier: 2
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
  confirmations: 2
  anchor_at: "playbook-price-raise.md:212"
  tier: 2
  merged_from: [D-playbooks-price-044]
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
  confirmations: 3
  anchor_at: "playbook-price-raise.md:215"
  tier: 2
  merged_from: [D-playbooks-price-045]
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
  tier: 2
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
  confirmations: 3
  anchor_at: "playbook-price-raise.md:243"
  tier: 2
  merged_from: [D-playbooks-price-047]
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  confirmations: 4
  anchor_at: "playbook-price-raise.md:411"
  tier: 2
  merged_from: [C-playbooks-price-030, E-playbooks-price-020]
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
  confirmations: 3
  anchor_at: "playbook-price-raise.md:429"
  tier: 2
  merged_from: [D-playbooks-price-054]
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
  confirmations: 3
  anchor_at: "playbook-price-raise.md:505"
  tier: 2
  merged_from: [D-playbooks-price-056]
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
  confirmations: 4
  anchor_at: "playbook-price-raise.md:508"
  tier: 2
  merged_from: [C-playbooks-price-032, D-playbooks-price-057]
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
  confirmations: 3
  anchor_at: "playbook-lifetime-value.md:205"
  tier: 2
  merged_from: [D-playbooks-price-063, E-playbooks-price-026]
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
  tier: 2
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
  confirmations: 4
  anchor_at: "playbook-lifetime-value.md:507"
  tier: 2
  merged_from: [D-playbooks-price-068]
```


## C. Разборы (кейсы) — 3

```yaml
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
  tier: 2
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
  tier: 2
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
  tier: 2
```


## D. Антипаттерны и границы — 5

```yaml
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
  confirmations: 3
  authors_caveat: >-
    Of course, test it out. Sometimes shorter numbers do better.
  anchor_at: "playbook-pricing.md:947"
  tier: 2
  merged_from: [D-playbooks-price-029, E-playbooks-price-011]
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
  confirmations: 2
  anchor_at: "playbook-price-raise.md:249"
  tier: 2
  merged_from: [C-playbooks-price-027]
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
  tier: 2
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
  tier: 2
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
  tier: 2
```
