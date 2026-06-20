# Writer Prompt

Use this prompt to generate an approved bounded prose or narrative unit for any novel in this repository.

This prompt does not default to writing a full chapter. In the collaborative workflow, generation happens only after relevant wiki retrieval, user discussion, and user-approved output scope.

## Required Inputs

Read the current novel wiki before writing:

- project direction;
- genre or type contract if present;
- base settings;
- style rules;
- name registry;
- relevant Entity records;
- relevant Timepoint records;
- relevant State records;
- relevant Relationship records;
- relevant Event records;
- relevant Session / Mutation records when the current output depends on previous user decisions;
- relevant open questions;
- `docs/narrative_model.md`;
- `docs/interactive_writing_flow.md`;
- `governance/wiki_retrieval_rules.md` if present;
- `prompts/00_name_term_gate.md` when names or recurring terms are involved;
- `governance/anti_record_driven_plot.md` when the unit involves systems, reports, logs, files, workflows, institutions, or records;
- `prompts/02_scene_convergence.md` output if available.

## Retrieval Plan

Before writing, prepare a short retrieval plan for internal use or for the user when requested:

```text
Expected entities:
Relevant timepoint:
Relevant states:
Relevant relationships:
Relevant events:
Relevant rule-system or base-setting constraints:
Relevant approved names and terms:
Relevant open questions:
Files read:
User-approved output scope:
```

Do not write detailed claims about an entity, event, place, organization, process, rule, term, relationship, or unresolved question if the matching wiki record was not read.

Reference settings under `reference_settings/` are not canon. Use the novel-specific wiki and approved records as canon.

## Generation Boundary

Generate only the approved unit.

A unit may be:

- one scene;
- one subscene;
- one bounded chapter segment;
- one transition passage;
- one dialogue sequence;
- one scene sketch;
- one event summary;
- one entity card;
- one wiki-ready update draft.

Do not continue into the next scene, solve the next design question, add a new unapproved entity, or create a durable canon fact outside the approved scope.

If the approved scope is structurally weak, output `REVISE SCOPE` with the smallest reason instead of writing around the weakness.

If required canon is missing, output `MISSING CANON` with the missing record or fact instead of inventing it.

If the unit needs a new name or recurring term, stop for Name & Term Gate unless the user explicitly asks for ordinary descriptive placeholder language.

## Generation Rules

The unit should move the story toward the approved pressure, status change, relationship change, resource change, knowledge change, access change, event consequence, or reader-facing movement.

Entities should stay within known authority, ability, resource, knowledge, access, and time-aware state boundaries.

A central actor should not solve every problem cleanly unless the approved design specifically requires it. Hesitation, misunderstanding, partial success, cost, missed chance, trace left behind, increased suspicion, or delayed consequence can be more believable than perfect action.

Recurring secondary entities should have their own pressure, desire, fear, possible loss, role limit, social position, or institutional pressure. They should not exist only to make the central actor look calm, clever, funny, righteous, or impressive.

Temporary entities may be functional, but their dialogue and action should still be grounded in the scene.

## Clear Prose Rule

Default prose should be clear and readable unless the user explicitly asks for another style.

Clear prose means:

- clear subject, clear action, clear consequence;
- short and medium sentences are allowed;
- concrete words over decorative abstraction;
- dialogue and action carry the scene;
- emotional pressure is shown through visible behavior, repeated attempts, changed access, blocked action, or concrete trouble;
- the reader should not need to reread a sentence to understand what happened.

Do not write like a report, essay, commentary, trailer, or final summary.

Do not pursue concise elegance at the cost of scene clarity.

It is allowed to be a little verbose if the extra words are concrete:

- a character asks one more question;
- someone hesitates before answering;
- someone repeats a practical concern;
- a physical action takes two or three steps;
- a misunderstanding is played out in dialogue;
- a small object is moved, lost, hidden, or checked;
- pressure lands on a visible person.

## Anti-Summary Rule

Do not replace story with conclusion.

Avoid narrator summary lines that merely announce a realization, a fate, a relationship change, a world truth, or an abstract escalation.

If the sentence is a conclusion, turn it into:

- a line of dialogue;
- a blocked action;
- a repeated attempt;
- a small failure;
- a visible reaction;
- an object or route changing hands;
- someone refusing to answer;
- someone changing position, access, or behavior.

## Narrative Economy Rule

Narrative economy does not mean terse prose.

It means every extra sentence must do real work.

Do not explain a rule, motive, resource, or mechanism in prose merely because it exists in planning.

A sentence should usually do at least one of the following:

- move action;
- change pressure;
- change relationship;
- expose a choice;
- create a concrete image;
- change information state;
- produce a visible consequence;
- preserve or sharpen a reader hook.

Cut or rewrite sentences that only:

- summarize what the reader already understands;
- explain psychology after the choice already shows it;
- repeat the same cost, limitation, or rule without new scene pressure;
- announce why a moment matters;
- turn subtext into text;
- prove that the setting is logical.

When in doubt, do not compress into an abstract line. Expand into concrete action.

## Name And Term Grounding Rule

Do not invent compact genre-looking labels in prose unless they are approved in `wiki/name_registry.md` or passed through `prompts/00_name_term_gate.md`.

This applies to:

- people names;
- organization names;
- place names;
- object names;
- status labels;
- process names;
- ability names;
- anomaly names;
- slang;
- system-state labels;
- color/status shorthand;
- recurring invented terms.

If a term has not passed the gate, use ordinary description.

