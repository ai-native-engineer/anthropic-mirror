<!-- source: https://platform.claude.com/docs/en/api/admin/api_keys/list -->

# List API Keys
GET/v1/organizations/api_keys
List API Keys
##### Query ParametersExpand Collapse 
after_id: optional string
ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#list.after_id)
before_id: optional string
ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#list.before_id)
created_by_user_id: optional string
Filter by the ID of the User who created the object.
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#list.created_by_user_id)
limit: optional number
Number of items to return per page.
Defaults to `20`. Ranges from `1` to `1000`.
maximum1000
minimum1
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#list.limit)
status: optional "active" or "inactive" or "archived" or "expired"
Filter by API key status.
"active"
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#list.status%5B0%5D)
"inactive"
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#list.status%5B1%5D)
"archived"
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#list.status%5B2%5D)
"expired"
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#list.status%5B3%5D)
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#list.status)
workspace_id: optional string
Filter by Workspace ID.
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#list.workspace_id)
data: array of [APIKey](https://platform.claude.com/docs/en/api/%24shared#api_key) { id, created_at, created_by, 6 more } 
ID of the API key.
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#api_key.id)
created_at: string
RFC 3339 datetime string indicating when the API Key was created.
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#api_key.created_at)
created_by: object { id, type } 
The ID and type of the actor that created the API key.
ID of the actor that created the object.
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#api_key.created_by.id)
type: string
Type of the actor that created the object.
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#api_key.created_by.type)
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#api_key.created_by)
expires_at: string
RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#api_key.expires_at)
name: string
Name of the API key.
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#api_key.name)
partial_key_hint: string
Partially redacted hint for the API key.
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#api_key.partial_key_hint)
status: "active" or "inactive" or "archived" or "expired"
Status of the API key.
"active"
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#api_key.status%5B0%5D)
"inactive"
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#api_key.status%5B1%5D)
"archived"
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#api_key.status%5B2%5D)
"expired"
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#api_key.status%5B3%5D)
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#api_key.status)
type: "api_key"
Object type.
For API Keys, this is always `"api_key"`.
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#api_key.type)
workspace_id: string
ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace.
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#api_key.workspace_id)
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#list)
first_id: string
First ID in the `data` list. Can be used as the `before_id` for the previous page.
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#list)
has_more: boolean
Indicates if there are more results in the requested page direction.
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#list)
last_id: string
Last ID in the `data` list. Can be used as the `after_id` for the next page.
[](https://platform.claude.com/docs/en/api/admin/api_keys/list#list)
List API Keys

curl https://api.anthropic.com/v1/organizations/api_keys \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "data": [
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
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"

  "data": [
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
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
