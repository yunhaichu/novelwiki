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

## Control-Based Chapter Principle

A chapter should usually change what the protagonist can understand, influence, protect, threaten, hide, or choose.

Do not make the chapter's progress depend only on:

- the protagonist becoming stronger;
- the protagonist being abused again;
- the protagonist receiving a convenient gift;
- an enemy making a foolish mistake for plot convenience.

For a control-based protagonist, each chapter should ask one of these:

```text
What can the protagonist notice that others miss?
What can they influence without openly controlling it?
What rule, fear, incentive, relationship, or object can they use?
What do they fail to control?
What cost do they accept to preserve a more important condition?
When would direct action be justified?
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
What the protagonist can control at start:
What the protagonist cannot control yet:
What the protagonist may influence indirectly:
What must not be easy:
State direction by chapter end:
Control change by chapter end:
Possible pressure sources:
Characters likely to act:
Objects or rules in play:
Information boundaries:
Forbidden answers:
Force / restraint / deception / retreat / direct action question:
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

### Control change by chapter end

Define what changes in the protagonist's control, not the exact event.

Examples:

```text
They gain one true piece of information.
They become noticed by one person.
They lose an easy retreat path.
They learn one rule that can later be used.
They influence someone indirectly but create suspicion.
```

### Possible pressure sources

List possible sources, not mandatory events.

### Force / restraint / deception / retreat / direct action question

State what mode of action the chapter pressure may test.

Do not decide the answer.

Examples:

```text
Is this a chapter where restraint is wiser than force?
Is this a chapter where deception creates short-term safety but long-term suspicion?
Is this a chapter where direct action is necessary because waiting would lose the key condition?
```

### Forbidden answers

Use this to prevent easy or false solutions.

Examples:

- no direct confession of future knowledge
- no instant power-up
- no convenient stranger rescue
- no perfect lie that works cleanly
- no repeated passive suffering without information or leverage
- no pure force solution unless the pressure question justifies it

## Rules

- Do not prescribe the protagonist's exact action.
- Do not prescribe the antagonist's exact reaction.
- Do not write a full scene outline.
- Do not decide the chapter hook.
- The answer must emerge from multi-agent simulation.
- If the pressure question has an obvious easy answer, revise the pressure card.
- Avoid both pure power escalation and passive suffering as default chapter engines.
- The chapter should change control, information, leverage, relationship, risk, or available choices.

## Output

Output only the chapter pressure card.
