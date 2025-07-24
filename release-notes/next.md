### Highlights

- Something cool is 🪩

<div id="checkbox"></div>

### Changelog

#### New features

- [#8072, #8207] Assistant now has a new experimental git integration. You can try it out by enabling the [`positron.assistant.gitIntegration.enable` setting](positron://settings/positron.assistant.gitIntegration.enable).
- [#8325] Assistant now uses Anthropic cache prompting.
- [#8327] Improved keyboard navigation in the Plots pane; arrow keys now navigate the plot history.
- [#8041] It is now possible to interrupt R and Python sessions in order to reconnect to them.
- [#5800] Improved performance and security for connections to R and Python sessions.
- [#8016] Assistant can now reference R help pages and package vignettes via a tool call.
- [#4411] The console font can now be configured independently of the editor font; see settings like `console.fontFamily`, `console.fontSize`, and related.
- [#8465] Assistant: the `documentCreate` tool is now available in Edit mode.
- [#7817, #8233, #8472] Added token usage to Assistant for chat. You can try it out by enabling the [`positron.assistant.showTokenUsage.enable` setting](positron://settings/positron.assistant.showTokenUsage.enable).
- [#8033] The Assistant chat log can now be exported for debugging/testing.
- [#7595] You can now control Assistant's access to data in your Python and R sessions. Opt out via the [`chat.implicitSessionContext.enabled` setting](positron://settings/chat.implicitSessionContext.enabled).
- [#8539] The default log level has been returned to info (this was previously debug) to reduce log noise. Please consider using the _Set Log Level_ command to restore debug logging when reporting bugs. 
- [#5486] R: `browseURL()` in R now delegates to the operating system's default opener for inputs that are not recognized as a web URL or an HTML file.
- [#8078] Assistant: tools are now disabled if the context doesn't include the info needed for the tool.
- TODO: add info on https://github.com/posit-dev/positron/issues/7114

#### Bug fixes

- [#7692] Now persist session renames in the console UI after reloads for web builds.
- [#8318] Fixed "zoom to fit" in the Plots pane.
- [#4547] "View" actions are now disabled in the Variables pane while one is already in progress.
- [#1360] R: `@examples` documentation highlighting no longer highlights further than expected.
- [#8203] Now inform users to install `numpy` if they want histograms in the Data Explorer for `polars` data frames.
- [#8371] Improve theme support for action bars.
- [#7638] Assistant: removed the run/debug play button from editor actions when a chat session is open in an editor.
- [#8433] Assistant: renamed chat command from `/quarto` to `/exportQuarto`.
- [#8522] Assistant: reduced token usage when Assistant is invoked via inline notebook editor.
- [#8538] Removed superfluous `RUST_LO`G environment variable from R and Python sessions.
- [#8245] Improved the performance of Python Variable pane updates.
- [#8095] In the Data Explorer in Python, if a column contains constant values, the histogram will show a single bin with the lower and upper edge equal, matching the DuckDB behavior when opening a file from the file explorer pane.
- [#8641, #8642] Assistant: now ensure Variables are included in context and tool calls.

#### Dependencies

- Updated `vscode-python` upstream to v2025.8.1.
- Updated `code-oss` upstream to v1.102.0.