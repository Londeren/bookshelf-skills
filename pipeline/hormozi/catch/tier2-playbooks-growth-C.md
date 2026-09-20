# Улов фазы 1 — $100M Playbooks: Lead Nurture, Retention, Fast Cash, GOATed Ads (2025) (ярус 2), тип C: разборы (кейсы)

Группа `tier2-playbooks-growth`, слаг `playbooks-growth`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **48** (экстрактор вернул 48, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `playbook-lead-nurture.md` | 1–1148 | 2 | 16 |
| `playbook-retention.md` | 1–835 | 2 | 17 |
| `playbook-fast-cash.md` | 1–779 | 2 | 8 |
| `playbook-goated-ads.md` | 1–707 | 1 | 7 |

## Как собран файл

Экстрактор C (Application cases) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-playbooks-growth.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-playbooks-growth-C.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: C-playbooks-growth-001
  type: case
  name: >-
    Vlad's show-rate analysis
  statement: >-
    With a tool managing 4,000+ appointments a day and failing, the author handed a data
    specialist a spreadsheet of about a million rows of appointment data and one question:
    what gets people to show up. The analysis came back with exactly four correlates of
    positive appointments - more time slots available, fewer days between scheduling and the
    appointment, more follow-ups, and more responses by leads to those follow-ups - and those
    four became the four pillars of lead nurture.
  why: >-
    These four points gave business owners something they could do to make money now, because
    you can only sell somebody if they show up to buy.
  anchor: >-
    First, the more time slots available, the greater the show rate.
  source: >-
    playbook-lead-nurture.md, Lead Nurture, lines 170-176
  confirmations: 2
  demonstrates: >-
    The four pillars of lead nurture (availability, speed, personalization, volume) and the
    common-factors way of finding what actually drives a metric.
  anchor_at: "playbook-lead-nurture.md:170"
- id: C-playbooks-growth-002
  type: case
  name: >-
    Leila's four calls for a nail appointment
  statement: >-
    Needing an appointment within the hour in an unfamiliar city, she works down the Yelp list:
    the first salon does not answer, the second has nothing until tomorrow, the third promises
    to call back and hangs up, and the fourth takes walk-ins, collects first and last name,
    confirms the number, texts the confirmation while still on the phone and names the person
    who will serve her. The fourth one gets the money.
  why: >-
    If leads cannot schedule, they cannot show, and if they cannot show, they cannot buy; on an
    absolute basis the businesses with the most time slots had the most schedules, shows and
    purchases.
  anchor: >-
    “No no openings. We can get you in tomorrow.”
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability, lines 264-285
  confirmations: 1
  demonstrates: >-
    Pillar I Availability - availability is the biggest lever on show rate; plus immediate
    confirmation and naming the person the lead will meet.
  anchor_at: "playbook-lead-nurture.md:267"
- id: C-playbooks-growth-003
  type: case
  name: >-
    Author Note: My First Online Scheduler
  statement: >-
    Three successive versions of the same thank-you page. First: thank you, you will be getting
    a text from this number shortly to book a time. Second: the same plus a photo of Leila
    saying she will be reaching out at this number. Third: text Leila at this number with the
    time that works for you to come in - and that one crushed.
  why: >-
    Apparently no one cared about faceless Alex, but as soon as leads saw a picture of a real
    young woman, both men and women were more likely to book.
  anchor: >-
    putting an image of Leila and saying “Leila will be reaching out to you at this
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability - Author Note: My First Online Scheduler, lines 387-392
  confirmations: 1
  demonstrates: >-
    Eliminating steps in the self-scheduling process and personalizing it by showing a real
    person rather than the business.
  anchor_at: "playbook-lead-nurture.md:390"
- id: C-playbooks-growth-004
  type: case
  name: >-
    The pull-the-appointment-forward call
  statement: >-
    Skeleton of the call to someone who self-scheduled: name yourself, say you are on a recorded
    line, name the booking you are calling about, ask whether now is a terrible time; then
    qualify in three moves - WHO they are, WHAT they want, WHAT they are struggling with and
    what they have tried - and get them to agree it is a priority to fix; then good news (we can
    help) plus a slot that just cancelled later the same day, closing with "unless now is a good
    time?".
  why: >-
    Show rates for same-day appointments are higher than not same day, and show rates for
    talking to them right now are 100%.
  applies_when: >-
    In the gaps between appointments, once there are no fresh leads to contact and schedule.
  anchor: >-
    Hey, this is Jim... calling from XYZ on a recorded line... I saw that you just booked a
  source: >-
    playbook-lead-nurture.md, Pillar II: Speed, lines 508-518
  confirmations: 1
  demonstrates: >-
    Pillar II Speed - speed to first appointment and pulling appointments forward; the five
    possible outcomes of a scheduling call.
  anchor_at: "playbook-lead-nurture.md:508"
- id: C-playbooks-growth-005
  type: case
  name: >-
    Re-confirming when the appointment cannot be moved
  statement: >-
    Worst case of the pull-forward call: frame the extra times offered as wanting to cost them
    as little time as possible, restate the existing day and hour back to them, and close with a
    commitment question - is there any reason you think you will not be able to make that
    appointment.
  why: >-
    Once you have worked the lead this way you have optimized their outcome for the maximum
    possible show-ups; the re-confirm is the worst of the three acceptable endings, and it still
    ends with a stated commitment.
  anchor: >-
    No worries at all. We always like to offer more times to make it convenient. We want to
  source: >-
    playbook-lead-nurture.md, Pillar II: Speed, lines 522-524
  confirmations: 1
  demonstrates: >-
    Pillar II Speed - ending every scheduling call with either a sale, a pulled-forward
    appointment or an explicitly re-confirmed one.
  anchor_at: "playbook-lead-nurture.md:522"
- id: C-playbooks-growth-006
  type: case
  name: >-
    The hot hand off
  statement: >-
    Handing the lead to the closer: tell them they are in luck, edify the closer by his
    expertise and by results with people matched to the lead's own description, check his
    calendar out loud, state whether the time moved or is confirmed, then promise a text
    introduction the moment the call ends and confirm the number to use.
  why: >-
    Edifying the closer and introducing them in real time is the last step of working the lead
    for maximum possible show-ups, and it probably means the sales team is understaffed for
    maximum selling.
  anchor: >-
    You’re in luck. You’re actually going to speak with one of our top experts on X. He’s been
  source: >-
    playbook-lead-nurture.md, Pillar II: Speed, lines 530-537
  confirmations: 1
  demonstrates: >-
    Pillar II Speed - the hot handoff to an active closer when setter and closer are different
    people.
  anchor_at: "playbook-lead-nurture.md:530"
- id: C-playbooks-growth-007
  type: case
  name: >-
    Scenario #1 and Scenario #2 after the appointment is booked
  statement: >-
    Both leads opt in, are contacted immediately and confirm the appointment. In the first, a
    texted question gets answered the next business day, then the next question the next
    business day again; the lead concludes the business is scattered and stops asking. In the
    second, every question gets an immediate reply and the closer adds context, so question and
    follow-up are both answered within a minute.
  why: >-
    Leads often make buying decisions before the sales call, which makes it the competitor's
    sale to lose; if you do not show up for them, they will not show up for you.
  anchor: >-
    You got your question and follow-up question answered within a minute. These guys are
  source: >-
    playbook-lead-nurture.md, Pillar II: Speed - 3) Speed of Response, lines 552-565
  confirmations: 1
  demonstrates: >-
    Pillar II Speed - speed of response between scheduling and the appointment; time stamps on
    calls and messages as the place to look first when show rates drop.
  anchor_at: "playbook-lead-nurture.md:563"
