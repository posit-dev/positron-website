# Python in Positron

Complete guide to Python development in Positron. Learn about environment management, IPython magics, formatting with Ruff, and interactive data science features.

Positron ships with first class support for Python, along with [R](guide-r.llms.md). Start with our guide on how Positron [discovers and manages Python installations](python-installations.llms.md), then read on for details on working with Python code in Positron.

## Settings

> **NOTE:**
>
> In addition to providing settings, Positron also provides [keyboard shortcuts](keyboard-shortcuts.llms.md) and [bundled extensions](extensions.llms.md#included-extensions), for a “batteries included” experience for data science with Python.

Positron provides setting defaults for working with Python for data science, but you can override or change these defaults if you prefer a different experience. For example:

- Positron bundles [Pyrefly](https://open-vsx.org/extension/meta/pyrefly) to provide Python language server features including syntax highlighting, type checking, and code completion. Positron sets the [`pyrefly.commentFoldingRanges`](positron://settings/pyrefly.commentFoldingRanges) setting to true to provide folding ranges for special `# Section Name ----` comment sections. If you prefer to disable this feature, change the setting to false.
- Positron bundles [Ruff](https://docs.astral.sh/ruff/) to provide [formatting](#code-formatting) for Python and sets the [`ruff.importStrategy`](positron://settings/ruff.importStrategy) setting to `"useBundled"`. If you prefer to use a Ruff installation that you manage yourself, change this setting to `"fromEnvironment"`.

You can see *all* the setting defaults that Positron provides with the command *Preferences: Open Default Settings (JSON)*.

## Python language server

The built-in language server in Positron uses your running Python session to provide runtime-aware completions and hover previews. Beyond what is in code, it knows your DataFrame column names, your dictionary keys, your environment variables, and more. As discussed in the [Settings section above](#settings), it also bundles [Pyrefly](https://pyrefly.org/) to handle the static analysis side: type checking, go-to-definition, rename, and code actions. Both run concurrently, and Positron merges their results.

Positron also makes it straightforward to switch the static analysis language server:

1.  Open the **Extensions** view ().
2.  Search for and install the language server you want to try (e.g., `basedpyright`, `ty`, or `zuban`).
3.  Disable Pyrefly: search for `pyrefly` in Extensions, and click **Disable**.
4.  Restart Positron.

If you want to permanently keep Pyrefly from auto-activating, you can use the [`extensions.allowed`](positron://settings/extensions.allowed) setting:

``` json
{
    "extensions.allowed": {
        "meta.pyrefly": false,
        "*": true
    }
}
```

To read more about Python language servers, see our [blog post on Python type checkers and language servers](https://opensource.posit.co/blog/2026-03-31_python-type-checkers/).

## Magics

Positron provides support for [IPython-style magics](https://ipython.readthedocs.io/en/stable/interactive/magics.llms.md) in the Positron console (as well as Python scripts and Jupyter notebooks, where appropriate). Magics are special commands prefixed with the `%` symbol that provide convenient shortcuts for common tasks. You can see the supported magics by running the `%lsmagic` command in the Positron console.

Positron provides three new, custom magics created specifically for working in Positron:

- `%view` opens a Python object in the [Data Explorer](data-explorer.llms.md). You can use this magic most simply via `%view df`, or additionally like `%view df.groupby('column').sum()` or `%view df "My Dataset"`.
- `%connection_show` shows a connection object in the [**Connections** pane](connections-pane.llms.md). Use this magic like `%connection_show my_connection`.
- `%clear` clears the Console.

## Code formatting

Positron can format Python code with [Ruff](https://docs.astral.sh/ruff/), a Python linter and formatter. Positron includes Ruff as a [bootstrapped extension](extensions.llms.md#bootstrapped-extensions) and installs it for you, including the bundled Ruff command line tool. Most Positron users do not need to do anything intentional to install Ruff or to keep it up-to-date.

You can format your Python code with various explicit and implicit gestures. You can use the commands *Format Selection* or *Format Document* to format specific bits of code. You can even configure Positron to run Ruff automatically whenever you save a Python file. In the Settings UI, search for `@lang:python editor.formatOnSave` and enable the setting, either at the workspace (recommended) or user level. This will add the following to the appropriate `settings.json`:

``` json
{
    "[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.formatOnSave": true
    }
}
```

## Debugging

Positron bundles the [Python Debugger](https://open-vsx.org/extension/ms-python/debugpy) as a [bootstrapped extension](extensions.llms.md#bootstrapped-extensions) to provide debugging support for Python code. You can set breakpoints, step through code, and inspect variables during debugging sessions. Learn more from the [VS Code documentation on debugging Python](https://code.visualstudio.com/docs/python/debugging).

> **NOTE:**
>
> Positron provides basic support for debugging in the console via `import ipdb; ipdb.set_trace()` and `%debug`. [Follow along on GitHub for further improvements](https://github.com/posit-dev/positron/issues/8688) in this support.

## Plots

Positron automatically sets the [`matplotlib` backend](https://matplotlib.org/stable/users/explain/figure/backends.llms.md#what-is-a-backend) to `module://positron.matplotlib_backend`. This configures your plots to be displayed inside the [Plots pane](plots-pane.llms.md) by default. If you prefer to use your own backend, you can override this setting by running `matplotlib.use(backend_name)` in the active Console or by setting the environment variable `MPLBACKEND` to the desired backend name.
