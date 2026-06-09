# Reference Settings

This directory stores reusable reference material for AI-assisted Chinese webnovel creation.

Reference settings are not canon for any novel.

They provide reusable boundaries for genre, identity, authority, organizations, processes, resources, objects, social life, power systems, and language register. They should help generate a specific novel's `wiki/base_settings.md`, but they must not be copied into a novel wiki as confirmed facts.

## Scope

Use this directory for generic and genre-neutral or genre-common material only.

Do not derive global rules from any test novel under `novels/`.

Existing novel instances are regression examples and workflow tests. They are not the source of system direction.

## Intended Flow

```text
project scope
-> type contract / novel spine
-> select reference settings
-> build novels/<novel_id>/wiki/base_settings.md
-> reader entry gate
-> opening chapter brief
-> draft
-> review
-> canon update
```

## Rules

1. Reference settings provide boundaries, not plot.
2. A reference entry becomes canon only after the novel-specific base settings file confirms it.
3. If a needed institution, rule, resource, or process is not supported by the selected reference material or the user's input, record it as a pending setting gap.
4. Do not turn local opening conditions into whole-world permanent rules.
5. Do not import a power system, goldfinger, anomaly, or supernatural rule unless the project explicitly has one.
6. Keep the generated novel-specific base settings short enough to guide writing.

## Files

```text
reference_settings/
  usage_contract.md
  index.json
  genre_common/
  power_system_common/
```
