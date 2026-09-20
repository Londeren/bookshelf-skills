# Улов фазы 1 — ACQ Advertising Handbook (2025) (ярус 2), тип A: фреймворки

Группа `tier2-advertising`, слаг `advertising`, ярус 2. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **36** (экстрактор вернул 36, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `acq-advertising-handbook.md` | 1–2657 | 4 | 36 |

## Как собран файл

Экстрактор A (Frameworks) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier2-advertising.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier2-advertising-A.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 1; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: A-advertising-001
  type: framework
  name: >-
    The Ad Kaleidoscope
  statement: >-
    Once a single ad wins, run it through a four-step cycle — Identify Winners, Remix Winners, Remake Winners, Try New Ideas — putting 80% of the effort into the first three steps and 20% into new ideas, and restart the cycle on every new winner.
  why: >-
    It harnesses power law: 80% of advertising results come from 20% of winners, so making permutations of what is already proven produces more winning ads than starting from scratch every time.
  applies_when: >-
    Only once you already have ads running and at least a single winner; you cannot optimize ads that do not exist yet.
  structure:
    - >-
      Step 1: Identify Winners
    - >-
      Step 2: Remix Winners
    - >-
      Step 3: Remake Winners
    - >-
      Step 4: Try New Ideas
  anchor: >-
    The Ad Kaleidoscope is my tool for taking winning ads and multiplying them.
  source: >-
    acq-advertising-handbook.md, Part I Kaleidoscope Ads / How To Use The Ad Kaleidoscope, line 152 (cycle at lines 257–300, 487)
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:152"
- id: A-advertising-002
  type: framework
  name: >-
    more, better, new
  statement: >-
    The Ad Kaleidoscope is the author's general growth strategy applied to advertising: it puts out more volume, makes that volume better, and generates new winners.
  why: >-
    It works because it puts advertising-specific action items on all three growth elements at once.
  structure:
    - >-
      more
    - >-
      better
    - >-
      new
  anchor: >-
    The Ad Kaleidoscope is “more, better, new” applied to advertising.
  source: >-
    acq-advertising-handbook.md, Part I Kaleidoscope Ads, lines 154–156
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:156"
- id: A-advertising-003
  type: framework
  name: >-
    Remixing Winners
  statement: >-
    Remixes are the post-production permutations of a winning ad — same raw footage, varied edits — listed from easiest to hardest and used all at once to turn one winner into dozens of variations.
  why: >-
    They are the fastest to make, so they keep ads performing and buy time to do the remakes; but they fatigue faster than remakes because they look more similar to the original.
  applies_when: >-
    Immediately after a winning ad is identified, since they can all be done on a computer without extra recording time.
  structure:
    - >-
      New Speed - Literally just change playback speed to 1.1x or 1.2x
    - >-
      New Filters - One-click black & white, sepia, or contrast adjustments
    - >-
      New Background/Border - Simple color swaps or border additions
    - >-
      New Fonts/Captions - Change text styling in editing software
    - >-
      New Headline - Replace text overlay with different copy
    - >-
      New Medium - Export video frame as static image
    - >-
      New Format - Resize for different placements (square, vertical, etc.)
    - >-
      New Meat - Splice in different middle section (requires editing skills)
    - >-
      New Effects - Add motion graphics, stickers, animations, etc.
  anchor: >-
    Your first run through the kaleidoscope, you’ll use the same raw footage of your previous winners, but vary the edits.
  source: >-
    acq-advertising-handbook.md, Part I Remixing Winners, line 283 (list at lines 312–320)
  confirmations: 3
  authors_caveat: >-
    Beyond that though, remixes tend to fatigue faster than remakes, because they look more similar.
  anchor_at: "acq-advertising-handbook.md:283"
- id: A-advertising-004
  type: framework
  name: >-
    Hook → Meat/Offer → CTA
  statement: >-
    Every ad in the Blackbook is broken into three labelled parts in this order — Hook, Meat (or Meat/Offer), CTA — and the parts are swappable between winners.
  why: >-
    Keeping the winning hook and splicing in a different ad meat produces a new variation without losing what made the ad a winner.
  structure:
    - >-
      Hook
    - >-
      Meat/Offer
    - >-
      CTA
  anchor: >-
    The right rectangle has "Hook 1" on the left, "Meat 2" in the middle, and "CTA 1" on the right.
  source: >-
    acq-advertising-handbook.md, Part I Remixing Winners (Same Hook. New Meat), line 394; the same three labels head the copy of all twenty ad breakdowns
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:394"
- id: A-advertising-005
  type: framework
  name: >-
    Remaking Winners
  statement: >-
    Remakes are the pre-production permutations of a winning ad — the real-world components are changed and the ad is recorded again — listed from easiest to hardest.
  why: >-
    They take more effort than remixes because you have to record again, but this is where you can keep a winner performing for years.
  applies_when: >-
    Simultaneously with remixing, once a winner exists and you are willing to record again.
  structure:
    - >-
      New Clone - Same everything, just hit record again
    - >-
      New Props - Swap one object for another
    - >-
      New Examples - Change names/numbers in same script
    - >-
      New Setting - Move to different location
    - >-
      New Talent - Find, coordinate, and direct different person
    - >-
      New Combination - Multiple changes at once
  anchor: >-
    This means we're actually changing the real world components of the ad.
  source: >-
    acq-advertising-handbook.md, Part I Remaking Winners, line 418 (list at lines 424–429)
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:418"
- id: A-advertising-006
  type: framework
  name: >-
    My Ads Blackbook: Best 20 Ad Frameworks of All Time
  statement: >-
    The catalog of the author's twenty best ad frameworks, five each from four businesses — Gym Launch, ALAN, Skool and the $100M Leads book launch — to be modelled by any business rather than invented from scratch.
  why: >-
    The author uses these frameworks across different industries and they still crush; any of them can be turned into a B2C, B2B, service, SaaS or product ad by replacing the blocks with words that describe your own service and benefits.
  applies_when: >-
    For anyone who needs winners these frameworks give a headstart; for anyone who already has winners they give more.
  structure:
    - >-
      Section I: My Best Gym Launch Ad Frameworks
    - >-
      Ad Framework #1: Personal Testimonial/Origin Story
    - >-
      Ad Framework #2: Prop Comedy
    - >-
      Ad Framework #3: Emotional Avatar Testimonial
    - >-
      Ad Framework #4 Show Don't Tell
    - >-
      Ad Framework #5 Long Term Result
    - >-
      Section II: My Best ALAN Ad Frameworks
    - >-
      Ad Framework #1 Looking For 5 Avatars...
    - >-
      Ad Framework #2: New vs. Old
    - >-
      Ad Framework #3: Why You Will Never
    - >-
      Ad Framework #4: The “North Star”
    - >-
      Ad Framework #5: No BS Selfie
    - >-
      Section III: My Best Skool Ad Frameworks
    - >-
      Ad Framework #1: Trending Format
    - >-
      Ad Framework #2: Value Anchor
    - >-
      Ad Framework #3: Bribe
    - >-
      Ad Framework #4: Underdog
    - >-
      Ad Framework #5: Challenge With Prize
    - >-
      Section IV: My Best $100M Leads Book Launch Ad Frameworks
    - >-
      Ad Framework #1: Flying Prop
    - >-
      Ad Framework #2: Bribe
    - >-
      Ad Framework #3: The Rumors Are True
    - >-
      Ad Framework #4: You're Being Lied To
    - >-
      Ad Framework #5: Data Stack
  anchor: >-
    I demonstrate my five best frameworks across four different businesses: Gym Launch, ALAN, Skool, and
  source: >-
    acq-advertising-handbook.md, Part II intro and Table of Contents, line 513 (names at lines 63–79, 562–566, 1038–1042, 1569–1573, 2033–2037)
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:513"
- id: A-advertising-007
  type: framework
  name: >-
    What You’ll See for Every Winning Ad Framework
  statement: >-
    Each of the twenty ad frameworks is documented in the same six fields, in this order, ending with a How To Apply section split into the what to say and the how to show it.
  why: >-
    The author includes more visual notes than usual so the reader can actually make these winners for their own business.
  structure:
    - >-
      Ad Framework Type
    - >-
      Why This Ad Framework Rocks: how this ad came to be, why I like it, and other useful tidbits
    - >-
      Thumbnail + Link: So you can watch and see them in action.
    - >-
      Visual Hook: A description of the first three seconds of motion and design that stopped the scroll.
    - >-
      Ad Copy: The exact words from the ad.
    - >-
      How To Apply This Framework: the “what to say” and the “how to show it”
  anchor: >-
    Directions to follow to apply this style and structure to advertise whatever you sell. This comes in two parts.
  source: >-
    acq-advertising-handbook.md, Part II intro (What You’ll See for Every Winning Ad Framework), lines 535–542
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:542"
- id: A-advertising-008
  type: framework
  name: >-
    Ad Framework #1: Personal Testimonial/Origin Story
  statement: >-
    Claim a ridiculous outcome up front, then tour circumstances that are the opposite of what should produce it, stacking anti-proof, and snap the open loop closed at the end with overwhelming proof.
  why: >-
    The ad is one gigantic open loop that builds mystery while eliminating the implied objections about why something will not work in the viewer's circumstances, and it ends with a massive payoff of proof.
  applies_when: >-
    Any business that can think of a situation that would make it less than ideal for a customer to get an outcome.
  structure:
    - >-
      Make a wild promise/claim in the first five seconds.
    - >-
      Show yourself in an obviously “wrong” environment.
    - >-
      Walk the viewer through a rapid “problems tour”.
    - >-
      Expand the open loop and stack more negatives.
    - >-
      Snap the loop closed with overwhelming proof.
    - >-
      Deliver the takeaway and soft CTA.
  anchor: >-
    This ad framework functions like one gigantic open loop. The entire ad builds mystery.
  source: >-
    acq-advertising-handbook.md, Section I Ad Framework #1: Personal Testimonial/Origin Story, line 592 (steps at lines 654–672)
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:592"
- id: A-advertising-009
  type: framework
  name: >-
    Ad Framework #2: Prop Comedy
  statement: >-
    Script the ad one phrase at a time as a series of Yes-questions, pair each phrase with its own prop and mini-setting, film each line as a separate clip and join them with whip-cuts, music and captions, ending on a CTA card.
  why: >-
    These types of ads do not try to do too much; the point is to get the right person to click with the right intent, and the music and visuals do a lot of the work.
  structure:
    - >-
      Map the value-equation questions.
    - >-
      Assign one prop + one mini-setting per line.
    - >-
      Film each line separately.
    - >-
      Use whip-cuts or camera swings between clips.
    - >-
      Layer upbeat music with captions.
    - >-
      Finish with a CTA card.
  anchor: >-
    These types of ads don’t try to do too much. The point is to get the right person to click with the right intent.
  source: >-
    acq-advertising-handbook.md, Section I Ad Framework #2: Prop Comedy, line 688 (steps at lines 720–736)
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:688"
- id: A-advertising-010
  type: framework
  name: >-
    the value-equation questions
  statement: >-
    Write three to four Yes prompts that hit dream outcome, speed, ease and proof, each line three to five seconds max, with the last one being a CTA.
  why: >-
    Hitting the main value equation pillars is what a short ad has to do to explain truthfully why your thing is awesome before the CTA.
  applies_when: >-
    Scripting a short, fast-cut ad; also the way to model a trending-format ad directly.
  structure:
    - >-
      dream outcome
    - >-
      speed
    - >-
      ease
    - >-
      proof
  anchor: >-
    Write three to four “Yes” prompts that hit  _dream outcome, speed, ease, and proof._
  source: >-
    acq-advertising-handbook.md, Section I Ad Framework #2: Prop Comedy, line 720 (also line 1605)
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:720"
- id: A-advertising-011
  type: framework
  name: >-
    six points to hit
  statement: >-
    Brief a customer filming a testimonial on six points in this order: life before personally, life before professionally, the skepticism they had, why they took action anyway, life after personally, life after professionally.
  why: >-
    Given these six points the customers knocked it out of the park and no testimonial has outperformed the result in the company's history.
  applies_when: >-
    Asking an existing customer to record a testimonial ad.
  structure:
    - >-
      1) what was life like before personally
    - >-
      2) professionally
    - >-
      3) What skepticism did you have
    - >-
      4) why did you choose to take action anyways
    - >-
      5) What was life after like personally
    - >-
      6) professionally
  anchor: >-
    I asked them to film a testimonial and gave them six points to hit: 1) what was life like before personally and 2) professionally.
  source: >-
    acq-advertising-handbook.md, Section I Ad Framework #3: Emotional Avatar Testimonial, line 786 (the card is duplicated; same sentence at line 760)
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:760"
- id: A-advertising-012
  type: framework
  name: >-
    Ad Framework #3: Emotional Avatar Testimonial
  statement: >-
    Film a real customer who looks like the avatar in their own setting, cut fast to a gloomy shot, open on a blunt pain statement, stack five to six pains and stakes, mark the turning point, then show the dream outcome with numbers, speed and a damaging admission before one clear CTA.
  why: >-
    This ad framework absolutely crushes: it birthed one of the author's best ads of all time and over 100 variations of that one piece of creative all performed.
  structure:
    - >-
      Pick a client and record them in a setting that communicates that they’re like your avatar visually.
    - >-
      Show sad setting fast.
    - >-
      Open with a blunt pain statement.
    - >-
      Mark a clear turning point.
    - >-
      Describe/show the dream outcome with numbers and personal benefits.
    - >-
      Highlight the speed and ease.
    - >-
      Insert a brief, honest disclaimer.
    - >-
      Give a condensed “reason why” to take action.
    - >-
      End with one crystal-clear CTA on screen.
  anchor: >-
    Pick a client and record them in a setting that communicates that they’re like your avatar visually.
  source: >-
    acq-advertising-handbook.md, Section I Ad Framework #3: Emotional Avatar Testimonial, lines 842–862
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:842"
- id: A-advertising-013
  type: framework
  name: >-
    the narrative rhythm
  statement: >-
    The testimonial ad follows a fixed ten-beat sequence from personal stakes through the turning point and the work to the professional and personal good, the skepticism, the reason why and the CTA.
  why: >-
    Follow that sequence and you’ll do just fine.
  applies_when: >-
    Structuring a customer testimonial ad.
  structure:
    - >-
      PERSONAL STAKES
    - >-
      PERSONAL PAIN
    - >-
      PROFESSIONAL PAIN
    - >-
      TURNING POINT
    - >-
      WORK
    - >-
      PROFESSIONAL GOOD
    - >-
      PERSONAL GOOD
    - >-
      ADDRESS SKEPTICISM
    - >-
      REASON WHY
    - >-
      CTA
  anchor: >-
    PERSONAL STAKES → PERSONAL PAIN → PROFESSIONAL PAIN → TURNING POINT → WORK → PROFESSIONAL GOOD → PERSONAL GOOD → ADDRESS SKEPTICISM → REASON WHY→ CTA.
  source: >-
    acq-advertising-handbook.md, Section I Ad Framework #3: Emotional Avatar Testimonial, line 864
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:864"
- id: A-advertising-014
  type: framework
  name: >-
    Ad Framework #4 Show Don’t Tell
  statement: >-
    Instead of claiming the result, film customers who match the avatar demonstrating the dream outcome, frame it with the fewest possible words in high contrast, get people moving in unison, and close with a visual CTA because the ad has no narration.
  why: >-
    The closer a prospect can approximate the proof to their situation, the lower the risk and the more compelling it is; proof works better than just about anything else for persuading people, and a demonstration without words works that much better.
  structure:
    - >-
      Show the outcome happening instead of saying it happened.
    - >-
      Frame what they’re looking at.
    - >-
      Get people to move in unison if possible.
    - >-
      Proof does the talking.
    - >-
      Non-verbal ads need non-verbal CTAs.
  anchor: >-
    In short, the closer a prospect can approximate the proof to their situation, the lower the risk, and by extension, the more compelling it is.
  source: >-
    acq-advertising-handbook.md, Section I Ad Framework #4 Show Don’t Tell, line 878 (steps at lines 909–925)
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:878"
- id: A-advertising-015
  type: framework
  name: >-
    Ad Framework #5 Long Term Result
  statement: >-
    Show bigger results over longer timelines using metrics only an advanced prospect understands: avatar in their own workspace with a wild before/after headline, one pain sentence, two or three more specific pains, a dated decision point, a Fast Win and a Big Win, deeper metrics, soft benefits, and a peer CTA.
  why: >-
    Contrasting big results on long timelines against the one trick ponies shows you are legit and brings in the highest quality customers, who cost more to acquire but pay more, stay longer, get better results and refer friends.
  applies_when: >-
    When you want the exact advanced customer rather than just your genre of customer; use language only the upper echelon of customers would understand.
  structure:
    - >-
      Open with a visual that matches the avatar plus wild before/after headline.
    - >-
      Hook with a single pain sentence.
    - >-
      Stack two to three more specific pains.
    - >-
      Mark the decision point.
    - >-
      Show two wins—the Fast Win and the Big Win.
    - >-
      Add more detail to further prove the initial claim.
    - >-
      Don’t forget life improvements and “soft” benefits.
    - >-
      Reason why CTA.
  anchor: >-
    Basically, I contrast my results against the “one trick ponies” in my industry. They’re all talking about small results in short timelines.
  source: >-
    acq-advertising-handbook.md, Section I Ad Framework #5 Long Term Result, line 945 (steps at lines 1002–1026)
  confirmations: 2
  authors_caveat: >-
    The cost per call for this campaign was higher than the author's KPIs; the lesson recorded is not to optimize for CAC but for LTV:CAC.
  anchor_at: "acq-advertising-handbook.md:945"
