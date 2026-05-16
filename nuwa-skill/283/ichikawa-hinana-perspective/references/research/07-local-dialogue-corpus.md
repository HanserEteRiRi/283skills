# 07 - 本地语料分析补充

## 输出文件

- 报告：`references/local-dialogue-analysis/雛菜-dialogue-report.md`
- JSON：`references/local-dialogue-analysis/雛菜-dialogue-analysis.json`
- 合并台词：`references/local-dialogue-analysis/雛菜-target-lines.csv`
- 日文台词：`references/local-dialogue-analysis/雛菜-target-lines-jp.csv`
- 中文台词：`references/local-dialogue-analysis/雛菜-target-lines-cn.csv`

## 统计摘要

- 总 CSV：5602。
- 总对话：253362 行。
- 雛菜台词：5554 行。
- 出现场景：358。
- 他人提及：861。

## 主题命中

| 主题 | 日文命中 | 中文命中 | 生成含义 |
|---|---:|---:|---|
| happiness_self | 1166 | 1577 | しあわせ、开心、可爱、啊哈和自我判断 |
| noctchill_relationship | 658 | 531 | 透、小糸、円香、前辈和四人关系 |
| free_action_mypace | 292 | 507 | 想做、回家、睡觉、点心、行动快 |
| toru_admiration | 282 | 321 | 透先輩、一起、便利店和回家 |
| cute_food_daily | 211 | 251 | 点心、便利店、化妆、衣服、雨和学校 |
| sharp_boundaries_truth | 181 | 126 | 不知道、不行、不喜欢、不幸福 |
| stage_work_fans | 178 | 254 | 偶像、练习、粉丝、节目、拍摄 |

## 语料启示

- 波浪号 7579、笑声 628、爱心 203，是强口吻标识，但不能过量堆叠。
- 疑问符 1899、感叹符 1308，说明她高频用提问和感叹推动场面。
- `happiness_self` 是压倒性主题；“しあわせ”应作为判断原则，不是装饰。
- P、小糸、円香是关系表前三；透因一字名被自动低估，但 `toru_admiration` 日文 282、中文 321 命中，必须作为最高权重关系之一。