- id: C-playbooks-growth-008
  type: case
  name: >-
    The beta tester who texted about a shirt
  statement: >-
    One ALAN beta tester had show rates far beyond the rest of the test group with the same open
    loops, the same messages, the same cadence and normal-looking ad campaigns. The difference
    was invisible in the system: a text from a separate iPhone offering a shirt that is already
    waiting for them and asking whether they prefer black or pink. As soon as a lead names a
    colour, they show up almost every time.
  why: >-
    If the lead knows they will get value just for showing up, their risk drops and their
    opportunity cost of skipping rises, which makes the appointment itself worth more.
  anchor: >-
    couldn’t see it—and say, ‘Hey, I’ve got a shirt here waiting for you. Do you prefer black or
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, lines 601-607
  confirmations: 1
  demonstrates: >-
    Pillar III Personalization - incentives, and specifically the A/B choice whose both options
    assume the lead shows up.
  anchor_at: "playbook-lead-nurture.md:604"
- id: C-playbooks-growth-009
  type: case
  name: >-
    The weight loss company that cancels sales appointments
  statement: >-
    A small, boring-product weight loss company with exceptional show percentages and high
    profits actively cancelled sales appointments. Every lead filled out an application before
    the sales call, and the owner cancelled the ones whose answers showed they were not a fit,
    so his time went to good leads and the bad ones were ignored completely.
  why: >-
    By qualifying before the call he spends way more time working good leads and completely
    ignores the bad ones.
  anchor: >-
    What I saw shocked me... they actively canceled sales appointments. Blasphemy!
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization - 2) Qualify The Leads, lines 661-671
  confirmations: 1
  demonstrates: >-
    Pillar III Personalization - qualify the leads: collect data, then remove from the calendar
    the leads unlikely to buy.
  anchor_at: "playbook-lead-nurture.md:663"
- id: C-playbooks-growth-010
  type: case
  name: >-
    The number one timeshare rep
  statement: >-
    The top rep of a nearly 3,000-rep timeshare company, first five years out of six, used his
    one meeting with the CEO to say the good leads were being wasted on junior reps while he
    spent two-thirds of his time on people with 500 credit scores. Given the best leads at his
    local office, he 5x'd its production the next year; rolled out nationwide, the company went
    from $200M to $1B a year in sales over the next five years.
  why: >-
    Connecting the leads most likely to buy with the reps most likely to close is where the same
    lead pool produces far more sales.
  anchor: >-
    I waste two-thirds of my time with people who have 500 credit scores. Just give me the
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization - 3) Send The Best Leads To The Best Closers, lines 684-689
  confirmations: 1
  demonstrates: >-
    Pillar III Personalization - look at your best customers, ask those questions in opt-ins and
    applications, score leads 1-5 or red-yellow-green, and route the best leads to the best
    closers.
  anchor_at: "playbook-lead-nurture.md:685"
- id: C-playbooks-growth-011
  type: case
  name: >-
    The Greg reach-out
  statement: >-
    The easy version of segmented messaging is five minutes of homework before contact -
    profile, website, recent news - turned into an opening that names a specific number from
    the lead's own business, a comparable customer's result, and a walkthrough already prepared
    for that lead's industry.
  why: >-
    People are more likely to listen and pay attention to someone who behaves like someone they
    know.
  anchor: >-
    quarter, we had another customer in a similar situation. They’re now up 100% 90 days later.
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization - 4) Segment Your Messaging, lines 710-712
  confirmations: 1
  demonstrates: >-
    Pillar III Personalization - segment your messaging, easy version; people listen to someone
    who behaves like someone they know.
  anchor_at: "playbook-lead-nurture.md:711"
- id: C-playbooks-growth-012
  type: case
  name: >-
    The gift card push incentive
  statement: >-
    A push incentive is a gift sent before the appointment with no strings, delivered whether
    they show or not, and small enough that the amount does not matter as long as it is not
    insulting: a text the day before saying they should be caffeinated for the meeting, and a
    $5 gift card already in their email.
  why: >-
    The strategy hinges on reciprocity, and it still works even when people know what you are
    doing, which also lifts close rate.
  anchor: >-
    Check your email. I just sent you a $5 gift card.”
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization - 5) Incentives, lines 753-754
  confirmations: 1
  demonstrates: >-
    Pillar III Personalization - push incentives given before arrival to evoke reciprocity.
  anchor_at: "playbook-lead-nurture.md:754"
