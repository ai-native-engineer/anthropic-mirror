<!-- source: https://platform.claude.com/docs/en/manage-claude/authentication -->

# Authentication
Authenticate to the Claude API with API keys or Workload Identity Federation.
The Claude API supports two ways to authenticate requests:  
| Method  | Credential  | Best for  |  
| --- | --- | --- |  
| [API key](https://platform.claude.com/docs/en/manage-claude/authentication#api-keys)  | Long-lived `sk-ant-api...` secret in the `x-api-key` header  | Local development, prototyping, scripts, and single-tenant servers where you control secret storage  |  
| [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/authentication#workload-identity-federation)  | Short-lived bearer token exchanged from your identity provider's identity token  | Production workloads on cloud platforms (AWS, Google Cloud, Azure), CI/CD pipelines, and Kubernetes, where you want to eliminate static secrets  |  
Both methods grant the same access to Claude API endpoints. Choose API keys to get started quickly, and move to Workload Identity Federation when your workload already has a platform-issued identity you can federate.
API keys
API keys are static secrets that you generate in the Claude Console and pass on every request.
  * **Create a key:** Go to [Settings → API keys](https://platform.claude.com/settings/keys) in the Claude Console. Use [workspaces](https://platform.claude.com/settings/workspaces) to scope keys by project or environment.
  * **Send the key:** Set the `x-api-key` header on direct HTTP requests, or set the `ANTHROPIC_API_KEY` environment variable and the [client SDKs](https://platform.claude.com/docs/en/cli-sdks-libraries/overview) pick it up automatically.

POST /v1/messages
x-api-key: YOUR_API_KEY
anthropic-version: 2023-06-01
content-type: application/json

API keys have no expiry. Store them in a secrets manager, rotate them periodically, and revoke any key you suspect has leaked.
cURLPythonTypeScriptGoJavaC#PHPRubyCLI

client = Anthropic(api_key="my-anthropic-api-key")
# or, with ANTHROPIC_API_KEY set in the environment:
client = Anthropic()

Workload Identity Federation
Workload Identity Federation (WIF) lets a workload authenticate with a short-lived identity token issued by an identity provider (IdP) you already trust, such as AWS IAM, Google Cloud, or any standards-compliant OIDC issuer (such as GitHub Actions, Kubernetes service accounts, SPIFFE, Microsoft Entra ID, or Okta). The workload exchanges its IdP-issued JWT at `POST /v1/oauth/token` for a short-lived Claude API access token, and the SDK refreshes that token automatically before it expires. There is no `sk-ant-api...` string to mint, distribute, or rotate.
Federation removes long-lived Claude API keys from your environment, which shrinks the blast radius of a leaked credential and lets you manage access with the same IdP controls you already use for cloud resources. It does not, on its own, guarantee end-to-end security: the trust chain is only as strong as your identity provider's configuration, and a long-lived secret one hop upstream (for example, a static cloud credential that can mint IdP tokens) can still undermine it. Pair federation with your provider's controls, such as IP allowlists, MFA, and audit logging.
To configure federation, you create three resources in the Claude Console (a service account, a federation issuer, and a federation rule) and then point your SDK at the rule. See [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) for the full setup walkthrough.
Next steps
[  Set up Workload Identity Federation Configure issuers, rules, and service accounts, then exchange tokens ](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation)[ Identity provider guides Step-by-step guides for AWS, Google Cloud, Azure, GitHub Actions, Kubernetes, SPIFFE, and Okta ](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#identity-providers)[  WIF reference Environment variables, validation rules, profile configuration, and error reference ](https://platform.claude.com/docs/en/manage-claude/wif-reference)[  Client SDKs Python, TypeScript, C#, Go, Java, PHP, Ruby, and the CLI ](https://platform.claude.com/docs/en/cli-sdks-libraries/overview)
  * [API keys](https://platform.claude.com/docs/en/manage-claude/authentication#api-keys)
  * [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/authentication#workload-identity-federation)
  * [Next steps](https://platform.claude.com/docs/en/manage-claude/authentication#next-steps)

Admin/Authentication
# Authentication
Authenticate to the Claude API with API keys or Workload Identity Federation.
The Claude API supports two ways to authenticate requests:  
| Method  | Credential  | Best for  |  
| --- | --- | --- |  
| [API key](https://platform.claude.com/docs/en/manage-claude/authentication#api-keys)  | Long-lived `sk-ant-api...` secret in the `x-api-key` header  | Local development, prototyping, scripts, and single-tenant servers where you control secret storage  |  
| [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/authentication#workload-identity-federation)  | Short-lived bearer token exchanged from your identity provider's identity token  | Production workloads on cloud platforms (AWS, Google Cloud, Azure), CI/CD pipelines, and Kubernetes, where you want to eliminate static secrets  |  
Both methods grant the same access to Claude API endpoints. Choose API keys to get started quickly, and move to Workload Identity Federation when your workload already has a platform-issued identity you can federate.
API keys
API keys are static secrets that you generate in the Claude Console and pass on every request.
  * **Create a key:** Go to [Settings → API keys](https://platform.claude.com/settings/keys) in the Claude Console. Use [workspaces](https://platform.claude.com/settings/workspaces) to scope keys by project or environment.
  * **Send the key:** Set the `x-api-key` header on direct HTTP requests, or set the `ANTHROPIC_API_KEY` environment variable and the [client SDKs](https://platform.claude.com/docs/en/cli-sdks-libraries/overview) pick it up automatically.

POST /v1/messages
x-api-key: YOUR_API_KEY
anthropic-version: 2023-06-01
content-type: application/json

API keys have no expiry. Store them in a secrets manager, rotate them periodically, and revoke any key you suspect has leaked.
cURLPythonTypeScriptGoJavaC#PHPRubyCLI

client = Anthropic(api_key="my-anthropic-api-key")
# or, with ANTHROPIC_API_KEY set in the environment:
client = Anthropic()

Workload Identity Federation
Workload Identity Federation (WIF) lets a workload authenticate with a short-lived identity token issued by an identity provider (IdP) you already trust, such as AWS IAM, Google Cloud, or any standards-compliant OIDC issuer (such as GitHub Actions, Kubernetes service accounts, SPIFFE, Microsoft Entra ID, or Okta). The workload exchanges its IdP-issued JWT at `POST /v1/oauth/token` for a short-lived Claude API access token, and the SDK refreshes that token automatically before it expires. There is no `sk-ant-api...` string to mint, distribute, or rotate.
Federation removes long-lived Claude API keys from your environment, which shrinks the blast radius of a leaked credential and lets you manage access with the same IdP controls you already use for cloud resources. It does not, on its own, guarantee end-to-end security: the trust chain is only as strong as your identity provider's configuration, and a long-lived secret one hop upstream (for example, a static cloud credential that can mint IdP tokens) can still undermine it. Pair federation with your provider's controls, such as IP allowlists, MFA, and audit logging.
To configure federation, you create three resources in the Claude Console (a service account, a federation issuer, and a federation rule) and then point your SDK at the rule. See [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) for the full setup walkthrough.
Next steps
[  Set up Workload Identity Federation Configure issuers, rules, and service accounts, then exchange tokens ](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation)[ Identity provider guides Step-by-step guides for AWS, Google Cloud, Azure, GitHub Actions, Kubernetes, SPIFFE, and Okta ](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#identity-providers)[  WIF reference Environment variables, validation rules, profile configuration, and error reference ](https://platform.claude.com/docs/en/manage-claude/wif-reference)[  Client SDKs Python, TypeScript, C#, Go, Java, PHP, Ruby, and the CLI ](https://platform.claude.com/docs/en/cli-sdks-libraries/overview)
