# Улов фазы 1 — ACQ Advertising Handbook (2025) (ярус 2), тип C: разборы (кейсы)

Группа `tier2-advertising`, слаг `advertising`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **47** (экстрактор вернул 47, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `acq-advertising-handbook.md` | 1–2657 | 4 | 47 |

## Как собран файл

Экстрактор C (Application cases) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-advertising.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-advertising-C.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 2; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: C-advertising-001
  type: case
  name: >-
    Henry Ford and the Model T ad on the wall
  statement: >-
    Ford passed the same black-and-white Model T print layout pinned on his chief marketing officer's wall every morning for three months, then asked when they would stop running it because he was tired of looking at it; the CMO answered that it had never run once and that Ford had seen it a hundred times only because he worked there.
  why: >-
    You make campaigns for the prospects, not for yourself, so you will tire of an ad long before the market has even noticed your name; an ad that works is kept running until it stops working, never until you get bored.
  anchor: >-
    Henry Ford walked the same hallway to his factory floor every morning. For three straight months he passed the glass door of his chief marketing officer and saw the exact same print layout pinned on the wall: a black-and-white ad for the Model T.
  source: >-
    acq-advertising-handbook.md, PART I: AD KALEIDOSCOPE, lines 132-136
  confirmations: 2
  demonstrates: >-
    Run a winner until it stops working, not until you are bored; the viewer's threshold of new is far lower than the advertiser's (restated at line 235).
  anchor_at: "acq-advertising-handbook.md:132"
- id: C-advertising-002
  type: case
  name: >-
    Two advertisers, 100 ads each
  statement: >-
    A worked comparison: two advertisers each make 100 ads in a month; one makes 100 brand new ads, the other takes his top five ads from the month before and makes 100 versions of those five. The author says there is no question the one replicating winners wins the next month.
  why: >-
    80% of advertising results come from 20% of winners, so spending 80% of the effort on permutations of already proven ads produces more winners than starting from scratch every time.
  anchor: >-
    imagine you had two advertisers, both of whom made 100 ads. One made 100 brand new ads, while the other took his top five ads from the month before and made 100 versions of those five winners.
  source: >-
    acq-advertising-handbook.md, Part I, Kaleidoscope Ads, lines 182-186
  confirmations: 2
  demonstrates: >-
    The Ad Kaleidoscope's 80/20 split: 80% of effort into remixing and remaking winners, 20% into totally new ideas (repeated at lines 2462-2464).
  anchor_at: "acq-advertising-handbook.md:184"
- id: C-advertising-003
  type: case
  name: >-
    The $100,000 Skool ad put through the kaleidoscope
  statement: >-
    The highest converting Skool ad for several months - a man in a skool cap with question marks floating around his head - carried over $100,000 of spend on that single creative. After it was squeezed dry the team permuted it into variations the files name Top Skool Ad-Neon B..., -Plexus B..., -Purple B..., -Rainbow..., -Retro-B..., -White-B..., -Yellow-B..., plus versions with a different prop; each variation performed like the original.
  why: >-
    New does not mean start from zero, it means new to the viewer; permutations keep results at or near the original without fatiguing the audience.
  applies_when: >-
    You already have an ad that outperforms; the process only works on ads that exist.
  anchor: >-
    For example, this ad was the highest converting Skool ad for a few months. We spent over $100,000 on this single ad creative alone.
  source: >-
    acq-advertising-handbook.md, Part I, What The Ad Kaleidoscope Is, lines 215-239
  confirmations: 1
  demonstrates: >-
    Remixing Winners - new background/border and new props applied to a proven creative.
  anchor_at: "acq-advertising-handbook.md:215"
- id: C-advertising-004
  type: case
  name: >-
    Same Ad. New Speeds
  statement: >-
    The winning ad is re-exported at 1.1x to 1.2x playback speed without making the speaker's voice sound weird; the demonstration pair is the same frame of the same ad with the on-screen readout at 1.00 and at 1.20. The checklist version: play the entire spot at 1.1x.
  why: >-
    Sometimes faster or slower versions convert better, and even when they only convert the same they convert the same as a top performer, which makes them top performers too.
  applies_when: >-
    You already have a winning ad; this process only works if you have already made ads.
  anchor: >-
    Yes, you can literally just speed up or slow down the ad. Just run it at 1.1 to 1.2x the speed (without making the voice of the person in the ad sound weird).
  source: >-
    acq-advertising-handbook.md, Part I, Remixing Winners, lines 334-336 (also Ad Kaleidoscope Checklist, line 2512)
  confirmations: 2
  demonstrates: >-
    Remixing Winners: post-production permutation, the fastest kind to make.
  anchor_at: "acq-advertising-handbook.md:334"
- id: C-advertising-005
  type: case
  name: >-
    Same Ad. New Filters
  statement: >-
    The AGENCY OWNERS whiteboard ad (RETAINER -> PERFORMANCE, $1,500/mo -> $15,000/mo) is shown twice side by side, the right-hand copy in higher contrast than the original on the left. The checklist version: add a high-contrast black-and-white, sepia or social-media style filter so the video looks different from the original.
  why: >-
    The aim is only to change the way a proven ad looks, which can be done on a computer with no extra recording time.
  applies_when: >-
    You already have a winning ad.
  anchor: >-
    Think black and white, sepia, higher contrast, etc. You just want to change the way the ad looks. The ad on the right demonstrates higher contrast compared to the original on the left.
  source: >-
    acq-advertising-handbook.md, Part I, Remixing Winners, lines 338-344 (also Ad Kaleidoscope Checklist, line 2513)
  confirmations: 2
  demonstrates: >-
    Remixing Winners: post-production permutation of a winner.
  anchor_at: "acq-advertising-handbook.md:338"
- id: C-advertising-006
  type: case
  name: >-
    Same Ad. New Background/Border
  statement: >-
    The same Skool creative is shown plain and then framed by a dark border, with the note that the trim colour can be varied too; the checklist version swaps a white backdrop for a neon-green gradient border.
  why: >-
    A background colour swap or a thin trim is enough to make a proven ad read as different, and it costs no recording time.
  applies_when: >-
    You already have a winning ad.
  anchor: >-
    It can be as simple as changing the background color in the ad. You can also put a thin trim around the border of the ad (especially true with images).
  source: >-
    acq-advertising-handbook.md, Part I, Remixing Winners, lines 354-356 (also Ad Kaleidoscope Checklist, line 2514)
  confirmations: 2
  demonstrates: >-
    Remixing Winners: post-production permutation of a winner.
  anchor_at: "acq-advertising-handbook.md:354"
- id: C-advertising-007
  type: case
  name: >-
    Same Ad. New Fonts/Captions
  statement: >-
    The same AGENCY OWNERS ad is shown twice with the copy identical and only the text styling changed; the checklist version replaces the default subtitle font with bold comic-style caps, either for the first three words or throughout.
  why: >-
    Changing the text styling of a proven ad is a post-production change, the fastest class of permutation to produce.
  applies_when: >-
    You already have a winning ad.
  anchor: >-
    Ex: Replace the default subtitle font with bold, comic-style caps for the first three words (or in its entirety).
  source: >-
    acq-advertising-handbook.md, Ad Kaleidoscope Checklist, line 2515 (the pair is shown at Remixing Winners, lines 358-360)
  confirmations: 2
  demonstrates: >-
    Remixing Winners: post-production permutation of a winner.
  anchor_at: "acq-advertising-handbook.md:2515"
- id: C-advertising-008
  type: case
  name: >-
    Same Ad. New Headline
  statement: >-
    The text overlay of the winning ad, AGENCY OWNERS $1,500/mo to $15,000/mo Clients How we SWITCHED, is replaced with the headline of another winner, Looking To Partner With 5 AGENCY OWNERS, and nothing else changes; the checklist pair is Double Your Leads Fast to Steal Our 30-Day Leads Blueprint, keeping the rest the same.
  why: >-
    On some platforms a different headline can be put on top of the same ad, or into its top third, which yields a new ad out of proven footage.
  applies_when: >-
    You already have a winning ad.
  anchor: >-
    An ad with the text "AGENCY OWNERS $1,500/mo to $15,000/mo Clients How we SWITCHED" and an arrow pointing to another ad with the text "Looking To Partner With 5 AGENCY OWNERS".
  source: >-
    acq-advertising-handbook.md, Part I, Remixing Winners, lines 362-364 (also Ad Kaleidoscope Checklist, line 2516)
  confirmations: 2
  demonstrates: >-
    Remixing Winners: post-production permutation; a headline proven in one ad carried onto another.
  anchor_at: "acq-advertising-handbook.md:364"
- id: C-advertising-009
  type: case
  name: >-
    Same Ad. New Medium
  statement: >-
    A winning hook or headline is exported out of the video as a standalone static: the skool video hook becomes a set of four images reading WHAT'S YOUR EMAIL? (I WANT TO SEND YOU SOME FREE STUFF), and the $100M Leads Bribe video was likewise cut into photo ads that were themselves big winners. The checklist version turns the Value Anchor hook, Would you build your dream business for $1000? $100? Well how about free?, into an image.
  why: >-
    The static inherits a hook that has already been proven in video, and the author notes these photo versions were big winners too - kaleidoscope to the rescue.
  applies_when: >-
    You already have a winning ad.
  anchor: >-
    Ex: Take your hook from one ad, “Would you build your dream business for $1000? $100? Well how about free?” and turn it into an image.
  source: >-
    acq-advertising-handbook.md, Ad Kaleidoscope Checklist, line 2517 (shown at Remixing Winners, lines 376-378, and at Section IV #2, lines 2202-2204)
  confirmations: 3
  demonstrates: >-
    Remixing Winners: one winning creative converted into another medium.
  anchor_at: "acq-advertising-handbook.md:2517"
- id: C-advertising-010
  type: case
  name: >-
    Same Ad. New Format
  statement: >-
    The same footage is re-cut native to each placement on each platform; the checklist version re-edits the vertical selfie ad into a square 1:1 version for a different ad placement.
  why: >-
    Native placements improve performance big time.
  applies_when: >-
    You already have a winning ad.
  anchor: >-
    Make different versions native to each ad placement on each platform.
  source: >-
    acq-advertising-handbook.md, Part I, Remixing Winners, lines 380-382 (also Ad Kaleidoscope Checklist, line 2518)
  confirmations: 2
  demonstrates: >-
    Remixing Winners: post-production permutation of a winner.
  anchor_at: "acq-advertising-handbook.md:380"
- id: C-advertising-011
  type: case
  name: >-
    Same Hook. New Meat
  statement: >-
    The structure is shown as a diagram: the winning Hook 1 and CTA 1 are kept and Meat 1 is replaced by Meat 2, a body section already recorded; the checklist version splices in a different case-study clip behind the winning hook.
  why: >-
    The best-performing element, the hook, is preserved and paired with body footage that already exists, so a new ad costs no new recording.
  applies_when: >-
    You already have a winning ad and other ad meat already recorded.
  anchor: >-
    When you find your best performer, pair the winning hook with a different “ad meat” you’ve already recorded.
  source: >-
    acq-advertising-handbook.md, Part I, Remixing Winners, lines 392-394 (also Ad Kaleidoscope Checklist, line 2519)
  confirmations: 2
  demonstrates: >-
    Remixing Winners: recombining the parts of the Hook - Meat - CTA anatomy.
  anchor_at: "acq-advertising-handbook.md:392"
- id: C-advertising-012
  type: case
  name: >-
    Same Ad. New Visual Effects
  statement: >-
    Effects are added or changed inside the original ad - the before-and-after frame pair changes a large white arrow to a black one - and the effects placed earliest, in the hook, matter most because that is what most people see. The checklist version drops a BOOM motion-graphic sticker over the revenue figure as it appears, or shows visual proof right after a number-driven hook.
  why: >-
    The hook is what most viewers see first, so effects there carry the most weight.
  applies_when: >-
    You already have a winning ad.
  anchor: >-
    You can add or change the visual effects in the original ad. You can add doodads and wizbangs to your heart’s desire.
  source: >-
    acq-advertising-handbook.md, Part I, Remixing Winners, lines 396-398 (also Ad Kaleidoscope Checklist, line 2520)
  confirmations: 2
  demonstrates: >-
    Remixing Winners: post-production permutation of a winner.
  anchor_at: "acq-advertising-handbook.md:396"
- id: C-advertising-013
  type: case
  name: >-
    New Clone
  statement: >-
    The same ad is simply recorded again in a new session; the demonstration pair is the same man, same cap, same price sign, framed slightly closer to the camera. The checklist version keeps gestures, script and background and changes clothing and lighting.
  why: >-
    Like fingerprints, no two recording sessions are the same: time of day, weather, lighting and sound create tiny variations that make the ad different enough to convert like new.
  applies_when: >-
    You already have a winning ad and can record again.
  anchor: >-
    You literally record the same ad again in a new session. Like fingerprints, no two recording sessions will be exactly the same.
  source: >-
    acq-advertising-handbook.md, Part I, Remaking Winners, lines 433-435 (also Ad Kaleidoscope Checklist, line 2524)
  confirmations: 2
  demonstrates: >-
    Remaking Winners: changing real-world variables instead of digital ones, which takes longer but keeps a winner alive for months or years.
  anchor_at: "acq-advertising-handbook.md:433"
- id: C-advertising-014
  type: case
  name: >-
    New Props
  statement: >-
    Props are added, swapped or removed while the winning script stays intact - in the shown pair the author removed the banana prop from the Flying Prop ad - and the category includes costumes, hair styles and accessories. The checklist version swaps a stack of cash for a silver platter holding signup sheets.
  why: >-
    A prop change creates significant variation while keeping the same winning script, so the ad stays likely to convert.
  applies_when: >-
    You already have a winning ad and can record again.
  anchor: >-
    This creates significant variation while allowing for the same winning script... so it stays likely to convert. In the example, I removed the banana prop.
  source: >-
    acq-advertising-handbook.md, Part I, Remaking Winners, lines 445-447 (also Ad Kaleidoscope Checklist, line 2525)
  confirmations: 2
  demonstrates: >-
    Remaking Winners; the prop here is the banana of Section IV Ad Framework #1 Flying Prop.
  anchor_at: "acq-advertising-handbook.md:445"
- id: C-advertising-015
  type: case
  name: >-
    New Examples
  statement: >-
    The same ad is recorded again with a different example in the hook: the first version opens on last month's lowest performer on the leaderboard at $4,664, the next month the number and the person's name are swapped for $6,760 and the rest of the ad stays as it was - and it worked again. The checklist version is $4497/mo Kyle to $6398/mo Sarah.
  why: >-
    Only the example changes, so the winning script and structure are preserved while the ad becomes new to the viewer.
  applies_when: >-
    You already have a winning ad and a fresh example to put in it.
  anchor: >-
    In this ad, I start with the last month’s lowest performer on the leaderboard. The next month, I swapped the number and the name of the person. The rest of the ad remained the same.
  source: >-
    acq-advertising-handbook.md, Part I, Remaking Winners, lines 449-451 (also Ad Kaleidoscope Checklist, line 2526)
  confirmations: 2
  demonstrates: >-
    Remaking Winners; the ad being permuted is Section III Ad Framework #4 Underdog.
  anchor_at: "acq-advertising-handbook.md:449"
- id: C-advertising-016
  type: case
  name: >-
    New Setting
  statement: >-
    The same winning script is recorded in a different place - on the left the author records in his studio, on the right the same script in his office - and the section lists the beach, a car and an office as interchangeable settings. The checklist version films the ad on a sidewalk instead of inside the office.
  why: >-
    A different place makes the same ad new again.
  applies_when: >-
    You already have a winning ad and can record again.
  anchor: >-
    On the left, I record in my studio. On the right, I record the same script in my office.
  source: >-
    acq-advertising-handbook.md, Part I, Remaking Winners, lines 463-465 (also Ad Kaleidoscope Checklist, line 2527)
  confirmations: 2
  demonstrates: >-
    Remaking Winners: changing a real-world variable while keeping the script.
  anchor_at: "acq-advertising-handbook.md:463"
- id: C-advertising-017
  type: case
  name: >-
    New Talent
  statement: >-
    The same ad is recorded with different people, chosen to look like the buyers: if the product is for midwestern men aged 18-25, more versions are made with different 18-25 year old midwestern men; to get more women, use more women. The author calls this a wildly underutilized variation style. The checklist version has someone else deliver the script to attract an avatar that looks like them.
  why: >-
    Talent that looks like the people who buy raises the chance the avatar sees the ad as being for them.
  applies_when: >-
    You already have a winning ad and can find, coordinate and direct different talent.
  anchor: >-
    For example, if you make stuff for midwestern men ages 18–25 then... then make more versions with different 18–25 year old midwestern men!
  source: >-
    acq-advertising-handbook.md, Part I, Remaking Winners, lines 467-469 (also Ad Kaleidoscope Checklist, line 2539)
  confirmations: 2
  demonstrates: >-
    Remaking Winners; matches the Similar Avatar must-have of the Best Ad Framework Checklist.
  anchor_at: "acq-advertising-handbook.md:467"
- id: C-advertising-018
  type: case
  name: >-
    New Combination
  statement: >-
    Several variables are changed at once - a new prop with a new post-production effect, or new talent saying the same script with a new filter or headline. The checklist version shoots the ad on a rooftop (new setting) with a bright red megaphone (new prop) and overlays comic-book captions (post-production font change).
  why: >-
    Combinations give endless permutations of the same winner, which is where the leverage is: the most effort goes into the thing most likely to win.
  applies_when: >-
    You already have a winning ad.
  anchor: >-
    You can do a new prop coupled with a new post-production effect. You can have new talent say the same script with a new filter or headline.
  source: >-
    acq-advertising-handbook.md, Part I, Remaking Winners, lines 479-483 (also Ad Kaleidoscope Checklist, line 2540)
  confirmations: 2
  demonstrates: >-
    Remaking and Remixing combined; milking a winner for all it's got.
  anchor_at: "acq-advertising-handbook.md:479"
- id: C-advertising-019
  type: case
  name: >-
    Ad Framework #1: Personal Testimonial/Origin Story
  statement: >-
    A shaky selfie video headlined 191 SIGNUPS IN 19 DAYS: the author walks a new gym in a residential, sketchy neighbourhood, names every flaw out loud as a damaging admission (bars on the windows, stairs people are scared to climb, a room that looks like an apartment), keeps the loop open with repeated curiosity lines, then snaps it shut on a stack of $500 bills of signed contracts and the lesson that you can sell wherever you want. The apply instructions: wild promise in five seconds, an obviously wrong environment, a rapid problems tour, more stacked negatives, overwhelming proof, one plain connecting sentence, soft CTA.
  why: >-
    Building mystery also eliminates the implied objections about location, neighbourhood, gym size, price point and age; a big promise on a fast timeline, made believable by a setting that contradicts it, is answered by a massive payoff of proof inside the ad itself.
  applies_when: >-
    Any business can name a situation that would make it less than ideal for a customer to get the outcome.
  anchor: >-
    So I’m opening this gym in kind of the middle of nowhere. It doesn’t really look like, it’s like a residential kind of neighborhood, kind of sketchy, (DAMAGING ADMISSION) but I wanna show you something (CURIOSITY).
  source: >-
    acq-advertising-handbook.md, Part II Section I, Ad Framework #1: Personal Testimonial/Origin Story, lines 586-672
  confirmations: 2
  demonstrates: >-
    One gigantic open loop closed by proof; damaging admission; anti-proof stacking; the ad framework the author calls the one that started it all (referenced again at lines 1288 and 2466).
  anchor_at: "acq-advertising-handbook.md:640"
- id: C-advertising-020
  type: case
  name: >-
    Ad Framework #2: Prop Comedy
  statement: >-
    A Dollar Shave Club style ad scripted one phrase at a time, each phrase paired with a prop and a mini-setting and filmed as its own clip: Are you a gym owner? (CALL OUT) - Do you want high ticket online clients? (DREAM OUTCOME) - Do you want this in as little as 30 days? (SPEED) - It's possible. We're already doing it. (PERCEIVED LIKELIHOOD) - then click the link, download the case studies, schedule a call time (CTA). Clips are joined with whip-cuts and camera swings, upbeat royalty-free music and huge high-contrast captions, ending on a CTA card frozen for a full second with the spokesperson pointing at it.
  why: >-
    The first scene is already in the gym because the ad targets gym owners: the avatar should immediately see the background, clothing and spokesperson as like them. These ads do not try to do too much - the point is to get the right person to click with the right intent.
  applies_when: >-
    Write three to four Yes prompts that hit dream outcome, speed, ease and proof, each three to five seconds.
  anchor: >-
    Do you want high ticket online clients? (DREAM OUTCOME) Do you want this in as little as 30 days? (SPEED)
  source: >-
    acq-advertising-handbook.md, Part II Section I, Ad Framework #2: Prop Comedy, lines 682-734
  confirmations: 1
  demonstrates: >-
    Call out the avatar; the value-equation questions (dream outcome, speed, ease, proof); paired verbal and visual hooks; one clear CTA.
  anchor_at: "acq-advertising-handbook.md:714"
- id: C-advertising-021
  type: case
  name: >-
    Ad Framework #3: Emotional Avatar Testimonial
  statement: >-
    Two early Gym Launch customers, Cale and Maggie, were given six points to hit - life before personally, life before professionally, what skepticism they had, why they acted anyway, life after personally, life after professionally. The cut opens on them in front of their gym, jumps within half a second to an empty gym with emotional music, opens on We were two months from shutting our doors (HOOK), stacks pains (31 members, about four grand a month, a second pregnancy, a second job, split shifts), marks the turning point, then the wins (31 to over 200 members, full staff hired, stepped away in four and a half months), a damaging admission, a reason why, and one CTA to download the 11 frameworks. The stated rhythm: PERSONAL STAKES to PERSONAL PAIN to PROFESSIONAL PAIN to TURNING POINT to WORK to PROFESSIONAL GOOD to PERSONAL GOOD to ADDRESS SKEPTICISM to REASON WHY to CTA.
  why: >-
    No testimonial has outperformed it in the company's history; talent that looks and talks like the avatar signals the ad is for them (it also brought in more married couple owners), and the honest disclaimer boosts credibility and lowers skepticism.
  anchor: >-
    I asked them to film a testimonial and gave them six points to hit: 1) what was life like before personally and 2) professionally.
  source: >-
    acq-advertising-handbook.md, Part II Section I, Ad Framework #3: Emotional Avatar Testimonial, lines 780-864 (the card is duplicated at lines 754-778 and counted once)
  confirmations: 1
  demonstrates: >-
    Six-question testimonial brief; avatar-matched proof; pain stack before dream outcome; speed and ease against the too slow / too hard objection; damaging admission; one crystal-clear CTA.
  anchor_at: "acq-advertising-handbook.md:760"
