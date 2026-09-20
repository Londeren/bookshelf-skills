# Улов фазы 1 — $100M Playbooks: Lead Nurture, Retention, Fast Cash, GOATed Ads (2025) (ярус 2), тип E: глоссарий

Группа `tier2-playbooks-growth`, слаг `playbooks-growth`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **53** (экстрактор вернул 53, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `playbook-lead-nurture.md` | 1–1148 | 2 | 20 |
| `playbook-retention.md` | 1–835 | 2 | 16 |
| `playbook-fast-cash.md` | 1–779 | 2 | 7 |
| `playbook-goated-ads.md` | 1–707 | 1 | 10 |

## Как собран файл

Экстрактор E (Glossary) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-playbooks-growth.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-playbooks-growth-E.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: E-playbooks-growth-001
  type: term
  name: >-
    Schedule rate
  statement: >-
    Schedule rate is the first of the three lead-nurture metrics: the share of engaged leads who book an appointment.
  definition: >-
    Schedule rate is the percentage of engaged leads who schedule an appointment.
  not_to_confuse_with: >-
    Show rate, which is measured on scheduled leads rather than on engaged leads; the author defines the two in the same breath.
  anchor: >-
    Schedule rate is the percentage of engaged leads who
  source: >-
    playbook-lead-nurture.md, Description, lines 190–191
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:190"
- id: E-playbooks-growth-002
  type: term
  name: >-
    Show rate
  statement: >-
    Show rate is the share of already scheduled leads who actually turn up to the appointment.
  definition: >-
    Show rate is the percentage of scheduled leads that show up to the appointment.
  why: >-
    Show rates matter so much because the more people who show up to buy your thing, the more of your thing you will sell.
  not_to_confuse_with: >-
    Schedule rate (measured on engaged leads) and throughput (engaged leads all the way to the show).
  anchor: >-
    Show rate is the percentage of scheduled leads that show up to the
  source: >-
    playbook-lead-nurture.md, Description, lines 191–192
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:191"
- id: E-playbooks-growth-003
  type: term
  name: >-
    Throughput
  statement: >-
    Throughput is the end-to-end share of engaged leads who end up showing, the product of schedule rate and show rate.
  definition: >-
    Throughput is the total percentage of engaged leads that show up. In the author example: 100 leads, 50% schedule rate, 50% show rate, throughput 25% (25 shows out of 100 leads).
  not_to_confuse_with: >-
    Show rate, which is counted only on the leads who already scheduled.
  anchor: >-
    Throughput is the total percentage of engaged leads that show up.
  source: >-
    playbook-lead-nurture.md, Description, line 192
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:192"
- id: E-playbooks-growth-004
  type: term
  name: >-
    Lead nurture (medium-term)
  statement: >-
    Lead nurture in this method is the stage between advertising and the sale, and its measured object is the 30-day show rate.
  definition: >-
    Lead nurturing occurs after advertising and before sales. The time after they show interest in your thing but before they buy it. This playbook covers medium-term lead nurture - aka - maximizing 30-day show rates.
  not_to_confuse_with: >-
    Long term follow up - aka emails, podcasts, and content - which the author says he covers in other places.
  anchor: >-
    Lead nurturing occurs after advertising and before sales. The time after they show interest
  source: >-
    playbook-lead-nurture.md, Next Up: The Four Pillars of Lead Nurture, lines 218–220
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:218"
- id: E-playbooks-growth-005
  type: term
  name: >-
    Speed to contact
  statement: >-
    Speed to contact, the second pillar, covers both how fast you answer a lead and how far into the future you let them book.
  definition: >-
    Speed to contact: How fast you respond to leads and how far out you let them schedule appointments.
  anchor: >-
    Speed  to  contact:  How  fast  you  respond  to  leads  and  how  far  out  you  let  them
  source: >-
    playbook-lead-nurture.md, Four Pillars of Lead Nurture, lines 231–232
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:231"
- id: E-playbooks-growth-006
  type: term
  name: >-
    Personalization
  statement: >-
    Personalization, the third pillar, means making every contact useful and relevant to that particular lead rather than templated.
  definition: >-
    Personalization: Making communication with leads useful and relevant to them. Personalization means making yourself useful, relevant, and pleasant to individual leads.
  why: >-
    The more personal the follow-up, the more likely they will respond, and the more often they respond, the more likely they will show up.
  anchor: >-
    Personalization: Making communication with leads useful and relevant to them.
  source: >-
    playbook-lead-nurture.md, Four Pillars of Lead Nurture, line 236
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:236"
- id: E-playbooks-growth-007
  type: term
  name: >-
    volume
  statement: >-
    Volume, the fourth pillar, is how many times you reach out to a lead before giving up on them.
  definition: >-
    volume: The number of times you reach out to leads before giving up. volume simply means the number of times you do something.
  anchor: >-
    volume: The number of times you reach out to leads before giving up.
  source: >-
    playbook-lead-nurture.md, Four Pillars of Lead Nurture, line 241
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:241"
- id: E-playbooks-growth-008
  type: term
  name: >-
    Availability
  statement: >-
    Availability, the first pillar, is the number of open appointment slots plus how far out leads may book them.
  definition: >-
    Availability is a combination of how many appointment slots you have and how far out leads can schedule them. In the pillar list: Availability: The number of open appointment slots you have.
  why: >-
    If you do not have availability when leads have availability, they either do not schedule at all or schedule at a bad time for them, and a bad time means a high chance of skipping or ghosting.
  anchor: >-
    Availability is a combination of how many appointment slots you have and how far out
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability, Description, lines 303–304
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:303"
- id: E-playbooks-growth-009
  type: term
  name: >-
    Speed To First Contact
  statement: >-
    Speed to first contact is the time between a lead expressing interest and your first call or message to them.
  definition: >-
    First contact refers to how long it takes you to call or message leads after they express interest in your stuff. For example, when they reply to ads, join your list, or self-schedule.
  why: >-
    The slower you contact leads, the more times you have to contact them before they buy; the faster you contact them, the fewer times you have to.
  anchor: >-
    Speed To First Contact : First contact refers to how long it takes you to call or message
  source: >-
    playbook-lead-nurture.md, Pillar II: Speed, How To Increase Speed To Contact, lines 437–438
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:437"
- id: E-playbooks-growth-010
  type: term
  name: >-
    Speed To First Appointment
  statement: >-
    Speed to first appointment is the delay between the moment an appointment is booked and the moment it happens.
  definition: >-
    Speed To First Appointment means the amount of time between scheduling a sales appointment and having the sales appointment.
  why: >-
    The shorter the delay between scheduling appointments and having them, the higher the show rate gets.
  anchor: >-
    Speed To First Appointment means the amount of time between scheduling a sales
  source: >-
    playbook-lead-nurture.md, Pillar II: Speed, 2) Speed To First Appointment, lines 457–458
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:457"
- id: E-playbooks-growth-011
  type: term
  name: >-
    hot handoff
  statement: >-
    A hot handoff is connecting a qualified lead to the closer in a three-way message while you still have them, instead of letting them wait for the appointment alone.
  definition: >-
    You connect them in a three-way message with the closer who is going to take the appointment (this is the hot hand off I referenced last page). If not, do a hot handoff to an active closer.
  anchor: >-
    to take the appointment (this is the hot hand off I referenced last page).
  source: >-
    playbook-lead-nurture.md, Pillar II: Speed, lines 526–527
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:527"
- id: E-playbooks-growth-012
  type: term
  name: >-
    Speed of Response
  statement: >-
    Speed of response is how fast you answer a lead in the window between their booking and the appointment itself.
  definition: >-
    The last element of speed is how fast you get back to leads after they schedule their appointment and before it happens. This is where leads fall through the cracks.
  anchor: >-
    The  last  element  of  speed  is  how  fast  you  get  back  to  leads  after  they  schedule
  source: >-
    playbook-lead-nurture.md, Pillar II: Speed, 3) Speed of Response, lines 547–548
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:547"
- id: E-playbooks-growth-013
  type: term
  name: >-
    push incentive
  statement: >-
    A push incentive is something good given to the lead before the appointment so that reciprocity pushes them to show.
  definition: >-
    A push incentive means they do the good stuff before they arrive with the intention to evoke reciprocity. Both are a kind of social contract.
  not_to_confuse_with: >-
    A pull incentive, where the good stuff is only received after they arrive.
  anchor: >-
    I’ve  seen  incentives  used  in  two  ways:  “push”  and  “pull.”  A  push  incentive  means
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, 5) Incentives, lines 745–746
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:745"
- id: E-playbooks-growth-014
  type: term
  name: >-
    pull incentive
  statement: >-
    A pull incentive is something good the lead only gets once they arrive, which motivates the action of showing up.
  definition: >-
    A pull incentive means the lead gets good stuff after they arrive with the intention to motivate the action.
  not_to_confuse_with: >-
    A push incentive, which is given before the appointment and works through reciprocity.
  anchor: >-
    incentive means the lead gets good stuff after they arrive with the intention to motivate
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, 5) Incentives, lines 747–748
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:747"
- id: E-playbooks-growth-015
  type: term
  name: >-
    A/B “Pull” Incentive
  statement: >-
    An A/B incentive is a two-option question about what the lead will receive at the appointment, where both options presuppose they show.
  definition: >-
    Leads choose what they get when they show up. But both choices assume they will show. A/B Incentives depend on three things. First, leads should want the thing. Second, it should have obvious connections to the thing you will offer them. Last, that you incurred some real cost by preparing it.
  not_to_confuse_with: >-
    The gift card push incentive: the first incentive was a gift, the second is a bribe.
  anchor: >-
    Leads choose what they get when they show up. But both choices assume they’ll show.
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, 5) Incentives, line 767
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:767"
- id: E-playbooks-growth-016
  type: term
  name: >-
    Double-dial
  statement: >-
    Double-dialing means calling a second time immediately after an unanswered call rather than waiting for the next cadence step.
  definition: >-
    Double-dial. If you call once and get nothing, immediately call again.
  why: >-
    They gave you permission to contact them, and you will call from a strange number: many phones block the first call and let the second call through, so even a lead expecting your call may miss it.
  anchor: >-
    Double-dial.  If  you  call  once  and  get  nothing,  immediately call  again.
  source: >-
    playbook-lead-nurture.md, Pillar IV: Volume, 1) Scheduling Appointments, line 852
  confirmations: 2
  authors_caveat: >-
    Obey the laws of your area.
  anchor_at: "playbook-lead-nurture.md:852"
