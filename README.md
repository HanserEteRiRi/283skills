# ShinyColors Character Distillation Workspace

这个仓库把两个项目放在同一个可迁移工作区里：

```text
shinycolors-distill-workspace/
├── SCTranslationData/   # 用户提供的剧情/翻译对话库
├── nuwa-skill/          # 女娲 skill 蒸馏项目与角色产物
├── git-history-backup/  # 旧子仓库 .git 备份，本仓库忽略
├── .gitignore
├── .gitattributes
└── README.md
```

目标：下一个对话里的 LLM 只要打开这个父目录，就能读取剧情库，继续用同一套流程蒸馏《偶像大师 闪耀色彩》的角色 skill。

## 当前状态

- 已迁移：`SCTranslationData` 与 `nuwa-skill` 已放在同一个父目录。
- 已配置：`nuwa-skill/scripts/analyze_story_dialogues.py` 会自动寻找 `../SCTranslationData/data/story`。
- 已完成角色：芹沢あさひ、大崎甘奈、大崎甜花、桑山千雪、鈴木羽那、浅倉透。
- 已加入通用机制：角色知识边界、剧情记忆包、中日分离台词分析、通用 quality check。
- 冬優子进度：已生成 profile/theme/voice/boundary 配置与本地对话分析，尚未完成最终 `SKILL.md` 写作。

## GitHub 上传步骤

在本目录执行：

```powershell
git status
git add .gitignore .gitattributes README.md SCTranslationData nuwa-skill
git status
git commit -m "Initial ShinyColors distillation workspace"
```

然后在 GitHub 新建空仓库，不要勾选初始化 README。复制远程地址后执行：

```powershell
git remote add origin https://github.com/<your-name>/<repo-name>.git
git branch -M main
git push -u origin main
```

注意：

- `git-history-backup/` 保存了迁移前两个子项目的旧 `.git`，已被 `.gitignore` 忽略，不会上传。
- 当前非备份文件未发现超过 GitHub 单文件 100MB 限制的文件。
- 如果 GitHub 提示仓库总体积太大，可以只上传 `SCTranslationData/data/story` 和 `nuwa-skill`，或改用 Git LFS。

## 路径迁移规则

推荐保持这个结构：

```text
任意父目录/
├── SCTranslationData/
│   └── data/story/
└── nuwa-skill/
    └── scripts/analyze_story_dialogues.py
```

这样运行分析时不需要写死路径：

```powershell
cd nuwa-skill
python scripts\analyze_story_dialogues.py --profile-config config\story-dialogue-profiles\serizawa-asahi.json
```

如果剧情库放在别处，可以二选一：

```powershell
$env:SC_TRANSLATION_STORY_ROOT = "D:\somewhere\SCTranslationData\data\story"
python scripts\analyze_story_dialogues.py --profile-config config\story-dialogue-profiles\serizawa-asahi.json
```

或：

```powershell
python scripts\analyze_story_dialogues.py `
  --story-root D:\somewhere\SCTranslationData\data\story `
  --profile-config config\story-dialogue-profiles\serizawa-asahi.json
```

不要把个人电脑上的绝对路径写进角色配置，除非只是临时调试。

## 新角色蒸馏流程

以下步骤在 `nuwa-skill/` 目录下执行。

### 1. 确认角色在剧情库里的 speaker 名

```powershell
rg -n "角色名|日文名|中文名" ..\SCTranslationData\data\story -g "*.csv" -m 20
```

确认 CSV 里的 `name` 列主要使用什么名字，例如冬優子主要是 `冬優子`。

### 2. 新增三个对话分析配置

在这些目录新增同名 JSON：

- `config/story-dialogue-profiles/<character>.json`
- `config/story-dialogue-themes/<character>.json`
- `config/story-dialogue-voice/<character>.json`

profile 示例：

```json
{
  "target": "冬優子",
  "aliases": ["黛冬優子", "黛 冬優子", "冬优子", "Fuyuko"],
  "mention_aliases": ["冬優子", "黛冬優子", "冬优子", "ふゆ"],
  "theme_config": "../story-dialogue-themes/mayuzumi-fuyuko.json",
  "voice_config": "../story-dialogue-voice/mayuzumi-fuyuko.json",
  "output_dir": "../../283/mayuzumi-fuyuko-perspective/references/local-dialogue-analysis"
}
```

规则：

- `target` 必须匹配 CSV speaker 的主要名字。
- `aliases` 用于 speaker 匹配。
- `mention_aliases` 用于“别人提到她”的文本匹配。
- `theme_config` 放主题关键词，必须中日分开。
- `voice_config` 放口癖/句式正则，必须中日分开。
- `output_dir` 指向该角色 skill 的本地分析目录。

