# Улов фазы 1 — $100M Playbooks: Lead Nurture, Retention, Fast Cash, GOATed Ads (2025) (ярус 2), тип A: фреймворки

Группа `tier2-playbooks-growth`, слаг `playbooks-growth`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **48** (экстрактор вернул 48, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `playbook-lead-nurture.md` | 1–1148 | 2 | 15 |
| `playbook-retention.md` | 1–835 | 2 | 16 |
| `playbook-fast-cash.md` | 1–779 | 2 | 9 |
| `playbook-goated-ads.md` | 1–707 | 1 | 8 |

## Как собран файл

Экстрактор A (Frameworks) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-playbooks-growth.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-playbooks-growth-A.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 1 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: A-playbooks-growth-001
  type: framework
  name: >-
    Four Pillars of Lead Nurture
  statement: >-
    Show-ups have four drivers, and lead nurture is built by working all four: availability, speed to contact, personalization, volume.
  why: >-
    If you reach out the moment they express interest, make it convenient for them to talk, frame the conversation as beneficial to them, and do it as many times as you can, more people will schedule and show up to buy your thing, no matter what you sell.
  applies_when: >-
    Maximizing 30-day show rates, after advertising and before sales.
  structure:
    - >-
      Availability: The number of open appointment slots you have.
    - >-
      Speed to contact: How fast you respond to leads and how far out you let them schedule appointments.
    - >-
      Personalization: Making communication with leads useful and relevant to them.
    - >-
      volume: The number of times you reach out to leads before giving up.
  anchor: >-
    generate upwards of 20,000 leads a day), show-ups have four main drivers:
  source: >-
    playbook-lead-nurture.md, Four Pillars of Lead Nurture, lines 224–250
  confirmations: 3
  anchor_at: "playbook-lead-nurture.md:227"
- id: A-playbooks-growth-002
  type: framework
  name: >-
    The three dimensions of availability
  statement: >-
    Availability is measured on three axes at once — the number of days, the hours per day, and the time slots per hour — and their aggregate is the biggest predictor of throughput.
  why: >-
    On an absolute basis, businesses with the most time slots had the most schedules, shows, and purchases; one time slot will get fewer people to schedule and show than 100.
  structure:
    - >-
      The number of days
    - >-
      hours per day
    - >-
      time slots per hour
  anchor: >-
    The number of days, hours per day, and time slots per hour, in aggregate, is the
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability, lines 289–301
  confirmations: 2
  authors_caveat: >-
    There are diminishing returns, but large increases still at the upper quartiles of availability.
  anchor_at: "playbook-lead-nurture.md:292"
- id: A-playbooks-growth-003
  type: framework
  name: >-
    Availability tactics
  statement: >-
    Availability is raised with four tactics in this order: more days per week, more hours per day, more flexible start times within the hour, and all three booking routes (inbound, outbound, self-scheduling).
  why: >-
    More appointment availability means more people will show up to appointments to buy; the more ways you give people to book an appointment, the more people will book an appointment.
  structure:
    - >-
      Take Appointments More Days Per Week
    - >-
      Take Appointments More Hours Per Day
    - >-
      Give Leads More Flexible Appointment Times
    - >-
      Have Inbound, Outbound, and Self-Scheduling Options
  anchor: >-
    Take Appointments More Days Per Week: You pay your rent seven days per week.
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability, Tactics, lines 330–370
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:333"
- id: A-playbooks-growth-004
  type: framework
  name: >-
    Tips to make online schedulers work better
  statement: >-
    An online scheduler is built on three checks: a header that confirms the visitor is in the right place, visible dates and times on load, and the fewest possible steps.
  why: >-
    Eliminating friction will increase the number of appointments booked, and tech that eliminates fields leads already filled out creates huge improvements in schedule rates.
  applies_when: >-
    Building the self-scheduling page leads land on after opting in.
  structure:
    - >-
      Make sure the header confirms they’re in the right place. Then, tell them the next thing to do and why to do it. (Header - Headline - Subheadline)
    - >-
      Make available dates and times super obvious as soon as the page loads. You want the time slots to be visible. This goes for mobile and desktop.
    - >-
      Eliminate as many steps as possible. And if leads already gave you relevant info earlier in the scheduling process, don’t make them do it again.
  anchor: >-
    A few tips to make online schedulers work better:
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability, lines 371–384
  confirmations: 2
  authors_caveat: >-
    Sometimes you have too many bad appointments on your calendar. When that happens—it’s okay to add friction.
  anchor_at: "playbook-lead-nurture.md:371"
- id: A-playbooks-growth-005
  type: framework
  name: >-
    The three speeds
  statement: >-
    Speed is increased in three distinct places: speed to first contact, speed to first appointment, and speed of response between scheduling and the appointment.
  why: >-
    The faster you contact leads, the fewer times you have to contact them before they buy; and leads often make buying decisions before the sales call, which makes it the competitor’s sale to lose.
  structure:
    - >-
      Speed To First Contact
    - >-
      Speed To First Appointment
    - >-
      Speed Of response
  anchor: >-
    I increase speed in three ways.
  source: >-
    playbook-lead-nurture.md, Pillar II: Speed, How To Increase Speed To Contact, lines 432–437
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:433"
- id: A-playbooks-growth-006
  type: framework
  name: >-
    Five possible outcomes of a scheduling call
  statement: >-
    Every outbound call to schedule or confirm ends in one of five outcomes, each with its own next action.
  why: >-
    Show rates for same-day appointments are higher than not same day, and show rates for talking to them right now are 100%, so pulling appointments forward becomes the objective of the call.
  applies_when: >-
    Calling leads who self-scheduled, to confirm or to pull their appointment forward.
  structure:
    - >-
      Doesn’t respond. We would remove this person from the calendar (or double book if in-person).
    - >-
      Contacted and unqualified. remove from the calendar and give free useful stuff or references if you can. Or—if you have an appropriate downsell, you can offer it.
    - >-
      Contacted, qualified, and free right now. This is the best scenario. You’re guaranteed a show because you’re already talking to them.
    - >-
      Contacted, qualified, and pulled appointment forward.
    - >-
      Contacted, qualified, and appointment confirmed.
  anchor: >-
    So that becomes the objective. When we call to schedule people, we have
  source: >-
    playbook-lead-nurture.md, Pillar II: Speed, lines 486–500
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:488"
- id: A-playbooks-growth-007
  type: framework
  name: >-
    Six personalization tactics
  statement: >-
    Personalization raises show rates in six ways, applied in this order: preferred channel, qualification, routing to the best closers, segmented messaging, incentives, and proof.
  why: >-
    If the lead knows they’ll get value just for showing up, then their chance of showing up goes up with it; it lowers their risk and raises their opportunity cost.
  structure:
    - >-
      use The Lead’s Preferred Communication Method - Talking to leads where they want to talk.
    - >-
      Qualify The Leads - Collect data then remove leads from the calendar that are unlikely to buy, to free up time for those who are more likely to buy.
    - >-
      Best Leads to Best Closers - Connect the leads most likely to buy with the reps most likely to close.
    - >-
      Segment Your Messaging - Talk to leads about stuff relevant to them.
    - >-
      Incentivize Showing up - Give them a reason (or multiple reasons) to show up.
    - >-
      Demonstrate Proof - Show the successes and positive experiences of people just like them.
  anchor: >-
    I personalize to boost show rates in six ways. They are:
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, Personalization Tactics, lines 622–633
  confirmations: 3
  anchor_at: "playbook-lead-nurture.md:623"
