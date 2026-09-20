# Улов фазы 1 — $100M Playbooks: Lead Nurture, Retention, Fast Cash, GOATed Ads (2025) (ярус 2), тип B: правила и критерии

Группа `tier2-playbooks-growth`, слаг `playbooks-growth`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **140** (экстрактор вернул 140, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `playbook-lead-nurture.md` | 1–1148 | 2 | 46 |
| `playbook-retention.md` | 1–835 | 2 | 48 |
| `playbook-fast-cash.md` | 1–779 | 2 | 26 |
| `playbook-goated-ads.md` | 1–707 | 1 | 20 |

## Как собран файл

Экстрактор B (Rules and criteria) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-playbooks-growth.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-playbooks-growth-B.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 1 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: B-playbooks-growth-001
  type: rule
  name: >-
    Take Appointments More Days Per Week
  statement: >-
    Appointments are offered all seven days of the week, not only on the five days the business happens to work.
  why: >-
    You pay rent, payroll and insurance seven days per week, so you might as well make money seven days per week; taking appointments seven days a week makes the business 40% more available to accept money.
  anchor: >-
    Take Appointments More Days Per Week: You pay your rent seven days per week.
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability, Tactics, line 333
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:333"
- id: B-playbooks-growth-002
  type: rule
  name: >-
    Take Appointments More Hours Per Day
  statement: >-
    Booking hours cover the hours when customers are free to buy rather than the hours the business finds convenient.
  why: >-
    Being open 9-5 Monday through Friday means being closed exactly when your customers are at work making money.
  anchor: >-
    Take Appointments More Hours Per Day: Be available to sell when your customers
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability, Tactics, line 345
  confirmations: 3
  anchor_at: "playbook-lead-nurture.md:345"
- id: B-playbooks-growth-003
  type: rule
  name: >-
    Nationwide booking window
  statement: >-
    A business selling nationwide in the US keeps its booking window open at least from 6 am to 6 pm PST.
  why: >-
    Those hours were found to cover the highest percentage of sales in the US relative to the hours, and you can always go beyond them; the checklist states 9 am to 9 pm EST as a good goal (2025).
  anchor: >-
    For businesses that sell nationwide we found 6 am to 6 pm PST covers the highest
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability, Tactics, line 349
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:349"
- id: B-playbooks-growth-004
  type: rule
  name: >-
    Give Leads More Flexible Appointment Times
  statement: >-
    Leads can pick a start time at least every 15 minutes, four options per hour, instead of only on the hour or half hour.
  why: >-
    Slots every 30 or 60 minutes make things convenient for the business, not for the lead.
  anchor: >-
    that makes things convenient for the business, not for the lead. Consider four scheduling
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability, Tactics, line 354
  confirmations: 2
  authors_caveat: >-
    Going at this alone produces some awkward gaps between appointments, and it may take extra salespeople to handle the extra volume.
  anchor_at: "playbook-lead-nurture.md:354"
- id: B-playbooks-growth-005
  type: rule
  name: >-
    Same appointment length, more start times
  statement: >-
    Appointment length stays the same when start times are split more finely; only the lead's choice of start time expands.
  anchor: >-
    just give people more freedom to choose when the appointment starts.
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability, Tactics, line 357
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:357"
- id: B-playbooks-growth-006
  type: rule
  name: >-
    Separate qualifying and closing calls
  statement: >-
    For more expensive offers, qualifying and closing happen on separate calls, with a 15-minute qualifying call and separate calendars for setters and closers.
  why: >-
    A 15-minute qualifying call removes the awkward gaps created by 15-minute scheduling increments and makes more money.
  applies_when: >-
    Expensive offers, where the author recommends qualifying and closing on separate calls.
  anchor: >-
    for more expensive stuff), then a 15-minute qualifying call solves this issue entirely. The
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability, Tactics, line 364
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:364"
- id: B-playbooks-growth-007
  type: rule
  name: >-
    Have Inbound, Outbound, and Self-Scheduling Options
  statement: >-
    All three booking routes exist at once: you call leads, leads call you, and leads schedule themselves online.
  why: >-
    The more ways you give people to book an appointment, the more people will book an appointment.
  anchor: >-
    Have Inbound, Outbound, and Self-Scheduling Options . You can call leads to set
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability, Tactics, line 367
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:367"
- id: B-playbooks-growth-008
  type: rule
  name: >-
    Scheduler header, headline, subheadline
  statement: >-
    The top of the scheduling page confirms the lead is in the right place and then states the next thing to do and why to do it.
  anchor: >-
    Make sure the header confirms they’re in the right place. Then, tell them the
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability, online scheduler tips, line 375
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:375"
- id: B-playbooks-growth-009
  type: rule
  name: >-
    Time slots visible on load
  statement: >-
    Available dates and times are visible as soon as the scheduling page loads, on mobile as well as desktop.
  anchor: >-
    Make available dates and times super obvious as soon as the page loads. You
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability, online scheduler tips, line 379
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:379"
- id: B-playbooks-growth-010
  type: rule
  name: >-
    Eliminate steps in scheduling
  statement: >-
    The scheduling flow contains as few steps as possible and never asks a lead again for information they have already given.
  why: >-
    Technology now removes fields the lead already filled out, and that creates huge improvements in schedule rates.
  anchor: >-
    Eliminate as many steps as possible. And if leads already gave you relevant info
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability, online scheduler tips, line 381
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:381"
- id: B-playbooks-growth-011
  type: rule
  name: >-
    Add friction when appointments are bad
  statement: >-
    When the calendar fills with bad appointments, friction is added before the scheduler - a video to watch, a sales letter, a visible price, a delayed scheduler - rather than removed.
  applies_when: >-
    Only when there are too many bad appointments on the calendar; the default direction is removing friction.
  anchor: >-
    When that happens—it’s okay to add friction.
  source: >-
    playbook-lead-nurture.md, Pillar I: Availability, Author Note: Solution For Too Many Bad Appointments, line 402
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:402"
- id: B-playbooks-growth-012
  type: rule
  name: >-
    Call leads within 5 minutes
  statement: >-
    Every lead is contacted within five minutes of opting in.
  why: >-
    Conversions rise 391% when leads are contacted within the first 60 seconds (Velocify), and the faster you contact leads the fewer times you have to contact them before they buy.
  anchor: >-
    Call leads within 5min of opting in. Seriously, once you get this, you will see an
  source: >-
    playbook-lead-nurture.md, Pillar IV: Volume, 1) Scheduling Appointments, line 849
  confirmations: 3
  authors_caveat: >-
    Extra credit is responding in under 60 seconds; the cost of reaching all leads immediately is carrying excess sales capacity.
  anchor_at: "playbook-lead-nurture.md:849"
- id: B-playbooks-growth-013
  type: rule
  name: >-
    Speed Litmus Test
  statement: >-
    If the team is not hearing that leads are impressed by the speed at least once a day, contact speed is too slow.
  anchor: >-
    If you aren’t getting “man that was fast! You guys are on top of it!” At least
  source: >-
    playbook-lead-nurture.md, Pillar II: Speed, Pro Tip: Speed Litmus Test, line 453
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:453"
- id: B-playbooks-growth-014
  type: rule
  name: >-
    Appointments inside 72 hours
  statement: >-
    Leads cannot schedule more than three days out, and every appointment set is same day, next day or the day after.
  why: >-
    The shorter the delay between scheduling and having the appointment, the higher the show rate; beyond three days you get more schedules but more ghosting, which also kills sales team morale and steals a convenient slot from a buyer.
  anchor: >-
    When you speak to them, aim to set appointments inside 72 hours. So—same
  source: >-
    playbook-lead-nurture.md, Pillar II: Speed, Speed Summary, line 577
  confirmations: 3
  authors_caveat: >-
    You can get away with five days if you have to; keep tabs on show rates and find the sweet spot for your business.
  anchor_at: "playbook-lead-nurture.md:577"
- id: B-playbooks-growth-015
  type: rule
  name: >-
    Pull appointments forward
  statement: >-
    Scheduled appointments are pulled forward, preferably to the same day, and the best available outcome is qualifying and selling on the call you are already on.
  why: >-
    Show rates for same-day appointments are higher than for later ones, and the show rate for the person you are talking to right now is 100%.
  anchor: >-
    now are 100%. So that becomes the objective. When we call to schedule people, we have
  source: >-
    playbook-lead-nurture.md, Pillar II: Speed, 2) Speed To First Appointment, line 488
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:488"
- id: B-playbooks-growth-016
  type: rule
  name: >-
    Second priority for a rep's gaps
  statement: >-
    When there are no fresh leads to contact, the next use of a rep's calendar gaps is calling self-scheduled leads to pull their appointments forward.
  anchor: >-
    no fresh leads to contact and schedule, then calling leads who self-scheduled to pull their
  source: >-
    playbook-lead-nurture.md, Pillar II: Speed, 2) Speed To First Appointment, line 503
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:503"
- id: B-playbooks-growth-017
  type: rule
  name: >-
    Hot handoff to the closer
  statement: >-
    When the setter is not the closer, the lead is connected to the closer in a three-way message during the call, after the closer has been edified.
  anchor: >-
    you connect them in a three-way message with the closer who is going
  source: >-
    playbook-lead-nurture.md, Pillar II: Speed, 2) Speed To First Appointment, line 526
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:526"
- id: B-playbooks-growth-018
  type: rule
  name: >-
    Time stamps are the first place to look
  statement: >-
    When show rates drop, response time stamps on calls and messages are checked first, per sales rep.
  why: >-
    Leads make buying decisions before the sales call, so slow responses between scheduling and the appointment are where leads fall through the cracks.
  anchor: >-
    So, if show rates drop, look here first—especially if they drop for a particular rep.
  source: >-
    playbook-lead-nurture.md, Pillar II: Speed, 3) Speed of Response, line 568
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:568"
- id: B-playbooks-growth-019
  type: rule
  name: >-
    Use The Lead's Preferred Communication Method
  statement: >-
    First contact goes out on several channels at once - call, text, DM, email - and the conversation then continues in whichever channel the lead answered.
  why: >-
    Most communication attempts fail for reasons that have nothing to do with interest, and a lead who opted in asked to be contacted.
  anchor: >-
    You will get higher initial response rates by starting conversations in as
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, 1) Use The Lead's Preferred Communication Method, line 658
  confirmations: 3
  anchor_at: "playbook-lead-nurture.md:658"
