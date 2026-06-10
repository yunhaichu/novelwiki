# Character Behavior Model Prompt

Use this prompt when creating or upgrading a major character wiki file.

The purpose is to prevent static character labels. A character is not a fixed adjective. A character is a default behavior pattern that changes under environment variables, relationship pressure, risk level, and threshold triggers.

## Hard Source Rule

All behavior traits must come from approved sources:

- user initial premise / initial settings;
- current novel wiki;
- approved character files;
- approved organization / faction files;
- approved actor cognition cards;
- approved character expression cards;
- approved chapter states.

Do not invent dramatic behavior, heroic override, breakdown, courage, cowardice, humor, cruelty, tenderness, or speech modulation without source support.

If the source is insufficient, write `behavior_gap` instead of filling it silently.

## Name Gate Rule

When creating a new character, do not generate the character name directly from model preference.

Before writing `Character name`, run a small Name Gate using the current novel's `wiki/name_registry.md` and the naming rules in `prompts/00_wiki_bootstrap.md`.

For new characters, produce:

```text
## Character Name Gate

Character function:
Social layer / occupation:
Legal-name system:
Nickname / handle / work-ID system:
Name candidates:
Rejected names and reasons:
Selected legal name:
Selected work name / handle / nickname if any:
Why selected name fits this world and social layer:
AI-default risk: low / medium / high
Previously used in this repository or current conversation: yes / no
Name gate decision: ALLOW / REVISE
```

If the character has no approved name yet, use a functional placeholder such as `recycling_shift_supervisor_01` instead of inventing a polished name.

For minor temporary characters, a role label is allowed until the character becomes recurring:

```text
night-shift guard
left-hand sorter
debt clinic clerk
```

Do not write a new named character file if the Name Gate is missing or fails.

## Core Principle

```text
Personality determines default mode.
Environment determines modulation.
Threshold determines reversal.
Aftermath determines whether the behavior becomes growth, shame, denial, collapse, or temporary exception.
```

A coward may fight when a protected child is threatened.
A bully may collapse when violence stops working.
A blunt speaker may become careful in front of a life-and-death authority.
A reckless person may think before speaking in public if the wrong sentence will harm someone they care about.

This is not out-of-character when the modulation is grounded.

## Output Format

```text
# Character Behavior Model

Character ID:
Character name:
Name Gate source / result:
Source files read:
Behavior confidence: high / medium / low

## Default Behavior Mode

Normal outward behavior:
-

Default conflict strategy:
-

Default speech strategy:
-

Default body strategy:
-

Default avoidance pattern:
-

Default way of gaining control:
-

## Works When

This default mode works when:
-

The character feels safe when:
-

The character assumes they can control the situation when:
-

## Breaks When

The default mode breaks when:
-

The character loses control when:
-

The character's usual strategy becomes useless when:
-

## Environmental Modulation

### Facing weaker person
Likely behavior:
What changes from default:
What remains from default:

### Facing equal / peer
Likely behavior:
What changes from default:
What remains from default:

### Facing stronger person / authority
Likely behavior:
What changes from default:
What remains from default:

### Facing unknown / monster / anomaly
Likely behavior:
What changes from default:
What remains from default:

### In public
Likely behavior:
What changes from default:
What remains from default:

### In private
Likely behavior:
What changes from default:
What remains from default:

### When core protected object is threatened
Likely behavior:
What changes from default:
What remains from default:

### When no escape route exists
Likely behavior:
What changes from default:
What remains from default:

### When violence / argument / money / status works
Likely behavior:

### When violence / argument / money / status fails
Likely behavior:

### When information is incomplete
Likely behavior:

### When physically hurt / exhausted / afraid
Likely behavior:

## Core Protected Object

Person / value / secret / status / object they most want to protect:
-

Why this matters more than ordinary self-protection:
-

What they will sacrifice for it:
-

What they will not sacrifice for it:
-

## Threshold / Override Behavior

Breaking point:
-

Conditions required to trigger override:
-

Conditions that are not enough to trigger override:
-

Override behavior:
-

Action style during override: clumsy / violent / silent / precise / panicked / cold / reckless / other
-

What abilities do not change during override:
-

What limits remain:
-

## Extreme Reaction

Under extreme fear:
-

Under extreme shame:
-

Under extreme anger:
-

Under extreme grief:
-

Under extreme protective urgency:
-

Possible collapse / freeze / flight / violence / confession / betrayal:
-

## Aftermath

After override or breakdown, they are likely to:
-

Physical aftermath:
-

Speech aftermath:
-

Relationship aftermath:
-

Whether they deny, hide, justify, regret, normalize, or repeat the behavior:
-

## Inner Monologue Mode

Inner thought usually uses:
- job logic / family logic / shame / fear / calculation / bodily sensation / practical checklist / moral judgment / other

Inner thought should not use:
-

Typical thought under default mode:
-

Typical thought under threshold pressure:
-

## Behavior Gaps

- Gap:
  Why missing:
  Needed before:
  Suggested source to resolve:
```

## Checks

Mark `REVISE` if:

- Name Gate is missing for a new named character;
- the selected name has high AI-default risk without explicit approval;
- the character is reduced to one adjective;
- the default behavior has no conditions;
- the character behaves the same toward weak, equal, strong, public, private, known, unknown, human, and non-human pressure;
- the character has no core protected object;
- a reversal behavior appears without a threshold trigger;
- a reversal makes the character suddenly competent beyond established ability;
- the aftermath is ignored;
- the model lets the character act from narrator knowledge rather than local perception;
- environmental modulation is invented without source support.
