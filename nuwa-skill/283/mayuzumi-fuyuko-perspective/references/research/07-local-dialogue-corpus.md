# 07 - 本地语料分析补充

## 输出文件

- 报告：`references/local-dialogue-analysis/冬優子-dialogue-report.md`
- JSON：`references/local-dialogue-analysis/冬優子-dialogue-analysis.json`
- 合并台词：`references/local-dialogue-analysis/冬優子-target-lines.csv`
- 日文台词：`references/local-dialogue-analysis/冬優子-target-lines-jp.csv`
- 中文台词：`references/local-dialogue-analysis/冬優子-target-lines-cn.csv`

## 统计摘要

- 总 CSV：5603。
- 总对话：253411 行。
- 冬優子台词：7721 行。
- 出现场景：402。
- 他人提及：1485。

## 主题命中

| 主题 | 日文命中 | 中文命中 | 生成含义 |
|---|---:|---:|---|
| persona_double_cast | 1175 | 1299 | 公开ふゆ / 后台冬優子 / 好感度经营 |
| irritation_tsukkomi | 864 | 142 | 私下吐槽、`あんた`、`バカ`、风险提醒 |
| care_management | 564 | 562 | 保护、准备、看着、粉丝和工作现场管理 |
| cute_desire | 315 | 567 | 可爱、甜、心形、喜欢和偶像装饰 |
| straylight | 538 | 579 | あさひ、愛依、组合、Live、练习 |
| vulnerability_true_feeling | 359 | 375 | 谢谢、真的、心情、说不出口 |

## 高频场景

| 场景 | 冬優子台词 | 说明 |
|---|---:|---|
| `The Straylight/第2话-TYPE ERROR` | 62 | 出道前冲突与团队定位 |
| `Straylight.run()/FREEDOM` | 59 | 商品/镜头/自由与失控 |
| `Straylight.run()/LIBERTY` | 57 | Straylight 三人互动和舞台前后 |
| `とまりかぜの春たちは02` | 52 | 跨单位主持和礼貌模式 |
| `The Straylight/第1话-ELSE IF` | 50 | 圆阵、表演、门面和后台语气 |
| `Straylight.run()/WE WILL` | 47 | 失败、输赢和吐槽中的不甘 |
| `The Straylight/第5话-PLAYBACK` | 46 | 网络/评价/P/愛依关系 |
| `Straylight.run()/FALSE` | 46 | 规则确认、分工、ファンサ指导 |

## 语料启示

- 冬優子的“可爱”不是点缀，而是她分析场合和调度行动的默认界面。
- 私下粗口和公开礼貌必须双栈生成；只留其中一种都会失真。
- 她对 P 的强硬通常夹着感谢，对あさひ和愛依的烦躁通常夹着照顾。
- 她非常在意“看着”：粉丝怎么看、P 有没有看、镜头和工作人员会怎么判断。
- 生成时必须把官方 canon、本地语料、二创推演分层。
