### Highlights

#### New features in the Data Explorer 🌟

We've introduced new features to help focus on key columns and navigate larger datasets during exploratory analysis.

Pin important columns or rows to keep them visible while scrolling through large datasets. When a column is pinned in the data grid, its corresponding row in the Summary Panel gets pinned as well, maintaining consistency across views.

Sort and filter rows in the Summary Panel to quickly view summary statistics for specific columns. Sort alphabetically by name or group by data type. Filter by column name to narrow down the list and focus on the columns most relevant to your current analysis.

#### GitHub Copilot Chat in Positron Assistant 🤖

[Positron Assistant](https://positron.posit.co/assistant) now supports GitHub Copilot for both completions _and_ chat.

When you have GitHub Copilot added as a model provider, GitHub Copilot models, chat participants, and tools are now available in the chat pane and inline chat, in addition to inline code completions.

We're continuing to expand our support for additional language model providers, with support for custom providers in progress.

#### Manage Positron Assistant completions ⚙️

Completions from an LLM such as GitHub Copilot can be super useful, but sometimes they can be distracting or interfere with other completions from the Python or R LSP. You now have more control over when you see Positron Assistant completions:

- Snooze these completions temporarily from the Assistant status bar popup.
- Disable completions for the current file type (or all files) from the same status bar popup.
- Use the new _Positron Assistant: Toggle (Enable/Disable) Completions_ command to toggle these completions.

<div id="checkbox"></div>

### Changelog

#### New features

- [[#8986](https://github.com/posit-dev/positron/issues/8986)] Data Explorer: added support for "Convert to Code" that generates SQL for headless/DuckDB Data Explorer sessions.
- [[#9030](https://github.com/posit-dev/positron/issues/9030)] Data Explorer: added support for "Convert to Code" that generates tidyverse code for R dataframes.
- [[#2580](https://github.com/posit-dev/positron/issues/2580), [#9344](https://github.com/posit-dev/positron/issues/9344), [#9265](https://github.com/posit-dev/positron/issues/9265)] Added pinning for both columns and rows to Data Explorer.
- [[#8446](https://github.com/posit-dev/positron/issues/8446)] Data Explorer histograms for Polars are now supported in environments where NumPy is not installed.
- [[#9083](https://github.com/posit-dev/positron/issues/9083)] Data Explorer: updated null filter labels to match summary panel.
- [[#9383](https://github.com/posit-dev/positron/issues/9383)] Data Explorer: added new selection backend for R.
- [[#2971](https://github.com/posit-dev/positron/issues/2971)] Data Explorer: now display R column labels in tooltips in the Data Explorer summary panel and column headers, if they exist.
- [#8934, #7585] Data Explorer: added keyboard accessibility for Data Explorer filter popup.
- [[#3377](https://github.com/posit-dev/positron/issues/3377)] Data Explorer: added keyboard support for context menus.
- [[#6515](https://github.com/posit-dev/positron/issues/6515)] Data Explorer: now support previewing `ibis` tables in the Connections pane.
- [[#2010](https://github.com/posit-dev/positron/issues/2010), [#9416](https://github.com/posit-dev/positron/issues/9416)] Added support for GitHub Copilot Chat in Positron Assistant.
- [[#8592](https://github.com/posit-dev/positron/issues/8592)] Added support for OpenAI and OpenAI compatible model providers in Positron Assistant.
- [[#9308](https://github.com/posit-dev/positron/issues/9308), [#9046](https://github.com/posit-dev/positron/issues/9046)] Improved tracking and display of token usage in Positron Assistant.
- [[#9287](https://github.com/posit-dev/positron/issues/9287), [#9288](https://github.com/posit-dev/positron/issues/9288)] Improved Positron Assistant Git integration.
- [[#8017](https://github.com/posit-dev/positron/issues/8017)] Assistant: added commands to toggle Copilot completions on/off, and a snooze button for temporarily disabling them.
- [[#8253](https://github.com/posit-dev/positron/issues/8253)] Assistant: Editor UI is now updated in real time as edits are produced by the language model.
- [[#9645](https://github.com/posit-dev/positron/issues/9645)] Assistant's Console actions enabled by default.
- [[#9163](https://github.com/posit-dev/positron/issues/9163)] Assistant: added a timeout to language model provider sign-in.
- [[#8674](https://github.com/posit-dev/positron/issues/8674)] Assistant: now show a warning when destructive code/actions are suggested.
- [[#9416](https://github.com/posit-dev/positron/issues/9416)] Assistant: use [`chat.useCopilotParticipantsWithOtherProviders` setting](positron://settings/chat.useCopilotParticipantsWithOtherProviders) to enable Copilot participants with other providers.
- [[#8992](https://github.com/posit-dev/positron/issues/8992)] Assistant: use a more efficient format for sending session variables, to reduce token usage.
- [[#9155](https://github.com/posit-dev/positron/issues/9155)] The <kbd>Ctrl+L</kbd> keybinding to clear the console now works when the editor is focused, in addition to when the console is focused.
- [[#8404](https://github.com/posit-dev/positron/issues/8404)] Improved user feedback when using the command _Interpreter: Discover All Interpreters_.
- [[#9114](https://github.com/posit-dev/positron/issues/9114)] New command _Fill Symbol to End of Line_ to fill the remainder of the line with a given symbol, such as `-`.
- [[#9022](https://github.com/posit-dev/positron/issues/9022)] When saving untitled notebooks, you can now update their working directory without losing data.
- [[#3801](https://github.com/posit-dev/positron/issues/3801)] Added a new optional way to attach a console to your notebook's R or Python session for one-off commands and interactive work.
- [[#8388](https://github.com/posit-dev/positron/issues/8388)] Posit Workbench: now show results of in-progress computations when reconnecting to a session.
- [[#8580](https://github.com/posit-dev/positron/issues/8580)] Python: added support for the Python Snowflake connector in the Connections Pane.
- [[#9419](https://github.com/posit-dev/positron/issues/9419)] Added preview support for Python 3.14.
- [[#9129](https://github.com/posit-dev/positron/issues/9129)] R: The keyboard shortcuts for _R: Source R File_ and _R: Source R File with Echo_ are now consistent with RStudio's defaults.
- [[#9165](https://github.com/posit-dev/positron/issues/9165)] R: A new [`positron.r.packageManagerRepository` setting](positron://settings/positron.r.packageManagerRepository) allows overriding the Posit Package Manager URL used to install R packages when `positron.r.defaultRepositories` is set to `auto`.
- [[#9099](https://github.com/posit-dev/positron/issues/9099)] R: added support for `rstudioapi::showPrompt`.

#### Bug fixes

- [[#9166](https://github.com/posit-dev/positron/issues/9166)] Fixed errors when kernels are run on a separate extension host.
- [[#8905](https://github.com/posit-dev/positron/issues/8905)] Fixed bug in parent folder handling ("Location") for _Workspaces: New Folder from Template..._ when using the "Empty Folder" template.
- [[#8921](https://github.com/posit-dev/positron/issues/8921)] Fixed state management for checkmarks in Variables pane context menus for sorting and grouping.
- [[#9623](https://github.com/posit-dev/positron/issues/9623)] Quarto and Pandoc are now included in the Remote SSH version of Positron.
- [[#9273](https://github.com/posit-dev/positron/issues/9273), [#9258](https://github.com/posit-dev/positron/issues/9258), [#9533](https://github.com/posit-dev/positron/issues/9533)] Fixed how Positron checks its version, including for extension updates.
- [[#9215](https://github.com/posit-dev/positron/issues/9215)] Fixed errors starting Python and R sessions on some systems when `HTTP_PROXY` is set.
- [[#6368](https://github.com/posit-dev/positron/issues/6368)] Fixed errors starting Python and R sessions on Windows when the Kernel Supervisor's _Shutdown Timeout_ setting is used.
- [[#8704](https://github.com/posit-dev/positron/issues/8704)] Fixed dialog dismiss behavior for _Workspaces: New Folder from Git..._ command.
- [[#8695](https://github.com/posit-dev/positron/issues/8695)] Data Explorer: fixed a bug with columns populating in the filter dropdown.
- [[#9278](https://github.com/posit-dev/positron/issues/9278)] Data Explorer: fixed bug where keybindings can forcibly open Convert to Code modal.
- [[#8935](https://github.com/posit-dev/positron/issues/8935)] Data Explorer: addressed UX issues with tooltips and buttons in Data Explorer.
- [[#9524](https://github.com/posit-dev/positron/issues/9524)] Data Explorer: fixed parameter validation when changing filter types.
- [[#9538](https://github.com/posit-dev/positron/issues/9538)] Data Explorer: fixed a non-deterministic bug where frequency table sparklines might be incorrect when looking at raw data file.
- [[#9525](https://github.com/posit-dev/positron/issues/9525)] Data Explorer: fixed bug in sparkline tooltips where a string value like "9E" would get incorrectly converted to a float for a frequency table tooltip.
- [[#8860](https://github.com/posit-dev/positron/issues/8860)] Always treat the first row of CSV files as the column labels in the Data Explorer to address cases where DuckDB infers the presence of a header incorrectly.
- [[#9316](https://github.com/posit-dev/positron/issues/9316)] Data Explorer: Fixed a bug where exporting whole columns after sorting would not return the data in the sorted order. This affected the R and raw data file (DuckDB) backends.
- [[#9619](https://github.com/posit-dev/positron/issues/9619)] Data Explorer: fixed handling for 0-row dataframes.
- [[#3755](https://github.com/posit-dev/positron/issues/3755)] Data Explorer: fixed mouse wheel handling so that holding the shift key down will invert the scroll direction from vertical to horizontal.
- [[#9593](https://github.com/posit-dev/positron/issues/9593)] Data Explorer: fixed how column profiles are recalculated.
- [[#9298](https://github.com/posit-dev/positron/issues/9298)] Data Explorer instances attached to raw files (i.e. using DuckDB) are no longer broken by extension host restarts or changing the installed extension configuration.
- [[#9526](https://github.com/posit-dev/positron/issues/9526)] Data Explorer: Fixed bug where missing value count would still show "Calculating..." for a 0-row table.
- [[#9527](https://github.com/posit-dev/positron/issues/9527)] Data Explorer: fixed errors computing summary sparklines for 0-row and 1-row data frames from Python and R.
- [[#9712](https://github.com/posit-dev/positron/issues/9712)] Data Explorer: fixed generating SVGs for sparklines, for tables with zero rows.
- [[#9281](https://github.com/posit-dev/positron/issues/9281)] Data Explorer: fixed bug where pending filters and sorts may not appear when converting to code.
- [#9482, #2614] Data Explorer: integer types display sparkline histogram bins as whole number intervals.
- [[#7040](https://github.com/posit-dev/positron/issues/7040)] Assistant: the action toolbar is now present on code generated for the `executeCode` tool, allowing users to copy/apply in editor/etc.
- [[#9183](https://github.com/posit-dev/positron/issues/9183)] Assistant: code maintains proper styling & interactivity even once executed/discarded.
- [[#8253](https://github.com/posit-dev/positron/issues/8253)] Assistant: when using Edit mode, or Apply in Editor, the same extension that provides the chat model will now also handle mapping the edits to the file.
- [[#8727](https://github.com/posit-dev/positron/issues/8727)] Fixed issue causing Assistant to occasionally try to execute code with the wrong language in a Positron console.
- [[#8976](https://github.com/posit-dev/positron/issues/8976)] Assistant: "get plot" tool works when tool details output is enabled.
- [[#8948](https://github.com/posit-dev/positron/issues/8948)] Fixed mishandling of `-m` in Windows paths for the Python `%run` magic.
- [[#9579](https://github.com/posit-dev/positron/issues/9579)] Set `JUPYTER_PREFER_ENV_PATH=1` in Positron terminals and consoles so that Python virtual environments are used consistently for Quarto rendering.
- [[#8053](https://github.com/posit-dev/positron/issues/8053)] R: Fixed how `Surv` objects are represented and formatted in the Data Explorer and Variables pane.
- [#5338, #6708] R: Remove some problematic S3 overrides for `shiny.tag` and `shiny.tag.list`.
- [[#8426](https://github.com/posit-dev/positron/issues/8426)] R: Fixed R Help failing to load in the Help pane in environments with system proxies.

#### Dependencies

- Updated Copilot Language Server to v1.367.0.
- Updated `vscode-python` upstream to v2025.14.0.