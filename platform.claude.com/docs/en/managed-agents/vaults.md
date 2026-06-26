<!-- source: https://platform.claude.com/docs/en/managed-agents/vaults -->

# Authenticate with vaults
Register per-user credentials when creating sessions.
Vaults and credentials are authentication primitives that let you register credentials for third-party services once and reference them by ID at session creation. This means you don't need to run your own secret store, transmit tokens on every call, or lose track of which end user an agent acted on behalf of.
The vault reference is a per-session parameter, so you can manage your product at the `agent` resource granularity and your users at the `session` resource granularity.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Create a vault

Vaults and credentials are workspace-scoped, meaning anyone with an API key for the same workspace can reference them when creating a session. To revoke access, delete the vault or credential.
A vault is the collection of `credentials` associated with an end user. Give it a `display_name` and optionally tag it with `metadata` so you can map it back to your own user records.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

VAULT_ID=$(ant beta:vaults create \
  --display-name "Alice" \
  --metadata '{external_user_id: usr_abc123}' \
  --transform id --raw-output)
echo "$VAULT_ID"  # "vlt_01ABC..."

The response is the full vault record:

  "type": "vault",
  "id": "vlt_01ABC...",
  "display_name": "Alice",
  "metadata": { "external_user_id": "usr_abc123" },
  "created_at": "2026-03-18T10:00:00Z",
  "updated_at": "2026-03-18T10:00:00Z",
  "archived_at": null

Add a credential
Two credential categories are supported:
  * **MCP credentials** (`mcp_oauth`, `static_bearer`): each credential is keyed by an `mcp_server_url`. When the agent connects to a server at that URL at session runtime, the token is injected automatically.
  * **Environment variables** (`environment_variable`): each credential is keyed by a `secret_name` (the environment variable name) and stored in the sandbox as an opaque placeholder. When the agent initiates an outbound request, the opaque placeholder is substituted with the real secret at egress. The agent never sees the secret value. Use this for any service that authenticates through an environment variable, such as CLIs, SDKs, or direct API calls.

The actual credential values you supply (`token`, `access_token`, `refresh_token`, `client_secret`, `secret_value`) are treated as sensitive, write-only fields and never returned in API responses.
Environment variable credentials (`environment_variable`) are not yet supported with [self-hosted sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes).
MCP OAuth
MCP OAuth
MCP static bearer
MCP static bearer
Environment variable
Environment variable
Use `mcp_oauth` when the MCP server uses OAuth 2.0. If you supply a `refresh` block, Anthropic refreshes the access token on your behalf when it expires.
The `refresh.token_endpoint_auth.type` field indicates how to authenticate the refresh call:
  * `none`: public client
  * `client_secret_basic`: HTTP Basic authentication with the client secret
  * `client_secret_post`: client secret in the POST body

curlCLIPythonTypeScriptC#GoJavaPHPRuby

CREDENTIAL_ID=$(ant beta:vaults:credentials create \
  --vault-id "$VAULT_ID" \
  --display-name "Alice's Slack" \
  --transform id --raw-output <<'YAML'
auth:
  type: mcp_oauth
  mcp_server_url: https://mcp.slack.com/mcp
  access_token: xoxp-...
  expires_at: "2099-12-31T23:59:59Z"
  refresh:
    token_endpoint: https://slack.com/api/oauth.v2.access
    client_id: "1234567890.0987654321"
    scope: channels:read chat:write
    refresh_token: xoxe-1-...
    token_endpoint_auth:
      type: client_secret_post
      client_secret: abc123...
YAML
)

Credentials are stored as provided and are not validated until session runtime. An invalid credential surfaces as an authentication or downstream error during the session, which is emitted but does not block the session from continuing.
Constraints:
  * **Unique key per vault.** `mcp_server_url` (MCP credentials) and `secret_name` (environment variable credentials) must be unique among active credentials in a vault. Creating a duplicate returns a 409.
  * **Keys are immutable.** To change `mcp_server_url` or `secret_name`, archive the credential and create a new one.
  * **Maximum 20 credentials per vault.**

Reference the vault at session creation
Pass `vault_ids` when creating a session:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

SESSION_ID=$(ant beta:sessions create \
  --agent "$AGENT_ID" \
  --environment-id "$ENVIRONMENT_ID" \
  --vault-id "$VAULT_ID" \
  --title "Alice's Slack digest" \
  --transform id --raw-output)

