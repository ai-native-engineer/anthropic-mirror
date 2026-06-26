<!-- source: https://claude.com/docs/third-party/claude-desktop/claude-api -->

To use Anthropic’s Claude API directly as the inference provider, set [`inferenceProvider`](/docs/third-party/claude-desktop/configuration#inferenceprovider) to `anthropic` and supply an API key as described below. This is the first-party path: inference goes straight to Anthropic rather than to a Claude deployment hosted in your Amazon, Google, or Microsoft tenancy.

When `inferenceProvider` is `anthropic`, inference traffic goes to Anthropic’s API endpoints rather than staying within your cloud provider. This option does not offer third-party data residency; see the [overview](/docs/third-party/claude-desktop/overview) for what that means for the compliance statements on these pages.

For environments where static API keys aren’t permitted, set [`inferenceCredentialHelper`](/docs/third-party/claude-desktop/configuration#inferencecredentialhelper) to an executable that fetches a short-lived credential at runtime; see [Write a credential helper](/docs/third-party/claude-desktop/credential-helper).

##  Configure the app

###  Configuration keys

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `inferenceAnthropicApiKey` | `string` | MDM + Bootstrap | — | Leave blank to fetch a key via browser sign-in, or to supply the key via a credential helper. |

[Microsoft Foundry](/docs/third-party/claude-desktop/foundry)[MCP, plugins, skills, and hooks](/docs/third-party/claude-desktop/extensions)