- id: B-playbooks-growth-020
  type: rule
  name: >-
    Qualify The Leads
  statement: >-
    Leads answer qualification questions in the opt-in or an application before the sales call, and poor fits are removed from the calendar.
  why: >-
    Qualifying frees time to work the good leads instead of spreading it over leads who will not buy.
  anchor: >-
    Qualify leads: use applications and demographic info so leads talk to the right
  source: >-
    playbook-lead-nurture.md, Lead Nurture Checklist, Pillar III, line 1112
  confirmations: 3
  anchor_at: "playbook-lead-nurture.md:1112"
- id: B-playbooks-growth-021
  type: rule
  name: >-
    Score leads 1-5 or red-yellow-green
  statement: >-
    Leads are scored on a 1-5 or red-yellow-green scale using the demographics and actions taken from your own best customers.
  anchor: >-
    Score  leads  on  a  1–5  or  red-yellow-green  system  based  on  how  qualified
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, 3) Send The Best Leads To The Best Closers, line 696
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:696"
- id: B-playbooks-growth-022
  type: rule
  name: >-
    Send The Best Leads To The Best Closers
  statement: >-
    The highest-scoring leads are routed to the best closers rather than spread evenly across the team.
  anchor: >-
    route your best leads to your best closers.
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, 3) Send The Best Leads To The Best Closers, line 698
  confirmations: 3
  anchor_at: "playbook-lead-nurture.md:698"
- id: B-playbooks-growth-023
  type: rule
  name: >-
    Five minutes of homework before contact
  statement: >-
    Before contacting a good lead, five minutes go into their profile, site and recent activity, and what was found is mentioned upfront and early.
  why: >-
    People are more likely to listen to someone who behaves like someone they know, and research raises response rates.
  anchor: >-
    It takes five minutes of preparation before you
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, 4) Segment Your Messaging, line 707
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:707"
- id: B-playbooks-growth-024
  type: rule
  name: >-
    Segment Your Messaging
  statement: >-
    Each category of lead has its own text and email sequence built around the pains of that category.
  why: >-
    Hubspot improved their email marketing ROI by 7x after segmenting their list.
  anchor: >-
    Make your nurture sequences specific to the pains these people deal
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, 4) Segment Your Messaging, line 723
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:723"
- id: B-playbooks-growth-025
  type: rule
  name: >-
    Get Your Team iPhones For Texting
  statement: >-
    Texts to leads are sent from devices that produce real-human messages rather than from channels that look automated.
  why: >-
    Spam and automated junk arrive as green messages and messages from real humans as blue ones, and blue messages get more responses (2025).
  anchor: >-
    send  blue  messages,  you’ll  get  more  responses.  The  tech  will  change  over
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, Pro Tip: Get Your Team iPhones For Texting, line 732
  confirmations: 1
  authors_caveat: >-
    The tech will change over time; the thing to invest in is whatever plays the role of pseudo-human verification.
  anchor_at: "playbook-lead-nurture.md:732"
- id: B-playbooks-growth-026
  type: rule
  name: >-
    Local Area Code Call Wrapping
  statement: >-
    Outbound calls display an area code local to the lead being called.
  why: >-
    Local area codes have significantly higher pick-up rates than unrecognized or out-of-area codes.
  anchor: >-
    Local area codes have significantly higher pick up rates than unrecognized or
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, Pro Tip: Local Area Code Call Wrapping, line 737
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:737"
- id: B-playbooks-growth-027
  type: rule
  name: >-
    Gift Card push incentive
  statement: >-
    A push incentive is sent before the appointment as a gift the lead keeps whether they show up or not.
  why: >-
    The strategy hinges on reciprocity, and it still works even when people know what you are doing; gifts have no strings.
  anchor: >-
    they get the gift card you send whether they show or not. This is a
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, 5) Incentives, line 751
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:751"
- id: B-playbooks-growth-028
  type: rule
  name: >-
    A/B pull incentive
  statement: >-
    A pull incentive is offered as a choice between two options that both assume the lead will show, where the lead wants the thing, it is obviously connected to the offer, and preparing it cost you something real.
  anchor: >-
    A/B Incentives depend on three things. First, leads should want the thing. Second, it
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, 5) Incentives, line 779
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:779"
- id: B-playbooks-growth-029
  type: rule
  name: >-
    Demonstrate Proof
  statement: >-
    The proof sent to a lead matches that lead's own situation, age, demographics and starting point.
  why: >-
    Proof gets people excited to talk to you about the product, and the closer the match, the better.
  anchor: >-
    Proof: show proof that matches their situation across all stages of follow-up.
  source: >-
    playbook-lead-nurture.md, Lead Nurture Checklist, Pillar III, line 1123
  confirmations: 2
  authors_caveat: >-
    Be compliant with the proof you send, which varies by state and country.
  anchor_at: "playbook-lead-nurture.md:1123"
- id: B-playbooks-growth-030
  type: rule
  name: >-
    Where proof is woven in
  statement: >-
    Proof is sent after they schedule and before they show, between the first and second call, and every 90 days to leads who ghosted.
  why: >-
    Showing ghosted leads the results of people who signed up when they ghosted makes them feel left behind while leaving them the option to make up for lost time.
  anchor: >-
    If they ghost, every 90 days. Show them the results of people who signed up about
  source: >-
    playbook-lead-nurture.md, Pillar III: Personalization, 6) Proof, line 794
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:794"
- id: B-playbooks-growth-031
  type: rule
  name: >-
    Double-dial
  statement: >-
    An unanswered call is dialled again immediately rather than left until the next attempt.
  why: >-
    They gave you permission to contact them, and many phones block the first call from an unknown number and let the second through.
  anchor: >-
    Double-dial.  If  you  call  once  and  get  nothing,  immediately call  again.  First,
  source: >-
    playbook-lead-nurture.md, Pillar IV: Volume, 1) Scheduling Appointments, line 852
  confirmations: 2
  authors_caveat: >-
    Obey the laws of your area.
  anchor_at: "playbook-lead-nurture.md:852"
- id: B-playbooks-growth-032
  type: rule
  name: >-
    Voicemail then immediate text
  statement: >-
    When nobody picks up, a voicemail is left and a text goes out immediately after it.
  anchor: >-
    Send a text immediately after you leave the voicemail.
  source: >-
    playbook-lead-nurture.md, Pillar IV: Volume, 1) Scheduling Appointments, line 861
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:861"
- id: B-playbooks-growth-033
  type: rule
  name: >-
    Front-loaded reach-out cadence
  statement: >-
    A new lead gets double-dial-plus-text three times on day one, twice a day for the next two days, and once a day for the four days after that.
  why: >-
    The more days that pass, the less likely the lead will schedule, so the reach-outs are front-loaded, with a few hours left between attempts.
  anchor: >-
    Call two times for the next two days. Once earlier in the day and once later in the
  source: >-
    playbook-lead-nurture.md, Pillar IV: Volume, 1) Scheduling Appointments, lines 862-868
  confirmations: 2
  authors_caveat: >-
    Steps 6 and 7 stay flexible - more days or fewer; as always, follow the laws in your area.
  anchor_at: "playbook-lead-nurture.md:864"
- id: B-playbooks-growth-034
  type: rule
  name: >-
    Seven or more reach-outs before giving up
  statement: >-
    A lead is contacted at least seven times in multiple ways before being given up on.
  why: >-
    Nearly half of salespeople stop after the first attempt and the average is 1.3 attempts, while most communication attempts fail for reasons unrelated to interest.
  anchor: >-
    You reach out seven or more times in multiple ways. You send automated reminders
  source: >-
    playbook-lead-nurture.md, Pillar IV: Volume, Volume Summary, line 926
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:926"
- id: B-playbooks-growth-035
  type: rule
  name: >-
    Transition to long-term nurture after week one
  statement: >-
    After the first week of reach-outs the lead moves into long-term nurture of free value with soft calls to action, and re-enters the cadence at the top once they re-engage.
  anchor: >-
    After the first week, I transition to long-term nurture. I cover this in other places.
  source: >-
    playbook-lead-nurture.md, Pillar IV: Volume, 1) Scheduling Appointments, line 869
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:869"
- id: B-playbooks-growth-036
  type: rule
  name: >-
    Automated reminders are labelled as automated
  statement: >-
    Automated reminders go out after scheduling and the lead is told that they are automated.
  why: >-
    People do not mind reminders; they mind being lied to.
  anchor: >-
    But  make  it  clear  they  are  automated.  People  don’t  mind
  source: >-
    playbook-lead-nurture.md, Pillar IV: Volume, 2) Reminding Them To Show, line 887
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:887"
- id: B-playbooks-growth-037
  type: rule
  name: >-
    Reminder cadence 24, 12 and 3 hours out
  statement: >-
    After scheduling, an immediate confirmation states the time, date, the number you will call from and who they are meeting, followed by reminders 24 hours, 12 hours and 3 hours before the appointment.
  anchor: >-
    24 hours, 12 hours, and 3 hours out from their appointment. You send manual reminders
  source: >-
    playbook-lead-nurture.md, Pillar IV: Volume, Volume Summary, line 927
  confirmations: 3
  anchor_at: "playbook-lead-nurture.md:927"
