<!-- source: https://platform.claude.com/docs/en/api/compliance/apps/chats/files/download -->

# Download file content
GET/v1/compliance/apps/chats/files/{claude_file_id}/content
Downloads the binary content of a file referenced in chat messages.
##### Path ParametersExpand Collapse 
claude_file_id: string
The file ID (tagged ID, e.g., claude_file_abc123)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/files/download#download.claude_file_id)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/files/download#download.x-api-key)
Download file content

curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
