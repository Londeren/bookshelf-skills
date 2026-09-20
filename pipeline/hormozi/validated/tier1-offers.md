# $100M Offers (2021) — ярус 1, группа `tier1-offers`, единиц после валидации: 137

Часть `pipeline/hormozi/validated.md` (там шапка, гейт, список валидаторов и правила обращения с якорем). Блоки перенесены из `pipeline/hormozi/catch/tier1-offers-<X>.md` байт в байт; фазой 2 дописаны `tier`, `merged_from` и поднятое `confirmations`. Проверка: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/validated/tier1-offers.md`.


## A. Фреймворки — 22

```yaml
- id: A-offers-001
  type: framework
  name: >-
    The Value Equation
  statement: >-
    Value is built from four drivers: raise the Dream Outcome and the Perceived Likelihood of Achievement, and cut the Perceived Time Delay and the Perceived Effort & Sacrifice.
  why: >-
    It is written as a division and not an addition on purpose: if the bottom of the equation goes to zero, value is infinite, so the bottom side is where the hardest and most rewarding work sits.
  applies_when: >-
    Quantifying and increasing the value of any offer before raising its price.
  structure:
    - >-
      (Yay) The Dream Outcome (Goal: Increase)
    - >-
      (Yay) Perceived Likelihood of Achievement (Goal: Increase)
    - >-
      (Boo) Perceived Time Delay Between Start and Achievement (Goal: Decrease)
    - >-
      (Boo) Perceived Effort & Sacrifice (Goal: Decrease)
  anchor: >-
    As you can see from the picture, there are four primary drivers of value. Two of the drivers (on top), you will seek to increase. The other two (on the bottom), you will seek to decrease.
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 31
  confirmations: 4
  authors_caveat: >-
    All four drivers are perceived ones: the offer becomes valuable only once the prospect perceives the increase in likelihood and the decrease in time delay and effort, so the drivers have to be communicated, not merely delivered.
  anchor_at: "100m-offers.md:31"
  tier: 1
  merged_from: [B-offers-010]
- id: A-offers-004
  type: framework
  name: >-
    Presenting Bonuses 1-on-1
  statement: >-
    In one-on-one selling, ask for the sale first and reveal the bonuses only after they sign up; if they do not buy, present a bonus that matches their perceived obstacle and ask again.
  why: >-
    Revealing bonuses after the yes creates a wow experience that reinforces the decision to buy, and people have a hard time rejecting reciprocity, so an added bonus makes them feel almost obligated to buy.
  applies_when: >-
    Selling one on one rather than to a group.
  structure:
    - >-
      you ask for the sale first, before offering the bonuses
    - >-
      If they say yes, then after they have signed up, you let them know the additional bonuses they're going to get
    - >-
      if the person does not buy after the first ask, then you present a bonus that matches their perceived obstacle, then ask again
  anchor: >-
    When selling one on one, you ask for the sale *first,* before offering the bonuses. If they say yes, then after they have signed up, you let them know the *additional* bonuses they're going to get.
  source: >-
    100m-offers.md, ch. 14 Bonuses, line 295
  confirmations: 4
  authors_caveat: >-
    Group selling is beyond the scope of this book; this sequence is stated for the 1-1 selling scenario.
  anchor_at: "100m-offers.md:295"
  tier: 1
  merged_from: [B-offers-013, B-offers-014, D-offers-008]
- id: A-offers-005
  type: framework
  name: >-
    Bonus Bullets
  statement: >-
    An eleven-point checklist for offering bonuses: always offer them, name them with a benefit, explain and prove them, price them, and make each one kill a specific obstacle.
  why: >-
    Enumerating and stacking the parts increases the prospect's perception of the offer's value and expands the price-to-value discrepancy until it is too big to bear.
  applies_when: >-
    Assembling and presenting the bonus stack of an offer.
  structure:
    - >-
      Always offer them (you can use the bulleted bundle we came up with at the end of Section III)
    - >-
      Give them a special name that has a benefit in the title
    - >-
      Tell them: a) How it relates to their issue b) What it is c) How you discovered it, or what you had to do to create it d) How it will specifically improve their lives
    - >-
      Provide some proof (this can be a stat, a past client, or personal experience) to prove that this thing is valuable
    - >-
      Paint a vivid mental image of what their life will be like assuming they have already used it and are experiencing the benefits
    - >-
      Always ascribe a price tag to them and justify it
    - >-
      Tools & checklists are better than additional trainings
    - >-
      They should each address a specific concern/obstacle in the prospects mind about why they can’t or won’t be successful
    - >-
      This can also be what they would logically realize they will need next
    - >-
      The value of the bonuses should eclipse the value of the core offer
    - >-
      You can further enhance the value of your bonuses by adding scarcity and urgency to the bonus themselves
  anchor: >-
    That being said, there are a few key things to remember when offering bonuses:
  source: >-
    100m-offers.md, ch. 14 Bonuses, lines 303–335
  confirmations: 8
  anchor_at: "100m-offers.md:303"
  tier: 1
  merged_from: [B-offers-015, B-offers-016, B-offers-017, B-offers-018, B-offers-019, B-offers-020, B-offers-021]
- id: A-offers-006
  type: framework
  name: >-
    Advanced Level Bonuses - Other People’s Products and Services
  statement: >-
    Get non-competing businesses to give their products and services as your bonuses in exchange for free exposure to your customers, then negotiate a group discount and a commission for yourself on top.
  why: >-
    It is free marketing for them and high value products for you at no cost; with enough of these relationships you can justify your entire price in savings and true-to-price bonuses, and each bonus becomes a revenue stream.
  applies_when: >-
    Raising the value of an offer without raising your own cost of fulfilment.
  structure:
    - >-
      get other businesses to give you their services and products as a part of your bonuses in exchange for exposure to your clients for free
    - >-
      As long as they are not direct competitors
    - >-
      repeat the above for multiple service providers
    - >-
      negotiate a group discount and a commission to yourself
    - >-
      come up with a grand slam offer with these partner businesses by using the same concepts in the book
  anchor: >-
    You can get other businesses to give you their services and products as a part of your bonuses in exchange for exposure to your clients for free.
  source: >-
    100m-offers.md, ch. 14 Bonuses, lines 351–391
  confirmations: 3
  anchor_at: "100m-offers.md:351"
  tier: 1
  merged_from: [B-offers-022, D-offers-010]
- id: A-offers-010
  type: framework
  name: >-
    Three scarcity caps for services
  statement: >-
    A service business creates honest scarcity with one of three caps: a total business cap, a growth rate cap per week, or a cohort cap per class.
  why: >-
    You can only handle a certain amount of new clients anyway, so you might as well let prospects know it; a cap creates a waiting list, and the moment the door opens price resistance disappears.
  applies_when: >-
    Using scarcity in a service business that wants customers consistently.
  structure:
    - >-
      Total Business Cap - Only accepting….X Clients
    - >-
      Growth Rate Cap - Only accepting X clients per week (on-going)
    - >-
      Cohort Cap - Only accepting….X clients per class or cohort
  anchor: >-
    With services, especially if you want to consistently get customers, it can be a little trickier to use scarcity. But I will show you a few simple ways to employ scarcity ethically to increase your take rates on offers.
  source: >-
    100m-offers.md, ch. 12 Scarcity, lines 573–581
  confirmations: 2
  authors_caveat: >-
    Always have less spots available than you think you can sell, so that you sell out and can point to it next time.
  anchor_at: "100m-offers.md:573"
  tier: 1
  merged_from: [D-offers-018]
- id: A-offers-012
  type: framework
  name: >-
    If you do not get X result in Y time period, we will Z
  statement: >-
    A guarantee is written as a conditional statement with three slots: the result X, the time period Y, and what you will do if they do not get it, Z.
  why: >-
    The or-what portion is what gives a guarantee teeth; without it the guarantee sounds weak and diluted, which is what most marketers do.
  applies_when: >-
    Wording any guarantee.
  structure:
    - >-
      X result
    - >-
      Y time period
    - >-
      we will Z
  anchor: >-
    What makes a guarantee have power is a conditional statement: If you do not get X result in Y time period, we will Z.
  source: >-
    100m-offers.md, ch. 15 Guarantees, lines 662–672
  confirmations: 4
  anchor_at: "100m-offers.md:662"
  tier: 1
  merged_from: [B-offers-041, D-offers-019]
- id: A-offers-013
  type: framework
  name: >-
    Stacking Guarantees
  statement: >-
    Guarantees stack: an unconditional one with a conditional one on top, or two conditional guarantees around different or sequential outcomes.
  why: >-
    Spelling out a sequence of outcomes with timelines future paces the prospect into an outcome they now believe is far more likely, and shifts the burden of risk from them onto you.
  applies_when: >-
    Strengthening an offer that already carries one guarantee.
  structure:
    - >-
      give an unconditional 30 day no questions asked guarantee then on top of that give a conditional triple your money back 90 day guarantee
    - >-
      stack two conditional guarantees around different (or sequential) outcomes
  anchor: >-
    For example, you could give an unconditional 30 day no questions asked guarantee then on top of that give a conditional triple your money back 90 day guarantee.
  source: >-
    100m-offers.md, ch. 15 Guarantees, lines 692–696
  confirmations: 2
  anchor_at: "100m-offers.md:694"
  tier: 1
  merged_from: [B-offers-046]
- id: A-offers-015
  type: framework
  name: >-
    Implied Guarantees: Performance Models, Revshares, and Profit-Sharing
  statement: >-
    Performance-based structures — performance fees, revshare, profit-share, ratchets and bonuses/triggers — carry an implied guarantee: if you do not perform, the client does not have to pay.
  why: >-
    It makes you accountable to your clients' results and weeds out low performers; perfect alignment between client and service provider fosters collaboration and a long-term relationship.
  applies_when: >-
    Offers with quantifiable outcomes, where you have transparency for measuring the outcome and trust or control that you will get compensated.
  structure:
    - >-
      Performance: A) ...Only pay me $XXX per sale/ $XXX per show B) $XX per Lb Lost
    - >-
      Revshare: A) 10% of top line revenue B) 20% profit share C) 25% of revenue growth from baseline
    - >-
      Profit-Share: A) X% of profit B) X% of Gross Profit
    - >-
      Ratchets: 10% if over X, 20% if over Y, 30% if over Z
    - >-
      Bonuses/Triggers: I get X when Y occurs.
  anchor: >-
    **What The Client Gets:** If you do not perform, they do not have to pay. If you perform,your compensation has been determined based on an agreement decided upon *before* you begin working.
  source: >-
    100m-offers.md, ch. 15 Guarantees, lines 821–843
  confirmations: 1
  authors_caveat: >-
    The drawbacks are tracking and collection; a revshare or performance setup can be paired with a minimum, such as the greater of $1000 or 10% of revenue generated.
  anchor_at: "100m-offers.md:835"
  tier: 1
- id: A-offers-018
  type: framework
  name: >-
    Virtuous Cycle of Price
  statement: >-
    Raising the price increases the client's emotional investment, their perceived value, their results, the quality of clients attracted, and your margin; lowering the price decreases all five.
  why: >-
    Clients who are invested get better results, and margin is what pays for an exceptional experience, the best people and growth; cutting price destroys the margin and attracts clients who are never satisfied until the service is free.
  applies_when: >-
    Deciding whether to compete on price.
  structure:
    - >-
      Increase your clients’ emotional investment
    - >-
      Increase your clients’ perceived value of your service
    - >-
      Increase your clients’ results because they value your service and are invested
    - >-
      Attract the best clients who are the easiest to satisfy and actually cost less to fulfill
    - >-
      Multiply your margin because you have money to invest in systems to create efficiency
  anchor: >-
    Let me introduce you to the virtuous cycle of price.
  source: >-
    100m-offers.md, ch. 5 Pricing: Charge What It’s Worth, lines 1166–1200
  confirmations: 8
  authors_caveat: >-
    Your product must deliver: to charge big ticket prices you must outwork your self doubt and be so confident in your delivery, because you have done it so many times, that you know this person will succeed.
  anchor_at: "100m-offers.md:1166"
  tier: 1
  merged_from: [A-playbooks-price-015, A-playbooks-price-016, B-offers-062, D-playbooks-price-038, D-playbooks-price-043, E-playbooks-price-017, E-playbooks-price-018]
- id: A-offers-019
  type: framework
  name: >-
    The Delicate Dance of Desire
  statement: >-
    All marketing works on the supply and demand curve: raise demand with persuasive communication to sell more units, cut supply to sell those units for more, and keep supply under the demand you generate.
  why: >-
    Desire comes from not getting what you want, so satisfying all the demand kills the golden goose, while unmet demand compounds into more desire and more urgency the next time you open.
  applies_when: >-
    Deciding how many units to sell and at what price when enhancing a core offer.
  structure:
    - >-
      We artificially increase the demand for our products and services through some sort of persuasive communication
    - >-
      When we increase the demand, we can sell more units
    - >-
      When we decrease supply, we can sell those units for more money
    - >-
      The “perfect profit combination” is lots of demand, and very little supply, or perceived supply
    - >-
      We must endeavor to keep our supply (and satisfaction of desire) under the demand that we are able to generate
  anchor: >-
    When we increase the demand, we can sell more units. When we decrease supply, we can sell those units for more money. The “perfect profit combination” is lots of demand, and very little supply, or *perceived* supply.
  source: >-
    100m-offers.md, ch. 11 Enhancing The Offer, lines 1518–1555
  confirmations: 4
  authors_caveat: >-
    This assumes a regular business who is not trying to gain mass market penetration for some other strategic advantage; and if you satisfy zero desire you will not make money and eventually leave people feeling rejected.
  anchor_at: "100m-offers.md:1522"
  tier: 1
  merged_from: [B-offers-063, D-offers-037, D-offers-038]
- id: A-offers-020
  type: framework
  name: >-
    The five offer enhancers
  statement: >-
    Five outside levers enhance a core offer without changing it: scarcity, urgency, bonuses, guarantees and names.
  why: >-
    These forces position the product in the prospect's mind and are often more powerful than the core offer itself; together they shift the demand curve in your favour.
  applies_when: >-
    The core offer is built and you are packaging it for the market.
  structure:
    - >-
      Use scarcity to decrease supply to raise prices (and indirectly increase demand through perceived exclusiveness)
    - >-
      Use urgency to increase demand by decreasing the action threshold of a prospect.
    - >-
      Use bonuses to increase demand (and increase perceived exclusivity).
    - >-
      Use guarantees to increase demand by reversing risk.
    - >-
      Use names to re-stimulate demand and expand awareness of my offer to my target audience.
  anchor: >-
    1. Use *scarcity* to decrease supply to raise prices (and indirectly increase demand through perceived exclusiveness)
  source: >-
    100m-offers.md, ch. 11 Enhancing The Offer, lines 1565–1569
  confirmations: 3
  authors_caveat: >-
    Scarcity, urgency, bonuses and guarantees were not the only persuasion tools at play in the story that opens the section; these are the ones the author treats as belonging to the offer rather than to selling.
  anchor_at: "100m-offers.md:1565"
  tier: 1
  merged_from: [D-offers-036]
