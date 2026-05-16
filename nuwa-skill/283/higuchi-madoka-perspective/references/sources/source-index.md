# 樋口円香蒸馏来源索引

调研日期：2026-05-16

本目录记录用于蒸馏 `higuchi-madoka-perspective` 的资料来源。本次蒸馏以用户提供的本地剧情 CSV 为主，官方资料用于校准身份、Noctchill 单位结构和公开设定。

## 本地同人语料（主来源）

- 本地故事 CSV：`SCTranslationData/data/story`
- 分析脚本：`scripts/analyze_story_dialogues.py`
- 角色 profile：`config/story-dialogue-profiles/higuchi-madoka.json`
- 主题配置：`config/story-dialogue-themes/higuchi-madoka.json`
- 口癖配置：`config/story-dialogue-voice/higuchi-madoka.json`
- 输出报告：`283/higuchi-madoka-perspective/references/local-dialogue-analysis/円香-dialogue-report.md`
- 结构化 JSON：`283/higuchi-madoka-perspective/references/local-dialogue-analysis/円香-dialogue-analysis.json`
- 中日合并台词：`283/higuchi-madoka-perspective/references/local-dialogue-analysis/円香-target-lines.csv`

语料统计：5602 个 CSV、253362 行对话、円香台词 5442 行、出现场景 369 个、他人提及円香 798 行。用户提供的本地语料用于口吻、关系、行为模式和二创剧情记忆，不自动等同官方 canon。

## 官方/一手来源

- 一手：官方 enza 角色页，校准樋口円香的基础设定：Noctchill 成员，17岁，高中2年级，东京都出身，冷静/讽刺，对 P 态度冷淡。  
  https://shinycolors.idolmaster-official.jp/idol/noctchill/madoka/
- 一手：官方 Noctchill 单位页，校准 Noctchill 是幼驯染四人单位，“不需要成为谁”的单位主题。  
  https://shinycolors.idolmaster-official.jp/idol/noctchill/
- 一手：アイドルマスター OFFICIAL WEB アイドル名鑑，校准年龄、身高、生日、血型等基础资料。  
  https://idollist.idolmaster-official.jp/detail/50018
- 一手：Song for Prism 官方 IDOL 页，校准シャニソン侧描述：冷静、讽刺，高中2年级，对幼驯染会有更随意的一面。  
  https://shinycolors-song-for-prism.idolmaster-official.jp/idol/

## 信息边界

- 官方事实以官方/一手来源为优先。
- 本地同人剧情用于生成口吻、关系反应、剧情记忆和二创校准；需要标注“本地语料/二创推演”。
- 资料没有记录时，不要让円香凭大模型常识硬答。
- 若用户问最新实装、活动、卡面或现实联动，应重新检索官方渠道。
