# Novel Wiki

NovelWiki is a Wiki-centered human-AI collaborative novel creation system.

It is not a one-way generator that turns an outline into chapters. Its primary purpose is to help the author and AI share the same structured story memory while they discuss, decide, update, and only then generate content when needed.

The core asset of a project is the evolving story knowledge base: entities, events, time-aware states, relationships, rules, decisions, and approved narrative facts. Draft prose is an output of that knowledge base, not the center of the system.

## Core Principle

Each novel must have its own independent wiki.

The repository stores three kinds of material:

1. Global governance and reusable prompts.
2. Reusable reference settings for genre, authority, process, resource, object, space, social life, and rule-system boundaries.
3. Per-novel canonical wiki, drafts, narrative states, collaboration sessions, and update records.

The author remains the creative authority. The AI retrieves relevant wiki material, points out possible conflicts, proposes options, helps refine scenes and facts, and updates the wiki only when the user approves a change as canon.

## Current Workflow Entry

Use these files in this order:

```text
1. docs/current_execution_flow.md
2. docs/narrative_model.md
3. docs/workflow_layers.md
4. docs/interactive_writing_flow.md
5. docs/file_roles.md
```

`docs/current_execution_flow.md` is the short operating card. It explains the current collaboration loop and stop conditions.

`docs/narrative_model.md` defines the generic story-memory model: Entity, Event, Timepoint, State, Relationship, Session, Mutation, and Consistency Check.

`docs/workflow_layers.md` is the full execution-order index for setup, planning, discussion, generation, and wiki update.

`docs/interactive_writing_flow.md` defines the default human-AI collaboration protocol.

`docs/file_roles.md` explains what each file is responsible for.

`docs/emergent_plot_workflow.md` is conceptual background, not the execution authority.

## Default Collaboration Loop

The default formal loop is:

```text
retrieve relevant wiki knowledge
-> discuss the creative problem with the user
-> propose options and identify conflicts
-> user decides, redirects, or asks for revision
-> record approved decisions and mutations
-> generate prose or design output only when needed
-> sync only user-approved canon back into the wiki
```

Hard rule:

```text
No user-approved decision, no canon mutation.
```

This rule applies to characters, organizations, locations, rule systems, plot arcs, scenes, events, names, terms, relationships, and generated prose.

## Narrative Model

NovelWiki uses a light structured model and leaves most rich creative information in natural-language summaries.

### Entity

A persistent story object.

Typical entity types include character, organization, location, rule system, item, creature, social group, title, institution, and other reusable narrative objects.

### Event

A story fact anchored in time.

An event records who participated, when it happened, where it happened, what occurred, who or what was affected, what changed, and what earlier facts caused or enabled it.

### Timepoint

A named point or span in the story timeline. Timepoints allow the same entity to have different states at different moments.

### State

The state of an entity at a specific timepoint. A character, organization, location, rule system, or other entity may have multiple states across the story.

### Relationship

A link between entities, optionally time-aware. Relationships describe association, dependency, conflict, alliance, hierarchy, influence, ownership, kinship, obligation, or other story-relevant connections.

### Session

A human-AI collaboration record. Sessions preserve what was discussed, what the user decided, what alternatives were rejected, and which wiki mutations followed.

### Mutation

An approved change to the wiki. A mutation may create, update, supersede, or deprecate an entity, event, state, relationship, timepoint, or session note.

## Current Flow Types

### Standard Long-Form Flow

Use for ordinary long-form projects.

```text
Run new-novel setup
-> bootstrap the initial wiki
-> retrieve relevant narrative model records
-> discuss arc / chapter / scene direction with the user
-> record approved decisions
-> design or generate only the approved unit when needed
-> run consistency check
-> user canon approval
-> wiki sync
```

### Extended Arena Flow

Use when the story requires a large arena, multiple rule systems, complex social structures, broad historical pressure, or multi-stage escalation.

```text
Run extended arena setup
-> run new-novel setup
-> bootstrap the initial wiki
-> retrieve relevant narrative model records
-> discuss current pressure, actors, rules, and consequences
-> record approved decisions
-> design or generate only the approved unit when needed
-> run consistency check
-> user canon approval
-> wiki sync
```

### Fast Trial Mode

Fast Trial output is non-canon.

It may produce only:

