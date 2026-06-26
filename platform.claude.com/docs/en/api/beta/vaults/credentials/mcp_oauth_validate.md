<!-- source: https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate -->

# Validate Credential
POST/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate
Validate Credential
##### Path ParametersExpand Collapse 
vault_id: string
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#mcp_oauth_validate.vault_id)
credential_id: string
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#mcp_oauth_validate.credential_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#mcp_oauth_validate.betas)
BetaManagedAgentsCredentialValidation object { credential_id, has_refresh_token, mcp_probe, 5 more } 
Result of live-probing a credential against its configured MCP server.
credential_id: string
Unique identifier of the credential that was validated.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_credential_validation.credential_id)
has_refresh_token: boolean
Whether the credential has a refresh token configured.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_credential_validation.has_refresh_token)
mcp_probe: [BetaManagedAgentsMCPProbe](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_probe) { http_response, method } 
The failing step of an MCP validation probe.
http_response: [BetaManagedAgentsRefreshHTTPResponse](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_refresh_http_response) { body, body_truncated, content_type, status_code } 
An HTTP response captured during a credential validation probe.
body: string
Response body. May be truncated and has sensitive values scrubbed.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_mcp_probe.http_response%20%2B%20\(resource\)%20beta.vaults.credentials.body)
body_truncated: boolean
Whether `body` was truncated.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_mcp_probe.http_response%20%2B%20\(resource\)%20beta.vaults.credentials.body_truncated)
content_type: string
Value of the `Content-Type` response header.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_mcp_probe.http_response%20%2B%20\(resource\)%20beta.vaults.credentials.content_type)
status_code: number
HTTP status code.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_mcp_probe.http_response%20%2B%20\(resource\)%20beta.vaults.credentials.status_code)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_credential_validation.mcp_probe%20%2B%20\(resource\)%20beta.vaults.credentials.http_response)
method: string
The MCP method that failed (for example `initialize` or `tools/list`).
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_credential_validation.mcp_probe%20%2B%20\(resource\)%20beta.vaults.credentials.method)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_credential_validation.mcp_probe)
refresh: [BetaManagedAgentsRefreshObject](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_refresh_object) { http_response, status } 
Outcome of a refresh-token exchange attempted during credential validation.
http_response: [BetaManagedAgentsRefreshHTTPResponse](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_refresh_http_response) { body, body_truncated, content_type, status_code } 
An HTTP response captured during a credential validation probe.
body: string
Response body. May be truncated and has sensitive values scrubbed.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_refresh_object.http_response%20%2B%20\(resource\)%20beta.vaults.credentials.body)
body_truncated: boolean
Whether `body` was truncated.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_refresh_object.http_response%20%2B%20\(resource\)%20beta.vaults.credentials.body_truncated)
content_type: string
Value of the `Content-Type` response header.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_refresh_object.http_response%20%2B%20\(resource\)%20beta.vaults.credentials.content_type)
status_code: number
HTTP status code.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_refresh_object.http_response%20%2B%20\(resource\)%20beta.vaults.credentials.status_code)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_credential_validation.refresh%20%2B%20\(resource\)%20beta.vaults.credentials.http_response)
status: "succeeded" or "failed" or "connect_error" or "no_refresh_token"
Outcome of a refresh-token exchange attempted during credential validation.
"succeeded"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_credential_validation.refresh%20%2B%20\(resource\)%20beta.vaults.credentials.status%5B0%5D)
"failed"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_credential_validation.refresh%20%2B%20\(resource\)%20beta.vaults.credentials.status%5B1%5D)
"connect_error"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_credential_validation.refresh%20%2B%20\(resource\)%20beta.vaults.credentials.status%5B2%5D)
"no_refresh_token"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_credential_validation.refresh%20%2B%20\(resource\)%20beta.vaults.credentials.status%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_credential_validation.refresh%20%2B%20\(resource\)%20beta.vaults.credentials.status)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_credential_validation.refresh)
status: [BetaManagedAgentsCredentialValidationStatus](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_credential_validation_status)
Overall verdict of a credential validation probe.
"valid"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_credential_validation.status%20%2B%20\(resource\)%20beta.vaults.credentials%5B0%5D)
"invalid"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_credential_validation.status%20%2B%20\(resource\)%20beta.vaults.credentials%5B1%5D)
"unknown"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_credential_validation.status%20%2B%20\(resource\)%20beta.vaults.credentials%5B2%5D)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_credential_validation.status)
type: "vault_credential_validation"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_credential_validation.type)
validated_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_credential_validation.validated_at)
vault_id: string
Identifier of the vault containing the credential.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_credential_validation.vault_id)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/mcp_oauth_validate#beta_managed_agents_credential_validation)
Validate Credential
cURL

curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID/mcp_oauth_validate \
    -X POST \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"

  "credential_id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "has_refresh_token": true,
  "mcp_probe": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    "method": "method"
  "refresh": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    "status": "succeeded"
  "status": "valid",
  "type": "vault_credential_validation",
  "validated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv"

  "credential_id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "has_refresh_token": true,
  "mcp_probe": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    "method": "method"
  "refresh": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    "status": "succeeded"
  "status": "valid",
  "type": "vault_credential_validation",
  "validated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv"
