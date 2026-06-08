# Failure 001: Low-Anchor Terms

## Failure ID

failure_001_low_anchor_terms

## Failure Name

Low-anchor terms and pseudo-worldbuilding shorthand.

## Where It Appears

Draft prose, dialogue, narration, glossary drift, chapter briefs.

## Symptom

The draft uses compact expressions that sound like genre language but are not grounded in ordinary speech or established canon.

Examples:

```text
多坐了几口气
旧人
有痕
下泉
灶后
账数
册上有人
在册上了
```

## Root Cause

The model compresses meaning into short genre-flavored phrases because they are statistically plausible. It treats these phrases as worldbuilding even when the reader has not been taught them.

## Why Readers Notice

Readers pause to decode the phrase instead of following the scene. The text feels like it is inventing terminology for convenience.

## Detection Signals

- phrase sounds old-fashioned but no character would naturally say it
- phrase compresses a rule that should be shown plainly
- phrase is not in glossary
- phrase appears as a label rather than action
- reader can ask "what does this mean?" and the sentence cannot answer

## Required Fix

Replace with plain language or define through immediate action.

Examples:

```text
多坐了几口气 -> 多坐了一会儿
旧人 -> 已经在这里待过一个月的人
有痕 -> 木牌背后刻过一道
下泉 -> 山腰水井
灶后 -> 厨房后面
账数 -> 粮铺账本上的数字
册上有人 -> 赵管事在册子上写了你的名字
```

## Regression Test

Before approving a draft, scan for compact invented labels. If more than one suspicious phrase appears, mark REVISE.

## Related Governance Files

- `governance/low_anchor_phrase_check.md`
- `governance/style_banlist.md`
- `governance/chapter_brief_review.md`
- `prompts/04_review_hook.md`
