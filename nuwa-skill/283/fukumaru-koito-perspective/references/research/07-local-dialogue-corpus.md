# 07 - 本地语料分析补充

## 输出文件

- 报告：`references/local-dialogue-analysis/小糸-dialogue-report.md`
- JSON：`references/local-dialogue-analysis/小糸-dialogue-analysis.json`
- 合并台词：`references/local-dialogue-analysis/小糸-target-lines.csv`
- 日文台词：`references/local-dialogue-analysis/小糸-target-lines-jp.csv`
- 中文台词：`references/local-dialogue-analysis/小糸-target-lines-cn.csv`

## 统计摘要

- 总 CSV：5602。
- 总对话：253362 行。
- 小糸台词：6364 行。
- 出现场景：365。
- 他人提及：983。

## 主题命中

| 主题 | 日文命中 | 中文命中 | 生成含义 |
|---|---:|---:|---|
| stutter_shyness | 1124 | 673 | 结巴、ぴぇ、怕生和紧张入口 |
| noctchill_childhood | 727 | 764 | 透、円香、雛菜、大家、幼驯染记忆 |
| small_courage_growth | 360 | 433 | 小步成长、我也要做、没关系 |
| care_responsibility | 374 | 232 | 感谢、道歉、确认、责任感 |
| effort_study | 203 | 193 | 学习、练习、努力、好好做 |
| idol_stage_work | 192 | 201 | 偶像、粉丝、节目、舞台工作 |
| family_daily_life | 121 | 338 | 学校、家、便当、妹妹、点心 |

## 高频场景

| 场景 | 小糸台词 | 说明 |
|---|---:|---|
| `海へ出るつもりじゃなかったし/终章` | 51 | Noctchill 四人、海与记忆 |
| `天槛/第3话` | 46 | 本番、学校和四人关系 |
| `天塵/第2话` | 45 | 练习、视界和小糸跟上大家 |
| `G.R.A.D./ゆううつな受動態` | 45 | 自我介绍、应援和优胜目标 |
| `海へ出るつもりじゃなかったし/第5话` | 44 | Noctchill 集体行动 |
| `天塵/第4话` | 43 | 训练、圆香与小糸关系 |
| `Landing Point/縫い違えても` | 38 | 个人成长和小步坚持 |
| `小糸STEP/怖くないの？` | 37 | 害怕、看见和行动选择 |

## 语料启示

- 小糸的结巴非常强：日文 stutter 2008、中文 1515，但不能只当作表面口癖。
- 感叹号远高于疑问符，说明她紧张时常用力回应，而不是低声消失。
- P 是最高权重关系，但 Noctchill 三人是她的关系底盘。
- 她的努力词虽然不如结巴高频，但在学习、练习、节目和粉丝问题上决定行动方向。
- 生成时必须把官方 canon、本地语料、二创推演分层。
