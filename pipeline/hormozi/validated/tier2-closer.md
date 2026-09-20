# ACQ Closer Handbook (2025) — ярус 2, группа `tier2-closer`, единиц после валидации: 98

Часть `pipeline/hormozi/validated.md` (там шапка, гейт, список валидаторов и правила обращения с якорем). Блоки перенесены из `pipeline/hormozi/catch/tier2-closer-<X>.md` байт в байт; фазой 2 дописаны `tier`, `merged_from` и поднятое `confirmations`. Проверка: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/validated/tier2-closer.md`.


## A. Фреймворки — 21

```yaml
- id: A-closer-002
  type: framework
  name: >-
    Memorizing the Script
  statement: >-
    The script is memorized by printing two copies, reading it aloud, blacking out one random word at a time and rereading until the whole script is blacked out, checking against the clean copy.
  why: >-
    The reader needs to breathe the script rather than read it, and letting memory fill each blacked-out gap forces recall instead of recognition.
  applies_when: >-
    The first days on the job, before going live on the phones.
  structure:
    - >-
      Print out *at least* two copies of the script.
    - >-
      Read the script out loud.
    - >-
      Use a marker to black out one random word.
    - >-
      Read it out loud again and let your memory fill in the gap.
    - >-
      Continue until you black out the whole script.
  anchor: >-
    **Memorizing the Script.** You will memorize the script. Here's how to do it:
  source: >-
    acq-closer-handbook.md, Onboarding: Schedule & Training, lines 670–677
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:670"
  tier: 2
- id: A-closer-009
  type: framework
  name: >-
    Work Your List: the three priorities
  statement: >-
    Prospects are worked in the order they are most likely to buy, in three groups: inbound sets first, then BAMFAMs, then pipeline.
  why: >-
    Newest, freshest appointments are the highest value, so they are called immediately; the other groups are worked in descending likelihood of buying.
  applies_when: >-
    Every hour of the day that is not a close call.
  structure:
    - >-
      **Priority 1: Inbound Sets.** These are prospects who have booked an appointment but have not spoken to a closer yet.
    - >-
      **Priority 2: BAMFAMs.** "Booked A Meeting From A Meeting." BAMFAMs have already spoken to a closer, have not bought yet, and have another close call scheduled.
    - >-
      **Priority 3: Pipeline.** Anyone that no-showed or declined our offer but who *we still have permission to call*.
  anchor: >-
    You work the prospects in the order they are most likely to buy. To make it simple, we split them into three groups. Each is explained below.
  source: >-
    acq-closer-handbook.md, Hunt Mode #2 Work Your List, lines 1289–1312
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1289"
  tier: 2
  merged_from: [B-closer-005, B-closer-011]
- id: A-closer-011
  type: framework
  name: >-
    Working Inbound Sets: The Full Process
  statement: >-
    An inbound set is taken to a close call through a fixed branching sequence: double dial to validate the contact, then three text blocks, with non-response steps and a cancel at twelve hours out.
  why: >-
    The process makes sure none of these precious prospects slip through the cracks.
  applies_when: >-
    From the moment an inbound lead books an appointment until the close call happens.
  structure:
    - >-
      **Double Dial to Validate Contact Info** — If Fake → Cancel and Opt Out; If they pick up → Pull Forward
    - >-
      Business (Block 1) — If response → [Why Us (Block 2)]
    - >-
      If no response after 12 hours → Non-Response 1
    - >-
      If no response after 24 hrs → Non-Response 2
    - >-
      Wait until 12 hrs before call → Cancel
    - >-
      Why Us (Block 2) — If response → [Pull Forward (Block 3)]; If not → Send Night Before/Morning of texts
    - >-
      Pull Forward (Block 3) — If Pulled Forward Same Day → Close; If not → Send Night Before/Morning of texts
  anchor: >-
    This process breaks down taking an Inbound Set all the way to a Close call. You need to know this very well.
  source: >-
    acq-closer-handbook.md, Hunt Mode, Working Inbound Sets: The Full Process, lines 1347–1388
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1367"
  tier: 2
  merged_from: [A-closer-041, B-closer-015]
- id: A-closer-012
  type: framework
  name: >-
    The two outbound priorities
  statement: >-
    Outbound time goes first to referrals from existing customers and only then, with the remainder, to opted-in leads worked from newest to oldest.
  why: >-
    Referrals are the best leads you can get and should net an extra deal a day; opt-ins at roughly two sets per hour produce at least one more close.
  applies_when: >-
    After the list is worked, and during the two-hour Pickup Primetime block at the end of the day.
  structure:
    - >-
      **Outbound Priority 1: Getting Referrals.** Referrals are customers that come from our customers.
    - >-
      **Outbound Priority 2: Opt-Ins.** With the remainder of your outbound block, you double dial and text unscheduled leads who opted into our marketing list—from newest to oldest.
  anchor: >-
    You create your own opportunities by making outbound calls to set your own appointments. First, you will do outbound after working your list. Second, you will do outbound during Pickup Primetime.
  source: >-
    acq-closer-handbook.md, Hunt Mode #3 Outbound, lines 1397–1409
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1397"
  tier: 2
  merged_from: [B-closer-020, B-closer-076]
- id: A-closer-016
  type: framework
  name: >-
    The three types of pauses
  statement: >-
    Pauses come in three marked lengths — short, medium and long — and the script notation says which one to use where.
  why: >-
    Pauses focus attention on what you just said, longer pauses focus more attention, and the more attention on a word the more important it becomes.
  applies_when: >-
    Wherever the script marks a pause; the longest pause always goes after the buying question.
  structure:
    - >-
      (…) → Short. Pauses that draw words out just enough to put more attention on or around that word.
    - >-
      (.) → Medium. Your normal pause. Like you’d use at the end of a sentence.
    - >-
      (—) → Long. Much longer than you’d normally use. These focus the most attention.
  anchor: >-
    We use three types of pauses. Short, medium, and long:
  source: >-
    acq-closer-handbook.md, Tone, lines 1654–1658; notation repeated ACQ Closing Script, lines 3247–3249
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1654"
  tier: 2
  merged_from: [E-closer-026]
- id: A-closer-019
  type: framework
  name: >-
    The 9 Steps of Discovery
  statement: >-
    Discovery runs nine steps — current, desired, then the pain cycle of obstacle, reason, pull teeth, recap, label, confirm — repeating the cycle until there are enough problems you can solve.
  why: >-
    Business owners never volunteer clearly labelled problems, so they have to be pulled out; every reason they cannot get results is another reason for them to buy.
  applies_when: >-
    After the introduction and before making the offer.
  structure:
    - >-
      **Current** - Establish where they are now
    - >-
      **Desired** - Establish where they want to be
    - >-
      **Obstacle** - Identify what's blocking them
    - >-
      **Reason** - Understand why it's not working
    - >-
      **Pull Teeth** - Get specific details when answers are vague, confusing, or incomplete
    - >-
      **Recap** - Restate their problem in their words
    - >-
      **Label** - Map their problem to your solution categories
    - >-
      **Confirm** - Verify you understood correctly
    - >-
      **Repeat** - Cycle back to steps 3-8 until you have enough problems you can solve
  anchor: >-
    Discovery follows a nine-step process that cycles through identifying problems until you have enough to make your offer:
  source: >-
    acq-closer-handbook.md, Discovery, The 9 Steps of Discovery, lines 1836–1868
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1838"
  tier: 2
  merged_from: [A-closer-020, D-closer-021]
- id: A-closer-021
  type: framework
  name: >-
    Pull Teeth
  statement: >-
    Whenever an answer is vague, confusing or incomplete, the response is the same two questions in the same order: ask them to tell you more, then ask for an example.
  why: >-
    Only two things matter — getting more information about the problem and mapping it to our solution — and asking for an example tends to make them connect it to a life experience.
  applies_when: >-
    Any vague, confusing or incomplete answer in discovery; also used on any objection the closer is unsure how to answer.
  structure:
    - >-
      **Vague:** I see. Can you tell me more about that?
    - >-
      Ok, cool. Can you give me an example?
  anchor: >-
    You'll note, no matter the type of bad answer, *you respond the same way*. You ask them to tell you more, and then you ask them to give an example.
  source: >-
    acq-closer-handbook.md, Discovery, Step 5: Pull Teeth, lines 1889–1912; reused Looping, lines 2352–2357
  confirmations: 7
  anchor_at: "acq-closer-handbook.md:1907"
  tier: 2
  merged_from: [B-closer-041, C-closer-016, D-closer-024, D-closer-041, E-closer-030]
- id: A-closer-022
  type: framework
  name: >-
    Recap, Label & Confirm
  statement: >-
    A problem is closed out in three moves: repeat it in their words, state it in our words, then ask whether you got it right.
  why: >-
    Recapping lays out their problem plainly and frames it in a way we can solve it, and the label is the word that will be mapped to the solution in the offer.
  applies_when: >-
    After the first steps of the Pain Cycle, and again on every later cycle.
  structure:
    - >-
      **Recap** - Repeat their problem in their words.
    - >-
      **Label** - State the problem in our words.
    - >-
      **Confirm** - Ask if you got it correct.
  anchor: >-
    Once you successfully go through the first steps of the Pain Cycle, it's time to recap. Recapping lays out their problem plainly and frames it in a way we can solve it.
  source: >-
    acq-closer-handbook.md, Discovery, Steps 6–8, lines 1914–1942
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1916"
  tier: 2
  merged_from: [B-closer-042]
- id: A-closer-023
  type: framework
  name: >-
    The five labels
  statement: >-
    However a business owner describes a problem, it is labelled into one of five categories — marketing, sales, product/delivery, people, profit — and it is those labels that get mapped to the offer.
  why: >-
    Business owners describe their problems in a million ways but every problem they have can and should be mapped to a solution we offer, so five labels are enough.
  structure:
    - >-
      **Marketing** → no views/reach, no ad conversions, too few leads, bad quality leads, personal brand not growing, etc.
    - >-
      **Sales** → can't close, no one can afford our stuff, no one can close like me, can't find good sales people, sales are inconsistent, etc.
    - >-
      **Product/Delivery** → churn is high, lifetime value is low, can't get people to buy again or come back, can't make enough to service customers.
    - >-
      **People** → my team sucks, I have no help, I'm overwhelmed, I can't find [insert role].
    - >-
      **Profit** → we're just not making as much money as we want, we are cash-flow constrained.
  anchor: >-
    Thankfully, we only describe them in five—and these five, listed below, are the labels we use to map to our offer later.
  source: >-
    acq-closer-handbook.md, Discovery, Steps 6–8, lines 1924–1942
  confirmations: 4
  authors_caveat: >-
    The scripts read the list back to the prospect in shorter and slightly different forms: marketing, sales, people, profit, or operations in the Outbound Set Phone Script (line 2857), and Marketing? Sales? People? Profit?...Something crazy? in the Closing Script (line 3351).
  anchor_at: "acq-closer-handbook.md:1924"
  tier: 2
  merged_from: [B-closer-078]