- id: A-playbooks-growth-008
  type: framework
  name: >-
    Send The Best Leads To The Best Closers
  statement: >-
    Lead routing is built in five steps: study your best customers, ask those same questions up front, score the leads, route the best ones to the best closers, then collect the result.
  why: >-
    The number one rep wasted two-thirds of his time on unqualified people; when the best leads were given to him he 5x’d the production of the office, and the company went from $200M to $1B a year in sales over the next five years.
  structure:
    - >-
      Step 1 : Look at your best customers. The actions they take and the people they are (demographics).
    - >-
      Step 2 : Ask those questions in your opt-ins, applications, and during the time before sales appointments.
    - >-
      Step 3 : Score leads on a 1–5 or red-yellow-green system based on how qualified they are.
    - >-
      Step 4 : route your best leads to your best closers.
    - >-
      Step 5 : Enjoy the fruits of your labor.
  anchor: >-
    Step 4 : route your best leads to your best closers.
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, 3) Send The Best Leads To The Best Closers, lines 692–699
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:698"
- id: A-playbooks-growth-009
  type: framework
  name: >-
    Push and pull incentives
  statement: >-
    Incentives to show up come in two kinds: a push incentive given before they arrive to evoke reciprocity, and a pull incentive they receive after they arrive to motivate the action.
  why: >-
    Both are a kind of social contract; the push strategy hinges on reciprocity and works even when people know what you’re doing, and a pull choice makes them show you are incurring a cost on their behalf.
  structure:
    - >-
      A push incentive means they do the good stuff before they arrive with the intention to evoke reciprocity. Gift Card “Push” Incentive.
    - >-
      A pull incentive means the lead gets good stuff after they arrive with the intention to motivate the action. A/B “Pull” Incentive.
  anchor: >-
    I’ve  seen  incentives  used  in  two  ways:  “push”  and  “pull.”  A  push  incentive  means
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, 5) Incentives, lines 744–775
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:745"
- id: A-playbooks-growth-010
  type: framework
  name: >-
    A/B Incentives depend on three things
  statement: >-
    An A/B incentive works only when all three conditions hold: the lead wants the thing, it connects obviously to what you will offer, and you incurred real cost preparing it.
  why: >-
    Leads choose what they get when they show up, but both choices assume they’ll show — and the choice only binds if the thing is wanted, relevant and visibly paid for.
  applies_when: >-
    Designing the A/B choice offered to a scheduled lead before the appointment.
  structure:
    - >-
      First, leads should want the thing.
    - >-
      Second, it should have obvious connections to the thing you’ll offer them.
    - >-
      Last, that you incurred some real cost by preparing it.
  anchor: >-
    A/B Incentives depend on three things. First, leads should want the thing. Second, it
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, 5) Incentives, lines 779–781
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:779"
- id: A-playbooks-growth-011
  type: framework
  name: >-
    Volume in three parts
  statement: >-
    Volume splits into three separate reach-out jobs: scheduling appointments, reminding them to show, and booking the next appointment at the current one.
  why: >-
    Most communication attempts fail — a bad time, a forgotten reply, a message missed in the flurry — so reaching out again makes both business and ethical sense, because if they opted in, they asked to be contacted.
  structure:
    - >-
      Scheduling appointments
    - >-
      reminding them to show
    - >-
      Booking their next appointment when they show up for their current appointment
  anchor: >-
    of  reach-outs  to  get  more  responses,  schedules,  and  then  shows.  I  break  volume  into
  source: >-
    playbook-lead-nurture.md, Pillar IV: Volume, Description, lines 839–847
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:842"
- id: A-playbooks-growth-012
  type: framework
  name: >-
    The scheduling reach-out cadence
  statement: >-
    Reach-outs to a new lead run as an eight-step front-loaded cadence over the first week, then hand over to long-term nurture.
  why: >-
    The more days that pass, the less likely they’ll schedule. For that reason, we front-load the reach-outs.
  applies_when: >-
    From the moment a lead opts in until the appointment is scheduled.
  structure:
    - >-
      Call leads within 5min of opting in.
    - >-
      Double-dial. If you call once and get nothing, immediately call again.
    - >-
      If nothing, leave a voicemail.
    - >-
      Send a text immediately after you leave the voicemail.
    - >-
      Double dial and text two more times that day. Make sure to leave a few hours between each attempt.
    - >-
      Call two times for the next two days. Once earlier in the day and once later in the day. Text after the second call each day.
    - >-
      Call and text once a day for the next four days.
    - >-
      After the first week, I transition to long-term nurture.
  anchor: >-
    1) Call leads within 5min of opting in. Seriously, once you get this, you will see an
  source: >-
    playbook-lead-nurture.md, Pillar IV: Volume, 1) Scheduling Appointments, lines 848–874
  confirmations: 2
  authors_caveat: >-
    Steps 6 and 7 stay flexible, you can do it for more days or fewer. As always, follow the laws in your area.
  anchor_at: "playbook-lead-nurture.md:849"
