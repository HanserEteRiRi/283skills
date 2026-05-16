# Story Dialogue Voice Metric Configs

这些 JSON 文件记录角色相关的口癖、自称和可复用语言统计项。`scripts/analyze_story_dialogues.py`
只负责读取配置并统计，不在代码里保存具体角色的数据。

Schema:

```json
{
  "jp": {
    "metric_name": "regular expression"
  },
  "cn": {
    "metric_name": "regular expression"
  }
}
```

常用指标名：

- `ssu_count`: 日文 `っす` 等口癖。
- `laugh_count`: 笑声。
- `again_count`: “再来一次/もう一回”类重复请求。
- `unknown_count`: 不知道、不明白类表达。
- `first_person_count`: 自称与第一人称。这个必须按角色单独配置。
