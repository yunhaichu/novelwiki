# Wiki Bootstrap Prompt

Use this prompt immediately after formal new-novel setup outputs are approved and before any formal chapter drafting.

The purpose is to create the initial per-novel wiki in the same workflow run as project setup, instead of relying on later manual patching.

Fast Trial sketches are non-canon and must not use this prompt unless the user decides to build the full novel wiki.

## Core Principle

```text
No wiki, no formal draft.
No name gate, no project file.
```

A new formal novel must not move into chapter design until its core setup has been written into `novels/<novel_id>/wiki/`.

A new novel must not write `project.md` with protagonist, organization, city, or key term names until the names pass the Name Gate.

## Required Inputs

Read:

- novel spine;
- genre mode contract;
- genre operating model;
- irreversible trend anchor;
- reality-causal preflight for opening event family;
- base settings;
- major conflict engine;
- dramatic arena;
- protagonist growth track;
- Reader Hook / Payoff Ladder if available;
- organization behavior models for major organizations;
- character behavior models, expression cards, and cognition cards for major recurring characters;
- style / name constraints if present;
- existing `novels/*/wiki/name_registry.md` files when available;
- existing project names and recurring names in this repository when available.

## Name Gate

Run this before writing `project.md`, character files, organization files, or chapter drafts.

Names are not decorative labels. They are part of the world model. A name should grow from:

- time period;
- region / migration background;
- class and family education;
- occupation;
- registration system;
- corporate, sect, state, clan, or platform naming rules;
- nickname practices;
- whether the character uses legal name, work name, handle, number, alias, or street name.

### Required Name Gate Output

```text
## Name Gate

Naming context:
- genre:
- region / city / social layer:
- naming institution or family practice:
- legal-name vs nickname vs handle rules:

Protagonist name candidates:
1.
2.
3.
...

Rejected names:
- name:
  reason:

Selected protagonist name:
Why this name fits world / family / class / job:
AI-default risk: low / medium / high
Previously used in this repository or current conversation: yes / no

Organization / city / key term candidates:
-

Approved names to write into name_registry.md:
-

Avoided names to record:
-
```

### Common AI-Default Name Warning List

Treat these names and similar polished literary names as high risk unless the user explicitly chooses them or the setting provides a strong reason:

```text
沈砚
陆沉
顾言
林澈
江辰
谢沉
秦川
裴行
许知
宋临
周砚
陈述
苏晚
云棠
白芷
阮清
夏禾
许栀
云无尘
谢玄微
顾长渊
沈照霜
```

### Character-Level Risk Markers

If a name contains any of these characters, it should be flagged and reviewed:

```text
砚 澈 言 知 棠 芷 栀 辞 珩 璟 宸 玦 弈 晏 清 沉 辰 川 行 述 晚 玄 微 渊 照 霜
```

This is a broad filter. A flagged name can still pass if it has a strong family/world explanation. This list is synchronized with `tools/name_gate.py` — `POLISHED_RISK_CHARS` contains the same characters.

Also treat these patterns as high risk:

- overly polished two-character literary names with rare aesthetic characters;
- names that sound genre-neutral and model-favored rather than class / region / family grounded;
- protagonist names reused from earlier test novels;
- names that could fit any modern / xianxia / cyberpunk story without change.

### Name Gate Hard Rules

Mark `REVISE` if:

- protagonist name appears in `project.md` before the Name Gate;
- no rejected-name list exists;
- the selected name has no social / family / institutional explanation;
- the selected name is from the warning list without explicit user approval;
- the name is too polished and not grounded in the world;
- the same name or close variant already appears in another active test novel;
- organization / city names are generic genre labels rather than functional entities.

## Required Output Files

Create or update these files for every formal new novel:

