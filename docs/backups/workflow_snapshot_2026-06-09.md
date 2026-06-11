# Workflow Snapshot Before Restructure

Date: 2026-06-09

Purpose: preserve the current workflow state before any cleanup, merging, renaming, or restructuring of prompts / governance / docs.

## Snapshot Commit

Use this commit as the restore anchor:

```text
2cfe5d803b18b298977b2afdc4819b390dd1f9eb
```

This snapshot records the state after adding:

- genre mode contract;
- reality-causal preflight;
- reality logic review;
- object function review;
- protagonist growth track;
- protagonist growth review;
- organization behavior model;
- character behavior model;
- scene convergence;
- anti-record-driven plot governance;
- updated emergent workflow and chapter design.

## Restore Principle

Do not rely on memory if restructuring breaks something.

Restore any file from the snapshot commit:

```bash
git checkout 2cfe5d803b18b298977b2afdc4819b390dd1f9eb -- <path>
```

Or inspect a file at the snapshot commit:

```bash
git show 2cfe5d803b18b298977b2afdc4819b390dd1f9eb:<path>
```

## Files Covered By Snapshot

### Root / overview

- `README.md`

### Docs

- `docs/emergent_plot_workflow.md`
- `docs/development_plan.md` if present

### Core opening / setup prompts

- `prompts/00_novel_spine.md`
- `prompts/00_volume_state_plan.md`
- `prompts/00_chapter_pressure_card.md`
- `prompts/00_multi_agent_scene_simulation.md`
- `prompts/00_base_settings_builder.md`
- `prompts/00_genre_mode_contract.md`
- `prompts/00_reality_causal_preflight.md`
- `prompts/00_major_conflict_engine.md`
- `prompts/00_dramatic_arena.md`
- `prompts/00_organization_behavior_model.md`
- `prompts/00_character_behavior_model.md`
- `prompts/00_character_expression_card.md`
- `prompts/00_protagonist_growth_track.md`

### Chapter / scene prompts

- `prompts/01_writer.md`
- `prompts/01_scene_log_to_draft.md`
- `prompts/02_emergent_chapter_design.md`
- `prompts/02_deprecated_advantage_reward_ledger.md`
- `prompts/02_scene_convergence.md`
- `prompts/02_scene_expression_state.md`
- `prompts/02_dialogue_intent.md`
- `prompts/02_opening_chapter_brief.md` if present
- `prompts/04_review_hook.md`
- `prompts/05_chapter_state_update.md` if present

### Governance / review

- `governance/wiki_retrieval_rules.md`
- `governance/wiki_write_rules.md`
- `governance/base_settings_review.md`
- `governance/review_checklist.md`
- `governance/anti_ai_taste_check.md`
- `governance/ai_taste_language_grounding.md`
- `governance/batch_commit_workflow.md`
- `governance/anti_record_driven_plot.md`
- `governance/reality_logic_review.md`
- `governance/object_function_review.md`
- `governance/emergent_plot_review.md`
- `governance/protagonist_growth_review.md`
- `governance/character_voice_review.md`
- `governance/anti_ai_expression_review.md`
- `governance/reader_entry_review.md` if present
- `governance/opening_chapter_brief_review.md` if present
- `governance/chapter_state_update_review.md` if present

### Reference settings

- `reference_settings/README.md`
- `reference_settings/usage_contract.md`
- `reference_settings/index.json`
- `reference_settings/genre_common/modern_common.md`
- `reference_settings/genre_common/generic_common.md`
- `reference_settings/genre_common/xianxia_common.md`
- `reference_settings/genre_common/apocalypse_common.md`
- `reference_settings/genre_common/sci_fi_cyber_common.md`
- `reference_settings/power_system_common/base_laws.md`

## Restructure Rule

Before editing or deleting any file above:

1. Check whether the file's responsibility is moving into another file.
2. Update `docs/workflow_layers.md` or equivalent index first.
3. Do not delete source files until the replacement path is documented.
4. If cleanup introduces regressions, restore from the snapshot commit.

## Notes

This is a backup pointer, not a duplicate workflow tree. Git history is the backup store; this file records the exact restore anchor and the scope of files protected by it.
