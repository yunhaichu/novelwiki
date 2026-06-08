# Development Plan: Reader-Entry Novel Workflow Upgrade

This document is the canonical development plan for improving the reusable AI-assisted novel creation workflow.

The goal is not to rebuild the repository from scratch. The current staged workflow is valuable: outline, volume plan, beat table, story bible, chapter brief, draft, review, revision, chapter state, and failure library should remain. The problem is that the current system is better at preventing long-form drift and canon errors than at ensuring that a first-time reader can understand, enter, and want to continue the story.

The upgrade therefore adds three hard priorities:

1. Reader entry.
2. Type contract.
3. Consequence-driven chapter progression.

## Core Diagnosis

The existing workflow is a creation governance system. It checks planning alignment, canon consistency, low-anchor language, repeated skeletons, and chapter state updates.

It does not yet sufficiently enforce:

- whether a stranger reader can understand the opening;
- whether the primary genre promise is visible on the page;
- whether the protagonist has an immediate desire and pressure;
- whether a chapter creates consequences that force the next chapter;
- whether conflict escalates through higher cost, stronger opposition, or fewer retreat paths;
- whether a draft can be rejected for being readable to the system but unreadable to the target reader.

This plan upgrades the workflow from:

```text
outline -> volume -> beat -> brief -> draft -> review -> revision -> canon update
```

to:

```text
project scope
-> type contract
-> reader entry gate for openings
-> outline / volume / beat
-> story bible
-> opening brief or normal chapter brief
-> draft
-> reader-aware review
-> revision
-> canon update
-> failure library regression
```

## Operating Principles

All future prompt and governance updates should follow these priorities:

1. Reader entry is more important than setting completeness.
2. Type promise is more important than topic decoration.
3. Immediate protagonist desire is more important than protagonist background.
4. Consequence is more important than event.
5. Escalation is more important than noise.
6. Visible choice is more important than inner explanation.
7. Target-reader recap is more important than model self-review.
8. Opening failure allows structural rewrite; it should not default to minimal line repair.

## Phase 1: Clean Global Governance Pollution

### Goal

Restore global workflow rules to topic-neutral and genre-neutral form.

### Problem

Some global governance material still contains local test-novel assumptions, especially cultivation-specific phrasing. A global workflow must not require every local process to convert into cultivation relevance.

### Required Changes

Update global governance language from:

```text
Work Must Convert Into Cultivation Relevance
```

to:

```text
Local Process Must Convert Into Declared Main Genre Promise
```

Use genre-neutral examples:

```text
cultivation: resource, rule understanding, power progress, sect survival
mystery: clue, contradiction, proof chain, suspect relation
urban: status, reputation, career pressure, money, social/legal risk
science fiction: anomaly proof, rule discovery, technical limit, human cost
romance: relationship movement, emotional risk, repair, intimacy, commitment
farming/management: resource chain, production, market, land, community defense
officialdom/political: position, procedure, alliance, policy risk, public reputation
```

### Files To Update

```text
governance/longform_ai_inertia_check.md
governance/chapter_brief_review.md
prompts/02_chapter_brief.md
prompts/04_review_hook.md
```

### Acceptance Criteria

- No global file should hard-code a local test novel's genre, setting, rules, terms, or deadlines.
- Local genre examples are allowed only as examples, not as mandatory checks.
- Any local rule belongs under `novels/<novel_id>/wiki/`, not under global `governance/`.

## Phase 2: Add Type Contract Sheet

### Goal

Make every novel explicitly state its reader-facing type promise before outline, beat, and chapter drafting.

### Rationale

Type fiction works through a reader contract. The question is not only what the story is about, but what reading payoff it promises: truth, power, status, relationship, fear release, wonder, justice, survival, or another dominant reward.

### New Files

```text
prompts/00_type_contract.md
governance/type_contract_review.md
```

### Type Contract Output

```text
Project title:
Primary genre:
Secondary genre if any:
Primary reader promise:
What reader expects by chapter 1:
What reader expects by chapter 3:
What reader expects by volume 1 end:
Main payoff type:
- truth / power / status / relationship / survival / wonder / justice / fear release / other
Opening must show:
Opening must not hide:
Forbidden false promises:
If genre-blended, which genre is primary:
How secondary genre supports primary genre:
Type drift risks:
```

### Review Rules

