# Улов фазы 1 — $100M Leads (2023), chapters up to #3 Cold Outreach (lines 1–6900) (ярус 1), тип A: фреймворки

Группа `tier1-leads-1`, слаг `leads-1`, ярус 1. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **32** (экстрактор вернул 32, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-leads.md` | 1–6900 | 6 | 32 |

## Как собран файл

Экстрактор A (Frameworks) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier1-leads-1.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier1-leads-1-A.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: A-leads-1-001
  type: framework
  name: >-
    The two ways to grow a business
  statement: >-
    A business can be grown in only two ways: get more customers, or make them worth more; this book works on the first one.
  why: >-
    The author grows every company in his portfolio with this exact framework, so any growth work has to fall into one of the two boxes.
  applies_when: >-
    Deciding where growth effort goes before choosing any tactic.
  structure:
    - >-
      1) Get more customers
    - >-
      2) Make them worth more
  anchor: >-
    I grow our portfolio companies with this exact framework.
  source: >-
    100m-leads.md, The Problem This Book Solves, lines 1205–1217
  confirmations: 1
  anchor_at: "100m-leads.md:1216"
- id: A-leads-1-002
  type: framework
  name: >-
    More, better, cheaper leads, reliably
  statement: >-
    You get more customers by getting more leads, better leads, cheaper leads, and getting them reliably, that is from lots of places.
  why: >-
    All else being equal, when you double your leads, you double your business.
  applies_when: >-
    Judging whether a lead source is doing its job; the four criteria are the targets of the whole book.
  structure:
    - >-
      1) More Leads
    - >-
      2) Better Leads
    - >-
      3) Cheaper Leads
    - >-
      4) Reliably (think 'from lots of places').
  anchor: >-
    more customers. You get more customers by getting:
  source: >-
    100m-leads.md, The Problem This Book Solves, lines 1217–1239
  confirmations: 1
  anchor_at: "100m-leads.md:1218"
- id: A-leads-1-003
  type: framework
  name: >-
    Seven Steps To Creating an Effective Lead Magnet
  statement: >-
    A lead magnet is built in seven ordered steps, from picking the narrow problem and the person it is solved for, through naming, packaging and quality, to the call to action that lets them say they want more.
  why: >-
    Good lead magnets get more engaged leads and customers than a core offer alone, and do it for less money.
  applies_when: >-
    When people want to know more about your offer before they buy, which is common for businesses that sell more expensive stuff; the author says to try advertising the core offer first.
  structure:
    - >-
      Step 1: Figure out the problem you want to solve and who to solve it for
    - >-
      Step 2: Figure out how to solve it
    - >-
      Step 3: Figure out how to deliver it
    - >-
      Step 4: Test what to name it
    - >-
      Step 5: Make it easy to consume
    - >-
      Step 6: Make it darn good
    - >-
      Step 7: Make it easy for them to tell you they want more
  anchor: >-
    Seven Steps To Creating an Effective Lead Magnet
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 1903–1932
  confirmations: 2
  anchor_at: "100m-leads.md:1903"
- id: A-leads-1-004
  type: framework
  name: >-
    The Problem-Solution cycle
  statement: >-
    Pick a problem that is narrow and meaningful, solve it with the lead magnet, and check that the new problem this reveals is the one your core offer solves in exchange for money.
  why: >-
    Every problem has a solution and every solution reveals more problems, so the free solution hands the lead straight to the paid one.
  applies_when: >-
    Step 1 of building a lead magnet, picking which problem to solve.
  structure:
    - >-
      Every problem has a solution.
    - >-
      Every solution reveals more problems.
    - >-
      smaller problem-solution cycles sit inside larger problem-solution cycles
  anchor: >-
    figure this out. I call it the Problem-Solution cycle. You can see it
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 1965–1988
  confirmations: 1
  anchor_at: "100m-leads.md:1966"
- id: A-leads-1-005
  type: framework
  name: >-
    The three types of lead magnets
  statement: >-
    A lead magnet solves its narrow problem in one of three ways: it reveals the problem, gives a sample or trial, or gives one step of a multi-step process.
  why: >-
    All three solve one problem and reveal others, which is what moves the lead toward the core offer.
  applies_when: >-
    Reveal Their Problem works great when the problems get worse the longer you wait; Samples And Trials when your core offer is a recurring solution to a recurring problem; One Step Of A Multi-Step Process when your core offer solves a more complex problem.
  structure:
    - >-
      1) Reveal Their Problem. Think "diagnosis."
    - >-
      2) Samples And Trials. You give full but brief access to your core offer.
    - >-
      3) One Step Of A Multi-Step Process. When your core offer has steps, you can give one valuable step for free and the rest when they buy.
  anchor: >-
    So your three types are: 1) Reveal Problems, 2) Samples and Trials, and
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 2016–2131
  confirmations: 1
  anchor_at: "100m-leads.md:2030"
- id: A-leads-1-006
  type: framework
  name: >-
    Four ways to deliver a lead magnet
  statement: >-
    The author's favourite lead magnets are delivered as software, information, services, or physical products.
  why: >-
    With three different types of lead magnets and four ways to deliver them, that is up to twelve lead magnets that solve a single narrow problem; the author makes as many versions as he can and rotates them, which keeps advertising fresh and shows which ones work best.
  applies_when: >-
    Step 3 of building a lead magnet, and again at Step 5 where each delivery form has its own way of being made easy to consume.
  structure:
    - >-
      1) Software: You give them a tool
    - >-
      2) Information: You teach them something
    - >-
      3) Services: You do work for free
    - >-
      4) Physical Products: You give them something they can hold in their hands
  anchor: >-
    magnets solve them with: software, information, services, and physical
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 2132–2211
  confirmations: 2
  anchor_at: "100m-leads.md:2141"
- id: A-leads-1-007
  type: framework
  name: >-
    The three things to test, in that order
  statement: >-
    Test the headline first, then the image or images, then the subheadline.
  why: >-
    Five times more people read your headline than any other part of your promotion, and improving the headline, name, and display of your lead magnet can 2x, 3x, or 10x your engagement.
  applies_when: >-
    Step 4 of building a lead magnet, naming and packaging it; if you only test one thing, test the headline.
  structure:
    - >-
      the headline
    - >-
      the image(s)
    - >-
      the subheadline
  anchor: >-
    and the subheadline, in that order. The headline is the most important.
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 2212–2381
  confirmations: 1
  anchor_at: "100m-leads.md:2237"
- id: A-leads-1-008
  type: framework
  name: >-
    Good CTAs have two things
  statement: >-
    A call to action says what to do, in clear, simple and direct language, and gives reasons to do it right now.
  why: >-
    If you give people a reason to take action, more people will do it.
  applies_when: >-
    Step 7 of the lead magnet, and every ask made in any of the core four.
  structure:
    - >-
      1) what to do
    - >-
      2) reasons to do it right now
  anchor: >-
    Good CTAs have two things: 1) what to do and 2)
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 2496–2633
  confirmations: 1
  anchor_at: "100m-leads.md:2505"
- id: A-leads-1-009
  type: framework
  name: >-
    My favorite reasons to act now
  statement: >-
    The reasons attached to a call to action are scarcity, urgency, and a made-up reason, and the author includes as many effective ones as he can.
  why: >-
    Good reasons work better than bad reasons, and any reason, even a bad one, tends to work better than no reason at all.
  applies_when: >-
    Writing the second half of a CTA, the part that makes people act right now.
  structure:
    - >-
      a) Scarcity - Scarcity is when there is a limited amount of something.
    - >-
      b) Urgency. Urgency is when people act faster because they have a short amount of time.
    - >-
      c) Fraternity Party Planner (my favorite) - Make Up A Reason.
  anchor: >-
    Here are my favorite reasons to act now:
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 2521–2633
  confirmations: 1
  authors_caveat: >-
    The best strategy the author knows for scarcity is reality: advertise the limit your business actually has, which gives ethical scarcity; the fewer you have, the fewer engaged leads you can get before running out.
  anchor_at: "100m-leads.md:2526"
- id: A-leads-1-010
  type: framework
  name: >-
    A good lead magnet does four things
  statement: >-
    A lead magnet is judged on four things: it engages ideal customers when they see it, gets more people to engage than the core offer alone, is valuable enough that they consume it, and makes the right people more likely to buy.
  why: >-
    Those four together are what makes more people show interest, makes more money from them, and delivers more value, all at the same time.
  applies_when: >-
    Checking a finished lead magnet before advertising it.
  structure:
    - >-
      1) Engages ideal customers when they see it.
    - >-
      2) Gets more people to engage than your core offer alone
    - >-
      3) Is valuable enough that they consume it.
    - >-
      4) Makes the right people more likely to buy
  anchor: >-
    And a good lead magnet does four things:
  source: >-
    100m-leads.md, Section II Conclusion, lines 2725–2756
  confirmations: 1
  anchor_at: "100m-leads.md:2733"
- id: A-leads-1-011
  type: framework
  name: >-
    The core four
  statement: >-
    Crossing warm and cold audiences with one-to-one and one-to-many communication gives the only four ways to let anyone know about anything: warm outreach, posting content, cold outreach, paid ads.
  why: >-
    These are the only four things you can do to let other people know about the stuff you sell, so if you are not getting as many leads as you want, you are not doing the core four with enough skill or with enough volume.
  applies_when: >-
    Any time lead flow has to be increased; the author refers to the core four throughout the rest of the book.
  structure:
    - >-
      1-to-1 to a Warm Audience = Warm Outreach
    - >-
      1-to-many to a Warm Audience = Posting Content
    - >-
      1-to-1 to a Cold Audience = Cold Outreach
    - >-
      1-to-many to a Cold Audience = Paid Ads
  anchor: >-
    the only four ways we can let anyone know about anything: the core four.
  source: >-
    100m-leads.md, Section III: Get Leads, lines 2786–2913
  confirmations: 2
  anchor_at: "100m-leads.md:2877"
- id: A-leads-1-012
  type: framework
  name: >-
    The two things you advertise
  statement: >-
    Whatever the method, you advertise one of two things: your lead magnet, something free and valuable, or your core offer, the main thing you sell.
  why: >-
    Advertising the core offer is the direct path to money and should be tried first; the lead magnet gets more people to engage and is the lower risk choice when you are unsure.
  applies_when: >-
    Every one of the core four: warm reach outs, asks made to a content audience, and cold outreach.
  structure:
    - >-
      your lead magnet (something free and valuable)
    - >-
      your core offer (the main thing you sell)
  anchor: >-
    advertise one of two things. You let them know about your lead magnet
  source: >-
    100m-leads.md, #1 Warm Outreach, lines 3092–3096
  confirmations: 3
  anchor_at: "100m-leads.md:3094"
- id: A-leads-1-013
  type: framework
  name: >-
    How To Do Warm Reach Outs in 10 Steps
  statement: >-
    Warm outreach runs as ten ordered steps, from assembling the list of everyone who has given you permission to contact them, through the free offer and the switch to charging, to keeping the list warm.
  why: >-
    It is the cheapest and easiest way to find people interested in the stuff you sell, and because everything is done by hand and personal, it is reliable.
  applies_when: >-
    Getting the first five clients for any new product or service; advanced folks use it for re-engagement and new product lines.
  structure:
    - >-
      Step 1: Get your list
    - >-
      Step 2: Pick a platform
    - >-
      Step 3: Personalize your message
    - >-
      Step 4: Reach out
    - >-
      Step 5: Warm them up
    - >-
      Step 6: Invite their friends
    - >-
      Step 7: Make them the easiest offer in the world
    - >-
      Step 8: Start at the top
    - >-
      Step 9: Start Charging
    - >-
      Step 10: Keep Your List Warm
  anchor: >-
    How To Do Warm Reach Outs in 10 Steps
  source: >-
    100m-leads.md, #1 Warm Outreach, lines 3117–3769
  confirmations: 1
  authors_caveat: >-
    Warm reach outs have two limitations: the time they take, and the number of people who know you, which you will eventually run out of.
  anchor_at: "100m-leads.md:3117"
- id: A-leads-1-014
  type: framework
  name: >-
    The A-C-A framework
  statement: >-
    When a contact replies, acknowledge what they said in your own words, compliment them and tie it to a positive character trait, then ask another question that leads the conversation toward your offer.
  why: >-
    People love talking about themselves and love being complimented, and if people feel good when talking to you, they will like and trust you more.
  applies_when: >-
    Step 5 of warm reach outs, replying when a contact responds; the same A-C-A format is used to qualify cold direct message replies for a call.
  structure:
    - >-
      Acknowledge what they said. Restate it in your own words. This shows active listening.
    - >-
      Compliment them on whatever they tell you. Tie it to a positive character trait if you can.
    - >-
      Ask another question. Lead the conversation in whatever direction you want.
  anchor: >-
    [ACA]{.calibre11}[ framework is great because it helps
  source: >-
    100m-leads.md, #1 Warm Outreach, lines 3286–3322
  confirmations: 2
  anchor_at: "100m-leads.md:3317"
- id: A-leads-1-015
  type: framework
  name: >-
    The value equation
  statement: >-
    Value has four elements: dream outcome, perceived likelihood of achievement, time delay, effort and sacrifice; the goal is to maximize the first two and minimize the second two.
  why: >-
    Doing that shows someone you have exactly what they want, that they are guaranteed to get it, insanely fast, and without lifting a finger or giving up anything they love.
  applies_when: >-
    Making an offer from scratch, in a warm reach out and in an ask made to a content audience.
  structure:
    - >-
      1) Dream Outcome: what the person wants to happen, the way they want it to happen
    - >-
      2) Perceived Likelihood of Achievement: how likely they think it is for them to achieve their goal
    - >-
      3) Time Delay: how long they believe it'll take to get results after they buy
    - >-
      4) Effort and Sacrifice: The bad stuff they'll have to endure and the good stuff they'll have to give up in their struggle to get the result.
  anchor: >-
    When I make an offer from scratch, I refer to the value equation.
  source: >-
    100m-leads.md, #1 Warm Outreach, lines 3352–3416
  confirmations: 2
  authors_caveat: >-
    The author states the equation was the core concept of his first book, $100M Offers, and restates the four elements here; he warns to get as close to the ideal as you can without lying or exaggerating.
  anchor_at: "100m-leads.md:3352"
- id: A-leads-1-016
  type: framework
  name: >-
    The value elements back to back
  statement: >-
    When there is little time or space, the offer is delivered as one sentence with five slots: who you help, the dream outcome, the time period, the effort and sacrifice they avoid, and something that raises perceived likelihood of achievement.
  why: >-
    It is the value equation compressed, so the four elements still land when there is no room for the full offer.
  applies_when: >-
    Emails, texts, direct messages, calls, and in-person; just fill in the blanks.
  structure:
    - >-
      I help (ideal customer)
    - >-
      get (dream outcome)
    - >-
      in (time period)
    - >-
      without (effort and sacrifice)
    - >-
      and (increase perceived likelihood of achievement)
  anchor: >-
    If you have even less time or space to deliver it, just use the value
  source: >-
    100m-leads.md, #1 Warm Outreach, lines 3463–3477
  confirmations: 2
  anchor_at: "100m-leads.md:3463"
- id: A-leads-1-017
  type: framework
  name: >-
    The content unit
  statement: >-
    All audience-growing content hooks attention, retains it, and rewards it; the smallest amount of material that does all three is a content unit, and longer content is made by linking content units together.
  why: >-
    A person can only be rewarded by content if they have a reason to consume it, pay attention long enough, and get that reason satisfied, so those three outcomes reverse into the three things you have to do.
  applies_when: >-
    Making any piece of content on any platform, short or long form.
  structure:
    - >-
      a) Hook attention: get them to notice your content.
    - >-
      b) Retain attention: get them to consume it.
    - >-
      c) Reward attention: satisfy the reason they consumed it to begin with.
  anchor: >-
    The smallest amount of material it takes to hook, retain and reward
  source: >-
    100m-leads.md, #2 Post Free Content Part I, lines 4214–4262
  confirmations: 2
  authors_caveat: >-
    The author separates the three so they can be discussed clearly, but they can all happen at once, which is how a short tweet, a meme image or a jingle goes viral.
  anchor_at: "100m-leads.md:4256"
- id: A-leads-1-018
  type: framework
  name: >-
    The three parts of the hook
  statement: >-
    You raise the share of people who pick your content by picking topics they find interesting, headlines that give them a reason, and matching the format of other stuff they like.
  why: >-
    This is a competition for attention: you have to beat every alternative they have to win theirs, and content that does not look like what they expect will reward them loses to better-looking content before it gets a chance.
  applies_when: >-
    The hook step of any content unit.
  structure:
    - >-
      topics they find interesting
    - >-
      headlines that give them a reason
    - >-
      matching the format of other stuff they like
  anchor: >-
    We increase the percentage of people who pick our content by picking
  source: >-
    100m-leads.md, #2 Post Free Content Part I, lines 4296–4547
  confirmations: 1
  anchor_at: "100m-leads.md:4296"
- id: A-leads-1-019
  type: framework
  name: >-
    Five categories of topics
  statement: >-
    Content topics are drawn from five categories of your own experience: far past, recent past, present, trending, and manufactured.
  why: >-
    There is only one of you, so the easiest way to differentiate is to say something no one else can say, because no one else has lived your life.
  applies_when: >-
    Choosing what to make content about, the topics part of the hook.
  structure:
    - >-
      a) Far Past: The important past lessons in your life. Connect that wisdom to your product or service.
    - >-
      b) Recent Past: Do stuff, then talk about what you did (or what happened).
    - >-
      c) Present: Write down ideas at the exact time they come to you.
    - >-
      d) Trending: Go where the attention is.
    - >-
      e) Manufactured: Turn your ideas into reality. Pick a topic people find interesting. Then, learn about it, make it, or do it.
  anchor: >-
    topics into five categories: Far Past, Recent Past, Present, Trending,
  source: >-
    100m-leads.md, #2 Post Free Content Part I, lines 4304–4414
  confirmations: 1
  authors_caveat: >-
    Manufactured costs the most time and effort, since you have to create the experience rather than talk about one you already had, but it can have the biggest payouts.
  anchor_at: "100m-leads.md:4308"
- id: A-leads-1-020
  type: framework
  name: >-
    Seven headline components
  statement: >-
    Headlines are built from seven components that drove the most interest in news stories: recency, relevancy, celebrity, proximity, conflict, unusual, ongoing.
  why: >-
    A meta-analysis of news revealed these as the components that drove the most interest, and the headline is what the audience uses to weigh whether your content will reward them.
  applies_when: >-
    Writing a headline; try to include at least two of the components.
  structure:
    - >-
      Recency - As recent as possible, quite literally the 'new's
    - >-
      Relevancy - Personally meaningful
    - >-
      Celebrity - Including prominent people (celebrities, authorities, etc.).
    - >-
      Proximity - Close to home -- geographically
    - >-
      Conflict - of opposing ideas, opposing people, nature, etc.
    - >-
      Unusual - odd, unique, rare, bizarre
    - >-
      Ongoing - Stories still in progress are dynamic, evolving, and have plot twists.
  anchor: >-
    A meta-analysis of news revealed headline components that drove the
  source: >-
    100m-leads.md, #2 Post Free Content Part I, lines 4428–4499
  confirmations: 1
  anchor_at: "100m-leads.md:4441"
- id: A-leads-1-021
  type: framework
  name: >-
    Lists, steps, and stories
  statement: >-
    Attention is retained by embedding unresolved questions in the audience's mind, and the three ways to do it are lists, steps, and stories, used alone or interwoven.
  why: >-
    The author's favourite driver of retention is curiosity: people want to know what happens next, and if done correctly they will wait years.
  applies_when: >-
    The retain step of a content unit, on any platform and any length.
  structure:
    - >-
      a) Lists: Lists are things, facts, tips, opinions, ideas, etc. presented one after the other.
    - >-
      b) Steps: Steps are actions that occur in order and accomplish a goal when completed.
    - >-
      c) Stories: Stories describe events, real or imaginary.
  anchor: >-
    favorite ways to embed questions are: lists, steps, and
  source: >-
    100m-leads.md, #2 Post Free Content Part I, lines 4553–4663
  confirmations: 1
  authors_caveat: >-
    Steps are actions that must be done in a specific order to get a result, so they are less flexible but have a more explicit reward; lists can have anything on them in any order, so they are more flexible but have a less explicit reward.
  anchor_at: "100m-leads.md:4571"
- id: A-leads-1-022
  type: framework
  name: >-
    Integrated and intermittent offers
  statement: >-
    There are two strategies for weaving promotions into content: integrate an ask into every piece while keeping the give to ask ratio high, or make many pure give pieces and occasionally make an ask piece.
  why: >-
    Asks are commercials that cost you trust and growth, so the strategy has to keep the give to ask ratio high enough that the audience keeps growing.
  applies_when: >-
    The difference depends on the platform: on short platforms the intermittent way will dominate, on long-form platforms integrations are often your best bet.
  structure:
    - >-
      Integrated: You can advertise in every piece of content so long as you keep your give : ask ratio high.
    - >-
      Intermittent: You make many pieces of content of pure 'gives' then occasionally make an 'ask' piece.
  anchor: >-
    Now, I use two strategies to weave promotions into content:
  source: >-
    100m-leads.md, #2 Post Free Content Part II, lines 4939–5053
  confirmations: 1
  authors_caveat: >-
    The author's own recommendation is the give until they ask strategy; asking too frequently inside the content made a friend's podcast stop growing and then shrink.
  anchor_at: "100m-leads.md:4945"
- id: A-leads-1-023
  type: framework
  name: >-
    Two opposing strategies to scale your warm audience
  statement: >-
    An audience is scaled either depth then width, maximizing one platform before moving to the next, or width then depth, getting on every platform early and maximizing them together; both are right.
  why: >-
    Both follow progressive steps and each buys a different advantage, compounding on one platform versus faster reach and repurposed content.
  applies_when: >-
    Once you are posting content regularly and want more of it.
  structure:
    - >-
      Depth then width: Maximize a platform, then move onto the next platform.
    - >-
      Width then depth: Get on every platform early, then maximize them together.
  anchor: >-
    There are two opposing strategies to scale your warm audience.
  source: >-
    100m-leads.md, #2 Post Free Content Part II, lines 5071–5185
  confirmations: 1
  anchor_at: "100m-leads.md:5071"
- id: A-leads-1-024
  type: framework
  name: >-
    Depth then width
  statement: >-
    Post on a relevant platform, post regularly, maximize quality and quantity there, then add another platform while holding the first, and repeat until all relevant platforms are maximized.
  why: >-
    Once you figure out one platform you maximize your return on that effort, audiences compound faster the more you do, and fewer resources are required to make it work.
  applies_when: >-
    Scaling content when resources are limited.
  structure:
    - >-
      Step #1: Post content on a relevant platform.
    - >-
      Step #2: Post content regularly on that platform.
    - >-
      Step #3: Maximize quality and quantity of the content on that platform.
    - >-
      Step #4: Add another platform while maintaining the quality and quantity on the first platform.
    - >-
      Step #5: Repeat steps 1-4 until all relevant platforms are maximized.
  anchor: >-
    Depth then width:]{.calibre66}[ Maximize a platform, then move onto the
  source: >-
    100m-leads.md, #2 Post Free Content Part II, lines 5078–5122
  confirmations: 1
  authors_caveat: >-
    You do not accomplish the feeling of omnipresence, and in the beginning you risk your business being reliant on a single channel, which can kill it if the platform shuts you down.
  anchor_at: "100m-leads.md:5078"
- id: A-leads-1-025
  type: framework
  name: >-
    Width then depth
  statement: >-
    Post on a relevant platform, post regularly, then move onto the next relevant platform while maintaining the previous, continue until you are on all relevant platforms, and only then maximize content creation on all of them at once.
  why: >-
    You reach a broader audience faster and you can repurpose content, so with a little extra work and minimal changes to the format the same content fits multiple platforms.
  applies_when: >-
    Scaling content when you can afford the extra labor, attention and time.
  structure:
    - >-
      Step #1: Post content on a relevant platform.
    - >-
      Step #2: Post content regularly on that platform.
    - >-
      Step #3: Instead of maximizing your first platform. Move onto the next relevant platform while maintaining the previous.
    - >-
      Step #4: Continue until you are on all relevant platforms.
    - >-
      Step #5: Now, maximize your content creation on all platforms at once.
  anchor: >-
    Width then depth]{.calibre66}[:]{.calibre11}[ Get on every platform
  source: >-
    100m-leads.md, #2 Post Free Content Part II, lines 5126–5168
  confirmations: 1
  authors_caveat: >-
    It costs more labor, attention, and time to do well, and oftentimes people end up with lots of bad content everywhere.
  anchor_at: "100m-leads.md:5126"
- id: A-leads-1-026
  type: framework
  name: >-
    7 Lessons I've Learned From Making Content
  statement: >-
    The author's seven lessons from making content: speak from your own experience, repeat yourself, narrow your pond, turn hits into sales tools, keep free content good for paying customers, stop blaming attention spans, and press submit yourself.
  why: >-
    Each lesson removes a mistake the author made himself while building his own audience.
  applies_when: >-
    Reviewing your own content practice once you are posting regularly.
  structure:
    - >-
      1) Switch from "How to" to "How I." From "This is the best way" to "These are my favorite ways" etc.
    - >-
      2) We Need To Be Reminded More Than We Need To Be Taught
    - >-
      3) Puddles, Ponds, Lakes, Oceans.
    - >-
      4) Content Creates Tools For Salespeople
    - >-
      5) Free Content Retains Paying Customers
    - >-
      6) People don't have shorter attention spans, they have higher standards.
    - >-
      7) Avoid Pre-Scheduling Posts
  anchor: >-
    7 Lessons I've Learned From Making Content
  source: >-
    100m-leads.md, #2 Post Free Content Part II, lines 5249–5345
  confirmations: 1
  anchor_at: "100m-leads.md:5249"
- id: A-leads-1-027
  type: framework
  name: >-
    What I measure: how big and how fast
  statement: >-
    Audience is measured monthly on two things: total followers and reach, which is how big, and the rate of getting followers and reach, which is how fast.
  why: >-
    We can only control inputs, so measuring outputs is only useful if we are consistent with inputs; measuring both absolute and relative growth also gives more ways to see progress.
  applies_when: >-
    Benchmarking the posting content method month over month.
  structure:
    - >-
      1) Total followers and reach - How big
    - >-
      2) Rate of getting followers and reach - How fast
  anchor: >-
    So I like to measure my audience
  source: >-
    100m-leads.md, #2 Post Free Content Part II, lines 5349–5396
  confirmations: 1
  anchor_at: "100m-leads.md:5353"
- id: A-leads-1-028
  type: framework
  name: >-
    Three problems strangers create
  statement: >-
    Compared to people who know you, strangers present three new problems: you have no way to contact them, if you can contact them they ignore you, and if they give you their attention they are not interested.
  why: >-
    Cold outreach has one key difference from warm outreach, trust: strangers do not trust you.
  applies_when: >-
    Starting cold outreach, which sits on the foundation of warm outreach.
  structure:
    - >-
      First, you don't have a way to contact them. Duh.
    - >-
      Second, even if you can contact them, they ignore you.
    - >-
      Third, even if they give you their attention, they're not interested.
  anchor: >-
    And compared to people who know us, strangers present
  source: >-
    100m-leads.md, #3 Cold Outreach, lines 6038–6057
  confirmations: 1
  anchor_at: "100m-leads.md:6043"
- id: A-leads-1-029
  type: framework
  name: >-
    The order we solve these problems
  statement: >-
    Cold outreach is done in three steps, one per problem: get a way to contact them, figure out what to say, then contact them until they are ready and able to listen.
  why: >-
    Cold outreach is a numbers game: once you figure out how much outreach it takes to engage a lead, the only thing left to do is more.
  applies_when: >-
    Building a cold outreach channel; the chapter is divided into one step per problem.
  structure:
    - >-
      1) Get a way to contact them
    - >-
      2) Figure out what to say
    - >-
      3) Contact them until they're ready and able to listen
  anchor: >-
    Now that we got that out of the way, the order we solve these problems
  source: >-
    100m-leads.md, #3 Cold Outreach, lines 6098–6135
  confirmations: 2
  anchor_at: "100m-leads.md:6098"
- id: A-leads-1-030
  type: framework
  name: >-
    Three ways to get a targeted lead list
  statement: >-
    Targeted lead lists come from three sources tried in order: scraping software, list brokers, and assembling the list yourself by joining groups and communities.
  why: >-
    The author works from the most accessible leads to the least accessible; if you can search the database so can everyone else, but a list you assemble yourself holds people who are less likely to have had many cold reach outs already, so they are the freshest.
  applies_when: >-
    Problem 1 of cold outreach, building the first 1000 names; if you have more time than money, start at step three since it only costs time.
  structure:
    - >-
      Step #1 Softwares: I subscribe to as many softwares as I can that scrape leads from different sources.
    - >-
      Step #2 Brokers: I go to multiple list brokers and ask them to make me a list based on my audience criteria.
    - >-
      Step #3 Elbow Grease: I join groups and communities that I think have my audience.
  anchor: >-
    There are three different ways I get my targeted lead lists.
  source: >-
    100m-leads.md, #3 Cold Outreach, lines 6141–6221
  confirmations: 1
  authors_caveat: >-
    Each step is tested on a representative sample first, a few hundred leads per software or a sample list per broker, and only kept if the contact information is current and the leads are responsive.
  anchor_at: "100m-leads.md:6169"
- id: A-leads-1-031
  type: framework
  name: >-
    Personalize, Then Give Big Fast Value
  statement: >-
    What you say to a stranger has two factors: personalization, so the cold reach out looks like a warm one, and big fast value, an offer or lead magnet good enough to blow their minds in under thirty seconds.
  why: >-
    They don't know us and they don't trust us, and we have to overcome both issues in a matter of seconds.
  applies_when: >-
    Problem 2 of cold outreach, writing the script or message.
  structure:
    - >-
      a) They Don't Know Us→Personalize (Act Like You Know Them).
    - >-
      b) They Don't Trust Us→Big Fast Value.
  anchor: >-
    two important factors I emphasize to get strangers to engage:
  source: >-
    100m-leads.md, #3 Cold Outreach, lines 6228–6389
  confirmations: 1
  authors_caveat: >-
    Personalization is one to three pieces of information a friend might know about the prospect; big fast value means giving away something people actually pay for, not something you merely think they should pay for.
  anchor_at: "100m-leads.md:6238"
- id: A-leads-1-032
  type: framework
  name: >-
    Three ways to get volume
  statement: >-
    Volume in cold outreach comes from three things: automate delivery as far as possible, automate distribution as far as possible, and follow up more times in more ways.
  why: >-
    A lower response rate from strangers is made up for by increasing the volume and the type of reach out attempts; you have far more people who don't know you than people who do, so you don't have to worry as much about burning through an audience.
  applies_when: >-
    Problem 3 of cold outreach, once the list and the message exist.
  structure:
    - >-
      a) Automated Delivery.
    - >-
      b) Automate Distribution.
    - >-
      c) Follow up. More times. More ways.
  anchor: >-
    First, we automate delivery to the greatest extent possible. Next,
  source: >-
    100m-leads.md, #3 Cold Outreach, lines 6395–6605
  confirmations: 1
  authors_caveat: >-
    Generally you sacrifice personalization for scale and get a higher response rate with personalized messages, so the fewer leads you have, the less automation you should use; automate when ethical and available.
  anchor_at: "100m-leads.md:6402"
```
