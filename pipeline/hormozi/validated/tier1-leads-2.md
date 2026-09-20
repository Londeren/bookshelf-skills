# $100M Leads (2023), from #4 Run Paid Ads to the end (lines 6901–14623) — ярус 1, группа `tier1-leads-2`, единиц после валидации: 117

Часть `pipeline/hormozi/validated.md` (там шапка, гейт, список валидаторов и правила обращения с якорем). Блоки перенесены из `pipeline/hormozi/catch/tier1-leads-2-<X>.md` байт в байт; фазой 2 дописаны `tier`, `merged_from` и поднятое `confirmations`. Проверка: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/validated/tier1-leads-2.md`.


## A. Фреймворки — 34

```yaml
- id: A-leads-2-002
  type: framework
  name: >-
    Find a platform where these four things are true
  statement: >-
    A platform is worth advertising on when all four hold: you have used it and got value from it as a consumer, you can target people on it interested in your stuff, you know how to format ads specific to it, and you have the minimum amount of money to place an ad.
  why: >-
    Having used the platform yourself means you have some idea how it works, and the four conditions together are what stay constant while the platforms themselves keep changing.
  applies_when: >-
    Choosing the first platform to advertise on; start with one platform that meets the four requirements.
  structure:
    - >-
      I've used it and gotten value from it as a consumer. So I have some idea how it works.
    - >-
      I can target people on the platform interested in my stuff.
    - >-
      I know how to format ads specific to the platform.
    - >-
      I have the minimum amount of money to spend to place an ad.
  anchor: >-
    what I look for in a platform I want to advertise on:
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step 1, lines 7133–7167
  confirmations: 2
  authors_caveat: >-
    ...And yes, platforms change all the time, but these principles stay the same.
  anchor_at: "100m-leads.md:7148"
  tier: 1
  merged_from: [B-leads-2-002]
- id: A-leads-2-005
  type: framework
  name: >-
    Four verbal callouts
  statement: >-
    Verbal callouts — using words to get attention — come in four kinds: Labels, Yes-Questions, If-Then Statements and Ridiculous Results.
  why: >-
    Callouts harness the cocktail party effect and cut through the noise; if they never notice your ad, nothing else matters, and the first impression is the part of the ad the author tests the most.
  applies_when: >-
    Writing the headline or first five seconds of an ad; make callouts specific enough to get the right people and broad enough to get as many of them as you can.
  structure:
    - >-
      Labels: A word or set of words putting people into a group — features, traits, titles, places and other descriptors the ideal customer identifies with (LOCAL AREA + TYPE OF PERSON for local ads).
    - >-
      Yes-Questions: Questions where if people answer "yes, that's me" they qualify themselves for the offer.
    - >-
      If-Then Statements: If they meet your conditions then you help them make a decision.
    - >-
      Ridiculous Results: Bizarre, rare, or out of the ordinary stuff someone would want.
  anchor: >-
    Here's what I look for with verbal callouts-
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #3 Call Out, lines 7359–7404
  confirmations: 2
  authors_caveat: >-
    Now, this isn't an exhaustive list. Far from it. I show you these to pull back the curtain.
  anchor_at: "100m-leads.md:7359"
  tier: 1
  merged_from: [B-leads-2-008]
- id: A-leads-2-007
  type: framework
  name: >-
    The What-Who-When Framework
  statement: >-
    To answer why a prospect should be interested, run the offer through three lenses in order: The What (the eight key elements of value and their opposites), The Who (whose perspective experiences them), and The When (past, present and future).
  why: >-
    Putting the What, the Who and the When together answers WHY they should be interested; each new who-perspective applied to each value driver produces a fresh angle, and the more angles you cover, the more interested they become.
  applies_when: >-
    Writing the value chunk of an ad, once the callout has their attention; it hinges on knowing the value equation forwards and backwards.
  structure:
    - >-
      The What: Eight Key Elements — how the offer fulfills each element of value and how it helps avoid their hidden costs.
    - >-
      The Who: show how the eight key things change your prospect's status, and how the people they know give status to them or take it away.
    - >-
      The When: get the prospect to see the consequences of buying and not buying through their past, present, and future.
  anchor: >-
    share with you my What-Who-When Framework. This mental framework hinges
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #3 Get Them Interested, lines 7539–7841
  confirmations: 4
  anchor_at: "100m-leads.md:7553"
  tier: 1
  merged_from: [A-leads-2-010, E-leads-2-006]
- id: A-leads-2-008
  type: framework
  name: >-
    The What: Eight Key Elements
  statement: >-
    Know eight things about your product: the four value elements and the four opposites — Dream Outcome / Nightmare, Perceived Likelihood of Achievement / Risk, Time Delay / Speed, Effort and Sacrifice / Ease — and show both in the ad.
  why: >-
    The best ads make the benefits look as big as possible and the costs look as small as possible; carrots and sticks, how your offer delivers more good stuff and less bad stuff.
  applies_when: >-
    The What lens of the What-Who-When framework.
  structure:
    - >-
      Dream Outcome: show and tell the maximum benefit the prospect can achieve using the thing you sell.
    - >-
      Opposite - Nightmare: show the worst possible hassles, pain, etc. of going without your solution.
    - >-
      Perceived Likelihood of Achievement: lower perceived risk with success of people like them, authority, guarantees.
    - >-
      Opposite - Risk: show how risky it is to not act, how they will repeat their past failures.
    - >-
      Time Delay: show how slow their current trajectory is or that they'll never get what they want at their current rate.
    - >-
      Opposite - Speed: show and tell how much faster they will get the thing they want.
    - >-
      Effort and Sacrifice: show the work and skill they'll need to get the result without your solution.
    - >-
      Opposite - Ease: tell and show how you can avoid the stuff you hate doing without working hard, or having a lot of skill, and still get the dream outcome.
  anchor: >-
    Those are the 8 key elements. Now we fully understand
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, The What, lines 7580–7656
  confirmations: 3
  anchor_at: "100m-leads.md:7653"
  tier: 1
  merged_from: [B-leads-2-012]
- id: A-leads-2-009
  type: framework
  name: >-
    The Who: two groups of people
  statement: >-
    Outline two groups: the people gaining status (your customers) and the people giving it to them — Spouse, Kids, Parents, Extended Family, Colleagues, Bosses, Friends, Rivals, Competitors — then talk about the value elements from each of their perspectives.
  why: >-
    Humans are primarily status driven, and the status of one human comes from how the other humans treat them; talking about the value elements from someone else's perspective shows all the ways the product improves the customer's status and surfaces bonus benefits you'd miss looking only from their own perspective.
  applies_when: >-
    The Who lens of the What-Who-When framework; apply each new who-perspective to each value driver.
  structure:
    - >-
      The first group is the people gaining status, your customers.
    - >-
      The second group is the people giving it to them: Spouse, Kids, Parents, Extended Family, Colleagues, Bosses, Friends, Rivals, Competitors, etc.
  anchor: >-
    outline two groups of people. The first group is the people gaining
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Who, lines 7664–7703
  confirmations: 1
  anchor_at: "100m-leads.md:7670"
  tier: 1
- id: A-leads-2-011
  type: framework
  name: >-
    The Three Phases of Scaling Paid Ads
  statement: >-
    Spending on ads goes through three phases in order: Track Money (set up accurate tracking before spending a dollar), Lose Money (budget losses while you find a winner), Print Money (once you make back more than you spend, reverse the budget from your sales goals).
  why: >-
    Without tracking you get cleaned out, like playing a casino game for as long as you feel like rather than as long as you can afford; the number of losses is high but small because you know when to shut it down, and the wins are few but big because you know when to hit the gas.
  applies_when: >-
    Deciding how much to spend on paid ads.
  structure:
    - >-
      Phase One: Track Money
    - >-
      Phase Two: Lose Money
    - >-
      Phase Three: Print Money
  anchor: >-
    There are three stages to spending money on ads as I see
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8066–8198
  confirmations: 5
  authors_caveat: >-
    In the Lose Money phase the author budgets two times the cash he collects from a customer in thirty days (not LTGP) to test a new ad, and shuts an ad off before 1x thirty-day cash if it produces no leads at all.
  anchor_at: "100m-leads.md:8071"
  tier: 1
  merged_from: [B-leads-2-021, B-leads-2-024, B-leads-2-033, D-leads-2-007]
- id: A-leads-2-012
  type: framework
  name: >-
    Two big levers to improving LTGP:CAC
  statement: >-
    There are only two levers on the LTGP-to-CAC ratio: make CAC lower by getting cheaper customers through more efficient ads, and make LTGP higher by increasing how much you make per customer through a better business model.
  why: >-
    Entrepreneurs often think they have crappy ads (high CAC) when in reality they have a crappy business model (low LTGP); costs can only approach zero but how much you make can go up to infinity.
  applies_when: >-
    Use the industry average CAC as the guide: if your CAC is below 3x your industry average, focus on your business model (LTGP); if it is above 3x the average, focus on your advertising (CAC).
  structure:
    - >-
      Make CAC lower - Get cheaper customers. We do this with more efficient ads.
    - >-
      Make LTGP higher - Increase how much you make per customer. We do this with a better business model.
  anchor: >-
    You have two big levers to improving LTGP:CAC:
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, Cost & Returns, lines 8261–8316
  confirmations: 4
  authors_caveat: >-
    Every business the author invests in that struggles to scale had an LTGP to CAC ratio below 3 to 1 — "This is a pattern I personally observed, not a rule." (2023 figures)
  anchor_at: "100m-leads.md:8261"
  tier: 1
  merged_from: [B-leads-2-028, D-leads-2-013]
- id: A-leads-2-013
  type: framework
  name: >-
    More, Better, New
  statement: >-
    Any of the core four can be boosted in three ways, in this order: do more of what you're currently doing, do what you're currently doing better, and do it somewhere new.
  why: >-
    Even with no improvements, doubling the inputs gets more engaged leads, and the biggest increases often come from advertising more; better and more work with each other, and only once more–better are exhausted do the real returns come from new.
  applies_when: >-
    You are already doing the core four and still not getting as many engaged leads as you want.
  structure:
    - >-
      You can do more of what you're currently doing.
    - >-
      You can do what you're currently doing better.
    - >-
      You can do it somewhere new.
  anchor: >-
    you advertise more? Could you advertise better? Could you advertise
  source: >-
    100m-leads.md, Core Four On Steroids: More Better New, lines 8720–8771; summary lines 9163–9190
  confirmations: 5
  anchor_at: "100m-leads.md:8762"
  tier: 1
  merged_from: [C-leads-2-043, E-leads-2-014]
- id: A-leads-2-014
  type: framework
  name: >-
    The Rule of 100
  statement: >-
    Do 100 primary actions every day, for one hundred days in a row, in whichever of the core four you have chosen.
  why: >-
    The author's one promise: if you do 100 primary actions per day for 100 days straight, you will get more engaged leads; most people dramatically underestimate the volume it takes to make advertising work.
  applies_when: >-
    The "More" of More Better New; step #2 of the one page advertising checklist offers a choice between the Rule of 100 and Open To Goal.
  structure:
    - >-
      Warm Reach Outs: 100 reach outs per day (email, text, direct message, calls, etc.)
    - >-
      Post Content: 100 minutes per day making content, releasing at least one per day on a platform.
    - >-
      Cold Reach Outs: 100 reach outs per day (email, text, direct message, cold call, flyers, etc.); expect lower response rates, so use automation.
    - >-
      Paid Ads: 100 minutes per day making paid ads, and 100 days straight of running those paid ads.
  anchor: >-
    The rule of 100 is simple. You advertise your stuff by doing 100
  source: >-
    100m-leads.md, Core Four On Steroids, More, lines 8805–8887
  confirmations: 5
  anchor_at: "100m-leads.md:8810"
  tier: 1
  merged_from: [B-leads-2-035, B-leads-2-036, D-leads-2-065]
- id: A-leads-2-015
  type: framework
  name: >-
    One test per week per platform — the Monday testing schedule
  statement: >-
    Every Monday run one split test per platform, give it a week, and the next Monday do three things: pick the winners, write the result into a log of all tests, and design the next test to beat the current best version.
  why: >-
    Testing several things at once on one platform means you never learn what worked, steps affect each other, one test per week forces you to prioritise, and a week is long enough to see whether the improvement is real.
  applies_when: >-
    The "Better" of More Better New; do the most testing at whatever step the most leads drop off — the constraint.
  structure:
    - >-
      Every Monday we run one split test per platform.
    - >-
      Look at the results, and pick the winners for each platform test.
    - >-
      Then (important), we write down the results of the test in a log of all tests.
    - >-
      Come up with our next test to beat our current 'best' version.
  anchor: >-
    In every company I own, I set up a testing schedule. Every Monday we
  source: >-
    100m-leads.md, Core Four On Steroids, Better, lines 8912–9035
  confirmations: 5
  authors_caveat: >-
    If we can't beat the version we're currently running in four tries (or one month), we move onto the next constraint; one week is long enough given the size of the author's team and ad spend.
  anchor_at: "100m-leads.md:9009"
  tier: 1
  merged_from: [B-leads-2-039, B-leads-2-041, D-leads-2-020, D-leads-2-022]
