# Install Positron

Get started with Positron right away. Install the free data science IDE for Python and R, with prerequisites and setup instructions for all platforms.

Positron is a modern, extensible IDE for data science built on [Code OSS](https://github.com/microsoft/vscode). Before you install Positron, please review the prerequisites to ensure your system is ready.

## Prerequisites

In most cases, Positron is ready to go as soon as it is installed. Check the section for your platform or language to see if you need anything more.

### Windows setup

If you’re using Windows, make sure you have the [latest Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#latest-microsoft-visual-c-redistributable-version) installed.

### Optional language setup

Positron runs without any programming language installed. If you plan to use R or Python, follow these steps to get your environment working.

## Python

Positron works with [actively supported versions](https://devguide.python.org/versions/#versions) of Python.

If you do not have a valid Python version available, Positron [can install one for you](python-installations.llms.md#automatic-uv-installation). If you prefer to use an existing environment, Positron supports the following Python environment managers:

- **venv**: Standard library virtual environments created with `python -m venv`
- **uv**: Virtual environments and Python installations managed by `uv`
- **pyenv**: Python installations managed by `pyenv`, including virtual environments
- **conda**: Conda environments created with `conda create` or `mamba create`, as well as pixi environments created with `pixi init`

Other tools might also be compatible, even if Positron does not officially support them. For the full list of requirements, see [Python environment qualifications](python-installations.llms.md).

## R

Ensure you have R 4.2 or higher installed. To install R, follow the [instructions for your operating system](https://cloud.r-project.org/).

Alternatively, if you’d like to have multiple R installations, [rig](https://github.com/r-lib/rig) is a great tool to manage this which works well with Positron.

If you’re an R package developer, you will also want to make sure that you have the current versions of certain R packages, all of which had recent updates to make them work more smoothly in Positron. Run one of the code snippets below to ensure that you are up-to-date:

``` r
# if you're a pak person (we are!)
pak::pak(c("usethis", "cli", "crayon", "rlang", "roxygen2", "pkgload"))

# or using base R
install.packages(c("usethis", "cli", "crayon", "rlang", "roxygen2", "pkgload"))
```

> **NOTE:**
>
> If you’re a Windows user, note that Positron doesn’t bundle [Rtools](https://cran.r-project.org/bin/windows/Rtools/). If you need Rtools for your package development or other work, you can either use the official guidance from CRAN on installing Rtools and putting it on the PATH, or alternatively, use [rig](https://github.com/r-lib/rig) to install and set up Rtools:
>
> ``` bash
> rig system rtools add
> ```

## Install Positron

Download the installer for your operating system from the button below and follow the standard installation process for your platform. You only need to install Positron once, as it [automatically updates](updating.llms.md) to the latest version after installation.

> **IMPORTANT:**
>
> Please review [Positron’s license agreement](licensing.llms.md) and [privacy policy](https://posit.co/about/privacy-policy/). Your acceptance of this license agreement and privacy policy is required as a condition to proceeding with your download or use of the software.
>
> I agree to the [Positron license agreement](licensing.llms.md) and [Posit Privacy Policy](https://posit.co/about/privacy-policy/).

[Download Positron ](#)

[Download for Windows (x64)](#) [Download for Windows (arm64)](#)

[Download for macOS (Apple Silicon)](#) [Download for macOS (Intel)](#)

[All Downloads](download.llms.md)
