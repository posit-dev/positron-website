### Patch notes

The [2026.02.1 patch release](https://github.com/posit-dev/positron/releases/tag/2026.02.1-5) (2026-02-17) provides fixes for Positron Pro on Workbench.

### Release highlights

#### New Positron Notebook Editor is available for alpha testing! 📓

We're excited to invite you to try the new Positron Notebook Editor, our reimagined experience for working with Jupyter (`.ipynb`) notebooks. While still in alpha, we're releasing early because we believe the best tools are built in collaboration with the community.

The Positron Notebook Editor provides a batteries-included environment for data science workflows with integrated panes for inspecting variables and exploring dataframes, context-aware AI that understands your notebook's execution history and variables, and streamlined interpreter management.

To try it out, enable the [`positron.notebook.enabled`](positron://settings/positron.notebook.enabled) setting. Check out our [documentation](https://positron.posit.co/notebooks-alpha) to get started, and please [share your feedback](https://github.com/posit-dev/positron/discussions/10047)!

#### Connections Pane 🔌

The [Connections Pane](https://positron.posit.co/connections-pane) lets you create connections to databases, explore their schemas, and interactively preview tables in the Data Explorer. This release expands Python database support with new drivers for SQL Server (via pymssql or pyodbc), Databricks, Snowflake, and BigQuery, each with multiple authentication methods including OAuth and service account options.

For R users, database connections now also appear in the Variables Pane, making it easier to access and explore your connections alongside other session objects.

#### Breakpoints and debugging in R 🛠️

R now has first-class support for breakpoints in Positron. Set breakpoints in the editor gutter and step through your code interactively. In scripts, breakpoints are enabled after evaluation or sourcing. In packages, install the latest version of pkgload and call `load_all()` to activate breakpoints.

This release also adds debug-specific command history; use <kbd>Ctrl+R</kbd> or <kbd>Cmd/Ctrl+Up</kbd> to navigate through commands from your debugging sessions separately from your regular console history.

<div id="checkbox"></div>

### Changelog

#### New features

- [[#9074](https://github.com/posit-dev/positron/issues/9074)] Per-kernel resource usage information is now displayed in the console tab list.
- [[#10433](https://github.com/posit-dev/positron/issues/10433)] Connections Pane: added support for SQL Server databases using pymssql or pyodbc.
- [[#11080](https://github.com/posit-dev/positron/issues/11080)] Connections Pane: added Python Databricks connection drivers supporting Personal Access Token, OAuth M2M, and OAuth U2M authentication methods.
- [[#9961](https://github.com/posit-dev/positron/issues/9961), [#11078](https://github.com/posit-dev/positron/issues/11078)] Connections Pane: added Snowflake connection support with multiple authentication methods.
- [[#11079](https://github.com/posit-dev/positron/issues/11079)] Connections Pane: added BigQuery connection driver for Python with support for Application Default Credentials and Service Account authentication.
- [[#10818](https://github.com/posit-dev/positron/issues/10818), [#11357](https://github.com/posit-dev/positron/issues/11357)] Connections Pane: added viewer support for R database connections in the Variables Pane.
- [[#7031](https://github.com/posit-dev/positron/issues/7031)] Plots: the Plots Pane now shows which session created the plot.
- [[#10183](https://github.com/posit-dev/positron/issues/10183)] Plots: the Plots Pane can now navigate to, copy, or re-run the code used to create a plot.
- [[#8216](https://github.com/posit-dev/positron/issues/8216)] Assistant: added [`positron.assistant.aiExcludes`](positron://settings/positron.assistant.aiExcludes) setting to exclude files from all AI features including inline completions and chat context.
- [[#10967](https://github.com/posit-dev/positron/issues/10967)] Assistant: improved reliability of Positron Assistant to edit files directly while in Edit mode.
- [[#11166](https://github.com/posit-dev/positron/issues/11166)] Assistant: model picker now shows a "(Default)" indicator next to the model configured as default for each provider.
- [[#11463](https://github.com/posit-dev/positron/issues/11463)] Assistant: added setting to configure Amazon Bedrock inference profile region for use with Positron Assistant.
- [[#8075](https://github.com/posit-dev/positron/issues/8075)] Added support for using R and Python installations via environment modules/Lmod.
- [[#11246](https://github.com/posit-dev/positron/issues/11246)] Added new button to interrupt a running Shiny app (Python or R) from the Viewer pane.
- [[#8870](https://github.com/posit-dev/positron/issues/8870)] Python: Assistant will now use `uv add` when appropriate when installing Python packages.
- [[#3156](https://github.com/posit-dev/positron/issues/3156), [#10045](https://github.com/posit-dev/positron/issues/10045)] Python: If code is run from an editor, the editor path is now added to `sys.path` for that cell.
- [[#3673](https://github.com/posit-dev/positron/issues/3673)] R: opening a file via `rstudioapi::navigateToFile(path)` now opens a non-preview, pinned editor.
- [[#2955](https://github.com/posit-dev/positron/issues/2955)] R: added [`positron.r.localPackageInstallMethod`](positron://settings/positron.r.localPackageInstallMethod) setting to use base R commands for package development tasks. When changed from the default, uses `R CMD INSTALL` instead of pak for installing a local R package project.
- [[#1766](https://github.com/posit-dev/positron/issues/1766)] R: gained support for breakpoints. In scripts, breakpoints are enabled after evaluation or sourcing. In packages, you need to install the latest version of pkgload (e.g. with `pak::pak("r-lib/pkgload")`) and call `load_all()` to activate breakpoints.
- [[#11289](https://github.com/posit-dev/positron/issues/11289)] Data Explorer: added new [`dataExplorer.enablePreview`](positron://settings/dataExplorer.enablePreview) setting that controls whether preview mode is used for Data Explorer tabs (similar to `workbench.editor.enablePreview` for regular editors).
- [[#10516](https://github.com/posit-dev/positron/issues/10516)] Release notes now display a header with the Positron logo and version number for clearer identification.

#### Bug fixes

- [[#11370](https://github.com/posit-dev/positron/issues/11370)] The [`remoteSSH.serverInstallPath`](positron://settings/remoteSSH.serverInstallPath) setting now puts all server data in the specified directory, instead of just the server binary. **BREAKING CHANGE:** if you were using a custom `serverInstallPath` and don't want to lose application state, make sure to move the files on your remote host in `~/.positron-server` to that custom path.
- [[#3651](https://github.com/posit-dev/positron/issues/3651)] Plots: fixed poor contrast ratio in the Close button in the Plot history.
- [[#9891](https://github.com/posit-dev/positron/issues/9891)] Assistant: settings for sharing Copilot tools/participants across providers are clearer about possible data sharing.
- [[#11188](https://github.com/posit-dev/positron/issues/11188)] Assistant: fixed model preference matching by provider to be case-insensitive as documented.
- [[#9170](https://github.com/posit-dev/positron/issues/9170)] Assistant: the `/doc` command no longer modifies code logic, only comments/docstrings.
- [[#11390](https://github.com/posit-dev/positron/issues/11390)] Assistant: Amazon Bedrock providers stay enabled across restarts of Positron.
- [[#10212](https://github.com/posit-dev/positron/issues/10212)] Assistant can no longer make edits when in Ask mode.
- [[#10818](https://github.com/posit-dev/positron/issues/10818)] Assistant: updated `ai-sdk` to v5, providing updated behavior for OpenAI-compatible model providers.
- [[#9750](https://github.com/posit-dev/positron/issues/9750)] Assistant works more consistently when interfacing with variable names & access keys.
- [[#10327](https://github.com/posit-dev/positron/issues/10327)] Assistant: OpenAI now works when [`positron.assistant.alwaysIncludeCopilotTools`](positron://settings/positron.assistant.alwaysIncludeCopilotTools) is enabled.
- [[#10759](https://github.com/posit-dev/positron/issues/10759)] Assistant: fixed `getPlot` tool errors for OpenAI-compatible providers.
- [[#11054](https://github.com/posit-dev/positron/issues/11054)] Changed default for [`terminal.integrated.detectLocale`](positron://settings/terminal.integrated.detectLocale) to `'on'` to ensure consistent locale behavior, fixing issues where R and Python sessions could behave differently across platforms.
- [[#11453](https://github.com/posit-dev/positron/issues/11453)] Python: fixed the Streamlit web app detection regex.
- [[#9230](https://github.com/posit-dev/positron/issues/9230)] Python: fixed bug where Python's builtin `map` was eagerly consumed by the Variables Pane.
- [[#7052](https://github.com/posit-dev/positron/issues/7052), [#9069](https://github.com/posit-dev/positron/issues/9069)] R: fixed language features (completions, outline, statement code execution) not working after an extension host restart or reloading the window.
- [[#11402](https://github.com/posit-dev/positron/issues/11402)] R: <kbd>Ctrl+R</kbd> and <kbd>Cmd/Ctrl+Up</kbd> now support debug-specific command histories.
- [[#5024](https://github.com/posit-dev/positron/issues/5024)] R: fixed a deadlock occurring when stepping rapidly in the debugger.
- [[#1006](https://github.com/posit-dev/ark/issues/1006)] R: fixed regression where evaluating empty lines was no longer interpreted as stepping to next expression in the debugger.
- [[#855](https://github.com/quarto-dev/quarto/issues/855)] Fixed spurious diagnostics from Quarto virtual documents appearing in Problems pane.
- [[#11161](https://github.com/posit-dev/positron/issues/11161)] Fixed "Initialize Git Repository" option not working for an empty project in the New Folder from Template flow.
- [[#11322](https://github.com/posit-dev/positron/issues/11322)] Fixed error messages when attempting to install an extension that is incompatible with the version of Positron.
- [[#10488](https://github.com/posit-dev/positron/issues/10488)] Fixed issue causing a mixup in tab titles when native macOS tabs are enabled.
- [[#11230](https://github.com/posit-dev/positron/issues/11230)] Fixed console startup hang when launching Positron for the first time after an upgrade.

#### Dependencies

- Updated `vscode-python` upstream to v2026.0.0.
- Updated bundled Quarto to 1.8.27.
- Updated bundled version of Air to [0.20.0](https://github.com/posit-dev/air/blob/main/editors/code/CHANGELOG.md#0200).
