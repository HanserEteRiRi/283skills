# 07 - 本地语料分析补充

## 输出文件

- 报告：`references/local-dialogue-analysis/円香-dialogue-report.md`
- JSON：`references/local-dialogue-analysis/円香-dialogue-analysis.json`
- 合并台词：`references/local-dialogue-analysis/円香-target-lines.csv`
- 日文台词：`references/local-dialogue-analysis/円香-target-lines-jp.csv`
- 中文台词：`references/local-dialogue-analysis/円香-target-lines-cn.csv`

## 统计摘要

- 总 CSV：5602。
- 总对话：253362 行。
- 円香台词：5442 行。
- 出现场景：369。
- 他人提及：798。

## 主题命中

| 主题 | 日文命中 | 中文命中 | 生成含义 |
|---|---:|---:|---|
| noctchill_childhood | 293 | 306 | 幼驯染、四人、屋上、便利店和现实照看 |
| producer_friction_boundary | 229 | 571 | P、你、代言权、担心与多余关心 |
| quiet_care | 209 | 230 | 谢谢、没关系、等待、担心和低温照看 |
| cynical_distance | 188 | 107 | 不知道、没什么、多余、同感和讽刺距离 |
| stage_idol_work | 130 | 116 | 偶像、练习、节目、舞台和粉丝 |
| school_ordinary | 76 | 40 | 学校、作业、老师、耳机、回家 |
| happiness_pain_flatness | 31 | 22 | 幸福、悲伤、平淡、波澜和伤口 |

## 语料启示

- 日文感叹号只有 42，远低于疑问符 703；生成时避免高情绪。
- 沉默/省略行 824，说明她大量使用无言判断，但沉默后通常会切出很短的核心。
- P 是最高关系权重，但自动分析低估透，因为一字说话人名被过滤；写 Noctchill 必须补回透。
- `producer_friction_boundary` 中文命中很高，说明翻译语料中“你/制作人/担心”会更显性。
