# Revision Prompt

Use this prompt after a draft or planning artifact receives REVISE from chapter review, reader entry review, opening brief review, outline review, beat review, or story bible review.

The goal is controlled repair. For ordinary failures, use the smallest sufficient change. For opening-reader-entry failures, structural rewrite is allowed. For prose-only failure, use line revision.

## Required Inputs

Read:

- the rejected draft or artifact
- the review result
- workflow decision and prose decision if present
- required fixes
- failed hard gates if any
- approved type contract if applicable
- approved reader entry gate if applicable
- approved outline / volume / beat / brief if applicable
- style rules
- glossary / approved term list
- story bible / world state if applicable
- contradiction check result if applicable
- previous version if available
- `prompts/06_line_revision.md` when prose decision is NEEDS LINE REVISION

## Revision Mode

Choose one mode before rewriting:

```text
ordinary repair
opening structural rewrite
planning artifact revision
line revision
```

### Ordinary Repair

Use for normal chapter failures where the structure still works but a specific story check failed.

Make the smallest sufficient change that resolves the failed check.

### Opening Structural Rewrite

Use for chapter 1-3, new volume openings, or new major arc openings when the failure is reader entry, type promise visibility, opening information overload, protagonist entry, or one-sentence recap failure.

In this mode, do not force minimal line repair. You may reorder, delete, merge, or rebuild scenes if needed.

### Planning Artifact Revision

Use when the outline, type contract, reader entry gate, beat table, story bible, or brief itself failed.

Revise the artifact first. Do not patch prose around a broken artifact.

### Line Revision

Use when:

```text
Workflow decision: PASS
Prose decision: NEEDS LINE REVISION
```

In this mode, preserve structure, consequence chain, and chapter ending function. Revise only language, naming, dialogue, artificial phrasing, and scene-naturalness problems.

If a line revision requires adding new facts, stop and request ordinary repair instead.

## Revision Principle

For ordinary repair:

- Preserve correct material.
- Remove or rewrite only failed material.
- Do not create new canon facts unless the review explicitly requires them.
- Do not change the approved engine, volume goal, beat role, or character arc unless the review explicitly says the structure itself must change.

For opening structural rewrite:

- Reader entry outranks preserving existing prose.
- Reduce opening information load.
- Put protagonist, immediate pressure, visible desire, cost, and active choice before secondary mysteries.
- Delay backstory, system terms, world rules, and institutional context unless they create present pressure.
- Replace setting explanation with scene pressure.
- Replace strange-but-vague hooks with concrete consequence, object, choice, or cost.

For line revision:

- Preserve the approved scene order.
- Preserve main action and consequence.
- Replace artificial terms with scene-natural wording.
- Make dialogue more practical and pressure-driven.
- Replace polished summary endings with concrete action, object, cost, or changed relationship where needed.
- Do not expand worldbuilding to explain a bad phrase.

## Revision Plan

Before rewriting, fill in:

```text
Artifact being revised:
Revision mode:
Review decision:
Workflow decision:
Prose decision:
Failed checks:
Root cause:
Allowed changes:
Forbidden changes:
Canon files that may need updating:
Expected output:
```

## Fix Types

Use one or more:

```text
reader entry fix
opening structure fix
type promise fix
information load reduction
structure fix
causal fix
consequence chain fix
conflict escalation fix
character motivation fix
character action logic fix
relationship fix
reward fix
main-system relevance fix
terminology fix
in-world naming fix
scene naturalness fix
dialogue pressure fix
low-anchor phrase fix
anti-AI phrase fix
ending concreteness fix
continuity fix
style compression
scene deletion / merge
scene reorder
```

## Revision Rules

- If a scene exists only as process log, either cut it or convert it into conflict, choice, or consequence.
- If a line states a character's inner emotion too directly, replace it with action, concealment, or practical speech.
- If a phrase is low-anchor or AI-polished, replace it with plain speech, clear narration, action, object, consequence, or changed relationship.
- If a name sounds like a map label, system UI, or outline tag, localize it through rougher in-world wording.
- If dialogue does not change pressure, relation, status, cost, or information, cut or rewrite it.
- If a gain does not connect to the primary genre promise, either connect it or remove it.
- If the consequence chain is weak, add or clarify who reacts, what path closes, what becomes harder, or what must happen next.
- If conflict does not escalate, add cost, stronger obstacle, reduced retreat, opponent/system adaptation, method failure, or approved controlled non-escalation.
- If a new fact is introduced, mark which canon file must be updated.

## Output

For prose revision, output:

```text
Revision plan:
Revised text:
Canon update notes:
```

For line revision, output:

```text
Line revision plan:
Revised text:
Change notes:
```

For planning artifact revision, output the revised artifact only unless the user asks for notes.
