# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the documentation website for Positron IDE, built with Quarto and published to GitHub Pages at https://positron.posit.co/. Documentation pages are `.qmd` files in the repository root, including reusable content in `.qmd` files that are prefixed with `_`. We use a mostly flat directory structure, especially for any files that get rendered into pages. The directories `/assets` and `/css` contain files we use for styling, and the directories `/images` and `/videos` contain visual content assets.

## File Naming

**Use all lowercase, kebab-case filenames.** This applies to everything in the repo that reaches the built site: `.qmd` pages, images, videos, poster frames, CSS, and JS. Write `tutorial-migrate-from-rstudio.qmd`, not `tutorial-migrate-from-RStudio.qmd`. Keep product names lowercase in filenames even where prose capitalizes them (`rstudio`, `vscode`, `python`).

GitHub Pages serves static files and matches paths case-sensitively, so `/Foo.html` and `/foo.html` are two different URLs and only the one that matches the file on disk resolves. The other 404s.

The two Posit logo assets (`assets/images/positron-logo_fullcolor-TM.png` and `images/posit-logo-black-TM.svg`) are known exceptions. Their references match their on-disk case, so they resolve correctly, and the `-TM` is meaningful. Leave them alone.

## Build Commands

```bash
quarto preview                # Local development with hot reload
quarto render                 # Render all .qmd files to HTML
```


## Multi-Profile Build System

The site has two Quarto profiles defined in `_quarto.yml`:
- **positron** (`_quarto-positron.yml`): Full public documentation site, outputs to `_site/`
- **workbench** (`_quarto-workbench.yml`): Subset for Workbench bundled docs, excludes the download page, outputs to `_site-workbench/`

There is also a **dailies** overlay (`_quarto-dailies.yml`) for the dev docs served at positron.posit.co/dailies, built from `main` on every merge. It is not a standalone profile: activate it together with positron, listed first so its values win for scalar options (`QUARTO_PROFILE=dailies,positron quarto render`). It only contains deltas from the positron profile (output to `_site-dailies/`, `/dailies` site URL, an announcement banner, a `NEXT_RELEASE` footer version, and a noindex meta tag), so it has no navbar/sidebar config of its own.

New pages will likely need to be added to both the positron and workbench profile config files (not the dailies overlay).

**Videos are excluded from the workbench profile.** The `cdn-video` shortcode drops video elements when `show-videos: false`, so videos appear in the public site but not in the workbench bundle. See "Videos" below.

## Code Execution and Freeze

Some pages contain executable code (e.g., download.qmd). The project uses Quarto's "freeze" feature (`execute: freeze: auto`). When updating pages with computations:
1. Render the page locally
2. Commit the generated files in `_freeze/` directory

## Version Management

Release versions are stored in `_environment`:
- `RELEASE_VERSION`: Current release (used in page footer via `{{< env RELEASE_VERSION >}}`)
- `NEXT_RELEASE`: Upcoming release version

Release notes live in `release-notes/` with a template at `release-notes/release-notes-template.md`.

## Writing Style Guide

**Before creating a PR, run `/doc-reviewer` to check documentation for style compliance.**
This must be installed separately.
You can find this skill at https://github.com/posit-dev/doc-reviewer

Key formatting rules:
- **Bold UI elements**: `**Publish**`, `**File** menu`
- **Italics for commands**: `_Extensions: Install from VSIX_`
- **Keyboard shortcuts**: In `.qmd` files, use the Quarto `kbd` shortcode:
  - Example: `{{< kbd mac=Command-Shift-P win=Ctrl-Shift-P linux=Ctrl-Shift-P >}}`
  - Do **not** use syntax like `<kbd>Cmd</kbd> + <kbd>C</kbd>` in `.qmd`
  - It is OK to use `<kbd>` syntax in markdown files
- **Settings links**: Point readers directly to the setting in their UI:
  ```markdown
  [`category.nameOfSetting`](positron://settings/category.nameOfSetting)
  ```
