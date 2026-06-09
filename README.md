# Novel Wiki

This repository is the canonical memory, reference-setting, and governance store for long-form Chinese webnovel creation with ChatGPT as the primary writer.

## Core Principle

Each novel must have its own independent wiki.

The repository stores three kinds of material:

1. Global governance and reusable prompts.
2. Reusable reference settings for genre, authority, process, resource, object, space, social life, and power-system boundaries.
3. Per-novel canonical wiki, drafts, chapter states, and update records.

ChatGPT is responsible for planning, base-setting construction, name-gate checking, writing, revision, review assistance, wiki bootstrap, and wiki sync after approved chapters. The wiki is responsible for long-term memory. The user remains the final approver.

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
Layer 1: New Novel Setup + Name Gate + Wiki Bootstrap
Layer 2: Actor Model Setup
Layer 3: Volume / Arc Planning
Layer 4: Chapter Preflight
Layer 5: Reader Entry / Opening Control
Layer 6: Scene Design
Layer 7: Drafting
Layer 8: Review / Revision
Layer 9: Wiki Sync / Canon Update
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
-> Name Gate
-> wiki bootstrap
-> volume / chapter planning
-> scene convergence
-> draft
-> review
-> wiki sync / canon update
```

For a normal later chapter:

```text
read current novel wiki
-> volume / arc state check
-> reality-causal preflight
-> emergent chapter design
-> scene convergence
-> draft
-> review
-> wiki sync / canon update
```

## Name Gate Rule

A new novel must run Name Gate before writing protagonist names, organization names, city names, key terms, `project.md`, character files, organization files, or chapter drafts.

Names are part of the world model. They must be grounded in period, region, class, family practice, job, registration system, nickname use, corporate / state / platform naming rules, or other in-world naming logic.

High-risk model-default names and polished genre-neutral names must be rejected unless the user explicitly approves them or the setting gives a strong reason.

Hard rule:

```text
No Name Gate, no project file.
```

Use `prompts/00_wiki_bootstrap.md` for the full Name Gate format and warning list.

## Wiki Bootstrap Rule

A new novel must create or update its initial wiki before any chapter draft.

Required prompt:

```text
prompts/00_wiki_bootstrap.md
```

Required initial wiki files:

```text
novels/<novel_id>/wiki/project.md
novels/<novel_id>/wiki/base_settings.md
novels/<novel_id>/wiki/style.md
novels/<novel_id>/wiki/name_registry.md
novels/<novel_id>/wiki/protagonist_growth.md
```

Add character, organization, and world files as needed before those actors appear in chapter planning.

Hard rule:

```text
No wiki bootstrap, no draft.
```

## Wiki Sync Rule

Every approved chapter must be synchronized into the novel wiki before the next chapter is planned.

Required prompt:

```text
prompts/05_wiki_sync_after_chapter.md
```

Always create or update:

```text
novels/<novel_id>/wiki/chapter_states/chapter_<number>.md
```

Update character, organization, world, growth, timeline, relationship, foreshadowing, style, and name files only when approved prose confirms new facts.

Hard rule:

```text
Approved chapter -> wiki sync -> next chapter.
```

## Non-Negotiable Gates

Do not draft if any of these are unresolved:

1. Genre mode is unclear.
2. Genre operating model is missing or too vague.
3. Name Gate is missing or failed.
4. Initial wiki bootstrap is missing.
5. Base settings for the active novel are missing.
6. Reality-causal preflight says the core event is unnatural.
7. The protagonist has no active growth stage.
8. The chapter has no usable protagonist gain.
9. The main scene has no convergence point.
10. The key object has no natural function.
11. The story relies on system/report/log/status change as climax.

Do not plan the next chapter if any of these are unresolved:

1. Approved chapter has no chapter state file.
2. New confirmed character / organization / world facts were not synchronized.
3. Next chapter constraints are missing.
4. The next chapter would need to rely on chat memory rather than wiki state.

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
  00_*.md   setup / operating model / name gate / wiki bootstrap / planning prompts
  01_*.md   drafting prompts
  02_*.md   chapter / scene prompts
  04_*.md   review hooks
  05_*.md   wiki sync / canon update prompts

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
      organizations/
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

Character names should be grounded in world, class, family, system, job, and usage context.

Each novel should maintain its own `wiki/name_registry.md` to avoid repeated model-favored names and to keep approved names stable.

The name registry must record both approved names and rejected / avoided names with reasons.

## Wiki Safety

Only confirmed content from final approved chapters should be written into the wiki.

Do not write speculation, inferred secrets, temporary actions, reference candidates, or unconfirmed explanations as canon.

## Restructure Safety

Before deleting, merging, or renaming workflow files, check:

```text
docs/backups/workflow_snapshot_2026-06-09.md
```

This file records the restore anchor for the pre-cleanup workflow state.
