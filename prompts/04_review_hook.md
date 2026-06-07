# Review Hook Prompt

Use this prompt after a chapter draft is written and before chapter state is created.

## Inputs

Read:

- the chapter draft
- the current novel project file
- the current novel style file
- the current novel glossary / approved term list
- the current arc outline or chapter roadmap
- opening design or golden-three design when reviewing chapters 1-3 or a new major opening
- relevant character files
- relevant world or object files
- previous chapter state
- `governance/review_checklist.md`
- `governance/anti_ai_taste_check.md`
- `governance/emotional_payoff_check.md`
- `governance/reader_reward_check.md`
- `prompts/05_golden_three_review.md` when reviewing chapters 1-3 or the opening as a unit

## Decision

Return one of:

- ALLOW
- REVISE

## Checks

Check main drive, wiki consistency, terminology, knowledge boundaries, character behavior, style, long-form direction, reader reward, emotional repayment, dialogue naturalness, and anti-AI taste.

For chapters 1-3 or a new major opening, also check whether the chapter serves the opening design and whether the three-chapter retention unit remains strong.

## Required Story Checks

1. Arc alignment.
   The chapter must serve a known arc beat, roadmap beat, opening beat, or explicitly approved course correction. If it reads like the story is inventing direction chapter by chapter, mark REVISE.

2. Terminology gate.
   Scan for unexplained terms, new place labels, job labels, system labels, evaluation labels, shorthand phrases, and genre-sounding compact terms. If a term is not ordinary language and is not approved by the glossary, mark REVISE.

3. First-use clarity.
   If an approved term appears for the first time in the current draft but the scene does not make its meaning clear, mark REVISE.

4. Golden-three alignment.
   For chapters 1-3, the chapter must serve its specified opening function. If chapter 1 does not create immediate reader pull, chapter 2 does not create visible payoff, or chapter 3 does not expand the hook into a longer arc, mark REVISE.

5. Reader reward ledger.
   Identify the reader expectation, the obstacle, the protagonist's action, the visible gain, who notices, and what next possibility opens. If the chapter creates no visible gain or next possibility, mark REVISE.

6. Emotional ledger.
   Identify what pressure, humiliation, injustice, fear, or frustration the reader feels through the protagonist. Then identify what visible compensation the chapter gives back. If the chapter only adds pressure and repays nothing visible, mark REVISE unless the arc outline explicitly calls for a short-term loss.

7. Visible payoff.
   The payoff must be visible on the page. It can be a win, reversal, discovery, returned humiliation, status shift, resource gain, relationship turn, new leverage, risk avoided, hostile reaction, watcher notice, or clearer threat. A hidden clue alone is not enough.

8. Social confirmation.
   If the chapter contains a payoff, check whether someone notices or reacts. A reaction is not always required, but it often makes the payoff legible. If the payoff is too private to feel real, mark REVISE.

9. Dialogue naturalness.
   Dialogue should arise from desire, fear, impatience, status, misunderstanding, concealment, bargaining, or practical need. If lines mainly explain the plot, ask reader questions, set up jokes, or make the protagonist look sharp, mark REVISE.

10. Dialogue readability.
   Dialogue may have subtext, but it should not make the reader work too hard. If too many lines are half-said, indirect, or ambiguous, mark REVISE.

## Golden Three Unit Review

After chapter 3 is drafted, run a separate opening-unit review using `prompts/05_golden_three_review.md`.

Do not continue into normal long-form chapters until the opening-unit review returns PASS or the user explicitly approves proceeding despite issues.

## Hard Anti-AI Checks

These are high-priority checks:

1. Adjacent template reuse.
   If two similar events appear close together, check whether the second event changes narrative focus. If it repeats the same sequence with different names or details, mark REVISE.

2. Ending over-summary.
   If the chapter ending defaults to a polished, symmetrical, aphoristic, or explanatory summary line, check whether it can be replaced by action, object, bodily sensation, unfinished choice, concrete consequence, or changed relationship. If yes, mark REVISE.

## Conditional Anti-AI Checks

These are context-dependent checks:

- repeated jokes, objects, phrases, or reactions
- recurring side characters used only as response machines
- protagonist solving too many problems cleanly over time
- chapter lacking a concrete memory point when the chapter is an opening, new arc, or major turn
- chapter not advancing long-term pressure unless it is intentionally a breather
- guesses, claims, or observations being treated as confirmed facts

Do not apply every conditional check as a hard rule to every chapter.

## Output Format

```text
Decision: ALLOW / REVISE

Main reason:

Terminology check:
- Undefined terms:
- Terms needing clearer first use:
- Required replacements:

Opening/golden-three check if applicable:
- Opening beat:
- Retention risk:
- Required opening fix:

Reader reward ledger:
- Reader expectation:
- Obstacle:
- Protagonist action:
- Visible gain:
- Witness or reaction:
- Next possibility:

Emotional ledger:
- Pressure:
- Protagonist action:
- Cost:
- Visible compensation:
- Who notices:
- New expectation:

Required fixes if REVISE:
1.
2.
3.
```

List only the most important fixes.
