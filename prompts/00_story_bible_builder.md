# Story Bible Builder Prompt

Use this prompt after the project outline and volume plan are approved.

The goal is to build a reusable story bible for any novel instance.

## Required Inputs

Read:

- approved project outline
- approved volume plan
- approved beat plan if available
- genre / story engine
- core relationship matrix
- three-layer suspense
- glossary / approved term list
- existing character files if any
- existing world or rules files if any

## Output Object

Produce or update a story bible with these sections:

```text
Project ID:
Canon version:
Main genre promise:
Core conflict:
Current volume goal:

Confirmed facts:
- fact_id:
  statement:
  source:
  first_confirmed_in:
  status:

World / system rules:
- rule_id:
  rule:
  limit:
  cost:
  first_shown_in:
  exceptions_allowed:

Character master list:
- character_id:
  name:
  public identity:
  hidden pressure:
  external goal:
  inner need:
  flaw / decision bias:
  current state:
  knowledge state:

Relationship map:
- relation_id:
  characters:
  surface relation:
  hidden tension:
  current state:
  expected change:

Timeline anchors:
- event_id:
  chapter / scene:
  time marker:
  location:
  cause:
  result:
  known by:

Foreshadow register:
- foreshadow_id:
  planted in:
  surface meaning:
  real meaning:
  target payoff:
  status:

Objects / clues / resources:
- object_id:
  name:
  current holder:
  status:
  rule relevance:
  first_seen_in:

Open questions:
- question_id:
  question:
  scope:
  target answer window:
  risk if ignored:
```

## Rules

- Do not invent facts not supported by approved outline, beats, or existing canon.
- If a field is unknown, write `unknown`, not a guess.
- Every rule must include a limit or cost.
- Every character must have a current knowledge state.
- Every foreshadow must have a target payoff or a reason to remain open.
- The bible is canon-facing. Do not include draft-only speculation unless clearly marked as non-canon.

## Output

Output only the story bible update.
