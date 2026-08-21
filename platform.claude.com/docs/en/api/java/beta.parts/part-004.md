<!-- source: https://platform.claude.com/docs/en/api/java/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/java/beta -->

<!-- chunk-start -->

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class SkillListResponse:`

  - `String id`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `String createdAt`

    ISO 8601 timestamp of when the skill was created.

  - `Optional<String> displayTitle`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `Optional<String> latestVersion`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `String source`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `String type`

    Object type.

    For Skills, this is always `"skill"`.

  - `String updatedAt`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.skills.SkillListPage;
import com.anthropic.models.beta.skills.SkillListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        SkillListPage page = client.beta().skills().list();
    }
}
```

#### Response

```json
{
  "data": [
    {
      "id": "skill_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_title": "My Custom Skill",
      "latest_version": "1759178010641129",
      "source": "custom",
      "type": "type",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Skill

`SkillRetrieveResponse beta().skills().retrieve(SkillRetrieveParamsparams = SkillRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/skills/{skill_id}`

Get Skill

### Parameters

- `SkillRetrieveParams params`

  - `Optional<String> skillId`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class SkillRetrieveResponse:`

  - `String id`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `String createdAt`

    ISO 8601 timestamp of when the skill was created.

  - `Optional<String> displayTitle`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `Optional<String> latestVersion`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `String source`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `String type`

    Object type.

    For Skills, this is always `"skill"`.

  - `String updatedAt`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.skills.SkillRetrieveParams;
import com.anthropic.models.beta.skills.SkillRetrieveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        SkillRetrieveResponse skill = client.beta().skills().retrieve("skill_id");
    }
}
```

#### Response

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_title": "My Custom Skill",
  "latest_version": "1759178010641129",
  "source": "custom",
  "type": "type",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

## Delete Skill

`SkillDeleteResponse beta().skills().delete(SkillDeleteParamsparams = SkillDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/v1/skills/{skill_id}`

Delete Skill

### Parameters

- `SkillDeleteParams params`

  - `Optional<String> skillId`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class SkillDeleteResponse:`

  - `String id`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `String type`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.skills.SkillDeleteParams;
import com.anthropic.models.beta.skills.SkillDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        SkillDeleteResponse skill = client.beta().skills().delete("skill_id");
    }
}
```

#### Response

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type"
}
```

# Versions

## Create Skill Version

`VersionCreateResponse beta().skills().versions().create(VersionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/skills/{skill_id}/versions`

Create Skill Version

### Parameters

- `VersionCreateParams params`

  - `Optional<String> skillId`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `List<String> files`

    Files to upload for the skill.

    All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

### Returns

- `class VersionCreateResponse:`

  - `String id`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `String createdAt`

    ISO 8601 timestamp of when the skill version was created.

  - `String description`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `String directory`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `String name`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `String skillId`

    Identifier for the skill that this version belongs to.

  - `String type`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `String version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.skills.versions.VersionCreateParams;
import com.anthropic.models.beta.skills.versions.VersionCreateResponse;
import java.io.ByteArrayInputStream;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        VersionCreateParams params = VersionCreateParams.builder()
            .skillId("skill_id")
            .addFile(new ByteArrayInputStream("Example data".getBytes()))
            .build();
        VersionCreateResponse version = client.beta().skills().versions().create(params);
    }
}
```

#### Response

```json
{
  "id": "skillver_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "A custom skill for doing something useful",
  "directory": "my-skill",
  "name": "my-skill",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type",
  "version": "1759178010641129"
}
```

## List Skill Versions

`VersionListPage beta().skills().versions().list(VersionListParamsparams = VersionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/skills/{skill_id}/versions`

List Skill Versions

### Parameters

- `VersionListParams params`

  - `Optional<String> skillId`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `Optional<Long> limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

  - `Optional<String> page`

    Optionally set to the `next_page` token from the previous response.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class VersionListResponse:`

  - `String id`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `String createdAt`

    ISO 8601 timestamp of when the skill version was created.

  - `String description`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `String directory`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `String name`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `String skillId`

    Identifier for the skill that this version belongs to.

  - `String type`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `String version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.skills.versions.VersionListPage;
import com.anthropic.models.beta.skills.versions.VersionListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        VersionListPage page = client.beta().skills().versions().list("skill_id");
    }
}
```

#### Response

```json
{
  "data": [
    {
      "id": "skillver_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "description": "A custom skill for doing something useful",
      "directory": "my-skill",
      "name": "my-skill",
      "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
      "type": "type",
      "version": "1759178010641129"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Download Skill Version Content

`HttpResponse beta().skills().versions().download(VersionDownloadParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/skills/{skill_id}/versions/{version}/content`

Download a skill version's content as a zip archive.

### Parameters

- `VersionDownloadParams params`

  - `String skillId`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `Optional<String> version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.http.HttpResponse;
import com.anthropic.models.beta.skills.versions.VersionDownloadParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        VersionDownloadParams params = VersionDownloadParams.builder()
            .skillId("skill_id")
            .version("version")
            .build();
        HttpResponse response = client.beta().skills().versions().download(params);
    }
}
```

## Get Skill Version

`VersionRetrieveResponse beta().skills().versions().retrieve(VersionRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/skills/{skill_id}/versions/{version}`

Get Skill Version

### Parameters

- `VersionRetrieveParams params`

  - `String skillId`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `Optional<String> version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class VersionRetrieveResponse:`

  - `String id`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `String createdAt`

    ISO 8601 timestamp of when the skill version was created.

  - `String description`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `String directory`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `String name`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `String skillId`

    Identifier for the skill that this version belongs to.

  - `String type`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `String version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.skills.versions.VersionRetrieveParams;
import com.anthropic.models.beta.skills.versions.VersionRetrieveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        VersionRetrieveParams params = VersionRetrieveParams.builder()
            .skillId("skill_id")
            .version("version")
            .build();
        VersionRetrieveResponse version = client.beta().skills().versions().retrieve(params);
    }
}
```

#### Response

```json
{
  "id": "skillver_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "A custom skill for doing something useful",
  "directory": "my-skill",
  "name": "my-skill",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type",
  "version": "1759178010641129"
}
```

## Delete Skill Version

`VersionDeleteResponse beta().skills().versions().delete(VersionDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

### Parameters

- `VersionDeleteParams params`

  - `String skillId`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `Optional<String> version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class VersionDeleteResponse:`

  - `String id`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `String type`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.skills.versions.VersionDeleteParams;
import com.anthropic.models.beta.skills.versions.VersionDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        VersionDeleteParams params = VersionDeleteParams.builder()
            .skillId("skill_id")
            .version("version")
            .build();
        VersionDeleteResponse version = client.beta().skills().versions().delete(params);
    }
}
```

#### Response

```json
{
  "id": "1759178010641129",
  "type": "type"
}
```

# User Profiles

## Create User Profile

`BetaUserProfile beta().userProfiles().create(UserProfileCreateParamsparams = UserProfileCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/user_profiles`

Create User Profile

### Parameters

- `UserProfileCreateParams params`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `Optional<AccessType> accessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `APPLICATION("application")`

    - `PASSTHROUGH("passthrough")`

  - `Optional<String> externalId`

    Platform's own identifier for this user. Not enforced unique. Maximum 255 characters.

  - `Optional<Metadata> metadata`

    Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

  - `Optional<String> name`

    Optional for all profiles. Real-world name of the entity this profile represents (company or individual); for a resold-to company (`relationship` `resold` / `access_type` `passthrough`), that company's name where known. Maximum 255 characters.

  - `Optional<Relationship> relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `EXTERNAL("external")`

    - `RESOLD("resold")`

    - `INTERNAL("internal")`

### Returns

- `class BetaUserProfile:`

  - `String id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `TrustGrants trustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `Status status`

      Status of the trust grant.

      - `ACTIVE("active")`

      - `PENDING("pending")`

      - `REJECTED("rejected")`

  - `Type type`

    Object type. Always `user_profile`.

    - `USER_PROFILE("user_profile")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<AccessType> accessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `APPLICATION("application")`

    - `PASSTHROUGH("passthrough")`

  - `Optional<String> externalId`

    Platform's own identifier for this user. Not enforced unique.

  - `Optional<String> name`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Optional<Relationship> relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `EXTERNAL("external")`

    - `RESOLD("resold")`

    - `INTERNAL("internal")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.userprofiles.BetaUserProfile;
import com.anthropic.models.beta.userprofiles.UserProfileCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaUserProfile betaUserProfile = client.beta().userProfiles().create();
    }
}
```

#### Response

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "access_type": "application",
  "external_id": "user_12345",
  "name": "Example User",
  "relationship": "external"
}
```

## List User Profiles

`UserProfileListPage beta().userProfiles().list(UserProfileListParamsparams = UserProfileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/user_profiles`

List User Profiles

### Parameters

- `UserProfileListParams params`

  - `Optional<Long> limit`

    Query parameter for limit

  - `Optional<Order> order`

    Query parameter for order

    - `ASC("asc")`

    - `DESC("desc")`

  - `Optional<String> page`

    Query parameter for page

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaUserProfile:`

  - `String id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `TrustGrants trustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `Status status`

      Status of the trust grant.

      - `ACTIVE("active")`

      - `PENDING("pending")`

      - `REJECTED("rejected")`

  - `Type type`

    Object type. Always `user_profile`.

    - `USER_PROFILE("user_profile")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<AccessType> accessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `APPLICATION("application")`

    - `PASSTHROUGH("passthrough")`

  - `Optional<String> externalId`

    Platform's own identifier for this user. Not enforced unique.

  - `Optional<String> name`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Optional<Relationship> relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `EXTERNAL("external")`

    - `RESOLD("resold")`

    - `INTERNAL("internal")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.userprofiles.UserProfileListPage;
import com.anthropic.models.beta.userprofiles.UserProfileListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        UserProfileListPage page = client.beta().userProfiles().list();
    }
}
```

#### Response

```json
{
  "data": [
    {
      "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
      "created_at": "2026-03-15T10:00:00Z",
      "metadata": {},
      "trust_grants": {
        "cyber": {
          "status": "active"
        }
      },
      "type": "user_profile",
      "updated_at": "2026-03-15T10:00:00Z",
      "access_type": "application",
      "external_id": "user_12345",
      "name": "Example User",
      "relationship": "external"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get User Profile

`BetaUserProfile beta().userProfiles().retrieve(UserProfileRetrieveParamsparams = UserProfileRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/user_profiles/{user_profile_id}`

Get User Profile

### Parameters

- `UserProfileRetrieveParams params`

  - `Optional<String> userProfileId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaUserProfile:`

  - `String id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `TrustGrants trustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `Status status`

      Status of the trust grant.

      - `ACTIVE("active")`

      - `PENDING("pending")`

      - `REJECTED("rejected")`

  - `Type type`

    Object type. Always `user_profile`.

    - `USER_PROFILE("user_profile")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<AccessType> accessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `APPLICATION("application")`

    - `PASSTHROUGH("passthrough")`

  - `Optional<String> externalId`

    Platform's own identifier for this user. Not enforced unique.

  - `Optional<String> name`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Optional<Relationship> relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `EXTERNAL("external")`

    - `RESOLD("resold")`

    - `INTERNAL("internal")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.userprofiles.BetaUserProfile;
import com.anthropic.models.beta.userprofiles.UserProfileRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaUserProfile betaUserProfile = client.beta().userProfiles().retrieve("uprof_011CZkZCu8hGbp5mYRQgUmz9");
    }
}
```

#### Response

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "access_type": "application",
  "external_id": "user_12345",
  "name": "Example User",
  "relationship": "external"
}
```

## Update User Profile

`BetaUserProfile beta().userProfiles().update(UserProfileUpdateParamsparams = UserProfileUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/user_profiles/{user_profile_id}`

Update User Profile

### Parameters

- `UserProfileUpdateParams params`

  - `Optional<String> userProfileId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `Optional<AccessType> accessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `APPLICATION("application")`

    - `PASSTHROUGH("passthrough")`

  - `Optional<String> externalId`

    If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters.

  - `Optional<Metadata> metadata`

    Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

  - `Optional<String> name`

    If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

  - `Optional<Relationship> relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `EXTERNAL("external")`

    - `RESOLD("resold")`

    - `INTERNAL("internal")`

### Returns

- `class BetaUserProfile:`

  - `String id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `TrustGrants trustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `Status status`

      Status of the trust grant.

      - `ACTIVE("active")`

      - `PENDING("pending")`

      - `REJECTED("rejected")`

  - `Type type`

    Object type. Always `user_profile`.

    - `USER_PROFILE("user_profile")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<AccessType> accessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `APPLICATION("application")`

    - `PASSTHROUGH("passthrough")`

  - `Optional<String> externalId`

    Platform's own identifier for this user. Not enforced unique.

  - `Optional<String> name`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Optional<Relationship> relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `EXTERNAL("external")`

    - `RESOLD("resold")`

    - `INTERNAL("internal")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.userprofiles.BetaUserProfile;
import com.anthropic.models.beta.userprofiles.UserProfileUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaUserProfile betaUserProfile = client.beta().userProfiles().update("uprof_011CZkZCu8hGbp5mYRQgUmz9");
    }
}
```

#### Response

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "access_type": "application",
  "external_id": "user_12345",
  "name": "Example User",
  "relationship": "external"
}
```

## Create Enrollment URL

`BetaUserProfileEnrollmentUrl beta().userProfiles().createEnrollmentUrl(UserProfileCreateEnrollmentUrlParamsparams = UserProfileCreateEnrollmentUrlParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

### Parameters

- `UserProfileCreateEnrollmentUrlParams params`

  - `Optional<String> userProfileId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaUserProfileEnrollmentUrl:`

  - `LocalDateTime expiresAt`

    A timestamp in RFC 3339 format

  - `Type type`

    Object type. Always `enrollment_url`.

    - `ENROLLMENT_URL("enrollment_url")`

  - `String url`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.userprofiles.BetaUserProfileEnrollmentUrl;
import com.anthropic.models.beta.userprofiles.UserProfileCreateEnrollmentUrlParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaUserProfileEnrollmentUrl betaUserProfileEnrollmentUrl = client.beta().userProfiles().createEnrollmentUrl("uprof_011CZkZCu8hGbp5mYRQgUmz9");
    }
}
```

#### Response

```json
{
  "expires_at": "2026-03-15T10:15:00Z",
  "type": "enrollment_url",
  "url": "https://platform.claude.com/user-profiles/enrollment/M3J0bGJxZ2ppMnptbnB1"
}
```

## Domain Types

### Beta User Profile

- `class BetaUserProfile:`

  - `String id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `TrustGrants trustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `Status status`

      Status of the trust grant.

      - `ACTIVE("active")`

      - `PENDING("pending")`

      - `REJECTED("rejected")`

  - `Type type`

    Object type. Always `user_profile`.

    - `USER_PROFILE("user_profile")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<AccessType> accessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `APPLICATION("application")`

    - `PASSTHROUGH("passthrough")`

  - `Optional<String> externalId`

    Platform's own identifier for this user. Not enforced unique.

  - `Optional<String> name`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Optional<Relationship> relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `EXTERNAL("external")`

    - `RESOLD("resold")`

    - `INTERNAL("internal")`