- id: A-offers-021
  type: framework
  name: >-
    Four indicators of a market
  statement: >-
    Pick a market on four indicators: massive pain, purchasing power, easy to target, and growing.
  why: >-
    The degree of the pain is proportional to the price you can charge; the audience must be able to afford you; if you cannot find them you cannot market to them; and a growing market is a tailwind while a declining one fights every effort.
  applies_when: >-
    Choosing the market before building an offer for it.
  structure:
    - >-
      1) Massive Pain
    - >-
      2) Purchasing Power
    - >-
      3) Easy to Target
    - >-
      4) Growing
  anchor: >-
    When picking markets, I look for four indicators:
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market -- A Starving Crowd, lines 1627–1661
  confirmations: 11
  anchor_at: "100m-offers.md:1627"
  tier: 1
  merged_from: [B-offers-065, B-offers-068, B-offers-071, B-offers-072, B-offers-073, D-offers-041, D-offers-042, D-offers-043]
- id: A-offers-023
  type: framework
  name: >-
    Starving Crowd (market) > Offer Strength > Persuasion Skills
  statement: >-
    The three levers on success rank in this order: the market first, then the strength of the offer, then persuasion skills.
  why: >-
    A great rating on a higher-order piece overpowers anything lower on the scale, a normal rating passes the buck to the next part, and a bad rating stops the equation unless a great higher-priority component nullifies it.
  applies_when: >-
    Deciding where to put effort when a business is not working.
  structure:
    - >-
      Starving Crowd (market)
    - >-
      Offer Strength
    - >-
      Persuasion Skills
  anchor: >-
    Starving Crowd (market) > Offer Strength > Persuasion Skills
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market -- A Starving Crowd, lines 1675–1687
  confirmations: 3
  authors_caveat: >-
    The whole book sits atop the assumption of at least a normal market; in a bad market nothing that follows will work.
  anchor_at: "100m-offers.md:1679"
  tier: 1
  merged_from: [B-offers-074, D-offers-040]
- id: A-offers-024
  type: framework
  name: >-
    M-A-G-I-C naming formula
  statement: >-
    Name an offer out of five components: a magnetic reason why, the avatar, the goal, the time interval and a container word.
  why: >-
    Each component maps to a job in the prospect's head — Attention, Discrimination, Purpose, Timeline and Method — and the container word signals a bundle that cannot be held up to a commoditized alternative.
  applies_when: >-
    Naming a program, a service, a promotion, and each item inside the stack.
  structure:
    - >-
      Make a Magnetic “Reason Why”
    - >-
      Announce Your Avatar
    - >-
      Give Them A Goal
    - >-
      Indicate a Time Interval
    - >-
      Complete With A Container Word
  anchor: >-
    If you like understanding the concepts behind my chosen M-A-G-I-C formula. Each roughly translates to: Attention (M-Magnet), Discrimination (A-Avatar), Purpose (G-Goal), Timeline (I-Interval), and Method (C-Container).
  source: >-
    100m-offers.md, ch. 16 Naming, lines 1991–2029
  confirmations: 6
  authors_caveat: >-
    Not all these components are mandatory: you will typically use three to five of them, they need not be in M-A-G-I-C order, and a quantifiable claim with a stated duration will not be approved on most platforms.
  anchor_at: "100m-offers.md:1991"
  tier: 1
  merged_from: [B-offers-079, B-offers-080, B-offers-087, D-offers-048]
- id: A-offers-025
  type: framework
  name: >-
    The order of change when offers fatigue
  statement: >-
    When an offer fatigues, change things in this order: creative, body copy, headline or wrapper, duration, the free/discount enhancer, and only last the monetization structure.
  why: >-
    Most of the time it is the first handful of items that need changing, and the lower on the list you go the more operationally heavy it is; changing the machine creates inefficiency and operational drag that costs money.
  applies_when: >-
    Lead flow from a working offer starts dropping, especially in a local market where offers fatigue faster.
  structure:
    - >-
      Change the creative (the images and pictures in your ads)
    - >-
      Change the body copy in your ads
    - >-
      Change the headline - the “wrapper” of your offer
    - >-
      Change the duration of your offer
    - >-
      Change the enhancer of your offer (your free/discount component)
    - >-
      Change the monetization structure, the series of offers you give prospects, and the price points associated with them (Book II)
  anchor: >-
    As you market offers, you will need to create variations over time as the tastes of the market change over time. Here’s the order in which you will change things to keep lead flow consistent.
  source: >-
    100m-offers.md, ch. 16 Naming, lines 2091–2110
  confirmations: 3
  authors_caveat: >-
    Reaching an audience one time in no way means an offer is fatigued; and once you’ve monetized an offer, rarely should you change it.
  anchor_at: "100m-offers.md:2091"
  tier: 1
  merged_from: [B-offers-088, D-offers-051]
- id: A-offers-029
  type: framework
  name: >-
    Create flow. Monetize flow. Then add friction.
  statement: >-
    Work in three stages: generate demand first, then get people to say yes with your offer, and only then add friction to the marketing or offer less for the same price.
  why: >-
    Practicality drives the order: without demand flowing in you cannot tell whether what you have is good, and optimising first leaves you with zero cash flow and zero idea what to adjust.
  applies_when: >-
    Sequencing the build of a business or a new offer.
  structure:
    - >-
      Create flow
    - >-
      Monetize flow
    - >-
      Then add friction
  anchor: >-
    I have always lived by the mantra, “Create flow. Monetize flow. Then add friction.” This means I generate demand *first*.
  source: >-
    100m-offers.md, ch. 10 Value Offer: Creating Your Grand Slam Offer Part II: Trim & Stack, line 2395
  confirmations: 6
  anchor_at: "100m-offers.md:2395"
  tier: 1
  merged_from: [A-lost-chapters-004, B-lost-chapters-011, B-offers-095, D-lost-chapters-007, D-offers-058]
- id: A-offers-030
  type: framework
  name: >-
    Product Delivery Cheat Codes
  statement: >-
    Vary a delivery vehicle along six dimensions: level of personal attention, level of effort expected from the client, live medium, recording format, response speed, and the 10x to 1/10th test.
  why: >-
    Stretching your mind in either direction gives widely different solutions, and solutions to one problem will give you ideas for others you would not normally have considered.
  applies_when: >-
    Step #4, inventing all the ways you could deliver a solution to each problem.
  structure:
    - >-
      What level of personal attention do I want to provide? one-on-one, small group, one to many
    - >-
      What level of effort is expected from them? Do it themselves (DIY); do it with them (DWY); done for them (DFY)
    - >-
      If doing something live, what environment or medium do I want to deliver it in? In-person, phone support, email support, text support, Zoom support, chat support
    - >-
      If doing a recording, how do I want them to consume it? Audio, video, or written.
    - >-
      How quickly do we want to reply? On what days? during what hours?
    - >-
      10x to 1/10th test
  anchor: >-
    1. What level of personal attention do I want to provide? one-on-one, small group, one to many
  source: >-
    100m-offers.md, ch. 10 Value Offer: Creating Your Grand Slam Offer Part II: Trim & Stack, lines 2460–2471
  confirmations: 1
  anchor_at: "100m-offers.md:2466"
  tier: 1
- id: A-offers-031
  type: framework
  name: >-
    10x to 1/10th test
  statement: >-
    Ask what you would provide if customers paid 10x your price, and how you would make the product more valuable if they paid one tenth of it.
  why: >-
    Stretching your mind in either direction produces widely different solutions than the version you would default to.
  applies_when: >-
    Generating delivery ideas when the obvious ones have run out.
  structure:
    - >-
      If my customers paid me 10x my price (or $100,000) what would I provide?
    - >-
      If they paid me 1/10th the price and I had to make my product more valuable than it already is, how would I do that? How could I still make them successful for 1/10th price?
  anchor: >-
    6. 10x to 1/10th test. If my customers paid me 10x my price (or $100,000) what would I provide?
  source: >-
    100m-offers.md, ch. 10 Value Offer: Creating Your Grand Slam Offer Part II: Trim & Stack, line 2471
  confirmations: 2
  anchor_at: "100m-offers.md:2471"
  tier: 1
  merged_from: [B-offers-098]
- id: A-offers-032
  type: framework
  name: >-
    Trim & Stack (Step #5)
  statement: >-
    Trim the list of delivery vehicles by cost and value — cut high cost, low value first, then low cost, low value — keeping only low cost, high value and high cost, high value items, then stack what remains into one deliverable.
  why: >-
    High value, one to many solutions typically have the biggest discrepancy between cost and value: a high one-time cost of creation and infinitely low additional effort after, which creates high margin profit for years.
  applies_when: >-
    After the list of possible delivery vehicles has been generated.
  structure:
    - >-
      I remove the ones that are high cost and low value first
    - >-
      Then I remove low cost, low value items
    - >-
      What should remain are offer items that are 1) low cost, high value and 2) high cost, high value
    - >-
      If there’s one type of delivery vehicle to focus on, it’s creating high value, “one to many” solutions
    - >-
      Put all the bundles together into the ultimate high value deliverable
  anchor: >-
    Next, I look at the cost of providing these solutions to me (the business). I remove the ones that are high cost and low value first. Then I remove low cost, low value items.
  source: >-
    100m-offers.md, ch. 10 Value Offer: Creating Your Grand Slam Offer Part II: Trim & Stack, lines 2487–2518
  confirmations: 5
  authors_caveat: >-
    That doesn’t mean you never do something in a small group or one-on-one model; you want to save those high cost items for big value adds only.
  anchor_at: "100m-offers.md:2489"
  tier: 1
  merged_from: [B-offers-100, B-offers-102, B-offers-104]
- id: A-offers-034
  type: framework
  name: >-
    The five steps of creating a Grand Slam Offer
  statement: >-
    Build the core offer in five steps: identify the dream outcome, list the problems, turn them into solutions, invent the delivery vehicles, then trim and stack them into one deliverable.
  why: >-
    Working through every problem and every possible way of solving it is what produces an offer that cannot be compared to anything else in the marketplace, so the prospect makes a value-based rather than a price-based decision.
  applies_when: >-
    Creating the core offer, before any enhancement.
  structure:
    - >-
      Step #1: We figured out our prospective client's dream outcome.
    - >-
      Step #2: We listed out all the obstacles they’re likely to encounter on their way (our opportunities for value).
    - >-
      Step #3: We listed all those obstacles as solutions.
    - >-
      Step #4: We figured out all the different ways we could deliver those solutions.
    - >-
      Step #5a: We trimmed those ways down to only the things that were the highest value and lowest cost to us.
    - >-
      Step #5b: Put all the bundles together into the ultimate high value deliverable.
  anchor: >-
    **Step #4:** We figured out all the different ways we could deliver those solutions.
  source: >-
    100m-offers.md, ch. 10 Value Offer: Creating Your Grand Slam Offer Part II: Trim & Stack, lines 2520–2536
  confirmations: 3
  authors_caveat: >-
    Steps #1–#3 are set out in ch. 9 and steps #4–#5 in ch. 10; the numbered list itself appears as the recap at lines 2520–2536.
  anchor_at: "100m-offers.md:2530"
  tier: 1
- id: A-offers-035
  type: framework
  name: >-
    Problem → Solution Wording→ Sexier Name for Bundle
  statement: >-
    Present each part of the stack as the problem, then the solution wording, then a sexier name for the bundle, with the actual delivery vehicles listed underneath.
  why: >-
    Presented this way the bundle solves all the perceived problems, gives you the conviction that what you sell is one of a kind, and makes the offering impossible to compare with the one down the street.
  applies_when: >-
    Writing out the final high value deliverable.
  structure:
    - >-
      Problem
    - >-
      Solution Wording
    - >-
      Sexier Name for Bundle
    - >-
      the actual delivery vehicle (what we’re actually gonna do for them/provide)
  anchor: >-
    Problem → Solution Wording→ Sexier Name for Bundle .
  source: >-
    100m-offers.md, ch. 10 Value Offer: Creating Your Grand Slam Offer Part II: Trim & Stack, lines 2540–2588
  confirmations: 1
  anchor_at: "100m-offers.md:2544"
  tier: 1
- id: A-offers-039
  type: framework
  name: >-
    The four problem buckets
  statement: >-
    Every problem a prospect has falls into one of four buckets matching the value drivers: it will not be financially worth it, it will not work for me, it will be too hard, and it will take too much time.
  why: >-
    Our problems always relate to those drivers, and our solutions provide the answer that gives a prospect permission to purchase; if only one of these needs is missing in a solution, it can cause someone not to buy.
  applies_when: >-
    Step #2, listing out every problem the prospect will encounter.
  structure:
    - >-
      Dream Outcome→ This will not be financially worth it
    - >-
      Likelihood of Achievement→ It won’t work for me specifically. I won't be able to stick with it. External factors will get in my way.
    - >-
      Effort & Sacrifice→ This will be too hard, confusing. I won’t like it. I will suck at it.
    - >-
      Time→ This will take too much time to do. I am too busy to do this. It will take too long to work.
  anchor: >-
    Now we’re gonna go full circle here. Each of the above problems has four negative elements. And you guessed it, each aligns with the four value drivers as well.
  source: >-
    100m-offers.md, ch. 9 Value Offer: Creating Your Grand Slam Offer Part I: Problems & Solutions, lines 2898–2905
  confirmations: 3
  authors_caveat: >-
    Don’t let these buckets, which are just meant to get your brain going, constrain you; if it’s easier, just list out everything you can possibly think of.
  anchor_at: "100m-offers.md:2898"
  tier: 1
  merged_from: [B-offers-110, D-offers-061]
```


## B. Правила и критерии — 47

```yaml
- id: B-offers-001
  type: rule
  name: >-
    Get the bottom of the equation to zero
  statement: >-
    Work on the offer attacks the two bottom drivers of the Value Equation, time delay and effort and sacrifice, harder than it attacks the claims on the top.
  why: >-
    Larger-than-life claims are the easiest to establish and therefore the least unique, since anyone can make a promise; time delay and effort are the harder and more competitive side, and the marketplace rewards making things immediate, seamless and effortless.
  applies_when: >-
    Any offer being built or improved.
  anchor: >-
    The harder, and more competitive, are the Time Delay and Effort & Sacrifice. The best companies in the world focus all their attention on the bottom side of the equation.
  source: >-
    100m-offers.md, ch. 6 The Value Equation, line 49
  confirmations: 3
  anchor_at: "100m-offers.md:49"
  tier: 1
  merged_from: [D-offers-002]
