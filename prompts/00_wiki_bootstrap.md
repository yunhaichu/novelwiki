# Wiki Bootstrap Prompt

Use this prompt immediately after formal new-novel setup outputs are approved and before any formal canon-dependent discussion, design, or generation.

The purpose is to create the initial per-novel wiki in the same workflow run as project setup, instead of relying on later manual patching.

Fast Trial sketches are non-canon and must not use this prompt unless the user decides to build the full novel wiki.

## Core Principle

```text
No wiki, no formal canon-dependent generation.
No name gate, no recurring invented name or term enters canon.
```

A new formal novel must not move into canon-dependent design until its core setup has been written into `novels/<novel_id>/wiki/`.

A new novel must not write recurring character, organization, location, rule-system, item, role, title, or key term names into canon until those names pass the Name Gate or the user explicitly approves them.

## Required Inputs

Read:

- novel spine;
- genre mode contract;
- genre operating model;
- irreversible trend anchor;
- reality-causal preflight for the first major event family when available;
- base settings;
- major conflict or pressure engine;
- dramatic arena;
- growth track when the project depends on a central growth route;
- Reader Hook / Payoff Ladder if available;
- behavior models for important entities when available;
- expression or cognition cards for important speaking / acting entities when available;
- style / name constraints if present;
- `docs/narrative_model.md`;
- existing `novels/*/wiki/name_registry.md` files when available;
- existing project names and recurring names in this repository when available.

## Name Gate

Run this before writing project files, entity files, relationship files, event records, or formal drafts that rely on recurring invented names or terms.

Names are not decorative labels. They are part of the story model. A name should grow from:

- time period;
- region / migration background;
- class and family education;
- occupation;
- registration system;
- organization, institution, clan, platform, workplace, title, or role naming rules;
- nickname practices;
- whether the entity uses legal name, work name, handle, number, alias, title, or public label.

### Required Name Gate Output

