### Highlights

- Stable releases of Positron are now available! Thank you to all our beta users who have been testing and giving feedback on our prereleases over the last year. ❤️
- For users who are interested in trying out new features at a faster cadence, we now provide a channel of daily builds; you can opt in to these builds by changing the [`update.positron.channel` setting](positron://settings/update.positron.channel) to `"dailies"`. 🪩
- Positron Assistant is... 🤖

### Changelog

#### New features

- [[#1744]](https://github.com/posit-dev/positron/issues/1744) R: A new Code Action is available for generating a roxygen documentation skeleton.
- [[#1728]](https://github.com/posit-dev/positron/issues/1728) By default, Positron no longer tries to save untitled editors when a debug session is started. This is to avoid disrupting the user workflow with a save dialog when a debug session starts.
- Folding rules are now supported for R comment sections [[#18]](https://github.com/posit-dev/positron/issues/18) and R code cells [[#2924]](https://github.com/posit-dev/positron/issues/2924). Thanks to our contributor [@kv9898](https://github.com/kv9898)!
- [[#7875]](https://github.com/posit-dev/positron/issues/7875) Custom environment variables for the Terminal and Consoles can now be configured in the Settings UI.
- [[#7550]](https://github.com/posit-dev/positron/issues/7550) The support for scaffolding a new folder based on templates has been revamped. Try out the improved "Workspaces: New Folder from Template..." command.
- [[#7838]](https://github.com/posit-dev/positron/issues/7838) The Assistant project tree tool now takes parameters to filter the tree output.
- [[#7404]](https://github.com/posit-dev/positron/issues/7404) Improved the Assistant Language Model Provider Configuration Modal close experience.
- [[#6158]](https://github.com/posit-dev/positron/issues/6158) Python Consoles now automatically reload imported files, so any changes made to a module are automatically picked up without needing to restart the Console session. You can opt out of this behavior with the [`python.enableAutoReload` setting](positron://settings/python.enableAutoReload).
- [[#7202]](https://github.com/posit-dev/positron/issues/7202) The Positron version field can now be specified and validated in Positron extensions.
- [[#8018]](https://github.com/posit-dev/positron/issues/8018) Added a new Agent mode to Positron Assistant; note that you'll now need to use this new mode if you want Assistant to run code on your behalf.
- [[#7902]](https://github.com/posit-dev/positron/issues/7902) New Python Projects can optionally now create a `pyproject.toml` file.
- [[#6167]](https://github.com/posit-dev/positron/issues/6167) We now link to our documentation from the Help menu.
- [[#6650]](https://github.com/posit-dev/positron/issues/6650) The up/down console input history navigation actions are now commands that you can bind custom keys to.



#### Bug fixes

- [[#3955]](https://github.com/posit-dev/positron/issues/3955) Notebook execution now respects the `raises-exception` cell tag and continues running subsequent cells after exceptions.
- [[#7884]](https://github.com/posit-dev/positron/issues/7884) Fixed how exited runtimes are shown in the dropdown of the console <kbd>+</kbd> button.
- [[#6987]](https://github.com/posit-dev/positron/issues/6987) Fixed console button and label behavior during interpreter restarts.
- [[#7406]](https://github.com/posit-dev/positron/issues/7406) Fixed failures loading local web server (e.g. Shiny) content in the Viewer pane in Remote SSH sessions.
- [[#7777]](https://github.com/posit-dev/positron/issues/7777) Fixed issue causing all JSON files to have the filetype "renv lockfile".
- [[#5101]](https://github.com/posit-dev/positron/issues/5101) Positron's version is now included in the built-in Issue Reporter and Diagnostics command output.
- [[#4843]](https://github.com/posit-dev/positron/issues/4843) R: Fixed issue opening localhost URLs from `shiny::paneViewer()` and related methods. 
- [[#6915]](https://github.com/posit-dev/positron/issues/6915) Jupyter notebooks: Added support for `update_display_data` requests.
- The `RSTUDIO_PANDOC` environment variable is now set correctly on Linux builds [[#7929]](https://github.com/posit-dev/positron/issues/7929) and in terminals and tasks as well as R sessions [[#7700]](https://github.com/posit-dev/positron/issues/7700).
- [[#7402]](https://github.com/posit-dev/positron/issues/7402) The `QUARTO_R` environment variable now points to your chosen R version in the Terminal.
- [[#7239]](https://github.com/posit-dev/positron/issues/7239) Fixed failure to set working directory from the Explorer when connecting via Remote SSH from Windows to Linux.
- [[#6701]](https://github.com/posit-dev/positron/issues/6701) Python: Updated search strategy to find uv interpreters more often.
- [[#7967]](https://github.com/posit-dev/positron/issues/7967) Fixed behavior on first boot of Positron to not show featured extension walkthroughs.
- [[#6422]](https://github.com/posit-dev/positron/issues/6422) We no longer encode URLs to display in the Viewer pane.
- [[#7510]](https://github.com/posit-dev/positron/issues/7510) Fixed plot image encoding for Anthropic model provider.
- [[#7781]](https://github.com/posit-dev/positron/issues/7781) Fixed how the plot history can be scrolled using the mouse wheel.
- [#7873, #7995] Fixed bug where specific Python console logs were printed to the user.
- [[#6660]](https://github.com/posit-dev/positron/issues/6660) Fixed R session management during sleep mode.
- [[#7850]](https://github.com/posit-dev/positron/issues/7850) Fixed duplicate preview buttons for `.Rmd` files.
- [[#7414]](https://github.com/posit-dev/positron/issues/7414) Folder templates for disabled languages no longer appear in New Folder from Template modal.
- [[#8052]](https://github.com/posit-dev/positron/issues/8052) Fixed Assistant sometimes failing to inspect variables.
- [[#7969]](https://github.com/posit-dev/positron/issues/7969) Fixed error using Github Copilot with Intel Mac computers.

#### Dependencies

- Updated bundled version of Air to [0.14.0](https://github.com/posit-dev/air/blob/main/editors/code/CHANGELOG.md#0140).