- id: B-offers-003
  type: rule
  name: >-
    Logical vs Psychological Solutions
  statement: >-
    When a problem in the offer or the business resists the obvious fix, a psychological solution is tried rather than a bigger logical one.
  why: >-
    Logical solutions have usually already been tried precisely because they are logical, so what is left are the psychological problems.
  anchor: >-
    As a business owners and entrepreneurs I increasingly approach problems to find *psychological* solutions, rather than *logical* ones.
  source: >-
    100m-offers.md, ch. 6 The Value Equation, line 71
  confirmations: 3
  anchor_at: "100m-offers.md:71"
  tier: 1
  merged_from: [D-offers-004]
- id: B-offers-005
  type: rule
  name: >-
    Talk in terms of status
  statement: >-
    The dream outcome in the offer is expressed in terms of the status the prospect believes it will gain them.
  why: >-
    In general the dream outcome that most directly increases a prospect's status is the one they value most, so whole categories of offers are valued above others for that reason alone.
  anchor: >-
    Talk in termsof things your prospect believes will increase their status, and you will have your prospects drooling.
  source: >-
    100m-offers.md, ch. 6 The Value Equation, line 149
  confirmations: 3
  anchor_at: "100m-offers.md:149"
  tier: 1
  merged_from: [B-offers-006]
- id: B-offers-009
  type: rule
  name: >-
    Fast Beats Free
  statement: >-
    In a market where the competition is free, the offer competes on speed.
  why: >-
    The only thing that beats free is fast; many companies have entered free spaces and done exceedingly well with a speed-first strategy, and many will always pay for the value of speed.
  applies_when: >-
    You find yourself in a market competing against free.
  anchor: >-
    So if you find yourself in a market competing against free, double down on speed.
  source: >-
    100m-offers.md, ch. 6 The Value Equation, line 201
  confirmations: 1
  anchor_at: "100m-offers.md:201"
  tier: 1
- id: B-offers-011
  type: rule
  name: >-
    Break the offer into component parts and stack them
  statement: >-
    The deliverables of the offer are enumerated and presented one at a time as stacked bonuses rather than as one undifferentiated offer.
  why: >-
    Until the pieces are enumerated they are unknown to the prospect; each added bonus widens the price-to-value discrepancy without cutting the price, anchored to the core offer.
  anchor: >-
    *a single offer is less valuable than* *the same offer broken into its component parts and stacked as bonuses (see image)*
  source: >-
    100m-offers.md, ch. 14 Bonuses, line 281
  confirmations: 2
  anchor_at: "100m-offers.md:281"
  tier: 1
- id: B-offers-012
  type: rule
  name: >-
    Never discount the main offer
  statement: >-
    When closing a deal, the price of the core offer is never discounted; value is added with bonuses instead.
  why: >-
    A discount teaches customers that your prices are negotiable and puts you in a position of weakness; adding bonuses keeps the price intact and puts you in a position of strength and goodwill.
  applies_when: >-
    Whenever trying to close a deal on a core offer.
  anchor: >-
    Whenever trying to close a deal, never discount the main offer. It teaches your customers that your prices are negotiable
  source: >-
    100m-offers.md, ch. 14 Bonuses, line 291
  confirmations: 1
  anchor_at: "100m-offers.md:291"
  tier: 1
- id: B-offers-023
  type: rule
  name: >-
    Wow Factor decides bonus versus core offer
  statement: >-
    What is pulled out of the deliverables and highlighted as a bonus is the most distinct piece that can almost stand on its own, especially one short in length but high in value.
  why: >-
    When there is so much stuff in the offer, valuable nuggets get lost in the mix; a checklist or infographic nobody would pay much for on its own is perceived as very valuable as a bonus.
  applies_when: >-
    Deciding what should be a bonus versus part of the core offer when you fulfil it yourself.
  anchor: >-
    You want to take the most distinct ones that can almost stand on their own and pull those out to highlight them. This is especially true for things that are short in length but high in quality or value.
  source: >-
    100m-offers.md, ch. 14 Bonuses, line 409
  confirmations: 2
  anchor_at: "100m-offers.md:409"
  tier: 1
  merged_from: [D-offers-009]
- id: B-offers-025
  type: rule
  name: >-
    Rolling Seasonal Urgency for local businesses
  statement: >-
    The same core service is re-released under a new seasonally named promotion with its own start and finish date instead of running the same campaign again.
  why: >-
    Naming it differently by season gives a real differentiator with a start and a finish, and deadlines drive decisions; local businesses must vary their marketing more frequently than national advertisers.
  applies_when: >-
    Local businesses; the author's number one strategy for them.
  anchor: >-
    Putting a new wrapper with a date on the same core service gives you urgency and novelty that will consistently outperform the “same old” campaigns.
  source: >-
    100m-offers.md, ch. 13 Urgency, line 471
  confirmations: 1
  anchor_at: "100m-offers.md:471"
  tier: 1
- id: B-offers-026
  type: rule
  name: >-
    Pricing or Bonus-Based Urgency
  statement: >-
    For a business that sells year round, the deadline is placed on the promotion, price or bonuses rather than on the availability of the service.
  why: >-
    It would be a lie to say you will not service them after the date, but talking specifically about the promotion elicits the same urgency while maintaining your integrity.
  applies_when: >-
    Businesses that sell clients year round.
  anchor: >-
    if you talk specifically about the promotion you can often elicit the same urgency on buying in the prospect while maintaining your integrity
  source: >-
    100m-offers.md, ch. 13 Urgency, line 477
  confirmations: 2
  anchor_at: "100m-offers.md:477"
  tier: 1
  merged_from: [D-offers-013]
- id: B-offers-027
  type: rule
  name: >-
    Clean Your Pipeline With Every Price Change
  statement: >-
    A price rise is announced to the existing pipeline before it takes effect.
  why: >-
    It shows a position of strength and gives an influx of cash from the people in the pipeline who were on the fence.
  applies_when: >-
    Whenever you are planning on raising your prices.
  anchor: >-
    Never raise your prices without letting people know.
  source: >-
    100m-offers.md, ch. 13 Urgency, line 479
  confirmations: 2
  anchor_at: "100m-offers.md:479"
  tier: 1
  merged_from: [D-offers-014]
- id: B-offers-028
  type: rule
  name: >-
    Exploding Opportunity
  statement: >-
    When the opportunity being sold decays with time, that decay is stated explicitly in the offer.
  why: >-
    Every second someone delays they miss out on disproportionate gains, which forces prospects to make fast decisions rather than wait it out for a better offer.
  applies_when: >-
    You are exposing the prospect to an arbitrage or market-inefficiency opportunity that corrects itself over time.
  anchor: >-
    All of these examples show opportunities that decay with time, so if you find yourself in front of an opportunity like this, make sure to emphasize it!
  source: >-
    100m-offers.md, ch. 13 Urgency, line 487
  confirmations: 1
  anchor_at: "100m-offers.md:487"
  tier: 1
- id: B-offers-030
  type: rule
  name: >-
    Always sell out
  statement: >-
    A limited release is sized so that it always sells out.
  why: >-
    It is better to sell out consistently than to over order and fail at creating the scarcity, and the method stacks in effectiveness when repeated over time.
  applies_when: >-
    Limited releases of physical products, flavors, colors, designs or sizes.
  anchor: >-
    Important point: to properly utilize this method you should *always* sell out.
  source: >-
    100m-offers.md, ch. 12 Scarcity, line 563
  confirmations: 4
  anchor_at: "100m-offers.md:563"
  tier: 1
  merged_from: [D-offers-015]
- id: B-offers-031
  type: rule
  name: >-
    Once a month is the sweet spot
  statement: >-
    Limited releases are repeated regularly but no more often than roughly once a month.
  why: >-
    The method stacks in effectiveness if it is done repeatedly over time, just not too often; once a month is the sweet spot for most of the companies the author knows who do this with regularity.
  anchor: >-
    it’s better to sell out consistently than over order and fail at creating that scarcity. This method stacks in effectiveness if it is done repeatedly over time (just not too often). Once a month seems to be the sweet spot
  source: >-
    100m-offers.md, ch. 12 Scarcity, line 565
  confirmations: 1
  anchor_at: "100m-offers.md:565"
  tier: 1
- id: B-offers-032
  type: rule
  name: >-
    Announce the sell-out
  statement: >-
    After a limited release sells out, everyone is told that it sold out.
  why: >-
    It gives social proof that other people thought it was worth it, and because the choice has been made for them they desire it more and are far more likely to take the next offer.
  anchor: >-
    Second Important Note: When using this tactic, you must also let everyone know that you sold out.
  source: >-
    100m-offers.md, ch. 12 Scarcity, line 567
  confirmations: 1
  anchor_at: "100m-offers.md:567"
  tier: 1
- id: B-offers-033
  type: rule
  name: >-
    Raise the cap by 10-20 percent, then cap again
  statement: >-
    Capacity under a total business cap is increased periodically by 10-20 percent and then capped again rather than opened.
  why: >-
    It keeps a waiting list in place so that the moment the door opens prospects jump in and price resistance disappears, always leaving some demand unmet.
  applies_when: >-
    Your highest tiers or service levels, run under a total business cap.
  anchor: >-
    Periodically, you can increase capacity by 10-20% then cap it again.
  source: >-
    100m-offers.md, ch. 12 Scarcity, line 575
  confirmations: 1
  anchor_at: "100m-offers.md:575"
  tier: 1
- id: B-offers-034
  type: rule
  name: >-
    Have less spots available than you think you can sell
  statement: >-
    The number of seats, spots or slots offered is set below what you believe you can sell.
  why: >-
    It is a compounding strategy: when you run it again everyone will remember that you sold out fast.
  applies_when: >-
    Higher ticket upsells such as one-off workshops, trainings, events, seminars and consulting.
  anchor: >-
    But always remember *have less spots available than you think you can sell*
  source: >-
    100m-offers.md, ch. 12 Scarcity, line 585
  confirmations: 2
  anchor_at: "100m-offers.md:585"
  tier: 1
  merged_from: [D-offers-016]
- id: B-offers-035
  type: rule
  name: >-
    Honest Scarcity
  statement: >-
    You define the number of clients you are willing to take in a given period, advertise that number, and publish how close to it you are.
  why: >-
    Letting people know you are three-fourths of the way to capacity moves them over the edge, and scarcity implies social proof, since a decent number of people already decided to work with you; only you get to draw the line where you are full.
  anchor: >-
    you might as well define a number that you are willing to take on in a given time period, then advertise that
  source: >-
    100m-offers.md, ch. 12 Scarcity, line 597
  confirmations: 2
  anchor_at: "100m-offers.md:597"
  tier: 1
- id: B-offers-036
  type: rule
  name: >-
    Once You're Out, You Can Never Come Back
  statement: >-
    A cap on the service level can be paired with a rule that anyone who leaves can never return.
  why: >-
    This type of scarcity makes people think extra hard about leaving.
  applies_when: >-
    Small groups.
  anchor: >-
    This works best with small groups (like the above example). As groups become much bigger, the tactic loses some teeth
  source: >-
    100m-offers.md, ch. 12 Scarcity, line 611
  confirmations: 2
  authors_caveat: >-
    As groups become much bigger the tactic loses some teeth, which the author says from experience.
  anchor_at: "100m-offers.md:611"
  tier: 1
  merged_from: [D-offers-017]
- id: B-offers-037
  type: rule
  name: >-
    Spend disproportionate time on risk reversal
  statement: >-
    The time spent designing the guarantee is disproportionate to the time spent on the rest of the offer.
  why: >-
    Risk is the single greatest objection for any product or service, so reversing it is an immediate way to make any offer more attractive; Jason Fladlien saw conversion on an offer 2-4x simply by changing the quality of the guarantee.
  anchor: >-
    You will want to spend a disproportionate amount of time figuring out how you want to reverse it.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 627
  confirmations: 2
  anchor_at: "100m-offers.md:627"
  tier: 1
- id: B-offers-038
  type: rule
  name: >-
    Always hit your guarantee hard
  statement: >-
    The guarantee is stated boldly with the reason why, even when the answer is that there is no guarantee.
  anchor: >-
    You must *always* hit your guarantee hard, even if you don't have one. Say it boldly and give the reason why.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 638
  confirmations: 1
  anchor_at: "100m-offers.md:638"
  tier: 1
- id: B-offers-039
  type: rule
  name: >-
    Judge a guarantee by net sales, not by refund fear
  statement: >-
    A guarantee is accepted or rejected on the arithmetic of net sales after refunds, not on the fear that people will take advantage of it.
  why: >-
    If you close 130 percent as many people and refunds double from 5 to 10 percent you still made 1.23x the money; for a guarantee not to be worth it the increase in sales would have to be fully offset by an equal absolute increase in refunds, which is unlikely.
  anchor: >-
    So, for the most part, the stronger the guarantee, the higher the *net* increase in total purchases, even if the refund rate increases alongside it.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 650
  confirmations: 3
  anchor_at: "100m-offers.md:650"
  tier: 1
  merged_from: [D-offers-020]
- id: B-offers-040
  type: rule
  name: >-
    High fulfilment cost means conditional or anti-guarantee
  statement: >-
    A business with a large cost of fulfilment uses a conditional guarantee or an anti-guarantee rather than an unconditional refund.
  why: >-
    With a refund you eat the cost of the refund and the cost of fulfilling it.
  applies_when: >-
    You have a tremendous amount of cost associated with your product or service.
  anchor: >-
    If you have a tremendous amount of cost associated with your product or service, you will likely want to employ a conditional guarantee or an ANTI guarantee
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 656
  confirmations: 3
  anchor_at: "100m-offers.md:656"
  tier: 1
  merged_from: [D-offers-022]
- id: B-offers-042
  type: rule
  name: >-
    Better than money back
  statement: >-
    A conditional guarantee promises something better than a refund of the money paid.
  why: >-
    If they are going to make an investment you want to match their investment psychologically with an equal or higher perceived commitment; given the choice between a refund and the outcome they were promised, the vast majority take the outcome.
  anchor: >-
    In general, you want these to be “better than money back” guarantees.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 682
  confirmations: 1
  anchor_at: "100m-offers.md:682"
  tier: 1
- id: B-offers-043
  type: rule
  name: >-
    Put the key actions into the conditions
  statement: >-
    The conditions of a conditional guarantee are the key actions the client must take to be successful.
  why: >-
    It has a very powerful effect on getting clients results, and it lets you reverse risk while keeping the client accountable; in a perfect world everyone qualifies for the guarantee but has achieved the result and does not want it.
  applies_when: >-
    You know the key actions someone must take in order to be successful.
  anchor: >-
    If you know the key actions someone must take in order to be successful, make those part of the conditional guarantee.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 682
  confirmations: 5
  anchor_at: "100m-offers.md:682"
  tier: 1
  merged_from: [B-offers-051, D-offers-021]
