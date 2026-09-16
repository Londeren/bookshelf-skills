# Улов фазы 1 — $100M Offers (2021) (ярус 1), тип B: правила и критерии

Группа `tier1-offers`, слаг `offers`, ярус 1. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **111** (экстрактор вернул 111, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-offers.md` | 1–2973 | 6 | 111 |

## Как собран файл

Экстрактор B (Rules and criteria) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier1-offers.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier1-offers-B.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

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
  confirmations: 2
  anchor_at: "100m-offers.md:49"
- id: B-offers-002
  type: rule
  name: >-
    Perception is reality
  statement: >-
    Every increase in likelihood of achievement and every decrease in time delay and effort is communicated so the prospect perceives it, not merely delivered.
  why: >-
    An improvement the prospect has no idea about is not valuable in itself; the offer becomes valuable only once the prospect perceives the increase and the decreases.
  anchor: >-
    The Grand Slam Offer only becomes valuable once the prospect *perceives* the increase in likelihood of achievement, *perceives* the decrease in time delay, and *perceives* the decrease in effort and sacrifice.
  source: >-
    100m-offers.md, ch. 6 The Value Equation, line 61
  confirmations: 2
  anchor_at: "100m-offers.md:61"
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
  confirmations: 2
  anchor_at: "100m-offers.md:71"
- id: B-offers-004
  type: rule
  name: >-
    Depict the dream back to them
  statement: >-
    The offer states the prospect's dream outcome accurately enough that they feel understood, and then explains how the vehicle gets them there.
  why: >-
    The dream outcome is the gap between the prospect's current reality and their dreams; the goal is not to create desire but to channel it through the offer and the monetization vehicle.
  anchor: >-
    Our goal is to accurately depict that dream back to them, so they feel understood, and explain how our vehicle will get them there.
  source: >-
    100m-offers.md, ch. 6 The Value Equation, line 109
  confirmations: 1
  anchor_at: "100m-offers.md:109"
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
  confirmations: 2
  anchor_at: "100m-offers.md:149"
- id: B-offers-006
  type: rule
  name: >-
    Frame benefits in terms of status gained from the viewpoint of others
  statement: >-
    Copy describes how other people will perceive the prospect's achievement, not only the achievement itself.
  why: >-
    Connecting the dots to how others will react makes the same benefit that much more powerful.
  applies_when: >-
    Writing copy.
  anchor: >-
    When writing copy, you can make it that much more powerful by talking about how *other people* will perceive the prospect’s achievement. Connect the dots for them.
  source: >-
    100m-offers.md, ch. 6 The Value Equation, line 153
  confirmations: 1
  anchor_at: "100m-offers.md:153"
- id: B-offers-007
  type: rule
  name: >-
    Communicate perceived likelihood of achievement
  statement: >-
    Every offer carries explicit means of raising perceived likelihood of achievement through messaging, proof, what is included or excluded, and guarantees.
  why: >-
    People pay for certainty, and increasing a prospect's conviction that the offer will actually work for them makes it more valuable even though the work on your end is unchanged.
  anchor: >-
    So to increase value with all offers, we must communicate perceived likelihood of achievement through our messaging, proof, what we choose to include or exclude in our offer, and our guarantees (more on these later).
  source: >-
    100m-offers.md, ch. 6 The Value Equation, line 173
  confirmations: 1
  anchor_at: "100m-offers.md:173"
- id: B-offers-008
  type: rule
  name: >-
    Fast Wins
  statement: >-
    The offer builds in a short-term, immediate win for the client as close to the purchase as possible.
  why: >-
    The thing people buy is the long-term dream outcome, but the thing that makes them stay long enough to get it is the short-term experience; an early emotional win gives the buy-in and momentum to see it through, and people who experience a victory early are more likely to continue.
  anchor: >-
    Always try and incorporate short-term, immediate wins for a client.
  source: >-
    100m-offers.md, ch. 6 The Value Equation, line 187
  confirmations: 3
  anchor_at: "100m-offers.md:187"
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
- id: B-offers-010
  type: rule
  name: >-
    The Value Equation as the test of every offer element
  statement: >-
    Every element of an offer is kept only if it increases the dream outcome or the perceived likelihood of achievement, or decreases the time delay or the effort and sacrifice.
  why: >-
    Those four drivers are what creates or detracts from the value someone is willing to pay; if the bottom two reach zero the product is infinitely valuable.
  anchor: >-
    Our goal as marketers and business owners is to *increase* the value of the dream outcome and its perceived likelihood of achievement, while *decreasing* the time delay of achievement and the effort and sacrifice one has to put in to get there.
  source: >-
    100m-offers.md, ch. 6 The Value Equation, line 231
  confirmations: 3
  anchor_at: "100m-offers.md:231"
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
- id: B-offers-013
  type: rule
  name: >-
    Ask for the sale first, reveal the bonuses after
  statement: >-
    In a one-on-one sale the ask for the sale comes before any bonus is mentioned, and the bonuses are revealed only after they have signed up.
  why: >-
    Revealing them after the signature creates a wow experience and reinforces their decision to buy.
  applies_when: >-
    Selling one on one rather than to a group.
  anchor: >-
    When selling one on one, you ask for the sale *first,* before offering the bonuses.
  source: >-
    100m-offers.md, ch. 14 Bonuses, line 295
  confirmations: 1
  anchor_at: "100m-offers.md:295"
- id: B-offers-014
  type: rule
  name: >-
    Match the bonus to the stated obstacle, then ask again
  statement: >-
    After a no, a bonus that matches the prospect's perceived obstacle is added and the ask is repeated.
  why: >-
    People have a hard time rejecting reciprocity; agreeing, adding a bonus and asking whether that is fair enough makes them feel almost obligated to buy.
  applies_when: >-
    The person does not buy after the first ask in a one-on-one sale.
  anchor: >-
    if the person does *not* buy after the first ask, then you present a bonus that matches their perceived obstacle, then ask again
  source: >-
    100m-offers.md, ch. 14 Bonuses, line 297
  confirmations: 1
  anchor_at: "100m-offers.md:297"
- id: B-offers-015
  type: rule
  name: >-
    Name every bonus with a benefit in the title
  statement: >-
    Each bonus carries a special name that has a benefit in the title.
  anchor: >-
    Give them a special name that has a benefit in the title
  source: >-
    100m-offers.md, ch. 14 Bonuses, line 307
  confirmations: 2
  anchor_at: "100m-offers.md:307"
- id: B-offers-016
  type: rule
  name: >-
    Prove each bonus
  statement: >-
    Each bonus is presented with some proof, a stat, a past client or personal experience, that the thing is valuable.
  anchor: >-
    Provide some proof (this can be a stat, a past client, or personal experience) to prove that this thing is valuable
  source: >-
    100m-offers.md, ch. 14 Bonuses, line 321
  confirmations: 1
  anchor_at: "100m-offers.md:321"
- id: B-offers-017
  type: rule
  name: >-
    Price-tag every bonus
  statement: >-
    Every bonus is given a stated price tag and the price tag is justified.
  anchor: >-
    Always ascribe a price tag to them and justify it
  source: >-
    100m-offers.md, ch. 14 Bonuses, line 325
  confirmations: 1
  anchor_at: "100m-offers.md:325"
- id: B-offers-018
  type: rule
  name: >-
    Tools and checklists over additional trainings
  statement: >-
    When choosing what to add as a bonus, a tool or checklist is chosen over another training.
  why: >-
    The effort and time are lower with a tool or checklist, so the value is higher; the value equation still reigns supreme.
  anchor: >-
    Tools & checklists are better than additional trainings (as the effort & time are lower with the former, so the value is higher.
  source: >-
    100m-offers.md, ch. 14 Bonuses, line 327
  confirmations: 2
  anchor_at: "100m-offers.md:327"
- id: B-offers-019
  type: rule
  name: >-
    One bonus per obstacle
  statement: >-
    Each bonus addresses a specific concern or obstacle in the prospect's mind about why they cannot or will not be successful, and proves that belief incorrect.
  why: >-
    A bonus can also be what they would logically realize they need next, solving their next problem before they encounter it.
  anchor: >-
    They should each address a specific concern/obstacle in the prospects mind about why they can’t or won’t be successful (bonus should prove their belief incorrect)
  source: >-
    100m-offers.md, ch. 14 Bonuses, line 329
  confirmations: 1
  anchor_at: "100m-offers.md:329"
- id: B-offers-020
  type: rule
  name: >-
    Bonus value eclipses the core offer
  statement: >-
    The stated value of the bonuses adds up to more than the value of the core offer.
  why: >-
    Adding offers keeps expanding the price-to-value discrepancy and subconsciously communicates that the core offer must be even more valuable than the bonuses.
  anchor: >-
    The value of the bonuses should eclipse the value of the core offer.
  source: >-
    100m-offers.md, ch. 14 Bonuses, line 333
  confirmations: 1
  anchor_at: "100m-offers.md:333"
- id: B-offers-021
  type: rule
  name: >-
    Put scarcity and urgency on the bonuses themselves
  statement: >-
    Scarcity or urgency is attached to the bonuses, not only to the core offer.
  why: >-
    It takes the bonus technique and puts it on steroids; a bonus with scarcity is unavailable anywhere else, a bonus with urgency is lost if they do not buy today.
  anchor: >-
    You can further enhance the value of your bonuses by adding scarcity and urgency to the bonus themselves (which takes this technique and puts it on steroids).
  source: >-
    100m-offers.md, ch. 14 Bonuses, line 335
  confirmations: 1
  anchor_at: "100m-offers.md:335"
- id: B-offers-022
  type: rule
  name: >-
    Advanced Level Bonuses - Other People's Products and Services
  statement: >-
    Bonuses are sourced from other businesses' products and services in exchange for free exposure to your customers, and those businesses are not direct competitors.
  why: >-
    It is free marketing for them and high value products for you at no cost; with enough of these relationships the savings and true-to-price bonuses can justify your entire price, and a group discount plus a commission to yourself can turn each one into a revenue stream.
  anchor: >-
    You can get other businesses to give you their services and products as a part of your bonuses in exchange for exposure to your clients for free.
  source: >-
    100m-offers.md, ch. 14 Bonuses, line 351
  confirmations: 2
  anchor_at: "100m-offers.md:351"
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
  confirmations: 1
  anchor_at: "100m-offers.md:409"
- id: B-offers-024
  type: rule
  name: >-
    Deadlines must be real
  statement: >-
    Every sign-up countdown and promotion end date published is a real one.
  why: >-
    If the dates are not real you lose credibility and just look like every other wannabe marketer.
  applies_when: >-
    Running date countdowns in a digital setting.
  anchor: >-
    But make sure they are real. If they aren’t, you’ll lose credibility and just look *like every other wannabe marketer*.
  source: >-
    100m-offers.md, ch. 13 Urgency, line 459
  confirmations: 1
  anchor_at: "100m-offers.md:459"
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
  confirmations: 1
  anchor_at: "100m-offers.md:477"
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
  confirmations: 1
  anchor_at: "100m-offers.md:479"
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
- id: B-offers-029
  type: rule
  name: >-
    Every offer carries a deadline
  statement: >-
    Every promotion carries a deadline and at least one of the four forms of urgency.
  why: >-
    Adding a deadline and one or multiple forms of urgency gets more people to take action than would otherwise; the biggest sales on a week-long campaign happen in the last four hours of the last day.
  anchor: >-
    Adding a deadline and incorporating one or multiple forms of urgency will get more people to take action than would otherwise.
  source: >-
    100m-offers.md, ch. 13 Urgency, line 491
  confirmations: 1
  anchor_at: "100m-offers.md:491"
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
  confirmations: 3
  anchor_at: "100m-offers.md:563"
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
  confirmations: 1
  anchor_at: "100m-offers.md:585"
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
  confirmations: 1
  authors_caveat: >-
    As groups become much bigger the tactic loses some teeth, which the author says from experience.
  anchor_at: "100m-offers.md:611"
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
  confirmations: 2
  anchor_at: "100m-offers.md:650"
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
  confirmations: 2
  anchor_at: "100m-offers.md:656"
- id: B-offers-041
  type: rule
  name: >-
    If you do not get X result in Y time period, we will Z
  statement: >-
    Every guarantee is written as a conditional statement naming the result, the time period and what you will do if it is not reached.
  why: >-
    Without the or-what portion the guarantee sounds weak and diluted, which is what most marketers do; the teeth come from deciding what you will do if they do not get the result.
  anchor: >-
    What makes a guarantee have power is a conditional statement: If you do not get X result in Y time period, we will Z.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 662
  confirmations: 2
  anchor_at: "100m-offers.md:662"
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
  confirmations: 3
  anchor_at: "100m-offers.md:682"
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
- id: B-offers-045
  type: rule
  name: >-
    Performance deals need measurement and collection
  statement: >-
    A performance, revshare or profit-share structure is used only where the outcome can be measured transparently and payment can be trusted or controlled.
  why: >-
    The drawbacks of implied guarantees are tracking and collection; these offers work well when you have quantifiable outcomes.
  anchor: >-
    These only work in situations where you have transparency for measuring the outcome and trust (or control) that you will get compensated when you do perform.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 690
  confirmations: 2
  anchor_at: "100m-offers.md:690"
- id: B-offers-046
  type: rule
  name: >-
    Stacking Guarantees
  statement: >-
    Guarantees can be stacked, combining an unconditional with a conditional one or two conditional ones around different or sequential outcomes.
  why: >-
    Stacking around sequential outcomes future paces the prospect into an outcome they now believe is far more likely and shifts the burden of risk from them onto you.
  anchor: >-
    An experienced salesman understands that, like bonuses, you can actually *stack* guarantees.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 694
  confirmations: 1
  anchor_at: "100m-offers.md:694"
- id: B-offers-047
  type: rule
  name: >-
    Few conditions on an unconditional guarantee
  statement: >-
    Conditions are kept off an unconditional guarantee, because each one added weakens it.
  why: >-
    The more conditions you add, the faster this guarantee loses its teeth.
  anchor: >-
    You can add conditions, but the more conditions you add, the faster this guarantee loses its teeth.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 708
  confirmations: 1
  anchor_at: "100m-offers.md:708"
- id: B-offers-048
  type: rule
  name: >-
    Name Your Guarantee Something Cool
  statement: >-
    The guarantee is given a vivid name instead of the words satisfaction or money back.
  why: >-
    Generic wording such as a 30 Day Money Back Satisfaction Guarantee is bad; creative imagery makes the same guarantee memorable.
  anchor: >-
    If you are going to give a guarantee, spice it up. Instead of using “satisfaction” or some other “vanilla” word, describe it more strongly.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 716
  confirmations: 1
  anchor_at: "100m-offers.md:716"
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
  confirmations: 1
  anchor_at: "100m-offers.md:732"
- id: B-offers-050
  type: rule
  name: >-
    Unconditional vs Conditional Based on Business Type
  statement: >-
    The higher the ticket and the more business-oriented the buyer, the more specific and conditional the guarantee.
  why: >-
    Bigger broader guarantees work better with lower ticket B2C businesses because many people just will not bother taking the time.
  anchor: >-
    The higher the ticket, and the more business oriented it is, the more you want to steer towards specific guarantees.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 736
  confirmations: 1
  anchor_at: "100m-offers.md:736"
- id: B-offers-051
  type: rule
  name: >-
    Personal service guarantees carry conditions
  statement: >-
    A guarantee of one-on-one work until the result is reached is written with conditions on the client's own behaviour, such as responding within twenty-four hours and using the products you tell them to.
  why: >-
    It is one of the strongest guarantees in existence, a service guarantee on crack, and without contingencies making failure unlikely it would be a nightmare to honour at scale.
  anchor: >-
    You will *definitely* want to add conditions, though: they must respond back in twenty-four hours, they must use the products you tell them to, they must XYZ.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 775
  confirmations: 1
  anchor_at: "100m-offers.md:775"
- id: B-offers-052
  type: rule
  name: >-
    Create Your Own Winning Guarantee
  statement: >-
    A new guarantee is built by identifying the client's biggest fears, pain and perceived obstacles and reversing them, and is as specific and creative as possible.
  why: >-
    Reversing risk is the number one way to increase the conversion of an offer, and experienced marketers spend as much time crafting their guarantees as the deliverables themselves.
  anchor: >-
    The key is to identify a client’s biggest fears, pain, and perceived obstacles.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 849
  confirmations: 2
  anchor_at: "100m-offers.md:849"
- id: B-offers-053
  type: rule
  name: >-
    A guarantee never covers a weak product
  statement: >-
    A guarantee is not used to compensate for a poor product or a poor sales team.
  why: >-
    Guarantees are enhancers; they can enhance the attraction of any offer but cannot make a business, and used as cover they backfire into lots of refunds.
  anchor: >-
    If a guarantee is used to cover up a poor sales team or a poor product, it will backfire into lots of refunds.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 851
  confirmations: 1
  anchor_at: "100m-offers.md:851"
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
  confirmations: 2
  anchor_at: "100m-offers.md:1139"
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
  confirmations: 1
  anchor_at: "100m-offers.md:1139"
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
  confirmations: 2
  anchor_at: "100m-offers.md:1141"
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
  confirmations: 2
  anchor_at: "100m-offers.md:1210"
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
- id: B-offers-061
  type: rule
  name: >-
    Outwork your self doubt before charging big ticket
  statement: >-
    Big ticket prices are asked only once you have delivered the result enough times to know this person will succeed.
  why: >-
    Experience is what gives the conviction to ask for someone's entire year's salary as payment, and your product must deliver; wishing to shortcut the real work makes you fail.
  anchor: >-
    You must be so confident in your delivery, because you have done it *so many times,* that you *know* that this person will succeed.
  source: >-
    100m-offers.md, ch. 5 Charge What It's Worth, line 1216
  confirmations: 1
  anchor_at: "100m-offers.md:1216"
- id: B-offers-062
  type: rule
  name: >-
    Charge a premium
  statement: >-
    The business charges a premium price rather than a market or below-market one.
  why: >-
    A premium lets you do things no one else can to make clients successful; lowering price decreases emotional investment, perceived value and results, attracts the worst clients and destroys the margin needed to provide an exceptional experience.
  anchor: >-
    First and foremost, charge a premium. It will allow you to do things no one else can to make your clients successful.
  source: >-
    100m-offers.md, ch. 5 Charge What It's Worth, line 1254
  confirmations: 3
  anchor_at: "100m-offers.md:1254"
- id: B-offers-063
  type: rule
  name: >-
    Keep supply under the demand you can generate
  statement: >-
    Fewer units are sold than the business is able to sell, so that supply and satisfied desire stay under generated demand.
  why: >-
    Desire comes from not getting what you want, so demand rises only if satisfying it is delayed; demand for services is fractal, one fifth of prospects will pay five times the price, and satisfying all the demand kills the golden goose.
  anchor: >-
    We must endeavor to keep our supply (and satisfaction of desire) under the demand that we are able to generate.
  source: >-
    100m-offers.md, ch. 11 Enhancing The Offer, line 1555
  confirmations: 2
  authors_caveat: >-
    This assumes a regular business who is not trying to gain mass market penetration for some other strategic advantage (line 1528).
  anchor_at: "100m-offers.md:1555"
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
- id: B-offers-065
  type: rule
  name: >-
    Serve the people who can pay you what you are worth
  statement: >-
    The market is chosen for its ability to pay, not for attachment to the audience.
  why: >-
    There is a market in desperate need of your abilities, and picking a market is always a choice.
  anchor: >-
    Don’t be romantic about your audience. Serve the people who can pay you what you’re worth.
  source: >-
    100m-offers.md, ch. 4 Finding The Right Market, line 1619
  confirmations: 1
  anchor_at: "100m-offers.md:1619"
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
  confirmations: 2
  anchor_at: "100m-offers.md:1621"
- id: B-offers-067
  type: rule
  name: >-
    Normal market
  statement: >-
    The market you sell into grows at least at the rate of the marketplace and has common unmet needs in health, wealth or relationships.
  why: >-
    The whole book sits atop the assumption of at least a normal market; the three main markets always exist because there is always tremendous pain when you lack them, and in a dying market nothing in the book would have worked.
  anchor: >-
    a market that is growing at the same rate as the marketplace and that has common unmet needs that fall into one of three categories: improved health, increased wealth, or improved relationships
  source: >-
    100m-offers.md, ch. 4 Finding The Right Market, line 1621
  confirmations: 2
  anchor_at: "100m-offers.md:1621"
- id: B-offers-068
  type: rule
  name: >-
    Massive Pain
  statement: >-
    The chosen market does not merely want the offer, it desperately needs it.
  why: >-
    The degree of the pain is proportional to the price you will be able to charge; a prospect must have a painful problem for us to solve and charge money for our solution.
  anchor: >-
    They must not want, but desperately need, what I am offering.
  source: >-
    100m-offers.md, ch. 4 Finding The Right Market, line 1633
  confirmations: 3
  anchor_at: "100m-offers.md:1633"
- id: B-offers-069
  type: rule
  name: >-
    The pain is the pitch
  statement: >-
    The pitch articulates the pain the prospect is feeling rather than describing the product.
  why: >-
    If you can articulate the pain a prospect is feeling accurately, they will almost always buy what you are offering.
  anchor: >-
    If you can articulate the pain a prospect is feeling accurately, they will almost always buy what you are offering.
  source: >-
    100m-offers.md, ch. 4 Finding The Right Market, line 1637
  confirmations: 1
  anchor_at: "100m-offers.md:1637"
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
  confirmations: 1
  anchor_at: "100m-offers.md:1643"
- id: B-offers-071
  type: rule
  name: >-
    Purchasing Power
  statement: >-
    The targets have the money, or access to the money, needed to buy at the prices you require.
  why: >-
    A market can be in massive pain, be easy to target and keep adding people, and still not pay, as with a resume service sold to the unemployed.
  anchor: >-
    Make sure your targets have the money, or access to the amount of money, needed to buy your services at the prices you require to make it worth your time.
  source: >-
    100m-offers.md, ch. 4 Finding The Right Market, line 1651
  confirmations: 2
  anchor_at: "100m-offers.md:1651"
- id: B-offers-072
  type: rule
  name: >-
    Easy to Target
  statement: >-
    The chosen avatar is gathered somewhere reachable: associations, mailing lists, social media groups or channels they all watch.
  why: >-
    If searching them out is like finding needles in a haystack it is very difficult to get your offer in front of interested eyes, and your promotions must be served to the right audience however good the offer is.
  anchor: >-
    Main point: you want to make sure you can target your ideal audience easily.
  source: >-
    100m-offers.md, ch. 4 Finding The Right Market, line 1657
  confirmations: 2
  anchor_at: "100m-offers.md:1657"
- id: B-offers-073
  type: rule
  name: >-
    Growing
  statement: >-
    A shrinking market is rejected and a growing one chosen.
  why: >-
    Growing markets are a tailwind and declining markets a headwind; newspapers had pain, purchasing power and easy targeting but the shrinking marketplace fought every effort.
  anchor: >-
    Business is hard enough, and markets move quickly. So you might as well find a good market to give you a tailwind to make the process easier.
  source: >-
    100m-offers.md, ch. 4 Finding The Right Market, line 1661
  confirmations: 2
  anchor_at: "100m-offers.md:1661"
- id: B-offers-074
  type: rule
  name: >-
    Starving Crowd > Offer Strength > Persuasion Skills
  statement: >-
    When results are poor, the market is fixed before the offer and the offer before persuasion skills.
  why: >-
    A great rating on a higher-order piece overpowers anything lower on the priority scale, and a bad one stops the equation unless a great higher-priority component nullifies it; a Grand Slam Offer given to the wrong audience falls on deaf ears.
  anchor: >-
    A “great” rating on a higher-order piece overpowers anything else lower on the priority scale.
  source: >-
    100m-offers.md, ch. 4 Finding The Right Market, line 1681
  confirmations: 2
  anchor_at: "100m-offers.md:1681"
- id: B-offers-075
  type: rule
  name: >-
    Commit to the Niche
  statement: >-
    One market is picked and kept long enough for trial and error rather than swapped after a failed offer.
  why: >-
    All markets have unpleasant characteristics and the grass is never greener; hopping from niche to niche means starting over from the beginning each time, and both abandoned markets are usually normal markets worth billions.
  anchor: >-
    You must stick with whatever you pick long enough to have trial and error.
  source: >-
    100m-offers.md, ch. 4 Finding The Right Market, line 1699
  confirmations: 3
  anchor_at: "100m-offers.md:1699"
- id: B-offers-076
  type: rule
  name: >-
    Under $10M per year, niche down
  statement: >-
    A business under $10M per year narrows its audience rather than broadening it.
  why: >-
    For 99.6 percent of readers below $10M a year it is almost always easier to serve fewer clients more narrowly, and many companies passed $30M a year serving a single niche.
  anchor: >-
    For most, if you are under $10M per year, niching down will make you more money.
  source: >-
    100m-offers.md, ch. 4 Finding The Right Market, line 1709
  confirmations: 2
  authors_caveat: >-
    Above that it depends on the size of the TAM, and going beyond it may require broadening up market, down market or into an adjacent market.
  anchor_at: "100m-offers.md:1709"
- id: B-offers-077
  type: rule
  name: >-
    Be the one who solves this problem for this person
  statement: >-
    The positioning names one type of person and one type of problem rather than a broad category of customers.
  why: >-
    The same product can be sold for up to 100x more as it is niched down, because the sales messaging speaks to that avatar and they get more value from it in a real way.
  anchor: >-
    You want to be ‘the guy’ who services ‘this type of person’ or solves ‘this type of problem.’
  source: >-
    100m-offers.md, ch. 4 Finding The Right Market, line 1741
  confirmations: 2
  anchor_at: "100m-offers.md:1741"
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
  confirmations: 3
  authors_caveat: >-
    Reaching an audience one time in no way means an offer is fatigued; most people do not even notice an offer on the first mention (line 1969).
  anchor_at: "100m-offers.md:1971"
- id: B-offers-079
  type: rule
  name: >-
    Three to five M-A-G-I-C components
  statement: >-
    A name uses three to five of the naming components, not all of them and not one.
  why: >-
    If you can fit them all in it is likely the name will become too long; three to five typically creates something more unique and desirable.
  anchor: >-
    You will typically use three to five of them in naming a program or service.
  source: >-
    100m-offers.md, ch. 16 Naming, line 1981
  confirmations: 2
  anchor_at: "100m-offers.md:1981"
- id: B-offers-080
  type: rule
  name: >-
    Brevity against specificity
  statement: >-
    A name is kept as short and punchy as it can be while staying specific.
  anchor: >-
    The shorter and punchier the better. So it's a balance between brevity and specificity.
  source: >-
    100m-offers.md, ch. 16 Naming, line 1983
  confirmations: 1
  anchor_at: "100m-offers.md:1983"
- id: B-offers-081
  type: rule
  name: >-
    Test names against a control
  statement: >-
    Two to three candidate names are run in the advertising campaign, the winner is noted and then used as the control that new names are tested against.
  why: >-
    The only way to really know what works is to write the names out and test them; some offers convert better than others and there is no telling in advance why a name takes off.
  anchor: >-
    you can use two to three of your best names in your advertising campaign. Quickly note the winner, then use that as a control to test against with new names.
  source: >-
    100m-offers.md, ch. 16 Naming, line 2083
  confirmations: 2
  anchor_at: "100m-offers.md:2083"
- id: B-offers-082
  type: rule
  name: >-
    Any reason why, as long as you believe it
  statement: >-
    The name opens with a reason why the promotion is being run, and any reason will do as long as you believe it.
  why: >-
    It should answer why they are making this great offer, or why the prospect should respond and what is in it for them.
  anchor: >-
    It really doesn't matter so long as you believe it.
  source: >-
    100m-offers.md, ch. 16 Naming, line 1999
  confirmations: 1
  anchor_at: "100m-offers.md:1999"
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
- id: B-offers-084
  type: rule
  name: >-
    Make the goal specific and tangible
  statement: >-
    The goal component of the name states a specific, tangible event, feeling, experience or outcome that would excite the prospect.
  anchor: >-
    It can be an event, a feeling, an experience, or an outcome, anything that would excite them. The more specific and tangible, the better.
  source: >-
    100m-offers.md, ch. 16 Naming, line 2013
  confirmations: 1
  anchor_at: "100m-offers.md:2013"
- id: B-offers-085
  type: rule
  name: >-
    No quantifiable claim plus a duration where the platform forbids it
  statement: >-
    A quantifiable outcome such as income gain or weight loss is not paired with a stated duration unless the advertising platform allows it.
  why: >-
    A claim with a stated duration implies a guarantee that they will get the outcome in that time, which goes against many platform rules.
  applies_when: >-
    Advertising a quantifiable claim on a platform with compliance rules; where the goal is not a claim per se, use the interval.
  anchor: >-
    So dont give a quantifiable outcome with the duration unless your platform allows it.
  source: >-
    100m-offers.md, ch. 16 Naming, line 2021
  confirmations: 1
  anchor_at: "100m-offers.md:2021"
- id: B-offers-086
  type: rule
  name: >-
    Find Time To Rhyme
  statement: >-
    A name is rhymed or alliterated where it comes naturally, and left alone where it does not.
  why: >-
    Good rhymes stick in people's minds, and alliteration is easier for most people than rhyming; but it is a nice-to-have, not a requirement.
  anchor: >-
    Good rhymes stick in people’s minds. Rhyme your program name to win the game.
  source: >-
    100m-offers.md, ch. 16 Naming, line 2033
  confirmations: 2
  authors_caveat: >-
    You do not need to rhyme or alliterate, and forcing it is explicitly ruled out (lines 2035, 2043).
  anchor_at: "100m-offers.md:2033"
- id: B-offers-087
  type: rule
  name: >-
    Name Sub Items & Bonuses
  statement: >-
    The naming formula is applied to every item in the stack and bundle, not only to the offer as a whole.
  why: >-
    It automatically enhances the value of your offerings simply by naming them in a way that resonates with your prospects.
  anchor: >-
    Use the magic headline formula for each item in your stack and bundle.
  source: >-
    100m-offers.md, ch. 16 Naming, line 2087
  confirmations: 1
  anchor_at: "100m-offers.md:2087"
- id: B-offers-088
  type: rule
  name: >-
    Exhaust the lighter variations first
  statement: >-
    When an offer fatigues, the creative, then the body copy, then the headline and duration are changed before anything about the offer itself.
  why: >-
    The lower on the list you go, the more operationally heavy it is; most of the time it is the first handful of items that need changing, again and again, without touching the bottom of the list.
  anchor: >-
    The lower on the list you go, the more operationally heavy it is, so really be sure you have exhausted the earlier “lighter” ways of varying your offer.
  source: >-
    100m-offers.md, ch. 16 Naming, line 2106
  confirmations: 2
  anchor_at: "100m-offers.md:2106"
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
  confirmations: 1
  anchor_at: "100m-offers.md:2178"
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
  confirmations: 1
  anchor_at: "100m-offers.md:2216"
- id: B-offers-093
  type: rule
  name: >-
    Indirect costs stay out of LTV
  statement: >-
    Indirect costs such as admin, software and rent are excluded from the lifetime value calculation.
  why: >-
    Gross profit is revenue minus the direct cost of servicing an additional customer, which is not net profit.
  anchor: >-
    Note that the indirect costs, like admin, software, rent, etc., are not included in LTV.
  source: >-
    100m-offers.md, ch. 3 Pricing: The Commodity Problem, line 2214
  confirmations: 1
  anchor_at: "100m-offers.md:2214"
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
  confirmations: 2
  anchor_at: "100m-offers.md:2381"
- id: B-offers-095
  type: rule
  name: >-
    Create flow. Monetize flow. Then add friction.
  statement: >-
    Friction is added to the marketing, or less is offered for the same price, only after demand has been generated and people are saying yes.
  why: >-
    If you cannot get demand flowing in you have no idea whether what you have is good.
  anchor: >-
    I have always lived by the mantra, “Create flow. Monetize flow. Then add friction.”
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, line 2395
  confirmations: 1
  anchor_at: "100m-offers.md:2395"
- id: B-offers-096
  type: rule
  name: >-
    Sales to Fulfillment Continuum
  statement: >-
    The offer is positioned at the point where it still sells very well and is also easy to fulfil, rather than at either extreme of the continuum.
  why: >-
    Lowering what you have to do makes the product harder to sell, and doing as much as possible makes it easy to sell but hard to fulfil because of the demand on your time.
  anchor: >-
    The trick, and the ultimate goal, is to find a sweet spot where you sell something very well that’s also easy to fulfill.
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, line 2393
  confirmations: 1
  anchor_at: "100m-offers.md:2393"
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
  confirmations: 2
  anchor_at: "100m-offers.md:2417"
- id: B-offers-098
  type: rule
  name: >-
    10x to 1/10th test
  statement: >-
    Each problem is run through the question of what you would provide if the customer paid 10x the price and what you would do if they paid one tenth of it.
  why: >-
    Stretching your mind in either direction produces widely different solutions.
  anchor: >-
    10x to 1/10th test. If my customers paid me 10x my price (or $100,000) what would I provide?
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, line 2471
  confirmations: 1
  anchor_at: "100m-offers.md:2471"
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
  confirmations: 4
  anchor_at: "100m-offers.md:2485"
- id: B-offers-100
  type: rule
  name: >-
    Trim high cost, low value first
  statement: >-
    Trimming removes the high cost, low value items first, then the low cost, low value ones.
  anchor: >-
    I remove the ones that are high cost and low value first. Then I remove low cost, low value items.
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, line 2489
  confirmations: 1
  anchor_at: "100m-offers.md:2489"
- id: B-offers-101
  type: rule
  name: >-
    Judge value by the four value-equation questions
  statement: >-
    An item's value is decided by asking whether the client will financially value it, believe it makes success likely, see less effort and sacrifice, and see the result in far less time.
  why: >-
    Those are the four drivers of the value equation applied to a single deliverable.
  applies_when: >-
    You are not sure whether an item on the solutions list is high value.
  anchor: >-
    If you aren’t sure what’s high value, go through the value equation and ask yourself which of these things will this person:
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, line 2491
  confirmations: 1
  anchor_at: "100m-offers.md:2491"
- id: B-offers-102
  type: rule
  name: >-
    What remains is high value only
  statement: >-
    After trimming, only low cost high value and high cost high value items remain in the offer.
  anchor: >-
    What should remain are offer items that are 1) low cost, high value and 2) high cost, high value.
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, line 2498
  confirmations: 1
  anchor_at: "100m-offers.md:2498"
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
- id: B-offers-104
  type: rule
  name: >-
    Focus on high value one to many
  statement: >-
    The delivery vehicles the offer leans on are high value one-to-many solutions.
  why: >-
    They typically have the biggest discrepancy between cost and value: a high one-time cost of creation and infinitely low additional effort after, which is exactly why software becomes so valuable, and they become assets that create value in perpetuity.
  anchor: >-
    If there’s *one* type of delivery vehicle to focus on, it’s creating high value, “one to many” solutions.
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, line 2506
  confirmations: 2
  anchor_at: "100m-offers.md:2506"
- id: B-offers-105
  type: rule
  name: >-
    Save high cost items for big value adds
  statement: >-
    One-on-one and small group delivery is kept for big value adds only, and replaced wherever a lower cost alternative achieves the same value.
  anchor: >-
    You just want to make sure you save those high cost items for *big* value adds only. If you think you can accomplish the same value with a lower cost alternative, then do that instead.
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, line 2510
  confirmations: 1
  anchor_at: "100m-offers.md:2510"
- id: B-offers-106
  type: rule
  name: >-
    The bundle must be incomparable
  statement: >-
    The finished bundle solves all the perceived problems and cannot be compared or confused with the business down the street.
  why: >-
    Doing so also gives you the conviction that what you are selling is one of a kind, so prospects make a value-based rather than a price-based decision.
  anchor: >-
    Makes it impossible to compare or confuse your business or offering with the one down the street
  source: >-
    100m-offers.md, ch. 10 Part II: Trim & Stack, line 2598
  confirmations: 2
  anchor_at: "100m-offers.md:2598"
- id: B-offers-107
  type: rule
  name: >-
    Sell the vacation, not the plane flight
  statement: >-
    The dream outcome sold is the client arriving at their destination and what they will experience there, not the membership, product or vehicle.
  anchor: >-
    When you are thinking about your dream outcome, it has to be themarriving at their destination and what they would like to *experience*.
  source: >-
    100m-offers.md, ch. 9 Creating Your Grand Slam Offer Part I, line 2866
  confirmations: 1
  anchor_at: "100m-offers.md:2866"
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
  confirmations: 2
  anchor_at: "100m-offers.md:2870"
- id: B-offers-109
  type: rule
  name: >-
    List problems in the customer's sequence
  statement: >-
    Problems are listed in the sequence in which the customer will experience them.
  anchor: >-
    I like to think in the sequence that the customer will experience each of these obstacles.
  source: >-
    100m-offers.md, ch. 9 Creating Your Grand Slam Offer Part I, line 2872
  confirmations: 1
  anchor_at: "100m-offers.md:2872"
- id: B-offers-110
  type: rule
  name: >-
    Use the four value drivers to generate the problems
  statement: >-
    For each core thing the client must do, the reasons they could not do it or keep doing it are generated against the four value drivers.
  why: >-
    Each problem has four negative elements that align with the four value drivers: not financially worth it, will not work for me, too hard and confusing, takes too much time.
  anchor: >-
    just list out each core thing that someone has to do. Then think of all the reasons they wouldn't be able to do it, or keep doing it (using the four value drivers as a guide).
  source: >-
    100m-offers.md, ch. 9 Creating Your Grand Slam Offer Part I, line 2911
  confirmations: 2
  anchor_at: "100m-offers.md:2911"
- id: B-offers-111
  type: rule
  name: >-
    Turn each problem into a solution by reversing it
  statement: >-
    Each listed problem is converted into a solution by adding how to and reversing every element of the obstacle into solution-oriented language.
  why: >-
    It gives a checklist of exactly what you will have to do for prospects and what you are going to solve for them.
  anchor: >-
    simply adding “how to” then reversing the problem will give most people new to this process a great place to start
  source: >-
    100m-offers.md, ch. 9 Creating Your Grand Slam Offer Part I, line 2919
  confirmations: 1
  anchor_at: "100m-offers.md:2919"
```
