# Beat Generator Prompt

Use this prompt after a volume plan passes `governance/volume_review.md` and before chapter briefs.

The goal is to turn a volume plan into a near-term chapter beat table. It is not prose.

## Required Inputs

Read:

- approved type contract if present
- approved project outline
- approved volume plan
- outline review result
- volume review result
- genre / story engine
- primary genre promise
- core relationship matrix
- three-layer suspense
- current story bible if present
- forbidden drift list
- `governance/consequence_chain_check.md`
- `governance/conflict_escalation_check.md`

## Output Object

Produce a chapter beat table for 10 chapters or another approved range.

For each chapter, fill in:

```text
Chapter number:
Beat role:
Main engine:
Opening pressure:
Protagonist goal:
Protagonist action:
Opposition / obstacle:
State change:
Relationship change:
Information change:
Resource / status change:
Reader reward:
Primary genre promise progress:
Cost or consequence:
Consequence chain:
- immediate consequence:
- who reacts:
- what becomes harder:
- what path closes:
- what new path opens:
- what must happen next because of this chapter:
Conflict escalation:
- conflict before:
- conflict after:
- escalation type:
- higher cost / stronger obstacle / reduced retreat:
Chapter hook:
What must not happen:
```

## Beat Rules

- A chapter beat is not a plot summary.
- Each beat must create a change in at least one of these:
  - status
  - resource
  - relationship
  - information
  - risk
  - method
  - belief
- No three adjacent chapters may use the same main engine.
- No chapter may exist only to move characters through routine.
- Each beat must serve the approved volume goal.
- Each beat must connect to the primary genre promise from the type contract if present.
- At least one relationship line must change every 2-3 chapters.
- At least one earlier detail should change meaning every 3 chapters.
- Each beat must state what consequence forces or strongly motivates a next action.
- Each beat must state whether and how conflict escalates.

## Consequence Rule

Do not build beats as `event -> event -> event`.

Use:

```text
pressure -> protagonist action -> consequence -> reaction -> narrowed or changed next step
```

Mark risk if a chapter can be removed without collapsing a later event.

## Escalation Rule

Conflict should usually grow by:

```text
stronger obstacle
higher cost
reduced retreat path
opponent/system adaptation
method failure or increased cost
relationship/reputation/resource/time/moral pressure
```

Controlled non-escalation is allowed only for planned aftermath, recovery, relationship repair, or breather pacing. Even then, the chapter must change information, method, relationship, or future pressure.

## Anti-Log Rule

Do not build the beat table from calendar order alone.

Bad pattern:

```text
Day 1 work
Day 2 work
Day 3 work
Evening lesson
After-lesson talk
```

Use event engines instead:

```text
external notice
resource conflict
relationship choice
failed imitation
rule consequence
first check
public reaction
hidden cost
opponent adaptation
method failure
```

## Output

Output only the beat table and a short risk note.
