# Reader Entry Gate Prompt

Use this prompt before drafting chapter 1, chapters 1-3, a new volume opening, a new major arc opening, or the first appearance of a major new system.

The goal is not to write prose. The goal is to ensure that a first-time target reader can enter the story without reading the wiki.

## Required Inputs

Read:

- type contract if present
- project outline if present
- opening or golden-three design if present
- current style file if present
- forbidden patterns
- any user-specified opening requirements

Do not rely on story bible knowledge to make the opening understandable. The reader does not have the wiki.

## Output Object

Produce:

```text
Chapter / opening unit:
Target reader:
Primary genre promise:

First 500 words must make clear:
1. Who is the protagonist?
2. What immediate trouble is present?
3. What does the protagonist want right now?
4. What can be lost soon?
5. What is strange / unfair / dangerous / desirable?
6. Why should the reader continue?

Reader should remember only these 3-4 things:
1.
2.
3.
4.

Information allowed now:
Information delayed:
Terms forbidden in opening:
Worldbuilding limit:
Backstory limit:

Opening action / pressure:
Opening image or object:
Protagonist visible choice:
Visible cost or consequence:
End-of-chapter question:
One-sentence reader recap target:
```

## Rules

- The opening must not require wiki knowledge.
- Do not solve reader confusion by adding more explanation. Prefer fewer elements and stronger pressure.
- The protagonist should enter as a person under pressure, not as a job function, observer, or setting tour guide.
- Backstory is allowed only if it changes present pressure.
- Mystery is allowed only if the reader already knows what is at stake.
- Setting detail is allowed only if it helps the reader understand pressure, desire, cost, or type promise.
- Introduce fewer proper nouns than the system knows.
- Delay secondary mysteries unless they sharpen the immediate problem.

## Hard Failure Patterns

Mark these as risks in the output if present:

```text
setting-correct but unreadable
protagonist appears as job function
opening explains world before pressure
many mysteries before reader cares
many names before reader knows the protagonist
backstory label without emotional anchor
type promise unclear
hook is weird but not compelling
```

## Output

Output only the reader entry gate artifact.
