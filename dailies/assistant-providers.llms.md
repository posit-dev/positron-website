# Providers

Connect Positron to a language model provider and manage your provider settings.

To connect a language model provider, run the command *Posit Assistant: Configure AI Providers* or select **Configure Language Model Providers** from the **Accounts** menu, then select **Connect** next to the provider.

For what each provider needs and how to sign in, see [Providers](https://assistant.posit.co/docs/getting-started/providers/) in the Posit Assistant documentation.

| Provider | Chat | Code Completions |
|----|:--:|:--:|
| Posit AI Pass |  |  |
| Amazon Bedrock |  |  |
| Anthropic |  |  |
| Databricks Preview |  |  |
| DeepSeek |  |  |
| GitHub Copilot Preview |  |  |
| Google Gemini |  |  |
| Google Vertex AI (Gemini Enterprise Agent Platform) Preview |  |  |
| LiteLLM Preview |  |  |
| LM Studio (local) |  |  |
| Microsoft Foundry |  |  |
| Ollama (local) |  |  |
| OpenAI |  |  |
| OpenAI Compatible (legacy) |  |  |
| OpenCode Preview |  |  |
| OpenRouter (use a custom provider) |  |  |
| Portkey Preview |  |  |
| Snowflake Cortex |  |  |

If your provider is not listed, add a [custom provider](https://assistant.posit.co/docs/getting-started/providers/#custom-providers). It can use any of the provider types above, so you can connect a company gateway, a second account on the same provider, or a local model server.

## `providers.json`

Posit Assistant saves your provider settings, but not your keys or tokens, to `~/.posit/ai/providers.json`. Some changes are not on the **AI Providers** screen, such as turning a provider off, sending custom HTTP headers, or filtering the model list. For those, run *Open AI Provider Settings (JSON)*. For every key the file accepts, see the [`providers.json` reference](https://assistant.posit.co/docs/reference/providers-config/).

> **NOTE:**
>
> Positron 2026.10 removed the `authentication.*`, `positron.assistant.provider.*`, and `positron.assistant.models.overrides.*` settings. If they are still in your `settings.json`, Positron moves them to `providers.json` on startup. To run this again, use *Migrate AI Provider Settings to providers.json*.
