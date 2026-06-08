# Scene Log To Draft Prompt

Use this prompt after `prompts/00_multi_agent_scene_simulation.md` has produced an action log and state update.

The purpose is to turn an emergent scene log into prose without changing the scene's core causality.

## Required Inputs

Read:

- scene simulation output
- current novel wiki files relevant to the scene
- style file
- name registry
- relevant character files
- relevant world/location/object files
- previous chapter state if any
- `governance/wiki_retrieval_rules.md`
- `governance/anti_ai_taste_check.md`

## Preserve

Preserve:

- active characters
- private knowledge boundaries
- order of important actions
- cause of each action
- key reactions
- state changes
- final pressure created by the scene

Do not add new plot facts to make the scene smoother.

## Convert To Prose

Convert the action log into a chapter or scene draft.

Focus on:

- physical action
- pressure
- concrete objects
- character-specific speech
- visible reactions
- misunderstanding
- partial information
- changed options

Avoid:

- explaining the theme
- making every motive explicit
- inserting polished summary lines
- adding new lore to explain weak actions
- making characters ask reader-facing questions
- turning the simulation into a mechanical report

## Causality Rule

If the action log has weak causality, do not hide it with prose.

Return:

```text
REVISE SIMULATION: [reason]
```

instead of drafting.

## Output

Output only the prose draft unless the user asks for notes.
