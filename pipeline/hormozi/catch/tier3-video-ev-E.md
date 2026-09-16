# Улов фазы 1 — Enterprise Value: fragments of four video transcripts (ярус 3), тип E: глоссарий

Группа `tier3-video-ev`, слаг `video-ev`, ярус 3. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **27** (экстрактор вернул 27, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `video-business-that-runs-without-you.md`, lecture | символы 4000–39500 | 1 | — |
| `video-business-that-runs-without-you.md`, zoom-out | символы 40321–44137 | 1 | — |
| `video-business-that-runs-without-you.md`, EV answer | символы 44492–47170 | 1 | — |
| `video-make-money-so-fast.md`, wealth alchemy | символы 31313–44384 | 1 | — |
| `video-13-years-no-bs-business-advice.md`, point 16 | символы 71372–73000 | 1 | — |
| `video-no-bs-business-advice-2026.md`, overextension | символы 67605–72500 | 1 | — |
| `video-13-years-no-bs-business-advice.md` (итого по файлу) | | | 1 |
| `video-business-that-runs-without-you.md` (итого по файлу) | | | 13 |
| `video-make-money-so-fast.md` (итого по файлу) | | | 9 |
| `video-no-bs-business-advice-2026.md` (итого по файлу) | | | 4 |

## Как собран файл

Экстрактор E (Glossary) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier3-video-ev.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier3-video-ev-E.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: E-video-ev-001
  type: term
  name: >-
    Business (a business that requires you isn't a business)
  statement: >-
    In this method the word business is reserved for something that creates value without the owner being required; anything that stops producing when the owner steps away is a job the owner cannot quit.
  definition: >-
    A business that requires you isn't a business; in the technical sense anything that generates a profit with an LLC is a business, but what the vast majority of people who begin one wanted was freedom.
  why: >-
    Once something goes from valuable to you to valuable to anyone, it is something other people would want to buy, and that is what makes it inherently worth something.
  not_to_confuse_with: >-
    The legal or technical sense the author names himself — a profit-generating LLC, which qualifies as a business on paper while being valueless without the owner.
  anchor: >-
    A business that requires you isn't a business. And I'm going to say that the technical sense, anything that generates a profit with an LLC is a business.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@4100"
- id: E-video-ev-002
  type: term
  name: >-
    Frustrated Fred and wealthy William
  statement: >-
    Frustrated Fred and wealthy William are the author's names for two owners of identically sized businesses — Fred is required in his and grows only by his after-tax savings, William owns his the way one owns a stock and grows by the sale multiple on profit.
  definition: >-
    Frustrated Fred runs the business himself and keeps what is left after 50% taxes and living expenses; wealthy William has a team that runs it day-to-day, so he just owns it like he owns the paper stock of a company, and his business trades at six times profit.
  why: >-
    On the author's live math an extra $500,000 of profit gives Fred $250,000 after tax and gives William $3 million of net worth at a 6x multiple — regular income is taxed to oblivion and gets zero multiplication, which is why he calls the second one the game of wealth.
  anchor: >-
    so we had frustrated Fred and let's call it wealthy William
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    Named and worked out live on a whiteboard in one talk; the 6x multiple and the 50% tax rate are his illustration numbers, not benchmarks.
  anchor_at: "video-business-that-runs-without-you.md@7123"
- id: E-video-ev-003
  type: term
  name: >-
    Self-inventory
  statement: >-
    A self-inventory is the owner's written list of literally everything he does, made as granular as possible so each item can be turned into something someone else can do.
  definition: >-
    You actually list out everything you do, literally all of it, and then you turn each of those checklist items into something that someone else can do.
  why: >-
    The author calls it how you get out of the day-to-day without breaking the machine.
  applies_when: >-
    The first step of moving from the owner who is required in the business to the owner who owns it.
  anchor: >-
    So the first step of actually taking it from frustrated Fred to wealthy William is you do a self-inventory. So what that means is that you actually list out everything you do, literally all of it.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@9154"
- id: E-video-ev-004
  type: term
  name: >-
    Time study
  statement: >-
    A time study is a week of noting in one word, every 15 minutes on a timer, what you actually did, used when the owner cannot yet say what his own work consists of.
  definition: >-
    Real simple, no fancy technology: an Excel sheet with times down one side every 15 minutes, a timer, and one note of what you did at each mark.
  why: >-
    It produces the list a self-inventory needs, and the author says it will be the most productive week of your life because you are proving your productivity to yourself.
  applies_when: >-
    The step before the self-inventory when you do not even know what you do; it can also be run on a team member who is a key man risk.
  anchor: >-
    So time study, real simple. You don't need any like fancy technology for this. You just take an Excel sheet and you write times on one side every 15 minutes and you simply put in a timer.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@9705"
- id: E-video-ev-005
  type: term
  name: >-
    Project, process or person
  statement: >-
    Every line of the self-inventory is resolved by exactly one of three things — a project, a process or a person — which is what gets installed in that slot in the owner's place.
  definition: >-
    A project is a one-time thing which sometimes creates a process, or you have a person who does this thing on a continuous basis; the author notes you probably already have underutilised people on the team to slot in.
  anchor: >-
    So it's either a project, a process or a person that's going to installed in each of these little slots next to it.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 2
  anchor_at: "video-business-that-runs-without-you.md@10973"
- id: E-video-ev-006
  type: term
  name: >-
    Red, yellow, green
  statement: >-
    Red, yellow and green rate each item of the self-inventory by how hard it is to hand off — green is something you can teach someone on the team today, yellow needs a one-time project or process you know how to build, red is something you cannot do or a person you do not have yet.
  definition: >-
    Green is I can give this to somebody; yellow is a one-time project or process that I have to install but I know how to do it; red is where it's something that I either don't know how to do or there's a person that I know I need to have, but I don't have.
  why: >-
    The author solves them green to red because the greens you can get out quickly, the yellows take a little more time, and the reds wait until the first two are done.
  anchor: >-
    The red is where it's something that I either don't know how to do or there's a person that I know I need to have, but I don't have. And so I solve these in green to reds because the greens you can get out quickly.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@11806"
- id: E-video-ev-007
  type: term
  name: >-
    If this then that (decision trees)
  statement: >-
    Decision trees, which the author states as if this then that, are written rules of behaviour for the common scenarios a role meets, so the decision no longer has to come back to the owner.
  definition: >-
    Rules of behavior, decision trees for common scenarios: somebody comes in and says I would like to change my card, this is how you change the card; change my flavor, this is how you change the flavor.
  applies_when: >-
    The more duplicatable the job and the more people in a function, the more standardized the questions become and the better this works; the more complex the role, the more one-off the scenario.
  anchor: >-
    we want to start saying if this then that these are rules of behavior right they're decision trees for common scenarios
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@12401"
- id: E-video-ev-008
  type: term
  name: >-
    Shadow train
  statement: >-
    Shadow train is the first of the three handoff steps — they watch you do it — followed by supervising them doing it in front of you and then supporting their independence, available but not involved.
  definition: >-
    So you'll shadow train, this is where they watch you do it; the next is you supervise them doing it; after that you just support their independence and you're available but not involved.
  why: >-
    In the beginning the handoff needs more ad hoc calls and consults, and over time a competent employee automates those decisions back down to himself, which is when the full handoff occurs and they own it completely.
  anchor: >-
    So you'll shadow train. So this is where they watch you do it. The next is you supervise them doing it.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@22699"
- id: E-video-ev-009
  type: term
  name: >-
    Intelligence (rate of learning)
  statement: >-
    In this method intelligence means rate of learning, not accumulated skill, so employees are measured on how fast they improve rather than on how well they started.
  definition: >-
    Intelligence I measure as rate of learning.
  why: >-
    Of two hires, the flat one is passed by the fast-improving one in three to six months, so the author would rather have a more intelligent employee who learns faster than a more experienced employee who learns slower.
  not_to_confuse_with: >-
    Experience or inherent skill — the author separates the two himself and says it sometimes pays to take the less experienced candidate.
  anchor: >-
    And like so intelligence I measure as rate of learning.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    Said once, in passing, and the author adds that it depends on the role.
  anchor_at: "video-business-that-runs-without-you.md@24091"
- id: E-video-ev-010
  type: term
  name: >-
    The phone test
  statement: >-
    The phone test is the author's name for the check that a location or business can be left alone without your phone ringing.
  definition: >-
    If you can leave it alone, like your phone doesn't ring — I call it the phone test.
  applies_when: >-
    Offered above all to brick-and-mortar owners before opening a second or third location.
  anchor: >-
    like your your phone doesn't ring, and I'll tell you how to do that in a second, right? I call it the phone test.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    Named once in passing and never explained in this talk — he says I'll tell you later and does not return to it; the mechanic of handing the phone to an operator is described, without this name, in video-no-bs-business-advice-2026.md, overextension.
  anchor_at: "video-business-that-runs-without-you.md@25247"
- id: E-video-ev-011
  type: term
  name: >-
    Key man / key man risk
  statement: >-
    The key man is whoever the business cannot produce without, and in a founder-led company the owner becomes the key man as soon as his face is what gets the customers.
  definition: >-
    A key man risk is when this person is super valuable to the business and you have to have less dependency on this person; if your face gets the customers, you are the key man.
  why: >-
    It is why you cannot leave and why revenue drops when you do; it feels good in the short term because everyone relies on you, but to make an important business you need to become less important.
  anchor: >-
    but if your face gets the customers, you are the key man
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 2
  anchor_at: "video-business-that-runs-without-you.md@33579"
- id: E-video-ev-012
  type: term
  name: >-
    Life cycle ads
  statement: >-
    Life cycle ads are ads assembled from recordings the business already makes — the sales call, the onboarding call, the delivery checkpoints, the testimonial — compressed into one timeline of a single customer.
  definition: >-
    You probably already record your sales calls, your onboarding calls and delivery checkpoints, so when someone gives a testimonial you pull the recordings from their sales call to their onboarding to each of their touch points and compress that into a timeline that also becomes another advertisement.
  why: >-
    Instead of the customer saying I was here and now I'm here, it shows them actually being scared, not sure and hesitating before signing up, and then getting the outcome.
  applies_when: >-
    One of the seven processes for capturing marketing without direct-to-camera founder ads.
  anchor: >-
    the next one is something I call life cycle ads, which basically you probably already have functions in the business that already occur, which is you probably record your sales calls.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@34875"
- id: E-video-ev-013
  type: term
  name: >-
    Enterprise value
  statement: >-
    Enterprise value is what the business itself is worth to a buyer or investor, and in this method it is the most tax-efficient vehicle for building wealth because it grows untaxed until it is sold.
  definition: >-
    Enterprise value dictates how valuable something is; it is the most efficient tax vehicle for building wealth, and a high-value enterprise is an asset you can take loans against, get lines of credit on and raise capital against.
  why: >-
    Excess cash flow reaches the owner in a tax-inefficient manner, so once the business already covers the owner's needs, growth in net worth that isn't affected by taxes is what is left to play for.
  not_to_confuse_with: >-
    Cash flow, which the author answers directly here — the objection that enterprise value is fictional numbers that can't liquidate, against hard cash; his reply is that both matter but they are stages, and if you don't know where your rent's coming next month, cash flow comes first.
  applies_when: >-
    Once the owner's own and his family's needs are satisfied; the author says most of his content is for business owners trying to get bigger and scale.
  anchor: >-
    So, enterprise value is important for a variety of reasons. Enterprise value dictates how valuable something is.
  source: >-
    video-business-that-runs-without-you.md, EV answer
  confirmations: 3
  anchor_at: "video-business-that-runs-without-you.md@44743"
- id: E-video-ev-014
  type: term
  name: >-
    Permanent customer
  statement: >-
    A permanent customer is one who, once acquired, never leaves — in practice the author counts anyone who has been with you two plus years as permanent.
  definition: >-
    One out of three customers becomes a permanent customer, meaning once they get on our subscription they never leave; within the context of what we're talking about, somebody who's been with you two plus years is a permanent customer.
  why: >-
    The recurring base built from permanent customers is what the business is valued on, so every acquisition dollar should be measured against it rather than against a first sale.
  anchor: >-
    now let's say that we know one out of three customers becomes a permanent customer meaning once they get on our subscription they never leave
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 2
  anchor_at: "video-make-money-so-fast.md@32054"
- id: E-video-ev-015
  type: term
  name: >-
    Permanent CAC
  statement: >-
    Permanent CAC is the cost of acquiring one permanent customer — the ordinary cost per customer divided by the share of customers who stay permanently.
  definition: >-
    If a customer costs $300 and one out of three becomes permanent, the permanent CAC is somewhere close to $900; more generally, take how much it costs to get a customer and multiply it by the number of customers it takes to get one that stays.
  why: >-
    It is the number the enterprise value arbitrage is computed against, and knowing it lets you accept a higher CAC for an avatar that converts to permanent at a better rate — a $600 permanent CAC at one in three beats a cheaper customer at one in ten.
  not_to_confuse_with: >-
    Plain CAC, the cost of acquiring a customer who may churn; the author builds permanent CAC out of it in two multiplications.
  anchor: >-
    which would mean that our permanent CAC is somewhere close to $900
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 2
  authors_caveat: >-
    Calculated live on a whiteboard with round illustration numbers; one of the enterprise value figures in this passage is garbled in the transcript.
  anchor_at: "video-make-money-so-fast.md@32196"
- id: E-video-ev-016
  type: term
  name: >-
    Wealth alchemy
  statement: >-
    Wealth alchemy is the author's name for the arbitrage between what a permanent customer costs to acquire and what that customer's annual revenue is worth once multiplied by the enterprise value multiple — an increase in asset value that is not taxed until sale.
  definition: >-
    A massive arbitrage between the permanent cost of acquiring customers, the annual value, and the enterprise value multiple; those three things together create the discrepancy between what you put in and what you get out.
  why: >-
    You get the cash and the asset — it's not either or, it's an and — and the growth in enterprise value compounds tax-free as long as you keep building and do not cash out, which the author says is a bigger lever than any tax loophole.
  anchor: >-
    when I understood this I was like oh it's literally just a massive Arbitrage between the permanent cost of acquiring customers relative to the annual value relative to the Enterprise Value multiple
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 3
  authors_caveat: >-
    Presented as live whiteboard math in one video; the author frames it as how software companies that IPO get there, not as a guaranteed path.
  anchor_at: "video-make-money-so-fast.md@34499"
- id: E-video-ev-017
  type: term
  name: >-
    Leverage
  statement: >-
    Leverage in this method means getting more out than you put in, and it is the name for the whole gap between acquisition cost and enterprise value created.
  definition: >-
    The two symbols woven into the acquisition.com logo, supply and demand and a fulcrum for leverage, mean that you get more for what you put in.
  anchor: >-
    the reason that there are two symbols that are woven into the acquisition. comom logo which is supply and demand and a full Chrome for leverage is that you get more for what you put in
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 1
  authors_caveat: >-
    The transcript garbles acquisition.com as acquisition. comom and fulcrum as full Chrome; the definition is given in passing while pointing at his t-shirt.
  anchor_at: "video-make-money-so-fast.md@34923"
- id: E-video-ev-018
  type: term
  name: >-
    Opportunity vehicle
  statement: >-
    The opportunity vehicle is the kind of business you are in, which decides what a dollar of customer value is worth as enterprise value — the same customer economics multiply very differently in different vehicles.
  definition: >-
    In both situations you still spent the $900 per customer and you still make the $1,200 per year; the big difference was how much is that $1,200 per year worth — a software business traded at 10 times topline against a business traded at a 7x multiple on profit.
  why: >-
    Picking a good opportunity vehicle is what turns identical acquisition work into a far larger asset; the author's own numbers show the same spend producing a 2-point-something multiple in one vehicle and far more in the other.
  anchor: >-
    this is why picking a good opportunity vehicle because in both of these situations you still spent the $900 per customer you still make the $1,200 per year
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 1
  authors_caveat: >-
    The 10x topline multiple is given as fairly typical for a B2B SaaS business and only as long as you have good retention metrics; figures are from a 2023-2024 talk.
  anchor_at: "video-make-money-so-fast.md@35791"
- id: E-video-ev-019
  type: term
  name: >-
    The value equation, applied to an investor
  statement: >-
    An investor values a business on the same variables as the value equation — how likely the outcome is, how much effort and sacrifice it takes, and the time delay before it arrives.
  definition: >-
    An investor is valuing a business fundamentally on the same things: how likely is this to occur, how much effort and sacrifice is this going to take, what is the time delay between now and when this becomes this ultimate thing.
  why: >-
    A business of permanent customers is far less risky, so time works for it rather than against it, and that is what the investor is paying the multiple for.
  anchor: >-
    if you recall the value equation from earlier an investor is valuing a business fundamentally on the same things which is How likely is this to occur how much effort and sacrifice is this going to take what is the time delay between now and when this becomes this ultimate thing right
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 1
  authors_caveat: >-
    Said once, in passing, as a callback to the value equation defined earlier in the same talk; this listing names only three of its variables, and the author adds that the same process is done at a slightly more complex scale. The books define the value equation itself and win any divergence.
  anchor_at: "video-make-money-so-fast.md@37475"
- id: E-video-ev-020
  type: term
  name: >-
    Churn factory
  statement: >-
    A churn factory is a business that has to re-acquire its whole customer base every year because it keeps none of it, so growth depends entirely on selling more.
  definition: >-
    They sell something and people don't like it and they leave, which means the only way to grow this business is market and sell more, but that is only a one-way road — at some point you sell through all the customers within a given base.
  not_to_confuse_with: >-
    A business with the same customer count built from retained cohorts; the author's two companies both reach 300 customers, and he says which one you would rather own is no question.
  anchor: >-
    company a is just a churn Factory they sell something want and people don't like it and they leave which means the only way to grow this business is market and sell more
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 1
  anchor_at: "video-make-money-so-fast.md@37952"
- id: E-video-ev-021
  type: term
  name: >-
    Recurring vs reoccurring
  statement: >-
    Recurring means a subscription; reoccurring means the customer buys again on a regular basis without any subscription — both build a permanent base.
  definition: >-
    Recurring means it's a subscription like Netflix; reoccurring means that you buy on a regular basis, the way you buy Coca-Cola at a restaurant or at Costco without being subscribed.
  not_to_confuse_with: >-
    Each other — the author separates the two words explicitly, and Starbucks is his example of engineering reoccurring purchase rather than subscription.
  anchor: >-
    so the difference there really quickly is recurring means it's a subscription like netflex reoccurring means that you buy on a regular basis
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 1
  authors_caveat: >-
    Given as a quick aside inside the Starbucks example; the transcript spells Netflix as netflex.
  anchor_at: "video-make-money-so-fast.md@39696"
- id: E-video-ev-022
  type: term
  name: >-
    Customer financed acquisition
  statement: >-
    Customer financed acquisition is the author's name for getting paid to acquire customers — the customer's own payment funds the cost of acquiring him, so capital stops being the limiter on growth.
  definition: >-
    We're literally getting paid to get new customers; they pay us, they finance our acquisition, which is why I call it customer financed acquisition.
  why: >-
    It is the step that lets you get customers on demand and profitably, after pricing off value and before the wealth alchemy step of turning them into a permanent base.
  anchor: >-
    we're literally getting paid to get new customers they pay us they finance our acquisition which why I call it customer Finance acquisition
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 1
  authors_caveat: >-
    The transcript garbles the name as customer Finance acquisition; the books are the authority on the term.
  anchor_at: "video-make-money-so-fast.md@42091"
- id: E-video-ev-023
  type: term
  name: >-
    Three legs to the stool
  statement: >-
    The three legs of the stool are the three functional leaders every business needs — one for acquisition, one for delivery, one for internal operations — each with one throat to choke for that function.
  definition: >-
    One person in charge of getting customers, acquisition; a second in charge of delivery and getting those customers exactly what was promised; and a third to run the internal operations, the day-to-day legal, HR, payroll and CRM that support the other two.
  why: >-
    The three legs map onto the only three ways to increase enterprise value: get more customers, make them worth more, and decrease risk in the business.
  not_to_confuse_with: >-
    A leadership team of equals — the author says operations functions as a vendor to the other two heads and that person should never be making the big decisions in the business.
  anchor: >-
    number 16 there are three legs to the stool and so every business needs three big functional leaders you need one person who's in charge of getting customers acquisition
  source: >-
    video-13-years-no-bs-business-advice.md, point 16
  confirmations: 1
  anchor_at: "video-13-years-no-bs-business-advice.md@71372"
- id: E-video-ev-024
  type: term
  name: >-
    Prune the tree
  statement: >-
    To prune the tree is to cut the overextended parts, reconcentrate on what works, get it right, and only then scale back out again.
  definition: >-
    You have to cut your losses, you have to prune the tree, you have to reconcentrate, get it right and then scale back out again the right way.
  applies_when: >-
    One of the only two answers to overextension; the other is to hire incredibly impressive people, which means giving up your own income to bring them on.
  anchor: >-
    you have to prune the tree you have to reconcentrate get it right and then scale back out again the right way
  source: >-
    video-no-bs-business-advice-2026.md, overextension
  confirmations: 2
  anchor_at: "video-no-bs-business-advice-2026.md@69359"
- id: E-video-ev-025
  type: term
  name: >-
    A who problem
  statement: >-
    Overextension is a who problem: the constraint is not the number of locations or lines of business but the absence of good people left behind who can run what you already opened without you.
  definition: >-
    Overextension is typically a who problem, which is you don't have enough good people that you left behind who can actually run it without you.
  applies_when: >-
    The author says it happens at all ranges but a lot in the one to three million range, where the owner has pulled himself out of selling and delivery and assumes he is therefore not required.
  anchor: >-
    and so overextension is typically a who problem which is you don't have enough good people that you left behind who can actually run it without you
  source: >-
    video-no-bs-business-advice-2026.md, overextension
  confirmations: 1
  anchor_at: "video-no-bs-business-advice-2026.md@69469"
- id: E-video-ev-026
  type: term
  name: >-
    Owner is not CEO
  statement: >-
    Owner and CEO are two different roles that one person happens to hold: the owner holds the asset, the CEO operates it, and a business only runs without you once someone else is backfilled into the CEO half.
  definition: >-
    A lot of owners will mistakenly think that CEO and owner mean the same thing; you happen to be both, but they are not the same.
  why: >-
    If you work every hour of the day and you are not selling and not delivering, then the other stuff you are doing is very much operating the business — so when you leave, the business stops running as well because the CEO is gone.
  not_to_confuse_with: >-
    Each other — this is the confusion the author names outright.
  anchor: >-
    a lot of owners will mistakenly think that CEO and owner mean the same thing you happen to be both but they are not the same
  source: >-
    video-no-bs-business-advice-2026.md, overextension
  confirmations: 1
  anchor_at: "video-no-bs-business-advice-2026.md@70330"
- id: E-video-ev-027
  type: term
  name: >-
    The six-month test
  statement: >-
    The six-month test is passed when the business maintains or grows for six straight months without the owner's direct involvement.
  definition: >-
    The business has to either maintain or grow for six straight months without your direct involvement; at the very least do a one-month test, where you go away for a month and hand the phone to your operator against an override on the business.
  why: >-
    The author stresses without your direct involvement: an owner who keeps working in the day-to-day through the six months has not run the test at all, he has only delayed the next location by six months.
  applies_when: >-
    Before opening the next location or taking on the next thing, as the check on whether you are overextended.
  anchor: >-
    and the six-month test I was alluding to is the business has to either maintain or grow for six straight months without your direct involvement
  source: >-
    video-no-bs-business-advice-2026.md, overextension
  confirmations: 2
  anchor_at: "video-no-bs-business-advice-2026.md@71719"
```
