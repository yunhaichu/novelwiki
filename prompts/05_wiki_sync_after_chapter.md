# Wiki Sync After Chapter Prompt

Use this prompt immediately after a chapter draft is approved and before planning the next chapter.

The purpose is to keep the per-novel wiki synchronized with approved prose, so the next chapter reads canon rather than relying on chat memory.

## Core Principle

```text
Approved chapter -> wiki sync -> next chapter.
```

Do not plan or draft the next chapter until chapter state and relevant wiki updates are written or explicitly rejected by the user.

## Required Inputs

Read:

- approved chapter draft;
- previous chapter state if present;
- current `project.md`;
- current `base_settings.md`;
- current `protagonist_growth.md`;
- relevant character files;
- relevant organization / world files;
- `style.md`;
- `name_registry.md`;
- `prompts/02_advantage_reward_ledger.md` output if available;
- `governance/wiki_write_rules.md`.

## Output Targets

Always create or update:

```text
novels/<novel_id>/wiki/chapter_states/chapter_<number>.md
```

Update when new confirmed information appears:

```text
novels/<novel_id>/wiki/characters/<character_id>.md
novels/<novel_id>/wiki/world/<system_or_place_id>.md
novels/<novel_id>/wiki/organizations/<organization_id>.md
novels/<novel_id>/wiki/protagonist_growth.md
novels/<novel_id>/wiki/timeline.md
novels/<novel_id>/wiki/relationships.md
novels/<novel_id>/wiki/foreshadowing.md
novels/<novel_id>/wiki/name_registry.md
novels/<novel_id>/wiki/style.md
```

Only update `base_settings.md` when the approved chapter establishes a durable world rule, not a one-time event.

## Chapter State Required Content

Each `chapter_<number>.md` must include:

- chapter title;
- chapter function;
- confirmed events;
- protagonist state;
- organization state;
- character state;
- key object / resource state;
- reader reward delivered;
- reader debt;
- pressure clock;
- repetition risk;
- unresolved questions;
- next chapter constraints;
- useful next-chapter attractor.

## Canon Update Rules

Write only confirmed facts from approved prose.

Do not write:

- speculation;
- inferred secrets;
- reader-only interpretation;
- temporary options not chosen;
- possible future twists;
- reference-setting ideas not used in the prose;
- model assumptions.

Distinguish:

- default behavior vs one-time action;
- environment-modulated behavior vs personality change;
- organizational rule vs local agent action;
- public status vs private knowledge;
- known fact vs unresolved question;
- foreshadowing object vs ordinary detail;
- reader debt vs confirmed canon;
- pressure clock vs completed event;
- repetition risk vs style preference.

## Reader Debt / Pressure / Repetition Rules

Reader debt, pressure clock, and repetition risk are planning state, not hidden canon.

They may be written into chapter state because they guide the next chapter, but they must not be treated as in-world facts known by characters.

### Reader Debt

Record only story-facing debts that affect future pacing:

- unanswered protagonist-bound questions;
- promises created by prior chapters;
- emotional or relationship expectations;
- ability / resource / status questions that need payoff.

Do not record vague mysteries such as `the truth of the world` unless they create a concrete next action.

### Pressure Clock

Record only pressures that will force action if ignored:

- deadlines;
- resource depletion;
- bodily deterioration;
- institutional review;
- scheduled test / hearing / mission / inspection;
- relationship limit;
- exposure risk;
- pursuit or escalation.

### Repetition Risk

Record repeated scene patterns that must be upgraded or avoided next:

- same location;
- same task;
- same conflict shape;
- same ability trigger;
- same conversation rhythm;
- same consequence pattern;
- same chapter ending shape.

The next chapter constraint should say what must change if repetition risk remains.

## Output Format

```text
# Wiki Sync After Chapter

Novel ID:
Chapter number:
Approved draft source:
Previous chapter state read: yes / no
Sync decision: ALLOW / REVISE

## 1. Chapter State File

Path:

Content draft:

## 2. Character Updates

Character:
Path:
Confirmed update:
Type: default behavior / one-time action / relationship state / knowledge state / status state / other
Should update file? yes / no

## 3. Organization / World Updates

Entity:
Path:
Confirmed update:
Type: rule / local practice / one-time action / resource state / place state / other
Should update file? yes / no

## 4. Protagonist Growth Update

Active stage:
Cost paid:
Usable leverage gained:
Capability changed? yes / no
Access changed? yes / no
Relationship changed? yes / no
Forbidden jump avoided? yes / no
Should update `protagonist_growth.md`? yes / no

## 5. Timeline / Relationship / Foreshadowing Updates

Timeline update:
Relationship update:
Foreshadowing update:
Name registry update:
Style update:

## 6. Reader Debt / Pressure / Repetition Updates

Reader debt paid or partially paid:
Reader debt created or carried:
Debt that cannot be delayed much longer:
Pressure clock advanced:
Pressure that worsened:
Repetition risk from this chapter:
Required structural change next chapter:

## 7. Next Chapter Constraints

Must continue from:
Must not contradict:
Must not escalate yet:
Required unresolved pressure:
Required structural upgrade:
Suggested next attractor:

## 8. Missing / Unsafe Updates

- candidate update:
  reason not written:
```

## Hard Checks

Mark `REVISE` if:

- chapter state is missing;
- updates include speculation or inferred secrets;
- protagonist growth is recorded without concrete cost or usable leverage;
- reader debt / pressure clock / repetition risk are missing from an important chapter state;
- a one-time action is written as a permanent trait;
- an organization agent's local action is written as full organization policy without proof;
- a reference-setting idea is written as canon without appearing in the approved chapter;
- next chapter constraints are missing;
- the next chapter has no required structural upgrade after repeated scene pattern;
- the next chapter would need to rely on chat memory rather than wiki state.
