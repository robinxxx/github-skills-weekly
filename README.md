# github-skills-weekly

> Claude Code Agent Skills 周榜｜自动统计本周新增 Star，每周自动更新

收集社区热门 Agent Skill（Claude Code 指令集），按**近 7 天新增 Star** 排序，方便发现优质新 Skill。

🔗 原版榜单来源：[NXplace Weekly Skill Leaderboard](https://www.nxplace.com/)
📡 RSS 订阅（周报更新通知）：https://rsshub.app/nxplace/weekly-skill-leaderboard

<!-- START_SKILL_TABLE -->
| Rank | Repo | 本周⭐ | 总⭐ | Description |
| ---- | ---- | ----- | ---- | ----------- |
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +0 | 0 | 仓库不存在/无权限 |
| 2 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +0 | 0 | 仓库不存在/无权限 |
| 3 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +0 | 0 | 仓库不存在/无权限 |
| 4 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +0 | 0 | 仓库不存在/无权限 |
| 5 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +0 | 0 | 仓库不存在/无权限 |
| 6 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +0 | 0 | 仓库不存在/无权限 |
| 7 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +0 | 0 | 仓库不存在/无权限 |
| 8 | [blader/humanizer](https://github.com/blader/humanizer) | +0 | 0 | 仓库不存在/无权限 |

<!-- END_SKILL_TABLE -->

## 使用说明

1. 榜单统计规则：UTC 时间最近 7 天新增 Star 数量
2. 数据更新：每周一 14:00（北京时间）自动刷新，也可以在 Actions 手动触发
3. 新增仓库：修改 `scripts/fetch_skills.py` 里的 `REPOS` 列表
4. 本仓库仅做热度汇总，Skill 使用方法请跳转对应原仓库查看

## 本地运行

```bash
pip install requests
python scripts/fetch_skills.py
```

## 仓库权限配置

需要在仓库 Secrets 添加 `GH_TOKEN`，权限勾选 `public_repo`：

```
Settings → Secrets and variables → Actions → New repository secret
```

| Name | Secret |
| ---- | ------ |
| GH_TOKEN | 你的 GitHub Personal Access Token（勾选 public_repo） |
