# Line Revision Prompt

Use this prompt when a chapter receives:

```text
Workflow decision: PASS
Prose decision: NEEDS LINE REVISION
```

The goal is not to change structure. The goal is to make the prose more natural inside the scene.

## Required Inputs

Read:

- the chapter draft
- the chapter review
- prose publishability review if present
- `governance/scene_naturalness_check.md`
- `governance/dialogue_pressure_check.md`
- `governance/in_world_naming_check.md`
- `governance/anti_ai_novel_phrase_check.md`
- `governance/low_anchor_phrase_check.md`
- current novel style file if present
- glossary / approved term list if present

## Revision Scope

Allowed:

- replace artificial terms with scene-natural wording;
- shorten or roughen in-world names;
- make dialogue more practical and pressure-driven;
- remove author-summary narration;
- replace polished endings with concrete action, object, cost, or changed relation;
- reduce forced jokes;
- compress explanation;
- preserve existing consequence chain.

Forbidden unless explicitly required:

- changing the chapter's main event;
- changing the approved beat;
- adding new canon facts;
- adding new characters;
- changing the ending hook's core function;
- expanding worldbuilding to explain a line.

## Line Revision Plan

Before revising, fill in:

```text
Structural material to preserve:
Artificial terms to revise:
Dialogue lines to revise:
Author-summary narration to revise:
Ending line risk:
Names / labels to localize:
Humor to keep:
Humor to cut or ground:
```

## Revision Rules

- Prefer ordinary scene wording over clever phrasing.
- Prefer what a character would say over what the author wants the reader to understand.
- Prefer rough local names over polished map or system labels.
- Let humor come from pressure, rank, mistake, or physical inconvenience.
- End on something visible whenever possible.

## Output

```text
Line revision plan:
Revised text:
Change notes:
```
