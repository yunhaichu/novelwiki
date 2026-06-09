# Chapter State Update Prompt

Use this prompt only after a chapter draft has passed review and the user has approved it as accepted prose.

The purpose is to update the current novel wiki with confirmed chapter state without turning speculation, plans, or reference settings into canon.

Do not update canon before user approval.
Do not import reference settings as confirmed facts.
Do not write future assumptions as facts.
Do not expand the mechanism beyond what the approved chapter shows.

## Required Inputs

Read:

- approved chapter draft
- chapter review
- current `wiki/base_settings.md`
- current `wiki/project.md`
- current `wiki/name_registry.md`
- relevant character files
- relevant world / object / organization / process files
- previous chapter state
- `governance/wiki_write_rules.md`
- `governance/wiki_retrieval_rules.md`

## Output Files To Prepare

Prepare updates for:

```text
wiki/chapter_states/chapter_<number>.md
wiki/characters/<character_id>.md if character state changed
wiki/world/*.md if world rules were confirmed or changed
wiki/name_registry.md if approved names changed
wiki/foreshadowing.md if open questions or planted clues changed
```

## Chapter State Format

```text
# Chapter <number> State

Status: approved / pending_user_approval
Source draft:
Review file:

## Chapter Function


## Confirmed Events

- Event:
  Source evidence:
  Status: confirmed

## Character State Changes

- Character:
  Before:
  After:
  Evidence:

## Object / Resource / Record State

- Object:
  Holder / location:
  State:
  Evidence:

## Organization / Process State

- Process or organization:
  Confirmed behavior:
  Limit:
  Evidence:

## Knowledge Boundary Updates

- Reader knows:
- Protagonist knows:
- Other characters know:
- Institutions can verify:
- Unknown remains:

## Foreshadowing / Open Questions

- Question:
  Status: planted / advanced / answered / still unknown
  Evidence:

## Base Settings Impact

- No change / update needed:
- Reason:

## Next Chapter Pressure


## Do Not Canonize

- Unconfirmed inference:
- Speculation:
- Reference-setting candidate:
```

## Rules

- Only confirmed events from approved prose may be recorded as confirmed.
- Character claims remain claims unless the narration or evidence confirms them.
- Anomaly or power rules should remain at the level shown in the approved chapter.
- If a draft implies something but does not prove it, record it as unknown or inference.
- If the chapter violates base settings, do not patch canon to fit the draft; return to revision instead.
