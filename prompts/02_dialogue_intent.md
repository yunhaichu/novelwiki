# Dialogue Intent Prompt

Use this prompt after `prompts/02_scene_expression_state.md` and before drafting prose.

The purpose is to design what each line of dialogue must do, without writing polished final dialogue too early.

## Hard Source Rule

Dialogue intent must be derived from:

- current scene expression state;
- character expression card;
- actor cognition card;
- current chapter design;
- approved wiki facts;
- previous line / previous event in the scene.

Do not invent new character voice traits, catchphrases, slang, dialect, or witty lines at this step.

If the speaker lacks a source-grounded voice pattern, write minimal functional dialogue and mark `expression_gap`.

## Core Principle

Dialogue must change at least one of:

```text
information
relationship
pressure
action direction
```

Dialogue is not for explaining background.
Dialogue is not for saying the whole truth.
Dialogue is not for making the character sound clever unless that is source-grounded and scene-relevant.

Characters may break, hide, stop, dodge, correct themselves, omit information, or answer a different question.

## Output Format

```text
# Dialogue Intent

Novel ID:
Chapter number:
Scene ID:
Source files read:

## Dialogue Beats

### Beat
Dialogue ID:
Speaker:
Listener:
Timing:
Previous trigger:
Speech goal:
Must reveal:
Must hide:
Subtext:
Allowed vocabulary:
Forbidden vocabulary:
Speech shape:
Scene effect:
Expression gap:

### Beat
...

## No-Dialogue Areas

List scene moments that should be carried by action, object, silence, sound, or position instead of dialogue.

-

## Pass / Fail

ALLOW / REVISE
```

## Field Guidance

`speech_goal` should be concrete.

Weak:

```text
show pressure
```

Strong:

```text
force the protagonist to either close the old data screen or openly question the official record
```

`speech_shape` should be a usable form.

Examples:

- short status report;
- clipped technical warning;
- formal denial;
- counter-question;
- unfinished warning;
- authority command;
- half-truth with missing subject;
- refusal without full reason;
- public politeness with private threat;
- background shout that changes movement.

## Checks

Mark `REVISE` if:

- a line only explains setting;
- a line says all information at once;
- a character says something they do not know;
- a character sounds like author commentary;
- different characters share the same rhythm and vocabulary;
- the same character speaks the same way to superior, subordinate, ally, and enemy;
- `scene_effect` does not change information, relationship, pressure, or action direction;
- a line is too polished for the speaker's job, pressure, and environment;
- the dialogue could be removed without changing the scene.

## Anti-AI Dialogue Rule

If a line sounds like a neat summary, aphorism, trailer sentence, dramatic slogan, or author explanation, replace it with:

- a shorter status report;
- a question;
- a refusal;
- an incomplete line;
- an action instead of speech;
- a concrete object / number / permission / record / route / consequence.