- id: E-playbooks-growth-017
  type: term
  name: >-
    BAMFAM
  statement: >-
    BAMFAM means booking the next appointment while you are still in the current one, never ending a call with a promise to circle back (the author credits it to Sharran Srivatsaa).
  definition: >-
    BAMFAM or Book-A-Meeting-From-A-Meeting. Internally, we call it BAMFAM as a way of life. Never let a lead go to no-man-s land.
  why: >-
    People have a higher chance of showing up to appointments if you schedule them, and you have the highest chance of scheduling an appointment if you do it with them in real time.
  anchor: >-
    He called it BAMFAM or “Book-A-Meeting-From-A-Meeting.”
  source: >-
    playbook-lead-nurture.md, Pillar IV: Volume, 3) Book Their Next Appointment At The Current Appointment, line 912
  confirmations: 3
  anchor_at: "playbook-lead-nurture.md:912"
- id: E-playbooks-growth-018
  type: term
  name: >-
    garbage man
  statement: >-
    A garbage man is a salesperson who takes the leads everyone else rejects as under-qualified and works them anyway.
  definition: >-
    He offered to take all the under-qualified leads from the whole team. Being garbage men - do not judge a book by its cover. Be an equal opportunity salesman. Every lead is an opportunity for practice.
  anchor: >-
    After this conversation, Jacob got the nickname “garbage man.” He offered to take all
  source: >-
    playbook-lead-nurture.md, Execution, lines 1006–1007
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:1006"
- id: E-playbooks-growth-019
  type: term
  name: >-
    reds / yellows / greens; “Yellow is the new gold”
  statement: >-
    Leads are scored by colour - reds truly unqualified, yellows less qualified, greens prime - and the middle colour is the one the author says is undervalued.
  definition: >-
    Our lead scoring system was simple. reds are truly unqualified. Yellows are less qualified. Greens are prime leads. Over time he started saying, Yellows are the new gold.
  not_to_confuse_with: >-
    The 1-5 score used for routing best leads to best closers, which the author gives as the alternative form of the same scoring.
  anchor: >-
    Our  lead  scoring  system  was  simple.  reds  are  truly  unqualified.  Yellows  are  less
  source: >-
    playbook-lead-nurture.md, Execution, lines 1011–1012
  confirmations: 3
  anchor_at: "playbook-lead-nurture.md:1011"
