# Help Pane

Access rich, in-IDE documentation for Python and R with the Help pane. View function docs, package vignettes, and source code without leaving Positron.

The **Help** pane provides rich, in-editor documentation for Python and R. It can be used to display information about an object, function, or package.

## Getting Help in Python & R

You can open documentation in the **Help** pane using language-specific tools or the keyboard shortcut F1F1. These methods automatically open the **Help** pane and display documentation.

## Python

``` python
int?
# or
help(int)
```

#### Supported content

The **Help** pane supports the following types of documentation in Python:

- Modules, classes, functions, and objects with docstrings
- Rich rendering for common docstring formats: Google, NumPy, Sphinx, Epytext

Additionally, you can use syntax like `int??` to view the source code for functions and classes, when available.

## R

``` r
?paste0
# or
help(paste0)
```

#### Supported content

The **Help** pane supports the following types of documentation in R:

- Function and package documentation
- Package vignettes (when available)

The **Help** pane includes built-in navigation tools:

-  Search – Find keywords within a help page

-  Back and Forward – Navigate through recent help views

All documentation is fully interlinked, with internal references and copyable code examples available where supported.
