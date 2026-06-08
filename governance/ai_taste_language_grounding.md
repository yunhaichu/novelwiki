# AI Taste Language Grounding

This note records the current understanding of AI-taste problems in generated Chinese prose.

It is not a heavy gate. Use it as a reminder when reviewing or revising drafts.

## Core Diagnosis

AI taste is not one problem.

It often appears as a combination of:

- overly smooth prose
- symmetrical sentence structures
- template phrases
- inflated abstract wording
- weak scene details
- low-grounded invented words or phrases
- characters speaking like narrative functions
- rules being explained as if in a manual

The most dangerous version is not an obviously bad sentence.

The dangerous version is a sentence that looks fluent but carries no real scene support.

## Common Failure Types In Fiction

### 1. Template Names

Names that look literary but do not feel like lived human names.

Examples from failed drafts:

```text
林砚
```

This kind of name may be valid in some stories, but if it appears by default it often signals model-generated ancient-style taste.

Prefer names with social, regional, family, or ordinary-life texture when the story needs a grounded protagonist.

### 2. Low-Grounded Phrases

Phrases that are syntactically understandable but not natural Chinese in context.

Examples:

```text
脸不老
灯里没有火
生人香火味
像是沾了点庙里的味儿
```

These fail because they are not anchored in how people actually describe things in that scene.

### 3. Rule-Manual Dialogue

Characters explain rules like a system prompt, game manual, or assessment form.

Example pattern:

```text
Each person submits X. If A, then B. If C, then D. Disputes are punished.
```

In fiction, rules should usually appear through action, failed attempts, punishment, observation, or practical speech.

### 4. Viewpoint Knowledge Leak

The narration uses a name or fact that the viewpoint character has not yet learned.

Example pattern:

```text
Someone calls him Manager Han.
The next sentence uses his full name as if the protagonist knows it.
```

If the viewpoint character only knows a role name, use the role name until the full name is naturally learned.

### 5. Weak Action Support

A character says or does something only because the story needs progress.

This is worse than wording failure.

Example pattern:

```text
The protagonist invents a weak reason.
The antagonist reacts in exactly the way needed for the plot.
```

Do not repair this by changing the phrase. Repair the action support or rerun scene simulation.

## Review Questions

Before accepting prose, ask:

```text
Is this normal Chinese?
Would this character say it this way?
Does this object need a polished label?
Does the viewpoint character know this name or fact?
Is a rule being explained instead of demonstrated?
Is this phrase grounded in a visible detail, action, or social context?
Does the key action have a real support source?
```

## Repair Principles

- Replace literary-default names with grounded names when needed.
- Replace compressed odd phrases with ordinary description.
- Show rules through one person failing or being corrected.
- Keep viewpoint knowledge strict.
- If the action support is weak, do not line-edit; go back to scene simulation.
- Do not solve AI taste by adding more ornate prose.

## Relation To Current Workflow

Use this after:

```text
Multi-Agent Scene Simulation
Scene Log To Draft
Writer Prompt
```

If the problem is only wording, revise the line.

If the problem is action support, return to scene simulation.
