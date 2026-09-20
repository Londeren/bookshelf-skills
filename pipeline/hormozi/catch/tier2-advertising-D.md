# Улов фазы 1 — ACQ Advertising Handbook (2025) (ярус 2), тип D: антипаттерны и границы

Группа `tier2-advertising`, слаг `advertising`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **45** (экстрактор вернул 45, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `acq-advertising-handbook.md` | 1–2657 | 4 | 45 |

## Как собран файл

Экстрактор D (Antipatterns and boundaries) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-advertising.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-advertising-D.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: D-advertising-001
  type: antipattern
  name: >-
    Making new ads instead of doubling down on the ones that work
  statement: >-
    Spending most of the advertising effort on producing brand-new ads while the ads that already win get little or no further work is the reason most advertisers struggle.
  why: >-
    80% of advertising results come from 20% of winners, so effort poured into unproven new creative buys a fraction of the return that permutations of a proven winner do.
  applies_when: >-
    Any advertiser who already has at least one winning ad.
  anchor: >-
    _they spend too much time making new ads and not nearly enough time doubling down on the ads that work._
  source: >-
    acq-advertising-handbook.md, Why People Struggle To Advertise And How To Fix It, line 91
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:91"
- id: D-advertising-002
  type: antipattern
  name: >-
    Retiring an ad because you are bored of it
  statement: >-
    Killing or replacing a working ad because the advertiser has grown tired of seeing it, rather than because its performance has dropped.
  why: >-
    The advertiser sees the ad a hundred times more often than the market does; the campaign is made for the prospects, not for the person who made it, and the ad should be run until it stops working.
  anchor: >-
    You will tire of your advertising before your prospects even know your name.
  source: >-
    acq-advertising-handbook.md, PART I: AD KALEIDOSCOPE (Henry Ford story), line 136
  confirmations: 2
  authors_caveat: >-
    The stopping rule is the ad's performance: hammer it until it dies, then rerun it with Kaleidoscope variations.
  anchor_at: "acq-advertising-handbook.md:136"
- id: D-advertising-003
  type: antipattern
  name: >-
    Reading "new" as "start from zero"
  statement: >-
    Treating "a new ad" as an ad built from scratch, when new only has to mean new to the viewer.
  why: >-
    Consumers have a far lower threshold of new than the advertiser does, so a variation of what already worked reads as new while keeping the thing that made it convert.
  anchor: >-
    New does not mean “start from zero”. New means new to the viewer. Like the Henry Ford story, consumers have a far lower threshold of “new” than you do.
  source: >-
    acq-advertising-handbook.md, What The Ad Kaleidoscope Is, line 235
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:235"
- id: D-advertising-004
  type: rule
  name: >-
    The Ad Kaleidoscope needs an existing winner
  statement: >-
    The Ad Kaleidoscope is not applied until at least one ad has already been run and won; it permutes winners and cannot create the first one.
  why: >-
    Ads that do not exist yet cannot be optimized.
  boundary: >-
    Only for advertisers who have already made and run ads and have at least a single winner. An advertiser with no winners uses the 20 ad frameworks of Part II instead.
  anchor: >-
    You can’t optimize ads that don’t exist yet. Duh. Don’t worry, I’ve got you covered there.
  source: >-
    acq-advertising-handbook.md, How To Use The Ad Kaleidoscope, line 273
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:273"
- id: D-advertising-005
  type: antipattern
  name: >-
    Retiring old winners when a new winner appears
  statement: >-
    Dropping the previous winning ads once a totally new idea produces a winner, instead of adding the new winner to the pool of ads being permuted.
  why: >-
    A new winner is yet another source of permutations, not a replacement for the ones already producing results.
  applies_when: >-
    Step 4 of the Kaleidoscope, when the 20% of effort spent on new ideas finally produces a winner.
  anchor: >-
    To be clear, this doesn’t mean you stop using your old winners
  source: >-
    acq-advertising-handbook.md, How To Use The Ad Kaleidoscope, line 300
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:300"
- id: D-advertising-006
  type: rule
  name: >-
    Remixes fatigue faster than remakes
  statement: >-
    Post-production remixes are the fastest variations to produce but have the shortest shelf life, so they are used to buy time rather than as the lasting supply of ads.
  why: >-
    Remixes look more similar to the original: good because the original worked, bad because they fatigue the audience faster than more differentiated ads.
  boundary: >-
    A remix keeps a winner alive only for a short stretch; keeping a winner performing for months or years takes remakes, which require recording again.
  anchor: >-
    Beyond that though, remixes tend to fatigue faster than remakes. Main reason—they tend to look more similar, which is both good and bad.
  source: >-
    acq-advertising-handbook.md, Remixing Winners, line 402
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:402"
- id: D-advertising-007
  type: antipattern
  name: >-
    Doing only remixes or only remakes
  statement: >-
    Running only post-production remixes, or waiting to re-film remakes before shipping anything, instead of running both tracks at the same time.
  why: >-
    Remixes go up fast and keep the ads performing while the slower remakes are produced; the author states both should be done simultaneously.
  anchor: >-
    To be clear though, you should be doing both simultaneously if you really want to advertise like a pro.
  source: >-
    acq-advertising-handbook.md, Remaking Winners, line 418
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:418"
- id: D-advertising-008
  type: antipattern
  name: >-
    Not doing it at all
  statement: >-
    Knowing the permutation process and not running it, which is what most advertisers do.
  why: >-
    The process is simple enough that the only simpler thing is not doing it, and not doing it produces the results most people get: none.
  anchor: >-
    It’s so simple, the only thing simpler is not doing it—which is what most people do
  source: >-
    acq-advertising-handbook.md, Remaking Winners / Next Steps, line 489
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:489"
- id: D-advertising-009
  type: antipattern
  name: >-
    "This ad won't work for my industry"
  statement: >-
    Dismissing an ad framework because the example is from another industry or business model (B2B, money-making, lawncare), instead of swapping the blocks for words that describe your own service, product and benefits.
  why: >-
    The structures work agnostic of industry; the test of having understood a framework is being able to turn it into a B2C, B2B, service, SaaS or product ad.
  anchor: >-
    Do not think “this won’t work for me” think “how can I make this work for me”.
  source: >-
    acq-advertising-handbook.md, PART II intro: My Ads Blackbook, line 519
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:519"
- id: D-advertising-010
  type: rule
  name: >-
    One ad should not try to do too much
  statement: >-
    A short creative is not asked to do the whole sale; its job is to get the right person to click with the right intent.
  why: >-
    Ads of this type do not try to do too much, which is what makes them clear and to the point.
  boundary: >-
    Stated for the fast prop-comedy style; the selling that the ad does not do has to happen somewhere else in the funnel.
  anchor: >-
    These types of ads don’t try to do too much. The point is to get the right person to click with the right intent.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #2: Prop Comedy, line 688
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:688"
- id: D-advertising-011
  type: antipattern
  name: >-
    Not filming in the avatar's own setting
  statement: >-
    Shooting the ad somewhere that does not look like the prospect's own world, when the opening frame could show the background, clothing and spokesperson the avatar recognises as "like them".
  why: >-
    The avatar has to see immediately that the ad is for them to be likely to respond; the author notes this is obvious and yet almost nobody does it.
  anchor: >-
    First scene already in the gym, because I’m targeting gym owners. This seems obvious, and yet so few people ever do it.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #2: Prop Comedy, Visual Hooks, line 706
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:706"
- id: D-advertising-012
  type: antipattern
  name: >-
    Music that is not royalty-free
  statement: >-
    Laying a track over the ad without checking it is royalty-free.
  why: >-
    The author reports learning this the hard way.
  applies_when: >-
    Any ad that layers music under the spoken lines.
  anchor: >-
    Choose a royalty-free track (found that out the hard way).
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #2: Prop Comedy, How Apply This Ad Framework, line 734
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:734"
- id: D-advertising-013
  type: antipattern
  name: >-
    Proof the prospect cannot approximate to their own situation
  statement: >-
    Using proof from someone who does not look like the prospect, far away, described rather than shown.
  why: >-
    The closer a prospect can approximate the proof to their own situation, the lower the perceived risk and the more compelling it is; distant, dissimilar, merely asserted proof is far less compelling than a similar person nearby with the result visible.
  anchor: >-
    someone who doesn’t look like them, in a different country, says they own a gym, and that it got full, is far less compelling than someone who looks like them, down the street, at their gym, with a line out the door they can see.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #4 Show Don’t Tell, line 878
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:878"
- id: D-advertising-014
  type: antipattern
  name: >-
    Making the ad fancy
  statement: >-
    Spending the effort on production polish rather than on getting people to click.
  why: >-
    Ads do not need to be fancy, they need to get people to click; the framework that took the author from broke to not broke was shot with what he had.
  anchor: >-
    Ads don’t need to be fancy. They need to get people to click.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #4 Show Don’t Tell, line 882
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:882"
- id: D-advertising-015
  type: antipattern
  name: >-
    Skipping the movement-in-unison tip
  statement: >-
    Passing over the instruction to show many people moving in unison, which the author flags as the tip people will skip.
  why: >-
    Lots of humans doing the same thing at the same time compels attention and stops the scroll far better than narration ever can.
  applies_when: >-
    Any visual hook where several people can be shown moving at once.
  anchor: >-
    This is a massive pro tip that people will skip over.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #4 Show Don’t Tell, How To Apply, line 913
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:913"
- id: D-advertising-016
  type: antipattern
  name: >-
    Proof that needs words to be understood
  statement: >-
    Relying on narration to explain what the proof footage means, instead of choosing proof clear enough to be read without words.
  why: >-
    If words are needed for people to know what they are looking at, the ad is less effective; non-verbal clips also tend to get more organic reach.
  anchor: >-
    If you have to use words for people to know what it means, you’ll have a less effective ad.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #4 Show Don’t Tell, How To Apply, line 915
  confirmations: 2
  authors_caveat: >-
    Not that a narrated version will not work, but that a wordless demonstration works that much better.
  anchor_at: "acq-advertising-handbook.md:915"
- id: D-advertising-017
  type: antipattern
  name: >-
    A spoken CTA on a wordless ad
  statement: >-
    Ending a non-verbal, show-don't-tell ad with a CTA that only works if someone is speaking or the sound is on.
  why: >-
    The ad has no words, so the next step has to be carried by a visual CTA; the footage says "this could be you" and the button has to say what to do next.
  boundary: >-
    Stated for the Show Don't Tell format specifically: non-verbal ads need non-verbal CTAs.
  anchor: >-
    Non-verbal ads need non-verbal CTAs. For this type of ad, there are no words, so make sure you add a visual CTA that works without narration/speaking.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #4 Show Don’t Tell, line 925
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:925"
- id: D-advertising-018
  type: antipattern
  name: >-
    Selling "get rich quick"
  statement: >-
    Advertising a fast, easy, small-timeline result, which sells but selects for poor beginner customers.
  why: >-
    Poor beginners will absolutely buy get-rich-quick, and then those are the only customers you have; the more advanced prospect is informed, knows it takes time and work, and only wants to see you are at their level.
  anchor: >-
    To be clear, poor beginner customers will absolutely buy “get rich quick” but then you’re only selling to poor beginners.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #5 Long Term Result, line 949
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:949"
- id: D-advertising-019
  type: antipattern
  name: >-
    Optimizing for CAC instead of LTV:CAC
  statement: >-
    Turning off a campaign because its cost per lead or cost per call is above the KPI, without looking at what those customers are worth.
  why: >-
    The author nearly killed his most successful campaign in aggregate on cost per call alone; that campaign's calls and customers cost more but paid more, stayed longer, got better results and referred friends.
  applies_when: >-
    Campaigns written for the advanced, higher-value avatar rather than for cheap leads.
  anchor: >-
    This campaign taught me an important lesson: don’t optimize for CAC, optimize for LTV:CAC.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #5 Long Term Result, line 951
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:951"
- id: D-advertising-020
  type: antipattern
  name: >-
    Being afraid to ostracize customers
  statement: >-
    Writing only to the beginner so as not to exclude anyone, which is what nearly everyone else does.
  why: >-
    Talking to the advanced customer mostly gets the smaller market as well, but only talking to a beginner never gets the advanced guy; because competitors avoid the advanced customer, that market is ripe for the taking.
  anchor: >-
    And besides, no one else will talk to the advanced customer because they’re afraid to ostracize any customers.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #5 Long Term Result, line 955
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:955"
- id: D-advertising-021
  type: rule
  name: >-
    When to use "Looking For 5 Avatars..."
  statement: >-
    The "I'm looking for # AVATARS who are looking to DREAM OUTCOME" ad is the one to start with when launching something new, starting paid ads, or first monetizing an audience.
  why: >-
    It is a classic direct response ad that works in any niche and is simple and brutally effective; the author almost always starts a launch with it.
  boundary: >-
    Positioned for the beginning of paid advertising or of monetizing an audience, and it needs a compelling reason why you are only taking a limited number.
  anchor: >-
    Use these if you are just starting to run paid ads or monetize your audience.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #1 Looking For 5 Avatars..., line 1072
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1072"
- id: D-advertising-022
  type: rule
  name: >-
    Where the ADucational / whiteboard setting fits
  statement: >-
    The educational setting (whiteboard, chalkboard, screen) is used for more advanced, complex, novel or higher-ticket offers rather than for simple ones.
  why: >-
    The teacher visual signals authority and value, and complex products need the prospect educated enough to make a decision.
  boundary: >-
    An educational setting works better with more complex products; it works whether you are brand new (you are judged on the quality of the information rather than an existing brand) or established.
  anchor: >-
    It works especially well with more advanced/complex products or services.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #2: New vs. Old, line 1184
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:1184"
- id: D-advertising-023
  type: antipattern
  name: >-
    Describing the prospect's problem in general terms
  statement: >-
    Naming the prospect's problem broadly instead of at the level of specific numbers and moments only an insider to that business would know.
  why: >-
    Expertise is demonstrated by how specifically the problem is described; a problem specific enough makes the prospect think the advertiser must be an insider or must be describing their life right now.
  applies_when: >-
    Pain- and problem-based ads such as "Why You Will Never" and the "North Star" framework.
  anchor: >-
    This is a personal favorite of mine because of how flexible it is. But remember… BE SPECIFIC.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #3: Why You Will Never, line 1292
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:1292"
- id: D-advertising-024
  type: antipattern
  name: >-
    An obvious name for the new mechanism
  statement: >-
    Naming the new mechanism after what it plainly is, which kills the curiosity that makes the prospect take the next step.
  why: >-
    The author renamed "Pay Per Show" to "reverse royalty" because the obvious name was too obvious and killed the curiosity.
  applies_when: >-
    Ads that introduce a new solution the prospect has to opt in to learn about.
  anchor: >-
    I had to come up with “reverse royalty” because “Pay Per Show” was too obvious and killed the curiosity.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #3: Why You Will Never, How To Apply, line 1372
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1372"
- id: D-advertising-025
  type: rule
  name: >-
    The No BS Selfie sells the next step, not the product
  statement: >-
    The short selfie ad is written to sell the lead magnet and the next step only, with the selling done later in the funnel.
  why: >-
    These ads rely on there being additional information in the funnel and conversion process; the solution is named without being explained and the lead magnet does the explaining.
  boundary: >-
    Top of funnel only, and only where a funnel with further information and a conversion process already exists behind it.
  anchor: >-
    These ads rely on having additional information in the funnel and conversion process. Think of this as an ad for your lead magnet more than an ad to sell.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #5: No BS Selfie, line 1492
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1492"
- id: D-advertising-026
  type: rule
  name: >-
    The wealth-flex setting works but costs you a brand
  statement: >-
    Letting a fancy car and house do the selling in the background is effective, and the author stopped doing it because of the brand it built.
  why: >-
    The setting has to establish credibility related to the thing you talk about; the author found he did not want that kind of brand, while stating the technique is effective.
  boundary: >-
    The author's own limit: he used it only for a brief stint in his career and stopped, though it works.
  anchor: >-
    Personally - I only did this for a brief stint in my career and I realized I didn’t want that kind of brand - so I stopped.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #5: No BS Selfie, How To Apply, line 1535
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1535"
- id: D-advertising-027
  type: antipattern
  name: >-
    Copying the surface of a trending format instead of the principle
  statement: >-
    Taking "make a podcast ad" as the lesson of a trend ad, when the lesson is that the ad used whatever video format was popular at that moment.
  why: >-
    The format that is popular now is the one that gets watched; the podcast was only the popular format at the time.
  boundary: >-
    Modeling the ad directly may work for a short period while short podcast clips are still in; modeling the larger concept (mine current organic formats and hooks) is what lasts.
  anchor: >-
    To be clear—the lesson to take from this ad isn’t that it was a podcast, it’s that it was a popular video format at the time.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #1: Trending Format, line 1601
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1601"
- id: D-advertising-028
  type: antipattern
  name: >-
    Ignoring organic content when making ads
  statement: >-
    Working as a pure ads person and not mining organic content for hooks and formats, which the author flags as the point most readers will miss.
  why: >-
    Organic is always ahead of paid because creators test at higher volume and speed; today's organic shows where ads will be in six to 12 months.
  anchor: >-
    If you want to see where ads will be in six to 12 months, just look at where organic is today.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #1: Trending Format, line 1603
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1603"
- id: D-advertising-029
  type: rule
  name: >-
    A directly modeled trend ad has a shelf life
  statement: >-
    An ad copied directly from a current trending format is expected to work only while that format is still in fashion.
  why: >-
    The format is what carries the attention, and formats go out of fashion.
  boundary: >-
    Direct modeling: short period only. The durable version is modeling the concept, taking the best current organic hooks into ads.
  anchor: >-
    This may work for a short period while short podcast clips are still “in”.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #1: Trending Format, line 1605
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1605"
- id: D-advertising-030
  type: rule
  name: >-
    The breakdown is written for the segment it was aimed at
  statement: >-
    The proof and speed claims in the Trending Format breakdown were written for prosumers; a different segment needs different content aligned with its own desires and expectations.
  why: >-
    What counts as a compelling number and a compelling promise is set by the segment being addressed.
  boundary: >-
    The author's explicit note that this ad was targeted at prosumers, and that the copy changes with the segment.
  anchor: >-
    this ad was targeted at prosumers. If you want to capture a different segment you’d say different stuff more aligned with their desires and expectations.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #1: Trending Format, How To Apply, line 1666
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1666"
- id: D-advertising-031
  type: antipattern
  name: >-
    Showing only the outsized outcomes
  statement: >-
    Stacking only the biggest results in an ad and leaving out the average and lower-tier ones.
  why: >-
    People want to know the big thing is possible, but most importantly want to understand what is likely; both the non-typical and the everyday outcome have to be in the ad.
  anchor: >-
    I always try to include both big and average outcomes in my ads.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #1: Trending Format, How To Apply, line 1668
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1668"
- id: D-advertising-032
  type: antipattern
  name: >-
    Assuming free sells itself
  statement: >-
    Offering something for free without first establishing what it is worth.
  why: >-
    Free still has costs, so the free thing still has to be made valuable; anchoring the value first makes free feel like an unexpected windfall instead of a marketing cliché.
  anchor: >-
    Free still has costs, this means that you still have to make free valuable.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #2: Value Anchor, How To Apply, line 1741
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1741"
- id: D-advertising-033
  type: antipattern
  name: >-
    Romanticizing random hits
  statement: >-
    Treating winning ads as lucky strikes rather than as the output of deliberate volume; the breakout winner here came out of a day of roughly 250 ads.
  why: >-
    Volume negates luck; the real winners are built by deliberate work and there is zero magic in it.
  anchor: >-
    People romanticize random hits, but volume negates luck. The real winners are built by deliberate work.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #3: Bribe, line 1769
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1769"
- id: D-advertising-034
  type: rule
  name: >-
    Some selling always has to happen
  statement: >-
    A short, proof-heavy ad does not remove the selling; it moves it onto the landing page and the video sales letter.
  why: >-
    The ad only has to earn the click; the page and the VSL then close.
  boundary: >-
    You can pack the selling into the ad or shift it to the page, but it cannot be skipped; the short-ad version presupposes a page that does the heavy lifting.
  anchor: >-
    To be clear—some selling always has to happen. But, you can pack it into the ad or shift it to the page.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #3: Bribe, line 1771
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1771"
- id: D-advertising-035
  type: antipattern
  name: >-
    Reinventing the wheel
  statement: >-
    Inventing fresh hooks and formats for each new campaign or niche instead of recycling proven ones across industries.
  why: >-
    Only amateurs reinvent the wheel; pros run proven playbooks and checklists and make up the rest with volume. The author reuses the same hook across a community software platform and a book launch.
  anchor: >-
    Only amateurs reinvent the wheel. Pros use proven playbooks and checklists and make up for the rest with volume.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #3: Bribe, line 1775
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:1775"
- id: D-advertising-036
  type: antipattern
  name: >-
    An unrealistic stated cash value
  statement: >-
    Putting a dollar figure on the free thing that is not realistic.
  why: >-
    Stating a cash value turns a vague lead magnet into a tangible benefit only if the figure is realistic; the market-price anchor is compelling because it is true.
  applies_when: >-
    Bribe and Value Anchor ads that price a free lead magnet.
  anchor: >-
    Stating cash value (if realistic!) turns a vague lead magnet into a tangible benefit.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #3: Bribe, How To Apply, line 1826
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1826"
- id: D-advertising-037
  type: antipattern
  name: >-
    Hiding the lower-tier outcomes
  statement: >-
    Avoiding the modest and below-average results in an ad, when leading with them beats the prospect's doubt to the punch.
  why: >-
    Prospects already know the outcome is desirable; what they doubt is that they can get it. They are already wondering about the average and below-average person, so telling them sets low, believable expectations and earns trust, while the big outcomes mentioned alongside still attract high achievers.
  anchor: >-
    So don't be afraid to talk about your lower tier outcomes—_beat people to the punch_. They're already doubtful.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #4: Underdog, line 1856
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1856"
- id: D-advertising-038
  type: rule
  name: >-
    Match the prize to the audience, not to its price tag
  statement: >-
    The giveaway is chosen for how big it is to that specific audience rather than for being cash, a car or a trip.
  why: >-
    Money, cars and vacations work better the broader the audience; for a narrow audience such as gym owners, re-outfitting their old gym with new equipment would be more compelling than a Cybertruck.
  boundary: >-
    The author states you do not need massive cash or a Cybertruck to make marketing more compelling, only that it helps; the broad-appeal prizes are for broad audiences.
  anchor: >-
    The broader the audience though, the more things like money, cars, and vacations work.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #5: Challenge With Prize, line 1932
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1932"
- id: D-advertising-039
  type: antipattern
  name: >-
    A deadline nobody believes
  statement: >-
    Attaching a time constraint to the giveaway that is not believable.
  why: >-
    A deadline only gets more people to act if it is believable; the same holds for the reason why you are taking limited clients, which the author says must be made believable and is best when true.
  anchor: >-
    A deadline gets more people to do it if it’s believable.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #5: Challenge With Prize, How To Apply, line 2007
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2007"
- id: D-advertising-040
  type: antipattern
  name: >-
    A complicated points system
  statement: >-
    Scoring a challenge or contest on a multi-part points system instead of one metric that both sides can track.
  why: >-
    One clear path beats a complicated points system; the entry condition should be a single metric that matches the business goal and is simple to track.
  anchor: >-
    One clear path beats a complicated points system.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #5: Challenge With Prize, How To Apply, line 2011
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2011"
- id: D-advertising-041
  type: antipattern
  name: >-
    Naming the undisclosed bonus
  statement: >-
    Spelling out exactly what the secret bonus is, instead of bounding it between a known low-value and a known high-value item and refusing details.
  why: >-
    Being vague lets each viewer's imagination fill in the perfect copy for them, and you are not going to beat anyone's imagination; the open loop can then only be closed by taking the action.
  applies_when: >-
    Curiosity- and open-loop ads built around an unrevealed bonus.
  anchor: >-
    Being vague allows people’s imaginations to fill in the perfect copy for each of them. And you’re not gonna beat anyone’s imagination.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #2: Bribe, How To Apply, line 2200
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2200"
- id: D-advertising-042
  type: antipattern
  name: >-
    Making the winner complicated
  statement: >-
    Dismissing a simple static permutation of a winning video as too plain, and complicating the ad instead.
  why: >-
    Simple does not mean ineffective; the static versions of the winning video ads were themselves winners, and winning is hard enough without adding complication.
  anchor: >-
    Winning is hard enough on its own. You don’t need to also make it complicated.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #3: The Rumors Are True, How To Apply, line 2284
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2284"
- id: D-advertising-043
  type: antipattern
  name: >-
    Promising fast results
  statement: >-
    Claiming the result will be fast, rather than framing how much time the prospect is saving or having compressed for them.
  why: >-
    The speed the prospect is being offered is the time it would otherwise take to solve the problem on their own; that reframe carries the speed without the promise.
  anchor: >-
    Reframe the amount of time it would take to solve this problem on their own without your product/services
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #4: You’re Being Lied To, How To Apply, line 2366
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2366"
- id: D-advertising-044
  type: antipattern
  name: >-
    Implying unlimited supply
  statement: >-
    Advertising as though you could serve any number of customers, instead of owning the real limits on hours, delivery capacity or inventory.
  why: >-
    Stating the true and real limitations increases demand by cutting perceived supply, which is what creates scarcity.
  authors_caveat: >-
    The limitation named has to be the true and real one.
  anchor: >-
    You can’t sell an unlimited amount (in all likelihood).
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #5: Data Stack, How To Apply, line 2442
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2442"
- id: D-advertising-045
  type: rule
  name: >-
    The must-haves are the author's own, not a law
  statement: >-
    The Best Ad Framework Checklist splits visual, verbal delivery, script and CTA into must-haves and nice-to-haves, and ads can be made without some of the must-haves.
  why: >-
    The author states these are his own divisions and his real-world checklist: he just does not make ads without them.
  boundary: >-
    The author's explicit limit on his own checklist, stated as a preference rather than a requirement.
  anchor: >-
    I want to be clear, you can make ads without some of my must-haves… I just don’t.
  source: >-
    acq-advertising-handbook.md, PART III, Best Ad Framework Checklist, line 2552
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2552"
```
