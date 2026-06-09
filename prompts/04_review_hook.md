# Review Hook Prompt

Use this prompt after a chapter draft is written and before chapter state is created.

## Inputs

Read:

- the chapter draft
- the current novel project file
- the current novel base settings file if present
- the current novel style file
- relevant character files
- relevant world, location, organization, process, object, or relationship files
- previous chapter state
- `governance/review_checklist.md`
- `governance/base_settings_review.md` when a setting boundary is involved
- `governance/anti_ai_taste_check.md`

## Decision

Return one of:

- ALLOW
- REVISE

## Checks

Check main drive, wiki consistency, base-setting consistency, knowledge boundaries, character behavior, authority and process boundaries, resource and object support, style, long-form direction, and anti-AI taste.

## Hard Base-Setting Checks

1. Reference settings are not canon.
   If the draft uses a `reference_settings/` idea that was not accepted into the current novel wiki or approved base settings, mark REVISE.

2. Authority boundary.
   If a character performs an action beyond their role, access, authority, knowledge, or resources without visible leverage, crisis condition, fraud, permission, or cost, mark REVISE.

3. Process support.
   If an institutional, social, technical, magical, legal, sect, camp, platform, or organizational result happens without the required support defined by base settings, mark REVISE.

4. Resource and object support.
   If a meaningful resource, document, tool, access right, clue, power source, or object appears without source, holder, access condition, use, limit, or risk, mark REVISE.

5. Power / anomaly / goldfinger boundary.
   If a mechanism gains an unapproved function, solves a major conflict without protagonist choice, has no visible result, or lets other characters know hidden rules without evidence, mark REVISE.

6. Knowledge boundary.
   If reader knowledge, protagonist knowledge, other-character knowledge, and institution-verifiable facts are mixed together, mark REVISE.

## Hard Anti-AI Checks

These are high-priority checks:

1. Adjacent template reuse.
   If two similar events appear close together, check whether the second event changes narrative focus. If it repeats the same sequence with different names or details, mark REVISE.

2. Ending over-summary.
   If the chapter ending defaults to a polished, symmetrical, aphoristic, or explanatory summary line, check whether it can be replaced by action, object, bodily sensation, unfinished choice, concrete consequence, or changed relationship. If yes, mark REVISE.

## Conditional Anti-AI Checks

These are context-dependent checks:

- repeated jokes, objects, phrases, or reactions
- recurring side characters used only as response machines
- protagonist solving too many problems cleanly over time
- chapter lacking a concrete memory point when the chapter is an opening, new arc, or major turn
- chapter not advancing long-term pressure unless it is intentionally a breather
- guesses, claims, observations, or reference candidates being treated as confirmed facts

Do not apply every conditional check as a hard rule to every chapter.

## Output Format

```text
Decision: ALLOW / REVISE

Main reason:

Base-setting check:
- Reference-setting misuse:
- Authority issue:
- Process issue:
- Resource / object issue:
- Power / anomaly issue if any:
- Knowledge boundary issue:

Story check:
- Main drive:
- Long-form movement:
- Concrete memory point:

Style / anti-AI check:
- Adjacent template reuse:
- Ending over-summary:
- Other issue:

Required fixes if REVISE:
1.
2.
3.
```

List only the most important fixes.
