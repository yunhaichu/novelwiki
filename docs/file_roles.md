# Workflow File Roles

This file explains the role of each major workflow file after the collaborative narrative-model update.

Use this as the file responsibility index. It does not override execution order.

Execution authority order:

```text
1. docs/current_execution_flow.md     # short operating card and stop conditions
2. docs/narrative_model.md            # story-memory model
3. docs/workflow_layers.md            # authoritative full execution-order index
4. docs/interactive_writing_flow.md   # human-AI collaboration protocol
5. docs/file_roles.md                 # file responsibility index
6. specific prompt / governance file
7. older general checklist
```

## Core Execution Concept

The workflow is no longer batch-draft-first and no longer approval-gate-first.

NovelWiki now runs on:

```text
wiki-centered story memory
+ author-AI discussion
+ user decision before canon mutation
+ time-aware entity states
+ event-centered factual memory
+ relationship and consequence tracking
+ consistency check before sync or generation
+ generation only when needed
```

The author controls creative direction and canon decisions. The AI retrieves wiki records, exposes constraints, proposes options, helps refine story objects and events, generates bounded outputs when requested, and synchronizes only user-approved canon.

Heavy review is no longer the default. Most errors should be prevented through retrieval, discussion, and consistency checks before canon mutation or generation.

## Docs

### `docs/current_execution_flow.md`

Scope: global
Required: yes

Role: short operational checklist and path-selection card. It chooses the operating flow, states the default collaboration loop, and lists stop conditions.

### `docs/narrative_model.md`

Scope: global
Required: yes for current workflow

Role: defines the story-memory model: Entity, Timepoint, State, Relationship, Event, Session, Mutation, retrieval rule, mutation rule, and consistency check.

### `docs/workflow_layers.md`

Scope: global
Required: yes

Role: authoritative full execution-order index. Defines which layers and files run at setup, arc, discussion preparation, scene / event design, generation, consistency check, and canon update stages.

### `docs/interactive_writing_flow.md`

Scope: global
Required: yes for current workflow

Role: interaction protocol. Defines the human-AI collaboration loop: retrieve, discuss, decide, mutate wiki if approved, generate when needed, and sync approved canon.

### `docs/file_roles.md`

Scope: global
Required: yes

Role: file responsibility index. Does not override execution order.

### `docs/emergent_plot_workflow.md`

Scope: global
Required: reference

Role: conceptual overview. If it conflicts with current execution flow, narrative model, workflow layers, or interactive writing flow, prefer the current execution files.

### `docs/backups/workflow_snapshot_2026-06-09.md`

Scope: global
Required: conditional

Role: restore anchor before restructuring or cleanup.

## Setup Prompts

### `prompts/00_novel_spine.md`

Scope: per-novel
Required: yes

Role: defines novel core direction, type promise, protagonist or central-actor engine, contradiction, and what the story is not.

### `prompts/00_genre_mode_contract.md`

Scope: per-novel
Required: yes

Role: defines genre reader promise, pressure carriers, growth assets, scene rhythm, terminology budget, and anti-drift rules.

### `prompts/00_genre_operating_model.md`

Scope: per-novel
Required: yes

Role: defines how the genre world actually operates before canon events are generated.

### `prompts/00_irreversible_trend_anchor.md`

Scope: per-novel
Required: yes

Role: defines large irreversible trend, central growth or value trajectory, coupling, stage map, and hard constraints.

### `prompts/00_reality_causal_preflight.md`

Scope: per-novel / per-event / per-important unit
Required: yes for new event families and important units

Role: proves that proposed event pressure can naturally exist in the story world before writing.

### `prompts/00_base_settings_builder.md`

Scope: per-novel
Required: yes

Role: converts premise and selected reference settings into novel-specific base settings.

### `prompts/00_major_conflict_engine.md`

Scope: per-novel
Required: yes

Role: defines large pressure and conflict forces. For extended-arena stories, must operate under the largest approved arena and not shrink it without user approval.

### `prompts/00_dramatic_arena.md`

Scope: per-novel / per-stage
Required: yes

Role: turns large conflict into concrete arenas of organizations, locations, resources, hidden interests, embodied agents, and character actors.

