# Narrative Model

NovelWiki uses a light structured model for human-AI collaborative novel creation.

The model is intentionally not a rigid database schema. Most creative information remains in natural-language summaries because novels are text-first artifacts and most author-AI work happens through discussion. Structure exists to make retrieval, consistency checking, time tracking, and wiki mutation reliable.

## Design Principle

Use structure for what must be indexed.

Use prose for what must be understood.

A record should therefore keep only a small number of mandatory fields and a rich natural-language summary.

## Core Records

### Entity

An Entity is a persistent story object.

Typical entity types include:

- character
- organization
- location
- rule system
- item
- creature
- social group
- title or role
- institution
- other reusable narrative object

Minimal fields:

```yaml
id:
type:
name:
summary:
```

Optional fields:

```yaml
aliases:
related_entities:
source_sessions:
notes:
```

The summary should describe the entity in natural language. Do not split every trait, motive, habit, tone, resource, or function into separate fields unless the project repeatedly needs to query that field.

### Timepoint

A Timepoint is a named point or span in story time.

Minimal fields:

```yaml
id:
label:
summary:
```

Optional fields:

```yaml
order:
parent_timepoint:
related_events:
notes:
```

Timepoints are needed because the same entity may have different states at different moments.

### State

A State records what an entity is like at a specific timepoint.

Minimal fields:

```yaml
id:
entity_id:
timepoint_id:
summary:
```

Optional fields:

```yaml
related_events:
related_entities:
source_sessions:
notes:
```

Use State when a change matters for later design or generation. Do not create a state record for every minor line-level detail.

### Relationship

A Relationship records a link between entities.

Minimal fields:

```yaml
id:
source_entity_id:
target_entity_id:
relationship_type:
summary:
```

Optional fields:

```yaml
timepoint_id:
related_events:
source_sessions:
notes:
```

Relationships may describe conflict, trust, hierarchy, debt, kinship, ownership, influence, obligation, alliance, dependency, rivalry, secrecy, or any other connection that affects story logic.

### Event

An Event is a story fact anchored in time.

It answers the core narrative questions:

```text
who
when
where
did what
affected whom
changed what
caused what
```

Minimal fields:

```yaml
id:
timepoint_id:
summary:
```

Recommended indexed fields:

```yaml
participants:
location_id:
affected_entities:
state_changes:
caused_by:
causes:
source_sessions:
```

The summary should describe the event in natural language. The indexed fields exist so the AI can retrieve related facts and avoid contradiction.

### Session

A Session records a human-AI collaboration discussion.

Minimal fields:

```yaml
id:
summary:
decisions:
```

Optional fields:

```yaml
related_entities:
related_events:
related_timepoints:
accepted_options:
rejected_options:
mutations:
notes:
```

A session is not canon by itself. It becomes canon only through approved mutations.

### Mutation

A Mutation records an approved wiki change.

Minimal fields:

```yaml
id:
operation:
target_record:
summary:
source_session:
```

Optional fields:

```yaml
before:
after:
reason:
supersedes:
notes:
```

Operations may include:

```text
create
update
supersede
deprecate
merge
split
```

A mutation exists to preserve why and when the wiki changed. It also gives the author a path to review or undo a design direction later.

## Retrieval Rule

Before discussing or generating a canon-dependent unit, retrieve the relevant records:

1. Entities directly involved.
2. Current states for the relevant timepoint.
3. Recent or causal events.
4. Important relationships.
5. Applicable rule-system records.
6. Relevant prior sessions and mutations when the design question depends on previous user decisions.

The assistant should summarize retrieved material before proposing changes when that material constrains the current decision.

## Mutation Rule

Do not mutate the wiki just because an idea is useful.

Mutation requires explicit user approval.

Approved changes should update the smallest sufficient set of records. If a single Event can record the change, do not scatter the same fact across many files. If an Entity or State summary must change, update it and reference the Event or Session that caused the change.

## Consistency Check

Consistency Check is not a heavy review layer. It is a constraint check before canon mutation or canon-dependent generation.

Check whether the proposed change contradicts:

- existing entity summaries;
- time-aware states;
- established relationships;
- prior events;
- rule-system boundaries;
- approved names and terms;
- user-approved session decisions.

If a conflict appears, stop and identify:

```text
conflicting record
proposed change
smallest safe resolution
whether user decision is needed
```

## What This Model Avoids

Do not turn the wiki into a field-heavy database before the story needs it.

Avoid forcing every character, organization, location, or scene into dozens of narrow fields. Prefer a compact set of indexed fields plus a clear summary.

Do not treat AI suggestions as canon.

Do not rely on chat memory for durable facts.

Do not write concrete project-specific story content into framework documentation.