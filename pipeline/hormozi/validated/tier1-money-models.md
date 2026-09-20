# $100M Money Models (2025) — ярус 1, группа `tier1-money-models`, единиц после валидации: 205

Часть `pipeline/hormozi/validated.md` (там шапка, гейт, список валидаторов и правила обращения с якорем). Блоки перенесены из `pipeline/hormozi/catch/tier1-money-models-<X>.md` байт в байт; фазой 2 дописаны `tier`, `merged_from` и поднятое `confirmations`. Проверка: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/validated/tier1-money-models.md`.


## A. Фреймворки — 22

```yaml
- id: A-money-models-003
  type: framework
  name: >-
    The three options of a Win Your Money Back Offer
  statement: >-
    A Win Your Money Back Offer can be won on results, on actions, or on both, and whichever you pick the results and actions must be simple to track.
  why: >-
    On results the customer bets on their own ability to reach the goal; on actions they bet on their ability to follow directions; on both, the author sets a good goal and shows how to reach it, so people who have too few skills to succeed alone still get a fighting chance.
  applies_when: >-
    Setting the terms a customer must meet to get their money back or store credit.
  structure:
    - >-
      Results: no matter what they do, if the customer gets the result, they win their money back.
    - >-
      Actions: no matter what results they get, if the customer does what you ask, they win their money back.
    - >-
      Actions and Results: you hold customers accountable to following directions and getting results; if they do both, they win their money back.
  anchor: >-
    To 'Win Your Money Back' the person has three options: Get Results, Take
  source: >-
    100m-money-models.md, Win Your Money Back, Description, lines 1148-1172
  confirmations: 1
  anchor_at: "100m-money-models.md:1148"
  tier: 1
- id: A-money-models-004
  type: framework
  name: >-
    The three characteristics of good Win Your Money Back criteria
  statement: >-
    Criteria for winning the money back must be easy to track, must get customers results, and must advertise the business.
  why: >-
    These criteria make or break the offer: people mess up what they are not trained on, realistic criteria are what actually produce the result, and building promotion into the criteria gets free advertising from participants.
  applies_when: >-
    Writing the refund criteria of a Win Your Money Back Offer, and the same criteria are reused for a Trial With Penalty.
  structure:
    - >-
      1) Easy To Track. Train them on exactly what they need to do (or they will mess up). Bonus points if people already do it.
    - >-
      2) Gets Customers Results. Make criteria likely to get them their desired results. Realistic criteria do just fine.
    - >-
      3) Advertises The Business. For example: posting about their participation, tagging in social media, referring, or leaving reviews and testimonials.
  anchor: >-
    or break this offer. Good criteria have three characteristics:
  source: >-
    100m-money-models.md, Win Your Money Back, Important Notes, lines 1268-1300
  confirmations: 5
  anchor_at: "100m-money-models.md:1269"
  tier: 1
  merged_from: [B-money-models-006, B-money-models-007, B-money-models-008]
- id: A-money-models-005
  type: framework
  name: >-
    The six steps of running a Giveaway Offer
  statement: >-
    A Giveaway runs as six steps: pick a Grand Prize, pick the promotional offer, ask for contact information and eligibility, pick the qualifying actions, put it on a deadline, then announce the winner and contact everyone else.
  why: >-
    Everyone who entered showed interest in the thing you sell, so after one person wins the Grand Prize the rest qualify for the promotional offer, and the Grand Prize's assigned value serves as the price anchor that makes the discounted core offer look huge.
  applies_when: >-
    Using a giveaway, scholarship, sweepstake or raffle as an Attraction Offer.
  structure:
    - >-
      Pick a Grand Prize.
    - >-
      Pick your promotional offer.
    - >-
      Ask for contact information and other eligibility criteria.
    - >-
      Pick what actions you want entrants to take to qualify for the big prize.
    - >-
      Put the giveaway on a deadline to add urgency.
    - >-
      Announce the Grand Prize winner and contact everyone else.
  anchor: >-
    Giveaway Offers advertise a chance to win a big prize in exchange for
  source: >-
    100m-money-models.md, Giveaways, Description, lines 1513-1533
  confirmations: 2
  authors_caveat: >-
    Consult legal counsel about how to structure your giveaway; somebody actually has to win the Grand Prize and the rules must make the qualifications clear.
  anchor_at: "100m-money-models.md:1513"
  tier: 1
- id: A-money-models-006
  type: framework
  name: >-
    Urgency in three places
  statement: >-
    A giveaway carries a deadline at three separate points: to enter, to claim, and to use.
  why: >-
    Deadlines make people act; putting an expiration date on claiming the prize makes them more likely to claim it.
  applies_when: >-
    Running a Giveaway Offer.
  structure:
    - >-
      To enter: make how long they have to enter clear in the advertisements.
    - >-
      To claim: once you announce the winner(s), let them know how long they have to claim.
    - >-
      To use: once you let people know what they won, tell them how long they have to use it.
  anchor: >-
    **Urgency, Urgency, Urgency.** I add urgency in three places---to enter,
  source: >-
    100m-money-models.md, Giveaways, Important Notes, lines 1688-1694
  confirmations: 3
  anchor_at: "100m-money-models.md:1688"
  tier: 1
  merged_from: [B-money-models-020, B-money-models-024]
- id: A-money-models-007
  type: framework
  name: >-
    The two steps of a Decoy Offer
  statement: >-
    Advertise a lesser, smaller or simpler version of your premium offer as a decoy, then when leads engage, offer both options side by side while emphasizing the premium one.
  why: >-
    Putting the decoy and the premium offer side-by-side lets leads see how much more valuable the premium offer is; either way you close everyone, which makes getting new customers cheap and profitable.
  applies_when: >-
    You want a cheap or free offer to get leads engaged but want most of them to buy the premium version.
  structure:
    - >-
      1) Advertise a lesser, smaller, or simpler version of your premium offer as a decoy.
    - >-
      2) When leads engage, offer both options, but emphasize the premium one.
  anchor: >-
    Here are the steps to make a Decoy Offer:
  source: >-
    100m-money-models.md, Decoy Offer, Description, lines 1864-1886
  confirmations: 2
  anchor_at: "100m-money-models.md:1878"
  tier: 1
- id: A-money-models-009
  type: framework
  name: >-
    The structure of Pay Less Now or Pay More Later
  statement: >-
    Give the prospect a choice between paying full price later under a conditional guarantee and paying a discounted price now with bonuses, offering the pay-now option only after they have accepted the pay-later one, and have something more, better or newer to sell them afterwards.
  why: >-
    The pay-later option removes all risk and lets you advertise free while putting their card on file; once they have agreed to pay later, a 20-50% discount and bonuses move many of them to pay now.
  applies_when: >-
    An Attraction Offer where you can promise a clear yes/no result inside a short time frame.
  structure:
    - >-
      The Pay Later option has a delayed payment with a conditional guarantee.
    - >-
      The Pay Now option offers a 20--50% discount and bonuses if they pay now, offered after they accept the pay later option.
    - >-
      Have something more, better, newer to offer when the time is right.
  anchor: >-
    ● Pay Less Now Or Pay More Later Offers give people a choice to pay
  source: >-
    100m-money-models.md, Pay Less Now or Pay More Later, Description and Summary Points, lines 2332-2467
  confirmations: 4
  authors_caveat: >-
    If more than 10% of pay-later people cancel their payment, you promised too much, the guarantee conditions are too low, or the price is too high.
  anchor_at: "100m-money-models.md:2450"
  tier: 1
  merged_from: [B-money-models-043, B-money-models-044]
- id: A-money-models-011
  type: framework
  name: >-
    The four tactics of a Menu Upsell
  statement: >-
    A Menu Upsell runs in order: unsell what they don't need, prescribe what they do need, ask their preference between A and B, then ask if they want to use the card on file.
  why: >-
    Each step replaces the question of whether to buy with a different question: crossing out what they don't need builds goodwill and highlights what they do, prescribing explains how to use it as if they already have it, an A/B question removes the option of not buying, and the card on file lowers the hidden costs of buying.
  applies_when: >-
    Menu Upsells work best when you have multiple offers available.
  structure:
    - >-
      First, I unsell what customers don't need.
    - >-
      Second, I prescribe what they do need.
    - >-
      Third, I ask their preferences between A and B.
    - >-
      Last, I make buying easy by asking if they want to use the card on file.
  anchor: >-
    Menu Upsells combine up to four tactics: Unselling,
  source: >-
    100m-money-models.md, Menu Upsell, Description and Summary Points, lines 3082-3261
  confirmations: 2
  anchor_at: "100m-money-models.md:3086"
  tier: 1
- id: A-money-models-013
  type: framework
  name: >-
    The five steps of an Anchor Upsell
  statement: >-
    Present the anchor, get the gasp, come to the rescue, present the main offer, then ask for payment.
  why: >-
    Presenting a premium version 5-10x the price first makes the main offer look like a much better deal, so more people buy it; anchored customers also spend more than they planned, and some still buy the expensive thing.
  applies_when: >-
    Anchor Upsells work best when the lower-price offer has the same core functions as the premium one.
  structure:
    - >-
      1. Present the Anchor---the really expensive thing.
    - >-
      2. Get "The Gasp"---expect the customer to freak out about the cost.
    - >-
      3. Come to the rescue---ask if they care about what makes it premium.
    - >-
      4. Present your main offer---expect the customer to feel relieved and see the better deal.
    - >-
      5. Ask how they wanna pay---Which card do you prefer?
  anchor: >-
    ● Present anchor. Get gasp. Come to the rescue. Present core offer. Ask
  source: >-
    100m-money-models.md, Anchor Upsell, Description and Summary, lines 3351-3451
  confirmations: 6
  authors_caveat: >-
    If you treat the anchor like a fake, so will the customer; make a premium offer you actually want people to buy.
  anchor_at: "100m-money-models.md:3450"
  tier: 1
  merged_from: [A-playbooks-price-013, B-playbooks-price-029, D-playbooks-price-032, E-playbooks-price-014]
- id: A-money-models-015
  type: framework
  name: >-
    The four situations for a Rollover Upsell
  statement: >-
    Rollover Upsells are used on customers who left a while ago, on upset customers instead of a refund, on other people's upset customers, and on regular customers.
  why: >-
    Previous customers are still customers, rolling over beats refunding when you did a bad job, and a competitor's unhappy customer becomes a hot lead once you credit what they paid elsewhere.
  applies_when: >-
    Choosing the who of a Rollover Upsell.
  structure:
    - >-
      First, to re-engage customers who left a while ago.
    - >-
      Second, to rescue upset customers as a better alternative to a refund.
    - >-
      Third, to 'rescue' other people's upset customers.
    - >-
      Fourth, to upsell regular customers.
  anchor: >-
    ● Who to upsell: old customers, upset customers, other people's upset
  source: >-
    100m-money-models.md, Rollover Upsell, Description and Summary Points, lines 3564-3690
  confirmations: 2
  anchor_at: "100m-money-models.md:3687"
  tier: 1
- id: A-money-models-017
  type: framework
  name: >-
    The Rules of Downselling
  statement: >-
    Six rules apply to every downsell process: the no was to this offer only, downsells are trades, personalize rather than pressure, offer the same things in new ways, never drop the price just to get somebody to buy, and remember that customers talk about price.
  why: >-
    A rejection of the offer is not a rejection of you but an opportunity to find what they really want; dropping the price is discounting rather than downselling, and when customers find out someone got the same thing for less just because, you upset people and create an ethical problem.
  applies_when: >-
    They apply to all my downsell processes.
  structure:
    - >-
      Remember, They Said No To This Offer, Not All Offers.
    - >-
      Downsells Are Trades. If you're gonna give something, get something.
    - >-
      Personalize, Don't Pressure.
    - >-
      Offer The Same Things In New Ways.
    - >-
      Don't Drop Your Price Just To Get Somebody To Buy.
    - >-
      Customers Talk About Price.
  anchor: >-
    First, we cover my rules of downselling---*they apply to all my downsell
  source: >-
    100m-money-models.md, Section IV: Downsell Offers, The Rules of Downselling, lines 3756-3810
  confirmations: 4
  anchor_at: "100m-money-models.md:3756"
  tier: 1
  merged_from: [B-money-models-074, B-money-models-075, D-money-models-047]
- id: A-money-models-018
  type: framework
  name: >-
    The seven steps of the Payment Plan Downsell
  statement: >-
    The payment plan process runs up to seven steps that shift from getting paid more up front to more over time, and you stop at the step where they buy.
  why: >-
    A huge percentage of the time "it costs too much" really means "this costs too much up front", so payment plans get more buyers like a discount while still collecting full price over time; presenting in order of most cash up front to least also matches the churn data, where fewer, bigger payments cancel less.
  applies_when: >-
    A prospect rejects the offer on price.
  structure:
    - >-
      1. Reward for paying in full rather than punish for paying over time
    - >-
      2. Offer 3rd-party financing, credit card, layaway options
    - >-
      3. Offer half now, half later
    - >-
      4. Check to see if they still want the thing
    - >-
      5. Offer to split into three payments
    - >-
      6. Offer evenly spread payments
    - >-
      7. Offer a Free Trial
  anchor: >-
    My Payment Plan Downsell process takes up to seven steps. The process
  source: >-
    100m-money-models.md, Payment Plan Downsells, Description and Summary Points, lines 3922-4133
  confirmations: 2
  authors_caveat: >-
    Payment plans can lose money in two ways: when people cancel before you turn a profit, and most of all when people who would have paid in full take a payment plan and cancel early; so the number of paid-in-fulls must not go down after you add them.
  anchor_at: "100m-money-models.md:3922"
  tier: 1
- id: A-money-models-019
  type: framework
  name: >-
    "Seesaw" Downselling
  statement: >-
    A shorter payment-plan process that starts by asking whether they want giant monthly payments or tiny ones, then frames prepaying as the way to get a discount and zero monthly payments, then adjusts the down payment down until the monthly rate suits them.
  why: >-
    It frames the payment plan as negative and highlights the benefits of prepaying, while still incentivizing bigger down payments to get the monthly payments lower.
  applies_when: >-
    If you prefer fewer steps, or have less experienced salespeople.
  structure:
    - >-
      Instead of asking for the full amount, just ask "Would you rather have giant monthly payments or tiny ones?"
    - >-
      Then you say "It normally costs XXX. And if you prepay it today, you get a huge discount and zero monthly payments. That work?"
    - >-
      Then, if they say they can't afford it, say the more they put down now, the lower their monthly payments: "We'll simply adjust the down payment until you get a monthly rate you like."
    - >-
      If they still say no, ask if they still want the product; if they do, walk them through the options as a team effort.
  anchor: >-
    ● "Seesaw" Downselling gradually shifts from paid-in-full to equal
  source: >-
    100m-money-models.md, Payment Plan Downsells, Important Notes, lines 4022-4037
  confirmations: 3
  anchor_at: "100m-money-models.md:4126"
  tier: 1
  merged_from: [B-money-models-088]
- id: A-money-models-020
  type: framework
  name: >-
    The five steps of downselling a Trial With Penalty
  statement: >-
    Offer the trial last, always get a credit card, sell staying and paying, explain the fees only after getting the card, and make check-ins required.
  why: >-
    Explaining the fees before you get the card produces more resistance; agreeing in advance to stay long-term if the program works means there is a point in giving the trial at all; and mandatory check-ins are the upsell opportunities that turn the trial into a paying customer.
  applies_when: >-
    Someone has made it clear they don't want your first offer, in a recurring product or service where the customer has to do work to get results.
  structure:
    - >-
      Offer The Trial Last.
    - >-
      Always Get A Credit Card.
    - >-
      Always Sell Staying And Paying.
    - >-
      Explain the fees after getting their card.
    - >-
      Make Check-ins Required.
  anchor: >-
    **How To Downsell The Trial.** Here's a graphic to show how I downsell a
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, lines 4296-4372
  confirmations: 2
  authors_caveat: >-
    The five steps themselves are shown in the book as a graphic; this list is reconstructed from the five headings that follow that sentence, in their order, and matches the summary point "get the card, get the commitment, explain what they have to do to get results and the meetings they must attend, and what happens if they don't."
  anchor_at: "100m-money-models.md:4296"
  tier: 1
- id: A-money-models-021
  type: framework
  name: >-
    The three trial outcomes and how to upsell each
  statement: >-
    When someone takes a trial one of three things happens — they like it, they hate it, or they don't use it — and each has its own upsell.
  why: >-
    Successful customers get even more value out of the better and more profitable offers; an unhappy customer is recovered by taking the blame and offering the higher level thing, which about half of them buy; and a non-starter is worth a waived fee rather than a one-star review.
  applies_when: >-
    The mid-trial or end-of-trial meeting of a Trial With Penalty.
  structure:
    - >-
      1) If they like it: meet with them anyway and offer a longer term or higher value version of your service (or both).
    - >-
      2) If they hate it: ask what they would have liked to be different, take the blame, and offer your higher level thing.
    - >-
      3) If they didn't use it: reach out multiple times, explain that you need to meet with them, and offer to waive the fee if they do.
  anchor: >-
    **How I Upsell From A Trial.** When someone takes a trial, one of three
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, lines 4374-4405
  confirmations: 6
  anchor_at: "100m-money-models.md:4374"
  tier: 1
  merged_from: [B-money-models-098, B-money-models-099, D-money-models-059, D-money-models-060]
- id: A-money-models-022
  type: framework
  name: >-
    The Feature Downsell formula
  statement: >-
    Take something away, lower the price, and in so many words ask "how about now?"; the levers are lesser quantity, lower quality, lower price alternatives, or cutting optional components, and features are removed from highest to lowest value.
  why: >-
    People weigh how much money they save against how much value they lose, so they see the value in what was removed only after they see the price difference; removing high-value features first makes many customers re-upsell themselves onto the more expensive offer.
  applies_when: >-
    You want to charge less without discounting, that is, without selling the same stuff cheaper.
  structure:
    - >-
      Lesser quantity
    - >-
      Lower quality
    - >-
      Lower price alternatives
    - >-
      Cutting optional components
  anchor: >-
    Feature Downsells have a simple formula: take something away, lower the
  source: >-
    100m-money-models.md, Feature Downsells, Description and Summary Points, lines 4557-4783
  confirmations: 3
  authors_caveat: >-
    If you remove stuff they hate and lower the price a lot, more people take the downsell; if you remove stuff they love and lower the price a little, more people take the original offer.
  anchor_at: "100m-money-models.md:4586"
  tier: 1
  merged_from: [B-money-models-104]
- id: A-money-models-024
  type: framework
  name: >-
    How I Standardize My Downsell Process
  statement: >-
    Cut something valuable and lower the price a little first, then keep removing features and lowering prices until they buy, and after two changes in a row check on a scale of 1-10 whether they still want the thing.
  why: >-
    The first cut exists to get them to reconsider the original offer and price, the rest exist to find the best deal for them, and the author would rather people get something rather than nothing; no downsell will satisfy a customer who doesn't want the thing.
  applies_when: >-
    Running Feature Downsells once you know what your customers find most valuable.
  structure:
    - >-
      First, I cut something valuable and lower the price a little. I do this to get them to reconsider the original offer/price.
    - >-
      If that fails, I continue removing features and lowering prices until they buy.
    - >-
      Temperature check after two downsells: "On a scale from 1--10 how bad do you want this?" 8 or above, start payment plan downselling; 7 or below, ask "What would a 10 look like?" and recombine the features.
  anchor: >-
    **How I Standardize My Downsell Process.** First, I cut something
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, lines 4701-4729
  confirmations: 2
  authors_caveat: >-
    The first two elements are the author's own two-step description; the third is taken from the adjacent note "Temperature Check After Two Downsells (Like Payment Plans)" rather than from one numbered list.
  anchor_at: "100m-money-models.md:4701"
  tier: 1
  merged_from: [B-money-models-107]
