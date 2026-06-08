# Scene Naturalness Check

Use this during drafting, chapter review, and line revision.

This check targets prose that is structurally correct but feels artificial, over-designed, or author-labeled.

## Core Question

Does the scene feel like it is happening through the characters, objects, pressure, and social setting, or does it feel like the author is explaining what the scene means?

## Required Checks

### 1. Character-Speech Fit

Ask:

```text
Would this character say this under this pressure?
Does the diction match their status, education, role, fear, and immediate goal?
Is the line too polished for the speaker?
Is the line explaining the story for the reader instead of pursuing a scene objective?
```

Mark `REVISE` if key dialogue uses words the character would not naturally use.

### 2. Scene-Object Fit

Ask:

```text
Would this object really be labeled this way in the world?
Does the object name sound like a map label, system UI, game quest marker, or outline tag?
Could the same information be shown through rougher, shorter, more local wording?
```

Mark `REVISE` if an object or place name sounds more like author-side classification than in-world usage.

### 3. Humor Source

Humor should come from:

- role mismatch;
- pressure;
- practical misunderstanding;
- character habit;
- social hierarchy;
- failed method;
- physical inconvenience.

Mark `REVISE` if humor mainly comes from author cleverness, modern commentary, or a line that could be pasted into another story.

### 4. Explanatory Narration

Mark `REVISE` if narration tells the reader the conclusion instead of letting action or consequence show it.

Suspicious forms:

```text
X's logic was different from Y's logic.
He finally understood his role.
This was not about A, but about B.
The real problem was not outside, but inside.
```

These are allowed only when brief, concrete, and not carrying the chapter's main meaning.

### 5. Local Social Reality

Ask:

```text
What would people in this place call this thing?
How short would the name become in speech?
Would a superior use the formal name, or a rough nickname?
Would a low-status character dare say it this way?
```

Mark `REVISE` if names or dialogue ignore the social reality of the scene.

## Output Block For Review

```text
Scene naturalness:
- Suspicious dialogue:
- Suspicious object/place terms:
- Author-summary narration:
- Humor source:
- Social reality fit:
- Required changes:
```

## Decision Rule

If reader entry and structure pass but scene naturalness fails, mark:

```text
Workflow decision: PASS
Prose decision: NEEDS LINE REVISION
```

Do not mark prose publishable if key scene language feels artificial.
