<!-- source: https://platform.claude.com/docs/en/api/compliance/code/artifacts/retrieve_version -->

# Download Code Artifact Version Content
GET/v1/compliance/code/artifacts/{artifact_id}/versions/{version_id}
Streams the content of one version of a Claude Code Artifact as the response body.
Returns 404 for Artifacts that don't exist or belong to another parent organization. A listed version id can start returning 404 if subsequent publishes rotated it out of retained history — re-list on 404. Returns 503 while the version's content upload is still in flight or was abandoned — retry with backoff. Oversized encoded content aborts mid-stream: headers and initial bytes arrive but the body terminates early — an aborted chunked transfer is the only truncation signal for encoded content. `Content-MD5` is emitted only for identity-stored content; validate against it when present.
##### Path ParametersExpand Collapse 
artifact_id: string
The Artifact ID (tagged ID, e.g., cart_abc123)
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/retrieve_version#retrieve_version.artifact_id)
version_id: string
Opaque version identifier from the Artifact's `versions` list
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/retrieve_version#retrieve_version.version_id)
##### Query ParametersExpand Collapse 
organization_uuid: optional string
The Artifact's owning organization UUID, from the list response. Strongly recommended — without it the route scans across child organizations and, for parents with many children, returns 400 rather than scanning further.
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/retrieve_version#retrieve_version.organization_uuid)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/code/artifacts/retrieve_version#retrieve_version.x-api-key)
Download Code Artifact Version Content

curl https://api.anthropic.com/v1/compliance/code/artifacts/$ARTIFACT_ID/versions/$VERSION_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
