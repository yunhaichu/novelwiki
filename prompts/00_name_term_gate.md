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
- civilization-level terms;
- macro-faction names;
- chapter-critical objects.

## Why This Exists

The model often turns ordinary descriptions into compact genre-looking labels.

That creates fake terms that sound like setting but have no real user, no workflow, no social source, and no reason to exist.

A term is allowed only if the world itself would create it.

## Name Risk Examples

### High-Risk Model-Favored Names

These names are not banned, but require a strong world / family / class / region reason:

```text
沈砚
陆沉
顾言
林澈
江辰
谢沉
秦川
裴行
许知
宋临
周砚
陈述
苏晚
云棠
白芷
阮清
夏禾
许栀
云无尘
谢玄微
顾长渊
沈照霜
```

Why high risk:

- polished but socially ungrounded;
- can fit any modern, xianxia, fantasy, or cyberpunk story without change;
- uses aesthetic characters that signal genre flavor more than family background;
- often appears as model-default protagonist or love-interest naming;
- does not reveal region, family expectation, occupation, class, or institution.

### Lower-Risk Grounded Names

Lower-risk examples are usually plain, socially legible, and easy to explain:

```text
陈既明
周成
梁敏
马宽
马小河
陆成
方远
韩管事
赵明川
钱管事
刘勇
何丽
```

Why lower risk:

- ordinary enough to belong to a real family or workplace;
- can reflect generation, class, job, or local naming practice;
- does not announce literary importance on first sight;
- can be explained by family, workplace, sect rank, or nickname use.

### Comparison

High-risk:

```text
谢玄微 entered the hall.
```

Better if grounded:

```text
His registry name was Xie Xuanwei, chosen by a family that had produced three ritual clerks. Outside the ancestral hall, most people still called him Old Xie’s second son.
```

Low-risk:

```text
Han Guanshi came over with the account board.
```

Reason: `Guanshi` is role-based usage. The prose does not pretend this is a rare poetic name.

## Macro Civilization Term Rule

For macro modern-to-cosmic stories:

```text
Function before name.
```

Do not introduce a long title-chain term before the reader sees what the thing does.

Bad early prose:

```text
The Taiyuan Star Alliance Low-Dimensional Civilization Observation Bureau Seventh Inspection Sequence arrived.
```

Better early prose:

```text
The woman said she was only responsible for observing civilizations that had not entered the star routes yet.
```

Later, after function is visible, the formal name may enter through dialogue, document, screen, academy registration, or faction conflict.

Macro term limits:

- one new macro term per scene unless absolutely required;
- avoid chain titles in early chapters;
- use ordinary description until function is clear;
- do not name every civilization, office, rank, artifact, law, and protocol at first mention;
- distinguish official names, slang, translations, Earth-side nicknames, and protagonist's modern analogy.

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

Reject or revise names that are polished, model-favored, genre-neutral, or reused without reason.

A high-risk name can pass only if the explanation is stronger than style preference.

## Organization / Place Name Check

For an organization or place name, answer:

```text
Candidate:
Type: organization / place / district / facility / route / room / civilization / faction / star region / dimensional zone
Who named it:
Why this name exists:
What function it performs:
Who uses the name in speech:
Can a simpler description replace it:
First prose use should show:
Decision: ALLOW / REVISE
```

Reject names that are only stylish labels.

## Object / Process / Status / Ability Term Check

For every new term, answer:

```text
Candidate term:
Ordinary description:
Type: object / process / status / ability / job / slang / civilization term / faction term / other
Who says it:
Official term or slang:
Earth translation / protagonist analogy if any:
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
- it compresses a normal color, status, object, job, civilization process, or energy behavior into an invented label without need;
- it chains too many titles together before the reader has a reason to care.

## Approved Output

Write approved names and terms into:

```text
novels/<novel_id>/wiki/name_registry.md
```

The registry must include:

- approved names;
- approved terms;
- who uses each term;
- whether each term is official, slang, translation, or protagonist analogy;
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
The woman said Earth had not been registered as a star-route civilization.
The object behaved less like a sword and more like a small engine with a blade-shaped shell.
```

Do not replace these with invented short labels unless the gate has approved the label.
