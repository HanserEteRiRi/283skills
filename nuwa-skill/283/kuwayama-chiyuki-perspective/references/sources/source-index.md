# 桑山千雪蒸馏来源索引

调研日期：2026-05-16

本目录记录用于蒸馏 `桑山千雪 perspective` 的资料来源。本次蒸馏以用户提供的本地同人剧情 CSV 为主要参考，官方资料用于校准身份、基础设定、单位主题和动画剧情位置。

## 本地同人语料（主来源）

- 本地故事 CSV：`C:\project\SCTranslationData\data\story`
- 分析脚本：`scripts/analyze_story_dialogues.py`
- 角色 profile：`config/story-dialogue-profiles/kuwayama-chiyuki.json`
- 主题配置：`config/story-dialogue-themes/kuwayama-chiyuki.json`
- 口癖配置：`config/story-dialogue-voice/kuwayama-chiyuki.json`
- 输出报告：`283/kuwayama-chiyuki-perspective/references/local-dialogue-analysis/千雪-dialogue-report.md`
- 结构化 JSON：`283/kuwayama-chiyuki-perspective/references/local-dialogue-analysis/千雪-dialogue-analysis.json`
- 中日合并台词：`283/kuwayama-chiyuki-perspective/references/local-dialogue-analysis/千雪-target-lines.csv`
- 日文原文台词：`283/kuwayama-chiyuki-perspective/references/local-dialogue-analysis/千雪-target-lines-jp.csv`
- 中文翻译台词：`283/kuwayama-chiyuki-perspective/references/local-dialogue-analysis/千雪-target-lines-cn.csv`

语料统计：5603 个 CSV、253411 行对话、千雪台词 4756 行、出现场景 288 个、他人提及千雪 1079 行。用户说明这些对话为同人剧情，可作为蒸馏主语料。

## 官方/一手来源

- 一手：官方角色页，桑山千雪基础设定、温柔包容、成为偶像前的杂货店兼职与手作小物。  
  https://shinycolors.idolmaster-official.jp/idol/alstroemeria/chiyuki/
- 一手：官方 ALSTROEMERIA 单位页，三人单位主题、幸福论、未来への憧れ。  
  https://shinycolors.idolmaster-official.jp/idol/alstroemeria/
- 一手：动画角色页，千雪的温柔姐姐感与手工小物。  
  https://shinycolors-anime.idolmaster-official.jp/character/chiyuki/
- 一手：动画 1st season Story，第3话对应 ALSTROEMERIA 作为单位思考方向。  
  https://shinycolors-anime.idolmaster-official.jp/story/
- 一手：动画 2nd season 第8话，ALSTROEMERIA 的彼此体贴与千雪内心动摇。  
  https://shinycolors-anime2nd.idolmaster-official.jp/story/story-8/

## 资料整理

- 二手：Shinycolors Wiki，Chiyuki Kuwayama 基础资料、趣味、特技、卡面/歌曲列表。  
  https://shinycolors.wiki/wiki/Chiyuki_Kuwayama
- 二手：Shinycolors Wiki，Chiyuki commus 列表。  
  https://shinycolors.wiki/wiki/Chiyuki_Kuwayama/Commus

## 信息边界

- 本地同人剧情用于口吻、关系、行为模式蒸馏，不用于声明官方 canon。
- 官方资料用于身份与背景校准。
- 若用户问官方剧情事实，应优先区分“官方设定/动画剧情”与“本地同人语料推断”。
