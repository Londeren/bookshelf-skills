# Улов фазы 1 — $100M Playbooks: Lead Nurture, Retention, Fast Cash, GOATed Ads (2025) (ярус 2), тип D: антипаттерны и границы

Группа `tier2-playbooks-growth`, слаг `playbooks-growth`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **81** (экстрактор вернул 81, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `playbook-lead-nurture.md` | 1–1148 | 2 | 25 |
| `playbook-retention.md` | 1–835 | 2 | 21 |
| `playbook-fast-cash.md` | 1–779 | 2 | 16 |
| `playbook-goated-ads.md` | 1–707 | 1 | 19 |

## Как собран файл

Экстрактор D (Antipatterns and boundaries) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-playbooks-growth.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-playbooks-growth-D.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 1 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: D-playbooks-growth-001
  type: antipattern
  name: >-
    Treating the show rate as something you cannot control
  statement: >-
    Owners do not work on show rate because they believe they cannot do anything about it, or they do not know what to do about it.
  why: >-
    Once you learn to see the money you did not make as money you lost, the show rate becomes one of the most important numbers in the business, and it is rare to get better returns than from getting more people to show up to buy.
  anchor: >-
    The problem is, most business owners don’t think much about it because they think:
  source: >-
    playbook-lead-nurture.md, Description, lines 207–211
  confirmations: 1
  authors_caveat: >-
    Of the three reasons owners give, the author accepts only the third, that they have more important stuff to do, because sometimes they do; even then he says it is rare to get better returns elsewhere.
  anchor_at: "playbook-lead-nurture.md:207"
- id: D-playbooks-growth-002
  type: rule
  name: >-
    What this playbook does not cover
  statement: >-
    The playbook solves one problem, maximizing 30-day show rates, and nothing else.
  why: >-
    Lead nurturing occurs after advertising and before sales; long-term follow-up is covered in other places by the author.
  anchor: >-
    This playbook covers medium-term lead nurture - aka - maximizing 30-day show rates.
  source: >-
    playbook-lead-nurture.md, Next Up: The Four Pillars of Lead Nurture, lines 217–221
  confirmations: 2
  boundary: >-
    Medium-term nurture only: the window between a lead showing interest and buying, within 30 days. Long-term follow-up (emails, podcasts, content) is explicitly outside this playbook.
  anchor_at: "playbook-lead-nurture.md:217"
- id: D-playbooks-growth-003
  type: rule
  name: >-
    Show rates differ by industry
  statement: >-
    Show-rate levels are not comparable across industries; the benchmark is being best in class within your own industry.
  why: >-
    Some industries have higher show rates than others, but the four pillars let any business become best in class within its industry.
  anchor: >-
    matter what you sell. That being said, some industries have higher show rates than others,
  source: >-
    playbook-lead-nurture.md, Four Pillars of Lead Nurture, lines 249–250
  confirmations: 1
  boundary: >-
    The absolute show rate is industry-bound; only the within-industry ranking is claimed to be movable by any business.
  anchor_at: "playbook-lead-nurture.md:249"
- id: D-playbooks-growth-004
  type: rule
  name: >-
    Availability applies to appointment-based businesses
  statement: >-
    The finding that availability is the biggest lever on shows was established for appointment-based businesses.
  why: >-
    If leads do not schedule they cannot show, and if they cannot show they cannot buy; on an absolute basis the businesses with the most time slots had the most schedules, shows and purchases.
  anchor: >-
    The data was crystal clear for appointment-based businesses-–if leads do not schedule,
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability, lines 299–301
  confirmations: 1
  boundary: >-
    Appointment-based businesses, the kind where a lead books a time and shows up for it.
  anchor_at: "playbook-lead-nurture.md:299"
- id: D-playbooks-growth-005
  type: antipattern
  name: >-
    Having no availability when leads have availability
  statement: >-
    The business offers slots that suit the business, so leads either do not schedule at all or schedule at a time that is bad for them.
  why: >-
    If nobody schedules, nobody shows and nobody buys; and a lead booked at a bad time has a huge chance of skipping or ghosting, buys less if they do show, and takes a slot away from someone who would have shown up and bought.
  anchor: >-
    have availability, they either: a) don’t schedule at all or b) schedule at a bad time for them.
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability, Description, lines 302–312
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:305"
- id: D-playbooks-growth-006
  type: antipattern
  name: >-
    Selling only during your own business hours
  statement: >-
    Taking appointments only on weekdays during office hours, while customers are at work.
  why: >-
    You pay rent, payroll and insurance seven days per week; most people work five days, so taking appointments seven days per week makes the business 40% more available to accept money.
  anchor: >-
    are available to buy. Not doing so would be like having a retail store open 9–5, Monday
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability, Tactics, lines 333–351
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:346"
- id: D-playbooks-growth-007
  type: antipattern
  name: >-
    Scheduling slots built around the appointment length
  statement: >-
    Only letting leads schedule every 30 or 60 minutes because the appointments are 30 or 60 minutes long.
  why: >-
    That makes things convenient for the business, not for the lead; four scheduling options per hour keeps the appointment length the same while giving people freedom over when it starts.
  anchor: >-
    that makes things convenient for the business, not for the lead. Consider four scheduling
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability, Tactics, lines 352–357
  confirmations: 1
  authors_caveat: >-
    It produces some awkward gaps between appointments and may take extra salespeople; if qualifying and closing are done on separate calls, a 15-minute qualifying call solves the issue entirely.
  anchor_at: "playbook-lead-nurture.md:354"
- id: D-playbooks-growth-008
  type: rule
  name: >-
    When to add friction instead of removing it
  statement: >-
    When the calendar fills with too many bad appointments, friction is added back on purpose: a video or sales letter before the scheduler, a price on the page, a delayed scheduler.
  why: >-
    Eliminating friction increases the number of appointments booked, which is the first step to getting a show, but these steps decrease appointments and increase quality.
  anchor: >-
    appointments on your calendar. When that happens—it’s okay to add friction.
  source: >-
    playbook-lead-nurture.md, Author Note: Solution For Too Many Bad Appointments, lines 399–407
  confirmations: 1
  boundary: >-
    The remove-all-friction rule reverses once appointment quality, not appointment quantity, is the constraint.
  anchor_at: "playbook-lead-nurture.md:402"
