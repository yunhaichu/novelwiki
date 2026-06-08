# Failure 001: Low-Anchor Terminology

## Symptom

The prose uses compact, pseudo-genre, pseudo-archaic, or unexplained phrases that feel like worldbuilding but do not give the reader enough grounding.

## Why It Happens

LLMs often compress an implied rule, status, or sensory quantity into a short label because such labels are probable in genre prose.

The phrase may not be a formal term, so it can bypass a glossary check.

## Bad Pattern

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

## Detection Rule

Mark REVISE if a phrase:

- requires the reader to infer an unstated rule
- sounds genre-appropriate but is not natural speech
- compresses location, status, quantity, or institution without explanation
- carries key meaning but is absent from the glossary

## Repair Strategy

Replace with plain language.

Examples:

```text
多坐了几口气 -> 昨天是不是比前几天多坐了一会儿
旧人 -> 已经在这里待过一个月的人
有痕 -> 木牌背后刻过一道
下泉 -> 山腰水井 / 去山腰水井挑水
灶后 -> 厨房后面 / 厨房后墙外
账数 -> 粮铺账本上的数字
册上有人 -> 赵管事在你名字后面写了记号
```

## Regression Test

Given a chapter draft, scan for low-anchor terms and require plain replacements.

## Related Governance Files

- `governance/low_anchor_phrase_check.md`
- `governance/style_banlist.md`
- `governance/chapter_brief_review.md`
- `prompts/04_review_hook.md`
