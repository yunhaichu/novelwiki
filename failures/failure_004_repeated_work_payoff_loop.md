# Failure 004: Repeated Work-Payoff Loop

## Failure ID

failure_004_repeated_work_payoff_loop

## Failure Name

Repeated assignment, cost, and payoff skeleton.

## Where It Appears

Serial chapters, early arcs, training arcs, workplace arcs, school arcs, cultivation arcs, management arcs.

## Symptom

Adjacent chapters repeat the same internal engine with different surface objects.

Common shape:

```text
protagonist receives or chooses a task
others mock or doubt them
task creates visible cost
ending or lesson confirms a small gain
```

## Root Cause

The model learns that the pattern worked once and reuses it because it is safe, coherent, and easy to continue.

## Why Readers Notice

The story feels mechanically fair but predictable. The reader can guess the next chapter before it begins.

## Detection Signals

- same chapter skeleton appears twice in a row
- only the task object changes
- same side character repeats the same reaction function
- same ending confirms the protagonist's small gain
- no external event changes the larger situation

## Required Fix

Break the skeleton through one of:

```text
external notice
public check
relationship choice
method failure
opponent adapts
side character acts first
resource conflict
old gain becomes new cost
```

## Regression Test

Write a one-line skeleton for the last three chapters. If two or more skeletons match, mark REVISE.

## Related Governance Files

- `governance/longform_ai_inertia_check.md`
- `governance/beat_review.md`
- `governance/reward_engine.md`
- `prompts/04_review_hook.md`