- id: A-closer-024
  type: framework
  name: >-
    Final Recap (Stacking the Pain)
  statement: >-
    When the pain cycles are done, all the recaps are put together and said again as one, given a single label, and confirmed.
  why: >-
    You are just sharing what you learned and then making sure they agree, which is what the offer is then built on.
  applies_when: >-
    Once the pain cycles are complete and before the transition to the offer.
  structure:
    - >-
      **Recap** - To make sure I understand. You tried three different marketing agencies, spent $50K, got leads that didn’t convert, and now you’re hesitant to invest again.
    - >-
      **Label** - So it sounds like the real issue isn’t just vendors, ads, and leads - it’s that you need an entirely new marketing and sales process.
    - >-
      **Confirm** - Does that sound right?
  anchor: >-
    Once you’ve completed your Pain Cycles, you need to stack the pain. To stack the pain, get your Recaps together and say them all again.
  source: >-
    acq-closer-handbook.md, Discovery, Final Recap (Stacking the Pain), lines 1956–1966
  confirmations: 4
  anchor_at: "acq-closer-handbook.md:1958"
  tier: 2
  merged_from: [B-closer-044, C-closer-007, E-closer-034]
- id: A-closer-025
  type: framework
  name: >-
    The offer making process
  statement: >-
    The offer runs five steps: transition with permission to share, map the problems to three solutions, stack the solution and benefit pairs, ask for the sale, then drop the price and stop talking.
  why: >-
    Typical salespeople go straight to pitching and abandon the pain points they just collected; mapping them instead crafts a personalized offer on the spot.
  applies_when: >-
    After all the problems have been recapped; the offer itself has two minutes, about 320 words.
  structure:
    - >-
      **Transition:** Tell them you think we can help. Then ask if they'd like to hear how.
    - >-
      **Map:** Connect their problems to our solutions, assurances, benefits, then confirm that it would help.
    - >-
      **Stack:** List all solution and benefit pairs up to this point. You do this three times.
    - >-
      **Ask:** Ask if they are ready to buy/move forward.
    - >-
      **Drop Price & STFU:** Then you state the price and shut the fuck up.
  anchor: >-
    To make the offer, we have to transition from discovery smoothly. We do this after we recapped all the problems.
  source: >-
    acq-closer-handbook.md, Offer, How to Make The Offer, lines 1991–2060
  confirmations: 5
  anchor_at: "acq-closer-handbook.md:1993"
  tier: 2
  merged_from: [B-closer-045, B-closer-047, B-closer-049, D-closer-025]
- id: A-closer-026
  type: framework
  name: >-
    Map: Problem, Solution, Assure, Benefit, Confirm
  statement: >-
    Each problem is mapped in five beats — remind them of the problem, name the solution, assure it, state the benefit, ask for confirmation — and this is repeated for three solutions.
  why: >-
    Prospects change but the solutions stay the same, so labels, assurances and benefits can all be prepared ahead of time and the closer never has to invent anything on the fly.
  applies_when: >-
    Inside the offer; one problem is broken into micro problems to fill three solutions, more than three problems are grouped so one solution solves several.
  structure:
    - >-
      **Problem:** Remind them of their problem.
    - >-
      **Solution:** Tell them how we'll solve it specifically (think feature).
    - >-
      **Assure:** Tell them why that thing is great (decrease risk).
    - >-
      **Benefit:** Tell them the good stuff the solution gets them.
    - >-
      **Confirm:** Ask for confirmation.
  anchor: >-
    Connect their problems to our solutions, assurances, benefits, then confirm that it would help.
  source: >-
    acq-closer-handbook.md, Offer, How to Make The Offer, lines 2003–2024
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2003"
  tier: 2
- id: A-closer-027
  type: framework
  name: >-
    The 5 Objections to Buying
  statement: >-
    Every reason not to buy chunks into five buckets — time, money, decision-maker, preference, stall — each with its own way of being solved.
  why: >-
    People may say a million different things to avoid buying, but five buckets can be prepared for and a million cannot.
  applies_when: >-
    Whenever the prospect is asked to buy and does anything other than buy.
  structure:
    - >-
      **#1 Time** - The prospect says they will not buy because they do not have the time to get the value.
    - >-
      #2 Money - The prospect says they are not able or not willing to pay the price.
    - >-
      #3 Decision-Maker - The prospect says they must get permission from somebody else before they can buy.
    - >-
      #4 Preference - The prospect says they expected something different or that they'd rather do something else.
    - >-
      #5 Stall - The prospect says they must wait before they will buy.
  anchor: >-
    People may say a million different things to avoid buying. But when you chunk it up there are only *five we care about*.
  source: >-
    acq-closer-handbook.md, Objections, The 5 Objections to Buying, lines 2080–2160
  confirmations: 1
  authors_caveat: >-
    Money accounts for roughly 50% of objections, by the author's own count at line 2101.
  anchor_at: "acq-closer-handbook.md:2080"
  tier: 2
- id: A-closer-028
  type: framework
  name: >-
    The three steps for a Decision-Maker objection
  statement: >-
    A decision-maker objection is solved in three steps: find out ahead of time whether permission is needed and get that person on the call, ask whether they would approve based on past approvals and encourage deciding now, and book a follow up call with the decision-maker.
  why: >-
    If they would get approval anyway there is no reason to wait, and if they would not, the decision-maker has to be in the conversation.
  applies_when: >-
    The prospect says they must get permission from somebody else before they can buy.
  structure:
    - >-
      First, we figure out if they need permission ahead of time. If so, we get the decision-maker on the call.
    - >-
      Second, we ask if they think the decision-maker would feel ok with this based on past approvals. And if they'd get approval anyway, we encourage them to decide now.
    - >-
      Third, we book a follow up call with the decision-maker.
  anchor: >-
    We solve this in three steps. First, we figure out if they need permission ahead of time. If so, we get the decision-maker on the call.
  source: >-
    acq-closer-handbook.md, Objections, #3 Decision-Maker, lines 2113–2128
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2113"
  tier: 2
  merged_from: [B-closer-055]
- id: A-closer-029
  type: framework
  name: >-
    The three steps for a Preference objection
  statement: >-
    A preference objection is solved in three steps: remind them of the problem they want solved, pull out the short-, medium- and long-term consequences of their current ways, then explain why our way is ultimately to their benefit.
  why: >-
    The aim is to get them to realize that if we change the variables that create the outcome, we change the outcome.
  applies_when: >-
    The prospect says they expected something different or would rather do something else.
  structure:
    - >-
      first we remind them of the problem they want solved
    - >-
      Second, we pull out the short-, medium-, and long-term consequences of their current ways.
    - >-
      Third, we explain why the way we do it is ultimately to their benefit.
  anchor: >-
    To solve this, first we remind them of the problem they want solved. Second, we pull out the short-, medium-, and long-term consequences of their current ways.
  source: >-
    acq-closer-handbook.md, Objections, #4 Preference, lines 2130–2141
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2130"
  tier: 2
  merged_from: [B-closer-056]
- id: A-closer-030
  type: framework
  name: >-
    The Objection Loop
  statement: >-
    An objection is handled in three moves — acknowledge and agree with it, address it, ask for the sale again immediately — and the loop repeats on every further objection until they buy or time runs out.
  why: >-
    Adding to their reasoning and immediately giving them the chance to buy again saves them embarrassment; the salespeople who ask for the buy the most times get the most closes.
  applies_when: >-
    Every objection after the value of the product has been confirmed.
  structure:
    - >-
      **Acknowledge/Agree** with the objection.
    - >-
      **Address** the objection.
    - >-
      **Ask** for the sale *again. Immediately.*
    - >-
      Loop 4: ...Until you close
  anchor: >-
    Looping is a technique to overcome objections by acknowledging their objection, presenting your additions, and then *looping* the prospect back to the offer.
  source: >-
    acq-closer-handbook.md, Looping, The Right Way to Handle Objections, lines 2250–2343
  confirmations: 9
  authors_caveat: >-
    The objection itself is never insulted, only its content addressed; and if you are looping a lot it means you are messing up earlier in the script, since most sales close on the first and second asks.
  anchor_at: "acq-closer-handbook.md:2250"
  tier: 2
  merged_from: [B-closer-059, B-closer-064, C-closer-013, C-closer-014, C-closer-015, D-closer-031, E-closer-046]
- id: A-closer-031
  type: framework
  name: >-
    Handling the First Objection
  statement: >-
    The first objection is ignored: the closer first asks whether the product could get them closer to their goal, then asks a triage question to surface the real concern, and only then starts looping.
  why: >-
    Before getting into objection whack-a-mole you need to know whether they think the product is valuable; the triage question makes them abandon their reflex objection and isolates the one worth handling.
  applies_when: >-
    The first objection on a call, before any loop.
  structure:
    - >-
      Verify: Objection → (Acknowledge → Confirm Value)
    - >-
      **Confirming Value** — I completely hear you… do you mind if I ask you a question… Do you think doing [Product] is something that can help get you closer to [Goal]?
    - >-
      **Triage Question** — *Super helpful. What's the biggest thing holding you back... Tell me your main concern?*
  anchor: >-
    Before getting into objection whack-a-mole, we need to know something very important: Do they think our product is valuable?
  source: >-
    acq-closer-handbook.md, Looping, Handling the First Objection, lines 2264–2308
  confirmations: 5
  anchor_at: "acq-closer-handbook.md:2270"
  tier: 2
  merged_from: [A-closer-044, B-closer-062, B-closer-063, D-closer-039]
