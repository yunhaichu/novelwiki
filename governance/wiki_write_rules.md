# Wiki Write Rules

## Canonical Source of Truth

The per-novel wiki is the canonical memory of a novel.

Formal canon comes from:

- approved formal chapter drafts;
- approved setup outputs written into wiki files;
- approved wiki sync outputs;
- user-approved corrections.

Planning files, Fast Trial sketches, review notes, and draft notes are not canon unless their content is explicitly accepted into the novel wiki.

## Planning Is Not Canon

Files under `planning/`, reviews, non-canon sketches, non-canon trial drafts, and working notes must not be used as confirmed story facts.

They may be used as:

- candidate ideas;
- rejected options;
- design reasoning;
- questions to resolve;
- temporary scaffolding.

They must not be treated as:

- confirmed events;
- confirmed character traits;
- confirmed world rules;
- confirmed timeline;
- confirmed relationship state;
- confirmed foreshadowing;
- confirmed protagonist growth.

If a planning file conflicts with an approved chapter state, use the approved chapter state.

If a draft changes a planning assumption, do not update the planning file just to keep it synchronized. Instead, record the confirmed result in `wiki/chapter_states/chapter_<number>.md` during wiki sync.

## What Can Be Written

Only write:

- confirmed facts;
- confirmed character traits;
- confirmed visual details;
- confirmed relationship changes;
- confirmed world rules;
- confirmed item states;
- confirmed chapter outcomes;
- confirmed behavior patterns supported by repeated action or approved initial settings;
- confirmed expression patterns supported by repeated speech or approved initial settings;
- confirmed threshold / override behavior only after source support or approved design;
- confirmed protagonist growth stage, cost, usable leverage, and final-form asset after approved chapter state;
- confirmed organization behavior patterns supported by approved settings, dramatic arena, or repeated chapter action;
- confirmed organization public legitimacy, real interests, action ladder, and agents when source-supported;
- reader hook/payoff, reader reward, reader debt, pressure clock, and repetition risk only as planning state inside chapter state, not as in-world facts.

## What Cannot Be Written

Do not write:

- speculation;
- guesses;
- unresolved secrets as facts;
- planning options as chosen events;
- non-canon trial material as canon;
- review suggestions as confirmed facts;
- temporary actions as permanent traits;
- one-off jokes as character personality;
- one-off panic as permanent cowardice;
- one-off courage as permanent bravery;
- future assumptions;
- unsupported catchphrases;
- unsupported dialect or speech quirks;
- unsupported environmental modulation;
- unsupported threshold reversal;
- unsupported protagonist growth not paid for by chapter cost or approved design;
- unsupported organization conspiracy;
- unsupported illegal organization methods;
- unsupported internal faction conflict;
- unsupported organization catchphrases or packaging language.

## Update Flow

1. Chapter written.
2. Chapter reviewed.
3. Advantage / reward ledger evaluated when needed.
4. Wiki update draft generated through `prompts/05_wiki_sync_after_chapter.md`.
5. Human approval.
6. Wiki updated.

## Source Discipline

Every important canon update should be traceable to one of:

- approved setup output;
- approved chapter prose;
- approved chapter state;
- direct user instruction.

If the source is uncertain, write it as pending or unresolved, not confirmed.

## Character Pages

Character pages must include:

- appearance;
- clothing;
- accessories;
- speech style;
- behavior style;
- fears;
- desires;
- weaknesses;
- capability boundaries.

Major and recurring character pages should also include the following behavior-generation fields.

### Perception Habits

- What they look at first in a scene.
- What they usually ignore.
- What abnormalities they are most sensitive to.
- What evidence they trust most.
- What claims they distrust.

### Judgment Habits

- Default judgment method.
- First reaction under incomplete information.
- Likely misjudgment.
- What they overestimate.
- What they underestimate.

### Environmental Modulation

A character trait is a default mode, not a fixed output.

Character pages should state how behavior changes under:

- weaker person;
- equal / peer;
- stronger person / authority;
- public setting;
- private setting;
- unknown / monster / anomaly;
- no escape route;
- core protected object threatened;
- violence / argument / money / status works;
- violence / argument / money / status fails;
- incomplete information;
- injury / exhaustion / fear.

### Threshold / Override Behavior

For major characters, record:

- core protected object;
- breaking point;
- conditions required to trigger override;
- conditions not enough to trigger override;
- override action style;
- limits that remain during override;
- cost and aftermath.

Example principle:

```text
A timid character may fight when a protected child is directly threatened.
A bully may collapse when facing an incomprehensible threat that makes intimidation useless.
A careless speaker may become careful in public when a wrong sentence harms someone important.
```

These are not out-of-character if the threshold is source-grounded.

### Embodied Behavior

Record how the character usually acts when:

