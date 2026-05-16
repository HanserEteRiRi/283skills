# 芹沢あさひ Perspective Skill

这是基于 `nuwa-skill` 方法论蒸馏出的《アイドルマスター シャイニーカラーズ》角色芹沢あさひ视角 Skill。

目录结构：

```text
283/serizawa-asahi-perspective/
├── serizawa-asahi_SKILL.md
└── references/
    ├── local-dialogue-analysis/
    │   ├── あさひ-dialogue-analysis.json
    │   ├── あさひ-dialogue-report.md
    │   └── あさひ-target-lines.csv
    ├── sources/source-index.md
    └── research/
        ├── 01-writings.md
        ├── 02-conversations.md
        ├── 03-expression-dna.md
        ├── 04-external-views.md
        ├── 05-decisions.md
        ├── 06-timeline.md
        └── 07-local-dialogue-corpus.md
```

使用方式：

- 将本目录复制到 Claude/Codex 的 skills 目录，或直接把 `serizawa-asahi_SKILL.md` 作为角色视角指令使用。
- 触发语示例：
  - `用芹沢あさひ的视角想想这个问题`
  - `切换到あさひ`
  - `あさひ会怎么看这个偶像企划`

版权边界：

- 本 Skill 不包含完整游戏脚本、动画字幕或歌词。
- 所有剧情内容均为摘要和分析。
- 角色与作品版权归 Bandai Namco Entertainment Inc. 等权利方所有。

## 复用脚本

后续蒸馏其他角色可以复用根目录脚本：

```powershell
python scripts\analyze_story_dialogues.py `
  --story-root C:\project\SCTranslationData\data\story `
  --target 冬優子 `
  --aliases 黛冬優子 "黛 冬優子" 冬优子 `
  --output-dir 283\mayuzumi-fuyuko-perspective\references\local-dialogue-analysis
```
