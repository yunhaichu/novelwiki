# Workflow Layers

This is the authoritative full execution-order index for the novel workflow.

Use `docs/current_execution_flow.md` only as a short path-selection card. Use `docs/file_roles.md` for file responsibilities.

The workflow has two valid setup paths:

- standard long-form setup;
- macro modern-to-cosmic setup.

Do not run every file for every chapter. Select layers according to project type and chapter importance.

## Layer 0: Safety Snapshot

Run before reorganizing prompts, deleting files, merging files, or changing workflow responsibilities.

Files:

- `docs/backups/workflow_snapshot_2026-06-09.md`

## Layer 1A: Macro Modern-To-Cosmic Setup

Run once before normal new-novel setup when the target story involves modern Earth, cosmic civilizations, multiverse scale, cultivation + technology + magic, or civilization war.

Required files:

1. `prompts/00_cosmic_civilization_arena.md`
2. `prompts/00_earth_civilization_value.md`
3. `prompts/00_unified_power_logic.md`
4. `prompts/00_modern_chinese_entry_bridge.md`
5. `prompts/00_webnovel_pleasure_ladder.md` as Reader Hook / Payoff Ladder

Required order:

```text
cosmic civilization arena
-> Earth civilization value
-> unified power logic
-> modern Chinese entry bridge
-> reader hook / payoff ladder
```

Hard rules:

```text
No cosmic civilization arena, no macro story.
No Earth value, no Earth protection story.
No unified power logic, no multi-system power story.
No modern entry bridge, no modern-reader self-insertion.
No hook/payoff ladder, no commercial webnovel execution.
```

## Layer 1B: New Novel Setup

Run once per formal novel project before chapter planning.

Required files:

1. `prompts/00_novel_spine.md`
2. `prompts/00_genre_mode_contract.md`
3. `prompts/00_genre_operating_model.md`
4. `prompts/00_irreversible_trend_anchor.md`
5. `prompts/00_reality_causal_preflight.md` for first major premise / opening event family
6. `prompts/00_base_settings_builder.md`
7. `prompts/00_major_conflict_engine.md`
8. `prompts/00_dramatic_arena.md`
9. `prompts/00_protagonist_growth_track.md`
10. `prompts/00_project_viability_gate.md`
11. `prompts/00_name_term_gate.md`
12. `prompts/00_wiki_bootstrap.md`

For macro modern-to-cosmic stories, Layer 1B must read Layer 1A outputs.

Macro boundary rule:

```text
Layer 1B must not shrink the arena created by Layer 1A.
```

For macro stories, base settings, major conflict, dramatic arena, protagonist growth, and project viability must derive from:

- cosmic civilization arena;
- Earth civilization value;
- unified power logic;
- modern Chinese entry bridge;
- reader hook / payoff ladder.

Do not let standard setup collapse a cosmic story back into a small sect, city, island, or single-country conflict unless the story intentionally starts local while preserving the larger arena.

Required order inside Layer 1B:

```text
premise / type promise
-> genre mode
-> genre operating model
-> irreversible trend anchor
-> base setting boundaries
-> major conflict / dramatic arena
-> protagonist growth track
-> Project Viability Gate
-> Name & Term Gate
-> wiki bootstrap
```

Project Viability Gate is the final stop before formal wiki bootstrap.

Hard rule:

```text
No Project Viability Gate pass, no formal wiki bootstrap.
```

Supporting reference files:

- `reference_settings/usage_contract.md`
- `reference_settings/index.json`
- selected `reference_settings/genre_common/` files
- selected `reference_settings/power_system_common/` files only if the novel contains powers, anomalies, goldfingers, cultivation, magic, psychic systems, or similar mechanisms.

Required wiki outputs:

- `novels/<novel_id>/wiki/project.md`
- `novels/<novel_id>/wiki/base_settings.md`
- `novels/<novel_id>/wiki/style.md`
- `novels/<novel_id>/wiki/name_registry.md`
- `novels/<novel_id>/wiki/protagonist_growth.md`
- `novels/<novel_id>/wiki/timeline.md`
- `novels/<novel_id>/wiki/relationships.md`
- `novels/<novel_id>/wiki/foreshadowing.md`
- initial character / organization / world files as needed

Hard rules:

