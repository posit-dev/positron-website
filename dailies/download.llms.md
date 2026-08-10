# Download Positron

Download and install Positron for Windows, macOS, or Linux. Free data science IDE supporting Python and R, with prerequisites, setup instructions, and automatic updates.

Download the desktop installer for your platform. Most systems need nothing else, but you can check the [prerequisites](#prerequisites) to be sure.

### Recommended for you

Detecting your operating system…

By downloading and using Positron, you agree to the Positron [license agreement](licensing.llms.md) and [privacy policy](https://posit.co/about/privacy-policy/).

## All platforms

By downloading and using Positron, you agree to the Positron [license agreement](licensing.llms.md) and [privacy policy](https://posit.co/about/privacy-policy/).

####  macOS 11.0+

Apple Silicon\
(M-series)

[ 997M](https://cdn.posit.co/positron/releases/mac/arm64/Positron-2026.08.1-2-arm64.dmg)

Intel

[ 1009M](https://cdn.posit.co/positron/releases/mac/x64/Positron-2026.08.1-2-x64.dmg)

####  Windows

**x64** (Windows 10+)

User install

[ 499M](https://cdn.posit.co/positron/releases/win/x86_64/Positron-2026.08.1-2-UserSetup-x64.exe)

System install

[ 499M](https://cdn.posit.co/positron/releases/win/x86_64/Positron-2026.08.1-2-Setup-x64.exe)

**ARM64** (Windows 11)

User install

[ 489M](https://cdn.posit.co/positron/releases/win/arm64/Positron-2026.08.1-2-UserSetup-arm64.exe)

System install

[ 489M](https://cdn.posit.co/positron/releases/win/arm64/Positron-2026.08.1-2-Setup-arm64.exe)

####  Linux

**x64**

.deb (Ubuntu, Debian)

[ 569M](https://cdn.posit.co/positron/releases/deb/x86_64/Positron-2026.08.1-2-x64.deb)

.rpm (Red Hat, Fedora)

[ 653M](https://cdn.posit.co/positron/releases/rpm/x86_64/Positron-2026.08.1-2-x64.rpm)

**ARM64**

.deb (Ubuntu, Debian)

[ 534M](https://cdn.posit.co/positron/releases/deb/arm64/Positron-2026.08.1-2-arm64.deb)

.rpm (Red Hat, Fedora)

[ 614M](https://cdn.posit.co/positron/releases/rpm/arm64/Positron-2026.08.1-2-arm64.rpm)

SHA-256 checksums

| Platform | Installer | Size | SHA-256 |
|:---|:---|:---|:---|
| Windows 10, 11 x64 (system level install) | [Positron-2026.08.1-2-Setup-x64.exe](https://cdn.posit.co/positron/releases/win/x86_64/Positron-2026.08.1-2-Setup-x64.exe) | 499M | d466795 |
| Windows 10, 11 x64 (user level install) | [Positron-2026.08.1-2-UserSetup-x64.exe](https://cdn.posit.co/positron/releases/win/x86_64/Positron-2026.08.1-2-UserSetup-x64.exe) | 499M | ea67b92 |
| Windows 11 arm64 (system level install) | [Positron-2026.08.1-2-Setup-arm64.exe](https://cdn.posit.co/positron/releases/win/arm64/Positron-2026.08.1-2-Setup-arm64.exe) | 489M | 12690ad |
| Windows 11 arm64 (user level install) | [Positron-2026.08.1-2-UserSetup-arm64.exe](https://cdn.posit.co/positron/releases/win/arm64/Positron-2026.08.1-2-UserSetup-arm64.exe) | 489M | 2e65f74 |
| MacOS 11.0+ (arm64/Apple Silicon) | [Positron-2026.08.1-2-arm64.dmg](https://cdn.posit.co/positron/releases/mac/arm64/Positron-2026.08.1-2-arm64.dmg) | 997M | 538b8ed |
| MacOS 11.0+ (x64/Intel) | [Positron-2026.08.1-2-x64.dmg](https://cdn.posit.co/positron/releases/mac/x64/Positron-2026.08.1-2-x64.dmg) | 1009M | 8f023df |
| Debian-based Linux x64 (Ubuntu 20+) | [Positron-2026.08.1-2-x64.deb](https://cdn.posit.co/positron/releases/deb/x86_64/Positron-2026.08.1-2-x64.deb) | 569M | e307d37 |
| Debian-based Linux arm64 (Ubuntu 20+) | [Positron-2026.08.1-2-arm64.deb](https://cdn.posit.co/positron/releases/deb/arm64/Positron-2026.08.1-2-arm64.deb) | 534M | 78ccb9b |
| Red Hat-based Linux x64 (RHEL9) | [Positron-2026.08.1-2-x64.rpm](https://cdn.posit.co/positron/releases/rpm/x86_64/Positron-2026.08.1-2-x64.rpm) | 653M | 1b8d889 |
| Red Hat-based Linux arm64 (RHEL9) | [Positron-2026.08.1-2-arm64.rpm](https://cdn.posit.co/positron/releases/rpm/arm64/Positron-2026.08.1-2-arm64.rpm) | 614M | 948370d |

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

## Staying up to date

Once you install Positron, it will [automatically check for updates moving forward](updating.llms.md).

> **NOTE:**
>
> Want to be notified about upcoming releases, new features, and community events? [Sign up for Positron updates](https://posit.co/positron-updates-signup/).

## Positron Pro on Posit Workbench

[Posit Workbench](https://posit.co/products/enterprise/workbench/) includes support for Positron Pro. To configure and use Positron Pro on Posit Workbench, please see the [Posit Workbench Administration Guide](https://docs.posit.co/ide/server-pro/admin/positron_sessions/) and the [Positron Pro user guide](https://docs.posit.co/ide/server-pro/user/positron/getting-started/).
