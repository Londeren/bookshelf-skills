# Улов фазы 1 — $100M Offers (2021) (ярус 1), тип C: разборы (кейсы)

Группа `tier1-offers`, слаг `offers`, ярус 1. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **60** (экстрактор вернул 60, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-offers.md` | 1–2973 | 6 | 60 |

## Как собран файл

Экстрактор C (Application cases) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier1-offers.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier1-offers-C.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

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
- id: C-offers-002
  type: case
  name: >-
    The London tunnel dotted map
  statement: >-
    In the London tunnel system the biggest rise in rider satisfaction came not from faster trains but from a dotted map showing when the next train arrives; the map cost a few million dollars against billions for faster trains.
  demonstrates: >-
    Perception is reality: value rises when the prospect perceives a smaller time delay and less sacrifice, not only when the delay actually shrinks.
  why: >-
    The map decreased the riders' perception of time delay and sacrifice (being bored waiting) more than actually making the trains faster did.
  anchor: >-
    The biggest increase in rider satisfaction (*aka value*) was never from faster trains to decrease wait times. Instead, it was from a simple dotted map that showed them when the next train was coming and how long they had to wait.
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 63
  confirmations: 2
  anchor_at: "100m-offers.md:63"
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
  confirmations: 1
  anchor_at: "100m-offers.md:91"
- id: C-offers-004
  type: case
  name: >-
    Collette's minivan versus the Lamborghini
  statement: >-
    Russell Brunson's wife rejected the claim that she was driven by status and said she would never want a Lamborghini, preferring her minivan; questioned further, she explained the Lamborghini would lower her standing among her mom friends while the minivan showed she was a good mother.
  demonstrates: >-
    The dream outcome that most directly increases the prospect's status is the one they value most; status is relative standing in their own group, not money or luxury.
  why: >-
    It is not about the money, it is about the perceived increase or decrease in relative standing when compared to others socially or professionally.
  anchor: >-
    But, after talking further, she revealed it was because driving a Lamborghini would decrease her status amongst her mom friends, while driving a minivan would show she was a good mother (increase in status).
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 149
  confirmations: 1
  anchor_at: "100m-offers.md:149"
- id: C-offers-005
  type: case
  name: >-
    The golf club copy rewritten through other people's eyes
  statement: >-
    A benefit line is written not as the gain itself but as the reaction of the people around the buyer: the drive increases by 40 yards, and the golf buddies' jaws drop when the ball soars past theirs and they ask what changed.
  demonstrates: >-
    Frame benefits in terms of status gained from the viewpoint of others.
  why: >-
    Talking about how other people will perceive the prospect's achievement makes copy that much more powerful because it connects the dots for them.
  applies_when: >-
    Writing copy for a benefit the prospect's circle can observe.
  anchor: >-
    Example: If you buy this golf club, your drive will increase by 40 yards*.* Your golf buddies' jaws will drop when they see your ball soar 40 yards past theirs . . . they’ll ask you what’s changed . . . only you will know.
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 153
  confirmations: 1
  anchor_at: "100m-offers.md:153"
- id: C-offers-006
  type: case
  name: >-
    The surgeon's 10,000th patient versus their first
  statement: >-
    Asked what they would pay to be a plastic surgeon's 10,000th patient rather than their first, a sane person pays far more and might even ask to be paid for being the first; the surgery itself, and the time it takes, are the same or better in the experienced hands.
  demonstrates: >-
    Perceived likelihood of achievement as a value driver, independent of the work performed.
  why: >-
    The only thing that changes is the perceived likelihood of getting what you want; the more-experienced surgeon has a track record of achieving a result, which incentivizes their desirability.
  anchor: >-
    For example, how much would you pay to be a plastic surgeon’s 10,000th patient versus their first?
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, lines 165–171
  confirmations: 1
  anchor_at: "100m-offers.md:165"
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
  confirmations: 1
  anchor_at: "100m-offers.md:183"
- id: C-offers-008
  type: case
  name: >-
    The fast win built into a weight-loss program
  statement: >-
    Weight-loss customers were introduced to another customer so they had a social benefit immediately, and were given a deliberately more aggressive diet at the start; the bikini body itself may be twelve months away, while higher sex drive, energy and new friends arrive along the way.
  demonstrates: >-
    Short-term experience keeps the client in the game long enough to reach the long-term outcome they actually bought.
  why: >-
    We wanted them to have a big, fast emotional win, so we could get them to commit to the long term; people who experience a victory early on are more likely to continue than those who do not.
  anchor: >-
    For a weight loss customer, we would get them to meet someone else so they immediately had some social benefits from the program, *and* we usually gave them a more aggressive diet in the beginning.
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, lines 189–191
  confirmations: 1
  anchor_at: "100m-offers.md:191"
- id: C-offers-009
  type: case
  name: >-
    Liposuction at $25,000 against a bootcamp at $100/mo
  statement: >-
    Two vehicles for the same body: liposuction with a tummy tuck is done in an afternoon and sells for $25,000, while a bootcamp asking twelve to twenty-four months of work can barely get $100 a month.
  demonstrates: >-
    With the dream outcome held equal, price is set by the remaining three variables — likelihood, time delay, effort and sacrifice.
  why: >-
    When you sell fitness you spend an hour arm-wrestling a client for a fraction of the surgery price, because the perceived likelihood, the time delay and the effort and sacrifice are all high.
  anchor: >-
    This shows just one of the reasons people pay $25,000 for liposuction with a tummy tuck, while people will barely pay $100/mo to join a bootcamp.
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, lines 193–217
  confirmations: 2
  anchor_at: "100m-offers.md:193"
- id: C-offers-010
  type: case
  name: >-
    Fast beats free
  statement: >-
    Markets where a paid option beats a free one on speed alone: pay $50 at the MVD to skip the DMV line and renew privately, Fedex against USPS when it has to be there overnight, Spotify against slow free music, Uber against walking.
  demonstrates: >-
    Time delay as a value driver, and the play to run when competing against free.
  why: >-
    The only thing that beats free is fast; many will always be willing to pay the price for the value of speed, so in a market competing against free you double down on speed.
  applies_when: >-
    When your market contains a free alternative.
  anchor: >-
    A few notable examples: The MVD vs DMV wait in line forever or pay $50 you can skip the line and get your license renewed privately.
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, line 201
  confirmations: 1
  anchor_at: "100m-offers.md:201"
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
- id: C-offers-012
  type: case
  name: >-
    Meditation versus Xanax, scored on all four drivers
  statement: >-
    Two vehicles with the identical dream outcome (relaxation, decreased anxiety, well-being) are scored 0 or 1 on each of the four drivers and summed; the same comparison is run on industries, where supplements ($123B) are twice the size of health clubs ($62B) and people pay $200 for supplements but not $29/mo for a membership.
  demonstrates: >-
    The Value Equation applied as a side-by-side scoring of two vehicles serving one desire.
  why: >-
    Both accomplish the same perceived objectives, but one is perceived as more valuable because it has lower costs in time and effort; that is why Xanax is a multi-billion dollar product and meditation businesses are not.
  anchor: >-
    And that is why Xanax is a multi-billion dollar product while I know of almost no multi-billion dollar meditation businesses . . . value.
  source: >-
    100m-offers.md, ch. 6 Value Offer: The Value Equation, lines 233–245
  confirmations: 2
  anchor_at: "100m-offers.md:239"
- id: C-offers-013
  type: case
  name: >-
    Bonus with scarcity versus bonus with urgency
  statement: >-
    The same bonus is written two ways: scarcity — the bonuses are never for sale anywhere else, or three tickets are left to a $5,000 virtual event; urgency — buy today and the $1,000 bonus is added free to reward action takers. The first two are not constrained by time, the third dies today.
  demonstrates: >-
    Scarcity is a function of quantity and urgency a function of time; bonuses can carry either.
  why: >-
    The bonus with urgency is about them buying today, and if they do not buy today, they lose those bonuses.
  anchor: >-
    Version 2: I have 3 tickets left to my $5,000 virtual event, if you buy this program you can get one of the last 3 tickets as a bonus.
  source: >-
    100m-offers.md, ch. 14 Bonuses, lines 337–347
  confirmations: 1
  anchor_at: "100m-offers.md:341"
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
  confirmations: 1
  anchor_at: "100m-offers.md:353"
- id: C-offers-015
  type: case
  name: >-
    Prestige Labs: the discount and the commission together
  statement: >-
    Gym-owner clients who become sponsored athletes of the sister supplement company give their clients a 30% discount off the main site, and the sponsored athlete is paid 40% of all sales netted after that discount.
  demonstrates: >-
    Negotiating both a group discount and a commission to yourself when a bonus comes from a partner business.
  why: >-
    Their clients get it for 30% less, they get paid for giving away exclusive discounts, and we get customers in exchange for the commission paid — everyone wins.
  anchor: >-
    Our gym owner clients who use our sister supplement company Prestige Labs sponsored athletes get a 30% discount on our products, on top of that, the sponsored athlete gets paid 40% of all sales netted after the applied discount.
  source: >-
    100m-offers.md, ch. 14 Bonuses, line 371
  confirmations: 1
  anchor_at: "100m-offers.md:371"
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
- id: C-offers-019
  type: case
  name: >-
    The rare problem: $10,000 a month versus $5M in profit
  statement: >-
    Two problem statements are set side by side — how do I make $10,000 per month, which many people can solve, against how do I add $5M in profit without adding product lines, which few can; the second was a real engagement that took 60 minutes and produced exactly $5M in bottom line profit by slightly altering the pricing model.
  demonstrates: >-
    Price comes from the rarity of solvers multiplied by the value provided; a specialized problem makes perceived supply equal one.
  why: >-
    By the nature of the problem being specialized there are very few people who can solve it, and value and rarity compound to create truly breathtaking profits.
  anchor: >-
    *How can I add $5M in profit without adding any extra product* *lines to my business? (This was a real project that took me 60min and resulted in exactly $5M in bottom line profit by slightly altering the pricing model of the business).*
  source: >-
    100m-offers.md, ch. 12 Scarcity, lines 519–527
  confirmations: 1
  anchor_at: "100m-offers.md:523"
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
  confirmations: 1
  anchor_at: "100m-offers.md:563"
- id: C-offers-021
  type: case
  name: >-
    Chanel's one or two pieces per store
  statement: >-
    Chanel sends only one or two of each piece to each store, so every store carries a different selection and every item is the last or second to last in stock.
  demonstrates: >-
    Engineered scarcity as a pricing lever, sustained over decades.
  why: >-
    This allows them to price far above market and turn buying impulses into purchases, which is how the brand has held insane margins for over a century.
  anchor: >-
    They send only 1-2 of each piece to each store so every store has a different selection and every item is the last or second to last item in stock.
  source: >-
    100m-offers.md, ch. 12 Scarcity, line 569
  confirmations: 1
  anchor_at: "100m-offers.md:569"
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
- id: C-offers-025
  type: case
  name: >-
    Bad guarantee versus better guarantee
  statement: >-
    Bad: we will get you 20 clients guaranteed. Better: you will get 20 clients in your first 30 days, or we give you your money back plus your advertising dollars spent with us.
  demonstrates: >-
    The conditional structure — if you do not get X result in Y time period, we will Z — and the or-what clause that gives a guarantee teeth.
  why: >-
    Without the or what portion of the guarantee, it sounds weak and diluted, which is what most marketers do.
  anchor: >-
    Better example: You will get 20 clients in your first 30 days, or we give you your money back + your advertising dollars spent with us. This is a simple, but strong guarantee.
  source: >-
    100m-offers.md, ch. 15 Guarantees, lines 662–672
  confirmations: 1
  anchor_at: "100m-offers.md:672"
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
- id: C-offers-027
  type: case
  name: >-
    From Satisfaction Guarantee to the Club a Baby Seal Guarantee
  statement: >-
    The same 30-day guarantee is named three ways: bad — 30 Day Money Back Satisfaction Guarantee; good — in 30 days, if you would not jump into shark-infested waters to get our product back, we return every dollar; great — the famous Club a Baby Seal Guarantee.
  demonstrates: >-
    Naming a guarantee with creative imagery instead of vanilla words like satisfaction.
  why: >-
    If you are going to give a guarantee, spice it up; describe it more strongly instead of using a vanilla word.
  anchor: >-
    **Creative Imagery Example #2** (Great): You’ll get our famous “Club a Baby SealGuarantee”After 30 days of using our services, if you wouldn’t club a baby seal to stay on as a customer, you don’t have to pay a penny.
  source: >-
    100m-offers.md, ch. 15 Guarantees, lines 714–722
  confirmations: 1
  anchor_at: "100m-offers.md:722"
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
  confirmations: 1
  anchor_at: "100m-offers.md:728"
- id: C-offers-029
  type: case
  name: >-
    The best-case / worst-case close
  statement: >-
    The guarantee is closed by laying out both ends: best case you get the body of your dreams and we put your money towards staying with us; worst case you tell me I suck, I write you a check and you got six weeks of free training; both are risk free, and the only thing guaranteed not to help is walking out today. Two people took it out of 4,000 sales in three and a half years.
  demonstrates: >-
    Pairing a guarantee with a close that makes both outcomes acceptable and leaves not buying as the only losing option.
  why: >-
    If you are good at what you do, a guarantee like this pushes a lot of people over the edge; that line made a lot of money and was almost never taken up.
  anchor: >-
    “Best case you get the body of your dreams and we give you all your money towards staying with us to hit your long-term goal. Worst case you tell me I suck, I write you a check, and you get six weeks of free training. Both options are risk free.
  source: >-
    100m-offers.md, ch. 15 Guarantees, line 730
  confirmations: 1
  anchor_at: "100m-offers.md:730"
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
- id: C-offers-031
  type: case
  name: >-
    Alex will personally work with you — with contingencies
  statement: >-
    A personal service guarantee voiced by a salesperson (Alex will personally work with you until your offer converts) is made survivable by contingencies: they must already have spent $10,000 on their existing offer using our structure, the offer must have been for lead generation, and it must have been a free offer.
  demonstrates: >-
    The personal service guarantee, and the rule that the strongest guarantees must carry conditions the client controls.
  why: >-
    Those stipulations are things that would make it unlikely the client would not succeed; without them the guarantee would work but would also be a nightmare.
  applies_when: >-
    When the founder is edified enough for their personal involvement to be the strongest promise available.
  anchor: >-
    So I would probably put contingencies like, “Provided you've already spent $10,000 on your existing offer using our structure, the offer you ran was for lead generation, and it was a free offer.
  source: >-
    100m-offers.md, ch. 15 Guarantees, lines 771–777
  confirmations: 1
  anchor_at: "100m-offers.md:777"
- id: C-offers-032
  type: case
  name: >-
    All sales are final, with the reason why
  statement: >-
    The anti-guarantee is worded as a damaging admission: we are going to show you the proprietary process we use right now to generate leads, our funnels, ads and metrics, we are exposing the inner workings of our business, and as a result all sales are final.
  demonstrates: >-
    The anti-guarantee — stating all sales are final and owning the position with a creative reason why.
  why: >-
    It implies the client will use it and see immense benefit, exposing the business to vulnerability; since it is standard to have some sort of guarantee, not having one is attention-worthy, and the more real exposure you show, the more effective it is.
  applies_when: >-
    Items that are consumable or massively diminish in value once given — a line of code, a script, anything easy to steal once seen.
  anchor: >-
    “We are going to show you our proprietary process that we are using right now to generate leads in our business. Our funnels, ads, and metrics. We’re going to be exposing the inner workings of our business, as a result, all sales are final.”
  source: >-
    100m-offers.md, ch. 15 Guarantees, lines 811–817
  confirmations: 1
  anchor_at: "100m-offers.md:817"
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
- id: C-offers-035
  type: case
  name: >-
    The blind wine tasting
  statement: >-
    Consumers rated a low-priced, a medium-priced and an expensive wine with the prices visible and ranked them in price order; all three glasses held the same wine, yet tasters reported a wide discrepancy between the high-priced and the cheap one.
  demonstrates: >-
    Raising the price raises the value the consumer actually receives, with nothing else about the product changed.
  why: >-
    Raising your prices can directly enhance the value you provide; the higher the price, the more allure the product has — people want to buy expensive things, they just need a reason.
  anchor: >-
    What the tasters didn’t know is that the researchers gave them the exact same wine all three times. Yet, the tasters reported a wide discrepancy between the “high priced” wine and the “cheap” wine.
  source: >-
    100m-offers.md, ch. 5 Pricing: Charge What It’s Worth, lines 1204–1210
  confirmations: 1
  anchor_at: "100m-offers.md:1208"
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
- id: C-offers-038
  type: case
  name: >-
    The charity that cut its tickets and raised the price
  statement: >-
    A fundraiser raised the ticket from $15,000 to $25,000 and cut the number of tickets sold in a year of higher demand; it took in an extra million dollars before the event even started, raised nearly $5,400,000 from 100 people ($54,000 per head), and auctioned each item as one of a kind that could never be bought again.
  demonstrates: >-
    When demand increases, cut supply; scarcity, urgency and bonuses raise price with the product unchanged.
  why: >-
    People want what they cannot have, what other people want, and what only a select few have access to; the products remained unchanged, yet in that setting an item that would not sell for $10,000 elsewhere sold for $100,000.
  anchor: >-
    They had raised an *extra* one million dollars that nightbefore the event had even started by cutting the supply of tickets *and* raising the prices.
  source: >-
    100m-offers.md, ch. 11 Enhancing The Offer, lines 1502–1512
  confirmations: 1
  anchor_at: "100m-offers.md:1510"
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
  confirmations: 1
  anchor_at: "100m-offers.md:1535"
- id: C-offers-040
  type: case
  name: >-
    The hot dog stand and the starving crowd
  statement: >-
    Asked which single advantage they would take for a hotdog stand, students name location, quality, low prices and best taste; the professor answers a starving crowd. With the worst hot dogs, terrible prices and a terrible location, the only stand in town when the college football game breaks out sells out.
  demonstrates: >-
    Starving Crowd (market) > Offer Strength > Persuasion Skills.
  why: >-
    If there is a ton of demand for a solution you can be mediocre at business, have a terrible offer and no ability to persuade, and still make money — as with toilet paper selling for $100 a roll at the start of Covid-19.
  anchor: >-
    You could have the worst hot dogs, terrible prices, and be in a terrible location, but if you’re the only hot dog stand in town and the local college football game breaks out, you’re going to sell out.
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market -- A Starving Crowd, lines 1589–1601
  confirmations: 1
  anchor_at: "100m-offers.md:1597"
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
- id: C-offers-042
  type: case
  name: >-
    The resume service sold to the unemployed
  statement: >-
    A friend with a very good system for improving resumes and getting interviews could not get anyone to pay, because his market was the unemployed — a market he had picked for being easy to target, in massive pain, plentiful and constantly refreshed.
  demonstrates: >-
    Purchasing power as one of the four market indicators, and that pain plus targeting are not enough.
  why: >-
    Your audience needs to be able to afford the service you are charging them for; make sure the targets have the money, or access to the money, needed at the prices you require.
  anchor: >-
    But try as he did, he just could not get people to pay for his services. Why? Because they were all unemployed!
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market -- A Starving Crowd, lines 1645–1651
  confirmations: 1
  anchor_at: "100m-offers.md:1647"
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
- id: C-offers-044
  type: case
  name: >-
    The avatar written down to four conditions
  statement: >-
    The chosen avatar is a microgym owner with about 100 members, a signed lease, at least one employee, who wants to help clients lose weight; everyone outside it — personal trainers, online coaches — is turned away even though they could have been helped.
  demonstrates: >-
    Commit to the niche: specificity of the avatar rather than small business owners or anyone who will pay me.
  why: >-
    Knowing exactly who the product was for maintained product focus and high converting messaging, and made it clear at all times whose problems were being solved.
  anchor: >-
    In my instance, I decided on a microgym owner with ~100 members, a signed lease, at least one employee, and wanted to help clients lose weight.
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market -- A Starving Crowd, lines 1713–1717
  confirmations: 1
  anchor_at: "100m-offers.md:1713"
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
  confirmations: 1
  anchor_at: "100m-offers.md:1737"
- id: C-offers-046
  type: case
  name: >-
    Generic weight loss at $19, shift-nurses at $1997
  statement: >-
    A fitness program for generic weight loss is priced at $19 while the same core program — eat less, move more — designed and marketed only to shift-nurses is priced at $1997.
  demonstrates: >-
    Niching the same core product multiplies the price it can carry.
  why: >-
    The core of the program is likely similar; what changes is that it has been applied to one avatar, which is what the market pays for.
  anchor: >-
    That’s why a fitness program for generic weight loss might be priced at only $19 while a fitness program designed and marketed only to shift-nurses might be priced at $1997
  source: >-
    100m-offers.md, ch. 4 Pricing: Finding The Right Market -- A Starving Crowd, line 1743
  confirmations: 1
  anchor_at: "100m-offers.md:1743"
- id: C-offers-047
  type: case
  name: >-
    Free Six-Week Stress Release Challenge versus Float Tank Center Session
  statement: >-
    The same thing named two ways — a Free Six-Week Stress Release Challenge and a Float Tank Center Session — and the reader is far more likely to respond to the first.
  demonstrates: >-
    Naming decides whether an offer is found and acted on, with the offer itself unchanged.
  why: >-
    A Grand Slam Offer will not make money if no one finds out about it; the goal is that on hearing the offer the ideal prospect is interested enough to take action.
  anchor: >-
    Say you see a “Free Six-Week Stress Release Challenge” and a “Float Tank Center Session.” While they may be the same thing, just named differently, you’re much more likely to respond to the first.
  source: >-
    100m-offers.md, ch. 16 Naming, line 1965
  confirmations: 1
  anchor_at: "100m-offers.md:1965"
- id: C-offers-048
  type: case
  name: >-
    Named offers across three industries
  statement: >-
    Worked names show the M-A-G-I-C components combined three to five at a time: Free Six-Week Lean-By-Halloween Challenge; 88% Off 12-Week Bikini Blueprint; Lakeway Moms - $1,500 Off Your Kids Braces; Back Sore No More! 90 Day Rapid Healing Intensive (81% off!); 5 Clients in 5 Days Blueprint; Fill Your Gym in 30 Days (Free!).
  demonstrates: >-
    The M-A-G-I-C naming formula — magnetic reason why, avatar, goal, time interval, container word — assembled into real names.
  why: >-
    Using three to five of the power components creates something unique and desirable that separates you from the competitive field and gets clicks and engagement; the shorter and punchier the better.
  applies_when: >-
    Naming an offer, and equally each sub-item and bonus in the stack.
  anchor: >-
    * Back Sore No More! 90 Day Rapid Healing Intensive (81% off!)
  source: >-
    100m-offers.md, ch. 16 Naming, lines 2049–2079
  confirmations: 1
  anchor_at: "100m-offers.md:2067"
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
- id: C-offers-057
  type: case
  name: >-
    The brick exercise
  statement: >-
    Given 120 seconds to list different uses of a brick, most readers stop early; three questions then unlock the rest — how big is the brick, what is it made of, how is it shaped — and the author's list runs to paperweight, door stop, fish home, plant holder with dirt in the holes, painted trophy, window breaker, resistance weight, pen holder, lego, plastic flotation device, gold payment and store of value, jumbo-brick seat.
  demonstrates: >-
    Divergent rather than convergent thinking as the mode in which an offer is built: many right answers to one problem, one far more right than the others.
  why: >-
    Life pays you for your ability to solve using a divergent thought process; every offer has building blocks, and the goal is to think of as many easy ways to combine them to provide value.
  applies_when: >-
    Before listing solutions and delivery vehicles for an offer.
  anchor: >-
    . . . What is the brick made of? Plastic, Gold, Clay, Wood, Metal?
  source: >-
    100m-offers.md, ch. 8 Value Offer: The Thought Process, lines 2694–2790
  confirmations: 1
  anchor_at: "100m-offers.md:2760"
- id: C-offers-058
  type: case
  name: >-
    Selling the vacation, not the plane flight
  statement: >-
    Unable to sell a $99/mo bootcamp against a $29/mo gym, he stopped selling the membership and defined the dream outcome instead: lose 20lbs in 6 weeks — a big dream outcome with a decreased time delay.
  demonstrates: >-
    Step #1, Identify Dream Outcome — state the destination and the experience, not the vehicle.
  why: >-
    No one wants a membership; they want to lose weight, so the dream outcome has to be them arriving at their destination and what they would like to experience.
  anchor: >-
    Note: I wasn't selling my membership anymore. I wasn’t selling the plane flight. *I was* *selling the vacation.*
  source: >-
    100m-offers.md, ch. 9 Creating Your Grand Slam Offer Part I, lines 2856–2866
  confirmations: 1
  anchor_at: "100m-offers.md:2866"
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
```
