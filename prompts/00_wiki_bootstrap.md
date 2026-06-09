# Wiki Bootstrap Prompt

Use this prompt immediately after new-novel setup outputs are approved and before any chapter drafting.

The purpose is to create the initial per-novel wiki in the same workflow run as project setup, instead of relying on later manual patching.

## Core Principle

```text
No wiki, no draft.
```

A new novel must not move into chapter design until its core setup has been written into `novels/<novel_id>/wiki/`.

## Required Inputs

Read:

- novel spine;
- genre mode contract;
- genre operating model;
- reality-causal preflight for opening event family;
- base settings;
- major conflict engine;
- dramatic arena;
- protagonist growth track;
- organization behavior models for major organizations;
- character behavior models and expression cards for major recurring characters;
- style / name constraints if present.

## Required Output Files

Create or update these files for every new novel:

```text
novels/<novel_id>/wiki/project.md
novels/<novel_id>/wiki/base_settings.md
novels/<novel_id>/wiki/style.md
novels/<novel_id>/wiki/name_registry.md
novels/<novel_id>/wiki/protagonist_growth.md
```

Create these directories / files as needed:

```text
novels/<novel_id>/wiki/world/
novels/<novel_id>/wiki/characters/
novels/<novel_id>/wiki/organizations/
novels/<novel_id>/wiki/chapter_states/
novels/<novel_id>/drafts/
```

For important initial actors, create:

```text
novels/<novel_id>/wiki/characters/<character_id>.md
```

For important initial organizations / systems, create:

```text
novels/<novel_id>/wiki/world/<system_or_place_id>.md
```

or:

```text
novels/<novel_id>/wiki/organizations/<organization_id>.md
```

Use whichever path is more consistent with the project.

## File Content Requirements

### `project.md`

Must include:

- novel ID;
- status;
- type promise;
- core reader promise;
- protagonist;
- core contradiction;
- story engine;
- what this story is not;
- current development goal.

### `base_settings.md`

Must include:

- genre foundation;
- core operating logic;
- identity / authority / hierarchy rules;
- resource rules;
- process rules;
- power / anomaly / goldfinger boundary if applicable;
- opening location rules;
- survival / body / time constraints;
- social behavior rules;
- opening chapter constraints;
- forbidden setting moves;
- pending setting gaps.

### `protagonist_growth.md`

Must include:

- initial position;
- current weakness;
- useful starting skill;
- starting misconception;
- starting fear;
- large trend pressure;
- growth direction;
- growth stages;
- growth asset ladder;
- invisible hand rule;
- chapter-one contract if writing opening.

### `style.md`

Must include:

- prose direction;
- opening texture;
- language rules;
- dialogue rules;
- special ability / goldfinger presentation if applicable;
- anti-AI notes.

### `name_registry.md`

Must include:

- approved protagonist name;
- approved organizations;
- approved places;
- approved recurring character names;
- approved terms;
- naming rules;
- pending / not-yet-canon names.

### Actor / Organization Files

Each important character / organization file must include:

- identity;
- story function;
- current status;
- default behavior;
- environmental modulation;
- voice / presentation rules;
- confirmed state;
- not-yet-confirmed boundaries.

## Output Format

```text
# Wiki Bootstrap Plan

Novel ID:
Source setup files read:
Bootstrap decision: ALLOW / REVISE

## Files To Create / Update

- path:
  purpose:
  source material:
  canon confidence:

## Missing Setup Inputs

- missing:
  why needed:
  can proceed? yes / no

## Canon Boundary Notes

- reference setting ideas not yet canon:
- inferred secrets not to write:
- pending names / terms:

## Completion Checklist

- project.md created / updated: yes / no
- base_settings.md created / updated: yes / no
- style.md created / updated: yes / no
- name_registry.md created / updated: yes / no
- protagonist_growth.md created / updated: yes / no
- initial character files created / updated: yes / no
- initial organization / world files created / updated: yes / no
- chapter_states directory ready: yes / no
- drafts directory ready: yes / no
```

## Hard Checks

Mark `REVISE` if:

- the setup has no novel ID;
- base settings are too vague to constrain chapter design;
- genre operating model is absent;
- protagonist growth stages are absent;
- style / name rules are absent;
- important actors appear in chapter planning without wiki files;
- reference settings are copied as canon without novel-specific acceptance;
- inferred secrets are written as confirmed canon.