```text
No irreversible trend anchor, no chapter design.
No Project Viability Gate pass, no formal wiki bootstrap.
No Name & Term Gate, no project file.
No wiki bootstrap, no formal draft.
```

## Layer 1T: Fast Trial Mode

Use before committing to a full novel wiki when testing whether a concept has reader desire.

Fast Trial output is non-canon.

Allowed outputs:

- non-canon opening sketch;
- non-canon chapter-one outline;
- non-canon desire test draft.

Forbidden outputs:

- approved chapter draft;
- chapter state;
- chapter two plan;
- canon wiki update.

Formal drafting still requires Layer 1B, Project Viability Gate pass, and Wiki Bootstrap.

For macro modern-to-cosmic trial:

```text
Layer 1A core files
-> Layer 5 modern-to-cosmic opening
-> non-canon sketch / outline / desire test
-> decide whether to build full wiki
```

## Layer 2: Actor Model And Cognition Setup

Run once for major recurring actors. Update only when canon changes.

Required for major recurring characters and organizations:

- `prompts/00_character_behavior_model.md`
- `prompts/00_character_expression_card.md`
- `prompts/00_organization_behavior_model.md`

Required when an actor influences chapter logic, limited knowledge, or multi-party conflict:

- `prompts/00_actor_cognition_card.md`

Governance rule for simulations and multi-actor scenes:

- `governance/agent_state_rules.md`

Guidance:

- Major forces need organization behavior models.
- Important recurring characters need behavior models and expression cards.
- Any actor who drives important choices needs cognition boundaries.
- Temporary characters may remain role labels, but their role, knowledge, goal, and scene function must be clear.
- Macro stories need models for high-civilization observers, evaluators, academy factions, military factions, and Earth-side stakeholders once recurring.

Hard rule:

```text
No omniscient actors.
Characters act from what they know, want, fear, misunderstand, can physically do, and can socially afford.
```

## Layer 3: Volume / Arc Planning

Run once per volume, arc, or large stage.

Files:

- `prompts/00_volume_state_plan.md`
- `prompts/00_chapter_pressure_card.md` when chapter pressure needs isolation
- `prompts/00_webnovel_pleasure_ladder.md` as Reader Hook / Payoff Ladder when a new volume starts or the story loses continuation desire

Outputs:

- current world / civilization trend stage;
- active protagonist final-form stage;
- current Earth evaluation / protection / exploitation status when relevant;
- volume attractor;
- organization pressure map;
- reader continuation promise;
- hook / payoff ladder;
- constraints on what must not escalate yet.

## Layer 4: Chapter Trend + Hook/Payoff Convergence

Run before designing any important chapter.

Required files:

1. `prompts/00_irreversible_trend_anchor.md`
2. `prompts/00_reality_causal_preflight.md`
3. `prompts/02_emergent_chapter_design.md`
4. (deprecated - function merged into `prompts/05_wiki_sync_after_chapter.md`)
5. `prompts/00_webnovel_pleasure_ladder.md` as Reader Hook / Payoff Ladder when the chapter is important or the previous draft feels flat.

For chapter one of modern-to-cosmic stories, also use:

- `prompts/01_modern_to_cosmic_opening.md`

Outputs:

- current trend pressure;
- current protagonist final-form pressure;
- primary reader hook type;
- specific question / crisis / choice / relationship tension / world reveal / mechanism reveal / earned visible gain;
- small payoff delivered;
- new question or pressure opened;
- whether face-slapping is necessary, and why;
- local choices available to the protagonist;
- how different choices pull toward the same trend node;
- event feasibility;
- actor knowledge limits;
- cost and usable leverage;
- result attractor.

Hard rules:

```text
No trend convergence, no formal chapter draft.
No hook/payoff, no important chapter.
Face-slapping is optional and must be situationally justified.
```

## Layer 5: Reader Entry / Opening Control

Run for first chapters, new arcs, new worlds, new power systems, or complex settings.

Primary file for modern-to-cosmic chapter one:

- `prompts/01_modern_to_cosmic_opening.md`

Optional review aids when present:

- `prompts/00_reader_entry_gate.md`
- `prompts/02_opening_chapter_brief.md`
- `governance/reader_entry_review.md`
- `governance/opening_chapter_brief_review.md`