- id: A-advertising-016
  type: framework
  name: >-
    Ad Framework #1 Looking For 5 Avatars...
  statement: >-
    Open in an educational setting with the one-liner naming how many avatars you are looking for and the dream outcome, explain why you are only taking a limited number, why your thing is better, split the risk, and send them to your assistant to be qualified.
  why: >-
    It is one of the most classic direct response ads of all time, it works in any niche, it worked 70 years ago and works today; naming who you are not looking for and adding a compelling reason why takes it to the next level.
  applies_when: >-
    When launching something new, when just starting to run paid ads, or when monetizing an audience; it also works great for organic audiences.
  structure:
    - >-
      Film in an educational setting.
    - >-
      Open with the one-liner.
    - >-
      Explain why you’re only taking limited clients.
    - >-
      Why your thing is better than what’s out there.
    - >-
      Split risk with the customer.
    - >-
      Send them to your assistant.
  anchor: >-
    This is one of the most classic direct response ads of all time. It works in any niche.
  source: >-
    acq-advertising-handbook.md, Section II Ad Framework #1 Looking For 5 Avatars..., line 1068 (steps at lines 1150–1170)
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1068"
- id: A-advertising-017
  type: framework
  name: >-
    the one-liner
  statement: >-
    The opening line is a fill-in-the-blank template: I’m looking for five (AVATAR) who are looking to (OUTCOME) but don’t want to (BIGGEST PAIN POINT) so that I can (REASON WHY), here’s my (PROOF), if interested (KEEP WATCHING).
  why: >-
    Being as specific as possible further increases credibility, and a compelling reason why is what takes these ads to the next level.
  applies_when: >-
    Opening a Looking For 5 Avatars ad; the New vs. Old framework closes with the same slot-filled hook.
  structure:
    - >-
      AVATAR
    - >-
      OUTCOME
    - >-
      BIGGEST PAIN POINT
    - >-
      REASON WHY
    - >-
      PROOF
    - >-
      KEEP WATCHING
  anchor: >-
    “I’m looking for five (AVATAR) who are looking to (OUTCOME) but don’t want to (BIGGEST PAIN POINT) so that I can (REASON WHY).
  source: >-
    acq-advertising-handbook.md, Section II Ad Framework #1 Looking For 5 Avatars..., line 1152 (also lines 1066 and 1274)
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:1152"
- id: A-advertising-018
  type: framework
  name: >-
    Ad Framework #2: New vs. Old
  statement: >-
    In an educational setting, call out the exact avatar, make a big detailed claim, attribute all their pain to their outdated model, reveal the new way anchored to one simple metric, prove it with a case study or hypothetical and a single proof line, reverse the risk, and close with a CTA that previews the process.
  why: >-
    ADucational ads can do a lot of heavy lifting: they build brand and drive sales at once, and if you are brand new you are judged on the quality of the information rather than a pre-existing brand.
  applies_when: >-
    Especially well with more advanced or complex products or services, and with something brand new.
  structure:
    - >-
      Film in an educational setting and call out your exact avatar in ≤ five seconds.
    - >-
      Make a big claim with details.
    - >-
      Attribute all the pain in their life to their outdated model.
    - >-
      Reveal the new way and anchor it to a simple metric.
    - >-
      Drive it home with a case study or hypothetical.
    - >-
      Reinforce authority with a single proof line.
    - >-
      Make a risk-reversed offer if possible.
    - >-
      Finish with a CTA that previews the process.
    - >-
      Close with your hook.
  anchor: >-
    It's a classic ADucational framework. You see these a lot, but few do them well.
  source: >-
    acq-advertising-handbook.md, Section II Ad Framework #2: New vs. Old, line 1184 (steps at lines 1250–1274)
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1184"
- id: A-advertising-019
  type: framework
  name: >-
    Ad Framework #3: Why You Will Never
  statement: >-
    From a whiteboard, call out the avatar, establish authority in one credential, rapid-fire the specific numeric warning signs that keep them stuck, name a non-obvious new solution that inverts all of them, and send them to a lead magnet or VSL.
  why: >-
    It capitalizes on understanding the prospects' problem and solution better than they do; each added detail builds pressure, and a problem described specifically enough makes the viewer think the author must be an insider.
  applies_when: >-
    Any niche — the pain/problem-based angle is super repeatable; list the problems as specifically as you possibly can.
  structure:
    - >-
      Begin by standing in front of a whiteboard and addressing your exact avatar in the first sentence.
    - >-
      Establish authority.
    - >-
      Rapid-fire through prospect-specific pains.
    - >-
      Introduce your new solution.
    - >-
      CTA to your lead magnet or Video Sales Letter.
  anchor: >-
    This pain/problem-based angle is super repeatable in any niche. List all the problems out as specifically as you possibly can.
  source: >-
    acq-advertising-handbook.md, Section II Ad Framework #3: Why You Will Never, line 1294 (steps at lines 1366–1374)
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1294"
- id: A-advertising-020
  type: framework
  name: >-
    Ad Framework #4: The “North Star”
  statement: >-
    Pick one predictive metric, call out the avatar with the nightmare it causes, establish authority, lay out a hierarchy of outcomes by level of that metric with the specific pains at each level, then present your model as what fixes the metric and CTA to the next step.
  why: >-
    A predictive metric lets you predict their pain point — as neck and wrist thickness predict body fat — so the ad lists what they want and explains why it is out of reach for them right now.
  applies_when: >-
    Any market where one metric predicts the prospect's ceiling; the differentiator is specificity, naming moments only an insider would know.
  structure:
    - >-
      Start with a direct callout plus a nightmare scenario.
    - >-
      Establish authority.
    - >-
      List a hierarchy of outcomes based on the metric.
    - >-
      List specific pains they experience at each level.
    - >-
      Introduce how your new method solves the north star metric.
    - >-
      CTA to the next step.
  anchor: >-
    In this framework, I create a “north star” metric. Then I predict their pain point based on this metric (it can be anything as long as it’s predictive).
  source: >-
    acq-advertising-handbook.md, Section II Ad Framework #4: The “North Star”, line 1388 (steps at lines 1468–1478)
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1388"
- id: A-advertising-021
  type: framework
  name: >-
    Ad Framework #5: No BS Selfie
  statement: >-
    A very short selfie clip shot in motion in a credible setting: an if-then pain statement, the solution named in one sentence without explanation, proof that someone worse off got a better result, and a swipe-up.
  why: >-
    Constraining your time forces you to limit your words to the only things that matter; the ad sells the next step and nothing more, letting the funnel and lead magnet do the rest.
  applies_when: >-
    Top of funnel, when there is additional information later in the funnel and conversion process; it is an ad for your lead magnet rather than an ad to sell.
  structure:
    - >-
      Let the setting do the selling.
    - >-
      Start with an if-then pain statement.
    - >-
      Introduce your solution in one sentence.
    - >-
      Show proof that someone worse than them got results better than them.
  anchor: >-
    Think of this as an ad for your lead magnet more than an ad to sell. It sells the next step. Nothing more.
  source: >-
    acq-advertising-handbook.md, Section II Ad Framework #5: No BS Selfie, line 1492 (steps at lines 1535–1549)
  confirmations: 2
  authors_caveat: >-
    On the flex setting: the author only did this for a brief stint in his career and stopped because he did not want that kind of brand, while noting it is effective.
  anchor_at: "acq-advertising-handbook.md:1492"
