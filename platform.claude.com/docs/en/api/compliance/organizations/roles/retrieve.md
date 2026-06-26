<!-- source: https://platform.claude.com/docs/en/api/compliance/organizations/roles/retrieve -->

# Get Compliance Role
GET/v1/compliance/organizations/{org_uuid}/roles/{role_id}
Get Compliance Role
##### Path ParametersExpand Collapse 
org_uuid: string
The organization UUID
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/retrieve#retrieve.org_uuid)
role_id: string
The role ID (tagged ID, e.g., rbac_role_abc123)
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/retrieve#retrieve.role_id)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/retrieve#retrieve.x-api-key)
Role identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/retrieve#role_retrieve_response.id)
created_at: string
Role creation timestamp (ISO 8601)
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/retrieve#role_retrieve_response.created_at)
description: string
Role description
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/retrieve#role_retrieve_response.description)
name: string
Role name
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/retrieve#role_retrieve_response.name)
updated_at: string
Role last-updated timestamp (ISO 8601)
[](https://platform.claude.com/docs/en/api/compliance/organizations/roles/retrieve#role_retrieve_response.updated_at)
Get Compliance Role

curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles/$ROLE_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "id": "id",
  "created_at": "created_at",
  "description": "description",
  "name": "name",
  "updated_at": "updated_at"

  "id": "id",
  "created_at": "created_at",
  "description": "description",
  "name": "name",
  "updated_at": "updated_at"
