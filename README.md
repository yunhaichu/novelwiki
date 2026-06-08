# Novel Wiki

This repository is the canonical memory and governance store for long-form novel creation with ChatGPT as the primary writer.

## Core Principle

Each novel must have its own independent wiki.

The repository stores two kinds of material:

1. Global governance and reusable prompts.
2. Per-novel canonical wiki, drafts, chapter states, and update records.

ChatGPT is responsible for writing, planning, revision, review assistance, and generating wiki update drafts. The wiki is responsible for long-term memory. The user remains the final approver.

## Current Development Plan

The current canonical development plan is:

```text
docs/development_plan.md
```

The active upgrade priority is to add reader-entry, type-contract, consequence-chain, and conflict-escalation gates to the existing staged workflow.

## Repository Layout

```text
docs/
  project_scope.md
  workflow_overview.md
  development_plan.md

prompts/
  00_outline_generation.md
  00_volume_planner.md
  00_beat_generator.md
  00_story_bible_builder.md
  01_writer.md
  02_chapter_brief.md
  03_revision.md
  04_review_hook.md
  05_golden_three_review.md

governance/
  outline_review.md
  volume_review.md
  beat_review.md
  story_bible_review.md
  chapter_brief_review.md
  wiki_retrieval_rules.md
  wiki_write_rules.md
  reward_engine.md
  longform_ai_inertia_check.md
  low_anchor_phrase_check.md
  anti_ai_taste_check.md
  contradiction_check.md
  review_checklist.md

failures/
  reusable failure cases and regression tests

evals/
  evaluation rubrics and batch comparison tools

novels/
  <novel_id>/
    wiki/
    drafts/
```

Planned workflow-upgrade files will be added under `prompts/`, `governance/`, and `failures/` according to `docs/development_plan.md`.

## Rule

Do not mix multiple novels in one wiki.

A new novel must be created under:

```text
novels/<novel_id>/
```

Each novel has its own:

- project direction
- type contract if implemented
- style rules
- name registry
- character files
- world rules
- timeline
- relationship state
- foreshadowing state
- chapter states
- drafts

## Name Rule

Character names should be simple, natural, and easy to remember.

Each novel should maintain its own `wiki/name_registry.md` to avoid repeated model-favored names and to keep approved names stable.

## Wiki Safety

Only confirmed content from final approved chapters should be written into the wiki.

Do not write speculation, inferred secrets, temporary actions, or unconfirmed explanations as canon.

## Workflow Safety

Reader entry is a hard quality gate for openings.

A draft that follows the brief but cannot be understood by a first-time target reader should be marked `REVISE`, not `ALLOW`.
