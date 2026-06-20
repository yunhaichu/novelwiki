# Interactive Writing Flow

This file defines the default interaction protocol for formal novel writing.

It exists because the workflow should no longer depend on a full-chapter draft followed by a large review pass. The review burden should move earlier, into small approval gates before prose is written.

## Core Rule

```text
Discuss -> approve -> draft bounded unit -> local self-check -> user canon approval -> sync
```

Do not invert this into:

```text
Draft everything -> review everything -> repair everything
```

## What Counts As Canon

Only these can become canon:

1. User-approved setup output.
2. User-approved chapter intent.
3. User-approved scene plan.
4. User-approved draft unit.
5. User-approved wiki sync.

A model proposal is not canon.
A rejected draft is not canon.
A useful but unapproved discussion point is not canon.
A fast-trial output is not canon.

## Gate A: Chapter Intent Approval

Run after wiki retrieval, volume / arc check, and chapter trend + hook/payoff convergence.

The assistant may output only:

```text
- chapter function in current volume / arc
- current trend pressure
- protagonist pressure and usable gain
- reader hook / payoff
- candidate scene list
- forbidden escalations
- uncertain decisions requiring user choice
```

The assistant must not output prose at Gate A.

The user may approve, reject, narrow, expand, reorder, or replace the intent.

If the user changes the intent, treat the correction as authority for the next proposal, but do not write it into canon until later approval and sync.

## Gate B: Scene Plan Approval

Run after Gate A passes and before prose.

The assistant may output only:

```text
- scene objective
- active actors
- actor cognition limits
- location / object anchors
- beat list
- dialogue intent when needed
- scene hook/payoff
- canon facts that may change if approved
```

The assistant must not write prose at Gate B.

For simple low-stakes transition units, Gate B may be collapsed into a short confirmation card, but it must still identify objective, actors, and state movement.

## Gate C: Draft Unit Approval

Run after Gate B passes.

A draft unit may be:

- one scene;
- one subscene;
- one bounded chapter segment;
- one transition passage;
- one dialogue sequence.

A draft unit must not silently continue into the next unapproved scene.

After the unit, provide a local status card:

```text
Canon changes if approved:
- ...

Unresolved reader debt:
- ...

Next decision point:
- ...
```

The user may approve, request revision, reject, or redirect.

## Local Self-Check

Every draft unit gets a lightweight check before canon sync.

Check:

1. No contradiction with current wiki.
2. No unapproved names or terms.
3. No actor omniscience.
4. No summary-only prose.
5. No interface, report, log, or status text replacing story action.
6. Approved hook/payoff remains visible.
7. Protagonist gain or state movement remains usable when required.
8. The next decision point is clear.

Do not run heavy review unless a trigger exists.

## Triggered Reviews

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

Do not sync after discussion.
Do not sync after an unapproved plan.
Do not sync after a rejected draft.
Do not sync speculative consequences.

Sync only after explicit canon approval.

For a full approved formal chapter, update:

```text
novels/<novel_id>/wiki/chapter_states/chapter_<number>.md
```

Also update character, organization, world, growth, timeline, relationship, foreshadowing, style, name, and term files only when approved prose confirms durable facts.

For an approved partial scene, either wait until the chapter is approved or create a clearly marked session / draft note if the user asks for incremental tracking.

## Batch Mode Exception

The user may explicitly request batch mode.

Batch mode allows longer continuous drafting, but it does not remove:

- canon wiki retrieval;
- Name & Term Gate;
- trend convergence;
- hook/payoff requirement;
- local self-check;
- user canon approval before sync.

If the user later asks to return to interactive mode, immediately stop batch continuation and resume Gate A / Gate B / Gate C behavior.

## Failure Handling

If a proposed chapter intent fails, revise Gate A. Do not patch prose.

If a scene plan fails, revise Gate B. Do not draft around the weakness.

If a draft unit fails, either revise only that unit or return to Gate B if the failure is structural.

If a canon contradiction appears, stop and identify:

```text
- conflicting fact
- source file if known
- whether the draft or wiki likely needs correction
- smallest safe next action
```

## Output Discipline

During interaction, prefer small cards over long documents.

Do not bury the user decision point.

Every proposal should make clear what the user is approving.

Every draft unit should make clear what would become canon if approved.