- id: A-money-models-027
  type: framework
  name: >-
    Pricing For Continuity vs. Up Front Cash
  statement: >-
    The share of buyers who choose continuity over a standalone purchase tracks the ratio between the two prices: 1.33x gives 50%, 1.66x gives 60%, 2x gives 70%, 2.33x gives 80% and 2.66x gives 90% (figures as published in 2025).
  why: >-
    The smaller the standalone price compared to the continuity price, the more people buy the standalone; the larger the standalone price, the more people choose continuity — so the ratio is the dial between up front cash today and recurring revenue tomorrow.
  applies_when: >-
    Setting the price of a standalone (bonus-only) option next to a continuity offer.
  structure:
    - >-
      To get 50% to choose continuity make the standalone offer 1.33x more.
    - >-
      To get 60% to choose continuity make the standalone offer 1.66x more.
    - >-
      To get 70% to choose continuity make the standalone offer 2x more.
    - >-
      To get 80% to choose continuity make the standalone offer 2.33x more.
    - >-
      To get 90% to choose continuity make the standalone offer 2.66x more.
  anchor: >-
    To get 50% to choose continuity make the standalone offer 1.33x more.
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, lines 5142-5165
  confirmations: 2
  authors_caveat: >-
    The exact numbers matter less than the principle; the author gives them as his own tested range.
  anchor_at: "100m-money-models.md:5142"
  tier: 1
  merged_from: [B-money-models-127]
- id: A-money-models-028
  type: framework
  name: >-
    The four ways to apply a continuity discount
  statement: >-
    A one-time continuity discount can be applied up front, at the end, spread evenly over the term, or after the first one or two payments.
  why: >-
    The placement trades conversion against churn and cash: frontloaded discounts convert more customers but may have higher churn, backloaded discounts convert fewer but lower churn, spreading keeps cash flowing while providing the full discount, and taking one or two payments first covers advertising and delivery costs and proves the card works.
  applies_when: >-
    Giving free time or product in exchange for a longer commitment.
  structure:
    - >-
      Up Front. You apply the discount up front and push out the term.
    - >-
      At The End. So long as they make every payment on time they get bonus time equal to the value of the discount. They earn their free time.
    - >-
      Spread Over Time. Apply the discount across the term.
    - >-
      After the first 1--2 payments. They pay a few times and then they get their one-time discount.
  anchor: >-
    **I discount in four ways:** Up front, at the end, an even spread, or
  source: >-
    100m-money-models.md, Continuity Discount Offers, Examples and Summary Points, lines 5328-5504
  confirmations: 5
  authors_caveat: >-
    Up Front works best in industries with a successful history of enforcing contracts; if you have historically high churn, skip it, and note that it gets customers but delays cash.
  anchor_at: "100m-money-models.md:5328"
  tier: 1
  merged_from: [B-money-models-138, D-money-models-075, D-money-models-076]
- id: A-money-models-029
  type: framework
  name: >-
    The structure of a Waived Fee Offer
  statement: >-
    Ask for a startup fee of 3-5x the monthly rate as part of a month-to-month program, waive the entire fee if they commit longer term, and charge the fee if they cancel inside the term.
  why: >-
    Customers will stay longer if leaving costs more than staying: fees get them to start because committing immediately avoids a fee, and fees get them to stick because the cost of quitting exceeds the cost of staying.
  applies_when: >-
    Continuity businesses, for commitments of one year and longer, especially services that take a long time to work.
  structure:
    - >-
      First, you ask the customer to pay a startup fee as part of joining a month-to-month program. Typically, I do 3--5x my monthly rate.
    - >-
      Then, you offer to discount the entire fee if they commit longer term.
    - >-
      But, if they cancel inside the term, they pay the fee.
  anchor: >-
    Waived Fee Offers work like this. First, you ask the customer to pay a
  source: >-
    100m-money-models.md, Waived Fee Offer, Description, lines 5594-5610
  confirmations: 5
  authors_caveat: >-
    Pricing incentivizes sticking but can't and shouldn't overcome a terrible product; if more than 5% of people want to cancel early, look into it. If someone stays the entirety of their commitment, the fee officially goes away.
  anchor_at: "100m-money-models.md:5594"
  tier: 1
  merged_from: [B-money-models-142, B-money-models-143, D-money-models-082]
- id: A-money-models-031
  type: framework
  name: >-
    How Money Models evolve
  statement: >-
    The order of development is: get customers reliably, then make sure they pay for themselves, then make sure they pay for other customers, then maximize each customer's long-term value, then spend as much on advertising as you can.
  why: >-
    The author makes sure each stage pays for the next, and each stage is improved until it becomes reliable both financially and operationally.
  applies_when: >-
    Sequencing the work on a money model over quarters rather than weeks.
  structure:
    - >-
      First, I get customers reliably then
    - >-
      I make sure they pay for themselves reliably then
    - >-
      I make sure they pay for other customers reliably then
    - >-
      I start maximizing each customer's long-term value then
    - >-
      I spend as many advertising dollars as I can to print as much money as possible.
  anchor: >-
    ● I make sure they pay for other customers reliably *then*
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, Description, lines 5843-5862
  confirmations: 2
  authors_caveat: >-
    When your Money Model starts working, your business starts breaking; that is part of the game.
  anchor_at: "100m-money-models.md:5849"
  tier: 1
- id: A-money-models-032
  type: framework
  name: >-
    Make Your Own Money Model — the four steps
  statement: >-
    Start with an Attraction Offer, then pick an Upsell Offer, then a Downsell Offer, then a Continuity Offer, each with its own goal.
  why: >-
    Each step has a defined goal: cover the cost of getting the customer, push 30-day profits well above the cost of getting and delivering, convert the nos from the same number of leads, then take one last sale in the 30-day window and stack recurring cash.
  applies_when: >-
    Building a money model from scratch.
  structure:
    - >-
      Step 1) Start With An Attraction Offer. The goal is to turn strangers into customers and cover our costs.
    - >-
      Step 2) Pick An Upsell Offer. The goal is to get 30-day profits well above our costs of getting a new customer and delivering what you offer to them.
    - >-
      Step 3) Pick A Downsell Offer. The goal is to get customers who said no to your last offer to say yes to another offer.
    - >-
      Step 4) Pick A Continuity Offer. The goal here is to get one last sale in our 30-day window and stack recurring cash.
  anchor: >-
    **Step 1) Start With An Attraction Offer**. The goal is to turn
  source: >-
    100m-money-models.md, Section VI, Make Your Own Money Model, lines 5968-6005
  confirmations: 3
  authors_caveat: >-
    Perfect one offer at a time: do not try and implement a full Money Model at once, it will break your business. Sometimes the best timing for Continuity Offers happens after the first thirty days, and that's OK.
  anchor_at: "100m-money-models.md:5968"
  tier: 1
  merged_from: [B-money-models-159]
- id: A-money-models-033
  type: framework
  name: >-
    Money Model, a good Money Model, a $100M Money Model
  statement: >-
    Three levels: a Money Model is a series of offers; a good one makes more profit from a customer than it costs to get and service them in the first 30 days; a $100M one makes more profit from one customer than it costs to get and service many customers in the first 30 days.
  why: >-
    The first 30-day threshold is the bare minimum for a business to work at all; clearing it many times over removes cash as a limiter to scaling.
  applies_when: >-
    Judging whether an existing money model is good enough.
  structure:
    - >-
      A Money Model is a series of offers designed to increase how many customers you get, how much they pay, and how fast they pay it.
    - >-
      A good Money Model makes more profit from a customer than it costs to get and service them in the first 30 days. That's the bare minimum.
    - >-
      A $100M Money Model makes more profit from one customer than it costs to get and service many customers in the first 30 days, which removes cash as a limiter to scaling your business.
  anchor: >-
    **A good Money Model** *makes more profit from a customer than it
  source: >-
    100m-money-models.md, Ten Years In Ten Minutes, lines 6161-6175
  confirmations: 4
  anchor_at: "100m-money-models.md:6166"
  tier: 1
  merged_from: [B-money-models-149, D-money-models-001]
```


## B. Правила и критерии — 99

```yaml
- id: B-money-models-001
  type: rule
  name: >-
    Offer at the moment of realization
  statement: >-
    Each offer in the sequence is placed at the moment the customer realizes they have the problem it solves, not earlier or later.
  why: >-
    Money Models find every opportunity to solve a customer's problem and then offer to solve it; timed right, the number of offers you can make is unlimited.
  anchor: >-
    order. If you offer the right thing when customers realize they need it,
  source: >-
    100m-money-models.md, Section I: What's A Money Model?, line 753
  confirmations: 7
  anchor_at: "100m-money-models.md:753"
  tier: 1
  merged_from: [B-money-models-002, B-money-models-157, D-money-models-007, D-money-models-035]
- id: B-money-models-005
  type: rule
  name: >-
    If A Customer Asks For Their Money Back, Give It Back
  statement: >-
    A customer who asks for a refund gets it, whether or not the request is justified.
  why: >-
    If someone does not want you to have their money, you want it less than they do; the effort belongs on getting the next customer instead of on the headache.
  anchor: >-
    asks for a refund---entitled or not---*I give it to them.* Just focus on
  source: >-
    100m-money-models.md, Win Your Money Back, Important Notes, line 1265
  confirmations: 3
  anchor_at: "100m-money-models.md:1265"
  tier: 1
  merged_from: [D-money-models-006]
- id: B-money-models-010
  type: rule
  name: >-
    Refund rate below 5%
  statement: >-
    A Win Your Money Back Offer is only used when the business's refund rate is below 5%.
  why: >-
    Above that you risk giving too many refunds, and the product has to be fixed before the offer runs.
  anchor: >-
    ● Only use a Win Your Money Back Offer if your refund rate is below 5%.
  source: >-
    100m-money-models.md, Win Your Money Back, Summary Points, line 1416
  confirmations: 2
  anchor_at: "100m-money-models.md:1416"
  tier: 1
  merged_from: [D-money-models-015]
- id: B-money-models-011
  type: rule
  name: >-
    Only offer it if you are OK giving money back
  statement: >-
    The offer is run only if the business can stomach roughly 10% of all customers asking for their money back.
  why: >-
    Data from thousands of gyms puts money-back requests at about 10% of customers (2025); when advertised well the extra customers and the follow-up offer more than outweigh the refunds.
  anchor: >-
    we've collected from thousands of gyms, about 10% of all customers will
  source: >-
    100m-money-models.md, Win Your Money Back, Important Notes, line 1251
  confirmations: 2
  anchor_at: "100m-money-models.md:1251"
  tier: 1
  merged_from: [D-money-models-012]
- id: B-money-models-012
  type: rule
  name: >-
    Store credit advertised as free carries an unconditional guarantee
  statement: >-
    If winnings are paid in store credit but the offer is still advertised as free, the offer is paired with an unconditional satisfaction guarantee.
  why: >-
    Testing showed store credit and cash back pull the same number of customers, and adding the unconditional guarantee never materially changed how many people asked for their money back.
  anchor: >-
    as 'free,' pair it with an unconditional satisfaction guarantee. Adding
  source: >-
    100m-money-models.md, Win Your Money Back, Important Notes, line 1258
  confirmations: 1
  authors_caveat: >-
    Check with legal counsel in your area.
  anchor_at: "100m-money-models.md:1258"
  tier: 1
- id: B-money-models-013
  type: rule
  name: >-
    How You Apply Store Credit
  statement: >-
    Winnings are applied to something that costs more than the winnings and spread over a longer period, not handed back as free months up front.
  why: >-
    People fall off if they do not pay something, so a discount over the long haul keeps them engaged over the long haul and makes you more money.
  applies_when: >-
    A customer has won their money back as store credit.
  anchor: >-
    Just offer to apply it to something that costs more than their winnings.
  source: >-
    100m-money-models.md, Win Your Money Back, Important Notes, line 1304
  confirmations: 3
  authors_caveat: >-
    They can use the credit however they want; this is only what you present first.
  anchor_at: "100m-money-models.md:1304"
  tier: 1
  merged_from: [D-money-models-013]
- id: B-money-models-014
  type: rule
  name: >-
    All Meetings And Calls Provide Opportunities To Make More Offers
  statement: >-
    Check-in meetings are written into the money-back criteria and attendance at all of them is required to win.
  why: >-
    Beyond helping the customer succeed, the meetings are the best opportunities to make upsell offers based on the customer's feedback.
  anchor: >-
    Make check-in meetings part of your money-back criteria whenever you
  source: >-
    100m-money-models.md, Win Your Money Back, Important Notes, line 1333
  confirmations: 2
  anchor_at: "100m-money-models.md:1333"
  tier: 1
- id: B-money-models-015
  type: rule
  name: >-
    Make Everyone A Winner
  statement: >-
    The program is sold as if the money comes back only on meeting the criteria, but about halfway through the next offer is made as if the customer has already won.
  why: >-
    It lowers the customer's anxiety about failing, keeps them longer and makes them like you more.
  anchor: >-
    through, make your next offer *as if they already won*. You lower the
  source: >-
    100m-money-models.md, Win Your Money Back, Important Notes, line 1354
  confirmations: 2
  anchor_at: "100m-money-models.md:1354"
  tier: 1
- id: B-money-models-016
  type: rule
  name: >-
    At The End Of The Program, Let The Losers Win
  statement: >-
    A customer who refuses the first upsell and fails the challenge is still upsold, by crediting their entire deposit toward staying long term.
  why: >-
    We do not get customers to make a sale, we make sales to get customers.
  anchor: >-
    your first upsell *and* fails the challenge, you can *still* upsell them
  source: >-
    100m-money-models.md, Win Your Money Back, Important Notes, line 1366
  confirmations: 1
  anchor_at: "100m-money-models.md:1366"
  tier: 1
- id: B-money-models-017
  type: rule
  name: >-
    Pick A Grand Prize
  statement: >-
    The Grand Prize is the thing you want everyone to buy, and it carries a stated monetary value that serves as the price anchor.
  why: >-
    Everyone who enters has shown interest in that thing, and the stated value is what makes the later discounted price look like savings.
  anchor: >-
    everyone to buy.* Make sure you assign a monetary value to your grand
  source: >-
    100m-money-models.md, Giveaways, Description, line 1536
  confirmations: 2
  anchor_at: "100m-money-models.md:1536"
  tier: 1
- id: B-money-models-018
  type: rule
  name: >-
    Pick Your Promotional Offer
  statement: >-
    Everyone who does not win is offered the core offer enhanced by a discount, a bonus or a minor change from the Grand Prize that ethically justifies the price reduction.
  why: >-
    The Grand Prize works as the price anchor, and the bigger the discount against it, the more compelling the offer.
  anchor: >-
    your core offer with a discount, a bonus, or by minorly changing it from
  source: >-
    100m-money-models.md, Giveaways, Description, line 1542
  confirmations: 2
  anchor_at: "100m-money-models.md:1542"
  tier: 1
- id: B-money-models-019
  type: rule
  name: >-
    Put The Giveaway On A Deadline To Add Urgency
  statement: >-
    The giveaway runs three to seven days from the start of promotion, with a daily update to entrants across all platforms until the winner is announced.
  why: >-
    A limited window adds urgency, and the daily countdown plus social proof keeps the hype alive.
  anchor: >-
    available for a limited time. I like three to seven days from the day I
  source: >-
    100m-money-models.md, Giveaways, Description, line 1571
  confirmations: 2
  anchor_at: "100m-money-models.md:1571"
  tier: 1
- id: B-money-models-021
  type: rule
  name: >-
    Explain The Cost-To-Value Using Their Discount
  statement: >-
    The discount on the core offer is set at 10%-30% of gross margins, and it is explained to the lead as the gap between the Grand Prize value and the price they pay.
  why: >-
    Compared against the value of the thing, a 10% discount off retail becomes a 64% difference in cost-to-value (2025 figures).
  anchor: >-
    thumb: make your core offer discount equal to 10%--30% of your gross
  source: >-
    100m-money-models.md, Giveaways, Description, line 1600
  confirmations: 1
  anchor_at: "100m-money-models.md:1600"
  tier: 1
- id: B-money-models-023
  type: rule
  name: >-
    Cap entries at what you can call
  statement: >-
    The giveaway is advertised for seven days or until entries exceed the number of people you can call within seven days, whichever comes first.
  why: >-
    Any more entries than you have time and resources to connect with inside seven days would be a waste.
  anchor: >-
    ● Advertise your Giveaway for seven days, or until the number of leads
  source: >-
    100m-money-models.md, Giveaways, Summary Points, line 1736
  confirmations: 3
  anchor_at: "100m-money-models.md:1736"
  tier: 1
  merged_from: [D-money-models-019]
- id: B-money-models-026
  type: rule
  name: >-
    If You Have A Recurring Revenue Business
  statement: >-
    In a recurring business the giveaway discount is spread over the longest period the customer will agree to, with billing set to resume at normal rates afterwards.
  why: >-
    It keeps the subscription running at full price once the discounted period ends.
  anchor: >-
    the longest period of time they'll agree to. Then, set up their monthly
  source: >-
    100m-money-models.md, Giveaways, Important Notes, line 1706
  confirmations: 1
  anchor_at: "100m-money-models.md:1706"
  tier: 1
- id: B-money-models-027
  type: rule
  name: >-
    If Your Giveaway Doesn't Work, It Means Your Grand Prize Wasn't Grand Enough
  statement: >-
    When a giveaway gets little interest, the fix is a bigger or better-for-the-audience Grand Prize, not different advertising.
  why: >-
    Giveaway kind of explains itself, so if nobody bites the prize was not grand; a portfolio company swapped event tickets for a $50,000 equipment bundle plus a year of product and it crushed.
  anchor: >-
    if nobody bites, then I suggest you give away something better. Or at
  source: >-
    100m-money-models.md, Giveaways, Important Notes, line 1663
  confirmations: 2
  anchor_at: "100m-money-models.md:1663"
  tier: 1
  merged_from: [D-money-models-018]
- id: B-money-models-028
  type: rule
  name: >-
    Give Away Two Prizes For Twice The Leads
  statement: >-
    To get referrals, two grand prizes are given away and entrants are told that if someone they refer wins, they win one too.
  why: >-
    It gives endless entries through referrals and makes referrers invested in the success of the people they refer, which keeps lead quality high.
  anchor: >-
    ● Give two prizes away if you want more people to refer. Tell them if
  source: >-
    100m-money-models.md, Giveaways, Summary Points, line 1720
  confirmations: 2
  anchor_at: "100m-money-models.md:1720"
  tier: 1
- id: B-money-models-029
  type: rule
  name: >-
    How To Make Your Decoy Offer
  statement: >-
    The decoy is built from the premium offer by cutting components, using older models, removing personalization and removing every guarantee.
  why: >-
    The Attraction Offer only has to get leads to engage, nothing more.
  anchor: >-
    **How To Make Your Decoy Offer.** Offer fewer components, older models,
  source: >-
    100m-money-models.md, Decoy Offer, Important Notes, line 1924
  confirmations: 2
  anchor_at: "100m-money-models.md:1924"
  tier: 1
