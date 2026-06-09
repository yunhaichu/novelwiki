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

## Process Expression Rule

Processes should appear through scene pressure, not explanatory blocks.

Prefer:

- a button that is disabled;
- a required field that blocks submission;
- a message from a superior;
- a record that contradicts another record;
- a warning prompt;
- a failed call;
- a visible note left in the system;
- a person refusing responsibility;
- a later consequence from an earlier process choice.

Avoid consecutive paragraphs explaining how the process works unless the explanation is immediately forced by action, conflict, or consequence.

## Reader Itch Rule

For opening chapters and major arc starts, make the reader's next question concrete and protagonist-bound.

Bad:

```text
What is the truth of this world?
```

Better:

```text
Can the protagonist stop the specific loss without creating a record that exposes him?
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