- id: A-closer-032
  type: framework
  name: >-
    BAMFAM (Book A Meeting From A Meeting)
  statement: >-
    A call that does not close ends by booking the next call while still on this one, for one of three reasons: time constraint, dependence on a decision-maker, or banking delay.
  why: >-
    Sometimes closing takes more than one call; if you will not book a call while on a call, you have no chance of booking it by text afterwards.
  applies_when: >-
    Any call that runs out of time or cannot close today; give yourself a three minute buffer for it.
  structure:
    - >-
      Time Constraint
    - >-
      Prospect depends on Decision-Maker
    - >-
      Banking Delay (For very high ticket)
  anchor: >-
    And that's totally okay. Sometimes closing takes more than one call. When it does, secure a time for the next call while on the current call.
  source: >-
    acq-closer-handbook.md, BAMFAM, lines 2454–2466
  confirmations: 5
  anchor_at: "acq-closer-handbook.md:2458"
  tier: 2
  merged_from: [A-closer-033, B-closer-072, D-closer-047]
- id: A-closer-034
  type: framework
  name: >-
    The Referral Process
  statement: >-
    Referrals are asked for in four steps: compliment the customer, ask who they know as successful as them, give them the exact words and a group chat, then ask for more.
  why: >-
    This is the least work per sale of anything in the handbook and the highest return on time; asking with a compliment means nobody is offended by it.
  applies_when: >-
    Right after closing and collecting payment, and whenever a customer sends anything positive by text.
  structure:
    - >-
      **Compliment them** - Tell them they're amazing to work with.
    - >-
      **Get introduction** - Then ask who they know as successful as them (a second compliment) that they'd want to come with them, which also improves their experience. Win-win.
    - >-
      **Give them words to use**: If they say yes, ask them to start a group chat.
    - >-
      Get more introductions – If you get one. Ask for more.
  anchor: >-
    Asking for referrals gets you the simplest, cheapest, fastest, easiest, highest-converting opportunities.
  source: >-
    acq-closer-handbook.md, Referrals, Referral Process, lines 2496–2524
  confirmations: 9
  authors_caveat: >-
    The author's own figures for this section: it should net one extra deal per day and over 30% of your sales come from it.
  anchor_at: "acq-closer-handbook.md:2503"
  tier: 2
  merged_from: [B-closer-018, B-closer-019, B-closer-052, B-closer-073, B-closer-074, B-closer-075, D-closer-048]
- id: A-closer-043
  type: framework
  name: >-
    The rapid fire metrics questions
  statement: >-
    After permission is asked, the metrics half of discovery runs as a fixed list of questions, each answer recapped before the next question is asked, ending with the constraint question.
  why: >-
    The block is announced as rapid fire to better understand the business and see if it is a fit, and every answer is recapped so the prospect keeps confirming.
  applies_when: >-
    The discovery phase of a close call, before the constraint question.
  structure:
    - >-
      Perfect. What's annual revenue?
    - >-
      Got it so [RECAP]. How about profit on that?
    - >-
      OK so [RECAP] and what's your main offer?
    - >-
      [RECAP]. Very cool. How are you currently getting clients for [RECAP]?
    - >-
      OK. Got it got it. So [RECAP]. How many new clients are you getting. Per month. On average?
    - >-
      OK so [RECAP]. And ballpark. How much do your clients spend with you?
    - >-
      OK so [RECAP] and how long have you owned [Business name]?
    - >-
      What's the biggest thing holding back growth? Marketing? Sales? People? Profit?...Something crazy?
  anchor: >-
    Great OK so I'm gonna rapid fire through a list of questions. Just to better understand the Business.
  source: >-
    acq-closer-handbook.md, ACQ Closing Script, DISCOVERY, lines 3317–3355
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3317"
  tier: 2
- id: A-closer-053
  type: framework
  name: >-
    ACQ Pipeline Phone & Text Script
  statement: >-
    A stalled or ghosting prospect is called first and then texted in five escalating steps: the five-minute follow up, value messages, check-ins, bumps, and a re-offer.
  why: >-
    The goal is to close the deal or agree on a timeline to touch base again, so each step gives the prospect a new reason to reply rather than repeating the ask.
  applies_when: >-
    A deal waiting on something off the call with no BAMFAM secured, or a prospect who has ghosted.
  structure:
    - >-
      Phone Script — wanted to touch base around [OBSTACLE THAT IS PREVENTING THE DEAL FROM MOVING FORWARD] How’s it going there? → Transition into objection overcomes/looping.
    - >-
      STEP #0: 5-MIN FOLLOW UP
    - >-
      STEP #1: VALUE MESSAGES — just saw this case study of [COMPANY SIMILAR TO THEIRS] who solved [THEIR SPECIFIC PROBLEM]
    - >-
      STEP #2: CHECK-INS — how are you feeling about [next steps/decision]?
    - >-
      STEP #3: BUMPING — should I assume this isn't a priority right now?
    - >-
      STEP 4: RE-OFFER/RE-ENGAGE — just had 3 spots open up for [DATES]. Want first dibs before I announce it?
  anchor: >-
    Start by calling. If they do not answer, transition to text. The goal is to close the deal or agree on a timeline to touch base again.
  source: >-
    acq-closer-handbook.md, ACQ Pipeline Phone & Text Script, lines 3987–4052
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:3994"
  tier: 2
  merged_from: [B-closer-089, B-closer-090]
```


## B. Правила и критерии — 32

```yaml
- id: B-closer-003
  type: rule
  name: >-
    Gametape is sold along with, not watched
  statement: >-
    Call recordings are studied with the script in hand, selling along with the salesman out loud, pausing and rewatching the hard parts until they are nailed.
  why: >-
    Watching only collects the words; the results come from roleplaying the recording rather than listening to it.
  applies_when: >-
    Gametape review, on your own or with the team.
  anchor: >-
    Have your script with you and sell along with the salesman. This is not about just getting the words. To maximize the results, you must also roleplay it.
  source: >-
    acq-closer-handbook.md, Onboarding: Schedule & Training, Gametape, line 697
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:697"
  tier: 2
- id: B-closer-007
  type: rule
  name: >-
    Pull the close call forward
  statement: >-
    On contact with an inbound set the objective is to pull the close call forward to right now, and failing that to later the same day.
  why: >-
    The appointment is at its most valuable before the prospect cools; same-day is the fallback, not a later date.
  applies_when: >-
    Working an Inbound Set that already has a future appointment.
  anchor: >-
    Your objective is to pull the close call forward. Ideally, to *right now*. And if not now, then later that day.
  source: >-
    acq-closer-handbook.md, Hunt Mode, Priority 1: Inbound Sets, line 1293
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1293"
  tier: 2
  merged_from: [A-closer-040]
- id: B-closer-008
  type: rule
  name: >-
    Double dial before you text
  statement: >-
    Every text to a prospect or customer is preceded by a double dial; texting is what you do after the call did not connect.
  why: >-
    A live conversation beats a text thread, so the phone attempt always comes first.
  applies_when: >-
    Inbound Sets, Pipeline prospects, referral outreach and opt-in outbound.
  anchor: >-
    Use the Inbound Set Phone Script and Inbound Set Text Script when working Inbound Set prospects. *Remember to double dial before you text.*
  source: >-
    acq-closer-handbook.md, Hunt Mode, Priority 1: Inbound Sets, line 1295
  confirmations: 4
  anchor_at: "acq-closer-handbook.md:1295"
  tier: 2
- id: B-closer-010
  type: rule
  name: >-
    Pipeline: newest to oldest, back 60 days
  statement: >-
    Prospects who declined or no-showed and have not opted out are contacted from newest to oldest, starting with today's, and going back no further than 60 days.
  why: >-
    The newest declines and no-shows are the likeliest to convert, and 60 days bounds how far back the pipeline is worth working.
  applies_when: >-
    Priority 3 of the list, for anyone you still have permission to call (ACQ, 2025).
  anchor: >-
    You will continue going "back in time," until you've contacted everyone who declined or no-showed in the past 60 days.
  source: >-
    acq-closer-handbook.md, Hunt Mode, Priority 3: Pipeline, line 1308
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1308"
  tier: 2
- id: B-closer-012
  type: rule
  name: >-
    A text back is answered with a call
  statement: >-
    When a prospect texts back, they are called immediately rather than answered by text.
  why: >-
    The point of the text is to get a conversation; if they do not pick up you text them back.
  applies_when: >-
    Any inbound text from a prospect during the day.
  anchor: >-
    When they text back, call them immediately.
  source: >-
    acq-closer-handbook.md, Hunt Mode, Texting Guidelines, line 1340
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1340"
  tier: 2
- id: B-closer-013
  type: rule
  name: >-
    Objections over text are answered with an appointment
  statement: >-
    An objection raised over text is handled by setting an appointment, not by typing out paragraphs of argument.
  applies_when: >-
    Text threads with prospects during Hunt Mode.
  anchor: >-
    Handle objections over text by setting appts rather than typing out paragraphs.
  source: >-
    acq-closer-handbook.md, Hunt Mode, Texting Guidelines, line 1342
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1342"
  tier: 2
  merged_from: [B-closer-081, D-closer-004]
- id: B-closer-016
  type: rule
  name: >-
    Two replies and a typing bubble means call
  statement: >-
    An ongoing text conversation is converted to a phone call after one or two replies, especially when the prospect is visibly typing.
  why: >-
    Either they pick up and you can close, pull forward or confirm them, or they say they cannot talk and the thread continues; always go for the phone call if you can.
  applies_when: >-
    Any live text exchange with a prospect.
  anchor: >-
    If you get into an ongoing text conversation with a prospect, after 1–2 replies, and a “…” on their side, call them.
  source: >-
    acq-closer-handbook.md, Hunt Mode, Working Inbound Sets: The Full Process, line 1388
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1388"
  tier: 2
- id: B-closer-017
  type: rule
  name: >-
    Pickup Primetime
  statement: >-
    At Pickup Primetime everything except a live call is dropped for two hours of outbound.
  why: >-
    Pickup Primetime falls at the end of the day because that is when pick up rates are highest, which maximizes the return on that time.
  applies_when: >-
    The end-of-day outbound block (ACQ, 2025).
  anchor: >-
    When Pickup Primetime occurs, you drop everything (except for a live call) to do outbound for the next two hours.
  source: >-
    acq-closer-handbook.md, Hunt Mode, #3 Outbound, line 1399
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1399"
  tier: 2
