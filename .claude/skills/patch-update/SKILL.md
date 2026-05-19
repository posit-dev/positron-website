---
name: patch-update
description: Walks through the ship-day site update for a Positron patch release. Bumps versions, copies the new patch entry from next.md into release.md, resets next.md, refreshes _freeze, and opens the PR. Use when the user starts the ship-day PR for a patch (typically invoked as /patch-update). The earlier "Prepare release notes" PR that lands patch content into next.md is a separate workflow and is not part of this skill.
---

# Patch release update

The pattern is well-established. Reference ship-day PRs: [#277](https://github.com/posit-dev/positron-website/pull/277) (2026.02.1, first patch of month), [#334](https://github.com/posit-dev/positron-website/pull/334) (2026.04.1, first patch), [#357](https://github.com/posit-dev/positron-website/pull/357) (2026.05.1, first patch), [#360](https://github.com/posit-dev/positron-website/pull/360) (2026.05.2, subsequent patch).

This skill assumes a separate "Prepare release notes" PR (e.g. [#359](https://github.com/posit-dev/positron-website/pull/359)) has already merged. That earlier PR adds the new patch entry to `release-notes/next.md` and bumps `NEXT_RELEASE` in `_environment` to the upcoming patch version. The content in `next.md` ships to S3 for in-product release notes during the patch cycle, so by ship day it has already been reviewed; treat it as the source of truth for the patch description.

This skill is a guided checklist. Drive the mechanical edits; pause for user input where noted with ⏸.

## 1. Gather and derive inputs

**Only one input from the user:** the new patch's full version, e.g. `2026.05.2-3`. Derive everything else.

### a. Confirm the patch exists and capture its date

```bash
gh release view <new full version> --repo posit-dev/positron --json tagName,publishedAt --jq '"\(.tagName)  \(.publishedAt[:10])"'
```

If this exits non-zero or reports "release not found", stop and re-confirm the version with the user. On success, the printed `YYYY-MM-DD` is the **patch release date**.

### b. Decompose the version

From `YYYY.MM.N-BUILD`:

- **Display version** = `YYYY.MM.N` (used in headings and link text)
- **Tag** = full version with `-BUILD` (used in URLs)
- **Patch number** = `N` (selects first-patch vs subsequent-patch handling in step 3)

### c. Compute next month's `.0`

Decompose `YYYY.MM.N`. Increment `MM`; if `MM == 12`, roll over to `YYYY+1` and `MM = 01`. Append `.0`. This is the new `NEXT_RELEASE` value.

- `2026.05.2-3` → next release `2026.06.0`
- `2026.12.1-...` → next release `2027.01.0`

### d. Sanity-check current state

```bash
grep RELEASE_VERSION _environment
grep NEXT_RELEASE _environment
```

Expected state on ship day (the prep PR has already merged):

- `RELEASE_VERSION` is the **previously** shipped tag (e.g. `2026.05.1-2` before shipping `2026.05.2-3`, or `2026.05.0-179` before shipping `2026.05.1-2`).
- `NEXT_RELEASE` matches the patch being shipped (e.g. `2026.05.2` before shipping `2026.05.2-3`).

⏸ If `NEXT_RELEASE` does not match the new patch's `YYYY.MM.N`, the prep PR may not have merged yet. Stop and ask the user.

Then read `release-notes/next.md`. It should open with `### Patch notes`, followed by one or more paragraphs (one per patch), followed by `### Release highlights`. Confirm the **last** paragraph under `### Patch notes` references the new patch's display version and tag; this is the entry that will be inserted into `release.md` verbatim in step 3.

### e. Show the user the derived set for sign-off

```
New patch:         2026.05.2-3   (2026-05-14)
Display version:   2026.05.2
Patch number:      2     (first-patch handling: false)
Next release:      2026.06.0
Branch name:       patch-2026-05-2-is-released
Patch entry to insert into release.md (copied verbatim from next.md):
  The [2026.05.2 patch release](https://github.com/posit-dev/positron/releases/tag/2026.05.2-3) (2026-05-14) fixes ...
```

⏸ Wait for explicit confirmation before editing files.

## 2. Branch

```bash
git checkout main && git pull
git checkout -b patch-YYYY-MM-N-is-released
```

`YYYY-MM-N` uses the patch's year, month, and patch number, e.g. `patch-2026-05-2-is-released`. If a prior branch with that name exists, append a suffix.

## 3. File edits

### `_environment`

```
RELEASE_VERSION="<new full version>"
NEXT_RELEASE="<next month .0>"
```

Both lines change. Reference: PR #360 went `RELEASE_VERSION="2026.05.1-2"` to `"2026.05.2-3"` and `NEXT_RELEASE="2026.05.2"` to `"2026.06.0"`.

### `release-notes/release.md`

Extract the new patch paragraph from `release-notes/next.md`. It is the last paragraph under `### Patch notes`, just before the blank line preceding `### Release highlights`. Copy it verbatim; do not rewrite.

**First patch of the month (N == 1)**: `release.md` currently starts with `### Highlights`. Replace just that heading with:

```
### Patch notes

<the extracted patch paragraph>

### Release highlights
```

The rest of `release.md` (the existing release content) stays untouched. See PRs #277, #334, #357 for shape.

**Subsequent patch (N >= 2)**: `release.md` already has a `### Patch notes` section with prior entries. Insert the new patch paragraph as a new paragraph after the last existing patch paragraph, before the blank line that precedes `### Release highlights`. Order is chronological (oldest first, newest last). See PR #360 for shape.

### `release-notes/next.md`

Overwrite with the contents of `release-notes/release-notes-template.md`. The patch content has already shipped to S3, so `next.md` returns to the empty-state stub.

## 4. Refresh `_freeze`

The site uses `execute: freeze: auto`. Re-render only the pages that reference `_environment` variables, not the whole site.

First, check which pages currently use the env vars:

```bash
grep -rln 'env RELEASE_VERSION\|env NEXT_RELEASE' --include='*.qmd' .
```

As of writing, the set is `download.qmd`, `install.qmd`, and `release-notes.qmd`. If grep returns a new file, render it too.

```bash
quarto render download.qmd
quarto render install.qmd
quarto render release-notes.qmd
```

⏸ Show the user the resulting `_freeze/` diff. Expect only version-string changes; flag anything unexpected.

Commit `_freeze/` changes in a dedicated commit so the diff stays reviewable (e.g. ``Update `_freeze` ``, matching prior PRs).

## 5. Commit structure

Match the cadence of PRs #357 / #360:

1. `Update site for YYYY.MM.N patch release` (the three mechanical files: `_environment`, `release-notes/release.md`, `release-notes/next.md`).
2. ``Update `_freeze` `` (only `_freeze/` files).

Heredoc commit messages so they format cleanly. Do not skip hooks.

## 6. PR

```bash
git push -u origin patch-YYYY-MM-N-is-released
```

PR conventions from past patch releases:

- **Title**: `Update site for YYYY.MM.N patch release`
- **Body**: one celebratory line. Past PRs have used `Release is now out! 🚀`, `Release is now out! 🚢`, or `Release is out!`. Pick one; reviewers read the diff, no summary needed.
- **Base**: `main`.

⏸ Confirm title and body with the user before running `gh pr create`. Do not merge automatically.

## Style and repo conventions

- No em dashes in file contents (repo style preference). Use commas, semicolons, parentheses, or two sentences.
- Sentence case for headings.
- Screenshot updates for the new patch (e.g. PR #361 followed PR #360) are handled in a separate PR, not bundled here.
- Downstream doc edits (faqs, troubleshooting, etc.) are rarely needed for patches. If the patch ships a notable behavior change that dates other pages, suggest the user open a separate PR rather than bundling here.

## Things to watch for

- If `next.md` does not have a `### Patch notes` section, the prep PR likely has not merged yet. Stop and ask the user before proceeding.
- The display version in the link text (`X.Y.N`) and the tag in the URL (`X.Y.N-BUILD`) are different. Do not confuse them. PR #334 shipped with the link text reading `2026.04.0 patch release` while the tag was `2026.04.1-10`; that was a typo. Use the correct display version `YYYY.MM.N` in the link text.
- `RELEASE_VERSION` keeps its `-BUILD` suffix (e.g. `2026.05.2-3`), but `NEXT_RELEASE` does not (e.g. `2026.06.0`). Match the format of the lines you are replacing.
