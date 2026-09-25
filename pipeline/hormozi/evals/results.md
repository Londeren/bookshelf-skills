# Results of the eval run of the `hormozi` skill

The test programme is `eval-set.md` next to this file. Here: how it was measured, the summary against the thresholds, the trigger results, the pass over invented rules, the failures of the first run and their diagnosis, then for every case both outputs whole and the grader's verdict on every assertion, and at the end the rerun after the fixes. First run on 2026-09-25, on the `SKILL.md` audited by prompt-writer the same day (commit `903219e`); the rerun on the same day, on the fixed `SKILL.md`.

## How it was measured

For every case, two independent subagents (Opus) with a clean context, one per arm, the request identical word for word in both.

- **With the skill:** the agent's first action is to read a file with the verbatim body of `SKILL.md` and the absolute paths of the sixteen sheets; it opens the sheets itself by the routing table. The skill was not installed into the user's configuration: the plugin is not published yet.
- **Without the skill (the baseline):** only the request; not a word about the skill, the method, the author or a test; the agent is told not to read files and not to search the web.
- **The grader:** separate subagents with a clean context, the prompt verbatim from the pipeline's `references/04-evals.md` plus a wrapper for batches of three or four items; the verdict is JSON with a verbatim quote for every assertion; no quote, `passed: false`. Outputs were laid out in nine batches so that the two arms of one case never met one grader, and the arm was not marked.
- **Trigger cases TP-01, TP-02, TN-01 … TN-04:** the agent gets the request and five skill descriptions — `hormozi`, `glavred`, `prompt-writer`, `book-to-skill`, `karpathy-guidelines`, the real descriptions from the plugin cache — and decides which skill it opens, without doing the task; `hormozi` stood at positions 1, 3 and 5 of the list in the three runs of every case. No baseline.
- **The pass over invented rules:** a script matched every `NN.M` in the sixteen outputs with the skill against the `#### NN.M.` headings of the sheets; then five grader subagents received 371 pairs "the sentence of the answer citing the rule — the text of the rule" and answered whether the rule fits the place, with a quote from the rule.
- **The description tuning set:** the tuning half (six positive and two negative requests) was run as one batch per agent, three agents with `hormozi` at three positions; the held-out half is the six formal trigger cases, one agent per run, plus four more positive requests run as a batch three times.

Agent runs of the phase: 32 case runs, 9 graders, 5 rule-fit graders, 3 tuning runs, 18 formal trigger runs, 3 held-out runs, 5 rerun case runs, 2 rerun graders — 77 in all, every one on Opus; the build as a whole, phases 0–4, used 167 runs.

## Summary

| case | with skill | baseline | delta |
|---|---|---|---|
| S-01 | 5/5 | 1/5 | +80 pp |
| S-02 | 5/5 | 1/5 | +80 pp |
| S-03 | 3/5 | 0/5 | +60 pp |
| S-04 | 5/5 | 3/5 | +40 pp |
| S-05 | 5/5 | 2/5 | +60 pp |
| M-01 | 5/5 | 1/5 | +80 pp |
| M-02 | 5/5 | 4/5 | +20 pp |
| M-03 | 5/5 | 3/5 | +40 pp |
| M-04 | 4/5 | 1/5 | +60 pp |
| M-05 | 4/5 | 2/5 | +40 pp |
| B-01 | 5/5 | 1/5 | +80 pp |
| B-02 | 4/4 | 0/4 | +100 pp |
| B-03 | 5/5 | 3/5 | +40 pp |
| B-04 | 4/5 | 2/5 | +40 pp |
| O-01 | 4/4 | 4/4 | +0 pp |
| O-02 | 4/4 | 4/4 | +0 pp |
| **Total, 77 assertions** | **72/77 = 93.5 %** | **32/77 = 41.6 %** | **+51.9 pp** |

By type: S 23/25 against 7/25; M 23/25 against 11/25; B 18/19 against 6/19; O 8/8 against 8/8. The two off-topic cases score the same in both arms by design (the assertions there check that the method is not applied, which the baseline cannot fail), so without them the picture is: with the skill 64/69 = 92.8 %, baseline 24/69 = 34.8 %, delta +58.0 pp.

### Thresholds

Set in `eval-set.md` before the first run and not moved.

| threshold | requirement | fact | result |
|---|---|---|---|
| With the skill | ≥ 80 % | 93.5 % (72/77) | passed |
| Delta over the baseline | ≥ 20 pp | +51.9 pp | passed |
| Baseline | < 70 % | 41.6 % (32/77) | passed |
| Zero invented rules, existence | every `NN.M` exists in the sheets | 372 references in 16 outputs, 0 not in the sheets | passed |
| Zero invented rules, fit | every `NN.M` fits the finding or step it stands at | 371 pairs graded; the graders flagged 11 on the single-sentence view; all 11 stand in steps whose heading cites several rules and whose body covers each of them, and each fits on reading the whole step (listed below); 0 misplaced numbers | passed, with the graders' raw count stated |
| Zero invented facts in the apply case (M-04) | 0 | 1: the rewritten letter set a loyalty discount schedule (3 600 ₽ for three months, then 1 800 ₽ for three, with dates) that the request does not give; the amounts were derived from the two prices with the calculation shown, the term was chosen for the user | **not passed** in the first run; fixed and rerun, see the rerun section |
| Sound material (B-03) without a false 🔴 | 0 🔴 | 0 🔴, 4 🟡, 1 🟢; verdict "the offer works" | passed |
| Triggers TP-01, TP-02 | ≥ 5 of 6 runs open `hormozi` | 6 of 6 | passed |
| Triggers TN-01 … TN-04 | 12 of 12 runs do not open `hormozi` | 12 of 12 | passed |

### Triggers

The description was not changed: the tuning half came back clean on the first iteration, so there was nothing to tune, and the held-out half was run on the same text. One version of the description exists, the one committed in `903219e`.

| set | requests | runs | correct |
|---|---|---|---|
| Tuning half, should open (TU-P1 … TU-P6) | 6 | 3 each, batched | 18 of 18 opened `hormozi` |
| Tuning half, should not open (TU-N1, TU-N2) | 2 | 3 each, batched | 6 of 6: TU-N1 opened `glavred`, TU-N2 opened none |
| Held-out, formal positive (TP-01, TP-02) | 2 | 3 each, one agent per run | 6 of 6 opened `hormozi`, never a distractor, the explanation named the words of the request |
| Held-out, formal negative (TN-01 … TN-04) | 4 | 3 each, one agent per run | 12 of 12 did not open `hormozi`: TN-01 opened `glavred` three times, TN-02 `prompt-writer` three times, TN-03 and TN-04 none |
| Held-out, extra positive (HO-P3 … HO-P6) | 4 | 3 each, batched | 12 of 12 opened `hormozi` |

Formal cases by run, with the position of `hormozi` in the list:

| case | run 1 (pos. 1) | run 2 (pos. 3) | run 3 (pos. 5) |
|---|---|---|---|
| TP-01 | hormozi | hormozi | hormozi |
| TP-02 | hormozi | hormozi | hormozi |
| TN-01 | glavred | glavred | glavred |
| TN-02 | prompt-writer | prompt-writer | prompt-writer |
| TN-03 | none | none | none |
| TN-04 | none | none | none |

The negatives were all clear-cut; the sharper negative of the tuning half, TU-N1 (a Telegram post about a marketing case, "проверь пост перед публикацией"), went to `glavred` three times out of three. What the trigger runs did not test: a request that is a business situation but belongs to another installed skill more strongly, and requests in a third language.

### The pass over invented rules

Every rule reference in the sixteen outputs with the skill was collected by script (`NN.M` with the sheet number in 01–16, percentages and prices excluded) and matched against the `#### NN.M.` headings of the sheets: **372 references, 0 numbers that do not exist**. The O cases carry none; the smallest count is 14 in B-01, the largest 44 in M-02.

The fit pass: 371 pairs "the sentence of the answer citing the rule — the rule text" were graded by five subagents; 360 fit on the sentence alone, 11 were flagged. All 11 sit in steps of S-03, B-02, M-03 and M-05 whose first sentence cites several rules in its heading — "(15.5, 15.6)", "(15.7, 15.8, 15.9)", "(01.23, 10.35 Step 2, 10.37, 10.1)", "(10.7, 10.35, 01.25)", "(09.17, 09.18)" — and whose following sentences carry the content of each rule: the green-yellow-red order of 15.6 ("Раскрасьте пункты: green … Отдавайте от зелёных к красным"; "Hand off the greens first"), the if-this-then-that rules and money box of 15.7, the scorecard and the 80 % test of 15.8, the hours moved from doing to managing of 15.9, the ladder of 15.10, the Problem → Solution → Assure → Benefit → Confirm map of 09.18 in the sentence before, the "sell more immediately" of 01.23, the Step 2 upsell of 10.35 and its "one offer at a time" caveat, and 10.7's "one conversion opportunity at a time, starting with whichever brings in the most money for the least cost", which the step repeats almost word for word. The pair files split the answers into sentences, so the graders saw the heading without its body; on the whole step every one of the 11 fits. Misplaced numbers: 0. The graders' raw count, 11 of 371 (3.0 %), is kept in the table above so the reading is checkable, and the pair files stay in the build's working directory.

### Failures of the first run and their diagnosis

Five assertions failed with the skill, in four cases. Each was read against the troubleshooting table of `references/04-evals.md` and the sheet map.

1. **S-03, assertion 2** — the answer cited the video source on every rule ("15.10, видео 2025") but never said in one line that the enterprise-value material rests on transcripts and weighs less than the books. The caveat stands in the opening paragraph of sheet 15, which the agent read; `SKILL.md` had no output rule asking for it in the answer. Diagnosis: the rule is in the sheet, the answer did not apply it; the fix is an output rule in `SKILL.md`.
2. **S-03, assertion 3** — the grader read "Платите ему override, долю прибыли или долю в компании" as a pay prescription. That sentence is rule 15.22 itself (the operator paid an override, a profit share or stock in exchange for the phone not ringing), inside the owner-removal mechanics that the build's scope line keeps in. The assertion was written too broadly and collides with the sheet; no defect of the skill, no fix. Recorded as an assertion flaw.
3. **M-04, assertion 4** — the rewritten letter set a loyalty discount schedule with amounts and dates; the amounts follow from the two prices by a calculation the answer shows, the term and the stair-step were chosen for the user, and the assertion asked for a placeholder. `SKILL.md` said "what is missing is marked, not invented, and a derived number is shown with its calculation", which the answer obeyed; it did not say that a value the method leaves to the user's choice stays a placeholder. Diagnosis: a gap in the apply rule of `SKILL.md`; the fix is one sentence there, duplicated in the output rules.
4. **M-05, assertion 4** — the answer used the advisor's form (a diagnosis paragraph, three steps, `[to clarify]`) on a written money model, so the findings carried no severity marks and the review had no verdict paragraph; every other assertion of the case passed. The material test of `SKILL.md` ("is there a text to quote?") plus the tie-breaker "when in doubt, a situation" let a block of numbers pass as a situation. Diagnosis: the routing rule exists (a money model is listed as a material), the entry test did not catch it; the fix is a sharper test in `SKILL.md`.
5. **B-04, assertion 3** — after stating the boundary (freemium is for software or media) and naming the method's alternative (a free front end as an Attraction Offer with a Decoy, the Two-Step Sale, Honest Scarcity and Free Money Math friction), the answer's first step kept a free three-minute edit for registrants, and the grader read that as building the freemium as asked. The answer renamed it, cut it off from "everyone who registers" by qualifying questions and a weekly cap, and put the cost of the free edit into CAC; the method's own alternative for this business (03.26, 03.27, 03.29) is a free or discounted front end with friction, which is what the answer built. No defect of the skill found; recorded as a strict reading of the assertion, and rerun for variance.

Fixes made to `SKILL.md` after the first run, all three in the register of how the agent applies the method, none adding a rule, a threshold or an example of the method:

- the entry test of the diagnosis: "did the user paste something to check: an offer, an ad, a script, a price list, a nurture sequence, or a money model written out as offers, prices, costs and take rates? A pasted thing is a material and is quoted, a written money model included; a story told in prose with nothing pasted is a situation" (for M-05);
- the apply rule, duplicated in the output rules: "a value the method leaves to the user's choice — the size and term of a loyalty discount, a deadline, a bonus, an investment to name — enters the rebuilt material as a placeholder with the rule's range next to it, not as a figure chosen for the user; a figure is written only when it follows from the request's numbers by a calculation shown next to it" (for M-04);
- the output rules: "an answer that rests on the enterprise-value sheet says in one line, in every mode, that its material comes from video transcripts — oral speech from auto-captions, some elements said once — and weighs less than the books" (for S-03).

No sheet was changed, no unit restored from the rejected set, and the description was not changed.

---

## S-01. Not enough leads: outsourced accounting, CAC at four times the industry average

### Request

> Мы — аутсорсинг бухгалтерии для малого бизнеса, работаем по всей России удалённо. Проблема: мало лидов, и те, что есть, дорогие. Цифры за последние три месяца:
>
> - Реклама: Яндекс Директ + холодные письма, всего 480 000 ₽ в месяц на всё привлечение (бюджет, подрядчик, зарплата менеджера по холодным письмам).
> - Заявок 120 в месяц, до созвона доходит 40, покупают 8. То есть один новый клиент обходится нам в 60 000 ₽.
> - Я спрашивал у трёх агентств и у знакомых из отрасли: у них клиент на бухобслуживание обходится в 12–18 тысяч.
> - Средний клиент платит 25 000 ₽ в месяц, наша валовая маржа 60 %, держится в среднем 6 месяцев.
> - Кто приходит: в основном ИП без сотрудников, которым нужна «бухгалтерия за 3 000 ₽», а у нас тариф от 25 000. Половина созвонов заканчивается словами «дорого, мне бы попроще».
>
> Что делать? Мне советуют увеличить бюджет на Директ в два раза.

### Output with the skill

###### Диагноз

Лидов не мало — 120 в месяц; мало тех, кто может заплатить вашу цену. Приходят, по вашим словам, в основном ИП без сотрудников, которым нужна бухгалтерия за 3 000 ₽, при тарифе от 25 000 ₽: у этой аудитории нет покупательной способности, а это один из четырёх признаков рынка, провал по которому не перекрывают остальные три (02.1). CAC 60 000 ₽ — это 3,3–5 средних по отрасли (60 000 / 18 000 и 60 000 / 12 000), выше порога в три средних (01.14, $100M Leads 2023), и при таком CAC метод задаёт один вопрос: есть ли у лидов проблема, которую вы решаете, и деньги на её решение (01.16)? Денег нет — половина созвонов кончается словами «дорого, мне бы попроще», значит, это проблема рекламы, а не продаж. Экономика клиента это подтверждает: валовая прибыль за жизнь 25 000 × 60 % × 6 мес. = 90 000 ₽, LTGP:CAC = 90 000 / 60 000 = 1,5:1 при ориентире выше 3:1 (01.11, $100M Leads 2023; сам автор оговаривает: «a pattern I personally observed, not a rule»). Первый месяц приносит 15 000 ₽ валовой прибыли, четверть CAC, и затраты на привлечение возвращаются через 60 000 / 15 000 = 4 месяца из шести. Это первый уровень Customer Financed Acquisition (01.20, Lost Chapters 2025), на котором, по оговорке автора, зарабатывать можно, только если своих денег уже много; порог «хорошей» модели — прибыль первых 30 дней выше стоимости привлечения и обслуживания — не пройден (01.21, Money Models 2025). Удвоение Директа при том же таргетинге приведёт больше тех же ИП за 3 000 ₽ и увеличит сумму, которая возвращается только через четыре месяца; тратить на рекламу столько, сколько можешь, метод ставит последним этапом, после того как клиенты надёжно окупают себя (01.25). Опускать цену к рынку в ответ на «дорого» тоже не выход: конкурировать ценой метод разрешает, только если ваши издержки в десять раз ниже, чем у конкурентов (02.26).

###### Три шага

1. Выведите аватар из лучших текущих клиентов: опросите их, возьмите верхние 20 % — тех, кого больше цените, кто больше платит и дольше остаётся, — и выпишите 3–5 признаков, общих для всех (02.4, Lost Chapters 2025).
2. Эти требования — прямо в объявления Директа, в холодные письма и до записи на созвон; тем, кто их не проходит, не продавайте, а бюджет переведите в канал, откуда приходят подходящие клиенты (02.5; автор предупреждает, что первое время клиентов станет меньше, а искать надо не максимум фильтров, а число шагов квалификации с лучшей отдачей от рекламы на длинной дистанции).
3. Бюджет увеличивайте не раньше, чем CAC, посчитанный по каждому каналу помесячно (01.13), войдёт в три отраслевых средних — ниже 36 000–54 000 ₽ по вашим данным (12 000 × 3, 18 000 × 3); дальше рычаг — деньги с клиента (01.14): 15 000 ₽ первого месяца даже при отраслевых 12–18 тыс. дают 0,8–1,25 CAC (15 000 / 18 000, 15 000 / 12 000) против рабочего стандарта 2x (01.19, Lost Chapters 2025), и добирать это нужно продажей большего в первые 30 дней, а не дальнейшим снижением CAC (01.23).

###### Что не удалось проверить

- Сколько из 40 созвонов в месяц было с теми, кто может платить 25 000 ₽, и сколько из них купили? Если подходящие покупают, ограничение в рекламе, и шаг 2 его снимает; если и они не покупают, это проблема продаж (01.16), и работать надо над созвоном, а не над рекламой.
- [уточнить: откуда пришли 8 покупателей в месяц — из Директа или из холодных писем, и CAC каждого канала отдельно] — без этого шаг 2 не знает, какой канал усиливать, а какой урезать.
- [уточнить: входят ли в 12–18 тыс. у агентств все затраты — подрядчик, зарплаты, — как в ваших 60 000 ₽, и сколько в месяц платят их клиенты] — на этом держится сравнение с тремя отраслевыми средними (01.14).

### Baseline output

**Коротко:** удваивать бюджет на Директ сейчас не стоит. Лидов вам хватает, но реклама приводит не тех людей: вы продаёте услугу за 25 000 ₽ тем, кто ищет бухгалтерию за 3 000 ₽. Если удвоить бюджет, таких людей придёт вдвое больше, а каждая следующая заявка обойдётся дороже, потому что ставки в аукционе растут. Сначала нужно изменить, кого вы привлекаете и сколько времени клиент у вас остаётся. Масштабировать стоит потом.

##### Что говорят ваши цифры

| Показатель | Значение |
|---|---|
| Стоимость заявки | 480 000 / 120 = 4 000 ₽ |
| Заявка → созвон | 40 / 120 = 33 % |
| Стоимость созвона | 12 000 ₽ |
| Созвон → покупка | 8 / 40 = 20 % |
| Стоимость клиента (CAC) | 60 000 ₽ |
| Валовая прибыль с клиента в месяц | 25 000 × 60 % = 15 000 ₽ |
| Валовая прибыль за жизнь клиента (6 мес.) | 90 000 ₽ |
| Валовая прибыль за жизнь клиента к CAC | 1,5 : 1 |
| Окупаемость привлечения | 4 месяца из 6 |

Отсюда три вывода.

1. **Вы в плюсе, но совсем небольшом.** С клиента остаётся 30 000 ₽ за полгода. Затраты на его привлечение окупаются только к концу четвёртого месяца, прибыль приносят последние два. Здоровый ориентир: валовая прибыль за жизнь клиента хотя бы втрое больше CAC. Для вас это значит либо CAC около 30 000 ₽, либо клиент, который остаётся на 12 месяцев вместо 6.
2. **Воронка ломается на входе, а не в продажах.** Половина созвонов заканчивается словом «дорого», то есть примерно 20 разговоров из 40 были бесполезны с самого начала. Из оставшихся 20 покупают 8, это 40 %, и для бухобслуживания такая конверсия нормальная. Продажи работают, просто им дают не тех людей. Ещё 80 заявок из 120 не доходят даже до созвона. Скорее всего, среди них тоже много ищущих за 3 000, но стоит проверить и то, как быстро менеджер перезванивает на заявку.
3. **Сравнение с 12–18 тысячами, скорее всего, некорректно.** Уточните у тех, с кем сравниваете, что входит в их цифру: только рекламный бюджет или ещё зарплаты и подрядчик, как у вас. И сколько платит их клиент. Если он платит 5 000 ₽ в месяц, то CAC в 15 000 равен трём месяцам его выручки, а ваши 60 000 равны 2,4 месяца. Стоимость клиента нужно сравнивать с тем, сколько он приносит, а не в абсолютных рублях.

##### Почему удвоение Директа не поможет

- Придёт больше таких же людей: ИП без сотрудников, которые ищут подешевле. Доля ответов «дорого» останется прежней.
- Бюджет в Директе даёт отдачу нелинейно. На вторую половину бюджета вы покупаете клики дороже и по менее целевым запросам, так что CAC скорее вырастет, чем останется на 60 000.
- Вы не знаете, какой из двух каналов приводит клиента дешевле. Ваши 480 000 ₽ складываются из бюджета Директа, оплаты подрядчику и зарплаты менеджера по письмам. Может оказаться, что клиент из Директа стоит 40 000, а из писем 150 000, или наоборот. Пока нет разбивки по каналам, удвоение делается вслепую.
- Привлечение окупается за 4 месяца, поэтому каждый дополнительный рубль в рекламе на несколько месяцев вперёд увеличивает кассовый разрыв.

##### Что делать вместо этого

###### 1. Выясните, кто у вас на самом деле покупает (первая неделя)

- Выгрузите клиентов за последние 6–12 месяцев. По каждому нужны форма бизнеса (ИП или ООО), налоговый режим, число сотрудников, отрасль, оборот, источник, чек и срок, который клиент у вас пробыл.
- Разделите расходы и результаты по каналам. Для Директа и для холодных писем отдельно посчитайте заявки, созвоны, клиентов и CAC.
- Позвоните 5–10 ушедшим клиентам и спросите, почему они ушли.

Так вы получите портрет клиента, который платит 25 000 и остаётся надолго. Моя гипотеза: это ООО с сотрудниками на ОСНО или на УСН с НДС, у которых есть зарплата, кадры, ВЭД или маркетплейсы. У таких компаний объём работы оправдывает вашу цену. Проверьте её на своих данных.

###### 2. Перестройте рекламу под этот портрет и отсеивайте остальных до созвона

- Укажите цену в объявлении и на сайте: «от 25 000 ₽ в месяц». Заявок станет меньше, зато ищущие за 3 000 отсеются сами и перестанут тратить бюджет и время менеджера.
- Добавьте минус-слова: «дешево», «недорого», «ИП без сотрудников», «нулевая отчётность», «за 3000», «бесплатно» и похожие. Посмотрите, по каким запросам пришли заявки, которые закончились словом «дорого».
- Обращайтесь к целевому клиенту напрямую: «бухгалтерия для ООО с сотрудниками», «для селлеров маркетплейсов», «для IT-компаний». Узкие формулировки обычно дают клик дешевле и конвертируют лучше, чем общее «бухгалтерское обслуживание».
- Добавьте в форму заявки 2–3 вопроса: форма бизнеса, число сотрудников, примерный оборот или число операций в месяц. Созванивайтесь только с подходящими.

Успех оценивайте не по числу заявок, а по стоимости клиента и по доле ответов «дорого» на созвонах.

###### 3. Зарабатывайте на тех, кто всё равно придёт за дешёвым

ИП без сотрудников будут приходить всегда. Сейчас вы платите за их заявки и ничего с них не получаете. Есть два варианта:

- Передавать их по партнёрской программе. Такие программы есть у многих онлайн-сервисов бухгалтерии и у банков, они платят вознаграждение за приведённого клиента.
- Завести отдельный простой тариф для ИП, но только если его можно обслуживать почти без ручной работы. Иначе он съест маржу и время бухгалтеров.

Даже 3–5 тысяч рублей с каждого такого лида заметно снижают реальную стоимость привлечения.

###### 4. Удлините срок жизни клиента: это самый дешёвый рычаг

Шесть месяцев для бухобслуживания мало. Менять бухгалтера хлопотно, поэтому довольные клиенты обычно остаются годами. Если клиент будет оставаться 12 месяцев, валовая прибыль с него вырастет до 180 000 ₽. Тогда даже при нынешнем CAC в 60 000 соотношение станет 3 : 1, и в рекламе ничего менять не придётся.

- Выясните причины ухода (см. п. 1). Возможно, часть ушедших тоже не могли толком позволить себе вашу цену: купили, а через полгода нашли дешевле. Тогда отбор на входе улучшит и удержание.
- Предложите оплату за квартал или за год вперёд со скидкой. Это удерживает клиента и закрывает кассовый разрыв.
- Сделайте переход к вам платным: аудит и восстановление учёта как отдельная услуга. Она окупает часть CAC уже в первый месяц.

###### 5. Добавьте более дешёвые каналы

- Рекомендации нынешних клиентов. Платите за каждого приведённого клиента, например, сумму одного месяца обслуживания. Это 25 000 ₽, в два с лишним раза меньше нынешнего CAC, и такие клиенты обычно лучше вам подходят.
- Партнёры, к которым уже приходят ваши клиенты: юристы, регистраторы бизнеса, банки с расчётно-кассовым обслуживанием, внедренцы 1С и CRM, консультанты по маркетплейсам. Партнёру платите процент с первых месяцев обслуживания.
- Холодные письма нацельте на базу ООО нужного размера и отрасли и давайте в них конкретный повод. Например, бесплатную экспресс-проверку учёта на налоговые риски.

##### Когда увеличивать бюджет

Увеличивайте бюджет, когда после перестройки CAC опустится примерно до 30 000 ₽ или когда клиенты станут оставаться достаточно долго, чтобы валовая прибыль за их жизнь втрое превышала CAC. Поднимайте бюджет того канала, где клиент дешевле, шагами по 20–30 %, и после каждого шага смотрите, во что обходится каждый дополнительный клиент. Если дополнительный клиент дорожает, останавливайтесь на этом уровне.

##### План на ближайшие два месяца

1. Неделя 1: разбивка по каналам, портрет покупателей, звонки ушедшим клиентам.
2. Недели 2–3: новые объявления с ценой и нишей, минус-слова, квалификация в форме заявки, партнёрская программа для ИП.
3. Недели 3–4: программа рекомендаций, предоплата за квартал или год, платный вводный аудит.
4. Недели 5–8: сравнение CAC, доли ответов «дорого» и конверсии со старыми цифрами, после этого решение о бюджете.

### Grader verdicts

| # | assertion | with skill | baseline |
|---|---|---|---|

| 1 | The answer states the ratio of the business's CAC to the industry average (four times 15 000 ₽, or "above 3×") and says that by that comparison the lever is the advertising, not the business model (01.14 or the same rule in words). | ✅ «CAC 60 000 ₽ — это 3,3–5 средних по отрасли (60 000 / 18 000 и 60 000 / 12 000), выше порога в три средних (01.14, $100M Leads 2023) [...] значит, это проблема рекламы, а не продаж. [...] Бюджет увеличивайте не раньше, чем CAC, посчитанный по каждому каналу помесячно (01.13), войдёт в три отраслевых» | ❌ «**Сравнение с 12–18 тысячами, скорее всего, некорректно.** Уточните у тех, с кем сравниваете, что входит в их цифру» |

| 2 | Before any advice on the ads or the budget, the answer puts the one question — do the engaged leads have the problem the business solves and the money to spend — and names the branch it lands on (leads not qualified → an advertising problem), citing 01.16 or the question in its own words. | ✅ «при таком CAC метод задаёт один вопрос: есть ли у лидов проблема, которую вы решаете, и деньги на её решение (01.16)? Денег нет — половина созвонов кончается словами «дорого, мне бы попроще», значит, это проблема рекламы, а не продаж.» | ❌ «**Коротко:** удваивать бюджет на Директ сейчас не стоит. Лидов вам хватает, но реклама приводит не тех людей» |

| 3 | The answer computes lifetime gross profit from the given numbers (25 000 × 60 % × 6 = 90 000 ₽) and sets the ratio to CAC (1.5:1) against the method's 3:1 (01.11 or the ratio named). | ✅ «валовая прибыль за жизнь 25 000 × 60 % × 6 мес. = 90 000 ₽, LTGP:CAC = 90 000 / 60 000 = 1,5:1 при ориентире выше 3:1 (01.11, $100M Leads 2023» | ✅ «\| Валовая прибыль за жизнь клиента (6 мес.) \| 90 000 ₽ \| ... \| Валовая прибыль за жизнь клиента к CAC \| 1,5 : 1 \| ... Здоровый ориентир: валовая прибыль за жизнь клиента хотя бы втрое больше CAC.» |

| 4 | The answer has a diagnosis paragraph and at most three steps, each step with a rule number of the form `NN.M`. | ✅ «### Диагноз [...] ### Три шага [...] выпишите 3–5 признаков, общих для всех (02.4, Lost Chapters 2025). [...] (02.5; автор предупреждает [...] посчитанный по каждому каналу помесячно (01.13)» | ❌ «### 4. Удлините срок жизни клиента: это самый дешёвый рычаг ... ### 5. Добавьте более дешёвые каналы» |

| 5 | The answer attributes no figures, services or results to the business that the request does not give (no invented conversion rates, churn, prices of competitors, or a doubled budget outcome). | ✅ «[уточнить: откуда пришли 8 покупателей в месяц — из Директа или из холодных писем, и CAC каждого канала отдельно] — без этого шаг 2 не знает, какой канал усиливать, а какой урезать.» | ❌ «Если удвоить бюджет, таких людей придёт вдвое больше, а каждая следующая заявка обойдётся дороже, потому что ставки в аукционе растут. ... Из оставшихся 20 покупают 8, это 40 %, и для бухобслуживания такая конверсия нормальная.» |



## S-02. Ads stopped paying back: a nursing exam-prep course after a 5× scale-up

### Request

> We sell an online prep course for the nursing licensing exam. The course is $397 one-time; after buying, students can join a $79/month study membership, and most do — the average member stays 20 months. Our gross margin is about 85% on both.
>
> Meta ads worked well from January to June: about $150 per customer at $300/day. In July we pushed the daily budget to $1,500 to grow faster. Since then cost per customer has crept up to $420 and it's still rising. CPMs are flat, but the click-through rate fell from 1.8% to 0.7%. We've been running the same three video ads since February, they were the winners. My media buyer says the audience is saturated and wants to expand targeting to all of the US and add lookalikes from the email list.
>
> What's actually wrong and what do we do first?

### Output with the skill

**Diagnosis.** The constraint is the creative, not the audience. With CPM flat, the drop in CTR from 1.8% to 0.7% by itself makes each click 2.57x as expensive (1.8 ÷ 0.7). Cost per customer rose 2.8x ($420 ÷ $150), so nearly all of the rise happens before the click and only about 8% after it (2.8 ÷ 2.57 = 1.09). Spend that was profitable and stops being profitable as you scale it is the case of 06.22 (GOATed Ads playbook, 2025): refresh the creative first, and widen the audience only after that has been done. In the method's reading, you have taken the low-hanging fruit; you have not saturated the platform. Your media buyer reads it as an audience problem, which is rule 06.4 (check reach before copy), but 06.4 withdraws itself for spend that was profitable and stopped being profitable as it scaled. The playbook's own example is the same pattern at a larger size: a founder who made about five new ads a month called his market saturated when CAC shot up past $5–8k a day in ad spend. He went to 150 ads a week and doubled the company in two quarters (06.19). Nothing in your numbers points higher up, at the market or the offer, because the same offer sold at $150 for six months. When a working offer's lead flow drops, the creative changes first and the offer and its price change last (01.27, $100M Offers, 2021). What the higher CAC has broken is the thirty-day test (01.18, $100M Leads, 2023). First-month gross profit is $337.45 ($397 × 85%), or $404.60 with one membership month added ($79 × 85% = $67.15). That was 2.25–2.70x a $150 CAC, above the 2x "real life" minimum of 01.19 (Lost Chapters, 2025). Against $420 it is 0.80–0.96x, below the 1x floor, so each new customer now costs more than he returns in thirty days and cash becomes the constraint on growth. The same arithmetic shows what the budget jump bought: $300 × 30 ÷ $150 = 60 customers a month then, and $1,500 × 30 ÷ $420 ≈ 107 now, 1.8x the customers for 5x the spend.

**What to do first**

1. **This week, make new versions of the three winners instead of replacing them.** The method is the Ad Kaleidoscope (07.1, ACQ Advertising Handbook, 2025): 80% of the effort on versions of winners, 20% on new ideas. Remixes cut from the footage you already have go up first: a new speed, new captions, a new headline, a static image of the hook, a different meat under the winning hook (07.3). At the same time, re-record the same scripts with new examples, a new setting or new talent (07.4). Keep each original running while it still performs (07.5).
2. **From then on, make ads in parts every week** with the Ad Assembly Process (06.19, GOATed Ads playbook, 2025): 50 hooks, 3–5 meats and 1–3 CTAs, combined into 150 to 750 ads. Spend 80% of the prep time on hooks (06.20), and take the hooks first from your own previous winners (06.21).
3. **Judge the refresh by cost per customer over four tries or one month (01.8, $100M Leads, 2023).** Under $337.45 passes 01.18. $168.73 or less meets the 2x of 01.19 ($337.45 ÷ 2), or $202.30 if a membership month falls inside the thirty days. Your media buyer's plan comes after the refresh, in the order 06.22 sets: expansion hooks matched to the colder audience's level of awareness (06.23), and a lookalike built from current and past customers first rather than from the whole email list (06.2). Rule 06.3 does allow a bigger audience once a small one is profitable. It also expects the ratio of spend to sales to get worse as the audience grows, which is acceptable only where you can afford the higher spend.

**What I could not check**

