# Story Dialogue Theme Configs

`scripts/analyze_story_dialogues.py` 是通用脚本，不再内置任何角色主题词。

每个角色/用途的主题词放在本目录的 JSON 文件中。推荐通过
`config/story-dialogue-profiles/*.json` 间接引用；临时实验时也可以用
`--theme-config` 直接传入：

```powershell
python scripts\analyze_story_dialogues.py `
  --profile-config config\story-dialogue-profiles\osaki-amana.json
```

如果 `SCTranslationData` 和 `nuwa-skill` 位于同一个父目录，`--story-root` 可以省略。其他位置可设置
`SC_TRANSLATION_STORY_ROOT` 或显式传入 `--story-root`。

JSON 结构：

```json
{
  "theme_name": {
    "jp": ["日文关键词"],
    "cn": ["中文关键词"]
  }
}
```

这样后续每蒸馏一个角色，只需要新增或修改 profile、theme、voice 三类 JSON，不需要改脚本。
