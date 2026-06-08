# Failure 003: Direct Emotion Dialogue

## Failure ID

failure_003_direct_emotion_dialogue

## Failure Name

Characters state their emotional thesis directly.

## Where It Appears

Dialogue, conflict scenes, relationship scenes, chapter endings.

## Symptom

A side character says exactly what the scene is meant to imply.

Examples:

```text
I am jealous.
I also want to stay.
You are ahead of me.
I am afraid.
I do not trust you.
```

## Root Cause

The model tries to make emotion legible by converting subtext into explicit explanation.

## Why Readers Notice

Real people often conceal, redirect, joke, bargain, or act before saying the exact emotional truth. Direct thesis lines make characters feel like tools.

## Detection Signals

- dialogue explains the scene's theme
- character says a feeling without needing to
- line could be replaced by an action
- recurring side character repeatedly announces jealousy, fear, admiration, or resentment
- conflict becomes too clean and readable

## Required Fix

Replace direct emotion with:

```text
practical request
small lie
delayed action
overly fast movement
avoidance
joke
misdirection
object handling
imitation without admission
```

## Regression Test

For each emotional line, ask:

```text
Could this character hide this feeling instead?
Could the action show it more naturally?
```

If yes, revise.

## Related Governance Files

- `governance/longform_ai_inertia_check.md`
- `prompts/02_chapter_brief.md`
- `governance/chapter_brief_review.md`
- `prompts/04_review_hook.md`
