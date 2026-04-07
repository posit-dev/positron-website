# Positron Newsletter 1: April 2026

Welcome to the first Newsletter from the Positron Team.  

In these monthly posts we'll share updates about our team, latest releases, upcoming events, new resources and more. 

If you prefer to receive these via email, please subscribe to our mailing list here [TODO]. 

How quickly March flew by! We gathered together at our company work week in Monterey, California this month. It was a wonderful time to bond as a team and brainstorm ways we can improve Positron for you. 

[TODO Work week photo]

---
## April Release 

This month's highlights include:
* a searchable Packages Pane to easily manage your dependencies
* a polished Jupyter editing experience in the Positron Notebook Editor
* a simplified Interpreter selector 
* Positron Assistant as a built-in extension 

The April release includes **188 issues**. View the full list in the [2026.04.0 Release milestone](https://github.com/posit-dev/positron/issues?q=is%3Aissue%20milestone%3A%222026.04.0%20Release%22).

Let's dig into these highlighted features. 

---
## Packages Pane: easily manage your dependencies

Managing packages across R and Python environments gets significantly easier this month with the Packages Pane.

### Search and filter

A search bar in the Packages Pane lets you filter installed packages by name with typeahead. Optional metadata filters (like "Out of Date") help you spot what needs updating.

In a conda environment with 500+ packages, scrolling to find `scikit-learn` is painful. Search gets you there instantly.

[#12091](https://github.com/posit-dev/positron/issues/12091)

[TODO]

### Newest versions first

Package versions now sort newest-first instead of oldest-first.

The version you want is almost always the latest. No more scrolling past years of old releases.

[#12435](https://github.com/posit-dev/positron/issues/12435)

![Package versions sorted newest-first](/images/april-2026-release/package-version-sort.png)

### Unified environment detection

The Environments Pane automatically detects venv, conda, uv, and renv environments for both Python and R, with a visual interface for install, update, and remove operations.

One pane for all your environments, regardless of language or tooling. No more switching between `pip`, `conda`, and `renv::install()`.

[#11214 (Epic)](https://github.com/posit-dev/positron/issues/11214)

We'd love to hear your feedback on this [discussion thread](https://github.com/posit-dev/positron/discussions/12863).

---

## Improved Positron Notebook Editor

In February, we shipped the native Positron Notebook Editor in alpha. This month, we're filling in the interactions that make notebooks feel production-ready for daily use.

### Cell output action bar

An output action bar now appears when you hover over a cell output — **Expand**, **Collapse**, and **Clear** — and it sticks to the top as you scroll. No more hunting for a way to tame a wall of output.

When you're staring at a 500-row DataFrame print or a stack of matplotlib figures, the last thing you want is to scroll past all of it just to reach your next cell. The action bar keeps output controls right where you're looking.

[#12370](https://github.com/posit-dev/positron/issues/12370)

![Cell output action bar with expand, collapse, and clear actions](/images/april-2026-release/cell-output-action-bar.png)

### Scrollable long outputs

Long cell outputs are now contained in a scrollable region instead of stretching the notebook forever. Outputs beyond a threshold are automatically truncated, with a click to expand.

[#12371 (Epic)](https://github.com/posit-dev/positron/issues/12371)

### Drag-and-drop cell reordering

You can now drag cells to reorder them, with visual insertion indicators, ghosted previews, multi-cell support, and auto-scrolling at edges.

Reorganizing a notebook — imports at the top, grouping related analysis, reordering visualizations for a presentation — is now as natural as reordering slides. No more cut-paste-scroll-paste.

[#9840](https://github.com/posit-dev/positron/issues/9840)

### Copy and download plots from output

New toolbar buttons on cell outputs let you copy a plot to your clipboard or download it as a file in one click.

Getting a chart into a Slack thread, a Google Doc, or a slide deck should be instant — not a detour through `plt.savefig()` or a screenshot tool.

[#10806](https://github.com/posit-dev/positron/issues/10806)

![Copy and download toolbar buttons on notebook cell output](/images/april-2026-release/copy-download-plots.png)

---

## Session management, simplified

If you've ever been confused by the difference between the interpreter picker and the kernel selector, this one's for you. We redesigned session management to make it obvious what's running where.

### Notebook sessions in the interpreter picker

The interpreter picker now shows a **Notebook Sessions** group — a read-only list of active sessions for each open notebook, with the filename, language, and environment at a glance.

Previously, it wasn't clear which interpreter was attached to which notebook, or whether a session was shared with the console. Now you see everything in one place.

[#11905](https://github.com/posit-dev/positron/issues/11905) | [Epic #11861](https://github.com/posit-dev/positron/issues/11861)

![Notebook sessions displayed in the interpreter quickpick](/images/april-2026-release/notebook-sessions-quickpick.png)

### Cleaner kernel selector

The kernel selector in notebooks no longer shows the session name. It focuses on one job: showing and switching the active kernel.

Users consistently confused the kernel selector with the interpreter picker, leading to unexpected session switches. The simplified design draws a clear line: the kernel selector is about *this notebook's kernel*.

[#11904](https://github.com/posit-dev/positron/issues/11904)

![Kernel selector before and after cleanup](/images/april-2026-release/kernel-selector-cleanup.png)

---

## Positron Assistant, now built in

The Assistant is no longer a separate extension to install — it ships with Positron and is ready to enable in settings. This release also adds capabilities for enterprise teams and deeper notebook integration.

### Ships out of the box

The Assistant is now a bootstrap extension included in every Positron installation. Enable or disable it in settings — no extension marketplace required.

Every Positron user can now try AI-assisted data science with zero setup. Teams get a consistent experience out of the box.

[#12507](https://github.com/posit-dev/positron/issues/12507)

### Azure Foundry model support

Organizations can now connect the Assistant to Azure-hosted foundation models through Azure Foundry, using their own managed model deployments.

Enterprise and regulated environments often require models to stay within their cloud infrastructure. Azure Foundry support means these teams can use the Assistant with their approved endpoints — no external API calls.

[#8583 (Epic)](https://github.com/posit-dev/positron/issues/8583)

### Shared custom agents for teams

A new `chat.agentFilesLocations` setting lets you point to additional directories for custom agent files — such as a shared team repository of agents.

Data science teams can now maintain a central library of agents (e.g., "data cleaning," "model validation") that every team member picks up automatically. No more copying agent files between workspaces.

[#12132](https://github.com/posit-dev/positron/issues/12132)

### Agent skills

Agent skills — reusable, structured capabilities — are now integrated into Positron. Agents can execute workflows like "run tests and summarize failures" or "profile this dataset and suggest cleaning steps."

This makes agents composable building blocks rather than one-off chat interactions.

[#11753](https://github.com/posit-dev/positron/issues/11753)

### Notebook kernel management

The Assistant can now run all cells, interrupt execution, restart the kernel, check kernel state, and clear outputs — not just edit cells.

Previously the Assistant could write code but couldn't run it. Now it can execute a full notebook workflow end-to-end, making it a true co-pilot for notebook work.

[#12094](https://github.com/posit-dev/positron/issues/12094)

---


## Windows ARM is generally available

Windows ARM builds are promoted from experimental to stable and available through all standard installers. Surface Pro, Snapdragon X, and other ARM-based Windows devices get the full Positron experience — no workarounds needed.

[#12207](https://github.com/posit-dev/positron/issues/12207)

---


---

*[Download Positron](https://positron.posit.co/download) | [Join the discussion on GitHub](https://github.com/posit-dev/positron/discussions) | [Sign up for the newsletter](https://posit.co/positron-newsletter)*

---

## Tip of the month

> **Did you know?** [Short description of an existing but underused feature. 2-3 sentences max. Link to docs page.]

---

## Upcoming events

- **[Event name]** — [Date, time, timezone]. [Brief description]. [Sign up here](url)
- **[Event name]** — [Date]. [Description]. [Link](url)

---

## Community

[Optional. Highlight a community contribution, a user blog post, an interesting use case, or a discussion thread worth reading. 2-3 sentences.]


  Already in the milestone but not in the newsletter:

  1. Quarto improvements (11 issues) — .qmd editor enhancements, webview output fixes post-VS Code 109 update (#12373). If your audience uses Quarto,
   this is relevant.
  2. Ghost cells (#12025, #12024) — AI-suggested cells that appear inline in notebooks. We mentioned the Assistant but didn't call out ghost cells
  specifically, which are a distinctive Positron feature.
  3. Plots pane (9 issues) — any notable improvements to plot viewing/interaction worth calling out?
  4. Console improvements (9 issues) — including the "awaiting trust" regression fix (#11828).
  5. MCP autostart fix (#12259) — MCP servers loading indefinitely was a pain point; the fix may resonate with users who hit it.
  6. Dark theme fixes (#12482) — button visibility issues, if there's a nice before/after.

  Beyond the milestone — typical newsletter sections:

  7. Community spotlight — any notable community contributions, plugins, or blog posts from users?
  8. Upcoming events — workshops, webinars, conference talks (like the March post promoted a Zoom workshop).
  9. Tip or workflow of the month — a short "did you know?" featuring an existing Positron capability that's underused.
  10. Download/install CTA — version number, link, what's the one-line reason to update today.
