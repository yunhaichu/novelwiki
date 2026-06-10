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
- `prompts/00_name_term_gate.md`
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
Relevant approved names and terms:
Relevant open questions:
Files read:
```

Do not write detailed claims about a character, object, place, organization, process, rule, term, or unresolved question if the matching wiki file was not read.

Reference settings under `reference_settings/` are not canon. Use the novel-specific `wiki/base_settings.md` and approved wiki files as canon.

## Chapter Drafting Rules

Write one chapter with one clear drive.

The chapter should normally move the story toward the current novel project's long-term pressure, status change, relationship change, resource change, knowledge change, access change, or irreversible consequence. Breather chapters are allowed when the novel wiki supports that pacing.

The protagonist should stay within known authority, ability, resource, knowledge, and access boundaries.

The protagonist should not solve every problem cleanly over time. Hesitation, misunderstanding, partial success, cost, missed chance, trace left behind, or increased suspicion can be more believable than perfect action.

Recurring side characters should have their own pressure, desire, fear, possible loss, role limit, or institutional pressure. They should not exist only to make the protagonist look calm, clever, or funny.

Temporary characters may be functional, but their lines should not feel like forced prompts for the protagonist.

## Xiaobai Prose Rule

Default prose should be Chinese webnovel xiaobai style unless the user explicitly asks otherwise.

Xiaobai style here means:

- clear subject, clear action, clear consequence;
- short and medium sentences are allowed;
- simple words over elegant words;
- dialogue and action carry the scene;
- emotional pressure is shown through repeated small actions and concrete trouble;
- the reader should not need to reread a sentence to understand what happened.

Do not write like a report, essay, commentary, trailer, or final summary.

Do not pursue concise elegance.

It is allowed to be a little verbose if the extra words are concrete:

- a character asks one more question;
- someone hesitates before answering;
- someone repeats a practical concern;
- a physical action takes two or three steps;
- a misunderstanding is played out in dialogue;
- a small object is moved, lost, hidden, or checked;
- pressure lands on a visible person.

Bad compression:

```text
他意识到自己已经没有退路。
```

Better xiaobai expansion:

```text
他看着门口的红灯。

红灯没有变。

他又刷了一次工牌。

还是红的。

身后有人开始催。

他把工牌攥进手心，才发现掌心全是汗。
```

Bad summary:

```text
这件事让所有人的关系都发生了变化。
```

Better xiaobai expansion:

```text
左手分拣工没有再叫他二一九。

她把工具盒往自己那边挪了半寸。

马宽伸手去拿胶带时，摸了个空。

她低头干活，像没看见。
```

## Anti-Summary Rule

Do not replace story with conclusion.

Avoid narrator summary lines such as:

```text
这意味着他再也回不到从前。
他终于明白了这个世界的残酷。
真正的麻烦才刚刚开始。
所有人都被卷了进来。
命运的齿轮开始转动。
```

If the sentence is a conclusion, turn it into:

- a line of dialogue;
- a blocked action;
- a repeated attempt;
- a small failure;
- a visible reaction;
- an object or route changing hands;
- someone refusing to answer.

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
- explain the protagonist's psychology after the choice already shows it;
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
- worker slang;
- system-state labels;
- color/status shorthand.

If a term has not passed the gate, use ordinary description.

Prefer:

```text
门口的灯变成黄色。
那块板被机器标成报废件。
楼上的合规员下来了。
那股灰色反应还没有名字。
```

over unapproved compact terms.

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

If the chapter needs a new institution, process, resource, power function, anomaly rule, social rule, name, or term not covered by base settings / name registry, flag the gap rather than silently inventing it.

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
"黑灰送灵田，药泥明早有人来熬。掺错一桶，三天白干。"
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