- id: E-playbooks-growth-020
  type: term
  name: >-
    Culture
  statement: >-
    Culture here means nothing more than the rules that mark behaviour as good or bad inside the organization, which is why it is the lever for making lead work happen.
  definition: >-
    Culture refers to the rules that govern good and bad behavior in an organization. Simple as that. We want to have a culture of execution. Or accepting of the behaviors that make us available, fast, personal, and persistent. And reject the behaviors that make us unavailable, slow, boring, and fragile.
  anchor: >-
    Culture refers to the rules that govern good and bad behavior in an organization.
  source: >-
    playbook-lead-nurture.md, Execution, Tactics, lines 1032–1033
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:1032"
- id: E-playbooks-growth-021
  type: term
  name: >-
    leaky bucket business
  statement: >-
    A leaky bucket business is one that loses customers about as fast as it wins them, so it dies the moment acquisition slips.
  definition: >-
    They would lose their customers as fast as they would get them. And a business with a revolving door of customers is hardly a business at all. I call this a leaky bucket business. And it is a scary way to live. If you get behind at all... your business dies.
  anchor: >-
    I call this a leaky bucket business. And it’s a scary way to live.
  source: >-
    playbook-retention.md, Churn Checklist (opening), line 73
  confirmations: 1
  anchor_at: "playbook-retention.md:73"