- id: C-advertising-022
  type: case
  name: >-
    100+ variations of one testimonial
  statement: >-
    The Cale and Maggie creative was run in over 100 variations, among them dozens of different music tracks remixed behind the same footage, and all of them performed.
  why: >-
    A winner is multiplied rather than replaced; permutations of a proven piece of creative keep converting.
  anchor: >-
    We easily ran 100+ variations of this one piece of creative alone. And they all performed.
  source: >-
    acq-advertising-handbook.md, Part II Section I, Ad Framework #3, lines 784 and 810 (line 784 is duplicated at line 758 and counted once)
  confirmations: 2
  demonstrates: >-
    The Ad Kaleidoscope applied to a winning testimonial - remixing in post-production.
  anchor_at: "acq-advertising-handbook.md:758"
- id: C-advertising-023
  type: case
  name: >-
    Ad Framework #4 Show Don't Tell
  statement: >-
    Selling make your gym more profitable, the author asked his community to send videos of their most packed class times and ran them as ads. The winner is a packed gym clip with bold high-contrast text across the top, 171 NEW SIGNUPS AT $500, no ad copy at all - the ad copy section reads no telling, all showing - and a purely visual scan-me CTA button.
  why: >-
    The closer a prospect can approximate the proof to their own situation the lower the risk and the more compelling it is; proof works better than just about anything else, and if the proof is clear enough it needs no narration - non-verbal clips also tend to get more organic reach.
  applies_when: >-
    The dream outcome can be filmed by existing customers who match the target avatar.
  anchor: >-
    I sold “make your gym more profitable”. The way to show that was a packed class. So I asked my community to send me videos of their most packed times.
  source: >-
    acq-advertising-handbook.md, Part II Section I, Ad Framework #4 Show Don't Tell, lines 874-925
  confirmations: 1
  demonstrates: >-
    Show what you tell; frame the shot with the fewest possible words and numbers in a high-contrast colour; many people moving at once (better still in unison) stops the scroll; a non-verbal ad needs a non-verbal CTA.
  anchor_at: "acq-advertising-handbook.md:880"
