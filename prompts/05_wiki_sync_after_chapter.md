# Wiki Sync After Chapter Prompt

Use this prompt immediately after a formal chapter draft is approved and before planning the next chapter.

The purpose is to keep the per-novel wiki synchronized with approved prose, so the next chapter reads canon rather than relying on chat memory.

Fast Trial sketches are non-canon and must not use this prompt.

## Core Principle

```text
Approved formal chapter -> wiki sync -> next chapter.
```

Do not plan or draft the next formal chapter until chapter state and relevant wiki updates are written or explicitly rejected by the user.

## Chapter State File Status Rule

Only this file unlocks the next formal chapter:

```text
novels/<novel_id>/wiki/chapter_states/chapter_<number>.md
```

Pending or review-state files do not unlock the next chapter:

```text
chapter_<number>_pending.md
chapter_<number>_review.md
chapter_<number>_revise.md
```

If a pending state exists, it must be converted into `chapter_<number>.md` only after the chapter is formally approved and this sync prompt has passed.

## Required Inputs

Read:

- approved chapter draft;
- previous approved chapter state if present;
- current `project.md`;
- current `base_settings.md`;
- current `protagonist_growth.md`;
- irreversible trend anchor from project wiki or `prompts/00_irreversible_trend_anchor.md` output;
- relevant character files;
- relevant organization / world files;
- `style.md`;
- `name_registry.md`;
- `prompts/00_webnovel_pleasure_ladder.md` output as Reader Hook / Payoff Ladder if available;
- `prompts/02_advantage_reward_ledger.md` evaluation summary if available;
- `governance/wiki_write_rules.md`.

## Responsibility Boundary

```text
Advantage And Reward Ledger = evaluates whether gain / payoff / debt / pressure / repetition exist.
Wiki Sync = copies confirmed results into canonical wiki state.
```

Do not redo the full ledger here.

If the ledger exists, use its `Carry Forward To Wiki Sync` section as the source for:

- confirmed usable advantage;
- confirmed final-form asset;
- confirmed reader hook/payoff;
- confirmed reader reward;
- confirmed reader debt;
- confirmed pressure clock;
- confirmed repetition risk;
- confirmed Earth / civilization asset.

If the ledger is absent, create only the minimal confirmed state from the approved chapter. Do not infer unshown rewards or debts.

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

Each approved `chapter_<number>.md` must include:

- chapter title;
- chapter function;
- confirmed events;
- world / civilization trend progress;
- Earth status progress when relevant;
- protagonist final-form progress;
- confirmed usable advantage;
- confirmed final-form asset;
- reader hook / payoff delivered;
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
- world trend progress vs worldbuilding exposition;
- Earth status progress vs Earth nostalgia;
- protagonist final-form progress vs ordinary clue gain;
- reader hook/payoff delivered vs reusable protagonist asset;
- reader debt vs confirmed canon;
- pressure clock vs completed event;
- repetition risk vs style preference.

## Irreversible Trend Sync Rules

World trend progress, Earth status progress, and protagonist final-form progress are planning / structure state. They are written into chapter state to keep long-form direction stable.

They must not be treated as character knowledge unless the approved prose confirms that a character knows it.

### World / Civilization Trend Progress

Record how the chapter moves the world or civilization trend forward.

This can be small:

- a symptom becomes visible;
- a normal institution fails to explain something;
- an organization begins reacting;
- ordinary life changes slightly;
- a hidden pressure reaches the protagonist's level;
- public denial becomes harder;
- a high-civilization actor changes behavior;
- a faction evaluation changes.

Do not record vague worldbuilding. Record concrete movement.

### Earth Status Progress

Required for Earth-entry / Earth-protection / macro modern-to-cosmic stories.

Record how Earth status changes or is pressured:

- Earth remains unregistered but is observed;
- Earth enters a provisional evaluation;
- Earth gains a witness, advocate, risk, score, warning, or hidden protection;
- a faction misjudges Earth;
- the protagonist provides evidence that Earth should be reevaluated;
- Earth becomes more exposed to danger.

Do not record nostalgia as Earth status progress.

### Protagonist Final-Form Progress

Record how the chapter moves the protagonist toward the final form.

This can be small:

- gains a verification method;
- gains a relationship or debt;
- learns a rule;
- preserves a person/object/route;
- pays a cost for helping;
- becomes slightly more responsible;
- gains a team seed;
- gains a cross-system translation insight;
- gains a resource, qualification, or status that can matter later;
- understands that personal survival is not enough.

Do not record random clues as final-form progress unless they change future action.

## Reader Hook / Payoff Sync Rules