- id: B-closer-021
  type: rule
  name: >-
    Two hours of outbound is the floor
  statement: >-
    Every hour left over after the list is worked goes to setting your own appointments, and two hours of outbound is the minimum, not the target.
  why: >-
    Closers who do more outbound get more deals; opt-in calling should produce about two sets per hour, and four sets should yield at least one close.
  applies_when: >-
    Any day with availability after the priority list (ACQ, 2025).
  anchor: >-
    Any availability you have after working your list is dedicated to setting your own appointments. The two hour block is the minimum.
  source: >-
    acq-closer-handbook.md, Hunt Mode, #3 Outbound, line 1409
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1409"
  tier: 2
- id: B-closer-027
  type: rule
  name: >-
    Word-for-word, not "similar words in about the same order"
  statement: >-
    The script is delivered word-for-word and naturally, with no personal spin, paraphrase or improvised reordering.
  why: >-
    More sales are lost from people putting their own spin on things than from the script itself; the wording came from more calls than one closer could have in a lifetime.
  applies_when: >-
    Every call, at every level of seniority.
  anchor: >-
    You need to deliver the script word-for-word, with your eyes closed, *naturally*. More sales are lost from people putting their own spin on things.
  source: >-
    acq-closer-handbook.md, Breathe the Script, Important Note, line 1522
  confirmations: 5
  authors_caveat: >-
    The scripts in the appendix sometimes appear to bend the rules of the handbook because the missing variables are covered elsewhere in the process or by the brand.
  anchor_at: "acq-closer-handbook.md:1522"
  tier: 2
  merged_from: [D-closer-008, D-closer-009]
- id: B-closer-028
  type: rule
  name: >-
    150-170 words per minute
  statement: >-
    Speaking speed on a call stays in the range of about 150 to 170 words per minute, a little slower than normal conversation.
  why: >-
    Too fast and the prospect cannot track you or senses your stress; too slow and you sound drunk; the range is easy to measure as an average and leaves room for natural shifts.
  applies_when: >-
    Every phone call.
  anchor: >-
    The ideal range is about 150–170 words per minute.
  source: >-
    acq-closer-handbook.md, Tone, Talk Slower (Speed), line 1571
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1571"
  tier: 2
  merged_from: [D-closer-011]
- id: B-closer-029
  type: rule
  name: >-
    The prospect does four fifths of the talking
  statement: >-
    On a call that goes perfectly the closer talks about a fifth of the time, roughly three minutes of a fifteen-minute close.
  why: >-
    At 150-170 words per minute a 500-word script takes just over three minutes, so more talking than that means you are talking too much.
  applies_when: >-
    Reviewing your own call length and talk ratio.
  anchor: >-
    if a call goes perfect on your side and takes 15 minutes to close, then the prospect spoke for 12 minutes and you spoke for three.
  source: >-
    acq-closer-handbook.md, Tone, Talk Slower (Speed), line 1573
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1573"
  tier: 2
  merged_from: [D-closer-012]
- id: B-closer-031
  type: rule
  name: >-
    A question mark means pitch up
  statement: >-
    Wherever the script prints a question mark, the pitch rises at the end of that word, whatever position it holds in the sentence.
  why: >-
    A group of words does not become a question by itself; the rising pitch is what signals that you asked for information, and packs many words into one.
  applies_when: >-
    Every script that uses the (?) notation.
  anchor: >-
    So when you see question marks (?) in the script then say that word, no matter where it is, *as if you are asking a question.*
  source: >-
    acq-closer-handbook.md, Tone, Getting Prospects to Talk (Pitch), line 1617
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1617"
  tier: 2
- id: B-closer-032
  type: rule
  name: >-
    The longest pause goes after the buying question
  statement: >-
    After asking for the sale the closer stays silent, giving the buying question the longest pause of the call, eight seconds or more.
  why: >-
    Five mega studies showed a 23 to 40% increase in close rates from pausing 8+ seconds after asking for the sale; if the prospect is not forced to address the buying question head on, they will avoid it.
  applies_when: >-
    Every ask for the sale, and every re-ask inside a loop.
  anchor: >-
    Five mega studies by Harvard, UCLA, and other fancy places showed a 23 to 40% increase in close rates by pausing for 8+ seconds after asking for the sale.
  source: >-
    acq-closer-handbook.md, Tone, When You Don't Talk (Pauses), lines 1667-1712
  confirmations: 5
  anchor_at: "acq-closer-handbook.md:1667"
  tier: 2
  merged_from: [B-closer-050, D-closer-016]
- id: B-closer-034
  type: rule
  name: >-
    Do not train to sound natural
  statement: >-
    Naturalness is reached by knowing the script well enough that it becomes natural, never by practising an imitation of natural speech.
  why: >-
    Training to speak naturally is training to pretend; if you do not want to sound like you are reading a script, do not read a script.
  applies_when: >-
    Tone practice and roleplay.
  anchor: >-
    Instead of pretending to speak naturally, know the script so well it becomes natural.
  source: >-
    acq-closer-handbook.md, Tone, Advanced Tone Tactics, line 1710
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1710"
  tier: 2
  merged_from: [D-closer-015]
- id: B-closer-037
  type: rule
  name: >-
    Minimum questions, minimum words
  statement: >-
    The introduction contains only the required questions in the fewest possible words, delivered in the proper tone, and no small talk, pitch or filler.
  why: >-
    The minutes wasted at the beginning are the minutes you will wish for at the end, and a long intro can cost the sale and the referral that would have come with it.
  applies_when: >-
    The opening of every close call.
  anchor: >-
    The intro is a place to ask the minimum required questions, with the minimum required words, delivered in the proper tone.
  source: >-
    acq-closer-handbook.md, Introduction, line 1812
  confirmations: 5
  anchor_at: "acq-closer-handbook.md:1812"
  tier: 2
  merged_from: [D-closer-017, D-closer-019, D-closer-020]
- id: B-closer-040
  type: rule
  name: >-
    Only ask about results you can deliver
  statement: >-
    Discovery asks the prospect only about results in areas where the offer can produce good results, and moves to another area when the problem found is not big enough.
  why: >-
    Only problems you can solve are worth surfacing; every good result you offer becomes a result of theirs you can ask about.
  applies_when: >-
    Choosing which problems to open in Discovery.
  anchor: >-
    We only care about problems we can solve. This means one simple thing: we only ask the prospect about results in areas we can get good results.
  source: >-
    acq-closer-handbook.md, Discovery, Step 3: Obstacle, line 1881
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1881"
  tier: 2
  merged_from: [D-closer-023]
- id: B-closer-043
  type: rule
  name: >-
    When Discovery is allowed to end
  statement: >-
    Discovery ends only once you hold either one label built from several related problems or several labels from several different problems, all stated in the prospect's own words and mapped to your solution categories.
  why: >-
    Ideally one Pain Cycle is enough, but the cycle repeats until there are enough problems you can solve; have a list of results to ask about ready.
  applies_when: >-
    Step 9 of Discovery, deciding whether to cycle again or move to the offer.
  anchor: >-
    Once we have one label from multiple related problems, or multiple labels from multiple different problems, we have what we need to move on.
  source: >-
    acq-closer-handbook.md, Discovery, Step 9: Repeat Until Complete, lines 1950-1970
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1950"
  tier: 2
- id: B-closer-046
  type: rule
  name: >-
    Two minutes, about 320 words
  statement: >-
    The whole offer is delivered in about two minutes, which at 150-170 words per minute is roughly 320 words.
  why: >-
    That is plenty of words if you know what you are doing; needing more means you are wasting words.
  applies_when: >-
    The offer section of a close call.
  anchor: >-
    Remember, talking between 150–170 words per minute gives you about 320 words to make your offer.
  source: >-
    acq-closer-handbook.md, Offer, lines 1987-1989
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1989"
  tier: 2
  merged_from: [D-closer-026]
- id: B-closer-048
  type: rule
  name: >-
    Fit any number of problems to three solutions
  statement: >-
    One problem is broken into micro problems in discovery so that it maps to all three solutions, and more than three problems are grouped so that one solution answers several.
  applies_when: >-
    Building the map step of the offer.
  anchor: >-
    If they have one problem, then map it to all three solutions by breaking it into micro problems in the discovery phase.
  source: >-
    acq-closer-handbook.md, Offer, How to Make The Offer, line 2003
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2003"
  tier: 2
- id: B-closer-051
  type: rule
  name: >-
    Plug and chug: nothing invented on the call
  statement: >-
    Labels, solutions, assurances and benefits are written out before the call, so that nothing in the offer is composed live.
  why: >-
    Prospects change but the solutions stay the same; improvising risks saying something dumb, wrecking your tone, or both.
  applies_when: >-
    Preparation for close calls.
  anchor: >-
    With proper preparation you need only to “plug and chug”. You should never have to come up with anything on the fly and risk saying something dumb, screwing up your tone, or both.
  source: >-
    acq-closer-handbook.md, Offer, line 2024
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:2024"
  tier: 2
  merged_from: [D-closer-027]
- id: B-closer-053
  type: rule
  name: >-
    A time objection is a priority objection
  statement: >-
    A time objection is answered by finding lower-value things the prospect spends time on and getting them to agree those are less valuable than what is being offered.
  why: >-
    Not enough time is never an objection, only not a high-enough priority.
  applies_when: >-
    Objection type 1 of 5, Time.
  anchor: >-
    This is solved by finding lower value things they spend time on... and *getting them to agree they're not as valuable as taking the time to do what we're offering*.
  source: >-
    acq-closer-handbook.md, Objections, The 5 Objections to Buying, line 2084
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:2084"
  tier: 2
  merged_from: [D-closer-029]
- id: B-closer-060
  type: rule
  name: >-
    Address the content, never the objection itself
  statement: >-
    However weak the objection, the closer never insults or challenges the objection and addresses only its content.
  why: >-
    A prospect made to feel stupid, cornered or caught out acquires a better objection, that the closer is an asshole, and calls off the deal.
  applies_when: >-
    Every loop, with tone tightly controlled.
  anchor: >-
    no matter how silly the objection, you must *never ever* insult the objection itself. You will *only address its content*.
  source: >-
    acq-closer-handbook.md, Looping, The Right Way to Handle Objections, line 2252
  confirmations: 4
  anchor_at: "acq-closer-handbook.md:2252"
  tier: 2
  merged_from: [D-closer-036]
- id: B-closer-065
  type: rule
  name: >-
    Loop until they buy or time runs out
  statement: >-
    Looping continues until one of exactly two things happens: the prospect buys, or the call runs out of time.
  why: >-
    They will eventually run out of objections and you will never run out of loops, so every successful loop moves you closer to the close.
  applies_when: >-
    Any close call that reaches objections.
  anchor: >-
    This means you keep looping until one of two things happen. They buy or you run out of time.
  source: >-
    acq-closer-handbook.md, Looping, The Second Objection and Beyond, line 2316
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:2316"
  tier: 2
  merged_from: [D-closer-040]
