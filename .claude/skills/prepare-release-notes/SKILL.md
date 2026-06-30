---
name: prepare-release-notes
description: Guides authoring the in-product release notes in release-notes/next.md, especially adding and iterating on images/GIFs with a local in-product preview loop before committing the asset to release-notes/assets/. Use when writing or revising next.md ahead of a release or patch (typically invoked as /prepare-release-notes). The later ship-day promotion of next.md into release.md is handled by /release-update and /patch-update, not this skill.
---

# Prepare release notes

This skill covers **authoring** `release-notes/next.md`: the content that ships to S3 as the in-product release notes during the release cycle. It is the most painful part of the job when images are involved, because you usually have to iterate on a GIF or screenshot a few times to get it to look right, and previewing an image that is not yet on the CDN takes a specific trick.

By the time `next.md` is promoted into `release.md` on ship day (`/release-update` or `/patch-update`), it should already be final and reviewed. So do the real work here.

This skill is a guided checklist. Drive the mechanical edits; pause for user input where noted with ⏸.

## 1. Where content goes

All authoring happens in `release-notes/next.md`. Use `release-notes/release-notes-template.md` as the shape of the empty state: a `### Highlights` list, the `<div id="checkbox"></div>` marker, and a `### Changelog` with `#### New features`, `#### Bug fixes`, and `#### Dependencies`. Look at the most recent `release-notes/release-*.qmd` for tone and the level of detail in highlights.

## 2. Adding and iterating on images (the painful part)

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

## 3. Before you commit (checklist)

Once the image looks right, convert the temporary preview reference into the committed form:

1. ⏸ **Move the asset into `release-notes/assets/`** with its final name, `<year>-<month>-<slug>.<ext>` (e.g. `release-notes/assets/2026-06-posit-assistant.gif`). Do not leave the iteration copy loose in `release-notes/`.
2. **Restore the `<img src>` to the absolute CDN URL** (`https://cdn.posit.co/positron/releases/release-notes/assets/<name>`), keeping the `<p align="center">` wrapper.
3. Confirm no stray bare-filename references or temporary image copies remain in `release-notes/` (only `next.md`, the archived `release-*.qmd`, the template, and the `assets/` directory should be there).
4. Check `git status`: the new asset under `release-notes/assets/` and the edits to `next.md` should be the only changes.

## 4. How the asset reaches the CDN

You do not upload assets by hand. When a change under `release-notes/assets/` merges to `main`, the `publish-release-notes-assets.yml` workflow syncs the directory to S3 and invalidates CloudFront (additive sync, never deletes). See `release-notes/assets/README.md`.

This means you can also work in two steps if you want to preview the *real* CDN rendering rather than the in-product approximation: merge an assets-only change first so the file goes live on the CDN, then author `next.md` against the live URL. Either order is fine.