```text
## Name Gate

Naming context:
- genre:
- region / social layer:
- naming institution or family practice:
- legal-name vs nickname vs handle vs title rules:

Candidate names or terms:
1.
2.
3.
...

Rejected names or terms:
- name / term:
  reason:

Selected names or terms:
- name / term:
  why it fits the world / function / social layer / role:
  AI-default risk: low / medium / high
  previously used in this repository or current conversation: yes / no

Approved names and terms to write into name_registry.md:
-

Avoided names and terms to record:
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

If a name contains any of these characters, it should be flagged and checked:

```text
砚 澈 言 知 棠 芷 栀 辞 珩 璟 宸 玦 弈 晏 清 沉 辰 川 行 述 晚 玄 微 渊 照 霜
```

This is a broad filter. A flagged name can still pass if it has a strong family, world, class, role, or institutional explanation. This list is synchronized with `tools/name_gate.py` — `POLISHED_RISK_CHARS` contains the same characters.

Also treat these patterns as high risk:

- overly polished two-character literary names with rare aesthetic characters;
- names that sound model-favored rather than class / region / family / role grounded;
- recurring names reused from earlier test novels without reason;
- names that could fit many unrelated genres without change.

### Name Gate Hard Rules

Mark `REVISE` if:

- recurring names or terms appear in canon files before the Name Gate;
- no rejected-name list exists for important names;
- the selected name has no social / family / institutional / functional explanation;
- the selected name is from the warning list without explicit user approval;
- the name is too polished and not grounded in the world;
- the same name or close variant already appears in another active test novel without reason;
- organization / location / role / rule-system names are generic genre labels rather than functional entities.

## Required Output Files

Create or update these files for every formal new novel:

```text
novels/<novel_id>/wiki/project.md
novels/<novel_id>/wiki/base_settings.md
novels/<novel_id>/wiki/style.md
novels/<novel_id>/wiki/name_registry.md
novels/<novel_id>/wiki/timeline.md
novels/<novel_id>/wiki/relationships.md
novels/<novel_id>/wiki/foreshadowing.md
```

Create these directories for current narrative-model records:

```text
novels/<novel_id>/wiki/entities/
novels/<novel_id>/wiki/events/
novels/<novel_id>/wiki/states/
novels/<novel_id>/wiki/sessions/
novels/<novel_id>/wiki/mutations/
novels/<novel_id>/wiki/chapter_states/
novels/<novel_id>/drafts/
```

Optional project-specific files may be added when the project needs them:

```text
novels/<novel_id>/wiki/reader_debt_tracker.md
novels/<novel_id>/wiki/growth_track.md
novels/<novel_id>/wiki/rule_systems.md
novels/<novel_id>/wiki/locations.md
novels/<novel_id>/wiki/organizations.md
novels/<novel_id>/wiki/items.md
novels/<novel_id>/wiki/draft_quality_log.md
```

Do not force optional files into every project.

## File Content Requirements

### `project.md`

Must include:

- novel ID;
- status;
- type promise;
- core reader promise;
- central actor or viewpoint model when known;
- core contradiction;
- story engine;
- irreversible trend anchor reference;
- what this story is not;
- genre mode contract summary;
- current development goal.

Do not write recurring character, organization, location, rule-system, item, role, title, or key term names here until the Name Gate has passed or the user explicitly approves them.

### `base_settings.md`

Must include:

- genre foundation;
- core operating logic;
- identity / authority / hierarchy rules;
- resource rules;
- process rules;
- rule-system / special-mechanism boundary if applicable;
- opening location or initial situation rules;
- survival / body / time constraints if relevant;
- social behavior rules;
- initial unit constraints;
- forbidden setting moves;
- pending setting gaps.

### `style.md`

Must include:

- prose direction;
- opening texture;
- language rules;
- dialogue rules;
- special mechanism presentation if applicable;
- first-contact or unfamiliar-situation handling if applicable;
- anti-AI notes.

### `name_registry.md`

Must include:

- Name Gate result;
- approved recurring entity names;
- approved organizations;
- approved places;
- approved roles / titles;
- approved recurring terms;
- rejected / avoided names and reasons;
- naming rules;
- pending / not-yet-canon names.

### `timeline.md`

Must start as a placeholder even if no canonical events exist yet.

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

### Entity Records

Each important initial entity file should include:

```text
id:
type:
name:
summary:
related_entities:
source_sessions:
notes:
```

Use natural-language summary for most creative content. Do not split every trait, motive, resource, voice pattern, or function into narrow fields unless the project repeatedly needs to query it.

### Timepoint / State / Event Records

Create initial timepoint, state, and event records only when they are needed for the first canon-dependent discussion or generation.

Do not create empty record files just to satisfy a schema.

## Output Format

```text
# Wiki Bootstrap Plan

Novel ID:
Source setup files read:
Bootstrap decision: ALLOW / REVISE

## Name Gate

Naming context:
Candidate names or terms:
Rejected names or terms:
Selected names or terms:
Why selected names / terms fit:
AI-default risk:
Previously used in repository or current conversation:
Approved names / terms:
Avoided names / terms:
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
- timeline.md placeholder created / updated: yes / no
- relationships.md placeholder created / updated: yes / no
- foreshadowing.md placeholder created / updated: yes / no
- entities directory ready: yes / no
- events directory ready: yes / no
- states directory ready: yes / no
- sessions directory ready: yes / no
- mutations directory ready: yes / no
- chapter_states directory ready: yes / no
- drafts directory ready: yes / no

## Optional Files Created

- path:
  reason:

## Initial Entity / Event / State Records

- record:
  reason:

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
- recurring names or terms appear before Name Gate;
- Name Gate is missing or fails;
- base settings are too vague to constrain canon-dependent design;
- genre operating model is absent;
- style / name rules are absent;
- timeline.md, relationships.md, or foreshadowing.md are missing from formal wiki bootstrap;
- important entities appear in canon-dependent planning without wiki records;
- reference settings are copied as canon without novel-specific acceptance;
- inferred secrets are written as confirmed canon;
- optional files are forced into the project without need.