- id: B-closer-066
  type: rule
  name: >-
    "And," never "But"
  statement: >-
    The acknowledgement is joined to your addition with "and"; the word "but" never appears.
  why: >-
    "But" works like a big fat eraser telling the prospect to ignore everything before it, which disrespects them and costs the sale.
  applies_when: >-
    Every acknowledge step of every loop.
  anchor: >-
    “And,” never “But”. Think of “But” like a big fat eraser. It means ignore all the words before it.
  source: >-
    acq-closer-handbook.md, Looping, line 2369
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:2369"
  tier: 2
  merged_from: [D-closer-042]
- id: B-closer-068
  type: rule
  name: >-
    Heavy looping is a symptom, not a skill
  statement: >-
    A call that needs many loops is read as a failure earlier in the script, not as good closing; the great majority of sales close on the first and second ask.
  applies_when: >-
    Reviewing your own calls and gametape.
  anchor: >-
    If you are looping a lot, it means you are messing up earlier in the script.
  source: >-
    acq-closer-handbook.md, Looping, Helpful Points About Looping, line 2441
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2441"
  tier: 2
  merged_from: [D-closer-044]
- id: B-closer-069
  type: rule
  name: >-
    Three-minute buffer before the next call
  statement: >-
    When another call follows immediately, the closer keeps three minutes free and spends them booking a time to finish closing this prospect.
  applies_when: >-
    A loop still running as the next appointment approaches.
  anchor: >-
    If you have a call right after this one, then give yourself a three minute buffer. Use that three minutes to book a time to finish closing them.
  source: >-
    acq-closer-handbook.md, Looping, Helpful Points About Looping, line 2445
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2445"
  tier: 2
- id: B-closer-077
  type: rule
  name: >-
    Cash thresholds that keep a set alive
  statement: >-
    When a price objection on a setting call turns out to be budget rather than value, financial questions are asked, and the appointment is set when the prospect has $15K or more cash on hand or $10K a month of cash flow.
  applies_when: >-
    The "too expensive" obstacle on the Outbound Set Phone Script (ACQ, 2025).
  anchor: >-
    IF THEY HAVE $15K+ CASH OR $10K/MO CASH FLOW
  source: >-
    acq-closer-handbook.md, ACQ Outbound Set Phone Script, Obstacles to Book a Meeting, line 2847
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2847"
  tier: 2
  merged_from: [D-closer-053]
- id: B-closer-079
  type: rule
  name: >-
    Every booked appointment is manually nurtured
  statement: >-
    Between the set and the call the prospect gets a manual text sequence: an intro, the pre-call video, a night-before message and a morning-of message.
  why: >-
    Manual nurture has raised show rates more than anything the author has seen across the portfolio.
  applies_when: >-
    Every appointment between the set and the close call (ACQ, 2025).
  anchor: >-
    Manual nurture has boosted show rates more than anything I have seen across our portfolio.
  source: >-
    acq-closer-handbook.md, ACQ Outbound Reminder Text Script, Why this is important, line 3064
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:3064"
  tier: 2
  merged_from: [A-closer-039]
- id: B-closer-083
  type: rule
  name: >-
    An unwatched pre-call video is watched on the call
  statement: >-
    A prospect who did not watch the pre-call video is asked to watch it during the call while the closer goes on mute, rather than being talked through it.
  why: >-
    The five-minute video saves about twenty minutes of the call.
  applies_when: >-
    The introduction, when the prospect confirms they have not seen the video.
  anchor: >-
    that's the video, it's just 5 min and will save us about 20 here today. Do you mind giving that a quick watch, I'll go on mute and we can jump in once you finish?
  source: >-
    acq-closer-handbook.md, ACQ Closing Script, INTRO, line 3268
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3268"
  tier: 2
- id: B-closer-086
  type: rule
  name: >-
    More than three days out means value messages
  statement: >-
    When the booked meeting is more than three days away, the gap is filled with value-based messages: a testimonial, a third-party review or a value video.
  applies_when: >-
    Nurturing a BAMFAM booked far out.
  anchor: >-
    Send a value-based message with one of the following:
  source: >-
    acq-closer-handbook.md, ACQ BAMFAM Script, IF BOOKED MORE THAN 3-DAYS, line 3908
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3908"
  tier: 2
  merged_from: [A-closer-050]
- id: B-closer-088
  type: rule
  name: >-
    No-show cadence: text now, again at five minutes, then outbound
  statement: >-
    A no-show is double dialled, texted immediately, texted again with two reschedule times if nothing comes back within five minutes, and added to the end-of-day outbound block if there is still no response.
  applies_when: >-
    A prospect who does not pick up at the scheduled time.
  anchor: >-
    Add these to your outbound block at the end of the day if you do not get responses. If they pick up → OUTBOUND SET PHONE SCRIPT
  source: >-
    acq-closer-handbook.md, ACQ No Show Script, lines 3972-3980
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3980"
  tier: 2
  merged_from: [A-closer-052]
```


## C. Разборы (кейсы) — 25

```yaml
- id: C-closer-003
  type: case
  name: >-
    Pauses In Action — the fit line
  statement: >-
    One line of the opening frame is printed with its pauses marked, then broken down clause by clause: the pauses after FIT, AND and IF SO are shown to say "we will make you an offer only if you are a fit" without the closer ever saying it.
  why: >-
    Placing the pauses makes the point as obvious as screaming it while the closer stays professional and chill.
  demonstrates: >-
    Pauses focus attention; the conditional frame of the introduction.
  anchor: >-
    I just want to make sure our product is a fit...And—if so—I’m happy to walk you through it.
  source: >-
    acq-closer-handbook.md, Tone, lines 1680-1696
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1682"
  tier: 2
  merged_from: [C-closer-002]
- id: C-closer-004
  type: case
  name: >-
    The girl that got away
  statement: >-
    A deliberately absurd four-line opening ("This is the girl that got away / Calling from my bed / Because I know we had something special / I've set up a camera for us to watch later... you got 20 minutes?") is dissected to show it contains exactly the four elements the law requires — identity, where the call comes from, the reason for the call, and that it is recorded — and that the format therefore cannot be what kills calls.
  why: >-
    If the same four elements work in that opening, then bad experiences with the compliant opening come from the prospect not liking or trusting the rep, the company or the reason for the call, not from the format itself.
  demonstrates: >-
    The four things every call must open with; the rejection of "it sounds like a sales call" as a reason to skip them.
  anchor: >-
    I guarantee he'd continue into the discovery phase (Ahem.) But, more importantly it has her identity, where she calls from, the reason she calls, and that the call is recorded.
  source: >-
    acq-closer-handbook.md, Introduction, lines 1752-1775
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1765"
  tier: 2
- id: C-closer-005
  type: case
  name: >-
    INTRO IN ACTION
  statement: >-
    The whole introduction is shown as three beats: name plus company plus product plus recorded line plus "how's it going?", then the time box ("We only have 20 minutes though. Cool if we jump in?"), then the agenda — metrics to check fit, walk through the product if a fit, set up if it makes sense — each closed with a confirmation question.
  why: >-
    The intro frames the rest of the call and can be blown in thirty seconds; minutes wasted at the start are minutes wanted at the end, and a long intro can cost the sale and the referral with it.
  applies_when: >-
    The first 30-60 seconds of every call.
  demonstrates: >-
    Minimum required questions, minimum required words, proper tone; the conditional fit frame.
  anchor: >-
    We'll just spend a couple minutes diving through your metrics to make sure you're a fit... And—if so—happy to walk you through [PRODUCT]... and if things make sense we can get you all set up.
  source: >-
    acq-closer-handbook.md, Introduction, lines 1786-1804
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1801"
  tier: 2
- id: C-closer-006
  type: case
  name: >-
    Recapping, Labeling, and Confirming Put Together
  statement: >-
    One worked line shows the three steps in a row: the problem repeated in the prospect's words ("not getting as many leads as you want"), then stated in the seller's label ("some marketing issues"), then checked ("Does that sound about right?").
  why: >-
    Every problem the prospect has should be mapped to a solution the seller offers, and the label is the word that will be carried into the offer, so it has to be confirmed as correct before the offer is built on it.
  demonstrates: >-
    Steps 6-8 of the 9 Steps of Discovery and the five labels (Marketing, Sales, Product/Delivery, People, Profit).
  anchor: >-
    So you're [not getting as many leads as you want] **Label** - It sounds like you've got some marketing issues. **Confirm** - Does that sound about right?
  source: >-
    acq-closer-handbook.md, Discovery, line 1940
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1940"
  tier: 2
  merged_from: [C-closer-025]
- id: C-closer-008
  type: case
  name: >-
    Mapping one problem: "Not enough leads"
  statement: >-
    A single labelled problem is carried through the five sub-steps with concrete wording for each: Problem ("For your 'Not enough leads' issue..."), Solution (you get to ask questions of our director of marketing), Assure (he leads ad and content strategy for the companies we advise), Benefit (he can help you improve your funnel conversion, content, ads), Confirm ("Do you think that would help?").
  why: >-
    Listing benefits and asking for money abandons the pain points the discovery produced; mapping each problem to a named solution with an assurance and a benefit is what makes the offer personal on the spot.
  demonstrates: >-
    Step 2 (Map) of the offer-making process: Problem, Solution, Assure, Benefit, Confirm.
  anchor: >-
    **Solution:** Tell them how we'll solve it specifically (think feature). Ex: *When you come out, you'll get to ask questions to our director of marketing.*
  source: >-
    acq-closer-handbook.md, Offer, lines 2005-2013
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2007"
  tier: 2
  merged_from: [E-closer-036]
- id: C-closer-009
  type: case
  name: >-
    A COMPLETELY STACKED OFFER: PLUG AND CHUG
  statement: >-
    The full offer is laid out as a fill-in template: transition and permission, then solution 1 with assurance and benefit and a confirmation question, then solutions 1+2 restated, then 1+2+3 restated, then the whole stack repeated from three angles, then the buying question, then the price and the card menu.
  why: >-
    Labels, solutions, assurances and benefits are all known in advance, so a prepared closer never has to invent anything on the fly and risk saying something dumb or wrecking the tone.
  applies_when: >-
    Roughly two minutes and about 320 words at 150-170 words per minute.
  demonstrates: >-
    Transition, Map, Stack (three times), Ask, Drop Price & STFU.
  anchor: >-
    So given [Problem(s)]... it looks like you’ll get the most from [Solution1]. It’s [Assurance1] so you can [Benefit1]... How does that sound?
  source: >-
    acq-closer-handbook.md, Offer, lines 2026-2057
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2044"
  tier: 2