- id: D-playbooks-growth-009
  type: antipattern
  name: >-
    Judging availability by its cost instead of its return
  statement: >-
    Owners refuse more availability and faster contact because of the extra cost, saying I can’t be open any more hours.
  why: >-
    It is not about how much it costs, it is about return on investment; people really mean it is not worth it right now, while they set a giant pile of money on fire by making it harder for people to buy.
  anchor: >-
    These are simple. And yet, no one does them. Most are afraid of the extra cost. But it’s
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability, lines 316–326 and 408–410
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:408"
- id: D-playbooks-growth-010
  type: antipattern
  name: >-
    Letting leads schedule far out
  statement: >-
    Letting people book meetings much beyond three days out.
  why: >-
    You get more people to schedule but more people ghosting: a triple loss, because the person ghosted you, because enough ghosted meetings kill the sales team’s morale, and because the ghost stole a convenient time from someone who may have bought.
  anchor: >-
    people to schedule, but you’ll also have more people ghosting. A triple loss. First, because
  source: >-
    playbook-lead-nurture.md, Pillar II: Speed, 2) Speed To First Appointment, lines 462–472
  confirmations: 1
  authors_caveat: >-
    You can get away with five days if you have to; the author prefers three, and in either case says to keep tabs on show rates and find the sweet spot for your business.
  anchor_at: "playbook-lead-nurture.md:464"
- id: D-playbooks-growth-011
  type: antipattern
  name: >-
    Letting leads fall through the cracks before the appointment
  statement: >-
    Answering a scheduled lead’s questions only on the next business day.
  why: >-
    Leads often make buying decisions before the sales call; slow replies make them assume you are scattered and disorganized and that you are not prioritizing them, and they stop asking.
  anchor: >-
    they’re not prioritizing you—because they’re not. If they don’t show up for you, why bother
  source: >-
    playbook-lead-nurture.md, Pillar II: Speed, 3) Speed of Response, lines 546–565
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:558"
- id: D-playbooks-growth-012
  type: antipattern
  name: >-
    Reaching out one time on one platform
  statement: >-
    Contacting a new lead once, through a single channel.
  why: >-
    Response rates are higher when conversations are started in as many ways as possible and then continued where the lead answers.
  anchor: >-
    phone call, Zoom, or video call). This sounds basic, but so many people only reach out
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, 1) Use The Lead’s Preferred Communication Method, lines 642–659
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:644"
- id: D-playbooks-growth-013
  type: antipattern
  name: >-
    Going through the motions on outreach
  statement: >-
    Making contact attempts for the record rather than actually trying to get hold of the lead.
  why: >-
    If you needed to reach your own parents you would call repeatedly, text, DM and call their friends; the leads asked for help, and not reaching out like you mean it does them a disservice.
  anchor: >-
    Also, you’ve gotta reach out like you’re actually trying to get ahold of them—not just
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, lines 649–657
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:649"
- id: D-playbooks-growth-014
  type: antipattern
  name: >-
    Wasting the good leads on junior reps
  statement: >-
    Routing the best leads to junior reps while the top closer spends two-thirds of their time on unqualified people.
  why: >-
    In the timeshare company this cost the top rep two-thirds of his time; when the best leads went to the best closer his office 5x’d production and the company went from $200M to $1B a year in sales over five years.
  anchor: >-
    more sales. I told him, ‘You’re wasting all the good leads on these junior reps. Meanwhile,
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, 3) Send The Best Leads To The Best Closers, lines 672–699
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:684"
- id: D-playbooks-growth-015
  type: rule
  name: >-
    A gift card has no strings
  statement: >-
    The push incentive is sent whether or not the lead shows up; it is a gift, not a conditional reward.
  why: >-
    The strategy hinges on reciprocity, and gifts have no strings; even when people know what you are doing it still works, because they feel they owe you one.
  anchor: >-
    insulting. And to be clear, they get the gift card you send whether they show or not. This is a
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, 5) Incentives, lines 749–764
  confirmations: 1
  boundary: >-
    A push incentive only works as an unconditional gift; making it conditional on showing up turns it into something else.
  anchor_at: "playbook-lead-nurture.md:751"
- id: D-playbooks-growth-016
  type: rule
  name: >-
    The three conditions of an A/B incentive
  statement: >-
    An A/B pull incentive works only if the lead wants the thing, it connects obviously to what you will offer them, and you incurred a real cost preparing it.
  why: >-
    Both choices assume they will show, and the point is to show you are incurring a cost on their behalf.
  anchor: >-
    A/B Incentives depend on three things. First, leads should want the thing. Second, it
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, 5) Incentives, lines 765–781
  confirmations: 1
  boundary: >-
    Missing any of the three conditions and the A/B offer stops being an incentive.
  anchor_at: "playbook-lead-nurture.md:779"
- id: D-playbooks-growth-017
  type: rule
  name: >-
    Proof has to be compliant
  statement: >-
    The proof woven into nurture messaging must comply with the rules of the jurisdiction.
  why: >-
    Compliance requirements for proof vary by state and country.
  anchor: >-
    Obviously  be  compliant  with  the  proof  you  send—which  varies  by  state  and  country.
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, 6) Proof, line 790
  confirmations: 1
  boundary: >-
    A legal limit on the proof tactic, set by state and country.
  anchor_at: "playbook-lead-nurture.md:790"
- id: D-playbooks-growth-018
  type: antipattern
  name: >-
    Giving up after the first attempt
  statement: >-
    Nearly half of all salespeople stop contacting a lead after the first attempt, with an average of 1.3 attempts.
  why: >-
    Most communication attempts fail for reasons that have nothing to do with interest: a bad moment, a forgotten reply, a message lost in the flurry; and since the lead opted in, they asked to be contacted, so reaching out again makes ethical as well as business sense.
  anchor: >-
    The problem: nearly half of all salespeople give up after the first attempt. No bueno.
  source: >-
    playbook-lead-nurture.md, Pillar Iv: volume, lines 829–838
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:837"
- id: D-playbooks-growth-019
  type: rule
  name: >-
    Obey the laws of your area
  statement: >-
    The call-and-text cadence, including double-dialling, is run only within the laws of your jurisdiction.
  why: >-
    The author states the limit twice without argument, as a condition on running the volume cadence at all.
  anchor: >-
    showed you what I prefer. As always, follow the laws in your area.
  source: >-
    playbook-lead-nurture.md, Pillar Iv: volume, 1) Scheduling Appointments, lines 852–874
  confirmations: 2
  boundary: >-
    Local law caps the contact cadence; the eight-step sequence is the author’s preference inside that cap.
  anchor_at: "playbook-lead-nurture.md:874"