- id: B-money-models-032
  type: rule
  name: >-
    Discount Offers Have Higher Show-Up Rates Than Free Offers
  statement: >-
    A business with low appointment show-up rates runs a discount Attraction Offer instead of a free one.
  why: >-
    Free gets more leads, a discount gets fewer leads but a higher percentage who show up; that matters most where a no-show is expensive, as for doctors, lawyers and dentists.
  anchor: >-
    appointments, try a Discount Offer instead. This is especially important
  source: >-
    100m-money-models.md, Decoy Offer, Important Notes, line 1961
  confirmations: 2
  anchor_at: "100m-money-models.md:1961"
  tier: 1
  merged_from: [D-money-models-021]
- id: B-money-models-033
  type: rule
  name: >-
    If Possible, Present The Premium Offer First
  statement: >-
    The premium offer is presented first and the decoy is kept back unless the lead asks for it or the law requires it to be presented.
  why: >-
    In a perfect world they take the premium offer immediately and the decoy stays in your back pocket.
  anchor: >-
    **If Possible, Present The Premium Offer First.** In a perfect world,
  source: >-
    100m-money-models.md, Decoy Offer, Important Notes, line 1965
  confirmations: 2
  anchor_at: "100m-money-models.md:1965"
  tier: 1
- id: B-money-models-034
  type: rule
  name: >-
    Get Them To Give You Permission To Sell Them
  statement: >-
    When the decoy has to be presented, it is immediately contrasted with the premium offer, and only after both are on the table is the lead asked which will get them to their goal faster.
  why: >-
    At that point they have to name the premium offer, and you move forward in the sale mutually agreeing it is the best thing for them.
  applies_when: >-
    The lead asks for the decoy, or you are legally required to present it.
  anchor: >-
    contrast it with your premium offer. Then only after presenting both,
  source: >-
    100m-money-models.md, Decoy Offer, Important Notes, line 1981
  confirmations: 3
  anchor_at: "100m-money-models.md:1981"
  tier: 1
  merged_from: [D-money-models-022]
- id: B-money-models-035
  type: rule
  name: >-
    Raise Prices Before Giving Stuff Away To Preserve Profits
  statement: >-
    Prices are permanently and honestly raised to accommodate the giveaway before a Buy X Get Y Free offer runs.
  why: >-
    The offer will work, and since it will work you need to make money on it; new customers all come in on this price, so the change makes sense for at least a season.
  anchor: >-
    need to make money. So, *permanently* raise prices to accommodate the
  source: >-
    100m-money-models.md, Buy X Get Y Free, Important Notes, line 2157
  confirmations: 2
  authors_caveat: >-
    Don't lie. Actually raise your prices.
  anchor_at: "100m-money-models.md:2157"
  tier: 1
  merged_from: [D-money-models-025]
- id: B-money-models-036
  type: rule
  name: >-
    Give more free than paid
  statement: >-
    A Buy X Get Y Free offer gives more free items than the customer is asked to buy, so buy one get two beats buy two get one.
  why: >-
    Buy ten get two free is not as strong as buy two get ten free; it seems obvious, but people do not do it.
  anchor: >-
    ● Always try to give more free things than paid things.
  source: >-
    100m-money-models.md, Buy X Get Y Free, Summary Points, line 2259
  confirmations: 3
  anchor_at: "100m-money-models.md:2259"
  tier: 1
  merged_from: [D-money-models-026]
- id: B-money-models-038
  type: rule
  name: >-
    Make This Offer To Existing Customers For Fast Cash
  statement: >-
    When a Buy X Get Y Free offer is made to existing recurring customers for a cash pop, it is capped at 10% of the customer base.
  why: >-
    It gives a good cash pop while keeping recurring cash flow healthy.
  anchor: >-
    at their current price. Just limit the offer to 10% of your customers.
  source: >-
    100m-money-models.md, Buy X Get Y Free, Important Notes, line 2227
  confirmations: 3
  anchor_at: "100m-money-models.md:2227"
  tier: 1
  merged_from: [D-money-models-029]
- id: B-money-models-042
  type: rule
  name: >-
    Make a Conditional Satisfaction Guarantee
  statement: >-
    Cancelling the delayed charge is possible only for customers who met tracked conditions, and those conditions are the actions that get the most value out of the product.
  why: >-
    They cannot say you suck if they never tried it; aligning the conditions with value delivery makes it win-win.
  anchor: >-
    turning in data, etc. Make the criteria what people do to get the most
  source: >-
    100m-money-models.md, Pay Less Now or Pay More Later, Important Notes, line 2420
  confirmations: 2
  anchor_at: "100m-money-models.md:2420"
  tier: 1
- id: B-money-models-046
  type: rule
  name: >-
    If More Than 10% Of Pay Later People Cancel Their Payment
  statement: >-
    A cancellation rate above 10% on the pay later option means the promise was too big, the guarantee conditions too low or the price too high, and one of the three is changed.
  why: >-
    No matter how well you deliver, some people will cancel; above 10% the offer itself is at fault (2025 benchmark).
  anchor: >-
    **If More Than 10% Of 'Pay Later' People Cancel Their Payment**. You
  source: >-
    100m-money-models.md, Pay Less Now or Pay More Later, Important Notes, line 2434
  confirmations: 3
  anchor_at: "100m-money-models.md:2434"
  tier: 1
  merged_from: [D-money-models-032]
- id: B-money-models-050
  type: rule
  name: >-
    Offer More Profitable Upsells First
  statement: >-
    When two upsells are available, the one with the higher profit is offered first.
  why: >-
    The order of offers decides which profit you capture before the customer stops buying.
  anchor: >-
    **Offer More Profitable Upsells First.** If I offer two products and one
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2814
  confirmations: 1
  anchor_at: "100m-money-models.md:2814"
  tier: 1
- id: B-money-models-051
  type: rule
  name: >-
    Surprise And Delight
  statement: >-
    Closing bonuses are added one at a time, and everyone who buys receives all of them even if they said yes before the later ones were offered.
  why: >-
    It surprises and delights them, and it guarantees everyone gets the same thing so nobody feels left out later.
  anchor: >-
    add to get people who are on the fence to buy. Add one at a time. If
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2827
  confirmations: 1
  anchor_at: "100m-money-models.md:2827"
  tier: 1
- id: B-money-models-052
  type: rule
  name: >-
    The Faster People Get Access To Stuff, The More They'll Value It
  statement: >-
    The upsell is made available as soon as possible, ideally placed in the customer's hands before they have said yes.
  why: >-
    The longer it takes to access something, the less value it has in the moment, and it is far harder to give something back than to say no.
  anchor: >-
    upsell, make it available as soon as you can. Bonus points if you put it
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2852
  confirmations: 2
  anchor_at: "100m-money-models.md:2852"
  tier: 1
- id: B-money-models-054
  type: rule
  name: >-
    Integrate Upsells Into Your Other Offers
  statement: >-
    The thing you intend to sell next is built into the delivery of the thing they just bought.
  why: >-
    Meal plans that included supplement suggestions made people ask about supplements; training that suggested software led owners to buy it.
  anchor: >-
    buy them. Integrate the next thing you wanna sell into the first thing
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2870
  confirmations: 1
  anchor_at: "100m-money-models.md:2870"
  tier: 1
- id: B-money-models-055
  type: rule
  name: >-
    Book-A-Meeting-From-A-Meeting (BAMFAM)
  statement: >-
    Every appointment ends with the next appointment scheduled, with the reason and the time agreed before the customer leaves.
  why: >-
    The more times you can upsell, the more people you will upsell; a customer should know the next time they see you and why before they leave.
  anchor: >-
    by scheduling the next appointment. Don't let them leave without
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2876
  confirmations: 2
  anchor_at: "100m-money-models.md:2876"
  tier: 1
- id: B-money-models-057
  type: rule
  name: >-
    Upsell Guarantees, Warranties, and Insurance
  statement: >-
    Guarantees, warranties and insurance are sold as a 5-50% addition to the price instead of being included free.
  why: >-
    An art studio that used to replace damaged portraits free now has 30% of customers paying an extra 10% for it, which is pure profit (2025 figures).
  anchor: >-
    *So instead of doing it for free, just add 5--50% onto the price in
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2893
  confirmations: 9
  anchor_at: "100m-money-models.md:2893"
  tier: 1
  merged_from: [A-playbooks-price-014, B-playbooks-price-030, C-playbooks-price-024, C-playbooks-price-025, D-playbooks-price-033, D-playbooks-price-034, E-playbooks-price-015]
- id: B-money-models-058
  type: rule
  name: >-
    Card On File
  statement: >-
    Payment is asked for by asking whether they want to use the card on file, not by asking them to produce a card.
  why: >-
    It lowers the hidden costs of buying: picking a card, taking it out, being reminded of ugly past buying decisions; make it easy and more people buy.
  anchor: >-
    Last, I make buying easy by asking if they want to use the card on file.
  source: >-
    100m-money-models.md, Menu Upsell, Description, line 3095
  confirmations: 3
  anchor_at: "100m-money-models.md:3095"
  tier: 1
- id: B-money-models-059
  type: rule
  name: >-
    Prescription Upsell
  statement: >-
    A prescription upsell explains how the product integrates with what the customer already bought and gives personalized, detailed instructions for using it, instead of asking whether they want it.
  why: >-
    Explaining how to use it as if they already have it removes the option of not buying, which lowers the chance they do not buy.
  applies_when: >-
    Offering a choice is inconvenient and you have only one thing that solves the problem.
  anchor: >-
    important components. First, you have to explain how it integrates with
  source: >-
    100m-money-models.md, Menu Upsell, Description, line 3107
  confirmations: 2
  anchor_at: "100m-money-models.md:3107"
  tier: 1
- id: B-money-models-060
  type: rule
  name: >-
    A/B Upsell
  statement: >-
    Where several products solve the same problem, the customer is asked which of two they prefer rather than whether they want one.
  why: >-
    When you give people the option to not buy, some do not buy; either choice in an A/B question results in an upsell.
  anchor: >-
    asking their preference. Instead of asking ***if*** customers wanted to
  source: >-
    100m-money-models.md, Menu Upsell, Description, line 3116
  confirmations: 4
  anchor_at: "100m-money-models.md:3116"
  tier: 1
  merged_from: [D-money-models-040]
- id: B-money-models-062
  type: rule
  name: >-
    If You've Sold Out Of It, Take Payment And Delay Delivery
  statement: >-
    When stock runs out, the sale is still made and the delivery expectation is set instead of the offer being withdrawn.
  why: >-
    It lets you sell far more selection without carrying inventory.
  anchor: >-
    collecting the cash and changing the delivery expectations. You'd be
  source: >-
    100m-money-models.md, Menu Upsell, Important Notes, line 3226
  confirmations: 1
  anchor_at: "100m-money-models.md:3226"
  tier: 1
- id: B-money-models-063
  type: rule
  name: >-
    Employees Love Unselling
  statement: >-
    Employees are encouraged to help customers game the system on purpose by telling them what they do not need.
  why: >-
    Employees have inside knowledge, and using it to show customers how to get the most value means everyone wins.
  anchor: >-
    ● Encourage employees to unsell and "game the system" on purpose.
  source: >-
    100m-money-models.md, Menu Upsell, Summary Points, line 3259
  confirmations: 2
  anchor_at: "100m-money-models.md:3259"
  tier: 1
- id: B-money-models-064
  type: rule
  name: >-
    Unsell the lower-margin items
  statement: >-
    What gets crossed off the menu is the lower-margin stuff, so the prescription lands on the higher-margin items.
  why: >-
    Unselling lower-margin stuff where appropriate incentivizes higher-margin upsells.
  anchor: >-
    ● Unselling lower-margin stuff where appropriate incentivizes
  source: >-
    100m-money-models.md, Menu Upsell, Summary Points, line 3256
  confirmations: 1
  anchor_at: "100m-money-models.md:3256"
  tier: 1
- id: B-money-models-065
  type: rule
  name: >-
    If You Treat The Anchor Like A Fake, So Will The Customer
  statement: >-
    The premium anchor is genuinely sold and the conversation moves on only after the customer pauses, hesitates or asks for something else.
  why: >-
    If you go through the motions the person never really considered it, and you lose trust and waste time.
  anchor: >-
    hesitate, or ask for something else, do you move to the next thing.
  source: >-
    100m-money-models.md, Anchor Upsell, Important Notes, line 3404
  confirmations: 3
  anchor_at: "100m-money-models.md:3404"
  tier: 1
  merged_from: [D-money-models-043]
- id: B-money-models-067
  type: rule
  name: >-
    Premium offer at 5-10x
  statement: >-
    The anchor offer is priced 5-10x the main offer.
  why: >-
    At that gap lots of people say no to the anchor and the main offer then looks like a much better deal, while some customers still buy the anchor (2025 figures).
  anchor: >-
    ● For the most effective anchor, make your premium offer 5--10x more
  source: >-
    100m-money-models.md, Anchor Upsell, Summary, line 3453
  confirmations: 2
  anchor_at: "100m-money-models.md:3453"
  tier: 1
- id: B-money-models-068
  type: rule
  name: >-
    Same primary features, different secondary features
  statement: >-
    The main offer keeps the same primary features as the premium offer, and only secondary features are changed.
  why: >-
    Most people just want a suit; the material and designer are secondary, so offering the primary features for a fifth of the price makes the main offer a great deal.
  anchor: >-
    ● The main offer and the premium offer should have the same primary
  source: >-
    100m-money-models.md, Anchor Upsell, Summary, line 3465
  confirmations: 4
  anchor_at: "100m-money-models.md:3465"
  tier: 1
  merged_from: [D-money-models-042]
- id: B-money-models-070
  type: rule
  name: >-
    How To Price Your Rollover Upsell
  statement: >-
    The offer the credit rolls into is priced at least 4x the credit given.
  why: >-
    At 4x, applying the whole first purchase discounts the new offer by 25% at most, so profit is left after the discount.
  anchor: >-
    ● Price your next offer *at least* 4x higher than the credit. This makes
  source: >-
    100m-money-models.md, Rollover Upsell, Summary Points, line 3700
  confirmations: 4
  anchor_at: "100m-money-models.md:3700"
  tier: 1
  merged_from: [B-money-models-069, D-money-models-046]
- id: B-money-models-071
  type: rule
  name: >-
    Do Rollover Upsells before refunding
  statement: >-
    Before any refund is issued, the purchase is offered as credit toward a do-over or toward a different product.
  why: >-
    It has saved the author tons of customers and cash.
  anchor: >-
    **Do Rollover Upsells** ***before*** **refunding.** This has saved me
  source: >-
    100m-money-models.md, Rollover Upsell, Important Notes, line 3639
  confirmations: 3
  anchor_at: "100m-money-models.md:3639"
  tier: 1
  merged_from: [D-money-models-045]
- id: B-money-models-072
  type: rule
  name: >-
    Previous Customers Are Still Customers. Upsell Them.
  statement: >-
    Customers with six or more months since their last purchase are contacted with a rollover credit toward returning.
  why: >-
    200 personalized winback videos offering $4,000 of credit converted about 20% and produced roughly $1,900,000 of annual revenue from one day of recording (2025 figures).
  anchor: >-
    old customers (6+ months since last purchase). Look at how much they
  source: >-
    100m-money-models.md, Rollover Upsell, Important Notes, line 3645
  confirmations: 2
  anchor_at: "100m-money-models.md:3645"
  tier: 1
- id: B-money-models-073
  type: rule
  name: >-
    Add Urgency To Rollover Upsells. Make Them One-Time Only.
  statement: >-
    The rollover credit is a once-in-a-customer-lifetime offer that has to be taken at the moment it is presented.
  why: >-
    They do not get to sleep on it; the surprise is the point, and if they pass they can still pay full price later.
  anchor: >-
    **Add Urgency To Rollover Upsells. Make Them One-Time Only.** If you're
  source: >-
    100m-money-models.md, Rollover Upsell, Important Notes, line 3653
  confirmations: 2
  anchor_at: "100m-money-models.md:3653"
  tier: 1
- id: B-money-models-077
  type: rule
  name: >-
    Offer The Same Things In New Ways
  statement: >-
    Downsells are built out of what the business already sells, not out of new products created for the occasion.
  why: >-
    Otherwise you create a hundred businesses' worth of products and problems; downselling is a hundred ways to offer the stuff you already have.
  anchor: >-
    just think of downselling more like a hundred ways to offer the stuff
  source: >-
    100m-money-models.md, Section IV: Downsell Offers, The Rules of Downselling, line 3794
  confirmations: 3
  anchor_at: "100m-money-models.md:3794"
  tier: 1
  merged_from: [D-money-models-048]
- id: B-money-models-078
  type: rule
  name: >-
    Don't Drop Your Price Just To Get Somebody To Buy
  statement: >-
    The price of a thing is never lowered in the moment to win a sale; only the payment schedule or the contents of the offer change.
  why: >-
    Dropping the price is discounting, not downselling; customers talk, and someone finding out another got the same thing cheaper just because is both an upset and an ethical problem.
  anchor: >-
    do, don't change the price just to get someone to buy because...
  source: >-
    100m-money-models.md, Section IV: Downsell Offers, The Rules of Downselling, line 3802
  confirmations: 7
  anchor_at: "100m-money-models.md:3802"
  tier: 1
  merged_from: [B-money-models-105, D-money-models-049, D-money-models-064, D-money-models-067]
- id: B-money-models-079
  type: rule
  name: >-
    Customers Talk About Price
  statement: >-
    Price tests are planned in advance, fixing the price and the number of people it is offered to, rather than decided during a sales conversation.
  why: >-
    That is different from charging somebody less in the moment because you were scared of losing the sale.
  anchor: >-
    your thing at a specific price, to a specific number of people, *ahead
  source: >-
    100m-money-models.md, Section IV: Downsell Offers, The Rules of Downselling, line 3805
  confirmations: 1
  anchor_at: "100m-money-models.md:3805"
  tier: 1
- id: B-money-models-080
  type: rule
  name: >-
    Reward For Paying In Full Rather Than Punish For Paying Over Time
  statement: >-
    The price is quoted with the interest already included and prepayment is offered as a discount, instead of adding interest to a payment plan.
  why: >-
    Same math, but it feels better: the offer is friendlier and the full price works as a price anchor.
  anchor: >-
    *with interest included*. Then, I offer prepayment as a way to get a
  source: >-
    100m-money-models.md, Payment Plan Downsells, Example Of Payment Plan Downsell Process, line 3948
  confirmations: 3
  anchor_at: "100m-money-models.md:3948"
  tier: 1
  merged_from: [D-money-models-052]
- id: B-money-models-081
  type: rule
  name: >-
    Schedule payments on paycheck dates
  statement: >-
    Payment dates are scheduled against the customer's paycheck dates rather than as monthly instalments.
  why: >-
    Most people get paid every two weeks, which boosts 30-day profit far more than monthly payments, and charging on payday means fewer declines.
  anchor: >-
    paid. Fair enough?"* I like scheduling payments off of paychecks since
  source: >-
    100m-money-models.md, Payment Plan Downsells, Example Of Payment Plan Downsell Process, line 3984
  confirmations: 3
  anchor_at: "100m-money-models.md:3984"
  tier: 1
- id: B-money-models-082
  type: rule
  name: >-
    Get Fewer Declined Payments
  statement: >-
    A declined card is re-run several times over the same day rather than treated as a failed payment.
  why: >-
    Paychecks get deposited at different times; the author recoups about a third of declined payments with this step, learned from John, an early mentor.
  anchor: >-
    times, so if at first it gets declined, run it a few times that day. I
  source: >-
    100m-money-models.md, Payment Plan Downsells, Important Notes, line 4052
  confirmations: 1
  anchor_at: "100m-money-models.md:4052"
  tier: 1
