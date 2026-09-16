# Улов фазы 1 — $100M Money Models (2025) (ярус 1), тип A: фреймворки

Группа `tier1-money-models`, слаг `money-models`, ярус 1. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **33** (экстрактор вернул 33, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-money-models.md` | 1–6495 | 7 | 33 |

## Как собран файл

Экстрактор A (Frameworks) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier1-money-models.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier1-money-models-A.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 1 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: A-money-models-001
  type: framework
  name: >-
    The Four Types of Offers
  statement: >-
    A Money Model is assembled out of four offer types, each doing a different job: Attraction Offers, Upsell Offers, Downsell Offers and Continuity Offers.
  why: >-
    All improve the Money Model but they all do it differently; they work on their own, but together the author used all four in his most profitable businesses, because without an offer for getting customers you get fewer, with only one offer you leave money behind, downsells turn the remaining nos into yeses, and continuity guarantees the cash month after month.
  applies_when: >-
    Deciding what to offer and in what order, since a Money Model is a sequence of offers and different offers solve different problems.
  structure:
    - >-
      Attraction Offers turn strangers into customers.
    - >-
      Upsell Offers get people to spend more cash.
    - >-
      Downsell Offers get people to say yes when they would have said no.
    - >-
      Continuity Offers keep people buying.
  anchor: >-
    There are four types of offers: Attraction Offers, Upsell Offers,
  source: >-
    100m-money-models.md, The Four Types of Offers That Make Money Models, lines 877-891
  confirmations: 2
  authors_caveat: >-
    You can use one, two, multiples of one, or all four together, and any offer can be used on its own, at any time, in any order.
  anchor_at: "100m-money-models.md:879"
- id: A-money-models-002
  type: framework
  name: >-
    The catalog of fifteen Money Model offers
  statement: >-
    The book's plays are fifteen named offers, five Attraction, four Upsell, three Downsell and three Continuity, in this order.
  why: >-
    Each offer type does a different job in the sequence, so the catalog is organised by the four types and by the order the author builds them in.
  applies_when: >-
    Picking which named play to use at a given point of the money model.
  structure:
    - >-
      Attraction: Win Your Money Back
    - >-
      Attraction: Giveaways
    - >-
      Attraction: Decoy Offer
    - >-
      Attraction: Buy X Get Y Free
    - >-
      Attraction: Pay Less Now or Pay More Later
    - >-
      Upsell: The Classic Upsell
    - >-
      Upsell: Menu Upsell
    - >-
      Upsell: Anchor Upsell
    - >-
      Upsell: Rollover Upsell
    - >-
      Downsell: Payment Plan Downsells
    - >-
      Downsell: Trial With Penalty
    - >-
      Downsell: Feature Downsells
    - >-
      Continuity: Continuity Bonus Offers
    - >-
      Continuity: Continuity Discount Offers
    - >-
      Continuity: Waived Fee Offer
  anchor: >-
    So I made this "back of the napkin" list of what
  source: >-
    100m-money-models.md, Ten Years In Ten Minutes, lines 6155-6300
  confirmations: 2
  anchor_at: "100m-money-models.md:6158"
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
  confirmations: 2
  anchor_at: "100m-money-models.md:1269"
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
  confirmations: 1
  anchor_at: "100m-money-models.md:1688"
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
- id: A-money-models-008
  type: framework
  name: >-
    The four ways to advertise a discount
  statement: >-
    The same discount can be stated four ways — percentage off, absolute amount, free portion, or the total package — and which one converts best is worth testing.
  why: >-
    They all mean the same thing, but markets respond differently to the framing.
  applies_when: >-
    Wording a discount in an advertisement or a sales presentation.
  structure:
    - >-
      1) Percentage Off: 25% off
    - >-
      2) Absolute Amount: $300 off
    - >-
      3) Free Portion: 3 Months Free
    - >-
      4) The Total Package: One Year For $900 ($1,200)
  anchor: >-
    **You Can Advertise Discounts in Four Ways.** Let's say you had a
  source: >-
    100m-money-models.md, Decoy Offer, Important Notes, lines 1936-1949
  confirmations: 1
  anchor_at: "100m-money-models.md:1936"
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
  confirmations: 2
  authors_caveat: >-
    If more than 10% of pay-later people cancel their payment, you promised too much, the guarantee conditions are too low, or the price is too high.
  anchor_at: "100m-money-models.md:2450"
- id: A-money-models-010
  type: framework
  name: >-
    More, Better, New
  statement: >-
    Whatever you offer next is one of three things: more of what they just got, a better version of it, or something new and complementary.
  why: >-
    When an offer solves a problem another appears, and every offer therefore opens the door to an upsell; these three directions are the whole space of what that next offer can be.
  applies_when: >-
    Choosing what to upsell, and choosing what to roll credit over into.
  structure:
    - >-
      More of what they just got (think quantity).
    - >-
      Better versions of it (think quality).
    - >-
      New or complementary stuff (think different).
  anchor: >-
    ● *More* of what they just got (think quantity)---*Why have one burger
  source: >-
    100m-money-models.md, Section III: Upsell Offers, lines 2674-2683
  confirmations: 2
  anchor_at: "100m-money-models.md:2676"
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
- id: A-money-models-012
  type: framework
  name: >-
    Make Anything A/B Sellable
  statement: >-
    Anything can be turned into an A/B choice; the author's list of dimensions is quantity, start dates, payment preference, flavors, time slots, media, delivery speeds, sizes, colors, materials, personnel and communication.
  why: >-
    When you give people the option to not buy, some don't buy, so you give the option to pick between two similar things instead, and either choice results in an upsell.
  applies_when: >-
    Building the A/B step of a Menu Upsell.
  structure:
    - >-
      Quantity (do you want one bottle or two?)
    - >-
      Start dates (start tomorrow or Monday?)
    - >-
      Payment preference (cash or card?)
    - >-
      Flavors (chocolate or vanilla?)
    - >-
      Time slots (morning or afternoon?)
    - >-
      Media (read or listen?)
    - >-
      Delivery speeds (standard or overnight?)
    - >-
      Sizes (small or medium?)
    - >-
      Colors (black or white?)
    - >-
      Materials (paper or plastic?)
    - >-
      Personnel (John or Sara?)
    - >-
      Communication (call or text?)
  anchor: >-
    **Make Anything A/B Sellable.** You can turn *anything* into an A/B
  source: >-
    100m-money-models.md, Menu Upsell, Important Notes, lines 3204-3212
  confirmations: 1
  authors_caveat: >-
    If your customers have limited experience with your products or service, add a nudge to the A/B question.
  anchor_at: "100m-money-models.md:3204"
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
  confirmations: 2
  authors_caveat: >-
    If you treat the anchor like a fake, so will the customer; make a premium offer you actually want people to buy.
  anchor_at: "100m-money-models.md:3450"
- id: A-money-models-014
  type: framework
  name: >-
    Who, what, how of a Rollover Upsell
  statement: >-
    Once you know how much credit to give, a Rollover Upsell is three decisions: who to upsell, what to upsell, and how to roll the credit over.
  why: >-
    Crediting a customer's previous purchases toward the next offer gets far more people to take it, and the three decisions are what make the credited offer still profitable.
  applies_when: >-
    You want a customer to buy the next thing and they have already paid you (or somebody else) for something.
  structure:
    - >-
      For the who, I use Rollover Upsells in four situations.
    - >-
      For the what, you can upsell more of what they just got, something better, or something new and different; roll their credit over to something more expensive.
    - >-
      For the how, you can apply all or part of the discount up front or spread it over time.
  anchor: >-
    ● To do Rollover Upsells, figure out who to upsell, what to upsell, and
  source: >-
    100m-money-models.md, Rollover Upsell, Description and Summary Points, lines 3556-3704
  confirmations: 2
  authors_caveat: >-
    Price your next offer at least 4x higher than the credit, so applying the whole first purchase discounts 25% at most.
  anchor_at: "100m-money-models.md:3684"
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
- id: A-money-models-016
  type: framework
  name: >-
    The two ways to downsell
  statement: >-
    There are two ways to downsell: change how they pay, or change what they get.
  why: >-
    Downselling tweaks the original offer to find the highest value solution for the customer's budget, and those are the only two dials: the schedule of payment, or the contents of the offer.
  applies_when: >-
    Any offer you make after someone says no.
  structure:
    - >-
      For how they pay, I balance how much they pay now with how much they pay over time.
    - >-
      For what they get, I change quantity, quality, or offer something different.
  anchor: >-
    I downsell in two ways. I change how they pay or *what they get*. For
  source: >-
    100m-money-models.md, Section IV: Downsell Offers, lines 3745-3754
  confirmations: 2
  anchor_at: "100m-money-models.md:3751"
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
  confirmations: 1
  anchor_at: "100m-money-models.md:3756"
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
  confirmations: 2
  anchor_at: "100m-money-models.md:4126"
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
  confirmations: 2
  anchor_at: "100m-money-models.md:4374"
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
  confirmations: 2
  authors_caveat: >-
    If you remove stuff they hate and lower the price a lot, more people take the downsell; if you remove stuff they love and lower the price a little, more people take the original offer.
  anchor_at: "100m-money-models.md:4586"
- id: A-money-models-023
  type: framework
  name: >-
    The service quality features you can downsell
  statement: >-
    Service quality is changed along a fixed list of dimensions, and the same list also works to increase the quality of a service.
  why: >-
    The job is to make the product have the highest value-to-cost in the eyes of the customer, and having the dimensions listed ahead of time is what lets you standardize which feature combinations to present.
  applies_when: >-
    Building the feature combinations of a Feature Downsell (or of a premium version).
  structure:
    - >-
      Time Availability: Come specific times vs. whenever you want (days of week, times of day, amount of time)
    - >-
      Location Availability: This one location vs. all locations we own
    - >-
      Cancellations: Reschedule fees vs. free
    - >-
      Speed Of Response: Reply in minutes vs. hours vs. days etc.
    - >-
      Speed Of Delivery: Wait in line vs. priority, same day/next day vs. next week etc.
    - >-
      Service Ratio: One-on-one vs. one-to-many vs. many-to-one
    - >-
      Communication Method: Text Support vs. Chat Support vs. Video Call Support etc.
    - >-
      Provider Qualifications: Owner vs. long-time employee vs. new employee, etc.
    - >-
      Live vs. Recorded
    - >-
      In-Person vs. Remote
    - >-
      DIY, DWY, DFY. Do It Yourself vs. Done With You vs. Done For You
    - >-
      Expirations: Works forever vs. works for X time vs. works at specific times
    - >-
      Personalization: Generic vs. made just for you
    - >-
      Insurance/Guarantee: lengths of time, coverage, terms
  anchor: >-
    **Feature Downselling Service Quality.** This means a lot of things. I
  source: >-
    100m-money-models.md, Feature Downsells, Feature Downsell Examples, lines 4607-4640
  confirmations: 1
  anchor_at: "100m-money-models.md:4607"
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
  confirmations: 1
  authors_caveat: >-
    The first two elements are the author's own two-step description; the third is taken from the adjacent note "Temperature Check After Two Downsells (Like Payment Plans)" rather than from one numbered list.
  anchor_at: "100m-money-models.md:4701"
- id: A-money-models-025
  type: framework
  name: >-
    Bonus, discount, urgency in a Continuity Offer
  statement: >-
    More people start on continuity when you add good stuff (bonuses), take away bad stuff (discounts) and add urgency by making it conditional on joining now.
  why: >-
    Free stuff and discounts both affect how we make decisions, so the author does both to get the benefits of both; typically the bonus itself has more value than the first continuity payment.
  applies_when: >-
    Getting customers to start on a Continuity Offer.
  structure:
    - >-
      Bonus---adding value. For products, many small things or one big product that complements the subscription; for services, a defined program, onboarding, setup, or feature.
    - >-
      Discount---lowering costs. Anything you offer for free you can also offer as a discount.
    - >-
      A dash of urgency---if they join now.
  anchor: >-
    When making Continuity Offers, I get more people to *start* if I add
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Description and Summary Points, lines 4991-5219
  confirmations: 2
  anchor_at: "100m-money-models.md:5004"
- id: A-money-models-026
  type: framework
  name: >-
    Bonuses Work Kinda Like Upsells
  statement: >-
    A continuity bonus takes one of three shapes: more of the same, complementary, or an upgrade.
  why: >-
    The bonus must stay related to the core offer, otherwise it attracts the wrong customers.
  applies_when: >-
    Choosing what to give away as the bonus of a Continuity Offer.
  structure:
    - >-
      More of the same: you get two years of past newsletters free by becoming a member.
    - >-
      Complementary: you get nutrition services for free when you sign up for our fitness membership.
    - >-
      Upgrade: you get a free gold membership when you buy a bronze membership (limited availability).
  anchor: >-
    *More of the same:* You get two years of past newsletters free by
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, lines 5057-5062
  confirmations: 1
  anchor_at: "100m-money-models.md:5059"
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
  confirmations: 1
  authors_caveat: >-
    The exact numbers matter less than the principle; the author gives them as his own tested range.
  anchor_at: "100m-money-models.md:5142"
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
  confirmations: 2
  authors_caveat: >-
    Up Front works best in industries with a successful history of enforcing contracts; if you have historically high churn, skip it, and note that it gets customers but delays cash.
  anchor_at: "100m-money-models.md:5328"
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
  confirmations: 2
  authors_caveat: >-
    Pricing incentivizes sticking but can't and shouldn't overcome a terrible product; if more than 5% of people want to cancel early, look into it. If someone stays the entirety of their commitment, the fee officially goes away.
  anchor_at: "100m-money-models.md:5594"
- id: A-money-models-030
  type: framework
  name: >-
    The three stages of a $100M Money Model
  statement: >-
    A Money Model is built in three stages: Get Cash with Attraction Offers, Get More Cash with Upsell and Downsell Offers, Get The Most Cash with Continuity Offers.
  why: >-
    Money Model growth happens alongside the growth of the business; a bootstrapped business started from zero with a finished Money Model will collapse on top of you, and none of the author's businesses started with a fully forged one.
  applies_when: >-
    Deciding which part of the money model to work on next.
  structure:
    - >-
      Stage I: Get Cash---Attraction Offers get more customers for less
    - >-
      Stage II: Get More Cash---Upsell & Downsell Offers make more money from them faster
    - >-
      Stage III: Get The Most Cash---Continuity Offers maximize their total money spent
  anchor: >-
    Stage I: Get Cash---Attraction Offers get more customers for less
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, Description, lines 5827-5842
  confirmations: 2
  anchor_at: "100m-money-models.md:5829"
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
  confirmations: 2
  authors_caveat: >-
    Perfect one offer at a time: do not try and implement a full Money Model at once, it will break your business. Sometimes the best timing for Continuity Offers happens after the first thirty days, and that's OK.
  anchor_at: "100m-money-models.md:5968"
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
  confirmations: 2
  anchor_at: "100m-money-models.md:6166"
```
