# Улов фазы 1 — $100M Leads (2023), chapters up to #3 Cold Outreach (lines 1–6900) (ярус 1), тип E: глоссарий

Группа `tier1-leads-1`, слаг `leads-1`, ярус 1. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **45** (экстрактор вернул 45, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-leads.md` | 1–6900 | 6 | 45 |

## Как собран файл

Экстрактор E (Glossary) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier1-leads-1.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier1-leads-1-E.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: E-leads-1-001
  type: term
  name: >-
    Grand Slam Offer
  statement: >-
    A Grand Slam Offer is an offer so good people feel stupid saying no, and the same bar applies to free offers and lead magnets, not only to paid ones.
  definition: >-
    An offer so good people feel stupid saying no; it answers the question "What should I sell?" and is the thing the leads in this book are pointed at.
  applies_when: >-
    Also for free stuff: Grand Slam Offers work for free stuff as much or better than they do for paid stuff, so a lead magnet is built to the same standard.
  anchor: >-
    ]{.calibre24}[Answer - an offer so good people feel stupid saying no.
  source: >-
    100m-leads.md, Section I: Start Here, lines 229–232; named again at lines 278–283 and at Engage Your Leads: Offers and Lead Magnets, lines 1938–1941
  confirmations: 2
  anchor_at: "100m-leads.md:232"
- id: E-leads-1-002
  type: term
  name: >-
    Advertising
  statement: >-
    Advertising is the process of making known: letting strangers know about the stuff you sell, whatever the channel.
  definition: >-
    Advertising, the process of making known, lets strangers know about the stuff you sell.
  why: >-
    If more people know about the stuff you sell, then you sell more stuff; if you sell more stuff, then you make more money. Advertising lets you have a terrible product and still make money, so it gives endless chances to get it right.
  anchor: >-
    making known]{.calibre24}[, lets strangers know about the stuff you
  source: >-
    100m-leads.md, Section I: Start Here, lines 245–249
  confirmations: 1
  anchor_at: "100m-leads.md:247"
- id: E-leads-1-003
  type: term
  name: >-
    Lead
  statement: >-
    A lead is a person you can contact, and nothing more than that.
  definition: >-
    A lead is a person you can contact. That's all. If you bought a list of emails, those are leads. The numbers in your phone are leads. People on the street are leads. If you can contact them, they are leads.
  not_to_confuse_with: >-
    An engaged lead. A lead has shown no interest yet; "leads alone aren't enough".
  why: >-
    Words matter because they affect how we think, how we think affects what we do, and if words have us thinking the wrong way we will probably do the wrong stuff.
  anchor: >-
    ]{.calibre3}[person you can contact]{.calibre35}[. That's all. If you
  source: >-
    100m-leads.md, Leads Alone Aren't Enough, lines 1579–1584
  confirmations: 1
  anchor_at: "100m-leads.md:1580"
- id: E-leads-1-004
  type: term
  name: >-
    Engaged lead
  statement: >-
    An engaged lead is a person who shows interest in the stuff you sell, and engaged leads, not leads, are what advertising is meant to produce.
  definition: >-
    Engaged leads: people who *show* interest in the stuff you sell. If someone gives their contact information on a website, that is an engaged lead. If someone follows you on social media and you can contact them, that is an engaged lead. If people reply to your email campaign, they are engaged leads.
  not_to_confuse_with: >-
    A lead, which is only a person you can contact and may never have shown interest.
  why: >-
    Engaged leads are the true output of advertising; the leads showing interest are the leads that matter.
  anchor: >-
    ]{.calibre3}[people who \*show\* interest in the stuff you
  source: >-
    100m-leads.md, Leads Alone Aren't Enough, lines 1588–1602
  confirmations: 2
  anchor_at: "100m-leads.md:1591"
- id: E-leads-1-005
  type: term
  name: >-
    Offer
  statement: >-
    An offer is what you promise to give in exchange for something of value.
  definition: >-
    Offers are what you promise to give in exchange for something of value. Often, a business promises to give its product or service in exchange for money.
  anchor: >-
    [Offers]{.calibre11}[ are what you promise to give in exchange for
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 1845–1847
  confirmations: 1
  anchor_at: "100m-leads.md:1845"
- id: E-leads-1-006
  type: term
  name: >-
    Core offer
  statement: >-
    The core offer is the main thing you sell: your product or service in exchange for money.
  definition: >-
    A business promises to give its product or service in exchange for money. This is a core offer. Elsewhere: your core offer (the main thing you sell).
  not_to_confuse_with: >-
    A lead magnet, which is the lower-cost or free offer that comes before it.
  why: >-
    If you advertise your core offer, then you go straight for the sale, the direct path to money; advertising the core offer might be all you need to get leads to engage, so try this way first.
  anchor: >-
    service in exchange for money. This is a ]{.calibre3}[core offer.
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 1845–1850; restated at #1 Warm Outreach, lines 3094–3096
  confirmations: 2
  anchor_at: "100m-leads.md:1847"
- id: E-leads-1-007
  type: term
  name: >-
    Lead magnet
  statement: >-
    A lead magnet is a complete solution to a narrow problem, usually low-cost or free, whose solution reveals the next problem that your core offer solves.
  definition: >-
    A lead magnet is a complete solution to a narrow problem. It's typically a lower-cost or free offer to see who is interested in your stuff. And, once solved, it reveals another problem solved by your core offer.
  not_to_confuse_with: >-
    The core offer, which is the main thing you sell in exchange for money.
  why: >-
    Leads interested in lower-cost or free offers now are more likely to buy a related higher-cost offer later; a person who pays with their time now is more likely to pay with their money later.
  applies_when: >-
    Sometimes people want to know more about your offer before they buy; this is common for businesses that sell more expensive stuff.
  anchor: >-
    ]{.calibre3}[complete solution to a narrow problem]{.calibre41}[. It's
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, lines 1858–1868
  confirmations: 2
  anchor_at: "100m-leads.md:1862"
- id: E-leads-1-008
  type: term
  name: >-
    Problem-Solution cycle
  statement: >-
    The Problem-Solution cycle is the author's model for picking the lead magnet's problem: every solution reveals a new problem, and the right narrow problem is the one whose next problem your core offer solves.
  definition: >-
    Every problem has a solution. Every solution reveals more problems. This is the never-ending cycle of business (and life). And, smaller problem-solution cycles sit inside larger problem-solution cycles.
  why: >-
    If we can solve that new problem with our core offer, we've got a winner, because we solve this new problem in exchange for money.
  anchor: >-
    figure this out. I call it the Problem-Solution cycle. You can see it
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, Step 1, lines 1965–1988
  confirmations: 1
  anchor_at: "100m-leads.md:1966"
- id: E-leads-1-009
  type: term
  name: >-
    Call To Action (CTA)
  statement: >-
    A Call To Action tells the audience what to do next and gives reasons to do it right now.
  definition: >-
    A Call To Action (CTA) tells the audience what to do next. Good CTAs have two things: 1) what to do and 2) reasons to do it right now. Good CTAs have clear, simple, and direct language.
  why: >-
    If you give people a reason to take action, more people will do it; good reasons work better than bad reasons, and any reason tends to work better than no reason at all.
  anchor: >-
    ]{.calibre3}[tells the audience what to do next. ]{.calibre24}[But,
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, Step 7, lines 2500–2506
  confirmations: 1
  anchor_at: "100m-leads.md:2503"
- id: E-leads-1-010
  type: term
  name: >-
    Scarcity
  statement: >-
    Scarcity is a limited amount of something, especially a small supply compared to demand, used as a reason to act now.
  definition: >-
    Scarcity is when there is a limited amount of something. Especially when there is a small supply compared to demand.
  not_to_confuse_with: >-
    Urgency, which limits the time people have rather than the number of units available.
  why: >-
    When something is scarce, people tend to want it more, and the fewer you have the more valuable people think it is; the catch is that the fewer you have, the fewer engaged leads you can get before running out.
  anchor: >-
    ]{.calibre11}[Scarcity]{.calibre3}[ is when there is a limited amount of
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, Step 7, lines 2530–2548
  confirmations: 1
  anchor_at: "100m-leads.md:2531"
- id: E-leads-1-011
  type: term
  name: >-
    Ethical scarcity
  statement: >-
    Ethical scarcity is advertising the real limit of what your business can handle instead of inventing one.
  definition: >-
    The best strategy I know for scarcity is reality. If you have a limit to how much you can sell, don't keep it a secret, advertise it. This gives you ethical scarcity.
  why: >-
    Draw attention to the natural scarcity in your business; if you have limitations you may as well use them to make money.
  anchor: >-
    per week, etc. Don't keep it a secret - advertise it. This gives you
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, Step 7, lines 2539–2548
  confirmations: 1
  anchor_at: "100m-leads.md:2544"
- id: E-leads-1-012
  type: term
  name: >-
    Urgency
  statement: >-
    Urgency is when people act faster because they have a short amount of time.
  definition: >-
    Urgency is when people act faster because they have a short amount of time. And the less time people have, the faster (more urgent) they tend to act.
  not_to_confuse_with: >-
    Scarcity: you can have unlimited units to sell and still create urgency by stopping the sale in an hour on purpose.
  why: >-
    If you make the time they can act on your CTA shorter, you can get more of them to act on it faster.
  anchor: >-
    ]{.calibre11}[is when people act faster because they have a short amount
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, Step 7, lines 2567–2576
  confirmations: 1
  anchor_at: "100m-leads.md:2571"
- id: E-leads-1-013
  type: term
  name: >-
    Fraternity Party Planner
  statement: >-
    The Fraternity Party Planner is the author's name for making up a reason to act now when no real scarcity or urgency is available.
  definition: >-
    Fraternity Party Planner (my favorite) - Make Up A Reason. Your reason doesn't even have to make sense, and it will still get more people to act. Think of the stuff you say after the word "because".
  why: >-
    Harvard ran an experiment showing that people were more likely to let someone cut in line if they only gave a reason; the number increased if the reason made sense, but any reason still works better than no reason.
  anchor: >-
    [c) Fraternity Party Planner (my favorite) - Make Up A
  source: >-
    100m-leads.md, Engage Your Leads: Offers and Lead Magnets, Step 7, lines 2602–2615
  confirmations: 1
  anchor_at: "100m-leads.md:2602"
- id: E-leads-1-014
  type: term
  name: >-
    Warm audience
  statement: >-
    A warm audience is the people who gave you permission to contact them.
  definition: >-
    Warm audiences are people who gave you permission to contact them. Think "people who know you" - aka - friends, family, followers, current customers, previous customers, contacts, etc.
  not_to_confuse_with: >-
    A cold audience, which has not given you permission to contact it.
  why: >-
    The difference matters because it changes how we advertise to them.
  anchor: >-
    [Warm audiences]{.calibre11}[ are ]{.calibre3}[people who gave you
  source: >-
    100m-leads.md, Section III: Get Leads, lines 2814–2817
  confirmations: 1
  anchor_at: "100m-leads.md:2814"
- id: E-leads-1-015
  type: term
  name: >-
    Cold audience
  statement: >-
    A cold audience is the people who have not given you permission to contact them.
  definition: >-
    Cold audiences are people who have not given you permission to contact them. Think "strangers" - aka - other peoples' audiences: buying contact lists, making contact lists, paying platforms for access, etc.
  not_to_confuse_with: >-
    A warm audience, which gave you permission to contact it.
  why: >-
    The difference matters because it changes how we advertise to them.
  anchor: >-
    [Cold audiences]{.calibre11}[ are ]{.calibre3}[people who have not given
  source: >-
    100m-leads.md, Section III: Get Leads, lines 2821–2829
  confirmations: 1
  anchor_at: "100m-leads.md:2821"
- id: E-leads-1-016
  type: term
  name: >-
    One to One (Private), One to Many (Public)
  statement: >-
    Communication is either private, one person getting a message at a time, or public, many people getting it at the same time; this axis is one of the two that define the core four.
  definition: >-
    Private communication is when only one person gets a message at a time. Think "phone call" or "email." If you announce something publicly, many people can get it at the same time. Think "social media posts" or "billboards" or "podcasts."
  why: >-
    Like audiences, the difference between public and private communication matters because they change how we advertise.
  anchor: >-
    about this is private or public communication. Private communication is
  source: >-
    100m-leads.md, Section III: Get Leads, lines 2844–2849
  confirmations: 1
  anchor_at: "100m-leads.md:2845"
- id: E-leads-1-017
  type: term
  name: >-
    Automation
  statement: >-
    Automation means only that some of the work is done by machines; it does not change whether the communication is one-to-one or one-to-many.
  definition: >-
    Automation just means some of the work is done by machines. The nature of the communication stays the same.
  not_to_confuse_with: >-
    One-to-many communication. Email is one-to-one; emailing a 10,000 person list "once" is more like one-to-one really fast by a machine.
  anchor: >-
    confusing. Don't let it. Automation just means some of the work is done
  source: >-
    100m-leads.md, Section III: Get Leads, lines 2853–2861
  confirmations: 1
  anchor_at: "100m-leads.md:2854"
- id: E-leads-1-018
  type: term
  name: >-
    The core four
  statement: >-
    The core four are the only four ways to let anyone know about anything: warm outreach, posting content, cold outreach and paid ads.
  definition: >-
    The only four ways we can let anyone know about anything: the core four. 1-to-1 to a Warm Audience = Warm Outreach; 1-to-many to a Warm Audience = Posting Content; 1-to-1 to a Cold Audience = Cold Outreach; 1-to-many to a Cold Audience = Paid Ads.
  why: >-
    These are the only four things you can do to let other people know about the stuff you sell, so if you aren't getting as many leads as you want, you're not doing the core four with enough skill or with enough volume.
  anchor: >-
    the only four ways we can let anyone know about anything: the core four.
  source: >-
    100m-leads.md, Section III: Get Leads, lines 2876–2888
  confirmations: 2
  anchor_at: "100m-leads.md:2877"
- id: E-leads-1-019
  type: term
  name: >-
    Warm reach outs (Warm Outreach)
  statement: >-
    Warm reach outs are one-to-one contact with the people who know you.
  definition: >-
    Warm reach outs are when you make one-to-one contact with your warm audience - aka - the people who know you. It's the cheapest and easiest way to find people interested in the stuff you sell.
  why: >-
    You do everything on your own and make each message personal, so you don't get many engaged leads for your time; but for that reason it is reliable.
  anchor: >-
    [Warm reach outs are when you make one-to-one contact with your warm
  source: >-
    100m-leads.md, #1 Warm Outreach, lines 3082–3088
  confirmations: 2
  anchor_at: "100m-leads.md:3082"
- id: E-leads-1-020
  type: term
  name: >-
    A-C-A framework (Acknowledge, Compliment, Ask)
  statement: >-
    ACA is the reply framework for outreach conversations: acknowledge what they said, compliment them, then ask another question that leads toward your offer.
  definition: >-
    Acknowledge what they said. Restate it in your own words. This shows active listening. Compliment them on whatever they tell you. Tie it to a positive character trait if you can. Ask another question. Lead the conversation in whatever direction you want.
  why: >-
    The ACA framework helps you talk to anyone, so you can learn about the person and guide the conversation toward your offer; people love talking about themselves and love to be complimented, and if people feel good when talking to you, they'll like and trust you more.
  anchor: >-
    [The ]{.calibre3}[ACA]{.calibre11}[ framework is great because it helps
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 5, lines 3286–3320; reused for cold direct messages at #3 Cold Outreach, lines 6704–6706
  confirmations: 2
  anchor_at: "100m-leads.md:3317"
- id: E-leads-1-021
  type: term
  name: >-
    The value equation
  statement: >-
    The value equation is the four-element model the author uses to build an offer from scratch: maximize dream outcome and perceived likelihood of achievement, minimize time delay and effort and sacrifice.
  definition: >-
    Value, as I define it, has four elements: Dream Outcome, Perceived Likelihood of Achievement, Time Delay, Effort and Sacrifice. The goal is to maximize the first two and minimize the second two.
  applies_when: >-
    When you make an offer from scratch.
  authors_caveat: >-
    The author marks it as the core concept of his first book $100M Offers, not new material of this one; and warns to get as close to the ideal as you can without lying or exaggerating.
  anchor: >-
    [When I make an offer from scratch, I refer to the value equation. If
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 6, lines 3352–3401
  confirmations: 1
  anchor_at: "100m-leads.md:3352"
- id: E-leads-1-022
  type: term
  name: >-
    Dream Outcome
  statement: >-
    The dream outcome is what the person wants to happen, the way they want it to happen.
  definition: >-
    Dream Outcome: what the person wants to happen, the way they want it to happen. State the best possible results your product can get. Big bonus points if those results come from people like the one you're talking to.
  anchor: >-
    [1) ]{.calibre3}[Dream Outcome]{.calibre41}[: what the person wants to
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 6, lines 3363–3369
  confirmations: 1
  anchor_at: "100m-leads.md:3363"
- id: E-leads-1-023
  type: term
  name: >-
    Perceived Likelihood of Achievement
  statement: >-
    Perceived likelihood of achievement is how likely the prospect thinks it is that they personally will achieve the goal.
  definition: >-
    Perceived Likelihood of Achievement: how likely they think it is for them to achieve their goal. Include results, reviews, awards, endorsements, certifications, and other forms of 3rd party validation. Also, guarantees are huge.
  anchor: >-
    likely they think it is for them to achieve their goal]{.calibre3}\
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 6, lines 3373–3380
  confirmations: 1
  anchor_at: "100m-leads.md:3374"
- id: E-leads-1-024
  type: term
  name: >-
    Time Delay
  statement: >-
    Time delay is how long the prospect believes it will take to get results after they buy.
  definition: >-
    Time Delay: how long they believe it'll take to get results after they buy. Describe how fast people start getting results, how often they get results when they start, and how long it takes to get the best results possible.
  anchor: >-
    [3) ]{.calibre3}[Time Delay]{.calibre41}[: how long they believe it'll
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 6, lines 3382–3389
  confirmations: 1
  anchor_at: "100m-leads.md:3382"
- id: E-leads-1-025
  type: term
  name: >-
    Effort and Sacrifice
  statement: >-
    Effort and sacrifice is the bad stuff the buyer has to endure and the good stuff they have to give up to get the result.
  definition: >-
    Effort and Sacrifice: The bad stuff they'll have to endure and the good stuff they'll have to give up in their struggle to get the result. Show them the good stuff they can keep doing, and the bad stuff they can avoid, and still get results.
  anchor: >-
    they\'ll have to endure and the good stuff they\'ll have to give up in
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 6, lines 3391–3399
  confirmations: 1
  anchor_at: "100m-leads.md:3392"
- id: E-leads-1-026
  type: term
  name: >-
    Hidden costs
  statement: >-
    Hidden costs are the time, effort and sacrifice it takes to get results from the thing you sell, and they are often the most expensive part of it.
  definition: >-
    Hidden costs are the time, effort, and sacrifice it takes to get results from the thing you sell. In other words, the bottom part of the value equation.
  why: >-
    If you struggle to give your stuff away for free, it means either people don't want it (dream outcome), they don't believe you (perceived likelihood of achievement), or the hidden costs are too high: your 'free' stuff is too expensive.
  anchor: >-
    the hidden costs. ]{.calibre3}[Hidden costs]{.calibre11}[ are the time,
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 7, lines 3596–3607
  confirmations: 1
  anchor_at: "100m-leads.md:3597"
- id: E-leads-1-027
  type: term
  name: >-
    The 9-word email
  statement: >-
    The 9-word email is a one-question message sent to a warm list, "Are you still looking to [4 word desire]?", used to find who is still interested.
  definition: >-
    Dean Jackson's timeless "9-word email" template: "Are you still looking to [4 word desire]?" No images. No frills. No links. Just a question. Nothing else.
  why: >-
    You make the ask to see who replies, aka engaged leads, and these replies should be your top priority for warm reach outs; it is among the first things the author does when he invests in a new business.
  applies_when: >-
    Once you've given value to your list for a while, or to see who wants value.
  anchor: >-
    list with Dean Jackson\'s timeless \"9-word email\"
  source: >-
    100m-leads.md, #1 Warm Outreach, Step 10, lines 3717–3724
  confirmations: 1
  authors_caveat: >-
    Attributed by the author to Dean Jackson, not to himself.
  anchor_at: "100m-leads.md:3719"
- id: E-leads-1-028
  type: term
  name: >-
    Posting free content
  statement: >-
    Posting free content is the core-four method of speaking one-to-many to a warm audience, and its compounding asset is the audience rather than the content.
  definition: >-
    1-to-many to a Warm Audience = Posting Content. By posting free content, we can say it once and reach all ten, so posting free content can get a lot more engaged leads for the time we invest.
  why: >-
    The content you create isn't the compounding asset, the audience is; free content also makes all other advertising more effective, because people who find lots of valuable content are more likely to buy.
  authors_caveat: >-
    Trade-offs the author names: it is harder to personalize so fewer people respond, you compete with everyone else posting, and if you stand out people will copy you.
  anchor: >-
    times. Lots of effort. By posting free content, we can say it once and
  source: >-
    100m-leads.md, #2 Post Free Content Part I, lines 4146–4150; named at Section III: Get Leads, line 2884
  confirmations: 2
  anchor_at: "100m-leads.md:4148"
- id: E-leads-1-029
  type: term
  name: >-
    Hook, retain, reward
  statement: >-
    Hook, retain and reward are the three things content must do: get them to notice it, get them to consume it, and satisfy the reason they consumed it.
  definition: >-
    A content unit has three components - Hook, retain, and reward. Hook attention: get them to notice your content. Retain attention: get them to consume it. Reward attention: satisfy the reason they consumed it to begin with.
  why: >-
    All audience-growing content does one thing, it rewards the people consuming it, and a person can only get rewarded if they have a reason to consume it, pay attention long enough, and get that reason satisfied.
  anchor: >-
    units. A content unit has three components - Hook, retain, and reward.
  source: >-
    100m-leads.md, #2 Post Free Content Part I, lines 4201–4253
  confirmations: 2
  anchor_at: "100m-leads.md:4203"
- id: E-leads-1-030
  type: term
  name: >-
    Content unit
  statement: >-
    A content unit is the smallest amount of material that hooks, retains and rewards attention; longer content is content units linked together.
  definition: >-
    The smallest amount of material it takes to hook, retain and reward attention is a content unit. It can be as little as an image, a meme, or a sentence.
  why: >-
    Hook, retain and reward can all happen at once, which is how short tweets, meme images or a jingle go viral; and to create a longer piece of content, we simply link content units together.
  anchor: >-
    [The smallest amount of material it takes to hook, retain and reward
  source: >-
    100m-leads.md, #2 Post Free Content Part I, lines 4256–4262; restated at lines 4749–4752
  confirmations: 2
  anchor_at: "100m-leads.md:4256"
- id: E-leads-1-031
  type: term
  name: >-
    Headline
  statement: >-
    A headline is a short phrase or sentence that grabs attention by communicating the reason to consume the content.
  definition: >-
    A headline is a short phrase or sentence used to grab the audience's attention. It communicates the reason they should consume the content. They use it to weigh the likelihood they will get a reward for consuming your content versus another.
  anchor: >-
    [Headlines]{.calibre11}[. A headline is a short phrase or sentence used
  source: >-
    100m-leads.md, #2 Post Free Content Part I, Hook, lines 4428–4431
  confirmations: 1
  anchor_at: "100m-leads.md:4428"
- id: E-leads-1-032
  type: term
  name: >-
    Lists, steps, and stories
  statement: >-
    Lists, steps and stories are the author's three ways of embedding unresolved questions in the audience's mind to retain attention.
  definition: >-
    Lists are things, facts, tips, opinions, ideas, etc. presented one after the other. Steps are actions that occur in order and accomplish a goal when completed. Stories describe events, real or imaginary.
  not_to_confuse_with: >-
    Steps versus lists: steps are actions that must be done in a specific order to get a result, so steps are less flexible but have a more explicit reward; lists can have anything on them in any order, so they are more flexible but have a less explicit reward.
  why: >-
    Curiosity drives retention, and unresolved questions, explicit or implied, make people want to know what happens next.
  anchor: >-
    [Note: Here's the difference between steps and lists. Steps are
  source: >-
    100m-leads.md, #2 Post Free Content Part I, Retain, lines 4568–4657
  confirmations: 1
  anchor_at: "100m-leads.md:4619"
- id: E-leads-1-033
  type: term
  name: >-
    Value per second
  statement: >-
    Value per second is the measure of how good content is: how often it rewards the audience in the time it takes them to consume it.
  definition: >-
    How good your content is depends on how often it rewards your audience in the time it takes them to consume it. Think value per second.
  why: >-
    The same person who gets bored three seconds into a ten-second video may binge a 900-page book, so there is no such thing as too long, only too boring.
  anchor: >-
    it rewards your audience in the time it takes them to consume
  source: >-
    100m-leads.md, #2 Post Free Content Part I, Reward, lines 4678–4684; the corollary repeated at #2 Post Free Content Part II, lines 5324–5327
  confirmations: 2
  anchor_at: "100m-leads.md:4679"
- id: E-leads-1-034
  type: term
  name: >-
    Give : ask ratio
  statement: >-
    The give : ask ratio is how much rewarding content you put out for every offer you make; growing platforms over-give and under-ask, mature ones sit near give-give-give-ask.
  definition: >-
    You deposit goodwill with rewarding content, then withdraw from it by making offers. Television is roughly a 3.5:1 ratio of giving to asking and Facebook roughly 4 content posts per 1 ad, which is the minimum ratio that can be sustained.
  why: >-
    When you deposit goodwill, your audience pays more attention and is more likely to do what you ask; the more you reward your audience, the bigger it gets, so if you want to grow an audience, give far far more than you ask.
  authors_caveat: >-
    Television and Facebook are mature platforms that care more about making money than about growing, so they are the model for maximally monetizing an audience, not for growing one.
  anchor: >-
    [Thankfully, the give : ask ratio has been well-studied. Television
  source: >-
    100m-leads.md, #2 Post Free Content Part II, lines 4829–4864; the idea attributed to Gary Vaynerchuk's "jab, jab, jab, right hook" at line 4833
  confirmations: 1
  anchor_at: "100m-leads.md:4843"
- id: E-leads-1-035
  type: term
  name: >-
    Give until they ask
  statement: >-
    Give until they ask is the author's version of the give-ask strategy: keep giving in public until the audience asks you for the offer in private.
  definition: >-
    If you give enough, people start asking you. When you use this strategy, you give in public, ask in private. You let the audience self-select when they're ready to give you money.
  why: >-
    People are always waiting for you to ask for money, and when you don't, they trust you more and share your stuff more; you get the best customers, and your growth never slows. The moment you start asking for money is the moment you decide to slow down your growth.
  anchor: >-
    [So, it's simple. If you give enough, ]{.calibre3}[people start asking
  source: >-
    100m-leads.md, #2 Post Free Content Part II, lines 4872–4914
  confirmations: 2
  anchor_at: "100m-leads.md:4889"
- id: E-leads-1-036
  type: term
  name: >-
    Integrated (offers)
  statement: >-
    An integrated offer is an ask woven into every piece of content, kept small enough that the give : ask ratio stays high.
  definition: >-
    Integrated: You can advertise in every piece of content so long as you keep your give : ask ratio high. For example, an hour-long podcast with 3 x 30-second ads is 58.5 min of giving to 1.5 min of asking.
  not_to_confuse_with: >-
    Intermittent offers, where whole pieces of content are pure gives and only an occasional piece is an ask.
  applies_when: >-
    On long-form platforms, integrations are often your best bet.
  authors_caveat: >-
    A friend whose podcast blew up started asking too frequently inside the content and the podcast stopped growing and shrank; over-give to protect the goodwill of your audience.
  anchor: >-
    [Integrated]{.calibre41}[: You can advertise in every piece of content
  source: >-
    100m-leads.md, #2 Post Free Content Part II, lines 4954–4980
  confirmations: 1
  anchor_at: "100m-leads.md:4954"
- id: E-leads-1-037
  type: term
  name: >-
    Intermittent (offers)
  statement: >-
    An intermittent offer is a whole piece of content devoted to the ask after many pieces of pure giving.
  definition: >-
    You make many pieces of content of pure 'gives' then occasionally make an 'ask' piece. Example: You make 10 'give' posts, and on the 11th, you promote your stuff.
  not_to_confuse_with: >-
    Integrated offers, where the ask sits inside every piece of content.
  applies_when: >-
    On short platforms, the intermittent way will dominate.
  anchor: >-
    [Intermittent]{.calibre41}[: The second way you can monetize is through
  source: >-
    100m-leads.md, #2 Post Free Content Part II, lines 4992–5001
  confirmations: 1
  anchor_at: "100m-leads.md:4992"
- id: E-leads-1-038
  type: term
  name: >-
    Depth then width
  statement: >-
    Depth then width is the scaling strategy of maximizing one platform before adding the next.
  definition: >-
    Depth then width: Maximize a platform, then move onto the next platform. Post on a relevant platform, post regularly, maximize quality and quantity there, then add another platform while maintaining the first, and repeat until all relevant platforms are maximized.
  not_to_confuse_with: >-
    Width then depth, which gets on every platform early and maximizes them together.
  why: >-
    Once you figure out one platform you maximize your return on that effort, audiences compound faster the more you do, and fewer resources are required.
  authors_caveat: >-
    Disadvantages the author names: less low hanging fruit, no feeling of omnipresence, and the risk of your business being reliant on a single channel that can change rules or ban you.
  anchor: >-
    [Depth then width:]{.calibre66}[ Maximize a platform, then move onto the
  source: >-
    100m-leads.md, #2 Post Free Content Part II, How to Scale It, lines 5071–5122
  confirmations: 1
  anchor_at: "100m-leads.md:5078"
- id: E-leads-1-039
  type: term
  name: >-
    Width then depth
  statement: >-
    Width then depth is the scaling strategy of getting onto every relevant platform early and only then maximizing output on all of them.
  definition: >-
    Width then depth: Get on every platform early, then maximize them together. Instead of maximizing your first platform, move onto the next relevant platform while maintaining the previous, continue until you are on all relevant platforms, then maximize content creation on all platforms at once.
  not_to_confuse_with: >-
    Depth then width, which maximizes one platform before adding the next.
  why: >-
    You reach a broader audience faster and you can repurpose content, so with a little extra work the same content fits multiple platforms.
  authors_caveat: >-
    It costs more labor, attention and time to do well, and oftentimes people end up with lots of bad content everywhere.
  anchor: >-
    [Width then depth]{.calibre66}[:]{.calibre11}[ Get on every platform
  source: >-
    100m-leads.md, #2 Post Free Content Part II, How to Scale It, lines 5126–5168
  confirmations: 1
  anchor_at: "100m-leads.md:5126"
- id: E-leads-1-040
  type: term
  name: >-
    Puddles, Ponds, Lakes, Oceans
  statement: >-
    Puddles, ponds, lakes and oceans is the author's name for narrowing content to the smallest audience you can be king of, then widening it over time.
  definition: >-
    Narrow the focus of your content. Narrow your topics to what you do and the place you do it, for example plumbing in a certain town; then you can become king of that puddle. Over time you expand the plumbing puddle to the general local business pond, then the lake of brick & mortar chains, then eventually the ocean of general business.
  why: >-
    If you have a small local business you probably shouldn't make general business content at first, because the audience will listen to people with better track records than you.
  anchor: >-
    expand your plumbing puddle to the general local business pond. Then the
  source: >-
    100m-leads.md, #2 Post Free Content Part II, 7 Lessons I've Learned From Making Content, lines 5289–5298
  confirmations: 1
  anchor_at: "100m-leads.md:5296"
- id: E-leads-1-041
  type: term
  name: >-
    Cold outreach
  statement: >-
    Cold outreach is private one-to-one contact with strangers, the core-four method that is no longer limited by the size of your warm audience.
  definition: >-
    Private one-to-one communication with cold outreach; we advertise to people who don't know us, cold audiences. Cold outreach sits atop the foundation of warm outreach, the more advanced cousin of warm outreach, no longer limited by your warm audience.
  not_to_confuse_with: >-
    Warm outreach. Cold outreach has one key difference from warm outreach: trust. Strangers don't trust you, and they present three new problems: no way to contact them, being ignored, and not being interested.
  why: >-
    Cold outreach is a numbers game: the more people you reach out to the more engaged leads you get, so once you know how much outreach it takes to engage a lead, you only have to do more.
  authors_caveat: >-
    Cold outreach takes a long time; veterans told the author it would take a year to scale, he figured twelve weeks and was wrong, it took almost a year.
  anchor: >-
    privately. In this chapter, we focus on private one-to-one communication
  source: >-
    100m-leads.md, #3 Cold Outreach, lines 6013–6039
  confirmations: 2
  anchor_at: "100m-leads.md:6021"
- id: E-leads-1-042
  type: term
  name: >-
    Personalization
  statement: >-
    Personalization in cold outreach means opening with one to three things about the prospect that a friend might know, so the cold reach out looks like a warm one.
  definition: >-
    Personalization is what gets your foot in the door to get the sale. Basically one to three pieces of information we can find that a friend might know about the prospect. Then we want to complement them on it, and ideally, show them how it benefited us.
  why: >-
    People like people who like them; even if someone doesn't know you, they'll give you more time if you know something about them, and they will appreciate the time you took to research them before contacting them.
  applies_when: >-
    Personal subject lines on emails, the first few messages in chat, or the first few sentences someone hears.
  anchor: >-
    [Personalization]{.calibre24}[ is what gets your foot in the door to get
  source: >-
    100m-leads.md, #3 Cold Outreach, Problem #2, lines 6246–6312
  confirmations: 1
  anchor_at: "100m-leads.md:6299"
- id: E-leads-1-043
  type: term
  name: >-
    Big fast value
  statement: >-
    Big fast value is the cold-outreach standard for what you lead with: give away something people actually pay for, and demonstrate it as fast as possible.
  definition: >-
    I specifically call out 'big fast value' rather than "your lead magnet" as a reminder that it needs to be BIG FAST VALUE. The goal is to demonstrate big value as fast as possible. Give away something for free people would normally pay for, not something so good they should pay for it.
  why: >-
    Strangers give you far less time to prove your worth and need more incentive to move toward you; if the value is mediocre you'll blend in with the ocean of people trying to get their attention and be ignored. We're not trying to tickle their interest, we're trying to blow their minds in under thirty seconds.
  anchor: >-
    [I specifically call out 'big fast value' rather than "your lead magnet"
  source: >-
    100m-leads.md, #3 Cold Outreach, Problem #2, lines 6328–6376
  confirmations: 2
  anchor_at: "100m-leads.md:6343"
- id: E-leads-1-044
  type: term
  name: >-
    Automated delivery
  statement: >-
    Automated delivery means the message itself is recorded once and sent to everyone, so no person has to convey it each time.
  definition: >-
    Automating delivery unlocks huge scale as someone doesn't need to literally communicate the message to the prospect. You record your message one time and then send the same message to everyone. If it takes a person time to convey the message each time, it's manual.
  not_to_confuse_with: >-
    Automated distribution, which is about sending the prepared messages out rather than producing them.
  why: >-
    You get more engaged leads per unit of time even if fewer engage by overall percentage, and you have far more people who don't know you than people who do, so you don't have to worry as much about burning through an audience.
  anchor: >-
    automating delivery unlocks huge scale as someone doesn't need to
  source: >-
    100m-leads.md, #3 Cold Outreach, Problem #3, lines 6408–6440
  confirmations: 1
  anchor_at: "100m-leads.md:6409"
- id: E-leads-1-045
  type: term
  name: >-
    Automate distribution
  statement: >-
    Automating distribution means sending the prepared messages in bulk instead of one by one.
  definition: >-
    Once we have our messages prepared, we gotta distribute them. Manual examples: dial each phone number, click send on each email, direct message, text. Automated examples: use a robot to dial multiple numbers at a time, send a blast of 1000 emails, texts, voicemails at one time.
  not_to_confuse_with: >-
    Automated delivery, which is about recording the message once rather than sending it out.
  authors_caveat: >-
    Generally speaking, you sacrifice personalization for scale; you get a higher response rate with personalized messages, and the fewer leads you have, the less automation you should use.
  anchor: >-
    [b) Automate Distribution]{.calibre66}[. Once we have our messages
  source: >-
    100m-leads.md, #3 Cold Outreach, Problem #3, lines 6448–6472
  confirmations: 1
  anchor_at: "100m-leads.md:6448"
```
