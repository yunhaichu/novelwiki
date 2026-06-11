# Workflow File Roles

This file explains the role of each major workflow file after the workflow cleanup.

Use this as the file responsibility index.

Execution authority order:

```text
1. docs/current_execution_flow.md   # short path-selection card
2. docs/workflow_layers.md         # authoritative full execution-order index
3. docs/file_roles.md              # file responsibility index
4. specific prompt / governance file
5. older general checklist
```

## Core Execution Concept

The workflow is no longer event-first.

Standard long-form flow runs on:

```text
world irreversible trend
+ protagonist irreversible final form
+ local character choices
+ trend convergence
+ reader hook/payoff
+ project viability before formal wiki
```

Macro modern-to-cosmic flow additionally runs on:

```text
cosmic civilization arena
+ Earth civilization value
+ unified power logic
+ modern Chinese reader bridge
+ reader hook/payoff ladder
```

The author controls the large trend and protagonist final form. Characters control local choices. Plot emerges when local choices are pulled back toward the large trend. Important chapters must give the reader a concrete reason to continue. Formal projects must prove they can sustain long-form execution before wiki bootstrap.

## Docs

### `docs/current_execution_flow.md`

Scope: global
Required: yes

Role: short operational checklist and path-selection card. It chooses standard flow, macro modern-to-cosmic flow, or non-canon fast trial mode.

### `docs/workflow_layers.md`

Scope: global
Required: yes

Role: authoritative full execution-order index. Defines which layers and files run at setup, volume, chapter, scene, draft, review, and canon-update stages.

### `docs/file_roles.md`

Scope: global
Required: yes

Role: file responsibility index. Does not override execution order.

### `docs/emergent_plot_workflow.md`

Scope: global
Required: reference

Role: conceptual overview. If it conflicts with current execution flow or workflow layers, prefer `docs/current_execution_flow.md` and `docs/workflow_layers.md`.

### `docs/backups/workflow_snapshot_2026-06-09.md`

Scope: global
Required: conditional

Role: restore anchor before restructuring or cleanup.

## Macro Modern-To-Cosmic Setup Prompts

### `prompts/00_cosmic_civilization_arena.md`

Scope: per-novel
Required: yes for macro modern-to-cosmic stories

Role: defines largest story arena, civilization routes, major factions, resource logic, Earth position, cosmic irreversible trend, and chapter-one visibility budget.

### `prompts/00_earth_civilization_value.md`

Scope: per-novel
Required: yes for Earth-entry cosmic stories

Role: defines why Earth is weak, why Earth still matters, why high civilizations observe or contest it, and how the protagonist can make Earth be reevaluated.

### `prompts/00_unified_power_logic.md`

Scope: per-novel
Required: yes when multiple power systems coexist

Role: unifies cultivation, magic, technology, biological systems, psychic systems, and high-dimensional laws under shared variables: energy, storage, conversion, control interface, law access, cost, and civilization scaling.

### `prompts/00_modern_chinese_entry_bridge.md`

Scope: per-novel
Required: yes when protagonist comes from modern China / modern Earth

Role: defines modern identity, reader-laoxiang feeling, modern knowledge structure, first contact mode, modern-thinking viewpoint, and Earth emotional anchor.

### `prompts/00_webnovel_pleasure_ladder.md`

Scope: per-novel / per-volume / per-chapter
Required: yes for commercial webnovel execution

Role: current internal function is Reader Hook And Payoff Ladder. It designs why readers continue: question, crisis, identity, relationship, world reveal, mechanism reveal, choice, resource, qualification, tactical win, or earned face-slapping when appropriate.

Face-slapping is optional, not the default.

### `prompts/01_modern_to_cosmic_opening.md`

Scope: chapter one / opening arc
Required: yes for modern-to-cosmic chapter one

Role: opens with modern ordinary pressure, believable first-contact psychology, high-civilization intrusion, one small macro-world crack, and a concrete reader hook/payoff.

## Standard Setup Prompts

### `prompts/00_novel_spine.md`

Scope: per-novel
Required: yes

Role: defines novel core direction, type promise, protagonist engine, contradiction, and what the story is not.

### `prompts/00_genre_mode_contract.md`

Scope: per-novel
Required: yes

Role: defines genre reader promise, pressure carriers, growth assets, scene rhythm, terminology budget, and anti-drift rules.

### `prompts/00_genre_operating_model.md`

Scope: per-novel
Required: yes

Role: defines how the genre world actually operates before chapter events are generated.

### `prompts/00_irreversible_trend_anchor.md`

Scope: per-novel
Required: yes

Role: defines world / civilization irreversible trend, Earth civilization pressure if relevant, protagonist irreversible final form, coupling, stage map, and hard constraints.

### `prompts/00_reality_causal_preflight.md`

Scope: per-novel / per-chapter
Required: yes for new event families and important chapters

Role: proves that proposed event pressure can naturally exist in the genre world before writing.

