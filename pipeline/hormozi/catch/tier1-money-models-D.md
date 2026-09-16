# Улов фазы 1 — $100M Money Models (2025) (ярус 1), тип D: антипаттерны и границы

Группа `tier1-money-models`, слаг `money-models`, ярус 1. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **88** (экстрактор вернул 88, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-money-models.md` | 1–6495 | 7 | 88 |

## Как собран файл

Экстрактор D (Antipatterns and boundaries) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier1-money-models.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier1-money-models-D.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: D-money-models-001
  type: antipattern
  name: >-
    Bad Money Models Kill Businesses
  statement: >-
    Spending more to acquire a customer than that customer produces in profit, and treating it as a normal cost of doing business.
  why: >-
    The author walks the sequence out: they spend, find at month end they spent more than they made, cut advertising, then cut it altogether, float the business with personal cash, loans and credit, sell percentages just to keep the lights on, wait months or years to make their money back, and finally lose it all.
  anchor: >-
    It costs many businesses more to get somebody to buy a thing than they
  source: >-
    100m-money-models.md, Section I, Beware: Bad Money Models Kill Businesses, line 799
  confirmations: 2
  anchor_at: "100m-money-models.md:799"
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
  confirmations: 1
  anchor_at: "100m-money-models.md:820"
- id: D-money-models-003
  type: antipattern
  name: >-
    Waiting two years to get paid
  statement: >-
    Accepting a profitable-but-slow deal (spend $100, make $500 in profit over two years) without asking how long the cash takes to come back.
  why: >-
    It is a great business only if you already have tons of cash in the bank; otherwise you run out of money while waiting.
  applies_when: >-
    Any business without investors or a large cash reserve.
  anchor: >-
    the bank. Otherwise, *you're gonna run out of money*. That leaves you
  source: >-
    100m-money-models.md, Section I, Beware: Bad Money Models Kill Businesses, line 830
  confirmations: 1
  anchor_at: "100m-money-models.md:830"
- id: D-money-models-004
  type: antipattern
  name: >-
    The poor person mantra
  statement: >-
    Saying "this won't work for my business" instead of asking "how will I make this work for my business?"
  why: >-
    All businesses have Money Models; it is what makes a business a business, so they all work and the question is only how.
  anchor: >-
    the *poor person* mantra "this won't work for my business" to the *rich
  source: >-
    100m-money-models.md, The Four Types of Offers That Make Money Models, Important Notes, line 954
  confirmations: 1
  anchor_at: "100m-money-models.md:954"
- id: D-money-models-005
  type: antipattern
  name: >-
    Copying what "they" do
  statement: >-
    Copying another business's Money Model instead of designing your own.
  why: >-
    Some Money Models work better in some businesses than others; if you just try to copy what "they" do you'll be disappointed.
  anchor: >-
    just different ways to offer stuff. If you just try to copy what "they"
  source: >-
    100m-money-models.md, The Four Types of Offers That Make Money Models, Important Notes, line 961
  confirmations: 1
  boundary: >-
    The offers are just different ways to offer stuff; to make one work for your business you have to design your own.
  anchor_at: "100m-money-models.md:961"
- id: D-money-models-006
  type: antipattern
  name: >-
    Fighting a refund request
  statement: >-
    Refusing or arguing over a refund a customer asks for, entitled or not.
  why: >-
    It is a headache; the author's personal rule is to give it back, fix the goof if you made one, and spend the time and resources on getting better customers next time. If someone doesn't want him to have their money, he wants it less than they do.
  anchor: >-
    And if you made a goof---*fix the goof.* Don't be a silly goose. Treat
  source: >-
    100m-money-models.md, The Four Types of Offers That Make Money Models, Important Notes, line 968
  confirmations: 2
  anchor_at: "100m-money-models.md:968"
- id: D-money-models-007
  type: antipattern
  name: >-
    Hard Selling Is For Weak Products
  statement: >-
    Convincing someone against their will to take an offer they don't want.
  why: >-
    Hard selling is for weak products; making offers available at the time the customer has a problem puts you ahead of the competition, and it's a numbers game, so find somebody who does want it.
  anchor: >-
    *OK*. Don't convince someone against their will. Make offers available
  source: >-
    100m-money-models.md, The Four Types of Offers That Make Money Models, Important Notes, line 975
  confirmations: 1
  anchor_at: "100m-money-models.md:975"
- id: D-money-models-008
  type: rule
  name: >-
    Obey The Law
  statement: >-
    Before running any offer from the book, check with lawyers whether it is legal where and when you are running it.
  why: >-
    The plays were learned in different places and times under different rules; advertising laws change all the time and only get tighter, especially around "free."
  anchor: >-
    they tend to only get tighter---especially when it comes to "free."
  source: >-
    100m-money-models.md, The Four Types of Offers That Make Money Models, Important Notes, line 985
  confirmations: 1
  boundary: >-
    The book is intended as Money Model inspiration only; legality of a given offer in a given jurisdiction is outside its scope and belongs to legal counsel.
  authors_caveat: >-
    "This book is intended to be Money Model inspiration. Use it that way."
  anchor_at: "100m-money-models.md:985"
- id: D-money-models-009
  type: antipattern
  name: >-
    Be Transparent
  statement: >-
    Lying or misstating the facts to make an offer compelling, instead of changing reality or reframing the true facts.
  why: >-
    You short-change yourself long-term; unlike credit card debt, you can't file bankruptcy to erase a bad reputation, and once you have a bad one it sticks for life.
  anchor: >-
    make them compelling or learn to frame them in a way that is. Don't lie.
  source: >-
    100m-money-models.md, The Four Types of Offers That Make Money Models, Important Notes, line 992
  confirmations: 1
  anchor_at: "100m-money-models.md:992"
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
- id: D-money-models-011
  type: antipattern
  name: >-
    Running Win Your Money Back with nothing to sell next
  statement: >-
    Running a Win Your Money Back offer without an upsell ready to apply the winnings to.
  why: >-
    The money comes from the qualifiers who stay as customers, and they can only stay customers if they have something else to buy.
  anchor: >-
    often stay as customers. But they can only stay customers *if they have
  source: >-
    100m-money-models.md, Win Your Money Back, Important Notes, line 1242
  confirmations: 2
  boundary: >-
    A prepared upsell (Section III) is a precondition of the offer, not an optional extra.
  anchor_at: "100m-money-models.md:1242"
- id: D-money-models-012
  type: rule
  name: >-
    Only Offer "Win Your Money Back" If You Feel Ok With Giving Money Back!
  statement: >-
    Do not run Win Your Money Back if you cannot stomach giving money back.
  why: >-
    From data collected from thousands of gyms, about 10% of all customers will ask for their money back; refunds are part of doing business.
  anchor: >-
    ask for their money back. If you can't stomach it, don't do this.
  source: >-
    100m-money-models.md, Win Your Money Back, Important Notes, line 1252
  confirmations: 1
  boundary: >-
    Benchmark, 2025, from thousands of gyms: expect about 10% of all customers to ask for their money back on this offer.
  anchor_at: "100m-money-models.md:1252"
- id: D-money-models-013
  type: antipattern
  name: >-
    Giving the winnings as free months up front
  statement: >-
    Handing a customer their won credit as free time up front (a $600 credit as three free months) instead of spreading it over a longer term.
  why: >-
    People fall off if they don't pay something; in the author's own gym, winners put $600 toward three months and then churned out before their first out-of-pocket payment, so he had effectively sold "buy six weeks get three months free." A discount over the long haul keeps them engaged over the long haul.
  anchor: >-
    ● A customer wins \$600 of credit. Avoid giving them three free months
  source: >-
    100m-money-models.md, Win Your Money Back, How You Apply Store Credit, line 1310
  confirmations: 3
  anchor_at: "100m-money-models.md:1310"
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
- id: D-money-models-015
  type: rule
  name: >-
    Refund rate below 5%
  statement: >-
    Only use a Win Your Money Back Offer if your refund rate is below 5%; otherwise fix the product first.
  why: >-
    You risk giving too many refunds.
  anchor: >-
    ● Only use a Win Your Money Back Offer if your refund rate is below 5%.
  source: >-
    100m-money-models.md, Win Your Money Back, Summary Points, line 1416
  confirmations: 1
  boundary: >-
    A hard precondition on the business, not on the offer: refund rate under 5% before the offer is run at all.
  anchor_at: "100m-money-models.md:1416"
- id: D-money-models-016
  type: rule
  name: >-
    Consult Legal Counsel About How To Structure Your Giveaway
  statement: >-
    In a Giveaway, somebody actually has to win the Grand Prize, the prize and the qualifications to win are made clear in the rules, and it is made clear that more than one person can win a prize.
  why: >-
    The author calls these no-brainers because of the way he likes to do business, and sends the rest to legal counsel.
  anchor: >-
    like to do business: somebody actually has to win the Grand Prize. Make
  source: >-
    100m-money-models.md, Giveaways, Important Notes, line 1638
  confirmations: 1
  boundary: >-
    The author states he is not legal counsel; the structure of a giveaway beyond these points is outside the method.
  anchor_at: "100m-money-models.md:1638"
- id: D-money-models-017
  type: rule
  name: >-
    Entry friction trade-off
  statement: >-
    The more work you make it to enter a Giveaway, the fewer people enter but the more qualified they are.
  why: >-
    Eligibility criteria and qualifying actions get better information and more committed entrants at the cost of volume, so the level of friction is a deliberate choice.
  anchor: >-
    That being said, the more work you make it to enter the fewer people
  source: >-
    100m-money-models.md, Giveaways, Important Notes, line 1649
  confirmations: 1
  boundary: >-
    There is no single right amount of entry friction; the author says to find your sweet spot.
  anchor_at: "100m-money-models.md:1649"
- id: D-money-models-018
  type: antipattern
  name: >-
    A Grand Prize that isn't grand
  statement: >-
    Offering a weak Grand Prize (a portfolio company offered tickets to their own event) and concluding the Giveaway mechanism doesn't work.
  why: >-
    Grand prizes only work if they're grand; the same company re-ran it with a $50,000 bundle of equipment plus their core product for a year and it crushed. If nobody bites, give away something better, or at least better for the audience.
  anchor: >-
    told them grand prizes only work if they're *grand*. They tried it again
  source: >-
    100m-money-models.md, Giveaways, Important Notes, line 1656
  confirmations: 1
  anchor_at: "100m-money-models.md:1656"
- id: D-money-models-019
  type: antipattern
  name: >-
    More entries than you can call
  statement: >-
    Letting more people enter the Giveaway than you have the time and resources to connect with inside seven days.
  why: >-
    Any more would be a waste; the author matches entries to callable capacity and advertises for seven days or until leads surpass that number, whichever comes first.
  anchor: >-
    inside seven days. Any more would be a waste.
  source: >-
    100m-money-models.md, Giveaways, Important Notes, line 1686
  confirmations: 2
  anchor_at: "100m-money-models.md:1686"
- id: D-money-models-020
  type: antipattern
  name: >-
    Advertise Benefits Not The Features
  statement: >-
    Putting specific product details into the advertising instead of the dream outcome.
  why: >-
    You advertise a transformation in 21 days, not workouts and meal plans; leads get specific product details in the sales presentation, not in the advertising.
  anchor: >-
    and meal plans. Leads get specific product details in the sales
  source: >-
    100m-money-models.md, Decoy Offer, Important Notes, line 1931
  confirmations: 1
  anchor_at: "100m-money-models.md:1931"
- id: D-money-models-021
  type: rule
  name: >-
    Discount Offers Have Higher Show-Up Rates Than Free Offers
  statement: >-
    A Free Attraction Offer gets more leads; a Discount Offer gets fewer leads but a higher percentage who show up, so use a Discount Offer where you have low show-up rates.
  why: >-
    In the author's experience the trade is volume of leads against show rate.
  anchor: >-
    for businesses where you have a high cost of someone not showing up
  source: >-
    100m-money-models.md, Decoy Offer, Important Notes, line 1962
  confirmations: 1
  boundary: >-
    Especially important for businesses with a high cost of a no-show: doctors, lawyers, dentists.
  anchor_at: "100m-money-models.md:1962"
- id: D-money-models-022
  type: rule
  name: >-
    Legally required to present the decoy
  statement: >-
    Where you are legally required to present the decoy option, present it and then immediately contrast it with the premium offer, instead of leading with the premium.
  why: >-
    In a perfect world they take the premium offer immediately and the decoy stays in your back pocket; the legal requirement removes that choice, so the contrast has to do the work.
  anchor: >-
    about your decoy, you are legally required to present it, or you prefer
  source: >-
    100m-money-models.md, Decoy Offer, Important Notes, line 1971
  confirmations: 1
  boundary: >-
    The author names the legal obligation to present the advertised offer as a case where his preferred sequence (premium first) does not apply.
  anchor_at: "100m-money-models.md:1971"
- id: D-money-models-023
  type: antipattern
  name: >-
    Too little contrast between decoy and premium
  statement: >-
    Running a Decoy Offer whose decoy option is not stripped down far enough to make the premium option look like a much better deal.
  why: >-
    The value of the premium option comes from huge differences with the decoy option; if you're not making money fast, make the contrast between offers larger.
  anchor: >-
    ● Expect to make money fast. If you're not, then make the contrast
  source: >-
    100m-money-models.md, Decoy Offer, Summary Points, line 2033
  confirmations: 2
  anchor_at: "100m-money-models.md:2033"
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
- id: D-money-models-025
  type: antipattern
  name: >-
    Raise Prices Before Giving Stuff Away To Preserve Profits
  statement: >-
    Adding free units to an existing price without permanently raising the price first, or claiming a raise that never happened.
  why: >-
    The offer will work, and since it will work you need to make money from it; the price rise has to be real because this is what all new customers will come in on.
  anchor: >-
    discount. Don't lie. Actually raise your prices. Since this is what all
  source: >-
    100m-money-models.md, Buy X Get Y Free, Important Notes, line 2158
  confirmations: 1
  anchor_at: "100m-money-models.md:2158"
- id: D-money-models-026
  type: antipattern
  name: >-
    Buy ten get two free
  statement: >-
    Structuring the offer so the paid quantity exceeds the free quantity (buy ten get two free).
  why: >-
    Buy ten get two free is not as strong as buy two get ten free; the author notes this seems obvious but people don't do it.
  applies_when: >-
    Always try to give more free things than paid things; play with the pricing until it makes sense for you.
  anchor: >-
    See second example. Buy ten get two free is not as strong as buy two get
  source: >-
    100m-money-models.md, Buy X Get Y Free, Important Notes, line 2171
  confirmations: 2
  anchor_at: "100m-money-models.md:2171"
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
- id: D-money-models-028
  type: antipattern
  name: >-
    Do Not Make Offers Like This If You Can't Manage Money
  statement: >-
    Collecting a year of prepayments with Buy X Get Y Free and spending the cash that is meant to service the customers for the duration of the agreement.
  why: >-
    Selling stuff you can't deliver on breaks the law and ruins your reputation; you must budget the correct amount to service customers for the whole agreement.
  anchor: >-
    **Do Not Make Offers Like This If You Can't Manage Money.** While Buy X
  source: >-
    100m-money-models.md, Buy X Get Y Free, Important Notes, line 2215
  confirmations: 2
  boundary: >-
    The author names cash management and delivery capacity for the full term as preconditions for using this offer at all.
  anchor_at: "100m-money-models.md:2215"
- id: D-money-models-029
  type: rule
  name: >-
    Cap the fast-cash offer at 10% of customers
  statement: >-
    When making Buy X Get Y Free to existing recurring customers for fast cash, limit the offer to 10% of your customers.
  why: >-
    This gives a good cash pop and keeps recurring cash flow healthy; selling it to everyone would trade away the recurring revenue.
  anchor: >-
    at their current price. Just limit the offer to 10% of your customers.
  source: >-
    100m-money-models.md, Buy X Get Y Free, Important Notes, line 2227
  confirmations: 2
  boundary: >-
    Applies to a business that already has recurring revenue and needs cash fast.
  anchor_at: "100m-money-models.md:2227"
- id: D-money-models-030
  type: antipattern
  name: >-
    Not selling to prepaid customers
  statement: >-
    Holding back further offers from customers who have prepaid for a long duration.
  why: >-
    The author calls this a mistake: these are the people who spend the most money, and their wallets have been refreshed with new money since they prepaid months ago.
  anchor: >-
    who prepay for stuff. This is a mistake. Speaking from experience, these
  source: >-
    100m-money-models.md, Buy X Get Y Free, Important Notes, line 2232
  confirmations: 2
  anchor_at: "100m-money-models.md:2232"
- id: D-money-models-031
  type: antipattern
  name: >-
    A promise you can't deliver in the time frame
  statement: >-
    Making a Pay Less Now or Pay More Later promise that is not a clear yes/no result, or that you cannot deliver inside the stated time frame.
  why: >-
    If you don't deliver, they will ask not to be billed; keeping the promise simple, clear and measurable avoids unnecessary cancellations.
  anchor: >-
    or no' result. Second, make sure you can deliver on it within your time
  source: >-
    100m-money-models.md, Pay Less Now or Pay More Later, Important Notes, line 2407
  confirmations: 1
  anchor_at: "100m-money-models.md:2407"
- id: D-money-models-032
  type: rule
  name: >-
    If More Than 10% Of 'Pay Later' People Cancel Their Payment
  statement: >-
    If more than 10% of pay-later customers cancel their payment, the diagnosis is one of three: you promised too much, the guarantee conditions are too low, or the price is too high.
  why: >-
    No matter how well you deliver, some people will cancel; above 10% the cause is in the offer, not in the customers.
  anchor: >-
    promised too much, the guarantee conditions are too low, or the price is
  source: >-
    100m-money-models.md, Pay Less Now or Pay More Later, Important Notes, line 2435
  confirmations: 2
  boundary: >-
    Benchmark, 2025: some cancellation is normal and is to be factored into the cost of doing business; only above 10% is it a fault in the offer.
  anchor_at: "100m-money-models.md:2435"
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
- id: D-money-models-034
  type: antipattern
  name: >-
    Upsells fail when — the offer is too different
  statement: >-
    Offering as an upsell something they don't want: too different, or not a solution to the problem the first offer revealed.
  why: >-
    Listed by the author as one of the three ways upsells fail.
  anchor: >-
    ● You offer something they don\'t want (too different or doesn\'t solve
  source: >-
    100m-money-models.md, Section III intro: Upsell Offers, Upsells fail when, line 2664
  confirmations: 1
  anchor_at: "100m-money-models.md:2664"
- id: D-money-models-035
  type: antipattern
  name: >-
    Upsells fail when — the wrong time
  statement: >-
    Making the upsell before the customer has experienced the problem it solves.
  why: >-
    The Classic Upsell works because the next problem becomes apparent as soon as the customer makes the first purchase; offered earlier, there is no problem to solve.
  anchor: >-
    ● You offer it at the wrong time (before they've experienced the
  source: >-
    100m-money-models.md, Section III intro: Upsell Offers, Upsells fail when, line 2667
  confirmations: 1
  anchor_at: "100m-money-models.md:2667"
- id: D-money-models-036
  type: antipattern
  name: >-
    Upsells fail when — the wrong way
  statement: >-
    Offering the upsell in a way the customer doesn't believe.
  why: >-
    Listed by the author as the third way upsells fail, alongside the wrong thing and the wrong time, and combinations of the three.
  anchor: >-
    ● You offer it the wrong way (they don\'t believe you).
  source: >-
    100m-money-models.md, Section III intro: Upsell Offers, Upsells fail when, line 2670
  confirmations: 1
  anchor_at: "100m-money-models.md:2670"
- id: D-money-models-037
  type: rule
  name: >-
    Warning on the Upsell section
  statement: >-
    The upsell tactics in Section III must be used ethically.
  why: >-
    The author flags the section as brutally effective and attaches the warning himself.
  anchor: >-
    **Warning**: This section is brutally effective and must be used
  source: >-
    100m-money-models.md, Section III intro: Upsell Offers, line 2696
  confirmations: 1
  boundary: >-
    An explicit ethical limit the author puts on his own upsell tactics.
  anchor_at: "100m-money-models.md:2696"
- id: D-money-models-038
  type: antipattern
  name: >-
    You barely have a business---you have a front end
  statement: >-
    Selling only one thing and having nothing to offer next.
  why: >-
    The author tells such businesses they barely have a business, they have a front end; those who actually added an upsell 5x'd the business.
  anchor: >-
    only sell one thing. I usually just tell them "You barely have a
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2809
  confirmations: 2
  anchor_at: "100m-money-models.md:2809"
- id: D-money-models-039
  type: antipattern
  name: >-
    Not asking
  statement: >-
    Holding back an upsell out of shyness when you can solve the problem.
  why: >-
    The second worst thing that happens is they say no; the worst thing is if they would have said yes but you never asked.
  anchor: >-
    offer to. The second worst thing that happens is they say no. *The worst
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2885
  confirmations: 2
  anchor_at: "100m-money-models.md:2885"
- id: D-money-models-040
  type: antipattern
  name: >-
    Giving the option not to buy
  statement: >-
    Asking whether the customer wants the product at all, instead of which of two they prefer, what they don't need, or how to use it.
  why: >-
    When you give people the option to not buy, some don't buy; the four Menu Upsell tactics all replace "if" with something else.
  anchor: >-
    the option to not buy, some don't buy. So, I give the option to pick
  source: >-
    100m-money-models.md, Menu Upsell, Description, line 3119
  confirmations: 2
  anchor_at: "100m-money-models.md:3119"
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
- id: D-money-models-042
  type: rule
  name: >-
    The anchor and the main offer must share core functions
  statement: >-
    Anchor Upsells work only when the lower-priced offer keeps the same core functions as the premium one; only secondary features are changed.
  why: >-
    Most people just want a suit; the suit is the primary feature and the material and designer are secondary, so offering the primary features for a fifth of the price makes the main offer a great deal.
  anchor: >-
    Anchor Upsells work best when the lower-price offer has the same *core
  source: >-
    100m-money-models.md, Anchor Upsell, Description, line 3342
  confirmations: 3
  boundary: >-
    For the anchor to work at all the premium offer should be 5--10x more expensive than the main offer.
  anchor_at: "100m-money-models.md:3342"
- id: D-money-models-043
  type: antipattern
  name: >-
    If You Treat The Anchor Like A Fake, So Will The Customer
  statement: >-
    Glossing over the premium offer, going through the motions, and then reporting that anchoring doesn't work.
  why: >-
    The person never really considered it because you never really offered it; you lose trust and waste time. Only after they pause, hesitate or ask for something else do you move on.
  anchor: >-
    people hear about this technique. Try it. Gloss over the premium offer.
  source: >-
    100m-money-models.md, Anchor Upsell, Important Notes, line 3399
  confirmations: 2
  anchor_at: "100m-money-models.md:3399"
- id: D-money-models-044
  type: antipattern
  name: >-
    Make A Premium Offer You Actually Want People To Buy
  statement: >-
    Inventing a premium anchor you don't actually want anyone to buy.
  why: >-
    A friend struggled with anchoring for exactly this reason; rebuilding the premium into something he would be happy to deliver tripled his profits. Some customers will buy the premium offer, and expensive premium offers add outsized profits with fewer sales.
  anchor: >-
    figure out the problem. He made up some BS that he didn't really want
  source: >-
    100m-money-models.md, Anchor Upsell, Important Notes, line 3408
  confirmations: 2
  anchor_at: "100m-money-models.md:3408"
- id: D-money-models-045
  type: antipattern
  name: >-
    Refunding before offering a rollover
  statement: >-
    Issuing a refund to an upset customer before offering to roll the purchase over into something else.
  why: >-
    Doing rollovers before refunding has saved the author tons of customers and cash; if you did a bad job, roll over for a do-over, and if they want something different, roll it toward that instead.
  anchor: >-
    tons of customers and cash. If you did a bad job (hey, it happens), roll
  source: >-
    100m-money-models.md, Rollover Upsell, Important Notes, line 3640
  confirmations: 1
  anchor_at: "100m-money-models.md:3640"
- id: D-money-models-046
  type: rule
  name: >-
    How To Price Your Rollover Upsell
  statement: >-
    Price the next offer at least four times the rollover credit, so applying the whole first purchase discounts it by 25% at most.
  why: >-
    To make money on a discounted offer you must have profit left after you discount it; the rules of discounting apply, bigger discounts make less profit per sale but get more sales.
  anchor: >-
    offer, you must have profit left after you discount it. Since I prefer
  source: >-
    100m-money-models.md, Rollover Upsell, Important Notes, line 3661
  confirmations: 2
  boundary: >-
    A rollover that leaves no profit after the credit is not a rollover upsell worth making; 4x the credit is the author's floor.
  anchor_at: "100m-money-models.md:3661"
- id: D-money-models-047
  type: antipattern
  name: >-
    Hiding your head in the sand after a no
  statement: >-
    Treating a no to this offer as a rejection of you and of all offers, and stopping.
  why: >-
    No means no for this thing, not no for everything; the no is an opportunity to find out what they really want and profit from it.
  anchor: >-
    from it. Instead of hiding your head in the sand, stand your ground and
  source: >-
    100m-money-models.md, Section IV, The Rules of Downselling, line 3775
  confirmations: 1
  anchor_at: "100m-money-models.md:3775"
- id: D-money-models-048
  type: antipattern
  name: >-
    Building a hundred products to downsell
  statement: >-
    Creating new products so that everyone has something to buy, instead of offering what you already have in new ways.
  why: >-
    Otherwise you create a hundred businesses' worth of products (and problems) — a silly choice; it's less about having 100 products to offer and more about having 100 ways to offer your product.
  anchor: >-
    world, you limit downsells to what you've got. Otherwise, you create a
  source: >-
    100m-money-models.md, Section IV, The Rules of Downselling, line 3792
  confirmations: 4
  anchor_at: "100m-money-models.md:3792"
- id: D-money-models-049
  type: antipattern
  name: >-
    Don't Drop Your Price Just To Get Somebody To Buy
  statement: >-
    Cutting the price in the moment to close a sale.
  why: >-
    Dropping your price is not downselling, it's discounting; customers talk, and if they find out someone got the same thing for less "just because" you'll upset people, which the author also calls an ethical problem. Planning a price for a specific number of people ahead of time is a different thing from charging less because you were scared of losing the sale.
  applies_when: >-
    If they want to pay less now, offer a payment plan; if they want to pay less overall, offer a feature downsell.
  anchor: >-
    dropping your price is not really downselling, *it's discounting*. If
  source: >-
    100m-money-models.md, Section IV, The Rules of Downselling, line 3798
  confirmations: 3
  anchor_at: "100m-money-models.md:3798"
- id: D-money-models-050
  type: antipattern
  name: >-
    Payment plans that swallow your paid-in-fulls
  statement: >-
    Introducing payment plans and putting people who would have paid in full onto a plan.
  why: >-
    You lose the most when people who would have paid in full take a payment plan and cancel early; the check is that close rate rises while the percentage of appointments paying in full stays the same.
  anchor: >-
    most when people who would have paid in full take a payment plan---and
  source: >-
    100m-money-models.md, Payment Plan Downsells, line 3894
  confirmations: 2
  boundary: >-
    Payment plans only grow the business if they get more customers and those customers actually pay; the author calls them a gamble that makes money one way and loses it two.
  anchor_at: "100m-money-models.md:3894"
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
- id: D-money-models-052
  type: antipattern
  name: >-
    Punishing for paying over time
  statement: >-
    Presenting the plan as the base price plus interest ("$10 now, $15 over time because we charge $5 interest") instead of presenting the higher price and offering a prepay discount.
  why: >-
    Same math, but it feels better: presenting the price with interest included and offering prepayment as a discount makes the offer friendlier and gives you a price anchor.
  anchor: >-
    say..."*It's \$10 if you get it right now, but it's \$15 if you pay over
  source: >-
    100m-money-models.md, Payment Plan Downsells, Step 1, line 3943
  confirmations: 2
  anchor_at: "100m-money-models.md:3943"
- id: D-money-models-053
  type: rule
  name: >-
    Check To See If They Still Want The Thing
  statement: >-
    No payment plan will satisfy a customer who doesn't want the thing; check that they do (1--10, you want 8 or above) before putting more effort into selling it.
  why: >-
    Below 8 the answer is a different product (Feature Downsells), not a different payment schedule.
  anchor: >-
    will satisfy a customer who doesn't want the thing. So, make sure the
  source: >-
    100m-money-models.md, Payment Plan Downsells, Step 4, line 3991
  confirmations: 2
  boundary: >-
    Payment plan downselling applies only to prospects who want the product; wanting it is the precondition the author tests for explicitly.
  anchor_at: "100m-money-models.md:3991"
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
- id: D-money-models-055
  type: rule
  name: >-
    Offer The Trial Last
  statement: >-
    The Trial With Penalty is offered only after someone makes it clear they don't want the first offer; it is a downsell, not an attraction offer.
  why: >-
    The software company in the story used it as an Attraction Offer, but the author prefers to downsell trials so it only changes what they pay today, not what they pay in total.
  anchor: >-
    **Offer The Trial Last.** If someone makes it clear they don\'t want
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4303
  confirmations: 2
  boundary: >-
    The author records that the offer can be used as an attraction offer (as the HR software company did) but states his own placement is last in the sequence.
  anchor_at: "100m-money-models.md:4303"
- id: D-money-models-056
  type: rule
  name: >-
    Always Get A Credit Card
  statement: >-
    No trial without a card on file; if they still refuse after "That's just how we've always done it," end the conversation.
  why: >-
    The penalty mechanism and the automatic billing both depend on having the card.
  anchor: >-
    we've always done it."* If they still refuse, wish them a lovely day and
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4317
  confirmations: 2
  boundary: >-
    A hard entry condition on the customer: the offer is withdrawn rather than adapted if no card is given.
  anchor_at: "100m-money-models.md:4317"
- id: D-money-models-057
  type: rule
  name: >-
    Always Sell Staying And Paying
  statement: >-
    Ask directly whether they will stay long-term if the program gets them the result; if they say no, there is no point in giving them a trial.
  why: >-
    The trial makes money by turning triallists into long-term customers, so a prospect who will not stay even on success cannot pay for the trial.
  anchor: >-
    staying long-term if you get them results. If they say no, there's no
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4326
  confirmations: 1
  boundary: >-
    An explicit disqualifying condition: a prospect looking for a quick fix is not given the trial at all.
  anchor_at: "100m-money-models.md:4326"
- id: D-money-models-058
  type: antipattern
  name: >-
    Explaining the fees before getting the card
  statement: >-
    Explaining the penalty fees before taking the card.
  why: >-
    You will get more resistance; explained after, with a "this is just how we've always done it" attitude, the take rate is higher. People still have to agree to the fees, and the author has customers initial separately next to the fee clauses.
  anchor: >-
    **Note:** If you explain the fees *before* you get the card, you will
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4355
  confirmations: 1
  anchor_at: "100m-money-models.md:4355"
- id: D-money-models-059
  type: antipattern
  name: >-
    Blaming the customer who hated the trial
  statement: >-
    Blaming the customer when they say the trial didn't work for them.
  why: >-
    Only one person can be angry and it needs to be you; asking what they'd have wanted different, taking the anger onto yourself and then offering the higher-level thing converts about half of these people.
  anchor: >-
    yourself for missing this. *Do not blame them.* Only one person can be
  source: >-
    100m-money-models.md, Trial With Penalty, How I Upsell From A Trial, line 4390
  confirmations: 1
  anchor_at: "100m-money-models.md:4390"
- id: D-money-models-060
  type: antipattern
  name: >-
    Billing the non-starters
  statement: >-
    Charging penalty fees to people who never started, instead of reaching out repeatedly and offering to waive the fee for a meeting.
  why: >-
    A small fee isn't worth a 1-star review; you make money by getting people results and turning them into customers, not by nickeling and diming people with fees.
  anchor: >-
    like billing non-starters. A small fee isn't worth a 1-star review. But
  source: >-
    100m-money-models.md, Trial With Penalty, How I Upsell From A Trial, line 4404
  confirmations: 2
  authors_caveat: >-
    The author states this is his preference and leaves the choice open: "But hey, it's your choice."
  anchor_at: "100m-money-models.md:4404"
- id: D-money-models-061
  type: rule
  name: >-
    Tweak Your Trial To Get The Most Customers
  statement: >-
    Diagnose a failing trial by which stage fails: nobody takes it, lower the requirements or penalties; they take it but don't follow through, explain how the fees help them and make sales meetings mandatory; they don't stay on the back end, emphasise staying and paying, deliver better, and match the back end to the front end.
  why: >-
    Each symptom has its own cause in the offer's construction.
  anchor: >-
    **Tweak Your Trial To Get The Most Customers.** If no one takes your
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4407
  confirmations: 1
  anchor_at: "100m-money-models.md:4407"
- id: D-money-models-062
  type: antipattern
  name: >-
    Just Call It A Trial
  statement: >-
    Naming the offer anything that reveals the penalty, instead of calling it a Free Trial.
  why: >-
    People may get scared and confused; no one wants to be penalized. If asked why the trial works this way, the answer is "This is just how we've always done it" or "People get the best results this way."
  anchor: >-
    'special features,' you should just call it a Free Trial. Otherwise,
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4422
  confirmations: 1
  anchor_at: "100m-money-models.md:4422"
- id: D-money-models-063
  type: rule
  name: >-
    Pay Less Now or Pay More Later vs. Trial With Penalty
  statement: >-
    Pay Less Now or Pay More Later is the downsell for physical products and one-time services; Trial With Penalty is the downsell for recurring products and services.
  why: >-
    The two offers differ in what happens after the trial period, so they fit different delivery shapes.
  anchor: >-
    recurring products or services. Also, I have only made this work in
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4431
  confirmations: 1
  boundary: >-
    The author has only made Trial With Penalty work in businesses where the customer has to do work to get results, and explicitly asks readers to tell him if they find other types of business it works for.
  anchor_at: "100m-money-models.md:4431"
- id: D-money-models-064
  type: antipattern
  name: >-
    Remember, Never Negotiate The Price
  statement: >-
    Letting anyone pay less for the same thing just because they demanded it.
  why: >-
    The author calls people who demand to pay less for the same thing business terrorists and says he doesn't negotiate with terrorists; if they want to pay less now, offer a payment plan, if less overall, a feature downsell.
  anchor: >-
    for the same thing are business terrorists. I don't negotiate with
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4680
  confirmations: 2
  anchor_at: "100m-money-models.md:4680"
- id: D-money-models-065
  type: antipattern
  name: >-
    Being pushy while downselling
  statement: >-
    Pushing during a downsell instead of staying a helpful guide finding the best deal for them.
  why: >-
    If you act pushy, your offers will exhaust customers faster; staying a helpful guide keeps the conversation collaborative rather than competitive and lets you downsell as many offers as necessary without exhausting the customer.
  anchor: >-
    pushy, your offers will exhaust customers faster. If you stay a helpful
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4688
  confirmations: 1
  anchor_at: "100m-money-models.md:4688"
- id: D-money-models-066
  type: rule
  name: >-
    Tweak Your Feature Downsell Process
  statement: >-
    You cannot standardize the feature combinations at the start; you learn what customers value by solving the same problems for the same type of customer, and only then standardize.
  why: >-
    Feature Downsells close more people when you know what feature combinations to present ahead of time, and that knowledge comes from repetition.
  anchor: >-
    But, in the beginning, you won't know much about your customers'
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4694
  confirmations: 1
  boundary: >-
    A stage limit: the standardized downsell process is something a business earns with volume, not something it starts with.
  anchor_at: "100m-money-models.md:4694"
- id: D-money-models-067
  type: rule
  name: >-
    Never the same stuff for cheaper
  statement: >-
    No downsell is ever the same stuff for a lower price; what changes is how they pay or what they get.
  why: >-
    Downselling means tweaking the offer until it is the best deal for them; the same product at a lower price is a discount, which the author rules out.
  anchor: >-
    *never the same stuff for cheaper.* We just keep tweaking the offer
  source: >-
    100m-money-models.md, Downsell Offers Conclusion, line 4832
  confirmations: 2
  boundary: >-
    The defining limit of the whole Downsell section: it separates downselling from discounting.
  anchor_at: "100m-money-models.md:4832"
- id: D-money-models-068
  type: rule
  name: >-
    Continuity as a standalone Attraction Offer
  statement: >-
    Continuity is hard to use as an Attraction Offer on its own: it attracts more customers than an expensive offer but leaves you strapped for cash today.
  why: >-
    A $1,000 thing sold to 10 of 100 makes $10,000 now; the same thing at $50/month sells to 40 and makes $2,000 now and $40,000 over time. Many businesses use Continuity to attract customers for less, but it crashes 30-day profits and makes profitable advertising difficult.
  applies_when: >-
    The author's fix is to make continuity last: Attraction, Upsell and Downsell Offers first, then Continuity, then a bulk prepay upsell.
  anchor: >-
    money *now*. That makes it tough to use as an Attraction Offer *on its
  source: >-
    100m-money-models.md, Section V intro: Continuity Offers, line 4881
  confirmations: 3
  boundary: >-
    Continuity's pros and cons are stated as a trade: more customers, far less cash now.
  anchor_at: "100m-money-models.md:4881"
- id: D-money-models-069
  type: rule
  name: >-
    Only some stuff makes sense for a Continuity Offer
  statement: >-
    Continuity fits only where the customer gets ongoing value; paying forever for a one-day workshop is silly, and paying until the cost is covered is a payment plan, not continuity.
  why: >-
    If your customers get ongoing value, it probably makes sense for them to make ongoing payments — and only then.
  anchor: >-
    Also, only *some* stuff makes sense for a Continuity Offer. It's silly
  source: >-
    100m-money-models.md, Section V intro: Continuity Offers, line 4894
  confirmations: 1
  boundary: >-
    Ongoing delivered value is the precondition for continuity; without it the same schedule is a payment plan.
  anchor_at: "100m-money-models.md:4894"
- id: D-money-models-070
  type: antipattern
  name: >-
    A single price for a service provided forever
  statement: >-
    Charging one price, even a big one, to provide a service forever.
  why: >-
    The author calls this probably a mistake: ongoing value should be matched by ongoing payments.
  anchor: >-
    plan. At the same time, you probably make a mistake to offer a single
  source: >-
    100m-money-models.md, Section V intro: Continuity Offers, line 4897
  confirmations: 1
  anchor_at: "100m-money-models.md:4897"
- id: D-money-models-071
  type: antipattern
  name: >-
    Focus On The Bonus, Not The Membership
  statement: >-
    Advertising the membership itself ("Join my membership program") instead of the free valuable thing they get for joining.
  why: >-
    "Join my membership program" isn't nearly as compelling as "get this free valuable thing"; the rest is explained after they show interest.
  anchor: >-
    **Focus On The Bonus, Not The Membership.** "Join my membership program"
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, line 5053
  confirmations: 2
  anchor_at: "100m-money-models.md:5053"
- id: D-money-models-072
  type: antipattern
  name: >-
    An unrelated bonus
  statement: >-
    Using a bonus too different from the core offer, such as a free t-shirt to upsell tech services.
  why: >-
    You attract the wrong customers; a free t-shirt to upsell t-shirt printing makes sense, the same bonus on tech services does not.
  anchor: >-
    different you will *attract the wrong customers.* For instance, don't
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, line 5065
  confirmations: 2
  anchor_at: "100m-money-models.md:5065"
- id: D-money-models-073
  type: antipattern
  name: >-
    Use Realistic Bonus Pricing
  statement: >-
    Assigning made-up, ridiculous values to bonuses to make the anchor bigger.
  why: >-
    It won't anchor the customer and you'll lose trust with them; giving away products you have actually sold before lets you anchor their real prices.
  anchor: >-
    anchor believable. Some business owners make up ridiculous values. Don't
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, line 5087
  confirmations: 1
  anchor_at: "100m-money-models.md:5087"
- id: D-money-models-074
  type: rule
  name: >-
    If You Want Commitments---Prepare To Make A Trade
  statement: >-
    Restricting the bonus to customers who commit to 3-6-12+ months loses the people who would have signed up month-to-month just for the bonus.
  why: >-
    This nets fewer sales but more committed customers — the author names it explicitly as the trade you make.
  anchor: >-
    to customers who commit, you'll lose people who would've signed up
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, line 5186
  confirmations: 1
  boundary: >-
    Commitment and volume cannot both be maximised; the author frames the choice as a trade, not an optimisation.
  anchor_at: "100m-money-models.md:5186"
- id: D-money-models-075
  type: rule
  name: >-
    Up Front discount — where it works
  statement: >-
    Applying the continuity discount up front works best in industries with a successful history of enforcing contracts: cell phones, storage, real estate, equipment, or anything with collateral.
  why: >-
    The free time comes before the paid term, so the business is exposed until the contract is enforced.
  anchor: >-
    in industries that have a successful history of enforcing contracts
  source: >-
    100m-money-models.md, Continuity Discount Offers, Examples, line 5340
  confirmations: 1
  boundary: >-
    Named industries only; elsewhere the author points to the other three ways of applying the discount.
  anchor_at: "100m-money-models.md:5340"
- id: D-money-models-076
  type: rule
  name: >-
    Skip the up-front discount if you have high churn
  statement: >-
    If you have historically high churn, skip the up-front discount; note also that it does not get customers profitably — it gets customers but delays cash.
  why: >-
    The two notes the author attaches to the method himself.
  anchor: >-
    collateral). Two notes: First, if you have historically high churn, then
  source: >-
    100m-money-models.md, Continuity Discount Offers, Examples, line 5342
  confirmations: 2
  boundary: >-
    Historically high churn disqualifies the up-front variant; frontloaded discounts convert more customers but may have higher churn, backloaded ones convert fewer but lower churn.
  anchor_at: "100m-money-models.md:5342"
- id: D-money-models-077
  type: antipattern
  name: >-
    Don't Eat Into The Term With Discounts, Extend Them!
  statement: >-
    Taking the free months out of the committed term (pay nine, get three free, 12 total) instead of adding them on top (pay 12, get three free, 15 total).
  why: >-
    The author prefers to start by extending the term, because from there he can Feature Downsell a shorter one.
  anchor: >-
    **Don't Eat Into The Term With Discounts, Extend Them!** Let's say you
  source: >-
    100m-money-models.md, Continuity Discount Offers, Important Notes, line 5400
  confirmations: 1
  anchor_at: "100m-money-models.md:5400"
- id: D-money-models-078
  type: rule
  name: >-
    You Need To Have A Cancellation Policy Figured Out Ahead Of Time
  statement: >-
    A continuity discount offer requires two things decided in advance: how you apply the discount, and your cancellation policy.
  why: >-
    People don't always keep their commitments; the author's preferred policy is a cancellation fee equal to the discount they agreed to get, which is simple to explain and puts them back at the month-to-month rate.
  anchor: >-
    **You Need To Have A Cancellation Policy Figured Out Ahead Of Time**.
  source: >-
    100m-money-models.md, Continuity Discount Offers, CANCELLATIONS, line 5457
  confirmations: 2
  boundary: >-
    The author states you can make this offer work in any business so long as you know these two things.
  anchor_at: "100m-money-models.md:5457"
- id: D-money-models-079
  type: antipattern
  name: >-
    No obvious way to cancel
  statement: >-
    Leaving customers with no obvious way to cancel or to complain inside the business.
  why: >-
    They will definitely complain outside it; more people will vanish and complain, and you lose the chance to save them. Small businesses don't get rich by making stuff hard for their customers — make it easy and you'll suffer fewer 1-star reviews.
  anchor: >-
    of your business. If you have no obvious way for them to cancel, more
  source: >-
    100m-money-models.md, Continuity Discount Offers, CANCELLATIONS, line 5468
  confirmations: 2
  anchor_at: "100m-money-models.md:5468"
- id: D-money-models-080
  type: rule
  name: >-
    Cancellation terms trade-off
  statement: >-
    Light cancellation terms get more people to sign up but more people leave; harsher terms get fewer sign-ups but fewer leave.
  why: >-
    The author states the trade directly and names his own preference: customers cancel by paying the discount they got with their commitment.
  anchor: >-
    ● Light cancellation terms get more people to sign up but more people
  source: >-
    100m-money-models.md, Continuity Discount Offers, Summary Points, line 5517
  confirmations: 1
  boundary: >-
    Sign-up volume and retention cannot both be maximised through the cancellation policy.
  anchor_at: "100m-money-models.md:5517"
- id: D-money-models-081
  type: rule
  name: >-
    Pricing can't overcome a terrible product
  statement: >-
    If more than 5% of people want to cancel early under a Waived Fee Offer, look into it: pricing incentivizes sticking but it can't and shouldn't overcome a terrible product.
  why: >-
    You want to nudge them, not handcuff people into paying for something they hate — then they'll just hate you.
  anchor: >-
    Pricing *incentivizes* sticking but it can't (and *shouldn't*) overcome
  source: >-
    100m-money-models.md, Waived Fee Offer, Important Notes, line 5661
  confirmations: 1
  boundary: >-
    The outer limit of the whole pricing method: product quality is not a pricing problem, and above 5% early-cancel intent the fault is in the product, 2025 benchmark.
  anchor_at: "100m-money-models.md:5661"
- id: D-money-models-082
  type: rule
  name: >-
    I Prefer This Offer For Commitments Of One Year And Longer
  statement: >-
    Waived Fee Offers are for commitments of a year or longer, and work especially well with services that take a long time to work (SEO, investing, weight loss).
  why: >-
    The longer the commitment, the better it works; it keeps people committed when they get emotional.
  anchor: >-
    with services that take a long time to work (SEO, Investing, Weight
  source: >-
    100m-money-models.md, Waived Fee Offer, Important Notes, line 5678
  confirmations: 2
  boundary: >-
    At minimum the commitment length should be a year; the fee is typically 3--5x the monthly rate.
  anchor_at: "100m-money-models.md:5678"
- id: D-money-models-083
  type: antipattern
  name: >-
    Starting with a finished Money Model
  statement: >-
    Trying to start a bootstrapped business from zero with a complete Money Model in place, or implementing a whole Money Model at once in an existing one.
  why: >-
    It will collapse on top of you and break your business; none of the author's businesses started with a fully forged Money Model, they all start at Stage I. Money Model growth happens alongside the growth of the business, and each stage pays for the next.
  applies_when: >-
    Stick to your stage: pick one offer, run it until it works reliably, then until it's automatic, then go to the next stage.
  anchor: >-
    with a "finished" Money Model... it will collapse *on top of you*. In
  source: >-
    100m-money-models.md, Section VI, Description, line 5840
  confirmations: 3
  anchor_at: "100m-money-models.md:5840"
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
- id: D-money-models-085
  type: rule
  name: >-
    Figuring out what works best may take up to a year
  statement: >-
    Expect the Attraction Offer step to take up to a year to get right, and measure progress in quarters, not weeks.
  why: >-
    Patience is still the fastest way to get to your goal; you either build it right or you build it again, and building again — no matter how fast — still takes longer than building it right the first time.
  anchor: >-
    you're on your way. Figuring out what works best may take up to a year.
  source: >-
    100m-money-models.md, Section VI, Make Your Own Money Model, line 5974
  confirmations: 2
  boundary: >-
    A timescale the author sets on his own method: it is not a thirty-day build, even though it targets thirty-day profit.
  anchor_at: "100m-money-models.md:5974"
- id: D-money-models-086
  type: rule
  name: >-
    Continuity timing may fall outside the 30-day window
  statement: >-
    Sometimes the best timing for a Continuity Offer is after the first thirty days, and that is acceptable.
  why: >-
    It's better to make the offer at the right time than to try and force it at the wrong time.
  anchor: >-
    first thirty days, and that's OK. *It's better to make the offer at the
  source: >-
    100m-money-models.md, Section VI, Make Your Own Money Model, line 6004
  confirmations: 1
  boundary: >-
    The 30-day profit window does not override offer timing; the author lets the window slip rather than force the offer.
  anchor_at: "100m-money-models.md:6004"
- id: D-money-models-087
  type: antipattern
  name: >-
    Simple Scales. Fancy Fails.
  statement: >-
    Starting more businesses or building more products in order to have more offers.
  why: >-
    It's less about having 100 products to offer and more about having 100 ways to offer your product; one personal training service becomes many offers as one, two, three or four sessions per week. Affiliate products can fill Money Model gaps without the operational headache.
  anchor: >-
    have. Remember, it's less about having 100 products to offer, and more
  source: >-
    100m-money-models.md, Section VI, Important Notes, line 6031
  confirmations: 3
  anchor_at: "100m-money-models.md:6031"
- id: D-money-models-088
  type: rule
  name: >-
    You Can Mix And Match Offers However You Want
  statement: >-
    The order and placement the book uses is the author's own, not a constraint: upsell tactics can go in an Attraction Offer, a downsell process can be installed with every offer, and a Continuity Offer can attract new customers.
  why: >-
    The author learned many of these offers from people who used them differently than he does, and expects readers to use them another way; start with the way he suggests, then experiment.
  anchor: >-
    can do whatever you want. I show you stuff one way, *but I fully expect
  source: >-
    100m-money-models.md, Section VI, Important Notes, line 6084
  confirmations: 2
  boundary: >-
    Explicitly removes the sequence itself from the set of rules: most offers in the book meet the minimum requirement of a business (making a profit) on their own, at any time, in any order.
  anchor_at: "100m-money-models.md:6084"
```
