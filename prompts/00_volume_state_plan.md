# Volume State Plan Prompt

Use this prompt after the novel spine is approved and before chapter pressure cards.

The purpose is to define the state movement and rhythm of one volume without locking specific chapter events.

## Core Principle

A volume plan should describe how the story state changes.

It should not prescribe exact scenes or solutions.

The volume is a medium-strength boundary: stronger than a scene prompt, weaker than a plot outline.

## Control-Based Volume Principle

If the novel spine uses a control-based protagonist engine, the volume should not measure progress only by strength, rank, or suffering endured.

Track how the protagonist's control changes.

Examples of control progress:

- understands one local rule;
- gains one small piece of leverage;
- influences one person;
- makes an opponent misread them;
- turns a hostile action into useful information;
- learns when not to act;
- acts directly when waiting would lose the key condition.

Pressure should make the protagonist more alert, better positioned, or more dangerous in a specific way. It should not become repeated passive abuse.

## Cross-Chapter Rhythm Principle

A volume must manage rhythm across chapters, not only chapter-by-chapter logic.

Do not let the story become:

- continuous mystery with no payoff;
- continuous pressure with no breathing space;
- continuous breathing space with no escalation;
- repeated same-hook chapters;
- repeated protagonist suffering without leverage;
- repeated face-slapping without larger state movement.

Use state movement, not mechanical beat-counting, as the main rhythm measure.

## Inputs

Read:

- novel spine;
- current wiki project file if present;
- irreversible trend anchor;
- protagonist growth track;
- Reader Hook / Payoff Ladder;
- previous chapter states if continuing an existing novel;
- current character and world state if continuing an existing novel;
- previous volume state if any;
- known user constraints.

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
Control state at start:
Control state at end:
New leverage that may emerge:
New rule or pattern the protagonist may learn:
Relationship influence likely to change:
Opponent misread or system misread likely to emerge:
Force moment if any:
Main risk of power inflation:
Main risk of passive suffering:
Key forces in conflict:
Resources available at start:
Resources that may emerge:
Relationships likely to change:
Known boundaries:
Forbidden shortcuts:
Open questions for emergence:
Rhythm plan:
Reader debt limits:
Breather chapter rule:
Mini-turn schedule:
Stage-turn schedule:
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

### Control state at start / end

Name what the protagonist can and cannot influence.

Example:

```text
Start: can only react and hide.
End: can influence one low-ranking ally and one local rule.
```

### New leverage that may emerge

Leverage should be specific but not predetermined.

Examples:

- someone owes the protagonist;
- a route pattern;
- a repeated office rule;
- a token;
- a witness;
- a small reputation;
- a known fear;
- a documented inconsistency.

### Rhythm plan

Define rhythm by required state movement, not exact events.

Include:

```text
Every 1-3 chapters: at least one concrete state movement.
Every 3 chapters: at least one mini-turn, small payoff, relationship shift, resource change, or new forced choice.
Every 8-12 chapters: one stage-turn, goal payoff/failure, status shift, arena expansion, or irreversible loss.
No 2 consecutive important chapters may only add mystery without payoff.
No 3 consecutive chapters may leave protagonist state unchanged.
No repeated hook type may appear 3 times without structural upgrade.
```

Adjust numbers by genre and chapter length, but explain why.

### Reader debt limits

Define how long key debts may remain unpaid.

Output:

```text
Debt:
Expected payoff type:
Maximum delay:
What happens if delayed too long:
```

### Breather chapter rule

A breather chapter is allowed, but it must still change state.

Allowed breather functions:

- relationship reset;
- emotional processing;
- aftermath cost;
- information organization;
- preparation;
- route change;
- quiet world reveal;
- low-stakes choice.

A breather chapter must not be filler.

### Mini-turn schedule

Do not script chapter events. Define possible mini-turn types:

- new leverage appears;
- old assumption fails;
- relationship changes;
- small question gets answered;
- new choice becomes forced;
- object/resource changes hands;
- organization notices protagonist;
- pressure clock advances.

### Stage-turn schedule

Define possible stage-turn types:

- stage goal succeeds;
- stage goal fails but reveals larger route;
- protagonist earns or loses status;
- arena expands;
- major actor changes behavior;
- Earth / civilization status changes if relevant;
- irreversible loss occurs;
- final-form asset upgrades.

### Force moment if any

A volume may include direct action.

Do not force it, but if the volume needs a direct action moment, define what kind of situation would justify it.

Example:

```text
If hesitation would cause immediate loss of the key condition, the protagonist should act directly.
```

### Key forces in conflict

List forces, not scripted events.

### Resources that may emerge

These are possibilities, not requirements.

Examples:

- a minor office rule;
- a weak alliance;
- a local map;
- a repeated route;
- a debt;
- a token;
- a witness.

### Open questions for emergence

Questions that later scene simulation may answer.

Do not pre-answer all of them.

## Rules

- Do not write chapter-by-chapter plot.
- Do not decide how the protagonist succeeds.
- Do not assign fixed twists.
- Do not define exact scene endings.
- Keep the volume pointed toward the novel spine.
- Track control growth as state change, not as guaranteed victories.
- Track reader debt and payoff timing.
- Avoid using repeated suffering as the main measure of progress.
- Avoid using pure strength growth as the only measure of progress.
- Avoid consecutive chapters that only add mysteries.
- Leave room for multi-agent scene simulation.

## Output


Output two artifacts:

1. The volume state plan (as defined above).
2. A volume rhythm tracker at `novels/<novel_id>/wiki/volume_<number>_rhythm_tracker.md` initialized with the chapter log table, breathing chapter budget, and hard checks. Populate row 001 and 002 if the volume has started.
