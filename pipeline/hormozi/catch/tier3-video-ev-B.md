# Улов фазы 1 — Enterprise Value: fragments of four video transcripts (ярус 3), тип B: правила и критерии

Группа `tier3-video-ev`, слаг `video-ev`, ярус 3. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **38** (экстрактор вернул 38, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `video-business-that-runs-without-you.md`, lecture | символы 4000–39500 | 1 | — |
| `video-business-that-runs-without-you.md`, zoom-out | символы 40321–44137 | 1 | — |
| `video-business-that-runs-without-you.md`, EV answer | символы 44492–47170 | 1 | — |
| `video-make-money-so-fast.md`, wealth alchemy | символы 31313–44384 | 1 | — |
| `video-13-years-no-bs-business-advice.md`, point 16 | символы 71372–73000 | 1 | — |
| `video-no-bs-business-advice-2026.md`, overextension | символы 67605–72500 | 1 | — |
| `video-13-years-no-bs-business-advice.md` (итого по файлу) | | | 2 |
| `video-business-that-runs-without-you.md` (итого по файлу) | | | 27 |
| `video-make-money-so-fast.md` (итого по файлу) | | | 4 |
| `video-no-bs-business-advice-2026.md` (итого по файлу) | | | 5 |

## Как собран файл

Экстрактор B (Rules and criteria) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier3-video-ev.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier3-video-ev-B.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: B-video-ev-001
  type: rule
  name: >-
    Self-inventory
  statement: >-
    Before delegating anything, the owner writes out a list of everything they personally do, at the most granular level, so that each item can be handed to someone else.
  why: >-
    A granular list is what lets the owner get out of the day-to-day without breaking the machine; without it there is nothing concrete to hand over.
  applies_when: >-
    First step of taking a business from owner-dependent to owner-independent.
  anchor: >-
    So what that means is that you actually list out everything you do, literally all of it.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@9262"
- id: B-video-ev-002
  type: rule
  name: >-
    Time study
  statement: >-
    An owner who cannot list what they do runs a time study first: a spreadsheet with a row every 15 minutes and a timer, noting in one word what was done in each slot.
  why: >-
    It produces the raw list the inventory needs, and the week itself turns out to be the most productive one because the owner is proving their productivity to themselves.
  applies_when: >-
    You do not know what you actually do all day; it also works on a team member who is a key man risk.
  anchor: >-
    You just take an Excel sheet and you write times on one side every 15 minutes and you simply put in a timer.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@9784"
- id: B-video-ev-003
  type: rule
  name: >-
    Project, process or person
  statement: >-
    Every item on the inventory is assigned one of three things next to it: a project, a process, or a person.
  why: >-
    A project is a one-time thing that sometimes creates a process, a person does the thing on a continuous basis; some slots can be filled with team members who are already underutilised.
  anchor: >-
    So it's either a project, a process or a person that's going to installed in each of these little slots next to it.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@10973"
- id: B-video-ev-004
  type: rule
  name: >-
    Green to reds
  statement: >-
    The items are worked in order green first, then yellow, then red: what can be handed to an existing person now, then what needs a one-time project or process you know how to build, then what needs a skill or a person you do not yet have.
  why: >-
    The greens get the owner out quickly, the yellows take a little more time, and only once greens and yellows are done is it worth moving on to the reds.
  anchor: >-
    And so I solve these in green to reds because the greens you can get out quickly.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@11939"
- id: B-video-ev-005
  type: rule
  name: >-
    If this then that
  statement: >-
    Alongside the list of tasks, the recurring decisions of the role are documented as if-this-then-that rules of behaviour, one branch per common scenario.
  why: >-
    The more duplicatable the job and the more people in the function, the more standardised the questions become, so common scenarios can be written down instead of being decided by the owner each time.
  applies_when: >-
    Roles where the same requests recur; the more complex and one-off the role, the less this holds.
  anchor: >-
    we want to start saying if this then that these are rules of behavior right they're decision trees for common scenarios
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@12401"
- id: B-video-ev-006
  type: rule
  name: >-
    Money box around a decision
  statement: >-
    A delegated decision comes with a stated money limit per decision and a cap on the total, below which the person acts without the owner's supervision.
  why: >-
    It gives the person a fixed number of shots to fix something on their own, while the monthly financials remain the feedback loop that catches anything out of whack.
  applies_when: >-
    The size of the limit depends on the size of the company.
  anchor: >-
    So it's like you can make decisions under $500 in total up to 5,000, right?
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 2
  authors_caveat: >-
    The author expects the loop to be abused at first and tells his own $250,000-a-month surprise-dinners mistake as the correction case; the check is whether the unlocked decision actually generates value.
  anchor_at: "video-business-that-runs-without-you.md@15645"
- id: B-video-ev-007
  type: rule
  name: >-
    How do you and your role make the company money
  statement: >-
    Every person in the business can state how their own role, not their department's function, makes the company money.
  why: >-
    Ask the team today and many will not be able to answer; once a person sees how what they do relates to the company making money, their role gains the impact they say they want.
  applies_when: >-
    Used on the team and on candidates in interviews, including ancillary roles such as finance, tech or media where the link is not obvious.
  anchor: >-
    You can say, how do you and your role make the company money?
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 2
  anchor_at: "video-business-that-runs-without-you.md@16134"
- id: B-video-ev-008
  type: rule
  name: >-
    Scorecard from reversed mistakes
  statement: >-
    A role's KPIs are built by listing what bad work in that role would cost the business and reversing each potential mistake into a percentage-of-the-time standard.
  why: >-
    Naming the costs of bad work (wasted team time, worse-performing media, lost footage, ill-fitted equipment) yields measurable standards such as saved correctly, named correctly, on the right drive, timestamped, lit and set up, on time.
  applies_when: >-
    Before a person can be tested and graduated on a role.
  anchor: >-
    And so, you can reverse each of these kind of potential mistakes into these are the things that we have to make.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@17762"
- id: B-video-ev-009
  type: rule
  name: >-
    The 80% test
  statement: >-
    A person is graduated onto a role only by passing a test showing that at 80% of the owner's skill they still produce 100% of the result.
  why: >-
    Nobody does it as well as you with one tenth of the reps, but someone who learns only the right way without your bad mistakes can start at half your level; if you can do it right with part of your time, someone else can do it better with all of theirs.
  anchor: >-
    The next thing is we have to have some sort of test to graduate the person which is can someone 80% as you get 100% of the result.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    At the start the author accepts 80% and sometimes 60% as good, as long as there is a clear path to the person getting better.
  anchor_at: "video-business-that-runs-without-you.md@18926"
- id: B-video-ev-010
  type: rule
  name: >-
    Trade doing for managing and leading
  statement: >-
    The owner's hours go to recruiting A players and to strategy and prioritisation, not to doing A-player work or to the tactics of what to do today.
  why: >-
    Swapping roughly 200 hours a month of doing for 20 hours of managing is a tenfold gain in leverage, and it repeats when a manager is hired to replace those hours; you can outwork anyone in your business but you cannot outwork everyone.
  anchor: >-
    We focus on recruiting a players not doing a player work.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@24578"
- id: B-video-ev-011
  type: rule
  name: >-
    Available but not involved
  statement: >-
    A handoff counts as complete only when the owner is available but not involved and the person owns the task completely, with the early ad hoc consults having tapered off.
  why: >-
    Handoff runs as they watch you do it, then you supervise them doing it, then you support their independence; with a competent employee the decisions get automated back down to them over time.
  anchor: >-
    and then after that you kind of just support their independence and you're available but not involved
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@22892"
- id: B-video-ev-012
  type: rule
  name: >-
    Measure how fast they improve
  statement: >-
    Employees are judged on their rate of improvement rather than on how well they started.
  why: >-
    A slower starter who improves steeply passes a flat stronger starter within three to six months, and intelligence here is measured as rate of learning, so the more intelligent hire beats the more experienced one who learns slower.
  anchor: >-
    I used to measure employees by how well they started. I measure employees today on how fast they improve.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    The author notes it depends on the role and presents it as a shift in his own thinking about talent.
  anchor_at: "video-business-that-runs-without-you.md@23525"
- id: B-video-ev-013
  type: rule
  name: >-
    The baseline litmus test
  statement: >-
    The baseline test of the business is that it does not burn down while the owner is away for a month; the next bar is that it is in a better position when the owner returns.
  why: >-
    A business that is better after a month away is what people want to buy, because it functions as a faster-growing annuity for an investor, which is what earns the big multiple.
  anchor: >-
    where you can leave for a month and when you come back it's in a better position than it was when you left
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@22282"
- id: B-video-ev-014
  type: rule
  name: >-
    Three months off
  statement: >-
    The ultimate test of the owner's replacement is taking three months off and having the business grow over that period.
  why: >-
    If it is merely flat while you are gone, the magic is still in you, and as soon as your attention moves the business goes down; the vast majority of businesses can grow year over year unless the market is capped.
  applies_when: >-
    Named by the author as the simplest litmus test before a brick-and-mortar owner opens a second or third location.
  anchor: >-
    ultimate test for you is can you take three months off and have the business grow
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 2
  anchor_at: "video-business-that-runs-without-you.md@24845"
- id: B-video-ev-015
  type: rule
  name: >-
    No second location before the first passes
  statement: >-
    A second location is not opened until the first one has been left alone and is bigger months later.
  why: >-
    Overexpansion is one of the number one reasons people go out of business: when the owner's attention splits, the first location drops, and the result is double the liability, debt and overhead with talent spread thinner, more risk and less profit.
  anchor: >-
    a lot of people shouldn't have second locations for much longer than they think
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 2
  anchor_at: "video-business-that-runs-without-you.md@26157"
- id: B-video-ev-016
  type: rule
  name: >-
    Skill measured by the metrics they track
  statement: >-
    A candidate's skill in a function is judged by the quality and quantity of the metrics they track and by how much detail they use to describe their role in metrics.
  why: >-
    The author's first genuinely good HR hire interviewed him with cost of acquiring talent, time to fill and 90-day two-way fit, metrics he did not know existed; absence of lawsuits or a low refund rate is not evidence of a good function.
  anchor: >-
    So I can measure someone's skill in any endeavor based on the quality and the quantitative metrics they track.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 2
  anchor_at: "video-business-that-runs-without-you.md@26540"
- id: B-video-ev-017
  type: rule
  name: >-
    Interview more people than you think you should
  statement: >-
    For each role, interview far more candidates than seems reasonable, stacking them as densely as possible.
  why: >-
    Volume tunes your picker: by the fiftieth conversation you already know who has game, and that pattern recognition becomes one of the biggest assets in building the next business faster.
  anchor: >-
    interview more people than you think you should. And I know how costly this is as a business owner.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    The author states the cost openly: his partner interviewed 600 developers over about a year to find the CTO, and he had to hire five sales managers, wasting six months to a year on each, before finding a good one.
  anchor_at: "video-business-that-runs-without-you.md@28833"
- id: B-video-ev-018
  type: rule
  name: >-
    Group interviews
  statement: >-
    Frontline and manager-level candidates are interviewed in groups rather than one at a time.
  why: >-
    It saves the owner time and lets them read people's vibes very quickly.
  applies_when: >-
    Frontline up to roughly manager level; the author says it is tough once you get into director and executive roles.
  anchor: >-
    you can have group interviews because it'll save you time and you'll very quickly be able to to read people's vibes
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@29158"
- id: B-video-ev-019
  type: rule
  name: >-
    Learn from them or do not hire them
  statement: >-
    At leadership level and above, an interview in which you learn nothing from the candidate is a waste of time and the candidate is not the hire.
  why: >-
    If you are not learning from them you will have to teach them, so your life gets worse before it gets better; the cheapest learning available is getting people out of your league to teach you about the role while you are also finding great talent.
  applies_when: >-
    Leadership roles and above; for those roles the candidate should be telling you what the function needs.
  anchor: >-
    if you aren't learning from the person, especially if it's in a leadership role or above, waste of time
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 2
  anchor_at: "video-business-that-runs-without-you.md@31843"
- id: B-video-ev-020
  type: rule
  name: >-
    Remove yourself from marketing
  statement: >-
    If the business relies on the owner's face to get customers, acquisition is rebuilt so that customers arrive without the founder appearing.
  why: >-
    Founder-led acquisition is one of the biggest risk factors in a business: it is why the owner cannot leave and why revenue drops when they do; having everyone rely on you feeds the ego, but to make an important business you have to become less important.
  anchor: >-
    but if your face gets the customers, you are the key man
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@33579"
- id: B-video-ev-021
  type: rule
  name: >-
    Seven marketing capture systems
  statement: >-
    In place of direct-to-camera founder ads, standing processes are installed that collect marketing material for the owner: weekly screenshots of praise in the customer community, incentives (credits, unlockables, a trial of a higher tier) for testimonials, life cycle ads from existing recordings, capture of emotive delivery moments, a per-testimonial bounty for support reps, and existing Google, Yelp, TripAdvisor or Amazon reviews turned into ads.
  why: >-
    Each of these exists already inside the business and produces ads without the founder on camera; the one-star reviews can be used as Liquid Death does, since clearly casting out the wrong type of person pulls in the right type.
  applies_when: >-
    A founder-led business removing its face from acquisition; the author adds that an affiliate programme or whitelisted TikTok shop creator ads go further in the same direction.
  anchor: >-
    There are seven different ways that you can install systems into the business to capture media and marketing on your behalf
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    The author lists six or seven items loosely from memory in one pass and marks the count himself as approximate.
  anchor_at: "video-business-that-runs-without-you.md@33830"
- id: B-video-ev-022
  type: rule
  name: >-
    Life cycle ads
  statement: >-
    Sales calls, onboarding calls and delivery checkpoints are recorded so that when a customer gives a testimonial their whole journey can be pulled from the CRM and scheduler and compressed into a timeline ad.
  why: >-
    Instead of the customer saying I was here and now I am here, the ad shows them scared, unsure and hesitating before signing up, and then the outcome.
  applies_when: >-
    The business already records calls and has a CRM and scheduler.
  anchor: >-
    look back through our scheduling and pull the recordings from their sales call to their onboarding to each of their touch points
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@35507"
- id: B-video-ev-023
  type: rule
  name: >-
    Take the 90 days off
  statement: >-
    After the inventory, the decision trees, the scorecards, the hiring and the removal from marketing, the owner actually takes the 90 days off and treats whatever breaks as the next item of work.
  why: >-
    Something will break, and the stress test is what reveals which dependency is left; the steps before it are only preparation for this one.
  anchor: >-
    And then finally, actually take your 90 days off. And something will break
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@39400"
- id: B-video-ev-024
  type: rule
  name: >-
    Decentralise decision-making
  statement: >-
    Decisions are pushed down to very smart and capable people rather than kept with the owner.
  why: >-
    No genuinely big business can have one person really involved in everything, so a business that grows without you is one staffed by people good enough to decide without you.
  anchor: >-
    And so you have to decentralize decision-making, two very smart people who are very capable.
  source: >-
    video-business-that-runs-without-you.md, zoom-out
  confirmations: 1
  authors_caveat: >-
    Said once, in the zoom-out where the author argues the tactics are downstream of being someone good people want to work for.
  anchor_at: "video-business-that-runs-without-you.md@41583"
- id: B-video-ev-025
  type: rule
  name: >-
    Track record or the ability to sell the future
  statement: >-
    To attract A-level talent the owner must bring either an experience and track record or a credible ability to sell the future, and without either must first build something smaller as proof.
  why: >-
    The best people only work for someone good enough to work for; the author had to build Gym Launch to prove he could build something of that size before acquisition.com could attract talent orders of magnitude better.
  applies_when: >-
    Generic proof of ambition, such as being valedictorian or president of several things, can stand in for a business track record if you can sell the future well enough.
  anchor: >-
    Your experience and track record and your ability to sell the future.
  source: >-
    video-business-that-runs-without-you.md, zoom-out
  confirmations: 1
  authors_caveat: >-
    Said once, thinking aloud; the author frames it as the real reason the tactics fail rather than as a step in the process.
  anchor_at: "video-business-that-runs-without-you.md@42234"
- id: B-video-ev-026
  type: rule
  name: >-
    Cash flow first, then enterprise value
  statement: >-
    Enterprise value is the goal only once the business already covers the owner's cash needs; if you do not know where next month's rent comes from, it is not your game yet.
  why: >-
    By the time a business actually has enterprise value it has already generated more than sufficient cash flow for the owner, and the excess cash flow it keeps transferring to the owner is taxed inefficiently.
  applies_when: >-
    The author addresses business owners trying to get bigger and scale; the bigger you get and the more the needs around you are satisfied, the more enterprise value matters.
  anchor: >-
    Once a business actually has enterprise value, it usually has already generated or had the ability to generate more than sufficient cash flow for the owner.
  source: >-
    video-business-that-runs-without-you.md, EV answer
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@45148"
- id: B-video-ev-027
  type: rule
  name: >-
    Enterprise value as the wealth vehicle
  statement: >-
    Wealth is accumulated by growing the value of what you own rather than by taking profit as income, and profit is reinvested into the business instead of being chased through tax strategy.
  why: >-
    Income is taxed to oblivion with zero multiplication, while growth in enterprise value is untaxed until sale and compounds; the same extra $500,000 of profit adds $250,000 after tax to one owner and $3 million of net worth at a 6x multiple to the other; a high-value enterprise can also be borrowed against, used for lines of credit and raised on.
  anchor: >-
    Then you want the most efficient tax vehicle for building wealth, which is your enterprise value.
  source: >-
    video-business-that-runs-without-you.md, EV answer
  confirmations: 3
  anchor_at: "video-business-that-runs-without-you.md@46051"
- id: B-video-ev-028
  type: rule
  name: >-
    Focus on not losing customers
  statement: >-
    The business's primary retention question is how not to lose customers, ahead of increasing acquisition.
  why: >-
    Two businesses can both reach 300 customers, one by tripling acquisition every year while churning everyone, the other by keeping each cohort; keeping customers for ten years is significantly easier than doubling marketing and sales every year, and an investor values the second on the same value equation the customer uses, as likelier, faster and less effortful.
  anchor: >-
    what every business owner needs to focus on is how do I not lose customers
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 2
  anchor_at: "video-make-money-so-fast.md@36143"
- id: B-video-ev-029
  type: rule
  name: >-
    Cost of a permanent customer
  statement: >-
    The number the business plans against is the cost of a permanent customer: the cost to acquire a customer multiplied by how many customers it takes to produce one who stays.
  why: >-
    Only the permanent base is what the enterprise value multiple is applied to, so the arbitrage that builds wealth is between the permanent CAC and the multiple on the recurring revenue that base produces; everything else is sifting for the kernels.
  applies_when: >-
    The author counts a customer who has stayed two-plus years as permanent within this calculation; in his worked example one in ten customers becomes permanent, so CAC is multiplied by ten.
  anchor: >-
    how much does it cost to get a customer multiply it by 10 this is actually the recurring base that we're trying to build
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 2
  authors_caveat: >-
    Calculated live on a whiteboard; the transcript's per-customer enterprise value figure ($122,000 for $1,200 of ARR at a 10x topline multiple) is garbled, the arithmetic gives $12,000.
  anchor_at: "video-make-money-so-fast.md@40787"
- id: B-video-ev-030
  type: rule
  name: >-
    Pick the opportunity vehicle by the multiple
  statement: >-
    Choose the business vehicle by what a dollar of its revenue is worth at exit, since identical acquisition cost and identical annual revenue produce very different enterprise value under a topline multiple than under a profit multiple.
  why: >-
    In the author's worked comparison the same $900 permanent CAC and $1,200 a year of revenue is worth ten times topline in a B2B SaaS with good retention and roughly 7x EBITDA in a business valued on profit, so the same effort buys a far larger asset in the first vehicle.
  applies_when: >-
    Topline multiples of that size assume good retention metrics, which is why permanent customers matter to the choice.
  anchor: >-
    this is why picking a good opportunity vehicle because in both of these situations you still spent the $900 per customer
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 1
  authors_caveat: >-
    Worked live with round numbers; EBITDA appears in the transcript as eida.
  anchor_at: "video-make-money-so-fast.md@35791"
- id: B-video-ev-031
  type: rule
  name: >-
    Advertise to the avatar that stays
  statement: >-
    Advertising is re-aimed at the avatar that actually becomes permanent, even at a higher cost per customer, as long as the cost per permanent customer falls.
  why: >-
    Changing the advertising to attract only those customers raises the hit rate: a CAC that doubles but converts one in three instead of one in ten costs $600 per permanent customer instead of $1,000.
  applies_when: >-
    You have measured which share of customers become permanent and can see how the permanent ones differ from the other nine.
  anchor: >-
    if we changed our advertising and attracted only those types of customers we would be able to get a higher hit rate on that
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 1
  anchor_at: "video-make-money-so-fast.md@41306"
- id: B-video-ev-032
  type: rule
  name: >-
    Operations is a vendor to the other two legs
  statement: >-
    The internal operations leader supports acquisition and delivery and never makes the big decisions of the business.
  why: >-
    Operations exists to support the other two functions, the things that keep you out of prison and keep the machine running, and its decisions should be the ones that let the business get more customers or deliver on them better.
  applies_when: >-
    A business with the three functional leaders in place: acquisition, delivery, and internal operations.
  anchor: >-
    that person should never be making the big decisions in the business
  source: >-
    video-13-years-no-bs-business-advice.md, point 16
  confirmations: 1
  anchor_at: "video-13-years-no-bs-business-advice.md@72105"
- id: B-video-ev-033
  type: rule
  name: >-
    The only three ways to increase Enterprise Value
  statement: >-
    An initiative counts as building enterprise value only if it gets more customers, makes customers worth more, or decreases risk in the business.
  why: >-
    Those three roll up exactly to the three legs of the stool, acquisition, delivery and operations; a business with no major risk, customers available on demand and an LTV that keeps scaling is a valuable business.
  anchor: >-
    the only three things that you can do to increase Enterprise Value in business you can get more customers you can make them worth more
  source: >-
    video-13-years-no-bs-business-advice.md, point 16
  confirmations: 1
  anchor_at: "video-13-years-no-bs-business-advice.md@72360"
- id: B-video-ev-034
  type: rule
  name: >-
    Overextension is a who problem
  statement: >-
    Before adding a second unit, check that a person good enough to run the existing one without you is already in place; if not, the expansion is a who problem and is not made.
  why: >-
    Opening the second location while the first is not really running well drops the first location's revenue, splits the star person and the owner across two sites, and leaves the same profit with twice the risk; opening a third compounds it.
  applies_when: >-
    The author sees it most in the $1M to $3M range, where the owner is already out of selling and delivery and therefore assumes wrongly that the business does not need them.
  anchor: >-
    overextension is typically a who problem which is you don't have enough good people that you left behind who can actually run it without you
  source: >-
    video-no-bs-business-advice-2026.md, overextension
  confirmations: 1
  anchor_at: "video-no-bs-business-advice-2026.md@69476"
- id: B-video-ev-035
  type: rule
  name: >-
    Backfill yourself
  statement: >-
    The owner hands the CEO role to an operator who runs the business behind them, on the ground that owner and CEO are two different jobs that happen to sit in the same person.
  why: >-
    If you work every hour of the day but are not selling and not delivering, the other stuff you are doing is operating the business, which is why it stops running as well the moment you leave.
  anchor: >-
    so you have to have somebody who's going to operate behind you you have to basically backfill yourself
  source: >-
    video-no-bs-business-advice-2026.md, overextension
  confirmations: 1
  anchor_at: "video-no-bs-business-advice-2026.md@70605"
- id: B-video-ev-036
  type: rule
  name: >-
    The six-month test
  statement: >-
    The business must maintain or grow for six straight months without the owner's direct involvement, with a one-month version as the minimum trial.
  why: >-
    Without your direct involvement is the load-bearing part: running the test while still working in the day-to-day only proves that the business operates with you as CEO and delays the decision by six months.
  applies_when: >-
    Before adding the next location or business.
  anchor: >-
    the six-month test I was alluding to is the business has to either maintain or grow for six straight months without your direct involvement
  source: >-
    video-no-bs-business-advice-2026.md, overextension
  confirmations: 2
  anchor_at: "video-no-bs-business-advice-2026.md@71723"
- id: B-video-ev-037
  type: rule
  name: >-
    The phone test
  statement: >-
    The operator's override, profit share or stock is paid explicitly in exchange for the owner's phone not ringing during the test month, and any call means the deal is not met.
  why: >-
    The scenarios are role-played in advance so the operator acts instead of escalating: a burst pipe means calling a plumber directly, an emergency means calling 911, and either way it does not mean calling the owner.
  applies_when: >-
    The one-month or six-month absence test, handing the phone to the operator at the start.
  anchor: >-
    I'm doing this in exchange for this not ringing that's the deal and if this rings then that's not the deal
  source: >-
    video-no-bs-business-advice-2026.md, overextension
  confirmations: 1
  authors_caveat: >-
    In the 2025 lecture the author promises to explain a phone test later in the stream and never returns to it; the worked version exists only here.
  anchor_at: "video-no-bs-business-advice-2026.md@71026"
- id: B-video-ev-038
  type: rule
  name: >-
    Two ways out of overextension
  statement: >-
    An already overextended owner takes one of two routes: pay for an impressive operator out of their own income, or cut the losses, prune back to one concentrated unit, get it right and scale out again.
  why: >-
    Overextension leaves the owner with the same money, several times the risk and no one good enough left behind, so either the who is bought or the footprint is reduced until it can be run properly.
  anchor: >-
    you either have to hire incredibly impressive people which means that you're going to probably give up your income in order to bring this person on
  source: >-
    video-no-bs-business-advice-2026.md, overextension
  confirmations: 1
  anchor_at: "video-no-bs-business-advice-2026.md@69184"
```
