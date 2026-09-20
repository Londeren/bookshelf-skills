# ACQ Advertising Handbook (2025) — ярус 2, группа `tier2-advertising`, единиц после валидации: 129

Часть `pipeline/hormozi/validated.md` (там шапка, гейт, список валидаторов и правила обращения с якорем). Блоки перенесены из `pipeline/hormozi/catch/tier2-advertising-<X>.md` байт в байт; фазой 2 дописаны `tier`, `merged_from` и поднятое `confirmations`. Проверка: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/validated/tier2-advertising.md`.


## A. Фреймворки — 27

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
  confirmations: 9
  anchor_at: "acq-advertising-handbook.md:152"
  tier: 2
  merged_from: [B-advertising-147, C-advertising-002, C-advertising-003, E-advertising-001, E-advertising-002, E-advertising-003]
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
  confirmations: 7
  authors_caveat: >-
    Beyond that though, remixes tend to fatigue faster than remakes, because they look more similar.
  anchor_at: "acq-advertising-handbook.md:283"
  tier: 2
  merged_from: [A-advertising-034, B-advertising-009, C-advertising-008, E-advertising-006]
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
  tier: 2
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
  confirmations: 6
  anchor_at: "acq-advertising-handbook.md:418"
  tier: 2
  merged_from: [C-advertising-014, C-advertising-015, C-advertising-018, E-advertising-007]
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
  confirmations: 7
  anchor_at: "acq-advertising-handbook.md:592"
  tier: 2
  merged_from: [B-advertising-016, B-advertising-018, B-advertising-019, B-advertising-021, B-advertising-022]
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
  confirmations: 5
  anchor_at: "acq-advertising-handbook.md:688"
  tier: 2
  merged_from: [B-advertising-026, B-advertising-027, B-advertising-028]
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
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:720"
  tier: 2
  merged_from: [B-advertising-025, B-advertising-092]
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
  tier: 2
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
  confirmations: 5
  anchor_at: "acq-advertising-handbook.md:842"
  tier: 2
  merged_from: [A-advertising-013, B-advertising-032, B-advertising-034, B-advertising-035]
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
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:878"
  tier: 2
  merged_from: [B-advertising-043, B-advertising-044]
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
  confirmations: 4
  authors_caveat: >-
    The cost per call for this campaign was higher than the author's KPIs; the lesson recorded is not to optimize for CAC but for LTV:CAC.
  anchor_at: "acq-advertising-handbook.md:945"
  tier: 2
  merged_from: [B-advertising-050, B-advertising-051]
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
  confirmations: 5
  anchor_at: "acq-advertising-handbook.md:1068"
  tier: 2
  merged_from: [B-advertising-059, B-advertising-065, D-advertising-021]
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
  tier: 2
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
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:1184"
  tier: 2
  merged_from: [B-advertising-070, B-advertising-140]
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
  tier: 2
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
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:1388"
  tier: 2
  merged_from: [B-advertising-082, B-advertising-083]
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
  confirmations: 4
  authors_caveat: >-
    On the flex setting: the author only did this for a brief stint in his career and stopped because he did not want that kind of brand, while noting it is effective.
  anchor_at: "acq-advertising-handbook.md:1492"
  tier: 2
  merged_from: [B-advertising-086, B-advertising-087]
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
  confirmations: 5
  anchor_at: "acq-advertising-handbook.md:1599"
  tier: 2
  merged_from: [B-advertising-094, B-advertising-095, B-advertising-096]
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
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:1692"
  tier: 2
  merged_from: [B-advertising-098]
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
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:1771"
  tier: 2
  merged_from: [A-advertising-028, B-advertising-107]
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
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:1854"
  tier: 2
  merged_from: [B-advertising-114, B-advertising-115]
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
  confirmations: 5
  anchor_at: "acq-advertising-handbook.md:1932"
  tier: 2
  merged_from: [B-advertising-118, B-advertising-120, B-advertising-122]
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
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:2065"
  tier: 2
  merged_from: [B-advertising-128, B-advertising-129]
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
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:2226"
  tier: 2
  merged_from: [B-advertising-136]
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
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:2308"
  tier: 2
  merged_from: [B-advertising-139]
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
  tier: 2
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
  tier: 2
```