- id: C-closer-010
  type: case
  name: >-
    The "Gotcha" Moment
  statement: >-
    A door-to-door dialogue is run to failure — the rep answers "can't afford it" by pointing at the BMW and the new deck, the prospect says "I think we're done here", the door slams — and the manager then supplies the replacement line, "That's a fair point. What would need to happen for this to make sense financially?", as the same goal with no confrontation.
  why: >-
    Even when the excuse is false, challenging it directly calls the prospect a liar to his face; he feels foolish and attacked and now has a good objection, so catching prospects in their objections feels clever but the only one who thinks so is the closer.
  demonstrates: >-
    The wrong way to handle objections; agree and add rather than contradict.
  anchor: >-
    You made him feel foolish and attacked. You could have said, ‘That’s a fair point. What would need to happen for this to make sense financially?’
  source: >-
    acq-closer-handbook.md, Looping, lines 2179-2199
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2197"
  tier: 2
- id: C-closer-018
  type: case
  name: >-
    Three closes that answer nothing
  statement: >-
    Three lines are given that can follow any reason a prospect gives — that is the exact reason you should come; most people just make it work anyways; best case you xyz, worst case you zyw — and the author points out they do not answer the objection at all, they only agree and ask again.
  why: >-
    On the author's own account the response given matters almost not at all; what matters is being able to ask again, which is why agreement is the point.
  authors_caveat: >-
    The author marks this as controversial and frames it as wanting the reader to be rich rather than right.
  demonstrates: >-
    Agreement exists to buy more opportunities to ask for the sale.
  anchor: >-
    … let’s just think about it like this “best case” you xyz, worst case you zyw. How’s that sound?
  source: >-
    acq-closer-handbook.md, Looping, lines 2384-2394
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2392"
  tier: 2
- id: C-closer-019
  type: case
  name: >-
    Time Constraint BAMFAM In Action
  statement: >-
    The unclosed call is ended in five moves: name the time overrun and say it could really help, offer two named times (branching on whether the block was time, a decision-maker or a banking delay), restate the agreed day and time, send the invite while still on the call and have them confirm receipt, then send an immediate follow-up text.
  why: >-
    Both parties are on the call now, so a closer who will not book a call while on a call has no chance of booking one by text afterwards; "do not say we'll follow up offline".
  applies_when: >-
    The close needs more than one call because of a time constraint, a decision-maker or a banking delay; give yourself a three minute buffer.
  demonstrates: >-
    BAMFAM — Book A Meeting From A Meeting.
  anchor: >-
    If Decision-Maker or Banking Delay: Do you think you'll get that taken care of today or tomorrow? Great. Let's pick this up then.
  source: >-
    acq-closer-handbook.md, BAMFAM, lines 2473-2483
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:2479"
  tier: 2
  merged_from: [C-closer-020]
- id: C-closer-021
  type: case
  name: >-
    Give them words to use
  statement: >-
    Instead of leaving the introduction to the customer, the closer dictates the exact message for the group chat, naming the event, the invitation and the rep, and ending with "I'll let you guys take it from here."
  why: >-
    Handing the customer a line to copy and paste removes the work of composing an introduction and keeps the rep's credibility inside the referrer's own words.
  applies_when: >-
    Step 3 of the referral process, once the customer has agreed to introduce someone.
  demonstrates: >-
    The four-step Referral Process: compliment, get introduction, give them words to use, get more introductions.
  anchor: >-
    Tell them to say: “I’m going to Alex Hormozi’s scaling workshop in Vegas. Thought you might want to come. This is [Salesman name] - he’s been great.
  source: >-
    acq-closer-handbook.md, Referrals, lines 2505-2518
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2516"
  tier: 2
- id: C-closer-022
  type: case
  name: >-
    Referrals In Action
  statement: >-
    Straight after payment the ask runs as compliment ("you're the exact type of business owner we love to work with"), then the introduction request phrased as a second compliment ("who else do you know who's as successful as you"), backed by a reason — a few spots left on that date — then the group text, then "anyone else come to mind?".
  why: >-
    Referrals are the simplest, cheapest, fastest, easiest, highest-converting opportunities and should net an extra deal a day; business owners are not offended by the ask, especially when it comes with a compliment.
  applies_when: >-
    Right after closing and collecting payment, or after a customer sends anything positive by text.
  demonstrates: >-
    The Referral Process and the claim that over 30% of sales come from referrals.
  anchor: >-
    **Get Introduction:** Who else do you know who’s as successful as you that would benefit from this? I ask because we have a few spots left on that date and I’d love to fill it with a couple people you know.
  source: >-
    acq-closer-handbook.md, Referrals, lines 2526-2535
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:2530"
  tier: 2
  merged_from: [C-closer-057]
- id: C-closer-026
  type: case
  name: >-
    "TOO EXPENSIVE" on a set call
  statement: >-
    The objection is first split into budget or value ("is it more of a budget thing? ...or if you saw the value... would you consider it?"); a value answer continues the script, a budget answer opens permission for financial questions — monthly cash flow, then cash on hand — and at $15K cash or $10K a month of cash flow the rep says there might be a way to make it work and asks to set the consultant call.
  why: >-
    Splitting the objection turns an unanswerable "too expensive" into either a value conversation the script already handles or a factual question about money that has a threshold answer.
  demonstrates: >-
    Isolating an objection before overcoming it; the Money objection.
  anchor: >-
    hmmm, is it more of a budget thing? ...or if you saw the value in the [PRODUCT]... would you consider it?
  source: >-
    acq-closer-handbook.md, ACQ Outbound Set Phone Script, OBSTACLES TO BOOK A MEETING, lines 2824-2853
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2826"
  tier: 2
- id: C-closer-027
  type: case
  name: >-
    "I DON'T KNOW MY CONSTRAINT"
  statement: >-
    A prospect who cannot name their problem is handed a closed menu — marketing, sales, people, profit, or operations — and if they still say they are not sure, asked which single fix in the business would drive the most growth.
  why: >-
    A forced choice from a short list produces the labelled problem the rest of the script needs, where an open question produced nothing.
  demonstrates: >-
    Labelling the problem; the same five-way menu used in the Closing Script's constraint question.
  anchor: >-
    Hmm....If you had to say it was one of— marketing, sales, people, profit, or operations... which would it be?
  source: >-
    acq-closer-handbook.md, ACQ Outbound Set Phone Script, lines 2855-2867
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2857"
  tier: 2
- id: C-closer-030
  type: case
  name: >-
    "I CAN'T LEAVE MY BUSINESS"
  statement: >-
    The rep normalises the problem among other attendees, names it key man risk, asks permission to offer a perspective, states that the product exists to save time by solving the problem faster, and reframes the trade as reallocating time rather than taking it away before asking again.
  why: >-
    The objection is treated as the very problem the product addresses, so agreeing with it strengthens rather than weakens the ask.
  demonstrates: >-
    The Time objection reframed as priority; agree, add, ask again with permission questions at each step.
  anchor: >-
    So, it’s not about taking time away…just allocating it differently ?…Would you be totally against exploring how we could help?
  source: >-
    acq-closer-handbook.md, ACQ Outbound Set Phone Script, lines 2892-2908
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2906"
  tier: 2
  merged_from: [C-closer-042]
- id: C-closer-031
  type: case
  name: >-
    Play out both scenarios
  statement: >-
    For "I need to solve a business problem first", the rep asks permission to play out both futures: if the problem is solved, the lead time (booked out at least six weeks) means the timing works and the next set of problems is next; if it is not solved by then, the team helps break past it — so either way the meeting is a win-win, closed with "would it be crazy just to have a conversation about it?".
  why: >-
    Both branches of the prospect's own reasoning are made to end in the same action, which removes the reason to wait without contradicting him.
  applies_when: >-
    Also used verbatim against "I ALREADY HAVE A SOLUTION", with the advisor in place of the prospect solving it.
  demonstrates: >-
    Agree and add rather than contradict; the Stall objection answered with the cost of waiting.
  anchor: >-
    Got it. So you solve that and we get you out… and get you out here…I think we are booked out at least 6 weeks anyways?…so it actually works well…(haha) then we can tackle the next set of problems…
  source: >-
    acq-closer-handbook.md, ACQ Outbound Set Phone Script, lines 2910-2932
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:2921"
  tier: 2
  merged_from: [C-closer-033]
- id: C-closer-036
  type: case
  name: >-
    The hold-the-spot nudge
  statement: >-
    A silent prospect is not chased with another reminder but told someone else wants the slot and asked for a one-character reply — a thumbs up or a bell emoji — to keep it.
  why: >-
    A request that costs one tap gets an answer where a question does not, and the scarcity of the slot supplies the reason to answer now.
  applies_when: >-
    No reply to the reminder or to the second non-response text before a booked call.
  demonstrates: >-
    Escalating non-response texts before cancelling the appointment.
  anchor: >-
    Hey [Name], I finished prepping for our meeting, though I have someone requesting that time. Could you please send a quick &lt;img&gt;bell emoji&lt;/img&gt; so I can hold the spot?
  source: >-
    acq-closer-handbook.md, ACQ Inbound Set Text Script, line 3207
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3207"
  tier: 2
- id: C-closer-039
  type: case
  name: >-
    Cancel and rebook after silence
  statement: >-
    Twelve hours before a call the prospect has not answered about, the appointment is cancelled in writing, the silence is excused as busy business-owner life, and a new date is proposed in the same message.
  why: >-
    Cancelling frees the slot while the excuse and the immediate re-offer keep the lead from being lost to the cancellation.
  applies_when: >-
    No responses at all up to twelve hours out from the scheduled call.
  demonstrates: >-
    The cancel/reschedule branch of the inbound workflow.
  anchor: >-
    Hey [Name], since I did not hear back, I've canceled our meeting. But, I know business owner life is busy...would you be free tomorrow by chance?
  source: >-
    acq-closer-handbook.md, ACQ Inbound Set Text Script, line 3213
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3213"
  tier: 2
