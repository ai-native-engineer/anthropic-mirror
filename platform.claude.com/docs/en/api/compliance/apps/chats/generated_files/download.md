<!-- source: https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/download -->

# Download a Claude-generated file
GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content
Downloads the binary content of a file the assistant created via tool use.
##### Path ParametersExpand Collapse 
claude_gen_file_id: string
The generated-file id (e.g., 'claude_gen_file_abc123') as returned in `chat_messages[].generated_files[].id` from GET /apps/chats/{claude_chat_id}/messages.
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/download#download.claude_gen_file_id)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/download#download.x-api-key)
Download a Claude-generated file

curl https://api.anthropic.com/v1/compliance/apps/chats/generated-files/$CLAUDE_GEN_FILE_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
