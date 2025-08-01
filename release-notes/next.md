### Highlights

#### Positron Assistant 🤖

Positron Assistant, our AI client currently in preview, has received several updates in this release. We have made changes to reduce token usage, added an experimental git integration, and added new tools that the Assistant can use (for example, to create documents, view documentation, or to get info on your rectangular data). You can also now control Assistant's access to data in your Python and R sessions. If you have a problem with the Assistant that you want to report, use the commands that begin _Positron Assistant: Export the current chat_ to export your logs.

#### New keybinding ✨

The most upvoted feature request in this release is a new keybinding to execute the current statement in your Python or R Console _without_ advancing to the next one. You can now use <kbd>Alt+Enter</kbd> to execute your current statement without moving the cursor. (The existing keybinding <kbd>Ctrl/Cmd+Enter</kbd> executes the current statement and _does_ advance your cursor.)

#### Diagnostics and outlines for R 😌

Our engine for providing R diagnostics has undergone a major upgrade! You'll notice that you no longer get overwhelmed with squiggles in your R code when you open a fresh session. Outlines in `.R` files have also been improved, especially for R6 methods and `targets` pipelines.

<div id="checkbox"></div>

### Changelog

#### New features

- [[#8072](https://github.com/posit-dev/positron/issues/8072), [#8207](https://github.com/posit-dev/positron/issues/8207)] Assistant now has a new experimental git integration. You can try it out by enabling the [`positron.assistant.gitIntegration.enable` setting](positron://settings/positron.assistant.gitIntegration.enable).
- [[#8325](https://github.com/posit-dev/positron/issues/8325)] Assistant now uses Anthropic cache prompting.
- [[#8327](https://github.com/posit-dev/positron/issues/8327)] Improved keyboard navigation in the Plots pane; arrow keys now navigate the plot history.
- [[#8041](https://github.com/posit-dev/positron/issues/8041)] It is now possible to interrupt R and Python sessions in order to reconnect to them.
- [[#5800](https://github.com/posit-dev/positron/issues/5800)] Improved performance and security for connections to R and Python sessions.
- [[#8016](https://github.com/posit-dev/positron/issues/8016)] Assistant can now reference R help pages and package vignettes via a tool call.
- [[#4411](https://github.com/posit-dev/positron/issues/4411)] The console font can now be configured independently of the editor font; see settings like `console.fontFamily`, `console.fontSize`, and related.
- [[#8465](https://github.com/posit-dev/positron/issues/8465)] Assistant: the `documentCreate` tool is now available in Edit mode.
- [[#7817](https://github.com/posit-dev/positron/issues/7807), [#8233](https://github.com/posit-dev/positron/issues/8233), [#8472](https://github.com/posit-dev/positron/issues/8472)] Added token usage to Assistant for chat. You can try it out by enabling the [`positron.assistant.showTokenUsage.enable` setting](positron://settings/positron.assistant.showTokenUsage.enable).
- [[#8033](https://github.com/posit-dev/positron/issues/8033)] The Assistant chat log can now be exported for debugging/testing.
- [[#7595](https://github.com/posit-dev/positron/issues/7595)] You can now control Assistant's access to data in your Python and R sessions. Opt out via the [`chat.implicitSessionContext.enabled` setting](positron://settings/chat.implicitSessionContext.enabled).
- [[#8539](https://github.com/posit-dev/positron/issues/8539)] The default log level has been returned to info (this was previously debug) to reduce log noise. Please consider using the _Set Log Level_ command to restore debug logging when reporting bugs. 
- [[#5486](https://github.com/posit-dev/positron/issues/5486)] R: `browseURL()` in R now delegates to the operating system's default opener for inputs that are not recognized as a web URL or an HTML file.
- [[#8078](https://github.com/posit-dev/positron/issues/8078)] Assistant: tools are now disabled if the context doesn't include the info needed for the tool.
- [[#7114](https://github.com/posit-dev/positron/issues/7114)] Assistant: added a new `getTableSummary` tool for Python.
- [[#8677](https://github.com/posit-dev/positron/issues/8677)] Updated button labels for session actions in the Console. The restart button now reads "Restart Python" or "Restart R" as appropriate.
- [[#1428](https://github.com/posit-dev/positron/issues/1428)] R: `test_that()` blocks now appear in the outline and breadcrumbs, and also support sticky scroll functionality.
- [[#6546](https://github.com/posit-dev/positron/issues/6546)] R: all functions passed as named arguments also gain outline, breadcrumbs, and sticky scroll support. This improves the UX for R6 methods in particular.
- [[#8402](https://github.com/posit-dev/positron/issues/8402)] R: added support for comment sections (like `# Title ----`) in function calls. This is especially useful for users of the `targets` package where it is common to have very large targets calls that can now be sectioned in the outline, with breadcrumbs and sticky scroll support.
- [[#6549](https://github.com/posit-dev/positron/issues/6549)] R: R6 methods are now exported as workspace symbols. You now search for them with <kbd>Ctrl/Cmd + T</kbd>.
- [[#8330](https://github.com/posit-dev/positron/issues/8330)] R: Added new [`positron.r.symbols.includeAssignmentsInBlocks` setting](positron://settings/positron.r.symbols.includeAssignmentsInBlocks) to control whether local variables in functions and nested `{}` blocks (e.g. in `test_that()` calls) appear in the outline. It's turned off by default to keep the outline focused on the overall structure of the file.
- [[#4886](https://github.com/posit-dev/positron/issues/4886)] R: Added new [`positron.r.workspaceSymbols.includeCommentSections` setting](positron://settings/positron.r.workspaceSymbols.includeCommentSections) to control whether comment sections (like `# Title ----`) are exported as workspace symbols. When enabled, you can search for the sections with <kbd>Ctrl/Cmd + T</kbd>. This is disabled by default to keep symbol search focused on actual symbols.
- [[#5486](https://github.com/posit-dev/positron/issues/5486)] R: `browseURL()` now delegates to the operating system's default opener for inputs that are not recognized as a web URL or an HTML file.
- [[#8429](https://github.com/posit-dev/positron/issues/8429)] Assistant: exported chat log now contains prompt and Positron context info. Use the commands that begin _Positron Assistant: Export the current chat_ to export logs when you want to report a problem with the Assistant.
- [[#1325](https://github.com/posit-dev/positron/issues/1325), [#8708](https://github.com/posit-dev/positron/issues/8708), [#2252](https://github.com/posit-dev/positron/issues/2252)] R: the diagnostics engine is vastly improved in fresh sessions. You no longer have to attach packages in the console session to silence "unknown symbol" diagnostics in scripts. The issue has also been resolved in packages where a `load_all()` is no longer necessary to silence symbol diagnostics.
- [[#2778](https://github.com/posit-dev/positron/issues/2778)] Added new keybinding <kbd>Alt+Enter</kbd> to execute the current statement _without_ advancing.
- [[#6477](https://github.com/posit-dev/positron/issues/6477)] Positron (and Positron Assistant) can now automatically install packages into `uv` environments without `pip`.

#### Bug fixes

- [[#7692](https://github.com/posit-dev/positron/issues/7692)] Now persist session renames in the console UI after reloads for web builds.
- [[#8318](https://github.com/posit-dev/positron/issues/8318)] Fixed "zoom to fit" in the Plots pane.
- [[#4547](https://github.com/posit-dev/positron/issues/4547)] "View" actions are now disabled in the Variables pane while one is already in progress.
- [[#1360](https://github.com/posit-dev/positron/issues/1360)] R: `@examples` documentation highlighting no longer highlights further than expected.
- [[#8203](https://github.com/posit-dev/positron/issues/8203)] Now inform users to install `numpy` if they want histograms in the Data Explorer for `polars` data frames.
- [[#8371](https://github.com/posit-dev/positron/issues/8371)] Improve theme support for action bars.
- [[#7638](https://github.com/posit-dev/positron/issues/7638)] Assistant: removed the run/debug play button from editor actions when a chat session is open in an editor.
- [[#8433](https://github.com/posit-dev/positron/issues/8433)] Assistant: renamed chat command from `/quarto` to `/exportQuarto`.
- [[#8522](https://github.com/posit-dev/positron/issues/8522), [#8556](https://github.com/posit-dev/positron/issues/8566)] Assistant: reduced token usage when calling tools or Assistant is invoked via inline notebook editor.
- [[#8538](https://github.com/posit-dev/positron/issues/8538)] Removed superfluous `RUST_LOG` environment variable from R and Python sessions.
- [[#8245](https://github.com/posit-dev/positron/issues/8245)] Improved the performance of Python Variable pane updates.
- [[#8095](https://github.com/posit-dev/positron/issues/8095)] In the Data Explorer in Python, if a column contains constant values, the histogram will show a single bin with the lower and upper edge equal, matching the DuckDB behavior when opening a file from the file explorer pane.
- [[#8641](https://github.com/posit-dev/positron/issues/8641), [#8642](https://github.com/posit-dev/positron/issues/8642)] Assistant: now ensure Variables are included in context and tool calls.
- [[#7038](https://github.com/posit-dev/positron/issues/7038)] Assistant: code block toolbar is now appropriately visible on long code blocks.
- [[#6137](https://github.com/posit-dev/positron/issues/6137)] R: the breadcrumbs and sticky scroll features now behave properly in the presence of comment sections like `# Title ----`.
- [[#6107](https://github.com/posit-dev/positron/issues/6107)] R: section comments nested in `{ }` blocks now appear in the outline.
- [[#4886](https://github.com/posit-dev/positron/issues/4886)] When a comment section (like `# Title ----`) is emitted as workspace symbol, and it clashes with another top-level definition (such as `Title <- function() {}`), the "Go to definition" feature now always prioritizes the definition of regular functions and variables.
- [[#8549](https://github.com/posit-dev/positron/issues/8549)] R: fixed a race condition between the workspace indexer and diagnostics that caused spurious diagnotics on startup.
- [[#8550](https://github.com/posit-dev/positron/issues/8550)] R: fixed a diagnostics issue where objects defined in other files were not properly detected.
- [[#8668](https://github.com/posit-dev/positron/issues/8668)] R: workspace symbols no longer get duplicates when a file is renamed.
- [[#8630](https://github.com/posit-dev/positron/issues/8630)] R: "Go to Definition" now gives priority to definitions in the current file.
- [[#8645](https://github.com/posit-dev/positron/issues/8645)] Assistant: fixed file path bug when using file contents tool.
- [[#8760](https://github.com/posit-dev/positron/issues/8760)] Fixed Data Explorer filtering for `YYYY-MM-DD` values for pandas data frames.

#### Dependencies

- Updated `vscode-python` upstream to v2025.8.1.
- Updated `code-oss` upstream to v1.102.0.