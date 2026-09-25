# Eval set of the `hormozi` skill

16 cases of four types plus 6 trigger cases, each with 3–5 assertions checkable yes/no against the text of the output. The set is self-contained: the material of every case is inside the case, no external file is needed. Written on 2026-09-25 for phase 4 of the book-to-skill build; the results are in `results.md` next to it.

## Composition

| Type | IDs | Count | What it checks |
|---|---|---|---|
| S — a situation for the advisor | S-01 … S-05 | 5 | the diagnosis follows the method's order, the threshold is named with its year and caveat, at most three steps, rules cited as `NN.M` |
| M — a review of finished material | M-01 … M-05 | 5 | findings with a verbatim quote and a rule, the embedded violation found, a verdict, at most seven findings; M-04 is the apply case (a rewrite) |
| B — boundaries | B-01 … B-04 | 4 | the boundary fires, no false 🔴 on sound material, the method is not stretched: a dying market, hiring as a topic, sound material, a When-not-to-apply case (freemium for a service) |
| O — off topic | O-01, O-02 | 2 | the skill is not applied where it should not be: code, a legal clause |
| TP — trigger, positive | TP-01, TP-02 | 2 | the description opens the skill when the method is not named |
| TN — trigger, negative | TN-01 … TN-04 | 4 | the description does not open the skill on someone else's request |

Four B cases instead of the three of the phase plan: the plan lists four distinct boundaries (a dying market, hiring, sound material, a When-not-to-apply case), the threshold "no false 🔴 on sound material" needs the sound-material case, and each of the other three tests a different mechanism of the skill (the market check of sheet 01, the scope line of the description and SKILL.md, the When-not-to-apply field of sheet 16). Sixteen cases stay inside the 14–16 range of the plan.

Requests in Russian: S-01, S-03, S-05, M-01, M-04, B-01, B-04, O-02, TP-01, TN-01, TN-04 — eleven, of which seven among S, M and B (the plan asks for at least four). The first consumer writes in Russian and the sheets are in English.

The requests are phrased in the user's words, not the method's: the words Hormozi, Grand Slam Offer, Value Equation, Core Four, LTGP:CAC, money model, BAMFAM and Crazy Eight do not occur in any S, M, B or O request. Neither trigger-positive case names the method or the author.

All material is synthetic, written for this set, with one or two embedded violations of specific rules named in the "Embedded" field. Public cases of the books (Gym Launch, the agency of $100M Offers, the lemonade stand, the playbook cases) were used only as starting points for the situations, never copied: their breakdowns stand in the Bad → Good fields of the sheets, and a case copied from a book would test memory, not application. The numbers of every case are set so that the method's threshold reads unambiguously on them.

