<!-- source: https://platform.claude.com/docs/en/api/overview -->

# API overview
The Claude API is a RESTful API at `https://api.anthropic.com` that provides programmatic access to Claude models and Claude Managed Agents.
**New to Claude?** For direct model access, start with [Get started](https://platform.claude.com/docs/en/get-started) and [Working with Messages](https://platform.claude.com/docs/en/build-with-claude/working-with-messages). For managed agent infrastructure, see the [Claude Managed Agents quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart).
Prerequisites
To use the Claude API, you'll need:
  * A [Claude Console account](https://platform.claude.com)
  * An [API key](https://platform.claude.com/settings/keys), or a configured [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) rule

For step-by-step setup instructions, see [Get started](https://platform.claude.com/docs/en/get-started).
Available APIs
The Claude API includes the following APIs:
**General Availability:**
  * **[Messages API](https://platform.claude.com/docs/en/api/messages/create)** : Send messages to Claude for conversational interactions (`POST /v1/messages`)
  * **[Message Batches API](https://platform.claude.com/docs/en/api/creating-message-batches)** : Process large volumes of Messages requests asynchronously with 50% cost reduction (`POST /v1/messages/batches`)
  * **[Token Counting API](https://platform.claude.com/docs/en/api/messages-count-tokens)** : Count tokens in a message before sending to manage costs and rate limits (`POST /v1/messages/count_tokens`)
  * **[Models API](https://platform.claude.com/docs/en/api/models-list)** : List available Claude models and their details (`GET /v1/models`)

**Beta:**
  * **[Files API](https://platform.claude.com/docs/en/api/files-create)** : Upload and manage files for use across multiple API calls (`POST /v1/files`, `GET /v1/files`)
  * **[Skills API](https://platform.claude.com/docs/en/api/skills/create-skill)** : Create and manage custom agent skills (`POST /v1/skills`, `GET /v1/skills`)
  * **[Agents API](https://platform.claude.com/docs/en/managed-agents/agent-setup)** : Define reusable, versioned agent configurations for Claude Managed Agents (`POST /v1/agents`, `GET /v1/agents`)
  * **[Sessions API](https://platform.claude.com/docs/en/managed-agents/sessions)** : Run stateful agent sessions in managed cloud sandboxes (`POST /v1/sessions`, `GET /v1/sessions/{id}/stream`)
  * **[Environments API](https://platform.claude.com/docs/en/managed-agents/environments)** : Configure sandbox templates for agent sessions (`POST /v1/environments`, `GET /v1/environments`)

For the complete API reference with all endpoints, parameters, and response schemas, explore the API reference pages listed in the navigation. To access beta features, see [Beta headers](https://platform.claude.com/docs/en/api/beta-headers).
Authentication
For details on both authentication methods and when to use each, see [Authentication](https://platform.claude.com/docs/en/manage-claude/authentication). All requests to the Claude API must include these headers:  
| Header  | Value  | Required  |  
| --- | --- | --- |  
| `x-api-key`  | Your API key from Console  | One of `x-api-key` or `Authorization`  |  
| `Authorization`  |  `Bearer <token>`, where `<token>` is a short-lived access token obtained from `POST /v1/oauth/token` via [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation)  | One of `x-api-key` or `Authorization`  |  
| `anthropic-version`  | API version (for example, `2023-06-01`)  | Yes  |  
| `content-type`  | `application/json`  | Yes  |  
If you are using the [Client SDKs](https://platform.claude.com/docs/en/api/overview#client-sdks), the SDK will send these headers automatically. For API versioning details, see [API versions](https://platform.claude.com/docs/en/api/versioning).
When accessing Claude through a [cloud platform](https://platform.claude.com/docs/en/api/overview#claude-api-vs-cloud-platforms), authentication is integrated with the cloud provider's IAM system. See the platform-specific documentation for supported credential types, required headers, and authentication options.
### 
Getting API keys
The API is made available through the web [Console](https://platform.claude.com/). You can use the [Workbench](https://platform.claude.com/workbench) to try out the API in the browser and then generate API keys in [Account Settings](https://platform.claude.com/settings/keys). Use [workspaces](https://platform.claude.com/settings/workspaces) to segment your API keys and [control spend](https://platform.claude.com/docs/en/api/rate-limits) by use case.
Client SDKs
Anthropic provides official SDKs that simplify API integration by handling authentication, request formatting, error handling, and more.
**Benefits:**
  * Automatic header management (x-api-key, anthropic-version, content-type)
  * Type-safe request and response handling
  * Built-in retry logic and error handling
  * Streaming support
  * Request timeouts and connection management

For a list of client SDKs, see [Client SDKs](https://platform.claude.com/docs/en/cli-sdks-libraries/overview).
Claude API vs cloud platforms
Claude is available through the direct Claude API and through cloud platforms. Choose based on your infrastructure, feature availability, compliance requirements, and pricing preferences.
### 
Claude API
  * **Direct access** to the latest models and features
  * **Anthropic billing and support**
  * **Best for:** New integrations, full feature access, direct relationship with Anthropic

### 
Cloud platform APIs
Access Claude through AWS, Google Cloud, or Microsoft Azure:
  * **Integrated** with cloud provider billing and IAM
  * **Feature availability varies by platform:** Anthropic-operated platforms include [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws) and [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry); partner-operated platforms include Amazon Bedrock and Google Cloud. See each platform's page for feature availability and timing.
  * **Best for:** Existing cloud commitments, specific compliance requirements, consolidated cloud billing

  
| Platform  | Provider  | Documentation  |  
| --- | --- | --- |  
| Claude Platform on AWS  | AWS (Anthropic-operated)  | [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)  |  
| Amazon Bedrock  | AWS  | [Claude in Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)  |  
| Agent Platform  | Google Cloud  | [Claude on Google Cloud](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)  |  
| Microsoft Foundry  | Microsoft Azure (Anthropic-operated)  | [Claude in Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)  |  
Claude Managed Agents is available through the direct Claude API and [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws). For feature availability across platforms, see the [Features overview](https://platform.claude.com/docs/en/build-with-claude/overview).
Request and response format
### 
Request size limits  
| Endpoint  | Maximum request size  |  
| --- | --- |  
| Messages, Token Counting  | 32 MB  |  
| [Message Batches API](https://platform.claude.com/docs/en/build-with-claude/batch-processing)  | 256 MB  |  
| [Files API](https://platform.claude.com/docs/en/build-with-claude/files)  | 500 MB  |  
| Sessions, Agents, Environments  | 32 MB  |  
If you exceed these limits, you'll receive a 413 `request_too_large` error.
Partner-operated platforms have their own request size limits: Google Cloud limits requests to 30 MB, and Bedrock limits requests to 20 MB. Claude Platform on AWS uses the same limits as the direct Claude API. Consult your platform's documentation for current values.
### 
Response headers
The Claude API includes the following headers in every response:
  * `request-id`: A globally unique identifier for the request
  * `anthropic-organization-id`: The organization ID associated with the API key used in the request

Claude Platform on AWS adds an AWS request ID (`x-amzn-requestid`) alongside the standard `request-id` header. See [Request IDs](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#request-ids) for the dual-ID handling pattern.
Rate limits and availability
### 
Rate limits
The API enforces rate limits and spend limits to prevent misuse and manage capacity. Limits are organized into usage tiers that increase automatically as you use the API. Each tier has:
  * **Spend limits** : Maximum monthly cost for API usage
  * **Rate limits** : Maximum number of requests per minute (RPM) and tokens per minute (TPM)

You can view your organization's current limits in the [Console](https://platform.claude.com/settings/limits). For higher limits, contact sales through the Console.
For detailed information about limits, tiers, and the token bucket algorithm used for rate limiting, see [Rate limits](https://platform.claude.com/docs/en/api/rate-limits).
### 
Availability
The Claude API is available in [many countries and regions](https://platform.claude.com/docs/en/api/supported-regions) worldwide. Check the supported regions page to confirm availability in your location.
Next steps
[  Messages API reference Complete API specification for direct model interactions ](https://platform.claude.com/docs/en/api/messages/create)[ Claude Managed Agents reference Agents, Sessions, and Environments endpoints ](https://platform.claude.com/docs/en/managed-agents/sessions)[  Client SDKs Python, TypeScript, C#, Go, Java, PHP, and Ruby ](https://platform.claude.com/docs/en/cli-sdks-libraries/overview)[ Rate limits Usage tiers, spend limits, and token bucket algorithm ](https://platform.claude.com/docs/en/api/rate-limits)
  * [Prerequisites](https://platform.claude.com/docs/en/api/overview#prerequisites)
  * [Available APIs](https://platform.claude.com/docs/en/api/overview#available-apis)
  * [Authentication](https://platform.claude.com/docs/en/api/overview#authentication)
  * [Getting API keys](https://platform.claude.com/docs/en/api/overview#getting-api-keys)
  * [Client SDKs](https://platform.claude.com/docs/en/api/overview#client-sdks)
  * [Claude API vs cloud platforms](https://platform.claude.com/docs/en/api/overview#claude-api-vs-cloud-platforms)
  * [Claude API](https://platform.claude.com/docs/en/api/overview#claude-api)
  * [Cloud platform APIs](https://platform.claude.com/docs/en/api/overview#cloud-platform-apis)
  * [Request and response format](https://platform.claude.com/docs/en/api/overview#request-and-response-format)
  * [Request size limits](https://platform.claude.com/docs/en/api/overview#request-size-limits)
  * [Response headers](https://platform.claude.com/docs/en/api/overview#response-headers)
  * [Rate limits and availability](https://platform.claude.com/docs/en/api/overview#rate-limits-and-availability)
  * [Rate limits](https://platform.claude.com/docs/en/api/overview#rate-limits)
  * [Availability](https://platform.claude.com/docs/en/api/overview#availability)
  * [Next steps](https://platform.claude.com/docs/en/api/overview#next-steps)

API reference/Using the API
# API overview
The Claude API is a RESTful API at `https://api.anthropic.com` that provides programmatic access to Claude models and Claude Managed Agents.
**New to Claude?** For direct model access, start with [Get started](https://platform.claude.com/docs/en/get-started) and [Working with Messages](https://platform.claude.com/docs/en/build-with-claude/working-with-messages). For managed agent infrastructure, see the [Claude Managed Agents quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart).
Prerequisites
To use the Claude API, you'll need:
  * A [Claude Console account](https://platform.claude.com)
  * An [API key](https://platform.claude.com/settings/keys), or a configured [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) rule

For step-by-step setup instructions, see [Get started](https://platform.claude.com/docs/en/get-started).
Available APIs
The Claude API includes the following APIs:
**General Availability:**
  * **[Messages API](https://platform.claude.com/docs/en/api/messages/create)** : Send messages to Claude for conversational interactions (`POST /v1/messages`)
  * **[Message Batches API](https://platform.claude.com/docs/en/api/creating-message-batches)** : Process large volumes of Messages requests asynchronously with 50% cost reduction (`POST /v1/messages/batches`)
  * **[Token Counting API](https://platform.claude.com/docs/en/api/messages-count-tokens)** : Count tokens in a message before sending to manage costs and rate limits (`POST /v1/messages/count_tokens`)
  * **[Models API](https://platform.claude.com/docs/en/api/models-list)** : List available Claude models and their details (`GET /v1/models`)

**Beta:**
  * **[Files API](https://platform.claude.com/docs/en/api/files-create)** : Upload and manage files for use across multiple API calls (`POST /v1/files`, `GET /v1/files`)
  * **[Skills API](https://platform.claude.com/docs/en/api/skills/create-skill)** : Create and manage custom agent skills (`POST /v1/skills`, `GET /v1/skills`)
  * **[Agents API](https://platform.claude.com/docs/en/managed-agents/agent-setup)** : Define reusable, versioned agent configurations for Claude Managed Agents (`POST /v1/agents`, `GET /v1/agents`)
  * **[Sessions API](https://platform.claude.com/docs/en/managed-agents/sessions)** : Run stateful agent sessions in managed cloud sandboxes (`POST /v1/sessions`, `GET /v1/sessions/{id}/stream`)
  * **[Environments API](https://platform.claude.com/docs/en/managed-agents/environments)** : Configure sandbox templates for agent sessions (`POST /v1/environments`, `GET /v1/environments`)

For the complete API reference with all endpoints, parameters, and response schemas, explore the API reference pages listed in the navigation. To access beta features, see [Beta headers](https://platform.claude.com/docs/en/api/beta-headers).
Authentication
For details on both authentication methods and when to use each, see [Authentication](https://platform.claude.com/docs/en/manage-claude/authentication). All requests to the Claude API must include these headers:  
| Header  | Value  | Required  |  
| --- | --- | --- |  
| `x-api-key`  | Your API key from Console  | One of `x-api-key` or `Authorization`  |  
| `Authorization`  |  `Bearer <token>`, where `<token>` is a short-lived access token obtained from `POST /v1/oauth/token` via [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation)  | One of `x-api-key` or `Authorization`  |  
| `anthropic-version`  | API version (for example, `2023-06-01`)  | Yes  |  
| `content-type`  | `application/json`  | Yes  |  
If you are using the [Client SDKs](https://platform.claude.com/docs/en/api/overview#client-sdks), the SDK will send these headers automatically. For API versioning details, see [API versions](https://platform.claude.com/docs/en/api/versioning).
When accessing Claude through a [cloud platform](https://platform.claude.com/docs/en/api/overview#claude-api-vs-cloud-platforms), authentication is integrated with the cloud provider's IAM system. See the platform-specific documentation for supported credential types, required headers, and authentication options.
### 
Getting API keys
The API is made available through the web [Console](https://platform.claude.com/). You can use the [Workbench](https://platform.claude.com/workbench) to try out the API in the browser and then generate API keys in [Account Settings](https://platform.claude.com/settings/keys). Use [workspaces](https://platform.claude.com/settings/workspaces) to segment your API keys and [control spend](https://platform.claude.com/docs/en/api/rate-limits) by use case.
Client SDKs
Anthropic provides official SDKs that simplify API integration by handling authentication, request formatting, error handling, and more.
**Benefits:**
  * Automatic header management (x-api-key, anthropic-version, content-type)
  * Type-safe request and response handling
  * Built-in retry logic and error handling
  * Streaming support
  * Request timeouts and connection management

For a list of client SDKs, see [Client SDKs](https://platform.claude.com/docs/en/cli-sdks-libraries/overview).
Claude API vs cloud platforms
Claude is available through the direct Claude API and through cloud platforms. Choose based on your infrastructure, feature availability, compliance requirements, and pricing preferences.
### 
Claude API
  * **Direct access** to the latest models and features
  * **Anthropic billing and support**
  * **Best for:** New integrations, full feature access, direct relationship with Anthropic

### 
Cloud platform APIs
Access Claude through AWS, Google Cloud, or Microsoft Azure:
  * **Integrated** with cloud provider billing and IAM
  * **Feature availability varies by platform:** Anthropic-operated platforms include [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws) and [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry); partner-operated platforms include Amazon Bedrock and Google Cloud. See each platform's page for feature availability and timing.
  * **Best for:** Existing cloud commitments, specific compliance requirements, consolidated cloud billing

  
| Platform  | Provider  | Documentation  |  
| --- | --- | --- |  
| Claude Platform on AWS  | AWS (Anthropic-operated)  | [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)  |  
| Amazon Bedrock  | AWS  | [Claude in Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)  |  
| Agent Platform  | Google Cloud  | [Claude on Google Cloud](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)  |  
| Microsoft Foundry  | Microsoft Azure (Anthropic-operated)  | [Claude in Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)  |  
Claude Managed Agents is available through the direct Claude API and [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws). For feature availability across platforms, see the [Features overview](https://platform.claude.com/docs/en/build-with-claude/overview).
Request and response format
### 
Request size limits  
| Endpoint  | Maximum request size  |  
| --- | --- |  
| Messages, Token Counting  | 32 MB  |  
| [Message Batches API](https://platform.claude.com/docs/en/build-with-claude/batch-processing)  | 256 MB  |  
| [Files API](https://platform.claude.com/docs/en/build-with-claude/files)  | 500 MB  |  
| Sessions, Agents, Environments  | 32 MB  |  
If you exceed these limits, you'll receive a 413 `request_too_large` error.
Partner-operated platforms have their own request size limits: Google Cloud limits requests to 30 MB, and Bedrock limits requests to 20 MB. Claude Platform on AWS uses the same limits as the direct Claude API. Consult your platform's documentation for current values.
### 
Response headers
The Claude API includes the following headers in every response:
  * `request-id`: A globally unique identifier for the request
  * `anthropic-organization-id`: The organization ID associated with the API key used in the request

Claude Platform on AWS adds an AWS request ID (`x-amzn-requestid`) alongside the standard `request-id` header. See [Request IDs](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#request-ids) for the dual-ID handling pattern.
Rate limits and availability
### 
Rate limits
The API enforces rate limits and spend limits to prevent misuse and manage capacity. Limits are organized into usage tiers that increase automatically as you use the API. Each tier has:
  * **Spend limits** : Maximum monthly cost for API usage
  * **Rate limits** : Maximum number of requests per minute (RPM) and tokens per minute (TPM)

You can view your organization's current limits in the [Console](https://platform.claude.com/settings/limits). For higher limits, contact sales through the Console.
For detailed information about limits, tiers, and the token bucket algorithm used for rate limiting, see [Rate limits](https://platform.claude.com/docs/en/api/rate-limits).
### 
Availability
The Claude API is available in [many countries and regions](https://platform.claude.com/docs/en/api/supported-regions) worldwide. Check the supported regions page to confirm availability in your location.
Next steps
[  Messages API reference Complete API specification for direct model interactions ](https://platform.claude.com/docs/en/api/messages/create)[ Claude Managed Agents reference Agents, Sessions, and Environments endpoints ](https://platform.claude.com/docs/en/managed-agents/sessions)[  Client SDKs Python, TypeScript, C#, Go, Java, PHP, and Ruby ](https://platform.claude.com/docs/en/cli-sdks-libraries/overview)[ Rate limits Usage tiers, spend limits, and token bucket algorithm ](https://platform.claude.com/docs/en/api/rate-limits)