If optional review files are absent, do not block execution.

Opening checks:

- protagonist is clear;
- immediate pressure is clear;
- reader knows what can be lost now;
- unfamiliar terms are limited;
- function appears before formal name;
- the chapter has a concrete continuation hook;
- chapter one reveals only a small crack of the macro world;
- first-contact psychology is believable when relevant.

## Layer 6: Scene Design

Run for each important scene. For simple transition scenes, this can be shortened.

Required files for major scenes:

1. `prompts/02_scene_convergence.md`
2. `prompts/02_scene_expression_state.md`
3. `prompts/02_dialogue_intent.md`
4. `prompts/00_multi_agent_scene_simulation.md` when the scene has more than two active actors or complex hidden motives.

Before multi-agent simulation, apply:

- `governance/agent_state_rules.md`

Outputs:

- scene trend pressure;
- reader hook/payoff movement in the scene;
- convergence point;
- actor local worlds;
- actor cognition boundaries;
- environmental modulation;
- organization packaging if relevant;
- collision map;
- performance beats;
- dialogue intent.

## Layer 7: Drafting

Run after chapter and scene planning.

Files:

- `prompts/01_writer.md`
- `prompts/01_scene_log_to_draft.md` if a scene simulation/action log exists.

Rules:

- Do not let interfaces write the story.
- Do not let narrator explanation replace character performance.
- Apply genre mode before universal workflow rules.
- Use current novel wiki as canon.
- Do not import reference settings directly into prose.
- Do not introduce unapproved names or terms; use ordinary description until the Name & Term Gate approves them.
- Do not start from a random event.
- Do not replace hook/payoff with exposition.
- For modern-to-cosmic stories, keep the modern Chinese viewpoint active.
- First-contact scenes must preserve psychological realism.

## Layer 8: Review / Revision

Run after draft.

Do not run every review on every chapter. Select reviews by route.

### Review Routing Matrix

#### Low-Stakes Transition

Use when the chapter mainly moves characters, resets location, breathes between conflicts, or prepares the next pressure.

Run:

- light self-check against current chapter state;
- `governance/anti_ai_expression_review.md` if prose feels generic;
- `governance/wiki_write_rules.md` before sync.

Required checks:

- no canon contradiction;
- no unapproved names or terms;
- at least one small hook/payoff or state movement;
- no summary-only prose;
- next chapter constraint remains clear.

#### Important Chapter

Use when the chapter changes protagonist state, resolves or creates major pressure, introduces a key actor/object, or moves the irreversible trend.

Run:

- `governance/emergent_plot_review.md`;
- `governance/protagonist_growth_review.md`;
- `governance/anti_ai_expression_review.md`;
- `governance/wiki_write_rules.md` before sync.

Add `governance/review_checklist.md` only if a general final pass is needed.

#### System / Record Heavy Chapter

Use when records, reports, logs, workflows, screens, archives, system prompts, or database statuses appear.

Run:

- `governance/anti_record_driven_plot.md`;
- `governance/reality_logic_review.md` if process / authority / institution logic matters;
- `governance/anti_ai_expression_review.md`.

#### Object-Centered Chapter

Use when a physical object, resource, artifact, document, weapon, medicine, body trace, token, or clue drives the chapter.

Run:

- `governance/object_function_review.md`;
- `governance/reality_logic_review.md` if object use depends on process, cost, timing, or authority.

#### Voice / Relationship Heavy Chapter

Use when the chapter depends on dialogue, emotional tension, negotiation, trust, suspicion, authority, or first contact.

Run:

- `governance/character_voice_review.md`;
- `governance/anti_ai_expression_review.md`.

For first-contact or high-pressure scenes, also check:

- psychological realism;
- no calm abstract AI-like speech under fear;
- actor cognition limits.

#### Setup / Canon Change Chapter

Use when base settings, durable world rules, protagonist growth stage, organization behavior, or wiki structure may change.

Run:

- `governance/base_settings_review.md` when durable settings are touched;
- `governance/wiki_retrieval_rules.md` before drafting;
- `governance/wiki_write_rules.md` before sync.

### Macro Modern-To-Cosmic Extra Checks

For macro modern-to-cosmic stories, always check:

