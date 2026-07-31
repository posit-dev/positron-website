# Restructure notebook editor docs for GA

Addresses https://github.com/posit-dev/positron/issues/14327

Text-only documentation uplift for the Positron Notebook Editor going GA. Branched off `docs/notebook-debugging` (please merge that PR first; this diff includes its commit until then).

- Restructure `positron-notebook-editor.qmd` into subsections and add new sections: Running cells (with shortcuts and execution status indicators), Cells (markdown features incl. KaTeX math and Mermaid diagrams, cell tags), Cell outputs (supported MIME types, interactive outputs via Plotly/Bokeh/HoloViews/ipywidgets, inline Data Explorer, output actions), Notebook outline, Export to scripts and Quarto, Notebook console (experimental), and Keyboard shortcuts (incl. the Notebook Help panel)
- Add missing settings to the settings section (output scrolling/truncation, `positron.assistant.notebook.autoFollow`)
- Fold the legacy notebook editor page into `jupyter-notebooks.qmd` (with a redirect alias) and remove it from both nav profiles, per the issue checklist; update all inbound links
- Fix a duplicated launch-post sentence on the overview page and link notebook shortcuts from the Keyboard Shortcuts page
- Mark every screenshot/video that needs re-capture (especially Assistant UI) with `TODO(screenshot)` / `TODO(video)` comments

All claims are grounded in current Positron main behavior (verified against source and merged PRs). Notably, plot export to file is not documented because only Copy Image / Copy Output ship today.
