# Novel Wiki

This repository is the canonical memory, reference-setting, and governance store for long-form Chinese webnovel creation with ChatGPT as the primary writer.

## Core Principle

Each novel must have its own independent wiki.

The repository stores three kinds of material:

1. Global governance and reusable prompts.
2. Reusable reference settings for genre, authority, process, resource, object, space, social life, and power-system boundaries.
3. Per-novel canonical wiki, drafts, chapter states, and update records.

ChatGPT is responsible for planning, base-setting construction, writing, revision, review assistance, and generating wiki update drafts. The wiki is responsible for long-term memory. The user remains the final approver.

## System Flow

```text
project scope
-> type contract / novel spine
-> reference settings selection
-> novel-specific base settings
-> reader entry gate
-> opening chapter brief or normal chapter brief
-> chapter draft
-> chapter review
-> revision if needed
-> canon update
```

The base settings step must happen before reader-entry and chapter drafting.

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

prompts/
  00_novel_spine.md
  00_volume_state_plan.md
  00_chapter_pressure_card.md
  00_multi_agent_scene_simulation.md
  00_base_settings_builder.md
  01_scene_log_to_draft.md
  01_writer.md
  04_review_hook.md

governance/
  wiki_retrieval_rules.md
  wiki_write_rules.md
  base_settings_review.md
  review_checklist.md
  anti_ai_taste_check.md
  ai_taste_language_grounding.md
  batch_commit_workflow.md

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

- project direction
- base settings
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

## Base Settings Rule

Before prose drafting, each active novel should have:

```text
novels/<novel_id>/wiki/base_settings.md
```

This file defines only the opening and first-volume setting boundaries needed for stable writing.

It should cover:

- genre foundation
- identity and authority rules
- organization and process rules
- resource and object rules
- space and location rules
- social life and language rules
- power / anomaly / goldfinger rules if applicable
- knowledge boundaries
- forbidden setting moves
- pending setting gaps

## Name Rule

Character names should be simple, natural, and easy to remember.

Each novel should maintain its own `wiki/name_registry.md` to avoid repeated model-favored names and to keep approved names stable.

## Wiki Safety

Only confirmed content from final approved chapters should be written into the wiki.

Do not write speculation, inferred secrets, temporary actions, reference candidates, or unconfirmed explanations as canon.
