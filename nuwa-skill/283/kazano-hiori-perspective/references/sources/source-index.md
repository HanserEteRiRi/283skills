# 風野灯織蒸馏来源索引

调研日期：2026-05-16

本目录记录用于蒸馏 `kazano-hiori-perspective` 的资料来源。本次蒸馏以用户提供的本地剧情 CSV 为主，官方资料用于校准身份、单位结构和公开设定。资料站或模型记忆不得覆盖官方事实。

## 本地同人语料（主来源）

- 本地故事 CSV：`SCTranslationData/data/story`
- 分析脚本：`scripts/analyze_story_dialogues.py`
- 角色 profile：`config/story-dialogue-profiles/kazano-hiori.json`
- 主题配置：`config/story-dialogue-themes/kazano-hiori.json`
- 口癖配置：`config/story-dialogue-voice/kazano-hiori.json`
- 输出报告：`283/kazano-hiori-perspective/references/local-dialogue-analysis/灯織-dialogue-report.md`
- 结构化 JSON：`283/kazano-hiori-perspective/references/local-dialogue-analysis/灯織-dialogue-analysis.json`
- 中日合并台词：`283/kazano-hiori-perspective/references/local-dialogue-analysis/灯織-target-lines.csv`
- 日文原文台词：`283/kazano-hiori-perspective/references/local-dialogue-analysis/灯織-target-lines-jp.csv`
- 中文翻译台词：`283/kazano-hiori-perspective/references/local-dialogue-analysis/灯織-target-lines-cn.csv`

语料统计：5602 个 CSV、253362 行对话、灯織台词 8816 行、出现场景 452 个、他人提及灯織 1846 行。用户提供的本地语料用于口吻、关系、行为模式和二创剧情记忆，不自动等同官方 canon。

## 官方/一手来源

- 一手：官方 enza 角色页，校准風野灯織的基础设定、15岁、高中1年级、东京都出身、黑发、酷系、努力到自己认可为止的ストイック性格。  
  https://shinycolors.idolmaster-official.jp/idol/illuminationstars/hiori/
- 一手：官方 illumination STARS 单位页，校准三人单位成员和互相碰撞、互相支撑、一等星目标的单位意象。  
  https://shinycolors.idolmaster-official.jp/idol/illuminationstars/
- 一手：アイドルマスター OFFICIAL WEB アイドル名鑑，校准年龄、身高、生日、血型、出身、趣味等基础资料。  
  https://idollist.idolmaster-official.jp/detail/50007

## 信息边界

- 官方事实以官方/一手来源为优先。
- 本地同人剧情用于生成口吻、关系反应、剧情记忆和二创校准；需要标注“本地语料/二创推演”。
- 若用户问最新实装、活动、卡面或现实联动，应重新检索官方渠道，不凭本 Skill 旧资料硬答。
- 不能替真乃、めぐる或 P 的内心下结论；只能引用本地语料中可观察的台词、共现和互动。
