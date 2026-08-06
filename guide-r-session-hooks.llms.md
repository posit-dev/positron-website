# R session hooks

Run R code once Positron is fully operational with the positron.session_init and positron.session_reconnect hooks.

Positron supports hooks to run some R code once R startup is complete and Positron is able to handle requests related to the user interface (UI), such as many [rstudioapi](https://rstudio.github.io/rstudioapi/) calls:

- `positron.session_init` fires when a session starts or restarts.
- `positron.session_reconnect` fires when Positron reconnects to an existing R session.

These hooks are analogous to RStudio’s [`rstudio.sessionInit`](https://rstudio.github.io/rstudioapi/articles/r-session.llms.md#running-at-startup) hook.

## Why session hooks?

Code in `.Rprofile` runs very early, before Positron is ready to respond to UI-related requests. That’s fine for setting options, but it’s too early to drive the UI or to query it for information. Session hooks solve this by deferring code execution until Positron is fully connected to the R session.

Common uses include:

- Driving the UI, such as opening a file with [`rstudioapi::navigateToFile()`](https://rstudio.github.io/rstudioapi/reference/navigateToFile.llms.md).
- Querying the UI for information, such as the current workspace with [`rstudioapi::getActiveProject()`](https://rstudio.github.io/rstudioapi/reference/projects.llms.md) or the actual [console width](https://cli.r-lib.org/reference/console_width.llms.md).

## Registering a hook

Register a hook with [`setHook()`](https://stat.ethz.ch/R-manual/R-patched/library/base/help/setHook.llms.md), typically in your `.Rprofile`. You usually want to use `action = "append"`, so you don’t clobber any hook logic that has been registered elsewhere:

``` r
setHook(
  "positron.session_init",
  function(start_type) {
    # your code here
  },
  action = "append"
)
```

### `positron.session_init`

The `positron.session_init` hook fires when an R session starts or restarts. The hook function should accept a `start_type` argument, which is one of:

- `"new"`: a new R session, whether in a new or existing Positron window.
- `"restart"`: an existing R session that was restarted within a Positron window.

``` r
setHook(
  "positron.session_init",
  function(start_type) {
    switch(
      start_type,
      new = message("Welcome to Positron ", rstudioapi::getVersion()),
      restart = message("Welcome BACK to Positron ", rstudioapi::getVersion())
    )
  },
  action = "append"
)
```

### `positron.session_reconnect`

The `positron.session_reconnect` hook fires when Positron reconnects to an R session that is already running, for example after reloading the Positron window or resuming a session on Posit Workbench. Because the R session itself is not starting fresh, your `.Rprofile` does not run again on reconnect, but this hook does. This function takes no arguments:

``` r
setHook(
  "positron.session_reconnect",
  function() {
    message("Reconnected to Positron ", rstudioapi::getVersion())
  },
  action = "append"
)
```

## Comparison to RStudio

| Event | RStudio [`rstudio.sessionInit`](https://rstudio.github.io/rstudioapi/articles/r-session.llms.md#running-at-startup) | Positron |
|----|----|----|
| Session start | Fires with `newSession = TRUE` | `positron.session_init` with `start_type = "new"` |
| Session restart | Fires with `newSession = TRUE` | `positron.session_init` with `start_type = "restart"` |
| Reconnect | Fires with `newSession = FALSE` | `positron.session_reconnect` |

Anything you can do via `rstudio.sessionInit` you can also achieve with the `positron.session_init` and `positron.session_reconnect` hooks. The Positron hooks provide more control, because it’s possible to distinguish a new session from a restart.
