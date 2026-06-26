<!-- source: https://platform.claude.com/docs/en/api/admin/api_keys/retrieve -->

# Get API Key
GET/v1/organizations/api_keys/{api_key_id}
Get API Key
##### Path ParametersExpand Collapse 
api_key_id: string
ID of the API key.
[](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve#retrieve.api_key_id)
APIKey object { id, created_at, created_by, 6 more } 
ID of the API key.
[](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve#api_key.id)
created_at: string
RFC 3339 datetime string indicating when the API Key was created.
[](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve#api_key.created_at)
created_by: object { id, type } 
The ID and type of the actor that created the API key.
ID of the actor that created the object.
[](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve#api_key.created_by.id)
type: string
Type of the actor that created the object.
[](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve#api_key.created_by.type)
[](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve#api_key.created_by)
expires_at: string
RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.
[](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve#api_key.expires_at)
name: string
Name of the API key.
[](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve#api_key.name)
partial_key_hint: string
Partially redacted hint for the API key.
[](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve#api_key.partial_key_hint)
status: "active" or "inactive" or "archived" or "expired"
Status of the API key.
"active"
[](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve#api_key.status%5B0%5D)
"inactive"
[](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve#api_key.status%5B1%5D)
"archived"
[](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve#api_key.status%5B2%5D)
"expired"
[](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve#api_key.status%5B3%5D)
[](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve#api_key.status)
type: "api_key"
Object type.
For API Keys, this is always `"api_key"`.
[](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve#api_key.type)
workspace_id: string
ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace.
[](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve#api_key.workspace_id)
[](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve#api_key)
Get API Key

curl https://api.anthropic.com/v1/organizations/api_keys/$API_KEY_ID \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "name": "Developer Key",
  "partial_key_hint": "sk-ant-api03-R2D...igAA",
  "status": "active",
  "type": "api_key",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"

  "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "name": "Developer Key",
  "partial_key_hint": "sk-ant-api03-R2D...igAA",
  "status": "active",
  "type": "api_key",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