- id: B-money-models-083
  type: rule
  name: >-
    Check To See If They Still Want The Thing
  statement: >-
    After the payment plan options run out, the customer is asked on a 1-10 scale how badly they want it, and payment plans continue only at 8 or above.
  why: >-
    No payment plan will satisfy a customer who does not want the thing, so effort is only spent where the desire is there.
  anchor: >-
    wanna do this?"* If they say 8 or above, keep offering payment plans and
  source: >-
    100m-money-models.md, Payment Plan Downsells, Example Of Payment Plan Downsell Process, line 3995
  confirmations: 6
  anchor_at: "100m-money-models.md:3995"
  tier: 1
  merged_from: [B-money-models-084, B-money-models-110, B-money-models-111, D-money-models-053]
- id: B-money-models-085
  type: rule
  name: >-
    How To Make Sure Payment Plans Make You Money
  statement: >-
    After payment plans are introduced, the share of appointments paying in full must stay the same while the overall close rate rises.
  why: >-
    If the number of paid-in-fulls drops you have put people who would have paid in full onto payment plans, which is where payment plans lose the most money.
  anchor: >-
    appointments overall but with the same percentage of appointments paying
  source: >-
    100m-money-models.md, Payment Plan Downsells, Important Notes, line 4060
  confirmations: 3
  anchor_at: "100m-money-models.md:4060"
  tier: 1
  merged_from: [D-money-models-050]
- id: B-money-models-086
  type: rule
  name: >-
    Start High Before Working Your Way Down
  statement: >-
    Pricing is always presented in order from most cash up front to least.
  why: >-
    Profitwell churn data from 14,000 businesses: monthly billing gave 10.7% monthly cancellations, quarterly 5%, annual 2%, so fewer bigger payments also make customers more valuable long term (2025 citation).
  anchor: >-
    term. So start high (fewer bigger payments) and work your way down.
  source: >-
    100m-money-models.md, Payment Plan Downsells, Important Notes, line 4084
  confirmations: 3
  anchor_at: "100m-money-models.md:4084"
  tier: 1
  merged_from: [B-playbooks-price-023]
- id: B-money-models-087
  type: rule
  name: >-
    Payment Plans Have Built-In Upsells
  statement: >-
    Customers on a payment plan are periodically offered the original paid-in-full discount if they clear the balance.
  why: >-
    Customers forget they have the option and some jump at it; if you incentivize people to pay faster, they pay faster.
  anchor: >-
    off the balance, they can still get the original 'prepay discount.' This
  source: >-
    100m-money-models.md, Payment Plan Downsells, Important Notes, line 4041
  confirmations: 2
  anchor_at: "100m-money-models.md:4041"
  tier: 1
- id: B-money-models-089
  type: rule
  name: >-
    Trial criteria activate and retain customers
  statement: >-
    The terms of a Trial With Penalty are criteria that activate and retain customers, taken from the Win Your Money Back criteria.
  why: >-
    By the end of the trial they have done the things that make great long-term customers and that advertise the business for free.
  anchor: >-
    rather than giving less---if you can afford it. The criteria should
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4286
  confirmations: 3
  anchor_at: "100m-money-models.md:4286"
  tier: 1
- id: B-money-models-090
  type: rule
  name: >-
    Offer The Trial Last
  statement: >-
    The Trial With Penalty is offered only after the customer has made clear they will not take the first offer.
  why: >-
    Used as a downsell it changes only what they pay today, not what they pay in total, and it saves the people who would otherwise be lost to a no.
  anchor: >-
    **Offer The Trial Last.** If someone makes it clear they don\'t want
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4303
  confirmations: 4
  anchor_at: "100m-money-models.md:4303"
  tier: 1
  merged_from: [D-money-models-055]
- id: B-money-models-091
  type: rule
  name: >-
    Always Get A Credit Card
  statement: >-
    No trial starts without a card on file; a customer who refuses to leave one is shown out.
  why: >-
    The penalty mechanism only exists if there is a card to charge; if they balk, the answer is that this is just how we have always done it.
  anchor: >-
    we've always done it."* If they still refuse, wish them a lovely day and
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4317
  confirmations: 3
  anchor_at: "100m-money-models.md:4317"
  tier: 1
  merged_from: [D-money-models-056]
- id: B-money-models-092
  type: rule
  name: >-
    Always Sell Staying And Paying
  statement: >-
    Before the trial begins the customer agrees out loud that they will stay long term if the program gets them the result; without that agreement no trial is given.
  why: >-
    There is no point giving a trial to someone who will not stay, and setting the expectation keeps you from promising a quick fix you cannot ethically deliver.
  anchor: >-
    staying long-term if you get them results. If they say no, there's no
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4326
  confirmations: 3
  anchor_at: "100m-money-models.md:4326"
  tier: 1
  merged_from: [D-money-models-057]
- id: B-money-models-093
  type: rule
  name: >-
    Explain the fees after getting their card
  statement: >-
    The penalty fees are explained after the card has been taken, not before.
  why: >-
    Explaining the fees before you get the card brings more resistance; explained afterwards, with a this-is-how-we-have-always-done-it attitude, the take rate is higher.
  anchor: >-
    **Explain the fees** ***after*** **getting their card.** I say something
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4346
  confirmations: 3
  anchor_at: "100m-money-models.md:4346"
  tier: 1
  merged_from: [D-money-models-058]
- id: B-money-models-094
  type: rule
  name: >-
    Initial next to the fee clauses
  statement: >-
    Customers initial separately next to the fee clauses in the agreement.
  why: >-
    It forces the sales team to explain them; people still have to agree to the fees.
  anchor: >-
    initial separately next to the fee clauses to force my sales guys to
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4359
  confirmations: 2
  anchor_at: "100m-money-models.md:4359"
  tier: 1
- id: B-money-models-095
  type: rule
  name: >-
    Make Check-ins Required
  statement: >-
    All criteria are explained up front and the check-in meetings are made required terms of the trial, with the benefit of each one named.
  why: >-
    The check-ins are the upsell opportunities, and charging for missing them is the only way to get the customer results.
  anchor: >-
    **Make Check-ins Required.** First, we explain *all* criteria so they
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4366
  confirmations: 2
  anchor_at: "100m-money-models.md:4366"
  tier: 1
- id: B-money-models-096
  type: rule
  name: >-
    Breaking Up Fees vs. One Lump Fee
  statement: >-
    The penalty is split into a small fee per missed criterion rather than one lump fee on the first miss.
  why: >-
    The author prefers billing $50 for each mess up over one $500 fee; a lump fee fits only where missing once really ruins the customer's result.
  anchor: >-
    ten things to do. I'd rather bill \$50 for each mess up than one \$500
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4291
  confirmations: 2
  authors_caveat: >-
    I've seen both work.
  anchor_at: "100m-money-models.md:4291"
  tier: 1
- id: B-money-models-097
  type: rule
  name: >-
    Tweak Your Trial To Get The Most Customers
  statement: >-
    If nobody takes the trial, the requirements or penalties are lowered; if people take it but do not follow through, the explanation of how the fees help them is strengthened and sales meetings are made mandatory.
  why: >-
    Each failure mode of the trial points at a specific part of the offer to change.
  anchor: >-
    Trial, lower the requirements or penalties. If people take your Trial
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4408
  confirmations: 2
  anchor_at: "100m-money-models.md:4408"
  tier: 1
  merged_from: [D-money-models-061]
- id: B-money-models-100
  type: rule
  name: >-
    Let People Make Up For Goofs
  statement: >-
    A customer who has been billed for a miss is offered a way to make it up; only if they miss that too is the billing justified.
  why: >-
    People get discouraged after getting billed, and the make-up gets them back on track and converting.
  anchor: >-
    getting billed. But, you can offer an opportunity to 'make it up.' This
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4417
  confirmations: 1
  anchor_at: "100m-money-models.md:4417"
  tier: 1
- id: B-money-models-101
  type: rule
  name: >-
    Just Call It A Trial
  statement: >-
    The offer is called a Free Trial in all customer-facing language, never a trial with a penalty.
  why: >-
    Otherwise people get scared and confused; nobody wants to be penalized.
  anchor: >-
    'special features,' you should just call it a Free Trial. Otherwise,
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4422
  confirmations: 2
  anchor_at: "100m-money-models.md:4422"
  tier: 1
  merged_from: [D-money-models-062]
- id: B-money-models-102
  type: rule
  name: >-
    Pay Less Now or Pay More Later vs. Trial With Penalty
  statement: >-
    Pay Less Now or Pay More Later is the downsell for physical products and one-time services; Trial With Penalty is the downsell for recurring products and services.
  why: >-
    That is how the author has made each of them work.
  anchor: >-
    one-time services. And I use Trial With Penalty as a downsell for
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4430
  confirmations: 2
  authors_caveat: >-
    I have only made this work in businesses where the customer has to do work to get results.
  anchor_at: "100m-money-models.md:4430"
  tier: 1
  merged_from: [D-money-models-063]
- id: B-money-models-103
  type: rule
  name: >-
    Discounts Get Cards on File
  statement: >-
    Where asking for a card against a free offer meets resistance, a very low first-month price is charged instead of nothing.
  why: >-
    The small price means the card will probably work when the automatic payments start.
  anchor: >-
    probably work when the automatic payments start. So instead of a free
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4438
  confirmations: 1
  anchor_at: "100m-money-models.md:4438"
  tier: 1
- id: B-money-models-109
  type: rule
  name: >-
    Name the cheapest combination The Minimum
  statement: >-
    The cheapest package is called The Minimum, and a customer who rejects everything else is asked whether they want nothing more than the minimum package.
  why: >-
    The name implies they have to get at least that thing, and the question gets them to say no in order to say yes, as in the Classic Upsell.
  anchor: >-
    **I Name My Cheapest Combination "The Minimum."** I like it because it
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4714
  confirmations: 1
  anchor_at: "100m-money-models.md:4714"
  tier: 1
- id: B-money-models-113
  type: rule
  name: >-
    Free Orientations Boost Do-It-Yourself Feature Downsells
  statement: >-
    A lead who has refused every done-for-you offer is invited to a free orientation, at the end of which a do-it-yourself product solving the same problem is offered.
  why: >-
    About half of those invited showed up and almost all of them bought supplements, which is money from people who would otherwise have said no.
  anchor: >-
    orientation, I offer a DIY product that solves the same problem as the
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4741
  confirmations: 1
  anchor_at: "100m-money-models.md:4741"
  tier: 1
- id: B-money-models-114
  type: rule
  name: >-
    Feature Downsell Your Guarantees
  statement: >-
    If the offer has a guarantee, removing it is a standard step of the Feature Downsell process.
  why: >-
    People value security, so removing the guarantee makes many of them see its value and flips an initial no back to a yes on the full-price offer.
  anchor: >-
    make removing it part of your Feature Downsell process. People value
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4749
  confirmations: 2
  anchor_at: "100m-money-models.md:4749"
  tier: 1
- id: B-money-models-115
  type: rule
  name: >-
    Feature Downsell Current Customers
  statement: >-
    A current customer who is not using a feature is offered a lower price for only the features they use, before they cancel.
  why: >-
    Customers who use all the features they pay for stay longer; customers downsold into a package just for them have the second highest value of all the author's customers.
  anchor: >-
    you see a customer isn't using a feature, offer a lower price---only
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4755
  confirmations: 2
  anchor_at: "100m-money-models.md:4755"
  tier: 1
- id: B-money-models-117
  type: rule
  name: >-
    Make Continuity Offers last
  statement: >-
    Continuity is offered after the Attraction, Upsell and Downsell offers, not used as the Attraction Offer on its own.
  why: >-
    Continuity attracts more customers but crashes 30-day profits; placed last it takes cash today from the other offers and stacks recurring cash for tomorrow.
  anchor: >-
    By making continuity offers *last,* we get the best of all worlds. We
  source: >-
    100m-money-models.md, Section V: Continuity Offers, line 4885
  confirmations: 4
  authors_caveat: >-
    You can make Continuity Offers wherever and however you want; they can attract, upsell, downsell or re-engage.
  anchor_at: "100m-money-models.md:4885"
  tier: 1
  merged_from: [D-money-models-068]
- id: B-money-models-118
  type: rule
  name: >-
    Ongoing value means ongoing payments
  statement: >-
    Something is put on continuity only when the customer keeps getting ongoing value from it; a one-off deliverable paid for over time is a payment plan, not continuity.
  why: >-
    It is silly for someone to pay for a one-day workshop forever, and equally a mistake to charge one price to provide a service forever.
  anchor: >-
    get ongoing value, it probably makes sense for them to make ongoing
  source: >-
    100m-money-models.md, Section V: Continuity Offers, line 4899
  confirmations: 3
  anchor_at: "100m-money-models.md:4899"
  tier: 1
  merged_from: [D-money-models-069, D-money-models-070]
- id: B-money-models-119
  type: rule
  name: >-
    The bonus outweighs the first continuity payment
  statement: >-
    The sign-up bonus on a Continuity Offer is worth more than the first continuity payment.
  why: >-
    That is what makes people start; more good stuff added and costs taken away gets more people onto continuity.
  anchor: >-
    sign up today. Typically, the bonus itself has more value than the first
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Description, line 4992
  confirmations: 2
  anchor_at: "100m-money-models.md:4992"
  tier: 1
- id: B-money-models-120
  type: rule
  name: >-
    Focus On The Bonus, Not The Membership
  statement: >-
    The advertising for a Continuity Offer sells the free valuable thing, and the membership is explained only after the lead shows interest.
  why: >-
    Join my membership program is nowhere near as compelling as get this free valuable thing.
  anchor: >-
    **Focus On The Bonus, Not The Membership.** "Join my membership program"
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, line 5053
  confirmations: 3
  anchor_at: "100m-money-models.md:5053"
  tier: 1
  merged_from: [D-money-models-071]
- id: B-money-models-122
  type: rule
  name: >-
    Make Bonuses Things You Already Have And Do
  statement: >-
    Bonuses are made out of things the business already has and already does, priced and given as bonuses.
  why: >-
    Past newsletters cost no extra time but carry high value, and onboarding has to happen anyway, so you might as well put a price on it; if you value it, they will too.
  anchor: >-
    **Make Bonuses Things You Already Have And Do.** For instance, the two
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, line 5069
  confirmations: 2
  anchor_at: "100m-money-models.md:5069"
  tier: 1
- id: B-money-models-124
  type: rule
  name: >-
    Anchor The Bonuses
  statement: >-
    The value and benefits of the bonus are sold before the customer is told how to get it for free.
  why: >-
    The high-value bonus works as the anchor: it may shock them, and that is the point at which you ask whether they want to know how to get it free.
  anchor: >-
    ● Sell the value of the bonus *before* telling them how they can get it
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Summary Points, line 5221
  confirmations: 2
  anchor_at: "100m-money-models.md:5221"
  tier: 1
- id: B-money-models-125
  type: rule
  name: >-
    More Bonuses Get More People To Join
  statement: >-
    When bonuses are stacked, the individual dollar value of each one is named.
  why: >-
    Mentioning the individual dollar values anchors the value, and stacking them this way gets even more people to join the continuity.
  anchor: >-
    *Mention the individual dollar values of each to anchor the value.*
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, line 5119
  confirmations: 1
  anchor_at: "100m-money-models.md:5119"
  tier: 1
- id: B-money-models-128
  type: rule
  name: >-
    If You Want More Up Front Cash
  statement: >-
    To take more cash up front, the bonus is also sold on its own as a single payment priced 1.33x to 2.66x the first month of the continuity-plus-bonus offer.
  why: >-
    People pay 33% more to avoid continuity, so even charging 33% more for the one-time purchase, half will buy it (2025 figures).
  anchor: >-
    *separate* offers. Make the bonus-only offer a single payment that's
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, line 5168
  confirmations: 2
  anchor_at: "100m-money-models.md:5168"
  tier: 1
- id: B-money-models-129
  type: rule
  name: >-
    Offer Bulk Prepaid Discounts
  statement: >-
    Customers who join continuity are immediately offered a discounted bulk block of months, such as buy five months get one free.
  why: >-
    Only one out of every eight people has to take it to raise 30-day profits by 50%, which can make or break the Money Model; the laws of discounting apply, the larger the discount the more take it.
  anchor: >-
    "buy five months get one free." Only *one out of every eight people* has
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, line 5178
  confirmations: 2
  anchor_at: "100m-money-models.md:5178"
  tier: 1
- id: B-money-models-130
  type: rule
  name: >-
    If You Want Commitments, Prepare To Make A Trade
  statement: >-
    A commitment of 3, 6 or 12+ months is bought with the bonus: the bonus is given only to customers who commit.
  why: >-
    You lose the people who would have signed up month-to-month just for the bonus, so it nets fewer sales but more committed customers; that is the trade.
  anchor: >-
    commitments, trade them for bonuses. For example, only allow customers
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, line 5184
  confirmations: 2
  anchor_at: "100m-money-models.md:5184"
  tier: 1
  merged_from: [D-money-models-074]
