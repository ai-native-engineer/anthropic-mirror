<!-- source: https://claude.com/docs/third-party/claude-desktop/mantle -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

Amazon Bedrock Mantle is Amazon Bedrock’s Anthropic-native API surface. Unlike the standard [Amazon Bedrock provider](https://claude.com/docs/third-party/claude-desktop/bedrock), Mantle speaks the Anthropic Messages API directly and authenticates with a bearer token rather than the AWS SigV4 credential chain, so no AWS CLI, named profile, or IAM Identity Center setup is needed on the device. In practice, Mantle is the Amazon Bedrock provider with a different runtime endpoint and a single bearer-token credential path.

##  Choose an authentication approach

Mantle supports a bearer token only. There is no in-app AWS sign-in or named-profile support for this provider; if you need per-user IAM Identity Center authentication, use the standard [Amazon Bedrock provider](https://claude.com/docs/third-party/claude-desktop/bedrock) instead.

| Scenario | Use | Notes |
| --- | --- | --- |
| Any Mantle deployment | [Bearer token](#bearer-token) (`inferenceBedrockBearerToken`) | A long-lived token distributed in the managed profile. |
| Token must not be stored statically | [Credential helper](https://claude.com/docs/third-party/claude-desktop/configuration#inferencecredentialhelper) (`inferenceCredentialHelper`) | An executable that prints the bearer token to stdout at runtime. |

##  Set up AWS

Enable Claude models in Amazon Bedrock for the region you will set as `inferenceBedrockRegion`, and obtain a Mantle bearer token for that account. See [Set up AWS](https://claude.com/docs/third-party/claude-desktop/bedrock#set-up-aws) on the Amazon Bedrock page for the model-access step; the IAM Identity Center steps there are not needed for Mantle.

##  Prepare devices

###  Bearer token

No per-device preparation is required. Place the Mantle bearer token in the managed configuration as `inferenceBedrockBearerToken`.
The app reaches `bedrock-mantle.<region>.api.aws` (or the host in `inferenceBedrockBaseUrl` if you set one). This host is included automatically in the **Egress Requirements** section of the in-app configuration window. The `.api.aws` zone has no FIPS endpoint variant.

##  Configure the app

Open the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration#open-the-configuration-window) (**Developer → Configure Third-Party Inference…**). In the **Connection** section, set **Inference provider** to **Bedrock Mantle**, then fill in the credentials card:

| Field | Value |
| --- | --- |
| AWS region | e.g. `us-east-1` |
| AWS bearer token | your Mantle bearer token |
| Bedrock base URL | *optional* |

If you set **Bedrock base URL**, provide the full SDK base URL including the `/anthropic` path (for example `https://bedrock-mantle.us-east-1.api.aws/anthropic`); it replaces the default `bedrock-mantle.<region>.api.aws/anthropic` endpoint.
Under **Models**, add at least one **Model list** entry. Mantle has no model-list endpoint, so model discovery is not available and `inferenceModels` is required.
Then click **Export** to produce a `.mobileconfig` (macOS) or `.reg` (Windows) file for your MDM. See [Deploy with MDM](https://claude.com/docs/third-party/claude-desktop/mdm) for the export and deployment workflow.

###  Configuration keys

Mantle reuses the `inferenceBedrock*` key names. Only `inferenceBedrockRegion`, `inferenceBedrockBearerToken`, and `inferenceBedrockBaseUrl` apply; the other keys below (`inferenceBedrockProfile`, `inferenceBedrockSso*`, `inferenceBedrockAwsDir`, `inferenceBedrockAwsCliPath`, `inferenceBedrockServiceTier`) are ignored for this provider.

| Setting | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| AWS region `inferenceBedrockRegion` | `string` | MDM + Bootstrap | — | AWS region for the Bedrock runtime endpoint. |
| Bedrock base URL `inferenceBedrockBaseUrl` | `string` | MDM + Bootstrap | — | For VPC endpoints or gateway proxies. Host origin only. |
| Bedrock service tier `inferenceBedrockServiceTier` | `enum` | MDM + Bootstrap | — | Sent as the X-Amzn-Bedrock-Service-Tier header. Leave unset for on-demand. One of: `flex`, `priority`. |
| AWS bearer token `inferenceBedrockBearerToken` | `string` | MDM + Bootstrap | — | Static bearer token for inference. For providers that support profile or helper-script credentials, prefer those. |
| AWS SSO start URL `inferenceBedrockSsoStartUrl` | `string` | MDM + Bootstrap | — | Enables in-app AWS sign-in (no AWS CLI needed). Set with the three SSO fields below. |
| AWS SSO region `inferenceBedrockSsoRegion` | `string` | MDM + Bootstrap | — | IAM Identity Center home region. |
| AWS SSO account ID `inferenceBedrockSsoAccountId` | `string` | MDM + Bootstrap | — | 12-digit AWS account ID assigned to users in IAM Identity Center. |
| AWS SSO role name `inferenceBedrockSsoRoleName` | `string` | MDM + Bootstrap | — | IAM Identity Center permission-set name granting bedrock:InvokeModel\* on the account above. |
| AWS profile name `inferenceBedrockProfile` | `string` | MDM + Bootstrap | — | AWS named profile to use for Bedrock inference credentials. |
| AWS config directory `inferenceBedrockAwsDir` | `string` | MDM + Bootstrap | — | Folder with AWS config/credentials. Defaults to ~/.aws when no bearer token is set. |
| AWS CLI path `inferenceBedrockAwsCliPath` | `string` | MDM + Bootstrap | — | Absolute path to the aws executable. Leave unset to find it on PATH. |

inferenceBedrockServiceTier details

Tier availability varies by model and region. Reserved capacity uses a provisioned-throughput ARN as the model ID instead of this setting. Older bundled Claude Code CLI versions ignore this key.

You must also set `inferenceModels`. As with the standard Amazon Bedrock provider, server-side Web Search is not supported. See the [Configuration reference](https://claude.com/docs/third-party/claude-desktop/configuration#inferencemodels).

##  What users experience

The app opens directly on first launch with no user action. Users are never prompted to sign in; re-authentication happens only when you rotate the bearer token in the managed profile.

##  Troubleshoot

To confirm which keys the app read and whether credentials validated, use **Help → Troubleshooting → Copy Managed Configuration Report**; see [Verifying the deployment](https://claude.com/docs/third-party/claude-desktop/installation#verifying-the-deployment) for that workflow and the common causes when the app does not enter 3P mode. Application log locations are listed in [Data storage and residency](https://claude.com/docs/third-party/claude-desktop/data-storage).
