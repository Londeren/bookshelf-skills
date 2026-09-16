# Улов фазы 1 — $100M Money Models (2025) (ярус 1), тип B: правила и критерии

Группа `tier1-money-models`, слаг `money-models`, ярус 1. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **159** (экстрактор вернул 159, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-money-models.md` | 1–6495 | 7 | 159 |

## Как собран файл

Экстрактор B (Rules and criteria) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier1-money-models.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier1-money-models-B.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: B-money-models-001
  type: rule
  name: >-
    Offer at the moment of realization
  statement: >-
    Each offer in the sequence is placed at the moment the customer realizes they have the problem it solves, not earlier or later.
  why: >-
    Money Models find every opportunity to solve a customer's problem and then offer to solve it; timed right, the number of offers you can make is unlimited.
  anchor: >-
    order. If you offer the right thing when customers realize they need it,
  source: >-
    100m-money-models.md, Section I: What's A Money Model?, line 753
  confirmations: 3
  anchor_at: "100m-money-models.md:753"
- id: B-money-models-002
  type: rule
  name: >-
    Hard Selling Is For Weak Products
  statement: >-
    No one is talked into buying against their will; the offer is made available at the time the customer has the problem, and a no is left alone.
  why: >-
    Making offers available at the moment of the problem puts you ahead of the competition; if they do not want it, finding somebody who does is a numbers game.
  anchor: >-
    *OK*. Don't convince someone against their will. Make offers available
  source: >-
    100m-money-models.md, The Four Types of Offers That Make Money Models, Important Notes, line 975
  confirmations: 1
  anchor_at: "100m-money-models.md:975"
- id: B-money-models-003
  type: rule
  name: >-
    Obey The Law
  statement: >-
    Before an offer runs, a lawyer has checked whether it is legal in the jurisdiction, especially any offer using the word free.
  why: >-
    Advertising laws change all the time and tend to get tighter, especially around free; the book is Money Model inspiration, not legal cover.
  anchor: >-
    Check with lawyers to see if an offer you want to make is legal or not.
  source: >-
    100m-money-models.md, The Four Types of Offers That Make Money Models, Important Notes, line 986
  confirmations: 3
  anchor_at: "100m-money-models.md:986"
- id: B-money-models-004
  type: rule
  name: >-
    Be Transparent
  statement: >-
    The offer states facts as they are; if the facts are not compelling, reality or the framing is changed rather than the facts.
  why: >-
    Lying short-changes you long-term, and unlike credit card debt you cannot file bankruptcy on a bad reputation; once you have one it sticks for life.
  anchor: >-
    make them compelling or learn to frame them in a way that is. Don't lie.
  source: >-
    100m-money-models.md, The Four Types of Offers That Make Money Models, Important Notes, line 992
  confirmations: 1
  anchor_at: "100m-money-models.md:992"
- id: B-money-models-005
  type: rule
  name: >-
    If A Customer Asks For Their Money Back, Give It Back
  statement: >-
    A customer who asks for a refund gets it, whether or not the request is justified.
  why: >-
    If someone does not want you to have their money, you want it less than they do; the effort belongs on getting the next customer instead of on the headache.
  anchor: >-
    asks for a refund---entitled or not---*I give it to them.* Just focus on
  source: >-
    100m-money-models.md, Win Your Money Back, Important Notes, line 1265
  confirmations: 2
  anchor_at: "100m-money-models.md:1265"
- id: B-money-models-006
  type: rule
  name: >-
    Easy To Track
  statement: >-
    Every result or action a customer must hit to win their money back is simple to track, and the customer is trained on exactly what to do.
  why: >-
    Untracked or unexplained criteria get messed up; bonus points when people already track it, as phones track steps and cameras date photos.
  applies_when: >-
    Setting the criteria of a Win Your Money Back Offer.
  anchor: >-
    Actions, or both. And to make this work, you have to make the results
  source: >-
    100m-money-models.md, Win Your Money Back, Description, line 1149
  confirmations: 3
  anchor_at: "100m-money-models.md:1149"
- id: B-money-models-007
  type: rule
  name: >-
    Gets Customers Results
  statement: >-
    The criteria are realistic and are the things the best customers already do to get the best results, not a stretch target.
  why: >-
    Realistic criteria do just fine; if the criteria look too easy you have probably gotten close to realistic, and whatever the best customers do makes everyone get great results.
  anchor: >-
    *Realistic* criteria do just fine. If you think the criteria look too
  source: >-
    100m-money-models.md, Win Your Money Back, Important Notes, line 1282
  confirmations: 2
  anchor_at: "100m-money-models.md:1282"
- id: B-money-models-008
  type: rule
  name: >-
    Advertises The Business
  statement: >-
    At least one of the money-back criteria makes the customer advertise the business, by posting, tagging, referring or leaving a review.
  why: >-
    The customers who qualify do free advertising that brings their friends and family in.
  anchor: >-
    **3) Advertises The Business.** Make advertising the business part of
  source: >-
    100m-money-models.md, Win Your Money Back, Important Notes, line 1294
  confirmations: 3
  anchor_at: "100m-money-models.md:1294"
- id: B-money-models-009
  type: rule
  name: >-
    Have an upsell ready for the winnings
  statement: >-
    A Win Your Money Back Offer only runs when there is a next offer for winners to spend their winnings on.
  why: >-
    The money comes from those who do qualify and stay as customers, but they can only stay customers if they have something else to buy.
  anchor: >-
    something else to buy.* So have an upsell ready to apply their winnings
  source: >-
    100m-money-models.md, Win Your Money Back, Important Notes, line 1243
  confirmations: 2
  anchor_at: "100m-money-models.md:1243"
- id: B-money-models-010
  type: rule
  name: >-
    Refund rate below 5%
  statement: >-
    A Win Your Money Back Offer is only used when the business's refund rate is below 5%.
  why: >-
    Above that you risk giving too many refunds, and the product has to be fixed before the offer runs.
  anchor: >-
    ● Only use a Win Your Money Back Offer if your refund rate is below 5%.
  source: >-
    100m-money-models.md, Win Your Money Back, Summary Points, line 1416
  confirmations: 1
  anchor_at: "100m-money-models.md:1416"
- id: B-money-models-011
  type: rule
  name: >-
    Only offer it if you are OK giving money back
  statement: >-
    The offer is run only if the business can stomach roughly 10% of all customers asking for their money back.
  why: >-
    Data from thousands of gyms puts money-back requests at about 10% of customers (2025); when advertised well the extra customers and the follow-up offer more than outweigh the refunds.
  anchor: >-
    we've collected from thousands of gyms, about 10% of all customers will
  source: >-
    100m-money-models.md, Win Your Money Back, Important Notes, line 1251
  confirmations: 1
  anchor_at: "100m-money-models.md:1251"
- id: B-money-models-012
  type: rule
  name: >-
    Store credit advertised as free carries an unconditional guarantee
  statement: >-
    If winnings are paid in store credit but the offer is still advertised as free, the offer is paired with an unconditional satisfaction guarantee.
  why: >-
    Testing showed store credit and cash back pull the same number of customers, and adding the unconditional guarantee never materially changed how many people asked for their money back.
  anchor: >-
    as 'free,' pair it with an unconditional satisfaction guarantee. Adding
  source: >-
    100m-money-models.md, Win Your Money Back, Important Notes, line 1258
  confirmations: 1
  authors_caveat: >-
    Check with legal counsel in your area.
  anchor_at: "100m-money-models.md:1258"
- id: B-money-models-013
  type: rule
  name: >-
    How You Apply Store Credit
  statement: >-
    Winnings are applied to something that costs more than the winnings and spread over a longer period, not handed back as free months up front.
  why: >-
    People fall off if they do not pay something, so a discount over the long haul keeps them engaged over the long haul and makes you more money.
  applies_when: >-
    A customer has won their money back as store credit.
  anchor: >-
    Just offer to apply it to something that costs more than their winnings.
  source: >-
    100m-money-models.md, Win Your Money Back, Important Notes, line 1304
  confirmations: 2
  authors_caveat: >-
    They can use the credit however they want; this is only what you present first.
  anchor_at: "100m-money-models.md:1304"
- id: B-money-models-014
  type: rule
  name: >-
    All Meetings And Calls Provide Opportunities To Make More Offers
  statement: >-
    Check-in meetings are written into the money-back criteria and attendance at all of them is required to win.
  why: >-
    Beyond helping the customer succeed, the meetings are the best opportunities to make upsell offers based on the customer's feedback.
  anchor: >-
    Make check-in meetings part of your money-back criteria whenever you
  source: >-
    100m-money-models.md, Win Your Money Back, Important Notes, line 1333
  confirmations: 2
  anchor_at: "100m-money-models.md:1333"
- id: B-money-models-015
  type: rule
  name: >-
    Make Everyone A Winner
  statement: >-
    The program is sold as if the money comes back only on meeting the criteria, but about halfway through the next offer is made as if the customer has already won.
  why: >-
    It lowers the customer's anxiety about failing, keeps them longer and makes them like you more.
  anchor: >-
    through, make your next offer *as if they already won*. You lower the
  source: >-
    100m-money-models.md, Win Your Money Back, Important Notes, line 1354
  confirmations: 2
  anchor_at: "100m-money-models.md:1354"
- id: B-money-models-016
  type: rule
  name: >-
    At The End Of The Program, Let The Losers Win
  statement: >-
    A customer who refuses the first upsell and fails the challenge is still upsold, by crediting their entire deposit toward staying long term.
  why: >-
    We do not get customers to make a sale, we make sales to get customers.
  anchor: >-
    your first upsell *and* fails the challenge, you can *still* upsell them
  source: >-
    100m-money-models.md, Win Your Money Back, Important Notes, line 1366
  confirmations: 1
  anchor_at: "100m-money-models.md:1366"
- id: B-money-models-017
  type: rule
  name: >-
    Pick A Grand Prize
  statement: >-
    The Grand Prize is the thing you want everyone to buy, and it carries a stated monetary value that serves as the price anchor.
  why: >-
    Everyone who enters has shown interest in that thing, and the stated value is what makes the later discounted price look like savings.
  anchor: >-
    everyone to buy.* Make sure you assign a monetary value to your grand
  source: >-
    100m-money-models.md, Giveaways, Description, line 1536
  confirmations: 2
  anchor_at: "100m-money-models.md:1536"
- id: B-money-models-018
  type: rule
  name: >-
    Pick Your Promotional Offer
  statement: >-
    Everyone who does not win is offered the core offer enhanced by a discount, a bonus or a minor change from the Grand Prize that ethically justifies the price reduction.
  why: >-
    The Grand Prize works as the price anchor, and the bigger the discount against it, the more compelling the offer.
  anchor: >-
    your core offer with a discount, a bonus, or by minorly changing it from
  source: >-
    100m-money-models.md, Giveaways, Description, line 1542
  confirmations: 2
  anchor_at: "100m-money-models.md:1542"
- id: B-money-models-019
  type: rule
  name: >-
    Put The Giveaway On A Deadline To Add Urgency
  statement: >-
    The giveaway runs three to seven days from the start of promotion, with a daily update to entrants across all platforms until the winner is announced.
  why: >-
    A limited window adds urgency, and the daily countdown plus social proof keeps the hype alive.
  anchor: >-
    available for a limited time. I like three to seven days from the day I
  source: >-
    100m-money-models.md, Giveaways, Description, line 1571
  confirmations: 2
  anchor_at: "100m-money-models.md:1571"
- id: B-money-models-020
  type: rule
  name: >-
    Second deadline on claiming
  statement: >-
    The promotional offer given to non-winners expires in seven days, and that deadline is stated when they are notified.
  why: >-
    Putting an expiration date on claiming the prize makes people more likely to claim it.
  anchor: >-
    To make sure they redeem, add another deadline. Make claiming your
  source: >-
    100m-money-models.md, Giveaways, Description, line 1592
  confirmations: 2
  anchor_at: "100m-money-models.md:1592"
- id: B-money-models-021
  type: rule
  name: >-
    Explain The Cost-To-Value Using Their Discount
  statement: >-
    The discount on the core offer is set at 10%-30% of gross margins, and it is explained to the lead as the gap between the Grand Prize value and the price they pay.
  why: >-
    Compared against the value of the thing, a 10% discount off retail becomes a 64% difference in cost-to-value (2025 figures).
  anchor: >-
    thumb: make your core offer discount equal to 10%--30% of your gross
  source: >-
    100m-money-models.md, Giveaways, Description, line 1600
  confirmations: 1
  anchor_at: "100m-money-models.md:1600"
- id: B-money-models-022
  type: rule
  name: >-
    Somebody actually has to win the Grand Prize
  statement: >-
    A real winner is picked, and the Grand Prize, the qualifications to win and the fact that more than one person can win a prize are all clear in the published rules.
  why: >-
    These are no-brainers because of the way the author does business; everything beyond them is a question for legal counsel.
  anchor: >-
    like to do business: somebody actually has to win the Grand Prize. Make
  source: >-
    100m-money-models.md, Giveaways, Important Notes, line 1638
  confirmations: 1
  authors_caveat: >-
    I'm not legal counsel; ask your legal counsel about the rest.
  anchor_at: "100m-money-models.md:1638"
- id: B-money-models-023
  type: rule
  name: >-
    Cap entries at what you can call
  statement: >-
    The giveaway is advertised for seven days or until entries exceed the number of people you can call within seven days, whichever comes first.
  why: >-
    Any more entries than you have time and resources to connect with inside seven days would be a waste.
  anchor: >-
    ● Advertise your Giveaway for seven days, or until the number of leads
  source: >-
    100m-money-models.md, Giveaways, Summary Points, line 1736
  confirmations: 2
  anchor_at: "100m-money-models.md:1736"
- id: B-money-models-024
  type: rule
  name: >-
    Urgency, Urgency, Urgency
  statement: >-
    Deadlines are attached in three places: to enter, to claim and to use the prize.
  why: >-
    In short, always have deadlines; the call is scheduled the same or next day and the prize has hours to days of usable life.
  anchor: >-
    **Urgency, Urgency, Urgency.** I add urgency in three places---to enter,
  source: >-
    100m-money-models.md, Giveaways, Important Notes, line 1688
  confirmations: 1
  anchor_at: "100m-money-models.md:1688"
- id: B-money-models-025
  type: rule
  name: >-
    Have Downsells Available
  statement: >-
    If a non-winner refuses the promotional offer, the same percentage discount is offered on any other product that makes sense for them.
  why: >-
    Some will not or cannot buy the promotional offer even with the discount, and another product may suit that lead better.
  anchor: >-
    offer the same discount by percentage on any other product you have that
  source: >-
    100m-money-models.md, Giveaways, Important Notes, line 1702
  confirmations: 2
  anchor_at: "100m-money-models.md:1702"
- id: B-money-models-026
  type: rule
  name: >-
    If You Have A Recurring Revenue Business
  statement: >-
    In a recurring business the giveaway discount is spread over the longest period the customer will agree to, with billing set to resume at normal rates afterwards.
  why: >-
    It keeps the subscription running at full price once the discounted period ends.
  anchor: >-
    the longest period of time they'll agree to. Then, set up their monthly
  source: >-
    100m-money-models.md, Giveaways, Important Notes, line 1706
  confirmations: 1
  anchor_at: "100m-money-models.md:1706"
- id: B-money-models-027
  type: rule
  name: >-
    If Your Giveaway Doesn't Work, It Means Your Grand Prize Wasn't Grand Enough
  statement: >-
    When a giveaway gets little interest, the fix is a bigger or better-for-the-audience Grand Prize, not different advertising.
  why: >-
    Giveaway kind of explains itself, so if nobody bites the prize was not grand; a portfolio company swapped event tickets for a $50,000 equipment bundle plus a year of product and it crushed.
  anchor: >-
    if nobody bites, then I suggest you give away something better. Or at
  source: >-
    100m-money-models.md, Giveaways, Important Notes, line 1663
  confirmations: 1
  anchor_at: "100m-money-models.md:1663"
- id: B-money-models-028
  type: rule
  name: >-
    Give Away Two Prizes For Twice The Leads
  statement: >-
    To get referrals, two grand prizes are given away and entrants are told that if someone they refer wins, they win one too.
  why: >-
    It gives endless entries through referrals and makes referrers invested in the success of the people they refer, which keeps lead quality high.
  anchor: >-
    ● Give two prizes away if you want more people to refer. Tell them if
  source: >-
    100m-money-models.md, Giveaways, Summary Points, line 1720
  confirmations: 2
  anchor_at: "100m-money-models.md:1720"
- id: B-money-models-029
  type: rule
  name: >-
    How To Make Your Decoy Offer
  statement: >-
    The decoy is built from the premium offer by cutting components, using older models, removing personalization and removing every guarantee.
  why: >-
    The Attraction Offer only has to get leads to engage, nothing more.
  anchor: >-
    **How To Make Your Decoy Offer.** Offer fewer components, older models,
  source: >-
    100m-money-models.md, Decoy Offer, Important Notes, line 1924
  confirmations: 2
  anchor_at: "100m-money-models.md:1924"
- id: B-money-models-030
  type: rule
  name: >-
    Advertise Benefits Not The Features
  statement: >-
    The advertising sells the dream outcome and the transformation; product details appear only in the sales presentation.
  why: >-
    Private jets and rowboats both get you to an exotic island; the lead is bought on the outcome and sold on the details later.
  anchor: >-
    dream outcome. We advertise a *transformation* in 21 days, not workouts
  source: >-
    100m-money-models.md, Decoy Offer, Important Notes, line 1930
  confirmations: 1
  anchor_at: "100m-money-models.md:1930"
- id: B-money-models-031
  type: rule
  name: >-
    Make The Contrast Huge
  statement: >-
    The decoy is made as basic as reasonable and the premium option as awesome as possible, so the gap between them is as large as it can be.
  why: >-
    The value of the premium option comes from the difference with the decoy; the bigger the contrast, the better the deal and the more customers take it.
  anchor: >-
    huge differences with the decoy option. So make the decoy option as
  source: >-
    100m-money-models.md, Decoy Offer, Important Notes, line 1952
  confirmations: 2
  anchor_at: "100m-money-models.md:1952"
- id: B-money-models-032
  type: rule
  name: >-
    Discount Offers Have Higher Show-Up Rates Than Free Offers
  statement: >-
    A business with low appointment show-up rates runs a discount Attraction Offer instead of a free one.
  why: >-
    Free gets more leads, a discount gets fewer leads but a higher percentage who show up; that matters most where a no-show is expensive, as for doctors, lawyers and dentists.
  anchor: >-
    appointments, try a Discount Offer instead. This is especially important
  source: >-
    100m-money-models.md, Decoy Offer, Important Notes, line 1961
  confirmations: 1
  anchor_at: "100m-money-models.md:1961"
- id: B-money-models-033
  type: rule
  name: >-
    If Possible, Present The Premium Offer First
  statement: >-
    The premium offer is presented first and the decoy is kept back unless the lead asks for it or the law requires it to be presented.
  why: >-
    In a perfect world they take the premium offer immediately and the decoy stays in your back pocket.
  anchor: >-
    **If Possible, Present The Premium Offer First.** In a perfect world,
  source: >-
    100m-money-models.md, Decoy Offer, Important Notes, line 1965
  confirmations: 2
  anchor_at: "100m-money-models.md:1965"
- id: B-money-models-034
  type: rule
  name: >-
    Get Them To Give You Permission To Sell Them
  statement: >-
    When the decoy has to be presented, it is immediately contrasted with the premium offer, and only after both are on the table is the lead asked which will get them to their goal faster.
  why: >-
    At that point they have to name the premium offer, and you move forward in the sale mutually agreeing it is the best thing for them.
  applies_when: >-
    The lead asks for the decoy, or you are legally required to present it.
  anchor: >-
    contrast it with your premium offer. Then only after presenting both,
  source: >-
    100m-money-models.md, Decoy Offer, Important Notes, line 1981
  confirmations: 2
  anchor_at: "100m-money-models.md:1981"
- id: B-money-models-035
  type: rule
  name: >-
    Raise Prices Before Giving Stuff Away To Preserve Profits
  statement: >-
    Prices are permanently and honestly raised to accommodate the giveaway before a Buy X Get Y Free offer runs.
  why: >-
    The offer will work, and since it will work you need to make money on it; new customers all come in on this price, so the change makes sense for at least a season.
  anchor: >-
    need to make money. So, *permanently* raise prices to accommodate the
  source: >-
    100m-money-models.md, Buy X Get Y Free, Important Notes, line 2157
  confirmations: 1
  authors_caveat: >-
    Don't lie. Actually raise your prices.
  anchor_at: "100m-money-models.md:2157"
- id: B-money-models-036
  type: rule
  name: >-
    Give more free than paid
  statement: >-
    A Buy X Get Y Free offer gives more free items than the customer is asked to buy, so buy one get two beats buy two get one.
  why: >-
    Buy ten get two free is not as strong as buy two get ten free; it seems obvious, but people do not do it.
  anchor: >-
    ● Always try to give more free things than paid things.
  source: >-
    100m-money-models.md, Buy X Get Y Free, Summary Points, line 2259
  confirmations: 2
  anchor_at: "100m-money-models.md:2259"
- id: B-money-models-037
  type: rule
  name: >-
    Do Not Make Offers Like This If You Can't Manage Money
  statement: >-
    Before taking a year of payments up front, the money to service the customer for the whole agreement is budgeted and held back.
  why: >-
    Selling stuff you cannot deliver on breaks the law and ruins your reputation.
  anchor: >-
    *make sure you can deliver* for the whole year. Budget the correct
  source: >-
    100m-money-models.md, Buy X Get Y Free, Important Notes, line 2218
  confirmations: 2
  anchor_at: "100m-money-models.md:2218"
- id: B-money-models-038
  type: rule
  name: >-
    Make This Offer To Existing Customers For Fast Cash
  statement: >-
    When a Buy X Get Y Free offer is made to existing recurring customers for a cash pop, it is capped at 10% of the customer base.
  why: >-
    It gives a good cash pop while keeping recurring cash flow healthy.
  anchor: >-
    at their current price. Just limit the offer to 10% of your customers.
  source: >-
    100m-money-models.md, Buy X Get Y Free, Important Notes, line 2227
  confirmations: 2
  anchor_at: "100m-money-models.md:2227"
- id: B-money-models-039
  type: rule
  name: >-
    If Customers Only Buy Once, Make Them Buy Big
  statement: >-
    Where customers make a single purchase in their lifetime, the offer is built to make that one purchase as large as possible.
  why: >-
    If you only have one shot you may as well make it count, provided you supply the value to back it up.
  anchor: >-
    reason, it makes sense to make that purchase as large as possible. Just
  source: >-
    100m-money-models.md, Buy X Get Y Free, Important Notes, line 2241
  confirmations: 1
  anchor_at: "100m-money-models.md:2241"
- id: B-money-models-040
  type: rule
  name: >-
    Keep selling prepaid customers
  statement: >-
    Customers who have prepaid for a long duration keep getting new offers rather than being left alone until their term ends.
  why: >-
    They are the people who spend the most; months after prepaying their wallets have refreshed with new money.
  anchor: >-
    ● Keep selling customers who prepay long durations, they are the most
  source: >-
    100m-money-models.md, Buy X Get Y Free, Summary Points, line 2287
  confirmations: 2
  anchor_at: "100m-money-models.md:2287"
- id: B-money-models-041
  type: rule
  name: >-
    Promise A Clear Yes/No Result
  statement: >-
    The promise of a Pay Less Now or Pay More Later offer is simple, clear, measurable and deliverable inside the stated time frame.
  why: >-
    A promise that cannot be measured produces unnecessary cancellations; rate the pain 1-10 before and after and the result is not arguable.
  anchor: >-
    Keep the promise simple, clear, and measurable. This avoids unnecessary
  source: >-
    100m-money-models.md, Pay Less Now or Pay More Later, Important Notes, line 2412
  confirmations: 2
  anchor_at: "100m-money-models.md:2412"
- id: B-money-models-042
  type: rule
  name: >-
    Make a Conditional Satisfaction Guarantee
  statement: >-
    Cancelling the delayed charge is possible only for customers who met tracked conditions, and those conditions are the actions that get the most value out of the product.
  why: >-
    They cannot say you suck if they never tried it; aligning the conditions with value delivery makes it win-win.
  anchor: >-
    turning in data, etc. Make the criteria what people do to get the most
  source: >-
    100m-money-models.md, Pay Less Now or Pay More Later, Important Notes, line 2420
  confirmations: 2
  anchor_at: "100m-money-models.md:2420"
- id: B-money-models-043
  type: rule
  name: >-
    Pay Now discount of 20-50% plus bonuses
  statement: >-
    The pay now option carries a 20-50% discount and greater bonuses than the pay later option.
  why: >-
    Once someone has agreed to pay later you can get them to pay now with hefty discounts and valuable bonuses, and their card is already on file (2025 figures).
  anchor: >-
    now. Pay now* options provide a 20--50% discount and greater bonuses.
  source: >-
    100m-money-models.md, Pay Less Now or Pay More Later, Description, line 2350
  confirmations: 2
  anchor_at: "100m-money-models.md:2350"
- id: B-money-models-044
  type: rule
  name: >-
    Pay now is offered after pay later is accepted
  statement: >-
    The pay now option is presented only after the customer has accepted the pay later option, and taking it replaces the guarantee with the discount and bonuses.
  why: >-
    Almost anyone will agree to pay later if satisfied, and that agreement is what the pay now offer is made against.
  anchor: >-
    ○ Offer customers the *pay now* option after they accept the *pay later*
  source: >-
    100m-money-models.md, Pay Less Now or Pay More Later, Summary Points, line 2465
  confirmations: 2
  anchor_at: "100m-money-models.md:2465"
- id: B-money-models-045
  type: rule
  name: >-
    Optimizing Your Pay Now And Pay Later Offer
  statement: >-
    If too many people take pay later, the pay now discount or its bonuses are increased; if too many take pay now, they are reduced.
  why: >-
    The split between the two options is the dial that balances up front cash against volume.
  anchor: >-
    take your 'pay later' option, discount the 'pay now' option more, add
  source: >-
    100m-money-models.md, Pay Less Now or Pay More Later, Important Notes, line 2430
  confirmations: 1
  anchor_at: "100m-money-models.md:2430"
- id: B-money-models-046
  type: rule
  name: >-
    If More Than 10% Of Pay Later People Cancel Their Payment
  statement: >-
    A cancellation rate above 10% on the pay later option means the promise was too big, the guarantee conditions too low or the price too high, and one of the three is changed.
  why: >-
    No matter how well you deliver, some people will cancel; above 10% the offer itself is at fault (2025 benchmark).
  anchor: >-
    **If More Than 10% Of 'Pay Later' People Cancel Their Payment**. You
  source: >-
    100m-money-models.md, Pay Less Now or Pay More Later, Important Notes, line 2434
  confirmations: 2
  anchor_at: "100m-money-models.md:2434"
- id: B-money-models-047
  type: rule
  name: >-
    Attraction Offer covers customer and delivery several times over
  statement: >-
    The Attraction Offer is judged by whether the up front cash covers the cost of getting the customer and the cost of delivering, multiple times over.
  why: >-
    That is what lets you pay yourself back and get your next customer out of the same cash.
  anchor: >-
    cash to cover the cost of the customer and the cost to deliver our thing
  source: >-
    100m-money-models.md, Attraction Offers Conclusion, line 2598
  confirmations: 2
  anchor_at: "100m-money-models.md:2598"
- id: B-money-models-048
  type: rule
  name: >-
    The Classic Upsell bottom line
  statement: >-
    Whenever a problem appears that you can solve immediately, the solution is offered for money on the spot.
  why: >-
    Your core offer solves one problem and creates another, and current customers always have a higher chance of buying than strangers.
  anchor: >-
    **Bottom Line:** If a problem appears, and you can solve it
  source: >-
    100m-money-models.md, The Classic Upsell, Description, line 2771
  confirmations: 2
  anchor_at: "100m-money-models.md:2771"
- id: B-money-models-049
  type: rule
  name: >-
    Actually Do It
  statement: >-
    A business with only one thing to sell defines what it offers next before anything else.
  why: >-
    With one thing to sell you barely have a business, you have a front end; owners who actually added an upsell report 5x-ing the business.
  anchor: >-
    business---you have a front end. Figure out what you're gonna offer
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2810
  confirmations: 2
  anchor_at: "100m-money-models.md:2810"
- id: B-money-models-050
  type: rule
  name: >-
    Offer More Profitable Upsells First
  statement: >-
    When two upsells are available, the one with the higher profit is offered first.
  why: >-
    The order of offers decides which profit you capture before the customer stops buying.
  anchor: >-
    **Offer More Profitable Upsells First.** If I offer two products and one
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2814
  confirmations: 1
  anchor_at: "100m-money-models.md:2814"
- id: B-money-models-051
  type: rule
  name: >-
    Surprise And Delight
  statement: >-
    Closing bonuses are added one at a time, and everyone who buys receives all of them even if they said yes before the later ones were offered.
  why: >-
    It surprises and delights them, and it guarantees everyone gets the same thing so nobody feels left out later.
  anchor: >-
    add to get people who are on the fence to buy. Add one at a time. If
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2827
  confirmations: 1
  anchor_at: "100m-money-models.md:2827"
- id: B-money-models-052
  type: rule
  name: >-
    The Faster People Get Access To Stuff, The More They'll Value It
  statement: >-
    The upsell is made available as soon as possible, ideally placed in the customer's hands before they have said yes.
  why: >-
    The longer it takes to access something, the less value it has in the moment, and it is far harder to give something back than to say no.
  anchor: >-
    upsell, make it available as soon as you can. Bonus points if you put it
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2852
  confirmations: 2
  anchor_at: "100m-money-models.md:2852"
- id: B-money-models-053
  type: rule
  name: >-
    If You Bundle Upsells, Name Them
  statement: >-
    Bundled upsells are sold as one named package, named after the customer type or the result.
  why: >-
    It is easier to sell someone one thing than nine things, so one ask gets nine sales; and features can later be peeled out of the package as a downsell.
  anchor: >-
    **If You Bundle Upsells, Name Them.** It's easier to sell someone one
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2856
  confirmations: 2
  anchor_at: "100m-money-models.md:2856"
- id: B-money-models-054
  type: rule
  name: >-
    Integrate Upsells Into Your Other Offers
  statement: >-
    The thing you intend to sell next is built into the delivery of the thing they just bought.
  why: >-
    Meal plans that included supplement suggestions made people ask about supplements; training that suggested software led owners to buy it.
  anchor: >-
    buy them. Integrate the next thing you wanna sell into the first thing
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2870
  confirmations: 1
  anchor_at: "100m-money-models.md:2870"
- id: B-money-models-055
  type: rule
  name: >-
    Book-A-Meeting-From-A-Meeting (BAMFAM)
  statement: >-
    Every appointment ends with the next appointment scheduled, with the reason and the time agreed before the customer leaves.
  why: >-
    The more times you can upsell, the more people you will upsell; a customer should know the next time they see you and why before they leave.
  anchor: >-
    by scheduling the next appointment. Don't let them leave without
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2876
  confirmations: 2
  anchor_at: "100m-money-models.md:2876"
- id: B-money-models-056
  type: rule
  name: >-
    Upsell As Many Times As It Makes Sense To
  statement: >-
    There are as many upsell offers as there are problems you can solve for that customer.
  why: >-
    The second worst outcome is that they say no; the worst is that they would have said yes and were never asked.
  anchor: >-
    of upsells. Gym Launch had lots of upsells. Offer as many solutions as
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2883
  confirmations: 2
  anchor_at: "100m-money-models.md:2883"
- id: B-money-models-057
  type: rule
  name: >-
    Upsell Guarantees, Warranties, and Insurance
  statement: >-
    Guarantees, warranties and insurance are sold as a 5-50% addition to the price instead of being included free.
  why: >-
    An art studio that used to replace damaged portraits free now has 30% of customers paying an extra 10% for it, which is pure profit (2025 figures).
  anchor: >-
    *So instead of doing it for free, just add 5--50% onto the price in
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2893
  confirmations: 2
  anchor_at: "100m-money-models.md:2893"
- id: B-money-models-058
  type: rule
  name: >-
    Card On File
  statement: >-
    Payment is asked for by asking whether they want to use the card on file, not by asking them to produce a card.
  why: >-
    It lowers the hidden costs of buying: picking a card, taking it out, being reminded of ugly past buying decisions; make it easy and more people buy.
  anchor: >-
    Last, I make buying easy by asking if they want to use the card on file.
  source: >-
    100m-money-models.md, Menu Upsell, Description, line 3095
  confirmations: 3
  anchor_at: "100m-money-models.md:3095"
- id: B-money-models-059
  type: rule
  name: >-
    Prescription Upsell
  statement: >-
    A prescription upsell explains how the product integrates with what the customer already bought and gives personalized, detailed instructions for using it, instead of asking whether they want it.
  why: >-
    Explaining how to use it as if they already have it removes the option of not buying, which lowers the chance they do not buy.
  applies_when: >-
    Offering a choice is inconvenient and you have only one thing that solves the problem.
  anchor: >-
    important components. First, you have to explain how it integrates with
  source: >-
    100m-money-models.md, Menu Upsell, Description, line 3107
  confirmations: 2
  anchor_at: "100m-money-models.md:3107"
- id: B-money-models-060
  type: rule
  name: >-
    A/B Upsell
  statement: >-
    Where several products solve the same problem, the customer is asked which of two they prefer rather than whether they want one.
  why: >-
    When you give people the option to not buy, some do not buy; either choice in an A/B question results in an upsell.
  anchor: >-
    asking their preference. Instead of asking ***if*** customers wanted to
  source: >-
    100m-money-models.md, Menu Upsell, Description, line 3116
  confirmations: 3
  anchor_at: "100m-money-models.md:3116"
- id: B-money-models-061
  type: rule
  name: >-
    If You Make An A/B Offer, Add A Nudge
  statement: >-
    An A/B question put to a customer with little experience of the products carries a one-line nudge toward one option.
  why: >-
    These one-liners move sales along, and nudging one product harder moves that product faster.
  anchor: >-
    **If You Make An A/B Offer, Add A Nudge.** If your customers have
  source: >-
    100m-money-models.md, Menu Upsell, Important Notes, line 3214
  confirmations: 2
  anchor_at: "100m-money-models.md:3214"
- id: B-money-models-062
  type: rule
  name: >-
    If You've Sold Out Of It, Take Payment And Delay Delivery
  statement: >-
    When stock runs out, the sale is still made and the delivery expectation is set instead of the offer being withdrawn.
  why: >-
    It lets you sell far more selection without carrying inventory.
  anchor: >-
    collecting the cash and changing the delivery expectations. You'd be
  source: >-
    100m-money-models.md, Menu Upsell, Important Notes, line 3226
  confirmations: 1
  anchor_at: "100m-money-models.md:3226"
- id: B-money-models-063
  type: rule
  name: >-
    Employees Love Unselling
  statement: >-
    Employees are encouraged to help customers game the system on purpose by telling them what they do not need.
  why: >-
    Employees have inside knowledge, and using it to show customers how to get the most value means everyone wins.
  anchor: >-
    ● Encourage employees to unsell and "game the system" on purpose.
  source: >-
    100m-money-models.md, Menu Upsell, Summary Points, line 3259
  confirmations: 2
  anchor_at: "100m-money-models.md:3259"
- id: B-money-models-064
  type: rule
  name: >-
    Unsell the lower-margin items
  statement: >-
    What gets crossed off the menu is the lower-margin stuff, so the prescription lands on the higher-margin items.
  why: >-
    Unselling lower-margin stuff where appropriate incentivizes higher-margin upsells.
  anchor: >-
    ● Unselling lower-margin stuff where appropriate incentivizes
  source: >-
    100m-money-models.md, Menu Upsell, Summary Points, line 3256
  confirmations: 1
  anchor_at: "100m-money-models.md:3256"
- id: B-money-models-065
  type: rule
  name: >-
    If You Treat The Anchor Like A Fake, So Will The Customer
  statement: >-
    The premium anchor is genuinely sold and the conversation moves on only after the customer pauses, hesitates or asks for something else.
  why: >-
    If you go through the motions the person never really considered it, and you lose trust and waste time.
  anchor: >-
    hesitate, or ask for something else, do you move to the next thing.
  source: >-
    100m-money-models.md, Anchor Upsell, Important Notes, line 3404
  confirmations: 2
  anchor_at: "100m-money-models.md:3404"
- id: B-money-models-066
  type: rule
  name: >-
    Make A Premium Offer You Actually Want People To Buy
  statement: >-
    The anchor is an offer you would be happy to deliver if someone paid for it, presented as though you want them to take it.
  why: >-
    A made-up premium offer does not work; tweaking it into something the seller would be glad to deliver tripled one friend's profits, and if nobody takes it you have still anchored them.
  anchor: >-
    profits.* Actually present your premium offer like you *want* people to
  source: >-
    100m-money-models.md, Anchor Upsell, Important Notes, line 3411
  confirmations: 2
  anchor_at: "100m-money-models.md:3411"
- id: B-money-models-067
  type: rule
  name: >-
    Premium offer at 5-10x
  statement: >-
    The anchor offer is priced 5-10x the main offer.
  why: >-
    At that gap lots of people say no to the anchor and the main offer then looks like a much better deal, while some customers still buy the anchor (2025 figures).
  anchor: >-
    ● For the most effective anchor, make your premium offer 5--10x more
  source: >-
    100m-money-models.md, Anchor Upsell, Summary, line 3453
  confirmations: 2
  anchor_at: "100m-money-models.md:3453"
- id: B-money-models-068
  type: rule
  name: >-
    Same primary features, different secondary features
  statement: >-
    The main offer keeps the same primary features as the premium offer, and only secondary features are changed.
  why: >-
    Most people just want a suit; the material and designer are secondary, so offering the primary features for a fifth of the price makes the main offer a great deal.
  anchor: >-
    ● The main offer and the premium offer should have the same primary
  source: >-
    100m-money-models.md, Anchor Upsell, Summary, line 3465
  confirmations: 3
  anchor_at: "100m-money-models.md:3465"
- id: B-money-models-069
  type: rule
  name: >-
    Roll credit into something more expensive
  statement: >-
    The rollover credit is applied to an offer that costs more than what the customer previously bought.
  why: >-
    That is how the rollover makes money rather than just giving away what they already paid for.
  anchor: >-
    Roll their credit over to something more expensive.
  source: >-
    100m-money-models.md, Rollover Upsell, Description, line 3574
  confirmations: 2
  anchor_at: "100m-money-models.md:3574"
- id: B-money-models-070
  type: rule
  name: >-
    How To Price Your Rollover Upsell
  statement: >-
    The offer the credit rolls into is priced at least 4x the credit given.
  why: >-
    At 4x, applying the whole first purchase discounts the new offer by 25% at most, so profit is left after the discount.
  anchor: >-
    ● Price your next offer *at least* 4x higher than the credit. This makes
  source: >-
    100m-money-models.md, Rollover Upsell, Summary Points, line 3700
  confirmations: 2
  anchor_at: "100m-money-models.md:3700"
- id: B-money-models-071
  type: rule
  name: >-
    Do Rollover Upsells before refunding
  statement: >-
    Before any refund is issued, the purchase is offered as credit toward a do-over or toward a different product.
  why: >-
    It has saved the author tons of customers and cash.
  anchor: >-
    **Do Rollover Upsells** ***before*** **refunding.** This has saved me
  source: >-
    100m-money-models.md, Rollover Upsell, Important Notes, line 3639
  confirmations: 2
  anchor_at: "100m-money-models.md:3639"
- id: B-money-models-072
  type: rule
  name: >-
    Previous Customers Are Still Customers. Upsell Them.
  statement: >-
    Customers with six or more months since their last purchase are contacted with a rollover credit toward returning.
  why: >-
    200 personalized winback videos offering $4,000 of credit converted about 20% and produced roughly $1,900,000 of annual revenue from one day of recording (2025 figures).
  anchor: >-
    old customers (6+ months since last purchase). Look at how much they
  source: >-
    100m-money-models.md, Rollover Upsell, Important Notes, line 3645
  confirmations: 2
  anchor_at: "100m-money-models.md:3645"
- id: B-money-models-073
  type: rule
  name: >-
    Add Urgency To Rollover Upsells. Make Them One-Time Only.
  statement: >-
    The rollover credit is a once-in-a-customer-lifetime offer that has to be taken at the moment it is presented.
  why: >-
    They do not get to sleep on it; the surprise is the point, and if they pass they can still pay full price later.
  anchor: >-
    **Add Urgency To Rollover Upsells. Make Them One-Time Only.** If you're
  source: >-
    100m-money-models.md, Rollover Upsell, Important Notes, line 3653
  confirmations: 2
  anchor_at: "100m-money-models.md:3653"
- id: B-money-models-074
  type: rule
  name: >-
    They Said No To This Offer, Not All Offers
  statement: >-
    A no is treated as a no to this offer only, and another offer is made instead of ending the conversation.
  why: >-
    It hurts when someone rejects you, but a no is an opportunity to find out what they really want and profit from it.
  anchor: >-
    make another offer. *No means no for this thing, not no for everything.*
  source: >-
    100m-money-models.md, Section IV: Downsell Offers, The Rules of Downselling, line 3776
  confirmations: 2
  anchor_at: "100m-money-models.md:3776"
- id: B-money-models-075
  type: rule
  name: >-
    Downsells Are Trades
  statement: >-
    Every concession in a downsell is exchanged for something from the customer; if you give something, you get something.
  why: >-
    Downselling works by finding combinations of giving and getting until you get a match.
  anchor: >-
    **Downsells Are Trades.** When downselling, you work with the customer
  source: >-
    100m-money-models.md, Section IV: Downsell Offers, The Rules of Downselling, line 3778
  confirmations: 1
  anchor_at: "100m-money-models.md:3778"
- id: B-money-models-076
  type: rule
  name: >-
    Personalize, Don't Pressure
  statement: >-
    The downsell offers more of what the customer likes and less of what they do not, with a price to match, rather than pressure to take the original offer.
  why: >-
    Asking is not offensive; if you can serve them better it would be offensive not to ask.
  anchor: >-
    **Personalize, Don\'t Pressure.** Figure out what they like and don't
  source: >-
    100m-money-models.md, Section IV: Downsell Offers, The Rules of Downselling, line 3782
  confirmations: 2
  anchor_at: "100m-money-models.md:3782"
- id: B-money-models-077
  type: rule
  name: >-
    Offer The Same Things In New Ways
  statement: >-
    Downsells are built out of what the business already sells, not out of new products created for the occasion.
  why: >-
    Otherwise you create a hundred businesses' worth of products and problems; downselling is a hundred ways to offer the stuff you already have.
  anchor: >-
    just think of downselling more like a hundred ways to offer the stuff
  source: >-
    100m-money-models.md, Section IV: Downsell Offers, The Rules of Downselling, line 3794
  confirmations: 2
  anchor_at: "100m-money-models.md:3794"
- id: B-money-models-078
  type: rule
  name: >-
    Don't Drop Your Price Just To Get Somebody To Buy
  statement: >-
    The price of a thing is never lowered in the moment to win a sale; only the payment schedule or the contents of the offer change.
  why: >-
    Dropping the price is discounting, not downselling; customers talk, and someone finding out another got the same thing cheaper just because is both an upset and an ethical problem.
  anchor: >-
    do, don't change the price just to get someone to buy because...
  source: >-
    100m-money-models.md, Section IV: Downsell Offers, The Rules of Downselling, line 3802
  confirmations: 3
  anchor_at: "100m-money-models.md:3802"
- id: B-money-models-079
  type: rule
  name: >-
    Customers Talk About Price
  statement: >-
    Price tests are planned in advance, fixing the price and the number of people it is offered to, rather than decided during a sales conversation.
  why: >-
    That is different from charging somebody less in the moment because you were scared of losing the sale.
  anchor: >-
    your thing at a specific price, to a specific number of people, *ahead
  source: >-
    100m-money-models.md, Section IV: Downsell Offers, The Rules of Downselling, line 3805
  confirmations: 1
  anchor_at: "100m-money-models.md:3805"
- id: B-money-models-080
  type: rule
  name: >-
    Reward For Paying In Full Rather Than Punish For Paying Over Time
  statement: >-
    The price is quoted with the interest already included and prepayment is offered as a discount, instead of adding interest to a payment plan.
  why: >-
    Same math, but it feels better: the offer is friendlier and the full price works as a price anchor.
  anchor: >-
    *with interest included*. Then, I offer prepayment as a way to get a
  source: >-
    100m-money-models.md, Payment Plan Downsells, Example Of Payment Plan Downsell Process, line 3948
  confirmations: 2
  anchor_at: "100m-money-models.md:3948"
- id: B-money-models-081
  type: rule
  name: >-
    Schedule payments on paycheck dates
  statement: >-
    Payment dates are scheduled against the customer's paycheck dates rather than as monthly instalments.
  why: >-
    Most people get paid every two weeks, which boosts 30-day profit far more than monthly payments, and charging on payday means fewer declines.
  anchor: >-
    paid. Fair enough?"* I like scheduling payments off of paychecks since
  source: >-
    100m-money-models.md, Payment Plan Downsells, Example Of Payment Plan Downsell Process, line 3984
  confirmations: 3
  anchor_at: "100m-money-models.md:3984"
- id: B-money-models-082
  type: rule
  name: >-
    Get Fewer Declined Payments
  statement: >-
    A declined card is re-run several times over the same day rather than treated as a failed payment.
  why: >-
    Paychecks get deposited at different times; the author recoups about a third of declined payments with this step, learned from John, an early mentor.
  anchor: >-
    times, so if at first it gets declined, run it a few times that day. I
  source: >-
    100m-money-models.md, Payment Plan Downsells, Important Notes, line 4052
  confirmations: 1
  anchor_at: "100m-money-models.md:4052"
- id: B-money-models-083
  type: rule
  name: >-
    Check To See If They Still Want The Thing
  statement: >-
    After the payment plan options run out, the customer is asked on a 1-10 scale how badly they want it, and payment plans continue only at 8 or above.
  why: >-
    No payment plan will satisfy a customer who does not want the thing, so effort is only spent where the desire is there.
  anchor: >-
    wanna do this?"* If they say 8 or above, keep offering payment plans and
  source: >-
    100m-money-models.md, Payment Plan Downsells, Example Of Payment Plan Downsell Process, line 3995
  confirmations: 2
  anchor_at: "100m-money-models.md:3995"
- id: B-money-models-084
  type: rule
  name: >-
    Seven or below means a different offer
  statement: >-
    A customer who rates their desire 7 or below is asked why not a 10 and is then sold a different thing rather than another payment plan.
  why: >-
    The answer tells you they are a better fit for something else, which is what Feature Downsells are for.
  anchor: >-
    happen for you."* If they say 7 or below, ask *"Why not a 10?"* and
  source: >-
    100m-money-models.md, Payment Plan Downsells, Example Of Payment Plan Downsell Process, line 3997
  confirmations: 2
  anchor_at: "100m-money-models.md:3997"
- id: B-money-models-085
  type: rule
  name: >-
    How To Make Sure Payment Plans Make You Money
  statement: >-
    After payment plans are introduced, the share of appointments paying in full must stay the same while the overall close rate rises.
  why: >-
    If the number of paid-in-fulls drops you have put people who would have paid in full onto payment plans, which is where payment plans lose the most money.
  anchor: >-
    appointments overall but with the same percentage of appointments paying
  source: >-
    100m-money-models.md, Payment Plan Downsells, Important Notes, line 4060
  confirmations: 2
  anchor_at: "100m-money-models.md:4060"
- id: B-money-models-086
  type: rule
  name: >-
    Start High Before Working Your Way Down
  statement: >-
    Pricing is always presented in order from most cash up front to least.
  why: >-
    Profitwell churn data from 14,000 businesses: monthly billing gave 10.7% monthly cancellations, quarterly 5%, annual 2%, so fewer bigger payments also make customers more valuable long term (2025 citation).
  anchor: >-
    term. So start high (fewer bigger payments) and work your way down.
  source: >-
    100m-money-models.md, Payment Plan Downsells, Important Notes, line 4084
  confirmations: 2
  anchor_at: "100m-money-models.md:4084"
- id: B-money-models-087
  type: rule
  name: >-
    Payment Plans Have Built-In Upsells
  statement: >-
    Customers on a payment plan are periodically offered the original paid-in-full discount if they clear the balance.
  why: >-
    Customers forget they have the option and some jump at it; if you incentivize people to pay faster, they pay faster.
  anchor: >-
    off the balance, they can still get the original 'prepay discount.' This
  source: >-
    100m-money-models.md, Payment Plan Downsells, Important Notes, line 4041
  confirmations: 2
  anchor_at: "100m-money-models.md:4041"
- id: B-money-models-088
  type: rule
  name: >-
    Seesaw Downselling
  statement: >-
    With inexperienced salespeople the payment plan is opened by asking whether they would rather have giant monthly payments or tiny ones, then adjusting the down payment until the monthly rate suits.
  why: >-
    It frames the payment plan as the negative option and highlights the benefits of prepaying, while still incentivizing bigger down payments.
  applies_when: >-
    You prefer fewer steps, or have less experienced salespeople.
  anchor: >-
    process. Instead of asking for the full amount, just ask *"Would you
  source: >-
    100m-money-models.md, Payment Plan Downsells, Important Notes, line 4024
  confirmations: 1
  anchor_at: "100m-money-models.md:4024"
- id: B-money-models-089
  type: rule
  name: >-
    Trial criteria activate and retain customers
  statement: >-
    The terms of a Trial With Penalty are criteria that activate and retain customers, taken from the Win Your Money Back criteria.
  why: >-
    By the end of the trial they have done the things that make great long-term customers and that advertise the business for free.
  anchor: >-
    rather than giving less---if you can afford it. The criteria should
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4286
  confirmations: 3
  anchor_at: "100m-money-models.md:4286"
- id: B-money-models-090
  type: rule
  name: >-
    Offer The Trial Last
  statement: >-
    The Trial With Penalty is offered only after the customer has made clear they will not take the first offer.
  why: >-
    Used as a downsell it changes only what they pay today, not what they pay in total, and it saves the people who would otherwise be lost to a no.
  anchor: >-
    **Offer The Trial Last.** If someone makes it clear they don\'t want
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4303
  confirmations: 3
  anchor_at: "100m-money-models.md:4303"
- id: B-money-models-091
  type: rule
  name: >-
    Always Get A Credit Card
  statement: >-
    No trial starts without a card on file; a customer who refuses to leave one is shown out.
  why: >-
    The penalty mechanism only exists if there is a card to charge; if they balk, the answer is that this is just how we have always done it.
  anchor: >-
    we've always done it."* If they still refuse, wish them a lovely day and
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4317
  confirmations: 2
  anchor_at: "100m-money-models.md:4317"
- id: B-money-models-092
  type: rule
  name: >-
    Always Sell Staying And Paying
  statement: >-
    Before the trial begins the customer agrees out loud that they will stay long term if the program gets them the result; without that agreement no trial is given.
  why: >-
    There is no point giving a trial to someone who will not stay, and setting the expectation keeps you from promising a quick fix you cannot ethically deliver.
  anchor: >-
    staying long-term if you get them results. If they say no, there's no
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4326
  confirmations: 2
  anchor_at: "100m-money-models.md:4326"
- id: B-money-models-093
  type: rule
  name: >-
    Explain the fees after getting their card
  statement: >-
    The penalty fees are explained after the card has been taken, not before.
  why: >-
    Explaining the fees before you get the card brings more resistance; explained afterwards, with a this-is-how-we-have-always-done-it attitude, the take rate is higher.
  anchor: >-
    **Explain the fees** ***after*** **getting their card.** I say something
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4346
  confirmations: 2
  anchor_at: "100m-money-models.md:4346"
- id: B-money-models-094
  type: rule
  name: >-
    Initial next to the fee clauses
  statement: >-
    Customers initial separately next to the fee clauses in the agreement.
  why: >-
    It forces the sales team to explain them; people still have to agree to the fees.
  anchor: >-
    initial separately next to the fee clauses to force my sales guys to
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4359
  confirmations: 2
  anchor_at: "100m-money-models.md:4359"
- id: B-money-models-095
  type: rule
  name: >-
    Make Check-ins Required
  statement: >-
    All criteria are explained up front and the check-in meetings are made required terms of the trial, with the benefit of each one named.
  why: >-
    The check-ins are the upsell opportunities, and charging for missing them is the only way to get the customer results.
  anchor: >-
    **Make Check-ins Required.** First, we explain *all* criteria so they
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4366
  confirmations: 2
  anchor_at: "100m-money-models.md:4366"
- id: B-money-models-096
  type: rule
  name: >-
    Breaking Up Fees vs. One Lump Fee
  statement: >-
    The penalty is split into a small fee per missed criterion rather than one lump fee on the first miss.
  why: >-
    The author prefers billing $50 for each mess up over one $500 fee; a lump fee fits only where missing once really ruins the customer's result.
  anchor: >-
    ten things to do. I'd rather bill \$50 for each mess up than one \$500
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4291
  confirmations: 2
  authors_caveat: >-
    I've seen both work.
  anchor_at: "100m-money-models.md:4291"
- id: B-money-models-097
  type: rule
  name: >-
    Tweak Your Trial To Get The Most Customers
  statement: >-
    If nobody takes the trial, the requirements or penalties are lowered; if people take it but do not follow through, the explanation of how the fees help them is strengthened and sales meetings are made mandatory.
  why: >-
    Each failure mode of the trial points at a specific part of the offer to change.
  anchor: >-
    Trial, lower the requirements or penalties. If people take your Trial
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4408
  confirmations: 1
  anchor_at: "100m-money-models.md:4408"
- id: B-money-models-098
  type: rule
  name: >-
    Reach non-starters before billing them
  statement: >-
    A customer who never used the trial is contacted several times and offered a waiver of the fee in exchange for a meeting before any fee is billed.
  why: >-
    The author does not like billing non-starters: a small fee is not worth a 1-star review.
  anchor: >-
    that you need to meet with them. Offer to waive the fee if they do. Now,
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4400
  confirmations: 1
  authors_caveat: >-
    But hey, it's your choice.
  anchor_at: "100m-money-models.md:4400"
- id: B-money-models-099
  type: rule
  name: >-
    If they hate it, do not blame them
  statement: >-
    When a trial customer is unhappy, the blame is taken by the business, and the higher level offer is then made to them on the basis of what you now understand about their needs.
  why: >-
    Only one person can be angry and it needs to be you; about half of these people buy.
  anchor: >-
    yourself for missing this. *Do not blame them.* Only one person can be
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4390
  confirmations: 1
  anchor_at: "100m-money-models.md:4390"
- id: B-money-models-100
  type: rule
  name: >-
    Let People Make Up For Goofs
  statement: >-
    A customer who has been billed for a miss is offered a way to make it up; only if they miss that too is the billing justified.
  why: >-
    People get discouraged after getting billed, and the make-up gets them back on track and converting.
  anchor: >-
    getting billed. But, you can offer an opportunity to 'make it up.' This
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4417
  confirmations: 1
  anchor_at: "100m-money-models.md:4417"
- id: B-money-models-101
  type: rule
  name: >-
    Just Call It A Trial
  statement: >-
    The offer is called a Free Trial in all customer-facing language, never a trial with a penalty.
  why: >-
    Otherwise people get scared and confused; nobody wants to be penalized.
  anchor: >-
    'special features,' you should just call it a Free Trial. Otherwise,
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4422
  confirmations: 1
  anchor_at: "100m-money-models.md:4422"
- id: B-money-models-102
  type: rule
  name: >-
    Pay Less Now or Pay More Later vs. Trial With Penalty
  statement: >-
    Pay Less Now or Pay More Later is the downsell for physical products and one-time services; Trial With Penalty is the downsell for recurring products and services.
  why: >-
    That is how the author has made each of them work.
  anchor: >-
    one-time services. And I use Trial With Penalty as a downsell for
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4430
  confirmations: 1
  authors_caveat: >-
    I have only made this work in businesses where the customer has to do work to get results.
  anchor_at: "100m-money-models.md:4430"
- id: B-money-models-103
  type: rule
  name: >-
    Discounts Get Cards on File
  statement: >-
    Where asking for a card against a free offer meets resistance, a very low first-month price is charged instead of nothing.
  why: >-
    The small price means the card will probably work when the automatic payments start.
  anchor: >-
    probably work when the automatic payments start. So instead of a free
  source: >-
    100m-money-models.md, Trial With Penalty, Important Notes, line 4438
  confirmations: 1
  anchor_at: "100m-money-models.md:4438"
- id: B-money-models-104
  type: rule
  name: >-
    Remove features from highest to lowest value
  statement: >-
    Feature Downsells strip features in order from the highest-value one downwards.
  why: >-
    People weigh money saved against value lost, so removing the most valuable thing first gets customers to re-upsell themselves onto the more expensive offer.
  anchor: >-
    means you want to *remove features from highest to lowest value.* Since
  source: >-
    100m-money-models.md, Feature Downsells, Description, line 4582
  confirmations: 2
  anchor_at: "100m-money-models.md:4582"
- id: B-money-models-105
  type: rule
  name: >-
    Never Negotiate The Price
  statement: >-
    Someone who wants to pay less for the same thing is given a payment plan if they want to pay less now and a feature downsell if they want to pay less overall, never a lower price for the same offer.
  why: >-
    People who demand to pay less for the same thing are business terrorists, and the author does not negotiate with terrorists.
  anchor: >-
    terrorists. If they want to pay less now---offer a payment plan. If they
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4681
  confirmations: 2
  anchor_at: "100m-money-models.md:4681"
- id: B-money-models-106
  type: rule
  name: >-
    Maintain The Position Of A Helpful Guide
  statement: >-
    The downselling conversation stays collaborative, framed as finding the best deal for the customer rather than pushing.
  why: >-
    If you act pushy your offers exhaust customers faster; as a helpful guide you can downsell as many offers as necessary without exhausting them.
  anchor: >-
    pushy, your offers will exhaust customers faster. If you stay a helpful
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4688
  confirmations: 2
  anchor_at: "100m-money-models.md:4688"
- id: B-money-models-107
  type: rule
  name: >-
    How I Standardize My Downsell Process
  statement: >-
    The first downsell cuts something valuable and lowers the price only a little; only if that fails do further features come off with bigger price drops.
  why: >-
    The first cut is there to make them reconsider the original offer and price; after that it is better for the customer to get something than nothing.
  anchor: >-
    valuable and lower the price *a little*. I do this to get them to
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4702
  confirmations: 2
  anchor_at: "100m-money-models.md:4702"
- id: B-money-models-108
  type: rule
  name: >-
    Name Your Feature Combinations
  statement: >-
    Each feature combination is a named package, with the most expensive one named after a status the customer finds aspirational.
  why: >-
    It works the way airlines run First Class, Business Class and Economy.
  anchor: >-
    **Name Your Feature Combinations.** Name the most expensive combination
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4707
  confirmations: 1
  anchor_at: "100m-money-models.md:4707"
- id: B-money-models-109
  type: rule
  name: >-
    Name the cheapest combination The Minimum
  statement: >-
    The cheapest package is called The Minimum, and a customer who rejects everything else is asked whether they want nothing more than the minimum package.
  why: >-
    The name implies they have to get at least that thing, and the question gets them to say no in order to say yes, as in the Classic Upsell.
  anchor: >-
    **I Name My Cheapest Combination "The Minimum."** I like it because it
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4714
  confirmations: 1
  anchor_at: "100m-money-models.md:4714"
- id: B-money-models-110
  type: rule
  name: >-
    Temperature Check After Two Downsells
  statement: >-
    After two feature changes in a row are refused, the customer is asked on a 1-10 scale how badly they want the thing before any further downsell.
  why: >-
    It is the same check as in payment plan downselling: no combination of features will satisfy someone who does not want the thing.
  anchor: >-
    make two changes in a row and they still refuse, make sure they really
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4720
  confirmations: 2
  anchor_at: "100m-money-models.md:4720"
- id: B-money-models-111
  type: rule
  name: >-
    Alternate feature and payment plan downsells
  statement: >-
    A customer at 8 or above moves to payment plan downselling; at 7 or below they are asked what a 10 would look like and the features are recombined.
  why: >-
    Alternating between payment plan and feature downsells in the same sale makes you very difficult to refuse.
  anchor: >-
    If they say 7 or below, ask *"What would a 10 look like?"* and then,
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4726
  confirmations: 2
  anchor_at: "100m-money-models.md:4726"
- id: B-money-models-112
  type: rule
  name: >-
    After Each Downsell, Ask Deal? Or Fair Enough?
  statement: >-
    Every downsell ends with a direct Deal? or Fair enough?
  why: >-
    It works astonishingly well: fewer people will watch you change the offer for them and then call it unfair.
  anchor: >-
    **After Each Downsell, Ask "Deal?" Or "Fair Enough?"** This works
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4731
  confirmations: 1
  anchor_at: "100m-money-models.md:4731"
- id: B-money-models-113
  type: rule
  name: >-
    Free Orientations Boost Do-It-Yourself Feature Downsells
  statement: >-
    A lead who has refused every done-for-you offer is invited to a free orientation, at the end of which a do-it-yourself product solving the same problem is offered.
  why: >-
    About half of those invited showed up and almost all of them bought supplements, which is money from people who would otherwise have said no.
  anchor: >-
    orientation, I offer a DIY product that solves the same problem as the
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4741
  confirmations: 1
  anchor_at: "100m-money-models.md:4741"
- id: B-money-models-114
  type: rule
  name: >-
    Feature Downsell Your Guarantees
  statement: >-
    If the offer has a guarantee, removing it is a standard step of the Feature Downsell process.
  why: >-
    People value security, so removing the guarantee makes many of them see its value and flips an initial no back to a yes on the full-price offer.
  anchor: >-
    make removing it part of your Feature Downsell process. People value
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4749
  confirmations: 2
  anchor_at: "100m-money-models.md:4749"
- id: B-money-models-115
  type: rule
  name: >-
    Feature Downsell Current Customers
  statement: >-
    A current customer who is not using a feature is offered a lower price for only the features they use, before they cancel.
  why: >-
    Customers who use all the features they pay for stay longer; customers downsold into a package just for them have the second highest value of all the author's customers.
  anchor: >-
    you see a customer isn't using a feature, offer a lower price---only
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4755
  confirmations: 2
  anchor_at: "100m-money-models.md:4755"
- id: B-money-models-116
  type: rule
  name: >-
    Barter With Reviews, Testimonials, And Referrals
  statement: >-
    A discount given against a price objection is traded for advertising: reviews, a video testimonial, public progress posts and introductions.
  why: >-
    The advertising is worth more than the discount to the business and the money is worth more than the advertising to the customer, so both sides win.
  anchor: >-
    bartering. If I get a price objection, sometimes I offer discounts in
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4765
  confirmations: 2
  anchor_at: "100m-money-models.md:4765"
- id: B-money-models-117
  type: rule
  name: >-
    Make Continuity Offers last
  statement: >-
    Continuity is offered after the Attraction, Upsell and Downsell offers, not used as the Attraction Offer on its own.
  why: >-
    Continuity attracts more customers but crashes 30-day profits; placed last it takes cash today from the other offers and stacks recurring cash for tomorrow.
  anchor: >-
    By making continuity offers *last,* we get the best of all worlds. We
  source: >-
    100m-money-models.md, Section V: Continuity Offers, line 4885
  confirmations: 3
  authors_caveat: >-
    You can make Continuity Offers wherever and however you want; they can attract, upsell, downsell or re-engage.
  anchor_at: "100m-money-models.md:4885"
- id: B-money-models-118
  type: rule
  name: >-
    Ongoing value means ongoing payments
  statement: >-
    Something is put on continuity only when the customer keeps getting ongoing value from it; a one-off deliverable paid for over time is a payment plan, not continuity.
  why: >-
    It is silly for someone to pay for a one-day workshop forever, and equally a mistake to charge one price to provide a service forever.
  anchor: >-
    get ongoing value, it probably makes sense for them to make ongoing
  source: >-
    100m-money-models.md, Section V: Continuity Offers, line 4899
  confirmations: 1
  anchor_at: "100m-money-models.md:4899"
- id: B-money-models-119
  type: rule
  name: >-
    The bonus outweighs the first continuity payment
  statement: >-
    The sign-up bonus on a Continuity Offer is worth more than the first continuity payment.
  why: >-
    That is what makes people start; more good stuff added and costs taken away gets more people onto continuity.
  anchor: >-
    sign up today. Typically, the bonus itself has more value than the first
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Description, line 4992
  confirmations: 2
  anchor_at: "100m-money-models.md:4992"
- id: B-money-models-120
  type: rule
  name: >-
    Focus On The Bonus, Not The Membership
  statement: >-
    The advertising for a Continuity Offer sells the free valuable thing, and the membership is explained only after the lead shows interest.
  why: >-
    Join my membership program is nowhere near as compelling as get this free valuable thing.
  anchor: >-
    **Focus On The Bonus, Not The Membership.** "Join my membership program"
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, line 5053
  confirmations: 2
  anchor_at: "100m-money-models.md:5053"
- id: B-money-models-121
  type: rule
  name: >-
    Keep Your Bonuses Related To Your Core Offer
  statement: >-
    The bonus is closely related to the core offer being sold.
  why: >-
    A bonus that is too different attracts the wrong customers: a free t-shirt sells t-shirt printing, not tech services.
  anchor: >-
    **Keep Your Bonuses Related To Your Core Offer.** If the bonus is too
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, line 5064
  confirmations: 2
  anchor_at: "100m-money-models.md:5064"
- id: B-money-models-122
  type: rule
  name: >-
    Make Bonuses Things You Already Have And Do
  statement: >-
    Bonuses are made out of things the business already has and already does, priced and given as bonuses.
  why: >-
    Past newsletters cost no extra time but carry high value, and onboarding has to happen anyway, so you might as well put a price on it; if you value it, they will too.
  anchor: >-
    **Make Bonuses Things You Already Have And Do.** For instance, the two
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, line 5069
  confirmations: 2
  anchor_at: "100m-money-models.md:5069"
- id: B-money-models-123
  type: rule
  name: >-
    Use Realistic Bonus Pricing
  statement: >-
    The value stated on a bonus is a believable one, ideally a price the business has actually charged for that thing before.
  why: >-
    A made-up value will not anchor the customer and loses their trust.
  anchor: >-
    anchor believable. Some business owners make up ridiculous values. Don't
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, line 5087
  confirmations: 1
  anchor_at: "100m-money-models.md:5087"
- id: B-money-models-124
  type: rule
  name: >-
    Anchor The Bonuses
  statement: >-
    The value and benefits of the bonus are sold before the customer is told how to get it for free.
  why: >-
    The high-value bonus works as the anchor: it may shock them, and that is the point at which you ask whether they want to know how to get it free.
  anchor: >-
    ● Sell the value of the bonus *before* telling them how they can get it
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Summary Points, line 5221
  confirmations: 2
  anchor_at: "100m-money-models.md:5221"
- id: B-money-models-125
  type: rule
  name: >-
    More Bonuses Get More People To Join
  statement: >-
    When bonuses are stacked, the individual dollar value of each one is named.
  why: >-
    Mentioning the individual dollar values anchors the value, and stacking them this way gets even more people to join the continuity.
  anchor: >-
    *Mention the individual dollar values of each to anchor the value.*
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, line 5119
  confirmations: 1
  anchor_at: "100m-money-models.md:5119"
- id: B-money-models-126
  type: rule
  name: >-
    Making Bonuses Available Only To Those Who Join
  statement: >-
    To force everyone into continuity, the bonuses are made available only to those who join the membership.
  why: >-
    Offering continuity as the only option is what stops people taking the bonus without the subscription.
  anchor: >-
    option. In other words, make the bonuses *only available* if they join
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, line 5124
  confirmations: 1
  anchor_at: "100m-money-models.md:5124"
- id: B-money-models-127
  type: rule
  name: >-
    Pricing For Continuity vs. Up Front Cash
  statement: >-
    The standalone one-time price is set as a multiple of the continuity price to hit the intended split: 1.33x for 50% choosing continuity, 1.66x for 60%, 2x for 70%, 2.33x for 80%, 2.66x for 90%.
  why: >-
    Tested repeatedly by the author: the smaller the standalone price relative to the continuity price, the more people buy the standalone, and the larger it is, the more choose continuity (2025 figures).
  anchor: >-
    To get 50% to choose continuity make the standalone offer 1.33x more.
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, line 5142
  confirmations: 2
  authors_caveat: >-
    The exact numbers matter less than the principle.
  anchor_at: "100m-money-models.md:5142"
- id: B-money-models-128
  type: rule
  name: >-
    If You Want More Up Front Cash
  statement: >-
    To take more cash up front, the bonus is also sold on its own as a single payment priced 1.33x to 2.66x the first month of the continuity-plus-bonus offer.
  why: >-
    People pay 33% more to avoid continuity, so even charging 33% more for the one-time purchase, half will buy it (2025 figures).
  anchor: >-
    *separate* offers. Make the bonus-only offer a single payment that's
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, line 5168
  confirmations: 2
  anchor_at: "100m-money-models.md:5168"
- id: B-money-models-129
  type: rule
  name: >-
    Offer Bulk Prepaid Discounts
  statement: >-
    Customers who join continuity are immediately offered a discounted bulk block of months, such as buy five months get one free.
  why: >-
    Only one out of every eight people has to take it to raise 30-day profits by 50%, which can make or break the Money Model; the laws of discounting apply, the larger the discount the more take it.
  anchor: >-
    "buy five months get one free." Only *one out of every eight people* has
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, line 5178
  confirmations: 2
  anchor_at: "100m-money-models.md:5178"
- id: B-money-models-130
  type: rule
  name: >-
    If You Want Commitments, Prepare To Make A Trade
  statement: >-
    A commitment of 3, 6 or 12+ months is bought with the bonus: the bonus is given only to customers who commit.
  why: >-
    You lose the people who would have signed up month-to-month just for the bonus, so it nets fewer sales but more committed customers; that is the trade.
  anchor: >-
    commitments, trade them for bonuses. For example, only allow customers
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Important Notes, line 5184
  confirmations: 1
  anchor_at: "100m-money-models.md:5184"
- id: B-money-models-131
  type: rule
  name: >-
    Bill weekly, not monthly
  statement: >-
    Recurring billing is set on weekly cycles (weekly, every 2, 4 or 12 weeks) rather than calendar months.
  why: >-
    A year has 12 months but 13 four-week cycles, an 8.3% difference; the same number of people buy at $100 every four weeks as at $100 a month, and at 20% margins annual profit rises 41% (2025 figures).
  anchor: >-
    hate money. Bill *weekly* (weekly, every 2 weeks, 4 weeks, 12 weeks
  source: >-
    100m-money-models.md, Continuity Discount Offers, Important Notes, line 5389
  confirmations: 1
  anchor_at: "100m-money-models.md:5389"
- id: B-money-models-132
  type: rule
  name: >-
    Don't Eat Into The Term With Discounts, Extend Them
  statement: >-
    Free months given for a commitment extend the term rather than being taken out of it, so twelve paid months plus three free is the starting shape.
  why: >-
    Starting from the extended term leaves room to Feature Downsell a shorter one later.
  anchor: >-
    prefer to start with extending the term. Then, I can Feature Downsell a
  source: >-
    100m-money-models.md, Continuity Discount Offers, Important Notes, line 5404
  confirmations: 1
  anchor_at: "100m-money-models.md:5404"
- id: B-money-models-133
  type: rule
  name: >-
    Get 3% More Revenue For Five Extra Words
  statement: >-
    The quoted price carries a stated 3% processing fee.
  why: >-
    The author has never had anyone not buy because of a processing fee, and 3% on the topline goes straight to the bottom line: a 10% profit business gains 30% of its profit.
  anchor: >-
    **Get 3% More Revenue For Five Extra Words.** "Yea, it\'s \$X *plus a 3%
  source: >-
    100m-money-models.md, Continuity Discount Offers, Important Notes, line 5407
  confirmations: 1
  anchor_at: "100m-money-models.md:5407"
- id: B-money-models-134
  type: rule
  name: >-
    Get Two Forms Of Payment
  statement: >-
    A second form of payment is collected from every recurring customer, traded for waiving the 3% processing fee.
  why: >-
    Recurring businesses lose mountains of cash to expired cards and insufficient funds; the fee waiver is justified because collecting new payment information costs man hours.
  anchor: >-
    with the same solution. I ask them if they want a 3% discount (a pretty
  source: >-
    100m-money-models.md, Continuity Discount Offers, Important Notes, line 5418
  confirmations: 1
  anchor_at: "100m-money-models.md:5418"
- id: B-money-models-135
  type: rule
  name: >-
    Get ACH If You Can
  statement: >-
    The second form of payment is ACH wherever it can be obtained.
  why: >-
    It links directly to the bank account and is the cheapest way to transact besides cash.
  anchor: >-
    **Get ACH If You Can.** If you get a second form of payment, try to get
  source: >-
    100m-money-models.md, Continuity Discount Offers, Important Notes, line 5426
  confirmations: 1
  anchor_at: "100m-money-models.md:5426"
- id: B-money-models-136
  type: rule
  name: >-
    Gift Cards
  statement: >-
    The discounted time is handed over as a physical gift card the customer can use after about the first three payments, or give to a friend.
  why: >-
    The gift becomes a lead magnet, and many people simply forget to use it, which leaves you a full-priced sign-up.
  anchor: >-
    can apply the discount whenever they want *after the first three
  source: >-
    100m-money-models.md, Continuity Discount Offers, Important Notes, line 5433
  confirmations: 2
  anchor_at: "100m-money-models.md:5433"
- id: B-money-models-137
  type: rule
  name: >-
    Try Lifetime Discount At Your Most Common Churn Point
  statement: >-
    A lifetime lower rate is advertised up front but earned only by staying past the month where the average customer drops off.
  why: >-
    It pulls customers through the point where they usually cancel; a rice company set 15% off at five straight months, just beyond where most people cancelled.
  anchor: >-
    lower rate *if* they stay past X period. Make X the month your average
  source: >-
    100m-money-models.md, Continuity Discount Offers, Important Notes, line 5441
  confirmations: 2
  anchor_at: "100m-money-models.md:5441"
- id: B-money-models-138
  type: rule
  name: >-
    High churn rules out the front-loaded discount
  statement: >-
    A business with historically high churn does not apply the continuity discount up front and uses one of the other three placements instead.
  why: >-
    The up front placement works where contracts are reliably enforced (cell phones, storage, real estate, collateral); it gets customers but delays cash, so it does not get customers profitably.
  anchor: >-
    collateral). Two notes: First, if you have historically high churn, then
  source: >-
    100m-money-models.md, Continuity Discount Offers, Important Notes, line 5342
  confirmations: 1
  anchor_at: "100m-money-models.md:5342"
- id: B-money-models-139
  type: rule
  name: >-
    Cancellation fee equals the discount they agreed to
  statement: >-
    The cancellation fee is set equal to the discount the customer received for committing, payable whenever they want to leave.
  why: >-
    It is simple to explain, and it just puts them back at the month-to-month rate.
  applies_when: >-
    Every customer enters the Continuity Offer on a discount of some kind.
  anchor: >-
    Just make the cancellation fee *equal to the discount they agreed to
  source: >-
    100m-money-models.md, Continuity Discount Offers, CANCELLATIONS, line 5462
  confirmations: 2
  anchor_at: "100m-money-models.md:5462"
- id: B-money-models-140
  type: rule
  name: >-
    Make Sure Customers Know How To Cancel
  statement: >-
    There is an obvious, stated way for a customer to cancel and to complain inside the business.
  why: >-
    With nowhere to complain inside the business they complain outside it; with no obvious way to cancel more people vanish and complain, and you lose the chance to save them.
  anchor: >-
    people will vanish *and* complain. By having a clear way for them to
  source: >-
    100m-money-models.md, Continuity Discount Offers, CANCELLATIONS, line 5469
  confirmations: 2
  anchor_at: "100m-money-models.md:5469"
- id: B-money-models-141
  type: rule
  name: >-
    If A Customer Wants To Cancel, Ask To Do An Exit Interview
  statement: >-
    Every cancelling customer is asked for an exit interview, incentivized by waiving the cancellation fee.
  why: >-
    It gives customers a real reason to give feedback; the author routinely saves a third of the customers who agree to an exit interview, and some can be rolled over into a higher level of service.
  anchor: >-
    waive your cancellation fee if you come in and tell me what I could do
  source: >-
    100m-money-models.md, Continuity Discount Offers, CANCELLATIONS, line 5486
  confirmations: 2
  anchor_at: "100m-money-models.md:5486"
- id: B-money-models-142
  type: rule
  name: >-
    Setup fee at 3-5x the monthly rate
  statement: >-
    The waived startup fee is set at 3-5x the monthly rate.
  why: >-
    The fee has to be big enough that buyers commit to avoid it, and big enough that quitting early costs about as much as staying (2025 figures).
  anchor: >-
    ● I typically make the fee 3--5x my monthly rate.
  source: >-
    100m-money-models.md, Waived Fee Offer, Summary Points, line 5695
  confirmations: 2
  anchor_at: "100m-money-models.md:5695"
- id: B-money-models-143
  type: rule
  name: >-
    Commitment of at least a year
  statement: >-
    A Waived Fee Offer asks for a commitment of at least twelve months.
  why: >-
    The longer the commitment the better it works, especially for services that take a long time to work such as SEO, investing and weight loss, because it keeps people committed when they get emotional.
  anchor: >-
    ● At minimum, the commitment length should be a year.
  source: >-
    100m-money-models.md, Waived Fee Offer, Summary Points, line 5697
  confirmations: 2
  anchor_at: "100m-money-models.md:5697"
- id: B-money-models-144
  type: rule
  name: >-
    Presenting The Fee
  statement: >-
    The startup fee is justified by the cost of getting a new customer started: short-term flexibility means the customer covers their own setup costs, a long commitment means the business covers them.
  why: >-
    It gives a reason the customer accepts without the fee looking like a penalty.
  anchor: >-
    **Presenting The Fee.** Justify the fee by explaining the costs of
  source: >-
    100m-money-models.md, Waived Fee Offer, Important Notes, line 5652
  confirmations: 1
  anchor_at: "100m-money-models.md:5652"
- id: B-money-models-145
  type: rule
  name: >-
    If More Than 5% Of People Want To Cancel Early, Look Into It
  statement: >-
    More than 5% of committed customers wanting to cancel early is a signal to investigate the product rather than tighten the terms.
  why: >-
    Pricing incentivizes sticking but cannot and should not overcome a terrible product; you want to nudge people, not handcuff them into paying for something they hate (2025 benchmark).
  anchor: >-
    **If More Than 5% Of People Want To Cancel Early, Look Into It.**
  source: >-
    100m-money-models.md, Waived Fee Offer, Important Notes, line 5660
  confirmations: 1
  anchor_at: "100m-money-models.md:5660"
- id: B-money-models-146
  type: rule
  name: >-
    If You Want More Up Front Cash, Have A Smaller Fee
  statement: >-
    When more up front cash is the goal, the fee is set at 1.5-3x the monthly rate instead of 3-5x.
  why: >-
    A smaller fee encourages people to go month-to-month and pay it, a larger fee encourages the commitment (2025 figures).
  anchor: >-
    the fee 1.5--3x the monthly rate. When you do this, more people will
  source: >-
    100m-money-models.md, Waived Fee Offer, Important Notes, line 5668
  confirmations: 2
  anchor_at: "100m-money-models.md:5668"
- id: B-money-models-147
  type: rule
  name: >-
    Drop The Fee After The Customer Fulfills The Commitment
  statement: >-
    Once a customer has served out the full commitment, the waived fee is cancelled and they can leave free of charge.
  why: >-
    They have earned their free cancellation; it does not stick forever, which makes the arrangement equitable.
  anchor: >-
    **Drop The Fee After The Customer Fulfills The Commitment.** If someone
  source: >-
    100m-money-models.md, Waived Fee Offer, Important Notes, line 5671
  confirmations: 2
  anchor_at: "100m-money-models.md:5671"
- id: B-money-models-148
  type: rule
  name: >-
    The $100M Money Model test
  statement: >-
    A Money Model qualifies as a $100M Money Model when one customer produces enough money to get and service at least two more customers in less than 30 days.
  why: >-
    At that point cash stops being the limiter on scaling the business.
  anchor: >-
    and service *at least* two more customers *in less than 30 days.*
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, Description, line 5826
  confirmations: 2
  anchor_at: "100m-money-models.md:5826"
- id: B-money-models-149
  type: rule
  name: >-
    The good Money Model minimum
  statement: >-
    The bare minimum for a Money Model is that one customer makes more profit in the first 30 days than it costs to get and service them.
  why: >-
    Below that the business loses money getting customers, which is what forces it to cut advertising and eventually fail.
  anchor: >-
    2\. **A good Money Model** *makes more profit from a customer than it
  source: >-
    100m-money-models.md, Ten Years In Ten Minutes, What We Covered, line 6166
  confirmations: 2
  anchor_at: "100m-money-models.md:6166"
- id: B-money-models-150
  type: rule
  name: >-
    Each stage pays for the next
  statement: >-
    A stage of the Money Model is only extended once it works reliably, financially and operationally, and pays for the stage after it.
  why: >-
    Starting a bootstrapped business with a finished Money Model makes it collapse on top of you; none of the author's businesses started with a fully forged one.
  anchor: >-
    for the next*. We keep improving each stage until it gets *reliable*.
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, Description, line 5857
  confirmations: 2
  anchor_at: "100m-money-models.md:5857"
- id: B-money-models-151
  type: rule
  name: >-
    Perfect One Offer At A Time
  statement: >-
    One offer is implemented at a time and repeated until it works reliably and then automatically, before the next stage is started.
  why: >-
    Implementing a whole Money Model at once breaks the business; when the Money Model starts working the business starts breaking anyway.
  anchor: >-
    Money Model at once. Don't. Stick to your stage. Pick one offer. Try it.
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, Important Notes, line 6014
  confirmations: 2
  anchor_at: "100m-money-models.md:6014"
- id: B-money-models-152
  type: rule
  name: >-
    Measure in quarters, not weeks
  statement: >-
    Progress on a Money Model is measured in quarters rather than weeks.
  why: >-
    You either build it right or you build it again, and building again, however fast, still takes longer than building it right the first time.
  anchor: >-
    to measure in quarters, not weeks. You either build it right or you
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, Important Notes, line 6019
  confirmations: 1
  anchor_at: "100m-money-models.md:6019"
- id: B-money-models-153
  type: rule
  name: >-
    Raise Price In Stages
  statement: >-
    New offers start cheap and the price is raised as yeses come in, until raising it further makes less money in total.
  why: >-
    Lots of early yeses generate the customer feedback that improves the product; the stopping point is where the nos are no longer made up for by the extra cash from the yeses.
  anchor: >-
    raising the price. And keep raising the price until you cannot make up
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, Important Notes, line 6026
  confirmations: 2
  anchor_at: "100m-money-models.md:6026"
- id: B-money-models-154
  type: rule
  name: >-
    Simple Scales. Fancy Fails.
  statement: >-
    New offers are made out of new ways to sell the existing product rather than out of new products or new businesses.
  why: >-
    It is less about having 100 products to offer and more about having 100 ways to offer your product; one personal training product becomes many offers by varying sessions per week.
  anchor: >-
    about having 100 ways to offer your product. Think more ways to sell the
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, Important Notes, line 6032
  confirmations: 2
  anchor_at: "100m-money-models.md:6032"
- id: B-money-models-155
  type: rule
  name: >-
    Affiliate Products Can Fill Money Model Gaps
  statement: >-
    A gap in the Money Model is filled by selling somebody else's product for a commission and letting them deliver it.
  why: >-
    It adds offers and money without the operational headache of delivery, at any size from no offer at all to a $100M business.
  anchor: >-
    somebody else's stuff. In short, you can always offer somebody else's
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, Important Notes, line 6044
  confirmations: 2
  anchor_at: "100m-money-models.md:6044"
- id: B-money-models-156
  type: rule
  name: >-
    Turn Attraction Offers Into Continuity Offers With Automatic Renewal
  statement: >-
    A bulk Attraction Offer rolls automatically into a month-to-month subscription when the purchased period ends.
  why: >-
    It makes the offer a two-for-one, getting the benefits of an Attraction Offer and a Continuity Offer from the same sale.
  anchor: >-
    Renewal.** This makes it a two-for-one. For example, if you do a Buy 6
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, Important Notes, line 6072
  confirmations: 2
  anchor_at: "100m-money-models.md:6072"
- id: B-money-models-157
  type: rule
  name: >-
    Make the upsell at the time of greatest need
  statement: >-
    The Upsell Offer is matched to the problem the Attraction Offer creates and made at the customer's time of greatest need.
  why: >-
    Once you solve a problem another appears, and those problems need solutions too.
  anchor: >-
    Upsell, Anchor Upsell, Rollover Upsell. Then, make your offer at their
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, Make Your Own Money Model, line 5985
  confirmations: 2
  anchor_at: "100m-money-models.md:5985"
- id: B-money-models-158
  type: rule
  name: >-
    Continuity at the right time beats continuity inside 30 days
  statement: >-
    If the right moment for the Continuity Offer falls after the first thirty days, it is made then rather than forced into the window.
  why: >-
    It is better to make the offer at the right time than to force it at the wrong time.
  anchor: >-
    first thirty days, and that's OK. *It's better to make the offer at the
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, Make Your Own Money Model, line 6004
  confirmations: 1
  anchor_at: "100m-money-models.md:6004"
- id: B-money-models-159
  type: rule
  name: >-
    The Upsell Offer target
  statement: >-
    The Upsell Offer is sized so that 30-day profit lands well above the cost of getting a new customer plus the cost of delivering to them.
  why: >-
    That is the goal of the second step of building a Money Model; the first offer does not always make the profit.
  anchor: >-
    *well above* our costs of getting a new customer and delivering what you
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, Make Your Own Money Model, line 5979
  confirmations: 2
  anchor_at: "100m-money-models.md:5979"
```
