#!/usr/bin/env python3
"""
Name Gate generator for novelwiki.

Purpose:
- Generate grounded Chinese legal-name candidates.
- Add work IDs / handles / nicknames when the setting needs them.
- Reject high-risk AI-default names and names already used in the repository.
- Produce a Name Gate report that can be pasted into wiki/name_registry.md.

Optional dependency:
- faker. If installed, Faker('zh_CN') can be used as an additional name source.

Usage examples:

python tools/name_gate.py \
  --novel-id cyberpunk_offline_city \
  --genre cyberpunk \
  --social-layer lower_city_worker \
  --occupation implant_recycling_worker \
  --count 40

python tools/name_gate.py \
  --novel-id test_xianxia_luchen \
  --genre xianxia \
  --social-layer rural_apprentice \
  --occupation medicine_apprentice \
  --count 30
"""

from __future__ import annotations

import argparse
import random
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Set, Tuple


AI_DEFAULT_RISK_NAMES: Set[str] = {
    "沈砚",
    "陆沉",
    "顾言",
    "林澈",
    "江辰",
    "谢沉",
    "秦川",
    "裴行",
    "许知",
    "宋临",
    "周砚",
    "陈述",
    "苏晚",
    "云棠",
    "白芷",
    "阮清",
    "夏禾",
    "许栀",
}

# Common surnames, intentionally ordinary. Avoid surnames that make every name feel like a protagonist template.
SURNAMES: Sequence[str] = (
    "王", "李", "张", "刘", "陈", "杨", "赵", "黄", "周", "吴",
    "徐", "孙", "马", "朱", "胡", "郭", "何", "高", "林", "罗",
    "郑", "梁", "谢", "宋", "唐", "许", "韩", "冯", "邓", "曹",
    "彭", "曾", "萧", "田", "董", "潘", "袁", "于", "蒋", "蔡",
    "余", "杜", "叶", "程", "苏", "魏", "吕", "丁", "任", "沈",
    "姚", "卢", "姜", "崔", "钟", "谭", "陆", "汪", "范", "金",
    "石", "廖", "贾", "夏", "韦", "傅", "方", "白", "邹", "孟",
    "熊", "秦", "邱", "江", "尹", "薛", "闫", "段", "雷", "侯",
    "龙", "史", "陶", "黎", "贺", "顾", "毛", "郝", "龚", "邢",
    "佟", "樊", "童", "翟", "蓝", "路", "梅", "申", "管", "纪",
)

# Workaday given-name characters. These are deliberately plainer than typical AI literary names.
PLAIN_GIVEN_CHARS: Sequence[str] = (
    "平", "安", "立", "成", "民", "建", "军", "强", "刚", "勇",
    "明", "亮", "华", "国", "生", "志", "良", "富", "根", "福",
    "顺", "贵", "宽", "正", "来", "发", "义", "全", "兴", "旺",
    "海", "山", "川", "林", "田", "河", "东", "南", "西", "北",
    "小", "大", "二", "三", "久", "准", "检", "栓", "泊", "束",
    "旧", "岭", "轨", "钧", "载", "衡", "拴", "钉", "桥", "岸",
)

# Extra character pools by genre/social layer. Use sparingly; names should remain plausible.
CYBERPUNK_WORKER_CHARS: Sequence[str] = (
    "准", "检", "栓", "泊", "旧", "轨", "桥", "岸", "衡", "载",
    "钳", "闸", "线", "号", "匣", "站", "区", "零", "九", "七",
)

XIANXIA_RURAL_CHARS: Sequence[str] = (
    "禾", "田", "山", "石", "川", "青", "木", "根", "生", "平",
    "安", "成", "良", "守", "泊", "岑", "岭", "药", "秋", "河",
)

# Characters that often push a name toward overly polished literary-protagonist style.
POLISHED_RISK_CHARS: Set[str] = set("砚澈言知棠芷栀辞珩璟宸玦弈晏清沉")


@dataclass(frozen=True)
class Candidate:
    legal_name: str
    work_id: Optional[str]
    nickname: Optional[str]
    risk: str
    reasons: Tuple[str, ...]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def collect_used_names(root: Path) -> Set[str]:
    names: Set[str] = set()
    for path in root.glob("novels/**/wiki/**/*.md"):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        # Conservative extraction: 2-4 Chinese chars after common labels.
        for pattern in [
            r"Name[:：]\s*([\u4e00-\u9fff]{2,4})",
            r"名字[:：]\s*([\u4e00-\u9fff]{2,4})",
            r"Name\s*`?([\u4e00-\u9fff]{2,4})`?",
            r"^-\s*([\u4e00-\u9fff]{2,4})\s*[—-]",
        ]:
            for match in re.finditer(pattern, text, flags=re.MULTILINE):
                names.add(match.group(1))
    return names


def faker_names(count: int) -> List[str]:
    try:
        from faker import Faker  # type: ignore
    except Exception:
        return []

    fake = Faker("zh_CN")
    result: List[str] = []
    for _ in range(count):
        name = fake.name()
        # remove whitespace and rare separators
        name = re.sub(r"\s+", "", name)
        if re.fullmatch(r"[\u4e00-\u9fff]{2,4}", name):
            result.append(name)
    return result


def given_pool(genre: str, social_layer: str, occupation: str) -> Sequence[str]:
    key = f"{genre} {social_layer} {occupation}".lower()
    if "cyber" in key or "worker" in key or "recycling" in key:
        return tuple(dict.fromkeys((*PLAIN_GIVEN_CHARS, *CYBERPUNK_WORKER_CHARS)))
    if "xianxia" in key or "rural" in key or "medicine" in key:
        return tuple(dict.fromkeys((*PLAIN_GIVEN_CHARS, *XIANXIA_RURAL_CHARS)))
    return PLAIN_GIVEN_CHARS


