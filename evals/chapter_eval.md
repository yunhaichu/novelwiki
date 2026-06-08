# Chapter Evaluation

Use this rubric after chapter review or for batch evaluation of generated prose.

This rubric is designed for fiction chapters across genres. It should be used together with:

- `governance/reward_engine.md`
- `governance/contradiction_check.md`
- `governance/longform_ai_inertia_check.md`
- `governance/low_anchor_phrase_check.md`
- `governance/style_banlist.md`

## Scores

Score each item from 1 to 7.

```text
Main drive:
Causal chain:
Conflict escalation:
State change:
Character action logic:
Relationship motion:
Reader reward:
Main genre promise relevance:
Scene concreteness:
Dialogue naturalness:
Language freshness:
Continuity safety:
Hook strength:
```

## Score Anchors

### 1-2

Severe failure.

Examples:

- events happen only because the author needs them
- characters state emotions directly without action logic
- chapter is mostly process log
- no visible reward or state change
- genre promise is ignored
- new terms appear without grounding
- hard contradiction remains

### 3-4

Usable but weak.

Examples:

- chapter has a goal but weak pressure
- payoff exists but is too private or abstract
- side characters act as functions
- language is clear but generic
- main-system relevance is present but thin
- some continuity risk remains

### 5-6

Publishable draft level.

Examples:

- one clear drive
- visible state change
- reward and cost both legible
- side characters act from pressure
- dialogue is practical and readable
- no hard contradiction
- chapter hook creates real next-step desire

### 7

Strong chapter.

Examples:

- every scene changes pressure, relation, information, or method
- reward pays a reader desire while opening a stronger one
- character choices reveal desire and flaw without explanation
- prose is concrete, plain, and specific
- chapter fits volume and story bible cleanly

## Hard Gates

Mark REVISE regardless of average score if:

- hard contradiction exists
- chapter violates approved brief
- chapter ignores volume beat
- chapter repeats a banned skeleton
- chapter is mainly a morning-noon-evening log
- main genre promise is not advanced
- low-anchor phrases carry key meaning
- side characters explain theme instead of acting
- new canon facts are not logged or are unsupported

## Output Format

```text
Decision: PASS / REVISE / FAIL

Score table:
- Main drive:
- Causal chain:
- Conflict escalation:
- State change:
- Character action logic:
- Relationship motion:
- Reader reward:
- Main genre promise relevance:
- Scene concreteness:
- Dialogue naturalness:
- Language freshness:
- Continuity safety:
- Hook strength:

Average score:
Hard gate triggered: yes/no

Top 3 strengths:
1.
2.
3.

Top 3 required fixes:
1.
2.
3.
```
