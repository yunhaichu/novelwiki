# Review Hook Prose Addendum

Use this addendum with `prompts/04_review_hook.md` after the structural chapter review is complete.

This addendum is mandatory for chapter 1-3, new arc openings, and any chapter the user flags as having AI taste or artificial wording.

## Additional Inputs

Read:

```text
governance/scene_naturalness_check.md
governance/dialogue_pressure_check.md
governance/in_world_naming_check.md
governance/prose_publishability_review.md
governance/anti_ai_novel_phrase_check.md
governance/low_anchor_phrase_check.md
```

## Additional Decision Layer

The review must now return two decisions:

```text
Workflow decision: PASS / REVISE
Prose decision: PUBLISHABLE / NEEDS LINE REVISION / STRUCTURAL REWRITE
```

Map the old decision as follows:

```text
ALLOW = Workflow decision: PASS
REVISE = Workflow decision: REVISE or Prose decision: NEEDS LINE REVISION / STRUCTURAL REWRITE
```

## Prose Checks

### 1. Scene Naturalness

Check whether key lines feel natural for the character, scene, social status, and pressure.

Mark `NEEDS LINE REVISION` if the scene works structurally but uses artificial diction, author-side labels, forced jokes, or summary narration.

### 2. Dialogue Pressure

Check whether dialogue changes pressure, status, relation, information, cost, or practical action.

Mark `NEEDS LINE REVISION` if dialogue mainly explains setting, asks the reader's question, sets up jokes, or says the character's whole inner thesis.

### 3. In-World Naming

Check whether object names, place labels, ranks, routes, and institutions feel like in-world usage rather than map labels, system UI, or outline tags.

Mark `NEEDS LINE REVISION` if a rough scene uses a polished label without reason.

### 4. Ending Concreteness

Check whether the ending lands on action, object, bodily sensation, unfinished choice, concrete consequence, or changed relationship.

Mark `NEEDS LINE REVISION` if the ending lands on a polished role-summary or theme sentence.

## Output Block

Append this block to the normal chapter review:

```text
Prose publishability:
- Workflow decision:
- Prose decision:
- Scene naturalness:
- Dialogue pressure:
- In-world naming:
- AI phrase risk:
- Ending concreteness:

Required line revisions if needed:
1.
2.
3.
```

## Decision Examples

```text
Workflow decision: PASS
Prose decision: NEEDS LINE REVISION
Reason: reader entry and consequence chain pass, but the ending uses a polished role-summary line and several names feel like map labels.
```

```text
Workflow decision: REVISE
Prose decision: STRUCTURAL REWRITE
Reason: reader entry fails, so line revision is insufficient.
```