- id: B-playbooks-growth-038
  type: rule
  name: >-
    Manual reminders from a real phone
  statement: >-
    Manual reminders are sent from a real cell phone the night before, the morning of, and 60 minutes before the appointment.
  anchor: >-
    Manual reminders from a real phone: night before, morning of, 60 min prior.
  source: >-
    playbook-lead-nurture.md, Lead Nurture Checklist, Pillar IV, line 1132
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:1132"
- id: B-playbooks-growth-039
  type: rule
  name: >-
    Reminders carry the calling area code
  statement: >-
    Every reminder states the area code the call will come from.
  why: >-
    It doubles pick-up rates (2025).
  anchor: >-
    Add the area code you’ll be calling from. You’ll 2x your pick-up rates.
  source: >-
    playbook-lead-nurture.md, Pillar IV: Volume, Automated Reminder Tips, line 898
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:898"
- id: B-playbooks-growth-040
  type: rule
  name: >-
    Reminders in the lead's time zone
  statement: >-
    Reminders are timed to the lead's local time zone, not the company's.
  anchor: >-
    use the lead’s local time zone. Thank me later.
  source: >-
    playbook-lead-nurture.md, Pillar IV: Volume, Automated Reminder Tips, line 899
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:899"
- id: B-playbooks-growth-041
  type: rule
  name: >-
    Several short messages, not one block
  statement: >-
    A message to a lead is sent as several short messages rather than one big block of text.
  why: >-
    Short consecutive messages read as more natural.
  anchor: >-
    Send  multiple  short  messages  rather  than  a  big  blocky  message.  It’s  more
  source: >-
    playbook-lead-nurture.md, Lead Nurture Checklist, Pillar IV, line 1133
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:1133"
- id: B-playbooks-growth-042
  type: rule
  name: >-
    Keep nurturing after they respond
  statement: >-
    Once a lead responds, the nurture and the fast responses continue rather than stopping at the reply.
  anchor: >-
    Once they respond—keep nurturing! keep responding quickly.
  source: >-
    playbook-lead-nurture.md, Pillar IV: Volume, 2) Reminding Them To Show, line 906
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:906"
- id: B-playbooks-growth-043
  type: rule
  name: >-
    BAMFAM: Book-A-Meeting-From-A-Meeting
  statement: >-
    No call ends without the next appointment booked on the calendar during that call.
  why: >-
    People are more likely to show up to appointments you schedule, and the highest chance of scheduling one is with the person in real time; after limbo they put you in their rearview mirror.
  applies_when: >-
    Every call that does not end in a close, including the gap between a first and second call.
  anchor: >-
    If you can’t schedule an appointment with them right then and
  source: >-
    playbook-lead-nurture.md, Pillar IV: Volume, 3) Book Their Next Appointment At The Current Appointment, line 915
  confirmations: 3
  anchor_at: "playbook-lead-nurture.md:915"
- id: B-playbooks-growth-044
  type: rule
  name: >-
    Commission bump for show rate
  statement: >-
    Sales pay includes a commission bump tied to show-up rate, in the neighbourhood of 5-30% of what the salesperson makes on a sale.
  why: >-
    Culture is the rules that govern good and bad behaviour, and the behaviours that get leads worked have to be paid for as well as praised (2025).
  anchor: >-
    it’s in the neighborhood of 5–30% of what a
  source: >-
    playbook-lead-nurture.md, Execution, Tactics, line 1041
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:1041"
- id: B-playbooks-growth-045
  type: rule
  name: >-
    Track and rank three metrics per rep
  statement: >-
    Show rate, close rate and lead-to-close ratio are tracked and ranked for every sales rep, not close rate alone.
  why: >-
    The nurture list measures work ethic and the closing list measures skill; the only thing that actually matters is the conversion rate on the leads you already have.
  anchor: >-
    Track and rank: show rate, close rates, and lead-to-close ratio by sales rep.
  source: >-
    playbook-lead-nurture.md, Lead Nurture Checklist, Execution, line 1140
  confirmations: 2
  anchor_at: "playbook-lead-nurture.md:1140"
- id: B-playbooks-growth-046
  type: rule
  name: >-
    New salespeople start as setters
  statement: >-
    New salespeople are started on setting appointments, and the ones who set a lot of leads are the ones moved to closing.
  why: >-
    It is the same skill set at lower stakes, so setting is a low-risk environment to test a new hire.
  anchor: >-
    the best closers are typically the best setters.
  source: >-
    playbook-lead-nurture.md, Execution, Tactics, line 1056
  confirmations: 1
  anchor_at: "playbook-lead-nurture.md:1056"
- id: B-playbooks-growth-047
  type: rule
  name: >-
    Track attendance
  statement: >-
    Every customer's attendance or usage is tracked, with three or more sessions a week as the sticking level and a drop to two sessions as the trigger to reach out.
  why: >-
    Attendance falls step by step before a cancellation, and talking to the member right when it drops to two sessions rescues them.
  applies_when: >-
    Gym memberships, where attendance is the observable behaviour; the general form is the activation point of your own business.
  anchor: >-
    Track  attendance:  If  a  member  went  to  the  gym  three  times  per  week  or  more,  they
  source: >-
    playbook-retention.md, The 5 Horsemen of Retention, line 110
  confirmations: 1
  anchor_at: "playbook-retention.md:110"
- id: B-playbooks-growth-048
  type: rule
  name: >-
    Reach out 2x per week
  statement: >-
    Every customer is contacted twice a week to praise their participation and progress and to solve the small problems they have.
  anchor: >-
    Reach out 2x per week: Praising customers about their participation and progress goes
  source: >-
    playbook-retention.md, The 5 Horsemen of Retention, line 125
  confirmations: 1
  anchor_at: "playbook-retention.md:125"
- id: B-playbooks-growth-049
  type: rule
  name: >-
    Handwritten cards
  statement: >-
    Handwritten cards are sent when a customer signs up and at the three, six and twelve month milestones where referrals are asked for.
  why: >-
    There is never a bad time to send a handwritten card so long as you make it yourself.
  anchor: >-
    Handwritten cards: Send hand-written cards when they sign up, when you ask for re-
  source: >-
    playbook-retention.md, The 5 Horsemen of Retention, line 127
  confirmations: 1
  anchor_at: "playbook-retention.md:127"
- id: B-playbooks-growth-050
  type: rule
  name: >-
    Member events on an internal calendar
  statement: >-
    Member events are held on an internal calendar every 21, 42 or 63 days, regular to you and random to them, with handwritten invites.
  why: >-
    Events reduce churn and generate referrals at the same time.
  anchor: >-
    Member events: Hold regular events on an internal calendar. Keep them regular to you
  source: >-
    playbook-retention.md, The 5 Horsemen of Retention, line 131
  confirmations: 1
  anchor_at: "playbook-retention.md:131"
- id: B-playbooks-growth-051
  type: rule
  name: >-
    Exit interviews
  statement: >-
    New customers are told at onboarding that an exit interview is required, and the cancellation notice is the signal to set that interview up before they leave.
  why: >-
    Done right this saves about half of phone and email cancellations, which cuts churn by roughly 25% assuming half show - a 33% increase in LTV.
  anchor: >-
    set the expectation you’ll require an exit interview when you onboard new customers.
  source: >-
    playbook-retention.md, The 5 Horsemen of Retention, line 136
  confirmations: 3
  anchor_at: "playbook-retention.md:136"
- id: B-playbooks-growth-052
  type: rule
  name: >-
    Expect churn to rise in month one
  statement: >-
    Churn rising in the first month after the retention work starts is expected and is not a reason to stop doing it.
  why: >-
    Shaking the three flushes out people who would have cancelled anyway and people who stopped consuming long ago while automated billing kept running.
  anchor: >-
    We would tell gym owners to expect churn to increase at first. But as long as they do
  source: >-
    playbook-retention.md, The 5 Horsemen Of Retention: Results, line 163
  confirmations: 2
  anchor_at: "playbook-retention.md:163"
- id: B-playbooks-growth-053
  type: rule
  name: >-
    Keep value above price
  statement: >-
    The value the customer gets stays greater than the price they pay, and the gap is opened by adding value rather than by lowering price.
  anchor: >-
    the value customers get greater than the price they pay, customers will stick.
  source: >-
    playbook-retention.md, Price, Value, And Churn, line 198
  confirmations: 1
  anchor_at: "playbook-retention.md:198"
