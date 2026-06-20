# Interactive Writing Flow

This file defines the default human-AI collaboration protocol for formal novel creation.

NovelWiki should not operate as a batch drafting pipeline followed by heavy review. The normal process is discussion-first and wiki-centered: retrieve relevant story knowledge, discuss the creative problem, make a user-approved decision, update the wiki when needed, and generate content only when the user wants a concrete output.

## Core Rule

```text
retrieve wiki knowledge -> discuss -> decide -> mutate wiki if approved -> generate when needed -> sync approved canon
```

Do not invert this into:

```text
draft everything -> review everything -> repair everything
```

## What Counts As Canon

Only these can become canon:

1. User-approved setup output.
2. User-approved entity, event, state, relationship, rule, name, or term decisions.
3. User-approved scene or chapter design.
4. User-approved generated prose.
5. User-approved wiki sync.

A model proposal is not canon.
A rejected option is not canon.
A useful but unapproved discussion point is not canon.
A fast-trial output is not canon.

## Collaboration Loop

### 1. Retrieve Relevant Wiki Knowledge

Before discussing any canon-dependent issue, retrieve the relevant wiki records.

Typical retrieval targets:

```text
- entities directly involved
- states at the relevant timepoint
- recent or causal events
- important relationships
- applicable rule systems
- approved names and terms
- prior sessions and mutations when the current issue depends on earlier user decisions
```

The assistant should surface only the relevant constraints. Do not dump the entire wiki into the discussion.

### 2. Discuss The Creative Problem

The user and AI may discuss any story object or story movement, including:

```text
- character behavior
- organization behavior
- location state
- rule-system logic
- time-aware state changes
- relationships
- scene design
- dialogue direction
- plot consequences
- reader hook / payoff
- naming and terminology
- prose rendering
```

The assistant's role is to clarify the current wiki state, expose possible contradictions, offer options, and ask for user choice when the direction is not determined.

### 3. Decide

The user is the creative authority.

A decision may:

```text
- accept one option
- combine options
- reject all options
- redirect the design problem
- request another proposal
- approve a canon mutation
- approve generation of a bounded output
```

Do not treat assistant preference as user decision.

### 4. Mutate Wiki When Approved

When the user approves a durable change, update the smallest sufficient set of wiki records.

Possible mutation targets:

```text
- Entity
- Timepoint
- State
- Relationship
- Event
- Session
- Mutation
- name registry
- style record
- chapter state
- other project-specific wiki file
```

Do not sync speculative consequences. Do not sync rejected options. Do not sync unapproved assistant proposals.

### 5. Generate When Needed

Generation is optional.

A user may ask for:

```text
- scene sketch
- scene plan
- dialogue sequence
- chapter segment
- full chapter draft
- entity card
- event summary
- wiki update record
- prose revision
```

Generated prose must stay inside the approved scope. It must not silently continue into an unapproved scene, chapter, arc, or canon change.

### 6. Sync Approved Canon

After the user approves a generated unit or durable design decision, sync the approved canon back into the wiki before the next canon-dependent step.

## Session Record

When a discussion changes the story model, create or update a session record if the user wants traceability or if the decision affects future canon.

A session should record:

```text
- what was discussed
- which wiki records were relevant
- accepted decisions
- rejected options when important
- approved mutations
- unresolved questions
```

A session is not canon by itself. It points to approved mutations that change canon.

## Event-Centered Memory

When a story fact matters later, prefer recording it as an Event.

An event should answer:

```text
who
when
where
did what
affected whom
changed what
caused or enabled what
```

This makes later retrieval more reliable than relying only on character notes or chapter summaries.

## Time-Aware State

Do not assume an entity has only one state.

When a character, organization, location, rule system, or other entity changes in a way that matters later, record the state at the relevant timepoint.

Use State records for durable changes. Do not create state records for trivial line-level details.

## Consistency Check

Consistency Check replaces heavy default review.

Run it before canon mutation and before canon-dependent generation.

Check:

1. No contradiction with retrieved wiki records.
2. No unapproved names or terms.
3. No entity acting outside its time-aware state.
4. No actor omniscience.
5. No rule-system violation unless the user explicitly approves a rule change.
6. No event consequence that lacks an Event or State update when it matters later.
7. No reliance on chat memory for durable facts.
8. No interface, report, log, or status text replacing story action in prose.

Do not run heavy review unless the user asks or a specific risk requires it.

## Targeted Review Triggers

Use targeted governance only when the risk is present.

```text
prose feels generic -> anti_ai_expression_review
trend logic changed -> emergent_plot_review
protagonist capability/state changed -> protagonist_growth_review
dialogue/relationship/authority drives scene -> character_voice_review
record/report/log/screen/status drives scene -> anti_record_driven_plot
object/resource/clue drives scene -> object_function_review
institution/process/timing/survival cost matters -> reality_logic_review
durable setting changed -> base_settings_review
canon sync is about to happen -> wiki_write_rules
```

## Wiki Sync Boundary

Do not sync after discussion alone.
Do not sync after an unapproved plan.
Do not sync after a rejected draft.
Do not sync speculative consequences.

Sync only after explicit canon approval.

For a full approved formal chapter, update:

```text
novels/<novel_id>/wiki/chapter_states/chapter_<number>.md
```

Also update relevant Entity, Event, Timepoint, State, Relationship, Session, Mutation, name, term, style, or foreshadowing records when approved canon confirms durable facts.

For an approved partial scene, either wait until the chapter is approved or create a clearly marked session / event / mutation note if the user asks for incremental tracking.

## Batch Mode Exception

The user may explicitly request batch mode.

Batch mode allows longer continuous drafting, but it does not remove:

- canon wiki retrieval;
- Name & Term Gate;
- relevant consistency check;
- user canon approval before sync;
- wiki sync before the next canon-dependent step.

If the user later asks to return to interactive mode, immediately stop batch continuation and resume the collaboration loop.

## Failure Handling

If a proposed direction conflicts with the wiki, stop and identify the conflicting record before proposing a workaround.

If a generated unit fails, either revise only that unit or return to discussion if the failure is structural.

If a canon contradiction appears, stop and identify:

```text
- conflicting record
- proposed or generated conflict
- whether the draft, plan, or wiki likely needs correction
- smallest safe next action
- whether user decision is required
```

## Output Discipline

During interaction, prefer small cards over long documents.

Do not bury the user decision point.

Every proposal should make clear what the user is deciding.

Every canon mutation should make clear what would change in the wiki.

Every generated unit should make clear what would become canon if approved.