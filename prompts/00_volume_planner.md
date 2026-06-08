# Volume Planner Prompt

Use this prompt after the project outline passes `governance/outline_review.md` and before chapter beat generation.

The goal is to turn a project outline into a volume-level plan that can control 10-30 chapters at a time.

## Required Inputs

Read:

- project outline
- outline review result
- genre / story engine
- main genre promise
- core relationship matrix
- three-layer suspense
- five turning points
- style rules
- forbidden drift list

## Output Object

Produce a volume plan with these sections:

```text
Volume number:
Volume title:
Volume role in whole story:
Volume core conflict:
Volume external goal:
Volume inner pressure:
Volume main opposition:
Volume failure cost:
Volume start state:
Volume end state:
Main genre promise to pay in this volume:
Reader expectation:
Primary reward pattern:
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
Required chapter groups:
- chapters 1-3:
- chapters 4-6:
- chapters 7-10:
Continuity objects to track:
Forbidden drift in this volume:
```

## Rules

- Do not write chapter prose.
- Do not invent chapter-by-chapter events yet unless required.
- Define what changes between volume start and volume end.
- Define what the reader gets in this volume, not only what pressure is added.
- Every volume must contain at least one relationship change and one main-system progress change.
- The volume midpoint must change either the protagonist's plan, opponent, rule understanding, resource state, or relationship map.
- The volume climax must close a local problem while opening a larger pressure or consequence.

## Output

Output only the volume plan.
