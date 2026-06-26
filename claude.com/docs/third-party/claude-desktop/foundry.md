<!-- source: https://claude.com/docs/third-party/claude-desktop/foundry -->

This page walks an IT administrator through a Microsoft Foundry deployment: creating the Azure AI Foundry resource, choosing the authentication path that fits your organization, and pushing the managed configuration. If you only need the list of configuration keys, skip to [Configure the app](#configure-the-app).

In this preview platform integration, Claude models on Microsoft Foundry run on Anthropic’s infrastructure. This is a commercial integration for billing and access through Azure. The data-residency and “no conversation data sent to Anthropic” statements elsewhere in these pages do not apply when using Microsoft Foundry. See the [Overview](/docs/third-party/claude-desktop/overview) for details.

##  Choose an authentication approach

| Scenario | Use | Per-user identity | Notes |
| --- | --- | --- | --- |
| Proof of concept, single team | [API key](#api-key) (`inferenceFoundryApiKey`) | No (shared key) | A long-lived secret distributed in the managed profile. Simplest to start. |
| Broad rollout with per-user identity | [In-app Entra ID sign-in](#in-app-entra-id-sign-in) (`inferenceFoundryTenantId`, `inferenceFoundryClientId`) | Yes | Users sign in with their Entra ID account inside the app via device code. Requires app version 1.8555 or later. |
| Your organization already has tooling that obtains a Foundry credential | [Credential helper](/docs/third-party/claude-desktop/configuration#inferencecredentialhelper) (`inferenceCredentialHelper`) | Depends on what the helper obtains | An executable that prints the credential to stdout at runtime. |

##  Set up Azure

These steps are performed once per Azure subscription. You need permission to create resources and, for in-app sign-in, to register an application in Microsoft Entra ID.

1

Create an Azure AI Foundry resource

In the Azure portal, create an Azure AI Foundry resource in your subscription. Record the **resource name**; the app constructs the endpoint as `<resource-name>.services.ai.azure.com`.

2

Deploy the Claude models

In the Azure AI Foundry portal for your resource, deploy the Claude models you intend to serve. Record each **deployment name**; you will list these in `inferenceModels`.

3

Obtain an API key (API-key approach only)

If you chose the API-key approach, copy one of the resource’s keys from the Azure portal. You will place it in the managed configuration in [Configure the app](#configure-the-app).

4

Register an Entra ID application (in-app sign-in only)

If you chose in-app Entra ID sign-in, register an application in the [Microsoft Entra admin center](https://entra.microsoft.com) under **Identity → Applications → App registrations → New registration**. On the registration:

* Under **Authentication**, enable **Allow public client flows**. The app uses the OAuth device-code flow, which requires a public client.
* Under **API permissions**, add the **Azure Cognitive Services** delegated scope (`https://cognitiveservices.azure.com/.default`) so the issued token is accepted by your Foundry resource.

Record the **Directory (tenant) ID** and **Application (client) ID**.Grant the users or groups who will sign in a role on the Foundry resource that permits inference (for example, **Cognitive Services User**).

##  Prepare devices

What each end-user device needs depends on the authentication approach you chose.

###  API key

No per-device preparation is required. Place the resource’s API key in the managed configuration as `inferenceFoundryApiKey`.

###  In-app Entra ID sign-in

No per-device preparation is required. Distribute `inferenceFoundryTenantId` and `inferenceFoundryClientId` in the managed configuration.
When both keys are set and `inferenceCredentialKind` is `interactive`, the app shows a **Sign in with Microsoft** page the first time a user opens the Cowork tab. Clicking the button starts a device-code flow against `login.microsoftonline.com`: the app displays a short verification code and opens the Microsoft sign-in page in the default browser, where the user enters the code and approves access. On success, the app stores the refresh token encrypted with the operating system’s secure storage (Keychain on macOS, DPAPI on Windows) and returns to the Cowork tab.
These two keys can be set only via an MDM profile, not via a [bootstrap server](/docs/third-party/claude-desktop/bootstrap).

####  Allow network egress

The sign-in flow reaches `login.microsoftonline.com` in addition to your Foundry endpoint. Both hosts are included automatically in the **Egress Requirements** section of the in-app configuration window when these keys are set.

##  Configure the app

Open the in-app configuration window (**Developer → Configure third-party inference**). In the **Connection** section, set **Inference provider** to **Foundry**, then fill in the **Foundry credentials** card with the values for whichever authentication approach you chose:

| Field | API key | In-app Entra ID sign-in |
| --- | --- | --- |
| Azure AI Foundry resource name | `your-foundry-resource` | `your-foundry-resource` |
| Azure AI Foundry API key | your resource key | *leave empty* |
| Entra ID tenant ID | *leave empty* | `00000000-0000-0000-0000-000000000000` |
| Entra ID client ID | *leave empty* | `11111111-1111-1111-1111-111111111111` |

Under **Models**, add at least one **Model list** entry using the Foundry deployment name.
Then click **Export** to produce a `.mobileconfig` (macOS) or `.reg` (Windows) file for your MDM. See [Installation and setup](/docs/third-party/claude-desktop/installation) for the export and deployment workflow.

###  Configuration keys

The full set of Foundry keys is below. Set `inferenceProvider` to `foundry`, supply the resource name, and provide exactly one credential source.

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `inferenceFoundryResource` | `string` | MDM + Bootstrap | — | Azure AI Foundry resource name used to construct the endpoint URL. |
| `inferenceFoundryApiKey` | `string` | MDM + Bootstrap | — |  |
| `inferenceFoundryTenantId` | `string` | MDM only | — | Directory (tenant) ID of the Entra ID app registration that has the Cognitive Services scope. |
| `inferenceFoundryClientId` | `string` | MDM only | — | Application (client) ID of the Entra ID app registration. The app must allow public client flows for device code. |

You must also set `inferenceModels` to a list of Foundry deployment names. See the [Configuration reference](/docs/third-party/claude-desktop/configuration#inferencemodels).

##  What users experience

| Approach | First launch | Re-authentication |
| --- | --- | --- |
| API key | The app opens directly; no user action. | Never, until you rotate the key in the managed profile. |
| In-app Entra ID sign-in | The app shows a **Sign in with Microsoft** page; the user approves a device code in the browser. | When the stored refresh token expires or is revoked under your tenant’s policy. The app prompts in-app. |

##  Troubleshoot

To confirm which keys the app read and whether credentials validated, use **Help → Troubleshooting → Copy Managed Configuration Report**; see [Verifying the deployment](/docs/third-party/claude-desktop/installation#verifying-the-deployment) for that workflow and the common causes when the app does not enter 3P mode. Application log locations are listed in [Data storage and residency](/docs/third-party/claude-desktop/data-storage).
If in-app sign-in fails at the token step, confirm the Entra ID app registration has **Allow public client flows** enabled and that the **Cognitive Services** scope is granted; without the public-client setting, the device-code flow is rejected.

[Vertex AI](/docs/third-party/claude-desktop/vertex)[Claude API](/docs/third-party/claude-desktop/claude-api)