- id: C-playbooks-growth-013
  type: case
  name: >-
    The beauty chain A/B pull incentive
  statement: >-
    Brick-and-mortar beauty chain: the prospect opts in, gets a call within five minutes, and is
    told that as a first-time client some free products are being set aside - face cream or hand
    lotion? She picks one, and the answer is that it will be waiting for her tomorrow.
  why: >-
    A pull incentive works when the lead wants the thing, it connects obviously to what you
    sell, and you have visibly incurred a real cost preparing it - and both options assume they
    will show.
  anchor: >-
    “Hey Name! Since you are a first-time client, I’m going to set aside some free products for
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization - 5) Incentives, lines 757-761
  confirmations: 1
  demonstrates: >-
    Pillar III Personalization - the A/B pull incentive, and the five-minute speed to contact
    that carries it.
  anchor_at: "playbook-lead-nurture.md:758"
- id: C-playbooks-growth-014
  type: case
  name: >-
    The insurance company and BAMFAM
  statement: >-
    In an acquired insurance company the biggest constraint was prospects dropping off between
    the first and second call, while reps built and sent qualified plans in between - lots of
    work, low return. One change was made to the lead nurture process: BAMFAM, book a meeting
    from a meeting, never ending a call with "we will circle back later". Second-call show rates
    skyrocketed and sales increased.
  why: >-
    People are likelier to show up to appointments you scheduled, and you have the highest
    chance of scheduling one while you are with them in real time.
  anchor: >-
    We bought an insurance company over a year ago. The biggest constraint was prospects
  source: >-
    playbook-lead-nurture.md, Pillar IV: Volume - 3) Book Their Next Appointment At The Current Appointment, lines 908-924
  confirmations: 1
  authors_caveat: >-
    The author attributes BAMFAM to his friend Sharran Srivatsaa.
  demonstrates: >-
    Pillar IV Volume - BAMFAM: someone being dodgy about their next call is an objection to
    handle, not a scheduling problem.
  anchor_at: "playbook-lead-nurture.md:908"
- id: C-playbooks-growth-015
  type: case
  name: >-
    Double what the top guy does
  statement: >-
    Coaching a new hire onto a cold-call team with a 150-call-per-day quota: look at what the
    top guy on the team is doing and do double it - 400 calls to his 200, six days to his five,
    no lunch break - because doing the same amount as him leaves you permanently behind.
  why: >-
    You cannot do the same amount as the top guy, because then he will always be ahead; the only
    way to catch up is to do more.
  anchor: >-
    then do double that. So he’s making 200 calls a day, I need you to make 400. If he works
  source: >-
    playbook-lead-nurture.md, Execution, lines 982-986
  confirmations: 1
  demonstrates: >-
    Volume negates luck, and the culture of execution that makes the boring work of working
    leads happen.
  anchor_at: "playbook-lead-nurture.md:983"
- id: C-playbooks-growth-016
  type: case
  name: >-
    Yellows are the new gold
  statement: >-
    On a simple lead scoring system - reds truly unqualified, yellows less qualified, greens
    prime - the other reps cherry-picked and handed their yellows to one new salesman, who
    worked them in off-hours and on weekends and kept closing them, finishing as the top
    salesman of 26. Behind it was a reframe: an under-qualified lead is not wasted time but free
    practice at the script and the objections.
  why: >-
    Seeing every opportunity as a swing of the hammer that chisels the skillset means no lead is
    wasted time, and some people who look unpromising turn out to be the opposite.
  anchor: >-
    of their guys would give their yellows to Jacob and he would take them in off-hours and
  source: >-
    playbook-lead-nurture.md, Execution, lines 1010-1015
  confirmations: 1
  demonstrates: >-
    Execution culture - be a garbage man, do not judge leads by their score alone, every lead is
    an opportunity for practice.
  anchor_at: "playbook-lead-nurture.md:1013"
- id: C-playbooks-growth-017
  type: case
  name: >-
    The leaky bucket arithmetic
  statement: >-
    At 15% month-over-month churn a gym owner loses 83% of their members in a year: with 250
    members on January 1st they need 208 new clients by December 31st just to stay the same,
    and at 12.5% margins falling two customers a month behind loses the gym.
  why: >-
    A business with a revolving door of customers is hardly a business at all; if you get behind
    at all, it dies.
  anchor: >-
    At 15% month-over-month churn, a gym owner loses 83% of their members in a year.
  source: >-
    playbook-retention.md, Churn Checklist - opening, lines 69-74
  confirmations: 1
  demonstrates: >-
    Why churn is worked on before more selling - the leaky bucket business.
  anchor_at: "playbook-retention.md:69"
- id: C-playbooks-growth-018
  type: case
  name: >-
    Common factors analysis applied to churn
  statement: >-
    The three-step consulting process - ask experts in the plural, collect all their answers,
    find the common threads - applied to retention: research every gym owner under 3%
    month-over-month churn for the last six months, interview each about every single thing they
    did, then overlap the answers. Five common factors survived and became The 5 Horsemen of
    Retention.
  why: >-
    Talking to people who already know your problem gets solutions faster, and overlapping many
    answers eliminates each expert's bias and reveals the core problem.
  anchor: >-
    I found 5 common factors – which became The 5 Horsemen of Retention.
  source: >-
    playbook-retention.md, Solving Problems Like The Big Boys, lines 101-104
  confirmations: 1
  demonstrates: >-
    The expert-interview plus common-factors method, later reused to find activation points.
  anchor_at: "playbook-retention.md:104"
- id: C-playbooks-growth-019
  type: case
  name: >-
    The attendance decay pattern
  statement: >-
    The churn signature of a gym member, week by week: 3 sessions, 2, 2, 1, CANCEL. Talking to
    them at the moment attendance drops to two sessions - in week 2, not later - turns the same
    member into 3, 2 with a reach-out, then 3, 3, 3.
  why: >-
    A member who goes three times a week or more sticks; twice a week or less and they churn
    out, so attendance is the leading indicator you can act on.
  anchor: >-
    would stick. If they went less than twice per week or less, they’d churn out. Attendance
  source: >-
    playbook-retention.md, The 5 Horsemen of Retention, lines 110-124
  confirmations: 1
  demonstrates: >-
    Horseman 1 Track attendance, and more generally usage churn: intercept the customer at the
    moment consumption drops, not at cancellation.
  anchor_at: "playbook-retention.md:111"
