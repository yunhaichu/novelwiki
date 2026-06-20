# Workflow Layers

This is the authoritative full execution-order index for the novel workflow.

Use `docs/current_execution_flow.md` as the short path-selection card. Use `docs/interactive_writing_flow.md` for the approval protocol. Use `docs/file_roles.md` for file responsibilities.

The workflow has two valid setup paths:

- standard long-form setup;
- macro modern-to-cosmic setup.

The default execution mode is interactive. Do not run every file for every chapter. Do not draft a full formal chapter before the user approves the chapter intent and scene plan.

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
5. `prompts/00_webnovel_reader_hook_payoff_ladder.md` as Reader Hook / Payoff Ladder

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

For macro modern-to-cosmic stories, Layer 1B must read Layer 1A outputs and must not shrink the arena created by Layer 1A.

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
-> interactive trial approval
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

Hard rule:

```text
No omniscient actors.
Characters act from what they know, want, fear, misunderstand, can physically do, and can socially afford.
```

## Layer 3: Volume / Arc Planning

Run once per volume, arc, or large stage. For later chapters, read the current volume state and update only when the volume attractor, pressure map, or rhythm budget has changed.

Files:

- `prompts/00_volume_state_plan.md`
- `prompts/00_chapter_pressure_card.md` when chapter pressure needs isolation
- `prompts/00_webnovel_reader_hook_payoff_ladder.md` as Reader Hook / Payoff Ladder when a new volume starts or the story loses continuation desire

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
4. `prompts/00_webnovel_reader_hook_payoff_ladder.md` as Reader Hook / Payoff Ladder when the chapter is important or the previous draft feels flat.

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

Interactive rule:

After Layer 4, stop at Gate A and present the chapter intent. Do not design scenes or draft prose until the user approves or corrects the chapter intent.

Hard rules:

```text
No trend convergence, no formal chapter draft.
No hook/payoff, no important chapter.
No Gate A approval, no scene design.
Face-slapping is optional and must be situationally justified.
```

## Layer 5: Reader Entry / Opening Control

Run for first chapters, new arcs, new worlds, new power systems, or complex settings.

Primary file for modern-to-cosmic chapter one:

- `prompts/01_modern_to_cosmic_opening.md`

Optional review aids when present:

- `prompts/00_reader_entry_gate.md`
- `prompts/02_opening_chapter_brief.md`

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

Interactive rule:

After Layer 6, stop at Gate B and present the scene plan. Do not draft prose until the user approves or corrects the scene plan.

Hard rule:

```text
No Gate B approval, no prose for that scene.
```

## Layer 7: Drafting

Run only after approved chapter intent and approved scene plan.

Files:

- `prompts/01_writer.md`
- `prompts/01_scene_log_to_draft.md` if a scene simulation/action log exists.

Rules:

- Draft in approved units: scene, subscene, or bounded chapter segment.
- Do not continue into the next unit without user approval unless the user explicitly switches to batch mode.
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

After each draft unit, provide a local status card:

```text
- canon changes if approved
- unresolved reader debt
- next decision point
```

## Layer 8: Local Self-Check / Targeted Review

Layer 8 is no longer a mandatory heavy review after every draft.

Most review pressure should move earlier into Gate A and Gate B. After drafting, run only the minimum check needed for the approved unit.

### Always Run Light Self-Check

For every draft unit, check:

- no canon contradiction;
- no unapproved names or terms;
- no actor omniscience;
- no summary-only prose;
- no interface / record / report replacing story action;
- the unit preserves the approved hook/payoff or state movement;
- the next decision point is clear.

### Triggered Targeted Reviews

Run specialized reviews only when their trigger appears:

