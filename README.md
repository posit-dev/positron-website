# positron-website

[![Netlify Status](https://api.netlify.com/api/v1/badges/2567d399-328e-4f0f-9784-c14cbe238fb7/deploy-status)](https://app.netlify.com/sites/positron-posit-co/deploys)
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" height = 20 /></a>

This is the repo for the Positron website at <https://positron.posit.co/>.

This site is built with [Quarto](https://quarto.org/) and the [Posit product documentation theme](https://github.com/posit-dev/product-doc-theme), and these educational materials are released under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Positron™ and the Positron icon™ are trademarks of Posit Software, PBC. All rights reserved.

## Reporting issues

We currently use the issue tracker for [Positron](https://github.com/posit-dev/positron). Please report documentation bugs and feature requests at <https://github.com/posit-dev/positron/issues>.

## Prerequisites

This repo uses [Git LFS](https://git-lfs.com/) for video files. Run `git lfs install` before cloning so large files are pulled correctly.

## Local development

If you have [Quarto installed locally](https://quarto.org/docs/get-started/) and Chrome or Edge, you can preview the site by running one of the Debug Configurations in VS Code or Positron.

The configurations run `quarto preview` and then open the site in a new browser window.
- **Preview Docs (Chrome)**: Preview the site in Chrome
- **Preview Docs (Edge)**: Preview the site in Edge

The site will re-render as you make changes to the `.qmd` files.

Alternatively, you can run the command `quarto preview` in the terminal.

## Managing execution and rendering

Some `.qmd` files used for our site involve executable code, like the `.qmd` files that creates <https://positron.posit.co/download> and <https://positron.posit.co/install>. We currently use the ["Local Execution with CI Rendering" option described in the Quarto docs](https://quarto.org/docs/publishing/ci.html#rendering-for-ci), with the [freeze](https://quarto.org/docs/projects/code-execution.html#freeze) execution option to make it easier for us to collaborate together across the large number of pages. For now, if you need to update a page involving computations, be sure to render that page locally and check in the files created in the `_freeze` directory.

## Videos and Git LFS

When adding or replacing a video, make sure Git LFS is initialized (`git lfs install`) so the file goes through the LFS filter.

If you see a "phantom diff" on a video file you didn't touch, it means that file was committed as raw binary instead of an LFS pointer. Don't commit the change into an unrelated PR: run `git restore <file>` to clear it locally, and open a separate PR to re-add the file through LFS:

```bash
git lfs install          # ensure LFS is set up
git rm --cached <file>   # remove the raw binary from the index
git add <file>           # re-add it through the LFS filter
git commit
```
