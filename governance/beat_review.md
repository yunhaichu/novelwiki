# Beat Review Gate

Use this after generating or revising a chapter beat table and before creating chapter briefs.

## Decision

Return one of:

- PASS
- REVISE
- FAIL

## Required Checks

### 1. Volume Alignment

Each beat must serve the approved volume goal.

Mark REVISE if chapters drift into local events without changing the volume state.

### 2. State Change

Each chapter must change at least one of:

- protagonist status
- resource access
- relationship state
- information state
- risk level
- method or strategy
- belief or self-understanding

Mark REVISE if any chapter is only routine movement.

### 3. Engine Variety

No three adjacent beats may use the same main engine.

Mark REVISE if the table repeats:

```text
assignment -> cost -> payoff
```

or:

```text
morning -> task -> evening validation
```

### 4. Reader Reward

Each beat must identify a reader reward or a deliberately planned short-term loss.

Mark REVISE if the beat only adds pressure.

### 5. Main-System Progress

Each beat must connect to the main genre promise.

Examples:

```text
cultivation: resource, power, rule, sect survival
urban: money, reputation, relationship, career pressure
mystery: clue, contradiction, suspect relation, proof chain
romance: relationship movement, emotional risk, choice
```

Mark REVISE if the beat advances only local logistics.

### 6. Relationship Motion

At least one core relationship must change every 2-3 chapters.

Mark REVISE if side characters remain fixed functions.

### 7. Information Timing

The beat table must distribute information across immediate, midterm, and long-term suspense.

Mark REVISE if all truth is delayed or all truth is explained too early.

### 8. Hook Chain

Each chapter hook must create a reason to read the next chapter.

Mark REVISE if hooks are only mood lines, polished summaries, or vague mysteries.

## Output Format

```text
Decision: PASS / REVISE / FAIL

Main reason:

Checks:
- Volume alignment:
- State change:
- Engine variety:
- Reader reward:
- Main-system progress:
- Relationship motion:
- Information timing:
- Hook chain:

Required fixes if REVISE:
1.
2.
3.
```