- What share of course buyers join the membership, and is the first $79 charged inside the first thirty days? A member's LTGP is $337.45 + 20 × $67.15 = $1,680.45, which is 4.0:1 against $420. Averaged over all buyers, the ratio stays above 3:1 only if at least 69% join (($1,260 − $337.45) ÷ $1,343). The 3:1 comes from 01.11 ($100M Leads, 2023), with the author's own caveat: "This is a pattern I personally observed, not a rule."
- [to clarify: whether the $150 and $420 are Meta spend only] Rule 01.13 counts every acquisition cost, including the media buyer's pay and creative, so the real CAC and the thirty-day gap may be larger.
- [to clarify: the industry-average CAC for nursing-exam prep] Rule 01.14 picks the lever by it: above 3x the average, the work goes to the ads; within 3x, it goes to LTGP through the money model (sheets 10–13). If CAC stays above first-month gross profit after the refresh, that gap is the case of 01.23 ($100M Leads, 2023): when LTGP exceeds CAC but the first thirty days do not cover it, sell the customer more right away, rather than waiting for lifetime profit or lowering CAC.

### Baseline output

**Short answer:** your audience isn't worn out. Your three ads are. The audience is saturated only in the sense that it has seen those three videos too many times. Expanding the targeting treats the symptom. The first fix is new creative, and while you make it, stop putting $1,500 a day behind the old three.

##### What the numbers say

Your cost per customer breaks down into three parts:

**CAC = CPM ÷ (1,000 × CTR × conversion rate after the click)**

- **CPM is flat.** The auction hasn't gotten more expensive, so media cost isn't the problem.
- **CTR fell from 1.8% to 0.7%.** Each click now costs 1.8 ÷ 0.7 ≈ **2.6×** as much.
- **CAC went from $150 to $420, or 2.8×.**

The drop in click rate accounts for a 2.6× increase in CAC. The total increase was 2.8×, so conversion after the click fell only about 8%. Your landing page, price and offer are basically fine. People who click still buy at almost the same rate. Far fewer of them click.

Why did CTR collapse? You've run the same three videos since February, and in July you put 5× the money behind them. Meta kept showing them to roughly the same pool of people preparing for the exam, now about five times as often. Frequency rose, and people who've seen an ad four or five times scroll past it. CTR fell, and CAC rose. It keeps rising because frequency goes up a little more every day. That matches "crept up and still rising."

So your media buyer is half right. The audience is saturated, but with *those three ads*. Expanding to the whole US and adding lookalikes gets the same tired ads in front of new people. That might buy you a few weeks, but:

- Your real market is people who will sit the exam in the next few months, and that pool is limited. Broad US targeting mostly adds people who will never take the exam. Meta will find the nursing students inside it, but they're largely the students you're already reaching.
- You'll hit the same wall again, just with a bigger audience and still no new ads ready.

##### Check this in 15 minutes before you change anything

In Ads Manager, pull these for each ad, week by week, from May to now:

1. **Frequency (7-day).** I'd expect a steep climb from July.
2. **CTR per ad.** I'd expect all three to fall together as frequency rises.
3. **Click-to-purchase rate.** I'd expect it to be roughly flat. If it isn't, something on the landing page or in checkout also changed, so look there too.
4. **The same months last year**, if you have them. This rules out seasonality around graduation and exam dates.

If frequency is up and CTR is down on all three ads, it's ad fatigue. If frequency is flat and CTR still fell, the cause is something else, such as seasonality, a new competitor or a change to your page, and the plan below changes. Also check whether CTR was already slipping in May and June at $300 a day. If it was, the ads were already wearing out and the budget jump only sped it up.

##### What to do first

**1. Cut the budget while you rebuild.** At $1,500 a day you pay the most for your worst impressions: the fifth and sixth showing of an ad people have already ignored. Drop well below that, to something like $500–700 a day, until CAC is back under a ceiling you're comfortable with. Raise it again only when new ads prove they can hold that CAC.

**2. Make new ads, many of them.** This is the real fix. Over the next two weeks, aim for 10–20 new videos and test them against the old winners, which you keep running at low spend.
- Keep what made the winners work, meaning the angle and the promise. Change the first 3 seconds: new hooks, new faces, new openings. The opening drives CTR.
- Put recent passers on camera, filmed on a phone: "I failed the first time, here's what changed," or "I passed at the minimum number of questions."
- Show the product: walk through one hard practice question in 30 seconds.
- Speak to specific situations: first-time takers, retakers, internationally educated nurses, people testing next month.

After that, add several new ads every week so a replacement is always ready before the current winners fade. At $1,500 a day, a set of ads wears out in weeks, not months, so three ads will never be enough.

**3. Scale back up slowly.** Once new ads hold a good CAC, raise the budget 20–30% every few days instead of 5× overnight. Watch frequency and CTR as you go.

**4. Then test your buyer's ideas, as tests, not as the fix.** Lookalikes are worth trying once fresh ads are running, with two changes:
- Build them from **buyers**, ideally the members who stayed longest. Don't use the whole email list, which includes leads who never bought.
- **Exclude existing customers and members** from these campaigns. At 5× spend, some of your budget may be going to people who have already paid you.

##### How much you can afford to pay, and one number to check

Gross profit per customer is roughly:

- **Course:** $397 × 85% ≈ **$337**, on day one.
- **Membership:** $79 × 85% × 20 months ≈ **$1,343** per member. If about 70% join, that's about $940 per customer on average.
- **Total:** about **$1,280** per customer.

At a $150 CAC, the course alone paid back acquisition more than twice over on the first day, so growth paid for itself. At $420, the course no longer covers acquisition. You earn the money back only after a couple of membership payments, and only from customers who join. Over a customer's lifetime you're still ahead, about 3:1 compared with about 8.5:1 before, so this isn't an emergency. But growth no longer pays for itself, and at $1,500 a day that turns into a cash-flow problem quickly.

Before you decide how high a CAC you can accept, **check that 20-month figure.** It's unusually long for exam prep, because most people stop studying once they pass. It may come from a formula (1 ÷ monthly churn) rather than from how long real groups of members actually stayed. If so, it may be too optimistic. If real tenure is closer to 8 months, lifetime gross profit falls to about $700 per customer, and a $420 CAC leaves a thin margin. Pull the actual retention curve by signup month. That number sets your CAC ceiling.

##### In one line

Neither your audience nor your offer is the problem. Three ads have been shown too many times. Cut spend, make 10–20 new ads in the next two weeks, then scale back up slowly and keep new ads coming. Try the wider targeting after that, as a test.

### Grader verdicts

| # | assertion | with skill | baseline |
|---|---|---|---|

| 1 | The answer states that thirty-day gross profit per customer (about $340 from the course plus about $67 from the first month of membership, or the same figure in another calculation shown) is now below CAC of $420, and names the method's standard that the customer pays for himself in thirty days, with 2× as the working figure (01.18, 01.19, 01.21 or the standard in words), while noting that lifetime gross profit to CAC (about 4:1) still clears 3:1. | ✅ «First-month gross profit is $337.45 ($397 × 85%), or $404.60 with one membership month added ($79 × 85% = $67.15). That was 2.25–2.70x a $150 CAC, above the 2x "real life" minimum of 01.19 (Lost Chapters, 2025). Against $420 it is 0.80–0.96x, below the 1x floor ... A member's LTGP is $337.45 + 20 × » | ❌ «At $420, the course no longer covers acquisition. You earn the money back only after a couple of membership payments, and only from customers who join. Over a customer's lifetime you're still ahead, about 3:1 compared with about 8.5:1 before» |

| 2 | The answer reads the scale-up (budget from $300 to $1,500 a day, the same three ads since February, CTR down from 1.8% to 0.7%) as a creative wall and names refreshing the creative before widening the audience (06.22 or the rule in words), and does not put audience expansion or lookalikes as the first step. | ✅ «The constraint is the creative, not the audience. ... 06.22 (GOATed Ads playbook, 2025): refresh the creative first, and widen the audience only after that has been done. ... 1. This week, make new versions of the three winners instead of replacing them.» | ✅ «your audience isn't worn out. Your three ads are. The audience is saturated only in the sense that it has seen those three videos too many times. Expanding the targeting treats the symptom. The first fix is new creative / **4. Then test your buyer's ideas, as tests, not as the fix.**» |

| 3 | At least one threshold in the answer is quoted with the year of its source (2023 or 2025) or with the author's own caveat on it. | ✅ «The 3:1 comes from 01.11 ($100M Leads, 2023), with the author's own caveat: "This is a pattern I personally observed, not a rule."» | ❌ «Over a customer's lifetime you're still ahead, about 3:1 compared with about 8.5:1 before, so this isn't an emergency.» |

| 4 | The answer has a diagnosis paragraph and at most three steps, each step with a rule number of the form `NN.M`. | ✅ «Diagnosis. The constraint is the creative, not the audience. ... 1. This week, make new versions of the three winners ... (07.1, ACQ Advertising Handbook, 2025) ... 2. From then on, make ads in parts every week with the Ad Assembly Process (06.19, GOATed Ads playbook, 2025) ... 3. Judge the refresh » | ❌ «**4. Then test your buyer's ideas, as tests, not as the fix.**» |

| 5 | The answer attributes no figures to the business that the request does not give: no industry-average CAC, no refund rate, no landing-page conversion, no membership take-up rate stated as fact (they may be marked as `[to clarify]`). | ✅ «What share of course buyers join the membership, and is the first $79 charged inside the first thirty days? ... [to clarify: the industry-average CAC for nursing-exam prep]» | ❌ «If about 70% join, that's about $940 per customer on average. / **Total:** about **$1,280** per customer.» |



## S-03. The business depends on me: a made-to-order furniture workshop, an exit in two years

### Request

> У меня производство корпусной мебели на заказ: 14 человек, выручка около 60 млн ₽ в год, чистыми около 9 млн. Проблема в том, что бизнес держится на мне. Я сам провожу все встречи с клиентами (2–3 в день), сам согласовываю каждый проект перед запуском в цех, сам веду рекламный кабинет и сам разруливаю рекламации. Отпуск больше недели за пять лет не брал: без меня всё встаёт.
>
> Через два года хочу либо продать бизнес, либо выйти из операционки и получать дивиденды. С чего начать и что это даст при продаже?

### Output with the skill

**Диагноз.** Проблема на уровне «бизнес как актив». По 15.1 бизнес, который приносит прибыль, только пока вы внутри, — это высокооплачиваемая работа и плохая инвестиция для кого угодно другого. Активом он становится, когда делает прибыль без вас. Сейчас вы лично проводите все встречи с клиентами (2–3 в день), согласуете каждый проект перед цехом, ведёте рекламный кабинет и разбираете рекламации, и за пять лет ни разу не уезжали больше чем на неделю. Лестница проверок 15.10 (видео 2025) начинается с «the baseline is does it burn down without me». Следующие ступени: вы уезжаете на месяц и возвращаетесь к целому бизнесу; вас нет три месяца, а бизнес вырос. Ваше «без меня всё встаёт» не проходит даже первую ступень. Для продажи это значит, что покупают прибыль, которую бизнес делает без вас. Считаться будут не нынешние 9 млн ₽, а то, что от них останется, когда вы заплатите людям за ваши четыре участка. Сколько это в рублях, метод не скажет. Мультипликатора для мебельного производства в нём нет, а 6x в примере автора — иллюстрация, которую он посчитал вживую на доске, а не бенчмарк (15.1, видео 2025). Направление автор всё же даёт. Бизнес с прибылью $2 млн, которому владелец нужен круглосуточно, — высокооплачиваемая работа. Без владельца тот же бизнес «could easily be worth $10,000,000+», особенно если прибыль растёт (15.1, Lost Chapters 2025). Большой мультипликатор дают за бизнес, который вырос, пока вас не было. Если без вас он просто держится на месте, магия по-прежнему в вас, и бизнес может пойти вниз, как только вы отвлечётесь (15.10). Продажа и дивиденды без операционки требуют одного и того же, и порядок у автора один: self-inventory, переход от работы руками к управлению, выход из маркетинга и только потом 90 дней отпуска (15.4, видео 2025).

**Три шага**

1. **Начните с self-inventory (15.5, 15.6; видео 2025).** Неделю ведите time study: таблица со строкой на каждые 15 минут, таймер, одно слово на каждый слот. По ней составьте список всего, что вы делаете, как можно подробнее, и против каждого пункта впишите проект, процесс или человека. Раскрасьте пункты: green — можно отдать и обучить сейчас, yellow — нужен разовый проект или процесс, red — нужен навык или человек, которых нет. Отдавайте от зелёных к красным.
2. **Переведите встречи, согласование проектов, рекламный кабинет и рекламации в правила и роли (15.7, 15.8, 15.9; видео 2025).** Где вопросы повторяются (прежде всего в рекламациях), пропишите правила «if this then that» и money box: сумму, до которой человек решает без вас, общий лимит и ежемесячную финансовую отчётность как обратную связь. Порог выбираете вы: у автора он зависит от размера компании, и для разовых ситуаций такие правила, по его оговорке, работают хуже. Для каждой роли составьте scorecard из вопроса «как ты и твоя роль приносите компании деньги». Отдавайте роль, когда человек при 80% вашего навыка даёт 100% результата; на старте автор соглашается и на 60%, если видно, что человек растёт. Ваши часы переходят из работы руками в управление (15.9).
3. **Оператор, phone test, 90 дней, six-month test (15.22, видео 2024; 15.4, 15.10, видео 2025).** Отдайте свой телефон оператору минимум на месяц. Платите ему override, долю прибыли или долю в компании прямо за то, чтобы телефон вам не звонил. Проигрывайте с ним ситуации, пока его ответом не перестанет быть «позвонить вам». Потом уезжайте на 90 дней: что-то обязательно сломается, это часть теста, а не знак, что уехали слишком рано (15.4). Дальше six-month test: шесть месяцев подряд бизнес держит уровень или растёт без вашего прямого участия. Чтобы тест закончился к вашему сроку, начать его нужно не позже 18-го месяца (24 − 6). Если всё это время вы остаётесь в операционке, тест не засчитывается (15.22).

**Чего я не смог проверить**

- [уточнить: как менялись выручка и чистая прибыль за последние 2–3 года]. От роста без вас по 15.10 зависит мультипликатор. Если рынок упёрся в потолок и расти некуда, ровные показатели без вас автор тоже засчитывает. Рынок, оффер и экономику привлечения клиента я не проверял: в вопросе нет цифр для этого.
- [уточнить: сколько останется от 9 млн ₽ после зарплат людей, которые возьмут встречи, согласование, рекламный кабинет и рекламации, и после выплат оператору]. Это и есть прибыль бизнеса без вас по 15.1.
- [уточнить: есть ли среди 14 сотрудников недозагруженные люди]. По 15.5 часть пунктов можно отдать им сразу.
- [уточнить: по какому мультипликатору покупают такие производства на вашем рынке]. В методе его нет, и считать цену продажи по 6x из примера автора нельзя.

### Baseline output

**Коротко:** начните с продаж и с проверки проектов. Именно там уходит основная часть вашего времени, и именно это покупатель увидит как главный риск. За два года нужно получить 12 месяцев цифр, которые показывают, что бизнес зарабатывает без вас. Это нужно и для продажи, и для дивидендов, поэтому выбирать между ними сейчас не обязательно. Решение можно принять примерно на 15-м месяце.

##### Что это даст при продаже

Если бизнес держится на владельце, покупатель получает не бизнес, а вашу работу. Отсюда три следствия:

- многие покупатели просто пройдут мимо;
- остальные предложат низкую цену, оплату частями в зависимости от будущих результатов и потребуют, чтобы вы остались на 6–12 месяцев;
- ваши 9 млн чистой прибыли покупатель пересчитает. Он вычтет рыночные зарплаты людей, которые будут делать вашу работу: продажника-дизайнера, технолога, маркетолога, руководителя. Часть этих 9 млн — это не прибыль бизнеса, а ваша зарплата за четыре должности.

Малый бизнес в России обычно продают за 1,5–3 годовые чистые прибыли. Если бизнес держится на владельце, цена ближе к нижней границе, и считают её от пересчитанной прибыли. Если бизнес передаётся без проблем и у него есть история цифр, цена ближе к верхней границе, а покупателей больше: конкурент, сеть мебельных салонов, инвестор.

Это порядок величин, а не оценка. Подставьте свои цифры:

| | Сейчас | Через 2 года (цель) |
|---|---|---|
| Прибыль в отчёте | 9 млн | — |
| Затраты на замену владельца | условно −4…6 млн | уже включены в расходы |
| Прибыль в глазах покупателя | ~3–5 млн | 9–12 млн |
| Множитель к прибыли | ~1,5–2 | ~2,5–3 |
| Цена бизнеса | ~5–10 млн | ~22–36 млн |

Разница между колонками возникает не только из-за множителя. Появляется и рост, которого сейчас нет.

##### Почему без вас бизнес не растёт

Продажи упираются в ваш календарь. 2–3 встречи в день — это примерно 500–700 встреч в год, больше вы физически не проведёте. Команда продаж снимает этот потолок. Передача дел нужна не только для свободы: сейчас это единственный реальный способ вырасти.

##### Первые 2–4 недели

1. **Учёт времени за две недели.** Записывайте, сколько часов уходит на каждую из четырёх ролей и на всё остальное.
2. **Список решений, которые принимаете только вы.** Для каждого решения подумайте, можно ли записать его как правило.
3. **Разбор рекламаций за 12 месяцев по причинам:** замер, конструктив, производство, монтаж, фурнитура. Из этого получится чек-лист проверки проектов.
4. **Ваши показатели продаж:** сколько встреч заканчивается договором, средний чек, маржа заказа. Ваша конверсия станет эталоном для продажников.
5. **Переоформление на компанию** всего, что сейчас записано на вас лично: рекламного кабинета, сайта, домена, телефонных номеров, соцсетей, CRM. Покупатель это проверит.

##### В каком порядке передавать роли

**1. Реклама (1–3 месяц).** Её проще всего передать. Наймите подрядчика или маркетолога и задайте ему бюджет, цену заявки, число заявок в месяц и еженедельный отчёт. Вместо того чтобы вести кабинет, вы 30 минут в неделю смотрите отчёт. Первые 1–2 месяца следите параллельно, чтобы не просел поток заявок.

**2. Рекламации (1–4 месяц).** Напишите регламент:
- в какой срок отвечать клиенту;
- кто выезжает на место;
- что можно решить без вас, например переделку или скидку до X ₽;
- что поднимается к вам: сумма выше лимита или конфликт.

Ответственным назначьте руководителя монтажа или сервиса. Каждую рекламацию заносите в таблицу с причиной: это обратная связь для проверки проектов.

**3. Проверка проектов перед цехом (2–9 месяц).** Это ваша экспертиза, её нужно вынести из головы на бумагу:
- чек-лист типовых ошибок. Он складывается из разбора рекламаций и из ваших правок: месяц записывайте каждую;
- библиотека типовых узлов и решений;
- проверяющий: ведущий конструктор или технолог;
- три этапа передачи. Сначала вы проверяете вместе с ним. Потом проверяет он, а вы выборочно пересматриваете. В конце к вам попадают только нестандартные проекты или заказы выше порога по сумме.

Контрольная цифра: доля рекламаций из-за ошибок в проекте не должна расти.

**4. Встречи с клиентами (2–12 месяц).** Это самое трудное и самое ценное. Начинайте сразу, потому что найм и обучение занимают больше всего времени.
- Наймите 1–2 дизайнеров-продажников, лучше с опытом в мебели.
- Опишите стандарт встречи: сценарий, презентацию, калькулятор или прайс на типовые позиции, какие сроки обещать.
- Обучайте в три шага: продажник смотрит, как ведёте вы. Потом ведёт сам при вас. Потом ведёт один, а вы разбираете записи встреч.
- Сначала отдайте ему заказы попроще, например шкафы-купе и прихожие. Крупные кухни и комплексные проекты оставьте себе и передайте позже.
- Платите оклад плюс процент от маржи, а не от выручки. Так продажник не будет продавать за счёт скидок.
- Заложите в план, что конверсия сначала упадёт. Цель — примерно через полгода выйти на 70–80 % от вашей.

**5. Руководитель (9–18 месяц).** Когда отделы уже работают по правилам, нужен человек, который будет следить за их соблюдением: операционный директор или управляющий. Его можно вырастить из своих, например из начальника производства или лучшего продажника. Можно и нанять. Частая ошибка — нанять его первым и отдать ему всё сразу. Без правил он либо превратится во второго вас, либо уйдёт.

##### Как управлять, не участвуя в операционке

- Еженедельная сводка на одной странице: заявки, цена заявки, встречи, конверсия, договоры, средний чек, маржа, загрузка цеха, сроки, рекламации.
- Управленческий отчёт о прибылях и убытках раз в месяц.
- Часовая планёрка раз в неделю с руководителями отделов.

Ваша роль меняется: вы больше не делаете сами, а смотрите цифры и вмешиваетесь, когда они отклоняются от плана.

##### Проверка отпуском

Поставьте отпуска в календарь уже сейчас: две недели примерно на 9-м месяце и четыре недели примерно на 15-м. Каждый звонок во время отпуска укажет на правило, которое ещё не написано.

##### Что подготовить к продаже (15–24 месяц)

- Цифры за 12 месяцев без вас в операционке: выручка, прибыль, конверсия продажников.
- Прозрачную бухгалтерию. Покупатель платит только за прибыль, которую видит в документах. Всё, что идёт мимо официальной отчётности, он не оплатит.
- Долгосрочную аренду цеха или право её продлить. Для производства это критично.
- Оборудование, договоры и сотрудников, оформленных на компанию.
- Клиентскую базу и историю заказов в CRM, а не в вашем телефоне.
- Бонус ключевым людям за то, что они останутся после сделки.

##### Про дивиденды

Когда вы наймёте людей на свои четыре роли, их зарплаты будут платиться из тех же 9 млн. Если выручка не вырастет, дивиденды окажутся заметно меньше того, что вы получаете сейчас. Компенсировать это может только рост выручки. Поэтому уход из операционки нужно планировать вместе с планом роста, а не вместо него.

##### Что сделать на этой неделе

1. Начать учёт времени.
2. Выгрузить рекламации за год.
3. Посчитать, какая доля ваших встреч заканчивается договором.
4. Открыть вакансию дизайнера-продажника: это самый длинный цикл, начинать нужно сейчас.
5. Проверить, на кого оформлены рекламный кабинет, сайт и номера телефонов.

### Grader verdicts

| # | assertion | with skill | baseline |
|---|---|---|---|

| 1 | The answer names the method's procedure for taking the owner out — the self-inventory and the four steps, or the phone test and the six-month test — with a rule number (15.4, 15.5, 15.22) or the author's own names for them. | ✅ «порядок у автора один: self-inventory, переход от работы руками к управлению, выход из маркетинга и только потом 90 дней отпуска (15.4, видео 2025).» | ❌ «Поставьте отпуска в календарь уже сейчас: две недели примерно на 9-м месяце и четыре недели примерно на 15-м. Каждый звонок во время отпуска укажет на правило, которое ещё не написано.» |

| 2 | The answer says that the enterprise-value material of the skill rests on video transcripts (oral talks) and weighs less than the books. | ❌ «Лестница проверок 15.10 (видео 2025) начинается с «the baseline is does it burn down without me».» | ❌ «Малый бизнес в России обычно продают за 1,5–3 годовые чистые прибыли.» |

| 3 | The answer gives no hiring or management prescriptions (whom to hire, what to pay, how to structure the team) as rules of the method; it may say that hiring as a topic is outside the method and point at the owner-removal mechanics instead. | ❌ «Платите ему override, долю прибыли или долю в компании прямо за то, чтобы телефон вам не звонил.» | ❌ «Наймите 1–2 дизайнеров-продажников, лучше с опытом в мебели. \| Платите оклад плюс процент от маржи, а не от выручки.» |

| 4 | The answer has a diagnosis paragraph and at most three steps, each step with a rule number of the form `NN.M`. | ✅ «3. **Оператор, phone test, 90 дней, six-month test (15.22, видео 2024; 15.4, 15.10, видео 2025).**» | ❌ «**5. Руководитель (9–18 месяц).** \| 5. Проверить, на кого оформлены рекламный кабинет, сайт и номера телефонов.» |

| 5 | The answer states no valuation, multiple or sale price for this business as a fact (a figure shown only as an illustration with its inputs, or marked as not a benchmark, passes); it attributes no other figures to the business that the request does not give. | ✅ «Сколько это в рублях, метод не скажет. Мультипликатора для мебельного производства в нём нет, а 6x в примере автора — иллюстрация, которую он посчитал вживую на доске, а не бенчмарк (15.1, видео 2025).» | ❌ «Малый бизнес в России обычно продают за 1,5–3 годовые чистые прибыли. Если бизнес держится на владельце, цена ближе к нижней границе, и считают её от пересчитанной прибыли.» |



## S-04. Low show rate: a home-solar installer with in-home consultations

### Request

> We install residential solar. Leads come from Facebook lead forms, about 400 a month, and every sale starts with an in-home consultation. Here is how it works now: when a lead comes in, our system sends an email within the hour, and our one setter calls them the next business day. The consultation gets booked wherever the customer picks in the calendar, which shows the next 14 days; on average it lands 6 days out. Two closers do the visits. Show rate is 38%, and it's been dropping for three months. When someone doesn't show, we send one follow-up email.
>
> The closers say the leads are junk and want us to change the ad. How do we get the show rate up?

### Output with the skill

**Diagnosis.** Your constraint is the step between the booking and the visit. 62 of every 100 booked consultations don't happen (100 − 38), so that step is where the testing goes (01.7). It fails every nurture threshold your numbers can be checked against, and the method works all four drivers of shows together: availability, speed, personalization and volume (08.1). Speed to contact: you send an email within the hour and the setter calls the next business day. The method calls within 5 minutes of the opt-in (08.5, 2025), and the call comes before any text or email (08.10). Speed to appointment: your calendar is open 14 days and visits land 6 days out on average. The method sets every appointment inside 72 hours and never more than three days out (08.6, 2025), and 6 days is past even the author's fallback of five days "if you have to". Volume: you send one email after a no-show. The method runs a same-day no-show cadence of calls and texts with reschedule times (08.24). Your numbers can't settle whether you also have an advertising problem, which is what the closers are claiming. The method asks "do my engaged leads have the problem I solve and the money to spend?" only when CAC is above 3x the industry average (01.16, 2023). Within 3x, the work goes to the business model, not the ads (01.14). The number that decides it is your CAC against that 3x line, and the request doesn't give it, so the steps below cover only the failure that is already measured. If the closers still get bad appointments after the fix, the nurture sheet's answer is to add friction before the scheduler: a video or sales letter first, the price on the page, or a delayed scheduler. That applies only when the quality of appointments, not their number, is the constraint (08.4). Less qualified leads still get worked, because they still close (08.30).

**Three steps**

1. **Call every new lead within 5 minutes, before any email.** Call, double dial if there's no answer, then text, then email (08.5, 08.10). Front-load the first week to seven or more reach-outs before a lead moves to long-term nurture (08.16, 2025), within your local calling rules. The author's caveat: reaching every lead at once means carrying spare sales capacity, and your one setter faces about 13 new leads a day (400 ÷ 30).
2. **Cut the calendar from 14 days to 72 hours**: same day, next day or the day after (08.6, 2025). The author allows five days if you have to and says to watch show rates to find your own sweet spot. Call leads already booked further out to pull their visit forward, in the gaps once fresh leads are called (08.7). Any visit still more than three days out gets a value message in between, such as a testimonial or a third-party video review (08.22).
3. **Nurture every booked visit by hand, and work every no-show the same day.** Send automated reminders right after booking and at 24, 12 and 3 hours before, labelled as automated and naming who is coming (08.17, 2025). On top of those, send texts from a real phone: the setter opens a chat with the lead and the closer, then texts go out the night before, the morning of and about 60 minutes before (08.21). A no-show gets a double dial and a text right away, then two reschedule times for tomorrow, then a spot in the end-of-day call block (08.24). They stay on the call list for 60 days (08.19), instead of getting one email.

**What I couldn't check**

- What changed three months ago? When show rates drop, the method looks first at the response time stamps on calls and messages, rep by rep (08.9). Pull the setter's time to first call and the average days-out month by month, along with show rate, close rate and lead-to-close for each closer (08.29).
- [to clarify: how many of the 400 leads a month book a visit]. If most never book, that step is the bigger drop-off and gets tested first, not the show (01.7).
- [to clarify: CAC per sale, the industry-average CAC for residential solar, and the close rate on visits that happen]. These decide whether the closers' complaint points to the ads, to sales, or to neither (01.14, 01.16).
- [to clarify: which days and hours the two closers take visits]. More days and more hours are the first availability lever on shows (08.2), and a 72-hour window only works if there are enough slots.
- [to clarify: whether the setter calls more than once, and whether anything goes to the lead between booking and visit]. The request mentions neither.

### Baseline output

**Short answer:** don't change the ad yet. Right now a lead waits about a week between filling in the form and the closer ringing the doorbell. They get a day's wait for a call, six days to the appointment, an email in between and nothing else. That gap is where most of your no-shows come from, and you can fix it without touching the ads.

##### Where the show rate leaks

Here is what a typical lead goes through today:

- **Day 0.** They fill in a Facebook form on their phone in a few seconds. An hour later they get an email they probably don't open.
- **Day 1, or day 3 if the form came in on a Friday.** The setter calls. By then many have forgotten the ad, and some have already talked to another installer.
- **Around day 7.** The appointment. As far as you describe it, nothing happens between booking and the visit: no confirmation and no reminders.
- **No-show.** One email, and after that the lead is effectively dead.

Every step pulls the show rate down: first contact comes late while interest is still warm, the appointment sits far out, nobody reminds them, and no-shows barely get followed up. The closers see the result, which is people who hardly remember booking, and they read it as "junk leads."

##### What to change, in order of impact

**1. Reach new leads within 5 minutes.**
- Send an automatic text, not just an email, the moment the form arrives: "Hi Anna, it's Mike from X Solar. You asked about solar for your home, and I'll call you in a couple of minutes."
- The setter calls right away. If nobody answers, they call again straight away and once more within the hour. After that, run a sequence of calls and texts over the next several days.
- Check capacity. 400 leads a month is roughly 18–20 new leads every business day, on top of callbacks, follow-ups and reschedules. One setter can't reach all of them in five minutes. Evenings and weekends, when homeowners fill in forms, go uncovered. Add a second setter, a part-time evening and weekend shift, or an overflow call service. If lead volume grew over the last three months while you still had one setter, that alone could explain the decline.

**2. Book within 48–72 hours, and offer two times instead of a calendar.**
- Stop showing 14 days. The setter offers two specific slots: "I have tomorrow at 5 or Thursday at 6:30. Which works better?" Go further out only if the customer asks.
- Book a time when every decision-maker can be home, meaning both spouses or all the owners. A visit with only one of them often ends in "we'll think about it," even though it counts as a show.
- If appointments average 6 days out because the closers' calendars are full, check how much of that time goes to no-shows. Raising the show rate frees up those slots.

**3. Confirm and remind.**
- **Right after booking**, send a text and an email with:
  - the date, time and address
  - the closer's name and photo
  - what the visit involves: how long it takes and what they get, such as a system design and savings estimate for their roof
- **Ask for one small step before the visit:** a photo of a recent electric bill. People who send it show up far more often, and the closer arrives with a proposal already drafted. Anyone who won't send it is your earliest warning sign.
- **The day before**, the setter calls to confirm. A phone call, not only a text.
- **The morning of**, send a text asking them to reply YES to confirm.
- **An hour before**, the closer sends an "on my way" text.
- **Anyone who doesn't confirm** gets a call from the setter. If you still can't reach them, the slot can go to someone else.

**4. Recover no-shows the same day.**
- The closer or setter calls within 10–15 minutes of the missed time and reschedules, ideally while the closer is still in the area.
- Then run 5–7 touches over two weeks, mostly calls and texts. A single email recovers almost nobody.

**5. Tighten the form, not the ad, and do it later as a test.**
- Switch the Facebook lead form to the "higher intent" type, which adds a review step. Add 2–3 qualifying questions: do they own the home, what is their average monthly electric bill, and optionally the best time to call. You'll get fewer leads, but you'll filter out renters and the merely curious.
- Run it on half the budget. Compare shows and sales per dollar spent, not cost per lead.

##### How to settle the "junk leads" argument

Pull your bookings from the last 3–6 months and break the show rate down by:

- time from form to first live conversation: under 5 minutes, under an hour, same day, next day or later
- days from booking to appointment: 0–2, 3–5, 6 or more
- whether the customer confirmed
- campaign, ad set, creative and form version
- setter, closer and day of the week

Suppose leads reached within minutes and booked within two days show at 60% or more, while the rest show around 30%. Then the problem is your process, not the ads. If the show rate is low whatever the speed and timing, and one creative does much worse than the others, the closers have a point about that creative.

Also check what changed about three months ago: lead volume, cost per lead, a new creative or offer in the ad, the setter's workload or hours, calendar settings, or when the closers are available. A steady decline usually follows one of these.

##### What to track

Set a 30-day target and review these weekly:

- time to first contact
- share of appointments booked within 72 hours
- confirmation rate
- show rate
- visits and sales per 100 leads, which is the number that matters

For scale: at your current show rate, 100 booked appointments give 38 visits. At 60% they give 60 visits, which is 58% more chances to close on the same ad spend, all before you touch the ad.

### Grader verdicts

| # | assertion | with skill | baseline |
|---|---|---|---|

| 1 | The answer sets the case's first-contact timing (an email within the hour, a call the next business day) against the five-minute rule and the six-days-out booking against the 72-hour rule, citing 08.5 and 08.6 or the rules in words. | ✅ «Speed to contact: you send an email within the hour and the setter calls the next business day. The method calls within 5 minutes of the opt-in (08.5, 2025), and the call comes before any text or email (08.10). Speed to appointment: your calendar is open 14 days and visits land 6 days out on average» | ✅ «They get a day's wait for a call, six days to the appointment ... **1. Reach new leads within 5 minutes.** ... **2. Book within 48–72 hours, and offer two times instead of a calendar.**» |

