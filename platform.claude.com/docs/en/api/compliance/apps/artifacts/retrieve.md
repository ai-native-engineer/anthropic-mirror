<!-- source: https://platform.claude.com/docs/en/api/compliance/apps/artifacts/retrieve -->

# Get artifact metadata
GET/v1/compliance/apps/artifacts/{artifact_version_id}
Returns metadata for an artifact version, without the content body.
Use the sibling `/content` endpoint to fetch the artifact text. The `md5` and `size_bytes` fields here are computed over the UTF-8 encoding of that text, so a DLP consumer can dedupe or match hashes without downloading every artifact.
##### Path ParametersExpand Collapse 
artifact_version_id: string
The artifact version ID (tagged ID, e.g., claude_artifact_version_abc123)
[](https://platform.claude.com/docs/en/api/compliance/apps/artifacts/retrieve#retrieve.artifact_version_id)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/apps/artifacts/retrieve#retrieve.x-api-key)
Artifact ID e.g. 'claude_artifact_abc123'
[](https://platform.claude.com/docs/en/api/compliance/apps/artifacts/retrieve#artifact_retrieve_response.id)
artifact_type: string
MIME-like artifact type e.g. 'application/vnd.ant.code'
[](https://platform.claude.com/docs/en/api/compliance/apps/artifacts/retrieve#artifact_retrieve_response.artifact_type)
claude_chat_id: string
The chat this artifact belongs to
[](https://platform.claude.com/docs/en/api/compliance/apps/artifacts/retrieve#artifact_retrieve_response.claude_chat_id)
created_at: string
Artifact version creation timestamp
[](https://platform.claude.com/docs/en/api/compliance/apps/artifacts/retrieve#artifact_retrieve_response.created_at)
md5: string
Lowercase hex MD5 of the artifact content (UTF-8 encoded). Matches the `content` field returned by the sibling `/content` endpoint.
[](https://platform.claude.com/docs/en/api/compliance/apps/artifacts/retrieve#artifact_retrieve_response.md5)
size_bytes: number
Size in bytes of the artifact content (UTF-8 encoded)
[](https://platform.claude.com/docs/en/api/compliance/apps/artifacts/retrieve#artifact_retrieve_response.size_bytes)
title: string
Artifact title
[](https://platform.claude.com/docs/en/api/compliance/apps/artifacts/retrieve#artifact_retrieve_response.title)
version_id: string
Artifact version ID e.g. 'claude_artifact_version_abc123'
[](https://platform.claude.com/docs/en/api/compliance/apps/artifacts/retrieve#artifact_retrieve_response.version_id)
Get artifact metadata

curl https://api.anthropic.com/v1/compliance/apps/artifacts/$ARTIFACT_VERSION_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "id": "id",
  "artifact_type": "artifact_type",
  "claude_chat_id": "claude_chat_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "md5": "md5",
  "size_bytes": 0,
  "title": "title",
  "version_id": "version_id"

  "id": "id",
  "artifact_type": "artifact_type",
  "claude_chat_id": "claude_chat_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "md5": "md5",
  "size_bytes": 0,
  "title": "title",
  "version_id": "version_id"