- id: C-closer-044
  type: case
  name: >-
    "I see the value in it... I just don't have the money"
  statement: >-
    The rep confirms it is only about the finances, isolates it with a hypothetical ("if you had the money today, would anything else prevent you from getting started?"), asks permission for a financial question, takes monthly cash flow and cash on hand with a recap in between, and then proposes setting everything up to hold the date.
  why: >-
    The hypothetical proves money is the only remaining objection before any work is done on it, and the money objection is then a matter of facts rather than feelings.
  demonstrates: >-
    Isolating the objection; the Money objection.
  anchor: >-
    So if you had the money today. Would anything else prevent you from getting started?
  source: >-
    acq-closer-handbook.md, Money Objections, lines 3568-3594
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3577"
  tier: 2
- id: C-closer-045
  type: case
  name: >-
    "It's really expensive"
  statement: >-
    The rep agrees the price is high and turns it into a reason it will work — a high price makes the buyer care and act — tests it against a $500 version they would not believe in, then quotes Warren Buffet on price versus value, asks whether they see the value, and closes.
  why: >-
    The price is reframed as the mechanism of the result rather than as a cost to be justified.
  demonstrates: >-
    The Money objection solved by comparing what the problem costs with what the solution costs; agree and add.
  anchor: >-
    I think it’s good that it’s a lot...it means you’ll actually care and be more likely to take action. I mean if it were only $500—would you even believe it was valuable?
  source: >-
    acq-closer-handbook.md, Money Objections, lines 3598-3608
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3600"
  tier: 2
- id: C-closer-047
  type: case
  name: >-
    "I just don't know if I see the value"
  statement: >-
    The rep turns to the free content the prospect already consumed and asks what it has done for them, then branches: growth from the content proves the source works and the product is the tactical version of it; no growth is attributed to not being able to apply it, which is exactly what the product supplies — both branches ending in an ask, with the no-guarantees line repeated.
  why: >-
    The prospect's own history with the material supplies the evidence, so either answer becomes a reason to buy rather than a point to argue.
  demonstrates: >-
    Agree and add rather than contradict; asking for the sale again at the end of every branch.
  anchor: >-
    Got it—Well let me ask you this…earlier you mentioned you consumed [CONTENT]— what has that done for you so far?
  source: >-
    acq-closer-handbook.md, Money Objections, lines 3658-3683
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3660"
  tier: 2
- id: C-closer-048
  type: case
  name: >-
    "I need to talk to my spouse or business partner"
  statement: >-
    The rep isolates the other person as the only blocker, asks what their biggest concern would be, loops that concern as its own objection, then offers the reversal — if the partner hates the idea, call me and I will make sure you are taken care of — and asks for the order; a persistent no is met with "what if she/he says no?", an "I would go anyways" with the order, and an "I need to talk to them" with a BAMFAM for the conversation.
  why: >-
    The absent decision-maker's objection is the one that actually has to be handled, and the reversal removes the risk of deciding without them.
  demonstrates: >-
    The Decision-Maker objection; isolate, loop the real objection, ask for the order, BAMFAM as the fallback.
  anchor: >-
    Cool so typically what we do in this situation...because it's [INSERT REASON WHY]—Then if your [SPOUSE/BUSINESS PARTNER] absolutely hates the idea of you [RIDICULOUS BENEFIT #1] AND [RIDICULOUS BENEFIT #2]...then you can give me a call and I will make sure you are taken care of—fair enough?
  source: >-
    acq-closer-handbook.md, Decision-Maker, lines 3693-3734
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3728"
  tier: 2
- id: C-closer-051
  type: case
  name: >-
    "I went to a similar [PRODUCT] and I didn't like it"
  statement: >-
    The rep diagnoses the bad experience first — how many people were there, did you get personalised help from the speakers, were they just not tactical enough — and only then asks permission to describe the structure, starting by ruling out the thing they disliked ("if you're looking for a RARA event, this isn't that") before the pre-work, small groups and three to five tactical steps, closing with a confidence check and "Is there any reason we shouldn't do this?".
  why: >-
    The prospect's objection is to a different thing, and that can only be shown after the difference has been established from their own answers.
  demonstrates: >-
    Pull Teeth applied to a preference objection; agree and add, then ask again.
  anchor: >-
    First off, if you're looking for a RARA event, this isn't that.
  source: >-
    acq-closer-handbook.md, Preferences, lines 3772-3801
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3782"
  tier: 2
  merged_from: [C-closer-049]
- id: C-closer-053
  type: case
  name: >-
    "I need to think about it"
  statement: >-
    The rep asks permission to be upfront, states that almost everyone locks in their spot and the exceptions come down to one of two reasons — they do not see the value, or logistics — checks the value in passing, and asks the prospect to pick number two or something crazy.
  why: >-
    A stall with no stated reason is converted into a forced choice from a short list, which produces the real objection the loop can handle.
  demonstrates: >-
    The Stall objection; isolating the objection worth handling.
  anchor: >-
    Yeah so typically almost everyone is ready to lock in their spot… and if not it’s really because of 1 or 2 reasons.
  source: >-
    acq-closer-handbook.md, Stall Objections, lines 3833-3842
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3837"
  tier: 2
- id: C-closer-054
  type: case
  name: >-
    "I always take 24 hours to make a decision"
  statement: >-
    The rep respects the rule, asks whether any new information is making them reconsider, asks permission to share a perspective, reports that the large owners he watches make quick logical decisions when they see value, confirms the prospect sees the value, and asks whether it would be absolutely crazy to break the rule.
  why: >-
    The prospect's own rule is not attacked; a model of how decision makers he admires behave is offered instead, and breaking the rule becomes his choice.
  demonstrates: >-
    The Stall objection; agree and add, then ask again.
  anchor: >-
    The cool part of my job is I get to see the decision making process of Alex and Leila and other large business owners. They make quick logical decisions when they see value.
  source: >-
    acq-closer-handbook.md, Stall Objections, lines 3844-3859
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3855"
  tier: 2
- id: C-closer-055
  type: case
  name: >-
    "It's a big commitment / I need time"
  statement: >-
    The rep names the decision as big, then names the nervousness, then turns it into the reason to start — people who start nervous do great — and tests it by asking whether, having paid, they would let things fall through the cracks or come in, ask their questions and implement; the answer confirms nervousness predicts taking it seriously, then value and action are confirmed and the card menu closes it.
  why: >-
    The emotion behind the stall is made into evidence for buying rather than something to be talked out of, and the prospect states the commitment himself.
  demonstrates: >-
    The Stall objection; agree and add; asking for the sale immediately after agreement.
  anchor: >-
    If you put down [PROGRAM COST], do you think you would just let things fall through the cracks? Or do you feel you would come in, ask all your questions, implement everything we give you, and make the most out of your time here?
  source: >-
    acq-closer-handbook.md, Stall Objections, lines 3861-3875
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:3869"
  tier: 2
```


## D. Антипаттерны и границы — 7

```yaml
- id: D-closer-013
  type: rule
  name: >-
    Talking quieter works in person, not on the phone
  statement: >-
    The tactic of lowering your voice so people listen harder is accepted for in-person selling and rejected for phone selling.
  why: >-
    Over the phone they turn the volume up anyway, or ask you to repeat yourself, or strain to hear — which annoys business owners rather than persuading them.
  boundary: >-
    The author grants the opposing tactic inside its medium and limits his own rule to the phone.
  anchor: >-
    Some people argue that if you talk quieter then people will listen harder. And I agree, *in-person*.
  source: >-
    acq-closer-handbook.md, Tone, Talk Louder (Volume), line 1575
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1575"
  tier: 2
- id: D-closer-028
  type: antipattern
  name: >-
    Asking do you have any questions
  statement: >-
    Asking the prospect whether they have any questions, which the author treats as asking them for reasons not to buy.
  why: >-
    The author states the consequence for the rep directly: being benched and made an example of.
  anchor: >-
    If you ever ask “do you have any questions?” you will be benched and made an example of. I do not recommend asking prospects for reasons not to buy.
  source: >-
    acq-closer-handbook.md, Offer, PRO TIP, line 2063
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2063"
  tier: 2
- id: D-closer-038
  type: rule
  name: >-
    Any response short of a clear no is fear
  statement: >-
    A prospect who genuinely did not want the offer would say so, so every other response is read as the normal fear of doing something new.
  why: >-
    The product is new to them and not to us, so the closer's job is to help them past that fear rather than to corner them.
  boundary: >-
    The author's own premise for looping, and the one case it excludes: a prospect who says outright they do not want it.
  anchor: >-
    if they truly didn’t want what we offered, they would say so. This means any other response is just their natural fear of doing something new.
  source: >-
    acq-closer-handbook.md, Looping, The Right Way to Handle Objections, line 2262
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2262"
  tier: 2
- id: D-closer-043
  type: rule
  name: >-
    The content of the answer matters almost not at all
  statement: >-
    The author holds that the specific response given to an objection matters far less than being able to ask again, and that logic matters almost not at all.
  why: >-
    His top closes can follow any reason a prospect gives and do not answer the objection at all: they agree and ask again; if the prospect feels good, they buy.
  boundary: >-
    The author flags this himself as a personal note and as controversial, and states his aim as making the closer rich rather than right.
  anchor: >-
    The more I’ve studied sales and persuasion, the less I think the response you give matters.
  source: >-
    acq-closer-handbook.md, Looping, On a personal note, line 2384
  confirmations: 2
  authors_caveat: >-
    Marked by the author as controversial and as his own view rather than a team standard.
  anchor_at: "acq-closer-handbook.md:2384"
  tier: 2
- id: D-closer-050
  type: rule
  name: >-
    A script is one part of a larger process
  statement: >-
    An element missing from one script is usually covered elsewhere in the process, so a single script is not evaluated on its own.
  why: >-
    The inbound closing script is light on the pain cycle because the prospect has to watch one or two videos before the call, so that section was trimmed without hurting close rates.
  boundary: >-
    A script may be copied only together with the process around it; lifting one out of that process removes the compensating steps.
  anchor: >-
    These scripts operate together as part of a larger sales process. So variables that aren’t covered in one are likely covered in another part of the process.
  source: >-
    acq-closer-handbook.md, Appendix: Script Bank, line 2640
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2640"
  tier: 2
