# Chat Agents

Customize AI behavior with chat agents in Positron Assistant. Choose from Ask, Edit, Agent, and Plan modes or create custom agents for specific tasks.

> **WARNING:**
>
> This page documents Positron Assistant, the previous AI chat and completions experience, which has been deprecated and replaced by [Posit Assistant](https://assistant.posit.co) as of Positron 2026.07. These docs remain in place for folks on older builds of Positron.
>
> If you are on Positron 2026.07 or later, see the [Posit Assistant documentation](https://assistant.posit.co) to get set up with Posit Assistant. For background on this change, see [The history of Posit’s data science agents](https://opensource.posit.co/blog/2026-06-11_history-of-posit-data-science-agents).

> **NOTE:**
>
> Posit Assistant manages tool use and agent behavior through permissions. See [Permissions](https://assistant.posit.co/docs/features/permissions/) in the Posit Assistant documentation.

Chat agents tailor Assistant’s behavior for specific tasks by providing unique instructions and tools. Select the agent selector dropdown at the bottom of the chat pane to switch between agents.

You can also create [custom chat agents](#custom-chat-agents) to suit your specific workflows and requirements.

## Default chat agents

- **Ask**: Provides answers and code suggestions without automatic execution
- **Edit**: Suggests code changes for you to apply to files
- **Agent**: Autonomously executes work including running code and modifying files
- **Plan**: Creates detailed step-by-step plans before execution

View detailed descriptions and example prompts

[TABLE]

## Custom chat agents

Adding custom chat agents allows you to:

- Create specialized agents for specific tasks or workflows
- Tailor the Positron Assistant’s behavior and available tools for different use cases

### Create a custom chat agent

1.  Run the command *Chat: New Custom Agent…* and follow the prompts to create a new chat agent file.
2.  Edit the newly created `.agent.md` file to specify the chat agent `description`, the `tools` the chat agent can use, as well as the chat agent prompt content.
3.  Once you have created a custom chat agent, it will be available in the agent selector dropdown in the chat pane.

> **NOTE:**
>
> To learn more about the format of custom agents, see the following VS Code documentation:
>
> - [Custom agent file structure](https://code.visualstudio.com/docs/copilot/customization/custom-agents#_custom-agent-file-structure)
> - [Custom agents in VS Code](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
>
> Positron Assistant does not support the `model` field.

Example custom chat agent

Below is a custom chat agent tailored to debugging R and Python code. The definition contains rules, direction, and clarification that the agent follows when invoked. These guide its responses to be more relevant to troubleshooting and fixing code issues.

``` code-overflow-wrap
---
description: Debug and troubleshoot issues in R or Python code.
name: Code Debugger
tools: ['search', 'edit', 'executeCode', 'inspectVariables', 'runCommands', 'runTasks']
handoffs:
  - label: Test Code
    agent: agent
    prompt: Run the code to verify the fix works correctly.
    send: false
---
# R/Python Debugging Specialist

You are a debugging expert for R and Python. Your role is to identify, diagnose, and fix issues in code.

## Your debugging expertise includes:

* **Logic Errors**: Identify incorrect algorithms, off-by-one errors, and faulty conditional logic
* **Runtime Errors**: Diagnose exceptions, type errors, and null/missing value issues
* **Data Issues**: Detect problems with data types, shapes, and unexpected values

## Debugging workflow:

1. Ask the user to describe the problem, error messages, and expected behavior
2. Review relevant code sections and identify potential issues
3. Use available tools to inspect variables and test code snippets
4. Explain the root cause and suggest specific code changes
5. Edit the code directly with the proposed solution

## Common issues you solve:

- Index out of bounds errors
- Type mismatches and conversion errors
- Incorrect function arguments or return values
- Logic errors producing unexpected results

## Rules

- Always explain the root cause before proposing a fix.
- Edit files directly rather than just providing code snippets.
- Use `executeCode` to test fixes when appropriate.
```

**`tools`**: The agent is restricted to tools relating to debugging functionality, limiting the number of “decisions” Positron Assistant must make while working. For example, you can grant a data analysis agent access to the `getPlot` tool to inspect the plot output in Positron, whereas a debugging agent focuses on code inspection and execution tools.

**`handoffs`**: This agent provides a handoff, which gives users a way to trigger a subsequent action with one click. A user will naturally want to test code after it is fixed, so this handoff presents the user with a button titled “Test Code” which instructs Assistant to run the code and verify the fix. An agent can provide as few or many handoffs as makes sense for its use case.
