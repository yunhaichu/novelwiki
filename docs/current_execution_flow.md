# Current Execution Flow

This is the short operational checklist for the current human-AI collaborative novel workflow.

Use this file to choose the execution path, identify required wiki retrieval, and check stop conditions.

Detailed story-memory concepts belong in `docs/narrative_model.md`.
Detailed layer logic belongs in `docs/workflow_layers.md`.
File responsibilities belong in `docs/file_roles.md`.
The interaction protocol belongs in `docs/interactive_writing_flow.md`.

## Operating Mode

The default mode is collaborative and wiki-centered.

Do not treat NovelWiki as a one-way batch generation pipeline. Do not produce a full formal chapter in one uninterrupted pass unless the user explicitly asks for batch mode.

The normal loop is:

```text
retrieve relevant wiki records
-> discuss the creative issue with the user
-> propose options and expose conflicts
-> user decides or redirects
-> record approved decisions / mutations
-> generate the requested bounded output when needed
-> run consistency check
-> user canon approval
-> sync approved canon into the wiki
```

Heavy review is not the default. Most structural problems should be handled during discussion and consistency checking before canon mutation or generation.

## Choose Flow

### Standard Long-Form Flow

Use for ordinary long-form projects.

```text
Run New Novel Setup
-> Run Wiki Bootstrap
-> Retrieve relevant Entity / Event / State / Relationship records
-> Discuss arc, chapter, scene, or object design with the user
-> Record approved decisions as Session / Mutation records when needed
-> Generate only the approved unit when needed
-> Run Consistency Check
-> User Canon Approval
-> Run Wiki Sync
```

### Extended Arena Flow

Use when the target story requires broad arenas, multiple rule systems, large social structures, long historical pressure, or multi-stage escalation.

```text
Run Extended Arena Setup
-> Run New Novel Setup
-> Run Wiki Bootstrap
-> Retrieve relevant Entity / Event / State / Relationship records
-> Discuss pressure, rule systems, actors, consequences, and time-aware states with the user
-> Record approved decisions as Session / Mutation records when needed
-> Generate only the approved unit when needed
-> Run Consistency Check
-> User Canon Approval
-> Run Wiki Sync
```

### Fast Trial Mode

Use this before committing to a full new-novel wiki when testing whether a concept has reader desire.

Fast Trial output is not canon.

It may produce only:

```text
non-canon concept sketch
non-canon opening sketch
non-canon scene sketch
non-canon desire test draft
```

It must not be treated as an approved chapter draft.
It must not create canonical story facts.
It must not create canon-dependent later planning.

If the non-canon test has no desire to continue, do not build the full wiki yet.

Formal drafting still requires wiki bootstrap and user-approved canon decisions.

## Required Collaboration Steps

### Step 1: Retrieve Wiki Records

Before any canon-dependent discussion or generation, retrieve relevant records:

```text
- involved entities
- current states at the relevant timepoint
- recent or causal events
- important relationships
- applicable rule systems
- approved names and terms
- relevant prior sessions and mutations
```

Do not rely on chat memory for durable facts.

### Step 2: Discuss

The assistant may discuss characters, organizations, locations, rule systems, time-aware states, relationships, events, scene direction, dialogue direction, plot consequence, naming, or prose rendering.

The assistant should show only the relevant retrieved constraints and then offer options or identify the unresolved decision.

### Step 3: Decide

The user decides.

The assistant must not treat its own proposal as canon. The user may accept, reject, combine, redirect, or request another proposal.

### Step 4: Record Approved Change

When the user approves a durable change, record it in the smallest sufficient place:

```text
Entity
Event
Timepoint
State
Relationship
Session
Mutation
name registry
style record
chapter state
other project-specific wiki file
```

### Step 5: Generate When Needed

Generate prose or design output only when the user asks for a concrete output.

The output must stay inside the approved scope.

### Step 6: Consistency Check

Before canon mutation or canon-dependent generation, check:

```text
- no contradiction with retrieved wiki records
- no unapproved names or terms
- no entity acting outside its time-aware state
- no actor omniscience
- no unsupported rule-system change
- important consequences are recorded as Event or State movement
- no durable fact exists only in chat memory
```

### Step 7: Canon Approval And Sync

```text
user-approved canon -> consistency check -> wiki sync -> next canon-dependent step
```

## Core Essence To Preserve

Never remove these principles:

```text
wiki state before canon-dependent discussion
user decision before canon mutation
time-aware states for durable changes
facts recorded as events when they matter later
local character choice, not author puppetry
limited cognition, not omniscient actors
Name & Term Gate before recurring invented terms
reader hook/payoff for important generated units
clear prose through action, dialogue, reaction, process, and consequence
```

## Standard Stop Conditions

Stop if any are true:

1. Fast Trial is being mistaken for canon.
2. Genre mode is unclear.
3. Genre operating model is missing or too vague.
4. Name & Term Gate is missing for recurring names or invented terms.
5. Wiki bootstrap is missing before formal canon-dependent work.
6. Relevant wiki records have not been retrieved.
7. A proposed change affects existing canon but no consistency check has been made.
8. A discussion point is being treated as canon before user approval.
9. A draft changes canon without explicit user approval.
10. The next step would rely on chat memory instead of wiki state.
11. Time-aware state is needed but the relevant timepoint or state record is missing.
12. A major entity acts outside its current state, knowledge, authority, motivation, or ability.
13. A generated unit uses summary voice instead of action, dialogue, reaction, process, and consequence.
14. A generated unit replaces story action with interface, report, log, archive, status, or abstract explanation.
15. A generated unit has no clear consequence, hook, or next decision point when the unit requires one.

## Extended Arena Stop Conditions

For stories with large arenas, multiple rule systems, or broad escalation, also stop if any are true:

1. The largest story arena is missing.
2. The active rule systems lack shared operating logic or clear boundaries.
3. Major organizations or social structures act without incentives, costs, or authority boundaries.
4. The opening or current unit explains the whole world instead of presenting one concrete pressure point.
5. A major change lacks affected entities, state changes, or event consequences.
6. The story narrows into a smaller arena without user-approved reason.

## Canon Rule

```text
User-approved decision or generated unit -> consistency check -> wiki sync -> next canon-dependent discussion / design / generation
```