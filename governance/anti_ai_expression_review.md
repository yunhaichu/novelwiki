# Anti-AI Expression Review

Use this checklist after drafting and final polish.

The purpose is to remove AI-flavored expression and unnecessary explanatory prose that survives plot, scene, and dialogue planning.

This review focuses on prose-level symptoms:

- pretty summaries;
- vague emotional labels;
- generic body reactions;
- unsupported metaphors;
- identity label sentences;
- author commentary;
- polished trailer lines;
- repetitive rhythm;
- dialogue that sounds like narration;
- record-driven narration;
- explanatory proof lines;
- optional sentences that weaken subtext.

## Required Inputs

Read:

- current chapter draft;
- character expression cards;
- scene expression states;
- dialogue intent;
- current novel style file;
- anti-AI taste rules if present;
- relevant character wiki files;
- `governance/anti_record_driven_plot.md` when relevant.

## Hard Principle

Do not improve prose by making it more literary.

Improve prose by making it more grounded in:

```text
current person
current object
current action
current speaker
current listener
current pressure
current route / permission / resource
current consequence
```

Records, screens, reports, and systems can support pressure, but they should not be the emotional or narrative center of the scene.

## Narrative Economy Principle

If a sentence can be removed without losing action, necessary information, pressure, relationship change, object state, or reader hook, remove it.

The prose should not repeat what the reader can infer from:

- a choice;
- a refusal;
- a visible cost;
- a changed object;
- a changed relationship;
- a character's silence;
- a scene consequence.

Logic belongs in planning and wiki. The draft should show only the smallest amount of explanation needed for the reader to follow the scene.

## Hard Checks

### 1. Pretty Summary Check

Mark `REVISE` if the prose uses neat, dramatic, trailer-like, or aphoristic summary lines to create weight.

Weak patterns:

```text
Everything had changed.
The real test had just begun.
He finally understood what this meant.
This was no longer a simple accident.
The storm had awakened.
```

Replace with:

- object state;
- person entering / leaving;
- a route blocked;
- a witness changing answer;
- someone refusing to hand something over;
- someone taking or protecting a physical object;
- a relationship changing in public.

### 2. Unsupported Metaphor Check

Mark `REVISE` if a metaphor is not grounded in the current character viewpoint, role, environment, or established style.

Metaphors should be rare. For high-pressure scenes, prefer hard object state.

### 3. Generic Body Reaction Check

Mark `REVISE` if repeated body reactions carry tension without changing the scene.

Weak patterns:

```text
heart skipped a beat
breath caught
fingers tightened
pupils shrank
cold sweat
body froze
mind went blank
```

Use body reaction only when it affects action, speech, object handling, position, or timing.

### 4. Identity Label Check

Mark `REVISE` if the prose says identity directly instead of embedding it in action, permission, tools, relationship, or setting.

Weak:

```text
As a low-level technician, he had no authority.
```

Stronger:

```text
The stop command was gray on his screen. His account could read it, not press it.
```

### 5. Psychological Summary Check

Mark `REVISE` if the prose summarizes mental change instead of showing action, omission, object state, or relationship pressure.

Weak:

```text
He realized he could no longer turn back.
```

Stronger:

```text
His name appeared under the locked record. The cancel button disappeared.
```

### 6. Dialogue-As-Narration Check

Mark `REVISE` if a character says what the narrator wants the reader to know instead of what the character wants the listener to do, reveal, hide, stop, admit, or change.

### 7. Same-Rhythm Check

Mark `REVISE` if consecutive paragraphs use the same structure:

```text
observation -> explanation -> consequence
short sentence -> dramatic line
question -> answer -> realization
```

Vary with action, interruption, object state, omitted answer, or external sound.

### 8. Role-Grounding Check

When a line sounds AI-flavored, ask:

```text
What would this character's job, rank, tool, fear, or relationship make them say instead?
```

Replace abstract lines with role-grounded speech or action.

### 9. Scene Utility Check

Every paragraph should do at least one:

- move action;
- reveal necessary information;
- change pressure;
- change relationship;
- alter object / person / position;
- expose a knowledge boundary;
- create a choice;
- pay off a prior setup.

Mark `REVISE` for decorative atmosphere that does not affect reading path.

### 10. Optional Sentence / Leave-Blank Check

Mark `REVISE` if a sentence explains, repeats, or labels something that the scene already shows.

Common weak patterns:

```text
This was his only chance.
That was enough.
He understood what it meant.
He was not kind, only practical.
This proved the world was cruel.
He had no way back.
```

Repair by deleting the sentence first. Add replacement only if deletion breaks comprehension.

Ask:

```text
If this sentence is removed, does the scene still work?
If yes, delete it.
```

### 11. Explanation Leakage Check

Mark `REVISE` if preflight, wiki, or world-model reasoning leaks into prose as explanation.

Examples:

- explaining an institution's full cost logic after the action already demonstrates it;
- explaining why a labor process exists when one concrete consequence or line of dialogue would suffice;
- explaining a character's survival calculation after their action already reveals it;
- restating a goldfinger limitation after the cost has been shown.

Keep the functional minimum and cut the rest.

### 12. Source Support Check

If an expressive habit, metaphor style, repeated gesture, speech quirk, or emotional display is not supported by wiki or expression card, remove or mark an expression gap.

### 13. Record-Centered Expression Check

Mark `REVISE` if paragraphs repeatedly center on:

- screen prompts;
- report forms;
- case numbers;
- database status;
- logs;
- archives;
- system messages;
- automatic workflow changes;
- electronic records;

while people and objects remain secondary.

Convert record-centered paragraphs into person/object-centered paragraphs.

Weak:

```text
The system marked the case as abnormal.
```

Stronger:

```text
The doctor stopped at the stairwell after one call, turned back to the child, and told the nurse not to move her.
```

Weak:

```text
The report triggered an investigation.
```

Stronger:

```text
A man in plain clothes came up the stairs, showed his badge only to the doctor, and asked who had touched the handrail.
```

## Output Format

```text
Decision: ALLOW / REVISE

Main reason:

Expression checks:
- Pretty summary:
- Unsupported metaphor:
- Generic body reaction:
- Identity label:
- Psychological summary:
- Dialogue-as-narration:
- Same rhythm:
- Role grounding:
- Scene utility:
- Optional sentence / leave-blank:
- Explanation leakage:
- Source support:
- Record-centered expression:

Lines to revise:
1. Original:
   Problem:
   Delete or replace:
   Replacement direction if needed:

2. Original:
   Problem:
   Delete or replace:
   Replacement direction if needed:

Required fixes if REVISE:
1.
2.
3.
```

## Repair Method

First try deletion.

If deletion makes the scene unclear, replace with one of:

- visible object state;
- specific permission boundary;
- scene movement;
- concrete refusal;
- interrupted sentence;
- role-grounded status report;
- person-to-person action;
- physical object being moved, hidden, protected, taken, damaged, or exposed;
- relationship change;
- a smaller, less polished line.

## Review Standard

A line can be plain and still strong.

The target is not literary polish. The target is believable pressure carried by people, objects, actions, relationships, and consequences.