Mark `REVISE` if:

- the primary genre cannot be identified;
- the secondary genre overtakes the primary genre without explanation;
- the first three chapters do not visibly signal the primary promise;
- readers may enter under the wrong genre expectation;
- the type promise exists only in planning notes and cannot be seen from prose.

### Files To Integrate

```text
prompts/00_outline_generation.md
governance/outline_review.md
prompts/00_volume_planner.md
governance/volume_review.md
prompts/00_beat_generator.md
governance/beat_review.md
prompts/02_chapter_brief.md
prompts/04_review_hook.md
```

### Acceptance Criteria

- Every novel instance has a type contract before prose drafting.
- Reader reward fields must be tied to the primary genre promise.
- Mixed-genre projects must state which promise controls the ending and opening.

## Phase 3: Add Reader Entry Gate

### Goal

Prevent openings that are correct in plan but unreadable to a first-time reader.

### New Files

```text
prompts/00_reader_entry_gate.md
governance/reader_entry_review.md
```

### When To Use

Use before drafting:

- chapter 1;
- chapters 1-3 as an opening unit;
- a new volume opening;
- a new major arc opening;
- the first appearance of a major new system, world area, genre mechanism, or protagonist reset.

### Reader Entry Gate Output

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
6. Why should reader continue?

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
End-of-chapter question:
One-sentence reader recap target:
```

### Review Rules

Mark `REVISE` if:

- a first-time reader cannot identify the protagonist in the first 500 words;
- the immediate trouble is unclear;
- the protagonist has no visible immediate desire;
- the cost of inaction is unclear;
- the opening requires the reader to process too many names, systems, rules, backstory items, or unresolved mysteries before caring about the protagonist;
- the chapter is strange but not compelling;
- the intended one-sentence reader recap cannot be stated in ordinary language.

### Acceptance Criteria

- Chapter 1 cannot proceed to draft without a passed reader entry gate.
- New arc openings cannot proceed without a reader entry check.
- Reader entry failure outranks brief alignment.

## Phase 4: Split Chapter Brief Into Opening and Normal Briefs

### Goal

Avoid overloading chapter 1 with every planning field from the normal brief.

### New Files

```text
prompts/02_opening_chapter_brief.md
governance/opening_chapter_brief_review.md
```

### Opening Brief Output

```text
Chapter number:
Primary reader promise:
Protagonist entry:
Immediate pressure:
Protagonist visible desire:
Obstacle:
Cost if no action:
One active choice:
Visible consequence:
One concrete memory point:
Information withheld:
End hook:
One-sentence reader recap target:
```

### Opening Brief Rules

For chapters 1-3 and major new openings:

- do not start with world explanation;
- do not introduce too many proper nouns or system labels;
- do not let the protagonist appear only as a job function, observer, or process executor;
- do not use backstory labels as substitutes for present pressure;
- do not use mystery as a substitute for stake;
- do not use setting wonder as a substitute for protagonist situation.

### Acceptance Criteria

- Opening chapters use the opening brief, not the full normal brief.
- Normal chapter brief remains available for ordinary long-form production.
- Drafting must follow the approved opening brief for chapter 1-3.

## Phase 5: Rewrite Chapter Review Priority

### Goal

Make reader comprehension a hard gate, not a soft observation.

### File To Update

```text
prompts/04_review_hook.md
```

### Add Hard Reader Gates

```text
Hard Reader Gates:

1. Stranger Reader Comprehension
If a reader who has not read the wiki cannot identify protagonist, immediate trouble, active choice, and next reason to read, mark REVISE.

2. Genre Promise Visibility
If the chapter does not visibly signal the declared primary genre promise, mark REVISE.

3. Opening Information Load
For chapter 1-3 or new arc openings, if the draft requires the reader to process too many names, systems, rules, backstory items, or unresolved mysteries before caring about the protagonist, mark REVISE.

4. Protagonist Entry
If the protagonist appears as a job function, setting observer, or plot device instead of a person under pressure, mark REVISE.

5. One-Sentence Recap Test
If the chapter cannot be recapped in one ordinary sentence by a target reader, mark REVISE.

