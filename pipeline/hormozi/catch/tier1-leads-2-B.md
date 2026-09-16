# Улов фазы 1 — $100M Leads (2023), from #4 Run Paid Ads to the end (lines 6901–14623) (ярус 1), тип B: правила и критерии

Группа `tier1-leads-2`, слаг `leads-2`, ярус 1. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **124** (экстрактор вернул 124, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-leads.md` | 6901–14623 | 7 | 124 |

## Как собран файл

Экстрактор B (Rules and criteria) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier1-leads-2.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier1-leads-2-B.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 1 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: B-leads-2-001
  type: rule
  statement: >-
    An audience is only broadened after the smaller one has been advertised to profitably, and is made as big as it can be while still turning a profit.
  why: >-
    As the audience gets bigger it has more of the wrong people but more of the right ones too, so the ratio of spend to sales drops while the total money made goes up.
  applies_when: >-
    Scaling paid ads from a first working audience.
  anchor: >-
    Once we advertise profitably in a small puddle of an audience, we
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, lines 7096–7106
  confirmations: 2
  anchor_at: "100m-leads.md:7096"
- id: B-leads-2-002
  type: rule
  statement: >-
    A platform is only chosen for advertising when all four are true: you have used it and got value from it as a consumer, you can target people on it who are interested in your stuff, you know how to format ads for it, and you have the minimum money to place an ad.
  why: >-
    Having used it yourself gives you some idea how it works, and platforms change all the time while these principles stay the same.
  applies_when: >-
    Picking where to run paid ads; start with one platform that meets all four.
  anchor: >-
    I\'ve used it and gotten value from it as a consumer. So I have
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step 1, lines 7148–7177
  confirmations: 2
  anchor_at: "100m-leads.md:7152"
- id: B-leads-2-003
  type: rule
  statement: >-
    Targeting is judged by one goal only: getting the highest number of people who you think will buy your stuff to see the ad.
  why: >-
    The right message to the wrong audience falls on deaf ears no matter how good the ads are.
  applies_when: >-
    Setting targeting on any ad platform.
  anchor: >-
    So you have only one goal when targeting--get the highest number of
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #2, lines 7203–7207
  confirmations: 1
  anchor_at: "100m-leads.md:7206"
- id: B-leads-2-004
  type: rule
  name: >-
    Lookalike audience
  statement: >-
    The list uploaded to build a lookalike audience is assembled in order of quality — current and previous customers first, then warm reach out contacts, then cold reach out leads — only until the platform minimum is reached.
  why: >-
    The bigger the list and the higher quality the contacts, the more responsive the lookalike audience; forcing the list to size sometimes makes it too broad, which filters then fix.
  applies_when: >-
    The platform allows lookalike audiences; if you cannot make one, start by targeting interests.
  anchor: >-
    Start with your list of current and previous customers. If your
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #2, lines 7218–7269
  confirmations: 2
  anchor_at: "100m-leads.md:7225"
- id: B-leads-2-005
  type: rule
  statement: >-
    Filters are stacked on top of the audience early on to make the list more specific, and loosened later, not the other way round.
  why: >-
    The more specific the list, the more efficient the ads but the faster you burn through it; the wins from small specific audiences pay for advertising to larger, broader ones later.
  applies_when: >-
    Early paid-ad campaigns with a limited budget.
  anchor: >-
    the list, the more efficient your ads but the faster you will "burn"
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #2, lines 7251–7256
  confirmations: 1
  anchor_at: "100m-leads.md:7252"
- id: B-leads-2-006
  type: rule
  name: >-
    Call Out
  statement: >-
    The majority of the effort on an ad goes into its first five seconds (the headline or opening), and that first impression is the element tested most.
  why: >-
    The purpose of each second of the ad is to sell the next second, and as David Ogilvy says, after you have written your headline you have spent eighty cents of your advertising dollar; focusing on the first five seconds made the author's advertising 20x more effective.
  applies_when: >-
    Writing or testing any ad.
  anchor: >-
    The purpose of each second of the ad is to sell the next second of the
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #3, lines 7313–7324
  confirmations: 2
  anchor_at: "100m-leads.md:7315"
- id: B-leads-2-007
  type: rule
  statement: >-
    A callout is specific enough to get the right people and broad enough to get as many of them as possible.
  why: >-
    Callouts run from hyperspecific (only one person turns) to not specific at all (everyone turns); both get attention, and the useful setting is the widest one that still calls the right people.
  applies_when: >-
    Writing the opening of an ad.
  anchor: >-
    And I try to make my call outs specific enough to get the
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #3, lines 7345–7355
  confirmations: 1
  anchor_at: "100m-leads.md:7352"
- id: B-leads-2-008
  type: rule
  name: >-
    Labels
  statement: >-
    A label used as a callout is one your ideal customers actually identify with.
  why: >-
    A label is a word or set of words putting people into a group, and it only catches attention if the person places themselves in that group.
  applies_when: >-
    Using verbal callouts (features, traits, titles, places, descriptors).
  anchor: >-
    To be most effective, ]{.calibre3}[your ideal customers
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #3, lines 7364–7369
  confirmations: 1
  anchor_at: "100m-leads.md:7368"
- id: B-leads-2-009
  type: rule
  statement: >-
    In a local ad the callout names the smallest local area the buyer identifies with, combined with the type of person (LOCAL AREA + TYPE OF PERSON).
  why: >-
    People automatically identify with their local area, so the more local, the better: Americans < Texans < Dallas Residents < Irving Residents.
  applies_when: >-
    Advertising a local business.
  anchor: >-
    So with local ads, the more local, the better. A local
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #3, lines 7372–7380
  confirmations: 1
  anchor_at: "100m-leads.md:7373"
- id: B-leads-2-010
  type: rule
  name: >-
    Likeness
  statement: >-
    The people shown in an ad match the breadth of the customer base — more ethnicities, ages, genders and personalities for a broad base, people who look like the buyer for a narrow one.
  why: >-
    People want to work with people who look, talk and act in ways familiar to them, and you may not look, talk or act in ways familiar to them.
  applies_when: >-
    Choosing the spokesperson and cast of an ad.
  anchor: >-
    talk, or act in ways familiar to them). So if you serve a broad customer
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #3, lines 7442–7452
  confirmations: 1
  anchor_at: "100m-leads.md:7449"
- id: B-leads-2-011
  type: rule
  name: >-
    Quack like a duck
  statement: >-
    The spokesperson, dress and setting of an ad look like the audience being called out — to attract plumbers, dress like a plumber, talk like a plumber, be in a plumbing environment.
  why: >-
    Even with the same message, the ad does far better if you look the part (or find people who do).
  applies_when: >-
    Nonverbal callouts: setting and spokesperson.
  anchor: >-
    environment. Even with the same message, your ad will do far better if
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #3, lines 7455–7460
  confirmations: 1
  anchor_at: "100m-leads.md:7459"
- id: B-leads-2-012
  type: rule
  statement: >-
    The ad makes the benefits look as big as possible and the costs look as small as possible.
  why: >-
    If people think an offer or lead magnet has big benefits and tiny costs they value it and will exchange money or contact information for it; if the cost outweighs the benefits they will not.
  applies_when: >-
    Writing the value section of any ad.
  anchor: >-
    So the best ads make the benefits look as big as possible
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #3, lines 7539–7546
  confirmations: 1
  anchor_at: "100m-leads.md:7543"
- id: B-leads-2-013
  type: rule
  statement: >-
    The ad answers the question the prospect is thinking at the moment they think it, in the words they would use.
  why: >-
    Ads cause the prospect to think questions to themselves, and a good ad answers those questions at precisely the time they think it; in David Ogilvy's words, the customer is not a moron, she is your wife.
  applies_when: >-
    Writing ad copy.
  anchor: >-
    they think it. So if you can answer what they're thinking with your ad,
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #3, lines 7571–7576
  confirmations: 1
  anchor_at: "100m-leads.md:7575"
- id: B-leads-2-014
  type: rule
  statement: >-
    Ad length is varied by adding or removing value angles, while the callout (the first few seconds) and the CTA stay the same.
  why: >-
    The only difference between long ads and short ads is how many angles from the copywriting framework there is time to cover.
  applies_when: >-
    Adapting one ad to platforms with different lengths.
  anchor: >-
    away based on the platform, but keep the callouts (the first few
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #3, lines 7806–7810
  confirmations: 1
  anchor_at: "100m-leads.md:7809"
- id: B-leads-2-015
  type: rule
  name: >-
    CTA - Tell Them What To Do Next
  statement: >-
    The ad spells out exactly one next action — click this button, call this number, reply with YES, go to this website, scan this QR code.
  why: >-
    After a good ad the audience has huge motivation for a tiny time, and they can only know what to do if you tell them.
  applies_when: >-
    Every ad, and everywhere else you tell an audience to do something.
  anchor: >-
    S-P-E-L-L it out: Click this button. Call this number. Reply with "YES."
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #3, lines 7856–7866
  confirmations: 1
  anchor_at: "100m-leads.md:7863"
- id: B-leads-2-016
  type: rule
  statement: >-
    The action the CTA asks for is quick and easy: easy phone numbers, obvious buttons, and a short memorable web address rather than a long path.
  why: >-
    A common CTA sends the audience to a website, and acquisition.com/training is actionable where alexsprivateequityfirm.com/free-book-and-course2782 is not.
  applies_when: >-
    Designing the mechanics of a call to action.
  anchor: >-
    Make CTAs quick and easy]{.calibre41}[. Easy phone numbers, obvious
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #3, lines 7870–7890
  confirmations: 1
  anchor_at: "100m-leads.md:7870"
- id: B-leads-2-017
  type: rule
  statement: >-
    After the prospect takes the action from the ad, their contact information is collected — permission to contact them is what turns them into an engaged lead.
  why: >-
    We are not selling in the ad, we are asking if they are interested; when they give a way to tell them more, they become engaged leads.
  applies_when: >-
    Any paid ad campaign; the author's default mechanism is a simple landing page.
  anchor: >-
    After they take the action--Get. Their. Contact.
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #4, lines 7913–7954
  confirmations: 1
  anchor_at: "100m-leads.md:7917"
- id: B-leads-2-018
  type: rule
  statement: >-
    The landing page is kept simple, with the words and the image as the things being tested.
  why: >-
    The simpler the landing page, the easier it is to test.
  applies_when: >-
    Building the page that collects contact information.
  anchor: >-
    your landing page, the easier it is to test. Focus on the words and the
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #4, lines 7917–7922
  confirmations: 1
  anchor_at: "100m-leads.md:7920"
- id: B-leads-2-019
  type: rule
  statement: >-
    The landing page carries the same look and language as the ad, and delivers what the ad promised.
  why: >-
    People click an ad because you promised them a benefit; a Frankenstein experience where everything looks different wastes money until it is fixed. You want a continuous experience from click to close.
  applies_when: >-
    Any ad that sends traffic to a page.
  anchor: >-
    And make your landing pages match your ads.]{.calibre41}[ People click
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #4, lines 7930–7936
  confirmations: 1
  anchor_at: "100m-leads.md:7930"
- id: B-leads-2-020
  type: rule
  statement: >-
    Each next step reminds the person of the action they just took and shows how the next action follows from it.
  why: >-
    In Robert Cialdini's Influence, people like to think of themselves as consistent, so reminding them of the action they just took gets more of them to take the second one.
  applies_when: >-
    Multi-step opt-in flows (ad to CTA to contact information).
  anchor: >-
    action they just took (CTA), and show how taking the next action aligns
  source: >-
    100m-leads.md, #4 Run Paid Ads Part I, Step #4, lines 7940–7947
  confirmations: 1
  anchor_at: "100m-leads.md:7943"
- id: B-leads-2-021
  type: rule
  name: >-
    Phase One: Track Money
  statement: >-
    Tracking of returns is set up and working before the first dollar is spent on ads.
  why: >-
    Without tracking you get cleaned out, like playing a casino game for as long as you feel like rather than as long as you can afford; with tracking you can do more of what makes money and less of what does not.
  applies_when: >-
    Before starting paid advertising.
  anchor: >-
    Before spending a dollar on ads, set everything up
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, lines 8094–8103
  confirmations: 1
  anchor_at: "100m-leads.md:8095"
- id: B-leads-2-022
  type: rule
  statement: >-
    A new ad is given a test budget of two times the cash collected from a customer in the first thirty days (not LTGP) before it is shut off, as long as it is producing leads.
  why: >-
    Letting ads run too long wastes money, but giving up on ads before they have had a chance wastes even more; two times thirty-day cash is the author's sweet spot.
  applies_when: >-
    Testing new paid ads. Figure from $100M Leads, 2023.
  anchor: >-
    I budget two times the cash I collect from a customer in thirty days
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, lines 8146–8157
  confirmations: 1
  anchor_at: "100m-leads.md:8146"
- id: B-leads-2-023
  type: rule
  statement: >-
    An ad producing no leads at all is shut off before it has spent one times the thirty-day cash from a customer.
  why: >-
    Below that spend there is nothing to learn from an ad that has produced nothing, and the money is better spent on the next test.
  applies_when: >-
    Testing new paid ads that generate zero leads.
  anchor: >-
    leads from an ad at all, before I spend 1x thirty-day cash I shut it off
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, lines 8155–8157
  confirmations: 1
  anchor_at: "100m-leads.md:8156"
- id: B-leads-2-024
  type: rule
  name: >-
    Phase Three: Print Money
  statement: >-
    Once ads make back more money than they cost, the budget is raised as far as the rest of the business can take it.
  why: >-
    If you had a magic machine that gave you ten dollars for every one you put in, the budget would be all the money; the limit is the other constraints of the business, not the ads.
  applies_when: >-
    Ads are profitable and tracked.
  anchor: >-
    you spend - the answer is simple - ]{.calibre3}[spend as much as you
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, lines 8176–8183
  confirmations: 1
  anchor_at: "100m-leads.md:8178"
- id: B-leads-2-025
  type: rule
  statement: >-
    Once ads break even or better, the daily ad budget is calculated backwards from how many customers you want or can handle multiplied by your cost per customer, and then committed to.
  why: >-
    The question stops being how much to spend and becomes how many customers you can handle; if the resulting number terrifies you, you are doing it right — trust the data.
  applies_when: >-
    Ads at or above break-even.
  anchor: >-
    ads break even or better, I reverse my budget from my sales
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, lines 8187–8198
  confirmations: 1
  anchor_at: "100m-leads.md:8189"
- id: B-leads-2-026
  type: rule
  statement: >-
    The budget reversed from a customer goal is padded by twenty percent.
  why: >-
    Ads get less efficient as they scale, so 100 customers at $100 needs $12,000 over thirty days ($400 per day), not $10,000.
  applies_when: >-
    Scaling a profitable ad budget.
  anchor: >-
    they scale, I usually pad the budget by twenty percent. So that means
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, lines 8190–8195
  confirmations: 1
  anchor_at: "100m-leads.md:8193"
- id: B-leads-2-027
  type: rule
  name: >-
    LTGP to CAC
  statement: >-
    Paid advertising is measured as lifetime gross profit per customer divided by cost to acquire a customer, and the ratio has to be above 3 to 1.
  why: >-
    Every business the author invests in that struggles to scale has an LTGP to CAC below 3 to 1, and as soon as it goes above 3 to 1, by lowering CAC or raising LTGP, they take off; all the costs of getting a customer together should be at most one third of the lifetime profit.
  applies_when: >-
    Judging whether advertising and the business model are working. Benchmark from $100M Leads, 2023.
  anchor: >-
    to CAC ratio was ]{.calibre3}[less than]{.calibre24}[ 3 to 1. As soon as
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, lines 8248–8253; #2 Employees, lines 11295–11298; #4 Affiliates, lines 13144–13146
  confirmations: 3
  authors_caveat: >-
    "This is a pattern I personally observed, not a rule."
  anchor_at: "100m-leads.md:8250"
- id: B-leads-2-028
  type: rule
  statement: >-
    Whether to fix the ads or the business model is decided by comparing your CAC with the industry average: below 3x the average, work on LTGP; above 3x the average, work on the advertising.
  why: >-
    Entrepreneurs usually think they have crappy ads (high CAC) when they have a crappy business model (low LTGP); CAC between competitors in the same industry is much closer than you would think, and the difference between winners and losers is how much they make off each customer.
  applies_when: >-
    Diagnosing unprofitable advertising; requires research into the industry average CAC.
  anchor: >-
    below 3x your industry average (good), ]{.calibre3}[focus on your
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, lines 8299–8316
  confirmations: 1
  anchor_at: "100m-leads.md:8302"
- id: B-leads-2-029
  type: rule
  name: >-
    Client financed acquisition
  statement: >-
    The customer pays back more than it costs to get and fulfil them within the first thirty days, so the cash can be recycled into getting the next customer.
  why: >-
    Any business can get interest-free money for thirty days in the form of a credit card; cover the cost to get and fulfil the customer in that window and you square the balance, keep the customer and repeat, so money stops being the bottleneck.
  applies_when: >-
    The full LTGP takes months to collect and cash flow blocks scaling.
  anchor: >-
    But... if your customer spends more than it costs you to get
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, lines 8337–8453
  confirmations: 2
  anchor_at: "100m-leads.md:8337"
- id: B-leads-2-030
  type: rule
  statement: >-
    When the first purchase does not cover CAC inside thirty days, more is sold to the customer immediately rather than waiting for the lifetime profit to accumulate.
  why: >-
    A $100 upsell with 100% margins taken by one in five customers adds $20 of gross profit per customer, which turns $10 collected in thirty days into $30 and covers a $30 CAC; everything after that is gravy.
  applies_when: >-
    LTGP exceeds CAC but the first purchase does not, creating a cash flow problem.
  anchor: >-
    Here's the way I fix it- ]{.calibre3}[I immediately sell them more
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, lines 8390–8439
  confirmations: 1
  anchor_at: "100m-leads.md:8402"
- id: B-leads-2-031
  type: rule
  name: >-
    Don't Confuse Sales Problems With Advertising Problems
  statement: >-
    Before blaming the ads, ask whether the engaged leads have the problem you solve and the money to spend: if they do and are not buying, it is a sales problem, not an advertising problem.
  why: >-
    A company spent twelve weeks and $150,000 on ads that were getting the right leads on the phone; the ads worked and the sales did not, and confusing the two cost an estimated ~$30M in enterprise value. If the leads are not qualified, that is the advertising problem; if they are qualified and buying but too few, that is also advertising.
  applies_when: >-
    CAC is above 3x the industry average, or an owner concludes that advertising does not work.
  anchor: >-
    the problem you solve and the money to spend, and they're not
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, lines 8463–8475; #2 Employees, lines 11266–11291
  confirmations: 2
  anchor_at: "100m-leads.md:8473"
- id: B-leads-2-032
  type: rule
  statement: >-
    A free content piece that generated sales or performed very well is turned into a paid ad.
  why: >-
    Nine times out of ten a free content piece that performs well makes a great paid ad; user generated testimonials and reviews that do well as content often make killer ads too, at no extra work.
  applies_when: >-
    You already post free content and are looking for ad creative.
  anchor: >-
    you make a free content piece that generates sales, or performs very
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, Personal Lessons, lines 8477–8489
  confirmations: 1
  anchor_at: "100m-leads.md:8479"
- id: B-leads-2-033
  type: rule
  statement: >-
    Paid advertising starts with an amount of money per month you have decided you are willing to lose, and you expect to lose it.
  why: >-
    You will lose money more times than you make it; the number of losses is high but each loss is small because you know when to shut it down, and you will not be earning, you will be learning.
  applies_when: >-
    First paid ad campaigns.
  anchor: >-
    Spend money. Start with an acceptable amount of money you are willing to
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, lines 8505–8525
  confirmations: 2
  anchor_at: "100m-leads.md:8523"
- id: B-leads-2-034
  type: rule
  statement: >-
    Of the core four, paid ads are taken up last.
  why: >-
    Skills from the other three methods transfer to this one, and paid ads cost money — money you will have if you start with the other three first, which gives the shortest learning curve.
  applies_when: >-
    Choosing the order in which to learn the core four.
  anchor: >-
    I recommend doing paid ads ]{.calibre3}[last]{.calibre41}[ for two
  source: >-
    100m-leads.md, #4 Run Paid Ads Part II, Conclusion, lines 8555–8560
  confirmations: 1
  anchor_at: "100m-leads.md:8555"
- id: B-leads-2-035
  type: rule
  name: >-
    The Rule of 100
  statement: >-
    You do 100 primary advertising actions every day for 100 days in a row — 100 warm reach outs, 100 cold reach outs, 100 minutes making content, or 100 minutes making paid ads plus 100 days of running them.
  why: >-
    Do 100 primary actions per day for 100 days straight and you will get more engaged leads; people who say advertising does not work did 100 over six weeks, which is 1/42 of the work required — it was 100 per day, not 100 over time.
  applies_when: >-
    Any of the core four, once you know the activity works at all.
  anchor: >-
    The rule of 100 is simple. You advertise your stuff by doing 100
  source: >-
    100m-leads.md, Core Four On Steroids, lines 8805–8886; Open To Goal, lines 13754–13757
  confirmations: 2
  anchor_at: "100m-leads.md:8810"
- id: B-leads-2-036
  type: rule
  statement: >-
    At least one piece of content is released per day on a platform, on top of the 100 minutes per day spent making it.
  why: >-
    The rule of 100 for content is measured in minutes of making plus a daily release, and as you get better you post even more.
  applies_when: >-
    Applying the rule of 100 to posting free content.
  anchor: >-
    Release at least one per day on a platform. As you get better, post
  source: >-
    100m-leads.md, Core Four On Steroids, lines 8834–8848
  confirmations: 1
  anchor_at: "100m-leads.md:8842"
- id: B-leads-2-037
  type: rule
  statement: >-
    Cold advertising at rule-of-100 volume is run with automation, because response rates are lower.
  why: >-
    As with all cold advertising, expect lower response rates, so the volume has to come from somewhere other than manual work.
  applies_when: >-
    100 cold reach outs per day.
  anchor: >-
    As with all cold advertising, expect lower response rates, so use
  source: >-
    100m-leads.md, Core Four On Steroids, lines 8852–8866
  confirmations: 1
  anchor_at: "100m-leads.md:8865"
- id: B-leads-2-038
  type: rule
  name: >-
    Constraints
  statement: >-
    Testing is concentrated on the step of the funnel where the most leads drop off.
  why: >-
    Constraints are the points where the smallest improvements create the biggest boost: improving a 5% apply step by 5 points doubles leads (2x), while the same 5 points on a 30% optin adds 16% and on a 50% schedule adds 10%.
  applies_when: >-
    Choosing what to test next in any lead flow.
  anchor: >-
    "drop-off" point. So ]{.calibre3}[I do the most testing at whatever step
  source: >-
    100m-leads.md, Core Four On Steroids, Better, lines 8924–8970
  confirmations: 2
  anchor_at: "100m-leads.md:8925"
- id: B-leads-2-039
  type: rule
  statement: >-
    One split test is run per week per platform, started on the same day each week and given the full week.
  why: >-
    Testing several things at once on one platform means never learning what worked, steps affect each other, one test per week forces you to prioritise, and a week is long enough to see whether the change was actually an improvement.
  applies_when: >-
    Any ongoing testing schedule; a week is what fits the author's team size and spend.
  anchor: >-
    Here's how I get better]{.calibre41}[: ]{.calibre3}[I test one thing
  source: >-
    100m-leads.md, Core Four On Steroids, Better, lines 8974–9011
  confirmations: 1
  anchor_at: "100m-leads.md:8974"
- id: B-leads-2-040
  type: rule
  statement: >-
    The one weekly test is not spent on a trivial change such as red to bright red.
  why: >-
    You can run an infinite number of tests but time is limited, so the tests have to be chosen for the ones that will get the most engaged leads.
  applies_when: >-
    Picking the content of the weekly split test.
  anchor: >-
    you only do one "big" test per week per platform, don't waste it on a
  source: >-
    100m-leads.md, Core Four On Steroids, Better, lines 8994–8999
  confirmations: 1
  anchor_at: "100m-leads.md:8997"
- id: B-leads-2-041
  type: rule
  statement: >-
    The result of every test is written down in a log of all tests.
  why: >-
    So that the next time you do something you start a zillion improvements later, not at square one.
  applies_when: >-
    Every completed split test.
  anchor: >-
    results of the test in a log of all tests. So the next time we do
  source: >-
    100m-leads.md, Core Four On Steroids, Better, lines 9019–9022
  confirmations: 1
  anchor_at: "100m-leads.md:9020"
- id: B-leads-2-042
  type: rule
  statement: >-
    If the current best version cannot be beaten in four tries (or one month), work moves to the next constraint.
  why: >-
    Beyond that point the effort put into making the step better brings lower and lower returns than the same effort spent elsewhere.
  applies_when: >-
    Running weekly tests against a current champion version.
  anchor: >-
    running in ]{.calibre3}[four tries (or one month)]{.calibre24}[, we move
  source: >-
    100m-leads.md, Core Four On Steroids, Better, lines 9025–9035
  confirmations: 1
  anchor_at: "100m-leads.md:9027"
- id: B-leads-2-043
  type: rule
  name: >-
    When to do new
  statement: >-
    Something new is added only when the returns from doing more and better are lower than what the same effort would return in a new placement or a new way of advertising.
  why: >-
    New is much harder in practice, which is why more and better are exhausted first.
  applies_when: >-
    Deciding whether to add a placement, a platform or a core four activity.
  anchor: >-
    from doing more↔better are lower than what you could get from a new
  source: >-
    100m-leads.md, Core Four On Steroids, New, lines 9104–9157
  confirmations: 2
  anchor_at: "100m-leads.md:9105"
- id: B-leads-2-044
  type: rule
  statement: >-
    More and better are exhausted on what you already do before anything new is started.
  why: >-
    The biggest increases often come from advertising more, and doing more until it breaks makes the next drop-off point obvious so better has something to work on.
  applies_when: >-
    Any business that already has one working advertising activity.
  anchor: >-
    Exhaust more better first. Once you can't do
  source: >-
    100m-leads.md, Core Four On Steroids, lines 9151–9190
  confirmations: 2
  anchor_at: "100m-leads.md:9151"
- id: B-leads-2-045
  type: rule
  statement: >-
    New is added in the order new placements, then new platforms, then a new core four activity.
  why: >-
    The order comes down to one thing — what will get the most leads for the amount of work — and nine times out of ten it goes in that order.
  applies_when: >-
    Expanding after more and better are exhausted.
  anchor: >-
    [new]{.calibre24}[. Use this rough order: new placement, new
  source: >-
    100m-leads.md, Core Four On Steroids, New, lines 9110–9157
  confirmations: 2
  anchor_at: "100m-leads.md:9154"
- id: B-leads-2-046
  type: rule
  statement: >-
    After warm outreach, the next core four activity is chosen by what you have more of: more time than money means posting content, more money than time means cold outreach or paid ads.
  why: >-
    Advertising is paid for with time, money, or both, and the method picked should be paid for with the resource you actually have.
  applies_when: >-
    Building a business and choosing where to put advertising effort next.
  anchor: >-
    I have more time than money, I move to posting content. If I have more
  source: >-
    100m-leads.md, Core Four On Steroids, Conclusion, lines 9214–9217
  confirmations: 1
  anchor_at: "100m-leads.md:9216"
- id: B-leads-2-047
  type: rule
  statement: >-
    One core four activity is picked and maxed out with more, better and new before a second is added.
  why: >-
    You only need one to get engaged leads, and the money, systems and experience earned from one method help you master the next.
  applies_when: >-
    Starting out with the core four.
  anchor: >-
    But remember, you only need to do ]{.calibre3}[one]{.calibre41}[ to get
  source: >-
    100m-leads.md, Core Four On Steroids, Conclusion, lines 9221–9232
  confirmations: 1
  anchor_at: "100m-leads.md:9221"
- id: B-leads-2-048
  type: rule
  name: >-
    The referral growth equation
  statement: >-
    Referrals are compared with churn: if the percentage of referrals each month is greater than the percentage of customers who leave, the business grows without any other advertising.
  why: >-
    Referrals in minus churned customers out; if referrals equal churn you need other advertising to grow, if they are less than churn you advertise just to break even. Nothing scales like word of mouth because it is exponential rather than linear.
  applies_when: >-
    Assessing whether word of mouth can carry growth.
  anchor: >-
    If referrals are greater than churn: you grow without any other
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 9813–9842
  confirmations: 1
  anchor_at: "100m-leads.md:9824"
- id: B-leads-2-049
  type: rule
  statement: >-
    If customers are not bringing you more customers, the product is treated as the problem, not the advertising.
  why: >-
    If your product were exceptional, people would already know about it and you would have more business than you could handle; the question to ask is why customers are too embarrassed to tell everyone they know about it — it may be okay, but unremarkable, as in not worthy of remark.
  applies_when: >-
    Selling direct to consumers with few or no referrals.
  anchor: >-
    business than you could handle. So if you sell direct to consumers and
  source: >-
    100m-leads.md, #1 Customer Referrals, Problem #1, lines 9870–9905
  confirmations: 2
  anchor_at: "100m-leads.md:9882"
- id: B-leads-2-050
  type: rule
  name: >-
    Goodwill
  statement: >-
    Goodwill, the gap between price and value, is built by giving more value rather than by lowering the price.
  why: >-
    Lower the price enough and people line up but you lose money, so a price cut is at best a temporary solution; as Rory Sutherland says, any fool can sell something for less. Lots of goodwill creates word of mouth, and word of mouth means referrals.
  applies_when: >-
    Trying to increase referrals.
  anchor: >-
    So, to build goodwill to get referrals, the question isn't how do we
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 9913–9938
  confirmations: 1
  anchor_at: "100m-leads.md:9937"
- id: B-leads-2-051
  type: rule
  name: >-
    Call Outs → Sell Better Customers
  statement: >-
    You work out what your most successful customers have in common, retarget the advertising callouts at that narrower group, and then sell only people who meet those criteria.
  why: >-
    Customers who get the most value have the most goodwill and are the most likely to refer; increase the quality of the prospect and you increase the quality of the product.
  applies_when: >-
    A business with sales but high churn and a plateau.
  anchor: >-
    Figure out what your most successful customers have in common. Use those
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 9974–10019
  confirmations: 1
  anchor_at: "100m-leads.md:10015"
- id: B-leads-2-052
  type: rule
  name: >-
    Dream Outcome → Set Better Expectations
  statement: >-
    The promises made in the offer are lowered step by step until close rates start to drop, and then held there.
  why: >-
    You set the expectations, so lowering them leaves room to overdeliver, and that maximises both the number of customers you get and the goodwill you build with them.
  applies_when: >-
    Wanting more referrals from an existing offer.
  anchor: >-
    making offers. Keep lowering them until your close rates lower. At that
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10025–10061
  confirmations: 1
  anchor_at: "100m-leads.md:10058"
- id: B-leads-2-053
  type: rule
  name: >-
    Increase Perceived Likelihood of Achievement → Get More People Better Results
  statement: >-
    You survey and interview the customers with the best results, find the actions they had in common, and force new customers to repeat those actions.
  why: >-
    At Gym Launch, gym owners who ran paid ads and made a sale in the first seven days tripled their LTGP; once everyone was pushed to launch ads and sell in the first seven days, average results skyrocketed and more testimonials and referrals followed.
  applies_when: >-
    Improving average customer results in order to get referrals.
  anchor: >-
    Step #4: Force new customers to repeat the actions that got the best
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10069–10141
  confirmations: 2
  anchor_at: "100m-leads.md:10116"
- id: B-leads-2-054
  type: rule
  statement: >-
    The conditions of the guarantee are set to the actions that produce the best results.
  why: >-
    Matching the guarantee to those actions gets more people to do them.
  applies_when: >-
    You have identified what the best customers do differently.
  anchor: >-
    Match the conditions of your guarantee to the
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10126–10140
  confirmations: 2
  anchor_at: "100m-leads.md:10126"
- id: B-leads-2-055
  type: rule
  name: >-
    Decrease Time Delay → Make Faster Wins
  statement: >-
    Outcomes are broken into the smallest possible increments and delivered at shorter intervals, and the customer is updated as often as is reasonable even when there is no progress.
  why: >-
    A week of work delivered as daily updates is the same progress with seven times the wins; and if someone said seven things would happen and all seven do, trust rises, which makes referring a friend lower risk.
  applies_when: >-
    Any product delivered over time.
  anchor: >-
    possible increment. Communicate as often as reasonable (even if there is
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10147–10198
  confirmations: 2
  anchor_at: "100m-leads.md:10195"
- id: B-leads-2-056
  type: rule
  statement: >-
    As many wins as possible are forced into the first forty-eight hours after purchase.
  why: >-
    Customers form their lasting impression of a business within the first forty-eight hours after they buy, so that impression is forced rather than left to chance: set many expectations, meet many expectations, repeat.
  applies_when: >-
    Onboarding a new customer.
  anchor: >-
    first forty-eight hours after they buy. Force a good impression.
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10176–10179
  confirmations: 1
  anchor_at: "100m-leads.md:10177"
- id: B-leads-2-057
  type: rule
  name: >-
    BAMFAM (Book-A-Meeting-From-A-Meeting)
  statement: >-
    The customer always knows the next time they will hear from you; a meeting is booked from the meeting.
  why: >-
    Never leave a customer in no man's land — they should always know what happens next.
  applies_when: >-
    Every customer interaction.
  anchor: >-
    They should always know the next time they'll hear from you. I got
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10181–10185
  confirmations: 1
  anchor_at: "100m-leads.md:10181"
- id: B-leads-2-058
  type: rule
  statement: >-
    Fifty percent is added to every timeline given to a customer so that delivery is always early and never late.
  why: >-
    Never expect customers to forgive you; padding the timeline makes on time for you early for them.
  applies_when: >-
    Quoting delivery dates.
  anchor: >-
    you can deliver early, but never late. I add fifty percent
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10187–10190
  confirmations: 1
  anchor_at: "100m-leads.md:10188"
- id: B-leads-2-059
  type: rule
  name: >-
    Decrease Effort and Sacrifice → Keep Making Your Stuff Better
  statement: >-
    A monthly loop runs on the product: survey and support data to find the most common problem, a fix built with feedback from customers who made it work anyway, release to a small group of struggling customers, then roll out or go back, then move to the next most common problem.
  why: >-
    There is no such thing as a perfect product and the easier you make it for customers to benefit, the more goodwill you get and the more likely they are to refer.
  applies_when: >-
    Running an existing product; set as a recurring monthly process.
  anchor: >-
    changes. Implement. Measure. Repeat. I run this process every month. Set
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10206–10251
  confirmations: 1
  anchor_at: "100m-leads.md:10248"
- id: B-leads-2-060
  type: rule
  name: >-
    Call To Action → Tell Them What To Buy Next
  statement: >-
    Every customer is sold again, with a next offer more compelling than the first, and reminded to buy more after each big win.
  why: >-
    If you do not satisfy their desire to buy, they will still buy — from someone else; customers who fall off the product are unlikely to refer, and the more things they can buy, the more they can refer their friends to.
  applies_when: >-
    After the first purchase and after each big customer win.
  anchor: >-
    time you\'ve sold them. Make sure your next offer is more compelling
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10259–10291
  confirmations: 1
  anchor_at: "100m-leads.md:10287"
- id: B-leads-2-061
  type: rule
  statement: >-
    A request for referrals is built as an offer, showing the value the customer gets for referring.
  why: >-
    The author tried a lot of referral strategies and most failed until this: asking for referrals only works when you treat it like an offer, and referring is a risk to the customer's goodwill with their friend, so the benefit to them has to outweigh it.
  applies_when: >-
    Any referral programme or ask.
  anchor: >-
    Asking for referrals only works when you treat it like an
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10348–10360
  confirmations: 2
  anchor_at: "100m-leads.md:10356"
- id: B-leads-2-062
  type: rule
  name: >-
    One-Sided Referral Benefit
  statement: >-
    The incentive paid for a referral is your average cost to acquire a customer, paid either to the referrer or to the friend, and the customer is told about it.
  why: >-
    The author would rather pay customers than a platform any day of the week; the money is being spent on acquisition either way.
  applies_when: >-
    Setting up a referral incentive; also the default for spouses and households.
  anchor: >-
    of the week. Pay your average cost to acquire a customer (CAC) to the
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10401–10418
  confirmations: 1
  anchor_at: "100m-leads.md:10403"
- id: B-leads-2-063
  type: rule
  statement: >-
    What is asked for is an actual three-way introduction by call, SMS or email — not a name and a number — and it is asked for right when they buy.
  why: >-
    A salesman who simply asked who else the buyer would want to come with them and then asked to be introduced got half his sales from referrals and shattered the company's records; so simple and yet no one does it.
  applies_when: >-
    Asking a customer for a referral.
  anchor: >-
    SMS, or email. Not just a name and number. Also, ask them to do it right
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10407–10461
  confirmations: 2
  anchor_at: "100m-leads.md:10409"
- id: B-leads-2-064
  type: rule
  name: >-
    Two-Sided Referral Benefits
  statement: >-
    The CAC is split between the two parties: half to the referrer in cash or credit and half to the friend in credit.
  why: >-
    This is what Dropbox (free storage to both) and PayPal ($10 to both) used; both sides benefit, which is what made those programmes go viral.
  applies_when: >-
    Referral programmes where both sides should gain; the author's local businesses used $100 cash to the referrer and $100 off for the friend on a $500 program with a $200 CAC, good for up to three friends.
  anchor: >-
    CAC to both parties. Half goes to the referrer (in credit or cash) and
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10422–10432
  confirmations: 1
  anchor_at: "100m-leads.md:10424"
- id: B-leads-2-065
  type: rule
  statement: >-
    The referral ask is placed on the sales contract or checkout page, with the reason that they get better results doing it with a friend.
  why: >-
    Showing how they will get better results makes the ask about them; the scripted version is "People who do our program with someone else tend to get 3x the results. Who else could you do this program with?"
  applies_when: >-
    The moment of purchase.
  anchor: >-
    When They Buy:]{.calibre41}[ On the sales contract or checkout page, ask
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10440–10461
  confirmations: 1
  anchor_at: "100m-leads.md:10441"
- id: B-leads-2-066
  type: rule
  statement: >-
    A discount is given in exchange for introductions to friends rather than given away on its own.
  why: >-
    You can ethically charge a different price for the same thing because you changed the terms of the sale; and when a full-price customer finds out, the same offer is made to them — they either back off or give you three friends.
  applies_when: >-
    A prospect negotiating on price.
  anchor: >-
    referrals as a way to negotiate a lower price. In other words, if
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10469–10489
  confirmations: 1
  anchor_at: "100m-leads.md:10471"
- id: B-leads-2-067
  type: rule
  statement: >-
    A referral gift card carries an expiration date seven to fourteen days from the day it is given.
  why: >-
    The deadline forces the referrer to use it, and handing a friend a gift card gives the referrer status compared with saying "join my program for $2000 off".
  applies_when: >-
    Running a gift-card referral promotion (the card is worth about one third of the cost of the programme).
  anchor: >-
    Give the gift card an expiration date within seven to fourteen days from
  source: >-
    100m-leads.md, #1 Customer Referrals, lines 10552–10572
  confirmations: 1
  anchor_at: "100m-leads.md:10559"
- id: B-leads-2-068
  type: rule
  statement: >-
    Referral percentage and churn percentage are measured first, as a baseline, before any referral work.
  why: >-
    The two numbers are what tells you whether referrals outrun churn, which is what decides whether the business compounds.
  applies_when: >-
    Starting work on referrals.
  anchor: >-
    Figure out your referral percentages and churn percentages to set a
  source: >-
    100m-leads.md, #1 Customer Referrals, Action Items, lines 10630–10637
  confirmations: 1
  anchor_at: "100m-leads.md:10634"
- id: B-leads-2-069
  type: rule
  statement: >-
    The business is built so that other people run it, because only a business that makes money without the owner is worth something to someone else.
  why: >-
    The same $5,000,000 revenue and $2,000,000 profit is a risky job if it needs you and a valuable asset if it does not; $2,000,000 of climbing profit could easily be worth $10,000,000+ right now. You get rich from what you make; you become wealthy from what you own.
  applies_when: >-
    Judging enterprise value rather than income.
  anchor: >-
    Second, you become much wealthier because your business is now
  source: >-
    100m-leads.md, #2 Employees, Why Employees Make You Wealthy, lines 10839–10905
  confirmations: 2
  anchor_at: "100m-leads.md:10880"
- id: B-leads-2-070
  type: rule
  name: >-
    The Internal Core Four
  statement: >-
    Employees are got with the same core four used to get customers — asking your network, recruiting, posting job openings, promoting job postings — and when you need more, you do more of them.
  why: >-
    Employees are just other people you let know about your stuff, so the actions line up one for one: customer referrals become employee referrals, affiliates become associations and guilds, agencies become staffing firms.
  applies_when: >-
    Needing more lead-getting workers.
  anchor: >-
    lead getters. So when you need to get new talent, you just advertise to
  source: >-
    100m-leads.md, #2 Employees, lines 11003–11058
  confirmations: 1
  anchor_at: "100m-leads.md:11054"
- id: B-leads-2-071
  type: rule
  name: >-
    Document (the first of the 3Ds)
  statement: >-
    The job is written down as a checklist of the steps exactly as you do them, and the draft is accepted only when you can do an A+ job following your own directions exactly.
  why: >-
    You already know how to do the thing; recording yourself doing it in multiple ways lets you watch as an observer instead of breaking your flow to take notes.
  applies_when: >-
    Training an employee on a lead-getting activity.
  anchor: >-
    thing. Now you just need to write down the steps exactly as you do it.
  source: >-
    100m-leads.md, #2 Employees, lines 11086–11100
  confirmations: 1
  anchor_at: "100m-leads.md:11088"
- id: B-leads-2-072
  type: rule
  statement: >-
    The standard for a finished checklist is that a stranger following it alone would get the results you get if you vanished tomorrow.
  why: >-
    That is the level of clarity to shoot for; after the first few employees the kinks are worked out and training is smooth from there.
  applies_when: >-
    Judging whether training documentation is good enough.
  anchor: >-
    vanished tomorrow, could a stranger get the results you get if they only
  source: >-
    100m-leads.md, #2 Employees, lines 11132–11137
  confirmations: 1
  anchor_at: "100m-leads.md:11135"
- id: B-leads-2-073
  type: rule
  statement: >-
    If a step has to be explained, the step is rewritten — it is too complicated or it is several steps in one.
  why: >-
    If they get it wrong or get confused, then we got it wrong or made it confusing; an inferior checklist can be forced to work but becomes a nightmare when someone else takes over training.
  applies_when: >-
    Demonstrating or duplicating a checklist with a new employee.
  anchor: >-
    confusing.]{.calibre24}[ If we have to explain what a step means
  source: >-
    100m-leads.md, #2 Employees, lines 11145–11156
  confirmations: 1
  anchor_at: "100m-leads.md:11147"
- id: B-leads-2-074
  type: rule
  statement: >-
    When an employee knows exactly what to do but is not good at it yet, the instructions are left alone and more reps are given.
  why: >-
    There is a difference between competence and performance — slow, then smooth, then fast.
  applies_when: >-
    Diagnosing whether to fix the checklist or to keep practising.
  anchor: >-
    There is a difference between competence and performance. In other
  source: >-
    100m-leads.md, #2 Employees, lines 11158–11164
  confirmations: 1
  anchor_at: "100m-leads.md:11158"
- id: B-leads-2-075
  type: rule
  statement: >-
    Employees are judged and rewarded on their ability to follow directions rather than on getting the right result.
  why: >-
    Train employees to follow directions and they will follow directions; then if they follow directions and get the wrong result, you know it is the directions, which you have a lot more control over.
  applies_when: >-
    Training and supervising lead-getting employees.
  anchor: >-
    Focus on your employee's ability to follow directions more than
  source: >-
    100m-leads.md, #2 Employees, lines 11166–11172
  confirmations: 1
  anchor_at: "100m-leads.md:11166"
- id: B-leads-2-076
  type: rule
  statement: >-
    An employee who followed the directions exactly and still got the wrong result is praised for following them, and the checklist is corrected on the spot.
  why: >-
    Every successful step is acknowledged and mistakes are what training is for; do not take over when they mess up, pause, step back and let them try again — fast feedback cycles make people learn faster.
  applies_when: >-
    The duplicate step, when the trainee does it in front of you.
  anchor: >-
    directions. Praise them, then make the corrections to your checklist
  source: >-
    100m-leads.md, #2 Employees, lines 11174–11184
  confirmations: 1
  anchor_at: "100m-leads.md:11183"
- id: B-leads-2-077
  type: rule
  statement: >-
    No punishment or penalty of any type is used for doing things wrong during training.
  why: >-
    As a rule of thumb, reward the good stuff you want them to do more of and they will do more of it; learning a new skill is punishing enough.
  applies_when: >-
    Training.
  anchor: >-
    Avoid punishment or penalties of any type for doing stuff wrong
  source: >-
    100m-leads.md, #2 Employees, lines 11186–11189
  confirmations: 1
  anchor_at: "100m-leads.md:11186"
- id: B-leads-2-078
  type: rule
  statement: >-
    Feedback is given one step and one piece at a time, practised until right, before moving to the next step.
  why: >-
    It is hard to fix multiple things when you have never done something before.
  applies_when: >-
    Training a new employee.
  anchor: >-
    Give one piece of feedback at a time. Practice until they get
  source: >-
    100m-leads.md, #2 Employees, lines 11191–11194
  confirmations: 1
  anchor_at: "100m-leads.md:11193"
- id: B-leads-2-079
  type: rule
  statement: >-
    A major dip from normal team performance is answered by retraining the team.
  why: >-
    They stopped doing an important step in the process, often because they did not know it was important; once the step is found, people are rewarded for following it going forward.
  applies_when: >-
    Performance of an existing team drops.
  anchor: >-
    Whenever there is a major dip from normal performance, retrain the
  source: >-
    100m-leads.md, #2 Employees, lines 11196–11199
  confirmations: 1
  anchor_at: "100m-leads.md:11196"
- id: B-leads-2-080
  type: rule
  statement: >-
    The cost of advertising done by employees is measured as total payroll divided by total engaged leads, carried through to CAC and compared with LTGP.
  why: >-
    Excluding paid ad spend, the cost of outreach and content with employees is almost entirely what you pay them; $100,000 of payroll over 1000 leads is $100 per engaged lead, and at ten leads per customer that is a $1000 CAC, which against a $4000 LTGP is 4:1.
  applies_when: >-
    Employees are doing outreach, content or ads for you.
  anchor: >-
    this by just comparing how much money we spend on payroll to how much
  source: >-
    100m-leads.md, #2 Employees, lines 11209–11248
  confirmations: 1
  anchor_at: "100m-leads.md:11212"
- id: B-leads-2-081
  type: rule
  statement: >-
    For ground-level advertising jobs, anyone willing is hired and trained, and the effort goes into the training rather than into the selection.
  why: >-
    Anyone can be taught to do ground level jobs, so who you pick is not as important as how you train the ones you do; and for low level jobs you will never have a shortage of labour.
  applies_when: >-
    Hiring frontline lead-getting workers.
  anchor: >-
    pick is not as important as how you train the ones you do.
  source: >-
    100m-leads.md, #2 Employees, Conclusion, lines 11317–11353
  confirmations: 1
  authors_caveat: >-
    "Get picky when you have to make massive investments in hyper-specific-multiple-six-figure-C-suite employees."
  anchor_at: "100m-leads.md:11319"
- id: B-leads-2-082
  type: rule
  statement: >-
    Agencies are hired for two things only — learning a new method and learning a new platform — and only once there is money to pay a good one.
  why: >-
    Good agencies cost money; with no money you learn through trial and error. They have already made the big mistakes, so hiring one skips to the make-money part and buys skills you cannot learn elsewhere without spending the time that should go into scaling.
  applies_when: >-
    Considering an agency.
  anchor: >-
    suggest using agencies for two things: learning new methods and learning
  source: >-
    100m-leads.md, #3 Agencies, lines 11635–11670
  confirmations: 1
  anchor_at: "100m-leads.md:11639"
- id: B-leads-2-083
  type: rule
  statement: >-
    Every agency relationship opens with a stated purpose and a deadline: you work with them for a fixed period (six months) to learn how they do it, pay extra for them to explain the decisions, then train your team and drop to a lower-cost consulting arrangement.
  why: >-
    Being upfront gets you both better short-term results, because they know more than you, and better long-term results, because you or your team learn to do it; you also spend the maximum amount of time with their best reps. Most agencies are not opposed, and if one is, move on — but be willing to negotiate.
  applies_when: >-
    Signing with an agency.
  anchor: >-
    start every agency relationship with a purpose and a deadline to fulfill
  source: >-
    100m-leads.md, #3 Agencies, lines 11680–11745
  confirmations: 1
  anchor_at: "100m-leads.md:11683"
- id: B-leads-2-084
  type: rule
  statement: >-
    On a new platform, one good enough agency is hired to learn the ropes and a more elite one to learn how to maximise it.
  why: >-
    Learning YouTube, the author hired one agency to keep him committed and do legwork, and a second at 4x the price to teach the in-depth ideas; once their own videos beat the agency's, they dropped to consulting.
  applies_when: >-
    Entering an advertising platform you do not understand.
  anchor: >-
    to learn the ropes of a new platform. Then, I hire a more elite agency
  source: >-
    100m-leads.md, #3 Agencies, lines 11707–11720
  confirmations: 1
  anchor_at: "100m-leads.md:11718"
- id: B-leads-2-085
  type: rule
  statement: >-
    Your team and the agency run in parallel and the results are compared until your team beats theirs regularly; only then is the agency cancelled and the money moved into scaling.
  why: >-
    You only get a fraction of the agency's attention and their results get worse whenever they take on new clients, while your team gets better because they stay focused on you full-time.
  applies_when: >-
    An agency engagement entered to learn a method or platform.
  anchor: >-
    beat them. Then, cancel the relationship and put the money into scaling
  source: >-
    100m-leads.md, #3 Agencies, lines 11733–11738; Next Steps, lines 11914–11920
  confirmations: 2
  anchor_at: "100m-leads.md:11737"
- id: B-leads-2-086
  type: rule
  statement: >-
    An agency you only know about from their own paid ads or cold outreach is treated as a worse bet than one you found through word of mouth.
  why: >-
    The best agencies rely solely on word of mouth; somebody you know getting good results with them, prominent companies getting good results, and a waiting list are the signals that demand exceeds supply.
  applies_when: >-
    Shortlisting agencies.
  anchor: >-
    with them. If you only know about an agency from their paid ads or cold
  source: >-
    100m-leads.md, #3 Agencies, How to Pick The Right Agency, lines 11774–11790
  confirmations: 1
  anchor_at: "100m-leads.md:11775"
- id: B-leads-2-087
  type: rule
  statement: >-
    A cheap agency is not considered: all good agencies are expensive, though not all expensive agencies are good.
  why: >-
    Price alone does not qualify an agency, which is why the rest of the checklist exists — talk with as many as it takes and use the list as a guide.
  applies_when: >-
    Choosing an agency; also "don't be cheap" in the chapter's next steps.
  anchor: >-
    agencies are expensive... but not all expensive agencies are good. So
  source: >-
    100m-leads.md, #3 Agencies, lines 11829–11836
  confirmations: 2
  anchor_at: "100m-leads.md:11830"
- id: B-leads-2-088
  type: rule
  statement: >-
    Several more agencies are talked to and compared against the checklist even after one has agreed to your terms.
  why: >-
    Talking to a lot of agencies gives a feel for the market before a decision is made.
  applies_when: >-
    Before signing with an agency.
  anchor: >-
    with a few more before you make a decision. Compare them using the
  source: >-
    100m-leads.md, #3 Agencies, lines 11844–11846
  confirmations: 1
  anchor_at: "100m-leads.md:11845"
- id: B-leads-2-089
  type: rule
  statement: >-
    The budget allows for a stretch where the agency and your own team are paid to do the same work at the same time.
  why: >-
    You have to give yourself breathing room to get results from the agency, learn what they do, and train your team on it all at once; it costs a lot of money and is worth it when done right.
  applies_when: >-
    Making the learn-from-the-agency method work at scale.
  anchor: >-
    good amount of time where you pay the agency and your team
  source: >-
    100m-leads.md, #3 Agencies, Conclusion, lines 11866–11872
  confirmations: 1
  anchor_at: "100m-leads.md:11867"
- id: B-leads-2-090
  type: rule
  statement: >-
    A candidate affiliate qualifies when it is a business with a warm audience full of people like your customers.
  why: >-
    The list is built by answering, about your best customers, what they buy and who provides it, where they go and what businesses are nearby, what they like to do and who provides those services — in a nutshell, who's got my leads.
  applies_when: >-
    Building an affiliate hit list; the author's categories are softwares, products, equipment, services, groups they belong to, and events they attended.
  anchor: >-
    The ideal affiliate has a business with a warm audience full of people
  source: >-
    100m-leads.md, #4 Affiliates, Step 1, lines 12226–12286
  confirmations: 1
  anchor_at: "100m-leads.md:12230"
- id: B-leads-2-091
  type: rule
  statement: >-
    A business that falls into several of the affiliate categories at once is prioritised.
  why: >-
    There is a high chance they have lots of good leads for you and would make a great affiliate.
  applies_when: >-
    Sorting an affiliate hit list.
  anchor: >-
    categories, there's a high chance they've got lots of good leads for you
  source: >-
    100m-leads.md, #4 Affiliates, Step 1, lines 12264–12273
  confirmations: 1
  anchor_at: "100m-leads.md:12272"
- id: B-leads-2-092
  type: rule
  statement: >-
    What is offered to an affiliate is a fast, simple and easy new way for them to make money, not your product.
  why: >-
    Affiliates are businesses, or start one by signing up, so the offer is advertised to them exactly like any other offer — callout, value elements, call to action — with affiliates as the customer.
  applies_when: >-
    Recruiting affiliates.
  anchor: >-
    offer them a new way to make money. ]{.calibre24}[We'll start with the
  source: >-
    100m-leads.md, #4 Affiliates, Step 2, lines 12292–12364
  confirmations: 2
  anchor_at: "100m-leads.md:12301"
- id: B-leads-2-093
  type: rule
  name: >-
    Qualify Them
  statement: >-
    An affiliate is qualified by getting them to invest — their time, their money, and in the product itself.
  why: >-
    Nine times out of ten, if they pay, they'll pay attention; the terms are set up to force them to win as fast as possible.
  applies_when: >-
    Turning potential affiliates into actual ones.
  anchor: >-
    I do that by getting them to invest. I prefer they invest their time,
  source: >-
    100m-leads.md, #4 Affiliates, Step 3, lines 12379–12391
  confirmations: 1
  anchor_at: "100m-leads.md:12386"
- id: B-leads-2-094
  type: rule
  name: >-
    Make Them A Customer
  statement: >-
    Keeping affiliate status requires buying and preferably using the product.
  why: >-
    The more money an affiliate invests in your product, the more money they make; if they do not believe in your stuff enough to buy it, they probably should not sell it. This is the lowest barrier investment that has worked for the author.
  applies_when: >-
    Setting affiliate terms.
  anchor: >-
    Make them buy and preferably use the product to keep
  source: >-
    100m-leads.md, #4 Affiliates, Step 3, lines 12399–12405
  confirmations: 1
  anchor_at: "100m-leads.md:12400"
- id: B-leads-2-095
  type: rule
  name: >-
    Make Them An Expert
  statement: >-
    Affiliates pay for the onboarding and certification, priced at 10–20% of what the average active affiliate makes in the first twelve months.
  why: >-
    Too low and they are not invested, too high and you do not get enough affiliates; 10–20% maximises the number who become active. The fee also covers some advertising cost and pays for proper onboarding of every single affiliate.
  applies_when: >-
    Charging for affiliate certification; an affiliate averaging $40,000 a year is charged $4000–$8000. Figures from $100M Leads, 2023.
  anchor: >-
    How much do I charge? ]{.calibre11}[I recommend 10-20% of what the
  source: >-
    100m-leads.md, #4 Affiliates, Step 3, lines 12417–12439
  confirmations: 1
  anchor_at: "100m-leads.md:12429"
- id: B-leads-2-096
  type: rule
  statement: >-
    The affiliate commitment is lowered if not enough people start and raised if not enough people follow through.
  why: >-
    The level of required investment is calibrated against the two failure modes rather than fixed in advance; the warm reachout method of raising the minimum every five sign ups also applies.
  applies_when: >-
    Tuning affiliate entry terms.
  anchor: >-
    If you don\'t get enough people to start, lower
  source: >-
    100m-leads.md, #4 Affiliates, Step 3, lines 12443–12446
  confirmations: 1
  anchor_at: "100m-leads.md:12444"
- id: B-leads-2-097
  type: rule
  statement: >-
    Before any payout math, you decide exactly what you want the affiliate to do, and that is what you pay them for.
  why: >-
    Once that is settled, how much and how often they get paid nearly solve themselves; the author pays for new customers and repeat customers, and with better tracking for steps before the sale such as lead magnets downloaded or appointments set.
  applies_when: >-
    Designing an affiliate payout.
  anchor: >-
    Before I do any affiliate payout money math I ask myself a simple
  source: >-
    100m-leads.md, #4 Affiliates, Step 4, lines 12482–12495
  confirmations: 1
  anchor_at: "100m-leads.md:12485"
- id: B-leads-2-098
  type: rule
  statement: >-
    Affiliate pay is set from your maximum allowable cost to acquire a customer, which is what is left of gross profit after the business keeps its share of a 3:1 LTGP:CAC.
  why: >-
    On a $200 single-use product costing $40 to fulfil, $160 of gross profit at a 3:1 ratio leaves $120 to the business and $40 as the maximum payout for a new customer.
  applies_when: >-
    Deciding affiliate commissions.
  anchor: >-
    I suggest paying affiliates based on your maximum allowable cost to
  source: >-
    100m-leads.md, #4 Affiliates, Step 4, lines 12501–12512
  confirmations: 1
  anchor_at: "100m-leads.md:12501"
- id: B-leads-2-099
  type: rule
  name: >-
    Three-tier payout structure
  statement: >-
    Affiliate payouts are tiered: 25% of maximum CAC for agreeing to the terms, 50% once they activate, 100% once they sustain a level of performance.
  why: >-
    Not all affiliates are created equal; tiering doubles the reward for activating, and because the blended average payout lands below the maximum (20/20/60 across the tiers gives $30 against a $40 maximum), the ratio improves from 3:1 to 4:1 and the leftover funds contests and recruiting.
  applies_when: >-
    Any affiliate programme.
  anchor: >-
    I give it to. Not all affiliates are created equal. So, I suggest having
  source: >-
    100m-leads.md, #4 Affiliates, Step 4, lines 12516–12572
  confirmations: 1
  anchor_at: "100m-leads.md:12518"
- id: B-leads-2-100
  type: rule
  statement: >-
    All the launch work is done for the affiliates ahead of time, so that they can plug and play.
  why: >-
    Good launches have the work done ahead of time; the author has not found a better way to activate affiliates than launches.
  applies_when: >-
    Launching with affiliates.
  anchor: >-
    work done ahead of time.]{.calibre24}[ So do all the work for them.
  source: >-
    100m-leads.md, #4 Affiliates, Step 5, lines 12613–12630
  confirmations: 1
  anchor_at: "100m-leads.md:12625"
- id: B-leads-2-101
  type: rule
  name: >-
    Whisper
  statement: >-
    In the whisper phase the product stays mysterious, the posts are short, and the work behind the scenes is shown.
  why: >-
    The key to the phase is curiosity — telling them about something they want to know more about and then saying not yet; the longer something appears to take, the more an audience values it, so show your work.
  applies_when: >-
    The first phase of a launch, which can start years out.
  anchor: >-
    and hint at how big of a deal it is. Keep whispers short. And bonus
  source: >-
    100m-leads.md, #4 Affiliates, Step 5, lines 12634–12667
  confirmations: 1
  anchor_at: "100m-leads.md:12637"
- id: B-leads-2-102
  type: rule
  statement: >-
    Whispers run every four to six weeks until sixty days out, then every two to three weeks until thirty days out.
  why: >-
    The cadence tightens as the launch approaches, handing over to the tease phase at thirty days.
  applies_when: >-
    Scheduling a launch.
  anchor: >-
    until you get sixty days out. Then whisper every two to three weeks
  source: >-
    100m-leads.md, #4 Affiliates, Step 5, lines 12671–12673
  confirmations: 1
  anchor_at: "100m-leads.md:12672"
- id: B-leads-2-103
  type: rule
  name: >-
    Tease
  statement: >-
    Teasing — revealing the product, making the launch date public and showing the elements of value with the What-Who-When framework — runs once per week until fourteen days out, then twice per week until three days out.
  why: >-
    The tease phase satisfies the curiosity built in the whisper phase, which is why it carries the hard information and the value elements.
  applies_when: >-
    The middle phase of a launch.
  anchor: >-
    days out. Then tease twice per week until three days out. Three days
  source: >-
    100m-leads.md, #4 Affiliates, Step 5, lines 12681–12701
  confirmations: 1
  anchor_at: "100m-leads.md:12700"
- id: B-leads-2-104
  type: rule
  name: >-
    Shout
  statement: >-
    Shouting — specific calls to action with bonuses, scarcity, urgency and guarantees — runs at least twice a day from three days out, every few hours on the day, and every thirty minutes in the last two hours.
  why: >-
    The shout phase is the call to action: you shout to get as many people exposed to the offer as you can while it is live.
  applies_when: >-
    The last three days of a launch.
  anchor: >-
    days out. On the day of, start shouting every few hours until two hours
  source: >-
    100m-leads.md, #4 Affiliates, Step 5, lines 12709–12727
  confirmations: 1
  anchor_at: "100m-leads.md:12725"
- id: B-leads-2-105
  type: rule
  statement: >-
    The affiliate keeps all the cash from selling a lead magnet that you fulfil.
  why: >-
    It becomes all profit and no work for them, an attractive proposition for any business; your money comes from selling your main thing for more than the lead magnet cost to deliver, and you do not split anything on the core offer. If you give the affiliate all the money, they want to do it more and send even more leads.
  applies_when: >-
    Integration strategy 2, affiliates selling your lead magnet.
  anchor: >-
    sample product, etc. Also, giving affiliates all the cash from selling a
  source: >-
    100m-leads.md, #4 Affiliates, Step 6, lines 12836–12859; case study, lines 13019–13028
  confirmations: 3
  anchor_at: "100m-leads.md:12839"
- id: B-leads-2-106
  type: rule
  statement: >-
    Affiliate payouts are paid for as long as the customer stays and are never capped.
  why: >-
    Paying forever keeps affiliates motivated to keep your customers forever.
  applies_when: >-
    Splitting money with affiliates on your core offer.
  anchor: >-
    forever so my affiliates stay motivated to keep my customers forever.
  source: >-
    100m-leads.md, #4 Affiliates, Step 6, lines 12868–12871
  confirmations: 1
  anchor_at: "100m-leads.md:12870"
- id: B-leads-2-107
  type: rule
  statement: >-
    Affiliates are treated like customers, and the offer is made to make sense for their business.
  why: >-
    How much value affiliates get from you determines how much they advertise your stuff; integration is the long-term strategy for enduring lead flow, and you are only as good as the goodwill you have with your affiliate partners.
  applies_when: >-
    Keeping affiliates advertising after the launch.
  anchor: >-
    using affiliates to get enduring lead flow. Treat affiliates like
  source: >-
    100m-leads.md, #4 Affiliates, Step 6, lines 12592–12595, 12908–12911, 13188–13194
  confirmations: 3
  anchor_at: "100m-leads.md:12909"
- id: B-leads-2-108
  type: rule
  statement: >-
    Integration is set up as one of three arrangements: the affiliate gives your lead magnet away with their purchase, sells your lead magnet, or sells your core offer directly.
  why: >-
    The three are ordered easiest to hardest; giving the lead magnet away makes the affiliate's own offer more valuable at no extra cost, and you upsell your core offer from there.
  applies_when: >-
    Turning an activated affiliate into a long-term lead source.
  anchor: >-
    whether you want them to give your lead magnet away, to sell your lead
  source: >-
    100m-leads.md, #4 Affiliates, Step 6, lines 12756–12917
  confirmations: 1
  anchor_at: "100m-leads.md:12916"
- id: B-leads-2-109
  type: rule
  statement: >-
    Affiliate returns are measured by comparing the cost to get an affiliate with the gross profit of all the customers that affiliate sends, not with money made from the affiliate.
  why: >-
    You spend money to get affiliates but make little back from affiliates themselves; the money comes back from the customers they bring. A $4000 affiliate CAC against $54,000 of leftover gross profit is 12.5:1.
  applies_when: >-
    Calculating returns on an affiliate programme.
  anchor: >-
    compare how much it costs us to get an affiliate with the gross profit
  source: >-
    100m-leads.md, #4 Affiliates, Costs and Returns, lines 13066–13138
  confirmations: 1
  anchor_at: "100m-leads.md:13074"
- id: B-leads-2-110
  type: rule
  statement: >-
    An affiliate programme is expected to run at least 3:1 LTGP to CAC, and is aimed higher — 5:1 or 10:1 and up.
  why: >-
    Below 3:1 there are three ways to fix it: lower CAC with better ads, offer and sales process; get more affiliates to activate with a launch process; make each affiliate worth more with a better integration process.
  applies_when: >-
    Judging an affiliate programme. Benchmark from $100M Leads, 2023.
  anchor: >-
    least]{.calibre24}[ at 3:1 to have a decent business. Like the example,
  source: >-
    100m-leads.md, #4 Affiliates, Costs and Returns, lines 13144–13165
  confirmations: 1
  anchor_at: "100m-leads.md:13145"
- id: B-leads-2-111
  type: rule
  statement: >-
    The affiliate offer is advertised until there are ten to twenty affiliates, whose results and feedback are used to fix the offer, terms, launches and integration before scaling.
  why: >-
    Their results then become the first batch of affiliate lead magnets used to scale.
  applies_when: >-
    Starting an affiliate programme.
  anchor: >-
    Advertise your affiliate offer until you get ten to twenty affiliates.
  source: >-
    100m-leads.md, #4 Affiliates, Action Steps, lines 13233–13237
  confirmations: 1
  anchor_at: "100m-leads.md:13233"
- id: B-leads-2-112
  type: rule
  statement: >-
    A chosen lead source is not abandoned after a few losses; three to six months is the expected time to crack a new one.
  why: >-
    It is normal to lose in the beginning, and the author expects three to six months to crack a new lead source and this is not his first rodeo; people try shortcuts for a decade until they realise they should have picked a strategy and stuck with it for a decade.
  applies_when: >-
    Judging whether a lead source has failed.
  anchor: >-
    in three to six months (and this isn't my first rodeo). So if your
  source: >-
    100m-leads.md, Section IV Conclusion, lines 13306–13320
  confirmations: 1
  anchor_at: "100m-leads.md:13318"
- id: B-leads-2-113
  type: rule
  statement: >-
    Some percentage of the advertising budget — 1%, 5% or 10% — is set aside for new campaigns, channels, pages and plain crazy ideas, with no return expected.
  why: >-
    You learn something every time you test, so the money is well spent; when one of the tests wins, and some do, you make far more than you spent. Consider it an investment in your education.
  applies_when: >-
    An established advertising budget. Attributed in the book to a speaker at a private entrepreneurs' event, not to the author.
  anchor: >-
    business and, more importantly, myself. So whether it\'s 1%, 5%, or 10%,
  source: >-
    100m-leads.md, Section V: Get Started, lines 13466–13476
  confirmations: 1
  anchor_at: "100m-leads.md:13473"
- id: B-leads-2-114
  type: rule
  statement: >-
    A test is run at a volume where the expected response rate produces a countable number of responses — 5,000 flyers, not 300.
  why: >-
    At half a percent (decent) or one percent (a winner), 300 flyers would produce one and a half people, which makes it impossible to tell a winner from a loser; and when a winner is found it goes out 5,000 per day, every day, for a month.
  applies_when: >-
    Testing an advertising channel; response benchmarks are for flyers.
  anchor: >-
    a small number...I test with 5000. Then when we find a winner, we put
  source: >-
    100m-leads.md, Advertising in Real Life, lines 13679–13757
  confirmations: 2
  anchor_at: "100m-leads.md:13696"
- id: B-leads-2-115
  type: rule
  name: >-
    Open To Goal
  statement: >-
    You commit to working until a specific number of outcomes is hit that day, no matter what, rather than to a fixed number of actions or hours.
  why: >-
    It is the rule of 100 for the big kids: it unlocks a level of effort you did not realise you had, and it may mean fifty attempts or five thousand every day for years. Give up the idea of doing your best and do what is required.
  applies_when: >-
    Once the rule of 100 has become normal; the gym chain's sales managers signed up five new members a day, leaving early if done by lunch and working eighteen hours if not.
  anchor: >-
    a specific number of times... you commit to the work until you hit a
  source: >-
    100m-leads.md, Advertising in Real Life, lines 13776–13804
  confirmations: 2
  anchor_at: "100m-leads.md:13792"
- id: B-leads-2-116
  type: rule
  statement: >-
    The daily advertising goal is done in one uninterrupted block at the start of the day, before fires, people and day-to-day work.
  why: >-
    The magic is not in waking early but in a long stretch of uninterrupted work immediately after a long stretch of uninterrupted sleep — the most productive hours in a row of the most productive work, every single day.
  applies_when: >-
    Structuring a day to make open to goal possible; the author's stack is waking at 4–5 am, getting right to work with no rituals, and no meetings until noon.
  anchor: >-
    goal accordingly. Then, only after my dedicated block of work--do I go
  source: >-
    100m-leads.md, Advertising in Real Life, lines 13818–13860
  confirmations: 1
  anchor_at: "100m-leads.md:13848"
- id: B-leads-2-117
  type: rule
  name: >-
    One Page Advertising Checklist
  statement: >-
    The daily advertising action is done by you until there is enough money to pay someone else to do it.
  why: >-
    That is the point at which the plan restarts with employees as the target lead type.
  applies_when: >-
    Running the one page advertising checklist.
  anchor: >-
    Do this daily action until you have enough money
  source: >-
    100m-leads.md, Advertising in Real Life, lines 13914–13915
  confirmations: 1
  anchor_at: "100m-leads.md:13914"
- id: B-leads-2-118
  type: rule
  statement: >-
    Once you can afford help, the checklist is run again from step one with employees as the new target lead type, and repeated until you have the help you need.
  why: >-
    The same five steps that get customers get the people who then get customers, and then you scale again.
  applies_when: >-
    You can afford to pay someone to do the daily advertising action.
  anchor: >-
    When you do, go back to step 1. Make employees
  source: >-
    100m-leads.md, Advertising in Real Life, lines 13919–13921
  confirmations: 1
  anchor_at: "100m-leads.md:13919"
- id: B-leads-2-119
  type: rule
  statement: >-
    The advertising plan fits on a single page and is filled out in about five minutes.
  why: >-
    A hundred-page plan never gets used; a single page leaves little room for excuses, distractions and delusions — you either did the stuff or you did not.
  applies_when: >-
    Planning advertising.
  anchor: >-
    pages of baloney. Harness the power of laying out your action steps on a
  source: >-
    100m-leads.md, Advertising in Real Life, Conclusion, lines 13954–13961
  confirmations: 1
  anchor_at: "100m-leads.md:13956"
- id: B-leads-2-120
  type: rule
  name: >-
    Level 1
  statement: >-
    At the start you make one offer, to one avatar, on one platform, with warm outreach as the primary action.
  why: >-
    The moment you get engaged leads is the moment you can start making money.
  applies_when: >-
    The first level of the advertising roadmap.
  anchor: >-
    make one offer, to one avatar, on one platform. The moment you get
  source: >-
    100m-leads.md, The Roadmap, lines 14006–14015
  confirmations: 1
  anchor_at: "100m-leads.md:14008"
- id: B-leads-2-121
  type: rule
  name: >-
    Level 3
  statement: >-
    People are hired to advertise on your behalf when your personal advertising inputs are maxed out but the platform is not.
  why: >-
    If you want more engaged leads at that point it can only mean doing more, and the doing has to come from someone else; the author hired a videographer and a media buyer to take the paid ads work off his plate.
  applies_when: >-
    The third level of the advertising roadmap.
  anchor: >-
    help you do more advertising.]{.calibre24}[ You've maxed your personal
  source: >-
    100m-leads.md, The Roadmap, lines 14039–14049
  confirmations: 1
  anchor_at: "100m-leads.md:14040"
- id: B-leads-2-122
  type: rule
  name: >-
    Level 4
  statement: >-
    Before ramping advertising again, the product is worked on until at least 25% of customers come from referrals.
  why: >-
    This is where most people mess up: they let their product slip and never recover. At the $100M machine level the product is so good that a third of customers bring more customers.
  applies_when: >-
    The fourth level of the advertising roadmap; the author doubled down on referrals after noticing that his ads were off and referrals kept coming, updating the product from customer feedback every two weeks and running a strong referral programme.
  anchor: >-
    shoot for getting 25% or more of your customers from referrals. Now,
  source: >-
    100m-leads.md, The Roadmap, lines 14053–14073, 14189–14190
  confirmations: 2
  anchor_at: "100m-leads.md:14055"
- id: B-leads-2-123
  type: rule
  name: >-
    Level 5
  statement: >-
    On the best platform you first expand to new audiences, then use every placement and media type the platform supports, and only after the team gets consistent results add another platform, lead getter or core four activity.
  why: >-
    This is the roadmap order for more, better and new applied with a team rather than alone.
  applies_when: >-
    The fifth level of the advertising roadmap.
  anchor: >-
    platform. Then, you make ads with all placements and media types the
  source: >-
    100m-leads.md, The Roadmap, lines 14077–14094
  confirmations: 1
  anchor_at: "100m-leads.md:14080"
- id: B-leads-2-124
  type: rule
  name: >-
    Level 6
  statement: >-
    At the executive level you hire experienced leaders specialising in exactly the advertising method or platform you want, not people with potential.
  why: >-
    The author's companies capped here; it took three years to learn that he needed veteran executives suited to his problems and that they needed stronger incentives, and expanding the pie to get the right people invested in winning is how Acquisition.com crossed $100M and $200M in portfolio revenue.
  applies_when: >-
    The sixth level of the advertising roadmap.
  anchor: >-
    advertising method or platform without you. And you\'re not looking for
  source: >-
    100m-leads.md, The Roadmap, lines 14098–14118
  confirmations: 1
  anchor_at: "100m-leads.md:14100"
```
