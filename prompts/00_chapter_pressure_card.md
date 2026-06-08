# Chapter Pressure Card Prompt

Use this prompt before multi-agent scene simulation for a chapter.

The purpose is to define the pressure problem of a chapter without deciding the answer.

This is a weak boundary. It should force direction, not dictate plot.

## Core Principle

A chapter pressure card is not a beat sheet.

It should ask a hard story question and define the state direction, while leaving the specific actions to character interaction.

Do not write:

```text
The protagonist does X, then Y happens.
```

Write:

```text
The protagonist wants X, but pressure Y makes every attempt risky. By the end, their state must move toward Z.
```

## Inputs

Read:

- novel spine
- volume state plan
- current chapter state if continuing
- relevant character files
- relevant world/location/object files
- unresolved questions

## Output Object

Produce:

```text
Chapter number:
Current state before chapter:
Chapter pressure question:
Protagonist immediate desire:
Main constraint:
What must not be easy:
State direction by chapter end:
Possible pressure sources:
Characters likely to act:
Objects or rules in play:
Information boundaries:
Forbidden answers:
What should remain open:
```

## Field Guidance

### Chapter pressure question

Ask the central pressure question.

Example:

```text
Can the protagonist avoid being sent to a dangerous route without revealing that they know why it is dangerous?
```

### State direction by chapter end

Define how the state should move, not how it must happen.

Example:

```text
The protagonist should be in a narrower and more dangerous position, but should learn something true about the local system.
```

### Possible pressure sources

List possible sources, not mandatory events.

### Forbidden answers

Use this to prevent easy or false solutions.

Examples:

- no direct confession of future knowledge
- no instant power-up
- no convenient stranger rescue
- no perfect lie that works cleanly

## Rules

- Do not prescribe the protagonist's exact action.
- Do not prescribe the antagonist's exact reaction.
- Do not write a full scene outline.
- Do not decide the chapter hook.
- The answer must emerge from multi-agent simulation.
- If the pressure question has an obvious easy answer, revise the pressure card.

## Output

Output only the chapter pressure card.
