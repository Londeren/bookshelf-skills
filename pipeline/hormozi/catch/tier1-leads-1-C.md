# Улов фазы 1 — $100M Leads (2023), chapters up to #3 Cold Outreach (lines 1–6900) (ярус 1), тип C: разборы (кейсы)

Группа `tier1-leads-1`, слаг `leads-1`, ярус 1. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **37** (экстрактор вернул 37, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-leads.md` | 1–6900 | 6 | 37 |

## Как собран файл

Экстрактор C (Application cases) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier1-leads-1.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier1-leads-1-C.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: C-leads-1-001
  type: case
  name: >-
    The webinar nobody watched versus the 13-minute case study
  statement: >-
    Eight Sundays of building a webinar plus \$150 per day of ads produced 80 leads
    and 0 sales in three days, and he shut it down. He then copied an ad that had
    engaged him ("Free Case Study on How I Spent \$1 and Made \$123,000 in a Weekend"),
    recorded a plain 13-minute screen share of a real gym launch, put it behind the
    headline "FREE Case Study: How we added 213 members and \$112,000 in revenue to a
    small gym in San Diego", and sent viewers to a booking page. The next morning
    strangers had booked the calendar solid for a week.
  why: >-
    Author: they did not want the webinar, they wanted the case study; getting leads
    works by giving people something they want, and the results of what engages are
    often surprising, so you will not know until you try.
  demonstrates: >-
    A lead magnet has to be the thing the audience actually wants, not the most
    impressive thing you can build; swapping the lead magnet outranks polishing it.
  anchor: >-
    Three days, \$450, 80 leads, and 0 sales later...
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 1705–1831
  confirmations: 2
  anchor_at: "100m-leads.md:1712"
- id: C-leads-1-002
  type: case
  name: >-
    The script of the 13-minute case study lead magnet
  statement: >-
    Skeleton of the recording, in order: here is the ad account of a gym we just
    launched, here are the ads we ran, this is how much we spent, this is the page and
    offer we sent them to, here are the leads, the appointments scheduled, the shows,
    the sales, and this is how much the gym owner made. It closes with the offer and a
    CTA: we will do the whole thing for free and only get paid off the sales you make,
    if that sounds fair, book a call. No slides, no presenting, about 13 minutes.
  why: >-
    The format he copied was nothing fancy, no slides, no presenting, just a dude
    explaining how his stuff worked - which is why he judged he could do it himself.
  demonstrates: >-
    A lead magnet delivered as information plus free service, ending in a Call To
    Action that says what to do and why it is fair.
  anchor: >-
    Okay everyone. So here's the ad account of a gym we just launched. Here
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 1757–1778
  confirmations: 1
  anchor_at: "100m-leads.md:1757"
- id: C-leads-1-003
  type: case
  name: >-
    The book worked through as its own lead magnet
  statement: >-
    Walk-through of Step 1 on the book in hand: the book is the lead magnet, the reader
    is the lead, the narrow problem is getting engaged leads, and the audience is
    businesses making less than \$1,000,000 in annual profit. Solving it moves them past
    \$1,000,000, which is the qualification for the core offer - him investing in the
    company to help it scale.
  why: >-
    Leads who take a free or low-cost offer now are more likely to buy the related
    higher-cost offer later, provided the problem the lead magnet reveals is the one the
    core offer solves.
  demonstrates: >-
    Step 1 of the seven steps: pick a narrow problem whose next problem your core offer
    solves, and pick who you solve it for.
  anchor: >-
    lead magnet. You are a lead. I want to solve an engaged lead problem.
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 1955–1961
  confirmations: 1
  anchor_at: "100m-leads.md:1956"
- id: C-leads-1-004
  type: case
  name: >-
    Narrow problems in front of selling a home
  statement: >-
    "Help homeowners sell their homes" is a broad solution. The steps before it are the
    narrow problems: what the house is worth, how to increase its value, pictures,
    cleaning, landscaping, minor repairs, moving services, staging. Pick one and solve it
    free; it helps but makes the remaining problem obvious - they still have to sell the
    home - and with trust now earned you charge to solve that with the core offer.
  why: >-
    Every solution reveals more problems; the winner is a narrow problem whose revealed
    problem your core offer solves in exchange for money.
  demonstrates: >-
    The Problem-Solution cycle used to choose a lead magnet problem.
  anchor: >-
    They need pictures. They need it cleaned. They need landscaping.
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 1992–2010
  confirmations: 1
  anchor_at: "100m-leads.md:1996"
- id: C-leads-1-005
  type: case
  name: >-
    Worked examples of the three lead magnet types
  statement: >-
    Reveal Their Problem - a termite inspection showing what the bugs do: if they have
    termites you remove them cheaper than the cost of another home, if they do not you
    sell prevention, so you can sell them either way. Samples And Trials - a free
    adjustment that gives relief, with permanent benefits only if they buy more; a
    consumable sample, the way Costco sells food. One Step Of A Multi-Step Process - one
    free coat of garage-door sealant out of the three the job needs, explained as partial
    coverage, with the other two offered as a bundle.
  why: >-
    All three solve one problem and reveal others; diagnosis-type magnets work best when
    the problem they reveal gets worse the longer you wait, and samples work best when the
    core offer is a recurring solution to a recurring problem.
  demonstrates: >-
    Step 2 of the seven steps: the three types of lead magnet.
  anchor: >-
    sealant for a garage door. But the sealing process requires three
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 2039–2117
  confirmations: 1
  anchor_at: "100m-leads.md:2107"
- id: C-leads-1-006
  type: case
  name: >-
    Twelve lead magnets for one audience - gym owners
  statement: >-
    The same narrow audience, one delivery form at a time. Software: a spreadsheet or
    dashboard giving a gym owner his business stats, comparing them to industry averages
    and ranking him. Information: a mini course on how to write an ad. Services: running
    a gym owner's ads free for thirty days. Physical product: a book for gym owners, Gym
    Launch Secrets. Three types times four delivery forms is up to twelve lead magnets
    for a single narrow problem; he makes as many versions as he can and rotates them.
  why: >-
    Rotating versions keeps advertising fresh and low effort and shows which ones work
    best, and the winners are often surprising.
  demonstrates: >-
    Step 3 of the seven steps: the four ways to deliver a lead magnet.
  anchor: >-
    Ex: I give away a spreadsheet or dashboard that gives a gym owner all
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 2148–2199
  confirmations: 1
  anchor_at: "100m-leads.md:2153"
- id: C-leads-1-007
  type: case
  name: >-
    Testing the title and subtitle of \$100M Leads
  statement: >-
    Head-to-head polls run on his own following. Headline: Advertising beat Promotion,
    Leads beat Advertising, Leads beat Marketing. Image: real beat cartoon. Subheadline,
    four rounds, all won by "How to get strangers to want to buy your stuff" - over "How
    to get more people...", "How to get more strangers...", "How to get as many leads as
    you darn well please", and over "Get strangers to want to buy your stuff", a loss
    turning on the two words "how to". One round was won by deleting the single word
    "more".
  why: >-
    Five times more people read the headline than any other part of the promotion, so how
    you present the lead magnet matters more than anything; small changes make big
    differences, and if nobody notices it nobody learns how good it is.
  applies_when: >-
    Test in this order - headline first, then images, then subheadline; if you test only
    one thing, test the headline.
  demonstrates: >-
    Step 4 of the seven steps: test what to name it, with polls if you have any following
    at all.
  anchor: >-
    1) "How to get strangers to want to buy your stuff" overwhelmingly beat
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 2240–2376
  confirmations: 1
  anchor_at: "100m-leads.md:2341"
- id: C-leads-1-008
  type: case
  name: >-
    \$100M Offers split evenly across four formats
  statement: >-
    The first book ended with a near-perfect quarter-quarter-quarter-quarter split
    between ebooks, physical books, audiobooks and videos; publishing in every format is
    called the easiest way he knows to get 2-3-4x the leads for the same work.
  why: >-
    People consume in different ways; a single format would have missed the three to four
    times as many people who would not have read the book otherwise.
  demonstrates: >-
    Step 5 of the seven steps: make the lead magnet easy to consume by packaging it every
    way you can.
  anchor: >-
    perfect ¼, ¼, ¼, ¼ split between ebooks, physical books, audiobooks, and
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 2433–2439
  confirmations: 1
  anchor_at: "100m-leads.md:2434"
- id: C-leads-1-009
  type: case
  name: >-
    Scarcity and urgency lines for a CTA
  statement: >-
    Scarcity taken from a real limit: "The most convenient class times fill up fast. Call
    now to get the one you want."; "I can only handle five people per week, so if you want
    it solved soon, do xyz..."; one batch of shirts that will never be reprinted. Urgency
    taken from a deadline: a July 4th promotion ending Monday at midnight; a Black Friday
    promotion with four hours left; a free hat through Friday for anyone buying more than
    three books.
  why: >-
    The fewer you have the more valuable people think it is, and the less time people have
    the faster they act; drawing attention to the natural limits of your business is
    ethical scarcity you may as well use to make money.
  demonstrates: >-
    Step 7 of the seven steps: a CTA needs what to do plus reasons to do it right now.
  anchor: >-
    "I can only handle five people per week, so if you want it solved soon,
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 2530–2592
  confirmations: 1
  anchor_at: "100m-leads.md:2557"
- id: C-leads-1-010
  type: case
  name: >-
    Fraternity Party Planner - make up a reason
  statement: >-
    Fraternity reasons to party ("John got his wisdom teeth removed...kegger!",
    "Margherita Monday!", "Toga Tuesdays") are offered as reasons that work although they
    make no sense. Hormozi cites a Harvard experiment in which people were more likely to
    let someone cut in line if they simply gave a reason, and more likely still if the
    reason made sense. His own filled examples: Because...moms know best;
    Because...your country needs you; Because...it's my birthday, and I want you to
    celebrate with me.
  why: >-
    Good reasons work better than bad ones, but any reason works better than no reason, so
    he always includes one - the stuff you say after the word "because".
  demonstrates: >-
    Step 7: the reason why attached to a Call To Action.
  anchor: >-
    In fact, Harvard ran an experiment showing that people
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 2602–2633
  confirmations: 1
  anchor_at: "100m-leads.md:2608"
- id: C-leads-1-011
  type: case
  name: >-
    What a lead magnet does to the cost of a customer
  statement: >-
    Advertising the core offer directly: \$10,000 profit per sale, \$1000 of advertising
    to get someone on a call, closing one in three, so \$3000 of advertising per customer.
    Advertising a free lead magnet instead: it costs \$25 to deliver, engagement rises so
    a call costs \$75 of advertising, \$100 all in. One in ten lead magnet takers buys the
    core offer, so a customer costs \$1000 - a 3x cut in cost per customer, a 10:1 return,
    and triple the business on the same advertising budget.
  why: >-
    By delivering value before they buy you get ten times more engaged leads for the same
    cost, and the extra customers more than cover the delivery cost - so a lead magnet
    that costs money still lowers your cost to get a customer.
  demonstrates: >-
    Why a paid-for lead magnet beats a \$0 one, and why the goal is to print money rather
    than take your fair share.
  anchor: >-
    Let's say you make \$10,000 of profit on your core offer. And it costs
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 2637–2680
  confirmations: 1
  anchor_at: "100m-leads.md:2645"
- id: C-leads-1-012
  type: case
  name: >-
    The first six clients of The Free Training Project
  statement: >-
    The message sent by call, text and Facebook to people he already knew: does anyone
    want to get into shape, twelve weeks of training free, plus a custom nutrition plan
    and grocery list, in exchange for a donation to a charity of their choice and a
    testimonial. Six said yes - two high school friends, one college friend, three people
    they referred. After the twelve free weeks he asked them to pay him instead and none
    minded; their referrals, another five or six clients, were charged directly. The
    business settled at about \$4000 per month and replaced his job income.
  why: >-
    Warm reach outs are the cheapest and easiest way to find people interested in what you
    sell, and free customers convert into paying ones, send referrals and give
    testimonials - so you win either way.
  demonstrates: >-
    Warm outreach end to end: work your own contacts, make the first ones free, then start
    charging once people start referring.
  anchor: >-
    Hey, do you know anyone who's trying to get into shape? I\'m training
  source: >-
    100m-leads.md, #1 Warm Outreach, lines 2996–3047
  confirmations: 1
  anchor_at: "100m-leads.md:3003"
- id: C-leads-1-013
  type: case
  name: >-
    A-C-A worked on a mother of two
  statement: >-
    Acknowledge, restating what she said: "Two kids. And you're an accountant...".
    Compliment, tied to a character trait: "...Wow! Supermom! So hardworking! Managing a
    full-time career and two kids...". Ask, steering toward the offer - for therapy or
    life coaching, "Do you get time for yourself?"; for fitness or weight loss, "Do you
    have time to get workouts in?"; for cleaning services, "Do you have anyone who helps
    you keep the house tidy?".
  why: >-
    People love talking about themselves and love being complimented, and if they feel
    good talking to you they like and trust you more; the third move lets you lead the
    conversation wherever you want.
  demonstrates: >-
    The A-C-A framework for replying when a warm reach out gets a response; reused
    verbatim to qualify cold direct-message replies.
  anchor: >-
    Ex: ...Wow! Supermom! So hardworking! Managing a full-time
  source: >-
    100m-leads.md, #1 Warm Outreach, lines 3286–3322
  confirmations: 2
  anchor_at: "100m-leads.md:3300"
- id: C-leads-1-014
  type: case
  name: >-
    The do-you-know-anybody offer
  statement: >-
    Skeleton of the script, in order: ask whether they know anybody who is (struggle)
    looking to (dream outcome) in (time delay); say you are taking on five case studies
    for free because that is all you can handle and you want testimonials; state the
    dream outcome without the effort and sacrifice; add the guarantee that you work with
    people until they get it; give two named client results, one of them sharing the
    contact's own struggle; close with "Does anyone you like come to mind?" and, on a no,
    the joke "does anyone you hate come to mind?" to break the awkwardness. The compressed
    version when there is less room: I help (ideal customer) get (dream outcome) in (time
    period) without (effort and sacrifice) and (perceived likelihood of achievement).
  why: >-
    You are not asking them to buy anything, only whether they know anyone, so you do not
    come off as pushy - and of those who say yes, most turn out to be interested
    themselves; the whole thing is engineered to raise their perceived likelihood of
    achievement by showing people with struggles like theirs.
  demonstrates: >-
    The four elements of the value equation (dream outcome, perceived likelihood of
    achievement, time delay, effort and sacrifice) turned into a warm reach out offer.
  anchor: >-
    studies for free, because that's all I can handle. I just want to get
  source: >-
    100m-leads.md, #1 Warm Outreach, lines 3422–3477
  confirmations: 1
  anchor_at: "100m-leads.md:3426"
- id: C-leads-1-015
  type: case
  name: >-
    The free offer with three conditions
  statement: >-
    "Since I'm only taking on five people, I can give you all the attention you need to
    get brag-worthy results. And I'll give it all for free so long as you promise to: 1)
    Use it 2) Give me feedback and 3) Leave a killer review if you think it deserves one.
    Does that sound fair?"
  why: >-
    It sets reasonable expectations upfront; free is the easiest offer enhancer in the
    world, and you should not try to look advanced if you are not, because people are not
    dumb.
  demonstrates: >-
    Step 7 of warm outreach: make it easy for them to say yes by making it free, with the
    reciprocity spelled out.
  anchor: >-
    Since I'm only taking on five people, I can give you all the attention
  source: >-
    100m-leads.md, #1 Warm Outreach, lines 3502–3524
  confirmations: 1
  anchor_at: "100m-leads.md:3514"
- id: C-leads-1-016
  type: case
  name: >-
    Dean Jackson's 9-word email
  statement: >-
    Attributed to Dean Jackson. The whole message is one question - "Are you still looking
    to [4 word desire]?" - with no images, frills or links. Filled examples: buy your
    dream home, get more sales leads, tone up your arms, open an online store, start a
    YouTube channel. Whoever replies is an engaged lead, and those replies become the top
    priority for warm reach outs.
  why: >-
    The bare ask surfaces who is ready without anything else in the message; it is among
    the first things he does when he invests in a new business.
  applies_when: >-
    After you have given value to a list for a while, to probe it and see who wants more.
  demonstrates: >-
    Step 10 of warm outreach: keep your list warm and probe it with a give-then-ask.
  anchor: >-
    Are you still looking to \[4 word desire\]?
  source: >-
    100m-leads.md, #1 Warm Outreach, lines 3710–3762
  confirmations: 1
  anchor_at: "100m-leads.md:3724"
- id: C-leads-1-017
  type: case
  name: >-
    The \$104,000 warm outreach math
  statement: >-
    The benchmark chain: 100 warm reach outs get about 20 replies, about one in five of
    those take the free offer (four people), and about one of those four converts to a
    paid offer later - one customer per 100 reach outs. The money math on it: assuming 1%
    of the list buys a \$400 offer, 500 reach outs per week is 5 customers per week,
    \$2000 per week, \$104,000 per year on warm reach outs alone - about twice the median
    US household income at the time of writing (2023).
  why: >-
    The framework lets you predict how many customers you get per 100 reach outs; the
    numbers vary with the value of your offer and how much they trust you, but with enough
    volume you will get a customer, and the numbers improve as you do more.
  demonstrates: >-
    Warm outreach benchmarks and the volume rule behind them.
  anchor: >-
    This assumes 1% of your list buys a \$400 offer using
  source: >-
    100m-leads.md, #1 Warm Outreach, lines 3796–3843
  confirmations: 1
  anchor_at: "100m-leads.md:3824"
- id: C-leads-1-018
  type: case
  name: >-
    The influencer who counted posts
  statement: >-
    Leila paid \$120,000 for four calls with a big influencer. Call one: post regularly on
    every platform - twelve months later the audience had grown by more than 200,000. Call
    two, asked for the blueprint, the influencer went platform by platform instead: on
    Instagram "You've posted once today. I posted three times", on LinkedIn "You posted
    once this week. I posted five times today", and concluded "You just gotta do more
    bro." Over the next six months he put out ten times the content and added 1.2M people.
  why: >-
    Anyone claiming there is a secret is selling something; when he put out ten times the
    content his audience grew ten times as fast. Volume works, content works, and a growing
    audience is the result.
  demonstrates: >-
    That posting free content scales with output, not with a hidden technique.
  anchor: >-
    Instagram and pull up my Instagram\... Look. You've posted once today. I
  source: >-
    100m-leads.md, #2 Post Free Content Part I, lines 4096–4131
  confirmations: 1
  anchor_at: "100m-leads.md:4114"
- id: C-leads-1-019
  type: case
  name: >-
    A Far Past content unit - "I found you some time"
  statement: >-
    A personal lesson broken into the three components. Hook: he complained to a friend
    that he did not have enough time, while glued to his phone. Retain: the friend yanked
    the phone out of his hands and read the usage - three hours a day on social media.
    Reward: "Hey, I found you some time."
  why: >-
    It is a simple story others can relate to, which makes the topic interesting to more
    people, and it connects what he does - growing businesses - to a struggle many people
    have; the epiphany he gives away is what makes the lesson valuable to his audience.
  demonstrates: >-
    The content unit (hook, retain, reward) built out of a Far Past topic - the story
    without the scar.
  anchor: >-
    and looked at its usage. It showed I spent three hours
  source: >-
    100m-leads.md, #2 Post Free Content Part I, lines 4320–4343
  confirmations: 1
  anchor_at: "100m-leads.md:4330"
- id: C-leads-1-020
  type: case
  name: >-
    Hooks that fail to reward
  statement: >-
    A hook promising "7 Ways to Make Up with Your Spouse" fails if you give four ways, if
    the seven stink or have all been heard before, or if you are talking to a room of
    single guys. A hook promising "4 Marketing Strategies Dentists Can Use" fails if they
    cannot use them. In both, the audience will not watch again and certainly will not
    share it.
  why: >-
    How good content is depends on how often it rewards the audience in the time it takes
    to consume it; rewarding means matching or exceeding the expectation the hook set, and
    the audience decides, not you - you know you succeeded because your audience grows.
  demonstrates: >-
    The Reward component of the content unit: clearly satisfy the reason they started
    consuming.
  anchor: >-
    Example: If your hook promises "7 Ways to Make Up with Your Spouse" and
  source: >-
    100m-leads.md, #2 Post Free Content Part I, lines 4703–4738
  confirmations: 1
  anchor_at: "100m-leads.md:4703"
- id: C-leads-1-021
  type: case
  name: >-
    Give : ask ratios read off television and Facebook
  statement: >-
    Television averages 13 minutes of advertising per 60 minutes of air time - 47 minutes
    of giving to 13 of asking, roughly 3.5:1. Facebook shows roughly 4 content posts for
    every 1 ad in the newsfeed. These mature platforms care more about monetising than
    growing, so "give, give, give, ask" is read as the minimum sustainable ratio, the one
    that maximally monetises an audience without shrinking it. Growing platforms instead
    show lots of content with almost no advertisements, and they are the ones to model.
  why: >-
    The more you reward an audience the bigger it gets, so someone who wants to grow should
    give far more than they ask; the moment you start asking for money is the moment you
    decide to slow your growth.
  demonstrates: >-
    Mastering the give : ask ratio, and the case for "give until they ask".
  anchor: >-
    Thankfully, the give : ask ratio has been well-studied. Television
  source: >-
    100m-leads.md, #2 Post Free Content Part II, lines 4843–4914
  confirmations: 1
  anchor_at: "100m-leads.md:4843"
- id: C-leads-1-022
  type: case
  name: >-
    Three 30-second ads in an hour-long podcast, and the friend whose podcast shrank
  statement: >-
    An hour-long podcast carrying 3 x 30-second ads is 58.5 minutes of giving to 1.5
    minutes of asking, well above the 3:1 ratio, so the audience keeps growing while the
    asks run. Against it: a friend whose podcast blew up quickly monetised by making
    offers too frequently inside the content, and the podcast stopped growing and then
    shrank.
  why: >-
    You can advertise in every piece of content so long as the give : ask ratio stays
    high; over-give to protect the most valuable asset, the goodwill of your audience, and
    do not kill the golden goose.
  demonstrates: >-
    Integrated offers as one of the two ways to weave promotions into content.
  anchor: >-
    For example, if I make an hour-long podcast, having 3 x 30-second ads
  source: >-
    100m-leads.md, #2 Post Free Content Part II, lines 4954–4980
  confirmations: 1
  anchor_at: "100m-leads.md:4961"
- id: C-leads-1-023
  type: case
  name: >-
    The 11-more-tips ask
  statement: >-
    After a piece of content about getting more leads, the ask is: "I have 11 more tips
    that have helped me do this. Go to my site to grab a pretty visual of them." The
    thank-you page after the opt-in then displays the paid offer with a video explaining
    how it works. Bonus points if the lead magnet is relevant to the content advertising
    it.
  why: >-
    As long as the audience wants what the content was about, some of them will engage;
    when you are not sure whether to advertise the core offer or the lead magnet, the lead
    magnet is the lower-risk ask.
  demonstrates: >-
    How to ask from content: advertise either the core offer or the lead magnet, and
    nothing else.
  anchor: >-
    more leads on a post/video/podcast/etc., I would then say, "I have 11
  source: >-
    100m-leads.md, #2 Post Free Content Part II, lines 5005–5018
  confirmations: 1
  anchor_at: "100m-leads.md:5012"
- id: C-leads-1-024
  type: case
  name: >-
    Going for the jugular - the core offer ask to an audience
  statement: >-
    Skeleton of the post: I'm looking for 5 (specific avatar) to help achieve (dream
    outcome) in (time delay); the best part is you don't have to (effort and sacrifice);
    and if you don't get (dream outcome) I will do two things - hand you your money back
    and work with you until you do - because I want everyone to have an amazing experience
    and I'm confident I can deliver. It closes "If that sounds fair, DM me/book a
    call/comment below/reply to this email". Then get back to providing value.
  why: >-
    It is the offer from the warm outreach chapter, modelled for a public audience; the
    double guarantee is what raises perceived likelihood of achievement.
  demonstrates: >-
    The value equation reused for a public ask, the direct path to money.
  anchor: >-
    "I'm looking for 5 (specific avatar) to help achieve (dream outcome) in
  source: >-
    100m-leads.md, #2 Post Free Content Part II, lines 5022–5040
  confirmations: 1
  anchor_at: "100m-leads.md:5029"
- id: C-leads-1-025
  type: case
  name: >-
    Why the paid ads stopped working - the 78% survey
  statement: >-
    With paid advertising declining, the department meeting debated the creative, the
    copy, the offer, the pages, the sales process and the price. Leila asked a different
    question - what did we stop doing in the months before the decline - and the unanimous
    answer was that Alex had stopped making gym content and started talking about general
    business. He then surveyed gym owner clients: 78% had consumed at least two long form
    pieces of content before booking a call.
  why: >-
    He had given paid ads all the credit while free content was nurturing the demand; free
    content also warms the people moving to and from the cold methods, so even where it is
    hard to measure it improves the return on every other advertising method.
  demonstrates: >-
    Why to make content even when it is not your primary advertising strategy - and
    diagnosing a decline by what you stopped doing rather than by what you could change.
  anchor: >-
    78% of all clients had consumed at least TWO long form pieces of
  source: >-
    100m-leads.md, #2 Post Free Content Part II, lines 5200–5245
  confirmations: 1
  anchor_at: "100m-leads.md:5229"
- id: C-leads-1-026
  type: case
  name: >-
    How I instead of How to
  statement: >-
    Three rewritten pairs: "I make my oatmeal this way" against "you should make your
    oatmeal this way"; "How I Built My 7-Figure Agency" against "How To Build a 7-Figure
    Agency"; "My favorite way to generate leads for my business" against "This is the best
    way to generate leads for your business".
  why: >-
    When you talk about your own experience no one can question you, which makes you
    bulletproof; telling a stranger what to do is hard to do without coming off preachy or
    arrogant.
  applies_when: >-
    Especially when starting out.
  demonstrates: >-
    Lesson 1 of the seven content lessons: switch from "How to" to "How I", from "this is
    the best way" to "these are my favorite ways".
  anchor: >-
    my business vs. This is the best way to generate leads for your
  source: >-
    100m-leads.md, #2 Post Free Content Part II, lines 5253–5277
  confirmations: 1
  anchor_at: "100m-leads.md:5270"
- id: C-leads-1-027
  type: case
  name: >-
    One in five did not know about the book
  statement: >-
    He posts about his book every single day; he surveyed his audience asking whether they
    knew he had a book, and one in five of those who saw the post said they did not know.
  why: >-
    You are a silly goose if you think 100 percent of your audience listens 100 percent of
    the time - we need to be reminded more than we need to be taught, and you will get bored
    of your content before your whole audience even sees it.
  demonstrates: >-
    Lesson 2 of the seven content lessons: keep repeating yourself.
  anchor: >-
    surveyed my audience and asked them if they knew I had a book. One in
  source: >-
    100m-leads.md, #2 Post Free Content Part II, lines 5279–5286
  confirmations: 1
  anchor_at: "100m-leads.md:5283"
- id: C-leads-1-028
  type: case
  name: >-
    Puddles, Ponds, Lakes, Oceans - the plumber
  statement: >-
    A small local business should not start with general business content, because the
    audience will listen to people with better track records. Narrow to what you do and
    where you do it - plumbing in a certain town - and become king of that puddle. Then
    expand the plumbing puddle to the general local business pond, then the lake of brick
    and mortar chains, then eventually the ocean of general business.
  why: >-
    On a narrow topic your track record is the best one available, which is not true on the
    broad one.
  demonstrates: >-
    Lesson 3 of the seven content lessons: narrow the focus of your content, then widen it
    over time.
  anchor: >-
    you do and the place you do it. Example: plumbing in a certain town. If
  source: >-
    100m-leads.md, #2 Post Free Content Part II, lines 5289–5298
  confirmations: 1
  anchor_at: "100m-leads.md:5294"
- id: C-leads-1-029
  type: case
  name: >-
    Nine months before cold outreach paid
  statement: >-
    A salesman hired from a cold-outreach company promised profitability in twelve weeks
    and was given runway on the condition he figured out the software, the lists and
    everything else himself. What followed: September 0 sales; October 2 sales (\$32,000)
    and the team asking to pull the plug; December 4 sales (\$64,000) and the team asking
    again; January 6; February 10; March 14; April 20; May 30 sales (\$480,000). Today
    cold outreach generates millions per month.
  why: >-
    Cold outreach veterans had said it would take a year to scale and they were right - it
    took almost a year; proper expectations matter, and the two earlier attempts failed
    while the third, run by someone who had done it before and tracked every metric,
    worked.
  demonstrates: >-
    That cold outreach is a slow, volume-and-time channel - and why the metrics owner
    decides whether it survives the early months.
  anchor: >-
    October: 2 Sales (\$32,000 in revenue) Team asks me to pull the plug on
  source: >-
    100m-leads.md, #3 Cold Outreach, lines 5915–5999
  confirmations: 2
  anchor_at: "100m-leads.md:5923"
- id: C-leads-1-030
  type: case
  name: >-
    The dog trainer cold call
  statement: >-
    The call played out move by move: say the person's name and pause like a normal
    person; "it's Alex..." and pause; then the researched part - I watched a few of your
    videos and read your recent blog post on dog training, the peanut butter trick really
    helped with my doberman. Then the reason for calling - I work for a company that helps
    dog trainers fill up their books, we like to partner with the best in the area - and a
    neighbour as proof: "We worked with someone about an hour north from you...John's
    Doggy Daycare...heard of them?", who got 100 appointments in 30 days with text, email
    and some ads. Then a qualifying question, a light joke, and a booked time: "Will you be
    around at 4?". The contrast: opening with "hey man, wanna buy some marketing services?"
    gets you hung up on.
  why: >-
    Personalization - one to three pieces of information a friend might know, complimented
    and ideally shown to have benefited you - is what gets your foot in the door; people
    like people who like them, and even a stranger gives you more time if you know
    something about them.
  demonstrates: >-
    Problem #2 of cold outreach: personalize, so the cold reach out looks like a warm one.
  anchor: >-
    a few of your videos and read that recent blog post you wrote on dog
  source: >-
    100m-leads.md, #3 Cold Outreach, lines 6256–6312
  confirmations: 1
  anchor_at: "100m-leads.md:6267"
- id: C-leads-1-031
  type: case
  name: >-
    Swapping the game planning session for real free service
  statement: >-
    For the first four months of cold outreach the lead magnet was a "game planning
    session" - code for a sales call; some gyms took it, most did not. Many parts of the
    process were tested, but swapping the lead magnet to as much free service as they
    could possibly afford blew everything else out of the water: take rates tripled and
    cold outreach became a monster channel.
  why: >-
    Strangers give far less time to prove your worth and need more incentive to move
    toward you, so the goal is to demonstrate big value as fast as possible - give away
    something people actually pay for, not merely something good enough that they should.
  applies_when: >-
    When the offer or lead magnet is not working, up the ante until it is so good they feel
    stupid saying no.
  demonstrates: >-
    Problem #2 of cold outreach: big fast value.
  anchor: >-
    We swapped from "game planning" - code for "sales call" -
  source: >-
    100m-leads.md, #3 Cold Outreach, lines 6343–6376
  confirmations: 1
  anchor_at: "100m-leads.md:6355"
- id: C-leads-1-032
  type: case
  name: >-
    1000 hedge fund managers against tens of millions of dieters
  statement: >-
    If only 1000 hedge fund managers meet your criteria, personalize every one of them. If
    you are targeting women 25-45 trying to lose weight, there are tens of millions, so you
    can get away with less personalization - though personalizing still gets you more.
  why: >-
    You sacrifice personalization for scale, and personalized messages get a higher
    response rate, so the fewer leads you have the less automation you should use.
  demonstrates: >-
    Problem #3 of cold outreach: how far to automate delivery and distribution.
  anchor: >-
    For example, if there are only 1000 hedge fund managers who meet your
  source: >-
    100m-leads.md, #3 Cold Outreach, lines 6470–6480
  confirmations: 1
  anchor_at: "100m-leads.md:6476"
- id: C-leads-1-033
  type: case
  name: >-
    Cold call benchmark - one engaged lead per hour
  statement: >-
    100 cold calls a day at a twenty percent pick-up rate, with twenty-five percent of
    those taking the lead magnet, is four engaged leads; if the calls took four hours, that
    is one engaged lead per hour. You do it yourself at first, and hand it to someone else
    once the customers those leads convert into make more than a cold outreach rep costs
    - the bar being at least three times the lifetime profit of a customer against what it
    costs to get them (2023).
  why: >-
    Cold outreach is a numbers game: once you know how much outreach it takes to engage a
    lead, the only thing left to do is more.
  demonstrates: >-
    Cold outreach benchmarks on the phone, and the point at which you delegate the channel.
  anchor: >-
    Let's say I make 100 cold calls per day. And, let's say I get a twenty
  source: >-
    100m-leads.md, #3 Cold Outreach, lines 6659–6672
  confirmations: 1
  anchor_at: "100m-leads.md:6663"
- id: C-leads-1-034
  type: case
  name: >-
    Cold email benchmark - shoot for 3%
  statement: >-
    100 personalized emails a day, thirty percent open, ten percent of those reply showing
    interest: three engaged leads, 30% x 10% = 3%. The target given is 3% of the list
    turning into engaged leads. A new campaign for a very niche high ticket service
    business in the portfolio showed a 4% engagement rate, and with about a third
    converting that is one new customer per hundred outreach attempts (2023).
  why: >-
    The numbers vary by platform, but the ratio is what you steer the channel by.
  demonstrates: >-
    Cold outreach benchmarks by email.
  anchor: >-
    Let's say you send 100 personalized emails per day. From there, thirty
  source: >-
    100m-leads.md, #3 Cold Outreach, lines 6676–6688
  confirmations: 1
  anchor_at: "100m-leads.md:6680"
- id: C-leads-1-035
  type: case
  name: >-
    Direct message benchmark - a hundred personal videos
  statement: >-
    A personal video or voice memo recorded for a hundred people, each one saying their
    name and adding one personal line before the standard message, gets about twenty
    percent replying - twenty engaged leads - who are then qualified for a call with the
    same A-C-A format from the warm outreach section. The same bar applies, cost of
    outreach under a third of the profit from a customer, and it is called the bare
    minimum: the portfolio company cited gets over 30:1 from its outreach (2023).
  why: >-
    A name and one personal line in front of an otherwise standard message are what lift
    the reply rate; three times is a floor, not a target.
  demonstrates: >-
    Cold outreach benchmarks by direct message, and the reuse of A-C-A on cold replies.
  anchor: >-
    Let's say I make a personal video or record a personal voice memo for
  source: >-
    100m-leads.md, #3 Cold Outreach, lines 6697–6710
  confirmations: 1
  anchor_at: "100m-leads.md:6701"
- id: C-leads-1-036
  type: case
  name: >-
    The cost model of a cold calling team
  statement: >-
    Reps paid \$15 per hour plus \$50 per shown appointment; \$3600 profit per sale; leads
    at ten cents; 200 leads called per day giving about two shows per rep. An eight-hour
    day costs \$120 in labour, \$100 in show commissions and \$20 for the leads - \$240 for
    two shows, \$120 per show. Closing 33% of shows puts the cost of a client, excluding
    commissions, at \$360 against \$3600 profit: a 10:1 return. Then you just add bodies
    (2023).
  why: >-
    Cold outreach is labour intensive and nearly all its cost is labour, so the return is
    computed by adding up labour and software across the three steps; it is boring and
    tedious, but brutally effective.
  demonstrates: >-
    How to calculate the return on a cold outreach channel.
  anchor: >-
    If they worked eight hours per day, we would pay \$120 in labor and
  source: >-
    100m-leads.md, #3 Cold Outreach, lines 6716–6759
  confirmations: 1
  anchor_at: "100m-leads.md:6743"
- id: C-leads-1-037
  type: case
  name: >-
    Solving for X - three people sending emails
  statement: >-
    If every 100 emails gets one customer and you want 100 customers, you need to send
    10,000 emails, which is 333 per day; one person can send 111 emails a day, so you need
    three people sending emails every day.
  why: >-
    Cold outreach is incredibly reliable - a certain amount of input creates a certain
    number of responses, so you can reverse engineer the sales you want back to the inputs
    at the top of the lead pathway and then simply solve for X.
  demonstrates: >-
    The reliability benefit of cold outreach: to get more, do more.
  anchor: >-
    Ex: Let's say for every 100 emails, I get one customer. If I want 100
  source: >-
    100m-leads.md, #3 Cold Outreach, lines 6795–6808
  confirmations: 1
  anchor_at: "100m-leads.md:6805"
```
