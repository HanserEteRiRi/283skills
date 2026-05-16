#!/usr/bin/env python3
"""
Build a character knowledge-boundary pack for a generated perspective skill.

The pack is intentionally separate from SKILL.md so future character distillation
can keep persona rules concise while still recording what the character can
remember, what they should refuse, and where plot memories live.

Usage:
    python scripts/build_character_knowledge_pack.py \
      --skill-dir 283/asakura-toru-perspective \
      --profile-config config/story-dialogue-profiles/asakura-toru.json \
      --boundary-config config/character-knowledge-boundaries/asakura-toru.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def read_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"JSON root must be an object: {path}")
    return data


def resolve_profile_path(profile_path: Path, value: object) -> Path | None:
    if not value:
        return None
    path = Path(str(value))
    if path.is_absolute():
        return path
    return (profile_path.parent / path).resolve()


def load_analysis(profile_path: Path, profile: dict[str, Any]) -> dict[str, Any] | None:
    output_dir = resolve_profile_path(profile_path, profile.get("output_dir"))
    target = str(profile.get("target", "")).strip()
    if not output_dir or not target:
        return None
    analysis_path = output_dir / f"{target}-dialogue-analysis.json"
    if not analysis_path.exists():
        return None
    return read_json(analysis_path)


def bullet_list(items: list[Any]) -> str:
    if not items:
        return "- 未配置"
    return "\n".join(f"- {item}" for item in items)


def relationship_table(relationships: list[dict[str, Any]]) -> str:
    if not relationships:
        return "| 对象 | 分数 | 说明 |\n|---|---:|---|\n| 未生成 | 0 | 未找到本地分析 |"
    lines = ["| 对象 | 分数 | 共现场景 | 说明 |", "|---|---:|---:|---|"]
    for item in relationships[:8]:
        partner = item.get("partner", "")
        score = item.get("score", 0)
        scenes = item.get("scene_cooccurrence", 0)
        lines.append(f"| {partner} | {score} | {scenes} | 语料高权重关系，剧情问题可作为记忆锚点 |")
    return "\n".join(lines)


def plot_memory(items: list[dict[str, Any]]) -> str:
    if not items:
        return "- 未配置。请在 boundary config 的 `plot_memory` 中补充。"
    lines = []
    for item in items:
        label = item.get("label", "未命名剧情")
        status = item.get("status", "已记录")
        note = item.get("note", "")
        sources = item.get("sources", [])
        source_text = ", ".join(str(s) for s in sources) if sources else "SKILL.md / references"
        lines.append(f"- **{label}**（{status}）：{note}  来源：{source_text}")
    return "\n".join(lines)


def render_markdown(
    skill_dir: Path,
    profile: dict[str, Any],
    boundary: dict[str, Any],
    analysis: dict[str, Any] | None,
) -> str:
    display_name = boundary.get("display_name") or profile.get("target") or skill_dir.name
    aliases = profile.get("aliases", [])
    summary = (analysis or {}).get("target_summary", {})
    metadata = (analysis or {}).get("metadata", {})
    relationships = (analysis or {}).get("relationships", [])

    lines = [
        f"# {display_name} 知识边界与剧情记忆",
        "",
        "本文件是角色 Skill 的知识范围门禁。它的优先级高于模型通用知识：角色回答时只能使用这里允许的知识、SKILL.md 身份与心智模型、`references/research/`、`references/local-dialogue-analysis/` 和用户当前提供的新信息。",
        "",
        "## 身份与认知范围",
        "",
        f"- 角色：{display_name}",
        f"- 其他名称：{', '.join(str(a) for a in aliases) if aliases else '未配置'}",
        f"- 年龄/阶段：{boundary.get('age_stage', '未配置')}",
        f"- 学历/职业身份：{boundary.get('education_or_role', '未配置')}",
        f"- 所属关系：{boundary.get('affiliation', '未配置')}",
        "",
        "## 可以回答的范围",
        "",
        bullet_list(boundary.get("allowed_scope", [])),
        "",
        "## 需要谨慎回答的范围",
        "",
        bullet_list(boundary.get("cautious_scope", [])),
        "",
        "## 必须拒答或承认不知道",
        "",
        bullet_list(boundary.get("refuse_scope", [])),
        "",
        "## 越界回答方式",
        "",
        f"- 中文：{boundary.get('refusal_cn', '这个我不太懂。')}",
        f"- 日本語：{boundary.get('refusal_jp', 'それは、よくわからない。')}",
        "- 不要先给专家答案再补一句“不确定”；角色不知道就先说不知道。",
        "- 用户明确说“退出角色/用普通助手回答”时，才可以切回普通助手能力。",
        "",
        "## 角色应记得的剧情",
        "",
        plot_memory(boundary.get("plot_memory", [])),
        "",
        "## 本地语料记忆索引",
        "",
        f"- 故事根目录：{metadata.get('story_root', '未生成')}",
        f"- 总 CSV 文件数：{metadata.get('total_files', '未生成')}",
        f"- 总对话行数：{metadata.get('total_rows', '未生成')}",
        f"- 目标台词行数：{summary.get('target_line_count', '未生成')}",
        f"- 目标出现场景数：{summary.get('target_scene_count', '未生成')}",
        f"- 他人提及目标行数：{summary.get('mentioned_by_others_count', '未生成')}",
        "",
        "## 高频关系记忆",
        "",
        relationship_table(relationships),
        "",
        "## 读取顺序",
        "",
        "1. 角色身份、语言和回答方式：先读 `SKILL.md`。",
        "2. 知识范围和拒答方式：读本文件。",
        "3. 剧情/人物关系问题：读 `references/research/06-timeline.md`、`references/research/07-local-dialogue-corpus.md` 和本地 `*-dialogue-report.md`。",
        "4. 官方事实：读 `references/sources/source-index.md` 中的一手来源；不把本地同人语料冒充官方 canon。",
        "",
        "## 生成时的硬规则",
        "",
        "- 角色可以记得自身经历、亲密关系、已记录剧情和与身份相符的日常知识。",
        "- 角色不能凭大模型预训练知识回答专业、现代、跨领域或剧情外问题。",
        "- 如果用户问“这个角色知道吗”，优先按年龄、学历、职业经历和剧情证据判断。",
        "- 如果资料没有记录，不要编造剧情；可以说“不记得/不知道/好像没有听说过”。",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build character knowledge-boundary reference files.")
    parser.add_argument("--skill-dir", required=True, type=Path)
    parser.add_argument("--profile-config", required=True, type=Path)
    parser.add_argument("--boundary-config", required=True, type=Path)
    args = parser.parse_args()

    profile = read_json(args.profile_config)
    boundary = read_json(args.boundary_config)
    analysis = load_analysis(args.profile_config, profile)

    knowledge_dir = args.skill_dir / "references" / "knowledge"
    knowledge_dir.mkdir(parents=True, exist_ok=True)

    markdown = render_markdown(args.skill_dir, profile, boundary, analysis)
    (knowledge_dir / "knowledge-boundary.md").write_text(markdown, encoding="utf-8")
    (knowledge_dir / "character-memory.json").write_text(
        json.dumps(
            {
                "profile": profile,
                "boundary": boundary,
                "analysis_summary": (analysis or {}).get("target_summary", {}),
                "top_relationships": (analysis or {}).get("relationships", [])[:12],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Wrote {knowledge_dir / 'knowledge-boundary.md'}")
    print(f"Wrote {knowledge_dir / 'character-memory.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
