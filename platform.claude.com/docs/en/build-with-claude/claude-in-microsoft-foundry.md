<!-- source: https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry -->

# Claude in Microsoft Foundry
Access Claude models through Microsoft Foundry with Azure-native endpoints and authentication.
This guide walks you through the process of setting up and making API calls to Claude in Foundry using one of Anthropic's client SDKs or direct HTTP requests. When you can access Claude in Foundry, you are billed for Claude usage in the Microsoft Marketplace, allowing you to access Claude's latest capabilities while managing costs through your Azure subscription.
Regional availability: At launch, Claude is available as a Global Standard deployment type in Foundry resources. Pricing for Claude in the Microsoft Marketplace uses Anthropic's standard API pricing. Visit [Pricing](https://claude.com/pricing#api) for details.
Foundry is supported by the C#, Java, PHP, Python, and TypeScript SDKs. The Go and Ruby SDKs do not currently support Microsoft Foundry.
Preview
In this preview platform integration, Claude models run on Anthropic's infrastructure. This is a commercial integration for billing and access through Azure. As an independent processor for Microsoft, customers using Claude through Microsoft Foundry are subject to Anthropic's data use terms. Anthropic continues to provide its industry-leading safety and data commitments, including zero data retention availability.
Prerequisites
Before you begin, ensure you have:
  * An active Azure subscription
  * Access to [Foundry](https://ai.azure.com/)
  * The [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed (optional, for resource management)

Install an SDK
Anthropic's [client SDKs](https://platform.claude.com/docs/en/cli-sdks-libraries/overview) support Foundry through a platform-specific package or client class.
Python
Python
TypeScript
TypeScript
C#
C#
Java
Java
PHP
PHP

pip install -U "anthropic"

Provisioning
Foundry uses a two-level hierarchy: **resources** contain your security and billing configuration, while **deployments** are the model instances you call via API. You'll first create a Foundry resource, then create one or more Claude deployments within it.
### 
Provisioning Foundry resources
Create a Foundry resource, which is required to use and manage services in Azure. You can follow these instructions to create a [Foundry resource](https://learn.microsoft.com/en-us/azure/ai-services/multi-service-resource?pivots=azportal#create-a-new-azure-ai-foundry-resource). Alternatively, you can start by creating a [Foundry project](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/create-projects?tabs=ai-foundry), which involves creating a Foundry resource.
To provision your resource:
  1. Navigate to the [Foundry portal](https://ai.azure.com/)
  2. Create a new Foundry resource or select an existing one
  3. Configure access management using Azure-issued API keys or Entra ID (formerly Azure Active Directory) for role-based access control
  4. Optionally configure the resource to be part of a private network (Azure Virtual Network) for enhanced security
  5. Note your resource name. You'll use this as `{resource}` in API endpoints (for example, `https://{resource}.services.ai.azure.com/anthropic/v1/*`)

### 
Creating Foundry deployments
After creating your resource, deploy a Claude model to make it available for API calls:
  1. In the Foundry portal, navigate to your resource
  2. Go to **Models + endpoints** and select **+ Deploy model** > **Deploy base model**
  3. Search for and select a Claude model (for example, `claude-sonnet-4-6`)
  4. Configure deployment settings:
     * **Deployment name:** Defaults to the model ID, but you can customize it (for example, `my-claude-deployment`). The deployment name cannot be changed after it has been created.
     * **Deployment type:** Select Global Standard (recommended for Claude)
  5. Select **Deploy** and wait for provisioning to complete
  6. Once deployed, you can find your endpoint URL and keys under **Keys and Endpoint**

The deployment name you choose becomes the value you pass in the `model` parameter of your API requests. You can create multiple deployments of the same model with different names to manage separate configurations or rate limits.
Authentication
Claude in Foundry supports two authentication methods: API keys and Entra ID tokens. Both methods use Azure-hosted endpoints in the format `https://{resource}.services.ai.azure.com/anthropic/v1/*`.
### 
API key authentication
After provisioning your Foundry Claude resource, you can obtain an API key from the Foundry portal:
  1. Navigate to your resource in the Foundry portal
  2. Go to **Keys and Endpoint** section
  3. Copy one of the provided API keys
  4. Use either the `api-key` or `x-api-key` header in your requests, or provide it to the SDK

The Foundry SDKs require an API key and either a resource name or base URL. The C#, Java, PHP, Python, and TypeScript SDKs automatically read these from the following environment variables if they are defined:
  * `ANTHROPIC_FOUNDRY_API_KEY` - Your API key
  * `ANTHROPIC_FOUNDRY_RESOURCE` - Your resource name (for example, `example-resource`)
  * `ANTHROPIC_FOUNDRY_BASE_URL` - Alternative to resource name; the full base URL (for example, `https://example-resource.services.ai.azure.com/anthropic/`)

The `resource` and `base_url` parameters are mutually exclusive. Provide either the resource name (which the SDK uses to construct the URL as `https://{resource}.services.ai.azure.com/anthropic/`) or the full base URL directly.
**Example using API key:**
cURL
cURL
CLI
CLI
Python
Python
TypeScript
TypeScript
C#
C#
Java
Java
PHP
PHP
Ruby
Ruby

import os
from anthropic import AnthropicFoundry

client = AnthropicFoundry(
    api_key=os.environ.get("ANTHROPIC_FOUNDRY_API_KEY"),
    resource="example-resource",  # your resource name
)

message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}],
)
print(message.content)


Keep your API keys secure. Never commit them to version control or share them publicly. Anyone with access to your API key can make requests to Claude through your Foundry resource.
### 
Microsoft Entra authentication
For enhanced security and centralized access management, you can use Entra ID tokens:
  1. Enable Entra authentication for your Foundry resource
  2. Obtain an access token from Entra ID
  3. Use the token in the `Authorization: Bearer {TOKEN}` header

**Example using Entra ID:**
cURL
cURL
Python
Python
TypeScript
TypeScript
C#
C#
Java
Java
PHP
PHP
Ruby
Ruby

import os
from anthropic import AnthropicFoundry
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# Get Microsoft Entra ID token using token provider pattern
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

# Create client with Entra ID authentication
client = AnthropicFoundry(
    resource="example-resource",  # your resource name
    azure_ad_token_provider=token_provider,  # Use token provider for Entra ID auth
)

# Make request
message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}],
)
print(message.content)

