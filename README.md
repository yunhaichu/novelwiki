# Novel Wiki

This repository is the canonical memory and governance store for long-form novel creation with ChatGPT as the primary writer.

## Core Principle

Each novel must have its own independent wiki.

The repository stores two kinds of material:

1. Global governance and reusable prompts.
2. Per-novel canonical wiki, drafts, chapter states, and update records.

ChatGPT is responsible for writing, planning, revision, and generating wiki update drafts. The wiki is responsible for long-term memory. The user remains the final approver.

## Repository Layout

```text
prompts/
  00_master_workflow.md
  01_writer.md
  02_wiki_update_draft.md

governance/
  workflow.md
  wiki_write_rules.md

novels/
  _template/
    README.md
    wiki/
      project.md
      style.md
      name_registry.md
      timeline.md
      relationships.md
      foreshadowing.md
      characters/
        _template.md
      world/
        rules.md
        locations.md
        items.md
      chapter_states/
        _template.md
    drafts/
      README.md
```

## Rule

Do not mix multiple novels in one wiki.

A new novel must be created under:

```text
novels/<novel_id>/
```

Each novel has its own:

- project direction
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
