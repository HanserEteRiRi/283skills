# 浅倉透蒸馏来源索引

调研日期：2026-05-16

本目录记录用于蒸馏 `浅倉透 perspective` 的资料来源。本次蒸馏以用户提供的本地同人剧情 CSV 为主要参考，官方资料用于校准身份、基础设定、Noctchill 结构与动画二期定位。

## 本地同人语料（主来源）

- 本地故事 CSV：`C:\project\SCTranslationData\data\story`
- 分析脚本：`scripts/analyze_story_dialogues.py`
- 角色 profile：`config/story-dialogue-profiles/asakura-toru.json`
- 主题配置：`config/story-dialogue-themes/asakura-toru.json`
- 口癖配置：`config/story-dialogue-voice/asakura-toru.json`
- 输出报告：`283/asakura-toru-perspective/references/local-dialogue-analysis/透-dialogue-report.md`
- 结构化 JSON：`283/asakura-toru-perspective/references/local-dialogue-analysis/透-dialogue-analysis.json`
- 中日合并台词：`283/asakura-toru-perspective/references/local-dialogue-analysis/透-target-lines.csv`
- 日文原文台词：`283/asakura-toru-perspective/references/local-dialogue-analysis/透-target-lines-jp.csv`
- 中文翻译台词：`283/asakura-toru-perspective/references/local-dialogue-analysis/透-target-lines-cn.csv`

语料统计：5603 个 CSV、253411 行对话、透台词 6341 行、出现场景 373 个、他人提及透 132 行。用户说明这些对话为同人剧情，可作为蒸馏主语料。

## 官方/一手来源

- 一手：官方 enza 角色页，浅倉透基础设定、CV、年龄、出身地、自然体、マイペース、透明感和吸引力。  
  https://shinycolors.idolmaster-official.jp/idol/noctchill/toru/
- 一手：官方 Noctchill 单位页，幼驯染四人组、透明感、无需成为他人的单位主题。  
  https://shinycolors.idolmaster-official.jp/idol/noctchill/
- 一手：Song for Prism 官方 IDOL 页，浅倉透的シャニソン侧描述、基础资料和 Noctchill 列表。  
  https://shinycolors-song-for-prism.idolmaster-official.jp/idol/
- 一手：动画二期角色页，透的动画侧基础设定，并确认她是幼馴染4人組的中心。  
  https://shinycolors-anime2nd.idolmaster-official.jp/character/toru/
- 一手：动画二期第5话、第6话、第11话页面，用于校准动画二期中 Noctchill 的登场节点和标题语义。  
  https://shinycolors-anime2nd.idolmaster-official.jp/story/story-5/  
  https://shinycolors-anime2nd.idolmaster-official.jp/story/story-6/  
  https://shinycolors-anime2nd.idolmaster-official.jp/story/story-11/

## 资料整理/剧情目录

- 二手：Shinycolors Wiki - Toru Asakura/Commus，Morning / Audition / W.I.N.G. / Fan Festival / G.R.A.D. / Landing Point 目录。  
  https://shinycolors.wiki/wiki/Toru_Asakura/Commus
- 二手：シャニマス攻略 Wiki - 浅倉透，基础资料、趣味、特技、卡面列表、实装日期整理。  
  https://wikiwiki.jp/shinycolors/%E6%B5%85%E5%80%89%E9%80%8F
- 二手：Fandom - Toru Asakura，英文资料站对公交站、攀登架记忆、P 不认出透等剧情的整理。  
  https://shinycolors.fandom.com/wiki/Toru_Asakura

## 信息边界

- 本地同人剧情用于口吻、关系、行为模式蒸馏，不用于声明官方 canon。
- 官方资料用于身份、单位主题、公开设定和动画侧基础事实校准。
- 透在动画二期登场，但本地 CSV 仍是本 Skill 的主蒸馏语料。
- 若用户问官方剧情事实，应优先区分“官方设定/游戏剧情目录/动画页面”与“本地同人语料推断”。
