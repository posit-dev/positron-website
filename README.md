# positron-website

[![Netlify Status](https://api.netlify.com/api/v1/badges/2567d399-328e-4f0f-9784-c14cbe238fb7/deploy-status)](https://app.netlify.com/sites/positron-posit-co/deploys)
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" height = 20 /></a>

This is the repo for the Positron website at <https://positron.posit.co/>. 

This site is built with [Quarto](https://quarto.org/) and the [Posit product documentation theme](https://github.com/posit-dev/product-doc-theme), and these educational materials are released under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Positron™ and the Positron icon™ are trademarks of Posit Software, PBC. All rights reserved.

## Reporting issues

We currently use the issue tracker for [Positron](https://github.com/posit-dev/positron). Please report documentation bugs and feature requests at <https://github.com/posit-dev/positron/issues>.

## Linting

This project uses [Vale](https://vale.sh/docs/) for automated linting and compliance with the Posit style guide. 

- If you are a Posit employee, you can find the "Posit Documentation Style Guide" on Confluence.
- If you are an external contributor, we as reviewers will take responsibility for compliance with the guidelines. Thank you for being willing to improve our docs!

Vale runs [via GH action on PRs](https://github.com/posit-dev/positron-website/actions/workflows/lint.yml), but you can also run it locally before you submit a PR if you have [installed Vale](https://vale.sh/docs/vale-cli/installation/) locally. Run `vale .` from the root directory of this project to lint the `.qmd` files used to build to site.