- **Font Awesome icons**: Use the Quarto `fa` shortcode:
  - Example: `{{< fa font-awesome-id >}}`
  - Refer to [fontawesome.com/icons](https://fontawesome.com/icons) for available icon IDs
- Add `description` YAML front matter for social sharing metadata

## Publishing and CI/CD

Two sites are published from the `gh-pages` branch, and **merging to `main` does not update the released site**:

- **positron.posit.co** (the root of `gh-pages`) serves the released docs. Only `release-docs-bundles.yml` publishes here, and only when `release_channel` is `releases`, so the site changes when we ship a release or a patch, not when a PR merges.
- **positron.posit.co/dailies** serves the docs for the in-development version. `build-and-deploy.yml` republishes it from `main` on every merge.

Both live on one branch. The root publish preserves `dailies/` and `CNAME`; the dailies publish writes only into `dailies/`. The two jobs share the `gh-pages-deploy` concurrency group, so a release publish and a merge to `main` queue instead of overwriting each other.

A fix to the released site therefore needs a release publish, not a merge. Land the fix on `main` and rerun Release Documentation Bundles. Check the workflow's `overwrite` input: the version is already published, so the pre-flight step fails the run without it. `overwrite` also deletes and recreates the GitHub release and its tag. When `main` already carries content that is not ready to ship, build instead from a backport branch cut from the release tag and pass that branch as the workflow's `ref` input.

GitHub Actions:

- `build-and-deploy.yml`: renders on every PR and every push to `main`. PRs get a Netlify deploy preview at `pr-<n>--positron-website-preview.netlify.app`; fork PRs get no preview, because they cannot read secrets. Pushes to `main` also render the dailies overlay and publish it to `gh-pages` under `dailies/`.
- `release-docs-bundles.yml`: builds the versioned docs bundles for the GitHub release and S3, and publishes the rendered `_site` to the `gh-pages` root.
- `lint.yml`: URL checking on PRs, plus the script tests for the redirect stubs and the LLM bundles.
- `publish-release-notes.yml`: manual workflow for S3/CloudFront deployment of the release notes markdown.
- `publish-release-notes-assets.yml`: syncs `release-notes/assets/` (images, GIFs) to S3/CloudFront. Runs automatically when assets change on `main`, plus manual dispatch. See `release-notes/assets/README.md`.
- `publish-videos.yml`: syncs `videos/` to the CDN. See "Videos" below.

Netlify now serves PR previews only. It no longer builds or serves production.

The Quarto version is pinned in `.quarto-version`, and both rendering workflows read it. That is the only pin, so there is nothing to keep in sync.

GitHub Pages does not read `_redirects`, but it stays the single source of truth for redirects. `scripts/generate-redirect-stubs.sh` runs as a post-render hook in the positron profile and writes meta-refresh HTML stubs into the rendered site.

## Videos

**Read `videos/README.md` before adding, replacing, or referencing a video.** It is the authoritative reference; the summary here is only so you know the shape of the workflow.

Videos are **not served by the docs site**. They are published to `cdn.posit.co` by `.github/workflows/publish-videos.yml` and referenced from pages by absolute CDN URL. Adding one is a three-step sequence, and the order matters:

1. **Encode and add the file** to `videos/` (cap at 1600px/30fps, drop silent audio tracks, use `-movflags +faststart`), then run `bash videos/generate-posters.sh` to make its poster frame. Check the poster is a sensible thumbnail rather than a splash screen or empty editor; add a per-file offset in the script if not.
2. **Merge that change to `main` first.** Publishing happens on merge, so a PR that adds a video and the page using it in one go will show a broken player in its Netlify preview.
3. **Then reference it** with the `cdn-video` shortcode, writing both the video and poster URLs out in full:

```
{{< cdn-video https://cdn.posit.co/positron/releases/videos/example.mp4
  poster="https://cdn.posit.co/positron/releases/videos/example-poster.jpg"
  aria-label="Describe what the video shows" >}}
```

Both URLs are explicit on purpose, so what you read in the source is exactly what the browser requests. `poster` and `aria-label` are both required and the build fails without them.

**Do not use Quarto's built-in `{{< video >}}` shortcode.** It injects video.js, 569 KB of render-blocking JavaScript, into the page head.

### Git LFS

Video files (`.mp4`, `.mov`) are stored with Git LFS (see `.gitattributes`). Poster frames (`.jpg`) are not; they are plain git objects, matching `images/`. When adding or replacing a video, make sure Git LFS is installed and initialized (`git lfs install`) so the file goes through the LFS filter.

If a video shows up as changed in `git diff` or `git status` but you didn't touch it, that's a phantom diff: the file was committed as raw binary instead of an LFS pointer, so the clean filter now produces a pointer that differs from the stored blob. Do not stage or commit this as part of unrelated work. Running `git add` would rewrite the stored blob into a pointer, which is a real change to history. Instead, discard it with `git restore <file>`, and open a separate PR to re-add the file through LFS:

```bash
git lfs install          # ensure LFS is set up
git rm --cached <file>   # remove the raw binary from the index
git add <file>           # re-add it through the LFS filter
git commit
```

## Issue Tracking

Report issues at https://github.com/posit-dev/positron/issues (main Positron repo, not this website repo).
