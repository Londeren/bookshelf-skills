# Улов фазы 1 — ACQ Advertising Handbook (2025) (ярус 2), тип B: правила и критерии

Группа `tier2-advertising`, слаг `advertising`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **155** (экстрактор вернул 155, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `acq-advertising-handbook.md` | 1–2657 | 4 | 155 |

## Как собран файл

Экстрактор B (Rules and criteria) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-advertising.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-advertising-B.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 0; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: B-advertising-001
  type: rule
  name: >-
    Run a winner until it stops working
  statement: >-
    A working ad keeps running until its performance dies, not until the person who made it is bored with it.
  why: >-
    You will tire of your advertising long before your prospects even know your name, because you see it every day and they have barely seen it once.
  applies_when: >-
    Any ad that is currently performing.
  anchor: >-
    And when an ad finally works, keep running it until it stops working—never until
  source: >-
    acq-advertising-handbook.md, PART I: AD KALEIDOSCOPE, line 136
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:136"
- id: B-advertising-002
  type: rule
  name: >-
    The Ad Kaleidoscope needs an existing winner
  statement: >-
    The Ad Kaleidoscope is started only once at least one ad has already been made and has won; it is never used to make the first ads.
  why: >-
    You cannot optimize ads that do not exist yet.
  applies_when: >-
    Before choosing between remixing and making new creative from scratch.
  anchor: >-
    works if you’ve already made ads. You can’t optimize ads that don’t exist yet.
  source: >-
    acq-advertising-handbook.md, PART I: AD KALEIDOSCOPE, How To Use The Ad Kaleidoscope, line 273
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:273"
- id: B-advertising-003
  type: rule
  name: >-
    One winner is enough to start
  statement: >-
    The moment a single ad wins, the Kaleidoscope is applied to it rather than waiting for a larger set of winners.
  anchor: >-
    _a single winner_, you can use the Ad Kaleidoscope.
  source: >-
    acq-advertising-handbook.md, PART I: AD KALEIDOSCOPE, How To Use The Ad Kaleidoscope, line 275
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:275"
- id: B-advertising-004
  type: rule
  name: >-
    Identify Winners
  statement: >-
    Winners are picked as the top-performing slice of everything run (top 20%, 10% or 5%), not by taste.
  why: >-
    The more ads you make, the more winners you have to choose from, and that is what gives the output.
  anchor: >-
    Look for ads that outperform. Your top 20%, your top 10%, top 5%, etc.
  source: >-
    acq-advertising-handbook.md, PART I: AD KALEIDOSCOPE, How To Use The Ad Kaleidoscope, line 279
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:279"
- id: B-advertising-005
  type: rule
  name: >-
    Remixes before remakes
  statement: >-
    Post-production variations of a winner are produced first, before any re-filming.
  why: >-
    They are the fastest to make, so they keep the ads performing and buy time for the slower remakes.
  anchor: >-
    You’ll make these post-production variations first because they’re the fastest to make.
  source: >-
    acq-advertising-handbook.md, PART I: AD KALEIDOSCOPE, How To Use The Ad Kaleidoscope, line 283
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:283"
- id: B-advertising-006
  type: rule
  name: >-
    Remake keeps the winning script
  statement: >-
    A remake re-films the same winning script and changes only real-world variables, so nothing that made the ad a winner is lost.
  why: >-
    The variation is significant while the script that converted stays intact, so the new version stays likely to convert.
  anchor: >-
    we make new ads with basically the same winning script. Think re-filming.
  source: >-
    acq-advertising-handbook.md, PART I: AD KALEIDOSCOPE, How To Use The Ad Kaleidoscope, line 285
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:285"
- id: B-advertising-007
  type: rule
  name: >-
    Try New Ideas
  statement: >-
    The remaining 20% of the time is spent testing totally new ideas, and permutations of the current winner keep running until a new winner emerges from them.
  why: >-
    A new winner does not retire the old ones, it only adds another winner to make more winners from.
  anchor: >-
    The remaining 20% of your time you spend testing totally new stuff.
  source: >-
    acq-advertising-handbook.md, PART I: AD KALEIDOSCOPE, How To Use The Ad Kaleidoscope, line 300
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:300"
- id: B-advertising-008
  type: rule
  name: >-
    New Speed
  statement: >-
    A speed remix runs the same spot at 1.1x to 1.2x and no faster than the point where the speaker's voice starts sounding weird.
  why: >-
    Faster and slower versions sometimes convert better, and even converting the same as a top performer makes them top performers.
  anchor: >-
    Just run it at 1.1 to 1.2x the speed (without making the voice of the person in the ad sound weird)
  source: >-
    acq-advertising-handbook.md, PART I: AD KALEIDOSCOPE, Remixing Winners, line 334
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:334"
- id: B-advertising-009
  type: rule
  name: >-
    New Format
  statement: >-
    A separate version of the ad is cut native to each placement on each platform.
  why: >-
    Native placements improve performance big time.
  anchor: >-
    Make different versions native to each ad placement on each platform.
  source: >-
    acq-advertising-handbook.md, PART I: AD KALEIDOSCOPE, Remixing Winners, line 380
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:380"
- id: B-advertising-010
  type: rule
  name: >-
    Effects go early
  statement: >-
    Added visual effects are placed in the opening of the ad, at the hook, rather than later in the spot.
  why: >-
    The hook is what most people will see first.
  anchor: >-
    The ones that will matter most are the ones you do earlier (the hook), since this is what most people will see first.
  source: >-
    acq-advertising-handbook.md, PART I: AD KALEIDOSCOPE, Remixing Winners, line 396
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:396"
- id: B-advertising-011
  type: rule
  name: >-
    Remix and remake at the same time
  statement: >-
    Remixes and remakes of a winner are produced simultaneously, not one style of variation alone.
  why: >-
    Remixes fatigue faster than remakes because they look more similar to the original, so they have a shorter shelf life; remakes can keep a winner performing for months or years.
  anchor: >-
    you should be doing both simultaneously if you really want to advertise like a pro.
  source: >-
    acq-advertising-handbook.md, PART I: AD KALEIDOSCOPE, Remaking Winners, line 418
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:418"
- id: B-advertising-012
  type: rule
  name: >-
    New Talent
  statement: >-
    Talent recorded for a remake looks like the people who buy the product, and matches the segment the ad is meant to bring in.
  why: >-
    This is a wildly underutilized variation style; matching the buyer's demographic brings more of that demographic.
  anchor: >-
    Ideally, you should find talent that looks like the people that buy your stuff.
  source: >-
    acq-advertising-handbook.md, PART I: AD KALEIDOSCOPE, Remaking Winners, line 467
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:467"
- id: B-advertising-013
  type: rule
  name: >-
    80/20 split of advertising effort
  statement: >-
    80% of ad-making effort goes into permutations of ads that already won and only 20% into ads built from scratch.
  why: >-
    80% of advertising results come from 20% of winners, so effort spent replicating proven ads produces more winners than starting from zero every time.
  anchor: >-
    80% of your energy goes into making Kaleidoscope variations, and the other 20% goes into a totally new ad
  source: >-
    acq-advertising-handbook.md, PART I: AD KALEIDOSCOPE, Next Steps, line 487
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:487"
- id: B-advertising-014
  type: rule
  name: >-
    Volume until the first winner
  statement: >-
    Before any winner exists, as many ads as possible are run until one wins, and only then does the Kaleidoscope start.
  why: >-
    Volume negates luck; the real winners are built by deliberate work, not by random hits.
  applies_when: >-
    Starting out, with no winning ad yet.
  anchor: >-
    When starting, run as many ads as you can until you find a winner.
  source: >-
    acq-advertising-handbook.md, PART I: AD KALEIDOSCOPE, Next Steps, line 487
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:487"
- id: B-advertising-015
  type: rule
  name: >-
    The model test for a borrowed framework
  statement: >-
    A framework is understood only when it can be turned into a B2C, B2B, service, SaaS or product ad; the blocks are replaced with words describing your own service, product and benefits.
  why: >-
    Objections that an ad belongs to another industry are wrong; the structure works agnostic of industry, only the blocks change.
  applies_when: >-
    Modeling any of the 20 ad frameworks for your own business.
  anchor: >-
    you should be able to turn every ad into a B2C, B2B, service, SaaS, or product ad.
  source: >-
    acq-advertising-handbook.md, PART II: MY ADS BLACKBOOK, line 519
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:519"
- id: B-advertising-016
  type: rule
  name: >-
    Anti-proof then payoff
  statement: >-
    An origin-story ad shows a row of circumstances that make the outcome look impossible and then shows an insane outcome that proves the thing works regardless of circumstance.
  why: >-
    It eliminates, inside the ad itself, every reason someone would say it would not work for them, and pays the loop off with a massive piece of proof.
  anchor: >-
    Show all of those negatives in a row. Then show an insane outcome to prove your thing works regardless of circumstance.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #1: Personal Testimonial/Origin Story, line 596
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:596"
- id: B-advertising-017
  type: rule
  name: >-
    Wild claim in the first five seconds
  statement: >-
    The ad opens within five seconds with the end result the prospect craves, stated short and with no details yet.
  anchor: >-
    Open with the end result your prospects crave
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #1: Personal Testimonial/Origin Story, line 654
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:654"
- id: B-advertising-018
  type: rule
  name: >-
    Film in an obviously wrong environment
  statement: >-
    The setting of the ad looks incompatible with the promise, and its flaws are named aloud.
  applies_when: >-
    An origin-story or anti-proof ad.
  anchor: >-
    Film in a setting that looks incompatible with the promise
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #1: Personal Testimonial/Origin Story, line 655
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:655"
- id: B-advertising-019
  type: rule
  name: >-
    The problems tour
  statement: >-
    The ad moves the camera and names out loud every objection prospects normally raise, each objection serving as anti-proof.
  why: >-
    Each objection voiced as anti-proof keeps curiosity piqued instead of leaving the objection unanswered in the viewer's head.
  anchor: >-
    Move the camera and rattle off every objection prospects normally raise
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #1: Personal Testimonial/Origin Story, line 656
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:656"
- id: B-advertising-020
  type: rule
  name: >-
    No resolution before the end
  statement: >-
    The open loop keeps taking on fresh negatives and is given no resolution until the payoff.
  anchor: >-
    Let curiosity build. Offer no resolution yet.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #1: Personal Testimonial/Origin Story, line 668
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:668"
- id: B-advertising-021
  type: rule
  name: >-
    Snap the loop closed with proof
  statement: >-
    The ad ends by putting irrefutable evidence in focus, tied to the wild claim it opened with, plus one plain sentence that connects them.
  anchor: >-
    End the tour by shoving irrefutable evidence into the focus
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #1: Personal Testimonial/Origin Story, line 670
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:670"
- id: B-advertising-022
  type: rule
  name: >-
    Takeaway tied to a limiting belief
  statement: >-
    The closing takeaway is tied to the prospect's own limiting belief before the invitation to the next step.
  anchor: >-
    Tie the lesson to the prospect’s own limiting belief
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #1: Personal Testimonial/Origin Story, line 672
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:672"
- id: B-advertising-023
  type: rule
  name: >-
    One job per ad
  statement: >-
    An ad does not try to do too much; its job is to get the right person to click with the right intent.
  anchor: >-
    The point is to get the right person to click with the right intent.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #2: Prop Comedy, line 688
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:688"
- id: B-advertising-024
  type: rule
  name: >-
    Similar Avatar
  statement: >-
    The background, clothing and spokesperson in the first frame read as like the target avatar, so the viewer sees immediately that the ad is for them.
  why: >-
    It increases the likelihood they respond; it seems obvious and yet few advertisers ever do it.
  anchor: >-
    Your avatar should immediately see the background, clothing, and spokesperson as “like them” to increase the likelihood they respond.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #2: Prop Comedy, line 706
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:706"
- id: B-advertising-025
  type: rule
  name: >-
    Three to five seconds per line, last line is the CTA
  statement: >-
    In a prop-comedy ad each spoken line runs three to five seconds at most and the last line is the CTA.
  applies_when: >-
    A fast prop-comedy ad built from three to four value-equation questions.
  anchor: >-
    Keep each line three to five seconds max. The last one should be a CTA.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #2: Prop Comedy, line 720
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:720"
- id: B-advertising-026
  type: rule
  name: >-
    One prop and one mini-setting per line
  statement: >-
    Each line of the ad gets its own prop and mini-setting, and the first setting is one the avatar recognizes.
  why: >-
    The recognizable first setting tells the avatar the ad is for them; where the prop cannot be matched to the line, it is made fun and interesting instead.
  anchor: >-
    Make sure the first setting is one your avatar recognizes so they know it’s for them.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #2: Prop Comedy, line 721
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:721"
- id: B-advertising-027
  type: rule
  name: >-
    Film each line separately
  statement: >-
    All lines are shot in order but as individual clips, with the talent centered and moving.
  anchor: >-
    Shoot all lines in order but as individual clips.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #2: Prop Comedy, line 722
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:722"
- id: B-advertising-028
  type: rule
  name: >-
    Whip-cuts between clips
  statement: >-
    Every clip ends on a fast pan and the next clip starts continuing that motion.
  why: >-
    The momentum drags viewers forward without missing a beat, which is decisive for the pace of the ad.
  anchor: >-
    Finish each clip with a fast pan; start the next clip continuing that motion.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #2: Prop Comedy, line 732
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:732"
- id: B-advertising-029
  type: rule
  name: >-
    Royalty-free music only
  statement: >-
    The music track laid under the ad is royalty-free.
  why: >-
    The author found that out the hard way.
  anchor: >-
    Choose a royalty-free track (found that out the hard way).
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #2: Prop Comedy, line 734
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:734"
- id: B-advertising-030
  type: rule
  name: >-
    Captions
  statement: >-
    Captions are huge and high-contrast and match the spoken line.
  anchor: >-
    Make captions in huge, high-contrast font to match the spoken line.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #2: Prop Comedy, line 734
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:734"
- id: B-advertising-031
  type: rule
  name: >-
    Freeze the CTA card for one second
  statement: >-
    The last CTA card is frozen on screen for one full second, with the spokesperson pointing at it.
  why: >-
    The viewer needs the time to read it and take action.
  anchor: >-
    Freeze-frame the last card for one full second so they have time to read it and take action.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #2: Prop Comedy, line 736
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:736"
- id: B-advertising-032
  type: rule
  name: >-
    Cut to the sad setting within half a second
  statement: >-
    A testimonial ad cuts within half a second to an empty, gloomy shot of the same setting, under a gentle emotional soundtrack.
  why: >-
    The visual contrast plus music sets the mood for hardship before any words are spoken.
  anchor: >-
    Cut within half a second to an empty, gloomy shot of the same setting
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #3: Emotional Avatar Testimonial, line 843
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:843"
- id: B-advertising-033
  type: rule
  name: >-
    Five to six rapid-fire pains
  statement: >-
    After the blunt opening pain statement the testimonial stacks five to six rapid-fire pains and stakes, each on its own jump-cut.
  why: >-
    The quick cuts keep viewers locked in while the pains accumulate.
  anchor: >-
    stack five-to-six rapid-fire pains and stakes.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #3: Emotional Avatar Testimonial, line 844
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:844"
- id: B-advertising-034
  type: rule
  name: >-
    Keep the work phase short
  statement: >-
    The part of the testimonial covering the work after the turning point stays short.
  why: >-
    The audience only needs to hear that there was work, enough to set realistic expectations.
  anchor: >-
    Keep this portion short; the audience only needs to hear that there’s work and to set realistic expectations
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #3: Emotional Avatar Testimonial, line 845
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:845"
- id: B-advertising-035
  type: rule
  name: >-
    Switch the music at the turning point
  statement: >-
    The soundtrack switches to upbeat exactly at the turning point of the story.
  anchor: >-
    Switch to upbeat music at the turning point in the ad.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #3: Emotional Avatar Testimonial, line 845
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:845"
- id: B-advertising-036
  type: rule
  name: >-
    Dream outcome with numbers and personal benefits
  statement: >-
    The dream outcome is described with hard numbers and with personal benefits, each positive matched to uplifting B-roll where footage exists.
  anchor: >-
    Describe/show the dream outcome with numbers and personal benefits.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #3: Emotional Avatar Testimonial, line 846
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:846"
- id: B-advertising-037
  type: rule
  name: >-
    Highlight the speed and ease
  statement: >-
    The ad names how fast and how easily the result arrived, in concrete terms.
  why: >-
    It tackles the too slow and too hard objection before it forms.
  anchor: >-
    This tackles the “too slow/too hard” objection before it forms.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #3: Emotional Avatar Testimonial, line 847
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:847"
- id: B-advertising-038
  type: rule
  name: >-
    Damaging admission
  statement: >-
    A brief, honest disclaimer about the difficulty is inserted before the call to action.
  why: >-
    The damaging admission boosts credibility and decreases skepticism.
  anchor: >-
    The damaging admission boosts credibility and decreases skepticism.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #3: Emotional Avatar Testimonial, line 848
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:848"
- id: B-advertising-039
  type: rule
  name: >-
    The customer speaks to camera
  statement: >-
    In a testimonial the customer addresses the camera directly when inviting the prospect.
  why: >-
    Prospects then feel the invitation is personal.
  anchor: >-
    Let the customer speak directly to camera so prospects feel the invitation is personal.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #3: Emotional Avatar Testimonial, line 860
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:860"
- id: B-advertising-040
  type: rule
  name: >-
    One clear verbal and visual next step
  statement: >-
    The ad ends on exactly one next step, said out loud and shown on screen, with a bold numeric hook and a button graphic.
  anchor: >-
    Use a bold numeric hook and a button graphic so the next step is clear.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #3: Emotional Avatar Testimonial, line 862
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:862"
- id: B-advertising-041
  type: rule
  name: >-
    Proof the prospect can approximate
  statement: >-
    Proof is chosen so the prospect can approximate it to their own situation: someone like them, nearby, in a setting they recognise, rather than a distant stranger.
  why: >-
    The closer a prospect can approximate the proof to their situation, the lower the risk and the more compelling it is.
  anchor: >-
    the closer a prospect can approximate the proof to their situation, the lower the risk, and by extension, the more compelling it is.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #4 Show Don’t Tell, line 878
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:878"
- id: B-advertising-042
  type: rule
  name: >-
    Ads do not need to be fancy
  statement: >-
    An ad is judged by whether it gets people to click, not by its production value.
  anchor: >-
    Ads don’t need to be fancy. They need to get people to click.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #4 Show Don’t Tell, line 882
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:882"
- id: B-advertising-043
  type: rule
  name: >-
    Show What You Tell
  statement: >-
    The ad shows the outcome happening instead of saying that it happened, filmed by current customers who match the target avatar.
  why: >-
    The more the ad shows viewers their own dream outcome, the lower the perceived risk.
  anchor: >-
    Ask current customers who match your target avatar to film their “dream outcome proof moment”.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #4 Show Don’t Tell, line 909
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:909"
- id: B-advertising-044
  type: rule
  name: >-
    Frame what they are looking at
  statement: >-
    The fewest possible words and numbers are overlaid in post production, in a high-contrast colour, to frame the visual immediately.
  why: >-
    We do not want the viewer to have to figure out what they are looking at.
  anchor: >-
    Use the fewest possible words and numbers to frame what they’re looking at immediately.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #4 Show Don’t Tell, line 911
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:911"
- id: B-advertising-045
  type: rule
  name: >-
    Many people moving, ideally in unison
  statement: >-
    Where possible the ad shows many people moving at once, and in unison if it can be arranged.
  why: >-
    Many people moving at once almost always draws attention, and people doing the same thing at the same time stops the scroll far better than narration.
  anchor: >-
    Get people to move in unison if possible.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #4 Show Don’t Tell, line 913
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:913"
- id: B-advertising-046
  type: rule
  name: >-
    Proof does the talking
  statement: >-
    The proof shown is clear enough that the ad needs no narration to be understood.
  why: >-
    If words are needed for people to know what it means the ad is less effective, and non-verbal clips also tend to get more organic reach.
  anchor: >-
    The proof should be so clear you don’t need to add narration (if possible).
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #4 Show Don’t Tell, line 915
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:915"
- id: B-advertising-047
  type: rule
  name: >-
    Non-verbal ads need non-verbal CTAs
  statement: >-
    An ad with no spoken words carries a visual CTA that works without narration.
  applies_when: >-
    A show-don't-tell ad with no ad copy.
  anchor: >-
    Non-verbal ads need non-verbal CTAs. For this type of ad, there are no words, so make sure you add a visual CTA that works without narration/speaking.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #4 Show Don’t Tell, line 925
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:925"
- id: B-advertising-048
  type: rule
  name: >-
    Optimize for LTV:CAC, not CAC
  statement: >-
    A campaign is not switched off for a cost per lead above the KPI; it is judged on LTV:CAC rather than on acquisition cost alone.
  why: >-
    This type of ad does not optimize for cheap leads, it optimizes for big spenders: $1,000 customers who pay $10,000 cost more and make more than $100 customers who pay $200.
  applies_when: >-
    A campaign written for advanced, higher-value prospects (Gym Launch long-term-result campaign; handbook 2025).
  anchor: >-
    This campaign taught me an important lesson: don’t optimize for CAC, optimize for LTV:CAC.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #5 Long Term Result, line 951
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:951"
- id: B-advertising-049
  type: rule
  name: >-
    Speak the language of the customer you want
  statement: >-
    To attract the exact customer rather than the genre of customer, the ad uses language and numbers only the upper echelon of customers would understand.
  why: >-
    Talking to the upper market gets the upper market and the smaller market too, but only talking to a beginner never gets the advanced buyer, and nobody else talks to the advanced buyer for fear of ostracizing the rest.
  anchor: >-
    Use language that only the upper echelon of customers would understand.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #5 Long Term Result, line 953
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:953"
- id: B-advertising-050
  type: rule
  name: >-
    Avatar in their own workspace plus a before/after stat
  statement: >-
    The ad opens on the ideal customer filmed in their own workspace with a bold industry-specific before/after stat on screen.
  anchor: >-
    Film your ideal customer in their own workspace (chef in the kitchen, contractor on-site, founder at the desk).
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #5 Long Term Result, line 1002
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1002"
- id: B-advertising-051
  type: rule
  name: >-
    One pain sentence as the hook
  statement: >-
    The hook is a single pain sentence, enough to make the right prospect think that's me.
  anchor: >-
    Hook with a single pain sentence.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #5 Long Term Result, line 1004
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1004"
- id: B-advertising-052
  type: rule
  name: >-
    Their pain, not someone else's
  statement: >-
    Two to three further pains are stacked, each a detail only the intended avatar would relate to.
  why: >-
    Pain always works, but the pain has to be their pain; advanced prospects lean in when the struggle sounds exactly like theirs.
  anchor: >-
    Ex: Mention hours, cash burn, family pressure—details only an advanced avatar would relate to.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #5 Long Term Result, line 1016
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1016"
- id: B-advertising-053
  type: rule
  name: >-
    Mark the decision point
  statement: >-
    The testimonial names the solution and the date it was bought.
  why: >-
    The timestamp increases credibility by a lot.
  anchor: >-
    make sure they name your solution and when they did it
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #5 Long Term Result, line 1018
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1018"
- id: B-advertising-054
  type: rule
  name: >-
    Fast Win and Big Win
  statement: >-
    The ad shows two tiers of result: a fast early win and a big long-term win.
  why: >-
    Two tiers show both the quick payoff and the long-term climb, and you want both.
  anchor: >-
    Show two wins—the Fast Win and the Big Win.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #5 Long Term Result, line 1020
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1020"
- id: B-advertising-055
  type: rule
  name: >-
    Deep metrics attract advanced avatars
  statement: >-
    The ad displays metrics only advanced people would understand (LTV, churn, margin, head count, salaries) aligned with the headline proof.
  why: >-
    The deeper the metric, the more advanced the avatar you attract.
  anchor: >-
    Display metrics only advanced people would understand that would be aligned with the larger proof
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #5 Long Term Result, line 1022
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1022"
- id: B-advertising-056
  type: rule
  name: >-
    Money stuff and soft stuff together
  statement: >-
    Alongside the financial results the ad names life improvements and soft benefits.
  why: >-
    Human outcomes make the financials feel real, and covering both angles gets both types of avatar, since some buyers want the soft stuff and others the money stuff.
  anchor: >-
    Don’t forget life improvements and “soft” benefits.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #5 Long Term Result, line 1024
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1024"
- id: B-advertising-057
  type: rule
  name: >-
    Reason why CTA
  statement: >-
    The spokesperson restates the hook and ties the outcome to the call to action.
  anchor: >-
    Have the spokesperson/testimonial restate the hook and tie the outcome to the call to action.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #5 Long Term Result, line 1026
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1026"
- id: B-advertising-058
  type: rule
  name: >-
    Peer endorsement for advanced prospects
  statement: >-
    When the target is an advanced prospect the invitation is issued by the peer in the ad, not by the advertiser.
  why: >-
    Advanced prospects respond better to peer endorsement than to the seller.
  applies_when: >-
    Ads aimed at advanced, higher-value prospects.
  anchor: >-
    Advanced prospects respond better to peer endorsement than you.
  source: >-
    acq-advertising-handbook.md, Section I, Ad Framework #5 Long Term Result, line 1026
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1026"
- id: B-advertising-059
  type: rule
  name: >-
    Looking For 5 Avatars as the opening ad of a launch
  statement: >-
    When something new is launched, the first ad run is the looking-for-N-avatars ad.
  why: >-
    It is one of the most classic direct response ads of all time, it works in any niche, it worked 70 years ago and it works today.
  applies_when: >-
    Launching something new, starting to run paid ads, or beginning to monetize an audience.
  anchor: >-
    When I launch something new, I’ll almost always start with an ad like this.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #1 Looking For 5 Avatars..., line 1068
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1068"
- id: B-advertising-060
  type: rule
  name: >-
    Say who you are not looking for
  statement: >-
    The looking-for ad also names who you are not looking for, as specifically as possible.
  why: >-
    It further increases credibility.
  anchor: >-
    Be as specific as possible—it’ll further increase credibility.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #1 Looking For 5 Avatars..., line 1070
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1070"
- id: B-advertising-061
  type: rule
  name: >-
    ADucational setting for complex offers
  statement: >-
    Ads for complex, novel or higher-ticket offers are filmed in an educational setting (whiteboard, chalkboard, screen).
  why: >-
    The teacher visual signals authority and value; an educational setting works better with more complex products.
  anchor: >-
    The “teacher” visual signals authority and works best for complex, novel, or higher ticket offers.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #1 Looking For 5 Avatars..., line 1150
  confirmations: 5
  anchor_at: "acq-advertising-handbook.md:1150"
- id: B-advertising-062
  type: rule
  name: >-
    A believable reason for taking limited clients
  statement: >-
    The ad states why only a limited number of clients is being taken, and the reason given is believable.
  why: >-
    The author's preference is the truth.
  anchor: >-
    Explain why you’re only taking limited clients.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #1 Looking For 5 Avatars..., line 1164
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1164"
- id: B-advertising-063
  type: rule
  name: >-
    The difference must elevate and be proved
  statement: >-
    The stated difference from what else is on the market elevates your product or service and is underlined with proof.
  anchor: >-
    The difference should elevate your product/service. You’ll underline this with proof.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #1 Looking For 5 Avatars..., line 1166
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1166"
- id: B-advertising-064
  type: rule
  name: >-
    Split risk with the customer
  statement: >-
    The offer in the ad carries some element of performance compensation, so the advertiser is paid only if the customer wins.
  why: >-
    It decreases risk, shows intent to deliver, and attracts more people.
  anchor: >-
    have some element of performance compensation; this decreases risk, shows intent to deliver, and attracts more people.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #1 Looking For 5 Avatars..., line 1168
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1168"
- id: B-advertising-065
  type: rule
  name: >-
    Send them to your assistant
  statement: >-
    The CTA routes the applicant to an assistant or team member who qualifies them against the stated requirements.
  why: >-
    Mentioning the executive assistant reinforces authority and the authenticity of the ad, and keeps the frame that this is by application only.
  anchor: >-
    Mentioning my executive assistant further reinforced my authority and the authenticity of the ad.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #1 Looking For 5 Avatars..., line 1170
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1170"
- id: B-advertising-066
  type: rule
  name: >-
    Educate enough to decide
  statement: >-
    An ADucational ad teaches the prospect enough to make a decision, since marketing and sales share that objective and differ only in medium.
  anchor: >-
    The goal is to educate the prospect enough to make a decision.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #2: New vs. Old, line 1186
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1186"
- id: B-advertising-067
  type: rule
  name: >-
    ADucational ads for advertisers with no brand
  statement: >-
    An advertiser with no pre-existing brand uses ADucational ads, because the prospect judges the quality of the information rather than the brand.
  applies_when: >-
    Brand new in the market; it works even better once established.
  anchor: >-
    you'll be judged based on the quality of the information
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #2: New vs. Old, line 1188
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1188"
- id: B-advertising-068
  type: rule
  name: >-
    Call out the exact avatar in five seconds
  statement: >-
    The exact avatar is called out in the first sentence, within five seconds.
  why: >-
    The hyper-specific call-out filters for qualified prospects only.
  anchor: >-
    Film in an educational setting and call out your exact avatar in ≤ five seconds.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #2: New vs. Old, line 1250
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:1250"
- id: B-advertising-069
  type: rule
  name: >-
    Big claim with details
  statement: >-
    The claim states a big increase inside the same context (same niche, same leads), not a bare number.
  why: >-
    Big increase plus same context equals curiosity.
  anchor: >-
    Make a big claim with details.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #2: New vs. Old, line 1260
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1260"
- id: B-advertising-070
  type: rule
  name: >-
    Attribute the pain to the old model
  statement: >-
    Every relevant problem the prospect lives with is attributed, as specifically as possible, to their outdated model.
  why: >-
    If the person relates to the old way and to the problems described, they are hooked to hear how it was solved.
  anchor: >-
    attribute all relevant woes to their outdated model
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #2: New vs. Old, line 1262
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1262"
- id: B-advertising-071
  type: rule
  name: >-
    Anchor the new way to one simple metric
  statement: >-
    The new way is explained as superior on one simplified metric, written out on screen.
  anchor: >-
    Explain your model/way/method is superior based on this simplified metric.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #2: New vs. Old, line 1264
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1264"
- id: B-advertising-072
  type: rule
  name: >-
    Case study or hypothetical as proxy proof
  statement: >-
    The claim is driven home with a worked case study or hypothetical whose math the prospect can follow.
  why: >-
    The math makes the promise believable and serves as a proxy for proof.
  anchor: >-
    The math makes the promise believable and serves as a proxy for proof.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #2: New vs. Old, line 1266
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1266"
- id: B-advertising-073
  type: rule
  name: >-
    One proof line is enough
  statement: >-
    Authority is established with a single giant credential or number, not a list.
  why: >-
    One number is enough if it is compelling, and a single giant credential convinces the audience to keep listening before attention fades.
  anchor: >-
    Reinforce authority with a single proof line.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #2: New vs. Old, line 1268
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:1268"
- id: B-advertising-074
  type: rule
  name: >-
    The CTA previews the process
  statement: >-
    The CTA spells out the micro-journey that follows the click (apply, qualification call, what happens on it).
  why: >-
    Detailing the micro-journey removes friction, keeps the advertiser elevated and maintains the frame that this is by application only.
  anchor: >-
    Finish with a CTA that previews the process.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #2: New vs. Old, line 1272
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1272"
- id: B-advertising-075
  type: rule
  name: >-
    Specificity is the proof of expertise
  statement: >-
    The problem is described so specifically that the listener concludes the advertiser must be an insider.
  why: >-
    You demonstrate expertise by how specifically and relevantly you can describe the problem; the prospect thinks he must really understand this space.
  anchor: >-
    You demonstrate your expertise by how specific or relevant you can describe the problem.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #3: Why You Will Never, line 1292
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:1292"
- id: B-advertising-076
  type: rule
  name: >-
    Build pressure, then resolve it with the CTA
  statement: >-
    The ad lists the problems as specifically as possible, keeps building pressure, and resolves that pressure only with the CTA.
  anchor: >-
    List all the problems out as specifically as you possibly can. Continue to build pressure, then resolve the pressure with a CTA.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #3: Why You Will Never, line 1294
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1294"
- id: B-advertising-077
  type: rule
  name: >-
    Rapid-fire numeric pains
  statement: >-
    The warning signs are delivered as rapid-fire numbers with thresholds (LTV under $10k, ARPC under $2.5k, gross margin below 80%, payback over 30 days).
  why: >-
    Each number makes owners think this is me.
  applies_when: >-
    Agency owners; the thresholds are the author's benchmarks for that niche (handbook 2025).
  anchor: >-
    Ex: LTV under $10k, ARPC under $2.5k, gross margin below 80%, payback over 30 days.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #3: Why You Will Never, line 1370
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1370"
- id: B-advertising-078
  type: rule
  name: >-
    Name the mechanism something non-obvious
  statement: >-
    The new solution gets a non-obvious name and is explained in one sentence that shows how it inverts the problems just listed.
  why: >-
    An obvious name kills the curiosity: Pay Per Show was too obvious, so it became reverse royalty.
  anchor: >-
    Name it something non-obvious. Explain what it is in one sentence and how it inverts all their problems.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #3: Why You Will Never, line 1372
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1372"
- id: B-advertising-079
  type: rule
  name: >-
    CTA to the lead magnet when more information is needed
  statement: >-
    If the prospect needs to consume more information before buying, the CTA sends them to the lead magnet or video sales letter and names the steps after it.
  anchor: >-
    If you need the prospect to consume more information to buy, tell them how.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #3: Why You Will Never, line 1374
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1374"
- id: B-advertising-080
  type: rule
  name: >-
    The north star metric must be predictive
  statement: >-
    The metric the ad is built around predicts the prospect's pain point; any metric qualifies as long as it is predictive.
  anchor: >-
    You need to pick a metric that does the same for your prospect.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #4: The “North Star”, line 1388
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1388"
- id: B-advertising-081
  type: rule
  name: >-
    Callout plus nightmare in one breath
  statement: >-
    The opening addresses the avatar and their biggest pain in one breath.
  anchor: >-
    Address the avatar and their biggest pain in one breath.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #4: The “North Star”, line 1468
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1468"
- id: B-advertising-082
  type: rule
  name: >-
    A hierarchy of outcomes on the metric
  statement: >-
    The ad lays out a hierarchy of outcomes tied to the north star metric so the prospect can locate themselves in it.
  anchor: >-
    The prospect can identify themselves in the hierarchy.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #4: The “North Star”, line 1472
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1472"
- id: B-advertising-083
  type: rule
  name: >-
    Pains at every level of the hierarchy
  statement: >-
    Specific pains are listed for each level of the hierarchy, as concrete moments rather than categories.
  why: >-
    The narrower your focus, the more examples there are.
  anchor: >-
    The narrower your focus, the more examples there are.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #4: The “North Star”, line 1474
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1474"
- id: B-advertising-084
  type: rule
  name: >-
    One sentence for the new method
  statement: >-
    The explanation of how the new method fixes the north star metric stays to one clear sentence.
  anchor: >-
    Keep the explanation to one clear sentence
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #4: The “North Star”, line 1476
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1476"
- id: B-advertising-085
  type: rule
  name: >-
    A short selfie ad sells only the next step
  statement: >-
    A very short selfie ad sells the next step and nothing more, and is used only where the funnel behind it carries the rest of the information.
  why: >-
    These ads rely on additional information in the funnel and conversion process; think of it as an ad for the lead magnet, not an ad to sell.
  applies_when: >-
    Top of funnel.
  anchor: >-
    These ads rely on having additional information in the funnel and conversion process.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #5: No BS Selfie, line 1492
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1492"
- id: B-advertising-086
  type: rule
  name: >-
    Let the setting do the selling
  statement: >-
    The clip opens in motion, with something in frame that establishes credibility for the thing being talked about.
  anchor: >-
    Walk and talk with something that establishes you as credible related to the thing you talk about.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #5: No BS Selfie, line 1535
  confirmations: 1
  authors_caveat: >-
    The author used the fancy car and house only for a brief stint and stopped because he did not want that kind of brand, while noting that it is effective.
  anchor_at: "acq-advertising-handbook.md:1535"
- id: B-advertising-087
  type: rule
  name: >-
    If-then pain statement
  statement: >-
    The ad opens with an if-then pain statement built on a specific number.
  why: >-
    The specificity pulls in the right prospects.
  anchor: >-
    Start with an if-then pain statement.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #5: No BS Selfie, line 1537
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1537"
- id: B-advertising-088
  type: rule
  name: >-
    Name the solution without explaining it
  statement: >-
    In a short ad the solution is named in one sentence and left unexplained.
  why: >-
    The lead magnet does the explaining.
  applies_when: >-
    A short top-of-funnel ad whose job is the click.
  anchor: >-
    Name the solution without explaining it.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #5: No BS Selfie, line 1539
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1539"
- id: B-advertising-089
  type: rule
  name: >-
    Proof from someone worse off
  statement: >-
    The proof point names someone in a weaker position than the prospect who got a better result than the prospect has.
  why: >-
    The juxtaposition implies that bigger or more experienced prospects can do even better, and makes the prospect think if they could do it, so can I.
  anchor: >-
    Show proof that someone worse than them got results better than them.
  source: >-
    acq-advertising-handbook.md, Section II, Ad Framework #5: No BS Selfie, line 1549
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1549"
- id: B-advertising-090
  type: rule
  name: >-
    Model the format, not the podcast
  statement: >-
    What is copied from a trending ad is the video format that is popular right now, not the specific format of the example.
  anchor: >-
    the lesson to take from this ad isn’t that it was a podcast, it’s that it was a popular video format at the time
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #1: Trending Format, line 1601
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1601"
- id: B-advertising-091
  type: rule
  name: >-
    Read organic to see paid six to twelve months ahead
  statement: >-
    Ad formats and hooks are taken from what organic content is doing today, because organic runs ahead of paid.
  why: >-
    Organic is always ahead of paid ads because of the volume and speed of testing by creators.
  anchor: >-
    If you want to see where ads will be in six to 12 months, just look at where organic is today.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #1: Trending Format, line 1603
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1603"
- id: B-advertising-092
  type: rule
  name: >-
    Hit the value equation pillars, then cut to CTA
  statement: >-
    In a trending-format ad the speaker truthfully explains why the thing is good by hitting the main value equation pillars, then cuts to the CTA.
  anchor: >-
    Just truthfully explain why you think your thing is awesome by hitting the main value equation pillars.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #1: Trending Format, line 1605
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1605"
- id: B-advertising-093
  type: rule
  name: >-
    Bolt a CTA onto winning organic
  statement: >-
    Your highest-performing organic content is turned into an ad by adding a CTA at the end.
  applies_when: >-
    You already make organic content.
  anchor: >-
    take your highest performing organic content and simply bolt on a CTA on the end
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #1: Trending Format, line 1607
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1607"
- id: B-advertising-094
  type: rule
  name: >-
    The clip must read as organic
  statement: >-
    A trending-format ad is cut so that viewers think they are watching a snippet from your show rather than an ad.
  anchor: >-
    Viewers should think they’re watching a snippet from your show, not an ad.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #1: Trending Format, line 1654
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1654"
- id: B-advertising-095
  type: rule
  name: >-
    Lead with a recent surprising discovery
  statement: >-
    The ad opens on something recent that genuinely surprised the speaker.
  why: >-
    The recency and the genuine disbelief hook attention.
  anchor: >-
    Lead with a recent surprising discovery.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #1: Trending Format, line 1656
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1656"
- id: B-advertising-096
  type: rule
  name: >-
    Speed and scale in one line
  statement: >-
    One line carries both the size of the result and the short window it happened in.
  why: >-
    Big numbers plus a 30-day window make the result feel both huge and fast.
  anchor: >-
    Big numbers plus a 30-day window make the result feel both huge and fast.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #1: Trending Format, line 1666
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1666"
- id: B-advertising-097
  type: rule
  name: >-
    Big outcomes and average outcomes together
  statement: >-
    Every ad states both the big outcomes and the average, everyday outcomes.
  why: >-
    People want to know the big thing is possible but most importantly want to understand what is likely.
  anchor: >-
    I always try to include both big and average outcomes in my ads.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #1: Trending Format, line 1668
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1668"
- id: B-advertising-098
  type: rule
  name: >-
    Three-second keyframe opening
  statement: >-
    The ad opens on a three-second keyframe of a prop against a high-contrast backdrop, which creates immediate motion.
  anchor: >-
    Film a three-second keyframe of cash fanned out against a high-contrast backdrop (red works everywhere).
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #2: Value Anchor, line 1739
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1739"
- id: B-advertising-099
  type: rule
  name: >-
    Oversized on-screen text repeating the hook
  statement: >-
    Oversized text repeating the first line fills the screen so that muted viewers get the hook before they can scroll away.
  anchor: >-
    Overlay oversized text that repeats your first question so even muted viewers grasp the hook
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #2: Value Anchor, line 1739
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1739"
- id: B-advertising-100
  type: rule
  name: >-
    Make free valuable before giving it away
  statement: >-
    Before the offer is given away free, its value is anchored with a series of descending price questions.
  why: >-
    Free still has costs, so free has to be made valuable; the descending anchor makes free feel like an unexpected windfall instead of a marketing cliché.
  anchor: >-
    Free still has costs, this means that you still have to make free valuable.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #2: Value Anchor, line 1741
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1741"
- id: B-advertising-101
  type: rule
  name: >-
    Dream outcome on a fast timeline
  statement: >-
    Right after the anchor and price drop comes a one-sentence promise naming the outcome and the duration.
  anchor: >-
    Put the dream outcome on a fast timeline.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #2: Value Anchor, line 1743
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1743"
- id: B-advertising-102
  type: rule
  name: >-
    Better than free
  statement: >-
    A variable incentive is added on top of the free offer, for top performers, a random selection or everyone.
  why: >-
    It turns zero cost into potential gain at no cost.
  anchor: >-
    Make it better than free with a variable incentive.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #2: Value Anchor, line 1747
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1747"
- id: B-advertising-103
  type: rule
  name: >-
    Volume negates luck
  statement: >-
    Winners are produced by deliberate volume and testing sessions, not by waiting for a lucky hit.
  why: >-
    People romanticize random hits, but the real winners are built by deliberate work; the winning Bribe ad came out of one day of about 250 ads and produced 200+ further variations.
  anchor: >-
    People romanticize random hits, but volume negates luck.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #3: Bribe, line 1769
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1769"
- id: B-advertising-104
  type: rule
  name: >-
    The ad earns the click, the page closes
  statement: >-
    The creative carries only as much selling as is needed to earn the click, and the rest of the selling is shifted to the page and the video sales letter.
  why: >-
    Some selling always has to happen, but shorter proof-heavy creatives worked best; curiosity and stakes drive the click and then the page converts the traffic.
  anchor: >-
    We just needed enough to earn the click, then let the page and video sales letter close.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #3: Bribe, line 1771
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1771"
- id: B-advertising-105
  type: rule
  name: >-
    Recycle hooks across industries
  statement: >-
    A hook or format proven in one niche is reused in other niches instead of inventing a new one.
  why: >-
    Only amateurs reinvent the wheel; pros use proven playbooks and checklists and make up for the rest with volume.
  anchor: >-
    I recycle hooks and formats across industries. You should too. Only amateurs reinvent the wheel.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #3: Bribe, line 1775
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1775"
- id: B-advertising-106
  type: rule
  name: >-
    Big visuals, big offer, small words, short sentences
  statement: >-
    The creative uses big visuals and a big offer with small words and short sentences.
  anchor: >-
    Big visuals. Big offer. Small words. Short sentences.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #3: Bribe, line 1775
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1775"
- id: B-advertising-107
  type: rule
  name: >-
    Pattern-interrupt ask for contact information
  statement: >-
    A lead-magnet ad opens by asking the viewer directly for their contact information as a pattern interrupt.
  why: >-
    The reveal plus the direct ask buys time and signals immediately that handing over contact info triggers something valuable.
  anchor: >-
    Ask them for contact information with a pattern-interrupt question.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #3: Bribe, line 1816
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1816"
- id: B-advertising-108
  type: rule
  name: >-
    State the cash value of the free stuff
  statement: >-
    The free thing is promised with a stated cash value, and only a realistic one.
  why: >-
    Stating cash value turns a vague lead magnet into a tangible benefit.
  anchor: >-
    Stating cash value (if realistic!) turns a vague lead magnet into a tangible benefit.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #3: Bribe, line 1826
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1826"
- id: B-advertising-109
  type: rule
  name: >-
    Anchor against real market pricing
  statement: >-
    The free thing is priced against what comparable products really sell for, with escalating numbers, and only if the comparison is true.
  why: >-
    It proves the free offer does not suck and makes free feel like generosity rather than a gimmick.
  anchor: >-
    Point out that comparable products/services sell for more and escalate the numbers.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #3: Bribe, line 1828
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1828"
- id: B-advertising-110
  type: rule
  name: >-
    Tie the gift to the dream outcome
  statement: >-
    One line ties the free thing to the result that matters to the prospect.
  why: >-
    Outcome focus prevents the offer from sounding random.
  anchor: >-
    Outcome focus prevents the offer from sounding random.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #3: Bribe, line 1830
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1830"
- id: B-advertising-111
  type: rule
  name: >-
    Every bonus carries a reason why
  statement: >-
    Any additional incentive in the ad is accompanied by a stated motive for it.
  why: >-
    A motive behind a bonus makes the bonus feel more authentic and by extension increases urgency.
  anchor: >-
    A motive behind a bonus makes the bonus feel more authentic, and by extension increases urgency.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #3: Bribe, line 1832
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:1832"
- id: B-advertising-112
  type: rule
  name: >-
    CTA congruent with the hook
  statement: >-
    The CTA repeats the hook, so the same thing that made them watch makes them act.
  why: >-
    If they stayed to watch because of the hook, they will also take the next step because of it.
  anchor: >-
    Make your CTA the same as your hook.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #3: Bribe, line 1834
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1834"
- id: B-advertising-113
  type: rule
  name: >-
    Beat them to the punch on low outcomes
  statement: >-
    The ad itself names the lower-tier and below-average outcomes rather than leaving the prospect to wonder about them.
  why: >-
    People already know earning an income is cool; the issue is that they do not believe they will be able to do it, and they are already doubtful and already wondering about the average person.
  anchor: >-
    So don't be afraid to talk about your lower tier outcomes
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #4: Underdog, line 1856
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1856"
- id: B-advertising-114
  type: rule
  name: >-
    Lead with the modest number
  statement: >-
    The hook is a modest, believable, specific number flashed against a blank screen with subtle motion before the audio starts.
  why: >-
    Lower, specific numbers convert better because viewers think I could do that.
  anchor: >-
    Lead with a modest, believable number/outcome that feels attainable.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #4: Underdog, line 1898
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1898"
- id: B-advertising-115
  type: rule
  name: >-
    Show the floor, not just the ceiling
  statement: >-
    After naming the big results the ad circles back to the smallest one.
  why: >-
    The contrast makes the offer credible to beginners while still engaging top performers.
  anchor: >-
    then circle back to the underdog outcome to show the floor, not just the ceiling
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #4: Underdog, line 1908
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:1908"
- id: B-advertising-116
  type: rule
  name: >-
    They will only think it is a big deal if you tell them it is
  statement: >-
    A promotion is stated in the ad to be a big deal, and the big and crazy reason behind it is given.
  why: >-
    Prospects will believe you would do something big and crazy if you have a big and crazy reason; putting your money where your mouth is dissolves skepticism and adds credibility.
  anchor: >-
    Prospects will believe that you’d do something big and crazy if you have a big and crazy reason.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #4: Underdog, line 1910
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1910"
- id: B-advertising-117
  type: rule
  name: >-
    The prize is chosen for your audience
  statement: >-
    The giveaway is the most valuable thing you can afford that is huge for your specific audience, not automatically cash or a car.
  why: >-
    The broader the audience, the better money, cars and vacations work; for a narrow audience such as gym owners, re-outfitting their gym is more compelling.
  anchor: >-
    The broader the audience though, the more things like money, cars, and vacations work.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #5: Challenge With Prize, line 1932
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1932"
- id: B-advertising-118
  type: rule
  name: >-
    Show the prize on camera
  statement: >-
    The prize is displayed on camera in the ad.
  why: >-
    It proves you actually have the thing to give away.
  anchor: >-
    Display it on-camera to prove that you have the thing to give away.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #5: Challenge With Prize, line 2005
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2005"
- id: B-advertising-119
  type: rule
  name: >-
    Put the giveaway on a time constraint
  statement: >-
    The giveaway is tied to a clear, short and believable window.
  why: >-
    A deadline gets more people to act if it is believable.
  anchor: >-
    Tie the giveaway to a clear, short window
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #5: Challenge With Prize, line 2007
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2007"
- id: B-advertising-120
  type: rule
  name: >-
    Name a previous winner
  statement: >-
    The ad references a recent contest winner who actually received the prize.
  why: >-
    Real-world peers prove the prize is winnable and the process legitimate.
  anchor: >-
    Real-world peers prove the prize is winnable and the process is legitimate.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #5: Challenge With Prize, line 2009
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2009"
- id: B-advertising-121
  type: rule
  name: >-
    One metric of entry
  statement: >-
    Winning the challenge is defined by a single metric that matches your business goal and is simple for both sides to track.
  why: >-
    One clear path beats a complicated points system.
  anchor: >-
    One clear path beats a complicated points system.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #5: Challenge With Prize, line 2011
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2011"
- id: B-advertising-122
  type: rule
  name: >-
    Show how you will help them win
  statement: >-
    The ad promises the tools, checklists, tips or live Q&A that participants get while competing.
  why: >-
    Hand-holding overcomes the I'll get stuck objection before it forms.
  anchor: >-
    Hand-holding overcomes the “I’ll get stuck” objection before it forms.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #5: Challenge With Prize, line 2013
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2013"
- id: B-advertising-123
  type: rule
  name: >-
    Make not winning valuable too
  statement: >-
    The ad states that the worst case is walking away with the free things, which have value on their own outside the grand prize.
  why: >-
    It makes both outcomes a win and leaves not doing it as the only bad outcome.
  anchor: >-
    Remind them the worst-case scenario is walking away with all the free stuff
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #5: Challenge With Prize, line 2015
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2015"
- id: B-advertising-124
  type: rule
  name: >-
    Prove the free thing works
  statement: >-
    User counts, testimonial snippets or screenshots of past wins are cited for the free thing, each paired with a visual.
  why: >-
    Pairing visuals with each component makes them dramatically more compelling.
  anchor: >-
    Cite user counts, testimonial snippets, or quick screenshots of past wins.
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #5: Challenge With Prize, line 2017
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2017"
- id: B-advertising-125
  type: rule
  name: >-
    Show the signup flow
  statement: >-
    The ad shows a fast screen recording of the page and opt-in the click leads to.
  why: >-
    It aligns expectations and reduces uncertainty about the next step, which removes the final barrier to conversion.
  anchor: >-
    Overlay a fast screen recording or screenshare mock-up of the signup flow
  source: >-
    acq-advertising-handbook.md, Section III, Ad Framework #5: Challenge With Prize, line 2019
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:2019"
- id: B-advertising-126
  type: rule
  name: >-
    Movement, and real movement first
  statement: >-
    The ad contains movement, and real physical movement is preferred over digital motion.
  why: >-
    Stuff that moves generally beats stuff that does not, and real stuff that moves often beats computer stuff that moves; ads where the author moves almost always outperform.
  anchor: >-
    Stuff that moves generally beats stuff that doesn’t. And real stuff that moves often beats computer stuff that moves.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #1: Flying Prop, line 2063
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:2063"
- id: B-advertising-127
  type: rule
  name: >-
    Daisy-chained open loops
  statement: >-
    A curiosity ad chains open loops so that the only action that closes any of them is taking the next step.
  why: >-
    Everything in the ad has the objective of making people want to come and see what is going to happen, which gets both the registration and the show.
  anchor: >-
    The entire ad is a daisy chain of open loops with only one action to close them—taking the next step.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #1: Flying Prop, line 2065
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:2065"
- id: B-advertising-128
  type: rule
  name: >-
    Catch a flying prop
  statement: >-
    The video starts with the spokesperson catching something mid-air while looking at the camera.
  anchor: >-
    Start the video by having the spokesperson catch something mid-air while looking at the camera.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #1: Flying Prop, line 2116
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2116"
- id: B-advertising-129
  type: rule
  name: >-
    Tie the prop to the offer with one joke
  statement: >-
    A one-liner links the prop to the product or service immediately after the visual hook.
  anchor: >-
    Drop a one-liner that links the prop to your product or service.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #1: Flying Prop, line 2117
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2117"
- id: B-advertising-130
  type: rule
  name: >-
    Make it a big deal to you
  statement: >-
    The ad names the time, money and relationship capital invested and ties that investment to what the viewer gets.
  why: >-
    It approximates the value for them: make it a big deal to you, so it is a big deal to them; stakes are a big part of that.
  anchor: >-
    In short, make it a big deal to you, so it’s a big deal to them.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #1: Flying Prop, line 2118
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:2118"
- id: B-advertising-131
  type: rule
  name: >-
    Tease a secret available only after the next step
  statement: >-
    An unrevealed bonus is teased that only people who take the next step can get, and its details are withheld.
  why: >-
    Withholding details keeps tension high until they act; after they act, more loops can be opened to move them through the process.
  anchor: >-
    Tease an unrevealed bonus available only to people who take the next step.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #1: Flying Prop, line 2119
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2119"
- id: B-advertising-132
  type: rule
  name: >-
    Keep a closet of props
  statement: >-
    Anything that catches your attention and can be bought is bought and stored as a prop for future ads.
  why: >-
    It will probably catch someone else's attention too, and when it does it will make more money than it cost, by a lot.
  anchor: >-
    Anytime something catches your attention—if you can buy it, do so—because it’ll probably catch someone else’s.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #1: Flying Prop, line 2120
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2120"
- id: B-advertising-133
  type: rule
  name: >-
    Investment as a proxy for value
  statement: >-
    When the thing itself cannot be revealed without killing the curiosity, the ad talks about the costs incurred to create it instead.
  why: >-
    The investment stands as a proxy for the prospect's potential benefit; where parts can be named directly, they are.
  anchor: >-
    then you talk more about your investment as a proxy for their potential benefit.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #2: Bribe, line 2188
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2188"
- id: B-advertising-134
  type: rule
  name: >-
    A value range between two known items
  statement: >-
    An unnamed gift is described as a range between one low-value and one high-value known item rather than named.
  why: >-
    People automatically abstract what they will get towards the bigger thing, and you are not going to beat anyone's imagination.
  anchor: >-
    Give a range of values between two known items: one low-value and one high-value.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #2: Bribe, line 2200
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2200"
- id: B-advertising-135
  type: rule
  name: >-
    Good ads do two things
  statement: >-
    Every ad has a part that gets attention and a part that increases the benefit and decreases the cost of taking action.
  anchor: >-
    get the prospect’s attention→get the prospect to take action.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #3: The Rumors Are True, line 2228
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2228"
- id: B-advertising-136
  type: rule
  name: >-
    The Rumors Are True
  statement: >-
    The ad opens by telling the viewer that other people already want what you have and that it is finally coming out.
  why: >-
    Positioning the product as important because other people talk about it makes the viewer feel left out of something important, which motivates action; this hook works in any market.
  anchor: >-
    Tell them other people want what you have.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #3: The Rumors Are True, line 2266
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2266"
- id: B-advertising-137
  type: rule
  name: >-
    Show receipts for the investment
  statement: >-
    Claims about the personal investment made (iterations, hours, money) are backed with receipts that prove it was actually spent.
  why: >-
    Proving the spend dramatically increases how much they believe the value.
  anchor: >-
    prove that you actually spent all that on the thing—it will
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #3: The Rumors Are True, line 2278
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2278"
- id: B-advertising-138
  type: rule
  name: >-
    Turn a winning hook into other formats
  statement: >-
    Once a hook wins in video, permutations of it are made in static and other formats.
  why: >-
    Those static permutations were big winners too; simple does not mean ineffective, and winning is hard enough without also making it complicated.
  anchor: >-
    Once we have a winning hook, we will make permutations of that ad into static form.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #3: The Rumors Are True, line 2284
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:2284"
- id: B-advertising-139
  type: rule
  name: >-
    Confront while walking into the lens
  statement: >-
    A confrontational hook is delivered walking toward the camera, rounding a corner, looking into the lens.
  why: >-
    Walking around corners and high movement towards the camera works exceptionally well and pairs with a confrontational hook; people find walking and talking hard, so doing it well is rarer.
  anchor: >-
    Confront their belief. Look into the lens, round a corner, and open with
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #4: You’re Being Lied To, line 2358
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2358"
- id: B-advertising-140
  type: rule
  name: >-
    Old way, then new way
  statement: >-
    The ad throws rocks at the old way, naming it as the lie, and then states the new way as the truth.
  anchor: >-
    Throw rocks at the old way (the lie), then tell them the new way (the truth).
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #4: You’re Being Lied To, line 2360
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2360"
- id: B-advertising-141
  type: rule
  name: >-
    Prove the new way
  statement: >-
    The new way is followed immediately by proof, whether math, authority or social proof.
  anchor: >-
    Use math, authority, social proof, or any other kind of proof.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #4: You’re Being Lied To, line 2362
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2362"
- id: B-advertising-142
  type: rule
  name: >-
    Share your selfish reason why
  statement: >-
    The ad states openly what the advertiser gets out of it.
  why: >-
    People trust people who share their biases openly, even when they know the bias runs against their own interest.
  anchor: >-
    People trust people who share their biases openly,
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #4: You’re Being Lied To, line 2364
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2364"
- id: B-advertising-143
  type: rule
  name: >-
    Frame the time saved, not a fast promise
  statement: >-
    Instead of promising fast results, the ad reframes how long solving the problem alone would take and presents the compression as the speed being offered.
  anchor: >-
    Reframe the amount of time it would take to solve this problem on their own without your product/services
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #4: You’re Being Lied To, line 2366
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2366"
- id: B-advertising-144
  type: rule
  name: >-
    One step resolves the tension
  statement: >-
    The ad closes with a single on-screen step that resolves the tension it created.
  anchor: >-
    One step resolves the tension you created.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #4: You’re Being Lied To, line 2368
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2368"
- id: B-advertising-145
  type: rule
  name: >-
    Big numbers at the beginning
  statement: >-
    Numbers, especially big ones, are placed at the beginning of the ad.
  why: >-
    They seem to work every time the author uses them, and a theme repeated across the Blackbook represents the absolute best of zillions of ads.
  anchor: >-
    Numbers at the beginning of ads, especially big numbers, seem to work every time I use them.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #5: Data Stack, line 2390
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2390"
- id: B-advertising-146
  type: rule
  name: >-
    Half-written board
  statement: >-
    The whiteboard in frame is only half filled in when the ad opens.
  why: >-
    Having half of something written invokes more curiosity because people want to see it completed, and it is itself a flex showing the work that went in.
  anchor: >-
    having half of something written on the board invokes more curiosity because people want to see it completed
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #5: Data Stack, line 2392
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2392"
- id: B-advertising-147
  type: rule
  name: >-
    Say the winning thing in multiple ways
  statement: >-
    A winning statement is rewritten into several permutations rather than run in one wording.
  why: >-
    When you say a winning thing in multiple ways, it gives you multiple winners.
  anchor: >-
    And when you say a winning thing in multiple ways, it gives you multiple winners.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #5: Data Stack, line 2394
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2394"
- id: B-advertising-148
  type: rule
  name: >-
    Collect the stats before the shoot
  statement: >-
    All the stats about the product are put on one sheet and the most impressive ones selected before the recording session.
  anchor: >-
    Put all of them on one sheet. Select the most impressive ones. Do this before your recording session.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #5: Data Stack, line 2428
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2428"
- id: B-advertising-149
  type: rule
  name: >-
    Name how many have already shown interest
  statement: >-
    The ad states the number of people who have already registered, preordered or joined the waiting list.
  why: >-
    You want people to feel like they are going to be left out.
  anchor: >-
    You want people to feel like they’re gonna be left out.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #5: Data Stack, line 2432
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2432"
- id: B-advertising-150
  type: rule
  name: >-
    State the real limitations
  statement: >-
    The true limits on what can be delivered (hours, inventory, number of people) are stated in the ad.
  why: >-
    Owning the real limitation increases demand by cutting perceived supply, which is what creates scarcity.
  anchor: >-
    Doing this increases demand by cutting perceived supply.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #5: Data Stack, line 2442
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2442"
- id: B-advertising-151
  type: rule
  name: >-
    Fast, clear and easy next step
  statement: >-
    The instruction for what to do next is fast, clear and easy.
  anchor: >-
    Make it fast, clear, and easy.
  source: >-
    acq-advertising-handbook.md, Section IV, Ad Framework #5: Data Stack, line 2444
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2444"
- id: B-advertising-152
  type: rule
  name: >-
    The four promises of an ad
  statement: >-
    The ad promises a result and makes it fast, likely and easy.
  anchor: >-
    Promise a result, make it fast, make it likely, and make it easy.
  source: >-
    acq-advertising-handbook.md, PART III: WHAT TO DO NEXT→CHECKLISTS, line 2472
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2472"
- id: B-advertising-153
  type: rule
  name: >-
    Curiosity front, proof middle, one action at the end
  statement: >-
    Curiosity is packed at the front of the ad, proof in the middle, and a single action at the end.
  anchor: >-
    Pack curiosity up front, proof in the middle, and a single action at the end.
  source: >-
    acq-advertising-handbook.md, PART III: WHAT TO DO NEXT→CHECKLISTS, line 2472
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2472"
- id: B-advertising-154
  type: rule
  name: >-
    Comparisons
  statement: >-
    The script carries all four comparisons: dream outcome against the nightmare of staying the same, speed to result against the delay of inaction, certainty of the new path against the risk of the current one, and ease of the result against the difficulty of the current path.
  applies_when: >-
    Checking an ad script against the Best Ad Framework Checklist must-haves.
  anchor: >-
    Dream Outcome & Nightmare of Staying The Same
  source: >-
    acq-advertising-handbook.md, Best Ad Framework Checklist, AD SCRIPT, line 2601
  confirmations: 1
  authors_caveat: >-
    I want to be clear, you can make ads without some of my must-haves… I just don’t.
  anchor_at: "acq-advertising-handbook.md:2601"
- id: B-advertising-155
  type: rule
  name: >-
    As Many Proof Points As Possible
  statement: >-
    The script carries as many proof points as possible.
  applies_when: >-
    Checking an ad script against the Best Ad Framework Checklist must-haves.
  anchor: >-
    As Many Proof Points As Possible
  source: >-
    acq-advertising-handbook.md, Best Ad Framework Checklist, AD SCRIPT, line 2605
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2605"
```
