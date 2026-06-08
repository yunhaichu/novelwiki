# Implementation Status: Reader-Entry Workflow Upgrade

This file tracks implementation progress for `docs/development_plan.md`.

## Completed

### Type Contract

Implemented:

```text
prompts/00_type_contract.md
governance/type_contract_review.md
```

Integrated into:

```text
prompts/00_outline_generation.md
prompts/00_beat_generator.md
governance/beat_review.md
prompts/02_chapter_brief.md
governance/chapter_brief_review.md
prompts/01_writer.md
prompts/04_review_hook.md
prompts/05_golden_three_review.md
```

### Reader Entry Gate

Implemented:

```text
prompts/00_reader_entry_gate.md
governance/reader_entry_review.md
```

Integrated into:

```text
prompts/04_review_hook.md
prompts/01_writer.md
prompts/05_golden_three_review.md
```

Reader-entry failure now outranks brief alignment in chapter review.

### Opening Chapter Brief

Implemented:

```text
prompts/02_opening_chapter_brief.md
governance/opening_chapter_brief_review.md
```

Opening chapters now use a smaller reader-entry-focused brief instead of the full ordinary chapter brief.

### Genre-Neutral Longform Inertia

Updated:

```text
governance/longform_ai_inertia_check.md
```

The previous cultivation-specific global rule was replaced with a genre-neutral rule:

```text
Local Process Must Convert Into Declared Main Genre Promise
```

### Consequence Chain

Implemented:

```text
governance/consequence_chain_check.md
```

Integrated into:

```text
prompts/00_beat_generator.md
governance/beat_review.md
prompts/02_chapter_brief.md
governance/chapter_brief_review.md
prompts/01_writer.md
prompts/03_revision.md
prompts/05_golden_three_review.md
```

### Conflict Escalation

Implemented:

```text
governance/conflict_escalation_check.md
```

Integrated into:

```text
prompts/00_beat_generator.md
governance/beat_review.md
prompts/02_chapter_brief.md
governance/chapter_brief_review.md
prompts/01_writer.md
prompts/03_revision.md
prompts/05_golden_three_review.md
```

### Character Action Logic

Implemented:

```text
prompts/00_character_action_logic.md
governance/character_action_review.md
```

Integrated into:

```text
prompts/02_chapter_brief.md
governance/chapter_brief_review.md
prompts/01_writer.md
prompts/00_story_bible_builder.md
```

### Anti-AI Novel Phrase Check

Implemented:

```text
governance/anti_ai_novel_phrase_check.md
```

Integrated into:

```text
prompts/01_writer.md
prompts/03_revision.md
prompts/05_golden_three_review.md
```

### Revision Modes

Updated:

```text
prompts/03_revision.md
```

Revision now supports:

```text
ordinary repair
opening structural rewrite
planning artifact revision
```

Opening-reader-entry failure no longer defaults to minimal line repair.

### Golden Three Review

Updated:

```text
prompts/05_golden_three_review.md
```

Golden-three review now includes:

- target reader recap test;
- type promise visibility;
- consequence chain from chapter 1 to chapter 3;
- conflict escalation from chapter 1 to chapter 3;
- concrete memory point check.

### Opening Failure Library

Implemented initial cases:

```text
failures/opening_reader_entry/brief_passed_reader_failed.md
failures/opening_reader_entry/setting_correct_but_unreadable.md
failures/opening_reader_entry/protagonist_as_job_function.md
failures/opening_reader_entry/too_many_mysteries_before_care.md
failures/opening_reader_entry/type_promise_unclear.md
failures/opening_reader_entry/hook_is_weird_not_compelling.md
```

## Partially Complete

### Story Bible Character Action Logic

`prompts/00_story_bible_builder.md` has been updated with a character action logic extension.

The story bible review gate still needs stronger checks for action logic.

Pending file:

```text
governance/story_bible_review.md
```

### Outline Type Contract Integration

`prompts/00_outline_generation.md` has been updated to require type contract and reader entry requirements.

The outline review gate still needs direct type-contract and reader-entry checks.

Pending file:

```text
governance/outline_review.md
```

## Pending

### Volume Planner Integration

Need to update:

```text
prompts/00_volume_planner.md
governance/volume_review.md
```

Required changes:

- add type contract as input;
- make volume reader promise explicit;
- require volume-level consequence and escalation structure;
- ensure first volume pays the primary genre promise.

### Story Bible Review Integration

Need to update:

```text
governance/story_bible_review.md
```

Required changes:

- recurring characters should include action logic;
- character entries should not remain static labels;
- unknown fields should remain `unknown`, not guessed.

### Outline Review Integration

Need to update:

```text
governance/outline_review.md
```

Required changes:

- outline must serve type contract;
- chapter 1 reader entry must be possible;
- false type promises should trigger REVISE.

### Regression Tests

Need to add formal regression test cases for:

```text
setting-correct but unreadable opening
protagonist as job function
unclear type promise
removable chapter beat
weird hook without stake
AI-summary ending
```

Recommended location:

```text
evals/reader_entry_regression.md
```

## Next Recommended Work

1. Update `governance/outline_review.md`.
2. Update `prompts/00_volume_planner.md` and `governance/volume_review.md`.
3. Update `governance/story_bible_review.md`.
4. Add `evals/reader_entry_regression.md`.
5. Run a new-fiction first-chapter pipeline test.