- id: A-playbooks-growth-013
  type: framework
  name: >-
    Automated reminder cadence
  statement: >-
    Once an appointment is scheduled, four automated reminders go out — immediately, 24 hours before, 12 hours out, and 3 hours from the appointment — and they are declared as automated.
  why: >-
    People don’t mind reminders. They do mind being lied to. And if you follow the speed pillar you don’t need to send that many anyway.
  structure:
    - >-
      Immediately: Automatic confirmation of time, date, number you’ll be calling from, and person they’re meeting with.
    - >-
      24 hours before.
    - >-
      12 hours out.
    - >-
      3 hours from the appointment.
  anchor: >-
    Once you get the person scheduled, or they automatically schedule themselves, send
  source: >-
    playbook-lead-nurture.md, Pillar IV: Volume, 2) Reminding Them To Show, lines 884–899
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:886"
- id: A-playbooks-growth-014
  type: framework
  name: >-
    Non-monetary good stuff
  statement: >-
    Rewards for the behaviors that produce show rates split into money and non-money, and the non-monetary half falls into three categories: attention, affection, and approval.
  why: >-
    Kudos, asking what they did, and the team’s little -isms reinforce the right behaviors, while a rep with a high close rate who doesn’t work their leads is seen as entitled and wasteful.
  applies_when: >-
    Building a culture of execution around lead nurture.
  structure:
    - >-
      money: Include a small commission bump for show-up rates, usually in the neighborhood of 5–30% of what a salesman makes on a sale.
    - >-
      attention
    - >-
      affection
    - >-
      approval
  anchor: >-
    Non-monetary good stuff falls into three categories: attention, affection, and approval.
  source: >-
    playbook-lead-nurture.md, Execution, Tactics, lines 1039–1050
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:1043"
- id: A-playbooks-growth-015
  type: framework
  name: >-
    Track and rank three sales metrics
  statement: >-
    The team is ranked on three lists at once — show rate, close rate, and total call-to-close percentage — because the first measures work ethic and the second measures skill.
  why: >-
    The only thing that actually matters is the conversion rate on the leads you’ve got, and that takes everything into account, so you might as well take everything into account when paying and giving status to your team.
  structure:
    - >-
      show rate
    - >-
      close rate
    - >-
      total call-to-close percentage
  anchor: >-
    Track and rank: show rate, close rates, and lead-to-close ratio by sales rep.
  source: >-
    playbook-lead-nurture.md, Execution, Tactics and Lead Nurture Checklist, lines 1051–1063, 1140
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:1140"
- id: A-playbooks-growth-016
  type: framework
  name: >-
    A very particular process for solving problems
  statement: >-
    An unfamiliar problem is solved in three steps: ask several experts about it, collect all their answers, then find the common threads.
  why: >-
    Talking to people who already know your problem gets you solutions faster than doing it all on your own, and talking to as many as you can helps eliminate bias and reveals the core problem.
  applies_when: >-
    Learning more about a complex problem than the people who have been doing it their whole careers.
  structure:
    - >-
      Ask experts (plural) about the problem.
    - >-
      Get all their answers.
    - >-
      Find common threads to solve the problem.
  anchor: >-
    something we did was working. We had a very particular process for solving problems. It went
  source: >-
    playbook-retention.md, Solving Problems Like The Big Boys, lines 78–104
  confirmations: 2
  authors_caveat: >-
    The last part can get tricky: if every expert lists 5 factors but the same 2 pop up each time across all of them, solve for those.
  anchor_at: "playbook-retention.md:83"
- id: A-playbooks-growth-017
  type: framework
  name: >-
    The 5 Horsemen of Retention
  statement: >-
    Gym retention is built on five activities found as common factors among the lowest-churn owners: track attendance, reach out twice a week, handwritten cards, member events, exit interviews.
  why: >-
    They were the common factors among gym owners with less than 3% month-over-month churn for the last 6 months; a reduction in churn from 9% to 3% is a 3.3x increase in lifetime value.
  structure:
    - >-
      Track attendance: If a member went to the gym three times per week or more, they would stick. If they went less than twice per week or less, they’d churn out.
    - >-
      Reach out 2x per week: Praising customers about their participation and progress goes a long way. Solving little problems they have does too. Do both.
    - >-
      Handwritten cards: Send hand-written cards when they sign up, when you ask for referrals at three, six, twelve month milestones.
    - >-
      Member events: Hold regular events on an internal calendar. Keep them regular to you and random to them. Every 21, 42, or 63 days is a good cadence.
    - >-
      Exit interviews: If a person says they want to leave then talk to them before they do.
  anchor: >-
    I found 5 common factors – which became The 5 Horsemen of Retention.
  source: >-
    playbook-retention.md, The 5 Horsemen of Retention, lines 101–140
  confirmations: 2
  authors_caveat: >-
    Expect churn to increase at first — Month 1: churn UP by 50%, which the author calls “shaking the three” — before it falls in months 2 and 3.
  anchor_at: "playbook-retention.md:104"
- id: A-playbooks-growth-018
  type: framework
  name: >-
    What can I do to churn 100% of my customers?
  statement: >-
    Retention is designed by inversion: list everything that would make customers leave, then do the exact opposite of each item.
  why: >-
    If you can keep the value customers get greater than the price they pay, customers will stick; asking what would make them leave produces the list faster than asking how to retain them.
  structure:
    - >-
      Talk with them
    - >-
      Keep your promises
    - >-
      Communicate clearly
    - >-
      Treat them like royalty
    - >-
      Set realistic expectations
    - >-
      Give them status updates
    - >-
      Connect them with other happy customers
    - >-
      Make it as easy as possible for them to get the most value they can.
  anchor: >-
    Instead of asking “How should I retain all my customers?”, I ask “What would make
  source: >-
    playbook-retention.md, Price, Value, And Churn, lines 200–226
  confirmations: 1
  anchor_at: "playbook-retention.md:202"
- id: A-playbooks-growth-019
  type: framework
  name: >-
    The Churn Checklist
  statement: >-
    Churn reduction runs as a nine-step checklist applied in order, from activation points through to the customer journey.
  why: >-
    I have never not made more money by going through and applying this checklist. It works every time. And to be clear I don’t know which steps worked better than others, I just know that doing them all worked.
  applies_when: >-
    Starting work with a business that keeps losing customers; it is the exact checklist walked through with a new portfolio company.
  structure:
    - >-
      Figure out activation points
    - >-
      Onboard your customers
    - >-
      Incentivize customer activation
    - >-
      Community linking / events
    - >-
      Fire or Correct Bad Customers
    - >-
      Add Annual Pricing Options
    - >-
      Cancellation call/video
    - >-
      Survey Customers Regularly
    - >-
      Four-Step Customer Journey
  anchor: >-
    The churn checklist steps are as follows:
  source: >-
    playbook-retention.md, Churn Checklist, lines 337–355; Action Steps Summary, lines 788–835
  confirmations: 2
  authors_caveat: >-
    Not all of these will apply to your business. So if you find one and think “That won’t work for me” - you might be right - but many of them will.
  anchor_at: "playbook-retention.md:340"
