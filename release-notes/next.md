### Highlights

#### Remote sessions 🚀

This release brings a slew of improvements to the remote SSH experience in Positron. We've improved:

- our UI treatment of configured hosts
- the command to connect to your remote machine(s)
- bundling of components such as Quarto
- what happens when something goes wrong with the server download on your remote machine
- how you can manage the installation location of Positron server

Additionally, the most upvoted feature in this month's release is native support for remote sessions on WSL (Windows Subsystem for Linux). You can now connect to WSL distributions as remote sessions in Positron, giving you a seamless development experience when working with Linux-based environments on Windows. If you previously used the community-maintained extension for WSL support, you will want to uninstall that extension and transition to the built-in functionality.

#### Positron Assistant 🤖

Our new release brings initial preview support for using [Positron Assistant](https://positron.posit.co/assistant) with models provided by Amazon Bedrock, in addition to the existing support for models provided by Anthropic, GitHub Copilot, and [OpenAI and OpenAI-compatible providers](https://github.com/posit-dev/positron/discussions/9988).

Positron Pro sessions on Posit Workbench benefit from a smoother authentication experience with [Workbench-managed AWS Credentials](https://docs.posit.co/ide/server-pro/user/posit-workbench/managed-credentials/aws.html). Positron Desktop users can get started with Bedrock models by [manually authenticating via the AWS CLI](https://github.com/posit-dev/positron/discussions/10322).

We'll continue to improve the Bedrock experience in Positron, particularly around authentication. Stay tuned for updates in future releases!

#### Customize your plots display 📊

One of the most upvoted features in this month's release is a new setting to customize the default sizing policy for the Plots pane, giving you more control over how your visualizations are displayed. Use the new [`plots.defaultSizingPolicy` setting](positron://settings/plots.defaultSizingPolicy) to configure how your plots are displayed by default if, for example, you prefer to always start with the "fill" option instead of the "auto" option. You can still change the sizing policy via the UI for plots after they are created, but this setting lets you set your preferred default behavior.

<div id="checkbox"></div>

### Changelog

#### New features

- [[#10039](https://github.com/posit-dev/positron/issues/10039)] Added new preview Catalog Explorer functionality for interacting with data catalogs, with initial support today available for Databricks catalogs. This feature is in preview and can be enabled by opting in to the new [`catalogExplorer.enable` setting](positron://settings/catalogExplorer.enable).
- [[#4366](https://github.com/posit-dev/positron/issues/4366)] Remote sessions: added native support for remote sessions on WSL.
- [[#4799](https://github.com/posit-dev/positron/issues/4799)] Remote sessions: improved _Remote-SSH: Connect to host_ command.
- [[#10017](https://github.com/posit-dev/positron/issues/10017)] Remote sessions: the new [`remoteSSH.serverInstallPath` setting](positron://settings/remoteSSH.serverInstallPath) lets you customize the directory for the Positron server installation.
- [[#9788](https://github.com/posit-dev/positron/issues/9788), [#9983](https://github.com/posit-dev/positron/issues/9983)] Assistant: added [a new setting `positron.assistant.filterModels`](positron://settings/positron.assistant.filterModels) to configure available models. Positron provides defaults to this setting to only show models that are known to work well with Positron Assistant, but you can customize it as needed.
- [[#9388](https://github.com/posit-dev/positron/issues/9388)] Assistant: added [a new setting `positron.assistant.preferredModel`](positron://settings/positron.assistant.preferredModel) to set the preferred model to pre-select in the model selector. 
- [[#9388](https://github.com/posit-dev/positron/issues/9388)] Assistant: added [a new setting `positron.assistant.defaultModels`](positron://settings/positron.assistant.defaultModels) to set the default model per provider. 
- [[#9738](https://github.com/posit-dev/positron/issues/9738), [#9643](https://github.com/posit-dev/positron/issues/9643)] Assistant: now dynamically fetch Bedrock models from AWS.
- [[#9563](https://github.com/posit-dev/positron/issues/9563)] Assistant: enabled custom chat modes, instructions, and prompt files.
- [[#10174](https://github.com/posit-dev/positron/issues/10174)] Assistant: simplified project tree tool output structure.
- [[#9847](https://github.com/posit-dev/positron/issues/9847)] Data Explorer: updated the column selector to use our new backend search.
- [[#6582](https://github.com/posit-dev/positron/issues/6582)] Python: switched interpreter discovery to use the native locator by default.
- [[#10094](https://github.com/posit-dev/positron/issues/10094)] R: Positron now reads R repository configuration from `/etc/rstudio/repos.conf` automatically if no other repository configuration is present.
- [[#964](https://github.com/posit-dev/positron/issues/964)] R: added a new setting [`positron.r.saveAndRestoreWorkspace`](positron://settings/positron.r.saveAndRestoreWorkspace) to opt in to saving a workspace to `.RData` on exit and restoring on startup.
- [[#1301](https://github.com/posit-dev/positron/issues/1301)] The Shiny extension (which provides support for both Python and R) is now included as a bootstrap installed extension.
- [[#9554](https://github.com/posit-dev/positron/issues/9554)] Added support for Databricks-style `# COMMAND ----------` code cells in `.py` and `.R` files. You can customize this behavior by changing the new [`codeCells.additionalCellDelimiter` setting](positron://settings/codeCells.additionalCellDelimiter).
- [[#9573](https://github.com/posit-dev/positron/issues/9573)] Workbench: settings in Positron can now be enforced by Workbench admins. 
- [[#8393](https://github.com/posit-dev/positron/issues/8393)] Now support pasting or dropping files as paths in R and Python scripts. You can now copy files from a file manager and paste (or <kbd>Shift</kbd> then drop) into an R or Python file to automatically insert properly formatted, quoted file paths. Paths use forward slashes and are made relative when possible.
- [[#7268](https://github.com/posit-dev/positron/issues/7268)] Added new [`plots.defaultSizingPolicy` setting](positron://settings/plots.defaultSizingPolicy) to configure the sizing policy used for creating plots, and updated other existing plots settings to have new names [`plots.darkFilter`](positron://settings/plots.darkFilter) and [`plots.freezeSlowPlots`](positron://settings/plots.freezeSlowPlots).

#### Bug fixes

- [[#9416](https://github.com/posit-dev/positron/issues/9416), [#9747](https://github.com/posit-dev/positron/issues/9747)] Assistant: fixed how Anthropic models call Copilot participants.
- [[#9283](https://github.com/posit-dev/positron/issues/9283)] Assistant: removed non-functional providers from "Manage models..." quickpick.
- [[#9919](https://github.com/posit-dev/positron/issues/9919)] Assistant: fixed the behavior of Assistant’s Console actions when Assistant is not enabled at all.
- [[#9929](https://github.com/posit-dev/positron/issues/9929)] Assistant: fixed streaming selection edits.
- [[#9990](https://github.com/posit-dev/positron/issues/9990)] Assistant: fixed tool to read R package help documentation.
- [[#9209](https://github.com/posit-dev/positron/issues/9209)] Assistant: quick chat now sources its model & context from the main chat interface.
- [[#9438](https://github.com/posit-dev/positron/issues/9438)] Assistant: Bedrock models no longer error in Agent mode when using Copilot tools.
- [[#10007](https://github.com/posit-dev/positron/issues/10007)] Assistant: fixed how Copilot accesses Positron's tools.
- [[#9861](https://github.com/posit-dev/positron/issues/9861)] Assistant: Positron Assistant no longer stops after tool errors. The assistant now sees and responds to tool failures instead of ending the conversation.
- [[#8347](https://github.com/posit-dev/positron/issues/8347)] Assistant: now exclude the "Install Python Package" tool from Assistant Ask mode.
- [[#9047](https://github.com/posit-dev/positron/issues/9047)] Remote sessions: fixed errors connecting to WSL when using IPC transport.
- [[#8848](https://github.com/posit-dev/positron/issues/8848)] Remote sessions: if downloading the server tarball is canceled during Remote SSH, it will be retried upon the next connection.
- [[#6692](https://github.com/posit-dev/positron/issues/6692)] Remote sessions: addressed an issue that could create orphaned R and Pythons sessions in Remote SSH.
- [[#9812](https://github.com/posit-dev/positron/issues/9812)] Data Explorer: fixed formatting in histogram tooltips.
- [[#9836](https://github.com/posit-dev/positron/issues/9836)] Data Explorer: fixed layout problems when the summary panel is on the right.
- [[#9365](https://github.com/posit-dev/positron/issues/9365)] Python: no longer show unsupported Python versions in the New Folder Template flow.
- [[#9186](https://github.com/posit-dev/positron/issues/9186)] Python: fixed bug where environments created by Positron were displayed as version 0.0.1 on Windows.
- [[#9216](https://github.com/posit-dev/positron/issues/9216)] R: fixed handling of paths to R on Windows.
- [[#9813](https://github.com/posit-dev/positron/issues/9813)] R: now report the working directory with correct slashes on Windows, in the Console action bar.
- [[#8453](https://github.com/posit-dev/positron/issues/8453)] R: on linux 64-bit distros, "lib64" R_HOME paths are detected before "lib" R_HOME paths.
- [[#9985](https://github.com/posit-dev/positron/issues/9985)] R: fixed `browseURL()` behavior for non-ASCII text on Windows.
- [[#9467](https://github.com/posit-dev/positron/issues/9467)] R: fixed a crash when interrupting R while output is emitted in the console.
- [[#9927](https://github.com/posit-dev/positron/issues/9927)] R: the setting that restores an R workspace is now respected on Windows. Thanks to our contributor [@kv9898](https://github.com/kv9898)!
- [[#917](https://github.com/posit-dev/ark/issues/917)] R: the R backend is now more robust to loading issues of internal graphics packages such as ragg.
- [[#10192](https://github.com/posit-dev/positron/issues/10192)] The R backend now works on macOS 11. Thanks to our contributor [@kv9898](https://github.com/kv9898)!
- [[#9488](https://github.com/posit-dev/positron/issues/9488)] Workbench: fixed a bug when opening workspaces such as with `usethis::create_from_github()`.
- [[#10060](https://github.com/posit-dev/positron/issues/10060)] Workbench: fixed Positron details in the "About" dialog.
- [[#9631](https://github.com/posit-dev/positron/issues/9631)] Fixed the [`notebook.workingDirectory` setting](positron://settings/notebook.workingDirectory) for untitled Jupyter notebooks.
- [[#7205](https://github.com/posit-dev/positron/issues/7205)] Fixed the `positron.RuntimeCodeExecutionMode.Silent` behavior for extensions, for queued code in the console. Thanks to our contributor [@kv9898](https://github.com/kv9898)!
- [[#7861](https://github.com/posit-dev/positron/issues/7861)] Fixed what Positron reports to extensions in `positron.runtime.getForegroundSession()`.
- [[#9820](https://github.com/posit-dev/positron/issues/9820)] Fixed Quarto bundling on Windows.
- [[#9575](https://github.com/posit-dev/positron/issues/9575)] Removed the limit on active console and notebook sessions.

#### Dependencies

- Updated `code-oss` upstream to v1.105.0.
- Updated `vscode-python` upstream to v2025.16.0.
- Updated bundled version of the Air extension to 0.18.0. This update includes experimental support for tabular calls like `tibble::tribble()` and `data.table::fcase()`.