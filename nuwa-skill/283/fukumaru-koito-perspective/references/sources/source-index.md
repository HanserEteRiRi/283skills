# 福丸小糸蒸馏来源索引

调研日期：2026-05-16

本目录记录用于蒸馏 `fukumaru-koito-perspective` 的资料来源。本次蒸馏以用户提供的本地剧情 CSV 为主，官方资料用于校准身份、单位结构、动画二期定位和公开设定。资料站只用于目录与交叉确认，不覆盖官方事实。

## 本地同人语料（主来源）

- 本地故事 CSV：`SCTranslationData/data/story`
- 分析脚本：`scripts/analyze_story_dialogues.py`
- 角色 profile：`config/story-dialogue-profiles/fukumaru-koito.json`
- 主题配置：`config/story-dialogue-themes/fukumaru-koito.json`
- 口癖配置：`config/story-dialogue-voice/fukumaru-koito.json`
- 输出报告：`283/fukumaru-koito-perspective/references/local-dialogue-analysis/小糸-dialogue-report.md`
- 结构化 JSON：`283/fukumaru-koito-perspective/references/local-dialogue-analysis/小糸-dialogue-analysis.json`
- 中日合并台词：`283/fukumaru-koito-perspective/references/local-dialogue-analysis/小糸-target-lines.csv`
- 日文原文台词：`283/fukumaru-koito-perspective/references/local-dialogue-analysis/小糸-target-lines-jp.csv`
- 中文翻译台词：`283/fukumaru-koito-perspective/references/local-dialogue-analysis/小糸-target-lines-cn.csv`

语料统计：5602 个 CSV、253362 行对话、小糸台词 6364 行、出现场景 365 个、他人提及小糸 983 行。用户提供的本地语料用于口吻、关系、行为模式和二创剧情记忆，不自动等同官方 canon。

## 官方/一手来源

- 一手：官方 enza 角色页，校准小糸基础设定、内弁慶な小動物系、认真努力、学习好、容易被骗、被幼驯染逗弄和高中1年级。  
  https://shinycolors.idolmaster-official.jp/idol/noctchill/koito/
- 一手：官方 Noctchill 单位页，校准 Noctchill 是幼驯染四人组成、透明感、无需成为他人的单位主题。  
  https://shinycolors.idolmaster-official.jp/idol/noctchill/
- 一手：アイドルマスター OFFICIAL WEB アイドル名鑑，校准年龄、身高、生日、血型、出身、趣味等基础资料。  
  https://idollist.idolmaster-official.jp/detail/50019
- 一手：Song for Prism 官方 IDOL 页，校准シャニソン侧描述：认真努力、学习热心、内向、和不熟的人说话稍微困难。  
  https://shinycolors-song-for-prism.idolmaster-official.jp/idol/
- 一手：动画二期角色页，校准动画侧人物描述：一直拼命努力、认真努力、内向、强烈想跟上三人。  
  https://shinycolors-anime2nd.idolmaster-official.jp/character/koito/
- 一手：动画二期第5话页面，校准 Noctchill 出道前关系：四人是幼驯染，小糸努力练舞，円香守望，雛菜闯入，透看天空。  
  https://shinycolors-anime2nd.idolmaster-official.jp/story/story-5/
- 一手：动画二期第6话页面，校准 Noctchill 在节目事故后被 P 告知事情，进入“ほんとの気持ち”相关剧情。  
  https://shinycolors-anime2nd.idolmaster-official.jp/story/story-6/

## 资料整理/二手来源

- 二手：Shinycolors Wiki - Koito Fukumaru，交叉确认基础资料、个人 commu、歌曲与卡面目录。  
  https://shinycolors.wiki/wiki/Koito_Fukumaru
- 二手：Shinycolors Wiki - Noctchill，交叉确认成员、单位描述、歌曲目录。  
  https://shinycolors.wiki/wiki/Noctchill
- 二手：シャニマス攻略 Wiki - 福丸小糸，交叉确认卡面和剧情目录。  
  https://wikiwiki.jp/shinycolors/%E7%A6%8F%E4%B8%B8%E5%B0%8F%E7%B3%B8

## 信息边界

- 官方事实以官方/一手来源为优先。
- 本地同人剧情用于生成口吻、关系反应、剧情记忆和二创校准；需要标注“本地语料/二创推演”。
- 二手资料只作为目录和交叉确认，不单独决定角色设定。
- 若用户问最新实装、活动、卡面或现实联动，应重新检索官方渠道，不凭本 Skill 旧资料硬答。
