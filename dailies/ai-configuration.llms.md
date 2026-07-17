# Configure AI features

Configure the AI features in Positron, including turning individual features or all AI features on or off.

Once you have [set up a language model provider](assistant-getting-started.llms.md), you can configure how AI features behave in Positron.

## Turn features on or off

You can turn off individual features or disable all AI features at once.

### Turn off all AI features

To turn off all Positron AI features at once, set [`ai.enabled`](positron://settings/ai.enabled) to `false`. This overrides individual feature settings and disables:

- Posit Assistant
- Posit AI Next Edit Suggestions (NES)
- Notebook AI features
- Console Fix & Explain
- Quarto Fix & Explain
- GitHub Copilot (Chat, Completions)
- Git commit message generation

### Turn off a specific feature

To disable a specific feature without affecting others:

| Setting | Features affected |
|----|----|
| [`assistant.enabled`](positron://settings/assistant.enabled) | [Posit Assistant](https://assistant.posit.co) (set to `false` to disable) |
| [`nextEditSuggestions.enabled`](positron://settings/nextEditSuggestions.enabled) | [Posit AI NES](assistant-completions.llms.md#posit-ai-nes) (set to `{ "*": false }` to disable) |
| [`github.copilot.enable`](positron://settings/github.copilot.enable) | [GitHub Copilot Code Completions](assistant-completions.llms.md#github-copilot) (set to `{ "*": false }` to disable) |
| [`notebook.ai.enabled`](positron://settings/notebook.ai.enabled) | [Notebook AI features](positron-notebook-editor.llms.md#ai-integration) (set to `false` to disable) |
| [`console.assistantActions.enabled`](positron://settings/console.assistantActions.enabled) | [Console Fix & Explain](managing-interpreters.llms.md#console-fix-and-explain) (set to `false` to disable) |
| [`git.suggestions.enabled`](positron://settings/git.suggestions.enabled) | [Git commit messages](git.llms.md#generate-commit-messages) (set to `false` to disable) |