- id: A-playbooks-growth-020
  type: framework
  name: >-
    How to find your activation point
  statement: >-
    The activation point is found in five moves: gather churned customers, keep those who stayed three months or longer, order them by spend and take the top 20%, learn everything about them, then work out what they did and how you treated them.
  why: >-
    Activation points refer to leading indicators of customer retention, and they have the greatest effect on customer churn: if you find the stuff that keeps people from leaving, then you can do that stuff.
  structure:
    - >-
      Find your churned customers. Gather all the data you can about churned customers.
    - >-
      Find who stayed for 3 months or longer.
    - >-
      Order that list by who spent the most money. Take the top 20% of customers.
    - >-
      Learn everything you can about them. Look at demographics, psychographics, income, business size, revenue, and any other data you have.
    - >-
      Figure out how they used your stuff and how you treated them. Common factors become your activation-point candidates. Narrow it down to 5 factors and start working your way down the list.
  anchor: >-
    Here’s how to find your activation point:.
  source: >-
    playbook-retention.md, Churn Checklist #1: Figure Out Your Activation Points, lines 359–429
  confirmations: 2
  authors_caveat: >-
    Three months is a convention, but there is nothing special about three months. You can do whatever time you want. Retest every 6-12 months.
  anchor_at: "playbook-retention.md:374"
- id: A-playbooks-growth-021
  type: framework
  name: >-
    Onboarding guidelines
  statement: >-
    Onboarding format is chosen against five ranked comparisons, of which the last overrides the rest.
  why: >-
    Every time I have followed this checklist, churn goes down. I’ve never done it and it not work. The more personalized the onboarding, the better.
  structure:
    - >-
      Custom outperforms generic.
    - >-
      Personal outperforms group.
    - >-
      Live outperforms recorded.
    - >-
      Carrots outperform sticks.
    - >-
      Last, and most important, some beats none.
  anchor: >-
    Last, and most important, some beats none.
  source: >-
    playbook-retention.md, Churn Checklist #2: Onboard Your Customers, lines 439–447
  confirmations: 1
  anchor_at: "playbook-retention.md:447"
- id: A-playbooks-growth-022
  type: framework
  name: >-
    How I onboard customers
  statement: >-
    An onboarding session runs through five moves: outline how to get value and drive to the activation point, resell the purchase inside their goals, name what staying longer unlocks, set communication best practices, and follow up.
  why: >-
    Onboarding here means teaching customers how to hit the activation points, and the onboarding is used to establish long term communication: customers should always know when you’ll speak to them next.
  applies_when: >-
    Any new customer; the author also recommends doing it for sales prospects, which will increase your close rate.
  structure:
    - >-
      Outline how to get value → Drive them to the activation point
    - >-
      Resell the value of the purchase. Important! Frame it within the context of their goals.
    - >-
      Tell them how they can unlock more value as they stay longer
    - >-
      Tell them best practices to communicate with you, your team and other customers
    - >-
      Follow up.
  anchor: >-
    Resell the value of the purchase. Important! Frame it within the context of their
  source: >-
    playbook-retention.md, Churn Checklist #2: Onboard Your Customers, lines 448–484
  confirmations: 2
  anchor_at: "playbook-retention.md:464"
- id: A-playbooks-growth-023
  type: framework
  name: >-
    Incentivize customer activation
  statement: >-
    Activation is paid for with unlockables — courses, calls, event tickets, higher-tier access, status badges — and extra unlocks are timed to land just after the major churn points.
  why: >-
    A vast majority of Skool host cancellations come from people in the bottom two tiers of engagement; the more a customer uses Skool, the longer they stay a customer.
  structure:
    - >-
      Courses that unlock
    - >-
      1-1 consulting calls or bundles of calls once they reach a certain duration or status
    - >-
      Tickets to a live or virtual events
    - >-
      Access to another set of higher tier calls
    - >-
      Custom badges, profile images, and other indicators to say that they’re “in”.
    - >-
      By putting some incentives just after major churn points, you can retain more customers on the edge.
    - >-
      Time unlocks: put unlocks past average lifespan, then 30 days after, then 3 months later, then 3 months later.
  anchor: >-
    You figured out what the perfect customer does. You onboard all new customers to do
  source: >-
    playbook-retention.md, Churn Checklist #3: Incentivize Customer Activation, lines 497–525; Action Steps Summary, lines 799–803
  confirmations: 2
  anchor_at: "playbook-retention.md:498"
- id: A-playbooks-growth-024
  type: framework
  name: >-
    Community linking
  statement: >-
    Members are connected to each other rather than to you, through four moves: group events, manual introductions, a community podcast, and elevating micro-celebrities.
  why: >-
    It’s more scalable to facilitate multiple, deeper connections than one single tie to the group — it’s easy to quit a membership, it’s hard to leave a relationship.
  structure:
    - >-
      Group events
    - >-
      Manually connect people. If you think a member would benefit from knowing another member, connect them.
    - >-
      Start a community podcast. Interview members.
    - >-
      Elevate micro-celebrities within your community. You do this by calling them out in public channels and praising them for their specific area of expertise.
  anchor: >-
    Action Step: Host group events. Manually connect people. Start a community podcast.
  source: >-
    playbook-retention.md, Churn Checklist #4: Community Linking, lines 536–553
  confirmations: 2
  anchor_at: "playbook-retention.md:553"
- id: A-playbooks-growth-025
  type: framework
  name: >-
    Four topic categories: wins, fun, discovered, and meetups
  statement: >-
    A community's posting categories are set by you, and four of them are always included: wins, fun, discovered, and meetups.
  why: >-
    Wins give you testimonials. Fun keeps it light and lets people talk about whatever. Discovered gets people sharing with data and proof. Meetups gives people a place to connect on or offline.
  structure:
    - >-
      Wins give you testimonials.
    - >-
      Fun keeps it light and lets people talk about whatever.
    - >-
      Discovered: tell people to share what they’ve discovered using data and proof.
    - >-
      Meetups: gives people a place to connect on or offline.
  anchor: >-
    Make topic categories for what you want people to post. But include these four:
  source: >-
    playbook-retention.md, Churn Checklist #5: Correct or Fire Bad Customers, lines 568–574
  confirmations: 1
  anchor_at: "playbook-retention.md:568"