- id: B-offers-044
  type: rule
  name: >-
    An anti-guarantee needs a reason why
  statement: >-
    An all-sales-are-final policy is stated together with a creative reason why that shows a real exposure or vulnerability on your part.
  why: >-
    The reason must be something a consumer immediately understands and thinks makes sense; it acts as a damaging admission, and the more real exposure you can show the more effective it will be.
  applies_when: >-
    Items that are consumable or massively diminish in value once given, and high ticket products requiring a lot of work or customization.
  anchor: >-
    You must come up with a creative “reason why” the sales are final.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 686
  confirmations: 2
  anchor_at: "100m-offers.md:686"
  tier: 1
- id: B-offers-049
  type: rule
  name: >-
    Satisfaction guarantees only for low ticket and good fulfilment
  statement: >-
    A satisfaction or no-questions-asked guarantee is used only when you are good at fulfilling your promises and the ticket is low.
  why: >-
    It is the highest form of guarantee and means you could do everything right and still be asked for the money back; it becomes very risky as you go into higher-ticket services with higher costs of fulfilment.
  anchor: >-
    *But you have to be good at fulfilling your promises.* If not, steer clear. I believe this offer works much better in lower-ticket situations.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 732
  confirmations: 2
  anchor_at: "100m-offers.md:732"
  tier: 1
  merged_from: [D-offers-024]
- id: B-offers-054
  type: rule
  name: >-
    Start with service-based guarantees
  statement: >-
    The first guarantee a business adopts is a service-based guarantee or a performance partnership, and looser guarantees come later.
  why: >-
    It makes all sales final so there is no fear from refunds, and it commits you to your customers' results and keeps you honest; from there you either keep it and scale or move up to less restrictive guarantees to increase volume.
  anchor: >-
    My advice: Start selling service-based guarantees or setting up performance partnerships.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 853
  confirmations: 1
  anchor_at: "100m-offers.md:853"
  tier: 1
- id: B-offers-055
  type: rule
  name: >-
    Optimise for money, not for customer count
  statement: >-
    A pricing or offer decision is judged by how much money it makes, not by how many customers it brings.
  why: >-
    Getting people to buy is not the objective of a business; making money is.
  anchor: >-
    Getting people to buy is NOT the objective of a business. Making money is.
  source: >-
    100m-offers.md, ch. 5 Charge What It's Worth, line 1139
  confirmations: 6
  anchor_at: "100m-offers.md:1139"
  tier: 1
  merged_from: [B-playbooks-price-002, D-offers-032, D-playbooks-price-007, E-playbooks-price-004]
- id: B-offers-056
  type: rule
  name: >-
    Do not compete on price
  statement: >-
    Price is not used as the competitive lever unless you have a revolutionary way of getting your costs to one tenth of the competition's.
  why: >-
    Lowering price is a one-way road to destruction, because you can only go down to zero but infinitely high in the other direction.
  anchor: >-
    So, unless you have a revolutionary way of decreasing your costs to 1/10th compared to your competition, don't compete on price.
  source: >-
    100m-offers.md, ch. 5 Charge What It's Worth, line 1139
  confirmations: 3
  anchor_at: "100m-offers.md:1139"
  tier: 1
  merged_from: [D-offers-029, D-offers-031]
- id: B-offers-057
  type: rule
  name: >-
    Never be the second cheapest
  statement: >-
    A business is positioned as the most expensive in its marketplace rather than anywhere near the bottom.
  why: >-
    Dan Kennedy: there is no strategic benefit to being the second cheapest in the marketplace, but there is for being the most expensive.
  anchor: >-
    There is no strategic benefit to being the second cheapest in the marketplace, but there is for being the most expensive.
  source: >-
    100m-offers.md, ch. 5 Charge What It's Worth, line 1141
  confirmations: 3
  anchor_at: "100m-offers.md:1141"
  tier: 1
  merged_from: [D-playbooks-price-042]
- id: B-offers-058
  type: rule
  name: >-
    Raise the price only after raising the value
  statement: >-
    A price rise follows an increase in value, never precedes it, so the buyer still gets a deal.
  why: >-
    People buy to get a deal, believing the value exceeds the price; the moment value dips below what they are paying they stop buying, so the goal is more yeses at a higher price through a wider value-to-price discrepancy.
  anchor: >-
    In other words, we will raise our price only *after* we have sufficiently increased our value.
  source: >-
    100m-offers.md, ch. 5 Charge What It's Worth, line 1143
  confirmations: 1
  anchor_at: "100m-offers.md:1143"
  tier: 1
- id: B-offers-059
  type: rule
  name: >-
    Price far above the market, not slightly above
  statement: >-
    The price is set high enough that a consumer concludes something entirely different must be going on, not merely above the market average.
  why: >-
    Raising the price directly enhances the value the consumer perceives, and only a price that far above the market creates a category of one where you can make monopoly profits.
  anchor: >-
    And the goal isn’t just to be slightly above the market price — the goal is to be so much higher that a consumer thinks to themselves
  source: >-
    100m-offers.md, ch. 5 Charge What It's Worth, line 1210
  confirmations: 4
  anchor_at: "100m-offers.md:1210"
  tier: 1
  merged_from: [D-offers-033, D-offers-034]
- id: B-offers-060
  type: rule
  name: >-
    Price so that it stings
  statement: >-
    When the customer must do something to get the result, the price is set so that paying it stings a little.
  why: >-
    The more invested they are the more likely they are to achieve the result, and the sting forces and focuses their attention; those who pay the most pay the most attention.
  applies_when: >-
    You offer a service where a customer must do something in order to achieve the result.
  anchor: >-
    Ideally, this means pricing your services or product in such a way that it *stings* a little when they buy.
  source: >-
    100m-offers.md, ch. 5 Charge What It's Worth, line 1214
  confirmations: 1
  anchor_at: "100m-offers.md:1214"
  tier: 1
- id: B-offers-064
  type: rule
  name: >-
    Hormozi Law
  statement: >-
    The ask is delayed in proportion to its size: the longer you delay the ask, the bigger the ask you can make.
  why: >-
    The longer the runway, the bigger the plane that can take off.
  anchor: >-
    Hormozi Law: The longer you delay the ask, the bigger the ask you can make.
  source: >-
    100m-offers.md, ch. 11 Enhancing The Offer, line 1553
  confirmations: 1
  anchor_at: "100m-offers.md:1553"
  tier: 1
- id: B-offers-066
  type: rule
  name: >-
    Channel demand, do not create it
  statement: >-
    The offer channels demand that already exists in the market instead of trying to create demand.
  why: >-
    In order to sell anything you need demand, and if you do not have a market for your offer, nothing that follows will work.
  anchor: >-
    We are not trying to *create* demand. We are trying to *channel* it.
  source: >-
    100m-offers.md, ch. 4 Finding The Right Market, line 1621
  confirmations: 3
  anchor_at: "100m-offers.md:1621"
  tier: 1
  merged_from: [D-offers-005]
- id: B-offers-070
  type: rule
  name: >-
    Persuasion is judged by the prospect feeling understood
  statement: >-
    A piece of persuasive copy passes when the prospect feels understood, not merely when the reader understands it.
  why: >-
    The point of good writing is for the reader to understand; the point of good persuasion is for the prospect to feel understood.
  anchor: >-
    The point of good persuasion is for the prospect to feel *understood.*
  source: >-
    100m-offers.md, ch. 4 Finding The Right Market, line 1643
  confirmations: 3
  anchor_at: "100m-offers.md:1643"
  tier: 1
  merged_from: [B-offers-004, B-offers-069]
- id: B-offers-078
  type: rule
  name: >-
    Change the wrapper, not the offer
  statement: >-
    Refreshing a fatigued offer changes only its name and presentation; the services, products and work delivered stay the same.
  why: >-
    Offers fatigue over time and faster in local markets, but renaming keeps leads coming forever while the value stack is untouched.
  anchor: >-
    We are *not* changing the actual offer. We are only changing the *wrapping paper*.
  source: >-
    100m-offers.md, ch. 16 Naming, line 1971
  confirmations: 4
  authors_caveat: >-
    Reaching an audience one time in no way means an offer is fatigued; most people do not even notice an offer on the first mention (line 1969).
  anchor_at: "100m-offers.md:1971"
  tier: 1
  merged_from: [D-offers-047]
- id: B-offers-083
  type: rule
  name: >-
    Go hyper local in the avatar
  statement: >-
    A local headline names the sub-market or hyper local area rather than the city.
  why: >-
    The more local you can make your headline, the more it will convert.
  applies_when: >-
    When in a local area.
  anchor: >-
    You want to be as specific as possible, but no more. When in a local area, the more local you can make your headline, the more it will convert.
  source: >-
    100m-offers.md, ch. 16 Naming, line 2007
  confirmations: 1
  anchor_at: "100m-offers.md:2007"
  tier: 1
- id: B-offers-089
  type: rule
  name: >-
    Do not change a monetized offer
  statement: >-
    Once an offer has been monetized it is rinsed and repeated rather than changed, and the machine behind it is changed only as a last resort.
  why: >-
    Change here usually just creates inefficiency and operational drag, costing you money, and entrepreneurs love change for its own sake.
  anchor: >-
    Once you’ve monetized an offer, rarely should you change it.
  source: >-
    100m-offers.md, ch. 16 Naming, line 2108
  confirmations: 2
  anchor_at: "100m-offers.md:2108"
  tier: 1
- id: B-offers-090
  type: rule
  name: >-
    Nine percent a year is maintenance
  statement: >-
    A business growing slower than 9 percent year over year is treated as falling behind, not as maintaining.
  why: >-
    The market is continuously growing and the stock market grows at 9 percent per year, so maintenance in the most generic sense is 9 percent growth year over year; maintenance is a myth.
  anchor: >-
    If we aren't growing at 9 percent per year, we are falling behind.
  source: >-
    100m-offers.md, ch. 3 Pricing: The Commodity Problem, line 2178
  confirmations: 2
  anchor_at: "100m-offers.md:2178"
  tier: 1
  merged_from: [D-offers-054]
- id: B-offers-091
  type: rule
  name: >-
    Twenty to thirty percent in a growing marketplace
  statement: >-
    In a growing marketplace the business must grow 20-30 percent per year just to keep up.
  applies_when: >-
    You are in a growing marketplace.
  anchor: >-
    if you’re in a growing marketplace, then you might have to grow at 20-30 percent per year, just to keep up, or risk falling behind
  source: >-
    100m-offers.md, ch. 3 Pricing: The Commodity Problem, line 2180
  confirmations: 1
  anchor_at: "100m-offers.md:2180"
  tier: 1
- id: B-offers-092
  type: rule
  name: >-
    Lifetime value is counted on gross profit
  statement: >-
    Lifetime value is computed from gross profit over the customer's lifespan, not from total revenue.
  why: >-
    Definitions differ by source; the author focuses on gross profit and refers to it elsewhere as LTGP, Lifetime Gross Profit.
  anchor: >-
    The biggest difference is that some sources only count total revenue, while others focus on gross profit over the lifespan. I focus on gross profit.
  source: >-
    100m-offers.md, ch. 3 Pricing: The Commodity Problem, line 2216
  confirmations: 2
  anchor_at: "100m-offers.md:2216"
  tier: 1
  merged_from: [B-offers-093]
- id: B-offers-094
  type: rule
  name: >-
    Over-deliver on the first Grand Slam Offer
  statement: >-
    A first offer over-delivers to the point of being uneconomic, and operations are fixed later out of the resulting cash flow.
  why: >-
    You cannot tell whether what you have is good until demand is flowing; better to do more for every customer with cash coming in than to optimise a business with zero cash flow and no idea what to adjust.
  applies_when: >-
    Your first Grand Slam Offer, or a business owner who has not yet created flow.
  anchor: >-
    if this is your first Grand Slam Offer, it’s important to over-deliver like crazy
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, line 2381
  confirmations: 3
  anchor_at: "100m-offers.md:2381"
  tier: 1
  merged_from: [D-offers-057]
- id: B-offers-097
  type: rule
  name: >-
    List delivery vehicles divergently, including ones you would not do
  statement: >-
    When listing ways to solve each problem, every possibility is written down, including things you are not actually willing to do.
  why: >-
    The goal is to push your limits and jog your brain into a different version of the solution you would default to; life pays for divergent thinking, where multiple answers are right and one is far more right than the others.
  anchor: >-
    Think of all the things that might enhance the value of your offer.
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, line 2417
  confirmations: 4
  anchor_at: "100m-offers.md:2417"
  tier: 1
  merged_from: [A-offers-037, A-offers-038]
- id: B-offers-099
  type: rule
  name: >-
    Solve every perceived problem
  statement: >-
    The offer resolves every obstacle a buyer believes they will have, not just some of them.
  why: >-
    One single unsolved item is repeatedly the reason someone does not buy; refusing to be romantic about how you solve it, and solving it instead, is what makes the offer one people cannot say no to.
  anchor: >-
    You must resolve every obstacle a buyer believes they will have to convert the highest amount of people.
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, line 2485
  confirmations: 5
  anchor_at: "100m-offers.md:2485"
  tier: 1
  merged_from: [D-offers-059]
- id: B-offers-103
  type: rule
  name: >-
    Step back one level at a time
  statement: >-
    An unaffordable deliverable is replaced by the nearest lesser version you can live with, one step back at a time, or the price is raised until it becomes worth it.
  why: >-
    The question after imagining the maximum service is whether there is a lesser version of that experience you can deliver at scale.
  anchor: >-
    Just take one step back at a time until you arrive at something that has a time commitment or cost you are willing to live with
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, line 2504
  confirmations: 1
  anchor_at: "100m-offers.md:2504"
  tier: 1
- id: B-offers-108
  type: rule
  name: >-
    List the problems before and after the product too
  statement: >-
    The problem list covers what happens immediately before and immediately after someone uses the product or service, not only during it.
  why: >-
    Answering the next problem as it manifests makes the offer more valuable and compelling.
  anchor: >-
    When listing out problems, think about what happens immediately before and immediately after someone uses your product/service.
  source: >-
    100m-offers.md, ch. 9 Creating Your Grand Slam Offer Part I, line 2870
  confirmations: 3
  anchor_at: "100m-offers.md:2870"
  tier: 1
  merged_from: [B-offers-109]
