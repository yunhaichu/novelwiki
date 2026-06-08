# Project Scope

This repository is a general novel-creation workflow project.

Its main object is not any single generated novel.

## Primary Object

The primary object is the reusable workflow for AI-assisted Chinese webnovel creation:

```text
outline generation
outline review
volume / arc beats
chapter brief
brief review
chapter draft
chapter review
chapter state update
continuity update
```

## Sample Novels

Directories under `novels/` are project instances, test novels, or experiments used to validate the workflow.

For example:

```text
novels/qingheng/
```

is a test novel instance. It should not define the whole repository's direction.

## Rule Placement

Rules that apply to all fiction projects must live in generic locations such as:

```text
prompts/
governance/
docs/
```

Rules that apply only to one test novel should live inside that novel's directory:

```text
novels/<novel_id>/wiki/
```

## Do Not Confuse Levels

Do not turn a test novel's local setting, terminology, or arc design into a global rule.

Global rules may include:

- outline-first workflow
- chapter brief gate
- terminology clarity
- low-anchor phrase checks
- anti-repetition checks
- character concealment checks
- continuity state updates

Local test-novel rules may include:

- specific sect names
- specific character names
- specific cultivation rules
- specific chapter beats
- specific glossary entries

## Correct Mental Model

The workflow should be topic-neutral and genre-neutral by default.

A novel instance supplies its own genre, world, characters, glossary, body state, and beats.

Generic prompts should not hard-code a specific test novel's content.
