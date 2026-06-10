# Name And Term Gate

Use this before writing a new novel project file, character file, organization file, world file, or chapter draft.

Purpose: prevent model-default names and fake setting terms from entering canon or prose.

## Core Rule

```text
No Name And Term Gate, no new named entity.
```

This gate applies to:

- people;
- organizations;
- places;
- districts;
- objects;
- tools;
- resources;
- jobs;
- ranks;
- procedures;
- ability labels;
- status labels;
- recurring slang;
- chapter-critical objects.

## Why This Exists

The model often turns ordinary descriptions into compact genre-looking labels.

That creates fake terms that sound like setting but have no real user, no workflow, no social source, and no reason to exist.

A term is allowed only if the world itself would create it.

## People Name Check

For a person name, answer:

```text
Legal name:
Nickname / handle / work ID if any:
Who uses each version:
Social layer:
Family or institution naming logic:
Occupation or role:
Previously used in this repository: yes / no
AI-default risk: low / medium / high
Decision: ALLOW / REVISE
```

Reject names that are polished, model-favored, genre-neutral, or reused without reason.

## Organization / Place Name Check

For an organization or place name, answer:

```text
Candidate:
Type: organization / place / district / facility / route / room
Who named it:
Why this name exists:
What function it performs:
Who uses the name in speech:
Can a simpler description replace it:
Decision: ALLOW / REVISE
```

Reject names that are only stylish labels.

## Object / Process / Status / Ability Term Check

For every new term, answer:

```text
Candidate term:
Ordinary description:
Type: object / process / status / ability / job / slang / other
Who says it:
Official term or slang:
Why people would shorten or name it this way:
What first prose use must show:
Can ordinary description be clearer:
Decision: ALLOW / REVISE
```

Reject the term if:

- it only makes the prose sound genre-specific;
- nobody in the world would actually say it;
- it appears before the reader sees what it does;
- ordinary description is clearer;
- it compresses a normal color, status, object, job, or process into an invented label without need.

## Approved Output

Write approved names and terms into:

```text
novels/<novel_id>/wiki/name_registry.md
```

The registry must include:

- approved names;
- approved terms;
- who uses each term;
- whether each term is official or slang;
- first-use rule;
- rejected names and reasons;
- rejected terms and reasons.

## Drafting Rule

If a term has not passed this gate, the writer should use ordinary description instead.

Examples of ordinary description style:

```text
The gate showed yellow.
The board had been marked as scrap.
The upstairs compliance clerk came down.
The gray response had no official name yet.
```

Do not replace these with invented short labels unless the gate has approved the label.
