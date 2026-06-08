# Type Contract Review Gate

Use this after creating or revising a type contract and before project outline generation.

The type contract is the reader-facing promise of the novel. It controls how the opening, volume plan, beats, reader rewards, and ending payoff should be evaluated.

## Decision

Return one of:

```text
PASS
REVISE
FAIL
```

## Required Checks

### 1. Primary Genre Clarity

The type contract must identify one primary genre or primary story engine.

Mark `REVISE` if the contract lists several genres but does not say which promise controls the opening and ending.

### 2. Reader Promise

The type contract must define what the reader is promised emotionally or structurally.

Examples:

```text
truth payoff
survival pressure
relationship movement
power/status growth
anomaly proof
justice/revenge
wonder/exploration
fear release
```

Mark `REVISE` if the promise is only a topic, setting, occupation, or mood.

### 3. Opening Visibility

The contract must say what the opening must show on the page.

Mark `REVISE` if the opening promise requires wiki knowledge, backstory explanation, or later chapters before it becomes visible.

### 4. Chapter 1-3 Expectation

The contract must state what the reader should expect by chapter 1 and chapter 3.

Mark `REVISE` if the first three chapters do not have a concrete reader-facing delivery target.

### 5. Genre Blend Control

If the project is cross-genre, the contract must state:

- which genre is primary;
- which genre is secondary;
- how the secondary genre supports the primary promise;
- which promise controls the ending payoff.

Mark `REVISE` if the project risks attracting one type of reader while paying another type of promise.

### 6. False Promise Prevention

The contract must name forbidden false promises.

Mark `REVISE` if it could mislead readers about the kind of story they are entering.

### 7. Drift Risk

The contract must identify likely type drift.

Common drift risks:

```text
setting explanation replacing story pressure
mystery becoming vague mood
romance becoming background decoration
workplace process replacing status/reputation stakes
cultivation labor replacing power/resource/rule progress
science fiction concept replacing human cost
secondary genre overtaking primary promise
```

Mark `REVISE` if no drift risks are named.

## Output Format

```text
Decision: PASS / REVISE / FAIL

Main reason:

Checks:
- Primary genre clarity:
- Reader promise:
- Opening visibility:
- Chapter 1-3 expectation:
- Genre blend control:
- False promise prevention:
- Drift risk:

Required fixes if REVISE:
1.
2.
3.
```