- id: A-leads-2-016
  type: framework
  name: >-
    New placements → New Platforms → New Core Four
  statement: >-
    When you go "new", expand in this rough order: new placements on a platform you know, then a new platform, then an entirely new core four activity.
  why: >-
    The order comes down to one thing — what will get the most leads for the amount of work; nine times out of ten that is placements first, platforms second, a new core four activity last.
  applies_when: >-
    When the returns you get from doing more and better are lower than what you could get from a new placement or new way of advertising.
  structure:
    - >-
      New placements
    - >-
      New Platforms
    - >-
      New Core Four
  anchor: >-
    ]{.calibre3}[new]{.calibre24}[. Use this rough order: new placement, new
  source: >-
    100m-leads.md, Core Four On Steroids, New, lines 9104–9157 (the order itself at line 9130)
  confirmations: 3
  anchor_at: "100m-leads.md:9154"
  tier: 1
  merged_from: [B-leads-2-045]
- id: A-leads-2-018
  type: framework
  name: >-
    The four lead getters
  statement: >-
    Four kinds of other people advertise your stuff for you: Customers, Employees, Agencies and Affiliates; you do the core four to get them, and then they do the core four on your behalf.
  why: >-
    All four let other people know about your stuff, so all four are higher leverage than doing it on your own; the core four stacks — once to get them, and a second time when the lead getters get engaged leads for you.
  applies_when: >-
    Scaling past what one person can advertise; the author puts them in the order they arise naturally — referrals, employees, agencies, affiliates.
  structure:
    - >-
      #1 Customers - they buy your stuff then tell other people about it to get you leads. Biggest potential for low-cost exponential growth.
    - >-
      #2 Employees - people in your business that get you leads. They have your direct influence and run your business on your behalf.
    - >-
      #3 Agencies - businesses with services that get you leads. They teach skills you keep forever and can transfer to your team.
    - >-
      #4 Affiliates - businesses who tell their audiences about your stuff to get you leads. Once you get them going, they can operate entirely on their own.
  anchor: >-
    [#1 Customers]{.calibre11}[- they buy your stuff then tell other people
  source: >-
    100m-leads.md, Section IV: Get Lead Getters, lines 9464–9486; restated Section IV Conclusion, lines 13259–13278
  confirmations: 5
  anchor_at: "100m-leads.md:9464"
  tier: 1
  merged_from: [D-leads-2-026, D-leads-2-036, E-leads-2-020]
- id: A-leads-2-019
  type: framework
  name: >-
    The referral growth equation
  statement: >-
    Referrals (in) minus churned customers (out) decides whether word of mouth grows the business: referrals greater than churn means you grow without any other advertising, equal means you need other advertising, less means you advertise just to break even.
  why: >-
    With the core four, inputs and outputs are roughly linear; with word of mouth one customer brings two, two bring four, so growth is exponential and can be maintained no matter how big you get — which is why so few scale on word of mouth: they lose customers faster than they get them.
  applies_when: >-
    Measuring whether your product can grow the business on referrals alone; figure out your referral percentages and churn percentages to set a baseline.
  structure:
    - >-
      If referrals are greater than churn: you grow without any other advertising (yay!)
    - >-
      If referrals are equal to churn: you need other advertising to grow your business (meh)
    - >-
      If referrals are less than churn: you've got to advertise to break even (boo - most folks)
  anchor: >-
    get them. Look at the referral growth equation to see it in action.
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, lines 9813–9842
  confirmations: 5
  anchor_at: "100m-leads.md:9815"
  tier: 1
  merged_from: [B-leads-2-048, B-leads-2-068, D-leads-2-027, E-leads-2-022]
- id: A-leads-2-021
  type: framework
  name: >-
    Six Ways To Get More Referrals By Giving More Value
  statement: >-
    Six ways to build the goodwill that produces referrals, mapped one-to-one onto the parts of an ad: sell better customers, set better expectations, get more people better results, get faster results, keep making your stuff better, and tell them what to buy next.
  why: >-
    The difference between price and value is goodwill; lots of goodwill creates word of mouth, and word of mouth means referrals — and since you can only lower price so far for so long, the question is not how to lower price but how to give more value.
  applies_when: >-
    Before or alongside asking for referrals; building goodwill does a fantastic job of getting referrals on its own.
  structure:
    - >-
      Call Outs → Sell Better Customers
    - >-
      Dream Outcome → Set Better Expectations
    - >-
      Increase Perceived Likelihood of Achievement → Get More People Better Results
    - >-
      Decrease Time Delay → Get Faster Results
    - >-
      Decrease Effort and Sacrifice → Keep Making Your Stuff Better
    - >-
      Call to Action → Tell Them What To Buy Next
  anchor: >-
    There are six ways I get referrals by giving more value. And it just so
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 9944–10291
  confirmations: 2
  anchor_at: "100m-leads.md:9949"
  tier: 1
- id: A-leads-2-022
  type: framework
  name: >-
    The process to get more people better results (six steps)
  statement: >-
    Find what your best customers did and make everyone do it: survey, interview, find the common actions, force new customers to repeat them, measure the improvement, and match your guarantee's conditions to those actions.
  why: >-
    The customers with the best results get the most value from your product; at Gym Launch, gym owners who ran paid ads and made a sale in the first seven days tripled their LTGP, so getting everyone to do that lifted average results, testimonials and referrals.
  applies_when: >-
    Way #3 of the six ways to give more value (Increase Perceived Likelihood of Achievement).
  structure:
    - >-
      Step #1: Survey customers to find the ones who got the best results.
    - >-
      Step #2: Interview them to find out what they did differently.
    - >-
      Step #3: Look at the actions they had in common.
    - >-
      Step #4: Force new customers to repeat the actions that got the best results.
    - >-
      Step #5: Measure the improvement in average customer results (speed and outcome)
    - >-
      Step #6: Match the conditions of your guarantee to the actions that get the best results to get more people to do them.
  anchor: >-
    Here's the process I use to get more people better results:
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10069–10141
  confirmations: 3
  anchor_at: "100m-leads.md:10097"
  tier: 1
  merged_from: [B-leads-2-053, B-leads-2-054]
- id: A-leads-2-023
  type: framework
  name: >-
    Five ways to make wins happen faster
  statement: >-
    To make wins feel faster, give them more often: split deliverables into shorter intervals, treat updates as wins, force wins in the first forty-eight hours, always book the next contact, and set timelines with breathing room so you deliver early.
  why: >-
    Faster wins increase their perception of speed, increase the likelihood they'll stick, and increase how much they trust you; if someone said seven things would happen and all seven do, referring a friend becomes lower risk.
  applies_when: >-
    Way #4 of the six ways to give more value (Decrease Time Delay).
  structure:
    - >-
      If I have seven small things to deliver, I deliver them at shorter intervals rather than all at once.
    - >-
      Updates are wins. If it's a bigger project, I share progress updates as frequently as possible.
    - >-
      Customers form their lasting impression of a business within the first forty-eight hours after they buy. Force as many wins as you can in that window.
    - >-
      They should always know the next time they'll hear from you. BAMFAM: Book-A-Meeting-From-A-Meeting.
    - >-
      Never expect customers to forgive you. You can deliver early, but never late. I add fifty percent to my timelines so I always deliver early.
  anchor: >-
    Here's five ways I make wins happen faster in the real
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10147–10198
  confirmations: 7
  anchor_at: "100m-leads.md:10164"
  tier: 1
  merged_from: [B-leads-2-055, B-leads-2-056, B-leads-2-057, B-leads-2-058, D-leads-2-032, D-leads-2-033]
- id: A-leads-2-024
  type: framework
  name: >-
    The process to keep making your stuff better (six steps)
  statement: >-
    Run a recurring monthly loop on the product: find the most common problem from service data, surveys and reviews; design the fix with feedback from customers who made it work anyway; implement; release to a small group of struggling customers; re-test; then move to the next most common problem.
  why: >-
    There's no such thing as a perfect product — you can always make it better, and the easier you make it for customers to benefit, the more goodwill you get and the more likely they'll refer.
  applies_when: >-
    Way #5 of the six ways to give more value (Decrease Effort & Sacrifice); set it as a recurring monthly process.
  structure:
    - >-
      Step #1: Use customer service data, surveys, and reviews to find the most common problem with your product.
    - >-
      Step #2: Figure out your fix. Get feedback from the customers who made your product work for them despite the problem it has.
    - >-
      Step #3: Use that feedback to improve your product.
    - >-
      Step #4: Give the new version to a small group of your (struggling) customers.
    - >-
      Step #5: Get your next round of feedback. If you solved the original problem, roll it out to all customers. If it didn't, go back to step #2.
    - >-
      Step #6: Move to the next most common problem and repeat the process. Do this until the end of time.
  anchor: >-
    the more likely they'll refer. Here's my process to keep making
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10206–10251
  confirmations: 2
  anchor_at: "100m-leads.md:10213"
  tier: 1
  merged_from: [B-leads-2-059]
- id: A-leads-2-026
  type: framework
  name: >-
    Seven Ways To Ask For Referrals
  statement: >-
    Seven combinations of incentive, currency and ask that worked best: one-sided referral benefit, two-sided referral benefits, ask right when they buy, referrals as a negotiation chip, referral events, ongoing referral programs, and unlockable referral bonuses.
  why: >-
    Referring is always a risk for the customer — they risk their goodwill with their friend — so you add benefits for them and their friends with incentives and lower the risk by building goodwill; done this way Dropbox 39x'd in fifteen months and PayPal reached a million users in two years.
  applies_when: >-
    After building goodwill with the six ways to give more value — capitalize on that goodwill by asking.
  structure:
    - >-
      One-Sided Referral Benefit: pay your average CAC to the referrer or the friend, and ask for an actual three-way introduction right when they buy.
    - >-
      Two-Sided Referral Benefits: pay the CAC to both parties, half to the referrer and half to the friend (what Dropbox and PayPal used).
    - >-
      Ask For A Referral Right When They Buy: on the sales contract or checkout page, ask for names and phone numbers of people they'd like to do this with.
    - >-
      Add Referrals As A Negotiation Chip: give a discount in exchange for an introduction to three friends — you changed the terms of the sale.
    - >-
      Referral Events: points, credits, dollars or bragging rights for bringing friends within an explicit time period, typically one to four weeks.
    - >-
      Ongoing Referral Programs: talk about the benefits of doing things with others all the time, in free content, outreach, paid ads, etc.
    - >-
      Unlockable Referral Bonuses: bonuses for people who 1) refer and 2) leave a testimonial — VIP bonuses, courses, tokens, status, training, merchandise, premium support.
  anchor: >-
    you a hundred variations that may or may not work, here are the seven
  source: >-
    100m-leads.md, #1 Customer Referrals, Seven Ways To Ask For Referrals, lines 10389–10542
  confirmations: 6
  anchor_at: "100m-leads.md:10396"
  tier: 1
  merged_from: [B-leads-2-062, B-leads-2-063, B-leads-2-064, B-leads-2-065, B-leads-2-066]
- id: A-leads-2-027
  type: framework
  name: >-
    The Internal Core Four
  statement: >-
    Getting employees is the same advertising you already do, with the frame changed from potential customers to potential employees: warm outreach becomes asking your network, cold outreach becomes recruiting, posting content becomes posting job openings, paid ads become promoting job postings, and the lead getters map across too.
  why: >-
    Employees are just other people you let know about your stuff, so the actions to get employees line up with the actions to get customers — and like getting customers, you can build a reliable process, and when you need more you do more.
  applies_when: >-
    You need more workers in order to advertise more; you need both processes to scale.
  structure:
    - >-
      Warm Outreach→Asking Your Network
    - >-
      Cold Outreach→ Recruiting
    - >-
      Post Content→Posting Job Openings
    - >-
      Paid Ads→Promoting Job Postings
    - >-
      Customer Referrals→Employee Referrals
    - >-
      Affiliates→ Associations, Guilds, Listservs etc.
    - >-
      Agencies→ Staffing firms etc.
    - >-
      Employees→Employees (unchanged)
  anchor: >-
    Remember the core four? Well, they work for getting employees too.
  source: >-
    100m-leads.md, #2 Employees, How To Get Employee Leads, lines 11003–11058
  confirmations: 3
  anchor_at: "100m-leads.md:11007"
  tier: 1
  merged_from: [B-leads-2-070, E-leads-2-029]
- id: A-leads-2-028
  type: framework
  name: >-
    The 3Ds: document, demonstrate, duplicate
  statement: >-
    Train an employee to get leads in three steps: document the job as a checklist written exactly as you do it, demonstrate by walking them through the checklist step by step, then have them duplicate it while you observe and fix the checklist.
  why: >-
    If the checklist is right, the outcome will be the same, and if it's off you'll find out fast; the level of clarity to shoot for is that a stranger could get your results if they only followed your checklist.
  applies_when: >-
    Turning a hired employee into a lead-getter, when you cannot afford people who already know how.
  structure:
    - >-
      Step One - Document. You make a checklist. Follow it yourself on a work block and see if you can do an A+ job following only your own directions — that's the first draft.
    - >-
      Step Two - Demonstrate: You do it in front of them. Walk them through the checklist step by step, adjusting it wherever they stop or slow you down — the second draft.
    - >-
      Step Three - Duplicate: They do it in front of you. They follow the same checklist while you observe; fix the checklist until it's right, then have them follow it until they get it right.
  anchor: >-
    activities. I think about and actually approach training with this 3Ds
  source: >-
    100m-leads.md, #2 Employees, How To Get Employees To Get You Leads, lines 11074–11137
  confirmations: 4
  authors_caveat: >-
    If they get it wrong or get confused then we got it wrong or made it confusing; but there is a difference between competence and performance — if the instructions are fine they just need practice.
  anchor_at: "100m-leads.md:11080"
  tier: 1
  merged_from: [B-leads-2-071, B-leads-2-072, E-leads-2-030]
- id: A-leads-2-029
  type: framework
  name: >-
    How to Calculate Returns From Lead-Getting Employees
  statement: >-
    Excluding paid ad spend, compare payroll with what the leads bring: total payroll divided by total engaged leads gives cost per engaged lead, multiplied by engaged leads per customer gives CAC, and LTGP divided by CAC gives the ratio.
  why: >-
    The cost of advertising with employees (outreach, content, etc.) is almost entirely the money you pay them to do it, so payroll against engaged leads is the whole calculation.
  applies_when: >-
    Measuring employee lead-getting; as long as your total costs of getting a customer are at least one-third of the lifetime profit, you're in good shape.
  structure:
    - >-
      Total Payroll / Total Engaged Leads = Cost per engaged lead.
    - >-
      (cost per engaged lead) x (engaged leads per customer) = CAC
    - >-
      (LTGP) / (CAC) = your LTGP : CAC ratio
  anchor: >-
    this by just comparing how much money we spend on payroll to how much
  source: >-
    100m-leads.md, #2 Employees, How to Calculate Returns, lines 11205–11248
  confirmations: 2
  anchor_at: "100m-leads.md:11212"
  tier: 1
  merged_from: [B-leads-2-080]
