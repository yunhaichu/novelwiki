# Contradiction Check

Use this during story bible review, chapter brief review, chapter review, revision review, and pre-merge review.

The goal is to prevent local prose from breaking global canon.

## Required Data Sources

Use available project files:

- story bible / world state
- character files
- timeline file
- foreshadow register
- object / clue / resource state
- glossary / approved term list
- chapter states
- change log if present

## Check Types

### 1. Logic Consistency

Ask:

```text
Can this event happen under the current rules?
Is the cause already present?
Does the result follow from the cause?
Would removing this event break later events?
```

Mark REVISE if an event only happens because the author needs it to happen.

### 2. Timeline Consistency

Ask:

```text
When does this happen?
How long does it take?
Can involved characters be there?
Does this conflict with another scene happening at the same time?
```

Mark REVISE for impossible travel, repeated time slots, missing time anchors in critical scenes, or order conflicts.

### 3. Location Consistency

Ask:

```text
Where is each character, object, or clue?
Can they move from the previous location to this location in time?
Does the scene use a location that has not been established or explained?
```

### 4. Motivation Consistency

Ask:

```text
Why does this character act now?
Which desire, fear, flaw, promise, or pressure drives the action?
Is the action consistent with the character's known decision pattern?
```

Mark REVISE if a character turns only to move the plot.

### 5. Information Flow Consistency

Ask:

```text
Who knows this information?
When did they learn it?
How did they learn it?
Is the POV character allowed to know this?
Is the reader allowed to know this?
```

Mark REVISE for knowledge leaks, unexplained deductions, or characters knowing facts from unavailable scenes.

### 6. Rule and Terminology Consistency

Ask:

```text
Does this term already exist?
Is the rule still the same as before?
Does the chapter create an exception?
Is the exception paid for, limited, or logged?
```

Mark REVISE if a world rule changes only to solve the current scene.

### 7. Object / Clue / Resource State

Ask:

```text
Who has the object?
Where is the clue?
What is the resource amount or status?
Was it consumed, damaged, lost, hidden, revealed, or transferred?
```

Mark REVISE if important items, wounds, money, tokens, documents, clues, or powers appear or disappear without state change.

### 8. Foreshadow Consistency

Ask:

```text
Was this planted earlier?
Was it intended as foreshadowing?
What is its surface meaning?
What is its real meaning?
When should it pay off?
```

Mark REVISE if payoff appears without plant, or plant has no planned treatment.

### 9. Version Consistency

Ask:

```text
Did a later revision change canon?
Were story bible, chapter state, timeline, character files, and glossary updated together?
```

Mark REVISE if prose and database disagree.

## Output Block

When reviewing, include:

```text
Contradiction check:
- Logic:
- Timeline:
- Location:
- Motivation:
- Information flow:
- Rules / terminology:
- Object / clue state:
- Foreshadow:
- Version sync:
Required fixes:
```

## Decision Rule

Mark REVISE if any hard contradiction remains.

Hard contradictions include:

- impossible event
- impossible location/time
- character knows unavailable information
- rule changes without explanation
- key object state breaks
- character action has no motive under known pressure
- prose and canon files disagree