- Earth value remains active;
- modern viewpoint remains active;
- macro world is hinted, not dumped;
- reader hook/payoff is concrete;
- protagonist gain helps personal growth, Earth status, or cross-system capability;
- first-contact or high-pressure dialogue does not sound like calm abstract analysis.

## Layer 9: Wiki Sync / Canon Update

Run immediately after the chapter is approved and before planning the next chapter.

Primary sync file:

- `prompts/05_wiki_sync_after_chapter.md`

Governance:

- `governance/wiki_write_rules.md`


Deprecated old prompt:

- `prompts/06_chapter_state_update.md` is deprecated. Do not use it for current workflow.

Always create or update:

- `novels/<novel_id>/wiki/chapter_states/chapter_<number>.md`

Chapter state must track:

- world / civilization trend progress;
- Earth status progress when relevant;
- protagonist final-form progress;
- reader hook / payoff delivered;
- reader reward delivered;
- reader debt;
- pressure clock;
- repetition risk;
- next chapter constraints.

Hard rule:

```text
Approved formal chapter -> wiki sync -> next chapter.
```

## Required Execution Order

For a macro modern-to-cosmic new novel:

```text
Layer 1A -> Layer 1B including Project Viability Gate -> Layer 2 -> Layer 3 -> Layer 4 -> Layer 5 -> Layer 6 -> Layer 7 -> Layer 8 -> Layer 9
```

For a standard new novel:

```text
Layer 1B including Project Viability Gate -> Layer 2 -> Layer 3 -> Layer 4 -> Layer 5 -> Layer 6 -> Layer 7 -> Layer 8 -> Layer 9
```

For a macro modern-to-cosmic fast trial:

```text
Layer 1A core files -> Layer 5 modern-to-cosmic opening -> non-canon sketch / outline / desire test -> decide whether to build full wiki
```

For a normal later chapter:

```text
Read wiki -> Layer 3 check -> Layer 4 trend + hook/payoff convergence -> Layer 6 -> Layer 7 -> Layer 8 by route -> Layer 9
```

For a simple low-stakes transition chapter:

```text
Read wiki -> Layer 3 check -> Layer 4 light trend + hook/payoff check -> Layer 7 -> Layer 8 low-stakes route -> Layer 9
```

## Existing Legacy Chapter States

Older test novels may contain chapter state files that predate the current template.

They should not block new workflow tests unless the user explicitly resumes that novel.

If resuming an old approved novel, migrate its latest chapter state to the current template before planning the next chapter.

## Non-Negotiable Gates

Do not formal draft if any of these are unresolved:

1. Fast Trial is being mistaken for canon draft.
2. Macro story lacks cosmic civilization arena.
3. Earth-entry story lacks Earth civilization value.
4. Multi-system story lacks unified power logic.
5. Modern-entry story lacks modern Chinese entry bridge.
6. Genre mode is unclear.
7. Genre operating model is missing or too vague.
8. Irreversible trend anchor is missing or weak.
9. Reader Hook / Payoff Ladder is missing for commercial long-form execution.
10. Project Viability Gate has not passed.
11. Name & Term Gate is missing or failed.
12. Initial wiki bootstrap is missing.
13. Base settings for the active novel are missing.
14. Reality-causal preflight says the core event is unnatural.
15. Chapter trend convergence is missing.
16. Important chapter has no concrete reader hook/payoff.
17. Actor cognition boundary is missing for an important actor who drives chapter logic.
18. The protagonist has no active growth stage toward final form.
19. The chapter has no usable protagonist gain when gain is required.
20. The main scene has no convergence point.
21. The key object has no natural function.
22. Unapproved invented terms appear where ordinary description would be clearer.
23. The story relies on system/report/log/status change as climax.

Do not plan the next formal chapter if any of these are unresolved:

1. Approved chapter has no current-format chapter state file.
2. World / civilization trend progress was not recorded.
3. Earth status progress was not recorded when relevant.
4. Protagonist final-form progress was not recorded.
5. Reader hook/payoff delivered was not recorded for an important chapter.
6. Reader reward delivered was not recorded when relevant.
7. New confirmed character / organization / world facts were not synchronized.
8. Newly approved or rejected terms were not synchronized into the name registry.
9. Next chapter constraints are missing.
10. The next chapter would need to rely on chat memory instead of wiki state.
