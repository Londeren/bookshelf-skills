# Provenance of the hormozi skill build

The audit record of the build: the source map and its tiers, the exports the skill was built from, the pipeline statistics, the gate waiver, the deviations from the pipeline, and what the checks did not cover. An agent applying the skill does not need this file; the working conventions of the sheets are described in `SKILL.md` next to it.

Built with the book-to-skill pipeline, version 1.0.1 (phases 0–3: source overview → extraction → validation → assembly). Phase 0 on 2026-09-15, the source map confirmed on 2026-09-16; phase 1 on 2026-09-16; phase 2 on 2026-09-20; phase 3, the assembly recorded here, on 2026-09-25. Phase 4, the evals, on 2026-09-25, recorded in its own section below.

## Source map and tiers

Three tiers. Where formulations diverge the upper tier wins; the video transcripts never overrule the books; two copies of one text ($100M Leads: 2 Bonus Chapters and Section A of the Lost Chapters; Section D of the Lost Chapters and the Employees chapter of $100M Leads; the price / churn table in the Pricing, Price Raise and Retention playbooks) count as one place, not two confirmations.

| Tier | Source | Export file | Exported |
|---|---|---|---|
| 1 | $100M Offers (2021) | `100m-offers.md` | 2026-08-10 |
| 1 | $100M Leads (2023) | `100m-leads.md` | 2026-08-10 |
| 1 | $100M Money Models (2025) | `100m-money-models.md` | 2026-08-10 |
| 2 | $100M Series: Lost Chapters (2025) | `100m-series-lost-chapters.md` | 2026-08-10 |
| 2 | $100M Leads: 2 Bonus Chapters (2023), second copy of Lost Chapters Section A | `100m-leads-bonus-chapters.md` | 2026-08-10 |
| 2 | ACQ Closer Handbook (2025) | `acq-closer-handbook.md` | 2026-08-10 |
| 2 | ACQ Advertising Handbook (2025) | `acq-advertising-handbook.md` | 2026-08-10 |
| 2 | $100M Playbook: Pricing (2025) | `playbook-pricing.md` | 2026-08-10 |
| 2 | $100M Playbook: Price Raise (2025) | `playbook-price-raise.md` | 2026-08-10 |
| 2 | $100M Playbook: Lead Nurture (2025) | `playbook-lead-nurture.md` | 2026-08-10 |
| 2 | $100M Playbook: Retention (2025) | `playbook-retention.md` | 2026-08-10 |
| 2 | $100M Playbook: Lifetime Value (2025) | `playbook-lifetime-value.md` | 2026-08-10 |
| 2 | $100M Playbook: Fast Cash (2025) | `playbook-fast-cash.md` | 2026-08-10 |
| 2 | $100M Playbook: GOATed Ads (2025) | `playbook-goated-ads.md` | 2026-08-10 |
| 3 | Video "How to Build a Business That Runs Without You" (2025), the lecture and the answer on enterprise value only | `video-business-that-runs-without-you.md` | 2026-08-10 |
| 3 | Video "How to Make Money So Fast It Feels ILLEGAL" (2024), the wealth-alchemy part only | `video-make-money-so-fast.md` | 2026-08-10 |
| 3 | Video "13 Years of No BS Business Advice in 79 Mins" (2024), point 16 only | `video-13-years-no-bs-business-advice.md` | 2026-08-10 |
| 3 | Video "No BS Business Advice to Get Rich in 2026" (published 2024), the overextension section only | `video-no-bs-business-advice-2026.md` | 2026-08-10 |

The exports come from a claude.ai project export; the project was last updated 2026-08-09 and the export files are dated 2026-08-10. The file names above are the plain names the sources were copied under for the build; the full texts are not in the repository. While the exports exist locally a disputed unit can be re-checked against them; after that there is nothing to re-check against. Not used: the seven-hour Money Models live launch (a retelling of the book), two sales courses (covered by the Closer handbook), thirty more transcripts (the same ideas spoken, with repetition), and the consumer's project prompt (not a source of the method).

