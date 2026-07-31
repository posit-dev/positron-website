# Add notebook debugging documentation page

Addresses https://github.com/posit-dev/positron/issues/13276

Adds a new `notebook-debugging.qmd` page under the Jupyter Notebooks section documenting debugging in the Positron Notebook Editor:

- Requirements (Python via debugpy, R out of the box)
- Setting breakpoints, including cross-cell breakpoints and the Run Cell vs Debug Cell distinction
- Starting a debug session (Debug Cell button, keyboard shortcut, Command Palette) and its lifecycle (session ends when the cell finishes)
- Inspecting variables, watch expressions, and the call stack while paused
- Step controls, tips, and current limitations

Also links the page from the notebook editor page's key features list and adds it to the positron and workbench nav profiles.

Screenshots and a walkthrough video still need to be captured; the spots are marked with `TODO(screenshot)` / `TODO(video)` HTML comments in the page.