- id: A-playbooks-growth-026
  type: framework
  name: >-
    Add Annual Payment Options
  statement: >-
    Longer payment terms are offered in three forms: an annual billing option, a big one-time up-front with a small monthly, or a founder rate.
  why: >-
    Customers who pay for longer stays...stay longer. So, if customers want to stay longer, allow them to pay to stay longer.
  structure:
    - >-
      Annual billing option: typically 10-20% of people will take the annual option if you price at “buy 10 months get 2 free.”
    - >-
      Alternative One: Big upfront (1-time) with small monthly payments works well.
    - >-
      Alternative Two: Implement “founder rates” to convert more people and keep them longer. A 50% decrease is a great way to start.
  anchor: >-
    front with a smaller monthly. Alternatively, create a founders price which incentivizes people
  source: >-
    playbook-retention.md, Churn Checklist #6: Add Annual Payment Options, lines 582–651
  confirmations: 2
  authors_caveat: >-
    If you make annual mandatory (as in, the only way to pay), it will decrease sales. But, it will decrease churn as well.
  anchor_at: "playbook-retention.md:650"
- id: A-playbooks-growth-027
  type: framework
  name: >-
    Big head, long tail
  statement: >-
    A two-part price splits the offer: the big one-time fee is priced to the one-time value (education, implementation, setup) and the small recurring fee to the consumable value, both sold together in one purchase.
  why: >-
    The base continues to stack and you’ll likely have a high upsell rate, so LTV rises from $6,800 to $12,800 because you are appropriately priced.
  structure:
    - >-
      Make the big upfront thing something that has big one time value (education or one time implementation/setup). Price according to THAT value.
    - >-
      Then, make the recurring according to the consumable value (which may be far less).
    - >-
      Make sure to include the recurring fee WITH the 1-time up front fee and not make it a second sale.
  anchor: >-
    Example: I call this a “big head, long tail” where you might charge $6,800
  source: >-
    playbook-retention.md, Churn Checklist #6: Add Annual Payment Options, lines 600–620
  confirmations: 1
  authors_caveat: >-
    Otherwise, you lose the price anchor between the first big purchase and second small recurring that drives the retention.
  anchor_at: "playbook-retention.md:604"
- id: A-playbooks-growth-028
  type: framework
  name: >-
    Two ways to save a cancellation
  statement: >-
    Of the people who take a cancellation call, half are unsaveable and give feedback; the other half are saved either with a redo or with an upsell.
  why: >-
    You can usually save half of the people who will hop on a cancellation call, and the chances you’ll save them on a call are higher than in email or text.
  applies_when: >-
    A customer gives notice; the expectation of a cancellation call is set when they are onboarded.
  structure:
    - >-
      Save with a redo. “Let me give it another shot and I’ll make it right.”
    - >-
      Save with an upsell. You realize they need more help and should’ve been in your higher program. You credit their payment toward the higher program.
  anchor: >-
    stuff. The other half, you can save them in one of two ways:
  source: >-
    playbook-retention.md, Churn Checklist #7: Exit Interviews or Cancellation Videos, lines 656–691
  confirmations: 2
  anchor_at: "playbook-retention.md:659"
- id: A-playbooks-growth-029
  type: framework
  name: >-
    The two-question survey
  statement: >-
    Twice a year, customers are shown the full list of what you provide and asked one keep question and one remove question.
  why: >-
    This helps you identify the core 2-3 things your product or service does, so you can do more of the stuff they like and cut the stuff they don’t.
  structure:
    - >-
      If I removed everything on this list but one, what would you want to keep the most?
    - >-
      If I kept everything on this list but one, which would bother you the least to see me remove
  anchor: >-
    removed everything on this list but one, what would you want to keep the most?” and fol-
  source: >-
    playbook-retention.md, Churn Checklist #8, lines 692–712
  confirmations: 2
  anchor_at: "playbook-retention.md:694"
- id: A-playbooks-growth-030
  type: framework
  name: >-
    The ACA framework
  statement: >-
    A regular one-on-one check-in with a customer follows three beats: acknowledge what you've seen them do, compliment them on something, ask a question.
  why: >-
    Reaching out to customers 1 on 1 every two to three weeks retained more people than never speaking with customers.
  applies_when: >-
    Between large surveys, and in lead nurture to qualify leads and pull appointments forward.
  structure:
    - >-
      Acknowledge what you’ve seen them do.
    - >-
      Complement them on something.
    - >-
      Ask a question.
  anchor: >-
    with customers. The subject of the reach out followed the ACA framework. Acknowl-
  source: >-
    playbook-retention.md, Churn Checklist #8, lines 700–703; Action Steps Summary, line 831; playbook-lead-nurture.md, Lead Nurture Checklist, line 1135
  confirmations: 3
  authors_caveat: >-
    Counterintuitively, the wealthier the customers, the less handholding they typically want.
  anchor_at: "playbook-retention.md:702"
- id: A-playbooks-growth-031
  type: framework
  name: >-
    Four-Step Customer Journey
  statement: >-
    Every customer is planned through four milestones — activate, testimonial, refer, ascend — with something given at each one.
  why: >-
    Customers get an itch to buy more stuff over time, and if someone just bought another thing from you, they’re the least likely to churn. They’re definitely more likely to happen if you plan for it than if you don’t.
  structure:
    - >-
      activate
    - >-
      testimonial
    - >-
      refer
    - >-
      ascend
  anchor: >-
    every customer to do: activate, testimonial, refer, ascend. You can also incentivize by giving
  source: >-
    playbook-retention.md, Churn Checklist #9: Make a Customer Journey, lines 713–723
  confirmations: 2
  authors_caveat: >-
    Besides activation, 2-3-4 may all happen in different orders depending on the customer and business model.
  anchor_at: "playbook-retention.md:715"
- id: A-playbooks-growth-032
  type: framework
  name: >-
    The four attributes of a Fast Cash Play
  statement: >-
    A Fast Cash Play is built to carry four attributes at once: scarcity, exclusivity, big ticket, urgency.
  why: >-
    They create tremendous profit for two reasons: you’ve already acquired the leads you advertise to, so there’s no additional cost to make the sale, and bigger price tags tend to have much better margins.
  applies_when: >-
    A limited time offer advertised to your warmest audiences — current customers, previous customers, and all engaged leads.
  structure:
    - >-
      limited in spots (scarcity)
    - >-
      high touch (exclusivity)
    - >-
      sold for lots of money (big ticket)
    - >-
      for a limited time (urgency)
  anchor: >-
    customers. Fast Cash plays are limited in spots (scarcity), high touch (exclusivity), and sold
  source: >-
    playbook-fast-cash.md, How Fast Cash Plays Work, lines 149–161
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:152"
- id: A-playbooks-growth-033
  type: framework
  name: >-
    The Fast Cash Playbook design decisions
  statement: >-
    A Fast Cash Play is designed by answering six questions in order: who to advertise to, what to sell them, how many to sell, how to sell it, what to charge, and how to promote it.
  why: >-
    How you sell matters because it changes how you promote, so the promotion sequence cannot be chosen before the earlier answers are fixed.
  structure:
    - >-
      Who to advertise to. Your existing customers, previous customers, and engaged leads list.
    - >-
      What to sell them. Think scarcity, urgency, exclusivity, and a premium price — the most valuable things you can do that are “unscalable.”
    - >-
      How many to sell. Cap it to a number where you will absolutely sell out — maybe five to ten percent of your customers.
    - >-
      How to sell it. For most businesses, high price points deserve a one-on-one consultation.
    - >-
      What to charge. Take whatever your average cart value - or transaction size is, and add a zero. Think 10x to 50x your current price tag.
    - >-
      Promoting It. Promote your Fash Cash play for seven days or less or until spots run out.
  anchor: >-
    I’ll cover who you advertise your offer to, what you sell, what to charge, how
  source: >-
    playbook-fast-cash.md, The Fast Cash Playbook, Description, lines 222–305
  confirmations: 2
  anchor_at: "playbook-fast-cash.md:224"
