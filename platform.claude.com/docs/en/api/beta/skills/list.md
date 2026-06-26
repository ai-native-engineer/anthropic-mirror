<!-- source: https://platform.claude.com/docs/en/api/beta/skills/list -->

# List Skills
GET/v1/skills
List Skills
##### Query ParametersExpand Collapse 
limit: optional number
Number of results to return per page.
Maximum value is 100. Defaults to 20.
[](https://platform.claude.com/docs/en/api/beta/skills/list#list.limit)
page: optional string
Pagination token for fetching a specific page of results.
Pass the value from a previous response's `next_page` field to get the next page of results.
[](https://platform.claude.com/docs/en/api/beta/skills/list#list.page)
source: optional string
Filter skills by source.
If provided, only skills from the specified source will be returned:
  * `"custom"`: only return user-created skills
  * `"anthropic"`: only return Anthropic-created skills

[](https://platform.claude.com/docs/en/api/beta/skills/list#list.source)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/skills/list#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/skills/list#list.betas)
data: array of object { id, created_at, display_title, 4 more } 
List of skills.
Unique identifier for the skill.
The format and length of IDs may change over time.
[](https://platform.claude.com/docs/en/api/beta/skills/list#skill_list_response.id)
created_at: string
ISO 8601 timestamp of when the skill was created.
[](https://platform.claude.com/docs/en/api/beta/skills/list#skill_list_response.created_at)
display_title: string
Display title for the skill.
This is a human-readable label that is not included in the prompt sent to the model.
[](https://platform.claude.com/docs/en/api/beta/skills/list#skill_list_response.display_title)
latest_version: string
The latest version identifier for the skill.
This represents the most recent version of the skill that has been created.
[](https://platform.claude.com/docs/en/api/beta/skills/list#skill_list_response.latest_version)
source: string
Source of the skill.
This may be one of the following values:
  * `"custom"`: the skill was created by a user
  * `"anthropic"`: the skill was created by Anthropic

[](https://platform.claude.com/docs/en/api/beta/skills/list#skill_list_response.source)
type: string
Object type.
For Skills, this is always `"skill"`.
[](https://platform.claude.com/docs/en/api/beta/skills/list#skill_list_response.type)
updated_at: string
ISO 8601 timestamp of when the skill was last updated.
[](https://platform.claude.com/docs/en/api/beta/skills/list#skill_list_response.updated_at)
[](https://platform.claude.com/docs/en/api/beta/skills/list#list)
has_more: boolean
Whether there are more results available.
If `true`, there are additional results that can be fetched using the `next_page` token.
[](https://platform.claude.com/docs/en/api/beta/skills/list#list)
next_page: string
Token for fetching the next page of results.
If `null`, there are no more results available. Pass this value to the `page_token` parameter in the next request to get the next page.
[](https://platform.claude.com/docs/en/api/beta/skills/list#list)
List Skills
cURL

curl https://api.anthropic.com/v1/skills \
    -H 'anthropic-beta: skills-2025-10-02' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"

  "data": [
      "id": "skill_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_title": "My Custom Skill",
      "latest_version": "1759178010641129",
      "source": "custom",
      "type": "type",
      "updated_at": "2024-10-30T23:58:27.427722Z"
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="

  "data": [
      "id": "skill_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_title": "My Custom Skill",
      "latest_version": "1759178010641129",
      "source": "custom",
      "type": "type",
      "updated_at": "2024-10-30T23:58:27.427722Z"
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