```text
non-canon concept sketch
non-canon opening sketch
non-canon scene sketch
non-canon desire test draft
```

It must not be treated as an approved chapter draft. It must not create canonical story facts. It must not plan canon-dependent later units.

Formal drafting still requires wiki bootstrap and user-approved canon decisions.

## Name & Term Rule

A formal new novel must run Name & Term Gate before recurring names, key invented terms, organization names, location names, rule-system terms, project files, entity records, event records, or formal drafts rely on them.

Names and recurring terms are part of the story model. They must be grounded in in-world logic: period, region, class, family practice, job, registration system, nickname use, official wording, visible function, social role, or other story-specific cause.

Hard rule:

```text
No Name & Term Gate, no recurring invented name or term enters canon.
```

Use `prompts/00_name_term_gate.md` for the full Name & Term Gate format.

## Wiki Bootstrap Rule

A formal new novel must create or update its initial wiki before any formal canon-dependent draft.

Required prompt:

```text
prompts/00_wiki_bootstrap.md
```

Recommended initial wiki files:

```text
novels/<novel_id>/wiki/project.md
novels/<novel_id>/wiki/base_settings.md
novels/<novel_id>/wiki/style.md
novels/<novel_id>/wiki/name_registry.md
novels/<novel_id>/wiki/timeline.md
novels/<novel_id>/wiki/relationships.md
novels/<novel_id>/wiki/foreshadowing.md
novels/<novel_id>/wiki/entities/
novels/<novel_id>/wiki/events/
novels/<novel_id>/wiki/states/
novels/<novel_id>/wiki/sessions/
novels/<novel_id>/wiki/mutations/
```

Add specialized files only when a project needs them. Do not force every project into a large schema before the story requires it.

Hard rule:

```text
No wiki bootstrap, no formal canon-dependent draft.
```

## Wiki Sync Rule

Every approved canon change must be synchronized into the novel wiki before the next canon-dependent discussion, scene design, or draft.

Required prompt:

```text
prompts/05_wiki_sync_after_chapter.md
```

For approved formal chapters, update the relevant chapter state or event records.

For approved partial scenes, design decisions, character changes, organization changes, location changes, rule-system changes, relationship changes, or timeline changes, update the relevant Entity, Event, State, Relationship, Session, or Mutation records.

Hard rule:

```text
User-approved canon -> wiki sync -> next canon-dependent step.
```

`prompts/06_chapter_state_update.md` is deprecated. Do not use it in the current workflow.

## Non-Negotiable Stop Conditions

Stop if any are true:

1. Fast Trial is being mistaken for canon.
2. Genre mode is unclear.
3. Genre operating model is missing or too vague.
4. Initial wiki bootstrap is missing.
5. Required base settings for the active novel are missing.
6. Name & Term Gate is missing for recurring names or invented terms.
7. Relevant wiki material has not been retrieved before discussion.
8. A proposed change affects existing canon but no conflict check has been made.
9. A discussion decision is being treated as canon before user approval.
10. A draft changes canon without explicit user approval.
11. A scene or chapter depends on facts stored only in chat memory rather than the wiki.
12. Time-aware state is needed but the relevant timepoint or state record is missing.
13. A major entity acts with knowledge, ability, authority, or motivation not supported by its current state.
14. A generated unit replaces story action with abstract explanation, interface text, report text, or summary-only prose.

Do not plan the next canon-dependent unit if any are true:

1. Approved changes were not synchronized.
2. New confirmed entity, event, state, relationship, name, or term facts were not recorded.
3. Important consequences were not recorded as Event or State changes.
4. The next unit would rely on chat memory instead of wiki state.
5. The previous generated unit was not explicitly approved as canon.

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
  narrative_model.md
  workflow_layers.md
  interactive_writing_flow.md
  file_roles.md
  emergent_plot_workflow.md
  backups/

prompts/
  00_*.md   setup / operating model / name and term gate / wiki bootstrap / planning prompts
  01_*.md   opening and drafting prompts
  02_*.md   chapter / scene prompts
  04_*.md   consistency and targeted review hooks
  05_*.md   wiki sync / canon update prompts

governance/
  wiki retrieval and write rules
  base setting reviews
  reality / object / plot / growth / voice / AI-expression checks
  review priority and conflict resolution

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
      entities/
      events/
      states/
      sessions/
      mutations/
      chapter_states/
```