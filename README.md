# Novel Wiki

This repository is the canonical memory, reference-setting, and governance store for long-form Chinese webnovel creation with ChatGPT as the primary writer.

## Core Principle

Each novel must have its own independent wiki.

The repository stores three kinds of material:

1. Global governance and reusable prompts.
2. Reusable reference settings for genre, authority, process, resource, object, space, social life, and power-system boundaries.
3. Per-novel canonical wiki, drafts, chapter states, and update records.

ChatGPT is responsible for planning, base-setting construction, name-and-term gate checking, writing, revision, review assistance, wiki bootstrap, and wiki sync after approved formal chapters. The wiki is responsible for long-term memory. The user remains the final approver.

## Current Workflow Entry

Use these files in this order:

```text
1. docs/current_execution_flow.md
2. docs/workflow_layers.md
3. docs/file_roles.md
```

`docs/current_execution_flow.md` is a short path-selection card. It tells you whether to use the standard flow, macro modern-to-cosmic flow, or non-canon fast trial mode.

`docs/workflow_layers.md` is the authoritative full execution-order index.

`docs/file_roles.md` explains what each file is responsible for.

`docs/emergent_plot_workflow.md` is conceptual background, not the execution authority.

## Current Flow Types

### Standard Long-Form Flow

Use for ordinary long-form projects: xianxia, urban fantasy, cyberpunk, single-world fantasy, standard rebirth, or other non-cosmic stories.

```text
Run Layer 1B New Novel Setup
-> Run Layer 2 Actor Setup
-> Run Layer 3 Volume / Arc Planning
-> Run Layer 4 Chapter Trend + Hook/Payoff Convergence
-> Run Layer 5 Reader Entry / Opening Control when needed
-> Run Layer 6 Scene Design
-> Run Layer 7 Drafting
-> Run Layer 8 Review
-> Run Layer 9 Wiki Sync
```

### Macro Modern-To-Cosmic Flow

Use when the target story has modern Earth, cosmic civilizations, multiverse stages, cultivation + technology + magic, or civilization war.

```text
Run Layer 1A Macro Modern-To-Cosmic Setup
-> Run Layer 1B New Novel Setup
-> Run Layer 2 Actor Setup
-> Run Layer 3 Volume / Arc Planning
-> Run Layer 4 Chapter Trend + Hook/Payoff Convergence
-> Run Layer 5 Modern-To-Cosmic Opening / Reader Entry
-> Run Layer 6 Scene Design
-> Run Layer 7 Drafting
-> Run Layer 8 Review
-> Run Layer 9 Wiki Sync
```

### Fast Trial Mode

Fast Trial output is non-canon.

It may produce only:

```text
non-canon opening sketch
non-canon chapter-one outline
non-canon desire test draft
```

It must not be treated as an approved chapter draft. It must not create chapter state. It must not plan chapter two.

Formal drafting still requires Layer 1B and Wiki Bootstrap.

## Name & Term Gate Rule

A formal new novel must run Name & Term Gate before writing protagonist names, organization names, city names, key terms, `project.md`, character files, organization files, world files, or chapter drafts.

Names and recurring terms are part of the world model. They must be grounded in period, region, class, family practice, job, registration system, nickname use, official wording, visible function, or other in-world logic.

Hard rule:

```text
No Name & Term Gate, no project file.
```

Use `prompts/00_name_term_gate.md` for the full Name & Term Gate format.

## Wiki Bootstrap Rule

A formal new novel must create or update its initial wiki before any formal chapter draft.

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
novels/<novel_id>/wiki/timeline.md
novels/<novel_id>/wiki/relationships.md
novels/<novel_id>/wiki/foreshadowing.md
```

Add character, organization, and world files as needed before those actors appear in chapter planning.

Hard rule:

```text
No wiki bootstrap, no formal draft.
```

## Wiki Sync Rule

Every approved formal chapter must be synchronized into the novel wiki before the next formal chapter is planned.

Required prompt:

```text
prompts/05_wiki_sync_after_chapter.md
```

Always create or update:

```text
novels/<novel_id>/wiki/chapter_states/chapter_<number>.md
```

Update character, organization, world, growth, timeline, relationship, foreshadowing, style, name, and term files only when approved prose confirms new facts.

Hard rule:

```text
Approved formal chapter -> wiki sync -> next chapter.
```

`prompts/06_chapter_state_update.md` is deprecated. Do not use it in the current workflow.

## Non-Negotiable Gates

Do not formal draft if any of these are unresolved:

1. Fast Trial is being mistaken for canon draft.
2. Macro story lacks cosmic civilization arena.
3. Earth-entry story lacks Earth civilization value.
4. Multi-system story lacks unified power logic.
5. Modern-entry story lacks modern Chinese entry bridge.
6. Genre mode is unclear.
7. Genre operating model is missing or too vague.
8. Irreversible trend anchor is missing or weak.
9. Reader Hook / Payoff Ladder is missing for commercial long-form execution.
10. Name & Term Gate is missing or failed.
11. Initial wiki bootstrap is missing.
12. Base settings for the active novel are missing.
13. Reality-causal preflight says the core event is unnatural.
14. Chapter trend convergence is missing.
15. Important chapter has no concrete reader hook/payoff.
16. Actor cognition boundary is missing for an important actor who drives chapter logic.
17. The protagonist has no active growth stage toward final form.
18. The chapter has no usable protagonist gain when gain is required.
19. The main scene has no convergence point.
20. The key object has no natural function.
21. Unapproved invented terms appear where ordinary description would be clearer.
22. The story relies on system/report/log/status change as climax.

Do not plan the next formal chapter if any of these are unresolved:

1. Approved chapter has no current-format chapter state file.
2. World / civilization trend progress was not recorded.
3. Earth status progress was not recorded when relevant.
4. Protagonist final-form progress was not recorded.
5. Reader hook/payoff delivered was not recorded for an important chapter.
6. Reader reward delivered was not recorded when relevant.
7. New confirmed character / organization / world facts were not synchronized.
8. Newly approved or rejected terms were not synchronized into the name registry.
9. Next chapter constraints are missing.
10. The next chapter would need to rely on chat memory rather than wiki state.

## Repository Layout

```text
reference_settings/
  README.md
  usage_contract.md
  index.json
  genre_common/
  power_system_common/

docs/
  current_execution_flow.md
  workflow_layers.md
  file_roles.md
  emergent_plot_workflow.md
  backups/

prompts/
  00_*.md   setup / operating model / name and term gate / wiki bootstrap / planning prompts
  01_*.md   opening and drafting prompts
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

Legacy chapter state files may predate the current template. They should not block new workflow tests unless the user explicitly resumes that novel.

## Novel Rule

Do not mix multiple novels in one wiki.

A new formal novel must be created under:

```text
novels/<novel_id>/
```

Each formal novel has its own:

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
- chapter states.