## B. Правила и критерии — 56

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
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:136"
  tier: 2
  merged_from: [D-advertising-002]
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:418"
  tier: 2
  merged_from: [D-advertising-007]
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
  confirmations: 6
  anchor_at: "acq-advertising-handbook.md:487"
  tier: 2
  merged_from: [B-advertising-007, D-advertising-001]
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
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:519"
  tier: 2
  merged_from: [D-advertising-009]
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
  tier: 2
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
  tier: 2
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
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:878"
  tier: 2
  merged_from: [D-advertising-013]
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
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:913"
  tier: 2
  merged_from: [D-advertising-015]
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
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:951"
  tier: 2
  merged_from: [D-advertising-019]
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
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:953"
  tier: 2
  merged_from: [B-advertising-055, D-advertising-020]
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  confirmations: 6
  anchor_at: "acq-advertising-handbook.md:1150"
  tier: 2
  merged_from: [D-advertising-022]
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
  tier: 2
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
  tier: 2
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
  confirmations: 5
  anchor_at: "acq-advertising-handbook.md:1250"
  tier: 2
  merged_from: [B-advertising-081]
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  confirmations: 6
  anchor_at: "acq-advertising-handbook.md:1292"
  tier: 2
  merged_from: [B-advertising-052, B-advertising-077, D-advertising-023]
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
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:1372"
  tier: 2
  merged_from: [D-advertising-024]
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
  tier: 2
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
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1539"
  tier: 2
  merged_from: [B-advertising-084]
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
  tier: 2
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
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1603"
  tier: 2
  merged_from: [D-advertising-028]
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
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:1668"
  tier: 2
  merged_from: [D-advertising-031]
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
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1741"
  tier: 2
  merged_from: [D-advertising-032]
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
  tier: 2
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
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:1769"
  tier: 2
  merged_from: [B-advertising-014, D-advertising-033]
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
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:1775"
  tier: 2
  merged_from: [B-playbooks-growth-127, D-advertising-035]
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
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:1826"
  tier: 2
  merged_from: [B-advertising-109, D-advertising-036]
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
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:1834"
  tier: 2
  merged_from: [B-advertising-057]
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
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:1856"
  tier: 2
  merged_from: [D-advertising-037]
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
  tier: 2
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
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:1932"
  tier: 2
  merged_from: [D-advertising-038]
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
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2011"
  tier: 2
  merged_from: [D-advertising-040]
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:2118"
  tier: 2
  merged_from: [B-advertising-133]
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
  tier: 2
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
  tier: 2
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
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:2200"
  tier: 2
  merged_from: [D-advertising-041]
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
  tier: 2
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
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:2284"
  tier: 2
  merged_from: [D-advertising-042]
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
  tier: 2
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
  confirmations: 2
  anchor_at: "acq-advertising-handbook.md:2366"
  tier: 2
  merged_from: [D-advertising-043]
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
  tier: 2
```


## C. Разборы (кейсы) — 25

```yaml
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
  tier: 2
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
  confirmations: 3
  demonstrates: >-
    Remixing Winners: recombining the parts of the Hook - Meat - CTA anatomy.
  anchor_at: "acq-advertising-handbook.md:392"
  tier: 2
  merged_from: [E-advertising-013]
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  confirmations: 2
  demonstrates: >-
    Call out the avatar; the value-equation questions (dream outcome, speed, ease, proof); paired verbal and visual hooks; one clear CTA.
  anchor_at: "acq-advertising-handbook.md:714"
  tier: 2
  merged_from: [E-advertising-037]
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
  tier: 2
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
  confirmations: 3
  demonstrates: >-
    Show what you tell; frame the shot with the fewest possible words and numbers in a high-contrast colour; many people moving at once (better still in unison) stops the scroll; a non-verbal ad needs a non-verbal CTA.
  anchor_at: "acq-advertising-handbook.md:880"
  tier: 2
  merged_from: [C-advertising-024, E-advertising-034]
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  confirmations: 3
  demonstrates: >-
    Price anchoring and price drop; competitor pricing as proof the free thing does not suck; a variable incentive that turns zero cost into potential gain.
  anchor_at: "acq-advertising-handbook.md:1717"
  tier: 2
  merged_from: [E-advertising-028]
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
  confirmations: 2
  demonstrates: >-
    Ask for contact information with a pattern interrupt; state the cash value of the free thing; anchor against real market pricing; give a reason why for the bonus; CTA congruent with the hook.
  anchor_at: "acq-advertising-handbook.md:1802"
  tier: 2
  merged_from: [C-advertising-042]
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
  confirmations: 3
  demonstrates: >-
    Identify winners out of volume, then remix and remake them; only amateurs reinvent the wheel.
  anchor_at: "acq-advertising-handbook.md:1769"
  tier: 2
  merged_from: [C-advertising-022]
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  confirmations: 3
  demonstrates: >-
    A winning framework transfers between niches by swapping the words that describe the product and benefit; the same hook used for Section III #3 Bribe and Section IV #2 Bribe.
  anchor_at: "acq-advertising-handbook.md:2142"
  tier: 2
  merged_from: [C-advertising-027]
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
  tier: 2
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
  tier: 2
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
  tier: 2
```


## D. Антипаттерны и границы — 8

```yaml
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
  tier: 2
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
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:273"
  tier: 2
  merged_from: [B-advertising-002]
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  confirmations: 4
  anchor_at: "acq-advertising-handbook.md:1601"
  tier: 2
  merged_from: [B-advertising-090, D-advertising-029]
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
  tier: 2
```


## E. Глоссарий — 13

```yaml
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:1388"
  tier: 2
  merged_from: [C-advertising-031]
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
  tier: 2
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
  tier: 2
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
  tier: 2
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
  confirmations: 3
  anchor_at: "acq-advertising-handbook.md:2200"
  tier: 2
  merged_from: [C-advertising-044]
```
