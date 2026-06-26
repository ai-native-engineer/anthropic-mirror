<!-- source: https://platform.claude.com/docs/en/api/compliance/organizations/list -->

# List organizations
GET/v1/compliance/organizations
List organizations under the parent organization.
Returns a list of organizations sorted by creation date in ascending order. This endpoint does not support pagination and will return an error if the response would exceed 1,000 organizations.
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/organizations/list#list.x-api-key)
data: array of object { created_at, name, uuid } 
List of organizations sorted by creation date, ascending
created_at: string
Organization creation time (RFC 3339 format)
[](https://platform.claude.com/docs/en/api/compliance/organizations/list#organization_list_response.data.items.created_at)
name: string
Organization name
[](https://platform.claude.com/docs/en/api/compliance/organizations/list#organization_list_response.data.items.name)
uuid: string
Unique identifier for the organization (UUID format)
[](https://platform.claude.com/docs/en/api/compliance/organizations/list#organization_list_response.data.items.uuid)
[](https://platform.claude.com/docs/en/api/compliance/organizations/list#organization_list_response.data)
List organizations

curl https://api.anthropic.com/v1/compliance/organizations \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "data": [
      "created_at": "created_at",
      "name": "name",
      "uuid": "uuid"
  ]

  "data": [
      "created_at": "created_at",
      "name": "name",
      "uuid": "uuid"
  ]
