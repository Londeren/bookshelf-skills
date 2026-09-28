# Answer-shape smoke of the `hormozi` skill, 2026-09-28

The check behind version 0.2.0 of the skill: the same three cases of the eval set run on 0.1.1 and on the skill with its output rules rebuilt by book-to-skill 1.1.0, one run each. It is a smoke, not a rerun of the eval set: three cases, one sample per arm.

## Why

The first consumer read a long document produced with the skill and found it hard to read: 96 rule numbers in 3,845 words, source years, the author's caveats retold, "the method says" as a refrain and "my opinion, not the method's" with no method named. The skill asked for it: a diagnosis without a rule number was "an opinion", every threshold carried its year and caveat, and the check before handing over hunted for missing numbers. Book-to-skill 1.1.0 moved the rule numbers of a generated skill's answer into a basis block at its end and made a request for the basis a check against the sheets rather than a new search.

## How it was run

- **The rebuild.** A separate Opus subagent read book-to-skill 1.1.0 (SKILL.md and the sheet on the output format) and rewrote, in a copy of 0.1.1, the answer shape of `SKILL.md` and the section "Before handing over" of sheet 16, by that sheet alone. The smoke ran on its version. The hand edits made after the smoke (the enterprise-value note restored, the scope line, the figures line, the check split into six questions) were not run.
- **The cases.** S-01 (advice: an accounting outsourcer with CAC four times the industry's), M-01 (review: a CRM offer to dental clinics), M-04 (apply: a price-raise letter), requests verbatim from `../eval-set.md`.
- **The arms.** One Opus subagent per case and arm, the body of `SKILL.md` in an intro file with the paths of the sheets, as an installed skill loads; r1–r3 on 0.1.1, r4–r6 on the rebuilt skill.
- **The grading.** Two blind graders with the prompt of book-to-skill's sheet on evals, the basis blocks cut from the answers first (`strip.py`), the two arms of a case never in one batch. The assertions of `../eval-set.md` were reworded to be neutral to the shape: the parts "citing NN.M" and "each step with a rule number of the form NN.M" were dropped, since the rebuilt skill keeps the numbers out of the body by design and the fit pass below checks them instead.
- **The counts.** `metrics.py <sheets_dir> <answer.md>...` counts the words, the basis block, the rule numbers above it and inside it, the rules that are not in the sheets, "метод" and the source years in the body.
- **The fit pass.** A separate grader took every line of every basis block of r4–r6, read the Rule and When not to apply fields of each rule it names, and judged whether the rule says what the step says.
- **The basis on request.** The subagent of r4 got the follow-up «Откуда взят каждый шаг и точно ли это из книг Хормози? Проверь себя на галлюцинации.» Its reply is `outputs/r4-followup.md`; every English passage it quotes was searched in the sheets as an exact substring.

## Results

| | S-01, advice | M-01, review | M-04, apply |
|---|---|---|---|
| Rule numbers in the body, 0.1.1 → rebuilt | 23 → 0 | 50 → 0 | 35 → 0 |
| "метод" in the body | 5 → 0 | 2 → 0 | 1 → 0 |
| Source years in the body | 6 → 0 | 1 → 0 | 4 → 0 |
| Words | 678 → 551 | 1,096 → 865 | 1,200 → 1,201 |
| Basis block of the rebuilt answer | 5 lines, 13 numbers | 7 lines, 20 numbers | 12 lines, 24 numbers |
| Assertions passed, 0.1.1 → rebuilt | 5 → 4 | 4 → 4 | 3 → 4 |

- **Assertions.** 12 of 15 in both arms.
  - S-01 rebuilt fails the assertion that the one question (do the engaged leads have the problem and the money) is put before any advice. The answer opens with the budget verdict and gives the branch, "the need is there, the money is not, so it is the advertising", without the question itself: the rebuilt rules give the result of the diagnosis, not the walk through it. The assertion asks for the walk.
  - M-01 fails the "reason why" of the discount in both arms.
  - M-04 names the loyalty discount of 3 600 ₽ in both arms: the finding waived in phase 4. M-04 on 0.1.1 also lost its list of changes.
- **Invented rules.** None in either arm: every cited number exists in the sheets. In the rebuilt arm all 57 basis pairs fit their steps (S-01 13, M-01 20, M-04 24). The one item without a basis line is a question of the "could not check" part, not a step.
- **The basis on request.** The reply quotes 7 Rule fields and 7 anchors, and all 14, with 2 more quoted phrases, were found verbatim in the sheets. It says it checked the sheets, not the books. It names two rules from the Lost Chapters as a lower tier. It finds three places where its first answer gave its own suggestion unmarked (a forecast, a line of reasoning, the portrait of the target client) and corrects them. After this finding, the check before handing over got its own question on an unmarked suggestion; that question was not run.

## Files

- `outputs/r1.md`, `r2.md`, `r3.md`: S-01, M-01, M-04 on 0.1.1.
- `outputs/r4.md`, `r5.md`, `r6.md`: the same cases on the rebuilt skill.
- `outputs/r4-followup.md`: the reply to the request for the basis.
- `metrics.py`, `strip.py`: the counts and the grading copies.
