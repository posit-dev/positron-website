---
name: prepare-release-notes
description: Guides authoring the in-product release notes in release-notes/next.md, including assembling the changelog by mining merged PRs forward from the version-bump anchor PR, and adding and iterating on images/GIFs with a local in-product preview loop before committing the asset to release-notes/assets/. Use when writing or revising next.md ahead of a release or patch (typically invoked as /prepare-release-notes). The later ship-day promotion of next.md into release.md is handled by /release-update and /patch-update, not this skill.
---

# Prepare release notes

This skill covers **authoring** `release-notes/next.md`: the content that ships to S3 as the in-product release notes during the release cycle. It is the most painful part of the job when images are involved, because you usually have to iterate on a GIF or screenshot a few times to get it to look right, and previewing an image that is not yet on the CDN takes a specific trick.

By the time `next.md` is promoted into `release.md` on ship day (`/release-update` or `/patch-update`), it should already be final and reviewed. So do the real work here.

This skill is a guided checklist. Drive the mechanical edits; pause for user input where noted with ⏸.

## 1. Where content goes

All authoring happens in `release-notes/next.md`. Use `release-notes/release-notes-template.md` as the shape of the empty state: a `### Highlights` list, the `<div id="checkbox"></div>` marker, and a `### Changelog` with `#### New features`, `#### Bug fixes`, and `#### Dependencies`. Look at the most recent `release-notes/release-*.qmd` for tone and the level of detail in highlights.

## 2. Gathering the changelog from merged PRs

The changelog is assembled from the `### Release Notes` section that each Positron PR fills in. Work through the PRs in merge order.

### a. Find the anchor PR

Every cycle opens with a PR that bumps the version, such as "Update version to 2026.08", and that PR is the first one merged for the new release. Ask the user for it if they know the number. Use its merge timestamp as the start of the window.

```bash
gh pr view <anchor> --repo posit-dev/positron --json number,title,mergedAt,baseRefName
```

### b. Fetch every merged PR with its body in one pass

Do not fetch PRs one at a time. One list call returns the bodies too.

```bash
gh pr list --repo posit-dev/positron --state merged --base main \
  --search "merged:>=YYYY-MM-DD" --limit 1500 \
  --json number,title,url,body,mergedAt,author > prs-raw.json
```

Sort by `mergedAt` and review in chronological order. Expect a few hundred PRs for a month, of which roughly a third carry release-note content (2026.08: 291 PRs, 99 with content, 49 feature bullets and 75 fix bullets). Some PRs in the window have numbers *lower* than the anchor because they sat on long-lived branches. That is correct, keep them.

### c. Extract the Release Notes section

The template shape is:

```markdown
### Release Notes

#### New Features

- N/A

#### Bug Fixes

- N/A
```

Parse from the `### Release Notes` heading until the next heading at the same level or higher, such as `### Commits` or `### QA Notes`. Then discard the `N/A` bullets, including parenthesized variants that a plain equality check misses: `- N/A (test-only change)`, `- N/A (CI-only change)`, `- N/A (e2e test infrastructure only)`.

Two things to know:

- **Labels are useless here.** `gh pr list --json labels` comes back empty for every PR in this repo, so derive the `Area:` prefix on each changelog line from the PR title and the linked issue instead.
- **External contributors** sometimes leave the template comment block in place. Strip HTML comments before parsing bullets.

### d. Audit the PRs you skipped

Do not treat "no Release Notes content" as "nothing shipped." Most skipped PRs are genuinely not user-facing: e2e and CI work, skill iterations, bootstrap extension bumps, Snyk upgrades, refactors. But some real features ship with no Release Notes section at all.