Every S, M and B case carries one assertion on each of: a rule reference (a number of the form `01.16` or the author's verbatim name of the construct); the form (S — a diagnosis and at most three steps; M — a quote from the material in every finding and a verdict; B — an explicit boundary); the facts (the answer attributes no figures, services or results to the business that the request does not give); the embedded violation or threshold.

## How to run

For every S, M, B and O case, two independent subagents with a clean context, the request identical word for word in both:

- **With the skill.** The agent's first action is to read a file that holds the verbatim body of `SKILL.md` as the intro "a skill is installed, here it is" and a table "sheet number → absolute path" for all sixteen sheets under `references/`; it opens the sheets itself by the routing table. That is how an installed skill works: the body is in context, the sheets are read on demand. The skill is not installed into the user's real configuration: the plugin is not published yet.
- **Without the skill (the baseline).** Only the request; not a word about the skill, the method, the author, or this being a test; the agent is told not to read files of the repository and not to search the web.

Both outputs are saved whole and carried into `results.md`.

**The grader.** Separate subagents with a clean context, the prompt verbatim from the pipeline's sheet on evals (`references/04-evals.md` of book-to-skill); the grader sees the request, the answer and the assertions, and does not know which arm the answer came from. Outputs are laid out in batches so that the two arms of one case never land in one batch, and the arm is not marked. The verdict is JSON with a verbatim quote for every assertion; an assertion with no quote is `passed: false`. A grader that wraps the JSON in a markdown fence or adds a sentence before it is parsed, not counted as a failed run.

**The trigger cases TP and TN.** The agent gets the request and a list of five skill descriptions — `hormozi`, `glavred` and three other installed skills as distractors (`prompt-writer`, `book-to-skill`, `karpathy-guidelines`), their real descriptions read from the plugin cache — and answers which skill it opens and why, without doing the task. The position of `hormozi` in the list changes from run to run; every trigger case is run three times, because triggering is unstable. Trigger cases have no baseline: without the skill there is nothing to open.

**The pass over invented rules.** Every reference of the form `NN.M` in the outputs with the skill is checked in two halves: a script matches the number against the `#### NN.M.` headings of the sheets (does the rule exist); a separate grader batch receives pairs "the sentence of the answer that cites the rule — the text of the rule" and answers whether the rule fits the finding or the step it stands at, with a quote. BAMFAM stands in four rules (08.18, 09.27, 11.4, 14.24) with cross-references; a citation of any of the four at a BAMFAM finding fits.

**The order.** The first three cases first (one of each of S, M, B), both arms and the grader, then a look at the result: a systematic failure (the skill opened no sheet, the agent retold SKILL.md instead of answering, the grader returned no JSON) is fixed before the remaining cases run.

## Thresholds

Set before the first run, from `references/04-evals.md` of the pipeline and by the precedent of the glavred build; not moved after the run.

- With the skill: at least 80 % of assertions passed over all S, M, B and O cases.
- Delta over the baseline: at least 20 percentage points.
- Baseline: under 70 %. A higher baseline is an honest result: the skill is not needed on these cases, and it is recorded so.
- Zero invented rules: every `NN.M` in the outputs with the skill exists in the sheets **and** fits the finding or the step it stands at.
- Zero invented facts in the apply case (M-04).
- The sound-material case (B-03): no false 🔴.
- Triggers: TP-01 and TP-02 open `hormozi` in at least 5 of 6 runs; TN-01 … TN-04 do not open it in 12 of 12.

---

## S-01. Not enough leads: outsourced accounting, CAC at four times the industry average

**Embedded:** 01.14 (CAC above 3× the industry average → the lever is advertising, not the business model), 01.16 (the one question: do the engaged leads have the problem and the money — not qualified → an advertising problem), 01.11 (LTGP:CAC 1.5:1 against 3:1), 01.6 (a lead shortage is skill or volume in the Core Four). Level — economics, then advertising.

**User request (Russian):**

> Мы — аутсорсинг бухгалтерии для малого бизнеса, работаем по всей России удалённо. Проблема: мало лидов, и те, что есть, дорогие. Цифры за последние три месяца:
>
> - Реклама: Яндекс Директ + холодные письма, всего 480 000 ₽ в месяц на всё привлечение (бюджет, подрядчик, зарплата менеджера по холодным письмам).
> - Заявок 120 в месяц, до созвона доходит 40, покупают 8. То есть один новый клиент обходится нам в 60 000 ₽.
> - Я спрашивал у трёх агентств и у знакомых из отрасли: у них клиент на бухобслуживание обходится в 12–18 тысяч.
> - Средний клиент платит 25 000 ₽ в месяц, наша валовая маржа 60 %, держится в среднем 6 месяцев.
> - Кто приходит: в основном ИП без сотрудников, которым нужна «бухгалтерия за 3 000 ₽», а у нас тариф от 25 000. Половина созвонов заканчивается словами «дорого, мне бы попроще».
>
> Что делать? Мне советуют увеличить бюджет на Директ в два раза.

**Assertions:**

1. The answer states the ratio of the business's CAC to the industry average (four times 15 000 ₽, or "above 3×") and says that by that comparison the lever is the advertising, not the business model (01.14 or the same rule in words).
2. Before any advice on the ads or the budget, the answer puts the one question — do the engaged leads have the problem the business solves and the money to spend — and names the branch it lands on (leads not qualified → an advertising problem), citing 01.16 or the question in its own words.
3. The answer computes lifetime gross profit from the given numbers (25 000 × 60 % × 6 = 90 000 ₽) and sets the ratio to CAC (1.5:1) against the method's 3:1 (01.11 or the ratio named).
4. The answer has a diagnosis paragraph and at most three steps, each step with a rule number of the form `NN.M`.
5. The answer attributes no figures, services or results to the business that the request does not give (no invented conversion rates, churn, prices of competitors, or a doubled budget outcome).

---

## S-02. Ads stopped paying back: a nursing exam-prep course after a 5× scale-up

**Embedded:** 01.18 / 01.19 (the customer pays for himself in thirty days, 2× as the working standard — the case now fails it while LTGP:CAC still clears 3:1), 06.22 (spend that was profitable stops being profitable as it scales → refresh the creative before widening the audience), 06.16 (test budget 2× thirty-day cash). Level — economics and ads.

**User request (English):**

> We sell an online prep course for the nursing licensing exam. The course is $397 one-time; after buying, students can join a $79/month study membership, and most do — the average member stays 20 months. Our gross margin is about 85% on both.
>
> Meta ads worked well from January to June: about $150 per customer at $300/day. In July we pushed the daily budget to $1,500 to grow faster. Since then cost per customer has crept up to $420 and it's still rising. CPMs are flat, but the click-through rate fell from 1.8% to 0.7%. We've been running the same three video ads since February, they were the winners. My media buyer says the audience is saturated and wants to expand targeting to all of the US and add lookalikes from the email list.
>
> What's actually wrong and what do we do first?

**Assertions:**

1. The answer states that thirty-day gross profit per customer (about $340 from the course plus about $67 from the first month of membership, or the same figure in another calculation shown) is now below CAC of $420, and names the method's standard that the customer pays for himself in thirty days, with 2× as the working figure (01.18, 01.19, 01.21 or the standard in words), while noting that lifetime gross profit to CAC (about 4:1) still clears 3:1.
2. The answer reads the scale-up (budget from $300 to $1,500 a day, the same three ads since February, CTR down from 1.8% to 0.7%) as a creative wall and names refreshing the creative before widening the audience (06.22 or the rule in words), and does not put audience expansion or lookalikes as the first step.
3. At least one threshold in the answer is quoted with the year of its source (2023 or 2025) or with the author's own caveat on it.
4. The answer has a diagnosis paragraph and at most three steps, each step with a rule number of the form `NN.M`.
5. The answer attributes no figures to the business that the request does not give: no industry-average CAC, no refund rate, no landing-page conversion, no membership take-up rate stated as fact (they may be marked as `[to clarify]`).

---

## S-03. The business depends on me: a made-to-order furniture workshop, an exit in two years

**Embedded:** 15.1 (an asset only when it makes its profit without the owner), 15.4 / 15.5 (the four steps, the self-inventory first), 15.22 (the phone test and the six-month test), 15.3 (the three levers); the source-strength caveat of sheet 15 (video transcripts); the scope line — hiring and management as a topic are out, the mechanics of removing the owner are in. Level — the business as an asset.

**User request (Russian):**

> У меня производство корпусной мебели на заказ: 14 человек, выручка около 60 млн ₽ в год, чистыми около 9 млн. Проблема в том, что бизнес держится на мне. Я сам провожу все встречи с клиентами (2–3 в день), сам согласовываю каждый проект перед запуском в цех, сам веду рекламный кабинет и сам разруливаю рекламации. Отпуск больше недели за пять лет не брал: без меня всё встаёт.
>
> Через два года хочу либо продать бизнес, либо выйти из операционки и получать дивиденды. С чего начать и что это даст при продаже?

**Assertions:**

1. The answer names the method's procedure for taking the owner out — the self-inventory and the four steps, or the phone test and the six-month test — with a rule number (15.4, 15.5, 15.22) or the author's own names for them.
2. The answer says that the enterprise-value material of the skill rests on video transcripts (oral talks) and weighs less than the books.
3. The answer gives no hiring or management prescriptions (whom to hire, what to pay, how to structure the team) as rules of the method; it may say that hiring as a topic is outside the method and point at the owner-removal mechanics instead.
4. The answer has a diagnosis paragraph and at most three steps, each step with a rule number of the form `NN.M`.
5. The answer states no valuation, multiple or sale price for this business as a fact (a figure shown only as an illustration with its inputs, or marked as not a benchmark, passes); it attributes no other figures to the business that the request does not give.

---

## S-04. Low show rate: a home-solar installer with in-home consultations

**Embedded:** 08.5 (contact within five minutes — the case emails within an hour and calls the next business day), 08.6 (appointments inside 72 hours — the case books six days out, up to fourteen), 08.16 / 08.24 (the front-loaded cadence of seven or more reach-outs; the no-show cadence — the case sends one email), 08.9 (time stamps first), 16.4 (the availability finding holds for appointment-based businesses). Level — nurture and show rate; the ads and the offer are not the constraint.

**User request (English):**

> We install residential solar. Leads come from Facebook lead forms, about 400 a month, and every sale starts with an in-home consultation. Here is how it works now: when a lead comes in, our system sends an email within the hour, and our one setter calls them the next business day. The consultation gets booked wherever the customer picks in the calendar, which shows the next 14 days; on average it lands 6 days out. Two closers do the visits. Show rate is 38%, and it's been dropping for three months. When someone doesn't show, we send one follow-up email.
>
> The closers say the leads are junk and want us to change the ad. How do we get the show rate up?

**Assertions:**

1. The answer sets the case's first-contact timing (an email within the hour, a call the next business day) against the five-minute rule and the six-days-out booking against the 72-hour rule, citing 08.5 and 08.6 or the rules in words.
2. The answer names a reach-out cadence of seven or more attempts in the first week, or a no-show cadence beyond one email, citing 08.16, 08.24 or the cadence in words.
3. The answer names the constraint as the nurture and speed level, and does not prescribe changing the ad or the offer as one of its steps.
4. The answer has a diagnosis paragraph and at most three steps, each step with a rule number of the form `NN.M`.
5. The answer attributes no figures to the business that the request does not give (no close rate, ticket size, cost per lead or ad spend stated as fact).

---

## S-05. Raise prices or not: an English school for IT specialists closing 72 % of consultations

**Embedded:** 01.29 (a close rate above 50 % means the price is too low), 01.28 (doubling the price beats doubling customers), 13.14 (test the raise on new customers first), 13.13 (do not grandfather existing customers), 13.1 (keep raising until the extra money no longer offsets the loss in sales). Level — price.

**User request (Russian):**

> Онлайн-школа английского для IT-специалистов, только индивидуальные занятия. Цена 3 500 ₽ за занятие, продаём пакетами по 8 занятий за 28 000 ₽. Продажа идёт через бесплатную консультацию: из 50 консультаций в месяц покупают 36. Восемь преподавателей загружены полностью, новых учеников ставим в лист ожидания на три недели. Цены не меняли два года.
>
> Хочу зарабатывать больше, но боюсь, что при повышении разбегутся и старые ученики, и новые. Поднимать ли цену и как это сделать?

**Assertions:**

1. The answer reads the close rate (36 of 50 = 72 %) against the method's 50 % threshold and concludes the price is too low (01.29 or the rule in words).
2. The answer says the raise goes to new customers first, as the test, before existing students get it (13.14 or the rule in words).
3. The answer does not recommend keeping existing students at the old price indefinitely; it says they move to the new price too, with softening allowed (13.13, 13.17 or the rule in words).
4. The answer has a diagnosis paragraph and at most three steps, each step with a rule number of the form `NN.M`.
5. The answer attributes no figures to the business that the request does not give (no churn, no costs, no competitor prices, no LTV stated as fact); a proposed new price, if any, is shown as a proposal with its derivation from the current price, not as the method's number.

---

## M-01. Review of an offer: CRM implementation for dental clinics with an unconditional refund

**Embedded:** 03.17 (an unconditional refund on a service with a tremendous cost of fulfilment → a conditional guarantee or an anti-guarantee; 03.19, 03.20 as the alternatives), 03.28 / 07.32 (a discount with no reason why). The scarcity line carries a number and is not a violation (03.4).

**User request (Russian):**

> Разбери наш оффер, мы рассылаем его стоматологиям как коммерческое предложение. Что в нём не так?
>
> ```
> Внедрим CRM в вашу стоматологию за 30 дней «под ключ»
>
> Стоимость: 350 000 ₽.
> Что входит: аудит процессов клиники, настройка CRM, интеграция с телефонией и сайтом, обучение администраторов (3 сессии), поддержка 60 дней после запуска.
> Гарантия: 100 % возврат денег в любой момент без объяснения причин.
> Скидка 30 % при оплате до конца месяца.
> Осталось 3 места в этом месяце.
> ```

**Assertions:**

1. At least one finding quotes the guarantee line verbatim («100 % возврат денег в любой момент без объяснения причин») and names a conditional guarantee (with key actions as conditions) or an anti-guarantee in place of an unconditional refund for a service with a high cost of fulfilment, citing 03.17, 03.19 or 03.20, or the construct's name.
2. At least one finding quotes the discount line («Скидка 30 % при оплате до конца месяца») and names the missing reason why, citing 03.28, 07.32 or the construct's name ("reason why").
3. Every finding has a severity mark, a verbatim quote from the material and a rule cited as `NN.M`; there are at most seven findings; the review ends with a verdict paragraph.
4. The scarcity line («Осталось 3 места в этом месяце») is not marked 🔴.
5. The answer attributes no results, prices, clients or services to the business that the material does not give.

---

## M-02. Review of an ad: an unknown bookkeeping brand leading with 50 % off to a cold, broad audience

**Embedded:** 06.24 (no offer-driven hook to a cold broad audience for an unknown brand), 06.5 / 06.6 / 06.3 (no callout; the audience is everyone; start with a puddle), 07.31 / 06.14 (the CTA "Learn More" to a homepage is incongruent with "sign up today" and does not show the next step), 07.32 (no reason why for the discount).

**User request (English):**

> Here's the ad we're about to launch for Ledgerly, our online bookkeeping service for small businesses. Nobody knows us yet, this is the first campaign. Tell me what's wrong with it before we spend the money.
>
> ```
> Audience: United States, 25–65, interest "small business". Placements: Facebook and Instagram feed. Budget: $150/day. New ad account.
>
> Primary text:
> 🔥 50% OFF your first 3 months of bookkeeping — this week only! Ledgerly does your books so you don't have to. Sign up today.
>
> Headline: Ledgerly — Bookkeeping Made Simple
> CTA button: Learn More → links to our homepage
> ```

**Assertions:**

1. A finding quotes the opening line ("50% OFF your first 3 months…") and names the problem of leading with an offer-driven hook to a cold, broad audience for a brand nobody knows, citing 06.24 or the rule in words (awareness, callout before the offer).
2. A finding names the missing callout or the audience being everyone (25–65, all of the US), quoting the audience line or the primary text and citing 06.5, 06.6, 06.7 or 06.3, or the construct's name ("callout").
3. A finding quotes the CTA ("Learn More" or "links to our homepage") and names the mismatch with the hook or the missing next step, citing 07.31, 06.14 or 06.13, or the rule in words.
4. Every finding has a severity mark, a verbatim quote from the material and a rule cited as `NN.M`; there are at most seven findings; the review ends with a verdict paragraph.
5. The answer attributes no click-through rate, cost per lead, conversion rate or business figure to the campaign or the company that the material does not give.

---

## M-03. Review of a sales call: the close of a $6,000 coaching program

**Embedded:** 09.21 (never ask "do you have any questions?"), 11.19 / 16.11 / 09.29 (the price of the same offer is not dropped in the moment; a payment plan or a trade instead), 09.27 (BAMFAM — the call ends with "let me know" and no next meeting), 09.25 ("I get it, but"), 09.6 (the closer talks 31 of 40 minutes against one fifth).

**User request (English):**

> This is the end of a sales call one of my closers had yesterday. It's for our $6,000 twelve-week coaching program. Where did he lose it?
>
> ```
> [12:40] CLOSER: So that's the program. Twelve weeks, weekly calls, the templates, the community. It's $6,000. Do you have any questions?
> [12:52] PROSPECT: Honestly, it's a lot. I'd need to think about it.
> [12:58] CLOSER: I get it, but you said yourself you've been stuck for two years. Think about what that costs you.
> [13:20] PROSPECT: I know. It's just the money right now.
> [13:26] CLOSER: OK, look — if you sign up today I can do $4,800. That's 20% off, only for today.
> [13:45] PROSPECT: Let me talk to my wife and I'll get back to you.
> [13:50] CLOSER: Sure, no problem. I'll send you the details by email and you can let me know. Talk soon!
> [13:55] — call ends. Closer talk time: 31 minutes of 40.
> ```

**Assertions:**

1. A finding quotes "Do you have any questions?" and names the rule against asking it, citing 09.21 or the rule in words.
2. A finding quotes the discount line ("$4,800" or "20% off, only for today") and says the price of the same offer is not lowered in the moment — a payment plan, a trade or a feature downsell instead — citing 11.19, 11.20, 11.17, 16.11 or 09.29, or the rule in words.
3. A finding quotes the ending ("I'll send you the details by email and you can let me know" or "Let me talk to my wife") and names booking the next meeting before the call ends — BAMFAM, cited as 09.27, 08.18, 11.4 or 14.24, or by name.
4. Every finding has a severity mark, a verbatim quote from the transcript and a rule cited as `NN.M`; there are at most seven findings; the review ends with a verdict paragraph.
5. The answer attributes nothing to the program, the closer's close rate or the prospect's situation beyond what the transcript says.

---

## M-04. Apply: rewrite a price-raise letter of a subscription accounting service

**Embedded:** 13.17 (the RAISE letter: value reminder, one direct sentence, investments, a loyalty reward, a PS for those affected), 13.18 / 16.18 (a raise justified by the company's own costs), 13.13 (grandfathering "бессрочно"), 13.14 (the raise tested on new customers first). The apply case: facts, prices and names carried unchanged; a derived number shown with its calculation.

**User request (Russian):**

> Перепиши это письмо о повышении цены, чтобы клиенты не разбежались. Контекст: мы — «Клауд-Бухгалтерия», подписка на бухгалтерское обслуживание для малого бизнеса, 180 клиентов на тарифе «Стандарт», письмо уходит всем действующим клиентам разом. Новых клиентов мы уже месяц подключаем по 15 600 ₽, они покупают нормально.
>
> ```
> Тема: Изменение стоимости обслуживания с 1 ноября
>
> Здравствуйте!
>
> С 1 ноября 2026 года стоимость абонемента «Стандарт» повышается с 12 000 ₽ до 15 600 ₽ в месяц. К сожалению, мы вынуждены пойти на этот шаг: за последний год выросли аренда, зарплаты и стоимость программного обеспечения.
>
> Для клиентов, которые с нами больше года, цена остаётся прежней бессрочно.
>
> Если у вас есть вопросы, обращайтесь в поддержку.
>
> С уважением,
> команда «Клауд-Бухгалтерия»
> ```

**Assertions:**

1. The answer contains the rewritten letter in full, preceded by a short diagnosis and followed by a list of changes in which at least one line cites a rule as `NN.M` (13.17, 13.13, 13.18, 16.18) or names the RAISE letter or its sections.
2. The rewritten letter keeps the facts unchanged: 1 ноября 2026, the plan «Стандарт», 12 000 ₽ and 15 600 ₽, the name «Клауд-Бухгалтерия»; if a percentage of the raise is given (30 %), it is shown with its calculation from 12 000 and 15 600.
3. The rewritten letter no longer justifies the raise by the company's own risen costs (rent, salaries, software) and no longer promises any client the old price indefinitely.
4. The rewritten letter states no fact the request does not give — no past results for the client, no named investments, no discount amount, no deadline — unless it is marked as a placeholder to fill (for example `[указать …]` or `[to clarify: …]`).
5. The rewritten letter states the change directly in one sentence and ends with an invitation for anyone materially affected to reply (the A and E sections of RAISE, 13.17 / 13.20).

---

## M-05. Review of a money model: a kids' coding school with a free trial class and nothing after it

**Embedded:** 01.18 / 01.19 / 01.21 (thirty-day gross profit $66 against CAC $150 — the customer does not pay for himself in thirty days), 01.11 (LTGP $330 to CAC $150 = 2.2:1, under 3:1), 01.13 (CAC counts every acquisition cost, the trial delivery included), 16.10 / 11.1 / 10.35 (one offer, no upsell, no downsell after a no), 12.10 / 13.2 / 14.15 (prepaid or annual options as a remedy).

**User request (English):**

> Here's how our kids' coding school (in-person, Saturday classes) makes money. Tell me what's broken.
>
> ```
> Front end: "First class free" — a Saturday trial lesson. It costs us $15 to deliver a trial. Ads: $2,400/month on Meta, 40 trials/month, 16 of them sign up.
> Main offer: monthly membership $120/month (4 classes), billed month to month, cancel anytime. Gross margin 55%. Average stay: 5 months.
> Nothing else is sold. If a parent says no after the trial, we email them a month later.
> ```

**Assertions:**

1. The answer computes CAC from the given numbers ($2,400 / 16 = $150, or including the trial delivery cost) and thirty-day gross profit per customer ($120 × 55 % = $66), shows the calculation, and states that the customer does not pay for himself in thirty days (01.18, 01.19, 01.21 or the standard in words).
2. The answer computes lifetime gross profit (5 × $66 = $330) and sets the ratio to CAC (about 2.2:1) against the method's 3:1 (01.11 or the ratio named).
3. A finding quotes "Nothing else is sold" or "we email them a month later" and names the missing upsell and the missing downsell after the no, citing 16.10, 11.1, 10.35, 11.17 or 11.29, or the constructs by name.
4. Every finding has a severity mark, a verbatim quote from the material and a rule cited as `NN.M`; there are at most seven findings; the review ends with a verdict paragraph.
5. The answer attributes no show rate, churn reason, price or cost to the school that the material does not give or that is not derived from it with the calculation shown.

---

## B-01. Boundary: a shrinking market — printer cartridge refilling

**Embedded:** 01.2 (the method assumes a normal market and does not repair a dying one), 01.1 (Starving Crowd first), 02.1 (the four indicators of a market, growing among them). The boundary answer comes first; no offer or ad plan for this market as the fix.

**User request (Russian):**

> У нас сервис по обслуживанию офисных принтеров и заправке картриджей, 4 точки в городе, 11 сотрудников. Рынок падает примерно на 15 % в год уже пять лет: офисы переходят на электронный документооборот и печатают всё меньше. Выручка падает третий год подряд, клиентов теряем быстрее, чем находим, два конкурента в городе за год закрылись.
>
> Помогите переделать наш оффер и рекламу, чтобы вернуть рост. Готовы вложиться в продвижение.

**Assertions:**

1. Before any advice on the offer or the ads, the answer states that the method assumes a normal, growing market and does not repair a shrinking one, citing 01.2, 01.1 or the construct's name (Starving Crowd, "a normal market").
2. The answer does not deliver an offer rewrite or an ad plan for this market as the fix; any step it gives concerns the choice of market (the four indicators, a niche in a growing need) or is explicitly conditional on the market verdict.
3. The answer names the four indicators of a market (massive pain, purchasing power, easy to target, growing) as the criterion for the next market, citing 02.1 or the indicators by name.
4. The boundary is stated in the first paragraph of the answer, and the answer has at most three steps, each with a rule number of the form `NN.M`.
5. The answer states no market figures beyond the request: no market size, no growth rate of an adjacent market, no competitor data.

---

## B-02. Boundary: hiring the first salesperson

**Embedded:** the scope line of the skill — hiring and management as a topic are out; the mechanics of removing the owner from sales are in (15.4, 15.5, 15.13, 09.2). No hiring rules or pay figures under the method's name.

**User request (English):**

> We're a six-person landscaping company doing about $1.4M a year. I do all the selling myself and I'm the bottleneck. How do I hire my first salesperson, and what should I pay them — base, commission, or both? What's a normal split?

**Assertions:**

1. The answer says that hiring as a topic — how to hire, what to pay, the base-versus-commission split — is outside the method the skill carries, and presents no compensation figures or hiring process as the method's rules.
2. Any advice given beyond that boundary is marked as general advice, not the method's; nothing outside the boundary carries a rule number of the form `NN.M`.
3. If the answer points at what the method does cover — the owner's self-inventory, documenting the sales process (document, demonstrate, duplicate), a word-for-word script — it cites those rules as `NN.M` (15.4, 15.5, 15.13, 09.2 or others of sheets 15 and 09).
4. The answer attributes no figures to the company that the request does not give (no close rate, ticket size, margin or pay benchmark stated as fact).

---

## B-03. Sound material: a postnatal fitness challenge offer with no embedded violation

**Embedded:** nothing. The offer follows the sheets: a M-A-G-I-C name (03.23), a conditional guarantee with key actions and a payout above money back (03.19), honest scarcity with the number and how close (03.4), cohort urgency (03.7), a named bonus with its price anchor (03.11), a reason why (03.28), a price above the market with the comparison stated (02.28). The threshold: no false 🔴.

**User request (English):**

> Review this offer for our small Pilates studio before we put it on the landing page. Be honest, what would you change?
>
> ```
> Riverside Moms — 6-Week Postnatal Core Rebuild Challenge
>
> For moms in Riverside 3–18 months postpartum who want their core strength back without leaving the baby for hours.
>
> What you get: 12 small-group sessions (max 6 per group), a 10-minute at-home daily routine on video, a weekly 15-minute check-in with your coach, and the "Back-to-Running" bonus plan (sold separately at $97) included free this round.
>
> Price: $597. Local studios charge $25–40 per class; this is not a class, it's a program with a measured result.
>
> Guarantee: attend 10 of the 12 sessions and log the daily routine at least 5 days a week. If at the end you can't hold a 60-second plank without doming, you get your $597 back and the next challenge free.
>
> Why the deal: we're opening the Tuesday/Thursday 10:00 group and want it full of moms who'll talk about it — that's why the bonus plan is included this round only.
>
> Spots: 12 per cohort, 9 taken as of today. Next cohort starts October 6; enrollment closes October 3.
> ```

**Assertions:**

1. No finding is marked 🔴.
2. The verdict says the material does its job (works, is sound, is ready) and names what to do first, if anything.
3. Every finding present has a verbatim quote from the material and a rule cited as `NN.M`; there are at most seven findings; the answer names at least one rule the material satisfies (for example 03.19, 03.4, 03.23, 03.28 or by the construct's name).
4. No finding claims the material lacks something it contains (a guarantee, a deadline, a reason why, a bonus, scarcity).
5. The answer does not mark the price ($597) as too high and does not recommend a discount.

---

## B-04. When not to apply: freemium for a video-editing service with salaried editors

**Embedded:** 16.3 / 10.30 (freemium only for software or media with near-100 % incremental margins, never for a service; an acquisition strategy, not a business model), 10.31 / 10.32 (the three requirements, the true cost of acquisition), the alternative for this business: a free or discount wrapper on the front end or another attraction offer (03.26, 03.27, 03.29, 10.22).

**User request (Russian):**

> У нас студия монтажа видео для блогеров: 6 монтажёров на зарплате, подписка 30 000 ₽ в месяц за 8 роликов. Сейчас клиент обходится нам в 9 000 ₽ рекламы, маржа на услуге 45 %. Хотим запустить freemium: первый ролик до 3 минут монтируем бесплатно всем, кто зарегистрируется на сайте, а дальше предлагаем подписку. Как правильно построить freemium, чтобы он окупался?

**Assertions:**

1. The answer says that freemium is for software or media with incremental margins near 100 % and not for a service delivered by salaried staff, citing 16.3, 10.30 or the rule in words, before or instead of building the freemium.
2. The answer names the alternative the method offers this business — a free or discount wrapper on the front end, or another attraction offer — citing 03.26, 03.27, 03.29, 10.22 or another rule of sheets 03 or 10 as `NN.M`.
3. No step of the answer builds the freemium as asked (a free edit for everyone who registers, then the subscription) under the method's name.
4. The boundary is stated in the first paragraph of the answer, and the answer has at most three steps, each with a rule number of the form `NN.M`.
5. The answer attributes no upgrade rate, conversion, servicing cost or other figure to the business that the request does not give (it gives 9 000 ₽ per customer, a 45 % margin, 30 000 ₽ a month, 8 videos, 6 editors).

---

## O-01. Off topic: a Python function that computes CAC crashes

**Embedded:** nothing; the skill must not apply. The word CAC in the code is the trap.

**User request (English):**

> This function is supposed to compute CAC per channel from a CSV but it crashes with `KeyError: 'spend'`. Can you fix it?
>
> ```python
> import csv
> from collections import defaultdict
>
> def cac_by_channel(path):
>     spend = defaultdict(float)
>     customers = defaultdict(int)
>     with open(path) as f:
>         for row in csv.DictReader(f):
>             spend[row['channel']] += float(row['spend'])
>             customers[row['channel']] += int(row['new_customers'])
>     return {ch: spend[ch] / customers[ch] for ch in spend}
> ```
>
> The CSV header is `channel,ad_spend,new_customers`.

**Assertions:**

1. The answer fixes the bug by reading the `ad_spend` column (it names the header mismatch) and gives corrected code.
2. The answer contains no rule number of the form `NN.M`, no method construct and no business advice about CAC thresholds, ratios or what to do with the ads.
3. The answer contains no diagnosis of the business and no findings with severity marks.
4. The answer does not ask for or invent business figures (an industry-average CAC, lifetime value, a ratio).

---

## O-02. Off topic: a clause of an office lease

**Embedded:** nothing; the skill must not apply. The clause is about a rent raise — the trap is the price-raise sheet.

**User request (Russian):**

> Проверь пункт договора аренды офиса: что тут не так и чем это грозит нам как арендатору?
>
> ```
> 5.4. Арендодатель вправе в одностороннем порядке изменять размер арендной платы не чаще одного раза в год, уведомив Арендатора за 10 (десять) календарных дней. В случае несогласия Арендатора с новым размером арендной платы Договор считается расторгнутым по инициативе Арендатора с удержанием обеспечительного платежа.
> ```

**Assertions:**

1. The answer treats the clause as a legal and contractual question (the notice period, the retention of the security deposit, the one-sided change) and names at least one risk to the tenant.
2. The answer contains no rule number of the form `NN.M` and does not apply the method's constructs (no price-raise letter, no offer or pricing advice, no review of "the business").
3. The answer does not treat the clause as a price raise of the user's own business.
4. The answer attributes no amounts, dates or parties to the lease that the clause does not give.

---

## TP-01. Trigger, positive: a yoga studio whose cost per lead rose, method not named

**Checks:** whether the description opens the skill when the method is not named. The agent gets the request and five skill descriptions (`hormozi` and four others) and decides which skill to open, without doing the task. Three runs, the position of `hormozi` changing.

**User request (Russian):**

> У нас студия йоги в спальном районе. За полгода стоимость заявки с рекламы выросла с 400 до 1 100 ₽, а записываются в итоге те же 15–20 человек в месяц, бюджет тот же. Что делать в первую очередь — менять рекламу или что-то ещё?

**Assertions:**

1. The agent decides to open the skill `hormozi`.
2. The agent does not choose any of the other four skills.
3. The explanation names the words of the request or the properties of the situation the decision rests on (cost per lead rising, ads, sign-ups, what to do first).

---

## TP-02. Trigger, positive: a bookkeeping firm afraid to raise its price, method not named

**Checks:** the same as TP-01, in English, on a pricing situation.

**User request (English):**

> We run a bookkeeping firm: $300 a month per client, 40 clients, we haven't changed the price in three years and we're at capacity. I'm nervous about raising it. Can you look at how we should do this without losing half the clients?

**Assertions:**

1. The agent decides to open the skill `hormozi`.
2. The agent does not choose any of the other four skills.
3. The explanation names the words of the request or the properties of the situation the decision rests on (raising the price, losing clients, at capacity).

---

## TN-01. Trigger, negative: a Telegram post to check before publishing

**Checks:** that the skill does not open on a text-editing request; the fitting skill is `glavred`.

**User request (Russian):**

> Глянь пост перед публикацией, через час выкладываю в канал.
>
> ```
> Три месяца учу английский по 20 минут в день. Не курсы, не репетитор — просто приложение и сериалы с субтитрами. Что изменилось: перестала бояться звонков на работе, начала понимать шутки в подкастах, а на прошлой неделе впервые поспорила с коллегой из Лондона и выиграла. Вывод простой: не нужен большой план, нужны 20 минут, которые вы не пропускаете.
> ```

**Assertions:**

1. The agent does not open the skill `hormozi`.
2. The explanation names why the request is not a business, marketing, sales or pricing situation, or names the skill that fits (`glavred`).

---

## TN-02. Trigger, negative: a system prompt for a support bot

**Checks:** that the skill does not open on a prompt-writing request; the fitting skill is `prompt-writer`.

**User request (English):**

> Write a system prompt for a support bot for our SaaS. It should answer billing questions, escalate refund requests to a human, and never promise delivery dates for features.

**Assertions:**

1. The agent does not open the skill `hormozi`.
2. The explanation names why the request is not a business situation for the method, or names the skill that fits (`prompt-writer`).

---

## TN-03. Trigger, negative: personal finance

**Checks:** that the skill does not open on personal finance, which its description excludes; no skill fits.

**User request (English):**

> I'm 34 with $40k in savings and a $22k student loan at 6.8%. Should I pay off the loan first or put the money into index funds?

**Assertions:**

1. The agent does not open the skill `hormozi`.
2. The agent opens none of the five skills, or names explicitly that personal finance is outside `hormozi`.

---

## TN-04. Trigger, negative: grades, KPIs and when to hire an HR manager

**Checks:** that the skill does not open on hiring and management as a topic, which its description excludes; no skill fits.

**User request (Russian):**

> У нас отдел из 12 человек, хочу ввести грейды и KPI и не понимаю, когда пора нанимать HR-менеджера. Как выстроить систему, чтобы люди понимали, за что им платят и как расти?

**Assertions:**

1. The agent does not open the skill `hormozi`.
2. The agent opens none of the five skills, or names explicitly that hiring and management as a topic are outside `hormozi`.

---

## Trigger tuning set

Used by the trigger-tuning procedure of the pipeline (`references/04-evals.md`, trigger tuning): 12 requests that should open the skill and 6 that should not, split into a tuning half and a held-out half. The description is tuned on the tuning half only, at most five iterations; the held-out half is run at the end, and the version of the description that does better on it is kept. The held-out half contains the six formal trigger cases above (TP-01, TP-02, TN-01 … TN-04) and four more positive requests. Tuning-half runs are batched: one agent gets the eight requests of the half in one prompt, decides for each request separately, and is run three times with the position of `hormozi` changing; the formal cases are run one request per agent.

**Tuning half, should open (6):**

- TU-P1 (Russian): «Продажи на созвонах падают: из 40 звонков в месяц закрываем 6, полгода назад закрывали 12. Скрипт тот же. Куда смотреть?»
- TU-P2 (English): "We're a dental clinic. Our new-patient offer isn't converting on the landing page — 'Free consultation + $99 cleaning for new patients'. What's wrong with it?"
- TU-P3 (Russian): «Клиенты уходят после первого месяца подписки, отток 18 % в месяц. Что делать, чтобы удерживать дольше?»
- TU-P4 (English): "Which should we do next: cold email or paid ads? We do about 60 warm DMs a day and post three times a week, and it's working but slowly."
- TU-P5 (Russian): «Есть 300 000 ₽ на рекламу, и их нужно окупить за месяц, иначе следующего бюджета не будет. Какой оффер запускать первым?»
- TU-P6 (English): "Review this Facebook ad copy for our roofing company: 'Storm damage? Get a free roof inspection this week — Denver homeowners only. Book online in 60 seconds.'"

**Tuning half, should not open (2):**

- TU-N1 (Russian): «Проверь пост для телеграм-канала нашего агентства перед публикацией: "Кейс: как мы за месяц снизили стоимость заявки клиенту в два раза. Делимся цифрами и ошибками, которых можно было избежать…"» — a text-editing request about a marketing topic; `glavred` fits.
- TU-N2 (English): "Write me a cold email template for a job application to a marketing agency, I'm a junior designer." — a personal job search, not a business situation.

**Held-out half, should open (6):** TP-01, TP-02, and:

- HO-P3 (Russian): «Мы агентство по настройке рекламы, а собственные лиды кончились: раньше приходили по рекомендации, теперь тишина. Что делать?»
- HO-P4 (English): "How do I structure a free trial so people actually convert to paid? It's a meal-prep subscription, $89 a week."
- HO-P5 (Russian): «Хочу продать компанию через два года, а сейчас всё на мне: продажи, найм, реклама. С чего начать?»
- HO-P6 (English): "Our cost per customer doubled in Q3 while the sales team's close rate stayed at 22%. Is it the ads or the sales team?"

**Held-out half, should not open (4):** TN-01, TN-02, TN-03, TN-04.

Tuning-half results, held-out results and every version of the description are recorded in `results.md`.
