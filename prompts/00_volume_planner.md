# Volume Planner Prompt

Use this prompt after the project outline passes `governance/outline_review.md` and before chapter beat generation.

The goal is to turn a project outline into a volume-level plan that can control 10-30 chapters at a time.

## Required Inputs

Read:

- approved type contract if present
- project outline
- outline review result
- genre / story engine
- primary genre promise
- core relationship matrix
- three-layer suspense
- five turning points
- reader entry requirements from outline
- style rules
- forbidden drift list
- `governance/consequence_chain_check.md`
- `governance/conflict_escalation_check.md`

## Output Object

Produce a volume plan with these sections:

```text
Volume number:
Volume title:
Volume role in whole story:
Primary genre promise to pay in this volume:
Volume reader expectation:
Volume core conflict:
Volume external goal:
Volume inner pressure:
Volume main opposition:
Volume failure cost:
Volume start state:
Volume end state:
Primary reward pattern:

Opening reader-entry target:
- what chapters 1-3 must make clear:
- what chapters 1-3 must delay:
- what visible gain/change should exist by chapter 3:

Relationship changes:
- character A / character B:
- surface relation at start:
- hidden tension:
- required change by end:

Three-layer suspense in this volume:
- immediate:
- midterm:
- longterm/global link:

Volume turning points:
- opening imbalance:
- first method/tool/resource:
- midpoint turn:
- late reversal:
- volume climax:

Consequence chain across volume:
- opening consequence:
- midpoint consequence:
- climax consequence:
- next-volume pressure:

Conflict escalation across volume:
- start conflict level:
- midpoint escalation:
- late escalation:
- climax cost:
- retreat path reduced by:

Required chapter groups:
- chapters 1-3:
- chapters 4-6:
- chapters 7-10:

Continuity objects to track:
Forbidden drift in this volume:
False promise risks:
```

## Rules

- Do not write chapter prose.
- Do not invent chapter-by-chapter events yet unless required.
- Define what changes between volume start and volume end.
- Define what the reader gets in this volume, not only what pressure is added.
- The first volume must make the primary genre promise visible early.
- Chapters 1-3 must support a future reader entry gate and golden-three review.
- Every volume must contain at least one relationship change and one main-system progress change.
- The volume midpoint must change either the protagonist's plan, opponent, rule understanding, resource state, or relationship map.
- The volume climax must close a local problem while opening a larger pressure or consequence.
- Volume events should form consequence chains, not only a list of episodes.
- Conflict should escalate through stronger opposition, higher cost, reduced retreat, method failure, or changed relationship/status risk.

## Output

Output only the volume plan.
