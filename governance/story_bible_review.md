# Story Bible Review Gate

Use this after creating or updating a story bible.

The story bible is canon-facing. It controls continuity, character state, time, rules, clues, and open questions.

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

- current goal
- hidden pressure or need
- knowledge state
- current relationship state
- ability or limit if relevant

Mark REVISE if characters only have static labels.

### 3. Timeline State

Major events must have enough time/order information to prevent contradictions.

At minimum, the bible should track:

- event order
- cause
- result
- involved characters
- who knows what

Mark REVISE if sequence and information flow are unclear.

### 4. Rule State

World, profession, system, or genre rules must include:

- what the rule allows
- what it forbids
- cost or limit
- first shown location

Mark REVISE if a rule is only a decorative setting idea.

### 5. Foreshadow State

Foreshadowing must have:

- surface meaning
- real meaning or unknown status
- target payoff window
- current status

Mark REVISE if planted details have no planned treatment.

### 6. Object / Clue / Resource State

Important objects, clues, resources, injuries, money, status tokens, documents, or secrets must have current status and holder or location.

Mark REVISE if an object can disappear or reappear without being tracked.

### 7. Open Questions

Open questions must state:

- question
- scope
- target answer window
- risk if ignored

Mark REVISE if mysteries accumulate without payoff control.

## Output Format

```text
Decision: PASS / REVISE / FAIL

Main reason:

Checks:
- Canon scope:
- Character state:
- Timeline state:
- Rule state:
- Foreshadow state:
- Object/resource state:
- Open questions:

Required fixes if REVISE:
1.
2.
3.
```