```


## C. Разборы (кейсы) — 33

```yaml
- id: C-offers-001
  type: case
  name: >-
    The photography client: 5x ticket, 38x profit
  statement: >-
    A private photography company raised its average ticket from $300 to $1,500 over two years by finding what customers valued most, tripling down on it and eliminating everything else; time per customer went down, satisfaction went up, and weekly profit went from $1,000 to $38,000.
  demonstrates: >-
    That value, not cost, sets the price; and that a price increase works when the offer is rebuilt around what people value most rather than padded.
  why: >-
    Clients voted with their dollars that what the company provides now is far better than what it did before, so cracking value opened unlimited profit.
  anchor: >-
    The 5x increase in average ticket, 38x’d the profit of the business. It went from making $1,000/wk in profit to $38,000/wk in profit, and continues to grow.
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 19
  confirmations: 1
  anchor_at: "100m-offers.md:19"
  tier: 1
- id: C-offers-003
  type: case
  name: >-
    Logical vs psychological solutions, paired
  statement: >-
    Each problem is shown twice: make the elevator faster (logical) against floor-to-ceiling mirrors so people forget how long they rode (psychological); make it cheaper (logical) against make fewer of them and raise the price (psychological); make trains faster against the dotted map; and pay models to host the trip so people wish the ride were longer.
  demonstrates: >-
    Look for the psychological solution to a value problem, because the logical one has usually already been tried.
  why: >-
    If there were a logical solution it probably would have already been solved, thereby eliminating the problem; all that is left are the psychological problems.
  applies_when: >-
    A problem of value, waiting or price where the obvious fix has already been tried.
  anchor: >-
    *Psychological solution:* add floor to ceiling mirrors so people are distracted staring at themselves and forget how long they were on the elevator
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, lines 83–95
  confirmations: 2
  anchor_at: "100m-offers.md:91"
  tier: 1
  merged_from: [C-offers-002]
- id: C-offers-007
  type: case
  name: >-
    The gym's first $2,000 sale in seven days
  statement: >-
    Gym clients buy an extra $239,000 per year, which takes a while to arrive, so the delivery is built to produce an emotional win fast: ads live and their first $2,000 sale closed within the first seven days.
  demonstrates: >-
    Time delay as a value driver, split into the long-term outcome people buy and the short-term experience that makes them stay.
  why: >-
    By doing this their decision to work with us is reinforced, they immediately trust us more, and they become more likely to follow the rest of our systems and reach their ultimate destination.
  applies_when: >-
    Any service whose promised outcome takes months to arrive.
  anchor: >-
    So, once they have purchased, we need to create emotional wins fast. One way we do this is to get their ads live and get them to close their first $2,000 sale within their first seven days.
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 183
  confirmations: 2
  anchor_at: "100m-offers.md:183"
  tier: 1
  merged_from: [C-offers-008]
- id: C-offers-011
  type: case
  name: >-
    The plastic surgeons' ad copy read as the value equation
  statement: >-
    The marketing of plastic surgeons is read back as a deliberate hit on the effort-and-sacrifice column of the competing vehicle: tired of wasting countless hours in the gym, tired of trying diets that just don't work.
  demonstrates: >-
    Copy attacks the effort and sacrifice of the alternative vehicle rather than promising a bigger outcome.
  why: >-
    These are the exact pain points of the alternative; decreasing the effort and sacrifice, or at least the perceived effort and sacrifice, massively boosts the appeal of an offer.
  anchor: >-
    In fact, in looking at the marketing of plastic surgeons, these are the *exact* pain points they hit on when they say things like: *“Tired of wasting countless hours in the gym. . . . tired of trying* *diets that just don't work?”*
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 213
  confirmations: 1
  anchor_at: "100m-offers.md:213"
  tier: 1
- id: C-offers-014
  type: case
  name: >-
    The pain clinic's borrowed bonuses
  statement: >-
    A hypothetical pain clinic assembles bonuses from neighbouring businesses in exchange for exposure: free massages, two chiropractic adjustments ($100), a low-inflammation food discount ($50), brace and orthotic discounts ($150), a free PT session and pool month ($100), pharmacy discounts ($100/mo), repeated across many providers — so the bonuses alone outvalue the $400 offer, and the referral commissions negotiated on top ($100 from the chiro, $100 from orthotics, $50 from the health club, $100 from the pharmacy) add about $350 of pure profit per customer.
  demonstrates: >-
    Advanced bonuses from other people's products and services, and the negotiation of a group discount plus a commission on top.
  why: >-
    It is free marketing for them and high value products for you at no cost; the other businesses pay you and you do nothing but refer customers you have already paid to acquire.
  applies_when: >-
    Adjacent, non-competing businesses that solve the next need your customer will have.
  anchor: >-
    For example - if I owned a pain clinic, I might get a massage therapist to give me 1-2 free massages to incorporate into my offer.
  source: >-
    100m-offers.md, ch. 14 Bonuses, lines 351–389
  confirmations: 2
  anchor_at: "100m-offers.md:353"
  tier: 1
  merged_from: [C-offers-015]
- id: C-offers-016
  type: case
  name: >-
    The cohort kickoff line
  statement: >-
    Clients start in weekly cohorts, and the close is: sign up today and get into the group that kicks off Monday, otherwise wait for the next kickoff. The juiced version adds a client who dropped out a few weeks ago, so one opening exists for Monday's cohort, and points out that they will pay the same either way while starting later.
  demonstrates: >-
    Cohort-based rolling urgency, generated by the start cadence rather than by a fake deadline.
  why: >-
    Those two tweaks have pushed many sales over the edge by reminding a customer that they start Monday or wait a week; the less frequently you kick off, the more powerful it is.
  applies_when: >-
    A business that can start clients on a regular cadence, even in unlimited amounts.
  anchor: >-
    *“If you sign up today, I can get you in with our next group that kicks off on Monday, otherwise you’ll have to wait until our next kickoff date.”*
  source: >-
    100m-offers.md, ch. 13 Urgency, lines 435–447
  confirmations: 1
  anchor_at: "100m-offers.md:439"
  tier: 1
- id: C-offers-017
  type: case
  name: >-
    The same promotion rewrapped by season
  statement: >-
    One unchanged promotion is run month after month under dated seasonal names: New Year Promotion ends Jan 30, Valentines Lovers Promo Ends Feb 30, Sexy By Spring Special Ends March 31, Fools in Love April Promo Ends April 30, with the dates visible on the landing page and in the copy.
  demonstrates: >-
    Rolling seasonal urgency, a real start and finish created without changing the offer.
  why: >-
    Naming it something different by season gives you a real differentiator with a start and a finish; deadlines drive decisions, and you can fire up a new campaign and landing page with new dates in five minutes.
  applies_when: >-
    Especially local businesses, which must vary their marketing more often than national advertisers.
  anchor: >-
    *Next Month:* Our Sexy By Spring Special Ends March 31!
  source: >-
    100m-offers.md, ch. 13 Urgency, lines 457–471
  confirmations: 1
  anchor_at: "100m-offers.md:465"
  tier: 1
- id: C-offers-018
  type: case
  name: >-
    Urgency on the promotion, not on the service
  statement: >-
    For a business that sells year round, the close puts the deadline on the promotion rather than on the service: start today to take advantage of the discount you came in for, because the promotions change every four weeks or so and this is one of the better ones.
  demonstrates: >-
    Pricing or bonus-based urgency, which keeps integrity because the service itself is never withheld.
  why: >-
    It would be a lie to say a roofer will not serve them after the date, but talking about the promotion elicits the same urgency to buy while maintaining your integrity.
  applies_when: >-
    Businesses that sell clients all year and cannot use cohorts or seasons.
  anchor: >-
    *“Yes, let’s get you started today so you* *can take advantage of the discount you came in for. I’m not sure how long we will be running it as we change them every 4 weeks or so, and this is one of the better ones we have run in a while.”*
  source: >-
    100m-offers.md, ch. 13 Urgency, lines 473–477
  confirmations: 1
  anchor_at: "100m-offers.md:475"
  tier: 1
- id: C-offers-020
  type: case
  name: >-
    The limited release that must sell out
  statement: >-
    A physical product runs limited releases by flavour, colour, design or size — this month, 100 boxes of mint chocolate cookie protein bars — sized so it always sells out, repeated about once a month, and followed by an announcement that it sold out.
  demonstrates: >-
    Limited supply of units as scarcity, and the announcement of the sell-out as social proof.
  why: >-
    It is better to sell out consistently than to over order and fail at creating that scarcity; telling everyone you sold out gives social proof that other people thought it was worth it, and the choice having been made for them, they desire it more.
  applies_when: >-
    Physical products; the method stacks in effectiveness when repeated over time, but not too often.
  anchor: >-
    “This month, we are releasing 100 boxes of mint chocolate cookie flavored protein bars.” Important point: to properly utilize this method you should *always* sell out.
  source: >-
    100m-offers.md, ch. 12 Scarcity, lines 561–567
  confirmations: 2
  anchor_at: "100m-offers.md:563"
  tier: 1
  merged_from: [C-offers-021]
- id: C-offers-022
  type: case
  name: >-
    Three service caps, in the words used on the call
  statement: >-
    Scarcity for services is worded three ways: a total business cap — my agency will only service twenty-five customers total, period; a growth rate cap — we only accept 5 new clients per week, the first 3 spots are taken and I have 6 more calls this week; and a cohort cap — we take on 100 clients 4 times a year, we open the doors then close them.
  demonstrates: >-
    The three ways to put a fixed supply on a service without lying about it.
  why: >-
    You can only handle a certain number of new clients anyway, so you might as well let prospects know; the waiting list makes price resistance disappear the moment the door opens.
  applies_when: >-
    Services, where scarcity is trickier than for products; pick the cap that fits the business model.
  anchor: >-
    “We onlyaccept 5 new clients per week and we already have the first 3 spots taken. I have 6 more calls this week, so you can take the spot or one of my next calls and you can wait until we reopen.”
  source: >-
    100m-offers.md, ch. 12 Scarcity, lines 573–581
  confirmations: 1
  anchor_at: "100m-offers.md:579"
  tier: 1
- id: C-offers-023
  type: case
  name: >-
    Scarcity on a free lead magnet
  statement: >-
    A free checklist is offered two ways: available to download now, which a reader might get to eventually; or a page that only allows twenty new people to download it each week, which makes the reader go and check, join a notification list when it has run out, and click the link the moment the next twenty open.
  demonstrates: >-
    Controlling supply turns a neat free download into a desirable thing not everyone has access to.
  why: >-
    By employing scarcity we make what would otherwise be a neat free download into a desirable thing, and the person is far more likely to consume it once they get it.
  applies_when: >-
    Free offers and lead magnets, where there is no price to create desire.
  anchor: >-
    *But*, if I told you I have it set so that every week the page only allows *twenty* newpeople to download it, you’d be far *more likely* to go see if you can grab it.
  source: >-
    100m-offers.md, ch. 12 Scarcity, lines 587–591
  confirmations: 1
  anchor_at: "100m-offers.md:589"
  tier: 1
- id: C-offers-024
  type: case
  name: >-
    The guarantee arithmetic
  statement: >-
    The worked comparison: 100 sales with 5 refunds (5%) leaves 95 net sales; with the guarantee, 130 sales with 13 refunds (10%) leaves 117 net sales; 117/95 = 1.23x, a 23 percent increase that all goes to the bottom line.
  demonstrates: >-
    Deciding on a guarantee by arithmetic rather than by fear of abuse.
  why: >-
    For a guarantee not to be worth it, the absolute increase in sales would have to be fully offset by an absolute increase in refunds, which would usually mean a doubling of the refund rate — unlikely.
  anchor: >-
    If you close 130 percent as many people, and your refund percentage *doubles* from 5 percent to 10 percent, you’ve still made 1.23x the money, or 23 percent more, and that all goes to the bottom line.
  source: >-
    100m-offers.md, ch. 15 Guarantees, lines 642–650
  confirmations: 1
  anchor_at: "100m-offers.md:642"
  tier: 1
- id: C-offers-026
  type: case
  name: >-
    Jason Fladlien's fully informed decision pitch
  statement: >-
    An unconditional guarantee is pitched as a request not to decide yes or no today but to make a fully informed decision, which can only be made from the inside — like not buying a house without looking inside it; whether it is 29 minutes or 29 days later, any reason at all, one email to support gets the money back, with support response times quoted at 61 minutes on average.
  demonstrates: >-
    How an unconditional, no-questions-asked refund guarantee is worded so it reframes the buying decision instead of merely promising a refund.
  why: >-
    You can only make such a guarantee when you are confident that what you have is the real deal; the author notes these are 100% Fladlien's words and takes no credit.
  authors_caveat: >-
    Attributed verbatim to Jason Fladlien; unconditional guarantees get a lot more people to buy but will produce refunds, and work better in lower-ticket situations.
  anchor: >-
    “I’m not asking you to decide yes or no today...I'm asking you to make a fully informed decision, that is all. The only way you can make a fully informed decision is on the inside, not the outside.
  source: >-
    100m-offers.md, ch. 15 Guarantees, lines 710–712
  confirmations: 1
  anchor_at: "100m-offers.md:712"
  tier: 1
- id: C-offers-028
  type: case
  name: >-
    The weight-loss satisfaction guarantee, as said on the call
  statement: >-
    The satisfaction guarantee is sold by answering the doubt it creates — would I still be in business giving a crazy guarantee if I were not good at this — then narrowing what is guaranteed: not the six-week goal, since I cannot eat the food for you, but $500 worth of value and service, and a check the day you tell me we suck.
  demonstrates: >-
    An unconditional satisfaction guarantee whose promise is moved from the outcome to the level of service, so it can be made honestly.
  why: >-
    The strength of the guarantee closed a lot of deals; satisfaction / no questions asked is the highest form of guarantee, but you have to be good at fulfilling your promises.
  authors_caveat: >-
    Works much better in lower-ticket situations and becomes very risky in higher-ticket services with higher costs of fulfilment.
  anchor: >-
    “Do you think I'd still be in business if I gave a crazy guarantee like that and wasn't good at what I did? Now I'm *not* guaranteeing you’re going to hit this goal in six weeks, after all, because I can't eat the food for you. But I am guaranteeing that you will get $500 worth of value and service from us to support you.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 728
  confirmations: 2
  anchor_at: "100m-offers.md:728"
  tier: 1
  merged_from: [C-offers-029]
- id: C-offers-030
  type: case
  name: >-
    I will buy your store for $25,000
  statement: >-
    On a $2997 ecommerce course, the guarantee was: buy this course, spend $X on advertising your store using the methods here, and if you do not make money I will buy your store from you for $25,000, no questions asked. It is claimed to have produced an extra $3M in sales, with only ten $25,000 refunds paid out, so the refunds generated $2.75M in extra sales.
  demonstrates: >-
    The outsized refund guarantee with a consumption condition — used when margins are high and the prospect must do a lot for the result to be near-certain.
  why: >-
    A guarantee like this serves its purpose when you need a lot of things done by the prospect and, assuming they are done, there is a low chance of the result not being achieved; it typically outperforms a 30-day money back guarantee on net conversions.
  authors_caveat: >-
    Attributed to Jason Fladlien; for products with high margins only.
  anchor: >-
    He said “if you buy this course and spend $X on advertising your ecommerce store using the methods herein, and don't make money, I will buy your store from you for $25,000 no questions asked.” He claimed that an additional $3M in sales came from this crazy guarantee on a $2997 course.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 742
  confirmations: 1
  anchor_at: "100m-offers.md:742"
  tier: 1