### `prompts/00_protagonist_growth_track.md`

Scope: per-novel
Required: conditional

Role: defines controlled central-actor growth stages, current weakness, growth asset ladder, forbidden jumps, and route toward the approved final form when the project depends on such a track.

### `prompts/00_project_viability_gate.md`

Scope: per-novel
Required: yes before formal wiki bootstrap

Role: blocks weak concepts from entering formal wiki. It checks whether the project can sustain long-form escalation, whether the central actor has a usable engine, whether early units create retention and reusable assets, and whether reader return matches the selected genre promise.

Hard rule:

```text
No Project Viability Gate pass, no formal wiki bootstrap.
```

### `prompts/00_name_term_gate.md`

Scope: per-novel / per-entity / per-term
Required: yes before recurring named entities or invented terms

Role: checks names and terms before they enter project files, entity records, organization records, location records, world files, drafts, or canon. Function should appear before formal name when the name might confuse the reader.

### `prompts/00_wiki_bootstrap.md`

Scope: per-novel
Required: yes before formal canon-dependent drafting

Role: creates the initial per-novel wiki after setup approval and Project Viability Gate pass.

Fast Trial sketches are non-canon and do not require wiki bootstrap until the user decides to build a formal novel wiki.

## Extended Arena Setup Prompts

### `prompts/00_cosmic_civilization_arena.md`

Scope: per-novel
Required: yes only for projects that need a cosmic or civilization-scale arena

Role: defines largest arena, civilization routes, major factions, resource logic, home-civilization position when relevant, large irreversible trend, and opening visibility budget.

### `prompts/00_earth_civilization_value.md`

Scope: per-novel
Required: yes only when an Earth-like or home-civilization anchor matters

Role: defines why the home civilization is weak, why it still matters, why stronger powers observe or contest it, and how the central actor can affect its evaluation.

### `prompts/00_unified_power_logic.md`

Scope: per-novel
Required: yes when multiple rule systems coexist

Role: unifies multiple power, technology, magic, biological, psychic, social, or high-dimensional systems under shared variables: energy, storage, conversion, control interface, rule access, cost, and scaling.

### `prompts/00_modern_chinese_entry_bridge.md`

Scope: per-novel
Required: yes when a modern Chinese reader-entry bridge is part of the premise

Role: defines modern identity, reader familiarity, modern knowledge structure, first-contact mode, modern-thinking viewpoint, and emotional anchor.

### `prompts/00_webnovel_reader_hook_payoff_ladder.md`

Scope: per-novel / per-stage / per-important unit
Required: yes for commercial webnovel execution

Role: designs why readers continue: question, crisis, identity, relationship, world reveal, mechanism reveal, choice, resource, qualification, tactical win, or earned face-slapping when appropriate.

Face-slapping is optional, not the default.

## Narrative Model And Actor Prompts

### `docs/narrative_model.md`

Scope: global model reference
Required: yes for current workflow

Role: defines how wiki records should represent story memory with light structure and natural-language summaries.

### `prompts/00_organization_behavior_model.md`

Scope: per-novel, per major organization
Required: conditional; yes for recurring organizations

Role: defines public legitimacy, real interests, operating boundaries, packaging language, action ladder, embodied agents, and environmental modulation.

### `prompts/00_character_behavior_model.md`

Scope: per-novel, per major character
Required: conditional; yes for recurring major characters

Role: defines default behavior, environmental modulation, protected object, threshold behavior, extreme reaction, aftermath, and inner monologue mode.

### `prompts/00_character_expression_card.md`

Scope: per-novel, per major character
Required: conditional; yes for recurring speaking characters

Role: defines source-grounded speech patterns and how speech changes with risk, audience, authority, secrecy, and relationship.

### `prompts/00_actor_cognition_card.md`

Scope: per-novel / per major actor / per important scene actor
Required: yes when an actor drives logic, limited knowledge, or multi-party conflict

Role: prevents omniscient actors. Defines what each actor knows directly, infers, misunderstands, wants, fears, can afford, and cannot know.

### `governance/agent_state_rules.md`

