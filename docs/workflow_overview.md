# Novel Creation Workflow Overview

This repository is a general AI-assisted novel creation workflow project.

The workflow is staged. Each stage produces an inspectable artifact before prose generation continues.

## Pipeline

```text
Project Scope
→ Outline Generation
→ Outline Review
→ Volume Planner
→ Volume Review
→ Beat Generator
→ Beat Review
→ Story Bible Builder
→ Story Bible Review
→ Chapter Brief
→ Brief Review
→ Chapter Draft
→ Chapter Review
→ Revision
→ Chapter State / Story Bible Update
→ Evaluation / Failure Library Update
```

## Stage 0: Project Scope

Purpose:

Define whether we are working on the reusable system or on a specific novel instance.

Generic system files live in:

```text
prompts/
governance/
docs/
evals/
failures/
```

Novel-specific files live in:

```text
novels/<novel_id>/wiki/
```

## Stage 1: Project Outline

Files:

```text
prompts/00_outline_generation.md
governance/outline_review.md
```

Purpose:

Define core conflict, opening imbalance, five turning points, relationship matrix, three-layer suspense, main genre promise, and drift risks.

Do not write prose at this stage.

## Stage 2: Volume Plan

Files:

```text
prompts/00_volume_planner.md
governance/volume_review.md
```

Purpose:

Turn the whole-story outline into a volume-level plan with start state, end state, midpoint turn, climax, reader reward, relationship changes, and drift controls.

## Stage 3: Chapter Beats

Files:

```text
prompts/00_beat_generator.md
governance/beat_review.md
```

Purpose:

Generate 10-chapter or approved-range beat tables.

Each beat must identify state change, relationship change, reader reward, main-system progress, cost, and hook.

## Stage 4: Story Bible

Files:

```text
prompts/00_story_bible_builder.md
governance/story_bible_review.md
```

Purpose:

Maintain canon-facing structured memory:

```text
confirmed facts
world / system rules
characters
relationships
timeline anchors
foreshadow register
objects / clues / resources
open questions
```

## Stage 5: Chapter Brief

Files:

```text
prompts/02_chapter_brief.md
governance/chapter_brief_review.md
```

Purpose:

Create a pre-draft gate for each chapter.

The brief must pass before prose drafting begins.

It must align with project outline, volume plan, chapter beat, story bible, reward engine, and contradiction risk.

## Stage 6: Chapter Draft

File:

```text
prompts/01_writer.md
```

Purpose:

Write prose only after outline, volume plan, beat table, story bible, and chapter brief exist.

The writer must not invent new canon facts without logging the need for updates.

## Stage 7: Chapter Review

File:

```text
prompts/04_review_hook.md
```

Purpose:

Check draft against approved brief, beat, volume, project outline, story bible, reward engine, contradiction checks, style banlist, and failure library.

Decision:

```text
ALLOW
REVISE
```

## Stage 8: Revision

File:

```text
prompts/03_revision.md
```

Purpose:

Repair failed drafts through minimal necessary change.

Do not regenerate everything unless the review says the structure itself failed.

## Stage 9: Evaluation

Files:

```text
evals/outline_eval.md
evals/chapter_eval.md
```

Purpose:

Batch-score outputs and compare versions.

The evaluation files do not replace human judgment. They make failures more visible and comparable.

## Stage 10: Failure Library

Directory:

```text
failures/
```

Purpose:

Store reusable failure cases and regression tests.

Known failures include:

```text
low-anchor terms
chronological log structure
direct emotion dialogue
repeated work-payoff loop
genre promise drift
character function loop
```

If a new draft repeats a known failure, mark REVISE unless the approved brief explicitly allows it for a controlled reason.

## Operating Principle

The system should not rely on one magical prompt.

It should rely on inspectable artifacts:

```text
outline
volume plan
beat table
story bible
chapter brief
chapter draft
review log
revision plan
chapter state
failure case
```

Each artifact reduces one class of failure.

## Current Priority

The next useful test is to create a new novel instance and run the complete pipeline from project outline to chapter 1 draft.