- id: D-playbooks-growth-020
  type: antipattern
  name: >-
    Passing automated reminders off as personal
  statement: >-
    Sending automated reminders without making it clear that they are automated.
  why: >-
    People don’t mind reminders, they do mind being lied to.
  anchor: >-
    them  automated  reminders.  But  make  it  clear  they  are  automated.  People  don’t  mind
  source: >-
    playbook-lead-nurture.md, Pillar IV: Volume, 2) Reminding Them To Show, lines 884–899
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:887"
- id: D-playbooks-growth-021
  type: antipattern
  name: >-
    Getting off the call without booking the next one
  statement: >-
    Ending a call with we’ll circle back later or I’ll follow up and propose some times.
  why: >-
    If you cannot schedule an appointment with them right then and there, you certainly will not after you have put them in limbo and they have put you in their rearview mirror; people have a higher chance of showing up to appointments you schedule with them in real time.
  anchor: >-
    Here’s  how  it  works:  NEVEr  get  off  the  call  with  “We’ll  circle  back  later.”  or  “I’ll
  source: >-
    playbook-lead-nurture.md, Pillar IV: Volume, 3) Book Their Next Appointment At The Current Appointment, lines 907–924
  confirmations: 2
  applies_when: >-
    Any call that does not end in a close; internally called BAMFAM as a way of life, and someone being dodgy about their next call is treated as an objection to handle.
  anchor_at: "playbook-lead-nurture.md:913"
- id: D-playbooks-growth-022
  type: antipattern
  name: >-
    Cherry-picking leads
  statement: >-
    Reps take only the prime leads and hand off or drop the less qualified ones.
  why: >-
    The less qualified leads still close: the rep who took everyone else’s yellows worked them off-hours and kept closing them, finishing as top salesman out of 26; yellows are the new gold.
  anchor: >-
    They just wanted to cherry-pick. So they gave him all their “garbage” leads. And he would
  source: >-
    playbook-lead-nurture.md, Execution, lines 1006–1015
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:1008"
- id: D-playbooks-growth-023
  type: antipattern
  name: >-
    A high close rate on unworked leads
  statement: >-
    A rep closes at a very high rate but does not work their leads.
  why: >-
    In this culture that is seen as entitled and wasteful, and the person is made aware of it; the nurture list measures work ethic, the closing list measures skill.
  anchor: >-
    reinforce the right behaviors. And conversely, if someone has a very high close rate but
  source: >-
    playbook-lead-nurture.md, Execution, Tactics, lines 1048–1055
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:1048"
- id: D-playbooks-growth-024
  type: antipattern
  name: >-
    Being obsessed with close rates
  statement: >-
    Businesses track and reward close rate by rep and ignore show rate and lead-to-close rate.
  why: >-
    The only thing that actually matters is the conversion rate on the leads you’ve got, and that takes everything into account, so pay and status should be based on all three metrics.
  anchor: >-
    metrics by sales rep. They’re so obsessed with close rates. But the only thing that actually
  source: >-
    playbook-lead-nurture.md, Execution, Tactics, lines 1059–1063
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:1060"
- id: D-playbooks-growth-025
  type: rule
  name: >-
    My way is not the only way
  statement: >-
    The playbook is presented as one working way of getting leads to show, not as the only way.
  why: >-
    The author states it as his own practice: it is just his way, and it has worked pretty well so far.
  anchor: >-
    Like my other Playbooks, I do not say that my way is the only way. It’s just my way.
  source: >-
    playbook-lead-nurture.md, Execution Conclusion, lines 1064–1066
  confirmations: 1
  boundary: >-
    Everything in the playbook is offered as the author’s practice rather than as the general case.
  anchor_at: "playbook-lead-nurture.md:1065"
- id: D-playbooks-growth-026
  type: antipattern
  name: >-
    Outselling your churn
  statement: >-
    Believing you can make up for one customer leaving by selling two more.
  why: >-
    It works until it doesn’t: a business with a revolving door of customers is hardly a business at all, and at 15% monthly churn a gym owner loses 83% of members in a year and dies if they fall behind by two customers a month.
  anchor: >-
    always thought that you could make up for one customer leaving by selling two more. And
  source: >-
    playbook-retention.md, Churn Checklist, lines 55–74
  confirmations: 1
  anchor_at: "playbook-retention.md:60"
- id: D-playbooks-growth-027
  type: antipattern
  name: >-
    Growing out of a churn problem by acquiring more customers
  statement: >-
    Trying to 3.3x the number of customers sold each month instead of cutting churn from 10% to 3%.
  why: >-
    It costs way more to do, and even if you did it you accelerate how quickly everyone in your market knows you suck; acquiring a new customer costs five to twenty-five times more than retaining one.
  anchor: >-
    even if you did that, you accelerate how quickly everyone in your market knows you suck.
  source: >-
    playbook-retention.md, Why Is Reducing Churn So Important?, lines 296–304
  confirmations: 1
  anchor_at: "playbook-retention.md:298"
- id: D-playbooks-growth-028
  type: rule
  name: >-
    Expect churn to go up first
  statement: >-
    In the first month of implementing the retention work, churn rises before it falls; the author calls it shaking the three.
  why: >-
    Some people would have canceled anyway, and some have churned as consumers while automated billing still runs, so reminding them makes them cancel; month two and month three then halved churn each.
  anchor: >-
    We would tell gym owners to expect churn to increase at first. But as long as they do
  source: >-
    playbook-retention.md, The 5 Horsemen Of Retention: Results, lines 146–167
  confirmations: 1
  boundary: >-
    Month-one numbers do not measure whether the method works; the judgment comes from the following months.
  anchor_at: "playbook-retention.md:163"
- id: D-playbooks-growth-029
  type: rule
  name: >-
    I don’t know why these things work
  statement: >-
    The retention items are reported as things observed to work, without a mechanism and without knowing which of them contributed most.
  why: >-
    The author says it of both the five horsemen and the Skool findings: he does not know why they work, he just knows that they work, and that doing them all worked.
  anchor: >-
    And to be clear - I don’t know why these things work. Same as the five horsemen. I don’t
  source: >-
    playbook-retention.md, The 5 Horsemen Of Retention: Results, line 174; Putting It All Together, lines 732–734
  confirmations: 2
  boundary: >-
    No causal claim is made, so the items are not to be decomposed or ranked; the claim covers the checklist applied as a whole.
  anchor_at: "playbook-retention.md:174"
- id: D-playbooks-growth-030
  type: antipattern
  name: >-
    Counting churn against the wrong pool
  statement: >-
    Letting new signups during the period change the churn number.
  why: >-
    Churn only counts the pool of customers from the first timepoint; you could sign up zero or 1,000 new clients in the same month and if you lost five of the original hundred your churn is still five percent.
  anchor: >-
    Note: Churn only counts the pool of customers from the first timepoint. People get this
  source: >-
    playbook-retention.md, What Is Churn?, lines 189–192
  confirmations: 1
  anchor_at: "playbook-retention.md:189"
- id: D-playbooks-growth-031
  type: antipattern
  name: >-
    The behaviours that churn 100% of customers
  statement: >-
    Ignoring customers, breaking promises, miscommunicating, treating them poorly, setting unrealistic expectations, hiding progress and updates, keeping them away from other happy customers, and making your stuff harder to use.
  why: >-
    The author derives the retention list by asking what would make customers leave and doing the exact opposite; the opposite behaviours seem obvious, but nobody does them, because it is work.
  anchor: >-
    Seems obvious. But nobody does it. Because....it’s work.
  source: >-
    playbook-retention.md, Price, Value, And Churn, lines 202–226
  confirmations: 1
  anchor_at: "playbook-retention.md:226"
