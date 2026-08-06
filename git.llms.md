# Git Version Control

Track changes, collaborate on code, and manage project history with built-in Git integration in Positron.

Git is a powerful version control system that helps you track changes to your code, collaborate with others, and maintain a history of your project. Positron provides built-in Git integration that works seamlessly with Git repositories.

## What is Git?

Git is a distributed version control system that tracks changes in your files over time. It allows you to:

- Keep a complete history of your project
- Work on different features simultaneously using branches  
- Collaborate with others on the same codebase
- Revert to previous versions when needed
- Merge changes from different contributors

## Getting started with Git

### Set up Git in Positron

Before you can use Git in Positron, you need to have Git installed on your computer. If Git is not installed, the Source Control view will show instructions on how to install it.

**Learn more:** [Set up Git in VS Code](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git#_set-up-git-in-vs-code)

### Open a Git repository

Positron provides a few ways to work with Git repositories:

- **Open Folder** to open an existing Git repository that you already have locally
- **New Folder from Template** to create a new folder locally, with the option to initialize it as a Git repository
- **New Folder from Git** to clone an existing Git repository from a remote source like GitHub

These options are available from the Welcome screen when you are not already in a folder/workspace, or you can access them later through the Command Palette by searching for *Workspaces: New Folder from Git…* or *Workspaces: New Folder from Template…*.

### Initialize Git in an existing project

If you are working with an existing project that does not use Git, you can also initialize a Git repository within Positron:

1.  Open your project folder in Positron
2.  Open the Source Control view from the Activity Bar
3.  Select **Initialize Repository** to create a new Git repository in your current folder

This creates a `.git` folder in your project directory and begins tracking your files.

> **NOTE:**
>
> If you are a more advanced Git user, consider installing the [GitLens extension](https://open-vsx.org/vscode/item?itemName=eamodio.gitlens) for extended Git capabilities in Positron.

## Basic Git workflow

### Staging and committing changes

The basic Git workflow involves making changes to your files, then staging and committing those changes:

1.  **Make changes** to your files in Positron
2.  **Stage changes** by selecting which files to include in your next commit
3.  **Commit changes** with a descriptive message about what you changed
4.  **Push changes** to share them with others, when you have setup a remote repository like GitHub or GitLab

The Source Control view in Positron shows all your changed files and makes it easy to stage and commit changes with a few clicks.

**Learn more:** [Staging and committing code changes](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git#_staging-and-committing-code-changes)

### Generate commit messages with AI

If you are signed in to a [language model provider](assistant-getting-started.llms.md), Positron can draft a commit message from your changes. Stage the changes you want included (Positron uses all changes if nothing is staged), then select the sparkle icon in the commit message box in the Source Control view.

To disable AI commit message generation, set [`git.suggestions.enabled`](positron://settings/git.suggestions.enabled) to `false`. See [Configure AI features](ai-configuration.llms.md) for other ways to turn AI features on and off.

By default, Positron uses a fast, low-cost model to generate commit messages. To pick a different one, run *Git: Select Git Suggestions Model* from the Command Palette, or set [`git.suggestions.model`](positron://settings/git.suggestions.model) to a list of patterns to try in order, e.g., `["haiku", "flash"]`.

If both GitHub Copilot and Positron AI features are enabled, each adds its own button to the commit message box. Use the dropdown to choose which one to use.

### Syncing with remote repositories

When working with a remote repository like GitHub, you can sync changes between your local and remote repositories:

- **Push** your local commits to the remote repository
- **Pull** changes from the remote repository to your local copy
- **Sync** to both push and pull changes at once

**Learn more:** [Pushing and pulling remote changes](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git#_pushing-and-pulling-remote-changes)

## Working with branches

Branches allow you to work on different features or experiments without affecting your main line of development:

- **Create branches** for new features or bug fixes
- **Switch between branches** to focus on different development efforts within your project
- **Create pull requests** to propose changes and solicit feedback from colleagues or continuous integration services
- **Merge branches** to incorporate changes into the main branch

**Learn more:** [Using branches](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git#_using-branches)

## Handling merge conflicts

Merge conflicts occur when Git cannot automatically combine changes from different branches. When this happens, Positron displays conflicted files in the Source Control view with a warning icon.

Positron provides a 3-way merge editor to help you resolve conflicts by choosing which changes to accept. You can also resolve conflicts manually by editing the file directly and removing the conflict markers.

**Learn more:** [Merge conflicts in VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview#_merge-conflicts)

## Integration with Git platforms

Positron includes the [GitHub](https://open-vsx.org/extension/vscode/github) and [GitHub Pull Requests and Issues](https://open-vsx.org/extension/GitHub/vscode-pull-request-github) extensions out of the box, which let you manage GitHub repositories, issues, and PRs directly from within Positron. You can learn more about the extensions that Positron automatically installs for you on the [Extensions](extensions.llms.md#bootstrapped-extensions) page.

Other platforms are not integrated by default, but similar features are available after installing extensions like [GitLab Workflow](https://open-vsx.org/extension/GitLab/gitlab-workflow) or [Atlassian: Jira & Bitbucket](https://open-vsx.org/extension/atlassian/atlascode). You can search in the [Extensions pane](extensions.llms.md#accessing-extensions) to find other extensions for the Git platform you use.

## Additional resources

- [Introduction to Git in VS Code](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git): Comprehensive guide with screenshots and examples
- [Git Documentation](https://git-scm.com/doc): Official Git documentation
- [GitHub Docs](https://guides.github.com/): Learn GitHub-specific features
- [Learn Git Branching](https://learngitbranching.js.org/): Visual and interactive way to learn Git
- [Happy Git and GitHub for the useR](https://happygitwithr.com/): A guide for R users to learn Git and GitHub
