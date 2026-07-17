# Get started

Set up AI assistance in Positron: configure a language model provider such as Posit AI, Anthropic, or GitHub Copilot, then use AI features in Positron, such as Posit Assistant.

To use AI in Positron, first configure a language model provider, then start using AI features such as Posit Assistant. Follow the steps below to get set up.

## Step 1: Configure a language model provider

Positron enables all providers by default and they appear in the provider list, but none are active unless you authenticate with the provider.

To connect a provider, run the command *Authentication: Configure Language Model Providers*, select the provider, and authenticate. For account requirements, authentication details, and any settings to configure first, see the [Language Model Providers](assistant-providers.llms.md) reference.

| Provider | Chat | Code Completions | Authentication |
|----|:--:|:--:|----|
| [Posit AI](assistant-providers.llms.md#posit-ai) |  |  | OAuth |
| [Amazon Bedrock](assistant-providers.llms.md#amazon-bedrock) |  |  | AWS CLI or Posit Workbench Managed Credentials |
| [Anthropic](assistant-providers.llms.md#anthropic) |  |  | API Key |
| [Microsoft Foundry](assistant-providers.llms.md#microsoft-foundry) |  |  | API Key or Workbench Managed Credentials |
| [OpenAI](assistant-providers.llms.md#openai) |  |  | API Key |
| [Snowflake Cortex](assistant-providers.llms.md#snowflake-cortex) |  |  | API Key or Workbench Managed Credentials |
| [GitHub Copilot](assistant-providers.llms.md#github-copilot) Preview |  |  | OAuth |
| [Custom Provider](assistant-providers.llms.md#custom-provider) Experimental |  |  | API Key |
| [DeepSeek](assistant-providers.llms.md#deepseek) Experimental |  |  | API Key |
| [Google Gemini](assistant-providers.llms.md#gemini-code-assist) Experimental |  |  | API Key |
| [Gemini Enterprise Agent Platform](assistant-providers.llms.md#gemini-enterprise-agent-platform) Experimental |  |  | Google Cloud CLI or Service Account Credentials |

Please ensure you consult your provider’s privacy policy for information on the data they collect and how they use it. For reference links, see the [Privacy & Terms](assistant-provider-info.llms.md) guide.

For information on what information is collected by Posit, review [Posit’s privacy policy](privacy.llms.md).

## Step 2: Use AI in Positron

With a language model provider configured, you can use AI throughout Positron. To start a chat, run the *View: Show Posit Assistant* command in the Command Palette to open the chat panel.

### Posit Assistant

Chat about your code, Console sessions, and in-memory objects.

### Code completions

Get inline code suggestions as you type in the editor or a notebook.

### All AI features

Learn more about AI features in Positron.

To control which AI features are active, or to turn them off, see [Configure AI features](ai-configuration.llms.md).
