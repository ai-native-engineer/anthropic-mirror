<!-- source: https://platform.claude.com/docs/en/api/skills/list-skill-versions -->

# List Skill Versions
GET/v1/skills/{skill_id}/versions
List Skill Versions
##### Path ParametersExpand Collapse 
skill_id: string
Unique identifier for the skill.
The format and length of IDs may change over time.
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#list.skill_id)
##### Query ParametersExpand Collapse 
limit: optional number
Number of items to return per page.
Defaults to `20`. Ranges from `1` to `1000`.
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#list.limit)
page: optional string
Optionally set to the `next_page` token from the previous response.
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#list.page)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#list.betas)
data: array of object { id, created_at, description, 5 more } 
List of skill versions.
Unique identifier for the skill version.
The format and length of IDs may change over time.
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#version_list_response.id)
created_at: string
ISO 8601 timestamp of when the skill version was created.
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#version_list_response.created_at)
description: string
Description of the skill version.
This is extracted from the SKILL.md file in the skill upload.
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#version_list_response.description)
directory: string
Directory name of the skill version.
This is the top-level directory name that was extracted from the uploaded files.
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#version_list_response.directory)
name: string
Human-readable name of the skill version.
This is extracted from the SKILL.md file in the skill upload.
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#version_list_response.name)
skill_id: string
Identifier for the skill that this version belongs to.
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#version_list_response.skill_id)
type: string
Object type.
For Skill Versions, this is always `"skill_version"`.
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#version_list_response.type)
version: string
Version identifier for the skill.
Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#version_list_response.version)
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#list)
has_more: boolean
Indicates if there are more results in the requested page direction.
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#list)
next_page: string
Token to provide in as `page` in the subsequent request to retrieve the next page of data.
[](https://platform.claude.com/docs/en/api/beta/skills/versions/list#list)
List Skill Versions
cURL

curl https://api.anthropic.com/v1/skills/$SKILL_ID/versions \
    -H 'anthropic-beta: skills-2025-10-02' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"

  "data": [
      "id": "skillver_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "description": "A custom skill for doing something useful",
      "directory": "my-skill",
      "name": "my-skill",
      "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
      "type": "type",
      "version": "1759178010641129"
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="

  "data": [
      "id": "skillver_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "description": "A custom skill for doing something useful",
      "directory": "my-skill",
      "name": "my-skill",
      "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
      "type": "type",
      "version": "1759178010641129"
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
