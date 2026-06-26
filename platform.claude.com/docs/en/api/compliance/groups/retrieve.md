<!-- source: https://platform.claude.com/docs/en/api/compliance/groups/retrieve -->

# Get Compliance Group
GET/v1/compliance/groups/{group_id}
Get Compliance Group
##### Path ParametersExpand Collapse 
group_id: string
The group ID (tagged ID, e.g., rbac_group_abc123)
[](https://platform.claude.com/docs/en/api/compliance/groups/retrieve#retrieve.group_id)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/groups/retrieve#retrieve.x-api-key)
Group identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/groups/retrieve#group_retrieve_response.id)
created_at: string
Group creation timestamp (ISO 8601)
[](https://platform.claude.com/docs/en/api/compliance/groups/retrieve#group_retrieve_response.created_at)
description: string
Group description
[](https://platform.claude.com/docs/en/api/compliance/groups/retrieve#group_retrieve_response.description)
name: string
Group name
[](https://platform.claude.com/docs/en/api/compliance/groups/retrieve#group_retrieve_response.name)
roles: array of string
Role IDs assigned to this group.
[](https://platform.claude.com/docs/en/api/compliance/groups/retrieve#group_retrieve_response.roles)
source_type: string
How the group was created ('direct' or 'scim')
[](https://platform.claude.com/docs/en/api/compliance/groups/retrieve#group_retrieve_response.source_type)
updated_at: string
Group last-updated timestamp (ISO 8601)
[](https://platform.claude.com/docs/en/api/compliance/groups/retrieve#group_retrieve_response.updated_at)
Get Compliance Group

curl https://api.anthropic.com/v1/compliance/groups/$GROUP_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "id": "id",
  "created_at": "created_at",
  "description": "description",
  "name": "name",
  "roles": [
    "string"
  ],
  "source_type": "source_type",
  "updated_at": "updated_at"

  "id": "id",
  "created_at": "created_at",
  "description": "description",
  "name": "name",
  "roles": [
    "string"
  ],
  "source_type": "source_type",
  "updated_at": "updated_at"
