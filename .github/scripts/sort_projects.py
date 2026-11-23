#!/usr/bin/env python3
"""
Automatically sorts the featured projects table in README.md by GitHub stars (descending).
"""

import os
import re
import json
import urllib.request

README_PATH = "README.md"
START_MARKER = "<!-- PROJECTS:START -->"
END_MARKER = "<!-- PROJECTS:END -->"

def get_stars(repo: str, token: str | None = None) -> int:
    url = f"https://api.github.com/repos/{repo}"
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "GitHub-Profile-AutoSorter",
            "Accept": "application/vnd.github.v3+json",
        }
    )
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("stargazers_count", 0)
    except Exception as e:
        print(f"[!] Warning: could not fetch stars for {repo}: {e}")
        return 0

def main():
    if not os.path.exists(README_PATH):
        print(f"Error: {README_PATH} not found.")
        return

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(
        rf"({re.escape(START_MARKER)}\s*\n)(.*?)(\n\s*{re.escape(END_MARKER)})",
        re.DOTALL
    )
    match = pattern.search(content)
    if not match:
        print(f"Markers {START_MARKER} and {END_MARKER} not found in {README_PATH}.")
        return

    pre_marker = match.group(1)
    table_block = match.group(2).strip().splitlines()
    post_marker = match.group(3)

    if len(table_block) < 3:
        print("Table does not have enough lines to parse.")
        return

    header = table_block[0]
    separator = table_block[1]
    rows = [r.strip() for r in table_block[2:] if r.strip().startswith("|")]

    token = os.environ.get("GITHUB_TOKEN")

    project_data = []
    for idx, row in enumerate(rows):
        m = re.search(r"https://github\.com/([a-zA-Z0-9_-]+/[a-zA-Z0-9_.-]+)", row)
        if m:
            repo = m.group(1)
            stars = get_stars(repo, token)
            print(f"-> {repo}: {stars} stars")
            # idx is used as secondary key to preserve stable order when stars are equal
            project_data.append((stars, idx, row))
        else:
            project_data.append((0, idx, row))

    # Sort descending by stars (higher stars first)
    project_data.sort(key=lambda x: (x[0], -x[1]), reverse=True)
    sorted_rows = [p[2] for p in project_data]

    new_table_content = f"{header}\n{separator}\n" + "\n".join(sorted_rows)
    new_full_content = (
        content[:match.start()]
        + pre_marker
        + new_table_content
        + post_marker
        + content[match.end():]
    )

    if new_full_content != content:
        with open(README_PATH, "w", encoding="utf-8", newline="\n") as f:
            f.write(new_full_content)
        print("README.md successfully updated with projects sorted by stars.")
    else:
        print("No changes needed. Projects are already correctly sorted by stars.")

if __name__ == "__main__":
    main()
