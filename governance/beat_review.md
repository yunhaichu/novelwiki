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

### 2. Type Contract Alignment

Each beat must visibly serve the declared primary genre promise if a type contract exists.

Mark REVISE if beats mainly pay a secondary promise while the primary promise remains invisible.

### 3. State Change

Each chapter must change at least one of:

- protagonist status
- resource access
- relationship state
- information state
- risk level
- method or strategy
- belief or self-understanding

Mark REVISE if any chapter is only routine movement.

### 4. Engine Variety

No three adjacent beats may use the same main engine.

Mark REVISE if the table repeats:

```text
assignment -> cost -> payoff
```

or:

```text
morning -> task -> evening validation
```

### 5. Reader Reward

Each beat must identify a reader reward or a deliberately planned short-term loss.

Mark REVISE if the beat only adds pressure.

### 6. Primary Genre Promise Progress

Each beat must connect to the primary genre promise.

Examples:

```text
cultivation/progression: resource, power, rule, sect survival
urban/workplace: money, reputation, relationship, career pressure
mystery: clue, contradiction, suspect relation, proof chain
science fiction: anomaly proof, technical limit, rule discovery, human cost
romance: relationship movement, emotional risk, choice
farming/management: resource chain, production, land, market, community defense
officialdom/political: position, procedure, alliance, policy risk, reputation
```

Mark REVISE if the beat advances only local logistics.

### 7. Consequence Chain

Each beat must identify:

- immediate consequence;
- who reacts;
- what becomes harder;
- what path closes;
- what new path opens;
- what must happen next because of this chapter.

Mark REVISE if a beat can be removed without affecting later events, or if its events can be freely reordered without changing causality.

### 8. Conflict Escalation

Each beat must identify whether the conflict escalates and how.

Escalation may occur through:

- stronger obstacle;
- higher cost;
- reduced retreat path;
- opponent or system adaptation;
- protagonist method failure;
- relationship, reputation, resource, time, physical, moral, or knowledge pressure.

Mark REVISE if beats add information without escalation across multiple chapters, or if the protagonist's method keeps working cleanly without cost.

Controlled non-escalation is allowed only for planned aftermath, recovery, relationship repair, or breather pacing, and must still change information, method, relationship, or future pressure.

### 9. Relationship Motion

At least one core relationship must change every 2-3 chapters.

Mark REVISE if side characters remain fixed functions.

### 10. Information Timing

The beat table must distribute information across immediate, midterm, and long-term suspense.

Mark REVISE if all truth is delayed or all truth is explained too early.

### 11. Hook Chain

Each chapter hook must create a reason to read the next chapter.

Mark REVISE if hooks are only mood lines, polished summaries, or vague mysteries.

## Output Format

```text
Decision: PASS / REVISE / FAIL

Main reason:

Checks:
- Volume alignment:
- Type contract alignment:
- State change:
- Engine variety:
- Reader reward:
- Primary genre promise progress:
- Consequence chain:
- Conflict escalation:
- Relationship motion:
- Information timing:
- Hook chain:

Required fixes if REVISE:
1.
2.
3.
```