- id: D-playbooks-growth-032
  type: antipattern
  name: >-
    Mispricing the business model
  statement: >-
    Trying to create something recurring out of something that has one-time value.
  why: >-
    The business model has to be matched with the pricing model that makes the most sense; across the Skool platform the higher the price, the higher the churn.
  anchor: >-
    Many businesses misprice their products. For example, they’ll try to create something recur-
  source: >-
    playbook-retention.md, Price, Value, And Churn, lines 248–251
  confirmations: 1
  anchor_at: "playbook-retention.md:249"
- id: D-playbooks-growth-033
  type: antipattern
  name: >-
    Adding more deliverables to reduce churn
  statement: >-
    Answering a retention problem by adding calls, features and material, giving more and decent instead of less but better.
  why: >-
    Overwhelm is the #1 reason for churn; retention comes down to making sure customers consume the value, not to overwhelming them with it, and each version of Gym Launch got shorter and simpler for that reason.
  anchor: >-
    Think value per second, not seconds of value. Less but better is better than more and
  source: >-
    playbook-retention.md, Provide On-Going Value To Get On-Going Customers, lines 254–276
  confirmations: 3
  anchor_at: "playbook-retention.md:255"
- id: D-playbooks-growth-034
  type: antipattern
  name: >-
    Everything I added increased churn
  statement: >-
    The newsletter owner’s churn was lowest with one Q&A call and one physical newsletter a month; going to weekly calls and adding more raised churn.
  why: >-
    Sometimes less is more, there is wisdom in deletion: decide on the core 2-3 things you deliver and focus on making them really good.
  anchor: >-
    I added all these other things...but everything I added increased churn.” Moral of the story:
  source: >-
    playbook-retention.md, Provide On-Going Value To Get On-Going Customers, lines 257–268
  confirmations: 1
  anchor_at: "playbook-retention.md:262"
- id: D-playbooks-growth-035
  type: rule
  name: >-
    Structural churn in VSMB markets
  statement: >-
    Businesses serving very small business owners carry structural churn because those customers go out of business, which makes them high-churn businesses by nature.
  why: >-
    The author says that is okay and you still want to decrease it; Shopify and Skool are both large businesses serving very small customers by percentage.
  anchor: >-
    If you are in an industry where you serve VSMBs (very small business owners),
  source: >-
    playbook-retention.md, Author Note: Churn Varies By Industry, lines 326–333
  confirmations: 1
  boundary: >-
    Churn benchmarks are industry-bound: in VSMB markets a high churn number is structural and does not mean the retention work failed.
  anchor_at: "playbook-retention.md:327"
- id: D-playbooks-growth-036
  type: rule
  name: >-
    Not all of these will apply to your business
  statement: >-
    The nine churn-checklist steps are not all applicable to every business, but many of them will be.
  why: >-
    The checklist is boiled down to activities that work across many businesses hosted on the Skool platform; if you find one and think that won’t work for me, you might be right.
  anchor: >-
    last thing, not all of these will apply to your business. So if you find one and think “That
  source: >-
    playbook-retention.md, Churn Checklist, lines 337–354
  confirmations: 1
  boundary: >-
    Step-level applicability is left to the reader; the author claims the checklist as a whole, not every step.
  anchor_at: "playbook-retention.md:352"
- id: D-playbooks-growth-037
  type: rule
  name: >-
    Exact engagement numbers do not transfer
  statement: >-
    Skool’s activity levels and its level-3 threshold are not to be copied as numbers; what transfers is that engagement matters and that segmenting by engagement makes retention tools more effective.
  why: >-
    The author states the exact numbers matter less for the reader than those two facts.
  anchor: >-
    Exact numbers matter less for you than knowing: First, that customer engagement mat-
  source: >-
    playbook-retention.md, Churn Checklist #1: Figure Out Your Activation Points, lines 359–368
  confirmations: 1
  boundary: >-
    The Skool figures are an illustration of a platform, not a benchmark for another business.
  anchor_at: "playbook-retention.md:366"
- id: D-playbooks-growth-038
  type: rule
  name: >-
    Three months is a convention
  statement: >-
    The three-month cut used to find long-staying customers is arbitrary and may be set to any period.
  why: >-
    There is nothing special about three months; you can do whatever time you want.
  anchor: >-
    is nothing special about three months. You can do whatever time you want.
  source: >-
    playbook-retention.md, Churn Checklist #1: Figure Out Your Activation Points, lines 377–378
  confirmations: 1
  boundary: >-
    A convention inside the activation-point procedure, not a finding.
  anchor_at: "playbook-retention.md:378"
- id: D-playbooks-growth-039
  type: rule
  name: >-
    Activation points are company-specific
  statement: >-
    Activation points differ for every company; the listed examples (first leads for a B2B service, first dashboard login for software, first use of a consumable) are only common ones.
  why: >-
    The activation point is found from your own churned and retained customers by common factors analysis, narrowed to five candidates and worked down the list.
  anchor: >-
    űCommon activation points: they are different for every company. But here
  source: >-
    playbook-retention.md, Churn Checklist #1: Figure Out Your Activation Points, lines 422–429
  confirmations: 1
  boundary: >-
    Borrowing another company’s activation point is out of scope; it has to be re-derived, and retested every 6-12 months.
  anchor_at: "playbook-retention.md:422"
- id: D-playbooks-growth-040
  type: antipattern
  name: >-
    No onboarding at all
  statement: >-
    Running without onboarding while looking for the right onboarding format.
  why: >-
    Custom outperforms generic, personal outperforms group, live outperforms recorded, carrots outperform sticks, and last and most important, some beats none; every time the author has followed the checklist churn has gone down.
  anchor: >-
    sell cheap stuff, do what makes the most sense for the cost. Just do something. Every time I
  source: >-
    playbook-retention.md, Churn Checklist #2: Onboard Your Customers, lines 439–484
  confirmations: 2
  anchor_at: "playbook-retention.md:483"
- id: D-playbooks-growth-041
  type: rule
  name: >-
    Mandatory annual billing trades sales for churn
  statement: >-
    Making annual the only way to pay decreases sales as well as churn, and sometimes that makes more money overall.
  why: >-
    Customers who pay for longer stay longer; the mandatory version is a solid option if you sell over the phone or via webinar, while website checkout should simply make the annual option available.
  anchor: >-
    it mandatory (as in, the only way to pay), it will decrease sales. But, it will decrease churn
  source: >-
    playbook-retention.md, Churn Checklist #6: Add Annual Payment Options, lines 582–594
  confirmations: 1
  boundary: >-
    Mandatory annual pricing belongs to phone or webinar sales; for website checkout the annual option is offered alongside monthly, typically taken by 10-20% at buy 10 months get 2 free.
  anchor_at: "playbook-retention.md:588"
