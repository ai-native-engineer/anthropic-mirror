<!-- source: https://platform.claude.com/docs/en/api/admin-api/organization/get-me -->

# Get Current Organization
GET/v1/organizations/me
Retrieve information about the organization associated with the authenticated API key.
Organization object { id, name, type } 
ID of the Organization.
[](https://platform.claude.com/docs/en/api/admin/organizations/me#organization.id)
name: string
Name of the Organization.
[](https://platform.claude.com/docs/en/api/admin/organizations/me#organization.name)
type: "organization"
Object type.
For Organizations, this is always `"organization"`.
[](https://platform.claude.com/docs/en/api/admin/organizations/me#organization.type)
[](https://platform.claude.com/docs/en/api/admin/organizations/me#organization)
Get Current Organization

curl https://api.anthropic.com/v1/organizations/me \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "id": "12345678-1234-5678-1234-567812345678",
  "name": "Organization Name",
  "type": "organization"

  "id": "12345678-1234-5678-1234-567812345678",
  "name": "Organization Name",
  "type": "organization"