- id: E-playbooks-growth-022
  type: term
  name: >-
    common factors analysis
  statement: >-
    A common factors analysis is asking many experts about one problem and keeping only the factors that repeat across their answers.
  definition: >-
    You look through all the notes and do a common factors analysis. A fancy way to say Find the stuff they have in common. Say every expert lists 5 factors contributing to your problem. But, if you overlap all the factors from all the experts the same 2 pop up each time - solve for those.
  why: >-
    Since everyone puts their own spin on stuff, talking to as many as you can helps eliminate bias and reveals the core problem.
  anchor: >-
    the notes and do a “common factors analysis.” A fancy way to say “Find the stuff they have
  source: >-
    playbook-retention.md, Solving Problems Like The Big Boys, lines 91–92
  confirmations: 2
  anchor_at: "playbook-retention.md:91"
- id: E-playbooks-growth-023
  type: term
  name: >-
    The 5 Horsemen of Retention
  statement: >-
    The 5 Horsemen of Retention are the five habits common to the lowest-churn gym owners: track attendance, reach out twice a week, handwritten cards, member events, exit interviews.
  definition: >-
    I researched all the gym owners with less than 3% month-over-month churn for the last 6 months. I interviewed each about every single thing they did to reduce churn. I found 5 common factors - which became The 5 Horsemen of Retention.
  applies_when: >-
    Gyms and comparable memberships; the author says The Five Horsemen for gyms is alive and well.
  anchor: >-
    I found 5 common factors – which became The 5 Horsemen of Retention.
  source: >-
    playbook-retention.md, The 5 Horsemen of Retention, line 104
  confirmations: 2
  anchor_at: "playbook-retention.md:104"
- id: E-playbooks-growth-024
  type: term
  name: >-
    Exit interview (cancellation call)
  statement: >-
    An exit interview here is a save conversation held with a customer after they announce a cancellation and before they actually leave, not an HR debrief.
  definition: >-
    If a person says they want to leave then talk to them before they do. First, set the expectation you will require an exit interview when you onboard new customers. Second, use their cancellation notice as the sign to set up the exit interview.
  why: >-
    Done right it saves about half of phone and email cancellations; realistically you would cut churn by 25% assuming half show, a 33% increase in LTV.
  anchor: >-
    Exit interviews: If a person says they want to leave then talk to them before they do.
  source: >-
    playbook-retention.md, The 5 Horsemen of Retention, line 134
  confirmations: 2
  anchor_at: "playbook-retention.md:134"
- id: E-playbooks-growth-025
  type: term
  name: >-
    shaking the three
  statement: >-
    Shaking the three is the churn spike that arrives in the first month of retention work, before churn falls.
  definition: >-
    Churn going up right away raises eyebrows - but I call it shaking the three. First, you have got the people who would have canceled anyway. Second, some people have churned as consumers but automated billing still occurs. So once you remind them of it, they cancel.
  why: >-
    Owners are told to expect churn to increase at first; as long as they do the stuff, churn goes down month after month.
  anchor: >-
    more gyms started to feel ok with “shaking the three,” their numbers looked like this:
  source: >-
    playbook-retention.md, The 5 Horsemen Of Retention: Results, lines 152–159
  confirmations: 2
  anchor_at: "playbook-retention.md:159"
- id: E-playbooks-growth-026
  type: term
  name: >-
    Churn
  statement: >-
    Churn is the share of the customers you had at the start of a period who left during it, counted only on that starting pool.
  definition: >-
    Churn refers to customers who leave over a specific period of time. Churn = people who left divided by original customer pool = 5 / 100 = 5%.
  not_to_confuse_with: >-
    Net change in customer count: churn only counts the pool of customers from the first timepoint, so signing zero or 1,000 new clients in the same month does not change it.
  anchor: >-
    Churn refers to customers who leave over a specific period of time. All businesses churn
  source: >-
    playbook-retention.md, What Is Churn?, lines 181–189
  confirmations: 2
  anchor_at: "playbook-retention.md:181"
- id: E-playbooks-growth-027
  type: term
  name: >-
    structural churn
  statement: >-
    Structural churn is the churn you carry because your customers - very small business owners - go out of business, independently of how well you serve them.
  definition: >-
    If you are in an industry where you serve VSMBs (very small business owners), you will have what is called structural churn. They go out of business. This makes your business, a high churn business. And that is okay.
  anchor: >-
    you  will  have  what’s  called  “structural  churn”.  They  go  out  of  business.
  source: >-
    playbook-retention.md, Author Note: Churn Varies By Industry, lines 327–328
  confirmations: 1
  anchor_at: "playbook-retention.md:328"
