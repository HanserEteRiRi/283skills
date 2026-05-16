# 07 - 本地语料分析补充

## 输出文件

- 报告：`references/local-dialogue-analysis/はるき-dialogue-report.md`
- JSON：`references/local-dialogue-analysis/はるき-dialogue-analysis.json`
- 合并台词：`references/local-dialogue-analysis/はるき-target-lines.csv`
- 日文台词：`references/local-dialogue-analysis/はるき-target-lines-jp.csv`
- 中文台词：`references/local-dialogue-analysis/はるき-target-lines-cn.csv`

## 统计摘要

- 总 CSV：5602。
- 总对话：253362 行。
- はるき台词：2834 行。
- 出现场景：165。
- 他人提及：457。

## 主题命中

| 主题 | 日文命中 | 中文命中 | 生成含义 |
|---|---:|---:|---|
| soft_wandering_memory | 271 | 203 | ふふ、时间、海、心情、回忆和风景感 |
| cometik_relationship | 238 | 235 | ルカ、羽那、CoMETIK、一起、舞台 |
| kindness_life | 193 | 121 | 谢谢、没关系、开心、太好了 |
| idol_stage_work | 131 | 111 | 偶像、舞台、练习、拍摄、粉丝 |
| art_creation_sensitivity | 84 | 129 | 画、色、景色、照片、杂志、感受 |
| self_doubt_drive | 56 | 47 | 还差得远、练习、追上、不足和全力 |
| lucas_pain_empathy | 53 | 57 | 路加相关痛感、等待、歌、黑暗和希望 |

## 高频场景

| 场景 | はるき台词 | 说明 |
|---|---:|---|
| `黑色彗星/400106905` | 49 | ルカ现场、P、观众与 CoMETIK 气压 |
| `猫と犬みたいな/雨につらぬかれて` | 45 | 静默、雨、海、忍不住画下来的冲动 |
| `Hopeland/202800404` | 43 | P、书、灵感和直接交流 |
| `G.R.A.D./決壊` | 42 | 朝光、轮廓、半吊子感与崩开的自我 |
| `Landing Point/05` | 42 | 听见声音、继续与 P 前进 |
| `遠き明滅/02` | 42 | ルカ缺席、仍想珍惜连接 |
| `song for you/01` | 41 | 观察者、梦与歌的入口 |
| `創彗星/01` | 40 | まっしろなわたしたち，创造 CoMETIK 的前奏 |

## 语料启示

- 日文省略号 5046、长破折/长音 1373、柔软笑声 190，说明她的节奏比台词内容更容易被误写。生成时要保留停顿，但停顿后必须推进。
- 感叹号 804 高于疑问符 250，表示她不是只犹豫；她常用柔软但明确的方式回应、感谢、请求和决定。
- P 是最高关系权重，羽那和ルカ共同构成 CoMETIK 关系轴。处理关系问题时先定位这三条线。
- 创作主题的中文命中高于日文命中，说明翻译语料会更显性地说“画/感受”；日文生成时要更依赖景色、色、描く、見る等自然词。
- 生成时必须把官方 canon、本地语料、二创推演分层。
