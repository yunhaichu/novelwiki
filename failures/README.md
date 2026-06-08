# Failure Library

This directory stores recurring failure modes found during AI-assisted fiction creation.

Failure cases are reusable evaluation assets. They should be cited by prompts, review gates, and regression tests.

## Purpose

Use this library to prevent the same failure from being rediscovered through trial and error.

Each failure should include:

```text
Failure name:
Symptom:
Why it happens:
Bad pattern:
Detection rule:
Repair strategy:
Regression test:
Related governance files:
```

## Current Failure Categories

```text
001 low-anchor terminology
002 chronological log structure
003 repeated plot skeleton
004 direct-emotion dialogue
005 repeated physical detail tag
006 local progress without main-genre relevance
007 test-novel contamination of global rules
```

## Usage

Before drafting:

- check whether the approved brief risks repeating any failure.

During review:

- mark REVISE if the draft repeats a known failure unless the brief explicitly justifies a controlled exception.

During evaluation:

- use failure cases as regression prompts.

## Rule

Do not treat one sample novel's local setting as a global rule.

Global failures belong here.

Local story facts belong inside `novels/<novel_id>/wiki/`.