- id: C-playbooks-growth-020
  type: case
  name: >-
    Shaking the tree: what the 5 Horsemen did to churn
  statement: >-
    Rolling out all five horsemen with the gyms, churn went UP by 50% in month 1, then DOWN by
    50% in month 2 and by another 50% in month 3. In numbers: 10% to 15%, then 15% to 7%, then
    7% to 3%. The first-month spike is the people who would have cancelled anyway plus those who
    had already churned as consumers while the billing ran on.
  why: >-
    A reduction in churn from 9% to 3% is a 3.3x increase in lifetime value, and the author has
    yet to see a business under 3% churn that does not make great money.
  applies_when: >-
    Warn owners in advance that churn will rise at first, so they keep doing the work.
  anchor: >-
    We would tell gym owners to expect churn to increase at first. But as long as they do
  source: >-
    playbook-retention.md, The 5 Horsemen Of Retention: Results, lines 149-167
  confirmations: 1
  demonstrates: >-
    The 5 Horsemen of Retention and the expected shape of the result curve after a retention
    push.
  anchor_at: "playbook-retention.md:163"
- id: C-playbooks-growth-021
  type: case
  name: >-
    The price, churn and LTV table
  statement: >-
    The same product at three prices with 100 clicks each: $10 converts 5% for 5 sales, 10%
    churn, $100 LTV, $500 total; $20 converts 4% for 4 sales, 10% churn, $200 LTV, $800 total;
    $100 converts 2% for 2 sales, 33% churn, $300 LTV, $600 total. The $20 point wins, and the
    next tests go between $20 and $100, around $39 to $59.
  why: >-
    Price affects both conversion rate and churn, and they do not suffer proportionally: if you
    can double your price and close 20% fewer deals with all else equal, you should.
  authors_caveat: >-
    The price in the example does not matter, only the relationship between the numbers; and
    across the Skool platform the higher the price, the higher the churn. The same table appears
    in Pricing and in Price Raise - it is one place, not two.
  anchor: >-
    So what’s the best price? The $20 price point. Now, we’d probably test more prices be-
  source: >-
    playbook-retention.md, Price, Value, And Churn - Relationship Between Price and Churn, lines 228-247
  confirmations: 1
  demonstrates: >-
    The best price is the one that produces the most sales at the highest LTV, which is found by
    testing rather than by reasoning.
  anchor_at: "playbook-retention.md:241"
- id: C-playbooks-growth-022
  type: case
  name: >-
    The newsletter that got worse as it got bigger
  statement: >-
    A friend running a $500k-per-month newsletter had his lowest churn while delivering two
    things: one Q&A call a month held until every question was answered, and one long physical
    newsletter a month. He then went to weekly calls and added other things - and everything he
    added increased churn. Gym Launch is on its 10th version, each shorter and simpler than the
    last, for the same reason.
  why: >-
    Overwhelm is the number one reason for churn; retention comes down to making sure customers
    consume the value, not to burying them in it. Think value per second, not seconds of value.
  anchor: >-
    I added all these other things...but everything I added increased churn.” Moral of the story:
  source: >-
    playbook-retention.md, Provide On-Going Value To Get On-Going Customers, lines 257-270
  confirmations: 2
  demonstrates: >-
    Deciding on the core 2-3 things you deliver and making them really good; there is wisdom in
    deletion.
  anchor_at: "playbook-retention.md:262"
- id: C-playbooks-growth-023
  type: case
  name: >-
    The Gym Launch competitor who sold the same and earned 70x less
  statement: >-
    A competitor sold just as many people at about the same cost to acquire a customer, running
    ads to everyone in fitness. The author targeted only the people with the highest chance of
    staying longest, identified by taking the common factors of the top 20% of customers and
    using them to qualify prospects ahead of time. First-year customer worth: $5,000 for the
    competitor, $42,000 for the author - 70x more profit.
  why: >-
    One of the highest leverage things you can do in a business is simply serve better
    customers: find those people, price appropriately, ignore the rest.
  anchor: >-
    sell just as many people as we did. But I would make 70x more profit. His cost to
  source: >-
    playbook-retention.md, Churn Checklist #1 - Bonus: Update your messaging, lines 403-410
  confirmations: 1
  demonstrates: >-
    Churn Checklist #1 - after finding who your best customers are, update the messaging so the
    ads select for them.
  anchor_at: "playbook-retention.md:404"
- id: C-playbooks-growth-024
  type: case
  name: >-
    Gym Launch onboarding and The Fast Cash Play
  statement: >-
    Churn sat at 8% and the target was 4%. Asking "When do people first get value from the
    product?" showed that leavers never made their investment back quickly while the
    longest-staying customers made it back in the first 30 days. So The Fast Cash Play was
    created and every client was pushed to recoup their investment inside 30 days. Churn went
    from 8% to 3% within 6 months.
  why: >-
    Activation points are the leading indicators of retention and have the greatest effect on
    churn, so finding them is the top priority.
  anchor: >-
    first 30 days. So we created what we called “The Fast Cash Play” and pushed every
  source: >-
    playbook-retention.md, Churn Checklist #1 - Bonus: Update your messaging, lines 411-421
  confirmations: 1
  demonstrates: >-
    Churn Checklist #1 - find the activation point and rebuild onboarding to drive customers to
    it. Common activation points: first leads for a B2B service, first login and dashboard for
    software, first use for a consumable.
  anchor_at: "playbook-retention.md:419"
- id: C-playbooks-growth-025
  type: case
  name: >-
    What the best communities on Skool do at onboarding
  statement: >-
    Their onboarding moves: tell the new member to make a post with a specific structure and
    comment on 1-2 other posts; tell them where to start; connect 4-6 people to each other right
    after onboarding so they already know someone; tell them what unlocks once the homework gets
    them to level 3; and show them what to cancel or stop paying for to free up the money for
    this membership, as homework they report back on.
  why: >-
    Onboarding here means teaching customers how to hit the activation points you investigated;
    the author has never run this checklist without churn going down.
  anchor: >-
    Show them what to cancel or do to save the money for this membership.
  source: >-
    playbook-retention.md, Churn Checklist #2: Onboard Your Customers, lines 450-463
  confirmations: 1
  demonstrates: >-
    Churn Checklist #2 - onboarding means teaching customers how to hit the activation point,
    reselling the value inside their goals, and setting up when you will speak next.
  anchor_at: "playbook-retention.md:462"