### `prompts/00_base_settings_builder.md`

Scope: per-novel
Required: yes

Role: converts premise and selected reference settings into novel-specific base settings.

### `prompts/00_major_conflict_engine.md`

Scope: per-novel
Required: yes

Role: defines macro pressure and large conflict forces. For macro stories, must operate under the cosmic civilization arena and not shrink it.

### `prompts/00_dramatic_arena.md`

Scope: per-novel / per-volume
Required: yes

Role: turns macro conflict into concrete arenas of organizations, locations, resources, hidden interests, embodied agents, and character actors.

### `prompts/00_protagonist_growth_track.md`

Scope: per-novel
Required: yes

Role: defines controlled protagonist growth stages, current weakness, growth asset ladder, forbidden jumps, and route toward final form. For macro stories, include cross-civilization growth and Earth-facing assets.

### `prompts/00_project_viability_gate.md`

Scope: per-novel
Required: yes before formal wiki bootstrap

Role: blocks weak concepts from entering formal wiki. It checks whether the project can sustain long-form escalation, whether the protagonist final form is stronger than good person / witness / helper, whether the first three chapters create retention and reusable growth assets, and whether reader return matches type-webnovel expectations.

Hard rule:

```text
No Project Viability Gate pass, no formal wiki bootstrap.
```

### `prompts/00_name_term_gate.md`

Scope: per-novel / per-character / per-term
Required: yes before new named entities or invented terms

Role: checks names and terms before they enter project files, character files, organization files, world files, drafts, or canon. For macro terms, function must appear before formal name.

### `prompts/00_wiki_bootstrap.md`

Scope: per-novel
Required: yes before formal drafting

Role: creates initial per-novel wiki after setup approval and Project Viability Gate pass. Required core files now include:

```text
project.md
base_settings.md
style.md
name_registry.md
protagonist_growth.md
timeline.md
relationships.md
foreshadowing.md
```

Fast Trial sketches are non-canon and do not require wiki bootstrap until the user decides to build a formal novel wiki.

## Actor Setup Prompts

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
Required: yes when an actor drives chapter logic, limited knowledge, or multi-party conflict

Role: prevents omniscient actors. Defines what each actor knows directly, infers, misunderstands, wants, fears, can afford, and cannot know.

### `governance/agent_state_rules.md`

Scope: multi-actor simulation / important scenes
Required: yes before multi-agent scene simulation

Role: ensures characters act from local pressure and partial knowledge, not outline knowledge.

## Volume / Arc Prompts

### `prompts/00_volume_state_plan.md`

Scope: per-volume
Required: yes for long stories

Role: defines volume state movement under irreversible trend and protagonist-final-form trajectory.

### `prompts/00_chapter_pressure_card.md`

Scope: per-chapter
Required: optional / conditional

Role: defines chapter pressure before detailed chapter design.

## Chapter Prompts

### `prompts/02_emergent_chapter_design.md`

Scope: per-chapter
Required: yes for important chapters

Role: designs a chapter through trend convergence, actor limited choices, reader hook/payoff, cost, leverage, and consequence chain.

Face-slapping is optional and must be justified by scene logic.

### `prompts/02_advantage_reward_ledger.md`

Scope: per-chapter
Required: **deprecated**

Role: [DEPRECATED] Function merged into `prompts/05_wiki_sync_after_chapter.md`.
Read the chapter design's "Planned Advantages" from `prompts/02_emergent_chapter_design.md`.
The wiki_sync prompt now handles both planned and actual advantage tracking.
See `prompts/02_advantage_reward_ledger.md` for migration guide.

### `prompts/02_opening_chapter_brief.md`

Scope: per-opening / per-arc opening
Required: conditional if present

Role: older opening chapter constraint file. For modern-to-cosmic chapter one, prefer `prompts/01_modern_to_cosmic_opening.md`.

## Scene Prompts

### `prompts/02_scene_convergence.md`

Scope: per-scene
Required: yes for major scenes

Role: defines trend pressure in the scene, convergence point, actor local worlds, environmental modulation, organization packaging, collision map, and performance beats.

### `prompts/02_scene_expression_state.md`

Scope: per-scene
Required: conditional

Role: adapts character expression cards to the current scene.

### `prompts/02_dialogue_intent.md`

Scope: per-scene / per-dialogue sequence
Required: conditional

Role: designs what each dialogue line must change before final prose is written.

### `prompts/00_multi_agent_scene_simulation.md`

Scope: per-scene
Required: conditional

Role: simulates multi-actor scenes before prose when more than two actors have hidden motives or many moving parts. Must follow `governance/agent_state_rules.md`.

### `prompts/01_scene_log_to_draft.md`

Scope: per-scene / per-chapter
Required: conditional

Role: converts an approved scene simulation or action log into prose. Should return `REVISE SIMULATION` if the action log is weak.

## Drafting Prompt