- id: A-leads-2-030
  type: framework
  name: >-
    Advertising problem or sales problem — one diagnostic question
  statement: >-
    When CAC is more than 3x industry average, ask one question — do my engaged leads have the problem I solve and the money to spend? — and branch: not qualified is an advertising problem; qualified and buying but too few is an advertising problem; qualified and not buying is a sales problem.
  why: >-
    Don't fire your sales guy if you've got advertising problems, and don't fire your advertising employees if you've got a sales problem; one company spent twelve weeks and $150,000 on ads that worked fine, blamed advertising, and the confusion cost an estimated ~$30M in enterprise value.
  applies_when: >-
    Your cost to get a customer is more than 3x the industry average; within 3x means you're doing good enough and should bump up LTGP instead.
  structure:
    - >-
      If no, then they're not qualified--that's an advertising problem.
    - >-
      They're buying but you don't have enough of them--advertising problem.
    - >-
      They're qualified but not buying--sales problem.
  anchor: >-
    Do my engaged leads have the problem I solve and the money to
  source: >-
    100m-leads.md, #2 Employees, Which Employees to Focus On, lines 11259–11291; Personal Lessons from Paid Ads, lines 8463–8475
  confirmations: 5
  anchor_at: "100m-leads.md:11272"
  tier: 1
  merged_from: [B-leads-2-031, D-leads-2-015, D-leads-2-047]
- id: A-leads-2-031
  type: framework
  name: >-
    How I Use Agencies Now — buy the skill, then leave
  statement: >-
    Start every agency relationship with a stated purpose and a deadline: work with them for about six months to learn how they do it, pay extra for them to explain their decisions, train your team on it, run both teams until yours beats theirs, then drop to a lower-cost consulting arrangement and finally cut them loose.
  why: >-
    You get better short-term results because they probably know more than you, and better long-term results because you or your team learn to do it; you only get a fraction of the agency's attention and results get worse whenever they take on new clients, while your team stays focused on you full-time.
  applies_when: >-
    As soon as you have enough money for a good agency, and specifically for two things: learning new methods and learning new platforms.
  structure:
    - >-
      Decide if using an agency makes sense for you right now.
    - >-
      Talk to a lot of agencies to get a feel for the market. Don't be cheap.
    - >-
      Use the agreement framework I outlined.
    - >-
      Set a clear deadline to force you (and your team) to learn the skills.
    - >-
      Use both teams until yours beats theirs regularly.
    - >-
      Switch to discounted consulting until you feel like you're teaching them instead of them teaching you...then cut 'em loose.
  anchor: >-
    start every agency relationship with a purpose and a deadline to fulfill
  source: >-
    100m-leads.md, #3 Agencies, lines 11676–11745; Next Steps, lines 11894–11921
  confirmations: 7
  authors_caveat: >-
    To make it work at scale you have to count on a good amount of time where you pay the agency and your team to do the same stuff; the author's time to get a team as good as an agency went from about a year down to six months or less.
  anchor_at: "100m-leads.md:11683"
  tier: 1
  merged_from: [B-leads-2-083, B-leads-2-085, D-leads-2-049, D-leads-2-050, D-leads-2-052]
- id: A-leads-2-032
  type: framework
  name: >-
    What I look for in a good agency (ten checks)
  statement: >-
    A list of ten things all the good agencies had in common — word-of-mouth referrals, recognisable clients, a waiting list, a clear sales process with realistic expectations, long-term strategy over hacks, clarity about what they need from you, a regular meeting schedule, simple tracked reporting, a good offer by the four value elements, and a high price.
  why: >-
    If you only know about an agency from their paid ads or cold outreach, they probably aren't as good as the ones who rely solely on word of mouth; and all good agencies are expensive, but not all expensive agencies are good.
  applies_when: >-
    Comparing agencies before signing; talk with a few more even if one already agrees to your terms.
  structure:
    - >-
      Somebody I know got good results working with them.
    - >-
      Prominent companies got good results working with them.
    - >-
      A waiting list. When demand for a service exceeds the supply, they are probably pretty good.
    - >-
      A clear sales process that makes a point to set realistic expectations. No funny business.
    - >-
      No short term hacks. They keep the talk on long term strategy, with clear timelines for setup, scaling, and results.
    - >-
      They tell me exactly what they need from me, when they need it, and how they use it.
    - >-
      They suggest a regular schedule of meetings and offer several ways to update me on their progress.
    - >-
      They give updates in simple terms and have clear ways to track so I know how costs compare with results.
    - >-
      They make a good offer: dream outcome, perceived likelihood of achievement, time delay, effort and sacrifice.
    - >-
      They are expensive. All good agencies are expensive... but not all expensive agencies are good.
  anchor: >-
    After working with tons of bad agencies, and a handful of good ones, I
  source: >-
    100m-leads.md, #3 Agencies, How to Pick The Right Agency, lines 11763–11836
  confirmations: 5
  authors_caveat: >-
    Now it isn't the last word on what makes a good agency, but it is useful stuff that's worked for me.
  anchor_at: "100m-leads.md:11763"
  tier: 1
  merged_from: [B-leads-2-086, B-leads-2-087, B-leads-2-088, D-leads-2-053]
- id: A-leads-2-033
  type: framework
  name: >-
    How To Build An Affiliate Army in Six Steps
  statement: >-
    Building an affiliate army runs through six steps in order: find your ideal affiliates, make them an offer, qualify them, figure out what to pay them, get them advertising, and keep them advertising.
  why: >-
    Affiliates are among the most advanced ways to get engaged leads — first you have to convince them to advertise someone else's stuff, second to advertise yours, third to keep advertising so they become a long-term lead source.
  applies_when: >-
    Recruiting other businesses to tell their audiences about your stuff; the author built ALAN and Prestige Labs this way, together more than $75,000,000 in revenue from over 5000+ affiliates.
  structure:
    - >-
      Step 1: Find Your Ideal Affiliates
    - >-
      Step 2: Make Them an Offer
    - >-
      Step 3: Qualify Them
    - >-
      Step 4: Figure Out What To Pay Them
    - >-
      Step 5: Get Them Advertising
    - >-
      Step 6: Keep Them Advertising
  anchor: >-
    How To Build An Affiliate Army in Six Steps
  source: >-
    100m-leads.md, #4 Affiliates and Partners, lines 12174–12215
  confirmations: 1
  anchor_at: "100m-leads.md:12174"
  tier: 1
- id: A-leads-2-034
  type: framework
  name: >-
    Find Your Ideal Affiliate — the questions
  statement: >-
    The ideal affiliate has a business with a warm audience full of people like your customers; find them by asking, about your best customers, what they buy, where they go, what they like to do, and — if you sell direct to consumer — what businesses they work for.
  why: >-
    In a nutshell the question is "Who's got my leads!?" — once you know the businesses that have your leads, you know exactly where to put your advertising efforts.
  applies_when: >-
    Step 1 of building an affiliate army; if none come to mind, answer these questions about your best customers, and if you struggle, call up your customers and ask them.
  structure:
    - >-
      What do they buy? → Who provides that stuff?
    - >-
      Where do they go? → What businesses are in those surrounding areas?
    - >-
      What do they like to do? → Who provides those services?
    - >-
      If direct to consumer: What types of businesses do they work for? What kinds of jobs do they have?
  anchor: >-
    The ideal affiliate has a business with a warm audience full of people
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 1, lines 12226–12286
  confirmations: 2
  anchor_at: "100m-leads.md:12230"
  tier: 1
  merged_from: [B-leads-2-090]
- id: A-leads-2-035
  type: framework
  name: >-
    The six affiliate hit list categories
  statement: >-
    Every new affiliate hit list starts from six categories of business around your customer: softwares, products, equipment, services, groups they belong to, and events they attended.
  why: >-
    If you find a business that falls into multiple categories, there's a high chance they've got lots of good leads for you and that they'd make a great affiliate.
  applies_when: >-
    Building the affiliate lead list in Step 1; the author made a list of 200 products and services for agencies when starting ALAN and they fit neatly into these categories.
  structure:
    - >-
      softwares
    - >-
      products
    - >-
      equipment
    - >-
      services
    - >-
      groups they belong to
    - >-
      events they attended
  anchor: >-
    Every time I create a new affiliate "hit list" I start with these
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 1, lines 12264–12273
  confirmations: 2
  anchor_at: "100m-leads.md:12270"
  tier: 1
  merged_from: [B-leads-2-091]
- id: A-leads-2-036
  type: framework
  name: >-
    Two ways to get affiliates invested: make them a customer, make them an expert
  statement: >-
    Qualify a potential affiliate by getting them to invest — make them buy and preferably use the product to keep affiliate status, and make them pay for the onboarding and training that certifies them as a product expert.
  why: >-
    Nine times out of ten, if they pay, they'll pay attention; the more money an affiliate invests in your product the more money they make, and certification covers some of the advertising cost and pays for proper onboarding of every single affiliate.
  applies_when: >-
    Step 3 of building an affiliate army. If you don't get enough people to start, lower the commitment; if you don't get enough people to follow through, raise it.
  structure:
    - >-
      Way #1: Make Them A Customer — make them buy and preferably use the product to keep affiliate status.
    - >-
      Way #2: Make Them An Expert — they pay for the onboarding and training that certifies them as a product expert; charge 10-20% of what the average active affiliate makes in the first twelve months.
  anchor: >-
    invested and winning: make them a customer, and make them an expert.
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 3: Qualify Them, lines 12375–12446
  confirmations: 4
  anchor_at: "100m-leads.md:12390"
  tier: 1
  merged_from: [B-leads-2-093, B-leads-2-094, D-leads-2-057]
- id: A-leads-2-038
  type: framework
  name: >-
    The three-tier affiliate payout structure
  statement: >-
    Split the maximum allowable CAC into three payout tiers: 25% for anyone who agrees to your initial terms, 50% once they activate, and 100% once they sustain a level of performance.
  why: >-
    Not all affiliates are created equal, and the tiered method has a hidden and very profitable side effect — the average payout is much less than your maximum allowable CAC, and the leftover funds contests, recruiting more affiliates, or profit.
  applies_when: >-
    Setting affiliate compensation in Step 4; the author's worked example has a $40 maximum allowable CAC and a blended payout of $30, moving LTGP : CAC from 3:1 to 4:1.
  structure:
    - >-
      Tier 1: 25% CAC - Anyone who agrees to my initial terms qualifies. Example: They sign up and buy products or a certification.
    - >-
      Tier 2: 50% CAC - Once they activate. Example: actually finishing the certification they bought, doing a specific number of posts and outreach, doing a launch, etc.
    - >-
      Tier 3: 100% CAC - Once they sustain a level of performance. Example: They maintain five customers per month on subscription.
  anchor: >-
    I give it to. Not all affiliates are created equal. So, I suggest having
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 4, lines 12516–12572
  confirmations: 5
  anchor_at: "100m-leads.md:12518"
  tier: 1
  merged_from: [B-leads-2-099, C-leads-2-035, D-leads-2-059, E-leads-2-035]
- id: A-leads-2-039
  type: framework
  name: >-
    The whisper-tease-shout method
  statement: >-
    A launch has three phases that mirror the three chunks of an ad: whisper (think call outs — curiosity, keep the product mysterious), tease (think elements of value — reveal the product, make the date public, use the What-Who-When framework), shout (think call to action — specific actions, bonuses, scarcity, urgency, guarantees).
  why: >-
    Curiosity comes from wanting to know what happens next, so whispers plant questions and teases satisfy them; the longer something appears to take, the more an audience will value it, which is why the whisper phase can start years out.
  applies_when: >-
    Activating affiliates through launches — but this is how you launch anything, not just affiliates; good launches have the work done ahead of time, so do all the work for the affiliates and let them plug and play.
  structure:
    - >-
      Whisper: Think "Call Outs." The key is curiosity. Keep the product itself mysterious and hint at how big of a deal it is.
    - >-
      Tease: Think "Elements Of Value." Reveal your product, make the date of the launch public, and start showing the elements of value.
    - >-
      Shout: Think "Call to Action." Give specific actions for the audience to take when the product launches; bonuses, scarcity, urgency, and guarantees around being "the first ones."
  anchor: >-
    should, you may as well do them right. I use the whisper-tease-shout
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 5: Get Them Advertising -- Launch, lines 12588–12738
  confirmations: 4
  authors_caveat: >-
    I can't remember where I first heard this, but the name stuck.
  anchor_at: "100m-leads.md:12614"
  tier: 1
  merged_from: [B-leads-2-101, C-leads-2-036, E-leads-2-037]