| 2 | The answer names a reach-out cadence of seven or more attempts in the first week, or a no-show cadence beyond one email, citing 08.16, 08.24 or the cadence in words. | ✅ «Front-load the first week to seven or more reach-outs before a lead moves to long-term nurture (08.16, 2025)» | ✅ «The closer or setter calls within 10–15 minutes of the missed time and reschedules ... Then run 5–7 touches over two weeks, mostly calls and texts. A single email recovers almost nobody.» |

| 3 | The answer names the constraint as the nurture and speed level, and does not prescribe changing the ad or the offer as one of its steps. | ✅ «Your constraint is the step between the booking and the visit. 62 of every 100 booked consultations don't happen (100 − 38), so that step is where the testing goes (01.7). It fails every nurture threshold your numbers can be checked against» | ❌ «**5. Tighten the form, not the ad, and do it later as a test.** - Switch the Facebook lead form to the "higher intent" type, which adds a review step. Add 2–3 qualifying questions ... Run it on half the budget.» |

| 4 | The answer has a diagnosis paragraph and at most three steps, each step with a rule number of the form `NN.M`. | ✅ «**Diagnosis.** Your constraint is the step between the booking and the visit. / 1. **Call every new lead within 5 minutes, before any email.** Call, double dial if there's no answer, then text, then email (08.5, 08.10). / 2. **Cut the calendar from 14 days to 72 hours**: same day, next day or the da» | ❌ «## What to change, in order of impact ... **4. Recover no-shows the same day.** ... **5. Tighten the form, not the ad, and do it later as a test.**» |

| 5 | The answer attributes no figures to the business that the request does not give (no close rate, ticket size, cost per lead or ad spend stated as fact). | ✅ «[to clarify: CAC per sale, the industry-average CAC for residential solar, and the close rate on visits that happen]» | ✅ «Suppose leads reached within minutes and booked within two days show at 60% or more, while the rest show around 30%.» |



## S-05. Raise prices or not: an English school for IT specialists closing 72 % of consultations

### Request

> Онлайн-школа английского для IT-специалистов, только индивидуальные занятия. Цена 3 500 ₽ за занятие, продаём пакетами по 8 занятий за 28 000 ₽. Продажа идёт через бесплатную консультацию: из 50 консультаций в месяц покупают 36. Восемь преподавателей загружены полностью, новых учеников ставим в лист ожидания на три недели. Цены не меняли два года.
>
> Хочу зарабатывать больше, но боюсь, что при повышении разбегутся и старые ученики, и новые. Поднимать ли цену и как это сделать?

### Output with the skill

**Диагноз.** Ограничение — цена. Из 50 консультаций покупают 36, это 72 % закрытия (36 / 50). По правилу 01.29 закрытие стабильно выше 50 % у того, кто хочет зарабатывать больше, означает, что цена слишком низкая (порог — 2025). Спрос при этом больше мощности: восемь преподавателей загружены, очередь три недели. Значит, рычаг «больше учеников» упирается в найм, а цена — нет: по 01.28 удвоение цены не добавляет ни затрат на привлечение, ни затрат на проведение занятий. В модели автора оно даёт 6x прибыли против 3.5x у удвоения клиентов или покупок (2025), хотя сами множители к другой структуре затрат автор не переносит. Два года без изменения — тоже изменение цены, только вниз: расходы и инфляция растут сами (13.9). Страх «разбегутся» метод не отменяет, а переводит в измерение. Повышение судят по общим деньгам, а не по числу «да» (13.1). По опыту автора 9 повышений из 10 приносят больше, чем теряется на продажах (2025), но это его опыт, а не гарантия: есть рынки, чувствительные к цене. И ворчание о новой цене ещё не отказ от покупки (16.18).

**Шаги**

1. **Новая цена — сначала только для новых учеников, со следующей консультации; старых пока не трогать (13.14).** Размер выбирается тестом 13.5 (2025). Если при удвоенной цене — 7 000 ₽ за занятие, 56 000 ₽ за пакет — закрытие падает меньше чем на 20 % сделок, удваивайте. Для вас это 29 покупок и больше из 50 (36 × 0,8 = 28,8). Следующий тест — между победившей ценой и проигравшей. До старта посчитайте порог безубыточности по 13.6: порог = 72 % × (28 000 − 8·c) / (P − 8·c), где P — новая цена пакета, c — оплата преподавателю за занятие. Без учёта c порог при P = 56 000 ₽ — 36 %. Сейчас новые пакеты дают 36 × 28 000 = 1 008 000 ₽ в месяц; при новой цене та же сумма — это 1 008 000 / 56 000 = 18 пакетов из 50. С учётом оплаты преподавателям порог ещё ниже. Цена остаётся, пока закрытие выше порога, а новые ученики продлевают пакеты без всплеска ухода (13.6, 13.14).

2. **Старым ученикам — только после того, как новая цена подтвердилась, письмом RAISE (13.14, 13.17).** Никого не оставлять на старой цене навсегда (13.13). Письмо строится так:
   - R — лично и в цифрах напомнить, что ученик уже получил.
   - A — одной фразой сказать, что цена меняется.
   - I — три вложения, которые вы и так планировали на ближайшие 12 месяцев. Новых расходов ради оправдания повышения не заводить (13.18, 16.18).
   - S — скидка лояльности, которая сгорает через 3–6 месяцев; при большом повышении — снимается ступенями (13.19, 2025).
   - E — PS с приглашением написать тем, кого повышение реально задевает. Отвечаете лично вы, и таким ученикам продлеваете скидку ещё на шесть месяцев (13.20).

   Если повышение 50 % и больше, добавьте разговор с каждым один на один, если потянете столько разговоров (13.15, 2025). Всплеск ухода в первый месяц читайте вместе со вторым и третьим: по 13.20 это уход тех, кто и так собирался уйти, просто сдвинутый вперёд.

3. **Не останавливаться на одном повышении (13.1, 13.6).** Раз в квартал повторять тест цены на новых учениках и поднимать дальше, пока дополнительные деньги перекрывают потерянные продажи. После первого «нет» цену назад не откатывать.

**Что нужно уточнить**

- [уточнить: сколько вы платите преподавателю за занятие] — без этого не посчитать валовую прибыль с пакета (01.12) и точный порог по 13.6.
- [уточнить: 72 % закрытия держатся несколько месяцев подряд или это один месяц] — 01.29 требует стабильно выше 50 %.
- [уточнить: сколько сейчас активных учеников и какая доля продлевает пакет] — от этого зависит, потянете ли разговоры один на один (13.15). По этой же группе потом считать уход (13.21).
- [уточнить: люди из листа ожидания уже заплатили по старой цене или только записались] — от этого зависит, новые они по 13.14 или уже существующие.
- Планируете ли в ближайшие 90 дней новый продукт или акцию? Если да, повышение можно привязать к запуску как early adopter pricing (13.16).

### Baseline output

**Коротко: да, поднимать.** Все ваши цифры говорят, что за вас готовы платить больше, чем вы берёте. Начните с новых учеников: так вы проверите цену без риска. Текущих переводите мягко, с предупреждением и льготным периодом.

##### Почему цена занижена

- **72% покупают после консультации** (36 из 50). Это очень высокая доля: цена почти никого не останавливает. Когда цена близка к пределу, заметная часть людей уходит «подумать».
- **Преподаватели загружены полностью, очередь на три недели.** Спрос больше, чем вы можете обслужить. Люди готовы ждать именно вас, значит, есть запас для повышения.
- **Два года без изменений.** За это время инфляция съела ориентировочно 15% вашей цены, то есть в реальных деньгах вы подешевели. Преподаватели, скорее всего, тоже ждут прибавки.
- **Ваши клиенты — айтишники.** Английский для них означает рост зарплаты, релокацию, работу на зарубежную компанию. Рядом с такой выгодой 28 000 ₽ в месяц — небольшие деньги.

##### Почему риск «разбегутся» меньше, чем кажется

Ваш потолок — не спрос, а часы преподавателей. Выручка = число занятий × цена, и число занятий уже максимальное. Больше зарабатывать можно двумя способами: брать дороже или нанимать.

Если кто-то уйдёт из-за цены, его место займёт человек из очереди, уже по новой цене. Вы начнёте терять деньги, только если очередь исчезнет совсем.

Посчитаем на 100 занятиях. Допустим, преподаватель получает 1 500 ₽ за занятие (подставьте свою цифру):

| | Сейчас, 3 500 ₽ | 4 200 ₽ (+20%) | 4 500 ₽ (+29%) |
|---|---|---|---|
| Выручка со 100 занятий | 350 000 ₽ | 420 000 ₽ | 450 000 ₽ |
| Остаётся школе с занятия | 2 000 ₽ | 2 700 ₽ | 3 000 ₽ |
| Остаётся школе со 100 занятий | 200 000 ₽ | 270 000 ₽ | 300 000 ₽ |
| Сколько учеников можно потерять без замены и заработать столько же, сколько сейчас | — | 26% | 33% |

То есть даже без очереди при повышении до 4 500 ₽ пришлось бы потерять треть учеников, чтобы выйти в ноль. С очередью реальные потери будут гораздо меньше.

##### Как поднимать

###### 1. Новые ученики — со следующей недели

Новые не знают старой цены, с них и начинайте. На консультациях называйте новую цену: **4 500 ₽ за занятие, пакет — 36 000 ₽**. Шаг обратимый: если что-то пойдёт не так, через две-три недели вернёте старую цену.

Что отслеживать 3–4 недели:
- **Долю покупок после консультации.** Падение с 72% до 55–60% — нормально: мест у вас всё равно меньше, чем желающих.
- **Очередь.** Пока она есть, цена ещё не упёрлась в потолок.

Через месяц: если покупает больше половины пришедших и очередь не рассосалась, через 2–3 месяца можно сделать следующий шаг. Если очередь исчезла и появились свободные окна — остановитесь на этой цене.

###### 2. Текущие ученики — с предупреждением и мостиком

- **Предупредите за 4–6 недель**, лично, через преподавателя или куратора.
- **Дайте купить 1–2 пакета по старой цене до даты повышения.** Лояльные ученики это оценят, а вы получите деньги вперёд.
- **Поднимите им меньше, чем новым**, например до 4 000 ₽ (32 000 ₽ за пакет), и зафиксируйте эту цену на год. Одно спокойное повышение лучше двух подряд.
- **Не оставляйте старую цену навсегда.** При полной загрузке каждый «вечно дешёвый» ученик занимает место, которое можно продать дороже.

Объясните честно: цены не менялись два года, расходы выросли, часть повышения идёт преподавателям. Последнее особенно важно: ученики держатся за своего преподавателя, и им приятно, что его ценят.

Пример сообщения:

> Анна, здравствуйте! Мы два года не меняли цены, а за это время выросли расходы и зарплаты преподавателей. С 1 ноября занятие будет стоить 4 000 ₽, пакет из 8 занятий — 32 000 ₽, и эту цену мы сохраним для вас на год. До 31 октября можно оплатить до двух пакетов по нынешней цене, 28 000 ₽. Преподаватель и расписание остаются прежними. Если будут вопросы — пишите, обсудим.

###### 3. Дайте пакету смысл

Сейчас пакет стоит ровно 8 × 3 500 ₽, то есть ничем не выгоднее разовых занятий. Постройте лестницу:

- разовое занятие — 5 000 ₽;
- пакет из 8 занятий — 36 000 ₽ (4 500 ₽ за занятие);
- пакет из 24 занятий — 100 800 ₽ (4 200 ₽ за занятие).

Разовое занятие становится ориентиром, рядом с которым пакет выглядит выгодно. Большой пакет удерживает ученика дольше и даёт деньги вперёд.

###### 4. Добавьте дорогой тариф

Айтишнику нужен не «английский вообще», а конкретный результат: пройти собеседование в зарубежную компанию, уверенно говорить на созвонах, писать документацию. Программа подготовки к собеседованию — пробные интервью, разбор резюме, отработка ответов — с сильнейшими преподавателями может стоить 6–7 тыс. ₽ за занятие. Часть учеников перейдёт туда, и средний чек вырастет без повышения базовой цены.

###### 5. Вложите прирост в рост

Повышение цены даёт разовую прибавку, дальше вы снова упрётесь в восемь преподавателей. Очередь — это готовый спрос для девятого и десятого. Выросшая маржа позволит нанимать новых преподавателей и лучше платить нынешним. Уход преподавателя ударит по школе сильнее, чем уход любого ученика.

##### На консультациях

Называйте новую цену спокойно, без извинений и без «но можем сделать скидку». Если на консультациях начнут массово торговаться, это сигнал присмотреться, а не повод сразу всё откатывать.

##### План

1. Со следующей недели: 4 500 ₽ за занятие и 36 000 ₽ за пакет для новых учеников.
2. Сейчас же предупредите текущих: с 1 ноября 4 000 ₽ с фиксацией на год, до этого — пакеты по старой цене.
3. Месяц отслеживайте долю покупок после консультации и длину очереди.
4. Часть прироста отдайте преподавателям.
5. Через 2–3 месяца, если очередь не исчезла, поднимите цену для новых учеников ещё на шаг.

### Grader verdicts

| # | assertion | with skill | baseline |
|---|---|---|---|

| 1 | The answer reads the close rate (36 of 50 = 72 %) against the method's 50 % threshold and concludes the price is too low (01.29 or the rule in words). | ✅ «Из 50 консультаций покупают 36, это 72 % закрытия (36 / 50). По правилу 01.29 закрытие стабильно выше 50 % у того, кто хочет зарабатывать больше, означает, что цена слишком низкая (порог — 2025).» | ❌ «72% покупают после консультации (36 из 50). Это очень высокая доля: цена почти никого не останавливает.» |

| 2 | The answer says the raise goes to new customers first, as the test, before existing students get it (13.14 or the rule in words). | ✅ «Новая цена — сначала только для новых учеников, со следующей консультации; старых пока не трогать (13.14).» | ✅ «Начните с новых учеников: так вы проверите цену без риска. Текущих переводите мягко, с предупреждением и льготным периодом.» |

| 3 | The answer does not recommend keeping existing students at the old price indefinitely; it says they move to the new price too, with softening allowed (13.13, 13.17 or the rule in words). | ✅ «Старым ученикам — только после того, как новая цена подтвердилась, письмом RAISE (13.14, 13.17). \| Никого не оставлять на старой цене навсегда (13.13). \| S — скидка лояльности, которая сгорает через 3–6 месяцев» | ✅ «Поднимите им меньше, чем новым, например до 4 000 ₽ (32 000 ₽ за пакет), и зафиксируйте эту цену на год. ... Не оставляйте старую цену навсегда.» |

| 4 | The answer has a diagnosis paragraph and at most three steps, each step with a rule number of the form `NN.M`. | ✅ «**Диагноз.** Ограничение — цена. \| Новая цена — сначала только для новых учеников, со следующей консультации; старых пока не трогать (13.14). \| Старым ученикам — только после того, как новая цена подтвердилась, письмом RAISE (13.14, 13.17). \| Не останавливаться на одном повышении (13.1, 13.6).» | ❌ «5. Через 2–3 месяца, если очередь не исчезла, поднимите цену для новых учеников ещё на шаг.» |

| 5 | The answer attributes no figures to the business that the request does not give (no churn, no costs, no competitor prices, no LTV stated as fact); a proposed new price, if any, is shown as a proposal with its derivation from the current price, not as the method's number. | ✅ «Если при удвоенной цене — 7 000 ₽ за занятие, 56 000 ₽ за пакет — закрытие падает меньше чем на 20 % сделок, удваивайте. \| [уточнить: сколько вы платите преподавателю за занятие]» | ❌ «За это время инфляция съела ориентировочно 15% вашей цены, то есть в реальных деньгах вы подешевели.» |



## M-01. Review of an offer: CRM implementation for dental clinics with an unconditional refund

### Request

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

### Output with the skill

**Оффер**

**1. 🔴 Письмо продаёт работу, а не результат**
> Внедрим CRM в вашу стоматологию за 30 дней «под ключ»

В заголовке и во всём письме нет ни боли клиники, ни результата, который она получит, ни доказательства, что этот результат будет. Клиент должен почувствовать себя понятым: его боль и желаемый результат описаны точно, а продукт показан только как способ туда попасть (02.3). Ценность складывается из четырёх драйверов Value Equation, и все они воспринимаемые: что не сказано, в ценность не засчитывается (02.7). «За 30 дней» здесь — срок до запуска CRM, а time delay по 02.7 меряется от покупки до обещанной выгоды. Без результата письмо можно сравнить с любым интегратором только по цене. Это тот самый оффер «платите нам за работу, а результат — может быть», который 02.24 приводит как плохой пример, противопоставляя ему категорию из одного. [уточнить: что меняется в клинике после внедрения и в каких цифрах; в каких клиниках вы это уже сделали]

**2. 🟡 Состав — список работ, а не решённых проблем; бонусов нет**
> Что входит: аудит процессов клиники, настройка CRM, интеграция с телефонией и сайтом, обучение администраторов (3 сессии), поддержка 60 дней после запуска.

Каждый пункт назван по тому, что делаете вы. По 02.21 каждая часть стека пишется как проблема → формулировка решения → название блока, а аудит, настройка и интеграция идут под ним как способы доставки. Бонусов нет, хотя 03.11 велит давать их всегда: у каждого название с выгодой, обоснованная цена и прицел на одно конкретное препятствие клиента, а вместе они стоят больше ядра. Самые обособленные и короткие части вашей же работы можно вынуть из общего списка и подать как бонусы (03.14). [уточнить: какую проблему клиники снимает каждый пункт и что мешает клиникам решиться на внедрение]

**3. 🟡 Безусловный возврат на B2B-услуге за 350 000 ₽**
> Гарантия: 100 % возврат денег в любой момент без объяснения причин.

Гарантия «без объяснения причин» по 03.18 — для низкого чека и уверенного исполнения; с ростом чека и стоимости исполнения она становится очень рискованной. Для бизнес-клиента 03.17 ведёт к конкретной, условной гарантии, а если исполнение дорого вам обходится — к условной гарантии или anti-guarantee, но не к безусловному возврату: иначе вы возвращаете деньги, уже потратившись на аудит, интеграцию и обучение. «В любой момент» не ограничено даже 60 днями поддержки. В формулировке нет X и Y из формулы «если вы не получите X за Y, мы сделаем Z» (03.15). Решать о гарантии правило велит арифметикой чистых продаж после возвратов, а не страхом злоупотреблений (03.16). Замена — условная гарантия, где условия — ключевые действия клиники (03.19), например из вашего же состава: администраторы прошли все 3 сессии обучения. [уточнить: какой измеримый результат X за какой срок Y вы готовы гарантировать; сколько вам стоит одно внедрение]

**4. 🟡 Скидка на весь оффер и без причины**
> Скидка 30 % при оплате до конца месяца.

Срок на цене сам по себе допустим: для услуги, которую продают круглый год, 03.9 ставит дедлайн на промо, цену или бонусы, а не на доступность услуги. Но скидка снимается со всего ядра, а 03.31 велит ядро не дисконтировать, иначе покупатели учатся брать только со скидкой: оффер дробят и скидку дают на одну часть. Причины у скидки нет, а 03.28 требует у скидочного предложения правдивого «почему». Цена вопроса: 350 000 × 0,7 = 245 000 ₽, то есть каждая сделка до конца месяца отдаёт 105 000 ₽. Если эта строка стоит в каждой ежемесячной рассылке, реальная цена — 245 000 ₽, а 350 000 ₽ остаются на бумаге [уточнить: скидка повторяется каждый месяц?]. Срочность можно сохранить, перенеся дедлайн на бонусы (03.9) при неизменной цене: разрыв между ценой и ценностью расширяют добавлением ценности, а не снижением цены (02.29).

**5. 🟢 Дефицит без лимита**
> Осталось 3 места в этом месяце.

Honest Scarcity (03.4): назвать, сколько клиентов вы готовы взять за период, объявить это число и сообщать, насколько вы к нему близки. Здесь есть остаток, но нет самого лимита; по образцу Growth Rate Cap (03.3), только на ваш период, это звучит как «берём N новых клиник в месяц, столько-то мест уже занято». В шаблоне рассылки остаток зашит текстом и не меняется, сколько бы писем ни ушло, поэтому о близости к лимиту он ничего не сообщает. [уточнить: сколько внедрений в месяц команда реально выдерживает]

**Экономика**

**6. 🟡 Один оффер, после него — ничего**
> поддержка 60 дней после запуска.

В письме одна покупка по одной цене: клинике, которая откажется от 350 000 ₽, нечего предложить, и после 60 дней поддержки тоже ничего не продаётся. 16.10 называет это антипаттерном: прибыль делают второй, третий и четвёртый офферы, а downsell подбирает тех, кто сказал «нет». Модель денег — это последовательность attraction, upsell, downsell, continuity (10.35). [уточнить: что клиника покупает у вас после запуска и что вы предлагаете тем, кто отказался]

**Канал**

**7. 🟡 Холодное письмо сразу просит 350 000 ₽**
> Стоимость: 350 000 ₽.

По Hormozi Law (03.2) чем больше просьба, тем длиннее разбег перед ней, а здесь крупная сумма названа в первом же касании. По 03.26, если бизнес только начинает, объём мал или стоимость привлечения не выдерживается, премиум-оффер холодной аудитории в лоб не продают, а заворачивают неизменным в бесплатный или скидочный вход; премиальный вход — для тех, у кого уже есть репутация, объём и терпимая стоимость привлечения. Кандидат на вход уже есть в составе — «аудит процессов клиники»: 03.31 разрешает скидку на одну часть оффера, а Two-Step Sale (03.33) продаёт дешёвый первый шаг и ядро на второй встрече. Два правила здесь стоят рядом: 03.27 советует делать единственный вход бесплатным, а 03.33 для услуг, где время исполнителя дорого, велит брать за первый шаг деньги или отдавать его ассистенту — аудит как раз требует времени специалиста. [уточнить: сколько клиник получили письмо, сколько ответили и знают ли вас стоматологии]

**Вердикт.** В нынешнем виде письмо — commodity-оффер: оно перечисляет работы и цену, поэтому клиника сравнивает его с любым интегратором по цене, а скидка 30 % это сравнение только закрепляет. Метод чинит сначала оффер, потом то, как его доносят (01.1), да и вход по 03.26 оборачивают вокруг уже готового Grand Slam Offer, которым этот оффер пока не стал. Поэтому первое — вписать в заголовок измеримый результат клиники и доказательство, что он достижим (02.3, 02.7), и переписать состав как проблемы клиники с решениями и бонусами (02.21, 03.11); «за 30 дней «под ключ»» при этом оставить — это работа по нижней части Value Equation, сроку и усилиям клиента (02.8). Второе — заменить скидку на ядро бонусами со сроком (03.9), а безусловный возврат — условной гарантией «X за Y, иначе Z» (03.15, 03.19). Нужен ли вход через аудит (03.26, 03.33), решат цифры отклика рассылки, которых в запросе нет.

### Baseline output

Коротко: оффер продаёт процесс («внедрим CRM»), а не результат для клиники. Слабые места он закрывает слишком агрессивными приёмами: безусловным возвратом, скидкой и дефицитом одновременно. Для владельца стоматологии это похоже на рекламу инфобизнеса, а не на предложение подрядчика, которому можно доверить пациентов и администраторов. Ниже разбор по пунктам, от главного к второстепенному, и в конце пример переделки.

##### 1. Продаёте инструмент, а не результат

Владельцу клиники CRM не нужна. Ему нужно, чтобы:
- пропущенные звонки и заявки с сайта не пропадали;
- первичный пациент доходил от звонка до кресла;
- пациенты с незакрытым планом лечения возвращались;
- на гигиену приходили раз в полгода, а не «когда вспомнят»;
- было меньше неявок;
- было видно, где теряются деньги и кто из администраторов не дорабатывает.

В оффере нет ни одного из этих результатов. Заголовок «Внедрим CRM за 30 дней „под ключ“» описывает вашу работу, а не то, что изменится в клинике. Такой же заголовок может поставить любой интегратор, поэтому письмо не отличить от десятка похожих.

**Что сделать:** в заголовок и первые строки вынести результат в понятных клинике единицах: записи, пациенты, рубли. Например: «Перестаньте терять пациентов между звонком и креслом».

##### 2. Нет причины поверить

Сейчас в тексте нет ничего, что подтверждает, что вы умеете это делать именно для стоматологий:
- **Нет кейсов и цифр.** Сколько клиник внедрили, что изменилось: доля обработанных звонков, конверсия в запись, возвраты по планам лечения.
- **Нет стоматологической специфики.** «Аудит процессов» и «настройка CRM» подходят автосервису так же, как клинике.
- **Не упомянута МИС.** Это, пожалуй, самый важный пробел по сути. В большинстве клиник уже стоит медицинская информационная система с расписанием и картами пациентов (IDENT, Инфоклиника, МЕДОДС, 1С:Медицина и т. п.). Первое возражение будет таким: «У нас уже есть IDENT, зачем нам ещё CRM?» Нужно прямо написать, с какими МИС вы интегрируетесь и чем CRM дополняет МИС, а не дублирует её.
- **Не назван сам продукт.** Какая CRM? Входит ли лицензия в 350 000 ₽ или это отдельный ежемесячный платёж? Что будет после 60 дней поддержки? Скрытые будущие расходы — частая причина отказа, а молчание о них выглядит как попытка скрыть.

##### 3. Главный страх клиента не закрыт

Владелец боится не того, что вы плохо настроите систему. Он боится, что **администраторы не будут в ней работать**, и через три месяца он останется с дорогой пустой CRM. Администраторы в стоматологиях к тому же часто меняются.

«Обучение администраторов (3 сессии)» этот страх не снимает. Лучше показать, как вы добиваетесь, чтобы система реально использовалась:
- регламент и скрипты для администраторов;
- автоматические задачи вместо ручного ввода;
- отчёт для руководителя, где видно, кто что не обработал;
- видеоуроки для новых сотрудников;
- контроль заполнения в период поддержки.

##### 4. Гарантия опасна для вас и неубедительна для клиента

«100 % возврат денег в любой момент без объяснения причин» плохо работает с обеих сторон.

- **Для вас это финансовый риск.** «В любой момент» значит и через 59 дней, когда аудит проведён, интеграции сделаны, администраторы обучены. Клиника может забрать деньги и остаться с настроенной системой. Такие условия притягивают как раз тех клиентов, которые ими воспользуются.
- **Для клиента это звучит неправдоподобно.** В B2B-услуге за 350 000 ₽ безусловная гарантия без срока вызывает не доверие, а вопрос «где подвох?».
- **Она гарантирует не то.** Клиенту важно, что система заработает, а не то, что ему вернут деньги.

**Что сделать:** привязать гарантию к измеримому результату и к обязательствам клиники. Например:
- «Если через 60 дней после запуска в CRM фиксируются не все входящие звонки и заявки с сайта, дорабатываем бесплатно, пока не заработает»;
- или поэтапная оплата: аудит оплачивается отдельно, и если после него клиника решает не продолжать, отчёт остаётся у неё, а за внедрение она не платит. Такой вариант снижает риск клиента честнее, чем обещание вернуть всё.

##### 5. Скидка и «3 места» разрушают доверие

- **«Осталось 3 места в этом месяце» в массовой рассылке.** Все получатели видят одну и ту же фразу, и многие это понимают. Дефицит без объяснения причины читается как манипуляция.
- **«Скидка 30 % до конца месяца».** Получается, что реальная цена 245 000 ₽, а 350 000 ₽ завышены. Скидка обесценивает услугу и сдвигает разговор с результата на торг. Кроме того, в клинике решение за 350 000 ₽ часто принимают вместе с партнёрами или главврачом, и срок «до конца месяца» может просто не совпасть с их циклом.
- **Всё вместе:** безусловный возврат, скидка и дефицит в пяти строках — тройное давление. Владелец клиники — обычно врач или предприниматель с опытом, и на такое он реагирует настороженно.

**Что сделать:**
- если ограничение реальное, назовите причину: «Мы берём не больше 4 клиник в месяц: аудит и обучение ведёт один специалист. На ноябрь свободно 2 места»;
- вместо скидки дайте бонус, который добавляет ценность: «При старте до 15 ноября дополнительно настроим автоматические напоминания о визитах и сценарий возврата пациентов на гигиену». Цена сохраняется, а срок начинает работать на результат.

##### 6. Цена ни с чем не сравнивается

Сама по себе сумма 350 000 ₽ ощущается как «дорого». Её нужно сопоставить с тем, сколько клиника теряет сейчас. Логика такая (цифры условные, подставьте свои реальные данные):

> Если клиника теряет хотя бы 10 первичных пациентов в месяц из-за пропущенных звонков и отсутствия перезвона, а средний чек первичного лечения 40 000 ₽, это 400 000 ₽ выручки в месяц. Внедрение окупается за первый месяц работы.

Если у вас есть данные по реальным клиентам, эта часть становится самой убедительной в письме.

##### 7. Нет следующего шага

Письмо заканчивается на «осталось 3 места», и непонятно, что делать дальше: позвонить, ответить, куда-то записаться? К тому же холодное письмо просит сразу принять решение на 350 000 ₽. Это слишком большой шаг для первого контакта.

**Что сделать:** предложить бесплатный первый шаг, который сам по себе приносит пользу. Например: «Дайте доступ к записям звонков за неделю. Мы прослушаем их и за 30 минут покажем, сколько записей вы потеряли и на каком этапе». Такой разбор одновременно служит доказательством экспертизы и подводит к продаже.

##### Пример переделки

Все цифры, названия и кейсы ниже — заглушки. Подставьте только реальные данные: придуманный кейс в письме владельцу клиники вскроется на первой же встрече.

```
Тема: Сколько пациентов ваша клиника теряет между звонком и креслом

В стоматологиях, с которыми мы работали, до внедрения терялось [X–Y %]
обращений: пропущенные звонки, заявки с сайта без перезвона, пациенты,
которые не вернулись по плану лечения.

Мы выстраиваем систему, в которой обращения не теряются:
— каждый звонок и заявка с сайта попадают в CRM, пропущенный звонок
  сразу становится задачей на перезвон;
— запись синхронизируется с вашей МИС ([IDENT, Инфоклиника, ...]);
— пациенты с незакрытым планом лечения и те, кому пора на гигиену,
  попадают в список обзвона автоматически;
— вы видите в отчёте, сколько обращений стало записями и на каком этапе
  теряются остальные.

Клиника «[название]», [N] кресел: за [3] месяца после запуска
[конкретный результат в цифрах].

Срок запуска — 30 дней. Стоимость — 350 000 ₽,
лицензия CRM — [сумма] ₽ в месяц, оплачивается отдельно.
Оплата в два этапа: [аудит] и [внедрение после согласования плана].

Гарантия: если через 60 дней после запуска в CRM фиксируются
не все обращения, дорабатываем бесплатно, пока не заработает.

Мы берём [4] клиники в месяц, на [месяц] свободно [2] места.

Первый шаг бесплатный: пришлите записи звонков за неделю, и мы покажем,
сколько записей вы потеряли и почему. 30 минут, без обязательств.
[Контакт / кнопка записи]
```

##### Главное, если менять только три вещи

1. Заголовок и первые строки: результат для клиники вместо «внедрим CRM».
2. Безусловный возврат заменить гарантией результата или поэтапной оплатой.
3. Убрать скидку и немотивированный дефицит, добавить понятный бесплатный первый шаг.

### Grader verdicts

| # | assertion | with skill | baseline |
|---|---|---|---|

| 1 | At least one finding quotes the guarantee line verbatim («100 % возврат денег в любой момент без объяснения причин») and names a conditional guarantee (with key actions as conditions) or an anti-guarantee in place of an unconditional refund for a service with a high cost of fulfilment, citing 03.17, 03.19 or 03.20, or the construct's name. | ✅ «> Гарантия: 100 % возврат денег в любой момент без объяснения причин. ... Для бизнес-клиента 03.17 ведёт к конкретной, условной гарантии, а если исполнение дорого вам обходится — к условной гарантии или anti-guarantee, но не к безусловному возврату ... Замена — условная гарантия, где условия — ключе» | ❌ «**Что сделать:** привязать гарантию к измеримому результату и к обязательствам клиники.» |

| 2 | At least one finding quotes the discount line («Скидка 30 % при оплате до конца месяца») and names the missing reason why, citing 03.28, 07.32 or the construct's name ("reason why"). | ✅ «> Скидка 30 % при оплате до конца месяца. ... Причины у скидки нет, а 03.28 требует у скидочного предложения правдивого «почему».» | ❌ «**«Скидка 30 % до конца месяца».** Получается, что реальная цена 245 000 ₽, а 350 000 ₽ завышены.» |

| 3 | Every finding has a severity mark, a verbatim quote from the material and a rule cited as `NN.M`; there are at most seven findings; the review ends with a verdict paragraph. | ✅ «**1. 🔴 Письмо продаёт работу, а не результат** ... **6. 🟡 Один оффер, после него — ничего** > поддержка 60 дней после запуска. ... 16.10 называет это антипаттерном ... **7. 🟡 Холодное письмо сразу просит 350 000 ₽** > Стоимость: 350 000 ₽.  По Hormozi Law (03.2) ... **Вердикт.** В нынешнем виде пись» | ❌ «## 1. Продаёте инструмент, а не результат» |

| 4 | The scarcity line («Осталось 3 места в этом месяце») is not marked 🔴. | ✅ «**5. 🟢 Дефицит без лимита** > Осталось 3 места в этом месяце.» | ✅ «**«Осталось 3 места в этом месяце» в массовой рассылке.** Все получатели видят одну и ту же фразу, и многие это понимают.» |

| 5 | The answer attributes no results, prices, clients or services to the business that the material does not give. | ✅ «[уточнить: что меняется в клинике после внедрения и в каких цифрах; в каких клиниках вы это уже сделали]» | ❌ «Срок запуска — 30 дней. Стоимость — 350 000 ₽, лицензия CRM — [сумма] ₽ в месяц, оплачивается отдельно.» |



