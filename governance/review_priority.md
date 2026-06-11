# Review Priority Sort

When multiple review files are triggered, they do not all carry the same weight.

This file defines the priority of each review, how conflicts between them are resolved, and when reviews can run in parallel.

## Priority Levels

### P0 — Block Draft / Block Sync (hard stop)

These checks MUST pass before the next stage can proceed.

- **Reality logic**: event violates genre reality, authority, timing, survival cost, institution logic, role knowledge
- **Base settings**: reference settings used as canon; character action beyond role/access/authority/knowledge/resources without visible leverage, cost, fraud, permission
- **Name gate**: new name or term that has not passed the Name Gate
- **Wiki write rules**: fact written without approved source; planning file used as canon; speculation written as confirmed fact
- **Protagonist growth**: growth recorded without concrete cost or usable leverage; forbidden jump attempted
- **Wiki retrieval rules**: character knows information outside their knowledge boundary; reference settings from another novel used

If any P0 check fails, the chapter or wiki update must be revised before proceeding.

### P1 — Must Fix Before Canon (strong requirement)

These checks should be resolved before the chapter is approved as canon.

- **Reader hook/payoff**: important chapter has no concrete reason for readers to continue
- **Reader debt**: critical debt has exceeded its maximum delay from the volume plan; debt carried forward without any partial payment for too long
- **Consequence chain**: chapter ends on abstract realization instead of concrete consequence
- **Scene convergence**: main scene has no convergence point
- **Protagonist advantage**: protagonist suffers with no usable final-form asset; planned advantages not delivered without explanation
- **Wiki conflict**: chapter contradicts existing wiki without following the conflict handling workflow
- **Reader debt enforcement**: a debt from the volume plan exceeds its maximum delay; no structural change is planned to address it

If any P1 check flags an issue, note it as a required fix but allow proceed if the user explicitly approves.

### P2 — Should Fix (recommended)

These checks improve quality but do not block execution.

- **AI expression**: pretty summary, unsupported metaphor, generic body reaction, identity label sentence, psychological summary, dialogue-as-narration, same rhythm, record-centered expression
- **AI taste**: template reuse, ending pattern, repeated joke, concrete memory points, long-form direction
- **Character voice**: source-ungrounded speech, listener-unaware dialogue, missing environmental modulation
- **Writing style**: prose uses summary voice; process shown as explanation instead of scene friction; world function missing
- **Narrative economy**: sentence does not move action, change pressure, change relationship, expose a choice, create image, change info state, produce consequence, or preserve reader hook
- **Protagonist growth**: vague growth recorded without tied-to-later-action consequence

If P2 issues are found, fix them when they are clear and actionable. Do not block execution.

### P3 — Observation Only

These are structural warnings for the workflow designer, not per-chapter fixes.

- Volume rhythm: consecutive chapters with no state movement; repeated hook type without structural upgrade
- Wiki drift: accumulated debt across multiple chapters approaching the volume's maximum delay
- Name registry: new terms accumulating without systematic review

## Conflict Resolution

When different reviews flag conflicting issues:

1. **P0 always overrides P1, P2, P3.** A blocked draft cannot proceed regardless of other review outcomes.
2. **P1 overrides P2 and P3.** If the story structure is weak, style fixes come after structural fixes.
3. **Within the same priority level**, resolve conflicts by:
   - Reality logic and base settings take precedence over reader hook/payoff concerns
   - Protagonist advantage takes precedence over scene-level concerns
   - Reader debt enforcement takes precedence over AI expression fixes
4. **If a P2 fix would worsen a P1 issue**, defer the P2 fix until the P1 issue is resolved.
   - Example: expanding prose to show a reaction (P2 fix) should not obscure the concrete consequence the chapter needs (P1 requirement).

## Execution Order

When multiple reviews are triggered for a single chapter, run them in this order:

```text
1. wiki retrieval rules (before writing)
2. reality logic review
3. base settings review
4. name gate check
5. wiki write rules check (before wiki sync)
6. emergent plot review
7. protagonist growth review
8. wiki conflict handling (if needed)
9. character voice review
10. anti-AI expression review
11. anti-AI taste check
12. reader hook/payoff evaluation
```

Some reviews can run in parallel when they do not share input:

```text
Parallel group A: reality logic + base settings + name gate
Parallel group B: character voice + anti-AI expression + anti-AI taste
Sequential after A and B: emergent plot + protagonist growth + wiki conflict handling
Final: wiki write rules + reader hook/payoff evaluation
```

## Output Format

When running multiple reviews, the combined output should look like:

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
```

Do not list every check as equally important. The user needs to see what must be fixed versus what is optional.