```text
novels/<novel_id>/wiki/project.md
novels/<novel_id>/wiki/base_settings.md
novels/<novel_id>/wiki/style.md
novels/<novel_id>/wiki/name_registry.md
novels/<novel_id>/wiki/protagonist_growth.md
novels/<novel_id>/wiki/timeline.md
novels/<novel_id>/wiki/relationships.md
novels/<novel_id>/wiki/foreshadowing.md
novels/<novel_id>/wiki/reader_debt_tracker.md
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
- irreversible trend anchor reference;
- what this story is not;
- genre mode contract summary (reader promise, primary pressure carrier, what scenes feel off-genre);
- current development goal.

Do not write protagonist, organization, city, or key term names here until the Name Gate has passed.

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
- first-contact psychological realism if applicable;
- anti-AI notes.

### `name_registry.md`

Must include:

- Name Gate result;
- approved protagonist name;
- approved organizations;
- approved places;
- approved recurring character names;
- approved terms;
- rejected / avoided names and reasons;
- naming rules;
- pending / not-yet-canon names.

### `timeline.md`

Must start as a placeholder even if no chapters exist yet.

Must include:

```text
# Timeline

Status: initialized

## Confirmed Timeline

- None yet.

## Pending / Not Yet Canon

- None yet.
```

### `relationships.md`

Must start as a placeholder even if no relationship state exists yet.

Must include:

```text
# Relationships

Status: initialized

## Confirmed Relationships

- None yet.

## Tension / Debt / Trust Pending

- None yet.
```

### `foreshadowing.md`

Must start as a placeholder even if no foreshadowing exists yet.

Must include:

```text
# Foreshadowing

Status: initialized

## Active Questions

- None yet.

## Planted Objects / Lines / Events

- None yet.

## Answered / Closed

- None yet.
```


### `genre_mode` (inline in project.md)

Must include:

- genre mode (from genre_mode_contract);
- subgenre / flavor;
- primary pressure carrier (what should carry tension in this genre);
- what kind of scene makes readers continue;
- what kind of scene feels off-genre;
- key genre-specific forbidden moves.

This section ensures the genre constraints generated by `genre_mode_contract` are persisted in project.md and remain available to every downstream prompt.

### Actor / Organization Files

Each important character / organization file must include:

- identity;
- story function;
- current status;
- default behavior;
- cognition boundary if relevant;
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

## Name Gate

Naming context:
Protagonist name candidates:
Rejected names:
Selected protagonist name:
Why selected name fits:
AI-default risk:
Previously used in repository or current conversation:
Approved names:
Avoided names:
Name gate decision: ALLOW / REVISE

## Files To Create / Update

- path:
  purpose:
  source material:
  canon confidence:

## Required Core Files Checklist

- project.md created / updated: yes / no
- base_settings.md created / updated: yes / no
- style.md created / updated: yes / no
- name_registry.md created / updated: yes / no
- protagonist_growth.md created / updated: yes / no
- timeline.md placeholder created / updated: yes / no
- relationships.md placeholder created / updated: yes / no
- foreshadowing.md placeholder created / updated: yes / no
- reader_debt_tracker.md placeholder created / updated: yes / no
- draft_quality_log.md placeholder created / updated: yes / no
- initial character files created / updated: yes / no
- initial organization / world files created / updated: yes / no
- chapter_states directory ready: yes / no
- drafts directory ready: yes / no

## Missing Setup Inputs

- missing:
  why needed:
  can proceed? yes / no

## Canon Boundary Notes

- reference setting ideas not yet canon:
- inferred secrets not to write:
- pending names / terms:
```

## Hard Checks

Mark `REVISE` if:

- the setup has no novel ID;
- protagonist or major organization names appear before Name Gate;
- Name Gate is missing or fails;
- base settings are too vague to constrain chapter design;
- genre operating model is absent;
- protagonist growth stages are absent;
- style / name rules are absent;
- timeline.md, relationships.md, or foreshadowing.md are missing from formal wiki bootstrap;
- important actors appear in chapter planning without wiki files;
- reference settings are copied as canon without novel-specific acceptance;
- inferred secrets are written as confirmed canon.
