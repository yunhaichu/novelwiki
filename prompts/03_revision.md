# Revision Prompt

Use this prompt after a draft receives REVISE from the chapter review, outline review, beat review, or story bible review.

The goal is not to regenerate everything. The goal is controlled repair.

## Required Inputs

Read:

- the rejected draft or artifact
- the review result
- required fixes
- approved outline / volume / beat / brief if applicable
- style rules
- glossary / approved term list
- story bible / world state if applicable
- contradiction check result if applicable
- previous version if available

## Revision Principle

Make the smallest sufficient change that resolves the failed check.

Do not create new canon facts unless the review explicitly requires them.

Do not change the approved engine, volume goal, beat role, or character arc unless the review explicitly says the structure itself must change.

## Revision Plan

Before rewriting, fill in:

```text
Artifact being revised:
Review decision:
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
structure fix
causal fix
character motivation fix
relationship fix
reward fix
main-system relevance fix
terminology fix
low-anchor phrase fix
continuity fix
style compression
scene deletion / merge
scene reorder
```

## Revision Rules

- Preserve correct material.
- Remove or rewrite only failed material.
- If a scene exists only as process log, either cut it or convert it into conflict, choice, or consequence.
- If a line states a character's inner emotion too directly, replace it with action, concealment, or practical speech.
- If a phrase is low-anchor, replace with plain speech or clear narration.
- If a gain does not connect to the main genre promise, either connect it or remove it.
- If a new fact is introduced, mark which canon file must be updated.

## Output

For prose revision, output:

```text
Revision plan:
Revised text:
Canon update notes:
```

For planning artifact revision, output the revised artifact only unless the user asks for notes.
