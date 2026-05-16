# 大崎甘奈 Perspective Skill

这是基于 `nuwa-skill` 方法论蒸馏出的《アイドルマスター シャイニーカラーズ》角色大崎甘奈视角 Skill。

本版本以用户提供的本地同人剧情 CSV 为主语料，并结合官方角色/单位/动画资料校准背景。

```text
283/osaki-amana-perspective/
├── SKILL.md
└── references/
    ├── local-dialogue-analysis/
    │   ├── 甘奈-dialogue-analysis.json
    │   ├── 甘奈-dialogue-report.md
    │   ├── 甘奈-target-lines.csv
    │   ├── 甘奈-target-lines-jp.csv
    │   └── 甘奈-target-lines-cn.csv
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

- 日常角色使用：只给 `SKILL.md`。
- 精修或查证：加 `references/research/*.md`。
- 口吻调试：加 `references/local-dialogue-analysis/甘奈-dialogue-report.md`。

复用脚本：

```powershell
python scripts\analyze_story_dialogues.py `
  --story-root C:\project\SCTranslationData\data\story `
  --target 甘奈 `
  --aliases 大崎甘奈 "大崎 甘奈" Amana "Osaki Amana" `
  --output-dir 283\osaki-amana-perspective\references\local-dialogue-analysis
```
