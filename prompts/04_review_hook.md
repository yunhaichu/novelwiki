# Review Hook Prompt

Use this prompt after a chapter draft is written and before chapter state is created.

## Inputs

Read:

- the chapter draft
- the approved chapter brief for this chapter
- the approved reader entry gate when reviewing chapter 1-3, a new volume opening, or a new major arc opening
- the approved type contract if present
- the approved project outline
- the approved volume plan
- the approved chapter beat table
- the current novel project file
- the current novel style file
- the current novel glossary / approved term list
- story bible / world state if present
- relevant character files
- relevant world, location, object, clue, or relationship files
- continuity files, including body state if present
- previous chapter state
- `governance/review_checklist.md`
- `governance/anti_ai_taste_check.md`
- `governance/emotional_payoff_check.md`
- `governance/reader_reward_check.md`
- `governance/reward_engine.md`
- `governance/longform_ai_inertia_check.md`
- `governance/low_anchor_phrase_check.md`
- `governance/style_banlist.md`
- `governance/contradiction_check.md`
- `governance/chapter_brief_review.md`
- `governance/reader_entry_review.md` when applicable
- `governance/type_contract_review.md` when applicable
- `prompts/05_golden_three_review.md` when reviewing chapters 1-3 or the opening as a unit

## Decision

Return one of:

- ALLOW
- REVISE

## Reader Hard Gates

These checks have priority over brief alignment.

If any hard gate fails, mark `REVISE` even when the draft follows the approved brief.

### 1. Stranger Reader Comprehension

A reader who has not read the wiki must be able to identify:

- who the protagonist is;
- what immediate trouble or imbalance is present;
- what the protagonist wants now;
- what can be lost soon;
- why there is a reason to read the next chapter or scene.

Mark `REVISE` if the chapter requires wiki knowledge, planning notes, or later explanations to become readable.

### 2. Genre Promise Visibility

The declared primary genre promise must be visible on the page.

Mark `REVISE` if the chapter pays only a side promise while hiding or delaying the primary promise without a deliberate and approved reason.

### 3. Opening Information Load

For chapter 1-3, new volume openings, and new major arc openings, check whether the draft introduces too many names, systems, rules, backstory items, places, organizations, or mysteries before the reader cares about the protagonist.

Mark `REVISE` if the reader has to assemble the story from fragments before knowing what to care about.

### 4. Protagonist Entry

The protagonist should enter as a person under pressure, not as a job function, setting observer, or plot device.

Mark `REVISE` if the protagonist mostly observes, processes work, or carries exposition without a visible immediate desire.

### 5. One-Sentence Recap Test

The chapter must be reducible to one ordinary sentence from a target reader's perspective.

Example shape:

```text
[Protagonist] wants/needs [immediate goal], but [obstacle/risk], so [choice/consequence].
```

Mark `REVISE` if the recap is overloaded, vague, abstract, or impossible without wiki terms.

### 6. Type Payoff

The visible reward, discovery, pressure, or denial must connect to the primary genre promise.

Mark `REVISE` if the reward is locally interesting but does not make the reader feel the promised story type.

## Checks

Check main drive, reader entry, type promise, approved brief alignment, project/volume/beat alignment, story bible consistency, terminology, low-anchor phrases, knowledge boundaries, character behavior, style, reader reward, emotional repayment, main-system relevance, contradiction risk, dialogue naturalness, anti-AI taste, and long-form AI inertia.

For chapters 1-3 or a new major opening, also check whether the chapter serves the opening design and whether the three-chapter retention unit remains strong.

## Required Story Checks

1. Reader entry.
   Apply the Reader Hard Gates above first. If the opening fails the stranger-reader test, mark REVISE.

2. Type contract alignment.
   The chapter must visibly serve the declared primary reader promise. If it signals a different genre promise without approval, mark REVISE.

3. Brief alignment.
   The chapter must follow the approved chapter brief. If it changes the engine, repeats a forbidden skeleton, or slips back into a time-order log that the brief was meant to avoid, mark REVISE.

4. Project / volume / beat alignment.
   The chapter must serve the approved project outline, volume plan, and chapter beat. If it reads like the story is inventing direction chapter by chapter, mark REVISE.

5. Terminology gate.
   Scan for unexplained terms, new place labels, job labels, system labels, evaluation labels, shorthand phrases, and genre-sounding compact terms. If a term is not ordinary language and is not approved by the glossary, mark REVISE.

6. Low-anchor phrase gate.
   Scan for pseudo-archaic quantities, vague group labels, compressed system-like labels, polished contrast lines, and motto-like narration. If an important meaning depends on such a phrase, mark REVISE.

7. First-use clarity.
   If an approved term appears for the first time in the current draft but the scene does not make its meaning clear, mark REVISE.

8. Golden-three alignment.
   For chapters 1-3, the chapter must serve its specified opening function. If chapter 1 does not create immediate reader pull, chapter 2 does not create visible payoff, or chapter 3 does not expand the hook into a longer arc, mark REVISE.

9. Reader reward.
   Identify reader desire, pressure, protagonist action, visible reward, reward confirmation, and next desire opened. If the chapter creates no visible reward or no deliberate, well-signaled delay of reward, mark REVISE.

10. Emotional repayment.
   Identify what pressure, humiliation, injustice, fear, or frustration the reader feels through the protagonist. Then identify what visible compensation or future payoff signal the chapter gives back. If the chapter only adds pressure and repays nothing visible, mark REVISE unless the beat explicitly calls for a short-term loss.

