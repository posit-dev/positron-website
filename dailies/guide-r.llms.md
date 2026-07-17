# Overview

Master R development in Positron with native language support. Discover settings, keyboard shortcuts, debugging tools, and interactive Console features.

Positron ships with first class support for R, along with [Python](guide-python.llms.md). Start with our guide on how Positron [discovers and manages R installations](r-installations.llms.md), then read on for details on working with R code in Positron.

## Settings

> **NOTE:**
>
> If you’d prefer to customize Positron to feel similar to RStudio, learn [what settings to consider](migrate-rstudio-settings-and-extensions.llms.md#settings-for-rstudio-users).

Positron provides setting defaults for working with R, but you can override or change these defaults if you prefer a different experience. For example, Positron sets the tab size for R code to 2 spaces, but if you prefer 4 spaces, you can change the [`editor.tabSize`](positron://settings/editor.tabSize) setting for R files by adding the following to your user or workspace `settings.json`:

``` json
{
    "[r]":  {
      "editor.tabSize": 4
    }
}
```

You can see *all* the setting defaults that Positron provides with the command *Preferences: Open Default Settings (JSON)*.

## Keyboard shortcuts

The keyboard shortcuts in Positron are largely a superset of the keyboard shortcuts used by Visual Studio Code, plus additional [keyboard shortcuts](keyboard-shortcuts.llms.md) specific to Positron’s data science features. Some of those additional shortcuts are specific to R programming:

| Shortcut | Description                                                     |
|----------|-----------------------------------------------------------------|
|          | Insert the pipe operator (`|>` or `%>%`)[^1]                    |
|          | Insert the assignment operator (`<-`)                           |
| , HH     | Insert section                                                  |
|          | Load the current R package, if any, with `devtools::load_all()` |
|          | Build and install the current R package, if any                 |
|          | Test the current R package, if any                              |
|          | Check the current R package, if any                             |
|          | Document the current R package, if any                          |

> **NOTE:**
>
> If you’d prefer to use keybindings as similar as possible to RStudio, learn [how to enable them](migrate-rstudio-keybindings.llms.md) in Positron. This will overwrite some of Positron’s default keybindings, but will provide a more familiar experience for RStudio users.

You can create [custom keyboard shortcuts](keyboard-shortcuts.llms.md#custom-shortcuts) as well.

## Debugging

Positron supports a modern R debugging workflow with breakpoints, variables inspections, and more. See [Debugging R code](guide-r-debugging.llms.md) for details on setting breakpoints and stepping through your code.

## Session hooks

Positron can run R code once the session is fully operational, via the `positron.session_init` and `positron.session_reconnect` hooks. See [R session hooks](guide-r-session-hooks.llms.md) for details.

## Footnotes

[^1]: You can choose which pipe operator to insert via the [`positron.r.pipe`](positron://settings/positron.r.pipe) setting.
