# Base Settings Review

Use this checklist after `prompts/00_base_settings_builder.md` creates a novel-specific base settings draft and before any reader entry gate or chapter brief is created.

The base settings file is allowed to be short. It is not allowed to be unsupported, overbroad, secretly novel-specific to a test project, or ambiguous about unresolved gaps.

## Decision

Return one of:

```text
ALLOW
REVISE
```

## Required Inputs

Read:

- base settings draft
- approved project scope
- approved type contract if present
- approved novel spine or project outline
- selected reference setting files
- `reference_settings/usage_contract.md`

## Hard Checks

### 1. Scope Check

Mark `REVISE` if the draft tries to build a full encyclopedia instead of opening and first-volume boundaries.

Mark `REVISE` if the draft decides concrete chapter outcomes, deaths, victories, recruitment, betrayals, or final solutions.

### 2. Reference / Canon Boundary

Mark `REVISE` if the draft treats reference settings as confirmed canon without adapting them to the project.

Mark `REVISE` if it says or implies that every item in a selected reference library exists in the novel world.

### 3. Support Check

For each role, organization, process, resource, location, social rule, or mechanism, identify support from:

- user input
- approved type contract
- approved novel spine / outline
- selected reference setting
- explicit project constraint

Mark `REVISE` if important settings lack support and are not listed as pending gaps.

### 4. Pending Gap Classification Check

Every pending gap must be classified as one of:

```text
blocking
non_blocking
```

Use `blocking` when the gap affects opening reader entry, protagonist motivation, immediate stake, core mechanism boundary, authority boundary, required process support, or the first chapter's main action.

Use `non_blocking` when the gap can safely remain unknown until a later chapter without weakening reader entry, action logic, or setting consistency.

Mark `REVISE` if:

- a pending gap has no classification;
- a blocking gap remains unresolved before reader-entry or chapter brief;
- a non-blocking gap is actually required for the first chapter's protagonist desire, action, cost, or visible consequence;
- the draft hides an unresolved setting problem by vague wording.

### 5. Test Novel Pollution Check

Mark `REVISE` if the draft imports names, organizations, rules, events, or local constraints from an existing test novel unless the user explicitly asked to use that test novel.

Existing `novels/` directories may be used as regression tests, not as global setting sources.

### 6. Genre Support Check

The base settings must support the declared primary genre promise.

Mark `REVISE` if:

- the setting creates a different genre promise.
- a secondary genre overtakes the primary genre without approval.
- the setting is decorative and does not affect action, risk, resource, relationship, status, or knowledge.

### 7. Authority And Process Check

Mark `REVISE` if:

- low-authority characters can perform high-authority actions without leverage, access, crisis condition, fraud, cost, or permission.
- organizations produce results without process support.
- procedures have no visible record, participant, rule, or consequence when these matter to the story.

### 8. Resource And Object Check

Mark `REVISE` if:

- major resources appear without holder, source, access condition, use, limit, or risk.
- important objects do not change action, information, relationship, status, access, or consequence.
- scarce resources become unlimited without support.

### 9. Power / Anomaly / Goldfinger Check

Apply only if the project explicitly has such a mechanism.

Mark `REVISE` if:

- the draft imports a mechanism into a project that has none.
- the mechanism has no reader-known basic rule.
- the mechanism has no stable current-stage boundary.
- the mechanism solves problems without protagonist choice.
- other characters understand the hidden mechanism without evidence.
- the mechanism has no visible result, limit, failure mode, or pressure.
- the draft adds unapproved side effects, counters, costs, or extra functions.

### 10. Knowledge Boundary Check

Mark `REVISE` if:

- reader knowledge, protagonist knowledge, other-character knowledge, and institution-verifiable facts are mixed together.
- unknowns are stated as confirmed facts.
- secrets are explained before the project needs them.

### 11. Language And Absolute Claim Check

Mark `REVISE` if the draft relies on overbroad wording such as:

```text
all
always
never
completely
inevitably
no one
anyone
absolute
permanent
```

unless the project explicitly requires that exact rule.

Prefer scoped wording:

```text
in the opening scope
within the protagonist's visible range
under current institutional rules
at the current story stage
unless later canon expands it
```

## Output Format

```text
Decision: ALLOW / REVISE

Main reason:

Scope check:
-

Reference / canon boundary:
-

Support issues:
-

Pending gap classification:
- Blocking gaps:
- Non-blocking gaps:
- Misclassified gaps:

Genre support:
-

Authority / process issues:
-

Resource / object issues:
-

Power / anomaly issues if any:
-

Knowledge boundary issues:
-

Required fixes if REVISE:
1.
2.
3.
```

List only the fixes that matter for safe downstream writing.