- id: B-playbooks-growth-054
  type: rule
  name: >-
    The best price is the one with the most sales at the highest LTV
  statement: >-
    The price is chosen as the one producing the most sales at the highest LTV, and is found by testing prices rather than by reasoning about them.
  why: >-
    Price moves both conversion rate and churn rate, and both suffer as price goes up but not always proportionally; across Skool the higher the price the higher the churn (2025).
  anchor: >-
    The most sales at the highest LTV is the best price. This doesn’t necessarily mean lowest
  source: >-
    playbook-retention.md, Price, Value, And Churn, Relationship Between Price and Churn, line 229
  confirmations: 2
  anchor_at: "playbook-retention.md:229"
- id: B-playbooks-growth-055
  type: rule
  name: >-
    Double the price if you lose less than 20% of deals
  statement: >-
    If doubling the price costs fewer than 20% of deals with everything else unchanged, the price is doubled.
  anchor: >-
    20% fewer deals, with all else staying the same...you should do it! And that’s exactly what
  source: >-
    playbook-retention.md, Price, Value, And Churn, Relationship Between Price and Churn, line 245
  confirmations: 1
  anchor_at: "playbook-retention.md:245"
- id: B-playbooks-growth-056
  type: rule
  name: >-
    Match the pricing model to the business model
  statement: >-
    Something with one-time value is not sold as a recurring subscription; the pricing model matches what the business actually delivers over time.
  why: >-
    Many businesses misprice by trying to create something recurring out of something that has one-time value.
  anchor: >-
    You want to match your business model with
  source: >-
    playbook-retention.md, Price, Value, And Churn, line 250
  confirmations: 1
  anchor_at: "playbook-retention.md:250"
- id: B-playbooks-growth-057
  type: rule
  name: >-
    Decide on the core 2-3 things
  statement: >-
    The offer is cut to two or three core deliverables made really good instead of a growing list of additions.
  why: >-
    Overwhelm is the number one reason for churn: the newsletter business had its lowest churn on one call and one newsletter a month, and everything added after that increased churn.
  anchor: >-
    Sometimes less is more. There is wisdom in deletion. Decide on the core 2-3 things you deliv-
  source: >-
    playbook-retention.md, Price, Value, And Churn, Provide On-Going Value, line 267
  confirmations: 2
  anchor_at: "playbook-retention.md:267"
- id: B-playbooks-growth-058
  type: rule
  name: >-
    Make them consume the value
  statement: >-
    The product is built so customers actually consume what they bought, with effort and sacrifice reduced as far as possible.
  why: >-
    Most people never finish the video, the course or the goal, so retention comes down to consumption rather than to how much value you pile on.
  anchor: >-
    Retention  comes  down  making  sure  they  CONSUME  the  value, not  to  overwhelm
  source: >-
    playbook-retention.md, Price, Value, And Churn, Provide On-Going Value, line 271
  confirmations: 2
  anchor_at: "playbook-retention.md:271"
- id: B-playbooks-growth-059
  type: rule
  name: >-
    Contact more when consumption stops
  statement: >-
    When a customer stops consuming the product, contact goes up rather than down.
  anchor: >-
    When  customers  stop  consuming,  you  want  to
  source: >-
    playbook-retention.md, Price, Value, And Churn, Provide On-Going Value, line 275
  confirmations: 2
  anchor_at: "playbook-retention.md:275"
- id: B-playbooks-growth-060
  type: rule
  name: >-
    Retention budget of one fifth of CAC
  statement: >-
    A per-customer retention budget is set at one fifth of what it costs to acquire a customer.
  why: >-
    Acquiring a new customer costs five to twenty-five times more than retaining one, so money spent on keeping customers returns far more (2025).
  anchor: >-
    1/5th of CAC and you’d be amazed how far that goes.
  source: >-
    playbook-retention.md, Why Is Reducing Churn So Important?, line 307
  confirmations: 1
  anchor_at: "playbook-retention.md:307"
- id: B-playbooks-growth-061
  type: rule
  name: >-
    Activation point template
  statement: >-
    The business states its activation point in the form: every customer that does X or gets Y stays longer than customers who do not.
  why: >-
    Activation points are the leading indicators of retention, and segmenting customers by engagement makes every other retention tool more effective.
  anchor: >-
    ery customer that does (X thing) or gets (Y result) stays for longer than customers who don’t.
  source: >-
    playbook-retention.md, Churn Checklist #1: Figure Out Your Activation Points, line 361
  confirmations: 2
  anchor_at: "playbook-retention.md:361"
- id: B-playbooks-growth-062
  type: rule
  name: >-
    Find the activation point in the top 20% of long-staying customers
  statement: >-
    The activation-point analysis takes customers who stayed three months or longer and works from the top 20% of them by spend.
  anchor: >-
    Order that list by who spent the most money .  Take the top  20% of customers.
  source: >-
    playbook-retention.md, Churn Checklist #1: Figure Out Your Activation Points, line 379
  confirmations: 2
  authors_caveat: >-
    Three months is a convention, not a magic number - you can use whatever time window you want.
  anchor_at: "playbook-retention.md:379"
- id: B-playbooks-growth-063
  type: rule
  name: >-
    Narrow to five activation candidates
  statement: >-
    The common factors found among the best customers are narrowed to five candidates and worked down the list one at a time.
  anchor: >-
    Narrow it down to 5 factors and start working your way down the list. Some
  source: >-
    playbook-retention.md, Churn Checklist #1: Figure Out Your Activation Points, line 393
  confirmations: 1
  anchor_at: "playbook-retention.md:393"
- id: B-playbooks-growth-064
  type: rule
  name: >-
    All Roads Lead To Activation
  statement: >-
    Finding the activation point is worked on before the other churn-reduction activities.
  why: >-
    Activation points have the greatest effect on churn of anything on the checklist.
  anchor: >-
    Make finding activation points your top priority. They have the greatest effect
  source: >-
    playbook-retention.md, Churn Checklist #1, Author Note: All Roads Lead To Activation, line 396
  confirmations: 1
  anchor_at: "playbook-retention.md:396"
- id: B-playbooks-growth-065
  type: rule
  name: >-
    Update messaging and onboarding, retest every 6-12 months
  statement: >-
    Messaging is updated to attract the customers who stay longest, onboarding is updated to drive to the activation point, and both are retested every 6-12 months.
  why: >-
    The Gym Launch competitor sold the same number of people at the same CAC but earned 70x less profit because he advertised to everyone in fitness rather than to the people most likely to stay.
  anchor: >-
    Find  who  your  best  customers  are.  Find  your  activation  point.  Update
  source: >-
    playbook-retention.md, Churn Checklist #1: Figure Out Your Activation Points, Action Step, lines 427-429
  confirmations: 2
  anchor_at: "playbook-retention.md:427"
- id: B-playbooks-growth-066
  type: rule
  name: >-
    Onboarding teaches the activation point
  statement: >-
    Onboarding exists to teach customers how to hit the activation points, whatever form it takes - booklet, video, call or event.
  anchor: >-
    Here, I mean “Teach customers how to
  source: >-
    playbook-retention.md, Churn Checklist #2: Onboard Your Customers, line 440
  confirmations: 2
  anchor_at: "playbook-retention.md:440"
- id: B-playbooks-growth-067
  type: rule
  name: >-
    Some onboarding beats none
  statement: >-
    Every customer gets some onboarding, and the more custom, personal and live it is, the better.
  why: >-
    Custom outperforms generic, personal outperforms group, live outperforms recorded, and carrots outperform sticks; a portfolio company moving from group to 1-on-1 onboarding got a 25% boost in ascensions.
  anchor: >-
    Last, and most important, some beats none.
  source: >-
    playbook-retention.md, Churn Checklist #2: Onboard Your Customers, line 447
  confirmations: 3
  anchor_at: "playbook-retention.md:447"
- id: B-playbooks-growth-068
  type: rule
  name: >-
    Resell the value during onboarding
  statement: >-
    Onboarding resells the value of the purchase, framed inside the customer's own goals.
  anchor: >-
    Resell the value of the purchase. Important! Frame it within the context of their
  source: >-
    playbook-retention.md, Churn Checklist #2: Onboard Your Customers, line 464
  confirmations: 2
  anchor_at: "playbook-retention.md:464"
- id: B-playbooks-growth-069
  type: rule
  name: >-
    Customers always know when you speak next
  statement: >-
    A customer always knows when the next conversation with you will happen.
  why: >-
    Onboarding is used to establish long-term communication rather than as a one-off welcome.
  anchor: >-
    Customers  should  always  know  when  you’ll  speak  to  them
  source: >-
    playbook-retention.md, Churn Checklist #2: Onboard Your Customers, line 475
  confirmations: 2
  anchor_at: "playbook-retention.md:475"
- id: B-playbooks-growth-070
  type: rule
  name: >-
    Onboard sales prospects too
  statement: >-
    The same onboarding treatment is given to sales prospects, not only to paying customers.
  why: >-
    It increases the close rate.
  anchor: >-
    Do this for sales prospects as well. It will increase your close rate.
  source: >-
    playbook-retention.md, Churn Checklist #2: Onboard Your Customers, line 477
  confirmations: 1
  anchor_at: "playbook-retention.md:477"
- id: B-playbooks-growth-071
  type: rule
  name: >-
    Incentivize Customer Activation
  statement: >-
    Doing the activation behaviours earns the customer something they value - unlocked courses, calls, event tickets, higher-tier access, badges or status.
  why: >-
    A vast majority of cancellations come from the bottom two tiers of engagement, so the more a customer uses the product the longer they stay.
  anchor: >-
    Give  your  customers  relevant  and  valuable  incentives  to  become  perfect
  source: >-
    playbook-retention.md, Churn Checklist #3: Incentivize Customer Activation, Action Step, line 522
  confirmations: 2
  anchor_at: "playbook-retention.md:522"