Reader hook/payoff is planning state, not hidden canon.

It must be recorded so the next chapter does not repeat the same hook, delay payoff too long, or force face-slapping where another hook would be more natural.

Record:

- primary hook type;
- specific question, crisis, choice, relationship tension, world reveal, mechanism reveal, or visible gain;
- small payoff delivered;
- new question or pressure opened;
- whether face-slapping was used;
- if face-slapping was used, who was corrected and why it was natural;
- what the next hook/payoff escalation should be.

Do not count vague praise, secret admiration, exposition, or broad mystery as delivered hook/payoff.

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
- same chapter ending shape;
- same face-slapping target type;
- same reward type;
- same hook type.

The next chapter constraint should say what must change if repetition risk remains.

## Output Format

```text
# Wiki Sync After Chapter

Novel ID:
Chapter number:
Approved draft source:
Previous approved chapter state read: yes / no
Ledger summary read: yes / no
Sync decision: ALLOW / REVISE

## 1. Chapter State File

Path:

Content draft:

Required fields in content draft:
- chapter title:
- chapter function:
- confirmed events:
- world / civilization trend progress:
- Earth status progress if relevant:
- protagonist final-form progress:
- confirmed usable advantage:
- confirmed final-form asset:
- reader hook / payoff delivered:
- protagonist state:
- organization state:
- character state:
- key object / resource state:
- reader reward delivered:
- reader debt:
- pressure clock:
- repetition risk:
- unresolved questions:
- next chapter constraints:
- useful next-chapter attractor:

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
Type: rule / local practice / one-time action / resource state / place state / status evaluation / faction behavior / other
Should update file? yes / no

## 4. Protagonist Growth Update

Active stage:
Cost paid:
Confirmed usable leverage gained:
Confirmed final-form asset gained or strengthened:
Capability changed? yes / no
Access changed? yes / no
Relationship changed? yes / no
Earth / civilization asset changed? yes / no
Forbidden jump avoided? yes / no
Should update `protagonist_growth.md`? yes / no

## 5. Irreversible Trend Updates

World / civilization trend progress:
Earth status progress if relevant:
Protagonist final-form progress:
Coupling among trend, Earth, and protagonist:
What became irreversible this chapter:
What must carry into next chapter:

## 6. Reader Hook / Payoff Delivered

Primary hook type:
Specific question / crisis / choice / relationship / reveal:
Small payoff delivered:
New question or pressure opened:
Visible gain, if any:
Was face-slapping used? yes / no
If yes, who was corrected and why it was natural:
Next hook/payoff escalation:

## 7. Timeline / Relationship / Foreshadowing Updates

Timeline update:
Relationship update:
Foreshadowing update:
Name registry update:
Style update:

## 8. Reader Debt / Pressure / Repetition Updates

Reader debt paid or partially paid:
Reader debt created or carried:
Debt that cannot be delayed much longer:
Pressure clock advanced:
Pressure that worsened:
Repetition risk from this chapter:
Required structural change next chapter:

## 9. Next Chapter Constraints

Must continue from:
Must not contradict:
Must not escalate yet:
Required unresolved pressure:
Required structural upgrade:
Suggested next attractor:
Required hook/payoff escalation:

## 10. Missing / Unsafe Updates

- candidate update:
  reason not written:
```

## Hard Checks

Mark `REVISE` if:

- chapter state path is not `chapter_<number>.md` for an approved formal chapter;
- chapter state is missing;
- a pending / review / revise state is used to unlock next chapter;
- world / civilization trend progress is missing from an important chapter state;
- Earth status progress is missing from a relevant macro chapter state;
- protagonist final-form progress is missing from a protagonist-centered chapter state;
- confirmed usable advantage is missing when the chapter requires protagonist gain;
- confirmed final-form asset is missing from a protagonist-centered chapter;
- reader hook/payoff delivered is missing from an important chapter state;
- updates include speculation or inferred secrets;
- protagonist growth is recorded without concrete cost or usable leverage;
- final-form progress is recorded as a random clue with no next-action value;
- reader hook/payoff is recorded as vague praise, secret admiration, broad mystery, or exposition;
- reader debt / pressure clock / repetition risk are missing from an important chapter state;
- a one-time action is written as a permanent trait;
- an organization agent's local action is written as full organization policy without proof;
- a reference-setting idea is written as canon without appearing in the approved chapter;
- next chapter constraints are missing;
- the next chapter has no required structural upgrade after repeated scene pattern;
- the next chapter does not carry forward the irreversible trend;
- the next chapter would need to rely on chat memory rather than wiki state.
