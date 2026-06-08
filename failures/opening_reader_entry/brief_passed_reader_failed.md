# Failure Case: Brief Passed, Reader Failed

## Symptom

The draft satisfies the approved brief fields, but a first-time target reader cannot identify the core reading path.

The chapter may contain the planned setting, object, mystery, pressure, relationship note, and hook, yet the reader does not know what to care about first.

## Why It Happens In LLM Writing

The model treats a chapter brief as a checklist. It tries to include every planned element instead of building a low-cost reader entry path.

This often happens when the story bible contains more information than the opening should reveal.

## Reader Effect

The reader sees many valid elements but cannot decide:

- who matters most;
- what the immediate problem is;
- what is at stake;
- what type of story they are reading;
- why the next chapter is necessary.

## Detection Questions

```text
Can a first-time reader identify the protagonist?
Can they state the immediate trouble in one sentence?
Can they say what the protagonist wants now?
Can they say what can be lost soon?
Can they identify the primary genre promise?
Can they name one concrete memory point?
```

## Reject Rule

If a chapter requires wiki knowledge to feel clear, mark `REVISE`.

If a chapter follows the brief but fails the stranger-reader test, mark `REVISE`.

## Repair Strategy

Reduce the opening to:

```text
protagonist + immediate pressure + one abnormal object/action/choice + visible cost
```

Delay:

- secondary mysteries;
- backstory labels;
- system terms;
- organizational context;
- long-range lore;
- explanations of mechanism.

## Regression Prompt

Review an opening chapter that contains all planned brief elements but gives a first-time reader too many names, systems, and mysteries before the protagonist's immediate trouble becomes clear.

## Expected Reviewer Decision

```text
REVISE
```
