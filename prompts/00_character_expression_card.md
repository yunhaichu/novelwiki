# Character Expression Card Prompt

Use this prompt after initial settings, base settings, major conflict engine, dramatic arena, actor cognition cards, and character behavior model are available.

The purpose is to define how a character expresses themselves without inventing unsupported personality traits, speech habits, catchphrases, or emotional patterns during drafting.

## Hard Source Rule

All expression traits must come from approved sources:

- user initial premise / initial settings;
- current novel `wiki/project.md`;
- current novel `wiki/base_settings.md`;
- current novel `wiki/style.md`;
- current novel `wiki/name_registry.md`;
- approved character wiki files;
- approved organization / faction wiki files;
- approved actor cognition cards;
- approved character behavior models;
- approved chapter states.

Do not invent speech habits, personality quirks, catchphrases, dialect, humor style, emotional habits, or relationship modes because they sound vivid.

If the source is insufficient, mark an `expression_gap` instead of filling it silently.

## Core Principle

A character's expression is not a single voice label.

A character expresses differently depending on:

```text
base personality
+ role / profession
+ environmental variables
+ current pressure
+ relationship with listener
+ power difference
+ audience / public setting
+ risk level
+ what they know
+ what they must hide
+ what they cannot afford
+ whether their default behavior works here
```

Speech habits are default modes, not permanent outputs.

A blunt person may become careful in front of a life-and-death authority.
A careless speaker may pause in public if the wrong sentence can harm someone.
A bully may speak softly when their usual intimidation stops working.
A timid person may speak sharply when a protected person is threatened.

## Output Format

```text
# Character Expression Card

Character ID:
Character name:
Source files read:
Expression confidence: high / medium / low

## Source-Grounded Identity

Role / job / social position:
-

Affiliation:
-

Base personality supported by wiki:
-

Known fears / desires:
-

Known constraints:
-

Known knowledge limits:
-

Behavior model link / summary:
-

## Default Expression Pattern

Default sentence length:
-

Default vocabulary range:
-

Default rhythm:
-

Default emotional leakage:
-

Default avoidance pattern:
-

Default pressure reaction:
-

Default body / action habits while speaking:
-

## Environmental Speech Modulation

### Low-risk familiar setting
Speech shape:
What relaxes:
What remains from default:

### High-power listener
Speech shape:
What becomes controlled:
What default habit leaks through:

### Public / watched setting
Speech shape:
What becomes controlled:
What default habit leaks through:

### High punishment risk
Speech shape:
What becomes controlled:
What default habit leaks through:

### Protecting core object / person
Speech shape:
What becomes sharper:
What default habit breaks:

### Facing unknown / anomaly / monster / unmanageable situation
Speech shape:
What becomes simpler / shorter / broken:
What default habit fails:

### When default speech strategy fails
Second speech strategy:
Possible breakdown / silence / confession / aggression / retreat:

## Forbidden Expression

This character must not sound like:
-

This character should avoid:
-

This character should not know or say:
-

Unsupported voice traits:
-

## Relationship-Specific Modes

### Speaking to superior / authority
Speech goal tendency:
What they reveal:
What they hide:
Sentence shape:
Common move:
Forbidden move:

### Speaking to subordinate / weaker person
Speech goal tendency:
What they reveal:
What they hide:
Sentence shape:
Common move:
Forbidden move:

### Speaking to ally / trusted person
Speech goal tendency:
What they reveal:
What they hide:
Sentence shape:
Common move:
Forbidden move:

### Speaking to opponent / investigator / enemy
Speech goal tendency:
What they reveal:
What they hide:
Sentence shape:
Common move:
Forbidden move:

### Speaking in public / formal setting
Speech goal tendency:
What they reveal:
What they hide:
Sentence shape:
Common move:
Forbidden move:

### Speaking under private stress
Speech goal tendency:
What they reveal:
What they hide:
Sentence shape:
Common move:
Forbidden move:

## Scene Pressure Modifiers

When afraid:
-

When hiding information:
-

When trying to control the situation:
-

When caught off guard:
-

When lying or half-truthing:
-

When protecting someone:
-

When protecting self-interest:
-

When default mode breaks:
-

## Dialogue Examples

Examples must be source-consistent and short.

Good line:
Why it fits:
Which environment applies:

Bad line:
Why it fails:
Which environment it ignores:

## Expression Gaps

- Gap:
  Why missing:
  Needed before:
  Suggested source to resolve:
```

## Checks

Mark `REVISE` if:

- a voice trait is not grounded in initial settings or wiki;
- the card gives a catchphrase without source support;
- the character sounds the same to every listener;
- the character sounds the same in low-risk, high-risk, public, private, authority, and unknown-threat situations;
- the card ignores role, profession, class, rank, relationship, power difference, audience, or punishment risk;
- the card lets the character say information outside their knowledge boundary;
- the card treats `blunt`, `cowardly`, `strong`, `reckless`, `cold`, `witty`, or similar labels as fixed output rather than default modes modified by environment;
- the card uses abstract labels such as `cold`, `strong`, `smart`, `witty` without showing sentence shape, avoidance pattern, action habits, and environmental modulation;
- examples sound like author commentary rather than character speech.
