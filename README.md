# github-skills-weekly

> Claude Code Agent Skills 周榜｜自动统计本周新增 Star，每周自动更新

收集社区热门 Agent Skill（Claude Code 指令集），按**近 7 天新增 Star** 排序，方便发现优质新 Skill。

🔗 原版榜单来源：[NXplace Weekly Skill Leaderboard](https://www.nxplace.com/)
📡 RSS 订阅（周报更新通知）：https://rsshub.app/nxplace/weekly-skill-leaderboard

<!-- START_SKILL_TABLE -->
<!-- 榜单会由机器人自动填充在这里 -->
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
