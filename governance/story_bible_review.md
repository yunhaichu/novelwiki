# Story Bible Review Gate

Use this after creating or updating a story bible.

The story bible is canon-facing. It controls continuity, character state, time, rules, clues, open questions, and recurring character action logic.

## Decision

Return one of:

- PASS
- REVISE
- FAIL

## Required Checks

### 1. Canon Scope

The story bible must separate confirmed canon from draft-only speculation.

Mark REVISE if uncertain material is written as confirmed fact.

### 2. Character State

Each recurring character must have:

- current goal or desire
- hidden pressure or need
- knowledge state
- current relationship state
- ability or limit if relevant

Mark REVISE if characters only have static labels.

### 3. Character Action Logic

Recurring characters should include action logic when known:

- what they want now
- what pressure changes their decisions
- what fear or flaw gets triggered
- what they protect first under stress
- how they handle conflict
- what they will not say directly

Mark REVISE if a recurring character has only identity, personality, and role, with no action logic or `unknown` markers.

Do not invent action logic. If unknown, write `unknown`.

### 4. Timeline State

Major events must have enough time/order information to prevent contradictions.

At minimum, the bible should track:

- event order
- cause
- result
- involved characters
- who knows what

Mark REVISE if sequence and information flow are unclear.

### 5. Rule State

World, profession, system, or genre rules must include:

- what the rule allows
- what it forbids
- cost or limit
- first shown location

Mark REVISE if a rule is only a decorative setting idea.

### 6. Foreshadow State

Foreshadowing must have:

- surface meaning
- real meaning or unknown status
- target payoff window
- current status

Mark REVISE if planted details have no planned treatment.

### 7. Object / Clue / Resource State

Important objects, clues, resources, injuries, money, status tokens, documents, or secrets must have current status and holder or location.

Mark REVISE if an object can disappear or reappear without being tracked.

### 8. Open Questions

Open questions must state:

- question
- scope
- target answer window
- risk if ignored

Mark REVISE if mysteries accumulate without payoff control.

### 9. Reader Exposure Boundary

The story bible may know more than the reader.

Mark REVISE if bible notes imply that all canon-facing knowledge should be exposed in an opening chapter.

Openings must still use reader entry gates and information-delay controls.

## Output Format

```text
Decision: PASS / REVISE / FAIL

Main reason:

Checks:
- Canon scope:
- Character state:
- Character action logic:
- Timeline state:
- Rule state:
- Foreshadow state:
- Object/resource state:
- Open questions:
- Reader exposure boundary:

Required fixes if REVISE:
1.
2.
3.
```