- id: B-money-models-131
  type: rule
  name: >-
    Bill weekly, not monthly
  statement: >-
    Recurring billing is set on weekly cycles (weekly, every 2, 4 or 12 weeks) rather than calendar months.
  why: >-
    A year has 12 months but 13 four-week cycles, an 8.3% difference; the same number of people buy at $100 every four weeks as at $100 a month, and at 20% margins annual profit rises 41% (2025 figures).
  anchor: >-
    hate money. Bill *weekly* (weekly, every 2 weeks, 4 weeks, 12 weeks
  source: >-
    100m-money-models.md, Continuity Discount Offers, Important Notes, line 5389
  confirmations: 4
  anchor_at: "100m-money-models.md:5389"
  tier: 1
  merged_from: [A-playbooks-price-005, B-playbooks-price-017, D-playbooks-price-019]
- id: B-money-models-132
  type: rule
  name: >-
    Don't Eat Into The Term With Discounts, Extend Them
  statement: >-
    Free months given for a commitment extend the term rather than being taken out of it, so twelve paid months plus three free is the starting shape.
  why: >-
    Starting from the extended term leaves room to Feature Downsell a shorter one later.
  anchor: >-
    prefer to start with extending the term. Then, I can Feature Downsell a
  source: >-
    100m-money-models.md, Continuity Discount Offers, Important Notes, line 5404
  confirmations: 2
  anchor_at: "100m-money-models.md:5404"
  tier: 1
  merged_from: [D-money-models-077]
- id: B-money-models-133
  type: rule
  name: >-
    Get 3% More Revenue For Five Extra Words
  statement: >-
    The quoted price carries a stated 3% processing fee.
  why: >-
    The author has never had anyone not buy because of a processing fee, and 3% on the topline goes straight to the bottom line: a 10% profit business gains 30% of its profit.
  anchor: >-
    **Get 3% More Revenue For Five Extra Words.** "Yea, it\'s \$X *plus a 3%
  source: >-
    100m-money-models.md, Continuity Discount Offers, Important Notes, line 5407
  confirmations: 1
  anchor_at: "100m-money-models.md:5407"
  tier: 1
- id: B-money-models-134
  type: rule
  name: >-
    Get Two Forms Of Payment
  statement: >-
    A second form of payment is collected from every recurring customer, traded for waiving the 3% processing fee.
  why: >-
    Recurring businesses lose mountains of cash to expired cards and insufficient funds; the fee waiver is justified because collecting new payment information costs man hours.
  anchor: >-
    with the same solution. I ask them if they want a 3% discount (a pretty
  source: >-
    100m-money-models.md, Continuity Discount Offers, Important Notes, line 5418
  confirmations: 6
  anchor_at: "100m-money-models.md:5418"
  tier: 1
  merged_from: [A-playbooks-price-006, B-money-models-135, B-playbooks-price-018, C-playbooks-price-009, E-playbooks-price-010]
- id: B-money-models-136
  type: rule
  name: >-
    Gift Cards
  statement: >-
    The discounted time is handed over as a physical gift card the customer can use after about the first three payments, or give to a friend.
  why: >-
    The gift becomes a lead magnet, and many people simply forget to use it, which leaves you a full-priced sign-up.
  anchor: >-
    can apply the discount whenever they want *after the first three
  source: >-
    100m-money-models.md, Continuity Discount Offers, Important Notes, line 5433
  confirmations: 2
  anchor_at: "100m-money-models.md:5433"
  tier: 1
- id: B-money-models-137
  type: rule
  name: >-
    Try Lifetime Discount At Your Most Common Churn Point
  statement: >-
    A lifetime lower rate is advertised up front but earned only by staying past the month where the average customer drops off.
  why: >-
    It pulls customers through the point where they usually cancel; a rice company set 15% off at five straight months, just beyond where most people cancelled.
  anchor: >-
    lower rate *if* they stay past X period. Make X the month your average
  source: >-
    100m-money-models.md, Continuity Discount Offers, Important Notes, line 5441
  confirmations: 2
  anchor_at: "100m-money-models.md:5441"
  tier: 1
- id: B-money-models-139
  type: rule
  name: >-
    Cancellation fee equals the discount they agreed to
  statement: >-
    The cancellation fee is set equal to the discount the customer received for committing, payable whenever they want to leave.
  why: >-
    It is simple to explain, and it just puts them back at the month-to-month rate.
  applies_when: >-
    Every customer enters the Continuity Offer on a discount of some kind.
  anchor: >-
    Just make the cancellation fee *equal to the discount they agreed to
  source: >-
    100m-money-models.md, Continuity Discount Offers, CANCELLATIONS, line 5462
  confirmations: 3
  anchor_at: "100m-money-models.md:5462"
  tier: 1
  merged_from: [D-money-models-078]
- id: B-money-models-141
  type: rule
  name: >-
    If A Customer Wants To Cancel, Ask To Do An Exit Interview
  statement: >-
    Every cancelling customer is asked for an exit interview, incentivized by waiving the cancellation fee.
  why: >-
    It gives customers a real reason to give feedback; the author routinely saves a third of the customers who agree to an exit interview, and some can be rolled over into a higher level of service.
  anchor: >-
    waive your cancellation fee if you come in and tell me what I could do
  source: >-
    100m-money-models.md, Continuity Discount Offers, CANCELLATIONS, line 5486
  confirmations: 2
  anchor_at: "100m-money-models.md:5486"
  tier: 1
- id: B-money-models-145
  type: rule
  name: >-
    If More Than 5% Of People Want To Cancel Early, Look Into It
  statement: >-
    More than 5% of committed customers wanting to cancel early is a signal to investigate the product rather than tighten the terms.
  why: >-
    Pricing incentivizes sticking but cannot and should not overcome a terrible product; you want to nudge people, not handcuff them into paying for something they hate (2025 benchmark).
  anchor: >-
    **If More Than 5% Of People Want To Cancel Early, Look Into It.**
  source: >-
    100m-money-models.md, Waived Fee Offer, Important Notes, line 5660
  confirmations: 2
  anchor_at: "100m-money-models.md:5660"
  tier: 1
  merged_from: [D-money-models-081]
- id: B-money-models-146
  type: rule
  name: >-
    If You Want More Up Front Cash, Have A Smaller Fee
  statement: >-
    When more up front cash is the goal, the fee is set at 1.5-3x the monthly rate instead of 3-5x.
  why: >-
    A smaller fee encourages people to go month-to-month and pay it, a larger fee encourages the commitment (2025 figures).
  anchor: >-
    the fee 1.5--3x the monthly rate. When you do this, more people will
  source: >-
    100m-money-models.md, Waived Fee Offer, Important Notes, line 5668
  confirmations: 2
  anchor_at: "100m-money-models.md:5668"
  tier: 1
- id: B-money-models-147
  type: rule
  name: >-
    Drop The Fee After The Customer Fulfills The Commitment
  statement: >-
    Once a customer has served out the full commitment, the waived fee is cancelled and they can leave free of charge.
  why: >-
    They have earned their free cancellation; it does not stick forever, which makes the arrangement equitable.
  anchor: >-
    **Drop The Fee After The Customer Fulfills The Commitment.** If someone
  source: >-
    100m-money-models.md, Waived Fee Offer, Important Notes, line 5671
  confirmations: 2
  anchor_at: "100m-money-models.md:5671"
  tier: 1
- id: B-money-models-148
  type: rule
  name: >-
    The $100M Money Model test
  statement: >-
    A Money Model qualifies as a $100M Money Model when one customer produces enough money to get and service at least two more customers in less than 30 days.
  why: >-
    At that point cash stops being the limiter on scaling the business.
  anchor: >-
    and service *at least* two more customers *in less than 30 days.*
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, Description, line 5826
  confirmations: 2
  anchor_at: "100m-money-models.md:5826"
  tier: 1
- id: B-money-models-150
  type: rule
  name: >-
    Each stage pays for the next
  statement: >-
    A stage of the Money Model is only extended once it works reliably, financially and operationally, and pays for the stage after it.
  why: >-
    Starting a bootstrapped business with a finished Money Model makes it collapse on top of you; none of the author's businesses started with a fully forged one.
  anchor: >-
    for the next*. We keep improving each stage until it gets *reliable*.
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, Description, line 5857
  confirmations: 2
  anchor_at: "100m-money-models.md:5857"
  tier: 1
- id: B-money-models-151
  type: rule
  name: >-
    Perfect One Offer At A Time
  statement: >-
    One offer is implemented at a time and repeated until it works reliably and then automatically, before the next stage is started.
  why: >-
    Implementing a whole Money Model at once breaks the business; when the Money Model starts working the business starts breaking anyway.
  anchor: >-
    Money Model at once. Don't. Stick to your stage. Pick one offer. Try it.
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, Important Notes, line 6014
  confirmations: 3
  anchor_at: "100m-money-models.md:6014"
  tier: 1
  merged_from: [D-money-models-083]
- id: B-money-models-153
  type: rule
  name: >-
    Raise Price In Stages
  statement: >-
    New offers start cheap and the price is raised as yeses come in, until raising it further makes less money in total.
  why: >-
    Lots of early yeses generate the customer feedback that improves the product; the stopping point is where the nos are no longer made up for by the extra cash from the yeses.
  anchor: >-
    raising the price. And keep raising the price until you cannot make up
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, Important Notes, line 6026
  confirmations: 4
  anchor_at: "100m-money-models.md:6026"
  tier: 1
  merged_from: [B-playbooks-price-056, D-playbooks-price-064]
- id: B-money-models-154
  type: rule
  name: >-
    Simple Scales. Fancy Fails.
  statement: >-
    New offers are made out of new ways to sell the existing product rather than out of new products or new businesses.
  why: >-
    It is less about having 100 products to offer and more about having 100 ways to offer your product; one personal training product becomes many offers by varying sessions per week.
  anchor: >-
    about having 100 ways to offer your product. Think more ways to sell the
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, Important Notes, line 6032
  confirmations: 3
  anchor_at: "100m-money-models.md:6032"
  tier: 1
  merged_from: [D-money-models-087]
- id: B-money-models-156
  type: rule
  name: >-
    Turn Attraction Offers Into Continuity Offers With Automatic Renewal
  statement: >-
    A bulk Attraction Offer rolls automatically into a month-to-month subscription when the purchased period ends.
  why: >-
    It makes the offer a two-for-one, getting the benefits of an Attraction Offer and a Continuity Offer from the same sale.
  anchor: >-
    Renewal.** This makes it a two-for-one. For example, if you do a Buy 6
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, Important Notes, line 6072
  confirmations: 2
  anchor_at: "100m-money-models.md:6072"
  tier: 1
```


## C. Разборы (кейсы) — 39

```yaml
- id: C-money-models-002
  type: case
  name: >-
    The gym that opens full: $1 in, $34 out in 48 hours
  statement: >-
    $3,000 down on a lease, then ads for a Free 6 Week Challenge run until about 20 leads a day come in at $5 per lead; about half of the leads show for appointments and half of those buy a $600 program, so about 25% of leads become customers, plus another $80 of profit per customer from supplements, giving about $680 per customer before the doors open.
  why: >-
    The marketer who heard it called it amazing because one advertising dollar came back as thirty-four within forty-eight hours, which is what removes cash as a limit on getting customers.
  demonstrates: >-
    An Attraction Offer that pays back the cost of getting the customer many times over inside the first days.
  anchor: >-
    He stuttered a bit, "So you put *one* dollar in...and get *34 dollars*
  source: >-
    100m-money-models.md, Start Here, line 556
  confirmations: 1
  anchor_at: "100m-money-models.md:556"
  tier: 1
- id: C-money-models-004
  type: case
  name: >-
    The rental car counter: a $19/day car leaves at $100/day
  statement: >-
    At the counter the agent offers, in order, a roomier pick-up truck instead of the reserved car, a late return so there are no late fees, premium insurance covering any damage, a minimum-insurance downsell when premium is refused, and prepaid gas at $3.75 a gallon against $3.50 locally; the reservation leaves as a $100 a day rental, a 5x difference.
  why: >-
    The company told him about each problem and then made its solution available, trading a bigger later fee or hassle for a smaller fee right now, so he paid more and was happy to.
  demonstrates: >-
    A Money Model as a deliberate sequence of offers, including a downsell placed immediately after a no.
  anchor: >-
    left paying \$100/day. A 5x difference! And that's the power of a well
  source: >-
    100m-money-models.md, Section I: What's A Money Model?, line 736
  confirmations: 4
  anchor_at: "100m-money-models.md:736"
  tier: 1
  merged_from: [C-money-models-001, C-money-models-005]
- id: C-money-models-009
  type: case
  name: >-
    The three required appointments in the gym's Win Your Money Back
  statement: >-
    The money-back criteria required three meetings, each carrying an offer: a Nutrition Orientation with before pictures where a supplement offer is made, a Progress Check-in where the membership offer is made, and a Transformation Feedback session with after pictures where the membership offer is made again, with a prepay-for-a-year discount for anyone who already bought.
  demonstrates: >-
    Making meetings part of the money-back criteria because every meeting is an opportunity to make another offer.
  anchor: >-
    ● Nutrition Orientation → "Before pictures"→ I make a supplement offer.
  source: >-
    100m-money-models.md, ch. Win Your Money Back, line 1340
  confirmations: 2
  anchor_at: "100m-money-models.md:1340"
  tier: 1
  merged_from: [C-money-models-054]
- id: C-money-models-010
  type: case
  name: >-
    Make Everyone A Winner
  statement: >-
    About halfway through the program the seller asks for the customer's long-term goal, agrees that the program is not the point, and offers to credit this program towards the next one whether or not the short-term goal is hit.
  why: >-
    It lowers the customer's anxiety about failing, keeps them longer, and means the next offer arrives as a surprise rather than as a verdict.
  demonstrates: >-
    Selling the program as if the money comes back only on the criteria, then privately making the next offer as if the customer already won.
  anchor: >-
    *"I know you\'re trying to hit this short-term goal, but what's your
  source: >-
    100m-money-models.md, ch. Win Your Money Back, line 1358
  confirmations: 2
  anchor_at: "100m-money-models.md:1358"
  tier: 1
  merged_from: [C-money-models-011]
- id: C-money-models-012
  type: case
  name: >-
    The full-ride scholarship giveaway of a fitness certification business
  statement: >-
    The business advertises a full-ride scholarship to its whole program, collects contact details and answers to questions like why should we pick you, announces one full-ride winner publicly, then calls everybody else privately to tell them they got a partial scholarship; most join on the call, having never heard the list price and knowing only the value of the full ride.
  why: >-
    Only one full ride can be given away, but as many partial scholarships as you like; everyone who entered already showed interest in the most expensive product, so the discounted version lands on qualified leads.
  demonstrates: >-
    The Giveaway Offer: one Grand Prize, and everyone else qualifies for the promotional offer priced against it.
  anchor: >-
    "Right. So I make a big deal out of the person who wins the full-ride
  source: >-
    100m-money-models.md, ch. Giveaways, line 1478
  confirmations: 1
  anchor_at: "100m-money-models.md:1478"
  tier: 1
- id: C-money-models-013
  type: case
  name: >-
    Explaining the giveaway discount as cost-to-value
  statement: >-
    A Grand Prize advertised at $5,000 of value with a $2,000 retail price is offered to everyone else at $1,800, a 10% discount off retail; presented as $5,000 of value for an $1,800 price it becomes a 64% difference in cost-to-value. The rule of thumb is a core-offer discount equal to 10-30% of gross margins.
  demonstrates: >-
    Anchoring the promotional offer on the Grand Prize's value so a small discount reads as a large one.
  anchor: >-
    discount becomes a 64% difference in cost-to-value!
  source: >-
    100m-money-models.md, ch. Giveaways, line 1606
  confirmations: 1
  anchor_at: "100m-money-models.md:1606"
  tier: 1
- id: C-money-models-017
  type: case
  name: >-
    The 5-Day $5 VIP Tanning Pass and the turkey talk
  statement: >-
    A $5 five-day VIP pass gets people in; when a customer says they want to be several shades darker they get the turkey talk, that doubling the temperature of a Thanksgiving turkey burns it, so it takes five to ten sessions with rest days, more than five days. The pass is then credited towards the first month with the line that $25 day passes make no sense when members get unlimited access for $19.99.
  demonstrates: >-
    The Decoy Offer: a cheap advertised thing, then a premium offer presented as the clear solution because the seller knows what gets results better than the customer does.
  anchor: >-
    "*'Let's just credit your VIP pass toward your first month. Why buy so
  source: >-
    100m-money-models.md, ch. Decoy Offer, line 1803
  confirmations: 1
  anchor_at: "100m-money-models.md:1803"
  tier: 1
- id: C-money-models-020
  type: case
  name: >-
    Are you here for free stuff or lasting results?
  statement: >-
    When a lead asks for the decoy, ask whether they are here for free stuff or lasting results; on results, skip straight to the premium offer, and on free stuff, present the decoy, immediately contrast it with the premium, and only then ask which they think will get them to their goal faster.
  demonstrates: >-
    Getting permission to present the premium offer first when the decoy has to be shown.
  anchor: >-
    Ask them a simple question: *"Are you here for free stuff or lasting
  source: >-
    100m-money-models.md, ch. Decoy Offer, line 1974
  confirmations: 1
  anchor_at: "100m-money-models.md:1974"
  tier: 1
- id: C-money-models-022
  type: case
  name: >-
    The Boot Factory offer
  statement: >-
    A single pair of boots is $200; the store advertises buy one pair for $600 and get two pairs free, so the customer still buys three $200 pairs for $600 while the store gets a free offer instead of a fair-price one.
  why: >-
    A free offer gets far more attention than a discount, and since the store's tourist customers buy once ever, the one purchase is made as large as possible.
  demonstrates: >-
    Buy X Get Y Free as a price reframe; raise prices permanently before giving stuff away.
  anchor: >-
    ● Buy X Get Y Free Offer: Buy One Pair For \$600, Get Two Pairs for Free
  source: >-
    100m-money-models.md, ch. Buy X Get Y Free, line 2131
  confirmations: 3
  anchor_at: "100m-money-models.md:2131"
  tier: 1
  merged_from: [C-money-models-021]
- id: C-money-models-023
  type: case
  name: >-
    Eighteen months of service framed three ways at $1,800
  statement: >-
    Good is Buy 12 Months Get 6 Months Free, better is Buy 9 Get 9 Free, best is Buy 6 Get 12 Free, all at $1,800 for the same eighteen months of service; the third is the most compelling because it has the most free stuff.
  demonstrates: >-
    Always give more free things than paid things; buy ten get two free is weaker than buy two get ten free.
  anchor: >-
    Best: *"Buy 6 Months Get 12 Months Free"* - \$1,800
  source: >-
    100m-money-models.md, ch. Buy X Get Y Free, line 2142
  confirmations: 2
  anchor_at: "100m-money-models.md:2142"
  tier: 1
  merged_from: [C-money-models-024]
- id: C-money-models-025
  type: case
  name: >-
    The speed reading registration page
  statement: >-
    Headline: double your reading speed in 3 hours, or it's free. Pay later: put the card down for $0 and get billed $297 tomorrow, cancellable by email before then if the speed does not double, but attendance is required to qualify. Pay now: $97 with the recordings, sold nowhere else, as a free bonus. An eight-week program was upsold at the end of the training.
  demonstrates: >-
    Pay Less Now or Pay More Later, with a conditional satisfaction guarantee and the card captured on the free option.
  anchor: >-
    The registration page said, "You can put your credit card down for \$0,
  source: >-
    100m-money-models.md, ch. Pay Less Now or Pay More Later, line 2313
  confirmations: 2
  anchor_at: "100m-money-models.md:2313"
  tier: 1
  merged_from: [C-money-models-026]
- id: C-money-models-027
  type: case
  name: >-
    Rating shoulder pain 1-10 to make the promise yes or no
  statement: >-
    Where the promise is to decrease shoulder pain, the customer rates the pain from 1 to 10 before the treatment and again after; if it went down the promise was kept and something else can be sold.
  why: >-
    A promise that is simple, clear and measurable avoids unnecessary cancellations on the pay-later option.
  demonstrates: >-
    Promise a clear yes or no result you can deliver inside the time frame.
  anchor: >-
    pain 1--10 before you do your magic, then ask them to rate it after. If
  source: >-
    100m-money-models.md, ch. Pay Less Now or Pay More Later, line 2410
  confirmations: 1
  anchor_at: "100m-money-models.md:2410"
  tier: 1
- id: C-money-models-028
  type: case
  name: >-
    The burger shop upsell ladder
  statement: >-
    A $2.00 burger makes $0.25 of profit, which would need roughly 10,000 burgers a day to survive; fries add $0.75, making it a meal with a drink adds another $1.75 taking profit from $0.25 to $2.00, an 8x increase, and supersizing for a buck more takes it to $3.00, an 11.6x increase.
  why: >-
    The thing you sell the most is not always the thing you make the most profit on; the profit is on the second, third and fourth offers.
  demonstrates: >-
    Why upsells make or break a money model, and why every business needs its version of do you want fries with that.
  anchor: >-
    with that?"* If they say yes, they profit another \$0.75 and ask *"Do
  source: >-
    100m-money-models.md, Section III: Upsell Offers, line 2641
  confirmations: 1
  anchor_at: "100m-money-models.md:2641"
  tier: 1
- id: C-money-models-029
  type: case
  name: >-
    Free earmuffs with coat storage
  statement: >-
    The fur shop advertises free earmuffs with coat storage; when customers arrive to collect the muffs and drop their coats they are told the muffs will be stored as well for $30, with the question you don't want to store anything else do you, so customers pay to store something they were just given free.
  why: >-
    Bonuses solve problems, and because of the problem-solution cycle they also reveal new ones the upsell can solve; and people are trained to answer no to that question, which here means yes.
  demonstrates: >-
    The Classic Upsell structure you can't have X without Y, getting them to say no to say yes, and using free bonuses to create the problem an upsell solves.
  anchor: >-
    *'Great. And we'll store those as well for \$30. You don't want to store
  source: >-
    100m-money-models.md, ch. The Classic Upsell, line 2739
  confirmations: 2
  anchor_at: "100m-money-models.md:2739"
  tier: 1
- id: C-money-models-033
  type: case
  name: >-
    Prescription upselling discovered on an order form
  statement: >-
    After writing step-by-step dosing instructions on scratch paper for one insistent customer, the next appointment asked for the same; this time the instructions were written on the order form itself next to each item, with how much to take and when, and the close became I got all your instructions here, do you want to just use the card on file. Thirty-day profits rose from then on.
  why: >-
    Detailed and personalised instructions upsell more people than vague and general suggestions, because you explain how to use the thing as if they already have it.
  demonstrates: >-
    The Prescription Upsell inside the Menu Upsell.
  anchor: >-
    "I got all your instructions here, do you want to just use the card on
  source: >-
    100m-money-models.md, ch. Menu Upsell, line 3026
  confirmations: 1
  anchor_at: "100m-money-models.md:3026"
  tier: 1
- id: C-money-models-034
  type: case
  name: >-
    Unselling discovered after running out of stock
  statement: >-
    Out of inventory, he sent a customer to a cheaper shop down the street for two products, then crossed the weight-gainer off her sheet after confirming she was not trying to gain weight, crossed off the testosterone booster the same way, and prescribed what was left; she bought without hesitation. Afterwards he kept products in stock just to cross them out.
  why: >-
    Going out of his way to cross out what she did not need built enough goodwill to upsell what she did.
  demonstrates: >-
    Unselling: telling customers what they don't need in order to get them excited about what they do.
  anchor: >-
    "Okay great. You won\'t be needing this," crossing out the weight-gainer
  source: >-
    100m-money-models.md, ch. Menu Upsell, line 3068
  confirmations: 1
  anchor_at: "100m-money-models.md:3068"
  tier: 1
- id: C-money-models-036
  type: case
  name: >-
    The $16,000 suit that sold a $2,200 suit
  statement: >-
    With a $500 budget, the first suit tried on turned out to be $16,000; on the visible gasp the owner asked whether he cared much about the designer and immediately draped a second suit, already pulled, at $2,200, which was bought along with $300 of socks, handkerchief and shirt that all seemed cheap afterwards.
  why: >-
    The key point is that the cheaper suit was pulled before the reaction: the seller knew the gasp was coming, and after the anchor the same primary feature at a fifth of the price reads as a great deal.
  demonstrates: >-
    The Anchor Upsell: present the anchor, get the gasp, come to the rescue by asking about the premium feature, present the main offer, ask for payment.
  anchor: >-
    Coming to my aid he asked "Do you care about the designer much?"
  source: >-
    100m-money-models.md, ch. Anchor Upsell, line 3306
  confirmations: 2
  anchor_at: "100m-money-models.md:3306"
  tier: 1
- id: C-money-models-038
  type: case
  name: >-
    Justin's rollover of the challenge winnings
  statement: >-
    Alex's winners put their $600 towards three months of membership and churned before the first out-of-pocket payment, so he had effectively sold buy six weeks get three months free; Justin rolled the same winnings into a year-long membership as fifty dollars off per month, so winners started paying immediately and still got their money back over the year.
  why: >-
    Spreading the credit means the business never has customers who are not paying, and it keeps the recurring revenue going instead of restarting from zero every month.
  demonstrates: >-
    The Rollover Upsell: credit the previous purchase towards the next offer, spread out rather than given up front.
  anchor: >-
    answer. "We just give them fifty bucks off per month for a year."
  source: >-
    100m-money-models.md, ch. Rollover Upsell, line 3530
  confirmations: 4
  anchor_at: "100m-money-models.md:3530"
  tier: 1
  merged_from: [C-money-models-003, C-money-models-008, C-money-models-042]
- id: C-money-models-041
  type: case
  name: >-
    Rolling over a competitor's remaining payments
  statement: >-
    Find a competitor's upset customers, for instance by scraping contact details from negative product reviews, and credit whatever payments they have left with that vendor towards a longer agreement with you: I saw your negative review and it upset me, I'll credit whatever payments you have left with them to switch to ours.
  demonstrates: >-
    Using Rollover Offers to attract new customers, not only to upsell your own.
  anchor: >-
    Ex: *"Hi John, I saw your negative review on their product and it really
  source: >-
    100m-money-models.md, ch. Rollover Upsell, line 3613
  confirmations: 1
  anchor_at: "100m-money-models.md:3613"
  tier: 1
- id: C-money-models-044
  type: case
  name: >-
    The first payment plan, sold in five questions
  statement: >-
    A lead said she couldn't afford it; the seller asked when she got paid, offered half down now and half on the first, then a third down today across three payments, then asked what she actually could do; she could pay in full on the first, so her card was taken and charged on the second.
  why: >-
    It costs too much usually means it costs too much up front; the price never moved, only when the money arrived.
  demonstrates: >-
    The Payment Plan Downsell ladder, and never dropping the price just to get someone to buy.
  anchor: >-
    "What if you do three payments and just put a third down today?"
  source: >-
    100m-money-models.md, ch. Payment Plan Downsells, line 3867
  confirmations: 1
  anchor_at: "100m-money-models.md:3867"
  tier: 1
- id: C-money-models-045
  type: case
  name: >-
    Interest presented as a prepayment discount
  statement: >-
    Instead of it's $10 now but $15 over time because we charge $5 in interest, the price is presented as $15 with the interest already included, and prepayment is offered as a way to get it for $10 and save $5, which is what most people do.
  why: >-
    Same math, but the offer is friendlier and the full price works as a price anchor.
  demonstrates: >-
    Step 1 of the Payment Plan Downsell: reward for paying in full rather than punish for paying over time.
  anchor: >-
    Instead, I say *"It's \$15...but it's \$10 if you prepay it. You save
  source: >-
    100m-money-models.md, ch. Payment Plan Downsells, line 3946
  confirmations: 1
  anchor_at: "100m-money-models.md:3946"
  tier: 1
- id: C-money-models-051
  type: case
  name: >-
    $500 onboarding waived on four conditions
  statement: >-
    HR software at $500 onboarding then $99 per month: the $500 is not paid up front provided the buyer attends onboarding, which is three sixty-minute Zoom calls, does the homework, activates the employer profile and gets employees set up by the end of the third call; otherwise the fee is charged.
  demonstrates: >-
    Writing the terms of a Trial With Penalty so that the criteria activate and retain the customer, with the calls doubling as upsell opportunities.
  anchor: >-
    Trial With Penalty: You don't have to pay \$500 up front, but you
  source: >-
    100m-money-models.md, ch. Trial With Penalty, line 4268
  confirmations: 2
  anchor_at: "100m-money-models.md:4268"
  tier: 1
  merged_from: [C-money-models-049]
- id: C-money-models-053
  type: case
  name: >-
    Explaining the fees after the card is taken
  statement: >-
    The fees are framed as keeping the customer on track: we do our part so long as you do yours, if you miss or skip anything your results suffer, you get dinged a little fee that gets you back on track, and if you follow through you get all this for free. Customers initial separately next to the fee clauses.
  why: >-
    Explaining the fees before taking the card produces more resistance; explained afterwards with a this is just how we've always done it attitude, the take rate is higher, and the separate initials force the sales staff to explain them.
  demonstrates: >-
    The order of the Trial With Penalty close: card first, fees second.
  anchor: >-
    like:*"We will do our part so long as you do yours. That's fair right?
  source: >-
    100m-money-models.md, ch. Trial With Penalty, line 4347
  confirmations: 2
  anchor_at: "100m-money-models.md:4347"
  tier: 1
  merged_from: [C-money-models-052]
- id: C-money-models-055
  type: case
  name: >-
    Upselling from each of the three trial outcomes
  statement: >-
    If they liked it, meet anyway and offer a longer term or a higher-value version. If they hated it, ask what they would have wanted different, agree they are right, take the blame rather than blaming them, and offer the higher level thing on the ground that you now understand their needs; about half buy. If they never used it, reach out repeatedly, ask for a meeting and offer to waive the fee for it, then get them back on track or offer something better.
  authors_caveat: >-
    Hormozi says he does not like billing non-starters, because a small fee is not worth a 1-star review.
  demonstrates: >-
    Using the end of a trial as an upsell point in all three outcomes.
  anchor: >-
    2\) If they hate it: *Turn that frown upside down*. Ask them what they
  source: >-
    100m-money-models.md, ch. Trial With Penalty, line 4386
  confirmations: 1
  anchor_at: "100m-money-models.md:4386"
  tier: 1
- id: C-money-models-056
  type: case
  name: >-
    Downselling by removing the money-back guarantee
  statement: >-
    On a price objection the seller asks: if you don't want the option to get your money back, you can pay less, or you can keep your money-back guarantee, which would you prefer. Once they understand what they would give up, many say they would rather keep the guarantee and pay the original price.
  why: >-
    People only see the value of the guarantee after it has been removed and the price difference is visible, so cutting a feature is not a discount and does not devalue the product.
  demonstrates: >-
    Feature Downsells: lower the price by changing what they get, and remove features from highest to lowest value so customers re-upsell themselves.
  anchor: >-
    "Yea. Works great. When we get a price objection we ask '*If you don't
  source: >-
    100m-money-models.md, ch. Feature Downsells, line 4528
  confirmations: 2
  anchor_at: "100m-money-models.md:4528"
  tier: 1
  merged_from: [C-money-models-057]
- id: C-money-models-058
  type: case
  name: >-
    Downselling service quality instead of price
  statement: >-
    Instead of 5-minute response times, start at overnight response times, framed as saving money while still getting answers with a small delay; the same lever runs across time availability, days and hours, location, cancellation terms, speed of response and delivery, service ratio, communication method, provider qualifications, live against recorded, in-person against remote, DIY against DWY against DFY, expirations, personalisation and guarantee terms.
  demonstrates: >-
    Feature Downsells by lowering quality rather than cutting the price of the same thing.
  anchor: >-
    Service Quality Downsell: *Instead of 5-minute response times, why
  source: >-
    100m-money-models.md, ch. Feature Downsells, line 4611
  confirmations: 1
  anchor_at: "100m-money-models.md:4611"
  tier: 1
- id: C-money-models-059
  type: case
  name: >-
    The painter's Done-For-You to Do-It-Yourself downsell
  statement: >-
    If the customer cannot afford the painter painting the house, he gives them the paint and leases them a spray machine at a daily rate; the chiropractor's version starts the patient with home massage tools, foam rollers and mats instead of adjustments.
  demonstrates: >-
    Downselling from a service to a product that solves the same problem, once all service downsells are refused.
  anchor: >-
    ● Painter: *If you can't afford me painting your house, why don\'t I
  source: >-
    100m-money-models.md, ch. Feature Downsells, line 4666
  confirmations: 1
  anchor_at: "100m-money-models.md:4666"
  tier: 1
- id: C-money-models-061
  type: case
  name: >-
    The free orientation after every offer is refused
  statement: >-
    Once someone has refused all the Done For You offers, they are invited to a free orientation the next day on the same topic, and a DIY product solving the same problem is offered at the end; of those who refused the fitness offer about half showed up, and almost all of them bought supplements.
  demonstrates: >-
    Free orientations as the last step of a Feature Downsell chain, turning a final no into revenue.
  anchor: >-
    refused my fitness offer. Of the people who showed up to the orientation
  source: >-
    100m-money-models.md, ch. Feature Downsells, line 4743
  confirmations: 1
  anchor_at: "100m-money-models.md:4743"
  tier: 1
- id: C-money-models-062
  type: case
  name: >-
    Bartering a discount for advertising
  statement: >-
    On a price objection, $100 off in exchange for four things: a review on all review sites, a video testimonial, public social posts at the beginning, middle and end of the program showing progress, and introductions to two friends who would want to do this too, closed with Deal?
  why: >-
    The advertising is worth more than the $100 to the seller and less than the $100 to the buyer, which makes it a trade rather than a discount.
  demonstrates: >-
    Downsells are trades: if you're gonna give something, get something.
  anchor: >-
    exchange for advertising. Ex:*"I'll knock \$100 off if you: 1) Leave me
  source: >-
    100m-money-models.md, ch. Feature Downsells, line 4766
  confirmations: 1
  anchor_at: "100m-money-models.md:4766"
  tier: 1
- id: C-money-models-063
  type: case
  name: >-
    The continuity arithmetic on 100 people
  statement: >-
    A $1,000 thing sold to 100 people gets 10 buyers and $10,000 now with nothing later; the same thing at $50 a month gets 40 of the 100, and held for twenty months still makes $1,000 from each, so $10,000 now and $0 later becomes $2,000 now and $40,000 over time, with four times as many customers left to upsell.
  why: >-
    This is why continuity attracts more customers but cannot carry acquisition on its own: more money tomorrow, strapped for cash today, which is why Hormozi makes continuity offers last.
  demonstrates: >-
    The trade-off that decides where Continuity Offers sit in a money model.
  anchor: >-
    thing...\$50 per month instead. At fifty bucks, we can get 40 out of 100
  source: >-
    100m-money-models.md, Section V: Continuity Offers, line 4869
  confirmations: 1
  anchor_at: "100m-money-models.md:4869"
  tier: 1
- id: C-money-models-064
  type: case
  name: >-
    The gym that sold membership instead of the challenge
  statement: >-
    The gym still advertises the six-week challenge and still pitches its price, but as soon as the lead is interested it asks whether they want it for free: it becomes free if they become a member, and members also get exclusive bonuses such as better class times, the tanning booth and VIP events. Everyone who joins is immediately asked wanna save even more money and offered a prepaid discount with bonuses for six months.
  demonstrates: >-
    Continuity Bonus Offers, with a bulk prepaid continuity upsell stacked immediately on top.
  anchor: >-
    soon as they say they\'re interested, we ask if they want to get it for
  source: >-
    100m-money-models.md, ch. Continuity Bonus Offers, line 4955
  confirmations: 2
  anchor_at: "100m-money-models.md:4955"
  tier: 1
  merged_from: [C-money-models-065]
- id: C-money-models-067
  type: case
  name: >-
    The newsletter continuity bonus and lifetime discount
  statement: >-
    One-time bonus: all 40 past newsletters valued at $15,880, free on becoming a member today at $399 a month after a 30-day free trial. Lifetime discount and lifetime bonuses: paying today locks the rate at $299 a month with early digital access and a physical copy every month.
  why: >-
    Back issues cost no extra time but carry a high, real, anchorable value, which is what makes them the right kind of bonus.
  demonstrates: >-
    Making bonuses out of things you already have, and pairing a continuity bonus with a lifetime discount.
  anchor: >-
    *One-Time Bonus:* Get all my past 40 newsletters valued at \$15,880 by
  source: >-
    100m-money-models.md, ch. Continuity Bonus Offers, line 5043
  confirmations: 3
  anchor_at: "100m-money-models.md:5043"
  tier: 1
  merged_from: [C-money-models-066]
- id: C-money-models-071
  type: case
  name: >-
    Trading the processing fee for a second form of payment
  statement: >-
    Customers are offered a 3% discount, the size of a standard processing fee, in exchange for giving a second form of payment in case anything happens to the first; if they ask why, the answer is that the fee exists because chasing new payment information costs man hours, so saving that time passes the saving on. ACH is the preferred second method.
  why: >-
    Recurring businesses lose large amounts of cash to expired or maxed-out cards from customers who never cancelled, and both failures are fixed by the same second card.
  demonstrates: >-
    Reducing involuntary churn in a continuity offer.
  anchor: >-
    standard processing fee). *"Do you want to save the processing fee?
  source: >-
    100m-money-models.md, ch. Continuity Discount Offers, line 5419
  confirmations: 1
  anchor_at: "100m-money-models.md:5419"
  tier: 1
