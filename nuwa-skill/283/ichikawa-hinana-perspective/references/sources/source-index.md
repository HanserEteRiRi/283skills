# 市川雛菜蒸馏来源索引

调研日期：2026-05-16

本目录记录用于蒸馏 `ichikawa-hinana-perspective` 的资料来源。本次蒸馏以用户提供的本地剧情 CSV 为主，官方资料用于校准身份、Noctchill 单位结构和公开设定。

## 本地同人语料（主来源）

- 本地故事 CSV：`SCTranslationData/data/story`
- 分析脚本：`scripts/analyze_story_dialogues.py`
- 角色 profile：`config/story-dialogue-profiles/ichikawa-hinana.json`
- 主题配置：`config/story-dialogue-themes/ichikawa-hinana.json`
- 口癖配置：`config/story-dialogue-voice/ichikawa-hinana.json`
- 输出报告：`283/ichikawa-hinana-perspective/references/local-dialogue-analysis/雛菜-dialogue-report.md`
- 结构化 JSON：`283/ichikawa-hinana-perspective/references/local-dialogue-analysis/雛菜-dialogue-analysis.json`
- 中日合并台词：`283/ichikawa-hinana-perspective/references/local-dialogue-analysis/雛菜-target-lines.csv`

语料统计：5602 个 CSV、253362 行对话、雛菜台词 5554 行、出现场景 358 个、他人提及雛菜 861 行。用户提供的本地语料用于口吻、关系、行为模式和二创剧情记忆，不自动等同官方 canon。

## 官方/一手来源

- 一手：官方 enza 角色页，校准市川雛菜的基础设定：Noctchill 成员，15岁，高中1年级，神奈川县出身，朝自己的“しあわせ”突进，仰慕幼驯染前辈透。  
  https://shinycolors.idolmaster-official.jp/idol/noctchill/hinana/
- 一手：官方 Noctchill 单位页，校准 Noctchill 是幼驯染四人单位，“不需要成为谁”的单位主题。  
  https://shinycolors.idolmaster-official.jp/idol/noctchill/
- 一手：アイドルマスター OFFICIAL WEB アイドル名鑑，校准年龄、身高、生日、血型、出身和趣味。  
  https://idollist.idolmaster-official.jp/detail/50004
- 一手：Song for Prism 官方 IDOL 页，校准シャニソン侧描述：奔放、マイペース、重视自己的しあわせ，高中1年级，仰慕透。  
  https://shinycolors-song-for-prism.idolmaster-official.jp/idol/

## 信息边界

- 官方事实以官方/一手来源为优先。
- 本地同人剧情用于生成口吻、关系反应、剧情记忆和二创校准；需要标注“本地语料/二创推演”。
- 资料没有记录时，不要让雛菜凭大模型常识硬答。
- 若用户问最新实装、活动、卡面或现实联动，应重新检索官方渠道。
