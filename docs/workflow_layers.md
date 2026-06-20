# Workflow Layers

This is the authoritative full execution-order index for the NovelWiki collaboration workflow.

Use `docs/current_execution_flow.md` as the short operating card. Use `docs/narrative_model.md` for story-memory concepts. Use `docs/interactive_writing_flow.md` for the human-AI collaboration protocol. Use `docs/file_roles.md` for file responsibilities.

The default execution mode is collaborative and wiki-centered. Do not run every file for every chapter. Do not draft a full formal chapter before relevant wiki retrieval, user discussion, and user-approved scope.

## Layer 0: Safety Snapshot

Run before reorganizing prompts, deleting files, merging files, or changing workflow responsibilities.

Files:

- `docs/backups/workflow_snapshot_2026-06-09.md`

## Layer 1A: Extended Arena Setup

Run once before normal new-novel setup when the target story requires broad arenas, multiple rule systems, large social structures, long historical pressure, or multi-stage escalation.

Required files may include:

1. `prompts/00_cosmic_civilization_arena.md` when the project needs a cosmic or civilization-scale arena.
2. `prompts/00_earth_civilization_value.md` when an Earth-like or home-civilization anchor matters.
3. `prompts/00_unified_power_logic.md` when multiple rule systems coexist.
4. `prompts/00_modern_chinese_entry_bridge.md` when a modern Chinese reader bridge is part of the project premise.
5. `prompts/00_webnovel_reader_hook_payoff_ladder.md` as Reader Hook / Payoff Ladder.

Required order:

```text
largest arena
-> home / reader-entry value when relevant
-> unified rule logic when relevant
-> entry bridge when relevant
-> reader hook / payoff ladder
```

Hard rules:

```text
No defined largest arena, no large-arena story.
No unified rule logic, no multi-system rule story.
No reader-entry bridge, no reader-entry dependent story.
No hook/payoff ladder, no commercial long-form execution.
```

## Layer 1B: New Novel Setup

Run once per formal novel project before canon-dependent discussion or drafting.

Required files:

1. `prompts/00_novel_spine.md`
2. `prompts/00_genre_mode_contract.md`
3. `prompts/00_genre_operating_model.md`
4. `prompts/00_irreversible_trend_anchor.md`
5. `prompts/00_reality_causal_preflight.md` for first major premise / opening event family
6. `prompts/00_base_settings_builder.md`
7. `prompts/00_major_conflict_engine.md`
8. `prompts/00_dramatic_arena.md`
9. `prompts/00_protagonist_growth_track.md` when protagonist growth is a major project engine
10. `prompts/00_project_viability_gate.md`
11. `prompts/00_name_term_gate.md`
12. `prompts/00_wiki_bootstrap.md`

For extended-arena stories, Layer 1B must read Layer 1A outputs and must not shrink the arena without user approval.

Required order inside Layer 1B:

```text
premise / type promise
-> genre mode
-> genre operating model
-> irreversible trend anchor
-> base setting boundaries
-> major conflict / dramatic arena
-> growth track when relevant
-> Project Viability Gate
-> Name & Term Gate
-> wiki bootstrap
```

Required wiki outputs:

- `novels/<novel_id>/wiki/project.md`
- `novels/<novel_id>/wiki/base_settings.md`
- `novels/<novel_id>/wiki/style.md`
- `novels/<novel_id>/wiki/name_registry.md`
- `novels/<novel_id>/wiki/timeline.md`
- `novels/<novel_id>/wiki/relationships.md`
- `novels/<novel_id>/wiki/foreshadowing.md`
- initial entity / event / state / session directories as needed

Hard rules:

```text
No irreversible trend anchor, no formal chapter design.
No Project Viability Gate pass, no formal wiki bootstrap.
No Name & Term Gate, no recurring invented name or term enters canon.
No wiki bootstrap, no formal canon-dependent draft.
```

## Layer 1T: Fast Trial Mode

Use before committing to a full novel wiki when testing whether a concept has reader desire.

Fast Trial output is non-canon.

Allowed outputs:

- non-canon concept sketch;
- non-canon opening sketch;
- non-canon scene sketch;
- non-canon desire test draft.

Forbidden outputs:

- approved chapter draft;
- canonical event;
- canonical state;
- chapter state;
- canon-dependent later plan;
- canon wiki update.

Formal drafting still requires Layer 1B, Project Viability Gate pass, Name & Term Gate when needed, and Wiki Bootstrap.

## Layer 2: Narrative Model Setup

Run once for major recurring story objects and update only when canon changes.

Primary reference:

- `docs/narrative_model.md`

Core record types:

- Entity
- Timepoint
- State
- Relationship
- Event
- Session
- Mutation

Required for major recurring actors and organizations:

- `prompts/00_character_behavior_model.md` when the entity is a recurring character.
- `prompts/00_character_expression_card.md` when the entity is a recurring speaking character.
- `prompts/00_organization_behavior_model.md` when the entity is a recurring organization.

Required when an entity influences logic, limited knowledge, or multi-party conflict:

- `prompts/00_actor_cognition_card.md`

Governance rule for simulations and multi-actor scenes:

- `governance/agent_state_rules.md`

Hard rule:

```text
No omniscient actors.
Entities act from their time-aware state, local knowledge, available resources, social position, motive, fear, misunderstanding, and physical ability.
```

## Layer 3: Arc / Stage Planning

Run once per volume, arc, or large stage. For later units, read the current wiki state and update only when the attractor, pressure map, rhythm budget, or state trajectory has changed.

Files:

- `prompts/00_volume_state_plan.md`
- `prompts/00_chapter_pressure_card.md` when chapter pressure needs isolation
- `prompts/00_webnovel_reader_hook_payoff_ladder.md` as Reader Hook / Payoff Ladder when a new stage starts or the story loses continuation desire

Outputs:

- current large trend stage;
- active protagonist or central-actor growth stage when relevant;
- arc attractor;
- organization / entity pressure map;
- reader continuation promise;
- hook / payoff ladder;
- constraints on what must not escalate yet;
- timepoints or state records that need to exist before later discussion.

## Layer 4: Discussion Preparation

Run before designing any important scene, chapter, event, or durable wiki mutation.

Required actions:

1. Retrieve relevant Entity, Timepoint, State, Relationship, Event, Session, and Mutation records.
2. Identify the current creative problem.
3. Identify constraints from the retrieved records.
4. Identify user decision points.
5. Prepare options when the direction is not already determined.

Useful files:

- `prompts/00_irreversible_trend_anchor.md`
- `prompts/00_reality_causal_preflight.md`
- `prompts/02_emergent_chapter_design.md`
- `prompts/00_webnovel_reader_hook_payoff_ladder.md` when the unit is important or the previous unit feels flat

Outputs:

- relevant retrieved facts;
- current pressure;
- affected entities;
- relevant timepoint and states;
- possible event or state changes;
- reader hook / payoff when needed;
- open user decision points;
- conflicts or uncertainty.

Interactive rule:

After Layer 4, discuss with the user. Do not design scenes or draft prose until the user approves the scope or direction.

Hard rules:

```text
No relevant wiki retrieval, no canon-dependent discussion.
No user-approved direction, no canon mutation.
No hook/payoff, no important generated unit.
```

## Layer 5: Reader Entry / Opening Control

Run for first chapters, new arcs, new worlds, new rule systems, or complex settings.

Primary file for projects that require a modern-to-large-arena opening:

- `prompts/01_modern_to_cosmic_opening.md`

Optional review aids when present:

- `prompts/00_reader_entry_gate.md`
- `prompts/02_opening_chapter_brief.md`

If optional review files are absent, do not block execution.

Opening checks:

- central viewpoint is clear;
- immediate pressure is clear;
- reader knows what can be lost now;
- unfamiliar terms are limited;
- function appears before formal name;
- the unit has a concrete continuation hook;
- large setting reveals only a small crack at first;
- first-contact psychology is believable when relevant.

## Layer 6: Scene / Event Design

Run for each important scene, event, or state-changing unit. For simple transition units, this can be shortened.

Required files for major scenes:

1. `prompts/02_scene_convergence.md`
2. `prompts/02_scene_expression_state.md`
3. `prompts/02_dialogue_intent.md` when dialogue changes state or relationship
4. `prompts/00_multi_agent_scene_simulation.md` when the scene has more than two active actors or complex hidden motives

Before multi-agent simulation, apply:

- `governance/agent_state_rules.md`

Outputs:

- scene or event objective;
- active entities;
- relevant timepoint;
- current states;
- location and object anchors;
- collision map;
- possible state changes;
- affected entities;
- consequence chain;
- performance beats;
- dialogue intent when needed.

Interactive rule:

After Layer 6, discuss the proposed scene or event design with the user. Do not draft prose until the user approves the bounded output scope.

Hard rule:

```text
No user-approved scope, no prose for that unit.
```

## Layer 7: Generation

Run only after relevant wiki retrieval, user discussion, and user-approved scope.

Files:

- `prompts/01_writer.md`
- `prompts/01_scene_log_to_draft.md` if a scene simulation/action log exists.

Rules:

- Generate only the approved unit: scene, subscene, bounded chapter segment, dialogue sequence, scene sketch, entity card, event summary, or wiki update record.
- Do not continue into the next unit without user approval unless the user explicitly switches to batch mode.
- Do not let interfaces write the story.
- Do not let narrator explanation replace character performance.
- Apply genre mode before universal workflow rules.
- Use current novel wiki as canon.
- Do not import reference settings directly into prose.
- Do not introduce unapproved names or terms; use ordinary description until the Name & Term Gate approves them.
- Do not start from a random event.
- Do not replace hook/payoff with exposition.

After each generated unit, provide a local status card:

```text
- canon changes if approved
- affected entities
- possible state changes
- unresolved reader debt when relevant
- next decision point
```

## Layer 8: Consistency Check / Targeted Review

Layer 8 is no longer a mandatory heavy review after every draft.

Consistency Check is a constraint check before canon mutation and before canon-dependent generation.

### Always Run Consistency Check

Check:

