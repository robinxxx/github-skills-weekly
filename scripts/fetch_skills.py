# -*- coding: utf-8 -*-
"""github-skills-weekly 周榜抓取脚本。

按"相邻两次运行的总 Star 增量"排序（快照法）：
- 当前环境的 GitHub API 不返回 star 事件时间序列（stargazers 列表不可用），
  故无法实时统计"近 7 天新增 Star"；
- 改为保存每次运行的总 Star 快照（data/stars.json），
  本周新增 = 本次总 Star - 上次快照总 Star，首次运行建立基线显示 "-"。

用法: GH_TOKEN=<token> python scripts/fetch_skills.py
"""

import json
import os
import sys
from datetime import datetime, timezone

import requests

GH_TOKEN = os.getenv("GH_TOKEN")
HEADERS = {"Authorization": f"Bearer {GH_TOKEN}"} if GH_TOKEN else {}
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAPSHOT_PATH = os.path.join(BASE_DIR, "data", "stars.json")

# ========= 在这里添加/删除要监控的 Skill 仓库 =========
REPOS = [
    "mattpocock/skills",
    "emilkowalski/skills",
    "earthtojake/text-to-cad",
    "AgriciDaniel/claude-seo",
    "cathrynlavery/diagram-design",
    "JuliusBrussee/caveman",
    "tt-a1i/archify",
    "blader/humanizer",
]
# =====================================================

GRAPHQL_QUERY = """
query($owner: String!, $name: String!) {
  repository(owner: $owner, name: $name) {
    stargazerCount
    nameWithOwner
    description
  }
}
"""


def load_snapshot():
    if os.path.exists(SNAPSHOT_PATH):
        try:
            with open(SNAPSHOT_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def save_snapshot(snapshot):
    os.makedirs(os.path.dirname(SNAPSHOT_PATH), exist_ok=True)
    with open(SNAPSHOT_PATH, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, ensure_ascii=False, indent=2)


def fetch_repo(repo_full):
    owner, name = repo_full.split("/")
    resp = requests.post(
        "https://api.github.com/graphql",
        json={"query": GRAPHQL_QUERY, "variables": {"owner": owner, "name": name}},
        headers=HEADERS,
        timeout=30,
    )
    if resp.status_code == 401:
        sys.exit("❌ GH_TOKEN 无效或未设置，请检查仓库 Secrets")
    data = resp.json()
    repo = data.get("data", {}).get("repository")
    if repo is None:
        return {"repo": repo_full, "total": 0, "desc": "仓库不存在/无权限"}
    return {
        "repo": repo["nameWithOwner"],
        "total": repo["stargazerCount"],
        "desc": repo["description"] or "-",
    }


def main():
    snapshot = load_snapshot()
    now = datetime.now(timezone.utc).isoformat()

    result_list = []
    new_snapshot = {}
    for repo in REPOS:
        print(f"🔍 fetching {repo} ...")
        item = fetch_repo(repo)
        prev = snapshot.get(item["repo"], {}).get("total")
        if prev is None:
            gain = None  # 首次运行，建立基线
        else:
            gain = max(0, item["total"] - prev)
        new_snapshot[item["repo"]] = {"total": item["total"], "ts": now}
        item["gain"] = gain
        result_list.append(item)

    save_snapshot(new_snapshot)

    # 排序：有增量的优先按增量降序，其余按总 star 降序
    result_list.sort(
        key=lambda x: (x["gain"] if x["gain"] is not None else -1, x["total"]),
        reverse=True,
    )

    md_table = "| Rank | Repo | 本周⭐ | 总⭐ | Description |\n"
    md_table += "| ---- | ---- | ----- | ---- | ----------- |\n"
    for idx, row in enumerate(result_list, start=1):
        link = f"https://github.com/{row['repo']}"
        gain_str = f"+{row['gain']}" if row["gain"] is not None else "-"
        safe_desc = row["desc"].replace("|", " ")
        md_table += (
            f"| {idx} | [{row['repo']}]({link}) | {gain_str} "
            f"| {row['total']} | {safe_desc} |\n"
        )

    readme_path = os.path.join(BASE_DIR, "README.md")
    with open(readme_path, "r", encoding="utf-8") as f:
        readme_content = f.read()
    start_tag = "<!-- START_SKILL_TABLE -->"
    end_tag = "<!-- END_SKILL_TABLE -->"
    if start_tag not in readme_content or end_tag not in readme_content:
        sys.exit("❌ README.md 中缺少榜单标记，请检查文件")

    left_part = readme_content.split(start_tag)[0]
    right_part = readme_content.split(end_tag)[1]
    new_readme = f"{left_part}{start_tag}\n{md_table}\n{end_tag}{right_part}"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_readme)
    print("✅ README 榜单更新完成！")


if __name__ == "__main__":
    main()
