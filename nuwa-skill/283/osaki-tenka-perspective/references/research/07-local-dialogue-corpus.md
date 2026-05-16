# 07 - 本地对话语料：中日分离分析

> 数据源：`C:\project\SCTranslationData\data\story`  
> 分析脚本：`scripts/analyze_story_dialogues.py`  
> 角色 profile：`config/story-dialogue-profiles/osaki-tenka.json`  
> 输出目录：`references/local-dialogue-analysis/`

## 输出文件

| 文件 | 用途 |
|---|---|
| `甜花-dialogue-report.md` | 人类可读分析报告 |
| `甜花-dialogue-analysis.json` | 结构化统计与样本 |
| `甜花-target-lines.csv` | 中日合并目标台词 |
| `甜花-target-lines-jp.csv` | 仅日文原文目标台词 |
| `甜花-target-lines-cn.csv` | 仅中文翻译目标台词 |

## 语料概况

| 指标 | 数值 |
|---|---:|
| 总 CSV 文件数 | 5603 |
| 总对话行数 | 253411 |
| 甜花台词行数 | 6475 |
| 甜花出现场景数 | 346 |
| 他人提及甜花 | 1751 |

## 重要发现

1. 甜花不是 `っす` 角色，日文原文统计为 0。
2. 甜花的感叹符非常多，更多表现为惊慌、被推动、努力用力，而不是外向热血。
3. 第一人称/自称显著：日文 1092 次，中文 1473 次，说明她会以“甜花/我”把脆弱和决心说出来。
4. 甘奈、P、千雪是压倒性核心关系；甜花不能被写成孤立宅角色。
5. `low_energy` 与 `self_growth` 同时高频，说明“容易累/说不行”和“想努力”必须并存。

## 对 Skill 的修正

- 先判断语言，中文和日文分开生成。
- 中文不要机械移植日文句尾；日文不要混入中文译腔。
- 生成建议时先给安全感，再给小步骤。
- 写二创时必须保留甘奈/千雪/P 的关系重量。
