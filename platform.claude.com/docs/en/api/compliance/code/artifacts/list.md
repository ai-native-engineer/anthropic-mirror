<!-- source: https://platform.claude.com/docs/en/api/compliance/code/artifacts/list -->

# List Code Artifacts
GET/v1/compliance/code/artifacts
List Claude Code Artifacts owned by organizations under the parent organization.
Results are sorted by Artifact identifier within each batch of child organizations. Pages may be short or empty while `next_page` is still set — continue until `next_page` is absent. Artifacts are sorted by identifier (not creation time): an Artifact published during an export may land before the cursor and be omitted, so for a point-in-time-complete export re-enumerate after publishing quiesces.
Artifacts owned by a since-deleted child organization are not returned.
##### Query ParametersExpand Collapse 
limit: optional number
Maximum results (default: 20, max: 100)
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#list.limit)
organization_ids: optional array of string
Filter by organization IDs (accepts `org_...` or organization UUID, up to 500). Enumerate IDs via `GET /v1/compliance/organizations`.
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#list.organization_ids)
page: optional string
Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#list.page)
updated_at: optional object { gt, gte, lt, lte } 
gt: optional string
Return only Artifacts updated after this time (RFC 3339 format). See `updated_at.gte` for the completeness caveat.
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#list.updated_at.gt)
gte: optional string
Return only Artifacts updated at or after this time (RFC 3339 format). Time filters match an eventually-consistent index and Artifacts published before this field was recorded never match — omit the time filter for compliance-complete enumeration. For incremental export, apply a generous overlap margin between windows and dedupe by `id`: adjacent tiling silently misses items whose index update lagged their publish.
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#list.updated_at.gte)
lt: optional string
Return only Artifacts updated before this time (RFC 3339 format). Multiple time operators are AND-ed to the tightest bound. See `updated_at.gte` for the completeness caveat.
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#list.updated_at.lt)
lte: optional string
Return only Artifacts updated at or before this time (RFC 3339 format). See `updated_at.gte` for the completeness caveat.
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#list.updated_at.lte)
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#list.updated_at)
user_ids: optional array of string
Filter by owner user IDs (up to 200). Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#list.user_ids)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#list.x-api-key)
data: array of object { id, organization_id, organization_uuid, 6 more } 
Page of Artifacts
Artifact identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#artifact_list_response.id)
Deprecatedorganization_id: string
Organization identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#artifact_list_response.organization_id)
organization_uuid: string
Organization UUID this Artifact belongs to
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#artifact_list_response.organization_uuid)
owner_user_id: string
Artifact owner's user identifier (tagged ID). Always set, so attribution survives after the owner's account is deleted or the owner leaves every organization under the parent.
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#artifact_list_response.owner_user_id)
published_version_id: string
Identifier of the version a non-owner viewer would render when `read_mode` permits them — the version the owner has pinned for non-owner readers if one is pinned, otherwise the owner's latest. When `read_mode` is `owner` no non-owner renders any version; the field still reports which version would be served were read_mode widened.
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#artifact_list_response.published_version_id)
read_mode: "org" or "owner" or "users"
Who can view this Artifact: only its owner, a named set of users, or every member of its organization
"org"
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#artifact_list_response.read_mode%5B0%5D)
"owner"
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#artifact_list_response.read_mode%5B1%5D)
"users"
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#artifact_list_response.read_mode%5B2%5D)
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#artifact_list_response.read_mode)
updated_at: string
Artifact last update timestamp, or null for Artifacts published before this field was recorded
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#artifact_list_response.updated_at)
user: object { id, email_address } 
The user who owns a Code Artifact.
Fields that reference this type are null when the owner's account has been deleted or the owner is no longer a member of any organization under the parent organization.
User identifier (tagged ID)
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#artifact_list_response.user.id)
email_address: string
User's email address
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#artifact_list_response.user.email_address)
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#artifact_list_response.user)
versions: array of object { id, created_at, name } 
Up to roughly 20 most-recently-published versions of this Artifact (older versions are not retained). Metadata only — use `GET /v1/compliance/code/artifacts/{artifact_id}/versions/{version_id}` to download a version's content.
Opaque version identifier
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#artifact_list_response.versions.items.id)
created_at: string
When this version was published
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#artifact_list_response.versions.items.created_at)
name: string
Artifact title at this version. Falls back to the version identifier when the title for an older version is no longer retained.
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#artifact_list_response.versions.items.name)
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#artifact_list_response.versions)
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#list)
has_more: boolean
Whether `next_page` is set. When enumeration spans multiple organization batches this may be true for a page whose next page is empty — continue until `next_page` is absent.
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#list)
next_page: string
Token to retrieve the next page. Use this as the 'page' parameter in your next request
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list#list)
List Code Artifacts

curl https://api.anthropic.com/v1/compliance/code/artifacts \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "data": [
      "id": "id",
      "organization_id": "organization_id",
      "organization_uuid": "organization_uuid",
      "owner_user_id": "owner_user_id",
      "published_version_id": "published_version_id",
      "read_mode": "org",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "user": {
        "id": "id",
        "email_address": "email_address"
      "versions": [
          "id": "id",
          "created_at": "2019-12-27T18:11:19.117Z",
          "name": "name"
      ]
  ],
  "has_more": true,
  "next_page": "next_page"

  "data": [
      "id": "id",
      "organization_id": "organization_id",
      "organization_uuid": "organization_uuid",
      "owner_user_id": "owner_user_id",
      "published_version_id": "published_version_id",
      "read_mode": "org",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "user": {
        "id": "id",
        "email_address": "email_address"
      "versions": [
          "id": "id",
          "created_at": "2019-12-27T18:11:19.117Z",
          "name": "name"
      ]
  ],
  "has_more": true,
  "next_page": "next_page"