- id: C-money-models-076
  type: case
  name: >-
    The Waived Fee Offer priced out
  statement: >-
    Twelve-month commitment, $1,000 per month, $5,000 fee if they pay month-to-month. Option A: a one-time $5,000 plus $1,000 for the first month, then $1,000 a month, cancel whenever. Option B: the $5,000 is waived for a twelve-month commitment at $1,000 a month, and is paid only if the commitment is broken early.
  applies_when: >-
    The fee is typically 3-5x the monthly rate; making it 1.5-3x pushes more people to month-to-month and brings more cash up front.
  demonstrates: >-
    The mechanics of a Waived Fee Offer, where the risk is traded between the two options.
  anchor: >-
    Option A: Pay a one-time fee of \$5,000 *plus* \$1,000 for the first
  source: >-
    100m-money-models.md, ch. Waived Fee Offer, line 5629
  confirmations: 1
  anchor_at: "100m-money-models.md:5629"
  tier: 1
- id: C-money-models-077
  type: case
  name: >-
    The cancellation fee donated to a cause they hate
  statement: >-
    To keep customers extra motivated, ask what cause they absolutely hate and tell them that if they cancel early their setup fee will be donated to it, which gives two reasons to stay rather than one.
  demonstrates: >-
    Strengthening the stick in a Waived Fee Offer.
  anchor: >-
    motivated, you can donate it to a cause they are *against*. Ex: "What
  source: >-
    100m-money-models.md, ch. Waived Fee Offer, line 5682
  confirmations: 1
  anchor_at: "100m-money-models.md:5682"
  tier: 1
- id: C-money-models-078
  type: case
  name: >-
    How Gym Launch's money model was built one offer at a time
  statement: >-
    A Decoy Offer, free courses and calls with either do it yourself free or $16,000 of done-with-you over 16 weeks, reached $476,000 a month in three months. Adding a Classic Upsell, Gym Lords at $42,000 a year with a $6,000 prepay discount and a community as a Continuity Bonus, a Payment Plan Downsell of $10,000 down then about $800 a week for 52 weeks, and a Continuity Discount frontloading free time until the first offer was paid off, took it to about $1,500,000 a month; a personalised Menu Upsell plus Feature Downsells took it to $2,300,000 a month within 14 months.
  why: >-
    Each stage paid for the next: with only one thing to sell, revenue was going to plateau fast, so every level was added after the previous one was working.
  demonstrates: >-
    Building a money model one stage at a time rather than implementing a finished one at once.
  anchor: >-
    zoom...The Classic Upsell + Continuity Bonus + Payment Plan Downsell +
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, line 5792
  confirmations: 3
  anchor_at: "100m-money-models.md:5792"
  tier: 1
  merged_from: [C-money-models-079]
- id: C-money-models-080
  type: case
  name: >-
    Micro Gyms money model breakdown (local business)
  statement: >-
    Stage I attraction: Win Your Money Back, a pay-to-enter fitness challenge with the money back on hitting goals, with a Payment Plan Downsell running split pay, then three-pay, then a free Trial With Penalty. Stage II upsell: Menu Upsell of supplement bundles personalised to the goal, with a Feature Downsell from big bundle to small bundle to monthly subscription. Stage III continuity: Rollover Upsell plus a lifetime discount of $50 off per month for a 12-month commitment.
  demonstrates: >-
    A local-business money model using all four offer types in sequence.
  anchor: >-
    \$50 off per month for life with a 12-month commitment
  source: >-
    100m-money-models.md, Section VI Example Money Models, line 5924
  confirmations: 1
  anchor_at: "100m-money-models.md:5924"
  tier: 1
