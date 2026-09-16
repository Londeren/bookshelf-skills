# Улов фазы 1 — Enterprise Value: fragments of four video transcripts (ярус 3), тип D: антипаттерны и границы

Группа `tier3-video-ev`, слаг `video-ev`, ярус 3. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **39** (экстрактор вернул 39, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `video-business-that-runs-without-you.md`, lecture | символы 4000–39500 | 1 | — |
| `video-business-that-runs-without-you.md`, zoom-out | символы 40321–44137 | 1 | — |
| `video-business-that-runs-without-you.md`, EV answer | символы 44492–47170 | 1 | — |
| `video-make-money-so-fast.md`, wealth alchemy | символы 31313–44384 | 1 | — |
| `video-13-years-no-bs-business-advice.md`, point 16 | символы 71372–73000 | 1 | — |
| `video-no-bs-business-advice-2026.md`, overextension | символы 67605–72500 | 1 | — |
| `video-13-years-no-bs-business-advice.md` (итого по файлу) | | | 1 |
| `video-business-that-runs-without-you.md` (итого по файлу) | | | 27 |
| `video-make-money-so-fast.md` (итого по файлу) | | | 5 |
| `video-no-bs-business-advice-2026.md` (итого по файлу) | | | 6 |

## Как собран файл

Экстрактор D (Antipatterns and boundaries) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier3-video-ev.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier3-video-ev-D.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: D-video-ev-001
  type: antipattern
  name: >-
    A business that requires you isn't a business
  statement: >-
    Building a company that cannot produce without the owner in it: the owner ends up with more
    liabilities, more dependencies, less optionality and a job he cannot quit, which is the opposite
    of the freedom the business was started for.
  why: >-
    Such a business is valueless without the owner, so nobody would buy it; only when something moves
    from valuable to you to valuable to anyone does it become something other people want to buy.
  anchor: >-
    A business that requires you isn't a business. And I'm going to say that the technical sense, anything that generates a profit with an LLC is a business. But in terms of the intention of the vast majority of people who begin a business, it's for freedom.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 2
  authors_caveat: >-
    He concedes the technical point himself: anything that turns a profit inside an LLC is a business.
    The claim is about the intent of freedom, made live at the opening of the lecture.
  anchor_at: "video-business-that-runs-without-you.md@4100"
- id: D-video-ev-002
  type: antipattern
  name: >-
    Getting wealthy off regular income
  statement: >-
    Trying to build wealth by accumulating after-tax income out of the business instead of building
    enterprise value inside it.
  why: >-
    Income is taxed to oblivion (he assumes 50%) and carries no multiplication, while the same extra
    profit inside a sellable business is multiplied by the valuation multiple and is untaxed until
    sale; on his whiteboard the same extra $500,000 of profit adds $250,000 of savings to one owner
    and $3 million of net worth to the other.
  anchor: >-
    It's very very inefficient to become wealthy off of regular income because it's taxed to oblivion
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 3
  authors_caveat: >-
    Live whiteboard arithmetic on round numbers (a 6x profit multiple, 50% tax); the EV answer states
    the same as excess cash flow reaching the owner in a tax inefficient manner, and the wealth
    alchemy fragment repeats it as the effective-tax-rate example.
  anchor_at: "video-business-that-runs-without-you.md@8652"
- id: D-video-ev-003
  type: antipattern
  name: >-
    Nobody can do it as well as me
  statement: >-
    Keeping a task on the owner's plate because nobody will ever be able to do it as well as he does.
  why: >-
    The belief is not true and had to be broken: it only holds per unit of practice. If he can do it
    right with part of his time, someone else can do it better with all of their time, and a person
    taught only the right way without the bad mistakes may start at 50% of him.
  anchor: >-
    no one's going to ever be able to do it as as well as you. Not true.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    Stated as a belief of his own that he had to break; he grants that nobody will match you at one
    tenth of the reps, and that a five out of ten done in one tenth of your time is not a hundred.
  anchor_at: "video-business-that-runs-without-you.md@19184"
- id: D-video-ev-004
  type: antipattern
  name: >-
    Outworking everyone
  statement: >-
    Trying to carry the business on your own work ethic: you can outwork anyone in your business, but
    you cannot outwork everyone in it.
  why: >-
    The longer he took to learn it, the longer it limited his ability to grow — a mountain of work is
    possible alone, Mount Everest needs more hands and more shovels, which is what an organization is.
  anchor: >-
    you can outwork anyone in your business. You will not be able to outwork everyone.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    Told as his own late lesson; he says he prides himself on his work ethic.
  anchor_at: "video-business-that-runs-without-you.md@20790"
- id: D-video-ev-005
  type: rule
  name: >-
    Where if-this-then-that stops standardizing
  statement: >-
    Decision trees (if this, then that) are written for the questions that repeat in a role.
  why: >-
    Standardization rises with repetition: the same handful of requests come back (change my card,
    change my flavor, change my billing cadence) and each gets one written answer.
  boundary: >-
    The more complex the role, the more one-off the scenario and the less it standardizes; the method
    pays off where the job is duplicatable and several people sit in the same department or function.
  anchor: >-
    The more complex the roles, the more one-off the scenario. The more duplicatable the job, the more people you have in a specific department or function typically the more standardized the questions become.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@13677"
- id: D-video-ev-006
  type: rule
  name: >-
    The money threshold on delegated decisions
  statement: >-
    A delegated decision is bounded by a money threshold per decision plus a total cap, so the person
    can act independently without supervision inside it (his example: decisions under $500 each, up to
    $5,000 in total, which gives ten shots to fix something).
  why: >-
    Monthly financials remain the feedback loop: if something looks out of whack at the end of the
    month you go and check it.
  boundary: >-
    There is no universal number — under $500, under $1,000, under $10,000, sometimes under $100,000;
    the threshold depends on the size of the company.
  anchor: >-
    we decide that under $500 or under $1,000, under $10,000, depends on the size of your company, under $100,000 sometimes
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@14215"
- id: D-video-ev-007
  type: antipattern
  name: >-
    Delegated spend nobody checks against value
  statement: >-
    Letting a delegated perk run without asking whether it generates true value — his team's surprise
    five-star client dinners had reached $250,000 a month before he saw the bill.
  why: >-
    When the perk was removed nothing changed in the happiness scores or the reviews: the spend bought
    no measurable value.
  anchor: >-
    when we removed that thing it didn't change anything about our our happiness scores or reviews or anything like that
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    He frames the episode as expected rather than as a failure of delegation: there is going to be a
    feedback loop and you are going to mess up; the guards are the cap on delegated spend and the
    monthly financials.
  anchor_at: "video-business-that-runs-without-you.md@15269"
- id: D-video-ev-008
  type: antipattern
  name: >-
    The team cannot say how their role makes money
  statement: >-
    Unlocking decision rights and scorecards for people who cannot answer how they and their role make
    the company money.
  why: >-
    Ask the question today and many of them will not know the answer, and that will frighten you; the
    connection is also what gives a role its felt impact — if you have a job in a company you have an
    impact, you probably just don't know what it is.
  applies_when: >-
    Any role, including the ancillary ones (finance, tech, media) where the link to revenue is indirect;
    his worked example is the camera operator, whose mistakes are reversed into the metrics he is held to.
  anchor: >-
    If you ask this to your team today many of them will not know the answer to that question
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@16341"
- id: D-video-ev-009
  type: rule
  name: >-
    The 80% handoff bar
  statement: >-
    A handoff is accepted when the person delivers 80%, sometimes 60%, of the owner's result, tested
    against the scorecard and KPIs rather than against the owner's feel.
  why: >-
    Waiting for a hundred percent keeps the work with the owner; someone at 80% who improves fast
    passes him anyway.
  boundary: >-
    Only as long as there is a clear path to them getting better; without that path the lower bar does
    not apply.
  anchor: >-
    initially I'm cool with 80% sometimes 60% as good as long as I have a clear path to them getting better.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@23377"
- id: D-video-ev-010
  type: antipattern
  name: >-
    Measuring employees by how well they start
  statement: >-
    Judging a new employee by the level they start at instead of by how fast they improve.
  why: >-
    A weaker starter who improves fast passes a flat strong starter within three to six months and
    keeps going; he measures intelligence as rate of learning and would rather have the faster learner
    than the more experienced slower learner.
  anchor: >-
    I used to measure employees by how well they started. I measure employees today on how fast they improve.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    He limits it himself — it depends on the role, obviously — and presents it as a personal shift in
    how he thinks about talent.
  anchor_at: "video-business-that-runs-without-you.md@23525"
- id: D-video-ev-011
  type: antipattern
  name: >-
    Overextension
  statement: >-
    Opening the second location (and then the third) while the first is not really operating as well as
    you think it is.
  why: >-
    Revenue at the first drops as soon as you leave it, and that revenue was your profit; the new one is
    not yet at the first one's level, your star person is split between sites, so you end up making the
    same money with twice the fixed cost and twice the risk, then three times the risk and no profit.
    Overexpansion is one of the number one reasons people go out of business.
  applies_when: >-
    Two fixes only: hire incredibly impressive people, which will probably cost you your own income, or
    cut your losses, prune the tree, reconcentrate, get it right and scale back out again the right way.
  anchor: >-
    where you open that second location when the first location isn't really operating as much as well as you think it is
  source: >-
    video-no-bs-business-advice-2026.md, overextension
  confirmations: 2
  authors_caveat: >-
    He calls it his own greatest hit of mistakes; the lecture states the same conclusion in one line.
  anchor_at: "video-no-bs-business-advice-2026.md@68249"
- id: D-video-ev-012
  type: antipattern
  name: >-
    Expanding on a business that only stays flat without you
  statement: >-
    Treating survival as the pass mark — the business did not burn down while you were away — and
    expanding on that.
  why: >-
    As soon as your attention moves, a business that is merely flat often starts to decline, and then
    you are carrying double the liability, debt and overhead with half the talent, spread across two
    sites: more risk and less profit.
  applies_when: >-
    The bar before a second location: leave it alone for three months and come back to a bigger
    business, not the same one.
  anchor: >-
    As soon as the eye of Sauron moves, sometimes if it's flat, it's going to go down. Now all of a sudden, you've got double the liability, double the debt, double the overhead, half the talent because it's spread.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@25775"
- id: D-video-ev-013
  type: rule
  name: >-
    The growth litmus test and its exception
  statement: >-
    The real test is not that the business survives your absence but that it is bigger when you come
    back.
  why: >-
    A business that grows without the owner is a faster growing annuity for an investor, which is what
    buys the multiple.
  boundary: >-
    Unless you are in a super capped market where there is no way it can grow — there flat is fine; but
    the vast majority of businesses can improve and grow year over year if the business is good.
  anchor: >-
    Unless you're in a super cap market where there's no way it can grow, fine.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@25503"
- id: D-video-ev-014
  type: antipattern
  name: >-
    Reading the absence of disasters as a metric
  statement: >-
    Concluding a function is healthy from the absence of bad outcomes — a low refund rate proving the
    product is good, no recent lawsuits proving the talent function is good.
  why: >-
    That is not how you know you have a good product, and it is not a way to know you have a good
    culture, team or talent process. Skill in any function is read from the quality and quantity of the
    metrics the person tracks — his HR hire asked him for cost of acquiring talent, time to fill and
    the 90-day two-way fit, and he knew none of them.
  anchor: >-
    if I have a low refund rate, therefore my product is good. It's kind of like I had that on the talent side
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    Told against himself, as the internet-marketer thinking he arrived with.
  anchor_at: "video-business-that-runs-without-you.md@27539"
- id: D-video-ev-015
  type: antipattern
  name: >-
    Interviewing too few people
  statement: >-
    Interviewing fewer candidates for a role than you think you should.
  why: >-
    Volume is what tunes your picker: ten people claiming the same role tell you far more than one, by
    the fiftieth you know who has game, and that pattern recognition becomes one of your biggest assets.
    His co-founder Sam interviewed 600 developers over a year to find the CTO.
  applies_when: >-
    Every level, from frontline rep upward, and repeated at each new layer (first managers, then
    directors) because you do not yet know what right looks like there.
  anchor: >-
    I would interview as interview more people than you think you should.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    He acknowledges how costly this is for an owner and suggests stacking interviews to absorb it.
  anchor_at: "video-business-that-runs-without-you.md@28812"
- id: D-video-ev-016
  type: rule
  name: >-
    Group interviews and where they stop
  statement: >-
    Group interviews are used to get through volume and read people's vibes quickly.
  boundary: >-
    They work from frontline up to maybe manager level; once you get into director and executive roles
    it is tough.
  anchor: >-
    pretty high up once you get into director and executive, it's tough, but like anything that's like frontline to maybe even manager
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@29022"
- id: D-video-ev-017
  type: antipattern
  name: >-
    Hiring a leader you have to teach
  statement: >-
    Hiring into a leadership role or above someone you learn nothing from during the interview.
  why: >-
    If you are not learning from them you will have to teach them, so your life gets worse before it
    gets better; at that level the person should be telling you what to do for their function rather
    than being trained by you.
  anchor: >-
    if you aren't learning from the person, especially if it's in a leadership role or above, waste of time.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    He allows that teaching a hire is sometimes required — the rule bites at leadership level and above.
  anchor_at: "video-business-that-runs-without-you.md@31843"
- id: D-video-ev-018
  type: rule
  name: >-
    When you cannot buy the people who teach you
  statement: >-
    The cheapest learning available is hiring people far out of your league and being taught the role
    by them.
  boundary: >-
    When you are starting out this is not available: those people do not want to work for you, or you
    cannot afford them, or both.
  anchor: >-
    When you're starting out though, it's hard to afford those people because those people don't want to work for you
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 2
  anchor_at: "video-business-that-runs-without-you.md@28535"
- id: D-video-ev-019
  type: antipattern
  name: >-
    Founder-led acquisition
  statement: >-
    Leaving the business dependent on the founder to bring the customers in — the owner as breadwinner,
    promoter and the one who closes.
  why: >-
    It is one of the biggest risk factors in a business: it is why you cannot leave, and when you do
    leave revenue goes down. If your face gets the customers, you are the key man.
  applies_when: >-
    Very common in founder-led companies, including his own face-driven businesses.
  anchor: >-
    if the business relies on you to get customers which is very common in founder led companies
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@32653"
- id: D-video-ev-020
  type: antipattern
  name: >-
    The ego reward of being irreplaceable
  statement: >-
    Enjoying that everyone relies on you and treating that as evidence that you are important.
  why: >-
    It feels good in the short term and feeds the ego, but to make an important business you have to
    become less important; wanting to help more people and being the one who helps are incompatible.
  anchor: >-
    it feels good in the short term to have everyone rely on you, right? It feeds your ego.
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@33053"
- id: D-video-ev-021
  type: rule
  name: >-
    The 90 days off will break something
  statement: >-
    The stress test of the whole sequence is actually taking 90 days off.
  boundary: >-
    Something will break — breakage is part of the test, not a sign the test was premature; the process
    continues through it.
  anchor: >-
    actually take your 90 days off. And something will break, but you continue this
  source: >-
    video-business-that-runs-without-you.md, lecture
  confirmations: 1
  authors_caveat: >-
    The fragment ends mid-sentence here; the ultimate version of the test he states earlier is three
    months off with the business growing.
  anchor_at: "video-business-that-runs-without-you.md@39418"
- id: D-video-ev-022
  type: antipattern
  name: >-
    Looking for the answer in tactics
  statement: >-
    Explaining why the business is not as big, not as valuable and does not run without you by missing
    tactics, when the binding constraint is the owner's own level.
  why: >-
    Business at the simplest level is getting the best people in the world to work for you, and the best
    people only work for someone good enough — Jony Ive was an employee, but of Steve Jobs; the smartest
    people work for Elon because he is Elon. A big business cannot have one person involved in
    everything, so it needs capable people to decentralize to, and those people do not want to work for
    you yet.
  anchor: >-
    The reason that your business one isn't as big as you want, two isn't as valuable as you want, and number three doesn't run without you is because you're not as good as you think you are.
  source: >-
    video-business-that-runs-without-you.md, zoom-out
  confirmations: 1
  authors_caveat: >-
    Said once, at the end of the lecture, as the deliberate hard answer after the tactics ("I know that
    sometimes hurts people's earballs"); the source spells the designer's name as John Ivy.
  anchor_at: "video-business-that-runs-without-you.md@40321"
- id: D-video-ev-023
  type: rule
  name: >-
    The real real behind the tactics
  statement: >-
    The time study, the doing-to-managing switch, removing your face from marketing and the stress test
    are the steps.
  boundary: >-
    They only carry as far as the owner's own capability: you have to become someone capable that people
    would want to follow, which comes from experience and track record plus the ability to sell the
    future. An outstanding ability to sell the future can substitute for a thin track record.
  anchor: >-
    But the real real is that like you have to become someone who's capable who's who's desire people would want to follow
  source: >-
    video-business-that-runs-without-you.md, zoom-out
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@42055"
- id: D-video-ev-024
  type: rule
  name: >-
    Reputation is the precondition and it takes time
  statement: >-
    The level of talent you can attract tracks your proven track record; generic traits (valedictorian,
    president of three things) give only a semi-credible one.
  boundary: >-
    For ordinary operators the proof has to come before the pudding, and building the reputation takes
    time — he had to build Gym Launch first to be able to build something a hundred times bigger, and
    the talent acquisition.com attracts is orders of magnitude above Gym Launch and Prestige Labs.
  anchor: >-
    does that mean that it will take me time to develop a reputation? Yeah, it's kind of how it works.
  source: >-
    video-business-that-runs-without-you.md, zoom-out
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@43890"
- id: D-video-ev-025
  type: antipattern
  name: >-
    One person involved in everything
  statement: >-
    Staying involved in everything as the company gets big, instead of decentralizing decision-making
    to very smart, very capable people.
  why: >-
    No really big business can have one person really involved in everything — it is impossible; that is
    why the quality of the people you can decentralize to sets the ceiling.
  anchor: >-
    no real big businesses can have one person who's in really involved in everything. It's just impossible
  source: >-
    video-business-that-runs-without-you.md, zoom-out
  confirmations: 1
  anchor_at: "video-business-that-runs-without-you.md@41471"
- id: D-video-ev-026
  type: rule
  name: >-
    Enterprise value is a game you graduate into
  statement: >-
    Enterprise value becomes the objective to play for once the owner's cash needs, and the needs of the
    people around him, are already met.
  why: >-
    A business that actually has enterprise value has usually already generated more than sufficient cash
    flow for the owner, and the excess reaches him in a tax inefficient way — which is when the untaxed
    growth of enterprise value becomes the better vehicle.
  boundary: >-
    If you do not know where next month's rent is coming from, enterprise value is not your game. There
    are levels, and to move up a level you have to play a different game — you have to graduate.
  anchor: >-
    And you have to graduate. If you can't, if you don't know where your rent's coming next month
  source: >-
    video-business-that-runs-without-you.md, EV answer
  confirmations: 1
  authors_caveat: >-
    Spoken as a live answer to a viewer comment; the word after "next month" is missing from the
    transcript, the sense is that enterprise value is not the thing to chase.
  anchor_at: "video-business-that-runs-without-you.md@46449"
- id: D-video-ev-027
  type: antipattern
  name: >-
    Enterprise value is fictional numbers
  statement: >-
    Dismissing enterprise value as unliquidatable fiction and preferring hard cash flow.
  why: >-
    Stripe is not publicly traded and people still invest in it, so its founders can get liquidity; a
    high-value enterprise can be borrowed against, gives lines of credit, becomes an asset and lets you
    raise capital, while the cash flow preferred instead reaches the owner in a tax inefficient manner.
  anchor: >-
    Of course, you build net worth without taxes, but it's fictional numbers that can't liquidate. I like cash flow, hard cash.
  source: >-
    video-business-that-runs-without-you.md, EV answer
  confirmations: 1
  authors_caveat: >-
    The wording of the objection is a viewer comment he reads aloud before answering it, not his own
    formulation.
  anchor_at: "video-business-that-runs-without-you.md@44548"
- id: D-video-ev-028
  type: rule
  name: >-
    Net worth as the measure, and what it is not
  statement: >-
    Inside the game of business, net worth is the objective measure.
  boundary: >-
    He states explicitly that this is not the only game worth playing and that other games in life are
    worth winning; and that the content is aimed at business owners who are trying to get bigger and to
    scale.
  anchor: >-
    I'm not saying this game is the only game worth playing and there's not other games in life that are worth winning
  source: >-
    video-business-that-runs-without-you.md, EV answer
  confirmations: 2
  anchor_at: "video-business-that-runs-without-you.md@46987"
- id: D-video-ev-029
  type: rule
  name: >-
    The 10x topline multiple holds on retention
  statement: >-
    The wealth alchemy arithmetic prices a B2B SaaS business at roughly 10 times topline.
  boundary: >-
    That multiple is fairly typical only as long as the retention metrics are good — which is exactly why
    permanent CAC and the permanent customer are the units of the calculation.
  anchor: >-
    let's say that it trades at 10 times Topline which is fairly typical for like a B2B SAS business as long as you have good retention metrics
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 1
  authors_caveat: >-
    Live arithmetic: the per-customer enterprise value he says aloud, $122,000, is garbled — his own
    numbers ($1,200 a year at 10x) give $12,000.
  anchor_at: "video-make-money-so-fast.md@32839"
- id: D-video-ev-030
  type: antipattern
  name: >-
    The wrong opportunity vehicle
  statement: >-
    Running good acquisition economics inside a business type that is valued on a low multiple of profit.
  why: >-
    With the identical $900 permanent CAC and the identical $1,200 of annual revenue per customer, the
    10x-topline business turns $9 million of spend into $120 million of enterprise value while the
    7x-EBITDA business turns the same spend into about $21 million. The unit economics are the same; what
    differs is what a year of that revenue is worth, which is the choice of vehicle.
  anchor: >-
    in both of these situations you still spent the $900 per customer you still make the $1,200 per year but the big difference was how much is that $1,200 per year worth
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 1
  authors_caveat: >-
    He calls the 2-point-something multiple on the second business not bad — the weaker vehicle is still
    a good deal, just an order of magnitude less leverage. EBITDA is garbled as "eida" in the source.
  anchor_at: "video-make-money-so-fast.md@35846"
- id: D-video-ev-031
  type: antipattern
  name: >-
    The churn Factory
  statement: >-
    Growing by acquiring more customers each year while losing the previous year's base — 100, then 200,
    then 300 new customers, none of them kept.
  why: >-
    The only way to grow such a business is to market and sell more, which is a one-way road: at some
    point you sell through all the customers in the base, and doubling marketing and sales every year is
    hard. Two businesses can both stand at 300 customers and be nothing alike; you want time on your side,
    not as your enemy.
  anchor: >-
    the only way to grow this business is market and sell more but that is only a oneway road at some point you sell through all the customers within a given base
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 1
  authors_caveat: >-
    He also reads it through the investor's eyes: an investor values the business on the same value
    equation — likelihood, effort and sacrifice, time delay — so the retaining business is the less risky
    one.
  anchor_at: "video-make-money-so-fast.md@38063"
- id: D-video-ev-032
  type: antipattern
  name: >-
    Retention skipped because it isn't sexy
  statement: >-
    Not spending time on how not to lose customers, because retention is less attractive work than
    acquisition.
  why: >-
    Keeping the customers you already have for ten years is significantly easier than doubling marketing
    and sales every single year, and it is where the real leverage and the wealth alchemy actually happen.
  anchor: >-
    but just keeping the customers you had for 10 years significantly easier but people don't focus on because it's not as sexy
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 1
  authors_caveat: >-
    He says the concept of the permanent customer took him a long time to grasp as an entrepreneur.
  anchor_at: "video-make-money-so-fast.md@38503"
- id: D-video-ev-033
  type: antipattern
  name: >-
    Chasing tax loopholes instead of building value
  statement: >-
    Obsessing over tax strategy and maximizing loopholes as the way to keep more of what the business
    makes.
  why: >-
    The biggest and most obvious loophole is building something valuable: enterprise value compounds
    untaxed, and in his example $120 million of added value next to $3 million of profit taxed at 50%
    comes to an effective rate of about 1.5%. The clue was noticing that the Forbes names sat in
    California, the highest-tax state.
  boundary: >-
    The untaxed compounding holds only as long as you keep building it and do not want to cash it out —
    the growth is tax-free until the day you sell.
  anchor: >-
    I was really obsessed with tax strategy and trying to maximize all these loopholes when the biggest and most obvious one is just build something valuable
  source: >-
    video-make-money-so-fast.md, wealth alchemy
  confirmations: 1
  anchor_at: "video-make-money-so-fast.md@43779"
- id: D-video-ev-034
  type: antipattern
  name: >-
    The operations head making the big calls
  statement: >-
    Letting the leader of internal operations make the big decisions in the business.
  why: >-
    Operations is a vendor to the other two heads: its job is to support the decisions that let the
    company get more customers or deliver on them better, which is also the only way it contributes to
    enterprise value — the third lever, decreasing risk.
  applies_when: >-
    A business with the three functional leaders in place: acquisition, delivery, and internal operations
    (legal, HR, payroll, CRM).
  anchor: >-
    that person should never be making the big decisions in the business they should be supporting the decisions
  source: >-
    video-13-years-no-bs-business-advice.md, point 16
  confirmations: 1
  anchor_at: "video-13-years-no-bs-business-advice.md@72105"
- id: D-video-ev-035
  type: antipattern
  name: >-
    Overextension is a who problem
  statement: >-
    Reading overextension as a money, market or execution problem when it is a who problem — there are
    not enough good people left behind who can run the place without you.
  why: >-
    Only two ways out follow from that diagnosis: hire incredibly impressive people, paid for out of your
    own income, or prune the tree, reconcentrate, get it right and scale back out the right way.
  applies_when: >-
    It happens at all revenue ranges but concentrates around the $1 to $3 million range (the transcript
    garbles the figures), where the owner has pulled himself out of selling and delivering.
  anchor: >-
    so overextension is typically a who problem which is you don't have enough good people that you left behind who can actually run it without you
  source: >-
    video-no-bs-business-advice-2026.md, overextension
  confirmations: 1
  anchor_at: "video-no-bs-business-advice-2026.md@69473"
- id: D-video-ev-036
  type: antipattern
  name: >-
    Not selling or delivering mistaken for being out of the business
  statement: >-
    Concluding that because you are no longer involved in acquisition or delivery you are no longer
    required to run the business.
  why: >-
    You still work every hour of the day, and the other stuff filling those hours is very much operating
    the business — which is why the business stops running as well the moment you step away.
  anchor: >-
    you think that because you're not involved in the acquisition and delivery that you're not required to run the business
  source: >-
    video-no-bs-business-advice-2026.md, overextension
  confirmations: 1
  anchor_at: "video-no-bs-business-advice-2026.md@69938"
- id: D-video-ev-037
  type: antipattern
  name: >-
    Owner and CEO treated as one role
  statement: >-
    Assuming that owner and CEO mean the same thing because you happen to be both.
  why: >-
    They are not the same. When the CEO leaves, the business stops running as well, so somebody has to
    operate behind you: you have to backfill yourself before you can own without running.
  anchor: >-
    a lot of owners will mistakenly think that CEO and owner mean the same thing you happen to be both but they are not the same
  source: >-
    video-no-bs-business-advice-2026.md, overextension
  confirmations: 1
  anchor_at: "video-no-bs-business-advice-2026.md@70330"
- id: D-video-ev-038
  type: antipattern
  name: >-
    Faking the six-month test
  statement: >-
    Running the six-month test while carrying on in the day-to-day exactly as before, then declaring
    you passed it.
  why: >-
    Nothing changed: the business kept operating with you as its CEO, so the test proved nothing and you
    only delayed the next location by six months — better for your cash position, not his recommendation.
  boundary: >-
    The test only counts without your direct involvement: the business has to maintain or grow for six
    straight months while you are out of it (one month as the minimum version), with the phone handed to
    the operator.
  anchor: >-
    some of you are going to run that test still continue to work in the day-to-day for six months and then say oh I think I did it
  source: >-
    video-no-bs-business-advice-2026.md, overextension
  confirmations: 1
  anchor_at: "video-no-bs-business-advice-2026.md@71934"
- id: D-video-ev-039
  type: antipattern
  name: >-
    The operator whose answer is to call you
  statement: >-
    An operator who escalates to the owner — a pipe bursts and the answer is to call you.
  why: >-
    Wrong answer: all the owner would do is call a plumber, so the operator should call the plumber
    directly. If it is an emergency call 911, if it is not an emergency do not call; either way do not
    call. The phone not ringing is the actual deal traded against the operator's override or profit share.
  applies_when: >-
    Role-played out loud with the operator before the owner leaves, scenario by scenario.
  anchor: >-
    so it's like let's say a pipe burst what do you do if it's call you wrong answer
  source: >-
    video-no-bs-business-advice-2026.md, overextension
  confirmations: 1
  authors_caveat: >-
    The lecture promises a "phone test" and never delivers it; this fragment is where the test is
    actually described.
  anchor_at: "video-no-bs-business-advice-2026.md@71176"
```
