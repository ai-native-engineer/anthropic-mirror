<!-- source: https://platform.claude.com/docs/en/api/compliance/apps/projects/delete -->

# Delete project
DELETE/v1/compliance/apps/projects/{project_id}
Delete a project for compliance purposes.
Hard-deletes the project and all its associated data including:
  * All project documents and files
  * All role assignments
  * Knowledge base (if RAG is enabled)
  * Sync sources

Project must have no attached chats - returns 409 if chats exist.
##### Path ParametersExpand Collapse 
project_id: string
The project ID (tagged ID, e.g., claude_proj_abc123)
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/delete#delete.project_id)
##### Header ParametersExpand Collapse 
"x-api-key": optional string
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/delete#delete.x-api-key)
The ID of the Claude project that was deleted
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/delete#project_delete_response.id)
type: optional "claude_project_deleted"
Constant string confirming deletion.
[](https://platform.claude.com/docs/en/api/compliance/apps/projects/delete#project_delete_response.type)
Delete project

curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"

  "id": "id",
  "type": "claude_project_deleted"

  "id": "id",
  "type": "claude_project_deleted"
