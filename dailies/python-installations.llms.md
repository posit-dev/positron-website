# Discovering Python Installations

Understand how Positron discovers and manages Python installations. Covers automatic uv installation and support for uv, pyenv, conda, venv, and more environment managers.

This guide explains how Positron discovers and manages Python installations. For using Python in Positron, see our [Python language guide](guide-python.llms.md).

## Python installation discovery

Positron uses multiple strategies to discover Python interpreters and virtual environments across your system. The discovery process includes both global Python installations and various virtual environment managers.

### Supported environment managers

Positron supports the following Python environment managers:

- **venv**: Standard library virtual environments created with `python -m venv`
- **uv**: Virtual environments and Python installations managed by `uv`
- **pyenv**: Python installations managed by `pyenv`, including virtual environments
- **conda**: Conda environments created with `conda create` or `mamba create`, as well as pixi environments created with `pixi init`

Other tools might also be compatible, although Positron does not officially support them.

### Discovery locations

Positron searches for Python installations in the following locations. In general, it is best to use an environment that is highest in this list. Read more about [why virtual environments matter](https://realpython.com/python-virtual-environments-a-primer/#why-do-you-need-virtual-environments).

#### 1. Project environments

Environments associated with the open project, if you have a project folder open. In particular, Positron finds any environment at the root of the open project (for example, `.venv/` or `.conda/` folders).

> **NOTE:**
>
> If you do not have a project open, Positron does not find any project environments, like project `.venv/` folders. In general, Positron does not look across your whole system for all project-level virtual environments. Open a project folder to use that project’s environment.

#### 2. Global environments

Positron also discovers other named environments on your system, including:

- Custom configured environments (see the [discovery settings](#discovery-location-settings))
- Environments in `/opt/python`
- Environments in well-known venv homes, including `$WORKON_HOME`, `~/.venvs`, `~/.virtualenvs`, and `~/.local/share/virtualenvs`
- Conda-managed named environments

#### 3. Base interpreters

Standalone, pip-writable installs. Use these installations as seeds for new virtual environments rather than modifying them:

- Installations from pyenv, python.org, or the Windows registry or store
- Environment-module interpreters

#### 4. System or externally managed interpreters

Base interpreters that you can only use for seeding virtual environments:

- System interpreters like `/usr/bin` or Homebrew-installed
- Tool-managed base interpreters, like the uv or conda base interpreters

> **IMPORTANT:**
>
> Using a system Python installation in a new session can lead to problems (see the official [guidance](https://packaging.python.org/en/latest/specifications/externally-managed-environments/) about this). For that reason, we recommend using virtual environments.

## Automatic uv installation

Positron provides the option to install Python via [uv](https://docs.astral.sh/uv/) to provide an improved Python environment management experience. If you have no Python or only system Pythons, Positron offers to install uv from the **Start New Console Session** dropdown.

You can control uv installation and usage in Positron in a variety of ways:

- **Disable uv installation**: To never see this installation option, set [`python.allowUvPythonInstall`](positron://settings/python.allowUvPythonInstall) to `false`.
- **Use existing uv**: If you have uv already installed system-wide, Positron uses your existing installation.
- **Manual installation**: You can also [install uv yourself](https://docs.astral.sh/uv/getting-started/installation/) if you prefer to manage it directly.

You do not need uv to run Positron. Positron looks for other environment managers like `venv` and `conda`, regardless of whether uv is available.

### What is uv?

[uv](https://docs.astral.sh/uv/) is a modern Python package manager that provides:

- Fast virtual environment creation
- Efficient package installation
- Python version management
- Project dependency management

Positron uses uv to enhance Python workflows, including creating environments, installing packages, and managing Python versions.

## Environment creation and discovery timing

### Creating new environments

You can create new Python environments directly from Positron using the *Python: Create Environment* command:

1.  Open the Command Palette with
2.  Select *Python: Create Environment*
3.  Choose from available environment providers:
    - **uv**: Creates a uv-managed virtual environment (if uv is available)
    - **venv**: Creates a standard virtual environment using `python -m venv`
    - **conda**: Creates a conda environment (if conda is available)

Positron creates the environment in your workspace and automatically discovers it.

You can also use the [New Folder From Template feature](folder-templates.llms.md#new-folder-from-template) to create a new Python project, and set up an environment as part of the project.

### Discovering existing environments

Positron automatically discovers environments when:

- You open Positron
- You open a new workspace folder
- Positron detects certain file system changes in watched directories
- You refresh using the *Interpreter: Discover All Interpreters* command

The discovery process runs in the background and updates the interpreter list as Positron finds new environments.

## Other details

### IPython kernel

Positron requires the [IPython kernel](https://pypi.org/project/ipykernel/) (version 6.19.1 or higher) to communicate with Python. By default, Positron bundles the IPython kernel for the CPython implementation (the standard Python implementation) and adds it to the [Python search path](https://docs.python.org/3/library/sys_path_init.llms.md). This means you can use new environments immediately after Positron creates them, without installing extra dependencies.

If you prefer finer control over your Python environment, set the [`python.useBundledIpykernel`](positron://settings/python.useBundledIpykernel) setting to false. If you do that or are using an implementation other than CPython, install the IPython kernel yourself with `pip install ipykernel`.

### Unsupported Python versions

Positron supports the [supported versions](https://devguide.python.org/versions/) of Python, and might continue to support end-of-life versions for a time after. Positron can discover other versions, but you might run into issues using them.

## Troubleshooting

### Environment not appearing

If you configure the above settings correctly, Positron supports your Python version, and *Interpreter: Discover All Interpreters* or a restart of Positron does not help, check the logs. See more in the [troubleshooting guide](troubleshooting.llms.md). Positron logs the discovery process in the Python Locator and Python Language Pack channels.

### uv installation issues

If you encounter issues with the automatic uv installation in Positron:

1.  **Check network connectivity**: uv installation requires internet access to download the binary.
2.  **Manual installation**: You can also [install uv yourself](https://docs.astral.sh/uv/getting-started/installation/) if you prefer to manage it directly.
3.  **Disable automatic installation**: If you do not want Positron to show you uv installation, disable it by setting [`python.allowUvPythonInstall`](positron://settings/python.allowUvPythonInstall) to `false`.

For detailed uv troubleshooting, refer to the [uv documentation](https://docs.astral.sh/uv/).

## Related settings

Key settings that control Python environment discovery:

### Discovery location settings

- [`python.interpreters.include`](positron://settings/python.interpreters.include): Specific interpreter paths to include
- [`python.interpreters.exclude`](positron://settings/python.interpreters.exclude): Interpreter paths to exclude from discovery
- [`python.interpreters.override`](positron://settings/python.interpreters.override): Override discovery so Positron shows only these

### Environment providers

- [`python.environmentProviders.enable`](positron://settings/python.environmentProviders.enable): Turn specific environment providers on or off for environment creation (`Venv`, `Conda`, `uv`)

### Discovery behavior

- [`python.defaultInterpreterPath`](positron://settings/python.defaultInterpreterPath): Default Python interpreter path (used only the first time when no other interpreter takes precedence)
- [`python.useBundledIpykernel`](positron://settings/python.useBundledIpykernel): Turn the built-in IPython kernel on or off

## Related commands

- *Interpreter: Discover All Interpreters*: Find new interpreters
- *Interpreter: Select Session*: Select a running interpreter session
- *Python: Create Environment*: Create a new virtual environment
