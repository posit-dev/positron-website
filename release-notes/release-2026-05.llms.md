# 2026.05.0-179 Release Notes

<https://github.com/posit-dev/positron/releases/tag/2026.05.0-179>

Published

May 4, 2026

### Patch notes

The [2026.05.1 patch release](https://github.com/posit-dev/positron/releases/tag/2026.05.1-2) (2026-05-06) provides corrected builds for x64/Intel macOS.

The [2026.05.2 patch release](https://github.com/posit-dev/positron/releases/tag/2026.05.2-3) (2026-05-14) fixes the behavior when switching tabs in the Positron notebook editor.

### Release highlights

Welcome to the 2026.05.0 release of Positron!

- [Announcing the Packages pane](#announcing-the-packages-pane)
- [Inline output for Quarto](#inline-output-for-quarto)
- [Extensions available from Posit Public Package Manager](#extensions-available-from-posit-public-package-manager)
- [Positron Notebook Editor is now in beta](#positron-notebook-editor-is-now-in-beta)
- [Posit Assistant and Posit AI](#posit-assistant-and-posit-ai)

#### Announcing the Packages pane

Our Packages pane is available in this release as a preview feature. The new Packages pane brings streamlined package management directly into the IDE so you can see at a glance what’s installed, what’s attached, and what’s out of date.

![The Packages pane showing installed Python packages](https://cdn.posit.co/positron/releases/release-notes/assets/2026-05-packages-pane.png)

Find it in the Primary Sidebar by clicking the package icon. Positron automatically detects and integrates with your current interpreter; today we have support for pip, venv, uv, and conda for Python, plus base R, pak, and renv for R. You can search, sort, install, update, remove, filter by category (including “Outdated Packages”), and even see which packages are attached in your current session. To hide the pane, disable [`positron.packages.enable`](positron://settings/positron.packages.enable). [Let us know](https://github.com/posit-dev/positron/discussions) how it fits into your workflow.

#### Inline output for Quarto

Inline output for `.qmd` documents was one of Positron’s most-requested features ever, with many users telling us it was the one thing keeping them tied to RStudio or Jupyter notebooks. We are happy to share that Quarto inline output is available this release as a preview feature. Quarto kernels start automatically when you open a document with inline output, so you don’t wait for a kernel on first execution. Each inline output cell shows a status line with execution status and elapsed time, and outputs are now collapsible when they get long. We’ve also added a tool to switch the interpreter used for inline output, support for *Show Notebook Console* for Quarto documents, and fixed a handful of papercuts around execution indicators, autocompletion, and the kernel selector. Enable inline output via the [`positron.quarto.inlineOutput.enabled`](positron://settings/positron.quarto.inlineOutput.enabled) setting.

#### Extensions available from Posit Public Package Manager

Positron’s extension gallery now uses [Posit Public Package Manager](https://p3m.dev) (P3M) by default, replacing Open VSX as the source for browsing and installing extensions. The catalog is the same set of extensions you already use, served from Posit infrastructure for reliable distribution. If you prefer to stay on Open VSX, the new [`positron.extensions.gallerySource`](positron://settings/positron.extensions.gallerySource) setting lets you switch back at any time. For organizations on Posit Workbench, [Posit Package Manager also added support for mirroring and serving VS Code extensions](https://posit.co/blog/manage-vs-code-extensions-like-packages-with-posit-package-manager-2026-04-0/) from your own instance, bringing the same governance, security, and air-gapped distribution to extensions that you already have for R and Python packages.

#### Positron Notebook Editor is now in beta

The Positron Notebook Editor for `.ipynb` files is officially moving from alpha to beta. This release brings a wave of polish and reliability we hope makes it ready for your daily workflow:

- **Cleaner git diffs by default:** New [`notebook.save.outputs`](positron://settings/notebook.save.outputs) and [`notebook.save.executionCounts`](positron://settings/notebook.save.executionCounts) settings let you exclude outputs and execution counts from saved notebook files so reviewers see only the relevant code changes.

- **Stronger R support:** R notebooks can now be debugged with breakpoints and the “Debug Cell” action, and R dataframe outputs in notebook cells now render in the inline Data Explorer for the same interactive exploration you get in the Console.

- **Help on F1:** Pressing F1 on a function in a notebook cell now opens the Help pane, just like in `.py` and `.R` files. Works for both Python and R Jupyter notebooks.

- **UX polish:** Long cell outputs default to scrolling instead of overwhelming the page, the cell action bar stays visible as you scroll through tall cells, markdown cells render footnotes, and your scroll position is preserved when switching between notebook tabs.

#### Posit Assistant and Posit AI

This release introduces two new AI options: Posit Assistant and Posit AI.

- You may have tried some of our previous experiments for AI code assistance available in Positron, Positron Assistant and/or Databot. We are now migrating to a more data-science-specific, holistic, unified approach to AI chat, built on the same Posit Assistant interface that [we recently brought to RStudio](https://posit.co/blog/introducing-ai-in-rstudio/). Instead of switching between tools, you get code generation, next edit suggestions, chat, and agentic tools all in one place. [Learn how to get started](https://assistant.posit.co/docs/downloads/positron/).

- [Posit AI](https://posit.co/products/ai) is a new, optional model provider service available to use with Posit Assistant. Posit AI is a subscription priced at \$20/month for individual users; both Positron and Posit Assistant remain free to use. [Learn how to sign up for an account](https://posit.co/products/ai).

### Changelog

#### New features

- \[[\#11896](https://github.com/posit-dev/positron/issues/11896)\] Notebooks: now track notebook sessions in the top-right interpreter picker.
- \[[\#11773](https://github.com/posit-dev/positron/issues/11773)\] Notebooks: added Shift+Enter keyboard shortcut to run active cell and insert a new cell immediately beneath.
- \[[\#11852](https://github.com/posit-dev/positron/issues/11852)\] Notebooks: added “Copy Output Text” to the notebook cell output right-click menu, enabling copy of selected text or all text output.
- \[[\#10117](https://github.com/posit-dev/positron/issues/10117)\] Notebooks: cell action bars are now sticky and won’t scroll out of view for tall cells.
- \[[\#11775](https://github.com/posit-dev/positron/issues/11775)\] Notebooks: cell execution footer now hides when the cell has not been run and smoothly animates in/out during execution.
- \[[\#10597](https://github.com/posit-dev/positron/issues/10597)\] Notebooks: footnotes in markdown cells now render with superscript links and a numbered footnote section.
- \[[\#12600](https://github.com/posit-dev/positron/issues/12600)\] Notebooks: long notebook outputs are resizable.
- \[[\#12110](https://github.com/posit-dev/positron/issues/12110)\] Notebooks: added [`notebook.save.outputs`](positron://settings/notebook.save.outputs) and [`notebook.save.executionCounts`](positron://settings/notebook.save.executionCounts) settings to optionally exclude outputs and execution counts from saved notebook files, improving version control workflows.
- \[[\#12104](https://github.com/posit-dev/positron/issues/12104)\] Notebooks: R notebooks can now be debugged with breakpoints and the “Debug Cell” action.
- \[[\#10246](https://github.com/posit-dev/positron/issues/10246)\] Notebooks: surface “Restart Kernel” as a top-level toolbar button instead of nesting it in the kernel badge dropdown.
- \[[\#12616](https://github.com/posit-dev/positron/issues/12616)\] Quarto: automatically start a kernel when a Quarto document with inline output is opened, instead of waiting until code is run.
- \[[\#12155](https://github.com/posit-dev/positron/issues/12155)\] Quarto: inline output cells now have a new status line showing execution status and time.
- \[[\#12789](https://github.com/posit-dev/positron/issues/12789)\] Quarto: updated “Show Notebook Console” to work with Quarto inline output.
- \[[\#12684](https://github.com/posit-dev/positron/issues/12684)\] Quarto: added tool to switch the interpreter used to run code with inline output.
- \[[\#12985](https://github.com/posit-dev/positron/issues/12985)\] Quarto: inline outputs are now collapsible.
- \[[\#12928](https://github.com/posit-dev/positron/issues/12928)\] Packages: added support for supplementing Packages pane with metadata from Posit Public Package Manager.
- \[[\#12992](https://github.com/posit-dev/positron/issues/12992)\] Packages: added simple text search to the Packages pane.
- \[[\#12924](https://github.com/posit-dev/positron/issues/12924)\] Packages: added sort action item to the Packages pane.
- \[[\#12923](https://github.com/posit-dev/positron/issues/12923)\] Packages: added category filters to the Packages pane.
- \[[\#11899](https://github.com/posit-dev/positron/issues/11899)\] Interpreter: now show runtime status icon in the interpreter picker to indicate session state.
- \[[\#11905](https://github.com/posit-dev/positron/issues/11905)\] Interpreter: now display notebook and Quarto sessions in the interpreter session quickpick.
- \[[\#12741](https://github.com/posit-dev/positron/issues/12741)\] Interpreter: changed icons shown for runtime sessions.
- \[[\#8923](https://github.com/posit-dev/positron/issues/8923), [\#11901](https://github.com/posit-dev/positron/issues/11901)\] Interpreter: removed the independent, redundant session picker from the Variables pane. The Variables pane now always follows the foreground session.
- \[[\#12753](https://github.com/posit-dev/positron/issues/12753)\] Assistant: migrated authentication for all language model providers to the new Authentication extension.
- \[[\#13195](https://github.com/posit-dev/positron/issues/13195)\] Assistant: Console “Fix” and “Explain” buttons now route error context to the Posit Assistant extension’s new chat API.
- \[[\#13120](https://github.com/posit-dev/positron/issues/13120)\] Assistant: Posit AI provider is out of preview.
- \[[\#12875](https://github.com/posit-dev/positron/issues/12875)\] Extensions: now use Posit Public Package Manager by default for Positron’s extension gallery.
- \[[\#12877](https://github.com/posit-dev/positron/issues/12877)\] Extensions: the new [`positron.extensions.gallerySource`](positron://settings/positron.extensions.gallerySource) setting allows users to switch the extension gallery between Open VSX or P3M.
- \[[\#2136](https://github.com/posit-dev/positron/issues/2136)\] Console: added find/search functionality to the Console (Cmd/Ctrl+F) with support for case-sensitive, whole-word, and regex modes.
- \[[\#8359](https://github.com/posit-dev/positron/issues/8359)\] Python: if no usable Pythons are found, provide installation of `uv` and a supported Python version.
- \[[\#12624](https://github.com/posit-dev/positron/issues/12624)\] R: package names preceding `::` and `:::` are now assigned the `entity.name.namespace` TextMate scope, allowing them to be styled independently from regular variables.
- \[[\#12582](https://github.com/posit-dev/positron/issues/12582)\] R: support clearing the Console via `cat("\014")` / `cat("\f")`.
- \[[\#2974](https://github.com/posit-dev/positron/issues/2974)\] Data Explorer: added a *View Data Frame at Cursor* command that opens the Data Explorer for the variable at the editor cursor, available from the command palette and the editor context menu. Works in R, Python, and Quarto files.
- \[[\#13154](https://github.com/posit-dev/positron/issues/13154)\] Workbench: static assets are now pre-compressed at build time, reducing load times in the browser.
- \[[\#13217](https://github.com/posit-dev/positron/issues/13217)\] Removed the already deprecated `update.systemArchitecture` setting and all remaining components of universal macOS builds. We now only provide architecture-specific builds for macOS.
- \[[\#12857](https://github.com/posit-dev/positron/issues/12857)\] A new [`positron.runApp.previewMode`](positron://settings/positron.runApp.previewMode) setting controls where application previews open by default. Choose between the Viewer pane, an editor tab, an external browser, or no preview at all. This applies to all apps launched through Positron’s Run App framework, including Flask, Dash, FastAPI, Gradio, and Streamlit. Note that Shiny applications remain governed by the existing [`shiny.previewType`](positron://settings/shiny.previewType) setting.

#### Bug fixes

- \[[\#11802](https://github.com/posit-dev/positron/issues/11802)\] Notebooks: fixed how notebook rendering errors could produce a blank screen instead of showing the error recovery UI.
- \[[\#12610](https://github.com/posit-dev/positron/issues/12610)\] Notebooks: now clean up orphaned notebook consoles when notebook is closed.
- \[[\#11802](https://github.com/posit-dev/positron/issues/11802)\] Notebooks: non-ipywidgets HTML-based outputs now render properly.
- \[[\#12914](https://github.com/posit-dev/positron/issues/12914)\] Notebooks: fixed a crash in the notebook kernel selector when a notebook replaces another notebook in a preview tab.
- \[[\#12947](https://github.com/posit-dev/positron/issues/12947)\] Notebooks: fixed cell outputs flashing briefly when re-running a cell.
- \[[\#12065](https://github.com/posit-dev/positron/issues/12065)\] Notebooks: fixed inline Data Explorer sort indicators disappearing after switching tabs.
- \[[\#11777](https://github.com/posit-dev/positron/issues/11777)\] Notebooks: fixed scroll position not being restored when switching tabs or reloading the window.
- \[[\#12320](https://github.com/posit-dev/positron/issues/12320)\] Notebooks: now route relative markdown links in cells to the correct file.
- \[[\#12317](https://github.com/posit-dev/positron/issues/12317)\] Notebooks: fixed scrolling over Plotly charts and other webview-hosted outputs.
- \[[\#12615](https://github.com/posit-dev/positron/issues/12615)\] Notebooks: AI features now respect the [`positron.assistant.aiExcludes`](positron://settings/positron.assistant.aiExcludes) setting.
- \[[\#13244](https://github.com/posit-dev/positron/issues/13244)\] Notebooks: now strip ANSI escape codes when copying cell output text via the cell context menu.
- \[[\#12604](https://github.com/posit-dev/positron/issues/12604)\] Notebooks: switching back to a tab with a large notebook no longer freezes the UI while Monaco editors are recreated.
- \[[\#12662](https://github.com/posit-dev/positron/issues/12662)\] Quarto: fixed stray execution indicators in editor gutter when executing cells in a Quarto document with inline output.
- \[[\#12614](https://github.com/posit-dev/positron/issues/12614)\] Quarto: fixed the Quarto kernel selector appearing on non-Quarto editor panes when a Quarto document is open alongside other editors.
- \[[\#12885](https://github.com/posit-dev/positron/issues/12885)\] Quarto: fixed autocompletion in Quarto docs when inline output is disabled.
- \[[\#12741](https://github.com/posit-dev/positron/issues/12741)\] Quarto: show Quarto icon for Quarto sessions rather than generic notebook icon.
- \[[\#13153](https://github.com/posit-dev/positron/issues/13153)\] Quarto: disable “Interrupt Kernel” for inline output when kernel isn’t running or busy.
- \[[\#12202](https://github.com/posit-dev/positron/issues/12202)\] Assistant: fixed an issue where links in Assistant error messages could have a white background in some themes, making them hard to read.
- \[[\#12456](https://github.com/posit-dev/positron/issues/12456)\] Assistant: fixed text encoding problems in responses for AWS Bedrock.
- \[[\#12954](https://github.com/posit-dev/positron/issues/12954)\] Assistant: updated provider settings tags and default enabled providers.
- \[[\#12920](https://github.com/posit-dev/positron/issues/12920)\] Assistant: fixed Snowflake Cortex model provider rejecting valid credentials.
- \[[\#12142](https://github.com/posit-dev/positron/issues/12142)\] Assistant: resolved Anthropic cache errors when using AWS Bedrock.
- \[[\#12166](https://github.com/posit-dev/positron/issues/12166)\] Assistant: fixed prompt caching and cached token count for AWS Bedrock.
- \[[\#13018](https://github.com/posit-dev/positron/issues/13018)\] Assistant: fixed Azure Foundry managed credentials not auto-configuring on Posit Workbench.
- \[[\#12572](https://github.com/posit-dev/positron/issues/12572), [\#13053](https://github.com/posit-dev/positron/issues/13053)\] Assistant: fixed issues with GitHub Copilot models being missing from model picker.
- \[[\#12974](https://github.com/posit-dev/positron/issues/12974)\] Assistant: fixed Anthropic custom base URL being silently modified during API key validation.
- \[[\#13121](https://github.com/posit-dev/positron/issues/13121)\] Assistant: removed broken *Reset State* command and fixed *Collect Diagnostics* to show correct credential status after auth extension migration.
- \[[\#12730](https://github.com/posit-dev/positron/issues/12730)\] Assistant: fixed issue causing pending console input to be combined with commands run from Assistant.
- \[[\#13195](https://github.com/posit-dev/positron/issues/13195)\] Assistant: Console “Fix” and “Explain” buttons fall back to the built-in quick chat when the Posit Assistant sidebar is disabled, instead of always trying to launch Posit Assistant.
- \[[\#9852](https://github.com/posit-dev/positron/issues/9852)\] Console: fixed performance problems in long-running sessions.
- \[[\#11230](https://github.com/posit-dev/positron/issues/11230)\] Console: fixed the Console hanging on first startup after upgrading Positron.
- \[[\#13152](https://github.com/posit-dev/positron/issues/13152)\] Console: fixed input field not pre-selecting text when renaming a Console session.
- \[[\#12349](https://github.com/posit-dev/positron/issues/12349)\] Python: fixed Python extension activation and interpreter discovery blocking startup, and sped it up.
- \[[\#12397](https://github.com/posit-dev/positron/issues/12397)\] Python: Conda environments without Python will get Python installed upon selection, not discovery.
- \[[\#12367](https://github.com/posit-dev/positron/issues/12367)\] R: fixed loading `.RData`/`.rds` files from the Explorer on Windows.
- \[[\#13229](https://github.com/posit-dev/positron/issues/13229)\] R: fixed incorrect URL matching when starting a Shiny app.
- \[[\#12478](https://github.com/posit-dev/positron/issues/12478)\] Reticulate: now defer `positron-reticulate` activation until it is actually needed, reducing unnecessary work during startup.
- \[[\#9364](https://github.com/posit-dev/positron/issues/9364)\] Help: prevent the Help copy keybinding from hijacking Cmd/Ctrl+C elsewhere in the app when Help focus tracking misses a blur event.
- \[[\#12380](https://github.com/posit-dev/positron/issues/12380)\] Workbench: language-scoped enforced settings (e.g., `[r]`) now apply correctly.
- \[[\#12492](https://github.com/posit-dev/positron/issues/12492)\] Fixed PDF viewer print button and Cmd/Ctrl+P not opening a print dialog.

#### Dependencies

- Updated bundled Quarto to 1.9.37.
