# 07 - 本地对话语料：中日分离分析

> 数据源：`C:\project\SCTranslationData\data\story`  
> 分析脚本：`scripts/analyze_story_dialogues.py`  
> 角色 profile：`config/story-dialogue-profiles/osaki-amana.json`  
> 输出目录：`references/local-dialogue-analysis/`

## 输出文件

| 文件 | 用途 |
|---|---|
| `甘奈-dialogue-report.md` | 人类可读分析报告 |
| `甘奈-dialogue-analysis.json` | 结构化统计与样本 |
| `甘奈-target-lines.csv` | 中日合并目标台词 |
| `甘奈-target-lines-jp.csv` | 仅日文原文目标台词 |
| `甘奈-target-lines-cn.csv` | 仅中文翻译目标台词 |

## 语料概况

| 指标 | 数值 |
|---|---:|
| 总 CSV 文件数 | 5603 |
| 总对话行数 | 253411 |
| 甘奈台词行数 | 6166 |
| 甘奈出现场景数 | 335 |
| 他人提及甘奈 | 907 |

## 重要发现

1. 甘奈不是 `っす` 角色。日文原文中 `っす` 仅 8 次，应避免混成あさひ。
2. 甘奈高频使用波浪号和星号：日文 `～` 828 次、`☆` 531 次；中文译文也高度保留。
3. 甘奈的第一人称非常显著：日文“甘奈/私/あたし”865 次，中文“甘奈/我”1521 次。
4. 关系主题强于行动主题：甜花、P、千雪三者远超其他人物。
5. `care_support` 和 `fashion_cute` 都是稳定主题，说明“照顾”和“可爱/时尚”都不是表层。

## 对 Skill 的修正

- 回答工作流必须先判断语言：中文走“中文译文甘奈”，日文走“日文原声甘奈”。
- 甘奈的建议应先照顾关系，再给行动方案。
- 若问题涉及双子/家人/队友，应主动检查“保护 vs 代替”的边界。
- 若问题涉及创作、穿搭、舞台或企划，应允许她用“可爱/准备/幸福感”作为有效分析维度。