- id: E-playbooks-growth-028
  type: term
  name: >-
    Activation point
  statement: >-
    An activation point is a specific customer action or result that predicts how long that customer stays.
  definition: >-
    Activation points refer to leading indicators of customer retention. Use this template: Every customer that does (X thing) or gets (Y result) stays for longer than customers who do not.
  why: >-
    Make finding activation points your top priority. They have the greatest effect on customer churn.
  anchor: >-
    Activation points refer to leading indicators of customer retention.
  source: >-
    playbook-retention.md, Churn Checklist #1: Figure Out Your Activation Points, lines 360–361
  confirmations: 3
  anchor_at: "playbook-retention.md:360"
- id: E-playbooks-growth-029
  type: term
  name: >-
    Onboarding
  statement: >-
    Onboarding in this method means one thing only: teaching a new customer to reach the activation point you identified.
  definition: >-
    People use onboarding to mean lots of things. Here, I mean Teach customers how to hit the activation points I just painstakingly investigated. You can onboard with a booklet, a video, a call, an event, whatever.
  not_to_confuse_with: >-
    The general senses the word carries elsewhere; the author states explicitly that he narrows it.
  anchor: >-
    People use onboarding to mean lots of things. Here, I mean “Teach customers how to
  source: >-
    playbook-retention.md, Churn Checklist #2: Onboard Your Customers, lines 440–441
  confirmations: 1
  anchor_at: "playbook-retention.md:440"
- id: E-playbooks-growth-030
  type: term
  name: >-
    Usage Churn
  statement: >-
    Usage churn is a customer who has stopped using the product while still paying for it, which is a leading indicator of a real cancellation.
  definition: >-
    A leading indicator of churn is what is called Usage Churn, which is when a customer is still subscribed but no longer uses the product.
  not_to_confuse_with: >-
    Churn proper, which is only counted when they actually leave; a usage-churned customer is still on the books.
  anchor: >-
    A  leading  indicator  of  churn  is  what’s  called  “Usage  Churn”,  which  is  when  a
  source: >-
    playbook-retention.md, Pro Tip: Usage Churn, lines 527–528
  confirmations: 1
  anchor_at: "playbook-retention.md:527"
- id: E-playbooks-growth-031
  type: term
  name: >-
    Community linking
  statement: >-
    Community linking is deliberately tying members to each other rather than to you, so leaving costs them relationships.
  definition: >-
    Connect members to each other, not you. It is more scalable to facilitate multiple, deeper connections than one single tie to the group.
  why: >-
    It is easy to quit a membership, it is hard to leave a relationship. They come for the bikini. They stay for the community.
  anchor: >-
    Connect members to each other, not you. It’s more scalable to facilitate multiple, deeper
  source: >-
    playbook-retention.md, Churn Checklist #4: Community Linking, lines 537–538
  confirmations: 2
  anchor_at: "playbook-retention.md:537"
- id: E-playbooks-growth-032
  type: term
  name: >-
    big head, long tail
  statement: >-
    A big head, long tail model charges a large one-time fee priced on one-time value and a small recurring fee priced on the consumable value (2025 figures).
  definition: >-
    I call this a big head, long tail where you might charge $6,800 upfront for education or a setup fee, then $199 for the community and everything after that.
  why: >-
    The base continues to stack, so you might get 30 months of LTV out of the $199 and increase LTV from $6,800 to $12,800 because you are appropriately priced.
  anchor: >-
    I call this a “big head, long tail” where you might charge $6,800
  source: >-
    playbook-retention.md, Churn Checklist #6: Add Annual Payment Options, lines 604–605
  confirmations: 1
  authors_caveat: >-
    Include the recurring fee WITH the 1-time up front fee and not make it a second sale, otherwise you lose the price anchor that drives the retention.
  anchor_at: "playbook-retention.md:604"
- id: E-playbooks-growth-033
  type: term
  name: >-
    founder rate
  statement: >-
    A founder rate is a discount offered to the owner of a business to get them both to buy and to stay.
  definition: >-
    Implement founder rates to convert more people and keep them longer. A founder rate is a discount for the owner of a business. A 50% decrease is a great way to start (provided gross margins still there).
  anchor: >-
    A founder rate is a discount for the owner of a business.
  source: >-
    playbook-retention.md, Churn Checklist #6: Add Annual Payment Options, line 647
  confirmations: 1
  anchor_at: "playbook-retention.md:647"
