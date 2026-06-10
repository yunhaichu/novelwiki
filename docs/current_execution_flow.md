# Current Execution Flow

This is the short operational checklist for the current novel-generation workflow.

Use `docs/workflow_layers.md` as the authoritative full version and `docs/file_roles.md` as the file responsibility index.

## Non-Negotiable Order

```text
Name & Term Gate
-> Wiki Bootstrap
-> Actor Setup
-> Chapter Preflight
-> Scene Design
-> Drafting
-> Review
-> Wiki Sync
```

Do not skip forward.

## 1. Name & Term Gate

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

Examples of ordinary description:

```text
The gate showed yellow.
The board had been marked as scrap.
The upstairs compliance clerk came down.
The gray reaction had no official name yet.
```

Do not compress ordinary things into new terms just because they sound genre-specific.

## 2. Wiki Bootstrap

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

Create character / world / organization files as needed before those actors or places enter chapter planning.

Hard rule:

```text
No wiki bootstrap, no draft.
```

## 3. Actor Setup

Required for recurring major actors.

Files:

```text
prompts/00_character_behavior_model.md
prompts/00_character_expression_card.md
prompts/00_organization_behavior_model.md
```

Temporary characters may remain role labels.

If a temporary character repeatedly changes the plot, creates debt, becomes a relationship pressure, or appears across chapters, run Name & Term Gate and create a character file.

## 4. Chapter Preflight

Required files for important chapters:

```text
prompts/00_reality_causal_preflight.md
prompts/02_emergent_chapter_design.md
prompts/02_advantage_reward_ledger.md
```

The chapter event must grow from the world model.

Do not create an event just to trigger a goldfinger, reveal a clue, or show a workflow.

## 5. Scene Design

Required for major scenes:

```text
prompts/02_scene_convergence.md
prompts/02_scene_expression_state.md
prompts/02_dialogue_intent.md
```

The scene must have:

- convergence point;
- actors with different local goals;
- scene function in the world;
- visible action collision;
- concrete result.

## 6. Drafting

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

## 7. Review

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

## 8. Wiki Sync

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

1. New name or term appears without Name & Term Gate.
2. Prose uses invented shorthand where ordinary description is clearer.
3. Draft uses summary voice instead of action/dialogue.
4. Main scene has no convergence point.
5. Key object has no world function.
6. Protagonist only suffers and gains no usable leverage.
7. Chapter ends on abstract realization instead of concrete consequence.
8. Next chapter would rely on chat memory instead of wiki state.