6. Type Payoff
If the visible reward does not connect to the primary genre promise, mark REVISE even if it is locally interesting.
```

### Review Output Additions

```text
Reader entry check:
- Can a stranger reader identify protagonist?
- Can a stranger reader identify immediate trouble?
- Can a stranger reader identify what is at stake?
- Can a stranger reader identify why to read next?
- One-sentence recap:
- Failure if any:

Genre promise check:
- Declared primary promise:
- Visible promise on page:
- Mismatch if any:
```

### Acceptance Criteria

- A draft can no longer pass only because it follows the brief.
- Opening comprehension failure forces `REVISE`.
- Review must explicitly diagnose reader-entry success or failure.

## Phase 6: Add Consequence Chain Gate

### Goal

Ensure chapters are driven by cause, action, consequence, and forced next action rather than event listing.

### New File

```text
governance/consequence_chain_check.md
```

### Check Fields

```text
Opening state:
Protagonist action:
Immediate consequence:
Who reacts:
What becomes harder:
What path closes:
What new path opens:
What must happen next because of this chapter:
If this chapter is removed, what later event collapses:
```

### Review Rules

Mark `REVISE` if:

- deleting the chapter does not affect later events;
- the chapter only adds information but does not change action pressure;
- the ending does not force or strongly motivate a next action;
- events can be freely reordered without changing causality;
- the chapter reads as `and then` rather than `therefore`, `as a result`, or `instead`.

### Files To Integrate

```text
prompts/00_beat_generator.md
governance/beat_review.md
prompts/02_chapter_brief.md
governance/chapter_brief_review.md
prompts/04_review_hook.md
```

### Acceptance Criteria

- Every beat and brief must name a forced consequence.
- Review must identify what future event depends on this chapter.
- Chapters with removable events should be revised or merged.

## Phase 7: Add Conflict Escalation Gate

### Goal

Ensure chapters raise cost, strengthen opposition, reduce retreat paths, or force strategy change.

### New File

```text
governance/conflict_escalation_check.md
```

### Check Fields

```text
Conflict before chapter:
Conflict after chapter:
Obstacle stronger? yes/no:
Cost higher? yes/no:
Retreat path reduced? yes/no:
Opponent / system adapts? yes/no:
Protagonist method still works? yes/no:
If method fails or partially fails, how:
Escalation type:
- risk
- time pressure
- relationship
- resource
- reputation
- physical danger
- moral cost
- knowledge contradiction
- rule limit
```

### Review Rules

Mark `REVISE` if:

- the chapter adds only new information without escalation;
- the chapter adds only pressure without protagonist action;
- the protagonist acts but pays no cost;
- adjacent chapters use the same escalation type without variation;
- the protagonist's method keeps working cleanly over multiple chapters.

### Files To Integrate

```text
prompts/00_beat_generator.md
governance/beat_review.md
prompts/02_chapter_brief.md
governance/chapter_brief_review.md
prompts/04_review_hook.md
```

### Acceptance Criteria

- Each chapter beat identifies a specific escalation type or controlled non-escalation.
- Chapter review checks whether the conflict actually changes.
- Repeated flat pressure becomes a revision trigger.

## Phase 8: Upgrade Character Action Logic

### Goal

Make characters act from desire, fear, flaw, and decision pattern rather than from author convenience.

### New Files

```text
prompts/00_character_action_logic.md
governance/character_action_review.md
```

### Character Logic Fields

```text
External desire:
Inner need:
Core fear:
Dominant flaw:
Flaw trigger:
Default protection priority:
- life / status / relationship / principle / control / truth / belonging / freedom
Information threshold:
- acts on instinct / waits for evidence / avoids decision / over-verifies
Conflict mode:
- compete / avoid / compromise / submit / cooperate / manipulate
Self-justification:
First wrong method:
How this flaw creates plot:
Arc direction:
```

### Chapter-Level Additions

Add to opening and normal briefs:

```text
Why must protagonist act now?
What does protagonist protect first in this scene?
Which flaw is triggered?
What wrong or partial choice does this produce?
What consequence does that choice create?
```

### Review Rules

Mark `REVISE` if:

- the protagonist acts only because the plot needs it;
- the protagonist has no immediate desire;
- a stated flaw creates no action cost;
- a recurring character explains their whole inner position directly;
- the same character behaves like a different person without a trigger.

### Files To Integrate

```text
prompts/00_story_bible_builder.md
governance/story_bible_review.md
prompts/02_chapter_brief.md
prompts/02_opening_chapter_brief.md
prompts/01_writer.md
prompts/04_review_hook.md
```

### Acceptance Criteria

- Character cards include action logic, not only labels.
- Draft review checks action logic against scene pressure.
- Major character decisions require a visible trigger.

## Phase 9: Expand Anti-AI Novel Taste Checks

### Goal

Reject generic AI novel phrasing, abstract emotional labels, and polished summary endings.

### New File

```text
governance/anti_ai_novel_phrase_check.md
```

### Phrase Classes

#### 1. Emotion Labels

```text
心跳漏了一拍
心里一紧
说不清是什么感觉
有那么一瞬间
```

#### 2. Summary Endings

```text
这不是结束，而是开始
真正的问题才刚刚浮出水面
他终于明白
这一次，不一样了
```

#### 3. Fake Suspense Lines

```text
没人知道，命运的齿轮已经转动
他还不知道，危险正在靠近
```

#### 4. Abstract Relationship Lines

```text
两人的关系发生了微妙变化
空气安静下来
沉默说明了一切
```

#### 5. Generic Realization Lines

```text
答案一直在他心里
他真正要面对的是自己
```

#### 6. Compressed Setting Labels

```text
旧日规则
命运缝隙
秩序背面
时代残响
```

### Review Rules

Mark `REVISE` if:

- a key payoff depends on an abstract phrase;
- an opening or ending lands on a polished summary instead of action, object, choice, cost, or changed relationship;
- multiple AI-taste phrases appear in one chapter;
- character dialogue uses labels rather than practical speech under pressure.

### Acceptance Criteria

- Chapter endings prefer concrete consequence over theme summary.
- Emotional changes are shown through action, speech, pressure, and choice.
- Generic AI-taste lines become revision triggers.

## Phase 10: Add Opening Failure Library

### Goal

Convert known opening failures into reusable regression cases.

### New Directory

```text
failures/opening_reader_entry/
```

### Initial Failure Case Files

```text
failures/opening_reader_entry/setting_correct_but_unreadable.md
failures/opening_reader_entry/protagonist_as_job_function.md
failures/opening_reader_entry/too_many_mysteries_before_care.md
failures/opening_reader_entry/type_promise_unclear.md
failures/opening_reader_entry/hook_is_weird_not_compelling.md
failures/opening_reader_entry/brief_passed_reader_failed.md
failures/opening_reader_entry/backstory_label_without_emotional_anchor.md
failures/opening_reader_entry/wiki_overexposure_in_chapter_1.md
```

### Failure Case Template

```text
Failure name:
Symptom:
Why it happens in LLM writing:
Reader effect:
Detection questions:
Reject rule:
Repair strategy:
Regression prompt:
Expected reviewer decision:
```

### Required Initial Case

```text
Failure name:
Brief Passed, Reader Failed