- id: C-advertising-024
  type: case
  name: >-
    Don't say it, show it - three swaps
  statement: >-
    Three claims turned into filmed proof: instead of saying you can get their phone to ring off the hook, show their packed calendars; instead of saying you can fill their gym, show them a line around the block; instead of saying you fix their credit, show them reacting to paying off their last loan and getting a card in the mail with ten times their old limit.
  why: >-
    The more the ad shows viewers their own dream outcome, the lower the perceived risk.
  anchor: >-
    Ask current customers who match your target avatar to film their “dream outcome proof moment”.
  source: >-
    acq-advertising-handbook.md, Part II Section I, Ad Framework #4, How To Apply This Ad Framework, line 909
  confirmations: 1
  demonstrates: >-
    Show Don't Tell carried out of the gym niche into other businesses.
  anchor_at: "acq-advertising-handbook.md:909"
- id: C-advertising-025
  type: case
  name: >-
    Ad Framework #5 Long Term Result
  statement: >-
    From the one year later campaign: a gym owner filmed in his own gym beside a whiteboard, headline showing 93 to 321 members and 4x client lifespan. One pain sentence opens (My profit was $0... I was working 60 plus hours a week), two or three more advanced-owner pains follow, then a dated decision (we joined Gym Launch in March of 2017), a fast win (tripled revenue within the first few months) and a big win ($83,000 a month, 321 members, attrition under 2%, six full-time staff at $40-75k), closing on the customer's own thanks as an implicit CTA. The campaign's cost per call ran above the KPIs and the author nearly shut it off.
  why: >-
    Don't optimize for CAC, optimize for LTV:CAC - these calls and customers cost more to acquire but paid more, stayed longer, got better results and referred friends; deeper, more specific metrics attract a more advanced avatar, and no one else talks to the advanced customer for fear of ostracizing the rest.
  applies_when: >-
    You want the exact customer (the advanced one), not just the genre of customer.
  anchor: >-
    This campaign taught me an important lesson: don’t optimize for CAC, optimize for LTV:CAC.
  source: >-
    acq-advertising-handbook.md, Part II Section I, Ad Framework #5 Long Term Result, lines 941-1026
  confirmations: 1
  demonstrates: >-
    Speak the language only the upper echelon understands; two-tier proof (Fast Win and Big Win); soft benefits alongside the money numbers; peer endorsement as the CTA.
  authors_caveat: >-
    Poor beginner customers will buy get rich quick offers, but then you are only selling to poor beginners; this style does not optimize for cheap leads.
  anchor_at: "acq-advertising-handbook.md:951"
