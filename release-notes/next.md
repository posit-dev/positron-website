### Highlights

#### Try our new Python language server options 🐍

Our new release provides both a better default experience for editing Python code, as well as more flexibility for folks who want to customize their experience. We changed our approach to providing a Python LSP so you can bring your own chosen Python LSP extension to provide syntax highlighting and other LSP features; we've tested out basedpyright, ty, Pyrefly, and ZubanLS and expect all to work in Positron now. One of our goals is to provide a great "batteries included" experience for all users (including those who aren't sure which to choose) so, starting with this release, we now bundle the Pyrefly extension.

We no longer bundle the Pyright extension because its functionality overlaps with Pyrefly. If you do not want to use Pyrefly, uninstall that extension. You also will want to uninstall the Python Environments extension if you have it, because its features do not work in Positron.

[Let us know](https://github.com/posit-dev/positron/discussions) how it goes with our new Python language server support!

#### Positron Assistant 🤖

This release brings several improvements to make Assistant more reliable and easier to troubleshoot. Two new commands help you manage your Assistant configuration:

- _Positron Assistant: Reset State_ lets you start totally fresh when needed.
- _Positron Assistant: Collect Diagnostics_ generates a diagnostics report to help identify issues. 
  
We've also improved token efficiency across many tools and introduced preview support for Snowflake Cortex as a language model provider. If you're on Posit Workbench, AWS Bedrock is now automatically enabled when managed credentials are available, with graceful handling of credential expiration.

#### Run your code with new keyboard shortcuts 💥

The most upvoted feature in this month's release is a new set of keyboard shortcuts for running code from your document beginning to the current line <kbd>Ctrl/Cmd+Alt+Home</kbd> and from the current line to your document end <kbd>Ctrl/Cmd+Alt+End</kbd>. If you opt in the RStudio Keymap, these are available as <kbd>Ctrl/Cmd+Alt+B</kbd> and <kbd>Ctrl/Cmd+Alt+E</kbd>.

<div id="checkbox"></div>

### Changelog

#### New features

- [[#10104](https://github.com/posit-dev/positron/issues/10104), [#10243](https://github.com/posit-dev/positron/issues/10243), [#10241](https://github.com/posit-dev/positron/issues/10241)] Added new Catalog Explorer support for Snowflake data catalogs. This feature is in preview and can be enabled by opting in to the new [`catalogExplorer.enable`](positron://settings/catalogExplorer.enable) setting.
- [[#10430](https://github.com/posit-dev/positron/issues/10430)] Added Connections Pane support for Python Databricks SQL Connector.
- [[#10431](https://github.com/posit-dev/positron/issues/10431)] Added Connections Pane support for Python Google BigQuery.
- [[#10348](https://github.com/posit-dev/positron/issues/10348), [#10236](https://github.com/posit-dev/positron/issues/10236)] Assistant: improved token efficiency of project tools.
- [[#10368](https://github.com/posit-dev/positron/issues/10368)] Assistant: added directory structure tool.
- [[#10346](https://github.com/posit-dev/positron/issues/10346)] Assistant: added command _Positron Assistant: Reset State_ to reset Assistant state.
- [[#10344](https://github.com/posit-dev/positron/issues/10344)] Assistant: added command _Positron Assistant: Collect Diagnostics_ to generate a diagnostics report.
- [[#10179](https://github.com/posit-dev/positron/issues/10179)] Assistant: on Posit Workbench, AWS Bedrock is automatically enabled within Assistant when Managed Credentials are available.
- [[#9652](https://github.com/posit-dev/positron/issues/9652)] Assistant: the AWS Bedrock provider now gracefully handles credential expiration, and automatically refreshes them with the `aws` CLI tool.
- [[#9971](https://github.com/posit-dev/positron/issues/9971)] Assistant: added initial support for user-defined model listing.
- [[#8613](https://github.com/posit-dev/positron/issues/8613)] Assistant: added preview support for Snowflake Cortex language model provider with OAuth managed credentials integration.
- [[#8334](https://github.com/posit-dev/positron/issues/8334)] Added a new layout present for an Assistant-centric workflow (in addition to the existing stacked, side-by-side, and notebook layout presets).
- [[#3731](https://github.com/posit-dev/positron/issues/3731), [#10304](https://github.com/posit-dev/positron/issues/10304)] Python: we now bundle the Pyrefly extension, which gives a much richer Python editing experience, including better syntax highlighting.
- [[#2318](https://github.com/posit-dev/positron/issues/2318)] R: now apply syntax highlighting to roxygen `@examplesif` sections.
- [[#10325](https://github.com/posit-dev/positron/issues/10325)] R: added shim for `rstudioapi::readRStudioPreference()`.
- [[#7430](https://github.com/posit-dev/positron/issues/7430)] R: allow extensions contribute F1 "show help topic" entries.
- [[#10645](https://github.com/posit-dev/positron/issues/10645)] R: the syntax highlighting for `T` and `F` now treats them as regular variables (since they are not reserved words or constants in R).
- [[#8559](https://github.com/posit-dev/positron/issues/8559)] R: <kbd>Cmd/Ctrl+Enter</kbd> within roxygen2 `@examples` and `@examplesIf` tags now executes entire R expressions rather than executing one line at a time.
- [[#4395](https://github.com/posit-dev/positron/issues/4395)] Added new keyboard shortcuts to run code from the document beginning to the current line <kbd>Ctrl/Cmd+Alt+Home</kbd> and from the current line to the document end <kbd>Ctrl/Cmd+Alt+End</kbd>. If you opt in the RStudio Keymap, these are available as <kbd>Ctrl/Cmd+Alt+B</kbd> and <kbd>Ctrl/Cmd+Alt+E</kbd>.
- [[#6479](https://github.com/posit-dev/positron/issues/6479)] Added a new [`workbench.topActionBar.visible`](positron://settings/workbench.topActionBar.visible) setting to control whether the Positron top bar is visible.
- [[#7054](https://github.com/posit-dev/positron/issues/7054)] Added new command _Plots: Open Plots Gallery in New Window_ to open the whole Plots pane UI in an auxiliary window. You can also pop out the new standalone window from the plots action bar.
- [[#10329](https://github.com/posit-dev/positron/issues/10329)] Added new setting [`plots.historyPolicy`](positron://settings/plots.historyPolicy) to control the when the plot history filmstrip is visible.
- [[#7747](https://github.com/posit-dev/positron/issues/7747)] Added new button to interrupt a running app (such as Streamlit or FastAPI) from the Viewer pane.
- [[#10580](https://github.com/posit-dev/positron/issues/10580)] Added new command `positron.executeCodeInConsole` for extensions to execute code for a given language, URI, and position (such as for the Quarto visual editor).


#### Bug fixes

- [[#4604](https://github.com/posit-dev/positron/issues/4604)] Console: fixed interrupt of Python console on Windows.
- [[#10382](https://github.com/posit-dev/positron/issues/10382)] Console: fixed rendering of Python data frames in the console.
- [[#8303](https://github.com/posit-dev/positron/issues/8303)] Console: fixed bug where consoles that failed to start could not be deleted.
- [[#9761](https://github.com/posit-dev/positron/issues/9761)] Console: fixed issue causing code from scripts to be executed in a notebook console if it had the same language.
- [[#9989](https://github.com/posit-dev/positron/issues/9989)] Console: fixed the "play" button behavior for split editors.
- [[#10115](https://github.com/posit-dev/positron/issues/10115)] Assistant: fixed issue where Console Fix/Explain Actions were hidden when only logged in with Copilot.
- [[#9700](https://github.com/posit-dev/positron/issues/9700)] Assistant: Remove "Next Edit Suggestions" from being displayed in chat status.
- [[#10332](https://github.com/posit-dev/positron/issues/10332)] Assistant: Disable completions for custom providers.
- [[#9770](https://github.com/posit-dev/positron/issues/9770), [#10719](https://github.com/posit-dev/positron/issues/10719)] Assistant: fixed Copilot tools included in chat requests not using a Copilot model and filtering the tools from the "Configure Tools" quick pick.
- [[#10763](https://github.com/posit-dev/positron/issues/10763)] Assistant: fixed stale Assistant model listing when Bedrock is the only registered provider.
- [[#10823](https://github.com/posit-dev/positron/issues/10823)] Assistant: fixed API key error when signing in to Anthropic.
- [[#10737](https://github.com/posit-dev/positron/issues/10737)] Assistant: now show all GitHub Copilot models.
- [[#9883](https://github.com/posit-dev/positron/issues/9883)] Assistant: enabled "Apply in Editor" only when using Copilot to avoid poor results from other model providers.
- [[#10545](https://github.com/posit-dev/positron/issues/10545), [#7393](https://github.com/posit-dev/positron/issues/7393)] Python: The LSP extensions pyrefly and basedpyright can now be activated without popup errors.
- [[#10423](https://github.com/posit-dev/positron/issues/10423)] Python: now stop the Python Environments Extension from being installed because it conflicts with internal features. You may want to uninstall this extension if it's installed already.
- [[#9655](https://github.com/posit-dev/positron/issues/9655)] Python: silenced non-actionable syntax warnings in Python 3.14 coming from `ipykernel`.
- [[#966](https://github.com/posit-dev/ark/issues/966)] R: fixed a bug in the R backend that caused visible errors when the `R_PROFILE` or `R_PROFILE_USER` environment variables were set to paths that don't exist.
- [[#2951](https://github.com/posit-dev/positron/issues/2951)] Setting the activity bar position to bottom or top no longer causes duplicate tab names in the secondary side bar.
- [[#9516](https://github.com/posit-dev/positron/issues/9516)] Added "(preview)" to Connections tables that are truncated to 1,000 rows.

#### Dependencies

- Updated `code-oss` upstream to v1.106.0.
- Updated `vscode-python` upstream to v2025.18.0.
