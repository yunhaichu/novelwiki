# Current Execution Flow

This is the short operational checklist for the current novel-generation workflow.

Use this file only to choose the execution path, identify interactive checkpoints, and check stop conditions.

Detailed layer logic belongs in `docs/workflow_layers.md`.
File responsibilities belong in `docs/file_roles.md`.
The interactive approval protocol belongs in `docs/interactive_writing_flow.md`.

## Operating Mode

The default mode is now interactive.

Do not produce a full formal chapter in one uninterrupted pass unless the user explicitly asks for batch mode.

The normal chapter loop is:

```text
read canon wiki
-> propose chapter / scene intent
-> wait for user approval or correction
-> design approved scene beat
-> wait for user approval or correction
-> draft only the approved unit
-> perform local self-check only
-> user approves / revises / rejects
-> sync only approved canon
```

The old heavy review layer is no longer the default. Most structural review must happen before drafting through interactive checkpoints. After drafting, use only the smallest review needed to catch contradictions, prose failure, or wiki-sync risk.

## Choose Flow

### Standard Long-Form Flow

Use for ordinary long-form projects: xianxia, urban fantasy, cyberpunk, single-world fantasy, standard rebirth, or other non-cosmic stories.

```text
Run Layer 1B New Novel Setup, including Project Viability Gate
-> Run Layer 2 Actor Setup
-> Run Layer 3 Volume / Arc Planning
-> Run Layer 4 Chapter Trend + Hook/Payoff Convergence
-> Interactive Approval Gate A: chapter intent
-> Run Layer 5 Reader Entry / Opening Control when needed
-> Run Layer 6 Scene Design
-> Interactive Approval Gate B: scene plan
-> Run Layer 7 Drafting in approved units
-> Local Self-Check / Targeted Review only when triggered
-> User Canon Approval
-> Run Layer 9 Wiki Sync
```

### Macro Modern-To-Cosmic Flow

Use when the target story has modern Earth, cosmic civilizations, multiverse stages, cultivation + technology + magic, or civilization war.

```text
Run Layer 1A Macro Modern-To-Cosmic Setup
-> Run Layer 1B New Novel Setup, including Project Viability Gate
-> Run Layer 2 Actor Setup
-> Run Layer 3 Volume / Arc Planning
-> Run Layer 4 Chapter Trend + Hook/Payoff Convergence
-> Interactive Approval Gate A: chapter intent
-> Run Layer 5 Modern-To-Cosmic Opening / Reader Entry
-> Run Layer 6 Scene Design
-> Interactive Approval Gate B: scene plan
-> Run Layer 7 Drafting in approved units
-> Local Self-Check / Targeted Review only when triggered
-> User Canon Approval
-> Run Layer 9 Wiki Sync
```

## Interactive Approval Gates

### Gate A: Chapter Intent

Before scene design, present only:

```text
- chapter role in current volume / arc
- current pressure
- reader hook / payoff
- protagonist usable gain or state movement
- forbidden escalations
- candidate scenes
- open decision points for user choice
```

Do not write prose at Gate A.

### Gate B: Scene Plan

Before prose, present only:

```text
- scene objective
- active actors and cognition limits
- location / object anchors
- beat list
- dialogue intent if needed
- expected payoff
- canon facts that may be updated after approval
```

Do not write prose at Gate B.

### Gate C: Draft Unit Approval

Draft only the approved unit: one scene, one subscene, or one clearly bounded chapter segment.

After each unit, provide:

```text
- what changed in canon if approved
- unresolved reader debt
- next decision point
```

Do not continue into the next unit without user approval unless the user explicitly switches to batch mode.

## Fast Trial Mode

Use this before committing to a full new-novel wiki when testing whether a concept has reader desire.

Fast Trial output is not canon.

It may produce only:

```text
non-canon opening sketch
non-canon chapter-one outline
non-canon desire test draft
```

It must not be treated as an approved chapter draft.
It must not create chapter state.
It must not plan chapter two.

For macro modern-to-cosmic trial chapters, run only:

```text
Cosmic Civilization Arena
-> Earth Civilization Value
-> Unified Power Logic
-> Modern Chinese Entry Bridge
-> Reader Hook And Payoff Ladder
-> Modern-To-Cosmic Opening
-> Interactive Trial Approval
```

If the non-canon opening sketch has no desire to continue, do not build the full wiki yet.

Formal drafting still requires Layer 1B, Project Viability Gate pass, and Wiki Bootstrap.

## Core Essence To Preserve

Never remove these principles:

```text
large arena first
modern reader entry when applicable
project viability before formal wiki
reader hook/payoff every important chapter
irreversible trend, not random event
local character choice, not author puppetry
limited cognition, not omniscient actors
Name & Term Gate before new terms
wiki state before next chapter
user approval before canon expansion
xiaobai readable prose
```

## Standard Stop Conditions

Stop if any are true:

1. Project Viability Gate has not passed before formal wiki bootstrap.
2. Irreversible trend anchor is missing.
3. Name & Term Gate is missing for new names or invented terms.
4. Wiki bootstrap is missing before formal drafting.
5. Chapter intent has not passed Gate A.
6. Scene plan has not passed Gate B for an important scene.
7. Chapter begins from a random event instead of trend convergence.
8. Important chapter has no reader hook/payoff.
9. Local choices do not pull toward a shared trend node.
10. Prose uses invented shorthand where ordinary description is clearer.
11. Draft uses summary voice instead of action/dialogue.
12. Main scene has no convergence point.
13. Active actors know things outside their position, evidence, or private knowledge boundary.
14. Protagonist only suffers and gains no usable final-form asset.
15. Chapter ends on abstract realization instead of concrete consequence.
16. Next chapter would rely on chat memory instead of wiki state.
17. A draft unit changes canon without explicit user approval.

## Macro Story Stop Conditions

For macro modern-to-cosmic stories, also stop if any are true:

1. Cosmic civilization arena is missing.
2. Earth is only a hometown and has no civilization value.
3. Multiple power systems lack unified power logic.
4. Modern protagonist loses modern identity after entry.
5. Macro setup gets narrowed back into a small sect / city / island story without reason.
6. Chapter one explains the whole universe instead of showing one small crack.
7. Chapter one ignores first-contact psychological realism.
8. No concrete question, crisis, choice, relationship tension, world reveal, mechanism reveal, or earned visible gain makes the reader continue.
9. Earth status progress is not tracked after relevant formal chapters.

## Canon Rule

```text
User-approved draft unit -> local self-check -> user canon approval -> wiki sync -> next unit / next chapter
```