- id: C-advertising-026
  type: case
  name: >-
    Ad Framework #1 Looking For 5 Avatars...
  statement: >-
    Filmed in front of a whiteboard: the hook qualifies by revenue (a local lead gen agency in one niche doing $15,000 a month or more in recurring revenue) and by ambition, then states right now I'm looking for five agencies that I can help do exactly that. The meat is us versus them (most people who help agencies made their money helping agencies, not dominating a niche), one proof number ($98.5 million in a single niche of gyms), a limited-partner reason why, and a risk-split offer - if what I help you with doesn't make you a red cent, then I don't get paid. The CTA routes through an application and a call from the executive assistant. The template given: I'm looking for five (AVATAR) who are looking to (OUTCOME) but don't want to (BIGGEST PAIN POINT) so that I can (REASON WHY). Here's my (PROOF). If interested, (KEEP WATCHING).
  why: >-
    One of the most classic direct response ads of all time - it worked 70 years ago, works today and will likely work tomorrow; naming who you are not looking for and giving a believable reason for taking only a few clients raise credibility further.
  applies_when: >-
    Use these if you are just starting to run paid ads or monetize your audience; it also works well for organic audiences and is the author's usual first ad when launching something new.
  anchor: >-
    I’m looking for five (AVATAR) who are looking to (OUTCOME) but don’t want to (BIGGEST PAIN POINT) so that I can (REASON WHY).
  source: >-
    acq-advertising-handbook.md, Part II Section II, Ad Framework #1 Looking For 5 Avatars..., line 1152 (full breakdown lines 1062-1170)
  confirmations: 2
  demonstrates: >-
    Call out plus limited-slots reason why; the educational (ADucational) setting for complex or higher ticket offers; risk reversal through performance compensation.
  anchor_at: "acq-advertising-handbook.md:1152"