- id: A-playbooks-growth-034
  type: framework
  name: >-
    The unscalable value categories
  statement: >-
    What to put in a Fast Cash offer is chosen from ten categories of unscalable value.
  why: >-
    These ‘unscalable’ solutions are the things that typically justify the crazy high price tags, so at a crazy high price you include the stuff before you cut things for being ‘unscalable.’
  structure:
    - >-
      Attention: 1 on 1 attention from you, or senior persons in the company
    - >-
      Personalization: Personalized, customized versions of your standard solutions.
    - >-
      Convenience: 24/7 support, extended hours, exclusive times, etc.
    - >-
      Status: Special parking, perks, badges, public recognition.
    - >-
      Duration: Longer duration than standard solutions. Think six months to a year.
    - >-
      Speed: First in line. Priority. Fast response time promises (<10 min or less)
    - >-
      Experience: Think “White Glove” service. Personal cell phone access. A concierge line. Nice dinners. Nice drinks. Gifts.
    - >-
      Access: In-person experiences. Retreats. Normally restricted areas. Behind the scenes.
    - >-
      Network: Connection with other top customers (where applicable)
    - >-
      Secrets: Exclusive bonuses. Trade secrets. Access to vendors you have vetted.
  anchor: >-
    What to sell them . With Fast Cash offers, you want to think scarcity, urgency, exclusivity,
  source: >-
    playbook-fast-cash.md, The Fast Cash Playbook, Description, lines 236–257
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:236"
- id: A-playbooks-growth-035
  type: framework
  name: >-
    One to three core components and three bonuses
  statement: >-
    A Fast Cash offer is assembled as one to three core components plus three bonuses that are revealed one at a time across the promotion.
  why: >-
    We layer in these bonuses one at a time to increase the likelihood people buy with each additional bonus: new information further expands the price-to-value discrepancy to push them over the edge.
  structure:
    - >-
      one to three core components of your offer
    - >-
      three bonuses, layered in one at a time
    - >-
      You’ll make all the bonuses available to all buyers, no matter when they buy.
  anchor: >-
    You will want to have one to three core components of your offer, and three bonuses.
  source: >-
    playbook-fast-cash.md, The Fast Cash Playbook, Description, lines 258–263
  confirmations: 2
  anchor_at: "playbook-fast-cash.md:258"
- id: A-playbooks-growth-036
  type: framework
  name: >-
    PUSH TO CONSULT SEQUENCE
  statement: >-
    When the Fast Cash offer is sold by consultation, the promotion runs eight dated touches from seven days out to twelve hours out, each adding a bonus or a scarcity update.
  why: >-
    Unless you have enough competent salespeople you’ll struggle to smash all consultations together, so you make the thing available day one but drive people to book appointments and spread out the consults.
  applies_when: >-
    Selling the Fast Cash offer through one-on-one consultations.
  structure:
    - >-
      7 DAYS OUT - Let them know something big is coming via email tomorrow.
    - >-
      6 DAYS OUT - Announcement email. List the one to three core components of your offer. Have a CTA in that email for them to schedule a consult.
    - >-
      5 DAYS OUT - Recap offer. Add your first additional bonus if you have it.
    - >-
      3 DAYS OUT - Sales update. Let everyone know how many sold already, how many you have left, and remind them it’s first come first serve.
    - >-
      2 DAYS - X Spots Left. Add your second bonus if you have it.
    - >-
      24 HOURS OUT (AM) - Warning: A few hours out or X spots left. Add your best bonus here.
    - >-
      12 HOURS OUT (PM) - Sold out.
    - >-
      (Optional) Back out one spot left. If you have someone back out.
  anchor: >-
    7 DAYS OUT - Let them know something big is coming via email tomorrow. I prefer
  source: >-
    playbook-fast-cash.md, PUSH TO CONSULT SEQUENCE, lines 306–336
  confirmations: 2
  anchor_at: "playbook-fast-cash.md:307"
- id: A-playbooks-growth-037
  type: framework
  name: >-
    PUSH TO AUTOMATED CHECKOUT SEQUENCE
  statement: >-
    When the Fast Cash offer is sold by automated checkout, the promotion runs ten touches from five days out to the day after, building tension before the cart opens and reporting scarcity after.
  why: >-
    If you blast your whole list and have an automated checkout, you build up tension launch style, cause a stampede by opening the cart to everyone at once, and make it first come, first serve.
  applies_when: >-
    Selling the Fast Cash offer through an automated checkout rather than consultations.
  structure:
    - >-
      5 DAYS OUT - Primer Text: Let them know something big is coming via email tomorrow.
    - >-
      4 DAYS OUT - Announcement email. Say the one to three core components of your offer.
    - >-
      2 DAYS OUT - Tell them the cart opens in 48 hours. Remind them it’s first come, first serve.
    - >-
      24 HOURS OUT. Add first bonus. Tell them to set an alarm so they don’t miss it.
    - >-
      60 MIN OUT. Text to remind them to set an alarm and have their payment method ready.
    - >-
      5 MIN - Cart open. Add the best bonus here the moment you tell them the cart is open.
    - >-
      60 MIN POST - Sales update. How many sold already. How many left.
    - >-
      6 HOURS POST - X spots left. Add one bonus you didn’t mention.
    - >-
      12 HOURS POST - Sold out. You let everyone know.
    - >-
      NEXT DAY - Back out one spot left. If you have someone back out.
  anchor: >-
    5 DAYS OUT - Primer Text: Let them know something big is coming via email tomor-
  source: >-
    playbook-fast-cash.md, PUSH TO AUTOMATED CHECKOUT SEQUENCE, lines 337–373
  confirmations: 1
  authors_caveat: >-
    I’d rather you sell out and then waitlist people who already tried to buy.
  anchor_at: "playbook-fast-cash.md:338"
