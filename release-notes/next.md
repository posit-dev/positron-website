### Release highlights

Welcome to the 2026.11.0 release of Positron!

- [Object Explorer](#object-explorer)
- [Interpreter selection](#interpreter-selection)
- [More for Posit Assistant and other agents](#more-for-posit-assistant-and-other-agents)
- [Data Connections](#data-connections)
- [A smaller, faster Positron](#a-smaller-faster-positron)

<div id="checkbox"></div>

#### Object Explorer

Our new Object Explorer is like the [Data Explorer](https://positron.posit.co/data-explorer?utm_source=positron&utm_medium=referral&utm_campaign=positron-2026-11-release-highlights&utm_content=object-explorer-section), but for data that is not rectangular, such as R lists, model fits, Python dicts, and JSON files. This was [the most upvoted issue](https://github.com/posit-dev/positron/issues/3028) that we completed this release.

<p align="center"><img src="https://cdn.posit.co/positron/releases/release-notes/assets/2026-11-object-explorer.gif" alt="Opening a nested Python dictionary of model results in the Object Explorer from a Quarto document, expanding test metrics by segment, and opening a nested data frame in the Data Explorer"></p>

The Object Explorer shows your object as a tree with name, type, and value columns, and it opens large or deeply nested objects quickly. You can search across names and values, open a nested data frame in the Data Explorer, and copy the code that gets to any item, such as `fit$coefficients[["wt"]]`. When the variable changes, the Object Explorer updates.

To open the Object Explorer, run `%view` in Python or `View()` in R, or click the view button in the Variables pane. In the editor, you can also use the **Open in Object Explorer** code action on a variable. In Positron notebooks and Quarto documents, nested output shows as a small inline explorer. You can also open a JSON file in the Object Explorer, and generate code to import it into R or Python.

#### Interpreter selection

For Python, Positron now uses one ranked list to choose the interpreter to start for a project. The list starts with the environment that is active in the shell that launched Positron. Next come [`python.defaultInterpreterPath`](positron://settings/python.defaultInterpreterPath), the project environment such as `.venv`, the version in `.python-version`, and then other environments. A project environment starts before interpreter discovery finishes, so your console is ready sooner.

Positron also finds environments one level below the workspace root, such as at `app/.venv`. Base and externally managed installs, such as Homebrew Python, no longer start automatically and instead only start when you select them.

The interpreter picker groups Python interpreters into project, global, base, and externally managed interpreters, with short labels such as "Python 3.12.4". It also tells you why it suggests an interpreter, for example because it was identified as the project environment. In a folder with no environment, the picker suggests **Create Python Environment** or **Install Python**. This release adds support for Python 3.15 and removes support for Python 3.9.

For R, the interpreter picker shows all R versions in one group, with your current R first. When you have more than one R version, Positron uses your current R by default, and R no longer starts automatically in a folder with no R files. Positron also finds Pixi R installations when you open a Pixi project.

#### More for Posit Assistant and other agents

[Posit Assistant](https://assistant.posit.co/?utm_source=positron&utm_medium=referral&utm_campaign=positron-2026-11-release-highlights&utm_content=assistant-section) and other coding agents that use the Positron MCP server can now do more with Positron. Agents can read help pages and vignettes from your installed R and Python packages, so they can answer questions about packages that they do not know from their training data. They can also read the output of data apps that Positron runs, read Viewer output such as Plotly charts, and trace Snowflake data lineage. To learn more, read our recent blog post on how [Posit Assistant can drive Positron](https://opensource.posit.co/blog/2026-10-21_assistant-drives-positron/?utm_source=positron&utm_medium=referral&utm_campaign=positron-2026-11-release-highlights&utm_content=assistant-section).

Posit Assistant knows about the active Data Explorer, including its filters, sorting, and selection, and can run chunks and read inline output in Quarto documents. When Assistant runs code, it no longer moves your focus or replaces the tab that you have open. AI provider sign-in, including [Posit AI Pass](https://posit.ai?utm_source=positron&utm_medium=referral&utm_campaign=positron-2026-11-release-highlights&utm_content=assistant-ai-pass), now also lives in Posit Assistant.

For other coding agents, the Positron MCP server now starts through a launcher at a stable path, so your agent configuration keeps working after Positron upgrades. _Positron MCP: Add to Coding Agent_ can now also set up OpenCode, Copilot CLI, and Kiro CLI. **Fix** and **Explain** on errors can send the error to a coding agent such as Claude Code, with the [`ai.errorActions.agent`](positron://settings/ai.errorActions.agent) setting.

To try these features with Posit Assistant, enable the [`assistant.previewFeatures`](positron://settings/assistant.previewFeatures) setting. For other coding agents, enable the experimental [`ai.mcp.enabled`](positron://settings/ai.mcp.enabled) setting.

#### Data Connections

[Data Connections](https://positron.posit.co/data-connections?utm_source=positron&utm_medium=referral&utm_campaign=positron-2026-11-release-highlights&utm_content=data-connections-section) now supports MotherDuck. Positron reads your access token from the `motherduck_token` environment variable, so you can browse your databases, preview tables in the Data Explorer, and generate connection code. 

To keep the connections for one project out of your other workspaces, select **This Workspace Only** when you configure a connection. Group rows such as **Tables** and **Views** now show how many items they hold. Tables that you open from the Data Connections pane have a **Refresh** action in the Data Explorer toolbar. It shows changes made outside Positron and keeps your sort and filters. Scrolling and copying rows from PostgreSQL, Redshift, Snowflake, Databricks, and ODBC connections no longer repeats or skips rows. Snowflake `NUMBER` and DuckDB `DECIMAL` values are no longer rounded.

SQL files can now use a data connection for language features. Positron offers table and column completions from the connected database, warns about names that are not in its schema, and follows the SQL dialect of the driver. A status bar item shows the connection for the file. To try these new features, enable the [`sql.enabled`](positron://settings/sql.enabled) setting.

#### A smaller, faster Positron

Positron is about 224 MB smaller on each platform, because its extensions now share one copy of the DuckDB library. The bundled Python kernel has about 1,900 fewer files, and Positron Server and [Posit Workbench](https://posit.co/products/enterprise/workbench?utm_source=positron&utm_medium=referral&utm_campaign=positron-2026-11-release-highlights&utm_content=faster-workbench) installs are smaller too. Fewer files help most when you install Positron on a network file system, where startup, upgrades, and antivirus scans can slow down with each file.

Positron also does less work in the background now. Interpreter discovery no longer runs again on every launch after a long break, and a project environment starts before discovery finishes. On Workbench, Positron stops trying to reconnect after your session exits, and checks your login less often.

### Changelog

#### New features

- [[#8709](https://github.com/posit-dev/positron/issues/8709)] Assistant: Posit Assistant knows about the active Data Explorer, including its data source, filters, sorting, cursor, and selection.
- [[#14733](https://github.com/posit-dev/positron/issues/14733)] Assistant: Posit Assistant can run chunks and read inline output in Quarto documents that use inline output.
- [[#15724](https://github.com/posit-dev/positron/issues/15724)] Assistant: Posit Assistant can read help pages and vignettes from installed R and Python packages.
- [[#16377](https://github.com/posit-dev/positron/issues/16377)] Assistant: Posit Assistant can read and use output in the Viewer from a console session or a Quarto chunk, such as Plotly charts. On Desktop, this includes Quarto output that opens in the Viewer.
- [[#15848](https://github.com/posit-dev/positron/issues/15848)] Assistant: Posit Assistant can read the output of data apps that Positron runs. This helps it troubleshoot an app that fails to start or gives an error on a request.
- [[#15160](https://github.com/posit-dev/positron/issues/15160)] Assistant: Posit Assistant can trace Snowflake data lineage, upstream and downstream, for tables, views, and columns in your data connections.
- [[#15778](https://github.com/posit-dev/positron/issues/15778)] Assistant: Posit Assistant runs Positron commands that only read data or change what shows on screen without asking first, for example to list settings, packages, or sessions. It shows a readable name for each command it runs, such as "Get Configured Settings".
- [[#16963](https://github.com/posit-dev/positron/pull/16963)] Assistant: when you enable it, Posit Assistant can start and run code in any console or notebook session without a change to the active console or to focus.
- [[#13394](https://github.com/posit-dev/positron/issues/13394)] Assistant: when Posit Assistant runs code, the Console and Plots tabs no longer replace a different tab that you have open in the same area. The output is ready when you switch back.
- [[#12838](https://github.com/posit-dev/positron/issues/12838)] Assistant: the Quarto editor has AI actions, with **Ask Assistant**, suggested prompts for Quarto, and support to follow the edits of the assistant.
- [[#16092](https://github.com/posit-dev/positron/issues/16092)] Assistant: AI provider sign-in now lives in Posit Assistant. Your existing API keys and Posit AI Pass sign-in carry over.
- [[#16611](https://github.com/posit-dev/positron/issues/16611)] Assistant: Git commit messages and notebook AI use the provider code from the installed Posit Assistant when it is newer than the copy in Positron. New providers arrive with Posit Assistant updates.
- [[#16365](https://github.com/posit-dev/positron/issues/16365)] Assistant: AI settings have their own **AI** group under **Features** in the Settings editor.
- [[#13603](https://github.com/posit-dev/positron/issues/13603)] Assistant: **Fix** and **Explain** on console, notebook, and Quarto errors can send the error to a supported third-party coding agent, such as Claude Code. Choose the agent with the [`ai.errorActions.agent`](positron://settings/ai.errorActions.agent) setting.
- [[#16901](https://github.com/posit-dev/positron/issues/16901)] Assistant: _AI: Create Diagnostic Report_ includes the Posit Assistant settings report.
- [[#16344](https://github.com/posit-dev/positron/issues/16344)] Python: Positron supports Python 3.15.
- [[#15825](https://github.com/posit-dev/positron/issues/15825)] Python: Positron picks the Python interpreter to start from one ranked list: the environment of the launch shell, [`python.defaultInterpreterPath`](positron://settings/python.defaultInterpreterPath), the project environment, `.python-version`, and then other environments.
- [[#16168](https://github.com/posit-dev/positron/issues/16168)] Python: Positron discovers Python environments one level below the workspace root, such as `app/.venv`.
- [[#16536](https://github.com/posit-dev/positron/issues/16536)] R: R sessions tell the cli package that Positron supports 24-bit color. Packages that use hex colors show the exact colors in the Console, notebooks, and Quarto inline output.
- [[#11358](https://github.com/posit-dev/positron/issues/11358)] R: the Variables pane shows the properties of S7 objects, and you can expand them.
- [[#16694](https://github.com/posit-dev/positron/issues/16694)] R: `View()` works on character and other atomic vectors.
- [[#15353](https://github.com/posit-dev/positron/issues/15353)] Connections: you can limit a data connection to one workspace. Connections stay global by default.
- [[#15353](https://github.com/posit-dev/positron/issues/15353)] Connections: Positron checks the database file path of SQLite and DuckDB connections when you save, and saves it as an absolute path. Before, a relative path pointed at a different file in each project.
- [[#15100](https://github.com/posit-dev/positron/issues/15100)] Connections: added MotherDuck as a data connection provider. Connect with the `motherduck_token` environment variable, browse your databases, preview tables in the Data Explorer, and generate connection code for Python, R, and ggsql.
- [[#16100](https://github.com/posit-dev/positron/issues/16100)] Connections: the SQL Server connection form has an **Authentication** option, so you can set Microsoft Entra sign-in modes such as `ActiveDirectoryIntegrated` without a hand-written connection string.
- [[#14630](https://github.com/posit-dev/positron/issues/14630)] Connections: group rows in the Data Connections pane, such as **Tables** and **Views**, show how many items they hold, for example "Tables (14)". For most drivers, the count shows before you expand the group.
- [[#15871](https://github.com/posit-dev/positron/issues/15871)] Connections: the Data Connections pane shows the **Views** group only for databases and schemas that contain views.
- [[#16717](https://github.com/posit-dev/positron/issues/16717)] Data Explorer: you can refresh a table that you open from the Data Connections pane to see changes made outside Positron. Sort and filters stay. A filter on a column that no longer exists stays in the filter bar, marked as not valid.
- [[#16910](https://github.com/posit-dev/positron/pull/16910)] Data Explorer: for a large database table or view with no enforced key, the Data Explorer shows the first 10,000 rows. The status bar says so, for example "First N of M rows". You can still scroll all rows of a table with an enforced key.
- [[#15929](https://github.com/posit-dev/positron/issues/15929)] Interpreter: the interpreter picker sorts Python interpreters into Project, Global, Base, and Externally managed groups, with short labels such as "Python 3.12.4". It also tells you why it suggests an interpreter, such as "project environment".
- [[#15929](https://github.com/posit-dev/positron/issues/15929)] Interpreter: the interpreter picker shows all R versions in one group, with your current R first. When you have more than one R version, Positron uses your current R by default.
- [[#15999](https://github.com/posit-dev/positron/issues/15999)] Interpreter: the new [`interpreters.languageOrder`](positron://settings/interpreters.languageOrder) setting sets the order of languages in interpreter pickers and on the Welcome page.
- [[#16585](https://github.com/posit-dev/positron/issues/16585)] Interpreter: interpreter definitions can list environment modules to load with the new `modules` field.
- [[#14744](https://github.com/posit-dev/positron/issues/14744)] Interpreter: R and Python sessions run `module purge` before they load environment modules. To keep the modules from shell startup scripts, set `"purge": false` on an environment.
- [[#15587](https://github.com/posit-dev/positron/issues/15587)] Interpreter: [`positron.r.interpreters.default`](positron://settings/positron.r.interpreters.default) can name an environment module or module environment. R starts with that module loaded.
- [[#16252](https://github.com/posit-dev/positron/issues/16252)] New Folder: _New Folder from Template_ and _New Folder from Git_ use the [`files.dialog.defaultPath`](positron://settings/files.dialog.defaultPath) setting for the first location, if you set it. _New Folder from Git_ uses [`git.defaultCloneDirectory`](positron://settings/git.defaultCloneDirectory) first. An enforced `files.dialog.defaultPath` can start with `~` to use the home folder of each user.
- [[#16789](https://github.com/posit-dev/positron/pull/16789)] Dev Containers: the Ports view is available when you connect to a dev container.
- [[#16847](https://github.com/posit-dev/positron/issues/16847)] Notebooks: the [`notebook.showCellStatusBar`](positron://settings/notebook.showCellStatusBar) setting hides the cell execution status and time in Positron notebooks and in Quarto inline output.
- [[#16727](https://github.com/posit-dev/positron/issues/16727)] MCP: coding agents start the Positron MCP server through a launcher at a stable path, so agent configurations keep working after Positron upgrades. This includes agents that Positron does not configure.
- [[#16727](https://github.com/posit-dev/positron/issues/16727)] MCP: added OpenCode, Copilot CLI, and Kiro CLI to _Positron MCP: Add to Coding Agent_.
- [[#15072](https://github.com/posit-dev/positron/issues/15072)] SQL: SQL files offer table and column completions from the connected database, and flag names that are not in its schema. To try SQL language features, enable the [`sql.enabled`](positron://settings/sql.enabled) setting.
- [[#15071](https://github.com/posit-dev/positron/issues/15071)] SQL: SQL completions and parsing follow the dialect of the driver for the connection.
- [[#13598](https://github.com/posit-dev/positron/issues/13598)] Settings: Positron reads the `POSITRON_EXTENSIONS`, `POSITRON_PORTABLE`, and `POSITRON_APPDATA` environment variables. With these, you can set the extensions folder and data folders of Positron with no effect on VS Code. The deprecated `VSCODE_*` names still work, but Positron 2027.01 will ignore them.
- [[#3028](https://github.com/posit-dev/positron/issues/3028)] Object Explorer: the new Object Explorer lets you browse, search, and copy accessors for nested data such as R lists, model fits, Python dicts, and JSON files. Open it with `View()` in R, from the Variables pane, or with **Open in Object Explorer** on a JSON file. You can also import a JSON file as R or Python code from the Object Explorer.
- [[#422](https://github.com/posit-dev/positron/issues/422)] Help: the Help pane has a search box. It suggests help topics as you type, and it can search all of the help for the active R or Python interpreter.
- [[#16484](https://github.com/posit-dev/positron/issues/16484)] Folders: you can pin recent folders to the top of the folder menu.
- [[#16131](https://github.com/posit-dev/positron/issues/16131)] Terminal: the new [`terminal.integrated.allowProgramsToCopyToClipboard`](positron://settings/terminal.integrated.allowProgramsToCopyToClipboard) setting lets programs in the terminal, such as tmux, Vim, or Claude Code, copy text to the system clipboard in the browser.
- [[#10753](https://github.com/posit-dev/positron/issues/10753)] Extensions: extensions that use `positron.window.createPreviewPanel` can show a stop button in the Viewer with `PreviewPanel.stoppable` and `onDidRequestStop`.
- [[#16475](https://github.com/posit-dev/positron/pull/16475)] Updates: automatic updates wait when you are on a metered connection.

#### Bug fixes

- [[#16743](https://github.com/posit-dev/positron/issues/16743)] Assistant: the Viewer `press` command of Posit Assistant submits a form on Enter, steps number boxes, and toggles checkboxes. It no longer reports success for keys that the browser does not act on.
- [[#15914](https://github.com/posit-dev/positron/issues/15914)] Assistant: Posit Assistant can open files on Workbench and over Remote SSH.
- [[#15778](https://github.com/posit-dev/positron/issues/15778)] Assistant: Posit Assistant sees a new interpreter as soon as it asks Positron to discover interpreters again.
- [[#16553](https://github.com/posit-dev/positron/issues/16553)] Assistant: fixed keybinding conflicts in Posit Assistant views.
- [[#16611](https://github.com/posit-dev/positron/issues/16611)] Assistant: Git commit messages and notebook AI use a configured Posit AI Pass gateway, and the configured protocol and endpoints of a custom provider. They work with LiteLLM and OpenAI-compatible providers that have no API key.
- [[#16611](https://github.com/posit-dev/positron/issues/16611)] Assistant: Git commit messages and notebook AI show the error of the provider when a request fails, instead of an empty or cut-off result. Providers with model discovery off no longer get a `/models` request, and the AI provider list loads after a failed first attempt.
- [[#16825](https://github.com/posit-dev/positron/pull/16825)] Assistant: completions in `settings.json` and language model queries no longer stop responding when Copilot Chat has no GitHub session.
- [[#16069](https://github.com/posit-dev/positron/issues/16069)] Assistant: GitHub Copilot sign-in from the status bar no longer fails with "Failed to sign in to GitHub".
- [[#16569](https://github.com/posit-dev/positron/issues/16569)] Python: `?polars` shows the polars documentation in the Help pane instead of an error.
- [[#16192](https://github.com/posit-dev/positron/issues/16192)] Python: when you create a venv with uv and uv is missing, Positron offers to install uv.
- [[#4556](https://github.com/posit-dev/positron/issues/4556)] Python: when you recreate a workspace `.venv` with a different Python version, the console and session picker show the new version. When you delete a workspace `.venv`, Positron shuts down its session and removes it from the session picker.
- [[#12281](https://github.com/posit-dev/positron/issues/12281)] Python: the Python extension no longer writes files into the Positron install folder, so the macOS code signature stays valid after launch.
- [[#16464](https://github.com/posit-dev/positron/issues/16464)] Python: the prompt to create a virtual environment for a project with `requirements.txt` or `pyproject.toml` no longer depends on timing at startup.
- [[#16584](https://github.com/posit-dev/positron/issues/16584)] Python: Positron no longer offers to start a second Python console after it creates a Python environment, including from the New Folder flow.
- [[#16928](https://github.com/posit-dev/positron/issues/16928)] Python: the unsupported Python version notification no longer shows in projects that have no Python console session. When you have not chosen a Python interpreter for a folder, Python language features use the suggested interpreter.
- [[#15825](https://github.com/posit-dev/positron/issues/15825)] Python: `python.interpreters.exclude` and `python.interpreters.override` also apply to the saved interpreter of the workspace and to `interpreters.definitions`.
- [[#10698](https://github.com/posit-dev/positron/issues/10698)] Python: Positron no longer supports Python 3.9.
- [[#16936](https://github.com/posit-dev/positron/pull/16936)] Python: removed a test-only Python lockfile from the packaged Python extension. This file caused false-positive findings in vulnerability scans.
- [[#16405](https://github.com/posit-dev/positron/issues/16405)] R: `rstudioapi::getSourceEditorContext()` and `rstudioapi::documentPath()` no longer return the console when the console has focus.
- [[#15992](https://github.com/posit-dev/positron/issues/15992)] R: new windows start the default R after you change the default, and also after interpreter discovery runs.
- [[#16608](https://github.com/posit-dev/positron/issues/16608)] R: in R notebook cells and Quarto chunks, diagnostics no longer warn about functions from a package that an earlier cell attaches with `library()`.
- [[#16633](https://github.com/posit-dev/positron/issues/16633)] R: `file.choose()` opens a file dialog. Before, it asked for a file name in the console.
- [[#16523](https://github.com/posit-dev/positron/issues/16523)] R: Go to Definition works for packages in renv projects, whose libraries use symlinks.
- [[#16376](https://github.com/posit-dev/positron/issues/16376)] R: R no longer starts automatically in a folder with no R files.
- [[#16551](https://github.com/posit-dev/positron/issues/16551)] R: Positron finds Pixi R installations when you open a Pixi project, without _Discover All Interpreters_ (thanks to @roaldarbol).
- [[#12098](https://github.com/posit-dev/positron/issues/12098)] R: completions show one item for an object that the document defines and that is also in the global environment. The item has the same icon and position each time.
- [[#12303](https://github.com/posit-dev/positron/issues/12303)] R: on Windows, R sessions start when the path to R contains non-ASCII characters.
- [[#16657](https://github.com/posit-dev/positron/issues/16657)] Connections: a slow or stuck metadata query no longer keeps a level of the Data Connections tree in the loading state. After 5 seconds the level shows, and a row that was still waiting uses the query that is already running.
- [[#16104](https://github.com/posit-dev/positron/issues/16104)] Connections: when you edit an ODBC configuration file while Positron is open, the affected ODBC connections close cleanly. Before, the pane showed them as connected when they were not.
- [[#15700](https://github.com/posit-dev/positron/issues/15700)] Connections: Databricks, ODBC, PostgreSQL, Redshift, and Snowflake connections release a table view when you close its Data Explorer tab. Before, they kept it until the connection closed.
- [[#16409](https://github.com/posit-dev/positron/issues/16409)] Connections: Databricks connections on Workbench can sign in with OAuth User-to-Machine. Positron opens your browser, and when the redirect cannot reach Positron, you can paste the redirect address back.
- [[#13632](https://github.com/posit-dev/positron/issues/13632)] Connections: the Authentication output channel no longer shows repeated "No SNOWFLAKE_HOME configured" warnings on Desktop.
- [[#15361](https://github.com/posit-dev/positron/issues/15361)] Data Explorer: fixed rows that repeated or went missing when you scrolled or copied from PostgreSQL, Redshift, Snowflake, Databricks, and ODBC connections. Copied cells now match the rows that show.
- [[#16639](https://github.com/posit-dev/positron/issues/16639)] Data Explorer: when you close and open a table from the Data Connections pane again, Positron opens a new Data Explorer. Before, it showed the closed one, with its old sort order and scroll position.
- [[#16721](https://github.com/posit-dev/positron/pull/16721)] Data Explorer: when the data source rejects a filter change, the filter bar shows the filters in effect and an error that tells you why. Before, it showed filters that were not applied.
- [[#16527](https://github.com/posit-dev/positron/issues/16527)] Data Explorer: the summary panel shows exact integer Min and Max values for polars and CSV columns.
- [[#15885](https://github.com/posit-dev/positron/issues/15885)] Data Explorer: DuckDB `DECIMAL` columns display, copy, and export their exact values. Before, Positron rounded them through a double.
- [[#15887](https://github.com/posit-dev/positron/issues/15887)] Data Explorer: Snowflake `NUMBER` columns display, copy, and export their exact values. Summaries no longer fail on wide `NUMBER` columns, and `FLOAT` infinity shows as `INF` instead of `NaN`.
- [[#16942](https://github.com/posit-dev/positron/issues/16942)] Data Explorer: the Data Explorer, Object Explorer, Plots editor, Plots gallery, and Preview editor open when [`workbench.editorAssociations`](positron://settings/workbench.editorAssociations) contains a catch-all pattern such as `"*": "default"`.
- [[#16443](https://github.com/posit-dev/positron/issues/16443)] Interpreter: interpreter discovery no longer runs on every launch after you do not open Positron for longer than [`interpreters.discoveryCache.maxAgeDays`](positron://settings/interpreters.discoveryCache.maxAgeDays). The interpreter cache no longer drops interpreters that discovery finds.
- [[#13487](https://github.com/posit-dev/positron/issues/13487)] Interpreter: R and Python interpreter settings no longer show in the folder settings of a multi-root workspace. Positron always ignored them there.
- [[#15587](https://github.com/posit-dev/positron/issues/15587)] Interpreter: an R that an environment module provides shows in the interpreter picker, even when Positron also finds the same R without the module.
- [[#16575](https://github.com/posit-dev/positron/issues/16575)] Workbench: help pages after the first one no longer fail to load on Workbench.
- [[#16276](https://github.com/posit-dev/positron/issues/16276)] Workbench: the extension host no longer stops when the connection drops on Workbench with session SSL.
- [[#17023](https://github.com/posit-dev/positron/pull/17023)] Workbench: Positron stops trying to reconnect after Workbench reports that the session exited, and tries less often while you are logged out.
- [[#16412](https://github.com/posit-dev/positron/issues/16412)] Workbench: reconnection no longer fails behind proxies that remove the WebSocket query string, such as SageMaker Studio.
- [[#10893](https://github.com/posit-dev/positron/issues/10893)] Workbench: `browseURL()` on a local file opens the file in a new browser tab.
- [[#16199](https://github.com/posit-dev/positron/issues/16199)] Workbench: the extension marketplace stays disabled in Workbench sessions for users who cannot write to the global extensions folder.
- [[#17029](https://github.com/posit-dev/positron/pull/17029)] Workbench: the shell startup files of a user no longer override the settings that an administrator enforces in the extension host.
- [[#9494](https://github.com/posit-dev/positron/issues/9494)] New Folder: the SSH key passphrase prompt shows when you clone a repository with _New Folder from Git_ after you select a folder with **Browse**.
- [[#16290](https://github.com/posit-dev/positron/issues/16290)] New Folder: the first **Browse** click in the New Folder flow opens the folder picker.
- [[#16252](https://github.com/posit-dev/positron/issues/16252)] New Folder: _New Folder from Template_ and _New Folder from Git_ show an error and stop when you cannot create a folder in the location.
- [[#8621](https://github.com/posit-dev/positron/issues/8621)] New Folder: when the default folder name already exists, the New Folder flow suggests a unique name, such as `my-python-project-2`, instead of an error.
- [[#12749](https://github.com/posit-dev/positron/issues/12749)] Dev Containers: Positron substitutes variables in `devcontainer.json`, such as `${localEnv:HOME}` (thanks to @fleverest).
- [[#14943](https://github.com/posit-dev/positron/issues/14943)] Dev Containers: fixed a build failure on Ubuntu (thanks to @fleverest).
- [[#12172](https://github.com/posit-dev/positron/issues/12172)] Dev Containers: the server download works in containers that have `curl` but not `wget` (thanks to @fleverest).
- [[#16789](https://github.com/posit-dev/positron/pull/16789)] Dev Containers: fixed connections in containers without IPv6, and server startup when environment values contain quotes or `$`. `${containerEnv:...}` works in `remoteEnv` and lifecycle commands.
- [[#16151](https://github.com/posit-dev/positron/issues/16151)] Notebooks: language features such as completions and diagnostics continue to work after you save an untitled notebook or rename a notebook. An untitled Quarto document keeps its kernel and variables when you save it to a file.
- [[#16311](https://github.com/posit-dev/positron/issues/16311)] Notebooks: the missing packages badge no longer shows two times in the Positron notebook toolbar when a script with a missing package is also open.
- [[#16933](https://github.com/posit-dev/positron/issues/16933)] Notebooks: notebooks no longer sometimes reconnect to the wrong kernel after the extension host reconnects.
- [[#16630](https://github.com/posit-dev/positron/issues/16630)] MCP: Viewer screenshots that you take through the MCP server come back as images. Before, they failed the size limit.
- [[#8738](https://github.com/posit-dev/positron/issues/8738)] Console: the mouse wheel scrolls the Console when the pointer is over a multi-line input.
- [[#11627](https://github.com/posit-dev/positron/issues/11627)] Console: console output no longer repeats text when the same URL shows more than once in a line.
- [[#16121](https://github.com/posit-dev/positron/issues/16121)] Console: the function signature dialog in the Console closes when you submit code. Before, it stayed open until the R code finished.
- [[#13598](https://github.com/posit-dev/positron/issues/13598)] Settings: a portable Positron no longer gives its portable folder to a VS Code that you start from the Positron terminal.
- [[#14265](https://github.com/posit-dev/positron/issues/14265)] Installer: Positron is about 224 MB smaller on each platform, because its extensions now share one copy of the DuckDB library.
- [[#16567](https://github.com/posit-dev/positron/pull/16567)] Installer: the bundled Python kernel has about 1,900 fewer files.
- [[#16015](https://github.com/posit-dev/positron/issues/16015)] Quarto: Quarto no longer logs a false "did not respond" warning for R and Python cells when [`quarto.embeddedLanguageFeatures.native`](positron://settings/quarto.embeddedLanguageFeatures.native) is off.
- [[#17019](https://github.com/posit-dev/positron/issues/17019)] Quarto: <kbd>Cmd/Ctrl+Click</kbd>, **View Variable at Cursor**, and **Open in Data Explorer** work in Quarto and R Markdown documents with inline output.
- [[#12414](https://github.com/posit-dev/positron/issues/12414)] Variables: the Variables pane no longer shows extra spaces in NumPy array values, such as `[ 3,10]`.
- [[#11301](https://github.com/posit-dev/positron/issues/11301)] Variables: Ibis joins and other `Table` subclasses show as data in the Variables pane and open in the Data Explorer.
- [[#15909](https://github.com/posit-dev/positron/issues/15909)] Data Apps: Positron shows a warning when it cannot find the URL of an app that runs in the terminal. If the URL shows later, Positron previews the app.
- [[#16468](https://github.com/posit-dev/positron/issues/16468)] Data Apps: the **Show Console** action on **Run App** notifications opens the Console view if it is hidden.
- [[#16869](https://github.com/posit-dev/positron/pull/16869)] Server: Positron Server and Workbench installs are smaller.
- [[#16136](https://github.com/posit-dev/positron/issues/16136)] Welcome page: the **Environment Setup** card updates after you trust a workspace. Before, it said that the Python extension was not available.
- [[#16155](https://github.com/posit-dev/positron/issues/16155)] Sessions: when an R or Python language server stops, for example after a Quarto session shuts down, Positron no longer asks it for statement ranges, input boundaries, or help. The console session answers instead.
- [[#15714](https://github.com/posit-dev/positron/issues/15714)] Packages: when you filter the Packages pane after you scroll down, the pane shows the matching packages. Before, it was empty.
- [[#11713](https://github.com/posit-dev/positron/issues/11713)] WSL: Positron blocks the third-party Open Remote WSL extension, because it conflicts with the built-in WSL support and breaks first-time WSL connections.
- [[#16619](https://github.com/posit-dev/positron/pull/16619)] Windows: per-filename entries in `nextEditSuggestions.enabled` apply on Windows. When you open a DuckDB database that another session has locked, Positron explains the conflict on Windows too.
- [[#16607](https://github.com/posit-dev/positron/pull/16607)] Snippets: _Snippets: Configure Snippets_ again adds the R and Python example content when it creates a language snippets file.
- [[#8494](https://github.com/posit-dev/positron/issues/8494)] Themes: in Positron Dark, the cursor is easy to see next to a matched bracket.
- [[#16534](https://github.com/posit-dev/positron/issues/16534)] UI: Data Connections and Packages show in a more logical place in the activity bar.
- [[#16556](https://github.com/posit-dev/positron/pull/16556)] Accessibility: keyboard focus no longer goes missing after you delete or restart a console session. Screen readers no longer announce the name of each plot thumbnail two times.

#### Dependencies

- Updated `code-oss` upstream to v1.138.0.
- Updated bundled Quarto to 1.11.9.