- id: D-closer-051
  type: rule
  name: >-
    The brand has already done some of the selling
  statement: >-
    These scripts assume many prospects already know the company, so part of the selling has happened before the call and the scripting accommodates that.
  why: >-
    Other variables have already made the horse more likely to drink, so the script does not have to do that work.
  boundary: >-
    The author's explicit caveat that his scripts suit a known brand and are not calibrated for a company the prospect has never heard of.
  anchor: >-
    Our brand is different from many companies. We have many prospects who already know who we are. This means that some selling has already occurred.
  source: >-
    acq-closer-handbook.md, Appendix: Script Bank, line 2641
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2641"
  tier: 2
- id: D-closer-055
  type: rule
  name: >-
    Stop pushing payment and BAMFAM
  statement: >-
    When every payment route has been offered and refused, the money objection is dropped and the call is converted into a booked next meeting.
  why: >-
    The author frames the exhausted attempts as covering all the bases; with no way to pay, the next step is a timeline, not another ask.
  boundary: >-
    The author's stop condition on the money objection, against the general rule of looping until the buy.
  anchor: >-
    IF NO AGAIN → All good haha— just wanted to cover all the bases. BAMFAM.
  source: >-
    acq-closer-handbook.md, Money Objections, line 3656
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:3656"
  tier: 2
```


## E. Глоссарий — 13

```yaml
- id: E-closer-001
  type: term
  name: >-
    Selling
  statement: >-
    Selling means maximizing the likelihood a prospect buys, nothing more.
  definition: >-
    First, **selling** means *maximizing the likelihood a prospect buys*. That's it.
  not_to_confuse_with: >-
    Persuading or convincing a single prospect by argument; the author frames selling as arranging conditions so that buying becomes the most likely response, the way a horse is made to drink.
  why: >-
    If selling is a matter of likelihood, then every condition you control moves the odds, and nothing is left to whether the prospect was in the mood.
  anchor: >-
    First, **selling** means *maximizing the likelihood a prospect buys*. That’s it.
  source: >-
    acq-closer-handbook.md, What is Selling?, line 483
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:483"
  tier: 2
  merged_from: [E-closer-002]
- id: E-closer-008
  type: term
  name: >-
    Hunt Mode
  statement: >-
    Hunt Mode is everything a closer does to get prospects on the phone, and it maximizes opportunities while increasing conversion.
  definition: >-
    **Hunt Mode:** Everything you do to get prospects on the phone. This is where you sharpen your tools, lay your snares, and track your targets. Hunting maximizes opportunities and increases conversion.
  why: >-
    Hunting is more important than killing because you cannot take a shot without something to shoot.
  anchor: >-
    **Hunt Mode:** Everything you do to get prospects on the phone. This is where you sharpen your tools, lay your snares, and track your targets.
  source: >-
    acq-closer-handbook.md, On-Going: Schedule, line 1028
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1028"
  tier: 2
- id: E-closer-009
  type: term
  name: >-
    Kill Mode
  statement: >-
    Kill Mode is everything a closer does while on the phone to get the sale, and it maximizes conversion while increasing opportunities.
  definition: >-
    **Kill Mode:** Everything you do while on the phone to get the sale. This is where you bring the pain, make your offer, loop any objections, and go for the kill.
  not_to_confuse_with: >-
    Hunt Mode, everything done to get prospects on the phone; a closer is always in one of the two modes.
  anchor: >-
    **Kill Mode:** Everything you do while on the phone to get the sale. This is where you bring the pain, make your offer, loop any objections, and go for the kill.
  source: >-
    acq-closer-handbook.md, On-Going: Schedule, line 1030
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1030"
  tier: 2
- id: E-closer-015
  type: term
  name: >-
    Pickup Primetime
  statement: >-
    Pickup Primetime is the end-of-day two-hour window when pick-up rates are highest, during which everything except a live call is dropped for outbound.
  definition: >-
    When Pickup Primetime occurs, you drop everything (except for a live call) to do outbound for the next two hours. Pickup Primetime happens at the end of the day because that's when our pick up rates are highest.
  why: >-
    It maximizes your return on time and maximizes your opportunities.
  anchor: >-
    When Pickup Primetime occurs, you drop everything (except for a live call) to do outbound for the next two hours.
  source: >-
    acq-closer-handbook.md, Hunt Mode, #3 Outbound, line 1399
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:1399"
  tier: 2
- id: E-closer-021
  type: term
  name: >-
    Breathe the script
  statement: >-
    Breathing the script means delivering it word-for-word, with your eyes closed, naturally, so knowing it costs no attention.
  definition: >-
    You need to deliver the script word-for-word, with your eyes closed, *naturally*.
  not_to_confuse_with: >-
    Reading it, or merely memorizing it, or using similar words in about the same order, which the author calls wrong.
  why: >-
    If you cannot remember what to say, have to look for it, or read it, you are not paying attention to the prospect, and then you say the wrong stuff and do not close.
  anchor: >-
    Most people think “breathe the script” means “use similar words in about the same order”. *This is wrong*. You need to deliver the script word-for-word, with your eyes closed, *naturally*.
  source: >-
    acq-closer-handbook.md, Breathe the Script, line 1522
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1522"
  tier: 2
- id: E-closer-029
  type: term
  name: >-
    Pain Cycle
  statement: >-
    The Pain Cycle is steps 3–8 of discovery — Obstacle, Reason, Pull Teeth, Recap, Label, Confirm — run after the current and desired results are established and repeated until there are enough solvable problems.
  definition: >-
    Once we get the prospect to state their current and desired results, we start the Pain Cycle:
  applies_when: >-
    Ideally run once; repeated when a problem is not big enough, with a list of results ready to ask about.
  anchor: >-
    Once we get the prospect to state their current and desired results, we start the Pain Cycle:
  source: >-
    acq-closer-handbook.md, Discovery, line 1849
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:1849"
  tier: 2
- id: E-closer-032
  type: term
  name: >-
    Label
  statement: >-
    A Label states the prospect's problem in our words, using one of five categories — Marketing, Sales, Product/Delivery, People, Profit — that map to the solutions offered later.
  definition: >-
    Thankfully, we only describe them in five—and these five, listed below, are the labels we use to map to our offer later.
  why: >-
    Business owners describe their problems in a million ways, and the label is what the solution and benefits in the offer are mapped to.
  anchor: >-
    Thankfully, we only describe them in five—and these five, listed below, are the labels we use to map to our offer later.
  source: >-
    acq-closer-handbook.md, Discovery, lines 1919–1936
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1924"
  tier: 2
- id: E-closer-035
  type: term
  name: >-
    Solution stack
  statement: >-
    The solution stack is the set of solution-and-benefit pairs mapped to the prospect's problems, listed again after each mapping and three times in total before asking for the sale.
  definition: >-
    So what words should you say? Your solution stack.
  applies_when: >-
    In the offer, which lasts two minutes, about 320 words at 150–170 words per minute.
  anchor: >-
    It just means... you must make every word count. So what words should you say? Your solution stack.
  source: >-
    acq-closer-handbook.md, Offer, lines 1989–2015
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:1989"
  tier: 2
- id: E-closer-038
  type: term
  name: >-
    Drop Price & STFU
  statement: >-
    Drop Price & STFU is the last step of the offer: state the price and then stop talking.
  definition: >-
    5) **Drop Price & STFU:** Then you state the price and shut the fuck up.
  why: >-
    The longest pause always goes after the buying question, because it forces the prospect to address it head on instead of avoiding it.
  anchor: >-
    5) **Drop Price & STFU:** Then you state the price and shut the fuck up.
  source: >-
    acq-closer-handbook.md, Offer, line 2017
  confirmations: 1
  anchor_at: "acq-closer-handbook.md:2017"
  tier: 2
- id: E-closer-042
  type: term
  name: >-
    Money objection
  statement: >-
    A Money objection is the prospect saying they are not able or not willing to pay the price, and it is roughly half of all objections.
  definition: >-
    #2 Money - The prospect says they are not able or not willing to pay the price. This is solved by showing how much the problem costs compared to the solution. This accounts for roughly 50% of objections.
  anchor: >-
    #2 Money - The prospect says they are not able or not willing to pay the price.
  source: >-
    acq-closer-handbook.md, Objections, line 2101
  confirmations: 2
  anchor_at: "acq-closer-handbook.md:2101"
  tier: 2
- id: E-closer-047
  type: term
  name: >-
    Confirming Value
  statement: >-
    Confirming value is the step before any looping: ignore the first objection and ask whether the prospect thinks the product can help get them closer to their goal.
  definition: >-
    Do they think our product is valuable? To get that information we must confirm the value.
  applies_when: >-
    On the first objection, before getting into objection whack-a-mole.
  anchor: >-
    Do they think our product is valuable? To get that information we must confirm the value.
  source: >-
    acq-closer-handbook.md, Looping, line 2270
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:2270"
  tier: 2
  merged_from: [C-closer-011]
- id: E-closer-048
  type: term
  name: >-
    Triage question / reflex objection
  statement: >-
    The triage question follows the value confirmation whatever the answer, and gets the prospect to abandon their reflex objection so the objection actually worth handling is isolated.
  definition: >-
    The main objective is to get them to abandon their "reflex" objection. This way, you isolate the objection worth handling.
  anchor: >-
    The main objective is to get them to abandon their “reflex” objection. This way, you isolate the objection worth handling.
  source: >-
    acq-closer-handbook.md, Looping, lines 2282–2291
  confirmations: 4
  anchor_at: "acq-closer-handbook.md:2282"
  tier: 2
  merged_from: [C-closer-012, C-closer-041]
- id: E-closer-049
  type: term
  name: >-
    AGREE… AND…
  statement: >-
    AGREE… AND… is the acknowledgement formula that opens every loop: agree with the objection, then add the line of reasoning with and, never but.
  definition: >-
    What comes after the "AGREE… AND…" will be the line of reasoning we add to their own, depending on their reason.
  not_to_confuse_with: >-
    Agree… but…: the author calls But a big fat eraser that means ignore all the words before it, and says using it will cost the sale.
  why: >-
    The acknowledgement is disarming because prospects expect an argument, and agreement buys you more opportunities to ask again.
  anchor: >-
    What comes after the “AGREE… AND…” will be the line of reasoning we add to their own, depending on their reason.
  source: >-
    acq-closer-handbook.md, Looping, lines 2369–2382
  confirmations: 3
  anchor_at: "acq-closer-handbook.md:2382"
  tier: 2
  merged_from: [C-closer-017]
```
