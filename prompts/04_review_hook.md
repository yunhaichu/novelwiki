# Review Hook Prompt

Use this prompt after a chapter draft is written and before chapter state is created.

## Inputs

Read:

- the chapter draft
- the approved reader entry gate when reviewing an opening chapter
- the approved opening chapter brief or normal chapter brief if present
- the current novel project file
- the current novel base settings file if present
- the current novel style file
- relevant character files
- relevant world, location, organization, process, object, or relationship files
- previous chapter state
- `governance/review_checklist.md`
- `governance/base_settings_review.md` when a setting boundary is involved
- `governance/anti_ai_taste_check.md`
- `governance/review_priority.md` — always read this to determine review priority and conflict resolution

## Priority Rule

All review checks are categorized into four priority levels.
Read `governance/review_priority.md` for the full priority definitions and conflict resolution rules.

- **P0 — Block**: reality logic, base settings, name gate, wiki write rules, protagonist growth, wiki retrieval. Hard stop.
- **P1 — Must fix before canon**: reader hook/payoff, reader debt enforcement, consequence chain, scene convergence, protagonist advantage, wiki conflict.
- **P2 — Should fix**: AI expression, AI taste, character voice, writing style, narrative economy.
- **P3 — Observation only**: volume rhythm, wiki drift, name registry.

When conflicts arise between review findings, resolve them using the priority system in `review_priority.md`.

## Decision

Return one of:

- ALLOW
- REVISE

Do not use ambiguous pass language such as `mostly yes`, `basically okay`, or `acceptable but unclear` for hard gates.

For hard gates, the answer is either pass or fail. If a gate is partial, mark `REVISE`.

## Checks

Check main drive, reader entry, wiki consistency, base-setting consistency, knowledge boundaries, character behavior, authority and process boundaries, resource and object support, style, long-form direction, reader itch, and anti-AI taste.

## Hard Reader-Entry Checks

Apply to chapter 1, chapters 1-3, volume openings, and major arc openings.

Mark `REVISE` if any answer is not clearly yes:

1. A first-time target reader can identify the protagonist in the first 500 words.
2. The protagonist has a visible immediate desire.
3. The immediate trouble is present on the page.
4. The cost of no action is concrete.
5. The protagonist makes or approaches one active choice.
6. The choice creates or threatens a visible consequence.
7. The reader itch is concrete and tied to protagonist pressure.
8. The one-sentence recap can be stated in ordinary language.
9. No blocking setting gap remains unresolved.

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

## Process Exposition Check

Mark `REVISE` if process rules are explained in consecutive blocks without being forced by action, refusal, disabled option, message, warning prompt, record contradiction, or consequence.

Process details should be carried by visible friction.

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

When all review checks are complete, produce a prioritized summary:

```text
Review Summary

P0 Issues (block):
1. [file] description — action needed

P1 Issues (must fix):
1. [file] description — action needed

P2 Issues (should fix):
1. [file] description — action needed

P3 Issues (observation):
1. [file] description — note only

Decision: BLOCK / REVISE / ALLOW
Blocking reason (if any):

Required fixes if REVISE:
1. [P1 or higher] description
2. [P1 or higher] description
```

- P0 issues always produce a BLOCK decision.
- If only P1 issues exist, use REVISE but explain which are critical vs. optional.
- If only P2/P3 issues exist, use ALLOW but note what should be improved.
- List only fixes at P1 or above in the "Required fixes" section.
- Use the conflict resolution rules in `governance/review_priority.md` when findings disagree.
