# Privacy & terms

Data handling, privacy, and terms of service for AI model providers used for AI features in Positron.

> **NOTE:**
>
> For information on what information is collected by Posit, review [Posit’s privacy policy](privacy.llms.md).

When you use AI features in Positron, Positron might share data including your prompts, responses, and usage with third-party AI model providers, depending on the providers you use. Each provider has its own data handling, privacy policies, and terms of service.

Please review your providers’ websites directly for complete and updated details on their data practices and terms of service. This list might not be up to date.

## Providers

### Posit AI

Posit AI is Posit’s own hosted service, so Posit’s own policies apply rather than a third party’s.

- [Privacy Policy](https://posit.co/about/privacy-policy/)
- [Posit AI Agreement](https://posit.co/about/posit-ai-agreement)

### Amazon Bedrock

- [Privacy Notice](https://aws.amazon.com/privacy/)
- [Terms of Service](https://aws.amazon.com/service-terms/)

### Anthropic

- [Privacy Policy](https://www.anthropic.com/legal/privacy)
- [Commercial Privacy Center](https://privacy.claude.com/en/collections/10663361-commercial-customers)
- [Console Privacy Controls](https://platform.claude.com/settings/privacy)
- [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms)

### DeepSeek

- [Privacy Policy](https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.llms.md)
- [Terms of Use](https://cdn.deepseek.com/policies/en-US/deepseek-terms-of-use.llms.md)
- [Open Platform Terms of Service](https://cdn.deepseek.com/policies/en-US/deepseek-open-platform-terms-of-service.llms.md)

### Gemini Enterprise Agent Platform

- [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice)
- [Google Cloud Platform Terms of Service](https://cloud.google.com/terms)
- [Gemini Enterprise Agent Platform and zero data retention](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention)

### GitHub Copilot

- [Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement#personal-data-we-collect)
- [Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products-and-features#github-copilot)

### Google Gemini

- [Privacy Policy](https://policies.google.com/privacy)
- [Google APIs Terms of Service](https://developers.google.com/terms)
- [Gemini API Additional Terms of Service](https://ai.google.dev/gemini-api/terms)

### Microsoft Foundry

- [Microsoft Privacy Statement](https://privacy.microsoft.com/en-us/privacystatement)
- [Azure AI Services Terms](https://www.microsoft.com/licensing/terms/productoffering/MicrosoftAzure)

### OpenAI

- [Privacy Policy](https://openai.com/policies/row-privacy-policy/)
- [Privacy Portal](https://privacy.openai.com/policies/en/?name=welcome-to-open-ai-privacy-portal)
- [Terms of Use](https://openai.com/policies/row-terms-of-use/)

### Snowflake Cortex

- [Privacy Policy](https://www.snowflake.com/en/legal/privacy/privacy-policy/)
- [Terms of Service](https://www.snowflake.com/en/legal/terms-of-service/)

### Custom Provider

The custom provider connects to any OpenAI-compatible endpoint you configure, so its data handling and terms depend entirely on the provider you choose. Review that provider’s own privacy policy and terms of service directly.

## Support and terms of service

Posit does not provide support or assistance for any code written or generated in Positron, with or without AI features in Positron such as Posit Assistant, Positron Assistant, or Databot, regardless of which model provider you use. Posit does not support any model provider’s output or test the logic a provider uses to generate code from prompts. Consult your AI model provider’s [documentation](assistant-provider-info.llms.md) for more information.

### BYO-key model providers

AI features in Positron use a bring-your-own-key (BYO-key) model. You connect to a range of different model providers, such as Anthropic, Amazon Bedrock, GitHub Copilot, or OpenAI. You or your organization has an agreement with the provider and pays them directly for access to the model.

### Data collection and privacy

Positron provides local software as a client to your selected model provider. As a result, Posit does not track, collect, or store your prompts, code, or conversations when you use AI features within Positron (i.e., Posit Assistant, Positron Assistant, Databot, etc.). This applies as long as you use an external model provider. These features operate by communicating directly from your client software to your chosen AI model provider. Posit does not receive any AI traffic from your client’s software and nor does Posit ever access or store your data. If you select [Posit AI](assistant-provider-info.llms.md#posit-ai) as your model provider, the [privacy policy](privacy.llms.md) and [Posit AI Agreement](https://posit.co/about/posit-ai-agreement) apply instead.

If you voluntarily share diagnostic logs or information with Posit for troubleshooting purposes, that shared information will be handled in accordance with [Posit’s privacy policy](privacy.llms.md).

However, your AI model provider may store or collect data according to their own privacy policies and terms of service. Please review your [AI model provider’s data practices](assistant-provider-info.llms.md) for details on what information they collect and how it is used.

By using an external model provider, you acknowledge that your use is subject to their Terms of Service. All external model providers are considered “Third Party Materials” as defined in the [Posit End User License Agreement](https://posit.co/about/eula/) and Posit assumes no liability or other obligations with respect thereto and, without limiting the foregoing, is not liable for any loss or damage resulting from the use or access thereof.
