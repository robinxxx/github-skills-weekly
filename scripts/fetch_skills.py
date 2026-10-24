# -*- coding: utf-8 -*-
"""github-skills-weekly 周榜抓取脚本。

按近 7 天新增 Star 排序，自动更新 README.md 榜单区域。
用法: GH_TOKEN=<token> python scripts/fetch_skills.py
"""

import os
import sys
from datetime import datetime, timedelta

import requests

GH_TOKEN = os.getenv("GH_TOKEN")
HEADERS = {"Authorization": f"Bearer {GH_TOKEN}"} if GH_TOKEN else {}
ONE_WEEK_AGO = (datetime.utcnow() - timedelta(days=7)).isoformat() + "Z"

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
query($owner: String!, $name: String!, $after: String) {
  repository(owner: $owner, name: $name) {
    stargazerCount
    nameWithOwner
    description
    stargazers(first: 100, after: $after, orderBy: {field: STARRED_AT, direction: DESC}) {
      edges {
        starredAt
      }
      pageInfo {
        endCursor
        hasNextPage
      }
    }
  }
}
"""


def get_week_star_gain(repo_full: str):
    owner, name = repo_full.split("/")
    gain = 0
    after = None
    total_stars = 0
    desc = "-"

    while True:
        resp = requests.post(
            "https://api.github.com/graphql",
            json={
                "query": GRAPHQL_QUERY,
                "variables": {"owner": owner, "name": name, "after": after},
            },
            headers=HEADERS,
            timeout=30,
        )
        if resp.status_code == 401:
            sys.exit("❌ GH_TOKEN 无效或未设置，请检查仓库 Secrets")
        data = resp.json()
        repo = data.get("data", {}).get("repository")
        if repo is None:
            return {"repo": repo_full, "gain": 0, "total": 0, "desc": "仓库不存在/无权限"}

        total_stars = repo["stargazerCount"]
        desc = repo["description"] or "-"
        edges = repo["stargazers"]["edges"]
        page_info = repo["stargazers"]["pageInfo"]

        # starredAt 按时间降序返回：遇到第一个早于一周的即可停止
        stop = False
        for e in edges:
            if e["starredAt"] >= ONE_WEEK_AGO:
                gain += 1
            else:
                stop = True
                break

        if stop or not page_info["hasNextPage"]:
            break
        after = page_info["endCursor"]

    return {
        "repo": repo["nameWithOwner"],
        "gain": gain,
        "total": total_stars,
        "desc": desc,
    }


def main():
    result_list = []
    for repo in REPOS:
        print(f"🔍 fetching {repo} ...")
        result_list.append(get_week_star_gain(repo))

    # 按本周新增 star 降序
    result_list.sort(key=lambda x: x["gain"], reverse=True)

    md_table = "| Rank | Repo | 本周⭐ | 总⭐ | Description |\n"
    md_table += "| ---- | ---- | ----- | ---- | ----------- |\n"
    for idx, row in enumerate(result_list, start=1):
        link = f"https://github.com/{row['repo']}"
        safe_desc = row["desc"].replace("|", " ")
        md_table += (
            f"| {idx} | [{row['repo']}]({link}) | +{row['gain']} "
            f"| {row['total']} | {safe_desc} |\n"
        )

    with open("README.md", "r", encoding="utf-8") as f:
        readme_content = f.read()
    start_tag = "<!-- START_SKILL_TABLE -->"
    end_tag = "<!-- END_SKILL_TABLE -->"
    if start_tag not in readme_content or end_tag not in readme_content:
        sys.exit("❌ README.md 中缺少榜单标记，请检查文件")

    left_part = readme_content.split(start_tag)[0]
    right_part = readme_content.split(end_tag)[1]
    new_readme = f"{left_part}{start_tag}\n{md_table}\n{end_tag}{right_part}"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_readme)
    print("✅ README 榜单更新完成！")


if __name__ == "__main__":
    main()