- id: C-offers-033
  type: case
  name: >-
    The anti-guarantee that filters the buyer
  statement: >-
    For high ticket work that needs customization, the anti-guarantee is turned into a filter: if you are the type of customer who needs a guarantee before taking a jump, you are not the type of person we want to work with; we want motivated self-starters, and if you are not serious, do not buy it.
  demonstrates: >-
    Anti-guarantees used as qualification on high-ticket, high-effort offers.
  why: >-
    A person who only buys because of a guarantee may not be willing to put in the work needed to succeed, so a stance that repels them protects fulfilment.
  applies_when: >-
    High ticket products and services that require a lot of work or customization.
  anchor: >-
    “If you're the type of customer who needs a guarantee before taking a jump, then you are not the type of person we want to work with. We want motivated self-starters who can follow instructions and are not looking for a way out before they even begin.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 819
  confirmations: 1
  anchor_at: "100m-offers.md:819"
  tier: 1
- id: C-offers-034
  type: case
  name: >-
    The four questions his father asked
  statement: >-
    A sceptic who thinks $42,000 a year cannot be legitimate is walked through four questions and converts on his own: if I made you $239,000 extra this year, would you pay me $42,000 (yes, if I knew I would make it back) — but what would I have to do (about 15 hours a week) — how long would it take (eleven months) — how much up front (nothing, pay me as you start making the money). He says: well then, yeah, I would do it.
  demonstrates: >-
    The four value drivers as four questions — dream outcome, perceived likelihood, time delay, effort and sacrifice — answered in the prospect's own terms.
  why: >-
    The questions his father asked corresponded exactly with the four pillars of the value equation, and answering them is what made the price make sense; the $239,000 was the real average increase in topline revenue of a gym on the systems for 11 months.
  anchor: >-
    “If I made you $239,000 extra this year, would you pay me $42,000?” I asked, using “$239,000” because it was the average increase in topline revenue of a gym using our systems for 11 months.
  source: >-
    100m-offers.md, ch. 5 Pricing: Charge What It’s Worth, lines 1089–1105
  confirmations: 2
  anchor_at: "100m-offers.md:1089"
  tier: 1
- id: C-offers-036
  type: case
  name: >-
    Done-for-you turned into done-with-you
  statement: >-
    The original model was 21 days on site per gym, paying his own hotels, car, food and ad spend, generating and working the leads and selling for them, keeping 100% of the cash collected, with the gym risking only a refundable $500 deposit. One gym he did not want to fly to was told he would show him how but the owner would do all the work; that gym collected almost $44,000 in 30 days, four times its previous month, and the model moved to done-with-you at about a third of the price while serving hundreds of gyms a month instead of eight.
  demonstrates: >-
    The sales-to-fulfilment continuum — over-deliver first to create flow, then convert the same promise into a version that scales, changing the how and not the promise.
  why: >-
    Create flow, monetize flow, then add friction: once he saw the process could be duplicated from afar the travel constraint disappeared, and the promise stayed the same (I will fill your gym in 30 days) while only the how and what changed.
  anchor: >-
    Within thirty days, this gym had made almost $44,000 in new up front cash collected sales (4x their previous month).
  source: >-
    100m-offers.md, ch. 5 Pricing: Charge What It’s Worth, lines 1220–1228; ch. 10 Part II: Trim & Stack, lines 2395–2405
  confirmations: 2
  anchor_at: "100m-offers.md:1228"
  tier: 1
- id: C-offers-037
  type: case
  name: >-
    Pricing Gym Launch above every competitor
  statement: >-
    Entering a market where low-price competitors charged $500 per month and the single premium player charged $5,000, the offer was priced at $16,000 for a 16-week done-with-you intensive — three times the highest player and 32 times the lowest — then 35 percent were upsold into a three-year $42,000/year agreement, against an average gym owner take-home of $35,280/year.
  demonstrates: >-
    Deliberate premium pricing to create allure and a category of one, backed by conviction from documented results.
  why: >-
    The goal is not to be slightly above market but so much higher that the consumer thinks there must be something entirely different going on here; it was possible because conviction, built by outworking self-doubt and by survey data on results, was stronger than their skepticism.
  anchor: >-
    A price of $16,000 for a 16-week, done-with-you intensive. Then we upsold 35 percent of those people into a three-year, $42,000/year agreement for us to help them grow their gyms.
  source: >-
    100m-offers.md, ch. 5 Pricing: Charge What It’s Worth, lines 1230–1246
  confirmations: 1
  anchor_at: "100m-offers.md:1232"
  tier: 1
- id: C-offers-039
  type: case
  name: >-
    Ten units at $500 against two at $5000
  statement: >-
    The same two-day workshop is sold two ways: scenario one, 10 units at $500 each, selling the entire pyramid; scenario two, two one-day 1-on-1 workshops at $5000 each, skimming the top with 80 percent not purchasing. Scenario two makes more money at lower cost and leaves eight people with unsatisfied desire, so the next promotion opens three spots at the same price and sells them all; scenario one sells fewer slots next time because all desire was satisfied.
  demonstrates: >-
    The Delicate Dance of Desire and the fractal (80/20) shape of demand — one fifth of prospects will pay five times the price.
  why: >-
    Desire comes from not getting what you want, so satisfying all the demand kills the golden goose; keeping supply under the demand you can generate maximizes profit and keeps desire ravenous.
  anchor: >-
    *Scenario two:* We sell two one-day workshops 1-on-1 for $5000 each. (skim top of pyramid, with 80 percent not purchasing)
  source: >-
    100m-offers.md, ch. 11 Enhancing The Offer, lines 1532–1551
  confirmations: 2
  anchor_at: "100m-offers.md:1535"
  tier: 1
  merged_from: [C-offers-038]
- id: C-offers-041
  type: case
  name: >-
    Lloyd: everything was right except the market
  statement: >-
    A software business for newspapers is diagnosed by elimination — the product was great, the offer was a zero-risk revshare, the founder was a natural salesman — leaving the market, which was shrinking 25 percent a year. After Covid he applied the same skills to automated mask manufacturing, a business he had zero experience in, and was doing millions per month within five months.
  demonstrates: >-
    How to diagnose a failing business in the order market, offer, persuasion; and the Growing criterion among the four market indicators.
  why: >-
    Same entrepreneur, different market: he had looked at all the angles except the most obvious one, and no matter how hard he tried the entire marketplace was fighting against him.
  anchor: >-
    It wasn’t his product — that was great. It wasn’t his offer — he had a zero risk revshare model. It wasn’t his sales skills — he was a natural salesman.
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market -- A Starving Crowd, lines 1605–1611
  confirmations: 2
  anchor_at: "100m-offers.md:1609"
  tier: 1
- id: C-offers-043
  type: case
  name: >-
    Choosing the relationship avatar by the four indicators
  statement: >-
    Inside the relationships market, second-half-of-life coaching for old timers is chosen over college students, scored on the four indicators: seniors alone near the end of life suffer more pain, have more buying power, are easy to find, and at the time of writing more people turn 65 each year than turn 20.
  demonstrates: >-
    The four market indicators — massive pain, purchasing power, easy to target, growing — applied to pick a subgroup inside health, wealth or relationships.
  why: >-
    The goal is to find a smaller subgroup within one of the three big buckets that is growing, has the buying power and is easy to target.
  anchor: >-
    So if I were a relationship expert trying to find my avatar, I’d rather focus on “second half of life relationship” coaching for old timers than helping college students in relationships.
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market -- A Starving Crowd, lines 1663–1671
  confirmations: 1
  anchor_at: "100m-offers.md:1669"
  tier: 1
- id: C-offers-045
  type: case
  name: >-
    The time management course, niched down four times
  statement: >-
    The same course is renamed down a ladder of specificity and repriced at each rung: a generic Time Management course at $19; Time Management For Sales Professionals at $99; Time Management for B2B Outbound Sales Reps at $499, justified because one sale nets that rep $500; Time Management for B2B Outbound Power Tools & Gardening Sales Reps at $1000 to $2000, because the reader thinks this is made exactly for me.
  demonstrates: >-
    Riches are in the niches — you can charge 100x more for the exact same product when it is applied to a specific avatar.
  why: >-
    The pieces of the program may be identical to the generic course, but since they have been applied and the sales messaging speaks to this avatar, buyers find it more compelling and get more value from it in a real way.
  authors_caveat: >-
    Taught to the author by Dan Kennedy; for most businesses under $10M a year, with broadening advised only beyond that depending on the total addressable market.
  anchor: >-
    Let’s just niche down one last level…. “Time Management for B2B Outbound Power Tools & Gardening Sales Reps.” Boom.
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market -- A Starving Crowd, lines 1721–1741
  confirmations: 2
  anchor_at: "100m-offers.md:1737"
  tier: 1
  merged_from: [C-offers-046]
- id: C-offers-049
  type: case
  name: >-
    Changing the wrapper when an offer fatigues
  statement: >-
    Worked wrapper changes, made in order from lightest to heaviest: Free 6 Week Lean Challenge becomes Free 6 Week Tone Challenge; Holiday Hangover becomes New Year New You; a Six-Week Stress Release Challenge becomes a 42-Day Relaxing Holidays Challenge for a massage center — then the duration changes, then the free or discount enhancer, and only last the monetization structure.
  demonstrates: >-
    The order of variation when offers fatigue: creative, body copy, headline/wrapper, duration, enhancer, money model.
  why: >-
    The lower on the list you go the more operationally heavy it is, so exhaust the lighter ways first; once an offer is monetized it should rarely be changed, because change creates inefficiency and operational drag.
  applies_when: >-
    When ads or offers fatigue — fastest in local markets, where a small radius burns offers quickly.
  anchor: >-
    Let’s say we change from a Six-Week Stress Release Challenge to a 42-Day Relaxing Holidays Challenge for a massage center. Same core offer, just a different wrapper.
  source: >-
    100m-offers.md, ch. 16 Naming, lines 2089–2110
  confirmations: 1
  anchor_at: "100m-offers.md:2106"
  tier: 1
- id: C-offers-050
  type: case
  name: >-
    The agency offer rewritten
  statement: >-
    Before: $1,000 down, then a $1,000/mo retainer for agency services — the same offer as everyone else, you pay us to work, maybe you get results. After: pay one time, no recurring fee, no retainer, just cover ad spend; I generate and work your leads; you only pay me if people show up; I guarantee 20 people in your first month or the next month is free; plus daily sales coaching, tested scripts, tested price points and offers, and sales recordings.
  demonstrates: >-
    Turning a commoditized, price-driven offer into a differentiated, value-driven Grand Slam Offer that cannot be compared.
  why: >-
    Commoditized marketing all looks the same because everyone is making the same offer; an incomparable offer forces the prospect to stop and assess value, which re-calibrates their value-meter and removes the price comparison.
  anchor: >-
    And only pay me if people show up. And I’ll guarantee you get 20 people in your first month, or you get your next month free.
  source: >-
    100m-offers.md, ch. 3 Pricing: The Commodity Problem, lines 2264–2303
  confirmations: 1
  anchor_at: "100m-offers.md:2294"
  tier: 1
- id: C-offers-051
  type: case
  name: >-
    22.4x, factor by factor
  statement: >-
    The same ad spend is followed through the funnel: 2.5x more people respond because the offer is more compelling, 2.5x more of them close, and the up-front price is 4x higher — 2.5 x 2.5 x 4 = 22.4x more cash collected up front, $10,000 spent to make $112,000, against the old model that lost half the ad spend up front and broke even only after 30 days.
  demonstrates: >-
    A Grand Slam Offer moves all three growth levers at once (response, conversion, price), which multiplies rather than adds.
  why: >-
    Your cost to acquire a customer becomes so cheap relative to what you make that cash flow and acquiring customers stop being the bottleneck; the limiting factor becomes your ability to do the work.
  anchor: >-
    The end result is 2.5 x 2.5 x 4 = 22.4x more cash collected up front. Yes, you spent $10,000 to make $112,000. You just *made money* getting new customers.
  source: >-
    100m-offers.md, ch. 3 Pricing: The Commodity Problem, lines 2305–2313
  confirmations: 1
  anchor_at: "100m-offers.md:2309"
  tier: 1
- id: C-offers-052
  type: case
  name: >-
    One problem, sixteen delivery vehicles
  statement: >-
    For the single problem buying healthy food is hard, the solutions are listed by how many people are served at once: one-on-one (in-person grocery shopping, personalized list, full-service shopping, orientation, text support, a phone call during the shop), small group (group shopping trip, group list workshop, buying and delivering food, offsite orientation), one to many (live-streamed grocery tour, recorded tour, DIY grocery calculator, a list per plan per week, a grocery buddy system, pre-made insta-cart carts).
  demonstrates: >-
    Step #4, Create Your Solutions Delivery Vehicles, with the delivery cheat codes — level of personal attention, DIY/DWY/DFY, live medium, recording format, response speed, and the 10x to 1/10th test.
  why: >-
    Listing anything you could possibly do pushes past the default solution and jogs the brain into a different version of it; solutions for one problem give ideas for others you would not have considered.
  applies_when: >-
    Once per product, for every perceived problem the client meets before, during and after the service.
  anchor: >-
    1. Live grocery tour virtual, where I might live stream me going through the grocery store for all my new customers and let them ask questions live
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, lines 2429–2471
  confirmations: 1
  anchor_at: "100m-offers.md:2449"
  tier: 1
- id: C-offers-053
  type: case
  name: >-
    The eating out guide
  statement: >-
    A sales presentation was about to be lost because the prospect ate lunch out every day and the program insisted on home-cooked food; instead of holding the line he offered to make her an eating out guide for restaurants, asked how does that sound, and closed the sale — then had the guide for every prospect afterwards and kept building templates until no single objection was left.
  demonstrates: >-
    Solve every perceived problem: one unsolved obstacle is enough to lose the sale, and the solution becomes a permanent asset.
  why: >-
    Do not get romantic about how you want to solve the problem; you must resolve every obstacle a buyer believes they will have to convert the highest number of people.
  anchor: >-
    Refusing to lose the sale because of this *one thing*, I conceded “I’ll make you an eating out guide for when you go to restaurants so you can eat our 100 percent of the time and still hit your goal. How does that sound?” She agreed, and I closed the sale.
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, lines 2477–2485
  confirmations: 1
  anchor_at: "100m-offers.md:2481"
  tier: 1