- id: C-playbooks-growth-026
  type: case
  name: >-
    Author Note: Real Life Outcome - group to one-on-one onboarding
  statement: >-
    A portfolio company went first from no onboarding to group onboarding, then after a year and
    change to one-on-one onboarding, which was hard because it is a huge volume business. It
    gave a 25% boost in ascensions; the higher LTV let them scale ad spend, and it was one of the
    largest contributing factors to going from $2M per month to $2M per week.
  why: >-
    The more personalized the onboarding, the better: custom outperforms generic, personal
    outperforms group, live outperforms recorded, and some beats none.
  anchor: >-
    one (not easy because it’s a huge volume business). We did and it gave us a 25%
  source: >-
    playbook-retention.md, Churn Checklist #2 - Author Note: Real Life Outcome, lines 490-496
  confirmations: 1
  demonstrates: >-
    Churn Checklist #2 - the onboarding quality ladder, and doing one-on-one onboarding for
    expensive offers.
  anchor_at: "playbook-retention.md:493"
- id: C-playbooks-growth-027
  type: case
  name: >-
    How Skool incentivizes activation
  statement: >-
    The unlockables Skool uses: courses that unlock, one-to-one consulting calls or bundles of
    calls at a certain duration or status, tickets to a live or virtual event, access to a higher
    tier of calls, custom badges and profile images that mark someone as "in", and free lifetime
    access at level 8, a very hard level to attain.
  why: >-
    The vast majority of host cancellations come from the bottom two tiers of engagement, so the
    more a customer uses the product, the longer they stay.
  anchor: >-
    At level 8, (a very hard level to attain) they give members free lifetime access.
  source: >-
    playbook-retention.md, Churn Checklist #3: Incentivize Customer Activation, lines 509-516
  confirmations: 1
  demonstrates: >-
    Churn Checklist #3 - make it worth the customer's while to do the things the perfect
    customer does.
  anchor_at: "playbook-retention.md:516"
- id: C-playbooks-growth-028
  type: case
  name: >-
    An unlock placed just past the churn point
  statement: >-
    Incentives are also timed rather than earned: if most customers leave after the third month,
    something cool unlocks on month 4, which retains the customers sitting on the edge.
  why: >-
    By putting some incentives just after major churn points you retain more of the customers
    sitting on the edge - easy and effective.
  anchor: >-
    Ex: If most customers leave after the third month, put something cool that
  source: >-
    playbook-retention.md, Churn Checklist #3: Incentivize Customer Activation, lines 517-521
  confirmations: 1
  demonstrates: >-
    Churn Checklist #3 - putting incentives just after major churn points, and staggering later
    unlocks past the average lifespan.
  anchor_at: "playbook-retention.md:520"
- id: C-playbooks-growth-029
  type: case
  name: >-
    From one-on-one to one-on-six onboarding
  statement: >-
    A woman running a Skool group moved from one-on-one onboarding to one-on-six - not to make
    it less personalized, but to introduce members to each other deliberately during onboarding.
    The result was low churn.
  why: >-
    It is easy to quit a membership and hard to leave a relationship; connecting members to each
    other scales better than one tie to you.
  anchor: >-
    to intentionally connect people and introduce them to each other. As a
  source: >-
    playbook-retention.md, Churn Checklist #4: Community Linking, lines 542-545
  confirmations: 1
  demonstrates: >-
    Churn Checklist #4 - community linking through group events, manual introductions, a
    community podcast and elevating micro-celebrities.
  anchor_at: "playbook-retention.md:544"
- id: C-playbooks-growth-030
  type: case
  name: >-
    Correcting bad customers inside a Skool group
  statement: >-
    The moves: delete bad posts and tell the poster why they sucked and what good looks like;
    three strikes on bad posters; pin the best 1-2 new posts daily, which elevates those members,
    gives everyone fresh value and signals what gets rewarded; and give the group four post
    categories - wins (which become testimonials), fun, discovered (shared with data and proof),
    and meetups.
  why: >-
    Bad customers make it bad for everyone else, while pinning the best posts elevates those
    members, gives everyone fresh value and signals to the group what kind of content gets
    rewarded.
  anchor: >-
    Delete bad posts and tell people why they sucked and tell them what good looks
  source: >-
    playbook-retention.md, Churn Checklist #5: Correct or Fire Bad Customers, lines 561-574
  confirmations: 1
  demonstrates: >-
    Churn Checklist #5 - incentivize good behaviour in public, eliminate bad behaviour with a
    stated standard and a strike count.
  anchor_at: "playbook-retention.md:561"
- id: C-playbooks-growth-031
  type: case
  name: >-
    Big head, long tail
  statement: >-
    A one-time charge priced on one-time value plus a recurring charge priced on consumable
    value: $6,800 up front for education or setup, then $199 a month for the community and
    everything after. The base keeps stacking, and 30 months of the $199 takes LTV from $6,800 to
    $12,800. The recurring fee must be included with the up-front fee rather than sold as a
    second purchase, or the price anchor that drives the retention is lost.
  why: >-
    The one-time part is priced on one-time value and the recurring part on consumable value, so
    both are appropriately priced and the base keeps stacking.
  anchor: >-
    upfront for education or a setup fee, then $199 for the community and
  source: >-
    playbook-retention.md, Churn Checklist #6: Add Annual Payment Options, lines 600-609
  confirmations: 1
  demonstrates: >-
    Churn Checklist #6 - match the pricing model to the business model; customers who pay for
    longer stay longer.
  anchor_at: "playbook-retention.md:605"
- id: C-playbooks-growth-032
  type: case
  name: >-
    Agency example from $100M Offers, with a one-time setup fee
  statement: >-
    Same $10,000 of ad spend and 300,000 impressions on both sides. Commodity offer: 40
    appointments booked, 75% show rate, 30 shown, 16% close, 5 sales at $1,000 = $5,000, ROAS
    0.5:1. Grand Slam offer: 2.5x the response rate, so 100 booked and 75 shown at the same show
    rate, 37% close, 28 sales at $3,997 = $112,000, ROAS 11.2:1 - 22.4x the cash collected up
    front.
  why: >-
    The better offer is more appealing, so more respond, and carries more value, so more buy -
    the same spend moves through both multipliers.
  anchor: >-
    Agency example from $100M Offers with a one-time setup fee:
  source: >-
    playbook-retention.md, Churn Checklist #6: Add Annual Payment Options, lines 621-645
  confirmations: 1
  authors_caveat: >-
    The author carries this table over from $100M Offers; it is quoted here to show a one-time
    setup fee working alongside recurring revenue.
  demonstrates: >-
    Churn Checklist #6 - a big one-time fee plus a smaller recurring charge, and what a better
    offer does to response, close rate and cash collected up front.
  anchor_at: "playbook-retention.md:621"
