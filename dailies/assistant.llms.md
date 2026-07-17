# Posit Assistant

Posit Assistant is an AI coding assistant for data science in Positron, bringing together the capabilities of Positron Assistant and Databot in a unified experience.

[Posit Assistant](https://assistant.posit.co) is an AI coding assistant for data science in Positron. It first became available as a preview feature in Positron 2026.04.0, and as of Positron 2026.07 it ships with Positron as the default AI experience, replacing Positron Assistant and Databot. For more on how it came to be, see [The history of Posit’s data science agents](https://opensource.posit.co/blog/2026-06-11_history-of-posit-data-science-agents).

Beyond your active files, selected code, and project structure, Posit Assistant uses context from your interactive data science work, such as your loaded data, plots, and console history. This enables more relevant guidance for core data science workflows, including exploratory analysis, data cleaning, data app development, and modeling.

To learn how to enable it and get set up, visit the [Get Started guide](assistant-getting-started.llms.md).

## Features

Posit Assistant has a rich set of features with the highlights listed below.

| Feature | Summary |
|----|----|
| [Commands](https://assistant.posit.co/docs/features/commands/) | Slash commands typed at the start of a message that trigger special actions, such as `/plan`, `/new`, and `/savememory`. |
| [Skills](https://assistant.posit.co/docs/features/skills/) | Specialized knowledge modules that load automatically when relevant to a request, with no manual activation needed. Built-ins include `quarto-authoring`, `shiny-bslib`, and `predictive-modeling-r`, plus user and project-level custom skills. |
| [Memory](https://assistant.posit.co/docs/features/memory/) | Persistent project context via an `AGENTS.md` file that captures conventions, architecture, and preferences. The file loads automatically at the start of every conversation in trusted workspaces. |
| [Conversations](https://assistant.posit.co/docs/features/conversations/) | Full conversation history with switching, renaming, and deletion. Includes tree-based branching when you edit a previous message and import and export in Markdown, HTML, or JSON. |
| [Plan Mode](https://assistant.posit.co/docs/features/plan-mode/) | A collaborative design phase where the assistant explores the codebase, asks questions, and writes a plan file before changing code. Best for multi-step features, refactors, and unfamiliar codebases. |
| [Chat Features](https://assistant.posit.co/docs/features/chat-features/) | File attachments via drag-and-drop, clipboard paste, or the paperclip, with `@` mentions to reference workspace files. Also includes adjustable thinking effort (Off, Low, Medium, and High) and optional web search. |
| [Context Management](https://assistant.posit.co/docs/features/context-management/) | Automatic inclusion of session info (language, version, variable names and types) when connected to R or Python. Provides a token counter with detailed breakdown and auto, manual, and micro-compaction to keep long conversations within the model’s context window. |
| [Permissions & Trust](https://assistant.posit.co/docs/features/permissions/) | Three approval modes (Normal, YOLO, Restricted) and per-tool permissions configurable in settings. Includes workspace trust prompts when opening projects with `AGENTS.md` and an optional sandbox mode for bash execution. |

For the full Posit Assistant configuration guide and feature documentation, see the [Posit Assistant documentation](https://assistant.posit.co/docs/getting-started/).

## Learn more

### Get Started

Configure a language model provider and start using Posit Assistant in Positron.

### Posit Assistant vs. Positron Assistant

Watch a walkthrough comparing Posit Assistant and Positron Assistant.

### AI at Posit

Explore Posit's broader work on artificial intelligence for data science.

## Support and terms of service

Posit does not provide support or assistance for any code written or generated in Positron, with or without AI features in Positron such as Posit Assistant, Positron Assistant, or Databot, regardless of which model provider you use. Posit does not support any model provider’s output or test the logic a provider uses to generate code from prompts. Consult your AI model provider’s [documentation](assistant-provider-info.llms.md) for more information.

### BYO-key model providers

AI features in Positron use a bring-your-own-key (BYO-key) model. You connect to a range of different model providers, such as Anthropic, Amazon Bedrock, GitHub Copilot, or OpenAI. You or your organization has an agreement with the provider and pays them directly for access to the model.

### Data collection and privacy

Positron provides local software as a client to your selected model provider. As a result, Posit does not track, collect, or store your prompts, code, or conversations when you use AI features within Positron (i.e., Posit Assistant, Positron Assistant, Databot, etc.). This applies as long as you use an external model provider. These features operate by communicating directly from your client software to your chosen AI model provider. Posit does not receive any AI traffic from your client’s software and nor does Posit ever access or store your data. If you select [Posit AI](assistant-provider-info.llms.md#posit-ai) as your model provider, the [privacy policy](privacy.llms.md) and [Posit AI Agreement](https://posit.co/about/posit-ai-agreement) apply instead.

If you voluntarily share diagnostic logs or information with Posit for troubleshooting purposes, that shared information will be handled in accordance with [Posit’s privacy policy](privacy.llms.md).

However, your AI model provider may store or collect data according to their own privacy policies and terms of service. Please review your [AI model provider’s data practices](assistant-provider-info.llms.md) for details on what information they collect and how it is used.

By using an external model provider, you acknowledge that your use is subject to their Terms of Service. All external model providers are considered “Third Party Materials” as defined in the [Posit End User License Agreement](https://posit.co/about/eula/) and Posit assumes no liability or other obligations with respect thereto and, without limiting the foregoing, is not liable for any loss or damage resulting from the use or access thereof.
