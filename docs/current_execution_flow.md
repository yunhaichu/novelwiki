# Current Execution Flow

This is the short operational checklist for the current novel-generation workflow.

Use `docs/workflow_layers.md` as the authoritative full version and `docs/file_roles.md` as the file responsibility index.

## Non-Negotiable Order

```text
Irreversible Trend Anchor
-> Name & Term Gate
-> Wiki Bootstrap
-> Actor Setup
-> Chapter Trend Convergence
-> Scene Design
-> Drafting
-> Review
-> Wiki Sync
```

Do not skip forward.

## 1. Irreversible Trend Anchor

Required file:

```text
prompts/00_irreversible_trend_anchor.md
```

Run once during new-novel setup, before chapter planning.

This defines:

- world irreversible trend;
- protagonist irreversible final form;
- how the two lines force each other;
- stage map for world trend and protagonist growth.

Hard rule:

```text
No irreversible trend anchor, no chapter design.
```

The author controls the world trend and protagonist final form. Characters control local choices. Plot emerges when local choices are pulled back into the irreversible trend.

## 2. Name & Term Gate

Required file:

```text
prompts/00_name_term_gate.md
```

Run before any new:

- person name;
- organization name;
- place name;
- object name;
- process name;
- status label;
- ability / anomaly / goldfinger label;
- recurring slang;
- chapter-critical term.

Hard rule:

```text
No Name & Term Gate, no new named entity or invented term.
```

If a term has not passed the gate, use ordinary description.

Do not compress ordinary things into new terms just because they sound genre-specific.

## 3. Wiki Bootstrap

Required file:

```text
prompts/00_wiki_bootstrap.md
```

Required output files:

```text
novels/<novel_id>/wiki/project.md
novels/<novel_id>/wiki/base_settings.md
novels/<novel_id>/wiki/style.md
novels/<novel_id>/wiki/name_registry.md
novels/<novel_id>/wiki/protagonist_growth.md
```

The project wiki must include or reference:

- world irreversible trend;
- protagonist irreversible final form;
- current stage map;
- approved names and terms.

Create character / world / organization files as needed before those actors or places enter chapter planning.

Hard rule:

```text
No wiki bootstrap, no draft.
```

## 4. Actor Setup

Required for recurring major actors.

Files:

```text
prompts/00_character_behavior_model.md
prompts/00_character_expression_card.md
prompts/00_organization_behavior_model.md
```

Temporary characters may remain role labels.

If a temporary character repeatedly changes the plot, creates debt, becomes a relationship pressure, or appears across chapters, run Name & Term Gate and create a character file.

## 5. Chapter Trend Convergence

Required files for important chapters:

```text
prompts/00_reality_causal_preflight.md
prompts/02_emergent_chapter_design.md
prompts/02_advantage_reward_ledger.md
```

A chapter must not begin from a random event.

It must begin from:

- current stage of world irreversible trend;
- current stage of protagonist final form;
- local choices available to the protagonist;
- how different choices are pulled toward the same trend node.

Hard rule:

```text
No trend convergence, no chapter draft.
```

Do not create an event just to trigger a goldfinger, reveal a clue, or show a workflow.

## 6. Scene Design

Required for major scenes:

```text
prompts/02_scene_convergence.md
prompts/02_scene_expression_state.md
prompts/02_dialogue_intent.md
```

The scene must have:

- trend pressure in this scene;
- convergence point;
- actors with different local goals;
- scene function in the world;
- visible action collision;
- concrete result.

The scene should not begin from a preselected event. It should begin from actor goals under trend pressure.

## 7. Drafting

Required file:

```text
prompts/01_writer.md
```

Default prose mode:

```text
xiaobai readable prose
```

This means:

- clear action;
- clear dialogue;
- clear reaction;
- clear process;
- concrete consequence.

Do not write summary voice.

Do not reward concise abstract conclusions.

It is allowed to be a little verbose when the extra sentences show action, hesitation, repeated attempt, misunderstanding, object movement, or relationship pressure.

## 8. Review

Use targeted reviews, not every file every time.

Always for important chapters:

```text
governance/emergent_plot_review.md
governance/protagonist_growth_review.md
```

Use when language quality, AI flavor, summary voice, or invented terms appear:

```text
governance/anti_ai_expression_review.md
```

Use when records / screens / logs / reports threaten to carry the plot:

```text
governance/anti_record_driven_plot.md
```

Use when object logic matters:

```text
governance/object_function_review.md
```

## 9. Wiki Sync

Required after each approved chapter:

```text
prompts/05_wiki_sync_after_chapter.md
governance/wiki_write_rules.md
```

Always create or update:

```text
novels/<novel_id>/wiki/chapter_states/chapter_<number>.md
```

Chapter state must include:

- confirmed events;
- world trend progress;
- protagonist final-form progress;
- protagonist state;
- character / organization / object state;
- reader reward;
- reader debt;
- pressure clock;
- repetition risk;
- next chapter constraints.

Hard rule:

```text
Approved chapter -> wiki sync -> next chapter.
```

## Quick Failure Checks

Stop if any are true:

1. Irreversible trend anchor is missing.
2. New name or term appears without Name & Term Gate.
3. Chapter begins from a random event instead of trend convergence.
4. Local choices do not pull toward a shared trend node.
5. Prose uses invented shorthand where ordinary description is clearer.
6. Draft uses summary voice instead of action/dialogue.
7. Main scene has no convergence point.
8. Key object has no world function.
9. Protagonist only suffers and gains no usable final-form asset.
10. Chapter does not advance world trend or protagonist final form.
11. Chapter ends on abstract realization instead of concrete consequence.
12. Next chapter would rely on chat memory instead of wiki state.