- id: C-offers-054
  type: case
  name: >-
    Stepping back from moving in with the client
  statement: >-
    The highest-value delivery imaginable — moving in and doing the client's shopping, exercising and cooking — would make them certain of the result but is not worth any price short of a gazillion dollars; the move is then to ask whether a lesser version of that experience can be delivered at scale, stepping back one notch at a time until the cost is acceptable, or to raise the price until it is.
  demonstrates: >-
    Step #5a, Trim — keeping only low cost, high value and high cost, high value items, judged through the four questions of the value equation.
  why: >-
    Take one step back at a time until you arrive at something with a time commitment or cost you are willing to live with; high cost items are saved for big value adds only, and a lower cost alternative of equal value is always preferred.
  anchor: >-
    **Example:** Let’s say I moved in with someone and did their shopping, exercising, andcooking for them. They would probably believe they would definitely lose weight. But I am not willing to do that for any amount of money short of a gazillion dollars.
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, lines 2489–2510
  confirmations: 1
  anchor_at: "100m-offers.md:2500"
  tier: 1
- id: C-offers-055
  type: case
  name: >-
    100 hours once, 15 minutes each time after
  statement: >-
    An excel application built before his first gym took goals as input and generated over 100 meals matched to the client's macronutrients and calories, the exact grocery amounts to buy and bulk preparation instructions; it took about 100 hours to build and then produced a truly personalized, expensively priced eating plan in about 15 minutes.
  demonstrates: >-
    High value, one to many solutions — a high one-time cost of creation and near-zero additional effort afterwards.
  why: >-
    These are the delivery vehicles with the biggest discrepancy between cost and value, which is exactly why software becomes so valuable; the meal plans made this way were later used by 4,000+ gyms.
  applies_when: >-
    When choosing which delivery vehicles to keep after trimming.
  anchor: >-
    It took me about 100 hours to put the whole thing together. But from that point going forward I sold truly personalized eating plans for very expensive prices, but they only took me about 15minutes to make.
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, lines 2506–2518
  confirmations: 1
  anchor_at: "100m-offers.md:2506"
  tier: 1
- id: C-offers-056
  type: case
  name: >-
    The finished weight-loss stack: $4,351 of value for $599
  statement: >-
    Each problem is presented as problem, solution wording, then a named bundle with a price tag and the delivery items underneath: Foolproof Bargain Grocery System ($1,000), Ready in 5min Busy Parent Cooking Guide ($600), Personalized Lick Your Fingers Good Meal Plan ($500), Fat Burning Workouts ($699), The Ultimate Tone Up While You Travel Blueprint ($199), The Never Fall Off Accountability System ($1,000), The Live It Up While Slimming Down Eating Out System ($349) — total value $4,351, all for only $599.
  demonstrates: >-
    Step #5b, Stack — assembling trimmed solutions into one high value deliverable, each named and priced, so the bundle solves all perceived problems and cannot be compared to a gym membership.
  why: >-
    The bundle solves all the perceived problems, not just some; gives you conviction that what you sell is one of a kind; and makes it impossible to compare your offering with the one down the street.
  anchor: >-
    Total value: $4,351 (!) All for only $599
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, lines 2538–2598
  confirmations: 1
  anchor_at: "100m-offers.md:2588"
  tier: 1
- id: C-offers-059
  type: case
  name: >-
    The weight-loss problem list
  statement: >-
    The problems are listed in the sequence the customer meets them — buying healthy food, cooking it, eating it, exercising regularly — and under each, four objections that map onto the four value drivers: it will not be financially worth it (dream outcome); it will not work for me, I will not stick with it, outside factors will get in the way (likelihood); it is hard, confusing, I will suck at it (effort and sacrifice); it takes too much time, I am too busy, it will take too long to work (time). The example yields 16 core problems with two to four sub-problems each, 32 to 64 in total.
  demonstrates: >-
    Step #2, List Problems — in insane detail, in customer sequence, using the four value drivers as prompts.
  why: >-
    The more problems you think of, the more problems you get to solve; thinking about what happens immediately before and immediately after someone uses your service surfaces the next thing they need help with.
  anchor: >-
    4. I will not be able to cook healthy food forever. My family’s needs will get in my way. If I travel I won’t know what to get.
  source: >-
    100m-offers.md, ch. 9 Creating Your Grand Slam Offer Part I, lines 2868–2911
  confirmations: 1
  anchor_at: "100m-offers.md:2881"
  tier: 1
- id: C-offers-060
  type: case
  name: >-
    Problems reversed into solutions, one line each
  statement: >-
    Every listed problem is flipped into solution-oriented language by adding how to and reversing the complaint: hard, confusing, I will suck at it becomes how to make buying healthy food easy and enjoyable so anyone can do it; takes too much time becomes how to buy healthy food quickly; is expensive becomes how to buy healthy food for less than your current grocery bill; is undoable if I travel becomes how to get healthy food when traveling.
  demonstrates: >-
    Step #3, Solutions List — transform each problem into a solution, then name it; repetition across problems is expected because they all trace back to the four value drivers.
  why: >-
    This gives a checklist of exactly what has to be done for the prospect and solved for them; if only one of these needs is missing in a solution it can cause someone not to buy.
  anchor: >-
    *. . . is hard, confusing, I won’t like it. I will suck at it→* How to make buying healthy food easy and enjoyable, so that anyone can do it (especially busy moms!)
  source: >-
    100m-offers.md, ch. 9 Creating Your Grand Slam Offer Part I, lines 2915–2965
  confirmations: 1
  anchor_at: "100m-offers.md:2927"
  tier: 1
```


## D. Антипаттерны и границы — 9

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
  tier: 1
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
  tier: 1
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
  confirmations: 2
  anchor_at: "100m-offers.md:736"
  tier: 1
  merged_from: [B-offers-050]
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
  tier: 1
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
  confirmations: 5
  anchor_at: "100m-offers.md:1621"
  tier: 1
  merged_from: [A-offers-022, B-offers-067]
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
  confirmations: 3
  anchor_at: "100m-offers.md:1697"
  tier: 1
  merged_from: [B-offers-075]
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
  confirmations: 2
  anchor_at: "100m-offers.md:1709"
  tier: 1
  merged_from: [B-offers-076]
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
  confirmations: 2
  anchor_at: "100m-offers.md:2021"
  tier: 1
  merged_from: [B-offers-085]
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
  tier: 1
```


## E. Глоссарий — 26

