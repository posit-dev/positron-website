# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is the documentation website for Positron, a next-generation data science IDE built by Posit PBC. The site uses Quarto as the static site generator and is deployed on Netlify.

## Development Commands

- **Preview site locally**: `quarto preview`
- **Render specific page**: `quarto render [filename.qmd]`
- **Lint documentation**: `vale .` (requires Vale installed locally)
- **Check URLs**: Run URL checker via GitHub Actions on PRs

The site auto-renders on changes to `.qmd` files during preview.

### VS Code / Positron Debug Configurations

Two debug configurations are available in `.vscode/launch.json`:
- **Preview Docs (Chrome)**: Runs `quarto preview` and opens in Chrome
- **Preview Docs (Edge)**: Runs `quarto preview` and opens in Edge

## Architecture

### Technology Stack
- **Static Site Generator**: Quarto v1.8.16 with Posit product documentation theme
- **Deployment**: Netlify (via `@quarto/netlify-plugin-quarto`)
- **Extensions**: Font Awesome icons, custom Posit theme
- **Execution**: Freeze enabled for computational reproducibility
- **Linting**: Vale with custom Posit and Microsoft style rules

### Content Structure
- Each feature/topic has its own `.qmd` file
- Sidebar navigation organized in three sections: Get Started, Guides, Help
- Computational outputs cached in `_freeze/` directory
- Images stored in `images/` directory
- Release notes stored in `release-notes/` directory

### Key Files
- `_quarto.yml`: Site configuration and navigation structure
- `download.qmd`: Contains executable code for dynamic download page (uses params)
- `styles.css`: Custom styling (mainly for settings gear icons)
- `_environment`: Contains version information (RELEASE_VERSION, NEXT_RELEASE)
- `.vale.ini`: Vale linting configuration
- `netlify.toml`: Netlify deployment configuration

## Documentation Guidelines

When writing or editing documentation:

1. **Audience**: Less technical users (data scientists, IT professionals)
2. **Tone**: Clear, accessible, encouraging
3. **Formatting**:
   - Bold for UI elements: **File** menu
   - Backticks for code/config: `quarto preview`
   - Sentence case for headings (except H1)
4. **Writing rules**:
   - Brief sentences (28-30 words max)
   - Active voice preferred
   - Present tense
   - No contractions
   - Oxford comma

## Workflow Notes

- Issues tracked in main Positron repository: https://github.com/posit-dev/positron/issues
- Vale linting runs automatically on PRs via GitHub Actions
- URL checking also runs automatically on PRs
- When updating pages with computations, render locally and commit `_freeze/` changes
- Content licensed under Creative Commons Attribution-ShareAlike 4.0
- Release notes can be published to S3/CloudFront via GitHub Actions workflow

## Special Quarto Syntax

The documentation uses several Quarto-specific features beyond standard markdown:

### Callout Blocks
```markdown
::: {.callout-note}
Informational content here
:::

::: {.callout-tip}
Helpful tip content here
:::

::: callout-important
## Optional custom heading
Important information here
:::
```

### Code Chunks with Options
```markdown
```{r, id='chunk-name'}
#| echo: false
#| warning: false
#| classes: plain
# R code here
```

### Panel Tabsets
```markdown
::: {.panel-tabset}
### Tab 1 Name
Content for first tab

### Tab 2 Name
Content for second tab
:::
```

### Layout Directives
```markdown
::: {#fig-example layout-ncol=2}
![First image](image1.png)
![Second image](image2.png)
:::
```

### Image Attributes
```markdown
![Alt text](image.png){width=700}
![Alt text](image.png){height=400}
```

### Special Links
- Positron settings: `positron://settings/setting.name`
- Cross-references to other pages: `[Link text](filename.qmd)`

### Keyboard Shortcuts
Use `<kbd>` tags for keyboard shortcuts:
```markdown
<kbd>Cmd</kbd>+<kbd>Enter</kbd> (Mac)
<kbd>Ctrl</kbd>+<kbd>Enter</kbd> (Windows/Linux)
```

### YAML Frontmatter Options
- `params:` - For parameterized documents (e.g., download.qmd)
- `include-in-header:` - For custom HTML/CSS inclusion
- `hide-description: true` - To hide page descriptions
- `pagetitle:` - For custom page titles