- id: D-playbooks-growth-042
  type: antipattern
  name: >-
    Selling the recurring fee as a second sale
  statement: >-
    Charging the big one-time upfront fee first and selling the small recurring fee separately afterwards.
  why: >-
    You lose the price anchor between the first big purchase and the second small recurring one, and that anchor is what drives the retention.
  anchor: >-
    make it a second sale. Otherwise, you lose the price anchor between the first big
  source: >-
    playbook-retention.md, Churn Checklist #6: Add Annual Payment Options, lines 600–620
  confirmations: 1
  anchor_at: "playbook-retention.md:619"
- id: D-playbooks-growth-043
  type: rule
  name: >-
    When cancellation calls do not pay
  statement: >-
    In a high volume, low price business, getting on the phone with churning customers may not make financial sense; a cancellation video is used instead.
  why: >-
    The video reminds them why they started, resells them, and reminds them what they risk losing by canceling; the author adds that the call almost always pays anyway through what you learn.
  anchor: >-
    ʶIf you have a high volume low price business, hopping on the phone with churning cus-
  source: >-
    playbook-retention.md, Churn Checklist #7: Exit Interviews or Cancellation Videos, lines 685–691
  confirmations: 1
  boundary: >-
    Price point and volume decide whether the save call is run at all; the chance of saving them is higher on a call than in email or text.
  anchor_at: "playbook-retention.md:685"
- id: D-playbooks-growth-044
  type: rule
  name: >-
    The wealthier the customer, the less handholding
  statement: >-
    Wealthier customers typically want less handholding, against the expectation that more contact always retains better.
  why: >-
    The author marks it as a counterintuitive extra finding alongside the result that reaching out 1 on 1 every two to three weeks retained more people than never speaking with customers.
  anchor: >-
    finding: counterintuitively, the wealthier the customers, the less handholding they typ-
  source: >-
    playbook-retention.md, Churn Checklist #8, lines 700–712
  confirmations: 1
  boundary: >-
    The regular 1-on-1 reach-out cadence is dialled down as customer wealth goes up.
  anchor_at: "playbook-retention.md:708"
- id: D-playbooks-growth-045
  type: rule
  name: >-
    There is no magic bullet for churn
  statement: >-
    Churn is not fixed by one lever; it is 100 tiny things that each save a few people.
  why: >-
    Those people stack up into mountains of cash over time, and a business that never fixes churn is doomed to be an always marketing, never growing business.
  anchor: >-
    There is no magic bullet for churn. It’s 100 tiny things that all save a few people
  source: >-
    playbook-retention.md, DO YOU WANT TO SCALE YOUR BUSINESS?, lines 774–780
  confirmations: 1
  boundary: >-
    Looking for a single retention fix is outside what the method offers.
  anchor_at: "playbook-retention.md:777"
- id: D-playbooks-growth-046
  type: antipattern
  name: >-
    Living with high churn
  statement: >-
    Running a business that has to keep getting new customers every month just to stay the same size.
  why: >-
    It never compounds, it is hard to sell and thereby less valuable, feedback and word of mouth go negative, employees lose motivation watching customers fail, and credibility goes because you always have to create new stuff to stay alive.
  anchor: >-
    ʶHave to keep getting new customers every month, just to stay the same size.
  source: >-
    playbook-retention.md, Putting It All Together, lines 750–761
  confirmations: 1
  anchor_at: "playbook-retention.md:751"
- id: D-playbooks-growth-047
  type: rule
  name: >-
    A Fast Cash Play is not lead nurture and not list warming
  statement: >-
    Fast Cash Plays are limited-time offers to the warmest audiences; they are not nurturing new leads about the main offer and not the long-term value-adds that keep a list warm.
  why: >-
    They are designed to make the most money in the shortest period from the people most likely to buy, which for most businesses means existing customers.
  anchor: >-
    To be clear, fast cash plays are different from nurturing new leads about your main offer.
  source: >-
    playbook-fast-cash.md, What Fast Cash Plays Are, lines 137–148
  confirmations: 1
  not_to_confuse_with: >-
    Nurture sequences for new leads on the main offer, and content emails or other long-term value-adds sent to keep lists warm.
  anchor_at: "playbook-fast-cash.md:142"
- id: D-playbooks-growth-048
  type: rule
  name: >-
    Customers won’t mind, if you do it the way I show you
  statement: >-
    Running a specific promotion to existing customers four times a year does not fatigue them only when it is run as described, limited in spots and in time.
  why: >-
    Making it a limited offer is what lets you run it multiple times per year without fatiguing your warm audience.
  anchor: >-
    tomers won’t mind... at least if you do it the way I show you anyway.
  source: >-
    playbook-fast-cash.md, What Fast Cash Plays Are, lines 145–148
  confirmations: 2
  boundary: >-
    The no-fatigue claim is conditional on the scarcity, urgency and cadence rules of this playbook; the author separately warns that implementing it incorrectly makes you seem like a shill.
  anchor_at: "playbook-fast-cash.md:148"
- id: D-playbooks-growth-049
  type: antipattern
  name: >-
    A single fixed-price offer
  statement: >-
    Having only one fixed-price offer, which caps how much any customer can spend with you.
  why: >-
    Making other offers available lets the people who want to spend money on your business actually do it, and 1 out of 9 Americans is a millionaire, so they can afford it if you provide the value.
  anchor: >-
    Think about it like this. If you only have a single fixed-price offer, you cap how much
  source: >-
    playbook-fast-cash.md, How Fast Cash Plays Work, lines 154–184
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:157"
- id: D-playbooks-growth-050
  type: antipattern
  name: >-
    Being a scaredy cat about ultra-premium prices
  statement: >-
    Owners do not make a big-ticket offer because they forget how fast ultra premium prices add up, or are simply afraid.
  why: >-
    Worst case you just don’t sell that many, you still make money and you are no worse off; and if one customer in ten buys at 10x the price you double revenue, with the extra revenue minus delivery dropping to the bottom line.
  anchor: >-
    Business  owners  forget  how  fast  ultra  premium  prices  add  up  to  mountains  of  cash.
  source: >-
    playbook-fast-cash.md, How Fast Cash Plays Work, lines 171–183
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:176"
- id: D-playbooks-growth-051
  type: rule
  name: >-
    What a Fast Cash Play will and will not do
  statement: >-
    The play produces a burst of cash in a week or two from a few emails, texts and posts; it is not a growth engine.
  why: >-
    The author sizes it himself: it won’t make you a billionaire, but it can probably buy you a nice car in a week or two.
  anchor: >-
    To be clear - this playbook won’t make you a billionaire. But, it can probably buy you a
  source: >-
    playbook-fast-cash.md, Fast Cash Play Outline, lines 202–207
  confirmations: 1
  boundary: >-
    A one-off cash event, run about once a quarter; the author places it as one playbook inside his Cash Calendar playbook.
  anchor_at: "playbook-fast-cash.md:206"
