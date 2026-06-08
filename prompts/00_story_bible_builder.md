# Story Bible Builder Prompt

Use this prompt after the project outline and volume plan are approved.

The goal is to build a reusable story bible for any novel instance.

## Required Inputs

Read:

- approved type contract if present
- approved project outline
- approved volume plan
- approved beat plan if available
- genre / story engine
- primary genre promise
- core relationship matrix
- three-layer suspense
- glossary / approved term list
- existing character files if any
- existing world or rules files if any
- `prompts/00_character_action_logic.md` if available

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
```

When available, extend recurring character entries with:

```text
  external desire:
  core fear:
  flaw trigger:
  default protection priority:
  information threshold:
  conflict mode:
  stress action:
  what this character will not say directly:
```

Continue the story bible with:

```text
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

## Character Action Logic Extension

For recurring characters, include action logic when it is known from approved outline, beats, prose, or character files.

If unknown, write `unknown`. Do not guess.

Action logic should help future chapters answer:

```text
what the character wants now
what pressure changes their decisions
what fear or flaw gets triggered
what they protect first under stress
how they handle conflict
what they will not say directly
```

## Rules

- Do not invent facts not supported by approved outline, beats, or existing canon.
- If a field is unknown, write `unknown`, not a guess.
- Every rule must include a limit or cost.
- Every character must have a current knowledge state.
- Recurring characters should have action logic, not only static labels.
- Every foreshadow must have a target payoff or a reason to remain open.
- The bible is canon-facing. Do not include draft-only speculation unless clearly marked as non-canon.
- The story bible may know more than the reader. Do not expose all bible information in opening chapters.

## Output

Output only the story bible update.
