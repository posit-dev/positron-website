---
name: release-update
description: Walks through the monthly release-day site update for positron-website. Archives last month's notes, promotes next.md into release.md, bumps versions, refreshes _freeze, flags downstream doc updates, and opens the PR. Use when the user starts the monthly release PR (typically invoked as /release-update).
---

# Monthly release update

The pattern is well-established. Reference PRs: [#295](https://github.com/posit-dev/positron-website/pull/295) (2026.03 release) and [#351](https://github.com/posit-dev/positron-website/pull/351) (2026.05 release).

This skill is a guided checklist. Drive the mechanical edits; pause for user input where noted with ⏸.

## 1. Gather and derive inputs

**Only one input from the user:** the new release's full version, e.g. `2026.06.0-179`. Derive everything else via the `gh` CLI and arithmetic, then confirm the full set with the user before touching files.

### a. Confirm the new release exists and capture its date

```bash
gh release view <new release full version> --repo posit-dev/positron --json tagName,publishedAt --jq '"\(.tagName)  \(.publishedAt[:10])"'
```

If this exits non-zero or reports "release not found", stop and re-confirm the version with the user. On success, the printed `YYYY-MM-DD` is the **new release date**.

### b. Compute next month's expected release

Decompose the new version `YYYY.MM.0-BUILD` and increment `MM`. If `MM == 12`, roll over to `YYYY+1` and `MM = 01`. Append `.0`. Examples:

- `2026.06.0-179` → next release `2026.07.0`
- `2026.12.0-179` → next release `2027.01.0`

### c. Identify the previous month's `.0` build

Decompose the new version and decrement `MM` (roll back the year if `MM == 01`). Call this `<prev YYYY.MM>`.

Then check the current `_environment` file:

```bash
grep RELEASE_VERSION _environment
```

- If `RELEASE_VERSION` starts with `<prev YYYY.MM>.0-` already (no patches happened last month), use it directly. Strip the surrounding quotes.
- Otherwise (patches happened, e.g. `2026.05.2-3`), find the `.0` build via:

  ```bash
  gh release list --repo posit-dev/positron --limit 100 --json tagName --jq ".[] | select(.tagName | startswith(\"<prev YYYY.MM>.0-\")) | .tagName"
  ```

  Should print exactly one tag. If zero or multiple, stop and ask the user.

### d. Capture the previous `.0` date

```bash
gh release view <prev .0 version> --repo posit-dev/positron --json tagName,publishedAt --jq '"\(.tagName)  \(.publishedAt[:10])"'
```

The printed date is the **previous release date** (the `.0` ship date, regardless of any patches). This is what goes into the archive YAML `date:` field.

### e. Show the user the full derived set for sign-off

Print a summary like:

```
New release:        2026.06.0-179   (2026-06-02)
Next release:       2026.07.0
Previous .0:        2026.05.0-179   (2026-05-04)
Archive file:       release-notes/release-2026-05.qmd
Branch name:        release-2026-06-0
```

Also note: any "### Patch notes" already at the top of `release-notes/release.md` will be carried forward into the archive (correct behavior).

⏸ Wait for explicit confirmation before editing files.

## 2. Branch

```bash
git checkout main && git pull
git checkout -b release-YYYY-MM-0
```

`YYYY-MM` is the new release's year-month (e.g. `release-2026-06-0`). The `-0` suffix is an iteration counter; bump if a prior branch already exists.

## 3. File edits

### `_environment`

```
RELEASE_VERSION="<new full version>"
NEXT_RELEASE="<next month .0>"
```

### Archive last month: create `release-notes/release-YYYY-MM.qmd`

Filename uses the **previous** month (e.g. `release-2026-05.qmd` for a PR releasing 2026.06).

Body = current contents of `release-notes/release.md`, with this YAML prepended:

```
---
title: "<prev .0 version> Release Notes"
date: <prev release date>
subtitle: <https://github.com/posit-dev/positron/releases/tag/<prev .0 version>>
---
```

Keep any "### Patch notes" section from `release.md` at the top of the body. It belongs in the archive.

### Promote `release-notes/next.md` to `release-notes/release.md`

Overwrite `release.md` with the current contents of `next.md`. Do not edit the content during this move.

`next.md` is the final, shipped copy: it gets pushed to the S3 bucket for in-product release notes during the release cycle, so by release day it has already been edited and reviewed. Treat this step as a straight copy.

### Reset `release-notes/next.md`

Overwrite with `release-notes/release-notes-template.md` (which is the empty-state stub with `Something cool is 🪩`, `Added new ✨`, `Fixed 🐛`, `Updated bundled version ⚙️`).

### `release-notes.qmd` alias

Update the aliases line (around line 15) to point to the **new** release month:

```yaml
aliases:
  - release-notes/release-YYYY-MM.html
```

Use the new release's year-month, not the archived month.

## 4. Refresh `_freeze`

The site uses `execute: freeze: auto`. Only re-render the specific pages that reference the `_environment` variables, not the whole site.

First, check which pages currently use the env vars so you do not miss a newly-added one:

```bash
grep -rln 'env RELEASE_VERSION\|env NEXT_RELEASE' --include='*.qmd' .
```

As of writing, the set is `download.qmd`, `install.qmd`, and `release-notes.qmd`. If grep returns a new file, render it too.

Then render each file individually:

```bash
quarto render download.qmd
quarto render install.qmd
quarto render release-notes.qmd
```

⏸ Show the user the resulting `_freeze/` diff. Expect only version-string changes; flag anything unexpected.

Commit `_freeze/` changes in a dedicated commit so the diff stays reviewable (e.g. ``Update `_freeze` ``, matching prior PRs).

## 5. Flag downstream doc updates (do NOT auto-edit)

Read the just-promoted `release.md` and skim for features that may date other pages. Common targets observed in prior release PRs:

- **Extensions / marketplace changes**: `extensions.qmd`, `migrate-vscode.qmd`, `migrate-rstudio-rproj.qmd`. PR #351 reworded these when P3M replaced Open VSX as the default.
- **Resolved RStudio gaps**: `faqs.qmd`, `migrate-rstudio-compare.qmd`. PR #351 deleted the "no inline output for Quarto" caveat once inline output shipped.
- **New diagnostics or troubleshooting commands**: `troubleshooting.qmd`. PR #295 added a section for a new diagnostics command.
- **Quarto integration changes**: `quarto.qmd`.
- **Notebook editor changes**: `notebooks-alpha.qmd` (or whatever the current notebook page is named).

⏸ Surface the list to the user and let them decide what to edit. Keep each content fix in its own commit so the PR diff stays readable.

## 6. Commit structure

Match the cadence of PRs #295 / #351:

1. `Update to YYYY.MM release` (the four mechanical files: `_environment`, archive file, `release.md`, `next.md`, `release-notes.qmd`).
2. ``Update `_freeze` `` (only `_freeze/` files).
3. One commit per incidental doc fix from step 5, with a descriptive subject (e.g. `Update info about extension gallery`, `Remove "no inline output" from FAQ`).

Heredoc the commit messages so they format cleanly. Do not skip hooks.

## 7. PR

```bash
git push -u origin release-YYYY-MM-0
```

PR conventions from past releases:

- **Title**: `Updates for YYYY.MM release`
- **Body**: one line, celebratory. `Release is out today! 🎉` or similar. Reviewers read the diff; no summary needed.
- **Base**: `main`.

⏸ Confirm title and body with the user before running `gh pr create`. Do not merge automatically.

## Style and repo conventions

- Sentence case for headings inside `.qmd` content (per the Posit style guide; PR #295 had a follow-up commit to fix this).
- No em dashes anywhere in file contents (repo style preference). Use commas, semicolons, parentheses, or two sentences.
- For keyboard shortcuts in `.qmd`, use the `{{< kbd ... >}}` shortcode, not `<kbd>` tags. Using `<kbd>` is OK in `.md` file, though.
- Suggest `/doc-reviewer` if the user wants a style pass on the new highlights or any other prose edits before opening the PR.

## Things to watch for

- If there were no patches last month, `release.md` will lack a "### Patch notes" section. That is fine; the archive simply starts at "### Release highlights".
- Workbench profile excludes videos via a Lua filter; no special handling needed during this PR.
