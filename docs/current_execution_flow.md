# Current Execution Flow

This is the short operational checklist for the current novel-generation workflow.

Use `docs/workflow_layers.md` as the authoritative full version and `docs/file_roles.md` as the file responsibility index.

## Non-Negotiable Order

### Standard Long-Form Flow

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

### Macro Modern-To-Cosmic Flow

Use this for stories where a modern Chinese protagonist enters a cosmic / multiverse / high-civilization arena.

```text
Cosmic Civilization Arena
-> Earth Civilization Value
-> Unified Power Logic
-> Modern Chinese Entry Bridge
-> Irreversible Trend Anchor
-> Webnovel Pleasure Ladder
-> Name & Term Gate
-> Wiki Bootstrap
-> Actor Setup
-> Modern-To-Cosmic Opening / Chapter Trend + Pleasure Convergence
-> Scene Design
-> Drafting
-> Review
-> Wiki Sync
```

Do not skip forward.

## 1. Cosmic Civilization Arena

Required for macro modern-to-cosmic stories:

```text
prompts/00_cosmic_civilization_arena.md
```

Defines:

- universe / multiverse stage;
- civilization routes;
- major factions;
- resource logic;
- Earth position;
- cosmic irreversible trend;
- chapter-one visibility budget.

Hard rule for macro stories:

```text
No cosmic civilization arena, no macro story setup.
```

## 2. Earth Civilization Value

Required for Earth-entry cosmic stories:

```text
prompts/00_earth_civilization_value.md
```

Defines:

- why Earth is weak;
- why Earth is not meaningless;
- why high civilizations observe, exploit, protect, or contest Earth;
- how the protagonist can make Earth be reevaluated.

Hard rule:

```text
Earth cannot be only nostalgia or hometown.
```

## 3. Unified Power Logic

Required when cultivation, magic, technology, psychic power, biology, or higher-dimensional law coexist:

```text
prompts/00_unified_power_logic.md
```

Defines the shared substrate underneath different systems:

```text
energy -> storage -> conversion -> control interface -> law/rule access -> civilization scale
```

Hard rule:

```text
Power systems cannot be decorative labels.
```

## 4. Modern Chinese Entry Bridge

Required when the protagonist comes from modern China / modern Earth:

```text
prompts/00_modern_chinese_entry_bridge.md
```

Defines:

- modern identity;
- reader-laoxiang feeling;
- modern knowledge structure;
- first contact mode;
- modern thinking as pleasure;
- Earth emotional anchor.

Hard rule:

```text
Modern identity must remain active after chapter one.
```

## 5. Irreversible Trend Anchor

Required file:

```text
prompts/00_irreversible_trend_anchor.md
```

Run once during new-novel setup, before chapter planning.

For macro stories, this must include:

- cosmic civilization irreversible trend;
- Earth irreversible civilization pressure;
- protagonist irreversible final form.

Hard rule:

```text
No irreversible trend anchor, no chapter design.
```

The author controls the world / civilization trend and protagonist final form. Characters control local choices. Plot emerges when local choices are pulled back into the irreversible trend.

## 6. Webnovel Pleasure Ladder

Required for commercial webnovel drafting:

```text
prompts/00_webnovel_pleasure_ladder.md
```

Defines:

- repeated surface pleasure;
- first low-position label;
- face-slapping targets;
- resource ladder;
- qualification ladder;
- chapter pleasure plan.

Hard rule:

```text
No visible reader pleasure, no important chapter.
```

Depth does not replace pleasure. Every important chapter needs a visible reward such as face-slapping, hidden value, resource gain, status shift, tactical win, qualification, recognition, or public correction.

## 7. Name & Term Gate

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

## 8. Wiki Bootstrap

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

For macro modern-to-cosmic stories, the project wiki must also include or reference:

- cosmic civilization arena;
- Earth civilization value;
- unified power logic;
- modern Chinese entry bridge;
- webnovel pleasure ladder;
- world / civilization irreversible trend;
- protagonist irreversible final form;
- current stage map;
- approved names and terms.

Create character / world / organization files as needed before those actors or places enter chapter planning.

Hard rule:

```text
No wiki bootstrap, no draft.
```

## 9. Actor Setup

Required for recurring major actors and organizations.

Files:

```text
prompts/00_character_behavior_model.md
prompts/00_character_expression_card.md
prompts/00_organization_behavior_model.md
```

Temporary characters may remain role labels.

If a temporary character repeatedly changes the plot, creates debt, becomes a relationship pressure, or appears across chapters, run Name & Term Gate and create a character file.

## 10. Opening / Chapter Trend + Pleasure Convergence

Required files for important chapters:

```text
prompts/00_reality_causal_preflight.md
prompts/02_emergent_chapter_design.md
prompts/02_advantage_reward_ledger.md
```

For modern-to-cosmic chapter one, also use:

```text
prompts/01_modern_to_cosmic_opening.md
```

A chapter must not begin from a random event.

It must begin from:

- current stage of world / civilization irreversible trend;
- current stage of protagonist final form;
- local choices available to the protagonist;
- visible reader pleasure;
- how different choices are pulled toward the same trend node.

Hard rule:

```text
No trend convergence, no pleasure convergence, no chapter draft.
```

Do not create an event just to trigger a goldfinger, reveal a clue, or show a workflow.

## 11. Scene Design

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
- concrete result;
- reader pleasure movement when this is a major scene.

The scene should not begin from a preselected event. It should begin from actor goals under trend pressure.

## 12. Drafting

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

## 13. Review

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

## 14. Wiki Sync

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
- world / civilization trend progress;
- Earth status progress when relevant;
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

1. Macro story lacks cosmic civilization arena.
2. Earth is only a hometown and has no civilization value.
3. Multiple power systems lack unified power logic.
4. Modern protagonist loses modern identity after entry.
5. Irreversible trend anchor is missing.
6. New name or term appears without Name & Term Gate.
7. Chapter begins from a random event instead of trend convergence.
8. Important chapter has no visible reader pleasure.
9. Local choices do not pull toward a shared trend node.
10. Prose uses invented shorthand where ordinary description is clearer.
11. Draft uses summary voice instead of action/dialogue.
12. Main scene has no convergence point.
13. Key object has no world function.
14. Protagonist only suffers and gains no usable final-form asset.
15. Chapter does not advance world trend, Earth status, or protagonist final form.
16. Chapter ends on abstract realization instead of concrete consequence.
17. Next chapter would rely on chat memory instead of wiki state.
