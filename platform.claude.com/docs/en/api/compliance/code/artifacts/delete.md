<!-- source: https://platform.claude.com/docs/en/api/compliance/code/artifacts/delete -->

# Delete Code Artifact
DELETE/v1/compliance/code/artifacts/{artifact_id}
Permanently deletes a Code Artifact and all its versions. This is a destructive operation that cannot be undone. A 200 response means the deletion is initiated and the Artifact is claimed; content removal completes asynchronously.
Returns 404 for Artifacts that don't exist or belong to another parent organization. Returns 404 on a repeated delete of an already-deleted Artifact.
##### Path ParametersExpand Collapse 
artifact_id: string
The Artifact ID (tagged ID, e.g., cart_abc123)
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/delete#delete.artifact_id)
##### Query ParametersExpand Collapse 
organization_uuid: optional string
The Artifact's owning organization UUID, from the list response. Strongly recommended — without it the route scans across child organizations and, for parents with many children, returns 400 rather than scanning further.
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/delete#delete.organization_uuid)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/delete#delete.x-api-key)
The ID of the Artifact that was deleted
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/delete#artifact_delete_response.id)
type: "code_artifact_deleted"
Constant string confirming deletion
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/delete#artifact_delete_response.type)
Delete Code Artifact

curl https://api.anthropic.com/v1/compliance/code/artifacts/$ARTIFACT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "id": "cart_xyz789",
  "type": "code_artifact_deleted"

  "id": "cart_xyz789",
  "type": "code_artifact_deleted"