### Beta User Profile Enrollment URL

- `class BetaUserProfileEnrollmentUrl:`

  - `LocalDateTime expiresAt`

    A timestamp in RFC 3339 format

  - `Type type`

    Object type. Always `enrollment_url`.

    - `ENROLLMENT_URL("enrollment_url")`

  - `String url`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Beta User Profile Trust Grant

- `class BetaUserProfileTrustGrant:`

  - `Status status`

    Status of the trust grant.

    - `ACTIVE("active")`

    - `PENDING("pending")`

    - `REJECTED("rejected")`

# Dreams

## Create a Dream

`BetaDream beta().dreams().create(DreamCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/dreams`

Create a Dream

### Parameters

- `DreamCreateParams params`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `List<BetaDreamInput> inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `String memoryStoreId`

      - `Type type`

        - `MEMORY_STORE("memory_store")`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `List<String> sessionIds`

      - `Type type`

        - `SESSIONS("sessions")`

  - `Model model`

    Model identifier and configuration applied to every pipeline stage.

    - `String`

    - `class BetaDreamModelConfigParam:`

      Model identifier and configuration applied to every pipeline stage.

      - `String id`

        Model identifier, e.g. "claude-opus-5". 1-256 characters.

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

  - `Optional<String> instructions`

  - `Optional<BetaOutputBehavior> outputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> endedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaDreamError> error`

    Failure detail for a Dream whose `status` is `failed`.

    - `String message`

    - `String type`

  - `List<BetaDreamInput> inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `String memoryStoreId`

      - `Type type`

        - `MEMORY_STORE("memory_store")`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `List<String> sessionIds`

      - `Type type`

        - `SESSIONS("sessions")`

  - `Optional<String> instructions`

  - `BetaDreamModelConfig model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `String id`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

  - `BetaOutputBehavior outputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type type`

        - `CREATE_NEW("create_new")`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `String memoryStoreId`

      - `Type type`

        - `UPDATE_EXISTING("update_existing")`

  - `List<BetaDreamOutput> outputs`

    - `String memoryStoreId`

    - `Type type`

      - `MEMORY_STORE("memory_store")`

  - `Optional<String> sessionId`

  - `BetaDreamStatus status`

    Lifecycle status of a Dream.

    - `PENDING("pending")`

    - `RUNNING("running")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `CANCELED("canceled")`

  - `Type type`

    - `DREAM("dream")`

  - `BetaDreamUsage usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `long cacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `long cacheReadInputTokens`

      Total tokens read from prompt cache.

    - `long inputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `long outputTokens`

      Total output tokens generated across every pipeline stage.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.dreams.BetaDream;
import com.anthropic.models.beta.dreams.DreamCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        DreamCreateParams params = DreamCreateParams.builder()
            .addMemoryStoreInput("x")
            .model("string")
            .build();
        BetaDream betaDream = client.beta().dreams().create(params);
    }
}
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "output_behavior": {
    "type": "create_new"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## List Dreams

`DreamListPage beta().dreams().list(DreamListParamsparams = DreamListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/dreams`

List Dreams

### Parameters

- `DreamListParams params`

  - `Optional<LocalDateTime> createdAtGt`

    Return dreams with `created_at` strictly after this timestamp (exclusive lower bound, RFC 3339). Unset applies no lower bound.

  - `Optional<LocalDateTime> createdAtLt`

    Return dreams with `created_at` strictly before this timestamp (exclusive upper bound, RFC 3339). Unset applies no upper bound.

  - `Optional<Boolean> includeArchived`

    Query parameter for include_archived

  - `Optional<Long> limit`

    Query parameter for limit

  - `Optional<String> page`

    Query parameter for page

  - `Optional<List<BetaDreamStatus>> statuses`

    Filter by lifecycle status. Repeat the parameter to match any of multiple statuses. Empty applies no status filter.

    - `PENDING("pending")`

    - `RUNNING("running")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `CANCELED("canceled")`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> endedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaDreamError> error`

    Failure detail for a Dream whose `status` is `failed`.

    - `String message`

    - `String type`

  - `List<BetaDreamInput> inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `String memoryStoreId`

      - `Type type`

        - `MEMORY_STORE("memory_store")`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `List<String> sessionIds`

      - `Type type`

        - `SESSIONS("sessions")`

  - `Optional<String> instructions`

  - `BetaDreamModelConfig model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `String id`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

  - `BetaOutputBehavior outputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type type`

        - `CREATE_NEW("create_new")`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `String memoryStoreId`

      - `Type type`

        - `UPDATE_EXISTING("update_existing")`

  - `List<BetaDreamOutput> outputs`

    - `String memoryStoreId`

    - `Type type`

      - `MEMORY_STORE("memory_store")`

  - `Optional<String> sessionId`

  - `BetaDreamStatus status`

    Lifecycle status of a Dream.

    - `PENDING("pending")`

    - `RUNNING("running")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `CANCELED("canceled")`

  - `Type type`

    - `DREAM("dream")`

  - `BetaDreamUsage usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `long cacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `long cacheReadInputTokens`

      Total tokens read from prompt cache.

    - `long inputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `long outputTokens`

      Total output tokens generated across every pipeline stage.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.dreams.DreamListPage;
import com.anthropic.models.beta.dreams.DreamListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        DreamListPage page = client.beta().dreams().list();
    }
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "ended_at": "2019-12-27T18:11:19.117Z",
      "error": {
        "message": "message",
        "type": "type"
      },
      "inputs": [
        {
          "memory_store_id": "x",
          "type": "memory_store"
        }
      ],
      "instructions": "instructions",
      "model": {
        "id": "x",
        "speed": "standard"
      },
      "output_behavior": {
        "type": "create_new"
      },
      "outputs": [
        {
          "memory_store_id": "memory_store_id",
          "type": "memory_store"
        }
      ],
      "session_id": "session_id",
      "status": "pending",
      "type": "dream",
      "usage": {
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0
      }
    }
  ],
  "next_page": "next_page"
}
```

## Get a Dream

`BetaDream beta().dreams().retrieve(DreamRetrieveParamsparams = DreamRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/dreams/{dream_id}`

Get a Dream

### Parameters

- `DreamRetrieveParams params`

  - `Optional<String> dreamId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> endedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaDreamError> error`

    Failure detail for a Dream whose `status` is `failed`.

    - `String message`

    - `String type`

  - `List<BetaDreamInput> inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `String memoryStoreId`

      - `Type type`

        - `MEMORY_STORE("memory_store")`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `List<String> sessionIds`

      - `Type type`

        - `SESSIONS("sessions")`

  - `Optional<String> instructions`

  - `BetaDreamModelConfig model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `String id`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

  - `BetaOutputBehavior outputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type type`

        - `CREATE_NEW("create_new")`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `String memoryStoreId`

      - `Type type`

        - `UPDATE_EXISTING("update_existing")`

  - `List<BetaDreamOutput> outputs`

    - `String memoryStoreId`

    - `Type type`

      - `MEMORY_STORE("memory_store")`

  - `Optional<String> sessionId`

  - `BetaDreamStatus status`

    Lifecycle status of a Dream.

    - `PENDING("pending")`

    - `RUNNING("running")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `CANCELED("canceled")`

  - `Type type`

    - `DREAM("dream")`

  - `BetaDreamUsage usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `long cacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `long cacheReadInputTokens`

      Total tokens read from prompt cache.

    - `long inputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `long outputTokens`

      Total output tokens generated across every pipeline stage.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.dreams.BetaDream;
import com.anthropic.models.beta.dreams.DreamRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaDream betaDream = client.beta().dreams().retrieve("dream_id");
    }
}
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "output_behavior": {
    "type": "create_new"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## Cancel a Dream

`BetaDream beta().dreams().cancel(DreamCancelParamsparams = DreamCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/dreams/{dream_id}/cancel`

Cancel a Dream

### Parameters

- `DreamCancelParams params`

  - `Optional<String> dreamId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> endedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaDreamError> error`

    Failure detail for a Dream whose `status` is `failed`.

    - `String message`

    - `String type`

  - `List<BetaDreamInput> inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `String memoryStoreId`

      - `Type type`

        - `MEMORY_STORE("memory_store")`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `List<String> sessionIds`

      - `Type type`

        - `SESSIONS("sessions")`

  - `Optional<String> instructions`

  - `BetaDreamModelConfig model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `String id`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

  - `BetaOutputBehavior outputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type type`

        - `CREATE_NEW("create_new")`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `String memoryStoreId`

      - `Type type`

        - `UPDATE_EXISTING("update_existing")`

  - `List<BetaDreamOutput> outputs`

    - `String memoryStoreId`

    - `Type type`

      - `MEMORY_STORE("memory_store")`

  - `Optional<String> sessionId`

  - `BetaDreamStatus status`

    Lifecycle status of a Dream.

    - `PENDING("pending")`

    - `RUNNING("running")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `CANCELED("canceled")`

  - `Type type`

    - `DREAM("dream")`

  - `BetaDreamUsage usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `long cacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `long cacheReadInputTokens`

      Total tokens read from prompt cache.

    - `long inputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `long outputTokens`

      Total output tokens generated across every pipeline stage.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.dreams.BetaDream;
import com.anthropic.models.beta.dreams.DreamCancelParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaDream betaDream = client.beta().dreams().cancel("dream_id");
    }
}
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "output_behavior": {
    "type": "create_new"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## Archive a Dream

`BetaDream beta().dreams().archive(DreamArchiveParamsparams = DreamArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/dreams/{dream_id}/archive`

Archive a Dream

### Parameters

- `DreamArchiveParams params`

  - `Optional<String> dreamId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> endedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaDreamError> error`

    Failure detail for a Dream whose `status` is `failed`.

    - `String message`

    - `String type`

  - `List<BetaDreamInput> inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `String memoryStoreId`

      - `Type type`

        - `MEMORY_STORE("memory_store")`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `List<String> sessionIds`

      - `Type type`

        - `SESSIONS("sessions")`

  - `Optional<String> instructions`

  - `BetaDreamModelConfig model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `String id`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

  - `BetaOutputBehavior outputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type type`

        - `CREATE_NEW("create_new")`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `String memoryStoreId`

      - `Type type`

        - `UPDATE_EXISTING("update_existing")`

  - `List<BetaDreamOutput> outputs`

    - `String memoryStoreId`

    - `Type type`

      - `MEMORY_STORE("memory_store")`

  - `Optional<String> sessionId`

  - `BetaDreamStatus status`

    Lifecycle status of a Dream.

    - `PENDING("pending")`

    - `RUNNING("running")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `CANCELED("canceled")`

  - `Type type`

    - `DREAM("dream")`

  - `BetaDreamUsage usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `long cacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `long cacheReadInputTokens`

      Total tokens read from prompt cache.

    - `long inputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `long outputTokens`

      Total output tokens generated across every pipeline stage.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.dreams.BetaDream;
import com.anthropic.models.beta.dreams.DreamArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaDream betaDream = client.beta().dreams().archive("dream_id");
    }
}
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "output_behavior": {
    "type": "create_new"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## Domain Types

### Beta Dream

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> endedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaDreamError> error`

    Failure detail for a Dream whose `status` is `failed`.

    - `String message`

    - `String type`

  - `List<BetaDreamInput> inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `String memoryStoreId`

      - `Type type`

        - `MEMORY_STORE("memory_store")`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `List<String> sessionIds`

      - `Type type`

        - `SESSIONS("sessions")`

  - `Optional<String> instructions`

  - `BetaDreamModelConfig model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `String id`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

  - `BetaOutputBehavior outputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type type`

        - `CREATE_NEW("create_new")`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `String memoryStoreId`

      - `Type type`

        - `UPDATE_EXISTING("update_existing")`

  - `List<BetaDreamOutput> outputs`

    - `String memoryStoreId`

    - `Type type`

      - `MEMORY_STORE("memory_store")`

  - `Optional<String> sessionId`

  - `BetaDreamStatus status`

    Lifecycle status of a Dream.

    - `PENDING("pending")`

    - `RUNNING("running")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `CANCELED("canceled")`

  - `Type type`

    - `DREAM("dream")`

  - `BetaDreamUsage usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `long cacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `long cacheReadInputTokens`

      Total tokens read from prompt cache.

    - `long inputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `long outputTokens`

      Total output tokens generated across every pipeline stage.

### Beta Dream Error

- `class BetaDreamError:`

  Failure detail for a Dream whose `status` is `failed`.

  - `String message`

  - `String type`

### Beta Dream Input

- `class BetaDreamInput: A class that can be one of several variants.union`

  An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

  - `class BetaDreamMemoryStoreInput:`

    An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

    - `String memoryStoreId`

    - `Type type`

      - `MEMORY_STORE("memory_store")`

  - `class BetaDreamSessionsInput:`

    Input session transcripts the dream reads.

    - `List<String> sessionIds`

    - `Type type`

      - `SESSIONS("sessions")`

### Beta Dream Memory Store Input

- `class BetaDreamMemoryStoreInput:`

  An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

  - `String memoryStoreId`

  - `Type type`

    - `MEMORY_STORE("memory_store")`

### Beta Dream Memory Store Output

- `class BetaDreamMemoryStoreOutput:`

  An output memory store the dream writes consolidated memories into.

  - `String memoryStoreId`

  - `Type type`

    - `MEMORY_STORE("memory_store")`

### Beta Dream Model Config

- `class BetaDreamModelConfig:`

  Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

  - `String id`

    Model identifier, e.g. "claude-opus-5". 1-256 characters.

  - `Optional<Speed> speed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `STANDARD("standard")`

    - `FAST("fast")`

### Beta Dream Model Config Param

- `class BetaDreamModelConfigParam:`

  Model identifier and configuration applied to every pipeline stage.

  - `String id`

    Model identifier, e.g. "claude-opus-5". 1-256 characters.

  - `Optional<Speed> speed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `STANDARD("standard")`

    - `FAST("fast")`

### Beta Dream Output

- `class BetaDreamOutput:`

  An output memory store the dream writes consolidated memories into.

  - `String memoryStoreId`

  - `Type type`

    - `MEMORY_STORE("memory_store")`

### Beta Dream Sessions Input

- `class BetaDreamSessionsInput:`

  Input session transcripts the dream reads.

  - `List<String> sessionIds`

  - `Type type`

    - `SESSIONS("sessions")`

### Beta Dream Status

- `enum BetaDreamStatus:`

  Lifecycle status of a Dream.

  - `PENDING("pending")`

  - `RUNNING("running")`

  - `COMPLETED("completed")`

  - `FAILED("failed")`

  - `CANCELED("canceled")`

### Beta Dream Usage

- `class BetaDreamUsage:`

  Cumulative token usage for the dream across every pipeline stage.

  - `long cacheCreationInputTokens`

    Total tokens used to create prompt-cache entries (sum of all TTL tiers).

  - `long cacheReadInputTokens`

    Total tokens read from prompt cache.

  - `long inputTokens`

    Total uncached input tokens consumed across every pipeline stage.

  - `long outputTokens`

    Total output tokens generated across every pipeline stage.

### Beta Output Behavior

- `class BetaOutputBehavior: A class that can be one of several variants.union`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `class BetaOutputBehaviorCreateNew:`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `Type type`

      - `CREATE_NEW("create_new")`

  - `class BetaOutputBehaviorUpdateExisting:`

    The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

    - `String memoryStoreId`

    - `Type type`

      - `UPDATE_EXISTING("update_existing")`

### Beta Output Behavior Create New

- `class BetaOutputBehaviorCreateNew:`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `Type type`

    - `CREATE_NEW("create_new")`

### Beta Output Behavior Update Existing

- `class BetaOutputBehaviorUpdateExisting:`

  The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

  - `String memoryStoreId`

  - `Type type`

    - `UPDATE_EXISTING("update_existing")`

# Tunnels

## Create Tunnel

`BetaTunnel beta().tunnels().create(TunnelCreateParamsparams = TunnelCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Creates a tunnel. Creation allocates a fresh hostname and provisions the tunnel; it is not idempotent. The new tunnel rejects MCP traffic until at least one CA certificate is added.

### Parameters

- `TunnelCreateParams params`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `Optional<String> displayName`

    Optional human-readable name for the tunnel (1-255 characters).

### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `String id`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> displayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `String domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonValue; type "tunnel"constant`

    - `TUNNEL("tunnel")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.tunnels.BetaTunnel;
import com.anthropic.models.beta.tunnels.TunnelCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaTunnel betaTunnel = client.beta().tunnels().create();
    }
}
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "display_name": "display_name",
  "domain": "domain",
  "type": "tunnel"
}
```

## Get Tunnel

`BetaTunnel beta().tunnels().retrieve(TunnelRetrieveParamsparams = TunnelRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/tunnels/{tunnel_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel by ID.

### Parameters

- `TunnelRetrieveParams params`

  - `Optional<String> tunnelId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `String id`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> displayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `String domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonValue; type "tunnel"constant`

    - `TUNNEL("tunnel")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.tunnels.BetaTunnel;
import com.anthropic.models.beta.tunnels.TunnelRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaTunnel betaTunnel = client.beta().tunnels().retrieve("tunnel_id");
    }
}
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "display_name": "display_name",
  "domain": "domain",
  "type": "tunnel"
}
```

## List Tunnels

`TunnelListPage beta().tunnels().list(TunnelListParamsparams = TunnelListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists tunnels. Results are ordered by creation time, newest first; archived tunnels are excluded unless include_archived is set.

### Parameters

- `TunnelListParams params`

  - `Optional<Boolean> includeArchived`

    Whether to include archived tunnels in the results. Defaults to false.

  - `Optional<Long> limit`

    Maximum number of tunnels to return per page. Defaults to 20, maximum 1000.

  - `Optional<String> page`

    Opaque pagination cursor from a previous `list_tunnels` response.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `String id`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> displayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `String domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonValue; type "tunnel"constant`

    - `TUNNEL("tunnel")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.tunnels.TunnelListPage;
import com.anthropic.models.beta.tunnels.TunnelListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        TunnelListPage page = client.beta().tunnels().list();
    }
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "display_name": "display_name",
      "domain": "domain",
      "type": "tunnel"
    }
  ],
  "next_page": "next_page"
}
```

## Archive Tunnel

`BetaTunnel beta().tunnels().archive(TunnelArchiveParamsparams = TunnelArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/tunnels/{tunnel_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel. Archival is irreversible: every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.

### Parameters

- `TunnelArchiveParams params`

  - `Optional<String> tunnelId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `String id`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> displayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `String domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonValue; type "tunnel"constant`

    - `TUNNEL("tunnel")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.tunnels.BetaTunnel;
import com.anthropic.models.beta.tunnels.TunnelArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaTunnel betaTunnel = client.beta().tunnels().archive("tunnel_id");
    }
}
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "display_name": "display_name",
  "domain": "domain",
  "type": "tunnel"
}
```

## Reveal Tunnel Token

`BetaTunnelToken beta().tunnels().revealToken(TunnelRevealTokenParamsparams = TunnelRevealTokenParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/tunnels/{tunnel_id}/reveal_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

### Parameters

- `TunnelRevealTokenParams params`

  - `Optional<String> tunnelId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaTunnelToken:`

  A tunnel's connector token.

  - `String id`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `String tunnelToken`

    The connector token used to run the tunnel. Treat as a credential.

  - `JsonValue; type "tunnel_token"constant`

    - `TUNNEL_TOKEN("tunnel_token")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.tunnels.BetaTunnelToken;
import com.anthropic.models.beta.tunnels.TunnelRevealTokenParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaTunnelToken betaTunnelToken = client.beta().tunnels().revealToken("tunnel_id");
    }
}
```

#### Response

```json
{
  "id": "id",
  "tunnel_token": "tunnel_token",
  "type": "tunnel_token"
}
```

## Rotate Tunnel Token

`BetaTunnelToken beta().tunnels().rotateToken(TunnelRotateTokenParamsparams = TunnelRotateTokenParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/tunnels/{tunnel_id}/rotate_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

### Parameters

- `TunnelRotateTokenParams params`

  - `Optional<String> tunnelId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `Optional<String> reason`

    Optional free-text reason for the rotation, recorded for audit.

### Returns

- `class BetaTunnelToken:`

  A tunnel's connector token.

  - `String id`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `String tunnelToken`

    The connector token used to run the tunnel. Treat as a credential.

  - `JsonValue; type "tunnel_token"constant`

    - `TUNNEL_TOKEN("tunnel_token")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.tunnels.BetaTunnelToken;
import com.anthropic.models.beta.tunnels.TunnelRotateTokenParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaTunnelToken betaTunnelToken = client.beta().tunnels().rotateToken("tunnel_id");
    }
}
```

#### Response

```json
{
  "id": "id",
  "tunnel_token": "tunnel_token",
  "type": "tunnel_token"
}
```

## Domain Types

### Beta Tunnel

- `class BetaTunnel:`

  An MCP tunnel.

  - `String id`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> displayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `String domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonValue; type "tunnel"constant`

    - `TUNNEL("tunnel")`

### Beta Tunnel Token

- `class BetaTunnelToken:`

  A tunnel's connector token.

  - `String id`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `String tunnelToken`

    The connector token used to run the tunnel. Treat as a credential.

  - `JsonValue; type "tunnel_token"constant`

    - `TUNNEL_TOKEN("tunnel_token")`

# Certificates

## Create Tunnel Certificate

`BetaTunnelCertificate beta().tunnels().certificates().create(CertificateCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

### Parameters

- `CertificateCreateParams params`

  - `Optional<String> tunnelId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `String caCertificatePem`

    PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material. Maximum 8KB.

### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `String id`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> expiresAt`

    A timestamp in RFC 3339 format

  - `String fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `String tunnelId`

    ID of the tunnel the certificate is registered against.

  - `JsonValue; type "tunnel_certificate"constant`

    - `TUNNEL_CERTIFICATE("tunnel_certificate")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.tunnels.certificates.BetaTunnelCertificate;
import com.anthropic.models.beta.tunnels.certificates.CertificateCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CertificateCreateParams params = CertificateCreateParams.builder()
            .tunnelId("tunnel_id")
            .caCertificatePem("ca_certificate_pem")
            .build();
        BetaTunnelCertificate betaTunnelCertificate = client.beta().tunnels().certificates().create(params);
    }
}
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```

## Get Tunnel Certificate

`BetaTunnelCertificate beta().tunnels().certificates().retrieve(CertificateRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

### Parameters

- `CertificateRetrieveParams params`

  - `String tunnelId`

  - `Optional<String> certificateId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `String id`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> expiresAt`

    A timestamp in RFC 3339 format

  - `String fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `String tunnelId`

    ID of the tunnel the certificate is registered against.

  - `JsonValue; type "tunnel_certificate"constant`

    - `TUNNEL_CERTIFICATE("tunnel_certificate")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.tunnels.certificates.BetaTunnelCertificate;
import com.anthropic.models.beta.tunnels.certificates.CertificateRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CertificateRetrieveParams params = CertificateRetrieveParams.builder()
            .tunnelId("tunnel_id")
            .certificateId("certificate_id")
            .build();
        BetaTunnelCertificate betaTunnelCertificate = client.beta().tunnels().certificates().retrieve(params);
    }
}
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```

## List Tunnel Certificates

`CertificateListPage beta().tunnels().certificates().list(CertificateListParamsparams = CertificateListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

### Parameters

- `CertificateListParams params`

  - `Optional<String> tunnelId`

  - `Optional<Boolean> includeArchived`

    Whether to include archived certificates in the results. Defaults to false.

  - `Optional<Long> limit`

    Maximum number of certificates to return per page. Defaults to 20, maximum 1000.

  - `Optional<String> page`

    Opaque pagination cursor from a previous `list_tunnel_certificates` response.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `String id`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> expiresAt`

    A timestamp in RFC 3339 format

  - `String fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `String tunnelId`

    ID of the tunnel the certificate is registered against.

  - `JsonValue; type "tunnel_certificate"constant`

    - `TUNNEL_CERTIFICATE("tunnel_certificate")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.tunnels.certificates.CertificateListPage;
import com.anthropic.models.beta.tunnels.certificates.CertificateListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CertificateListPage page = client.beta().tunnels().certificates().list("tunnel_id");
    }
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "expires_at": "2019-12-27T18:11:19.117Z",
      "fingerprint": "fingerprint",
      "tunnel_id": "tunnel_id",
      "type": "tunnel_certificate"
    }
  ],
  "next_page": "next_page"
}
```

## Archive Tunnel Certificate

`BetaTunnelCertificate beta().tunnels().certificates().archive(CertificateArchiveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

### Parameters

- `CertificateArchiveParams params`

  - `String tunnelId`

  - `Optional<String> certificateId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `String id`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> expiresAt`

    A timestamp in RFC 3339 format

  - `String fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `String tunnelId`

    ID of the tunnel the certificate is registered against.

  - `JsonValue; type "tunnel_certificate"constant`

    - `TUNNEL_CERTIFICATE("tunnel_certificate")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.tunnels.certificates.BetaTunnelCertificate;
import com.anthropic.models.beta.tunnels.certificates.CertificateArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CertificateArchiveParams params = CertificateArchiveParams.builder()
            .tunnelId("tunnel_id")
            .certificateId("certificate_id")
            .build();
        BetaTunnelCertificate betaTunnelCertificate = client.beta().tunnels().certificates().archive(params);
    }
}
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```

## Domain Types

### Beta Tunnel Certificate

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `String id`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> expiresAt`

    A timestamp in RFC 3339 format

  - `String fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `String tunnelId`

    ID of the tunnel the certificate is registered against.

  - `JsonValue; type "tunnel_certificate"constant`

    - `TUNNEL_CERTIFICATE("tunnel_certificate")`

# Webhooks

## Domain Types

### Beta Webhook Agent Archived Event Data

- `class BetaWebhookAgentArchivedEventData:`

  - `String id`

    ID of the agent that triggered the event.

  - `String organizationId`

  - `JsonValue; type "agent.archived"constant`

    - `AGENT_ARCHIVED("agent.archived")`

  - `String workspaceId`

### Beta Webhook Agent Created Event Data

- `class BetaWebhookAgentCreatedEventData:`

  - `String id`

    ID of the agent that triggered the event.

  - `String organizationId`

  - `JsonValue; type "agent.created"constant`

    - `AGENT_CREATED("agent.created")`

  - `String workspaceId`

### Beta Webhook Agent Deleted Event Data

- `class BetaWebhookAgentDeletedEventData:`

  - `String id`

    ID of the agent that triggered the event.

  - `String organizationId`

  - `JsonValue; type "agent.deleted"constant`

    - `AGENT_DELETED("agent.deleted")`

  - `String workspaceId`

### Beta Webhook Agent Updated Event Data

- `class BetaWebhookAgentUpdatedEventData:`

  - `String id`

    ID of the agent that triggered the event.

  - `String organizationId`

  - `JsonValue; type "agent.updated"constant`

    - `AGENT_UPDATED("agent.updated")`

  - `String workspaceId`

### Beta Webhook Deployment Archived Event Data

- `class BetaWebhookDeploymentArchivedEventData:`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `JsonValue; type "deployment.archived"constant`

    - `DEPLOYMENT_ARCHIVED("deployment.archived")`

  - `String workspaceId`

### Beta Webhook Deployment Created Event Data

- `class BetaWebhookDeploymentCreatedEventData:`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `JsonValue; type "deployment.created"constant`

    - `DEPLOYMENT_CREATED("deployment.created")`

  - `String workspaceId`

### Beta Webhook Deployment Deleted Event Data

- `class BetaWebhookDeploymentDeletedEventData:`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `JsonValue; type "deployment.deleted"constant`

    - `DEPLOYMENT_DELETED("deployment.deleted")`

  - `String workspaceId`

### Beta Webhook Deployment Paused Event Data

- `class BetaWebhookDeploymentPausedEventData:`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `JsonValue; type "deployment.paused"constant`

    - `DEPLOYMENT_PAUSED("deployment.paused")`

  - `String workspaceId`

### Beta Webhook Deployment Run Failed Event Data

- `class BetaWebhookDeploymentRunFailedEventData:`

  - `String id`

    ID of the deployment run that triggered the event.

  - `String organizationId`

  - `JsonValue; type "deployment_run.failed"constant`

    - `DEPLOYMENT_RUN_FAILED("deployment_run.failed")`

  - `String workspaceId`

### Beta Webhook Deployment Run Started Event Data

- `class BetaWebhookDeploymentRunStartedEventData:`

  - `String id`

    ID of the deployment run that triggered the event.

  - `String organizationId`

  - `JsonValue; type "deployment_run.started"constant`

    - `DEPLOYMENT_RUN_STARTED("deployment_run.started")`

  - `String workspaceId`

### Beta Webhook Deployment Run Succeeded Event Data

- `class BetaWebhookDeploymentRunSucceededEventData:`

  - `String id`

    ID of the deployment run that triggered the event.

  - `String organizationId`

  - `JsonValue; type "deployment_run.succeeded"constant`

    - `DEPLOYMENT_RUN_SUCCEEDED("deployment_run.succeeded")`

  - `String workspaceId`

### Beta Webhook Deployment Unpaused Event Data

- `class BetaWebhookDeploymentUnpausedEventData:`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `JsonValue; type "deployment.unpaused"constant`

    - `DEPLOYMENT_UNPAUSED("deployment.unpaused")`

  - `String workspaceId`

### Beta Webhook Deployment Updated Event Data

- `class BetaWebhookDeploymentUpdatedEventData:`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `JsonValue; type "deployment.updated"constant`

    - `DEPLOYMENT_UPDATED("deployment.updated")`

  - `String workspaceId`

### Beta Webhook Environment Archived Event Data

- `class BetaWebhookEnvironmentArchivedEventData:`

  - `String id`

    ID of the environment that triggered the event.

  - `String organizationId`

  - `JsonValue; type "environment.archived"constant`

    - `ENVIRONMENT_ARCHIVED("environment.archived")`

  - `String workspaceId`

### Beta Webhook Environment Created Event Data

- `class BetaWebhookEnvironmentCreatedEventData:`

  - `String id`

    ID of the environment that triggered the event.

  - `String organizationId`

  - `JsonValue; type "environment.created"constant`

    - `ENVIRONMENT_CREATED("environment.created")`

  - `String workspaceId`

### Beta Webhook Environment Deleted Event Data

- `class BetaWebhookEnvironmentDeletedEventData:`

  - `String id`

    ID of the environment that triggered the event.

  - `String organizationId`

  - `JsonValue; type "environment.deleted"constant`

    - `ENVIRONMENT_DELETED("environment.deleted")`

  - `String workspaceId`

### Beta Webhook Environment Updated Event Data

- `class BetaWebhookEnvironmentUpdatedEventData:`

  - `String id`

    ID of the environment that triggered the event.

  - `String organizationId`

  - `JsonValue; type "environment.updated"constant`

    - `ENVIRONMENT_UPDATED("environment.updated")`

  - `String workspaceId`

### Beta Webhook Event

- `class BetaWebhookEvent:`

  - `String id`

    Unique event identifier for idempotency.

  - `LocalDateTime createdAt`

    RFC 3339 timestamp when the event occurred.

  - `BetaWebhookEventData data`

    - `class BetaWebhookSessionCreatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.created"constant`

        - `SESSION_CREATED("session.created")`

      - `String workspaceId`

    - `class BetaWebhookSessionPendingEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.pending"constant`

        - `SESSION_PENDING("session.pending")`

      - `String workspaceId`

    - `class BetaWebhookSessionRunningEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.running"constant`

        - `SESSION_RUNNING("session.running")`

      - `String workspaceId`

    - `class BetaWebhookSessionIdledEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.idled"constant`

        - `SESSION_IDLED("session.idled")`

      - `String workspaceId`

    - `class BetaWebhookSessionRequiresActionEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.requires_action"constant`

        - `SESSION_REQUIRES_ACTION("session.requires_action")`

      - `String workspaceId`

    - `class BetaWebhookSessionArchivedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.archived"constant`

        - `SESSION_ARCHIVED("session.archived")`

      - `String workspaceId`

    - `class BetaWebhookSessionDeletedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.deleted"constant`

        - `SESSION_DELETED("session.deleted")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusRescheduledEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_rescheduled"constant`

        - `SESSION_STATUS_RESCHEDULED("session.status_rescheduled")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusRunStartedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_run_started"constant`

        - `SESSION_STATUS_RUN_STARTED("session.status_run_started")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusIdledEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_idled"constant`

        - `SESSION_STATUS_IDLED("session.status_idled")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusTerminatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_terminated"constant`

        - `SESSION_STATUS_TERMINATED("session.status_terminated")`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadCreatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String sessionThreadId`

        ID of the session thread this event refers to.

      - `JsonValue; type "session.thread_created"constant`

        - `SESSION_THREAD_CREATED("session.thread_created")`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadIdledEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String sessionThreadId`

        ID of the session thread this event refers to.

      - `JsonValue; type "session.thread_idled"constant`

        - `SESSION_THREAD_IDLED("session.thread_idled")`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadTerminatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String sessionThreadId`

        ID of the session thread this event refers to.

      - `JsonValue; type "session.thread_terminated"constant`

        - `SESSION_THREAD_TERMINATED("session.thread_terminated")`

      - `String workspaceId`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.outcome_evaluation_ended"constant`

        - `SESSION_OUTCOME_EVALUATION_ENDED("session.outcome_evaluation_ended")`

      - `String workspaceId`

    - `class BetaWebhookVaultCreatedEventData:`

      - `String id`

        ID of the vault that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault.created"constant`

        - `VAULT_CREATED("vault.created")`

      - `String workspaceId`

    - `class BetaWebhookVaultArchivedEventData:`

      - `String id`

        ID of the vault that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault.archived"constant`

        - `VAULT_ARCHIVED("vault.archived")`

      - `String workspaceId`

    - `class BetaWebhookVaultDeletedEventData:`

      - `String id`

        ID of the vault that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault.deleted"constant`

        - `VAULT_DELETED("vault.deleted")`

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialCreatedEventData:`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.created"constant`

        - `VAULT_CREDENTIAL_CREATED("vault_credential.created")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialArchivedEventData:`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.archived"constant`

        - `VAULT_CREDENTIAL_ARCHIVED("vault_credential.archived")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialDeletedEventData:`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.deleted"constant`

        - `VAULT_CREDENTIAL_DELETED("vault_credential.deleted")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.refresh_failed"constant`

        - `VAULT_CREDENTIAL_REFRESH_FAILED("vault_credential.refresh_failed")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookSessionUpdatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.updated"constant`

        - `SESSION_UPDATED("session.updated")`

      - `String workspaceId`

    - `class BetaWebhookAgentCreatedEventData:`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `JsonValue; type "agent.created"constant`

        - `AGENT_CREATED("agent.created")`

      - `String workspaceId`

    - `class BetaWebhookAgentArchivedEventData:`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `JsonValue; type "agent.archived"constant`

        - `AGENT_ARCHIVED("agent.archived")`

      - `String workspaceId`

    - `class BetaWebhookAgentDeletedEventData:`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `JsonValue; type "agent.deleted"constant`

        - `AGENT_DELETED("agent.deleted")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentPausedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.paused"constant`

        - `DEPLOYMENT_PAUSED("deployment.paused")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentRunFailedEventData:`

      - `String id`

        ID of the deployment run that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment_run.failed"constant`

        - `DEPLOYMENT_RUN_FAILED("deployment_run.failed")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentCreatedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.created"constant`

        - `DEPLOYMENT_CREATED("deployment.created")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentUpdatedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.updated"constant`

        - `DEPLOYMENT_UPDATED("deployment.updated")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentUnpausedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.unpaused"constant`

        - `DEPLOYMENT_UNPAUSED("deployment.unpaused")`

      - `String workspaceId`

    - `class BetaWebhookAgentUpdatedEventData:`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `JsonValue; type "agent.updated"constant`

        - `AGENT_UPDATED("agent.updated")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentArchivedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.archived"constant`

        - `DEPLOYMENT_ARCHIVED("deployment.archived")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentRunStartedEventData:`

      - `String id`

        ID of the deployment run that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment_run.started"constant`

        - `DEPLOYMENT_RUN_STARTED("deployment_run.started")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentDeletedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.deleted"constant`

        - `DEPLOYMENT_DELETED("deployment.deleted")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentRunSucceededEventData:`

      - `String id`

        ID of the deployment run that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment_run.succeeded"constant`

        - `DEPLOYMENT_RUN_SUCCEEDED("deployment_run.succeeded")`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentCreatedEventData:`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "environment.created"constant`

        - `ENVIRONMENT_CREATED("environment.created")`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentUpdatedEventData:`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "environment.updated"constant`

        - `ENVIRONMENT_UPDATED("environment.updated")`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentArchivedEventData:`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "environment.archived"constant`

        - `ENVIRONMENT_ARCHIVED("environment.archived")`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentDeletedEventData:`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "environment.deleted"constant`

        - `ENVIRONMENT_DELETED("environment.deleted")`

      - `String workspaceId`

    - `class BetaWebhookMemoryStoreCreatedEventData:`

      - `String id`

        ID of the memory store that triggered the event.

      - `String organizationId`

      - `JsonValue; type "memory_store.created"constant`

        - `MEMORY_STORE_CREATED("memory_store.created")`

      - `String workspaceId`

    - `class BetaWebhookMemoryStoreArchivedEventData:`

      - `String id`

        ID of the memory store that triggered the event.

      - `String organizationId`

      - `JsonValue; type "memory_store.archived"constant`

        - `MEMORY_STORE_ARCHIVED("memory_store.archived")`

      - `String workspaceId`

    - `class BetaWebhookMemoryStoreDeletedEventData:`

      - `String id`

        ID of the memory store that triggered the event.

      - `String organizationId`

      - `JsonValue; type "memory_store.deleted"constant`

        - `MEMORY_STORE_DELETED("memory_store.deleted")`

      - `String workspaceId`

    - `class BetaWebhookSessionBudgetReachedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.budget_reached"constant`

        - `SESSION_BUDGET_REACHED("session.budget_reached")`

      - `String workspaceId`

  - `JsonValue; type "event"constant`

    Object type. Always `event` for webhook payloads.

    - `EVENT("event")`

### Beta Webhook Event Data

- `class BetaWebhookEventData: A class that can be one of several variants.union`

  - `class BetaWebhookSessionCreatedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.created"constant`

      - `SESSION_CREATED("session.created")`

    - `String workspaceId`

  - `class BetaWebhookSessionPendingEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.pending"constant`

      - `SESSION_PENDING("session.pending")`

    - `String workspaceId`

  - `class BetaWebhookSessionRunningEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.running"constant`

      - `SESSION_RUNNING("session.running")`

    - `String workspaceId`

  - `class BetaWebhookSessionIdledEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.idled"constant`

      - `SESSION_IDLED("session.idled")`

    - `String workspaceId`

  - `class BetaWebhookSessionRequiresActionEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.requires_action"constant`

      - `SESSION_REQUIRES_ACTION("session.requires_action")`

    - `String workspaceId`

  - `class BetaWebhookSessionArchivedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.archived"constant`

      - `SESSION_ARCHIVED("session.archived")`

    - `String workspaceId`

  - `class BetaWebhookSessionDeletedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.deleted"constant`

      - `SESSION_DELETED("session.deleted")`

    - `String workspaceId`

  - `class BetaWebhookSessionStatusRescheduledEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.status_rescheduled"constant`

      - `SESSION_STATUS_RESCHEDULED("session.status_rescheduled")`

    - `String workspaceId`

  - `class BetaWebhookSessionStatusRunStartedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.status_run_started"constant`

      - `SESSION_STATUS_RUN_STARTED("session.status_run_started")`

    - `String workspaceId`

  - `class BetaWebhookSessionStatusIdledEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.status_idled"constant`

      - `SESSION_STATUS_IDLED("session.status_idled")`

    - `String workspaceId`

  - `class BetaWebhookSessionStatusTerminatedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.status_terminated"constant`

      - `SESSION_STATUS_TERMINATED("session.status_terminated")`

    - `String workspaceId`

  - `class BetaWebhookSessionThreadCreatedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String sessionThreadId`

      ID of the session thread this event refers to.

    - `JsonValue; type "session.thread_created"constant`

      - `SESSION_THREAD_CREATED("session.thread_created")`

    - `String workspaceId`

  - `class BetaWebhookSessionThreadIdledEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String sessionThreadId`

      ID of the session thread this event refers to.

    - `JsonValue; type "session.thread_idled"constant`

      - `SESSION_THREAD_IDLED("session.thread_idled")`

    - `String workspaceId`

  - `class BetaWebhookSessionThreadTerminatedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String sessionThreadId`

      ID of the session thread this event refers to.

    - `JsonValue; type "session.thread_terminated"constant`

      - `SESSION_THREAD_TERMINATED("session.thread_terminated")`

    - `String workspaceId`

  - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.outcome_evaluation_ended"constant`

      - `SESSION_OUTCOME_EVALUATION_ENDED("session.outcome_evaluation_ended")`

    - `String workspaceId`

  - `class BetaWebhookVaultCreatedEventData:`

    - `String id`

      ID of the vault that triggered the event.

    - `String organizationId`

    - `JsonValue; type "vault.created"constant`

      - `VAULT_CREATED("vault.created")`

    - `String workspaceId`

  - `class BetaWebhookVaultArchivedEventData:`

    - `String id`

      ID of the vault that triggered the event.

    - `String organizationId`

    - `JsonValue; type "vault.archived"constant`

      - `VAULT_ARCHIVED("vault.archived")`

    - `String workspaceId`

  - `class BetaWebhookVaultDeletedEventData:`

    - `String id`

      ID of the vault that triggered the event.

    - `String organizationId`

    - `JsonValue; type "vault.deleted"constant`

      - `VAULT_DELETED("vault.deleted")`

    - `String workspaceId`

  - `class BetaWebhookVaultCredentialCreatedEventData:`

    - `String id`

      ID of the vault credential that triggered the event.

    - `String organizationId`

    - `JsonValue; type "vault_credential.created"constant`

      - `VAULT_CREDENTIAL_CREATED("vault_credential.created")`

    - `String vaultId`

      ID of the vault that owns this credential.

    - `String workspaceId`

  - `class BetaWebhookVaultCredentialArchivedEventData:`

    - `String id`

      ID of the vault credential that triggered the event.

    - `String organizationId`

    - `JsonValue; type "vault_credential.archived"constant`

      - `VAULT_CREDENTIAL_ARCHIVED("vault_credential.archived")`

    - `String vaultId`

      ID of the vault that owns this credential.

    - `String workspaceId`

  - `class BetaWebhookVaultCredentialDeletedEventData:`

    - `String id`

      ID of the vault credential that triggered the event.

    - `String organizationId`

    - `JsonValue; type "vault_credential.deleted"constant`

      - `VAULT_CREDENTIAL_DELETED("vault_credential.deleted")`

    - `String vaultId`

      ID of the vault that owns this credential.

    - `String workspaceId`

  - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

    - `String id`

      ID of the vault credential that triggered the event.

    - `String organizationId`

    - `JsonValue; type "vault_credential.refresh_failed"constant`

      - `VAULT_CREDENTIAL_REFRESH_FAILED("vault_credential.refresh_failed")`

    - `String vaultId`

      ID of the vault that owns this credential.

    - `String workspaceId`

  - `class BetaWebhookSessionUpdatedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.updated"constant`

      - `SESSION_UPDATED("session.updated")`

    - `String workspaceId`

  - `class BetaWebhookAgentCreatedEventData:`

    - `String id`

      ID of the agent that triggered the event.

    - `String organizationId`

    - `JsonValue; type "agent.created"constant`

      - `AGENT_CREATED("agent.created")`

    - `String workspaceId`

  - `class BetaWebhookAgentArchivedEventData:`

    - `String id`

      ID of the agent that triggered the event.

    - `String organizationId`

    - `JsonValue; type "agent.archived"constant`

      - `AGENT_ARCHIVED("agent.archived")`

    - `String workspaceId`

  - `class BetaWebhookAgentDeletedEventData:`

    - `String id`

      ID of the agent that triggered the event.

    - `String organizationId`

    - `JsonValue; type "agent.deleted"constant`

      - `AGENT_DELETED("agent.deleted")`

    - `String workspaceId`

  - `class BetaWebhookDeploymentPausedEventData:`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `JsonValue; type "deployment.paused"constant`

      - `DEPLOYMENT_PAUSED("deployment.paused")`

    - `String workspaceId`

  - `class BetaWebhookDeploymentRunFailedEventData:`

    - `String id`

      ID of the deployment run that triggered the event.

    - `String organizationId`

    - `JsonValue; type "deployment_run.failed"constant`

      - `DEPLOYMENT_RUN_FAILED("deployment_run.failed")`

    - `String workspaceId`

  - `class BetaWebhookDeploymentCreatedEventData:`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `JsonValue; type "deployment.created"constant`

      - `DEPLOYMENT_CREATED("deployment.created")`

    - `String workspaceId`

  - `class BetaWebhookDeploymentUpdatedEventData:`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `JsonValue; type "deployment.updated"constant`

      - `DEPLOYMENT_UPDATED("deployment.updated")`

    - `String workspaceId`

  - `class BetaWebhookDeploymentUnpausedEventData:`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `JsonValue; type "deployment.unpaused"constant`

      - `DEPLOYMENT_UNPAUSED("deployment.unpaused")`

    - `String workspaceId`

  - `class BetaWebhookAgentUpdatedEventData:`

    - `String id`

      ID of the agent that triggered the event.

    - `String organizationId`

    - `JsonValue; type "agent.updated"constant`

      - `AGENT_UPDATED("agent.updated")`

    - `String workspaceId`

  - `class BetaWebhookDeploymentArchivedEventData:`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `JsonValue; type "deployment.archived"constant`

      - `DEPLOYMENT_ARCHIVED("deployment.archived")`

    - `String workspaceId`

  - `class BetaWebhookDeploymentRunStartedEventData:`

    - `String id`

      ID of the deployment run that triggered the event.

    - `String organizationId`

    - `JsonValue; type "deployment_run.started"constant`

      - `DEPLOYMENT_RUN_STARTED("deployment_run.started")`

    - `String workspaceId`

  - `class BetaWebhookDeploymentDeletedEventData:`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `JsonValue; type "deployment.deleted"constant`

      - `DEPLOYMENT_DELETED("deployment.deleted")`

    - `String workspaceId`

  - `class BetaWebhookDeploymentRunSucceededEventData:`

    - `String id`

      ID of the deployment run that triggered the event.

    - `String organizationId`

    - `JsonValue; type "deployment_run.succeeded"constant`

      - `DEPLOYMENT_RUN_SUCCEEDED("deployment_run.succeeded")`

    - `String workspaceId`

  - `class BetaWebhookEnvironmentCreatedEventData:`

    - `String id`

      ID of the environment that triggered the event.

    - `String organizationId`

    - `JsonValue; type "environment.created"constant`

      - `ENVIRONMENT_CREATED("environment.created")`

    - `String workspaceId`

  - `class BetaWebhookEnvironmentUpdatedEventData:`

    - `String id`

      ID of the environment that triggered the event.

    - `String organizationId`

    - `JsonValue; type "environment.updated"constant`

      - `ENVIRONMENT_UPDATED("environment.updated")`

    - `String workspaceId`

  - `class BetaWebhookEnvironmentArchivedEventData:`

    - `String id`

      ID of the environment that triggered the event.

    - `String organizationId`

    - `JsonValue; type "environment.archived"constant`

      - `ENVIRONMENT_ARCHIVED("environment.archived")`

    - `String workspaceId`

  - `class BetaWebhookEnvironmentDeletedEventData:`

    - `String id`

      ID of the environment that triggered the event.

    - `String organizationId`

    - `JsonValue; type "environment.deleted"constant`

      - `ENVIRONMENT_DELETED("environment.deleted")`

    - `String workspaceId`

  - `class BetaWebhookMemoryStoreCreatedEventData:`

    - `String id`

      ID of the memory store that triggered the event.

    - `String organizationId`

    - `JsonValue; type "memory_store.created"constant`

      - `MEMORY_STORE_CREATED("memory_store.created")`

    - `String workspaceId`

  - `class BetaWebhookMemoryStoreArchivedEventData:`

    - `String id`

      ID of the memory store that triggered the event.

    - `String organizationId`

    - `JsonValue; type "memory_store.archived"constant`

      - `MEMORY_STORE_ARCHIVED("memory_store.archived")`

    - `String workspaceId`

  - `class BetaWebhookMemoryStoreDeletedEventData:`

    - `String id`

      ID of the memory store that triggered the event.

    - `String organizationId`

    - `JsonValue; type "memory_store.deleted"constant`

      - `MEMORY_STORE_DELETED("memory_store.deleted")`

    - `String workspaceId`

  - `class BetaWebhookSessionBudgetReachedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.budget_reached"constant`

      - `SESSION_BUDGET_REACHED("session.budget_reached")`

    - `String workspaceId`

### Beta Webhook Memory Store Archived Event Data

- `class BetaWebhookMemoryStoreArchivedEventData:`

  - `String id`

    ID of the memory store that triggered the event.

  - `String organizationId`

  - `JsonValue; type "memory_store.archived"constant`

    - `MEMORY_STORE_ARCHIVED("memory_store.archived")`

  - `String workspaceId`

### Beta Webhook Memory Store Created Event Data

- `class BetaWebhookMemoryStoreCreatedEventData:`

  - `String id`

    ID of the memory store that triggered the event.

  - `String organizationId`

  - `JsonValue; type "memory_store.created"constant`

    - `MEMORY_STORE_CREATED("memory_store.created")`

  - `String workspaceId`

### Beta Webhook Memory Store Deleted Event Data

- `class BetaWebhookMemoryStoreDeletedEventData:`

  - `String id`

    ID of the memory store that triggered the event.

  - `String organizationId`

  - `JsonValue; type "memory_store.deleted"constant`

    - `MEMORY_STORE_DELETED("memory_store.deleted")`

  - `String workspaceId`

### Beta Webhook Session Archived Event Data

- `class BetaWebhookSessionArchivedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.archived"constant`

    - `SESSION_ARCHIVED("session.archived")`

  - `String workspaceId`

### Beta Webhook Session Budget Reached Event Data

- `class BetaWebhookSessionBudgetReachedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.budget_reached"constant`

    - `SESSION_BUDGET_REACHED("session.budget_reached")`

  - `String workspaceId`

### Beta Webhook Session Created Event Data

- `class BetaWebhookSessionCreatedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.created"constant`

    - `SESSION_CREATED("session.created")`

  - `String workspaceId`

### Beta Webhook Session Deleted Event Data

- `class BetaWebhookSessionDeletedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.deleted"constant`

    - `SESSION_DELETED("session.deleted")`

  - `String workspaceId`

### Beta Webhook Session Idled Event Data

- `class BetaWebhookSessionIdledEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.idled"constant`

    - `SESSION_IDLED("session.idled")`

  - `String workspaceId`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.outcome_evaluation_ended"constant`

    - `SESSION_OUTCOME_EVALUATION_ENDED("session.outcome_evaluation_ended")`

  - `String workspaceId`

### Beta Webhook Session Pending Event Data

- `class BetaWebhookSessionPendingEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.pending"constant`

    - `SESSION_PENDING("session.pending")`

  - `String workspaceId`

### Beta Webhook Session Requires Action Event Data

- `class BetaWebhookSessionRequiresActionEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.requires_action"constant`

    - `SESSION_REQUIRES_ACTION("session.requires_action")`

  - `String workspaceId`

### Beta Webhook Session Running Event Data

- `class BetaWebhookSessionRunningEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.running"constant`

    - `SESSION_RUNNING("session.running")`

  - `String workspaceId`

### Beta Webhook Session Status Idled Event Data

- `class BetaWebhookSessionStatusIdledEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.status_idled"constant`

    - `SESSION_STATUS_IDLED("session.status_idled")`

  - `String workspaceId`

### Beta Webhook Session Status Rescheduled Event Data

- `class BetaWebhookSessionStatusRescheduledEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.status_rescheduled"constant`

    - `SESSION_STATUS_RESCHEDULED("session.status_rescheduled")`

  - `String workspaceId`

### Beta Webhook Session Status Run Started Event Data

- `class BetaWebhookSessionStatusRunStartedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.status_run_started"constant`

    - `SESSION_STATUS_RUN_STARTED("session.status_run_started")`

  - `String workspaceId`

### Beta Webhook Session Status Terminated Event Data

- `class BetaWebhookSessionStatusTerminatedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.status_terminated"constant`

    - `SESSION_STATUS_TERMINATED("session.status_terminated")`

  - `String workspaceId`

### Beta Webhook Session Thread Created Event Data

- `class BetaWebhookSessionThreadCreatedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String sessionThreadId`

    ID of the session thread this event refers to.

  - `JsonValue; type "session.thread_created"constant`

    - `SESSION_THREAD_CREATED("session.thread_created")`

  - `String workspaceId`

### Beta Webhook Session Thread Idled Event Data

- `class BetaWebhookSessionThreadIdledEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String sessionThreadId`

    ID of the session thread this event refers to.

  - `JsonValue; type "session.thread_idled"constant`

    - `SESSION_THREAD_IDLED("session.thread_idled")`

  - `String workspaceId`

### Beta Webhook Session Thread Terminated Event Data

- `class BetaWebhookSessionThreadTerminatedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String sessionThreadId`

    ID of the session thread this event refers to.

  - `JsonValue; type "session.thread_terminated"constant`

    - `SESSION_THREAD_TERMINATED("session.thread_terminated")`

  - `String workspaceId`

### Beta Webhook Session Updated Event Data

- `class BetaWebhookSessionUpdatedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.updated"constant`

    - `SESSION_UPDATED("session.updated")`

  - `String workspaceId`

### Beta Webhook Vault Archived Event Data

- `class BetaWebhookVaultArchivedEventData:`

  - `String id`

    ID of the vault that triggered the event.

  - `String organizationId`

  - `JsonValue; type "vault.archived"constant`

    - `VAULT_ARCHIVED("vault.archived")`

  - `String workspaceId`

### Beta Webhook Vault Created Event Data

- `class BetaWebhookVaultCreatedEventData:`

  - `String id`

    ID of the vault that triggered the event.

  - `String organizationId`

  - `JsonValue; type "vault.created"constant`

    - `VAULT_CREATED("vault.created")`

  - `String workspaceId`

### Beta Webhook Vault Credential Archived Event Data

- `class BetaWebhookVaultCredentialArchivedEventData:`

  - `String id`

    ID of the vault credential that triggered the event.

  - `String organizationId`

  - `JsonValue; type "vault_credential.archived"constant`

    - `VAULT_CREDENTIAL_ARCHIVED("vault_credential.archived")`

  - `String vaultId`

    ID of the vault that owns this credential.

  - `String workspaceId`

### Beta Webhook Vault Credential Created Event Data

- `class BetaWebhookVaultCredentialCreatedEventData:`

  - `String id`

    ID of the vault credential that triggered the event.

  - `String organizationId`

  - `JsonValue; type "vault_credential.created"constant`

    - `VAULT_CREDENTIAL_CREATED("vault_credential.created")`

  - `String vaultId`

    ID of the vault that owns this credential.

  - `String workspaceId`

### Beta Webhook Vault Credential Deleted Event Data

- `class BetaWebhookVaultCredentialDeletedEventData:`

  - `String id`

    ID of the vault credential that triggered the event.

  - `String organizationId`

  - `JsonValue; type "vault_credential.deleted"constant`

    - `VAULT_CREDENTIAL_DELETED("vault_credential.deleted")`

  - `String vaultId`

    ID of the vault that owns this credential.

  - `String workspaceId`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `class BetaWebhookVaultCredentialRefreshFailedEventData:`

  - `String id`

    ID of the vault credential that triggered the event.

  - `String organizationId`

  - `JsonValue; type "vault_credential.refresh_failed"constant`

    - `VAULT_CREDENTIAL_REFRESH_FAILED("vault_credential.refresh_failed")`

  - `String vaultId`

    ID of the vault that owns this credential.

  - `String workspaceId`

### Beta Webhook Vault Deleted Event Data

- `class BetaWebhookVaultDeletedEventData:`

  - `String id`

    ID of the vault that triggered the event.

  - `String organizationId`

  - `JsonValue; type "vault.deleted"constant`

    - `VAULT_DELETED("vault.deleted")`

  - `String workspaceId`

### Unwrap Webhook Event

- `class UnwrapWebhookEvent:`

  - `String id`

    Unique event identifier for idempotency.

  - `LocalDateTime createdAt`

    RFC 3339 timestamp when the event occurred.

  - `BetaWebhookEventData data`

    - `class BetaWebhookSessionCreatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.created"constant`

        - `SESSION_CREATED("session.created")`

      - `String workspaceId`

    - `class BetaWebhookSessionPendingEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.pending"constant`

        - `SESSION_PENDING("session.pending")`

      - `String workspaceId`

    - `class BetaWebhookSessionRunningEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.running"constant`

        - `SESSION_RUNNING("session.running")`

      - `String workspaceId`

    - `class BetaWebhookSessionIdledEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.idled"constant`

        - `SESSION_IDLED("session.idled")`

      - `String workspaceId`

    - `class BetaWebhookSessionRequiresActionEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.requires_action"constant`

        - `SESSION_REQUIRES_ACTION("session.requires_action")`

      - `String workspaceId`

    - `class BetaWebhookSessionArchivedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.archived"constant`

        - `SESSION_ARCHIVED("session.archived")`

      - `String workspaceId`

    - `class BetaWebhookSessionDeletedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.deleted"constant`

        - `SESSION_DELETED("session.deleted")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusRescheduledEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_rescheduled"constant`

        - `SESSION_STATUS_RESCHEDULED("session.status_rescheduled")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusRunStartedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_run_started"constant`

        - `SESSION_STATUS_RUN_STARTED("session.status_run_started")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusIdledEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_idled"constant`

        - `SESSION_STATUS_IDLED("session.status_idled")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusTerminatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_terminated"constant`

        - `SESSION_STATUS_TERMINATED("session.status_terminated")`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadCreatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String sessionThreadId`

        ID of the session thread this event refers to.

      - `JsonValue; type "session.thread_created"constant`

        - `SESSION_THREAD_CREATED("session.thread_created")`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadIdledEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String sessionThreadId`

        ID of the session thread this event refers to.

      - `JsonValue; type "session.thread_idled"constant`

        - `SESSION_THREAD_IDLED("session.thread_idled")`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadTerminatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String sessionThreadId`

        ID of the session thread this event refers to.

      - `JsonValue; type "session.thread_terminated"constant`

        - `SESSION_THREAD_TERMINATED("session.thread_terminated")`

      - `String workspaceId`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.outcome_evaluation_ended"constant`

        - `SESSION_OUTCOME_EVALUATION_ENDED("session.outcome_evaluation_ended")`

      - `String workspaceId`

    - `class BetaWebhookVaultCreatedEventData:`

      - `String id`

        ID of the vault that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault.created"constant`

        - `VAULT_CREATED("vault.created")`

      - `String workspaceId`

    - `class BetaWebhookVaultArchivedEventData:`

      - `String id`

        ID of the vault that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault.archived"constant`

        - `VAULT_ARCHIVED("vault.archived")`

      - `String workspaceId`

    - `class BetaWebhookVaultDeletedEventData:`

      - `String id`

        ID of the vault that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault.deleted"constant`

        - `VAULT_DELETED("vault.deleted")`

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialCreatedEventData:`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.created"constant`

        - `VAULT_CREDENTIAL_CREATED("vault_credential.created")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialArchivedEventData:`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.archived"constant`

        - `VAULT_CREDENTIAL_ARCHIVED("vault_credential.archived")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialDeletedEventData:`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.deleted"constant`

        - `VAULT_CREDENTIAL_DELETED("vault_credential.deleted")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.refresh_failed"constant`

        - `VAULT_CREDENTIAL_REFRESH_FAILED("vault_credential.refresh_failed")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookSessionUpdatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.updated"constant`

        - `SESSION_UPDATED("session.updated")`

      - `String workspaceId`

    - `class BetaWebhookAgentCreatedEventData:`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `JsonValue; type "agent.created"constant`

        - `AGENT_CREATED("agent.created")`

      - `String workspaceId`

    - `class BetaWebhookAgentArchivedEventData:`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `JsonValue; type "agent.archived"constant`

        - `AGENT_ARCHIVED("agent.archived")`

      - `String workspaceId`

    - `class BetaWebhookAgentDeletedEventData:`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `JsonValue; type "agent.deleted"constant`

        - `AGENT_DELETED("agent.deleted")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentPausedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.paused"constant`

        - `DEPLOYMENT_PAUSED("deployment.paused")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentRunFailedEventData:`

      - `String id`

        ID of the deployment run that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment_run.failed"constant`

        - `DEPLOYMENT_RUN_FAILED("deployment_run.failed")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentCreatedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.created"constant`

        - `DEPLOYMENT_CREATED("deployment.created")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentUpdatedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.updated"constant`

        - `DEPLOYMENT_UPDATED("deployment.updated")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentUnpausedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.unpaused"constant`

        - `DEPLOYMENT_UNPAUSED("deployment.unpaused")`

      - `String workspaceId`

    - `class BetaWebhookAgentUpdatedEventData:`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `JsonValue; type "agent.updated"constant`

        - `AGENT_UPDATED("agent.updated")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentArchivedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.archived"constant`

        - `DEPLOYMENT_ARCHIVED("deployment.archived")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentRunStartedEventData:`

      - `String id`

        ID of the deployment run that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment_run.started"constant`

        - `DEPLOYMENT_RUN_STARTED("deployment_run.started")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentDeletedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment.deleted"constant`

        - `DEPLOYMENT_DELETED("deployment.deleted")`

      - `String workspaceId`

    - `class BetaWebhookDeploymentRunSucceededEventData:`

      - `String id`

        ID of the deployment run that triggered the event.

      - `String organizationId`

      - `JsonValue; type "deployment_run.succeeded"constant`

        - `DEPLOYMENT_RUN_SUCCEEDED("deployment_run.succeeded")`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentCreatedEventData:`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "environment.created"constant`

        - `ENVIRONMENT_CREATED("environment.created")`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentUpdatedEventData:`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "environment.updated"constant`

        - `ENVIRONMENT_UPDATED("environment.updated")`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentArchivedEventData:`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "environment.archived"constant`

        - `ENVIRONMENT_ARCHIVED("environment.archived")`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentDeletedEventData:`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `JsonValue; type "environment.deleted"constant`

        - `ENVIRONMENT_DELETED("environment.deleted")`

      - `String workspaceId`

    - `class BetaWebhookMemoryStoreCreatedEventData:`

      - `String id`

        ID of the memory store that triggered the event.

      - `String organizationId`

      - `JsonValue; type "memory_store.created"constant`

        - `MEMORY_STORE_CREATED("memory_store.created")`

      - `String workspaceId`

    - `class BetaWebhookMemoryStoreArchivedEventData:`

      - `String id`

        ID of the memory store that triggered the event.

      - `String organizationId`

      - `JsonValue; type "memory_store.archived"constant`

        - `MEMORY_STORE_ARCHIVED("memory_store.archived")`

      - `String workspaceId`

    - `class BetaWebhookMemoryStoreDeletedEventData:`

      - `String id`

        ID of the memory store that triggered the event.

      - `String organizationId`

      - `JsonValue; type "memory_store.deleted"constant`

        - `MEMORY_STORE_DELETED("memory_store.deleted")`

      - `String workspaceId`

    - `class BetaWebhookSessionBudgetReachedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.budget_reached"constant`

        - `SESSION_BUDGET_REACHED("session.budget_reached")`

      - `String workspaceId`

  - `JsonValue; type "event"constant`

    Object type. Always `event` for webhook payloads.

    - `EVENT("event")`