def make_legal_names(count: int, genre: str, social_layer: str, occupation: str, seed: int) -> List[str]:
    rng = random.Random(seed)
    pool = given_pool(genre, social_layer, occupation)
    names: List[str] = []

    # Mix optional Faker names with rule-generated names.
    names.extend(faker_names(max(10, count // 3)))

    while len(names) < count * 4:
        surname = rng.choice(SURNAMES)
        given_len = 1 if rng.random() < 0.45 else 2
        if given_len == 1:
            given = rng.choice(pool)
        else:
            a = rng.choice(pool)
            b = rng.choice(pool)
            # Avoid duplicated char names unless intentionally numeric/common.
            if a == b and a not in {"二", "三", "九", "七"}:
                continue
            given = a + b
        names.append(surname + given)
    return names


def make_work_id(index: int, genre: str, social_layer: str, occupation: str) -> Optional[str]:
    key = f"{genre} {social_layer} {occupation}".lower()
    if "cyber" not in key and "worker" not in key and "recycling" not in key:
        return None
    prefix = "R" if "recycling" in key else "W"
    return f"{prefix}-{index:03d}"


def make_nickname(name: str, work_id: Optional[str]) -> Optional[str]:
    if work_id:
        number = work_id.split("-")[-1]
        if number.startswith("0"):
            number = number.lstrip("0") or "零"
        return number
    if len(name) >= 2:
        return name[-1] + "子" if name[-1] not in "平安立" else name[-1]
    return None


def evaluate_name(name: str, used: Set[str]) -> Tuple[str, Tuple[str, ...]]:
    reasons: List[str] = []
    risk = "low"

    if name in used:
        risk = "high"
        reasons.append("already used in repository")

    if name in AI_DEFAULT_RISK_NAMES:
        risk = "high"
        reasons.append("listed as AI-default risk name")

    if any(ch in POLISHED_RISK_CHARS for ch in name[1:]):
        if risk != "high":
            risk = "medium"
        reasons.append("contains polished literary-risk character")

    if len(name) > 3:
        if risk == "low":
            risk = "medium"
        reasons.append("longer legal name; verify it fits naming context")

    if re.search(r"[零一二三四五六七八九十]$", name):
        if risk == "low":
            risk = "medium"
        reasons.append("number-like legal name; may work better as nickname/work ID")

    if not reasons:
        reasons.append("ordinary legal-name shape")

    return risk, tuple(reasons)


def generate_candidates(
    novel_id: str,
    genre: str,
    social_layer: str,
    occupation: str,
    count: int,
    seed: int,
) -> List[Candidate]:
    root = repo_root()
    used = collect_used_names(root)
    raw_names = make_legal_names(count=count, genre=genre, social_layer=social_layer, occupation=occupation, seed=seed)

    seen: Set[str] = set()
    candidates: List[Candidate] = []
    index = 1
    for name in raw_names:
        if name in seen:
            continue
        seen.add(name)
        risk, reasons = evaluate_name(name, used)
        work_id = make_work_id(index, genre, social_layer, occupation)
        nickname = make_nickname(name, work_id)
        candidates.append(Candidate(name, work_id, nickname, risk, reasons))
        index += 1
        if len(candidates) >= count:
            break
    return candidates


def render_report(args: argparse.Namespace, candidates: Sequence[Candidate]) -> str:
    accepted = [c for c in candidates if c.risk == "low"]
    review = [c for c in candidates if c.risk == "medium"]
    rejected = [c for c in candidates if c.risk == "high"]

    lines: List[str] = []
    lines.append("# Name Gate Report")
    lines.append("")
    lines.append(f"Novel ID: `{args.novel_id}`")
    lines.append(f"Genre: `{args.genre}`")
    lines.append(f"Social layer: `{args.social_layer}`")
    lines.append(f"Occupation: `{args.occupation}`")
    lines.append(f"Count requested: {args.count}")
    lines.append("")
    lines.append("## Accepted Candidates")
    lines.append("")
    for c in accepted:
        lines.append(f"- {c.legal_name}" + (f" / {c.work_id} / {c.nickname}" if c.work_id else ""))
    lines.append("")
    lines.append("## Review Candidates")
    lines.append("")
    for c in review:
        lines.append(f"- {c.legal_name}" + (f" / {c.work_id} / {c.nickname}" if c.work_id else "") + f" — {'; '.join(c.reasons)}")
    lines.append("")
    lines.append("## Rejected Candidates")
    lines.append("")
    for c in rejected:
        lines.append(f"- {c.legal_name}" + (f" / {c.work_id} / {c.nickname}" if c.work_id else "") + f" — {'; '.join(c.reasons)}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"Accepted: {len(accepted)}")
    lines.append(f"Review: {len(review)}")
    lines.append(f"Rejected: {len(rejected)}")
    lines.append("")
    lines.append("Decision: ALLOW if at least one accepted candidate fits the character function; otherwise REVISE.")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate and screen character names for novelwiki.")
    parser.add_argument("--novel-id", required=True)
    parser.add_argument("--genre", required=True)
    parser.add_argument("--social-layer", required=True)
    parser.add_argument("--occupation", required=True)
    parser.add_argument("--count", type=int, default=40)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    candidates = generate_candidates(
        novel_id=args.novel_id,
        genre=args.genre,
        social_layer=args.social_layer,
        occupation=args.occupation,
        count=args.count,
        seed=args.seed,
    )
    print(render_report(args, candidates))


if __name__ == "__main__":
    main()
