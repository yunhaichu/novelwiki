# Wiki Sync After Approved Canon Prompt

Use this prompt immediately after the user approves a canon change and before planning the next canon-dependent discussion, design, or generated unit.

The purpose is to keep the per-novel wiki synchronized with approved canon so later work reads the wiki rather than relying on chat memory.

Fast Trial sketches are non-canon and must not use this prompt unless the user explicitly promotes a trial element into canon.

## Core Principle

```text
User-approved canon -> wiki sync -> next canon-dependent step
```

Do not plan, discuss, or generate the next canon-dependent unit until relevant wiki updates are written or explicitly rejected by the user.

## Required Inputs

Read:

- the approved canon source;
- the user approval statement or instruction;
- current `project.md`;
- current `base_settings.md`;
- current `style.md`;
- current `name_registry.md`;
- relevant Entity records;
- relevant Timepoint records;
- relevant State records;
- relevant Relationship records;
- relevant Event records;
- relevant Session / Mutation records when the approved change depends on previous design decisions;
- `docs/narrative_model.md`;
- `governance/wiki_write_rules.md`.

If the approved source is a chapter, also read the previous chapter state if present.

If the approved source is a partial scene, event design, character decision, organization decision, location decision, rule-system decision, or relationship decision, read only the relevant records. Do not force a chapter-state update when no chapter has been approved.

## Output Targets

Update the smallest sufficient set of wiki records.

Possible targets:

```text
novels/<novel_id>/wiki/entities/<entity_id>.md
novels/<novel_id>/wiki/events/<event_id>.md
novels/<novel_id>/wiki/states/<state_id>.md
novels/<novel_id>/wiki/sessions/<session_id>.md
novels/<novel_id>/wiki/mutations/<mutation_id>.md
novels/<novel_id>/wiki/timeline.md
novels/<novel_id>/wiki/relationships.md
novels/<novel_id>/wiki/foreshadowing.md
novels/<novel_id>/wiki/name_registry.md
novels/<novel_id>/wiki/style.md
novels/<novel_id>/wiki/chapter_states/chapter_<number>.md
```

Only update `base_settings.md` when the approved canon establishes a durable world rule, not a one-time event.

Do not scatter the same fact across many files unless later retrieval genuinely needs those indexes.

## Canon Update Rules

Write only confirmed facts from approved canon.

Every wiki entry must include a source. Do not write any fact without attribution.

Required format for each confirmed entry:

```text
Fact: <the confirmed fact>
Source: <approved source>
Status: confirmed / claim / observation / inference / unknown
```

If no approved source exists for an entry, it must not be written to the wiki.

Do not write:

- speculation;
- inferred secrets;
- reader-only interpretation;
- temporary options not chosen;
- possible future twists;
- reference-setting ideas not used in approved canon;
- model assumptions;
- any fact without a source.

Distinguish:

- stable trait vs one-time action;
- environment-modulated behavior vs durable change;
- organization rule vs local agent action;
- public status vs private knowledge;
- known fact vs unresolved question;
- foreshadowing object vs ordinary detail;
- rule-system movement vs worldbuilding exposition;
- reader hook / payoff vs confirmed canon;
- reader debt vs unresolved question;
- pressure clock vs completed event;
- repetition risk vs style preference.

## Event Record Rule

When an approved fact matters later, prefer recording it as an Event.

An Event should answer:

```text
who participated
when it happened
where it happened
what occurred
who or what was affected
what changed
what caused or enabled it
what it caused or may force next
```

Do not create an Event for every minor line. Create one when the fact may affect later retrieval, state, relationship, timeline, rule logic, or reader memory.

## Time-Aware State Rule

When an entity changes in a way that matters later, update or create a State record.

A State should identify:

```text
entity
timepoint
current condition
current knowledge
current access / authority / resource if relevant
current relationship position if relevant
source event or session
```

Do not overwrite a previous state if the old state remains true at an earlier timepoint. Add a new state or supersede the old one with source attribution.

