# Wiki Retrieval Rules

These rules prevent missed context, wrong context, and accidental replacement of true canon with false or inferred facts.

## Purpose

As a novel grows, the wiki will become too large to read in full before every chapter.

The workflow must therefore retrieve only the relevant files, but it must do so systematically.

The goal is to avoid:

- missing important prior facts
- treating guesses as facts
- overwriting true canon with mistaken updates
- confusing one novel's wiki with another novel's wiki
- letting a character know information they should not know
- using reference settings as if they were novel canon

## Required Reading Before Writing a Chapter

Before writing a new chapter, read at least:

1. The novel's `wiki/project.md`.
2. The novel's `wiki/base_settings.md` if it exists.
3. The novel's `wiki/style.md`.
4. The novel's `wiki/name_registry.md`.
5. The previous chapter state.
6. The protagonist character file.
7. Character files for every planned speaking or plot-impacting character.
8. Relevant world, location, organization, process, item, object, or relationship files for the scene.
9. Relevant open questions or foreshadowing files when the chapter touches unresolved material.

If a character, location, item, organization, process, rule, object, mechanism, or unresolved mystery is not retrieved, do not write detailed claims about it.

## Reference Settings Boundary

Files under `reference_settings/` are reusable references, not canon.

A reference-setting idea may be used in a chapter only if it has already been accepted into the current novel's wiki, usually through `wiki/base_settings.md` or another approved canon file.

Do not retrieve reference settings from another novel or use test-novel settings to define a current novel.

## Retrieval Planning

Before writing, prepare a short retrieval plan:

```text
Chapter Retrieval Plan

Expected characters:
- 

Expected locations:
- 

Expected organizations or processes:
- 

Expected items or abnormal objects:
- 

Relevant base setting rules:
- 

Relevant unresolved questions:
- 

Files to read:
- 
```

The writing step should follow this plan.

## Knowledge Categories

Every important entry in the wiki should belong to one of these categories.

### Confirmed Fact

Something directly shown in approved text or confirmed by reliable narration.

### Character Claim

Something said by a character. It may be true, false, incomplete, or biased.

### Observation

Something a character or narration directly observes, without explaining its cause.

### Inference

A character's or narrator-limited interpretation of observed signs.

### Unknown

An unresolved question or not-yet-explained element.

### Reference Candidate

A reusable idea from `reference_settings/` that may help build a novel-specific setting, but is not canon until accepted into the current novel's wiki.

## Writing Rule

When writing a chapter:

- Confirmed facts may be used as stable canon.
- Character claims must not be treated as objective truth unless later confirmed.
- Observations may be repeated but not over-explained.
- Inferences must remain tied to the character who made them.
- Unknowns must not be filled in early.
- Reference candidates must not be used as canon unless accepted into the current novel wiki.

## Wiki Update Rule

When updating the wiki after a chapter:

- Do not convert a character claim into confirmed fact.
- Do not convert a suspicion into confirmed fact.
- Do not convert a one-time action into a permanent trait.
- Do not erase previous state unless the new chapter clearly changes it.
- If the new chapter changes a character, record the transition, not just the result.
- Do not import unrelated reference-setting material during wiki updates.

## Conflict Handling

If new text conflicts with existing wiki:

1. Do not overwrite immediately.
2. Create a conflict note.
3. List the old wiki entry.
4. List the new chapter evidence.
5. Decide whether it is:
   - old wiki error
   - new draft error
   - character development
   - unreliable claim
   - intentional contradiction
   - reference-setting misuse
6. Only then update canon.

## Source Requirement

Every canon entry in the wiki must include a source. This is mandatory, not optional.

Required format:

```text
Fact: <the confirmed fact>
Source: <chapter_XXX / setup_output / chapter_state / user_instruction>
Status: confirmed / claim / observation / inference / unknown / reference_candidate
```

If no approved source exists for an entry, it must not enter the wiki. Do not use "I remember" or "it fits the story" as a source.

## Character Knowledge Boundary

Before allowing a character to say or act on information, check:

- Has this character personally seen it?
- Has someone told this character?
- Is it available through their role, authority, records, tools, or institution?
- Is the character guessing?
- If guessing, does the text mark it as a guess?

If none applies, the character should not know it.

## Long-Running Novel Safety

For long projects, never rely only on recent chat context.

Use the wiki as the canonical source of truth.

If the wiki and memory disagree, trust the wiki unless the user explicitly says the wiki is wrong.

## Independent Novel Rule

Only retrieve files from the current novel's folder unless the change is global governance or reference-setting development.

Do not mix facts, character states, naming rules, base settings, or timelines across novels.
