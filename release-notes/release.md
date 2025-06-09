### Highlights

- Stable releases of Positron are now available! Thank you to all our beta users who have been testing and giving feedback on our prereleases over the last year. ❤️
- Positron Assistant is... 🤖
- Another cool thing we want to highlight about this release is... 🪩

### Changelog

#### New features

- [[#1744]](https://github.com/posit-dev/positron/issues/1744) R: A new Code Action is available for generating a roxygen documentation skeleton.
- [[#1728]](https://github.com/posit-dev/positron/issues/1728) By default, Positron no longer tries to save untitled editors when a debug session is started. This is to avoid disrupting the user workflow with a save dialog when a debug session starts.
- Foding rules are now supported for R comment sections [[#18]](https://github.com/posit-dev/positron/issues/18) and R code cells [[#2924]](https://github.com/posit-dev/positron/issues/2924). Thanks to our contributor [@kv9898](https://github.com/kv9898)!
- [[#7875]](https://github.com/posit-dev/positron/issues/7875) Custom environment variables for the Terminal and Consoles can now be configured in the Settings UI.
- [[#7550]](https://github.com/posit-dev/positron/issues/7550) The support for scaffolding a new folder based on templates has been revamped. Try out the improved "Workspaces: New Folder from Template..." command.

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

#### Dependencies

- Updated something!