### `prompts/01_writer.md`

Scope: per-chapter
Required: yes for formal drafting

Role: writes chapter draft from current novel wiki, trend-converged chapter design, scene convergence, approved names/terms, and relevant governance rules.

It enforces xiaobai prose: clear action, dialogue, reaction, process, and consequence. It forbids summary voice and does not reward concise abstract conclusions.

## Review Governance

### `governance/reality_logic_review.md`

Scope: per-chapter
Required: yes for important chapters

Role: checks whether event obeys genre reality, normal process, authority, timing, survival cost, institution logic, and role knowledge.

### `governance/object_function_review.md`

Scope: per-object / per-chapter
Required: conditional

Role: checks whether a key object has earned its importance.

### `governance/emergent_plot_review.md`

Scope: per-chapter
Required: yes for important chapters

Role: checks major conflict connection, level frequency, organization function, scene convergence, protagonist advantage, reader hook/payoff, consequence chain, randomness, repetition, and record-driven plot.

### `governance/protagonist_growth_review.md`

Scope: per-chapter
Required: yes for protagonist-centered chapters

Role: checks active growth stage, pressure-to-weakness fit, cost, usable leverage, no jump, large trend respect, final-form movement, and state update.

### `governance/character_voice_review.md`

Scope: per-chapter / per-scene
Required: conditional

Role: checks source-grounded character voice, listener-specific mode, environmental modulation, knowledge boundary, dialogue function, and anti-pretty-summary.

### `governance/anti_ai_expression_review.md`

Scope: per-chapter
Required: conditional

Role: removes pretty summaries, unsupported metaphors, generic body reactions, identity-label sentences, psychological summaries, dialogue-as-narration, same rhythm, record-centered expression, summary voice, and ungrounded invented terms.

### `governance/anti_record_driven_plot.md`

Scope: per-chapter
Required: conditional

Role: prevents records, reports, systems, logs, status changes, and prompts from driving the plot.

### `governance/base_settings_review.md`

Scope: per-novel setup / when base settings change
Required: yes when base settings are built or updated

Role: reviews scope, source support, reference/canon boundary, authority/process/resource rules, and pending gaps.

### `governance/review_priority.md`

Scope: global
Required: yes

Role: defines priority levels (P0-block, P1-must-fix, P2-should-fix, P3-observation), conflict resolution rules, and execution order when multiple review files are triggered simultaneously. Read this first when running multiple reviews.

### `governance/review_checklist.md`

Scope: per-chapter
Required: optional fallback

Role: older general review checklist. Use as a simple review when newer specialized checks are excessive.

### `governance/anti_ai_taste_check.md`

Scope: per-chapter
Required: conditional

Role: older AI-taste review focused on template reuse, endings, repeated jokes, concrete memory points, and long-form direction.

### `governance/ai_taste_language_grounding.md`

Scope: global guidance
Required: reference

Role: explains common Chinese prose AI-taste issues and repair principles.

## Wiki Governance

### `governance/wiki_retrieval_rules.md`

Scope: per-chapter
Required: yes before drafting

Role: defines what canon files must be read before writing and prevents reference settings from being treated as canon.

### `governance/wiki_write_rules.md`

Scope: per-canon update
Required: yes

Role: defines what can and cannot be written into a novel wiki.

### `prompts/05_wiki_sync_after_chapter.md`

Scope: per-approved-formal-chapter / per-canon update
Required: yes after every approved formal chapter

Role: creates or updates chapter state and synchronizes confirmed character, organization, world, growth, timeline, relationship, foreshadowing, style, name, term, world/civilization trend progress, Earth-status progress when relevant, protagonist-final-form progress, and reader hook/payoff.

### `prompts/06_chapter_state_update.md`

### `novels/<novel_id>/wiki/reader_debt_tracker.md`

Tracks all outstanding reader debts across chapters. Each entry has priority (P0/P1/P2), age, and status. Updated by wiki sync after each chapter. If a P0 debt is >= 3 chapters old or P1 >= 6, the next chapter must address it.

### `novels/<novel_id>/wiki/volume_XX_rhythm_tracker.md`

Tracks volume-level rhythm across chapters. Includes breathing chapter budget, chapter-by-chapter state movement log, and 7 hard checks (consecutive stateless chapters, mystery-without-payoff streaks, hook repetition, breather ratio, debt aging). Updated by wiki sync and volume state plan.

Status: deprecated

Role: legacy compatibility only. Do not use for current workflow.

## Operational Governance

### `governance/batch_commit_workflow.md`

Scope: repository operations
Required: conditional

Role: recommends grouped commits instead of file-by-file commits when tooling allows.

## Deprecated / Compatibility Notes

Older test novels and legacy chapter state files are regression examples, not global workflow authority.

If resuming an old approved novel, migrate its latest chapter state to the current template before planning the next formal chapter.

If a file is referenced as optional or `if present`, absence does not block execution.