- id: D-playbooks-growth-052
  type: rule
  name: >-
    Fulfillment caps the spot count before the 5-10% rule does
  statement: >-
    The cap is set at five to ten percent of customers, a number you will absolutely sell out; above roughly a thousand customers fulfillment constrains you well before that window.
  why: >-
    The point is to sell out fast, which makes the offer more compelling the next time you run it.
  anchor: >-
    you’d limit it to 5-10. If you have 1000 or more, then fulfillment may constrain you well
  source: >-
    playbook-fast-cash.md, Description, How many to sell, lines 264–273
  confirmations: 1
  boundary: >-
    The 5-10% rule holds for small customer bases; with a large base the constraint is delivery capacity, and with only a handful of customers you appeal to all of them privately.
  anchor_at: "playbook-fast-cash.md:269"
- id: D-playbooks-growth-053
  type: rule
  name: >-
    One-on-one consultation unless you cannot
  statement: >-
    High price points deserve a one-on-one consultation; only a very large customer base or a brand big enough to sell expensive things without a consult justifies skipping it.
  why: >-
    The more personal you make the sale of a personal product, the more bites you get; and how you sell changes how you promote, since consults have to be spread across the seven-day window.
  anchor: >-
    tion. If you can’t because you have a ton of customers, or a very big brand that allows you
  source: >-
    playbook-fast-cash.md, Description, How to sell it, lines 274–287
  confirmations: 1
  boundary: >-
    Automated checkout is the exception, not the default; with it you build tension and open the cart to everyone at once, first come first serve.
  anchor_at: "playbook-fast-cash.md:275"
- id: D-playbooks-growth-054
  type: rule
  name: >-
    You will work more for these customers
  statement: >-
    The 10x to 50x price is paid for with unscalable delivery: you will work more for these customers and you will earn that money.
  why: >-
    The only thing that should shock them as much as the price is the value that goes with it.
  anchor: >-
    Will. Work. More. For. These. Customers. You will earn that money. Personally, I like work-
  source: >-
    playbook-fast-cash.md, Description, What to charge, lines 296–302
  confirmations: 1
  boundary: >-
    The play suits owners willing to deliver unscalable work; the author recommends pricing high enough to make you happy about providing it.
  anchor_at: "playbook-fast-cash.md:301"
- id: D-playbooks-growth-055
  type: antipattern
  name: >-
    Cutting the offer down for being unscalable
  statement: >-
    Stripping the unscalable components out of a Fast Cash offer.
  why: >-
    Those unscalable solutions are the things that typically justify the crazy high price tags, so at a crazy high price they have to be included.
  anchor: >-
    you cut things for being ‘unscalable.’ Main reason: these ‘unscalable’ solutions are the things
  source: >-
    playbook-fast-cash.md, Ultra-Premium Examples, lines 374–383
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:379"
- id: D-playbooks-growth-056
  type: antipattern
  name: >-
    Taking the ultra-premium examples literally
  statement: >-
    Rejecting the play with I’m not giving anyone cell phone access, treating the example components as the requirement.
  why: >-
    It is not about giving people access to your cell, it is about offering crazy value; you balance what your customers find crazy valuable, how many of those things you will do, and whether they demand prices that overflow your bank account.
  anchor: >-
    Ultra Premium Prices for Ultra Premium Value . If you think to yourself “I’m not giv-
  source: >-
    playbook-fast-cash.md, Important Points, lines 421–426
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:422"
- id: D-playbooks-growth-057
  type: rule
  name: >-
    Exclude cooled-off leads
  statement: >-
    Leads you have not contacted for six months or more are excluded from the Fast Cash offer and warmed up for the next one.
  why: >-
    Fast Cash Plays work best with warm audiences; for now you stick with existing customers and past customers in good standing.
  anchor: >-
    Exclude Cooled-Off Leads . Fast Cash Plays work best with warm audiences. So, if your
  source: >-
    playbook-fast-cash.md, Important Points, lines 427–430
  confirmations: 1
  boundary: >-
    Audience limit: existing customers, past customers in good standing and engaged leads; neglected lists are out until warmed up.
  anchor_at: "playbook-fast-cash.md:427"
- id: D-playbooks-growth-058
  type: rule
  name: >-
    Weekly does not work, yearly does not work
  statement: >-
    Fast Cash Plays are run about once a quarter; every week does not work and once a year does not really work either.
  why: >-
    A quarter cleans up the pipeline of on-the-fence leads, increases the value of every customer, keeps something new going on, and leaves time to deliver and reset before the next one.
  anchor: >-
    As much as it would be great to run Fast Cash Plays every week... it doesn’t work. On the
  source: >-
    playbook-fast-cash.md, 5 Reasons To Run Fast Cash Offers Every 90 Days, lines 458–471
  confirmations: 1
  boundary: >-
    Cadence boundary of the play; the author allows twice a year if you feel you need longer than twelve weeks to cool off between promotions.
  anchor_at: "playbook-fast-cash.md:460"
- id: D-playbooks-growth-059
  type: rule
  name: >-
    Repeat buying holds only if delivery holds
  statement: >-
    People who buy more often are more likely to keep buying, provided your delivery doesn’t suck.
  why: >-
    The claim that the play increases the value of every customer is conditional on the delivery of what was sold.
  anchor: >-
    likely to keep buying (provided your delivery doesn’t suck).
  source: >-
    playbook-fast-cash.md, 5 Reasons To Run Fast Cash Offers Every 90 Days, lines 466–467
  confirmations: 1
  boundary: >-
    Delivery quality is the precondition on the retention benefit of the play.
  anchor_at: "playbook-fast-cash.md:467"
- id: D-playbooks-growth-060
  type: rule
  name: >-
    Profit claim assumes break-even or better
  statement: >-
    The claim that all the additional revenue from warm leads drops straight to the bottom line assumes the business is break-even or better.
  why: >-
    Even a smaller percentage of revenue then becomes a much larger percentage of profit; in the author’s early days Cash Plays were about 15% of annual revenue and nearly half his profit.
  anchor: >-
    Fifth,  assuming  your  business  is  break-even  or  better,  all  the  additional  revenue  from
  source: >-
    playbook-fast-cash.md, 5 Reasons To Run Fast Cash Offers Every 90 Days, lines 472–475
  confirmations: 1
  boundary: >-
    A loss-making business does not get the drop-to-the-bottom-line effect claimed here.
  anchor_at: "playbook-fast-cash.md:472"
