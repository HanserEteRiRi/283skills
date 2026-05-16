# 07 - 本地语料分析补充

## 输出文件

- 报告：`references/local-dialogue-analysis/透-dialogue-report.md`
- JSON：`references/local-dialogue-analysis/透-dialogue-analysis.json`
- 合并台词：`references/local-dialogue-analysis/透-target-lines.csv`
- 日文台词：`references/local-dialogue-analysis/透-target-lines-jp.csv`
- 中文台词：`references/local-dialogue-analysis/透-target-lines-cn.csv`

## 统计摘要

- 总 CSV：5603。
- 总对话：253411 行。
- 透台词：6341 行。
- 出现场景：373。
- 他人提及：132。

## 高频场景

| 场景 | 透台词 | 说明 |
|---|---:|---|
| `海へ出るつもりじゃなかったし/终章` | 76 | Noctchill 集体行动和海的意象 |
| `海へ出るつもりじゃなかったし/第2话` | 58 | 夜、等待、四人关系 |
| `天槛/第6话` | 57 | 主题事件中的外部视线 |
| `ワールプールフールガールズ/终章` | 51 | 四人行动与重复尝试 |
| `浅倉透/【faaaar】/so easy` | 50 | 透个人卡剧情的跳跃行动 |
| `天塵/第5话` | 49 | 透与雛菜同步、练习和评价 |
| `W.I.N.G./produce_events_102000105` | 33 | 攀登架记忆、日誌、开心传达 |

## 语料启示

- 透的口吻最重要的是“短”和“空白”，不是奇怪词汇本身。
- 她的慢不是迟钝，很多时候是在自己内部已经把感觉走完，只是外部还没听见。
- P 的误读是透剧情的重要发动机；生成时不能把 P 写成无条件读懂。
- 透与 Noctchill 的关系高权重且均衡，三位幼驯染都不能被省略。
- 单字 speaker `透` 容易与“透明”误撞，因此分析脚本已把 speaker aliases 和 text mention aliases 分离。
