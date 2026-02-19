# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the documentation website for Positron IDE, built with Quarto and hosted on Netlify at https://positron.posit.co/. Documentation pages are `.qmd` files in the repository root, including reusable content in `.qmd` files that are prefixed with `_`. We use a mostly flat directory structure, especially for any files that get rendered into pages. The directories `/assets` and `/css` contain files we use for styling, and the directories `/images` and `/videos` contain visual content assets.

## Build Commands

```bash
quarto preview                # Local development with hot reload
quarto render                 # Render all .qmd files to HTML
```


## Multi-Profile Build System

The site has two Quarto profiles defined in `_quarto.yml`:
- **positron** (`_quarto-positron.yml`): Full public documentation site, outputs to `_site/`
- **workbench** (`_quarto-workbench.yml`): Subset for Workbench bundled docs, excludes download/install pages, outputs to `_site-workbench/`

New pages will likely need to be added to both profile config files.

**Videos are excluded from the workbench profile.** A Lua filter (`_extensions/video-filter/`) automatically removes video elements when building for workbench. Use the standard `{{< video >}}` shortcode; videos will appear in the public site but not in the workbench bundle.

## Code Execution and Freeze

Some pages contain executable code (e.g., download.qmd, install.qmd). The project uses Quarto's "freeze" feature (`execute: freeze: auto`). When updating pages with computations:
1. Render the page locally
2. Commit the generated files in `_freeze/` directory

## Version Management

Release versions are stored in `_environment`:
- `RELEASE_VERSION`: Current release (used in page footer via `{{< env RELEASE_VERSION >}}`)
- `NEXT_RELEASE`: Upcoming release version

Release notes live in `release-notes/` with a template at `release-notes/release-notes-template.md`.

## Writing Style Guide

**Before creating a PR, run `/doc-reviewer` to check documentation for style compliance.**

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

## CI/CD

- **Netlify**: Auto-deploys from main branch using `@quarto/netlify-plugin-quarto`
- **GitHub Actions**:
  - `lint.yml`: URL checking on PRs
  - `upload-index.yml`: Daily Algolia search index updates
  - `publish-release-notes.yml`: Manual workflow for S3/CloudFront deployment

## Issue Tracking

Report issues at https://github.com/posit-dev/positron/issues (main Positron repo, not this website repo).