Symptom:
The draft satisfies approved brief fields but a first-time reader cannot identify the core reading path.

Reader effect:
The reader sees many valid elements but cannot decide what to care about.

Reject rule:
If a chapter requires wiki knowledge to feel clear, mark REVISE.

Repair strategy:
Reduce opening to protagonist + immediate pressure + one abnormal object / choice + visible cost.
Delay backstory, system terms, and secondary mysteries.
```

### Acceptance Criteria

- New failures must be added when user or reviewer identifies a repeatable pattern.
- A draft that repeats a failure case must be marked `REVISE` unless the brief explicitly allows a controlled exception.
- Failure cases should be used as regression tests before continuing system development.

## Phase 11: Upgrade Golden Three Review

### Goal

Make the first three chapters a reader-retention unit, not only three aligned chapters.

### File To Update

```text
prompts/05_golden_three_review.md
```

### Structural Review Layer

```text
Chapter 1:
- protagonist entry
- immediate pressure
- type promise signal
- visible choice
- concrete memory point
- reason to chapter 2

Chapter 2:
- pressure proves real
- protagonist active method
- visible cost
- visible gain
- someone reacts

Chapter 3:
- gain widens story
- relationship shifts
- long-term arc opens
- chapter 4 concrete hook
```

### Reader Recap Layer

A target reader should be able to answer:

```text
1. What kind of story is this?
2. Who is the protagonist?
3. What does the protagonist want now?
4. What blocks them?
5. What has changed by chapter 3?
6. What do they expect next?
7. What is the most memorable object/action/conflict?
```

### Review Rules

Mark `REVISE` if:

- the reader cannot identify the primary type;
- the protagonist's immediate desire is unclear;
- chapter 1 spends too long on setup before pressure appears;
- chapter 2 adds hardship without visible gain;
- chapter 3 resets into another local task instead of widening the story;
- no concrete memory point remains after three chapters.

### Acceptance Criteria

- No project should continue into normal long-form production until the opening unit passes.
- If the first three chapters fail reader recap, revise structurally before continuing.

## Updated Canonical Workflow

```text
Stage 0: Project Scope
-> Stage 0.5: Type Contract
-> Stage 1: Project Outline
-> Stage 1.5: Outline Review
-> Stage 2: Volume Plan
-> Stage 2.5: Volume Review
-> Stage 3: Beat Table
-> Stage 3.5: Beat Review
-> Stage 4: Story Bible
-> Stage 4.5: Story Bible Review
-> Stage 5a: Reader Entry Gate / Opening Brief for chapter 1-3 or new major openings
-> Stage 5b: Normal Chapter Brief for ordinary chapters
-> Stage 5.5: Brief Review
-> Stage 6: Chapter Draft
-> Stage 7: Chapter Review with Reader Hard Gates
-> Stage 8: Revision
   - normal failure: minimal sufficient repair
   - opening failure: structural rewrite allowed
