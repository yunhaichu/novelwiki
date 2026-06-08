# Volume State Plan Prompt

Use this prompt after the novel spine is approved and before chapter pressure cards.

The purpose is to define the state movement of one volume without locking specific chapter events.

## Core Principle

A volume plan should describe how the story state changes.

It should not prescribe exact scenes or solutions.

The volume is a medium-strength boundary: stronger than a scene prompt, weaker than a plot outline.

## Inputs

Read:

- novel spine
- current wiki project file if present
- current character and world state if continuing an existing novel
- previous volume state if any
- known user constraints

## Output Object

Produce:

```text
Volume number:
Volume role in whole novel:
Start state:
End state:
Main pressure of this volume:
Primary state change:
Secondary state changes:
Key forces in conflict:
Resources available at start:
Resources that may emerge:
Relationships likely to change:
Known boundaries:
Forbidden shortcuts:
Open questions for emergence:
```

## Field Guidance

### Start state / End state

Use state language.

Good:

```text
The protagonist is a disposable patrol demon with no leverage.
```

Bad:

```text
Chapter 1 patrols west road, chapter 2 finds footprints, chapter 3 hides in cave.
```

### Primary state change

Name the change this volume must accomplish.

Example:

```text
disposable -> minimally useful
```

### Key forces in conflict

List forces, not scripted events.

### Resources that may emerge

These are possibilities, not requirements.

Examples:

- a minor office rule
- a weak alliance
- a local map
- a repeated route
- a debt
- a token
- a witness

### Open questions for emergence

Questions that later scene simulation may answer.

Do not pre-answer all of them.

## Rules

- Do not write chapter-by-chapter plot.
- Do not decide how the protagonist succeeds.
- Do not assign fixed twists.
- Do not define exact scene endings.
- Keep the volume pointed toward the novel spine.
- Leave room for multi-agent scene simulation.

## Output

Output only the volume state plan.
