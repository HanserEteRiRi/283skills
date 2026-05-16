#!/usr/bin/env python3
"""
Analyze Shiny Colors style story CSV dialogue data for a target character.

The script is intentionally character-agnostic. Pass a target display name plus
aliases, and it will extract target lines, scenes, adjacent interactions,
mentions, phrase/theme counts, and relationship evidence.

Expected CSV columns:
    id,name,text,trans

Usage:
    python scripts/analyze_story_dialogues.py \
      --profile-config config/story-dialogue-profiles/serizawa-asahi.json

Story root discovery order:
    1. --story-root
    2. profile_config.story_root
    3. SC_TRANSLATION_STORY_ROOT / SC_TRANSLATION_DATA_ROOT
    4. ../SCTranslationData/data/story next to this nuwa-skill directory
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from statistics import mean, median
from typing import Iterable


CSV_COLUMNS = ("id", "name", "text", "trans")
ENCODINGS = ("utf-8-sig", "utf-8", "cp932", "gb18030")

SPEAKER_SPLIT_RE = re.compile(r"(?:＆|&|、|,|/|／|・|\+|＋|と|和)")

ThemeConfig = dict[str, dict[str, list[str]]]
VoiceConfig = dict[str, dict[str, str]]

IGNORE_RELATIONSHIP_SPEAKERS = {
    "",
    "off",
    "一同",
}


@dataclass(frozen=True)
class DialogueRow:
    row_id: str
    speaker: str
    text: str
    trans: str
    file: str
    rel_file: str
    category: str
    arc: str
    episode: str
    line_no: int

    @property
    def combined_text(self) -> str:
        return f"{self.text}\n{self.trans}".strip()


def read_text_with_fallback(path: Path) -> str:
    for encoding in ENCODINGS:
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace")


def normalize_text(value: str | None) -> str:
    if value is None:
        return ""
    return value.replace("\\n", "\n").strip()


def rel_parts(path: Path, root: Path) -> tuple[str, str, str, str]:
    rel = path.relative_to(root)
    parts = rel.parts
    category = parts[0] if len(parts) >= 1 else ""
    arc = parts[1] if len(parts) >= 2 else ""
    episode = path.stem
    return str(rel), category, arc, episode


def iter_dialogues(root: Path) -> Iterable[DialogueRow]:
    csv.field_size_limit(min(sys.maxsize, 2**31 - 1))
    for path in sorted(root.rglob("*.csv")):
        content = read_text_with_fallback(path)
        rel_file, category, arc, episode = rel_parts(path, root)
        try:
            reader = csv.DictReader(content.splitlines())
        except csv.Error:
            continue

        if not reader.fieldnames or not set(CSV_COLUMNS).issubset(reader.fieldnames):
            continue

        for idx, row in enumerate(reader, start=2):
            text = normalize_text(row.get("text"))
            trans = normalize_text(row.get("trans"))
            # Translation CSVs often end with metadata rows such as
            # "info,produce_events/xxxx.json,," or "译者,name,,".
            if not text and not trans:
                continue
            yield DialogueRow(
                row_id=normalize_text(row.get("id")),
                speaker=normalize_text(row.get("name")),
                text=text,
                trans=trans,
                file=str(path),
                rel_file=rel_file,
                category=category,
                arc=arc,
                episode=episode,
                line_no=idx,
            )


def split_speakers(name: str) -> list[str]:
    parts = [p.strip() for p in SPEAKER_SPLIT_RE.split(name) if p.strip()]
    return parts or ([name.strip()] if name.strip() else [])


def is_valid_relationship_name(name: str) -> bool:
    if name in IGNORE_RELATIONSHIP_SPEAKERS:
        return False
    if len(name) < 2:
        return False
    if name.endswith(".json") or "/" in name or "\\" in name:
        return False
    if re.fullmatch(r"[\W_ー─—…・]+", name):
        return False
    if re.fullmatch(r"\d+", name):
        return False
    return True


def alias_in_text(text: str, aliases: list[str]) -> bool:
    return any(alias and alias in text for alias in aliases)


def speaker_matches(name: str, aliases: list[str]) -> bool:
    for part in split_speakers(name):
        for alias in aliases:
            if part == alias:
                return True
            if part.startswith(alias):
                suffix = part[len(alias) :]
                # Include forms that are clearly the target's own message or
                # parenthetical role, but avoid "あさひの同級生" being counted
                # as Asahi speaking.
                if suffix.startswith(("のメッセージ", "(", "（", "：", ":")):
                    return True
    return False


def short_quote(row: DialogueRow, limit: int = 120) -> str:
    text = row.trans or row.text
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1] + "…"


def japanese_quote(row: DialogueRow, limit: int = 100) -> str:
    text = re.sub(r"\s+", " ", row.text).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1] + "…"


def get_lang_text(row: DialogueRow, lang: str) -> str:
    if lang == "jp":
        return row.text
    if lang == "cn":
        return row.trans
    raise ValueError(f"Unsupported language: {lang}")


def line_length_stats(rows: list[DialogueRow], lang: str) -> dict[str, float | int]:
    lengths = [len(get_lang_text(r, lang)) for r in rows if get_lang_text(r, lang)]
    if not lengths:
        return {"count": 0, "avg": 0, "median": 0, "max": 0}
    return {
        "count": len(lengths),
        "avg": round(mean(lengths), 2),
        "median": round(median(lengths), 2),
        "max": max(lengths),
    }


def count_regex(rows: list[DialogueRow], pattern: str, lang: str) -> int:
    reg = re.compile(pattern)
    return sum(len(reg.findall(get_lang_text(r, lang))) for r in rows)


def language_voice_stats(rows: list[DialogueRow], lang: str) -> dict[str, object]:
    target_text = "\n".join(get_lang_text(r, lang) for r in rows)
    ellipsis_pattern = r"[…。・\s—─]+"
    return {
        "line_length": line_length_stats(rows, lang),
        "question_marks": target_text.count("？") + target_text.count("?"),
        "exclamation_marks": target_text.count("！") + target_text.count("!"),
        "ellipsis_lines": sum(1 for r in rows if re.fullmatch(ellipsis_pattern, get_lang_text(r, lang) or "")),
        "tilde_count": target_text.count("～") + target_text.count("~"),
        "star_count": target_text.count("☆") + target_text.count("★"),
    }


def count_voice_config(rows: list[DialogueRow], config: VoiceConfig) -> dict[str, dict[str, int]]:
    result: dict[str, dict[str, int]] = {}
    for lang in ("jp", "cn"):
        result[lang] = {}
        for metric, pattern in config.get(lang, {}).items():
            result[lang][metric] = count_regex(rows, pattern, lang)
    return result


def count_theme_matches(rows: list[DialogueRow], themes: ThemeConfig) -> dict[str, dict[str, object]]:
    result: dict[str, dict[str, object]] = {}
    for theme, per_lang_patterns in themes.items():
        result[theme] = {}
        for lang in ("jp", "cn"):
            patterns = per_lang_patterns.get(lang, [])
            matches = []
            phrase_counter: Counter[str] = Counter()
            for row in rows:
                text = get_lang_text(row, lang)
                hit = False
                for pattern in patterns:
                    if pattern in text:
                        phrase_counter[pattern] += text.count(pattern)
                        hit = True
                if hit:
                    matches.append(row)
            result[theme][lang] = {
                "line_count": len(matches),
                "top_phrases": phrase_counter.most_common(12),
                "samples": [
                    {
                        "file": row.rel_file,
                        "line_no": row.line_no,
                        "speaker": row.speaker,
                        "jp": japanese_quote(row),
                        "cn": short_quote(row),
                    }
                    for row in matches[:12]
                ],
            }
    return result


def top_scene_samples(scene_rows: dict[str, list[DialogueRow]], target_aliases: list[str], n: int) -> list[dict[str, object]]:
    ranked = []
    for rel_file, rows in scene_rows.items():
        target_lines = [r for r in rows if speaker_matches(r.speaker, target_aliases)]
        if not target_lines:
            continue
        speakers = Counter()
        for r in rows:
            for speaker in split_speakers(r.speaker):
                speakers[speaker] += 1
        ranked.append(
            {
                "file": rel_file,
                "target_line_count": len(target_lines),
                "total_line_count": len(rows),
                "speakers": speakers.most_common(10),
                "first_target_line_jp": japanese_quote(target_lines[0]),
                "first_target_line_cn": short_quote(target_lines[0]),
                "last_target_line_jp": japanese_quote(target_lines[-1]),
                "last_target_line_cn": short_quote(target_lines[-1]),
            }
        )
    ranked.sort(key=lambda item: (item["target_line_count"], item["total_line_count"]), reverse=True)
    return ranked[:n]


def context_window(rows: list[DialogueRow], index: int, window: int) -> list[dict[str, object]]:
    start = max(0, index - window)
    end = min(len(rows), index + window + 1)
    result = []
    for idx in range(start, end):
        row = rows[idx]
        result.append(
            {
                "offset": idx - index,
                "speaker": row.speaker,
                "jp": row.text,
                "cn": row.trans,
                "line_no": row.line_no,
            }
        )
    return result


def relation_samples(
    scene_rows: dict[str, list[DialogueRow]],
    target_aliases: list[str],
    partner: str,
    max_samples: int = 5,
) -> list[dict[str, object]]:
    samples = []
    for rel_file, rows in scene_rows.items():
        if len(samples) >= max_samples:
            break
        has_target = any(speaker_matches(r.speaker, target_aliases) for r in rows)
        has_partner = any(partner in split_speakers(r.speaker) or partner in r.combined_text for r in rows)
        if not (has_target and has_partner):
            continue
        for idx, row in enumerate(rows):
            if speaker_matches(row.speaker, target_aliases) and (
                partner in row.combined_text
                or (idx > 0 and partner in split_speakers(rows[idx - 1].speaker))
                or (idx + 1 < len(rows) and partner in split_speakers(rows[idx + 1].speaker))
            ):
                samples.append({"file": rel_file, "line_no": row.line_no, "context": context_window(rows, idx, 2)})
                break
    return samples


def build_analysis(
    rows: list[DialogueRow],
    root: Path,
    target: str,
    aliases: list[str],
    mention_aliases: list[str],
    themes: ThemeConfig,
    voice_config: VoiceConfig,
    sample_limit: int,
) -> dict[str, object]:
    scene_rows: dict[str, list[DialogueRow]] = defaultdict(list)
    for row in rows:
        scene_rows[row.rel_file].append(row)

    target_rows = [r for r in rows if speaker_matches(r.speaker, aliases)]
    target_scene_keys = {r.rel_file for r in target_rows}
    target_scenes = {key: scene_rows[key] for key in target_scene_keys}
    mentioned_rows = [
        r
        for r in rows
        if not speaker_matches(r.speaker, aliases) and alias_in_text(r.combined_text, mention_aliases)
    ]

    speaker_counts = Counter()
    for row in rows:
        for speaker in split_speakers(row.speaker):
            speaker_counts[speaker] += 1

    target_speaker_forms = Counter(r.speaker for r in target_rows)
    category_counts = Counter(r.category for r in target_rows)
    arc_counts = Counter(r.arc for r in target_rows)

    cooccurrence = Counter()
    adjacent_prev = Counter()
    adjacent_next = Counter()
    mentions_by_speaker = Counter()
    target_mentions_other = Counter()
    all_speakers = [speaker for speaker, _ in speaker_counts.most_common()]

    for rel_file, scene in scene_rows.items():
        if rel_file not in target_scene_keys:
            continue
        scene_speakers = set()
        for row in scene:
            for speaker in split_speakers(row.speaker):
                scene_speakers.add(speaker)
        for speaker in scene_speakers:
            if is_valid_relationship_name(speaker) and not alias_in_text(speaker, aliases):
                cooccurrence[speaker] += 1

        for idx, row in enumerate(scene):
            if speaker_matches(row.speaker, aliases):
                if idx > 0:
                    for speaker in split_speakers(scene[idx - 1].speaker):
                        if is_valid_relationship_name(speaker) and not alias_in_text(speaker, aliases):
                            adjacent_prev[speaker] += 1
                if idx + 1 < len(scene):
                    for speaker in split_speakers(scene[idx + 1].speaker):
                        if is_valid_relationship_name(speaker) and not alias_in_text(speaker, aliases):
                            adjacent_next[speaker] += 1
                for speaker in all_speakers:
                    if (
                        is_valid_relationship_name(speaker)
                        and not alias_in_text(speaker, aliases)
                        and speaker in row.combined_text
                    ):
                        target_mentions_other[speaker] += 1

    for row in mentioned_rows:
        for speaker in split_speakers(row.speaker):
            if is_valid_relationship_name(speaker):
                mentions_by_speaker[speaker] += 1

    relationship_partners = []
    partner_names = set()
    for counter in (cooccurrence, adjacent_prev, adjacent_next, mentions_by_speaker, target_mentions_other):
        partner_names.update(counter.keys())
    for partner in partner_names:
        score = (
            cooccurrence[partner] * 2
            + adjacent_prev[partner]
            + adjacent_next[partner]
            + mentions_by_speaker[partner]
            + target_mentions_other[partner]
        )
        if score <= 0:
            continue
        relationship_partners.append(
            {
                "partner": partner,
                "score": score,
                "scene_cooccurrence": cooccurrence[partner],
                "prev_to_target": adjacent_prev[partner],
                "target_to_next": adjacent_next[partner],
                "mentions_target": mentions_by_speaker[partner],
                "target_mentions_partner": target_mentions_other[partner],
                "samples": [],
            }
        )
    relationship_partners.sort(key=lambda item: item["score"], reverse=True)

    # Context sampling is intentionally limited to the strongest relationships.
    # Scanning every scene once per low-signal partner is too slow for large
    # translation corpora with thousands of CSV files.
    for item in relationship_partners[:20]:
        item["samples"] = relation_samples(scene_rows, aliases, str(item["partner"]), max_samples=3)

    configured_voice_stats = count_voice_config(target_rows, voice_config)
    voice_stats = {
        "jp": {**language_voice_stats(target_rows, "jp"), **configured_voice_stats.get("jp", {})},
        "cn": {**language_voice_stats(target_rows, "cn"), **configured_voice_stats.get("cn", {})},
    }

    theme_matches = count_theme_matches(target_rows, themes)

    sample_target_lines = [
        {
            "file": row.rel_file,
            "line_no": row.line_no,
            "speaker": row.speaker,
            "jp": row.text,
            "cn": row.trans,
        }
        for row in target_rows[:sample_limit]
    ]

    return {
        "metadata": {
            "story_root": str(root),
            "target": target,
            "aliases": aliases,
            "mention_aliases": mention_aliases,
            "total_rows": len(rows),
            "total_files": len({r.rel_file for r in rows}),
            "total_speakers": len(speaker_counts),
        },
        "target_summary": {
            "target_line_count": len(target_rows),
            "target_scene_count": len(target_scene_keys),
            "mentioned_by_others_count": len(mentioned_rows),
            "speaker_forms": target_speaker_forms.most_common(20),
            "top_categories": category_counts.most_common(20),
            "top_arcs": arc_counts.most_common(30),
            "top_scenes": top_scene_samples(scene_rows, aliases, sample_limit),
        },
        "relationships": relationship_partners[:50],
        "voice_stats": voice_stats,
        "themes": theme_matches,
        "sample_target_lines": sample_target_lines,
        "mention_samples": [
            {
                "file": row.rel_file,
                "line_no": row.line_no,
                "speaker": row.speaker,
                "jp": row.text,
                "cn": row.trans,
            }
            for row in mentioned_rows[:sample_limit]
        ],
    }


def write_json(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def write_target_lines_csv(path: Path, rows: list[DialogueRow], aliases: list[str]) -> None:
    target_rows = [r for r in rows if speaker_matches(r.speaker, aliases)]
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "file",
                "line_no",
                "id",
                "speaker",
                "text",
                "trans",
                "category",
                "arc",
                "episode",
            ],
        )
        writer.writeheader()
        for row in target_rows:
            writer.writerow(
                {
                    "file": row.rel_file,
                    "line_no": row.line_no,
                    "id": row.row_id,
                    "speaker": row.speaker,
                    "text": row.text,
                    "trans": row.trans,
                    "category": row.category,
                    "arc": row.arc,
                    "episode": row.episode,
                }
            )


def write_language_target_lines_csv(path: Path, rows: list[DialogueRow], aliases: list[str], lang: str) -> None:
    target_rows = [r for r in rows if speaker_matches(r.speaker, aliases)]
    text_field = "text" if lang == "jp" else "trans"
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "file",
                "line_no",
                "id",
                "speaker",
                text_field,
                "category",
                "arc",
                "episode",
            ],
        )
        writer.writeheader()
        for row in target_rows:
            writer.writerow(
                {
                    "file": row.rel_file,
                    "line_no": row.line_no,
                    "id": row.row_id,
                    "speaker": row.speaker,
                    text_field: get_lang_text(row, lang),
                    "category": row.category,
                    "arc": row.arc,
                    "episode": row.episode,
                }
            )


def md_table(rows: list[list[object]], headers: list[str]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        clean = [str(cell).replace("\n", "<br>").replace("|", "\\|") for cell in row]
        lines.append("| " + " | ".join(clean) + " |")
    return "\n".join(lines)


def voice_metric_rows(stats: dict[str, object]) -> list[list[object]]:
    labels = {
        "ssu_count": "っす",
        "laugh_count": "笑声",
        "again_count": "もう一回/再来一次",
        "unknown_count": "わからない/不知道",
        "first_person_count": "第一人称/自称",
    }
    rows = [
        ["平均长度", stats["line_length"]["avg"]],
        ["长度中位数", stats["line_length"]["median"]],
        ["最长长度", stats["line_length"]["max"]],
        ["疑问符", stats["question_marks"]],
        ["感叹符", stats["exclamation_marks"]],
        ["沉默/省略行", stats["ellipsis_lines"]],
        ["波浪号", stats["tilde_count"]],
        ["星号", stats["star_count"]],
    ]
    base_keys = {
        "line_length",
        "question_marks",
        "exclamation_marks",
        "ellipsis_lines",
        "tilde_count",
        "star_count",
    }
    for key in sorted(k for k in stats.keys() if k not in base_keys):
        rows.append([labels.get(key, key), stats[key]])
    return rows


def write_markdown(path: Path, analysis: dict[str, object]) -> None:
    meta = analysis["metadata"]
    summary = analysis["target_summary"]
    voice = analysis["voice_stats"]
    relationships = analysis["relationships"]
    themes = analysis["themes"]

    lines: list[str] = []
    lines.append(f"# {meta['target']} 本地对话语料分析")
    lines.append("")
    lines.append("此报告由 `scripts/analyze_story_dialogues.py` 自动生成，用于角色蒸馏。")
    lines.append("")
    lines.append("## 语料概况")
    lines.append("")
    lines.append(
        md_table(
            [
                ["故事根目录", meta["story_root"]],
                ["总 CSV 文件数", meta["total_files"]],
                ["总对话行数", meta["total_rows"]],
                ["总说话人形式数", meta["total_speakers"]],
                ["目标台词行数", summary["target_line_count"]],
                ["目标出现场景数", summary["target_scene_count"]],
                ["他人提及目标行数", summary["mentioned_by_others_count"]],
            ],
            ["项目", "值"],
        )
    )
    lines.append("")
    lines.append("## 日文原文口癖与节奏")
    lines.append("")
    jp_voice = voice["jp"]
    lines.append(md_table(voice_metric_rows(jp_voice), ["指标", "值"]))
    lines.append("")
    lines.append("## 中文翻译口癖与节奏")
    lines.append("")
    cn_voice = voice["cn"]
    lines.append(md_table(voice_metric_rows(cn_voice), ["指标", "值"]))
    lines.append("")
    lines.append("## 主题匹配")
    lines.append("")
    theme_rows = []
    for theme, data in themes.items():
        jp_data = data["jp"]
        cn_data = data["cn"]
        jp_top = ", ".join(f"{phrase}:{count}" for phrase, count in jp_data["top_phrases"][:8])
        cn_top = ", ".join(f"{phrase}:{count}" for phrase, count in cn_data["top_phrases"][:8])
        theme_rows.append([theme, jp_data["line_count"], jp_top, cn_data["line_count"], cn_top])
    lines.append(md_table(theme_rows, ["主题", "日文命中", "日文高频词", "中文命中", "中文高频词"]))
    lines.append("")
    lines.append("## 人物关系")
    lines.append("")
    rel_rows = []
    for item in relationships[:20]:
        rel_rows.append(
            [
                item["partner"],
                item["score"],
                item["scene_cooccurrence"],
                item["prev_to_target"],
                item["target_to_next"],
                item["mentions_target"],
                item["target_mentions_partner"],
            ]
        )
    lines.append(
        md_table(
            rel_rows,
            ["对象", "综合分", "共现场景", "上一句->目标", "目标->下一句", "提及目标", "目标提及对象"],
        )
    )
    lines.append("")
    lines.append("## 高频场景")
    lines.append("")
    scene_rows = []
    for item in summary["top_scenes"][:20]:
        speakers = ", ".join(f"{name}:{count}" for name, count in item["speakers"][:6])
        scene_rows.append(
            [
                item["file"],
                item["target_line_count"],
                item["total_line_count"],
                speakers,
                item["first_target_line_jp"],
                item["first_target_line_cn"],
            ]
        )
    lines.append(md_table(scene_rows, ["文件", "目标台词", "总行数", "主要说话人", "首句日文", "首句中文"]))
    lines.append("")
    lines.append("## 关系样本")
    lines.append("")
    for item in relationships[:8]:
        lines.append(f"### {item['partner']}")
        if not item["samples"]:
            lines.append("")
            lines.append("无样本。")
            lines.append("")
            continue
        for sample in item["samples"][:2]:
            lines.append("")
            lines.append(f"- `{sample['file']}:{sample['line_no']}`")
            for ctx in sample["context"]:
                marker = ">" if ctx["offset"] == 0 else " "
                cn = re.sub(r"\s+", " ", ctx["cn"]).strip()
                jp = re.sub(r"\s+", " ", ctx["jp"]).strip()
                lines.append(f"  {marker} **{ctx['speaker']}**: {cn} / {jp}")
        lines.append("")
    lines.append("## 目标台词样本")
    lines.append("")
    for row in analysis["sample_target_lines"][:30]:
        lines.append(f"- `{row['file']}:{row['line_no']}` **{row['speaker']}**: {row['cn']} / {row['jp']}")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def load_themes(path: Path | None) -> ThemeConfig:
    if path is None:
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Theme config must be a JSON object")
    normalized: ThemeConfig = {}
    for key, values in data.items():
        theme = str(key)
        if isinstance(values, dict):
            normalized[theme] = {
                "jp": [str(v) for v in values.get("jp", [])],
                "cn": [str(v) for v in values.get("cn", [])],
            }
        else:
            # Backward-compatible form: a simple list is applied to both
            # languages, though explicit jp/cn config is preferred.
            shared = [str(v) for v in values]
            normalized[theme] = {"jp": shared, "cn": shared}
    return normalized


def load_voice_config(path: Path | None) -> VoiceConfig:
    if path is None:
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Voice config must be a JSON object")
    normalized: VoiceConfig = {}
    for lang in ("jp", "cn"):
        values = data.get(lang, {})
        if not isinstance(values, dict):
            raise ValueError(f"Voice config language block must be an object: {lang}")
        normalized[lang] = {str(key): str(pattern) for key, pattern in values.items()}
    return normalized


def load_profile(path: Path | None) -> dict[str, object]:
    if path is None:
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Profile config must be a JSON object")
    return data


def resolve_config_path(profile_path: Path | None, value: object) -> Path | None:
    if not value:
        return None
    path = Path(str(value))
    if path.is_absolute() or profile_path is None:
        return path
    return (profile_path.parent / path).resolve()


def discover_story_root(profile_path: Path | None, explicit: Path | None, profile: dict[str, object]) -> Path | None:
    """Find SCTranslationData/data/story without baking in a local C: drive path."""
    candidates: list[Path] = []
    if explicit is not None:
        candidates.append(explicit)

    profile_story_root = resolve_config_path(profile_path, profile.get("story_root"))
    if profile_story_root is not None:
        candidates.append(profile_story_root)

    for env_name in ("SC_TRANSLATION_STORY_ROOT", "SC_TRANSLATION_DATA_ROOT", "SHINYCOLORS_STORY_ROOT"):
        env_value = os.environ.get(env_name)
        if not env_value:
            continue
        env_path = Path(env_value)
        if env_path.name == "SCTranslationData":
            candidates.append(env_path / "data" / "story")
        else:
            candidates.append(env_path)

    script_root = Path(__file__).resolve().parents[1]
    workspace_root = script_root.parent
    cwd = Path.cwd()
    candidates.extend(
        [
            workspace_root / "SCTranslationData" / "data" / "story",
            script_root / ".." / "SCTranslationData" / "data" / "story",
            cwd / "SCTranslationData" / "data" / "story",
            cwd / ".." / "SCTranslationData" / "data" / "story",
            cwd / "data" / "story",
        ]
    )

    for candidate in candidates:
        resolved = candidate.expanduser().resolve()
        if resolved.exists() and resolved.is_dir():
            return resolved
    return None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze story dialogue CSVs for a target character.")
    parser.add_argument(
        "--story-root",
        type=Path,
        default=None,
        help="Root directory containing story CSV files. If omitted, the script auto-discovers SCTranslationData/data/story.",
    )
    parser.add_argument("--profile-config", type=Path, default=None, help="Optional JSON profile with target, aliases, configs, and output_dir.")
    parser.add_argument("--target", default=None, help="Target character display name. Overrides profile target.")
    parser.add_argument("--aliases", nargs="+", default=[], help="Aliases used for speaker matching.")
    parser.add_argument(
        "--mention-aliases",
        nargs="+",
        default=[],
        help="Aliases used for text mention matching. Defaults to --aliases/profile aliases.",
    )
    parser.add_argument("--output-dir", type=Path, default=None, help="Directory for report outputs. Overrides profile output_dir.")
    parser.add_argument(
        "--theme-config",
        type=Path,
        default=None,
        help="Optional JSON theme config. Overrides profile theme_config. If omitted, theme matching is skipped.",
    )
    parser.add_argument(
        "--voice-config",
        type=Path,
        default=None,
        help="Optional JSON voice metric config. Overrides profile voice_config. If omitted, only base punctuation stats are emitted.",
    )
    parser.add_argument("--sample-limit", type=int, default=30, help="Number of samples to include.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    profile = load_profile(args.profile_config)
    root = discover_story_root(args.profile_config, args.story_root, profile)
    if root is None:
        print(
            "Story root not found. Provide --story-root, set SC_TRANSLATION_STORY_ROOT, "
            "or place SCTranslationData next to nuwa-skill.",
            file=sys.stderr,
        )
        return 2

    target = args.target or profile.get("target")
    if not target:
        print("Target is required. Provide --target or profile_config.target.", file=sys.stderr)
        return 2
    target = str(target)

    profile_aliases = profile.get("aliases", [])
    if not isinstance(profile_aliases, list):
        print("profile_config.aliases must be a list.", file=sys.stderr)
        return 2
    aliases = [target, *(str(alias) for alias in profile_aliases), *args.aliases]
    aliases = list(dict.fromkeys(alias for alias in aliases if alias))

    profile_mention_aliases = profile.get("mention_aliases", [])
    if profile_mention_aliases and not isinstance(profile_mention_aliases, list):
        print("profile_config.mention_aliases must be a list.", file=sys.stderr)
        return 2
    mention_aliases = [*(str(alias) for alias in profile_mention_aliases), *args.mention_aliases]
    mention_aliases = list(dict.fromkeys(alias for alias in mention_aliases if alias))
    if not mention_aliases:
        mention_aliases = aliases

    theme_path = args.theme_config or resolve_config_path(args.profile_config, profile.get("theme_config"))
    voice_path = args.voice_config or resolve_config_path(args.profile_config, profile.get("voice_config"))
    output_dir = args.output_dir or resolve_config_path(args.profile_config, profile.get("output_dir"))
    if output_dir is None:
        print("Output dir is required. Provide --output-dir or profile_config.output_dir.", file=sys.stderr)
        return 2

    themes = load_themes(theme_path)
    if not themes:
        print("No theme config provided; theme matching will be skipped.", file=sys.stderr)
    voice_config = load_voice_config(voice_path)

    rows = list(iter_dialogues(root))
    analysis = build_analysis(rows, root, target, aliases, mention_aliases, themes, voice_config, args.sample_limit)

    output_dir.mkdir(parents=True, exist_ok=True)
    write_json(output_dir / f"{target}-dialogue-analysis.json", analysis)
    write_markdown(output_dir / f"{target}-dialogue-report.md", analysis)
    write_target_lines_csv(output_dir / f"{target}-target-lines.csv", rows, aliases)
    write_language_target_lines_csv(output_dir / f"{target}-target-lines-jp.csv", rows, aliases, "jp")
    write_language_target_lines_csv(output_dir / f"{target}-target-lines-cn.csv", rows, aliases, "cn")

    summary = analysis["target_summary"]
    print(f"Analyzed {analysis['metadata']['total_files']} files / {analysis['metadata']['total_rows']} rows")
    print(f"Target lines: {summary['target_line_count']}")
    print(f"Target scenes: {summary['target_scene_count']}")
    print(f"Report: {output_dir / f'{target}-dialogue-report.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
