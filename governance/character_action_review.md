# Character Action Review Gate

Use this after creating or revising character action logic, story bible character entries, or chapter-specific character action plans.

## Decision

Return one of:

```text
PASS
REVISE
```

## Required Checks

### 1. External Desire

The character must want something concrete enough to create action.

Mark `REVISE` if the character only has mood, background, or personality labels.

### 2. Inner Need

The character must have an inner pressure, lack, wound, or need that can shape choices.

Mark `REVISE` if the character is only a function in the plot.

### 3. Triggerable Flaw

The flaw must name what triggers it and how it creates cost.

Mark `REVISE` if the flaw is only an adjective.

### 4. Decision Pattern

The character must have a recognizable protection priority, information threshold, and conflict mode.

Mark `REVISE` if the character could act in any way depending on author need.

### 5. Self-Justification

Complex characters should have a way to explain their own wrong choices.

Mark `REVISE` if the character's mistakes can only be explained from outside the story.

### 6. Scene Action Logic

For chapter use, the character must have a reason to act now.

Mark `REVISE` if the action is only an author convenience.

### 7. Consequence

A flaw-triggered or desire-driven action must create consequence.

Mark `REVISE` if the character's internal design does not affect plot, relationship, cost, or future pressure.

### 8. Dialogue Concealment

The character should not state their whole emotional thesis directly.

Mark `REVISE` if dialogue mainly explains theme, motive, or relationship state without practical pressure.

## Output Format

```text
Decision: PASS / REVISE

Main reason:

Checks:
- External desire:
- Inner need:
- Triggerable flaw:
- Decision pattern:
- Self-justification:
- Scene action logic:
- Consequence:
- Dialogue concealment:

Required fixes if REVISE:
1.
2.
3.
```
