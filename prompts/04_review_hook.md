# Review Hook Prompt

Use this prompt after a chapter draft is written and before chapter state is created.

## Inputs

Read:

- the chapter draft
- the current novel project file
- the current novel style file
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

Check main drive, wiki consistency, knowledge boundaries, character behavior, style, long-form direction, and anti-AI taste.

Pay special attention to:

- repeated jokes, objects, phrases, or reactions
- side characters used only as response machines
- overly polished closing lines
- protagonist solving too many problems cleanly
- chapter lacking a concrete memory point
- chapter not advancing the current novel's long-term pressure or consequence
- guesses, claims, or observations being treated as confirmed facts

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