- nervous;
- lying;
- controlling a situation;
- hiding information;
- protecting someone;
- trying to escape responsibility;
- facing authority;
- facing public scrutiny.

### Speech Modes

Record how the character speaks under different listener and environment conditions:

- default speech;
- superior / authority;
- weaker person;
- ally / trusted person;
- opponent / investigator;
- public setting;
- private stress;
- high punishment risk;
- protecting core object;
- default speech strategy fails.

### Inner Monologue Mode

Record what the character's inner thought usually uses:

- job logic;
- family logic;
- shame;
- fear;
- calculation;
- bodily sensation;
- practical checklist;
- moral judgment;
- relationship worry.

Also record what the inner monologue should not use, such as author summary, destiny language, theme statements, or all-knowing conclusions.

## Protagonist Growth Pages / Sections

A protagonist wiki or dedicated growth file should include:

- initial position;
- starting weakness;
- starting useful skill;
- starting misconception;
- starting fear;
- what the protagonist cannot do at the start;
- larger trend pressure they cannot directly stop;
- staged growth path;
- growth asset ladder;
- forbidden jumps;
- costs required for each stage;
- what remains unsolved after each stage.

After each approved chapter, record protagonist growth only as concrete state:

- active growth stage;
- pressure tested;
- cost paid;
- usable leverage gained;
- relationship/access/object/skill/judgment change;
- final-form asset gained or strengthened;
- what this enables next;
- what the protagonist still cannot do.

Do not record vague growth such as `became stronger`, `understood the world`, or `changed mindset` unless it is tied to a usable later action.

## Organization Pages

Organization pages must include:

- public identity;
- public mission / legitimacy;
- real interests;
- resources controlled;
- operating boundaries;
- embodied agents;
- relationship to other forces;
- what the organization cannot publicly admit.

Major and recurring organizations should also include the following behavior-generation fields.

### Public Legitimacy

- How the organization explains itself to ordinary people.
- What public good it claims to protect.
- What words it uses to make its actions sound legitimate.

### Real Interests

- What the organization truly needs.
- What resource, person, location, record, legitimacy, or secret it must control.
- What it fears losing.

### Operating Boundaries

- What it can openly do.
- What it cannot openly do.
- What it can privately do.
- What it needs cutouts, agents, contractors, subordinates, or other organizations to do.

### Packaging Language

Record how the organization packages:

- control;
- taking someone away;
- sealing a scene;
- taking an object / record / body / witness;
- refusing help, payment, rescue, access, or explanation;
- punishment;
- silence;
- delay.

### Action Ladder

Record escalation stages:

1. Soft pressure: persuasion, reassurance, delay, informal request.
2. Procedural pressure: registration, assessment, signature, review, permission boundary, responsibility split.
3. Coercive but legal pressure: sealing scene, taking a person away, limiting contact, suspending access, isolation, official warning.
4. Gray pressure: threat, scapegoating, selective leak, resource cutoff, outsourced dirty work, pressure on family/job/status.
5. Illegal or irreversible pressure: forced disappearance, falsified scene, destroyed evidence, physical control, killing, permanent disposal.

For Level 5, record trigger conditions, likely executor, and responsibility-cutting method. Do not add Level 5 methods without source support.

### Internal Factions

When relevant, record:

- internal factions;
- their goals;
- their resources;
- their fears;
- frontline executor constraints;
- where frontline agents may diverge from leadership interest.

### Environmental Modulation

Organization behavior should change under:

- public setting;
- private setting;
- crowd / media watching;
- superior watching;
- another strong organization present;
- target has no power;
- target has evidence;
- target cannot be handled legally;
- default strategy fails.

### Misjudgment Pattern

Record:

- what the organization most often misreads;
- what it trusts as evidence;
- what it dismisses;
- what it overestimates;
- what it underestimates.

### Embodied Agents

Record:

- common scene agents;
- agent speech style;
- agent action boundary;
- how much agents can be sacrificed;
- how agents may diverge from organization interest.

## Scene Performance Rule

Do not convert one scene action into permanent personality, protagonist growth, or organization policy too quickly.

For characters, record whether an action is:

- default behavior;
- environment-modulated behavior;
- threshold / override behavior;
- breakdown / collapse;
- strategic performance;
- one-time exception.

For protagonist growth, record whether a change is:

- stage pressure;
- usable leverage;
- final-form asset;
- skill / judgment upgrade;
- relationship / access gain;
- temporary advantage;
- unearned coincidence;
- forbidden jump.

For organizations, record whether an action is:

- default policy;
- public packaging;
- action ladder escalation;
- local agent choice;
- internal faction move;
- gray action;
- illegal exception;
- cutout action;
- one-time emergency response.

## Independent Novel Rule

Every novel maintains a separate wiki.

Never merge character or world state across novels.
