# Scene Expression State Prompt

Use this prompt after emergent chapter design and before drafting dialogue or prose.

The purpose is to derive each character's scene-specific speech and behavior mode from approved wiki facts, current scene pressure, relationship position, and knowledge boundary.

## Hard Source Rule

All scene expression state must come from:

- approved character expression card;
- approved actor cognition card;
- current chapter design;
- current scene board / scene pressure;
- current novel wiki;
- previous chapter state.

Do not invent new speech traits, emotional habits, posture habits, accents, catchphrases, or relationship modes inside this step.

If a needed trait is missing, mark `expression_gap` and continue with only source-grounded behavior.

## Core Principle

The same person should not speak the same way in every situation.

Scene expression is:

```text
character expression card
+ listener relationship
+ immediate speech goal
+ what must be revealed
+ what must be hidden
+ what they know / do not know
+ current pressure
+ setting constraints
```

## Output Format

```text
# Scene Expression State

Novel ID:
Chapter number:
Scene ID:
Source files read:

## Character Expression States

### Character
Character ID:
Listener / target:
Relationship position:
Scene pressure:
Immediate goal:
What they know:
What they do not know:
What they must reveal:
What they must hide:
What they fear if they say too much:
Allowed vocabulary:
Forbidden vocabulary:
Speech shape:
Body / action habit while speaking:
Expected subtext:
Required scene effect:
Expression gaps:

### Character
...

## Scene-Level Dialogue Constraints

What cannot be said openly:
-

What must remain implied:
-

What information should move through object, action, silence, interruption, or refusal instead of direct explanation:
-

Which dialogue line, if any, must change information / relationship / pressure / action direction:
-

## Pass / Fail

ALLOW / REVISE
```

## Checks

Mark `REVISE` if:

- every character uses the same sentence rhythm;
- dialogue states are not grounded in expression cards or wiki;
- a character says information they do not know;
- a character explains background rather than pursuing a scene goal;
- `speech_shape` is vague, such as `serious` or `emotional`, instead of usable forms like `short status report`, `unfinished sentence`, `formal denial`, `counter-question`, `refusal with reason omitted`;
- `required scene effect` does not change information, relationship, pressure, or action direction;
- a character's relationship to the listener does not affect their speech.
