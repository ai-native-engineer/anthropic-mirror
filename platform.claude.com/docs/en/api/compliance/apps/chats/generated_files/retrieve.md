<!-- source: https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/retrieve -->

# Get Claude-generated file metadata
GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}
Returns metadata for a file the assistant created via tool use.
Use the sibling `/content` endpoint to download the bytes.
##### Path ParametersExpand Collapse 
claude_gen_file_id: string
The generated-file id (e.g., 'claude_gen_file_abc123') as returned in `chat_messages[].generated_files[].id` from GET /apps/chats/{claude_chat_id}/messages.
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/retrieve#retrieve.claude_gen_file_id)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/retrieve#retrieve.x-api-key)
Opaque generated-file id, e.g. 'claude_gen_file_abc123'.
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/retrieve#generated_file_retrieve_response.id)
claude_chat_id: string
The chat this generated file belongs to
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/retrieve#generated_file_retrieve_response.claude_chat_id)
created_at: string
File creation timestamp, when available
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/retrieve#generated_file_retrieve_response.created_at)
filename: string
Display name of the generated file
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/retrieve#generated_file_retrieve_response.filename)
md5: string
Lowercase hex MD5 of the stored file. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes.
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/retrieve#generated_file_retrieve_response.md5)
mime_type: string
MIME type of the stored file, when available
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/retrieve#generated_file_retrieve_response.mime_type)
size_bytes: number
Size in bytes of the stored file, when available
[](https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/retrieve#generated_file_retrieve_response.size_bytes)
Get Claude-generated file metadata

curl https://api.anthropic.com/v1/compliance/apps/chats/generated-files/$CLAUDE_GEN_FILE_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "id": "id",
  "claude_chat_id": "claude_chat_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "md5": "md5",
  "mime_type": "mime_type",
  "size_bytes": 0

  "id": "id",
  "claude_chat_id": "claude_chat_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "md5": "md5",
  "mime_type": "mime_type",
  "size_bytes": 0
