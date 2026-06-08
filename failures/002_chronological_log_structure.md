# Failure 002: Chronological Log Structure

## Symptom

The chapter moves through time blocks rather than through conflict, pressure, choice, or consequence.

It may look organized, but it reads like a process log.

## Why It Happens

LLMs often use time order as the safest narrative scaffold when the next chapter's engine is under-specified.

## Bad Pattern

```text
morning setup
midday work
small trade
evening lesson
after-lesson conversation
```

or:

```text
wakes up
gets assigned
works
learns something
reflects
```

## Detection Rule

Mark REVISE if:

- time labels are the main progression device
- events could be reordered without major consequence
- no central conflict escalates across the chapter
- the chapter only records routine actions

## Repair Strategy

Replace time order with event engine.

Use one of:

```text
external notice
public consequence
relationship choice
failed imitation
resource conflict
rule revealed through consequence
opponent action first
inspection / test / deadline
```

## Regression Test

Ask:

```text
What is the chapter's main engine?
What changes because of that engine?
Can the scenes be reordered without damage?
```

If the answer is weak, revise before drafting.

## Related Governance Files

- `governance/longform_ai_inertia_check.md`
- `governance/chapter_brief_review.md`
- `prompts/02_chapter_brief.md`
- `prompts/04_review_hook.md`
