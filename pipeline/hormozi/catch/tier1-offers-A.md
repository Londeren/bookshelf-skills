# Улов фазы 1 — $100M Offers (2021) (ярус 1), тип A: фреймворки

Группа `tier1-offers`, слаг `offers`, ярус 1. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **40** (экстрактор вернул 40, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-offers.md` | 1–2973 | 6 | 40 |

## Как собран файл

Экстрактор A (Frameworks) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier1-offers.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier1-offers-A.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

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
  confirmations: 3
  authors_caveat: >-
    All four drivers are perceived ones: the offer becomes valuable only once the prospect perceives the increase in likelihood and the decrease in time delay and effort, so the drivers have to be communicated, not merely delivered.
  anchor_at: "100m-offers.md:31"
- id: A-offers-002
  type: framework
  name: >-
    The four prospect questions behind the value drivers
  statement: >-
    Each value driver answers one question the prospect is asking: What will I make? How will I know it's going to happen? How long will it take? What is expected of me?
  why: >-
    The extent to which these questions are answered in the mind of the prospect determines the value being created.
  applies_when: >-
    Checking whether an offer speaks to all four value drivers.
  structure:
    - >-
      What will I make? (Dream Outcome)
    - >-
      How will I know it's going to happen? (Perceived Likelihood of Achievement)
    - >-
      How long will it take? (Time Delay)
    - >-
      What is expected of me? (Effort & Sacrifice)
  anchor: >-
    If you noticed the questions in the last section that my father asked me, you’ll see they corresponded with these pillars:
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 38
  confirmations: 2
  anchor_at: "100m-offers.md:38"
- id: A-offers-003
  type: framework
  name: >-
    Long-term outcome and short-term experience
  statement: >-
    The time-delay driver splits in two: the long-term outcome the client buys, and the short-term experiences along the way that make them stay long enough to reach it.
  why: >-
    A big emotional win as close as possible to the purchase reinforces the buying decision, builds trust and gives the momentum to see the long-term goal through; people who experience a victory early on are more likely to continue.
  applies_when: >-
    Designing delivery so that value shows up early, not only at the end.
  structure:
    - >-
      Long-term outcome
    - >-
      Short-term experience
  anchor: >-
    There are two elements to this driver of value: Long-term outcome and short-term experience.
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 179
  confirmations: 1
  anchor_at: "100m-offers.md:179"
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
  confirmations: 1
  authors_caveat: >-
    Group selling is beyond the scope of this book; this sequence is stated for the 1-1 selling scenario.
  anchor_at: "100m-offers.md:295"
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
  confirmations: 1
  anchor_at: "100m-offers.md:303"
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
  confirmations: 1
  anchor_at: "100m-offers.md:351"
- id: A-offers-007
  type: framework
  name: >-
    Three habits that build a bonus vault
  statement: >-
    Build bonuses from three sources: create one-time assets that are easy to use, record every event you run, and pre-negotiate discounts and referral commissions with adjacent businesses.
  why: >-
    Anything you can invest in one time that clearly cost time or money to create, but can be given away endless times, is a perfect fit for a bonus; and you negotiate with the purchasing power of all your customers at once.
  applies_when: >-
    Stocking up bonus material to sprinkle into offers as needed.
  structure:
    - >-
      Create checklists, tools, swipe files, scripts, templates, and anything else that would take lots of time and effort to create on one’s own, but is easy to use once created
    - >-
      make a habit to record every workshop, every webinar, every event, every interview and use them as additional bonuses (as needed to crush a perceived obstacle)
    - >-
      Proactively negotiate group discounts and a referral commission with adjacent businesses that solve needs your customer will have
  anchor: >-
    1. Create checklists, tools, swipe files, scripts, templates, and anything else that would take lots of time and effort to create on one’s own, but is easy to use once created.
  source: >-
    100m-offers.md, ch. 14 Bonuses, lines 399–403
  confirmations: 1
  anchor_at: "100m-offers.md:401"
- id: A-offers-008
  type: framework
  name: >-
    Four ways of using urgency
  statement: >-
    Four ethical ways to put a deadline on a purchase: rolling cohorts, rolling seasonal promotions, pricing or bonus-based urgency, and an exploding opportunity.
  why: >-
    Deadlines drive decisions, and having them lets human beings push themselves over the edge so as not to miss out; on a week-long campaign the last 4 hours produce up to 50-60% of the sales.
  applies_when: >-
    Limiting when people can sign up rather than how many can, in a business that sells year round.
  structure:
    - >-
      1) Cohort-Based Rolling Urgency
    - >-
      2) Rolling Seasonal Urgency
    - >-
      3) Pricing or Bonus-Based Urgency
    - >-
      4) Exploding Opportunity
  anchor: >-
    I’m going to show you my four favorite ways of using urgency on a consistent basis, ethically: 1) Rolling Cohorts, 2) Rolling Seasonal Urgency, and 3) Promotional or Pricing Urgency 4) Exploding Opportunity.
  source: >-
    100m-offers.md, ch. 13 Urgency, lines 433–487
  confirmations: 1
  authors_caveat: >-
    Countdowns and dates must be real; if they aren’t, you’ll lose credibility and just look like every other wannabe marketer.
  anchor_at: "100m-offers.md:433"
- id: A-offers-009
  type: framework
  name: >-
    Three Types of Scarcity
  statement: >-
    Scarcity comes in three types: a limited supply of seats or slots, a limited supply of bonuses, and never available again.
  why: >-
    A fixed supply creates a fear of missing out and increases the need to take action, because fear of loss is stronger than desire for gain.
  applies_when: >-
    Limiting how many units or clients are available, as opposed to when they can buy.
  structure:
    - >-
      Limited Supply of Seats/Slots: in general or over X period of time.
    - >-
      Limited Supply of Bonuses
    - >-
      Never available again.
  anchor: >-
    1. Limited Supply of Seats/Slots: in general or over X period of time.
  source: >-
    100m-offers.md, ch. 12 Scarcity, lines 553–557
  confirmations: 1
  anchor_at: "100m-offers.md:555"
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
  confirmations: 1
  authors_caveat: >-
    Always have less spots available than you think you can sell, so that you sell out and can point to it next time.
  anchor_at: "100m-offers.md:573"
- id: A-offers-011
  type: framework
  name: >-
    Four types of guarantees
  statement: >-
    Guarantees come in four types: unconditional, conditional, anti-guarantee, and implied.
  why: >-
    Risk is the single greatest objection for any product or service, so reversing it is an immediate way to make any offer more attractive; changing the quality of a guarantee has been seen to 2-4x conversion.
  applies_when: >-
    Choosing how to reverse the risk in an offer.
  structure:
    - >-
      Unconditional
    - >-
      Conditional
    - >-
      Anti-Guarantee
    - >-
      Implied Guarantees.
  anchor: >-
    From an overarching perspective there are four types of guarantees:
  source: >-
    100m-offers.md, ch. 15 Guarantees, lines 631–690
  confirmations: 2
  authors_caveat: >-
    With a tremendous amount of cost associated with your product or service, you will likely want a conditional or an ANTI guarantee, as you will have to eat the cost of the refund AND the cost of fulfilling.
  anchor_at: "100m-offers.md:631"
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
  confirmations: 2
  anchor_at: "100m-offers.md:662"
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
  confirmations: 1
  anchor_at: "100m-offers.md:694"
- id: A-offers-014
  type: framework
  name: >-
    The guarantee catalog
  statement: >-
    A worked catalog of guarantees to pick from, each stated as what the client gets, running from unconditional refunds through eleven conditional forms to the anti-guarantee and implied performance deals.
  why: >-
    Reversing risk is the number one way to increase the conversion of an offer, and experienced marketers spend as much time crafting their guarantees as the deliverables themselves.
  applies_when: >-
    Choosing a specific guarantee for an offer rather than inventing one from scratch.
  structure:
    - >-
      [Unconditional] “No Questions Asked” Refund Guarantee
    - >-
      [Unconditional] Satisfaction-Based Refund Guarantee
    - >-
      [Conditional] Outsized Refund Guarantee
    - >-
      [Conditional] Service Guarantee
    - >-
      [Conditional] Modified Service Guarantee
    - >-
      [Conditional] Credit-based Guarantee
    - >-
      [Conditional] Personal Service Guarantee
    - >-
      [Conditional] Hotel + Airfare Perks Guarantee
    - >-
      [Conditional] Wage-Payment Guarantee
    - >-
      [Conditional] Release of Service Guarantee
    - >-
      [Conditional] Delayed Second Payment Guarantee
    - >-
      [Conditional] First Outcome Guarantee
    - >-
      [Anti-Guarantee] All Sales Are Final
    - >-
      Implied Guarantees: Performance Models, Revshares, and Profit-Sharing
  anchor: >-
    Let’s go through some different guarantee examples:
  source: >-
    100m-offers.md, ch. 15 Guarantees, lines 698–843
  confirmations: 1
  authors_caveat: >-
    Bigger broader guarantees work better with lower ticket B2C businesses; the higher the ticket, and the more business oriented it is, the more you want to steer towards specific guarantees.
  anchor_at: "100m-offers.md:698"
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
- id: A-offers-016
  type: framework
  name: >-
    Create Your Own Winning Guarantee
  statement: >-
    Build a guarantee by identifying the client's biggest fears, pain and perceived obstacles, asking what they do not want to happen if they pay you, and reversing those fears into the guarantee.
  why: >-
    The more specific and creative the guarantee is, the better; and it commits you to your customers' results and keeps you honest.
  applies_when: >-
    Writing a guarantee of your own instead of taking one from the catalog.
  structure:
    - >-
      identify a client’s biggest fears, pain, and perceived obstacles
    - >-
      What do they not want to have happen if they pay you? What are they most afraid of?
    - >-
      Reverse their fears into a guarantee
    - >-
      Think of the time, emotion, and outside costs associated with any program or service
  anchor: >-
    The key is to identify a client’s biggest fears, pain, and perceived obstacles.
  source: >-
    100m-offers.md, ch. 15 Guarantees, lines 845–853
  confirmations: 1
  authors_caveat: >-
    Guarantees are enhancers: they can enhance the attraction of any offer, but they cannot make a business, and used to cover a poor sales team or product they backfire into lots of refunds.
  anchor_at: "100m-offers.md:849"
- id: A-offers-017
  type: framework
  name: >-
    The Two Main Problems Most Entrepreneurs Face
  statement: >-
    However long the list of problems, they stem from two: not enough clients, and not enough cash.
  why: >-
    The two are linked: it costs more money and time to get more clients, and that money comes out of the profit margins, which creates the second problem.
  applies_when: >-
    Diagnosing what is actually wrong in a business before building an offer.
  structure:
    - >-
      Not enough clients
    - >-
      Not enough cash (excess profit at the end of the month)
  anchor: >-
    Although you *can* make the list of problems you face a mile long, which is a great way to stress yourself out, all these problems typically stem from two big kahunas:
  source: >-
    100m-offers.md, ch. 2 Grand Slam Offers, lines 977–980
  confirmations: 1
  anchor_at: "100m-offers.md:977"
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
  confirmations: 1
  authors_caveat: >-
    Your product must deliver: to charge big ticket prices you must outwork your self doubt and be so confident in your delivery, because you have done it so many times, that you know this person will succeed.
  anchor_at: "100m-offers.md:1166"
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
  confirmations: 1
  authors_caveat: >-
    This assumes a regular business who is not trying to gain mass market penetration for some other strategic advantage; and if you satisfy zero desire you will not make money and eventually leave people feeling rejected.
  anchor_at: "100m-offers.md:1522"
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
  confirmations: 2
  authors_caveat: >-
    Scarcity, urgency, bonuses and guarantees were not the only persuasion tools at play in the story that opens the section; these are the ones the author treats as belonging to the offer rather than to selling.
  anchor_at: "100m-offers.md:1565"
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
  confirmations: 3
  anchor_at: "100m-offers.md:1627"
- id: A-offers-022
  type: framework
  name: >-
    Health, Wealth, and Relationships
  statement: >-
    Three main markets always exist — health, wealth and relationships — and the task is to find a smaller subgroup inside one of them that is growing, has buying power and is easy to target.
  why: >-
    There is always tremendous pain when people lack these, so there is always demand for solutions to these core human pains.
  applies_when: >-
    Locating a niche to commit to.
  structure:
    - >-
      Health
    - >-
      Wealth
    - >-
      Relationships
  anchor: >-
    There are three main markets that will always exist: Health, Wealth, and Relationships. The reason that those will always exist is that there is always tremendous pain when you lack them.
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market -- A Starving Crowd, lines 1667–1671
  confirmations: 1
  anchor_at: "100m-offers.md:1667"
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
  confirmations: 1
  authors_caveat: >-
    The whole book sits atop the assumption of at least a normal market; in a bad market nothing that follows will work.
  anchor_at: "100m-offers.md:1679"
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
  confirmations: 2
  authors_caveat: >-
    Not all these components are mandatory: you will typically use three to five of them, they need not be in M-A-G-I-C order, and a quantifiable claim with a stated duration will not be approved on most platforms.
  anchor_at: "100m-offers.md:1991"
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
  confirmations: 1
  authors_caveat: >-
    Reaching an audience one time in no way means an offer is fatigued; and once you’ve monetized an offer, rarely should you change it.
  anchor_at: "100m-offers.md:2091"
- id: A-offers-026
  type: framework
  name: >-
    The three ways to grow
  statement: >-
    A business grows in only three ways: get more customers, increase their average purchase value, and get them to buy more times.
  why: >-
    Revenue caps at new clients per month multiplied by lifetime value, so growth has to come from selling more clients or from making each one worth more.
  applies_when: >-
    Working out where growth can come from at all.
  structure:
    - >-
      Get more customers
    - >-
      Increase their average purchase value
    - >-
      Get them to buy more times
  anchor: >-
    So, then,what does it take to grow? Thankfully, just three simple things:
  source: >-
    100m-offers.md, ch. 3 Pricing: The Commodity Problem, lines 2182–2186
  confirmations: 3
  authors_caveat: >-
    The author notes there are really only two ways to grow — get more customers and increase each customer’s value — and splits the second into two sub-buckets for this book.
  anchor_at: "100m-offers.md:2182"
- id: A-offers-027
  type: framework
  name: >-
    Grand Slam Offer
  statement: >-
    A Grand Slam Offer combines an attractive promotion, an unmatchable value proposition, a premium price, an unbeatable guarantee and a money model that gets you paid to acquire customers.
  why: >-
    It cannot be compared to any other product or service available, so it sells in a category of one and the purchasing decision is between your product and nothing; the result is increased response rates, increased conversion and premium prices.
  applies_when: >-
    Building the offer that a business goes to market with.
  structure:
    - >-
      an attractive promotion
    - >-
      an unmatchable value proposition
    - >-
      a premium price
    - >-
      an unbeatable guarantee
    - >-
      a money model (payment terms)
  anchor: >-
    combining an attractive promotion, an unmatchable value proposition, a premium price, and an unbeatable guarantee with a money model (payment terms)
  source: >-
    100m-offers.md, ch. 3 Pricing: The Commodity Problem, lines 2240–2246
  confirmations: 2
  anchor_at: "100m-offers.md:2240"
- id: A-offers-028
  type: framework
  name: >-
    Sales to Fulfillment Continuum
  statement: >-
    Ease of sales and ease of fulfilment sit on one continuum: doing less makes the offer harder to sell, doing as much as possible makes it easy to sell and hard to fulfil, and the goal is the sweet spot between them.
  why: >-
    If you cannot get demand flowing in, you have no idea whether what you have is good; cash flow from over-delivering is what pays for fixing operations afterwards.
  applies_when: >-
    Deciding how much to include in an offer, especially the first one.
  structure:
    - >-
      If you lower what you have to do, it increases how hard your product or service is to sell
    - >-
      If you do as much as possible, it makes your product or service easy to sell but hard to fulfill
    - >-
      The trick, and the ultimate goal, is to find a sweet spot where you sell something very well that’s also easy to fulfill
  anchor: >-
    Whenever you are building a business, you have a continuum between ease of fulfillment and ease of sales. If you lower what you have to do, it increases how hard your product or service is to sell.
  source: >-
    100m-offers.md, ch. 10 Value Offer: Creating Your Grand Slam Offer Part II: Trim & Stack, lines 2385–2411
  confirmations: 1
  authors_caveat: >-
    If this is your first Grand Slam Offer, it’s important to over-deliver like crazy.
  anchor_at: "100m-offers.md:2393"
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
  confirmations: 1
  anchor_at: "100m-offers.md:2395"
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
  confirmations: 1
  anchor_at: "100m-offers.md:2471"
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
  confirmations: 2
  authors_caveat: >-
    That doesn’t mean you never do something in a small group or one-on-one model; you want to save those high cost items for big value adds only.
  anchor_at: "100m-offers.md:2489"
- id: A-offers-033
  type: framework
  name: >-
    The value-equation test for what is high value
  statement: >-
    To judge whether an item is high value, ask whether the client will financially value it, believe it makes them likely to succeed, feel it takes much less effort and sacrifice, and see the result with far less time invested.
  why: >-
    These are the four value drivers applied as a screen, so that the trimming keeps what the prospect actually values rather than what is cheap to provide.
  applies_when: >-
    Trimming the list of possible deliverables in Step #5.
  structure:
    - >-
      Financially value
    - >-
      Cause them to believe they will be likely to succeed
    - >-
      Make them feel like they can do it with much less effort and sacrifice
    - >-
      Help them accomplish their goal and see the result they want with far less time investment.
  anchor: >-
    If you aren’t sure what’s high value, go through the value equation and ask yourself which of these things will this person:
  source: >-
    100m-offers.md, ch. 10 Value Offer: Creating Your Grand Slam Offer Part II: Trim & Stack, lines 2491–2496
  confirmations: 1
  anchor_at: "100m-offers.md:2491"
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
- id: A-offers-036
  type: framework
  name: >-
    The three core things the bundle does
  statement: >-
    A finished bundle must do three things: solve all the perceived problems, give you the conviction that what you sell is one of a kind, and make it impossible to compare your offering with anyone else's.
  why: >-
    Selling something unique means you are no longer bound by the normal pricing forces of commoditization, so prospects make a value-based rather than a price-based decision.
  applies_when: >-
    Checking the assembled offer before taking it to market.
  structure:
    - >-
      Solves all the perceived problems (not just some)
    - >-
      Gives you the conviction that what you’re selling is one of a kind (very important)
    - >-
      Makes it impossible to compare or confuse your business or offering with the one down the street
  anchor: >-
    *Can you see how much more valuable this is than a gym membership?* The bundle does three corethings:
  source: >-
    100m-offers.md, ch. 10 Value Offer: Creating Your Grand Slam Offer Part II: Trim & Stack, lines 2594–2598
  confirmations: 1
  anchor_at: "100m-offers.md:2594"
- id: A-offers-037
  type: framework
  name: >-
    Convergent & Divergent Thinking
  statement: >-
    Convergent problem solving takes known variables under unchanging conditions to a single answer; divergent thinking works with multiple known and unknown variables under dynamic conditions and many answers.
  why: >-
    School trains convergent thinking because it is easy to grade, but life pays for the divergent kind: many solutions to a single problem, of which one is far more right than the others.
  applies_when: >-
    Before generating the problems, solutions and delivery vehicles of an offer.
  structure:
    - >-
      Convergent: lots of variables, all known, with unchanging conditions and converge on a singular answer
    - >-
      Divergent: Multiple Variables, Known & Unknown, Dynamic Conditions, Multiple Answers
  anchor: >-
    Here’s what life presents us for divergent thinking: Multiple Variables, Known & Unknown, Dynamic Conditions, Multiple Answers.
  source: >-
    100m-offers.md, ch. 8 Value Offer: The Thought Process, lines 2650–2686
  confirmations: 1
  anchor_at: "100m-offers.md:2686"
- id: A-offers-038
  type: framework
  name: >-
    The Brick Exercise
  statement: >-
    Set a timer for 120 seconds and write as many different uses of a brick as you can; then re-run it asking how big the brick is, what it is made of and how it is shaped.
  why: >-
    Every offer has building blocks, and the exercise engages the divergent thinking needed to combine them; the three questions show you can find far more uses than you first wrote down.
  applies_when: >-
    Warming up before creating an offer, and as the cheat-code pattern for varying a product.
  structure:
    - >-
      set a timer on your phone for 120 seconds
    - >-
      Think of a brick
    - >-
      Write down as many different uses of a brick as you can possibly think of
    - >-
      How big is the brick?
    - >-
      What is the brick made of?
    - >-
      How is the brick shaped?
  anchor: >-
    Right now, I want you to set a timer on your phone for 120 seconds. What you need to do: Think of a brick.
  source: >-
    100m-offers.md, ch. 8 Value Offer: The Thought Process, lines 2694–2790
  confirmations: 1
  anchor_at: "100m-offers.md:2696"
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
  confirmations: 1
  authors_caveat: >-
    Don’t let these buckets, which are just meant to get your brain going, constrain you; if it’s easier, just list out everything you can possibly think of.
  anchor_at: "100m-offers.md:2898"
- id: A-offers-040
  type: framework
  name: >-
    Step #3: Solutions List
  statement: >-
    Turning problems into solutions has two steps: reverse each element of the obstacle into solution-oriented language, then name the solutions.
  why: >-
    It gives you a checklist of exactly what you are going to have to do for your prospects and what you are going to solve for them, before you work out how you will actually deliver it.
  applies_when: >-
    After the full list of problems has been written out.
  structure:
    - >-
      we are going to first transform our problems into solutions
    - >-
      Second, we are going to name these solutions
    - >-
      turn them into solutions by thinking, “What would I need to show someone to solve this problem?”
    - >-
      reverse each element of the obstacle into solution-oriented language
  anchor: >-
    Creating the solutions list has two steps. First, we are going to first transform our problems into solutions. Second, we are going to name these solutions.
  source: >-
    100m-offers.md, ch. 9 Value Offer: Creating Your Grand Slam Offer Part I: Problems & Solutions, lines 2915–2921
  confirmations: 1
  anchor_at: "100m-offers.md:2919"
```
