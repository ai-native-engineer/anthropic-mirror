<!-- source: https://claude.com/docs/third-party/claude-desktop/claude-api -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

To use Anthropic’s Claude API directly as the inference provider, set [`inferenceProvider`](https://claude.com/docs/third-party/claude-desktop/configuration#inferenceprovider) to `anthropic` and supply an API key as described below. This is the first-party path: inference goes straight to Anthropic rather than to a Claude deployment hosted in your Amazon, Google, or Microsoft tenancy.

When `inferenceProvider` is `anthropic`, inference traffic goes to Anthropic’s API endpoints rather than staying within your cloud provider. The data-residency and compliance statements on these pages do not apply to this option.

##  Choose an authentication approach

A static API key in the managed configuration is the simplest path. For environments where static API keys aren’t permitted, set [`inferenceCredentialHelper`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencecredentialhelper) to an executable that fetches a short-lived credential at runtime; see [Write a credential helper](https://claude.com/docs/third-party/claude-desktop/credential-helper).

##  Configure the app

###  Configuration keys

| Setting | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| Claude API key `inferenceAnthropicApiKey` | `string` | MDM + Bootstrap | — | Leave blank to fetch a key via browser sign-in, or to supply the key via a credential helper. |
