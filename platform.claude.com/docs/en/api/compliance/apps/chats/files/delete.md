<!-- source: https://platform.claude.com/docs/en/api/compliance/apps/chats/files/delete -->

# Delete file
DELETE/v1/compliance/apps/chats/files/{claude_file_id}
Permanently deletes a specific file. This is a destructive operation that cannot be undone.
##### Path ParametersExpand Collapse 
claude_file_id: string
The file ID (tagged ID, e.g., claude_file_abc123)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/files/delete#delete.claude_file_id)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/files/delete#delete.x-api-key)
The ID of the file that was deleted
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/files/delete#file_delete_response.id)
type: optional "claude_file_deleted"
Constant string confirming deletion
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/files/delete#file_delete_response.type)
Delete file

curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "id": "claude_file_xyz789",
  "type": "claude_file_deleted"

  "id": "claude_file_xyz789",
  "type": "claude_file_deleted"
