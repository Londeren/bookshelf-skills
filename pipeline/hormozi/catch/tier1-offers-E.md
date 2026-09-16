# Улов фазы 1 — $100M Offers (2021) (ярус 1), тип E: глоссарий

Группа `tier1-offers`, слаг `offers`, ярус 1. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **38** (экстрактор вернул 38, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-offers.md` | 1–2973 | 6 | 38 |

## Как собран файл

Экстрактор E (Glossary) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier1-offers.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier1-offers-E.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

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
  confirmations: 2
  anchor_at: "100m-offers.md:21"
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
- id: E-offers-003
  type: term
  name: >-
    Status
  statement: >-
    Status is the perceived increase or decrease in a person's relative standing compared with others socially or professionally, and it is what decides which dream outcome a prospect values most.
  definition: >-
    the status (the perceived increase or decrease in relative standing when compared to others socially or professionally)
  why: >-
    In general the dream outcome that most directly increases a prospect's status will be the one they value most, so talking in terms of status is what makes prospects drool.
  not_to_confuse_with: >-
    Money or luxury: the Lamborghini example shows the same purchase can lower status inside one peer group while a minivan raises it, so it is not about the money.
  anchor: >-
    the *status (the perceived* *increase or decrease in relative standing when compared to others socially or professionally)*
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 149
  confirmations: 2
  anchor_at: "100m-offers.md:149"
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
  confirmations: 2
  anchor_at: "100m-offers.md:163"
- id: E-offers-005
  type: term
  name: >-
    Time Delay
  statement: >-
    Time delay is the time between a client buying and receiving the promised benefit; the shorter it is, the more valuable the product or service.
  definition: >-
    Time delay is the time between a client buying and receiving the promised benefit. The shorter the distance between when they purchase and they receive value/the outcome, the more valuable your services or product is.
  anchor: >-
    Time delay is the time between a client buying and receiving the promised benefit.
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 177
  confirmations: 2
  anchor_at: "100m-offers.md:177"
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
  confirmations: 2
  anchor_at: "100m-offers.md:662"
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
  confirmations: 1
  anchor_at: "100m-offers.md:682"
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
  confirmations: 2
  anchor_at: "100m-offers.md:686"
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
- id: E-offers-016
  type: term
  name: >-
    Offer
  statement: >-
    An offer is the goods and services agreed to be provided, the way payment is accepted, and the terms of the agreement; it is what initiates the trade of dollars for value.
  definition: >-
    In a nutshell, the offer is the goods and services you agree to give or provide, how you accept payment, and the terms of the agreement.
  why: >-
    It is the first thing any new customer interacts with and what attracts them, so it is the lifeblood of the business: no offer, no business.
  anchor: >-
    In a nutshell, the offer is the goods and services you agree to give or provide, how you accept payment, and the terms of the agreement.
  source: >-
    100m-offers.md, ch. 2 Grand Slam Offers, line 955
  confirmations: 2
  anchor_at: "100m-offers.md:955"
- id: E-offers-017
  type: term
  name: >-
    Value (worth-it-ness)
  statement: >-
    Value in this method is the worth-it-ness of an offer: what the buyer believes they get, as against the price they give.
  definition: >-
    how to create and communicate value, aka the worth-it-ness of an offer
  not_to_confuse_with: >-
    Price, quoted from Warren Buffet: price is what you pay, value is what you get.
  anchor: >-
    What I want to show you is how to create and communicate value, aka the “worth-it-ness” of an offer.
  source: >-
    100m-offers.md, ch. 5 Pricing: Charge What It’s Worth, line 1129
  confirmations: 1
  anchor_at: "100m-offers.md:1129"
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
- id: E-offers-019
  type: term
  name: >-
    Churn
  statement: >-
    Churn is the percentage of clients who leave each month.
  definition: >-
    Churn (% of clients who leave each month)
  anchor: >-
    *Churn (% of clients who leave each month):* From 10.7 percent to 6.8 percent
  source: >-
    100m-offers.md, ch. 5 Pricing: Charge What It’s Worth, line 1242
  confirmations: 1
  anchor_at: "100m-offers.md:1242"
- id: E-offers-020
  type: term
  name: >-
    The perfect profit combination
  statement: >-
    The perfect profit combination is lots of demand together with very little supply, or very little perceived supply.
  definition: >-
    The perfect profit combination is lots of demand, and very little supply, or perceived supply.
  why: >-
    Increasing demand lets you sell more units; decreasing supply lets you sell those units for more money, so enhancing the core offer is designed to do both at once.
  anchor: >-
    The “perfect profit combination” is lots of demand, and very little supply, or *perceived* supply.
  source: >-
    100m-offers.md, ch. 11 Enhancing The Offer, line 1522
  confirmations: 1
  anchor_at: "100m-offers.md:1522"
- id: E-offers-021
  type: term
  name: >-
    Desire
  statement: >-
    Desire comes from not getting what you want, so demand is raised by decreasing or delaying the satisfaction of a prospect's desire rather than by satisfying it.
  definition: >-
    Desire comes from not getting what you want. Quoted from Naval Ravikant: Desire is a contract you make with yourself to be unhappy until you get what you want.
  why: >-
    We only want things we do not have; as soon as we have them the desire disappears, so supply and the satisfaction of desire must be kept under the demand that can be generated.
  anchor: >-
    Desire comes from *not* getting what you want. In fact, I heard this quote that I love from Naval Ravikant: “Desire is a contract you make with yourself to be unhappy until you get what you want.”
  source: >-
    100m-offers.md, ch. 11 Enhancing The Offer, line 1530
  confirmations: 1
  anchor_at: "100m-offers.md:1530"
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
  confirmations: 3
  anchor_at: "100m-offers.md:1597"
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
  confirmations: 2
  anchor_at: "100m-offers.md:1697"
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
  confirmations: 2
  anchor_at: "100m-offers.md:1991"
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
- id: E-offers-030
  type: term
  name: >-
    Gross Profit
  statement: >-
    Gross profit is revenue minus the direct cost of servicing one additional customer.
  definition: >-
    Gross Profit: The revenue minus the direct cost of servicing an ADDITIONAL customer.
  not_to_confuse_with: >-
    Net profit, which is what is left over after all expenses are paid, not just the direct costs of fulfillment.
  anchor: >-
    The revenue minus the direct cost of servicing an ADDITIONALcustomer.
  source: >-
    100m-offers.md, ch. 3 Pricing: The Commodity Problem, line 2206
  confirmations: 1
  anchor_at: "100m-offers.md:2206"
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
  confirmations: 2
  anchor_at: "100m-offers.md:2208"
- id: E-offers-032
  type: term
  name: >-
    Value-driven versus price-driven purchase
  statement: >-
    A differentiated offer produces a value-driven purchase, where the product is sold on value; a commoditized one produces a price-driven purchase, a race to the bottom.
  definition: >-
    Commoditized = Price Driven Purchases (race to the bottom). Differentiated = Value Driven Purchases (sell in a category of one with no comparison).
  why: >-
    A business does the same work in both cases and the fulfillment is identical, but the Grand Slam Offer makes the business appear to have a totally different product, which recalibrates the prospect's value-meter.
  anchor: >-
    In other words, it allows you to sell your product based on VALUE not on PRICE.
  source: >-
    100m-offers.md, ch. 3 Pricing: The Commodity Problem, line 2224
  confirmations: 2
  anchor_at: "100m-offers.md:2224"
- id: E-offers-033
  type: term
  name: >-
    Commodity
  statement: >-
    A commodity, in this method, is a product available from many places, which makes it prone to purchases based on price instead of value.
  definition: >-
    A commodity, as I define it, is a product available from many places. For that reason, it's prone to purchases based on price instead of value.
  why: >-
    Commodities are valued at the point of market efficiency: competition drives the price down until margins are just enough to keep the lights on. If a prospect thinks these are pretty much the same, I'll buy the cheaper one, they commoditized you.
  anchor: >-
    A commodity, as I define it, is a product available from many places.
  source: >-
    100m-offers.md, ch. 3 Pricing: The Commodity Problem, line 2230
  confirmations: 2
  anchor_at: "100m-offers.md:2230"
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
  confirmations: 2
  anchor_at: "100m-offers.md:2240"
- id: E-offers-035
  type: term
  name: >-
    Money model
  statement: >-
    The money model is the payment terms of the offer, the part that makes it possible to get paid to acquire new customers and so removes the cash constraint on growth.
  definition: >-
    a money model (payment terms) that allows you to get paid to get new customers . . . forever removing the cash constraint on business growth
  anchor: >-
    with a money model (payment terms) that allows you to *get paid* to get new customers
  source: >-
    100m-offers.md, ch. 3 Pricing: The Commodity Problem, line 2240
  confirmations: 1
  anchor_at: "100m-offers.md:2240"
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
  confirmations: 2
  anchor_at: "100m-offers.md:2242"
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
- id: E-offers-038
  type: term
  name: >-
    Divergent thought process
  statement: >-
    A divergent thought process generates many solutions to a single problem under multiple known and unknown variables and dynamic conditions, with multiple right answers.
  definition: >-
    But life will pay you for your ability to solve using a divergent thought process. In other words, think of many solutions to a single problem. Here's what life presents us for divergent thinking: Multiple Variables, Known & Unknown, Dynamic Conditions, Multiple Answers.
  why: >-
    It is the mode needed to create the offer: listing every possible way to deliver a solution, as in the brick exercise, before trimming.
  not_to_confuse_with: >-
    Convergent problem solving, where lots of known variables under unchanging conditions converge on a single binary answer (think math), which is what school teaches because it is easy to grade.
  anchor: >-
    But life will pay you for your ability to solve using a divergent thought process. In other words, think of many solutions to a single problem.
  source: >-
    100m-offers.md, ch. 8 Value Offer: The Thought Process, line 2684
  confirmations: 2
  anchor_at: "100m-offers.md:2684"
```
