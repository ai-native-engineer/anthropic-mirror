<!-- source: https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url -->

# Create Enrollment URL
POST/v1/user_profiles/{user_profile_id}/enrollment_url
Create Enrollment URL
##### Path ParametersExpand Collapse 
user_profile_id: string
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#create_enrollment_url.user_profile_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#create_enrollment_url.betas)
BetaUserProfileEnrollmentURL object { expires_at, type, url } 
expires_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#beta_user_profile_enrollment_url.expires_at)
type: "enrollment_url"
Object type. Always `enrollment_url`.
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#beta_user_profile_enrollment_url.type)
url: string
Enrollment URL to send to the end user. Valid until `expires_at`.
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#beta_user_profile_enrollment_url.url)
[](https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url#beta_user_profile_enrollment_url)
Create Enrollment URL
cURL

curl https://api.anthropic.com/v1/user_profiles/$USER_PROFILE_ID/enrollment_url \
    -X POST \
    -H 'anthropic-beta: user-profiles-2026-03-24' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"

  "expires_at": "2026-03-15T10:15:00Z",
  "type": "enrollment_url",
  "url": "https://platform.claude.com/user-profiles/enrollment/M3J0bGJxZ2ppMnptbnB1"

  "expires_at": "2026-03-15T10:15:00Z",
  "type": "enrollment_url",
  "url": "https://platform.claude.com/user-profiles/enrollment/M3J0bGJxZ2ppMnptbnB1"
