# Улов фазы 1 — $100M Money Models (2025) (ярус 1), тип C: разборы (кейсы)

Группа `tier1-money-models`, слаг `money-models`, ярус 1. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **83** (экстрактор вернул 83, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-money-models.md` | 1–6495 | 7 | 83 |

## Как собран файл

Экстрактор C (Application cases) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier1-money-models.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier1-money-models-C.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: C-money-models-001
  type: case
  name: >-
    The storage facility where a free month of storage costs $127
  statement: >-
    A storage owner advertises the first month free and then sells, in order, a heavy-duty lock at $47, boxes with tape, labels and markers, an affiliate kickback on a local mover plus dollies and hand trucks for a fee, an insurance upgrade from the free $500 cover to $100,000 for an extra $10 per month available only with his special lock, and one size up on the unit because everyone rents too small; the free month averages $127 of revenue.
  why: >-
    Every step of actually using a storage unit creates a problem the owner already stocks the solution to, so each offer lands at the moment the customer feels the need.
  demonstrates: >-
    A Money Model as a sequence of offers: find every opportunity to solve the customer's problem and then offer to solve it.
  anchor: >-
    "Good morning, Judy. *How much does a free month of storage cost?"*
  source: >-
    100m-money-models.md, Start Here, line 405
  confirmations: 1
  anchor_at: "100m-money-models.md:405"
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
- id: C-money-models-003
  type: case
  name: >-
    Rolling the $600 challenge fee into a year of membership
  statement: >-
    A few weeks into the program customers are told they can have their $600 back as credit if they sign up for a year; two-thirds of the sign-ups convert, so the model ends with a full gym and $20,000 of monthly memberships for $3,000 down, all inside thirty days, and is then repeated at the next location.
  demonstrates: >-
    Rolling the price of the Attraction Offer forward into a longer commitment (the Rollover Upsell) as the back end of a money model.
  anchor: >-
    *I grinned ear-to-ear.* "Yea! A few weeks later, I tell them they can
  source: >-
    100m-money-models.md, Start Here, line 564
  confirmations: 1
  anchor_at: "100m-money-models.md:564"
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
  confirmations: 2
  anchor_at: "100m-money-models.md:736"
- id: C-money-models-005
  type: case
  name: >-
    Each rental car offer named as the problem it solved
  statement: >-
    Hormozi breaks the rental sequence back into problems: big man in a small car answered by a larger vehicle, late checkout answered by keeping the vehicle longer, worry about dinging the car answered by insurance, and the risk of missing the flight answered by prepaying for gas.
  why: >-
    Naming the problem behind each offer is what makes the sequence transferable: the offers are not add-ons, they are solutions timed to the moment the customer realises the need.
  demonstrates: >-
    Offers are built from the problems the previous offer creates, not from the product catalogue.
  anchor: >-
    ● She solved my 'big man in a small car' problem by *offering* a vehicle
  source: >-
    100m-money-models.md, Section I: What's A Money Model?, line 771
  confirmations: 1
  anchor_at: "100m-money-models.md:771"
- id: C-money-models-006
  type: case
  name: >-
    Danny's client invents Win Your Money Back
  statement: >-
    A prospect who refused to buy proposed paying $500 for eight weeks of training, getting the money back if he hit his goal, in exchange for the gym being allowed to use his results in marketing; he hit the goal, spent the winnings on more training instead of taking cash, and his before and after pictures produced thirteen referrals.
  why: >-
    Winners stay customers when there is something else to buy, and the results they produce advertise the business for free.
  demonstrates: >-
    The Win Your Money Back Offer, and the rule that the money comes from the people who succeed rather than from the ones who fail.
  anchor: >-
    me for eight weeks. And if I hit my goal, I get my money back. But in
  source: >-
    100m-money-models.md, ch. Win Your Money Back, line 1099
  confirmations: 1
  anchor_at: "100m-money-models.md:1099"
- id: C-money-models-007
  type: case
  name: >-
    Put 1,000,000 Miles On Your Car, And Get A Free Car
  statement: >-
    Buy a new car, drive it a million miles, turn it in, take pictures and appear in a press release, and the whole original purchase price is credited towards the next car; Hormozi notes this was an actual offer.
  demonstrates: >-
    Win Your Money Back applied to a physical product, with criteria that are easy to track and that advertise the business.
  anchor: >-
    We'll credit all your original purchase price towards your next car.
  source: >-
    100m-money-models.md, ch. Win Your Money Back, line 1218
  confirmations: 1
  anchor_at: "100m-money-models.md:1218"
- id: C-money-models-008
  type: case
  name: >-
    Applying $600 of winnings as $50 a month for a year
  statement: >-
    On a $200 per month product a customer who wins $600 of credit is not given three free months up front; the $600 is spread over twelve months as a $50 monthly discount, so they keep paying $150 a month.
  why: >-
    People fall off if they do not pay something, so a discount stretched over the long haul keeps them engaged over the long haul and keeps skin in the game.
  applies_when: >-
    Whenever a customer wins their money back or holds store credit.
  demonstrates: >-
    How to apply store credit; the Rollover Upsell spread over time rather than given up front.
  anchor: >-
    ○ They now pay: \$200 per month---\$50 discount = \$150 per month
  source: >-
    100m-money-models.md, ch. Win Your Money Back, line 1316
  confirmations: 2
  anchor_at: "100m-money-models.md:1316"
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
  confirmations: 1
  anchor_at: "100m-money-models.md:1340"
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
  confirmations: 1
  anchor_at: "100m-money-models.md:1358"
- id: C-money-models-011
  type: case
  name: >-
    At the end of the program, let the losers win
  statement: >-
    For someone who refused the first upsell and then failed the challenge, the seller acts as if they won: they met our goal, which was finishing what they started, so the entire deposit is credited towards staying long term.
  demonstrates: >-
    Turning a failed program into a second upsell rather than a refund.
  anchor: >-
    *"Don't worry about it. You started. That\'s the biggest victory of all.
  source: >-
    100m-money-models.md, ch. Win Your Money Back, line 1369
  confirmations: 1
  anchor_at: "100m-money-models.md:1369"
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
- id: C-money-models-014
  type: case
  name: >-
    Four Grand Prize and promotional offer pairs
  statement: >-
    Dentist: free invisible braces at $6,000 retail against a $2,000 gift card for braces. Physical product: a free year of organic dog food at $1,000 retail against a $300 gift card usable only with a one-year subscription. Services: a free 1-year package at $5,000 against a $2,000 voucher towards a 1-year agreement; consulting: a $12,000 16-week turnaround against a $6,000 partial scholarship.
  demonstrates: >-
    Picking as the Grand Prize the thing you want everyone to buy, and building the promotional offer as its discounted twin.
  anchor: >-
    Offer: \$300 gift card for dog food *only useable with a one-year
  source: >-
    100m-money-models.md, ch. Giveaways, line 1620
  confirmations: 1
  anchor_at: "100m-money-models.md:1620"
- id: C-money-models-015
  type: case
  name: >-
    The giveaway that failed because the prize was not grand
  statement: >-
    A portfolio company gave away tickets to its own event and barely got any interest; rerun with a $50,000 bundle of equipment from a well-known industry supplier plus a year of their core product, the same giveaway crushed.
  why: >-
    Giveaway explains itself, so when nobody bites the prize is the problem: it has to be grand, and grand for that audience.
  demonstrates: >-
    Diagnosing a failed giveaway by the size of the Grand Prize rather than by the advertising.
  anchor: >-
    with a \$50,000 bundle of equipment from a well-known industry supplier
  source: >-
    100m-money-models.md, ch. Giveaways, line 1657
  confirmations: 1
  anchor_at: "100m-money-models.md:1657"
- id: C-money-models-016
  type: case
  name: >-
    Two grand prizes for twice the leads
  statement: >-
    Everyone is told that if someone they refer wins the grand prize, they win one too, which gives entrants endless entries through referring friends; Hormozi ran this for Skool.com.
  why: >-
    Referrers become invested in the success of the people they refer, which keeps the quality of the entries high while doubling the leads.
  demonstrates: >-
    Building a referral mechanism into a Giveaway Offer.
  anchor: >-
    someone they refer wins the grand prize, they win one too. That way,
  source: >-
    100m-money-models.md, ch. Giveaways, line 1669
  confirmations: 1
  anchor_at: "100m-money-models.md:1669"
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
- id: C-money-models-018
  type: case
  name: >-
    Free once a week against the $399 Ultimate version
  statement: >-
    Two options were offered: a free version with one session per week, and an Ultimate version at $399 with unlimited sessions, 1-1 coaching, more personalisation and a guarantee that they get results or repeat the program free; about eight out of ten people took the $399 option.
  demonstrates: >-
    A Decoy Offer where the contrast, and especially the guarantee, carries the premium version.
  anchor: >-
    "We got about eight out of ten people to take the \$399 option. We're
  source: >-
    100m-money-models.md, ch. Decoy Offer, line 1849
  confirmations: 1
  anchor_at: "100m-money-models.md:1849"
- id: C-money-models-019
  type: case
  name: >-
    The gym decoy and premium pair spelled out
  statement: >-
    Attraction offer: Free 21-Day Transformation or $21 21-Day Transformation. Decoy: workouts in a Skool.com group once a day, a general nutrition plan, recordings, no support, no guarantee. Premium: unlimited workouts, a personalised nutrition plan, 1-1 accountability, results guaranteed or another 21 days free.
  why: >-
    The value of the premium option comes from the size of its difference with the decoy, so the decoy is stripped as basic as is reasonable and the guarantee is removed from it.
  demonstrates: >-
    How to build the decoy by removing components, personalisation and guarantees from the premium offer.
  anchor: >-
    *Attraction Offer*: "Free 21-Day Transformation" **OR** "\$21 21-Day
  source: >-
    100m-money-models.md, ch. Decoy Offer, line 1913
  confirmations: 1
  anchor_at: "100m-money-models.md:1913"
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
- id: C-money-models-021
  type: case
  name: >-
    The t-shirt reframe
  statement: >-
    Three t-shirts at $10 each is $30, or one t-shirt at $30 with two given away free: the same price with far more free stuff. With a discount added, three shirts at $6.67 is $20, or one shirt at $20 with two free.
  demonstrates: >-
    Turning a Discount Offer into a stronger Free Offer by selling more than one thing at once.
  anchor: >-
    price of more stuff. For example, I could sell three t-shirts for \$10
  source: >-
    100m-money-models.md, ch. Buy X Get Y Free, line 2100
  confirmations: 1
  anchor_at: "100m-money-models.md:2100"
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
  confirmations: 2
  anchor_at: "100m-money-models.md:2131"
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
  confirmations: 1
  anchor_at: "100m-money-models.md:2142"
- id: C-money-models-024
  type: case
  name: >-
    One free shirt against three free pairs of socks
  statement: >-
    For the same cost as giving away one shirt, three pairs of socks can be given, so Buy 1 Shirt Get 1 Shirt Free is tested against Buy 1 Shirt Get 3 Socks Free; people still see one thing bought and three things free.
  demonstrates: >-
    The free things can differ from the paid things, and more cheap free things can beat fewer expensive ones.
  anchor: >-
    pairs of socks. I'd probably test "Buy 1 Shirt Get 1 Shirt Free" against
  source: >-
    100m-money-models.md, ch. Buy X Get Y Free, line 2198
  confirmations: 1
  anchor_at: "100m-money-models.md:2198"
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
  confirmations: 1
  anchor_at: "100m-money-models.md:2313"
- id: C-money-models-026
  type: case
  name: >-
    Trim Your Hedges For Free
  statement: >-
    Pay later is $0 for the lawn cut and hedges then $599 afterwards; pay now is $369 for the lawn cut, hedges and a lawn treatment; the upsell is $199 per month of lawncare. The rep makes the estimate at the house, offers both options, and upsells once the work is done.
  demonstrates: >-
    The pay-later, pay-now and upsell slots of a Pay Less Now or Pay More Later offer in a local service.
  anchor: >-
    Pay Later: \$0 Lawn Cut + Hedges then \$599 after.
  source: >-
    100m-money-models.md, ch. Pay Less Now or Pay More Later, line 2381
  confirmations: 1
  anchor_at: "100m-money-models.md:2381"
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
- id: C-money-models-030
  type: case
  name: >-
    Three Classic Upsell chains with their one-line reasons
  statement: >-
    Car wash upsold to sealant with you're not gonna wanna do the wash without sealant; bicycle upsold to helmet, then lights, then puncture-resistant tires with you can't have a bike without a helmet; an exercise course upsold to a nutrition course with you can't out-exercise a bad diet.
  demonstrates: >-
    The Classic Upsell across a local service, a physical product and a digital product, each carried by the problem the first purchase creates.
  anchor: >-
    *You can't out-exercise a bad diet...so you're gonna want our course on
  source: >-
    100m-money-models.md, ch. The Classic Upsell, line 2803
  confirmations: 1
  anchor_at: "100m-money-models.md:2803"
- id: C-money-models-031
  type: case
  name: >-
    The art studio that started charging for what it gave away
  statement: >-
    An art studio used to replace damaged portraits at no charge; told to ask customers whether they would pay an extra 10% for that cover, 30% of customers now buy what the studio used to give away free.
  demonstrates: >-
    Charging 5-50% extra for guarantees, warranties and insurance instead of including them.
  anchor: >-
    them to start asking customers if they would pay an extra 10% for it.
  source: >-
    100m-money-models.md, ch. The Classic Upsell, line 2896
  confirmations: 1
  anchor_at: "100m-money-models.md:2896"
- id: C-money-models-032
  type: case
  name: >-
    Chocolate or vanilla: the A/B upsell discovered
  statement: >-
    After nineteen nutrition consults with no sales, the pitch was dropped for a question about the customer's own breakfast shake, chocolate or vanilla, which sold immediately; the next item was asked as kiwi or strawberry lemonade with a stated preference attached, and the close was do you just want to use the card we have on file. The next twenty customers in a row bought.
  why: >-
    Asking which product they prefer instead of whether they want the product removes the option of not buying; referring to the card they already gave removes the hidden costs of paying.
  demonstrates: >-
    The A/B Upsell and the Card On File close.
  anchor: >-
    about science stuff, I just asked "You've got a protein shake for
  source: >-
    100m-money-models.md, ch. Menu Upsell, line 2962
  confirmations: 1
  anchor_at: "100m-money-models.md:2962"
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
- id: C-money-models-035
  type: case
  name: >-
    The dog food Menu Upsell in four moves
  statement: >-
    Unsell the small bag, the puppy food and the separate vitamins already contained in the food; prescribe a joint chew at each meal and a heartworm wafer every 90 days, and book next month's visit now; A/B on beef or chicken flavour; close with wanna just use the card on file.
  demonstrates: >-
    The four Menu Upsell tactics in order: Unselling, Prescription Upselling, A/B Upselling, Card On File.
  anchor: >-
    ● *A/B:* So does your dog prefer beef or chicken flavor?
  source: >-
    100m-money-models.md, ch. Menu Upsell, line 3169
  confirmations: 2
  anchor_at: "100m-money-models.md:3169"
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
- id: C-money-models-037
  type: case
  name: >-
    Three Anchor Upsell pairs with the primary feature held constant
  statement: >-
    Lawn care: the owner's cell number, fancy mulch, natural pest control and bi-weekly maintenance at $1,000 a week against the team's number, generic mulch, normal pest control and the same bi-weekly maintenance at $200. A painting: protective packaging, 20-year insurance and gift wrap at $1,000 against normal packaging, 1-year insurance and a sticker at $200. A newsletter: all back issues plus new issues 24 hours early at $199 a month against new issues on time at $19.
  why: >-
    Only secondary features are changed, so the customer keeps the primary feature and gets a far better deal; and some customers still buy the premium version.
  demonstrates: >-
    Making the premium offer 5-10x the price while keeping the same core functions in the main offer.
  anchor: >-
    *Premium Anchor:* All previous issues + new issues + 24hrs early =
  source: >-
    100m-money-models.md, ch. Anchor Upsell, line 3391
  confirmations: 1
  anchor_at: "100m-money-models.md:3391"
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
  confirmations: 1
  anchor_at: "100m-money-models.md:3530"
- id: C-money-models-039
  type: case
  name: >-
    The chiropractor winback call
  statement: >-
    Reach out to patients six months since their last purchase, look at their purchase history, and offer to apply some or all of it towards something more expensive: the call opens with wanting to give them their money back, asks how the back pain is going, and credits $500 towards staying pain-free for good.
  demonstrates: >-
    The Rollover Upsell used to re-engage customers who left a while ago, with the credit given up front.
  anchor: >-
    Ex: *"Hi Mrs. Banks, I wanted to give you your money back, do you have a
  source: >-
    100m-money-models.md, ch. Rollover Upsell, line 3589
  confirmations: 1
  anchor_at: "100m-money-models.md:3589"
- id: C-money-models-040
  type: case
  name: >-
    The dentist rescuing his own upset customer
  statement: >-
    A customer paid $200 for a cleaning and did not think their teeth got whiter; they are told they need more to get more, and the $200 is credited towards a whitening package of multiple sessions, an at-home kit and several deep cleanings.
  demonstrates: >-
    Doing a Rollover Upsell before refunding, as a better alternative to a refund.
  anchor: >-
    The person pays \$200 for teeth cleaning but doesn\'t think their teeth
  source: >-
    100m-money-models.md, ch. Rollover Upsell, line 3599
  confirmations: 1
  anchor_at: "100m-money-models.md:3599"
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
- id: C-money-models-042
  type: case
  name: >-
    Spreading a first purchase over a twelve-month membership
  statement: >-
    Someone buys a small block of service or membership time, and the entire amount is immediately offered as credit towards twelve months: a $600 first purchase becomes a $50 per month rollover discount for twelve months.
  demonstrates: >-
    The how of a Rollover Upsell: full purchase price, spread over the longer term rather than given up front.
  anchor: >-
    a \$600 first purchase makes a \$50 per month rollover discount for 12
  source: >-
    100m-money-models.md, ch. Rollover Upsell, line 3626
  confirmations: 2
  anchor_at: "100m-money-models.md:3626"
- id: C-money-models-043
  type: case
  name: >-
    The winback video campaign
  statement: >-
    Personalised videos were recorded for 200 past customers offering them $4,000 of credit to return; about 20% took the offer, and one day of recording produced roughly $1,900,000 of extra annual revenue.
  demonstrates: >-
    Previous customers are still customers: decide how much of their past spend you will roll over, and actually make the offer.
  anchor: >-
    personalized videos for 200 past customers offering them \$4,000 of
  source: >-
    100m-money-models.md, ch. Rollover Upsell, line 3648
  confirmations: 1
  anchor_at: "100m-money-models.md:3648"
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
- id: C-money-models-046
  type: case
  name: >-
    The 1-10 temperature check mid-downsell
  statement: >-
    After the half-down option fails, the seller pauses and asks on a scale of 1 to 10 how badly they want to do this; 8 or above keeps the payment plan ladder going with don't worry, we're gonna figure out a way to make this happen, while 7 or below is answered with why not a 10 and a move to selling something different.
  why: >-
    No payment plan will satisfy a customer who does not want the thing, so effort stops going into the wrong sale.
  demonstrates: >-
    Step 4 of the Payment Plan Downsell, reused as the temperature check after two Feature Downsells.
  anchor: >-
    Real quick. I want to make sure. On a scale from 1--10 how bad do you
  source: >-
    100m-money-models.md, ch. Payment Plan Downsells, line 3994
  confirmations: 2
  anchor_at: "100m-money-models.md:3994"
- id: C-money-models-047
  type: case
  name: >-
    Seesaw downselling
  statement: >-
    A shorter version for less experienced sellers: ask whether they would rather have giant monthly payments or tiny ones, they say tiny, then state the normal price and the big prepay discount with zero monthly payments; if they still cannot afford it, adjust the down payment until the monthly rate suits them, since a bigger down payment lowers it.
  why: >-
    It frames the payment plan as the negative option and highlights the benefit of prepaying, and it turns the sale into a team effort rather than a negotiation.
  demonstrates: >-
    A compressed Payment Plan Downsell that still shifts from paid-in-full towards equal payments.
  anchor: >-
    process. Instead of asking for the full amount, just ask *"Would you
  source: >-
    100m-money-models.md, ch. Payment Plan Downsells, line 4024
  confirmations: 1
  anchor_at: "100m-money-models.md:4024"
- id: C-money-models-048
  type: case
  name: >-
    Ten leads, three sales, and three more from the downsell
  statement: >-
    Of ten leads three buy; with a downsell three more buy, for six, so the up-front cash from the first three is kept and the payments from the second three are added. The check on whether payment plans worked is that the close rate rises while the same percentage of appointments still pays in full.
  why: >-
    Payment plans lose the most money when people who would have paid in full take a plan and cancel early, so the count of paid-in-fulls is the thing to watch.
  demonstrates: >-
    How to tell whether a downsell added customers or only converted paid-in-fulls into plans.
  anchor: >-
    Ex: If I talk to ten leads, I might sell three. If I have a downsell, I
  source: >-
    100m-money-models.md, ch. Payment Plan Downsells, line 4063
  confirmations: 1
  anchor_at: "100m-money-models.md:4063"
- id: C-money-models-049
  type: case
  name: >-
    The HR software that made onboarding free if you did the training
  statement: >-
    The vendor took Leila's card and told her onboarding was free if she completed their training and payable if she skipped it; she did the training, learned the complicated software, and stayed with the vendor rather than learn anyone else's.
  why: >-
    The penalty forced her to use the product, which is what made her a long-term customer; the terms made her a perfect fit for the next offer.
  demonstrates: >-
    Trial With Penalty: customers pay only if they don't meet the terms, the mirror image of Win Your Money Back.
  anchor: >-
    "They said if I did their training I'd get free onboarding. But, if I
  source: >-
    100m-money-models.md, ch. Trial With Penalty, line 4169
  confirmations: 1
  anchor_at: "100m-money-models.md:4169"
- id: C-money-models-050
  type: case
  name: >-
    The trial downsell that doubles the customers
  statement: >-
    Three of ten close on the Attraction Offer; another four are downsold onto a Trial With Penalty; after the trial finishes three of those are upsold, taking three sales to six.
  demonstrates: >-
    Why the trial is offered as a downsell rather than as the front-end offer.
  anchor: >-
    ten people on your Attraction Offer. And now you downsell *another* four
  source: >-
    100m-money-models.md, ch. Trial With Penalty, line 4223
  confirmations: 1
  anchor_at: "100m-money-models.md:4223"
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
  confirmations: 1
  anchor_at: "100m-money-models.md:4268"
- id: C-money-models-052
  type: case
  name: >-
    Offering the trial last
  statement: >-
    Once someone has made clear they do not want the first offer, the trial is offered as a pickle solved: how about we just get you started for free, we can help you out and if you like it you can stay, let me get your ID and we can get the process started, fair enough. The card is taken before the fees are explained.
  demonstrates: >-
    Offer the trial last and always get a credit card.
  anchor: >-
    might sound:*"Hmmm...that sure is a pickle. I'll tell ya what. How about
  source: >-
    100m-money-models.md, ch. Trial With Penalty, line 4305
  confirmations: 1
  anchor_at: "100m-money-models.md:4305"
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
  confirmations: 1
  anchor_at: "100m-money-models.md:4347"
- id: C-money-models-054
  type: case
  name: >-
    Making the check-ins part of the criteria
  statement: >-
    After explaining all the criteria, attention is drawn to the check-ins, which are the upsell opportunities: you agree to attend each of the three check-ins, the first we do X so that you can get benefit one, the second Y, the third Z, and obviously we charge if you miss these because it's the only way we can get you results.
  demonstrates: >-
    Building mandatory meetings into the trial terms so the trial generates offers.
  anchor: >-
    to check-ins (our upsell opportunities): *"Yep, and you agree to attend
  source: >-
    100m-money-models.md, ch. Trial With Penalty, line 4368
  confirmations: 1
  anchor_at: "100m-money-models.md:4368"
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
  confirmations: 1
  anchor_at: "100m-money-models.md:4528"
- id: C-money-models-057
  type: case
  name: >-
    The numbers behind the guarantee downsell
  statement: >-
    Before, with a single full-price option, 25 of every 100 people on a call bought; after adding the downsell, 35 buy the main thing and 40 take the downsell, tripling the close rate from 25% to 75% while raising both full-price buyers and up-front cash.
  demonstrates: >-
    That a well-built downsell increases sales of the original offer rather than cannibalising them.
  anchor: >-
    call, 25 bought. Now, 35 people buy the main thing and 40 take the
  source: >-
    100m-money-models.md, ch. Feature Downsells, line 4539
  confirmations: 1
  anchor_at: "100m-money-models.md:4539"
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
- id: C-money-models-060
  type: case
  name: >-
    Naming the cheapest package The Minimum
  statement: >-
    The most expensive combination is named after an aspirational status, such as The Whale Package or The Total Transformation, on the airline First-Business-Economy pattern; the cheapest is named The Minimum, so that after all other packages are refused the seller can ask so nothing more than the minimum package then.
  demonstrates: >-
    Naming feature combinations, and getting people to say no in order to say yes as in the Classic Upsell.
  anchor: >-
    other packages, I just say "so nothing more than the minimum package
  source: >-
    100m-money-models.md, ch. Feature Downsells, line 4716
  confirmations: 1
  anchor_at: "100m-money-models.md:4716"
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
  confirmations: 1
  anchor_at: "100m-money-models.md:4955"
- id: C-money-models-065
  type: case
  name: >-
    The numbers of that switch
  statement: >-
    Before, 34 of every 100 signed up for the challenge and about half of those, seventeen, converted to stay; after, only about fifteen take the challenge but forty go straight into continuity, and about eight of those forty take the six-month prepayment upsell. Membership sales tripled while up-front cash from challenges and prepayments still stacked.
  demonstrates: >-
    That a continuity bonus offered at the point of interest converts better than selling a challenge and converting later.
  anchor: >-
    "Before, we'd get thirty-four out of a hundred to sign up for the
  source: >-
    100m-money-models.md, ch. Continuity Bonus Offers, line 4976
  confirmations: 1
  anchor_at: "100m-money-models.md:4976"
- id: C-money-models-066
  type: case
  name: >-
    The pet food continuity bonus
  statement: >-
    One-time bonus: every dog toy the company has ever made, an $800 value, free on signing up for monthly dog food shipments at $59 a month. Monthly bonus: a new dog toy every month as a member.
  demonstrates: >-
    A Continuity Bonus worth more than the first continuity payment, plus recurring bonuses to keep people in.
  anchor: >-
    *One-Time Bonus:* Get every dog toy we've ever made for free, an \$800
  source: >-
    100m-money-models.md, ch. Continuity Bonus Offers, line 5027
  confirmations: 1
  anchor_at: "100m-money-models.md:5027"
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
  confirmations: 2
  anchor_at: "100m-money-models.md:5043"
- id: C-money-models-068
  type: case
  name: >-
    Buy five months get one free
  statement: >-
    On a bulk prepaid continuity upsell of buy five months get one free, only one person in every eight has to take it to raise 30-day profits by 50%.
  authors_caveat: >-
    The laws of discounting still apply: the larger the discount, the more people take it.
  demonstrates: >-
    Bulk prepaid discounts as the continuity upsell that makes or breaks 30-day profit.
  anchor: >-
    "buy five months get one free." Only *one out of every eight people* has
  source: >-
    100m-money-models.md, ch. Continuity Bonus Offers, line 5178
  confirmations: 1
  anchor_at: "100m-money-models.md:5178"
- id: C-money-models-069
  type: case
  name: >-
    A free year of trash for five years paid
  statement: >-
    A trash hauler with one truck and a credit card went to the big apartment complexes and offered a whole year of trash service free if they contracted the next five years paid; he fronted the year, no one would invest, and after the year mark the cash came in. He later sold the business.
  demonstrates: >-
    Continuity Discount Offers with the discount applied up front and the term pushed out, in an industry with a history of enforceable contracts.
  anchor: >-
    "I went to all the big apartments and said I'd do their trash for a
  source: >-
    100m-money-models.md, ch. Continuity Discount Offers, line 5285
  confirmations: 1
  anchor_at: "100m-money-models.md:5285"
- id: C-money-models-070
  type: case
  name: >-
    Spreading a continuity discount over the term
  statement: >-
    Three months free for a one-year commitment at $200 a month is a $600 discount; spread across twelve months it becomes $50 off each month, and customers who make every payment on time can be told they keep the discount for life once the term ends.
  demonstrates: >-
    The spread-over-time option among the four ways to apply a continuity discount: up front, at the end, spread, or after the first one to two payments.
  anchor: >-
    discounted \$600. By spreading that \$600 over 12 months, they get a
  source: >-
    100m-money-models.md, ch. Continuity Discount Offers, line 5369
  confirmations: 1
  anchor_at: "100m-money-models.md:5369"
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
- id: C-money-models-072
  type: case
  name: >-
    The rice company's earned lifetime discount
  statement: >-
    A rice company offered three options: a one-time price, a 5% off subscription, and 15% off if you stayed on the subscription for five straight months, so the lower lifetime rate had to be earned; the five months sat just beyond the point where most customers cancelled.
  demonstrates: >-
    Placing a lifetime discount at the month of greatest churn so customers stay through it.
  anchor: >-
    subscription 3) 15% off *if you stayed on the subscription for five
  source: >-
    100m-money-models.md, ch. Continuity Discount Offers, line 5451
  confirmations: 1
  anchor_at: "100m-money-models.md:5451"
- id: C-money-models-073
  type: case
  name: >-
    The cancellation fee set equal to the discount taken
  statement: >-
    Since everyone enters the continuity offer on a discount of some kind, the cancellation fee is made equal to the discount they agreed to take: $600 of discounts means they can pay $600 whenever they want to cancel, which puts them back at the month-to-month rate.
  why: >-
    It is simple to explain, and light cancellation terms get more sign-ups but more leavers while harsher terms do the opposite.
  demonstrates: >-
    Deciding the cancellation policy ahead of time as part of the Continuity Discount Offer.
  anchor: >-
    get.* So if they got \$600 in discounts by committing, they can pay
  source: >-
    100m-money-models.md, ch. Continuity Discount Offers, line 5463
  confirmations: 1
  anchor_at: "100m-money-models.md:5463"
- id: C-money-models-074
  type: case
  name: >-
    Waiving the cancellation fee for an exit interview
  statement: >-
    A customer who wants to cancel is told the cancellation fee will be waived if they come in and say what could be done better; the feedback either fixes the problem or opens a rollover into a higher level of service, and about a third of the customers who agree to the interview are saved.
  demonstrates: >-
    Using cancellation fees to the customer's advantage and turning a cancellation into a rollover upsell.
  anchor: >-
    waive your cancellation fee if you come in and tell me what I could do
  source: >-
    100m-money-models.md, ch. Continuity Discount Offers, line 5486
  confirmations: 1
  anchor_at: "100m-money-models.md:5486"
- id: C-money-models-075
  type: case
  name: >-
    The high-ticket seller's two options
  statement: >-
    Customers are given two options: go month-to-month with a big setup fee covering the cost of getting started and leave whenever, or commit to a year and have the fee waived. The fee is made huge so buyers commit to avoid it, and they initial that they understand they can still quit early by paying the fee that was waived.
  why: >-
    It costs a lot to quit at the beginning, which keeps people engaged; once they pass that point cancelling costs about what sticking it out costs, so they stick it out.
  demonstrates: >-
    The Waived Fee Offer, and the bottom line that customers stay longer if leaving costs more than staying.
  anchor: >-
    "I tell customers they have two options: *'You can go month-to-month
  source: >-
    100m-money-models.md, ch. Waived Fee Offer, line 5575
  confirmations: 1
  anchor_at: "100m-money-models.md:5575"
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
  confirmations: 2
  anchor_at: "100m-money-models.md:5792"
- id: C-money-models-079
  type: case
  name: >-
    Gym Launch money model breakdown (services)
  statement: >-
    Stage I attraction: Decoy Offer, free do-it-yourself against $16,000 done-with-you licensing. Stage II upsell: Classic Upsell at $42,000 per year, $36,000 prepaid. Stage II downsell: Payment Plan seesaw starting at $10,000 down with the rest over 52 weeks, ending at $800 per week for 52 weeks. Stage III continuity: Menu Close plus Feature Downsell from an $800 per week full package down through done-for-you advertising, sales training and monthly releases to a $100 per week Minimum package of the original materials with tech support.
  demonstrates: >-
    All four offer types arranged into the three stages of a $100M Money Model in a services business.
  anchor: >-
    \$42,000 Per year (\$36,000 Prepaid) for advanced business services.
  source: >-
    100m-money-models.md, Section VI Example Money Models, line 5880
  confirmations: 2
  anchor_at: "100m-money-models.md:5880"
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
- id: C-money-models-083
  type: case
  name: >-
    Filling money model gaps with other people's products
  statement: >-
    A dental agency sends its dentist clients to a braces manufacturer and takes a commission on each. A massage therapist sells clients someone else's home massage tools, exercise bands and medicine balls, with the customer paying through the therapist and the other company shipping. An educator tells clients to use a specific customer service software and is paid a commission for every sign-up.
  why: >-
    In every case it is more money with no extra work and no extra service delivered, which is what makes affiliate offers a way to add offers without adding operations.
  demonstrates: >-
    Affiliate relationships filling gaps in a money model without the headache of delivery.
  anchor: >-
    ● Service: A dental agency sends their dentist clients to a braces
  source: >-
    100m-money-models.md, Section VI Important Notes, line 6047
  confirmations: 1
  anchor_at: "100m-money-models.md:6047"
```