- id: D-playbooks-growth-061
  type: antipattern
  name: >-
    Dismissing the play as not scalable
  statement: >-
    Owners do not run Fast Cash Plays because they think stuff like this isn’t scalable.
  why: >-
    The author says it is scalable, and that what helps you scale is all the extra high-margin money you just made selling to existing customers; the worked benchmark quadruples net income and adds 22 new customers off four promotions a year.
  anchor: >-
    happens). The crazy thing is - most people don’t because they think stuff like this isn’t “scal-
  source: >-
    playbook-fast-cash.md, ROI Benchmarks, lines 496–503
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:499"
- id: D-playbooks-growth-062
  type: antipattern
  name: >-
    Running the play badly
  statement: >-
    Implementing the Cash Play incorrectly makes you seem like a shill, turns off good customers and makes room for better competitors.
  why: >-
    The author states it as the downside case against the upside that one play a year pays for itself many years over.
  anchor: >-
    implement this incorrectly, you can seem like a shill, turn off
  source: >-
    playbook-fast-cash.md, DO YOU WANT TO SCALE YOUR BUSINESS?, lines 528–537
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:536"
- id: D-playbooks-growth-063
  type: rule
  name: >-
    On top of the paid ads chapters, not instead of
  statement: >-
    GOATed Ads is used on top of the paid ads chapters in $100M Leads, not as a replacement for them.
  why: >-
    It takes those ideas and puts them on steroids.
  anchor: >-
    Disclaimer: This is to be used on top of the paid ads chapters in $100M Leads.
  source: >-
    playbook-goated-ads.md, GOATed Ads, lines 44–46
  confirmations: 1
  boundary: >-
    A prerequisite the author sets on his own playbook: the paid-ads fundamentals come from $100M Leads.
  anchor_at: "playbook-goated-ads.md:44"
- id: D-playbooks-growth-064
  type: antipattern
  name: >-
    Blaming market saturation for the ad ceiling
  statement: >-
    Concluding that the market is saturated when cost to acquire shoots up past a certain daily ad spend.
  why: >-
    You haven’t saturated the platform, you have gotten all the low hanging fruit and hit a wall with your ad quality, not with the market; the better your ads, the bigger the audience they convert.
  anchor: >-
    hit a wall with your ad quality, not with the market. The better your ads, the bigger the au-
  source: >-
    playbook-goated-ads.md, GOATed Ads, lines 48–81
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:73"
- id: D-playbooks-growth-065
  type: antipattern
  name: >-
    Making five new ads a month
  statement: >-
    Recording ads once a month and producing about five new ones.
  why: >-
    Ads scale by making better ads, and you only do that by making more, way more: fifty hooks times three to five meats times one to three CTAs is 150 to 750 ads per week, and the company that switched doubled in two quarters.
  anchor: >-
    “Wait. You’re only making ads once a month?”
  source: >-
    playbook-goated-ads.md, GOATed Ads, lines 53–67
  confirmations: 1
  anchor_at: "playbook-goated-ads.md:55"
- id: D-playbooks-growth-066
  type: rule
  name: >-
    Labels are clean, reality is messy
  statement: >-
    The five levels of awareness are treated as a continuous scale rather than five kinds of people; the author has never met the people in the pyramid.
  why: >-
    All he knows is that the larger the audience he reaches, the more varied and exceptional his ads must be, which is why he adapted the chunked model into a continuous one.
  anchor: >-
    I want to be clear, I’ve never met these people in Eugene’s pyramid. Labels are clean.
  source: >-
    playbook-goated-ads.md, Why Ads Hit A Wall And How To Scale Past It, lines 96–130
  confirmations: 1
  boundary: >-
    The five levels come from Eugene Schwartz (spelled Swartz at line 98) and are used as a continuum, not as an audience taxonomy to segment by.
  anchor_at: "playbook-goated-ads.md:126"
- id: D-playbooks-growth-067
  type: antipattern
  name: >-
    Putting the work into the recording
  statement: >-
    Treating ad production as a recording session rather than as preparation.
  why: >-
    Ads are made in research, not in recording: ninety percent of the work in advertising is in the preparation to record, not in the recording itself.
  anchor: >-
    in research, not in recording. In other words, ninety percent of the work in advertising is in
  source: >-
    playbook-goated-ads.md, Next Time You film, lines 159–165
  confirmations: 1
  anchor_at: "playbook-goated-ads.md:161"
- id: D-playbooks-growth-068
  type: antipattern
  name: >-
    Splitting prep time away from hooks
  statement: >-
    Spending prep time on the body of the ad instead of putting 80% of it into hooks, 20% into the meat and roughly none into CTAs.
  why: >-
    If someone doesn’t make it through the hook, then nothing else matters.
  anchor: >-
    And this follows because if someone doesn’t make it through the hook, then nothing
  source: >-
    playbook-goated-ads.md, Next Time You film, lines 162–167
  confirmations: 1
  anchor_at: "playbook-goated-ads.md:166"
- id: D-playbooks-growth-069
  type: rule
  name: >-
    Skip your own past winners on the first run
  statement: >-
    The first hook source, winning hooks from your previous ads, is skipped if it is your first time running ads.
  why: >-
    Those are literally past winners that you reuse, and over time you develop a stable of winners; there is none on a first run.
  anchor: >-
    much runway one good hook can give you. Note: If it’s your first time running ads, skip
  source: >-
    playbook-goated-ads.md, Writing Hooks For Immediate Results From Previous Winners, lines 179–183
  confirmations: 1
  boundary: >-
    Stage boundary: the hook-sourcing list has one item that does not exist for a business with no ad history.
  anchor_at: "playbook-goated-ads.md:182"
- id: D-playbooks-growth-070
  type: antipattern
  name: >-
    Modelling ads from platform ad libraries
  statement: >-
    Using platform ad libraries as the source of hooks to model.
  why: >-
    You will have a hard time figuring out which ads perform well enough to justify modeling, and most people don’t know what they’re doing, so big ad libraries are a fun place for ideas more than a guarantee of winners.
  anchor: >-
    out which ads perform well enough to justify modeling. Remember, most people don’t
  source: >-
    playbook-goated-ads.md, Writing Hooks For Immediate Results From Previous Winners, lines 202–209
  confirmations: 1
  authors_caveat: >-
    The author lists it last rather than excluding it: for inspiration he looks at companies he knows run great paid ads and checks the hooks they use.
  anchor_at: "playbook-goated-ads.md:205"
- id: D-playbooks-growth-071
  type: antipattern
  name: >-
    Writing only offer and proof hooks
  statement: >-
    Continuing to write hooks that focus on your offer or your proof once you have capped your ad spend.
  why: >-
    You convert a small slice of a larger audience very well; to grab a bigger slice you meet the audience where they are, at their level of awareness.
  anchor: >-
    Here’s how: If you continue to write hooks that focus on your offer or proof, you will
  source: >-
    playbook-goated-ads.md, Writing Expansion Hooks To Enter New Markets, lines 213–222
  confirmations: 1
  anchor_at: "playbook-goated-ads.md:219"