- id: E-playbooks-growth-034
  type: term
  name: >-
    ACA framework
  statement: >-
    ACA is the shape of a routine check-in message: Acknowledge, Complement, Ask.
  definition: >-
    The subject of the reach out followed the ACA framework. Acknowledge what you have seen them do. Complement them on something. Ask a question.
  anchor: >-
    The subject of the reach out followed the ACA framework.
  source: >-
    playbook-retention.md, Churn Checklist #8: Survey Customers Regularly, lines 702–703
  confirmations: 3
  anchor_at: "playbook-retention.md:702"
- id: E-playbooks-growth-035
  type: term
  name: >-
    The four milestones (customer journey)
  statement: >-
    The customer journey is four milestones every customer should reach: activate, testimonial, refer, ascend.
  definition: >-
    You can start with the four milestones that I want every customer to do: activate, testimonial, refer, ascend. You can also incentivize by giving them something at each milestone.
  anchor: >-
    every customer to do: activate, testimonial, refer, ascend.
  source: >-
    playbook-retention.md, Churn Checklist #9: Make a Customer Journey, lines 714–715
  confirmations: 2
  authors_caveat: >-
    Besides activation, milestones 2-3-4 may all happen in different orders depending on the customer and business model.
  anchor_at: "playbook-retention.md:715"
- id: E-playbooks-growth-036
  type: term
  name: >-
    ascension
  statement: >-
    Ascension is the existing customer buying more from you, the last of the four milestones.
  definition: >-
    The last step - ascension - is one I want to emphasize. Customers get an itch to buy more stuff over time. And they are gonna buy it from you or the guy down the street.
  why: >-
    If someone just bought another thing from you, they are the least likely to churn, so you save yourself the churn and bring in new revenue at once.
  anchor: >-
    The last step - ascension- is one I want to emphasize. Customers get an itch to buy more
  source: >-
    playbook-retention.md, Churn Checklist #9: Make a Customer Journey, lines 717–718
  confirmations: 2
  anchor_at: "playbook-retention.md:717"
- id: E-playbooks-growth-037
  type: term
  name: >-
    Fast Cash Play
  statement: >-
    A Fast Cash Play is a limited-time, limited-spot, high-ticket offer run to the warmest audiences about four times a year.
  definition: >-
    Fast Cash Plays are limited time offers advertised to your warmest audiences. Fast Cash plays are limited in spots (scarcity), high touch (exclusivity), and sold for lots of money (big ticket), for a limited time (urgency).
  not_to_confuse_with: >-
    Nurturing new leads about your main offer, and the long term value-adds like content emails you use to keep your lists warm; the author separates all three.
  anchor: >-
    Fast  Cash  Plays are  limited  time  offers  advertised  to  your  warmest  audiences.
  source: >-
    playbook-fast-cash.md, Fast Cash Plays - What/How/Why, What Fast Cash Plays Are, lines 139–152
  confirmations: 2
  anchor_at: "playbook-fast-cash.md:139"
- id: E-playbooks-growth-038
  type: term
  name: >-
    warmest audiences
  statement: >-
    Your warmest audiences are current customers, previous customers and engaged leads - everyone who gave explicit permission to be contacted about what you sell.
  definition: >-
    Your warmest audiences include current customers, previous customers, and all engaged leads - all people who have given you explicit permission to contact them about the stuff you sell.
  not_to_confuse_with: >-
    Cooled-off or neglected leads, whom the author excludes from a Fast Cash Play.
  anchor: >-
    audiences include current customers, previous customers, and all engaged leads–all people
  source: >-
    playbook-fast-cash.md, Fast Cash Plays - What/How/Why, What Fast Cash Plays Are, lines 140–141
  confirmations: 2
  anchor_at: "playbook-fast-cash.md:140"
- id: E-playbooks-growth-039
  type: term
  name: >-
    10x The 10%
  statement: >-
    10x the 10% is the arithmetic that one customer in ten buying something at ten times the price doubles revenue.
  definition: >-
    10x The 10%: If you get 10% of your customers to pay 10x the price...you double your revenue. Since you already spent the money to get the customer, all the extra revenue (minus delivery) drops straight to the bottom line.
  anchor: >-
    10x The 10%: If you get 10% of your customers to pay 10x the price...you double your
  source: >-
    playbook-fast-cash.md, How Fast Cash Plays Work, lines 172–173
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:172"
- id: E-playbooks-growth-040
  type: term
  name: >-
    Cash Plays (Reactivation, Referral, Easy Cash, Fast Cash)
  statement: >-
    Cash Plays are the author's family of promotions run to the existing customer base, of which Fast Cash is the fastest-paying member.
  definition: >-
    There are lots of promotions you can run to your existing customers: Reactivation Plays. Referral Plays. Easy Cash Plays. We will start with the one that makes you the most money the fastest: Fast Cash.
  anchor: >-
    There are lots of promotions you can run to your existing customers: Reactivation Plays.
  source: >-
    playbook-fast-cash.md, Fast Cash Play Outline, lines 203–205
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:203"
- id: E-playbooks-growth-041
  type: term
  name: >-
    unscalable value
  statement: >-
    Unscalable value is the set of things you can only do in small numbers - attention, personalization, convenience, status, duration, speed, experience, access, network, secrets - and it is what a Fast Cash price is built on.
  definition: >-
    So think of all the most valuable things you can do that are unscalable. If you sell at a crazy high price, then you want to include the stuff before you cut things for being unscalable. Main reason: these unscalable solutions are the things that typically justify the crazy high price tags.
  anchor: >-
    you cut things for being ‘unscalable.’ Main reason: these ‘unscalable’ solutions are the things
  source: >-
    playbook-fast-cash.md, Ultra-Premium Examples, lines 379–380
  confirmations: 2
  anchor_at: "playbook-fast-cash.md:379"
