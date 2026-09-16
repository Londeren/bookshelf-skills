# Улов фазы 1 — $100M Leads (2023), chapters up to #3 Cold Outreach (lines 1–6900) (ярус 1), тип B: правила и критерии

Группа `tier1-leads-1`, слаг `leads-1`, ярус 1. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **97** (экстрактор вернул 97, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-leads.md` | 1–6900 | 6 | 97 |

## Как собран файл

Экстрактор B (Rules and criteria) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier1-leads-1.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier1-leads-1-B.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: B-leads-1-001
  type: rule
  name: >-
    Advertise the core offer first
  statement: >-
    Advertising points at the core offer first, and a lead magnet is added only when the core offer alone does not get enough leads to engage.
  why: >-
    Advertising the core offer goes straight for the sale, the direct path to money; the lead magnet exists for the case where people want to know more before they buy, which is common for businesses that sell more expensive stuff.
  applies_when: >-
    Deciding what an ad, post or reach out should point at.
  anchor: >-
    all you need to get leads to engage. Try this way first.]{.calibre3}
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 1848–1850
  confirmations: 1
  anchor_at: "100m-leads.md:1850"
- id: B-leads-1-002
  type: rule
  name: >-
    A lead magnet you could charge for
  statement: >-
    The lead magnet is valuable enough on its own that you could charge for it, and after getting it the lead wants more of what you offer.
  why: >-
    A person who pays with their time now is more likely to pay with their money later, and leads interested in lower-cost or free offers now are more likely to buy a related higher-cost offer later.
  anchor: >-
    [So your lead magnet should be valuable enough on its own that you
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 1882–1888
  confirmations: 2
  anchor_at: "100m-leads.md:1882"
- id: B-leads-1-003
  type: rule
  name: >-
    Grand Slam Offer standard for free stuff
  statement: >-
    The free lead magnet is built to the same standard as a paid Grand Slam Offer, so good that people feel stupid saying no.
  why: >-
    Grand Slam Offers work for free stuff as much or better than for paid stuff, and the business that provides the most value wins.
  anchor: >-
    stuff. So make your lead magnet so insanely good people will feel stupid
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 1938–1944
  confirmations: 2
  anchor_at: "100m-leads.md:1940"
- id: B-leads-1-004
  type: rule
  name: >-
    Narrow problem, next problem your core offer solves
  statement: >-
    The lead magnet solves one narrowly defined problem, and the new problem it reveals is one the core offer can solve.
  why: >-
    Every solution reveals more problems, and the new problem is the one solved in exchange for money; a broad solution leaves nothing for the core offer to be paid for.
  applies_when: >-
    Picking which problem a lead magnet should solve.
  anchor: >-
    to solve. Then, make sure your core offer can solve the next problem
  source: >-
    100m-leads.md, Engage Your Leads, Step 1: Figure out the problem, lines 1982–2010
  confirmations: 2
  anchor_at: "100m-leads.md:2009"
- id: B-leads-1-005
  type: rule
  name: >-
    Many versions, rotated
  statement: >-
    Several versions of the same lead magnet are made across delivery types and rotated rather than one version being run indefinitely.
  why: >-
    It keeps the advertising fresh and low effort, and it shows which versions work best; the results are often surprising and you won't know until you try.
  anchor: >-
    [I make as many versions of a lead magnet as I can and rotate them. This
  source: >-
    100m-leads.md, Engage Your Leads, Step 3: Figure out how to deliver it, lines 2189–2206
  confirmations: 1
  anchor_at: "100m-leads.md:2195"
- id: B-leads-1-006
  type: rule
  name: >-
    Test headline, image, subheadline, in that order
  statement: >-
    Tests run on the headline first, then the image or images, then the subheadline, and if only one thing is tested it is the headline.
  why: >-
    Five times more people read the headline than any other part of the promotion, and improving the headline, name and display of a lead magnet can 2x, 3x or 10x engagement.
  anchor: >-
    and the subheadline, in that order. The headline is the most important.
  source: >-
    100m-leads.md, Engage Your Leads, Step 4: Test What To Name It, lines 2220–2241
  confirmations: 1
  anchor_at: "100m-leads.md:2237"
- id: B-leads-1-007
  type: rule
  name: >-
    Winner and mega winner
  statement: >-
    A tested name is kept when people engage in droves, and counts as a mega winner when they also ask when they can get their hands on it.
  why: >-
    If no one shows interest in your lead magnet, no one will ever know how good it is, so the packaging cannot be left to chance.
  anchor: >-
    [Action Step]{.calibre11}[: Test. If people engage in droves, you've got
  source: >-
    100m-leads.md, Engage Your Leads, Step 4: Test What To Name It, lines 2358–2376
  confirmations: 2
  anchor_at: "100m-leads.md:2358"
- id: B-leads-1-008
  type: rule
  name: >-
    Always test the name somehow
  statement: >-
    Names are tested with polls to whatever following you have, or a post on every platform asking people to answer 1 or 2, or direct messages to individuals, but never left untested.
  why: >-
    You don't need a lot of votes to get a directional idea, and making sure the packaging gets engagement is one of the highest leverage things you can do with your time.
  anchor: >-
    [And if you have any following at all, you can run polls like these. You
  source: >-
    100m-leads.md, Engage Your Leads, Step 4: Test What To Name It, lines 2363–2370
  confirmations: 1
  anchor_at: "100m-leads.md:2363"
- id: B-leads-1-009
  type: rule
  name: >-
    Package it in every format
  statement: >-
    The lead magnet is offered in every format and access point it can be consumed in — phone and computer for software, images, video, text and audio for information, more times and more channels for services, fast and simple ordering for physical products.
  why: >-
    People prefer to do things that take less effort, so making it easier to consume gives 2x, 3x and even 4x+ increases in take rates and in consumption; $100M Offers splits almost evenly across ebook, physical, audiobook and video.
  anchor: >-
    as many different formats as you can: images, video, text, audio, etc.
  source: >-
    100m-leads.md, Engage Your Leads, Step 5: Make it easy for them to consume, lines 2390–2439
  confirmations: 3
  anchor_at: "100m-leads.md:2406"
- id: B-leads-1-010
  type: rule
  name: >-
    More value than the price of the core offer
  statement: >-
    The lead magnet provides more value than the cost of the core offer before anything has been bought.
  why: >-
    People buy based on how much value they think they'll get after they buy, and the easiest way to make them think that is to give them value before they buy; give away the secrets, sell the implementation.
  anchor: >-
    magnet to provide so much value people feel obligated to pay you. The
  source: >-
    100m-leads.md, Engage Your Leads, Step 6: Make it darn good, lines 2453–2481
  confirmations: 1
  anchor_at: "100m-leads.md:2456"
- id: B-leads-1-011
  type: rule
  name: >-
    Free stuff as good as paid stuff
  statement: >-
    Free material is made as good as the paid product.
  why: >-
    99% of people aren't gonna buy, but they create or destroy your reputation based on the value of your free stuff; sucky fluff sends them to a competitor and they tell others not to buy from you.
  anchor: >-
    So, make your lead magnets as good as your paid stuff.
  source: >-
    100m-leads.md, Engage Your Leads, Step 6: Make it darn good, lines 2453–2490
  confirmations: 2
  anchor_at: "100m-leads.md:2488"
- id: B-leads-1-012
  type: rule
  name: >-
    Two things in every CTA
  statement: >-
    Every call to action says what to do and gives reasons to do it right now.
  why: >-
    If you give people a reason to take action, more people will do it.
  anchor: >-
    advertising to work. Good CTAs have two things: 1) what to do and 2)
  source: >-
    100m-leads.md, Engage Your Leads, Step 7: Make it easy for them to tell you they want more, lines 2500–2506
  confirmations: 1
  anchor_at: "100m-leads.md:2505"
- id: B-leads-1-013
  type: rule
  name: >-
    Clear, simple, direct CTA language
  statement: >-
    The CTA is worded clearly, simply and directly — "call now" rather than "don't delay".
  why: >-
    The CTA's only job is to tell the audience how to become engaged leads: don't be clever, be clear.
  anchor: >-
    Good CTAs have clear, simple, and direct
  source: >-
    100m-leads.md, Engage Your Leads, Step 7, lines 2510–2517
  confirmations: 2
  anchor_at: "100m-leads.md:2513"
- id: B-leads-1-014
  type: rule
  name: >-
    Always attach a reason why
  statement: >-
    Every ask carries a reason to act now, and a weak or made-up reason is used rather than none.
  why: >-
    Good reasons work better than bad ones, but any reason, even a bad one, tends to work better than no reason at all; a Harvard experiment showed more people let someone cut in line if they were only given a reason.
  anchor: >-
    reason (even bad ones) tends to work better than no reason at all. So to
  source: >-
    100m-leads.md, Engage Your Leads, Step 7, lines 2521–2615
  confirmations: 2
  anchor_at: "100m-leads.md:2524"
- id: B-leads-1-015
  type: rule
  name: >-
    Ethical scarcity is real scarcity
  statement: >-
    The scarcity used in advertising is the business's actual limit — customer service, onboarding, inventory, time slots per week — stated openly, not an invented number.
  why: >-
    The best strategy for scarcity is reality; if you have limitations you may as well use them to make money, and advertising them rather than hiding them is what makes the scarcity ethical.
  anchor: >-
    per week, etc. Don't keep it a secret - advertise it. This gives you
  source: >-
    100m-leads.md, Engage Your Leads, Step 7, lines 2530–2563
  confirmations: 2
  anchor_at: "100m-leads.md:2544"
- id: B-leads-1-016
  type: rule
  name: >-
    Urgency with a real end point
  statement: >-
    Urgency comes from a stated end point — the offer, discount or bonus stops at a named time and then is gone.
  why: >-
    The less time people have, the faster they tend to act, so making the window to act on the CTA shorter gets more of them to act faster.
  anchor: >-
    urgency with discounts or bonuses that go away after X minutes or hours.
  source: >-
    100m-leads.md, Engage Your Leads, Step 7, lines 2567–2592
  confirmations: 1
  anchor_at: "100m-leads.md:2576"
- id: B-leads-1-017
  type: rule
  name: >-
    Clear, not clever, and often
  statement: >-
    The CTA is given clearly and repeated often rather than being made clever or said once.
  why: >-
    Don't be clever, be clear; and since any reason gets more people to act, the reason why is attached every time.
  anchor: >-
    [Action Step:]{.calibre41}[ Give a clear, simple, action-oriented CTA.
  source: >-
    100m-leads.md, Engage Your Leads, Step 7, lines 2630–2633
  confirmations: 1
  anchor_at: "100m-leads.md:2630"
- id: B-leads-1-018
  type: rule
  name: >-
    A paid lead magnet must lower cost per customer
  statement: >-
    A lead magnet that costs money to deliver is kept only if it lowers what it costs to get a new customer.
  why: >-
    More engaged leads means more chances to get customers, and the extra customers more than cover the delivery cost; in the author's worked example a $25 magnet cuts cost per customer from $3000 to $1000 and triples the business on the same budget.
  anchor: >-
    [Even if your lead magnet costs money to deliver, it should still
  source: >-
    100m-leads.md, Engage Your Leads, Step 7, lines 2637–2670
  confirmations: 1
  anchor_at: "100m-leads.md:2637"
- id: B-leads-1-019
  type: rule
  name: >-
    The four things a good lead magnet does
  statement: >-
    A lead magnet passes only if it engages ideal customers when they see it, gets more people to engage than the core offer alone, is valuable enough that they consume it, and makes the right people more likely to buy.
  why: >-
    Those four jobs are what make more people show interest, make the business more money from them, and deliver more value, all at the same time.
  anchor: >-
    or offer]{.calibre24}[. And a good lead magnet does four things:
  source: >-
    100m-leads.md, Section II Conclusion, lines 2729–2752
  confirmations: 1
  anchor_at: "100m-leads.md:2733"
- id: B-leads-1-020
  type: rule
  name: >-
    Diagnose a lead shortage as skill or volume
  statement: >-
    A shortage of leads is diagnosed as not enough skill or not enough volume in the core four, never as a missing fifth method.
  why: >-
    The core four are the only four things you can do to let anyone know about anything, and you're not getting as many leads as you want because you're not advertising enough. Period.
  anchor: >-
    [So if you aren't getting as many leads as you want, you're not doing
  source: >-
    100m-leads.md, Section III: Get Leads, lines 2891–2913
  confirmations: 2
  anchor_at: "100m-leads.md:2907"
- id: B-leads-1-021
  type: rule
  name: >-
    Everyone has a list
  statement: >-
    Before claiming there are no leads, every contact on every platform — phone contacts, all email accounts ever used, all social profiles — is added up into one number.
  why: >-
    Each contact has subscribed to communication from you and has given you the means and permission to contact them; between phone, email, social media and other platforms you will have more than enough contacts to get started, for many the first 1000 leads.
  anchor: >-
    [Add up ]{.calibre3}[all]{.calibre41}[ your contacts from
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 1: Everyone Has A List, lines 3182–3202
  confirmations: 1
  anchor_at: "100m-leads.md:3196"
- id: B-leads-1-022
  type: rule
  name: >-
    Start on the platform with the most contacts
  statement: >-
    Warm outreach starts on whichever platform holds the most contacts.
  why: >-
    Which platform it is doesn't matter, because you'll hit them all eventually anyway.
  anchor: >-
    [Pick the platform you have the most contacts on. Phone, email, social
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 2: Pick A Platform, lines 3218–3221
  confirmations: 1
  anchor_at: "100m-leads.md:3218"
- id: B-leads-1-023
  type: rule
  name: >-
    A real reason to reach out
  statement: >-
    Each warm reach out opens with something you actually know about that person as the reason for contacting them, researched from their profiles if you don't already know it.
  why: >-
    At this point you haven't asked for anything — you are checking in and providing value, and the personal detail is what makes the message not weird.
  anchor: >-
    [Use something you know about the contact as your actual reason to reach
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 3: Personalize your greeting, lines 3231–3244
  confirmations: 1
  anchor_at: "100m-leads.md:3231"
- id: B-leads-1-024
  type: rule
  name: >-
    Ask for nothing in the opener
  statement: >-
    The first message in a warm reach out asks for nothing.
  why: >-
    Pay your social dues; people love talking about themselves and love being complimented, and if people feel good talking to you they will like and trust you more.
  anchor: >-
    [Don't be a weirdo. Pay your social dues. Remember, you haven't asked
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 3, lines 3237–3239
  confirmations: 1
  anchor_at: "100m-leads.md:3237"
- id: B-leads-1-025
  type: rule
  name: >-
    One hundred reach outs a day
  statement: >-
    Warm outreach runs at 100 personalized reach outs per day.
  why: >-
    A thousand contacts then equals ten solid days of work, a month with follow-ups, after which five or more people will have accepted the free offer; and you learn more in the first ten days of doing 100 reach outs than from everything you have ever read or watched.
  anchor: >-
    [Now, reach out to 100 of them per day with your personalized messages.
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 4, lines 3250–3263
  confirmations: 2
  anchor_at: "100m-leads.md:3260"
- id: B-leads-1-026
  type: rule
  name: >-
    Three attempts, one per day
  statement: >-
    Each contact is reached out to up to three times, once per day for three days, or until they respond, whichever comes first.
  why: >-
    Volume is what makes warm outreach reliable: with enough volume you will get a customer, and the numbers improve the more you do it.
  authors_caveat: >-
    Once per week with physical mail.
  anchor: >-
    reach out to them up to three times. Once per day for three days\* or
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 4, lines 3260–3267
  confirmations: 1
  anchor_at: "100m-leads.md:3262"
- id: B-leads-1-027
  type: rule
  name: >-
    Offer after a normal amount of conversation
  statement: >-
    The offer is made after a normal amount of conversation — 3 to 4 exchanges by phone or message, 3 to 4 minutes in person.
  why: >-
    The A-C-A exchanges let you learn about the person and steer the conversation toward a topic closer to your offer before you test whether they are interested.
  anchor: >-
    [Get through a 'normal' amount of conversation. Think 3-4 exchanges if
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 6: Make them an offer, lines 3341–3348
  confirmations: 1
  anchor_at: "100m-leads.md:3346"
- id: B-leads-1-028
  type: rule
  name: >-
    Maximize the top two, minimize the bottom two
  statement: >-
    An offer built from scratch maximizes dream outcome and perceived likelihood of achievement and minimizes time delay and effort and sacrifice.
  why: >-
    Those are the four elements of value (the value equation from $100M Offers): you show someone you have exactly what they want, that they are guaranteed to get it, insanely fast, without lifting a finger or giving up anything they love.
  authors_caveat: >-
    That ideal is unreachable in full — get as close to it as you can without lying or exaggerating.
  anchor: >-
    [The goal is to maximize the first two and minimize the second two. So
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 6, lines 3352–3416
  confirmations: 1
  anchor_at: "100m-leads.md:3401"
- id: B-leads-1-029
  type: rule
  name: >-
    Ask who they know, not whether they'll buy
  statement: >-
    The warm offer asks whether they know anybody who fits the description, not whether they want to buy.
  why: >-
    Of the people who say yes, most say they themselves are interested; since you didn't ask anyone to buy anything you don't come off as pushy, and you win whether they show interest, refer someone, or both.
  anchor: >-
    to buy anything. We're asking if they know
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 6, lines 3422–3459
  confirmations: 1
  anchor_at: "100m-leads.md:3448"
- id: B-leads-1-030
  type: rule
  name: >-
    Don't try to look advanced
  statement: >-
    The offer is stated honestly and simply rather than dressed up to look more advanced than you are.
  why: >-
    People aren't dumb.
  applies_when: >-
    Making offers early, before you have results to show.
  anchor: >-
    [And don't try to look advanced if you're not. ]{.calibre3}[People
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 7, lines 3508–3510
  confirmations: 1
  anchor_at: "100m-leads.md:3508"
- id: B-leads-1-031
  type: rule
  name: >-
    Three promises in exchange for free
  statement: >-
    The free offer is given on three conditions: they use it, they give feedback, and they leave a review if they think it deserves one.
  why: >-
    It sets reasonable expectations upfront; people who get value, especially for free, are far more likely to leave testimonials, give feedback and send friends and family.
  anchor: >-
    long as you promise to: 1) Use it 2) Give me feedback and 3) Leave a
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 7, lines 3514–3524
  confirmations: 1
  anchor_at: "100m-leads.md:3516"
- id: B-leads-1-032
  type: rule
  name: >-
    Make the first five free
  statement: >-
    Every new product or service is given away free to the first five people.
  why: >-
    You get the reps in and get comfortable making offers, you probably suck for now and people are far more forgiving when they haven't paid, and free customers convert into paying ones, refer paying ones and produce the testimonials that bring paying ones.
  applies_when: >-
    Whenever you launch a new product or service, including in an established business.
  anchor: >-
    [My recommendation - whenever you launch a new product or service -
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 7, lines 3532–3584
  confirmations: 1
  anchor_at: "100m-leads.md:3532"
- id: B-leads-1-033
  type: rule
  name: >-
    Free stuff that is too expensive
  statement: >-
    When people won't take the thing even for free, the cause is one of three: they don't want it, they don't believe you, or the hidden costs of time, effort and sacrifice are too high.
  why: >-
    The most expensive part of what you sell is not the price but the hidden costs — the bottom of the value equation; if you struggle to give your stuff away free, your free stuff is too expensive.
  anchor: >-
    free, it means either people don't want it (dream outcome), they don't
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 7, lines 3596–3607
  confirmations: 1
  anchor_at: "100m-leads.md:3601"
- id: B-leads-1-034
  type: rule
  name: >-
    Ask why after every no
  statement: >-
    Every no is followed by a question about what it would take to make it worth their while to continue.
  why: >-
    Their answers give you a chance to solve their problem, and even if they never buy, they give you the ammunition to get the next person to; yeses give opportunity, nos give feedback.
  anchor: >-
    ["What would I have to do to make it worth it for you to
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 7, lines 3611–3633
  confirmations: 1
  anchor_at: "100m-leads.md:3617"
- id: B-leads-1-035
  type: rule
  name: >-
    Exhaust one platform, then the next
  statement: >-
    When the contacts on one platform are used up, reach outs move to the platform with the next most contacts rather than stopping.
  why: >-
    A thousand contacts across platforms is ten solid days of work and a month with follow-ups, by which point five or more people will have accepted the free offer and some will have become paying customers.
  anchor: >-
    [After reaching out to all the leads on one platform, switch to the
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 8, lines 3656–3669
  confirmations: 1
  anchor_at: "100m-leads.md:3656"
- id: B-leads-1-036
  type: rule
  name: >-
    Once people start referring, start charging
  statement: >-
    The signal that you are good enough to charge is that people start referring others to you.
  why: >-
    That is the litmus test for being good enough to charge, and it replaces guessing about readiness with an observable event.
  anchor: >-
    enough" to charge. ]{.calibre3}[Once people start referring, start
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 9: Start Charging, lines 3679–3694
  confirmations: 1
  anchor_at: "100m-leads.md:3689"
- id: B-leads-1-037
  type: rule
  name: >-
    Raise the price every five
  statement: >-
    After free, the price climbs in steps of 20 percent every five customers — 80% off for the next five, then 60%, then 40% — and keeps climbing until the sweet spot is found.
  why: >-
    The "I increase my prices every five" rule also adds urgency because the prices actually go up, and charging more as you get more experienced is a nice reward.
  anchor: >-
    by 20% every five until you find your sweet spot. It's your business.
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 9: Start Charging, lines 3689–3700
  confirmations: 1
  anchor_at: "100m-leads.md:3698"
- id: B-leads-1-038
  type: rule
  name: >-
    Keep your list warm
  statement: >-
    The list is given regular value through email, social media and the like between reach outs.
  why: >-
    A warm list stays primed for future warm reach outs and is a huge asset because it is a consistent and growing source of engaged leads; treat them well and the audience will feed you forever.
  anchor: >-
    [Give regular value to your list through email, social media, etc. to
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 10: Keep Your List Warm, lines 3710–3769
  confirmations: 1
  anchor_at: "100m-leads.md:3715"
- id: B-leads-1-039
  type: rule
  name: >-
    The 9-word email
  statement: >-
    A warm list is probed with the nine-word email "Are you still looking to [4 word desire]?" and nothing else — no images, no frills, no links, just the question.
  why: >-
    The author credits the template to Dean Jackson and calls it money for getting leads to engage; it is among the first things he does when he invests in a new business.
  applies_when: >-
    Once you have given value to the list for a while, or want to see who wants value.
  anchor: >-
    [No images. No frills. No links. Just a question. Nothing else. This
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 10, lines 3718–3731
  confirmations: 1
  anchor_at: "100m-leads.md:3728"
- id: B-leads-1-040
  type: rule
  name: >-
    Replies go to the top of the queue
  statement: >-
    People who reply to the probe are worked before any other warm reach out.
  why: >-
    The replies are the engaged leads — the ask exists to see who replies.
  anchor: >-
    replies - aka - engaged leads. And ]{.calibre3}[these replies should be
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 10, lines 3759–3761
  confirmations: 1
  anchor_at: "100m-leads.md:3760"
- id: B-leads-1-041
  type: rule
  name: >-
    Warm outreach benchmarks
  statement: >-
    Warm outreach is on benchmark when about one in five contacts engages, about one in five of those takes the free offer, and about one in four of those converts to a paid offer — roughly one customer per 100 reach outs.
  why: >-
    The framework lets you predict how many customers you get per 100 reach outs; the numbers vary with the value of your offer and how much people trust you, but with enough volume you will get a customer.
  applies_when: >-
    Benchmarks as published in 2023.
  anchor: >-
    [Warm reach outs should get about one in five contacts to engage. So one
  source: >-
    100m-leads.md, #1 Warm Outreach, Benchmarks, lines 3796–3814
  confirmations: 1
  anchor_at: "100m-leads.md:3796"
- id: B-leads-1-042
  type: rule
  name: >-
    Four hours a day, first thing
  statement: >-
    When starting out, getting new customers takes the majority of the day — four hours minimum, first thing after getting up, and you don't stop until the goal is reached.
  why: >-
    Time is the first limitation of warm reach outs, and getting new customers is what should take the majority of your time when you are starting out.
  anchor: >-
    should take the majority of your time. Think four hours per day,
  source: >-
    100m-leads.md, #1 Warm Outreach, What's Next?, lines 3869–3877
  confirmations: 1
  anchor_at: "100m-leads.md:3874"
- id: B-leads-1-043
  type: rule
  name: >-
    Topics from your own life
  statement: >-
    Content topics are drawn from your own experience — far past, recent past, present, trending, manufactured — rather than from generic material.
  why: >-
    There is only one of you, so the easiest way to differentiate is to say something no one else can say; no one else has lived your life.
  anchor: >-
    about. I prefer to use personal experiences. Here's why: there's only
  source: >-
    100m-leads.md, #2 Post Free Content Part I, Hook / Topics, lines 4304–4309
  confirmations: 2
  anchor_at: "100m-leads.md:4305"
- id: B-leads-1-044
  type: rule
  name: >-
    Record ideas the moment they come
  statement: >-
    Ideas are written down at the exact time they occur, with a way to record them always within arm's reach, even if a meeting has to be paused.
  why: >-
    Then, when you make content, you have a bucket of fresh stories to work with; people don't mind when you ask to take notes anyway.
  anchor: >-
    you]{.calibre24}[. Always have a way to record your ideas in arms reach.
  source: >-
    100m-leads.md, #2 Post Free Content Part I, Hook / Topics, Present, lines 4378–4384
  confirmations: 1
  anchor_at: "100m-leads.md:4380"
- id: B-leads-1-045
  type: rule
  name: >-
    Make more of what outperforms
  statement: >-
    When a post does better than normal, more content is made on that topic.
  why: >-
    A post doing better than normal tells you it is something people find interesting; posting ideas publicly as they happen is how the author finds out.
  anchor: >-
    as they happen. If a post does better than normal, I know it\'s
  source: >-
    100m-leads.md, #2 Post Free Content Part I, Hook / Topics, Present, lines 4387–4391
  confirmations: 1
  anchor_at: "100m-leads.md:4389"
- id: B-leads-1-046
  type: rule
  name: >-
    At least two headline components
  statement: >-
    A headline carries at least two of the seven components — Recency, Relevancy, Celebrity, Proximity, Conflict, Unusual, Ongoing.
  why: >-
    A meta-analysis of news identified these as the headline components that drove the most interest in stories, and news is the greatest headline creator there is.
  authors_caveat: >-
    The action step of the same section relaxes this to one or more of the components.
  anchor: >-
    most interest in stories. They are as follows. Try and include at least
  source: >-
    100m-leads.md, #2 Post Free Content Part I, Hook / Headlines, lines 4441–4499
  confirmations: 2
  anchor_at: "100m-leads.md:4442"
- id: B-leads-1-047
  type: rule
  name: >-
    Format for the platform first
  statement: >-
    Content is formatted to match the platform first and tweaked to the ideal audience second, using the best-performing content on that platform in your market as the guide.
  why: >-
    People consume content because it is similar to stuff they have liked before; otherwise, no matter how good yours is, better-looking content hooks them before yours has a chance.
  anchor: >-
    Then, tweak it so it hooks your ideal audience. Use the best content on
  source: >-
    100m-leads.md, #2 Post Free Content Part I, Hook / Format, lines 4505–4541
  confirmations: 1
  anchor_at: "100m-leads.md:4540"
- id: B-leads-1-048
  type: rule
  name: >-
    State the number of items
  statement: >-
    When the content is a list or a set of steps, the number of items is given in the headline or in the first few seconds.
  why: >-
    It tells people what to expect, and in the author's experience that retains more of the audience's attention for longer.
  anchor: >-
    your headline, or in the first few seconds of your content, tells people
  source: >-
    100m-leads.md, #2 Post Free Content Part I, Retain / Lists, lines 4580–4586
  confirmations: 1
  anchor_at: "100m-leads.md:4584"
- id: B-leads-1-049
  type: rule
  name: >-
    Retain with lists, steps and stories
  statement: >-
    Attention is held by embedding unresolved questions in the audience's mind through lists, steps and stories, alone or interwoven.
  why: >-
    Curiosity is the strongest driver of retention — people want to know what happens next, and done correctly they will wait years.
  anchor: >-
    [Action Step]{.calibre11}[: Use lists, steps, and stories to keep your
  source: >-
    100m-leads.md, #2 Post Free Content Part I, Retain, lines 4559–4663
  confirmations: 1
  anchor_at: "100m-leads.md:4661"
- id: B-leads-1-050
  type: rule
  name: >-
    Value per second, not length
  statement: >-
    Content is judged by how often it rewards the audience in the time it takes to consume it, never by how long it is.
  why: >-
    There is no such thing as too long, only too boring — the same person who gets bored three seconds into a ten-second video will binge a 900-page book or eight hours of television.
  anchor: >-
    to share it? ]{.calibre3}[How good your content is depends on how often
  source: >-
    100m-leads.md, #2 Post Free Content Part I, Reward, lines 4675–4684
  confirmations: 2
  anchor_at: "100m-leads.md:4678"
- id: B-leads-1-051
  type: rule
  name: >-
    Audience growth is the verdict on content
  statement: >-
    Content counts as rewarding only when the audience is growing; if it is not growing, the content isn't good enough.
  why: >-
    No matter how good you think your content is, the audience decides; rewarding means matching or exceeding their expectations when they chose to consume it.
  anchor: >-
    grows]{.calibre24}[. If it's not growing, your stuff isn't that good.
  source: >-
    100m-leads.md, #2 Post Free Content Part I, Reward, lines 4723–4731
  confirmations: 1
  anchor_at: "100m-leads.md:4730"
- id: B-leads-1-052
  type: rule
  name: >-
    Deliver exactly what the hook promised
  statement: >-
    The content completely answers the unresolved question its hook created — the number promised, for the audience addressed, with material they can use.
  why: >-
    Promising "7 Ways to Make Up with Your Spouse" and giving four ways, weak ways, or giving them to a room of single guys is a bad job of rewarding: people will not watch again and certainly won't share it.
  anchor: >-
    [Action Step]{.calibre11}[: Provide more value than anyone else. Make
  source: >-
    100m-leads.md, #2 Post Free Content Part I, Reward, lines 4703–4738
  confirmations: 2
  anchor_at: "100m-leads.md:4735"
- id: B-leads-1-053
  type: rule
  name: >-
    Start with shorter content
  statement: >-
    Content practice starts with shorter pieces and builds up to longer ones.
  why: >-
    Longer content has to hook, retain and reward more times in a row, which takes more skill: a new comedian gets a few minutes on stage, only a master comic gets an hour.
  anchor: >-
    fine, I suggest starting with shorter versions. You'll have an easier go
  source: >-
    100m-leads.md, #2 Post Free Content Part I, short vs long form, lines 4766–4775
  confirmations: 1
  anchor_at: "100m-leads.md:4773"
- id: B-leads-1-054
  type: rule
  name: >-
    Give far more than you ask
  statement: >-
    A growing audience is fed with a give : ask ratio far above the mature-platform minimum of roughly 3.5:1 on television and about 4 posts per ad on Facebook.
  why: >-
    Mature platforms give less and ask more because they care about monetizing rather than growing their audience; the more you reward your audience, the bigger it gets, so growing platforms dramatically over give and under ask.
  applies_when: >-
    Ratios as observed in 2023.
  anchor: >-
    the bigger it gets. So if you want to grow an audience, give far far
  source: >-
    100m-leads.md, #2 Post Free Content Part II, Mastering the Give : Ask ratio, lines 4843–4864
  confirmations: 1
  anchor_at: "100m-leads.md:4863"
- id: B-leads-1-055
  type: rule
  name: >-
    Give until they ask
  statement: >-
    The preferred strategy is to keep giving until people ask you for the offer, giving in public and asking in private.
  why: >-
    People are always waiting for you to ask for money, and when you don't they trust you more and share more; the moment you start asking for money is the moment you decide to slow your growth, and letting the audience self-select gets the best customers.
  anchor: >-
    strategy, you ]{.calibre3}[give in public, ask in private]{.calibre24}[.
  source: >-
    100m-leads.md, #2 Post Free Content Part II, Mastering the Give : Ask ratio, lines 4872–4914
  confirmations: 3
  anchor_at: "100m-leads.md:4898"
- id: B-leads-1-056
  type: rule
  name: >-
    Integrated asks keep the ratio high
  statement: >-
    An ask may sit in every piece of content as long as the give : ask ratio inside the piece stays high — three 30-second ads in an hour-long podcast is 58.5 minutes of giving to 1.5 of asking.
  why: >-
    A friend whose podcast blew up started asking too frequently inside the content and it stopped growing and then shrank; over-give to protect your most valuable asset, the goodwill of your audience.
  anchor: >-
    so long as you keep your give : ask ratio high. You will continue to
  source: >-
    100m-leads.md, #2 Post Free Content Part II, How To Make Money From Content: Ask, lines 4954–4973
  confirmations: 1
  anchor_at: "100m-leads.md:4955"
- id: B-leads-1-057
  type: rule
  name: >-
    Where the ask goes
  statement: >-
    Asks are placed after a valuable moment or at the end of the piece, one placement at a time, and a second is added only after audience growth has been checked and has not slowed.
  why: >-
    The ask is paid for with potential loss of trust and slower growth, so it is a balancing act — don't kill your golden goose.
  anchor: >-
    CTAs after a valuable moment or the end of the content piece. Consider
  source: >-
    100m-leads.md, #2 Post Free Content Part II, Ask, lines 4977–4980
  confirmations: 1
  anchor_at: "100m-leads.md:4978"
- id: B-leads-1-058
  type: rule
  name: >-
    Short platforms ask intermittently, long ones integrate
  statement: >-
    On short-form platforms asks are intermittent — a promotion every so many give posts; on long-form platforms they are integrated into the piece.
  why: >-
    Which of the two ways dominates depends on the platform.
  anchor: >-
    platform. On short platforms, the intermittent way will dominate. On
  source: >-
    100m-leads.md, #2 Post Free Content Part II, Ask, lines 4992–5001
  confirmations: 1
  anchor_at: "100m-leads.md:5000"
- id: B-leads-1-059
  type: rule
  name: >-
    An ask advertises one of two things
  statement: >-
    An ask advertises either the core offer or the lead magnet, and nothing else.
  why: >-
    That's it — don't overcomplicate this.
  anchor: >-
    [When you make your ask, you either advertise]{.calibre3}[ your core
  source: >-
    100m-leads.md, #2 Post Free Content Part II, Ask, lines 5005–5007
  confirmations: 1
  anchor_at: "100m-leads.md:5005"
- id: B-leads-1-060
  type: rule
  name: >-
    Match the magnet to the content
  statement: >-
    The lead magnet advertised inside a piece of content is relevant to that piece of content.
  why: >-
    As long as the audience wants what the content was about, a matching magnet gets some of them to engage; the thank you page after the opt-in then carries the paid offer.
  anchor: >-
    offer with some video explaining how it works. Bonus points if your lead
  source: >-
    100m-leads.md, #2 Post Free Content Part II, Ask, lines 5011–5018
  confirmations: 1
  anchor_at: "100m-leads.md:5017"
- id: B-leads-1-061
  type: rule
  name: >-
    Back to value after the ask
  statement: >-
    After an ask, the next content returns to providing value.
  why: >-
    Asks are commercials interrupting your own programming: you deposit goodwill with rewarding content and withdraw from it when you make offers, so the deposit has to resume.
  anchor: >-
    [After you make your ask, get back to providing value.]{.calibre3}
  source: >-
    100m-leads.md, #2 Post Free Content Part II, Ask, line 5040
  confirmations: 1
  anchor_at: "100m-leads.md:5040"
- id: B-leads-1-062
  type: rule
  name: >-
    When unsure, advertise the lead magnet
  statement: >-
    If it is unclear whether to advertise the core offer or the lead magnet, the lead magnet is advertised.
  why: >-
    It's lower risk.
  anchor: >-
    lead magnet. If you're not sure, do the lead magnet. It's lower
  source: >-
    100m-leads.md, #2 Post Free Content Part II, Ask, lines 5050–5053
  confirmations: 1
  anchor_at: "100m-leads.md:5052"
- id: B-leads-1-063
  type: rule
  name: >-
    Ceilings for maximizing a platform
  statement: >-
    A platform counts as maximized at up to ten short-form posts per day, or up to five days per week for long form, before the next platform is added.
  why: >-
    Audiences compound faster the more you do, and maximizing one platform before moving on takes advantage of that compounding with fewer resources.
  anchor: >-
    that platform. Short form, you may sometimes be able to get up to ten
  source: >-
    100m-leads.md, #2 Post Free Content Part II, How to Scale It, lines 5092–5095
  confirmations: 1
  anchor_at: "100m-leads.md:5093"
- id: B-leads-1-064
  type: rule
  name: >-
    Pick one scaling approach and start
  statement: >-
    One of the two scaling approaches — depth then width, or width then depth — is chosen and posting starts before the steps are climbed.
  why: >-
    Both are right: depth first compounds faster with fewer resources but risks reliance on one channel, width first reaches a broader audience and repurposes content but costs more labor and often produces bad content everywhere.
  anchor: >-
    [Action Step]{.calibre11}[: Pick an approach. Start posting. Then, go up
  source: >-
    100m-leads.md, #2 Post Free Content Part II, How to Scale It, lines 5071–5185
  confirmations: 1
  anchor_at: "100m-leads.md:5184"
- id: B-leads-1-065
  type: rule
  name: >-
    Content stays relevant to the audience you sell to
  statement: >-
    Content stays on the topics of the audience you sell to rather than drifting to broader subjects.
  why: >-
    When the author stopped making gym content and moved to general business, paid advertising stopped working as it used to; a survey showed 78% of clients had consumed at least two long-form pieces of content before booking a call.
  anchor: >-
    [Bottom line:]{.calibre66}[ Start making content relevant to your
  source: >-
    100m-leads.md, #2 Post Free Content Part II, Why You Should Make Content, lines 5200–5245
  confirmations: 1
  anchor_at: "100m-leads.md:5244"
- id: B-leads-1-066
  type: rule
  name: >-
    How I, not how to
  statement: >-
    Claims are made from your own experience — "How I", "my favorite ways" — rather than as instructions about the best way for the audience.
  why: >-
    When you talk about experience no one can question you, which makes you bulletproof; telling a stranger what to do is hard to do without coming off preachy or arrogant.
  applies_when: >-
    Especially when starting out.
  anchor: >-
    [1)]{.calibre60}[ ]{.calibre61}[Switch from "How to" to "How I." From
  source: >-
    100m-leads.md, #2 Post Free Content Part II, 7 Lessons I've Learned From Making Content, lines 5253–5277
  confirmations: 1
  anchor_at: "100m-leads.md:5253"
- id: B-leads-1-067
  type: rule
  name: >-
    Keep repeating yourself
  statement: >-
    The same message is repeated long past the point where you are bored of it.
  why: >-
    The author posted about his book every single day and one in five people who saw the post still said they didn't know he had a book; we need to be reminded more than we need to be taught, and you get bored of your content before your whole audience has even seen it.
  anchor: >-
    five that saw the post said they didn't know. Keep repeating yourself.
  source: >-
    100m-leads.md, #2 Post Free Content Part II, 7 Lessons, lines 5279–5286
  confirmations: 1
  anchor_at: "100m-leads.md:5284"
- id: B-leads-1-068
  type: rule
  name: >-
    Puddles, Ponds, Lakes, Oceans
  statement: >-
    A small or local business narrows its content to what it does and where it does it before widening to general topics.
  why: >-
    On broad topics the audience will listen to people with better track records than you; narrow and you can become king of that puddle, then expand to the pond, the lake and eventually the ocean.
  anchor: >-
    ]{.calibre11}[Narrow the focus of your content. If you have a small
  source: >-
    100m-leads.md, #2 Post Free Content Part II, 7 Lessons, lines 5289–5298
  confirmations: 1
  anchor_at: "100m-leads.md:5290"
- id: B-leads-1-069
  type: rule
  name: >-
    A master list of greatest hits
  statement: >-
    Content that performs is kept in a master list of "greatest hits", each labelled with the problem it solves and the benefit it provides, for the sales team to send before or after calls.
  why: >-
    That content helps people decide to buy, and works especially well when it resolves specific concerns prospects commonly face.
  anchor: >-
    hits." Label each 'hit' with the problem it solves and the benefit it
  source: >-
    100m-leads.md, #2 Post Free Content Part II, 7 Lessons, lines 5301–5308
  confirmations: 1
  anchor_at: "100m-leads.md:5305"
- id: B-leads-1-070
  type: rule
  name: >-
    Free content is part of the paid ROI
  statement: >-
    Free content is kept as good as the paid product because paying customers consume it and count it in the return they got from what they bought.
  why: >-
    Somebody who buys your stuff is more likely to consume your free content; if it is valuable they like you more and stay loyal longer, and if it sucks they like your paid product less.
  anchor: >-
    free content. This is why it's so important to make your free content
  source: >-
    100m-leads.md, #2 Post Free Content Part II, 7 Lessons, lines 5311–5321
  confirmations: 2
  anchor_at: "100m-leads.md:5319"
- id: B-leads-1-071
  type: rule
  name: >-
    Too boring, never too long
  statement: >-
    Content is fixed for being boring rather than shortened for length.
  why: >-
    People don't have shorter attention spans, they have higher standards: streaming platforms proved people will binge hours of long-form content if they like it — there's no such thing as too long, only too boring.
  anchor: >-
    rewarding stuff to choose from. So make good stuff people like and reap
  source: >-
    100m-leads.md, #2 Post Free Content Part II, 7 Lessons, lines 5324–5333
  confirmations: 2
  anchor_at: "100m-leads.md:5331"
- id: B-leads-1-072
  type: rule
  name: >-
    Avoid pre-scheduling posts
  statement: >-
    Posts are published by a person pressing submit rather than pre-scheduled.
  why: >-
    Manually posted content performs better: knowing you will be rewarded or punished within seconds is a close feedback loop that makes you try that much harder to make it better.
  anchor: >-
    Posts]{.calibre11}[. The posts I manually post perform better than ones
  source: >-
    100m-leads.md, #2 Post Free Content Part II, 7 Lessons, lines 5336–5345
  confirmations: 1
  anchor_at: "100m-leads.md:5337"
- id: B-leads-1-073
  type: rule
  name: >-
    Measure size and speed monthly
  statement: >-
    Audience size (total followers and reach) and the rate of growth are measured every month, in both absolute and relative terms.
  why: >-
    If the audience grows you did good, if it grows fast you did gooder; and as Dr. Kashey puts it, the more ways you measure, the more ways you can win.
  anchor: >-
    did ]{.calibre3}[gooder]{.calibre24}[. So I like to measure my audience
  source: >-
    100m-leads.md, #2 Post Free Content Part II, Benchmarks, lines 5349–5418
  confirmations: 1
  anchor_at: "100m-leads.md:5353"
- id: B-leads-1-074
  type: rule
  name: >-
    Fixed posting and ask cadence
  statement: >-
    A posting cadence and an ask cadence are picked for each platform and then held without stopping.
  why: >-
    We can only control inputs, and measuring outputs is only useful if the inputs are consistent; the author posted a podcast twice a week for four years before it was picked up on the Top 100 list, and could trust the feedback because he did the same thing every week.
  anchor: >-
    if we are consistent with inputs. So, pick the posting cadence you want
  source: >-
    100m-leads.md, #2 Post Free Content Part II, Benchmarks, lines 5392–5428
  confirmations: 1
  anchor_at: "100m-leads.md:5393"
- id: B-leads-1-075
  type: rule
  name: >-
    The first post may carry an ask
  statement: >-
    The very first post may include an ask, and if it produces no engaged lead you give for a while before asking again.
  why: >-
    You have probably been providing value to other humans knowingly or unknowingly for a while, so the right to ask may already have been earned; if not, it has to be earned first.
  anchor: >-
    engaged lead. If it doesn't, you need to give for a while, then make an
  source: >-
    100m-leads.md, #2 Post Free Content Part II, Your First Post, lines 5438–5448
  confirmations: 1
  anchor_at: "100m-leads.md:5441"
- id: B-leads-1-076
  type: rule
  name: >-
    Content is added to warm outreach, not swapped for it
  statement: >-
    Posting free content is done in addition to warm reach outs, never instead of them.
  why: >-
    Posting free content grows the warm audience, and a bigger warm audience means more people for warm reach outs, so content gets engaged leads on its own and keeps getting them through warm reach outs.
  anchor: >-
    ditching one for the other, I recommend you post free content
  source: >-
    100m-leads.md, #2 Post Free Content Part II, So What Do I Do Right Now?, lines 5506–5513
  confirmations: 1
  anchor_at: "100m-leads.md:5512"
- id: B-leads-1-077
  type: rule
  name: >-
    Most accessible leads first
  statement: >-
    Targeted cold lists are sourced in order — scraping software first, list brokers second, manual assembly from groups and communities third — with a sample of a few hundred tested before any source is scaled.
  why: >-
    You work from the most accessible leads to the least accessible; if you can search the database so can everyone else, whereas a list you assemble yourself is the freshest because those people are less likely to have had cold reach outs from other companies.
  anchor: >-
    [So I work my way from the most accessible leads to the least accessible
  source: >-
    100m-leads.md, #3 Cold Outreach, Problem #1: Build a List, lines 6169–6211
  confirmations: 1
  anchor_at: "100m-leads.md:6204"
- id: B-leads-1-078
  type: rule
  name: >-
    Put your first 1000 names together
  statement: >-
    The first cold list is 1000 names, and someone with more time than money starts with manual assembly rather than software or brokers.
  why: >-
    Manual assembly only costs time, while software and brokers cost money.
  anchor: >-
    Put your first 1000 names together. If you have more time than money,
  source: >-
    100m-leads.md, #3 Cold Outreach, Problem #1 action step, lines 6215–6220
  confirmations: 1
  anchor_at: "100m-leads.md:6218"
- id: B-leads-1-079
  type: rule
  name: >-
    One to three personal facts
  statement: >-
    Each cold message opens with one to three pieces of information a friend might know about the prospect, a compliment on them, and ideally how they benefited you.
  why: >-
    People like people who like them, and even a stranger will give you more time if you know something about them; personalization is what gets your foot in the door to get the sale, making the cold reach out look like a warm one.
  anchor: >-
    the sale. Basically one to three pieces of information we can find that
  source: >-
    100m-leads.md, #3 Cold Outreach, Problem #2a: Personalize, lines 6246–6312
  confirmations: 1
  anchor_at: "100m-leads.md:6300"
- id: B-leads-1-080
  type: rule
  name: >-
    Research before you send
  statement: >-
    A little research is done on each lead before a message is sent, batched, and the notes are used for the opening line.
  why: >-
    Even if someone doesn't know you, they will appreciate the time you took to research them before contacting them; this tiny effort goes a long way.
  anchor: >-
    [Action step: ]{.calibre11}[Do a little research on each lead before you
  source: >-
    100m-leads.md, #3 Cold Outreach, Problem #2a, lines 6316–6320
  confirmations: 1
  anchor_at: "100m-leads.md:6316"
- id: B-leads-1-081
  type: rule
  name: >-
    Blow their minds in under thirty seconds
  statement: >-
    The cold message is built to demonstrate big value in under thirty seconds, not to tickle interest.
  why: >-
    Strangers give you far less time to prove your worth and need far more incentive to move towards you, so mediocre offers blend into the ocean of people trying to get their attention and get ignored.
  anchor: >-
    We're not trying to tickle their interest, ]{.calibre3}[we're trying to
  source: >-
    100m-leads.md, #3 Cold Outreach, Problem #2b: Big Fast Value, lines 6328–6376
  confirmations: 2
  anchor_at: "100m-leads.md:6332"
- id: B-leads-1-082
  type: rule
  name: >-
    Up the ante when it isn't working
  statement: >-
    When the cold offer or lead magnet isn't working, more is offered until they feel stupid saying no, rather than the message being tweaked.
  why: >-
    Four months of cold outreach on a "game planning session" — code for a sales call — mostly failed; swapping it for as much free service as could be afforded tripled take rates and made cold outreach a monster channel.
  anchor: >-
    [If your offer/lead magnet isn't working for you, up the ante. Keep
  source: >-
    100m-leads.md, #3 Cold Outreach, Problem #2b, lines 6351–6365
  confirmations: 1
  anchor_at: "100m-leads.md:6362"
- id: B-leads-1-083
  type: rule
  name: >-
    Give away what people actually pay for
  statement: >-
    The free thing offered to strangers is something people actually pay for, not merely something good enough that they should pay for it.
  why: >-
    Give yourself a downhill battle by giving away something crazy: give away for free something people would normally pay for and they will want it — the difference between "so good they should pay for it" and "stuff they actually pay for" is big.
  anchor: >-
    free people would normally pay for and they will want it. Note: I didn't
  source: >-
    100m-leads.md, #3 Cold Outreach, Problem #2b, lines 6369–6376
  confirmations: 1
  anchor_at: "100m-leads.md:6373"
- id: B-leads-1-084
  type: rule
  name: >-
    Script length limits
  statement: >-
    Phone and chat scripts run no more than a page or two and cold emails rarely more than half a page.
  why: >-
    There are no awards for prettiest script, so don't overthink it.
  anchor: >-
    scripts are never more than a page or two, and cold emails rarely more
  source: >-
    100m-leads.md, #3 Cold Outreach, Problem #2b action step, lines 6380–6389
  confirmations: 1
  anchor_at: "100m-leads.md:6385"
- id: B-leads-1-085
  type: rule
  name: >-
    Volume before tweaking the script
  statement: >-
    A cold script is only tweaked after the first 100 conversations or 10,000 emails have gone out.
  why: >-
    Get testing first, then tweak as you learn.
  anchor: >-
    prettiest script. Get your first 100 conversations or 10,000 emails out
  source: >-
    100m-leads.md, #3 Cold Outreach, Problem #2b action step, lines 6386–6389
  confirmations: 1
  anchor_at: "100m-leads.md:6387"
- id: B-leads-1-086
  type: rule
  name: >-
    Automate when ethical and available
  statement: >-
    Delivery and distribution of cold messages are automated wherever it is ethical and available.
  why: >-
    Automated delivery unlocks huge scale because nobody has to convey the message each time, so you get more engaged leads per unit of time even if a smaller percentage engages; and there's no award for who works hardest, only for who gets the best results.
  anchor: >-
    portions of the work. I encourage you to automate when ethical and
  source: >-
    100m-leads.md, #3 Cold Outreach, Problem #3a–b: Volume, lines 6400–6453
  confirmations: 1
  anchor_at: "100m-leads.md:6452"
- id: B-leads-1-087
  type: rule
  name: >-
    Automation scales with the size of the list
  statement: >-
    The fewer leads on the list, the less automation is used and the more each message is personalized.
  why: >-
    You sacrifice personalization for scale and get a higher response rate with personalized messages: with only 1000 qualifying hedge fund managers you personalize every one, with tens of millions of prospects you can get away with less.
  anchor: >-
    leads you have, the less automation you should use.]{.calibre24}
  source: >-
    100m-leads.md, #3 Cold Outreach, Problem #3b, lines 6470–6480
  confirmations: 1
  anchor_at: "100m-leads.md:6472"
- id: B-leads-1-088
  type: rule
  name: >-
    Ten to twenty percent on untested technology
  statement: >-
    Ten to twenty percent of outreach effort is spent on brand new, untested technology.
  why: >-
    Embrace new technology: if you make phone calls five days a week, run a new dialer or tool on one of those days and see how it does compared to your standard one.
  anchor: >-
    twenty percent of your effort towards brand new untested technology. For
  source: >-
    100m-leads.md, #3 Cold Outreach, Problem #3b action step, lines 6488–6492
  confirmations: 1
  anchor_at: "100m-leads.md:6489"
- id: B-leads-1-089
  type: rule
  name: >-
    A non-response is the reason for the next channel
  statement: >-
    A lead who doesn't answer on one channel is followed up on another, using the unanswered attempt as the stated reason for the new one.
  why: >-
    You either get a response or a real reason to reach out again, so you win either way; and people respond to different methods.
  anchor: >-
    methods, use that as a reason to follow up with another method.
  source: >-
    100m-leads.md, #3 Cold Outreach, Problem #3c: Follow up, lines 6516–6535
  confirmations: 1
  anchor_at: "100m-leads.md:6532"
- id: B-leads-1-090
  type: rule
  name: >-
    Expect two to three conversations
  statement: >-
    A higher-ticket cold sale is planned for two to three conversations after the appointment is booked, not one.
  why: >-
    Outreach takes more touch points with people who don't know you; shoot for less, but expect more when you start out.
  anchor: >-
    don't know you. So expect two to three conversations before a higher
  source: >-
    100m-leads.md, #3 Cold Outreach, Problem #3c, lines 6539–6544
  confirmations: 1
  anchor_at: "100m-leads.md:6542"
- id: B-leads-1-091
  type: rule
  name: >-
    Multiple times, multiple ways
  statement: >-
    Each cold lead is contacted more than once and through more than one method.
  why: >-
    The more ways you try to contact someone the more likely you are to reach them, and contacting someone multiple times in multiple ways quickly shows you are serious and that you have something important to discuss.
  anchor: >-
    [Action Step: ]{.calibre11}[Contact each lead multiple times in multiple
  source: >-
    100m-leads.md, #3 Cold Outreach, Problem #3c, lines 6504–6556
  confirmations: 1
  anchor_at: "100m-leads.md:6555"
- id: B-leads-1-092
  type: rule
  name: >-
    Work the list again after three to six months
  statement: >-
    Once a list has been worked through with multiple attempts in multiple ways, it is left three to six months and then worked again from the top.
  why: >-
    They may not have seen the first messages, it may not have been a moment when they could respond, or their circumstances may have changed — everything may be right except the timing.
  anchor: >-
    multiple times, multiple ways, wait three to six months. Then, do it
  source: >-
    100m-leads.md, #3 Cold Outreach, Problem #3c, lines 6564–6605
  confirmations: 1
  anchor_at: "100m-leads.md:6604"
- id: B-leads-1-093
  type: rule
  name: >-
    Warm first, content next, cold after
  statement: >-
    Cold outreach is started only after warm reach outs and posted content have given you reps, not as the first advertising method.
  why: >-
    Cold outreach sits atop the foundation of warm outreach and is its more advanced cousin; the book is written in that order to build on itself.
  anchor: >-
    reach outs. Get some reps. Post some content to grow your warm audience.
  source: >-
    100m-leads.md, #3 Cold Outreach, Three Problems Strangers Create→Solved, lines 6619–6622
  confirmations: 2
  anchor_at: "100m-leads.md:6620"
- id: B-leads-1-094
  type: rule
  name: >-
    Whoever runs outreach knows every stat
  statement: >-
    The person running cold outreach knows every single metric of the sales process like the back of their hand.
  why: >-
    The two times cold outreach failed, the author had hired people who never tracked metrics well; the third person did, and cold reach outs succeeded.
  anchor: >-
    succeeded. The person who runs it (maybe you) has to know the metrics of
  source: >-
    100m-leads.md, #3 Cold Outreach, Benchmarks, lines 6642–6646
  confirmations: 1
  anchor_at: "100m-leads.md:6644"
- id: B-leads-1-095
  type: rule
  name: >-
    Three times the cost, minimum
  statement: >-
    Cold outreach is doing well when the lifetime profit from a customer is at least three times what it cost to get them.
  why: >-
    Three times is the bare minimum and you can do WAY better — the portfolio company cited gets over 30:1 returns from its outreach; the same test decides when to hand the work to a hired rep.
  applies_when: >-
    Benchmarks as published in 2023.
  anchor: >-
    this in Section IV). So you know you do well when you make at least
  source: >-
    100m-leads.md, #3 Cold Outreach, Benchmarks, lines 6663–6710
  confirmations: 2
  anchor_at: "100m-leads.md:6670"
- id: B-leads-1-096
  type: rule
  name: >-
    Three percent of a cold email list
  statement: >-
    Cold email is on benchmark when about 3% of the list turns into engaged leads — roughly 30% opening and 10% of those replying with interest.
  why: >-
    A new campaign for a very niche high-ticket service business in the portfolio showed a 4% lead engagement rate, with presumably a third converting to sales — one new customer per hundred outreach attempts.
  applies_when: >-
    Benchmarks as published in 2023.
  anchor: >-
    vary but ]{.calibre3}[shoot for 3% of your list turning into engaged
  source: >-
    100m-leads.md, #3 Cold Outreach, Benchmarks, Email Example, lines 6680–6688
  confirmations: 1
  anchor_at: "100m-leads.md:6683"
- id: B-leads-1-097
  type: rule
  name: >-
    When to start cold outreach
  statement: >-
    Cold outreach is begun when you run out of people to advertise to, or simply because you want more leads.
  why: >-
    At some point you will want to grow faster than you currently are, or to increase the predictability of your lead flow, and cold outreach is no longer limited by the size of your warm audience.
  anchor: >-
    get more engaged leads with cold outreach. You start this as you run out
  source: >-
    100m-leads.md, #3 Cold Outreach, Your Turn, lines 6864–6867
  confirmations: 2
  anchor_at: "100m-leads.md:6865"
```