- id: A-leads-2-040
  type: framework
  name: >-
    The launch cadence for whisper, tease and shout
  statement: >-
    The launch has a fixed schedule: whisper every four to six weeks until sixty days out then every two to three weeks until thirty days out; tease once per week until fourteen days out then twice per week until three days out; shout at least twice a day from three days out, every few hours on the day, then every thirty minutes until launch.
  why: >-
    The cadence tightens as the launch nears so that curiosity built early is converted into exposure at the moment the product becomes available — you shout to get as many people exposed to your offer as you can.
  applies_when: >-
    Running a launch with or for affiliates.
  structure:
    - >-
      Start whispering every four to six weeks until you get sixty days out. Then whisper every two to three weeks until you get thirty days out.
    - >-
      Start teasing once per week until fourteen days out. Then tease twice per week until three days out.
    - >-
      Shout at least twice a day starting three days out. On the day of, start shouting every few hours until two hours out. Then shout every thirty minutes until you launch.
  anchor: >-
    [Action Step]{.calibre11}[: Start whispering every four to six weeks
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 5, lines 12671–12727
  confirmations: 4
  anchor_at: "100m-leads.md:12671"
  tier: 1
  merged_from: [B-leads-2-102, B-leads-2-103, B-leads-2-104]
- id: A-leads-2-041
  type: framework
  name: >-
    Three ways to integrate your product into an affiliate's offer
  statement: >-
    Integration comes in three forms, ordered from easiest to hardest: the affiliate gives away your lead magnet with every purchase of their stuff, sells your lead magnet separately to their audience, or directly sells your core offer.
  why: >-
    The strategy to start them advertising differs from the one to keep them advertising; integration is what turns a single affiliate sale into engaged leads for life.
  applies_when: >-
    Step 6 of building an affiliate army — keeping affiliates advertising long term.
  structure:
    - >-
      You can get them to give away your lead magnet with every purchase of their stuff.
    - >-
      You can get them to sell your lead magnet separately to their audience.
    - >-
      You can get them to directly sell your core offer.
  anchor: >-
    I've got three ways you can integrate your product into their offer. I
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 6: Keep Them Advertising, lines 12744–12917
  confirmations: 3
  authors_caveat: >-
    All three strategies work. They're just different. After testing, the author's companies continue to do Strategy 1 twice per year as a big event and Strategy 3 on an ongoing basis.
  anchor_at: "100m-leads.md:12756"
  tier: 1
  merged_from: [B-leads-2-108, E-leads-2-039]
- id: A-leads-2-046
  type: framework
  name: >-
    One Page Advertising Checklist
  statement: >-
    The whole advertising plan fits on one page in five steps: pick the type of engaged lead to get, pick Rule of 100 or Open To Goal and commit to the daily actions, fill out the advertising checklist for that daily action, do it daily until you can afford to pay someone else, then go back to step 1 with employees as the new target lead type.
  why: >-
    Laying the action steps out on a single page leaves little room for excuses, distractions and delusions — you either did the stuff or you didn't — and it can be filled out in about five minutes.
  applies_when: >-
    Starting or resetting daily advertising work; the checklist is filled out for one daily action at a time.
  structure:
    - >-
      Step #1: Pick The Type Of Engaged Lead To Get: Customers, Affiliates, Employees, or Agencies
    - >-
      Step #2: Pick Rule of 100 or Open To Goal. Commit To Your Daily Advertising Actions
    - >-
      Step #3: Fill Out The Advertising Checklist For That Daily Action
    - >-
      Step #4: Do this daily action until you have enough money to afford paying someone else to do it.
    - >-
      Step #5: When you do, go back to step 1. Make employees your new target lead type. And repeat steps 1-4 until you have the help you need. Then, scale again.
  anchor: >-
    [Step #1:]{.calibre11}[ Pick The Type Of Engaged Lead To Get: Customers,
  source: >-
    100m-leads.md, Advertising in Real Life: Open To Goal, One Page Advertising Checklist, lines 13887–13921
  confirmations: 5
  authors_caveat: >-
    The content of steps #2 and #3 is given in the book only as images, so the checklist's own fields are not in the text.
  anchor_at: "100m-leads.md:13891"
  tier: 1
  merged_from: [B-leads-2-117, B-leads-2-118, B-leads-2-119, D-leads-2-067]
- id: A-leads-2-047
  type: framework
  name: >-
    The Roadmap — seven levels of advertisers
  statement: >-
    Scaling advertising runs through levels, each with one primary action: warm outreach; consistent warm outreach plus content; hiring employees to advertise; a product good enough for consistent referrals; advertising in more places, more ways, with more people; hiring battle-hardened executives; and a seventh level the author has not reached.
  why: >-
    Acquisition.com uses this roadmap to scale portfolio companies from a few million a year to $100,000,000+, and the levels let you identify where you are on the advertising totem pole so you know what to do to get to the next one.
  applies_when: >-
    Diagnosing which advertising problem to work on next at your current size.
  structure:
    - >-
      Level 1: Your friends know about the stuff you sell. Primary Action: Warm outreach.
    - >-
      Level 2: You consistently let everyone you know about the stuff you sell. Primary Actions: Do as much warm outreach and post as much content as you can consistently.
    - >-
      Level 3: You get employees to help you do more advertising. Primary Action: You hire people to advertise profitably on your behalf.
    - >-
      Level 4: Your product is good enough to get consistent referrals. Primary Actions: Focus on your product until you get consistent referrals (25% or more of customers), then go back to scaling advertising with a bigger team.
    - >-
      Level 5: You advertise in more places in more ways with more people. Primary Action: Advertise profitably using at least two methods on multiple platforms.
    - >-
      Level 6: You hire killers. Primary Action: Get battle-hardened executives and department heads to take over new advertising activities and channels.
    - >-
      Level 7: I'll come back and edit this chapter once I cross a billion.
  anchor: >-
    this chapter, I describe the phases you will go through as you scale
  source: >-
    100m-leads.md, The Roadmap - Putting it All Together, lines 13996–14130
  confirmations: 7
  authors_caveat: >-
    Last Points: I know this looks clean. But it never is. Real business is messy. Level 7 is not written — the author had not crossed a billion at the time of writing (2023).
  anchor_at: "100m-leads.md:13997"
  tier: 1
  merged_from: [B-leads-2-120, B-leads-2-121, B-leads-2-123, B-leads-2-124, D-leads-2-069]
```


## B. Правила и критерии — 46

```yaml
- id: B-leads-2-001
  type: rule
  statement: >-
    An audience is only broadened after the smaller one has been advertised to profitably, and is made as big as it can be while still turning a profit.
  why: >-
    As the audience gets bigger it has more of the wrong people but more of the right ones too, so the ratio of spend to sales drops while the total money made goes up.
  applies_when: >-
    Scaling paid ads from a first working audience.
  anchor: >-
    Once we advertise profitably in a small puddle of an audience, we
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, lines 7096–7106
  confirmations: 3
  anchor_at: "100m-leads.md:7096"
  tier: 1
  merged_from: [D-leads-2-002]
- id: B-leads-2-004
  type: rule
  name: >-
    Lookalike audience
  statement: >-
    The list uploaded to build a lookalike audience is assembled in order of quality — current and previous customers first, then warm reach out contacts, then cold reach out leads — only until the platform minimum is reached.
  why: >-
    The bigger the list and the higher quality the contacts, the more responsive the lookalike audience; forcing the list to size sometimes makes it too broad, which filters then fix.
  applies_when: >-
    The platform allows lookalike audiences; if you cannot make one, start by targeting interests.
  anchor: >-
    Start with your list of current and previous customers. If your
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #2, lines 7218–7269
  confirmations: 2
  anchor_at: "100m-leads.md:7225"
  tier: 1
- id: B-leads-2-005
  type: rule
  statement: >-
    Filters are stacked on top of the audience early on to make the list more specific, and loosened later, not the other way round.
  why: >-
    The more specific the list, the more efficient the ads but the faster you burn through it; the wins from small specific audiences pay for advertising to larger, broader ones later.
  applies_when: >-
    Early paid-ad campaigns with a limited budget.
  anchor: >-
    the list, the more efficient your ads but the faster you will "burn"
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #2, lines 7251–7256
  confirmations: 1
  anchor_at: "100m-leads.md:7252"
  tier: 1
- id: B-leads-2-009
  type: rule
  statement: >-
    In a local ad the callout names the smallest local area the buyer identifies with, combined with the type of person (LOCAL AREA + TYPE OF PERSON).
  why: >-
    People automatically identify with their local area, so the more local, the better: Americans < Texans < Dallas Residents < Irving Residents.
  applies_when: >-
    Advertising a local business.
  anchor: >-
    So with local ads, the more local, the better. A local
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #3, lines 7372–7380
  confirmations: 1
  anchor_at: "100m-leads.md:7373"
  tier: 1
- id: B-leads-2-014
  type: rule
  statement: >-
    Ad length is varied by adding or removing value angles, while the callout (the first few seconds) and the CTA stay the same.
  why: >-
    The only difference between long ads and short ads is how many angles from the copywriting framework there is time to cover.
  applies_when: >-
    Adapting one ad to platforms with different lengths.
  anchor: >-
    away based on the platform, but keep the callouts (the first few
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #3, lines 7806–7810
  confirmations: 1
  anchor_at: "100m-leads.md:7809"
  tier: 1
- id: B-leads-2-020
  type: rule
  statement: >-
    Each next step reminds the person of the action they just took and shows how the next action follows from it.
  why: >-
    In Robert Cialdini's Influence, people like to think of themselves as consistent, so reminding them of the action they just took gets more of them to take the second one.
  applies_when: >-
    Multi-step opt-in flows (ad to CTA to contact information).
  anchor: >-
    action they just took (CTA), and show how taking the next action aligns
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #4, lines 7940–7947
  confirmations: 1
  anchor_at: "100m-leads.md:7943"
  tier: 1
- id: B-leads-2-022
  type: rule
  statement: >-
    A new ad is given a test budget of two times the cash collected from a customer in the first thirty days (not LTGP) before it is shut off, as long as it is producing leads.
  why: >-
    Letting ads run too long wastes money, but giving up on ads before they have had a chance wastes even more; two times thirty-day cash is the author's sweet spot.
  applies_when: >-
    Testing new paid ads. Figure from $100M Leads, 2023.
  anchor: >-
    I budget two times the cash I collect from a customer in thirty days
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, lines 8146–8157
  confirmations: 2
  anchor_at: "100m-leads.md:8146"
  tier: 1
  merged_from: [D-leads-2-009]
- id: B-leads-2-023
  type: rule
  statement: >-
    An ad producing no leads at all is shut off before it has spent one times the thirty-day cash from a customer.
  why: >-
    Below that spend there is nothing to learn from an ad that has produced nothing, and the money is better spent on the next test.
  applies_when: >-
    Testing new paid ads that generate zero leads.
  anchor: >-
    leads from an ad at all, before I spend 1x thirty-day cash I shut it off
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, lines 8155–8157
  confirmations: 1
  anchor_at: "100m-leads.md:8156"
  tier: 1
- id: B-leads-2-025
  type: rule
  statement: >-
    Once ads break even or better, the daily ad budget is calculated backwards from how many customers you want or can handle multiplied by your cost per customer, and then committed to.
  why: >-
    The question stops being how much to spend and becomes how many customers you can handle; if the resulting number terrifies you, you are doing it right — trust the data.
  applies_when: >-
    Ads at or above break-even.
  anchor: >-
    ads break even or better, I reverse my budget from my sales
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, lines 8187–8198
  confirmations: 2
  anchor_at: "100m-leads.md:8189"
  tier: 1
  merged_from: [D-leads-2-011]
- id: B-leads-2-026
  type: rule
  statement: >-
    The budget reversed from a customer goal is padded by twenty percent.
  why: >-
    Ads get less efficient as they scale, so 100 customers at $100 needs $12,000 over thirty days ($400 per day), not $10,000.
  applies_when: >-
    Scaling a profitable ad budget.
  anchor: >-
    they scale, I usually pad the budget by twenty percent. So that means
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, lines 8190–8195
  confirmations: 1
  anchor_at: "100m-leads.md:8193"
  tier: 1
- id: B-leads-2-027
  type: rule
  name: >-
    LTGP to CAC
  statement: >-
    Paid advertising is measured as lifetime gross profit per customer divided by cost to acquire a customer, and the ratio has to be above 3 to 1.
  why: >-
    Every business the author invests in that struggles to scale has an LTGP to CAC below 3 to 1, and as soon as it goes above 3 to 1, by lowering CAC or raising LTGP, they take off; all the costs of getting a customer together should be at most one third of the lifetime profit.
  applies_when: >-
    Judging whether advertising and the business model are working. Benchmark from $100M Leads, 2023.
  anchor: >-
    to CAC ratio was ]{.calibre3}[less than]{.calibre24}[ 3 to 1. As soon as
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, lines 8248–8253; #2 Employees, lines 11295–11298; #4 Affiliates, lines 13144–13146
  confirmations: 6
  authors_caveat: >-
    "This is a pattern I personally observed, not a rule."
  anchor_at: "100m-leads.md:8250"
  tier: 1
  merged_from: [B-leads-1-095, D-leads-1-061, D-leads-2-012]
- id: B-leads-2-029
  type: rule
  name: >-
    Client financed acquisition
  statement: >-
    The customer pays back more than it costs to get and fulfil them within the first thirty days, so the cash can be recycled into getting the next customer.
  why: >-
    Any business can get interest-free money for thirty days in the form of a credit card; cover the cost to get and fulfil the customer in that window and you square the balance, keep the customer and repeat, so money stops being the bottleneck.
  applies_when: >-
    The full LTGP takes months to collect and cash flow blocks scaling.
  anchor: >-
    But... if your customer spends more than it costs you to get
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, lines 8337–8453
  confirmations: 2
  anchor_at: "100m-leads.md:8337"
  tier: 1
- id: B-leads-2-030
  type: rule
  statement: >-
    When the first purchase does not cover CAC inside thirty days, more is sold to the customer immediately rather than waiting for the lifetime profit to accumulate.
  why: >-
    A $100 upsell with 100% margins taken by one in five customers adds $20 of gross profit per customer, which turns $10 collected in thirty days into $30 and covers a $30 CAC; everything after that is gravy.
  applies_when: >-
    LTGP exceeds CAC but the first purchase does not, creating a cash flow problem.
  anchor: >-
    Here's the way I fix it- ]{.calibre3}[I immediately sell them more
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, lines 8390–8439
  confirmations: 1
  anchor_at: "100m-leads.md:8402"
  tier: 1
- id: B-leads-2-034
  type: rule
  statement: >-
    Of the core four, paid ads are taken up last.
  why: >-
    Skills from the other three methods transfer to this one, and paid ads cost money — money you will have if you start with the other three first, which gives the shortest learning curve.
  applies_when: >-
    Choosing the order in which to learn the core four.
  anchor: >-
    I recommend doing paid ads ]{.calibre3}[last]{.calibre41}[ for two
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, Conclusion, lines 8555–8560
  confirmations: 2
  anchor_at: "100m-leads.md:8555"
  tier: 1
  merged_from: [D-leads-2-018]
- id: B-leads-2-038
  type: rule
  name: >-
    Constraints
  statement: >-
    Testing is concentrated on the step of the funnel where the most leads drop off.
  why: >-
    Constraints are the points where the smallest improvements create the biggest boost: improving a 5% apply step by 5 points doubles leads (2x), while the same 5 points on a 30% optin adds 16% and on a 50% schedule adds 10%.
  applies_when: >-
    Choosing what to test next in any lead flow.
  anchor: >-
    "drop-off" point. So ]{.calibre3}[I do the most testing at whatever step
  source: >-
    100m-leads.md, Core Four On Steroids, Better, lines 8924–8970
  confirmations: 2
  anchor_at: "100m-leads.md:8925"
  tier: 1
- id: B-leads-2-042
  type: rule
  statement: >-
    If the current best version cannot be beaten in four tries (or one month), work moves to the next constraint.
  why: >-
    Beyond that point the effort put into making the step better brings lower and lower returns than the same effort spent elsewhere.
  applies_when: >-
    Running weekly tests against a current champion version.
  anchor: >-
    running in ]{.calibre3}[four tries (or one month)]{.calibre24}[, we move
  source: >-
    100m-leads.md, Core Four On Steroids, Better, lines 9025–9035
  confirmations: 2
  anchor_at: "100m-leads.md:9027"
  tier: 1
  merged_from: [D-leads-2-023]
- id: B-leads-2-043
  type: rule
  name: >-
    When to do new
  statement: >-
    Something new is added only when the returns from doing more and better are lower than what the same effort would return in a new placement or a new way of advertising.
  why: >-
    New is much harder in practice, which is why more and better are exhausted first.
  applies_when: >-
    Deciding whether to add a placement, a platform or a core four activity.
  anchor: >-
    from doing more↔better are lower than what you could get from a new
  source: >-
    100m-leads.md, Core Four On Steroids, New, lines 9104–9157
  confirmations: 4
  anchor_at: "100m-leads.md:9105"
  tier: 1
  merged_from: [B-leads-2-044, D-leads-2-025]
- id: B-leads-2-046
  type: rule
  statement: >-
    After warm outreach, the next core four activity is chosen by what you have more of: more time than money means posting content, more money than time means cold outreach or paid ads.
  why: >-
    Advertising is paid for with time, money, or both, and the method picked should be paid for with the resource you actually have.
  applies_when: >-
    Building a business and choosing where to put advertising effort next.
  anchor: >-
    I have more time than money, I move to posting content. If I have more
  source: >-
    100m-leads.md, Core Four On Steroids, Conclusion, lines 9214–9217
  confirmations: 1
  anchor_at: "100m-leads.md:9216"
  tier: 1
- id: B-leads-2-047
  type: rule
  statement: >-
    One core four activity is picked and maxed out with more, better and new before a second is added.
  why: >-
    You only need one to get engaged leads, and the money, systems and experience earned from one method help you master the next.
  applies_when: >-
    Starting out with the core four.
  anchor: >-
    But remember, you only need to do ]{.calibre3}[one]{.calibre41}[ to get
  source: >-
    100m-leads.md, Core Four On Steroids, Conclusion, lines 9221–9232
  confirmations: 1
  anchor_at: "100m-leads.md:9221"
  tier: 1
- id: B-leads-2-049
  type: rule
  statement: >-
    If customers are not bringing you more customers, the product is treated as the problem, not the advertising.
  why: >-
    If your product were exceptional, people would already know about it and you would have more business than you could handle; the question to ask is why customers are too embarrassed to tell everyone they know about it — it may be okay, but unremarkable, as in not worthy of remark.
  applies_when: >-
    Selling direct to consumers with few or no referrals.
  anchor: >-
    business than you could handle. So if you sell direct to consumers and
  source: >-
    100m-leads.md, #1 Customer Referrals, Problem #1, lines 9870–9905
  confirmations: 5
  anchor_at: "100m-leads.md:9882"
  tier: 1
  merged_from: [A-leads-2-020, D-leads-2-028, D-leads-2-029]
- id: B-leads-2-051
  type: rule
  name: >-
    Call Outs → Sell Better Customers
  statement: >-
    You work out what your most successful customers have in common, retarget the advertising callouts at that narrower group, and then sell only people who meet those criteria.
  why: >-
    Customers who get the most value have the most goodwill and are the most likely to refer; increase the quality of the prospect and you increase the quality of the product.
  applies_when: >-
    A business with sales but high churn and a plateau.
  anchor: >-
    Figure out what your most successful customers have in common. Use those
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 9974–10019
  confirmations: 1
  anchor_at: "100m-leads.md:10015"
  tier: 1
- id: B-leads-2-052
  type: rule
  name: >-
    Dream Outcome → Set Better Expectations
  statement: >-
    The promises made in the offer are lowered step by step until close rates start to drop, and then held there.
  why: >-
    You set the expectations, so lowering them leaves room to overdeliver, and that maximises both the number of customers you get and the goodwill you build with them.
  applies_when: >-
    Wanting more referrals from an existing offer.
  anchor: >-
    making offers. Keep lowering them until your close rates lower. At that
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10025–10061
  confirmations: 2
  anchor_at: "100m-leads.md:10058"
  tier: 1
  merged_from: [D-leads-2-031]
- id: B-leads-2-061
  type: rule
  statement: >-
    A request for referrals is built as an offer, showing the value the customer gets for referring.
  why: >-
    The author tried a lot of referral strategies and most failed until this: asking for referrals only works when you treat it like an offer, and referring is a risk to the customer's goodwill with their friend, so the benefit to them has to outweigh it.
  applies_when: >-
    Any referral programme or ask.
  anchor: >-
    Asking for referrals only works when you treat it like an
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10348–10360
  confirmations: 3
  anchor_at: "100m-leads.md:10356"
  tier: 1
  merged_from: [D-leads-2-035]
- id: B-leads-2-067
  type: rule
  statement: >-
    A referral gift card carries an expiration date seven to fourteen days from the day it is given.
  why: >-
    The deadline forces the referrer to use it, and handing a friend a gift card gives the referrer status compared with saying "join my program for $2000 off".
  applies_when: >-
    Running a gift-card referral promotion (the card is worth about one third of the cost of the programme).
  anchor: >-
    Give the gift card an expiration date within seven to fourteen days from
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10552–10572
  confirmations: 1
  anchor_at: "100m-leads.md:10559"
  tier: 1
- id: B-leads-2-073
  type: rule
  statement: >-
    If a step has to be explained, the step is rewritten — it is too complicated or it is several steps in one.
  why: >-
    If they get it wrong or get confused, then we got it wrong or made it confusing; an inferior checklist can be forced to work but becomes a nightmare when someone else takes over training.
  applies_when: >-
    Demonstrating or duplicating a checklist with a new employee.
  anchor: >-
    confusing.]{.calibre24}[ If we have to explain what a step means
  source: >-
    100m-leads.md, #2 Employees, lines 11145–11156
  confirmations: 3
  anchor_at: "100m-leads.md:11147"
  tier: 1
  merged_from: [D-leads-2-042, D-leads-2-043]
- id: B-leads-2-074
  type: rule
  statement: >-
    When an employee knows exactly what to do but is not good at it yet, the instructions are left alone and more reps are given.
  why: >-
    There is a difference between competence and performance — slow, then smooth, then fast.
  applies_when: >-
    Diagnosing whether to fix the checklist or to keep practising.
  anchor: >-
    There is a difference between competence and performance. In other
  source: >-
    100m-leads.md, #2 Employees, lines 11158–11164
  confirmations: 2
  anchor_at: "100m-leads.md:11158"
  tier: 1
  merged_from: [D-leads-2-044]
- id: B-leads-2-075
  type: rule
  statement: >-
    Employees are judged and rewarded on their ability to follow directions rather than on getting the right result.
  why: >-
    Train employees to follow directions and they will follow directions; then if they follow directions and get the wrong result, you know it is the directions, which you have a lot more control over.
  applies_when: >-
    Training and supervising lead-getting employees.
  anchor: >-
    Focus on your employee's ability to follow directions more than
  source: >-
    100m-leads.md, #2 Employees, lines 11166–11172
  confirmations: 2
  anchor_at: "100m-leads.md:11166"
  tier: 1
  merged_from: [B-leads-2-076]
- id: B-leads-2-081
  type: rule
  statement: >-
    For ground-level advertising jobs, anyone willing is hired and trained, and the effort goes into the training rather than into the selection.
  why: >-
    Anyone can be taught to do ground level jobs, so who you pick is not as important as how you train the ones you do; and for low level jobs you will never have a shortage of labour.
  applies_when: >-
    Hiring frontline lead-getting workers.
  anchor: >-
    pick is not as important as how you train the ones you do.
  source: >-
    100m-leads.md, #2 Employees, Conclusion, lines 11317–11353
  confirmations: 2
  authors_caveat: >-
    "Get picky when you have to make massive investments in hyper-specific-multiple-six-figure-C-suite employees."
  anchor_at: "100m-leads.md:11319"
  tier: 1
  merged_from: [D-leads-2-048]
- id: B-leads-2-082
  type: rule
  statement: >-
    Agencies are hired for two things only — learning a new method and learning a new platform — and only once there is money to pay a good one.
  why: >-
    Good agencies cost money; with no money you learn through trial and error. They have already made the big mistakes, so hiring one skips to the make-money part and buys skills you cannot learn elsewhere without spending the time that should go into scaling.
  applies_when: >-
    Considering an agency.
  anchor: >-
    suggest using agencies for two things: learning new methods and learning
  source: >-
    100m-leads.md, #3 Agencies, lines 11635–11670
  confirmations: 2
  anchor_at: "100m-leads.md:11639"
  tier: 1
  merged_from: [D-leads-2-051]
- id: B-leads-2-084
  type: rule
  statement: >-
    On a new platform, one good enough agency is hired to learn the ropes and a more elite one to learn how to maximise it.
  why: >-
    Learning YouTube, the author hired one agency to keep him committed and do legwork, and a second at 4x the price to teach the in-depth ideas; once their own videos beat the agency's, they dropped to consulting.
  applies_when: >-
    Entering an advertising platform you do not understand.
  anchor: >-
    to learn the ropes of a new platform. Then, I hire a more elite agency
  source: >-
    100m-leads.md, #3 Agencies, lines 11707–11720
  confirmations: 1
  anchor_at: "100m-leads.md:11718"
  tier: 1
- id: B-leads-2-089
  type: rule
  statement: >-
    The budget allows for a stretch where the agency and your own team are paid to do the same work at the same time.
  why: >-
    You have to give yourself breathing room to get results from the agency, learn what they do, and train your team on it all at once; it costs a lot of money and is worth it when done right.
  applies_when: >-
    Making the learn-from-the-agency method work at scale.
  anchor: >-
    good amount of time where you pay the agency and your team
  source: >-
    100m-leads.md, #3 Agencies, Conclusion, lines 11866–11872
  confirmations: 2
  anchor_at: "100m-leads.md:11867"
  tier: 1
  merged_from: [D-leads-2-054]
- id: B-leads-2-092
  type: rule
  statement: >-
    What is offered to an affiliate is a fast, simple and easy new way for them to make money, not your product.
  why: >-
    Affiliates are businesses, or start one by signing up, so the offer is advertised to them exactly like any other offer — callout, value elements, call to action — with affiliates as the customer.
  applies_when: >-
    Recruiting affiliates.
  anchor: >-
    offer them a new way to make money. ]{.calibre24}[We'll start with the
  source: >-
    100m-leads.md, #4 Affiliates, Step 2, lines 12292–12364
  confirmations: 4
  anchor_at: "100m-leads.md:12301"
  tier: 1
  merged_from: [D-leads-2-055, D-leads-2-056]
- id: B-leads-2-095
  type: rule
  name: >-
    Make Them An Expert
  statement: >-
    Affiliates pay for the onboarding and certification, priced at 10–20% of what the average active affiliate makes in the first twelve months.
  why: >-
    Too low and they are not invested, too high and you do not get enough affiliates; 10–20% maximises the number who become active. The fee also covers some advertising cost and pays for proper onboarding of every single affiliate.
  applies_when: >-
    Charging for affiliate certification; an affiliate averaging $40,000 a year is charged $4000–$8000. Figures from $100M Leads, 2023.
  anchor: >-
    How much do I charge? ]{.calibre11}[I recommend 10-20% of what the
  source: >-
    100m-leads.md, #4 Affiliates, Step 3, lines 12417–12439
  confirmations: 2
  anchor_at: "100m-leads.md:12429"
  tier: 1
  merged_from: [D-leads-2-058]
- id: B-leads-2-096
  type: rule
  statement: >-
    The affiliate commitment is lowered if not enough people start and raised if not enough people follow through.
  why: >-
    The level of required investment is calibrated against the two failure modes rather than fixed in advance; the warm reachout method of raising the minimum every five sign ups also applies.
  applies_when: >-
    Tuning affiliate entry terms.
  anchor: >-
    If you don\'t get enough people to start, lower
  source: >-
    100m-leads.md, #4 Affiliates, Step 3, lines 12443–12446
  confirmations: 1
  anchor_at: "100m-leads.md:12444"
  tier: 1
- id: B-leads-2-098
  type: rule
  statement: >-
    Affiliate pay is set from your maximum allowable cost to acquire a customer, which is what is left of gross profit after the business keeps its share of a 3:1 LTGP:CAC.
  why: >-
    On a $200 single-use product costing $40 to fulfil, $160 of gross profit at a 3:1 ratio leaves $120 to the business and $40 as the maximum payout for a new customer.
  applies_when: >-
    Deciding affiliate commissions.
  anchor: >-
    I suggest paying affiliates based on your maximum allowable cost to
  source: >-
    100m-leads.md, #4 Affiliates, Step 4, lines 12501–12512
  confirmations: 1
  anchor_at: "100m-leads.md:12501"
  tier: 1
- id: B-leads-2-105
  type: rule
  statement: >-
    The affiliate keeps all the cash from selling a lead magnet that you fulfil.
  why: >-
    It becomes all profit and no work for them, an attractive proposition for any business; your money comes from selling your main thing for more than the lead magnet cost to deliver, and you do not split anything on the core offer. If you give the affiliate all the money, they want to do it more and send even more leads.
  applies_when: >-
    Integration strategy 2, affiliates selling your lead magnet.
  anchor: >-
    sample product, etc. Also, giving affiliates all the cash from selling a
  source: >-
    100m-leads.md, #4 Affiliates, Step 6, lines 12836–12859; case study, lines 13019–13028
  confirmations: 3
  anchor_at: "100m-leads.md:12839"
  tier: 1
- id: B-leads-2-106
  type: rule
  statement: >-
    Affiliate payouts are paid for as long as the customer stays and are never capped.
  why: >-
    Paying forever keeps affiliates motivated to keep your customers forever.
  applies_when: >-
    Splitting money with affiliates on your core offer.
  anchor: >-
    forever so my affiliates stay motivated to keep my customers forever.
  source: >-
    100m-leads.md, #4 Affiliates, Step 6, lines 12868–12871
  confirmations: 1
  anchor_at: "100m-leads.md:12870"
  tier: 1
- id: B-leads-2-109
  type: rule
  statement: >-
    Affiliate returns are measured by comparing the cost to get an affiliate with the gross profit of all the customers that affiliate sends, not with money made from the affiliate.
  why: >-
    You spend money to get affiliates but make little back from affiliates themselves; the money comes back from the customers they bring. A $4000 affiliate CAC against $54,000 of leftover gross profit is 12.5:1.
  applies_when: >-
    Calculating returns on an affiliate programme.
  anchor: >-
    compare how much it costs us to get an affiliate with the gross profit
  source: >-
    100m-leads.md, #4 Affiliates, Costs and Returns, lines 13066–13138
  confirmations: 2
  anchor_at: "100m-leads.md:13074"
  tier: 1
  merged_from: [D-leads-2-061]
- id: B-leads-2-110
  type: rule
  statement: >-
    An affiliate programme is expected to run at least 3:1 LTGP to CAC, and is aimed higher — 5:1 or 10:1 and up.
  why: >-
    Below 3:1 there are three ways to fix it: lower CAC with better ads, offer and sales process; get more affiliates to activate with a launch process; make each affiliate worth more with a better integration process.
  applies_when: >-
    Judging an affiliate programme. Benchmark from $100M Leads, 2023.
  anchor: >-
    least]{.calibre24}[ at 3:1 to have a decent business. Like the example,
  source: >-
    100m-leads.md, #4 Affiliates, Costs and Returns, lines 13144–13165
  confirmations: 2
  anchor_at: "100m-leads.md:13145"
  tier: 1
  merged_from: [A-leads-2-043]
- id: B-leads-2-111
  type: rule
  statement: >-
    The affiliate offer is advertised until there are ten to twenty affiliates, whose results and feedback are used to fix the offer, terms, launches and integration before scaling.
  why: >-
    Their results then become the first batch of affiliate lead magnets used to scale.
  applies_when: >-
    Starting an affiliate programme.
  anchor: >-
    Advertise your affiliate offer until you get ten to twenty affiliates.
  source: >-
    100m-leads.md, #4 Affiliates, Action Steps, lines 13233–13237
  confirmations: 1
  anchor_at: "100m-leads.md:13233"
  tier: 1
- id: B-leads-2-112
  type: rule
  statement: >-
    A chosen lead source is not abandoned after a few losses; three to six months is the expected time to crack a new one.
  why: >-
    It is normal to lose in the beginning, and the author expects three to six months to crack a new lead source and this is not his first rodeo; people try shortcuts for a decade until they realise they should have picked a strategy and stuck with it for a decade.
  applies_when: >-
    Judging whether a lead source has failed.
  anchor: >-
    in three to six months (and this isn't my first rodeo). So if your
  source: >-
    100m-leads.md, Section IV Conclusion, lines 13306–13320
  confirmations: 3
  anchor_at: "100m-leads.md:13318"
  tier: 1
  merged_from: [D-leads-2-062, D-leads-2-063]
- id: B-leads-2-113
  type: rule
  statement: >-
    Some percentage of the advertising budget — 1%, 5% or 10% — is set aside for new campaigns, channels, pages and plain crazy ideas, with no return expected.
  why: >-
    You learn something every time you test, so the money is well spent; when one of the tests wins, and some do, you make far more than you spent. Consider it an investment in your education.
  applies_when: >-
    An established advertising budget. Attributed in the book to a speaker at a private entrepreneurs' event, not to the author.
  anchor: >-
    business and, more importantly, myself. So whether it\'s 1%, 5%, or 10%,
  source: >-
    100m-leads.md, Section V: Get Started, lines 13466–13476
  confirmations: 1
  anchor_at: "100m-leads.md:13473"
  tier: 1
- id: B-leads-2-114
  type: rule
  statement: >-
    A test is run at a volume where the expected response rate produces a countable number of responses — 5,000 flyers, not 300.
  why: >-
    At half a percent (decent) or one percent (a winner), 300 flyers would produce one and a half people, which makes it impossible to tell a winner from a loser; and when a winner is found it goes out 5,000 per day, every day, for a month.
  applies_when: >-
    Testing an advertising channel; response benchmarks are for flyers.
  anchor: >-
    a small number...I test with 5000. Then when we find a winner, we put
  source: >-
    100m-leads.md, Advertising in Real Life, lines 13679–13757
  confirmations: 3
  anchor_at: "100m-leads.md:13696"
  tier: 1
  merged_from: [D-leads-2-064]
- id: B-leads-2-115
  type: rule
  name: >-
    Open To Goal
  statement: >-
    You commit to working until a specific number of outcomes is hit that day, no matter what, rather than to a fixed number of actions or hours.
  why: >-
    It is the rule of 100 for the big kids: it unlocks a level of effort you did not realise you had, and it may mean fifty attempts or five thousand every day for years. Give up the idea of doing your best and do what is required.
  applies_when: >-
    Once the rule of 100 has become normal; the gym chain's sales managers signed up five new members a day, leaving early if done by lunch and working eighteen hours if not.
  anchor: >-
    a specific number of times... you commit to the work until you hit a
  source: >-
    100m-leads.md, Advertising in Real Life, lines 13776–13804
  confirmations: 3
  anchor_at: "100m-leads.md:13792"
  tier: 1
  merged_from: [D-leads-2-066]
- id: B-leads-2-116
  type: rule
  statement: >-
    The daily advertising goal is done in one uninterrupted block at the start of the day, before fires, people and day-to-day work.
  why: >-
    The magic is not in waking early but in a long stretch of uninterrupted work immediately after a long stretch of uninterrupted sleep — the most productive hours in a row of the most productive work, every single day.
  applies_when: >-
    Structuring a day to make open to goal possible; the author's stack is waking at 4–5 am, getting right to work with no rituals, and no meetings until noon.
  anchor: >-
    goal accordingly. Then, only after my dedicated block of work--do I go
  source: >-
    100m-leads.md, Advertising in Real Life, lines 13818–13860
  confirmations: 1
  anchor_at: "100m-leads.md:13848"
  tier: 1
- id: B-leads-2-122
  type: rule
  name: >-
    Level 4
  statement: >-
    Before ramping advertising again, the product is worked on until at least 25% of customers come from referrals.
  why: >-
    This is where most people mess up: they let their product slip and never recover. At the $100M machine level the product is so good that a third of customers bring more customers.
  applies_when: >-
    The fourth level of the advertising roadmap; the author doubled down on referrals after noticing that his ads were off and referrals kept coming, updating the product from customer feedback every two weeks and running a strong referral programme.
  anchor: >-
    shoot for getting 25% or more of your customers from referrals. Now,
  source: >-
    100m-leads.md, The Roadmap, lines 14053–14073, 14189–14190
  confirmations: 3
  anchor_at: "100m-leads.md:14055"
  tier: 1
  merged_from: [D-leads-2-068]
```


## C. Разборы (кейсы) — 17

```yaml
- id: C-leads-2-001
  type: case
  name: >-
    The ugliest ad: the Chino Hills 6 week challenge
  statement: >-
    A text-only all-caps Facebook ad named the town and the number of spots (5 Chino Hills residents), offered a free 6 week challenge, stated the price of entry as before and after pictures, and ended with a single explicit instruction plus a link; leads came within hours, were called and reminded by text an hour before the appointment, and 19 sold at $299 each, turning $1000 of ad spend into just under $5700.
  why: >-
    The ad had no images, no video and no frills, so its whole effect came from a local callout, a concrete offer and a spelled-out next step; conviction made up for the lack of sales skill.
  demonstrates: >-
    The three chunks of an ad (callout, value, CTA); the Label callout with LOCAL AREA + TYPE OF PERSON; a lead magnet that asks for something in exchange; spelling out the next step.
  anchor: >-
    I'M LOOKING FOR 5 CHINO HILLS RESIDENTS TO TAKE PLACE IN A FREE 6 WEEK
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, lines 6975–7006
  confirmations: 1
  anchor_at: "100m-leads.md:6979"
  tier: 1
- id: C-leads-2-003
  type: case
  name: >-
    Weight loss run through What-Who-When
  statement: >-
    The same weight loss offer is written out along a timeline from the prospect's view (teased as a kid — past, struggling to button favourite jeans — present, moving up another belt loop — future), then along the same timeline from other people's view (the kid asking why other kids make fun of them, kids complaining that other dads join practice, the doctor saying he may not walk his daughter down the aisle), and finally as combined copy lines that tag WHO, WHAT and WHEN in one sentence.
  why: >-
    People only think of how decisions affect the here and now; running the past, present and future through their own and other people's perspectives makes them see the consequence of their decision or indecision right now, and produces many different angles from one offer.
  demonstrates: >-
    The What-Who-When framework: value elements plus perspectives plus timeline; the bad stuff first, then contrasted with the good stuff if they buy.
  anchor: >-
    struggling to button their favorite pair of jeans (present) or moving up
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, lines 7728–7776
  confirmations: 1
  anchor_at: "100m-leads.md:7730"
  tier: 1
- id: C-leads-2-005
  type: case
  name: >-
    Ten ads, nine losers, 100x down on the winner
  statement: >-
    $100 goes into each of ten ads ($1,000 total); nine lose the full $100 and one returns $500 on its $100, leaving the account $500 down — most people stop at the loss, but the $500 return marks a winner, so $10,000 goes into that one ad and returns $50,000.
  why: >-
    The number of losses is high but each loss is small because the author knows when to shut an ad down, and the number of wins is low but each win is large because he knows when to hit the gas; to win big you have to see the winners and double, triple, quadruple, 10x down on them.
  demonstrates: >-
    Phase Two Lose Money of the three phases of scaling paid ads; scaling the winner rather than mourning the losers.
  anchor: >-
    Imagine I spend \$100 on ten ads - \$1,000 in total. Nine of them lose
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8126–8130
  confirmations: 1
  anchor_at: "100m-leads.md:8126"
  tier: 1
- id: C-leads-2-007
  type: case
  name: >-
    Reversing the daily budget from the customer goal
  statement: >-
    The question is not how much to spend but how many customers can be handled: 100 customers next month at $100 each requires $10,000, padded twenty percent because ads get less efficient as they scale, giving $12,000 over thirty days or $400 per day — and then the number is committed to.
  why: >-
    Once ads break even or better the constraint is the business, not the budget; if the number terrifies you, you are doing it right — trust the data.
  applies_when: >-
    Phase Three, once ads make back more money than they cost.
  demonstrates: >-
    Reverse the ad budget from the sales goal rather than picking a spend.
  anchor: >-
    next month, and customers cost me \$100 to get, I'd need to spend
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8187–8196
  confirmations: 1
  anchor_at: "100m-leads.md:8191"
  tier: 1
- id: C-leads-2-008
  type: case
  name: >-
    Client financed acquisition on a $15 membership
  statement: >-
    A $15 per month membership costing $5 to deliver leaves $10 gross profit a month; at ten months average tenure that is $100 LTGP against a $30 CAC, a 3.3:1 ratio — profitable but with a cash flow problem, since only $10 comes back in month one. A $100 upsell at 100% margins taken by one in five customers adds $20 average per customer, so $10 + $20 = $30 collected inside thirty days and the customer is free.
  why: >-
    Any business can get interest free money for thirty days on a credit card, so covering the cost to get and fulfil a customer within thirty days squares the balance, removes money as the bottleneck and lets the cash be recycled into the next customer.
  demonstrates: >-
    Client financed acquisition; fixing a cash flow problem by immediately selling more rather than by cutting CAC.
  anchor: >-
    Say we have a \$15 per month membership that costs us \$5 to
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8363–8431
  confirmations: 1
  anchor_at: "100m-leads.md:8363"
  tier: 1
- id: C-leads-2-014
  type: case
  name: >-
    The PR company that renarrowed its call outs
  statement: >-
    A portfolio company doing public relations for generic small businesses had plenty of sales, heavy churn and years of plateau; its lowest churning customers all turned out to be in one specific niche and looking to raise funding from investors — only fifteen percent of the business, so retargeting risked the other eighty-five percent. The advertising call outs were changed to match that narrower perfect fit customer: the plateau broke, growth resumed toward millions per month, advertising cost fell because the messaging could be more specific, and the new customers started referring like clockwork.
  why: >-
    Increase the quality of the prospect and you increase the quality of the product: customers who get the most value have the most goodwill, and the customers with the most goodwill are the most likely to refer.
  demonstrates: >-
    Call Outs → Sell Better Customers, the first of the six ways to get more referrals by giving more value.
  anchor: >-
    To see what we could do, we looked at their lowest churning customers
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, lines 9982–10009
  confirmations: 1
  anchor_at: "100m-leads.md:9988"
  tier: 1
- id: C-leads-2-015
  type: case
  name: >-
    Gym Launch: paid ad and a sale in the first seven days
  statement: >-
    Gym Launch tracked customer activities — speed to running the first paid ad, speed to the first sale, attendance on calls — and compared average customers with the best ones; gym owners who ran paid ads and made a sale in the first seven days had triple the LTGP, so the company forced everyone to launch ads and sell inside seven days, and average results, testimonials and referrals all rose.
  why: >-
    The customers with the best results get the most value from the product, so finding what they did and making everyone else do it raises the results of the average customer.
  demonstrates: >-
    Increase Perceived Likelihood of Achievement → Get More People Better Results; the six-step survey-interview-common actions-force-measure-guarantee process.
  anchor: >-
    We found out something huge. If a gym owner ran paid ads and
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, lines 10082–10092
  confirmations: 1
  anchor_at: "100m-leads.md:10087"
  tier: 1
- id: C-leads-2-018
  type: case
  name: >-
    The salesman who asked who else they'd bring
  statement: >-
    A new salesman shattered the ticket sales records of a portfolio company doing nothing different except one move: he asked each buyer who else they would want to come with them, then asked to be introduced. Half his sales were referrals. The scripted form is: people who do our program with someone else tend to get 3x the results — who else could you do this program with?
  why: >-
    Customers can only know what to do if you tell them, and the ask works when it shows the value the customer gets by referring — here, better results from doing the program with a friend.
  applies_when: >-
    On the sales contract or checkout page, right when they buy.
  demonstrates: >-
    Ask For A Referral Right When They Buy; showing how they get better results doing it with a friend.
  anchor: >-
    ask them who else they'd want to have come with them. Then ask them to
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, Seven Ways To Ask For Referrals, lines 10448–10460
  confirmations: 1
  anchor_at: "100m-leads.md:10453"
  tier: 1
- id: C-leads-2-019
  type: case
  name: >-
    Referrals as a negotiation chip, and the Stacy answer
  statement: >-
    Against a $500 price and a prospect at $400, the discount is traded for introductions: I can't do anything less than $500 down, but if you make a 3-way text introduction to a few of your friends right now, I'd be happy to cut that initiation fee. When a full-priced customer finds out, the answer is that Stacy got $100 off because she referred three friends and the same $100 is available to them for three friends — who do you have in mind?
  why: >-
    You can ethically charge a different price for the same thing because you changed the terms of the sale; the objection ends either way — they back off or they give you three friends.
  demonstrates: >-
    Add Referrals As A Negotiation Chip; handling the discount objection from other customers.
  anchor: >-
    Ex: "I can't do anything less than \$500 down, but if you make a 3-way
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, Seven Ways To Ask For Referrals, lines 10469–10489
  confirmations: 1
  anchor_at: "100m-leads.md:10478"
  tier: 1
- id: C-leads-2-020
  type: case
  name: >-
    The gift card referral promotion
  statement: >-
    Every customer is given a gift card worth one third of the cost of their program to hand to a friend who signs up, with an expiry seven to fourteen days out to force use; the referrer then says I got this gift card for $2000, do you want it, I don't want to waste it, rather than join my program for $2000 off. It combines with the three-way introduction — text a picture of the card with the friend's name written on it, which also gives a reason to ask for the name — and the cards can be sold at ninety percent off to friends of customers, so the referrer looks generous and you get paid to acquire.
  why: >-
    Handing over a gift card gives the referrer status with their friend and makes the offer feel like a much bigger deal than a discount.
  demonstrates: >-
    Combining several of the seven ways to ask: one-sided benefit, three-way introduction, scarcity by expiry.
  anchor: >-
    Give everyone a gift card for one-third the cost of their program. Tell
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, You're Only Limited By Your Creativity, lines 10557–10579
  confirmations: 1
  anchor_at: "100m-leads.md:10557"
  tier: 1
- id: C-leads-2-021
  type: case
  name: >-
    Forty interviews per frontline hire (the cold outreach miss)
  statement: >-
    A cold outreach goal missed two quarters running is traced back through a chain of questions: a rep is lost every four weeks; churn is below industry average for the position; one of every four candidates from HR is hired; one qualified candidate comes per ten screening interviews — forty interviews for a single low-skill frontline worker, which caps hiring at about one a week. The fix was to stop one-on-one screening, interview in groups, screen only for crazies there and push everyone with a good work ethic and basic social skills to sales. Within six weeks hiring outpaced churn and by quarter end cold outreach sales had doubled to more than half of total sales.
  why: >-
    The issue was not the cold outreach method, skills or offer — there were simply not enough people doing cold outreach; to advertise more you need more workers.
  demonstrates: >-
    Finding the constraint and testing at it; employees as the way to do more of a core four activity.
  anchor: >-
    We get one qualified candidate per ten screening interviews, give or
  source: >-
    100m-leads.md, #2 Employees, lines 10684–10780
  confirmations: 1
  anchor_at: "100m-leads.md:10751"
  tier: 1
- id: C-leads-2-025
  type: case
  name: >-
    Buying the agency owner's time at $750 an hour
  statement: >-
    Unable to afford either agency, the author asked the second one to show him in a few hours how they would run ads on his account; the owner refused — my time's not for sale — then priced it at $750 an hour, with the first four hours paid up front, $3,000. The arrangement was one hour a week with homework between calls, every call recorded and rewatched: calls one and two the agency drove and he watched, calls three and four he drove, by five and six he understood how the decisions were made and what data was tracked, and by seven and eight he no longer needed help. Eight hours and $6000 bought a skill that made millions.
  why: >-
    Hiring an agency is investing in a skill you cannot learn anywhere else short of all the trial and error, and learning it from a pro is what made the difference.
  demonstrates: >-
    Using an agency to learn a platform or method rather than to outsource it; paying extra to have decisions explained.
  anchor: >-
    Can you just show me in a few hours how you would run ads on my
  source: >-
    100m-leads.md, #3 Agencies, lines 11444–11520 and 11856–11862
  confirmations: 2
  anchor_at: "100m-leads.md:11444"
  tier: 1
- id: C-leads-2-026
  type: case
  name: >-
    The opening the author uses with every agency
  statement: >-
    Every agency relationship is opened with a purpose and a deadline, in one speech: I want to do what you do but don't know how; work with me for six months so I can learn it; I'll pay extra for you to break down why you make the decisions you do and the steps you take; then I'll train my team, and once they can do it well enough we move to a lower cost consulting arrangement so you can still help if we run into problems — are you opposed to this?
  why: >-
    Most agencies are not opposed; if one is, move on, but be willing to negotiate, because at some price it is worth it for both parties.
  demonstrates: >-
    How to use agencies now: upfront intentions, a deadline, a planned move to consulting.
  anchor: >-
    I want to do what you do in my business, but I don't know how. I'd
  source: >-
    100m-leads.md, #3 Agencies, How I Use Agencies Now. And How You Can Too., lines 11688–11695
  confirmations: 1
  anchor_at: "100m-leads.md:11688"
  tier: 1
- id: C-leads-2-031
  type: case
  name: >-
    Five callouts at one affiliate target (spa owners)
  statement: >-
    The same potential affiliate is called out five ways: the business owners themselves (ATTENTION SPA OWNERS); their customers (Do you work with busy professionals who spend all day in meetings?); the result they promise (To the heroes who heal the stress of others...); the products and services they deliver (If you sell lotions or scented oils this is for you...); and your own customers (Do you know anyone who owns a spa?).
  why: >-
    The affiliate offer is advertised the same way as any other offer — call out the audience, show the value elements, call to action — with affiliates as the customer you are advertising to.
  demonstrates: >-
    Step 2: Make Them An Offer, the call out; callouts as labels, yes-questions and if-then statements applied to affiliates.
  anchor: >-
    The affiliate's customers - ]{.calibre3}[Do you work with busy
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 2: Make Them An Offer, lines 12310–12328
  confirmations: 1
  anchor_at: "100m-leads.md:12318"
  tier: 1
- id: C-leads-2-038
  type: case
  name: >-
    The same nutrition consult at all three integration levels
  statement: >-
    Strategy 1: gym affiliates give away a free nutrition consult to every new member, the gym markets the included consult and charges more, and the supplements are upsold at the consult. Strategy 2: the gym sells the same nutrition consult for $99 or $199 and keeps all the money — letting them keep it makes them send even more leads — and the products are upsold during the consult. Strategy 3: gyms are taught to hold nutrition consultations with white labeled products and upsell the supplements to their members directly, with the money split.
  why: >-
    Giving affiliates all the cash from a lead magnet you fulfil makes it all profit and no work for them; your money comes from selling the main thing for more than the lead magnet cost to deliver.
  demonstrates: >-
    Step 6: the three integration strategies — give the lead magnet away, sell the lead magnet, sell the core offer.
  anchor: >-
    We'd get gym affiliates to give away a free
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 6: Keep Them Advertising, lines 12815–12893
  confirmations: 1
  authors_caveat: >-
    After testing, the author's companies kept Strategy 1 twice a year as a big event and Strategy 3 ongoing; many similar portfolio businesses use Strategy 2 — I'm just sharing what worked for us.
  anchor_at: "100m-leads.md:12815"
  tier: 1
- id: C-leads-2-039
  type: case
  name: >-
    Service Business Case Study #1: National Tax Preparation Services
  statement: >-
    A $50M business preparing LLCs, bank accounts and articles of incorporation does not compete with Legalzoom; it partners with people who train new entrepreneurs and offers every affiliate's customer a free LLC setup — a high cost lead magnet. Launch: a big blast off seminar to the affiliates' audiences, where people take the free LLC. Integrate: once affiliates see the launch work, they build the free LLC into their own core offer, and the company's team then phones the customers the affiliates send for free and sells what they need next — bookkeeping, tax preparation. No money is spent on paid ads; the only advertising costs are delivering the lead magnet and a percentage of every first sale.
  demonstrates: >-
    Launch then integrate; a high cost lead magnet carried by affiliates; monetising on the back end.
  anchor: >-
    My friend\'s \$50M business prepares LLCs, bank accounts, and articles
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Three Case Studies You Can Model, lines 12938–12966
  confirmations: 2
  anchor_at: "100m-leads.md:12938"
  tier: 1
  merged_from: [C-leads-2-040]
- id: C-leads-2-041
  type: case
  name: >-
    Local Business Case Study #3: Chiropractors
  statement: >-
    Chiropractors go to high volume businesses whose people need adjustments — a gym. Launch: the gym owner promotes a three hour workshop on correct exercises and posture, free or at $29-$99 a head, and the money is split — give the gym 100% and they want to run it again, so thirty people at $99 makes the gym $2970 for a few emails and posts, while the chiropractor soft pitches at the workshop and collects patients. Integrate: long term the chiropractor gets one to two adjustments included with every new gym membership, which raises the value of the membership against the gym down the street and signals the gym cares about member safety, so every new member becomes a lead — repeated across thirty gyms.
  demonstrates: >-
    Launch then integrate for a local business; paying the affiliate all of the launch money to buy repetition.
  anchor: >-
    workshop where they show correct exercises and posture to get more from
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Three Case Studies You Can Model, lines 13011–13038
  confirmations: 1
  anchor_at: "100m-leads.md:13020"
  tier: 1
```


## D. Антипаттерны и границы — 6

```yaml
- id: D-leads-2-001
  type: antipattern
  name: >-
    Blaming the ad when the right people never saw it
  statement: >-
    Treating an unprofitable ad as a copy or creative failure, when most of the time the cause is that the right people never saw it.
  why: >-
    Paid ads go to colder, lower-trust audiences, so a smaller percentage of people respond; the way over that hurdle is putting the offer in front of more of the right people, which is what keeps ads efficient.
  anchor: >-
    in front of more people. And if an ad isn't profitable, most of the
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, lines 7071–7078
  confirmations: 1
  anchor_at: "100m-leads.md:7074"
  tier: 1
- id: D-leads-2-005
  type: rule
  name: >-
    The ad is not selling
  statement: >-
    The ad and its landing page do not sell the product; they ask whether the person is interested, and what they exchange for is contact information.
  why: >-
    A person who is interested gives you a way to tell them more, and at that moment becomes an engaged lead.
  not_to_confuse_with: >-
    Selling the offer inside the ad or on the landing page.
  anchor: >-
    [To be clear, we aren't selling anything. We are asking if they're
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, lines 7951–7954
  confirmations: 2
  anchor_at: "100m-leads.md:7951"
  tier: 1
  merged_from: [B-leads-2-017]
- id: D-leads-2-008
  type: antipattern
  name: >-
    Stopping at the loss instead of scaling the winner
  statement: >-
    Reading the total loss across a batch of tested ads as a failure and stopping, instead of finding the one winner in the batch and putting far more money behind it.
  why: >-
    In a batch of ten ads, nine can lose while one returns five to one; the aggregate still shows a loss, but the winner is there to be scaled by doubling, tripling, quadrupling, 10x-ing down on it. You might lose nine or ninety-nine times in a row before you win big.
  anchor: >-
    still down \$500. Many people stop here because they see a \$500 dollar
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8126–8140
  confirmations: 2
  anchor_at: "100m-leads.md:8128"
  tier: 1
- id: D-leads-2-014
  type: rule
  name: >-
    Costs can only approach zero
  statement: >-
    Pushing advertising efficiency past the point where cutting the cost of a customer by $100 takes more work than making an extra $100 from them.
  why: >-
    Costs can only approach zero while how much you make can go up to infinity, so efficiency beyond that point is like trying to save your way to a billion dollars - you feel like you are making progress and you are never going to get there.
  boundary: >-
    Once the cost of getting a customer is low enough, the work moves to the business model; there is a floor under CAC and no ceiling over LTGP.
  anchor: >-
    infinity. Increasing advertising efficiency beyond a certain point is
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8309–8316
  confirmations: 1
  anchor_at: "100m-leads.md:8314"
  tier: 1
- id: D-leads-2-024
  type: antipattern
  name: >-
    The Size Of The Pie Fallacy
  statement: >-
    Mistaking the tiny slice of the universe you advertise to - one core four activity, on one platform, in one way, to one targeted audience - for the entire available market.
  why: >-
    This is why most businesses stay small: when they plateau they believe there are no more leads to get, because saying "I'm as big as I can get" is much easier than saying "I'm not as good at advertising as I thought", and this false argument keeps entrepreneurs poorer than they should be.
  applies_when: >-
    The diagnostic in the chapter's opening: a $2M chiropractic business spending $30k a month on one platform, doing no content and no cold outreach, declaring a $15.1B industry saturated.
  anchor: >-
    universe they advertise to is the entire available market! This is why
  source: >-
    100m-leads.md, Core Four On Steroids: More Better New, lines 9093–9100
  confirmations: 6
  anchor_at: "100m-leads.md:9094"
  tier: 1
  merged_from: [C-leads-2-010, C-leads-2-011, E-leads-2-017]
- id: D-leads-2-037
  type: rule
  name: >-
    Customers only refer when the risk to the friendship is outweighed
  statement: >-
    A customer refers only when they think it very likely their friend will have a good experience - when the benefit to them personally outweighs the risk of hurting the relationship.
  why: >-
    Referring is always a risk for the customer: they stake their own goodwill with their friend in the hope of getting more of it by showing them something good.
  boundary: >-
    Incentives raise the benefit side, but the risk side is lowered only by goodwill - by showing you deliver on your promises.
  anchor: >-
    ]{.calibre3}[only]{.calibre24}[ refer when they think it's very likely
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, lines 10602–10616
  confirmations: 1
  anchor_at: "100m-leads.md:10606"
  tier: 1
```


## E. Глоссарий — 14

```yaml
- id: E-leads-2-003
  type: term
  name: >-
    Callout
  statement: >-
    A callout is whatever you do to get the attention of your audience, made specific enough to get the right people and broad enough to get as many of them as you can.
  definition: >-
    A callout is whatever you do to get the attention of your audience. Call outs go from hyperspecific - to get one person's attention - to not at all specific - to get everyone's attention.
  why: >-
    People noticing your ad is the most important part of the ad...by a lot; the callout is the first of the three core elements of every ad the author makes (callouts, value elements, calls to action).
  anchor: >-
    [A ]{.calibre3}[callout]{.calibre11}[ ]{.calibre3}[is whatever you do to
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, Step #3 Call Out, lines 7345–7355
  confirmations: 2
  anchor_at: "100m-leads.md:7345"
  tier: 1
- id: E-leads-2-007
  type: term
  name: >-
    Status
  statement: >-
    Status is what other humans give a person by how they treat them, so the value of your product is shown through the eyes of the people around the customer.
  definition: >-
    Humans are primarily status driven. And the status of one human comes from how the other humans treat them. So if your product or service changes how other people treat your customer, which it does in some way, it pays to show how.
  why: >-
    Talking about the value elements from someone else's perspective shows all the ways it'll improve the status of your customer and gives a ton of bonus benefits you'd miss if you only looked at it from their own perspective.
  anchor: >-
    [Who]{.calibre11}[: Humans are primarily status driven. And the status
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I: Making An Ad, The Who, lines 7664–7673
  confirmations: 3
  anchor_at: "100m-leads.md:7664"
  tier: 1
  merged_from: [C-leads-2-002]
- id: E-leads-2-009
  type: term
  name: >-
    Lifetime gross profit (LTGP)
  statement: >-
    Lifetime gross profit is all the money a customer ever spends with you minus all the money it takes to deliver it.
  definition: >-
    Lifetime gross profit is all the money a customer ever spends on your stuff minus all the money it takes to deliver it. For example, if a customer buys something for $15 and it costs $5 to deliver it, your gross profit is $10. So if that customer buys ten things over their lifetime, then they bought a total of $150 in stuff. But it cost you a total of $50 to deliver that stuff. That makes the lifetime gross profit $100.
  not_to_confuse_with: >-
    "Lifetime Value" or "LTV" - the author's heading is "I Measure LTGP Instead of 'Lifetime Value' or 'LTV'", because gross profit is the actual money you use to acquire customers, pay rent, cover payroll, and everything else to run your business.
  anchor: >-
    [Lifetime gross profit]{.calibre11}[ is all the money a customer ever
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, lines 8217–8233
  confirmations: 2
  anchor_at: "100m-leads.md:8221"
  tier: 1
- id: E-leads-2-010
  type: term
  name: >-
    LTGP to CAC
  statement: >-
    LTGP to CAC is the author's measure of advertising efficiency: the lifetime gross profit of a customer compared with the cost to acquire one.
  definition: >-
    I measure paid ad efficiency by comparing the lifetime gross profit of a customer (LTGP) with the cost to acquire a customer (CAC). I express this ratio as LTGP to CAC.
  why: >-
    So if LTGP is greater than CAC, you have profitable advertising. If it's lower than CAC, you're losing money. Every business the author invests in that struggles to scale has an LTGP to CAC ratio of less than 3 to 1, and takes off as soon as it goes above 3 to 1.
  anchor: >-
    (LTGP) with the cost to acquire a customer (CAC). I express this ratio
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, Cost & Returns, lines 8209–8253
  confirmations: 3
  authors_caveat: >-
    On the 3 to 1 threshold: This is a pattern I personally observed, not a rule.
  anchor_at: "100m-leads.md:8212"
  tier: 1
- id: E-leads-2-011
  type: term
  name: >-
    Client financed acquisition
  statement: >-
    Client financed acquisition is when the customer pays you more than it costs to get and fulfill them within the first thirty days, so the same cash can be recycled into the next customer.
  definition: >-
    But... if your customer spends more than it costs you to get and fulfill them--in the first 30 days--then you have the funds to scale now and forever. I call this client financed acquisition.
  why: >-
    I pick thirty days because any business can get interest free money for thirty days in the form of a credit card. And if we make more than the cost to get and fulfill the customer in the first thirty days, we square our balance. Money is no longer your bottleneck. This is the key to limitless scale.
  anchor: >-
    [But... if your customer spends more than it costs you to get
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, Client Financed Acquisition, lines 8337–8351
  confirmations: 3
  anchor_at: "100m-leads.md:8337"
  tier: 1
- id: E-leads-2-012
  type: term
  name: >-
    Sales problem (as opposed to an advertising problem)
  statement: >-
    If engaged leads have the problem you solve and the money to spend and still do not buy, that is a sales problem, not an advertising problem.
  definition: >-
    If your engaged leads have the problem you solve and the money to spend, and they're not buying, then your ads work fine--you have a sales problem. The diagnostic question is: Do my engaged leads have the problem I solve and the money to spend?
  not_to_confuse_with: >-
    An advertising problem: if the leads are not qualified, that's an advertising problem; if they are qualified and buying but there aren't enough of them, that's also an advertising problem.
  why: >-
    A company the author invested in spent twelve weeks and $150,000 on ads, blamed advertising, and gave up; confusing an advertising problem with a sales problem cost them an estimated ~$30M in enterprise value. Don't fire your sales guy if you've got advertising problems, and don't fire your advertising employees if you've got a sales problem.
  anchor: >-
    the problem you solve and the money to spend, and they're not
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II: Money Stuff, Personal Lessons from Paid Ads, lines 8463–8475
  confirmations: 3
  anchor_at: "100m-leads.md:8473"
  tier: 1
  merged_from: [C-leads-2-009]
- id: E-leads-2-015
  type: term
  name: >-
    The Rule of 100
  statement: >-
    The rule of 100 is doing 100 primary advertising actions, or 100 minutes of making content or ads, every day for one hundred days in a row.
  definition: >-
    The rule of 100 is simple. You advertise your stuff by doing 100 primary actions every day, for one hundred days in a row. Applied to the core four: 100 warm reach outs per day; 100 minutes per day making content, with at least one release per day; 100 cold reach outs per day; 100 minutes per day making paid ads and 100 days straight of running them.
  why: >-
    If you do 100 primary actions per day, and you do it for 100 days straight, you will get more engaged leads. Commit to the rule of 100 and you will never go hungry again.
  anchor: >-
    [The rule of 100 is simple. You advertise your stuff by doing 100
  source: >-
    100m-leads.md, Core Four On Steroids: More Better New, Here's how I do more: The Rule of 100, lines 8805–8885
  confirmations: 4
  anchor_at: "100m-leads.md:8810"
  tier: 1
  merged_from: [C-leads-2-045]
- id: E-leads-2-016
  type: term
  name: >-
    Constraints
  statement: >-
    Constraints are the steps where the most leads drop off, the points where the smallest improvement creates the biggest boost in results.
  definition: >-
    Every action a lead takes before they become a customer is a potential "drop-off" point. So I do the most testing at whatever step the most leads drop off. I call these "constraints." Constraints are the points where the smallest improvements create the biggest boost in results.
  applies_when: >-
    If you're not sure which step is the biggest constraint, find the step where the most leads drop off. You'll get the biggest reward for the smallest improvement.
  anchor: >-
    Constraints are the points where the smallest improvements create the
  source: >-
    100m-leads.md, Core Four On Steroids: More Better New, Better, lines 8924–8970
  confirmations: 3
  anchor_at: "100m-leads.md:8927"
  tier: 1
  merged_from: [C-leads-2-012]
- id: E-leads-2-024
  type: term
  name: >-
    Win
  statement: >-
    A win is any positive experience a customer has, and wins are made to feel faster by giving them more often rather than by delivering faster.
  definition: >-
    I define a "win" as any positive experience a customer has. Faster wins increase their perception of speed, increase the likelihood they'll stick, and increase how much they trust you. Triple win. To make wins feel faster, we give them wins more often.
  anchor: >-
    "win" as any positive experience a customer has. Faster wins
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, Decrease Time Delay, lines 10147–10160
  confirmations: 1
  anchor_at: "100m-leads.md:10148"
  tier: 1
- id: E-leads-2-025
  type: term
  name: >-
    BAMFAM
  statement: >-
    BAMFAM means Book-A-Meeting-From-A-Meeting: the customer always leaves knowing the next time they will hear from you.
  definition: >-
    They should always know the next time they'll hear from you. I got a slick saying from a public CEO friend of mine - BAMFAM: Book-A-Meeting-From-A-Meeting. Again, never leave a customer in no man's land. They should always know what happens...next.
  anchor: >-
    a slick saying from a public CEO friend of mine - BAMFAM:
  source: >-
    100m-leads.md, #1 Customer Referrals - Word of Mouth, Decrease Time Delay, lines 10181–10185 (the author credits a public CEO friend for the saying)
  confirmations: 4
  anchor_at: "100m-leads.md:10182"
  tier: 1
  merged_from: [C-playbooks-growth-014, E-closer-012, E-playbooks-growth-017]
- id: E-leads-2-034
  type: term
  name: >-
    Maximum allowable CAC
  statement: >-
    The maximum allowable CAC is the slice of gross profit you can hand over to get one customer while keeping your target LTGP to CAC ratio.
  definition: >-
    I suggest paying affiliates based on your maximum allowable cost to acquire a customer (CAC). Example: we sell a single-use product for $200 and it costs $40 to fulfill. This gives us $160 to pay the affiliate and run the business. If we want an LTGP:CAC ratio of 3:1 then three parts goes to the business - $120. And one part, $40, goes to the affiliate.
  anchor: >-
    [I suggest paying affiliates based on your maximum allowable cost to
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Step 4: Figure Out What To Pay Them, lines 12501–12512
  confirmations: 3
  anchor_at: "100m-leads.md:12501"
  tier: 1
  merged_from: [C-leads-2-034]
- id: E-leads-2-040
  type: term
  name: >-
    Affiliate LTGP to CAC
  statement: >-
    With affiliates the return compares what it costs to get an affiliate with the gross profit of all the customers that affiliate sends you.
  definition: >-
    So to calculate returns, we compare how much it costs us to get an affiliate with the gross profit of all the customers they send to our business.
  why: >-
    We spend money to get affiliates, but we don't really make much back from affiliates themselves; the money we spend to get an affiliate comes back from the customers they bring us.
  anchor: >-
    compare how much it costs us to get an affiliate with the gross profit
  source: >-
    100m-leads.md, #4 Affiliates and Partners, Costs and Returns, lines 13066–13138
  confirmations: 2
  anchor_at: "100m-leads.md:13074"
  tier: 1
  merged_from: [C-leads-2-042]
- id: E-leads-2-041
  type: term
  name: >-
    Super-affiliate
  statement: >-
    A super-affiliate is an affiliate who brings you other affiliates - the people who get you the people who get you customers.
  definition: >-
    With affiliates, you now have at least two layers of customers. Your customers, and the people who get you customers. And if you've got super-affiliates you add a third, the people who get you the people who get you customers! At ALAN, one super-affiliate added ten agencies per month, those agencies brought in about fifty local businesses per month, and those local businesses brought in about 2500 leads per month.
  anchor: >-
    super-affiliates you add a third, the people who get you the people who
  source: >-
    100m-leads.md, #4 Affiliates and Partners, lines 13170–13173 (with the ALAN example at lines 12154–12169)
  confirmations: 3
  anchor_at: "100m-leads.md:13172"
  tier: 1
  merged_from: [C-leads-2-029]
- id: E-leads-2-042
  type: term
  name: >-
    Open To Goal
  statement: >-
    Open to goal means working until you hit a set number of outcomes that day, no matter how long it takes.
  definition: >-
    A very successful gym chain allowed their sales managers to make their own schedules. But there was a catch--they had to sign up five new members per day no matter what. So if they did it by lunch, they could cut out early. But if it took 18 hours, so be it. They called this type of work schedule 'open-to-goal'.
  not_to_confuse_with: >-
    The rule of 100: You don't just commit to doing something a specific number of times... you commit to the work until you hit a specific number of outcomes--no matter what.
  why: >-
    It means you unlock a whole new level of effort you never even realized you had: give up the idea of 'doing your best' and instead do what is required.
  anchor: >-
    a specific number of times... you commit to the work until you hit a
  source: >-
    100m-leads.md, Advertising in Real Life: Open To Goal, lines 13780–13804
  confirmations: 3
  anchor_at: "100m-leads.md:13792"
  tier: 1
  merged_from: [C-leads-2-046]
```