- id: C-playbooks-growth-033
  type: case
  name: >-
    The cancellation call, move by move
  statement: >-
    About half the people who take the call say no, and their feedback is the payoff. The other
    half are saved one of two ways: with a redo - let me give it another shot and I will make it
    right - or with an upsell into the higher program they should have been sold into, crediting
    what they already paid. In text or email the move is to invite the venting, get more upset
    than they are, validate completely, and then ask whether they would be happy if those things
    were fixed, which turns their complaint into a roadmap. They are also told what they lose by
    leaving: custom URLs, posts, access, founder pricing.
  why: >-
    You can usually save half of the people who will hop on a cancellation call, and the chances
    of saving them on a call are higher than in email or text.
  applies_when: >-
    Set the expectation that you do cancellation calls when the customer is onboarded; for
    high-volume low-price businesses a cancellation video that resells them and names what they
    lose can replace the call.
  anchor: >-
    Save with a redo .“Let me give it another shot and I’ll make it right.”
  source: >-
    playbook-retention.md, Churn Checklist #7: Exit Interviews or Cancellation Videos, lines 656-675
  confirmations: 2
  demonstrates: >-
    Churn Checklist #7 and Horseman 5 exit interviews - find the expectation that was unmet and
    see if you can meet it.
  anchor_at: "playbook-retention.md:660"
- id: C-playbooks-growth-034
  type: case
  name: >-
    The Fast Cash Play built against the tax bills
  statement: >-
    Gym Launch clients started cancelling because unexpected tax bills had eaten the money they
    had made. A grand opening giveaway idea was converted into a high-ticket offer, sized from
    the clients' own numbers at 5-10 people at $5,000 each; sales training for the offer was
    bundled in because most owners had never sold anything expensive; Sunday training slots were
    cleared to hold the high-ticket clients; the promotional materials were written the same day
    and taught on a call the next; and everyone who had recently cancelled was invited to that
    call.
  why: >-
    Revenue is vanity, profit is sanity, cash is reality - as long as you have cash you are
    still in business.
  anchor: >-
    I first saw it as a giveaway, but I think we could easily make it a high ticket offer. Looking
  source: >-
    playbook-fast-cash.md, Start Here, lines 78-100
  confirmations: 1
  demonstrates: >-
    Fast Cash Plays - a limited, high-ticket, high-touch offer to the warmest audience, launched
    within days, with the sales enablement shipped alongside it.
  anchor_at: "playbook-fast-cash.md:79"
- id: C-playbooks-growth-035
  type: case
  name: >-
    What the first Fast Cash Play collected
  statement: >-
    Within a few days the average business had collected an extra $30,000 in cash. Many owners
    chickened out and priced the offer at $3,000; the few who held the $5,000 price raked in
    $50k or more. The cancelling gyms renewed and came back into good standing, and owners with
    cash left over were told to prepay the rest of their year.
  why: >-
    The price is set high deliberately to select for the people with the purchasing power to
    take it; the only thing that should shock them as much as the price is the value that goes
    with it.
  anchor: >-
    “Nah, a lot of them chickened out and sold it for $3000 But the few who did $5000 all
  source: >-
    playbook-fast-cash.md, Start Here, lines 104-117
  confirmations: 1
  demonstrates: >-
    Price like you mean it - the same play at a lower price collects far less; and a cash play
    doubles as a retention save.
  anchor_at: "playbook-fast-cash.md:108"
- id: C-playbooks-growth-036
  type: case
  name: >-
    B2C Fast Cash Offer - Fitness, $10,000
  statement: >-
    Core: a one-on-one year-long "Total Transformation" package - tailored supplements, meals,
    workouts, a photoshoot. Bonus 1: a nutrition plan designed for a year plus an introduction to
    a meal prep company that delivers food to that plan. Bonus 2: workouts with you one-on-one
    three times per week. Bonus 3: 24/7 personal cell phone access.
  why: >-
    The unscalable components are exactly what justifies the crazy high price tag, so they go in
    rather than being cut.
  anchor: >-
    Offer: 1 on 1 Year Long “Total Transformation” Package. Aka “Look like a Greek
  source: >-
    playbook-fast-cash.md, Ultra-Premium Examples, lines 392-400
  confirmations: 1
  demonstrates: >-
    One to three core components plus three bonuses, assembled from unscalable value - attention,
    personalization, convenience, duration, experience, access.
  anchor_at: "playbook-fast-cash.md:393"
- id: C-playbooks-growth-037
  type: case
  name: >-
    B2B Fast Cash Offer - Marketing Agency, $50,000 per year
  statement: >-
    Core: a one-year "Personal Brand Explosion" - script, film, edit and post all content, four
    times a year. Bonus 1: an additional social media platform. Bonus 2: lead magnet creation.
    Bonus 3: an organic funnel built with video sales letters to convert maximum leads.
  why: >-
    One to three core components and three bonuses are kept separate so the bonuses can be
    layered in one at a time, each one widening the price-to-value discrepancy.
  anchor: >-
    B2B Fast Cash Offer - Marketing Agency. Price: $50,000 per year.
  source: >-
    playbook-fast-cash.md, Ultra-Premium Examples, lines 401-406
  confirmations: 1
  demonstrates: >-
    The same core-plus-three-bonuses skeleton carried into a business-to-business offer, with the
    bonuses kept separable so they can be dropped into the promotion one at a time.
  anchor_at: "playbook-fast-cash.md:401"
