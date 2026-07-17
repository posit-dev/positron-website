# Custom Instructions

Tailor Positron Assistant to your project with custom instructions. Set up workspace-specific AI behavior and coding preferences automatically.

> **WARNING:**
>
> This page documents Positron Assistant, the previous AI chat and completions experience, which has been deprecated and replaced by [Posit Assistant](https://assistant.posit.co) as of Positron 2026.07. These docs remain in place for folks on older builds of Positron.
>
> If you are on Positron 2026.07 or later, see the [Posit Assistant documentation](https://assistant.posit.co) to get set up with Posit Assistant. For background on this change, see [The history of Posit’s data science agents](https://opensource.posit.co/blog/2026-06-11_history-of-posit-data-science-agents).

> **NOTE:**
>
> Posit Assistant includes a built-in skill, `/import-instructions`, that migrates Positron, Copilot, Claude Code, and VS Code instruction files into Posit Assistant skills. Run it to bring the instructions described on this page over to Posit Assistant.

Positron Assistant supports both **automatic workspace instructions** and **custom instructions files** to tailor AI behavior to your project’s needs.

Custom instructions do not apply to code completions.

## Automatic workspace instructions

Add project-wide custom instructions by creating one or more of these files in your workspace root directory:

- `agent.md`
- `agents.md`
- `positron.md`
- `claude.md`
- `gemini.md`
- `llms.txt`

Positron Assistant automatically appends the content from these files to all chat interactions. This allows you to:

- Add project-specific coding standards or conventions
- Include domain-specific terminology or context
- Define preferred libraries or frameworks for your project

Note that Positron Assistant does not guarantee the order in which it appends these files. Follow issue [\#10571](https://github.com/posit-dev/positron/issues/10571) for updates.

## Custom instructions files

Create `.instructions.md` files that specify [glob patterns](https://code.visualstudio.com/docs/editor/glob-patterns) for when the instructions should apply.

Positron Assistant automatically uses these instructions when you work with files that match the specified patterns. This allows you to:

- Enforce coding standards for specific file types (e.g., `*.py` for Python scripts)
- Provide context-specific guidelines for different parts of your project (e.g., `src/data/**/*` for data processing scripts)
- Apply instructions workspace-wide using broad patterns (e.g., `**/*` for all files)

### Creating and managing custom instructions files

1.  Run the command *Chat: New Instructions File…* and follow the prompts to create a new instructions file
2.  Edit the newly created `.instructions.md` file to specify the `applyTo` file glob pattern and the instructions you want to apply
3.  To manage existing files, run the command *Chat: Configure Instructions…*

> **NOTE:**
>
> To learn more about the format of custom instructions files, see the following VS Code documentation:
>
> - [Instructions file format](https://code.visualstudio.com/docs/copilot/customization/custom-instructions#_instructions-file-format)
> - [Tips for defining custom instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions#_tips-for-defining-custom-instructions)

Example custom instructions

This example demonstrates how a `quarto.instructions.md` file shapes Positron Assistant behavior when working with Quarto documentation files. The filename was chosen to reflect the purpose of these instructions, but can be anything ending with `.instructions.md`.

By automatically applying these rules to all `.qmd` files, Assistant writes in a consistent style that prioritizes clarity, brevity, and accessibility. The instructions guide Assistant to use active voice, avoid technical jargon, maintain proper formatting conventions, and produce content suitable for screen readers and translation tools. This keeps content aligned with your project’s standards without repeating these preferences in every chat request.

``` code-overflow-wrap
---
name: "Quarto Documentation Standards"
description: "Writing guidelines for Quarto documentation following Positron style guide"
applyTo: "**/*.qmd"
---

# Quarto Documentation Guidelines

## Writing and Style

- Write at approximately 12th grade reading level with sentences of 28-30 words or fewer
- Use present tense and active voice; avoid contractions and gerunds as nouns
- Use the Oxford comma and spell out acronyms on first use
- Maintain an energetic, compassionate tone that is simple and direct
- Use clear, literal language suitable for screen readers and translation tools; avoid idioms and metaphors
- Do not use possessives with product names

## Formatting

- Use Title Case for titles/H1s; sentence case for other headings
- Always include `title` and `description` in YAML front matter
- Bold UI elements, italicize commands, use backticks for code
- Use the Quarto `kbd` shortcode for keyboard shortcuts: `{{< kbd mac=Command-Shift-P win=Ctrl-Shift-P linux=Ctrl-Shift-P >}}`
- Link to settings: `[positron://settings/category.nameOfSetting](positron://settings/category.nameOfSetting)`
- Use em dashes (—) for emphasis; en dashes (–) for ranges
```