Scope: multi-actor simulation / important scenes
Required: yes before multi-agent scene simulation

Role: ensures characters act from local pressure and partial knowledge, not outline knowledge.

## Arc, Event, And Scene Prompts

### `prompts/00_volume_state_plan.md`

Scope: per-stage / per-volume
Required: yes for long stories

Role: defines stage movement under irreversible trend and central growth or value trajectory.

### `prompts/00_chapter_pressure_card.md`

Scope: per-chapter / per-important unit
Required: optional / conditional

Role: defines current pressure before detailed scene or event design.

### `prompts/02_emergent_chapter_design.md`

Scope: per-chapter / per-important unit
Required: yes for important units

Role: designs through trend convergence, actor limited choices, reader hook/payoff, cost, leverage, and consequence chain. In the current workflow, it feeds discussion and decision rather than automatic prose.

Face-slapping is optional and must be justified by scene logic.

### `prompts/02_scene_convergence.md`

Scope: per-scene / per-event
Required: yes for major scenes or state-changing events

Role: defines pressure in the scene, convergence point, actor local worlds, environmental modulation, organization packaging, collision map, and performance beats.

### `prompts/02_scene_expression_state.md`

Scope: per-scene / per-event
Required: conditional

Role: adapts character expression cards to the current timepoint, relationship state, and scene pressure.

### `prompts/02_dialogue_intent.md`

Scope: per-scene / per-dialogue sequence
Required: conditional

Role: designs what each dialogue line must change before final prose is written.

### `prompts/00_multi_agent_scene_simulation.md`

Scope: per-scene / per-event
Required: conditional

Role: simulates multi-actor scenes before prose when more than two actors have hidden motives or many moving parts. Must follow `governance/agent_state_rules.md`.

### `prompts/01_scene_log_to_draft.md`

Scope: per-scene / per-chapter
Required: conditional

Role: converts an approved scene simulation or action log into prose. Should return `REVISE SIMULATION` if the action log is weak.

## Generation Prompt

### `prompts/01_writer.md`

Scope: per-approved unit
Required: yes for formal prose generation

Role: writes prose from current novel wiki, approved scope, approved names/terms, relevant Entity / Event / State / Relationship records, and relevant governance rules.

In the collaborative workflow, it must generate only the approved unit. It must not continue into the next unit, add unapproved canon, or silently solve unresolved design questions.

It enforces clear prose: action, dialogue, reaction, process, and consequence. It forbids summary voice and does not reward concise abstract conclusions.

## Consistency And Targeted Governance

### Always-on Consistency Check

Scope: every canon mutation and canon-dependent generation
Required: yes

Role: checks wiki contradiction, unapproved names/terms, missing time-aware states, actor omniscience, unsupported rule-system change, unrecorded consequences, chat-memory dependence, summary-only prose, and record-driven climax.

### Targeted governance files

Run only when triggered by specific risk:

- `governance/anti_ai_expression_review.md`
- `governance/emergent_plot_review.md`
- `governance/protagonist_growth_review.md`
- `governance/character_voice_review.md`
- `governance/anti_record_driven_plot.md`
- `governance/object_function_review.md`
- `governance/reality_logic_review.md`
- `governance/base_settings_review.md`
- `governance/wiki_write_rules.md`
- `governance/review_priority.md`

## Wiki Sync Prompt

### `prompts/05_wiki_sync_after_chapter.md`

Scope: per-approved canon change / per-approved chapter
Required: yes after user-approved canon

Role: updates the smallest sufficient wiki records after user approval.

Current sync targets include:

```text
Entity
Timepoint
State
Relationship
Event
Session
Mutation
chapter state
name registry
style
foreshadowing
project-specific wiki file
```

### `prompts/06_chapter_state_update.md`

Scope: deprecated
Required: no

Role: deprecated. Do not use in the current workflow.

## Legacy Compatibility

Older files may still use approval-gate language or chapter-first language.

When conflict appears, prefer:

```text
current_execution_flow.md
-> narrative_model.md
-> workflow_layers.md
-> interactive_writing_flow.md
-> file_roles.md
```

Do not reintroduce a batch-draft-first workflow unless the user explicitly asks for batch mode.