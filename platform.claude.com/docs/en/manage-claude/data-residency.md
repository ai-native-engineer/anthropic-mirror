<!-- source: https://platform.claude.com/docs/en/manage-claude/data-residency -->

# Data residency
Manage where model inference runs and where data is stored with geographic controls.
This feature is eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
Data residency controls let you manage where your data is processed and stored. Two independent settings govern this:
  * **Inference geo:** Controls where model inference runs, on a per-request basis. Set through the `inference_geo` API parameter or as a workspace default.
  * **Workspace geo:** Controls where data is stored at rest and where endpoint processing (such as image transcoding and code execution) happens. Configured at the workspace level in the [Claude Console](https://platform.claude.com).

[Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) does not support the `inference_geo` parameter, but respects the Workspace geo configured in Console. With [self-hosted sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes), tool execution and the sandbox filesystem stay on infrastructure you control.
Inference geo
The `inference_geo` parameter controls where model inference runs for a specific API request. Add it to any `POST /v1/messages` call.  
| Value  | Description  |  
| --- | --- |  
| `"global"`  | Default. Inference may run in any available geography for optimal performance and availability.  |  
| `"us"`  | Inference runs only in US-based infrastructure.  |  
### 
API usage
cURLCLIPythonTypeScript

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    inference_geo="us",
    messages=[
        {"role": "user", "content": "Summarize the key points of this document."}
    ],
)

print(response.content[0].text)
# Check where inference actually ran
print(f"Inference geo: {response.usage.inference_geo}")

