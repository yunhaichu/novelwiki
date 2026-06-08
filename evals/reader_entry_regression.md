# Reader Entry Regression Tests

Use these tests after changing prompts, governance files, or review gates related to openings.

The goal is not to generate good prose. The goal is to verify that the system rejects drafts, briefs, outlines, or beats that fail reader entry, type promise, consequence chain, or conflict escalation.

## How To Use

For each case:

1. Create a minimal artifact matching the test input.
2. Run the relevant review gate.
3. Confirm the expected decision.
4. If the reviewer returns PASS or ALLOW, update the review gate or failure library.

## Test 1: Setting Correct But Unreadable Opening

### Input Pattern

An opening brief or draft contains accurate setting, institution, transfer, world rule, or system context before the reader knows the protagonist's immediate trouble.

### Expected Review

```text
Decision: REVISE
```

### Required Reason

Reader entry failure. The setting is correct but does not yet create protagonist pressure, present desire, stake, or reason to continue.

## Test 2: Protagonist As Job Function

### Input Pattern

The protagonist appears as a worker, clerk, disciple, investigator, official, or student performing duties. The role is clear, but the protagonist has no visible immediate desire.

### Expected Review

```text
Decision: REVISE
```

### Required Reason

The protagonist enters as a job function or process executor, not as a person under pressure.

## Test 3: Too Many Mysteries Before Care

### Input Pattern

The opening introduces several mysteries, old cases, secret terms, strange objects, and unexplained institutions before the reader cares about the protagonist.

### Expected Review

```text
Decision: REVISE
```

### Required Reason

Mystery overload before reader attachment. Reduce to one primary question tied to immediate pressure.

## Test 4: Type Promise Unclear

### Input Pattern

The type contract says mystery, romance, progression, science fiction, thriller, or workplace story, but the opening does not visibly signal that primary promise.

### Expected Review

```text
Decision: REVISE
```

### Required Reason

Declared primary promise is not visible on the page.

## Test 5: Weird Hook Without Stake

### Input Pattern

The opening has a prophecy, abnormal object, strange sentence, impossible image, or system sign, but it does not change protagonist pressure, risk, relationship, proof path, or choice.

### Expected Review

```text
Decision: REVISE
```

### Required Reason

The hook is weird but not compelling. It must connect to stake or consequence.

## Test 6: Removable Chapter Beat

### Input Pattern

A beat contains a local event and a small discovery, but if the chapter is deleted, no later event collapses.

### Expected Review

```text
Decision: REVISE
```

### Required Reason

Consequence chain failure. The chapter is removable.

## Test 7: Flat Conflict

### Input Pattern

A chapter adds information and pressure, but no obstacle strengthens, no cost rises, no retreat path closes, and the protagonist's method still works cleanly.

### Expected Review

```text
Decision: REVISE
```

### Required Reason

Conflict escalation failure.

## Test 8: AI Summary Ending

### Input Pattern

The chapter ending lands on a polished summary line such as:

```text
This was not the end, but the beginning.
The real problem had only just surfaced.
Everything had changed.
```

No concrete action, object, cost, choice, or changed relationship appears at the ending.

### Expected Review

```text
Decision: REVISE
```

### Required Reason

Anti-AI novel phrase failure. Replace summary with concrete consequence.

## Test 9: Brief Passed Reader Failed

### Input Pattern

A draft satisfies all approved brief fields but a first-time reader cannot state the core reading path in one ordinary sentence.

### Expected Review

```text
Decision: REVISE
```

### Required Reason

Reader entry outranks brief alignment.

## Test 10: Story Bible Overexposure

### Input Pattern

The opening reveals multiple story-bible facts, rules, relationships, mysteries, and long-term objects before the immediate scene pressure is clear.

### Expected Review

```text
Decision: REVISE
```

### Required Reason

The story bible may know more than the reader. Opening chapters need information-delay control.

## Acceptance Standard

A compliant system must reject all ten cases.

If any case passes, the relevant review gate must be strengthened before continuing novel production.
