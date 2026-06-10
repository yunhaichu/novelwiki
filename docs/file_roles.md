# Workflow File Roles

This file explains the role of each major workflow file after the workflow cleanup.

Use this as the file responsibility index. Use `docs/workflow_layers.md` for execution order. Use `docs/current_execution_flow.md` for the short operational checklist.

## Current Priority Order

```text
1. docs/current_execution_flow.md
2. docs/workflow_layers.md
3. docs/file_roles.md
4. specific prompt / governance file
5. older general checklist
```

## Core Execution Concept

The current workflow is no longer event-first.

It runs on:

```text
world irreversible trend
+ protagonist irreversible final form
+ local character choices
+ trend convergence
```

The author controls the world trend and protagonist final form.

Characters control local choices.

Plot emerges when local choices are pulled back toward the irreversible trend.

## Docs

### `docs/current_execution_flow.md`

Scope: global
Required: yes

Role: short operational checklist. Defines the current 9-step execution order:

```text
Irreversible Trend Anchor
-> Name & Term Gate
-> Wiki Bootstrap
-> Actor Setup
-> Chapter Trend Convergence
-> Scene Design
-> Drafting
-> Review
-> Wiki Sync
```

### `docs/workflow_layers.md`

Scope: global
Required: yes

Role: canonical full execution-order index. Defines which workflow files run at new novel, volume, chapter, scene, draft, review, and canon-update layers.

### `docs/emergent_plot_workflow.md`

Scope: global
Required: reference

Role: conceptual overview. If it conflicts with the current execution flow, prefer `docs/current_execution_flow.md` and `docs/workflow_layers.md`.

### `docs/backups/workflow_snapshot_2026-06-09.md`

Scope: global
Required: conditional

Role: restore anchor before restructuring or cleanup.

## Reference Settings

### `reference_settings/README.md`

Scope: global
Required: yes

Role: explains that reference settings are reusable references, not canon.

### `reference_settings/usage_contract.md`

Scope: global
Required: yes for new novels

Role: governs how reference settings can be selected and converted into novel-specific base settings.

### `reference_settings/index.json`

Scope: global
Required: yes for new novels

Role: maps reference setting IDs to files.

### `reference_settings/genre_common/*.md`

Scope: global
Required: conditional

Role: genre reference boundaries. Use only the files relevant to the current novel.

### `reference_settings/power_system_common/base_laws.md`

Scope: global
Required: conditional

Role: reference rules for powers, anomalies, goldfingers, supernatural mechanisms, or similar systems.

## Setup Prompts

### `prompts/00_novel_spine.md`

Scope: per-novel
Required: yes

Role: defines the novel's core direction, promise, protagonist engine, contradiction, and what the story is not.

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

Role: defines the two highest-order anchors:

```text
world irreversible trend
protagonist irreversible final form
```

This file prevents event-first plotting.

Hard rule:

```text
No irreversible trend anchor, no chapter design.
```

### `prompts/00_reality_causal_preflight.md`

Scope: per-novel / per-chapter
Required: yes for new event families and important chapters

Role: proves that the proposed event can naturally exist in the genre world before writing.

### `prompts/00_base_settings_builder.md`

Scope: per-novel
Required: yes

Role: converts user premise and selected reference settings into novel-specific base settings.

### `prompts/00_major_conflict_engine.md`

Scope: per-novel
Required: yes

Role: defines macro pressure and large conflict forces. It should now operate under the irreversible trend anchor.

### `prompts/00_dramatic_arena.md`

Scope: per-novel / per-volume
Required: yes

Role: turns macro conflict into concrete arenas of organizations, locations, resources, hidden interests, and embodied agents.

### `prompts/00_protagonist_growth_track.md`

Scope: per-novel
Required: yes

Role: defines controlled protagonist growth stages, current weakness, growth asset ladder, forbidden jumps, and the route toward the protagonist final form.

### `prompts/00_name_term_gate.md`

Scope: per-novel / per-character / per-term
Required: yes before new named entities or invented terms

Role: checks names and terms before they enter project files, character files, organization files, world files, drafts, or canon.

It covers people, organizations, places, objects, tools, resources, jobs, ranks, procedures, status labels, ability labels, recurring slang, and chapter-critical objects.

Hard rule:

```text
No Name & Term Gate, no new named entity or invented term.
```

If a term is not approved, use ordinary description instead.

### `prompts/00_wiki_bootstrap.md`

Scope: per-novel
Required: yes

Role: creates or updates the initial per-novel wiki after setup approval and before chapter drafting.

Required outputs include:

```text
project.md
base_settings.md
style.md
name_registry.md
protagonist_growth.md
initial character / world / organization files as needed
```

Hard rule:

```text
No wiki bootstrap, no draft.
```

## Actor Setup Prompts

### `prompts/00_organization_behavior_model.md`

Scope: per-novel, per major organization
Required: conditional; yes for recurring organizations