### 
Response
The response `usage` object includes an `inference_geo` field indicating where inference ran:
Output

  "usage": {
    "input_tokens": 25,
    "output_tokens": 150,
    "inference_geo": "us"

### 
Model availability
The `inference_geo` parameter is supported on Claude Opus 4.6, Claude Sonnet 4.6, and later models. Requests with `inference_geo` on Claude Opus 4.5, Claude Sonnet 4.5, Claude Haiku 4.5, or earlier models return a 400 error.
The `inference_geo` parameter is available on the Claude API (first-party) and [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws). On Amazon Bedrock, Google Cloud, and Microsoft Foundry, the inference region is determined by the endpoint URL or inference profile, so `inference_geo` is not applicable. The `inference_geo` parameter is also not available through the [OpenAI SDK compatibility endpoint](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk).
### 
Workspace-level restrictions
Workspace settings also support restricting which inference geos are available:
  * **`allowed_inference_geos`:** Restricts which geos a workspace can use. If a request specifies an `inference_geo` not in this list, the API returns an error.
  * **`default_inference_geo`:** Sets the fallback geo when `inference_geo` is omitted from a request. Individual requests can override this by setting `inference_geo` explicitly.

These settings can be configured through the Console or the [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api) under the `data_residency` field.
Workspace geo
Workspace geo is set when you create a workspace and can't be changed afterwards. Currently, `"us"` is the only available workspace geo.
To set workspace geo, create a new workspace in the [Console](https://platform.claude.com):
  1. Go to **Settings** > **Workspaces**.
  2. Create a new workspace.
  3. Select the workspace geo.

**Claude Platform on AWS:** Workspace geo is not configurable. Workspaces are provisioned through the AWS Console, and the Claude Console Workspaces page is read-only. Claude Managed Agents sessions on this platform run with an effective Workspace geo of `"us"`, which is currently the only available workspace geo. See [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws) for data residency considerations specific to that platform.
Pricing
Data residency pricing varies by model generation:
  * **Claude Opus 4.6, Claude Sonnet 4.6, and later:** US-only inference (`inference_geo: "us"`) is priced at 1.1x the standard rate across all token pricing categories (input tokens, output tokens, cache writes, and cache reads).
  * **Global routing** (`inference_geo: "global"`): Standard pricing applies.
  * **Older models:** Don't support `inference_geo` (see [Model availability](https://platform.claude.com/docs/en/manage-claude/data-residency#model-availability)); standard pricing applies. Requests that include the parameter return a 400 error.

This pricing applies to the Claude API (first-party) and Claude Platform on AWS. Partner-operated platforms (Bedrock and Google Cloud) have their own regional pricing. See [Data residency pricing](https://platform.claude.com/docs/en/about-claude/pricing#data-residency-pricing) for details.
If you have a [Priority Tier](https://platform.claude.com/docs/en/api/service-tiers) commitment, the 1.1x multiplier for US-only inference also affects how tokens are counted against your Priority Tier capacity. Each token consumed with `inference_geo: "us"` draws down 1.1 tokens from your committed TPM, consistent with how other pricing multipliers (such as prompt caching) affect burndown rates.
Batch API support
The `inference_geo` parameter is supported on the [Batch API](https://platform.claude.com/docs/en/build-with-claude/batch-processing). Each request in a batch can specify its own `inference_geo` value.
Migration from legacy opt-outs
If your organization previously opted out of global routing to keep inference in the US, your workspace has been automatically configured with `allowed_inference_geos: ["us"]` and `default_inference_geo: "us"`. No code changes are required. Your existing data residency requirements continue to be enforced through the new geo controls.
### 
What changed
The legacy opt-out was an organization-level setting that restricted all requests to US-based infrastructure. The new data residency controls replace this with two mechanisms:
  * **Per-request control:** The `inference_geo` parameter lets you specify `"us"` or `"global"` on each API call, giving you request-level flexibility.
  * **Workspace controls:** The `default_inference_geo` and `allowed_inference_geos` settings in the Console let you enforce geo policies across all keys in a workspace.

### 
What happened to your workspace
Your workspace was migrated automatically:  
| Legacy setting  | New equivalent  |  
| --- | --- |  
| Global routing opt-out (US only)  |  `allowed_inference_geos: ["us"]`, `default_inference_geo: "us"`  |  
All API requests using keys from your workspace continue to run on US-based infrastructure. No action is needed to maintain your current behavior.
### 
If you want to use global routing
If your data residency requirements have changed and you want to take advantage of global routing for better performance and availability, update your workspace's inference geo settings to include `"global"` in the allowed geos and set `default_inference_geo` to `"global"`. See [Workspace-level restrictions](https://platform.claude.com/docs/en/manage-claude/data-residency#workspace-level-restrictions) for details.
### 
Pricing impact
Legacy models are unaffected by this migration. For current pricing on newer models, see [Pricing](https://platform.claude.com/docs/en/manage-claude/data-residency#pricing).
Current limitations
  * **Shared rate limits:** Rate limits are shared across all geos.
  * **Inference geo:** Only `"us"` and `"global"` are available.
  * **Workspace geo:** Only `"us"` is currently available. Workspace geo can't be changed after workspace creation.

Next steps
[ Pricing View data residency pricing details. ](https://platform.claude.com/docs/en/about-claude/pricing#data-residency-pricing)[ Workspaces Learn about workspace configuration. ](https://platform.claude.com/docs/en/manage-claude/workspaces)[  Usage and Cost API Track usage and costs by data residency. ](https://platform.claude.com/docs/en/manage-claude/usage-cost-api)
  * [Inference geo](https://platform.claude.com/docs/en/manage-claude/data-residency#inference-geo)
  * [API usage](https://platform.claude.com/docs/en/manage-claude/data-residency#api-usage)
  * [Response](https://platform.claude.com/docs/en/manage-claude/data-residency#response)
  * [Model availability](https://platform.claude.com/docs/en/manage-claude/data-residency#model-availability)
  * [Workspace-level restrictions](https://platform.claude.com/docs/en/manage-claude/data-residency#workspace-level-restrictions)
  * [Workspace geo](https://platform.claude.com/docs/en/manage-claude/data-residency#workspace-geo)
  * [Pricing](https://platform.claude.com/docs/en/manage-claude/data-residency#pricing)
  * [Batch API support](https://platform.claude.com/docs/en/manage-claude/data-residency#batch-api-support)
  * [Migration from legacy opt-outs](https://platform.claude.com/docs/en/manage-claude/data-residency#migration-from-legacy-opt-outs)
  * [What changed](https://platform.claude.com/docs/en/manage-claude/data-residency#what-changed)
  * [What happened to your workspace](https://platform.claude.com/docs/en/manage-claude/data-residency#what-happened-to-your-workspace)
  * [If you want to use global routing](https://platform.claude.com/docs/en/manage-claude/data-residency#if-you-want-to-use-global-routing)
  * [Pricing impact](https://platform.claude.com/docs/en/manage-claude/data-residency#pricing-impact)
  * [Current limitations](https://platform.claude.com/docs/en/manage-claude/data-residency#current-limitations)
  * [Next steps](https://platform.claude.com/docs/en/manage-claude/data-residency#next-steps)

Admin/Data & compliance
# Data residency
Manage where model inference runs and where data is stored with geographic controls.
This feature is eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
Data residency controls let you manage where your data is processed and stored. Two independent settings govern this:
  * **Inference geo:** Controls where model inference runs, on a per-request basis. Set through the `inference_geo` API parameter or as a workspace default.
  * **Workspace geo:** Controls where data is stored at rest and where endpoint processing (such as image transcoding and code execution) happens. Configured at the workspace level in the [Claude Console](https://platform.claude.com).

[Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) does not support the `inference_geo` parameter, but respects the Workspace geo configured in Console. With [self-hosted sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes), tool execution and the sandbox filesystem stay on infrastructure you control.
Inference geo
The `inference_geo` parameter controls where model inference runs for a specific API request. Add it to any `POST /v1/messages` call.  
| Value  | Description  |  
| --- | --- |  
| `"global"`  | Default. Inference may run in any available geography for optimal performance and availability.  |  
| `"us"`  | Inference runs only in US-based infrastructure.  |  
### 
API usage
cURLCLIPythonTypeScript

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    inference_geo="us",
    messages=[
        {"role": "user", "content": "Summarize the key points of this document."}
    ],
)

print(response.content[0].text)
# Check where inference actually ran
print(f"Inference geo: {response.usage.inference_geo}")

### 
Response
The response `usage` object includes an `inference_geo` field indicating where inference ran:
Output

  "usage": {
    "input_tokens": 25,
    "output_tokens": 150,
    "inference_geo": "us"

### 
Model availability
The `inference_geo` parameter is supported on Claude Opus 4.6, Claude Sonnet 4.6, and later models. Requests with `inference_geo` on Claude Opus 4.5, Claude Sonnet 4.5, Claude Haiku 4.5, or earlier models return a 400 error.
The `inference_geo` parameter is available on the Claude API (first-party) and [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws). On Amazon Bedrock, Google Cloud, and Microsoft Foundry, the inference region is determined by the endpoint URL or inference profile, so `inference_geo` is not applicable. The `inference_geo` parameter is also not available through the [OpenAI SDK compatibility endpoint](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk).
### 
Workspace-level restrictions
Workspace settings also support restricting which inference geos are available:
  * **`allowed_inference_geos`:** Restricts which geos a workspace can use. If a request specifies an `inference_geo` not in this list, the API returns an error.
  * **`default_inference_geo`:** Sets the fallback geo when `inference_geo` is omitted from a request. Individual requests can override this by setting `inference_geo` explicitly.

These settings can be configured through the Console or the [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api) under the `data_residency` field.
Workspace geo
Workspace geo is set when you create a workspace and can't be changed afterwards. Currently, `"us"` is the only available workspace geo.
To set workspace geo, create a new workspace in the [Console](https://platform.claude.com):
  1. Go to **Settings** > **Workspaces**.
  2. Create a new workspace.
  3. Select the workspace geo.

**Claude Platform on AWS:** Workspace geo is not configurable. Workspaces are provisioned through the AWS Console, and the Claude Console Workspaces page is read-only. Claude Managed Agents sessions on this platform run with an effective Workspace geo of `"us"`, which is currently the only available workspace geo. See [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws) for data residency considerations specific to that platform.
Pricing
Data residency pricing varies by model generation:
  * **Claude Opus 4.6, Claude Sonnet 4.6, and later:** US-only inference (`inference_geo: "us"`) is priced at 1.1x the standard rate across all token pricing categories (input tokens, output tokens, cache writes, and cache reads).
  * **Global routing** (`inference_geo: "global"`): Standard pricing applies.
  * **Older models:** Don't support `inference_geo` (see [Model availability](https://platform.claude.com/docs/en/manage-claude/data-residency#model-availability)); standard pricing applies. Requests that include the parameter return a 400 error.

This pricing applies to the Claude API (first-party) and Claude Platform on AWS. Partner-operated platforms (Bedrock and Google Cloud) have their own regional pricing. See [Data residency pricing](https://platform.claude.com/docs/en/about-claude/pricing#data-residency-pricing) for details.
If you have a [Priority Tier](https://platform.claude.com/docs/en/api/service-tiers) commitment, the 1.1x multiplier for US-only inference also affects how tokens are counted against your Priority Tier capacity. Each token consumed with `inference_geo: "us"` draws down 1.1 tokens from your committed TPM, consistent with how other pricing multipliers (such as prompt caching) affect burndown rates.
Batch API support
The `inference_geo` parameter is supported on the [Batch API](https://platform.claude.com/docs/en/build-with-claude/batch-processing). Each request in a batch can specify its own `inference_geo` value.
Migration from legacy opt-outs
If your organization previously opted out of global routing to keep inference in the US, your workspace has been automatically configured with `allowed_inference_geos: ["us"]` and `default_inference_geo: "us"`. No code changes are required. Your existing data residency requirements continue to be enforced through the new geo controls.
### 
What changed
The legacy opt-out was an organization-level setting that restricted all requests to US-based infrastructure. The new data residency controls replace this with two mechanisms:
  * **Per-request control:** The `inference_geo` parameter lets you specify `"us"` or `"global"` on each API call, giving you request-level flexibility.
  * **Workspace controls:** The `default_inference_geo` and `allowed_inference_geos` settings in the Console let you enforce geo policies across all keys in a workspace.

### 
What happened to your workspace
Your workspace was migrated automatically:  
| Legacy setting  | New equivalent  |  
| --- | --- |  
| Global routing opt-out (US only)  |  `allowed_inference_geos: ["us"]`, `default_inference_geo: "us"`  |  
All API requests using keys from your workspace continue to run on US-based infrastructure. No action is needed to maintain your current behavior.
### 
If you want to use global routing
If your data residency requirements have changed and you want to take advantage of global routing for better performance and availability, update your workspace's inference geo settings to include `"global"` in the allowed geos and set `default_inference_geo` to `"global"`. See [Workspace-level restrictions](https://platform.claude.com/docs/en/manage-claude/data-residency#workspace-level-restrictions) for details.
### 
Pricing impact
Legacy models are unaffected by this migration. For current pricing on newer models, see [Pricing](https://platform.claude.com/docs/en/manage-claude/data-residency#pricing).
Current limitations
  * **Shared rate limits:** Rate limits are shared across all geos.
  * **Inference geo:** Only `"us"` and `"global"` are available.
  * **Workspace geo:** Only `"us"` is currently available. Workspace geo can't be changed after workspace creation.

Next steps
[ Pricing View data residency pricing details. ](https://platform.claude.com/docs/en/about-claude/pricing#data-residency-pricing)[ Workspaces Learn about workspace configuration. ](https://platform.claude.com/docs/en/manage-claude/workspaces)[  Usage and Cost API Track usage and costs by data residency. ](https://platform.claude.com/docs/en/manage-claude/usage-cost-api)
