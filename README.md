# Novel Wiki

This repository is the canonical memory, reference-setting, and governance store for long-form Chinese webnovel creation with ChatGPT as the primary writer.

## Core Principle

Each novel must have its own independent wiki.

The repository stores three kinds of material:

1. Global governance and reusable prompts.
2. Reusable reference settings for genre, authority, process, resource, object, space, social life, and power-system boundaries.
3. Per-novel canonical wiki, drafts, chapter states, and update records.

ChatGPT is responsible for planning, base-setting construction, writing, revision, review assistance, and generating wiki update drafts. The wiki is responsible for long-term memory. The user remains the final approver.

## Current Workflow Entry

Use these two files as the current workflow entry:

```text
docs/workflow_layers.md
docs/file_roles.md
```

`docs/workflow_layers.md` tells you when to run each layer.

`docs/file_roles.md` tells you what each file is responsible for.

`docs/emergent_plot_workflow.md` is the conceptual overview, not the only execution checklist.

## Layered System Flow

Do not run every prompt for every chapter.

The current workflow is organized by layer:

```text
Layer 1: New Novel Setup
Layer 2: Actor Model Setup
Layer 3: Volume / Arc Planning
Layer 4: Chapter Preflight
Layer 5: Reader Entry / Opening Control
Layer 6: Scene Design
Layer 7: Drafting
Layer 8: Review / Revision
Layer 9: Canon Update
```

For a new novel:

```text
project scope / type promise
-> genre mode contract
-> genre operating model / reality-causal preflight
-> base settings
-> major conflict engine
-> dramatic arena
-> protagonist growth track
-> organization and character behavior models
-> volume / chapter planning
-> scene convergence
-> draft
-> review
-> canon update
```

For a normal later chapter:

```text
volume / arc state check
-> reality-causal preflight
-> emergent chapter design
-> scene convergence
-> draft
-> review
-> canon update
```

## Non-Negotiable Gates

Do not draft if any of these are unresolved:

1. Genre mode is unclear.
2. Base settings for the active novel are missing.
3. Reality-causal preflight says the core event is unnatural.
4. The protagonist has no active growth stage.
5. The chapter has no usable protagonist gain.
6. The main scene has no convergence point.
7. The key object has no natural function.
8. The story relies on system/report/log/status change as climax.

## Repository Layout

```text
reference_settings/
  README.md
  usage_contract.md
  index.json
  genre_common/
    modern_common.md
    apocalypse_common.md
    xianxia_common.md
    sci_fi_cyber_common.md
    generic_common.md
  power_system_common/
    base_laws.md

docs/
  workflow_layers.md
  file_roles.md
  emergent_plot_workflow.md
  backups/

prompts/
  00_*.md   setup / operating model / planning prompts
  01_*.md   drafting prompts
  02_*.md   chapter / scene prompts
  04_*.md   review hooks
  05_*.md   canon update prompts if present

governance/
  wiki retrieval and write rules
  base setting reviews
  reality / object / plot / growth / voice / AI-expression reviews

novels/
  <novel_id>/
    wiki/
      project.md
      base_settings.md
      style.md
      name_registry.md
      timeline.md
      relationships.md
      foreshadowing.md
      protagonist_growth.md
      characters/
      world/
      chapter_states/
    drafts/
```

## Reference Settings Rule

Files under `reference_settings/` are reusable references, not canon.

They may provide boundaries for identity, authority, process, resource, object, space, social life, language register, and power or anomaly rules. They must not be copied into a novel wiki as confirmed facts.

A reference-setting idea becomes usable canon only after it is accepted into the current novel's own `wiki/base_settings.md` or another approved canon file.

Existing test novels under `novels/` are regression examples and workflow tests. They must not define global system direction.

## Novel Rule

Do not mix multiple novels in one wiki.

A new novel must be created under:

```text
novels/<novel_id>/
```

Each novel has its own:

- project direction;
- genre mode contract;
- genre operating model or equivalent reality model;
- base settings;
- protagonist growth track;
- style rules;
- name registry;
- character files;
- organization files;
- world rules;
- timeline;
- relationship state;
- foreshadowing state;
- chapter states;
- drafts.

## Base Settings Rule

Before prose drafting, each active novel should have:

```text
novels/<novel_id>/wiki/base_settings.md
```

This file defines only the opening and first-volume setting boundaries needed for stable writing.

It should cover:

- genre foundation;
- identity and authority rules;
- organization and process rules;
- resource and object rules;
- space and location rules;
- social life and language rules;
- power / anomaly / goldfinger rules if applicable;
- knowledge boundaries;
- forbidden setting moves;
- pending setting gaps.

## Name Rule

Character names should be simple, natural, and easy to remember.

Each novel should maintain its own `wiki/name_registry.md` to avoid repeated model-favored names and to keep approved names stable.

## Wiki Safety

Only confirmed content from final approved chapters should be written into the wiki.

Do not write speculation, inferred secrets, temporary actions, reference candidates, or unconfirmed explanations as canon.

## Restructure Safety

Before deleting, merging, or renaming workflow files, check:

```text
docs/backups/workflow_snapshot_2026-06-09.md
```

This file records the restore anchor for the pre-cleanup workflow state.