Role: defines public legitimacy, real interests, operating boundaries, packaging language, action ladder, embodied agents, and environmental modulation for an organization.

### `prompts/00_character_behavior_model.md`

Scope: per-novel, per major character
Required: conditional; yes for recurring major characters

Role: defines default behavior, environmental modulation, core protected object, threshold behavior, extreme reaction, aftermath, and inner monologue mode.

New named characters must pass Name & Term Gate before a named character file is written.

### `prompts/00_character_expression_card.md`

Scope: per-novel, per major character
Required: conditional; yes for recurring speaking characters

Role: defines source-grounded speech patterns and how those speech patterns change with risk, audience, authority, secrecy, and relationship.

## Volume / Arc Prompts

### `prompts/00_volume_state_plan.md`

Scope: per-volume
Required: yes for long stories

Role: defines volume state movement under the irreversible world trend and protagonist final-form trajectory.

### `prompts/00_chapter_pressure_card.md`

Scope: per-chapter
Required: optional / conditional

Role: defines chapter pressure before detailed chapter design. Useful for complex chapters or when the story is drifting.

## Chapter Prompts

### `prompts/02_emergent_chapter_design.md`

Scope: per-chapter
Required: yes for important chapters

Role: designs a chapter through trend convergence, not random events.

It requires:

- world irreversible trend;
- protagonist irreversible final form;
- current stage pressure;
- local choices;
- shared trend node;
- cost;
- usable leverage;
- reader reward;
- consequence chain.

### `prompts/02_advantage_reward_ledger.md`

Scope: per-chapter
Required: yes for important chapters

Role: ensures the protagonist gains usable leverage, reader reward, and at least one asset that moves toward protagonist final form.

Prevents punishment-only chapters and random clue accumulation.

### `prompts/02_opening_chapter_brief.md`

Scope: per-opening / per-arc opening
Required: conditional if present

Role: defines opening chapter execution constraints after reader-entry gate. Use for first chapter or major new arc.

## Scene Prompts

### `prompts/02_scene_convergence.md`

Scope: per-scene
Required: yes for major scenes

Role: defines trend pressure in the scene, convergence point, actor local worlds, environmental modulation, organization packaging, collision map, and performance beats.

The scene must begin from actor goals under trend pressure, not from a preselected event.

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

Role: simulates multi-actor scenes before prose when more than two actors have hidden motives or many moving parts.

### `prompts/01_scene_log_to_draft.md`

Scope: per-scene / per-chapter
Required: conditional

Role: converts an approved scene simulation or action log into prose. Should return `REVISE SIMULATION` if the action log is weak.

## Drafting Prompt

### `prompts/01_writer.md`

Scope: per-chapter
Required: yes

Role: writes chapter draft from current novel wiki, trend-converged chapter design, scene convergence, approved names/terms, and relevant governance rules.

It enforces xiaobai prose: clear action, dialogue, reaction, process, and consequence. It forbids summary voice and does not reward concise abstract conclusions.

Do not use it before setup, wiki bootstrap, trend convergence, chapter design, and Name & Term Gate are clear.

## Review Governance

### `governance/reality_logic_review.md`

Scope: per-chapter
Required: yes for important chapters

Role: checks whether the event obeys genre reality, normal process, authority, timing, survival cost, institution logic, and role knowledge.

### `governance/object_function_review.md`

Scope: per-object / per-chapter
Required: conditional

Role: checks whether a key object has earned its importance.

### `governance/emergent_plot_review.md`

Scope: per-chapter
Required: yes for important chapters

Role: checks major conflict connection, level frequency, organization function, scene convergence, protagonist advantage, reader reward, consequence chain, randomness, repetition, and record-driven plot.

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

### `governance/review_checklist.md`

Scope: per-chapter
Required: optional general fallback

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

Role: defines what can and cannot be written into a novel wiki, including character behavior, organization behavior, protagonist growth, scene performance distinctions, approved/rejected names and terms, and chapter state boundaries.

### `prompts/05_wiki_sync_after_chapter.md`

Scope: per-chapter / per-canon update
Required: yes after every approved chapter

Role: creates or updates `chapter_states/chapter_<number>.md` and synchronizes confirmed character, organization, world, growth, timeline, relationship, foreshadowing, style, name, term, world-trend progress, and protagonist-final-form progress before the next chapter is planned.

Hard rule:

```text
Approved chapter -> wiki sync -> next chapter.
```

### `governance/chapter_state_update_review.md`

Scope: per-canon update
Required: conditional if present

Role: should review chapter-state update draft before canon write. If absent, use `wiki_write_rules.md` manually.

## Operational Governance

### `governance/batch_commit_workflow.md`

Scope: repository operations
Required: conditional

Role: recommends grouped commits instead of file-by-file commits when tooling allows.

## Deprecated / Compatibility Notes

Older files are not automatically wrong. Prefer newer layered flow when there is conflict.

If a file is missing but referenced, treat it as planned or optional unless `workflow_layers.md` marks the function as non-negotiable.