- id: D-playbooks-growth-072
  type: antipattern
  name: >-
    Ninety percent of hooks in the Most Aware bucket
  statement: >-
    Writing nearly all hooks at the Most Aware level.
  why: >-
    Spreading them out captures a bigger slice; when in doubt go a little broader, since you still catch your warm audience and attract some of the colder audience too.
  anchor: >-
    If 90% of your hooks land in the “Most aware” bucket, spread them out to capture a
  source: >-
    playbook-goated-ads.md, Writing Expansion Hooks To Enter New Markets, lines 356–358
  confirmations: 1
  anchor_at: "playbook-goated-ads.md:356"
- id: D-playbooks-growth-073
  type: rule
  name: >-
    The $5 Foot Long works because the nation already knows the product
  statement: >-
    A national offer-driven hook works only where the brand and the product are already known.
  why: >-
    Subway ran it for 20 years as a sandwich ad; it works because the entire nation knows the product, after hundreds of millions spent getting everyone to know the brand, and everyone knows what a sandwich is.
  anchor: >-
    (which for 20 years ran as a sandwich ad). This only works because the entire nation knows
  source: >-
    playbook-goated-ads.md, Writing Expansion Hooks To Enter New Markets, lines 339–347
  confirmations: 1
  boundary: >-
    Awareness level of the audience, not the size of the advertiser, decides which hook type is allowed; a known brand plus a known product is what licenses an offer hook to everyone.
  anchor_at: "playbook-goated-ads.md:342"
- id: D-playbooks-growth-074
  type: antipattern
  name: >-
    An offer hook from a no-name brand to a national audience
  statement: >-
    A no-name competitor with a product that needs education leads with an offer-driven hook to a national audience.
  why: >-
    It would be the closest thing to burning money on fire.
  anchor: >-
    a national audience would be the closest thing to burning money on fire. On the other ex-
  source: >-
    playbook-goated-ads.md, Writing Expansion Hooks To Enter New Markets, lines 347–351
  confirmations: 1
  anchor_at: "playbook-goated-ads.md:351"
- id: D-playbooks-growth-075
  type: rule
  name: >-
    Frameworks, not a magical recipe
  statement: >-
    The awareness-level hook templates are frameworks rather than a recipe; real campaigns break the pattern in both directions.
  why: >-
    A national ad can carry a killer offer-driven hook, and a broad curiosity piece can convert a very warm audience, as a movie trailer does; this is not written in stone.
  anchor: >-
    That being said, think of these more as frameworks than some magical recipe. You may
  source: >-
    playbook-goated-ads.md, Writing Expansion Hooks To Enter New Markets, lines 339–355
  confirmations: 1
  boundary: >-
    The awareness-to-hook mapping is a tool for writing the fifty hooks, not a law about which hook converts which audience.
  anchor_at: "playbook-goated-ads.md:339"
- id: D-playbooks-growth-076
  type: rule
  name: >-
    Five formats, not the only formats
  statement: >-
    Demonstration, testimonial, education, story and faceless are the formats the author has used that worked, not a closed list.
  why: >-
    They have worked across services, education, physical products, brick and mortar and software, and the author encourages mixing and matching them.
  anchor: >-
    are the only formats. I’m just saying these are the ones I’ve used that worked. And they’ve
  source: >-
    playbook-goated-ads.md, The Ad Meat, lines 371–374
  confirmations: 1
  boundary: >-
    A list of what worked for the author, offered as a reference to fall back on when stuck, not as a taxonomy of ads.
  anchor_at: "playbook-goated-ads.md:372"
- id: D-playbooks-growth-077
  type: antipattern
  name: >-
    An ad that does not tell the audience what to do
  statement: >-
    Leaving the next step unsaid: no button, number, reply word, website or code spelled out.
  why: >-
    Your audience can only know what to do if you tell them, and if you don’t tell anyone to take action you will have significantly fewer people taking action; after the ad they have huge motivation for a tiny time.
  anchor: >-
    So many ads still don’t do this. Your audience can only know what to do if you tell them.
  source: >-
    playbook-goated-ads.md, CTA - Call To Action, lines 505–529
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:512"
- id: D-playbooks-growth-078
  type: antipattern
  name: >-
    Telling without showing what happens next
  statement: >-
    Stating the next step without demonstrating it: the click, the form, the fields, the submit.
  why: >-
    When they click and get exactly what they expected they are more likely to follow through; it provides the ultimate congruence, and almost no one does it.
  anchor: >-
    your number. This seems obvious and basic, but almost no one does it…and it really works.
  source: >-
    playbook-goated-ads.md, CTA - Call To Action, lines 513–519
  confirmations: 1
  anchor_at: "playbook-goated-ads.md:517"
- id: D-playbooks-growth-079
  type: rule
  name: >-
    A sound CTA has never broken a campaign, but no CTA has
  statement: >-
    CTAs are not a place to optimise: once one follows the fundamentals it works well enough and is kept.
  why: >-
    CTAs take the least effort to make and come last; the author tests a few by running three identical hook plus meat combinations to the same audience, changing only the CTA, then sticks with the winner.
  anchor: >-
    fundamentals it will work well enough. A sound CTA’s hasn’t ever broken a campaign, but
  source: >-
    playbook-goated-ads.md, CTA - Call To Action, lines 525–564
  confirmations: 1
  boundary: >-
    The effort split holds: roughly no prep time goes to CTAs, against 80% for hooks and 20% for the meat.
  anchor_at: "playbook-goated-ads.md:531"
- id: D-playbooks-growth-080
  type: antipattern
  name: >-
    Getting bored of your own winning ads
  statement: >-
    Retiring ads because the advertiser is tired of them.
  why: >-
    New customers enter your market every day and it will still be the first time they see it; when a few ads wildly outperform the rest you double down and reuse the same hooks to make even more winners.
  anchor: >-
    do. So, don’t get bored repeating the same stuff. it’ll still be the first time they see it.
  source: >-
    playbook-goated-ads.md, Scale It, lines 617–625
  confirmations: 1
  anchor_at: "playbook-goated-ads.md:620"
- id: D-playbooks-growth-081
  type: rule
  name: >-
    Kaleidoscope Ads come after winners
  statement: >-
    The Kaleidoscope Ads step cannot be run until this process has produced winning ads.
  why: >-
    This playbook is how the author finds winners; Kaleidoscope is how he takes them to the moon, and you can’t do those without this.
  anchor: >-
    you have winners, you’ll be ready for the next step: Kaleidoscope Ads. It’s how I take ads to
  source: >-
    playbook-goated-ads.md, Final Note, lines 626–629
  confirmations: 1
  boundary: >-
    Sequence boundary: this playbook is the prerequisite step, not the scaling step.
  anchor_at: "playbook-goated-ads.md:628"
```
