# Story Dialogue Character Profiles

这些 profile 用来把角色数据从 `scripts/analyze_story_dialogues.py` 中分离出来。新增角色时，
优先新增一个 profile、一个 theme config、一个 voice config，而不是改 Python 代码。

Schema:

```json
{
  "target": "角色显示名",
  "aliases": ["用于说话人/文本提及匹配的别名"],
  "story_root": "../../SCTranslationData/data/story 可选；通常省略，让脚本自动发现",
  "theme_config": "../story-dialogue-themes/example.json",
  "voice_config": "../story-dialogue-voice/example.json",
  "output_dir": "../../283/example-perspective/references/local-dialogue-analysis"
}
```

运行示例：

```powershell
python scripts\analyze_story_dialogues.py `
  --profile-config config\story-dialogue-profiles\osaki-tenka.json
```

路径规则：

- 推荐把 `SCTranslationData` 和 `nuwa-skill` 放在同一个父目录下；脚本会自动读取 `../SCTranslationData/data/story`。
- 若目录结构不同，传入 `--story-root`，或设置环境变量 `SC_TRANSLATION_STORY_ROOT`。
- 不要在角色 profile 中写死个人电脑上的绝对路径，除非只是临时调试。
