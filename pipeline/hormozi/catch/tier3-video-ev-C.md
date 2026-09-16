# Улов фазы 1 — Enterprise Value: fragments of four video transcripts (ярус 3), тип C: разборы (кейсы)

Группа `tier3-video-ev`, слаг `video-ev`, ярус 3. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **23** (экстрактор вернул 23, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `video-business-that-runs-without-you.md`, lecture | символы 4000–39500 | 1 | — |
| `video-business-that-runs-without-you.md`, zoom-out | символы 40321–44137 | 1 | — |
| `video-business-that-runs-without-you.md`, EV answer | символы 44492–47170 | 1 | — |
| `video-make-money-so-fast.md`, wealth alchemy | символы 31313–44384 | 1 | — |
| `video-13-years-no-bs-business-advice.md`, point 16 | символы 71372–73000 | 1 | — |
| `video-no-bs-business-advice-2026.md`, overextension | символы 67605–72500 | 1 | — |
| `video-business-that-runs-without-you.md` (итого по файлу) | | | 13 |
| `video-make-money-so-fast.md` (итого по файлу) | | | 8 |
| `video-no-bs-business-advice-2026.md` (итого по файлу) | | | 2 |

## Как собран файл

Экстрактор C (Application cases) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier3-video-ev.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier3-video-ev-C.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: C-video-ev-001
  type: case
  name: >-
    Frustrated Fred and Wealthy William
  statement: >-
    Two businesses are identical on paper, $10 million topline and $2 million bottom line, but Fred is required at work 80 hours a week while William's team runs his day to day; Fred pays 50% tax and living expenses and adds about $500,000 a year to his net worth, William's business trades at six times profit and is therefore worth $12 million, so the absentee owner is far richer on the same profit and loss.
  why: >-
    A business that runs without its owner is valuable to anyone rather than only to the owner, which makes it something other people will buy, and only what can be bought carries a multiple; income accumulates linearly and is taxed, ownership does not.
  demonstrates: >-
    A business that requires you is not a business; the same profit is worth a multiple once the owner is not required.
  anchor: >-
    And so of these two guys, this guy adds $500,000 to his net worth every year. This guy has a business that is worth $12 million. This guy's way richer.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    The author builds the figures live on a board and tells the listener to remove zeros if the scale is uncomfortable; the six times multiple is his illustration, not a stated benchmark.
  anchor_at: "video-business-that-runs-without-you.md@7563"
- id: C-video-ev-002
  type: case
  name: >-
    The extra $500,000, taxed once or multiplied
  statement: >-
    The same two owners each add $500,000 of annual profit: Fred nets about $250,000 after 50% tax, so his savings go from $500,000 to about $750,000 a year, while William's $500,000 is capitalised at his 6x multiple and adds $3 million, taking the business from $12 million to $15 million.
  why: >-
    Regular income is taxed to oblivion and nothing multiplies on it, you get one year divided by two; profit inside a sellable business is bought at a multiple, which is what the author calls the game of wealth.
  demonstrates: >-
    Marginal profit in a business that runs without you is worth the multiple, not the after-tax cash.
  anchor: >-
    And so he actually gets another $3 million added to his net worth. So his 12 million becomes 15 million. And this is the game of wealth.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    Calculating aloud, the author closes the example with a 20x difference between a company that can sell for 10x and one that cannot, after using 6x throughout the worked example.
  anchor_at: "video-business-that-runs-without-you.md@8486"
- id: C-video-ev-003
  type: case
  name: >-
    Prestige Labs support, written as if this then that
  statement: >-
    When the support manager at Prestige Labs said it was hard to onboard new people, the author listed the entire role as if-this-then-that pairs — change address, change card, change flavour, change billing cadence, cancel, refund — each with one documented answer, showing the job was a short set of standard scenarios rather than something to be taught case by case.
  why: >-
    The more duplicatable the job and the more people in a function, the more standardized the incoming questions become, so a role can be documented as decision trees for common scenarios instead of transferred by experience.
  demonstrates: >-
    Turning a documented list of what you do into decision trees, the rules of behaviour a replacement follows.
  anchor: >-
    Somebody will come in and say I would like to change my card. This is how you change your card.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    The author tells the story as he behaved at the time, less patient than now, and notes Leila told him off for being rude to a team member who was trying to win.
  anchor_at: "video-business-that-runs-without-you.md@13350"
- id: C-video-ev-004
  type: case
  name: >-
    The surprise dinners bill
  statement: >-
    The author let his team book surprise dinners for visiting clients at their own discretion; the monthly bill came to $250,000 of five-star dinners, and when the perk was cut, happiness scores and reviews did not change.
  why: >-
    Delegated spending needs a feedback loop: you still read the financials at the end of the month and check whether a delegated decision is generating true value; the author's point is that you will mess up, not that you should decide everything yourself.
  demonstrates: >-
    Giving a person a money cap they can decide under without supervision, and capping the total as well, so a mistake stays inside a known number.
  applies_when: >-
    Handing a team the authority to spend money on their own judgement.
  anchor: >-
    we were spending $250,000 a month in fivestar dinners
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@15034"
- id: C-video-ev-005
  type: case
  name: >-
    The camera operator's scorecard
  statement: >-
    Asked how his role makes the company money, the author's camera operator can only answer that he holds the camera, so the author works backwards from what bad camera work costs — the whole team's time wasted, media that performs worse because of framing or lighting, wasted footage, ill-fitted equipment, files not saved — and reverses each failure into a metric: what percentage of the time footage was saved correctly, named correctly in the system, put on the right drive, timestamped, lighting and camera set up right, and the shoot started on time.
  why: >-
    When people understand how what they do relates to how the company makes money, they see the impact of their own role, and the KPIs that unlock a decision tree are then tied to value rather than to activity.
  demonstrates: >-
    Building a role's scorecard and KPIs from the frame how do you and your role make the company money, by reversing the role's possible mistakes.
  anchor: >-
    I say, "All right, what does bad camera work do?" Well, bad camera work would be a waste of time, right, of the entire team.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    The author warns that if you ask the question of your team today, many will not be able to answer it, and that this will frighten you.
  anchor_at: "video-business-that-runs-without-you.md@17190"
- id: C-video-ev-006
  type: case
  name: >-
    Trading 200 hours of doing for 20 hours of managing
  statement: >-
    The author prices the swap: 200 hours a month of doing the work, roughly 50 hours a week, traded for 20 hours a month of managing, a tenfold gain in leverage, and then the same trade repeated one level up by hiring a manager, four hours for one.
  why: >-
    You can outwork anyone in your business but not everyone; leverage through labour means turning your effort into an organisation that produces without you.
  demonstrates: >-
    Step two of getting out of the business, moving from doing to managing and leading.
  anchor: >-
    let's say you swap 200 hours a month. So you know roughly 50 hours a week of work for doing 20 hours of managing
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    The author is doing the arithmetic aloud and restates the same trade as going from 50 to five, that is per week rather than per month.
  anchor_at: "video-business-that-runs-without-you.md@21379"
- id: C-video-ev-007
  type: case
  name: >-
    The HR hire who interviewed the author
  statement: >-
    The first genuinely good HR professional the author hired interviewed him with metrics he could not answer — the cost of acquiring talent, time to fill, and two-way fit, the percentage of hires where both the employee and the manager call it a 10 out of 10 at 90 days — and that catalogue of metrics was how he knew she had the skill, after which he learned the measures from her.
  why: >-
    The author measures skill in any endeavour by the quality and the quantity of the metrics a person tracks; at leadership level and above, a candidate who teaches you nothing means you will have to teach them, so the interview was a waste of time.
  demonstrates: >-
    Reading a candidate's level from the metrics they bring to the interview, and hiring people who are out of your league so they teach you the function.
  applies_when: >-
    Interviewing for a leadership role or above.
  anchor: >-
    She was like so what's your cost of acquiring talent? And I was like I don't know. That's a good question.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    The author notes that when you are starting out you usually cannot afford such people, or they do not want to work for you, or both.
  anchor_at: "video-business-that-runs-without-you.md@26927"
- id: C-video-ev-008
  type: case
  name: >-
    600 developers for one CTO
  statement: >-
    To find Daniel, the co-founder and CTO of Skool (the transcript renders it as school), Sam interviewed 600 developers, each a 30 to 60 minute conversation spread over about a year; the author uses the number to show what volume buys — by the tenth person claiming to be a sales manager you can already compare, and by the fiftieth you know who has game.
  why: >-
    Interview volume tunes your picker: pattern recognition across many candidates in the same role is what lets each next business be built faster, and it is otherwise bought by hiring five bad sales managers and losing six months to a year on each.
  demonstrates: >-
    Interviewing many more people than feels reasonable, and stacking or grouping interviews to afford it.
  anchor: >-
    for school, Sam interviewed 600 developers. developers to find our co-founder Daniel the CTO.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    The author calls the process brutal and acknowledges the cost of it to a business owner; he suggests group interviews for frontline to manager roles, but admits they are tough at director and executive level.
  anchor_at: "video-business-that-runs-without-you.md@29350"
- id: C-video-ev-009
  type: case
  name: >-
    Life cycle ads
  statement: >-
    When a customer says something good about you, pull the recordings that normal operations already produced — their sales call, their onboarding call, each delivery checkpoint — out of the CRM and the scheduling system and compress them into a timeline that shows the same person hesitant and unsure before signing up and then getting the outcome, instead of a stated before and after.
  why: >-
    The material already exists inside the business, so the advertisement costs nothing new to produce, and showing the customer's doubt before the result is more persuasive than a claim that I was here and now I am here.
  demonstrates: >-
    One of the seven processes that make marketing arrive without a direct to camera founder ad.
  anchor: >-
    We're going to look back through our CRM, look back through our scheduling and pull the recordings from their sales call to their onboarding to each of their touch points.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@35465"
- id: C-video-ev-010
  type: case
  name: >-
    Five dollars a testimonial in support chat
  statement: >-
    Pay a customer support person five dollars for every mini testimonial they capture in chat format after resolving a ticket, and screenshot it; the author says he has done this.
  why: >-
    Support already produces the moment where a customer says the product is great, so a small bounty turns an existing conversation into marketing material that arrives without the founder.
  demonstrates: >-
    Installing a repeatable process that collects marketing on your behalf, one of the seven the author lists.
  anchor: >-
    you can pay a customer support person five bucks for every person that they get like a mini testimonial in chat format from
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    Given once, in a quick list of examples, with no figure for how many testimonials a bounty produces.
  anchor_at: "video-business-that-runs-without-you.md@36711"
- id: C-video-ev-011
  type: case
  name: >-
    One-star reviews as ads
  statement: >-
    Most businesses already hold hundreds of Google, Yelp, Trustpilot or Amazon reviews that never become marketing; the author takes the funniest one-star reviews and, after Liquid Death's marketing, runs them as an ad saying that if you are one of these people you will not like our stuff.
  why: >-
    Clearly casting out the wrong type of person pulls in the right type, and the ad is funny as well.
  demonstrates: >-
    Turning existing review inventory into marketing that does not need the founder's face; repelling the wrong customer to attract the right one.
  anchor: >-
    and just say like, "Hey, if you're one of these people, you won't like our stuff."
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    Attributed by the author to Liquid Death's marketing, and said once in passing at the end of the list.
  anchor_at: "video-business-that-runs-without-you.md@37767"
- id: C-video-ev-012
  type: case
  name: >-
    Jony Ive worked for Steve Jobs
  statement: >-
    Jony Ive (the transcript says John Ivy), one of the best designers in the world and the man you would want to design your product, was an employee — and would only work for somebody as good as Steve Jobs; the same is why the smartest people in the world are willing to work for Elon Musk, and why those companies can be that size.
  why: >-
    No large business can have one person involved in everything, so decision making has to be decentralised to very capable people; the reason yours is not as big, not as valuable and does not run without you is that such people do not yet want to work for you.
  demonstrates: >-
    The real constraint behind every tactic in the talk is the level of talent you can attract, which rests on your track record and your ability to sell the future.
  anchor: >-
    The problem is that John Ivy only wants to work for somebody as good as Steve Jobs, right?
  source: >-
    video-business-that-runs-without-you.md, zoom-out
  confirmations: 1
  authors_caveat: >-
    The author allows a substitute for track record: someone who can sell the future well enough can outsell a thin record, and generic proof of ambition can stand in early on.
  anchor_at: "video-business-that-runs-without-you.md@41050"
- id: C-video-ev-013
  type: case
  name: >-
    Answering I like cash flow, hard cash
  statement: >-
    A commenter objects that enterprise value is fictional numbers that cannot be liquidated and that he prefers hard cash flow; the author answers by walking the cash down the owner's own ladder — rent, the house paid off, the parents' house, their cars and your cars, the kids' schools, upgrading the cars, a $100,000 vacation — and then asking what the surplus is for, since by the time a business has enterprise value it already throws off more cash than the owner needs, and that surplus reaches him taxed, while enterprise value grows untaxed and can still be borrowed against, used for lines of credit and raised on.
  why: >-
    Excess cash flow is transferred to the owner in a tax inefficient manner, so once needs are met the most efficient vehicle for building wealth is the enterprise value itself, which is also an asset you can finance against.
  demonstrates: >-
    Enterprise value and cash flow are not alternatives but levels of the same game; the objection comes from the position of not yet having enough.
  anchor: >-
    Once a business actually has enterprise value, it usually has already generated or had the ability to generate more than sufficient cash flow for the owner.
  source: >-
    video-business-that-runs-without-you.md, EV answer
  confirmations: 1
  authors_caveat: >-
    The author caps it himself: if you do not know where next month's rent is coming from, enterprise value is not your game yet; and he says the business game is not the only game in life worth winning.
  anchor_at: "video-business-that-runs-without-you.md@45148"
- id: C-video-ev-014
  type: case
  name: >-
    From free trial to permanent CAC
  statement: >-
    A free trial that costs $100 to start and converts one in three makes a customer cost $300; if one in three customers then stays permanently, the permanent CAC is about $900, and at a $100 a month price that customer is $1,200 of annual recurring revenue — $900 spent to buy $1,200 a year.
  why: >-
    The author frames it as a stock: if you could buy one for $900 and it sent you $1,200 inside twelve months, and kept doing it, you would call it an unbelievable investment.
  demonstrates: >-
    The permanent customer concept and the chain trial cost, conversion rate, permanent rate that produces permanent CAC.
  anchor: >-
    now let's say that we know one out of three customers becomes a permanent customer meaning once they get on our subscription they never leave
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 2
  authors_caveat: >-
    The numbers are chosen for simple math on a board; the author says retention metrics are what make the multiple stand up, so the chain only holds where the permanent rate is real.
  anchor_at: "video-make-money-so-fast.md@32054"
- id: C-video-ev-015
  type: case
  name: >-
    Wealth alchemy, $9 million in and $120 million out
  statement: >-
    At a 10x topline multiple, which the author calls fairly typical for a B2B SaaS business with good retention, that $1,200 a year customer carries about $12,000 of enterprise value (the transcript garbles the figure as $122,000 and $112,000); so 10,000 permanent customers at $900 each cost $9 million and produce $12 million of annual revenue plus roughly $120 million of enterprise value on which no tax is paid.
  why: >-
    It is an arbitrage between the permanent cost of acquiring a customer, the annual value of that customer and the enterprise value multiple, and the gap between what you put in and what you get out is the definition of leverage.
  demonstrates: >-
    Wealth alchemy, and why software companies can go from nothing to billions in a few years.
  anchor: >-
    walk through this in sequence with me you spend 9 million you get back $12 million in annual revenue
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 1
  authors_caveat: >-
    The author is calculating live and misstates the per-customer enterprise value; the 10x topline multiple is given as typical for B2B SaaS with good retention at the time of the video, not as a universal figure.
  anchor_at: "video-make-money-so-fast.md@34024"
- id: C-video-ev-016
  type: case
  name: >-
    The same customers in a different vehicle
  statement: >-
    Run the identical economics, $900 permanent CAC and $1,200 a year, in a business valued on the bottom line instead: $12 million of revenue at $3 million of profit on a 7x EBITDA multiple (the transcript writes EBITDA as eida) is $21 million of enterprise value against $120 million in the topline-valued case.
  why: >-
    In both situations you spent the same $900 per customer and make the same $1,200 a year, so the entire difference is what a year of that revenue is worth in that vehicle — which is why the choice of opportunity vehicle matters more than the acquisition work.
  demonstrates: >-
    Picking a good opportunity vehicle; the multiple, not the customer math, decides the size of the outcome.
  anchor: >-
    in both of these situations you still spent the $900 per customer you still make the $1,200 per year but the big difference was how much is that $1,200 per year worth
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 1
  authors_caveat: >-
    The author does not condemn the weaker vehicle: $9 million turned into $21 million is still a 2 point something multiple and he would take it.
  anchor_at: "video-make-money-so-fast.md@35846"
- id: C-video-ev-017
  type: case
  name: >-
    Business A and business B, both at 300 customers
  statement: >-
    Business A sells 100 customers in year one and loses them all, doubles marketing and sales to 200 in year two and loses those, then adds half again for 300 in year three; business B sells 100 a year with no increase in marketing at all and keeps them, so year three is 100 plus 100 plus 100. Both have 300 customers, and the author says there is no question which one you would rather own.
  why: >-
    You want time on your side rather than against you, because time passes either way; B keeps growing at constant sales effort and is far less risky, and an investor values a business on the same terms as the value equation, likelihood, effort and sacrifice, and time delay.
  demonstrates: >-
    The permanent customer versus the churn factory, where the only way to grow is a one-way road of selling more until the base is exhausted.
  anchor: >-
    both of these businesses A and B have 300 customers but which company would you rather own
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 1
  anchor_at: "video-make-money-so-fast.md@37004"
- id: C-video-ev-018
  type: case
  name: >-
    Starbucks against the coffee shop down the street
  statement: >-
    The author puts Starbucks' lifetime value per customer at about $14,000 (he first says $114,000 in the transcript), while the cost of getting somebody to buy a cup of coffee is much the same for Starbucks, a Dunkin' Donuts or a random coffee shop on the street; the difference is that Starbucks engineered a model people keep coming back to, making them reoccurring customers — reoccurring meaning a regular repurchase, as against recurring, which is a subscription like Netflix.
  why: >-
    When the cost of acquisition is roughly equal across competitors, everything that separates them is how much a customer is worth afterwards, which is decided by retention and repurchase rather than by cheaper advertising.
  demonstrates: >-
    Where LTV actually comes from, and the distinction between recurring and reoccurring customers.
  anchor: >-
    the cost to get a customer for Starbucks to get somebody buy coffee is probably similar to a Dunkin Donut
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 1
  authors_caveat: >-
    The LTV figure is quoted from memory in a talk and comes out garbled in the transcript before he repeats it.
  anchor_at: "video-make-money-so-fast.md@39362"
- id: C-video-ev-019
  type: case
  name: >-
    Permanent CAC for a high-churn agency
  statement: >-
    In a business with no subscription, such as an agency, count anyone who has stayed two or more years as a permanent customer; if only one in ten customers reaches that, multiply the cost of acquiring a customer by ten to get what a permanent customer really costs, because that permanent base is what the business is being built and valued on while the other nine are chaff.
  why: >-
    The recurring base is what carries the enterprise value multiple, so the price worth knowing is the price of a member of that base, not the price of a sale.
  demonstrates: >-
    Calculating permanent CAC where the business has churn and no subscription.
  applies_when: >-
    A high-churn business where some customers have nonetheless stayed a long time.
  anchor: >-
    it's only one out of every 10 of your customers becomes a permanent customer well then you say okay well how much does it cost to get a customer multiply it by 10
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 1
  authors_caveat: >-
    The two plus years threshold is the author's working definition within this talk.
  anchor_at: "video-make-money-so-fast.md@40682"
- id: C-video-ev-020
  type: case
  name: >-
    Advertising only to the avatar that stays
  statement: >-
    Look at how the one in ten who become permanent look, smell, walk and talk differently from the other nine, and change the advertising to attract only them: even if the cost of acquiring that avatar doubles, a one in three permanent rate makes the permanent customer cost $600 instead of $1,000, and you are still winning overall.
  why: >-
    A higher hit rate on permanence beats a lower price per customer, because the permanent customer is the unit the enterprise value is built from.
  demonstrates: >-
    Lowering permanent CAC by changing who you attract rather than what you pay per lead.
  anchor: >-
    even if our CAC for this specific Avatar doubles but we get it to one out of three it cost us $600 to get a customer rather than $1,000
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 1
  anchor_at: "video-make-money-so-fast.md@41433"
- id: C-video-ev-021
  type: case
  name: >-
    $1.5 million of tax on $123 million of gain
  statement: >-
    A business making $3 million of profit in a high tax state leaves the owner $1.5 million after 50% tax; but if that year the owner spent the money to add $12 million of revenue and roughly $120 million of enterprise value, the gain is about $123 million against $1.5 million paid, an effective rate of around one and a half per cent.
  why: >-
    Growth in enterprise value is untaxed and compounds as long as you keep building and do not cash out, so the biggest and most obvious tax play is simply to build something valuable, not to hunt loopholes.
  demonstrates: >-
    Why the author treats enterprise value as the most efficient tax vehicle for building wealth.
  anchor: >-
    so you have three million bucks in profit in this business and let's say that you live in a high tax state and you get tax 50% for tax reasons so you're going to take home $1.5 million after taxes
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 2
  authors_caveat: >-
    The author says this shifted how he played the game after being obsessed with tax strategy, and that the clue was the Forbes list being full of Californians despite the highest state taxes; the transcript garbles the combined total.
  anchor_at: "video-make-money-so-fast.md@43066"
- id: C-video-ev-022
  type: case
  name: >-
    Overextension, the second and third location
  statement: >-
    The second location opens while the first is not really running as well as the owner thinks: the moment he moves over, revenue at the first drops, and that drop was the profit, while the fixed costs stay; the new location is new so it underperforms, the star operator is at the first one and the owner is split between the two, so he earns what one location earned with twice the risk. Opening a third to fix it takes profit down further and leaves three locations, three times the risk and no money.
  why: >-
    Overextension is a who problem, there are not enough good people left behind who can run the place without you; the two ways out are to hire someone genuinely impressive, paid for out of your own income, or to prune the tree, reconcentrate, get it right and scale back out again.
  demonstrates: >-
    What a business that still requires its owner costs when it is expanded; the reason overexpansion is a leading cause of businesses going under.
  anchor: >-
    you open that second location when the first location isn't really operating as much as well as you think it is and as soon as you go there the revenue from the first one drops
  source: >-
    video-no-bs-business-advice-2026.md, overextension
  confirmations: 2
  authors_caveat: >-
    The author says it happens at all sizes but a lot in the one to three million range, where the owner has sucked himself out of selling and delivery and therefore believes he is no longer required — confusing being the owner with being the CEO.
  anchor_at: "video-no-bs-business-advice-2026.md@68255"
- id: C-video-ev-023
  type: case
  name: >-
    The phone test
  statement: >-
    Hand your phone to your operator before you go away and make the trade explicit — an override on the business, a profit share or stock, in exchange for the phone not ringing — then role-play the exceptions with them: a pipe bursts, calling you is the wrong answer because all you would do is call a plumber, so call the plumber; if it is an emergency call 911; either way, do not call me. The author wants a month at the very least and prefers a six-month test in which the business maintains or grows without the owner's direct involvement.
  why: >-
    Someone has to operate behind you, because the business stops running well when the CEO leaves and the owner is usually still the CEO; the handoff is only real when the decisions move with it rather than routing back through your phone.
  demonstrates: >-
    Backfilling yourself as CEO and testing it; the litmus test that the business must still be there, and ideally bigger, when you come back.
  applies_when: >-
    Before taking time off, and before opening the next location.
  anchor: >-
    I'm going to call a plumber so what are you going to do just call the plumber directly you don't need to call me to call the plumber
  source: >-
    video-no-bs-business-advice-2026.md, overextension
  confirmations: 2
  authors_caveat: >-
    The author warns that people run the six-month test while carrying on in the day to day and change nothing, so the business simply keeps operating with them as CEO and the test proves nothing; the name phone test is promised in the other talk and never explained there.
  anchor_at: "video-no-bs-business-advice-2026.md@71294"
```
