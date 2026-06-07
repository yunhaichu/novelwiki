# Review Hook Prompt

Use this prompt after a chapter draft is written and before chapter state is created.

## Inputs

Read:

- the chapter draft
- the current novel project file
- the current novel style file
- the current arc outline or chapter roadmap
- relevant character files
- relevant world or object files
- previous chapter state
- `governance/review_checklist.md`
- `governance/anti_ai_taste_check.md`

## Decision

Return one of:

- ALLOW
- REVISE

## Checks

Check main drive, wiki consistency, knowledge boundaries, character behavior, style, long-form direction, reader payoff, dialogue naturalness, and anti-AI taste.

## Required Story Checks

1. Arc alignment.
   The chapter must serve a known arc beat, roadmap beat, or explicitly approved course correction. If it reads like the story is inventing direction chapter by chapter, mark REVISE.

2. Reader payoff.
   The chapter must give a felt payoff. This can be a win, reversal, discovery, humiliation returned, status shift, resource gain, relationship turn, new leverage, or clearer threat. If the chapter only records process, mark REVISE.

3. Dialogue naturalness.
   Dialogue should arise from desire, fear, impatience, status, misunderstanding, concealment, bargaining, or practical need. If lines mainly explain the plot, ask reader questions, set up jokes, or make the protagonist look sharp, mark REVISE.

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

Required fixes if REVISE:
1.
2.
3.
```

List only the most important fixes.