- id: B-playbooks-growth-072
  type: rule
  name: >-
    Put unlocks just past the major churn points
  statement: >-
    Bonuses and unlockables are placed just after the points in the lifecycle where most customers leave.
  why: >-
    If most customers leave after the third month, something cool unlocking in month four retains the ones on the edge.
  anchor: >-
    By  putting  some  incentives  just  after  major  churn  points,  you  can  retain
  source: >-
    playbook-retention.md, Churn Checklist #3: Incentivize Customer Activation, line 518
  confirmations: 2
  anchor_at: "playbook-retention.md:518"
- id: B-playbooks-growth-073
  type: rule
  name: >-
    Usage Churn
  statement: >-
    A still-paying customer who has stopped using the product is treated as churning and is intercepted at the moment usage stops.
  why: >-
    Usage churn is a leading indicator: a customer on an annual contract who stops using the service at six months is likely to cancel at renewal.
  anchor: >-
    But if you intercept them right when they stop using it and get them to
  source: >-
    playbook-retention.md, Churn Checklist #3, Pro Tip: Usage Churn, line 530
  confirmations: 2
  anchor_at: "playbook-retention.md:530"
- id: B-playbooks-growth-074
  type: rule
  name: >-
    Community Linking
  statement: >-
    Retention work connects customers to each other rather than only to you.
  why: >-
    It is easy to quit a membership and hard to leave a relationship, and multiple deeper connections scale better than one tie to the group.
  anchor: >-
    Connect members to each other, not you. It’s more scalable to facilitate multiple, deeper
  source: >-
    playbook-retention.md, Churn Checklist #4: Community Linking, line 537
  confirmations: 2
  anchor_at: "playbook-retention.md:537"
- id: B-playbooks-growth-075
  type: rule
  name: >-
    How community linking is executed
  statement: >-
    Community linking is executed as group events, manual introductions between members, a community podcast, and public elevation of micro-celebrities in the group.
  anchor: >-
    Host group events. Manually connect people. Start a community podcast.
  source: >-
    playbook-retention.md, Churn Checklist #4: Community Linking, Action Step, line 553
  confirmations: 2
  anchor_at: "playbook-retention.md:553"
- id: B-playbooks-growth-076
  type: rule
  name: >-
    Delete bad posts and say why
  statement: >-
    A bad contribution is deleted and the person is told why it was bad and what good looks like.
  anchor: >-
    Delete bad posts and tell people why they sucked and tell them what good looks
  source: >-
    playbook-retention.md, Churn Checklist #5: Correct or Fire Bad Customers, line 561
  confirmations: 2
  anchor_at: "playbook-retention.md:561"
- id: B-playbooks-growth-077
  type: rule
  name: >-
    Three strikes
  statement: >-
    A customer who keeps behaving badly is removed after three strikes.
  why: >-
    Bad customers make it bad for everyone else.
  anchor: >-
    Give 3 strikes on bad posters.
  source: >-
    playbook-retention.md, Churn Checklist #5: Correct or Fire Bad Customers, line 563
  confirmations: 3
  anchor_at: "playbook-retention.md:563"
- id: B-playbooks-growth-078
  type: rule
  name: >-
    Pin the best posts daily
  statement: >-
    The best one or two new contributions are pinned every day.
  why: >-
    It elevates those people, gives fresh value to everyone else, helps them level up and signals what content you reward.
  anchor: >-
    Pin the best 1-2 new posts daily.
  source: >-
    playbook-retention.md, Churn Checklist #5: Correct or Fire Bad Customers, line 564
  confirmations: 1
  anchor_at: "playbook-retention.md:564"
- id: B-playbooks-growth-079
  type: rule
  name: >-
    Four topic categories
  statement: >-
    The community has topic categories for what you want people to post and includes wins, fun, discovered and meetups.
  why: >-
    Wins give you testimonials, fun keeps it light, discovered makes people share findings with proof, and meetups give people a place to connect.
  anchor: >-
    Make topic categories for what you want people to post. But include these four:
  source: >-
    playbook-retention.md, Churn Checklist #5: Correct or Fire Bad Customers, line 568
  confirmations: 1
  anchor_at: "playbook-retention.md:568"
- id: B-playbooks-growth-080
  type: rule
  name: >-
    Add Annual Payment Options
  statement: >-
    An annual payment option is available so the customers who want to stay longer can pay to stay longer.
  why: >-
    Some customers take it and stay a full year, which extends the average stay per customer; typically 10-20% take it when it is priced at buy 10 months get 2 free (2025).
  anchor: >-
    Customers who pay for longer stays...stay longer. So, if customers want to stay longer,
  source: >-
    playbook-retention.md, Churn Checklist #6: Add Annual Payment Options, line 583
  confirmations: 2
  anchor_at: "playbook-retention.md:583"
- id: B-playbooks-growth-081
  type: rule
  name: >-
    Price the annual option above the average lifetime spend
  statement: >-
    The annual option is priced above what the average customer currently spends over their stay, and at buy-10-get-2-free when the average stay is longer than 12 months.
  why: >-
    To increase annual take-up without removing the monthly option, offer a steeper annual discount.
  anchor: >-
    Price it above your avg # of months if less than
  source: >-
    playbook-retention.md, Churn Checklist #6: Add Annual Payment Options, line 595
  confirmations: 1
  anchor_at: "playbook-retention.md:595"
- id: B-playbooks-growth-082
  type: rule
  name: >-
    Mandatory annual only where you sell by phone or webinar
  statement: >-
    Annual billing is made the only option only where the sale happens by phone or webinar; in website checkout the annual option sits alongside the monthly one.
  why: >-
    Making it mandatory decreases sales and decreases churn, and sometimes that makes more money overall.
  anchor: >-
    You can make the annual option mandatory or simply make it an option. If you make
  source: >-
    playbook-retention.md, Churn Checklist #6: Add Annual Payment Options, line 587
  confirmations: 1
  anchor_at: "playbook-retention.md:587"