Microsoft Entra ID authentication allows you to manage access using Azure RBAC, integrate with your organization's identity management, and avoid managing API keys manually.
Correlation request IDs
Foundry includes request identifiers in HTTP response headers for debugging and tracing. When contacting support, provide both the `request-id` and `apim-request-id` values to help teams quickly locate and investigate your request across both Anthropic and Azure systems.
Feature support
Claude in Foundry supports most of Claude's powerful features. You can find all the features currently supported in [Features overview](https://platform.claude.com/docs/en/build-with-claude/overview).
### 
Context window
Claude Fable 5, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6 have a [1M-token context window](https://platform.claude.com/docs/en/build-with-claude/context-windows) on Microsoft Foundry. Other Claude models, including Claude Opus 4.8 and Sonnet 4.5, have a 200k-token context window.
### 
Features not supported
  * Admin API
  * Compliance API
  * Models API
  * Message Batches API
  * Server-side fallback (the [`fallbacks` parameter](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#server-side-fallback); use the [client-side fallback pattern](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#client-side-fallback) instead)

API responses
API responses from Claude in Foundry follow the standard [Claude API response format](https://platform.claude.com/docs/en/api/messages/create). This includes the `usage` object in response bodies, which provides detailed token consumption information for your requests. The `usage` object is consistent across all platforms (Claude API, Foundry, Claude Platform on AWS, Amazon Bedrock, and Google Cloud).
For details on response headers specific to Foundry, see [Correlation request IDs](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#correlation-request-ids).
API model IDs and deployments
Lifecycle terms (Deprecated, Retired) are defined in [Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations). Microsoft Foundry follows the Claude API lifecycle schedule.
The following Claude models are available through Foundry. The latest generation models (Claude Fable 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 4.6, and Haiku 4.5) offer the most advanced capabilities:  
| Model  | Default deployment name  |  
| --- | --- |  
| Claude Fable 5  | claude-fable-5  |  
| Claude Opus 4.8  | claude-opus-4-8  |  
| Claude Opus 4.7  | claude-opus-4-7  |  
| Claude Opus 4.6  | claude-opus-4-6  |  
| Claude Opus 4.5  | claude-opus-4-5  |  
| Claude Opus 4.1   
Deprecated. Retiring August 5, 2026.  | claude-opus-4-1  |  
| Claude Sonnet 4.6  | claude-sonnet-4-6  |  
| Claude Sonnet 4.5  | claude-sonnet-4-5  |  
| Claude Haiku 4.5  | claude-haiku-4-5  |  
By default, deployment names match the model IDs shown in the preceding table. However, you can create custom deployments with different names in the Foundry portal to manage different configurations, versions, or rate limits. Use the deployment name (not necessarily the model ID) in your API requests.

Upgrading to a newer Claude model? In Claude Code, run `/claude-api migrate` to apply model ID swaps and breaking parameter changes across your codebase. The skill detects which cloud platform your code targets and adjusts model ID formats and feature changes for that platform. See [Migrating to a newer Claude model](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill#migrating-to-a-newer-claude-model).
Monitoring and logging
Azure provides comprehensive monitoring and logging capabilities for your Claude usage through standard Azure patterns:
  * **Azure Monitor:** Track API usage, latency, and error rates
  * **Azure Log Analytics:** Query and analyze request/response logs
  * **Cost Management:** Monitor and forecast costs associated with Claude usage

Anthropic recommends logging your activity on at least a 30-day rolling basis to understand usage patterns and investigate any potential issues.
Azure's logging services are configured within your Azure subscription. Enabling logging does not provide Microsoft or Anthropic access to your content beyond what's necessary for billing and service operation.
Troubleshooting
### 
Authentication errors
**Error:** `401 Unauthorized` or `Invalid API key`
  * **Solution:** Verify your API key is correct. You can obtain a new API key from the Foundry portal under **Keys and Endpoint** for your Foundry resource.
  * **Solution:** If using Microsoft Entra ID, ensure your access token is valid and hasn't expired. Tokens typically expire after 1 hour.

**Error:** `403 Forbidden`
  * **Solution:** Your Azure account may lack the necessary permissions. Ensure you have the appropriate Azure RBAC role assigned (for example, "Cognitive Services OpenAI User").

### 
Rate limiting
**Error:** `429 Too Many Requests`
  * **Solution:** You've exceeded your rate limit. Implement exponential backoff and retry logic in your application.
  * **Solution:** Consider requesting rate limit increases through the Azure portal or Azure support.

#### 
Rate limit headers
Foundry does not include Anthropic's standard rate limit headers (`anthropic-ratelimit-tokens-limit`, `anthropic-ratelimit-tokens-remaining`, `anthropic-ratelimit-tokens-reset`, `anthropic-ratelimit-input-tokens-limit`, `anthropic-ratelimit-input-tokens-remaining`, `anthropic-ratelimit-input-tokens-reset`, `anthropic-ratelimit-output-tokens-limit`, `anthropic-ratelimit-output-tokens-remaining`, and `anthropic-ratelimit-output-tokens-reset`) in responses. Manage rate limiting through Azure's monitoring tools instead.
### 
Model and deployment errors
**Error:** `Model not found` or `Deployment not found`
  * **Solution:** Verify you're using the correct deployment name. If you haven't created a custom deployment, use the default model ID (for example, `claude-sonnet-4-6`).
  * **Solution:** Ensure the model/deployment is available in your Azure region.

**Error:** `Invalid model parameter`
  * **Solution:** The model parameter should contain your deployment name, which can be customized in the Foundry portal. Verify the deployment exists and is properly configured.

[Claude Mythos Preview](https://anthropic.com/glasswing) is a research preview available to invited customers on Microsoft Foundry. For more information, see [Project Glasswing](https://anthropic.com/glasswing).
Additional resources
  * **Foundry documentation:** [ai.azure.com/catalog](https://ai.azure.com/catalog/publishers/anthropic)
  * **Azure pricing:** [azure.microsoft.com/en-us/pricing/details/ai-foundry](https://azure.microsoft.com/en-us/pricing/details/ai-foundry/#pricing)
  * **Anthropic pricing details:** [Model pricing](https://platform.claude.com/docs/en/about-claude/pricing#model-pricing)
  * **Authentication guide:** See [Authentication](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#authentication)
  * **Azure portal:** [portal.azure.com](https://portal.azure.com/)

  * [Preview](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#preview)
  * [Prerequisites](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#prerequisites)
  * [Install an SDK](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#install-an-sdk)
  * [Provisioning](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#provisioning)
  * [Provisioning Foundry resources](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#provisioning-foundry-resources)
  * [Creating Foundry deployments](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#creating-foundry-deployments)
  * [Authentication](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#authentication)
  * [API key authentication](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#api-key-authentication)
  * [Microsoft Entra authentication](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#microsoft-entra-authentication)
  * [Correlation request IDs](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#correlation-request-ids)
  * [Feature support](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#feature-support)
  * [Context window](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#context-window)
  * [Features not supported](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#features-not-supported)
  * [API responses](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#api-responses)
  * [API model IDs and deployments](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#api-model-ids-and-deployments)
  * [Monitoring and logging](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#monitoring-and-logging)
  * [Troubleshooting](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#troubleshooting)
  * [Authentication errors](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#authentication-errors)
  * [Rate limiting](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#rate-limiting)
  * [Model and deployment errors](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#model-and-deployment-errors)
  * [Additional resources](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#additional-resources)

Messages/Claude on cloud platforms
# Claude in Microsoft Foundry
Access Claude models through Microsoft Foundry with Azure-native endpoints and authentication.
This guide walks you through the process of setting up and making API calls to Claude in Foundry using one of Anthropic's client SDKs or direct HTTP requests. When you can access Claude in Foundry, you are billed for Claude usage in the Microsoft Marketplace, allowing you to access Claude's latest capabilities while managing costs through your Azure subscription.
Regional availability: At launch, Claude is available as a Global Standard deployment type in Foundry resources. Pricing for Claude in the Microsoft Marketplace uses Anthropic's standard API pricing. Visit [Pricing](https://claude.com/pricing#api) for details.
Foundry is supported by the C#, Java, PHP, Python, and TypeScript SDKs. The Go and Ruby SDKs do not currently support Microsoft Foundry.
Preview
In this preview platform integration, Claude models run on Anthropic's infrastructure. This is a commercial integration for billing and access through Azure. As an independent processor for Microsoft, customers using Claude through Microsoft Foundry are subject to Anthropic's data use terms. Anthropic continues to provide its industry-leading safety and data commitments, including zero data retention availability.
Prerequisites
Before you begin, ensure you have:
  * An active Azure subscription
  * Access to [Foundry](https://ai.azure.com/)
  * The [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed (optional, for resource management)

Install an SDK
Anthropic's [client SDKs](https://platform.claude.com/docs/en/cli-sdks-libraries/overview) support Foundry through a platform-specific package or client class.
Python
Python
TypeScript
TypeScript
C#
C#
Java
Java
PHP
PHP

pip install -U "anthropic"

Provisioning
Foundry uses a two-level hierarchy: **resources** contain your security and billing configuration, while **deployments** are the model instances you call via API. You'll first create a Foundry resource, then create one or more Claude deployments within it.
### 
Provisioning Foundry resources
Create a Foundry resource, which is required to use and manage services in Azure. You can follow these instructions to create a [Foundry resource](https://learn.microsoft.com/en-us/azure/ai-services/multi-service-resource?pivots=azportal#create-a-new-azure-ai-foundry-resource). Alternatively, you can start by creating a [Foundry project](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/create-projects?tabs=ai-foundry), which involves creating a Foundry resource.
To provision your resource:
  1. Navigate to the [Foundry portal](https://ai.azure.com/)
  2. Create a new Foundry resource or select an existing one
  3. Configure access management using Azure-issued API keys or Entra ID (formerly Azure Active Directory) for role-based access control
  4. Optionally configure the resource to be part of a private network (Azure Virtual Network) for enhanced security
  5. Note your resource name. You'll use this as `{resource}` in API endpoints (for example, `https://{resource}.services.ai.azure.com/anthropic/v1/*`)

### 
Creating Foundry deployments
After creating your resource, deploy a Claude model to make it available for API calls:
  1. In the Foundry portal, navigate to your resource
  2. Go to **Models + endpoints** and select **+ Deploy model** > **Deploy base model**
  3. Search for and select a Claude model (for example, `claude-sonnet-4-6`)
  4. Configure deployment settings:
     * **Deployment name:** Defaults to the model ID, but you can customize it (for example, `my-claude-deployment`). The deployment name cannot be changed after it has been created.
     * **Deployment type:** Select Global Standard (recommended for Claude)
  5. Select **Deploy** and wait for provisioning to complete
  6. Once deployed, you can find your endpoint URL and keys under **Keys and Endpoint**

The deployment name you choose becomes the value you pass in the `model` parameter of your API requests. You can create multiple deployments of the same model with different names to manage separate configurations or rate limits.
Authentication
Claude in Foundry supports two authentication methods: API keys and Entra ID tokens. Both methods use Azure-hosted endpoints in the format `https://{resource}.services.ai.azure.com/anthropic/v1/*`.
### 
API key authentication
After provisioning your Foundry Claude resource, you can obtain an API key from the Foundry portal:
  1. Navigate to your resource in the Foundry portal
  2. Go to **Keys and Endpoint** section
  3. Copy one of the provided API keys
  4. Use either the `api-key` or `x-api-key` header in your requests, or provide it to the SDK

The Foundry SDKs require an API key and either a resource name or base URL. The C#, Java, PHP, Python, and TypeScript SDKs automatically read these from the following environment variables if they are defined:
  * `ANTHROPIC_FOUNDRY_API_KEY` - Your API key
  * `ANTHROPIC_FOUNDRY_RESOURCE` - Your resource name (for example, `example-resource`)
  * `ANTHROPIC_FOUNDRY_BASE_URL` - Alternative to resource name; the full base URL (for example, `https://example-resource.services.ai.azure.com/anthropic/`)

The `resource` and `base_url` parameters are mutually exclusive. Provide either the resource name (which the SDK uses to construct the URL as `https://{resource}.services.ai.azure.com/anthropic/`) or the full base URL directly.
**Example using API key:**
cURL
cURL
CLI
CLI
Python
Python
TypeScript
TypeScript
C#
C#
Java
Java
PHP
PHP
Ruby
Ruby

import os
from anthropic import AnthropicFoundry

client = AnthropicFoundry(
    api_key=os.environ.get("ANTHROPIC_FOUNDRY_API_KEY"),
    resource="example-resource",  # your resource name
)

message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}],
)
print(message.content)


Keep your API keys secure. Never commit them to version control or share them publicly. Anyone with access to your API key can make requests to Claude through your Foundry resource.
### 
Microsoft Entra authentication
For enhanced security and centralized access management, you can use Entra ID tokens:
  1. Enable Entra authentication for your Foundry resource
  2. Obtain an access token from Entra ID
  3. Use the token in the `Authorization: Bearer {TOKEN}` header

**Example using Entra ID:**
cURL
cURL
Python
Python
TypeScript
TypeScript
C#
C#
Java
Java
PHP
PHP
Ruby
Ruby

import os
from anthropic import AnthropicFoundry
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# Get Microsoft Entra ID token using token provider pattern
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

# Create client with Entra ID authentication
client = AnthropicFoundry(
    resource="example-resource",  # your resource name
    azure_ad_token_provider=token_provider,  # Use token provider for Entra ID auth
)

# Make request
message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}],
)
print(message.content)

Microsoft Entra ID authentication allows you to manage access using Azure RBAC, integrate with your organization's identity management, and avoid managing API keys manually.
Correlation request IDs
Foundry includes request identifiers in HTTP response headers for debugging and tracing. When contacting support, provide both the `request-id` and `apim-request-id` values to help teams quickly locate and investigate your request across both Anthropic and Azure systems.
Feature support
Claude in Foundry supports most of Claude's powerful features. You can find all the features currently supported in [Features overview](https://platform.claude.com/docs/en/build-with-claude/overview).
### 
Context window
Claude Fable 5, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6 have a [1M-token context window](https://platform.claude.com/docs/en/build-with-claude/context-windows) on Microsoft Foundry. Other Claude models, including Claude Opus 4.8 and Sonnet 4.5, have a 200k-token context window.
### 
Features not supported
  * Admin API
  * Compliance API
  * Models API
  * Message Batches API
  * Server-side fallback (the [`fallbacks` parameter](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#server-side-fallback); use the [client-side fallback pattern](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#client-side-fallback) instead)

API responses
API responses from Claude in Foundry follow the standard [Claude API response format](https://platform.claude.com/docs/en/api/messages/create). This includes the `usage` object in response bodies, which provides detailed token consumption information for your requests. The `usage` object is consistent across all platforms (Claude API, Foundry, Claude Platform on AWS, Amazon Bedrock, and Google Cloud).
For details on response headers specific to Foundry, see [Correlation request IDs](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#correlation-request-ids).
API model IDs and deployments
Lifecycle terms (Deprecated, Retired) are defined in [Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations). Microsoft Foundry follows the Claude API lifecycle schedule.
The following Claude models are available through Foundry. The latest generation models (Claude Fable 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 4.6, and Haiku 4.5) offer the most advanced capabilities:  
| Model  | Default deployment name  |  
| --- | --- |  
| Claude Fable 5  | claude-fable-5  |  
| Claude Opus 4.8  | claude-opus-4-8  |  
| Claude Opus 4.7  | claude-opus-4-7  |  
| Claude Opus 4.6  | claude-opus-4-6  |  
| Claude Opus 4.5  | claude-opus-4-5  |  
| Claude Opus 4.1   
Deprecated. Retiring August 5, 2026.  | claude-opus-4-1  |  
| Claude Sonnet 4.6  | claude-sonnet-4-6  |  
| Claude Sonnet 4.5  | claude-sonnet-4-5  |  
| Claude Haiku 4.5  | claude-haiku-4-5  |  
By default, deployment names match the model IDs shown in the preceding table. However, you can create custom deployments with different names in the Foundry portal to manage different configurations, versions, or rate limits. Use the deployment name (not necessarily the model ID) in your API requests.

Upgrading to a newer Claude model? In Claude Code, run `/claude-api migrate` to apply model ID swaps and breaking parameter changes across your codebase. The skill detects which cloud platform your code targets and adjusts model ID formats and feature changes for that platform. See [Migrating to a newer Claude model](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill#migrating-to-a-newer-claude-model).
Monitoring and logging
Azure provides comprehensive monitoring and logging capabilities for your Claude usage through standard Azure patterns:
  * **Azure Monitor:** Track API usage, latency, and error rates
  * **Azure Log Analytics:** Query and analyze request/response logs
  * **Cost Management:** Monitor and forecast costs associated with Claude usage

Anthropic recommends logging your activity on at least a 30-day rolling basis to understand usage patterns and investigate any potential issues.
Azure's logging services are configured within your Azure subscription. Enabling logging does not provide Microsoft or Anthropic access to your content beyond what's necessary for billing and service operation.
Troubleshooting
### 
Authentication errors
**Error:** `401 Unauthorized` or `Invalid API key`
  * **Solution:** Verify your API key is correct. You can obtain a new API key from the Foundry portal under **Keys and Endpoint** for your Foundry resource.
  * **Solution:** If using Microsoft Entra ID, ensure your access token is valid and hasn't expired. Tokens typically expire after 1 hour.

**Error:** `403 Forbidden`
  * **Solution:** Your Azure account may lack the necessary permissions. Ensure you have the appropriate Azure RBAC role assigned (for example, "Cognitive Services OpenAI User").

### 
Rate limiting
**Error:** `429 Too Many Requests`
  * **Solution:** You've exceeded your rate limit. Implement exponential backoff and retry logic in your application.
  * **Solution:** Consider requesting rate limit increases through the Azure portal or Azure support.

#### 
Rate limit headers
Foundry does not include Anthropic's standard rate limit headers (`anthropic-ratelimit-tokens-limit`, `anthropic-ratelimit-tokens-remaining`, `anthropic-ratelimit-tokens-reset`, `anthropic-ratelimit-input-tokens-limit`, `anthropic-ratelimit-input-tokens-remaining`, `anthropic-ratelimit-input-tokens-reset`, `anthropic-ratelimit-output-tokens-limit`, `anthropic-ratelimit-output-tokens-remaining`, and `anthropic-ratelimit-output-tokens-reset`) in responses. Manage rate limiting through Azure's monitoring tools instead.
### 
Model and deployment errors
**Error:** `Model not found` or `Deployment not found`
  * **Solution:** Verify you're using the correct deployment name. If you haven't created a custom deployment, use the default model ID (for example, `claude-sonnet-4-6`).
  * **Solution:** Ensure the model/deployment is available in your Azure region.

**Error:** `Invalid model parameter`
  * **Solution:** The model parameter should contain your deployment name, which can be customized in the Foundry portal. Verify the deployment exists and is properly configured.

[Claude Mythos Preview](https://anthropic.com/glasswing) is a research preview available to invited customers on Microsoft Foundry. For more information, see [Project Glasswing](https://anthropic.com/glasswing).
Additional resources
  * **Foundry documentation:** [ai.azure.com/catalog](https://ai.azure.com/catalog/publishers/anthropic)
  * **Azure pricing:** [azure.microsoft.com/en-us/pricing/details/ai-foundry](https://azure.microsoft.com/en-us/pricing/details/ai-foundry/#pricing)
  * **Anthropic pricing details:** [Model pricing](https://platform.claude.com/docs/en/about-claude/pricing#model-pricing)
  * **Authentication guide:** See [Authentication](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#authentication)
  * **Azure portal:** [portal.azure.com](https://portal.azure.com/)
