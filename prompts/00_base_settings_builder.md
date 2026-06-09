# Base Settings Builder Prompt

Use this prompt after the project scope, type contract, and novel spine are approved, and before the reader entry gate or chapter brief.

The purpose is to build the novel-specific base settings for the opening and first volume.

Do not write prose.
Do not write chapter beats.
Do not write a full world encyclopedia.
Do not treat reference settings as canon.
Do not derive global rules from existing test novels.

## Required Inputs

Read:

- approved project scope
- approved type contract if present
- approved novel spine or project outline
- approved name registry or initial term list if present
- `reference_settings/usage_contract.md`
- `reference_settings/index.json`
- selected reference setting files relevant to the declared genre and mechanism

## Task

Create a short, usable, novel-specific `wiki/base_settings.md` draft.

The base settings should define only the boundaries that the opening and first volume need for stable writing.

It should answer:

1. What genre promise must the setting support?
2. What identities, roles, or authority limits matter early?
3. What organizations, institutions, or processes matter early?
4. What resources, objects, documents, tools, or access rights matter early?
5. What spaces or locations matter early?
6. What social-life or language-register rules matter early?
7. If a power, anomaly, goldfinger, system, or special mechanism exists, what are its current-stage boundaries?
8. What does the reader know, what does the protagonist know, and what remains unknown?
9. What setting moves are forbidden because they would break genre, logic, authority, or canon safety?
10. What important setting gaps remain unresolved?

## Core Rules

- Build from approved project inputs first, reference settings second.
- Reference settings provide boundaries, not plot.
- A reference setting becomes novel-specific only when this output accepts it.
- Do not import unused genre material.
- Do not create institutions, roles, processes, resources, or power rules that are not supported by input or selected reference settings.
- If a needed rule has insufficient support, write it under `pending_setting_gaps`.
- Keep the scope to opening and first volume unless the user explicitly asks for whole-book settings.
- Do not turn local opening conditions into whole-world permanent law.
- Avoid absolute claims unless the project requires them.
- Do not add power-system, goldfinger, anomaly, or supernatural rules to projects that do not explicitly contain them.
- Do not create new side effects, counters, hidden costs, or extra mechanism functions beyond approved inputs.
- Do not decide concrete chapter outcomes, deaths, victories, recruitment, betrayals, or final solutions.
- Do not over-explain. Settings should guide writing, not replace scene generation.

## Output Format

Output only the base settings draft in this format:

```text
# Base Settings

Novel ID:
Scope: opening_and_volume_1
Reference settings used:

## Genre Foundation
Primary genre:
Secondary genre if any:
Reader promise:
Setting must support:
Setting must not replace:

## Identity And Authority Rules
- Rule:
  Applies to:
  Writing use:
  Limit:

## Organization And Process Rules
- Rule:
  Applies to:
  Required support:
  Writing use:
  Limit:

## Resource And Object Rules
- Rule:
  Applies to:
  Source / holder:
  Writing use:
  Limit:

## Space And Location Rules
- Rule:
  Applies to:
  Access / route / restriction:
  Writing use:
  Limit:

## Social Life And Language Rules
- Rule:
  Applies to:
  Writing use:
  Limit:

## Power / Anomaly / Goldfinger Rules
Use this section only if the project explicitly has such a mechanism.

- Mechanism:
  Reader-known rule:
  Protagonist-known rule:
  Other-character visible result:
  Source or binding:
  Current-stage ability:
  Current-stage limit:
  Failure mode:
  Counter / pressure:
  Forbidden uses:
  Disclosure stage:

## Knowledge Boundary Rules
- Reader knows:
  Protagonist knows:
  Other characters know:
  Institutions can verify:
  Unknown remains:

## Forbidden Setting Moves
1.
2.
3.

## Pending Setting Gaps
- Gap:
  Why unresolved:
  When to resolve:
```

If a section is not applicable, write `None for current opening scope.` Do not leave it ambiguous.