- id: C-money-models-081
  type: case
  name: >-
    Newsletter money model (digital product)
  statement: >-
    Stage I attraction: a free trial, $0 then $399 per month after 30 days. Stages II and III combined: Pay Less Now or Pay More Later with a lifetime discount, pay $297 now and keep that rate for life. Hormozi calls it a six-headed money-making monster because one offer serves as attraction, upsell and continuity at once.
  demonstrates: >-
    Mixing and matching offer types inside a single offer.
  anchor: >-
    Pay \$297 Now and Keep That Rate For Life
  source: >-
    100m-money-models.md, Section VI Example Money Models, line 5935
  confirmations: 1
  anchor_at: "100m-money-models.md:5935"
  tier: 1
- id: C-money-models-082
  type: case
  name: >-
    Dog food money model (physical product)
  statement: >-
    Stage I attraction: Buy Four Months of Food, Get Two Months Free. Stage II upsell: Classic Upsell, as in the rental car story, of monthly dog toys then dog vitamins. Stage II downsell: Feature Downsell, just the premium food then, you don't want anything else do you. Stage III continuity: automatic renewal month-to-month after the first bulk purchase runs out.
  demonstrates: >-
    Turning an Attraction Offer into a Continuity Offer with automatic renewal.
  anchor: >-
    Buy Four Months of Food, Get Two Months Free
  source: >-
    100m-money-models.md, Section VI Example Money Models, line 5947
  confirmations: 1
  anchor_at: "100m-money-models.md:5947"
  tier: 1
```


## D. Антипаттерны и границы — 10

```yaml
- id: D-money-models-002
  type: antipattern
  name: >-
    The slow drip
  statement: >-
    Relying on a slow drip of profit from many customers to eventually pay for a single customer.
  why: >-
    The drip starves the business of cash; it means they can only get lots of customers through advertising if they already have lots of customers.
  anchor: >-
    *eventually* pays for a *single* customer. This 'drip' starves the
  source: >-
    100m-money-models.md, Section I, Beware: Bad Money Models Kill Businesses, line 820
  confirmations: 2
  anchor_at: "100m-money-models.md:820"
  tier: 1
  merged_from: [D-money-models-003]
- id: D-money-models-010
  type: rule
  name: >-
    It Works Well With Stuff People Start And...Quit
  statement: >-
    Win Your Money Back is aimed at things people start and quit: starting businesses, learning new skills, losing weight, building fitness, beauty regimes, self-care, time management, mental health management.
  why: >-
    It keeps motivation during the early pains of learning; the author has never seen a better way of setting up a program for results.
  anchor: >-
    **It Works Well With Stuff People Start And...Quit.** Like starting
  source: >-
    100m-money-models.md, Win Your Money Back, Important Notes, line 1232
  confirmations: 2
  boundary: >-
    Win Your Money Back is for businesses that require their customers to put in continuous effort to get their ideal outcome, not for one-shot purchases.
  anchor_at: "100m-money-models.md:1232"
  tier: 1
- id: D-money-models-014
  type: antipattern
  name: >-
    Everyone thinks businesses make money on people who fail
  statement: >-
    Believing that a Win Your Money Back program makes its money from the people who fail to qualify.
  why: >-
    No: the real money comes from people who succeed with it and you have something else to offer them; the more results you deliver, the more money you'll make.
  anchor: >-
    ● Everyone thinks businesses make money on people who fail the program.
  source: >-
    100m-money-models.md, Win Your Money Back, Summary Points, line 1404
  confirmations: 1
  anchor_at: "100m-money-models.md:1404"
  tier: 1
- id: D-money-models-024
  type: rule
  name: >-
    One thing to sell and you give it away
  statement: >-
    Do not build a free offer around a single product; if you only have one thing to sell and you give it away, you go hungry.
  why: >-
    Buy X Get Y Free turns a discount into a free offer only because you are selling more than one thing at once, so the discount value can cover the price of more stuff.
  anchor: >-
    Offers. But if you only have one thing to sell, and you give it away,
  source: >-
    100m-money-models.md, Buy X Get Y Free, Description, line 2091
  confirmations: 2
  boundary: >-
    Buy X Get Y Free works for stuff that makes sense to buy more of or get longer access to.
  anchor_at: "100m-money-models.md:2091"
  tier: 1
- id: D-money-models-027
  type: antipattern
  name: >-
    Matching the free stuff to the paid stuff
  statement: >-
    Beginners make the free items the same as the paid items instead of mixing and matching.
  why: >-
    You can pair different free things with paid things as long as the value still makes the offer compelling; more cheaper things can work better than fewer expensive things (three pairs of socks against one shirt).
  anchor: >-
    When people first start doing offers like this, they match the free and
  source: >-
    100m-money-models.md, Buy X Get Y Free, Important Notes, line 2183
  confirmations: 1
  anchor_at: "100m-money-models.md:2183"
  tier: 1
- id: D-money-models-033
  type: antipattern
  name: >-
    Expecting the first offer to make the profit
  statement: >-
    Building a business on the assumption that the thing you sell the most is the thing you make the most profit on.
  why: >-
    Profit is made on the second, third and fourth offers; a burger shop making $0.25 on a $2.00 burger would need ~10,000 burgers a day, and if McDonald's didn't upsell fries and soda there wouldn't be a McDonald's.
  anchor: >-
    first offer *doesn't always* make the profit. In other words, *the thing
  source: >-
    100m-money-models.md, Section III intro: Upsell Offers, line 2654
  confirmations: 1
  anchor_at: "100m-money-models.md:2654"
  tier: 1
- id: D-money-models-041
  type: rule
  name: >-
    Menu Upsells work best when you have multiple offers available
  statement: >-
    Menu Upsells require multiple offers to be available; the A/B tactic in particular needs multiple offers that solve the same problem, and Prescription Upselling is for when offering a choice is inconvenient and you have only one thing that solves the problem.
  why: >-
    Each of the four tactics is matched to a different shape of the product line.
  anchor: >-
    ● Menu Upsells work best when you have multiple offers available.
  source: >-
    100m-money-models.md, Menu Upsell, Summary Points, line 3246
  confirmations: 3
  boundary: >-
    A/B Upsell needs several offers solving the same problem; Prescription Upsell is the one for a single solution.
  anchor_at: "100m-money-models.md:3246"
  tier: 1
- id: D-money-models-051
  type: antipattern
  name: >-
    Discounting in response to "it costs too much"
  statement: >-
    Immediately discounting or selling cheaper stuff when a prospect says the price is too high.
  why: >-
    A huge percentage of the time "it costs too much" really means "this costs too much up front"; people think discounts work because the customer pays less for the product, when really it's because they pay less in the moment. A payment plan gets the buyer and keeps the full price.
  anchor: >-
    will immediately discount or sell cheaper stuff *just to get people to
  source: >-
    100m-money-models.md, Payment Plan Downsells, Description, line 3913
  confirmations: 2
  anchor_at: "100m-money-models.md:3913"
  tier: 1
- id: D-money-models-054
  type: antipattern
  name: >-
    One offer and no downsell
  statement: >-
    Running a single offer, so everyone who says no is lost.
  why: >-
    If you normally close three of ten, a Trial With Penalty downsell picks up another four and three of those upsell after the trial — three sales become six, doubling customers.
  anchor: >-
    If you only have one offer, you lose everyone who says no. Downselling
  source: >-
    100m-money-models.md, Trial With Penalty, Description, line 4226
  confirmations: 2
  anchor_at: "100m-money-models.md:4226"
  tier: 1
- id: D-money-models-084
  type: rule
  name: >-
    When your Money Model starts working, your business starts breaking
  statement: >-
    Reliability must be financial and operational both; when the Money Model starts working the business starts breaking.
  why: >-
    The author calls it part of the game and suggests finding someone who can build and lead the team that makes the vision a reality.
  anchor: >-
    warning: when your Money Model starts working, your business starts
  source: >-
    100m-money-models.md, Section VI, Description, line 5859
  confirmations: 1
  boundary: >-
    A named limit of the Money Model itself: it solves cash, and hands you an operational problem the book does not solve. Elsewhere the author calls keeping up with the volume "A problem for another book to solve."
  anchor_at: "100m-money-models.md:5859"
  tier: 1
```


## E. Глоссарий — 35

```yaml
- id: E-money-models-001
  type: term
  name: >-
    Money Model
  statement: >-
    A Money Model is the deliberate sequence of offers a business makes to a customer — what you offer, when you offer it and how — not a single offer or a price list.
  definition: >-
    A Money Model is a sequence of offers. At their core, we find every opportunity to solve a customer's problem...and then offer to solve it. It's what you offer, when you offer, and how you offer it to make as much money as you can as fast as you can.
  not_to_confuse_with: >-
    A single offer: the author stresses that Money Models tend to have many offers in a specific order, and that if you offer the right thing when customers realize they need it, you can make as many offers as you like.
  anchor: >-
    A Money Model is *a deliberate sequence of offers*. It's what you offer,
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, Description, line 5823
  confirmations: 5
  anchor_at: "100m-money-models.md:5823"
  tier: 1
  merged_from: [E-lost-chapters-025, E-lost-chapters-026]
- id: E-money-models-002
  type: term
  name: >-
    A good Money Model
  statement: >-
    A Money Model counts as good when one customer produces more profit in the first 30 days than it costs to get and service that same customer — the author's bare minimum, not a target.
  definition: >-
    A good Money Model makes more profit from a customer than it costs to get and service them in the first 30 days. That's the bare minimum.
  not_to_confuse_with: >-
    A $100M Money Model, which the author sets one level higher: profit from one customer above the cost of getting and servicing many.
  anchor: >-
    **A good Money Model** *makes more profit from a customer than it
  source: >-
    100m-money-models.md, Ten Years In Ten Minutes, What We Covered, line 6166
  confirmations: 1
  anchor_at: "100m-money-models.md:6166"
  tier: 1
- id: E-money-models-003
  type: term
  name: >-
    $100M Money Model
  statement: >-
    A $100M Money Model makes more profit from one customer in the first 30 days than it costs to get and service many customers, which removes cash as the limit on growth.
  definition: >-
    A $100M Money Model makes more profit from one customer than it costs to get and service many customers in the first 30 days, which removes cash as a limiter to scaling your business.
  why: >-
    With so much money made in the first thirty days, the cost of getting more customers is never a problem again, and the business is forced to fix everything else just to keep up.
  anchor: >-
    **A \$100M Money Model** *makes more profit from one customer than
  source: >-
    100m-money-models.md, Ten Years In Ten Minutes, What We Covered, line 6171
  confirmations: 3
  anchor_at: "100m-money-models.md:6171"
  tier: 1
- id: E-money-models-004
  type: term
  name: >-
    Attraction Offer
  statement: >-
    An Attraction Offer is the offer that turns strangers into customers by offering something free or at a discount, generating leads and converting them in one move.
  definition: >-
    Attraction Offers generate leads and convert them into customers. They turn advertising into money by offering something free or at a discount. Attraction Offers turn strangers into customers.
  not_to_confuse_with: >-
    A lead-generation offer alone: the author's Attraction Offer both generates the lead and converts it, and often also makes money by offering a better deal at a higher price.
  anchor: >-
    Attraction Offers generate leads *and* convert them into customers. They
  source: >-
    100m-money-models.md, Section II: Attraction Offers, line 1026
  confirmations: 3
  anchor_at: "100m-money-models.md:1026"
  tier: 1
- id: E-money-models-006
  type: term
  name: >-
    Win Your Money Back
  statement: >-
    Win Your Money Back is the Attraction Offer where the seller sets the customer's goal and the route to it, and the customer who reaches it qualifies for their money back in cash or store credit.
  definition: >-
    A Win Your Money Back Offer works like this. You set a goal for the customer and tell them how to reach it. If they reach it, then they qualify to get their money back or get it back as store credit. Bottom line: customers put money down. If they do the stuff OR they get the result OR both — they get it back as cash or store credit.
  not_to_confuse_with: >-
    Trial With Penalty, which the author separates himself: Win Your Money Back gives customers the chance to get their money back if they meet the terms; in Trial With Penalty customers only pay if they don't meet the terms.
  applies_when: >-
    Businesses that require their customers to put in continuous effort to get their ideal outcome, and stuff people start and quit.
  anchor: >-
    A Win Your Money Back Offer works like this. *You* set a goal for the
  source: >-
    100m-money-models.md, Win Your Money Back, Description, line 1139
  confirmations: 4
  authors_caveat: >-
    Only use a Win Your Money Back Offer if your refund rate is below 5%; and only offer it if you feel OK with giving money back, since about 10% of all customers will ask for it.
  anchor_at: "100m-money-models.md:1139"
  tier: 1
  merged_from: [C-money-models-006]
- id: E-money-models-007
  type: term
  name: >-
    Giveaway Offer
  statement: >-
    A Giveaway Offer advertises a chance to win a big prize in exchange for contact information, and after a winner is picked everyone else is offered the same prize at a discount.
  definition: >-
    Giveaway Offers advertise a chance to win a big prize in exchange for contact information and whatever else you want. Then, after picking a winner, you offer everyone else the big prize at a discounted price.
  not_to_confuse_with: >-
    Scholarship, sweepstakes and raffle are the author's own aliases for the same offer: they all mean enter for a chance to win.
  anchor: >-
    Giveaway Offers advertise a chance to win a big prize in exchange for
  source: >-
    100m-money-models.md, Giveaways, Description, line 1513
  confirmations: 2
  anchor_at: "100m-money-models.md:1513"
  tier: 1
- id: E-money-models-008
  type: term
  name: >-
    Grand Prize
  statement: >-
    The Grand Prize of a Giveaway is the thing you want everyone to buy, carrying an assigned monetary value that serves as the price anchor for the offer made to everyone who does not win.
  definition: >-
    Make your Grand Prize the thing you want everyone to buy. Make sure you assign a monetary value to your grand prize to serve as a price anchor.
  why: >-
    Leads entered because they found the Grand Prize interesting, so the bigger the value assigned to it, the more compelling the discounted offer made to everyone else.
  anchor: >-
    **Pick A Grand Prize.** Make your Grand Prize *the thing you want
  source: >-
    100m-money-models.md, Giveaways, Description, line 1535
  confirmations: 3
  anchor_at: "100m-money-models.md:1535"
  tier: 1
  merged_from: [C-money-models-014]
- id: E-money-models-009
  type: term
  name: >-
    Promotional Offer (Giveaway)
  statement: >-
    The promotional offer is the discounted version of the Grand Prize that every non-winning entrant qualifies for — the author's generalisation of the partial scholarship.
  definition: >-
    Your promotional offer takes the place of the partial scholarship in the story. You create it by enhancing your core offer with a discount, a bonus, or by minorly changing it from the Grand Prize in order to ethically justify a price reduction (using the Grand Prize as a price anchor).
  not_to_confuse_with: >-
    The Grand Prize: the Grand Prize is announced publicly to one winner, while everybody else qualifies for the promotional offer, which the author calls a participation trophy.
  anchor: >-
    **Pick Your Promotional Offer.** Your promotional offer takes the place
  source: >-
    100m-money-models.md, Giveaways, Description, line 1540
  confirmations: 1
  anchor_at: "100m-money-models.md:1540"
  tier: 1
- id: E-money-models-010
  type: term
  name: >-
    Qualifying Actions
  statement: >-
    Qualifying Actions are the things a Giveaway entrant must do to qualify to win, chosen so they also promote the giveaway or demonstrate a higher level of interest.
  definition: >-
    Other stuff entrants do to qualify to win. I also use these to get them to promote my giveaway more, or demonstrate higher levels of interest. Ex: attending a call or event, making a post, entering a group, etc.
  not_to_confuse_with: >-
    Eligibility, which the author keeps separate: eligibility questions ask whether the entrant is a fit for the product (Do you own a vet clinic? Why should you be selected?), while qualifying actions are things they do.
  anchor: >-
    **Qualifying Actions.** Other stuff entrants do to qualify to win. I
  source: >-
    100m-money-models.md, Giveaways, Description, line 1564
  confirmations: 1
  anchor_at: "100m-money-models.md:1564"
  tier: 1
- id: E-money-models-011
  type: term
  name: >-
    Decoy Offer
  statement: >-
    A Decoy Offer advertises something free or discounted, and when leads engage both the decoy and a more valuable premium offer are presented side by side.
  definition: >-
    Decoy Offers advertise something free or discounted. Then, when leads ask to learn more, you also present a more valuable premium offer. The premium offer provides more features, benefits, bonuses, guarantees, and so on.
  why: >-
    By putting decoy and premium side by side leads see how much more valuable the premium is; either way you close everyone, which makes getting new customers cheap and profitable.
  not_to_confuse_with: >-
    The premium offer itself: the decoy is deliberately a lesser, smaller or simpler version of the premium offer, made by offering fewer components, older models, less personalisation and no guarantees.
  anchor: >-
    Decoy Offers advertise something free or discounted. Then, when leads
  source: >-
    100m-money-models.md, Decoy Offer, Description, line 1866
  confirmations: 5
  anchor_at: "100m-money-models.md:1866"
  tier: 1
  merged_from: [C-money-models-018, C-money-models-019]
- id: E-money-models-013
  type: term
  name: >-
    Pay Less Now or Pay More Later
  statement: >-
    Pay Less Now or Pay More Later gives people a choice between paying full price later, only if satisfied, and paying a discounted price now with bonuses.
  definition: >-
    In Pay Less Now or Pay More Later, you give people a choice to pay full-price later OR pay a discounted price now. The pay now option offers a 20-50% discount and bonuses if they pay now.
  why: >-
    It removes all risk from the customer, combining a delayed payment with a satisfaction guarantee, and the pay later option lets you advertise free while still getting their card on file.
  not_to_confuse_with: >-
    Trial With Penalty: the author uses Pay Less Now or Pay More Later as a downsell for physical products or one-time services, and Trial With Penalty as a downsell for recurring products or services.
  anchor: >-
    In Pay Less Now or Pay More Later, you give people a choice to pay
  source: >-
    100m-money-models.md, Pay Less Now or Pay More Later, Description, line 2334
  confirmations: 3
  anchor_at: "100m-money-models.md:2334"
  tier: 1
- id: E-money-models-014
  type: term
  name: >-
    Conditional Satisfaction Guarantee
  statement: >-
    A conditional satisfaction guarantee lets the customer cancel the billing only if they meet stated conditions, usually the actions that get them the most value from the product.
  definition: >-
    People can only cancel the billing if they qualify. So, be sure to track the conditions necessary to qualify. Think: attendance, showing up to an appointment, turning in data, etc. Make the criteria what people do to get the most value out of the product.
  why: >-
    They can't say you suck if they never try it.
  anchor: >-
    **Make a Conditional Satisfaction Guarantee.** *People can only cancel
  source: >-
    100m-money-models.md, Pay Less Now or Pay More Later, Important Notes, line 2415
  confirmations: 2
  anchor_at: "100m-money-models.md:2415"
  tier: 1
- id: E-money-models-015
  type: term
  name: >-
    Upsell Offer
  statement: >-
    An upsell is simply whatever you offer next — more of what they just got, a better version, or something new and complementary — offered the moment the previous offer reveals the next problem.
  definition: >-
    Anytime you offer something next, you upsell. Upsells just mean whatever we offer next. When an offer solves a problem, another appears. You upsell the solution to the problem your offer reveals.
  why: >-
    The thing you sell the most isn't always the thing you make the most profit on; often upsells make the majority of the profit and make or break a Money Model.
  anchor: >-
    Anytime you offer something *next*, you upsell. Upsells play a key role
  source: >-
    100m-money-models.md, Upsell Offers Conclusion, line 3720
  confirmations: 3
  anchor_at: "100m-money-models.md:3720"
  tier: 1