In 2026.08, both new Data Connections drivers, Redshift (#14830) and Snowflake (#14998), had no Release Notes section whatsoever and would have been missed entirely. Read the title of every skipped PR and open anything that sounds user-visible. Write those entries by hand from the PR body.

### e. Link issues, not PRs

Prefer the issue in each `[[#N](...)]` reference. Link a PR only when no issue exists.

- GraphQL `closingIssuesReferences` returns the issues GitHub has linked to the PR.
- Also scan PR bodies for `Fixes|Closes|Resolves #N`, which catches references GitHub did not link.
- Check the issue's own comments. A maintainer may have written "Closed by <PR url>", which is authoritative when the Development link is missing or points elsewhere.

```bash
gh api graphql -f query='query{repository(owner:"posit-dev",name:"positron"){
  pullRequest(number:15226){title closingIssuesReferences(first:20){nodes{number title}}}}}'
```

**Ark submodule bumps need an extra hop.** A PR titled "Bump Ark to posit-dev/ark#NNNN" lists its ark commits under `### Commits`, and the positron issue references live in the *ark* PR bodies, not in the bump PR. So read the ark PR numbers out of the bump body, then query the `posit-dev/ark` repo for those PRs and look for `posit-dev/positron#NNNN` or full positron issue URLs. In 2026.08 this recovered issue #15259 for the lone `fig-width` and `fig-height` plot sizing, which the bump PR itself did not describe.

Beware two traps with ark bumps: the bare `(#NNNN)` numbers in a bump body are *ark* PR numbers, and resolving them against the positron repo produces convincing but wrong matches. And one bump can carry several unrelated ark changes, so the issue GitHub links may belong to a different change than the release note you are writing.

### f. What not to document

Skip regressions that were introduced and fixed inside the same cycle, because users of the released build never saw them. A bump PR where the engineer deliberately filled in `N/A` is a signal worth trusting. In 2026.08 the Ark LSP hang (#15211) was filed and fixed on `main` within three days, and correctly stayed out of the notes even though it was a serious bug.

Also skip internal dev-experience and build work, extension API plumbing with no user-visible effect, and anything already shipped in a previous release. Check the previous release notes before reusing an issue number.

### g. Verify every reference

`lint.yml` checks URLs on PRs, so a bad reference fails CI. Confirm that every number resolves and that issues use `/issues/` while PRs use `/pull/`. GitHub silently redirects `/issues/N` to `/pull/N`, so a mislabeled path still opens in a browser and will not fail the link check, but it is wrong.

```bash
gh api repos/posit-dev/positron/issues/<n> --jq 'if .pull_request then "pull" else "issue" end'
```

### h. Calibrate before review

Compare the draft against the last two or three `release-*.qmd` files: entry counts, and the share of sentences longer than 30 words. Published highlight prose stays well under that limit (2026.06 at 3%, 2026.07 at 15%). A first draft easily lands above 30%, which reads dense and gets flagged.

Then run `/doc-reviewer`. Findings that recur in release notes:

- No possessives on product names. "Positron's memory footprint" becomes "the memory footprint of Positron".
- "popup" is not an approved term. Use "dialog".
- No semicolons and no em dashes.
- Avoid hypothetical "would" and prefer "sometimes did" over "could" when describing an old bug.
- Expand acronyms that are not on the excepted list. TSV and SVG are not excepted; CSV, PNG, JSON, API, SDK, SSL, and UI are.
- Refer to a button by its label alone, without the word "button".
- Bold UI elements, and use the `{pkg}` or "the pkg package" form for R and Python packages.
- Time-anchored words such as "now" and "new" ARE allowed in release notes, so do not let them get flagged.

Watch one interaction while fixing: splitting a long sentence can push a paragraph past the five-sentence limit. Split the paragraph too rather than trading one violation for another.

## 3. Adding and iterating on images (the painful part)

Images are referenced with an **absolute CDN URL**, not a relative path:

```html
<p align="center"><img src="https://cdn.posit.co/positron/releases/release-notes/assets/2026-06-posit-assistant.gif" alt="Describe the image"></p>
```

But during authoring that URL does not resolve yet, because the asset is not on the CDN. To see how it actually renders inside Positron, use the in-product preview loop below.

### a. Preview an unpublished image in-product

Positron has a _Developer: Open Current File as Release Notes_ command that renders a file as release notes. To make an unpublished image show up in that webview:

1. Put the image file **in the same directory as the file you are previewing**, i.e. directly in `release-notes/` next to `next.md` (not in a subdirectory).
2. Reference it by a **bare relative filename** while iterating:
   ```html
   <p align="center"><img src="2026-06-posit-assistant.gif" alt="Describe the image"></p>
   ```
3. Run _Developer: Open Current File as Release Notes_ on `next.md`.
4. Tweak the asset, re-export, overwrite the file, and re-run the command. Repeat until it looks right.

**Why a bare filename in the same directory, and why not other approaches** (empirical, from Positron's `releaseNotesEditor.ts`):

- The webview content security policy is `img-src https: data:;`.
- For the current file, the webview's allowed root is the file's own directory and the `<base href>` points there, so a bare relative filename resolves to an `https`-scheme webview resource and satisfies the CSP.
- Paths that leave that single directory were observed to be blocked: subdirectory paths like `assets/...` or `images/...`, parent paths like `../images/...`, and absolute file paths. That is why the iteration copy lives directly in `release-notes/`, even though its permanent home is `release-notes/assets/`.
- `http://localhost` fails (not `https`). Large `data:` URIs failed in practice (sanitizer/size), even though `data:` is allowed by the CSP.

### b. Centering

Wrap the image in `<p align="center">...</p>` so it centers in both the in-product webview and the published site. Do **not** use inline `style="..."`: the webview CSP blocks inline styles, so CSS centering will not render in-product. The `align` attribute is on the sanitizer's allow-list and is honored directly by the browser, so it works in both places and is safe to keep in the shipped markup.

## 4. Before you commit (checklist)

Once the image looks right, convert the temporary preview reference into the committed form:

1. ⏸ **Move the asset into `release-notes/assets/`** with its final name, `<year>-<month>-<slug>.<ext>` (e.g. `release-notes/assets/2026-06-posit-assistant.gif`). Do not leave the iteration copy loose in `release-notes/`.
2. **Restore the `<img src>` to the absolute CDN URL** (`https://cdn.posit.co/positron/releases/release-notes/assets/<name>`), keeping the `<p align="center">` wrapper.
3. Confirm no stray bare-filename references or temporary image copies remain in `release-notes/` (only `next.md`, the archived `release-*.qmd`, the template, and the `assets/` directory should be there).
4. Check `git status`: the new asset under `release-notes/assets/` and the edits to `next.md` should be the only changes.

## 5. How the asset reaches the CDN

You do not upload assets by hand. When a change under `release-notes/assets/` merges to `main`, the `publish-release-notes-assets.yml` workflow syncs the directory to S3 and invalidates CloudFront (additive sync, never deletes). See `release-notes/assets/README.md`.

This means you can also work in two steps if you want to preview the *real* CDN rendering rather than the in-product approximation: merge an assets-only change first so the file goes live on the CDN, then author `next.md` against the live URL. Either order is fine.
