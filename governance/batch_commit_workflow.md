# Batch Commit Workflow

This repository should avoid file-by-file commits during normal novel creation.

## Purpose

A novel workflow step should prepare all required file changes first, then write them as one coherent commit.

This reduces noisy history and keeps each commit tied to one clear creative operation.

## Commit Unit

Use one commit for each complete workflow stage.

Recommended commit units:

- initialize one novel workspace
- write one chapter draft and related initial character wiki files
- revise one chapter and sync related wiki files
- approve one chapter and add its chapter state
- update global prompts or governance rules

## Do Not Commit This Way

Avoid this pattern during normal workflow:

```text
create one file
commit
create another file
commit
update state
commit
update name registry
commit
```

This creates too many commits and makes review harder.

## Preferred Flow

1. Read the relevant current files.
2. Prepare the full change set in memory.
3. List all files to be created or updated.
4. Check for knowledge-boundary problems before writing.
5. Write all changes in one commit when possible.

## Change Set Format

Before writing, prepare a change set like this:

```text
Change Set

Purpose:

Files to create:
- path

Files to update:
- path

Files to delete:
- path

Canon impact:
- none / low / medium / high

Requires human approval:
- yes / no
```

## Git Write Strategy

When tool support allows it, prefer:

```text
create blobs
create tree
create commit
update branch ref
```

This creates one commit containing all file changes.

If only file-level writes are available, minimize writes and group related content into the fewest safe commits.

## Safety Rules

Do not batch-write speculative wiki facts.

Do not mix unrelated workflow stages in one commit.

Do not combine multiple novels in one commit unless the change is a global prompt or governance update.

Do not update a chapter state before the related chapter passes review.

## Example Commit Messages

```text
Initialize Qingheng novel workspace

Add Qingheng chapter 001 draft and initial character wiki

Revise Qingheng chapter 001 for knowledge boundaries

Add Qingheng chapter 001 state after review

Update governance batch commit workflow
```
