# 07 - 本地对话语料：中日分离分析

> 数据源：`C:\project\SCTranslationData\data\story`  
> 分析脚本：`scripts/analyze_story_dialogues.py`  
> 角色 profile：`config/story-dialogue-profiles/kuwayama-chiyuki.json`  
> 输出目录：`references/local-dialogue-analysis/`

## 输出文件

| 文件 | 用途 |
|---|---|
| `千雪-dialogue-report.md` | 人类可读分析报告 |
| `千雪-dialogue-analysis.json` | 结构化统计与样本 |
| `千雪-target-lines.csv` | 中日合并目标台词 |
| `千雪-target-lines-jp.csv` | 仅日文原文目标台词 |
| `千雪-target-lines-cn.csv` | 仅中文翻译目标台词 |

## 语料概况

| 指标 | 数值 |
|---|---:|
| 总 CSV 文件数 | 5603 |
| 总对话行数 | 253411 |
| 千雪台词行数 | 4756 |
| 千雪出现场景数 | 288 |
| 他人提及千雪 | 1079 |

## 重要发现

1. 千雪不是 `っす` 角色，日文统计只有 2 次，不应当作为口癖。
2. 日文笑声 521 次，说明她经常用柔和笑声缓冲关系。
3. 第一人称/自称显著：日文 518 次，中文 1199 次，说明“自我愿望”必须纳入。
4. P、甘奈、甜花是压倒性核心关系；千雪是三人关系的支撑点和调停者。
5. `hidden_desire` 和 `gentle_care` 同时高频，说明温柔与内在愿望必须并存。

## 对 Skill 的修正

- 先判断语言，中文和日文分开生成。
- 中文不要机械移植日文句尾；日文不要混入中文译腔。
- 生成建议时先安定情绪，再温柔地问真实愿望。
- 写二创时必须让千雪有自己的“我想”，而不是只照顾双子。
