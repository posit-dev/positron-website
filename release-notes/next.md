### Highlights

#### Improved statement execution for R ✨

The most upvoted issue we addressed this release was about stepping through code with <kbd>Cmd/Ctrl+Enter</kbd> in R scripts and Quarto documents. Previously, if your R script or Quarto document had a syntax error anywhere, even far below your cursor, stepping through code could fail silently or behave unpredictably. This was especially confusing when teaching or during exploratory analysis. Now, code above a syntax error executes reliably. If you try to run code below an error, Positron shows a notification explaining why execution isn't possible and offers a button to jump directly to the problem. This works in R scripts, Quarto documents that use R, and even roxygen2 examples.

#### Integrated PDF viewer 📄

Positron now includes a built-in PDF viewer. Click any PDF in the Explorer and it opens directly in Positron, with no need for external applications or additional extensions. The viewer automatically matches your IDE theme (light or dark) and updates when you switch themes. This works in Positron Desktop, Positron Server, and Posit Workbench environments, making it easy to view reports, papers, and documentation alongside your code.

#### Positron Notebook Editor 📓

The Positron Notebook Editor continues to be available for alpha testing and is maturing with new features for data science workflows. Cell outputs for pandas and polars dataframes now render as interactive data grids with scrolling, sorting, and cell selection; you can open any dataframe directly in the Data Explorer with one click. This release also adds the ability to show or hide individual cell outputs, raw cell support for content that shouldn't be executed or rendered, and split/join cell commands with keyboard shortcuts matching Jupyter conventions. Right-click context menus are now available on cells and outputs for quick access to common actions.

<div id="checkbox"></div>

### Changelog

#### New features