- no contradiction with retrieved wiki records;
- no unapproved names or terms;
- no entity acting outside its time-aware state;
- no actor omniscience;
- no unsupported rule-system change;
- important consequences are recorded as Event or State movement;
- no durable fact exists only in chat memory;
- generated prose uses action, dialogue, reaction, process, and consequence rather than summary-only abstraction.

### Triggered Targeted Reviews

Run specialized reviews only when their trigger appears:

- `governance/anti_ai_expression_review.md` if prose feels generic, abstract, pretty, or summary-heavy.
- `governance/emergent_plot_review.md` if important trend logic changed.
- `governance/protagonist_growth_review.md` if protagonist or central-actor state, capability, qualification, or final-form progress changed.
- `governance/character_voice_review.md` if the unit depends on dialogue, trust, fear, authority, secrecy, or first contact.
- `governance/anti_record_driven_plot.md` if records, reports, logs, screens, prompts, archives, or system/status changes appear.
- `governance/object_function_review.md` if a physical object, resource, artifact, document, weapon, medicine, body trace, token, or clue drives the unit.
- `governance/reality_logic_review.md` if process, authority, institution logic, timing, survival cost, or jurisdiction matters.
- `governance/base_settings_review.md` if durable world rules or base settings may change.
- `governance/wiki_write_rules.md` before any canon sync.

### User Approval Boundary

A generated unit or design decision is not canon until the user approves it.

Do not synchronize, plan consequences, or build the next canon-dependent unit from an unapproved generated unit.

## Layer 9: Wiki Sync / Canon Update

Run immediately after the user approves canon and before planning the next canon-dependent discussion, design, or generated unit.

Primary sync file:

- `prompts/05_wiki_sync_after_chapter.md`

Governance:

- `governance/wiki_write_rules.md`

Deprecated old prompt:

- `prompts/06_chapter_state_update.md` is deprecated. Do not use it for current workflow.

For approved formal chapters, update:

- `novels/<novel_id>/wiki/chapter_states/chapter_<number>.md`

For approved partial scenes, design decisions, event facts, state changes, entity updates, relationship changes, and rule-system changes, update the smallest sufficient wiki records:

- Entity
- Timepoint
- State
- Relationship
- Event
- Session
- Mutation
- name registry
- style record
- chapter state
- other project-specific wiki file

Hard rule:

```text
User-approved canon -> wiki sync -> next canon-dependent step.
```

## Required Execution Order

For an extended-arena new novel:

```text
Layer 1A -> Layer 1B including Project Viability Gate -> Layer 2 -> Layer 3 -> Layer 4 retrieval / discussion prep -> user discussion / decision -> Layer 5 when needed -> Layer 6 scene or event design -> user-approved scope -> Layer 7 generation when needed -> Layer 8 consistency check -> user canon approval -> Layer 9 sync
```

For a standard new novel:

```text
Layer 1B including Project Viability Gate -> Layer 2 -> Layer 3 -> Layer 4 retrieval / discussion prep -> user discussion / decision -> Layer 5 when needed -> Layer 6 scene or event design when needed -> user-approved scope -> Layer 7 generation when needed -> Layer 8 consistency check -> user canon approval -> Layer 9 sync
```

For a fast trial:

```text
selected setup checks -> non-canon sketch / outline / desire test -> decide whether to build full wiki
```

For a normal later unit:

```text
Read wiki -> retrieve relevant narrative records -> discuss with user -> record approved decision -> design bounded scene / event / output -> generate when needed -> consistency check -> user canon approval -> wiki sync
```

## Existing Legacy Chapter States

Older test novels may contain chapter state files that predate the current template.

They should not block new workflow tests unless the user explicitly resumes that novel.

If resuming an old approved novel, migrate its latest chapter state to the current narrative model before planning the next formal canon-dependent unit.

## Non-Negotiable Stop Conditions

Do not formal draft if any of these are unresolved:

1. Fast Trial is being mistaken for canon.
2. Genre mode is unclear.
3. Genre operating model is missing or too vague.
4. Irreversible trend anchor is missing or weak.
5. Reader Hook / Payoff Ladder is missing for commercial long-form execution.
6. Name & Term Gate is missing or failed for recurring invented names or terms.
7. Initial wiki bootstrap is missing.
8. Base settings for the active novel are missing.
9. Relevant Entity / Event / State / Relationship records were not retrieved.
10. Time-aware state is needed but missing.
11. A proposed mutation lacks user approval.
12. Actor cognition boundary is missing for an important actor who drives logic.
13. The important generated unit has no usable gain, state movement, or consequence when required.
14. The main scene has no convergence point.
15. Unapproved invented terms appear where ordinary description would be clearer.
16. The story relies on system/report/log/status change as climax.
17. The user has not approved the current unit or change as canon.

Do not plan the next canon-dependent unit if any of these are unresolved:

1. Approved changes were not synchronized.
2. Important consequences were not recorded as Event or State movement.
3. New confirmed entity / organization / location / rule / relationship facts were not synchronized.
4. Newly approved or rejected terms were not synchronized into the name registry.
5. Next unit constraints are missing.
6. The next unit would need to rely on chat memory rather than wiki state.
7. The previous generated unit or design change was not explicitly approved as canon.