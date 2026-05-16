# 07 - 本地语料分析补充

## 输出文件

- 报告：`references/local-dialogue-analysis/めぐる-dialogue-report.md`
- JSON：`references/local-dialogue-analysis/めぐる-dialogue-analysis.json`
- 合并台词：`references/local-dialogue-analysis/めぐる-target-lines.csv`
- 日文台词：`references/local-dialogue-analysis/めぐる-target-lines-jp.csv`
- 中文台词：`references/local-dialogue-analysis/めぐる-target-lines-cn.csv`

## 统计摘要

- 总 CSV：5602。
- 总对话：253362 行。
- めぐる台词：9448 行。
- 出现场景：494。
- 他人提及：1754。

## 主题命中

| 主题 | 日文命中 | 中文命中 | 生成含义 |
|---|---:|---:|---|
| energetic_friendship | 825 | 852 | 大家、一起、朋友、开心 |
| action_sports_body | 225 | 295 | 快走、运动、练习、身体 |
| illumination_bonds | 1429 | 1477 | 真乃、灯織、三人关系 |
| honesty_empathy | 642 | 439 | 谢谢、对不起、没关系和担心 |
| america_family_identity | 27 | 28 | 美国、妈妈、家人身份线索 |
| producer_fans | 841 | 948 | P、粉丝、看着、传达 |
| idol_stage_work | 261 | 231 | 偶像、舞台、练习、拍摄 |

## 语料启示

- めぐる的高频能量很强，但 `honesty_empathy` 说明她也有认真照顾和道歉。
- 灯織、P、真乃是最高关系权重；不要让她泛化成所有人的朋友而忘掉三人轴。
- 感叹号与长音非常多，生成要保留高能但控制密度。
- 生成时必须把官方 canon、本地语料、二创推演分层。
