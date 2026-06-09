# Character Voice Review

Use this checklist after dialogue intent, after drafting, and before final prose approval.

The purpose is to detect AI-flavored character speech and prevent unsupported voice traits.

## Required Inputs

Read:

- character behavior models;
- character expression cards;
- scene expression states;
- dialogue intent;
- actor cognition cards;
- current character wiki files;
- current chapter draft;
- current novel style file;
- previous chapter state if relevant.

## Hard Source Rule

All character voice traits must be grounded in initial settings or current wiki.

Mark `REVISE` if the draft invents:

- catchphrases;
- dialect;
- humor style;
- speaking rhythm;
- emotional habit;
- repeated gesture while speaking;
- relationship mode;
- technical vocabulary;
- class / rank speech habit;
- private nickname;
- environmental speech modulation;
- threshold speech reversal;

without approved source support.

## Hard Checks

### 1. Source Grounding

Does each character's speech match approved character expression card, behavior model, and wiki?

Mark `REVISE` if a character suddenly sounds vivid in a way the wiki does not support.

### 2. Listener-Specific Mode

Does the character speak differently to superior, subordinate, ally, opponent, stranger, public audience, and private contact when the situation requires it?

Mark `REVISE` if the character uses the same rhythm and openness with everyone.

### 3. Environment Modulation

Does the character's speech change under different environmental variables?

Check:

- low-risk vs high-risk;
- private vs public;
- weak listener vs powerful listener;
- familiar person vs stranger;
- ordinary problem vs unknown / monster / anomaly;
- safe exit vs no escape route;
- personal risk vs protected person/object threatened;
- default speech strategy works vs fails.

Mark `REVISE` if a character's default label is treated as a fixed output.

Examples:

```text
A blunt person should not always be blunt in front of a life-and-death authority.
A careless speaker should not always speak without thinking in public when a wrong word harms someone important.
A bully should not sound equally dominant when facing a threat their usual intimidation cannot control.
```

### 4. Scene Pressure Fit

Does each line come from the current scene goal, pressure, previous line, previous action, and relationship position?

Mark `REVISE` if the line sounds good but is not necessary for the current scene.

### 5. Knowledge Boundary

Mark `REVISE` if a character says, implies, or correctly infers information outside their direct or indirect knowledge.

Characters may guess, but guesses must be marked by wording, hesitation, or evidence.

### 6. Dialogue Function

Every meaningful dialogue line must change at least one of:

```text
information
relationship
pressure
action direction
```

Mark `REVISE` if a line only explains setting, repeats known facts, or gives author commentary.

### 7. Anti-Pretty-Summary Check

Mark `REVISE` if dialogue contains trailer-like, aphoristic, or overly polished summary language.

Examples of weak patterns:

```text
This is bigger than we thought.
The real game has just begun.
That thing has been asleep for years, and today it woke up.
You don't understand what you're involved in.
```

Replace with role-grounded speech:

- a status report;
- a concrete warning;
- a refusal;
- a number;
- a permission boundary;
- a location / object state;
- a question that exposes pressure.

### 8. Role / Profession Language

Does the character use vocabulary appropriate to their job, rank, class, training, and immediate environment?

Example:

A repair technician under pressure should usually report device state, maintenance record, fault, route, or risk, not poetic conclusions.

### 9. Concealment And Omission

Characters should not say everything they know.

Mark `REVISE` if a character fully explains their motive, fear, inference, and plan in one line without scene pressure forcing disclosure.

### 10. Repeated Voice Pattern

Mark `REVISE` if multiple characters use the same sentence pattern, joke structure, question style, metaphor style, or dramatic pause.

### 11. Action Alternative

If a line can be replaced by action, object state, silence, interruption, distance change, or a visible record without losing meaning, consider replacing it.

## Output Format

```text
Decision: ALLOW / REVISE

Main reason:

Character voice checks:
- Source grounding:
- Listener-specific mode:
- Environment modulation:
- Scene pressure fit:
- Knowledge boundary:
- Dialogue function:
- Pretty-summary issue:
- Role language:
- Concealment / omission:
- Repeated pattern:
- Action alternative:

Required fixes if REVISE:
1.
2.
3.
```

## Review Standard

Good dialogue does not need to sound clever.

Good dialogue should sound like this person, in this situation, speaking to this listener, under this environmental pressure, while trying to get or hide something.