- `governance/anti_ai_expression_review.md` if prose feels generic, abstract, pretty, or summary-heavy.
- `governance/emergent_plot_review.md` if an important chapter's trend logic changed after drafting.
- `governance/protagonist_growth_review.md` if protagonist state, capability, qualification, or final-form progress changed.
- `governance/character_voice_review.md` if the unit depends on dialogue, trust, fear, authority, secrecy, or first contact.
- `governance/anti_record_driven_plot.md` if records, reports, logs, screens, prompts, archives, or system/status changes appear.
- `governance/object_function_review.md` if a physical object, resource, artifact, document, weapon, medicine, body trace, token, or clue drives the unit.
- `governance/reality_logic_review.md` if process, authority, institution logic, timing, survival cost, or jurisdiction matters.
- `governance/base_settings_review.md` if durable world rules or base settings may change.
- `governance/wiki_write_rules.md` before any canon sync.

### User Approval Boundary

A draft unit is not canon until the user approves it.

Do not synchronize, plan consequences, or build the next chapter from an unapproved draft unit.

## Layer 9: Wiki Sync / Canon Update

Run immediately after the user approves canon and before planning the next chapter or next canon-dependent unit.

Primary sync file:

- `prompts/05_wiki_sync_after_chapter.md`

Governance:

- `governance/wiki_write_rules.md`

Deprecated old prompt:

- `prompts/06_chapter_state_update.md` is deprecated. Do not use it for current workflow.

Always create or update after an approved formal chapter:

- `novels/<novel_id>/wiki/chapter_states/chapter_<number>.md`

For partial scene approvals, write only to the appropriate draft/session note unless the user explicitly approves a canon update.

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
User-approved canon -> wiki sync -> next canon-dependent planning step.
```

## Required Execution Order

For a macro modern-to-cosmic new novel:

```text
Layer 1A -> Layer 1B including Project Viability Gate -> Layer 2 -> Layer 3 -> Layer 4 -> Gate A -> Layer 5 -> Layer 6 -> Gate B -> Layer 7 unit drafting -> Layer 8 light / targeted -> user canon approval -> Layer 9
```

For a standard new novel:

```text
Layer 1B including Project Viability Gate -> Layer 2 -> Layer 3 -> Layer 4 -> Gate A -> Layer 5 when needed -> Layer 6 -> Gate B -> Layer 7 unit drafting -> Layer 8 light / targeted -> user canon approval -> Layer 9
```

For a macro modern-to-cosmic fast trial:

```text
Layer 1A core files -> Layer 5 modern-to-cosmic opening -> interactive trial approval -> non-canon sketch / outline / desire test -> decide whether to build full wiki
```

For a normal later chapter:

```text
Read wiki -> Layer 3 check -> Layer 4 trend + hook/payoff convergence -> Gate A -> Layer 6 scene design -> Gate B -> Layer 7 approved-unit drafting -> Layer 8 light / targeted -> user canon approval -> Layer 9
```

For a simple low-stakes transition chapter:

```text
Read wiki -> Layer 3 check -> Layer 4 light trend + hook/payoff check -> Gate A short confirmation -> Layer 7 approved-unit drafting -> Layer 8 light self-check -> user canon approval -> Layer 9
```

## Existing Legacy Chapter States

Older test novels may contain chapter state files that predate the current template.

They should not block new workflow tests unless the user explicitly resumes that novel.

If resuming an old approved novel, migrate its latest chapter state to the current template before planning the next formal chapter.

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
10. Name & Term Gate is missing or failed.
11. Initial wiki bootstrap is missing.
12. Base settings for the active novel are missing.
13. Reality-causal preflight says the core event is unnatural.
14. Chapter trend convergence is missing.
15. Gate A chapter intent has not been approved.
16. Important scene has no approved Gate B scene plan.
17. Actor cognition boundary is missing for an important actor who drives chapter logic.
18. The protagonist has no active growth stage toward final form.
19. The chapter has no usable protagonist gain when gain is required.
20. The main scene has no convergence point.
21. Unapproved invented terms appear where ordinary description would be clearer.
22. The story relies on system/report/log/status change as climax.
23. The user has not approved the current unit as canon.

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
10. The next chapter would need to rely on chat memory rather than wiki state.
11. The previous draft unit was not explicitly approved as canon.