- id: A-advertising-022
  type: framework
  name: >-
    Ad Framework #1: Trending Format
  statement: >-
    Record an ad in whatever video format is currently popular so it looks organic, open on a recent surprising discovery, stack speed and scaled proof in one line, then kill the standard objections with proof of both big and average outcomes.
  why: >-
    Trend ads capitalize on current popular video formats, which are popular for a reason; organic is always ahead of paid ads because of the volume and speed of testing for creators, so where organic is today is where ads will be in six to 12 months.
  applies_when: >-
    Any niche selling any product or service — model the ad directly while the format is in, or model the concept by taking the best organic hooks and bolting a CTA onto your best organic content.
  structure:
    - >-
      Record a solo podcast clip that looks 100% organic.
    - >-
      Lead with a recent surprising discovery.
    - >-
      Stack speed and scaled proof in one line.
    - >-
      Hammer perceived likelihood and ease by removing every classic objection using proof.
  anchor: >-
    Trend ads capitalize on current popular video formats. The example I show emerged when podcast clips were my entire feed.
  source: >-
    acq-advertising-handbook.md, Section III Ad Framework #1: Trending Format, line 1599 (steps at lines 1654–1668)
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1599"
- id: A-advertising-023
  type: framework
  name: >-
    Ad Framework #2: Value Anchor
  statement: >-
    An offer-centric ad with two stacks that anchor high and then price-drop: ask descending price questions about the dream outcome, explain the offer, anchor it at the marketplace rate, give it away free or below the anchor, then add a last-minute incentive that makes it better than free, then CTA.
  why: >-
    Free still has costs, so you have to make free valuable: anchoring makes free feel like an unexpected windfall instead of a marketing cliché, and the variable reward turns zero cost into potential gain.
  applies_when: >-
    Any niche — the structure could be copied anywhere; the alternative anchor question asks how much it would be worth to make something bad go away.
  structure:
    - >-
      How much would you pay for DREAM OUTCOME? $XXX, $XX, $X?
    - >-
      Explain offer
    - >-
      Anchor value of offer at marketplace rate.
    - >-
      Give it free/or less than anchor
    - >-
      Add in a last-minute incentive that makes it even better than free.
    - >-
      CTA
  anchor: >-
    How much would you pay for DREAM OUTCOME? $XXX, $XX, $X? →Explain offer→Anchor value of offer at marketplace rate.
  source: >-
    acq-advertising-handbook.md, Section III Ad Framework #2: Value Anchor, line 1692 (steps at lines 1739–1747)
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1692"
- id: A-advertising-024
  type: framework
  name: >-
    Ad Framework #3: Bribe
  statement: >-
    Open with a pattern-interrupt request for their contact information, say what they get in exchange, anchor its value against real market pricing, tie it to the dream outcome, add an incentive with a reason why, and make the CTA the same as the hook.
  why: >-
    It is a killer offer-driven ad up front driving to a page that does the heavy lifting; shorter, proof-heavy creatives just have to earn the click and let the page and VSL close. Mirroring the hook in the CTA increases congruency: if they stayed for the hook they will act on it too.
  structure:
    - >-
      Ask them for contact information with a pattern-interrupt question.
    - >-
      Tell them what they’ll get in exchange.
    - >-
      Explain why it’s valuable by anchoring against real market pricing.
    - >-
      Clarify what it will help them do→the dream outcome.
    - >-
      Add an additional incentive if desired.
    - >-
      Make your CTA the same as your hook.
  anchor: >-
    It’s a killer offer-driven ad up front driving to a page that did the heavy lifting.
  source: >-
    acq-advertising-handbook.md, Section III Ad Framework #3: Bribe, line 1771 (steps at lines 1816–1834)
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1771"
- id: A-advertising-025
  type: framework
  name: >-
    Ad Framework #4: Underdog
  statement: >-
    Lead with the lowest, most believable result on your leaderboard against a blank screen, name the big achievers only to pivot back to the small number, and give a big reason why the promotion is a big deal.
  why: >-
    It sets low expectations and is more believable: people already know the outcome is cool, the issue is that they do not believe they can do it, so beating them to the punch about lower-tier outcomes gains trust while the higher range still attracts high achievers.
  structure:
    - >-
      Lead with a modest, believable number/outcome that feels attainable.
    - >-
      Stack proof by naming progressively larger results, then pivot back to the smallest.
    - >-
      Give them a good “reason why” this promotion is a big deal.
  anchor: >-
    What's beautiful about it is it sets low expectations—which is my preference.
  source: >-
    acq-advertising-handbook.md, Section III Ad Framework #4: Underdog, line 1854 (steps at lines 1898–1910)
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1854"
- id: A-advertising-026
  type: framework
  name: >-
    Ad Framework #5: Challenge With Prize
  statement: >-
    Show an outsized prize on camera, put it on a short deadline, prove a past winner got it, state the single metric that wins it, show how you will help them win, make not winning valuable too, prove the free thing works, and show what happens the moment they click.
  why: >-
    A giveaway makes marketing more compelling, and making both outcomes a win leaves not doing it as the only bad outcome; showing the signup flow removes the final barrier to conversion.
  applies_when: >-
    Ideally something huge for your specific audience — the broader the audience, the better money, cars and vacations work; for a narrow audience something like re-outfitting a gym is more compelling.
  structure:
    - >-
      Give away something insane.
    - >-
      Put it on a time constraint.
    - >-
      Prove somebody else has gotten the thing you give away.
    - >-
      Tell them exactly how to get it.
    - >-
      Show how you’ll help them win.
    - >-
      Make not winning valuable too.
    - >-
      Show proof your free thing works.
    - >-
      Show them what happens the moment they take the next step.
  anchor: >-
    To state the obvious, you don’t need to give away massive amounts of cash or a Cybertruck to make your marketing more compelling—
  source: >-
    acq-advertising-handbook.md, Section III Ad Framework #5: Challenge With Prize, line 1932 (steps at lines 2005–2019)
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1932"
- id: A-advertising-027
  type: framework
  name: >-
    Ad Framework #1: Flying Prop
  statement: >-
    Catch a real object thrown into frame on camera, joke it into the offer, pile on the tangible investment you made, and hint at a secret that only taking the next step can reveal.
  why: >-
    Stuff that moves generally beats stuff that doesn't, and real stuff that moves often beats computer stuff that moves; the whole ad is a daisy chain of open loops whose only closing action is the next step, which gets people to register and to show.
  structure:
    - >-
      Catch a flying prop.
    - >-
      Make a quick joke and tie the prop to your offer.
    - >-
      Pile on tangible reasons to attend.
    - >-
      Hint at a big secret and leave the loop open.
    - >-
      Props.
  anchor: >-
    The entire ad is curiosity-driven. The entire ad is a daisy chain of open loops with only one action to close them—taking the next step.
  source: >-
    acq-advertising-handbook.md, Section IV Ad Framework #1: Flying Prop, line 2065 (steps at lines 2116–2120)
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2065"
- id: A-advertising-028
  type: framework
  name: >-
    Ad Framework #2: Bribe (book launch)
  statement: >-
    The same Bribe hook applied to a different industry: ask for the contact info, promise outrageously valuable free stuff, justify the value by the cost you incurred, call the thing a big deal, and describe the mystery gift as a range between one low-value and one high-value known item.
  why: >-
    These ad structures work agnostic of industry — the same hook sold a software platform and a book launch event; being vague lets people's imagination fill in the perfect copy, and you are not going to beat anyone's imagination.
  applies_when: >-
    When you cannot tell someone exactly what the thing is and want to keep curiosity: talk about your investment as a proxy for their potential benefit.
  structure:
    - >-
      Tell them what you want.
    - >-
      Tell them what they’ll get in exchange.
    - >-
      Explain why it’s valuable.
    - >-
      Emphasize that the thing you promote is a big deal.
    - >-
      Make your free thing mysterious and valuable through comparisons.
  anchor: >-
    This hook is the same hook I used for a Skool ad.
  source: >-
    acq-advertising-handbook.md, Section IV Ad Framework #2: Bribe, line 2142 (steps at lines 2184–2200)
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2142"
- id: A-advertising-029
  type: framework
  name: >-
    Ad Framework #3: The Rumors Are True
  statement: >-
    Open by saying other people already want what you have and it is finally coming out, frame the gift as the tip of the iceberg, justify its value with receipts of your personal investment, add an unnamed secret described as a range, and close on a purely visual CTA.
  why: >-
    Positioning the product as important because other people talk about it leverages curiosity and makes the viewer feel left out of something important, which motivates action.
  applies_when: >-
    Any market — this hook works in any market; once the hook wins, permute it into static formats.
  structure:
    - >-
      Tell them other people want what you have.
    - >-
      Tell them what they’ll get for taking the next step.
    - >-
      Explain why it’s valuable.
    - >-
      Add curiosity.
    - >-
      Visual CTA.
    - >-
      Make multiple versions in multiple formats.
  anchor: >-
    I position my product as important because  _other people talk about it_. It leverages curiosity.
  source: >-
    acq-advertising-handbook.md, Section IV Ad Framework #3: The Rumors Are True, line 2226 (steps at lines 2266–2284)
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2226"
- id: A-advertising-030
  type: framework
  name: >-
    Good ads do two things
  statement: >-
    An ad has two jobs in order: get the prospect's attention, then get the prospect to take action — so it needs a part that creates attention and a part that increases the benefit and decreases the cost of acting.
  why: >-
    Motivating action is the point of all good ads, so the recipe follows from the two objectives.
  structure:
    - >-
      get the prospect’s attention
    - >-
      get the prospect to take action
  anchor: >-
    get the prospect’s attention→get the prospect to take action. So it would follow that you have a part of the ad that gets attention
  source: >-
    acq-advertising-handbook.md, Section IV Ad Framework #3: The Rumors Are True, line 2228
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2228"
- id: A-advertising-031
  type: framework
  name: >-
    Ad Framework #4: You’re Being Lied To
  statement: >-
    Walk fast towards the camera, confront the viewer with a lie they believe, throw rocks at the old way and name the new way, prove it, share your selfish reason why, reframe the time you are compressing for them as speed, and flash one on-screen next step.
  why: >-
    It is another spin on old way vs. new way, and the classics work; the confrontational walking-and-talking delivery pairs with the confrontational hook, and ads where the author moves almost always outperform. People trust people who share their biases openly.
  structure:
    - >-
      Walk towards the camera aggressively. Tell them they’re being lied to.
    - >-
      Expose the old way and present the new way.
    - >-
      Show proof your new way works.
    - >-
      Share your selfish reason why.
    - >-
      Promise fast results.
    - >-
      Tell them what to do next to learn about the new way.
  anchor: >-
    It’s another spin on a classic: old way vs. new way. Problem vs. solution. Us vs. them.
  source: >-
    acq-advertising-handbook.md, Section IV Ad Framework #4: You’re Being Lied To, line 2308 (steps at lines 2358–2368)
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2308"
- id: A-advertising-032
  type: framework
  name: >-
    Ad Framework #5: Data Stack
  statement: >-
    Promise to blow their mind in front of a half-written whiteboard, rapid-fire the most impressive stats you collected beforehand, state how many people already registered, own the real limits of what you can supply, and tell them what to do next.
  why: >-
    Numbers at the beginning of ads, especially big numbers, work every time; half-written work on the board invokes curiosity and flexes the effort, and owning the true limitation increases demand by cutting perceived supply.
  applies_when: >-
    Once you have listed all the wild stats about your product or service; there are then many permutations of this ad to make with very little effort.
  structure:
    - >-
      Tell them you’re going to blow their mind.
    - >-
      Collect stats.
    - >-
      List your most impressive stats.
    - >-
      Tell them how many people have shown interest already.
    - >-
      Explain the true and real limitations of your product/service.
    - >-
      Tell them what to do next.
  anchor: >-
    Numbers at the beginning of ads, especially big numbers, seem to work every time I use them.
  source: >-
    acq-advertising-handbook.md, Section IV Ad Framework #5: Data Stack, line 2390 (steps at lines 2426–2444)
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2390"
- id: A-advertising-033
  type: framework
  name: >-
    Three ideas power the engine
  statement: >-
    The whole method rests on three ideas: volume negates luck, winners are rare so squeeze every drop of blood from them, and winning ad frameworks work for any business.
  why: >-
    80% of sales come from 20% of ads, and consistent winners take the volatility out of advertising; every hook, proof stack and CTA in the twenty frameworks can sell whatever you have if you swap the details.
  structure:
    - >-
      First, volume negates luck.
    - >-
      Second, winners are rare, so squeeze every drop of blood from them.
    - >-
      Third, winning ad frameworks work for any business.
  anchor: >-
    You’ve now seen the whole machine—how I find winners, how I multiply them, and the exact steps to do it. Three ideas power the engine.
  source: >-
    acq-advertising-handbook.md, Part III intro, lines 2460–2466
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2460"
- id: A-advertising-034
  type: framework
  name: >-
    Ad Kaleidoscope Checklist
  statement: >-
    The tear-out checklist splits the fifteen permutation moves into two buckets, each in order of difficulty: post-production moves applied to an existing winning ad, and pre-production moves that record a fresh version of the same winner.
  why: >-
    The author is a checklist guy and keeps the books on the desk so the reader can always find what they need: remixes you can use tonight, remakes you can film this weekend.
  structure:
    - >-
      Post-production: Apply to an existing winning ad (in order of difficulty) — New Speed, New Filters, New Background/Border, New Fonts/Captions, New Headline, New Medium, New Format, New Meat, New Effects
    - >-
      Pre-production: Record a fresh version of the same winner — New Clone, New Props, New Examples, New Setting, New Talent, New Combination
  anchor: >-
    Here are two checklists on the following pages for the next time you make ads. One for the Ad Kaleidoscope.
  source: >-
    acq-advertising-handbook.md, Part III Ad Kaleidoscope Checklist, line 2500 (checklist at lines 2508–2541)
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2500"
- id: A-advertising-035
  type: framework
  name: >-
    Best Ad Framework Checklist
  statement: >-
    The ad-making checklist has four parts — visual elements, verbal delivery, ad script, CTA — each split into must-haves and nice-to-haves.
  why: >-
    The four parts correspond roughly to what they see, what you say, what they get and how to get it; the author notes you can make ads without some of his must-haves, he just doesn't.
  structure:
    - >-
      VISUAL ELEMENTS — Must-Haves: Paired Verbal & Visual Hooks, Movement, Similar Avatar, Show What You Tell, Captions, Platform Native
    - >-
      VISUAL ELEMENTS — Nice-to-Haves: Aspirational Setting/Trending Formats, Real World Demonstrations and Settings, Props
    - >-
      VERBAL DELIVERY — Must-Haves: Simple Words, Enunciation (No mumbling!)
    - >-
      VERBAL DELIVERY — Nice-to-Haves: Details/Numbers, Continuous “Open-looped” Curiosity, Benefits & Pains Through Prospect’s Real Life Experiences
    - >-
      AD SCRIPT — Must-Haves: Call Out Prospects, Compelling Reason Why, Comparisons, As Many Proof Points As Possible
    - >-
      AD SCRIPT — Nice-to-Haves: Damaging Admissions, Stakes/Struggles/Investment
    - >-
      CTA — Must-Haves: One Clear Verbal & Visual Next Step To Take
    - >-
      CTA — Nice-to-Haves: Reasons To Act (CTA Congruent With Hook, Scarcity & Urgency, Bonus/Incentives)
  anchor: >-
    I divide the checklist into four parts: visual, verbal delivery, script, and CTA. They correspond roughly to: what they see, what you say, what they get, how to get it.
  source: >-
    acq-advertising-handbook.md, Part III Best Ad Framework Checklist, lines 2550–2631
  confirmations: 1
  authors_caveat: >-
    I want to be clear, you can make ads without some of my must-haves… I just don’t.
  anchor_at: "acq-advertising-handbook.md:2550"
- id: A-advertising-036
  type: framework
  name: >-
    Comparisons
  statement: >-
    A must-have of the ad script: four paired comparisons, each setting what the new path gives against what staying the same costs — outcome, speed, certainty, ease.
  why: >-
    They are listed among the must-haves of the ad script bucket of the author's real-world checklist for making ads that make money.
  structure:
    - >-
      Dream Outcome & Nightmare of Staying The Same
    - >-
      Speed To Result & Delay of Inaction
    - >-
      Certainty Of New Path & Risk of Current Path
    - >-
      Ease Of Result & Difficulty of Current Path
  anchor: >-
    Dream Outcome & Nightmare of Staying The Same
  source: >-
    acq-advertising-handbook.md, Part III Best Ad Framework Checklist, AD SCRIPT, lines 2600–2604
  confirmations: 1
  anchor_at: "acq-advertising-handbook.md:2601"
```