- [[#4201](https://github.com/posit-dev/positron/issues/4201)] Added an integrated PDF viewer.
- [[#11081](https://github.com/posit-dev/positron/issues/11081)] Connections Pane: added Redshift connection drivers for Python with support for Username/Password, IAM, and Okta authentication.
- [[#11582](https://github.com/posit-dev/positron/issues/11582)] Connections Pane: added validation support for connection drivers with inline error display.
- [[#10531](https://github.com/posit-dev/positron/issues/10531)] Assistant: switched Anthropic provider to use Vercel SDK.
- [[#10866](https://github.com/posit-dev/positron/issues/10866)] Assistant: you can now enable or disable individual language model providers via settings.
- [[#11001](https://github.com/posit-dev/positron/issues/11001)] Assistant: improved error handling for exceeding rate limit for Anthropic.
- [[#11675](https://github.com/posit-dev/positron/issues/11675)] Assistant: include user agent for Snowflake Cortex requests.
- [[#11645](https://github.com/posit-dev/positron/issues/11645)] Assistant: added Claude Opus 4.5 and 4.6 models for Snowflake Cortex.
- [[#2352](https://github.com/posit-dev/positron/issues/2352), [#11672](https://github.com/posit-dev/positron/issues/11672)] Notebooks: cell outputs for pandas and polars DataFrames now render as interactive data grids with scrolling, sorting, cell selection/copy, and an "Open in Data Explorer" button.
- [[#6571](https://github.com/posit-dev/positron/issues/6571)] Notebooks: added ability to show/hide the output of a cell.
- [[#11164](https://github.com/posit-dev/positron/issues/11164)] Notebooks: added raw cell support. Raw cells can be inserted via the cell action bar submenu or cell context menu and display as plain editors without execution controls.
- [[#11305](https://github.com/posit-dev/positron/issues/11305)] Notebooks: added in-app notification to announce the Positron Notebook Editor when users open Jupyter notebooks.
- [[#10576](https://github.com/posit-dev/positron/issues/10576)] Notebooks: now show cell output context menu on right-click.
- [[#10575](https://github.com/posit-dev/positron/issues/10575)] Notebooks: show cell context menu on right-click of rendered markdown cells.
- [[#10065](https://github.com/posit-dev/positron/issues/10065)] Notebooks: added split and join cell commands, including keyboard shortcuts matching Jupyter conventions.
- [[#10485](https://github.com/posit-dev/positron/issues/10485), [#10426](https://github.com/posit-dev/positron/issues/10426)] Python: now support starting x64 Python interpreters on ARM Windows and macOS.
- [[#3573](https://github.com/posit-dev/positron/issues/3573)] Python: now allow users to name their virtual environments in the New Folder Template flow.
- [[#8060](https://github.com/posit-dev/positron/issues/8060)] Python: comments like `# SECTION ----` will now create a section in the Outline and be foldable by default.
- [[#11542](https://github.com/posit-dev/positron/issues/11542)] Python: autocomplete now suggests integer keys when accessing dicts, DataFrames, and Series with bracket notation.
- [[#5436](https://github.com/posit-dev/positron/issues/5436)] Python: column name completions now appear inside pandas and polars DataFrame method string arguments such as `groupby()`, `sort_values()`, `select()`, `merge()`, and others.
- [[#2347](https://github.com/posit-dev/positron/issues/2347)] R: added support for opening `.RData` and `.rds` files in Positron, importing them into your R session.
- [[#9841](https://github.com/posit-dev/positron/issues/9841)] R: Quarto documents using `engine: jupyter` with `jupyter: ark` can now use Positron's bundled ark kernel.
- [[#8939](https://github.com/posit-dev/positron/issues/8939)] R: classed lists like data frames or model results can now be expanded in the debugger's Variables pane.
- [[#11889](https://github.com/posit-dev/positron/issues/11889)] R: virtual sources generated while stepping in the debugger now show the function name in the source to make where R is paused clearer.
- [[#11784](https://github.com/posit-dev/positron/issues/11784)] R: Shiny is now fully supported by the R debugger. Please update to the latest version of the `shiny` package to get full support.
- [[#11797](https://github.com/posit-dev/positron/issues/11797)] R: debugger now supports error and warning breakpoints. Set these in the Breakpoints pane to drop in the debugger as soon as an error or warning is emitted.
- [[#11799](https://github.com/posit-dev/positron/issues/11799)] R: debugger can now be invoked while R code is running. You can either run the command "Debug: Pause", or check the Interrupt breakpoint option in the Breakpoints pane and interrupt R. This feature allows you to peek at what R is doing while running long computations or stuck in an infinite loop. You can even resume the computation by clicking on Continue in the Debug Toolbar.
- [[#11892](https://github.com/posit-dev/positron/issues/11892)] R: the debugger now excludes Shiny internals from the call stack by default. Set the global option `"ark.debugger.show_hidden_frames"` to `"fenced"` to show them (or to `TRUE` to show all hidden frames).
- [[#11144](https://github.com/posit-dev/positron/issues/11144), [#11848](https://github.com/posit-dev/positron/issues/11848)] Added new _Runtime Startup Diagnostics_ command for troubleshooting slow or failing R or Python environments.
- [[#1765](https://github.com/posit-dev/positron/issues/1765)] R: debugger now has support for the Watch Pane. This is especially useful for tracking variables that do not show in the Debug Variables pane, or the result of computations. If you prefix expressions with `/print`, the result shows the R output instead of a structured variable.
- [[#3078](https://github.com/posit-dev/positron/issues/3078)] R: the Console now synchronizes with the frame environment selected in the Call Stack view of the debugger pane. You can now interact with local objects higher up in the call stack, just like you would with `base::recover()`.
- [[#11050](https://github.com/posit-dev/positron/issues/11050)] R: dynamic completions (e.g., for data frame columns) are now sensitive to which call frame is selected in the debugger.
- [[#12131](https://github.com/posit-dev/positron/issues/12131)] R: the Variables pane now synchronizes with the frame selected in the call stack.
- [[#2702](https://github.com/posit-dev/positron/issues/2702)] Added a warning when an interpreter's architecture doesn't match the system architecture, helping users understand potential performance or package compatibility issues.
- [[#11735](https://github.com/posit-dev/positron/issues/11735)] Deprecated the `update.systemArchitecture` setting to always automatically detect the system architecture on upgrade.
- [[#11816](https://github.com/posit-dev/positron/issues/11816)] Added [`files.enableDownloads`](positron://settings/files.enableDownloads) and [`files.enableUploads`](positron://settings/files.enableUploads) settings for file transfer restrictions.

#### Bug fixes

- [[#8290](https://github.com/posit-dev/positron/issues/8290)] Assistant: tools disabled via Agent mode Configure Tools are now disabled in chat.
- [[#11616](https://github.com/posit-dev/positron/issues/11616)] Assistant: tools requiring a specific language session are now filtered correctly when those sessions are not active.
- [[#11701](https://github.com/posit-dev/positron/issues/11701)] Assistant: fixed issue causing tool calls to be unavailable for autoconfigured providers.
- [[#10831](https://github.com/posit-dev/positron/issues/10831)] Assistant: no longer have to reload Positron after enabling Snowflake Cortex model provider. Also applies to the Catalog Explorer!
- [[#11845](https://github.com/posit-dev/positron/issues/11845)] Assistant: fixed model picker when no models are available.
- [[#11575](https://github.com/posit-dev/positron/issues/11575)] Assistant: fixed Sonnet models not using the `getTableSummary` tool when asked to summarize data.
- [[#11328](https://github.com/posit-dev/positron/issues/11328)] Assistant: fixed endpoint resolution issue with Copilot Auto model endpoint.
- [[#8910](https://github.com/posit-dev/positron/issues/8910)] Assistant: Bedrock error messages now link to Settings and documentation.
- [[#11755](https://github.com/posit-dev/positron/issues/11755)] Assistant: simplified IAM authorization errors with documentation links.
- [[#11361](https://github.com/posit-dev/positron/issues/11361)] Assistant: file editing tools no longer delete code at wrong locations when text appears multiple times in a document.
- [[#11923](https://github.com/posit-dev/positron/issues/11923)] Assistant: fixed "Working..." progress message when streaming chat response.
- [[#12070](https://github.com/posit-dev/positron/issues/12070)] Assistant: fixed issue where token usage was not being reported in progress data part.
- [[#11611](https://github.com/posit-dev/positron/issues/11611)] Notebooks: cells now auto-scroll into view during keyboard navigation (<kbd>Arrow Up</kbd>/<kbd>Arrow Down</kbd>, <kbd>Shift+Arrow</kbd>) so the active cell is always visible.
- [[#10641](https://github.com/posit-dev/positron/issues/10641)] Notebooks: multiple cells can now be run at a time with <kbd>Shift+Enter</kbd> when in a multi-selection state.
- [[#9070](https://github.com/posit-dev/positron/issues/9070)] Notebooks: fixed notebook language features (code completions, hover, etc.) not working after restoring a session.
- [[#10600](https://github.com/posit-dev/positron/issues/10600)] Notebooks: fixed superscript (`^text^`) and subscript (`~text~`) syntax not rendering in Positron notebooks.
- [[#12087](https://github.com/posit-dev/positron/issues/12087)] Notebooks: fixed Assistant using wrong notebook tools for package management when Positron notebook mode is active.
- [[#10785](https://github.com/posit-dev/positron/issues/10785)] Notebooks: fixed SVG plot output not rendering in Positron notebooks when using `%matplotlib inline` with SVG figure format.
- [[#8687](https://github.com/posit-dev/positron/issues/8687)] Console: when an interactive prompt like R `readline()` or `menu()` or Python `input()` or `getpass()` is submitted or canceled, focus will go back to the Console.
- [[#8201](https://github.com/posit-dev/positron/issues/8201)] Console: pasting now works in interactive prompts like R `readline()` or `menu()`, or Python `input()` or `getpass()`.
- [[#11411](https://github.com/posit-dev/positron/issues/11411)] Console: double-clicking text in the Console now selects it instead of jumping to the bottom.
- [[#9740](https://github.com/posit-dev/positron/issues/9740)] Console: fixed Python console crashes on Windows when using conda environments with packages that have native dependencies (numpy, matplotlib, scipy, etc).
- [[#11010](https://github.com/posit-dev/positron/issues/11010)] Console: fixed issues with startup timeouts when starting kernel supervisor.
- [[#11486](https://github.com/posit-dev/positron/issues/11486)] Console: fixed issues starting long-running background kernel sessions on Windows.
- [[#7584](https://github.com/posit-dev/positron/issues/7584)] Python: matplotlib plots do not repopulate after pressing "Clear All".
- [[#9999](https://github.com/posit-dev/positron/issues/9999)] Python: fixed race condition where wrong Python runtime could start during new folder initialization.
- [[#11553](https://github.com/posit-dev/positron/issues/11553)] Python: fixed column name completions not appearing for multi-column DataFrame selection with `df[["` syntax.
- [[#11270](https://github.com/posit-dev/positron/issues/11270)] Python: fixed `uv` package installs not respecting the [`http.proxy`](positron://settings/http.proxy) setting.
- [[#11137](https://github.com/posit-dev/positron/issues/11137)] R: plots are no longer always saved as PNG in Plots pane.
- [[#8350](https://github.com/posit-dev/positron/issues/8350)] R: Stepping through code with <kbd>Cmd/Ctrl+Enter</kbd> now works more reliably when there are syntax errors in the document, both in R code and Quarto documents.
- [[#8979](https://github.com/posit-dev/positron/issues/8979), [#12021](https://github.com/posit-dev/positron/issues/12021)] R: fixed a debugger crash that occurred under some circumstances.
- [[#11890](https://github.com/posit-dev/positron/issues/11890)] R: the R debugger now disables the JIT compiler before executing the "stepping into" gesture. This prevents the debugger from confusingly pausing in the compiler's internal frames.
- [[#11891](https://github.com/posit-dev/positron/issues/11891)] R: long call stacks in the debugger are no longer truncated.
- [[#1035](https://github.com/posit-dev/ark/issues/1035)] R: debugger's `source()` hook now returns the last value, consistently with `base::source()`.
- [[#12085](https://github.com/posit-dev/positron/issues/12085)] R: backtraces of errors emitted while in the debugger are now properly stored in the Console.
- [[#7667](https://github.com/posit-dev/positron/issues/7667), [#11604](https://github.com/posit-dev/positron/issues/11604)] R: fixed focus issues when evaluating code in the Console while the debugger is active.
- [[#11780](https://github.com/posit-dev/positron/issues/11780)] R: fixed a regression when stepping through certain calls like `tryCatch()`. Console evaluations are now evaluated in the expected environment.
- [[#11989](https://github.com/posit-dev/positron/issues/11989)] Dev Containers: now respect environment variables set in `containerEnv`.

#### Dependencies

- Updated `code-oss` upstream to v1.108.0.
- Updated `vscode-python` upstream to v2026.2.0.
