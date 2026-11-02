# Contributing to Awesome Marketing Repos

Thank you for helping make this the best open-source marketing resource on GitHub! This guide covers everything you need to know to contribute.

---

## What We're Looking For

This list is focused on **open-source repositories** that help marketing teams do their jobs better. A good addition is:

- ✅ Publicly accessible on GitHub
- ✅ Actively maintained (updated within the last 18 months)
- ✅ Solves a real marketing problem
- ✅ Has meaningful documentation
- ✅ Has at least 50 GitHub stars (or is exceptionally unique/new)

We do **not** include:
- ❌ Paid or closed-source tools
- ❌ Abandoned or unmaintained repos (no commits in 18+ months)
- ❌ Generic developer tools without a clear marketing use case
- ❌ Promotional content or repos you created without disclosing the conflict of interest

---

## How to Add a Repo

### Option 1: Pull Request (preferred)

1. **Fork** this repository
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/awesome-marketing-repos.git
   cd awesome-marketing-repos
   ```
3. **Add your entry** to the most relevant section in `README.md` using this format:
   ```markdown
   - **[owner/repo](https://github.com/owner/repo)** 🆕 `[Beginner/Intermediate/Advanced]` `Best for: audience description` — One clear sentence describing what it does and why marketers care.
     ![Stars](https://img.shields.io/github/stars/owner/repo?style=flat-square)
   ```
   Each repo lives in **one** section only. If it is relevant elsewhere, add it to that section's **Also see:** line instead of duplicating the entry.
4. **Add the repo to the Alphabetical Index** at the bottom of `README.md`, keeping it sorted case-insensitively by `owner/repo`
5. **Add it to the Recently Added section** at the top. The 🆕 tag goes only on repos listed in Recently Added; remove the tag from any entry you rotate out of that list
6. **Update the tag section** if relevant tags apply
7. **Run the checks** locally: `python3 scripts/check_readme.py`
8. **Submit a pull request** with the title: `Add: owner/repo — One-line description`

### Option 2: Open an Issue

Not comfortable with PRs? [Open an issue](https://github.com/kokasexton/awesome-marketing-repos/issues/new/choose) and pick the matching template (they live in `.github/ISSUE_TEMPLATE/`). We'll add it for you.

---

## Issue Templates

These are also available as selectable templates when you open an issue.

### 🆕 Request: Add a New Repo

```
**Repo URL:** https://github.com/owner/repo

**Category it belongs in:**
[ ] AI Marketing Tools & Agents
[ ] AI Frameworks & LLM Infrastructure
[ ] LinkedIn Tools & Outreach
[ ] Email Marketing & Automation
[ ] Analytics & Attribution
[ ] SEO & Content Optimization
[ ] Social Media & Community
[ ] Lead Generation & CRM
[ ] Design & Creative Assets
[ ] Video Production & Motion
[ ] Advertising & Paid Media
[ ] Growth Engineering & Experimentation
[ ] Marketing Automation Platforms
[ ] Learning Resources & Prompts
[ ] Awesome Lists & Curations
[ ] New category: ____________

**Difficulty level:**
[ ] Beginner (no coding required)
[ ] Intermediate (some technical knowledge)
[ ] Advanced (engineering team required)

**Best for:** (who specifically benefits most)

**Why it belongs here:** (one paragraph explaining the marketing use case)

**Stars:** (check GitHub)
**Last commit:** (check GitHub)
```

---

### 🐛 Report: Outdated or Broken Repo

```
**Repo URL:** https://github.com/owner/repo

**Issue:**
[ ] Repo has been archived
[ ] No commits in 18+ months
[ ] Broken link
[ ] Misleading description
[ ] Wrong category

**Details:**
```

---

### 💡 Suggest: New Section or Feature

```
**What you'd like to add:**

**Why it would be valuable:**

**Example content:**
```

---

## Format Reference

### Difficulty Tags

| Tag | Meaning |
|-----|---------|
| `[Beginner]` | Can be used without writing code. UI-based or no-technical-setup required. |
| `[Intermediate]` | Requires some configuration, basic command line, or light scripting. |
| `[Advanced]` | Requires engineering expertise, infrastructure, or significant setup. |

### "Best for" Labels

Keep these short and specific. Examples:
- `Best for: replacing HubSpot`
- `Best for: non-technical marketers`
- `Best for: agencies managing multiple clients`
- `Best for: B2B demand gen teams`

### Shields Badges

Every entry includes a Stars badge:
```markdown
![Stars](https://img.shields.io/github/stars/OWNER/REPO?style=flat-square)
```

Editor's Picks and other flagship entries may also add a Last Commit badge:
```markdown
![Last Commit](https://img.shields.io/github/last-commit/OWNER/REPO?style=flat-square)
```

Replace `OWNER/REPO` with the actual GitHub path.

---

## Disclosure

If you're submitting a repo you created or are affiliated with, please disclose this in your PR description or issue. We welcome creator submissions — we just want transparency for readers.

---

## Automated Checks

Every pull request runs two checks (see `.github/workflows/`):
- **README consistency** (`scripts/check_readme.py`): every listed repo appears in the Alphabetical Index, the index is sorted, no repo is listed in more than one section, 🆕 tags match Recently Added, and the repo counts are accurate.
- **Link check** ([lychee](https://github.com/lycheeverse/lychee)): catches dead or moved links. It also runs weekly so link rot gets noticed.

---

## License

By contributing, you agree that your contributions are dedicated to the public domain under [CC0 1.0](LICENSE).

---

## Code of Conduct

Be respectful. This is a community resource. Contributions are reviewed on merit, not personality. If you disagree with a rejection decision, open a discussion issue rather than re-submitting or escalating.

---

*Questions? Open an issue or reach out to [@kokasexton](https://github.com/kokasexton) on GitHub.*