## M-02. Review of an ad: an unknown bookkeeping brand leading with 50 % off to a cold, broad audience

### Request

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

### Output with the skill

**1. 🟡 Offer: 50% off, but no price to compare it to, and the discount is on the whole service**
> "50% OFF your first 3 months of bookkeeping"

Using a discount isn't the mistake. For a business that's just starting out, 03.26 says to wrap the offer in a free or discount front end instead of leading with a premium offer. 03.27 goes a step further: if you can make only one front-end offer, make it free. And 50% passes 03.30's bar of "massive discounts (50% or more)"; a small 5–25% discount wouldn't (Lost Chapters, 2025). The trouble is how this one is built:
- **No price anywhere.** 03.30 has its own caveat for this: if people don't know what the service costs, the discount means nothing. Its example is 50% off an agency retainer. So state the price first, then the discount. Also test the four ways to show a discount: percent off, amount off, a relative equivalent, and the discounted price alone.
- **It discounts the core service itself.** 03.31 says to split the offer into pieces and discount one of them instead. If buyers always see the core offer discounted, they learn to buy only when it's on sale.

[to clarify: Ledgerly's regular monthly price, and whether small business owners in your audience know what bookkeeping usually costs]

**2. 🟡 Offer: no reason why**
> "🔥 50% OFF … — this week only!"

A company nobody knows is offering half price and doesn't say why.
- 03.28 (Lost Chapters, 2025): every crazy free or discount offer needs a good and true reason why. An offer that seems too good to be true gets no response.
- 07.32 (ACQ Advertising Handbook, 2025): every big promotion needs a stated motive that is believable and as big as the offer.

For a business that sells all year, the deadline belongs on the promotion, not on the service. The ad gets that right (03.9), but the deadline also has to be true.

[to clarify: why you're giving 50% off, and whether the offer really ends after this week]

**3. 🟡 Economics: one ad, and no testing rules for the budget**
> "Budget: $150/day. New ad account."

A first campaign on a new account is the Lose Money phase of 06.15 ($100M Leads, 2023). Two things come before the first dollar:
- tracking of returns that works;
- a monthly amount you've decided you can lose, and expect to lose, on tests until one ad wins. At $150 a day that is $150 × 30 = $4,500 a month.

06.16 ($100M Leads, 2023) sets a limit for each ad. An ad that brings leads gets up to 2× the cash you collect from a customer in their first 30 days. An ad that brings no leads is turned off before it spends 1× that amount. Your discount halves that 30-day cash. If you bill monthly:
- 30-day cash = 0.5 × monthly price;
- an ad that brings leads gets up to 2 × 0.5 = one full monthly price;
- an ad that brings none is turned off before 1 × 0.5 = half a monthly price.

The whole budget also sits behind a single ad. 07.2 says to run as many ads as you can until you have your first winner. Until then, new ads come from the 20 ad frameworks, 07.7–07.26 (07.1).

[to clarify: whether you track leads, signups and cash for each ad; whether $4,500 a month is money you've decided you can lose while testing; how you bill]

**4. 🟡 Channel: the whole country as your first audience**
> "Audience: United States, 25–65, interest "small business"."

06.3 ($100M Leads, 2023) says to start with a small, specific audience and add filters early. You widen it only after the small audience has been profitable. Its caveat says filters-first is for early campaigns with a limited budget, which is exactly your situation. One broad interest across the whole country and a 40-year age range is the opposite. If you have any customers or contacts, 06.2 builds a lookalike audience from that list, best contacts first: current and past customers, then warm contacts, then cold leads. If you can't build one, start from interests, narrowed down.

[to clarify: whether you already have any customers or a contact list]

**5. 🔴 Channel: the ad opens with an offer to people who've never heard of you, and it doesn't say who it's for**
> "🔥 50% OFF your first 3 months of bookkeeping — this week only!"
> Headline: "Ledgerly — Bookkeeping Made Simple"

**The hook leads with the offer.** 06.24 (GOATed Ads playbook, 2025): don't open with the offer to a broad cold audience unless it already knows both the brand and the product. What makes that hook work is how well the audience knows you, not how big the advertiser is. Subway's $5 Foot Long worked nationwide because the whole country already knew Subway. A hook that leads with the offer is written for the Most Aware level of 06.23. You said nobody knows you yet, so the whole-US audience of a new ad account doesn't know Ledgerly. The sheet says leading with the offer to the whole country, when people don't know you, is about as close as you can get to burning money.

**Nobody is called out.** 06.5 builds every ad in three parts: callout, then value, then CTA. The most important thing, by far, is that people notice the ad. Neither your first line nor your headline says who the ad is for, and the headline names the company instead of the buyer. 06.6 lists four ways to call someone out in words: a Label, a Yes-Question, an If-Then Statement, a Ridiculous Result.

For people who know less about you, 06.23 matches the hook to how much they know:
- they know solutions exist: a hook built on a promise;
- they know the problem: a hook built on the pain;
- they don't know they have a problem: a hook built on curiosity.

Its caveat: these are frameworks, not a recipe, and when in doubt, go a little broader.

**6. 🟡 Channel: one line of value and no proof**
> "Ledgerly does your books so you don't have to."

That sentence is the whole value section of the ad. It uses only one of the eight key elements from 06.9, effort, and only from the owner's point of view, today. 06.8 ($100M Leads, 2023) builds the value section by taking the eight elements and looking at each one from several points of view and across time:
- **the eight elements:** Dream Outcome and Nightmare, Perceived Likelihood and Risk, Time Delay and Speed, Effort and Sacrifice and Ease;
- **the points of view:** the owner and the people around him (06.10);
- **time:** past, present and future.

An unknown company most needs to raise Perceived Likelihood, the buyer's belief that it will work for them. 06.9 raises it with results from people like them, authority and guarantees, and the ad has none of these. 07.36 lists as many proof points as possible as a must-have for the script, though its caveat treats a missing must-have as a flag, not an automatic fail. "Bookkeeping Made Simple" describes the problem in general terms. 07.29 describes it with numbers, thresholds and moments that only an insider would know.

[to clarify: what proof you have: customers, results, credentials, a guarantee]

**7. 🟡 Next step: two different asks, and the click goes to your homepage**
> "Sign up today."
> "CTA button: Learn More → links to our homepage"

The text says to sign up, the button says to learn more, and the click goes to your general homepage.
- 07.36 requires one clear next step, both said and shown.
- 06.12 ($100M Leads, 2023): the ad and its landing page don't sell. They ask whether the person is interested and take contact details in exchange, by default on a simple landing page.
- 06.13: each step should remind people of the step they just took. A homepage that doesn't repeat the 50% offer breaks that.
- 06.14: show what the next step looks like, don't only describe it.

[to clarify: what the homepage asks visitors to do, and whether it shows the 50% offer]

**What I couldn't check**
- The image or video. The visual half of 07.36 needs it: matching verbal and visual hooks, movement, people who look like your buyer, captions, and a format native to the placement. [to clarify: the creative]
- Whether paid ads are your first channel at all. The method puts paid ads last of the Core Four (05.7). [to clarify: whether you've done any warm outreach or have any customers yet]

**Verdict**

As it stands, the ad can't do its job. Its first line is an offer from a brand nobody knows, shown to the whole country, which is exactly what 06.24 rules out. Fix the first line and the audience first, together:
1. Write a callout that names the small business owner (06.5, 06.6), with a hook built on their problem or the result they want rather than on the discount (06.23). Show it to a narrower audience (06.3).
2. Keep the 50% off, but move it out of the first line and add the price and a true reason why (03.30, 03.28).
3. Send the click to a page that repeats the offer and asks for contact details (06.12).
4. Then launch several versions instead of one, with a testing budget you've decided you can lose and a spending limit for each ad (06.15, 06.16, 07.2).

### Baseline output

**Short version:** the ad asks strangers to buy, on price alone, from a company they've never heard of, in a category that runs on trust. It gives them no reason to believe you, no reason to pick you over QuickBooks Live or a local bookkeeper, and a discount on a price they can't see. The fixes are cheap. Make them before the $150/day starts.

##### What's wrong, most important first

**1. The whole pitch is a discount, and discounts don't work on cold traffic.**
"50% off" only means something when people already know what you cost and believe you're worth it. Nobody knows Ledgerly, so the discount reads as "we're cheap" and nothing else. It also causes three business problems:
- It pulls in the most price-sensitive owners, who are the ones most likely to cancel in month 4 when the price doubles.
- Bookkeeping costs you the most in the first months (setup, catch-up, cleaning up messy accounts). You'd be discounting your most expensive months.
- It sets your price anchor at half price from day one.

**2. "This week only" is fake urgency, and it will backfire.**
A brand-new company running a 7-day deadline looks like a spam ad. On a new ad account, the first week is roughly the length of Meta's learning phase, so the ad would expire just as delivery stabilises. If you then extend the deadline, the claim becomes false, and regulators treat fake countdowns as a deceptive practice. There is real urgency you can use: it's late September, year-end is coming, and every owner who is behind on their books will get an ugly bill from their CPA in the spring. "Get caught up before year-end" is true, and it's stronger.

**3. It doesn't speak to anyone in particular.**
"Small business, US, 25–65" covers a food truck, a dental practice, a Shopify store and a roofing contractor, and each has a different bookkeeping headache. The copy doesn't call out any of them, so nobody feels it's about them. Pick one or two segments you can serve well and name them in the first line ("Contractors:", "Running a Shopify store?"). Broad targeting on Meta is fine now. In practice, the creative does the targeting.

**4. There's no proof, in a category where proof is everything.**
You're asking people to hand over their bank feeds and tax exposure to an unknown company. The ad says nothing about who does the work (real bookkeepers? certified? US-based?), gives no numbers, no clients, no reviews and no guarantee. Even one line of proof changes how the ad reads, for example "Every account handled by a dedicated bookkeeper" or "[N] businesses' books closed on time last month." Before launch, also check what people find when they google "Ledgerly reviews". Cold prospects will.

**5. The promise is generic.**
"Does your books so you don't have to" and "Bookkeeping Made Simple" are what every competitor says. Sell the outcome instead: books closed by a set day each month, a P&L they can actually read, tax-ready files for their CPA, no more Sunday nights with receipts. Show the price too. A flat, visible monthly price is a differentiator in a category known for vague quotes.

**6. The CTA contradicts itself and points to the wrong place.**
The text says "Sign up today", the button says "Learn More", and the link goes to the homepage. That's three different asks. Nobody signs up for bookkeeping from a feed ad on first sight: it's a considered purchase. Offer a smaller first step that's easy to say yes to, such as a free books review, a free catch-up estimate or a 15-minute call. Send people to a landing page built for this ad, with the same promise, the price, the proof and one form. The homepage makes them go looking.

**7. There's only one ad.**
The first campaign's real job is to find out which message works. One ad gives you one data point. Launch 3–5 variants with different angles (pain, outcome, flat price, niche callout, proof) and let the numbers choose.

**8. The brief doesn't mention a visual.**
In the feed, the image or video is what stops the scroll, and the text only gets read after that. If the visual is a stock photo of a smiling person at a laptop, that's a bigger problem than anything in the copy. Consider a short founder or bookkeeper video, a screenshot of the monthly report a client receives, or a before/after of a messy spreadsheet next to a clean P&L.

##### Setup issues on the account side

- **Tracking.** Install the Meta Pixel plus the Conversions API and define the conversion event (lead form submitted, call booked, signup) before launch. Optimise for that event, not for link clicks or traffic. A traffic objective buys cheap clicks from people who never convert.
- **Budget vs. learning.** $150/day is about $1,050/week. If a lead costs $50–100, that's only 10–20 conversions a week, well below the roughly 50 per ad set that Meta's learning phase wants. Keep to one campaign and one ad set with several ads inside. Optimise for the most frequent event that still means something, which is usually the lead or the booked call, not the paid signup.
- **Know your ceiling before you spend.** Monthly price × average months retained × gross margin gives the value of a customer. Multiply that by your lead-to-customer close rate and you get the most you can pay per lead. Decide in advance what number makes you pause an ad.
- **New ad account.** Expect lower spending limits at first and more ad reviews. Verify the business in Business Manager, and don't be alarmed if the first days deliver unevenly.
- **Plan retargeting now.** Most people won't convert on first sight. A second, cheap ad set shown to landing-page visitors, carrying proof (a client quote, how onboarding works, the guarantee), is often where the conversions come from.

##### A rewrite to start from

Fill the brackets with things that are true about Ledgerly. Don't claim anything you can't back up.

**Variant A (pain + real urgency)**
> Behind on your books? Get caught up before year-end, not in a panic in April.
> A dedicated Ledgerly bookkeeper reconciles your accounts every month and sends you a P&L you can actually read. Flat $[X]/month. No hourly billing, no surprises.
> Get a free review of your books: we'll tell you what's missing and what it costs to fix.

Headline: *Tax-ready books for a flat $[X]/month*
Button: **Get Quote** or **Book Now**, linking to a dedicated landing page

**Variant B (niche callout)**
> Contractors: your books shouldn't be a shoebox of receipts and a guess at job profitability.
> Ledgerly closes your books by the [15th] of every month, job costs included, so you know which jobs actually made money.
> See what it would cost for your business. Free 15-minute review.

**Variant C (risk reversal)**
> Your books closed by the [15th] every month, or that month is free.
> [Guarantee only if you can deliver it every time.]

If you want to keep a promotional offer, make it about removing risk rather than cutting price: "first month free, cancel anytime" or "free catch-up for your first [N] months of backlog". Either costs you less than 50% off three months and gives a stranger a reason to try an unknown company.

**What I'd need from you to sharpen this:** your actual monthly price, who does the bookkeeping, any results or quotes from early clients, and which types of business you serve best.

### Grader verdicts

| # | assertion | with skill | baseline |
|---|---|---|---|

| 1 | A finding quotes the opening line ("50% OFF your first 3 months…") and names the problem of leading with an offer-driven hook to a cold, broad audience for a brand nobody knows, citing 06.24 or the rule in words (awareness, callout before the offer). | ✅ «> "🔥 50% OFF your first 3 months of bookkeeping — this week only!" ... 06.24 (GOATed Ads playbook, 2025): don't open with the offer to a broad cold audience unless it already knows both the brand and the product.» | ✅ «**1. The whole pitch is a discount, and discounts don't work on cold traffic.** "50% off" only means something when people already know what you cost and believe you're worth it. Nobody knows Ledgerly, so the discount reads as "we're cheap" and nothing else.» |

| 2 | A finding names the missing callout or the audience being everyone (25–65, all of the US), quoting the audience line or the primary text and citing 06.5, 06.6, 06.7 or 06.3, or the construct's name ("callout"). | ✅ «> "Audience: United States, 25–65, interest "small business"." 06.3 ($100M Leads, 2023) says to start with a small, specific audience and add filters early.» | ✅ «**3. It doesn't speak to anyone in particular.** "Small business, US, 25–65" covers a food truck, a dental practice, a Shopify store and a roofing contractor, and each has a different bookkeeping headache. The copy doesn't call out any of them, so nobody feels it's about them.» |

| 3 | A finding quotes the CTA ("Learn More" or "links to our homepage") and names the mismatch with the hook or the missing next step, citing 07.31, 06.14 or 06.13, or the rule in words. | ✅ «> "CTA button: Learn More → links to our homepage" The text says to sign up, the button says to learn more, and the click goes to your general homepage. ... 06.13: each step should remind people of the step they just took. A homepage that doesn't repeat the 50% offer breaks that.» | ✅ «The text says "Sign up today", the button says "Learn More", and the link goes to the homepage. That's three different asks.» |

| 4 | Every finding has a severity mark, a verbatim quote from the material and a rule cited as `NN.M`; there are at most seven findings; the review ends with a verdict paragraph. | ✅ «7. 🟡 Next step: two different asks, and the click goes to your homepage > "Sign up today." ... 07.36 requires one clear next step, both said and shown. ... Verdict As it stands, the ad can't do its job.» | ❌ «**8. The brief doesn't mention a visual.**» |

| 5 | The answer attributes no click-through rate, cost per lead, conversion rate or business figure to the campaign or the company that the material does not give. | ✅ «At $150 a day that is $150 × 30 = $4,500 a month. ... [to clarify: Ledgerly's regular monthly price, and whether small business owners in your audience know what bookkeeping usually costs]» | ✅ «If a lead costs $50–100, that's only 10–20 conversions a week / Fill the brackets with things that are true about Ledgerly. Don't claim anything you can't back up.» |



## M-03. Review of a sales call: the close of a $6,000 coaching program

### Request

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

### Output with the skill

**1. 🔴 [13:26] He cut the price to save the sale**

> "OK, look — if you sign up today I can do $4,800. That's 20% off, only for today."

The prospect had just said "It's just the money right now". The rule is never to lower the price of the same offer in the moment to win a sale. Someone who wants to pay less now gets a payment plan, and someone who wants to pay less overall gets a Feature Downsell, which changes what they get (11.19). 16.11 names this exact move as an antipattern: "it costs too much" usually means "it costs too much up front", so you change how they pay and keep the full price. The Payment Plan Downsell (11.20) has up to seven steps, from most cash up front to least: a reward for paying in full, financing or a credit card, half now and half later, three payments, evenly spread payments, a free trial. He skipped all of them and gave away $1,200 ($6,000 − $4,800) with nothing in return, while 11.17 makes every concession a trade. 11.19 also names the side effect: customers talk, and anyone who paid $6,000 will hear that someone else got it for $4,800. The one exception in 11.19 is a set price offered to a set number of people and decided in advance, which counts as a price test, not a discount. [to clarify: is $4,800 a test you set up, or did he decide it on the call?]

**2. 🔴 [12:40] He stated the price and asked for questions instead of asking for the sale**

> "It's $6,000. Do you have any questions?"

09.21: never ask "do you have any questions?". In the author's words: "I do not recommend asking prospects for reasons not to buy." The prospect gives one in his very next line. The offer should end with two steps (09.17). First the Ask: is he ready to move forward? Then Drop Price & STFU: state the price and stop talking. The pause after the buying question is the longest of the call, 8 seconds or more. The handbook cites studies where pausing that long raised close rates by 23 to 40% (09.8, ACQ Closer Handbook, 2025). Here there is no buying question, and the silence after the price is filled at once.

**3. 🟡 [12:40] The last stack before the price lists features**

> "So that's the program. Twelve weeks, weekly calls, the templates, the community."

The offer maps the prospect's own problems onto three solutions, each through Problem → Solution → Assure → Benefit → Confirm. The solutions are then stacked, three times in all, before the Ask (09.17, 09.18). This line lists four deliverables and none of his problems. The one problem we know of, "stuck for two years", comes up only after the objection, as an argument. The excerpt starts at 12:40, so the earlier part of the offer isn't visible (16.1). This finding covers only the stack right before the price.

**4. 🟡 [12:58] He argued with the first objection instead of confirming value, and did not ask again**

> "I get it, but you said yourself you've been stuck for two years. Think about what that costs you."

"It's a lot. I'd need to think about it" is a Money objection plus a Stall (09.22). The first objection of a call is not answered head-on (09.23). You acknowledge it, ask permission for one question, and ask whether the program could help get him closer to his goal. Then comes the triage question: what is the biggest thing holding him back, and is anything else holding him back? "But" erases the "I get it" in front of it; the form is "agree… and…" (09.25). Weighing the cost of the problem is the right move on money (09.29). But 09.29 first isolates it ("if you had the money today, would anything else stop you from starting?") and then works from his facts, not from "think about what that costs you". The wife at [13:45] shows money was not the only thing left. His answer also ends without asking for the sale again, and under 09.24 an answer without a fresh ask has not handled the objection.

**5. 🔴 [13:45–13:50] He accepted the decision-maker objection and ended the call with nothing booked**

> "Let me talk to my wife and I'll get back to you." → "Sure, no problem. I'll send you the details by email and you can let me know. Talk soon!"

09.30 handles this in order:
1. Isolate the wife as the only blocker.
2. Ask what her biggest concern would be, and loop that concern as its own objection.
3. Offer the reversal: if she hates the idea, they call you and you make sure they're taken care of.
4. Ask for the order.
5. If he still needs to talk to her, book that conversation.

09.27 (BAMFAM): when a call can't close today, the next call is booked before this one ends. Offer two named times, restate the agreed day and time, send the invite while he is still on the call and have him confirm he got it, then text right away. The rule's Bad example is "We'll follow up offline", which is what his last line amounts to. "I'll send you the details by email and you can let me know" leaves the next step with the prospect.

**6. 🟡 He did most of the talking**

> "Closer talk time: 31 minutes of 40."

09.6: on a close that goes perfectly and takes 15 minutes, the prospect talks for 12 minutes and the closer for 3, so the closer's share is 3 ÷ 15 = 20% (ACQ Closer Handbook, 2025). His share was 31 ÷ 40 = 77.5%, almost four times that, so the ratio is reversed. At 150–170 words per minute, a 500-word script takes just over three minutes (09.5, 09.6, 2025). Any talk beyond that share is his own words, not the script.

**Not visible in this excerpt**
- [to clarify: does he have a written script, and does he deliver it word for word (09.2)? 31 minutes of his own talk suggests he doesn't, but the transcript can't show it]
- [to clarify: did anyone find out before the call, or early in it, that his wife has a say? The first step of 09.30 is to learn this ahead of time and get the decision-maker on the call]
- [to clarify: how long was the offer section? 09.19 gives about two minutes, roughly 320 words (ACQ Closer Handbook, 2025). And did discovery end with his problems labelled in his own words and confirmed (09.11, 09.15)?]

**Verdict.** He didn't lose it at the wife. He lost it at [12:40], when he said the price, followed it with "Do you have any questions?", and never asked for the sale or held the silence (09.17, 09.21, 09.8). After that he never asked for the sale at full price. He argued with the objections instead of looping them, gave away $1,200 for nothing, and let the call end with no date on the calendar. "I'll get back to you" after an email is exactly the outcome BAMFAM exists to prevent (09.27). Fix three things with him, in this order. First, the end of the offer: the ask, the price, then 8+ seconds of silence. Second, no price changes on a call: on money, the only moves are the Payment Plan Downsell steps (11.20) or a trade (11.17). Third, no call ends without the next one booked, with the decision-maker on it (09.27, 09.30). Use this recording as his gametape: script in hand, selling along out loud, rewinding each moment above until he nails it (09.4).

### Baseline output

**Short answer:** The 20% discount at 13:26 is the most obvious mistake, but it's a symptom. The deal was already in trouble before he said the price, because the prospect hadn't talked themselves into it. Then at 13:50 he let it go without booking a next step. There are three mistakes, in the order they happened:

1. The price came with no value built up (before 12:40).
2. He answered a stall with a discount (12:52–13:26).
3. He accepted "talk to my wife" and ended the call (13:45–13:50).

One caveat: I only see the last 75 seconds of the call. What I say about the first 38 minutes comes from the talk-time figure and from how the prospect reacted to the price.

---

###### 1. The price landed cold (12:40)

- **He talked for 31 of 40 minutes, which is 78%.** On a good closing call the prospect does most of the talking. They describe where they are now, where they want to be, what's stopping them and what staying stuck costs them. Here the closer presented and the prospect listened. People buy on what they say themselves, not on what they're told.
- **The pitch ends with a list of what's included:** weekly calls, templates, community. That describes the program. It doesn't say what the program will do for this person. Nothing ties $6,000 to the prospect's own goal.
- **"Do you have any questions?" right after the price** hands the prospect an opening to object, and he takes it: "it's a lot."

**Better:** before the price, sum up the prospect's situation in their own words and get a yes: *"You've been stuck at X for two years, you want Y by [date], and you said what's missing is Z. Is that right?"* Then give the price, ask a closing question (*"Want to get started?"*) and stop talking.

###### 2. The discount (12:52–13:26)

- **12:52: "I need to think about it"** is a stall, not an objection. He didn't ask what the prospect needed to think about: *"Sure. Which part would you be thinking over?"*
- **12:58: "I get it, but..."** The "but" turns it into an argument. He also told the prospect what being stuck costs instead of having the prospect work it out. When prospects put their own number on the cost of staying stuck, it carries weight. When the closer says it, it sounds like pressure.
- **13:20: "It's just the money right now."** Here the real issue comes out, and it could be either of two problems with different fixes:
  - **They don't have the cash right now.** That's a cash-flow problem, and a payment plan fixes it.
  - **They're not sure it's worth $6,000.** That's a value problem, and the fix is to go back to their goal.

  He didn't ask which one it was.
- **13:26: he cut $1,200 off the price when nobody asked for a discount.** That did four kinds of damage:
  - It told the prospect the $6,000 was never a real price.
  - It fixed neither problem. If they don't have $6,000 now, they probably don't have $4,800 either. If they doubt the value, a discount tells them it's worth less.
  - He got nothing in return for it. There was no commitment, no deposit, no decision.
  - "Only for today" was fake urgency, and he dropped it himself 25 seconds later when he agreed to wait. Now the prospect knows his deadlines aren't real.

The prospect answered a 20% discount with a new reason to leave. That shows the discount never touched the real objection.

**Better:** *"Is it the total, or the timing?"* If it's the timing, and you offer a payment plan: *"If we split it into three payments of $2,000, would that work?"* If it's the total: *"Set the money aside for a second. Is this what gets you unstuck?"* If they say yes, you're dealing with a financing problem. If they say no, you're not at the close yet. Go back to discovery.

###### 3. The exit (13:45–13:50)

"Let me talk to my wife" shouldn't come as a surprise at minute 39. Finding out who else decides is part of discovery, and it belongs early in the call: *"If this turns out to be the right fit, is there anyone you'd want to talk it over with before deciding?"* If the answer is yes, the spouse gets invited to the call.

Even at this point he had options:
- **Find out where the prospect stands:** *"Totally fair. How do you feel about it yourself?"*
- **Bring out the real questions:** *"What do you think she'll ask you?"* Often the "wife" objection is the prospect's own doubt.
- **Book a call with both of them:** *"Let's get the three of us on for 20 minutes. Does tomorrow at 7 work?"*

What he actually said was "Sure, no problem. I'll send you the details by email." No date, no time, no commitment, and it's now up to the prospect to get back in touch. Deals that end this way rarely come back.

---

###### What to do with this lead now

- **Call, don't email, within a day.** The call has one goal: get a time on the calendar with the prospect and his wife.
- **On the $4,800:** he's stuck with it now. Taking it back would look like bait-and-switch. Don't bring it up first, but honor it if they ask.

###### What to train the closer on

1. **Discovery where the prospect talks more than the closer.** Aim for the closer under 40–50% of the talk time.
2. **Ask who else decides during discovery,** never after the price.
3. **Before the price, sum up the prospect's problem and goal. After the price, ask a closing question and wait.**
4. **Tell a stall from an objection,** and find out which money problem it is before answering it.
5. **No discounts at the closer's discretion.** Money objections get a payment plan or a diagnosing question, not a lower price.
6. **Every call ends with a booked next step,** never "I'll email you the details."

### Grader verdicts

| # | assertion | with skill | baseline |
|---|---|---|---|

| 1 | A finding quotes "Do you have any questions?" and names the rule against asking it, citing 09.21 or the rule in words. | ✅ «> "It's $6,000. Do you have any questions?" ... 09.21: never ask "do you have any questions?".» | ✅ «**"Do you have any questions?" right after the price** hands the prospect an opening to object, and he takes it: "it's a lot." [...] Then give the price, ask a closing question (*"Want to get started?"*) and stop talking.» |

| 2 | A finding quotes the discount line ("$4,800" or "20% off, only for today") and says the price of the same offer is not lowered in the moment — a payment plan, a trade or a feature downsell instead — citing 11.19, 11.20, 11.17, 16.11 or 09.29, or the rule in words. | ✅ «> "OK, look — if you sign up today I can do $4,800. That's 20% off, only for today." ... The rule is never to lower the price of the same offer in the moment to win a sale. Someone who wants to pay less now gets a payment plan, and someone who wants to pay less overall gets a Feature Downsell, which» | ✅ «If they don't have $6,000 now, they probably don't have $4,800 either. [...] **No discounts at the closer's discretion.** Money objections get a payment plan or a diagnosing question, not a lower price.» |

| 3 | A finding quotes the ending ("I'll send you the details by email and you can let me know" or "Let me talk to my wife") and names booking the next meeting before the call ends — BAMFAM, cited as 09.27, 08.18, 11.4 or 14.24, or by name. | ✅ «> "Let me talk to my wife and I'll get back to you." → "Sure, no problem. I'll send you the details by email and you can let me know. Talk soon!" ... 09.27 (BAMFAM): when a call can't close today, the next call is booked before this one ends.» | ❌ «What he actually said was "Sure, no problem. I'll send you the details by email." No date, no time, no commitment [...] **Every call ends with a booked next step,** never "I'll email you the details."» |

| 4 | Every finding has a severity mark, a verbatim quote from the transcript and a rule cited as `NN.M`; there are at most seven findings; the review ends with a verdict paragraph. | ✅ «**1. 🔴 [13:26] He cut the price to save the sale** ... **6. 🟡 He did most of the talking** > "Closer talk time: 31 minutes of 40." 09.6: on a close that goes perfectly ... **Verdict.** He didn't lose it at the wife.» | ❌ «### 1. The price landed cold (12:40)» |

| 5 | The answer attributes nothing to the program, the closer's close rate or the prospect's situation beyond what the transcript says. | ✅ «The excerpt starts at 12:40, so the earlier part of the offer isn't visible (16.1). This finding covers only the stack right before the price.» | ✅ «One caveat: I only see the last 75 seconds of the call. What I say about the first 38 minutes comes from the talk-time figure and from how the prospect reacted to the price.» |



## M-04. Apply: rewrite a price-raise letter of a subscription accounting service

### Request

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

### Output with the skill

**Диагноз.** Уровень — цена, материал — письмо о повышении. Само повышение метод поддерживает. Рост на 30% (15 600 − 12 000 = 3 600 ₽; 3 600 / 12 000 = 30%) ниже порога в 50%, с которого автор добавляет к письму личный разговор с каждым клиентом (13.15, 2025). Цену уже месяц проверяют на новых клиентах, как требует 13.14. Повышение судят по деньгам, а не по числу клиентов (13.1). Сейчас база приносит 180 × 12 000 = 2 160 000 ₽ в месяц. По полной новой цене ту же выручку дают 2 160 000 / 15 600 ≈ 138,5, то есть 139 клиентов: можно потерять до 41 из 180 (≈23%) без потери выручки. По валовой прибыли запас ещё больше: удержать нужно долю (12 000 − c) / (15 600 − c), где c — себестоимость обслуживания одного клиента в месяц (13.6). Автор видит, что в 9 случаях из 10 повышение приносит больше прибыли, чем теряется в продажах, но это его опыт, а не гарантия, и рынки по-разному чувствительны к цене (13.1, 2025). Проблема в самом письме, и она в трёх местах. Первое: «цена остаётся прежней бессрочно» — это grandfathering, который метод запрещает (13.13). Второе: текст не собран по RAISE (13.17): нет напоминания о ценности, вместо вложений в клиента названы ваши расходы, вопросы уходят в поддержку. Третье: письмо адресовано «всем действующим клиентам разом», а по 13.14 его получают только те, кто пришёл до повышения.

До отправки уточнить:
- [уточнить: сколько из 180 уже платят 15 600 ₽ — они выпадают и из рассылки, и из расчёта выше]
- [уточнить: сколько новых клиентов на 15 600 ₽ оплатили второй месяц — по 13.14 новые должны не только покупать, но и оставаться]
- [уточнить: c — себестоимость обслуживания одного клиента в месяц]

**Письмо**

В фигурных скобках — поля, которые рассылка подставляет для каждого клиента. В квадратных — то, что вы решаете один раз до отправки.

```
Тема: Изменение стоимости обслуживания с 1 ноября

{Имя}, здравствуйте!

Вы работаете с «Клауд-Бухгалтерией» с {месяц и год подключения}. За это время мы {показатель 1}, {показатель 2} и {показатель 3}.
[уточнить: какие 2–3 показателя вы можете выгрузить по каждому клиенту: сколько работ сделано за него, сколько обращений и консультаций, какой результат в деньгах, если вы его считаете]

С 1 ноября 2026 года абонемент «Стандарт» стоит 15 600 ₽ в месяц вместо 12 000 ₽. Новые клиенты уже подключаются по этой цене.

Эти деньги пойдут на три вещи, которые мы запланировали на ближайший год:
1. [вложение 1] — [что это даёт вам].
2. [вложение 2] — [что это даёт вам].
3. [вложение 3] — [что это даёт вам].
[уточнить: три вложения, уже запланированные на 12 месяцев, — более сильные сотрудники, обучение команды, технологии и ПО, уровень сервиса; к каждому — что клиент получит: больше, быстрее, проще или с меньшим риском]

В благодарность за то, что вы с нами, мы даём вам скидку постоянного клиента. Она будет отдельной строкой в каждом счёте:
• ноябрь 2026 — январь 2027: скидка 3 600 ₽, вы платите 12 000 ₽ в месяц;
• февраль — апрель 2027: скидка 1 800 ₽, вы платите 13 800 ₽ в месяц;
• с 1 мая 2027 года — 15 600 ₽ в месяц.

Спасибо, что доверяете нам свою бухгалтерию.

[уточнить: имя и фамилия владельца]
[уточнить: должность], «Клауд-Бухгалтерия»

P.S. Если новая цена ощутимо ударит по вашему бизнесу, ответьте на это письмо и напишите, как именно. Ответ придёт лично мне, я прочитаю каждое письмо и отвечу.
```

**Что изменилось и почему**

- Добавлен блок R (Remind): стаж клиента и 2–3 цифры того, что вы для него сделали. Письмо теперь о клиенте, а не о вас — 13.17.
- «Стоимость… повышается… К сожалению, мы вынуждены пойти на этот шаг» → A (Address): цена одним предложением, без извинений и преамбулы — 13.17.
- «выросли аренда, зарплаты и стоимость программного обеспечения» → I (Invest): три вложения из уже запланированных на ближайшие 12 месяцев, к каждому — что получит клиент — 13.18. Зарплаты и ПО попадают сюда, только если за ними стоит такое вложение (сильнее люди, новые инструменты), а не подорожание того же самого. Называйте только то, что точно сделаете (13.18), и не заводите новых трат ради обоснования повышения (16.18).
- Добавлено «Новые клиенты уже подключаются по этой цене»: тест на новых показывает базе, что рынок уже принял новую цену — 13.14.
- «Для клиентов, которые с нами больше года, цена остаётся прежней бессрочно» → S (Soften): скидка постоянного клиента для всех, кто пришёл до повышения. Она исчезает за 6 месяцев в две ступени и видна строкой в счёте — 13.13; 13.19 (скидка на 3–6 месяцев, 2025). Расчёт: 15 600 − 3 600 = 12 000 ₽ с ноября по январь, 15 600 − 1 800 = 13 800 ₽ с февраля по апрель, с мая 2027 года — 15 600 ₽. Вариант без ступеней: держать 12 000 ₽ три–шесть месяцев и сразу перейти на 15 600 ₽ (13.19, шаблон в 13.17). [уточнить: может ли ваш биллинг показать скидку отдельной строкой]. Новые клиенты скидки не получают — 13.19.
- «Если у вас есть вопросы, обращайтесь в поддержку» → E (Explain) в виде P.S.: написать предлагается тем, по чьему бизнесу цена ударит ощутимо, а ответы идут лично владельцу — 13.17, 13.20. Этот блок сознательно не масштабируется: отвечать придётся самому (13.17). Ответы бывают трёх типов (13.20). Те, кто видит ценность, остаются. Тем, по кому повышение действительно ударило, скидку продлевают ещё на 6 месяцев и возвращаются к разговору после. Те, кто и так собирался уйти, уйдут сейчас. Всплеск оттока в первый месяц — ещё не провал: его смотрят вместе с месяцами 2–3 (13.20).
- «С уважением, команда» → личная подпись владельца — 13.14.
- Рассылка «всем действующим клиентам разом» → только клиентам, которые пришли до повышения — 13.14.

### Baseline output

##### Почему нынешнее письмо может отпугнуть клиентов

1. **Одно письмо уходит всем.** Каждый из 180 клиентов первым делом прочитает «цена растёт на 30 %», в том числе те, кого повышение не касается. Давние клиенты испугаются зря. Клиенты, которые с вами меньше года, узнают, что другим цену оставили, а им нет.
2. **Причина противоречит оговорке.** Вы пишете «выросли аренда и зарплаты», а следующей строкой оставляете части клиентов старую цену. Получается, что дело всё-таки не в расходах. К тому же клиенту ваши расходы не аргумент: он сравнивает вас с другими бухгалтериями.
3. **«К сожалению, вынуждены» звучит как извинение.** Такой тон подталкивает торговаться или искать, где дешевле.
4. **У клиента нет выбора.** Остаётся только согласиться или уйти. Если дать способ сохранить текущую цену, уход перестанет быть единственным ответом на письмо.
5. **«Обращайтесь в поддержку» звучит безлично.** Лучше дать живой контакт и предложить просто ответить на письмо.

Поэтому я предлагаю два письма, по одному на каждую группу клиентов.

---

##### Письмо 1. Клиентам, которые с вами меньше года

**Тема:** Новая цена «Стандарта» с 1 ноября и как сохранить текущую

Здравствуйте, [Имя]!

Пишем заранее, чтобы вы успели всё спокойно спланировать. С 1 ноября 2026 года абонемент «Стандарт» будет стоить 15 600 ₽ в месяц вместо 12 000 ₽, то есть на 3 600 ₽ больше.

Новые клиенты подключаются по этой цене уже с [месяц]. Для вас она меняется только сейчас, и вы можете выбрать, как перейти:

**Сохранить 12 000 ₽ ещё на год.** Оплатите 12 месяцев вперёд до 31 октября: 144 000 ₽ вместо 187 200 ₽ по новой цене, экономия 43 200 ₽. Чтобы получить счёт, просто ответьте на это письмо.

**Перейти на новую цену с 1 ноября.** Делать ничего не нужно, следующий счёт придёт на 15 600 ₽.

Состав абонемента не меняется: [2–3 конкретных пункта, например: ведём учёт и сдаём всю отчётность, отвечаем на вопросы в течение N часов, у вас свой бухгалтер]. [Если за год что-то добавили, напишите одной строкой.]

Если хотите что-то обсудить, ответьте на это письмо или напишите вашему бухгалтеру: [Имя], [телефон / мессенджер].

Спасибо, что работаете с нами.

[Имя Фамилия, должность]
«Клауд-Бухгалтерия»

---

##### Письмо 2. Клиентам, которые с вами больше года

**Тема:** Для вас цена «Стандарта» не меняется

Здравствуйте, [Имя]!

С 1 ноября 2026 года абонемент «Стандарт» стоит 15 600 ₽ в месяц. Вы с нами больше года, поэтому для вас цена остаётся прежней: 12 000 ₽ в месяц, пока вы пользуетесь «Стандартом» без перерыва.

Делать ничего не нужно, счета будут приходить на ту же сумму.

Спасибо, что вы с нами. Если есть вопросы, ответьте на это письмо или напишите [Имя], [контакт].

[Имя Фамилия, должность]
«Клауд-Бухгалтерия»

---

##### Что решить до отправки

- **С какой даты считать «больше года».** Выберите дату, на которую считаете стаж, например 1 ноября, и разделите по ней список клиентов. Иначе клиент, у которого год исполняется в ноябре, окажется в спорной зоне и сразу напишет вам с вопросом.
- **Что значит «бессрочно».** В письме я заменил это слово условием «пока вы пользуетесь „Стандартом“ без перерыва». Решите, что будет при паузе, смене тарифа или переоформлении на другое юрлицо, и закрепите это в оферте или договоре. Бессрочное обещание придётся выполнять и при следующем повышении.
- **Нужна ли предоплата за год.** Плюсы: вы сразу получаете деньги, а оплатившие клиенты точно не уйдут в течение года. Минус: они ещё год платят старую цену. Если такой вариант вам не подходит, уберите блок с выбором, а тему письма замените на «Новая цена „Стандарта“ с 1 ноября». Можно предложить более мягкий вариант: оплату за 6 месяцев (72 000 ₽).
- **Срок уведомления по договору.** Проверьте, за сколько дней вы обязаны предупредить клиента об изменении цены. Сейчас до 1 ноября чуть больше месяца.
- **Готовность бухгалтеров.** Письмо 1 предлагает «просто ответить», поэтому бухгалтеры должны знать условия и быстро выставлять счета на предоплату.

### Grader verdicts

| # | assertion | with skill | baseline |
|---|---|---|---|

| 1 | The answer contains the rewritten letter in full, preceded by a short diagnosis and followed by a list of changes in which at least one line cites a rule as `NN.M` (13.17, 13.13, 13.18, 16.18) or names the RAISE letter or its sections. | ✅ «- Добавлен блок R (Remind): стаж клиента и 2–3 цифры того, что вы для него сделали. Письмо теперь о клиенте, а не о вас — 13.17.» | ❌ «## Что решить до отправки» |

| 2 | The rewritten letter keeps the facts unchanged: 1 ноября 2026, the plan «Стандарт», 12 000 ₽ and 15 600 ₽, the name «Клауд-Бухгалтерия»; if a percentage of the raise is given (30 %), it is shown with its calculation from 12 000 and 15 600. | ✅ «С 1 ноября 2026 года абонемент «Стандарт» стоит 15 600 ₽ в месяц вместо 12 000 ₽.» | ✅ «С 1 ноября 2026 года абонемент «Стандарт» будет стоить 15 600 ₽ в месяц вместо 12 000 ₽, то есть на 3 600 ₽ больше. \| «Клауд-Бухгалтерия»» |

| 3 | The rewritten letter no longer justifies the raise by the company's own risen costs (rent, salaries, software) and no longer promises any client the old price indefinitely. | ✅ «Эти деньги пойдут на три вещи, которые мы запланировали на ближайший год:» | ❌ «Вы с нами больше года, поэтому для вас цена остаётся прежней: 12 000 ₽ в месяц, пока вы пользуетесь «Стандартом» без перерыва.» |

| 4 | The rewritten letter states no fact the request does not give — no past results for the client, no named investments, no discount amount, no deadline — unless it is marked as a placeholder to fill (for example `[указать …]` or `[to clarify: …]`). | ❌ «• ноябрь 2026 — январь 2027: скидка 3 600 ₽, вы платите 12 000 ₽ в месяц;» | ❌ «Оплатите 12 месяцев вперёд до 31 октября: 144 000 ₽ вместо 187 200 ₽ по новой цене, экономия 43 200 ₽.» |

| 5 | The rewritten letter states the change directly in one sentence and ends with an invitation for anyone materially affected to reply (the A and E sections of RAISE, 13.17 / 13.20). | ✅ «P.S. Если новая цена ощутимо ударит по вашему бизнесу, ответьте на это письмо и напишите, как именно.» | ❌ «С 1 ноября 2026 года абонемент «Стандарт» будет стоить 15 600 ₽ в месяц вместо 12 000 ₽, то есть на 3 600 ₽ больше. \| Если хотите что-то обсудить, ответьте на это письмо или напишите вашему бухгалтеру: [Имя], [телефон / мессенджер].» |



## M-05. Review of a money model: a kids' coding school with a free trial class and nothing after it

### Request

> Here's how our kids' coding school (in-person, Saturday classes) makes money. Tell me what's broken.
>
> ```
> Front end: "First class free" — a Saturday trial lesson. It costs us $15 to deliver a trial. Ads: $2,400/month on Meta, 40 trials/month, 16 of them sign up.
> Main offer: monthly membership $120/month (4 classes), billed month to month, cancel anytime. Gross margin 55%. Average stay: 5 months.
> Nothing else is sold. If a parent says no after the trial, we email them a month later.
> ```

### Output with the skill

**Diagnosis: the economics fail, at the money model.** Going down the checklist, the first line that fails on your numbers is the economics. A new member doesn't pay for himself, and you have nothing else to sell him.

- **CAC, counting every acquisition cost (01.13):** ($2,400 ads + 40 trials × $15) ÷ 16 members = $3,000 ÷ 16 = **$187.50**.
- **Lifetime gross profit (01.12):** $120 × 55% = $66 a month, × 5 months = **$330**.
- **LTGP:CAC:** $330 ÷ $187.50 ≈ **1.76:1**. That's under 3:1 (01.11, 2023), and the author's own caveat is that 3:1 is "a pattern I personally observed, not a rule". At today's CAC, 3:1 would take $562.50 of LTGP (3 × $187.50).
- **The 30-day test fails by more:** month one returns $66 of gross profit against $187.50 of CAC, or 0.35x. That puts you at level 1 of Customer Financed Acquisition (01.20, 2025). It's below the bare minimum for a good Money Model (01.21, 2025) and far from the 2x working standard of $375 (01.19, 2025).
- **Cash:** a member's cost comes back only in the third month ($187.50 ÷ $66 ≈ 2.8 months). Each month you spend $3,000 and get $1,056 back within 30 days (16 × $66). The author says level 1 works only for businesses that already have lots of money (01.20).

This is exactly the case 01.23 covers: LTGP is above CAC, but the first purchase doesn't cover CAC within 30 days. The rule is to sell the customer more right away, instead of waiting for the lifetime profit and instead of cutting CAC. Right now you can't do that. You have one offer, and the 24 of 40 trial families who say no each month (60%) get a single email a month later. That's the one-offer, no-downsell mistake (16.10).

**Steps**

1. **Add one offer inside the first 30 days.** It has to raise month-one gross profit per new member by at least $121.50 to break even ($187.50 − $66), or by $309 to reach 2x ($375 − $66). Size it as take rate × gross profit per sale. Build it from the classes you already run, sold in a new way, and offer it when the parent runs into the problem it solves (01.23, 10.35 Step 2, 10.37, 10.1).
2. **Replace the email a month later with a downsell made to the parent at the trial.** Make another offer as a trade, built from what you already teach, for example fewer classes a month at a lower price (11.17, 11.18, 11.29). Never offer the same membership for less (11.19). A parent who still says no leaves with the next meeting booked (11.4).
3. **Build the new offers one at a time, and hold ad spend until a new member pays for himself.** Start with the offer that brings the most money for the least cost. Raise the $2,400 only once a new member's 30-day gross profit is above $187.50: more ad spend comes after customers pay for themselves (10.7, 10.35, 01.25).

**What I couldn't check**

- [to clarify: does anyone get paid to run the trials, the sign-up conversation and the follow-up? If that pay isn't inside the $15, CAC is higher than $187.50 (01.13).]
- [to clarify: what is the industry-average CAC for kids' coding schools? The sheets have no figure. If your CAC is within 3x of it (2023), the ads are good enough and the work stays on the money model. If it's above 3x, ask the question from 01.16: do the parents who book trials have the problem you solve and the money to pay for it? (01.14, 01.16)]
- [to clarify: how is the membership offered after the trial: face to face with the parent, or by email or a link? A downsell ladder needs a one-on-one setting (16.5).]
- [to clarify: what do enrolled families ask for, or buy elsewhere, after the first few weeks? That's where the offer in step 1 comes from (10.1).]
- [to clarify: how much cash do you have? At level 1, each month's $3,000 takes about three months to come back, which the author accepts only with a large cash reserve (01.20, 01.22).]
- [to clarify: is demand in your area growing? The request gives no figure to check the market line (01.2).]

### Baseline output

**In short:** the front end works fine. The problem is the money model behind it. You pay about $188 to get a family, earn $66 a month from them, and they stay 5 months. Each family nets you about $140 over its whole stay, you wait 3–4 months to get your ad money back, and with this setup the school stops growing at about 80 students.

##### The math

| | Per family |
|---|---|
| Cost per trial (ads $60 + delivery $15) | $75 |
| Acquisition cost (40 × $75 = $3,000 ÷ 16 sign-ups) | **$187.50** |
| Gross profit per month ($120 × 55%) | $66 |
| Lifetime gross profit ($66 × 5 months) | **$330** |
| Lifetime gross profit ÷ acquisition cost | **1.8 : 1** (healthy is 3 : 1 or better) |
| What's left after paying for acquisition | $142.50 |
| Gross profit in the first 30 days vs. acquisition cost | $66 vs. $187.50 (covers 35%) |

Two consequences:

- **Growth is limited by cash.** Every monthly group of 16 families costs $3,000 up front. With about 20% of families leaving each month, a group doesn't pay back its ad spend until month 4. Doubling the ad budget means carrying twice that gap before you see any money back.
- **There's a ceiling.** A 5-month average stay means about 20% of students leave every month. At 16 new students a month, enrollment levels off at 16 ÷ 0.20 = **80 students**. That's $9,600 revenue, $5,280 gross profit, and about $2,280 a month after ads and trials, before any fixed costs that aren't already in the 55%. The only ways past that ceiling are more sign-ups or longer stays.

##### What's broken, most important first

1. **Nothing brings in cash up front.** The trial is free, the first payment is $120, and the plan is month to month. You fund all of the acquisition yourself and wait months to get it back. Fixing this is what lets you scale ads.
2. **Families leave around month 5 because nothing tells them what comes next.** "4 classes a month, cancel anytime" makes the parent decide again every month whether to keep paying, with no finish line to aim for. Five months is about one school term, so families probably leave once their kid has "done coding," or when summer starts.
3. **You sell one product.** Families who love you have nothing else to buy, and families who can't commit to $120 a month have nothing smaller to buy.
4. **You throw away 24 of your 40 trials each month.** You've already paid $75 for each of them, about $1,800 a month, and they get one email a month later. By then the kid's excitement is gone and the parent has forgotten you.
5. **Former students and referrals go unused.** At full size about 16 families leave every month, and nobody follows up with them. Parents of kids in activities talk to each other constantly, but you give them no reason to refer friends.
6. **The price may be low.** $120 for 4 classes is $30 per in-person group class. Compare it with local robotics, chess and coding programs before assuming parents won't pay more.

##### What I'd change

**At the trial (where the sale is made):** end the trial with a 10-minute demo of what the kid built for the parent, then offer a choice instead of just "sign up or not":
- Month to month at $120 plus a **$99 enrollment fee** that includes a starter kit (costs you about $20).
- **Prepay one level** (for example, 12 weeks at $330, with the enrollment fee waived). The level ends with a finished project, like "your kid builds and publishes their own game."

To illustrate (assumed numbers, not a forecast): if all 16 families pay the fee and 6 of them prepay, you collect about $4,700 in the first 30 days against $3,000 spent. Acquisition then pays for itself in month 1 instead of month 4.

**Retention:** organize classes into levels with a visible finish line and a showcase day for parents at the end of each one. At the end of a level, sign families up for the next one. Send parents a monthly progress video. Call any family whose kid misses two Saturdays. Sell a summer camp in spring so summer doesn't end memberships. Stretching the average stay from 5 to 8 months alone raises lifetime gross profit to $528 (ratio 2.8 : 1) and the ceiling to 128 students.

**The 24 who say no:**
- The same day, the instructor texts a photo or video of what the kid built.
- Within 48 hours, call and ask what's holding them back: price, schedule, the kid, or timing.
- Have a smaller option to offer: every other Saturday, a holiday camp, or a spot in the next level's start date.
- Follow with a 2–3 week email and text sequence, then check back at school-term starts.

Turning 4 more of the 24 into members brings acquisition cost down to $150.

**Things to sell besides the membership:** holiday and summer camp weeks, birthday parties, private sessions, a second weekly session or advanced track (Python, robotics), sibling enrollment, and a competition team.

**Referrals and win-back:** hold a bring-a-friend Saturday and give both families a free month when the friend enrolls. Offer former students camps and the next level.

**Price:** test $150. If your cost per student stays the same, monthly gross profit goes from $66 to $96, and lifetime gross profit to $480 (2.6 : 1), even with no other change.

##### What to check before acting

- Are the 40 trials booked or attended? If booked, how many actually show up?
- Does the 55% include rent and teacher pay, or are those fixed costs on top?
- How many students fit on a Saturday? If you're near capacity, raise the price before you raise ad spend.
- What's the pattern behind the 5-month average? Do most families leave after month 1 (the first weeks aren't working) or around months 4–6 (there's no next step)? The fix is different.
- What reasons do the "no" parents actually give?

### Grader verdicts

| # | assertion | with skill | baseline |
|---|---|---|---|

| 1 | The answer computes CAC from the given numbers ($2,400 / 16 = $150, or including the trial delivery cost) and thirty-day gross profit per customer ($120 × 55 % = $66), shows the calculation, and states that the customer does not pay for himself in thirty days (01.18, 01.19, 01.21 or the standard in words). | ✅ «**CAC, counting every acquisition cost (01.13):** ($2,400 ads + 40 trials × $15) ÷ 16 members = $3,000 ÷ 16 = **$187.50**. / $120 × 55% = $66 a month / **The 30-day test fails by more:** month one returns $66 of gross profit against $187.50 of CAC, or 0.35x.» | ✅ «Acquisition cost (40 × $75 = $3,000 ÷ 16 sign-ups) \| **$187.50** ... Gross profit per month ($120 × 55%) \| $66 ... Gross profit in the first 30 days vs. acquisition cost \| $66 vs. $187.50 (covers 35%)» |

| 2 | The answer computes lifetime gross profit (5 × $66 = $330) and sets the ratio to CAC (about 2.2:1) against the method's 3:1 (01.11 or the ratio named). | ✅ «**Lifetime gross profit (01.12):** $120 × 55% = $66 a month, × 5 months = **$330**. / **LTGP:CAC:** $330 ÷ $187.50 ≈ **1.76:1**. That's under 3:1 (01.11, 2023)» | ✅ «Lifetime gross profit ($66 × 5 months) \| **$330** ... Lifetime gross profit ÷ acquisition cost \| **1.8 : 1** (healthy is 3 : 1 or better)» |

| 3 | A finding quotes "Nothing else is sold" or "we email them a month later" and names the missing upsell and the missing downsell after the no, citing 16.10, 11.1, 10.35, 11.17 or 11.29, or the constructs by name. | ✅ «You have one offer, and the 24 of 40 trial families who say no each month (60%) get a single email a month later. That's the one-offer, no-downsell mistake (16.10). / 1. **Add one offer inside the first 30 days.** / 2. **Replace the email a month later with a downsell made to the parent at the trial» | ❌ «3. **You sell one product.** Families who love you have nothing else to buy, and families who can't commit to $120 a month have nothing smaller to buy.» |

| 4 | Every finding has a severity mark, a verbatim quote from the material and a rule cited as `NN.M`; there are at most seven findings; the review ends with a verdict paragraph. | ❌ «**Diagnosis: the economics fail, at the money model.**» | ❌ «1. **Nothing brings in cash up front.** The trial is free, the first payment is $120, and the plan is month to month.» |

| 5 | The answer attributes no show rate, churn reason, price or cost to the school that the material does not give or that is not derived from it with the calculation shown. | ✅ «It has to raise month-one gross profit per new member by at least $121.50 to break even ($187.50 − $66), or by $309 to reach 2x ($375 − $66).» | ❌ «2. **Families leave around month 5 because nothing tells them what comes next.** ... a **$99 enrollment fee** that includes a starter kit (costs you about $20).» |



## B-01. Boundary: a shrinking market — printer cartridge refilling

### Request

> У нас сервис по обслуживанию офисных принтеров и заправке картриджей, 4 точки в городе, 11 сотрудников. Рынок падает примерно на 15 % в год уже пять лет: офисы переходят на электронный документооборот и печатают всё меньше. Выручка падает третий год подряд, клиентов теряем быстрее, чем находим, два конкурента в городе за год закрылись.
>
> Помогите переделать наш оффер и рекламу, чтобы вернуть рост. Готовы вложиться в продвижение.

### Output with the skill

Здесь метод останавливается. Переделать оффер и рекламу для рынка, который сжимается на 15 % в год, мешает граница 01.2: метод рассчитан хотя бы на «нормальный» рынок и не чинит сжимающийся.

**Диагноз.** Метод проверяет бизнес в порядке Starving Crowd > Offer Strength > Persuasion Skills и сначала чинит самый верхний уровень, который не прошёл проверку (01.1). У вас не проходит первый уровень, рынок. Порог такой: рынок растёт хотя бы в темпе рынка в целом и закрывает насущные нужды в здоровье, деньгах или отношениях (01.2, $100M Offers, 2021). Ваш рынок пятый год теряет около 15 % в год. Автор пишет об этом так: «If you don’t have a market for your offer, nothing that follows will work. This entire book sits atop the assumption that you have at least a “normal” market» ($100M Offers, 2021). Рынок оценивают по четырём признакам: Massive Pain, Purchasing Power, Easy to Target, Growing. У вас не выполнен последний. Рынок, который провалил хоть один признак, не выбирают, как бы хорошо он ни выглядел по трём остальным (02.1). Поэтому то, что в городе закрылись два конкурента, результат проверки не меняет. Ваша выручка падает третий год подряд, а метод считает отставанием уже рост меньше 9 % в год (01.5, 2021). В примере автора к 01.1 софт для газет не рос, хотя продукт был отличный, оффер без риска для клиента, а основатель прирождённый продавец. Его рынок сжимался на 25 % в год. Тот же основатель занялся производством масок и через пять месяцев делал миллионы в месяц (2021). Новый оффер и бюджет на рекламу в нынешнем рынке — это работа на уровне ниже того, который не прошёл проверку.

**Три шага**

1. Не переделывайте оффер и рекламу обслуживания принтеров и заправки картриджей и не вкладывайте туда бюджет на продвижение. Пока не пройден уровень рынка, всё, что ниже, работать не будет (01.1, 01.2).
2. Выпишите рынки, куда можно перейти, и проверьте каждый по четырём признакам. Massive Pain: людям это отчаянно нужно, а не просто хочется. Purchasing Power: у них есть деньги на вашу цену. Easy to Target: их можно найти через ассоциации, рассылки, группы или каналы. Growing: рынок не сжимается. Кандидат, который провалил хоть один признак, отпадает. Выбирайте по тому, может ли клиент платить, а не по привязанности к нынешней аудитории (02.1).
3. Когда рынок выбран, оставайтесь в нём достаточно долго, чтобы пройти пробы и ошибки. Только там стройте Grand Slam Offer (листы 02 и 03) и рекламу (листы 06 и 07). Правило niche slap запрещает бросать рынок, если в нём один раз не сработал оффер (01.3). Вы уходите по другой причине: сжимается сам рынок (01.2), так что 01.3 этот уход не запрещает. Но оно запрещает второй прыжок, если в новом рынке не сработает первый оффер.

**Что я не смог проверить**

- [уточнить: откуда цифра −15 % в год — это данные по рынку обслуживания принтеров и картриджей в вашем городе или оценка по вашей собственной выручке]. На этой цифре держится весь диагноз. Если падает только ваша выручка, а рынок нормальный, проблема не на уровне рынка, а на уровне оффера (01.1). Тогда переделывать оффер как раз правильно.
- [уточнить: какие рынки-кандидаты вы видите для своих 4 точек и 11 сотрудников]. Список для шага 2 должен прийти от вас, конкретных рынков метод не называет.
- Как вести четыре нынешние точки, пока идёт переход, метод не отвечает. 01.2 требует нормального рынка для любого его правила, поэтому советов для сжимающегося рынка от имени метода я не даю.

### Baseline output

Начну с неприятного: новый оффер и реклама рост не вернут, если бизнес продолжит продавать то же самое. Рынок, который пять лет теряет по 15 % в год, сжался больше чем вдвое (0,85⁵ ≈ 0,44). Если темп сохранится, через пять лет от сегодняшнего рынка останется меньше половины. Реклама в таком рынке отбирает долю у конкурентов, но сам рынок при этом уменьшается каждый год. Деньги, вложенные в продвижение нынешнего предложения, скорее всего уйдут на то, чтобы падать чуть медленнее.

Зато у вас есть два сильных козыря, и бюджет стоит тратить на них.

##### Козырь 1. Конкуренты уходят, их клиенты свободны

Два конкурента закрылись за год, и их клиентам прямо сейчас нужен кто-то, кто заправит картриджи и починит принтер. На сжимающемся рынке выигрывает тот, кто остался последним: к нему без ценовой войны приходят все, кто ещё печатает.

- Выясните, кому достались клиенты закрывшихся. Если никому, это самый дешёвый рост из доступных: реклама на картах и в бизнес-центрах в районах, где стояли их точки, обзвон офисов поблизости.
- Поговорите с владельцами тех конкурентов, что ещё работают. Слабые могут продать клиентскую базу, договоры и оборудование недорого. Купить базу часто дешевле, чем привести столько же клиентов рекламой.

Пример объявления для этой аудитории:
> «Ваш сервис по заправке закрылся? Заберём картриджи из офиса сегодня, вернём завтра. Первая заправка по цене вашего прежнего договора».

##### Козырь 2. Вы уже работаете в офисах, которые уходят в цифру

Клиенты не исчезают: они перестают тратить деньги на бумагу и начинают тратить их на цифру. У вас есть их доверие, контакты и выездные мастера, поэтому продать им смежные услуги проще, чем найти нового клиента на заправку. Растущие направления:

- **оцифровка бумажного архива**: сканирование и индексация. Каждый, кто переходит на ЭДО, упирается в шкафы с бумагой;
- **уничтожение архива с актом**: шредирование конфиденциальных документов;
- **подключение ЭДО и электронной подписи**: у операторов ЭДО есть партнёрские программы с вознаграждением;
- **ИТ-обслуживание малых офисов по абонентской плате**: компьютеры, сеть, Wi-Fi, видеонаблюдение;
- **продажа и настройка техники**.

Отдельно проверьте сегменты, где печать не падает или растёт: продавцы на маркетплейсах (этикетки, термопринтеры), клиники, школы, госучреждения, юристы, бухгалтерии, склады. Если такие клиенты у вас есть, они должны стать приоритетом для рекламы.

##### Оффер: от разовой заправки к абонементу

Разовую заправку легко сравнить по цене и легко бросить. Клиента удерживает другое предложение, **«Печать под ключ»**:

- фиксированная плата в месяц или цена за страницу, на выбор клиента;
- в неё входят картриджи, обслуживание и ремонт;
- мастер приезжает в течение 4 часов, иначе месяц бесплатно;
- на время ремонта ставим подменный принтер;
- без обязательств на год, можно отказаться в любой месяц.

Клиент заранее знает бюджет и не думает о картриджах. Вам абонемент даёт предсказуемую выручку и меньше ушедших клиентов. Следующий шаг — **«Офис под ключ»**: принтеры, компьютеры и сеть по одному договору. Через него удобнее всего продавать смежные услуги.

##### Сначала закройте утечку клиентов

Пока клиенты уходят быстрее, чем приходят, реклама наливает воду в дырявое ведро. Позвоните 20–30 клиентам, ушедшим за последний год, и спросите почему. Ответ определяет, что делать:

- **перестали печатать** — предлагать оцифровку и ИТ-обслуживание;
- **покупают картриджи на маркетплейсах** — дело в цене или удобстве, тут поможет абонемент с доставкой;
- **перешли на подписку от производителя принтера** — сравнить условия и предложить выгоднее;
- **недовольны сервисом** — сначала чинить сервис, а рекламу запускать потом.

##### Точки и затраты

Четыре точки на падающем рынке могут оказаться лишними. Офисному клиенту нужна не точка, а выезд. Посмотрите выручку и затраты по каждой точке. Возможно, стоит оставить одну-две, а сэкономленную аренду вложить в выездную службу и доставку («забрали — привезли»).

##### Куда тратить бюджет на продвижение

По порядку:

1. **Клиенты закрывшихся конкурентов**: адресная работа в их районах.
2. **Нынешние клиенты**: перевод на абонемент и продажа смежных услуг. Это самые дешёвые продажи.
3. **Прямые продажи в офисы**: обзвон бизнес-центров, партнёрство с управляющими компаниями бизнес-центров.
4. **Карты и контекстная реклама** (Яндекс Карты, 2ГИС, Яндекс Директ): по запросам не только «заправка картриджей», но и «оцифровка документов», «обслуживание компьютеров в офисе».

Каждый канал проверяйте на небольшой сумме и считайте две цифры: сколько стоит привлечь клиента и сколько он приносит за год.

##### План на 90 дней

- **Недели 1–2**: собрать цифры, обзвонить ушедших клиентов.
- **Недели 3–4**: предложить абонемент нынешним клиентам, выйти на клиентов закрывшихся конкурентов.
- **Месяц 2**: запустить одну смежную услугу (оцифровку или ИТ-обслуживание) пилотом на 5–10 нынешних клиентах.
- **Месяц 3**: вложить рекламный бюджет в то, что сработало.

##### Что прислать, чтобы я собрал конкретный оффер и тексты рекламы

- структуру выручки: заправка, ремонт, продажа техники, договоры на обслуживание;
- число клиентов, долю юрлиц и топ-10 клиентов по выручке;
- средний чек и маржу по основным услугам;
- что вы знаете о причинах ухода клиентов;
- что стало с клиентами закрывшихся конкурентов;
- бюджет на продвижение.

С этими данными напишу оффер, тексты объявлений под каждый канал и скрипт обзвона.

### Grader verdicts

| # | assertion | with skill | baseline |
|---|---|---|---|

| 1 | Before any advice on the offer or the ads, the answer states that the method assumes a normal, growing market and does not repair a shrinking one, citing 01.2, 01.1 or the construct's name (Starving Crowd, "a normal market"). | ✅ «Здесь метод останавливается. Переделать оффер и рекламу для рынка, который сжимается на 15 % в год, мешает граница 01.2: метод рассчитан хотя бы на «нормальный» рынок и не чинит сжимающийся.» | ❌ «Начну с неприятного: новый оффер и реклама рост не вернут, если бизнес продолжит продавать то же самое.» |

| 2 | The answer does not deliver an offer rewrite or an ad plan for this market as the fix; any step it gives concerns the choice of market (the four indicators, a niche in a growing need) or is explicitly conditional on the market verdict. | ✅ «Не переделывайте оффер и рекламу обслуживания принтеров и заправки картриджей и не вкладывайте туда бюджет на продвижение. \| Когда рынок выбран, оставайтесь в нём достаточно долго, чтобы пройти пробы и ошибки. Только там стройте Grand Slam Offer (листы 02 и 03) и рекламу (листы 06 и 07).» | ❌ «Пример объявления для этой аудитории: > «Ваш сервис по заправке закрылся? Заберём картриджи из офиса сегодня, вернём завтра. Первая заправка по цене вашего прежнего договора».» |

| 3 | The answer names the four indicators of a market (massive pain, purchasing power, easy to target, growing) as the criterion for the next market, citing 02.1 or the indicators by name. | ✅ «Выпишите рынки, куда можно перейти, и проверьте каждый по четырём признакам. Massive Pain: людям это отчаянно нужно, а не просто хочется. Purchasing Power: у них есть деньги на вашу цену. Easy to Target: их можно найти через ассоциации, рассылки, группы или каналы. Growing: рынок не сжимается. \| Вы» | ❌ «Отдельно проверьте сегменты, где печать не падает или растёт» |

| 4 | The boundary is stated in the first paragraph of the answer, and the answer has at most three steps, each with a rule number of the form `NN.M`. | ✅ «Здесь метод останавливается. Переделать оффер и рекламу для рынка, который сжимается на 15 % в год, мешает граница 01.2 \| Пока не пройден уровень рынка, всё, что ниже, работать не будет (01.1, 01.2). \| а не по привязанности к нынешней аудитории (02.1). \| Правило niche slap запрещает бросать рынок» | ❌ «4. Карты и контекстная реклама (Яндекс Карты, 2ГИС, Яндекс Директ): по запросам не только «заправка картриджей», но и «оцифровка документов», «обслуживание компьютеров в офисе».» |

| 5 | The answer states no market figures beyond the request: no market size, no growth rate of an adjacent market, no competitor data. | ✅ «В примере автора к 01.1 софт для газет не рос, хотя продукт был отличный, оффер без риска для клиента, а основатель прирождённый продавец. Его рынок сжимался на 25 % в год.» | ✅ «Рынок, который пять лет теряет по 15 % в год, сжался больше чем вдвое (0,85⁵ ≈ 0,44).» |



## B-02. Boundary: hiring the first salesperson

### Request

> We're a six-person landscaping company doing about $1.4M a year. I do all the selling myself and I'm the bottleneck. How do I hire my first salesperson, and what should I pay them — base, commission, or both? What's a normal split?

### Output with the skill

Hormozi's method stops at hiring and pay. It has no rule on base versus commission and no "normal split", so I won't give you a number under his name. How to find, choose and pay a salesperson is outside the method. The closest it gets is 01.13: sales salaries and commissions are part of what it costs you to acquire a customer (Lost Chapters, 2025). So whatever pay plan you pick, add it into CAC and check that lifetime gross profit per customer stays above 3x CAC (01.11, $100M Leads, 2023). The author's own caveat on 3:1 is that it's "a pattern I personally observed, not a rule".

**Diagnosis.** Two levels are in play, and a number you didn't give decides between them. The higher level is price. The method picks the lever that doubles a business by profit, and price comes before more customers (01.28). If you consistently close more than 50% of what you quote and you want to make more money, 01.29 says your price is too low (Pricing playbook, 2025). In that case the first move is a price rise, tried on new customers first (13.14), not a hire. The level you named sits below that one. Every sale runs through you, so at about $1.4M a year the business makes money only when you're in it, which 15.1 calls a high-paying job rather than an asset (Lost Chapters, 2025). The way out is the four steps of 15.4, in this order: a self-inventory, trading doing for managing, removing yourself from marketing, then 90 days off (video, 2025). In that order the salesperson is one slot in the inventory, not the first move.

**Steps**

1. **Inventory your selling before you hire (15.5, 15.6).** For one week, keep a spreadsheet with a row for every 15 minutes and one word per slot (video, 2025). Then list every selling task you do, in as much detail as you can, and put a project, process or person against each one. Hand off the greens first: tasks you can teach someone now, and some can go to a person on your team of six who has spare time. Yellows come next, which are tasks that need a process you know how to build. A salesperson you don't have yet is a red, and reds are solved last.
2. **Write the selling down so someone else can run it (09.2, 09.20, 15.7).** Write a script your hire delivers word for word. Write out your labels, solutions, assurances and benefits in advance, so nothing gets invented during a sale. Add if-this-then-that rules for situations that keep coming up, and a money box: the amount they can decide alone, plus a cap on the total. Price is not in that box. When a customer says "too expensive", the answer is a payment plan, never a discount (16.11, Money Models, 2025). One caveat on 09.2: ACQ's scripts are tuned for a brand prospects already know, so build your script from your own sales conversations, not from ACQ's wording.
3. **Set a scorecard and a pass/fail test before they sell alone (15.8).** Answer "How do you and your role make the company money?" for the job, and set its KPIs from that answer. Let the hire sell on their own only when a test shows they get 100% of the result at 80% of your skill (video, 2025). The author's caveat: at the start he accepts 80%, sometimes 60%, as long as the person has a clear path to getting better.

**What I couldn't check**

- [to clarify: your close rate on quotes, and whether it holds steady]. It decides whether the price rise comes before the hire (01.29).
- [to clarify: lifetime gross profit per customer and what it costs you now to get one]. You need both numbers to test any pay plan against 3:1 (01.11, 01.13).
- [to clarify: whether anyone on your current team has spare hours]. That decides how many selling tasks are greens you can hand off right away (15.6).

### Baseline output

Short answer: pay both. The base keeps them doing the dull parts of the job, like site walks, follow-ups and updating the CRM, and it lets a good person afford to join you. The commission keeps them selling. For a first salesperson at a company your size, it's normal for most of the pay to be base. Pay the commission on money you've collected, and tie it to margin if you can.

The pay plan is the easy part, though. When a first sales hire fails at an owner-led trades company, it's usually not because of the pay. Here's the order I'd do things in.

##### 1. Before you hire: three checks

**Can you hand over the pricing?** If your estimates live in your head ("that feels like a $38k patio"), a new person will do one of two things. Either they underbid and eat your margin, or they bring every estimate back to you, and you're still the bottleneck. Write down your production rates, labor hours per unit, material markups, minimum job size and target gross margin. A spreadsheet or estimating software (LMN, Aspire, SynkedUP and similar) is enough. Nothing matters more for making a salesperson possible.

**Do you know your sales numbers?** Track leads per month, how many you visit, your close rate, your average job size and the time from first call to signed contract. You need these numbers to set a quota and to tell within 90 days whether the hire is working.

**Can the crews take on more work?** With six people, another $400–600k of sold work means another crew. If operations is already full, a salesperson just builds a backlog and angers clients. Plan the crew hire at the same time.

Also check that you have enough leads. A salesperson turns existing demand into jobs, and in their first year they rarely create much new demand. If you're turning leads away or slow-walking them today, you have enough.

##### 2. Figure out what you're actually hiring

"Selling" in landscaping is usually five jobs:

1. Answering and qualifying inquiries
2. Site visits
3. Design and estimating
4. Follow-up
5. Closing

Track your time for two weeks. Owners often find that half of it goes to the first and fourth jobs. An office coordinator at $20–25/hr can take those off your plate for much less than a salesperson costs. If that frees enough of your time, the coordinator is your first hire and the salesperson comes later.

If you do need someone who closes, you have two options:

- **A sales estimator or project manager from the industry.** That could be a former foreman, a competitor's estimator, or a nursery or supplier rep: someone who can walk a property, measure it and price it. They're easier to trust with numbers, though you may need to coach their selling.
- **A pure salesperson from outside the industry.** They'll be better at closing. But you'll need a very tight pricing system, and you'll be reviewing their estimates for a long time.

At your size, the first option usually works better. Someone who knows what a 600 sq ft paver patio costs to build won't sell you into a loss.

##### 3. Finding and vetting candidates

- **Write a one-page scorecard.** Cover what they'll sell (design/build, enhancements or maintenance contracts), the results you expect by months 3, 6 and 12, and your non-negotiables.
- **Know where to look.** Try suppliers, nurseries and stone yards (ask the reps who's good), competitors' estimators, your own best crew lead, industry job boards (NALP, your state landscape association) and local postings.
- **Ask for their numbers:** what they sold last year, their average job size and their close rate. Good salespeople know them.
- **Make them do the job.** Give them a real property. Have them walk it, write an estimate and present it to you as if you were the homeowner. This tells you more than any interview.
- **Check references,** specifically on follow-through and on honesty with customers.

##### 4. Handing over the work

Don't hand over everything on day one. A typical path over the first 60–90 days:

1. They ride along on your appointments.
2. You ride along on theirs.
3. They handle smaller jobs alone (say, under $15k), and you review estimates before they go out.
4. You raise that limit as their numbers hold up.

Keep your biggest and most complex clients yourself for now.

##### 5. Pay: base, commission, or both

**Both.** Neither extreme works for you:

- **Commission only** attracts people who can't get a base elsewhere. They chase big jobs, skip small ones and neglect the admin. It also fits badly when you're the one supplying the leads. They aren't prospecting; they're converting demand you created.
- **Salary only** gives them no reason to push for the close or hold the price.

**The typical split** for trades sales roles runs from about 60/40 to 80/20, base to variable, at target pay. The more the role involves estimating and managing projects, the more of the pay is base. The more it's about hunting new clients, the more is commission.

**Typical numbers** in residential landscaping (these vary a lot by region, so check local job postings):

- **Base:** roughly $45k–65k.
- **Commission:** usually 2–5% of sold revenue on design/build and enhancements, or 8–15% of gross profit if you pay on margin. For maintenance contracts, it's often 5–10% of first-year contract value, with a smaller rate or nothing on renewals.
- **Total target pay:** often $75k–110k for a solid performer.
- **Output:** once ramped up, a productive design/build salesperson usually sells somewhere around $700k–1.5M a year. Total sales pay usually comes to about 6–10% of what they sell.

**Worked example:** a $55k base plus 3% of collected revenue. If they sell $900k in year one, they earn $55k + $27k = $82k, about 9% of what they sold. At a 40% gross margin, that $900k brings in $360k of gross profit, so the salesperson costs you about 23% of the gross profit they generate. Run this math against your own margins before you offer anyone a number.

**Guardrails that matter more than the percentage:**

- **Pay on collected money, not signed contracts.** Pay commission when the customer pays or when the job is complete, and include a clawback for cancellations.
- **Tie commission to margin.** Either pay on gross profit, or pay the full rate only when a job sells at or above your target margin, with a lower rate if they discount. Otherwise you're paying them to sell cheap.
- **Decide on house accounts before they start.** Say whether your existing clients and repeat customers earn full, reduced or no commission. Put it in writing now, not after the first argument.
- **Plan for the ramp-up.** Building a pipeline takes 3–6 months, and in landscaping sometimes a whole season. Cover it with a higher guaranteed amount for the first few months or with a recoverable draw against commission.
- **Allow for the seasons.** If most of your sales happen from January to May, think about paying commission monthly but settling up quarterly, so they stay motivated through the season.
- **Keep it simple.** They should be able to work out their own paycheck. Use one or two rates, not a matrix.
- **Put the whole plan in writing,** and note that you can revise it each year.

##### 6. Expectations

Set a quota. Selling roughly 10–15× their total pay is a reasonable target, and it matches the 6–10% cost of sales above. Review close rate, average job size and margin every month. If they're not on track by month 4–6, even though you've given them leads and support, act on it instead of waiting out the season.

Two things would change the details here: the mix of work you sell (design/build, maintenance or enhancements) and your gross margins. Share those and I can sketch a concrete pay plan with real numbers.

### Grader verdicts

| # | assertion | with skill | baseline |
|---|---|---|---|

| 1 | The answer says that hiring as a topic — how to hire, what to pay, the base-versus-commission split — is outside the method the skill carries, and presents no compensation figures or hiring process as the method's rules. | ✅ «How to find, choose and pay a salesperson is outside the method.» | ❌ «Short answer: pay both.» |

| 2 | Any advice given beyond that boundary is marked as general advice, not the method's; nothing outside the boundary carries a rule number of the form `NN.M`. | ✅ «It has no rule on base versus commission and no "normal split", so I won't give you a number under his name.» | ❌ «**The typical split** for trades sales roles runs from about 60/40 to 80/20, base to variable, at target pay.» |

| 3 | If the answer points at what the method does cover — the owner's self-inventory, documenting the sales process (document, demonstrate, duplicate), a word-for-word script — it cites those rules as `NN.M` (15.4, 15.5, 15.13, 09.2 or others of sheets 15 and 09). | ✅ «**Inventory your selling before you hire (15.5, 15.6).**» | ❌ «Track your time for two weeks. Owners often find that half of it goes to the first and fourth jobs. ... They ride along on your appointments. ... You ride along on theirs.» |

| 4 | The answer attributes no figures to the company that the request does not give (no close rate, ticket size, margin or pay benchmark stated as fact). | ✅ «[to clarify: your close rate on quotes, and whether it holds steady]. It decides whether the price rise comes before the hire (01.29).» | ❌ «With six people, another $400–600k of sold work means another crew. ... **Base:** roughly $45k–65k.» |



## B-03. Sound material: a postnatal fitness challenge offer with no embedded violation

### Request

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

### Output with the skill

##### Findings

1. 🟡 **The biggest obstacle is promised away but never solved.** "without leaving the baby for hours", yet the guarantee requires "attend 10 of the 12 sessions". For a mom of a 3–18-month-old, "what if I can't get there" is *the* obstacle. The page doesn't say how long a session is, whether the baby can come, or what happens when the baby is sick on a Tuesday. 02.18: the offer has to resolve every obstacle the buyer believes she'll have. 02.8: the bottom of the equation, effort & sacrifice, gets the harder work. And by the caveat of 02.7, a driver only counts once the prospect perceives it, so an answer you have but don't print doesn't count. **Change:** answer those three questions on the page, right under the avatar line. [to clarify: session length; are babies allowed in the studio; is there a make-up session for a missed one]. If there's no make-up option today, 02.18 argues for building one rather than leaving the objection standing.

2. 🟢 **The copy names the outcome, not what she feels.** "who want their core strength back". The only symptom on the page, "doming", appears once, inside the guarantee. 02.3: the prospect has to feel understood, which means saying her pain back to her first, then the outcome, then how you get her there. **Change:** open with the problem in the words your postnatal clients actually use [to clarify: what they say bothers them]. If they don't say "doming", explain it in their words. The guarantee is measured on it, and a result she can't picture doesn't raise her perceived likelihood of achievement (02.7).

3. 🟡 **"What you get" lists delivery vehicles, not problems solved, and puts no value on them.** "12 small-group sessions (max 6 per group), a 10-minute at-home daily routine on video, a weekly 15-minute check-in with your coach". The only price tag on the page is the $97 bonus, set against $597. 02.21: write each part as problem → solution wording → a named bundle, with the vehicle listed underneath. 03.14: pull the most distinct pieces out of the core and present them one at a time (the daily video routine and the weekly check-in could almost stand on their own). 03.11: give each a name with a benefit in it and a justified price tag, so the stack together is worth more than the price. [to clarify: what you would honestly charge for each part on its own; never more than it's worth, 16.9.]

4. 🟡 **The price line hands her a calculator for the comparison you're trying to escape.** "Local studios charge $25–40 per class; this is not a class, it's a program with a measured result." She'll do the math: 12 sessions × $25–40 = $300–$480, against $597. That's $597 ÷ 12 = $49.75 a session, about 1.2–2x the class price you quote yourself. It reads as "classes, a bit dearer", the opposite of 02.24 (the choice should be between you and nothing, not between you and the studio down the street) and of 02.28 (a premium works when it sits so far above the market that something entirely different must be going on, never slightly above it). **Change:** cut the first half and keep "this is not a class, it's a program with a measured result". The valued stack from finding 3 then serves as the anchor. Don't raise the price for this cohort: 02.29 raises the price only after value has risen enough that the buyer still gets a deal.

5. 🟡 **The scarcity numbers contradict each other.** "max 6 per group" · "we're opening the Tuesday/Thursday 10:00 group" · "Spots: 12 per cohort, 9 taken as of today". A reader can't tell whether the Tue/Thu 10:00 group has 6 spots or 12, how many are left in it, or when the other group trains. 03.4, honest scarcity: define one number, advertise it, and tell prospects how close you are to it. **Change:** give one number per group, the spots left in each, and the time of each. [to clarify: how many groups per cohort, and at what times.] Also, "as of today" on a landing page means whatever day she reads it, so update the count each time a spot goes.

**What already passes:**
- **Name:** it carries Avatar, Goal, Interval and Container (03.23). This holds if "Riverside" is the neighbourhood rather than a whole city, since the rule asks for the hyper-local area.
- **Avatar:** it is niched to one stage of one group (02.6).
- **Guarantee:** it fills all three slots: the result, the time period and what you'll do (03.15). It makes the key actions its conditions and pays out more than a refund (03.19). That is the right type for a service with a real cost of fulfilment (03.17).
- **Reason why:** it is stated (03.28), and it has to be true.
- **Deadline:** it sits on the bonus, not on the service (03.9).
- **Cohort:** it has a start date and a close date (03.7).

##### What I couldn't check

- [to clarify: what it costs you to get one mom enrolled, and your gross profit on $597 after coach time.] The method's test is that a customer pays back what it cost to get and serve her within thirty days (01.18, $100M Leads 2023), and the author's real-life minimum is 2x that (01.19, Lost Chapters 2025). The same figures size the guarantee. Its payout is $597 plus a free seat in a capped cohort, and by the caveat of 03.19 an outsized payout suits high-margin products only.
- [to clarify: what a mom who finishes the six weeks buys next.] The page doesn't need to show it, but 16.10 ($100M Money Models 2025) warns against a single offer with nothing after it: the profit is made on the second, third and fourth offers.
- [to clarify: what share of the moms who hear this offer buy.] If you consistently close more than 50% and want to make more money, 01.29 (Pricing playbook 2025) says the price is too low. The author's condition has both halves. "9 taken" shows demand, not a close rate. That's the test for the next cohort's price, not this one.

##### Verdict

The offer works. The parts that usually fail are built right: a guarantee with teeth, a reason why and a real deadline. Where it leaks is how it's presented. It doesn't answer the one obstacle every mom of a baby has, it sells a list of vehicles, and then it invites a per-class comparison it can't win. First, make the spot numbers consistent (finding 5), because contradictory facts on a sales page cost trust. Next, answer the questions about the baby and missed sessions (finding 1). Then rebuild "What you get" as a named, valued stack and drop the per-class line (findings 3 and 4). Keep the price and the guarantee as they are for the October 6 cohort.

### Baseline output

**Short verdict:** the offer has a solid core. It names a specific audience, has a measurable result, a real guarantee with sensible conditions, an honest reason for the deal and a real deadline. Most local studios never get that far. The problems are in how it's put together. It sells the studio's test instead of the result the mom wants. The price comparison works against you. The guarantee gives away too much in one place and is too vague in another. The numbers contradict each other. And the biggest objection, what to do with the baby, gets no answer.

Here are my changes, most important first.

##### 1. Lead with what she wants, not the plank

"Core strength back" is vague, and "a 60-second plank without doming" is how *you* measure progress. It isn't what a new mom lies awake wanting. She wants to lift the car seat without her back hurting, to have a firmer belly that doesn't bulge down the middle, to trust her body again, and maybe to run again. Put those outcomes first. Then bring in the plank as proof: "and here's how we measure it."

Keep your claims to what you can actually deliver and measure. Don't promise to "fix diastasis" or anything pelvic-floor related unless a qualified professional is involved.

Also, many moms don't know the word "doming." Explain it in half a sentence: the ridge that pops up along the middle of your belly when your deep core isn't holding yet.

##### 2. Answer "What do I do with the baby?"

You promise "without leaving the baby for hours," but the offer never says how. That's the first question every reader will have. Answer it plainly:

- Can babies come into the room? If so, say it in the headline. That alone sets you apart from nearly every studio.
- How long is a session, and where is the studio? "50 minutes, 10 minutes from anywhere in Riverside" is what backs up the "not for hours" claim.
- Say the daily video routine is built to fit into nap time or to do with the baby on the mat next to her.

##### 3. Drop the per-class comparison

"Local studios charge $25–40 per class" invites the reader to do the math: 12 × $40 = $480 at most, and you charge $597, about $50 a session. Then you just assert "this is not a class." You've set the anchor, and it works against you.

Instead:
- **Compare against the right alternative:** private postnatal Pilates or one-on-one postnatal sessions. Use the real local price. "Less than [N] private sessions" is a comparison you win.
- **Show why it's a program:** list what's included (a baseline assessment, 12 coached sessions, six 1:1 check-ins, the daily routine, a filmed before-and-after test). Only put a dollar value next to something you actually sell at that price.
- **Add a payment option,** such as 2 × $299. Many of these moms are on reduced income during parental leave.

I wouldn't lower the price. $597 for this much coaching is reasonable. The framing is what hurts it.

##### 4. Tighten the guarantee

Its structure is good: the conditions are the same things that produce the result. Four problems:

- **Refund *and* a free next round is too much.** If three moms miss the target, you pay back $1,791 and lose three seats in the next cohort. Let her choose one: her money back, or the next round free.
- **Nobody knows where they're starting from.** A mom at 3 months with a wide separation may not reach a clean 60-second plank in 6 weeks no matter what she does. Test everyone at the first session and film it. If someone clearly can't reach the target, tell her at intake. Adjust her goal or refer her to a pelvic floor physio. Don't take money on a guarantee you already expect to pay out.
- **You grade your own refund.** Who decides whether it's "doming"? Film the week 1 and week 6 tests and watch them together. That makes the guarantee credible. It also gives you before-and-after material, which is exactly what "moms who'll talk about it" need to share.
- **"10 of 12 sessions" is tight for a mom with an infant.** One sick baby plus one bad night and she's out. Offer make-up sessions in another slot, or she'll read the guarantee as a trap. Also say how she logs the daily routine: a checklist, a text to the coach, whatever you'll actually check.

##### 5. Fix the numbers, because readers will notice

- "Max 6 per group" but "12 spots per cohort," and the reason for the deal mentions one new group (Tue/Thu 10:00). Is it one group or two? If two, name both time slots and show spots left in each.
- "9 taken as of today" has no date on a landing page. Either update it honestly ("updated Sept 25") or remove it. A stale scarcity number does more damage than having none.
- "Next cohort starts October 6" makes it sound like there's a current one. Write "Starts Tuesday, October 6. Enrollment closes Saturday, October 3." The weekdays check out, and they make the dates feel concrete.

##### 6. Add proof and safety

Right now nothing tells a reader why *you* can deliver this. Add:
- The coach's name, postnatal training or certification, and how many moms she has coached.
- Any past results, even informal ones ("7 of 9 moms in our pilot passed the plank test"). If this is the first cohort, call it the founding group.
- A safety line: cleared for exercise by her doctor or midwife, C-section moms welcome, and a screening at intake. This builds trust and protects you.

##### 7. Check the bonus

- "Sold separately at $97": only keep that line if it's actually for sale at $97. Otherwise it's a made-up anchor, and people can tell.
- Back-to-Running only appeals to moms who run. A bonus that removes an objection would reach more of them, for example a guide to lifting and carrying (car seat, stroller, baby carrier) without straining your back. Keep the running plan as a second bonus if you like.

##### 8. Smaller points

- **"Challenge"** suggests intensity and pushing through, which is exactly what a mom worried about her abdominal separation fears. "Program" or just "6-Week Core Rebuild" feels safer and fits the price better.
- **Reframe the reason for the deal** so it's a two-way deal: "We're opening a new group and want it to be a founding group of moms who'll tell their friends. The bonus is our side of the deal. In return we'll ask for honest feedback and, if you're happy, a short review." Same honesty, but now she knows her part.
- **Add a clear next step:** a button to book an intake call or save a spot.
- **Plan what comes after week 6** (a continuation group or membership for graduates). It doesn't need to be on this page, but have it ready before October 6.

##### Revised draft

Placeholders are in [brackets]. Only keep "baby welcome" if it's true.

```
Riverside Postnatal Core Rebuild — 6 weeks, small group, baby welcome

Get your core back in 6 weeks: lift the car seat without back pain, feel your
belly firm up again, and get ready to [run / train] again — in 50-minute
sessions 10 minutes from home, with your baby [in the room].

For Riverside moms 3–18 months postpartum (vaginal or C-section birth),
cleared for exercise by your doctor or midwife.

How we measure it: at your first session we film a plank test and check your
midline. In week 6 we film it again. The target: a 60-second plank without
doming, the ridge along the middle of your belly that shows your deep core
isn't holding yet.

What you get
- Intake assessment: midline check and a filmed baseline test
- 12 coached sessions, Tue & Thu 10:00, max 6 moms per group
- A 15-minute 1:1 check-in with your coach every week
- A 10-minute daily routine on video, built for nap time
- Bonus this round: [Lift & Carry guide] + Back-to-Running plan [normally $97]

Your coach: [Name], [postnatal certification], [N] moms coached since [year].

Price: $597, or 2 payments of $299.
[Less than N private postnatal sessions in Riverside.]

Guarantee: come to 10 of the 12 sessions (missed one for a sick baby? make it
up on [day/time]) and do the daily routine 5 days a week ([how you log it]).
If you can't hold a 60-second plank without doming in week 6, you choose:
your $597 back, or the next 6-week round free.

Why the bonus: we're opening a new Tue/Thu 10:00 group and want it to be a
founding group of moms who'll tell their friends. The bonus is our side of the
deal; in return we'll ask for honest feedback and, if you're happy, a short
review.

[3] of 6 spots left (updated [Sept 25]). Starts Tuesday, October 6.
Enrollment closes Saturday, October 3.

[Book your intake call]
```

Before you publish, check three things: the baby policy, whether it's one group or two, and whether the $97 price is real. Those three matter most for trust.

### Grader verdicts

| # | assertion | with skill | baseline |
|---|---|---|---|

| 1 | No finding is marked 🔴. | ✅ «1. 🟡 **The biggest obstacle is promised away but never solved.** ... 2. 🟢 **The copy names the outcome, not what she feels.** ... 5. 🟡 **The scarcity numbers contradict each other.**» | ✅ «Here are my changes, most important first.» |

| 2 | The verdict says the material does its job (works, is sound, is ready) and names what to do first, if anything. | ✅ «The offer works. ... First, make the spot numbers consistent (finding 5), because contradictory facts on a sales page cost trust.» | ❌ «The problems are in how it's put together. It sells the studio's test instead of the result the mom wants. The price comparison works against you.» |

| 3 | Every finding present has a verbatim quote from the material and a rule cited as `NN.M`; there are at most seven findings; the answer names at least one rule the material satisfies (for example 03.19, 03.4, 03.23, 03.28 or by the construct's name). | ✅ «"Local studios charge $25–40 per class; this is not a class, it's a program with a measured result." ... the opposite of 02.24 ... **Name:** it carries Avatar, Goal, Interval and Container (03.23).» | ❌ «## 8. Smaller points» |

| 4 | No finding claims the material lacks something it contains (a guarantee, a deadline, a reason why, a bonus, scarcity). | ✅ «The parts that usually fail are built right: a guarantee with teeth, a reason why and a real deadline.» | ✅ «It names a specific audience, has a measurable result, a real guarantee with sensible conditions, an honest reason for the deal and a real deadline.» |

| 5 | The answer does not mark the price ($597) as too high and does not recommend a discount. | ✅ «Don't raise the price for this cohort ... Keep the price and the guarantee as they are for the October 6 cohort.» | ✅ «I wouldn't lower the price. $597 for this much coaching is reasonable. The framing is what hurts it.» |



## B-04. When not to apply: freemium for a video-editing service with salaried editors

### Request

> У нас студия монтажа видео для блогеров: 6 монтажёров на зарплате, подписка 30 000 ₽ в месяц за 8 роликов. Сейчас клиент обходится нам в 9 000 ₽ рекламы, маржа на услуге 45 %. Хотим запустить freemium: первый ролик до 3 минут монтируем бесплатно всем, кто зарегистрируется на сайте, а дальше предлагаем подписку. Как правильно построить freemium, чтобы он окупался?

### Output with the skill

**Freemium в том виде, в каком его описывает метод, вашей студии не подходит.** Хормози называет freemium стратегией привлечения, а не бизнес-моделью. Он допускает его только в бизнесе с инкрементальной маржой около 100 %, то есть в софте или медиа (16.3, 10.30; Lost Chapters, 2025). Монтаж — услуга: каждый ролик занимает часы монтажёров. Ближе всего к вашей идее то, что метод называет бесплатным front end, или Attraction Offer (листы 03 и 10). Дальше разбор по ним.

**Диагноз.** Бесплатный ролик нарушает два из трёх условий freemium, а выполняться должны все три сразу (10.31). Первое условие — выдача почти ничего не стоит. Здесь это не так: при марже 45 % себестоимость подписки 30 000 − 13 500 = 16 500 ₽, в среднем 16 500 ÷ 8 = 2 062,5 ₽ на ролик. Второе — ценность постоянная, а один ролик даёт её один раз. Третье выполняется: у клиента остаётся причина покупать дальше, подписка на 8 роликов. Значит, это бесплатный вход в воронку, и судить его надо по тесту 30 дней. Сейчас валовая прибыль первого месяца 30 000 × 45 % = 13 500 ₽, CAC 9 000 ₽, отношение 1,5x. Это выше минимума, при котором клиент окупается за 30 дней (01.18, $100M Leads, 2023; 01.21, $100M Money Models, 2025), но ниже рабочего стандарта 2x (01.19, Lost Chapters, 2025). Стоимость бесплатного ролика ложится на CAC каждого, кто купил подписку: CAC = (реклама на одну регистрацию + 2 062,5 ₽) ÷ доля зарегистрированных, купивших подписку. При 2x CAC не должен превышать 13 500 ÷ 2 = 6 750 ₽, а это меньше нынешних 9 000 ₽. Даже если реклама на регистрацию ничего не стоит, подписку должны купить не меньше 2 062,5 ÷ 6 750 ≈ 30,6 % зарегистрированных. Чтобы просто окупиться за 30 дней, нужно 2 062,5 ÷ 13 500 ≈ 15,3 %.

**Что сделать**

1. Постройте бесплатный ролик как Attraction Offer, который за один ход и привлекает, и продаёт (10.2). При регистрации показывайте бесплатный ролик до 3 минут рядом с подпиской на 8 роликов за 30 000 ₽ и делайте акцент на подписке (Decoy Offer, 10.20). Второй раз предлагайте подписку, когда сдаёте бесплатный ролик: блогер видит результат и понимает, что ему нужен следующий (10.1).
2. Включите себестоимость бесплатного ролика в CAC и держите вход на тесте 30 дней: (реклама на одну регистрацию + себестоимость ролика) ÷ доля купивших подписку ≤ 6 750 ₽ (01.13, 01.19). Если при реальной конверсии выходит больше, берите за первый ролик деньги, а не делайте его бесплатным. Метод убирает дорогое время исполнителя из бесплатного шага, а здесь это время монтажёра (Two-Step Sale, 03.33).
3. Ограничьте число бесплатных роликов свободной мощностью шести монтажёров. Объявите, сколько бесплатных роликов берёте в неделю и сколько мест осталось (Honest Scarcity, 03.4). Если регистраций больше, чем успеваете смонтировать, добавьте трение, например квалифицирующие вопросы при регистрации. Настраивайте его по числу квалифицированных заявок, а не по их доле (Free Money Math, 03.29).

**Что не удалось проверить**

- [уточнить: сколько вам стоит бесплатный ролик до 3 минут] — я взял среднюю себестоимость ролика из подписки, 2 062,5 ₽. Короткий ролик может стоить иначе, и от этой цифры зависят пороги 30,6 % и 15,3 %.
- [уточнить: сколько роликов в месяц шесть монтажёров делают сейчас и сколько могут сделать] — от этого зависит лимит из шага 3 и то, придётся ли нанимать людей под бесплатные ролики.
- [уточнить: что входит в 9 000 ₽] — по методу CAC включает не только рекламу, но и зарплату продаж, креатив и софт (01.13). Если такие расходы есть, реальное отношение ниже 1,5x.
- [уточнить: средний CAC в вашей нише] — от него зависит, где главный рычаг (01.14). Если ваши 9 000 ₽ не больше трёх средних по нише, с рекламой всё в порядке. Тогда работать нужно над моделью денег: добавить допродажу в первые 30 дней, чтобы валовая прибыль первого месяца заметно превысила CAC (10.35, шаг 2). Если больше трёх средних, работать нужно над рекламой (листы 04–07).
- [уточнить: месячный отток подписчиков] — LTGP = 13 500 ₽ ÷ отток (10.4). Его сравнивают с CAC по порогу 3:1 (01.11, $100M Leads, 2023). Автор сам оговаривает: «a pattern I personally observed, not a rule».
- [уточнить: подписку оплачивают в начале месяца?] — если нет, 13 500 ₽ приходят не в первые 30 дней, и тест 01.18 надо пересчитать.

### Baseline output

**Короткий ответ:** freemium «всем, кто зарегистрировался» скорее всего не окупится. Окупится freemium для отобранных блогеров, которым действительно нужны 8 роликов в месяц, при жёстком лимите бесплатных слотов и продаже в момент сдачи ролика. Ниже расчёт и схема.

##### 1. Ваша стартовая точка

- Валовая прибыль с клиента: 30 000 × 45 % = **13 500 ₽ в месяц**.
- 9 000 ₽ рекламы на клиента окупаются за 0,67 месяца, то есть уже в первый месяц.
- Себестоимость одного ролика: 30 000 × 55 % / 8 ≈ **2 060 ₽**.

Экономика у вас хорошая. Значит, freemium нужен не для того, чтобы спасать привлечение, а для одной из двух целей: получить больше клиентов, когда реклама перестаёт масштабироваться, или загрузить монтажёров, которые простаивают. Если нет ни того, ни другого, проще поднять рекламный бюджет: при окупаемости меньше месяца вы можете платить за клиента больше 9 000 ₽.

##### 2. Формула окупаемости

**Стоимость клиента через freemium = (A / k + V) / c**

- A — реклама на одну регистрацию;
- k — доля зарегистрированных, которые реально прислали исходники;
- V — себестоимость бесплатного ролика;
- c — доля получивших бесплатный ролик, которые купили подписку.

Пример на допущениях (подставьте свои цифры): A = 500 ₽, k = 50 %, V = 2 000 ₽. Тогда один сданный бесплатный ролик обходится в 1 000 + 2 000 = 3 000 ₽.

| Конверсия в подписку (c) | Стоимость клиента |
|---|---|
| 10 % | 30 000 ₽ |
| 20 % | 15 000 ₽ |
| 30 % | 10 000 ₽ |
| 35 % | ≈ 8 600 ₽ |

Чтобы freemium обходился не дороже нынешних 9 000 ₽, подписку должна купить треть получивших ролик. Чтобы клиент окупался за первый месяц (13 500 ₽), нужно 22 %. При раздаче «всем зарегистрированным» такая конверсия маловероятна: придёт много людей, которым нужен один бесплатный ролик и которые не могут платить 30 000 ₽ в месяц.

Сколько вы можете позволить себе платить за клиента, зависит от удержания. Посчитайте, сколько месяцев в среднем платит клиент. Если это 5 месяцев, валовая прибыль с него 67 500 ₽. При соотношении 3 к 1 допустимая стоимость клиента тогда до ~22 000 ₽, и даже вариант с конверсией 20 % проходит.

##### 3. Монтажёры на зарплате: бесплатный ролик ничего не стоит, только если они простаивают

От этого зависит, сработает ли вся схема.

- **Если у команды есть недогруз**, бесплатный ролик не стоит вам денег: V выпадает из формулы. В примере клиент тогда стоит 1 000 / c, то есть 5 000 ₽ при конверсии 20 %. Freemium превращает простой в клиентов, и это лучший сценарий.
- **Если недогруза нет**, каждый бесплатный ролик либо задерживает ролики платящих клиентов (а отток обойдётся дороже любой рекламы), либо требует найма. Тогда V считайте полностью.

Отсюда правило: **бесплатных роликов в неделю не больше, чем позволяет свободная мощность команды.** Посчитайте, сколько роликов 6 монтажёров делают при полной загрузке и сколько делают сейчас. Разница и есть ваш бюджет на freemium. Кто не попал в лимит, встаёт в очередь, и лист ожидания заодно создаёт дефицит.

##### 4. Как построить воронку

1. **Отбор вместо простой регистрации.** Подписка — это 8 роликов в месяц. Она нужна блогеру, который выпускает хотя бы 2 ролика в неделю и зарабатывает на канале достаточно, чтобы платить 30 000 ₽. Поэтому вместо «зарегистрируйтесь» сделайте короткую заявку: ссылка на канал, сколько роликов выходит в месяц, кто монтирует сейчас и за сколько. Бесплатный ролик даётся один на канал, а не на аккаунт. Регистрация подорожает (A вырастет), но конверсия вырастет сильнее.
2. **Бесплатный ролик должен быть образцом платного продукта.** Это настоящий ролик клиента, который он опубликует, в том формате, который вы продаёте. Лимит в 3 минуты подходит, если вы в основном монтируете короткие ролики. Если ваш основной продукт — 15-минутные видео для YouTube, трёхминутный ролик покажет не тот продукт. Тогда лучше ограничить объём работы: часы монтажа или объём исходников.
3. **Ограничьте себестоимость.** Один раунд правок, фиксированный срок, стандартный бриф. Замерьте часы на первых 20 бесплатных роликах: это и будет ваш реальный V.
4. **Продавайте в момент сдачи.** Не отправляйте ролик письмом со словами «вот, пользуйтесь». Проведите созвон: что сделали, чем ролик лучше их прошлых, какие ролики запланировать на следующий месяц. Дайте предложение со сроком: при оформлении подписки в течение 7 дней клиент получает бонус. Бонус лучше давать продуктом, а не скидкой: лишний ролик в первом месяце стоит вам около 2 000 ₽ себестоимости, а скидка 5 000 ₽ забирает 5 000 ₽ прибыли.
5. **Платящие клиенты всегда в приоритете.** Бесплатные ролики делаются только в свободные окна и со сроком длиннее, чем у подписчиков.

##### 5. Пилот и стоп-правило

Запустите пилот на 30–50 бесплатных роликов с отдельной рекламной кампанией и считайте A, k, V и c по факту. Через 2–3 месяца сравните удержание клиентов из freemium с обычными: пришедшие за бесплатным иногда уходят быстрее, и тогда допустимая стоимость такого клиента ниже.

Если по итогам пилота клиент обходится дороже, чем вы готовы платить, сначала ужесточите отбор. Не помогло — замените бесплатный ролик платным входом:

- **пробный пакет**: первые 2 ролика за 5 000 ₽ с зачётом в подписку, это примерно ваша себестоимость;
- **гарантия**: не понравился первый ролик — возвращаете оплату за месяц целиком. Вы рискуете той же себестоимостью одного ролика, но только на тех, кто уже был готов платить.

Оба варианта снимают тот же страх клиента («а вдруг смонтируют плохо») и отсекают тех, кто пришёл только за бесплатным.

### Grader verdicts

| # | assertion | with skill | baseline |
|---|---|---|---|

| 1 | The answer says that freemium is for software or media with incremental margins near 100 % and not for a service delivered by salaried staff, citing 16.3, 10.30 or the rule in words, before or instead of building the freemium. | ✅ «Он допускает его только в бизнесе с инкрементальной маржой около 100 %, то есть в софте или медиа (16.3, 10.30; Lost Chapters, 2025). Монтаж — услуга: каждый ролик занимает часы монтажёров.» | ❌ «**Короткий ответ:** freemium «всем, кто зарегистрировался» скорее всего не окупится. Окупится freemium для отобранных блогеров, которым действительно нужны 8 роликов в месяц, при жёстком лимите бесплатных слотов и продаже в момент сдачи ролика.» |

| 2 | The answer names the alternative the method offers this business — a free or discount wrapper on the front end, or another attraction offer — citing 03.26, 03.27, 03.29, 10.22 or another rule of sheets 03 or 10 as `NN.M`. | ✅ «Ближе всего к вашей идее то, что метод называет бесплатным front end, или Attraction Offer (листы 03 и 10). [...] Постройте бесплатный ролик как Attraction Offer, который за один ход и привлекает, и продаёт (10.2).» | ❌ «- **пробный пакет**: первые 2 ролика за 5 000 ₽ с зачётом в подписку, это примерно ваша себестоимость; - **гарантия**: не понравился первый ролик — возвращаете оплату за месяц целиком.» |

| 3 | No step of the answer builds the freemium as asked (a free edit for everyone who registers, then the subscription) under the method's name. | ❌ «Постройте бесплатный ролик как Attraction Offer, который за один ход и привлекает, и продаёт (10.2). При регистрации показывайте бесплатный ролик до 3 минут рядом с подпиской на 8 роликов за 30 000 ₽ и делайте акцент на подписке (Decoy Offer, 10.20). Второй раз предлагайте подписку, когда сдаёте бес» | ✅ «freemium «всем, кто зарегистрировался» скорее всего не окупится ... 1. **Отбор вместо простой регистрации.**» |

| 4 | The boundary is stated in the first paragraph of the answer, and the answer has at most three steps, each with a rule number of the form `NN.M`. | ✅ «**Freemium в том виде, в каком его описывает метод, вашей студии не подходит.** [...] 1. Постройте бесплатный ролик как Attraction Offer, который за один ход и привлекает, и продаёт (10.2). [...] 2. Включите себестоимость бесплатного ролика в CAC и держите вход на тесте 30 дней [...] (01.13, 01.19).» | ❌ «## 4. Как построить воронку ... 4. **Продавайте в момент сдачи.** ... 5. **Платящие клиенты всегда в приоритете.**» |

| 5 | The answer attributes no upgrade rate, conversion, servicing cost or other figure to the business that the request does not give (it gives 9 000 ₽ per customer, a 45 % margin, 30 000 ₽ a month, 8 videos, 6 editors). | ✅ «[уточнить: сколько вам стоит бесплатный ролик до 3 минут] — я взял среднюю себестоимость ролика из подписки, 2 062,5 ₽. Короткий ролик может стоить иначе, и от этой цифры зависят пороги 30,6 % и 15,3 %.» | ✅ «Пример на допущениях (подставьте свои цифры): A = 500 ₽, k = 50 %, V = 2 000 ₽.» |



## O-01. Off topic: a Python function that computes CAC crashes

### Request

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

### Output with the skill

Your CSV has no `spend` column. It's called `ad_spend`, so `row['spend']` raises `KeyError`. Change the key to `ad_spend`:

```python
import csv
from collections import defaultdict

def cac_by_channel(path):
    spend = defaultdict(float)
    customers = defaultdict(int)
    with open(path, newline='') as f:
        for row in csv.DictReader(f):
            spend[row['channel']] += float(row['ad_spend'])
            customers[row['channel']] += int(row['new_customers'])
    return {
        ch: spend[ch] / customers[ch] if customers[ch] else None
        for ch in spend
    }
```

I also made two small changes:

- **Division by zero.** Once the key is fixed, the next crash would be `ZeroDivisionError` on any channel that has spend but `new_customers` of 0. That channel now returns `None`, since its CAC is undefined. If you'd rather sort those channels to the bottom, use `float('inf')` instead.
- **`newline=''`.** The `csv` module docs recommend this when opening a file for `csv.reader`/`DictReader`. It keeps line endings inside quoted fields from being handled wrong.

Check with `channel,ad_spend,new_customers` / `meta,1000,10` / `meta,500,5` / `google,300,0`: the result is `{'meta': 100.0, 'google': None}`.

### Baseline output

The crash comes from the column name. `csv.DictReader` uses the header row as the keys for each row. Your header has `ad_spend`, not `spend`, so `row['spend']` fails on the first row. Your dict is also called `spend`, but that's unrelated. Only the key you look up in `row` matters.

Fixed version:

```python
import csv
from collections import defaultdict

def cac_by_channel(path):
    spend = defaultdict(float)
    customers = defaultdict(int)
    with open(path, newline='') as f:
        for row in csv.DictReader(f):
            spend[row['channel']] += float(row['ad_spend'])
            customers[row['channel']] += int(row['new_customers'])
    return {
        ch: spend[ch] / customers[ch] if customers[ch] else None
        for ch in spend
    }
```

Besides the key, I made two small changes:

- **Zero-customer guard.** With the KeyError fixed, the next crash would be a `ZeroDivisionError` on any channel that spent money but got no new customers. Those channels now return `None`, meaning CAC is undefined. If you'd rather flag them as infinitely expensive, use `float('inf')` instead.
- **`newline=''`** is how the `csv` docs say to open files. It keeps quoted fields that contain line breaks from being parsed wrong.

If you then get `KeyError: 'channel'` even though the header looks right, the file probably starts with a byte-order mark, which Excel exports often add. Open it with `open(path, newline='', encoding='utf-8-sig')` and the key will match.

### Grader verdicts

| # | assertion | with skill | baseline |
|---|---|---|---|

| 1 | The answer fixes the bug by reading the `ad_spend` column (it names the header mismatch) and gives corrected code. | ✅ «Your CSV has no `spend` column. It's called `ad_spend`, so `row['spend']` raises `KeyError`. Change the key to `ad_spend`:» | ✅ «Your header has `ad_spend`, not `spend`, so `row['spend']` fails on the first row. ... spend[row['channel']] += float(row['ad_spend'])» |

| 2 | The answer contains no rule number of the form `NN.M`, no method construct and no business advice about CAC thresholds, ratios or what to do with the ads. | ✅ «That channel now returns `None`, since its CAC is undefined.» | ✅ «Besides the key, I made two small changes: ... Those channels now return `None`, meaning CAC is undefined.» |

| 3 | The answer contains no diagnosis of the business and no findings with severity marks. | ✅ «I also made two small changes:» | ✅ «The crash comes from the column name. `csv.DictReader` uses the header row as the keys for each row.» |

| 4 | The answer does not ask for or invent business figures (an industry-average CAC, lifetime value, a ratio). | ✅ «Check with `channel,ad_spend,new_customers` / `meta,1000,10` / `meta,500,5` / `google,300,0`: the result is `{'meta': 100.0, 'google': None}`.» | ✅ «Those channels now return `None`, meaning CAC is undefined. If you'd rather flag them as infinitely expensive, use `float('inf')` instead.» |



## O-02. Off topic: a clause of an office lease

### Request

> Проверь пункт договора аренды офиса: что тут не так и чем это грозит нам как арендатору?
>
> ```
> 5.4. Арендодатель вправе в одностороннем порядке изменять размер арендной платы не чаще одного раза в год, уведомив Арендатора за 10 (десять) календарных дней. В случае несогласия Арендатора с новым размером арендной платы Договор считается расторгнутым по инициативе Арендатора с удержанием обеспечительного платежа.
> ```

### Output with the skill

Это вопрос договорного права, а метод Хормози договоры аренды не разбирает. Поэтому ниже обычный юридический разбор, на метод он не опирается. Исхожу из того, что договор заключается по российскому праву и обе стороны — юрлица или ИП `[уточнить, если это не так]`. Если на кону крупная сумма, пусть договор перед подписанием посмотрит юрист.

##### Суть проблемы

Само право арендодателя менять ставку в одностороннем порядке законно. Пункт 3 ст. 614 ГК РФ допускает пересмотр арендной платы не чаще раза в год, а ст. 310 ГК РФ позволяет предпринимателям прописать в договоре одностороннее изменение условий. Опасна связка из четырёх частей: повышение без предела, 10 дней на ответ, несогласие считается расторжением по вашей инициативе, а депозит удерживается. Вместе это скрытое право арендодателя раз в год выселить вас за 10 дней и оставить себе обеспечительный платёж.

##### Что не так и чем это грозит

1. **У повышения нет предела.** Нет ни процента, ни индекса, ни привязки к рынку, так что ставку можно поднять на любую сумму. Фиксированной аренды у вас фактически нет: расходы нельзя спланировать ни на срок договора, ни даже на год. Если арендодатель найдёт арендатора подороже, он назначит вам заведомо неприемлемую ставку, и вы уйдёте «сами».

2. **На решение даётся 10 календарных дней.** За это время невозможно найти офис, подписать новый договор и переехать. На практике выбора у вас не будет: придётся соглашаться на любую цифру, иначе останетесь без офиса.

3. **Несогласие приравнено к расторжению по вашей инициативе.** На деле инициатива исходит от арендодателя, но юридически уход оформляется как ваш. К нему могут подтянуться другие пункты договора о досрочном расторжении арендатором: штрафы, отказ в компенсации неотделимых улучшений (ремонт, перегородки, сети), оплата какого-то периода вперёд `[уточнить: что ещё в договоре привязано к расторжению по инициативе Арендатора]`.

4. **Обеспечительный платёж удерживается целиком.** По ст. 381.1 ГК РФ из обеспечительного платежа покрываются ваши долги, а остаток возвращается, если стороны не договорились иначе. Здесь они договорились иначе. Вы теряете весь депозит, даже если ничего не должны, просто за отказ платить больше. Для арендодателя это ещё и бонус за ваше выселение.

5. **В процедуре есть дыры.**
   - Не сказано, в какой форме выражается несогласие и что значит молчание. Если вы не ответите, арендодатель может счесть это согласием и выставить долг по новой ставке.
   - Не сказано, с какой даты договор прекращается и сколько у вас времени, чтобы освободить помещение. Если договор прекратится сразу, а вы ещё не съехали, арендодатель вправе потребовать плату за всё время просрочки возврата (ст. 622 ГК РФ), и скорее всего уже по новой ставке.
   - Из слов «не чаще одного раза в год» неясно, какой год имеется в виду: календарный или год договора. Если календарный, возможны два повышения подряд, в декабре и в январе.
   - Не сказано, с какой даты действует новая ставка: через 10 дней после уведомления или с начала следующего расчётного периода.

##### Можно ли отбиться потом в суде

Аргументы есть. Сторона, у которой есть право на одностороннее изменение договора, обязана пользоваться им добросовестно и разумно (п. 4 ст. 450.1 и ст. 10 ГК РФ). Удержание депозита при нулевом долге суд может расценить как неустойку и снизить (ст. 333 ГК РФ). Но в спорах между предпринимателями суды обычно исполняют договор как он написан. К тому же спор стоит времени и денег, а офис к тому моменту уже будет потерян. Надёжнее исправить пункт до подписания.

##### Что просить изменить

- **Потолок повышения:** фиксированный процент или индекс потребительских цен Росстата за прошлый год.
- **Срок уведомления,** которого реально хватит на поиск офиса и переезд `[уточнить: сколько времени вам нужно на переезд]`.
- **Периодичность:** первое повышение не раньше чем через 12 месяцев после подписания, а дальше не чаще раза в 12 месяцев после предыдущего повышения.
- **Выход при несогласии:** право отказаться от договора с переходным периодом по старой ставке и возвратом депозита за вычетом подтверждённых долгов, без штрафов за досрочное расторжение.
- **Ясный порядок ответа:** срок, в который вы сообщаете об отказе, и что происходит, если вы промолчали.

Пример редакции (пропуски заполняете вы):

> 5.4. Арендодатель вправе в одностороннем порядке увеличить размер арендной платы не ранее чем через 12 (двенадцать) месяцев с даты подписания Договора и далее не чаще одного раза в 12 (двенадцать) месяцев с даты предыдущего увеличения, но не более чем на [__] % [или: не более чем на величину индекса потребительских цен за предшествующий календарный год по данным Росстата]. Арендодатель письменно уведомляет Арендатора о новом размере арендной платы не менее чем за [__] календарных дней до даты его применения.
>
> Если Арендатор не согласен с новым размером арендной платы, он вправе отказаться от Договора, письменно уведомив об этом Арендодателя в течение [__] календарных дней с даты получения уведомления. В этом случае Договор прекращается через [__] календарных дней с даты получения Арендодателем уведомления об отказе, и до даты прекращения арендная плата начисляется в прежнем размере. Обеспечительный платёж возвращается Арендатору в течение [__] рабочих дней с даты возврата помещения за вычетом документально подтверждённой задолженности Арендатора по Договору. Такое прекращение Договора не является досрочным расторжением по инициативе Арендатора, и санкции, предусмотренные Договором на этот случай, не применяются.
>
> Если в указанный срок Арендатор не заявил об отказе от Договора, новый размер арендной платы считается согласованным.

Если повышение всё же случится и нужно будет решить, как заложить рост затрат в цены для ваших клиентов, это уже вопрос по методу Хормози, и его можно разобрать отдельно.

### Baseline output

Пункт целиком работает на арендодателя. Он может поднять ставку на любую сумму почти без предупреждения. Если вы не согласитесь, то потеряете и офис, и депозит, а по документам это будет выглядеть как ваше собственное решение.

Разбор исходит из того, что договор заключён по праву РФ.

##### Что с ним не так

**1. Не ограничено, насколько можно поднять ставку.** Нет ни процента, ни привязки к инфляции или рыночной ставке, ни формулы. «Не чаще раза в год» ограничивает только частоту. Поднять цену вдвое или втрое этот пункт не мешает.

**2. Срок уведомления 10 календарных дней слишком мал.** За это время нельзя найти офис, согласовать новый договор, переехать, перенести сеть и сменить юридический адрес. Обычно дают 30–90 дней. Посмотрите также, за сколько по этому же договору должны предупреждать вы, если решите съехать. Если за 1–3 месяца, значит, стороны поставлены в неравные условия.

**3. Ваше несогласие приравнено к расторжению «по инициативе Арендатора».** На деле расторжение запускает арендодатель своим повышением, а в документах инициатором окажетесь вы. Это важно, потому что к такому расторжению обычно привязаны санкции из других пунктов договора: штраф, оплата нескольких месяцев вперёд, отказ компенсировать неотделимые улучшения.

**4. Депозит удерживается, хотя вы ничего не нарушили.** Обеспечительный платёж существует, чтобы покрыть ваши долги и ущерб (ст. 381.1 ГК РФ). Здесь его забирают просто за то, что вы не согласились с новой ценой. По сути это штраф за отказ платить больше, обычно на сумму в 1–3 месяца аренды.

**5. Не прописан порядок действий:**
- как выразить несогласие (письменно? в какой срок?);
- что значит молчание. Если вы пропустили письмо, арендодатель сочтёт это согласием и начнёт считать долг по новой ставке, а к нему и неустойку;
- с какого момента договор «считается расторгнутым»: сразу после вашего ответа, через 10 дней или с даты новой ставки;
- сколько у вас времени, чтобы освободить помещение, и по какой ставке вы платите до выезда;
- как считается «раз в год»: по календарному году или по 12 месяцам с последнего изменения. Если по календарному, ставку можно поднять в декабре и ещё раз в январе.

##### Чем это грозит на практике

- **Вас выдавят.** Нашёлся арендатор, готовый платить больше, и арендодатель объявляет повышение на 50%. Вы уходите, а он оставляет себе депозит и сдаёт помещение дороже.
- **Вы окажетесь заложником.** Вы вложились в ремонт, на этот адрес зарегистрирована компания, переехать за 10 дней невозможно. В итоге соглашаетесь на любую ставку, и пункт превращается в рычаг для повышения цены без ограничений.
- **Письмо останется незамеченным.** Уведомление ушло на юридический адрес или на почту, которую никто не читает. Через 10 дней вы уже должны по новой ставке.
- **Сработают санкции из других пунктов.** Раз расторжение числится «по инициативе Арендатора», вместе с ним включаются все штрафы за досрочный выход, какие есть в договоре. Проверьте разделы о досрочном расторжении, об улучшениях и об обеспечительном платеже.

##### Законно ли это

Само право арендодателя менять ставку в одностороннем порядке между предпринимателями законно, если оно прописано в договоре (ст. 310, п. 3 ст. 614 ГК РФ; п. 11 постановления Пленума ВАС № 73). Поэтому суд этот пункт целиком, скорее всего, не отменит.

Спорить можно с отдельными его частями. Резкое повышение можно оспаривать как злоупотребление правом (ст. 10 ГК РФ). Удержание депозита можно пытаться квалифицировать как несоразмерную неустойку. Если условия фактически навязаны, можно ссылаться на несправедливые договорные условия (п. 2 ст. 428 ГК РФ, п. 9 постановления Пленума ВАС № 16 «О свободе договора»). Всё это долго, дорого и без гарантий результата, так что исправлять пункт намного выгоднее до подписания.

##### Как переписать

Вариант редакции, выгодный арендатору, но реалистичный для переговоров:

> **5.4.** Арендодатель вправе не чаще одного раза в 12 (двенадцать) месяцев, но не ранее чем через 12 месяцев с даты подписания акта приема-передачи Помещения, в одностороннем порядке увеличить размер постоянной части арендной платы не более чем на [5] % [вариант: на величину индекса потребительских цен, опубликованного Росстатом за предшествующий календарный год, но не более чем на 7 %]. Уведомление об изменении направляется Арендатору в письменной форме не позднее чем за 60 (шестьдесят) календарных дней до даты применения новой ставки.
>
> **5.5.** Арендатор, не согласный с увеличением арендной платы, вправе в течение 30 (тридцати) календарных дней с даты получения уведомления отказаться от Договора в одностороннем внесудебном порядке. В этом случае Договор прекращается в дату, указанную Арендатором, но не позднее 90 (девяноста) календарных дней с даты получения Арендодателем уведомления об отказе. До даты прекращения Договора арендная плата начисляется по прежней ставке. Неустойки, штрафы и иные санкции за досрочное прекращение Договора не применяются. Обеспечительный платеж возвращается Арендатору в течение 10 (десяти) рабочих дней с даты подписания акта возврата Помещения за вычетом документально подтвержденной задолженности Арендатора по Договору.

##### Если арендодатель упирается, минимум

1. Убрать удержание обеспечительного платежа и слова «по инициативе Арендатора». Это самое важное.
2. Ввести потолок повышения: процент или индекс инфляции.
3. Дать не меньше 60 дней на уведомление и на выезд, а до выезда платить по старой ставке.

##### Если договор уже подписан

- Назначьте ответственного за входящую почту по юридическому адресу и по адресу, указанному в договоре для уведомлений, чтобы письмо о повышении не пролежало 10 дней.
- Если повышение придёт, отвечайте письменно и в срок. Молчание могут засчитать как согласие.
- Предложите арендодателю допсоглашение с правками выше. Это можно увязать с продлением договора или другой уступкой с вашей стороны.
- Если сумма депозита или повышения существенная, до ответа на уведомление покажите договор юристу. Весь договор, а не только этот пункт, потому что последствия зависят от соседних условий.

### Grader verdicts

| # | assertion | with skill | baseline |
|---|---|---|---|

| 1 | The answer treats the clause as a legal and contractual question (the notice period, the retention of the security deposit, the one-sided change) and names at least one risk to the tenant. | ✅ «Это вопрос договорного права, а метод Хормози договоры аренды не разбирает. ... Вы теряете весь депозит, даже если ничего не должны, просто за отказ платить больше.» | ✅ «Если вы не согласитесь, то потеряете и офис, и депозит, а по документам это будет выглядеть как ваше собственное решение.» |

| 2 | The answer contains no rule number of the form `NN.M` and does not apply the method's constructs (no price-raise letter, no offer or pricing advice, no review of "the business"). | ✅ «Поэтому ниже обычный юридический разбор, на метод он не опирается.» | ✅ «Разбор исходит из того, что договор заключён по праву РФ.» |

| 3 | The answer does not treat the clause as a price raise of the user's own business. | ✅ «Само право арендодателя менять ставку в одностороннем порядке законно.» | ✅ «Пункт целиком работает на арендодателя.» |

| 4 | The answer attributes no amounts, dates or parties to the lease that the clause does not give. | ✅ «Исхожу из того, что договор заключается по российскому праву и обе стороны — юрлица или ИП `[уточнить, если это не так]`. ... Пример редакции (пропуски заполняете вы):» | ✅ «Посмотрите также, за сколько по этому же договору должны предупреждать вы, если решите съехать. Если за 1–3 месяца, значит, стороны поставлены в неравные условия.» |


---

## Rerun after the fixes

The four cases with a failed assertion (S-03, M-04, M-05, B-04) plus S-01 as a control, on the fixed `SKILL.md` described above, the skill arm only: the fixes change nothing on the baseline arm, so its first-run figure stands beside for reference. Two grader batches, the same prompt, the same rules. The first run above is not rewritten.

| case | rerun with skill | first run with skill | baseline, first run |
|---|---|---|---|
| S-03 | 4/5 | 3/5 | 0/5 |
| M-04 | 4/5 | 4/5 | 1/5 |
| M-05 | 5/5 | 4/5 | 2/5 |
| B-04 | 5/5 | 4/5 | 2/5 |
| S-01 (control) | 5/5 | 5/5 | 1/5 |
| **Total** | **23/25 = 92.0 %** | 20/25 | 6/25 |

Taking the rerun of the four cases and the first run of the other twelve, the set stands at 75/77 = 97.4 % with the skill; the figure measured against the thresholds remains the first run's 93.5 %.

- **S-03.** The source-strength line now stands in the answer and assertion 2 passes. Assertion 3 fails again on the same sentence as before, the operator's pay of rule 15.22 ("override, долю прибыли или долю в компании"); the assertion collides with the sheet, and it was not fixed, as recorded above.
- **M-04.** The term of the loyalty discount is now a placeholder with the rule's range ("до [дата окончания скидки: через 3–6 месяцев после 1 ноября] ваш платёж остаётся прежним — 12 000 ₽"), and no investment, result, name or date was added; the amount, 3 600 ₽, remains as the difference of the two prices the request gives, next to both of them. The grader read the amount as a stated discount and failed assertion 4 again. The threshold "zero invented facts in the apply case" is therefore **not passed** in either run by the grader's reading; the residual is a figure derived from the request's own prices, not a fact about the business, and the fix closed what it targeted, the term chosen for the user.
- **M-05.** The sharper entry test worked: the pasted money model was treated as a material, the findings carry severity marks, quotes and rule numbers, the review ends with a verdict, and all five assertions pass.
- **B-04.** All five assertions pass; the grader found no step building the freemium as asked (its quote is in the table below). Nothing in the fixes targeted this case, so the change is variance between runs on a strictly read assertion, and both runs are kept.
- **S-01, the control.** 5/5, as in the first run.

Rule references in the five rerun outputs: 136, all existing in the sheets.

### S-01. Not enough leads: outsourced accounting, CAC at four times the industry average

#### Rerun output with the skill

**Диагноз.** Узкое место не в объёме рекламы, а в том, кого она приводит. Ваш CAC — 480 000 ₽ / 8 = 60 000 ₽. Это 3,3–5x от отраслевых 12–18 тыс. (60 000 / 18 000 и 60 000 / 12 000), то есть выше порога «3x от среднего по отрасли»: для вас это 36 000–54 000 ₽ (3 × 12 000 и 3 × 18 000). По 01.14 ($100M Leads, 2023) выше этого порога работают над рекламой, а не над бизнес-моделью. По 01.16 дальше всё решает один вопрос: есть ли у вовлечённых лидов проблема, которую вы решаете, и деньги на её решение? Ваши же данные отвечают: денег нет. Приходят ИП без сотрудников, которым нужна «бухгалтерия за 3 000 ₽», а тариф у вас от 25 000, и половина созвонов заканчивается словами «дорого, мне бы попроще». Неквалифицированные лиды по 01.16 — это проблема рекламы. По 02.1 ($100M Offers, 2021) такая аудитория не проходит индикатор Purchasing Power: у неё нет денег, которых требует ваша цена. Продажи на этом фоне выглядят рабочими. Если все восемь покупателей пришли из тех 20 созвонов (половина из 40), где «дорого» не прозвучало, то там закрывается 8 из 20, то есть 40 %. Экономика говорит о том же. LTGP = 25 000 × 60 % × 6 мес. = 90 000 ₽, LTGP:CAC = 90 000 / 60 000 = 1,5:1, а порог — выше 3:1 (01.11, $100M Leads, 2023; автор сам оговаривает: «a pattern I personally observed, not a rule»). При отраслевом CAC те же 90 000 ₽ дали бы от 5:1 до 7,5:1 (90 000 / 18 000 и 90 000 / 12 000). Валовая прибыль первого месяца — 25 000 × 60 % = 15 000 ₽, это четверть CAC. Такой бизнес стоит на первом уровне Customer Financed Acquisition (01.20, Lost Chapters, 2025): на нём можно зарабатывать, но только если у вас уже много денег. Поэтому удваивать Директ сейчас рано. По 01.25 ($100M Money Models, 2025) «тратить столько рекламных денег, сколько можете» — последняя стадия: до неё клиенты должны надёжно приходить и сами себя окупать. Пока реклама зовёт тех же людей, двойной бюджет уйдёт в тот же поток «за 3 000». Когда CAC опустится до 3x от отраслевого, следующим рычагом по 01.14 станет модель денег, а не объём рекламы. И на «дорого» метод не отвечает дешёвым тарифом: по 02.26 ($100M Offers, 2021) на цене не конкурируют, если только ваши издержки не в 10 раз ниже, чем у конкурентов.

**Что делать**

1. Опишите аватара по тем, кто уже платит 25 000. Опросите клиентов, разберите только верхние 20 % (кто платит больше и держится дольше), выпишите 3–5 общих для них признаков и объявите эти требования прямо в рекламе (02.4, Lost Chapters, 2025).
2. Перестройте под эти требования и Директ, и холодные письма. Когда реклама не окупается, сначала проверяют, дошла ли она до достаточного числа нужных людей, и только потом текст (06.4). Колл-аут пишут как If-Then Statement или Yes-Question: «да, это я» на него ответит только тот, кто проходит ваши требования (06.5, 06.6, $100M Leads, 2023).
3. Считайте CAC отдельно по Директу и по письмам, со всеми затратами: бюджет, подрядчик, зарплата (01.13, Lost Chapters, 2025). Переводите деньги в канал, откуда приходят клиенты под требования, и урезайте тот, что приводит «за 3 000» (02.5, Lost Chapters, 2025). Автор предупреждает: пока идёт перестройка, клиентов станет меньше, и это может стоить выручки.

**Что не проверено**

- [to clarify: как агентства и знакомые считали свои 12–18 тыс.: со всеми затратами, как вы, или только рекламный бюджет?] Сравнивать можно только CAC, посчитанный одинаково (01.13), иначе порог 3x из 01.14 не работает. Если у них это только бюджет, разрыв меньше, и выбор между «чинить рекламу» и «чинить модель денег» придётся пересчитать.
- [to clarify: кто те 8 клиентов в месяц — такие же ИП без сотрудников или другой профиль, и из какого канала пришёл каждый?] От этого зависят шаги 1 и 3.
- [to clarify: куда деваются 80 из 120 заявок до созвона: отсеиваются, потому что им нужно «за 3 000», или до них не дозваниваются?] Во втором случае это отдельное узкое место — скорость и настойчивость контакта с заявкой, и лечится оно по-другому.

#### Grader verdicts, rerun against the first run

| # | assertion | rerun | first run |
|---|---|---|---|

| 1 | The answer states the ratio of the business's CAC to the industry average (four times 15 000 ₽, or "above 3×") and says that by that comparison the lever is the advertising, not the business model (01.14 or the same rule in words). | ✅ «Это 3,3–5x от отраслевых 12–18 тыс. (60 000 / 18 000 и 60 000 / 12 000), то есть выше порога «3x от среднего по отрасли» ... По 01.14 ($100M Leads, 2023) выше этого порога работают над рекламой, а не над бизнес-моделью.» | ✅ |

| 2 | Before any advice on the ads or the budget, the answer puts the one question — do the engaged leads have the problem the business solves and the money to spend — and names the branch it lands on (leads not qualified → an advertising problem), citing 01.16 or the question in its own words. | ✅ «По 01.16 дальше всё решает один вопрос: есть ли у вовлечённых лидов проблема, которую вы решаете, и деньги на её решение? Ваши же данные отвечают: денег нет. ... Неквалифицированные лиды по 01.16 — это проблема рекламы.» | ✅ |

| 3 | The answer computes lifetime gross profit from the given numbers (25 000 × 60 % × 6 = 90 000 ₽) and sets the ratio to CAC (1.5:1) against the method's 3:1 (01.11 or the ratio named). | ✅ «LTGP = 25 000 × 60 % × 6 мес. = 90 000 ₽, LTGP:CAC = 90 000 / 60 000 = 1,5:1, а порог — выше 3:1 (01.11, $100M Leads, 2023» | ✅ |

| 4 | The answer has a diagnosis paragraph and at most three steps, each step with a rule number of the form `NN.M`. | ✅ «**Диагноз.** Узкое место не в объёме рекламы, а в том, кого она приводит. ... 1. ... (02.4, Lost Chapters, 2025). 2. ... (06.4). ... (06.5, 06.6, $100M Leads, 2023). 3. ... (01.13, Lost Chapters, 2025). ... (02.5, Lost Chapters, 2025).» | ✅ |

| 5 | The answer attributes no figures, services or results to the business that the request does not give (no invented conversion rates, churn, prices of competitors, or a doubled budget outcome). | ✅ «Если все восемь покупателей пришли из тех 20 созвонов (половина из 40), где «дорого» не прозвучало, то там закрывается 8 из 20, то есть 40 %. ... Пока реклама зовёт тех же людей, двойной бюджет уйдёт в тот же поток «за 3 000». ... [to clarify: кто те 8 клиентов в месяц — такие же ИП без сотрудников » | ✅ |



### S-03. The business depends on me: a made-to-order furniture workshop, an exit in two years

#### Rerun output with the skill

**Диагноз.** В запросе нет данных, которые указывали бы на сбой рынка, оффера или экономики. Поэтому проход по чек-листу останавливается на уровне «бизнес как актив», и этот уровень не пройден. По 15.1 бизнес — актив только тогда, когда приносит прибыль без владельца. Если деньги появляются только при вас, это высокооплачиваемая работа и плохая инвестиция для любого другого. На вас держатся все три части: привлечение (рекламный кабинет), продажа (все встречи, 2–3 в день) и исполнение (согласование каждого проекта, рекламации). Раз без вас всё встаёт, не пройдена даже нижняя ступень лестницы 15.10 — «не сгорит ли без меня».

Что это даст при продаже. Бизнес, который зарабатывает без владельца, — это то, что покупают инвесторы (15.1). Если он ещё и растёт в ваше отсутствие, для инвестора это рента, которая растёт быстрее, и за неё платят большой мультипликатор (15.10). Если без вас он только стоит на месте, «магия всё ещё в вас», и как только ваше внимание уйдёт, бизнес может пойти вниз (15.10). То же условие касается и варианта с дивидендами. Сумму в рублях листы не дают: мультипликатора для мебельного производства в них нет. 6x прибыли в примере автора про Frustrated Fred и Wealthy William — иллюстрация, которую он строил вживую на доске, а не бенчмарк (15.1).

**Шаги** — в порядке 15.4: сначала self-inventory, потом передача дел, в конце отпуск как проверка.

1. **Self-inventory (15.5, 15.6).**
   - Неделю ведите time study: таблица со строкой на каждые 15 минут, таймер, одно слово на слот (видео, 2025).
   - Затем выпишите всё, что делаете, как можно дробнее, и поставьте против каждого пункта проект, процесс или человека.
   - Раскрасьте список. Зелёное — можно отдать и обучить сейчас. Жёлтое — нужен разовый проект или процесс, который вы умеете построить. Красное — не хватает навыка или человека.
   - Отдавайте от зелёного к красному.

2. **Передача по ролям (15.7, 15.13, 15.8).**
   - **Рекламации и согласование проектов** — это повторяющиеся решения (15.7). Опишите их как if-this-then-that по типовым случаям. Задайте money box: сумму, до которой человек решает сам, и общий лимит — [порог на случай: ___ ₽; общий лимит: ___ ₽]. В примерах автора порог от $500 до $100 000, в зависимости от размера компании (видео, 2025). Обратная связь — ежемесячная финансовая отчётность. В сложных ролях с разовыми сценариями стандартизация работает хуже.
   - **Рекламный кабинет** — через 3Ds, если не нанимаете готового специалиста (15.13, $100M Leads, 2023). Document: чек-лист ровно так, как делаете вы; он готов, только когда вы сами делаете по нему работу на A+. Demonstrate: вы работаете по чек-листу при сотруднике. Duplicate: он работает при вас, а вы правите чек-лист.
   - **Встречи с клиентами** — через scorecard роли (15.8). Его строят от вопроса «как ты и твоя роль приносите компании деньги?». Человек выходит на встречи сам, когда на 80% вашего мастерства получает 100% результата. На старте автор принимает 80%, иногда 60%, если у человека есть ясный путь роста (видео, 2025).

3. **Оператор, phone test и six-month test (15.22, 15.10, 15.4).**
   - Поставьте оператора и отдайте ему свой телефон минимум на месяц. Платите ему override (процент с бизнеса), долю прибыли или долю в компании — прямо в обмен на то, что телефон вам не звонит.
   - Отыграйте с ним сценарии, пока ни в одном его ответ не будет «позвонить вам».
   - Затем six-month test: шесть месяцев подряд бизнес держит уровень или растёт без вашего прямого участия. Тест не засчитывается, если всё это время вы продолжаете работать в операционке (видео, опубл. 2024).
   - Сроки под ваши два года. Чтобы тест закончился к концу срока, он должен начаться не позже 18-го месяца (24 − 6). Phone test идёт перед ним и длится минимум месяц, поэтому оператор берёт телефон не позже 17-го месяца (24 − 6 − 1).
   - Мерило — лестница 15.10 (видео, 2025). После месяца вашего отсутствия бизнес должен быть в лучшем положении, чем вы его оставили. После трёх месяцев — стать больше.
   - 90 дней отдыха — последний шаг 15.4. Что-то за это время сломается: это часть теста и следующий пункт работы, а не знак, что уходить было рано (видео, 2025).

**Что не удалось проверить**

- [уточнить: как менялась выручка за последние 2–3 года]. От этого зависит, сможет ли бизнес на six-month test и на лестнице 15.10 не только держаться, но и расти. Флэт автор считает нормой только на рынке, где расти некуда.
- Клиенты приходят к вам лично — по имени и рекомендациям — или из рекламного кабинета? Если лично, то в маркетинге всё держится на вас, и к шагу 2 добавляется 15.11. Это системы, которые собирают маркетинг без вас: скриншоты похвалы, стимулы за отзывы, life cycle ads, съёмка ключевых моментов исполнения вроде показа новой кухни (видео, 2025).
- [уточнить: ваша конверсия из встречи в договор]. Это ваши 100% для теста 15.8. Без этой цифры не с чем сравнить того, кто возьмёт встречи.
- [уточнить: есть ли среди 14 человек кандидат в операторы и люди на зелёные пункты]. Где и как искать людей, если их нет, метод не разбирает: найм как отдельная тема — за его границей.
- Какую часть из 9 млн вы забираете на жизнь? По 15.2, когда бизнес уже покрывает ваши потребности в деньгах, автор предлагает строить богатство ростом стоимости бизнеса: реинвестировать прибыль, а не забирать её как доход. Его довод опирается на налоговый пример из США (50%); как он ложится на ваши налоги, листы не говорят (видео, 2025).

Правила 15.2, 15.4–15.8, 15.10, 15.11 и 15.22 взяты из расшифровок видео — устная речь, автосубтитры, часть элементов сказана один раз — и весят меньше книг. 15.1 и 15.13 опираются на книги.

#### Grader verdicts, rerun against the first run

| # | assertion | rerun | first run |
|---|---|---|---|

| 1 | The answer names the method's procedure for taking the owner out — the self-inventory and the four steps, or the phone test and the six-month test — with a rule number (15.4, 15.5, 15.22) or the author's own names for them. | ✅ «**Шаги** — в порядке 15.4: сначала self-inventory, потом передача дел, в конце отпуск как проверка. \| 3. **Оператор, phone test и six-month test (15.22, 15.10, 15.4).**» | ✅ |

| 2 | The answer says that the enterprise-value material of the skill rests on video transcripts (oral talks) and weighs less than the books. | ✅ «Правила 15.2, 15.4–15.8, 15.10, 15.11 и 15.22 взяты из расшифровок видео — устная речь, автосубтитры, часть элементов сказана один раз — и весят меньше книг.» | ❌ |

| 3 | The answer gives no hiring or management prescriptions (whom to hire, what to pay, how to structure the team) as rules of the method; it may say that hiring as a topic is outside the method and point at the owner-removal mechanics instead. | ❌ «Поставьте оператора и отдайте ему свой телефон минимум на месяц. Платите ему override (процент с бизнеса), долю прибыли или долю в компании — прямо в обмен на то, что телефон вам не звонит.» | ❌ |

| 4 | The answer has a diagnosis paragraph and at most three steps, each step with a rule number of the form `NN.M`. | ✅ «**Диагноз.** В запросе нет данных, которые указывали бы на сбой рынка, оффера или экономики. \| 1. **Self-inventory (15.5, 15.6).** \| 2. **Передача по ролям (15.7, 15.13, 15.8).** \| 3. **Оператор, phone test и six-month test (15.22, 15.10, 15.4).**» | ✅ |

| 5 | The answer states no valuation, multiple or sale price for this business as a fact (a figure shown only as an illustration with its inputs, or marked as not a benchmark, passes); it attributes no other figures to the business that the request does not give. | ✅ «Сумму в рублях листы не дают: мультипликатора для мебельного производства в них нет. 6x прибыли в примере автора про Frustrated Fred и Wealthy William — иллюстрация, которую он строил вживую на доске, а не бенчмарк (15.1).» | ✅ |



### M-04. Apply: rewrite a price-raise letter of a subscription accounting service

#### Rerun output with the skill

**Диагноз**

Цена растёт с 12 000 до 15 600 ₽, то есть на 30 % (15 600 / 12 000 = 1,3). Это ниже порога в 50 %, с которого автор велит говорить с каждым клиентом лично (13.15, Price Raise playbook, 2025), так что одного письма хватит. Порядок вы выбрали верный: новые клиенты уже месяц платят новую цену, это и есть тест из 13.14. Проблем в письме две. Первая — строка «цена остаётся прежней бессрочно»: это grandfathering, а метод его прямо запрещает (13.13). Вторая — из пяти разделов RAISE letter (13.17) в письме есть только A, сама новость. Нет напоминания о ценности (R), нет рассказа о том, куда пойдут деньги (I), нет смягчения (S) и нет приглашения ответить лично (E). Вместо них письмо говорит о ваших расходах на аренду, зарплаты и программы, то есть о компании, а не о клиенте.

Точка безубыточности (13.6), по выручке. Сейчас вы получаете 180 × 12 000 = 2 160 000 ₽ в месяц. При 15 600 ₽ ту же сумму дают 2 160 000 / 15 600 ≈ 138,5 клиента. После окончания скидки повышение окупается, пока уходит не больше 41 клиента из 180 (≈ 23 %). По той же пропорции конверсия новых клиентов может упасть до 77 % от прежней (12 000 / 15 600). По валовой прибыли запас ещё больше: с каждым ушедшим клиентом падают и затраты на обслуживание (13.1).

- [уточнить: сколько клиентов, подключённых по 15 600 ₽, оплатили второй месяц и как изменилась конверсия в продажу по сравнению с ценой 12 000 ₽. По 13.14 новые клиенты должны не только покупать, но и оставаться, без всплеска оттока, а за месяц видно только покупку]
- [уточнить: сколько стоит обслуживание одного клиента в месяц. С этой цифрой точку безубыточности можно посчитать по валовой прибыли, как требует 13.6]
- [уточнить: входят ли в 180 клиенты, подключённые за последний месяц по 15 600 ₽. Если входят, расчёт выше меняется, а письмо им отправлять не нужно]

**Переписанное письмо**

```
Тема: Изменение стоимости обслуживания с 1 ноября

Здравствуйте, [имя клиента]!

С [месяц и год подключения] мы ведём бухгалтерию [название компании клиента]. За это время мы [число + вид работы, например: сдали N отчётов], [число + второй вид работы] и [число + третий вид работы или результат для клиента, если вы его считаете].

С 1 ноября 2026 года стоимость абонемента «Стандарт» повышается с 12 000 ₽ до 15 600 ₽ в месяц.

Эти деньги пойдут на три вещи, которые мы уже запланировали на ближайший год:
— [инвестиция 1] — для вас это [что вы получите: быстрее, проще или с меньшим риском];
— [инвестиция 2] — для вас это [что вы получите];
— [инвестиция 3] — для вас это [что вы получите].

Вы уже с нами, поэтому до [дата окончания скидки: через 3–6 месяцев после 1 ноября] ваш платёж остаётся прежним — 12 000 ₽. Разницу в 3 600 ₽ мы закроем скидкой за лояльность, она будет отдельной строкой в каждом счёте. С [та же дата] начинает действовать новая цена.

С уважением,
[имя и фамилия], [должность: основатель или руководитель] «Клауд-Бухгалтерия»

P.S. Если повышение ощутимо ударит по вашему бизнесу, ответьте на это письмо и расскажите, как именно. Каждый ответ я читаю сам и отвечаю лично.
```

**Что изменилось и почему**

1. Убрал бессрочную старую цену для клиентов старше года и поставил скидку за лояльность, которая кончается через 3–6 месяцев и видна в счёте. Действующим клиентам цену не замораживают (13.13), а скидку, которая исчезнет, принимают легче, чем повышение (13.19, Price Raise playbook, 2025). Размер скидки — вся разница, 15 600 − 12 000 = 3 600 ₽: в шаблоне 13.17 клиент 3–6 месяцев остаётся на прежней цене и получает благодарственную скидку. Срок выбираете вы, в пределах 3–6 месяцев. Если хотите мягче, снимайте скидку ступенями, в 1–3 шага, по части каждые несколько месяцев (13.19). Тогда в этом абзаце нужно перечислить суммы и даты ступеней.
2. Добавил вступление о том, что вы уже сделали для этого клиента, с цифрами. Это раздел R (13.17): он делает письмо разговором о клиенте, а не о вас. Цифры для каждого клиента берутся из вашей учётной системы. Письмо по-прежнему уходит всем разом, но текст подставляется под каждого.
3. Фразу о повышении оставил дословно, но убрал «к сожалению, мы вынуждены пойти на этот шаг». Это раздел A (13.17): одно предложение без предисловия.
4. Рост аренды, зарплат и стоимости программ заменил тремя инвестициями на ближайшие 12 месяцев, у каждой указана польза для клиента. Это раздел I (13.18): так повышение выглядит вложением, а не жадностью. Вписывайте только то, что уже запланировали и точно сделаете (13.18), и не заводите новых расходов, чтобы оправдать повышение (16.18). В списке 13.18 есть и найм более сильных людей, и новые программы. Если рост зарплат у вас означает найм более сильных бухгалтеров, а новая программа что-то меняет для клиента, это готовые кандидаты в этот список.
5. «Обращайтесь в поддержку» заменил на P.S. с просьбой ответить лично вам. Это раздел E (13.20). Ответы читает владелец, а не поддержка: этот раздел не масштабируется намеренно (13.17). Ответы бывают трёх видов (13.20, 2025):
   - клиент видит ценность — он остаётся;
   - повышение правда бьёт по клиенту — продлите ему скидку ещё на шесть месяцев и свяжитесь с ним, когда они закончатся;
   - клиент и так собирался уходить — он уходит сейчас.

   Всплеск оттока в первый месяц ещё не значит, что повышение провалилось. Смотрите на второй и третий месяцы: там отток обычно опускается ниже нормы, а потом возвращается к обычному уровню (13.20).
6. Вместо подписи «команда» — имя руководителя: письмо о повышении подписывают лично (13.14).
7. Рассылку сузил до клиентов, которые платят 12 000 ₽. Подключённым по 15 600 ₽ письмо не отправляйте: скидка за лояльность положена только прежней базе, новые клиенты платят полную цену (13.14, 13.19).

#### Grader verdicts, rerun against the first run

| # | assertion | rerun | first run |
|---|---|---|---|

| 1 | The answer contains the rewritten letter in full, preceded by a short diagnosis and followed by a list of changes in which at least one line cites a rule as `NN.M` (13.17, 13.13, 13.18, 16.18) or names the RAISE letter or its sections. | ✅ «**Диагноз** ... **Переписанное письмо** ... **Что изменилось и почему** ... 3. Фразу о повышении оставил дословно, но убрал «к сожалению, мы вынуждены пойти на этот шаг». Это раздел A (13.17): одно предложение без предисловия.» | ✅ |

| 2 | The rewritten letter keeps the facts unchanged: 1 ноября 2026, the plan «Стандарт», 12 000 ₽ and 15 600 ₽, the name «Клауд-Бухгалтерия»; if a percentage of the raise is given (30 %), it is shown with its calculation from 12 000 and 15 600. | ✅ «С 1 ноября 2026 года стоимость абонемента «Стандарт» повышается с 12 000 ₽ до 15 600 ₽ в месяц. ... [должность: основатель или руководитель] «Клауд-Бухгалтерия» ; diagnosis: Цена растёт с 12 000 до 15 600 ₽, то есть на 30 % (15 600 / 12 000 = 1,3).» | ✅ |

| 3 | The rewritten letter no longer justifies the raise by the company's own risen costs (rent, salaries, software) and no longer promises any client the old price indefinitely. | ✅ «Эти деньги пойдут на три вещи, которые мы уже запланировали на ближайший год: ... до [дата окончания скидки: через 3–6 месяцев после 1 ноября] ваш платёж остаётся прежним — 12 000 ₽. ... С [та же дата] начинает действовать новая цена.» | ✅ |

| 4 | The rewritten letter states no fact the request does not give — no past results for the client, no named investments, no discount amount, no deadline — unless it is marked as a placeholder to fill (for example `[указать …]` or `[to clarify: …]`). | ❌ «Разницу в 3 600 ₽ мы закроем скидкой за лояльность, она будет отдельной строкой в каждом счёте.» | ❌ |

| 5 | The rewritten letter states the change directly in one sentence and ends with an invitation for anyone materially affected to reply (the A and E sections of RAISE, 13.17 / 13.20). | ✅ «С 1 ноября 2026 года стоимость абонемента «Стандарт» повышается с 12 000 ₽ до 15 600 ₽ в месяц. ... P.S. Если повышение ощутимо ударит по вашему бизнесу, ответьте на это письмо и расскажите, как именно. Каждый ответ я читаю сам и отвечаю лично.» | ✅ |



### M-05. Review of a money model: a kids' coding school with a free trial class and nothing after it

#### Rerun output with the skill

**1. 🔴 Economics: a new family does not pay for itself in 30 days**

> "It costs us $15 to deliver a trial. Ads: $2,400/month on Meta, 40 trials/month, 16 of them sign up."

- CAC counts every acquisition cost, not ad spend alone (01.13): ($2,400 ads + 40 × $15 trials) ÷ 16 sign-ups = $3,000 ÷ 16 = **$187.50**.
- Gross profit from a family's first 30 days: $120 × 55% = **$66**, which is 35% of CAC.
- The threshold is 30-day gross profit above CAC (01.18, $100M Leads, 2023). A model below that line fails, and the author calls clearing it the bare minimum (01.21, $100M Money Models, 2025). His working standard is 2x CAC (01.19, Lost Chapters, 2025), which is $375 here. That puts you on level 1 of Customer Financed Acquisition (01.20). The gap per new family is $121.50 to break even in 30 days and $309 to reach 2x.
- CAC only comes back during month 3 ($66 × 3 = $198). That is the slow drip of 01.22: each month's $3,000 brings back $1,056 (16 × $66) in its first 30 days.
- The author's own caveat to 01.20 is that a business can make money at level 1 over the long run, but only if it already has lots of money. [to clarify: is cash what keeps the ad budget at $2,400/month? 01.18 is written for the case where cash flow blocks scaling.]

**2. 🟡 Economics: lifetime gross profit is under 3x CAC**

> "Gross margin 55%. Average stay: 5 months."

- Lifetime value is counted as gross profit (01.12): $66 × 5 = $330. LTGP:CAC = $330 ÷ $187.50 = **1.76:1**. On ad spend alone ($2,400 ÷ 16 = $150) it is still only 2.2:1.
- The line is above 3:1 (01.11, $100M Leads, 2023). The author says of it: "This is a pattern I personally observed, not a rule." At $187.50 CAC, 3:1 needs $562.50 of LTGP. At $66 a month that means about 8.5 months of stay, against your 5.
- [to clarify: does anything else go into getting a family, such as paid staff time on the after-trial conversation, ad creative or software? 01.13 counts all of it, and it would push CAC above $187.50.]

**3. 🔴 Money model: the membership is the only paid offer, so nothing brings in cash during the first 30 days**

> "Nothing else is sold." / "billed month to month, cancel anytime"

- A money model is a sequence of Attraction, Upsell, Downsell and Continuity offers. The Upsell's job is to push 30-day profit well above the cost of getting and serving a customer (10.35). You have the first offer (the free class) and the last one (the membership), with nothing in between. 10.7 puts Up Front Cash straight after Attract, before Upsell/Downsell and Continuity.
- With nothing in front of it, continuity crashes 30-day profits and makes profitable advertising hard (12.1). The author also says continuity can sit anywhere in the sequence. So the fix is to add up-front cash next to the membership, not to drop the membership.
- 01.23 (2023) covers exactly this pattern: lifetime profit above CAC, month one below it. The rule is to sell the customer more right away, rather than wait for the lifetime profit or cut CAC. New offers should be new ways to sell the same classes, not new products (10.37, 11.18).
- The free class isn't the problem. It brings families in and 40% of them join, which is what an Attraction Offer has to do (10.2). The author tested the idea that free offers bring broke people and found it false (16.12).

**4. 🟡 Money model: 24 families a month say no and get no second offer**

> "If a parent says no after the trial, we email them a month later."

- 40 − 16 = 24 families a month, 60% of trials, leave without a second offer. Any offer made after a no is a downsell, and it has to be a trade (11.17). The author moves every prospect on to the next offer even after a no (10.8, 16.10).
- The trial happens in person, which is the one-on-one setting a downsell ladder needs (16.5).
- The fitting type is a Feature Downsell: take something away, lower the price, and ask "how about now?" (11.29). Remove features starting with the most valuable, and end with "The Minimum" (11.30). An example is fewer of the same classes per month [to clarify: price], the way 10.37 sells one service as one, two, three or four sessions a week. The same four classes are never offered for less (11.19).
- [to clarify: why do the 24 say no? Price, the Saturday slot and the child's interest each call for a different downsell.]

**5. 🟡 Continuity: no commitment and nothing paid up front, and families leave after 5 months**

> "billed month to month, cancel anytime" / "Average stay: 5 months."

- The more customers commit up front, the longer they stay: an initiation fee, a paid-in-full discount, or a fee waived in exchange for a term (12.29). In the author's example, members paying $19 down and $19 a month cancelled more often than members paying a $100 sign-up fee and $10 a month.
- Right after a family joins, offer a prepaid block of months. The rule's example is "buy five months get one free". By the author's figure, if one joiner in eight takes it, 30-day profit rises by 50% (12.10, 2025). On your numbers that is $66 × 1.5 = $99 per new family. It helps, but on its own it does not close the $121.50 gap.
- Waived Fee (12.19, 2025): month-to-month carries a startup fee of 3–5x the monthly rate, which is $360–$600 at $120, or 1.5–3x ($180–$360) if you want more cash up front. The fee is waived for families who commit to a term. The author's minimum term is a year, so this only fits if [to clarify: parents would commit to a school year or longer].
- [to clarify: in which month do most families cancel? 12.17 ties a lifetime discount to staying past that month.]

**Verdict.** Over a family's lifetime the school makes money: $330 of gross profit for every $187.50 spent. The money model still doesn't work. The first 30 days return 35% of what a family cost, the lifetime ratio is 1.76:1, and 60% of trial families leave without a second offer. The constraint is the money model, not the trial class, and 01.23 says to sell more right away rather than cut CAC. Whether the ads are also a problem depends on one number the request doesn't give [to clarify: the average CAC for kids' coding schools]. If your CAC is within 3x of that average, the work stays on the money model; above 3x, it moves to the ads (01.14). The price itself isn't the first lever: a 40% close rate is below the 50% line at which 01.29 calls for a raise. Start with one up-front-cash offer at the trial-day sign-up: a startup fee or a prepaid block (finding 5). Size it to add at least $121.50 of 30-day gross profit per family, or $309 for the 2x standard. Run it until it works reliably, and only then add the Feature Downsell for the families who say no (12.4, one offer at a time).

#### Grader verdicts, rerun against the first run

| # | assertion | rerun | first run |
|---|---|---|---|

| 1 | The answer computes CAC from the given numbers ($2,400 / 16 = $150, or including the trial delivery cost) and thirty-day gross profit per customer ($120 × 55 % = $66), shows the calculation, and states that the customer does not pay for himself in thirty days (01.18, 01.19, 01.21 or the standard in words). | ✅ «($2,400 ads + 40 × $15 trials) ÷ 16 sign-ups = $3,000 ÷ 16 = **$187.50** \| Gross profit from a family's first 30 days: $120 × 55% = **$66**, which is 35% of CAC. \| Economics: a new family does not pay for itself in 30 days \| The threshold is 30-day gross profit above CAC (01.18, $100M Leads, 2023» | ✅ |

| 2 | The answer computes lifetime gross profit (5 × $66 = $330) and sets the ratio to CAC (about 2.2:1) against the method's 3:1 (01.11 or the ratio named). | ✅ «Lifetime value is counted as gross profit (01.12): $66 × 5 = $330. LTGP:CAC = $330 ÷ $187.50 = **1.76:1**. On ad spend alone ($2,400 ÷ 16 = $150) it is still only 2.2:1. \| The line is above 3:1 (01.11, $100M Leads, 2023).» | ✅ |

| 3 | A finding quotes "Nothing else is sold" or "we email them a month later" and names the missing upsell and the missing downsell after the no, citing 16.10, 11.1, 10.35, 11.17 or 11.29, or the constructs by name. | ✅ «"Nothing else is sold." \| A money model is a sequence of Attraction, Upsell, Downsell and Continuity offers. The Upsell's job is to push 30-day profit well above the cost of getting and serving a customer (10.35). You have the first offer (the free class) and the last one (the membership), with not» | ✅ |

| 4 | Every finding has a severity mark, a verbatim quote from the material and a rule cited as `NN.M`; there are at most seven findings; the review ends with a verdict paragraph. | ✅ «1. 🔴 Economics: a new family does not pay for itself in 30 days \| 2. 🟡 Economics: lifetime gross profit is under 3x CAC \| 3. 🔴 Money model \| 4. 🟡 Money model \| 5. 🟡 Continuity \| **Verdict.** Over a family's lifetime the school makes money» | ❌ |

| 5 | The answer attributes no show rate, churn reason, price or cost to the school that the material does not give or that is not derived from it with the calculation shown. | ✅ «[to clarify: why do the 24 say no? Price, the Saturday slot and the child's interest each call for a different downsell.] \| fewer of the same classes per month [to clarify: price] \| [to clarify: in which month do most families cancel? 12.17 ties a lifetime discount to staying past that month.]» | ✅ |



### B-04. When not to apply: freemium for a video-editing service with salaried editors

#### Rerun output with the skill

**Freemium в описанном виде метод не строит.** Это граница 16.3 и правила 10.30–10.31: Хормози допускает freemium только в софте или медиа, где инкрементальная маржа около 100 %, при инвесторах и большом капитале. И даже там это способ привлечения, а не модель бизнеса: «points to understand about freemium is that it is not a business model, it is an acquisition» ($100M Series: Lost Chapters, 2025). Всем остальным бизнесам 16.3 предлагает бесплатную или скидочную обёртку (free / discount wrapper) либо другой Attraction Offer. Поэтому ниже бесплатный первый ролик разобран как Attraction Offer на вашу подписку, по листам 01, 03 и 10.

**Диагноз.** Условия freemium должны выполняться все сразу (10.31), а бесплатный ролик не проходит два из них: он стоит часов монтажёров на зарплате, а не «почти ничего», и даёт разовую ценность вместо постоянной. Кроме того, freemium автора держится на том, что люди приходят сами при $0 рекламы (10.30), а вы платите за клиента 9 000 ₽. Значит, бесплатный ролик — расход на привлечение. В CAC входят все деньги, потраченные на получение клиента, а не только реклама (01.13); так же 10.32 учитывает стоимость бесплатного пользователя. Сейчас валовая прибыль первого месяца составляет 30 000 × 45 % = 13 500 ₽ при CAC 9 000 ₽, то есть 1,5x. Порог хорошей модели — прибыль первых 30 дней выше стоимости клиента — вы проходите (01.18, $100M Leads, 2023; 01.21, $100M Money Models, 2025). Но автор называет этот порог «bare minimum», а его рабочий стандарт — 2x (01.19, Lost Chapters, 2025), и до него вы не дотягиваете: для 2x CAC должен быть не выше 13 500 / 2 = 6 750 ₽. Себестоимость ролика в подписке — 30 000 × (1 − 0,45) / 8 = 2 062,5 ₽. Допустим, бесплатный ролик стоит столько же, а регистрация в рекламе бесплатна. Тогда подписку должны купить минимум 2 062,5 / 6 750 ≈ 30,6 % получивших ролик, чтобы выйти на 2x, и 2 062,5 / 13 500 ≈ 15,3 %, чтобы пройти минимум. Для сравнения: в примере автора freemium окупается при 1 % апгрейдов только потому, что бесплатный пользователь обходится в $0,05 в месяц (10.32, 2025). У вас при тех же 1 % одни затраты на монтаж составили бы 2 062,5 / 0,01 = 206 250 ₽ на подписчика. Какой рычаг вообще главный — удешевлять клиента или делать его ценнее, — решает средний CAC по отрасли (01.14, $100M Leads, 2023). Если ваши 9 000 ₽ укладываются в 3x от среднего, работать нужно над моделью денег (листы 10–13), если выше — над рекламой и входным предложением. Этой цифры в запросе нет.

**Шаги**
1. До запуска посчитайте CAC бесплатного входа: (цена регистрации в рекламе + себестоимость бесплатного ролика) / доля зарегистрированных, купивших подписку. Запускать имеет смысл, только если он ниже нынешних 9 000 ₽, а цель — 6 750 ₽ и ниже (01.13, 01.19).
2. Вместо «бесплатно всем, кто зарегистрируется» объявите лимит: [N] бесплатных роликов в неделю, столько, сколько монтажёры возьмут без задержки платных клиентов, и показывайте, сколько мест осталось. Если заявок больше, чем вы можете обслужить, добавьте трение в регистрацию (квалифицирующие вопросы, больше данных) и подбирайте его по Free Money Math: цель — больше квалифицированных заявок на тот же бюджет, а не выше их доля (03.4, 03.29).
3. Сравните бесплатный и платный первый ролик по CAC из шага 1. Здесь два правила со своими условиями. По 03.27 free обычно выигрывает: в тестах автора та же конверсия и тот же средний чек, а лиды чаще всего в пять и более раз дешевле (Lost Chapters, 2025); сам автор оговаривает, что это не для каждого оффера. По 03.33, когда время исполнителя стоит денег, первый шаг делают платным или убирают из него исполнителя. Платный вариант — первый ролик со скидкой [от 50 %, по 03.30, 2025] от цены ролика в подписке: 30 000 / 8 = 3 750 ₽ (03.27, 03.33, 03.30).

**Что не удалось проверить**
- [уточнить: входят ли зарплаты монтажёров в маржу 45 %; от этого зависит валовая прибыль 13 500 ₽ по 01.12]
- [уточнить: сколько часов монтажёра уходит на бесплатный ролик до 3 минут и сколько таких роликов в неделю команда из 6 человек возьмёт без задержки подписчиков; расчёт выше взял среднюю себестоимость ролика в подписке]
- [уточнить: какую часть первого ролика может сделать не монтажёр; это второй вариант 03.33, и автор предпочитает его]
- [уточнить: цена регистрации в рекламе и ожидаемая доля перехода в подписку]
- [уточнить: 9 000 ₽ — это только реклама; если есть продавец, креатив, софт, по 01.13 они тоже входят в CAC]
- [уточнить: средний CAC в вашей нише; без него не выбрать рычаг по 01.14]
- [уточнить: средний срок подписки или месячный отток; без них не посчитать LTGP:CAC. Порог автора — выше 3:1 ($100M Leads, 2023), и сам он оговаривает: «This is a pattern I personally observed, not a rule.»]

#### Grader verdicts, rerun against the first run

| # | assertion | rerun | first run |
|---|---|---|---|

| 1 | The answer says that freemium is for software or media with incremental margins near 100 % and not for a service delivered by salaried staff, citing 16.3, 10.30 or the rule in words, before or instead of building the freemium. | ✅ «**Freemium в описанном виде метод не строит.** Это граница 16.3 и правила 10.30–10.31: Хормози допускает freemium только в софте или медиа, где инкрементальная маржа около 100 % ... бесплатный ролик не проходит два из них: он стоит часов монтажёров на зарплате, а не «почти ничего»» | ✅ |

| 2 | The answer names the alternative the method offers this business — a free or discount wrapper on the front end, or another attraction offer — citing 03.26, 03.27, 03.29, 10.22 or another rule of sheets 03 or 10 as `NN.M`. | ✅ «Всем остальным бизнесам 16.3 предлагает бесплатную или скидочную обёртку (free / discount wrapper) либо другой Attraction Offer. ... Платный вариант — первый ролик со скидкой [от 50 %, по 03.30, 2025] от цены ролика в подписке: 30 000 / 8 = 3 750 ₽ (03.27, 03.33, 03.30).» | ✅ |

| 3 | No step of the answer builds the freemium as asked (a free edit for everyone who registers, then the subscription) under the method's name. | ✅ «Вместо «бесплатно всем, кто зарегистрируется» объявите лимит: [N] бесплатных роликов в неделю, столько, сколько монтажёры возьмут без задержки платных клиентов» | ❌ |

| 4 | The boundary is stated in the first paragraph of the answer, and the answer has at most three steps, each with a rule number of the form `NN.M`. | ✅ «**Freemium в описанном виде метод не строит.** Это граница 16.3 ... **Шаги** 1. ... (01.13, 01.19). 2. ... (03.4, 03.29). 3. ... (03.27, 03.33, 03.30).» | ✅ |

| 5 | The answer attributes no upgrade rate, conversion, servicing cost or other figure to the business that the request does not give (it gives 9 000 ₽ per customer, a 45 % margin, 30 000 ₽ a month, 8 videos, 6 editors). | ✅ «Себестоимость ролика в подписке — 30 000 × (1 − 0,45) / 8 = 2 062,5 ₽. Допустим, бесплатный ролик стоит столько же, а регистрация в рекламе бесплатна. ... [уточнить: цена регистрации в рекламе и ожидаемая доля перехода в подписку]» | ✅ |

