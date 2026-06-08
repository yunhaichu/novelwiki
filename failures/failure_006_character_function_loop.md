# Failure 006: Character Function Loop

## Failure ID

failure_006_character_function_loop

## Failure Name

Recurring characters become fixed functions.

## Where It Appears

Side characters, rivals, mentors, comic companions, authority figures, love interests, family members.

## Symptom

A recurring character repeats the same story function across chapters.

Examples:

```text
comic friend only makes jokes
rival only mocks
mentor only explains
authority figure only records or judges
love interest only rewards or worries
family member only motivates guilt
```

## Root Cause

The model treats characters as plot devices rather than people with their own desires, fears, costs, and changing tactics.

## Why Readers Notice

Side characters feel like buttons. When the protagonist arrives, they perform their assigned function and stop existing.

## Detection Signals

- character has the same reaction in multiple chapters
- character only asks questions the reader needs answered
- character's actions do not change their own status
- character has no hidden pressure or self-interested reason
- character does not adapt after previous events

## Required Fix

For each recurring character, define:

```text
surface behavior
hidden pressure
will say
will not say
stress action
self-interested goal
how they adapt after failure
```

Then require scenes to show at least one self-directed action.

## Regression Test

Ask:

```text
What does this character want in this chapter if the protagonist is removed?
What changes for them by the end?
```

If the answer is nothing, mark REVISE.

## Related Governance Files

- `prompts/02_chapter_brief.md`
- `governance/chapter_brief_review.md`
- `prompts/04_review_hook.md`
- `governance/longform_ai_inertia_check.md`
