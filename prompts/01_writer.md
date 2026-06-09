# Writer Prompt

Use this prompt to draft the next chapter of any novel in this repository.

## Required Inputs

Read the current novel wiki before writing:

- project direction
- type contract if present
- base settings
- style rules
- name registry
- protagonist file
- planned character files
- relevant world, location, item, organization, process, or relationship files
- previous chapter state
- relevant open questions
- `governance/wiki_retrieval_rules.md`
- `governance/anti_record_driven_plot.md` when the chapter involves systems, reports, logs, files, workflows, institutions, or records
- `prompts/02_scene_convergence.md` output if available

## Retrieval Plan

Before writing, prepare a short retrieval plan:

```text
Expected characters:
Expected locations:
Expected objects:
Relevant organizations or processes:
Relevant base setting rules:
Relevant open questions:
Files read:
```

Do not write detailed claims about a character, object, place, organization, process, rule, or unresolved question if the matching wiki file was not read.

Reference settings under `reference_settings/` are not canon. Use the novel-specific `wiki/base_settings.md` and approved wiki files as canon.

## Chapter Drafting Rules

Write one chapter with one clear drive.

The chapter should normally move the story toward the current novel project's long-term pressure, status change, relationship change, resource change, knowledge change, access change, or irreversible consequence. Breather chapters are allowed when the novel wiki supports that pacing.

The protagonist should stay within known authority, ability, resource, knowledge, and access boundaries.

The protagonist should not solve every problem cleanly over time. Hesitation, misunderstanding, partial success, cost, missed chance, trace left behind, or increased suspicion can be more believable than perfect action.

Recurring side characters should have their own pressure, desire, fear, possible loss, role limit, or institutional pressure. They should not exist only to make the protagonist look calm, clever, or funny.

Temporary characters may be functional, but their lines should not feel like forced prompts for the protagonist.

## Narrative Economy Rule

The draft should not prove the workflow. The workflow, wiki, and preflight prove the logic. The prose only needs to carry action, consequence, pressure, and necessary information.

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

Cut or compress sentences that only:

- summarize what the reader already understands;
- explain the protagonist's psychology after the choice already shows it;
- repeat the same cost, limitation, or rule;
- announce why a moment matters;
- turn subtext into text;
- prove that the setting is logical.

Prefer:

```text
choice -> action -> consequence
```

over:

```text
choice -> action -> explanation of why the choice matters
```

When a line is optional, leave it out.

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
```

Before writing an important scene, identify the convergence point: the person, object, route, room, witness, decision, or risk that multiple characters want to move, protect, take, hide, block, expose, or control.

Then write the scene through characters acting around that convergence point.

Avoid narrator summaries such as:

```text
everyone realized the situation had changed
the case was no longer simple
all sides began to compete for the child
the real conflict had just begun
he understood that he had crossed a line
```

Replace them with character performance:

- someone blocks a doorway;
- someone hides an object;
- someone changes testimony;
- someone refuses to hand over a person;
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
- what mechanisms, powers, anomalies, or goldfingers can do at the current stage if any;
- what setting moves are forbidden.

Do not import unused reference-setting material directly into prose.

If the chapter needs a new institution, process, resource, power function, anomaly rule, or social rule not covered by base settings, flag the gap rather than silently inventing it.

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

The chapter climax should not be clicking, submitting, uploading, approving, filing, logging, receiving a popup, or watching status change.

Prefer climax carried by:

- one person blocking another;
- someone trying to take a child, witness, object, or key person away;
- someone hiding, protecting, swapping, refusing, or exposing a physical object;
- someone changing testimony in front of another person;
- someone arriving in person and changing access;
- a relationship visibly shifting;
- a protagonist using a scene object or relationship as leverage.

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

If a scene involves labor, ritual, process, institution, task, exam, mission, repair, medical handling, sect work, business workflow, or similar recurring activity, prose must show enough functional purpose for the scene to feel real.

Do not explain the full system. Reveal only the smallest visible function needed for the reader to understand why the task exists and why errors matter.

Prefer one concrete line from an actor or one visible consequence:

```text
"Black ash goes to the field. Medicine mud gets boiled again. Mix them and the bucket is dead."
```

over a paragraph explaining the whole supply chain.

If the task has no world function beyond giving the protagonist something to touch, redesign the scene.

## Reader Itch Rule

For opening chapters and major arc starts, make the reader's next question concrete and protagonist-bound.

Bad:

```text
What is the truth of this world?
```

Better:

```text
Can the protagonist keep the key person or object in the room long enough to stop a stronger organization from taking it?
```

## Hard Anti-AI Taste Rules

When two similar events appear close together, do not use the same narrative sequence twice. The second pass must change focus, such as bodily sensation, visible detail, social reaction, mistake, hesitation, consequence, or missing information.

Chapter endings should usually land on action, object, bodily sensation, unfinished choice, concrete consequence, or changed relationship.

Avoid defaulting to polished, symmetrical, aphoristic, or explanatory closing lines.

## Conditional Anti-AI Taste Rules

Do not overuse the same joke, object, phrase, or reaction in a single chapter unless each repetition adds new information, a new cost, a new choice, or a relationship change.

Do not let recurring-character dialogue become repeated setup-and-response rhythm.

Each chapter should ideally have one concrete memory point that belongs to this story, especially for first chapters, new arcs, and major turning chapters.

## Output

Output only the chapter draft unless the user asks for planning notes.
