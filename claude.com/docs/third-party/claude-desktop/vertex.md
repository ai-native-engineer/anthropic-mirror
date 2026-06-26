<!-- source: https://claude.com/docs/third-party/claude-desktop/vertex -->

This page walks an IT administrator through a complete Vertex AI deployment: enabling Claude in your Google Cloud project, choosing the authentication path that fits your organization, preparing devices, and pushing the managed configuration. If you only need the list of configuration keys, skip to [Configure the app](#configure-the-app).

##  Choose an authentication approach

Vertex AI authenticates with Google Cloud Application Default Credentials, which can be supplied several ways. The right one depends on whether your users have Google identities and whether you need per-user attribution in Cloud Audit Logs.

| Scenario | Use | Per-device prerequisite | Per-user Cloud Audit Logs identity | Notes |
| --- | --- | --- | --- | --- |
| Proof of concept, single team | [Service-account key](#credentials-file) (`inferenceVertexCredentialsFile`) | The key file on each device | No (shared service account) | A long-lived secret distributed to every device. Simplest to start; not recommended for broad rollout. |
| Users have Google Workspace or Cloud Identity accounts | [In-app Google sign-in](#in-app-google-sign-in) (`inferenceVertexOAuth*`) | None | Yes | Users sign in with their Google account inside the app. See the session-control warning below. |
| Users authenticate with a third-party IdP (Entra ID, Okta, Ping, …) and you don’t want to provision Google identities | [In-app Workforce Identity sign-in](#in-app-workforce-identity-sign-in) (`inferenceVertexWorkforce*`) | None | Yes (workforce-pool principal) | Users sign in with their corporate identity inside the app. The app runs PKCE against your IdP and exchanges the ID token at Google STS. |
| Your organization already has tooling that obtains a Vertex-usable bearer | [Credential helper](/docs/third-party/claude-desktop/configuration#inferencecredentialhelper) (`inferenceCredentialHelper`) | The helper executable on each device | Depends on what the helper obtains | The helper’s stdout is sent as the bearer on each Vertex request. |
| You already operate an LLM proxy | [Gateway provider](/docs/third-party/claude-desktop/gateway) instead of Vertex | None | At your gateway | The proxy holds the Google Cloud credentials; the app authenticates only to the proxy. |

If your Google Workspace or Cloud Identity organization enforces a **Google Cloud session length** of a few hours or less (Admin console → Security → Google Cloud session control), the in-app Google sign-in stores a refresh token that is subject to that policy, and users will be prompted to sign in again each time it expires. For short session policies, either mark your OAuth client as a [trusted app exempt from reauthentication](https://support.google.com/a/answer/9368756), or use a service-account key, Workforce Identity sign-in, or the gateway provider instead.

##  Set up Google Cloud

These steps are performed once per Google Cloud project, regardless of which authentication approach you chose. You need a project with Owner or Editor access.

1

Enable the Vertex AI API

In the [Google Cloud console](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com), enable the **Vertex AI API** for your project.

2

Enable Claude models in Model Garden

In the Vertex AI [Model Garden](https://console.cloud.google.com/vertex-ai/model-garden), locate the Claude models you intend to deploy and click **Enable** on each. Model availability varies by region; enable them in the region you will set as `inferenceVertexRegion`.

3

Grant users access to Vertex AI

Each authenticated principal needs permission to call the model. On the project’s **IAM** page, grant the **Vertex AI User** role (`roles/aiplatform.user`) to:

* the service account, if using a service-account key file
* the Google group containing your users, if using in-app Google sign-in

If your organization uses a narrower custom role, it must include at minimum `aiplatform.endpoints.predict`.

4

Create an OAuth client (in-app Google sign-in only)

If you chose in-app Google sign-in, create a Desktop-app OAuth client in your project. See [In-app Google sign-in](#in-app-google-sign-in) below for the full procedure, including consent-screen setup.

5

Federate to your IdP (optional)

If your users authenticate with Microsoft Entra ID, Okta, or another identity provider and do not already have Google accounts, you have two options:

* **Workforce Identity Federation** (recommended). Create a workforce pool with an OIDC provider, and use the [in-app Workforce Identity sign-in](#in-app-workforce-identity-sign-in) approach. Users sign in directly with their corporate identity; no Google identity is provisioned.
* **Cloud Identity with SAML SSO.** Provision a free Cloud Identity tenant and configure SAML single sign-on to your IdP. Users then sign in through the in-app Google sign-in approach with a Google identity that is backed by your IdP. See [Set up SSO with a third-party IdP](https://support.google.com/cloudidentity/answer/12032922) in the Cloud Identity documentation.

##  Prepare devices

What each end-user device needs depends on the authentication approach you chose.

###  Credentials file

Create a service account in your project, grant it the **Vertex AI User** role, and download its JSON key. Distribute the key file to a fixed path on each device through your device-management tooling and set `inferenceVertexCredentialsFile` to that path.
`inferenceVertexCredentialsFile` accepts any Application Default Credentials JSON format, so if your environment already produces an `authorized_user` file (from `gcloud auth application-default login`) or an `external_account` Workforce Identity Federation configuration, you can point at that file instead. For `external_account` files, the `credential_source` must be of type `file` or `url` (`executable` sources are not supported), and separate tooling on the device must obtain the IdP token and write it to the configured location; Claude Desktop does not perform that step.

###  In-app Google sign-in

No per-device preparation is required. The sign-in experience uses a Google OAuth client that **you create in your own Google Cloud project**; Anthropic does not provide or operate an OAuth client for this flow. Distribute the OAuth client ID and secret in the managed configuration (see [Configure the app](#configure-the-app)).

####  How it works

When `inferenceVertexOAuthClientId` and `inferenceVertexOAuthClientSecret` are both set, the app shows a **Sign in with Google** page the first time a user opens the Cowork tab. Clicking the button opens the system browser for a standard Google consent flow, and the app listens on a loopback address for the redirect. On success, the app stores the user’s Google refresh token encrypted with the operating system’s secure storage (Keychain on macOS, DPAPI on Windows) and returns to the Cowork tab.
At the start of each Cowork session, the app writes an `authorized_user` Application Default Credentials file (the same format produced by `gcloud auth application-default login`) into the session sandbox and points `GOOGLE_APPLICATION_CREDENTIALS` at it. The Google Cloud client library inside the sandbox handles access-token minting and refresh automatically.
If the stored refresh token is revoked or expires, or if you deploy a new OAuth client ID, the app clears the stored token and shows the sign-in page again.

####  Create the OAuth client

1

Configure the OAuth consent screen

In the Google Cloud Console for your Vertex project, open **APIs & Services → OAuth consent screen**.If your project belongs to a Google Workspace organization, select the **Internal** user type. Internal apps are limited to users in your Workspace and do not require Google verification, regardless of which scopes they request.If the project is not in a Workspace organization, you must use the **External** user type. Because this flow requests the `https://www.googleapis.com/auth/cloud-platform` scope, Google classifies the app as using a sensitive scope, and publishing it beyond test users requires Google’s OAuth verification process. For that reason, Internal is strongly recommended for enterprise deployments.

2

Create a Desktop OAuth client

In **APIs & Services → Credentials**, choose **Create credentials → OAuth client ID**, and select **Desktop app** as the application type.Record the generated **Client ID** (ending in `.apps.googleusercontent.com`) and **Client secret**. For installed applications, Google does not treat the client secret as confidential; the flow is protected by PKCE and by the loopback redirect, so it is safe to distribute the secret in a managed configuration profile.You do not need to add redirect URIs. Desktop-app clients permit loopback (`http://127.0.0.1:<port>`) redirects automatically.

3

Allow network egress

The sign-in flow and subsequent token refreshes reach `accounts.google.com` and `oauth2.googleapis.com` from the user’s device. These hosts are already included in the standard Vertex AI egress requirements, so if you allowed egress based on the **Egress Requirements** section of the configuration window, no additional firewall changes are needed.

####  Federate to a third-party identity provider

The in-app sign-in always opens Google’s authorization endpoint, because Vertex AI only accepts Google-issued access tokens. To have users authenticate with your organization’s own identity provider (Microsoft Entra ID, Okta, Ping, or an in-house SAML IdP) instead of a Google password, configure Cloud Identity as a broker:

1. In the Google Admin console, set up [SSO with a third-party IdP](https://support.google.com/cloudidentity/answer/12032922) and assign the SSO profile to your Claude Desktop users’ organizational unit.
2. Provision those users into Cloud Identity (via SCIM from your IdP, or Google Cloud Directory Sync) so IAM grants resolve.
3. Optionally set `inferenceVertexOAuthLoginHint` so Google skips its own account chooser and routes straight to your IdP with the user’s identity pre-filled.

With this in place, clicking **Sign in with Google** opens the browser, Google immediately redirects to your IdP, the user authenticates there (including smart-card or PIV authentication if your IdP supports it), and Google issues the tokens on return. Claude Desktop is unchanged; the federation is configured entirely in Google Admin and your IdP.

####  Notes and limitations

* **Precedence.** When both `inferenceVertexOAuthClientId` and `inferenceVertexCredentialsFile` are set and `inferenceCredentialKind` is not, Google sign-in takes precedence and the credentials file is ignored (the app logs a multi-credential warning). To force the credentials file, set `inferenceCredentialKind` to `vendor-profile` or remove the OAuth client keys.
* **Both keys required.** If only one of `inferenceVertexOAuthClientId` or `inferenceVertexOAuthClientSecret` is set, the app logs a warning and falls back to standard Application Default Credentials discovery.
* **Client rotation.** If you replace the OAuth client in Google Cloud and push the new client ID via MDM, existing users are automatically signed out and prompted to sign in again on next launch.

###  In-app Workforce Identity sign-in

No per-device preparation is required. In Google Cloud, create a [workforce pool](https://cloud.google.com/iam/docs/workforce-identity-federation) with an OIDC provider pointing at your organization’s IdP, and grant the pool’s principals the **Vertex AI User** role on the project.
In your IdP, register a native OAuth client for the app. The app does not send a client secret in this flow, so the client must be public (no client authentication) with PKCE required. The sign-in redirect lands on `http://127.0.0.1:<port>/callback`, where the operating system chooses `<port>` on each sign-in:

* If your IdP permits loopback redirect URIs on any port (the [RFC 8252](https://datatracker.ietf.org/doc/html/rfc8252#section-7.3) native-app pattern, supported by Microsoft Entra ID under the **Mobile and desktop applications** platform), register `http://127.0.0.1/callback` and leave `redirectPort` unset.
* If your IdP requires an exact registered redirect URI (such as Okta or PingFederate), set the `redirectPort` field of `inferenceVertexWorkforceOidc` to a fixed port and register the resulting URI exactly, for example `http://127.0.0.1:53180/callback`.

Use `127.0.0.1`, not `localhost`; most IdPs do not treat them as interchangeable.
Distribute the workforce-pool provider audience and the IdP OIDC client in the managed configuration; the app shows a **Sign in** page on first launch, runs an authorization-code-with-PKCE flow against your IdP in the system browser, exchanges the returned ID token for a Google Cloud access token at `sts.googleapis.com`, and stores the IdP refresh token encrypted with the operating system’s secure storage. No `gcloud` CLI, helper script, or Google identity is required.

##  Configure the app

With Google Cloud set up and devices prepared, open the in-app configuration window (**Developer → Configure third-party inference**) on an evaluation device. In the **Connection** section, set **Inference provider** to **Vertex AI** and fill in the **Vertex AI credentials** card with the values for whichever authentication approach you chose:

| Field | Service-account key | In-app Google sign-in |
| --- | --- | --- |
| GCP project ID | `your-gcp-project` | `your-gcp-project` |
| GCP region | e.g. `us-east5` | e.g. `us-east5` |
| GCP credentials file path | `/path/to/sa-key.json` | *leave empty* |
| Vertex OAuth client ID | *leave empty* | `1234567890-abc123.apps.googleusercontent.com` |
| Vertex OAuth client secret | *leave empty* | `GOCSPX-xxxxxxxxxxxxxxxxxxxx` |
| Vertex OAuth scopes | *leave empty* | *leave empty for the default* |
| Vertex AI base URL | *optional* | *optional* |

Under **Models**, add at least one **Model list** entry using the Vertex publisher model ID, for example `claude-sonnet-4-5@20250929`.
Then click **Export** to produce a `.mobileconfig` (macOS) or `.reg` (Windows) file for your MDM. See [Installation and setup](/docs/third-party/claude-desktop/installation) for the export and deployment workflow.

###  Configuration keys

The full set of Vertex keys is below. Set `inferenceProvider` to `vertex`, supply a project and region, and provide exactly one credential source.

| Key | Type | Availability | Default | Description |
| --- | --- | --- | --- | --- |
| `inferenceVertexProjectId` | `string` | MDM + Bootstrap | — |  |
| `inferenceVertexRegion` | `string` | MDM + Bootstrap | — | GCP region where your Vertex AI Claude models are deployed. |
| `inferenceVertexBaseUrl` | `string` | MDM + Bootstrap | — | PSC endpoint, if using one. |
| `inferenceVertexOAuthClientId` | `string` | MDM + Bootstrap | — | Desktop-app OAuth client ID. Enables Sign in with Google instead of a credentials file. |
| `inferenceVertexOAuthClientSecret` | `string` | MDM + Bootstrap | — | Secret for the Desktop-app OAuth client above. |
| `inferenceVertexOAuthScopes` | `string` | MDM + Bootstrap | — | Override the Google OAuth scopes (space-separated). Leave blank for the default. |
| `inferenceVertexOAuthLoginHint` | `string` | MDM + Bootstrap | — | Pre-fill Google’s account chooser and forward to your federated IdP. {username} expands to the OS login name. |
| `inferenceVertexWorkforceAudience` | `string` | MDM + Bootstrap | — | Workforce-pool provider audience. When set, sign-in uses your own IdP plus a GCP STS exchange instead of a Google identity. |
| `inferenceVertexWorkforceUserProject` | `string` | MDM + Bootstrap | — | GCP project for STS billing and quota. Defaults to the Vertex project ID above. |
| `inferenceVertexWorkforceOidc` | `object` | MDM + Bootstrap | — | Your organization’s OIDC IdP. The app runs an authorization-code-with-PKCE flow against this issuer and exchanges the returned ID token at GCP STS. |
| `inferenceVertexCredentialsFile` | `string` | MDM only | — | Absolute path to service-account JSON. Leave blank to fall back to ADC. |

If none of `inferenceVertexCredentialsFile`, the OAuth client keys, the Workforce Identity keys, or `inferenceCredentialHelper` is set, the Google client library falls back to the standard Application Default Credentials search path on the device (`~/.config/gcloud/application_default_credentials.json`, then the environment’s metadata server).
You must also set `inferenceModels` to a list of Vertex publisher model IDs, for example `claude-sonnet-4-5@20250929`. See the [Configuration reference](/docs/third-party/claude-desktop/configuration#inferencemodels).

##  What users experience

The first-launch and re-authentication behavior depends on the authentication approach.

| Approach | First launch | Re-authentication |
| --- | --- | --- |
| Credentials file (service-account key) | The app opens directly; no user action. | Never, until you rotate the key file. |
| In-app Google sign-in | The Cowork tab shows a **Sign in with Google** page. Clicking it opens Google’s consent flow in the default browser. After approval, the app relaunches into Cowork. | When the refresh token is revoked, when you deploy a new OAuth client ID, or when your Google Cloud session-control policy expires it. |

For in-app Google sign-in, the browser flow runs on the host (outside the Cowork sandbox), so it can use the user’s existing Google session and any security keys or passkeys configured on the device. Users can sign out by revoking the app from their Google Account’s [third-party connections page](https://myaccount.google.com/connections); the app detects the revoked token at the next session start and shows the sign-in page again.

##  Troubleshoot

To confirm which keys the app read and whether credentials validated, use **Help → Troubleshooting → Copy Managed Configuration Report**; see [Verifying the deployment](/docs/third-party/claude-desktop/installation#verifying-the-deployment) for that workflow and the common causes when the app does not enter 3P mode. Application log locations are listed in [Data storage and residency](/docs/third-party/claude-desktop/data-storage).

[Bedrock Mantle](/docs/third-party/claude-desktop/mantle)[Microsoft Foundry](/docs/third-party/claude-desktop/foundry)
