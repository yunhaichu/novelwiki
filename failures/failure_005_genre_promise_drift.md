# Failure 005: Genre Promise Drift

## Failure ID

failure_005_genre_promise_drift

## Failure Name

The story pays a side promise while neglecting the main genre promise.

## Where It Appears

Project outlines, volume plans, beat tables, chapter briefs, prose drafts.

## Symptom

The declared genre promises one type of reader reward, but the chapter or arc mainly delivers another.

Examples:

```text
cultivation story becomes workplace routine
mystery story becomes relationship slice-of-life without clue progress
romance story advances career but not relationship movement
science fiction story becomes generic action without rule discovery
farming/management story becomes only daily chores without resource-chain progress
```

## Root Cause

The model follows the local scene that is easiest to continue, instead of the story engine that readers came for.

## Why Readers Notice

Readers feel that the book is not delivering what its label promised. Even if the scene is readable, it feels like drift.

## Detection Signals

- local status improves but genre progress does not
- side scene is more developed than main promise
- chapter reward does not satisfy the reader desire activated by the genre
- several chapters can be removed without affecting the main system
- chapter brief cannot answer "how does this serve the main genre promise?"

## Required Fix

Define the main genre promise in the project outline and volume plan, then require every beat and chapter brief to convert local events into that promise.

Examples:

```text
cultivation: work access -> rule understanding / resource / practice correction
mystery: conversation -> clue / contradiction / suspect relation
romance: banter -> emotional risk / intimacy / misbelief shift
urban: job scene -> money / reputation / career leverage / relationship consequence
science fiction: anomaly -> tested rule / technical limit / human cost
```

## Regression Test

For each chapter, fill in:

```text
Local gain:
Main genre promise conversion:
Reader desire paid:
```

If conversion is missing, mark REVISE.

## Related Governance Files

- `governance/reward_engine.md`
- `governance/outline_review.md`
- `governance/volume_review.md`
- `governance/beat_review.md`
- `prompts/04_review_hook.md`
