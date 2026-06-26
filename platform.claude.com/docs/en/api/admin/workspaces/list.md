<!-- source: https://platform.claude.com/docs/en/api/admin/workspaces/list -->

# List Workspaces
GET/v1/organizations/workspaces
List Workspaces
##### Query ParametersExpand Collapse 
after_id: optional string
ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#list.after_id)
before_id: optional string
ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#list.before_id)
include_archived: optional boolean
Whether to include Workspaces that have been archived in the response
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#list.include_archived)
limit: optional number
Number of items to return per page.
Defaults to `20`. Ranges from `1` to `1000`.
maximum1000
minimum1
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#list.limit)
data: array of [Workspace](https://platform.claude.com/docs/en/api/%24shared#workspace) { id, archived_at, compartment_id, 7 more } 
ID of the Workspace.
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#workspace.id)
archived_at: string
RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#workspace.archived_at)
compartment_id: string
Identifier for this Workspace's encryption compartment. When you configure a customer-managed encryption key (CMEK), reference this value in your cloud provider's key configuration — an AWS KMS key-policy condition or an Azure Key Vault tag — so the key is scoped to this compartment. See the CMEK integration guide for the required key configuration, including the value used during key validation.
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#workspace.compartment_id)
created_at: string
RFC 3339 datetime string indicating when the Workspace was created.
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#workspace.created_at)
data_residency: object { allowed_inference_geos, default_inference_geo, workspace_geo } 
Data residency configuration.
allowed_inference_geos: array of string or "unrestricted"
Permitted inference geo values. 'unrestricted' means all geos are allowed.
array of string
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#workspace.data_residency.allowed_inference_geos%5B0%5D)
"unrestricted"
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#workspace.data_residency.allowed_inference_geos%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#workspace.data_residency.allowed_inference_geos)
default_inference_geo: string
Default inference geo applied when requests omit the parameter.
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#workspace.data_residency.default_inference_geo)
workspace_geo: string
Geographic region for workspace data storage. Immutable after creation.
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#workspace.data_residency.workspace_geo)
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#workspace.data_residency)
display_color: string
Hex color code representing the Workspace in the Anthropic Console.
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#workspace.display_color)
external_key_id: string
ID of the customer-managed encryption key (CMEK) configuration to use for this Workspace. Setting this field requires CMEK to be enabled for your organization. When set, data stored for this Workspace is encrypted with the referenced key. Create key configurations with the External Keys API. This field is write-once: once a key is attached to a Workspace it cannot be detached or replaced. To rotate key material, rotate the underlying key on your cloud KMS; the `external_key_id` stays the same.
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#workspace.external_key_id)
name: string
Name of the Workspace.
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#workspace.name)
tags: map[string]
User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#workspace.tags)
type: "workspace"
Object type.
For Workspaces, this is always `"workspace"`.
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#workspace.type)
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#list)
first_id: string
First ID in the `data` list. Can be used as the `before_id` for the previous page.
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#list)
has_more: boolean
Indicates if there are more results in the requested page direction.
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#list)
last_id: string
Last ID in the `data` list. Can be used as the `after_id` for the next page.
[](https://platform.claude.com/docs/en/api/admin/workspaces/list#list)
List Workspaces

curl https://api.anthropic.com/v1/organizations/workspaces \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "data": [
      "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "data_residency": {
        "allowed_inference_geos": "unrestricted",
        "default_inference_geo": "default_inference_geo",
        "workspace_geo": "workspace_geo"
      "display_color": "#6C5BB9",
      "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
      "name": "Workspace Name",
      "tags": {
        "env": "prod",
        "team": "platform"
      "type": "workspace"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"

  "data": [
      "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "data_residency": {
        "allowed_inference_geos": "unrestricted",
        "default_inference_geo": "default_inference_geo",
        "workspace_geo": "workspace_geo"
      "display_color": "#6C5BB9",
      "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
      "name": "Workspace Name",
      "tags": {
        "env": "prod",
        "team": "platform"
      "type": "workspace"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