- id: C-advertising-027
  type: case
  name: >-
    The same looking for template as a gym image ad
  statement: >-
    An older Facebook image ad from the author's gym days runs the same template in a consumer niche: WE ARE LOOKING FOR 30 LOCAL WOMEN AND MEN TO LOSE WEIGHT AND TRANSFORM THEIR BODIES FOR FREE IN 6 WEEKS, followed by an apply link, a list of what they receive (customized food preparation instructions, personal eating plan, accountability coach and group, six weeks of unlimited training, a support group), one condition in exchange - permission to share the transformation - and the apply link repeated.
  why: >-
    The author digs it up to prove the template is not bound to one industry and works as a plain image with copy.
  anchor: >-
    WE ARE LOOKING FOR 30 LOCAL WOMEN AND MEN TO LOSE WEIGHT AND TRANSFORM THEIR BODIES FOR FREE IN 6 WEEKS.
  source: >-
    acq-advertising-handbook.md, Part II Section II, Ad Framework #1, lines 1074-1094
  confirmations: 1
  demonstrates: >-
    Looking For # Avatars ported from a B2B agency offer to a B2C weight loss offer; the number, the avatar, the outcome and the timeline are the only slots that change.
  anchor_at: "acq-advertising-handbook.md:1078"
- id: C-advertising-028
  type: case
  name: >-
    Ad Framework #2: New vs. Old
  statement: >-
    An ADucational whiteboard ad: call out (Lead gen agency owners for local businesses), then a big claim with details - how we went from retainer clients at $1,500 a month in the gym niche to performance clients at $15,000 a month in the same niche. The meat explains the old model's mechanics (price versus value; the moment value dips below price they cancel), reveals the new way anchored to one simple metric ($100 per person who walks in the door), runs a hypothetical that does the math (on day 30 you don't ask them to double the retainer, you double the ad spend and they say yes), adds one proof line, a risk-reversed offer, and a CTA that previews the process.
  why: >-
    Marketing and sales have the same objective in different media - educate the prospect enough to make a decision; ADucational ads build brand and drive sales at once, and a brand-new advertiser is judged on the quality of the information rather than on an existing brand.
  applies_when: >-
    It works especially well with more advanced/complex products or services.
  anchor: >-
    What I wanna show you in the next couple seconds is how we went from retainer clients at $1,500 a month in the gym niche to performance clients at $15,000 a month in the same niche
  source: >-
    acq-advertising-handbook.md, Part II Section II, Ad Framework #2: New vs. Old, lines 1180-1274
  confirmations: 1
  demonstrates: >-
    Old way versus new way; attribute the prospect's pains to their outdated model; anchor the new mechanism to one simple metric; a hypothetical as a proxy for proof; a single proof line.
  anchor_at: "acq-advertising-handbook.md:1216"
- id: C-advertising-029
  type: case
  name: >-
    Ad Framework #3: Why You Will Never
  statement: >-
    Whiteboard ad titled The 4 WARNING SIGNS Your Agency Will NEVER Pass $1M/Yr. Call out (Agency owners), one authority line (68 companies taken past a million dollars in four years, over a hundred million in sales in a single niche), then four specific thresholds - lifetime value under $10,000, average revenue per client under $2,500 a month, gross margin under 80%, payback period over 30 days - each explained in the prospect's own arithmetic, the pressure released by naming a model that reverses all four, then a CTA to a seven-minute video and a 15-minute call.
  why: >-
    The framework capitalizes on understanding the prospect's problem better than they do; each added statistic builds pressure until the prospect thinks this person named a bunch of stats about my business and might be able to fix it. Expertise is demonstrated by how specifically you can describe the problem.
  applies_when: >-
    Any niche - list the problems as specifically as possible, build pressure, then resolve it with a CTA.
  anchor: >-
    Ex: LTV under $10k, ARPC under $2.5k, gross margin below 80%, payback over 30 days. Each number makes owners think, “This is me”.
  source: >-
    acq-advertising-handbook.md, Part II Section II, Ad Framework #3: Why You Will Never, line 1370 (full breakdown lines 1284-1374)
  confirmations: 1
  demonstrates: >-
    The inversion of Ad Framework #1 of Section I - instead of achieving the outcome despite terrible circumstances, the circumstances are named as the reason the prospect has not achieved it.
  anchor_at: "acq-advertising-handbook.md:1370"
- id: C-advertising-030
  type: case
  name: >-
    Naming the mechanism reverse royalty
  statement: >-
    The new model is named the reverse royalty model rather than the descriptive Pay Per Show, because the obvious name gave the mechanism away; the name is non-obvious, explained in one sentence, and the explanation itself is held back for the lead magnet.
  why: >-
    The obvious name was too obvious and killed the curiosity that makes the prospect click.
  anchor: >-
    I had to come up with “reverse royalty” because “Pay Per Show” was too obvious and killed the curiosity.
  source: >-
    acq-advertising-handbook.md, Part II Section II, Ad Framework #3, How To Apply This Framework, line 1372
  confirmations: 1
  demonstrates: >-
    Introduce your new solution under a non-obvious name and explain what it is in one sentence.
  anchor_at: "acq-advertising-handbook.md:1372"
