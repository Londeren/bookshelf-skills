# Улов фазы 1 — $100M Leads (2023), chapters up to #3 Cold Outreach (lines 1–6900) (ярус 1), тип D: антипаттерны и границы

Группа `tier1-leads-1`, слаг `leads-1`, ярус 1. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **63** (экстрактор вернул 63, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-leads.md` | 1–6900 | 6 | 63 |

## Как собран файл

Экстрактор D (Antipatterns and boundaries) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier1-leads-1.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier1-leads-1-D.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: D-leads-1-001
  type: rule
  name: >-
    Leads sit on top of an offer
  statement: >-
    The lead-getting method starts from an offer that already exists; it does not tell you what to sell.
  why: >-
    All the pieces are needed to make money: the stuff to sell (an offer), the people to sell it to (leads), then sales. Leads are the problem that appears once you already have something to sell.
  boundary: >-
    The book assumes the reader already has a Grand Slam Offer to sell; the question What should I sell? belongs to the previous book, not to this method.
  anchor: >-
    Offers]{.calibre24}[. It assumes you already have a
  source: >-
    100m-leads.md, Section I: Start Here, line 279
  confirmations: 1
  anchor_at: "100m-leads.md:279"
- id: D-leads-1-002
  type: antipattern
  name: >-
    Masters never don't do the basics
  statement: >-
    Operators who already have skills and money stop doing the basic advertising activities that got them to their current level.
  why: >-
    Respecting the tried-and-true methods that got you to your current level will probably get you to the next one; the businesses of people who drop them deserve better.
  anchor: >-
    and money, me included, of the basics we stopped doing.
  source: >-
    100m-leads.md, The Problem This Book Solves, line 1413
  confirmations: 2
  anchor_at: "100m-leads.md:1413"
- id: D-leads-1-003
  type: rule
  name: >-
    Try the core offer first
  statement: >-
    Advertise the core offer first and only add a lead magnet if people need to know more before they buy.
  why: >-
    Advertising the core offer goes straight for the sale, the direct path to money, and it might be all you need to get leads to engage.
  boundary: >-
    A lead magnet is for the case where people want to know more about the offer before they buy, which the author says is common for businesses that sell more expensive stuff.
  anchor: >-
    all you need to get leads to engage. Try this way first.
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, line 1850
  confirmations: 1
  anchor_at: "100m-leads.md:1850"
- id: D-leads-1-004
  type: rule
  name: >-
    Reveal Their Problem
  statement: >-
    A diagnosis-type lead magnet is used where the problem it reveals gets worse the longer the prospect waits.
  why: >-
    The revealed problem has to create its own pressure to move; the author draws a clear line between where the prospect is and what the delay costs them.
  boundary: >-
    Works great when the problem revealed gets worse the longer you wait.
  anchor: >-
    Think "diagnosis." These lead magnets work great when they reveal
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, line 2040
  confirmations: 1
  anchor_at: "100m-leads.md:2040"
- id: D-leads-1-005
  type: rule
  name: >-
    Samples And Trials
  statement: >-
    A sample or trial as a lead magnet is used where the core offer is a recurring solution to a recurring problem.
  why: >-
    Full but brief access ends, and the recurring problem comes back, so the prospect has to keep paying to keep the result.
  boundary: >-
    Works great when your core offer is a recurring solution to a recurring problem.
  anchor: >-
    of uses, time they have access, or both. This works great when your core
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, line 2068
  confirmations: 1
  anchor_at: "100m-leads.md:2068"
- id: D-leads-1-006
  type: rule
  name: >-
    One Step Of A Multi-Step Process
  statement: >-
    Giving one free step of a multi-step process is used where the core offer solves a more complex problem.
  why: >-
    One valuable step solves part of the problem and makes the remaining steps, and the effort they take, obvious.
  boundary: >-
    Works great when your core offer solves a more complex problem, and requires a core offer that has steps.
  anchor: >-
    valuable step for free and the rest when they buy. This works great when
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, line 2097
  confirmations: 1
  anchor_at: "100m-leads.md:2097"
- id: D-leads-1-007
  type: antipattern
  name: >-
    Leaving the packaging to chance
  statement: >-
    Making a good lead magnet and then not testing its headline, name and display.
  why: >-
    Leads have to notice the lead magnet before they can consume it, so if no one shows interest in it, no one will ever know how good it is; improving the headline, name and display can 2x, 3x or 10x engagement.
  anchor: >-
    will ever know how good it is. You can't leave it to chance. So listen
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, line 2230
  confirmations: 1
  anchor_at: "100m-leads.md:2230"
- id: D-leads-1-008
  type: rule
  name: >-
    A raised hand is where this book ends
  statement: >-
    The method ends when a stranger shows interest; getting them to actually buy is a different discipline.
  why: >-
    Getting strangers to buy is sales, not getting leads; the point is to get strangers to show interest, not to buy yet.
  boundary: >-
    Out of scope: persuading the interested lead to purchase. The author names that as sales, a separate future book.
  anchor: >-
    that's sales, not getting leads. The point of this book is to get
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, line 2351
  confirmations: 1
  anchor_at: "100m-leads.md:2351"
- id: D-leads-1-009
  type: antipattern
  name: >-
    One format only
  statement: >-
    Publishing a lead magnet in a single format.
  why: >-
    People consume in different ways, so a single format misses the 3-4x of people who would have taken it in another one; multiple formats is the easiest way the author knows to get 2-3-4x the leads for the same work.
  anchor: >-
    the same work. If I only made it available in one format, I'd miss out
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, line 2437
  confirmations: 1
  anchor_at: "100m-leads.md:2437"
- id: D-leads-1-010
  type: antipattern
  name: >-
    Sucky fluff
  statement: >-
    Holding back the secrets and giving away thin filler as the free thing because giving away the real content feels dangerous.
  why: >-
    People who might have become customers conclude this person sucks, buy from someone else, and tell other people who might have bought not to; the author calls it a vicious cycle.
  applies_when: >-
    The fix the author states: give away the secrets and sell the implementation; make the lead magnet provide more value than the cost of the core offer, and as good as the paid stuff.
  anchor: >-
    imagine the alternative: You give away sucky fluff. Then, people who
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, line 2463
  confirmations: 2
  anchor_at: "100m-leads.md:2463"
- id: D-leads-1-011
  type: rule
  name: >-
    The catch in scarcity
  statement: >-
    Scarcity raises perceived value but caps how many engaged leads can be collected before the scarce thing runs out.
  why: >-
    The fewer you have, the more valuable people think it is, and the fewer engaged leads you can get before running out.
  boundary: >-
    Scarcity trades lead volume for perceived value; it cannot be used to maximise both at once.
  anchor: >-
    catch- the fewer you have, the fewer engaged leads you can get before
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, line 2538
  confirmations: 1
  anchor_at: "100m-leads.md:2538"
- id: D-leads-1-012
  type: rule
  name: >-
    Ethical scarcity
  statement: >-
    The scarcity used in a call to action is the real limit of the business (customer service, onboarding, inventory, time slots), advertised rather than kept quiet.
  why: >-
    The best strategy for scarcity is reality: every business has some limit to how much it can sell, and drawing attention to the natural limit makes money from it.
  boundary: >-
    The author's limit on the tactic is that the scarcity must be a real constraint of the business; that is what makes it ethical scarcity.
  anchor: >-
    per week, etc. Don't keep it a secret - advertise it. This gives you
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, line 2544
  confirmations: 1
  anchor_at: "100m-leads.md:2544"
- id: D-leads-1-013
  type: antipattern
  name: >-
    Don't be clever, be clear
  statement: >-
    Writing a clever or indirect call to action instead of a clear, simple, action-oriented one.
  why: >-
    Good CTAs use clear, simple and direct language; the author contrasts don't delay with call now.
  anchor: >-
    reasons you can think of. And, do it often. Don\'t be clever, be clear.
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, line 2632
  confirmations: 2
  anchor_at: "100m-leads.md:2632"
- id: D-leads-1-014
  type: antipattern
  name: >-
    Confusing automation with one-to-many
  statement: >-
    Treating an automated blast as one-to-many communication because a machine sends it.
  why: >-
    Automation only means some of the work is done by machines; the nature of the communication stays the same, so emailing a 10,000 person list once is one-to-one really fast, not a public post.
  anchor: >-
    confusing. Don't let it. Automation just means some of the work is done
  source: >-
    100m-leads.md, Section III: Get Leads, line 2854
  confirmations: 1
  anchor_at: "100m-leads.md:2854"
- id: D-leads-1-015
  type: antipattern
  name: >-
    Blaming anything but skill and volume
  statement: >-
    Explaining a shortage of leads by anything other than not doing the core four with enough skill or enough volume.
  why: >-
    The core four are the only four things you can do to let other people know about the stuff you sell; the author states flatly that you are not getting as many leads as you want because you are not advertising enough.
  anchor: >-
    So if you aren't getting as many leads as you want, you're not doing
  source: >-
    100m-leads.md, Section III: Get Leads, line 2907
  confirmations: 2
  anchor_at: "100m-leads.md:2907"
- id: D-leads-1-016
  type: antipattern
  name: >-
    Skipping warm outreach
  statement: >-
    Not making one-to-one contact with the people who already know you, which is what most businesses do.
  why: >-
    It is the cheapest and easiest way to find people interested in the stuff you sell, and it is super effective; the author's instruction is not to be like most businesses.
  anchor: >-
    effective--and most businesses don't do it. Don't be like most
  source: >-
    100m-leads.md, #1 Warm Outreach, line 3085
  confirmations: 1
  anchor_at: "100m-leads.md:3085"
- id: D-leads-1-017
  type: rule
  name: >-
    Warm outreach is for the first five clients
  statement: >-
    Warm reach outs are the method for getting the first five clients for any new product or service, and for re-engagement and new product lines once you are established.
  why: >-
    You do everything yourself and personalise each message, so the yield per hour is low but reliable.
  boundary: >-
    Positioned for a new product or service, and for advanced operators as re-engagement and new product lines; it is not the channel you scale on.
  anchor: >-
    Warm reach outs are a fantastic way to get your "First Five Clients"
  source: >-
    100m-leads.md, #1 Warm Outreach, line 3121
  confirmations: 1
  anchor_at: "100m-leads.md:3121"
- id: D-leads-1-018
  type: antipattern
  name: >-
    I don't have any leads
  statement: >-
    Believing you have no list to start from.
  why: >-
    Every contact in your phone, every email account you have used and every social profile is a list of people who gave you the means and permission to contact them; for many people that is their first 1000 leads.
  anchor: >-
    leads. Would ya look at that! "I don't have any leads." Psh. Just found
  source: >-
    100m-leads.md, #1 Warm Outreach, line 3201
  confirmations: 1
  anchor_at: "100m-leads.md:3201"
- id: D-leads-1-019
  type: antipattern
  name: >-
    Don't be a weirdo
  statement: >-
    Opening a warm reach out with the ask instead of a personalised greeting that pays your social dues.
  why: >-
    At that point you haven't asked for anything, you are just checking in and providing value; the greeting uses something you actually know about the contact as the reason to reach out.
  anchor: >-
    Don't be a weirdo. Pay your social dues. Remember, you haven't asked
  source: >-
    100m-leads.md, #1 Warm Outreach, line 3237
  confirmations: 1
  anchor_at: "100m-leads.md:3237"
- id: D-leads-1-020
  type: rule
  name: >-
    Without lying or exaggerating
  statement: >-
    The offer is pushed as close as possible to the ideal of the value equation, but never by lying or exaggerating.
  why: >-
    The ideal is exactly what they want, guaranteed, insanely fast, without lifting a finger; the author states you must get as close to that as you can within the truth.
  boundary: >-
    The author's own limit on maximising the value equation in the script: no lying, no exaggerating.
  anchor: >-
    that as we can without lying or exaggerating.
  source: >-
    100m-leads.md, #1 Warm Outreach, line 3416
  confirmations: 1
  anchor_at: "100m-leads.md:3416"
- id: D-leads-1-021
  type: antipattern
  name: >-
    Trying to look advanced
  statement: >-
    Dressing up a beginner offer to look advanced instead of being honest and keeping it simple.
  why: >-
    People aren't dumb; the honest version, which sets expectations up front, is what makes the free offer easy to say yes to.
  anchor: >-
    And don't try to look advanced if you're not.
  source: >-
    100m-leads.md, #1 Warm Outreach, line 3508
  confirmations: 1
  anchor_at: "100m-leads.md:3508"
- id: D-leads-1-022
  type: antipattern
  name: >-
    Free stuff that is too expensive
  statement: >-
    Concluding nothing is wrong when people decline even the free offer, instead of diagnosing which part of the value equation failed.
  why: >-
    If you struggle to give your stuff away for free, either people don't want it (dream outcome), they don't believe you (perceived likelihood of achievement), or the hidden costs of time, effort and sacrifice are too high; in short, your free stuff is too expensive.
  applies_when: >-
    The author's fix: when someone says no, ask why, using What would I have to do to make it worth it for you to continue?
  anchor: >-
    free, it means either people don't want it (dream outcome), they don't
  source: >-
    100m-leads.md, #1 Warm Outreach, line 3601
  confirmations: 1
  anchor_at: "100m-leads.md:3601"
- id: D-leads-1-023
  type: rule
  name: >-
    Once people start referring, start charging
  statement: >-
    You keep working for free until the free clients start referring people; referrals are the signal to start charging.
  why: >-
    The author calls it the litmus test for being good enough to charge; before that you probably suck, and people are far more forgiving when you haven't charged anything.
  boundary: >-
    A precondition on price: do not start charging before referrals appear, and then raise by roughly 20% every five clients.
  anchor: >-
    enough" to charge. ]{.calibre3}[Once people start referring, start
  source: >-
    100m-leads.md, #1 Warm Outreach, line 3689
  confirmations: 1
  anchor_at: "100m-leads.md:3689"
- id: D-leads-1-024
  type: rule
  name: >-
    The two limitations of warm reach outs
  statement: >-
    Warm outreach is limited by your time and by the number of people who know you, and you will eventually run out of contacts.
  why: >-
    You do everything on your own and make each message personal, so you don't get many engaged leads for the time you invest; the list itself is finite.
  boundary: >-
    Warm outreach cannot be scaled past the size of your warm audience; the author moves to posting free content, then cold outreach, precisely because of this ceiling.
  anchor: >-
    The second limiter is the number of people who know you.
  source: >-
    100m-leads.md, #1 Warm Outreach, line 3881
  confirmations: 2
  anchor_at: "100m-leads.md:3881"
- id: D-leads-1-025
  type: antipattern
  name: >-
    Explaining away someone who makes more than you
  statement: >-
    Writing off a competitor or peer who makes more money as lucky, as having rich parents, as having a shortcut or as having broken some moral code.
  why: >-
    If someone is making more money than you, they are better at the game of business in some way, which means you can learn from them; none of the dismissive beliefs serve you or make you better. The author lost a year to this over content.
  anchor: >-
    can learn from them. Don't think they had it easy. Don't think they had
  source: >-
    100m-leads.md, #2 Post Free Content Part I, line 4067
  confirmations: 3
  anchor_at: "100m-leads.md:4067"
- id: D-leads-1-026
  type: antipattern
  name: >-
    Content disappears so it's a waste
  statement: >-
    Refusing to make content on the grounds that a post disappears in a few days.
  why: >-
    The content is not the compounding asset, the audience is; the content may disappear but the audience keeps growing. The author calls building an audience the most valuable thing he has ever done.
  anchor: >-
    Why would I waste my time making something that would disappear in a few
  source: >-
    100m-leads.md, #2 Post Free Content Part I, line 4075
  confirmations: 1
  anchor_at: "100m-leads.md:4075"
- id: D-leads-1-027
  type: antipattern
  name: >-
    Looking for the content secret
  statement: >-
    Hunting for a blueprint or secret to personal branding instead of putting out more content.
  why: >-
    Anyone telling you there's some secret is trying to sell you something; the influencer's answer was that he simply puts out as much as he possibly can. When the author put out ten times the content, his audience grew ten times as fast.
  anchor: >-
    Bro, anyone telling you there's some secret is trying to sell
  source: >-
    100m-leads.md, #2 Post Free Content Part I, line 4112
  confirmations: 1
  anchor_at: "100m-leads.md:4112"
- id: D-leads-1-028
  type: rule
  name: >-
    The trade-offs of posting free content
  statement: >-
    Posting free content costs you personalisation, forces you to compete with everyone else posting, and gets you copied once you stand out.
  why: >-
    It is harder to personalise the message so fewer people respond; standing out among everyone else posting is harder; and being copied means you have to constantly innovate.
  boundary: >-
    The author states these as the three trade-offs of the channel: it is not all sunshine and rainbows, and it is less predictable than warm reach outs.
  anchor: >-
    But, posting free content is not all sunshine and rainbows. It has
  source: >-
    100m-leads.md, #2 Post Free Content Part I, line 4185
  confirmations: 2
  anchor_at: "100m-leads.md:4185"
- id: D-leads-1-029
  type: antipattern
  name: >-
    A hook the content does not pay off
  statement: >-
    Promising something in the hook and then delivering less, delivering something stale, or delivering it to an audience that cannot use it.
  why: >-
    You did a bad job of rewarding: people will not want to watch again and certainly won't share it. The audience decides how good the content is, and the proof is whether your audience grows.
  anchor: >-
    Use" and they can't use them, they will not share it or watch your
  source: >-
    100m-leads.md, #2 Post Free Content Part I, line 4717
  confirmations: 2
  anchor_at: "100m-leads.md:4717"
- id: D-leads-1-030
  type: rule
  name: >-
    Asking costs growth
  statement: >-
    Every ask made to an audience is paid for in slower growth, so the ask is postponed as long as possible.
  why: >-
    The moment you start asking for money is the moment you decide to slow down your growth; the more patient you are, the more you get when you finally make the ask. You also pay in potential loss of trust.
  boundary: >-
    The author's preferred strategy is give until they ask: give in public, ask in private, and let the audience self-select when they are ready. Asking is presented as the concession you make when you need money now.
  anchor: >-
    moment you decide to slow down your growth. So the more patient you are,
  source: >-
    100m-leads.md, #2 Post Free Content Part II, line 4908
  confirmations: 2
  anchor_at: "100m-leads.md:4908"
- id: D-leads-1-031
  type: antipattern
  name: >-
    Killing the golden goose
  statement: >-
    Monetising a new audience by making offers too frequently inside the content.
  why: >-
    The author's friend's podcast not only stopped growing, it actually shrank; the goodwill of the audience is the most valuable asset and over-giving is what protects it.
  applies_when: >-
    You can advertise in every piece of content so long as you keep your give : ask ratio high; the author's reference points are roughly 3.5:1 on television and 4:1 on Facebook, which are what mature platforms do to maximally monetise rather than grow.
  anchor: >-
    podcast not only stopped growing, it actually shrank! Don't be like
  source: >-
    100m-leads.md, #2 Post Free Content Part II, line 4970
  confirmations: 1
  anchor_at: "100m-leads.md:4970"
- id: D-leads-1-032
  type: rule
  name: >-
    Integrated or intermittent depends on the platform
  statement: >-
    Which way you weave the ask into content is decided by the platform, not by preference: intermittent asks on short platforms, integrations on long-form ones.
  why: >-
    The author states the difference between the two ways depends on the platform; on short platforms the intermittent way will dominate.
  boundary: >-
    Platform-dependent: an integrated ask is the best bet only on long-form platforms.
  anchor: >-
    platform. On short platforms, the intermittent way will dominate. On
  source: >-
    100m-leads.md, #2 Post Free Content Part II, line 5000
  confirmations: 1
  anchor_at: "100m-leads.md:5000"
- id: D-leads-1-033
  type: antipattern
  name: >-
    Relying on a single channel
  statement: >-
    Maximising one platform to the point where the business depends on it alone.
  why: >-
    Platforms change all the time and sometimes ban you for no reason; if you only have one way to get customers, it can kill your business if it gets shut down. This is the stated disadvantage of the depth-then-width approach.
  anchor: >-
    on a single channel. This is a risk because platforms change all the
  source: >-
    100m-leads.md, #2 Post Free Content Part II, line 5119
  confirmations: 1
  anchor_at: "100m-leads.md:5119"
- id: D-leads-1-034
  type: antipattern
  name: >-
    Bad content everywhere
  statement: >-
    Spreading onto every platform at once and ending up with lots of bad content in all of them.
  why: >-
    It costs more labor, attention and time to do width-then-depth well; oftentimes people end up with lots of bad content everywhere, which the author calls sucky fluff.
  anchor: >-
    to do this well. Oftentimes, people end up with lots of bad content
  source: >-
    100m-leads.md, #2 Post Free Content Part II, line 5167
  confirmations: 1
  anchor_at: "100m-leads.md:5167"
- id: D-leads-1-035
  type: antipattern
  name: >-
    Giving paid ads all the credit
  statement: >-
    Attributing results to paid advertising and dropping the free content that was nurturing the demand.
  why: >-
    When paid ads stopped working, the thing that had changed was that the author stopped making content for his market; a survey showed 78% of clients had consumed at least two long form pieces of content before booking a call. Free content improves the returns of every other advertising method, even when it is hard to measure.
  anchor: >-
    I had fallen into my old ways and given paid ads all the credit.
  source: >-
    100m-leads.md, #2 Post Free Content Part II, line 5234
  confirmations: 1
  anchor_at: "100m-leads.md:5234"
- id: D-leads-1-036
  type: antipattern
  name: >-
    How to instead of How I
  statement: >-
    Telling the audience what they should do and what the best way is, instead of what you did and what your favorite ways are.
  why: >-
    When you tell a stranger what to do it's hard to avoid coming off preachy or arrogant; when you talk about your own experience no one can question you, which the author calls bulletproof.
  applies_when: >-
    The author flags this especially when starting out.
  anchor: >-
    When you tell a stranger what to do, it\'s hard to avoid coming off
  source: >-
    100m-leads.md, #2 Post Free Content Part II, line 5275
  confirmations: 1
  anchor_at: "100m-leads.md:5275"
- id: D-leads-1-037
  type: antipattern
  name: >-
    We Need To Be Reminded More Than We Need To Be Taught
  statement: >-
    Assuming your audience has already heard something and moving on instead of repeating it.
  why: >-
    You are a silly goose if you think 100 percent of your audience listens 100 percent of the time: the author posts about his book daily and one in five people who saw the post did not know he had one. You will get bored of your content before your whole audience even sees it.
  anchor: >-
    five that saw the post said they didn't know. Keep repeating yourself.
  source: >-
    100m-leads.md, #2 Post Free Content Part II, line 5284
  confirmations: 2
  anchor_at: "100m-leads.md:5284"
- id: D-leads-1-038
  type: rule
  name: >-
    Puddles, Ponds, Lakes, Oceans
  statement: >-
    A small business narrows its content to what it does and the place it does it, rather than making general business content.
  why: >-
    The audience will listen to people with better track records than you; narrowing lets you become king of that puddle and expand later to the pond, the lake and eventually the ocean.
  boundary: >-
    Explicitly for a small local business, and for the beginning: not at first, at least.
  anchor: >-
    local business, you probably shouldn't make general business content.
  source: >-
    100m-leads.md, #2 Post Free Content Part II, line 5291
  confirmations: 1
  anchor_at: "100m-leads.md:5291"
- id: D-leads-1-039
  type: antipattern
  name: >-
    Weak free content devalues the paid product
  statement: >-
    Treating free content as lower stakes than the paid product.
  why: >-
    Somebody who buys your stuff is more likely to consume your free content, and customers include it in how they calculate their ROI from the paid thing; if the free content sucks they will like the paid product less.
  anchor: >-
    if they consume your free content, and it sucks, they will like your
  source: >-
    100m-leads.md, #2 Post Free Content Part II, line 5316
  confirmations: 2
  anchor_at: "100m-leads.md:5316"
- id: D-leads-1-040
  type: antipattern
  name: >-
    Blaming short attention spans
  statement: >-
    Explaining weak content performance by the audience's short attention spans.
  why: >-
    People don't have shorter attention spans, they have higher standards: our biology hasn't changed, our circumstances have, and people binge long form content if they like it. There is no such thing as too long, only too boring.
  anchor: >-
    the rewards rather than whining about people's "short attention
  source: >-
    100m-leads.md, #2 Post Free Content Part II, line 5332
  confirmations: 2
  anchor_at: "100m-leads.md:5332"
- id: D-leads-1-041
  type: antipattern
  name: >-
    Avoid Pre-Scheduling Posts
  statement: >-
    Scheduling posts in advance rather than having a person press submit.
  why: >-
    Manually posted content performs better for the author; his explanation is the close feedback loop, since within seconds you will be rewarded or punished for the quality, and that pressure makes you try harder.
  anchor: >-
    Posts]{.calibre11}[. The posts I manually post perform better than ones
  source: >-
    100m-leads.md, #2 Post Free Content Part II, line 5337
  confirmations: 1
  authors_caveat: >-
    The author presents the mechanism as his own theory, not a finding: Here's my theory, and Try it.
  anchor_at: "100m-leads.md:5337"
- id: D-leads-1-042
  type: rule
  name: >-
    Outputs only mean something against consistent inputs
  statement: >-
    Audience metrics are only worth reading if the posting and asking cadence has been held constant.
  why: >-
    We can only control inputs; measuring outputs is only useful if we are consistent with inputs. The author trusted his podcast feedback because he did the same thing every week for years.
  boundary: >-
    A precondition on measurement: pick the posting cadence and the ask cadence you will stick to on a platform before reading the growth numbers.
  anchor: >-
    Remember, we can only control inputs. Measuring outputs is only useful
  source: >-
    100m-leads.md, #2 Post Free Content Part II, line 5392
  confirmations: 1
  anchor_at: "100m-leads.md:5392"
- id: D-leads-1-043
  type: rule
  name: >-
    Give time, time
  statement: >-
    Audience building is measured in years of consistent output, not months.
  why: >-
    The author posted a podcast twice a week for four years before being picked up on the Top 100 list, and it became a Top 10 US business podcast only in its fifth year of multiple podcasts per week. In the beginning it didn't grow much.
  boundary: >-
    A timescale expectation on the content channel: the author's own case took four to five years of uninterrupted weekly output.
  anchor: >-
    For reference, I posted a new podcast twice a week for four years
  source: >-
    100m-leads.md, #2 Post Free Content Part II, line 5404
  confirmations: 2
  anchor_at: "100m-leads.md:5404"
- id: D-leads-1-044
  type: rule
  name: >-
    Earning the right to ask
  statement: >-
    You may make an ask in your very first post, but if it brings nothing you go back to giving until you have earned the right to ask.
  why: >-
    Most people have been providing value to other humans knowingly or unknowingly for a while already, which is what makes the first ask legitimate.
  boundary: >-
    The condition the author attaches to the first-post ask: if it doesn't get you an engaged lead, you need to give for a while first.
  anchor: >-
    engaged lead. If it doesn't, you need to give for a while, then make an
  source: >-
    100m-leads.md, #2 Post Free Content Part II, line 5441
  confirmations: 1
  anchor_at: "100m-leads.md:5441"
- id: D-leads-1-045
  type: antipattern
  name: >-
    Swapping one core four method for another
  statement: >-
    Ditching warm reach outs once you start posting free content.
  why: >-
    Posting free content grows the warm audience, and a bigger warm audience means more people to reach out to, so content gets engaged leads on its own and keeps getting them through warm reach outs; the two are complementary.
  anchor: >-
    ditching one for the other, I recommend you post free content
  source: >-
    100m-leads.md, #2 Post Free Content Part II, line 5512
  confirmations: 1
  anchor_at: "100m-leads.md:5512"
- id: D-leads-1-046
  type: rule
  name: >-
    Legal and ethical only
  statement: >-
    Cold outreach uses only legal methods, and work is automated only where automation is ethical and available.
  why: >-
    The author qualifies his own build as every (legal) cold outreach method we knew, and states he encourages automation when ethical and available.
  boundary: >-
    The author's own limit on the channel and on automating it: legality of the method and ethics of the automation.
  anchor: >-
    portions of the work. I encourage you to automate when ethical and
  source: >-
    100m-leads.md, #3 Cold Outreach, line 6452
  confirmations: 2
  anchor_at: "100m-leads.md:6452"
- id: D-leads-1-047
  type: rule
  name: >-
    Cold outreach takes about a year
  statement: >-
    A cold outreach channel takes roughly a year to become profitable at scale, not weeks.
  why: >-
    Cold outreach veterans told the author it would take a year to scale; he planned twelve weeks, was wrong, and it took almost a year. The month-by-month record shows zero sales in the first month and two sales in the second, with the team twice asking him to pull the plug.
  boundary: >-
    A timescale expectation: proper expectations are part of the method, and the author states cold outreach takes a long time, at least for him.
  anchor: >-
    me it would take a year to scale. I figured we could do it in twelve
  source: >-
    100m-leads.md, #3 Cold Outreach, line 5992
  confirmations: 1
  anchor_at: "100m-leads.md:5992"
- id: D-leads-1-048
  type: antipattern
  name: >-
    Milking the group
  statement: >-
    Prospecting inside a group or community in a way that makes you look like someone only there to take business from it.
  why: >-
    The author prefers to find the contact information outside the group so he doesn't come off that way, though he will reach out inside the platform if he has to.
  anchor: >-
    contact information outside the group so I don't come off as someone
  source: >-
    100m-leads.md, #3 Cold Outreach, line 6199
  confirmations: 1
  anchor_at: "100m-leads.md:6199"
- id: D-leads-1-049
  type: rule
  name: >-
    A searchable list is a worked list
  statement: >-
    Leads that anyone can pull out of a database have already been contacted by other companies; a list you assemble yourself is the freshest.
  why: >-
    If you can search the database, so can everyone else; a self-assembled name is less likely to have received many cold reach outs from other companies. The downside the author names is that it takes the most time.
  applies_when: >-
    The author's ordering: work from the most accessible leads (software, then brokers) to the least accessible; if you have more time than money, start with assembling the list yourself.
  anchor: >-
    leads. Here's an important point. If you can search the database, so can
  source: >-
    100m-leads.md, #3 Cold Outreach, line 6205
  confirmations: 1
  anchor_at: "100m-leads.md:6205"
- id: D-leads-1-050
  type: antipattern
  name: >-
    Opening cold with the pitch
  statement: >-
    Starting a cold contact by asking whether they want to buy what you sell.
  why: >-
    The author's worked example ends with the point that if the caller had opened with hey man, wanna buy some marketing services? you'd probably have hung up; personalisation is what gets your foot in the door.
  applies_when: >-
    The fix the author states: open with one to three pieces of information a friend might know about the prospect, compliment them on it, and ideally show how it benefited you, so the cold reach out looks like a warm one.
  anchor: >-
    call with "hey man, wanna buy some marketing services?" you'd probably
  source: >-
    100m-leads.md, #3 Cold Outreach, line 6294
  confirmations: 1
  anchor_at: "100m-leads.md:6294"
- id: D-leads-1-051
  type: antipattern
  name: >-
    A mediocre lead magnet in cold outreach
  statement: >-
    Sending strangers an ordinary or mediocre free offer.
  why: >-
    If it is not big fast value you blend in with the ocean of people trying to get their attention, and they treat you the same way: they ignore you. Strangers give you far less time to prove your worth and need far more incentive to move toward you.
  anchor: >-
    mediocre, you'll blend in with the ocean of people trying to get their
  source: >-
    100m-leads.md, #3 Cold Outreach, line 6345
  confirmations: 1
  anchor_at: "100m-leads.md:6345"
- id: D-leads-1-052
  type: antipattern
  name: >-
    A lead magnet that is code for a sales call
  statement: >-
    Offering a free session that is really a sales call dressed up as a lead magnet.
  why: >-
    The author's game planning session, code for sales call, was taken by some gyms but most declined through four months of torture; swapping it for as much free service as he could possibly afford 3x'd take rates and made cold outreach a monster channel.
  applies_when: >-
    If the offer or lead magnet isn't working, up the ante: keep offering more until you make it so good they feel stupid saying no.
  anchor: >-
    game planning session as our lead magnet. Some gyms took us up on it,
  source: >-
    100m-leads.md, #3 Cold Outreach, line 6352
  confirmations: 1
  anchor_at: "100m-leads.md:6352"
- id: D-leads-1-053
  type: antipattern
  name: >-
    So good they should pay for it
  statement: >-
    Judging a giveaway by whether it is good enough that people should pay for it, instead of giving away something people actually do pay for.
  why: >-
    The author marks the difference explicitly: he did not say so good they should pay for it, he said stuff they actually pay for. Give away something for free that people would normally pay for and they will want it.
  anchor: >-
    say, "so good they should pay for it," I said, "stuff they actually pay
  source: >-
    100m-leads.md, #3 Cold Outreach, line 6374
  confirmations: 1
  anchor_at: "100m-leads.md:6374"
- id: D-leads-1-054
  type: antipattern
  name: >-
    Polishing the script before the volume
  statement: >-
    Tweaking and perfecting the outreach script before running it at volume.
  why: >-
    There are no awards for prettiest script; phone and chat scripts are never more than a page or two and cold emails rarely more than half a page. Get the first 100 conversations or 10,000 emails out of the way, then tweak as you learn.
  anchor: >-
    prettiest script. Get your first 100 conversations or 10,000 emails out
  source: >-
    100m-leads.md, #3 Cold Outreach, line 6387
  confirmations: 1
  anchor_at: "100m-leads.md:6387"
- id: D-leads-1-055
  type: rule
  name: >-
    The fewer leads, the less automation
  statement: >-
    How much of the outreach you automate is set by how many qualified names exist: small lists get personalised, huge lists can take automation.
  why: >-
    You sacrifice personalization for scale, and you get a higher response rate with personalized messages. With only 1000 hedge fund managers who fit, you personalise every one; with tens of millions of prospects you can get away with less.
  boundary: >-
    The size of the qualified universe is the author's stated limit on automation.
  anchor: >-
    leads you have, the less automation you should use.
  source: >-
    100m-leads.md, #3 Cold Outreach, line 6472
  confirmations: 1
  anchor_at: "100m-leads.md:6472"
- id: D-leads-1-056
  type: antipattern
  name: >-
    Contacting a lead once
  statement: >-
    Reaching out to a cold lead a single time, in a single way.
  why: >-
    Most people don't try more than once; the more ways you try to contact someone the more likely you are to reach them, since people respond to different methods, and contacting someone multiple times in multiple ways shows you are serious. A non-response to one method is itself a reason to follow up with another.
  anchor: >-
    First, you try to contact them more than once. Shocker. But wanna know
  source: >-
    100m-leads.md, #3 Cold Outreach, line 6504
  confirmations: 1
  anchor_at: "100m-leads.md:6504"
- id: D-leads-1-057
  type: rule
  name: >-
    Expect two to three conversations
  statement: >-
    A cold lead booked for an appointment takes more than one conversation before a higher ticket sale.
  why: >-
    You are contacting complete strangers, and outreach takes more touch points with people who don't know you.
  boundary: >-
    Expect two to three conversations before a higher ticket sale; shoot for less, but expect more when you start out.
  anchor: >-
    don't know you. So expect two to three conversations before a higher
  source: >-
    100m-leads.md, #3 Cold Outreach, line 6542
  confirmations: 1
  anchor_at: "100m-leads.md:6542"
- id: D-leads-1-058
  type: antipattern
  name: >-
    Going through the motions
  statement: >-
    Working the outreach list as a procedure rather than actually trying to reach the people on it.
  why: >-
    The author's test is to act like you are actually trying to get ahold of these people, the way you would chase down your own parents over something important, and then you probably will.
  anchor: >-
    rather than going through the motions, and you probably
  source: >-
    100m-leads.md, #3 Cold Outreach, line 6550
  confirmations: 1
  anchor_at: "100m-leads.md:6550"
- id: D-leads-1-059
  type: rule
  name: >-
    Cold outreach sits on top of warm outreach
  statement: >-
    Cold outreach is started after warm reach outs and posted content, not instead of them.
  why: >-
    The book is ordered to build on itself: start with warm reach outs and get reps, post content to grow the warm audience and get more reps, then you are ready for cold reach outs. Cold outreach is the more advanced cousin of warm outreach.
  boundary: >-
    A prerequisite: reps in warm outreach and a warm audience come first.
  anchor: >-
    reach outs. Get some reps. Post some content to grow your warm audience.
  source: >-
    100m-leads.md, #3 Cold Outreach, line 6620
  confirmations: 2
  anchor_at: "100m-leads.md:6620"
- id: D-leads-1-060
  type: antipattern
  name: >-
    Running cold outreach without the metrics
  statement: >-
    Putting cold outreach in the hands of someone who does not track the numbers of the sales process.
  why: >-
    The two times the author failed at cold outreach he hired people who never tracked metrics well; the third person did, and cold reach outs succeeded. Whoever runs it has to know every single stat of the sales process like the back of their hand.
  anchor: >-
    The two times I failed at cold outreach I hired people who never
  source: >-
    100m-leads.md, #3 Cold Outreach, line 6642
  confirmations: 1
  anchor_at: "100m-leads.md:6642"
- id: D-leads-1-061
  type: rule
  name: >-
    Three times is the bare minimum
  statement: >-
    Making three times the lifetime profit of a customer against what it costs to get them is the floor for cold outreach, not the target.
  why: >-
    The author states you can do WAY better than three times and calls it the bare minimum; the portfolio company he cites gets over 30:1 returns from its outreach.
  boundary: >-
    The 3x benchmark is a minimum threshold; treating it as the goal is the author's stated misreading. Figures are from 2023.
  anchor: >-
    profit from a customer. Note: You can do WAY better than three times,
  source: >-
    100m-leads.md, #3 Cold Outreach, line 6708
  confirmations: 2
  anchor_at: "100m-leads.md:6708"
- id: D-leads-1-062
  type: antipattern
  name: >-
    Underestimating the volume and the time
  statement: >-
    Starting cold outreach with an expectation of how much volume and how long it takes that is far below reality.
  why: >-
    Most people dramatically underestimate the amount of volume it takes to use cold outreach and also underestimate how long it takes; the work itself is boring and tedious, but brutally effective, and scaling it is mostly adding bodies.
  anchor: >-
    Most people dramatically underestimate the amount of volume it takes to
  source: >-
    100m-leads.md, #3 Cold Outreach, line 6773
  confirmations: 2
  anchor_at: "100m-leads.md:6773"
- id: D-leads-1-063
  type: rule
  name: >-
    When cold outreach starts
  statement: >-
    Cold outreach is picked up when you run out of people to advertise to, or when you simply want more.
  why: >-
    At some point you will want to grow faster than you currently are, or you will want to increase the predictability of your lead flow; cold outreach is where you get to pick your targets rather than them picking you.
  boundary: >-
    The trigger is exhausting the warm audience or wanting more volume and predictability, not a preference for the channel.
  anchor: >-
    get more engaged leads with cold outreach. You start this as you run out
  source: >-
    100m-leads.md, #3 Cold Outreach, line 6865
  confirmations: 2
  anchor_at: "100m-leads.md:6865"
```