- id: A-playbooks-growth-038
  type: framework
  name: >-
    5 Reasons To Run Fast Cash Offers Every 90 Days
  statement: >-
    Once a quarter is the cadence for Fast Cash Plays, for five reasons that together set both the floor and the ceiling on frequency.
  why: >-
    Running them every week doesn’t work; running them once a year doesn’t really work either, at least if you don’t hate money.
  structure:
    - >-
      First, it cleans up your pipeline of qualified-but-on-the-fence leads.
    - >-
      Second, it increases the value of every customer. People who buy more often are more likely to keep buying.
    - >-
      Third, it always shows there’s something new and interesting going on. It shakes things up.
    - >-
      Fourth, doing it once per quarter allows you time to deliver and reset before running another Fast Cash Play.
    - >-
      Fifth, assuming your business is break-even or better, all the additional revenue from warm leads drops straight to the bottom line.
  anchor: >-
    I’ve found that once a quarter is the sweet spot for a few reasons:
  source: >-
    playbook-fast-cash.md, 5 Reasons To Run Fast Cash Offers Every 90 Days, lines 458–475
  confirmations: 1
  authors_caveat: >-
    If you feel you need to give it longer than twelve weeks to cool off between promotions, run it twice a year instead.
  anchor_at: "playbook-fast-cash.md:462"
- id: A-playbooks-growth-039
  type: framework
  name: >-
    Fast Cash Checklist
  statement: >-
    A Fast Cash Play is executed as a ten-item checklist, from assembling the list to setting the next date.
  why: >-
    A clean tear sheet you can use for yourself or hand to your team so they can get this done for you.
  structure:
    - >-
      Pick and assemble the list you plan to send your offer to (past and present customers).
    - >-
      Pick the offer you will send. Max out unscalable value. Model the examples.
    - >-
      Pick a price to match it. 10x to 50x for maximum cash. Be bold!
    - >-
      Choose consults (open the cart immediately and have people book calls) or automated checkout (build hype then open the cart and quickly close it).
    - >-
      Prep your emails and texts with CTAs that match the offer.
    - >-
      Send the sequence. Collect cash.
    - >-
      Deliver the stuff.
    - >-
      Collect the 4Rs at the end: Reviews, Results, Referrals, and Resells.
    - >-
      Cooldown your list. Get back to providing value.
    - >-
      Set your next date. Rinse & repeat.
  anchor: >-
    Pick and assemble the list you plan to send your offer to (past and present customers).
  source: >-
    playbook-fast-cash.md, Fast Cash Checklist, lines 545–566
  confirmations: 2
  anchor_at: "playbook-fast-cash.md:546"
