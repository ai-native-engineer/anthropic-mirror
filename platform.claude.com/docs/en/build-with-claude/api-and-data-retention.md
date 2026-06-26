<!-- source: https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention -->

# API and data retention
Learn about how Anthropic's APIs and associated features retain data, including information about zero data retention (ZDR) and HIPAA-ready API access.
Information about Anthropic's standard retention policies is set out in [Anthropic's commercial data retention policy](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data) and [consumer data retention policy](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data).
Anthropic offers two data handling arrangements for the Claude API:
  * **Zero data retention (ZDR):** Customer data is not stored at rest after the API response is returned, except where needed to comply with law or combat misuse.
  * **HIPAA readiness:** For organizations handling protected health information (PHI), Anthropic offers HIPAA-ready API access with a signed Business Associate Agreement (BAA). See [HIPAA readiness](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#hipaa-readiness).

Anthropic's approach to data retention
Different APIs and features have different storage and retention needs. Where an API or feature doesn't require storage of customer prompts or responses, it may be eligible for ZDR. Where an API or feature necessarily requires storage of customer prompts or responses, Anthropic designs for the smallest possible retention footprint. For these features:
  * Retained data is never used for model training without your express permission.
  * Only what is technically necessary for the API and feature to work is retained. Conversation content (your prompts and Claude's outputs) is not retained by default. Certain models require 30-day data retention; see [Model-specific data retention requirements](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#model-specific-data-retention-requirements).
  * Data is purged on the shortest practical TTL, and Anthropic aims to give customers control over how long data is retained. What is held, and the retention duration where a specific TTL applies, is documented on each feature's page.

Data accessible through the [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api) follows its own retention model. The [Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed) retains data for 6 years. Chat, file, and project content from claude.ai follows your organization's retention policy, set in [claude.ai > Organization settings > Data and privacy](https://claude.ai/admin-settings/data-privacy-controls).
In the [feature eligibility table](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#feature-eligibility), some features are marked "Yes (qualified)" in the ZDR eligible column. If your organization has a ZDR arrangement, you can use these features with confidence that what Anthropic retains is narrow and is required for optimal performance.
Zero data retention (ZDR) scope

Claude Fable 5 and Claude Mythos 5 are not available under ZDR; see [Model-specific data retention requirements](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#model-specific-data-retention-requirements).
**What ZDR covers**
  * **Certain Claude APIs:** ZDR applies to the Claude Messages and Token Counting APIs.
  * **Claude Code:** ZDR applies when used with Commercial organization API keys or through Claude Enterprise (see [Claude Code ZDR docs](https://code.claude.com/docs/en/zero-data-retention))

**What ZDR does NOT cover**
  * **Console and Workbench:** Any usage on Console or Workbench
  * **Claude Managed Agents:** Claude Managed Agents is a stateful resource. You can delete session transcripts, but there is no automatic deletion.
  * **Claude consumer products:** Claude Free, Pro, or Max plans, including when customers on those plans use Claude's web, desktop, or mobile apps or Claude Code
  * **Claude Teams and Claude Enterprise:** Claude Teams and Claude Enterprise product interfaces are **not ZDR-eligible** , except for Claude Code when used through Claude Enterprise with ZDR enabled for the organization. For other product interfaces, only Commercial organization API keys are eligible for ZDR.
  * **Third-party integrations:** Data processed by third-party websites, tools, or other integrations is **not ZDR-eligible** , though some may have similar offerings. When using external services in conjunction with the Claude API, make sure to review those services' data handling practices.

For the most up-to-date information on what products and features are ZDR-eligible, refer to your contract terms or contact your Anthropic account representative.
Model-specific data retention requirements
Claude Fable 5 and Claude Mythos 5 are designated [Covered Models](https://support.claude.com/en/articles/15425695) and require 30-day data retention. Zero data retention is not available for Claude Fable 5 or Claude Mythos 5. Requests to either model from an organization whose data retention configuration does not meet this requirement return a `400 invalid_request_error`.
This requirement applies on the Claude API. For Claude Fable 5 on Amazon Bedrock, Google Cloud, and Microsoft Foundry, data retention requirements are set by each platform.
Organizations with a ZDR arrangement can configure data retention at the workspace level in [Claude Console > Settings > Workspaces](https://platform.claude.com/settings/workspaces): open a workspace's **Privacy controls** tab and turn on 30-day data retention for that workspace. This makes Claude Fable 5 and Claude Mythos 5 available in the designated workspace while the organization's other workspaces keep zero data retention. Workspaces without an override follow the organization default.
HIPAA readiness
The Claude API supports HIPAA-ready integrations for organizations that handle protected health information (PHI). With a signed BAA and a HIPAA-enabled organization, you can use supported API features to process PHI while supporting your organization's HIPAA compliance.
Previously, organizations that required HIPAA readiness for the Claude API needed to enable ZDR. HIPAA-ready API access removes this requirement and provides a foundation for Anthropic to progressively enable additional features as they are audited for HIPAA readiness.
This page covers HIPAA readiness for the Claude API. For the full HIPAA Implementation Guide covering Claude Enterprise and configuration requirements, see the [Anthropic Trust Center](https://trust.anthropic.com/resources).
### 
Getting started
To set up HIPAA-ready API access:
  1. 1
Sign a Business Associate Agreement
Contact the [Anthropic sales team](https://claude.com/contact-sales) to sign a BAA that covers API usage.
  2. 2
Provision a HIPAA-enabled organization
Anthropic provisions a dedicated organization with HIPAA readiness controls enabled. This organization automatically enforces feature restrictions, blocking API requests that use non-eligible features.
  3. 3
Build with eligible features
Use the [feature eligibility table](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#feature-eligibility) to confirm which features are supported. Review the [PHI handling guidelines](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#phi-handling-guidelines) for features that require specific restrictions on where PHI can appear. For detailed configuration and compliance requirements, refer to the [HIPAA Implementation Guide](https://trust.anthropic.com/resources).


HIPAA readiness is enforced at the organization level. If you need both HIPAA-ready and general-purpose API access, use separate organizations for each.
### 
HIPAA readiness scope
**What HIPAA readiness covers**
  * **Claude API:** HIPAA readiness applies to the Claude API (`api.anthropic.com`) for eligible features listed in the [feature eligibility table](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#feature-eligibility).

**What HIPAA readiness does NOT cover**
  * **Claude consumer products:** Claude Free, Pro, or Max plans
  * **Console and Workbench:** Usage through the Claude Console interface
  * **Partner-operated platforms:** Amazon Bedrock or Google Cloud (refer to those platforms' compliance documentation)
  * **Claude Platform on AWS and Microsoft Foundry:** HIPAA readiness is not available
  * **Third-party integrations:** Data processed by external tools or services connected to your application
  * **Claude Code:** Claude Code is not covered under HIPAA readiness
  * **Beta features:** Features in beta are generally not covered under the BAA unless explicitly listed as eligible in the [feature eligibility table](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#feature-eligibility)

### 
PHI handling guidelines
Protected health information (PHI) includes any individually identifiable health information. In the context of the Claude API, PHI typically appears in:
  * Message content (prompts and responses from Claude)
  * Attached files (images, PDFs)
  * File names and metadata associated with message content

The following fields are not expected to contain PHI under the BAA: workspace names, user information (name, email, phone number), billing data, and support tickets.
#### 
Schema and tool definition restrictions
When using [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) or tools with `strict: true`, the API compiles JSON schemas into grammars that are cached separately from message content. These cached schemas do not receive the same PHI protections as prompts and responses.
**Do not include PHI in JSON schema definitions.** This restriction applies to:
  * Schema property names
  * `enum` values
  * `const` values
  * `pattern` regular expressions

Patient-specific information should only appear in message content, where it is protected under HIPAA safeguards.
### 
HIPAA error handling
Your signed BAA is the official source of truth for which features are covered. The API also enforces these restrictions automatically: when a HIPAA-enabled organization sends a request that includes a non-eligible feature, the API returns a `400` error to prevent accidental use of features not covered by your BAA:

  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "The requested features are not available for HIPAA-regulated organizations without Zero Data Retention: code_execution."

The error message lists the non-eligible features detected in the request. Remove these features from your request and retry.
Feature eligibility
The following table lists which Claude API features are eligible for ZDR and HIPAA readiness arrangements. For HIPAA-enabled organizations, features marked "No" in the HIPAA column are automatically blocked, and requests that include them return a `400` error.  
| Feature  | Endpoint  | ZDR eligible  | HIPAA eligible  | Details  |  
| --- | --- | --- | --- | --- |  
| [Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)  | `/v1/messages`  | Yes  | Yes  | Standard API calls for generating Claude responses.  |  
| [Token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting)  | `/v1/messages/count_tokens`  | Yes  | Yes  | Count tokens before sending requests.  |  
| [Web search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)  |  `/v1/messages` (with `web_search` tool)  |  Yes1  |  Yes1  | Real-time web search results returned in the API response.  |  
| [Web fetch](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)  |  `/v1/messages` (with `web_fetch` tool)  |  Yes1 2  | No  | Fetched web content returned in the API response.  |  
| [Advisor tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)  |  `/v1/messages` (with `advisor` tool)  | Yes  | No  | Advisor model output is returned in the API response; nothing is stored server-side after the response.  |  
| [Memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)  |  `/v1/messages` (with `memory` tool)  | Yes  | Yes  | Client-side memory storage where you control data retention.  |  
| [Context management (compaction)](https://platform.claude.com/docs/en/build-with-claude/compaction)  |  `/v1/messages` (with `context_management`)  | Yes  | No  | Server-side compaction results are returned/round-tripped statelessly through the API response.  |  
| [Context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing)  |  `/v1/messages` (with `context_management`)  | Yes  | No  | Context edits (tool use clearing + thinking clearing) are applied in real time.  |  
| [Fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode)  |  `/v1/messages` (with `speed: "fast"`)  | Yes  | Yes  | Same Messages API endpoint with faster inference. ZDR applies regardless of speed setting.  |  
| [1M token context window](https://platform.claude.com/docs/en/build-with-claude/context-windows)  | `/v1/messages`  | Yes  | Yes  | Extended context processing uses the standard Messages API.  |  
| [Adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)  | `/v1/messages`  | Yes  | Yes  | Dynamic thinking depth uses the standard Messages API.  |  
| [Citations](https://platform.claude.com/docs/en/build-with-claude/citations)  | `/v1/messages`  | Yes  | Yes  | Source attribution uses the standard Messages API.  |  
| [Data residency](https://platform.claude.com/docs/en/manage-claude/data-residency)  |  `/v1/messages` (with `inference_geo`)  | Yes  | Yes  | Geographic routing uses the standard Messages API.  |  
| [Effort](https://platform.claude.com/docs/en/build-with-claude/effort)  |  `/v1/messages` (with `effort`)  | Yes  | Yes  | Token efficiency control uses the standard Messages API.  |  
| [Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)  |  `/v1/messages` (with `thinking`)  | Yes  | Yes  | Step-by-step reasoning uses the standard Messages API.  |  
| [PDF support](https://platform.claude.com/docs/en/build-with-claude/pdf-support)  | `/v1/messages`  | Yes  | Yes  | PDF document processing uses the standard Messages API. HIPAA eligibility applies to PDFs sent inline via the Messages API, not through the Files API.  |  
| [Search results](https://platform.claude.com/docs/en/build-with-claude/search-results)  |  `/v1/messages` (with `search_results` source)  | Yes  | Yes  | RAG citation support uses the standard Messages API.  |  
| [Bash tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool)  |  `/v1/messages` (with `bash` tool)  | Yes  | Yes  | Client-side tool executed in your environment.  |  
| [Text editor tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool)  |  `/v1/messages` (with `text_editor` tool)  | Yes  | Yes  | Client-side tool executed in your environment.  |  
| [Computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)  |  `/v1/messages` (with `computer` tool)  | Yes  | No  | Client-side tool where screenshots and files are captured and stored in your environment, not by Anthropic. See [Computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#data-retention).  |  
| [Fine-grained tool streaming](https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)  | `/v1/messages`  | Yes  | Yes  | Streaming tool parameters uses the standard Messages API.  |  
| [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)  | `/v1/messages`  | Yes  | Yes  | Your prompts and Claude's outputs are not stored. KV cache representations and cryptographic hashes are held in memory for the cache TTL and promptly deleted after expiry. See [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#data-retention).  |  
| [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)  | `/v1/messages`  | Yes (qualified)  |  Yes3  | Your prompts and Claude's outputs are not stored. Only the JSON schema is cached, for up to 24 hours since last use. This also covers [strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use) (`strict: true` on tools), which uses the same grammar pipeline. See [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs#data-retention).  |  
| [Cache diagnostics](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics)  |  `/v1/messages` (with `diagnostics`)  | Yes (qualified)  | No  | Your prompts and Claude's outputs are not stored. A fingerprint of cryptographic hashes and token-count estimates is retained briefly to enable comparison against the next request. See [Cache diagnostics](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics#data-retention).  |  
| [Tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)  |  `/v1/messages` (with `tool_search` tool)  | Yes  | No  | Tool search uses the standard Messages API.  |  
| [Batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing)  | `/v1/messages/batches`  | No  | No  | 29-day retention; async storage required. See [Batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing#data-retention).  |  
| [Code execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)  |  `/v1/messages` (with `code_execution` tool)  | No  | No  | Container data retained up to 30 days. See [Code execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#data-retention).  |  
| [Programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)  |  `/v1/messages` (with `code_execution` tool)  | No  | No  | Built on code execution containers; data retained up to 30 days. See [Programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#data-retention).  |  
| [Files API](https://platform.claude.com/docs/en/build-with-claude/files)  | `/v1/files`  | No  | No  | Files retained until explicitly deleted. See [Files API](https://platform.claude.com/docs/en/build-with-claude/files#data-retention).  |  
| [Agent skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)  |  `/v1/messages` (with `skills`) / `/v1/skills`  | No  | No  | Skill data retained per standard policy. See [Agent skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#data-retention).  |  
| [MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)  |  `/v1/messages` (with `mcp_servers`)  | No  | No  | Data retained per standard policy. See [MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector#data-retention).  |  
| [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview)  |  `/v1/agents`, `/v1/sessions`, `/v1/environments`  | No  | No  | Sessions are stateful resources; transcripts persist until you delete them. Applies to all Managed Agents sub-features, including [Self-hosted sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes).  |  
| [MCP tunnels](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview)  | `/v1/organizations/tunnels`  | No  | No  | Research preview. See [MCP tunnels security](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/security) for the data-flow boundary and subprocessor details.  |  
1 [Dynamic filtering](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#dynamic-filtering) is not eligible for ZDR or HIPAA.
2 While web fetch is ZDR-eligible, website publishers may retain request data (such as fetched URLs and request metadata) according to their own policies.
3 PHI must not be included in JSON schema definitions. See [PHI handling guidelines](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#phi-handling-guidelines).
Limitations and exclusions
### 
CORS not supported for ZDR
**Cross-Origin Resource Sharing (CORS)** is not supported for organizations with ZDR arrangements. If you need to make API calls from browser-based applications, you must:
  * Use a backend proxy server to make API calls on behalf of your front end
  * Implement your own CORS handling on the proxy server
  * Never expose API keys directly in browser JavaScript

### 
Data retention for policy violations and where required by law
Even with ZDR or HIPAA arrangements in place, Anthropic may retain data where required by law or to combat Usage Policy violations and malicious uses of Anthropic's platform. As a result, if a chat or session is flagged for such a violation, Anthropic may retain inputs and outputs for up to 2 years.
Frequently asked questions
### How do I know if my organization has ZDR arrangements?
### Can I use ZDR-eligible (qualified) features under my ZDR arrangement?
### What happens if I use a feature marked "No" under ZDR?
### Can I request deletion of data from features that are not ZDR-eligible?
### How does HIPAA readiness differ from ZDR?
### Do I still need ZDR if I have HIPAA readiness?
### What happens if I use a non-eligible feature under HIPAA?
### Can I use the same organization for HIPAA and non-HIPAA workloads?
### How do I request HIPAA-ready API access?
### Does this apply to Amazon Bedrock or Google Cloud?
### Is Claude Platform on AWS eligible for ZDR or HIPAA readiness?
### Is Claude Code eligible for ZDR?
### Does Claude for Excel support ZDR?
### How do I request ZDR?
Related resources
  * [Privacy Policy](https://www.anthropic.com/legal/privacy)
  * [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
  * [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
  * [Batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing)
  * [Files API](https://platform.claude.com/docs/en/api/files-create)
  * [Trust Center](https://trust.anthropic.com/resources)

  * [Anthropic's approach to data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#anthropics-approach-to-data-retention)
  * [Zero data retention (ZDR) scope](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#zero-data-retention-zdr-scope)
  * [Model-specific data retention requirements](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#model-specific-data-retention-requirements)
  * [HIPAA readiness](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#hipaa-readiness)
  * [Getting started](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#getting-started)
  * [HIPAA readiness scope](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#hipaa-readiness-scope)
  * [PHI handling guidelines](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#phi-handling-guidelines)
  * [HIPAA error handling](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#hipaa-error-handling)
  * [Feature eligibility](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#feature-eligibility)
  * [Limitations and exclusions](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#limitations-and-exclusions)
  * [CORS not supported for ZDR](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#cors-not-supported-for-zdr)
  * [Data retention for policy violations and where required by law](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#data-retention-for-policy-violations-and-where-required-by-law)
  * [Frequently asked questions](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#frequently-asked-questions)
  * [Related resources](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#related-resources)

Admin/Data & compliance
# API and data retention
Learn about how Anthropic's APIs and associated features retain data, including information about zero data retention (ZDR) and HIPAA-ready API access.
Information about Anthropic's standard retention policies is set out in [Anthropic's commercial data retention policy](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data) and [consumer data retention policy](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data).
Anthropic offers two data handling arrangements for the Claude API:
  * **Zero data retention (ZDR):** Customer data is not stored at rest after the API response is returned, except where needed to comply with law or combat misuse.
  * **HIPAA readiness:** For organizations handling protected health information (PHI), Anthropic offers HIPAA-ready API access with a signed Business Associate Agreement (BAA). See [HIPAA readiness](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#hipaa-readiness).

Anthropic's approach to data retention
Different APIs and features have different storage and retention needs. Where an API or feature doesn't require storage of customer prompts or responses, it may be eligible for ZDR. Where an API or feature necessarily requires storage of customer prompts or responses, Anthropic designs for the smallest possible retention footprint. For these features:
  * Retained data is never used for model training without your express permission.
  * Only what is technically necessary for the API and feature to work is retained. Conversation content (your prompts and Claude's outputs) is not retained by default. Certain models require 30-day data retention; see [Model-specific data retention requirements](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#model-specific-data-retention-requirements).
  * Data is purged on the shortest practical TTL, and Anthropic aims to give customers control over how long data is retained. What is held, and the retention duration where a specific TTL applies, is documented on each feature's page.

Data accessible through the [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api) follows its own retention model. The [Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed) retains data for 6 years. Chat, file, and project content from claude.ai follows your organization's retention policy, set in [claude.ai > Organization settings > Data and privacy](https://claude.ai/admin-settings/data-privacy-controls).
In the [feature eligibility table](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#feature-eligibility), some features are marked "Yes (qualified)" in the ZDR eligible column. If your organization has a ZDR arrangement, you can use these features with confidence that what Anthropic retains is narrow and is required for optimal performance.
Zero data retention (ZDR) scope

Claude Fable 5 and Claude Mythos 5 are not available under ZDR; see [Model-specific data retention requirements](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#model-specific-data-retention-requirements).
**What ZDR covers**
  * **Certain Claude APIs:** ZDR applies to the Claude Messages and Token Counting APIs.
  * **Claude Code:** ZDR applies when used with Commercial organization API keys or through Claude Enterprise (see [Claude Code ZDR docs](https://code.claude.com/docs/en/zero-data-retention))

**What ZDR does NOT cover**
  * **Console and Workbench:** Any usage on Console or Workbench
  * **Claude Managed Agents:** Claude Managed Agents is a stateful resource. You can delete session transcripts, but there is no automatic deletion.
  * **Claude consumer products:** Claude Free, Pro, or Max plans, including when customers on those plans use Claude's web, desktop, or mobile apps or Claude Code
  * **Claude Teams and Claude Enterprise:** Claude Teams and Claude Enterprise product interfaces are **not ZDR-eligible** , except for Claude Code when used through Claude Enterprise with ZDR enabled for the organization. For other product interfaces, only Commercial organization API keys are eligible for ZDR.
  * **Third-party integrations:** Data processed by third-party websites, tools, or other integrations is **not ZDR-eligible** , though some may have similar offerings. When using external services in conjunction with the Claude API, make sure to review those services' data handling practices.

For the most up-to-date information on what products and features are ZDR-eligible, refer to your contract terms or contact your Anthropic account representative.
Model-specific data retention requirements
Claude Fable 5 and Claude Mythos 5 are designated [Covered Models](https://support.claude.com/en/articles/15425695) and require 30-day data retention. Zero data retention is not available for Claude Fable 5 or Claude Mythos 5. Requests to either model from an organization whose data retention configuration does not meet this requirement return a `400 invalid_request_error`.
This requirement applies on the Claude API. For Claude Fable 5 on Amazon Bedrock, Google Cloud, and Microsoft Foundry, data retention requirements are set by each platform.
Organizations with a ZDR arrangement can configure data retention at the workspace level in [Claude Console > Settings > Workspaces](https://platform.claude.com/settings/workspaces): open a workspace's **Privacy controls** tab and turn on 30-day data retention for that workspace. This makes Claude Fable 5 and Claude Mythos 5 available in the designated workspace while the organization's other workspaces keep zero data retention. Workspaces without an override follow the organization default.
HIPAA readiness
The Claude API supports HIPAA-ready integrations for organizations that handle protected health information (PHI). With a signed BAA and a HIPAA-enabled organization, you can use supported API features to process PHI while supporting your organization's HIPAA compliance.
Previously, organizations that required HIPAA readiness for the Claude API needed to enable ZDR. HIPAA-ready API access removes this requirement and provides a foundation for Anthropic to progressively enable additional features as they are audited for HIPAA readiness.
This page covers HIPAA readiness for the Claude API. For the full HIPAA Implementation Guide covering Claude Enterprise and configuration requirements, see the [Anthropic Trust Center](https://trust.anthropic.com/resources).
### 
Getting started
To set up HIPAA-ready API access:
  1. 1
Sign a Business Associate Agreement
Contact the [Anthropic sales team](https://claude.com/contact-sales) to sign a BAA that covers API usage.
  2. 2
Provision a HIPAA-enabled organization
Anthropic provisions a dedicated organization with HIPAA readiness controls enabled. This organization automatically enforces feature restrictions, blocking API requests that use non-eligible features.
  3. 3
Build with eligible features
Use the [feature eligibility table](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#feature-eligibility) to confirm which features are supported. Review the [PHI handling guidelines](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#phi-handling-guidelines) for features that require specific restrictions on where PHI can appear. For detailed configuration and compliance requirements, refer to the [HIPAA Implementation Guide](https://trust.anthropic.com/resources).


HIPAA readiness is enforced at the organization level. If you need both HIPAA-ready and general-purpose API access, use separate organizations for each.
### 
HIPAA readiness scope
**What HIPAA readiness covers**
  * **Claude API:** HIPAA readiness applies to the Claude API (`api.anthropic.com`) for eligible features listed in the [feature eligibility table](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#feature-eligibility).

**What HIPAA readiness does NOT cover**
  * **Claude consumer products:** Claude Free, Pro, or Max plans
  * **Console and Workbench:** Usage through the Claude Console interface
  * **Partner-operated platforms:** Amazon Bedrock or Google Cloud (refer to those platforms' compliance documentation)
  * **Claude Platform on AWS and Microsoft Foundry:** HIPAA readiness is not available
  * **Third-party integrations:** Data processed by external tools or services connected to your application
  * **Claude Code:** Claude Code is not covered under HIPAA readiness
  * **Beta features:** Features in beta are generally not covered under the BAA unless explicitly listed as eligible in the [feature eligibility table](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#feature-eligibility)

### 
PHI handling guidelines
Protected health information (PHI) includes any individually identifiable health information. In the context of the Claude API, PHI typically appears in:
  * Message content (prompts and responses from Claude)
  * Attached files (images, PDFs)
  * File names and metadata associated with message content

The following fields are not expected to contain PHI under the BAA: workspace names, user information (name, email, phone number), billing data, and support tickets.
#### 
Schema and tool definition restrictions
When using [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) or tools with `strict: true`, the API compiles JSON schemas into grammars that are cached separately from message content. These cached schemas do not receive the same PHI protections as prompts and responses.
**Do not include PHI in JSON schema definitions.** This restriction applies to:
  * Schema property names
  * `enum` values
  * `const` values
  * `pattern` regular expressions

Patient-specific information should only appear in message content, where it is protected under HIPAA safeguards.
### 
HIPAA error handling
Your signed BAA is the official source of truth for which features are covered. The API also enforces these restrictions automatically: when a HIPAA-enabled organization sends a request that includes a non-eligible feature, the API returns a `400` error to prevent accidental use of features not covered by your BAA:

  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "The requested features are not available for HIPAA-regulated organizations without Zero Data Retention: code_execution."

The error message lists the non-eligible features detected in the request. Remove these features from your request and retry.
Feature eligibility
The following table lists which Claude API features are eligible for ZDR and HIPAA readiness arrangements. For HIPAA-enabled organizations, features marked "No" in the HIPAA column are automatically blocked, and requests that include them return a `400` error.  
| Feature  | Endpoint  | ZDR eligible  | HIPAA eligible  | Details  |  
| --- | --- | --- | --- | --- |  
| [Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)  | `/v1/messages`  | Yes  | Yes  | Standard API calls for generating Claude responses.  |  
| [Token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting)  | `/v1/messages/count_tokens`  | Yes  | Yes  | Count tokens before sending requests.  |  
| [Web search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)  |  `/v1/messages` (with `web_search` tool)  |  Yes1  |  Yes1  | Real-time web search results returned in the API response.  |  
| [Web fetch](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)  |  `/v1/messages` (with `web_fetch` tool)  |  Yes1 2  | No  | Fetched web content returned in the API response.  |  
| [Advisor tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)  |  `/v1/messages` (with `advisor` tool)  | Yes  | No  | Advisor model output is returned in the API response; nothing is stored server-side after the response.  |  
| [Memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)  |  `/v1/messages` (with `memory` tool)  | Yes  | Yes  | Client-side memory storage where you control data retention.  |  
| [Context management (compaction)](https://platform.claude.com/docs/en/build-with-claude/compaction)  |  `/v1/messages` (with `context_management`)  | Yes  | No  | Server-side compaction results are returned/round-tripped statelessly through the API response.  |  
| [Context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing)  |  `/v1/messages` (with `context_management`)  | Yes  | No  | Context edits (tool use clearing + thinking clearing) are applied in real time.  |  
| [Fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode)  |  `/v1/messages` (with `speed: "fast"`)  | Yes  | Yes  | Same Messages API endpoint with faster inference. ZDR applies regardless of speed setting.  |  
| [1M token context window](https://platform.claude.com/docs/en/build-with-claude/context-windows)  | `/v1/messages`  | Yes  | Yes  | Extended context processing uses the standard Messages API.  |  
| [Adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)  | `/v1/messages`  | Yes  | Yes  | Dynamic thinking depth uses the standard Messages API.  |  
| [Citations](https://platform.claude.com/docs/en/build-with-claude/citations)  | `/v1/messages`  | Yes  | Yes  | Source attribution uses the standard Messages API.  |  
| [Data residency](https://platform.claude.com/docs/en/manage-claude/data-residency)  |  `/v1/messages` (with `inference_geo`)  | Yes  | Yes  | Geographic routing uses the standard Messages API.  |  
| [Effort](https://platform.claude.com/docs/en/build-with-claude/effort)  |  `/v1/messages` (with `effort`)  | Yes  | Yes  | Token efficiency control uses the standard Messages API.  |  
| [Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)  |  `/v1/messages` (with `thinking`)  | Yes  | Yes  | Step-by-step reasoning uses the standard Messages API.  |  
| [PDF support](https://platform.claude.com/docs/en/build-with-claude/pdf-support)  | `/v1/messages`  | Yes  | Yes  | PDF document processing uses the standard Messages API. HIPAA eligibility applies to PDFs sent inline via the Messages API, not through the Files API.  |  
| [Search results](https://platform.claude.com/docs/en/build-with-claude/search-results)  |  `/v1/messages` (with `search_results` source)  | Yes  | Yes  | RAG citation support uses the standard Messages API.  |  
| [Bash tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool)  |  `/v1/messages` (with `bash` tool)  | Yes  | Yes  | Client-side tool executed in your environment.  |  
| [Text editor tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool)  |  `/v1/messages` (with `text_editor` tool)  | Yes  | Yes  | Client-side tool executed in your environment.  |  
| [Computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)  |  `/v1/messages` (with `computer` tool)  | Yes  | No  | Client-side tool where screenshots and files are captured and stored in your environment, not by Anthropic. See [Computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#data-retention).  |  
| [Fine-grained tool streaming](https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)  | `/v1/messages`  | Yes  | Yes  | Streaming tool parameters uses the standard Messages API.  |  
| [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)  | `/v1/messages`  | Yes  | Yes  | Your prompts and Claude's outputs are not stored. KV cache representations and cryptographic hashes are held in memory for the cache TTL and promptly deleted after expiry. See [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#data-retention).  |  
| [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)  | `/v1/messages`  | Yes (qualified)  |  Yes3  | Your prompts and Claude's outputs are not stored. Only the JSON schema is cached, for up to 24 hours since last use. This also covers [strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use) (`strict: true` on tools), which uses the same grammar pipeline. See [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs#data-retention).  |  
| [Cache diagnostics](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics)  |  `/v1/messages` (with `diagnostics`)  | Yes (qualified)  | No  | Your prompts and Claude's outputs are not stored. A fingerprint of cryptographic hashes and token-count estimates is retained briefly to enable comparison against the next request. See [Cache diagnostics](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics#data-retention).  |  
| [Tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)  |  `/v1/messages` (with `tool_search` tool)  | Yes  | No  | Tool search uses the standard Messages API.  |  
| [Batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing)  | `/v1/messages/batches`  | No  | No  | 29-day retention; async storage required. See [Batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing#data-retention).  |  
| [Code execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)  |  `/v1/messages` (with `code_execution` tool)  | No  | No  | Container data retained up to 30 days. See [Code execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#data-retention).  |  
| [Programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)  |  `/v1/messages` (with `code_execution` tool)  | No  | No  | Built on code execution containers; data retained up to 30 days. See [Programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#data-retention).  |  
| [Files API](https://platform.claude.com/docs/en/build-with-claude/files)  | `/v1/files`  | No  | No  | Files retained until explicitly deleted. See [Files API](https://platform.claude.com/docs/en/build-with-claude/files#data-retention).  |  
| [Agent skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)  |  `/v1/messages` (with `skills`) / `/v1/skills`  | No  | No  | Skill data retained per standard policy. See [Agent skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#data-retention).  |  
| [MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)  |  `/v1/messages` (with `mcp_servers`)  | No  | No  | Data retained per standard policy. See [MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector#data-retention).  |  
| [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview)  |  `/v1/agents`, `/v1/sessions`, `/v1/environments`  | No  | No  | Sessions are stateful resources; transcripts persist until you delete them. Applies to all Managed Agents sub-features, including [Self-hosted sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes).  |  
| [MCP tunnels](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview)  | `/v1/organizations/tunnels`  | No  | No  | Research preview. See [MCP tunnels security](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/security) for the data-flow boundary and subprocessor details.  |  
1 [Dynamic filtering](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#dynamic-filtering) is not eligible for ZDR or HIPAA.
2 While web fetch is ZDR-eligible, website publishers may retain request data (such as fetched URLs and request metadata) according to their own policies.
3 PHI must not be included in JSON schema definitions. See [PHI handling guidelines](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#phi-handling-guidelines).
Limitations and exclusions
### 
CORS not supported for ZDR
**Cross-Origin Resource Sharing (CORS)** is not supported for organizations with ZDR arrangements. If you need to make API calls from browser-based applications, you must:
  * Use a backend proxy server to make API calls on behalf of your front end
  * Implement your own CORS handling on the proxy server
  * Never expose API keys directly in browser JavaScript

### 
Data retention for policy violations and where required by law
Even with ZDR or HIPAA arrangements in place, Anthropic may retain data where required by law or to combat Usage Policy violations and malicious uses of Anthropic's platform. As a result, if a chat or session is flagged for such a violation, Anthropic may retain inputs and outputs for up to 2 years.
Frequently asked questions
### How do I know if my organization has ZDR arrangements?
### Can I use ZDR-eligible (qualified) features under my ZDR arrangement?
### What happens if I use a feature marked "No" under ZDR?
### Can I request deletion of data from features that are not ZDR-eligible?
### How does HIPAA readiness differ from ZDR?
### Do I still need ZDR if I have HIPAA readiness?
### What happens if I use a non-eligible feature under HIPAA?
### Can I use the same organization for HIPAA and non-HIPAA workloads?
### How do I request HIPAA-ready API access?
### Does this apply to Amazon Bedrock or Google Cloud?
### Is Claude Platform on AWS eligible for ZDR or HIPAA readiness?
### Is Claude Code eligible for ZDR?
### Does Claude for Excel support ZDR?
### How do I request ZDR?
Related resources
  * [Privacy Policy](https://www.anthropic.com/legal/privacy)
  * [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
  * [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
  * [Batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing)
  * [Files API](https://platform.claude.com/docs/en/api/files-create)
  * [Trust Center](https://trust.anthropic.com/resources)