- id: C-playbooks-growth-038
  type: case
  name: >-
    Recurring Max Cash Offer
  statement: >-
    Priced at the monthly price times twelve, the offer is "1 Year to [ULTIMATE RESULT]" with
    three bonuses: custom work on the thing they struggle with, something that makes it faster
    for them, and something that makes it virtually guaranteed they achieve it - which is not a
    guarantee. Sold to the existing customer base, it is additional value for prepaying the
    year, and typically little else beyond the bonuses is needed to get 10% to say yes.
  why: >-
    It gives the existing base additional value for prepaying the year, which is why the author
    says the offer does exceptionally well and recommends it highly.
  anchor: >-
    you need to offer little else beyond the bonuses to get 10% to say yes. Highly, highly
  source: >-
    playbook-fast-cash.md, Ultra-Premium Examples, lines 407-420
  confirmations: 1
  demonstrates: >-
    10x the 10% applied to an existing base through annual prepay rather than through a new
    product.
  anchor_at: "playbook-fast-cash.md:419"
- id: C-playbooks-growth-039
  type: case
  name: >-
    ROI Benchmarks for a quarterly cash calendar
  statement: >-
    A gym doing $25,000 a month in recurring revenue - 166 members at $150 - on 25% margins
    makes $6,250 a month, $75,000 a year. Four Fast Cash Plays: Q1 10 buyers at $6,000 =
    $60,000 and 3 new customers; Q2 13 at $5,000 = $65,000 and 2; Q3 8 at $6,000 = $48,000 and
    1; Q4 14 at $4,000 = $56,000 and 2. Total extra cash $229,000: revenue goes from $300,000 to
    $529,000 and net income from $75,000 to $281,000 - a 76% revenue increase that quadruples
    net income and adds 22 customers. (2025 figures.)
  why: >-
    Fast Cash Plays run at least 90% gross margins and the leads are already paid for, so the
    additional revenue drops almost entirely to the bottom line; in the early days they were
    ~15% of annual revenue and nearly half of profit.
  authors_caveat: >-
    If twelve weeks feels too short a cooldown between promotions, run it twice a year instead.
  anchor: >-
    recurring revenue from a gym with 166 members paying $150 per month. A gym like that
  source: >-
    playbook-fast-cash.md, ROI Benchmarks, lines 476-496
  confirmations: 1
  demonstrates: >-
    Running Fast Cash offers every 90 days, and why a small share of revenue can be a large
    share of profit.
  anchor_at: "playbook-fast-cash.md:479"
- id: C-playbooks-growth-040
  type: case
  name: >-
    The announcement email, six days out
  statement: >-
    Skeleton of the announcement in the sample campaign: a short promise to get them to their
    goal faster, easier and cheaper; a declared selfish reason - an investment the sender was
    going to make anyway - with three benefits of that investment for the customer; the deal
    framed as thanks for their support, capped at ten customers, with a named expiry day and
    hour; what the first ten get, savings plus premium speed, ease and access features other
    customers will not get; the exchange asked for, prepaying the year; two ways to act, a
    booking link or a reply authorising the charge; and a PS repeating the cap and the deadline,
    whichever comes first.
  why: >-
    Texts draw attention to the emails and the emails give the details; the campaign is seven
    days because any longer loses urgency and any shorter misses sales.
  anchor: >-
    Main reason: Transparently, I want to invest in another [big expensive thing/person/vendor
  source: >-
    playbook-fast-cash.md, Sample Email And Text Sequence - Email 1: Monday 6 Days Out, lines 626-663
  confirmations: 1
  demonstrates: >-
    The promotion mechanics of a Fast Cash Play - scarcity, urgency, exclusivity, a reason why,
    and a single explicit action; the texts draw attention to the email, the email carries the
    details.
  anchor_at: "playbook-fast-cash.md:631"
- id: C-playbooks-growth-041
  type: case
  name: >-
    The last-day email that answers "I'll wait until the next one"
  statement: >-
    The final email names the objection it has been hearing and answers it in three beats - what
    if there is no next one, what if not acting now costs you the next step, and maybe the habit
    of waiting is why you are not where you want to be - then contrasts what people spend on
    phones and cars with what they spend on their goal, restates the hard expiry hour, and adds
    one more bonus for the last buyers before listing the whole stack again.
  why: >-
    Ideally you book and close everyone before the deadline, which is what drives the urgency of
    the deal.
  anchor: >-
    I’ve heard it from a few of you that are saying, «I’ll wait until the next one!» and I wanted to
  source: >-
    playbook-fast-cash.md, Sample Email And Text Sequence - Email 5: Saturday AM Last Day, lines 739-748
  confirmations: 1
  demonstrates: >-
    Handling the deferral objection inside the sequence, and layering a further bonus at the
    close to push the last spots.
  anchor_at: "playbook-fast-cash.md:741"
- id: C-playbooks-growth-042
  type: case
  name: >-
    The founder who made five ads a month
  statement: >-
    A portfolio founder selling weight loss on Facebook at $200,000 a month said the market was
    saturated because past $5-8k a day in ad spend his cost to acquire customers shot through the
    roof. He was recording at least five new ads a month. The prescription: devote every Friday
    to advertising, find your best ads, chop them into hook, meat and CTA, make 50 more hooks and
    3-5 variations of the meat - 150 ads a week, 600 a month instead of 5. The company doubled in
    two quarters.
  why: >-
    He had not saturated Facebook, he had taken the low-hanging fruit and hit a wall with ad
    quality, not with the market; the better the ads, the bigger the audience they convert.
  anchor: >-
    do that, we’ll be making 150 ads per week. That means we’ll go from 5 ads a month to 600
  source: >-
    playbook-goated-ads.md, GOATed Ads, lines 48-83
  confirmations: 1
  demonstrates: >-
    The Ad Assembly Process - 50 hooks x 3-5 meats x 1-3 CTAs; ads are assembled in parts, not
    created whole.
  anchor_at: "playbook-goated-ads.md:66"
- id: C-playbooks-growth-043
  type: case
  name: >-
    Old Spice, the ad that was not capped
  statement: >-
    The author was not an Old Spice buyer. He saw the ads with the man on the horse, thought they
    were funny and started buying the product - and so did 70% of the market. That is an ad that
    was not capped: it was good enough to convert everyone.
  why: >-
    That is how you make ads that scale - you make better ads, and you only do that by making
    more, far more.
  anchor: >-
    started buying their stuff. And so did 70% of the market. That’s an ad that wasn’t capped. It
  source: >-
    playbook-goated-ads.md, GOATed Ads, lines 76-81
  confirmations: 1
  demonstrates: >-
    You scale ads by making better ads, and you only make better ads by making far more of them;
    the colder and larger the traffic, the more exceptional the creative must be.
  anchor_at: "playbook-goated-ads.md:79"
- id: C-playbooks-growth-044
  type: case
  name: >-
    XFast: one hook per level of awareness (B2C)
  statement: >-
    A weight loss shake written five ways. Most Aware, offer driven: a new formula with 25% more
    protein and the same great taste. Product-Aware, proof driven: why 9 out of 10 users reached
    their goal weight within 3 months. Solution-Aware, promise driven: lose 15 pounds in 30 days
    with a scientifically proven meal replacement system. Problem-Aware, pain driven: frustrated
    with crash diets that don't last, there is a sustainable way. Completely Unaware, curiosity
    driven: the hidden hormonal imbalance making 1 in 3 Americans gain weight.
  why: >-
    Hooks that keep focusing on your offer or your proof convert a small slice of a larger
    audience very well; to grab a bigger slice you have to meet the audience where they are.
  applies_when: >-
    When existing ad capacity is capped and refreshed creative is not enough, so the audience
    itself has to be widened.
  anchor: >-
    1) Most Aware: “XFast’s new formula: now with 25% more protein - Same great taste!”
  source: >-
    playbook-goated-ads.md, Writing Expansion Hooks To Enter New Markets, lines 287-307
  confirmations: 1
  authors_caveat: >-
    The five levels of awareness are Eugene Schwartz's (spelt "Swartz" at line 98); the author
    says he has never met these people, labels are clean and reality is messy, and he uses a
    continuous version of the model.
  demonstrates: >-
    Writing expansion hooks by meeting each awareness level where it is - offer, proof, promise,
    pain, curiosity.
  anchor_at: "playbook-goated-ads.md:290"