- id: A-playbooks-growth-040
  type: framework
  name: >-
    The 4Rs
  statement: >-
    At the end of a Fast Cash Play, four things are collected from the buyers: Reviews, Results, Referrals, and Resells.
  applies_when: >-
    After delivering the Fast Cash offer and before cooling the list down.
  structure:
    - >-
      Reviews
    - >-
      Results
    - >-
      Referrals
    - >-
      Resells
  anchor: >-
    Collect the 4Rs at the end: Reviews, Results, Referrals, and Resells.
  source: >-
    playbook-fast-cash.md, Fast Cash Checklist, line 564
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:564"
- id: A-playbooks-growth-041
  type: framework
  name: >-
    The five levels of awareness
  statement: >-
    Audiences run from the warmest and smallest at the bottom to the coldest and largest at the top across five levels: Most Aware, Product-Aware, Solution-Aware, Problem-Aware, Completely Unaware.
  why: >-
    In the beginning, you start with the smallest but highest converting eyeballs; then, as you scale, you go to progressively larger but lower-converting eyeballs, so the larger the audience you reach, the more varied and exceptional your ads must be.
  structure:
    - >-
      Most Aware: (bottom) The customer knows your product and only needs to know the deal.
    - >-
      Product-Aware: The customer knows what you sell but isn’t sure it’s right for them.
    - >-
      Solution-Aware: The customer knows the result they want but doesn’t know your product can provide it.
    - >-
      Problem-Aware: The customer senses they have a problem but doesn’t know there’s a solution.
    - >-
      Completely Unaware: (top) The customer doesn’t know they have a problem or need.
  anchor: >-
    wonderful framework around this. He contends that audiences go from bottom (warmest
  source: >-
    playbook-goated-ads.md, Why Ads Hit A Wall And How To Scale Past It, lines 96–130
  confirmations: 2
  authors_caveat: >-
    The framework is Eugene Schwartz’s (spelt “Eugene Swartz” at line 98). The author adds: “I want to be clear, I’ve never met these people in Eugene’s pyramid. Labels are clean. Reality is messy,” and has adapted the chunked model into a continuous one.
  anchor_at: "playbook-goated-ads.md:100"
- id: A-playbooks-growth-042
  type: framework
  name: >-
    The Ad Assembly Process
  statement: >-
    Ads are not created but assembled from three separately produced parts — hooks, meats, CTAs — and multiplied: 50 hooks x 3-5 meat x 1-3 CTAs = 150 to 750 ads per week.
  why: >-
    It was much harder to make a bunch of ads at once and much easier to make the ads in parts; it also gives the side benefit of no one being able to figure out your top performing ads.
  applies_when: >-
    On top of the paid ads chapters in $100M Leads, not instead of them.
  structure:
    - >-
      First, I would make fifty hooks.
    - >-
      Then, I would record the three to five very well-thought-out scripts to match the hooks
    - >-
      and then I would have my one to three versions of my Call To Action or CTA.
  anchor: >-
    the result of this prep is 50 hooks x 3-5 meat x 1-3 CTAs = 150 to 750 ads…per week. This
  source: >-
    playbook-goated-ads.md, The Ad Assembly Process, lines 142–156
  confirmations: 3
  anchor_at: "playbook-goated-ads.md:152"
- id: A-playbooks-growth-043
  type: framework
  name: >-
    The prep time split
  statement: >-
    Preparation time for a recording session is split 80% hooks, 20% meat, ~0% CTAs.
  why: >-
    If someone doesn’t make it through the hook, then nothing else matters. So we put eighty percent of our time there.
  applies_when: >-
    Ninety percent of the work in advertising is in the preparation to record, not in the recording itself.
  structure:
    - >-
      80% Hooks
    - >-
      20% Meat
    - >-
      ~0% CTAs
  anchor: >-
    not in the recording itself. Here’s how I split my prep time:
  source: >-
    playbook-goated-ads.md, Next Time You film, lines 159–167
  confirmations: 1
  anchor_at: "playbook-goated-ads.md:162"
- id: A-playbooks-growth-044
  type: framework
  name: >-
    Five places to look for high-converting hooks
  statement: >-
    Hooks for immediate results are harvested from five sources, in this order of preference, with platform ad libraries last.
  why: >-
    Winning hooks in one industry often work in others, and hooks that worked on one platform or advertising method have the highest likelihood of converting when moved to another.
  structure:
    - >-
      Winning Hooks From Your Previous Ads - These are literally past winners that I reuse.
    - >-
      Winning Hooks From Your Free Content - find hooks that work on one platform or advertising method and use it in another.
    - >-
      Winning Hooks From Other People’s Ads - I save all ads I like and write down the hooks they use.
    - >-
      Winning Hooks From Other People’s Free Content: You just look for content with tons of views in your space.
    - >-
      Platform-Specific Ad Libraries: I list this last because it’s the last place I look.
  anchor: >-
    ments. I look for high-converting hooks in the following places:
  source: >-
    playbook-goated-ads.md, Writing Hooks For Immediate Results From Previous Winners, lines 171–209
  confirmations: 2
  authors_caveat: >-
    If it’s your first time running ads, skip the first source. Big ad libraries become a fun place for ideas more than they guarantee winners.
  anchor_at: "playbook-goated-ads.md:177"
- id: A-playbooks-growth-045
  type: framework
  name: >-
    Hook drivers by level of awareness
  statement: >-
    Each level of awareness takes a hook of its own kind: offer driven, proof driven, promise driven, pain driven, curiosity driven.
  why: >-
    If you continue to write hooks that focus on your offer or proof, you will convert a small slice of a larger audience very well; to grab a bigger slice of the pie you’ll want to meet the audience where they’re at.
  applies_when: >-
    Writing expansion hooks to enter new markets after you’ve capped your existing ad capacity.
  structure:
    - >-
      Most Aware: These hooks are typically offer driven.
    - >-
      Product-Aware: These hooks are typically proof driven.
    - >-
      Solution-Aware: These ads are typically promise driven.
    - >-
      Problem-Aware: These ads are typically pain driven.
    - >-
      Completely Unaware: These ads are typically curiosity driven.
  anchor: >-
    Most Aware: These hooks are typically offer driven.
  source: >-
    playbook-goated-ads.md, Writing Expansion Hooks To Enter New Markets, lines 219–285
  confirmations: 2
  authors_caveat: >-
    Think of these more as frameworks than some magical recipe; this isn’t written in stone. If 90% of your hooks land in the “Most aware” bucket, spread them out to capture a bigger slice. When in doubt, go a little broader.
  anchor_at: "playbook-goated-ads.md:224"
- id: A-playbooks-growth-046
  type: framework
  name: >-
    Five major ad formats
  statement: >-
    The meat of an ad is written in one of five formats, which can be mixed and matched: Demonstration, Testimonial, Education, Story, Faceless.
  why: >-
    These are the ones I’ve used that worked, and they’ve worked across all industries: services, education, physical products, brick and mortar, software, and so on.
  applies_when: >-
    Whenever I get stuck on what type of ad or format I’m going to use for the ‘meat’, I refer back to this list.
  structure:
    - >-
      Demonstration Ads: Think showcasing your product or service, unboxing, comparison ads, before-and-afters, high production hero ads.
    - >-
      Testimonial Ads: Think user-generated content (UGC), founder direct to camera, podcast style, professional testimonials, raw iPhone style testimonials, walk-n-talk rant style, group testimonials, lifecycle ads, man-on-the-street interviews, or celebrity or influencer collabs.
    - >-
      Education Ads: Think educational/informational, explainer videos, how-to/tutorial, whiteboard explainer, listicle videos, high performing organic content
    - >-
      Story Ads: Think storytelling/narrative, lifestyle, emotional/sentimental, humorous/comedy, brand manifesto, problem-solution
    - >-
      Faceless Ads: Think screenshots of customer comments/texts, text only, slide shows, animations, cartoon ads, or visual effect based ads.
  anchor: >-
    When I looked back at all my ads, I used five major formats. No, I’m not saying these
  source: >-
    playbook-goated-ads.md, The Ad Meat, lines 363–389; Cheat Sheet Step 3, lines 664–695
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:371"
- id: A-playbooks-growth-047
  type: framework
  name: >-
    A good CTA shows or tells
  statement: >-
    A sound call to action covers five things: what to do, how to do it, when to do it, what they get for doing it, and what happens next.
  why: >-
    Your audience can only know what to do if you tell them; and when they click and get exactly what they expected, they’ll be more likely to follow through — it provides the ultimate congruence.
  structure:
    - >-
      What to do
    - >-
      How to do it
    - >-
      When to do it
    - >-
      What they get for doing it
    - >-
      What happens next (optional)
  anchor: >-
    A good CTA shows or tells: what to do, how to do it, when to do it, what they get for
  source: >-
    playbook-goated-ads.md, CTA - Call To Action, lines 533–547; Cheat Sheet Step 4, lines 697–703
  confirmations: 2
  authors_caveat: >-
    What happens next is more important with lead magnets and multi-step sales processes.
  anchor_at: "playbook-goated-ads.md:533"
- id: A-playbooks-growth-048
  type: framework
  name: >-
    GOATed Ads Playbook Cheat Sheet
  statement: >-
    An ad day runs five steps: pick the level of awareness, write 50 hooks, write 3-5 meats, write 1-3 CTAs, then repeat to find another winner.
  why: >-
    A cheat sheet you can tear out and put on your wall or hand to your team to use on your next ad day.
  structure:
    - >-
      Step 1 - Figure out the level of awareness you’re targeting 1) Unaware 2) Problem Aware 3) Solution Aware 4) Product Aware 5) Most Aware.
    - >-
      Step 2 - Write 50 hooks: Either divide the hooks into buckets that hit each level of awareness or focus the majority of your ads broader than your current hooks.
    - >-
      Step 3 - Write 3-5 “meats”: Pick a few of the following types.
    - >-
      Step 4 - Write 1-3 CTAs: Both show and tell them what to do next.
    - >-
      Step 5 - Try To Find A New Winner: Repeat steps 1-4 to try and find another winner.
  anchor: >-
    Step 5 - Try To Find A New Winner: Repeat steps 1-4 to try and find another winner.
  source: >-
    playbook-goated-ads.md, GOATed Ads Playbook Cheat Sheet, lines 648–705
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:705"
```
