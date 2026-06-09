# Reference Settings Usage Contract

This contract defines how reusable reference settings may be used when building a novel-specific `wiki/base_settings.md`.

## Purpose

Reference settings provide reusable boundaries for:

- genre promise support
- identity and authority
- organization and process
- resource and object logic
- space and location constraints
- social life and language register
- power, anomaly, or goldfinger boundaries when applicable

They do not replace story creation, character action, reader entry, scene simulation, or canon review.

## Global Rules

1. Select reference settings according to the project's declared genre, era, world background, and explicit user constraints.
2. Read only modules touched by the current project. Do not inject unrelated genre material.
3. Reference settings are not canon. They become canon only after a novel-specific base settings file accepts them.
4. Do not create an institution, authority, process, resource, ability, or social rule as already existing unless the project input or selected reference material supports it.
5. If support is insufficient, record a pending setting gap instead of inventing a fact.
6. Base settings should cover the opening and first volume only unless the user explicitly asks for a whole-book setting bible.
7. Do not turn a local condition into a universal permanent rule.
8. Avoid absolute language such as all, always, never, completely, inevitably, or no one unless the project explicitly requires such a rule.
9. Do not use a test novel under `novels/` as a source for global rules.
10. Do not import power-system logic into a realistic project that explicitly has no power system, goldfinger, anomaly, or supernatural element.

## Selection Rules

Use the smallest suitable set of reference libraries.

```text
modern_common: modern, urban, workplace, business, school, family, realistic rebirth
apocalypse_common: apocalypse, zombie, disaster, wasteland, survival camp, collapse
xianxia_common: cultivation, xianxia, xuanhuan, sect, spiritual resources
sci_fi_cyber_common: science fiction, cyberpunk, future technology, AI, platform control
historical_period: specific historical era or premodern bureaucracy / military / social setting
generic_common: original fantasy or unspecified genre foundation
power_system_common: overlay only when a project has power, anomaly, goldfinger, system, supernatural, or technology ability rules
```

## Module Types

A reference library may contain any of these module types.

### identity_and_authority

Use when the story needs roles, rank, job limits, status, jurisdiction, or social authority.

Check that low-level characters do not perform high-level actions without leverage, access, permission, fraud, crisis conditions, or visible cost.

### organization_and_process

Use when the story needs institutions, workflows, approval chains, investigation, assignment, audit, exchange, reward, trial, or punishment.

A process should name the support required for its result to become visible.

### resource_and_object

Use when money, records, documents, tools, equipment, supplies, access, credentials, maps, tokens, or scarce materials affect the plot.

A resource should have a source, holder, use, limit, and risk if it matters to the chapter.

### space_and_location

Use when movement, jurisdiction, access, distance, terrain, route, territory, building layout, station, camp, sect area, city district, or restricted zone matters.

### social_life

Use when daily life, class, family, reputation, custom, service roles, local speech, or ordinary objects shape character action.

### language_and_genre_guard

Use to prevent tone mismatch, anachronism, game-like labels, pseudo-technical terms, fake ancient style, or genre leakage.

### power_or_anomaly

Use only when the project explicitly includes a power system, goldfinger, anomaly, supernatural force, system panel, special technology, rebirth memory, or rule-based ability.

The key fields are source, basic law, visible effect, limit, counter, reader knowledge, character knowledge, and stage of disclosure.

## Base Settings Output Requirement

A novel-specific base settings file should include:

```text
Genre foundation
Identity and authority rules
Organization and process rules
Resource and object rules
Space and location rules
Social life rules
Power / anomaly rules if any
Knowledge boundary rules
Language and term rules
Forbidden setting moves
Pending setting gaps
```

## Review Principle

If a draft uses a reference setting that has not been accepted into the novel-specific base settings or confirmed by approved prose, treat it as unconfirmed and mark the relevant planning or draft step for revision.