Runtime behavior:
  * When no MCP credential matches by `mcp_server_url`, the connection is attempted unauthenticated and will error if the server requires authentication.
  * When multiple vaults contain a matching credential, the first vault with a match wins.
  * In [multi-agent sessions](https://platform.claude.com/docs/en/managed-agents/multi-agent), vault credentials apply to every thread. An agent whose own definition declares the matching MCP server authenticates with these credentials. See [Connect agents to MCP servers](https://platform.claude.com/docs/en/managed-agents/multi-agent#connect-agents-to-mcp-servers).

Rotate a credential
Secret values and `display_name` can be updated. Structural fields (`mcp_server_url`, `secret_name`, `token_endpoint`, `client_id`) are locked after creation. To change them, archive the credential and create a new one.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:vaults:credentials update \
  --vault-id "$VAULT_ID" \
  --credential-id "$CREDENTIAL_ID" <<'YAML'
auth:
  type: mcp_oauth
  access_token: xoxp-new-...
  expires_at: "2099-12-31T23:59:59Z"
  refresh:
    refresh_token: xoxe-1-new-...
YAML

Credential lifecycle
Credentials are re-resolved periodically, both during a session and during the vault lifecycle. This ensures that credential rotation, archival, or deletion propagates to running sessions without a restart.
To be notified if a credential is archived, deleted, or fails to refresh, you can subscribe to the vault and credential [webhooks](https://platform.claude.com/docs/en/managed-agents/webhooks) associated with those lifecycle changes.  
| Event  | Trigger  |  
| --- | --- |  
| `vault.archived`  | Vault archived. A `vault_credential.archived` event is also emitted for each underlying credential.  |  
| `vault.deleted`  | Vault deleted. A `vault_credential.deleted` event is also emitted for each underlying credential.  |  
| `vault_credential.archived`  | Credential archived, either directly or as a result of vault archival.  |  
| `vault_credential.deleted`  | Credential deleted, either directly or as a result of vault deletion.  |  
| `vault_credential.refresh_failed`  | An `mcp_oauth` credential cannot be refreshed (invalid refresh token, or irrecoverable error from the OAuth server).  |  
This is a non-exhaustive list of webhooks; see [Subscribe to webhooks](https://platform.claude.com/docs/en/managed-agents/webhooks) for the complete list.
For `mcp_oauth` credentials, re-resolution also refreshes the access token if it has expired. If the refresh fails, a `vault_credential.refresh_failed` event is emitted.
### 
Diagnose an OAuth refresh failure
To diagnose why a refresh failed, call `POST /v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate` (or `client.beta.vaults.credentials.mcp_oauth_validate(...)` in the SDK). This lets you decide how to handle the failure; the right action depends on the error type.
The top-level `status` tells you what to do next:
  * `valid`: the token works; no action needed.
  * `invalid`: the grant is gone or the OAuth server rejected the refresh with a 4xx. Prompt the end user to re-authorize.
  * `unknown`: a transient error (5xx, 429, or network failure). Wait and retry.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:vaults:credentials mcp-oauth-validate \
  --vault-id "$VAULT_ID" \
  --credential-id "$CREDENTIAL_ID" \
  --transform status --raw-output  # "valid", "invalid", or "unknown"

The response is a `vault_credential_validation` object. `mcp_probe` includes the failed MCP handshake step; `refresh` includes the outcome of the attempted refresh.

  "type": "vault_credential_validation",
  "credential_id": "vcrd_01ABC...",
  "vault_id": "vlt_01XYZ...",
  "validated_at": "2026-04-29T17:12:00Z",
  "has_refresh_token": false,
  "status": "invalid",
  "mcp_probe": {
    "method": "initialize",
    "http_response": {
      "status_code": 401,
      "content_type": "application/json",
      "body": "{\"error\":\"invalid_token\"}",
      "body_truncated": false
  "refresh": {
    "status": "no_refresh_token",
    "http_response": null

Other operations
  * **List vaults or credentials:** Paginated, newest first. Archived records are excluded by default (pass `include_archived=true` to include them).
  * **Archive a vault:** `POST /v1/vaults/{id}/archive`. Cascades to all credentials. Secrets are purged; records are retained for auditing. Future sessions referencing this vault fail; running sessions continue.
  * **Archive a credential:** `POST /v1/vaults/{id}/credentials/{cred_id}/archive`. Purges the secret payload; the credential key (`mcp_server_url` or `secret_name`) remains visible and is freed for a replacement credential.
  * **Delete a vault or credential:** Hard delete. The record is not retained. Use archive if you need an audit trail.

  * [Create a vault](https://platform.claude.com/docs/en/managed-agents/vaults#create-a-vault)
  * [Add a credential](https://platform.claude.com/docs/en/managed-agents/vaults#add-a-credential)
  * [Reference the vault at session creation](https://platform.claude.com/docs/en/managed-agents/vaults#reference-the-vault-at-session-creation)
  * [Rotate a credential](https://platform.claude.com/docs/en/managed-agents/vaults#rotate-a-credential)
  * [Credential lifecycle](https://platform.claude.com/docs/en/managed-agents/vaults#credential-lifecycle)
  * [Diagnose an OAuth refresh failure](https://platform.claude.com/docs/en/managed-agents/vaults#diagnose-an-o-auth-refresh-failure)
  * [Other operations](https://platform.claude.com/docs/en/managed-agents/vaults#other-operations)

Managed Agents/Delegate work to your agent
# Authenticate with vaults
Register per-user credentials when creating sessions.
Vaults and credentials are authentication primitives that let you register credentials for third-party services once and reference them by ID at session creation. This means you don't need to run your own secret store, transmit tokens on every call, or lose track of which end user an agent acted on behalf of.
The vault reference is a per-session parameter, so you can manage your product at the `agent` resource granularity and your users at the `session` resource granularity.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Create a vault

Vaults and credentials are workspace-scoped, meaning anyone with an API key for the same workspace can reference them when creating a session. To revoke access, delete the vault or credential.
A vault is the collection of `credentials` associated with an end user. Give it a `display_name` and optionally tag it with `metadata` so you can map it back to your own user records.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

VAULT_ID=$(ant beta:vaults create \
  --display-name "Alice" \
  --metadata '{external_user_id: usr_abc123}' \
  --transform id --raw-output)
echo "$VAULT_ID"  # "vlt_01ABC..."

The response is the full vault record:

  "type": "vault",
  "id": "vlt_01ABC...",
  "display_name": "Alice",
  "metadata": { "external_user_id": "usr_abc123" },
  "created_at": "2026-03-18T10:00:00Z",
  "updated_at": "2026-03-18T10:00:00Z",
  "archived_at": null

Add a credential
Two credential categories are supported:
  * **MCP credentials** (`mcp_oauth`, `static_bearer`): each credential is keyed by an `mcp_server_url`. When the agent connects to a server at that URL at session runtime, the token is injected automatically.
  * **Environment variables** (`environment_variable`): each credential is keyed by a `secret_name` (the environment variable name) and stored in the sandbox as an opaque placeholder. When the agent initiates an outbound request, the opaque placeholder is substituted with the real secret at egress. The agent never sees the secret value. Use this for any service that authenticates through an environment variable, such as CLIs, SDKs, or direct API calls.

The actual credential values you supply (`token`, `access_token`, `refresh_token`, `client_secret`, `secret_value`) are treated as sensitive, write-only fields and never returned in API responses.
Environment variable credentials (`environment_variable`) are not yet supported with [self-hosted sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes).
MCP OAuth
MCP OAuth
MCP static bearer
MCP static bearer
Environment variable
Environment variable
Use `mcp_oauth` when the MCP server uses OAuth 2.0. If you supply a `refresh` block, Anthropic refreshes the access token on your behalf when it expires.
The `refresh.token_endpoint_auth.type` field indicates how to authenticate the refresh call:
  * `none`: public client
  * `client_secret_basic`: HTTP Basic authentication with the client secret
  * `client_secret_post`: client secret in the POST body

curlCLIPythonTypeScriptC#GoJavaPHPRuby

CREDENTIAL_ID=$(ant beta:vaults:credentials create \
  --vault-id "$VAULT_ID" \
  --display-name "Alice's Slack" \
  --transform id --raw-output <<'YAML'
auth:
  type: mcp_oauth
  mcp_server_url: https://mcp.slack.com/mcp
  access_token: xoxp-...
  expires_at: "2099-12-31T23:59:59Z"
  refresh:
    token_endpoint: https://slack.com/api/oauth.v2.access
    client_id: "1234567890.0987654321"
    scope: channels:read chat:write
    refresh_token: xoxe-1-...
    token_endpoint_auth:
      type: client_secret_post
      client_secret: abc123...
YAML
)

Credentials are stored as provided and are not validated until session runtime. An invalid credential surfaces as an authentication or downstream error during the session, which is emitted but does not block the session from continuing.
Constraints:
  * **Unique key per vault.** `mcp_server_url` (MCP credentials) and `secret_name` (environment variable credentials) must be unique among active credentials in a vault. Creating a duplicate returns a 409.
  * **Keys are immutable.** To change `mcp_server_url` or `secret_name`, archive the credential and create a new one.
  * **Maximum 20 credentials per vault.**

Reference the vault at session creation
Pass `vault_ids` when creating a session:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

SESSION_ID=$(ant beta:sessions create \
  --agent "$AGENT_ID" \
  --environment-id "$ENVIRONMENT_ID" \
  --vault-id "$VAULT_ID" \
  --title "Alice's Slack digest" \
  --transform id --raw-output)

Runtime behavior:
  * When no MCP credential matches by `mcp_server_url`, the connection is attempted unauthenticated and will error if the server requires authentication.
  * When multiple vaults contain a matching credential, the first vault with a match wins.
  * In [multi-agent sessions](https://platform.claude.com/docs/en/managed-agents/multi-agent), vault credentials apply to every thread. An agent whose own definition declares the matching MCP server authenticates with these credentials. See [Connect agents to MCP servers](https://platform.claude.com/docs/en/managed-agents/multi-agent#connect-agents-to-mcp-servers).

Rotate a credential
Secret values and `display_name` can be updated. Structural fields (`mcp_server_url`, `secret_name`, `token_endpoint`, `client_id`) are locked after creation. To change them, archive the credential and create a new one.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:vaults:credentials update \
  --vault-id "$VAULT_ID" \
  --credential-id "$CREDENTIAL_ID" <<'YAML'
auth:
  type: mcp_oauth
  access_token: xoxp-new-...
  expires_at: "2099-12-31T23:59:59Z"
  refresh:
    refresh_token: xoxe-1-new-...
YAML

Credential lifecycle
Credentials are re-resolved periodically, both during a session and during the vault lifecycle. This ensures that credential rotation, archival, or deletion propagates to running sessions without a restart.
To be notified if a credential is archived, deleted, or fails to refresh, you can subscribe to the vault and credential [webhooks](https://platform.claude.com/docs/en/managed-agents/webhooks) associated with those lifecycle changes.  
| Event  | Trigger  |  
| --- | --- |  
| `vault.archived`  | Vault archived. A `vault_credential.archived` event is also emitted for each underlying credential.  |  
| `vault.deleted`  | Vault deleted. A `vault_credential.deleted` event is also emitted for each underlying credential.  |  
| `vault_credential.archived`  | Credential archived, either directly or as a result of vault archival.  |  
| `vault_credential.deleted`  | Credential deleted, either directly or as a result of vault deletion.  |  
| `vault_credential.refresh_failed`  | An `mcp_oauth` credential cannot be refreshed (invalid refresh token, or irrecoverable error from the OAuth server).  |  
This is a non-exhaustive list of webhooks; see [Subscribe to webhooks](https://platform.claude.com/docs/en/managed-agents/webhooks) for the complete list.
For `mcp_oauth` credentials, re-resolution also refreshes the access token if it has expired. If the refresh fails, a `vault_credential.refresh_failed` event is emitted.
### 
Diagnose an OAuth refresh failure
To diagnose why a refresh failed, call `POST /v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate` (or `client.beta.vaults.credentials.mcp_oauth_validate(...)` in the SDK). This lets you decide how to handle the failure; the right action depends on the error type.
The top-level `status` tells you what to do next:
  * `valid`: the token works; no action needed.
  * `invalid`: the grant is gone or the OAuth server rejected the refresh with a 4xx. Prompt the end user to re-authorize.
  * `unknown`: a transient error (5xx, 429, or network failure). Wait and retry.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:vaults:credentials mcp-oauth-validate \
  --vault-id "$VAULT_ID" \
  --credential-id "$CREDENTIAL_ID" \
  --transform status --raw-output  # "valid", "invalid", or "unknown"

The response is a `vault_credential_validation` object. `mcp_probe` includes the failed MCP handshake step; `refresh` includes the outcome of the attempted refresh.

  "type": "vault_credential_validation",
  "credential_id": "vcrd_01ABC...",
  "vault_id": "vlt_01XYZ...",
  "validated_at": "2026-04-29T17:12:00Z",
  "has_refresh_token": false,
  "status": "invalid",
  "mcp_probe": {
    "method": "initialize",
    "http_response": {
      "status_code": 401,
      "content_type": "application/json",
      "body": "{\"error\":\"invalid_token\"}",
      "body_truncated": false
  "refresh": {
    "status": "no_refresh_token",
    "http_response": null

Other operations
  * **List vaults or credentials:** Paginated, newest first. Archived records are excluded by default (pass `include_archived=true` to include them).
  * **Archive a vault:** `POST /v1/vaults/{id}/archive`. Cascades to all credentials. Secrets are purged; records are retained for auditing. Future sessions referencing this vault fail; running sessions continue.
  * **Archive a credential:** `POST /v1/vaults/{id}/credentials/{cred_id}/archive`. Purges the secret payload; the credential key (`mcp_server_url` or `secret_name`) remains visible and is freed for a replacement credential.
  * **Delete a vault or credential:** Hard delete. The record is not retained. Use archive if you need an audit trail.
