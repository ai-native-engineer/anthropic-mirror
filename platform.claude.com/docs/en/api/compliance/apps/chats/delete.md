<!-- source: https://platform.claude.com/docs/en/api/compliance/apps/chats/delete -->

# Delete chat
DELETE/v1/compliance/apps/chats/{claude_chat_id}
Permanently deletes a chat and all associated messages and files. This is a destructive operation that cannot be undone.
##### Path ParametersExpand Collapse 
claude_chat_id: string
The chat ID (tagged ID, e.g., claude_chat_abc123)
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/delete#delete.claude_chat_id)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/delete#delete.x-api-key)
The ID of the Claude chat that was deleted
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/delete#chat_delete_response.id)
type: optional "claude_chat_deleted"
Constant string confirming deletion
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/delete#chat_delete_response.type)
Delete chat

curl https://api.anthropic.com/v1/compliance/apps/chats/$CLAUDE_CHAT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "id": "claude_chat_abc123",
  "type": "claude_chat_deleted"

  "id": "claude_chat_abc123",
  "type": "claude_chat_deleted"
