# Улов фазы 1 — $100M Series: Lost Chapters (2025) with $100M Leads: 2 Bonus Chapters (2023) as a second copy of Section A (ярус 2), тип B: правила и критерии

Группа `tier2-lost-chapters`, слаг `lost-chapters`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **130** (экстрактор вернул 130, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-series-lost-chapters.md` | 1–4810 | 6 | 118 |
| `100m-leads-bonus-chapters.md` | 1–568 | 1 | 12 |

## Как собран файл

Экстрактор B (Rules and criteria) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-lost-chapters.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-lost-chapters-B.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: B-lost-chapters-001
  type: rule
  name: >-
    Survey with a benefit attached
  statement: >-
    The customer survey is tied to a benefit the customer only receives after showing they completed it.
  why: >-
    Engagement is higher when the survey is done live at an event or on a call and the benefit depends on completion.
  applies_when: >-
    Step one of redefining the avatar, surveying existing customers.
  anchor: >-
    they show they completed it to receive some benefit Ask them every relevant detail
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, line 244
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:244"
- id: B-lost-chapters-002
  type: rule
  name: >-
    Sort for the top 20% and ignore the rest
  statement: >-
    Survey replies are sorted by the customers you like most, who spent the most and stayed the longest, and only the top 20% are analysed.
  why: >-
    Pareto on steroids: 20% of customers bring in 80% of revenue, so replacing the other 80% with high spenders grows the business 5x.
  applies_when: >-
    Step two of redefining the avatar, after the survey replies are in.
  anchor: >-
    spent the most, and stayed the longest Focus on the top 20% Ignore the rest
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, line 273
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:273"
- id: B-lost-chapters-003
  type: rule
  name: >-
    The fewest qualifiers in common
  statement: >-
    The new avatar is written as the fewest qualifiers all the top customers share, usually three to five.
  why: >-
    Reading the answers and finding the common qualifiers is work competitors will not do, which makes it an easy advantage.
  applies_when: >-
    Step three of redefining the avatar.
  anchor: >-
    Now, list them out Usually there are three to five qualifiers
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, line 279
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:279"
- id: B-lost-chapters-004
  type: rule
  name: >-
    Speak your new avatar
  statement: >-
    The customer requirements are stated up front and every piece of advertising speaks directly to that avatar.
  why: >-
    Naming the requirements repels the bad customers and attracts the good ones.
  applies_when: >-
    Step four of redefining the avatar, after the qualifiers are known.
  anchor: >-
    a) Speak your new avatar. Be up front about your customer requirements Get
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, line 284
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:284"
- id: B-lost-chapters-005
  type: rule
  name: >-
    Stop selling anyone outside the ideal customer requirements
  statement: >-
    No one who fails the ideal customer requirements is sold to, and effort shifts to the channels the qualifying customers come through.
  why: >-
    A business that accepts anyone with a pulse and a credit card gets high churn, high acquisition costs, low retention and lower satisfaction.
  anchor: >-
    Stop selling anyone who does not meet your
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, line 289
  confirmations: 1
  authors_caveat: >-
    Narrowing means serving fewer customers in the short term and may cost revenue while the change costs money.
  anchor_at: "100m-series-lost-chapters.md:289"
- id: B-lost-chapters-006
  type: rule
  name: >-
    Re-engineer the sales process from the best customers
  statement: >-
    The buying process the best customers actually went through is reverse-engineered and then made to happen on purpose for every lead.
  why: >-
    78% of the top Gym Launch customers had consumed at least two pieces of long-form content before buying, so forcing that consumption reproduced the buying process of the best customers.
  applies_when: >-
    Step four of redefining the avatar, after the survey shows how the best customers bought.
  anchor: >-
    b) Re-engineer the sales process. Look at what caused these better customers to
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, line 293
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:293"
- id: B-lost-chapters-007
  type: rule
  name: >-
    Start with what you know
  statement: >-
    With no customers to survey, the target is a narrow group inside the industry you already know most about, and it widens only as you learn more.
  why: >-
    The best venture capitalists pick founders with past experience in the industry they want to serve, because in-depth knowledge takes time to learn.
  applies_when: >-
    A business with no customers yet to run the survey on.
  anchor: >-
    the most. Create a narrow target, then serve them first. Don’t get fancy. Start
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, Pro Tip: What To Do If You Have No Customers, line 327
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:327"
- id: B-lost-chapters-008
  type: rule
  name: >-
    Do not cut qualification steps for volume
  statement: >-
    Qualification steps are not removed to raise lead volume; the number of steps is set by the long-run return on advertising.
  why: >-
    Every time qualification steps were removed, lead volume increased but the business made less money.
  applies_when: >-
    A buyer journey under pressure to produce more leads.
  anchor: >-
    every time we removed qualification steps, our lead volume increased, but we made less
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, Quality > Quantity, line 390
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:390"
- id: B-lost-chapters-009
  type: rule
  name: >-
    One acquisition department
  statement: >-
    Marketing and sales sit in one acquisition department rather than as two teams with separate goals.
  why: >-
    Merging them ended marketing complaining that sales was not closing and sales complaining that it wanted more leads; everyone focused on closing lots of valuable deals.
  anchor: >-
    money Merging marketing and sales into one acquisition department solved this problem
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, Quality > Quantity, line 391
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:391"
- id: B-lost-chapters-010
  type: rule
  name: >-
    Sell to people who do not stop buying
  statement: >-
    Either the product is improved until everyone wants to keep buying, or only customers who historically keep buying are sold to.
  why: >-
    Fortunes are created when we sell things that customers do not stop buying; companies with enterprise clients get higher multiples because those customers keep buying once they start.
  anchor: >-
    our goal should be either to improve our product so everyone wants to keep
  source: >-
    100m-series-lost-chapters.md, Your First Avatar, Pro Tip: Sell To People Who Don’t Stop Buying, line 423
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:423"
- id: B-lost-chapters-011
  type: rule
  name: >-
    Generate Flow, Monetize Flow, Increase Friction — in that order
  statement: >-
    Demand is generated first, monetised second, and friction added third, never in another order.
  why: >-
    Too many people put the cart before the horse; starting free or massively discounted gives something to benchmark and improve upon.
  anchor: >-
    Always remember - Generate Flow-->Monetize Flow-->Increase Friction. In that order. As I said in
  source: >-
    100m-leads-bonus-chapters.md, Attract Section Conclusion: Brass Tacks, line 561 = Lost Chapters lines 1424–1425
  confirmations: 2
  anchor_at: "100m-leads-bonus-chapters.md:561"
- id: B-lost-chapters-012
  type: rule
  name: >-
    Keep the front end as low as possible
  statement: >-
    When more Grand Slam Offers exist to upsell the customer over time, the front-end price is kept as low as possible to keep lead flow running.
  why: >-
    Demand is generated first, then monetised; the front end exists to keep lead flow cranking.
  applies_when: >-
    A money model that has further offers to make to the same customer over time.
  anchor: >-
    over time, I will keep my front end as low as possible to keep my lead flow cranking.
  source: >-
    100m-leads-bonus-chapters.md, Why I Use Free & Discount Promotions, line 89 = Lost Chapters line 554
  confirmations: 2
  anchor_at: "100m-leads-bonus-chapters.md:89"
- id: B-lost-chapters-013
  type: rule
  name: >-
    A promotion enhances the offer, it does not change it
  statement: >-
    The promotion is a wrapper around the existing Grand Slam Offer and leaves what is inside unchanged.
  why: >-
    Like wrapping paper: what is inside may be the same, but the wrapper makes it more inherently attractive.
  anchor: >-
    Important: The point of creating a promotion is to enhance your grand slam offer, not change it.
  source: >-
    100m-leads-bonus-chapters.md, Why I Use Free & Discount Promotions, line 99 = Lost Chapters lines 567–569
  confirmations: 2
  anchor_at: "100m-leads-bonus-chapters.md:99"
- id: B-lost-chapters-014
  type: rule
  name: >-
    Answer what’s in it for me
  statement: >-
    A promotion aimed at a cold market answers the question what’s in it for me on its face.
  why: >-
    In a cold market you must give people a reason to move towards you in order to generate demand flow.
  applies_when: >-
    Entering a cold market.
  anchor: >-
    move towards you. It must answer what’s in it for me. We are making it more attractive to a cold
  source: >-
    100m-leads-bonus-chapters.md, Why I Use Free & Discount Promotions, line 105 = Lost Chapters lines 573–574
  confirmations: 2
  anchor_at: "100m-leads-bonus-chapters.md:105"
- id: B-lost-chapters-015
  type: rule
  name: >-
    The two prerequisites of a premium offer
  statement: >-
    A premium offer is only run when there is something very valuable to provide and a selling process that demonstrates that value.
  why: >-
    With far lower volume the whole return rests on the value of the single thing sold and on the process that makes that value visible.
  applies_when: >-
    Choosing to lead with a premium offer rather than a free or discount one.
  anchor: >-
    1) Have something very valuable to provide (your Grand Slam Offer)
  source: >-
    100m-series-lost-chapters.md, Premium Promotions, lines 629–635
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:631"
- id: B-lost-chapters-016
  type: rule
  name: >-
    Do not start with a premium offer
  statement: >-
    A business that needs to make money now starts with a free or discount money model rather than a premium offer.
  why: >-
    Free and discount wrappers are essential in the beginning and can be removed over time as the reputation improves.
  applies_when: >-
    Starting over, or making money for a business owner from scratch.
  anchor: >-
    If I needed to make money, or make a business owner money, I would not start with
  source: >-
    100m-series-lost-chapters.md, Premium Promotions, If I Lost Everything And Had To Start Over, line 638
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:638"
- id: B-lost-chapters-017
  type: rule
  name: >-
    Free or discount first, premium after results
  statement: >-
    A new business gets customers in the door with a free or discount offer, proves results, and only then restructures to a premium offer.
  why: >-
    There is nothing below $0 and no lower to go, but the ticket can go infinitely higher once results are proven.
  applies_when: >-
    You are new in the market.
  anchor: >-
    If you’re new, start with a free or discount offer to get business in the door Prove results
  source: >-
    100m-series-lost-chapters.md, Premium Promotions, line 652
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:652"
- id: B-lost-chapters-018
  type: rule
  name: >-
    Premium as the second offer
  statement: >-
    A premium offer placed after a free offer only works if value was actually demonstrated in the first offer.
  why: >-
    The premium sale rests on believed value, and the free offer is where that value gets demonstrated.
  applies_when: >-
    Layering a premium offer behind a free front end.
  anchor: >-
    work well as the “second” offer you give after a free offer. But they'll only work if you demonstrated
  source: >-
    100m-leads-bonus-chapters.md, Premium Promotions, line 169 = Lost Chapters lines 657–658
  confirmations: 2
  anchor_at: "100m-leads-bonus-chapters.md:169"
- id: B-lost-chapters-019
  type: rule
  name: >-
    Proven process or cash to burn
  statement: >-
    Leading with a premium offer requires either an already proven conversion process or cash set aside to work one out.
  why: >-
    Each opportunity costs so much more that there is less room for error, and it takes time to get the sales process down.
  anchor: >-
    we want to lead with premium offers, we should already have a proven process or have some
  source: >-
    100m-series-lost-chapters.md, Premium Promotions, Cons #3, line 759
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:759"
- id: B-lost-chapters-020
  type: rule
  name: >-
    The premium package must merit the price
  statement: >-
    A premium offer is packed with bonuses, creative guarantees and premium support so it still feels like a deal at the higher cost.
  why: >-
    Only a small number of people raise their hands on a premium offer, so the offer they are getting has to be truly irresistible.
  anchor: >-
    you have a truly irresistible offer they are getting for their package Packed with bonuses,
  source: >-
    100m-series-lost-chapters.md, Premium Promotions, Cons #5, lines 790–791
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:790"
- id: B-lost-chapters-021
  type: rule
  name: >-
    When to wrap the premium offer
  statement: >-
    A premium offer is wrapped in a free or discount front end when the business is just starting out, its volume is not high enough, or its cost of acquisition is higher than it can bear.
  why: >-
    The wrapper gets people who would not otherwise respond to respond, without changing the core offer.
  anchor: >-
    But if you’re just starting out, or your volume isn’t high enough, or your cost of acquisition
  source: >-
    100m-series-lost-chapters.md, Premium Promotions, Conclusion, lines 805–807
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:805"
- id: B-lost-chapters-022
  type: rule
  name: >-
    Three reasons a free offer fails
  statement: >-
    When a free offer does not convert, the fix is what is given away or how it is described, the believability, or the targeting — never the price.
  why: >-
    A free offer is the fastest way to see if anyone wants the thing; if free does not work, prospects do not want it, do not believe you, or are not seeing it.
  applies_when: >-
    A free front end that is not producing response.
  anchor: >-
    1) Don’t want your thing—which means you should change what you are giving away
  source: >-
    100m-series-lost-chapters.md, Free Promotions, lines 822–837
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:822"
- id: B-lost-chapters-023
  type: rule
  name: >-
    Always answer Why
  statement: >-
    Every crazy free or discount offer carries a good and true reason why it is being made.
  why: >-
    An offer so good it is unbelievable gets no response; going out of business in 30 days makes 90% off believable where 90% off alone would not.
  anchor: >-
    whenever you give a crazy free offer away, you will always have to answer the next question:
  source: >-
    100m-series-lost-chapters.md, Free Promotions, lines 843–847
  confirmations: 2
  authors_caveat: >-
    The reason has to be true.
  anchor_at: "100m-series-lost-chapters.md:843"
- id: B-lost-chapters-024
  type: rule
  name: >-
    Add friction to raise lead quality
  statement: >-
    When a free offer brings more prospects than the business can handle or serve, friction is added rather than the offer abandoned.
  why: >-
    The more hoops someone has to go through, the higher the quality becomes; the key with free is the sweet spot on friction that maximises quality volume.
  applies_when: >-
    Free attracts too many prospects, or manual processes cannot handle the volume.
  anchor: >-
    problem. So we add friction. Friction increases lead quality. The more hoops someone has to go
  source: >-
    100m-leads-bonus-chapters.md, Free Promotions, Cons #1, line 329 = Lost Chapters lines 937–939
  confirmations: 2
  anchor_at: "100m-leads-bonus-chapters.md:329"
- id: B-lost-chapters-025
  type: rule
  name: >-
    Repeat the same qualifications everywhere
  statement: >-
    The listed qualifications appear at every point of the advertising — copy, creative and landing pages — in the same words.
  why: >-
    Listing qualifications decreases volume but increases quality, and it is friction that can be added at all points.
  anchor: >-
    advertising at all points You’ll want to repeat the same qualifications everywhere
  source: >-
    100m-series-lost-chapters.md, Free Promotions, Examples of Friction 1) Increased Qualifications, line 947
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:947"
- id: B-lost-chapters-026
  type: rule
  name: >-
    Weed out the weirdos, keep the lazy whales
  statement: >-
    The number of steps is set to just enough friction to weed out the weirdos without losing otherwise qualified people who will not bother.
  why: >-
    Prospects drop off at each point, so more steps give fewer and higher quality people but also lose qualified ones.
  anchor: >-
    weed out the weirdos but not so much that you lose some lazy whales.
  source: >-
    100m-leads-bonus-chapters.md, Free Promotions, Examples of Friction 3) Increased Number of Steps, line 350 = Lost Chapters lines 969–970
  confirmations: 2
  anchor_at: "100m-leads-bonus-chapters.md:350"
- id: B-lost-chapters-027
  type: rule
  name: >-
    Forced consumption needs cheap eyeballs
  statement: >-
    Forced consumption of sales material before the call to action is used only when advertising to a large audience where eyeballs are cheap.
  why: >-
    Forcing consumption cuts volume but increases lead quality; in other settings the volume is just too low to justify the friction.
  applies_when: >-
    Deciding whether to force a prospect to watch a video before the call to action appears.
  anchor: >-
    who have been pre-indoctrinated. This is a good strategy when you advertise to a large audience
  source: >-
    100m-leads-bonus-chapters.md, Free Promotions, Examples of Friction 4) Forced Consumption, line 355 = Lost Chapters lines 976–977
  confirmations: 2
  anchor_at: "100m-leads-bonus-chapters.md:355"
- id: B-lost-chapters-028
  type: rule
  name: >-
    Free Money Math
  statement: >-
    Campaigns are compared on the number of qualified leads the same ad spend produces, not on the percentage of leads that are qualified.
  why: >-
    $1,000 producing 500 leads of which half are qualified beats $1,000 producing 200 leads of which 80% are qualified, even though the team feels better about the second.
  anchor: >-
    Which campaign was better? Our team may feel better about #2, but according to pure dollars and
  source: >-
    100m-leads-bonus-chapters.md, Free Promotions, Free Money Math, line 383 = Lost Chapters line 1023
  confirmations: 2
  anchor_at: "100m-leads-bonus-chapters.md:383"
- id: B-lost-chapters-029
  type: rule
  name: >-
    Value without overextending
  statement: >-
    The free thing is valuable enough that people want it but cheap enough to deliver that it does not overextend the business.
  why: >-
    Giving away something with a real cost wastes resources on people with no intention of buying; with the volume high, friction skims the cream off the top.
  anchor: >-
    cents, #1 is better. So, make sure to provide value without overextending ourselves. This way, we
  source: >-
    100m-leads-bonus-chapters.md, Free Promotions, Free Money Math, line 384 = Lost Chapters line 1024
  confirmations: 2
  anchor_at: "100m-leads-bonus-chapters.md:384"
- id: B-lost-chapters-030
  type: rule
  name: >-
    Premium prices rise with premium lead costs
  statement: >-
    If the lead cost of a premium offer is 5–10x that of a free offer, the prices of that offer are at least 5–10x higher too.
  why: >-
    The number one mistake is running a premium offer at free-offer prices; free beats premium hands down unless the seller has truly mastered high-ticket selling.
  applies_when: >-
    Comparing or switching between a free and a premium front end (2025).
  anchor: >-
    If you know the lead cost is going to be 5–10x higher for a premium offer, your
  source: >-
    100m-series-lost-chapters.md, Free Promotions, Pro Tip: Free Makes More Money, lines 1056–1057
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1056"
- id: B-lost-chapters-031
  type: rule
  name: >-
    All five Ps reflect one structure
  statement: >-
    Price, Prospect, Process, Promotion and Product all reflect either a Free offer structure or a Premium offer structure, with no mixing of the two.
  why: >-
    They are entirely different acquisition strategies, and a comparison across mixed structures is not a fair comparison.
  anchor: >-
    Product should ALL reflect a Free offer structure or a Premium offer structure.
  source: >-
    100m-series-lost-chapters.md, Free Promotions, Pro Tip: Free Makes More Money, lines 1061–1063
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1062"
- id: B-lost-chapters-032
  type: rule
  name: >-
    If only one offer, make it free
  statement: >-
    When only one front-end offer can be made to convert a market, the free one is chosen.
  why: >-
    Better to wade through crappy leads and then add friction than to look at an empty calendar; going from a non-free to a free front end usually cut lead costs by five times or more.
  anchor: >-
    Bottom line: If I only had one offer to make to convert or my family would be killed, it would be a
  source: >-
    100m-leads-bonus-chapters.md, Free Promotions, line 410 = Lost Chapters lines 1068–1070
  confirmations: 2
  authors_caveat: >-
    The author does not claim free is for every offer, every time.
  anchor_at: "100m-leads-bonus-chapters.md:410"
- id: B-lost-chapters-033
  type: rule
  name: >-
    Massive discounts only
  statement: >-
    A discount promotion is 50% or more; marginal discounts of 5 to 25% off are not used.
  why: >-
    Marginal discounts are not enough to drive real behaviour and basically just cut into margin; 50% or more is what people respond to.
  anchor: >-
    Instead, we’re going to be talking about massive discounts (50% or more) Those are
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Understanding Discount Offers, lines 1080–1087
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1087"
- id: B-lost-chapters-034
  type: rule
  name: >-
    The test of a free or discount offer
  statement: >-
    A free or discount offer counts as working only if it gets people who would not otherwise consider the thing to respond.
  why: >-
    Free and discount offers create a perceived value discrepancy that drives action from a population that would not otherwise act.
  anchor: >-
    that wouldn’t otherwise act. And that’s what you have to accomplish with a free or discount
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Understanding Discount Offers, lines 1089–1091
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1090"
- id: B-lost-chapters-035
  type: rule
  name: >-
    Discount a piece of the thing
  statement: >-
    A discount offer covers a component of the offering, not the entire thing.
  why: >-
    In most instances a discount offer is a piece of the thing rather than the entire thing, with only a handful of notable exceptions.
  anchor: >-
    exceptions, in most instances a discount offer is a “piece of the thing,” not the “entire thing”
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Understanding Discount Offers, lines 1093–1096
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1096"
- id: B-lost-chapters-036
  type: rule
  name: >-
    Cycle through all four displays
  statement: >-
    The same discount is tested in all four display forms — percentage off, absolute amount off, relative equivalent, and the discounted price alone — before one is settled on.
  why: >-
    People respond differently to the same discount displayed differently, and multiple winners give more bullets in the chamber when a promotion fatigues.
  anchor: >-
    communicated differently By cycling through all four, you can test which resonates best in
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Four Ways To Display Discounts, lines 1151–1154
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1152"
- id: B-lost-chapters-037
  type: rule
  name: >-
    Discount only what is already understood
  statement: >-
    A discounted price is used only on a service people already have a price range for; otherwise the price is stated first and the discount second, or another offer is made.
  why: >-
    If a customer does not know what they are getting, a discount has nothing to compare against — 50% off an agency retainer means nothing.
  applies_when: >-
    Choosing a discount as a front-end offer.
  anchor: >-
    In order for the discounted price to be effective, the service will usually have
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Pro Tip: Use Absolute Prices When Talking about Understood Products and Services, lines 1161–1173
  confirmations: 3
  anchor_at: "100m-series-lost-chapters.md:1161"
- id: B-lost-chapters-038
  type: rule
  name: >-
    Regulated markets take the discount, not free
  statement: >-
    In a heavily regulated industry, state or country, the front end is a discount offer rather than a free one.
  why: >-
    In some countries stipulations or creative offers around free are forbidden; discounts allow compliant advertising and still generate decent lead volume.
  anchor: >-
    Note: If you are in a heavily regulated industry, state, or country, then a discount offer
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Pros #1, lines 1200–1202
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1200"
- id: B-lost-chapters-039
  type: rule
  name: >-
    Discount cash never funds acquisition
  statement: >-
    The money collected on a discount front end is never made the real way acquisition costs are liquidated.
  why: >-
    It will not amount to much money; it is only the first way to attract and transact with a customer.
  anchor: >-
    we will never build our business to use this money as the real way we are liquidating our costs. This
  source: >-
    100m-leads-bonus-chapters.md, Discount Promotions, Pros #2, line 465 = Lost Chapters lines 1211–1214
  confirmations: 2
  anchor_at: "100m-leads-bonus-chapters.md:465"
- id: B-lost-chapters-040
  type: rule
  name: >-
    Paid front end where a no-show costs real money
  statement: >-
    Where the time or cost of the person delivering is real, the front end is a paid discount offer rather than a free one.
  why: >-
    People typically show up for things they pay for, at least 85–90% or more, so a discount front end all but eliminates no-shows.
  applies_when: >-
    Services where a no-show burns a scarce resource, such as a doctor’s time (2025).
  anchor: >-
    people will typically show up for things they pay for (at least 85–90% or more) For us, if we
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Pros #4 The Two-Step Sale, lines 1261–1269
  confirmations: 3
  anchor_at: "100m-series-lost-chapters.md:1269"
- id: B-lost-chapters-041
  type: rule
  name: >-
    Add steps as price and complexity increase
  statement: >-
    The more complex or expensive the thing sold, the more time the prospect is given with you before the ask — all at once or spread over several calls.
  why: >-
    A conversion problem is often simply too little time spent with the prospect before asking for the sale.
  applies_when: >-
    Diagnosing a conversion problem on a complex or high-priced offer.
  anchor: >-
    you’re having a conversion issue, you may simply be spending too little time with
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Author Note: Add Steps As Price And Complexity Increase, lines 1325–1330
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1330"
- id: B-lost-chapters-042
  type: rule
  name: >-
    Give away the cheap time, not the expensive time
  statement: >-
    The first visit is operationally rebuilt so an admin or assistant can handle it, and the expensive practitioner’s time is spent only on the most qualified candidates.
  why: >-
    It eliminates the cost of no-shows while pre-qualifying candidates and putting them in the best position to say yes at the next visit.
  applies_when: >-
    A discount or free front end whose fulfilment would otherwise consume a high-cost practitioner’s time.
  anchor: >-
    doctor’s time. And instead operationally fix the first visit so it’s something a
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Pro Tip: Give Away Lower Cost Time If You Can, lines 1336–1345
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1338"
- id: B-lost-chapters-043
  type: rule
  name: >-
    Splinter the offer instead of discounting the core
  statement: >-
    The offer is splintered and a core component given at a discount; the core offer itself is not discounted.
  why: >-
    Always discounting the core offer trains people to buy only at discounted times.
  anchor: >-
    “splinter” our offer into tiny pieces and just give a core component at a discount—not the
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Cons #1 Giving Away The Farm, lines 1370–1380
  confirmations: 2
  authors_caveat: >-
    True discounts on the core offer work only where the pricing model is to raise prices wildly in the regular season and live off the discounting, as clothing retailers do.
  anchor_at: "100m-series-lost-chapters.md:1379"
- id: B-lost-chapters-044
  type: rule
  name: >-
    Discount buyers are qualified leads, not customers
  statement: >-
    Someone who buys the discount is counted as a qualified lead, and the offer is structured so that they qualify themselves into the core service.
  why: >-
    The businesses that complained about Groupon customers not buying the main thing did not know how to structure their offers to qualify prospects automatically.
  anchor: >-
    core service We shouldn’t see people as customers if they buy the discount We should see
  source: >-
    100m-series-lost-chapters.md, Discount Promotions, Cons #2 Bargain Hoppers, lines 1394–1396
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1395"
- id: B-lost-chapters-045
  type: rule
  name: >-
    Not enough response means the front end
  statement: >-
    When response is too low, the front end is made more appealing with a free or discount wrapper before anything else is changed.
  why: >-
    People who otherwise would not respond need a reason to do so, and enhancing the Grand Slam Offer with a free or discount front end is the fastest way to give one.
  applies_when: >-
    Whether figuring out a first acquisition channel or adding another.
  anchor: >-
    If you are not getting enough response, you probably need to make your front end
  source: >-
    100m-series-lost-chapters.md, Attract Section Conclusion: Brass Tacks, lines 1420–1423
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1420"
- id: B-lost-chapters-046
  type: rule
  name: >-
    Know the customer’s problem better than they do
  statement: >-
    Before running the promotion the business can name the further problems the customer will hit on their journey, and the upsells that solve them.
  why: >-
    All businesses capitalise on an information advantage: we know more about our customers’ problems than they do, and upsells are how that advantage is monetised.
  anchor: >-
    Fundamentally, to make this process work you must know your business and your
  source: >-
    100m-series-lost-chapters.md, Attract Section Conclusion: Brass Tacks, lines 1428–1433
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1428"
- id: B-lost-chapters-047
  type: rule
  name: >-
    Customer Financed Acquisition threshold
  statement: >-
    A money model passes Customer Financed Acquisition when 30 days of gross profit from a customer exceeds the cost of acquiring that customer.
  why: >-
    Getting the acquisition cost back as profit within the first thirty days lets the same money be used again to get the next customer, which removes cash as the bottleneck to growth.
  anchor: >-
    Customer Financed Acquisition (CFA) is when 30 days of GP (gross profit) from a
  source: >-
    100m-series-lost-chapters.md, Section B: The Expensive Customer Problem, lines 1461–1467
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1461"
- id: B-lost-chapters-048
  type: rule
  name: >-
    2x is the real life minimum
  statement: >-
    The working standard is 30-day gross profit of at least twice CAC, not merely more than CAC.
  why: >-
    At 2x you only have to buy your first customer; that customer pays for every other one and the business can grow as fast as it can handle.
  anchor: >-
    And 2x is my “real life” minimum standard In practice, I want customers to more than
  source: >-
    100m-series-lost-chapters.md, Section B: The Expensive Customer Problem, lines 1471–1477
  confirmations: 3
  anchor_at: "100m-series-lost-chapters.md:1474"
- id: B-lost-chapters-049
  type: rule
  name: >-
    Know CAC exactly, monthly, by channel
  statement: >-
    The actual cost to acquire a customer is calculated for the past few months and separately for every platform or way you advertise.
  why: >-
    Unlike LTGP, CAC is a hard science; most entrepreneurs report ad spend only and are surprised at the end of the month, and in some businesses that gap is the difference between $1,000,000 and $10,000,000 per month.
  anchor: >-
    can and should know exactly what it costs you to get a customer each month, by channel
  source: >-
    100m-series-lost-chapters.md, Cost To Acquire a Customer = CAC, lines 1586–1587, 1650–1652
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1587"
- id: B-lost-chapters-050
  type: rule
  name: >-
    CAC counts every acquisition cost
  statement: >-
    CAC includes advertising dollars, marketing and sales payroll, creative, software and sales commissions and salaries, not ad spend alone.
  why: >-
    Content leads counted as free and outbound teams counted only by commission turn a $1,000 sale that seemed to cost $200 into one that really costs $500.
  anchor: >-
    payroll to a media buyer, creative team, software, sales commissions and salaries, etc
  source: >-
    100m-series-lost-chapters.md, Cost To Acquire a Customer = CAC, lines 1591–1593
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1593"
- id: B-lost-chapters-051
  type: rule
  name: >-
    Gross profit per thing sold
  statement: >-
    Gross profit and gross margin are figured out for each individual thing sold as well as for the business overall.
  why: >-
    Some products you spend a lot of time on do not make as much profit as you thought.
  applies_when: >-
    Step one of calculating LTGP.
  anchor: >-
    LTGP Step One Action→Figure out your gross profit and gross margin for each thing
  source: >-
    100m-series-lost-chapters.md, Lifetime Gross Profit (LTGP), lines 1720–1722
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1720"
- id: B-lost-chapters-052
  type: rule
  name: >-
    New signups do not touch churn
  statement: >-
    Churn is the share of the original cohort that left in the period; customers signed up during the same period do not enter the calculation.
  why: >-
    You could sign up zero or 1,000 new clients in the month and still have lost five of the original hundred, so churn is still 5%.
  anchor: >-
    Note: People get this twisted Don’t be one If you sign up new clients during this time
  source: >-
    100m-series-lost-chapters.md, Lifetime Gross Profit (LTGP), lines 1767–1771
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1767"
- id: B-lost-chapters-053
  type: rule
  name: >-
    Two ways to compute LTGP
  statement: >-
    A physical products business multiplies average gross profit by the number of transactions; a recurring business divides gross profit by the churn percentage.
  why: >-
    The two business shapes give lifetime value differently, and the back-of-napkin formula has to match the shape.
  applies_when: >-
    Step three of calculating LTGP, once gross profit and transactions or churn are known.
  anchor: >-
    LTGP Step Three: If you have a physical products business, multiply average gross
  source: >-
    100m-series-lost-chapters.md, Lifetime Gross Profit (LTGP), lines 1774–1783
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:1774"
- id: B-lost-chapters-054
  type: rule
  name: >-
    30 Day Cash above CAC
  statement: >-
    The gross profit extracted from a new customer in their first 30 days is pushed above CAC.
  why: >-
    Thirty days is the window any business can get interest-free financing on a credit card, so a 30D Cash above CAC means customers are acquired with other people’s money and the balance cleared interest free.
  anchor: >-
    example If I can increase my 30D Cash above my CAC, then it means that I can get free
  source: >-
    100m-series-lost-chapters.md, Payback Period = PPD, Alex’s Most Prized Metric: 30 Day Cash (30D Cash), lines 1909–1914
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:1913"
- id: B-lost-chapters-055
  type: rule
  name: >-
    Pass CFA level one to stay in business
  statement: >-
    A business must at minimum get past CFA level one — where 30-day gross profit is below CAC — to survive for the long haul.
  why: >-
    Level one means floating the business on life savings, loans and lines of credit, which requires already having lots of money.
  anchor: >-
    You must pass CFA level one to stay in business for the long haul With a decent product
  source: >-
    100m-series-lost-chapters.md, Levels of Customer Financed Acquisition, lines 2134–2180
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:2177"
- id: B-lost-chapters-056
  type: rule
  name: >-
    Count the labour of working the leads
  statement: >-
    What can be paid per lead is calculated after the labour cost of working and selling the leads, not from revenue per prospect alone.
  why: >-
    In the example the $600 of revenue from ten prospects was entirely eaten by the $600 of labour to work and sell the leads, leaving $0 per lead.
  applies_when: >-
    Reading a value grid to decide what you can afford to pay for a lead.
  anchor: >-
    But what I’m not taking into account are the very real costs of working the leads
  source: >-
    100m-series-lost-chapters.md, Back End: The Value Grid, lines 2372–2380
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2372"
- id: B-lost-chapters-057
  type: rule
  name: >-
    New offers must add revenue without adding cost
  statement: >-
    A new offer is added only if it adds little or no cost in time, money or complexity, or if the profit it brings clearly outweighs the complexity it adds.
  why: >-
    Adding more offers and services is a fast track to operational complexity, which makes business hard.
  applies_when: >-
    Deciding whether to add an offer to an existing money model.
  anchor: >-
    complexity, it had better be worth it (lots of profit or very little cost)—keep that ratio high
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, lines 2423–2430
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2430"
- id: B-lost-chapters-058
  type: rule
  name: >-
    Buy what you refer out when it earns more
  statement: >-
    A revenue stream you refer out that makes more money than your own is a candidate for buying or incorporating rather than continuing to refer.
  why: >-
    Most businesses refer out lots of revenue; affiliate commissions are pure profit and go straight to the bottom line, and a bigger stream is worth owning.
  anchor: >-
    That being said, if something you refer out makes even more money, sometimes it’s
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, lines 2469–2470
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2469"
- id: B-lost-chapters-059
  type: rule
  name: >-
    Every service gets a feedback meeting
  statement: >-
    Every service has a scheduled feedback meeting a few weeks in with the customer.
  why: >-
    It gives information on what to improve, saves a customer who is not happy, and provides an upsell opportunity.
  anchor: >-
    they are enjoying the service You should do this for any service you have First, because it
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, Sales #3 More Services Sale (Continuity), lines 2597–2601
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2599"
- id: B-lost-chapters-060
  type: rule
  name: >-
    Every problem is an upsell opportunity
  statement: >-
    A client who is unhappy or says they need more support is offered a higher level of support, not just appeased.
  why: >-
    The complaint names the thing they want more of, so it is answered with the next Grand Slam Offer.
  applies_when: >-
    A client reports dissatisfaction or a gap in support.
  anchor: >-
    If the client is not enjoying their time or feel like they need more support, we still
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, Sales #3 More Services Sale (Continuity), lines 2605–2612
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2605"
- id: B-lost-chapters-061
  type: rule
  name: >-
    Advance every prospect after a no
  statement: >-
    A prospect who says no is still advanced to the next stage of the sales flow rather than exited.
  why: >-
    It gives another opportunity to provide value and monetise the person; people who said no to services still generated revenue at a complementary review.
  anchor: >-
    the next stage, even if they said no This gives us another opportunity to provide value and
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, Weaving Them Together, lines 2630–2632
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:2631"
- id: B-lost-chapters-062
  type: rule
  name: >-
    Add one conversion opportunity at a time
  statement: >-
    Offers are added to the money model one at a time, starting with the one that adds the most money at the lowest cost.
  why: >-
    The whole four-sale flow is overwhelming to build at once but not overwhelming when it is built one step at a time over 6 to 12 weeks.
  anchor: >-
    you start by adding one of these conversion opportunities that adds the most money at
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, Weaving Them Together, lines 2633–2635
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2634"
- id: B-lost-chapters-063
  type: rule
  name: >-
    Right Stage
  statement: >-
    A new offer fits the stage of the money model it is being added to: attraction offers to get customers at a reasonable price, upsells and downsells to raise 30-Day GP, continuity offers to maximise lifetime GP.
  why: >-
    Each stage of the money model has its own goal, and offer types that fit that goal.
  applies_when: >-
    First of the four steps to picking the right offer for your money model.
  anchor: >-
    Right Stage First, I make sure the offer fits the stage of the Money Model If I want to
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, Four Steps To Picking The Right Offer For Your Money Model, lines 2652–2655
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2652"
- id: B-lost-chapters-064
  type: rule
  name: >-
    Right Problem
  statement: >-
    The problem the offer solves makes sense for the business, can be solved with existing resources, and gives the customer big value when solved.
  why: >-
    Customers have many problems and you cannot solve them all.
  applies_when: >-
    Second of the four steps to picking the right offer for your money model.
  anchor: >-
    to pick problems that make sense for my business, that I can solve with existing resources,
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, Four Steps To Picking The Right Offer For Your Money Model, lines 2656–2658
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2657"
- id: B-lost-chapters-065
  type: rule
  name: >-
    Right Way
  statement: >-
    The offer solves the problem the way the customer prefers, presenting effective options they already want rather than convincing them of your way.
  why: >-
    Most times people just go to someone who solves the problem how they want it solved.
  applies_when: >-
    Third of the four steps to picking the right offer for your money model.
  anchor: >-
    Right Way Third, I solve based on the customer’s preference Say two people want to
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, Four Steps To Picking The Right Offer For Your Money Model, lines 2659–2663
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2659"
- id: B-lost-chapters-066
  type: rule
  name: >-
    Right Time
  statement: >-
    The offer is made at the customer’s moment of greatest need, not when it is convenient for the business.
  why: >-
    Someone might be hungry, but ask them if they want another steak after they are full and they will say no.
  applies_when: >-
    Fourth and, by the author, most important of the four steps to picking the right offer.
  anchor: >-
    are full, they’ll probably say no So to sell the most, I make my offer at the time of greatest
  source: >-
    100m-series-lost-chapters.md, Advanced Offer Stacking: How To, Four Steps To Picking The Right Offer For Your Money Model, lines 2664–2671
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:2666"
- id: B-lost-chapters-067
  type: rule
  name: >-
    Education time matches price and trust
  statement: >-
    The length of the presentation or education is set by the price of the thing and the amount of trust needed, not by format preference.
  why: >-
    The bigger the plane, the longer the runway: a 60-second ad sells a $67 physical product, a two-day workshop sells $100,000 consulting services.
  anchor: >-
    Bottom line: The amount of time you take educating the consumer is directly related to
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, lines 2734–2749
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:2746"
- id: B-lost-chapters-068
  type: rule
  name: >-
    Free dinner benchmark
  statement: >-
    A free education dinner converts about a quarter of the room to the lower offer and at least a third of those to the higher offer.
  why: >-
    The dinner presentation of 60 to 90 minutes sells a product that covers the cost of getting everyone there, and the buyers get individual appointments for the high-ticket item.
  applies_when: >-
    Free dinner presentations, e.g. a 100-person audience giving about 25 lower-offer and about eight higher-offer buyers (2025).
  anchor: >-
    Benchmark: Aim to convert a quarter of the room to the lower offer Of those who
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, Free Education with Offer Examples, lines 2751–2761
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2757"
- id: B-lost-chapters-069
  type: rule
  name: >-
    Free masterclass benchmark
  statement: >-
    A free 90-minute masterclass converts 10% of those still on the call when the offer is presented.
  why: >-
    The 90-minute presentation is structured to break the core beliefs around accomplishing the goal, and can be run remotely.
  applies_when: >-
    Free 90-minute masterclass as an attraction offer (2025).
  anchor: >-
    Benchmark: Convert 10% of those on the call when an offer is presented
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, Free 90-minute Masterclass, line 2768
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2768"
- id: B-lost-chapters-070
  type: rule
  name: >-
    Free challenge benchmark
  statement: >-
    A free multi-day challenge converts 2 to 5% of the people who sign up for it.
  why: >-
    Four live 60–90 minute presentations Monday to Thursday each break a core belief and deliver value that can be applied today, with the offer made on Friday.
  applies_when: >-
    Free 5 Day Challenge, converting ice-cold audiences for both low-cost and very high-cost offers (2025).
  anchor: >-
    Benchmark: Convert 2 to 5% of people who sign up for the free multi-day challenge
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, Free 5 Day Challenge, line 2795
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2795"
- id: B-lost-chapters-071
  type: rule
  name: >-
    One core belief per summit day
  statement: >-
    Each day of a multi-day summit is structured around one of the three core limiting beliefs, with the pitch at the end of day two and a repitch on day three.
  why: >-
    Three full days give the most content a reasonable person can consume in a row, which sets up the highest ticket offers of all.
  applies_when: >-
    Free 3 Day virtual Summit with 4+ presentations a day; the days of the week do not matter.
  anchor: >-
    Structure each of the days (4+ presentations) around one of the core beliefs (found
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, Free 3 Day virtual Summit, lines 2816–2821
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2816"
- id: B-lost-chapters-072
  type: rule
  name: >-
    Summit benchmark
  statement: >-
    A free three-day virtual summit converts 10% of those attending the final day.
  why: >-
    The summit forces the most exposure a reasonable person can take in a row, which is what high-ticket offers to cold audiences need.
  applies_when: >-
    Free 3 Day virtual Summit (2025).
  anchor: >-
    Benchmark: Aim to convert 10% of those attending the final day
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, Free 3 Day virtual Summit, line 2823
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2823"
- id: B-lost-chapters-073
  type: rule
  name: >-
    BANT on the free strategy call
  statement: >-
    On a free strategy call the prospect is triaged on Budget, Authority, Need and Timing before an offer is made.
  why: >-
    The call is a value-add that acts as a pre-qualification for a later sale; value is provided by listening, identifying needs and offering solutions.
  applies_when: >-
    Free Strategy Call as step one of a two-step sales process.
  anchor: >-
    acronym for this is BANT: Budget, Authority, Need, Timing You provide value on this
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, Free Strategy Call, lines 2825–2842
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2840"
- id: B-lost-chapters-074
  type: rule
  name: >-
    Strategy call benchmark
  statement: >-
    A free strategy call converts 25% of those who make it to the second call.
  why: >-
    The first call triages and provides value; the offer belongs on the second one.
  applies_when: >-
    Free Strategy Call in a two-step sales process (2025).
  anchor: >-
    Benchmark: Convert 25% of those who make it to the second call
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, Free Strategy Call, line 2844
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2844"
- id: B-lost-chapters-075
  type: rule
  name: >-
    More time with you, more money from them
  statement: >-
    Anything that gets more people to consume more of your material — email follow-up, text campaigns, participation-based value adds — is added, because time spent with you tracks money spent with you.
  why: >-
    As a rule to sell by, the more time they spend with you, the more money they will spend with you.
  anchor: >-
    numbers As a rule to sell by—the more time they spend with you, the more money they’ll spend
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, Pro Tips, lines 2894–2897
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:2896"
- id: B-lost-chapters-076
  type: rule
  name: >-
    Messaging aligned to the three core beliefs
  statement: >-
    Presentation messaging is aligned to the three core limiting beliefs — results must come easy, results must be the best possible, results must lead to attention and approval.
  why: >-
    The better the messaging aligns and plays to the three core beliefs, the better the conversion.
  applies_when: >-
    Any presentation-based selling, from one 60–90 minute session to a dozen.
  anchor: >-
    The better the messaging is at aligning and playing to the three core beliefs the better
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, Pro Tips, lines 2900–2901
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:2900"
- id: B-lost-chapters-077
  type: rule
  name: >-
    Get them to watch the whole thing
  statement: >-
    A long-form presentation is judged on whether people watch the whole thing, receive value in an entertaining way and come away with goodwill.
  why: >-
    Long-form presentation-based selling depends on value through entertainment, life lessons and breaking limiting beliefs; it is what converts cold traffic into buyers.
  applies_when: >-
    Long-form presentation selling to cold or large audiences.
  anchor: >-
    life lessons, and breaking limiting beliefs Your focus should be to get them to watch the
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Presentations, Pro Tips, lines 2902–2906
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:2903"
- id: B-lost-chapters-078
  type: rule
  name: >-
    No freemium without capital
  statement: >-
    Freemium is not used by a business without investors and large amounts of capital.
  why: >-
    Almost every one of the companies used as freemium examples has funding, and the author has seen it done wrong by smart people more often than right.
  anchor: >-
    do not have investors and large amounts of capital, I would not recommend this structure
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Freemium, lines 2941–2943
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:2942"
- id: B-lost-chapters-079
  type: rule
  name: >-
    The freemium qualifier
  statement: >-
    A business qualifies for freemium only if it has something so valuable that lots of people come to it without marketing; otherwise it steers clear.
  why: >-
    The free thing must spread by word of mouth at an ad spend of $0, or the model just loses money servicing free customers.
  anchor: >-
    towards you without marketing—then you have something that qualifies for this structure
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Freemium, lines 2944–2946
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:2945"
- id: B-lost-chapters-080
  type: rule
  name: >-
    Three conditions on the freemium giveaway
  statement: >-
    The freemium giveaway costs almost nothing to fulfil, provides continuous rather than one-time value, and does not give away so much that the customer never needs to buy anything else.
  why: >-
    Get it wrong and you run a business that loses money servicing customers for free; software fits because it is virtually free per extra user and gives continuous value.
  anchor: >-
    challenging You must give something away that 1) costs you almost nothing to fulfill, 2)
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Freemium, Details, lines 2993–2998
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:2993"
- id: B-lost-chapters-081
  type: rule
  name: >-
    Freemium CAC is service cost over upgrade rate
  statement: >-
    The true cost of acquisition under freemium is the monthly cost of servicing one free customer divided by the percentage of free customers who upgrade.
  why: >-
    At $0.05/mo to service and a 1% upgrade rate the CAC is $5/mo, so average revenue per paid user has to clear $15/mo for the business to be profitable and able to grow.
  applies_when: >-
    Judging whether a freemium model can work (2025).
  anchor: >-
    Your true cost of acquisition when using this model is understanding what percentage
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Freemium, Details, lines 3014–3019
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3014"
- id: B-lost-chapters-082
  type: rule
  name: >-
    Pick Your Price is free only
  statement: >-
    Free Pick Your Price is run as a free offer and never as a discount wrapper.
  why: >-
    The play rests on the offer being free and the payment being the prospect’s own choice.
  anchor: >-
    This offer does not work with a discount wrapper
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Pick Your Price, Free Versus Discount Note, lines 3140–3141
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3141"
- id: B-lost-chapters-083
  type: rule
  name: >-
    Three payment levels with bonuses
  statement: >-
    A pick-your-price offer carries bonuses at three levels of payment — small, medium and large — to move people off $0.
  why: >-
    The bonuses at rising levels are what encourage them to pay something more than nothing on a sliding scale that has no maximum.
  anchor: >-
    To further incentivize them paying, you offer bonuses for three levels of payment (think
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Pick Your Price, Details, lines 3144–3147
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3144"
- id: B-lost-chapters-084
  type: rule
  name: >-
    The basic level is always given free
  statement: >-
    Anyone who does not want to pay still receives the basic level for free.
  why: >-
    The offer was marketed as free; the goodwill and the later upsells depend on honouring that.
  anchor: >-
    someone doesn’t want to pay for the first thing, you must give them the basic level for free
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Pick Your Price, Details, lines 3147–3151
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3149"
- id: B-lost-chapters-085
  type: rule
  name: >-
    Pre-frame the pick-your-price setup
  statement: >-
    The pick-your-price setup and the bonus levels are explained at the beginning of the sale, together with the fact that the prospect is not obligated to pay anything.
  why: >-
    Explaining it up front avoids awkwardness at the end and earns the prospect’s goodwill.
  anchor: >-
    You want to make sure that at the beginning of the sale you explain that you do have a
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Pick Your Price, Details, lines 3155–3166
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3155"
- id: B-lost-chapters-086
  type: rule
  name: >-
    Confrontational commitment questions under the pre-frame
  statement: >-
    Under the pick-your-price pre-frame the prospect is asked hard commitment questions, and anyone with no intention of staying is weeded out.
  why: >-
    The clients you want are the ones who willingly pay and are appreciative; the free offer is a mini-test for that and should feel like an interview.
  applies_when: >-
    Selling a Free Pick Your Price offer with the pre-frame in place.
  anchor: >-
    When selling with that pre-frame, though, you can and should hit the prospect hard
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Pick Your Price, Details, lines 3167–3174
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3167"
- id: B-lost-chapters-087
  type: rule
  name: >-
    Low operational cost on the free thing
  statement: >-
    The thing given away free has low operational costs, and the higher-cost fulfilment is reserved for the people who choose to pay.
  why: >-
    Otherwise giving it to everyone burns out the staff.
  anchor: >-
    Make sure that the thing you are giving away for free has low operational costs so you
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Pick Your Price, Details, lines 3175–3177
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3175"
- id: B-lost-chapters-088
  type: rule
  name: >-
    Outline the levels, ask for payment, then shut up
  statement: >-
    At the end of the pitch the levels are outlined, the payment question is asked, and the seller says nothing further.
  why: >-
    They take out their card and tell you which level they want; it is hard for people to say no into the silence.
  anchor: >-
    say “we accept Visa, Mastercard, or XYZ payment, which would you prefer to use?” Then
  source: >-
    100m-series-lost-chapters.md, Attraction Offer: Free Pick Your Price, Details, lines 3180–3183
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3181"
- id: B-lost-chapters-089
  type: rule
  name: >-
    Multi-step sales process for free with alternate revenue
  statement: >-
    A free-with-alternate-revenue-stream offer is sold through a multi-step sales process, not a single transaction.
  why: >-
    The money is made on the upsell that follows the free thing, which needs its own step.
  applies_when: >-
    Marketing thing A for free and monetising thing B.
  anchor: >-
    You’ll want to use a multi-step sales process with this offer If you are marketing “thing
  source: >-
    100m-series-lost-chapters.md, Upsell Offer: Free With Alternate Revenue Stream, Details, lines 3325–3327
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3325"
- id: B-lost-chapters-090
  type: rule
  name: >-
    Low incremental cost on the free thing
  statement: >-
    What is marketed as free has low incremental costs, so that adding another unit costs the business almost nothing.
  why: >-
    If you market thing A for free then you must actually be able to give it away for free.
  anchor: >-
    something that has low incremental costs (i e , adding another unit doesn’t cost much)
  source: >-
    100m-series-lost-chapters.md, Upsell Offer: Free With Alternate Revenue Stream, Details, lines 3326–3328
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3328"
- id: B-lost-chapters-091
  type: rule
  name: >-
    Upsell the next natural thing
  statement: >-
    The thing upsold after the free front end is the next natural thing the prospect would need on their journey.
  why: >-
    It requires understanding the prospect’s problem and the available solutions better than they do; each upsell in the book example is a requisite for succeeding with the free thing.
  applies_when: >-
    Using free with an alternate revenue stream as a front-end offer.
  anchor: >-
    If you are using it as a front-end offer, you want to make the next thing you are selling/
  source: >-
    100m-series-lost-chapters.md, Upsell Offer: Free With Alternate Revenue Stream, Details, lines 3332–3335
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3332"
- id: B-lost-chapters-092
  type: rule
  name: >-
    Frictionless upsell, 90% plus take rate
  statement: >-
    The upsell process is made frictionless enough that take rates reach 90% or more, and the prospect feels it makes total sense to buy.
  why: >-
    The effectiveness of the play rests on how essential the next thing seems and how seamless the upsell process is.
  applies_when: >-
    Free with alternate revenue stream offers (2025).
  anchor: >-
    2) How seamless the upsell process is for the prospect If you make it frictionless, you
  source: >-
    100m-series-lost-chapters.md, Upsell Offer: Free With Alternate Revenue Stream, Details, lines 3352–3355
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3352"
- id: B-lost-chapters-093
  type: rule
  name: >-
    Cold traffic: card on the first transaction
  statement: >-
    With cold traffic the first transaction closes a trial plus a credit card, and the product upsell comes on the second.
  why: >-
    Otherwise you get a lot of no-shows.
  applies_when: >-
    Running a free-with-alternate-revenue offer on cold traffic.
  anchor: >-
    You can obviously use this up front With cold traffic, you’re going to want to close a
  source: >-
    100m-series-lost-chapters.md, Upsell Offer: Free With Alternate Revenue Stream, Details, lines 3379–3381
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3379"
- id: B-lost-chapters-094
  type: rule
  name: >-
    The upsell is the predictor of retention
  statement: >-
    Someone who does not buy the first upsell is treated as unlikely to stay, and the upsell is worked as a must-have rather than a nice-to-have.
  why: >-
    It is the greatest predictor of back-end conversion, so however minor the sale looks it is the most important one for the long-term value of the customer.
  anchor: >-
    NOTE: If someone does not buy the upsell, they are unlikely to stay It’s the greatest
  source: >-
    100m-series-lost-chapters.md, Upsell Offer: Free With Alternate Revenue Stream, Details, lines 3383–3387
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3383"
- id: B-lost-chapters-095
  type: rule
  name: >-
    Monthly stick needs monthly extra value
  statement: >-
    A continuity offer that has to hold customers longer delivers extra value on top of the product itself, every month.
  why: >-
    A good offer gets them to start; good bonuses get them to stick, and each bonus extends the stay again.
  applies_when: >-
    Continuity offers where customers have already started.
  anchor: >-
    value on top of the continuity product itself So improving monthly stick means providing
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, Description, lines 3477–3479
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3478"
- id: B-lost-chapters-096
  type: rule
  name: >-
    Customers must know the bonus exists
  statement: >-
    Customers are told what bonus is coming next, at signup and at every point after, including right after a bonus is given.
  why: >-
    They can only get excited enough to stay longer for a bonus if they know it exists.
  anchor: >-
    Make sure customers know about your bonuses They can only get excited enough to
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, Important Notes, lines 3553–3556
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3553"
- id: B-lost-chapters-097
  type: rule
  name: >-
    Announce the type, keep the bonus a surprise
  statement: >-
    Customers are told the type of bonus they will get, while the bonus itself is kept a surprise.
  why: >-
    It keeps flexibility for the business and makes the bonus more valuable; Gym Launch customers knew a new play was coming every month but not which one.
  anchor: >-
    bonus they get, but keep the bonus itself a surprise This gives you flexibility and makes the
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, Important Notes, lines 3557–3561
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3558"
- id: B-lost-chapters-098
  type: rule
  name: >-
    Keep bonuses variable unless the upgrade is permanent and huge
  statement: >-
    A recurring bonus stays variable unless it gives a huge and permanent improvement, in which case it can be a lifetime upgrade.
  why: >-
    However good the thing is, customers get used to it; new stuff given more often, even if less valuable, keeps more customers interested longer.
  anchor: >-
    variable bonuses or Lifetime Upgrades Unless your bonus gives a huge and permanent
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, Important Notes, lines 3565–3570
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3565"
- id: B-lost-chapters-099
  type: rule
  name: >-
    Milestones that pay you back
  statement: >-
    Every milestone that unlocks a bonus is something that makes the customer more successful, something that advertises on your behalf, or ideally both.
  why: >-
    Publicly posting that they are starting a weight loss challenge both increases their adherence and advertises the business, so it earns a bonus.
  applies_when: >-
    Setting the when for a milestone bonus.
  anchor: >-
    milestones either: things that make my customer more successful—think activation points
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, Important Notes, lines 3571–3577
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3572"
- id: B-lost-chapters-100
  type: rule
  name: >-
    Combine the whens and the whats
  statement: >-
    A continuity offer combines bonus timings and bonus types: a one-time bonus to get them to a point, a recurring or lifetime upgrade to keep them past it, a milestone bonus on top.
  why: >-
    A one-time bonus extends the stay once, so more incentives to start and stick are better than one.
  anchor: >-
    Combine bonuses when you can You can combine both the “whens” and the “whats”
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, Important Notes, lines 3578–3586
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3578"
- id: B-lost-chapters-101
  type: rule
  name: >-
    Change the label when a big bonus unlocks
  statement: >-
    When a customer unlocks a big bonus their label changes to one that names the trait of a loyal customer and that they would not want to lose.
  why: >-
    The status is worth more if it can be bragged about and feels bad to lose, as with airline status tiers.
  anchor: >-
    Give customers status and bragging rights when they unlock bonuses Once customers
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, Important Notes, lines 3592–3597
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3592"
- id: B-lost-chapters-102
  type: rule
  name: >-
    Celebrate status changes publicly
  statement: >-
    A status change is paired with a ceremony or graduation held in public.
  why: >-
    The more the status change is celebrated, the more it is worth, and the less the customer wants to lose it.
  applies_when: >-
    Monthly, quarterly, or whenever there are big achievements to celebrate.
  anchor: >-
    Celebrate status changes publicly The more you can pair status changes with little
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Upgrades, Important Notes, lines 3598–3602
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3598"
- id: B-lost-chapters-103
  type: rule
  name: >-
    Lifetime Discount plus urgency, scarcity and a reason
  statement: >-
    A Lifetime Discount carries urgency (limited time), scarcity (limited number) and a believable reason for both.
  why: >-
    With those components the Lifetime Discount works like magic; the grand-opening founding member discount filled locations with 400+ recurring members before opening.
  anchor: >-
    To make Lifetime Discounts even more attractive, add urgency (limited time), scarcity
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, Description, lines 3664–3675
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3664"
- id: B-lost-chapters-104
  type: rule
  name: >-
    A discount requires a real retail price
  statement: >-
    A Lifetime Discount is only offered where the business actually charges more once the offer ends.
  why: >-
    Otherwise you are just listing the price and pretending it is a discount.
  anchor: >-
    A Lifetime Discount only works if you actually charge more when this offer ends
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, Description, lines 3677–3678
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3677"
- id: B-lost-chapters-105
  type: rule
  name: >-
    Profit after the discount
  statement: >-
    Any discount, lifetime or not, still leaves a profit and a healthy LTGP after it is applied.
  why: >-
    The cost of getting and delivering to customers changes, and a locked-in rate below those costs is trouble.
  anchor: >-
    Final point: when giving Lifetime Discounts or any other discount, make sure you make
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, lines 3685–3686, 3903
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3685"
- id: B-lost-chapters-106
  type: rule
  name: >-
    Know your numbers before a Lifetime Discount
  statement: >-
    A Lifetime Discount is not offered by a business that does not know its acquisition and delivery costs.
  why: >-
    The customer keeps a locked-in rate as long as they pay, while costs change; if costs rise above the profit, the locked rate becomes a problem.
  anchor: >-
    Lifetime Discounts come with a big fat warning: know your numbers. Lifetime
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, Important Notes, lines 3761–3765
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3761"
- id: B-lost-chapters-107
  type: rule
  name: >-
    Percentage or dollars off rather than a fixed price
  statement: >-
    A lifetime discount is expressed as a percentage off retail or a dollar amount off retail rather than a fixed price for life.
  why: >-
    Those two keep flexibility: when things change you can adjust the retail price and the discounted customers still keep their discount.
  anchor: >-
    two are far more flexible If things change (they always do), you can adjust your retail price
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, Important Notes, lines 3766–3774
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3771"
- id: B-lost-chapters-108
  type: rule
  name: >-
    Price protection for a fixed period
  statement: >-
    Price protection is given for a stated number of months rather than forever.
  why: >-
    One price forever limits the business; a fixed term keeps flexibility while still protecting the customer.
  anchor: >-
    Limit price protection for fixed periods I try to always give myself flexibility Giving
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, Important Notes, lines 3775–3779
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3775"
- id: B-lost-chapters-109
  type: rule
  name: >-
    Never waste a crisis
  statement: >-
    The reason attached to a lifetime discount is a real event in the life of the business or owner, good or bad.
  why: >-
    Lifetime discounts are almost too good to be true, so they need an equally strong reason to be believable, and the best ones are real and true life events.
  anchor: >-
    Never waste a crisis Lifetime discounts are almost too good to be true So you need an
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, Important Notes, lines 3781–3795
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3781"
- id: B-lost-chapters-110
  type: rule
  name: >-
    A one-time-only discount is offered once
  statement: >-
    A discount announced as one time only is never offered on the same thing again; to sell at that rate again, what is included in the offer is changed.
  why: >-
    Repeating a one-time-only offer on the same thing costs credibility with everyone who took it.
  anchor: >-
    If you say you will only offer this discount once and never again, stay true to it To
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, Important Notes, lines 3797–3800
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3797"
- id: B-lost-chapters-111
  type: rule
  name: >-
    One price at a time for the same thing
  statement: >-
    Two different prices for the same thing are never offered to two different people at the same time.
  why: >-
    Businesses test price points all the time, but simultaneous prices for the same thing break credibility.
  anchor: >-
    do not offer two different prices to two different people at the same time for the same thing
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, Important Notes, lines 3800–3801
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3801"
- id: B-lost-chapters-112
  type: rule
  name: >-
    Loss leader conditional on retail
  statement: >-
    Where two services are complementary, one is given at a steep forever founder’s discount on condition that the other is bought at retail.
  why: >-
    Insane founder’s discounts attract the leads and the profit is made on the upsell; this works better than two mid-priced offers or a generic 25% off both.
  applies_when: >-
    A business with two or more complementary services.
  anchor: >-
    You can offer a Lifetime Discount on one thing so long as they buy another at retail
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, Important Notes, lines 3802–3809
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3802"
- id: B-lost-chapters-113
  type: rule
  name: >-
    Remind leavers what the discount costs them
  statement: >-
    A customer who wants to leave is reminded that they lose their lifetime discount.
  why: >-
    It saves some customers from leaving, because they cannot get the rate back.
  applies_when: >-
    A cancellation request from a lifetime discount customer.
  anchor: >-
    If a customer wants to leave the program, remind them they’ll lose the discount
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, Important Notes, lines 3810–3811
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3810"
- id: B-lost-chapters-114
  type: rule
  name: >-
    No discount back after a cancellation
  statement: >-
    A customer who cancelled a Lifetime Discount is not given it back; they are offered a downsell at the same price with different features.
  why: >-
    Giving it back loses credibility with everyone else who kept paying to keep theirs.
  applies_when: >-
    A cancelled lifetime discount customer who wants to return, especially a price-sensitive one.
  anchor: >-
    If a customer wants to return after canceling a Lifetime Discount First, don’t give it
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, Important Notes, lines 3812–3815
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3812"
- id: B-lost-chapters-115
  type: rule
  name: >-
    Buy down the monthly rate
  statement: >-
    As soon as the customer likes the product, the original offer is made again: pay the difference of the down payment and lock in a permanently lower monthly rate.
  why: >-
    It brings in more cash and makes a stickier customer at the same time.
  anchor: >-
    Bonus: The upsell comes built in As soon as they like the product, make the original
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, The Bigger The Head, The Longer The Tail, lines 3818–3823
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3818"
- id: B-lost-chapters-116
  type: rule
  name: >-
    The bigger the head, the longer the tail
  statement: >-
    The more the customer is made to commit up front — an initiation fee, a paid-in-full discount, a waived fee tied to a term — the longer they are expected to stay.
  why: >-
    The sunk cost fallacy: people keep investing where they have already invested time or money; the membership with the longest stick rate is the one where they paid the most up front.
  anchor: >-
    The more you can get people to commit up front the longer they’ll stick
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, The Bigger The Head, The Longer The Tail, lines 3836–3843
  confirmations: 3
  anchor_at: "100m-series-lost-chapters.md:3840"
- id: B-lost-chapters-117
  type: rule
  name: >-
    Weight the payment to the front
  statement: >-
    Payment plans put more money in the up-front payment than in the scheduled ones, and the customer is reminded of the cash and the price they forfeit as close to the purchase or the cancellation as possible.
  why: >-
    $1,000 today then five payments of $100 collects; $100 a month then $1,000 at the end is far likelier to fail on the last payment.
  anchor: >-
    last payment goes through is lower We account for this risk by adding more to the up front
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Lifetime Discounts, lines 3871–3883
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3875"
- id: B-lost-chapters-118
  type: rule
  name: >-
    The higher the startup fee, the lower the churn
  statement: >-
    A higher one-time startup fee is used where lower churn is wanted, because the barrier to entry becomes the barrier to exit.
  why: >-
    A $100 sign-up fee on a $10/mo tanning membership produced next to no churn while $19 down and $19/mo churned at a higher rate.
  anchor: >-
    The higher the one-time startup fee, the lower the churn The higher the barrier to entry,
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Discount + One-Time Fee, Details, lines 3972–3976
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:3972"
- id: B-lost-chapters-119
  type: rule
  name: >-
    A startup fee where the customer has to do the work
  statement: >-
    Where the customer must do something themselves to succeed — send information, fill out forms, show up, change behaviour — a one-time startup fee is charged to get them invested.
  why: >-
    When people pay, they pay attention; the fee actively decreases churn and increases the investment of the prospect.
  anchor: >-
    selections, changing behavior, etc If you need someone to do something in order to be
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Discount + One-Time Fee, Details, lines 3980–3984
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:3982"
- id: B-lost-chapters-120
  type: rule
  name: >-
    Name the reason for the fee
  statement: >-
    Every one-time fee has a clear stated reason, even though the fee is made up, and that reason is raised with every customer.
  why: >-
    You are doing the work anyway, so you may as well let them know exactly what you are going to be doing for them; it is not a fee to be taken lightly.
  anchor: >-
    Note: Be clear about what the “reason” for the one-time fee is (even though it’s made
  source: >-
    100m-series-lost-chapters.md, Continuity Offer: Discount + One-Time Fee, Details, lines 4000–4006
  confirmations: 2
  anchor_at: "100m-series-lost-chapters.md:4000"
- id: B-lost-chapters-121
  type: rule
  name: >-
    A business that needs you is not an asset
  statement: >-
    A business that only makes money with the owner in it is treated as a high-paying job, not a valuable asset, however large its profit.
  why: >-
    If the business only makes money with you in it, it is a bad investment for anyone else; the same $2,000,000 of profit in a business that runs without you could easily be worth $10,000,000 right now.
  anchor: >-
    Sure, you make a bit of money, but your business isn’t worth much. If the business only
  source: >-
    100m-series-lost-chapters.md, Section D: Expanded Employees Chapter, Why Employees Make You Wealthy, lines 4113–4131
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4113"
- id: B-lost-chapters-122
  type: rule
  name: >-
    Six to 11 contacts a week with a lead-getting employee
  statement: >-
    Each lead-getting employee is met six to 11 times a week by their owner or manager.
  why: >-
    The cadence creates faster feedback cycles for building skills and morale.
  applies_when: >-
    Employees whose job is getting leads (2025).
  anchor: >-
    on the business, I or my managers meet with each lead-getting employee six to 11 times per
  source: >-
    100m-series-lost-chapters.md, Section D, Keep Your Employees Getting You Leads—The Performance Diamond, lines 4334–4336
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4335"
- id: B-lost-chapters-123
  type: rule
  name: >-
    One weekly one-on-one plus daily huddles
  statement: >-
    The week holds one 30 to 45 minute one-on-one for coaching, feedback and praise, plus a short huddle at the start of each shift for expectations and one at the end for reporting.
  why: >-
    It gives a daily opportunity to praise and reward effort and to catch problems, which get added to the training checklist for the next hire.
  anchor: >-
    I schedule one 30 to 45 minute meeting per week for coaching, feedback, and praising
  source: >-
    100m-series-lost-chapters.md, Section D, Keep Your Employees Getting You Leads—The Performance Diamond, lines 4337–4347
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4337"
- id: B-lost-chapters-124
  type: rule
  name: >-
    Have them show you, do not ask if they understand
  statement: >-
    Understanding is verified by having the employee demonstrate the checklist, not by asking whether they understand.
  why: >-
    People are conditioned to say yes out of fear of saying no, and then it gets held against them later.
  applies_when: >-
    A performance drop that looks like a training problem.
  anchor: >-
    later—just have them show you Let them demonstrate the checklist like they did in
  source: >-
    100m-series-lost-chapters.md, Section D, Troubleshooting 2) Training, lines 4400–4405
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4403"
- id: B-lost-chapters-125
  type: rule
  name: >-
    The Best Diamond Hard Feedback Question
  statement: >-
    When an employee’s performance has been dropping for a week or two, the next weekly one-on-one opens with: over the last (length of time) your (task performance) has changed from the norm, what do you think has gotten in the way and how can I help?
  why: >-
    The question sets up a collaborative problem-solving conversation rather than a character-blaming one.
  applies_when: >-
    Performance has been dropping for a little while, a week or two.
  anchor: >-
    “Over the last (length of time) your (task performance) has changed from the norm.
  source: >-
    100m-series-lost-chapters.md, Section D, Pro Tip: The Best Diamond Hard Feedback Question, lines 4436–4449
  confirmations: 1
  authors_caveat: >-
    The author credits the line to Leila.
  anchor_at: "100m-series-lost-chapters.md:4445"
- id: B-lost-chapters-126
  type: rule
  name: >-
    Cost per engaged lead from payroll
  statement: >-
    The cost of advertising done by employees is measured as total payroll divided by total engaged leads, and CAC as that figure times the engaged leads needed per customer.
  why: >-
    Excluding paid media, the cost of outreach and content is almost entirely the money paid to the people doing it.
  applies_when: >-
    Lead-getting employees doing outreach or content rather than paid ads.
  anchor: >-
    ʶ Total Payroll / Total Engaged Leads = Cost per engaged lead
  source: >-
    100m-series-lost-chapters.md, Section D, How to Calculate Returns From Lead-Getting Employees, lines 4477–4491
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4482"
- id: B-lost-chapters-127
  type: rule
  name: >-
    Within 3x industry average CAC is good enough
  statement: >-
    A cost to get a customer within 3x the industry average counts as good enough and attention moves to raising LTGP; above 3x means there is a sales or an advertising problem.
  why: >-
    Past that point the lever with more room is lifetime gross profit, not further efficiency in acquisition.
  applies_when: >-
    Judging acquisition performance (2025); the same rule is given in the Run Paid Ads Part II chapter of $100M Leads.
  anchor: >-
    get a customer is within 3x industry average then you’re doing good enough From there, you
  source: >-
    100m-series-lost-chapters.md, Section D, How To Know Which Employees To Focus On To Maximize Returns, lines 4502–4505
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4503"
- id: B-lost-chapters-128
  type: rule
  name: >-
    One question separates a sales problem from an advertising problem
  statement: >-
    A high CAC is diagnosed by asking whether the engaged leads have the problem you solve and the money to spend: no means an advertising problem, yes but not buying means a sales problem, yes and buying but too few means an advertising problem.
  why: >-
    The answer names which side of the acquisition department to work on.
  applies_when: >-
    CAC is more than 3x industry average.
  anchor: >-
    Do my engaged leads have the problem I solve and the money to spend?
  source: >-
    100m-series-lost-chapters.md, Section D, How To Know Which Employees To Focus On To Maximize Returns, lines 4506–4513
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4507"
- id: B-lost-chapters-129
  type: rule
  name: >-
    Fire on the right diagnosis
  statement: >-
    Salespeople are not replaced over an advertising problem and advertising employees are not replaced over a sales problem.
  why: >-
    The single diagnostic question identifies which employees to focus on.
  anchor: >-
    Don’t fire your sales guy if you’ve got advertising problems And equally, don’t fire your
  source: >-
    100m-series-lost-chapters.md, Section D, How To Know Which Employees To Focus On To Maximize Returns, lines 4514–4516
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4514"
- id: B-lost-chapters-130
  type: rule
  name: >-
    All acquisition costs at a third of lifetime profit
  statement: >-
    All the costs of getting a customer added together stay at or below one third of the profit that customer makes over their lifetime.
  why: >-
    At that ratio the business is in good shape; the worked example runs $1,000 CAC against $4,000 LTGP for an LTGP:CAC of 4:1.
  anchor: >-
    together And as long as they’re at least one third of the profit you make over the lifetime,
  source: >-
    100m-series-lost-chapters.md, Section D, How To Know Which Employees To Focus On To Maximize Returns, lines 4517–4519
  confirmations: 1
  anchor_at: "100m-series-lost-chapters.md:4518"
```
