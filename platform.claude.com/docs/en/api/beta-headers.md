<!-- source: https://platform.claude.com/docs/en/api/beta-headers -->

# Beta headers
Documentation for using beta headers with the Claude API
Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API.
These features are subject to change and may be modified or removed in future releases.
Beta headers are often used in conjunction with the `beta` namespace exposed by each [client SDK](https://platform.claude.com/docs/en/cli-sdks-libraries/overview).
How to use beta headers
To access beta features, include the `anthropic-beta` header in your API requests:

POST /v1/messages
Content-Type: application/json
X-API-Key: YOUR_API_KEY
anthropic-beta: BETA_FEATURE_NAME

When using the SDK, you can specify beta headers in the request options:
cURLCLIPythonTypeScript

client = Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    betas=["files-api-2025-04-14"],
)


Beta features are experimental and may:
  * Have breaking changes with notice
  * Be deprecated or removed
  * Have different rate limits or pricing
  * Not be available in all regions

### 
Multiple beta features
To use multiple beta features in a single request, include all feature names in the header separated by commas:

anthropic-beta: feature1,feature2,feature3

### 
Endpoint-specific headers
Some beta features are scoped to specific endpoints rather than individual request parameters and require a feature-specific beta header on every request:  
| Endpoints  | Beta header  |  
| --- | --- |  
|  `/v1/agents`, `/v1/sessions`, `/v1/environments`  | `managed-agents-2026-04-01`  |  
See the [Managed Agents overview](https://platform.claude.com/docs/en/managed-agents/overview) for details.
### 
Version naming conventions
Beta feature names typically follow the pattern: `feature-name-YYYY-MM-DD`, where the date indicates when the beta version was released. Always use the exact beta feature name as documented.
Error handling
If you use an invalid or unavailable beta header, you'll receive an error response:
Output

  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "Unsupported beta header: invalid-beta-name"

Getting help
For questions about beta features:
  1. Check the documentation for the specific feature
  2. Review the [API changelog](https://platform.claude.com/docs/en/api/versioning) for updates
  3. Contact support for assistance with production usage

Remember that beta features are provided "as-is" and may not have the same SLA guarantees as stable API features.
  * [How to use beta headers](https://platform.claude.com/docs/en/api/beta-headers#how-to-use-beta-headers)
  * [Multiple beta features](https://platform.claude.com/docs/en/api/beta-headers#multiple-beta-features)
  * [Endpoint-specific headers](https://platform.claude.com/docs/en/api/beta-headers#endpoint-specific-headers)
  * [Version naming conventions](https://platform.claude.com/docs/en/api/beta-headers#version-naming-conventions)
  * [Error handling](https://platform.claude.com/docs/en/api/beta-headers#error-handling)
  * [Getting help](https://platform.claude.com/docs/en/api/beta-headers#getting-help)

API reference/Using the API
# Beta headers
Documentation for using beta headers with the Claude API
Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API.
These features are subject to change and may be modified or removed in future releases.
Beta headers are often used in conjunction with the `beta` namespace exposed by each [client SDK](https://platform.claude.com/docs/en/cli-sdks-libraries/overview).
How to use beta headers
To access beta features, include the `anthropic-beta` header in your API requests:

POST /v1/messages
Content-Type: application/json
X-API-Key: YOUR_API_KEY
anthropic-beta: BETA_FEATURE_NAME

When using the SDK, you can specify beta headers in the request options:
cURLCLIPythonTypeScript

client = Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    betas=["files-api-2025-04-14"],
)


Beta features are experimental and may:
  * Have breaking changes with notice
  * Be deprecated or removed
  * Have different rate limits or pricing
  * Not be available in all regions

### 
Multiple beta features
To use multiple beta features in a single request, include all feature names in the header separated by commas:

anthropic-beta: feature1,feature2,feature3

### 
Endpoint-specific headers
Some beta features are scoped to specific endpoints rather than individual request parameters and require a feature-specific beta header on every request:  
| Endpoints  | Beta header  |  
| --- | --- |  
|  `/v1/agents`, `/v1/sessions`, `/v1/environments`  | `managed-agents-2026-04-01`  |  
See the [Managed Agents overview](https://platform.claude.com/docs/en/managed-agents/overview) for details.
### 
Version naming conventions
Beta feature names typically follow the pattern: `feature-name-YYYY-MM-DD`, where the date indicates when the beta version was released. Always use the exact beta feature name as documented.
Error handling
If you use an invalid or unavailable beta header, you'll receive an error response:
Output

  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "Unsupported beta header: invalid-beta-name"

Getting help
For questions about beta features:
  1. Check the documentation for the specific feature
  2. Review the [API changelog](https://platform.claude.com/docs/en/api/versioning) for updates
  3. Contact support for assistance with production usage

Remember that beta features are provided "as-is" and may not have the same SLA guarantees as stable API features.
