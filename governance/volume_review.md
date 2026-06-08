# Volume Review Gate

Use this after creating or revising a volume plan and before generating chapter beats.

## Decision

Return one of:

- PASS
- REVISE
- FAIL

## Required Checks

### 1. Whole-Story Alignment

The volume must serve the approved project outline.

Mark REVISE if the volume introduces a new story direction that is not grounded in the project outline.

### 2. Type Contract Alignment

If a type contract exists, the volume must serve the declared primary reader promise.

Mark REVISE if the volume mainly pays a side promise while the primary promise remains delayed, hidden, or unclear.

### 3. Volume Start / End Change

The volume must clearly state how the protagonist's status, resource, relationship, knowledge, method, or risk changes from start to end.

Mark REVISE if the volume is only a setting tour or a sequence of tasks.

### 4. Opening Reader Entry

For volume 1 or any new major arc, the volume must define what chapters 1-3 make clear and what they delay.

Mark REVISE if the opening group requires wiki knowledge before the reader can identify:

```text
protagonist
immediate trouble
present desire
stake
primary promise
reason to continue
```

### 5. Main Genre Promise

The volume must pay the genre's main promise.

Examples:

```text
cultivation/progression: power/resource/rule/survival
urban/workplace: money/status/reputation/relationship/career pressure
science fiction: anomaly proof/rule discovery/human cost
mystery: clue/contradiction/suspect relation/proof chain
romance: relationship movement/emotional risk/choice
thriller: threat escalation/narrowed options/survival move
```

Mark REVISE if the volume's gains do not connect to the declared story engine.

### 6. Reader Reward

The volume must define what reader desire it activates and what it pays back.

Mark REVISE if it only adds suffering, pressure, or worldbuilding.

### 7. Relationship Change

At least one core relationship must change during the volume.

Mark REVISE if side characters only explain, mock, praise, or accompany the protagonist.

### 8. Midpoint Turn

The volume midpoint must change one of:

- protagonist plan
- known opponent
- rule understanding
- resource state
- relationship map
- suspense meaning
- primary method

Mark REVISE if the midpoint is only another event.

### 9. Consequence Chain

The volume must identify opening consequence, midpoint consequence, climax consequence, and next pressure.

Mark REVISE if the volume is only a list of episodes rather than a consequence chain.

### 10. Conflict Escalation

The volume must show how conflict escalates from start to midpoint to climax.

Mark REVISE if the protagonist's method keeps working cleanly without higher cost, stronger opposition, reduced retreat, relationship risk, public risk, or resource pressure.

### 11. Climax and Consequence

The volume climax must close a local problem and create a new consequence.

Mark REVISE if the climax only repeats earlier payoff or solves a problem cleanly without cost.

### 12. Drift Prevention

The volume must name at least two likely drifts and how to prevent them.

Mark REVISE if no drift controls are included.

## Output Format

```text
Decision: PASS / REVISE / FAIL

Main reason:

Checks:
- Whole-story alignment:
- Type contract alignment:
- Start/end change:
- Opening reader entry:
- Main genre promise:
- Reader reward:
- Relationship change:
- Midpoint turn:
- Consequence chain:
- Conflict escalation:
- Climax consequence:
- Drift prevention:

Required fixes if REVISE:
1.
2.
3.
```
