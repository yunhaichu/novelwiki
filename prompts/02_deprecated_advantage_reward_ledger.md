# Protagonist Advantage Ledger (Reader Reward Not Included)
# [DEPRECATED - Function merged into prompts/05_wiki_sync_after_chapter.md]

Use of this file is deprecated.

Its purpose has been merged into `prompts/05_wiki_sync_after_chapter.md` (Wiki Sync After Chapter).
The wiki_sync prompt now includes a "Planned Advantages (from design phase)" section that captures what the chapter promises to deliver,
and a "Actual Advantages Gained (from approved draft)" section that records what was actually delivered.
This eliminates duplicate output between chapter design and wiki sync.

## Note on "Reward" vs "Advantage"

This file tracked **protagonist advantage only** (relationship, physical object, access, information, etc.).
It did **not** track reader reward or reader debt — those belong in the wiki_sync output.
The confusing dual title has been updated to prevent ambiguity.

## Migration Guide

For chapter planning / design:
    - Read the "Planned Advantages" section in `prompts/05_wiki_sync_after_chapter.md`.
    - The wiki_sync prompt will ask what advantages the chapter **promises** to deliver.

For chapter review / sync:
    - The wiki_sync prompt will ask what advantages the chapter **actually delivered** in the approved draft.

If you are using an older workflow version, copy the "Planned Advantages" fields from this file into your wiki_sync output.
The core fields are protagonist advantage categories only:
    - Relationship / Physical object / Witness / Access / Enemy misjudgment / Operational space / Information / Evidence / Identity / Skill / Final-form asset

## Old Template (preserved for reference)

Read the original template at git commit 2cfe5d803b18b298977b2afdc4819b390dd1f9eb:
    `git show 2cfe5d803b18b298977b2afdc4819b390dd1f9eb:prompts/02_advantage_reward_ledger.md (original filename before rename)`

Do not use this file for new chapters.