- id: C-advertising-031
  type: case
  name: >-
    Ad Framework #4: The "North Star"
  statement: >-
    The ad picks one predictive metric - lifetime value, presented the way neck and wrist thickness predict body fat - and builds a hierarchy the prospect can place themselves in: under $5,000 LTV you will never crack $100-300k a year; nearing $10,000 you crack a million; $15,000 opens the $3 million range; over $20,000 makes a million a month realistic. The plateau is attributed to the old retainer model, the reverse royalty model is offered as the way out, and the CTA is a seven-minute video then a 15-minute call.
  why: >-
    A single number is one of the biggest predictors of where an agency will plateau, so the prospect locates themselves on the ladder and sees their ceiling as caused by their current model; the dream outcomes are listed precisely to show they are out of reach right now.
  anchor: >-
    Ex: “under $5k and you’ll never crack $300k a year; $10k opens $1 million; $15k unlocks $3 million; $20k+ makes $1 million-a-month realistic.”
  source: >-
    acq-advertising-handbook.md, Part II Section II, Ad Framework #4: The "North Star", line 1472 (full breakdown lines 1384-1477)
  confirmations: 1
  demonstrates: >-
    Pick a predictive metric, predict the pain from it, attribute the pain to the old way, then sell the new mechanism as the release valve.
  anchor_at: "acq-advertising-handbook.md:1472"
- id: C-advertising-032
  type: case
  name: >-
    Eight gym-music complaints
  statement: >-
    To show what specificity means, the author lists eight things only a gym owner would have lived through, all of them about music alone: one member saying the music is too loud five minutes after another said it was too quiet; one asking for more variety right after another asked for last week's playlist; one asking for clean versions while another wants the real music; the mic battery dying and having to shout over the music; realising members cared more about the playlists than the workouts; a cease and desist for playing an unlicensed personal playlist in a commercial setting; trainers' iPhones ringing or alarming over the speakers; ad breaks in the middle of a song because a trainer's account was not premium.
  why: >-
    All of these are just about the music in a gym and the reader might not have thought of them - but a gym owner would have; that is the level of detail that makes the prospect feel the copy is describing their life.
  anchor: >-
    Members saying the music is too loud while five minutes earlier a member complained it was too quiet.
  source: >-
    acq-advertising-handbook.md, Part II Section II, Ad Framework #4, lines 1394-1415
  confirmations: 1
  demonstrates: >-
    Be specific - list the specific pains they experience; think moments, not categories.
  anchor_at: "acq-advertising-handbook.md:1396"
