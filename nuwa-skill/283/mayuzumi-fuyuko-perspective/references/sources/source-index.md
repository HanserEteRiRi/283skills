# 黛冬優子蒸馏来源索引

调研日期：2026-05-16

本目录记录用于蒸馏 `mayuzumi-fuyuko-perspective` 的资料来源。本次蒸馏以用户提供的本地剧情 CSV 为主，官方资料用于校准身份、单位结构、动画二期定位和公开设定。资料站只用于目录与交叉确认，不覆盖官方事实。

## 本地同人语料（主来源）

- 本地故事 CSV：`SCTranslationData/data/story`
- 分析脚本：`scripts/analyze_story_dialogues.py`
- 角色 profile：`config/story-dialogue-profiles/mayuzumi-fuyuko.json`
- 主题配置：`config/story-dialogue-themes/mayuzumi-fuyuko.json`
- 口癖配置：`config/story-dialogue-voice/mayuzumi-fuyuko.json`
- 输出报告：`283/mayuzumi-fuyuko-perspective/references/local-dialogue-analysis/冬優子-dialogue-report.md`
- 结构化 JSON：`283/mayuzumi-fuyuko-perspective/references/local-dialogue-analysis/冬優子-dialogue-analysis.json`
- 中日合并台词：`283/mayuzumi-fuyuko-perspective/references/local-dialogue-analysis/冬優子-target-lines.csv`
- 日文原文台词：`283/mayuzumi-fuyuko-perspective/references/local-dialogue-analysis/冬優子-target-lines-jp.csv`
- 中文翻译台词：`283/mayuzumi-fuyuko-perspective/references/local-dialogue-analysis/冬優子-target-lines-cn.csv`

语料统计：5603 个 CSV、253411 行对话、冬優子台词 7721 行、出现场景 402 个、他人提及冬優子 1485 行。用户提供的本地语料用于口吻、关系、行为模式和二创剧情记忆，不自动等同官方 canon。

## 官方/一手来源

- 一手：官方 enza 角色页，校准冬優子的基础设定、专门学校一年级、清楚/気配り/被喜欢地行动、以及公开视觉文案中的双层表演。  
  https://shinycolors.idolmaster-official.jp/idol/straylight/fuyuko/
- 一手：官方 Straylight 单位页，校准 Straylight 的“偶像/アバター/真実か狂気か”单位主题和成员结构。  
  https://shinycolors.idolmaster-official.jp/idol/straylight/
- 一手：アイドルマスター OFFICIAL WEB アイドル名鑑，校准年龄、身高、生日、血型、出身、趣味等基础资料。  
  https://idollist.idolmaster-official.jp/detail/50020
- 一手：Song for Prism 官方 IDOL 页，校准シャニソン侧描述：被爱地行动、上升志向强、重视结果的ストイック一面。  
  https://shinycolors-song-for-prism.idolmaster-official.jp/idol/
- 一手：动画二期角色页，校准动画侧人物描述：温柔笑容、清楚氛围、目标是世界第一可爱的偶像。  
  https://shinycolors-anime2nd.idolmaster-official.jp/character/fuyuko/
- 一手：动画二期第2话页面，校准 Straylight 出道前故事：冬優子的“计算出偶像”和あさひ的“不在意被怎么看”的对照。  
  https://shinycolors-anime2nd.idolmaster-official.jp/story/story-2/

## 资料整理/二手来源

- 二手：Shinycolors Wiki - Fuyuko Mayuzumi，交叉确认基础资料、W.I.N.G. 轮廓、个人卡和歌曲目录。  
  https://shinycolors.wiki/wiki/Fuyuko_Mayuzumi
- 二手：Shinycolors Wiki - Straylight，交叉确认成员、单位描述、歌曲目录。  
  https://shinycolors.wiki/wiki/Straylight
- 二手：シャニマス攻略 Wiki - 黛冬優子，交叉确认卡面和剧情目录。  
  https://wikiwiki.jp/shinycolors/%E9%BB%9B%E5%86%AC%E5%84%AA%E5%AD%90

## 信息边界

- 官方事实以官方/一手来源为优先。
- 本地同人剧情用于生成口吻、关系反应、剧情记忆和二创校准；需要标注“本地语料/二创推演”。
- 二手资料只作为目录和交叉确认，不单独决定角色设定。
- 若用户问最新实装、活动、卡面或现实联动，应重新检索官方渠道，不凭本 Skill 旧资料硬答。