-> Stage 9: Chapter State / Story Bible Update
-> Stage 10: Evaluation / Failure Library Update
```

## Implementation Order

### Round 1: Reader Entry First

Actions:

1. Clean global cultivation-specific governance.
2. Add `00_reader_entry_gate.md`.
3. Add `reader_entry_review.md`.
4. Add reader hard gates to `04_review_hook.md`.
5. Add opening reader failure cases.

Acceptance test:

A chapter that satisfies its brief but cannot be understood by a first-time reader must be marked `REVISE`.

### Round 2: Type Contract

Actions:

1. Add `00_type_contract.md`.
2. Add `type_contract_review.md`.
3. Update outline, beat, brief, and review prompts to read the type contract.
4. Require reader reward to bind to the primary genre promise.

Acceptance test:

A mixed-genre premise must state its primary promise and opening payoff. If it cannot, mark `REVISE`.

### Round 3: Consequence and Escalation

Actions:

1. Add `consequence_chain_check.md`.
2. Add `conflict_escalation_check.md`.
3. Integrate both into beat, brief, and review stages.

Acceptance test:

A chapter that can be removed without later collapse must be marked `REVISE` or merged.

### Round 4: Character Logic and Anti-AI Taste

Actions:

1. Add `00_character_action_logic.md`.
2. Add `character_action_review.md`.
3. Update story bible character fields.
4. Add `anti_ai_novel_phrase_check.md`.
5. Integrate anti-AI phrase checks into writer and review.

Acceptance test:

A chapter where the protagonist observes and executes tasks without immediate desire, flaw-triggered choice, or visible cost must be marked `REVISE`.

## Regression Test Set

Create tests across at least six opening types:

```text
1. Cultivation opening: ordinary youth enters a sect; must not become labor log.
2. Urban mystery opening: abnormal evidence appears; reader must understand the problem within 500 words.
3. Fantasy/progression opening: weak status, desire, cost, and progress promise must be visible.
4. Romance opening: relationship tension must appear before background explanation dominates.
5. Science fiction opening: human problem first, mechanism later.
6. Officialdom/workplace opening: procedure pressure must convert into status, risk, relationship, or choice.
```

Each test should run:

```text
Type Contract
Reader Entry Gate
Opening Brief
Draft
Review
Golden Three Review if applicable
```

### Regression Acceptance Criteria

The system must:

- reject drafts that are setting-correct but reader-inaccessible;
- identify which information should be delayed;
- bind visible reward to primary genre promise;
- identify chapter consequence and forced next action;
- identify conflict escalation or lack of escalation;
- reject generic AI-taste openings and endings;
- allow structural rewrite for failed openings.

## Final Target

The upgraded workflow should not merely generate more artifacts. It should reject more bad drafts earlier.

A successful version of the system should be able to say:

```text
This draft follows the brief, but a target reader cannot enter the story. Mark REVISE.
```

That is the main behavioral change required by this plan.
