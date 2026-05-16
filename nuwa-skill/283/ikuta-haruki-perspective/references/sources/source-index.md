# 郁田はるき蒸馏来源索引

调研日期：2026-05-16

本目录记录用于蒸馏 `ikuta-haruki-perspective` 的资料来源。本次蒸馏以用户提供的本地剧情 CSV 为主，官方资料用于校准身份、单位结构和公开设定。资料站或模型记忆不得覆盖官方事实。

## 本地同人语料（主来源）

- 本地故事 CSV：`SCTranslationData/data/story`
- 分析脚本：`scripts/analyze_story_dialogues.py`
- 角色 profile：`config/story-dialogue-profiles/ikuta-haruki.json`
- 主题配置：`config/story-dialogue-themes/ikuta-haruki.json`
- 口癖配置：`config/story-dialogue-voice/ikuta-haruki.json`
- 输出报告：`283/ikuta-haruki-perspective/references/local-dialogue-analysis/はるき-dialogue-report.md`
- 结构化 JSON：`283/ikuta-haruki-perspective/references/local-dialogue-analysis/はるき-dialogue-analysis.json`
- 中日合并台词：`283/ikuta-haruki-perspective/references/local-dialogue-analysis/はるき-target-lines.csv`
- 日文原文台词：`283/ikuta-haruki-perspective/references/local-dialogue-analysis/はるき-target-lines-jp.csv`
- 中文翻译台词：`283/ikuta-haruki-perspective/references/local-dialogue-analysis/はるき-target-lines-cn.csv`

语料统计：5602 个 CSV、253362 行对话、はるき台词 2834 行、出现场景 165 个、他人提及はるき 457 行。用户提供的本地语料用于口吻、关系、行为模式和二创剧情记忆，不自动等同官方 canon。

## 官方/一手来源

- 一手：官方 enza 角色页，校准郁田はるき的基础设定、CoMETIK 归属、17岁、高中2年级、长野县出身、热爱创作和感受力强等公开描述。  
  https://shinycolors.idolmaster-official.jp/idol/cometik/haruki/
- 一手：官方 CoMETIK 单位页，校准 CoMETIK 是斑鳩ルカ、鈴木羽那、郁田はるき三人单位，以及黑色彗星、颜色不被固定、轨迹通向闇或光的单位意象。  
  https://shinycolors.idolmaster-official.jp/idol/cometik/
- 一手：アイドルマスター OFFICIAL WEB アイドル名鑑，校准年龄、身高、生日、血型、出身、趣味等基础资料。  
  https://idollist.idolmaster-official.jp/detail/50028
- 一手：Song for Prism 官方 IDOL 页，校准シャニソン侧角色展示与 CoMETIK 归属。  
  https://shinycolors-song-for-prism.idolmaster-official.jp/idol/

## 信息边界

- 官方事实以官方/一手来源为优先。
- 本地同人剧情用于生成口吻、关系反应、剧情记忆和二创校准；需要标注“本地语料/二创推演”。
- 若用户问最新实装、活动、卡面或现实联动，应重新检索官方渠道，不凭本 Skill 旧资料硬答。
- 不能把ルカ或羽那的内心动机替她们定论；只能引用本地语料中可观察的台词、共现和互动。
