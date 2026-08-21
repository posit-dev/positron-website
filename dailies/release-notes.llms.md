# Release Notes

View release notes for all Positron versions. Track new features, bug fixes, and improvements across monthly releases.

## Latest release

The current release of Positron is 2026.08.1-2.

### Patch notes

The [2026.08.1 patch release](https://github.com/posit-dev/positron/releases/tag/2026.08.1-2) (2026-08-10) fixes problems with autoupdating on Windows.

### Release highlights

Welcome to the 2026.08.0 release of Positron!

- [Data Connections](#data-connections)
- [Inline output for Quarto](#inline-output-for-quarto)
- [AI model providers](#ai-model-providers)
- [Install missing packages](#install-missing-packages)
- [Performance and memory](#performance-and-memory)

#### Data Connections

Data Connections is our new way to work with database-like resources in Positron, from local files and database servers to cloud data warehouses. It is currently available as a preview feature, and you can enable it with the [`dataConnections.enabled`](positron://settings/dataConnections.enabled) setting. This release more than doubles the number of data sources you can reach. Amazon Redshift, Snowflake, Databricks, and Posit Connect pins join the existing DuckDB, PostgreSQL, and SQLite support.

![Browsing the schemas and tables of a DuckDB connection in the Data Connections panel, then opening a table in the Data Explorer to see its column profiles and data.](https://cdn.posit.co/positron/releases/release-notes/assets/2026-08-data-connections.gif)

The panel itself is more capable as well. **Refresh** and **Refresh All** reload the tree while preserving what you have expanded, briefly highlighting the rows that were reloaded. Open connections now show an indicator. Collapsing a connection keeps it open while Data Explorers previewed from it are still open. Removing a connection asks for confirmation and reports how many Data Explorers will close with it.

Data Connections is still an experimental preview, and your feedback continues to shape it. Tell us which databases and warehouses you need, and anything confusing, missing, or broken, in the [Data Connections discussion](https://github.com/posit-dev/positron/discussions/14571).

#### Inline output for Quarto

[Inline output for `.qmd` documents](https://positron.posit.co/quarto-inline-output) came out of preview last release, and this release brings you a substantial round of polish for this way of working. Be aware that the Quarto settings have moved into a dedicated `quarto.*` namespace with its own group in the Settings editor. The previous `positron.quarto.*` keys still work but are deprecated, and Positron will prompt you to update your settings.

Before a kernel starts, the kernel status names the interpreter it will start and offers an explicit **Start Kernel** action. When a cell fails, **Fix** and **Explain** buttons send the error to [Posit Assistant](https://assistant.posit.co/), matching the Positron notebook experience. The editor also scrolls to reveal output as it is produced, which you can turn off with the new [`quarto.inlineOutput.autoScroll`](positron://settings/quarto.inlineOutput.autoScroll) setting.

Output renders more faithfully as well. Running a cell now tells you much more about what is happening, as the editor gutter shows per-statement progress, so you can see which statement is currently executing. Positron draws images at your display’s pixel ratio, so plots are sharp on retina screens, and Python figures now respect the `fig-width` and `fig-height` cell options.

HTML widgets no longer stick in the editor corner when you scroll past them, or trap scrolling instead of letting the document scroll. HTML widgets no longer render as raw HTML after a reload, and collapsed output no longer springs back open when its cell re-runs. Running code in a Quarto document also pins the editor tab now, so Positron does not silently close the document and its session when you open another file.

#### AI model providers

Positron now reads AI model provider configuration from a single `providers.json` file rather than a scattered set of settings. The new release will migrate your existing configuration automatically when you start it, and deprecates the `authentication.*` and `positron.assistant.provider.*.enable` settings in favor of it. Two new commands give you direct access: *Open AI Provider Settings (JSON)* opens `providers.json` from the Command Palette, and *Migrate Provider Settings to providers.json* runs the migration on demand.

#### Install missing packages

Positron now notices when your code refers to a package you do not have installed and offers to install it for you. The prompt appears for packages referenced by your scripts and notebooks in both R and Python. A `library()` or `import` call for something missing becomes a single click instead of an error you have to go resolve by hand.

#### Performance and memory

We continue to invest in the memory footprint, performance, and reliability of Positron. Several components now load only when they are actually needed, and turning off [`ai.enabled`](positron://settings/ai.enabled) now means Positron never loads some heavy AI-related components at all. We fixed a cluster of long-standing reliability problems around session restarts and lifecycles.

Startup and editing are faster as well. R and Python kernels start much faster on Windows systems with aggressive antivirus software. The interpreter session picker appears immediately instead of waiting for interpreter discovery to finish. We also fixed slow typing, formatting, and saving in long R and Python files.

### Changelog

#### New features

- \[[\#14654](https://github.com/posit-dev/positron/issues/14654)\] Connections: added an Amazon Redshift data connection driver, with user and password authentication, SSL on by default, schema and table browsing, cross-database browsing on RA3 and Serverless clusters. Positron generates connection code for `redshift_connector` (Python) and DBI with RPostgres (R).
- \[[\#14650](https://github.com/posit-dev/positron/issues/14650)\] Connections: added a Snowflake data connection driver with full Data Explorer support (filters, sorts, column profiles, and export) and four authentication mechanisms: key pair, OAuth client credentials, a programmatic access token, and a named connection from `connections.toml`.
- \[[\#14959](https://github.com/posit-dev/positron/issues/14959)\] Connections: added a Databricks data connection driver as a preview, with personal access token, interactive browser, and service principal authentication, Unity Catalog and Volumes browsing, and Data Explorer preview of tables, views, and columns.
- \[[\#14663](https://github.com/posit-dev/positron/issues/14663)\] Connections: added a Connect pins driver for browsing pins on a Connect server, including each pin’s versions in the tree with the active version marked. The driver supports browser and environment variable sign-in, and previewing tabular (Parquet and CSV) pins in the Data Explorer.
- \[[\#14624](https://github.com/posit-dev/positron/issues/14624)\] Connections: added **Refresh** and **Refresh All** actions to the Data Connections panel. Refreshing preserves the expanded state of the tree and briefly highlights the rows that were reloaded.
- \[[\#14623](https://github.com/posit-dev/positron/issues/14623)\] Connections: data connection entries now show an indicator while a connection is open. Collapsing a connection keeps it open while Data Explorers previewed from it are still open, and removing a connection asks for confirmation and reports how many open Data Explorers will close with it.
- \[[\#14728](https://github.com/posit-dev/positron/issues/14728)\] Connections: PostgreSQL connections can now omit the database to connect in server mode and browse all databases on the server.
- \[[\#14599](https://github.com/posit-dev/positron/issues/14599)\] Connections: added a **Browse** button to file fields in the Data Connections dialog for selecting local database files such as DuckDB and SQLite, with driver-declared file type filters.
- \[[\#14922](https://github.com/posit-dev/positron/issues/14922)\] Connections: Positron now remembers your preferred connection code package (such as SQLAlchemy or sqlite3) per data connection and language across sessions.
- \[[\#12841](https://github.com/posit-dev/positron/issues/12841)\] Notebooks: added **Save Image As** and **Open Output in New Tab** actions for image outputs, matching Quarto inline output.
- \[[\#14301](https://github.com/posit-dev/positron/issues/14301)\] Quarto: settings now live in the `quarto.*` namespace with a dedicated Quarto group in the Settings editor. The previous `positron.quarto.*` keys still work but are deprecated.
- \[[\#13505](https://github.com/posit-dev/positron/issues/13505)\] Quarto: the editor gutter now shows per-statement execution progress within a running cell, indicating which statement is currently executing.
- \[[\#14185](https://github.com/posit-dev/positron/pull/14185)\] Quarto: inline output now shows the output of each individual R expression when running a cell, rather than only the last one (thanks to @metehankaygsz).
- \[[\#13228](https://github.com/posit-dev/positron/issues/13228)\] Quarto: inline output errors now show **Fix** and **Explain** buttons that send the error to Posit Assistant, matching Positron notebooks.
- \[[\#14659](https://github.com/posit-dev/positron/issues/14659)\] Quarto: the editor now scrolls to reveal inline cell output as it is produced, controlled by the new [`quarto.inlineOutput.autoScroll`](positron://settings/quarto.inlineOutput.autoScroll) setting. This also applies to R Markdown documents.
- \[[\#14558](https://github.com/posit-dev/positron/issues/14558)\] Quarto: the kernel status now names the interpreter that will start and offers an explicit **Start Kernel** action.
- \[[\#15183](https://github.com/posit-dev/positron/issues/15183)\] Quarto: inline output now renders images at the display’s pixel ratio, so plots are sharp on retina screens.
- \[[\#14710](https://github.com/posit-dev/positron/issues/14710), [\#14708](https://github.com/posit-dev/positron/issues/14708)\] Assistant: Positron now reads AI provider configuration from `providers.json`, and migrates existing provider settings to it automatically on startup. Added an *Open AI Provider Settings (JSON)* command to open the file from the Command Palette and a *Migrate Provider Settings to providers.json* command to run the migration on demand. The `authentication.*` and `positron.assistant.provider.*.enable` settings are deprecated.
- \[[\#14818](https://github.com/posit-dev/positron/issues/14818)\] Assistant: added a **Configure LLM Providers** modal for connecting to and managing AI model providers, behind a hidden `assistant.newProviderModal` setting.
- \[[\#8612](https://github.com/posit-dev/positron/issues/8612)\] Assistant: added a Databricks authentication provider so you can use models hosted on Databricks Model Serving, signing in with either browser-based OAuth or a personal access token. This provider is experimental and off by default. Enable it with the `assistant.provider.databricks.enabled` setting.
- \[[\#15117](https://github.com/posit-dev/positron/issues/15117)\] Assistant: added an *AI: Create Diagnostic Report* command that collects AI settings, provider and model state, and recent AI logs into a single report for troubleshooting.
- \[[\#14638](https://github.com/posit-dev/positron/issues/14638)\] Assistant: Positron core now provides assistant context (runtime sessions, variables, and code execution) to Copilot Chat, instead of a separate extension.
- \[[\#4071](https://github.com/posit-dev/positron/issues/4071)\] Packages: Positron now prompts to install packages that are referenced by your scripts and notebooks but are not installed.
- \[[\#14675](https://github.com/posit-dev/positron/issues/14675)\] Packages: missing-package install prompts (the editor and notebook badge, the Command Palette commands, and the console error install suggestion) now work for any language runtime that implements the capability, rather than being hardcoded to Python and R.
- \[[\#2974](https://github.com/posit-dev/positron/issues/2974)\] Data Explorer: Cmd/Ctrl+Click a data frame in the editor to open it in the Data Explorer, when the RStudio keymap is enabled.
- \[[\#15226](https://github.com/posit-dev/positron/pull/15226)\] R: the R language engine now downloads and caches package sources on disk, so navigating to the definition of a package function shows you the actual source with full context and comments. This also lets the analysis engine discover much more about how the code you use works, which will be the basis for more sophisticated diagnostics in the future. You can disable source fetching with the new `oak.sourceFetching.enabled` setting.
- \[[\#15280](https://github.com/posit-dev/positron/pull/15280)\] R: improved symbol navigation and renaming. Symbols no longer escape their local scope in `testthat::test_that()`, `shiny::reactive()`, and other well-known non-standard evaluation functions. Unquoted `.()` parts of `quote()` and `bquote()` now participate in symbol resolution, as do the substituted parts of `substitute()`. Navigation and renaming also understand custom assignment calls and operators such as `assign()`, `delayedAssign()`, `%<>%` from magrittr, and `:=` from S7. Positron also recognizes `library()`, `require()`, and `source()` calls semantically.
- \[[\#14790](https://github.com/posit-dev/positron/issues/14790)\] R: symbol navigation and renaming now understand more of the ways code gets loaded. Files in an `R/` folder are treated as an alphabetical collation unless a more precise loading context is found, so functions in sibling files can see each other. Directory sourcing with `targets::tar_source()` and `sourceDir()` is supported, sourced files see the context inherited from the `source()` location, and Shiny app auto-loading is understood.
- \[[\#15019](https://github.com/posit-dev/positron/issues/15019)\] R: the test explorer now clears existing test statuses at the start of a partial or full run, so you no longer see a mix of current and stale results. Runs that finish uncleanly reveal more actionable information in the **Test Results** panel.
- \[[\#15130](https://github.com/posit-dev/positron/issues/15130)\] R: the test explorer now supports **Cancel Test Run**.
- \[[\#15259](https://github.com/posit-dev/positron/issues/15259)\] R: a lone `#| fig-width` or `#| fig-height` cell option now resizes plots, rather than falling back to the default size.
- \[[\#12660](https://github.com/posit-dev/positron/issues/12660)\] Python: figures in Quarto inline output now respect the `fig-width` and `fig-height` cell options, and render at the display’s pixel ratio.
- \[[\#14352](https://github.com/posit-dev/positron/issues/14352)\] Python: added a **Create Python Environment** item to the **Start Session** dropdown.
- \[[\#14570](https://github.com/posit-dev/positron/issues/14570)\] Help: added **Show Help at Cursor** to the editor context menu.
- \[[\#14685](https://github.com/posit-dev/positron/pull/14685)\] Extensions: added support for configuring a custom Open VSX-compatible extension gallery, such as a self-hosted Posit Package Manager, via the **Extension Gallery Source** and **Custom Gallery URL** settings.
- \[[\#15031](https://github.com/posit-dev/positron/issues/15031)\] Update notifications can now be muted, either from the gear menu on the notification or with the *Notifications: Toggle Do Not Disturb Mode By Source* command.
- \[[\#1507](https://github.com/posit-dev/positron/issues/1507)\] API: added `positron.window.activeConsoleEditor` and `onDidChangeActiveConsoleEditor`, which expose the active console input as a `vscode.TextEditor` so extensions can read and edit console text with the standard editor API.
- \[[\#14181](https://github.com/posit-dev/positron/issues/14181)\] API: added a `whenBusy` option to `positron.runtime.evaluateCode`, a synchronous `getRuntimeState()` accessor, and `onDidDisconnect` and `onDidReconnect` events on language runtime session handles.
- \[[\#14299](https://github.com/posit-dev/positron/issues/14299)\] API: added a `positron.workspace.registerConfigurationMigrations` API for extensions to migrate legacy configuration keys.

#### Bug fixes

- \[[\#14189](https://github.com/posit-dev/positron/issues/14189)\] Notebooks: restored hover tooltips, with keybinding hints, on the Find and Replace widget buttons.
- \[[\#12887](https://github.com/posit-dev/positron/issues/12887)\] Notebooks: Positron now disposes orphaned overlay webviews (interactive plots and raw HTML) when their outputs are cleared, their cell is deleted, or the cell is re-run.
- \[[\#14085](https://github.com/posit-dev/positron/issues/14085), [\#14656](https://github.com/posit-dev/positron/issues/14656)\] Notebooks: fixed clicks in a cell taller than the viewport placing the cursor on the wrong line, and jumping the scroll position to the top of the cell.
- \[[\#11142](https://github.com/posit-dev/positron/issues/11142)\] Notebooks: plots from a notebook console now appear in the Plots pane at a usable size, and the **Inspect** gesture works.
- \[[\#15006](https://github.com/posit-dev/positron/issues/15006)\] Notebooks: fixed the kernel status showing the wrong kernel after a notebook is moved to another editor group.
- \[[\#13978](https://github.com/posit-dev/positron/issues/13978)\] Quarto: fixed inline output webviews sticking in the editor corner when you scroll past the output.
- \[[\#14620](https://github.com/posit-dev/positron/issues/14620)\] Quarto: fixed inline output HTML widgets trapping scroll instead of letting the document scroll.
- \[[\#14559](https://github.com/posit-dev/positron/issues/14559)\] Quarto: fixed R HTML widgets in inline output rendering as raw HTML after a reload or reopen.
- \[[\#13613](https://github.com/posit-dev/positron/issues/13613)\] Quarto: fixed running code in documents with inline output enabled and a custom Jupyter kernelspec name in the YAML header.
- \[[\#14736](https://github.com/posit-dev/positron/issues/14736)\] Quarto: running code in a document now pins its editor tab, so the document and its runtime session are not silently closed when you open another file.
- \[[\#15205](https://github.com/posit-dev/positron/pull/15205)\] Quarto: collapsing inline output while a cell is re-running no longer springs back open when the new output arrives.
- \[[\#15275](https://github.com/posit-dev/positron/issues/15275)\] Quarto: opening an inline output plot in a new tab no longer leaves a temporary image file in the project directory.
- \[[\#15278](https://github.com/posit-dev/positron/pull/15278)\] Quarto: fixed opening Scalable Vector Graphics (SVG) output from inline output in a new tab.
- \[[\#15331](https://github.com/posit-dev/positron/pull/15331)\] Quarto: inline output no longer disappears after a window reload when an untitled document was saved with **Save As**.
- \[[\#15279](https://github.com/posit-dev/positron/issues/15279)\] Plots: fixed **Save Plot** doing nothing and **Copy Plot** failing for SVG plots.
- \[[\#14546](https://github.com/posit-dev/positron/issues/14546)\] Assistant: fixed Bedrock ignoring the configured AWS region when signing in.
- \[[\#12096](https://github.com/posit-dev/positron/issues/12096)\] Assistant: notebook tools now send SVG cell outputs to the model as rasterized PNG images instead of an unusable binary attachment.
- \[[\#14250](https://github.com/posit-dev/positron/issues/14250)\] Assistant: notebook tools now explain how to reopen a notebook in the Positron Notebook Editor when it is open in the built-in notebook editor, instead of failing with “no notebook is open”.
- \[[\#14762](https://github.com/posit-dev/positron/issues/14762)\] Assistant: fixed a failure to find an open Positron notebook when the notebook is not the active editor pane, such as after opening a Data Explorer or moving focus to another editor.
- \[[\#14735](https://github.com/posit-dev/positron/pull/14735)\] Assistant: the **Explain** button on notebook and Quarto error outputs now asks the assistant to explain the error without also attempting to fix it.
- \[[\#14369](https://github.com/posit-dev/positron/issues/14369)\] Assistant: Positron now shows the GitHub Copilot completions status icon by default, and using a GitHub account for AI features requires additional opt-in.
- \[[\#14989](https://github.com/posit-dev/positron/issues/14989)\] Assistant: Copilot usage (chat and premium request quotas) now appears in the status bar dialog even when the built-in Copilot chat UI is hidden.
- \[[\#15171](https://github.com/posit-dev/positron/issues/15171)\] Assistant: the AI provider settings migration now writes versioned base URLs (such as `https://api.anthropic.com/v1`) instead of copying bare hosts verbatim into `providers.json`.
- \[[\#14677](https://github.com/posit-dev/positron/pull/14677)\] Assistant: model providers registered with no authentication method now show a base URL input in the configuration modal.
- \[[\#15286](https://github.com/posit-dev/positron/pull/15286)\] Assistant: quick-fix attachment chips no longer expose `.txt` implementation-style names for console, notebook cell, and Quarto error attachments.
- \[[\#15306](https://github.com/posit-dev/positron/issues/15306)\] Assistant: fixed non-local model providers not appearing when you are connected to a remote session over Windows Subsystem for Linux (WSL) or Remote-SSH.
- \[[\#15095](https://github.com/posit-dev/positron/pull/15095)\] Assistant: removed the unused `chat.useCopilotParticipantsWithOtherProviders` setting.
- \[[\#14686](https://github.com/posit-dev/positron/issues/14686)\] Connections: fixed opening the same DuckDB database file from more than one saved connection, which previously failed for every connection after the first.
- \[[\#14631](https://github.com/posit-dev/positron/issues/14631)\] Connections: added padding to the datatype label so it no longer sits against the panel’s right edge and scrollbar.
- \[[\#14904](https://github.com/posit-dev/positron/issues/14904)\] Connections: fixed the spacing of wrapped package names in the package picker of the **Connect With** dialog.
- \[[\#14623](https://github.com/posit-dev/positron/issues/14623)\] Connections: removing a data connection now closes the underlying connection instead of leaving it open for the rest of the session.
- \[[\#15189](https://github.com/posit-dev/positron/issues/15189)\] Data Explorer: fixed intermittently failing to open a table or column from the Data Connections tree and leaving an empty editor. Also fixed columns not being auto-sized when opening a table or column, and column widths not adjusting when the editor font changes.
- \[[\#12547](https://github.com/posit-dev/positron/issues/12547)\] Data Explorer: fixed the grid remaining blank after a failed backend request, and fixed a blank grid when viewing an R matrix that has row names.
- \[[\#15042](https://github.com/posit-dev/positron/issues/15042)\] Data Explorer: fixed failing to open on Intel (x64) macOS with a missing `@duckdb/node-bindings-darwin-x64/duckdb.node` error.
- \[[\#15215](https://github.com/posit-dev/positron/pull/15215)\] Data Explorer: column headers no longer briefly display `<empty>` while a slow connection’s schema is loading.
- \[[\#13902](https://github.com/posit-dev/positron/issues/13902)\] Data Explorer: fixed columns and rows showing through pinned columns and pinned rows while scrolling.
- \[[\#14294](https://github.com/posit-dev/positron/issues/14294)\] Packages: **Refresh** now recomputes outdated packages live instead of showing stale cached indicators, and the pane no longer reports available updates for R packages that have only been rebuilt at the same version.
- \[[\#3817](https://github.com/posit-dev/positron/issues/3817)\] R: the parallel package, which is not supported in Positron, now fails with an informative error that recommends using PSOCK clusters, `future::multisession()`, mirai, or `purrr::in_parallel()`.
- \[[\#12840](https://github.com/posit-dev/positron/issues/12840)\] R: Positron help pages no longer include the new table of contents added in R 4.6.
- \[[\#7385](https://github.com/posit-dev/positron/issues/7385), [\#8167](https://github.com/posit-dev/positron/issues/8167)\] R: fixed the Data Explorer being blank when viewing objects piped with `%>%`.
- \[[\#14481](https://github.com/posit-dev/positron/issues/14481)\] R: fixed hangs with the Evaluate pane of the debugger. An expression that takes a long time to evaluate, or that loops forever, is now cancelled after one second.
- \[[\#14909](https://github.com/posit-dev/positron/issues/14909)\] R: fixed a usability issue in completions of string-quoted names in brackets.
- \[[\#14851](https://github.com/posit-dev/positron/issues/14851), [\#3599](https://github.com/posit-dev/positron/issues/3599)\] R: argument names in function hover docs are now top-aligned with the first line of their description, matching the Help pane.
- \[[\#14426](https://github.com/posit-dev/positron/issues/14426)\] R: fixed duplicate “Load R Object” prompts when viewing the diff of a modified `.rds` file.
- \[[\#15297](https://github.com/posit-dev/positron/issues/15297)\] R: fixed the interpreter architecture being misdetected as x64 for native arm64 conda-forge R on macOS.
- \[[\#15300](https://github.com/posit-dev/positron/issues/15300)\] R: interpreters installed by a Homebrew cask, such as miniforge, are no longer labeled “(Homebrew)”, and genuine Homebrew installs on Intel macOS are no longer labeled “System”.
- \[[\#7403](https://github.com/posit-dev/positron/issues/7403)\] R: the R version used in the Terminal now matches the R version selected in the Console, including `PATH`, `R_HOME`, and `QUARTO_R`.
- \[[\#14655](https://github.com/posit-dev/positron/pull/14655)\] Python: fixed local modules (sibling files and packages) being misreported as missing, installable packages when running a script.
- \[[\#14646](https://github.com/posit-dev/positron/pull/14646)\] Python: `import ibis` now suggests installing `ibis-framework`.
- \[[\#14493](https://github.com/posit-dev/positron/issues/14493)\] Python: fixed distinct virtual environments that share a base interpreter being collapsed into one entry in the interpreter list, and fixed the same uv-managed interpreter appearing multiple times when reached through a symlinked version directory.
- \[[\#14556](https://github.com/posit-dev/positron/issues/14556)\] Python: uv environments are labeled “Unknown” less often.
- \[[\#14912](https://github.com/posit-dev/positron/issues/14912)\] Python: uv-managed standalone Python installs are now classified as global interpreters instead of uv environments.
- \[[\#15028](https://github.com/posit-dev/positron/issues/15028)\] Python: fixed an intermittent “Error while creating virtual environment” when creating a venv, even though the environment was created successfully.
- \[[\#15167](https://github.com/posit-dev/positron/issues/15167)\] Python: fixed Positron not offering to create an environment for a `pyproject.toml` without a `[build-system]` table.
- \[[\#15153](https://github.com/posit-dev/positron/issues/15153)\] Python: fixed a web and remote failure where creating a new Python environment via the **New Folder** flow sometimes left the console without a session.
- \[[\#15254](https://github.com/posit-dev/positron/issues/15254)\] Python: fixed `matplotlib_inline.backend_inline.set_matplotlib_formats(...)` breaking figure rendering.
- \[[\#15253](https://github.com/posit-dev/positron/issues/15253)\] Python: fixed `%matplotlib` to toggle the matplotlib backend between the Plots pane and an interactive backend such as `qt`, and back again.
- \[[\#14267](https://github.com/posit-dev/positron/issues/14267)\] Console: adding a console while a notebook console is the active session now starts a new console session instead of showing an error.
- \[[\#14983](https://github.com/posit-dev/positron/issues/14983)\] Console: the session information dialog now opens immediately instead of waiting on the output channels lookup, so it no longer fails to open under load.
- \[[\#10016](https://github.com/posit-dev/positron/issues/10016)\] Interpreter: fixed a cluster of session restart failures. Python and R sessions now restart after an extension host restart, the console reliably returns after an interpreter restart, the notebook kernel status badge no longer sticks on “Disconnected”, and restart works when the Kernel Supervisor shutdown timeout is set to persist sessions.
- \[[\#14688](https://github.com/posit-dev/positron/issues/14688)\] Interpreter: fixed the suggested interpreter appearing twice in the **New Console Session** quick pick.
- \[[\#14991](https://github.com/posit-dev/positron/issues/14991)\] Interpreter: the workspace default interpreter now starts reliably when its environment is slow to resolve at startup.
- \[[\#14868](https://github.com/posit-dev/positron/pull/14868)\] Interpreter: the session picker now appears immediately instead of waiting on interpreter discovery, fixing a case where the session button sometimes appeared unresponsive right after opening a workspace.
- \[[\#15336](https://github.com/posit-dev/positron/pull/15336)\] Interpreter: fixed intermittent “No language runtime with id … was found” failures when starting a kernel after a window reload.
- \[[\#15335](https://github.com/posit-dev/positron/pull/15335)\] Workbench: access to `/proxy/` ports in Posit Workbench is now isolated to the user of the requesting session on multi-user hosts.
- \[[\#13388](https://github.com/posit-dev/positron/issues/13388)\] Windows: improved R and Python startup time on systems with aggressive antivirus software.
- \[[\#14671](https://github.com/posit-dev/positron/issues/14671)\] Windows: fixed the kernel supervisor failing to start when [`kernelSupervisor.shutdownTimeout`](positron://settings/kernelSupervisor.shutdownTimeout) is non-default on installations with spaces in the path.
- \[[\#8306](https://github.com/posit-dev/positron/issues/8306)\] Linux: **Download Update** now fetches the specific build detected by the update check, including on the dailies channel, instead of opening the website download page.
- \[[\#14685](https://github.com/posit-dev/positron/pull/14685)\] Extensions: a non-default extension gallery (custom or Open VSX) no longer silently falls back to the default gallery when a resource request fails.
- \[[\#13854](https://github.com/posit-dev/positron/issues/13854)\] Fixed tooltips not appearing for action buttons in view and sidebar headers.
- \[[\#14810](https://github.com/posit-dev/positron/issues/14810)\] Fixed links on the Help pane welcome page not opening when clicked.
- \[[\#14990](https://github.com/posit-dev/positron/issues/14990), [\#15250](https://github.com/posit-dev/positron/issues/15250)\] Fixed slow typing, formatting, and saving in long R and Python files.
- \[[\#14781](https://github.com/posit-dev/positron/issues/14781), [\#14826](https://github.com/posit-dev/positron/issues/14826)\] Fixed the Positron editor action bar rendering inside the new modal Settings editor as a spurious second row of icons. Also fixed the Quarto kernel badge flipping to “No Kernel” over the modal.
- \[[\#13764](https://github.com/posit-dev/positron/issues/13764)\] Fixed an empty icon column in context menus whose items are checkable but have no icons, such as the Packages pane **Filter** and **Sort** submenus, which pushed the checkmark and label to the right.
- \[[\#998](https://github.com/posit-dev/positron/issues/998)\] Added bottom padding to terminal instances so the prompt is no longer squished against the bottom edge of the pane.
- \[[\#1366](https://github.com/posit-dev/positron/issues/1366)\] Removed the “Copy vscode.dev Link” item from the editor, explorer, editor tab, and line number share menus.
- \[[\#14956](https://github.com/posit-dev/positron/pull/14956)\] Fixed an intermittent issue where the Import VS Code Settings preview sometimes lost its conflict markers before you had a chance to review them.
- \[[\#12942](https://github.com/posit-dev/positron/issues/12942)\] Fixed `runtimePath` containing a `~`-shortened path that broke `execFile` callers. The workbench now computes `runtimeDisplayPath` centrally at runtime registration.
- \[[\#14938](https://github.com/posit-dev/positron/pull/14938)\] Reduced the memory footprint of Positron at startup by only starting the backend for CSV, TSV, and Excel files when it is first used.
- \[[\#14982](https://github.com/posit-dev/positron/pull/14982)\] The experimental Catalog Explorer extension no longer loads on startup when it is disabled, and it loads the Snowflake SDK only when connecting to Snowflake, reducing startup cost and memory footprint.
- \[[\#14899](https://github.com/posit-dev/positron/pull/14899), [\#15008](https://github.com/posit-dev/positron/pull/15008)\] Reduced memory usage when AI features are disabled by not loading Posit Assistant, Copilot, or Next Edit Suggestions unless [`ai.enabled`](positron://settings/ai.enabled) is on.

#### Dependencies

- Updated `code-oss` upstream to v1.124.0.
- Updated bundled Quarto to 1.10.18.
