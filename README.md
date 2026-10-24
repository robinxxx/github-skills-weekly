# github-skills-weekly

> Claude Code Agent Skills 周榜｜自动统计本周新增 Star，每周自动更新

收集社区热门 Agent Skill（Claude Code 指令集），按**近 7 天新增 Star** 排序，方便发现优质新 Skill。

🔗 原版榜单来源：[NXplace Weekly Skill Leaderboard](https://www.nxplace.com/)
📡 RSS 订阅（周报更新通知）：https://rsshub.app/nxplace/weekly-skill-leaderboard

<!-- START_SKILL_TABLE -->
| Rank | Repo | 本周⭐ | 总⭐ | Description |
| ---- | ---- | ----- | ---- | ----------- |
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +0 | 301872 | Skills for Real Engineers. Straight from my .agents directory. |
| 2 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +0 | 49108 | Skills for Designers and Engineers. |
| 3 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +0 | 22780 | Give your agent CAD superpowers. |
| 4 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +0 | 19898 | Universal SEO skill for Claude Code. 26 sub-skills + 19 sub-agents covering technical SEO, E-E-A-T, schema, GEO/AEO, agent readiness (Lighthouse Agentic Browsing, WebMCP, llms.txt), backlinks, local SEO, e-commerce, international SEO, Google APIs, and PDF/Excel reporting. 9 optional extensions for live SEO data. |
| 5 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +0 | 60395 | Editorial diagram design for Claude Code, Codex, GitHub Copilot, Cursor, Factory Droid, Qoder, and Pi. 45 diagram types. Self-contained HTML + SVG. No shadows. No Mermaid slop. |
| 6 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +0 | 114651 | 🪨 why use many token when few token do trick. Viral skill + proxy for coding agents that cuts 65% of tokens by talking like a caveman. |
| 7 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +0 | 88335 | Turn any idea, plan, or codebase into a beautiful interactive diagram. An agent skill for Claude Code, Codex, and more. |
| 8 | [blader/humanizer](https://github.com/blader/humanizer) | +0 | 60022 | Agent skill that removes signs of AI-generated writing from text |

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

## 权限说明

- **默认无需配置任何 Secret**：Workflow 自动使用仓库内置的 `GITHUB_TOKEN`，足够读取公开仓库数据。
- 可选：如需监控**私有仓库**或提高 API 配额，可配置自定义 `GH_TOKEN` Secret：

```
Settings → Secrets and variables → Actions → New repository secret
```

| Name | Secret |
| ---- | ------ |
| GH_TOKEN | 你的 GitHub Personal Access Token（勾选 repo 权限） |
