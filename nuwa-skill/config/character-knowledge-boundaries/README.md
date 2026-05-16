# 角色知识边界配置

这些 JSON 文件用于 `scripts/build_character_knowledge_pack.py`，把“角色知道什么/不知道什么/必须拒答什么”从生成脚本中分离出来。

核心字段：

- `display_name`：角色显示名。
- `age_stage`：年龄与成长阶段，用于限制知识范围。
- `education_or_role`：学历、职业、身份。
- `affiliation`：所属组合/组织。
- `allowed_scope`：角色可以直接回答的范围。
- `cautious_scope`：角色可以用不确定语气回答的范围。
- `refuse_scope`：必须承认不知道或拒答的范围。
- `refusal_cn` / `refusal_jp`：越界时的中日角色口吻。
- `plot_memory`：角色需要记得的关键剧情节点，来源可以指向 `SKILL.md`、`references/research/*` 或本地语料报告。
