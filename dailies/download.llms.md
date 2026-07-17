# Download Positron

Download Positron for Windows, macOS, or Linux. Free data science IDE supporting Python and R with automatic updates included.

## Positron on desktop

Find out what you need to know before you [install](install.llms.md) Positron, then download the desktop installer for your platform.

> **IMPORTANT:**
>
> Please review [Positron’s license agreement](licensing.llms.md) and [privacy policy](https://posit.co/about/privacy-policy/). Your acceptance of this license agreement and privacy policy is required as a condition to proceeding with your download or use of the software.
>
> I agree to the [Positron license agreement](licensing.llms.md) and [Posit Privacy Policy](https://posit.co/about/privacy-policy/).

| Platform | Download | Size | SHA-256 |
|:---|:---|:---|:---|
| Windows 10, 11 x64 (system level install) | [Positron-2026.07.1-5-Setup-x64.exe](https://cdn.posit.co/positron/releases/win/x86_64/Positron-2026.07.1-5-Setup-x64.exe) | 425M | 95c1039 |
| Windows 10, 11 x64 (user level install) | [Positron-2026.07.1-5-UserSetup-x64.exe](https://cdn.posit.co/positron/releases/win/x86_64/Positron-2026.07.1-5-UserSetup-x64.exe) | 425M | 7672c1c |
| Windows 11 arm64 (system level install) | [Positron-2026.07.1-5-Setup-arm64.exe](https://cdn.posit.co/positron/releases/win/arm64/Positron-2026.07.1-5-Setup-arm64.exe) | 418M | b28c6dd |
| Windows 11 arm64 (user level install) | [Positron-2026.07.1-5-UserSetup-arm64.exe](https://cdn.posit.co/positron/releases/win/arm64/Positron-2026.07.1-5-UserSetup-arm64.exe) | 418M | e8a2e36 |
| MacOS 11.0+ (arm64/Apple Silicon) | [Positron-2026.07.1-5-arm64.dmg](https://cdn.posit.co/positron/releases/mac/arm64/Positron-2026.07.1-5-arm64.dmg) | 799M | dec25d7 |
| MacOS 11.0+ (x64/Intel) | [Positron-2026.07.1-5-x64.dmg](https://cdn.posit.co/positron/releases/mac/x64/Positron-2026.07.1-5-x64.dmg) | 811M | 1e6e88e |
| Debian-based Linux x64 (Ubuntu 20+) | [Positron-2026.07.1-5-x64.deb](https://cdn.posit.co/positron/releases/deb/x86_64/Positron-2026.07.1-5-x64.deb) | 454M | 432e22d |
| Debian-based Linux arm64 (Ubuntu 20+) | [Positron-2026.07.1-5-arm64.deb](https://cdn.posit.co/positron/releases/deb/arm64/Positron-2026.07.1-5-arm64.deb) | 428M | a928ea0 |
| Red Hat-based Linux x64 (RHEL9) | [Positron-2026.07.1-5-x64.rpm](https://cdn.posit.co/positron/releases/rpm/x86_64/Positron-2026.07.1-5-x64.rpm) | 519M | b01a872 |
| Red Hat-based Linux arm64 (RHEL9) | [Positron-2026.07.1-5-arm64.rpm](https://cdn.posit.co/positron/releases/rpm/arm64/Positron-2026.07.1-5-arm64.rpm) | 492M | 14407c2 |

  

Once you install Positron, it will [automatically check for updates moving forward](updating.llms.md).

> **NOTE:**
>
> Want to be notified about upcoming releases, new features, and community events? [Sign up for Positron updates](https://posit.co/positron-updates-signup/).

## Positron Pro on Posit Workbench

[Posit Workbench](https://posit.co/products/enterprise/workbench/) 2025.09.0 and later includes support for Positron Pro. To configure and use Positron Pro on Posit Workbench, please see the [Posit Workbench Administration Guide](https://docs.posit.co/ide/server-pro/admin/positron_sessions/) and the [Positron Pro user guide](https://docs.posit.co/ide/server-pro/user/positron/getting-started/).

## Release notes

The current release of Positron is 2026.07.1-5.

### Patch notes

The [2026.07.1 patch release](https://github.com/posit-dev/positron/releases/tag/2026.07.1-5) (2026-07-09) improves Python discovery behavior and when GitHub Copilot completions are offered.

### Release highlights

Welcome to the 2026.07.0 release of Positron!

- [Positron Notebook Editor](#positron-notebook-editor)
- [Packages pane](#packages-pane)
- [Posit Assistant](#posit-assistant)
- [R language intelligence](#r-language-intelligence)
- [Open Excel files directly in the Data Explorer](#open-excel-files-directly-in-the-data-explorer)
- [Try Data Connections (preview)](#try-data-connections-preview)

#### Positron Notebook Editor

The [Positron Notebook Editor](https://positron.posit.co/positron-notebook-editor) comes out of preview to general availability in this release, and is now the default editor for Jupyter (`.ipynb`) notebooks. Built specifically for data science, it offers notebook-aware AI assistance, integrated data exploration through the Variables pane and Data Explorer, and debugging that works out of the box, with no extensions required.

Alongside general availability, this release adds a wave of improvements. You can split-edit a notebook side by side, add and manage cell tags, run a selection or the current line in a cell, and export a notebook to a Quarto, Python, or R file. A new Help panel, opened from a toolbar button or F1, lists notebook commands and keyboard shortcuts, and we added many of the keyboard shortcuts you know from JupyterLab. Rich outputs also render more faithfully, including inline PDFs, Mermaid diagrams, htmlwidgets, and theme-aware ipywidgets.

#### Packages pane

The [Packages](https://positron.posit.co/packages-pane) pane also comes out of preview to general availability in this release. It gives you a live view of the R and Python packages installed in your active session, so you can search, install, update, and remove packages, and jump to their documentation, without leaving Positron.

![The Packages pane in Positron, showing installed Python packages with a detail editor.](https://cdn.posit.co/positron/releases/release-notes/assets/2026-07-packages-pane.gif)

This release also makes the pane more capable. Clicking a package opens a detail editor with its overview, metadata, and actions, similar to the Extensions pane. Installing a package searches results as you type, and each row has a button that opens the package’s website. Update indicators appear immediately on a new session from a cached snapshot, and **Update All Packages** reports exactly what changed. Package operations keep your environment consistent too, resolving against a workspace `requirements.txt` for Python and updating the `renv.lock` snapshot for R.

#### Posit Assistant

[Posit Assistant](https://assistant.posit.co/) is our unified, data-science-focused approach to AI assistance in Positron. As announced in the [previous release](https://opensource.posit.co/blog/2026-06-08_positron-2026-06-release/), we have now removed the older Positron Assistant, and Posit Assistant is the single way to bring AI into your Positron workflow. For the story of how we got here, read about the [history of Posit data science agents](https://opensource.posit.co/blog/2026-06-11_history-of-posit-data-science-agents/).

This release also gives you finer control over AI in Positron. The new [`ai.enabled`](positron://settings/ai.enabled) setting turns off every Positron AI feature at once, and administrators can enforce it; [`notebook.ai.enabled`](positron://settings/notebook.ai.enabled) does the same for notebooks specifically. The set of language model providers keeps growing, with DeepSeek joining as an experimental provider and Microsoft Foundry reaching general availability. The configuration modal now shows every provider by default with preview and experimental badges.

#### R language intelligence

Last release, R language support in Positron gained the ability to understand symbols within a file, and this release takes that further. Go to Definition, Find References, and Rename Symbol now work across files, in both R packages and standalone scripts, where cross-file resolution follows `source()` calls. This more accurate resolution strategy is experimental and, for now, powers symbol navigation only. R language intelligence is also more responsive to your workspace. Features such as diagnostics and workspace symbols react to changes made outside open editors, like switching a git branch or having an agent write a file. What Positron knows about your code stays in sync with what is on disk.

#### Open Excel files directly in the Data Explorer

Open an Excel workbook (`.xlsx`) and start exploring it right away in the [Data Explorer](https://positron.posit.co/data-explorer), without first needing to load it via Python or R. Sort, filter, and profile columns, switch between worksheets, and toggle whether the first row holds column names. An **Open in Excel** button opens the workbook in your native spreadsheet application.

This release broadens what you can open in the Data Explorer overall. Backed by a native DuckDB engine, it now also previews compressed CSV, TSV, and Parquet files. Also, a new **Open in Data Explorer** code action, from the editor lightbulb or Cmd+., opens the data frame under your cursor in R, Python, and Quarto files, so you can jump straight from your code to exploring your data.

#### Try Data Connections (preview)

We are building new Data Connections support to become the way you work with database-like resources in Positron, from local files and database servers to cloud data warehouses. In this experimental preview, you can browse schemas, tables, views, columns, and indexes in a tree, open a table or view in the Data Explorer with a double-click, and generate ready-to-run connection code in Python or R. It supports DuckDB, PostgreSQL, and SQLite today, with more databases and warehouses on the way. This feature is in early days, and your feedback will directly shape where it goes. Learn how to try it out and tell us what you think in the [Data Connections discussion](https://github.com/posit-dev/positron/discussions/14571): which databases and warehouses you need, whether the connection setup is clear, and anything confusing, missing, or broken.

### Changelog

#### New features

- \[[\#13529](https://github.com/posit-dev/positron/issues/13529)\] Notebooks: the Positron Notebook Editor is now the default editor for Jupyter notebooks.
- \[[\#10598](https://github.com/posit-dev/positron/issues/10598)\] Notebooks: Mermaid diagrams in notebook markdown cells now render as visual diagrams.
- \[[\#13876](https://github.com/posit-dev/positron/issues/13876)\] Notebooks: added support for split editing of notebooks.
- \[[\#13510](https://github.com/posit-dev/positron/issues/13510), [\#13512](https://github.com/posit-dev/positron/issues/13512)\] Notebooks: added a Help panel for the notebook editor (from a toolbar button or F1) with keyboard shortcuts and a searchable list of notebook commands grouped by area.
- \[[\#1532](https://github.com/posit-dev/positron/issues/1532)\] Notebooks: added inline cell tag support, with commands to add, remove, and toggle the visibility of tags.
- \[[\#3804](https://github.com/posit-dev/positron/issues/3804)\] Notebooks: run a selection or the current line in a notebook cell with Cmd/Ctrl+Shift+Enter, with the output shown on that cell.
- \[[\#9791](https://github.com/posit-dev/positron/issues/9791)\] Notebooks: added an **Export…** action to export a Jupyter notebook to Quarto (`.qmd`), Python, or R.
- \[[\#10606](https://github.com/posit-dev/positron/issues/10606)\] Notebooks: PDF outputs (such as from `IPython.display.IFrame`) now render inline in notebook cells using the full PDF viewer, with an **Open With…** action to open the PDF in another editor.
- \[[\#12727](https://github.com/posit-dev/positron/issues/12727)\] Notebooks: added commonly expected JupyterLab keyboard shortcuts, such as changing a cell to a heading level (1-6), toggling line numbers (Shift+L), and interrupting the kernel (I I).
- \[[\#13314](https://github.com/posit-dev/positron/issues/13314)\] Notebooks: the inline add-cell control now has a Code/Raw split button, so you can add a raw cell inline.
- \[[\#13323](https://github.com/posit-dev/positron/issues/13323)\] Notebooks: the R debugger for notebooks now supports Watch pane expressions.
- \[[\#14542](https://github.com/posit-dev/positron/issues/14542)\] Notebooks: added a [`notebook.ai.enabled`](positron://settings/notebook.ai.enabled) setting to turn off all notebook AI features (ghost cell suggestions, the Assistant, Visualize, and Fix/Explain) at once; notebook AI is active only when both this and the global [`ai.enabled`](positron://settings/ai.enabled) are on.
- \[[\#12527](https://github.com/posit-dev/positron/issues/12527)\] Notebooks: notebook settings now show a **Legacy** badge in the Settings editor when they only apply to the legacy notebook editor, and can be filtered with `@tag:legacy` or `@tag:positronNotebook`.
- \[[\#13128](https://github.com/posit-dev/positron/issues/13128)\] Packages: search for packages as you type when installing from the Packages pane, with results ordered to surface exact matches first.
- \[[\#13723](https://github.com/posit-dev/positron/issues/13723)\] Packages: package update indicators now appear immediately in the Packages pane on a new session, restored from a disk cache while the latest status refreshes in the background; the new [`packages.outdatedCache.enabled`](positron://settings/packages.outdatedCache.enabled) and [`packages.outdatedCache.maxAgeHours`](positron://settings/packages.outdatedCache.maxAgeHours) settings control this.
- \[[\#13890](https://github.com/posit-dev/positron/issues/13890)\] Packages: added an external link button to Packages pane rows that opens a package’s website.
- \[[\#13129](https://github.com/posit-dev/positron/issues/13129)\] Packages: after installing or updating a package, the affected package now scrolls into view and briefly flashes in the Packages pane so the change is easy to spot.
- \[[\#13607](https://github.com/posit-dev/positron/issues/13607)\] Packages: **Update All Packages** now reports which packages were actually updated, and confirms when everything is already up to date.
- \[[\#12926](https://github.com/posit-dev/positron/issues/12926)\] Packages: click a package in the Packages pane to open a detail editor showing its overview, metadata, and actions (such as Update, Uninstall, and Show Help), similar to the Extensions pane.
- \[[\#13808](https://github.com/posit-dev/positron/issues/13808), [\#13222](https://github.com/posit-dev/positron/issues/13222)\] Assistant: the older Positron Assistant has been removed, as announced in the previous release. Posit Assistant is now the unified approach to AI assistance in Positron, and the standalone chat UI reverts to Copilot Chat.
- \[[\#14356](https://github.com/posit-dev/positron/issues/14356)\] Assistant: added an [`ai.enabled`](positron://settings/ai.enabled) setting that turns off all Positron-integrated AI features (Posit Assistant, GitHub Copilot, Posit AI Next Edit Suggestions, notebook AI features, and Console Fix & Explain) at once, and can be enforced by administrators.
- \[[\#13652](https://github.com/posit-dev/positron/issues/13652)\] Assistant: added DeepSeek as an experimental language model provider (behind [`assistant.provider.deepseek.enabled`](positron://settings/assistant.provider.deepseek.enabled)).
- \[[\#13630](https://github.com/posit-dev/positron/issues/13630)\] Assistant: language model management actions (such as **Configure Language Model Providers**) are now hidden from the accounts menu and Command Palette when AI features are disabled.
- \[[\#13810](https://github.com/posit-dev/positron/issues/13810)\] Assistant: Microsoft Foundry is now generally available as a language model provider, no longer in preview.
- \[[\#14026](https://github.com/posit-dev/positron/pull/14026)\] Connections: added a native DuckDB data connection driver to the Connections pane.
- \[[\#14177](https://github.com/posit-dev/positron/pull/14177)\] Connections: you can now open a database table, view, or column from the Connections pane in the Data Explorer (by double-clicking or using the **Open in Data Explorer** action), for the SQLite, PostgreSQL, and DuckDB drivers.
- \[[\#14357](https://github.com/posit-dev/positron/pull/14357)\] Connections: generate Python and R connection code (**Connect With**) for SQLite, DuckDB, and PostgreSQL databases, with multiple package variants, an editable code preview, and the option to copy it, save it as a script, or run it in a console.
- \[[\#14357](https://github.com/posit-dev/positron/pull/14357)\] Connections: browse database schema in the Data Connections panel, with indexes nested under their tables and a primary-key indicator on table columns.
- \[[\#14498](https://github.com/posit-dev/positron/pull/14498)\] Connections: data connection drivers can now offer multiple connection mechanisms, selectable when creating a connection; PostgreSQL offers user and password, local server, client certificate, and connection string.
- \[[\#13859](https://github.com/posit-dev/positron/issues/13859)\] Quarto: reworked the inline output cell toolbar with a more prominent **Run** button and a **More cell actions** menu (cut, copy, delete, join, and insert cells); the new [`positron.quarto.inlineOutput.showCellToolbar`](positron://settings/positron.quarto.inlineOutput.showCellToolbar) setting can hide it.
- \[[\#13288](https://github.com/posit-dev/positron/issues/13288)\] Quarto: LaTeX display equations (`$$ ... $$`) now render inline in Quarto and R Markdown documents, updating live as you edit; controlled by the new [`positron.quarto.equationPreview.enabled`](positron://settings/positron.quarto.equationPreview.enabled) setting.
- \[[\#12891](https://github.com/posit-dev/positron/issues/12891)\] Quarto: added a **Preview** split button to the editor action bar, with a dropdown to preview a document in a specific format such as HTML, PDF, or Word.
- \[[\#14029](https://github.com/posit-dev/positron/issues/14029)\] Quarto: Positron can now be set as the default application to open `.qmd` files from the OS file manager, with a Quarto document icon (macOS and Windows).
- \[[\#5889](https://github.com/posit-dev/positron/issues/5889)\] Data Explorer: can now preview compressed CSV, TSV, and Parquet files, using native DuckDB.
- \[[\#4202](https://github.com/posit-dev/positron/issues/4202)\] Data Explorer: added Excel (`.xlsx`) workbook support, including multi-sheet selection, a header-row toggle, and an **Open in Excel** action.
- \[[\#2974](https://github.com/posit-dev/positron/issues/2974)\] Data Explorer: added an **Open in Data Explorer** code action that opens the Data Explorer for the data frame at the editor cursor, available from the editor lightbulb (Cmd+.) in R, Python, and Quarto files.
- \[[\#4525](https://github.com/posit-dev/positron/issues/4525)\] R: language intelligence features (diagnostics, workspace symbols, and more) are now reactive to changes outside open editors, such as switching a git branch or an agent writing a file in the workspace.
- \[[\#11112](https://github.com/posit-dev/positron/issues/11112)\] R: Go to Definition, Find References, and Rename Symbol now work across files, both in packages and in standalone scripts (following `source()` calls). This more accurate resolution strategy is experimental and currently used only for symbol navigation.
- \[[\#13256](https://github.com/posit-dev/positron/issues/13256)\] Python: added a *Python: Install Python via uv* command to the Command Palette for on-demand, uv-managed Python installation.
- \[[\#11458](https://github.com/posit-dev/positron/issues/11458)\] Console: added a resource monitor to the Console action bar when only one console is open, so it appears even without a console tab list.
- \[[\#12790](https://github.com/posit-dev/positron/issues/12790)\] Variables: added a configurable low-memory warning to the Variables pane memory meter, controlled by the new [`memoryUsage.lowMemoryThresholdPercent`](positron://settings/memoryUsage.lowMemoryThresholdPercent) and [`memoryUsage.lowMemoryThresholdMB`](positron://settings/memoryUsage.lowMemoryThresholdMB) settings.
- \[[\#3676](https://github.com/posit-dev/positron/issues/3676)\] Plots: R plots with Quarto figure dimensions (`fig-width` and `fig-height`) are now drawn at those dimensions in the Plots pane.
- \[[\#13135](https://github.com/posit-dev/positron/issues/13135)\] Interpreter: the interpreter picker now shows a progress spinner and status message while interpreters are still being discovered.
- \[[\#13118](https://github.com/posit-dev/positron/issues/13118)\] Workbench: added an API for extensions to be notified when files are uploaded or downloaded.
- \[[\#14260](https://github.com/posit-dev/positron/pull/14260)\] Server: Positron Server (such as running on JupyterHub) now verifies signed license tokens against a public key, replacing the file-based license-manager activation flow.

#### Bug fixes

- \[[\#13688](https://github.com/posit-dev/positron/issues/13688)\] Notebooks: fixed the notebook kernel badge spinning indefinitely when opening a saved notebook.
- \[[\#10466](https://github.com/posit-dev/positron/issues/10466)\] Notebooks: fixed conditional cell actions (such as Run All Above) not appearing in the Notebook Cells editor submenu.
- \[[\#13919](https://github.com/posit-dev/positron/issues/13919)\] Notebooks: fixed Quick Open consolidating split notebook panes instead of activating the notebook in place.
- \[[\#13564](https://github.com/posit-dev/positron/issues/13564)\] Notebooks: reduced the top and bottom padding above the first cell so it feels visually anchored.
- \[[\#8383](https://github.com/posit-dev/positron/issues/8383)\] Notebooks: fixed images displayed with `retina=True` rendering at full pixel size instead of the correct half-size dimensions.
- \[[\#12618](https://github.com/posit-dev/positron/issues/12618)\] Notebooks: fixed a cell staying stuck in the running state when the runtime exits unexpectedly, so the play button now resets.
- \[[\#13561](https://github.com/posit-dev/positron/issues/13561)\] Notebooks: fixed concurrently created untitled notebooks all being named `Untitled-1.ipynb`.
- \[[\#12665](https://github.com/posit-dev/positron/issues/12665)\] Notebooks: fixed the [`editor.scrollBeyondLastLine`](positron://settings/editor.scrollBeyondLastLine) setting having no effect in Positron notebooks.
- \[[\#4219](https://github.com/posit-dev/positron/issues/4219)\] Notebooks: fixed htmlwidgets (such as leaflet and plotly) not rendering inline, across the Jupyter notebook, Positron notebook, and inline Quarto output views.
- \[[\#13567](https://github.com/posit-dev/positron/issues/13567)\] Notebooks: fixed excessive left gutter padding on code cells, and all code cells now share the same line-number column width.
- \[[\#11586](https://github.com/posit-dev/positron/issues/11586)\] Notebooks: fixed a cell footer showing a stale execution time when you scroll back to the cell.
- \[[\#13565](https://github.com/posit-dev/positron/issues/13565)\] Notebooks: removed an underscore-like artifact that appeared to the left of unexecuted code cells; the execution-order badge now shows only after a cell has run.
- \[[\#14160](https://github.com/posit-dev/positron/issues/14160), [\#14194](https://github.com/posit-dev/positron/issues/14194)\] Notebooks: fixed Great Tables output overflowing into neighboring cells and hiding the output action bar buttons on hover, by rendering full-document HTML inline instead of in a webview overlay.
- \[[\#12806](https://github.com/posit-dev/positron/issues/12806)\] Notebooks: ipywidgets in notebook outputs now inherit the active Positron theme instead of the hardcoded JupyterLab palette, fixing low-contrast widgets in dark themes.
- \[[\#14127](https://github.com/posit-dev/positron/issues/14127), [\#13559](https://github.com/posit-dev/positron/issues/13559)\] Notebooks: fixed notebook modals (Help, Ghost Cell Info, Assistant, and Visualize) not closing on Escape when opened over a cell in edit mode.
- \[[\#13283](https://github.com/posit-dev/positron/issues/13283)\] Notebooks: fixed closing a Data Explorer editor tab breaking a still-open inline data explorer in a notebook cell output that shared the same connection.
- \[[\#12627](https://github.com/posit-dev/positron/issues/12627)\] Packages: R package install, update, and uninstall in renv projects no longer report failure when only the `renv.lock` snapshot fails; the new [`packages.r.renvAutoSnapshot`](positron://settings/packages.r.renvAutoSnapshot) setting controls the automatic snapshot.
- \[[\#14195](https://github.com/posit-dev/positron/issues/14195)\] Packages: fixed the first R package install or update in a session hanging when the pak install prompt was suppressed by notification filtering, such as Do Not Disturb.
- \[[\#14328](https://github.com/posit-dev/positron/issues/14328)\] Packages: installing or updating a Python package from the Packages pane now keeps the environment consistent, resolving against a workspace `requirements.txt` when present (otherwise the full installed set); an operation that would leave the environment inconsistent now fails with an error instead of silently breaking it. You can opt out of using `requirements.txt` with the new [`python.packageManager.useRequirementsFile`](positron://settings/python.packageManager.useRequirementsFile) setting.
- \[[\#14344](https://github.com/posit-dev/positron/issues/14344)\] Packages: the Python version picker now lists only versions installable in the active environment, hiding versions excluded by `Requires-Python` or that have been yanked.
- \[[\#13933](https://github.com/posit-dev/positron/issues/13933)\] Assistant: fixed the Assistant layout preset not opening the Posit Assistant pane.
- \[[\#13750](https://github.com/posit-dev/positron/issues/13750)\] Assistant: fixed the Snowflake Cortex provider referencing a nonexistent base URL setting.
- \[[\#14056](https://github.com/posit-dev/positron/issues/14056)\] Assistant: updated the provider notices in the language model configuration dialog, adding Terms of Service and Privacy Policy links for more providers.
- \[[\#13930](https://github.com/posit-dev/positron/issues/13930)\] Assistant: the Console **Fix** and **Explain** actions now appear for Posit Assistant users even when the legacy Positron Assistant is disabled.
- \[[\#13446](https://github.com/posit-dev/positron/issues/13446)\] Assistant: fixed MCP server OAuth sign-in on Posit Workbench and Positron Server.
- \[[\#13856](https://github.com/posit-dev/positron/issues/13856)\] Assistant: expiring AWS credentials are now refreshed on demand, so Bedrock keeps working in a long-lived session instead of failing with an expired-token error.
- \[[\#13810](https://github.com/posit-dev/positron/issues/13810)\] Assistant: all language model providers now show in the configuration modal by default, with preview and experimental providers indicated by a badge.
- \[[\#14563](https://github.com/posit-dev/positron/issues/14563)\] Assistant: renamed two language model providers in the provider modal: Gemini Code Assist is now Google Gemini, and Google Vertex AI is now Gemini Enterprise Agent Platform.
- \[[\#13716](https://github.com/posit-dev/positron/issues/13716)\] Assistant: Copilot inline completion language settings are now controlled by [`github.copilot.enable`](positron://settings/github.copilot.enable); Positron migrates the deprecated `positron.assistant.inlineCompletions.enable` setting automatically.
- \[[\#14026](https://github.com/posit-dev/positron/pull/14026)\] Connections: database connection drivers now run their native bindings in an isolated worker process, so a native fault in a connection no longer crashes the extension host.
- \[[\#13984](https://github.com/posit-dev/positron/issues/13984)\] Quarto: fixed floating “ghost” cell toolbars that could appear after deleting a cell.
- \[[\#13936](https://github.com/posit-dev/positron/issues/13936)\] R: fixed module-managed R interpreters at standard `/opt/R/<version>` locations were losing their environment module metadata, so the `module load` startup command now runs and module-provided dependencies are available.
- \[[\#14222](https://github.com/posit-dev/positron/issues/14222)\] R: fixed the runtime discovery cache sometimes missing R versions installed with [rig](https://github.com/r-lib/rig), particularly the default version. If you still have trouble with R 4.6 being discovered, update to the latest version of rig.
- \[[\#10682](https://github.com/posit-dev/positron/issues/10682)\] R: fixed the Test Explorer not matching test outcomes for testthat `describe()` and `it()` tests after testthat 3.3.0.
- \[[\#10133](https://github.com/posit-dev/positron/issues/10133)\] R: fixed the Test Explorer being unable to run an individual test with a multi-line description on Windows.
- \[[\#2929](https://github.com/posit-dev/positron/issues/2929)\] R: the Test Explorer now live-updates its file nodes as test files are created, deleted, or renamed.
- \[[\#14499](https://github.com/posit-dev/positron/issues/14499)\] R: the Test Explorer now refreshes a file’s test items when its contents change outside the editor, such as on a branch switch or an external edit.
- \[[\#7416](https://github.com/posit-dev/positron/issues/7416)\] Python: fixed `help()` raising an error for PyTorch and TensorFlow functions such as `torch.abs`.
- \[[\#12855](https://github.com/posit-dev/positron/issues/12855)\] Python: fixed inline color decorators not appearing for Python code in notebook cells and `.py` files.
- \[[\#12116](https://github.com/posit-dev/positron/issues/12116)\] Python: fixed spurious Python consoles starting during extension activation and after active environment changes.
- \[[\#11281](https://github.com/posit-dev/positron/issues/11281)\] Python: fixed the wrong active interpreter sometimes being used (wrong package-install target, stale diagnostics) when no folder is open, such as after switching between console sessions.
- \[[\#8898](https://github.com/posit-dev/positron/issues/8898)\] Python: fixed seaborn plots stacking elements such as colorbars when the same code is re-run across cells; each run now starts on a fresh figure.
- \[[\#14483](https://github.com/posit-dev/positron/issues/14483)\] Python: fixed Python interpreters intermittently missing from the interpreter list after the first discovery pass at startup, which previously required running *Interpreter: Discover All Interpreters* to resolve.
- \[[\#13691](https://github.com/posit-dev/positron/issues/13691)\] Console: fixed the “Cannot start consoles in restricted mode” message appearing briefly even in trusted workspaces.
- \[[\#13419](https://github.com/posit-dev/positron/issues/13419)\] Console: fixed Shift+Up and Shift+Down in the console extending text selection instead of triggering history navigation.
- \[[\#9500](https://github.com/posit-dev/positron/issues/9500)\] Console: on macOS, user keybindings for Ctrl+N and Ctrl+P now take effect in the console instead of being consumed by history navigation.
- \[[\#7380](https://github.com/posit-dev/positron/issues/7380)\] Console: cleaned up the console keyboard shortcuts. Reverse history search (Ctrl+R), Home, End, and Ctrl+U are now registered keybindings that appear in the Keyboard Shortcuts editor and can be reassigned, and the disabled interactive window’s keybindings no longer appear there misleadingly.
- \[[\#13991](https://github.com/posit-dev/positron/issues/13991), [\#11772](https://github.com/posit-dev/positron/issues/11772)\] Console: clicking the console now moves the cursor to the input even when the last line is not visible, and no longer jumps the viewport to the cursor when you have scrolled up to view output.
- \[[\#13532](https://github.com/posit-dev/positron/issues/13532)\] Console: fixed new windows sometimes opening with the Terminal focused in the Panel instead of the Console.
- \[[\#14155](https://github.com/posit-dev/positron/issues/14155)\] Console: fixed odd spacing around the **Start Session** button shown in an empty console.
- \[[\#13925](https://github.com/posit-dev/positron/issues/13925)\] Console: fixed the console intermittently losing its input prompt and no longer accepting input until the window was reloaded.
- \[[\#14131](https://github.com/posit-dev/positron/issues/14131)\] Plots: fixed removing a single plot from the gallery hiding the entire gallery.
- \[[\#13066](https://github.com/posit-dev/positron/issues/13066)\] Plots: fixed a pre-rendering issue that could cause a plot to miss a re-render after an update.
- \[[\#12124](https://github.com/posit-dev/positron/issues/12124)\] Variables: fixed the Variables pane rendering as empty after being dragged into a different view container.
- \[[\#13949](https://github.com/posit-dev/positron/issues/13949)\] Interpreter: fixed environment module interpreters failing to start a session on systems where the `module` command is only available in login shells.
- \[[\#12862](https://github.com/posit-dev/positron/issues/12862)\] Interpreter: fixed interpreters defined via environment modules being shown in the interpreter picker with the wrong source (“System” for R, “Unknown” for Python) instead of “Module”.
- \[[\#13530](https://github.com/posit-dev/positron/issues/13530)\] Workbench: fixed the editor action bar **Save** button staying disabled on web after editing.
- \[[\#13964](https://github.com/posit-dev/positron/issues/13964)\] Workbench: fixed *Show Release Notes* and other docs links not resolving in Workbench.
- \[[\#13451](https://github.com/posit-dev/positron/issues/13451)\] Workbench: fixed the PDF viewer being blocked by content security policy in remote and Workbench browser sessions.
- \[[\#9390](https://github.com/posit-dev/positron/issues/9390)\] Workbench: fixed terminal paste showing the browser’s native **Paste** menu on every Cmd/Ctrl+V in Firefox and Safari on the web.
- \[[\#13123](https://github.com/posit-dev/positron/issues/13123)\] Server: fixed orphaned `kcserver` processes accumulating when the server exits due to a missing or invalid license.
- \[[\#14063](https://github.com/posit-dev/positron/issues/14063)\] Windows: improved error handling for the kernel supervisor so startup failures are easier to diagnose.
- \[[\#13498](https://github.com/posit-dev/positron/issues/13498)\] Extensions: Positron now notifies you when the `EXTENSIONS_GALLERY` environment variable overrides the extension gallery source setting, or when its value cannot be parsed.
- \[[\#12921](https://github.com/posit-dev/positron/issues/12921)\] Help: fixed find in the Help pane so pressing Enter advances to the next match (and Shift+Enter to the previous, wrapping around) without leaving the Find input.
- \[[\#14128](https://github.com/posit-dev/positron/issues/14128)\] Removed the broken “Dark Experimental” and “Light Experimental” themes, which rendered as the default light theme; use the “Dark 2026” and “Light 2026” themes instead.
- \[[\#13711](https://github.com/posit-dev/positron/issues/13711)\] Fixed the interpreter picker in **New Folder from Template** occasionally missing interpreters.
- \[[\#13673](https://github.com/posit-dev/positron/issues/13673)\] Fixed clicking outside a dropdown inside a modal dialog dismissing the entire dialog.
- \[[\#14022](https://github.com/posit-dev/positron/issues/14022)\] Fixed the *Developer: Runtime Startup Diagnostics* report dropping the Discovery Cache section.
- \[[\#13687](https://github.com/posit-dev/positron/issues/13687)\] Fixed the update tooltip to show the Positron version and icon, and updated the release notes editor to use the Positron logo.
- \[[\#13426](https://github.com/posit-dev/positron/issues/13426)\] Standardized the refresh and restart icons across the Console, Variables, and Viewer panes to use the standard refresh icon.
- \[[\#13952](https://github.com/posit-dev/positron/issues/13952)\] Fixed a misleading `startup_environment_arg` warning appearing during normal kernel startup.
- \[[\#14036](https://github.com/posit-dev/positron/issues/14036)\] Fixed an unexpected `snowflake.log` file appearing in the user’s home directory on Linux.
- \[[\#14418](https://github.com/posit-dev/positron/issues/14418)\] Fixed the accept and discard buttons in the save-conflict editor doing nothing when clicked.
- \[[\#14386](https://github.com/posit-dev/positron/issues/14386)\] Fixed reconnecting to a kernel supervisor failing with `HTTP 401` when a different server was answering at the same address, which left the session unrecoverable; this was most common when returning to a long-idle Posit Workbench session.

#### Dependencies

- Updated `code-oss` upstream to v1.118.0.

## Older releases

Older releases [are available on GitHub](https://github.com/posit-dev/positron/releases), and you can also find the [release notes for previous versions](release-notes.llms.md#older-releases).