- id: E-playbooks-growth-042
  type: term
  name: >-
    Cooled-Off Leads
  statement: >-
    Cooled-off leads are neglected leads you have not messaged for six months or more.
  definition: >-
    If your list has neglected leads - aka - you have not sent them anything for six months or more, consider excluding them from this offer but start warming them up for the next one.
  not_to_confuse_with: >-
    Warm audiences, which Fast Cash Plays are built for; for now just stick with existing customers and past customers in good standing.
  anchor: >-
    list has neglected leads - aka - you haven’t sent them anything for six months or more, con-
  source: >-
    playbook-fast-cash.md, Important Points, lines 427–428
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:428"
- id: E-playbooks-growth-043
  type: term
  name: >-
    the 4Rs
  statement: >-
    The 4Rs are what you collect from buyers once a Fast Cash Play has been delivered: Reviews, Results, Referrals, and Resells.
  definition: >-
    Collect the 4Rs at the end: Reviews, Results, Referrals, and Resells.
  anchor: >-
    Collect the 4Rs at the end: Reviews, Results, Referrals, and Resells.
  source: >-
    playbook-fast-cash.md, Fast Cash Checklist, line 564
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:564"
- id: E-playbooks-growth-044
  type: term
  name: >-
    ad kaleidoscope
  statement: >-
    The ad kaleidoscope is the author's device for multiplying one winning ad into 50 more hooks and 3-5 variations of the meat; he treats it as the step after you already have winners.
  definition: >-
    Find your best ads. Second, chop them into: hook, meat, CTA. Then we will run them through a kaleidoscope to make 50 more hooks and with it, generate 3-5 variations on the meat. Once you have winners, you will be ready for the next step: Kaleidoscope Ads.
  anchor: >-
    kaleidoscope to make 50 more hooks and with it, generate 3-5 variations on the meat. If we
  source: >-
    playbook-goated-ads.md, GOATed Ads (opening), line 65
  confirmations: 3
  authors_caveat: >-
    You cannot do Kaleidoscope Ads without the ad assembly process first; this playbook stops before it.
  anchor_at: "playbook-goated-ads.md:65"