- id: C-advertising-033
  type: case
  name: >-
    Ad Framework #5: No BS Selfie
  statement: >-
    A very short low-fi selfie shot while walking, a big house and a nice car in the background. If-then pain hook (Agency owners, if you can't crack $10,000 in lifetime value per customer, you're never gonna hit the million dollar run rate you want), the mechanism named but not explained (a reverse royalty model), one proof line juxtaposing age (we've had $6 million-plus agencies for kids in their twenties), then swipe up.
  why: >-
    Constraining the time forces the words down to only what matters; the setting does the selling, and the ad sells the next step and nothing more.
  applies_when: >-
    These ads rely on additional information later in the funnel - think of it as an ad for your lead magnet rather than an ad to sell, and they work well at the top of the funnel.
  anchor: >-
    Agency owners, if you can’t crack $10,000 in lifetime value per customer, you’re never gonna hit the million dollar run rate you want. (HOOK)
  source: >-
    acq-advertising-handbook.md, Part II Section II, Ad Framework #5: No BS Selfie, lines 1488-1549
  confirmations: 1
  demonstrates: >-
    Movement and setting as credibility; name the mechanism without explaining it; one proof line that answers the prospect's doubt.
  authors_caveat: >-
    The author used the wealthy-setting style only for a brief stint because he decided he did not want that kind of brand, while noting it is effective.
  anchor_at: "acq-advertising-handbook.md:1523"
- id: C-advertising-034
  type: case
  name: >-
    Proof that someone worse off got a better result
  statement: >-
    The line the author says did the heavy lifting in the No BS Selfie ad was that kids in their twenties had built $6 million-plus agencies; he learned the move selling weight loss, where the meal plan was pitched as so easy that kids and people who couldn't speak English followed it, before asking the prospect whether they could too.
  why: >-
    The age juxtaposition implies that bigger, older agencies can do even better, and the preframe makes the prospect think if they could do it, so can I - with that preframe, how could they say no.
  anchor: >-
    I used to say our meal plan was “so easy to use kids and people who couldn’t speak English followed it”—before asking if the prospect could.
  source: >-
    acq-advertising-handbook.md, Part II Section II, Ad Framework #5, line 1549
  confirmations: 1
  demonstrates: >-
    Show proof that someone worse than them got results better than them; perceived likelihood and ease.
  anchor_at: "acq-advertising-handbook.md:1549"
- id: C-advertising-035
  type: case
  name: >-
    Ad Framework #1: Trending Format
  statement: >-
    A solo clip shot to look like an organic podcast reel - mic to the mouth, the look of a clip from a show rather than an ad. It opens on a recent surprising discovery (we launched the Skool Games a little over two weeks ago and I was surprised at how much people were making so quickly), stacks speed and scale in one line (the top ten making $10-40k a month, starting at zero on the first of the month), then removes the classic objections with proof - hundreds have made their first dollar online, eight models that need no audience and no expertise - and ends on a card, CLICK THE LINK TO START FREE. The alternative given: a real podcast where the host asks the questions you asked them to ask.
  why: >-
    Popular video formats are popular for a reason, so the ad borrows the format the feed is already rewarding; organic is always ahead of paid because of the volume and speed of testing, so to see where ads will be in six to twelve months look at where organic is today.
  applies_when: >-
    Can be modeled across any niche selling any product or service; model the specific format directly while it is still in, or model the larger concept by taking the best organic hooks into your ads.
  anchor: >-
    So we launched the Skool Games a little over two weeks ago, and I was surprised at how much people were making so quickly, (HOOK)
  source: >-
    acq-advertising-handbook.md, Part II Section III, Ad Framework #1: Trending Format, lines 1593-1668
  confirmations: 1
  demonstrates: >-
    Native format as the visual hook; speed and scaled proof in one line; perceived likelihood and ease; always include both the big outcomes and the average ones.
  anchor_at: "acq-advertising-handbook.md:1630"
- id: C-advertising-036
  type: case
  name: >-
    Ad Framework #2: Value Anchor
  statement: >-
    An offer-centric ad with two stacks and two price drops. Visual: a three-second keyframe of cash fanned out on a big red background with the hook repeated as screen-filling text. Copy: Would you pay a thousand dollars to get the business of your dream in 30 days? - how about a hundred dollars? - how about free? Then the offer on a fast timeline (build and monetize a community on one platform in 30 days), a second anchor against market pricing (people charge a thousand, $5,000, $10,000 for this training) dropped to free, then a variable reward that makes it better than free (the top ten Skools flown to Vegas for a full day with the author), then click the link to join for free. The structure given: How much would you pay for DREAM OUTCOME? $XXX, $XX, $X? - explain offer - anchor at the marketplace rate - give it free - add a last-minute incentive - CTA.
  why: >-
    Free still has costs, so the outcome has to be made valuable before it is given away; the descending questions set a value in the viewer's mind and make free feel like an unexpected windfall instead of a marketing cliche.
  applies_when: >-
    Any niche; alternatively ask how much it would be worth to make something bad go away.
  anchor: >-
    Would you pay a thousand dollars to get the business of your dream in 30 days?
  source: >-
    acq-advertising-handbook.md, Part II Section III, Ad Framework #2: Value Anchor, line 1717 (full breakdown lines 1678-1747)
  confirmations: 2
  demonstrates: >-
    Price anchoring and price drop; competitor pricing as proof the free thing does not suck; a variable incentive that turns zero cost into potential gain.
  anchor_at: "acq-advertising-handbook.md:1717"
- id: C-advertising-037
  type: case
  name: >-
    Ad Framework #3: Bribe
  statement: >-
    A pattern-interrupt ask with a prop swung in from behind the back: Real quick, can I get your email address? Because I wanna send you a thousand dollars of free stuff straight to your inbox. Then the mechanism and dream outcome (build and monetize a community through Skool), the market-price anchor ($1,000, $5,000, $10,000) dropped to absolutely free, a reason why (I just became the co-owner of Skool), and a CTA that mirrors the hook.
  why: >-
    It is a killer offer-driven ad driving to a page that does the heavy lifting: shorter, proof-heavy creatives worked best, needing only to earn the click and letting the page and the video sales letter close. Making the CTA the same as the hook keeps the ad congruent - if they stayed because of the hook, they act because of it too.
  anchor: >-
    Real quick, can I get your email address? Because I wanna send you a thousand dollars of free stuff straight to your inbox.
  source: >-
    acq-advertising-handbook.md, Part II Section III, Ad Framework #3: Bribe, lines 1765-1834
  confirmations: 1
  demonstrates: >-
    Ask for contact information with a pattern interrupt; state the cash value of the free thing; anchor against real market pricing; give a reason why for the bonus; CTA congruent with the hook.
  anchor_at: "acq-advertising-handbook.md:1802"
- id: C-advertising-038
  type: case
  name: >-
    250 ads in one day, then 200+ variations of the winner
  statement: >-
    The Bribe framework came out of the first Skool Games shoot: about 250 ads in one day varying hooks, meat, CTAs, background colours and shirts. Once the winner emerged from that day the author cut another 200-plus variations of that winner alone, and has reused its meat hundreds of times.
  why: >-
    People romanticize random hits, but volume negates luck - the real winners are built by deliberate work, and there is zero magic in it.
  anchor: >-
    It came from my first Skool Games shoot: one brutal day cranking out ~250 ads. Different hooks. Meat. CTAs.
  source: >-
    acq-advertising-handbook.md, Part II Section III, Ad Framework #3, lines 1769-1775 (restated at line 2462)
  confirmations: 2
  demonstrates: >-
    Identify winners out of volume, then remix and remake them; only amateurs reinvent the wheel.
  anchor_at: "acq-advertising-handbook.md:1769"
- id: C-advertising-039
  type: case
  name: >-
    Ad Framework #4: Underdog
  statement: >-
    A large white $4,664 on a blank black background with scroll motion and a visual effect, then the hook: that is what Kyle, the lowest person on the 20-person Skool Games leaderboard, built halfway through. The meat refuses the big names on purpose - I don't wanna talk about Evelyn, who's made $43,000, or Eddie, at about $30,000 a month - and circles back to what about like four or five thousand a month, adds a reason why (just became the largest investor in Skool, so the biggest games ever), and ends on a free 14-day trial. The author repeated the style several times, changing only the person described, and it outperformed every time.
  why: >-
    People already know earning an income is cool; the issue is that they don't believe they can do it, so a modest, believable number squashes that objection up front, while naming the bigger outcomes still engages the high achievers - you attract all potential buyers without setting crazy expectations.
  anchor: >-
    $4,664 per month in recurring revenue (HOOK). That’s what Kyle, the last person, the lowest person on the 20 leaderboard that we have for the Skool Games just halfway through has been able to build. (PROOF)
  source: >-
    acq-advertising-handbook.md, Part II Section III, Ad Framework #4: Underdog, lines 1850-1910
  confirmations: 1
  demonstrates: >-
    Lead with the floor rather than the ceiling; stack proof upward then pivot back to the underdog; give a big reason why so the promotion reads as a big deal.
  anchor_at: "acq-advertising-handbook.md:1884"
- id: C-advertising-040
  type: case
  name: >-
    Ad Framework #5: Challenge With Prize
  statement: >-
    Six months into the Skool Games the team asked what would kick things up a notch and landed on giving a Cybertruck to the winner. The ad is shot in front of the Acquisition.com headquarters with a metal ball thrown against the truck glass in the first second: This is a Cybertruck. This is a hundred grand. And in the next 30 days I'm gonna be giving away one to one person who's watching this ad right now. One tracked condition to win (build the largest community on Skool in 30 days), last month's winner at $40-50k monthly recurring revenue, likelihood and ease (one in two people who start a paid community make their first dollar online, average $1,360 a month, a step-by-step walkthrough and weekly live Q&A with 200-300 people), a free start, and a screen recording of the actual opt-in page.
  why: >-
    You don't need a Cybertruck to make marketing compelling, but it helps; the prize should be huge for your audience - the broader the audience the better money, cars and vacations work, while for a gym owner re-outfitting their old gym with new equipment would be even more compelling.
  anchor: >-
    This is a Cybertruck. This is a hundred grand. And in the next 30 days I’m gonna be giving away one to one person who’s watching this ad right now. (HOOK)
  source: >-
    acq-advertising-handbook.md, Part II Section III, Ad Framework #5: Challenge With Prize, lines 1926-2019
  confirmations: 1
  demonstrates: >-
    Give away something insane on a short deadline; prove a peer already won it; one simple tracked metric of entry; show how you'll help them win; make not winning valuable too; show what happens the moment they click.
  anchor_at: "acq-advertising-handbook.md:1959"
- id: C-advertising-041
  type: case
  name: >-
    Ad Framework #1: Flying Prop
  statement: >-
    Filmed in the author's old kitchen when the team threw a banana at him as a joke: he catches and mashes it on camera, then ties it to the offer with a one-liner (the book is nutritious and will make you money unlike bananas, but the launch event will be bananas), piles on the investment (over a million dollars spent on the event), teases a secret project four years in the making given to everyone live, adds a reason why (the day after his birthday), and closes with click the link to register.
  why: >-
    Stuff that moves generally beats stuff that doesn't, and real stuff that moves often beats computer stuff that moves; the whole ad is a daisy chain of open loops with only one action available to close them, which serves both campaign objectives - registering and showing up.
  anchor: >-
    Daisy-chained open loops: The banana→The money spent on the event→My birthday→Giving a secret away.
  source: >-
    acq-advertising-handbook.md, Part II Section IV, Ad Framework #1: Flying Prop, lines 2057-2120
  confirmations: 1
  demonstrates: >-
    Catch a flying prop for movement; tie the prop to the offer with a joke; investment as an approximation of value; keep the loop open until the next step. The author advises keeping a shed or closet of props.
  anchor_at: "acq-advertising-handbook.md:2067"
- id: C-advertising-042
  type: case
  name: >-
    Ad Framework #2: Bribe ($100M Leads launch)
  statement: >-
    Pointing straight at the viewer: Real quick question, what's your email address? The reason I ask is because what I wanna do is send you a gazillion dollars of free stuff. The meat is stakes rather than specifics - the biggest entrepreneur event of the season, a book two years in the making released live, a secret project of four years never mentioned publicly - and the CTA keeps the loop open with a value range instead of a name: more than a gift card and less than a Tesla, and everyone who shows up gets one.
  why: >-
    Curiosity and open loops plus stakes drive the click, and the page then does its job of converting the traffic; if you cannot say exactly what the thing is without killing the curiosity, you talk about your investment as a proxy for the prospect's benefit.
  anchor: >-
    Real quick question, what’s your email address? The reason I ask is because what I wanna do is send you a gazillion dollars of free stuff…
  source: >-
    acq-advertising-handbook.md, Part II Section IV, Ad Framework #2: Bribe, lines 2138-2200
  confirmations: 1
  demonstrates: >-
    Tell them what you want, tell them what they'll get, explain why it's valuable through your costs, then make it mysterious and valuable through a comparison range.
  anchor_at: "acq-advertising-handbook.md:2172"
- id: C-advertising-043
  type: case
  name: >-
    One hook, two unrelated businesses
  statement: >-
    The real quick, what's your email address hook ran as an ad for Skool, a software platform for building communities, and again for an event launching a book; the author points out that the products and businesses are entirely different and says that is precisely the point, and that he recycles hooks and formats across industries.
  why: >-
    These ad structures work agnostic of industry; only amateurs reinvent the wheel - pros use proven playbooks and checklists and make up for the rest with volume.
  anchor: >-
    This hook is the same hook I used for a Skool ad. But wait—one is for an event that sells a book, but the other was to advertise a software platform for building a community??
  source: >-
    acq-advertising-handbook.md, Part II Section IV, Ad Framework #2, lines 2142-2146 (also lines 1775 and 519)
  confirmations: 2
  demonstrates: >-
    A winning framework transfers between niches by swapping the words that describe the product and benefit; the same hook used for Section III #3 Bribe and Section IV #2 Bribe.
  anchor_at: "acq-advertising-handbook.md:2142"
- id: C-advertising-044
  type: case
  name: >-
    More than a gift card and less than a Tesla
  statement: >-
    Instead of naming the giveaway - if you do x, you'll get a free t-shirt - the ad gives a range between one known low-value item and one known high-value item: something more than a gift card but less than a Tesla, and every single person who shows up gets one. The same move is prescribed again for the Rumors Are True ad.
  why: >-
    People automatically abstract what they'll get towards the bigger thing, and you are not going to beat anyone's imagination, so details are refused and the loop stays open until they act.
  anchor: >-
    Instead of saying “if you do x, you’ll get a free t-shirt” we’d say “if you do x, you’ll get something more than a gift card but less than a Tesla”.
  source: >-
    acq-advertising-handbook.md, Part II Section IV, Ad Framework #2, line 2200 (used in the ad at line 2180, prescribed again at line 2280)
  confirmations: 3
  demonstrates: >-
    Make the free thing mysterious and valuable at once; leave an open loop only the desired action can close.
  anchor_at: "acq-advertising-handbook.md:2200"
- id: C-advertising-045
  type: case
  name: >-
    Ad Framework #3: The Rumors Are True
  statement: >-
    Hook: The rumors are true... then the product named ($100M Leads is finally coming out), the personal investment as proof of value (two years, 2,000 hours personally logged, 1,500 by the editor, over a million dollars into the event), the book given away free framed as only part of what is coming, curiosity about more stuff, and a CTA that is purely visual - an end card with REGISTER NOW!, never spoken. Winning statics were then cut from the same creative, reading IT'S TRUE. and THE RUMORS ARE TRUE...
  why: >-
    Positioning the product as important because other people talk about it makes the viewer feel left out of something important, which motivates action; showing receipts for the investment dramatically increases how much they believe the value.
  anchor: >-
    I’ve spent two years on this book, 2,000 hours that I personally logged. (STAKES)
  source: >-
    acq-advertising-handbook.md, Part II Section IV, Ad Framework #3: The Rumors Are True, lines 2222-2284
  confirmations: 1
  demonstrates: >-
    Good ads do two things - get attention, then get action; a visual-only CTA as an experiment, especially for remixes; permutations of a winning hook into statics.
  anchor_at: "acq-advertising-handbook.md:2254"
- id: C-advertising-046
  type: case
  name: >-
    Ad Framework #4: You're Being Lied To
  statement: >-
    The camera comes fast around a corner with the talent walking at it: You're being lied to... Then old way versus new way - I was told if you build it, they will come. That's not true. What is true is that if you tell them, they will find you, and you do that only through advertising - proof (multiple companies built, the last sold for $46 million; Acquisition.com doing over $10 million a month), an openly selfish reason why (companies that get to $10 million come back for help to $100 million), speed framed as a decade compressed into hours, and a tear-away on-screen CTA.
  why: >-
    Walking around corners and high movement towards the camera works exceptionally well and matched the confrontational hook; people trust people who share their biases openly, even when the bias runs against the listener's interest; ads where the author moves almost always outperform.
  anchor: >-
    Ex: “I was told if you build it, they will come. That’s not true. If you tell them, they will find you.”
  source: >-
    acq-advertising-handbook.md, Part II Section IV, Ad Framework #4: You're Being Lied To, line 2360 (full breakdown lines 2304-2368)
  confirmations: 1
  demonstrates: >-
    Old way versus new way, problem versus solution, us versus them; movement as a visual hook; reframe the time they'd spend alone as the speed you provide.
  anchor_at: "acq-advertising-handbook.md:2360"
- id: C-advertising-047
  type: case
  name: >-
    Ad Framework #5: Data Stack
  statement: >-
    The ad opens on a whiteboard with the numbers already half written - a column reading WORDS, HOURS, PAGES, DRAWINGS, PRO TIPS, TWEETS - and the line this is gonna blow your mind. Then the stack is read out: 67,000 words, 2,000 hours, 270 pages, 107 drawings, 62 pro tips, nine tweets, two years to make one cookbook for making money. Then the release date and the giveaway, social proof (200,000 people already registered), real scarcity (a limited number of books), and a register CTA.
  why: >-
    Numbers at the beginning of ads, especially big numbers, seem to work every time the author uses them; half of something written on the board invokes curiosity because people want to see it completed, and it is in itself a flex showing the work that went in.
  applies_when: >-
    Find and list out all the wild stats about your product or service first, on one sheet, before the recording session; then many permutations of the ad can be made with little effort.
  anchor: >-
    67,000 words, 2,000 hours, 270 pages, 107 drawings, 62 pro tips, nine tweets, two years to make one cookbook for making money (NUMBERS/PROOF).
  source: >-
    acq-advertising-handbook.md, Part II Section IV, Ad Framework #5: Data Stack, lines 2386-2444
  confirmations: 1
  demonstrates: >-
    Authority, social proof, curiosity, scarcity, urgency, call to action in one ad; own the real limits of what you can deliver to create scarcity.
  anchor_at: "acq-advertising-handbook.md:2418"
```