- id: E-money-models-016
  type: term
  name: >-
    The Classic Upsell
  statement: >-
    The Classic Upsell offers the solution to the customer's next problem the moment they become aware of it, in a You can't have X without Y structure.
  definition: >-
    The Classic Upsell offers a solution to the customer's next problem the moment they become aware of it. Your core offer solves one problem and creates another. Your upsell immediately solves that next problem. This gives the classic upsell its You can't have X without Y structure.
  why: >-
    Current customers always have a higher chance of buying your stuff than strangers, and when timed right customers upsell themselves.
  anchor: >-
    The Classic Upsell offers a solution to the customer's next problem *the
  source: >-
    100m-money-models.md, The Classic Upsell, Description, line 2754
  confirmations: 3
  anchor_at: "100m-money-models.md:2754"
  tier: 1
  merged_from: [C-money-models-030]
- id: E-money-models-017
  type: term
  name: >-
    Say No To Say Yes
  statement: >-
    Say No To Say Yes is the author's name for closing with you don't want anything else do you? — the habitual no is in fact agreement to what was just offered.
  definition: >-
    People had been trained to say no in response to you don't want anything else do you? But this actually turns a no into yes. So when upselling, the question translates to: You don't want anything [besides what I just offered] do you?
  anchor: >-
    **Get Them To "Say No To Say Yes."** I was always amazed at how often
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2818
  confirmations: 3
  anchor_at: "100m-money-models.md:2818"
  tier: 1
- id: E-money-models-019
  type: term
  name: >-
    BAMFAM
  statement: >-
    BAMFAM stands for Book-A-Meeting-From-A-Meeting: every appointment ends by scheduling the next one, so the customer knows the next time they see you and why before they leave.
  definition: >-
    Make sure you Book-A-Meeting-From-A-Meeting (BAMFAM). End every appointment by scheduling the next appointment. Don't let them leave without booking.
  why: >-
    The more times you can upsell, the more people you will upsell; if you upsell more people, you make more money.
  anchor: >-
    **Make Sure You Book-A-Meeting-From-A-Meeting (BAMFAM).** The more times
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2873
  confirmations: 2
  anchor_at: "100m-money-models.md:2873"
  tier: 1
- id: E-money-models-020
  type: term
  name: >-
    Menu Upsell
  statement: >-
    In a Menu Upsell you first tell customers which options they don't need, then what they do need, then ask their preference, then settle payment on the card on file.
  definition: >-
    In a Menu Upsell, you tell customers which options they don't need. Then, tell them what they do need, their preferences, and how to get their value from it. Menu Upsells combine up to four tactics: Unselling, Prescription Upselling, A/B Upselling, and Card On File.
  applies_when: >-
    Menu Upsells work best when you have multiple offers available.
  anchor: >-
    In a Menu Upsell, you tell customers which options they don't need.
  source: >-
    100m-money-models.md, Menu Upsell, Description, line 3084
  confirmations: 4
  anchor_at: "100m-money-models.md:3084"
  tier: 1
  merged_from: [C-money-models-035]
- id: E-money-models-021
  type: term
  name: >-
    Unselling
  statement: >-
    Unselling is telling customers what they don't need, crossing options out, so as to emphasise and excite them about what they do need.
  definition: >-
    You unsell by telling customers what they don't need so that you can emphasize what they do. Here, instead of asking if they want to buy it or not, you explain what they don't need as a way to get them excited about what they do.
  why: >-
    Going out of the way to cross out what the customer didn't need built enough goodwill to upsell what she did; unselling lower-margin stuff where appropriate incentivizes higher-margin upsells.
  anchor: >-
    *Unselling.* You unsell by telling customers what they don't need so
  source: >-
    100m-money-models.md, Menu Upsell, Description, line 3097
  confirmations: 3
  anchor_at: "100m-money-models.md:3097"
  tier: 1
- id: E-money-models-022
  type: term
  name: >-
    Prescription Upsell
  statement: >-
    A Prescription Upsell tells the customer what they do need and exactly how to use it, as if they already own it, instead of asking whether they want it.
  definition: >-
    We tell them what they do need. Prescription upselling has two important components. First, you have to explain how it integrates with offers they already bought. Second, you personalize and detail how to maximize its value. Here, instead of asking if they want to buy it or not, you explain how to use it as if they already have.
  applies_when: >-
    Prescription Upsells work well when offering a choice is inconvenient and you have only one thing that solves the problem.
  why: >-
    Detailed and personalized instructions upsell more people than vague and general suggestions; removing the option of not buying lowers the chance they don't buy.
  anchor: >-
    *Prescription Upsell.* We tell them what they do need. Prescription
  source: >-
    100m-money-models.md, Menu Upsell, Description, line 3104
  confirmations: 2
  anchor_at: "100m-money-models.md:3104"
  tier: 1
- id: E-money-models-023
  type: term
  name: >-
    A/B Upsell
  statement: >-
    An A/B Upsell asks which of two products the customer prefers rather than whether they want to buy at all, so either answer is a sale.
  definition: >-
    We ask them their preferences. A/B Upsells work for multiple offers that solve the same problem. Instead of asking if customers wanted to buy a product, yes or no, we ask which product they prefer: A or B. Either choice results in an upsell.
  why: >-
    When you give people the option to not buy, some don't buy; so the choice is between buying two similar things.
  anchor: >-
    *A/B Upsell.* We ask them their preferences. A/B Upsells work for
  source: >-
    100m-money-models.md, Menu Upsell, Description, line 3114
  confirmations: 4
  anchor_at: "100m-money-models.md:3114"
  tier: 1
  merged_from: [C-money-models-032]
- id: E-money-models-025
  type: term
  name: >-
    Anchor Upsell
  statement: >-
    In an Anchor Upsell the premium thing is offered first, and when the customer balks a cheaper but acceptable alternative with the same core functions is presented.
  definition: >-
    With Anchor Upsells, you offer premium stuff first. If the customer gasps, you offer a cheaper but acceptable alternative. Present the Anchor, get The Gasp, come to the rescue, present your main offer, ask how they wanna pay.
  why: >-
    If you present a premium version that's 5x-10x the price first, the main offer then looks like a much better deal, anchored customers spend more than they normally would, and some customers still buy the super expensive thing.
  applies_when: >-
    Anchor Upsells work best when the lower-price offer has the same core functions as the premium one.
  anchor: >-
    With Anchor Upsells, you offer premium stuff first. If the customer
  source: >-
    100m-money-models.md, Anchor Upsell, Description, line 3333
  confirmations: 3
  authors_caveat: >-
    If you treat the anchor like a fake, so will the customer: the premium offer must be one you actually want people to buy and actually sell.
  anchor_at: "100m-money-models.md:3333"
  tier: 1
  merged_from: [C-money-models-037]
- id: E-money-models-026
  type: term
  name: >-
    The Gasp
  statement: >-
    The Gasp is the customer's mini panic attack at the price of the anchor offer, and the signal to come to the rescue with the main offer.
  definition: >-
    When you do an anchor upsell correctly, customers will have mini panic attacks. I call this The Gasp. The bigger the gasp, the more they bought.
  why: >-
    If your customers don't gasp, then they probably find your premium offer reasonable — so just ask them if they wanna use the card on file.
  anchor: >-
    correctly, customers will have mini panic attacks. I call this "The
  source: >-
    100m-money-models.md, Anchor Upsell, Important Notes, line 3416
  confirmations: 2
  anchor_at: "100m-money-models.md:3416"
  tier: 1
- id: E-money-models-027
  type: term
  name: >-
    Rollover Upsell
  statement: >-
    A Rollover Upsell credits some or all of a customer's previous purchases toward the next, more expensive offer.
  definition: >-
    Rollover Upsells credit some or all of a customer's previous purchases toward your next offer. Once I know how much credit to give, I figure out three things: who to upsell, what to upsell, and how to roll over the credit.
  applies_when: >-
    Four situations: to re-engage customers who left a while ago, to rescue upset customers as a better alternative to a refund, to rescue other people's upset customers, and to upsell regular customers.
  anchor: >-
    Rollover Upsells credit some or all of a customer's previous purchases
  source: >-
    100m-money-models.md, Rollover Upsell, Description, line 3558
  confirmations: 5
  authors_caveat: >-
    Price the next offer at least 4x higher than the credit, so that applying the whole amount discounts 25% at most and the offer still makes a profit.
  anchor_at: "100m-money-models.md:3558"
  tier: 1
  merged_from: [C-money-models-040, E-lost-chapters-040]
- id: E-money-models-029
  type: term
  name: >-
    Downsell
  statement: >-
    A downsell is any offer made after someone says no: the original offer tweaked to find the highest value solution for that customer's budget, by changing how they pay or what they get.
  definition: >-
    Downselling tweaks the original offer to find the highest value solution for the customer's budget. So any offer you make after someone says no is a downsell. I downsell in two ways. I change how they pay or what they get.
  not_to_confuse_with: >-
    Discounting, which the author separates explicitly: dropping your price is not really downselling, it's discounting — the offer is never the same stuff for cheaper.
  anchor: >-
    Downselling tweaks the original offer to find the highest value solution
  source: >-
    100m-money-models.md, Section IV: Downsell Offers, line 3747
  confirmations: 3
  anchor_at: "100m-money-models.md:3747"
  tier: 1
- id: E-money-models-031
  type: term
  name: >-
    Seesaw Downselling
  statement: >-
    Seesaw Downselling is the short form of the payment plan process: it gradually shifts from paid-in-full to equal payments by adjusting the down payment until the monthly rate is acceptable.
  definition: >-
    Seesaw Downselling gradually shifts from paid-in-full to equal payments. Instead of asking for the full amount, just ask Would you rather have giant monthly payments or tiny ones? Then the more they put down now, the lower their monthly payments.
  applies_when: >-
    If you prefer fewer steps, or have less experienced salespeople.
  anchor: >-
    ● "Seesaw" Downselling gradually shifts from paid-in-full to equal
  source: >-
    100m-money-models.md, Payment Plan Downsells, Summary Points, line 4126
  confirmations: 3
  anchor_at: "100m-money-models.md:4126"
  tier: 1
  merged_from: [C-money-models-047]
- id: E-money-models-032
  type: term
  name: >-
    Trial With Penalty
  statement: >-
    In a Trial With Penalty the customer gets the product free so long as they meet stated terms, and pays a fee only where they fail to meet them.
  definition: >-
    In a Trial With Penalty offer, customers can try your product or service for free so long as they meet your terms. Customers only pay if they don't meet the terms.
  not_to_confuse_with: >-
    Win Your Money Back, which pays money back if the customer meets the terms, and an ordinary free trial: Trial With Penalty isn't here's my thing, see if you like it — it's here's my thing, you get it for free so long as you do this stuff, and if you don't, then you have to pay for it.
  applies_when: >-
    As a downsell for recurring products or services, and only in businesses where the customer has to do work to get results.
  anchor: >-
    In a Trial With Penalty offer, customers can try your product or service
  source: >-
    100m-money-models.md, Trial With Penalty, Description, line 4203
  confirmations: 4
  authors_caveat: >-
    Customer-facing, just call it a Free Trial: people may get scared and confused otherwise, since no one wants to be penalized.
  anchor_at: "100m-money-models.md:4203"
  tier: 1
  merged_from: [C-money-models-050]
- id: E-money-models-033
  type: term
  name: >-
    Feature Downsell
  statement: >-
    A Feature Downsell lowers the price by changing what the customer gets — less quantity, lower quality, a cheaper alternative, or cutting optional components.
  definition: >-
    Feature Downsells lower prices by changing what customers get. I do them by offering lesser quantity, lower quality, lower price alternatives, or cutting optional components. Take something away, lower the price, and in so many words ask how about now?
  not_to_confuse_with: >-
    A discount, which makes the same stuff cheaper; a Feature Downsell lowers the price by changing what they get.
  why: >-
    People see the value in what you removed after they see the price difference, so removing features from highest to lowest value gets customers to re-upsell themselves onto the more expensive offer.
  anchor: >-
    Feature Downsells lower prices by changing what customers get. I do them
  source: >-
    100m-money-models.md, Feature Downsells, Description, line 4559
  confirmations: 3
  anchor_at: "100m-money-models.md:4559"
  tier: 1
- id: E-money-models-035
  type: term
  name: >-
    Business terrorists
  statement: >-
    Business terrorists are people who demand to pay less for the same thing, and the author does not negotiate with them.
  definition: >-
    People who demand to pay less for the same thing are business terrorists. I don't negotiate with terrorists. If they want to pay less now — offer a payment plan. If they want to pay less overall — offer a feature downsell.
  anchor: >-
    **Remember, Never Negotiate The Price.** People who demand to pay less
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4679
  confirmations: 1
  anchor_at: "100m-money-models.md:4679"
  tier: 1
- id: E-money-models-036
  type: term
  name: >-
    The Minimum
  statement: >-
    The Minimum is the author's name for the cheapest named feature combination, chosen because the word implies the customer has to take at least that much.
  definition: >-
    I name my cheapest combination The Minimum. I like it because it implies they have to get at least that thing. If someone rejects all other packages, I just say so nothing more than the minimum package then? to get them to say no to say yes.
  not_to_confuse_with: >-
    The most expensive combination, which is named after an aspirational status — The Whale Package, The Total Transformation, High Roller.
  anchor: >-
    **I Name My Cheapest Combination "The Minimum."** I like it because it
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4714
  confirmations: 3
  anchor_at: "100m-money-models.md:4714"
  tier: 1
  merged_from: [C-money-models-060]
- id: E-money-models-037
  type: term
  name: >-
    Temperature Check
  statement: >-
    A Temperature Check is the pause after two refused changes in which you ask, on a scale from 1-10, how badly the person wants the thing, before continuing to downsell.
  definition: >-
    If you make two changes in a row and they still refuse, make sure they really want the thing. I'd say something like Got it. Real quick. I want to make sure. On a scale from 1-10 how bad do you want this?
  why: >-
    No payment plan will satisfy a customer who doesn't want the thing, so make sure the person actually wants it before putting more effort into selling it.
  anchor: >-
    **Temperature Check After Two Downsells (Like Payment Plans).** If you
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4719
  confirmations: 3
  anchor_at: "100m-money-models.md:4719"
  tier: 1
  merged_from: [C-money-models-046]
- id: E-money-models-038
  type: term
  name: >-
    Continuity Offer
  statement: >-
    A Continuity Offer provides ongoing value that customers make ongoing payments for until they cancel, so you sell once and get paid again and again.
  definition: >-
    Continuity Offers provide ongoing value that customers make ongoing payments for — until they cancel. They boost the profit from every customer and give you one last thing to sell.
  not_to_confuse_with: >-
    A payment plan: the author separates them himself — it's silly for someone to pay for a one-day workshop forever; it makes sense for them to pay until they cover the cost, and that makes it a payment plan.
  why: >-
    On their own Continuity Offers attract more customers but leave you strapped for cash today, which is why the author makes them last, after Attraction, Upsell and Downsell Offers.
  anchor: >-
    Continuity Offers *provide ongoing value that customers make ongoing
  source: >-
    100m-money-models.md, Continuity Offers Conclusion, line 5721
  confirmations: 4
  anchor_at: "100m-money-models.md:5721"
  tier: 1
- id: E-money-models-039
  type: term
  name: >-
    Continuity Bonus Offer
  statement: >-
    With a Continuity Bonus you give the customer an awesome thing if they sign up today, where the bonus itself typically has more value than the first continuity payment.
  definition: >-
    With Continuity Bonuses you give the customer an awesome thing if they sign up today. Typically, the bonus itself has more value than the first continuity payment. That's all there is to it.
  why: >-
    Join my membership program isn't nearly as compelling as get this free valuable thing, so you advertise the bonus and explain the rest after they show interest.
  anchor: >-
    With Continuity Bonuses you give the customer an awesome thing *if* they
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Description, line 4991
  confirmations: 3
  authors_caveat: >-
    Keep bonuses related to the core offer, or you attract the wrong customers; and use realistic bonus pricing, since made-up values won't anchor and lose trust.
  anchor_at: "100m-money-models.md:4991"
  tier: 1
- id: E-money-models-041
  type: term
  name: >-
    Continuity Discount Offer
  statement: >-
    A Continuity Discount Offer gives products or services away free — now or later — if the customer commits to buying more over time.
  definition: >-
    To make a one-time continuity discount, you give products or services away for free if the customer commits to buying more products and services over time. Continuity Discount Offers give continuity time for free if the customer signs up today.
  not_to_confuse_with: >-
    Buy X Get Y Free: the author says this looks like Buy X Get Y Free done continuity-style and that you'd be right, but there are enough differences specific to continuity that it justified its own chapter.
  applies_when: >-
    You know two things: how you'll apply the discount (up front, at the end, an even spread, or after the first month or two) and your cancellation policy.
  anchor: >-
    To make a one-time continuity discount, you give products or services
  source: >-
    100m-money-models.md, Continuity Discount Offers, Description, line 5314
  confirmations: 4
  anchor_at: "100m-money-models.md:5314"
  tier: 1
  merged_from: [C-money-models-070]
- id: E-money-models-042
  type: term
  name: >-
    Lifetime Discount
  statement: >-
    A lifetime discount is a permanently lower rate the customer earns by staying past a set point, which the author puts at the month of greatest churn.
  definition: >-
    You advertise the lifetime discount. But, you make customers earn it. They get a lower rate if they stay past X period. Make X the month your average customer drops off.
  why: >-
    Allowing customers to earn a lifetime discount at your month of greatest churn encourages customers to stick through it for a lifetime lower rate.
  anchor: >-
    **Try Lifetime Discount At Your Most Common Churn Point.** You advertise
  source: >-
    100m-money-models.md, Continuity Discount Offers, Important Notes, line 5439
  confirmations: 5
  anchor_at: "100m-money-models.md:5439"
  tier: 1
  merged_from: [C-money-models-072, E-lost-chapters-039]
- id: E-money-models-043
  type: term
  name: >-
    Waived Fee Offer
  statement: >-
    A Waived Fee Offer presents a month-to-month option carrying a startup fee of 3-5x the monthly rate, and waives that fee entirely if the customer commits long term — with the fee payable if they cancel inside the term.
  definition: >-
    Waived Fee Offers work like this. First, you ask the customer to pay a startup fee as part of joining a month-to-month program. Typically, I do 3-5x my monthly rate. Then, you offer to discount the entire fee if they commit longer term. But, if they cancel inside the term, they pay the fee.
  why: >-
    Customers will stay longer if leaving costs more than staying: fees get them to start because committing immediately avoids a fee, and fees get them to stick for the same reason.
  applies_when: >-
    Commitments of one year and longer; it works especially well with services that take a long time to work.
  anchor: >-
    Waived Fee Offers work like this. First, you ask the customer to pay a
  source: >-
    100m-money-models.md, Waived Fee Offer, Description, line 5594
  confirmations: 4
  authors_caveat: >-
    If more than 5% of people want to cancel early, look into it: pricing incentivizes sticking but it can't and shouldn't overcome a terrible product.
  anchor_at: "100m-money-models.md:5594"
  tier: 1
  merged_from: [C-money-models-075]
```
