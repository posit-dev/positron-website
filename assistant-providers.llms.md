# Providers

Account requirements, authentication, and settings for each language model provider you can use with Posit Assistant.

Positron connects to a range of language model providers. To connect one, run the command *Authentication: Configure Language Model Providers*, select the provider, and authenticate.

This page covers what each provider needs: the account to have ready, how you authenticate, and any Positron settings to configure first.

Please ensure you consult your provider’s privacy policy and terms of service for information on the data they collect and how it is used. For reference links, see the [Privacy & Terms](assistant-provider-info.llms.md) guide.

## Posit AI

Posit AI is a hosted language model service from Posit, offering both chat models and code completions through [Next Edit Suggestions (NES)](assistant-completions.llms.md#posit-ai-nes).

- **Account:** a Posit AI account, which you can create at [posit.ai](https://posit.ai/)
- **Authentication:** sign in through your browser with OAuth

## Amazon Bedrock

- **Account:** an AWS account with Amazon Bedrock access, plus [access to the foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access-modify.llms.md) you want to use
- **Authentication:** sign in to your AWS account with the AWS CLI. Positron checks that you are signed in
- **Settings:**
  - [`authentication.aws.credentials`](positron://settings/authentication.aws.credentials) (optional): override `AWS_REGION` or `AWS_PROFILE` for Positron only (see below)
  - [`authentication.aws.inferenceProfileRegion`](positron://settings/authentication.aws.inferenceProfileRegion) (optional): override the derived cross-region inference profile (`us`, `eu`, `apac`, or `global`) (see below)

### Sign in with the AWS CLI

1.  [Download and install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.llms.md)
2.  [Configure your AWS credentials for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.llms.md)
3.  [Sign in with the AWS CLI](https://docs.aws.amazon.com/signin/latest/userguide/command-line-sign-in.llms.md)

### Configure AWS region and profile (optional)

Positron reads `AWS_REGION` from your environment and uses your `default` AWS CLI profile automatically, so most people can skip this.

#### `AWS_REGION`

Set this if your shell does not already have a region configured and your Bedrock-enabled account is not in `us-east-1` (the default). Use the standard AWS region identifier (for example, `us-east-1`, `eu-west-1`, `ap-southeast-1`). The [Amazon Bedrock endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/bedrock.llms.md) reference lists the identifier for each location. Make sure the models you want are [available in that region](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.llms.md).

#### `AWS_PROFILE`

Set this if the profile you use for Bedrock is not named `default`, for example when you have a dedicated Bedrock role separate from your development credentials, or your Bedrock access lives in a different AWS account. Run `aws configure list-profiles` in a terminal to see your profiles.

To set either value, add it to the [`authentication.aws.credentials`](positron://settings/authentication.aws.credentials) setting as an item keyed by `AWS_REGION` or `AWS_PROFILE`. These override any matching environment variables for Positron only. They do not affect your terminal or other tools. Changes require a restart to take effect.

> **NOTE:**
>
> Do not set `AWS_PROFILE` if you use Posit Workbench managed credentials or environment variable credentials (`AWS_ACCESS_KEY_ID`/`AWS_SECRET_ACCESS_KEY`). Both of those paths bypass named profile resolution, so setting a profile name causes credential resolution to fail.

### Configure inference profile region (optional)

Positron uses [cross-region inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.llms.md) to route requests across multiple AWS regions for higher availability and throughput. Positron derives the inference profile region automatically from `AWS_REGION` by taking its geographic prefix:

| `AWS_REGION`                       | Derived inference profile region |
|------------------------------------|----------------------------------|
| `us-east-1`, `us-west-2`           | `us`                             |
| `eu-west-1`, `eu-central-1`        | `eu`                             |
| `ap-southeast-1`, `ap-northeast-1` | `apac`                           |

Most users do not need to change this. Use the [`authentication.aws.inferenceProfileRegion`](positron://settings/authentication.aws.inferenceProfileRegion) setting to override the derived value if:

- Your AWS account has Bedrock model access in a different geographic pool than your `AWS_REGION` implies. For example, you connect through `us-east-1` but want to route inference through `eu` profiles.
- You want a `global` inference profile, which Positron cannot derive automatically from any region.

Valid values are `us`, `eu`, `apac`, and `global`. This setting requires a restart to take effect.

If no inference profile exists for your preferred region, Positron falls back to the first available inference profile for that model. If a model has no inference profile at all, it does not appear in the model list.

## Anthropic

- **Account:** a [Claude Console](https://support.claude.com/en/collections/5370014-claude-api-and-console) account with API access (Claude Pro, Max, and other subscription plans do not work)
- **Authentication:** an Anthropic API key, or the `ANTHROPIC_API_KEY` environment variable

### Get an Anthropic API key

To use the Claude models from Anthropic in Positron, you bring your own API key (BYOK). To obtain an API key from Anthropic:

1.  Log in to or create an account for Anthropic’s [Claude Console](https://platform.claude.com).
2.  Navigate to the [API keys](https://platform.claude.com/settings/keys) management page.
3.  Select the **Create Key** button.
4.  Fill out any required information and select **Add** to generate your API key.
5.  Copy and save the API key to a password manager or another secure location.

### Why a Claude Pro or Max subscription does not work

Anthropic does not include Claude API usage in its [Pro](https://support.claude.com/en/articles/8325606-what-is-the-pro-plan) and Max subscription plans, so signing in to Claude with OAuth does not grant access to the API that Posit Assistant needs. To use Claude with Posit Assistant, you need [Claude Console access](https://support.claude.com/en/articles/8114521-how-can-i-access-the-claude-api) and an API key, billed separately from any subscription.

Support for OAuth sign-in depends on Anthropic offering API access to Posit Assistant through these plans. You can follow [this feature request](https://github.com/posit-dev/positron/issues/9481) for updates.

## Microsoft Foundry

- **Account:** a [Microsoft Foundry](https://ai.azure.com/) resource with one or more models deployed
- **Authentication:** the endpoint URL and API key for your Foundry resource
- **Settings:**
  - [`positron.assistant.models.overrides.msFoundry`](positron://settings/positron.assistant.models.overrides.msFoundry) (optional): Foundry has no automatic model discovery and defaults to `model-router`, so set this to use specific models (see below)

Positron accepts deployment-based Azure OpenAI URLs (for example, `https://<resource>.openai.azure.com/openai/deployments/<name>/chat/completions?api-version=...`) and automatically normalizes them to the supported v1 format. A message displays when this conversion occurs.

### Configure a custom model listing

To use specific models instead of `model-router`, configure the [`positron.assistant.models.overrides.msFoundry`](positron://settings/positron.assistant.models.overrides.msFoundry) setting:

``` json
"positron.assistant.models.overrides.msFoundry": [
  {
    "name": "gpt-4.1",
    "identifier": "gpt-4.1"
  },
  {
    "name": "gpt-5.3-chat",
    "identifier": "gpt-5.3-chat"
  }
]
```

Use the model name and deployment identifier from your Foundry resource for each entry.

## OpenAI

- **Account:** an OpenAI account, or any service that implements the [OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)
- **Authentication:** an OpenAI API key, or the `OPENAI_API_KEY` environment variable. For a compatible service, also provide its base URL (or the `OPENAI_BASE_URL` environment variable)

## Snowflake Cortex

- **Account:** a Snowflake account with Cortex access
- **Authentication:** your Snowflake [account identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier) and a [programmatic access token](https://docs.snowflake.com/en/user-guide/programmatic-access-tokens) (PAT)
- **Settings:**
  - [`authentication.snowflake.credentials`](positron://settings/authentication.snowflake.credentials) (required): add your account ID as an item with the key `SNOWFLAKE_ACCOUNT` before you connect

## GitHub Copilot Preview

- **Account:** a GitHub account with Copilot enabled
- **Authentication:** sign in through your browser with OAuth

To sign in, use the *Authentication: Configure Language Model Providers* command, select GitHub Copilot, and sign in. If you already have a GitHub session from another extension, this asks you to confirm reusing it for Assistant. Otherwise, it starts a new browser sign-in flow.

To sign out, use the **Accounts** icon or run the *Accounts: Manage Accounts* command. Unlike signing in, this signs you out for all features in Positron that use your GitHub account, such as the Git or GitHub Pull Requests extensions.

> **NOTE:**
>
> Signing in to GitHub through the **Accounts** menu in the Activity Bar does not sign you in to GitHub Copilot for AI features. This applies even when you use the Accounts menu for other extensions, such as Git or GitHub Pull Requests.

### Get GitHub Copilot access

GitHub Copilot is a proprietary tool from GitHub. To use GitHub Copilot for AI chat and code completions, you need a [subscription for GitHub Copilot](https://docs.github.com/en/billing/managing-billing-for-github-copilot/about-billing-for-github-copilot) in your personal GitHub account. You can also be assigned a seat by an organization with a GitHub Copilot for Business subscription.

Students and faculty can use GitHub Copilot for free as part of the GitHub Education program. For more information, see the [GitHub Education page](https://education.github.com/).

### Sign in with GitHub Copilot Enterprise

GitHub Copilot Enterprise runs on GHE.com (GitHub Enterprise Cloud), not github.com. Signing in requires two extra settings compared to a personal subscription.

Before you start, make sure your organization administrator has enabled GitHub Copilot for your enterprise and assigned you a Copilot seat.

1.  Open the [`github-enterprise.uri`](positron://settings/github-enterprise.uri) setting and enter your enterprise URL, for example `https://octocorp.ghe.com`.

2.  Run the command *Preferences: Open User Settings (JSON)* to open your `settings.json` directly. Add the `authProvider` key inside `github.copilot.advanced`:

    ``` json
    "github.copilot.advanced": {
      "authProvider": "github-enterprise"
    }
    ```

    This setting will be indicated as an **Unknown Configuration Setting**. This is expected and you can ignore the warning.

3.  Save the file. A prompt will appear asking you to sign in to GitHub. Click it and complete the browser authorization flow. If no prompt appears, restart Positron.

For more detail, see GitHub’s guide on [authenticating to GitHub Copilot on GHE.com](https://docs.github.com/en/copilot/how-tos/configure-personal-settings/authenticate-to-ghecom).

## Custom Provider Experimental

The custom provider works with any [OpenAI-compatible](https://ai-sdk.dev/providers/openai-compatible-providers) API endpoint that uses the `/v1/chat/completions` endpoint for chat. We do not recommend using a local model as a custom provider. Read more about why [local models are not there (yet)](https://posit.co/blog/local-models-are-not-there-yet/) on the Posit blog.

- **Account:** an account with your chosen OpenAI-compatible provider
- **Authentication:** an API key and the provider’s base URL
- **Settings:**
  - [`positron.assistant.models.overrides.customProvider`](positron://settings/positron.assistant.models.overrides.customProvider) (optional): list models if your provider does not implement the `/models` endpoint (see below)

### Configure a custom model listing

Some OpenAI-compatible providers might not implement the `/models` endpoint, which Positron uses to list available models. If this is the case for your provider, configure a custom model listing using the [`positron.assistant.models.overrides.customProvider`](positron://settings/positron.assistant.models.overrides.customProvider) setting:

``` json
"positron.assistant.models.overrides.customProvider": [
  {
    "name": "Claude Sonnet 4.5 via OpenRouter",
    "identifier": "anthropic/claude-sonnet-4.5"
  }
]
```

## DeepSeek Experimental

- **Account:** a [DeepSeek](https://platform.deepseek.com/) account with API access
- **Authentication:** a DeepSeek API key, or the `DEEPSEEK_API_KEY` environment variable

## Google Gemini Experimental

- **Account:** a Google account with access to the [Gemini API](https://ai.google.dev/), with an API key created in [Google AI Studio](https://aistudio.google.com/apikey)
- **Authentication:** a Gemini API key, or the `GEMINI_API_KEY` or `GOOGLE_API_KEY` environment variable

## Gemini Enterprise Agent Platform Experimental

Formerly Google Vertex AI.

- **Account:** a Google Cloud project with the [Agent Platform APIs enabled](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/cloud-environment) and [access to the models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models) you want to use
- **Authentication:** authenticate with Google Cloud using Application Default Credentials (`gcloud`) or a service account (see below)
- **Settings:**
  - [`authentication.googleVertex.credentials`](positron://settings/authentication.googleVertex.credentials) (required, or env vars): set your project ID and location, which take precedence over the `GOOGLE_VERTEX_PROJECT` and `GOOGLE_VERTEX_LOCATION` environment variables

### Sign in with Application Default Credentials (ADC)

1.  [Install the Google Cloud CLI (`gcloud`)](https://cloud.google.com/sdk/docs/install)
2.  Run `gcloud auth application-default login` and complete the browser sign-in flow

### Sign in with a service account

Set the following environment variables before launching Positron:

- `GOOGLE_CLIENT_EMAIL`: the service account’s client email
- `GOOGLE_PRIVATE_KEY`: the service account’s private key
