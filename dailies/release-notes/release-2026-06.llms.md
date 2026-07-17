# 2026.06.0-211 Release Notes

<https://github.com/posit-dev/positron/releases/tag/2026.06.0-211>

Published

June 1, 2026

### Patch notes

The [2026.06.1 patch release](https://github.com/posit-dev/positron/releases/tag/2026.06.1-6) (2026-06-23) provides security vulnerability updates.

### Release highlights

Welcome to the 2026.06.0 release of Positron!

- [Posit Assistant](#posit-assistant)
- [Packages pane improvements](#packages-pane-improvements)
- [Inline output for Quarto](#inline-output-for-quarto)
- [Faster startup](#faster-startup)
- [R language intelligence](#r-language-intelligence)

#### Posit Assistant

Last release we introduced [Posit Assistant](https://assistant.posit.co), our unified, data-science-focused approach to AI assistance. This release continues that work, and we want to give you advance notice that the older Positron Assistant will be deprecated in the next release. If you are still using Positron Assistant, we encourage you to migrate to Posit Assistant now. As a first step, the `positron.assistant.enable` setting is deprecated in favor of [`assistant.enabled`](positron://settings/assistant.enabled), and the Positron Assistant welcome view now points you to Posit Assistant.

Posit Assistant supports the same broad set of providers as Positron Assistant, along with the Posit AI model provider and new experimental support for Google Vertex. [Learn more](https://youtu.be/Y9P2nlFXKnQ) about the differences between the new Posit Assistant and the older Positron Assistant.

![Using Posit Assistant in Positron](https://cdn.posit.co/positron/releases/release-notes/assets/2026-06-posit-assistant.gif)

New in Posit Assistant this release, you can use the Posit AI model provider for Next Edit Suggestions, which propose your likely next change as you edit. You can also access the **Configure Language Model Providers** item in the accounts menu.

#### Packages pane improvements

We introduced the [Packages](https://positron.posit.co/packages-pane) pane last release, and this release makes it more informative and flexible. A **Show Help** button and context menu entry on every package take you straight to its documentation in the [Help pane](https://positron.posit.co/help-pane). You can now combine category filters as an intersection, so you can narrow the list to, for example, packages that are both attached and outdated. A new **Item Size** toggle lets you switch between a compact row view and a richer card view that surfaces package descriptions and other metadata. For R users, the new [`packages.r.installer`](positron://settings/packages.r.installer) setting controls whether installs, updates, and removals use pak, base R, or an automatic choice. The setting that controls the pane has been renamed to [`packages.enabled`](positron://settings/packages.enabled); the previous `positron.packages.enable` setting is deprecated but still honored.

#### Inline output for Quarto

[Inline output for `.qmd` documents](https://positron.posit.co/quarto-inline-output) was one of Positron’s most-requested features ever, and it is now out of preview. A new toolbar button in Quarto documents gives you one-click access to running cells, managing inline output, and showing the console. Inserting code into a Quarto document from the History pane now automatically wraps it in cell markup when you drop it into a prose region. You can opt in to inline output with the [`positron.quarto.inlineOutput.enabled`](positron://settings/positron.quarto.inlineOutput.enabled) setting.

#### Faster startup

We continue to invest in performance improvements, and Positron starts up even faster in this release. Positron now caches previously discovered system interpreters, dramatically speeding up startup in new folders and projects; you can control this with the new [`interpreters.discoveryCache.enabled`](positron://settings/interpreters.discoveryCache.enabled) setting. On Windows, we fixed multi-minute startup delays by skipping slow `PATH` discovery by default, governed by the new [`positron.r.interpreters.pathDiscoveryMode`](positron://settings/positron.r.interpreters.pathDiscoveryMode) setting. We also fixed an occasional hang at “Preparing” when starting Positron after updating to a new version.

#### R language intelligence

Positron’s R language support now understands symbols within a file. You can rename a local symbol and have every use of it updated at once, and Go to Definition and Find References now work for local symbols, so you can jump to where a variable is defined (such as via `<-` or a function parameter) or see everywhere it is used within a function. Renaming symbols across files is not yet supported, but it is coming soon.

### Changelog

#### New features

- \[[\#11708](https://github.com/posit-dev/positron/issues/11708)\] Notebooks: unified the notebook and Quarto kernel selectors with the interpreter selector so they share ordering, grouping, and icons.
- \[[\#11906](https://github.com/posit-dev/positron/issues/11906)\] Notebooks: added a “Change Notebook Session…” entry to the interpreter picker, allowing users to change the runtime for the active notebook editor.
- \[[\#10604](https://github.com/posit-dev/positron/issues/10604)\] Notebooks: render `application/json` outputs as a collapsible tree view with syntax highlighting, plus a **Copy JSON** action to copy formatted JSON output to the clipboard.
- \[[\#12680](https://github.com/posit-dev/positron/issues/12680)\] Notebooks: render bare LaTeX environment blocks (such as `\begin{equation}` and `\begin{align}`) in markdown cells.
- \[[\#12687](https://github.com/posit-dev/positron/issues/12687)\] Notebooks: render `text/latex` outputs (such as from `IPython.display.Math` and `IPython.display.Latex`) using KaTeX.
- \[[\#13174](https://github.com/posit-dev/positron/issues/13174)\] Notebooks: defer kernel startup for notebooks and Quarto documents until you interact with or edit the document, instead of when it is previewed.
- \[[\#10493](https://github.com/posit-dev/positron/issues/10493)\] Notebooks: the **Run All** toolbar button toggles to a **Stop** button while cells are running, so you can interrupt execution from the toolbar.
- \[[\#12434](https://github.com/posit-dev/positron/issues/12434)\] Notebooks: cell outputs can now be focused via Tab or click, enabling Cmd+C to copy a plot image to the clipboard when the output area is active.
- \[[\#12839](https://github.com/posit-dev/positron/issues/12839)\] Notebooks: added a **Toggle Outline** button to the editor action bar, which opens and focuses the Outline view in the Explorer pane.
- \[[\#13795](https://github.com/posit-dev/positron/issues/13795)\] Notebooks: context keys now show descriptions in autocompletion when editing `when` clauses in `keybindings.json` and extension `package.json`.
- \[[\#13321](https://github.com/posit-dev/positron/pull/13321)\] Notebooks: added an experimental **Visualize…** flow (behind [`positron.notebook.experimental`](positron://settings/positron.notebook.experimental)) that turns an inline Data Explorer view into a plotting cell, with code generation for Plotly, Matplotlib, and Seaborn as well as a live chart preview.
- \[[\#13334](https://github.com/posit-dev/positron/issues/13334)\] Assistant: added Posit AI Next Edit Suggestions.
- \[[\#13110](https://github.com/posit-dev/positron/issues/13110)\] Assistant: added a “Configure Language Model Providers” item to the accounts menu.
- \[[\#13664](https://github.com/posit-dev/positron/pull/13664)\] Assistant: added `authentication.<configKey>.customHeaders` settings to attach extra HTTP headers to provider requests.
- \[[\#12270](https://github.com/posit-dev/positron/issues/12270)\] Assistant: added Google Vertex AI as an experimental language model provider (behind [`assistant.provider.googleVertex.enabled`](positron://settings/assistant.provider.googleVertex.enabled)), supporting service-account environment variables and Application Default Credentials.
- \[[\#13543](https://github.com/posit-dev/positron/issues/13543)\] Assistant: updated the Positron Assistant welcome view to direct users to Posit Assistant, and deprecated `positron.assistant.enable` in favor of [`assistant.enabled`](positron://settings/assistant.enabled).
- \[[\#13499](https://github.com/posit-dev/positron/pull/13499), [\#13757](https://github.com/posit-dev/positron/pull/13757)\] Packages: added a **Show Help** button and context menu entry for every package in the Packages pane.
- \[[\#13156](https://github.com/posit-dev/positron/pull/13156)\] Packages: added an **Item Size** toggle to switch the Packages pane between row and card views, and added more package metadata including descriptions.
- \[[\#13759](https://github.com/posit-dev/positron/pull/13759)\] Packages: the Packages pane now supports combining multiple category filters (such as both outdated and attached) as an intersection.
- \[[\#13755](https://github.com/posit-dev/positron/pull/13755)\] Packages: added the [`packages.r.installer`](positron://settings/packages.r.installer) setting to control which installation method (auto, pak, or base R) the Packages pane uses for installing, updating, and removing R packages.
- \[[\#13642](https://github.com/posit-dev/positron/pull/13642)\] Packages: renamed the setting that controls the Packages pane to [`packages.enabled`](positron://settings/packages.enabled). The previous `positron.packages.enable` setting is deprecated but still honored.
- \[[\#12825](https://github.com/posit-dev/positron/issues/12825)\] R: plots created in a loop are now rendered on each iteration rather than all at once at the end.
- \[[\#13749](https://github.com/posit-dev/positron/issues/13749)\] R: you can now rename local symbols in R files. Renaming symbols across files is not yet supported, but is coming soon.
- \[[\#8631](https://github.com/posit-dev/positron/issues/8631)\] R: “Go to Definition” and “Find References” now support local symbols in R files, so you can jump to where a variable is defined (such as via `<-` or a function parameter) or see all references to a variable within a function.
- \[[\#11875](https://github.com/posit-dev/positron/issues/11875)\] R: the *R: Install R Package and Restart R* command now defaults to `devtools::install(build = FALSE)` instead of `pak::local_install(upgrade = FALSE)`. The [`positron.r.localPackageInstallMethod`](positron://settings/positron.r.localPackageInstallMethod) setting now accepts `"devtools"` or `"base"`.
- \[[\#12149](https://github.com/posit-dev/positron/issues/12149)\] Quarto: added a toolbar button in Quarto documents for running cells, managing inline output, and showing the console.
- \[[\#12737](https://github.com/posit-dev/positron/issues/12737)\] Quarto: inserting code into a Quarto document from the History pane now automatically wraps it in cell markup when inserting into a prose region.
- \[[\#6965](https://github.com/posit-dev/positron/issues/6965)\] Python: guide users to create a virtual environment if requirements files are present in a Python workspace.
- \[[\#13501](https://github.com/posit-dev/positron/pull/13501)\] Python: show help pages (such as via `?cowsay`) for packages that have not been imported yet.
- \[[\#13133](https://github.com/posit-dev/positron/issues/13133)\] Interpreter: cache previously discovered system interpreters across windows to dramatically speed up startup in new folders and projects. Caching can be controlled with the new [`interpreters.discoveryCache.enabled`](positron://settings/interpreters.discoveryCache.enabled) setting.
- \[[\#13224](https://github.com/posit-dev/positron/pull/13224)\] Workbench: static files are now served from consistent, session-independent URLs, allowing them to be cached across sessions.
- \[[\#13738](https://github.com/posit-dev/positron/pull/13738)\] Extensions: now send distribution type, Positron version, and update-check trigger as query parameters on extension gallery requests to Posit Public Package Manager (P3M), for load sizing and traffic disambiguation. This can be turned off with the new [`extensions.gallery.sendUsageData`](positron://settings/extensions.gallery.sendUsageData) setting.
- \[[\#13131](https://github.com/posit-dev/positron/issues/13131)\] Moved the **Save File** icon from the global toolbar to the editor action bar.

#### Bug fixes

- \[[\#13420](https://github.com/posit-dev/positron/issues/13420)\] Notebooks: fixed an “InstantiationService has been disposed” error when editing cells after switching tabs.
- \[[\#13393](https://github.com/posit-dev/positron/pull/13393)\] Notebooks: fixed “Save as SVG/PNG” silently failing for Altair/Vega plots.
- \[[\#13558](https://github.com/posit-dev/positron/pull/13558)\] Notebooks: fixed scrolling when running in web mode (Workbench).
- \[[\#12437](https://github.com/posit-dev/positron/issues/12437)\] Notebooks: fixed rendered markdown cells not respecting the [`notebook.markup.fontSize`](positron://settings/notebook.markup.fontSize) setting.
- \[[\#11649](https://github.com/posit-dev/positron/issues/11649)\] Notebooks: fixed `execution_count` being null in saved `execute_result` outputs.
- \[[\#11716](https://github.com/posit-dev/positron/issues/11716)\] Notebooks: removed the **Run Dash App** button from the toolbar.
- \[[\#13708](https://github.com/posit-dev/positron/issues/13708)\] Notebooks: fixed `ipydatagrid` and other widget outputs failing to render.
- \[[\#12726](https://github.com/posit-dev/positron/issues/12726)\] Notebooks: fixed showing the focused-cell blue border on multiple cells at once in the Positron Dark theme.
- \[[\#10452](https://github.com/posit-dev/positron/issues/10452)\] Notebooks: fixed `IPython.display.Audio` playback.
- \[[\#12740](https://github.com/posit-dev/positron/issues/12740)\] Notebooks: fixed side-by-side notebooks not distinguishing the focused pane from the unfocused pane; the unfocused pane’s selected cell now shows a muted border and its action bar no longer auto-appears.
- \[[\#10385](https://github.com/posit-dev/positron/issues/10385)\] Notebooks: fixed Escape not cancelling multiple selections.
- \[[\#11555](https://github.com/posit-dev/positron/issues/11555)\] Notebooks: fixed empty notebooks created via Cmd+N not auto-selecting the foreground session’s kernel.
- \[[\#13227](https://github.com/posit-dev/positron/issues/13227)\] Assistant: disabled the initial terminal hint by default.
- \[[\#11452](https://github.com/posit-dev/positron/issues/11452)\] Assistant: fixed `vscode.lm.selectChatModels()` returning no models when another chat-model provider extension throws during activation.
- \[[\#13412](https://github.com/posit-dev/positron/issues/13412)\] Assistant: fixed OpenAI provider connection test errors appearing shortly after activation.
- \[[\#13421](https://github.com/posit-dev/positron/issues/13421), [\#13489](https://github.com/posit-dev/positron/issues/13489)\] Assistant: fixed Custom Provider sign-in against OpenAI-compatible endpoints that reject empty model strings (such as Databricks).
- \[[\#13544](https://github.com/posit-dev/positron/issues/13544)\] Assistant: allowed reading project metadata files in dot-directories like `.github/` and `.vscode/` by default, while still excluding `.env`, SSH keys, and other secret-bearing files.
- \[[\#13556](https://github.com/posit-dev/positron/pull/13556)\] Packages: fixed scrolling issues in the Packages pane on web.
- \[[\#13453](https://github.com/posit-dev/positron/issues/13453)\] Packages: improved the accuracy of the “Outdated” indicator in the Packages pane, so development versions installed from sources like git are no longer incorrectly flagged as outdated.
- \[[\#13395](https://github.com/posit-dev/positron/issues/13395)\] Console: fixed jumpiness when resizing the Console height.
- \[[\#12772](https://github.com/posit-dev/positron/issues/12772)\] Console: fixed the working directory disappearing in the Console tab when it is long or the Console is narrow; it is now truncated and shown on hover.
- \[[\#13456](https://github.com/posit-dev/positron/issues/13456)\] Variables: fixed an unresponsive column resizer in the Variables pane that stopped tracking the pointer after the first move.
- \[[\#12734](https://github.com/posit-dev/positron/issues/12734)\] Variables: improved the layout of the Variables pane action bar at narrower widths.
- \[[\#13179](https://github.com/posit-dev/positron/issues/13179)\] Workbench: fixed an issue causing all links in the Help pane to open in new tabs instead of inside the Help pane.
- \[[\#13359](https://github.com/posit-dev/positron/issues/13359)\] Workbench: fixed the file picker overlapping other panes when advancing in the New Folder from Template flow on web.
- \[[\#12882](https://github.com/posit-dev/positron/issues/12882)\] Windows: fixed auto-update updating the wrong installation when multiple Positrons are installed.
- \[[\#13431](https://github.com/posit-dev/positron/issues/13431)\] Windows: fixed “Open” events initiated by a runtime, such as `usethis::use_r()` to open a file, failing with UNC paths.
- \[[\#13234](https://github.com/posit-dev/positron/issues/13234)\] macOS: fixed Cmd+C and Cmd+A not working when the PDF viewer has focus.
- \[[\#13369](https://github.com/posit-dev/positron/issues/13369), [\#13372](https://github.com/posit-dev/positron/issues/13372)\] macOS: fixed architecture-specific builds selecting arm64 binaries on Intel Macs.
- \[[\#12999](https://github.com/posit-dev/positron/issues/12999)\] R: fixed multi-minute startup delays by skipping slow `PATH` discovery on Windows by default. The new [`positron.r.interpreters.pathDiscoveryMode`](positron://settings/positron.r.interpreters.pathDiscoveryMode) setting controls this behavior.
- \[[\#9044](https://github.com/posit-dev/positron/issues/9044)\] R: fixed `()` inserted as part of a function completion, such as in `.libPaths()`, not being treated as an auto-closing pair; backspace once again removes `()`, not just `(`.
- \[[\#13242](https://github.com/posit-dev/positron/issues/13242)\] Quarto: fixed inline output appearing in the Diff view.
- \[[\#13518](https://github.com/posit-dev/positron/issues/13518)\] Python: removed the *Python: Install Python Packages* entry from the Command Palette, since it cannot be used that way.
- \[[\#13068](https://github.com/posit-dev/positron/issues/13068)\] Plots and Viewer: consolidated the **Open in…** actions in the Plots and Viewer panes into a single dropdown with consistent placement and iconography.
- \[[\#13230](https://github.com/posit-dev/positron/issues/13230)\] Themes: replaced upstream “Experimental” color themes with Positron-branded variants in the theme picker.
- \[[\#13415](https://github.com/posit-dev/positron/issues/13415)\] Extensions: fixed the `EXTENSIONS_GALLERY` environment variable not overriding the extension gallery URL.
- \[[\#13134](https://github.com/posit-dev/positron/issues/13134)\] Linux: fixed the Positron `.deb` uninstaller removing Visual Studio Code’s APT sources and signing key.
- \[[\#13113](https://github.com/posit-dev/positron/issues/13113)\] Fixed the [`workbench.topActionBar.visible`](positron://settings/workbench.topActionBar.visible) setting not hiding and showing the top action bar at runtime.
- \[[\#10149](https://github.com/posit-dev/positron/issues/10149)\] Fixed the [`window.commandCenter`](positron://settings/window.commandCenter) setting being ignored; it can now be enabled to show the command center in the title bar.
- \[[\#11629](https://github.com/posit-dev/positron/issues/11629)\] Fixed the [`workbench.secondarySideBar.defaultVisibility`](positron://settings/workbench.secondarySideBar.defaultVisibility) setting not being honored when explicitly configured.
- \[[\#7644](https://github.com/posit-dev/positron/issues/7644)\] Fixed the [`workbench.secondarySideBar.showLabel`](positron://settings/workbench.secondarySideBar.showLabel) setting not being respected, so Secondary Side Bar items can now render as icons.
- \[[\#12865](https://github.com/posit-dev/positron/issues/12865)\] Fixed the command *Developer: Runtime Startup Diagnostics* hanging when the extension host is unresponsive.
- \[[\#13343](https://github.com/posit-dev/positron/pull/13343)\] Fixed file icon size and alignment in the console tab list and session picker so icons render consistently across file icon themes.
- \[[\#13040](https://github.com/posit-dev/positron/issues/13040)\] Standardized clear and delete icons across pane action bars: filter inputs and notebook output-clearing use the clear-all icon, while destructive actions in the Variables, Plots, Console, and History panes use a trash icon.
- \[[\#13303](https://github.com/posit-dev/positron/issues/13303)\] Removed the “Editor Actions” toggle entry from the title bar context menu.
- \[[\#13550](https://github.com/posit-dev/positron/issues/13550)\] Clarified in the workspace trust editor and startup dialog that workspace trust gates Python and R sessions and Posit Assistant.
- \[[\#13139](https://github.com/posit-dev/positron/issues/13139)\] Fixed completions and diagnostics failing in IPv6-only environments.
- \[[\#12864](https://github.com/posit-dev/positron/issues/12864)\] Fixed an occasional hang at “Preparing” when starting Positron after updating to a new version.
- \[[\#12204](https://github.com/posit-dev/positron/issues/12204)\] Fixed right-click paste in “New Folder from Git” and other Positron text-input dialogs.

#### Dependencies

- Updated `code-oss` upstream to v1.111.0.
- Updated bundled Quarto to 1.9.38.
