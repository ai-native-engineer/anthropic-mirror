<!-- source: https://platform.claude.com/docs/en/api/admin/workspaces/update -->

# Update Workspace
POST/v1/organizations/workspaces/{workspace_id}
Update Workspace
##### Path ParametersExpand Collapse 
workspace_id: string
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#update.workspace_id)
#####  Body ParametersJSONExpand Collapse 
data_residency: optional object { allowed_inference_geos, default_inference_geo } 
Data residency configuration for the workspace.
allowed_inference_geos: optional array of string or "unrestricted"
Permitted inference geo values. Use 'unrestricted' to allow all geos, or a list of specific geos.
array of string
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#update.data_residency.allowed_inference_geos%5B0%5D)
"unrestricted"
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#update.data_residency.allowed_inference_geos%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#update.data_residency.allowed_inference_geos)
default_inference_geo: optional string
Default inference geo applied when requests omit the parameter. Must be a member of allowed_inference_geos unless allowed_inference_geos is `"unrestricted"`.
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#update.data_residency.default_inference_geo)
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#update.data_residency)
external_key_id: optional string
ID of the customer-managed encryption key (CMEK) configuration to use for this Workspace. Setting this field requires CMEK to be enabled for your organization. When set, data stored for this Workspace is encrypted with the referenced key. Create key configurations with the External Keys API. This field is write-once: once a key is attached to a Workspace it cannot be detached or replaced. To rotate key material, rotate the underlying key on your cloud KMS; the `external_key_id` stays the same.
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#update.external_key_id)
name: optional string
Name of the Workspace.
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#update.name)
tags: optional map[string]
User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#update.tags)
Workspace object { id, archived_at, compartment_id, 7 more } 
ID of the Workspace.
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#workspace.id)
archived_at: string
RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#workspace.archived_at)
compartment_id: string
Identifier for this Workspace's encryption compartment. When you configure a customer-managed encryption key (CMEK), reference this value in your cloud provider's key configuration — an AWS KMS key-policy condition or an Azure Key Vault tag — so the key is scoped to this compartment. See the CMEK integration guide for the required key configuration, including the value used during key validation.
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#workspace.compartment_id)
created_at: string
RFC 3339 datetime string indicating when the Workspace was created.
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#workspace.created_at)
data_residency: object { allowed_inference_geos, default_inference_geo, workspace_geo } 
Data residency configuration.
allowed_inference_geos: array of string or "unrestricted"
Permitted inference geo values. 'unrestricted' means all geos are allowed.
array of string
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#workspace.data_residency.allowed_inference_geos%5B0%5D)
"unrestricted"
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#workspace.data_residency.allowed_inference_geos%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#workspace.data_residency.allowed_inference_geos)
default_inference_geo: string
Default inference geo applied when requests omit the parameter.
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#workspace.data_residency.default_inference_geo)
workspace_geo: string
Geographic region for workspace data storage. Immutable after creation.
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#workspace.data_residency.workspace_geo)
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#workspace.data_residency)
display_color: string
Hex color code representing the Workspace in the Anthropic Console.
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#workspace.display_color)
external_key_id: string
ID of the customer-managed encryption key (CMEK) configuration to use for this Workspace. Setting this field requires CMEK to be enabled for your organization. When set, data stored for this Workspace is encrypted with the referenced key. Create key configurations with the External Keys API. This field is write-once: once a key is attached to a Workspace it cannot be detached or replaced. To rotate key material, rotate the underlying key on your cloud KMS; the `external_key_id` stays the same.
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#workspace.external_key_id)
name: string
Name of the Workspace.
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#workspace.name)
tags: map[string]
User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#workspace.tags)
type: "workspace"
Object type.
For Workspaces, this is always `"workspace"`.
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#workspace.type)
[](https://platform.claude.com/docs/en/api/admin/workspaces/update#workspace)
Update Workspace

curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
          "tags": {
            "env": "prod",
            "team": "platform"
        }'

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
