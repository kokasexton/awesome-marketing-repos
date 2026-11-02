#!/usr/bin/env python3
"""Consistency checks for README.md. Exits non-zero on any problem.

Checks:
  * every repo listed in a category section is in the Alphabetical Index, and vice versa
  * the Alphabetical Index is sorted case-insensitively by owner/repo
  * no repo is listed in more than one category section
  * the 🆕 tag appears exactly on the repos listed in "Recently Added"
  * the repo count in the badge and footer matches the real count
"""
import re
import sys
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"
text = README.read_text(encoding="utf-8")
errors = []


def section(start_marker, end_marker):
    start = text.index(start_marker)
    end = text.index(end_marker, start)
    return text[start:end]


ENTRY = re.compile(r"^- \*\*\[[^\]]+\]\(https://github\.com/([^/)]+/[^/)]+)[^)]*\)\*\*( 🆕)?", re.M)

recent_block = section("## 🆕 Recently Added", "\n---\n")
categories = section("## 🤖 AI Marketing Tools", "## 📦 Marketing Stack Templates")
index_block = section("## 🔤 Alphabetical Index", "\n---\n")

recent = {r.lower() for r, _ in ENTRY.findall(recent_block)}
entries = ENTRY.findall(categories)
listed = [r for r, _ in entries]
tagged = {r.lower() for r, new in entries if new}

# Duplicates across sections
seen = {}
for r in listed:
    seen[r.lower()] = seen.get(r.lower(), 0) + 1
for r, n in sorted(seen.items()):
    if n > 1:
        errors.append(f"{r} is listed {n} times; keep one entry and use an 'Also see:' line elsewhere")

# Index coverage and ordering
index_names = re.findall(r"^\| \[([^\]]+)\]\(", index_block, re.M)
index_set = {n.lower() for n in index_names}
for r in sorted(set(seen) - index_set):
    errors.append(f"{r} is missing from the Alphabetical Index")
for r in sorted(index_set - set(seen)):
    errors.append(f"{r} is in the Alphabetical Index but not in any section")
if index_names != sorted(index_names, key=str.lower):
    for a, b in zip(index_names, index_names[1:]):
        if a.lower() > b.lower():
            errors.append(f"Alphabetical Index out of order: '{a}' comes before '{b}'")

# 🆕 tags
for r in sorted(tagged - recent):
    errors.append(f"{r} has a 🆕 tag but is not in Recently Added")
for r in sorted(recent - tagged):
    errors.append(f"{r} is in Recently Added but its entry has no 🆕 tag")
for r in sorted(recent - set(seen)):
    errors.append(f"{r} is in Recently Added but not listed in any section")

# Counts
count = len(seen)
badge = re.search(r"badge/repos-(\d+)", text)
if not badge or int(badge.group(1)) != count:
    errors.append(f"Repos badge says {badge.group(1) if badge else '?'}, actual count is {count}")
footer = re.search(r"· (\d+) repos across", text)
if not footer or int(footer.group(1)) != count:
    errors.append(f"Footer says {footer.group(1) if footer else '?'} repos, actual count is {count}")

if errors:
    print(f"README check failed ({len(errors)} problem(s)):")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print(f"README check passed: {count} repos, {len(recent)} recently added.")