A term is allowed only when:

- a real group in the story uses it;
- its function has already appeared;
- the first use makes sense to the reader;
- `name_registry.md` records who uses it and why.

## Character Performance Rule

Do not let narration perform the story for the characters.

Characters must act from their own:

```text
what they see
what they hear
what they think is happening
what they want
what they fear
what they misread
what they can physically do
what they will not say openly
what their current state allows
```

Before writing an important scene, identify the convergence point: the person, object, route, room, witness, decision, resource, rule, or risk that multiple entities want to move, protect, take, hide, block, expose, control, or reinterpret.

Then write the scene through characters acting around that convergence point.

Avoid narrator summaries that announce everyone understood the situation, the real conflict began, the case changed, fate shifted, or the world revealed itself.

Replace them with character performance:

- someone blocks a route;
- someone hides an object;
- someone changes testimony;
- someone refuses to hand over a person or item;
- someone looks at a different target;
- someone moves closer or steps back;
- someone stops answering;
- someone redirects a question;
- someone physically preserves or damages a scene object.

If deleting narrator explanation makes the scene unclear, the scene convergence is weak and should be redesigned.

## Base Settings Rules

Use `wiki/base_settings.md` to check:

- what roles can and cannot do;
- which organizations and processes exist;
- what visible support a process requires;
- what resources, documents, tools, or access rights exist;
- what knowledge each party can plausibly have;
- what mechanisms, powers, anomalies, or special rules can do at the current stage if any;
- what setting moves are forbidden.

Do not import unused reference-setting material directly into prose.

If the unit needs a new institution, process, resource, rule function, anomaly rule, social rule, name, or term not covered by base settings / name registry, flag the gap rather than silently inventing it.

## Scene-First Plot Rule

Do not let interfaces write the story.

Systems, logs, reports, archives, files, case numbers, databases, screens, workflow states, and notifications may appear, but they must not replace people, objects, relationships, and scene action.

Every time a system or record appears, ask:

```text
Who changes action because of it?
Who blocks, takes, hides, refuses, moves, protects, or destroys something because of it?
What physical object, person, route, or relationship changes immediately?
Can the same plot effect be carried by a person or object instead?
```

If the answer is unclear, remove the system/record beat or demote it to background.

The unit climax should not be clicking, submitting, uploading, approving, filing, logging, receiving a popup, or watching status change unless the user explicitly approves that as the story form.

Prefer climax carried by:

- one person blocking another;
- someone trying to take a person, witness, object, or key resource away;
- someone hiding, protecting, swapping, refusing, or exposing a physical object;
- someone changing testimony in front of another person;
- someone arriving in person and changing access;
- a relationship visibly shifting;
- a central actor using a scene object or relationship as leverage.

## Process Expression Rule

Processes should appear through scene pressure, not explanatory blocks.

Prefer:

- a person refusing responsibility;
- a stronger actor arriving in person;
- a door or route being blocked;
- a worker trying to remove an object;
- a witness being moved;
- a superior demanding a choice;
- a physical item that must be preserved;
- a later consequence from an earlier process choice.

Use buttons, fields, popups, forms, reports, notes, and electronic records sparingly. They are support, not the main plot carrier.

Avoid consecutive paragraphs explaining how the process works unless the explanation is immediately forced by action, conflict, or consequence.

## World Function In Prose Rule

If a scene involves labor, ritual, process, institution, task, exam, mission, repair, medical handling, business workflow, official procedure, group duty, or similar recurring activity, prose must show enough functional purpose for the scene to feel real.

Do not explain the full system. Reveal only the smallest visible function needed for the reader to understand why the task exists and why errors matter.

Prefer one concrete line from an actor or one visible consequence over a paragraph explaining the whole supply chain.

If the task has no world function beyond giving the central actor something to touch, redesign the scene.

## Reader Itch Rule

For opening units and major arc starts, make the reader's next question concrete and tied to the active scene.

Avoid broad questions such as abstract truth, destiny, origin, or ultimate world secret unless the approved genre and scene specifically require them.

Prefer a concrete question about whether an actor can keep, reach, hide, prove, protect, expose, escape, persuade, survive, or change something under immediate pressure.

## Hard Anti-AI Taste Rules

When two similar events appear close together, do not use the same narrative sequence twice. The second pass must change focus, such as bodily sensation, visible detail, social reaction, mistake, hesitation, consequence, or missing information.

Unit endings should usually land on action, object, bodily sensation, unfinished choice, concrete consequence, or changed relationship.

Avoid defaulting to polished, symmetrical, aphoristic, or explanatory closing lines.

## Conditional Anti-AI Taste Rules

Do not overuse the same joke, object, phrase, or reaction in a single unit unless each repetition adds new information, a new cost, a new choice, or a changed relationship.

Do not turn every intense moment into silence, coldness, stillness, breath, pulse, light, shadow, or temperature.

Do not make every competent character speak in short cryptic lines.

Do not make every organization sound like a villain, teacher, judge, or puzzle box unless the wiki supports it.

## Output Format

Return only the requested output.

If the user requests prose, return prose.

If the user requests a scene sketch, return a scene sketch.

If the user requests a wiki-ready update, return the update.

When the output may change canon, append a short status card unless the user explicitly asks for prose only:

```text
Canon changes if approved:
- ...

Affected entities:
- ...

Possible state changes:
- ...

Next decision point:
- ...
```

If no canon change is introduced, say:

```text
Canon changes if approved:
- None.
```