- id: B-playbooks-growth-083
  type: rule
  name: >-
    Price the upfront and the recurring by their own value
  statement: >-
    A big upfront fee is priced against a genuine one-time value such as education or setup, and the recurring fee against the ongoing consumable value.
  why: >-
    A big head, long tail structure stacks the recurring base and can lift LTV from $6,800 to $12,800 because each part is appropriately priced (2025).
  anchor: >-
    Make the big upfront thing something that has big one time value (education or
  source: >-
    playbook-retention.md, Churn Checklist #6: Add Annual Payment Options, line 601
  confirmations: 1
  anchor_at: "playbook-retention.md:601"
- id: B-playbooks-growth-084
  type: rule
  name: >-
    Sell the recurring fee with the one-time fee
  statement: >-
    When a big one-time fee is paired with a small recurring fee, both are sold in the same transaction rather than as a second sale.
  why: >-
    Otherwise you lose the price anchor between the big first purchase and the small recurring one, and that anchor is what drives the retention.
  anchor: >-
    Make sure to include the recurring fee WITH the 1-time up front fee and not
  source: >-
    playbook-retention.md, Churn Checklist #6: Add Annual Payment Options, line 618
  confirmations: 1
  anchor_at: "playbook-retention.md:618"
- id: B-playbooks-growth-085
  type: rule
  name: >-
    Founder rates
  statement: >-
    A founder rate of about 50% off is offered to convert more buyers and hold them longer.
  anchor: >-
    A founder rate is a discount for the owner of a business. A 50% decrease is a great
  source: >-
    playbook-retention.md, Churn Checklist #6: Add Annual Payment Options, line 647
  confirmations: 1
  authors_caveat: >-
    Only provided the gross margins are still there.
  anchor_at: "playbook-retention.md:647"
- id: B-playbooks-growth-086
  type: rule
  name: >-
    Cancellation calls are required and taken
  statement: >-
    New customers are told that cancelling requires a call, and cancelling customers are got on the phone before they leave.
  why: >-
    You can usually save half of the people who get on a cancellation call, and the chances of saving them on a call are higher than by email or text; the other half give you feedback on how to improve.
  anchor: >-
    Tell  new  customers  you  do  cancellation  calls.  Get  the  customers  on  the
  source: >-
    playbook-retention.md, Churn Checklist #7: Exit Interviews or Cancellation Videos, Action Step, line 690
  confirmations: 3
  anchor_at: "playbook-retention.md:690"
- id: B-playbooks-growth-087
  type: rule
  name: >-
    Save with a redo or with an upsell
  statement: >-
    A save on a cancellation call is offered either as a redo or as an upsell into the higher program their payment is credited toward.
  why: >-
    They still want the result and do not want to leave; find the expectation that was unmet and see if you can meet it.
  anchor: >-
    Save with a redo .“Let me give it another shot and I’ll make it right.”
  source: >-
    playbook-retention.md, Churn Checklist #7: Exit Interviews or Cancellation Videos, line 660
  confirmations: 1
  anchor_at: "playbook-retention.md:660"
- id: B-playbooks-growth-088
  type: rule
  name: >-
    Let them vent and get more upset than they are
  statement: >-
    On a cancellation call the customer is let vent, you get more upset than they are, and you end with what would have to happen for them to be happy.
  why: >-
    Only one person can be in the angry boat at a time, and they want to feel validated rather than to fight; their answer becomes a clear roadmap of what needs to happen.
  anchor: >-
    Let them vent. Get more upset than they are – only one person can be
  source: >-
    playbook-retention.md, Churn Checklist #7: Exit Interviews or Cancellation Videos, line 670
  confirmations: 1
  anchor_at: "playbook-retention.md:670"
- id: B-playbooks-growth-089
  type: rule
  name: >-
    Tell them what they lose
  statement: >-
    The cancelling customer is told exactly what they will lose - custom URLs, posts, access, founder pricing, the work they have put in.
  why: >-
    Software companies are experts at this: losing data or work makes cancelling less likely.
  anchor: >-
    Tell them what they’re gonna lose that they spent time on or gave them status: custom
  source: >-
    playbook-retention.md, Churn Checklist #7: Exit Interviews or Cancellation Videos, line 677
  confirmations: 2
  anchor_at: "playbook-retention.md:677"
- id: B-playbooks-growth-090
  type: rule
  name: >-
    Cancellation video where a call does not pay
  statement: >-
    Where a cancellation call cannot pay for itself, a cancellation video resells them on why they started and reminds them what they risk losing.
  applies_when: >-
    High volume, low price businesses where getting on the phone with churning customers does not make sense financially.
  anchor: >-
    you can cut churn by simply adding a cancellation
  source: >-
    playbook-retention.md, Churn Checklist #7: Exit Interviews or Cancellation Videos, line 687
  confirmations: 1
  anchor_at: "playbook-retention.md:687"
- id: B-playbooks-growth-091
  type: rule
  name: >-
    Survey twice a year with the keep/remove questions
  statement: >-
    Customers are surveyed twice a year with the full list of what you provide, asking which single item they would keep and which they would least mind losing.
  why: >-
    It identifies the core 2-3 things your product actually does; one portfolio company found its customers loved its events and made events one of its largest product lines.
  anchor: >-
    This helps you identify the core 2-3 things your product or service does. Ask them, “If I
  source: >-
    playbook-retention.md, Churn Checklist #8: Survey Customers Regularly, line 693
  confirmations: 2
  anchor_at: "playbook-retention.md:693"
- id: B-playbooks-growth-092
  type: rule
  name: >-
    ACA reach-out every two to three weeks
  statement: >-
    Between surveys, each customer is contacted one on one every two to three weeks, following Acknowledge - Compliment - Ask.
  anchor: >-
    to customers 1 on 1 every two to three weeks retained more people than never speaking
  source: >-
    playbook-retention.md, Churn Checklist #8: Survey Customers Regularly, line 701
  confirmations: 3
  authors_caveat: >-
    Only if the price point allows it, and counterintuitively the wealthier the customers, the less handholding they typically want.
  anchor_at: "playbook-retention.md:701"
- id: B-playbooks-growth-093
  type: rule
  name: >-
    Activation is the first milestone
  statement: >-
    Activation is the first milestone of the customer journey; testimonial, referral and ascension can follow in whatever order suits the customer and the business model.
  why: >-
    All four are more likely to happen if you plan for them than if you do not.
  anchor: >-
    besides activation, 2-3-4 may all happen in different orders depending on the cus-
  source: >-
    playbook-retention.md, Churn Checklist #9: Make a Customer Journey, line 721
  confirmations: 2
  anchor_at: "playbook-retention.md:721"
- id: B-playbooks-growth-094
  type: rule
  name: >-
    Ask them to buy again
  statement: >-
    Existing customers are asked to buy the next thing rather than left to buy it from someone else.
  why: >-
    Customers get an itch to buy more over time and will buy from you or the guy down the street, and someone who just bought something else from you is the least likely to churn.
  anchor: >-
    bought another thing from you, they’re the least likely to churn. So ask them to buy!
  source: >-
    playbook-retention.md, Churn Checklist #9: Make a Customer Journey, line 720
  confirmations: 2
  anchor_at: "playbook-retention.md:720"
- id: B-playbooks-growth-095
  type: rule
  name: >-
    Run a Fast Cash Play once a quarter
  statement: >-
    A Fast Cash Play is run once a quarter, four times a year, not weekly and not annually.
  why: >-
    A quarterly cadence cleans the pipeline of on-the-fence leads, raises the value of every customer, keeps something new going on, and leaves time to deliver and reset between plays.
  anchor: >-
    I’ve found that once a quarter is the sweet spot for a few reasons:
  source: >-
    playbook-fast-cash.md, 5 Reasons To Run Fast Cash Offers Every 90 Days, line 462
  confirmations: 2
  authors_caveat: >-
    If you need longer than twelve weeks to cool off between promotions, run it twice a year instead.
  anchor_at: "playbook-fast-cash.md:462"
- id: B-playbooks-growth-096
  type: rule
  name: >-
    Advertise only to warm audiences
  statement: >-
    The Fast Cash offer goes to existing customers, previous customers and the engaged leads list, and to no one else.
  why: >-
    These groups are the most likely to buy and the cheapest to reach, often free, which shortens both the letting-them-know and the getting-them-to-buy process.
  anchor: >-
    You advertise your Fast Cash offer to your existing customers, pre-
  source: >-
    playbook-fast-cash.md, The Fast Cash Playbook, Description: Who to advertise to, line 229
  confirmations: 3
  anchor_at: "playbook-fast-cash.md:229"
- id: B-playbooks-growth-097
  type: rule
  name: >-
    Exclude Cooled-Off Leads
  statement: >-
    Leads who have had nothing from you for six months or more are excluded from the play and warmed up for the next one instead.
  anchor: >-
    list has neglected leads - aka - you haven’t sent them anything for six months or more, con-
  source: >-
    playbook-fast-cash.md, Important Points: Exclude Cooled-Off Leads, line 428
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:428"
- id: B-playbooks-growth-098
  type: rule
  name: >-
    Sell the unscalable
  statement: >-
    The Fast Cash offer is built from the most valuable unscalable things you can do - attention, personalization, convenience, status, duration, speed, experience, access, network, secrets - at a premium price.
  anchor: >-
    With Fast Cash offers, you want to think scarcity, urgency, exclusivity,
  source: >-
    playbook-fast-cash.md, The Fast Cash Playbook, Description: What to sell them, line 236
  confirmations: 2
  anchor_at: "playbook-fast-cash.md:236"
- id: B-playbooks-growth-099
  type: rule
  name: >-
    Keep the unscalable parts in at a high price
  statement: >-
    At a very high price the unscalable components stay in the offer rather than being cut for being unscalable.
  why: >-
    Those unscalable solutions are the things that justify the crazy high price tag.
  anchor: >-
    if you sell at a crazy high price, then you want to include the stuff before
  source: >-
    playbook-fast-cash.md, Ultra-Premium Examples, line 378
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:378"
- id: B-playbooks-growth-100
  type: rule
  name: >-
    One to three core components and three bonuses
  statement: >-
    The offer has one to three core components plus three bonuses held back to be layered in one at a time.
  why: >-
    Each new bonus gives new information that expands the price-to-value discrepancy and pushes more people over the edge.
  anchor: >-
    You will want to have one to three core components of your offer, and three bonuses.
  source: >-
    playbook-fast-cash.md, The Fast Cash Playbook, Description: What to sell them, line 258
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:258"
- id: B-playbooks-growth-101
  type: rule
  name: >-
    Every bonus goes to every buyer
  statement: >-
    All bonuses are given to all buyers no matter when in the sequence they bought.
  why: >-
    For someone who bought early, the later bonuses simply confirm they made the right choice.
  anchor: >-
    You’ll make all the bonuses available to all
  source: >-
    playbook-fast-cash.md, The Fast Cash Playbook, Description: What to sell them, line 261
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:261"
- id: B-playbooks-growth-102
  type: rule
  name: >-
    Cap the spots at five to ten percent of customers
  statement: >-
    The number of spots is capped at a number certain to sell out, about five to ten percent of your customers.
  why: >-
    Selling out fast makes the next Fast Cash offer more compelling, so it sells out even faster.
  anchor: >-
    At first, I suggest capping it to a number where you will absolutely sell out– maybe five to ten
  source: >-
    playbook-fast-cash.md, The Fast Cash Playbook, Description: How many to sell, line 265
  confirmations: 2
  authors_caveat: >-
    With a thousand customers or more, fulfilment will constrain you well before the 5-10% window, and that is fine.
  anchor_at: "playbook-fast-cash.md:265"
- id: B-playbooks-growth-103
  type: rule
  name: >-
    Price at 10x to 50x your average transaction
  statement: >-
    The price is set at ten to fifty times the current average cart value or transaction size.
  why: >-
    The point is to go beyond comparison with your other products and to select for the people who have the purchasing power to buy it (2025).
  anchor: >-
    add a zero. And if you want to get frisky, multiply it by five. So yes, think 10x to 50x your
  source: >-
    playbook-fast-cash.md, The Fast Cash Playbook, Description: What to charge, line 297
  confirmations: 3
  authors_caveat: >-
    You will work more for these customers and will earn that money; you can also price for volume, as long as you scale the features and bonuses to match.
  anchor_at: "playbook-fast-cash.md:297"
- id: B-playbooks-growth-104
  type: rule
  name: >-
    10x The 10%
  statement: >-
    The offer is sized so that ten percent of your customers paying ten times the price would double your revenue.
  why: >-
    The customers are already paid for, so the extra revenue minus delivery drops straight to the bottom line.
  anchor: >-
    10x The 10%: If you get 10% of your customers to pay 10x the price...you double your
  source: >-
    playbook-fast-cash.md, Fast Cash Plays - How Fast Cash Plays Work, line 172
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:172"
- id: B-playbooks-growth-105
  type: rule
  name: >-
    High price points get a one-on-one consultation
  statement: >-
    A high-priced Fast Cash offer is sold on a one-on-one consultation unless volume or an established brand makes that impossible.
  why: >-
    The more personal you make the sale of a personal product, the more bites you get.
  anchor: >-
    For most businesses, high price points deserve a one-on-one consulta-
  source: >-
    playbook-fast-cash.md, The Fast Cash Playbook, Description: How to sell it, line 274
  confirmations: 2
  anchor_at: "playbook-fast-cash.md:274"
- id: B-playbooks-growth-106
  type: rule
  name: >-
    Automated checkout: build tension, then stampede
  statement: >-
    When selling through an automated checkout, tension is built first and then the cart opens to everyone at once, first come first serve.
  applies_when: >-
    Blasting the whole list with an automated checkout rather than selling by consultation.
  anchor: >-
    If  you  blast  your  whole  list  and  have  an  automated  checkout.  Build  up  tension  (launch
  source: >-
    playbook-fast-cash.md, The Fast Cash Playbook, Description: Promoting It, line 280
  confirmations: 2
  anchor_at: "playbook-fast-cash.md:280"
- id: B-playbooks-growth-107
  type: rule
  name: >-
    Consults: buyable on day one, appointments spread across the window
  statement: >-
    When selling by consultation, the offer is purchasable from day one while appointments are spread out, and every sales appointment falls inside the seven-day window.
  why: >-
    Without enough competent salespeople you cannot smash all the consultations together, and limited spots plus first-come-first-serve still apply.
  anchor: >-
    make your thing available for purchase day one,
  source: >-
    playbook-fast-cash.md, The Fast Cash Playbook, Description: Promoting It, line 284
  confirmations: 2
  anchor_at: "playbook-fast-cash.md:284"
- id: B-playbooks-growth-108
  type: rule
  name: >-
    Reply-to-buy with cards on file
  statement: >-
    Where cards are on file, replying that they are in is enough, and the card is charged with their permission or collected by an immediate call.
  applies_when: >-
    Businesses that are not tech savvy enough for an automated checkout.
  anchor: >-
    If you aren’t too tech savvy but have cards on file, then instructions to simply reply to
  source: >-
    playbook-fast-cash.md, The Fast Cash Playbook, Description: Promoting It, line 292
  confirmations: 2
  anchor_at: "playbook-fast-cash.md:292"
- id: B-playbooks-growth-109
  type: rule
  name: >-
    Promote for seven days or less
  statement: >-
    The promotion runs seven days or less, or until the spots run out.
  why: >-
    Any longer and the offer loses urgency; any shorter and you miss sales.
  anchor: >-
    Promote your Fash Cash play for seven days or less or until spots run out.
  source: >-
    playbook-fast-cash.md, The Fast Cash Playbook, Description: Promoting It, line 303
  confirmations: 3
  anchor_at: "playbook-fast-cash.md:303"
- id: B-playbooks-growth-110
  type: rule
  name: >-
    Every message carries a countdown and a new bonus
  statement: >-
    Each message in the sequence adds a countdown and one new bonus, sold with the good it brings and the bad it removes.
  anchor: >-
    Send each message with a countdown and a new bonus. Sell the bonus with expla-
  source: >-
    playbook-fast-cash.md, Summary, line 448
  confirmations: 2
  anchor_at: "playbook-fast-cash.md:448"
- id: B-playbooks-growth-111
  type: rule
  name: >-
    The best bonus comes last and outweighs the price
  statement: >-
    The best bonus is added at the final step of the sequence and is worth more than the entire price tag.
  why: >-
    It is what sells out the remaining spots if they have not sold already.
  anchor: >-
    This should be worth more than the entire price tag and should get you to
  source: >-
    playbook-fast-cash.md, PUSH TO CONSULT SEQUENCE, 24 HOURS OUT, line 330
  confirmations: 2
  anchor_at: "playbook-fast-cash.md:330"
- id: B-playbooks-growth-112
  type: rule
  name: >-
    The cart-open bonus is the most immediate one
  statement: >-
    The bonus announced at cart-open is the one that gives an instant benefit the moment the buyer responds.
  applies_when: >-
    The automated checkout sequence.
  anchor: >-
    You want this bonus to be the most immediate ben-
  source: >-
    playbook-fast-cash.md, PUSH TO AUTOMATED CHECKOUT SEQUENCE, 5 MIN - Cart open, line 358
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:358"
- id: B-playbooks-growth-113
  type: rule
  name: >-
    Notify the list at every milestone
  statement: >-
    The list is told by email and text when a handful have sold, when two spots are left, when it is sold out, and if someone backs out afterwards.
  why: >-
    Announcing the sell-out shows the promotion was justified.
  anchor: >-
    Notify people via email and text message once you’ve sold a handful, when there are
  source: >-
    playbook-fast-cash.md, Summary, line 453
  confirmations: 3
  anchor_at: "playbook-fast-cash.md:453"
- id: B-playbooks-growth-114
  type: rule
  name: >-
    Waitlist after the sell-out
  statement: >-
    Once the spots are gone, people who tried to buy are waitlisted with permission to be charged if a spot opens up.
  anchor: >-
    I’d rather you sell out and then waitlist people who already tried to buy. If they
  source: >-
    playbook-fast-cash.md, PUSH TO AUTOMATED CHECKOUT SEQUENCE, Note, line 371
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:371"
- id: B-playbooks-growth-115
  type: rule
  name: >-
    Prep everything before the announcement
  statement: >-
    All emails, texts and bonuses are ready before the first message of the promotion goes out.
  anchor: >-
    Prep all your emails and texts ahead of time.
  source: >-
    playbook-fast-cash.md, Summary, line 441
  confirmations: 2
  anchor_at: "playbook-fast-cash.md:441"
- id: B-playbooks-growth-116
  type: rule
  name: >-
    Day three or four sell-out checkpoint
  statement: >-
    If the offer has not sold out or close to it by day three or four, the offer is made more compelling before the rest of the sequence is sent.
  anchor: >-
    If you nailed the offer, you should sell out by day three or four. If you haven’t
  source: >-
    playbook-fast-cash.md, Sample Email And Text Sequence, line 574
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:574"
- id: B-playbooks-growth-117
  type: rule
  name: >-
    At least 90% gross margin
  statement: >-
    A Fast Cash Play runs at a gross margin of at least 90%.
  why: >-
    Ten percent of a large number still leaves plenty of cash to spoil the customer with, and the point is to make money (2025).
  anchor: >-
    My Fast Cash Plays run at least 90% gross
  source: >-
    playbook-fast-cash.md, ROI Benchmarks, line 481
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:481"
- id: B-playbooks-growth-118
  type: rule
  name: >-
    Collect the 4Rs
  statement: >-
    At the end of delivery, reviews, results, referrals and resells are collected from the buyers.
  anchor: >-
    Collect the 4Rs at the end: Reviews, Results, Referrals, and Resells.
  source: >-
    playbook-fast-cash.md, Fast Cash Checklist, line 564
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:564"
- id: B-playbooks-growth-119
  type: rule
  name: >-
    Cool the list down and set the next date
  statement: >-
    After the play the list goes back to receiving value, and the date of the next play is set.
  anchor: >-
    Cooldown your list. Get back to providing value.
  source: >-
    playbook-fast-cash.md, Fast Cash Checklist, lines 565-566
  confirmations: 1
  anchor_at: "playbook-fast-cash.md:565"
- id: B-playbooks-growth-120
  type: rule
  name: >-
    Texts carry attention, emails carry detail
  statement: >-
    Texts are paired with the emails to draw attention to them while the emails hold the details of the offer.
  anchor: >-
    I like pairing texts with emails. The texts draw attention to the emails. The emails give
  source: >-
    playbook-fast-cash.md, Sample Email And Text Sequence, line 577
  confirmations: 2
  anchor_at: "playbook-fast-cash.md:577"
- id: B-playbooks-growth-121
  type: rule
  name: >-
    On top of the paid ads chapters of $100M Leads
  statement: >-
    This ad process is applied on top of the paid-ads chapters of $100M Leads, not instead of them.
  anchor: >-
    This is to be used on top of the paid ads chapters in $100M Leads.
  source: >-
    playbook-goated-ads.md, GOATed Ads, Disclaimer, line 44
  confirmations: 1
  anchor_at: "playbook-goated-ads.md:44"
- id: B-playbooks-growth-122
  type: rule
  name: >-
    The Ad Assembly Process quota
  statement: >-
    A weekly ad session produces 50 hooks, three to five meats and one to three CTAs, assembled into 150 to 750 ads.
  why: >-
    Ads are far easier to make in parts than whole, and the volume is what lets ads scale; as a side effect nobody can work out which of your ads is the top performer.
  anchor: >-
    the result of this prep is 50 hooks x 3-5 meat x 1-3 CTAs = 150 to 750 ads…per week.
  source: >-
    playbook-goated-ads.md, The Ad Assembly Process, line 152
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:152"
- id: B-playbooks-growth-123
  type: rule
  name: >-
    80% hooks, 20% meat, ~0% CTAs
  statement: >-
    Ad preparation time is split 80% on hooks, 20% on the meat and effectively none on CTAs.
  why: >-
    Ninety percent of the work in advertising is in the preparation rather than the recording, and if someone does not make it through the hook then nothing else matters.
  anchor: >-
    So we put eighty percent of our time there.
  source: >-
    playbook-goated-ads.md, The Ad Assembly Process, Next Time You film, line 167
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:167"
- id: B-playbooks-growth-124
  type: rule
  name: >-
    Match the hook's driver to the level of awareness
  statement: >-
    Each hook's driver matches the awareness level it targets: offer-driven for most aware, proof-driven for product-aware, promise-driven for solution-aware, pain-driven for problem-aware and curiosity-driven for completely unaware.
  why: >-
    The larger the audience you reach, the more varied your ads must be; to grab a bigger slice of the pie you meet the audience where they are instead of writing only offer and proof hooks.
  anchor: >-
    Most Aware: These hooks are typically offer driven.
  source: >-
    playbook-goated-ads.md, Why Ads Hit A Wall / Writing Expansion Hooks (five levels of awareness after Eugene Schwartz, spelt Swartz at line 98), lines 224-285
  confirmations: 2
  authors_caveat: >-
    Think of these more as frameworks than a magical recipe - a national brand can run an offer-driven hook to everyone because the product and brand are already known.
  anchor_at: "playbook-goated-ads.md:224"
- id: B-playbooks-growth-125
  type: rule
  name: >-
    Spread the hooks broader
  statement: >-
    If 90% of the hooks sit in the most-aware bucket, they are spread across the colder buckets, and in doubt the hook goes broader.
  why: >-
    A broader hook still catches the warm audience and attracts some of the colder audience as well.
  anchor: >-
    If 90% of your hooks land in the “Most aware” bucket, spread them out to capture a
  source: >-
    playbook-goated-ads.md, Writing Expansion Hooks To Enter New Markets, line 356
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:356"
- id: B-playbooks-growth-126
  type: rule
  name: >-
    Refresh creative before expanding the audience
  statement: >-
    When spend stops being profitable, the creative is refreshed first, and only if that has already been done is the targeted audience widened with expansion hooks.
  why: >-
    The wall is your ad quality, not the market: better ads convert a bigger audience.
  anchor: >-
    You likely need to refresh your creative. But let’s say you’ve done that too. If that’s the
  source: >-
    playbook-goated-ads.md, Writing Expansion Hooks To Enter New Markets, line 215
  confirmations: 1
  anchor_at: "playbook-goated-ads.md:215"
- id: B-playbooks-growth-127
  type: rule
  name: >-
    Winning hooks travel between industries and platforms
  statement: >-
    A hook that won in another industry, on another platform or in your own free content is reused in your ads rather than treated as unusable.
  why: >-
    Hooks that worked on one platform or advertising method have the highest likelihood of converting when moved to another.
  anchor: >-
    great paid ads, and see what hooks they are using. Key point: Winning hooks in one
  source: >-
    playbook-goated-ads.md, Writing Hooks For Immediate Results From Previous Winners, line 208
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:208"
- id: B-playbooks-growth-128
  type: rule
  name: >-
    Skip previous winners on a first ad run
  statement: >-
    The previous-winners source of hooks is skipped by anyone running ads for the first time.
  anchor: >-
    Note: If it’s your first time running ads, skip
  source: >-
    playbook-goated-ads.md, Writing Hooks For Immediate Results From Previous Winners, line 182
  confirmations: 1
  anchor_at: "playbook-goated-ads.md:182"
- id: B-playbooks-growth-129
  type: rule
  name: >-
    More and better before new
  statement: >-
    Once ads convert, the work goes into more and better versions of what already works before anything new is tried.
  anchor: >-
    Once you get ads converting, it’s about doing more/better far more than about doing
  source: >-
    playbook-goated-ads.md, Writing Hooks For Immediate Results From Previous Winners, line 210
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:210"
- id: B-playbooks-growth-130
  type: rule
  name: >-
    The widest hooks are memes
  statement: >-
    Meme or meme-like hooks are tested when the goal is the widest possible audience, using the culture-specific memes of whatever group you target.
  why: >-
    A relevant meme works like a moth to a flame and explodes the number of eyeballs exposed to the ad.
  anchor: >-
    Memes or meme-like content attract the largest percentage of your audience.
  source: >-
    playbook-goated-ads.md, Pro Tip: The Widest Hooks Possible, line 332
  confirmations: 1
  anchor_at: "playbook-goated-ads.md:332"
- id: B-playbooks-growth-131
  type: rule
  name: >-
    No offer-driven hooks to a cold broad audience
  statement: >-
    An offer-driven hook is not run to a broad cold audience unless the brand and the product are already known to it.
  why: >-
    The $5 Foot Long worked because the whole nation already knew the brand and what a sandwich is; for a no-name product that needs explaining it is the closest thing to burning money.
  anchor: >-
    a product that people need education to understand, leading with an offer driven hook to
  source: >-
    playbook-goated-ads.md, Writing Expansion Hooks To Enter New Markets, line 348
  confirmations: 1
  anchor_at: "playbook-goated-ads.md:348"
- id: B-playbooks-growth-132
  type: rule
  name: >-
    The meat fulfils the hook, the hook fits the awareness level
  statement: >-
    The creative of an ad fulfils its hook, and the hook matches the awareness level of the audience it is aimed at.
  anchor: >-
    It’s the part of the ad that fulfills your hook. The creative aligns with
  source: >-
    playbook-goated-ads.md, The Ad Meat, line 364
  confirmations: 1
  anchor_at: "playbook-goated-ads.md:364"
- id: B-playbooks-growth-133
  type: rule
  name: >-
    Three to five meats per recording session
  statement: >-
    Three to five meats per weekly recording session is enough, because the body of an ad is rotated far less often than the hook.
  why: >-
    Fewer people see the body of the ad than the hook, so you do not use it up as fast.
  anchor: >-
    rotated less often because fewer people see it. So you don’t ‘use it up’ as often. Usually three to
  source: >-
    playbook-goated-ads.md, The Ad Meat, lines 369-370
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:369"
- id: B-playbooks-growth-134
  type: rule
  name: >-
    Clear > Clever
  statement: >-
    Every ad spells out the exact next action - click this button, call this number, reply YES, go to this website, scan this QR code.
  why: >-
    Interest gives you huge motivation for a tiny window of time, and the audience can only know what to do if you tell them.
  anchor: >-
    Tell them exactly what to do next. S-P-E-L-L it out: Click this
  source: >-
    playbook-goated-ads.md, CTA - Call To Action, line 508
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:508"
- id: B-playbooks-growth-135
  type: rule
  name: >-
    Show the next step, not only tell it
  statement: >-
    The CTA demonstrates what the next step looks like - the button being clicked, the fields being filled, submit being pressed - as well as saying it.
  why: >-
    When they click and get exactly what they expected, they are more likely to follow through; it provides the ultimate congruence.
  anchor: >-
    If you want to take this up a level show and tell them. So not only do you make your
  source: >-
    playbook-goated-ads.md, CTA - Call To Action, line 513
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:513"
- id: B-playbooks-growth-136
  type: rule
  name: >-
    The five elements of a CTA
  statement: >-
    A CTA states what to do, how to do it, when to do it, what they get for doing it, and what happens next.
  why: >-
    Urgency, scarcity, guarantees and bonuses can be layered on top of these basics to get more people to act.
  applies_when: >-
    What happens next matters most with lead magnets and multi-step sales processes.
  anchor: >-
    A good CTA shows or tells: what to do, how to do it, when to do it, what they get for
  source: >-
    playbook-goated-ads.md, CTA - Call To Action, line 533
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:533"
- id: B-playbooks-growth-137
  type: rule
  name: >-
    Test CTAs by changing only the CTA
  statement: >-
    CTAs are tested by running three identical hook-plus-meat ads to the same audience and changing nothing but the CTA.
  anchor: >-
    run three identical hook + ad meat combinations, to the same audience,
  source: >-
    playbook-goated-ads.md, CTA - Call To Action, line 550
  confirmations: 1
  anchor_at: "playbook-goated-ads.md:550"
- id: B-playbooks-growth-138
  type: rule
  name: >-
    Stick with a CTA that works
  statement: >-
    Once a CTA follows the fundamentals and works, it is kept rather than reinvented each session.
  why: >-
    A sound CTA has never broken a campaign, but having no CTA has.
  anchor: >-
    But once you have a clear one that fol-
  source: >-
    playbook-goated-ads.md, CTA - Call To Action, line 563
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:563"
- id: B-playbooks-growth-139
  type: rule
  name: >-
    Double down on the winners
  statement: >-
    When a few ads wildly outperform the rest, their hooks are reused to make more variations instead of moving on to something else.
  why: >-
    In the beginning you cannot know which ads will hit, so you make many variations for the different segments of the market; and new customers enter the market every day, so repeating what works is still their first exposure.
  anchor: >-
    And when you find those, double down
  source: >-
    playbook-goated-ads.md, Scale It, line 623
  confirmations: 2
  anchor_at: "playbook-goated-ads.md:623"
- id: B-playbooks-growth-140
  type: rule
  name: >-
    Kaleidoscope Ads only after you have winners
  statement: >-
    Kaleidoscope Ads are only run once this process has produced winning ads.
  anchor: >-
    you have winners, you’ll be ready for the next step: Kaleidoscope Ads. It’s how I take ads to
  source: >-
    playbook-goated-ads.md, Final Note, line 628
  confirmations: 1
  anchor_at: "playbook-goated-ads.md:628"
```