11. Visible payoff.
   The payoff must be visible on the page. It can be a win, reversal, discovery, returned humiliation, status shift, resource gain, relationship turn, new leverage, risk avoided, hostile reaction, watcher notice, clearer threat, or proof that a path is wrong. A hidden clue alone is usually not enough.

12. Social confirmation.
   If the chapter contains a payoff, check whether someone notices or reacts. A reaction is not always required, but it often makes the payoff legible. If the payoff is too private to feel real, mark REVISE.

13. Main-system relevance.
   If the chapter gives the protagonist local status, work advantage, attention, access, social movement, or process progress, it must also connect to the novel's declared primary genre promise. If it only creates local logistics or workplace treatment, mark REVISE.

   Examples:

   ```text
   cultivation/progression: resource, power, rule, sect survival
   urban/workplace: money, reputation, relationship, career pressure
   science fiction: anomaly proof, technical limit, rule discovery, human cost
   mystery: clue, contradiction, suspect relation, proof chain
   romance: relationship movement, emotional risk, choice
   farming/management: production, land, market, community defense
   officialdom/political: position, procedure, alliance, policy risk, reputation
   ```

14. Causal chain.
   The chapter's key events must follow because of prior motive, pressure, choice, or consequence. If events can be reordered without changing the story, or if they happen only because the author needs them, mark REVISE.

15. Character action logic.
   Recurring characters must act from known desire, fear, flaw, pressure, or decision pattern. If they speak their inner thesis directly, act only to explain the plot, or change behavior without a trigger, mark REVISE.

16. Dialogue naturalness.
   Dialogue should arise from desire, fear, impatience, status, misunderstanding, concealment, bargaining, or immediate practical need. If lines mainly explain the plot, ask reader questions, set up jokes, or make the protagonist look sharp, mark REVISE.

17. Dialogue readability.
   Dialogue may have subtext, but it should not make the reader work too hard. If too many lines are half-said, indirect, or ambiguous, mark REVISE.

18. Contradiction check.
   Run logic, timeline, location, motivation, information flow, rule/terminology, object/clue/resource state, foreshadow, and version-sync checks. If any hard contradiction remains, mark REVISE.

19. Long-form AI inertia.
   Check for repeated chapter skeleton, chronological log structure, repeated detail attachment, characters stating emotions too directly, local progress disconnected from the declared primary genre promise, opening reader-entry failure, and chain-like progression without a larger web. If any is severe, mark REVISE.

## Golden Three Unit Review

After chapter 3 is drafted, run a separate opening-unit review using `prompts/05_golden_three_review.md`.

Do not continue into normal long-form chapters until the opening-unit review returns PASS or the user explicitly approves proceeding despite issues.

## Hard Anti-AI Checks

These are high-priority checks:

1. Adjacent template reuse.
   If two similar events appear close together, check whether the second event changes narrative focus. If it repeats the same sequence with different names or details, mark REVISE.

2. Ending over-summary.
   If the chapter ending defaults to a polished, symmetrical, aphoristic, or explanatory summary line, check whether it can be replaced by action, object, bodily sensation, unfinished choice, concrete consequence, or changed relationship. If yes, mark REVISE.

3. Style banlist.
   If the draft repeats a known failure pattern in `governance/style_banlist.md`, mark REVISE unless the approved brief explicitly allows it for a controlled reason.

## Conditional Anti-AI Checks

These are context-dependent checks:

- repeated jokes, objects, phrases, or reactions
- recurring side characters used only as response machines
- protagonist solving too many problems cleanly over time
- chapter lacking a concrete memory point when the chapter is an opening, new arc, or major turn
- chapter not advancing long-term pressure unless it is intentionally a breather
- guesses, claims, or observations being treated as confirmed facts

Do not apply every conditional check as a hard rule to every chapter.

## Output Format

```text
Decision: ALLOW / REVISE

Main reason:

Reader entry check:
- Can a stranger reader identify the protagonist?
- Can a stranger reader identify immediate trouble?
- Can a stranger reader identify what is at stake?
- Can a stranger reader identify why to read next?
- One-sentence recap:
- Failure if any:

Genre promise check:
- Declared primary promise:
- Visible promise on page:
- Mismatch if any:

Brief alignment:
- Approved engine:
- Draft engine:
- Drift:

Project / volume / beat alignment:
- Project promise:
- Volume goal:
- Beat role:
- Draft fit:

Terminology check:
- Undefined terms:
- Terms needing clearer first use:
- Required replacements:

Low-anchor phrase check:
- Suspicious phrases:
- Required plain replacements:

Reader reward check:
- Reader desire:
- Main pressure:
- Visible reward:
- Reward confirmation:
- Next desire opened:

Main-system relevance:
- Genre / story engine:
- Local gain:
- Main-system conversion:
- What remains unsolved:

Causal chain check:
- Key cause:
- Key action:
- Key consequence:
- Weak link:

Character action logic:
- Desire / flaw / pressure:
- Surface action:
- Concealed motive:
- Issue if any:

Contradiction check:
- Logic:
- Timeline:
- Location:
- Motivation:
- Information flow:
- Rules / terminology:
- Object / clue state:
- Foreshadow:
- Version sync:

Long-form inertia check:
- Repeated skeleton:
- Chronological log structure:
- Repeated physical/detail tags:
- Character concealment issue:
- Main-system relevance:
- Reader-entry issue:
- Web connection:

Opening/golden-three check if applicable:
- Opening beat:
- Retention risk:
- Required opening fix:

Emotional ledger:
- Pressure:
- Protagonist action:
- Cost:
- Visible compensation:
- Who notices:
- New expectation:

Required fixes if REVISE:
1.
2.
3.
```

List only the most important fixes.