- id: C-playbooks-growth-045
  type: case
  name: >-
    Digital Boost: one hook per level of awareness (B2B)
  statement: >-
    A marketing agency written five ways: social media management at 20% off for new clients;
    see how the agency increased ROI by 150% for 5 different industries; double your online
    sales in 6 months with data-driven marketing strategies; is your website getting sales, you
    might be missing these crucial elements; the unexpected way your business is losing
    thousands each month in untapped revenue.
  why: >-
    Hooks that keep focusing on your offer or your proof convert a small slice of a larger
    audience very well; to grab a bigger slice you have to meet the audience where they are.
  anchor: >-
    2) Product-Aware: “See how Digitalboost increased Roi by 150% for 5 different industries”
  source: >-
    playbook-goated-ads.md, Writing Expansion Hooks To Enter New Markets, lines 310-330
  confirmations: 1
  authors_caveat: >-
    The five levels of awareness are Eugene Schwartz's (spelt "Swartz" at line 98).
  demonstrates: >-
    The same awareness ladder carried into business-to-business hooks.
  anchor_at: "playbook-goated-ads.md:317"
- id: C-playbooks-growth-046
  type: case
  name: >-
    The $5 Foot Long by Subway
  statement: >-
    A national ad with a killer offer-driven hook that ran for 20 years works only because the
    entire nation already knows the brand and knows what a sandwich is, after hundreds of
    millions spent getting them there. A no-name competitor with a product people need educating
    about, leading with an offer-driven hook to a national audience, is the closest thing to
    burning money on fire.
  why: >-
    The awareness levels are frameworks rather than a magical recipe: a wide, curiosity-driven
    piece can also convert a warm audience, as a movie trailer does.
  applies_when: >-
    If 90% of your hooks land in the Most Aware bucket, spread them out; when in doubt, go a
    little broader, since you still catch the warm audience.
  anchor: >-
    see a national ad that has a killer offer-driven hook. Like the $5 Foot Long by Subway
  source: >-
    playbook-goated-ads.md, Writing Expansion Hooks To Enter New Markets, lines 339-351
  confirmations: 1
  demonstrates: >-
    The boundary on offer-driven hooks: they need a known brand and a known product to work on a
    cold, broad audience.
  anchor_at: "playbook-goated-ads.md:340"
- id: C-playbooks-growth-047
  type: case
  name: >-
    A CTA taken apart element by element
  statement: >-
    One call to action split into its parts: what to do - take advantage of this great offer by;
    how to do it - tapping the button on the bottom of your screen; when to do it - before it
    expires; what they get for doing it - $1000 of free stuff; and, optionally, what happens next
    - delivered straight to your inbox. In video, each step is also demonstrated on screen.
  why: >-
    Showing as well as telling gives the ultimate congruence: when they click and get exactly
    what they expected, they are likelier to follow through.
  applies_when: >-
    What happens next matters more with lead magnets and multi-step sales processes.
  anchor: >-
    How to do it: tapping the button on the bottom of your screen…
  source: >-
    playbook-goated-ads.md, CTA - Call To Action, lines 533-545
  confirmations: 2
  demonstrates: >-
    A good CTA shows or tells what to do, how to do it, when to do it, what they get for doing
    it, and what happens next; clear beats clever.
  anchor_at: "playbook-goated-ads.md:539"
- id: C-playbooks-growth-048
  type: case
  name: >-
    Testing three CTAs on a 14-day free trial
  statement: >-
    To find a CTA, run three identical hook-plus-meat combinations to the same audience and
    change only the CTA: "Start free on the next page", "Grab your 14-day free trial on the next
    page", "Get started on the next page free". Once one or two work, stick with them.
  why: >-
    CTAs take the least effort of the three parts and get about none of the prep time; a sound
    CTA has never broken a campaign, but having no CTA has.
  anchor: >-
    to figure it out is run three identical hook + ad meat combinations, to the same audience,
  source: >-
    playbook-goated-ads.md, CTA - Call To Action, lines 549-561
  confirmations: 1
  demonstrates: >-
    Isolating one variable to test it, and the 80% hooks / 20% meat / ~0% CTAs split of
    preparation time.
  anchor_at: "playbook-goated-ads.md:550"
```