```yaml
- id: E-offers-001
  type: term
  name: >-
    The Value Equation
  statement: >-
    The Value Equation is the author's own formula that quantifies the four drivers of an offer's value: dream outcome and perceived likelihood of achievement on top (increase them), perceived time delay and perceived effort and sacrifice on the bottom (decrease them).
  definition: >-
    A repeatable formula that I have created to help quantify the variables that create value for any offer; there are four primary drivers of value, two of which you seek to increase and two you seek to decrease.
  why: >-
    It is written as a division rather than an addition so that driving the bottom side towards zero makes the offer infinitely valuable.
  anchor: >-
    to help quantify the variables that create value for any offer. I call it *The Value Equation*.
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 21
  confirmations: 3
  anchor_at: "100m-offers.md:21"
  tier: 1
  merged_from: [E-offers-005]
- id: E-offers-002
  type: term
  name: >-
    Dream Outcome
  statement: >-
    The dream outcome is the feelings and experiences the prospect already pictures for themselves, the gap between their current reality and their dreams, which the offer channels rather than creates.
  definition: >-
    The dream outcome is the expression of the feelings and experiences the prospect has envisioned in their mind. It's the gap between their current reality and their dreams.
  why: >-
    The goal is not to create desire but to channel existing desire through the offer, so the dream has to be depicted back accurately enough that the prospect feels understood.
  not_to_confuse_with: >-
    The vehicle that delivers it: multiple vehicles can satisfy the same dream outcome, and when two offers serve the same desire the dream outcome cancels out and the other three value drivers decide the price.
  anchor: >-
    The dream outcome is the expression of the feelings and experiences the prospect has envisioned in their mind.
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 109
  confirmations: 2
  anchor_at: "100m-offers.md:109"
  tier: 1
- id: E-offers-004
  type: term
  name: >-
    Perceived Likelihood of Achievement
  statement: >-
    Perceived likelihood of achievement is the prospect's own answer to how likely they believe it is that they will get the result if they buy, and people pay for that certainty.
  definition: >-
    people pay for certainty. They value certainty. I call this the perceived likelihood of achievement. In other words, How likely do I believe it is that I will achieve the result I am looking for if I make this purchase?
  why: >-
    Raising the prospect's conviction that the offer will actually work for them makes the offer more valuable even though the work on the seller's end stays identical, as with the plastic surgeon's 10,000th patient versus their first.
  anchor: >-
    Then I realized people pay for certainty. They value certainty. I call this “the perceived likelihood of achievement.”
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 163
  confirmations: 3
  anchor_at: "100m-offers.md:163"
  tier: 1
  merged_from: [C-offers-006]
- id: E-offers-006
  type: term
  name: >-
    Long-term outcome and short-term experience
  statement: >-
    Inside the time-delay driver the author separates the long-term outcome, the thing people buy, from the short-term experience, the milestones along the way that make them stay long enough to get it.
  definition: >-
    There are two elements to this driver of value: Long-term outcome and short-term experience. The thing people buy is the long-term value, aka their dream outcome. But the thing that makes them stay long enough to get it is the short-term experience.
  why: >-
    An early emotional win reinforces the buying decision and gives the momentum to see it through; people who experience a victory early on are more likely to continue than those who do not.
  anchor: >-
    There are two elements to this driver of value: Long-term outcome and short-term experience.
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 179
  confirmations: 2
  anchor_at: "100m-offers.md:179"
  tier: 1
- id: E-offers-007
  type: term
  name: >-
    Effort & Sacrifice
  statement: >-
    Effort and sacrifice is what the offer costs the buyer in ancillary costs accrued along the way, both tangible and intangible, and the goal is to decrease it.
  definition: >-
    This is what it costs people in ancillary costs, aka other costs accrued along the way. These can be both tangible and intangible.
  why: >-
    Decreasing the effort and sacrifice, or at least the perceived effort and sacrifice, can massively boost the appeal of the offer; this is why done-for-you services cost more than do-it-yourself.
  anchor: >-
    This is what it “costs” people in ancillary costs, aka “other costs accrued along the way.” These can be both tangible and intangible.
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 205
  confirmations: 2
  anchor_at: "100m-offers.md:205"
  tier: 1
- id: E-offers-008
  type: term
  name: >-
    Wow Factor (what makes something a bonus rather than part of the core offer)
  statement: >-
    A deliverable becomes a bonus when it has Wow Factor, something the buyer should not be allowed to miss, distinct enough to stand on its own and be pulled out of the pile.
  definition: >-
    Short answer: Wow Factor - in other words - something you wouldn't want someone to miss.
  why: >-
    When so much stuff is provided that valuable nuggets get lost in the mix, the most distinct pieces are pulled out and highlighted; something short but high in value can seem unjustified as a paid product yet be perceived as very valuable as a bonus.
  not_to_confuse_with: >-
    The rest of the core offer, which is fulfilled anyway and stays inside the price.
  anchor: >-
    Short answer: Wow Factor - in other words - something you wouldn’t want someone to miss.
  source: >-
    100m-offers.md, ch. 14 Bonuses, line 409
  confirmations: 1
  anchor_at: "100m-offers.md:409"
  tier: 1
- id: E-offers-009
  type: term
  name: >-
    Urgency
  statement: >-
    Urgency is a function of time: limiting when people can sign up by putting a defined deadline or cut-off on the purchase.
  definition: >-
    Urgency is a function of time. This is where you only limit when people can sign up, rather than how many. Having a defined deadline or cut off for a purchase or action to occur creates urgency.
  why: >-
    Urgency increases demand by decreasing the action threshold of a prospect; deadlines drive decisions.
  not_to_confuse_with: >-
    Scarcity, which is a function of quantity (how many), while urgency is a function of time (when); they are frequently used together but are separate levers.
  anchor: >-
    This is where you *only* limit *when* people can sign up, rather than *how many*. Having a defined deadline or cut off for a purchase or action to occur creates urgency.
  source: >-
    100m-offers.md, ch. 13 Urgency, line 431
  confirmations: 2
  anchor_at: "100m-offers.md:431"
  tier: 1
- id: E-offers-010
  type: term
  name: >-
    Scarcity
  statement: >-
    Scarcity is a function of quantity: a fixed supply of products, seats or client slots that is publicly stated, which creates fear of missing out.
  definition: >-
    When there's a fixed supply or quantity of products or services that are available for purchase it creates scarcity or a fear of missing out. It pulls on our psychological fear of loss to get us to take action.
  why: >-
    Humans are far more motivated to hoard a scarce resource than to act on something that could help them: fear of loss is stronger than desire for gain. Scarcity also implies social proof.
  not_to_confuse_with: >-
    Urgency, which limits when people can buy; scarcity limits how many can buy.
  anchor: >-
    When there’s a fixed supply or quantity of products or services that are available for purchase it creates “scarcity” or a “fear of missing out.”
  source: >-
    100m-offers.md, ch. 12 Scarcity, line 547
  confirmations: 3
  anchor_at: "100m-offers.md:547"
  tier: 1
- id: E-offers-011
  type: term
  name: >-
    Guarantee (the conditional statement)
  statement: >-
    A guarantee in this method is a conditional statement of the form: if you do not get X result in Y time period, we will Z.
  definition: >-
    What makes a guarantee have power is a conditional statement: If you do not get X result in Y time period, we will Z.
  why: >-
    Without the or what portion, the guarantee sounds weak and diluted; deciding what you will do if they do not get the result is what gives it teeth.
  not_to_confuse_with: >-
    A bare promise with no consequence (We will get you 20 clients guaranteed), which is what most marketers do.
  anchor: >-
    What makes a guarantee have power is a conditional statement: If you do not get X result in Y time period, we will Z.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 662
  confirmations: 3
  anchor_at: "100m-offers.md:662"
  tier: 1
  merged_from: [C-offers-025]
- id: E-offers-012
  type: term
  name: >-
    Unconditional Guarantee
  statement: >-
    An unconditional guarantee is a no-questions-asked refund, effectively a trial where the buyer pays first and then decides whether to keep it.
  definition: >-
    Unconditional are the strongest guarantees. They're basically a trial where they pay first then see if they like it.
  why: >-
    It gets a lot more people to buy, but some will refund; satisfaction or no-questions-asked is the highest form of guarantee because the seller can do everything right and still be asked for the money back.
  authors_caveat: >-
    Works much better in lower-ticket B2C situations and becomes very risky in higher-ticket services with high costs of fulfillment; the more conditions are added, the faster it loses its teeth.
  anchor: >-
    Unconditional are the strongest guarantees. They're basically a trial where they pay first then see if they like it.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 678
  confirmations: 2
  anchor_at: "100m-offers.md:678"
  tier: 1
- id: E-offers-013
  type: term
  name: >-
    Conditional Guarantee
  statement: >-
    A conditional guarantee attaches terms and conditions, normally the key actions the client must take to succeed, and pays out in something better than money back.
  definition: >-
    Conditional guarantees include terms and conditions to the guarantee. These are the ones you can get VERY creative on. In general, you want these to be better than money back guarantees.
  why: >-
    If the client is making an investment, their commitment should be matched psychologically with an equal or higher one; tying the guarantee to the key actions of success also gets clients results.
  applies_when: >-
    Preferred as the ticket rises and the offer becomes more business-oriented, and where the product has a lot of cost attached to fulfillment.
  anchor: >-
    Conditional guarantees include “terms and conditions” to the guarantee. These are the ones you can get VERY creative on.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 682
  confirmations: 2
  anchor_at: "100m-offers.md:682"
  tier: 1
  merged_from: [C-offers-031]
- id: E-offers-014
  type: term
  name: >-
    Anti-Guarantee
  statement: >-
    An anti-guarantee is the explicit position that all sales are final, owned openly and backed by a creative reason why.
  definition: >-
    Anti-guarantees are when you explicitly state all sales are final. You will want to own this position. You must come up with a creative reason why the sales are final.
  why: >-
    It acts as a damaging admission: the reason why exposes a real vulnerability of the seller, which makes the product look so powerful that once seen it cannot be unseen. Since some sort of guarantee is standard, not having one is attention-worthy.
  applies_when: >-
    Items that are consumable or massively diminish in value once given, high-ticket products requiring a lot of work or customization, and services with a tremendous amount of cost attached.
  anchor: >-
    Anti-guarantees are when you explicitly state “all sales are final.” You will want to own this position.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 686
  confirmations: 3
  anchor_at: "100m-offers.md:686"
  tier: 1
  merged_from: [C-offers-032]
- id: E-offers-015
  type: term
  name: >-
    Implied Guarantee
  statement: >-
    An implied guarantee is any performance-based offer, revshare, profitshare, ratchets, triggers or bonuses, where no performance means no payment.
  definition: >-
    Implied guarantees are any offer that is a performance-based offer. This comes in many different forms. Revshare, profitshare, triggers, ratchets, monetary bonuses, etc are all examples. The end all concept is the same, if I don't perform, I don't get paid.
  why: >-
    It makes the seller accountable to the client's results and weeds out low performers, and it carries upside: doing a great job means being very well compensated.
  applies_when: >-
    Only where there is transparency for measuring the outcome and trust or control that compensation will follow performance; the drawbacks are tracking and collection.
  anchor: >-
    Implied guarantees are any offer that is a performance-based offer. This comes in many different forms. Revshare, profitshare, triggers, ratchets, monetary bonuses, etc are all examples.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 690
  confirmations: 2
  anchor_at: "100m-offers.md:690"
  tier: 1
- id: E-offers-018
  type: term
  name: >-
    Price to Value Discrepancy
  statement: >-
    The price to value discrepancy is the gap between what the buyer pays and what they believe they get; the moment value dips below price they stop buying, and the gap is to be widened by adding value rather than by cutting price.
  definition: >-
    They believe what they are getting (VALUE) is worth more than what they are giving in exchange for it (PRICE). The moment the value they receive dips below what they are paying, they stop buying from you.
  why: >-
    The simplest way to widen the gap is lowering the price, and it is most of the time the wrong decision: price can only go down to zero but value can go infinitely high, so the price is raised only after value has been sufficiently increased.
  anchor: >-
    They believe what they are getting (VALUE) is worth *more* than what they are giving in exchange for it (PRICE). The moment the value they receive dips below what they are paying, they stop buying from you.
  source: >-
    100m-offers.md, ch. 5 Pricing: Charge What It’s Worth, line 1131
  confirmations: 3
  anchor_at: "100m-offers.md:1131"
  tier: 1
- id: E-offers-022
  type: term
  name: >-
    Hormozi Law
  statement: >-
    Hormozi Law: the longer you delay the ask, the bigger the ask you can make.
  definition: >-
    Hormozi Law: The longer you delay the ask, the bigger the ask you can make. The longer the runway, the bigger the plane that can take off.
  anchor: >-
    Hormozi Law: The longer you delay the ask, the bigger the ask you can make.
  source: >-
    100m-offers.md, ch. 11 Enhancing The Offer, line 1553
  confirmations: 1
  anchor_at: "100m-offers.md:1553"
  tier: 1
- id: E-offers-023
  type: term
  name: >-
    Starving Crowd
  statement: >-
    A starving crowd is a market with so much demand for a solution that the business can be mediocre, the offer terrible and the persuasion absent and it still sells out.
  definition: >-
    You could have the worst hot dogs, terrible prices, and be in a terrible location, but if you're the only hot dog stand in town and the local college football game breaks out, you're going to sell out. That's the value of a starving crowd.
  why: >-
    Market beats everything below it in the order of importance: Starving Crowd (market) > Offer Strength > Persuasion Skills.
  anchor: >-
    but if you’re the only hot dog stand in town and the local college football game breaks out, you’re going to sell out. That’s the value of a starving crowd.
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market -- A Starving Crowd, line 1597
  confirmations: 4
  anchor_at: "100m-offers.md:1597"
  tier: 1
  merged_from: [C-offers-040]
- id: E-offers-024
  type: term
  name: >-
    Normal market
  statement: >-
    A normal market is one growing at the same rate as the marketplace that has common unmet needs falling into health, wealth or relationships; the whole book assumes at least this.
  definition: >-
    which I define as a market that is growing at the same rate as the marketplace and that has common unmet needs that fall into one of three categories: improved health, increased wealth, or improved relationships
  why: >-
    You can be in a normal market growing at an average rate and still make crazy money, but in a bad market (a shrinking one, like newspapers) nothing in the method will work.
  not_to_confuse_with: >-
    A great market (a buying frenzy) and a bad market (a dying one); the rule is not to pick a bad market, normal ones are fine.
  anchor: >-
    which I define as a market that is growing at the same rate as the marketplace and that has common unmet needs that fall into one of three categories: improved health, increased wealth, or improved relationships.
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market -- A Starving Crowd, line 1621
  confirmations: 2
  anchor_at: "100m-offers.md:1621"
  tier: 1
- id: E-offers-025
  type: term
  name: >-
    Niche slap
  statement: >-
    A niche slap is the author's coined reminder to commit to a niche once picked instead of hopping between markets.
  definition: >-
    I have coined the term niche slap to remind entrepreneurs in my communities to commit once they pick.
  why: >-
    All markets have unpleasant characteristics and the grass is never greener; switching who you market to means starting over from the beginning each time, so you fail far longer.
  anchor: >-
    I have coined the term “niche slap” to remind entrepreneurs in my communities to commit once they pick.
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market -- A Starving Crowd, line 1697
  confirmations: 3
  anchor_at: "100m-offers.md:1697"
  tier: 1
  merged_from: [C-offers-044]
- id: E-offers-026
  type: term
  name: >-
    Offer fatigue
  statement: >-
    Offers fatigue when a market has seen them for years, and in local markets they fatigue faster because the addressable radius is small.
  definition: >-
    over time, offers fatigue. And in local markets, they fatigue even faster.
  not_to_confuse_with: >-
    Having reached an audience once: reaching an audience one time in no way means an offer is fatigued, since most people do not even notice an offer on the first mention.
  anchor: >-
    Now here’s the rub: over time, offers fatigue. And in local markets, they fatigue even faster.
  source: >-
    100m-offers.md, ch. 16 Naming, line 1967
  confirmations: 2
  anchor_at: "100m-offers.md:1967"
  tier: 1
- id: E-offers-027
  type: term
  name: >-
    Wrapper (wrapping paper)
  statement: >-
    The wrapper is the exterior perception of the offer, its name, headline, copy and creative, which is changed to refresh a fatigued offer while the offer itself stays the same.
  definition: >-
    We are not changing the actual offer. We are only changing the wrapping paper. Changing the wrapper simply means changing the exterior perception of what your Grand Slam Offer is.
  why: >-
    Renaming refreshes an offer and keeps leads coming forever; the work done, services provided and products offered remain unchanged as the name shifts.
  not_to_confuse_with: >-
    The value stack, money model and price, which sit lower on the variation list and are changed only as a last resort because they are operationally heavy.
  anchor: >-
    We are *not* changing the actual offer. We are only changing the *wrapping paper*.
  source: >-
    100m-offers.md, ch. 16 Naming, line 1971
  confirmations: 3
  anchor_at: "100m-offers.md:1971"
  tier: 1
- id: E-offers-028
  type: term
  name: >-
    M-A-G-I-C formula
  statement: >-
    M-A-G-I-C is the author's naming formula: Magnet (a magnetic reason why), Avatar, Goal, Interval and Container.
  definition: >-
    Each roughly translates to: Attention (M-Magnet), Discrimination (A-Avatar), Purpose (G-Goal), Timeline (I-Interval), and Method (C-Container).
  applies_when: >-
    Naming an offer, a promotion, and each item in the stack and bundle; typically three to five of the components are used, and not necessarily in the M-A-G-I-C order.
  anchor: >-
    Each roughly translates to: Attention (M-Magnet), Discrimination (A-Avatar), Purpose (G-Goal), Timeline (I-Interval), and Method (C-Container).
  source: >-
    100m-offers.md, ch. 16 Naming, line 1991
  confirmations: 4
  anchor_at: "100m-offers.md:1991"
  tier: 1
  merged_from: [C-offers-047, C-offers-048]
- id: E-offers-029
  type: term
  name: >-
    Container word
  statement: >-
    The container word is the part of a name that signals the offer is a bundle, a system, something that cannot be held up against a commoditized alternative: Challenge, Blueprint, Bootcamp, Intensive, Masterclass and the like.
  definition: >-
    The container word denotes that this offer is a bundle of lots of things put together. It's a system. It's something that can't be held up to a commoditized alternative.
  anchor: >-
    The container word denotes that this offer is a bundle of lots of things put together.
  source: >-
    100m-offers.md, ch. 16 Naming, line 2027
  confirmations: 1
  anchor_at: "100m-offers.md:2027"
  tier: 1
- id: E-offers-031
  type: term
  name: >-
    Lifetime Value (LTGP, Lifetime Gross Profit)
  statement: >-
    Lifetime value here is gross profit accrued over the whole life of a customer, gross profit multiplied by the number of purchases an average customer makes, excluding indirect costs such as admin, software and rent.
  definition: >-
    Lifetime Value: The gross profit accrued over the entire lifetime of a customer. This is gross profit multiplied by the number of purchases an average customer will make over their lifetime.
  not_to_confuse_with: >-
    Revenue-based definitions of LTV used by other sources: the author counts gross profit over the lifespan and also calls it LTGP, Lifetime Gross Profit, in other texts.
  anchor: >-
    The gross profit accrued over the entire lifetime of a customer.This is gross profit multiplied by the number of purchases an average customer will make over their lifetime.
  source: >-
    100m-offers.md, ch. 3 Pricing: The Commodity Problem, line 2208
  confirmations: 5
  anchor_at: "100m-offers.md:2208"
  tier: 1
  merged_from: [E-lost-chapters-016, E-playbooks-price-024, E-playbooks-price-025]
- id: E-offers-034
  type: term
  name: >-
    Grand Slam Offer
  statement: >-
    A Grand Slam Offer is an offer that cannot be compared with anything else on the market, combining an attractive promotion, an unmatchable value proposition, a premium price, an unbeatable guarantee and a money model that gets you paid to acquire customers.
  definition: >-
    It's an offer you present to the marketplace that cannot be compared to any other product or service available, combining an attractive promotion, an unmatchable value proposition, a premium price, and an unbeatable guarantee with a money model (payment terms) that allows you to get paid to get new customers . . . forever removing the cash constraint on business growth.
  why: >-
    It hits all three requirements for growth at once: increased response rates, increased conversion and premium prices, and it removes price comparison by putting the business in a category of one.
  not_to_confuse_with: >-
    A commodity offer, which sells the same fulfillment on price; the work is the same in both cases, the perception is not.
  anchor: >-
    an offer you present to the marketplace that cannot be compared to any other product or service available, combining an attractive promotion, an unmatchable value proposition, a premium price, and an unbeatable guarantee
  source: >-
    100m-offers.md, ch. 3 Pricing: The Commodity Problem, line 2240
  confirmations: 3
  anchor_at: "100m-offers.md:2240"
  tier: 1
  merged_from: [E-offers-035]
- id: E-offers-036
  type: term
  name: >-
    Category of one (sell in a vacuum)
  statement: >-
    Selling in a category of one means the prospect's decision is between your product and nothing, so the price is whatever they can be got to perceive rather than a comparison with alternatives.
  definition: >-
    it allows you to sell in a category of one, or, to apply another great phrase, to sell in a vacuum. The resulting purchasing decision for the prospect is now between your product and nothing.
  why: >-
    Establishing your own category makes it too difficult to compare prices, which recalibrates the prospect's value-meter; in this new perceived marketplace you are a monopoly and can make monopoly profits.
  anchor: >-
    it allows you to sell in a “category of one,” or, to apply another great phrase, to “sell in a vacuum.”
  source: >-
    100m-offers.md, ch. 3 Pricing: The Commodity Problem, line 2242
  confirmations: 3
  anchor_at: "100m-offers.md:2242"
  tier: 1
  merged_from: [E-offers-032]
- id: E-offers-037
  type: term
  name: >-
    Sales to Fulfillment Continuum
  statement: >-
    The sales to fulfillment continuum is the trade-off between ease of sale and ease of fulfillment: doing less makes the offer harder to sell, doing as much as possible makes it easy to sell and hard to fulfill.
  definition: >-
    Whenever you are building a business, you have a continuum between ease of fulfillment and ease of sales. If you lower what you have to do, it increases how hard your product or service is to sell.
  why: >-
    The goal is the sweet spot where something sells very well and is also easy to fulfill; the author's mantra is create flow, monetize flow, then add friction, because without demand flowing in you have no idea whether what you have is good.
  anchor: >-
    Whenever you are building a business, you have a continuum between ease of fulfillment and ease of sales.
  source: >-
    100m-offers.md, ch. 10 Value Offer: Creating Your Grand Slam Offer Part II: Trim & Stack, line 2393
  confirmations: 1
  anchor_at: "100m-offers.md:2393"
  tier: 1
```