## Relationship Rule

When an approved canon change affects a relationship, update the relevant Relationship record.

A Relationship update should identify:

```text
source entity
target entity
relationship type
current condition
what changed
source event or session
```

Do not turn a temporary interaction into a durable relationship change unless the approved source supports it.

## Session And Mutation Rule

If the approved change came from human-AI discussion, create or update a Session record when traceability is useful.

A Session should record:

```text
what was discussed
relevant wiki records
accepted decisions
rejected options when important
approved mutations
unresolved questions
```

A Mutation should record:

```text
operation
target record
summary of change
source session or approved source
reason
```

## Reader Memory Rule

For important generated units, record reader-facing obligations when they affect later structure.

Track:

```text
prior reader debt paid or partially paid
prior reader debt carried forward
new reader debt created
pressure that must force later action
repetition risk that should be avoided or upgraded
```

Reader debt is the set of specific questions, promises, pressures, and emotional needs that the story has created but has not yet paid off. It is not the same as any unresolved question.

## Chapter State Rule

If the approved canon source is a full formal chapter, create or update:

```text
novels/<novel_id>/wiki/chapter_states/chapter_<number>.md
```

A chapter state should include only fields relevant to the chapter and project:

```text
chapter title:
chapter function:
confirmed events:
affected entities:
state changes:
relationship changes:
rule-system changes if any:
reader hook / payoff delivered:
reader debt:
pressure clock:
repetition risk:
unresolved questions:
next unit constraints:
useful next attractor:
```

Do not force project-specific fields into every chapter state. If a field is irrelevant, write `Not relevant for this project / chapter.`

## Output Format

```text
# Wiki Sync After Approved Canon

Novel ID:
Approved source:
Approved source type: setup / discussion decision / partial scene / full chapter / entity update / event design / prose unit / other
User approval source:
Sync decision: ALLOW / REVISE

## 1. Records Read

- ...

## 2. Canon Facts Confirmed

- Fact:
  Source:
  Status:

## 3. Event Updates

Event:
Path:
Confirmed update:
Participants:
Timepoint:
Location:
Affected entities:
State changes:
Caused by:
Causes:
Should update file? yes / no

## 4. Entity / State Updates

Entity:
State path:
Confirmed update:
Timepoint:
Type: stable description / one-time action / knowledge state / access state / resource state / relationship state / status state / other
Should update file? yes / no

## 5. Relationship Updates

Relationship:
Path:
Confirmed update:
Timepoint if relevant:
Should update file? yes / no

## 6. Session / Mutation Updates

Session:
Mutation:
Approved decision:
Rejected options if important:
Target records:
Should update file? yes / no

## 7. Name / Term / Style Updates

Name registry update:
Style update:
Term update:

## 8. Reader Memory Updates

Reader debt paid or partially paid:
Reader debt carried forward:
New reader debt created:
Pressure clock advanced:
Repetition risk:
Required structural change next unit:

## 9. Chapter State Update If Relevant

Chapter state path:
Content draft:

## 10. Next Constraints

Must continue from:
Must not contradict:
Must not escalate yet:
Required unresolved pressure:
Suggested next attractor:
Required hook/payoff movement if relevant:

## 11. Missing / Unsafe Updates

- candidate update:
  reason not written:
```

## Hard Checks

Mark `REVISE` if:

- approved source is unclear;
- user approval is missing;
- update includes speculation or inferred secrets;
- update writes a fact without a source;
- durable state changed but no State or Event update is proposed;
- relationship changed but no Relationship update is proposed;
- new recurring name or term appeared but no name registry update is proposed;
- next canon-dependent step would rely on chat memory rather than wiki state;
- a one-time action is written as a permanent trait;
- a local action is written as full organization policy without proof;
- a reference-setting idea is written as canon without appearing in approved canon;
- important consequences are not recorded;
- next constraints are missing when the approved change affects future units.