# Draft Quality Review

Use this review after a chapter draft is complete and before wiki sync.

The purpose is to evaluate draft quality across consistent dimensions so that chapters can be compared and tracked for quality trends.

This is not another gate. It supplements `governance/review_checklist.md` (which checks plot logic, wiki consistency, knowledge boundaries) and `governance/anti_ai_expression_review.md` (which checks prose-level AI artifacts).

## Decision

Return one of:

```
ALLOW
REVISE
BLOCK
```

- **ALLOW** — all dimensions pass.
- **REVISE** — one or more dimensions have P1 or P2 issues.
- **BLOCK** — a P0 issue exists. The draft cannot proceed until fixed.

## Required Inputs

Read:

- current chapter draft;
- previous chapter state;
- current chapter constraints (from wiki sync or chapter design);
- novel style file;
- character files relevant to this chapter;
- `prompts/01_writer.md` for xiaobai standards.

## Quality Dimensions

Score each dimension. Use PASS / FLAG / FAIL.

### 1. Scene Grounding

Does the scene feel physically real?

PASS markers:
- At least 3 concrete sensory details (sight, sound, touch, smell, taste)
- Characters move in physical space (positions, distances, obstacles)
- Objects have visible function, not just decoration

FLAG markers:
- Only 1-2 sensory details
- Characters float in abstract space
- Objects described but not used

FAIL markers:
- Scene could happen anywhere; no specific location
- Characters are narrators, not actors
- All information delivered through screens, reports, or exposition

### 2. Prose Quality (Xiaobai Standard)

Does the prose follow xiaobai principles?

PASS markers:
- Clear subject, clear action, clear consequence in most sentences
- Dialogue carries scene weight, not narrator explanation
- Emotional pressure shown through repeated small actions
- No summary compression of scenes

FLAG markers:
- A few sentences compress a scene into a conclusion
- Some dialogue sounds like exposition delivery
- Occasional elegant phrasing where simple would work better

FAIL markers:
- Summary voice dominates; scenes are told not shown
- Dialogue explains themes instead of serving character goals
- Prose reads like a report, essay, or trailer

### 3. Chapter Structure

Does the chapter have a clear arc?

PASS markers:
- Clear opening hook (character enters with a specific trigger)
- Rising pressure or complication in the middle
- Ending lands on action, object, consequence, or unresolved choice
- One core drive, not multiple competing drives

FLAG markers:
- Opening is slow or starts too early
- Middle meanders without clear escalation
- Ending is explanatory or weakly hooked

FAIL markers:
- No clear beginning, middle, or end
- Multiple unresolved plot threads compete for attention
- Ends on narrator commentary or summary

### 4. Character Presence

Do characters feel alive?

PASS markers:
- Each speaking character has distinct speech rhythm or word choice
- Side characters have their own pressure or desire in the chapter
- Protagonist makes a choice, not just receives information

FLAG markers:
- Some characters sound interchangeable
- Side characters only respond; they never push back
- Protagonist is mostly reactive

FAIL markers:
- All characters sound the same
- Characters exist only as plot devices
- Protagonist makes no real choice

### 5. Reader Engagement

Does the chapter keep the reader hooked?

PASS markers:
- At least one reader reward (answer, reversal, clever move, relationship shift, memorable image)
- Ending creates a concrete reason to read next chapter
- Reader debt from prior chapters is addressed or escalated

FLAG markers:
- One reward, but it is vague or weak
- Ending is functional but not compelling
- Some reader debt has accumulated without movement

FAIL markers:
- No reader reward; chapter only adds mystery
- Ending is flat or explanatory
- Multiple reader debts left untouched

## Chapter Quality Log

Maintain this table across chapters.

| Ch # | Scene Grounding | Prose | Structure | Character | Reader Engagement | Overall | P0 Issues | P1 Issues | P2 Issues | Notes |
|------|-----------------|-------|-----------|-----------|-------------------|---------|-----------|-----------|-----------|-------|
| 001 | PASS | PASS | PASS | PASS | PASS | ALLOW | 0 | 0 | 0 | Opening chapter; established core hook |
| 002 | PASS | FLAG | PASS | PASS | FLAG | REVISE | 0 | 1 | 1 | Prose had one summary compression; reader reward was thin |
| 003 | | | | | | | | | | |

## Quality Trend Check (run after every 3 chapters)

- Average overall: ALLOW / REVISE / BLOCK
- Most common FLAG dimension:
- Most common P1 issue:
- Quality trend: improving / stable / declining
- If declining: specify which dimension is dragging and what to fix

## Output Format

```
Decision: ALLOW / REVISE / BLOCK

1. Scene grounding: PASS / FLAG / FAIL
- notes:

2. Prose quality: PASS / FLAG / FAIL
- notes:

3. Chapter structure: PASS / FLAG / FAIL
- notes:

4. Character presence: PASS / FLAG / FAIL
- notes:

5. Reader engagement: PASS / FLAG / FAIL
- notes:

P0 issues: (none / list them)
P1 issues: (none / list them)
P2 issues: (none / list them)

Required fixes:
1.
2.
3.

Quality log entry for this chapter:
- Ch <number>: [overall status] — [brief note]
```

## Review Standard

A chapter does not need to be perfect. A chapter that delivers one clear reader reward, has one genuinely tense moment, and ends with a concrete reason to continue is a good chapter.

A weak chapter has all of: summary prose, no reader reward, no character choice, flat ending.

A blocked chapter has a P0 issue:
- Continuity contradiction with wiki
- Character violates hard ability/authority boundary
- Prose is entirely summary (no scene)
- Plot relies on a non-canonical invention
