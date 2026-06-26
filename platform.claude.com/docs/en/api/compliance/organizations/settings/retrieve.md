<!-- source: https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve -->

# Get effective organization settings
GET/v1/compliance/organizations/{organization_id}/settings
Retrieve the effective settings for an organization.
Returns the settings currently in force for the given organization — the enforced state after all policies are applied, which may differ from what is configured in the admin console. Settings an organization's administrators cannot change (for example, ones controlled by Anthropic policy or not available to the organization) are omitted from the list.
The organization must belong to the API key's organization hierarchy; unknown organizations and organizations outside the hierarchy return 404.
##### Path ParametersExpand Collapse 
organization_id: string
The organization's UUID
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#retrieve.organization_id)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#retrieve.x-api-key)
api_keys: array of object { id, created_at, created_by_id, 4 more } 
Compliance API keys configured for the organization hierarchy, ordered by creation time ascending. Key secret values are never included.
Unique identifier for the API key.
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.api_keys.items.id)
created_at: string
When the key was created.
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.api_keys.items.created_at)
created_by_id: string
Identifier of the user who created the key, or null when the key was created by automation or its creator's account no longer exists.
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.api_keys.items.created_by_id)
is_active: boolean
Whether the key is currently active. A deactivated key is listed for audit visibility but cannot authenticate requests.
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.api_keys.items.is_active)
name: string
The name given to the API key when it was created.
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.api_keys.items.name)
scopes: array of string
The permission scopes granted to the key.
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.api_keys.items.scopes)
type: optional "compliance_api_key"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.api_keys.items.type)
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.api_keys)
organization_id: string
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.organization_id)
settings: array of object { name, value, type }  or object { name, value, type }  or object { name, value, type }  or 2 more
Boolean object { name, value, type } 
A setting whose enforced value is a single true/false flag.
name: "api_workbench_feedback_collection_enabled" or "claude_ai_feedback_collection_enabled" or "claude_code_trusted_devices_required" or 9 more
"api_workbench_feedback_collection_enabled"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B0%5D.name%5B0%5D)
"claude_ai_feedback_collection_enabled"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B0%5D.name%5B1%5D)
"claude_code_trusted_devices_required"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B0%5D.name%5B2%5D)
"code_execution_enabled"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B0%5D.name%5B3%5D)
"code_execution_network_egress_enabled"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B0%5D.name%5B4%5D)
"content_redaction_enabled"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B0%5D.name%5B5%5D)
"directory_sync_enabled"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B0%5D.name%5B6%5D)
"frontier_data_use_enabled"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B0%5D.name%5B7%5D)
"ip_allowlist_enabled"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B0%5D.name%5B8%5D)
"sso_claude_ai_enforced"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B0%5D.name%5B9%5D)
"sso_console_enforced"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B0%5D.name%5B10%5D)
"sso_enabled"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B0%5D.name%5B11%5D)
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B0%5D.name)
value: boolean
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B0%5D.value)
type: optional "boolean"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B0%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B0%5D)
Integer object { name, value, type } 
A setting whose enforced value is a whole number; null means no limit is in force.
name: "account_session_duration_seconds"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B1%5D.name)
value: number
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B1%5D.value)
type: optional "integer"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B1%5D)
StringList object { name, value, type } 
A setting whose enforced value is a list of strings.
name: "allowed_invite_domains" or "ip_allowlist_ip_ranges"
"allowed_invite_domains"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B2%5D.name%5B0%5D)
"ip_allowlist_ip_ranges"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B2%5D.name%5B1%5D)
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B2%5D.name)
value: array of string
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B2%5D.value)
type: optional "string_list"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B2%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B2%5D)
ProvisioningMode object { value, name, type } 
How organization members are provisioned, resolved to the enforced mode.
A configured mode is reported only while the mechanism that enforces it is active: just-in-time modes require single sign-on to be enabled, and SCIM modes require directory sync to be enabled. Otherwise `login_only` is reported, regardless of any stored configuration.
value: "jit_advanced" or "jit_permissive" or "login_only" or 2 more
How organization members are provisioned under SSO.
"jit_advanced"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B3%5D.value%5B0%5D)
"jit_permissive"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B3%5D.value%5B1%5D)
"login_only"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B3%5D.value%5B2%5D)
"scim_advanced"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B3%5D.value%5B3%5D)
"scim_permissive"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B3%5D.value%5B4%5D)
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B3%5D.value)
name: optional "sso_provisioning_mode"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B3%5D.name)
type: optional "provisioning_mode"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B3%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B3%5D)
DataRetention object { value, name, type } 
The data retention periods in force, keyed by the type of data they apply to.
A key of `all` covers every data type and is exclusive: when present it is the only key. A missing key means no organization-level administrator-configured retention period is in force for that data type; Anthropic's service defaults may still apply.
value: map[object { duration, timescale, type }  or object { type } ]
Fixed object { duration, timescale, type } 
A fixed retention window measured from each item's last activity.
duration: number
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B4%5D.value.items%5B0%5D.duration)
timescale: "day" or "month"
"day"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B4%5D.value.items%5B0%5D.timescale%5B0%5D)
"month"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B4%5D.value.items%5B0%5D.timescale%5B1%5D)
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B4%5D.value.items%5B0%5D.timescale)
type: optional "fixed"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B4%5D.value.items%5B0%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B4%5D.value.items%5B0%5D)
Indefinite object { type } 
An indefinite retention period: data is kept with no time limit.
type: optional "indefinite"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B4%5D.value.items%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B4%5D.value.items%5B1%5D)
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B4%5D.value)
name: optional "data_retention_periods"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B4%5D.name)
type: optional "data_retention"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B4%5D.type)
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings.items%5B4%5D)
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.settings)
type: optional "effective_organization_settings"
[](https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve#setting_retrieve_response.type)
Get effective organization settings

curl https://api.anthropic.com/v1/compliance/organizations/$ORGANIZATION_ID/settings \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "api_keys": [
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "created_by_id": "created_by_id",
      "is_active": true,
      "name": "name",
      "scopes": [
        "string"
      ],
      "type": "compliance_api_key"
  ],
  "organization_id": "organization_id",
  "settings": [
      "name": "api_workbench_feedback_collection_enabled",
      "value": true,
      "type": "boolean"
  ],
  "type": "effective_organization_settings"

  "api_keys": [
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "created_by_id": "created_by_id",
      "is_active": true,
      "name": "name",
      "scopes": [
        "string"
      ],
      "type": "compliance_api_key"
  ],
  "organization_id": "organization_id",
  "settings": [
      "name": "api_workbench_feedback_collection_enabled",
      "value": true,
      "type": "boolean"
  ],
  "type": "effective_organization_settings"
