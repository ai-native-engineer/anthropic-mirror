<!-- source: https://platform.claude.com/docs/en/api/beta/vaults/credentials/update -->

# Update Credential
POST/v1/vaults/{vault_id}/credentials/{credential_id}
Update Credential
##### Path ParametersExpand Collapse 
vault_id: string
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#update.vault_id)
credential_id: string
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#update.credential_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#update.betas)
#####  Body ParametersJSONExpand Collapse 
auth: optional [BetaManagedAgentsMCPOAuthUpdateParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_oauth_update_params) { type, access_token, expires_at, refresh }  or [BetaManagedAgentsStaticBearerUpdateParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_static_bearer_update_params) { type, token }  or [BetaManagedAgentsEnvironmentVariableUpdateParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_environment_variable_update_params) { type, networking, secret_value } 
Updated authentication details for a credential.
BetaManagedAgentsMCPOAuthUpdateParams object { type, access_token, expires_at, refresh } 
Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.
type: "mcp_oauth"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_update_params.type)
access_token: optional string
Updated OAuth access token.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_update_params.access_token)
expires_at: optional string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_update_params.expires_at)
refresh: optional [BetaManagedAgentsMCPOAuthRefreshUpdateParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_oauth_refresh_update_params) { refresh_token, scope, token_endpoint_auth } 
Parameters for updating OAuth refresh token configuration.
refresh_token: optional string
Updated OAuth refresh token.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_update_params.refresh%20%2B%20\(resource\)%20beta.vaults.credentials.refresh_token)
scope: optional string
Updated OAuth scope for the refresh request.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_update_params.refresh%20%2B%20\(resource\)%20beta.vaults.credentials.scope)
token_endpoint_auth: optional [BetaManagedAgentsTokenEndpointAuthBasicUpdateParam](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_token_endpoint_auth_basic_update_param) { type, client_secret }  or [BetaManagedAgentsTokenEndpointAuthPostUpdateParam](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_token_endpoint_auth_post_update_param) { type, client_secret } 
Updated HTTP Basic authentication parameters for the token endpoint.
BetaManagedAgentsTokenEndpointAuthBasicUpdateParam object { type, client_secret } 
Updated HTTP Basic authentication parameters for the token endpoint.
type: "client_secret_basic"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_update_params.refresh%20%2B%20\(resource\)%20beta.vaults.credentials.type)
client_secret: optional string
Updated OAuth client secret.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_update_params.refresh%20%2B%20\(resource\)%20beta.vaults.credentials.client_secret)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_update_params.refresh%20%2B%20\(resource\)%20beta.vaults.credentials)
BetaManagedAgentsTokenEndpointAuthPostUpdateParam object { type, client_secret } 
Updated POST body authentication parameters for the token endpoint.
type: "client_secret_post"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_update_params.refresh%20%2B%20\(resource\)%20beta.vaults.credentials.type)
client_secret: optional string
Updated OAuth client secret.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_update_params.refresh%20%2B%20\(resource\)%20beta.vaults.credentials.client_secret)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_update_params.refresh%20%2B%20\(resource\)%20beta.vaults.credentials)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_update_params.refresh%20%2B%20\(resource\)%20beta.vaults.credentials.token_endpoint_auth)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_update_params.refresh)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_update_params)
BetaManagedAgentsStaticBearerUpdateParams object { type, token } 
Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.
type: "static_bearer"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_static_bearer_update_params.type)
token: optional string
Updated static bearer token value.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_static_bearer_update_params.token)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_static_bearer_update_params)
BetaManagedAgentsEnvironmentVariableUpdateParams object { type, networking, secret_value } 
Parameters for updating an environment variable credential. `secret_name` is immutable.
type: "environment_variable"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_environment_variable_update_params.type)
networking: optional [BetaManagedAgentsCredentialNetworkingParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_credential_networking_params)
Updated networking scope. Full replacement.
BetaManagedAgentsUnrestrictedCredentialNetworkingParams object { type } 
Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.
type: "unrestricted"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_environment_variable_update_params.networking%20%2B%20\(resource\)%20beta.vaults.credentials.type)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_environment_variable_update_params.networking%20%2B%20\(resource\)%20beta.vaults.credentials)
BetaManagedAgentsLimitedCredentialNetworkingParams object { allowed_hosts, type } 
Substitute the secret only on requests to the listed hosts.
allowed_hosts: array of string
Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_environment_variable_update_params.networking%20%2B%20\(resource\)%20beta.vaults.credentials.allowed_hosts)
type: "limited"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_environment_variable_update_params.networking%20%2B%20\(resource\)%20beta.vaults.credentials.type)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_environment_variable_update_params.networking%20%2B%20\(resource\)%20beta.vaults.credentials)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_environment_variable_update_params.networking)
secret_value: optional string
Updated secret value.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_environment_variable_update_params.secret_value)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_environment_variable_update_params)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#update.auth)
display_name: optional string
Updated human-readable name for the credential. 1-255 characters.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#update.display_name)
metadata: optional map[string]
Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#update.metadata)
BetaManagedAgentsCredential object { id, archived_at, auth, 6 more } 
A credential stored in a vault. Sensitive fields are never returned in responses.
Unique identifier for the credential.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_credential.id)
archived_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_credential.archived_at)
auth: [BetaManagedAgentsMCPOAuthAuthResponse](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_oauth_auth_response) { mcp_server_url, type, expires_at, refresh }  or [BetaManagedAgentsStaticBearerAuthResponse](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_static_bearer_auth_response) { mcp_server_url, type }  or [BetaManagedAgentsEnvironmentVariableAuthResponse](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_environment_variable_auth_response) { networking, secret_name, type } 
Authentication details for a credential.
BetaManagedAgentsMCPOAuthAuthResponse object { mcp_server_url, type, expires_at, refresh } 
OAuth credential details for an MCP server.
mcp_server_url: string
URL of the MCP server this credential authenticates against.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_auth_response.mcp_server_url)
type: "mcp_oauth"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_auth_response.type)
expires_at: optional string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_auth_response.expires_at)
refresh: optional [BetaManagedAgentsMCPOAuthRefreshResponse](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_oauth_refresh_response) { client_id, token_endpoint, token_endpoint_auth, 2 more } 
OAuth refresh token configuration returned in credential responses.
client_id: string
OAuth client ID.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20\(resource\)%20beta.vaults.credentials.client_id)
token_endpoint: string
Token endpoint URL used to refresh the access token.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20\(resource\)%20beta.vaults.credentials.token_endpoint)
token_endpoint_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_token_endpoint_auth_none_response) { type }  or [BetaManagedAgentsTokenEndpointAuthBasicResponse](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_token_endpoint_auth_basic_response) { type }  or [BetaManagedAgentsTokenEndpointAuthPostResponse](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_token_endpoint_auth_post_response) { type } 
Token endpoint requires no client authentication.
BetaManagedAgentsTokenEndpointAuthNoneResponse object { type } 
Token endpoint requires no client authentication.
type: "none"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20\(resource\)%20beta.vaults.credentials.type)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20\(resource\)%20beta.vaults.credentials)
BetaManagedAgentsTokenEndpointAuthBasicResponse object { type } 
Token endpoint uses HTTP Basic authentication with client credentials.
type: "client_secret_basic"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20\(resource\)%20beta.vaults.credentials.type)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20\(resource\)%20beta.vaults.credentials)
BetaManagedAgentsTokenEndpointAuthPostResponse object { type } 
Token endpoint uses POST body authentication with client credentials.
type: "client_secret_post"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20\(resource\)%20beta.vaults.credentials.type)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20\(resource\)%20beta.vaults.credentials)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20\(resource\)%20beta.vaults.credentials.token_endpoint_auth)
resource: optional string
OAuth resource indicator.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20\(resource\)%20beta.vaults.credentials.resource)
scope: optional string
OAuth scope for the refresh request.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_auth_response.refresh%20%2B%20\(resource\)%20beta.vaults.credentials.scope)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_auth_response.refresh)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_mcp_oauth_auth_response)
BetaManagedAgentsStaticBearerAuthResponse object { mcp_server_url, type } 
Static bearer token credential details for an MCP server.
mcp_server_url: string
URL of the MCP server this credential authenticates against.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_static_bearer_auth_response.mcp_server_url)
type: "static_bearer"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_static_bearer_auth_response.type)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_static_bearer_auth_response)
BetaManagedAgentsEnvironmentVariableAuthResponse object { networking, secret_name, type } 
Environment variable credential details. The secret value is never returned.
networking: [BetaManagedAgentsUnrestrictedCredentialNetworkingResponse](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_unrestricted_credential_networking_response) { type }  or [BetaManagedAgentsLimitedCredentialNetworkingResponse](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_limited_credential_networking_response) { allowed_hosts, type } 
Outbound hosts the secret value is substituted on.
BetaManagedAgentsUnrestrictedCredentialNetworkingResponse object { type } 
The secret is substituted on any host the session's Environment network policy permits egress to.
type: "unrestricted"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_unrestricted_credential_networking_response.type)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_unrestricted_credential_networking_response)
BetaManagedAgentsLimitedCredentialNetworkingResponse object { allowed_hosts, type } 
The secret is substituted only on requests to the listed hosts.
allowed_hosts: array of string
Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_limited_credential_networking_response.allowed_hosts)
type: "limited"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_limited_credential_networking_response.type)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_limited_credential_networking_response)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_environment_variable_auth_response.networking)
secret_name: string
Name of the environment variable.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_environment_variable_auth_response.secret_name)
type: "environment_variable"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_environment_variable_auth_response.type)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_environment_variable_auth_response)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_credential.auth)
created_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_credential.created_at)
metadata: map[string]
Arbitrary key-value metadata attached to the credential.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_credential.metadata)
type: "vault_credential"
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_credential.type)
updated_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_credential.updated_at)
vault_id: string
Identifier of the vault this credential belongs to.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_credential.vault_id)
display_name: optional string
Human-readable name for the credential.
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_credential.display_name)
[](https://platform.claude.com/docs/en/api/beta/vaults/credentials/update#beta_managed_agents_credential)
Update Credential
cURL

curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "display_name": "Example credential",
          "metadata": {
            "environment": "production"
        }'

  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"

  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
