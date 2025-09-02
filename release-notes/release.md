### Highlights

#### Positron Assistant 🤖

Positron Assistant, currently available as a preview feature, is now more powerful and versatile. New slash commands (`/fix`, `/explain`, and `/doc`) are available to debug, understand, and document code. These commands can even be triggered automatically; for example, you can convert a chat into a Quarto document just by asking, "Can you convert this to Quarto?", even if you don't specify the `/exportQuarto` command as part of your message.

"Fix" and "Explain" support for Console errors has also been introduced. With a single click, the Assistant can fix or explain an error, acting as a coding partner for troubleshooting. You can try it out by enabling the [`positron.assistant.consoleActions.enable` setting](positron://settings/positron.assistant.consoleActions.enable). 

Ways you already use Assistant have been enhanced. Code completions and inline chat are now available in notebooks, giving you access to the features you love no matter where you code. Assistant now also integrates with Git by default, letting you seamlessly chat about your project's history and providing suggestions when writing commit messages. Assistant can also now use the data summary tool for R objects, similar to what you have already been able to do in Python.

#### Convert your Data Explorer filters to code 💥

The Data Explorer now provides a **Convert to Code** button to make your analysis more reproducible. With one click, you can copy code to your clipboard that reflects the filters and sorts you have set up via the Data Explorer UI. Paste the code into the Console, a script, or a notebook to continue your data exploration with runnable, reproducible code. This feature currently supports both pandas and polars Python dataframes, with additional backends coming soon! 

#### DuckDB for Python 🦆

The [Connections Pane](https://positron.posit.co/connections-pane.html) now supports managing and exploring native DuckDB connections in Python, as has already been possible for R. Connect to local or remote DuckDB databases, explore their schemas, and interactively preview your DuckDB tables.

<div id="checkbox"></div>

### Changelog

#### New features

- [[#8530](https://github.com/posit-dev/positron/issues/8530), [#8696](https://github.com/posit-dev/positron/issues/8696), [#8719](https://github.com/posit-dev/positron/issues/8719), [#8753](https://github.com/posit-dev/positron/issues/8753), [#9139](https://github.com/posit-dev/positron/issues/9139)] Data Explorer filters created in the UI can be converted to runnable, reproducible code for pandas and polars data frames.
- [[#4370](https://github.com/posit-dev/positron/issues/4370)] Data Explorer: summary panel is now collapsed by default if its width would exceed 50% of the available space.
- [[#8395](https://github.com/posit-dev/positron/issues/8395)] Data Explorer: added tooltips to top-left and bottom-right corner square buttons to clarify quick-scrolling behaviors.
- [[#9096](https://github.com/posit-dev/positron/issues/9096)] Data Explorer: column profiles render more smoothly and incrementally for tables with many rows.
- [[#6509](https://github.com/posit-dev/positron/issues/6509)] Data Explorer: keep the collapse control always visible.
- [[#8692](https://github.com/posit-dev/positron/issues/8692)] Assistant: improved console traceback context summary.
- [[#7740](https://github.com/posit-dev/positron/issues/7740)] Assistant: now display a "Working..." indicator while a response is in progress.
- [[#7370](https://github.com/posit-dev/positron/issues/7370)] Assistant: added new slash commands `/fix`, `/explain`, and `/doc` especially for use in inline chat.
- [[#8579](https://github.com/posit-dev/positron/issues/8579)] Assistant: added "Fix" and "Explain" buttons on tracebacks in the Console.
- [[#8598](https://github.com/posit-dev/positron/issues/8598)] Assistant: now provide a new global [`positron.assistant.consoleActions.enable` setting](positron://settings/positron.assistant.consoleActions.enable) to disable Console integration. 
- [[#7370](https://github.com/posit-dev/positron/issues/7370)] Assistant: added editor inline chat slash commands to capture user intent.
- [[#8061](https://github.com/posit-dev/positron/issues/8061)] Assistant: Copilot inline completions are now available in Jupyter notebooks.
- [[#8871](https://github.com/posit-dev/positron/issues/8871)] Assistant: allow use of an Anthropic API key set via environment variable.
- [[#8343](https://github.com/posit-dev/positron/issues/8343)] Assistant can now use the data summary tool for R objects.
- [[#9066](https://github.com/posit-dev/positron/issues/9066)] Assistant: git integration Assistant tools are now available by default.
- [[#8305](https://github.com/posit-dev/positron/issues/8305)] Assistant: code generation now avoids unnecessary `print()` and similar statements.
- [[#7988](https://github.com/posit-dev/positron/issues/7988)] Added new [`notebook.workingDirectory` setting](positron://settings/notebook.workingDirectory), which can be used to set the default working directory for notebooks.
- [[#8563](https://github.com/posit-dev/positron/issues/8563)] Positron's reticulate integration will now be automatically enabled in workspaces where the reticulate R package has been loaded at least once; read more [in the reticulate documentation](https://positron.posit.co/reticulate).
- [[#8988](https://github.com/posit-dev/positron/issues/8988)] Python: added support for managing and exploring native DuckDB connections in the Connections Pane.
- [[#3906](https://github.com/posit-dev/positron/issues/3906)] Added initial support for debugging Python Jupyter notebooks.
- [[#8731](https://github.com/posit-dev/positron/issues/8731)] macOS: When the [`window.nativeTabs` setting](positron://settings/window.nativeTabs) is set to `true`, new windows will now always open in native tabs. Previously they would only do so if the global macOS setting to always prefer opening in native tabs was also set.

#### Bug fixes

- [[#8760](https://github.com/posit-dev/positron/issues/8760)] Data Explorer: now correctly filter `YYYY-MM-DD` values for pandas data frames.
- [[#8808](https://github.com/posit-dev/positron/issues/8808)] Data Explorer: fixed issues opening certain atypical Parquet files via the File Explorer pane.
- [[#8515](https://github.com/posit-dev/positron/issues/8515)] Data Explorer: fixed how null percentage values are displayed in the tooltip for small percentages.
- [[#8936](https://github.com/posit-dev/positron/issues/8936)] Data Explorer: streamlined the missing values tooltip for clarity.
- [[#8574](https://github.com/posit-dev/positron/issues/8574)] Assistant: fixed model provider switcher theme.
- [[#8207](https://github.com/posit-dev/positron/issues/8207)] Assistant: fixed adding a specific git commit as context item.
- [[#8755](https://github.com/posit-dev/positron/issues/8755)] Assistant: fixed `invalid base64 data` error when viewing the active plot.
- [[#9125](https://github.com/posit-dev/positron/issues/9125)] Assistant: fixed issue preventing git commit info from being constructed on Windows.
- [[#8770](https://github.com/posit-dev/positron/issues/8770)] Workbench: fixed error loading webview service worker on Chrome.
- [[#8785](https://github.com/posit-dev/positron/issues/8785)] Workbench: fixed non-HTML content being served through Positron Proxy for the Viewer Pane.
- [[#8510](https://github.com/posit-dev/positron/issues/8510)] Workbench: fixed log level problem, which was causing excessive log volumes in the user directory.
- [[#8930](https://github.com/posit-dev/positron/issues/8930)] Workbench: fixed Data Explorer scrollbars on Safari.
- [[#8867](https://github.com/posit-dev/positron/issues/8867)] Fixed a bug in how imported VS Code settings were displayed.
- [[#8637](https://github.com/posit-dev/positron/issues/8637)] Resolved keyboard shortcut conflict for code cells in `.R` files.
- [[#8794](https://github.com/posit-dev/positron/issues/8794)] Fixed the rstudioapi shim for `rstudioapi::restartSession()`.
- [[#7679](https://github.com/posit-dev/positron/issues/7679), [#7681](https://github.com/posit-dev/positron/issues/7681)] R plots created in steps with prompts in between (e.g. `demo(graphics)`) are now immediately displayed in full.
- [[#8941](https://github.com/posit-dev/positron/issues/8941)] R plots created in steps are now consistently rendered with expected rendering settings.
- [[#8881](https://github.com/posit-dev/positron/issues/8881)] R comment sections nested in control flow operations like `if` / `else` are now included in the outline.
- [[#8374](https://github.com/posit-dev/positron/issues/8374), [#8504](https://github.com/posit-dev/positron/issues/8504)] R: fixed an issue preventing the R backend from opening files on Windows.
- [[#4651](https://github.com/posit-dev/positron/issues/4651)] R: fixed an issue preventing virtual namespaces (created by Ark when debugging or viewing a function from a package that doesn't have source references) on Windows.
- [[#8964](https://github.com/posit-dev/positron/issues/8964)] Fixed padding on Connection Pane modals.
- [[#8661](https://github.com/posit-dev/positron/issues/8661)] Restored keyboard shortcuts for Quarto run commands <kbd>Ctrl+Enter</kbd> and <kbd>Ctrl+Shift+Enter</kbd> on Mac, in addition to <kbd>Cmd</kbd> versions.
- [[#9020](https://github.com/posit-dev/positron/issues/9020)] Fixed problem starting R and Python sessions when 'Run in Login Shell' is enabled and the user's `SHELL` is `csh`.


#### Dependencies

- Updated `code-oss` upstream to v1.103.0.
