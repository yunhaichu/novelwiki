# Workflow Layers

This is the operational entry point for the current novel-generation workflow.

The repository has accumulated many prompts and governance files. Do not run all files for every chapter. Use this layered flow to decide which files apply.

## Layer 0: Safety Snapshot

Purpose: protect the current workflow before restructuring or cleanup.

Run when:

- before reorganizing prompts or governance files;
- before deleting, merging, or renaming workflow files.

Files:

- `docs/backups/workflow_snapshot_2026-06-09.md`

## Layer 1: New Novel Setup

Run once per novel, before any chapter planning.

Purpose: define the novel's genre, operating world, base boundaries, macro pressure, major actors, protagonist growth path, Name & Term Gate, and initial wiki.

Required files:

1. `prompts/00_novel_spine.md`
2. `prompts/00_genre_mode_contract.md`
3. `prompts/00_genre_operating_model.md`
4. `prompts/00_reality_causal_preflight.md` for first major premise / opening event family
5. `prompts/00_base_settings_builder.md`
6. `prompts/00_major_conflict_engine.md`
7. `prompts/00_dramatic_arena.md`
8. `prompts/00_protagonist_growth_track.md`
9. `prompts/00_name_term_gate.md`
10. `prompts/00_wiki_bootstrap.md`

Supporting reference files:

- `reference_settings/usage_contract.md`
- `reference_settings/index.json`
- selected files under `reference_settings/genre_common/`
- selected files under `reference_settings/power_system_common/` only if the novel explicitly contains powers, anomalies, or goldfingers.

Required order inside Layer 1:

```text
premise / type promise
-> genre mode
-> genre operating model
-> base setting boundaries
-> Name & Term Gate
-> project.md
-> name_registry.md
-> other wiki bootstrap files
```

Name & Term Gate must run before `project.md`, character files, organization files, world files, city names, object names, process names, status labels, ability labels, slang, or key terms are written.

Required wiki outputs:

- `novels/<novel_id>/wiki/project.md`
- `novels/<novel_id>/wiki/base_settings.md`
- `novels/<novel_id>/wiki/style.md`
- `novels/<novel_id>/wiki/name_registry.md`
- `novels/<novel_id>/wiki/protagonist_growth.md`
- organization and character files as needed.

Hard rules:

```text
No Name & Term Gate, no project file.
No wiki bootstrap, no chapter draft.
```

## Layer 2: Actor Model Setup

Run once for major recurring organizations and characters. Update only when canon changes.

Purpose: prevent static labels, abstract organizations, and unsupported character voice.

Organization files:

- `prompts/00_organization_behavior_model.md`

Character files:

- `prompts/00_character_behavior_model.md`
- `prompts/00_character_expression_card.md`

Guidance:

- Major forces need organization behavior models.
- Important recurring characters need behavior models and expression cards.
- Temporary characters do not need full models, but their role, knowledge, goal, and scene function must be clear.

## Layer 3: Volume / Arc Planning

Run once per volume, arc, or large stage.

Purpose: define the current large trend, stage pressure, protagonist growth stage, and recurring consequence pattern.

Files:

- `prompts/00_volume_state_plan.md`
- `prompts/00_chapter_pressure_card.md` for upcoming chapter pressure when needed.

Outputs:

- volume attractor;
- active protagonist growth stage;
- organization pressure map;
- reader promise for the arc;
- constraints on what must not escalate yet.

## Layer 4: Chapter Preflight

Run before designing a chapter.

Purpose: prove that the chapter event can naturally exist in the selected genre world before writing it.

Required files:

1. `prompts/00_reality_causal_preflight.md`
2. `prompts/02_emergent_chapter_design.md`
3. `prompts/02_advantage_reward_ledger.md`

Use when:

- the chapter introduces a new event type;
- the chapter depends on an institution, craft, workflow, spell, resource, body cost, legal rule, sect rule, or industry process;
- earlier drafts produced logic errors.

Outputs:

- event feasibility;
- normal process;
- key actors and their natural roles;
- key object function;
- protagonist cost and usable leverage;
- result attractor.

## Layer 5: Reader Entry / Opening Control

Run for first chapters, new arcs, new worlds, new power systems, or complex settings.

Purpose: make the reader understand the immediate situation without requiring prior setting knowledge.

Files:

- `prompts/00_reader_entry_gate.md` if present
- `prompts/02_opening_chapter_brief.md` if present
- `governance/reader_entry_review.md` if present
- `governance/opening_chapter_brief_review.md` if present

If these files are missing, use the same checks manually:

- protagonist is clear;
- immediate pressure is clear;
- reader knows what can be lost now;
- unfamiliar terms are limited;
- function appears before formal name;
- the chapter has a concrete reader itch.

## Layer 6: Scene Design

Run for each important scene. For simple transition scenes, this can be shortened.

Purpose: make the scene emerge from multiple actors acting around a shared convergence point.

Required files for major scenes:

1. `prompts/02_scene_convergence.md`
2. `prompts/02_scene_expression_state.md`
3. `prompts/02_dialogue_intent.md`
4. `prompts/00_multi_agent_scene_simulation.md` when the scene has more than two active actors or complex hidden motives.

Outputs:

- convergence point;
- actor local worlds;
- environmental modulation;
- organization packaging if relevant;
- collision map;
- performance beats;
- dialogue intent.

## Layer 7: Drafting

Run after chapter and scene planning.

Files:

- `prompts/01_writer.md`
- `prompts/01_scene_log_to_draft.md` if a scene simulation/action log exists.

Rules:

- Do not let interfaces write the story.
- Do not let narrator explanation replace character performance.
- Apply genre mode before universal workflow rules.
- Use current novel wiki as canon.
- Do not import reference settings directly into prose.
- Do not introduce unapproved names or terms; use ordinary description until the Name & Term Gate approves them.

## Layer 8: Review / Revision

Run after draft.

Do not run every review on every minor scene. Use the review matrix below.

### Always run for important chapters

- `governance/emergent_plot_review.md`
- `governance/protagonist_growth_review.md`
- `governance/review_checklist.md`

### Run when genre / reality / object logic is involved

- `governance/reality_logic_review.md`
- `governance/object_function_review.md`

### Run when systems, records, reports, logs, workflows, or documents appear

- `governance/anti_record_driven_plot.md`

### Run when character voice, dialogue, AI flavor, or invented terms are a concern

- `governance/character_voice_review.md`
- `governance/anti_ai_expression_review.md`
- `governance/anti_ai_taste_check.md`
- `governance/ai_taste_language_grounding.md`

### Run when base settings or canon consistency is involved

- `governance/base_settings_review.md`
- `governance/wiki_retrieval_rules.md`
- `governance/wiki_write_rules.md`

## Layer 9: Wiki Sync / Canon Update

Run immediately after the chapter is approved and before planning the next chapter.

Purpose: synchronize approved prose into the per-novel wiki so the next chapter reads canon rather than relying on chat memory.

Required files:

1. `prompts/05_wiki_sync_after_chapter.md`
2. `governance/wiki_write_rules.md`
3. `governance/chapter_state_update_review.md` if present

Always create or update:

- `novels/<novel_id>/wiki/chapter_states/chapter_<number>.md`

Update relevant character, organization, world, growth, timeline, relationship, foreshadowing, style, name, and term files only when approved prose confirms new facts.

Hard rule:

```text
Approved chapter -> wiki sync -> next chapter.
```

## Required Execution Order

For a new novel:

```text
Layer 1 including Name & Term Gate and wiki bootstrap -> Layer 2 -> Layer 3 -> Layer 4 -> Layer 5 -> Layer 6 -> Layer 7 -> Layer 8 -> Layer 9 wiki sync
```

For a normal later chapter:

```text
Read wiki -> Layer 3 check -> Layer 4 -> Layer 6 -> Layer 7 -> Layer 8 -> Layer 9 wiki sync
```

For a simple low-stakes transition chapter:

```text
Read wiki -> Layer 4 light -> Layer 7 -> Layer 8 light -> Layer 9 wiki sync
```

## Non-Negotiable Gates

Do not draft if any of these are unresolved:

1. Genre mode is unclear.
2. Genre operating model is missing or too vague.
3. Name & Term Gate is missing or failed.
4. Initial wiki bootstrap is missing.
5. Base settings for the active novel are missing.
6. Reality-causal preflight says the core event is unnatural.
7. The protagonist has no active growth stage.
8. The chapter has no usable protagonist gain.
9. The main scene has no convergence point.
10. The key object has no natural function.
11. Unapproved invented terms appear where ordinary description would be clearer.
12. The story relies on system/report/log/status change as climax.

Do not plan the next chapter if any of these are unresolved:

1. Approved chapter has no chapter state file.
2. New confirmed character / organization / world facts were not synchronized.
3. Newly approved or rejected terms were not synchronized into the name registry.
4. Next chapter constraints are missing.
5. The next chapter would need to rely on chat memory rather than wiki state.
