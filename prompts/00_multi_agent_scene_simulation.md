# Multi-Agent Scene Simulation Prompt

Use this prompt before drafting prose when the story depends on character interaction.

The purpose is not to write a polished chapter. The purpose is to let story movement emerge from characters with partial knowledge, private motives, and conflicting pressures.

## Inputs

Read or define:

- current scene premise
- current world state
- relevant character files
- relevant rules or location facts
- previous chapter state if any
- unresolved questions touched by this scene

## Required Character State

For each active character, define:

```text
Character:
Private knowledge:
Public knowledge:
Current desire:
Current fear:
Current leverage:
Current constraint:
Likely first move:
What they will not say directly:
```

Do not give every character the same knowledge.

Do not let a character know the outline, the future plot, another character's private motive, or narrator-only information.

## Simulation Rule

Run the scene in action rounds.

Each round should contain:

```text
Round number:
World pressure:
Character action:
Reason this character takes this action:
What information the action reveals or hides:
Other characters' reactions:
State change:
New pressure created:
```

Run 3 to 5 rounds unless the scene naturally reaches a strong stopping point earlier.

## Action Rules

A character action must come from at least one of:

- private knowledge
- current desire
- fear
- social rank
- immediate threat
- material need
- misunderstanding
- local rule
- object in the scene
- previous action by another character

Do not use an action only because the story needs a hook, reversal, clue, or payoff.

## Output

Output only:

```text
Scene simulation title:
Initial world state:
Active character states:
Action rounds:
Emergent story movement:
State update:
Best next-scene pressure:
Material suitable for prose:
Material to discard:
```

Do not write chapter prose.
