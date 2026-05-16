# 07 - 本地语料分析补充

## 输出文件

- 报告：`references/local-dialogue-analysis/灯織-dialogue-report.md`
- JSON：`references/local-dialogue-analysis/灯織-dialogue-analysis.json`
- 合并台词：`references/local-dialogue-analysis/灯織-target-lines.csv`
- 日文台词：`references/local-dialogue-analysis/灯織-target-lines-jp.csv`
- 中文台词：`references/local-dialogue-analysis/灯織-target-lines-cn.csv`

## 统计摘要

- 总 CSV：5602。
- 总对话：253362 行。
- 灯織台词：8816 行。
- 出现场景：452。
- 他人提及：1846。

## 主题命中

| 主题 | 日文命中 | 中文命中 | 生成含义 |
|---|---:|---:|---|
| stoic_effort | 179 | 267 | 练习、准备、努力、完美与反省 |
| self_doubt_anxiety | 349 | 183 | 道歉、担心、做不到和不安 |
| illumination_bonds | 917 | 955 | 真乃、めぐる、三人关系 |
| producer_guidance | 798 | 766 | P、感谢、确认和建议 |
| scenery_music_fortune | 209 | 167 | 景色、音乐、占卜、未来 |
| care_responsibility | 241 | 143 | 没关系、帮忙、联系、责任 |
| idol_stage_work | 291 | 288 | 偶像、练习、粉丝、舞台、拍摄 |

## 语料启示

- 灯織的高频不是“冷”，而是努力、不安、确认和责任。
- めぐる、P、真乃是最高关系权重；三人关系比泛泛社交更重要。
- 问句和礼貌表达很高，生成时要让她先确认再判断。
- 生成时必须把官方 canon、本地语料、二创推演分层。