- id: E-playbooks-growth-045
  type: term
  name: >-
    Most Aware
  statement: >-
    Most Aware is the warmest and smallest audience level - they know the product and only need the deal - and its hooks are offer driven (level from Eugene Swartz, so spelt in the source).
  definition: >-
    Most Aware: (bottom) The customer knows your product and only needs to know the deal. These hooks are typically offer driven.
  anchor: >-
    Most Aware: (bottom) The customer knows your product and only needs to know
  source: >-
    playbook-goated-ads.md, Why Ads Hit A Wall And How To Scale Past It, lines 106–108
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:106"
- id: E-playbooks-growth-046
  type: term
  name: >-
    Product-Aware
  statement: >-
    Product-Aware is the level where the customer knows what you sell but is unsure it fits, and its hooks are proof driven (level from Eugene Swartz, so spelt in the source).
  definition: >-
    Product-Aware: The customer knows what you sell but is not sure it is right for them. These hooks are typically proof driven.
  anchor: >-
    Product-Aware: The customer knows what you sell but isn’t sure it’s right for them.
  source: >-
    playbook-goated-ads.md, Why Ads Hit A Wall And How To Scale Past It, line 110
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:110"
- id: E-playbooks-growth-047
  type: term
  name: >-
    Solution-Aware
  statement: >-
    Solution-Aware is the level where the customer knows the result they want but not that your product delivers it, and its ads are promise driven (level from Eugene Swartz, so spelt in the source).
  definition: >-
    Solution-Aware: The customer knows the result they want but does not know your product can provide it. These ads are typically promise driven.
  anchor: >-
    Solution-Aware: The customer knows the result they want but doesn’t know your
  source: >-
    playbook-goated-ads.md, Why Ads Hit A Wall And How To Scale Past It, lines 113–115
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:113"
- id: E-playbooks-growth-048
  type: term
  name: >-
    Problem-Aware
  statement: >-
    Problem-Aware is the level where the customer feels the problem but does not know a solution exists, and its ads are pain driven (level from Eugene Swartz, so spelt in the source).
  definition: >-
    Problem-Aware: The customer senses they have a problem but does not know there is a solution. These ads are typically pain driven.
  anchor: >-
    Problem-Aware: The customer senses they have a problem but doesn’t know there’s
  source: >-
    playbook-goated-ads.md, Why Ads Hit A Wall And How To Scale Past It, lines 117–119
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:117"
- id: E-playbooks-growth-049
  type: term
  name: >-
    Completely Unaware
  statement: >-
    Completely Unaware is the coldest and largest audience level - no sense of a problem at all - and its ads are curiosity driven (level from Eugene Swartz, so spelt in the source).
  definition: >-
    Completely Unaware: (top) The customer does not know they have a problem or need. These ads are typically curiosity driven.
  anchor: >-
    Completely Unaware: (top) The customer doesn’t know they have a problem or
  source: >-
    playbook-goated-ads.md, Why Ads Hit A Wall And How To Scale Past It, lines 121–123
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:121"
- id: E-playbooks-growth-050
  type: term
  name: >-
    The Ad Assembly Process
  statement: >-
    Ads are not written one by one but assembled from three separately produced chunks - hooks, meats, CTAs - whose combinations give 150 to 750 ads a week.
  definition: >-
    I began chunking ad creation into an assembly line like a process. First, I would make fifty hooks. Then, I would record the three to five very well-thought-out scripts to match the hooks, and then I would have my one to three versions of my Call To Action or CTA. I was not really creating ads at all. I was assembling them. 50 hooks x 3-5 meat x 1-3 CTAs = 150 to 750 ads per week.
  anchor: >-
    into an assembly line like a process. First, I would make fifty hooks. Then, I would record
  source: >-
    playbook-goated-ads.md, The Ad Assembly Process, lines 145–147
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:145"
- id: E-playbooks-growth-051
  type: term
  name: >-
    expansion hooks
  statement: >-
    Expansion hooks are experimental hooks written to reach a colder, broader audience once the existing ad capacity is capped.
  definition: >-
    If you do need something new, especially to reach a broader audience, then you need to write expansion hooks. You may need to expand the audience you target with your hooks. I write experimental hooks to expand my ads into new markets.
  not_to_confuse_with: >-
    Hooks written off previous winners - the bread-and-butter ads that you make on a weekly basis.
  anchor: >-
    then you need to write expansion hooks.
  source: >-
    playbook-goated-ads.md, The Ad Assembly Process, Writing Expansion Hooks To Enter New Markets, lines 212–216
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:212"
- id: E-playbooks-growth-052
  type: term
  name: >-
    The Ad Meat (creative)
  statement: >-
    The meat is the body of the ad, the creative that fulfils the promise made by the hook.
  definition: >-
    Every ad has creative. It is the part of the ad that fulfills your hook. The creative aligns with the hook, the hook aligns with the audience's awareness level. The meat only takes twenty percent of my attention. The body of an ad gets rotated less often because fewer people see it.
  anchor: >-
    Every ad has creative. It’s the part of the ad that fulfills your hook.
  source: >-
    playbook-goated-ads.md, The Ad Meat, lines 364–368
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:364"
- id: E-playbooks-growth-053
  type: term
  name: >-
    The five ad formats (Demonstration, Testimonial, Education, Story, Faceless)
  statement: >-
    The meat comes in five named formats the author has used across industries: Demonstration, Testimonial, Education, Story and Faceless Ads, which he also mixes and matches.
  definition: >-
    Demonstration Ads: think live use or reactions, unboxing, comparisons, high production hero ads. Testimonial Ads: think user-generated content, direct to camera, podcast style, raw iPhone style testimonials, walk-n-talk rants, group testimonials, man-on-the-street interviews, influencer collabs. Education Ads: think explainer videos, how-to listicles, high performing organic content. Story Ads: think storytelling, lifestyle, warnings and opportunities, documentary style, skits, brand manifestos. Faceless Ads: think screenshots of customer comments or texts, text only, slide shows, animations, cartoon ads, visual effect based ads.
  anchor: >-
    When I looked back at all my ads, I used five major formats. No, I’m not saying these
  source: >-
    playbook-goated-ads.md, The Ad Meat, line 371
  confirmations: 2
  authors_caveat: >-
    No, I am not saying these are the only formats. I am just saying these are the ones I have used that worked.
  anchor_at: "playbook-goated-ads.md:371"
```