### 3. 运行本地对话分析

```powershell
python scripts\analyze_story_dialogues.py `
  --profile-config config\story-dialogue-profiles\<character>.json
```

会生成：

- `*-dialogue-report.md`：人类可读报告
- `*-dialogue-analysis.json`：结构化统计
- `*-target-lines.csv`：中日合并台词
- `*-target-lines-jp.csv`：日文原文台词
- `*-target-lines-cn.csv`：中文翻译台词

优先阅读报告里的：

- 台词行数、出现场景数
- 日文/中文口癖统计
- 主题命中
- 人物关系权重
- 高频场景和关系样本

### 4. 新增知识边界配置

新增：

```text
config/character-knowledge-boundaries/<character>.json
```

必须写清楚：

- 年龄/阶段
- 学历/职业身份
- 所属组合
- 可以回答的范围
- 需要谨慎回答的范围
- 必须拒答的范围
- 中文拒答句
- 日文拒答句
- 角色应记得的剧情

生成知识包：

```powershell
python scripts\build_character_knowledge_pack.py `
  --skill-dir 283\<character>-perspective `
  --profile-config config\story-dialogue-profiles\<character>.json `
  --boundary-config config\character-knowledge-boundaries\<character>.json
```

会生成：

- `references/knowledge/knowledge-boundary.md`
- `references/knowledge/character-memory.json`

这个机制用于避免 LLM 只模仿口吻，却在角色不该知道的问题上调用通用知识硬答。

### 5. 补充官方/外部资料

必须区分：

- 官方/一手资料：角色页、单位页、动画官网、游戏内文本
- 二手资料：wiki、玩家整理、评论
- 本地同人语料：用户提供的 CSV，用于口吻、关系和二创剧情记忆，不冒充官方 canon

建议建立：

```text
283/<character>-perspective/references/
├── sources/source-index.md
├── research/01-writings.md
├── research/02-conversations.md
├── research/03-expression-dna.md
├── research/04-external-views.md
├── research/05-decisions.md
├── research/06-timeline.md
├── research/07-local-dialogue-corpus.md
├── local-dialogue-analysis/
└── knowledge/
```

### 6. 写 SKILL.md

参考已有角色，例如：

- `283/serizawa-asahi-perspective/SKILL.md`
- `283/asakura-toru-perspective/SKILL.md`

必须包含：

- YAML frontmatter：`name` 和 `description`
- 角色扮演规则
- 中文模式
- 日本語モード
- `知识边界与剧情记忆（必须优先执行）`
- 回答工作流
- 本地对话语料校准
- 身份卡
- 3 到 7 个核心心智模型
- 决策启发式
- 表达 DNA
- 人物时间线
- 人物关系模型
- 诚实边界
- 来源索引

核心要求：

- 中文和日文分开写，不要混用译腔。
- 角色不知道的问题，要用角色口吻承认不知道。
- 官方事实、本地同人语料、二创推演必须分层。
- 不要只写“像她说话”，还要写“她怎么判断、记得什么、不知道什么”。

### 7. 质量检查

```powershell
python scripts\quality_check.py 283\<character>-perspective\SKILL.md
```

必须 8/8 通过：

- 心智模型数量
- 模型局限性
- 表达 DNA 辨识度
- 知识边界
- 剧情记忆
- 诚实边界
- 内在张力
- 一手来源占比

同时建议验证配置与脚本：

```powershell
python -m json.tool config\story-dialogue-profiles\<character>.json > $null
python -m json.tool config\story-dialogue-themes\<character>.json > $null
python -m json.tool config\story-dialogue-voice\<character>.json > $null
python -m json.tool config\character-knowledge-boundaries\<character>.json > $null
python -m py_compile scripts\analyze_story_dialogues.py scripts\build_character_knowledge_pack.py scripts\quality_check.py
```

## 继续冬優子的提示

冬優子已经完成以下文件：

- `config/story-dialogue-profiles/mayuzumi-fuyuko.json`
- `config/story-dialogue-themes/mayuzumi-fuyuko.json`
- `config/story-dialogue-voice/mayuzumi-fuyuko.json`
- `config/character-knowledge-boundaries/mayuzumi-fuyuko.json`
- `283/mayuzumi-fuyuko-perspective/references/local-dialogue-analysis/冬優子-dialogue-report.md`
- `283/mayuzumi-fuyuko-perspective/references/knowledge/knowledge-boundary.md`

下一个 LLM 应从阅读冬優子的本地报告、官方角色页、Straylight 资料和动画二期第 2 话开始，然后补齐 `references/research/`、`references/sources/` 和最终 `SKILL.md`。
