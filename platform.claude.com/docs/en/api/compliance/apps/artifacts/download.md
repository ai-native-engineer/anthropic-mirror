<!-- source: https://platform.claude.com/docs/en/api/compliance/apps/artifacts/download -->

# Download artifact content
GET/v1/compliance/apps/artifacts/{artifact_version_id}/content
Download the content of an artifact version for compliance purposes.
Returns the full text content of the artifact version.
##### Path ParametersExpand Collapse 
artifact_version_id: string
The artifact version ID (tagged ID, e.g., claude_artifact_version_abc123)
[](https://platform.claude.com/docs/en/api/compliance/apps/artifacts/download#download.artifact_version_id)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/apps/artifacts/download#download.x-api-key)
Download artifact content

curl https://api.anthropic.com/v1/compliance/apps/artifacts/$ARTIFACT_VERSION_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