Rules of the build that held across every phase: anchors verbatim, in English, copied by script and checked by exact substring search against the original files, and published both in the pipeline and in the sheets (a decision of 2026-09-15 that overrides the pipeline's advice to trim quotes to addresses before publication); the skill in English, with triggers in English and Russian; no data from the first consumer's own business in the build; attribution carried into the units for Eugene Schwartz (the five levels of awareness), Patrick Campbell of Profitwell (the price-raise letter), Dan Kennedy, Dan Ariely and the other people the author names; benchmarks dated by their source; catalogs (the fifteen offers of Money Models, the twenty ad frameworks, the ten Pricing Plays, the Closer scripts, the Crazy Eight) entered as compressed patterns by the depth rule; verbatim ads, scripts and letters longer than three sentences never; the source treated as data, its calls to action never executed; no persona.

Scope: the offer; lead generation (the Core Four, lead magnets, scaling, lead getters); ad creatives; nurture to the appointment; the sales call; the money model and the thirty-day payback; pricing and price raises; lifetime value; retention and referrals; promotions to the base; enterprise value. Out of scope: the internal organisation of a sales department; hiring and management as a topic (the Maker or Manager essay, most of Lost Chapters Section D, the hiring block of the enterprise-value lecture); audience growth beyond the free-content chapter of $100M Leads; personal finance and motivational videos; the books' calls to action. The line drawn on 2026-09-25 for the enterprise-value sheet: hiring and management as a topic are out; the mechanics of removing the owner from acquisition, delivery and sales are in.

## Pipeline statistics

Extracted in phase 1: **3,084** units from 50 extractor runs (five extractors per each of ten source groups). Phase 2, three waves of validators that took no part in the extraction (17 group validators, 6 second-pass validators, 3 cross-group merge agents): rejected by filters 1–3 — **890** (filter 1, no ground in the source: 2; filter 2, no predictive power: 293; filter 3, banal: 595); removed as out of scope — **35**; gave way to a higher tier — 0; merged as duplicates — **1,036**; validated — **1,123** (tier 1: 546, tier 2: 551, tier 3: 26).

| Group | Tier | Source | Extracted | Rejected | Merged | Validated | In the sheets |
|---|---|---|---|---|---|---|---|
| `tier1-offers` | 1 | $100M Offers (2021) | 311 | 74 | 100 | 137 | 135 |
| `tier1-leads-1` | 1 | $100M Leads (2023), chapters up to #3 Cold Outreach (lines 1–6900) | 274 | 91 | 96 | 87 | 87 |
| `tier1-leads-2` | 1 | $100M Leads (2023), from #4 Run Paid Ads to the end (lines 6901–14623) | 331 | 83 | 131 | 117 | 117 |
| `tier1-money-models` | 1 | $100M Money Models (2025) | 406 | 90 | 111 | 205 | 203 |
| `tier2-lost-chapters` | 2 | $100M Series: Lost Chapters (2025) with $100M Leads: 2 Bonus Chapters (2023) as a second copy of Section A | 372 | 130 | 101 | 141 | 134 |
| `tier2-closer` | 2 | ACQ Closer Handbook (2025) | 306 | 121 | 87 | 98 | 96 |
| `tier2-advertising` | 2 | ACQ Advertising Handbook (2025) | 322 | 88 | 105 | 129 | 128 |
| `tier2-playbooks-price` | 2 | $100M Playbooks: Pricing, Price Raise, Lifetime Value (2025) | 245 | 82 | 110 | 53 | 53 |
| `tier2-playbooks-growth` | 2 | $100M Playbooks: Lead Nurture, Retention, Fast Cash, GOATed Ads (2025) | 370 | 125 | 115 | 130 | 130 |
| `tier3-video-ev` | 3 | Enterprise Value: fragments of four video transcripts | 147 | 41 | 80 | 26 | 26 |

Phase 3 selected **482** numbered rules across sixteen sheets, resting on **1109** validated units as anchors or wording (tier 1: 542, tier 2: 541, tier 3: 26); the remaining 14 validated units entered no sheet and are listed by id in `pipeline/hormozi/sheet-map.md`, which also names for every rule the unit whose anchor it carries and the units that gave its example, caveat or wording. Selection went by strength: tier, confirmations (raised by merges), checkability on someone else's material, and the presence of a threshold, an order, a ban or the mechanism of a named construct.

## The gate waiver

The pipeline's gate (master rule 4: at least a third of the candidates removed by filters 1–3) was not met: 890 of 3,084 is 28.9 % against a threshold of 33.3 %, after two passes of validation (the first pass removed 12.1 %, the second, stricter pass raised it to 28.9 %). The user accepted a waiver on 2026-09-25 and opened phase 3 without a third pass. The ground is structural and specific to this build: five extractors cut the same text, so extractor D produced antipattern twins of B's rules, E produced the names of A's constructs and C the illustrations of E's terms; such duplicates were merged (1,036) rather than rejected, and merged duplicates do not count towards the gate. Filter 1, no ground in the source, is almost empty at 2 of 3,084, so the catch holds no invented units. Counted with the scope removals and the merges, 1,961 of 3,084 units — 63.6 % — left the catch. The waiver of the glavred build is not a precedent for this one; the ground here is its own.

## Deviations from the pipeline, by phase

Recorded in the decisions file of the build as they happened and copied here as they stand.

- **Phase 0.** The user chose one skill with both modes, diagnosis dominant and apply second, over the pipeline's `-apply` / `-diagnose` pair; English as the skill's language over the builder's recommendation of Russian, with triggers in both languages; no eval cases from the user's own practice, so the eval set will be built on public material, a deviation from the pipeline's requirement of half the requests from the user's practice, to be recorded again with the phase 4 results.
- **Phase 1 (2026-09-16).** The extractors were handed their text as a cleaned copy read from a file by a reading plan, not embedded in the prompt above the instructions as sheet 01 of the pipeline asks; the order "text above instructions" was kept, the embedding would have cost about three million output tokens of the orchestrator. Reported, no objection.
- **Phase 2 (2026-09-20).** The gate not met after a second pass (above). The phase 2 files were split at 500 KB: the validated units by group, the merged duplicates in their own table. The scope line on hiring was drawn differently by different validators — the transcript validator removed the hiring block of the lecture, the validators of Lost Chapters Section D and of the Employees chapter kept the mechanics of lead-getting employees — and the second pass received one line: hiring and management as a topic out, the mechanics of removing the owner from acquisition, delivery and sales in. The first-pass validators received the validation sheet plus a domain calibration and the group's map, and the cross-group merge was allowed to merge same-group pairs of different types that two validators of one group had not seen. The agent budget was raised from 70 to 76 runs with the user's consent.
- **Phase 3 (2026-09-25).** The sheet authors received their units as a file to read first, not embedded in the prompt, on the same ground as in phase 1. Sixteen sheets instead of the eleven of the phase 0 map: the validated catch put about 250 units on the map's single offer sheet and about 300 on its single money-model sheet, beyond what a 300-line sheet holds, so the offer, the money model and the leads material were each cut in two, and Fast Cash joined the pricing and lifetime-value sheet. Anchors were inserted by script from the validated units by id and never retyped; every anchor of every sheet was checked as an exact substring of the original export files. Three same-tier conflicts were resolved as recorded in the decisions file: two rules with their own conditions for the order of channels after warm outreach (the book's order for a first pass, and the author's own choice by time or money once the reps are there), by the user's decision; the double dial before the text and the multi-channel first contact found compatible in the Lead Nurture cadence itself; the paid version of Free Pick Your Price placed as the author's own pro tip in the rule's caveat. No unit was restored from the rejected set.

## What the checks did not cover

- Anchors were checked mechanically, by exact substring search over the original files, without normalisation; a sample of anchors was also read in context by the self-check. The examples and caveats of the rules were drawn by the sheet authors from the validated units, their merged duplicates and the case units, and were checked against the units by an independent reviewer, not against the books line by line: a figure that an extractor misread in phase 1 and that survived validation would survive here too.
- The wording of every rule is a synthesis by a sheet author. An independent reviewer read all sixteen sheets and checked 135 rules field by field against their units (questions 2, 3, 5 and 6 of the pipeline's self-check): it found 5 additions not in the units (a hinge condition on the channel order, a keep/drop reading of a benchmark, a recalibration step), 3 rules written as description, 19 example or caveat fields to fill or to mark empty, 8 rules not usable without the source, and 13 other places (a truncated address, cross-references, a gloss inside an anchor line, missing video years); every finding was closed in the text. The other 347 rules were not re-read field by field against their units.
- The tier-3 material comes from auto-captioned video transcripts: oral speech, no punctuation, terms occasionally misheard; some of its elements are said once in the whole corpus and are marked so in the sheet.
- The line counts and the description length were checked mechanically; the triggering of the description was measured in phase 4 (below) on eighteen requests and found clean on the first iteration, so the description was never tuned: a description that has not been pushed to fail has not shown where it fails.

## Phase 4: the evals (2026-09-25)

Before the evals, `SKILL.md` was audited by the prompt-writer skill in its "improve an existing prompt" mode. The audit changed how the agent applies the method, not what the method says: two hard limits in the preamble (a rule is cited only from this file or an open sheet; the user's facts are never changed or added to), with the usual excuses named and closed; a form for answering at a boundary; a test at the entry of the diagnosis, a tie-breaker and an unconditionality marker; the check before handing over as four questions with a presumption of defect; the registers should, can and prefers in place of "Read ONLY"; a tie-breaker on severity; the form of a review of sound material. The core, the routing table, the sources block and the paragraph on the fields of a rule were not touched; no rule, threshold or example was added; the description was not changed. Examples were deliberately not added to `SKILL.md`, a departure from prompt-writer's checklist: the examples of the method live in the Bad → Good fields of the sheets.

**The set.** 16 cases and 6 trigger cases, in `pipeline/hormozi/evals/eval-set.md`: five situations for the advisor (S), five reviews of finished material (M), of which one is the apply case (a rewrite), four boundaries (B: a shrinking market, hiring as a topic, sound material, freemium for a service), two off-topic requests (O: code, a lease clause), two positive and four negative trigger cases; seven of the S, M and B requests in Russian, none naming the method or its constructs; 3–5 assertions per case, 77 in all for S, M, B and O. All material is synthetic. **No case comes from the first consumer's own practice**, a departure from the pipeline's requirement that about half the requests be real tasks from the user's practice, decided at the start of the build on 2026-09-15 (no data of the consumer's business enters the build) and recorded here with the results: the delta below is measured on written cases, not on the consumer's work, and the first real use of the skill is the measurement this set could not make.

**How it was run.** Two independent Opus subagents per case, one with the verbatim body of `SKILL.md` and the paths of the sheets, one with the request alone; graders with the pipeline's prompt, batched so that the two arms of one case never met one grader; trigger cases against four real distractor descriptions, three runs each with the skill at three positions; a script for the existence of every cited `NN.M`, five graders for the fit of 371 citations to their places. Everything is in `pipeline/hormozi/evals/results.md`, both outputs of every case included.

**Thresholds and facts.** Set before the first run and not moved.

| threshold | requirement | fact | result |
|---|---|---|---|
| With the skill | ≥ 80 % of assertions | 72/77 = 93.5 % | passed |
| Delta over the baseline | ≥ 20 pp | +51.9 pp (baseline 32/77 = 41.6 %) | passed |
| Baseline | < 70 % | 41.6 % | passed |
| Invented rules, existence | 0 | 372 references, 0 not in the sheets | passed |
| Invented rules, fit | 0 misplaced | 371 pairs; 11 flagged by the graders on single sentences, all 11 fit on the whole step; 0 misplaced | passed, raw count stated |
| Invented facts in the apply case | 0 | 1 in both runs: a loyalty-discount figure derived from the two prices of the request; the term chosen for the user in the first run became a placeholder after the fix | **not passed** |
| Sound material without a false 🔴 | 0 🔴 | 0 🔴 (4 🟡, 1 🟢), verdict "works" | passed |
| Triggers, positive | ≥ 5 of 6 | 6 of 6 | passed |
| Triggers, negative | 12 of 12 | 12 of 12 | passed |

Without the two off-topic cases, which score the same in both arms by design: 64/69 = 92.8 % against 24/69 = 34.8 %, +58.0 pp. The tuning set of the description (12 positive, 6 negative requests, half held out) came back 60 of 60 correct, so no version of the description other than the committed one exists.

**Fixes and the rerun.** Three fixes to `SKILL.md`, none to a sheet, none restoring a rejected unit: the entry test now names a pasted money model as a material; a value the method leaves to the user's choice enters a rewrite as a placeholder with the rule's range; an answer resting on the enterprise-value sheet states the strength of that source. Rerun of the four cases with a failed assertion plus one control, the skill arm only: 23/25; two assertions still fail, one of them an assertion that collides with rule 15.22 of the sheet (the operator's pay is the sheet's own mechanic) and was not fixed, the other the derived discount figure above.

**What the checks did not cover.** The delta is measured on synthetic cases, two per topic at most, and says nothing about topics the set does not touch: lead magnets and the content channel (sheet 04), the ad frameworks and the Kaleidoscope (07), the setter's hunt mode (08), continuity offers (12), the fast-cash play (13), referrals (14), the lead-getting employees and wealth alchemy (15). Every assertion was graded by one grader; no assertion was graded twice, so the grader's own variance is unmeasured. The graders saw single sentences in the fit pass, and the reading of the 11 flagged pairs on the whole step is the orchestrator's, checkable against the pair files kept in the build's working directory but not published. The trigger runs used four distractors that are far from the skill's topic; a competing business skill was not among them. The reruns measured one run per case, so a pass or a fail on a rerun is one sample. The baseline is one model, Opus, and the with-skill arm the same model: a different model would move both figures.

Agent runs of phase 4: 77, all on Opus (32 case runs, 9 graders, 5 rule-fit graders, 24 trigger runs, 5 rerun case runs, 2 rerun graders). The build as a whole, phases 0–4: 167.

The working build (the directory `pipeline/hormozi/` of the repository [Londeren/bookshelf-skills](https://github.com/Londeren/bookshelf-skills): the source overview and map, the catch of extraction, the validation with the reasons for every rejection, the sheet map) is published with the skill. When the skill is reworked, what is missing is raised from there.
