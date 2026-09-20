# Улов фазы 1 — ACQ Advertising Handbook (2025) (ярус 2), тип E: глоссарий

Группа `tier2-advertising`, слаг `advertising`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **39** (экстрактор вернул 39, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `acq-advertising-handbook.md` | 1–2657 | 4 | 39 |

## Как собран файл

Экстрактор E (Glossary) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-advertising.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-advertising-E.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: E-advertising-001
  type: term
  name: >-
    Ad Kaleidoscope
  statement: >-
    The Ad Kaleidoscope is the author's tool for permuting an ad that already won into many new variations rather than inventing ads from scratch.
  definition: >-
    The Ad Kaleidoscope permutes winning ads: it tweaks stuff that already worked, takes old winners and makes new ones, the way turning a kaleidoscope shows a hundred obviously different versions of the same thing.
  why: >-
    It harnesses power law: 80% of advertising results come from 20% of winners, so putting 80% of the effort into permutations of proven ads produces more winners than starting over each time.
  not_to_confuse_with: >-
    Making brand new ads; the Kaleidoscope only turns existing winners into more winners, and the new-ideas hunt is the other 20% of the effort.
  anchor: >-
    The Ad Kaleidoscope  _permutes winning ads_. In other words, it tweaks stuff that already worked. It takes old winners and makes new ones.
  source: >-
    acq-advertising-handbook.md, Part I What The Ad Kaleidoscope Is, line 209
  confirmations: 3
  authors_caveat: >-
    The process only works if you have already made ads and already have at least one winner (line 273).
  anchor_at: "acq-advertising-handbook.md:209"
- id: E-advertising-002
  type: term
  name: >-
    More, better, new
  statement: >-
    "More, better, new" is the author's growth strategy, and the Ad Kaleidoscope is that strategy applied to advertising.
  definition: >-
    The Ad Kaleidoscope puts advertising-specific action items on all three growth elements: it puts out more volume, makes that volume better, and generates new winners.
  anchor: >-
    The Ad Kaleidoscope is “more, better, new” applied to advertising. It works so well because it puts advertising-specific action items on all three growth elements.
  source: >-
    acq-advertising-handbook.md, Part I Kaleidoscope Ads, line 156
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:156"
- id: E-advertising-003
  type: term
  name: >-
    Power law in advertising (the Pareto Principle)
  statement: >-
    Power law in advertising means 80% of results come from 20% of the ads, which is why effort is concentrated on the winners.
  definition: >-
    Using the fact that 80% of advertising results come from 20% of winners, and only 20% of the results come from 80% of your effort.
  why: >-
    If you could make 100% of your ads like the 20% that get 80% of the results, you would get 5x the output.
  anchor: >-
    It all happens because the Ad Kaleidoscope harnesses power law. Aka - the Pareto Principle. In other words, using the fact that 80% of advertising results come from 20% of winners.
  source: >-
    acq-advertising-handbook.md, Part I Kaleidoscope Ads, line 158
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:158"
- id: E-advertising-004
  type: term
  name: >-
    Winner
  statement: >-
    A winner is an ad that outperforms the rest of your ads and therefore becomes the raw material for permutations.
  definition: >-
    Ads that outperform: your top 20%, your top 10%, top 5%, etc.
  why: >-
    The more ads you make the more winners you have to choose from, and that is what gives huge output.
  anchor: >-
    **Identify Winners:**  Look for ads that outperform. Your top 20%, your top 10%, top 5%, etc.
  source: >-
    acq-advertising-handbook.md, Part I How To Use The Ad Kaleidoscope, line 279
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:279"
- id: E-advertising-005
  type: term
  name: >-
    New (new to the viewer)
  statement: >-
    In this method "new" means new to the viewer, not newly invented by the advertiser.
  definition: >-
    New does not mean start from zero; new means new to the viewer, and consumers have a far lower threshold of new than the advertiser does.
  why: >-
    A permutation is new enough to keep results without fatiguing the audience, while the advertiser tires of an ad long before prospects ever see it.
  not_to_confuse_with: >-
    Starting from zero; a variation of a winner is already new in the only sense that matters.
  anchor: >-
    New does not mean “start from zero”. New means new to the viewer.
  source: >-
    acq-advertising-handbook.md, Part I What The Ad Kaleidoscope Is, line 235
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:235"
- id: E-advertising-006
  type: term
  name: >-
    Remix
  statement: >-
    A remix is a post-production variation of a winning ad: the same raw footage with the edits varied.
  definition: >-
    Your first run through the kaleidoscope: the same raw footage of your previous winners with varied edits, special effects and software, all the things you do after you film an ad.
  why: >-
    Remixes are the fastest variations to make, so they keep ads performing and buy time to do the remakes.
  not_to_confuse_with: >-
    Remakes, which change real-world variables and require recording again; remixes change only digital ones.
  anchor: >-
    **Remix Winners:**  Your first run through the kaleidoscope, you’ll use the same raw footage of your previous winners, but vary the edits.
  source: >-
    acq-advertising-handbook.md, Part I How To Use The Ad Kaleidoscope, line 283
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:283"
- id: E-advertising-007
  type: term
  name: >-
    Remake
  statement: >-
    A remake is a re-recorded version of a winning ad that keeps the winning script and changes the real-world components.
  definition: >-
    Remakes happen during recording: new ads made with basically the same winning script, changing the real world components of the ad rather than the digital ones.
  why: >-
    Real-world changes take longer to do, but the ads they produce can keep you fed for months and in some cases years.
  not_to_confuse_with: >-
    Remixes, which are done on a computer from existing footage; a remake means you actually need to record again.
  anchor: >-
    Remakes happen  _during recording_. This means we're actually changing the real world components of the ad.
  source: >-
    acq-advertising-handbook.md, Part I Remaking Winners, line 418
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:418"
- id: E-advertising-008
  type: term
  name: >-
    Fatigue and shelf life
  statement: >-
    An ad's shelf life is how long it keeps performing before the audience tires of it, and variations that look more like the original fatigue sooner.
  definition: >-
    Remixes tend to fatigue faster than remakes because they tend to look more similar, which is both good (the original worked) and bad (they will not have the same shelf life as more differentiated ads).
  anchor: >-
    Beyond that though, remixes tend to fatigue faster than remakes. Main reason—they tend to look more similar, which is both good and bad.
  source: >-
    acq-advertising-handbook.md, Part I Remixing Winners, line 402
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:402"
- id: E-advertising-009
  type: term
  name: >-
    Blackbook
  statement: >-
    The Blackbook is the author's own working list of ad frameworks he consults every time he makes ads.
  definition: >-
    The list of the 20 best ad frameworks of all time, demonstrated across four businesses, that the author refers to whenever he makes ads today.
  anchor: >-
    When I called this a Blackbook, I meant it. I refer to this list whenever I make ads today. Period.
  source: >-
    acq-advertising-handbook.md, Part II My Ads Blackbook intro, line 515
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:515"
- id: E-advertising-010
  type: term
  name: >-
    Visual Hook
  statement: >-
    The Visual Hook is the first three seconds of motion and design that stop the scroll, described separately from the words of the ad.
  definition: >-
    A description of the first three seconds of motion and design that stopped the scroll.
  anchor: >-
    **Visual Hook:**  A description of the first three seconds of motion and design that stopped the scroll.
  source: >-
    acq-advertising-handbook.md, Part II What You'll See for Every Winning Ad Framework, line 540
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:540"
- id: E-advertising-011
  type: term
  name: >-
    All-caps annotations inside the ad copy
  statement: >-
    Inside the transcribed ad copy the author marks what each line is doing with an all-caps tag such as (HOOK), (CALL OUT), (DREAM OUTCOME), (PROOF) or (CTA).
  definition: >-
    The exact words from the ad, with the author breaking down what is happening as it is happening, done in all caps inside the copy.
  why: >-
    The author finds it more useful to annotate inside the copy than to break the ad down separately.
  anchor: >-
    **Ad Copy:**  The exact words from the ad. I also include within the copy me breaking down what’s happening as it’s happening (I DO THESE IN ALL CAPS).
  source: >-
    acq-advertising-handbook.md, Part II What You'll See for Every Winning Ad Framework, line 541
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:541"
- id: E-advertising-012
  type: term
  name: >-
    Hook → Meat → CTA
  statement: >-
    Every ad in this handbook is laid out in three parts: the Hook, the Meat (also labelled Meat/Offer), and the CTA.
  definition: >-
    An ad is a hook at the front, a meat section in the middle, and a CTA at the end; swapping one part while keeping the others is what makes a variation.
  anchor: >-
    The right rectangle has "Hook 1" on the left, "Meat 2" in the middle, and "CTA 1" on the right.
  source: >-
    acq-advertising-handbook.md, Part I Remixing Winners, line 394
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:394"
- id: E-advertising-013
  type: term
  name: >-
    Meat (ad meat)
  statement: >-
    The meat is the middle section of an ad, the body between the hook and the CTA, and it can be swapped under a winning hook.
  definition: >-
    The different middle section you splice in; when you find your best performer you pair the winning hook with a different ad meat you have already recorded.
  anchor: >-
    **Same Hook. New Meat:**  When you find your best performer, pair the winning hook with a different “ad meat” you’ve already recorded.
  source: >-
    acq-advertising-handbook.md, Part I Remixing Winners, line 392
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:392"
- id: E-advertising-014
  type: term
  name: >-
    Anti-proof
  statement: >-
    Anti-proof is a circumstance shown in the ad that should have made the result impossible, stacked to build curiosity before the payoff.
  definition: >-
    The negatives of the situation stacked on top of the open loop until it snaps closed with the proof; each objection you raise about your own setting is anti-proof that keeps curiosity piqued.
  why: >-
    Showing the circumstances opposite to what you would expect eliminates the implied objections about why the thing would not work for the prospect.
  anchor: >-
    Then, it keeps expanding on this open loop by stacking “anti-proof” of the situation until it finally snaps the loop closed or “pays off” the viewer at the very end with the stack of $500 bills (signed contracts).
  source: >-
    acq-advertising-handbook.md, Section I Ad Framework #1 Personal Testimonial/Origin Story, line 594
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:594"
- id: E-advertising-015
  type: term
  name: >-
    Open loop
  statement: >-
    An open loop is unresolved curiosity deliberately built into the ad and closed only by the payoff or by the prospect taking the next step.
  definition: >-
    The ad functions like one gigantic open loop: the entire ad builds mystery and only the ending snaps the loop closed or pays the viewer off.
  anchor: >-
    This ad framework functions like one gigantic open loop. The entire ad builds mystery.
  source: >-
    acq-advertising-handbook.md, Section I Ad Framework #1 Personal Testimonial/Origin Story, line 592
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:592"
- id: E-advertising-016
  type: term
  name: >-
    Daisy chain of open loops
  statement: >-
    A daisy chain of open loops is several unresolved curiosities linked one after another in the same ad, all closable only by taking the next step.
  definition: >-
    The entire ad is a daisy chain of open loops with only one action to close them; in the example the chain runs banana → the money spent on the event → my birthday → giving a secret away.
  anchor: >-
    The entire ad is a daisy chain of open loops with only one action to close them—taking the next step.
  source: >-
    acq-advertising-handbook.md, Section IV Ad Framework #1 Flying Prop, line 2065
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2065"
- id: E-advertising-017
  type: term
  name: >-
    Damaging admission
  statement: >-
    A damaging admission is an honest negative the advertiser states about his own offer or setting.
  definition: >-
    A brief, honest disclaimer inside the ad, such as "It's not easy, but it's completely worth it".
  why: >-
    The damaging admission boosts credibility and decreases skepticism.
  anchor: >-
    Ex: “It’s not easy, but it’s completely worth it”. The damaging admission boosts credibility and decreases skepticism.
  source: >-
    acq-advertising-handbook.md, Section I Ad Framework #3 Emotional Avatar Testimonial, line 848
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:848"
- id: E-advertising-018
  type: term
  name: >-
    Narrative rhythm
  statement: >-
    The narrative rhythm is the fixed order of beats a testimonial ad follows from personal stakes through to the CTA.
  definition: >-
    PERSONAL STAKES → PERSONAL PAIN → PROFESSIONAL PAIN → TURNING POINT → WORK → PROFESSIONAL GOOD → PERSONAL GOOD → ADDRESS SKEPTICISM → REASON WHY → CTA.
  anchor: >-
    **Remember the narrative rhythm:**  PERSONAL STAKES → PERSONAL PAIN → PROFESSIONAL PAIN → TURNING POINT → WORK → PROFESSIONAL GOOD → PERSONAL GOOD → ADDRESS SKEPTICISM → REASON WHY→ CTA.
  source: >-
    acq-advertising-handbook.md, Section I Ad Framework #3 Emotional Avatar Testimonial, line 864
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:864"
- id: E-advertising-019
  type: term
  name: >-
    Genre of customer vs. the exact customer you want
  statement: >-
    The genre of customer is anyone in the category; the exact customer you want is the narrower profile you actually want to buy, and an ad can be aimed at either.
  definition: >-
    Ads that attract your genre of customer (any gym owner) as opposed to the exact customer you want (advanced gym owner); the way to get the second is to talk about the things those customers care about, using language only the upper echelon would understand.
  why: >-
    Talking to the advanced customer mostly gets you the upper market and the smaller market too, but only talking to a beginner never gets the advanced one.
  not_to_confuse_with: >-
    Targeting a whole industry or niche; the genre is the industry, the exact customer is the tier inside it.
  anchor: >-
    This style also taught me to make ads that don’t just attract your  _genre_  of customer (any gym owner), but the  _exact customer you want_  (advanced gym owner).
  source: >-
    acq-advertising-handbook.md, Section I Ad Framework #5 Long Term Result, line 953
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:953"
- id: E-advertising-020
  type: term
  name: >-
    Fast Win and Big Win
  statement: >-
    The Fast Win is the early result a customer got quickly; the Big Win is where they ended up, and a proof ad shows both.
  definition: >-
    Fast Win: "Within three months we tripled revenue." Big Win: "Today we clear $83k/month with <2 % churn." Two tiers show both quick payoff and long-term climb.
  anchor: >-
    **Show two wins—the Fast Win and the Big Win.**  Ex:  **Fast Win:**  “Within three months we tripled revenue.”  **Big Win:**  “Today we clear $83k/month with <2 % churn.”
  source: >-
    acq-advertising-handbook.md, Section I Ad Framework #5 Long Term Result, line 1020
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1020"
- id: E-advertising-021
  type: term
  name: >-
    ADucational (aducational)
  statement: >-
    An ADucational ad is an ad shot as a lesson, typically the speaker teaching in front of a whiteboard, so that education does the selling.
  definition: >-
    Man in front of whiteboard = educational = value; an educational setting works better with more complex products, and these ad types both build brand and drive sales.
  why: >-
    If you are brand new these work great because you will be judged on the quality of the information, not a pre-existing brand.
  anchor: >-
    It's a classic ADucational framework. You see these a lot, but few do them well. It works especially well with more advanced/complex products or services.
  source: >-
    acq-advertising-handbook.md, Section II Ad Framework #2 New vs. Old, line 1184
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:1184"
- id: E-advertising-022
  type: term
  name: >-
    Marketing and sales
  statement: >-
    Marketing and sales are the same job in different media, one to many and one to one, and both aim to educate the prospect into a decision.
  definition: >-
    Marketing and sales have the same objective, they simply operate in different media (one to one vs. one to many); the goal is to educate the prospect enough to make a decision.
  anchor: >-
    Marketing and sales have the same objective, they simply operate in different media (one to one vs. one to many). The goal is to educate the prospect enough to make a decision.
  source: >-
    acq-advertising-handbook.md, Section II Ad Framework #2 New vs. Old, line 1186
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1186"
- id: E-advertising-023
  type: term
  name: >-
    Specificity
  statement: >-
    Specificity means describing the prospect's problem in such narrow detail that he concludes you are an insider in his world.
  definition: >-
    You demonstrate your expertise by how specific or relevant you can describe the problem: a problem so specific that someone hears it and says "he must be an insider to know this" or "I feel like he's describing my life right now".
  why: >-
    It is what the author names as the thing that differentiates his copy from other people's, and each added specific detail keeps building pressure on the prospect.
  anchor: >-
    You demonstrate your expertise by how specific or relevant you can describe the problem.
  source: >-
    acq-advertising-handbook.md, Section II Ad Framework #3 Why You Will Never, line 1292
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:1292"
- id: E-advertising-024
  type: term
  name: >-
    North star metric
  statement: >-
    A north star metric is a single number about the prospect's business that predicts his pain and his ceiling, used to organise the whole ad.
  definition: >-
    A metric the advertiser creates and then uses to predict the prospect's pain point; it can be anything as long as it is predictive, the way neck and wrist thickness predict body fat.
  anchor: >-
    In this framework, I create a “north star” metric. Then I predict their pain point based on this metric (it can be anything as long as it’s predictive).
  source: >-
    acq-advertising-handbook.md, Section II Ad Framework #4 The "North Star", line 1388
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1388"
- id: E-advertising-025
  type: term
  name: >-
    Reverse royalty model
  statement: >-
    The reverse royalty model is the author's name for billing per result instead of a monthly retainer.
  definition: >-
    A model that reverses the retainer: billing per result means value always exceeds price, so profit scales without hitting the old plateaus; in the ALAN case, charging for shows rather than for service.
  why: >-
    The name had to be non-obvious: "Pay Per Show" was too obvious and killed the curiosity, so the mechanism was named "reverse royalty" instead.
  not_to_confuse_with: >-
    A retainer model, where the value delivered drifts below the price charged and the client cancels.
  anchor: >-
    but the good news is there is a model that reverses it and it's not a retainer model. It's called the reverse royalty model.
  source: >-
    acq-advertising-handbook.md, Section II Ad Framework #3 Why You Will Never, line 1346
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:1346"
- id: E-advertising-026
  type: term
  name: >-
    An ad for your lead magnet
  statement: >-
    An ad for the lead magnet sells only the next step, leaving the selling to the page and the funnel behind it.
  definition: >-
    An ad for your lead magnet more than an ad to sell: it sells the next step, nothing more, and relies on additional information existing further in the funnel and conversion process.
  applies_when: >-
    Top of funnel, where short ads can be produced in volume and the page or video sales letter closes.
  anchor: >-
    Think of this as an ad for your lead magnet more than an ad to sell. It sells the next step. Nothing more.
  source: >-
    acq-advertising-handbook.md, Section II Ad Framework #5 No BS Selfie, line 1492
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1492"
- id: E-advertising-027
  type: term
  name: >-
    Trend ads
  statement: >-
    Trend ads borrow whatever video format is currently popular in organic feeds and put the offer inside it.
  definition: >-
    Trend ads capitalize on current popular video formats; the example emerged when podcast clips filled the feed, so the ad was made as a podcast clip.
  why: >-
    Organic is always ahead of paid ads because of the volume and speed of testing for creators, so today's organic shows where ads will be in six to 12 months.
  not_to_confuse_with: >-
    The particular format used in the example; the lesson is not that it was a podcast, it is that it was a popular video format at the time.
  anchor: >-
    Trend ads capitalize on current popular video formats. The example I show emerged when podcast clips were my entire feed.
  source: >-
    acq-advertising-handbook.md, Section III Ad Framework #1 Trending Format, line 1599
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1599"
- id: E-advertising-028
  type: term
  name: >-
    Stack and price drop (value anchor)
  statement: >-
    A stack anchors the offer against a high price and the price drop then lowers it to the real one, usually free.
  definition: >-
    An offer-centric ad with two stacks that anchor high then price drop: the hook anchors what someone would pay for the dream outcome, and the second stack anchors what people normally charge for the thing you are giving away.
  why: >-
    Free still has costs, so you still have to make free valuable; the descending questions set an initial value in the viewer's mind and make free feel like an unexpected windfall instead of a marketing cliché.
  anchor: >-
    This is an offer-centric ad. It has two “stacks” that anchor high then “price drop”.
  source: >-
    acq-advertising-handbook.md, Section III Ad Framework #2 Value Anchor, line 1684
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:1684"
- id: E-advertising-029
  type: term
  name: >-
    Better than free
  statement: >-
    Better than free means adding a variable reward on top of a free offer so the prospect risks nothing and can still gain something.
  definition: >-
    A variable reward added to a free offer: not only does it cost them nothing, they could get something too, for the top performers, a random selection, or everyone.
  anchor: >-
    Then, we add a variable reward in making this “better than free” because not only does it cost them nothing, they could get something too.
  source: >-
    acq-advertising-handbook.md, Section III Ad Framework #2 Value Anchor, line 1688
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1688"
- id: E-advertising-030
  type: term
  name: >-
    Reason why
  statement: >-
    The reason why is the stated motive behind an offer, a bonus or a limited intake, given so the prospect believes it is genuine.
  definition: >-
    A motive behind a bonus, such as "It's my birthday, so I'm giving an insane bonus to the first 100 clients"; whatever reason you choose, make it believable.
  why: >-
    A motive makes the bonus feel more authentic and by extension increases urgency, and prospects will believe you would do something big and crazy if you have a big and crazy reason.
  anchor: >-
    A motive behind a bonus makes the bonus feel more authentic, and by extension increases urgency.
  source: >-
    acq-advertising-handbook.md, Section III Ad Framework #3 Bribe, line 1832
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:1832"
- id: E-advertising-031
  type: term
  name: >-
    Investment as a proxy for value (approximation of value)
  statement: >-
    When you cannot say what the thing is without killing the curiosity, you state what it cost you to make and let that stand in for its worth to the prospect.
  definition: >-
    Talking about your investment — time invested, money spent, relationship capital used, prototypes, years — as a proxy for the prospect's potential benefit, which approximates their value.
  why: >-
    Make it a big deal to you, so it is a big deal to them; if you can show receipts that you really spent it, it dramatically increases how much they believe the value.
  anchor: >-
    If you can’t tell someone  _exactly_  what something is (to keep curiosity), then you talk more about your investment as a proxy for their potential benefit.
  source: >-
    acq-advertising-handbook.md, Section IV Ad Framework #2 Bribe, line 2188
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:2188"
- id: E-advertising-032
  type: term
  name: >-
    Range of values ("more than a gift card, less than a Tesla")
  statement: >-
    Instead of naming an undisclosed gift, you bracket it between one low-value and one high-value known item and let imagination fill the gap.
  definition: >-
    Give a range of values between two known items: one low-value and one high-value, then say that someone, some group, or everyone will get this prize.
  why: >-
    People automatically abstract what they are going to get towards the bigger thing, and you are not going to beat anyone's imagination.
  anchor: >-
    Give a range of values between two known items: one low-value and one high-value.
  source: >-
    acq-advertising-handbook.md, Section IV Ad Framework #2 Bribe, line 2200
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2200"
- id: E-advertising-033
  type: term
  name: >-
    Good ads
  statement: >-
    A good ad does exactly two things: it gets attention and it gets action.
  definition: >-
    Good ads do two things: get the prospect's attention → get the prospect to take action; so one part of the ad gets attention and another part increases the benefit and decreases the cost of taking action.
  not_to_confuse_with: >-
    Fancy or polished production; ads do not need to be fancy, they need to get people to click.
  anchor: >-
    **Good ads do two things:**  get the prospect’s attention→get the prospect to take action.
  source: >-
    acq-advertising-handbook.md, Section IV Ad Framework #3 The Rumors Are True, line 2228
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2228"
- id: E-advertising-034
  type: term
  name: >-
    Non-verbal CTA (visual CTA)
  statement: >-
    A visual CTA is a next step shown on screen rather than spoken, required whenever the ad itself has no narration.
  definition: >-
    A CTA that works without narration or speaking: the end screen is the CTA, the ad shows "this could be you" and the button tells them what to do next.
  applies_when: >-
    Non-verbal ads, and as an experiment on remixes.
  anchor: >-
    Non-verbal ads need non-verbal CTAs. For this type of ad, there are no words, so make sure you add a visual CTA that works without narration/speaking.
  source: >-
    acq-advertising-handbook.md, Section I Ad Framework #4 Show Don't Tell, line 925
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:925"
- id: E-advertising-035
  type: term
  name: >-
    Scarcity
  statement: >-
    Scarcity here means stating the true limits of what you can deliver, which raises demand by cutting perceived supply.
  definition: >-
    Explaining the true and real limitations of your product or service — limited hours in a day, limited number of people you can deliver, limited inventory — which increases demand by cutting perceived supply.
  not_to_confuse_with: >-
    Invented limits; the limitation stated is the true and real one you own up to.
  anchor: >-
    Doing this increases demand by cutting perceived supply. Aka—creating scarcity.
  source: >-
    acq-advertising-handbook.md, Section IV Ad Framework #5 Data Stack, line 2442
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2442"
- id: E-advertising-036
  type: term
  name: >-
    Must-haves and nice-to-haves
  statement: >-
    In the ad checklist each of the four buckets is split into the author's must-haves and nice-to-haves.
  definition: >-
    The author's own division inside each checklist bucket (visual, verbal delivery, script, CTA), which correspond roughly to what they see, what you say, what they get, how to get it.
  authors_caveat: >-
    You can make ads without some of his must-haves; he just does not.
  anchor: >-
    Within each bucket, I divide them into my own division of “must-haves” and “nice-to-haves”.
  source: >-
    acq-advertising-handbook.md, Part III Best Ad Framework Checklist, line 2550
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2550"
- id: E-advertising-037
  type: term
  name: >-
    Value equation questions
  statement: >-
    The value-equation questions are the yes-prompts in an ad that hit dream outcome, speed, ease and proof.
  definition: >-
    Three to four "Yes" prompts that hit dream outcome, speed, ease, and proof, each line three to five seconds max, with the last one a CTA.
  anchor: >-
    **Map the value-equation questions.**  Write three to four “Yes” prompts that hit  _dream outcome, speed, ease, and proof._
  source: >-
    acq-advertising-handbook.md, Section I Ad Framework #2 Prop Comedy, line 720
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:720"
- id: E-advertising-038
  type: term
  name: >-
    Call out
  statement: >-
    A call out is the opening line that names the exact avatar so only the right prospect keeps watching.
  definition: >-
    Calling out your exact avatar in five seconds or less, such as "Local lead-gen agency owners doing about $15k a month—listen up"; the label filters for only qualified prospects.
  anchor: >-
    **Film in an educational setting and call out your exact avatar in ≤ five seconds.**  Ex: “Local lead-gen agency owners doing about $15k a month—listen up.”
  source: >-
    acq-advertising-handbook.md, Section II Ad Framework #2 New vs. Old, line 1250
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:1250"
- id: E-advertising-039
  type: term
  name: >-
    Proof (proximity of proof)
  statement: >-
    Proof is measured by how closely the prospect can approximate it to his own situation, not by how impressive it is.
  definition: >-
    The closer a prospect can approximate the proof to their situation, the lower the risk, and by extension, the more compelling it is; someone who looks like them, down the street, with a line out the door beats a stranger in another country.
  why: >-
    The more the ad shows viewers' own dream outcome, the lower the perceived risk; proof works better than just about anything else for persuading people.
  anchor: >-
    In short, the closer a prospect can approximate the proof to their situation, the lower the risk, and by extension, the more compelling it is.
  source: >-
    acq-advertising-handbook.md, Section I Ad Framework #4 Show Don't Tell, line 878
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:878"
```
