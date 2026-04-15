### Patch notes

The [2026.04.0 patch release](https://github.com/posit-dev/positron/releases/tag/2026.04.1-10) (2026-04-15) provides fixes for Positron Assistant and code completions in Quarto files.

### Release highlights

#### Positron Server for academic use via JupyterHub 🎓

Academic institutions can now offer Positron Server to their students at no cost through JupyterHub. If your institution already runs JupyterHub, you can add Positron as a launcher option alongside JupyterLab, with no additional infrastructure required. Students simply log in and select Positron from the launcher, getting the full Positron experience including rich Python and R support, the extension marketplace, and (optionally) Positron Assistant. To get started, review the [eligibility criteria](https://positron.posit.co/faqs.html#how-can-i-use-positron-in-an-educational-setting) and send an email to [academic-licenses@posit.co](mailto:academic-licenses@posit.co) to request a free teaching license.

#### Positron Notebook Editor improvements 📓

This release brings new quality-of-life improvements to the Positron Notebook Editor, currently available for alpha testing. You can now reorder cells by dragging them and a new output action bar makes it easy to expand, collapse, or clear outputs without hunting through menus. The find widget now supports replace, inline Data Explorers provide more functionality, and long text outputs can be individually truncated. We also fixed several bugs affecting side-by-side notebooks, real-time streaming output, and scrollbar rendering. If you are using Positron Assistant for AI chat, the Assistant can now analyze your current cell output and suggest a logical next step in a "ghost cell" at the bottom of your notebook.

#### New R commands and debugging features ✨

This release continues to deepen Positron R support across several areas. Shiny applications now run in Console sessions instead of the terminal, making it possible to use the Positron R debugger with your Shiny apps for the first time. The debugger also gains support for conditional breakpoints, log breakpoints, and hit count breakpoints. Two new commands make it easier to work with resources from R packages: _R: Run RStudio Addin_ lets you browse and execute installed addins from the Command Palette, and _R: New R Markdown from Template_ lets you discover and use `.Rmd` templates from your installed packages.

<div id="checkbox"></div>

### Changelog

#### New features


- [[#9638](https://github.com/posit-dev/positron/issues/9638)] Notebooks: added Outline pane support, showing markdown headers and code cell previews with click-to-navigate.
- [[#12043](https://github.com/posit-dev/positron/issues/12043)] Notebooks: inline Data Explorers now display the variable name and can be clicked to open a full Data Explorer.
- [[#10489](https://github.com/posit-dev/positron/issues/10489)] Notebooks: added "Clear Output" option to the notebook cell output context menu for clearing individual cell outputs. 
- [[#10756](https://github.com/posit-dev/positron/issues/10756)] Notebooks: find widget now supports replace.
- [[#10806](https://github.com/posit-dev/positron/issues/10806)] Notebooks: added "Copy Image" action for plot outputs, available via the output ellipsis menu and right-click context menu.
- [[#9840](https://github.com/posit-dev/positron/issues/9840)] Notebooks: added drag-and-drop to reorder cells, with multi-cell drag support.
- [[#12370](https://github.com/posit-dev/positron/issues/12370)] Notebooks: added a cell output action bar to easily expand, collapse, and clear outputs.
- [[#12518](https://github.com/posit-dev/positron/issues/12518)] Notebooks: long text cell outputs can now be individually truncated.
- [[#12507](https://github.com/posit-dev/positron/issues/12507)] Assistant: Our new Posit Assistant AI chat experience is now available for initial testing. This brings the [same AI chat interface available in RStudio](https://posit.co/blog/introducing-ai-in-rstudio/) to Positron, and will eventually replace Positron Assistant.
- [[#8007](https://github.com/posit-dev/positron/issues/8007)] Assistant: now support custom base URLs for Anthropic as a model provider.
- [[#12377](https://github.com/posit-dev/positron/issues/12377)] Assistant: Azure Foundry provider now accepts deployment-based Azure OpenAI URLs and automatically converts them to the supported v1 format.
- [[#12214](https://github.com/posit-dev/positron/issues/12214)] Assistant: show warning in chat when output token limit reached.
- [[#12341](https://github.com/posit-dev/positron/issues/12341)] Assistant: users can now open the Manage Accounts menu from Assistant's Copilot configuration dialog.
- [[#12132](https://github.com/posit-dev/positron/issues/12132)] Assistant: added toggleable option for `.vscode/positron/agents` directory in the `chat.agentFilesLocations` setting.
- [[#5640](https://github.com/posit-dev/positron/issues/5640)] Quarto: added experimental support for inline output for `.qmd` documents.
- [[#12150](https://github.com/posit-dev/positron/issues/12150)] Quarto: inline output for R now respects `fig-width` and `fig-height` options.
- [[#12148](https://github.com/posit-dev/positron/issues/12148)] Quarto: added inline data explorer for notebooks and Quarto documents.
- [[#7451](https://github.com/posit-dev/positron/issues/7451)] Python: now send plotting pre-renders in Python for snappier plotting experience.
- [[#1313](https://github.com/posit-dev/positron/issues/1313)] R: use the new command _R: Run RStudio Addin_ to browse and execute RStudio Addins via the Command Palette.
- [[#8762](https://github.com/posit-dev/positron/issues/8762)] R: use the new command _R: New R Markdown from Template_ to discover all `.Rmd` templates in your installed R packages and create a new file using your chosen option.
- [[#12120](https://github.com/posit-dev/positron/issues/12120)] R: Moved "RStudio Keybindings" setting to User settings; it was formerly under Remote settings for Remote SSH and Posit Workbench.
- [[#12556](https://github.com/posit-dev/positron/issues/12556)] R: Positron now runs Shiny applications in console sessions instead of the terminal. This makes it possible to debug them with the Positron R debugger.
- [[#12360](https://github.com/posit-dev/positron/issues/12360)] R: debugger now provides support for the special types of breakpoints: conditional breakpoints, log breakpoints, and hit count breakpoints.
- [[#9763](https://github.com/posit-dev/positron/issues/9763)] R: `positron.session_init` and `positron.session_reconnect` are new hooks that are executed in the R session, once R startup is complete and Positron is fully operational and able to handle requests that pertain to the UI, such as rstudioapi calls. This duo is intended to be analogous to RStudio's `rstudio.sessionInit`. A `positron.session_init` hook function should accept a `start_type` parameter, with possible values `"new"` or `"restart"`. A `positron.session_reconnect` hook takes no input.
- [[#12300](https://github.com/posit-dev/positron/issues/12300)] Workbench: added support for version-specific Workbench-hosted Positron documentation.
- [[#11426](https://github.com/posit-dev/positron/issues/11426)] Workbench: added support for reading the Posit Workbench `r-versions` configuration file to discover R installations with extended metadata. This enables administrators to configure R installations with custom labels, startup scripts, repository settings, library paths, and environment module integration for users on Linux servers.
- [[#7112](https://github.com/posit-dev/positron/issues/7112)] API: added new extension API method for evaluating code silently.
- [[#11321](https://github.com/posit-dev/positron/issues/11321)] Extensions: added a new `engines.positron` compatibility check for extension updates.
- [[#11460](https://github.com/posit-dev/positron/issues/11460)] Plots: show a link to the script that created the plot in the Plots pane.
- [[#12338](https://github.com/posit-dev/positron/issues/12338)] Console: improved console startup performance in existing workspaces.
- [[#12233](https://github.com/posit-dev/positron/issues/12233)] History: added support for selecting multiple entries at once in the History pane.
- [[#12524](https://github.com/posit-dev/positron/issues/12524)] Added anonymous usage reporting during update checks to help us understand unique usage patterns. This uses a random, resettable ID that is not linked to any other identifiers. Users can opt out via the `update.anonymousUsageReporting` setting or reset their ID via the command palette.
- [[#11898](https://github.com/posit-dev/positron/issues/11898)] Renamed some language runtime commands. For example, _Start New Interpreter Session_ is now _Start New Console Session_.
- [[#9074](https://github.com/posit-dev/positron/issues/9074)] Show overall memory usage and Positron footprint in the Variables pane.
- [[#12158](https://github.com/posit-dev/positron/issues/12158)] Added hover-based show/hide for submenus.
- [[#12207](https://github.com/posit-dev/positron/issues/12207)] Windows ARM builds now include Quarto (running under x64 emulation).
- [[#11854](https://github.com/posit-dev/positron/issues/11854)] Added link to [sign up for Positron email updates](https://posit.co/positron-updates-signup/) to the Help menu, Help pane, and Getting Started page. 

#### Bug fixes

- [[#11413](https://github.com/posit-dev/positron/issues/11413)] Notebooks: fixed ghost cell suggestions and cleanup.
- [[#11859](https://github.com/posit-dev/positron/issues/11859)] Notebooks: no longer goes blank when a single output or cell fails to render; errors are now caught and shown inline with retry/reload options.
- [[#12455](https://github.com/posit-dev/positron/issues/12455)] Notebooks: fixed action bar buttons (Run All, kernel status, etc.) targeting the wrong notebook when two notebooks are open side-by-side.
- [[#12454](https://github.com/posit-dev/positron/issues/12454)] Notebooks: fixed kernel status badge showing the wrong kernel when notebooks are open side-by-side.
- [[#12342](https://github.com/posit-dev/positron/issues/12342)] Notebooks: fixed selection state getting stuck in edit mode during multi-select.
- [[#12366](https://github.com/posit-dev/positron/issues/12366)] Notebooks: fixed scrollable cell outputs appearing in a nested bordered container instead of scrolling within the existing output area.
- [[#11720](https://github.com/posit-dev/positron/issues/11720)] Notebooks: text outputs now respect the `notebook.output.wordWrap` setting.
- [[#12421](https://github.com/posit-dev/positron/issues/12421), [#12426](https://github.com/posit-dev/positron/issues/12426)] Notebooks: fixed scrollbar UI bugs.
- [[#11726](https://github.com/posit-dev/positron/issues/11726), [#12502](https://github.com/posit-dev/positron/issues/12502), [#11630](https://github.com/posit-dev/positron/issues/11630)] Notebooks: fixed cell output not updating in real-time during streaming execution.
- [[#10481](https://github.com/posit-dev/positron/issues/10481)] Notebooks: hide irrelevant legacy notebook commands from the command palette when using the new Positron notebook editor.
- [[#12682](https://github.com/posit-dev/positron/issues/12682)] Notebooks: fixed side-by-side notebooks stealing focus when exiting edit mode in one notebook while clicking into another.
- [[#12162](https://github.com/posit-dev/positron/issues/12162)] Assistant: fixed Positron Assistant producing `.ipynb`-like JSON diffs instead of plain text edits when editing `.qmd` files.
- [[#11919](https://github.com/posit-dev/positron/issues/11919)] Assistant: fixed how prompting is used to fence Quarto code.
- [[#12214](https://github.com/posit-dev/positron/issues/12214)] Assistant: fixed issue where custom max output tokens were not being applied to requests.
- [[#11524](https://github.com/posit-dev/positron/issues/11524), [#11433](https://github.com/posit-dev/positron/issues/11433)] Assistant: fixed model selection for git commit message generation.
- [[#11488](https://github.com/posit-dev/positron/issues/11488)] Assistant: fixed Positron Assistant failing to create, read, or patch files when given relative paths in Edit/Agent mode.
- [[#11828](https://github.com/posit-dev/positron/issues/11828)] Console: fixed display of workbench trust status.
- [[#12255](https://github.com/posit-dev/positron/issues/12255)] Console: fixed an issue switching between consoles after selecting one via the Plots pane.
- [[#10929](https://github.com/posit-dev/positron/issues/10929)] Console: reduced flickering/switching at startup between languages in the Console for projects that use R and Python.
- [[#9759](https://github.com/posit-dev/positron/issues/9759), [#11157](https://github.com/posit-dev/positron/issues/11157), [#12302](https://github.com/posit-dev/positron/issues/12302), [#12393](https://github.com/posit-dev/positron/issues/12393)] Console: addressed issues with multi-line statement execution and completions in Quarto notebooks and notebook consoles.
- [[#12251](https://github.com/posit-dev/positron/issues/12251)] Console: fixed performance regression that caused slow evaluations from editor when a console is busy.
- [[#12277](https://github.com/posit-dev/positron/issues/12277)] Console: fixed execution indicator litter in the Console.
- [[#12161](https://github.com/posit-dev/positron/issues/12161)] Python: fixed Pyrefly static analysis features (semantic highlighting, hover, completions) not working when first opening a `.ipynb` file.
- [[#11787](https://github.com/posit-dev/positron/issues/11787), [#10758](https://github.com/posit-dev/positron/issues/10758)] Python: fixed how we install and display pre-release Python via uv.
- [[#7915](https://github.com/posit-dev/positron/issues/7915)] Python: enabled users to run `plt.close()` in a cell and still see plot.
- [[#12694](https://github.com/posit-dev/positron/issues/12694)] Python: fixed rare `'NoneType' object has no attribute 'is_alive'` bug in the Console.
- [[#11918](https://github.com/posit-dev/positron/issues/11918)] Python: fixed handling of geopandas in Variables pane.
- [[#12140](https://github.com/posit-dev/positron/issues/12140)] R: Variables pane now updates immediately when selecting a different stack frame in the debugger call stack.
- [[#11887](https://github.com/posit-dev/positron/issues/11887)] R: debugger virtual documents (`ark://` URIs) no longer show distracting diagnostic squiggles on code the user cannot edit.
- [[#12230](https://github.com/posit-dev/positron/issues/12230)] R: noisy messages emitted during debugging are now filtered out from the Console.
- [[#1065](https://github.com/posit-dev/ark/issues/1065)] R: fixed a rare bug that caused Console output to be temporarily swallowed.
- [[#12688](https://github.com/posit-dev/positron/issues/12688)] R: fixed an issue where output preceding a `menu()` or `readline()` question was swallowed.
- [[#12642](https://github.com/posit-dev/positron/issues/12642)] R: fixed the Console environment being incorrectly reset to the global environment when an error was thrown while debugging.
- [[#12405](https://github.com/posit-dev/positron/issues/12405)] Remote SSH: fixed architecture mismatch warning incorrectly appearing in remote SSH sessions.
- [[#11382](https://github.com/posit-dev/positron/issues/11382)] Remote SSH: fixed remote host connections failing after 60 days for monthly release users.
- [[#11654](https://github.com/posit-dev/positron/issues/11654)] Plots: fixed issue persisting selection in the Open in Editor menu in the Plots pane.
- [[#6292](https://github.com/posit-dev/positron/issues/6292)] Plots: now cascade buttons into an overflow menu at narrower widths.
- [[#7539](https://github.com/posit-dev/positron/issues/7539)] Variables: fixed Variables pane navigating away from the correct notebook session when opening the Data Explorer.
- [[#2795](https://github.com/posit-dev/positron/issues/2795), [#4279](https://github.com/posit-dev/positron/issues/4279)] Data Explorer: background computation no longer runs in some cases when the tab is inactive.
- [[#12541](https://github.com/posit-dev/positron/issues/12541)] Connections Pane: R PostgreSQL and SQLite connections can now be resumed after restarting Positron.
- [[#12156](https://github.com/posit-dev/positron/issues/12156)] Fixed error starting kernels when using exotic shells.
- [[#11585](https://github.com/posit-dev/positron/issues/11585)] Fixed issue where cloning the same repository to a different directory via "New Folder from Git" would open the first clone instead of creating a new one.
- [[#12113](https://github.com/posit-dev/positron/issues/12113)] Fixed warning messages overflowing the content area in the New Folder from Template dialog.
- [[#12220](https://github.com/posit-dev/positron/issues/12220)] Fixed keyboard shortcuts (<kbd>Ctrl/Cmd+Shift+P</kbd>, <kbd>Cmd+B</kbd>, etc) not working when PDF viewer has focus.
- [[#11203](https://github.com/posit-dev/positron/issues/11203)] Make display of per-session memory usage on macOS line up better with Activity Monitor.

#### Dependencies

- Updated `code-oss` upstream to v1.109.0.
- Updated `vscode-python` upstream to v2026.4.0.
- Updated bundled Quarto to 1.9.36.
- Updated bundled version of Air to [0.24.0](https://github.com/posit-dev/air/blob/main/editors/code/CHANGELOG.md#0240).
