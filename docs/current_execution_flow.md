# Current Execution Flow

This is the short operational checklist for the current novel-generation workflow.

Use this file only to choose the execution path and check stop conditions.

Detailed layer logic belongs in `docs/workflow_layers.md`.
File responsibilities belong in `docs/file_roles.md`.

## Choose Flow

### Standard Long-Form Flow

Use for ordinary long-form projects: xianxia, urban fantasy, cyberpunk, single-world fantasy, standard rebirth, or other non-cosmic stories.

```text
Run Layer 1B New Novel Setup, including Project Viability Gate
-> Run Layer 2 Actor Setup
-> Run Layer 3 Volume / Arc Planning
-> Run Layer 4 Chapter Trend + Hook/Payoff Convergence
-> Run Layer 5 Reader Entry / Opening Control when needed
-> Run Layer 6 Scene Design
-> Run Layer 7 Drafting
-> Run Layer 8 Review
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
-> Run Layer 5 Modern-To-Cosmic Opening / Reader Entry
-> Run Layer 6 Scene Design
-> Run Layer 7 Drafting
-> Run Layer 8 Review
-> Run Layer 9 Wiki Sync
```

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
xiaobai readable prose
```

## Standard Stop Conditions

Stop if any are true:

1. Project Viability Gate has not passed before formal wiki bootstrap.
2. Irreversible trend anchor is missing.
3. Name & Term Gate is missing for new names or invented terms.
4. Wiki bootstrap is missing before formal drafting.
5. Chapter begins from a random event instead of trend convergence.
6. Important chapter has no reader hook/payoff.
7. Local choices do not pull toward a shared trend node.
8. Prose uses invented shorthand where ordinary description is clearer.
9. Draft uses summary voice instead of action/dialogue.
10. Main scene has no convergence point.
11. Active actors know things outside their position, evidence, or private knowledge boundary.
12. Protagonist only suffers and gains no usable final-form asset.
13. Chapter ends on abstract realization instead of concrete consequence.
14. Next chapter would rely on chat memory instead of wiki state.

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
Approved chapter -> wiki sync -> next chapter.
```
