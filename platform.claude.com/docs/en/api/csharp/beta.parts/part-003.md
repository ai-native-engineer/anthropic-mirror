<!-- source: https://platform.claude.com/docs/en/api/csharp/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/csharp/beta -->

<!-- chunk-start -->
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "type": "session_resource_deleted"
}
```

## Domain Types

### Beta Managed Agents Delete Session Resource

- `class BetaManagedAgentsDeleteSessionResource:`

  Confirmation of resource deletion.

  - `required string ID`

  - `required Type Type`

    - `"session_resource_deleted"SessionResourceDeleted`

### Beta Managed Agents File Resource

- `class BetaManagedAgentsFileResource:`

  - `required string ID`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string FileID`

  - `required string MountPath`

  - `required Type Type`

    - `"file"File`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents GitHub Repository Resource

- `class BetaManagedAgentsGitHubRepositoryResource:`

  - `required string ID`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string MountPath`

  - `required Type Type`

    - `"github_repository"GitHubRepository`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required string Url`

  - `Checkout? Checkout`

    - `class BetaManagedAgentsBranchCheckout:`

      - `required string Name`

        Branch name to check out.

      - `required Type Type`

        - `"branch"Branch`

    - `class BetaManagedAgentsCommitCheckout:`

      - `required string Sha`

        Full commit SHA to check out.

      - `required Type Type`

        - `"commit"Commit`

### Beta Managed Agents Memory Store Resource

- `class BetaManagedAgentsMemoryStoreResource:`

  A memory store attached to an agent session.

  - `required string MemoryStoreID`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `required Type Type`

    - `"memory_store"MemoryStore`

  - `Access? Access`

    Access mode for an attached memory store.

    - `"read_write"ReadWrite`

    - `"read_only"ReadOnly`

  - `string Description`

    Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

  - `string? Instructions`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `string? MountPath`

    Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

  - `string? Name`

    Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Beta Managed Agents Session Resource

- `class BetaManagedAgentsSessionResource: A class that can be one of several variants.union`

  A memory store attached to an agent session.

  - `class BetaManagedAgentsGitHubRepositoryResource:`

    - `required string ID`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required string MountPath`

    - `required Type Type`

      - `"github_repository"GitHubRepository`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

    - `required string Url`

    - `Checkout? Checkout`

      - `class BetaManagedAgentsBranchCheckout:`

        - `required string Name`

          Branch name to check out.

        - `required Type Type`

          - `"branch"Branch`

      - `class BetaManagedAgentsCommitCheckout:`

        - `required string Sha`

          Full commit SHA to check out.

        - `required Type Type`

          - `"commit"Commit`

  - `class BetaManagedAgentsFileResource:`

    - `required string ID`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required string FileID`

    - `required string MountPath`

    - `required Type Type`

      - `"file"File`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsMemoryStoreResource:`

    A memory store attached to an agent session.

    - `required string MemoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `required Type Type`

      - `"memory_store"MemoryStore`

    - `Access? Access`

      Access mode for an attached memory store.

      - `"read_write"ReadWrite`

      - `"read_only"ReadOnly`

    - `string Description`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `string? Instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `string? MountPath`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `string? Name`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

# Threads

## List Session Threads

`ThreadListPageResponse Beta.Sessions.Threads.List(ThreadListParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/sessions/{session_id}/threads`

List Session Threads

### Parameters

- `ThreadListParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `Int limit`

    Query param: Maximum results per page. Defaults to 1000.

  - `string page`

    Query param: Opaque pagination cursor from a previous response's next_page. Forward-only.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class ThreadListPageResponse:`

  Paginated list of threads within a `session`.

  - `IReadOnlyList<BetaManagedAgentsSessionThread> Data`

    Threads in the session, primary first then children in spawn order.

    - `required string ID`

      Unique identifier for this thread.

    - `required Agent Agent`

      A session-resolved multiagent roster entry.

      - `class BetaManagedAgentsSessionThreadAgent:`

        Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

        - `required string ID`

        - `required string? Description`

        - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

          - `required string Name`

          - `required Type Type`

            - `"url"Url`

          - `required string Url`

        - `required BetaManagedAgentsModelConfig Model`

          Model identifier and configuration.

          - `required BetaManagedAgentsModel ID`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `"claude-sonnet-5"ClaudeSonnet5`

              High-performance model for coding and agents

            - `"claude-fable-5"ClaudeFable5`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-opus-5"ClaudeOpus5`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-8"ClaudeOpus4_8`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-7"ClaudeOpus4_7`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-6"ClaudeOpus4_6`

              Powerful intelligence for long-running agents and coding

            - `"claude-sonnet-4-6"ClaudeSonnet4_6`

              Best combination of speed and intelligence

            - `"claude-haiku-4-5"ClaudeHaiku4_5`

              Fastest model with near-frontier intelligence

            - `"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001`

              Fastest model with near-frontier intelligence

            - `"claude-opus-4-5"ClaudeOpus4_5`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101`

              Powerful intelligence for long-running agents and coding

            - `"claude-sonnet-4-5"ClaudeSonnet4_5`

              High-performance model for agents and coding

            - `"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929`

              High-performance model for agents and coding

          - `Effort Effort`

            How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

            - `class BetaManagedAgentsEffortLow:`

              Low effort. Favors latency over reasoning depth.

              - `required Type Type`

                - `"low"Low`

            - `class BetaManagedAgentsEffortMedium:`

              Medium effort. Balances latency and reasoning depth.

              - `required Type Type`

                - `"medium"Medium`

            - `class BetaManagedAgentsEffortHigh:`

              High effort. Favors reasoning depth.

              - `required Type Type`

                - `"high"High`

            - `class BetaManagedAgentsEffortXhigh:`

              Extra-high effort. Not all models accept this level.

              - `required Type Type`

                - `"xhigh"Xhigh`

            - `class BetaManagedAgentsEffortMax:`

              Maximum effort. Favors reasoning depth over latency.

              - `required Type Type`

                - `"max"Max`

          - `string InferenceGeo`

            Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

          - `Speed Speed`

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `"standard"Standard`

            - `"fast"Fast`

        - `required string Name`

        - `required IReadOnlyList<Skill> Skills`

          - `class BetaManagedAgentsAnthropicSkill:`

            A resolved Anthropic-managed skill.

            - `required string SkillID`

            - `required Type Type`

              - `"anthropic"Anthropic`

            - `required string Version`

          - `class BetaManagedAgentsCustomSkill:`

            A resolved user-created custom skill.

            - `required string SkillID`

            - `required Type Type`

              - `"custom"Custom`

            - `required string Version`

        - `required string? System`

        - `required IReadOnlyList<Tool> Tools`

          - `class BetaManagedAgentsAgentToolset20260401:`

            - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

              - `required Boolean Enabled`

              - `required Name Name`

                Built-in agent tool identifier.

                - `"bash"Bash`

                - `"edit"Edit`

                - `"read"Read`

                - `"write"Write`

                - `"glob"Glob`

                - `"grep"Grep`

                - `"web_fetch"WebFetch`

                - `"web_search"WebSearch`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                  - `required Type Type`

                    - `"always_allow"AlwaysAllow`

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

                  - `required Type Type`

                    - `"always_ask"AlwaysAsk`

            - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

              Resolved default configuration for agent tools.

              - `required Boolean Enabled`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

            - `required Type Type`

              - `"agent_toolset_20260401"AgentToolset20260401`

          - `class BetaManagedAgentsMcpToolset:`

            - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

              - `required Boolean Enabled`

              - `required string Name`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

            - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

              Resolved default configuration for all tools from an MCP server.

              - `required Boolean Enabled`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

            - `required string McpServerName`

            - `required Type Type`

              - `"mcp_toolset"McpToolset`

          - `class BetaManagedAgentsCustomTool:`

            A custom tool as returned in API responses.

            - `required string Description`

            - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

              JSON Schema for custom tool input parameters.

              - `JsonElement Type "object"constant`

              - `IReadOnlyDictionary<string, JsonElement>? Properties`

              - `IReadOnlyList<string>? Required`

            - `required string Name`

            - `required Type Type`

              - `"custom"Custom`

        - `required Type Type`

          - `"agent"Agent`

        - `required Int Version`

      - `class BetaManagedAgentsAdvisor:`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `required string Model`

          The advisor model id.

        - `required Type Type`

          - `"advisor"Advisor`

    - `required DateTimeOffset? ArchivedAt`

      A timestamp in RFC 3339 format

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required string? ParentThreadID`

      Parent thread that spawned this thread. Null for the primary thread.

    - `required string SessionID`

      The session this thread belongs to.

    - `required BetaManagedAgentsSessionThreadStats? Stats`

      Timing statistics for a session thread.

      - `Double ActiveSeconds`

        Cumulative time in seconds the thread spent actively running. Excludes idle time.

      - `Double DurationSeconds`

        Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      - `Double StartupSeconds`

        Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

    - `required BetaManagedAgentsSessionThreadStatus Status`

      SessionThreadStatus enum

      - `"running"Running`

      - `"idle"Idle`

      - `"rescheduling"Rescheduling`

      - `"terminated"Terminated`

    - `required Type Type`

      - `"session_thread"SessionThread`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

    - `required BetaManagedAgentsSessionThreadUsage? Usage`

      Cumulative token usage for a session thread across all turns.

      - `Double ActiveSeconds`

        Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      - `BetaManagedAgentsCacheCreationUsage CacheCreation`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `Int Ephemeral1hInputTokens`

          Tokens used to create 1-hour ephemeral cache entries.

        - `Int Ephemeral5mInputTokens`

          Tokens used to create 5-minute ephemeral cache entries.

      - `Int CacheReadInputTokens`

        Total tokens read from prompt cache.

      - `Int InputTokens`

        Total input tokens consumed across all turns.

      - `BetaMonetaryAmount? ListCost`

        A monetary amount in a specific currency.

        - `required string Amount`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `required BetaCurrency Currency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

          - `"USD"Usd`

      - `Int OutputTokens`

        Total output tokens generated across all turns.

      - `BetaManagedAgentsServerToolUsage? ServerToolUse`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `Int WebFetchRequests`

          Number of server-executed web fetch requests.

        - `Int WebSearchRequests`

          Number of server-executed web search requests.

  - `string? NextPage`

    Opaque cursor for the next page. Null when no more results.

### Example

```csharp
ThreadListParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

var page = await client.Beta.Sessions.Threads.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
      "agent": {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "description": "A focused research subagent.",
        "mcp_servers": [
          {
            "name": "example-mcp",
            "type": "url",
            "url": "https://example-server.modelcontextprotocol.io/sse"
          }
        ],
        "model": {
          "id": "claude-sonnet-4-6",
          "effort": {
            "type": "low"
          },
          "inference_geo": "inference_geo",
          "speed": "standard"
        },
        "name": "Researcher",
        "skills": [
          {
            "skill_id": "xlsx",
            "type": "anthropic",
            "version": "1"
          }
        ],
        "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
        "tools": [
          {
            "configs": [
              {
                "enabled": true,
                "name": "bash",
                "permission_policy": {
                  "type": "always_allow"
                }
              }
            ],
            "default_config": {
              "enabled": true,
              "permission_policy": {
                "type": "always_ask"
              }
            },
            "type": "agent_toolset_20260401"
          }
        ],
        "type": "agent",
        "version": 1
      },
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "parent_thread_id": null,
      "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
      "stats": {
        "active_seconds": 0,
        "duration_seconds": 0,
        "startup_seconds": 0
      },
      "status": "idle",
      "type": "session_thread",
      "updated_at": "2026-03-15T10:00:00Z",
      "usage": {
        "active_seconds": 0,
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "list_cost": {
          "amount": "2500",
          "currency": "USD"
        },
        "output_tokens": 0,
        "server_tool_use": {
          "web_fetch_requests": 0,
          "web_search_requests": 3
        }
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Session Thread

`BetaManagedAgentsSessionThread Beta.Sessions.Threads.Retrieve(ThreadRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

### Parameters

- `ThreadRetrieveParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string threadID`

    Path param: Path parameter thread_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsSessionThread:`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `required string ID`

    Unique identifier for this thread.

  - `required Agent Agent`

    A session-resolved multiagent roster entry.

    - `class BetaManagedAgentsSessionThreadAgent:`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `required string ID`

      - `required string? Description`

      - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

        - `required string Name`

        - `required Type Type`

          - `"url"Url`

        - `required string Url`

      - `required BetaManagedAgentsModelConfig Model`

        Model identifier and configuration.

        - `required BetaManagedAgentsModel ID`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-sonnet-5"ClaudeSonnet5`

            High-performance model for coding and agents

          - `"claude-fable-5"ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-5"ClaudeOpus5`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-8"ClaudeOpus4_8`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-7"ClaudeOpus4_7`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-6"ClaudeOpus4_6`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-6"ClaudeSonnet4_6`

            Best combination of speed and intelligence

          - `"claude-haiku-4-5"ClaudeHaiku4_5`

            Fastest model with near-frontier intelligence

          - `"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001`

            Fastest model with near-frontier intelligence

          - `"claude-opus-4-5"ClaudeOpus4_5`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-5"ClaudeSonnet4_5`

            High-performance model for agents and coding

          - `"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929`

            High-performance model for agents and coding

        - `Effort Effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `required Type Type`

              - `"low"Low`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `required Type Type`

              - `"medium"Medium`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `required Type Type`

              - `"high"High`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `required Type Type`

              - `"xhigh"Xhigh`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `required Type Type`

              - `"max"Max`

        - `string InferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"Standard`

          - `"fast"Fast`

      - `required string Name`

      - `required IReadOnlyList<Skill> Skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

          - `required string SkillID`

          - `required Type Type`

            - `"anthropic"Anthropic`

          - `required string Version`

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

          - `required string SkillID`

          - `required Type Type`

            - `"custom"Custom`

          - `required string Version`

      - `required string? System`

      - `required IReadOnlyList<Tool> Tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

          - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

            - `required Boolean Enabled`

            - `required Name Name`

              Built-in agent tool identifier.

              - `"bash"Bash`

              - `"edit"Edit`

              - `"read"Read`

              - `"write"Write`

              - `"glob"Glob`

              - `"grep"Grep`

              - `"web_fetch"WebFetch`

              - `"web_search"WebSearch`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

                - `required Type Type`

                  - `"always_allow"AlwaysAllow`

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

                - `required Type Type`

                  - `"always_ask"AlwaysAsk`

          - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for agent tools.

            - `required Boolean Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required Type Type`

            - `"agent_toolset_20260401"AgentToolset20260401`

        - `class BetaManagedAgentsMcpToolset:`

          - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

            - `required Boolean Enabled`

            - `required string Name`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `required Boolean Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required string McpServerName`

          - `required Type Type`

            - `"mcp_toolset"McpToolset`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

          - `required string Description`

          - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

            JSON Schema for custom tool input parameters.

            - `JsonElement Type "object"constant`

            - `IReadOnlyDictionary<string, JsonElement>? Properties`

            - `IReadOnlyList<string>? Required`

          - `required string Name`

          - `required Type Type`

            - `"custom"Custom`

      - `required Type Type`

        - `"agent"Agent`

      - `required Int Version`

    - `class BetaManagedAgentsAdvisor:`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `required string Model`

        The advisor model id.

      - `required Type Type`

        - `"advisor"Advisor`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? ParentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `required string SessionID`

    The session this thread belongs to.

  - `required BetaManagedAgentsSessionThreadStats? Stats`

    Timing statistics for a session thread.

    - `Double ActiveSeconds`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `Double DurationSeconds`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `Double StartupSeconds`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `required BetaManagedAgentsSessionThreadStatus Status`

    SessionThreadStatus enum

    - `"running"Running`

    - `"idle"Idle`

    - `"rescheduling"Rescheduling`

    - `"terminated"Terminated`

  - `required Type Type`

    - `"session_thread"SessionThread`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required BetaManagedAgentsSessionThreadUsage? Usage`

    Cumulative token usage for a session thread across all turns.

    - `Double ActiveSeconds`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

    - `BetaManagedAgentsCacheCreationUsage CacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Int Ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

      - `Int Ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

    - `Int CacheReadInputTokens`

      Total tokens read from prompt cache.

    - `Int InputTokens`

      Total input tokens consumed across all turns.

    - `BetaMonetaryAmount? ListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

        - `"USD"Usd`

    - `Int OutputTokens`

      Total output tokens generated across all turns.

    - `BetaManagedAgentsServerToolUsage? ServerToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `Int WebFetchRequests`

        Number of server-executed web fetch requests.

      - `Int WebSearchRequests`

        Number of server-executed web search requests.

### Example

```csharp
ThreadRetrieveParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ThreadID = "sthr_011CZkZVWa6oIjw0rgXZpnBt",
};

var betaManagedAgentsSessionThread = await client.Beta.Sessions.Threads.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsSessionThread);
```

#### Response

```json
{
  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "description": "A focused research subagent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-sonnet-4-6",
      "effort": {
        "type": "low"
      },
      "inference_geo": "inference_geo",
      "speed": "standard"
    },
    "name": "Researcher",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      }
    ],
    "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            }
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  },
  "status": "idle",
  "type": "session_thread",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "active_seconds": 0,
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "output_tokens": 0,
    "server_tool_use": {
      "web_fetch_requests": 0,
      "web_search_requests": 3
    }
  }
}
```

## Archive Session Thread

`BetaManagedAgentsSessionThread Beta.Sessions.Threads.Archive(ThreadArchiveParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/sessions/{session_id}/threads/{thread_id}/archive`

Archive Session Thread

### Parameters

- `ThreadArchiveParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string threadID`

    Path param: Path parameter thread_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsSessionThread:`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `required string ID`

    Unique identifier for this thread.

  - `required Agent Agent`

    A session-resolved multiagent roster entry.

    - `class BetaManagedAgentsSessionThreadAgent:`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `required string ID`

      - `required string? Description`

      - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

        - `required string Name`

        - `required Type Type`

          - `"url"Url`

        - `required string Url`

      - `required BetaManagedAgentsModelConfig Model`

        Model identifier and configuration.

        - `required BetaManagedAgentsModel ID`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-sonnet-5"ClaudeSonnet5`

            High-performance model for coding and agents

          - `"claude-fable-5"ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-5"ClaudeOpus5`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-8"ClaudeOpus4_8`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-7"ClaudeOpus4_7`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-6"ClaudeOpus4_6`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-6"ClaudeSonnet4_6`

            Best combination of speed and intelligence

          - `"claude-haiku-4-5"ClaudeHaiku4_5`

            Fastest model with near-frontier intelligence

          - `"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001`

            Fastest model with near-frontier intelligence

          - `"claude-opus-4-5"ClaudeOpus4_5`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-5"ClaudeSonnet4_5`

            High-performance model for agents and coding

          - `"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929`

            High-performance model for agents and coding

        - `Effort Effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `required Type Type`

              - `"low"Low`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `required Type Type`

              - `"medium"Medium`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `required Type Type`

              - `"high"High`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `required Type Type`

              - `"xhigh"Xhigh`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `required Type Type`

              - `"max"Max`

        - `string InferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"Standard`

          - `"fast"Fast`

      - `required string Name`

      - `required IReadOnlyList<Skill> Skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

          - `required string SkillID`

          - `required Type Type`

            - `"anthropic"Anthropic`

          - `required string Version`

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

          - `required string SkillID`

          - `required Type Type`

            - `"custom"Custom`

          - `required string Version`

      - `required string? System`

      - `required IReadOnlyList<Tool> Tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

          - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

            - `required Boolean Enabled`

            - `required Name Name`

              Built-in agent tool identifier.

              - `"bash"Bash`

              - `"edit"Edit`

              - `"read"Read`

              - `"write"Write`

              - `"glob"Glob`

              - `"grep"Grep`

              - `"web_fetch"WebFetch`

              - `"web_search"WebSearch`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

                - `required Type Type`

                  - `"always_allow"AlwaysAllow`

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

                - `required Type Type`

                  - `"always_ask"AlwaysAsk`

          - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for agent tools.

            - `required Boolean Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required Type Type`

            - `"agent_toolset_20260401"AgentToolset20260401`

        - `class BetaManagedAgentsMcpToolset:`

          - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

            - `required Boolean Enabled`

            - `required string Name`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `required Boolean Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required string McpServerName`

          - `required Type Type`

            - `"mcp_toolset"McpToolset`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

          - `required string Description`

          - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

            JSON Schema for custom tool input parameters.

            - `JsonElement Type "object"constant`

            - `IReadOnlyDictionary<string, JsonElement>? Properties`

            - `IReadOnlyList<string>? Required`

          - `required string Name`

          - `required Type Type`

            - `"custom"Custom`

      - `required Type Type`

        - `"agent"Agent`

      - `required Int Version`

    - `class BetaManagedAgentsAdvisor:`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `required string Model`

        The advisor model id.

      - `required Type Type`

        - `"advisor"Advisor`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? ParentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `required string SessionID`

    The session this thread belongs to.

  - `required BetaManagedAgentsSessionThreadStats? Stats`

    Timing statistics for a session thread.

    - `Double ActiveSeconds`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `Double DurationSeconds`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `Double StartupSeconds`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `required BetaManagedAgentsSessionThreadStatus Status`

    SessionThreadStatus enum

    - `"running"Running`

    - `"idle"Idle`

    - `"rescheduling"Rescheduling`

    - `"terminated"Terminated`

  - `required Type Type`

    - `"session_thread"SessionThread`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required BetaManagedAgentsSessionThreadUsage? Usage`

    Cumulative token usage for a session thread across all turns.

    - `Double ActiveSeconds`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

    - `BetaManagedAgentsCacheCreationUsage CacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Int Ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

      - `Int Ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

    - `Int CacheReadInputTokens`

      Total tokens read from prompt cache.

    - `Int InputTokens`

      Total input tokens consumed across all turns.

    - `BetaMonetaryAmount? ListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

        - `"USD"Usd`

    - `Int OutputTokens`

      Total output tokens generated across all turns.

    - `BetaManagedAgentsServerToolUsage? ServerToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `Int WebFetchRequests`

        Number of server-executed web fetch requests.

      - `Int WebSearchRequests`

        Number of server-executed web search requests.

### Example

```csharp
ThreadArchiveParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ThreadID = "sthr_011CZkZVWa6oIjw0rgXZpnBt",
};

var betaManagedAgentsSessionThread = await client.Beta.Sessions.Threads.Archive(parameters);

Console.WriteLine(betaManagedAgentsSessionThread);
```

#### Response

```json
{
  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "description": "A focused research subagent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-sonnet-4-6",
      "effort": {
        "type": "low"
      },
      "inference_geo": "inference_geo",
      "speed": "standard"
    },
    "name": "Researcher",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      }
    ],
    "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            }
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  },
  "status": "idle",
  "type": "session_thread",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "active_seconds": 0,
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "output_tokens": 0,
    "server_tool_use": {
      "web_fetch_requests": 0,
      "web_search_requests": 3
    }
  }
}
```

## Domain Types

### Beta Managed Agents Session Thread

- `class BetaManagedAgentsSessionThread:`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `required string ID`

    Unique identifier for this thread.

  - `required Agent Agent`

    A session-resolved multiagent roster entry.

    - `class BetaManagedAgentsSessionThreadAgent:`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `required string ID`

      - `required string? Description`

      - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

        - `required string Name`

        - `required Type Type`

          - `"url"Url`

        - `required string Url`

      - `required BetaManagedAgentsModelConfig Model`

        Model identifier and configuration.

        - `required BetaManagedAgentsModel ID`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-sonnet-5"ClaudeSonnet5`

            High-performance model for coding and agents

          - `"claude-fable-5"ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-5"ClaudeOpus5`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-8"ClaudeOpus4_8`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-7"ClaudeOpus4_7`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-6"ClaudeOpus4_6`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-6"ClaudeSonnet4_6`

            Best combination of speed and intelligence

          - `"claude-haiku-4-5"ClaudeHaiku4_5`

            Fastest model with near-frontier intelligence

          - `"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001`

            Fastest model with near-frontier intelligence

          - `"claude-opus-4-5"ClaudeOpus4_5`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-5"ClaudeSonnet4_5`

            High-performance model for agents and coding

          - `"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929`

            High-performance model for agents and coding

        - `Effort Effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `required Type Type`

              - `"low"Low`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `required Type Type`

              - `"medium"Medium`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `required Type Type`

              - `"high"High`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `required Type Type`

              - `"xhigh"Xhigh`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `required Type Type`

              - `"max"Max`

        - `string InferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"Standard`

          - `"fast"Fast`

      - `required string Name`

      - `required IReadOnlyList<Skill> Skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

          - `required string SkillID`

          - `required Type Type`

            - `"anthropic"Anthropic`

          - `required string Version`

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

          - `required string SkillID`

          - `required Type Type`

            - `"custom"Custom`

          - `required string Version`

      - `required string? System`

      - `required IReadOnlyList<Tool> Tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

          - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

            - `required Boolean Enabled`

            - `required Name Name`

              Built-in agent tool identifier.

              - `"bash"Bash`

              - `"edit"Edit`

              - `"read"Read`

              - `"write"Write`

              - `"glob"Glob`

              - `"grep"Grep`

              - `"web_fetch"WebFetch`

              - `"web_search"WebSearch`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

                - `required Type Type`

                  - `"always_allow"AlwaysAllow`

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

                - `required Type Type`

                  - `"always_ask"AlwaysAsk`

          - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for agent tools.

            - `required Boolean Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required Type Type`

            - `"agent_toolset_20260401"AgentToolset20260401`

        - `class BetaManagedAgentsMcpToolset:`

          - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

            - `required Boolean Enabled`

            - `required string Name`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `required Boolean Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required string McpServerName`

          - `required Type Type`

            - `"mcp_toolset"McpToolset`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

          - `required string Description`

          - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

            JSON Schema for custom tool input parameters.

            - `JsonElement Type "object"constant`

            - `IReadOnlyDictionary<string, JsonElement>? Properties`

            - `IReadOnlyList<string>? Required`

          - `required string Name`

          - `required Type Type`

            - `"custom"Custom`

      - `required Type Type`

        - `"agent"Agent`

      - `required Int Version`

    - `class BetaManagedAgentsAdvisor:`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `required string Model`

        The advisor model id.

      - `required Type Type`

        - `"advisor"Advisor`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? ParentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `required string SessionID`

    The session this thread belongs to.

  - `required BetaManagedAgentsSessionThreadStats? Stats`

    Timing statistics for a session thread.

    - `Double ActiveSeconds`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `Double DurationSeconds`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `Double StartupSeconds`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `required BetaManagedAgentsSessionThreadStatus Status`

    SessionThreadStatus enum

    - `"running"Running`

    - `"idle"Idle`

    - `"rescheduling"Rescheduling`

    - `"terminated"Terminated`

  - `required Type Type`

    - `"session_thread"SessionThread`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required BetaManagedAgentsSessionThreadUsage? Usage`

    Cumulative token usage for a session thread across all turns.

    - `Double ActiveSeconds`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

    - `BetaManagedAgentsCacheCreationUsage CacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Int Ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

      - `Int Ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

    - `Int CacheReadInputTokens`

      Total tokens read from prompt cache.

    - `Int InputTokens`

      Total input tokens consumed across all turns.

    - `BetaMonetaryAmount? ListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

        - `"USD"Usd`

    - `Int OutputTokens`

      Total output tokens generated across all turns.

    - `BetaManagedAgentsServerToolUsage? ServerToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `Int WebFetchRequests`

        Number of server-executed web fetch requests.

      - `Int WebSearchRequests`

        Number of server-executed web search requests.

### Beta Managed Agents Session Thread Stats

- `class BetaManagedAgentsSessionThreadStats:`

  Timing statistics for a session thread.

  - `Double ActiveSeconds`

    Cumulative time in seconds the thread spent actively running. Excludes idle time.

  - `Double DurationSeconds`

    Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

  - `Double StartupSeconds`

    Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

### Beta Managed Agents Session Thread Status

- `enum BetaManagedAgentsSessionThreadStatus:`

  SessionThreadStatus enum

  - `"running"Running`

  - `"idle"Idle`

  - `"rescheduling"Rescheduling`

  - `"terminated"Terminated`

### Beta Managed Agents Session Thread Usage

- `class BetaManagedAgentsSessionThreadUsage:`

  Cumulative token usage for a session thread across all turns.

  - `Double ActiveSeconds`

    Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

  - `BetaManagedAgentsCacheCreationUsage CacheCreation`

    Prompt-cache creation token usage broken down by cache lifetime.

    - `Int Ephemeral1hInputTokens`

      Tokens used to create 1-hour ephemeral cache entries.

    - `Int Ephemeral5mInputTokens`

      Tokens used to create 5-minute ephemeral cache entries.

  - `Int CacheReadInputTokens`

    Total tokens read from prompt cache.

  - `Int InputTokens`

    Total input tokens consumed across all turns.

  - `BetaMonetaryAmount? ListCost`

    A monetary amount in a specific currency.

    - `required string Amount`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `required BetaCurrency Currency`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `"USD"Usd`

  - `Int OutputTokens`

    Total output tokens generated across all turns.

  - `BetaManagedAgentsServerToolUsage? ServerToolUse`

    Cumulative count of server-executed tool invocations, broken down by tool.

    - `Int WebFetchRequests`

      Number of server-executed web fetch requests.

    - `Int WebSearchRequests`

      Number of server-executed web search requests.

### Beta Managed Agents Stream Session Thread Events

- `class BetaManagedAgentsStreamSessionThreadEvents: A class that can be one of several variants.union`

  Server-sent event in a single thread's stream.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

        - `required Type Type`

          - `"redacted"Redacted`

    - `required Type Type`

      - `"user.message"UserMessage`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `required string ID`

      Unique identifier for this event.

    - `required Type Type`

      - `"user.interrupt"UserInterrupt`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

    - `string? SessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Result Result`

      UserToolConfirmationResult enum

      - `"allow"Allow`

      - `"deny"Deny`

    - `required string ToolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

      - `"user.tool_confirmation"UserToolConfirmation`

    - `string? DenyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

    - `string? SessionThreadID`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string CustomToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

      - `"user.custom_tool_result"UserCustomToolResult`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

        - `required BetaManagedAgentsSearchResultCitations Citations`

          Citation settings for a search result.

          - `required Boolean Enabled`

            Whether citations are enabled for this search result.

        - `required IReadOnlyList<BetaManagedAgentsSearchResultContent> Content`

          Array of text content blocks from the search result.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `required string Source`

          The URL source of the search result.

        - `required string Title`

          The title of the search result.

        - `required Type Type`

          - `"search_result"SearchResult`

    - `Boolean? IsError`

      Whether the tool execution resulted in an error.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

    - `string? SessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string Name`

      Name of the custom tool being called.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.custom_tool_use"AgentCustomToolUse`

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Array of text blocks comprising the agent response.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.message"AgentMessage`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.thinking"AgentThinking`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string McpServerName`

      Name of the MCP server providing the tool.

    - `required string Name`

      Name of the MCP tool being used.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.mcp_tool_use"AgentMcpToolUse`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `"allow"Allow`

      - `"ask"Ask`

      - `"deny"Deny`

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string McpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.mcp_tool_result"AgentMcpToolResult`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Boolean? IsError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string Name`

      Name of the agent tool being used.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.tool_use"AgentToolUse`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `"allow"Allow`

      - `"ask"Ask`

      - `"deny"Deny`

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string ToolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `required Type Type`

      - `"agent.tool_result"AgentToolResult`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Boolean? IsError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `required string FromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.thread_message_received"AgentThreadMessageReceived`

    - `string? FromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent:`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string ToSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `required Type Type`

      - `"agent.thread_message_sent"AgentThreadMessageSent`

    - `string? ToAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.thread_context_compacted"AgentThreadContextCompacted`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Error Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"unknown_error"UnknownError`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

          - `"model_overloaded_error"ModelOverloadedError`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

          - `"model_rate_limited_error"ModelRateLimitedError`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

          - `"model_request_failed_error"ModelRequestFailedError`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `required string McpServerName`

          Name of the MCP server that failed to connect.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

          - `"mcp_connection_failed_error"McpConnectionFailedError`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `required string McpServerName`

          Name of the MCP server that failed authentication.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

          - `"mcp_authentication_failed_error"McpAuthenticationFailedError`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

          - `"billing_error"BillingError`

      - `class BetaManagedAgentsCredentialHostUnreachableError:`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `required string CredentialID`

          ID of the affected credential.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

          - `"credential_host_unreachable_error"CredentialHostUnreachableError`

        - `required string VaultID`

          ID of the vault containing the affected credential.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.error"SessionError`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.status_rescheduled"SessionStatusRescheduled`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.status_running"SessionStatusRunning`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required StopReason StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `required Type Type`

          - `"end_turn"EndTurn`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `required IReadOnlyList<string> EventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `required Type Type`

          - `"requires_action"RequiresAction`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `required Type Type`

          - `"retries_exhausted"RetriesExhausted`

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `required Type Type`

          - `"budget_reached"BudgetReached`

    - `required Type Type`

      - `"session.status_idle"SessionStatusIdle`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.status_terminated"SessionStatusTerminated`

  - `class BetaManagedAgentsSessionThreadCreatedEvent:`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the callable agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string SessionThreadID`

      Public `sthr_` ID of the newly created thread.

    - `required Type Type`

      - `"session.thread_created"SessionThreadCreated`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

    Emitted when an outcome evaluation cycle begins.

    - `required string ID`

      Unique identifier for this event.

    - `required Int Iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"span.outcome_evaluation_start"SpanOutcomeEvaluationStart`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `required string ID`

      Unique identifier for this event.

    - `required string Explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `required Int Iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `required string OutcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string Result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `required Type Type`

      - `"span.outcome_evaluation_end"SpanOutcomeEvaluationEnd`

    - `required BetaManagedAgentsSpanModelUsage Usage`

      Token usage for a single model request.

      - `required Int CacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

      - `required Int CacheReadInputTokens`

        Tokens read from prompt cache in this request.

      - `required Int InputTokens`

        Input tokens consumed by this request.

      - `required Int OutputTokens`

        Output tokens generated by this request.

      - `Speed? Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"Standard`

        - `"fast"Fast`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"span.model_request_start"SpanModelRequestStart`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `required string ID`

      Unique identifier for this event.

    - `required Boolean? IsError`

      Whether the model request resulted in an error.

    - `required string ModelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `required BetaManagedAgentsSpanModelUsage ModelUsage`

      Token usage for a single model request.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"span.model_request_end"SpanModelRequestEnd`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `required string ID`

      Unique identifier for this event.

    - `required Int Iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"span.outcome_evaluation_ongoing"SpanOutcomeEvaluationOngoing`

  - `class BetaManagedAgentsUserDefineOutcomeEvent:`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `required string ID`

      Unique identifier for this event.

    - `required string Description`

      What the agent should produce. Copied from the input event.

    - `required Int? MaxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `required string OutcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Rubric Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `required string FileID`

          ID of the rubric file.

        - `required Type Type`

          - `"file"File`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `required string Content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `required Type Type`

          - `"text"Text`

    - `required Type Type`

      - `"user.define_outcome"UserDefineOutcome`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.deleted"SessionDeleted`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that started running.

    - `required Type Type`

      - `"session.thread_status_running"SessionThreadStatusRunning`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `required StopReason StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `required Type Type`

      - `"session.thread_status_idle"SessionThreadStatusIdle`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that terminated.

    - `required Type Type`

      - `"session.thread_status_terminated"SessionThreadStatusTerminated`

  - `class BetaManagedAgentsUserToolResultEvent:`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `required string ID`

      Unique identifier for this event.

    - `required string ToolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

      - `"user.tool_result"UserToolResult`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Boolean? IsError`

      Whether the tool execution resulted in an error.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

    - `string? SessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that is retrying.

    - `required Type Type`

      - `"session.thread_status_rescheduled"SessionThreadStatusRescheduled`

  - `class BetaManagedAgentsSessionUpdatedEvent:`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.updated"SessionUpdated`

    - `BetaManagedAgentsSessionAgent? Agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `required string ID`

      - `required string? Description`

      - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

        - `required string Name`

        - `required Type Type`

          - `"url"Url`

        - `required string Url`

      - `required BetaManagedAgentsModelConfig Model`

        Model identifier and configuration.

        - `required BetaManagedAgentsModel ID`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-sonnet-5"ClaudeSonnet5`

            High-performance model for coding and agents

          - `"claude-fable-5"ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-5"ClaudeOpus5`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-8"ClaudeOpus4_8`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-7"ClaudeOpus4_7`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-6"ClaudeOpus4_6`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-6"ClaudeSonnet4_6`

            Best combination of speed and intelligence

          - `"claude-haiku-4-5"ClaudeHaiku4_5`

            Fastest model with near-frontier intelligence

          - `"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001`

            Fastest model with near-frontier intelligence

          - `"claude-opus-4-5"ClaudeOpus4_5`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-5"ClaudeSonnet4_5`

            High-performance model for agents and coding

          - `"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929`

            High-performance model for agents and coding

        - `Effort Effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `required Type Type`

              - `"low"Low`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `required Type Type`

              - `"medium"Medium`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `required Type Type`

              - `"high"High`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `required Type Type`

              - `"xhigh"Xhigh`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `required Type Type`

              - `"max"Max`

        - `string InferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"Standard`

          - `"fast"Fast`

      - `required BetaManagedAgentsSessionMultiagentCoordinator? Multiagent`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `required IReadOnlyList<Agent> Agents`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent:`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `required string ID`

            - `required string? Description`

            - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

              - `required string Name`

              - `required Type Type`

              - `required string Url`

            - `required BetaManagedAgentsModelConfig Model`

              Model identifier and configuration.

            - `required string Name`

            - `required IReadOnlyList<Skill> Skills`

              - `class BetaManagedAgentsAnthropicSkill:`

                A resolved Anthropic-managed skill.

                - `required string SkillID`

                - `required Type Type`

                  - `"anthropic"Anthropic`

                - `required string Version`

              - `class BetaManagedAgentsCustomSkill:`

                A resolved user-created custom skill.

                - `required string SkillID`

                - `required Type Type`

                  - `"custom"Custom`

                - `required string Version`

            - `required string? System`

            - `required IReadOnlyList<Tool> Tools`

              - `class BetaManagedAgentsAgentToolset20260401:`

                - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

                  - `required Boolean Enabled`

                  - `required Name Name`

                    Built-in agent tool identifier.

                    - `"bash"Bash`

                    - `"edit"Edit`

                    - `"read"Read`

                    - `"write"Write`

                    - `"glob"Glob`

                    - `"grep"Grep`

                    - `"web_fetch"WebFetch`

                    - `"web_search"WebSearch`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                      - `required Type Type`

                        - `"always_allow"AlwaysAllow`

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                      - `required Type Type`

                        - `"always_ask"AlwaysAsk`

                - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

                  Resolved default configuration for agent tools.

                  - `required Boolean Enabled`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required Type Type`

                  - `"agent_toolset_20260401"AgentToolset20260401`

              - `class BetaManagedAgentsMcpToolset:`

                - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

                  - `required Boolean Enabled`

                  - `required string Name`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `required Boolean Enabled`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required string McpServerName`

                - `required Type Type`

                  - `"mcp_toolset"McpToolset`

              - `class BetaManagedAgentsCustomTool:`

                A custom tool as returned in API responses.

                - `required string Description`

                - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

                  JSON Schema for custom tool input parameters.

                  - `JsonElement Type "object"constant`

                  - `IReadOnlyDictionary<string, JsonElement>? Properties`

                  - `IReadOnlyList<string>? Required`

                - `required string Name`

                - `required Type Type`

                  - `"custom"Custom`

            - `required Type Type`

              - `"agent"Agent`

            - `required Int Version`

          - `class BetaManagedAgentsAdvisor:`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `required string Model`

              The advisor model id.

            - `required Type Type`

              - `"advisor"Advisor`

        - `required Type Type`

          - `"coordinator"Coordinator`

      - `required string Name`

      - `required IReadOnlyList<Skill> Skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

      - `required string? System`

      - `required IReadOnlyList<Tool> Tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

        - `class BetaManagedAgentsMcpToolset:`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

      - `required Type Type`

        - `"agent"Agent`

      - `required Int Version`

    - `BetaManagedAgentsBudgetLimit? Budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `required BetaMonetaryAmount MaxListCost`

        A monetary amount in a specific currency.

        - `required string Amount`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `required BetaCurrency Currency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

          - `"USD"Usd`

      - `required Type Type`

        - `"limit"Limit`

    - `IReadOnlyDictionary<string, string> Metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `string? Title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent:`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `required BetaManagedAgentsStartEventPreview Event`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview:`

        - `required string ID`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `required Type Type`

          - `"agent.message"AgentMessage`

      - `class BetaManagedAgentsAgentThinkingPreview:`

        - `required string ID`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `required Type Type`

          - `"agent.thinking"AgentThinking`

    - `required Type Type`

      - `"event_start"EventStart`

  - `class BetaManagedAgentsDeltaEvent:`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `required BetaManagedAgentsDeltaContent Delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `required BetaManagedAgentsTextBlock Content`

        Regular text content.

      - `required Type Type`

        - `"content_delta"ContentDelta`

      - `Long Index`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    - `required string EventID`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `required Type Type`

      - `"event_delta"EventDelta`

  - `class BetaManagedAgentsSystemMessageEvent:`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

      System content blocks. Text-only.

      - `required string Text`

        The text content.

      - `required Type Type`

        - `"text"Text`

    - `required Type Type`

      - `"system.message"SystemMessage`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsSessionUsageEvent:`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.usage"SessionUsage`

    - `required BetaManagedAgentsSessionUsageSnapshot Usage`

      Point-in-time snapshot of a session's cumulative usage.

      - `Double ActiveSeconds`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

      - `BetaManagedAgentsCacheCreationUsage CacheCreation`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `Int Ephemeral1hInputTokens`

          Tokens used to create 1-hour ephemeral cache entries.

        - `Int Ephemeral5mInputTokens`

          Tokens used to create 5-minute ephemeral cache entries.

      - `Int CacheReadInputTokens`

        Total tokens read from prompt cache.

      - `Int InputTokens`

        Total input tokens consumed across all turns.

      - `BetaMonetaryAmount ListCost`

        A monetary amount in a specific currency.

      - `Int OutputTokens`

        Total output tokens generated across all turns.

      - `BetaManagedAgentsServerToolUsage ServerToolUse`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `Int WebFetchRequests`

          Number of server-executed web fetch requests.

        - `Int WebSearchRequests`

          Number of server-executed web search requests.

    - `BetaManagedAgentsBudgetLimit? Budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

# Events

## List Session Thread Events

`EventListPageResponse Beta.Sessions.Threads.Events.List(EventListParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

### Parameters

- `EventListParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string threadID`

    Path param: Path parameter thread_id

  - `Int limit`

    Query param: Query parameter for limit

  - `string page`

    Query param: Query parameter for page

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class EventListPageResponse:`

  Paginated list of events for a single thread within a `session`.

  - `IReadOnlyList<BetaManagedAgentsSessionEvent> Data`

    Events for the thread, ordered by `processed_at`.

    - `class BetaManagedAgentsUserMessageEvent:`

      A user message event in the session conversation.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks comprising the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

            - `"redacted"Redacted`

      - `required Type Type`

        - `"user.message"UserMessage`

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserInterruptEvent:`

      An interrupt event that pauses agent execution and returns control to the user.

      - `required string ID`

        Unique identifier for this event.

      - `required Type Type`

        - `"user.interrupt"UserInterrupt`

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

      - `string? SessionThreadID`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `class BetaManagedAgentsUserToolConfirmationEvent:`

      A tool confirmation event that approves or denies a pending tool execution.

      - `required string ID`

        Unique identifier for this event.

      - `required Result Result`

        UserToolConfirmationResult enum

        - `"allow"Allow`

        - `"deny"Deny`

      - `required string ToolUseID`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `required Type Type`

        - `"user.tool_confirmation"UserToolConfirmation`

      - `string? DenyMessage`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

      - `string? SessionThreadID`

        When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

    - `class BetaManagedAgentsUserCustomToolResultEvent:`

      Event sent by the client providing the result of a custom tool execution.

      - `required string ID`

        Unique identifier for this event.

      - `required string CustomToolUseID`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `required Type Type`

        - `"user.custom_tool_result"UserCustomToolResult`

      - `IReadOnlyList<Content> Content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock:`

          A block containing a web search result.

          - `required BetaManagedAgentsSearchResultCitations Citations`

            Citation settings for a search result.

            - `required Boolean Enabled`

              Whether citations are enabled for this search result.

          - `required IReadOnlyList<BetaManagedAgentsSearchResultContent> Content`

            Array of text content blocks from the search result.

            - `required string Text`

              The text content.

            - `required Type Type`

              - `"text"Text`

          - `required string Source`

            The URL source of the search result.

          - `required string Title`

            The title of the search result.

          - `required Type Type`

            - `"search_result"SearchResult`

      - `Boolean? IsError`

        Whether the tool execution resulted in an error.

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

      - `string? SessionThreadID`

        Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

    - `class BetaManagedAgentsAgentCustomToolUseEvent:`

      Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyDictionary<string, JsonElement> Input`

        Input parameters for the tool call.

      - `required string Name`

        Name of the custom tool being called.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"agent.custom_tool_use"AgentCustomToolUse`

      - `string? SessionThreadID`

        When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

    - `class BetaManagedAgentsAgentMessageEvent:`

      An agent response event in the session conversation.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyList<Content> Content`

        Array of text blocks comprising the agent response.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"agent.message"AgentMessage`

    - `class BetaManagedAgentsAgentThinkingEvent:`

      Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"agent.thinking"AgentThinking`

    - `class BetaManagedAgentsAgentMcpToolUseEvent:`

      Event emitted when the agent invokes a tool provided by an MCP server.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyDictionary<string, JsonElement> Input`

        Input parameters for the tool call.

      - `required string McpServerName`

        Name of the MCP server providing the tool.

      - `required string Name`

        Name of the MCP tool being used.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"agent.mcp_tool_use"AgentMcpToolUse`

      - `EvaluatedPermission EvaluatedPermission`

        AgentEvaluatedPermission enum

        - `"allow"Allow`

        - `"ask"Ask`

        - `"deny"Deny`

      - `string? SessionThreadID`

        When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

    - `class BetaManagedAgentsAgentMcpToolResultEvent:`

      Event representing the result of an MCP tool execution.

      - `required string ID`

        Unique identifier for this event.

      - `required string McpToolUseID`

        The id of the `agent.mcp_tool_use` event this result corresponds to.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"agent.mcp_tool_result"AgentMcpToolResult`

      - `IReadOnlyList<Content> Content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock:`

          A block containing a web search result.

      - `Boolean? IsError`

        Whether the tool execution resulted in an error.

    - `class BetaManagedAgentsAgentToolUseEvent:`

      Event emitted when the agent invokes a built-in agent tool.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyDictionary<string, JsonElement> Input`

        Input parameters for the tool call.

      - `required string Name`

        Name of the agent tool being used.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"agent.tool_use"AgentToolUse`

      - `EvaluatedPermission EvaluatedPermission`

        AgentEvaluatedPermission enum

        - `"allow"Allow`

        - `"ask"Ask`

        - `"deny"Deny`

      - `string? SessionThreadID`

        When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

    - `class BetaManagedAgentsAgentToolResultEvent:`

      Event representing the result of an agent tool execution.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required string ToolUseID`

        The id of the `agent.tool_use` event this result corresponds to.

      - `required Type Type`

        - `"agent.tool_result"AgentToolResult`

      - `IReadOnlyList<Content> Content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock:`

          A block containing a web search result.

      - `Boolean? IsError`

        Whether the tool execution resulted in an error.

    - `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

      Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyList<Content> Content`

        Message content blocks.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

      - `required string FromSessionThreadID`

        Public `sthr_` ID of the thread that sent the message.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"agent.thread_message_received"AgentThreadMessageReceived`

      - `string? FromAgentName`

        Name of the callable agent this message came from. Absent when received from the primary agent.

    - `class BetaManagedAgentsAgentThreadMessageSentEvent:`

      Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyList<Content> Content`

        Message content blocks.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required string ToSessionThreadID`

        Public `sthr_` ID of the thread the message was sent to.

      - `required Type Type`

        - `"agent.thread_message_sent"AgentThreadMessageSent`

      - `string? ToAgentName`

        Name of the callable agent this message was sent to. Absent when sent to the primary agent.

    - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

      Indicates that context compaction (summarization) occurred during the session.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"agent.thread_context_compacted"AgentThreadContextCompacted`

    - `class BetaManagedAgentsSessionErrorEvent:`

      An error event indicating a problem occurred during session execution.

      - `required string ID`

        Unique identifier for this event.

      - `required Error Error`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `class BetaManagedAgentsUnknownError:`

          An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `required Type Type`

                - `"retrying"Retrying`

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `required Type Type`

                - `"exhausted"Exhausted`

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

              - `required Type Type`

                - `"terminal"Terminal`

          - `required Type Type`

            - `"unknown_error"UnknownError`

        - `class BetaManagedAgentsModelOverloadedError:`

          The model is currently overloaded. Emitted after automatic retries are exhausted.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

          - `required Type Type`

            - `"model_overloaded_error"ModelOverloadedError`

        - `class BetaManagedAgentsModelRateLimitedError:`

          The model request was rate-limited.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

          - `required Type Type`

            - `"model_rate_limited_error"ModelRateLimitedError`

        - `class BetaManagedAgentsModelRequestFailedError:`

          A model request failed for a reason other than overload or rate-limiting.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

          - `required Type Type`

            - `"model_request_failed_error"ModelRequestFailedError`

        - `class BetaManagedAgentsMcpConnectionFailedError:`

          Failed to connect to an MCP server.

          - `required string McpServerName`

            Name of the MCP server that failed to connect.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

          - `required Type Type`

            - `"mcp_connection_failed_error"McpConnectionFailedError`

        - `class BetaManagedAgentsMcpAuthenticationFailedError:`

          Authentication to an MCP server failed.

          - `required string McpServerName`

            Name of the MCP server that failed authentication.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

          - `required Type Type`

            - `"mcp_authentication_failed_error"McpAuthenticationFailedError`

        - `class BetaManagedAgentsBillingError:`

          The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

          - `required Type Type`

            - `"billing_error"BillingError`

        - `class BetaManagedAgentsCredentialHostUnreachableError:`

          An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

          - `required string CredentialID`

            ID of the affected credential.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

          - `required Type Type`

            - `"credential_host_unreachable_error"CredentialHostUnreachableError`

          - `required string VaultID`

            ID of the vault containing the affected credential.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"session.error"SessionError`

    - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

      Indicates the session is recovering from an error state and is rescheduled for execution.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"session.status_rescheduled"SessionStatusRescheduled`

    - `class BetaManagedAgentsSessionStatusRunningEvent:`

      Indicates the session is actively running and the agent is working.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"session.status_running"SessionStatusRunning`

    - `class BetaManagedAgentsSessionStatusIdleEvent:`

      Indicates the agent has paused and is awaiting user input.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required StopReason StopReason`

        The agent completed its turn naturally and is ready for the next user message.

        - `class BetaManagedAgentsSessionEndTurn:`

          The agent completed its turn naturally and is ready for the next user message.

          - `required Type Type`

            - `"end_turn"EndTurn`

        - `class BetaManagedAgentsSessionRequiresAction:`

          The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

          - `required IReadOnlyList<string> EventIds`

            The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

          - `required Type Type`

            - `"requires_action"RequiresAction`

        - `class BetaManagedAgentsSessionRetriesExhausted:`

          The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

          - `required Type Type`

            - `"retries_exhausted"RetriesExhausted`

        - `class BetaManagedAgentsSessionBudgetReached:`

          The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

          - `required Type Type`

            - `"budget_reached"BudgetReached`

      - `required Type Type`

        - `"session.status_idle"SessionStatusIdle`

    - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

      Indicates the session has terminated, either due to an error or completion.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"session.status_terminated"SessionStatusTerminated`

    - `class BetaManagedAgentsSessionThreadCreatedEvent:`

      Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

      - `required string ID`

        Unique identifier for this event.

      - `required string AgentName`

        Name of the callable agent the thread runs.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required string SessionThreadID`

        Public `sthr_` ID of the newly created thread.

      - `required Type Type`

        - `"session.thread_created"SessionThreadCreated`

    - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

      Emitted when an outcome evaluation cycle begins.

      - `required string ID`

        Unique identifier for this event.

      - `required Int Iteration`

        0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      - `required string OutcomeID`

        The `outc_` ID of the outcome being evaluated.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"span.outcome_evaluation_start"SpanOutcomeEvaluationStart`

    - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

      Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

      - `required string ID`

        Unique identifier for this event.

      - `required string Explanation`

        Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

      - `required Int Iteration`

        0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      - `required string OutcomeEvaluationStartID`

        The id of the corresponding `span.outcome_evaluation_start` event.

      - `required string OutcomeID`

        The `outc_` ID of the outcome being evaluated.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required string Result`

        Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

      - `required Type Type`

        - `"span.outcome_evaluation_end"SpanOutcomeEvaluationEnd`

      - `required BetaManagedAgentsSpanModelUsage Usage`

        Token usage for a single model request.

        - `required Int CacheCreationInputTokens`

          Tokens used to create prompt cache in this request.

        - `required Int CacheReadInputTokens`

          Tokens read from prompt cache in this request.

        - `required Int InputTokens`

          Input tokens consumed by this request.

        - `required Int OutputTokens`

          Output tokens generated by this request.

        - `Speed? Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"Standard`

          - `"fast"Fast`

    - `class BetaManagedAgentsSpanModelRequestStartEvent:`

      Emitted when a model request is initiated by the agent.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"span.model_request_start"SpanModelRequestStart`

    - `class BetaManagedAgentsSpanModelRequestEndEvent:`

      Emitted when a model request completes.

      - `required string ID`

        Unique identifier for this event.

      - `required Boolean? IsError`

        Whether the model request resulted in an error.

      - `required string ModelRequestStartID`

        The id of the corresponding `span.model_request_start` event.

      - `required BetaManagedAgentsSpanModelUsage ModelUsage`

        Token usage for a single model request.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"span.model_request_end"SpanModelRequestEnd`

    - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

      Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

      - `required string ID`

        Unique identifier for this event.

      - `required Int Iteration`

        0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      - `required string OutcomeID`

        The `outc_` ID of the outcome being evaluated.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"span.outcome_evaluation_ongoing"SpanOutcomeEvaluationOngoing`

    - `class BetaManagedAgentsUserDefineOutcomeEvent:`

      Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

      - `required string ID`

        Unique identifier for this event.

      - `required string Description`

        What the agent should produce. Copied from the input event.

      - `required Int? MaxIterations`

        Evaluate-then-revise cycles before giving up. Default 3, max 20.

      - `required string OutcomeID`

        Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

            - `"file"File`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

            - `"text"Text`

      - `required Type Type`

        - `"user.define_outcome"UserDefineOutcome`

    - `class BetaManagedAgentsSessionDeletedEvent:`

      Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"session.deleted"SessionDeleted`

    - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

      A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `required string ID`

        Unique identifier for this event.

      - `required string AgentName`

        Name of the agent the thread runs.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required string SessionThreadID`

        Public sthr_ ID of the thread that started running.

      - `required Type Type`

        - `"session.thread_status_running"SessionThreadStatusRunning`

    - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

      A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `required string ID`

        Unique identifier for this event.

      - `required string AgentName`

        Name of the agent the thread runs.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required string SessionThreadID`

        Public sthr_ ID of the thread that went idle.

      - `required StopReason StopReason`

        The agent completed its turn naturally and is ready for the next user message.

        - `class BetaManagedAgentsSessionEndTurn:`

          The agent completed its turn naturally and is ready for the next user message.

        - `class BetaManagedAgentsSessionRequiresAction:`

          The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `class BetaManagedAgentsSessionRetriesExhausted:`

          The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `class BetaManagedAgentsSessionBudgetReached:`

          The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

      - `required Type Type`

        - `"session.thread_status_idle"SessionThreadStatusIdle`

    - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

      A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `required string ID`

        Unique identifier for this event.

      - `required string AgentName`

        Name of the agent the thread runs.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required string SessionThreadID`

        Public sthr_ ID of the thread that terminated.

      - `required Type Type`

        - `"session.thread_status_terminated"SessionThreadStatusTerminated`

    - `class BetaManagedAgentsUserToolResultEvent:`

      Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `required string ID`

        Unique identifier for this event.

      - `required string ToolUseID`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `required Type Type`

        - `"user.tool_result"UserToolResult`

      - `IReadOnlyList<Content> Content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock:`

          A block containing a web search result.

      - `Boolean? IsError`

        Whether the tool execution resulted in an error.

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

      - `string? SessionThreadID`

        Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

    - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

      A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `required string ID`

        Unique identifier for this event.

      - `required string AgentName`

        Name of the agent the thread runs.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required string SessionThreadID`

        Public sthr_ ID of the thread that is retrying.

      - `required Type Type`

        - `"session.thread_status_rescheduled"SessionThreadStatusRescheduled`

    - `class BetaManagedAgentsSessionUpdatedEvent:`

      Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"session.updated"SessionUpdated`

      - `BetaManagedAgentsSessionAgent? Agent`

        Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

        - `required string ID`

        - `required string? Description`

        - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

          - `required string Name`

          - `required Type Type`

            - `"url"Url`

          - `required string Url`

        - `required BetaManagedAgentsModelConfig Model`

          Model identifier and configuration.

          - `required BetaManagedAgentsModel ID`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `"claude-sonnet-5"ClaudeSonnet5`

              High-performance model for coding and agents

            - `"claude-fable-5"ClaudeFable5`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-opus-5"ClaudeOpus5`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-8"ClaudeOpus4_8`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-7"ClaudeOpus4_7`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-6"ClaudeOpus4_6`

              Powerful intelligence for long-running agents and coding

            - `"claude-sonnet-4-6"ClaudeSonnet4_6`

              Best combination of speed and intelligence

            - `"claude-haiku-4-5"ClaudeHaiku4_5`

              Fastest model with near-frontier intelligence

            - `"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001`

              Fastest model with near-frontier intelligence

            - `"claude-opus-4-5"ClaudeOpus4_5`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101`

              Powerful intelligence for long-running agents and coding

            - `"claude-sonnet-4-5"ClaudeSonnet4_5`

              High-performance model for agents and coding

            - `"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929`

              High-performance model for agents and coding

          - `Effort Effort`

            How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

            - `class BetaManagedAgentsEffortLow:`

              Low effort. Favors latency over reasoning depth.

              - `required Type Type`

                - `"low"Low`

            - `class BetaManagedAgentsEffortMedium:`

              Medium effort. Balances latency and reasoning depth.

              - `required Type Type`

                - `"medium"Medium`

            - `class BetaManagedAgentsEffortHigh:`

              High effort. Favors reasoning depth.

              - `required Type Type`

                - `"high"High`

            - `class BetaManagedAgentsEffortXhigh:`

              Extra-high effort. Not all models accept this level.

              - `required Type Type`

                - `"xhigh"Xhigh`

            - `class BetaManagedAgentsEffortMax:`

              Maximum effort. Favors reasoning depth over latency.

              - `required Type Type`

                - `"max"Max`

          - `string InferenceGeo`

            Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

          - `Speed Speed`

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `"standard"Standard`

            - `"fast"Fast`

        - `required BetaManagedAgentsSessionMultiagentCoordinator? Multiagent`

          Resolved coordinator topology with full agent definitions for each roster member.

          - `required IReadOnlyList<Agent> Agents`

            Full `agent` definitions the coordinator may spawn as session threads.

            - `class BetaManagedAgentsSessionThreadAgent:`

              Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

              - `required string ID`

              - `required string? Description`

              - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

                - `required string Name`

                - `required Type Type`

                - `required string Url`

              - `required BetaManagedAgentsModelConfig Model`

                Model identifier and configuration.

              - `required string Name`

              - `required IReadOnlyList<Skill> Skills`

                - `class BetaManagedAgentsAnthropicSkill:`

                  A resolved Anthropic-managed skill.

                  - `required string SkillID`

                  - `required Type Type`

                    - `"anthropic"Anthropic`

                  - `required string Version`

                - `class BetaManagedAgentsCustomSkill:`

                  A resolved user-created custom skill.

                  - `required string SkillID`

                  - `required Type Type`

                    - `"custom"Custom`

                  - `required string Version`

              - `required string? System`

              - `required IReadOnlyList<Tool> Tools`

                - `class BetaManagedAgentsAgentToolset20260401:`

                  - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

                    - `required Boolean Enabled`

                    - `required Name Name`

                      Built-in agent tool identifier.

                      - `"bash"Bash`

                      - `"edit"Edit`

                      - `"read"Read`

                      - `"write"Write`

                      - `"glob"Glob`

                      - `"grep"Grep`

                      - `"web_fetch"WebFetch`

                      - `"web_search"WebSearch`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                        - `required Type Type`

                          - `"always_allow"AlwaysAllow`

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                        - `required Type Type`

                          - `"always_ask"AlwaysAsk`

                  - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

                    Resolved default configuration for agent tools.

                    - `required Boolean Enabled`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                  - `required Type Type`

                    - `"agent_toolset_20260401"AgentToolset20260401`

                - `class BetaManagedAgentsMcpToolset:`

                  - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

                    - `required Boolean Enabled`

                    - `required string Name`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                  - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

                    Resolved default configuration for all tools from an MCP server.

                    - `required Boolean Enabled`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                  - `required string McpServerName`

                  - `required Type Type`

                    - `"mcp_toolset"McpToolset`

                - `class BetaManagedAgentsCustomTool:`

                  A custom tool as returned in API responses.

                  - `required string Description`

                  - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

                    JSON Schema for custom tool input parameters.

                    - `JsonElement Type "object"constant`

                    - `IReadOnlyDictionary<string, JsonElement>? Properties`

                    - `IReadOnlyList<string>? Required`

                  - `required string Name`

                  - `required Type Type`

                    - `"custom"Custom`

              - `required Type Type`

                - `"agent"Agent`

              - `required Int Version`

            - `class BetaManagedAgentsAdvisor:`

              Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

              - `required string Model`

                The advisor model id.

              - `required Type Type`

                - `"advisor"Advisor`

          - `required Type Type`

            - `"coordinator"Coordinator`

        - `required string Name`

        - `required IReadOnlyList<Skill> Skills`

          - `class BetaManagedAgentsAnthropicSkill:`

            A resolved Anthropic-managed skill.

          - `class BetaManagedAgentsCustomSkill:`

            A resolved user-created custom skill.

        - `required string? System`

        - `required IReadOnlyList<Tool> Tools`

          - `class BetaManagedAgentsAgentToolset20260401:`

          - `class BetaManagedAgentsMcpToolset:`

          - `class BetaManagedAgentsCustomTool:`

            A custom tool as returned in API responses.

        - `required Type Type`

          - `"agent"Agent`

        - `required Int Version`

      - `BetaManagedAgentsBudgetLimit? Budget`

        A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

        - `required BetaMonetaryAmount MaxListCost`

          A monetary amount in a specific currency.

          - `required string Amount`

            Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

          - `required BetaCurrency Currency`

            Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

            - `"USD"Usd`

        - `required Type Type`

          - `"limit"Limit`

      - `IReadOnlyDictionary<string, string> Metadata`

        The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

      - `string? Title`

        The session's new title. Present only when the update changed it.

    - `class BetaManagedAgentsSystemMessageEvent:`

      A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks. Text-only.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `required Type Type`

        - `"system.message"SystemMessage`

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsSessionUsageEvent:`

      Periodic snapshot of the session's cumulative usage and tracked list cost.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"session.usage"SessionUsage`

      - `required BetaManagedAgentsSessionUsageSnapshot Usage`

        Point-in-time snapshot of a session's cumulative usage.

        - `Double ActiveSeconds`

          Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        - `BetaManagedAgentsCacheCreationUsage CacheCreation`

          Prompt-cache creation token usage broken down by cache lifetime.

          - `Int Ephemeral1hInputTokens`

            Tokens used to create 1-hour ephemeral cache entries.

          - `Int Ephemeral5mInputTokens`

            Tokens used to create 5-minute ephemeral cache entries.

        - `Int CacheReadInputTokens`

          Total tokens read from prompt cache.

        - `Int InputTokens`

          Total input tokens consumed across all turns.

        - `BetaMonetaryAmount ListCost`

          A monetary amount in a specific currency.

        - `Int OutputTokens`

          Total output tokens generated across all turns.

        - `BetaManagedAgentsServerToolUsage ServerToolUse`

          Cumulative count of server-executed tool invocations, broken down by tool.

          - `Int WebFetchRequests`

            Number of server-executed web fetch requests.

          - `Int WebSearchRequests`

            Number of server-executed web search requests.

      - `BetaManagedAgentsBudgetLimit? Budget`

        A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `string? NextPage`

    Opaque cursor for the next page. Null when no more results.

### Example

```csharp
EventListParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ThreadID = "sthr_011CZkZVWa6oIjw0rgXZpnBt",
};

var page = await client.Beta.Sessions.Threads.Events.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "next_page"
}
```

## Stream Session Thread Events

`BetaManagedAgentsStreamSessionThreadEvents Beta.Sessions.Threads.Events.StreamStreaming(EventStreamParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

### Parameters

- `EventStreamParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string threadID`

    Path param: Path parameter thread_id

  - `IReadOnlyList<BetaManagedAgentsDeltaType> eventDeltas`

    Query param: When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

    - `"agent.message"AgentMessage`

    - `"agent.thinking"AgentThinking`

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsStreamSessionThreadEvents: A class that can be one of several variants.union`

  Server-sent event in a single thread's stream.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

        - `required Type Type`

          - `"redacted"Redacted`

    - `required Type Type`

      - `"user.message"UserMessage`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `required string ID`

      Unique identifier for this event.

    - `required Type Type`

      - `"user.interrupt"UserInterrupt`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

    - `string? SessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Result Result`

      UserToolConfirmationResult enum

      - `"allow"Allow`

      - `"deny"Deny`

    - `required string ToolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

      - `"user.tool_confirmation"UserToolConfirmation`

    - `string? DenyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

    - `string? SessionThreadID`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string CustomToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

      - `"user.custom_tool_result"UserCustomToolResult`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

        - `required BetaManagedAgentsSearchResultCitations Citations`

          Citation settings for a search result.

          - `required Boolean Enabled`

            Whether citations are enabled for this search result.

        - `required IReadOnlyList<BetaManagedAgentsSearchResultContent> Content`

          Array of text content blocks from the search result.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `required string Source`

          The URL source of the search result.

        - `required string Title`

          The title of the search result.

        - `required Type Type`

          - `"search_result"SearchResult`

    - `Boolean? IsError`

      Whether the tool execution resulted in an error.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

    - `string? SessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string Name`

      Name of the custom tool being called.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.custom_tool_use"AgentCustomToolUse`

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Array of text blocks comprising the agent response.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.message"AgentMessage`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.thinking"AgentThinking`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string McpServerName`

      Name of the MCP server providing the tool.

    - `required string Name`

      Name of the MCP tool being used.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.mcp_tool_use"AgentMcpToolUse`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `"allow"Allow`

      - `"ask"Ask`

      - `"deny"Deny`

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string McpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.mcp_tool_result"AgentMcpToolResult`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Boolean? IsError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string Name`

      Name of the agent tool being used.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.tool_use"AgentToolUse`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `"allow"Allow`

      - `"ask"Ask`

      - `"deny"Deny`

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string ToolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `required Type Type`

      - `"agent.tool_result"AgentToolResult`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Boolean? IsError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `required string FromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.thread_message_received"AgentThreadMessageReceived`

    - `string? FromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent:`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string ToSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `required Type Type`

      - `"agent.thread_message_sent"AgentThreadMessageSent`

    - `string? ToAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.thread_context_compacted"AgentThreadContextCompacted`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Error Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"unknown_error"UnknownError`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

          - `"model_overloaded_error"ModelOverloadedError`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

          - `"model_rate_limited_error"ModelRateLimitedError`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

          - `"model_request_failed_error"ModelRequestFailedError`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `required string McpServerName`

          Name of the MCP server that failed to connect.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

          - `"mcp_connection_failed_error"McpConnectionFailedError`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `required string McpServerName`

          Name of the MCP server that failed authentication.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

          - `"mcp_authentication_failed_error"McpAuthenticationFailedError`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

          - `"billing_error"BillingError`

      - `class BetaManagedAgentsCredentialHostUnreachableError:`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `required string CredentialID`

          ID of the affected credential.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

          - `"credential_host_unreachable_error"CredentialHostUnreachableError`

        - `required string VaultID`

          ID of the vault containing the affected credential.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.error"SessionError`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.status_rescheduled"SessionStatusRescheduled`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.status_running"SessionStatusRunning`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required StopReason StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `required Type Type`

          - `"end_turn"EndTurn`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `required IReadOnlyList<string> EventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `required Type Type`

          - `"requires_action"RequiresAction`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `required Type Type`

          - `"retries_exhausted"RetriesExhausted`

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `required Type Type`

          - `"budget_reached"BudgetReached`

    - `required Type Type`

      - `"session.status_idle"SessionStatusIdle`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.status_terminated"SessionStatusTerminated`

  - `class BetaManagedAgentsSessionThreadCreatedEvent:`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the callable agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string SessionThreadID`

      Public `sthr_` ID of the newly created thread.

    - `required Type Type`

      - `"session.thread_created"SessionThreadCreated`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

    Emitted when an outcome evaluation cycle begins.

    - `required string ID`

      Unique identifier for this event.

    - `required Int Iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"span.outcome_evaluation_start"SpanOutcomeEvaluationStart`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `required string ID`

      Unique identifier for this event.

    - `required string Explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `required Int Iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `required string OutcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string Result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `required Type Type`

      - `"span.outcome_evaluation_end"SpanOutcomeEvaluationEnd`

    - `required BetaManagedAgentsSpanModelUsage Usage`

      Token usage for a single model request.

      - `required Int CacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

      - `required Int CacheReadInputTokens`

        Tokens read from prompt cache in this request.

      - `required Int InputTokens`

        Input tokens consumed by this request.

      - `required Int OutputTokens`

        Output tokens generated by this request.

      - `Speed? Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"Standard`

        - `"fast"Fast`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"span.model_request_start"SpanModelRequestStart`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `required string ID`

      Unique identifier for this event.

    - `required Boolean? IsError`

      Whether the model request resulted in an error.

    - `required string ModelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `required BetaManagedAgentsSpanModelUsage ModelUsage`

      Token usage for a single model request.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"span.model_request_end"SpanModelRequestEnd`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `required string ID`

      Unique identifier for this event.

    - `required Int Iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"span.outcome_evaluation_ongoing"SpanOutcomeEvaluationOngoing`

  - `class BetaManagedAgentsUserDefineOutcomeEvent:`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `required string ID`

      Unique identifier for this event.

    - `required string Description`

      What the agent should produce. Copied from the input event.

    - `required Int? MaxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `required string OutcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Rubric Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `required string FileID`

          ID of the rubric file.

        - `required Type Type`

          - `"file"File`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `required string Content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `required Type Type`

          - `"text"Text`

    - `required Type Type`

      - `"user.define_outcome"UserDefineOutcome`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.deleted"SessionDeleted`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that started running.

    - `required Type Type`

      - `"session.thread_status_running"SessionThreadStatusRunning`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `required StopReason StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `required Type Type`

      - `"session.thread_status_idle"SessionThreadStatusIdle`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that terminated.

    - `required Type Type`

      - `"session.thread_status_terminated"SessionThreadStatusTerminated`

  - `class BetaManagedAgentsUserToolResultEvent:`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `required string ID`

      Unique identifier for this event.

    - `required string ToolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

      - `"user.tool_result"UserToolResult`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Boolean? IsError`

      Whether the tool execution resulted in an error.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

    - `string? SessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that is retrying.

    - `required Type Type`

      - `"session.thread_status_rescheduled"SessionThreadStatusRescheduled`

  - `class BetaManagedAgentsSessionUpdatedEvent:`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.updated"SessionUpdated`

    - `BetaManagedAgentsSessionAgent? Agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `required string ID`

      - `required string? Description`

      - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

        - `required string Name`

        - `required Type Type`

          - `"url"Url`

        - `required string Url`

      - `required BetaManagedAgentsModelConfig Model`

        Model identifier and configuration.

        - `required BetaManagedAgentsModel ID`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-sonnet-5"ClaudeSonnet5`

            High-performance model for coding and agents

          - `"claude-fable-5"ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-5"ClaudeOpus5`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-8"ClaudeOpus4_8`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-7"ClaudeOpus4_7`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-6"ClaudeOpus4_6`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-6"ClaudeSonnet4_6`

            Best combination of speed and intelligence

          - `"claude-haiku-4-5"ClaudeHaiku4_5`

            Fastest model with near-frontier intelligence

          - `"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001`

            Fastest model with near-frontier intelligence

          - `"claude-opus-4-5"ClaudeOpus4_5`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-5"ClaudeSonnet4_5`

            High-performance model for agents and coding

          - `"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929`

            High-performance model for agents and coding

        - `Effort Effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `required Type Type`

              - `"low"Low`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `required Type Type`

              - `"medium"Medium`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `required Type Type`

              - `"high"High`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `required Type Type`

              - `"xhigh"Xhigh`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `required Type Type`

              - `"max"Max`

        - `string InferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"Standard`

          - `"fast"Fast`

      - `required BetaManagedAgentsSessionMultiagentCoordinator? Multiagent`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `required IReadOnlyList<Agent> Agents`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent:`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `required string ID`

            - `required string? Description`

            - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

              - `required string Name`

              - `required Type Type`

              - `required string Url`

            - `required BetaManagedAgentsModelConfig Model`

              Model identifier and configuration.

            - `required string Name`

            - `required IReadOnlyList<Skill> Skills`

              - `class BetaManagedAgentsAnthropicSkill:`

                A resolved Anthropic-managed skill.

                - `required string SkillID`

                - `required Type Type`

                  - `"anthropic"Anthropic`

                - `required string Version`

              - `class BetaManagedAgentsCustomSkill:`

                A resolved user-created custom skill.

                - `required string SkillID`

                - `required Type Type`

                  - `"custom"Custom`

                - `required string Version`

            - `required string? System`

            - `required IReadOnlyList<Tool> Tools`

              - `class BetaManagedAgentsAgentToolset20260401:`

                - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

                  - `required Boolean Enabled`

                  - `required Name Name`

                    Built-in agent tool identifier.

                    - `"bash"Bash`

                    - `"edit"Edit`

                    - `"read"Read`

                    - `"write"Write`

                    - `"glob"Glob`

                    - `"grep"Grep`

                    - `"web_fetch"WebFetch`

                    - `"web_search"WebSearch`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                      - `required Type Type`

                        - `"always_allow"AlwaysAllow`

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                      - `required Type Type`

                        - `"always_ask"AlwaysAsk`

                - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

                  Resolved default configuration for agent tools.

                  - `required Boolean Enabled`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required Type Type`

                  - `"agent_toolset_20260401"AgentToolset20260401`

              - `class BetaManagedAgentsMcpToolset:`

                - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

                  - `required Boolean Enabled`

                  - `required string Name`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `required Boolean Enabled`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required string McpServerName`

                - `required Type Type`

                  - `"mcp_toolset"McpToolset`

              - `class BetaManagedAgentsCustomTool:`

                A custom tool as returned in API responses.

                - `required string Description`

                - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

                  JSON Schema for custom tool input parameters.

                  - `JsonElement Type "object"constant`

                  - `IReadOnlyDictionary<string, JsonElement>? Properties`

                  - `IReadOnlyList<string>? Required`

                - `required string Name`

                - `required Type Type`

                  - `"custom"Custom`

            - `required Type Type`

              - `"agent"Agent`

            - `required Int Version`

          - `class BetaManagedAgentsAdvisor:`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `required string Model`

              The advisor model id.

            - `required Type Type`

              - `"advisor"Advisor`

        - `required Type Type`

          - `"coordinator"Coordinator`

      - `required string Name`

      - `required IReadOnlyList<Skill> Skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

      - `required string? System`

      - `required IReadOnlyList<Tool> Tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

        - `class BetaManagedAgentsMcpToolset:`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

      - `required Type Type`

        - `"agent"Agent`

      - `required Int Version`

    - `BetaManagedAgentsBudgetLimit? Budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `required BetaMonetaryAmount MaxListCost`

        A monetary amount in a specific currency.

        - `required string Amount`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `required BetaCurrency Currency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

          - `"USD"Usd`

      - `required Type Type`

        - `"limit"Limit`

    - `IReadOnlyDictionary<string, string> Metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `string? Title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent:`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `required BetaManagedAgentsStartEventPreview Event`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview:`

        - `required string ID`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `required Type Type`

          - `"agent.message"AgentMessage`

      - `class BetaManagedAgentsAgentThinkingPreview:`

        - `required string ID`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `required Type Type`

          - `"agent.thinking"AgentThinking`

    - `required Type Type`

      - `"event_start"EventStart`

  - `class BetaManagedAgentsDeltaEvent:`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `required BetaManagedAgentsDeltaContent Delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `required BetaManagedAgentsTextBlock Content`

        Regular text content.

      - `required Type Type`

        - `"content_delta"ContentDelta`

      - `Long Index`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    - `required string EventID`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `required Type Type`

      - `"event_delta"EventDelta`

  - `class BetaManagedAgentsSystemMessageEvent:`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

      System content blocks. Text-only.

      - `required string Text`

        The text content.

      - `required Type Type`

        - `"text"Text`

    - `required Type Type`

      - `"system.message"SystemMessage`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsSessionUsageEvent:`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.usage"SessionUsage`

    - `required BetaManagedAgentsSessionUsageSnapshot Usage`

      Point-in-time snapshot of a session's cumulative usage.

      - `Double ActiveSeconds`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

      - `BetaManagedAgentsCacheCreationUsage CacheCreation`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `Int Ephemeral1hInputTokens`

          Tokens used to create 1-hour ephemeral cache entries.

        - `Int Ephemeral5mInputTokens`

          Tokens used to create 5-minute ephemeral cache entries.

      - `Int CacheReadInputTokens`

        Total tokens read from prompt cache.

      - `Int InputTokens`

        Total input tokens consumed across all turns.

      - `BetaMonetaryAmount ListCost`

        A monetary amount in a specific currency.

      - `Int OutputTokens`

        Total output tokens generated across all turns.

      - `BetaManagedAgentsServerToolUsage ServerToolUse`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `Int WebFetchRequests`

          Number of server-executed web fetch requests.

        - `Int WebSearchRequests`

          Number of server-executed web search requests.

    - `BetaManagedAgentsBudgetLimit? Budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

### Example

```csharp
EventStreamParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ThreadID = "sthr_011CZkZVWa6oIjw0rgXZpnBt",
};

await foreach (var betaManagedAgentsStreamSessionThreadEvents in client.Beta.Sessions.Threads.Events.StreamStreaming(parameters))
{
    Console.WriteLine(betaManagedAgentsStreamSessionThreadEvents);
}
```

#### Response

```json
{
  "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
  "content": [
    {
      "text": "Where is my order #1234?",
      "type": "text"
    }
  ],
  "type": "user.message",
  "processed_at": "2026-03-15T10:00:00Z"
}
```

# Deployments

## Create Deployment

`BetaManagedAgentsDeployment Beta.Deployments.Create(DeploymentCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/deployments`

Create Deployment

### Parameters

- `DeploymentCreateParams parameters`

  - `required Agent agent`

    Body param: Agent to deploy. Accepts the `agent` ID string, which pins the latest version, or an `agent` object with both id and version specified. The agent must exist and not be archived.

    - `string`

    - `class BetaManagedAgentsAgentParams:`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `required string ID`

        The `agent` ID.

      - `required Type Type`

        - `"agent"Agent`

      - `Int Version`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

  - `required string environmentID`

    Body param: ID of the `environment` defining the container configuration for sessions created from this deployment.

  - `required IReadOnlyList<BetaManagedAgentsDeploymentInitialEventParams> initialEvents`

    Body param: Events to send to each session immediately after creation. At least 1, maximum 50.

    - `class BetaManagedAgentsUserMessageEventParams:`

      Parameters for sending a user message to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

            - `"redacted"Redacted`

      - `required Type Type`

        - `"user.message"UserMessage`

    - `class BetaManagedAgentsUserDefineOutcomeEventParams:`

      Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubricParams:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

            - `"file"File`

        - `class BetaManagedAgentsTextRubricParams:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          - `required Type Type`

            - `"text"Text`

      - `required Type Type`

        - `"user.define_outcome"UserDefineOutcome`

      - `Int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsSystemMessageEventParams:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `required Type Type`

        - `"system.message"SystemMessage`

  - `required string name`

    Body param: Human-readable name for the deployment.

  - `BetaManagedAgentsBudgetLimit? budget`

    Body param: A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `string? description`

    Body param: Description of what the deployment does.

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `IReadOnlyList<Resource> resources`

    Body param: Resources (e.g. repositories, files) to mount into each session's container. Maximum 500.

    - `class BetaManagedAgentsGitHubRepositoryResourceParams:`

      Mount a GitHub repository into the session's container.

      - `required string AuthorizationToken`

        GitHub authorization token used to clone the repository.

      - `required Type Type`

        - `"github_repository"GitHubRepository`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

          - `required Type Type`

            - `"branch"Branch`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

          - `required Type Type`

            - `"commit"Commit`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceParams:`

      Mount a file uploaded via the Files API into the session.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

        - `"file"File`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceParam:`

      Parameters for attaching a memory store to an agent session.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

        - `"memory_store"MemoryStore`

      - `Access? Access`

        Access mode for an attached memory store.

        - `"read_write"ReadWrite`

        - `"read_only"ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `BetaManagedAgentsScheduleParams? schedule`

    Body param: 5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `IReadOnlyList<string> vaultIds`

    Body param: Vault IDs for stored credentials the agent can use during sessions created from this deployment. Maximum 50.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? Description`

    Description of what the deployment does.

  - `required string EnvironmentID`

    ID of the `environment` where sessions run.

  - `required IReadOnlyList<BetaManagedAgentsDeploymentInitialEvent> InitialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

            - `"redacted"Redacted`

      - `required Type Type`

        - `"user.message"UserMessage`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

            - `"file"File`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

            - `"text"Text`

      - `required Type Type`

        - `"user.define_outcome"UserDefineOutcome`

      - `Int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `required Type Type`

        - `"system.message"SystemMessage`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

        - `"manual"Manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

            - `"environment_archived_error"EnvironmentArchivedError`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

            - `"agent_archived_error"AgentArchivedError`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

            - `"environment_not_found_error"EnvironmentNotFoundError`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

            - `"vault_not_found_error"VaultNotFoundError`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

            - `"file_not_found_error"FileNotFoundError`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

            - `"session_resource_not_found_error"SessionResourceNotFoundError`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

            - `"workspace_archived_error"WorkspaceArchivedError`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

            - `"organization_disabled_error"OrganizationDisabledError`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

            - `"memory_store_archived_error"MemoryStoreArchivedError`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

            - `"skill_not_found_error"SkillNotFoundError`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

            - `"vault_archived_error"VaultArchivedError`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

            - `"unknown_error"UnknownError`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

            - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

            - `"mcp_egress_blocked_error"McpEgressBlockedError`

      - `required Type Type`

        - `"error"Error`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

        - `"github_repository"GitHubRepository`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

          - `required Type Type`

            - `"branch"Branch`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

          - `required Type Type`

            - `"commit"Commit`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

        - `"file"File`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

        - `"memory_store"MemoryStore`

      - `Access? Access`

        Access mode for an attached memory store.

        - `"read_write"ReadWrite`

        - `"read_only"ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `required Type Type`

      - `"cron"Cron`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `"active"Active`

    - `"paused"Paused`

  - `required Type Type`

    - `"deployment"Deployment`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `BetaManagedAgentsBudgetLimit? Budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `required BetaMonetaryAmount MaxListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

        - `"USD"Usd`

    - `required Type Type`

      - `"limit"Limit`

### Example

```csharp
DeploymentCreateParams parameters = new()
{
    Agent = "string",
    EnvironmentID = "x",
    InitialEvents =
    [
        new BetaManagedAgentsUserMessageEventParams()
        {
            Content =
            [
                new BetaManagedAgentsTextBlock()
                {
                    Text = "Where is my order #1234?",
                    Type = Type.Text,
                },
            ],
            Type = Type.UserMessage,
        },
    ],
    Name = "x",
};

var betaManagedAgentsDeployment = await client.Beta.Deployments.Create(parameters);

Console.WriteLine(betaManagedAgentsDeployment);
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  }
}
```

## List Deployments

`DeploymentListPageResponse Beta.Deployments.List(DeploymentListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/deployments`

List Deployments

### Parameters

- `DeploymentListParams parameters`

  - `string agentID`

    Query param: Filter by agent ID.

  - `DateTimeOffset createdAtGte`

    Query param: Return deployments created at or after this time (inclusive).

  - `DateTimeOffset createdAtLte`

    Query param: Return deployments created at or before this time (inclusive).

  - `Boolean includeArchived`

    Query param: When true, includes archived deployments. Default: false (exclude archived).

  - `Int limit`

    Query param: Maximum results per page. Default 20, maximum 100.

  - `string page`

    Query param: Opaque pagination cursor.

  - `BetaManagedAgentsDeploymentStatus status`

    Query param: Filter by status: active or paused. Omit for both. To include archived deployments, use include_archived instead; the two cannot be combined.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class DeploymentListPageResponse:`

  Paginated list of deployments.

  - `required IReadOnlyList<BetaManagedAgentsDeployment> Data`

    List of deployments.

    - `required string ID`

      Unique identifier for this deployment.

    - `required BetaManagedAgentsAgentReference Agent`

      A resolved agent reference with a concrete version.

      - `required string ID`

      - `required Type Type`

        - `"agent"Agent`

      - `required Int Version`

    - `required DateTimeOffset? ArchivedAt`

      A timestamp in RFC 3339 format

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required string? Description`

      Description of what the deployment does.

    - `required string EnvironmentID`

      ID of the `environment` where sessions run.

    - `required IReadOnlyList<BetaManagedAgentsDeploymentInitialEvent> InitialEvents`

      Events sent to each session immediately after creation.

      - `class BetaManagedAgentsDeploymentUserMessageEvent:`

        A user message sent to the session.

        - `required IReadOnlyList<Content> Content`

          Array of content blocks for the user message.

          - `class BetaManagedAgentsTextBlock:`

            Regular text content.

            - `required string Text`

              The text content.

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsImageBlock:`

            Image content specified directly as base64 data or as a reference via a URL.

            - `required Source Source`

              Union type for image source variants.

              - `class BetaManagedAgentsBase64ImageSource:`

                Base64-encoded image data.

                - `required string Data`

                  Base64-encoded image data.

                - `required string MediaType`

                  MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                - `required Type Type`

                  - `"base64"Base64`

              - `class BetaManagedAgentsUrlImageSource:`

                Image referenced by URL.

                - `required Type Type`

                  - `"url"Url`

                - `required string Url`

                  URL of the image to fetch.

              - `class BetaManagedAgentsFileImageSource:`

                Image referenced by file ID.

                - `required string FileID`

                  ID of a previously uploaded file.

                - `required Type Type`

                  - `"file"File`

            - `required Type Type`

              - `"image"Image`

          - `class BetaManagedAgentsDocumentBlock:`

            Document content, either specified directly as base64 data, as text, or as a reference via a URL.

            - `required Source Source`

              Union type for document source variants.

              - `class BetaManagedAgentsBase64DocumentSource:`

                Base64-encoded document data.

                - `required string Data`

                  Base64-encoded document data.

                - `required string MediaType`

                  MIME type of the document (e.g., "application/pdf").

                - `required Type Type`

                  - `"base64"Base64`

              - `class BetaManagedAgentsPlainTextDocumentSource:`

                Plain text document content.

                - `required string Data`

                  The plain text content.

                - `required MediaType MediaType`

                  MIME type of the text content. Must be "text/plain".

                  - `"text/plain"TextPlain`

                - `required Type Type`

                  - `"text"Text`

              - `class BetaManagedAgentsUrlDocumentSource:`

                Document referenced by URL.

                - `required Type Type`

                  - `"url"Url`

                - `required string Url`

                  URL of the document to fetch.

              - `class BetaManagedAgentsFileDocumentSource:`

                Document referenced by file ID.

                - `required string FileID`

                  ID of a previously uploaded file.

                - `required Type Type`

                  - `"file"File`

            - `required Type Type`

              - `"document"Document`

            - `string? Context`

              Additional context about the document for the model.

            - `string? Title`

              The title of the document.

          - `class BetaManagedAgentsRedactedBlock:`

            Placeholder for content withheld by Anthropic model policy.

            - `required Type Type`

              - `"redacted"Redacted`

        - `required Type Type`

          - `"user.message"UserMessage`

      - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

        An outcome the agent should work toward. The agent begins work on receipt.

        - `required string Description`

          What the agent should produce. This is the task specification.

        - `required Rubric Rubric`

          Rubric for grading the quality of an outcome.

          - `class BetaManagedAgentsFileRubric:`

            Rubric referenced by a file uploaded via the Files API.

            - `required string FileID`

              ID of the rubric file.

            - `required Type Type`

              - `"file"File`

          - `class BetaManagedAgentsTextRubric:`

            Rubric content provided inline as text.

            - `required string Content`

              Rubric content. Plain text or markdown — the grader treats it as freeform text.

            - `required Type Type`

              - `"text"Text`

        - `required Type Type`

          - `"user.define_outcome"UserDefineOutcome`

        - `Int? MaxIterations`

          Eval→revision cycles before giving up. Default 3, max 20.

      - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

        Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

        - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

          System content blocks to append. Text-only.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `required Type Type`

          - `"system.message"SystemMessage`

    - `required IReadOnlyDictionary<string, string> Metadata`

      Arbitrary key-value metadata. Maximum 16 pairs.

    - `required string Name`

      Human-readable name.

    - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

      Why a deployment is paused. Non-null exactly when `status` is `paused`.

      - `class BetaManagedAgentsManualDeploymentPausedReason:`

        The caller invoked the pause endpoint on the deployment.

        - `required Type Type`

          - `"manual"Manual`

      - `class BetaManagedAgentsErrorDeploymentPausedReason:`

        A scheduled fire recorded a failed run whose error auto-pauses the deployment.

        - `required BetaManagedAgentsDeploymentPausedReasonError Error`

          The error that triggered an auto-pause. Matches the failed run's `error.type`.

          - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

            The deployment's environment was archived.

            - `required Type Type`

              - `"environment_archived_error"EnvironmentArchivedError`

          - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

            The deployment's agent was archived.

            - `required Type Type`

              - `"agent_archived_error"AgentArchivedError`

          - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

            The deployment's environment no longer exists.

            - `required Type Type`

              - `"environment_not_found_error"EnvironmentNotFoundError`

          - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

            A vault referenced by the deployment no longer exists.

            - `required Type Type`

              - `"vault_not_found_error"VaultNotFoundError`

          - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

            A file resource referenced by the deployment no longer exists.

            - `required Type Type`

              - `"file_not_found_error"FileNotFoundError`

          - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

            A referenced resource no longer exists and its kind was not reported.

            - `required Type Type`

              - `"session_resource_not_found_error"SessionResourceNotFoundError`

          - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

            The deployment's workspace was archived.

            - `required Type Type`

              - `"workspace_archived_error"WorkspaceArchivedError`

          - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

            The deployment's organization is disabled.

            - `required Type Type`

              - `"organization_disabled_error"OrganizationDisabledError`

          - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

            A memory store referenced by the deployment is archived.

            - `required Type Type`

              - `"memory_store_archived_error"MemoryStoreArchivedError`

          - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

            A skill referenced by the deployment's agent no longer exists.

            - `required Type Type`

              - `"skill_not_found_error"SkillNotFoundError`

          - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

            A vault referenced by the deployment is archived.

            - `required Type Type`

              - `"vault_archived_error"VaultArchivedError`

          - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

            An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

            - `required Type Type`

              - `"unknown_error"UnknownError`

          - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

            The deployment configures resources, but its environment is self-hosted and cannot mount them.

            - `required Type Type`

              - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

          - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

            An MCP server host used by the deployment's agent is blocked by the environment's network policy.

            - `required Type Type`

              - `"mcp_egress_blocked_error"McpEgressBlockedError`

        - `required Type Type`

          - `"error"Error`

    - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

      Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

      - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

        A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

        - `required Type Type`

          - `"github_repository"GitHubRepository`

        - `required string Url`

          Github URL of the repository

        - `Checkout? Checkout`

          Branch or commit to check out. Defaults to the repository's default branch.

          - `class BetaManagedAgentsBranchCheckout:`

            - `required string Name`

              Branch name to check out.

            - `required Type Type`

              - `"branch"Branch`

          - `class BetaManagedAgentsCommitCheckout:`

            - `required string Sha`

              Full commit SHA to check out.

            - `required Type Type`

              - `"commit"Commit`

        - `string? MountPath`

          Mount path in the container. Defaults to `/workspace/<repo-name>`.

      - `class BetaManagedAgentsFileResourceConfig:`

        A file mounted into each session's container.

        - `required string FileID`

          ID of a previously uploaded file.

        - `required Type Type`

          - `"file"File`

        - `string? MountPath`

          Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

      - `class BetaManagedAgentsMemoryStoreResourceConfig:`

        A memory store attached to each session created from this deployment.

        - `required string MemoryStoreID`

          The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

        - `required Type Type`

          - `"memory_store"MemoryStore`

        - `Access? Access`

          Access mode for an attached memory store.

          - `"read_write"ReadWrite`

          - `"read_only"ReadOnly`

        - `string? Instructions`

          Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `required BetaManagedAgentsSchedule? Schedule`

      5-field POSIX cron schedule with computed runtime timestamps.

      - `required string Expression`

        5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      - `required string Timezone`

        IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      - `required Type Type`

        - `"cron"Cron`

      - `DateTimeOffset? LastRunAt`

        A timestamp in RFC 3339 format

      - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

        Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

    - `required BetaManagedAgentsDeploymentStatus Status`

      Lifecycle status of a deployment.

      - `"active"Active`

      - `"paused"Paused`

    - `required Type Type`

      - `"deployment"Deployment`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

    - `required IReadOnlyList<string> VaultIds`

      Vault IDs supplying stored credentials for sessions created from this deployment.

    - `BetaManagedAgentsBudgetLimit? Budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `required BetaMonetaryAmount MaxListCost`

        A monetary amount in a specific currency.

        - `required string Amount`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `required BetaCurrency Currency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

          - `"USD"Usd`

      - `required Type Type`

        - `"limit"Limit`

  - `string? NextPage`

    Opaque cursor for the next page. Null when no more results.

### Example

```csharp
DeploymentListParams parameters = new();

var page = await client.Beta.Deployments.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
      "agent": {
        "id": "agent_011CZkYpogX7uDKUyvBTophP",
        "type": "agent",
        "version": 1
      },
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "description": "Compiles yesterday's orders into a report every weekday morning.",
      "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
      "initial_events": [
        {
          "content": [
            {
              "text": "Compile yesterday's orders into report.md.",
              "type": "text"
            }
          ],
          "type": "user.message"
        }
      ],
      "metadata": {},
      "name": "Daily order report",
      "paused_reason": {
        "type": "manual"
      },
      "resources": [
        {
          "type": "github_repository",
          "url": "url",
          "checkout": {
            "name": "main",
            "type": "branch"
          },
          "mount_path": "mount_path"
        }
      ],
      "schedule": {
        "expression": "0 9 * * 1-5",
        "timezone": "America/Los_Angeles",
        "type": "cron",
        "last_run_at": "2026-03-16T16:00:09Z",
        "upcoming_runs_at": [
          "2026-03-17T16:00:00Z",
          "2026-03-18T16:00:00Z"
        ]
      },
      "status": "active",
      "type": "deployment",
      "updated_at": "2026-03-15T10:00:00Z",
      "vault_ids": [
        "vlt_011CZkZDLs7fYzm1hXNPeRjv"
      ],
      "budget": {
        "max_list_cost": {
          "amount": "2500",
          "currency": "USD"
        },
        "type": "limit"
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Deployment

`BetaManagedAgentsDeployment Beta.Deployments.Retrieve(DeploymentRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/deployments/{deployment_id}`

Get Deployment

### Parameters

- `DeploymentRetrieveParams parameters`

  - `required string deploymentID`

    Path parameter deployment_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? Description`

    Description of what the deployment does.

  - `required string EnvironmentID`

    ID of the `environment` where sessions run.

  - `required IReadOnlyList<BetaManagedAgentsDeploymentInitialEvent> InitialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

            - `"redacted"Redacted`

      - `required Type Type`

        - `"user.message"UserMessage`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

            - `"file"File`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

            - `"text"Text`

      - `required Type Type`

        - `"user.define_outcome"UserDefineOutcome`

      - `Int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `required Type Type`

        - `"system.message"SystemMessage`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

        - `"manual"Manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

            - `"environment_archived_error"EnvironmentArchivedError`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

            - `"agent_archived_error"AgentArchivedError`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

            - `"environment_not_found_error"EnvironmentNotFoundError`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

            - `"vault_not_found_error"VaultNotFoundError`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

            - `"file_not_found_error"FileNotFoundError`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

            - `"session_resource_not_found_error"SessionResourceNotFoundError`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

            - `"workspace_archived_error"WorkspaceArchivedError`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

            - `"organization_disabled_error"OrganizationDisabledError`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

            - `"memory_store_archived_error"MemoryStoreArchivedError`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

            - `"skill_not_found_error"SkillNotFoundError`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

            - `"vault_archived_error"VaultArchivedError`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

            - `"unknown_error"UnknownError`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

            - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

            - `"mcp_egress_blocked_error"McpEgressBlockedError`

      - `required Type Type`

        - `"error"Error`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

        - `"github_repository"GitHubRepository`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

          - `required Type Type`

            - `"branch"Branch`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

          - `required Type Type`

            - `"commit"Commit`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

        - `"file"File`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

        - `"memory_store"MemoryStore`

      - `Access? Access`

        Access mode for an attached memory store.

        - `"read_write"ReadWrite`

        - `"read_only"ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `required Type Type`

      - `"cron"Cron`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `"active"Active`

    - `"paused"Paused`

  - `required Type Type`

    - `"deployment"Deployment`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `BetaManagedAgentsBudgetLimit? Budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `required BetaMonetaryAmount MaxListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

        - `"USD"Usd`

    - `required Type Type`

      - `"limit"Limit`

### Example

```csharp
DeploymentRetrieveParams parameters = new()
{
    DeploymentID = "depl_011CZkZcDH3vPqd7xnEfwTai"
};

var betaManagedAgentsDeployment = await client.Beta.Deployments.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsDeployment);
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  }
}
```

## Update Deployment

`BetaManagedAgentsDeployment Beta.Deployments.Update(DeploymentUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/deployments/{deployment_id}`

Update Deployment

### Parameters

- `DeploymentUpdateParams parameters`

  - `required string deploymentID`

    Path param: Path parameter deployment_id

  - `Agent agent`

    Body param: Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared.

    - `string`

    - `class BetaManagedAgentsAgentParams:`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `required string ID`

        The `agent` ID.

      - `required Type Type`

        - `"agent"Agent`

      - `Int Version`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

  - `BetaManagedAgentsBudgetLimit? budget`

    Body param: A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `string? description`

    Body param: Description. Omit to preserve; send empty string or null to clear.

  - `string environmentID`

    Body param: ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.

  - `IReadOnlyList<BetaManagedAgentsDeploymentInitialEventParams> initialEvents`

    Body param: Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50.

    - `class BetaManagedAgentsUserMessageEventParams:`

      Parameters for sending a user message to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

            - `"redacted"Redacted`

      - `required Type Type`

        - `"user.message"UserMessage`

    - `class BetaManagedAgentsUserDefineOutcomeEventParams:`

      Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubricParams:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

            - `"file"File`

        - `class BetaManagedAgentsTextRubricParams:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          - `required Type Type`

            - `"text"Text`

      - `required Type Type`

        - `"user.define_outcome"UserDefineOutcome`

      - `Int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsSystemMessageEventParams:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `required Type Type`

        - `"system.message"SystemMessage`

  - `IReadOnlyDictionary<string, string>? metadata`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `string name`

    Body param: Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

  - `IReadOnlyList<Resource>? resources`

    Body param: Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.

    - `class BetaManagedAgentsGitHubRepositoryResourceParams:`

      Mount a GitHub repository into the session's container.

      - `required string AuthorizationToken`

        GitHub authorization token used to clone the repository.

      - `required Type Type`

        - `"github_repository"GitHubRepository`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

          - `required Type Type`

            - `"branch"Branch`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

          - `required Type Type`

            - `"commit"Commit`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceParams:`

      Mount a file uploaded via the Files API into the session.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

        - `"file"File`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceParam:`

      Parameters for attaching a memory store to an agent session.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

        - `"memory_store"MemoryStore`

      - `Access? Access`

        Access mode for an attached memory store.

        - `"read_write"ReadWrite`

        - `"read_only"ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `BetaManagedAgentsScheduleParams? schedule`

    Body param: 5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `IReadOnlyList<string>? vaultIds`

    Body param: Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? Description`

    Description of what the deployment does.

  - `required string EnvironmentID`

    ID of the `environment` where sessions run.

  - `required IReadOnlyList<BetaManagedAgentsDeploymentInitialEvent> InitialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

            - `"redacted"Redacted`

      - `required Type Type`

        - `"user.message"UserMessage`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

            - `"file"File`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

            - `"text"Text`

      - `required Type Type`

        - `"user.define_outcome"UserDefineOutcome`

      - `Int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `required Type Type`

        - `"system.message"SystemMessage`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

        - `"manual"Manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

            - `"environment_archived_error"EnvironmentArchivedError`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

            - `"agent_archived_error"AgentArchivedError`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

            - `"environment_not_found_error"EnvironmentNotFoundError`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

            - `"vault_not_found_error"VaultNotFoundError`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

            - `"file_not_found_error"FileNotFoundError`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

            - `"session_resource_not_found_error"SessionResourceNotFoundError`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

            - `"workspace_archived_error"WorkspaceArchivedError`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

            - `"organization_disabled_error"OrganizationDisabledError`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

            - `"memory_store_archived_error"MemoryStoreArchivedError`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

            - `"skill_not_found_error"SkillNotFoundError`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

            - `"vault_archived_error"VaultArchivedError`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

            - `"unknown_error"UnknownError`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

            - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

            - `"mcp_egress_blocked_error"McpEgressBlockedError`

      - `required Type Type`

        - `"error"Error`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

        - `"github_repository"GitHubRepository`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

          - `required Type Type`

            - `"branch"Branch`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

          - `required Type Type`

            - `"commit"Commit`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

        - `"file"File`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

        - `"memory_store"MemoryStore`

      - `Access? Access`

        Access mode for an attached memory store.

        - `"read_write"ReadWrite`

        - `"read_only"ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `required Type Type`

      - `"cron"Cron`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `"active"Active`

    - `"paused"Paused`

  - `required Type Type`

    - `"deployment"Deployment`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `BetaManagedAgentsBudgetLimit? Budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `required BetaMonetaryAmount MaxListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

        - `"USD"Usd`

    - `required Type Type`

      - `"limit"Limit`

### Example

```csharp
DeploymentUpdateParams parameters = new()
{
    DeploymentID = "depl_011CZkZcDH3vPqd7xnEfwTai"
};

var betaManagedAgentsDeployment = await client.Beta.Deployments.Update(parameters);

Console.WriteLine(betaManagedAgentsDeployment);
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  }
}
```

## Archive Deployment

`BetaManagedAgentsDeployment Beta.Deployments.Archive(DeploymentArchiveParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/deployments/{deployment_id}/archive`

Archive Deployment

### Parameters

- `DeploymentArchiveParams parameters`

  - `required string deploymentID`

    Path parameter deployment_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? Description`

    Description of what the deployment does.

  - `required string EnvironmentID`

    ID of the `environment` where sessions run.

  - `required IReadOnlyList<BetaManagedAgentsDeploymentInitialEvent> InitialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

            - `"redacted"Redacted`

      - `required Type Type`

        - `"user.message"UserMessage`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

            - `"file"File`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

            - `"text"Text`

      - `required Type Type`

        - `"user.define_outcome"UserDefineOutcome`

      - `Int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `required Type Type`

        - `"system.message"SystemMessage`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

        - `"manual"Manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

            - `"environment_archived_error"EnvironmentArchivedError`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

            - `"agent_archived_error"AgentArchivedError`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

            - `"environment_not_found_error"EnvironmentNotFoundError`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

            - `"vault_not_found_error"VaultNotFoundError`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

            - `"file_not_found_error"FileNotFoundError`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

            - `"session_resource_not_found_error"SessionResourceNotFoundError`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

            - `"workspace_archived_error"WorkspaceArchivedError`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

            - `"organization_disabled_error"OrganizationDisabledError`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

            - `"memory_store_archived_error"MemoryStoreArchivedError`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

            - `"skill_not_found_error"SkillNotFoundError`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

            - `"vault_archived_error"VaultArchivedError`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

            - `"unknown_error"UnknownError`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

            - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

            - `"mcp_egress_blocked_error"McpEgressBlockedError`

      - `required Type Type`

        - `"error"Error`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

        - `"github_repository"GitHubRepository`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

          - `required Type Type`

            - `"branch"Branch`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

          - `required Type Type`

            - `"commit"Commit`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

        - `"file"File`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

        - `"memory_store"MemoryStore`

      - `Access? Access`

        Access mode for an attached memory store.

        - `"read_write"ReadWrite`

        - `"read_only"ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `required Type Type`

      - `"cron"Cron`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `"active"Active`

    - `"paused"Paused`

  - `required Type Type`

    - `"deployment"Deployment`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `BetaManagedAgentsBudgetLimit? Budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `required BetaMonetaryAmount MaxListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

        - `"USD"Usd`

    - `required Type Type`

      - `"limit"Limit`

### Example

```csharp
DeploymentArchiveParams parameters = new()
{
    DeploymentID = "depl_011CZkZcDH3vPqd7xnEfwTai"
};

var betaManagedAgentsDeployment = await client.Beta.Deployments.Archive(parameters);

Console.WriteLine(betaManagedAgentsDeployment);
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  }
}
```

## Run Deployment Now

`BetaManagedAgentsDeploymentRun Beta.Deployments.Run(DeploymentRunParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/deployments/{deployment_id}/run`

Run Deployment Now

### Parameters

- `DeploymentRunParams parameters`

  - `required string deploymentID`

    Path parameter deployment_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsDeploymentRun:`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `required string ID`

    Unique identifier for this run (`drun_...`).

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string DeploymentID`

    ID of the deployment that produced this run.

  - `required Error? Error`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `class BetaManagedAgentsEnvironmentArchivedRunError:`

      The deployment's environment was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"environment_archived_error"EnvironmentArchivedError`

    - `class BetaManagedAgentsAgentArchivedRunError:`

      The deployment's agent was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"agent_archived_error"AgentArchivedError`

    - `class BetaManagedAgentsEnvironmentNotFoundRunError:`

      The deployment's environment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"environment_not_found_error"EnvironmentNotFoundError`

    - `class BetaManagedAgentsVaultNotFoundRunError:`

      A vault referenced by the deployment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"vault_not_found_error"VaultNotFoundError`

    - `class BetaManagedAgentsVaultArchivedRunError:`

      A vault referenced by the deployment is archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"vault_archived_error"VaultArchivedError`

    - `class BetaManagedAgentsFileNotFoundRunError:`

      A file resource referenced by the deployment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"file_not_found_error"FileNotFoundError`

    - `class BetaManagedAgentsMemoryStoreArchivedRunError:`

      A memory store referenced by the deployment is archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"memory_store_archived_error"MemoryStoreArchivedError`

    - `class BetaManagedAgentsSkillNotFoundRunError:`

      A skill referenced by the deployment's agent no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"skill_not_found_error"SkillNotFoundError`

    - `class BetaManagedAgentsSessionResourceNotFoundRunError:`

      A referenced resource no longer exists and its kind was not reported.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"session_resource_not_found_error"SessionResourceNotFoundError`

    - `class BetaManagedAgentsWorkspaceArchivedRunError:`

      The deployment's workspace was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"workspace_archived_error"WorkspaceArchivedError`

    - `class BetaManagedAgentsOrganizationDisabledRunError:`

      The deployment's organization is disabled.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"organization_disabled_error"OrganizationDisabledError`

    - `class BetaManagedAgentsSessionRateLimitedRunError:`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"session_rate_limited_error"SessionRateLimitedError`

    - `class BetaManagedAgentsSessionCreationRejectedRunError:`

      The session create request was rejected with a non-retryable validation error.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"session_creation_rejected_error"SessionCreationRejectedError`

    - `class BetaManagedAgentsUnknownRunError:`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"unknown_error"UnknownError`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

    - `class BetaManagedAgentsMcpEgressBlockedRunError:`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"mcp_egress_blocked_error"McpEgressBlockedError`

  - `required string? SessionID`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `required BetaManagedAgentsTriggerContext TriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext:`

      The run was fired by the deployment's cron schedule.

      - `required DateTimeOffset ScheduledAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"schedule"Schedule`

    - `class BetaManagedAgentsManualTriggerContext:`

      The run was started manually by creating a session directly against the deployment.

      - `required Type Type`

        - `"manual"Manual`

  - `required Type Type`

    - `"deployment_run"DeploymentRun`

### Example

```csharp
DeploymentRunParams parameters = new()
{
    DeploymentID = "depl_011CZkZcDH3vPqd7xnEfwTai"
};

var betaManagedAgentsDeploymentRun = await client.Beta.Deployments.Run(parameters);

Console.WriteLine(betaManagedAgentsDeploymentRun);
```

#### Response

```json
{
  "id": "id",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "type": "agent",
    "version": 1
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "deployment_id": "deployment_id",
  "error": {
    "message": "message",
    "type": "environment_archived_error"
  },
  "session_id": "session_id",
  "trigger_context": {
    "scheduled_at": "2019-12-27T18:11:19.117Z",
    "type": "schedule"
  },
  "type": "deployment_run"
}
```

## Pause Deployment

`BetaManagedAgentsDeployment Beta.Deployments.Pause(DeploymentPauseParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/deployments/{deployment_id}/pause`

Pause Deployment

### Parameters

- `DeploymentPauseParams parameters`

  - `required string deploymentID`

    Path parameter deployment_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? Description`

    Description of what the deployment does.

  - `required string EnvironmentID`

    ID of the `environment` where sessions run.

  - `required IReadOnlyList<BetaManagedAgentsDeploymentInitialEvent> InitialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

            - `"redacted"Redacted`

      - `required Type Type`

        - `"user.message"UserMessage`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

            - `"file"File`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

            - `"text"Text`

      - `required Type Type`

        - `"user.define_outcome"UserDefineOutcome`

      - `Int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `required Type Type`

        - `"system.message"SystemMessage`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

        - `"manual"Manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

            - `"environment_archived_error"EnvironmentArchivedError`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

            - `"agent_archived_error"AgentArchivedError`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

            - `"environment_not_found_error"EnvironmentNotFoundError`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

            - `"vault_not_found_error"VaultNotFoundError`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

            - `"file_not_found_error"FileNotFoundError`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

            - `"session_resource_not_found_error"SessionResourceNotFoundError`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

            - `"workspace_archived_error"WorkspaceArchivedError`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

            - `"organization_disabled_error"OrganizationDisabledError`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

            - `"memory_store_archived_error"MemoryStoreArchivedError`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

            - `"skill_not_found_error"SkillNotFoundError`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

            - `"vault_archived_error"VaultArchivedError`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

            - `"unknown_error"UnknownError`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

            - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

            - `"mcp_egress_blocked_error"McpEgressBlockedError`

      - `required Type Type`

        - `"error"Error`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

        - `"github_repository"GitHubRepository`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

          - `required Type Type`

            - `"branch"Branch`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

          - `required Type Type`

            - `"commit"Commit`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

        - `"file"File`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

        - `"memory_store"MemoryStore`

      - `Access? Access`

        Access mode for an attached memory store.

        - `"read_write"ReadWrite`

        - `"read_only"ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `required Type Type`

      - `"cron"Cron`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `"active"Active`

    - `"paused"Paused`

  - `required Type Type`

    - `"deployment"Deployment`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `BetaManagedAgentsBudgetLimit? Budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `required BetaMonetaryAmount MaxListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

        - `"USD"Usd`

    - `required Type Type`

      - `"limit"Limit`

### Example

```csharp
DeploymentPauseParams parameters = new()
{
    DeploymentID = "depl_011CZkZcDH3vPqd7xnEfwTai"
};

var betaManagedAgentsDeployment = await client.Beta.Deployments.Pause(parameters);

Console.WriteLine(betaManagedAgentsDeployment);
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  }
}
```

## Unpause Deployment

`BetaManagedAgentsDeployment Beta.Deployments.Unpause(DeploymentUnpauseParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/deployments/{deployment_id}/unpause`

Unpause Deployment

### Parameters

- `DeploymentUnpauseParams parameters`

  - `required string deploymentID`

    Path parameter deployment_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? Description`

    Description of what the deployment does.

  - `required string EnvironmentID`

    ID of the `environment` where sessions run.

  - `required IReadOnlyList<BetaManagedAgentsDeploymentInitialEvent> InitialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

            - `"redacted"Redacted`

      - `required Type Type`

        - `"user.message"UserMessage`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

            - `"file"File`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

            - `"text"Text`

      - `required Type Type`

        - `"user.define_outcome"UserDefineOutcome`

      - `Int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `required Type Type`

        - `"system.message"SystemMessage`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

        - `"manual"Manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

            - `"environment_archived_error"EnvironmentArchivedError`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

            - `"agent_archived_error"AgentArchivedError`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

            - `"environment_not_found_error"EnvironmentNotFoundError`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

            - `"vault_not_found_error"VaultNotFoundError`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

            - `"file_not_found_error"FileNotFoundError`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

            - `"session_resource_not_found_error"SessionResourceNotFoundError`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

            - `"workspace_archived_error"WorkspaceArchivedError`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

            - `"organization_disabled_error"OrganizationDisabledError`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

            - `"memory_store_archived_error"MemoryStoreArchivedError`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

            - `"skill_not_found_error"SkillNotFoundError`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

            - `"vault_archived_error"VaultArchivedError`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

            - `"unknown_error"UnknownError`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

            - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

            - `"mcp_egress_blocked_error"McpEgressBlockedError`

      - `required Type Type`

        - `"error"Error`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

        - `"github_repository"GitHubRepository`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

          - `required Type Type`

            - `"branch"Branch`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

          - `required Type Type`

            - `"commit"Commit`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

        - `"file"File`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

        - `"memory_store"MemoryStore`

      - `Access? Access`

        Access mode for an attached memory store.

        - `"read_write"ReadWrite`

        - `"read_only"ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `required Type Type`

      - `"cron"Cron`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `"active"Active`

    - `"paused"Paused`

  - `required Type Type`

    - `"deployment"Deployment`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `BetaManagedAgentsBudgetLimit? Budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `required BetaMonetaryAmount MaxListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

        - `"USD"Usd`

    - `required Type Type`

      - `"limit"Limit`

### Example

```csharp
DeploymentUnpauseParams parameters = new()
{
    DeploymentID = "depl_011CZkZcDH3vPqd7xnEfwTai"
};

var betaManagedAgentsDeployment = await client.Beta.Deployments.Unpause(parameters);

Console.WriteLine(betaManagedAgentsDeployment);
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  }
}
```

## Domain Types

### Beta Managed Agents Agent Archived Deployment Paused Reason Error

- `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

  The deployment's agent was archived.

  - `required Type Type`

    - `"agent_archived_error"AgentArchivedError`

### Beta Managed Agents Cron Schedule

- `class BetaManagedAgentsCronSchedule:`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `required string Expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `required string Timezone`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `required Type Type`

    - `"cron"Cron`

  - `DateTimeOffset? LastRunAt`

    A timestamp in RFC 3339 format

  - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Cron Schedule Params

- `class BetaManagedAgentsCronScheduleParams:`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `required string Expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `required string Timezone`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `required Type Type`

    - `"cron"Cron`

### Beta Managed Agents Deployment

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? Description`

    Description of what the deployment does.

  - `required string EnvironmentID`

    ID of the `environment` where sessions run.

  - `required IReadOnlyList<BetaManagedAgentsDeploymentInitialEvent> InitialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

            - `"redacted"Redacted`

      - `required Type Type`

        - `"user.message"UserMessage`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

            - `"file"File`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

            - `"text"Text`

      - `required Type Type`

        - `"user.define_outcome"UserDefineOutcome`

      - `Int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `required Type Type`

        - `"system.message"SystemMessage`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

        - `"manual"Manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

            - `"environment_archived_error"EnvironmentArchivedError`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

            - `"agent_archived_error"AgentArchivedError`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

            - `"environment_not_found_error"EnvironmentNotFoundError`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

            - `"vault_not_found_error"VaultNotFoundError`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

            - `"file_not_found_error"FileNotFoundError`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

            - `"session_resource_not_found_error"SessionResourceNotFoundError`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

            - `"workspace_archived_error"WorkspaceArchivedError`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

            - `"organization_disabled_error"OrganizationDisabledError`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

            - `"memory_store_archived_error"MemoryStoreArchivedError`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

            - `"skill_not_found_error"SkillNotFoundError`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

            - `"vault_archived_error"VaultArchivedError`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

            - `"unknown_error"UnknownError`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

            - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

            - `"mcp_egress_blocked_error"McpEgressBlockedError`

      - `required Type Type`

        - `"error"Error`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

        - `"github_repository"GitHubRepository`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

          - `required Type Type`

            - `"branch"Branch`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

          - `required Type Type`

            - `"commit"Commit`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

        - `"file"File`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

        - `"memory_store"MemoryStore`

      - `Access? Access`

        Access mode for an attached memory store.

        - `"read_write"ReadWrite`

        - `"read_only"ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `required Type Type`

      - `"cron"Cron`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `"active"Active`

    - `"paused"Paused`

  - `required Type Type`

    - `"deployment"Deployment`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `BetaManagedAgentsBudgetLimit? Budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `required BetaMonetaryAmount MaxListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

        - `"USD"Usd`

    - `required Type Type`

      - `"limit"Limit`

### Beta Managed Agents Deployment Initial Event

- `class BetaManagedAgentsDeploymentInitialEvent: A class that can be one of several variants.union`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `class BetaManagedAgentsDeploymentUserMessageEvent:`

    A user message sent to the session.

    - `required IReadOnlyList<Content> Content`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

        - `required Type Type`

          - `"redacted"Redacted`

    - `required Type Type`

      - `"user.message"UserMessage`

  - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

    An outcome the agent should work toward. The agent begins work on receipt.

    - `required string Description`

      What the agent should produce. This is the task specification.

    - `required Rubric Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `required string FileID`

          ID of the rubric file.

        - `required Type Type`

          - `"file"File`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `required string Content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `required Type Type`

          - `"text"Text`

    - `required Type Type`

      - `"user.define_outcome"UserDefineOutcome`

    - `Int? MaxIterations`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

    - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

      System content blocks to append. Text-only.

      - `required string Text`

        The text content.

      - `required Type Type`

        - `"text"Text`

    - `required Type Type`

      - `"system.message"SystemMessage`

### Beta Managed Agents Deployment Initial Event Params

- `class BetaManagedAgentsDeploymentInitialEventParams: A class that can be one of several variants.union`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `class BetaManagedAgentsUserMessageEventParams:`

    Parameters for sending a user message to the session.

    - `required IReadOnlyList<Content> Content`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

        - `required Type Type`

          - `"redacted"Redacted`

    - `required Type Type`

      - `"user.message"UserMessage`

  - `class BetaManagedAgentsUserDefineOutcomeEventParams:`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `required string Description`

      What the agent should produce. This is the task specification.

    - `required Rubric Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubricParams:`

        Rubric referenced by a file uploaded via the Files API.

        - `required string FileID`

          ID of the rubric file.

        - `required Type Type`

          - `"file"File`

      - `class BetaManagedAgentsTextRubricParams:`

        Rubric content provided inline as text.

        - `required string Content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        - `required Type Type`

          - `"text"Text`

    - `required Type Type`

      - `"user.define_outcome"UserDefineOutcome`

    - `Int? MaxIterations`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `class BetaManagedAgentsSystemMessageEventParams:`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

      System content blocks to append. Text-only.

      - `required string Text`

        The text content.

      - `required Type Type`

        - `"text"Text`

    - `required Type Type`

      - `"system.message"SystemMessage`

### Beta Managed Agents Deployment Paused Reason

- `class BetaManagedAgentsDeploymentPausedReason: A class that can be one of several variants.union`

  Why a deployment is paused. Non-null exactly when `status` is `paused`.

  - `class BetaManagedAgentsManualDeploymentPausedReason:`

    The caller invoked the pause endpoint on the deployment.

    - `required Type Type`

      - `"manual"Manual`

  - `class BetaManagedAgentsErrorDeploymentPausedReason:`

    A scheduled fire recorded a failed run whose error auto-pauses the deployment.

    - `required BetaManagedAgentsDeploymentPausedReasonError Error`

      The error that triggered an auto-pause. Matches the failed run's `error.type`.

      - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

        The deployment's environment was archived.

        - `required Type Type`

          - `"environment_archived_error"EnvironmentArchivedError`

      - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

        The deployment's agent was archived.

        - `required Type Type`

          - `"agent_archived_error"AgentArchivedError`

      - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

        The deployment's environment no longer exists.

        - `required Type Type`

          - `"environment_not_found_error"EnvironmentNotFoundError`

      - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

        A vault referenced by the deployment no longer exists.

        - `required Type Type`

          - `"vault_not_found_error"VaultNotFoundError`

      - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

        A file resource referenced by the deployment no longer exists.

        - `required Type Type`

          - `"file_not_found_error"FileNotFoundError`

      - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

        A referenced resource no longer exists and its kind was not reported.

        - `required Type Type`

          - `"session_resource_not_found_error"SessionResourceNotFoundError`

      - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

        The deployment's workspace was archived.

        - `required Type Type`

          - `"workspace_archived_error"WorkspaceArchivedError`

      - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

        The deployment's organization is disabled.

        - `required Type Type`

          - `"organization_disabled_error"OrganizationDisabledError`

      - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

        A memory store referenced by the deployment is archived.

        - `required Type Type`

          - `"memory_store_archived_error"MemoryStoreArchivedError`

      - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

        A skill referenced by the deployment's agent no longer exists.

        - `required Type Type`

          - `"skill_not_found_error"SkillNotFoundError`

      - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

        A vault referenced by the deployment is archived.

        - `required Type Type`

          - `"vault_archived_error"VaultArchivedError`

      - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

        An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

        - `required Type Type`

          - `"unknown_error"UnknownError`

      - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

        The deployment configures resources, but its environment is self-hosted and cannot mount them.

        - `required Type Type`

          - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

      - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

        An MCP server host used by the deployment's agent is blocked by the environment's network policy.

        - `required Type Type`

          - `"mcp_egress_blocked_error"McpEgressBlockedError`

    - `required Type Type`

      - `"error"Error`

### Beta Managed Agents Deployment Paused Reason Error

- `class BetaManagedAgentsDeploymentPausedReasonError: A class that can be one of several variants.union`

  The error that triggered an auto-pause. Matches the failed run's `error.type`.

  - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

    The deployment's environment was archived.

    - `required Type Type`

      - `"environment_archived_error"EnvironmentArchivedError`

  - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

    The deployment's agent was archived.

    - `required Type Type`

      - `"agent_archived_error"AgentArchivedError`

  - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

    The deployment's environment no longer exists.

    - `required Type Type`

      - `"environment_not_found_error"EnvironmentNotFoundError`

  - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

    A vault referenced by the deployment no longer exists.

    - `required Type Type`

      - `"vault_not_found_error"VaultNotFoundError`

  - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

    A file resource referenced by the deployment no longer exists.

    - `required Type Type`

      - `"file_not_found_error"FileNotFoundError`

  - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

    A referenced resource no longer exists and its kind was not reported.

    - `required Type Type`

      - `"session_resource_not_found_error"SessionResourceNotFoundError`

  - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

    The deployment's workspace was archived.

    - `required Type Type`

      - `"workspace_archived_error"WorkspaceArchivedError`

  - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

    The deployment's organization is disabled.

    - `required Type Type`

      - `"organization_disabled_error"OrganizationDisabledError`

  - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

    A memory store referenced by the deployment is archived.

    - `required Type Type`

      - `"memory_store_archived_error"MemoryStoreArchivedError`

  - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

    A skill referenced by the deployment's agent no longer exists.

    - `required Type Type`

      - `"skill_not_found_error"SkillNotFoundError`

  - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

    A vault referenced by the deployment is archived.

    - `required Type Type`

      - `"vault_archived_error"VaultArchivedError`

  - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

    An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

    - `required Type Type`

      - `"unknown_error"UnknownError`

  - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

    The deployment configures resources, but its environment is self-hosted and cannot mount them.

    - `required Type Type`

      - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

  - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

    An MCP server host used by the deployment's agent is blocked by the environment's network policy.

    - `required Type Type`

      - `"mcp_egress_blocked_error"McpEgressBlockedError`

### Beta Managed Agents Deployment Status

- `enum BetaManagedAgentsDeploymentStatus:`

  Lifecycle status of a deployment.

  - `"active"Active`

  - `"paused"Paused`

### Beta Managed Agents Deployment System Message Event

- `class BetaManagedAgentsDeploymentSystemMessageEvent:`

  Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

  - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

    System content blocks to append. Text-only.

    - `required string Text`

      The text content.

    - `required Type Type`

      - `"text"Text`

  - `required Type Type`

    - `"system.message"SystemMessage`

### Beta Managed Agents Deployment User Define Outcome Event

- `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

  An outcome the agent should work toward. The agent begins work on receipt.

  - `required string Description`

    What the agent should produce. This is the task specification.

  - `required Rubric Rubric`

    Rubric for grading the quality of an outcome.

    - `class BetaManagedAgentsFileRubric:`

      Rubric referenced by a file uploaded via the Files API.

      - `required string FileID`

        ID of the rubric file.

      - `required Type Type`

        - `"file"File`

    - `class BetaManagedAgentsTextRubric:`

      Rubric content provided inline as text.

      - `required string Content`

        Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `required Type Type`

        - `"text"Text`

  - `required Type Type`

    - `"user.define_outcome"UserDefineOutcome`

  - `Int? MaxIterations`

    Eval→revision cycles before giving up. Default 3, max 20.

### Beta Managed Agents Deployment User Message Event

- `class BetaManagedAgentsDeploymentUserMessageEvent:`

  A user message sent to the session.

  - `required IReadOnlyList<Content> Content`

    Array of content blocks for the user message.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `required string Text`

        The text content.

      - `required Type Type`

        - `"text"Text`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `required Source Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `required string Data`

            Base64-encoded image data.

          - `required string MediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `required Type Type`

            - `"base64"Base64`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `required Type Type`

            - `"url"Url`

          - `required string Url`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `required string FileID`

            ID of a previously uploaded file.

          - `required Type Type`

            - `"file"File`

      - `required Type Type`

        - `"image"Image`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `required Source Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `required string Data`

            Base64-encoded document data.

          - `required string MediaType`

            MIME type of the document (e.g., "application/pdf").

          - `required Type Type`

            - `"base64"Base64`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `required string Data`

            The plain text content.

          - `required MediaType MediaType`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"TextPlain`

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `required Type Type`

            - `"url"Url`

          - `required string Url`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `required string FileID`

            ID of a previously uploaded file.

          - `required Type Type`

            - `"file"File`

      - `required Type Type`

        - `"document"Document`

      - `string? Context`

        Additional context about the document for the model.

      - `string? Title`

        The title of the document.

    - `class BetaManagedAgentsRedactedBlock:`

      Placeholder for content withheld by Anthropic model policy.

      - `required Type Type`

        - `"redacted"Redacted`

  - `required Type Type`

    - `"user.message"UserMessage`

### Beta Managed Agents Environment Archived Deployment Paused Reason Error

- `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

  The deployment's environment was archived.

  - `required Type Type`

    - `"environment_archived_error"EnvironmentArchivedError`

### Beta Managed Agents Environment Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

  The deployment's environment no longer exists.

  - `required Type Type`

    - `"environment_not_found_error"EnvironmentNotFoundError`

### Beta Managed Agents Error Deployment Paused Reason

- `class BetaManagedAgentsErrorDeploymentPausedReason:`

  A scheduled fire recorded a failed run whose error auto-pauses the deployment.

  - `required BetaManagedAgentsDeploymentPausedReasonError Error`

    The error that triggered an auto-pause. Matches the failed run's `error.type`.

    - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

      The deployment's environment was archived.

      - `required Type Type`

        - `"environment_archived_error"EnvironmentArchivedError`

    - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

      The deployment's agent was archived.

      - `required Type Type`

        - `"agent_archived_error"AgentArchivedError`

    - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

      The deployment's environment no longer exists.

      - `required Type Type`

        - `"environment_not_found_error"EnvironmentNotFoundError`

    - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

      A vault referenced by the deployment no longer exists.

      - `required Type Type`

        - `"vault_not_found_error"VaultNotFoundError`

    - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

      A file resource referenced by the deployment no longer exists.

      - `required Type Type`

        - `"file_not_found_error"FileNotFoundError`

    - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

      A referenced resource no longer exists and its kind was not reported.

      - `required Type Type`

        - `"session_resource_not_found_error"SessionResourceNotFoundError`

    - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

      The deployment's workspace was archived.

      - `required Type Type`

        - `"workspace_archived_error"WorkspaceArchivedError`

    - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

      The deployment's organization is disabled.

      - `required Type Type`

        - `"organization_disabled_error"OrganizationDisabledError`

    - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

      A memory store referenced by the deployment is archived.

      - `required Type Type`

        - `"memory_store_archived_error"MemoryStoreArchivedError`

    - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

      A skill referenced by the deployment's agent no longer exists.

      - `required Type Type`

        - `"skill_not_found_error"SkillNotFoundError`

    - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

      A vault referenced by the deployment is archived.

      - `required Type Type`

        - `"vault_archived_error"VaultArchivedError`

    - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

      An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

      - `required Type Type`

        - `"unknown_error"UnknownError`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `required Type Type`

        - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

    - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `required Type Type`

        - `"mcp_egress_blocked_error"McpEgressBlockedError`

  - `required Type Type`

    - `"error"Error`

### Beta Managed Agents File Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

  A file resource referenced by the deployment no longer exists.

  - `required Type Type`

    - `"file_not_found_error"FileNotFoundError`

### Beta Managed Agents File Resource Config

- `class BetaManagedAgentsFileResourceConfig:`

  A file mounted into each session's container.

  - `required string FileID`

    ID of a previously uploaded file.

  - `required Type Type`

    - `"file"File`

  - `string? MountPath`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Config

- `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

  A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

  - `required Type Type`

    - `"github_repository"GitHubRepository`

  - `required string Url`

    Github URL of the repository

  - `Checkout? Checkout`

    Branch or commit to check out. Defaults to the repository's default branch.

    - `class BetaManagedAgentsBranchCheckout:`

      - `required string Name`

        Branch name to check out.

      - `required Type Type`

        - `"branch"Branch`

    - `class BetaManagedAgentsCommitCheckout:`

      - `required string Sha`

        Full commit SHA to check out.

      - `required Type Type`

        - `"commit"Commit`

  - `string? MountPath`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Manual Deployment Paused Reason

- `class BetaManagedAgentsManualDeploymentPausedReason:`

  The caller invoked the pause endpoint on the deployment.

  - `required Type Type`

    - `"manual"Manual`

### Beta Managed Agents MCP Egress Blocked Deployment Paused Reason Error

- `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

  An MCP server host used by the deployment's agent is blocked by the environment's network policy.

  - `required Type Type`

    - `"mcp_egress_blocked_error"McpEgressBlockedError`

### Beta Managed Agents Memory Store Archived Deployment Paused Reason Error

- `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

  A memory store referenced by the deployment is archived.

  - `required Type Type`

    - `"memory_store_archived_error"MemoryStoreArchivedError`

### Beta Managed Agents Memory Store Resource Config

- `class BetaManagedAgentsMemoryStoreResourceConfig:`

  A memory store attached to each session created from this deployment.

  - `required string MemoryStoreID`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `required Type Type`

    - `"memory_store"MemoryStore`

  - `Access? Access`

    Access mode for an attached memory store.

    - `"read_write"ReadWrite`

    - `"read_only"ReadOnly`

  - `string? Instructions`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Organization Disabled Deployment Paused Reason Error

- `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

  The deployment's organization is disabled.

  - `required Type Type`

    - `"organization_disabled_error"OrganizationDisabledError`

### Beta Managed Agents Schedule

- `class BetaManagedAgentsSchedule:`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `required string Expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `required string Timezone`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `required Type Type`

    - `"cron"Cron`

  - `DateTimeOffset? LastRunAt`

    A timestamp in RFC 3339 format

  - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Schedule Params

- `class BetaManagedAgentsScheduleParams:`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `required string Expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `required string Timezone`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `required Type Type`

    - `"cron"Cron`

### Beta Managed Agents Self Hosted Resources Unsupported Deployment Paused Reason Error

- `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

  The deployment configures resources, but its environment is self-hosted and cannot mount them.

  - `required Type Type`

    - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

### Beta Managed Agents Session Resource Config

- `class BetaManagedAgentsSessionResourceConfig: A class that can be one of several variants.union`

  A configured session resource. Echoes the input minus write-only credentials.

  - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

    A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

    - `required Type Type`

      - `"github_repository"GitHubRepository`

    - `required string Url`

      Github URL of the repository

    - `Checkout? Checkout`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `class BetaManagedAgentsBranchCheckout:`

        - `required string Name`

          Branch name to check out.

        - `required Type Type`

          - `"branch"Branch`

      - `class BetaManagedAgentsCommitCheckout:`

        - `required string Sha`

          Full commit SHA to check out.

        - `required Type Type`

          - `"commit"Commit`

    - `string? MountPath`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `class BetaManagedAgentsFileResourceConfig:`

    A file mounted into each session's container.

    - `required string FileID`

      ID of a previously uploaded file.

    - `required Type Type`

      - `"file"File`

    - `string? MountPath`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `class BetaManagedAgentsMemoryStoreResourceConfig:`

    A memory store attached to each session created from this deployment.

    - `required string MemoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `required Type Type`

      - `"memory_store"MemoryStore`

    - `Access? Access`

      Access mode for an attached memory store.

      - `"read_write"ReadWrite`

      - `"read_only"ReadOnly`

    - `string? Instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Session Resource Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

  A referenced resource no longer exists and its kind was not reported.

  - `required Type Type`

    - `"session_resource_not_found_error"SessionResourceNotFoundError`

### Beta Managed Agents Skill Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

  A skill referenced by the deployment's agent no longer exists.

  - `required Type Type`

    - `"skill_not_found_error"SkillNotFoundError`

### Beta Managed Agents Unknown Deployment Paused Reason Error

- `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

  An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

  - `required Type Type`

    - `"unknown_error"UnknownError`

### Beta Managed Agents Vault Archived Deployment Paused Reason Error

- `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

  A vault referenced by the deployment is archived.

  - `required Type Type`

    - `"vault_archived_error"VaultArchivedError`

### Beta Managed Agents Vault Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

  A vault referenced by the deployment no longer exists.

  - `required Type Type`

    - `"vault_not_found_error"VaultNotFoundError`

### Beta Managed Agents Workspace Archived Deployment Paused Reason Error

- `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

  The deployment's workspace was archived.

  - `required Type Type`

    - `"workspace_archived_error"WorkspaceArchivedError`

# Deployment Runs

## List Deployment Runs

`DeploymentRunListPageResponse Beta.DeploymentRuns.List(DeploymentRunListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/deployment_runs`

List Deployment Runs

### Parameters

- `DeploymentRunListParams parameters`

  - `DateTimeOffset createdAtGt`

    Query param: Return runs created strictly after this time (exclusive).

  - `DateTimeOffset createdAtGte`

    Query param: Return runs created at or after this time (inclusive).

  - `DateTimeOffset createdAtLt`

    Query param: Return runs created strictly before this time (exclusive).

  - `DateTimeOffset createdAtLte`

    Query param: Return runs created at or before this time (inclusive).

  - `string deploymentID`

    Query param: Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent deployment_id returns 200 with empty data.

  - `Boolean hasError`

    Query param: Filter: true for runs with non-null error, false for runs with non-null session_id. Omit for all.

  - `Int limit`

    Query param: Maximum results per page. Default 20, maximum 1000.

  - `string page`

    Query param: Opaque pagination cursor. Pass next_page from the previous response. Invalid or expired cursors return 400.

  - `BetaManagedAgentsTriggerType triggerType`

    Query param: Filter runs by what triggered them. Omit to return all runs.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class DeploymentRunListPageResponse:`

  Paginated list of deployment runs. Sorted by created_at descending (most recent first).

  - `required IReadOnlyList<BetaManagedAgentsDeploymentRun> Data`

    List of deployment runs.

    - `required string ID`

      Unique identifier for this run (`drun_...`).

    - `required BetaManagedAgentsAgentReference Agent`

      A resolved agent reference with a concrete version.

      - `required string ID`

      - `required Type Type`

        - `"agent"Agent`

      - `required Int Version`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required string DeploymentID`

      ID of the deployment that produced this run.

    - `required Error? Error`

      Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

      - `class BetaManagedAgentsEnvironmentArchivedRunError:`

        The deployment's environment was archived.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"environment_archived_error"EnvironmentArchivedError`

      - `class BetaManagedAgentsAgentArchivedRunError:`

        The deployment's agent was archived.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"agent_archived_error"AgentArchivedError`

      - `class BetaManagedAgentsEnvironmentNotFoundRunError:`

        The deployment's environment no longer exists.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"environment_not_found_error"EnvironmentNotFoundError`

      - `class BetaManagedAgentsVaultNotFoundRunError:`

        A vault referenced by the deployment no longer exists.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"vault_not_found_error"VaultNotFoundError`

      - `class BetaManagedAgentsVaultArchivedRunError:`

        A vault referenced by the deployment is archived.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"vault_archived_error"VaultArchivedError`

      - `class BetaManagedAgentsFileNotFoundRunError:`

        A file resource referenced by the deployment no longer exists.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"file_not_found_error"FileNotFoundError`

      - `class BetaManagedAgentsMemoryStoreArchivedRunError:`

        A memory store referenced by the deployment is archived.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"memory_store_archived_error"MemoryStoreArchivedError`

      - `class BetaManagedAgentsSkillNotFoundRunError:`

        A skill referenced by the deployment's agent no longer exists.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"skill_not_found_error"SkillNotFoundError`

      - `class BetaManagedAgentsSessionResourceNotFoundRunError:`

        A referenced resource no longer exists and its kind was not reported.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"session_resource_not_found_error"SessionResourceNotFoundError`

      - `class BetaManagedAgentsWorkspaceArchivedRunError:`

        The deployment's workspace was archived.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"workspace_archived_error"WorkspaceArchivedError`

      - `class BetaManagedAgentsOrganizationDisabledRunError:`

        The deployment's organization is disabled.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"organization_disabled_error"OrganizationDisabledError`

      - `class BetaManagedAgentsSessionRateLimitedRunError:`

        Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"session_rate_limited_error"SessionRateLimitedError`

      - `class BetaManagedAgentsSessionCreationRejectedRunError:`

        The session create request was rejected with a non-retryable validation error.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"session_creation_rejected_error"SessionCreationRejectedError`

      - `class BetaManagedAgentsUnknownRunError:`

        An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"unknown_error"UnknownError`

      - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:`

        The deployment configures resources, but its environment is self-hosted and cannot mount them.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

      - `class BetaManagedAgentsMcpEgressBlockedRunError:`

        An MCP server host used by the deployment's agent is blocked by the environment's network policy.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"mcp_egress_blocked_error"McpEgressBlockedError`

    - `required string? SessionID`

      Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

    - `required BetaManagedAgentsTriggerContext TriggerContext`

      Describes what triggered a deployment run, with trigger-specific metadata.

      - `class BetaManagedAgentsScheduleTriggerContext:`

        The run was fired by the deployment's cron schedule.

        - `required DateTimeOffset ScheduledAt`

          A timestamp in RFC 3339 format

        - `required Type Type`

          - `"schedule"Schedule`

      - `class BetaManagedAgentsManualTriggerContext:`

        The run was started manually by creating a session directly against the deployment.

        - `required Type Type`

          - `"manual"Manual`

    - `required Type Type`

      - `"deployment_run"DeploymentRun`

  - `string? NextPage`

    Opaque cursor for the next page. Null when no more results.

### Example

```csharp
DeploymentRunListParams parameters = new();

var page = await client.Beta.DeploymentRuns.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "agent": {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "type": "agent",
        "version": 1
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "deployment_id": "deployment_id",
      "error": {
        "message": "message",
        "type": "environment_archived_error"
      },
      "session_id": "session_id",
      "trigger_context": {
        "scheduled_at": "2019-12-27T18:11:19.117Z",
        "type": "schedule"
      },
      "type": "deployment_run"
    }
  ],
  "next_page": "next_page"
}
```

## Get Deployment Run

`BetaManagedAgentsDeploymentRun Beta.DeploymentRuns.Retrieve(DeploymentRunRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/deployment_runs/{deployment_run_id}`

Get Deployment Run

### Parameters

- `DeploymentRunRetrieveParams parameters`

  - `required string deploymentRunID`

    Path parameter deployment_run_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsDeploymentRun:`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `required string ID`

    Unique identifier for this run (`drun_...`).

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string DeploymentID`

    ID of the deployment that produced this run.

  - `required Error? Error`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `class BetaManagedAgentsEnvironmentArchivedRunError:`

      The deployment's environment was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"environment_archived_error"EnvironmentArchivedError`

    - `class BetaManagedAgentsAgentArchivedRunError:`

      The deployment's agent was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"agent_archived_error"AgentArchivedError`

    - `class BetaManagedAgentsEnvironmentNotFoundRunError:`

      The deployment's environment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"environment_not_found_error"EnvironmentNotFoundError`

    - `class BetaManagedAgentsVaultNotFoundRunError:`

      A vault referenced by the deployment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"vault_not_found_error"VaultNotFoundError`

    - `class BetaManagedAgentsVaultArchivedRunError:`

      A vault referenced by the deployment is archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"vault_archived_error"VaultArchivedError`

    - `class BetaManagedAgentsFileNotFoundRunError:`

      A file resource referenced by the deployment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"file_not_found_error"FileNotFoundError`

    - `class BetaManagedAgentsMemoryStoreArchivedRunError:`

      A memory store referenced by the deployment is archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"memory_store_archived_error"MemoryStoreArchivedError`

    - `class BetaManagedAgentsSkillNotFoundRunError:`

      A skill referenced by the deployment's agent no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"skill_not_found_error"SkillNotFoundError`

    - `class BetaManagedAgentsSessionResourceNotFoundRunError:`

      A referenced resource no longer exists and its kind was not reported.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"session_resource_not_found_error"SessionResourceNotFoundError`

    - `class BetaManagedAgentsWorkspaceArchivedRunError:`

      The deployment's workspace was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"workspace_archived_error"WorkspaceArchivedError`

    - `class BetaManagedAgentsOrganizationDisabledRunError:`

      The deployment's organization is disabled.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"organization_disabled_error"OrganizationDisabledError`

    - `class BetaManagedAgentsSessionRateLimitedRunError:`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"session_rate_limited_error"SessionRateLimitedError`

    - `class BetaManagedAgentsSessionCreationRejectedRunError:`

      The session create request was rejected with a non-retryable validation error.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"session_creation_rejected_error"SessionCreationRejectedError`

    - `class BetaManagedAgentsUnknownRunError:`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"unknown_error"UnknownError`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

    - `class BetaManagedAgentsMcpEgressBlockedRunError:`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"mcp_egress_blocked_error"McpEgressBlockedError`

  - `required string? SessionID`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `required BetaManagedAgentsTriggerContext TriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext:`

      The run was fired by the deployment's cron schedule.

      - `required DateTimeOffset ScheduledAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"schedule"Schedule`

    - `class BetaManagedAgentsManualTriggerContext:`

      The run was started manually by creating a session directly against the deployment.

      - `required Type Type`

        - `"manual"Manual`

  - `required Type Type`

    - `"deployment_run"DeploymentRun`

### Example

```csharp
DeploymentRunRetrieveParams parameters = new()
{
    DeploymentRunID = "deployment_run_id"
};

var betaManagedAgentsDeploymentRun = await client.Beta.DeploymentRuns.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsDeploymentRun);
```

#### Response

```json
{
  "id": "id",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "type": "agent",
    "version": 1
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "deployment_id": "deployment_id",
  "error": {
    "message": "message",
    "type": "environment_archived_error"
  },
  "session_id": "session_id",
  "trigger_context": {
    "scheduled_at": "2019-12-27T18:11:19.117Z",
    "type": "schedule"
  },
  "type": "deployment_run"
}
```

## Domain Types

### Beta Managed Agents Agent Archived Run Error

- `class BetaManagedAgentsAgentArchivedRunError:`

  The deployment's agent was archived.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"agent_archived_error"AgentArchivedError`

### Beta Managed Agents Deployment Run

- `class BetaManagedAgentsDeploymentRun:`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `required string ID`

    Unique identifier for this run (`drun_...`).

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string DeploymentID`

    ID of the deployment that produced this run.

  - `required Error? Error`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `class BetaManagedAgentsEnvironmentArchivedRunError:`

      The deployment's environment was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"environment_archived_error"EnvironmentArchivedError`

    - `class BetaManagedAgentsAgentArchivedRunError:`

      The deployment's agent was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"agent_archived_error"AgentArchivedError`

    - `class BetaManagedAgentsEnvironmentNotFoundRunError:`

      The deployment's environment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"environment_not_found_error"EnvironmentNotFoundError`

    - `class BetaManagedAgentsVaultNotFoundRunError:`

      A vault referenced by the deployment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"vault_not_found_error"VaultNotFoundError`

    - `class BetaManagedAgentsVaultArchivedRunError:`

      A vault referenced by the deployment is archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"vault_archived_error"VaultArchivedError`

    - `class BetaManagedAgentsFileNotFoundRunError:`

      A file resource referenced by the deployment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"file_not_found_error"FileNotFoundError`

    - `class BetaManagedAgentsMemoryStoreArchivedRunError:`

      A memory store referenced by the deployment is archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"memory_store_archived_error"MemoryStoreArchivedError`

    - `class BetaManagedAgentsSkillNotFoundRunError:`

      A skill referenced by the deployment's agent no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"skill_not_found_error"SkillNotFoundError`

    - `class BetaManagedAgentsSessionResourceNotFoundRunError:`

      A referenced resource no longer exists and its kind was not reported.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"session_resource_not_found_error"SessionResourceNotFoundError`

    - `class BetaManagedAgentsWorkspaceArchivedRunError:`

      The deployment's workspace was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"workspace_archived_error"WorkspaceArchivedError`

    - `class BetaManagedAgentsOrganizationDisabledRunError:`

      The deployment's organization is disabled.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"organization_disabled_error"OrganizationDisabledError`

    - `class BetaManagedAgentsSessionRateLimitedRunError:`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"session_rate_limited_error"SessionRateLimitedError`

    - `class BetaManagedAgentsSessionCreationRejectedRunError:`

      The session create request was rejected with a non-retryable validation error.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"session_creation_rejected_error"SessionCreationRejectedError`

    - `class BetaManagedAgentsUnknownRunError:`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"unknown_error"UnknownError`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

    - `class BetaManagedAgentsMcpEgressBlockedRunError:`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"mcp_egress_blocked_error"McpEgressBlockedError`

  - `required string? SessionID`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `required BetaManagedAgentsTriggerContext TriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext:`

      The run was fired by the deployment's cron schedule.

      - `required DateTimeOffset ScheduledAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"schedule"Schedule`

    - `class BetaManagedAgentsManualTriggerContext:`

      The run was started manually by creating a session directly against the deployment.

      - `required Type Type`

        - `"manual"Manual`

  - `required Type Type`

    - `"deployment_run"DeploymentRun`

### Beta Managed Agents Environment Archived Run Error

- `class BetaManagedAgentsEnvironmentArchivedRunError:`

  The deployment's environment was archived.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"environment_archived_error"EnvironmentArchivedError`

### Beta Managed Agents Environment Not Found Run Error

- `class BetaManagedAgentsEnvironmentNotFoundRunError:`

  The deployment's environment no longer exists.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"environment_not_found_error"EnvironmentNotFoundError`

### Beta Managed Agents File Not Found Run Error

- `class BetaManagedAgentsFileNotFoundRunError:`

  A file resource referenced by the deployment no longer exists.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"file_not_found_error"FileNotFoundError`

### Beta Managed Agents Manual Trigger Context

- `class BetaManagedAgentsManualTriggerContext:`

  The run was started manually by creating a session directly against the deployment.

  - `required Type Type`

    - `"manual"Manual`

### Beta Managed Agents MCP Egress Blocked Run Error

- `class BetaManagedAgentsMcpEgressBlockedRunError:`

  An MCP server host used by the deployment's agent is blocked by the environment's network policy.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"mcp_egress_blocked_error"McpEgressBlockedError`

### Beta Managed Agents Memory Store Archived Run Error

- `class BetaManagedAgentsMemoryStoreArchivedRunError:`

  A memory store referenced by the deployment is archived.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"memory_store_archived_error"MemoryStoreArchivedError`

### Beta Managed Agents Organization Disabled Run Error

- `class BetaManagedAgentsOrganizationDisabledRunError:`

  The deployment's organization is disabled.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"organization_disabled_error"OrganizationDisabledError`

### Beta Managed Agents Schedule Trigger Context

- `class BetaManagedAgentsScheduleTriggerContext:`

  The run was fired by the deployment's cron schedule.

  - `required DateTimeOffset ScheduledAt`

    A timestamp in RFC 3339 format

  - `required Type Type`

    - `"schedule"Schedule`

### Beta Managed Agents Self Hosted Resources Unsupported Run Error

- `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:`

  The deployment configures resources, but its environment is self-hosted and cannot mount them.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

### Beta Managed Agents Session Creation Rejected Run Error

- `class BetaManagedAgentsSessionCreationRejectedRunError:`

  The session create request was rejected with a non-retryable validation error.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"session_creation_rejected_error"SessionCreationRejectedError`

### Beta Managed Agents Session Rate Limited Run Error

- `class BetaManagedAgentsSessionRateLimitedRunError:`

  Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"session_rate_limited_error"SessionRateLimitedError`

### Beta Managed Agents Session Resource Not Found Run Error

- `class BetaManagedAgentsSessionResourceNotFoundRunError:`

  A referenced resource no longer exists and its kind was not reported.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"session_resource_not_found_error"SessionResourceNotFoundError`

### Beta Managed Agents Skill Not Found Run Error

- `class BetaManagedAgentsSkillNotFoundRunError:`

  A skill referenced by the deployment's agent no longer exists.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"skill_not_found_error"SkillNotFoundError`

### Beta Managed Agents Trigger Context

- `class BetaManagedAgentsTriggerContext: A class that can be one of several variants.union`

  Describes what triggered a deployment run, with trigger-specific metadata.

  - `class BetaManagedAgentsScheduleTriggerContext:`

    The run was fired by the deployment's cron schedule.

    - `required DateTimeOffset ScheduledAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"schedule"Schedule`

  - `class BetaManagedAgentsManualTriggerContext:`

    The run was started manually by creating a session directly against the deployment.

    - `required Type Type`

      - `"manual"Manual`

### Beta Managed Agents Trigger Type

- `enum BetaManagedAgentsTriggerType:`

  What triggered a deployment run.

  - `"schedule"Schedule`

  - `"manual"Manual`

### Beta Managed Agents Unknown Run Error

- `class BetaManagedAgentsUnknownRunError:`

  An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"unknown_error"UnknownError`

### Beta Managed Agents Vault Archived Run Error

- `class BetaManagedAgentsVaultArchivedRunError:`

  A vault referenced by the deployment is archived.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"vault_archived_error"VaultArchivedError`

### Beta Managed Agents Vault Not Found Run Error

- `class BetaManagedAgentsVaultNotFoundRunError:`

  A vault referenced by the deployment no longer exists.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"vault_not_found_error"VaultNotFoundError`

### Beta Managed Agents Workspace Archived Run Error

- `class BetaManagedAgentsWorkspaceArchivedRunError:`

  The deployment's workspace was archived.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"workspace_archived_error"WorkspaceArchivedError`

# Vaults

## Create Vault

`BetaManagedAgentsVault Beta.Vaults.Create(VaultCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/vaults`

Create Vault

### Parameters

- `VaultCreateParams parameters`

  - `required string displayName`

    Body param: Human-readable name for the vault. 1-255 characters.

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `required string ID`

    Unique identifier for the vault.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string DisplayName`

    Human-readable name for the vault.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the vault.

  - `required Type Type`

    - `"vault"Vault`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

### Example

```csharp
VaultCreateParams parameters = new() { DisplayName = "Example vault" };

var betaManagedAgentsVault = await client.Beta.Vaults.Create(parameters);

Console.WriteLine(betaManagedAgentsVault);
```

#### Response

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## List Vaults

`VaultListPageResponse Beta.Vaults.List(VaultListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/vaults`

List Vaults

### Parameters

- `VaultListParams parameters`

  - `Boolean includeArchived`

    Query param: Whether to include archived vaults in the results.

  - `Int limit`

    Query param: Maximum number of vaults to return per page. Defaults to 20, maximum 100.

  - `string page`

    Query param: Opaque pagination token from a previous `list_vaults` response.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class VaultListPageResponse:`

  Response containing a paginated list of vaults.

  - `IReadOnlyList<BetaManagedAgentsVault> Data`

    List of vaults.

    - `required string ID`

      Unique identifier for the vault.

    - `required DateTimeOffset? ArchivedAt`

      A timestamp in RFC 3339 format

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required string DisplayName`

      Human-readable name for the vault.

    - `required IReadOnlyDictionary<string, string> Metadata`

      Arbitrary key-value metadata attached to the vault.

    - `required Type Type`

      - `"vault"Vault`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

  - `string? NextPage`

    Pagination token for the next page, or null if no more results.

### Example

```csharp
VaultListParams parameters = new();

var page = await client.Beta.Vaults.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "display_name": "Example vault",
      "metadata": {
        "environment": "production"
      },
      "type": "vault",
      "updated_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Vault

`BetaManagedAgentsVault Beta.Vaults.Retrieve(VaultRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/vaults/{vault_id}`

Get Vault

### Parameters

- `VaultRetrieveParams parameters`

  - `required string vaultID`

    Path parameter vault_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `required string ID`

    Unique identifier for the vault.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string DisplayName`

    Human-readable name for the vault.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the vault.

  - `required Type Type`

    - `"vault"Vault`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

### Example

```csharp
VaultRetrieveParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv"
};

var betaManagedAgentsVault = await client.Beta.Vaults.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsVault);
```

#### Response

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## Update Vault

`BetaManagedAgentsVault Beta.Vaults.Update(VaultUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/vaults/{vault_id}`

Update Vault

### Parameters

- `VaultUpdateParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `string? displayName`

    Body param: Updated human-readable name for the vault. 1-255 characters.

  - `IReadOnlyDictionary<string, string>? metadata`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `required string ID`

    Unique identifier for the vault.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string DisplayName`

    Human-readable name for the vault.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the vault.

  - `required Type Type`

    - `"vault"Vault`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

### Example

```csharp
VaultUpdateParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv"
};

var betaManagedAgentsVault = await client.Beta.Vaults.Update(parameters);

Console.WriteLine(betaManagedAgentsVault);
```

#### Response

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## Delete Vault

`BetaManagedAgentsDeletedVault Beta.Vaults.Delete(VaultDeleteParamsparameters, CancellationTokencancellationToken = default)`

**delete** `/v1/vaults/{vault_id}`

Delete Vault

### Parameters

- `VaultDeleteParams parameters`

  - `required string vaultID`

    Path parameter vault_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsDeletedVault:`

  Confirmation of a deleted vault.

  - `required string ID`

    Unique identifier of the deleted vault.

  - `required Type Type`

    - `"vault_deleted"VaultDeleted`

### Example

```csharp
VaultDeleteParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv"
};

var betaManagedAgentsDeletedVault = await client.Beta.Vaults.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeletedVault);
```

#### Response

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

## Archive Vault

`BetaManagedAgentsVault Beta.Vaults.Archive(VaultArchiveParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/vaults/{vault_id}/archive`

Archive Vault

### Parameters

- `VaultArchiveParams parameters`

  - `required string vaultID`

    Path parameter vault_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `required string ID`

    Unique identifier for the vault.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string DisplayName`

    Human-readable name for the vault.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the vault.

  - `required Type Type`

    - `"vault"Vault`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

### Example

```csharp
VaultArchiveParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv"
};

var betaManagedAgentsVault = await client.Beta.Vaults.Archive(parameters);

Console.WriteLine(betaManagedAgentsVault);
```

#### Response

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## Domain Types

### Beta Managed Agents Deleted Vault

- `class BetaManagedAgentsDeletedVault:`

  Confirmation of a deleted vault.

  - `required string ID`

    Unique identifier of the deleted vault.

  - `required Type Type`

    - `"vault_deleted"VaultDeleted`

### Beta Managed Agents Vault

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `required string ID`

    Unique identifier for the vault.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string DisplayName`

    Human-readable name for the vault.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the vault.

  - `required Type Type`

    - `"vault"Vault`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

# Credentials

## Create Credential

`BetaManagedAgentsCredential Beta.Vaults.Credentials.Create(CredentialCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/vaults/{vault_id}/credentials`

Create Credential

### Parameters

- `CredentialCreateParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `required Auth auth`

    Body param: Authentication details for creating a credential.

    - `class BetaManagedAgentsMcpOAuthCreateParams:`

      Parameters for creating an MCP OAuth credential.

      - `required string AccessToken`

        OAuth access token.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

        - `"mcp_oauth"McpOAuth`

      - `DateTimeOffset? ExpiresAt`

        A timestamp in RFC 3339 format

      - `BetaManagedAgentsMcpOAuthRefreshParams? Refresh`

        OAuth refresh token parameters for creating a credential with refresh support.

        - `required string ClientID`

          OAuth client ID.

        - `required string RefreshToken`

          OAuth refresh token.

        - `required string TokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `required TokenEndpointAuth TokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneParam:`

            Token endpoint requires no client authentication.

            - `required Type Type`

              - `"none"None`

          - `class BetaManagedAgentsTokenEndpointAuthBasicParam:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `required string ClientSecret`

              OAuth client secret.

            - `required Type Type`

              - `"client_secret_basic"ClientSecretBasic`

          - `class BetaManagedAgentsTokenEndpointAuthPostParam:`

            Token endpoint uses POST body authentication with client credentials.

            - `required string ClientSecret`

              OAuth client secret.

            - `required Type Type`

              - `"client_secret_post"ClientSecretPost`

        - `string? Resource`

          OAuth resource indicator.

        - `string? Scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerCreateParams:`

      Parameters for creating a static bearer token credential.

      - `required string Token`

        Static bearer token value.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

        - `"static_bearer"StaticBearer`

    - `class BetaManagedAgentsEnvironmentVariableCreateParams:`

      Parameters for creating an environment variable credential.

      - `required BetaManagedAgentsCredentialNetworkingParams Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:`

          Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

          - `required Type Type`

            - `"unrestricted"Unrestricted`

        - `class BetaManagedAgentsLimitedCredentialNetworkingParams:`

          Substitute the secret only on requests to the listed hosts.

          - `required IReadOnlyList<string> AllowedHosts`

            Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

          - `required Type Type`

            - `"limited"Limited`

      - `required string SecretName`

        Name of the environment variable. Immutable after create.

      - `required string SecretValue`

        Secret value. Write-only; never returned in responses.

      - `required Type Type`

        - `"environment_variable"EnvironmentVariable`

      - `BetaManagedAgentsInjectionLocationParams InjectionLocation`

        Where in the outbound request the secret value may be substituted.

        - `Boolean Body`

          Substitute when the placeholder appears in the request body.

        - `Boolean Header`

          Substitute when the placeholder appears in a request header value.

  - `string? displayName`

    Body param: Human-readable name for the credential. Up to 255 characters.

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `required string ID`

    Unique identifier for the credential.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required Auth Auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

        - `"mcp_oauth"McpOAuth`

      - `DateTimeOffset? ExpiresAt`

        A timestamp in RFC 3339 format

      - `BetaManagedAgentsMcpOAuthRefreshResponse? Refresh`

        OAuth refresh token configuration returned in credential responses.

        - `required string ClientID`

          OAuth client ID.

        - `required string TokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `required TokenEndpointAuth TokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `required Type Type`

              - `"none"None`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `required Type Type`

              - `"client_secret_basic"ClientSecretBasic`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `required Type Type`

              - `"client_secret_post"ClientSecretPost`

        - `string? Resource`

          OAuth resource indicator.

        - `string? Scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

        - `"static_bearer"StaticBearer`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `required BetaManagedAgentsInjectionLocationResponse InjectionLocation`

        Where in the outbound request the secret value is substituted.

        - `required Boolean Body`

          Whether the placeholder is substituted in the request body.

        - `required Boolean Header`

          Whether the placeholder is substituted in request header values.

      - `required Networking Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `required Type Type`

            - `"unrestricted"Unrestricted`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `required IReadOnlyList<string> AllowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `required Type Type`

            - `"limited"Limited`

      - `required string SecretName`

        Name of the environment variable.

      - `required Type Type`

        - `"environment_variable"EnvironmentVariable`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the credential.

  - `required Type Type`

    - `"vault_credential"VaultCredential`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required string VaultID`

    Identifier of the vault this credential belongs to.

  - `string? DisplayName`

    Human-readable name for the credential.

### Example

```csharp
CredentialCreateParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    Auth = new BetaManagedAgentsStaticBearerCreateParams()
    {
        Token = "bearer_exampletoken",
        McpServerUrl = "https://example-server.modelcontextprotocol.io/sse",
        Type = Type.StaticBearer,
    },
};

var betaManagedAgentsCredential = await client.Beta.Vaults.Credentials.Create(parameters);

Console.WriteLine(betaManagedAgentsCredential);
```

#### Response

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

## List Credentials

`CredentialListPageResponse Beta.Vaults.Credentials.List(CredentialListParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/vaults/{vault_id}/credentials`

List Credentials

### Parameters

- `CredentialListParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `Boolean includeArchived`

    Query param: Whether to include archived credentials in the results.

  - `Int limit`

    Query param: Maximum number of credentials to return per page. Defaults to 20, maximum 100.

  - `string page`

    Query param: Opaque pagination token from a previous `list_credentials` response.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class CredentialListPageResponse:`

  Response containing a paginated list of credentials.

  - `IReadOnlyList<BetaManagedAgentsCredential> Data`

    List of credentials.

    - `required string ID`

      Unique identifier for the credential.

    - `required DateTimeOffset? ArchivedAt`

      A timestamp in RFC 3339 format

    - `required Auth Auth`

      Authentication details for a credential.

      - `class BetaManagedAgentsMcpOAuthAuthResponse:`

        OAuth credential details for an MCP server.

        - `required string McpServerUrl`

          URL of the MCP server this credential authenticates against.

        - `required Type Type`

          - `"mcp_oauth"McpOAuth`

        - `DateTimeOffset? ExpiresAt`

          A timestamp in RFC 3339 format

        - `BetaManagedAgentsMcpOAuthRefreshResponse? Refresh`

          OAuth refresh token configuration returned in credential responses.

          - `required string ClientID`

            OAuth client ID.

          - `required string TokenEndpoint`

            Token endpoint URL used to refresh the access token.

          - `required TokenEndpointAuth TokenEndpointAuth`

            Token endpoint requires no client authentication.

            - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

              Token endpoint requires no client authentication.

              - `required Type Type`

                - `"none"None`

            - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

              Token endpoint uses HTTP Basic authentication with client credentials.

              - `required Type Type`

                - `"client_secret_basic"ClientSecretBasic`

            - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

              Token endpoint uses POST body authentication with client credentials.

              - `required Type Type`

                - `"client_secret_post"ClientSecretPost`

          - `string? Resource`

            OAuth resource indicator.

          - `string? Scope`

            OAuth scope for the refresh request.

      - `class BetaManagedAgentsStaticBearerAuthResponse:`

        Static bearer token credential details for an MCP server.

        - `required string McpServerUrl`

          URL of the MCP server this credential authenticates against.

        - `required Type Type`

          - `"static_bearer"StaticBearer`

      - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

        Environment variable credential details. The secret value is never returned.

        - `required BetaManagedAgentsInjectionLocationResponse InjectionLocation`

          Where in the outbound request the secret value is substituted.

          - `required Boolean Body`

            Whether the placeholder is substituted in the request body.

          - `required Boolean Header`

            Whether the placeholder is substituted in request header values.

        - `required Networking Networking`

          Outbound hosts the secret value is substituted on.

          - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

            The secret is substituted on any host the session's Environment network policy permits egress to.

            - `required Type Type`

              - `"unrestricted"Unrestricted`

          - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

            The secret is substituted only on requests to the listed hosts.

            - `required IReadOnlyList<string> AllowedHosts`

              Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

            - `required Type Type`

              - `"limited"Limited`

        - `required string SecretName`

          Name of the environment variable.

        - `required Type Type`

          - `"environment_variable"EnvironmentVariable`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required IReadOnlyDictionary<string, string> Metadata`

      Arbitrary key-value metadata attached to the credential.

    - `required Type Type`

      - `"vault_credential"VaultCredential`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

    - `required string VaultID`

      Identifier of the vault this credential belongs to.

    - `string? DisplayName`

      Human-readable name for the credential.

  - `string? NextPage`

    Pagination token for the next page, or null if no more results.

### Example

```csharp
CredentialListParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv"
};

var page = await client.Beta.Vaults.Credentials.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
      "archived_at": null,
      "auth": {
        "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
        "type": "static_bearer"
      },
      "created_at": "2026-03-15T10:00:00Z",
      "metadata": {
        "environment": "production"
      },
      "type": "vault_credential",
      "updated_at": "2026-03-15T10:00:00Z",
      "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "display_name": "Example credential"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Credential

`BetaManagedAgentsCredential Beta.Vaults.Credentials.Retrieve(CredentialRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Get Credential

### Parameters

- `CredentialRetrieveParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `required string credentialID`

    Path param: Path parameter credential_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `required string ID`

    Unique identifier for the credential.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required Auth Auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

        - `"mcp_oauth"McpOAuth`

      - `DateTimeOffset? ExpiresAt`

        A timestamp in RFC 3339 format

      - `BetaManagedAgentsMcpOAuthRefreshResponse? Refresh`

        OAuth refresh token configuration returned in credential responses.

        - `required string ClientID`

          OAuth client ID.

        - `required string TokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `required TokenEndpointAuth TokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `required Type Type`

              - `"none"None`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `required Type Type`

              - `"client_secret_basic"ClientSecretBasic`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `required Type Type`

              - `"client_secret_post"ClientSecretPost`

        - `string? Resource`

          OAuth resource indicator.

        - `string? Scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

        - `"static_bearer"StaticBearer`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `required BetaManagedAgentsInjectionLocationResponse InjectionLocation`

        Where in the outbound request the secret value is substituted.

        - `required Boolean Body`

          Whether the placeholder is substituted in the request body.

        - `required Boolean Header`

          Whether the placeholder is substituted in request header values.

      - `required Networking Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `required Type Type`

            - `"unrestricted"Unrestricted`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `required IReadOnlyList<string> AllowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `required Type Type`

            - `"limited"Limited`

      - `required string SecretName`

        Name of the environment variable.

      - `required Type Type`

        - `"environment_variable"EnvironmentVariable`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the credential.

  - `required Type Type`

    - `"vault_credential"VaultCredential`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required string VaultID`

    Identifier of the vault this credential belongs to.

  - `string? DisplayName`

    Human-readable name for the credential.

### Example

```csharp
CredentialRetrieveParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYOQfSkw",
};

var betaManagedAgentsCredential = await client.Beta.Vaults.Credentials.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsCredential);
```

#### Response

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

## Update Credential

`BetaManagedAgentsCredential Beta.Vaults.Credentials.Update(CredentialUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

### Parameters

- `CredentialUpdateParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `required string credentialID`

    Path param: Path parameter credential_id

  - `Auth auth`

    Body param: Updated authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthUpdateParams:`

      Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

      - `required Type Type`

        - `"mcp_oauth"McpOAuth`

      - `string? AccessToken`

        Updated OAuth access token.

      - `DateTimeOffset? ExpiresAt`

        A timestamp in RFC 3339 format

      - `BetaManagedAgentsMcpOAuthRefreshUpdateParams? Refresh`

        Parameters for updating OAuth refresh token configuration.

        - `string? RefreshToken`

          Updated OAuth refresh token.

        - `string? Scope`

          Updated OAuth scope for the refresh request.

        - `TokenEndpointAuth TokenEndpointAuth`

          Updated HTTP Basic authentication parameters for the token endpoint.

          - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:`

            Updated HTTP Basic authentication parameters for the token endpoint.

            - `required Type Type`

              - `"client_secret_basic"ClientSecretBasic`

            - `string? ClientSecret`

              Updated OAuth client secret.

          - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:`

            Updated POST body authentication parameters for the token endpoint.

            - `required Type Type`

              - `"client_secret_post"ClientSecretPost`

            - `string? ClientSecret`

              Updated OAuth client secret.

    - `class BetaManagedAgentsStaticBearerUpdateParams:`

      Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

      - `required Type Type`

        - `"static_bearer"StaticBearer`

      - `string? Token`

        Updated static bearer token value.

    - `class BetaManagedAgentsEnvironmentVariableUpdateParams:`

      Parameters for updating an environment variable credential. `secret_name` is immutable.

      - `required Type Type`

        - `"environment_variable"EnvironmentVariable`

      - `BetaManagedAgentsInjectionLocationUpdateParams InjectionLocation`

        Updated injection location.

        - `Boolean Body`

          Substitute when the placeholder appears in the request body.

        - `Boolean Header`

          Substitute when the placeholder appears in a request header value.

      - `BetaManagedAgentsCredentialNetworkingParams? Networking`

        Updated networking scope. Full replacement.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:`

          Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

          - `required Type Type`

            - `"unrestricted"Unrestricted`

        - `class BetaManagedAgentsLimitedCredentialNetworkingParams:`

          Substitute the secret only on requests to the listed hosts.

          - `required IReadOnlyList<string> AllowedHosts`

            Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

          - `required Type Type`

            - `"limited"Limited`

      - `string? SecretValue`

        Updated secret value.

  - `string? displayName`

    Body param: Updated human-readable name for the credential. 1-255 characters.

  - `IReadOnlyDictionary<string, string>? metadata`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `required string ID`

    Unique identifier for the credential.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required Auth Auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

        - `"mcp_oauth"McpOAuth`

      - `DateTimeOffset? ExpiresAt`

        A timestamp in RFC 3339 format

      - `BetaManagedAgentsMcpOAuthRefreshResponse? Refresh`

        OAuth refresh token configuration returned in credential responses.

        - `required string ClientID`

          OAuth client ID.

        - `required string TokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `required TokenEndpointAuth TokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `required Type Type`

              - `"none"None`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `required Type Type`

              - `"client_secret_basic"ClientSecretBasic`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `required Type Type`

              - `"client_secret_post"ClientSecretPost`

        - `string? Resource`

          OAuth resource indicator.

        - `string? Scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

        - `"static_bearer"StaticBearer`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `required BetaManagedAgentsInjectionLocationResponse InjectionLocation`

        Where in the outbound request the secret value is substituted.

        - `required Boolean Body`

          Whether the placeholder is substituted in the request body.

        - `required Boolean Header`

          Whether the placeholder is substituted in request header values.

      - `required Networking Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `required Type Type`

            - `"unrestricted"Unrestricted`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `required IReadOnlyList<string> AllowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `required Type Type`

            - `"limited"Limited`

      - `required string SecretName`

        Name of the environment variable.

      - `required Type Type`

        - `"environment_variable"EnvironmentVariable`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the credential.

  - `required Type Type`

    - `"vault_credential"VaultCredential`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required string VaultID`

    Identifier of the vault this credential belongs to.

  - `string? DisplayName`

    Human-readable name for the credential.

### Example

```csharp
CredentialUpdateParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYOQfSkw",
};

var betaManagedAgentsCredential = await client.Beta.Vaults.Credentials.Update(parameters);

Console.WriteLine(betaManagedAgentsCredential);
```

#### Response

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

## Delete Credential

`BetaManagedAgentsDeletedCredential Beta.Vaults.Credentials.Delete(CredentialDeleteParamsparameters, CancellationTokencancellationToken = default)`

**delete** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

### Parameters

- `CredentialDeleteParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `required string credentialID`

    Path param: Path parameter credential_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsDeletedCredential:`

  Confirmation of a deleted credential.

  - `required string ID`

    Unique identifier of the deleted credential.

  - `required Type Type`

    - `"vault_credential_deleted"VaultCredentialDeleted`

### Example

```csharp
CredentialDeleteParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYOQfSkw",
};

var betaManagedAgentsDeletedCredential = await client.Beta.Vaults.Credentials.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeletedCredential);
```

#### Response

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

## Archive Credential

`BetaManagedAgentsCredential Beta.Vaults.Credentials.Archive(CredentialArchiveParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

### Parameters

- `CredentialArchiveParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `required string credentialID`

    Path param: Path parameter credential_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `required string ID`

    Unique identifier for the credential.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required Auth Auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

        - `"mcp_oauth"McpOAuth`

      - `DateTimeOffset? ExpiresAt`

        A timestamp in RFC 3339 format

      - `BetaManagedAgentsMcpOAuthRefreshResponse? Refresh`

        OAuth refresh token configuration returned in credential responses.

        - `required string ClientID`

          OAuth client ID.

        - `required string TokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `required TokenEndpointAuth TokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `required Type Type`

              - `"none"None`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `required Type Type`

              - `"client_secret_basic"ClientSecretBasic`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `required Type Type`

              - `"client_secret_post"ClientSecretPost`

        - `string? Resource`

          OAuth resource indicator.

        - `string? Scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

        - `"static_bearer"StaticBearer`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `required BetaManagedAgentsInjectionLocationResponse InjectionLocation`

        Where in the outbound request the secret value is substituted.

        - `required Boolean Body`

          Whether the placeholder is substituted in the request body.

        - `required Boolean Header`

          Whether the placeholder is substituted in request header values.

      - `required Networking Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `required Type Type`

            - `"unrestricted"Unrestricted`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `required IReadOnlyList<string> AllowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `required Type Type`

            - `"limited"Limited`

      - `required string SecretName`

        Name of the environment variable.

      - `required Type Type`

        - `"environment_variable"EnvironmentVariable`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the credential.

  - `required Type Type`

    - `"vault_credential"VaultCredential`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required string VaultID`

    Identifier of the vault this credential belongs to.

  - `string? DisplayName`

    Human-readable name for the credential.

### Example

```csharp
CredentialArchiveParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYOQfSkw",
};

var betaManagedAgentsCredential = await client.Beta.Vaults.Credentials.Archive(parameters);

Console.WriteLine(betaManagedAgentsCredential);
```

#### Response

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

## Validate Credential

`BetaManagedAgentsCredentialValidation Beta.Vaults.Credentials.McpOAuthValidate(CredentialMcpOAuthValidateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

### Parameters

- `CredentialMcpOAuthValidateParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `required string credentialID`

    Path param: Path parameter credential_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsCredentialValidation:`

  Result of live-probing a credential against its configured MCP server.

  - `required string CredentialID`

    Unique identifier of the credential that was validated.

  - `required Boolean HasRefreshToken`

    Whether the credential has a refresh token configured.

  - `required BetaManagedAgentsMcpProbe? McpProbe`

    The failing step of an MCP validation probe.

    - `required BetaManagedAgentsRefreshHttpResponse? HttpResponse`

      An HTTP response captured during a credential validation probe.

      - `required string Body`

        Response body. May be truncated and has sensitive values scrubbed.

      - `required Boolean BodyTruncated`

        Whether `body` was truncated.

      - `required string ContentType`

        Value of the `Content-Type` response header.

      - `required Int StatusCode`

        HTTP status code.

    - `required string Method`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `required BetaManagedAgentsRefreshObject? Refresh`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `required BetaManagedAgentsRefreshHttpResponse? HttpResponse`

      An HTTP response captured during a credential validation probe.

    - `required Status Status`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `"succeeded"Succeeded`

      - `"failed"Failed`

      - `"connect_error"ConnectError`

      - `"no_refresh_token"NoRefreshToken`

  - `required BetaManagedAgentsCredentialValidationStatus Status`

    Overall verdict of a credential validation probe.

    - `"valid"Valid`

    - `"invalid"Invalid`

    - `"unknown"Unknown`

  - `required Type Type`

    - `"vault_credential_validation"VaultCredentialValidation`

  - `required DateTimeOffset ValidatedAt`

    A timestamp in RFC 3339 format

  - `required string VaultID`

    Identifier of the vault containing the credential.

### Example

```csharp
CredentialMcpOAuthValidateParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYOQfSkw",
};

var betaManagedAgentsCredentialValidation = await client.Beta.Vaults.Credentials.McpOAuthValidate(parameters);

Console.WriteLine(betaManagedAgentsCredentialValidation);
```

#### Response

```json
{
  "credential_id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "has_refresh_token": true,
  "mcp_probe": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "method": "method"
  },
  "refresh": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "status": "succeeded"
  },
  "status": "valid",
  "type": "vault_credential_validation",
  "validated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv"
}
```

## Domain Types

### Beta Managed Agents Credential

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `required string ID`

    Unique identifier for the credential.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required Auth Auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

        - `"mcp_oauth"McpOAuth`

      - `DateTimeOffset? ExpiresAt`

        A timestamp in RFC 3339 format

      - `BetaManagedAgentsMcpOAuthRefreshResponse? Refresh`

        OAuth refresh token configuration returned in credential responses.

        - `required string ClientID`

          OAuth client ID.

        - `required string TokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `required TokenEndpointAuth TokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `required Type Type`

              - `"none"None`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `required Type Type`

              - `"client_secret_basic"ClientSecretBasic`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `required Type Type`

              - `"client_secret_post"ClientSecretPost`

        - `string? Resource`

          OAuth resource indicator.

        - `string? Scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

        - `"static_bearer"StaticBearer`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `required BetaManagedAgentsInjectionLocationResponse InjectionLocation`

        Where in the outbound request the secret value is substituted.

        - `required Boolean Body`

          Whether the placeholder is substituted in the request body.

        - `required Boolean Header`

          Whether the placeholder is substituted in request header values.

      - `required Networking Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `required Type Type`

            - `"unrestricted"Unrestricted`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `required IReadOnlyList<string> AllowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `required Type Type`

            - `"limited"Limited`

      - `required string SecretName`

        Name of the environment variable.

      - `required Type Type`

        - `"environment_variable"EnvironmentVariable`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the credential.

  - `required Type Type`

    - `"vault_credential"VaultCredential`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required string VaultID`

    Identifier of the vault this credential belongs to.

  - `string? DisplayName`

    Human-readable name for the credential.

### Beta Managed Agents Credential Networking Params

- `class BetaManagedAgentsCredentialNetworkingParams: A class that can be one of several variants.union`

  Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

  - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:`

    Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

    - `required Type Type`

      - `"unrestricted"Unrestricted`

  - `class BetaManagedAgentsLimitedCredentialNetworkingParams:`

    Substitute the secret only on requests to the listed hosts.

    - `required IReadOnlyList<string> AllowedHosts`

      Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

    - `required Type Type`

      - `"limited"Limited`

### Beta Managed Agents Credential Validation

- `class BetaManagedAgentsCredentialValidation:`

  Result of live-probing a credential against its configured MCP server.

  - `required string CredentialID`

    Unique identifier of the credential that was validated.

  - `required Boolean HasRefreshToken`

    Whether the credential has a refresh token configured.

  - `required BetaManagedAgentsMcpProbe? McpProbe`

    The failing step of an MCP validation probe.

    - `required BetaManagedAgentsRefreshHttpResponse? HttpResponse`

      An HTTP response captured during a credential validation probe.

      - `required string Body`

        Response body. May be truncated and has sensitive values scrubbed.

      - `required Boolean BodyTruncated`

        Whether `body` was truncated.

      - `required string ContentType`

        Value of the `Content-Type` response header.

      - `required Int StatusCode`

        HTTP status code.

    - `required string Method`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `required BetaManagedAgentsRefreshObject? Refresh`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `required BetaManagedAgentsRefreshHttpResponse? HttpResponse`

      An HTTP response captured during a credential validation probe.

    - `required Status Status`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `"succeeded"Succeeded`

      - `"failed"Failed`

      - `"connect_error"ConnectError`

      - `"no_refresh_token"NoRefreshToken`

  - `required BetaManagedAgentsCredentialValidationStatus Status`

    Overall verdict of a credential validation probe.

    - `"valid"Valid`

    - `"invalid"Invalid`

    - `"unknown"Unknown`

  - `required Type Type`

    - `"vault_credential_validation"VaultCredentialValidation`

  - `required DateTimeOffset ValidatedAt`

    A timestamp in RFC 3339 format

  - `required string VaultID`

    Identifier of the vault containing the credential.

### Beta Managed Agents Credential Validation Status

- `enum BetaManagedAgentsCredentialValidationStatus:`

  Overall verdict of a credential validation probe.

  - `"valid"Valid`

  - `"invalid"Invalid`

  - `"unknown"Unknown`

### Beta Managed Agents Deleted Credential

- `class BetaManagedAgentsDeletedCredential:`

  Confirmation of a deleted credential.

  - `required string ID`

    Unique identifier of the deleted credential.

  - `required Type Type`

    - `"vault_credential_deleted"VaultCredentialDeleted`

### Beta Managed Agents Environment Variable Auth Response

- `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

  Environment variable credential details. The secret value is never returned.

  - `required BetaManagedAgentsInjectionLocationResponse InjectionLocation`

    Where in the outbound request the secret value is substituted.

    - `required Boolean Body`

      Whether the placeholder is substituted in the request body.

    - `required Boolean Header`

      Whether the placeholder is substituted in request header values.

  - `required Networking Networking`

    Outbound hosts the secret value is substituted on.

    - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

      The secret is substituted on any host the session's Environment network policy permits egress to.

      - `required Type Type`

        - `"unrestricted"Unrestricted`

    - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

      The secret is substituted only on requests to the listed hosts.

      - `required IReadOnlyList<string> AllowedHosts`

        Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

      - `required Type Type`

        - `"limited"Limited`

  - `required string SecretName`

    Name of the environment variable.

  - `required Type Type`

    - `"environment_variable"EnvironmentVariable`

### Beta Managed Agents Environment Variable Create Params

- `class BetaManagedAgentsEnvironmentVariableCreateParams:`

  Parameters for creating an environment variable credential.

  - `required BetaManagedAgentsCredentialNetworkingParams Networking`

    Outbound hosts the secret value is substituted on.

    - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:`

      Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

      - `required Type Type`

        - `"unrestricted"Unrestricted`

    - `class BetaManagedAgentsLimitedCredentialNetworkingParams:`

      Substitute the secret only on requests to the listed hosts.

      - `required IReadOnlyList<string> AllowedHosts`

        Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

      - `required Type Type`

        - `"limited"Limited`

  - `required string SecretName`

    Name of the environment variable. Immutable after create.

  - `required string SecretValue`

    Secret value. Write-only; never returned in responses.

  - `required Type Type`

    - `"environment_variable"EnvironmentVariable`

  - `BetaManagedAgentsInjectionLocationParams InjectionLocation`

    Where in the outbound request the secret value may be substituted.

    - `Boolean Body`

      Substitute when the placeholder appears in the request body.

    - `Boolean Header`

      Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Environment Variable Update Params

- `class BetaManagedAgentsEnvironmentVariableUpdateParams:`

  Parameters for updating an environment variable credential. `secret_name` is immutable.

  - `required Type Type`

    - `"environment_variable"EnvironmentVariable`

  - `BetaManagedAgentsInjectionLocationUpdateParams InjectionLocation`

    Updated injection location.

    - `Boolean Body`

      Substitute when the placeholder appears in the request body.

    - `Boolean Header`

      Substitute when the placeholder appears in a request header value.

  - `BetaManagedAgentsCredentialNetworkingParams? Networking`

    Updated networking scope. Full replacement.

    - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:`

      Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

      - `required Type Type`

        - `"unrestricted"Unrestricted`

    - `class BetaManagedAgentsLimitedCredentialNetworkingParams:`

      Substitute the secret only on requests to the listed hosts.

      - `required IReadOnlyList<string> AllowedHosts`

        Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

      - `required Type Type`

        - `"limited"Limited`

  - `string? SecretValue`

    Updated secret value.

### Beta Managed Agents Injection Location Params

- `class BetaManagedAgentsInjectionLocationParams:`

  Where in the outbound request the secret value may be substituted.

  - `Boolean Body`

    Substitute when the placeholder appears in the request body.

  - `Boolean Header`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Injection Location Response

- `class BetaManagedAgentsInjectionLocationResponse:`

  Where in the outbound request the secret value is substituted.

  - `required Boolean Body`

    Whether the placeholder is substituted in the request body.

  - `required Boolean Header`

    Whether the placeholder is substituted in request header values.

### Beta Managed Agents Injection Location Update Params

- `class BetaManagedAgentsInjectionLocationUpdateParams:`

  Updated injection location.

  - `Boolean Body`

    Substitute when the placeholder appears in the request body.

  - `Boolean Header`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Limited Credential Networking Params

- `class BetaManagedAgentsLimitedCredentialNetworkingParams:`

  Substitute the secret only on requests to the listed hosts.

  - `required IReadOnlyList<string> AllowedHosts`

    Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

  - `required Type Type`

    - `"limited"Limited`

### Beta Managed Agents Limited Credential Networking Response

- `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

  The secret is substituted only on requests to the listed hosts.

  - `required IReadOnlyList<string> AllowedHosts`

    Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

  - `required Type Type`

    - `"limited"Limited`

### Beta Managed Agents MCP OAuth Auth Response

- `class BetaManagedAgentsMcpOAuthAuthResponse:`

  OAuth credential details for an MCP server.

  - `required string McpServerUrl`

    URL of the MCP server this credential authenticates against.

  - `required Type Type`

    - `"mcp_oauth"McpOAuth`

  - `DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsMcpOAuthRefreshResponse? Refresh`

    OAuth refresh token configuration returned in credential responses.

    - `required string ClientID`

      OAuth client ID.

    - `required string TokenEndpoint`

      Token endpoint URL used to refresh the access token.

    - `required TokenEndpointAuth TokenEndpointAuth`

      Token endpoint requires no client authentication.

      - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

        Token endpoint requires no client authentication.

        - `required Type Type`

          - `"none"None`

      - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `required Type Type`

          - `"client_secret_basic"ClientSecretBasic`

      - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

        Token endpoint uses POST body authentication with client credentials.

        - `required Type Type`

          - `"client_secret_post"ClientSecretPost`

    - `string? Resource`

      OAuth resource indicator.

    - `string? Scope`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Create Params

- `class BetaManagedAgentsMcpOAuthCreateParams:`

  Parameters for creating an MCP OAuth credential.

  - `required string AccessToken`

    OAuth access token.

  - `required string McpServerUrl`

    URL of the MCP server this credential authenticates against.

  - `required Type Type`

    - `"mcp_oauth"McpOAuth`

  - `DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsMcpOAuthRefreshParams? Refresh`

    OAuth refresh token parameters for creating a credential with refresh support.

    - `required string ClientID`

      OAuth client ID.

    - `required string RefreshToken`

      OAuth refresh token.

    - `required string TokenEndpoint`

      Token endpoint URL used to refresh the access token.

    - `required TokenEndpointAuth TokenEndpointAuth`

      Token endpoint requires no client authentication.

      - `class BetaManagedAgentsTokenEndpointAuthNoneParam:`

        Token endpoint requires no client authentication.

        - `required Type Type`

          - `"none"None`

      - `class BetaManagedAgentsTokenEndpointAuthBasicParam:`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `required string ClientSecret`

          OAuth client secret.

        - `required Type Type`

          - `"client_secret_basic"ClientSecretBasic`

      - `class BetaManagedAgentsTokenEndpointAuthPostParam:`

        Token endpoint uses POST body authentication with client credentials.

        - `required string ClientSecret`

          OAuth client secret.

        - `required Type Type`

          - `"client_secret_post"ClientSecretPost`

    - `string? Resource`

      OAuth resource indicator.

    - `string? Scope`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Params

- `class BetaManagedAgentsMcpOAuthRefreshParams:`

  OAuth refresh token parameters for creating a credential with refresh support.

  - `required string ClientID`

    OAuth client ID.

  - `required string RefreshToken`

    OAuth refresh token.

  - `required string TokenEndpoint`

    Token endpoint URL used to refresh the access token.

  - `required TokenEndpointAuth TokenEndpointAuth`

    Token endpoint requires no client authentication.

    - `class BetaManagedAgentsTokenEndpointAuthNoneParam:`

      Token endpoint requires no client authentication.

      - `required Type Type`

        - `"none"None`

    - `class BetaManagedAgentsTokenEndpointAuthBasicParam:`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `required string ClientSecret`

        OAuth client secret.

      - `required Type Type`

        - `"client_secret_basic"ClientSecretBasic`

    - `class BetaManagedAgentsTokenEndpointAuthPostParam:`

      Token endpoint uses POST body authentication with client credentials.

      - `required string ClientSecret`

        OAuth client secret.

      - `required Type Type`

        - `"client_secret_post"ClientSecretPost`

  - `string? Resource`

    OAuth resource indicator.

  - `string? Scope`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Response

- `class BetaManagedAgentsMcpOAuthRefreshResponse:`

  OAuth refresh token configuration returned in credential responses.

  - `required string ClientID`

    OAuth client ID.

  - `required string TokenEndpoint`

    Token endpoint URL used to refresh the access token.

  - `required TokenEndpointAuth TokenEndpointAuth`

    Token endpoint requires no client authentication.

    - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

      Token endpoint requires no client authentication.

      - `required Type Type`

        - `"none"None`

    - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `required Type Type`

        - `"client_secret_basic"ClientSecretBasic`

    - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

      Token endpoint uses POST body authentication with client credentials.

      - `required Type Type`

        - `"client_secret_post"ClientSecretPost`

  - `string? Resource`

    OAuth resource indicator.

  - `string? Scope`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Update Params

- `class BetaManagedAgentsMcpOAuthRefreshUpdateParams:`

  Parameters for updating OAuth refresh token configuration.

  - `string? RefreshToken`

    Updated OAuth refresh token.

  - `string? Scope`

    Updated OAuth scope for the refresh request.

  - `TokenEndpointAuth TokenEndpointAuth`

    Updated HTTP Basic authentication parameters for the token endpoint.

    - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `required Type Type`

        - `"client_secret_basic"ClientSecretBasic`

      - `string? ClientSecret`

        Updated OAuth client secret.

    - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:`

      Updated POST body authentication parameters for the token endpoint.

      - `required Type Type`

        - `"client_secret_post"ClientSecretPost`

      - `string? ClientSecret`

        Updated OAuth client secret.

### Beta Managed Agents MCP OAuth Update Params

- `class BetaManagedAgentsMcpOAuthUpdateParams:`

  Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

  - `required Type Type`

    - `"mcp_oauth"McpOAuth`

  - `string? AccessToken`

    Updated OAuth access token.

  - `DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsMcpOAuthRefreshUpdateParams? Refresh`

    Parameters for updating OAuth refresh token configuration.

    - `string? RefreshToken`

      Updated OAuth refresh token.

    - `string? Scope`

      Updated OAuth scope for the refresh request.

    - `TokenEndpointAuth TokenEndpointAuth`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:`

        Updated HTTP Basic authentication parameters for the token endpoint.

        - `required Type Type`

          - `"client_secret_basic"ClientSecretBasic`

        - `string? ClientSecret`

          Updated OAuth client secret.

      - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:`

        Updated POST body authentication parameters for the token endpoint.

        - `required Type Type`

          - `"client_secret_post"ClientSecretPost`

        - `string? ClientSecret`

          Updated OAuth client secret.

### Beta Managed Agents MCP Probe

- `class BetaManagedAgentsMcpProbe:`

  The failing step of an MCP validation probe.

  - `required BetaManagedAgentsRefreshHttpResponse? HttpResponse`

    An HTTP response captured during a credential validation probe.

    - `required string Body`

      Response body. May be truncated and has sensitive values scrubbed.

    - `required Boolean BodyTruncated`

      Whether `body` was truncated.

    - `required string ContentType`

      Value of the `Content-Type` response header.

    - `required Int StatusCode`

      HTTP status code.

  - `required string Method`

    The MCP method that failed (for example `initialize` or `tools/list`).

### Beta Managed Agents Refresh HTTP Response

- `class BetaManagedAgentsRefreshHttpResponse:`

  An HTTP response captured during a credential validation probe.

  - `required string Body`

    Response body. May be truncated and has sensitive values scrubbed.

  - `required Boolean BodyTruncated`

    Whether `body` was truncated.

  - `required string ContentType`

    Value of the `Content-Type` response header.

  - `required Int StatusCode`

    HTTP status code.

### Beta Managed Agents Refresh Object

- `class BetaManagedAgentsRefreshObject:`

  Outcome of a refresh-token exchange attempted during credential validation.

  - `required BetaManagedAgentsRefreshHttpResponse? HttpResponse`

    An HTTP response captured during a credential validation probe.

    - `required string Body`

      Response body. May be truncated and has sensitive values scrubbed.

    - `required Boolean BodyTruncated`

      Whether `body` was truncated.

    - `required string ContentType`

      Value of the `Content-Type` response header.

    - `required Int StatusCode`

      HTTP status code.

  - `required Status Status`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `"succeeded"Succeeded`

    - `"failed"Failed`

    - `"connect_error"ConnectError`

    - `"no_refresh_token"NoRefreshToken`

### Beta Managed Agents Static Bearer Auth Response

- `class BetaManagedAgentsStaticBearerAuthResponse:`

  Static bearer token credential details for an MCP server.

  - `required string McpServerUrl`

    URL of the MCP server this credential authenticates against.

  - `required Type Type`

    - `"static_bearer"StaticBearer`

### Beta Managed Agents Static Bearer Create Params

- `class BetaManagedAgentsStaticBearerCreateParams:`

  Parameters for creating a static bearer token credential.

  - `required string Token`

    Static bearer token value.

  - `required string McpServerUrl`

    URL of the MCP server this credential authenticates against.

  - `required Type Type`

    - `"static_bearer"StaticBearer`

### Beta Managed Agents Static Bearer Update Params

- `class BetaManagedAgentsStaticBearerUpdateParams:`

  Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

  - `required Type Type`

    - `"static_bearer"StaticBearer`

  - `string? Token`

    Updated static bearer token value.

### Beta Managed Agents Token Endpoint Auth Basic Param

- `class BetaManagedAgentsTokenEndpointAuthBasicParam:`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `required string ClientSecret`

    OAuth client secret.

  - `required Type Type`

    - `"client_secret_basic"ClientSecretBasic`

### Beta Managed Agents Token Endpoint Auth Basic Response

- `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `required Type Type`

    - `"client_secret_basic"ClientSecretBasic`

### Beta Managed Agents Token Endpoint Auth Basic Update Param

- `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:`

  Updated HTTP Basic authentication parameters for the token endpoint.

  - `required Type Type`

    - `"client_secret_basic"ClientSecretBasic`

  - `string? ClientSecret`

    Updated OAuth client secret.

### Beta Managed Agents Token Endpoint Auth None Param

- `class BetaManagedAgentsTokenEndpointAuthNoneParam:`

  Token endpoint requires no client authentication.

  - `required Type Type`

    - `"none"None`

### Beta Managed Agents Token Endpoint Auth None Response

- `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

  Token endpoint requires no client authentication.

  - `required Type Type`

    - `"none"None`

### Beta Managed Agents Token Endpoint Auth Post Param

- `class BetaManagedAgentsTokenEndpointAuthPostParam:`

  Token endpoint uses POST body authentication with client credentials.

  - `required string ClientSecret`

    OAuth client secret.

  - `required Type Type`

    - `"client_secret_post"ClientSecretPost`

### Beta Managed Agents Token Endpoint Auth Post Response

- `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

  Token endpoint uses POST body authentication with client credentials.

  - `required Type Type`

    - `"client_secret_post"ClientSecretPost`

### Beta Managed Agents Token Endpoint Auth Post Update Param

- `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:`

  Updated POST body authentication parameters for the token endpoint.

  - `required Type Type`

    - `"client_secret_post"ClientSecretPost`

  - `string? ClientSecret`

    Updated OAuth client secret.

### Beta Managed Agents Unrestricted Credential Networking Params

- `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:`

  Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

  - `required Type Type`

    - `"unrestricted"Unrestricted`

### Beta Managed Agents Unrestricted Credential Networking Response

- `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

  The secret is substituted on any host the session's Environment network policy permits egress to.

  - `required Type Type`

    - `"unrestricted"Unrestricted`

# Memory Stores

## Create a memory store

`BetaManagedAgentsMemoryStore Beta.MemoryStores.Create(MemoryStoreCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/memory_stores`

Create a memory store

### Parameters

- `MemoryStoreCreateParams parameters`

  - `required string name`

    Body param: Human-readable name for the store. Required; 1–255 characters; no control characters. The mount-path slug under `/mnt/memory/` is derived from this name (lowercased, non-alphanumeric runs collapsed to a hyphen). Names need not be unique within a workspace.

  - `string description`

    Body param: Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent.

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Not visible to the agent.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `required string ID`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string Name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `required Type Type`

    - `"memory_store"MemoryStore`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `string Description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```csharp
MemoryStoreCreateParams parameters = new() { Name = "x" };

var betaManagedAgentsMemoryStore = await client.Beta.MemoryStores.Create(parameters);

Console.WriteLine(betaManagedAgentsMemoryStore);
```

#### Response

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  }
}
```

## List memory stores

`MemoryStoreListPageResponse Beta.MemoryStores.List(MemoryStoreListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/memory_stores`

List memory stores

### Parameters

- `MemoryStoreListParams parameters`

  - `DateTimeOffset createdAtGte`

    Query param: Return only stores whose `created_at` is at or after this time (inclusive). Sent on the wire as `created_at[gte]`.

  - `DateTimeOffset createdAtLte`

    Query param: Return only stores whose `created_at` is at or before this time (inclusive). Sent on the wire as `created_at[lte]`.

  - `Boolean includeArchived`

    Query param: When `true`, archived stores are included in the results. Defaults to `false` (archived stores are excluded).

  - `Int limit`

    Query param: Maximum number of stores to return per page. Must be between 1 and 100. Defaults to 20 when omitted.

  - `string page`

    Query param: Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class MemoryStoreListPageResponse:`

  A page of `memory_store` results, ordered by `created_at` descending (newest first).

  - `IReadOnlyList<BetaManagedAgentsMemoryStore> Data`

    Memory stores on this page, newest first. Empty when there are no stores matching the filters.

    - `required string ID`

      Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required string Name`

      Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

    - `required Type Type`

      - `"memory_store"MemoryStore`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

    - `DateTimeOffset? ArchivedAt`

      A timestamp in RFC 3339 format

    - `string Description`

      Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

    - `IReadOnlyDictionary<string, string> Metadata`

      Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

  - `string? NextPage`

    Opaque cursor for the next page (a `page_...` value). Pass as `page` on the next request. `null` when there are no more results.

### Example

```csharp
MemoryStoreListParams parameters = new();

var page = await client.Beta.MemoryStores.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "name": "name",
      "type": "memory_store",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "description": "description",
      "metadata": {
        "foo": "string"
      }
    }
  ],
  "next_page": "next_page"
}
```

## Retrieve a memory store

`BetaManagedAgentsMemoryStore Beta.MemoryStores.Retrieve(MemoryStoreRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/memory_stores/{memory_store_id}`

Retrieve a memory store

### Parameters

- `MemoryStoreRetrieveParams parameters`

  - `required string memoryStoreID`

    Path parameter memory_store_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `required string ID`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string Name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `required Type Type`

    - `"memory_store"MemoryStore`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `string Description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```csharp
MemoryStoreRetrieveParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var betaManagedAgentsMemoryStore = await client.Beta.MemoryStores.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsMemoryStore);
```

#### Response

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  }
}
```

## Update a memory store

`BetaManagedAgentsMemoryStore Beta.MemoryStores.Update(MemoryStoreUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/memory_stores/{memory_store_id}`

Update a memory store

### Parameters

- `MemoryStoreUpdateParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `string? description`

    Body param: New description for the store, up to 1024 characters. Pass an empty string to clear it.

  - `IReadOnlyDictionary<string, string>? metadata`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `string? name`

    Body param: New human-readable name for the store. 1–255 characters; no control characters. Renaming changes the slug used for the store's `mount_path` in sessions created after the update.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `required string ID`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string Name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `required Type Type`

    - `"memory_store"MemoryStore`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `string Description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```csharp
MemoryStoreUpdateParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var betaManagedAgentsMemoryStore = await client.Beta.MemoryStores.Update(parameters);

Console.WriteLine(betaManagedAgentsMemoryStore);
```

#### Response

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  }
}
```

## Delete a memory store

`BetaManagedAgentsDeletedMemoryStore Beta.MemoryStores.Delete(MemoryStoreDeleteParamsparameters, CancellationTokencancellationToken = default)`

**delete** `/v1/memory_stores/{memory_store_id}`

Delete a memory store

### Parameters

- `MemoryStoreDeleteParams parameters`

  - `required string memoryStoreID`

    Path parameter memory_store_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsDeletedMemoryStore:`

  Confirmation that a `memory_store` was deleted.

  - `required string ID`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `required Type Type`

    - `"memory_store_deleted"MemoryStoreDeleted`

### Example

```csharp
MemoryStoreDeleteParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var betaManagedAgentsDeletedMemoryStore = await client.Beta.MemoryStores.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeletedMemoryStore);
```

#### Response

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

## Archive a memory store

`BetaManagedAgentsMemoryStore Beta.MemoryStores.Archive(MemoryStoreArchiveParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/memory_stores/{memory_store_id}/archive`

Archive a memory store

### Parameters

- `MemoryStoreArchiveParams parameters`

  - `required string memoryStoreID`

    Path parameter memory_store_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `required string ID`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string Name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `required Type Type`

    - `"memory_store"MemoryStore`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `string Description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```csharp
MemoryStoreArchiveParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var betaManagedAgentsMemoryStore = await client.Beta.MemoryStores.Archive(parameters);

Console.WriteLine(betaManagedAgentsMemoryStore);
```

#### Response

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  }
}
```

## Domain Types

### Beta Managed Agents Deleted Memory Store

- `class BetaManagedAgentsDeletedMemoryStore:`

  Confirmation that a `memory_store` was deleted.

  - `required string ID`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `required Type Type`

    - `"memory_store_deleted"MemoryStoreDeleted`

### Beta Managed Agents Memory Store

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `required string ID`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string Name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `required Type Type`

    - `"memory_store"MemoryStore`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `string Description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

# Memories

## Create a memory

`BetaManagedAgentsMemory Beta.MemoryStores.Memories.Create(MemoryCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/memory_stores/{memory_store_id}/memories`

Create a memory

### Parameters

- `MemoryCreateParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string? content`

    Body param: UTF-8 text content for the new memory. Maximum 100 kB (102,400 bytes). Required; pass `""` explicitly to create an empty memory.

  - `required string path`

    Body param: Hierarchical path for the new memory, e.g. `/projects/foo/notes.md`. Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive.

  - `BetaManagedAgentsMemoryView view`

    Query param: Query parameter for view

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsMemory:`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `required string ID`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `required string ContentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `required Int ContentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string MemoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `required string MemoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `required string Path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `required Type Type`

    - `"memory"Memory`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `string? Content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```csharp
MemoryCreateParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    Content = "content",
    Path = "xx",
};

var betaManagedAgentsMemory = await client.Beta.MemoryStores.Memories.Create(parameters);

Console.WriteLine(betaManagedAgentsMemory);
```

#### Response

```json
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

## List memories

`MemoryListPageResponse Beta.MemoryStores.Memories.List(MemoryListParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/memory_stores/{memory_store_id}/memories`

List memories

### Parameters

- `MemoryListParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `Int depth`

    Query param: `0` (or omitted) returns all descendants below `path_prefix` (recursive). `1` returns immediate children only; deeper entries roll up as `memory_prefix` items. `depth=1` behaves like `ls`; omitting `depth` behaves like `find`.

  - `Int limit`

    Query param: Maximum number of items to return per page. Must be between 1 and 100. Defaults to 20 when omitted. Capped at 20 when `view=full`. Both `memory` and `memory_prefix` items count toward the limit.

  - `string page`

    Query param: Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

  - `string pathPrefix`

    Query param: Optional path prefix filter. Must end with `/` (segment-aligned), e.g., `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

  - `BetaManagedAgentsMemoryView view`

    Query param: Which projection of each `memory` to return. Defaults to `basic` (content omitted). `full` populates `content` on each item and caps `limit` at 20; use this as the bulk-read path for export and sync.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class MemoryListPageResponse:`

  Response payload for [List memories](/docs/en/api/beta/memory_stores/memories/list).

  - `IReadOnlyList<BetaManagedAgentsMemoryListItem> Data`

    One page of results. Each item is either a `memory` object or, when `depth` was set, a `memory_prefix` rollup marker. Items are returned in a stable, server-defined order.

    - `class BetaManagedAgentsMemory:`

      A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

      - `required string ID`

        Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

      - `required string ContentSha256`

        Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

      - `required Int ContentSizeBytes`

        Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

      - `required DateTimeOffset CreatedAt`

        A timestamp in RFC 3339 format

      - `required string MemoryStoreID`

        ID of the memory store this memory belongs to (a `memstore_...` value).

      - `required string MemoryVersionID`

        ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

      - `required string Path`

        Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

      - `required Type Type`

        - `"memory"Memory`

      - `required DateTimeOffset UpdatedAt`

        A timestamp in RFC 3339 format

      - `string? Content`

        The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

    - `class BetaManagedAgentsMemoryPrefix:`

      A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

      - `required string Path`

        The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

      - `required Type Type`

        - `"memory_prefix"MemoryPrefix`

  - `string? NextPage`

    Opaque cursor for the next page (a `page_...` value), or `null` if there are no more results. Pass as `page` on the next request.

### Example

```csharp
MemoryListParams parameters = new() { MemoryStoreID = "memory_store_id" };

var page = await client.Beta.MemoryStores.Memories.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "content_sha256": "content_sha256",
      "content_size_bytes": 0,
      "created_at": "2019-12-27T18:11:19.117Z",
      "memory_store_id": "memory_store_id",
      "memory_version_id": "memory_version_id",
      "path": "path",
      "type": "memory",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "content": "content"
    }
  ],
  "next_page": "next_page"
}
```

## Retrieve a memory

`BetaManagedAgentsMemory Beta.MemoryStores.Memories.Retrieve(MemoryRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a memory

### Parameters

- `MemoryRetrieveParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string memoryID`

    Path param: Path parameter memory_id

  - `BetaManagedAgentsMemoryView view`

    Query param: Query parameter for view

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsMemory:`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `required string ID`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `required string ContentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `required Int ContentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string MemoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `required string MemoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `required string Path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `required Type Type`

    - `"memory"Memory`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `string? Content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```csharp
MemoryRetrieveParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryID = "memory_id",
};

var betaManagedAgentsMemory = await client.Beta.MemoryStores.Memories.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsMemory);
```

#### Response

```json
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

## Update a memory

`BetaManagedAgentsMemory Beta.MemoryStores.Memories.Update(MemoryUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a memory

### Parameters

- `MemoryUpdateParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string memoryID`

    Path param: Path parameter memory_id

  - `BetaManagedAgentsMemoryView view`

    Query param: Query parameter for view

  - `string? content`

    Body param: New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update).

  - `string? path`

    Body param: New path for the memory (a rename). Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive. The memory's `id` is preserved across renames. Omit to leave the path unchanged.

  - `BetaManagedAgentsPrecondition precondition`

    Body param: Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsMemory:`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `required string ID`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `required string ContentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `required Int ContentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string MemoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `required string MemoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `required string Path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `required Type Type`

    - `"memory"Memory`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `string? Content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```csharp
MemoryUpdateParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryID = "memory_id",
};

var betaManagedAgentsMemory = await client.Beta.MemoryStores.Memories.Update(parameters);

Console.WriteLine(betaManagedAgentsMemory);
```

#### Response

```json
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

## Delete a memory

`BetaManagedAgentsDeletedMemory Beta.MemoryStores.Memories.Delete(MemoryDeleteParamsparameters, CancellationTokencancellationToken = default)`

**delete** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a memory

### Parameters

- `MemoryDeleteParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string memoryID`

    Path param: Path parameter memory_id

  - `string expectedContentSha256`

    Query param: Query parameter for expected_content_sha256

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsDeletedMemory:`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

  - `required string ID`

    ID of the deleted memory (a `mem_...` value).

  - `required Type Type`

    - `"memory_deleted"MemoryDeleted`

### Example

```csharp
MemoryDeleteParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryID = "memory_id",
};

var betaManagedAgentsDeletedMemory = await client.Beta.MemoryStores.Memories.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeletedMemory);
```

#### Response

```json
{
  "id": "id",
  "type": "memory_deleted"
}
```

## Domain Types

### Beta Managed Agents Conflict Error

- `class BetaManagedAgentsConflictError:`

  - `required Type Type`

    - `"conflict_error"ConflictError`

  - `string Message`

### Beta Managed Agents Content Sha256 Precondition

- `class BetaManagedAgentsContentSha256Precondition:`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `required Type Type`

    - `"content_sha256"ContentSha256`

  - `string ContentSha256`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

### Beta Managed Agents Deleted Memory

- `class BetaManagedAgentsDeletedMemory:`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

  - `required string ID`

    ID of the deleted memory (a `mem_...` value).

  - `required Type Type`

    - `"memory_deleted"MemoryDeleted`

### Beta Managed Agents Error

- `class BetaManagedAgentsError: A class that can be one of several variants.union`

  - `class BetaInvalidRequestError:`

    - `required string Message`

    - `JsonElement Type "invalid_request_error"constant`

  - `class BetaAuthenticationError:`

    - `required string Message`

    - `JsonElement Type "authentication_error"constant`

  - `class BetaBillingError:`

    - `required string Message`

    - `JsonElement Type "billing_error"constant`

  - `class BetaPermissionError:`

    - `required string Message`

    - `JsonElement Type "permission_error"constant`

  - `class BetaNotFoundError:`

    - `required string Message`

    - `JsonElement Type "not_found_error"constant`

  - `class BetaRateLimitError:`

    - `required string Message`

    - `JsonElement Type "rate_limit_error"constant`

  - `class BetaGatewayTimeoutError:`

    - `required string Message`

    - `JsonElement Type "timeout_error"constant`

  - `class BetaApiError:`

    - `required string Message`

    - `JsonElement Type "api_error"constant`

  - `class BetaOverloadedError:`

    - `required string Message`

    - `JsonElement Type "overloaded_error"constant`

  - `class BetaManagedAgentsMemoryPreconditionFailedError:`

    - `required Type Type`

      - `"memory_precondition_failed_error"MemoryPreconditionFailedError`

    - `string Message`

  - `class BetaManagedAgentsMemoryPathConflictError:`

    - `required Type Type`

      - `"memory_path_conflict_error"MemoryPathConflictError`

    - `string ConflictingMemoryID`

    - `string ConflictingPath`

    - `string Message`

  - `class BetaManagedAgentsConflictError:`

    - `required Type Type`

      - `"conflict_error"ConflictError`

    - `string Message`

### Beta Managed Agents Memory

- `class BetaManagedAgentsMemory:`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `required string ID`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `required string ContentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `required Int ContentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string MemoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `required string MemoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `required string Path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `required Type Type`

    - `"memory"Memory`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `string? Content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Beta Managed Agents Memory List Item

- `class BetaManagedAgentsMemoryListItem: A class that can be one of several variants.union`

  One item in a [List memories](/docs/en/api/beta/memory_stores/memories/list) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

  - `class BetaManagedAgentsMemory:`

    A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

    - `required string ID`

      Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

    - `required string ContentSha256`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `required Int ContentSizeBytes`

      Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required string MemoryStoreID`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `required string MemoryVersionID`

      ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `required string Path`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `required Type Type`

      - `"memory"Memory`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

    - `string? Content`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `class BetaManagedAgentsMemoryPrefix:`

    A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

    - `required string Path`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `required Type Type`

      - `"memory_prefix"MemoryPrefix`

### Beta Managed Agents Memory Path Conflict Error

- `class BetaManagedAgentsMemoryPathConflictError:`

  - `required Type Type`

    - `"memory_path_conflict_error"MemoryPathConflictError`

  - `string ConflictingMemoryID`

  - `string ConflictingPath`

  - `string Message`

### Beta Managed Agents Memory Precondition Failed Error

- `class BetaManagedAgentsMemoryPreconditionFailedError:`

  - `required Type Type`

    - `"memory_precondition_failed_error"MemoryPreconditionFailedError`

  - `string Message`

### Beta Managed Agents Memory Prefix

- `class BetaManagedAgentsMemoryPrefix:`

  A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

  - `required string Path`

    The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

  - `required Type Type`

    - `"memory_prefix"MemoryPrefix`

### Beta Managed Agents Memory View

- `enum BetaManagedAgentsMemoryView:`

  Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

  - `"basic"Basic`

  - `"full"Full`

### Beta Managed Agents Precondition

- `class BetaManagedAgentsPrecondition:`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `required Type Type`

    - `"content_sha256"ContentSha256`

  - `string ContentSha256`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

# Memory Versions

## List memory versions

`MemoryVersionListPageResponse Beta.MemoryStores.MemoryVersions.List(MemoryVersionListParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions`

List memory versions

### Parameters

- `MemoryVersionListParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `string apiKeyID`

    Query param: Query parameter for api_key_id

  - `DateTimeOffset createdAtGte`

    Query param: Return versions created at or after this time (inclusive).

  - `DateTimeOffset createdAtLte`

    Query param: Return versions created at or before this time (inclusive).

  - `Int limit`

    Query param: Query parameter for limit

  - `string memoryID`

    Query param: Query parameter for memory_id

  - `BetaManagedAgentsMemoryVersionOperation operation`

    Query param: Query parameter for operation

  - `string page`

    Query param: Query parameter for page

  - `string sessionID`

    Query param: Query parameter for session_id

  - `BetaManagedAgentsMemoryView view`

    Query param: Query parameter for view

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class MemoryVersionListPageResponse:`

  Response payload for [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `IReadOnlyList<BetaManagedAgentsMemoryVersion> Data`

    One page of `memory_version` objects, ordered by `created_at` descending (newest first), with `id` as tiebreak.

    - `required string ID`

      Unique identifier for this version (a `memver_...` value).

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required string MemoryID`

      ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

    - `required string MemoryStoreID`

      ID of the memory store this version belongs to (a `memstore_...` value).

    - `required BetaManagedAgentsMemoryVersionOperation Operation`

      The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

      - `"created"Created`

      - `"modified"Modified`

      - `"deleted"Deleted`

    - `required Type Type`

      - `"memory_version"MemoryVersion`

    - `string? Content`

      The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

    - `string? ContentSha256`

      Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    - `Int? ContentSizeBytes`

      Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    - `BetaManagedAgentsActor CreatedBy`

      Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

      - `class BetaManagedAgentsSessionActor:`

        Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

        - `required string SessionID`

          ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

        - `required Type Type`

          - `"session_actor"SessionActor`

      - `class BetaManagedAgentsApiActor:`

        Attribution for a write made directly via the public API (outside of any session).

        - `required string ApiKeyID`

          ID of the API key that performed the write. This identifies the key, not the secret.

        - `required Type Type`

          - `"api_actor"ApiActor`

      - `class BetaManagedAgentsUserActor:`

        Attribution for a write made by a human user through the Anthropic Console.

        - `required Type Type`

          - `"user_actor"UserActor`

        - `required string UserID`

          ID of the user who performed the write (a `user_...` value).

    - `string? Path`

      The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

    - `DateTimeOffset? RedactedAt`

      A timestamp in RFC 3339 format

    - `BetaManagedAgentsActor RedactedBy`

      Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

  - `string? NextPage`

    Opaque cursor for the next page (a `page_...` value), or `null` if there are no more results. Pass as `page` on the next request.

### Example

```csharp
MemoryVersionListParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var page = await client.Beta.MemoryStores.MemoryVersions.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "memory_id": "memory_id",
      "memory_store_id": "memory_store_id",
      "operation": "created",
      "type": "memory_version",
      "content": "content",
      "content_sha256": "content_sha256",
      "content_size_bytes": 0,
      "created_by": {
        "session_id": "x",
        "type": "session_actor"
      },
      "path": "path",
      "redacted_at": "2019-12-27T18:11:19.117Z",
      "redacted_by": {
        "session_id": "x",
        "type": "session_actor"
      }
    }
  ],
  "next_page": "next_page"
}
```

## Retrieve a memory version

`BetaManagedAgentsMemoryVersion Beta.MemoryStores.MemoryVersions.Retrieve(MemoryVersionRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a memory version

### Parameters

- `MemoryVersionRetrieveParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string memoryVersionID`

    Path param: Path parameter memory_version_id

  - `BetaManagedAgentsMemoryView view`

    Query param: Query parameter for view

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsMemoryVersion:`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `required string ID`

    Unique identifier for this version (a `memver_...` value).

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string MemoryID`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `required string MemoryStoreID`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `required BetaManagedAgentsMemoryVersionOperation Operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `"created"Created`

    - `"modified"Modified`

    - `"deleted"Deleted`

  - `required Type Type`

    - `"memory_version"MemoryVersion`

  - `string? Content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `string? ContentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `Int? ContentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `BetaManagedAgentsActor CreatedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor:`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `required string SessionID`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `required Type Type`

        - `"session_actor"SessionActor`

    - `class BetaManagedAgentsApiActor:`

      Attribution for a write made directly via the public API (outside of any session).

      - `required string ApiKeyID`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `required Type Type`

        - `"api_actor"ApiActor`

    - `class BetaManagedAgentsUserActor:`

      Attribution for a write made by a human user through the Anthropic Console.

      - `required Type Type`

        - `"user_actor"UserActor`

      - `required string UserID`

        ID of the user who performed the write (a `user_...` value).

  - `string? Path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `DateTimeOffset? RedactedAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsActor RedactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```csharp
MemoryVersionRetrieveParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryVersionID = "memory_version_id",
};

var betaManagedAgentsMemoryVersion = await client.Beta.MemoryStores.MemoryVersions.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsMemoryVersion);
```

#### Response

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_id": "memory_id",
  "memory_store_id": "memory_store_id",
  "operation": "created",
  "type": "memory_version",
  "content": "content",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_by": {
    "session_id": "x",
    "type": "session_actor"
  },
  "path": "path",
  "redacted_at": "2019-12-27T18:11:19.117Z",
  "redacted_by": {
    "session_id": "x",
    "type": "session_actor"
  }
}
```

## Redact a memory version

`BetaManagedAgentsMemoryVersion Beta.MemoryStores.MemoryVersions.Redact(MemoryVersionRedactParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

Redact a memory version

### Parameters

- `MemoryVersionRedactParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string memoryVersionID`

    Path param: Path parameter memory_version_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsMemoryVersion:`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `required string ID`

    Unique identifier for this version (a `memver_...` value).

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string MemoryID`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `required string MemoryStoreID`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `required BetaManagedAgentsMemoryVersionOperation Operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `"created"Created`

    - `"modified"Modified`

    - `"deleted"Deleted`

  - `required Type Type`

    - `"memory_version"MemoryVersion`

  - `string? Content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `string? ContentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `Int? ContentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `BetaManagedAgentsActor CreatedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor:`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `required string SessionID`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `required Type Type`

        - `"session_actor"SessionActor`

    - `class BetaManagedAgentsApiActor:`

      Attribution for a write made directly via the public API (outside of any session).

      - `required string ApiKeyID`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `required Type Type`

        - `"api_actor"ApiActor`

    - `class BetaManagedAgentsUserActor:`

      Attribution for a write made by a human user through the Anthropic Console.

      - `required Type Type`

        - `"user_actor"UserActor`

      - `required string UserID`

        ID of the user who performed the write (a `user_...` value).

  - `string? Path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `DateTimeOffset? RedactedAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsActor RedactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```csharp
MemoryVersionRedactParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryVersionID = "memory_version_id",
};

var betaManagedAgentsMemoryVersion = await client.Beta.MemoryStores.MemoryVersions.Redact(parameters);

Console.WriteLine(betaManagedAgentsMemoryVersion);
```

#### Response

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_id": "memory_id",
  "memory_store_id": "memory_store_id",
  "operation": "created",
  "type": "memory_version",
  "content": "content",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_by": {
    "session_id": "x",
    "type": "session_actor"
  },
  "path": "path",
  "redacted_at": "2019-12-27T18:11:19.117Z",
  "redacted_by": {
    "session_id": "x",
    "type": "session_actor"
  }
}
```

## Domain Types

### Beta Managed Agents Actor

- `class BetaManagedAgentsActor: A class that can be one of several variants.union`

  Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

  - `class BetaManagedAgentsSessionActor:`

    Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

    - `required string SessionID`

      ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

    - `required Type Type`

      - `"session_actor"SessionActor`

  - `class BetaManagedAgentsApiActor:`

    Attribution for a write made directly via the public API (outside of any session).

    - `required string ApiKeyID`

      ID of the API key that performed the write. This identifies the key, not the secret.

    - `required Type Type`

      - `"api_actor"ApiActor`

  - `class BetaManagedAgentsUserActor:`

    Attribution for a write made by a human user through the Anthropic Console.

    - `required Type Type`

      - `"user_actor"UserActor`

    - `required string UserID`

      ID of the user who performed the write (a `user_...` value).

### Beta Managed Agents API Actor

- `class BetaManagedAgentsApiActor:`

  Attribution for a write made directly via the public API (outside of any session).

  - `required string ApiKeyID`

    ID of the API key that performed the write. This identifies the key, not the secret.

  - `required Type Type`

    - `"api_actor"ApiActor`

### Beta Managed Agents Memory Version

- `class BetaManagedAgentsMemoryVersion:`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `required string ID`

    Unique identifier for this version (a `memver_...` value).

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string MemoryID`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `required string MemoryStoreID`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `required BetaManagedAgentsMemoryVersionOperation Operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `"created"Created`

    - `"modified"Modified`

    - `"deleted"Deleted`

  - `required Type Type`

    - `"memory_version"MemoryVersion`

  - `string? Content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `string? ContentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `Int? ContentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `BetaManagedAgentsActor CreatedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor:`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `required string SessionID`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `required Type Type`

        - `"session_actor"SessionActor`

    - `class BetaManagedAgentsApiActor:`

      Attribution for a write made directly via the public API (outside of any session).

      - `required string ApiKeyID`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `required Type Type`

        - `"api_actor"ApiActor`

    - `class BetaManagedAgentsUserActor:`

      Attribution for a write made by a human user through the Anthropic Console.

      - `required Type Type`

        - `"user_actor"UserActor`

      - `required string UserID`

        ID of the user who performed the write (a `user_...` value).

  - `string? Path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `DateTimeOffset? RedactedAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsActor RedactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Beta Managed Agents Memory Version Operation

- `enum BetaManagedAgentsMemoryVersionOperation:`

  The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

  - `"created"Created`

  - `"modified"Modified`

  - `"deleted"Deleted`

### Beta Managed Agents Session Actor

- `class BetaManagedAgentsSessionActor:`

  Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

  - `required string SessionID`

    ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

  - `required Type Type`

    - `"session_actor"SessionActor`

### Beta Managed Agents User Actor

- `class BetaManagedAgentsUserActor:`

  Attribution for a write made by a human user through the Anthropic Console.

  - `required Type Type`

    - `"user_actor"UserActor`

  - `required string UserID`

    ID of the user who performed the write (a `user_...` value).

# Files

## Upload File

`FileMetadata Beta.Files.Upload(FileUploadParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/files`

Upload File

### Parameters

- `FileUploadParams parameters`

  - `required string file`

    Body param: The file to upload

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class FileMetadata:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing when the file was created.

  - `required string Filename`

    Original filename of the uploaded file.

  - `required string MimeType`

    MIME type of the file.

  - `required Long SizeBytes`

    Size of the file in bytes.

  - `JsonElement Type "file"constant`

    Object type.

    For files, this is always `"file"`.

  - `Boolean Downloadable`

    Whether the file can be downloaded.

  - `BetaFileScope? Scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `required string ID`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonElement Type "session"constant`

      The type of scope (e.g., `"session"`).

### Example

```csharp
FileUploadParams parameters = new()
{
    File = Encoding.UTF8.GetBytes("Example data")
};

var fileMetadata = await client.Beta.Files.Upload(parameters);

Console.WriteLine(fileMetadata);
```

#### Response

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "created_at": "2025-04-15T18:37:24.100435Z",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 102400,
  "type": "file",
  "downloadable": false,
  "scope": {
    "id": "id",
    "type": "session"
  }
}
```

## List Files

`FileListPageResponse Beta.Files.List(FileListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/files`

List Files

### Parameters

- `FileListParams parameters`

  - `string afterID`

    Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `Long limit`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

  - `string scopeID`

    Query param: Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class FileListPageResponse:`

  - `required IReadOnlyList<FileMetadata> Data`

    List of file metadata objects.

    - `required string ID`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `required DateTimeOffset CreatedAt`

      RFC 3339 datetime string representing when the file was created.

    - `required string Filename`

      Original filename of the uploaded file.

    - `required string MimeType`

      MIME type of the file.

    - `required Long SizeBytes`

      Size of the file in bytes.

    - `JsonElement Type "file"constant`

      Object type.

      For files, this is always `"file"`.

    - `Boolean Downloadable`

      Whether the file can be downloaded.

    - `BetaFileScope? Scope`

      The scope of this file, indicating the context in which it was created (e.g., a session).

      - `required string ID`

        The ID of the scoping resource (e.g., the session ID).

      - `JsonElement Type "session"constant`

        The type of scope (e.g., `"session"`).

  - `string? FirstID`

    ID of the first file in this page of results.

  - `Boolean HasMore`

    Whether there are more results available.

  - `string? LastID`

    ID of the last file in this page of results.

### Example

```csharp
FileListParams parameters = new();

var page = await client.Beta.Files.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "created_at": "2025-04-15T18:37:24.100435Z",
      "filename": "document.pdf",
      "mime_type": "application/pdf",
      "size_bytes": 102400,
      "type": "file",
      "downloadable": false,
      "scope": {
        "id": "id",
        "type": "session"
      }
    }
  ],
  "first_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "has_more": true,
  "last_id": "file_013Zva2CMHLNnXjNJJKqJ2EF"
}
```

## Download File

`HttpResponse Beta.Files.Download(FileDownloadParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/files/{file_id}/content`

Download File

### Parameters

- `FileDownloadParams parameters`

  - `required string fileID`

    ID of the File.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Example

```csharp
FileDownloadParams parameters = new() { FileID = "file_id" };

var response = await client.Beta.Files.Download(parameters);

Console.WriteLine(response);
```

## Get File Metadata

`FileMetadata Beta.Files.RetrieveMetadata(FileRetrieveMetadataParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/files/{file_id}`

Get File Metadata

### Parameters

- `FileRetrieveMetadataParams parameters`

  - `required string fileID`

    ID of the File.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class FileMetadata:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing when the file was created.

  - `required string Filename`

    Original filename of the uploaded file.

  - `required string MimeType`

    MIME type of the file.

  - `required Long SizeBytes`

    Size of the file in bytes.

  - `JsonElement Type "file"constant`

    Object type.

    For files, this is always `"file"`.

  - `Boolean Downloadable`

    Whether the file can be downloaded.

  - `BetaFileScope? Scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `required string ID`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonElement Type "session"constant`

      The type of scope (e.g., `"session"`).

### Example

```csharp
FileRetrieveMetadataParams parameters = new() { FileID = "file_id" };

var fileMetadata = await client.Beta.Files.RetrieveMetadata(parameters);

Console.WriteLine(fileMetadata);
```

#### Response

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "created_at": "2025-04-15T18:37:24.100435Z",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 102400,
  "type": "file",
  "downloadable": false,
  "scope": {
    "id": "id",
    "type": "session"
  }
}
```

## Delete File

`DeletedFile Beta.Files.Delete(FileDeleteParamsparameters, CancellationTokencancellationToken = default)`

**delete** `/v1/files/{file_id}`

Delete File

### Parameters

- `FileDeleteParams parameters`

  - `required string fileID`

    ID of the File.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class DeletedFile:`

  - `required string ID`

    ID of the deleted file.

  - `Type Type`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `"file_deleted"FileDeleted`

### Example

```csharp
FileDeleteParams parameters = new() { FileID = "file_id" };

var deletedFile = await client.Beta.Files.Delete(parameters);

Console.WriteLine(deletedFile);
```

#### Response

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file_deleted"
}
```

## Domain Types

### Beta File Scope

- `class BetaFileScope:`

  - `required string ID`

    The ID of the scoping resource (e.g., the session ID).

  - `JsonElement Type "session"constant`

    The type of scope (e.g., `"session"`).

### Deleted File

- `class DeletedFile:`

  - `required string ID`

    ID of the deleted file.

  - `Type Type`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `"file_deleted"FileDeleted`

### File Metadata

- `class FileMetadata:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing when the file was created.

  - `required string Filename`

    Original filename of the uploaded file.

  - `required string MimeType`

    MIME type of the file.

  - `required Long SizeBytes`

    Size of the file in bytes.

  - `JsonElement Type "file"constant`

    Object type.

    For files, this is always `"file"`.

  - `Boolean Downloadable`

    Whether the file can be downloaded.

  - `BetaFileScope? Scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `required string ID`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonElement Type "session"constant`

      The type of scope (e.g., `"session"`).

# Skills

## Create Skill

`SkillCreateResponse Beta.Skills.Create(SkillCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/skills`

Create Skill

### Parameters

- `SkillCreateParams parameters`

  - `required IReadOnlyList<string> files`

    Body param: Files to upload for the skill.

    All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

  - `string? displayTitle`

    Body param: Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class SkillCreateResponse:`

  - `required string ID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required string CreatedAt`

    ISO 8601 timestamp of when the skill was created.

  - `required string? DisplayTitle`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `required string? LatestVersion`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `required string Source`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `required string Type`

    Object type.

    For Skills, this is always `"skill"`.

  - `required string UpdatedAt`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```csharp
SkillCreateParams parameters = new()
{
    Files =
    [
        Encoding.UTF8.GetBytes("Example data")
    ],
};

var skill = await client.Beta.Skills.Create(parameters);

Console.WriteLine(skill);
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

## List Skills

`SkillListPageResponse Beta.Skills.List(SkillListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/skills`

List Skills

### Parameters

- `SkillListParams parameters`

  - `Long limit`

    Query param: Number of results to return per page.

    Maximum value is 100. Defaults to 20.

  - `string? page`

    Query param: Pagination token for fetching a specific page of results.

    Pass the value from a previous response's `next_page` field to get the next page of results.

  - `string? source`

    Query param: Filter skills by source.

    If provided, only skills from the specified source will be returned:

    * `"custom"`: only return user-created skills
    * `"anthropic"`: only return Anthropic-created skills

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class SkillListPageResponse:`

  - `required IReadOnlyList<SkillListResponse> Data`

    List of skills.

    - `required string ID`

      Unique identifier for the skill.

      The format and length of IDs may change over time.

    - `required string CreatedAt`

      ISO 8601 timestamp of when the skill was created.

    - `required string? DisplayTitle`

      Display title for the skill.

      This is a human-readable label that is not included in the prompt sent to the model.

    - `required string? LatestVersion`

      The latest version identifier for the skill.

      This represents the most recent version of the skill that has been created.

    - `required string Source`

      Source of the skill.

      This may be one of the following values:

      * `"custom"`: the skill was created by a user
      * `"anthropic"`: the skill was created by Anthropic

    - `required string Type`

      Object type.

      For Skills, this is always `"skill"`.

    - `required string UpdatedAt`

      ISO 8601 timestamp of when the skill was last updated.

  - `required Boolean HasMore`

    Whether there are more results available.

    If `true`, there are additional results that can be fetched using the `next_page` token.

  - `required string? NextPage`

    Token for fetching the next page of results.

    If `null`, there are no more results available. Pass this value to the `page` parameter in the next request to get the next page.

### Example

```csharp
SkillListParams parameters = new();

var page = await client.Beta.Skills.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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

`SkillRetrieveResponse Beta.Skills.Retrieve(SkillRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/skills/{skill_id}`

Get Skill

### Parameters

- `SkillRetrieveParams parameters`

  - `required string skillID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class SkillRetrieveResponse:`

  - `required string ID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required string CreatedAt`

    ISO 8601 timestamp of when the skill was created.

  - `required string? DisplayTitle`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `required string? LatestVersion`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `required string Source`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `required string Type`

    Object type.

    For Skills, this is always `"skill"`.

  - `required string UpdatedAt`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```csharp
SkillRetrieveParams parameters = new() { SkillID = "skill_id" };

var skill = await client.Beta.Skills.Retrieve(parameters);

Console.WriteLine(skill);
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

`SkillDeleteResponse Beta.Skills.Delete(SkillDeleteParamsparameters, CancellationTokencancellationToken = default)`

**delete** `/v1/skills/{skill_id}`

Delete Skill

### Parameters

- `SkillDeleteParams parameters`

  - `required string skillID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class SkillDeleteResponse:`

  - `required string ID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required string Type`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

### Example

```csharp
SkillDeleteParams parameters = new() { SkillID = "skill_id" };

var skill = await client.Beta.Skills.Delete(parameters);

Console.WriteLine(skill);
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

`VersionCreateResponse Beta.Skills.Versions.Create(VersionCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/skills/{skill_id}/versions`

Create Skill Version

### Parameters

- `VersionCreateParams parameters`

  - `required string skillID`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required IReadOnlyList<string> files`

    Body param: Files to upload for the skill.

    All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class VersionCreateResponse:`

  - `required string ID`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `required string CreatedAt`

    ISO 8601 timestamp of when the skill version was created.

  - `required string Description`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `required string Directory`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `required string Name`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `required string SkillID`

    Identifier for the skill that this version belongs to.

  - `required string Type`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `required string Version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```csharp
VersionCreateParams parameters = new()
{
    SkillID = "skill_id",
    Files =
    [
        Encoding.UTF8.GetBytes("Example data")
    ],
};

var version = await client.Beta.Skills.Versions.Create(parameters);

Console.WriteLine(version);
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

`VersionListPageResponse Beta.Skills.Versions.List(VersionListParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/skills/{skill_id}/versions`

List Skill Versions

### Parameters

- `VersionListParams parameters`

  - `required string skillID`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `Long? limit`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

  - `string? page`

    Query param: Optionally set to the `next_page` token from the previous response.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class VersionListPageResponse:`

  - `required IReadOnlyList<VersionListResponse> Data`

    List of skill versions.

    - `required string ID`

      Unique identifier for the skill version.

      The format and length of IDs may change over time.

    - `required string CreatedAt`

      ISO 8601 timestamp of when the skill version was created.

    - `required string Description`

      Description of the skill version.

      This is extracted from the SKILL.md file in the skill upload.

    - `required string Directory`

      Directory name of the skill version.

      This is the top-level directory name that was extracted from the uploaded files.

    - `required string Name`

      Human-readable name of the skill version.

      This is extracted from the SKILL.md file in the skill upload.

    - `required string SkillID`

      Identifier for the skill that this version belongs to.

    - `required string Type`

      Object type.

      For Skill Versions, this is always `"skill_version"`.

    - `required string Version`

      Version identifier for the skill.

      Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `required Boolean HasMore`

    Indicates if there are more results in the requested page direction.

  - `required string? NextPage`

    Token to provide in as `page` in the subsequent request to retrieve the next page of data.

### Example

```csharp
VersionListParams parameters = new() { SkillID = "skill_id" };

var page = await client.Beta.Skills.Versions.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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

`HttpResponse Beta.Skills.Versions.Download(VersionDownloadParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/skills/{skill_id}/versions/{version}/content`

Download a skill version's content as a zip archive.

### Parameters

- `VersionDownloadParams parameters`

  - `required string skillID`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required string version`

    Path param: Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Example

```csharp
VersionDownloadParams parameters = new()
{
    SkillID = "skill_id",
    Version = "version",
};

var response = await client.Beta.Skills.Versions.Download(parameters);

Console.WriteLine(response);
```

## Get Skill Version

`VersionRetrieveResponse Beta.Skills.Versions.Retrieve(VersionRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/skills/{skill_id}/versions/{version}`

Get Skill Version

### Parameters

- `VersionRetrieveParams parameters`

  - `required string skillID`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required string version`

    Path param: Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class VersionRetrieveResponse:`

  - `required string ID`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `required string CreatedAt`

    ISO 8601 timestamp of when the skill version was created.

  - `required string Description`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `required string Directory`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `required string Name`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `required string SkillID`

    Identifier for the skill that this version belongs to.

  - `required string Type`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `required string Version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```csharp
VersionRetrieveParams parameters = new()
{
    SkillID = "skill_id",
    Version = "version",
};

var version = await client.Beta.Skills.Versions.Retrieve(parameters);

Console.WriteLine(version);
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

`VersionDeleteResponse Beta.Skills.Versions.Delete(VersionDeleteParamsparameters, CancellationTokencancellationToken = default)`

**delete** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

### Parameters

- `VersionDeleteParams parameters`

  - `required string skillID`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required string version`

    Path param: Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class VersionDeleteResponse:`

  - `required string ID`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `required string Type`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

### Example

```csharp
VersionDeleteParams parameters = new()
{
    SkillID = "skill_id",
    Version = "version",
};

var version = await client.Beta.Skills.Versions.Delete(parameters);

Console.WriteLine(version);
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

`BetaUserProfile Beta.UserProfiles.Create(UserProfileCreateParams?parameters, CancellationTokencancellationToken = default)`

**post** `/v1/user_profiles`

Create User Profile

### Parameters

- `UserProfileCreateParams parameters`

  - `string? externalID`

    Body param: Platform's own identifier for this user. Not enforced unique. Maximum 255 characters.

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

  - `string? name`

    Body param: Display name of the entity this profile represents. Required when relationship is `resold` (the resold-to company's name); optional otherwise. Maximum 255 characters.

  - `Relationship relationship`

    Body param: How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"External`

    - `"resold"Resold`

    - `"internal"Internal`

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaUserProfile:`

  - `required string ID`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `required Relationship Relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"External`

    - `"resold"Resold`

    - `"internal"Internal`

  - `required IReadOnlyDictionary<string, BetaUserProfileTrustGrant> TrustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `required Status Status`

      Status of the trust grant.

      - `"active"Active`

      - `"pending"Pending`

      - `"rejected"Rejected`

  - `required Type Type`

    Object type. Always `user_profile`.

    - `"user_profile"UserProfile`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `string? ExternalID`

    Platform's own identifier for this user. Not enforced unique.

  - `string? Name`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Example

```csharp
UserProfileCreateParams parameters = new();

var betaUserProfile = await client.Beta.UserProfiles.Create(parameters);

Console.WriteLine(betaUserProfile);
```

#### Response

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "relationship": "external",
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "external_id": "user_12345",
  "name": "Example User"
}
```

## List User Profiles

`UserProfileListPageResponse Beta.UserProfiles.List(UserProfileListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/user_profiles`

List User Profiles

### Parameters

- `UserProfileListParams parameters`

  - `Int limit`

    Query param: Query parameter for limit

  - `Order order`

    Query param: Query parameter for order

    - `"asc"Asc`

    - `"desc"Desc`

  - `string page`

    Query param: Query parameter for page

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class UserProfileListPageResponse:`

  - `required IReadOnlyList<BetaUserProfile> Data`

    User profiles on this page.

    - `required string ID`

      Unique identifier for this user profile, prefixed `uprof_`.

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required IReadOnlyDictionary<string, string> Metadata`

      Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

    - `required Relationship Relationship`

      How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

      - `"external"External`

      - `"resold"Resold`

      - `"internal"Internal`

    - `required IReadOnlyDictionary<string, BetaUserProfileTrustGrant> TrustGrants`

      Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

      - `required Status Status`

        Status of the trust grant.

        - `"active"Active`

        - `"pending"Pending`

        - `"rejected"Rejected`

    - `required Type Type`

      Object type. Always `user_profile`.

      - `"user_profile"UserProfile`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

    - `string? ExternalID`

      Platform's own identifier for this user. Not enforced unique.

    - `string? Name`

      Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

  - `required string? NextPage`

    Cursor for the next page, or `null` when there are no more results.

### Example

```csharp
UserProfileListParams parameters = new();

var page = await client.Beta.UserProfiles.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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
      "relationship": "external",
      "trust_grants": {
        "cyber": {
          "status": "active"
        }
      },
      "type": "user_profile",
      "updated_at": "2026-03-15T10:00:00Z",
      "external_id": "user_12345",
      "name": "Example User"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get User Profile

`BetaUserProfile Beta.UserProfiles.Retrieve(UserProfileRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/user_profiles/{user_profile_id}`

Get User Profile

### Parameters

- `UserProfileRetrieveParams parameters`

  - `required string userProfileID`

    Path parameter user_profile_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaUserProfile:`

  - `required string ID`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `required Relationship Relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"External`

    - `"resold"Resold`

    - `"internal"Internal`

  - `required IReadOnlyDictionary<string, BetaUserProfileTrustGrant> TrustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `required Status Status`

      Status of the trust grant.

      - `"active"Active`

      - `"pending"Pending`

      - `"rejected"Rejected`

  - `required Type Type`

    Object type. Always `user_profile`.

    - `"user_profile"UserProfile`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `string? ExternalID`

    Platform's own identifier for this user. Not enforced unique.

  - `string? Name`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Example

```csharp
UserProfileRetrieveParams parameters = new()
{
    UserProfileID = "uprof_011CZkZCu8hGbp5mYRQgUmz9"
};

var betaUserProfile = await client.Beta.UserProfiles.Retrieve(parameters);

Console.WriteLine(betaUserProfile);
```

#### Response

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "relationship": "external",
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "external_id": "user_12345",
  "name": "Example User"
}
```

## Update User Profile

`BetaUserProfile Beta.UserProfiles.Update(UserProfileUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/user_profiles/{user_profile_id}`

Update User Profile

### Parameters

- `UserProfileUpdateParams parameters`

  - `required string userProfileID`

    Path param: Path parameter user_profile_id

  - `string? externalID`

    Body param: If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters.

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

  - `string? name`

    Body param: If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

  - `Relationship? relationship`

    Body param: How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"External`

    - `"resold"Resold`

    - `"internal"Internal`

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaUserProfile:`

  - `required string ID`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `required Relationship Relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"External`

    - `"resold"Resold`

    - `"internal"Internal`

  - `required IReadOnlyDictionary<string, BetaUserProfileTrustGrant> TrustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `required Status Status`

      Status of the trust grant.

      - `"active"Active`

      - `"pending"Pending`

      - `"rejected"Rejected`

  - `required Type Type`

    Object type. Always `user_profile`.

    - `"user_profile"UserProfile`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `string? ExternalID`

    Platform's own identifier for this user. Not enforced unique.

  - `string? Name`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Example

```csharp
UserProfileUpdateParams parameters = new()
{
    UserProfileID = "uprof_011CZkZCu8hGbp5mYRQgUmz9"
};

var betaUserProfile = await client.Beta.UserProfiles.Update(parameters);

Console.WriteLine(betaUserProfile);
```

#### Response

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "relationship": "external",
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "external_id": "user_12345",
  "name": "Example User"
}
```

## Create Enrollment URL

`BetaUserProfileEnrollmentUrl Beta.UserProfiles.CreateEnrollmentUrl(UserProfileCreateEnrollmentUrlParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

### Parameters

- `UserProfileCreateEnrollmentUrlParams parameters`

  - `required string userProfileID`

    Path parameter user_profile_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaUserProfileEnrollmentUrl:`

  - `required DateTimeOffset ExpiresAt`

    A timestamp in RFC 3339 format

  - `required Type Type`

    Object type. Always `enrollment_url`.

    - `"enrollment_url"EnrollmentUrl`

  - `required string Url`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Example

```csharp
UserProfileCreateEnrollmentUrlParams parameters = new()
{
    UserProfileID = "uprof_011CZkZCu8hGbp5mYRQgUmz9"
};

var betaUserProfileEnrollmentUrl = await client.Beta.UserProfiles.CreateEnrollmentUrl(parameters);

Console.WriteLine(betaUserProfileEnrollmentUrl);
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

  - `required string ID`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `required Relationship Relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"External`

    - `"resold"Resold`

    - `"internal"Internal`

  - `required IReadOnlyDictionary<string, BetaUserProfileTrustGrant> TrustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `required Status Status`

      Status of the trust grant.

      - `"active"Active`

      - `"pending"Pending`

      - `"rejected"Rejected`

  - `required Type Type`

    Object type. Always `user_profile`.

    - `"user_profile"UserProfile`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `string? ExternalID`

    Platform's own identifier for this user. Not enforced unique.

  - `string? Name`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Beta User Profile Enrollment URL

- `class BetaUserProfileEnrollmentUrl:`

  - `required DateTimeOffset ExpiresAt`

    A timestamp in RFC 3339 format

  - `required Type Type`

    Object type. Always `enrollment_url`.

    - `"enrollment_url"EnrollmentUrl`

  - `required string Url`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Beta User Profile Trust Grant

- `class BetaUserProfileTrustGrant:`

  - `required Status Status`

    Status of the trust grant.

    - `"active"Active`

    - `"pending"Pending`

    - `"rejected"Rejected`

# Dreams

## Create a Dream

`BetaDream Beta.Dreams.Create(DreamCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/dreams`

Create a Dream

### Parameters

- `DreamCreateParams parameters`

  - `required IReadOnlyList<BetaDreamInput> inputs`

    Body param

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store.

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"memory_store"MemoryStore`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `required IReadOnlyList<string> SessionIds`

      - `required Type Type`

        - `"sessions"Sessions`

  - `required Model model`

    Body param: Model identifier and configuration applied to every pipeline stage.

    - `string`

    - `class BetaDreamModelConfigParam:`

      Model identifier and configuration applied to every pipeline stage.

      - `required string ID`

        Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

      - `Speed? Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"Standard`

        - `"fast"Fast`

  - `string? instructions`

    Body param

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `required string ID`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? EndedAt`

    A timestamp in RFC 3339 format

  - `required BetaDreamError? Error`

    Failure detail for a Dream whose `status` is `failed`.

    - `required string Message`

    - `required string Type`

  - `required IReadOnlyList<BetaDreamInput> Inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store.

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"memory_store"MemoryStore`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `required IReadOnlyList<string> SessionIds`

      - `required Type Type`

        - `"sessions"Sessions`

  - `required string? Instructions`

  - `required BetaDreamModelConfig Model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `required string ID`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `Speed Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"Standard`

      - `"fast"Fast`

  - `required IReadOnlyList<BetaDreamOutput> Outputs`

    - `required string MemoryStoreID`

    - `required Type Type`

      - `"memory_store"MemoryStore`

  - `required string? SessionID`

  - `required BetaDreamStatus Status`

    Lifecycle status of a Dream.

    - `"pending"Pending`

    - `"running"Running`

    - `"completed"Completed`

    - `"failed"Failed`

    - `"canceled"Canceled`

  - `required Type Type`

    - `"dream"Dream`

  - `required BetaDreamUsage Usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `required Int CacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `required Int CacheReadInputTokens`

      Total tokens read from prompt cache.

    - `required Int InputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `required Int OutputTokens`

      Total output tokens generated across every pipeline stage.

### Example

```csharp
DreamCreateParams parameters = new()
{
    Inputs =
    [
        new BetaDreamMemoryStoreInput()
        {
            MemoryStoreID = "x",
            Type = Type.MemoryStore,
        },
    ],
    Model = "string",
};

var betaDream = await client.Beta.Dreams.Create(parameters);

Console.WriteLine(betaDream);
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

`DreamListPageResponse Beta.Dreams.List(DreamListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/dreams`

List Dreams

### Parameters

- `DreamListParams parameters`

  - `DateTimeOffset createdAtGt`

    Query param: Return dreams with `created_at` strictly after this timestamp (exclusive lower bound, RFC 3339). Unset applies no lower bound.

  - `DateTimeOffset createdAtLt`

    Query param: Return dreams with `created_at` strictly before this timestamp (exclusive upper bound, RFC 3339). Unset applies no upper bound.

  - `Boolean includeArchived`

    Query param: Query parameter for include_archived

  - `Int limit`

    Query param: Query parameter for limit

  - `string page`

    Query param: Query parameter for page

  - `IReadOnlyList<BetaDreamStatus> statuses`

    Query param: Filter by lifecycle status. Repeat the parameter to match any of multiple statuses. Empty applies no status filter.

    - `"pending"Pending`

    - `"running"Running`

    - `"completed"Completed`

    - `"failed"Failed`

    - `"canceled"Canceled`

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class DreamListPageResponse:`

  - `required IReadOnlyList<BetaDream> Data`

    - `required string ID`

    - `required DateTimeOffset? ArchivedAt`

      A timestamp in RFC 3339 format

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required DateTimeOffset? EndedAt`

      A timestamp in RFC 3339 format

    - `required BetaDreamError? Error`

      Failure detail for a Dream whose `status` is `failed`.

      - `required string Message`

      - `required string Type`

    - `required IReadOnlyList<BetaDreamInput> Inputs`

      - `class BetaDreamMemoryStoreInput:`

        An input memory store the dream reads from. The dream never mutates this store.

        - `required string MemoryStoreID`

        - `required Type Type`

          - `"memory_store"MemoryStore`

      - `class BetaDreamSessionsInput:`

        Input session transcripts the dream reads.

        - `required IReadOnlyList<string> SessionIds`

        - `required Type Type`

          - `"sessions"Sessions`

    - `required string? Instructions`

    - `required BetaDreamModelConfig Model`

      Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

      - `required string ID`

        Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

      - `Speed Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"Standard`

        - `"fast"Fast`

    - `required IReadOnlyList<BetaDreamOutput> Outputs`

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"memory_store"MemoryStore`

    - `required string? SessionID`

    - `required BetaDreamStatus Status`

      Lifecycle status of a Dream.

      - `"pending"Pending`

      - `"running"Running`

      - `"completed"Completed`

      - `"failed"Failed`

      - `"canceled"Canceled`

    - `required Type Type`

      - `"dream"Dream`

    - `required BetaDreamUsage Usage`

      Cumulative token usage for the dream across every pipeline stage.

      - `required Int CacheCreationInputTokens`

        Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      - `required Int CacheReadInputTokens`

        Total tokens read from prompt cache.

      - `required Int InputTokens`

        Total uncached input tokens consumed across every pipeline stage.

      - `required Int OutputTokens`

        Total output tokens generated across every pipeline stage.

  - `required string? NextPage`

### Example

```csharp
DreamListParams parameters = new();

var page = await client.Beta.Dreams.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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

`BetaDream Beta.Dreams.Retrieve(DreamRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/dreams/{dream_id}`

Get a Dream

### Parameters

- `DreamRetrieveParams parameters`

  - `required string dreamID`

    Path parameter dream_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `required string ID`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? EndedAt`

    A timestamp in RFC 3339 format

  - `required BetaDreamError? Error`

    Failure detail for a Dream whose `status` is `failed`.

    - `required string Message`

    - `required string Type`

  - `required IReadOnlyList<BetaDreamInput> Inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store.

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"memory_store"MemoryStore`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `required IReadOnlyList<string> SessionIds`

      - `required Type Type`

        - `"sessions"Sessions`

  - `required string? Instructions`

  - `required BetaDreamModelConfig Model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `required string ID`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `Speed Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"Standard`

      - `"fast"Fast`

  - `required IReadOnlyList<BetaDreamOutput> Outputs`

    - `required string MemoryStoreID`

    - `required Type Type`

      - `"memory_store"MemoryStore`

  - `required string? SessionID`

  - `required BetaDreamStatus Status`

    Lifecycle status of a Dream.

    - `"pending"Pending`

    - `"running"Running`

    - `"completed"Completed`

    - `"failed"Failed`

    - `"canceled"Canceled`

  - `required Type Type`

    - `"dream"Dream`

  - `required BetaDreamUsage Usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `required Int CacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `required Int CacheReadInputTokens`

      Total tokens read from prompt cache.

    - `required Int InputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `required Int OutputTokens`

      Total output tokens generated across every pipeline stage.

### Example

```csharp
DreamRetrieveParams parameters = new() { DreamID = "dream_id" };

var betaDream = await client.Beta.Dreams.Retrieve(parameters);

Console.WriteLine(betaDream);
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

`BetaDream Beta.Dreams.Cancel(DreamCancelParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/dreams/{dream_id}/cancel`

Cancel a Dream

### Parameters

- `DreamCancelParams parameters`

  - `required string dreamID`

    Path parameter dream_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `required string ID`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? EndedAt`

    A timestamp in RFC 3339 format

  - `required BetaDreamError? Error`

    Failure detail for a Dream whose `status` is `failed`.

    - `required string Message`

    - `required string Type`

  - `required IReadOnlyList<BetaDreamInput> Inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store.

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"memory_store"MemoryStore`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `required IReadOnlyList<string> SessionIds`

      - `required Type Type`

        - `"sessions"Sessions`

  - `required string? Instructions`

  - `required BetaDreamModelConfig Model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `required string ID`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `Speed Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"Standard`

      - `"fast"Fast`

  - `required IReadOnlyList<BetaDreamOutput> Outputs`

    - `required string MemoryStoreID`

    - `required Type Type`

      - `"memory_store"MemoryStore`

  - `required string? SessionID`

  - `required BetaDreamStatus Status`

    Lifecycle status of a Dream.

    - `"pending"Pending`

    - `"running"Running`

    - `"completed"Completed`

    - `"failed"Failed`

    - `"canceled"Canceled`

  - `required Type Type`

    - `"dream"Dream`

  - `required BetaDreamUsage Usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `required Int CacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `required Int CacheReadInputTokens`

      Total tokens read from prompt cache.

    - `required Int InputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `required Int OutputTokens`

      Total output tokens generated across every pipeline stage.

### Example

```csharp
DreamCancelParams parameters = new() { DreamID = "dream_id" };

var betaDream = await client.Beta.Dreams.Cancel(parameters);

Console.WriteLine(betaDream);
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

`BetaDream Beta.Dreams.Archive(DreamArchiveParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/dreams/{dream_id}/archive`

Archive a Dream

### Parameters

- `DreamArchiveParams parameters`

  - `required string dreamID`

    Path parameter dream_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `required string ID`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? EndedAt`

    A timestamp in RFC 3339 format

  - `required BetaDreamError? Error`

    Failure detail for a Dream whose `status` is `failed`.

    - `required string Message`

    - `required string Type`

  - `required IReadOnlyList<BetaDreamInput> Inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store.

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"memory_store"MemoryStore`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `required IReadOnlyList<string> SessionIds`

      - `required Type Type`

        - `"sessions"Sessions`

  - `required string? Instructions`

  - `required BetaDreamModelConfig Model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `required string ID`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `Speed Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"Standard`

      - `"fast"Fast`

  - `required IReadOnlyList<BetaDreamOutput> Outputs`

    - `required string MemoryStoreID`

    - `required Type Type`

      - `"memory_store"MemoryStore`

  - `required string? SessionID`

  - `required BetaDreamStatus Status`

    Lifecycle status of a Dream.

    - `"pending"Pending`

    - `"running"Running`

    - `"completed"Completed`

    - `"failed"Failed`

    - `"canceled"Canceled`

  - `required Type Type`

    - `"dream"Dream`

  - `required BetaDreamUsage Usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `required Int CacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `required Int CacheReadInputTokens`

      Total tokens read from prompt cache.

    - `required Int InputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `required Int OutputTokens`

      Total output tokens generated across every pipeline stage.

### Example

```csharp
DreamArchiveParams parameters = new() { DreamID = "dream_id" };

var betaDream = await client.Beta.Dreams.Archive(parameters);

Console.WriteLine(betaDream);
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

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `required string ID`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? EndedAt`

    A timestamp in RFC 3339 format

  - `required BetaDreamError? Error`

    Failure detail for a Dream whose `status` is `failed`.

    - `required string Message`

    - `required string Type`

  - `required IReadOnlyList<BetaDreamInput> Inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store.

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"memory_store"MemoryStore`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `required IReadOnlyList<string> SessionIds`

      - `required Type Type`

        - `"sessions"Sessions`

  - `required string? Instructions`

  - `required BetaDreamModelConfig Model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `required string ID`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `Speed Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"Standard`

      - `"fast"Fast`

  - `required IReadOnlyList<BetaDreamOutput> Outputs`

    - `required string MemoryStoreID`

    - `required Type Type`

      - `"memory_store"MemoryStore`

  - `required string? SessionID`

  - `required BetaDreamStatus Status`

    Lifecycle status of a Dream.

    - `"pending"Pending`

    - `"running"Running`

    - `"completed"Completed`

    - `"failed"Failed`

    - `"canceled"Canceled`

  - `required Type Type`

    - `"dream"Dream`

  - `required BetaDreamUsage Usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `required Int CacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `required Int CacheReadInputTokens`

      Total tokens read from prompt cache.

    - `required Int InputTokens`

      Total uncached input tokens consumed across every pipeline stage.

    - `required Int OutputTokens`

      Total output tokens generated across every pipeline stage.

### Beta Dream Error

- `class BetaDreamError:`

  Failure detail for a Dream whose `status` is `failed`.

  - `required string Message`

  - `required string Type`

### Beta Dream Input

- `class BetaDreamInput: A class that can be one of several variants.union`

  An input memory store the dream reads from. The dream never mutates this store.

  - `class BetaDreamMemoryStoreInput:`

    An input memory store the dream reads from. The dream never mutates this store.

    - `required string MemoryStoreID`

    - `required Type Type`

      - `"memory_store"MemoryStore`

  - `class BetaDreamSessionsInput:`

    Input session transcripts the dream reads.

    - `required IReadOnlyList<string> SessionIds`

    - `required Type Type`

      - `"sessions"Sessions`

### Beta Dream Memory Store Input

- `class BetaDreamMemoryStoreInput:`

  An input memory store the dream reads from. The dream never mutates this store.

  - `required string MemoryStoreID`

  - `required Type Type`

    - `"memory_store"MemoryStore`

### Beta Dream Memory Store Output

- `class BetaDreamMemoryStoreOutput:`

  An output memory store the dream writes consolidated memories into.

  - `required string MemoryStoreID`

  - `required Type Type`

    - `"memory_store"MemoryStore`

### Beta Dream Model Config

- `class BetaDreamModelConfig:`

  Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

  - `required string ID`

    Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

  - `Speed Speed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"Standard`

    - `"fast"Fast`

### Beta Dream Model Config Param

- `class BetaDreamModelConfigParam:`

  Model identifier and configuration applied to every pipeline stage.

  - `required string ID`

    Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

  - `Speed? Speed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"Standard`

    - `"fast"Fast`

### Beta Dream Output

- `class BetaDreamOutput:`

  An output memory store the dream writes consolidated memories into.

  - `required string MemoryStoreID`

  - `required Type Type`

    - `"memory_store"MemoryStore`

### Beta Dream Sessions Input

- `class BetaDreamSessionsInput:`

  Input session transcripts the dream reads.

  - `required IReadOnlyList<string> SessionIds`

  - `required Type Type`

    - `"sessions"Sessions`

### Beta Dream Status

- `enum BetaDreamStatus:`

  Lifecycle status of a Dream.

  - `"pending"Pending`

  - `"running"Running`

  - `"completed"Completed`

  - `"failed"Failed`

  - `"canceled"Canceled`

### Beta Dream Usage

- `class BetaDreamUsage:`

  Cumulative token usage for the dream across every pipeline stage.

  - `required Int CacheCreationInputTokens`

    Total tokens used to create prompt-cache entries (sum of all TTL tiers).

  - `required Int CacheReadInputTokens`

    Total tokens read from prompt cache.

  - `required Int InputTokens`

    Total uncached input tokens consumed across every pipeline stage.

  - `required Int OutputTokens`

    Total output tokens generated across every pipeline stage.

# Tunnels

## Create Tunnel

`BetaTunnel Beta.Tunnels.Create(TunnelCreateParams?parameters, CancellationTokencancellationToken = default)`

**post** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Creates a tunnel. Creation allocates a fresh hostname and provisions the tunnel; it is not idempotent. The new tunnel rejects MCP traffic until at least one CA certificate is added.

### Parameters

- `TunnelCreateParams parameters`

  - `string? displayName`

    Body param: Optional human-readable name for the tunnel (1-255 characters).

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `required string ID`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? DisplayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `required string Domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonElement Type "tunnel"constant`

### Example

```csharp
TunnelCreateParams parameters = new();

var betaTunnel = await client.Beta.Tunnels.Create(parameters);

Console.WriteLine(betaTunnel);
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

`BetaTunnel Beta.Tunnels.Retrieve(TunnelRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/tunnels/{tunnel_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel by ID.

### Parameters

- `TunnelRetrieveParams parameters`

  - `required string tunnelID`

    Path parameter tunnel_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `required string ID`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? DisplayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `required string Domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonElement Type "tunnel"constant`

### Example

```csharp
TunnelRetrieveParams parameters = new() { TunnelID = "tunnel_id" };

var betaTunnel = await client.Beta.Tunnels.Retrieve(parameters);

Console.WriteLine(betaTunnel);
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

`TunnelListPageResponse Beta.Tunnels.List(TunnelListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists tunnels. Results are ordered by creation time, newest first; archived tunnels are excluded unless include_archived is set.

### Parameters

- `TunnelListParams parameters`

  - `Boolean includeArchived`

    Query param: Whether to include archived tunnels in the results. Defaults to false.

  - `Int limit`

    Query param: Maximum number of tunnels to return per page. Defaults to 20, maximum 1000.

  - `string page`

    Query param: Opaque pagination cursor from a previous `list_tunnels` response.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class TunnelListPageResponse:`

  A paginated list of tunnels.

  - `required IReadOnlyList<BetaTunnel> Data`

    List of tunnels, ordered by created_at descending.

    - `required string ID`

      Unique identifier for the tunnel, prefixed with `tnl_`.

    - `required DateTimeOffset? ArchivedAt`

      A timestamp in RFC 3339 format

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required string? DisplayName`

      Human-readable name for the tunnel (1-255 characters). Null if unset.

    - `required string Domain`

      Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

    - `JsonElement Type "tunnel"constant`

  - `required string? NextPage`

    Pagination cursor for the next page, or null if no more results.

### Example

```csharp
TunnelListParams parameters = new();

var page = await client.Beta.Tunnels.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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

`BetaTunnel Beta.Tunnels.Archive(TunnelArchiveParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/tunnels/{tunnel_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel. Archival is irreversible: every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.

### Parameters

- `TunnelArchiveParams parameters`

  - `required string tunnelID`

    Path parameter tunnel_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `required string ID`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? DisplayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `required string Domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonElement Type "tunnel"constant`

### Example

```csharp
TunnelArchiveParams parameters = new() { TunnelID = "tunnel_id" };

var betaTunnel = await client.Beta.Tunnels.Archive(parameters);

Console.WriteLine(betaTunnel);
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

`BetaTunnelToken Beta.Tunnels.RevealToken(TunnelRevealTokenParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/tunnels/{tunnel_id}/reveal_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

### Parameters

- `TunnelRevealTokenParams parameters`

  - `required string tunnelID`

    Path parameter tunnel_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaTunnelToken:`

  A tunnel's connector token.

  - `required string ID`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `required string TunnelToken`

    The connector token used to run the tunnel. Treat as a credential.

  - `JsonElement Type "tunnel_token"constant`

### Example

```csharp
TunnelRevealTokenParams parameters = new() { TunnelID = "tunnel_id" };

var betaTunnelToken = await client.Beta.Tunnels.RevealToken(parameters);

Console.WriteLine(betaTunnelToken);
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

`BetaTunnelToken Beta.Tunnels.RotateToken(TunnelRotateTokenParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/tunnels/{tunnel_id}/rotate_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

### Parameters

- `TunnelRotateTokenParams parameters`

  - `required string tunnelID`

    Path param: Path parameter tunnel_id

  - `string? reason`

    Body param: Optional free-text reason for the rotation, recorded for audit.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaTunnelToken:`

  A tunnel's connector token.

  - `required string ID`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `required string TunnelToken`

    The connector token used to run the tunnel. Treat as a credential.

  - `JsonElement Type "tunnel_token"constant`

### Example

```csharp
TunnelRotateTokenParams parameters = new() { TunnelID = "tunnel_id" };

var betaTunnelToken = await client.Beta.Tunnels.RotateToken(parameters);

Console.WriteLine(betaTunnelToken);
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

  - `required string ID`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? DisplayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `required string Domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonElement Type "tunnel"constant`

### Beta Tunnel Token

- `class BetaTunnelToken:`

  A tunnel's connector token.

  - `required string ID`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `required string TunnelToken`

    The connector token used to run the tunnel. Treat as a credential.

  - `JsonElement Type "tunnel_token"constant`

# Certificates

## Create Tunnel Certificate

`BetaTunnelCertificate Beta.Tunnels.Certificates.Create(CertificateCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

### Parameters

- `CertificateCreateParams parameters`

  - `required string tunnelID`

    Path param: Path parameter tunnel_id

  - `required string caCertificatePem`

    Body param: PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material. Maximum 8KB.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `required string ID`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

  - `required string Fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `required string TunnelID`

    ID of the tunnel the certificate is registered against.

  - `JsonElement Type "tunnel_certificate"constant`

### Example

```csharp
CertificateCreateParams parameters = new()
{
    TunnelID = "tunnel_id",
    CaCertificatePem = "ca_certificate_pem",
};

var betaTunnelCertificate = await client.Beta.Tunnels.Certificates.Create(parameters);

Console.WriteLine(betaTunnelCertificate);
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

`BetaTunnelCertificate Beta.Tunnels.Certificates.Retrieve(CertificateRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

### Parameters

- `CertificateRetrieveParams parameters`

  - `required string tunnelID`

    Path param: Path parameter tunnel_id

  - `required string certificateID`

    Path param: Path parameter certificate_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `required string ID`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

  - `required string Fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `required string TunnelID`

    ID of the tunnel the certificate is registered against.

  - `JsonElement Type "tunnel_certificate"constant`

### Example

```csharp
CertificateRetrieveParams parameters = new()
{
    TunnelID = "tunnel_id",
    CertificateID = "certificate_id",
};

var betaTunnelCertificate = await client.Beta.Tunnels.Certificates.Retrieve(parameters);

Console.WriteLine(betaTunnelCertificate);
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

`CertificateListPageResponse Beta.Tunnels.Certificates.List(CertificateListParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

### Parameters

- `CertificateListParams parameters`

  - `required string tunnelID`

    Path param: Path parameter tunnel_id

  - `Boolean includeArchived`

    Query param: Whether to include archived certificates in the results. Defaults to false.

  - `Int limit`

    Query param: Maximum number of certificates to return per page. Defaults to 20, maximum 1000.

  - `string page`

    Query param: Opaque pagination cursor from a previous `list_tunnel_certificates` response.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class CertificateListPageResponse:`

  The tunnel's certificates.

  - `required IReadOnlyList<BetaTunnelCertificate> Data`

    List of certificates, ordered by created_at descending.

    - `required string ID`

      Unique identifier for the certificate, prefixed with `tcrt_`.

    - `required DateTimeOffset? ArchivedAt`

      A timestamp in RFC 3339 format

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required DateTimeOffset? ExpiresAt`

      A timestamp in RFC 3339 format

    - `required string Fingerprint`

      Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

    - `required string TunnelID`

      ID of the tunnel the certificate is registered against.

    - `JsonElement Type "tunnel_certificate"constant`

  - `required string? NextPage`

    Pagination cursor for the next page, or null if no more results.

### Example

```csharp
CertificateListParams parameters = new() { TunnelID = "tunnel_id" };

var page = await client.Beta.Tunnels.Certificates.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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

`BetaTunnelCertificate Beta.Tunnels.Certificates.Archive(CertificateArchiveParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

### Parameters

- `CertificateArchiveParams parameters`

  - `required string tunnelID`

    Path param: Path parameter tunnel_id

  - `required string certificateID`

    Path param: Path parameter certificate_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `required string ID`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

  - `required string Fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `required string TunnelID`

    ID of the tunnel the certificate is registered against.

  - `JsonElement Type "tunnel_certificate"constant`

### Example

```csharp
CertificateArchiveParams parameters = new()
{
    TunnelID = "tunnel_id",
    CertificateID = "certificate_id",
};

var betaTunnelCertificate = await client.Beta.Tunnels.Certificates.Archive(parameters);

Console.WriteLine(betaTunnelCertificate);
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

  - `required string ID`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

  - `required string Fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `required string TunnelID`

    ID of the tunnel the certificate is registered against.

  - `JsonElement Type "tunnel_certificate"constant`

# Webhooks

## Domain Types

### Beta Webhook Agent Archived Event Data

- `class BetaWebhookAgentArchivedEventData:`

  - `required string ID`

    ID of the agent that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "agent.archived"constant`

  - `required string WorkspaceID`

### Beta Webhook Agent Created Event Data

- `class BetaWebhookAgentCreatedEventData:`

  - `required string ID`

    ID of the agent that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "agent.created"constant`

  - `required string WorkspaceID`

### Beta Webhook Agent Deleted Event Data

- `class BetaWebhookAgentDeletedEventData:`

  - `required string ID`

    ID of the agent that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "agent.deleted"constant`

  - `required string WorkspaceID`

### Beta Webhook Agent Updated Event Data

- `class BetaWebhookAgentUpdatedEventData:`

  - `required string ID`

    ID of the agent that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "agent.updated"constant`

  - `required string WorkspaceID`

### Beta Webhook Deployment Archived Event Data

- `class BetaWebhookDeploymentArchivedEventData:`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "deployment.archived"constant`

  - `required string WorkspaceID`

### Beta Webhook Deployment Created Event Data

- `class BetaWebhookDeploymentCreatedEventData:`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "deployment.created"constant`

  - `required string WorkspaceID`

### Beta Webhook Deployment Deleted Event Data

- `class BetaWebhookDeploymentDeletedEventData:`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "deployment.deleted"constant`

  - `required string WorkspaceID`

### Beta Webhook Deployment Paused Event Data

- `class BetaWebhookDeploymentPausedEventData:`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "deployment.paused"constant`

  - `required string WorkspaceID`

### Beta Webhook Deployment Run Failed Event Data

- `class BetaWebhookDeploymentRunFailedEventData:`

  - `required string ID`

    ID of the deployment run that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "deployment_run.failed"constant`

  - `required string WorkspaceID`

### Beta Webhook Deployment Run Started Event Data

- `class BetaWebhookDeploymentRunStartedEventData:`

  - `required string ID`

    ID of the deployment run that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "deployment_run.started"constant`

  - `required string WorkspaceID`

### Beta Webhook Deployment Run Succeeded Event Data

- `class BetaWebhookDeploymentRunSucceededEventData:`

  - `required string ID`

    ID of the deployment run that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "deployment_run.succeeded"constant`

  - `required string WorkspaceID`

### Beta Webhook Deployment Unpaused Event Data

- `class BetaWebhookDeploymentUnpausedEventData:`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "deployment.unpaused"constant`

  - `required string WorkspaceID`

### Beta Webhook Deployment Updated Event Data

- `class BetaWebhookDeploymentUpdatedEventData:`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "deployment.updated"constant`

  - `required string WorkspaceID`

### Beta Webhook Environment Archived Event Data

- `class BetaWebhookEnvironmentArchivedEventData:`

  - `required string ID`

    ID of the environment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "environment.archived"constant`

  - `required string WorkspaceID`

### Beta Webhook Environment Created Event Data

- `class BetaWebhookEnvironmentCreatedEventData:`

  - `required string ID`

    ID of the environment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "environment.created"constant`

  - `required string WorkspaceID`

### Beta Webhook Environment Deleted Event Data

- `class BetaWebhookEnvironmentDeletedEventData:`

  - `required string ID`

    ID of the environment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "environment.deleted"constant`

  - `required string WorkspaceID`

### Beta Webhook Environment Updated Event Data

- `class BetaWebhookEnvironmentUpdatedEventData:`

  - `required string ID`

    ID of the environment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "environment.updated"constant`

  - `required string WorkspaceID`

### Beta Webhook Event

- `class BetaWebhookEvent:`

  - `required string ID`

    Unique event identifier for idempotency.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 timestamp when the event occurred.

  - `required BetaWebhookEventData Data`

    - `class BetaWebhookSessionCreatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionPendingEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.pending"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionRunningEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.running"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionIdledEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.idled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionRequiresActionEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.requires_action"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionArchivedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionDeletedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusRescheduledEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_rescheduled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusRunStartedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_run_started"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusIdledEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_idled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusTerminatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_terminated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadCreatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string SessionThreadID`

        ID of the session thread this event refers to.

      - `JsonElement Type "session.thread_created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadIdledEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string SessionThreadID`

        ID of the session thread this event refers to.

      - `JsonElement Type "session.thread_idled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadTerminatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string SessionThreadID`

        ID of the session thread this event refers to.

      - `JsonElement Type "session.thread_terminated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.outcome_evaluation_ended"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCreatedEventData:`

      - `required string ID`

        ID of the vault that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultArchivedEventData:`

      - `required string ID`

        ID of the vault that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultDeletedEventData:`

      - `required string ID`

        ID of the vault that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialCreatedEventData:`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.created"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialArchivedEventData:`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.archived"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialDeletedEventData:`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.deleted"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.refresh_failed"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookSessionUpdatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.updated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentCreatedEventData:`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "agent.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentArchivedEventData:`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "agent.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentDeletedEventData:`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "agent.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentPausedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.paused"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentRunFailedEventData:`

      - `required string ID`

        ID of the deployment run that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment_run.failed"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentCreatedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentUpdatedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.updated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentUnpausedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.unpaused"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentUpdatedEventData:`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "agent.updated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentArchivedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentRunStartedEventData:`

      - `required string ID`

        ID of the deployment run that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment_run.started"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentDeletedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentRunSucceededEventData:`

      - `required string ID`

        ID of the deployment run that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment_run.succeeded"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentCreatedEventData:`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "environment.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentUpdatedEventData:`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "environment.updated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentArchivedEventData:`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "environment.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentDeletedEventData:`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "environment.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookMemoryStoreCreatedEventData:`

      - `required string ID`

        ID of the memory store that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "memory_store.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookMemoryStoreArchivedEventData:`

      - `required string ID`

        ID of the memory store that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "memory_store.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookMemoryStoreDeletedEventData:`

      - `required string ID`

        ID of the memory store that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "memory_store.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionBudgetReachedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.budget_reached"constant`

      - `required string WorkspaceID`

  - `JsonElement Type "event"constant`

    Object type. Always `event` for webhook payloads.

### Beta Webhook Event Data

- `class BetaWebhookEventData: A class that can be one of several variants.union`

  - `class BetaWebhookSessionCreatedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.created"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionPendingEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.pending"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionRunningEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.running"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionIdledEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.idled"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionRequiresActionEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.requires_action"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionArchivedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.archived"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionDeletedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.deleted"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionStatusRescheduledEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.status_rescheduled"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionStatusRunStartedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.status_run_started"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionStatusIdledEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.status_idled"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionStatusTerminatedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.status_terminated"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionThreadCreatedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string SessionThreadID`

      ID of the session thread this event refers to.

    - `JsonElement Type "session.thread_created"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionThreadIdledEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string SessionThreadID`

      ID of the session thread this event refers to.

    - `JsonElement Type "session.thread_idled"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionThreadTerminatedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string SessionThreadID`

      ID of the session thread this event refers to.

    - `JsonElement Type "session.thread_terminated"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.outcome_evaluation_ended"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCreatedEventData:`

    - `required string ID`

      ID of the vault that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "vault.created"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookVaultArchivedEventData:`

    - `required string ID`

      ID of the vault that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "vault.archived"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookVaultDeletedEventData:`

    - `required string ID`

      ID of the vault that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "vault.deleted"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCredentialCreatedEventData:`

    - `required string ID`

      ID of the vault credential that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "vault_credential.created"constant`

    - `required string VaultID`

      ID of the vault that owns this credential.

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCredentialArchivedEventData:`

    - `required string ID`

      ID of the vault credential that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "vault_credential.archived"constant`

    - `required string VaultID`

      ID of the vault that owns this credential.

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCredentialDeletedEventData:`

    - `required string ID`

      ID of the vault credential that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "vault_credential.deleted"constant`

    - `required string VaultID`

      ID of the vault that owns this credential.

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

    - `required string ID`

      ID of the vault credential that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "vault_credential.refresh_failed"constant`

    - `required string VaultID`

      ID of the vault that owns this credential.

    - `required string WorkspaceID`

  - `class BetaWebhookSessionUpdatedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.updated"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookAgentCreatedEventData:`

    - `required string ID`

      ID of the agent that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "agent.created"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookAgentArchivedEventData:`

    - `required string ID`

      ID of the agent that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "agent.archived"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookAgentDeletedEventData:`

    - `required string ID`

      ID of the agent that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "agent.deleted"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentPausedEventData:`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "deployment.paused"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentRunFailedEventData:`

    - `required string ID`

      ID of the deployment run that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "deployment_run.failed"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentCreatedEventData:`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "deployment.created"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentUpdatedEventData:`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "deployment.updated"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentUnpausedEventData:`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "deployment.unpaused"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookAgentUpdatedEventData:`

    - `required string ID`

      ID of the agent that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "agent.updated"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentArchivedEventData:`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "deployment.archived"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentRunStartedEventData:`

    - `required string ID`

      ID of the deployment run that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "deployment_run.started"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentDeletedEventData:`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "deployment.deleted"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentRunSucceededEventData:`

    - `required string ID`

      ID of the deployment run that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "deployment_run.succeeded"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookEnvironmentCreatedEventData:`

    - `required string ID`

      ID of the environment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "environment.created"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookEnvironmentUpdatedEventData:`

    - `required string ID`

      ID of the environment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "environment.updated"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookEnvironmentArchivedEventData:`

    - `required string ID`

      ID of the environment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "environment.archived"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookEnvironmentDeletedEventData:`

    - `required string ID`

      ID of the environment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "environment.deleted"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookMemoryStoreCreatedEventData:`

    - `required string ID`

      ID of the memory store that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "memory_store.created"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookMemoryStoreArchivedEventData:`

    - `required string ID`

      ID of the memory store that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "memory_store.archived"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookMemoryStoreDeletedEventData:`

    - `required string ID`

      ID of the memory store that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "memory_store.deleted"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionBudgetReachedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.budget_reached"constant`

    - `required string WorkspaceID`

### Beta Webhook Memory Store Archived Event Data

- `class BetaWebhookMemoryStoreArchivedEventData:`

  - `required string ID`

    ID of the memory store that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "memory_store.archived"constant`

  - `required string WorkspaceID`

### Beta Webhook Memory Store Created Event Data

- `class BetaWebhookMemoryStoreCreatedEventData:`

  - `required string ID`

    ID of the memory store that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "memory_store.created"constant`

  - `required string WorkspaceID`

### Beta Webhook Memory Store Deleted Event Data

- `class BetaWebhookMemoryStoreDeletedEventData:`

  - `required string ID`

    ID of the memory store that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "memory_store.deleted"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Archived Event Data

- `class BetaWebhookSessionArchivedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.archived"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Budget Reached Event Data

- `class BetaWebhookSessionBudgetReachedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.budget_reached"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Created Event Data

- `class BetaWebhookSessionCreatedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.created"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Deleted Event Data

- `class BetaWebhookSessionDeletedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.deleted"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Idled Event Data

- `class BetaWebhookSessionIdledEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.idled"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.outcome_evaluation_ended"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Pending Event Data

- `class BetaWebhookSessionPendingEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.pending"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Requires Action Event Data

- `class BetaWebhookSessionRequiresActionEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.requires_action"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Running Event Data

- `class BetaWebhookSessionRunningEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.running"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Status Idled Event Data

- `class BetaWebhookSessionStatusIdledEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.status_idled"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Status Rescheduled Event Data

- `class BetaWebhookSessionStatusRescheduledEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.status_rescheduled"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Status Run Started Event Data

- `class BetaWebhookSessionStatusRunStartedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.status_run_started"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Status Terminated Event Data

- `class BetaWebhookSessionStatusTerminatedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.status_terminated"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Thread Created Event Data

- `class BetaWebhookSessionThreadCreatedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string SessionThreadID`

    ID of the session thread this event refers to.

  - `JsonElement Type "session.thread_created"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Thread Idled Event Data

- `class BetaWebhookSessionThreadIdledEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string SessionThreadID`

    ID of the session thread this event refers to.

  - `JsonElement Type "session.thread_idled"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Thread Terminated Event Data

- `class BetaWebhookSessionThreadTerminatedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string SessionThreadID`

    ID of the session thread this event refers to.

  - `JsonElement Type "session.thread_terminated"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Updated Event Data

- `class BetaWebhookSessionUpdatedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.updated"constant`

  - `required string WorkspaceID`

### Beta Webhook Vault Archived Event Data

- `class BetaWebhookVaultArchivedEventData:`

  - `required string ID`

    ID of the vault that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "vault.archived"constant`

  - `required string WorkspaceID`

### Beta Webhook Vault Created Event Data

- `class BetaWebhookVaultCreatedEventData:`

  - `required string ID`

    ID of the vault that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "vault.created"constant`

  - `required string WorkspaceID`

### Beta Webhook Vault Credential Archived Event Data

- `class BetaWebhookVaultCredentialArchivedEventData:`

  - `required string ID`

    ID of the vault credential that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "vault_credential.archived"constant`

  - `required string VaultID`

    ID of the vault that owns this credential.

  - `required string WorkspaceID`

### Beta Webhook Vault Credential Created Event Data

- `class BetaWebhookVaultCredentialCreatedEventData:`

  - `required string ID`

    ID of the vault credential that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "vault_credential.created"constant`

  - `required string VaultID`

    ID of the vault that owns this credential.

  - `required string WorkspaceID`

### Beta Webhook Vault Credential Deleted Event Data

- `class BetaWebhookVaultCredentialDeletedEventData:`

  - `required string ID`

    ID of the vault credential that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "vault_credential.deleted"constant`

  - `required string VaultID`

    ID of the vault that owns this credential.

  - `required string WorkspaceID`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `class BetaWebhookVaultCredentialRefreshFailedEventData:`

  - `required string ID`

    ID of the vault credential that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "vault_credential.refresh_failed"constant`

  - `required string VaultID`

    ID of the vault that owns this credential.

  - `required string WorkspaceID`

### Beta Webhook Vault Deleted Event Data

- `class BetaWebhookVaultDeletedEventData:`

  - `required string ID`

    ID of the vault that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "vault.deleted"constant`

  - `required string WorkspaceID`

### Unwrap Webhook Event

- `class UnwrapWebhookEvent:`

  - `required string ID`

    Unique event identifier for idempotency.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 timestamp when the event occurred.

  - `required BetaWebhookEventData Data`

    - `class BetaWebhookSessionCreatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionPendingEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.pending"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionRunningEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.running"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionIdledEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.idled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionRequiresActionEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.requires_action"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionArchivedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionDeletedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusRescheduledEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_rescheduled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusRunStartedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_run_started"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusIdledEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_idled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusTerminatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_terminated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadCreatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string SessionThreadID`

        ID of the session thread this event refers to.

      - `JsonElement Type "session.thread_created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadIdledEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string SessionThreadID`

        ID of the session thread this event refers to.

      - `JsonElement Type "session.thread_idled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadTerminatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string SessionThreadID`

        ID of the session thread this event refers to.

      - `JsonElement Type "session.thread_terminated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.outcome_evaluation_ended"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCreatedEventData:`

      - `required string ID`

        ID of the vault that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultArchivedEventData:`

      - `required string ID`

        ID of the vault that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultDeletedEventData:`

      - `required string ID`

        ID of the vault that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialCreatedEventData:`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.created"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialArchivedEventData:`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.archived"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialDeletedEventData:`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.deleted"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.refresh_failed"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookSessionUpdatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.updated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentCreatedEventData:`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "agent.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentArchivedEventData:`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "agent.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentDeletedEventData:`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "agent.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentPausedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.paused"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentRunFailedEventData:`

      - `required string ID`

        ID of the deployment run that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment_run.failed"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentCreatedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentUpdatedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.updated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentUnpausedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.unpaused"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentUpdatedEventData:`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "agent.updated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentArchivedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentRunStartedEventData:`

      - `required string ID`

        ID of the deployment run that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment_run.started"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentDeletedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentRunSucceededEventData:`

      - `required string ID`

        ID of the deployment run that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "deployment_run.succeeded"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentCreatedEventData:`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "environment.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentUpdatedEventData:`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "environment.updated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentArchivedEventData:`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "environment.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentDeletedEventData:`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "environment.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookMemoryStoreCreatedEventData:`

      - `required string ID`

        ID of the memory store that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "memory_store.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookMemoryStoreArchivedEventData:`

      - `required string ID`

        ID of the memory store that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "memory_store.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookMemoryStoreDeletedEventData:`

      - `required string ID`

        ID of the memory store that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "memory_store.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionBudgetReachedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.budget_reached"constant`

      - `required string WorkspaceID`

  - `JsonElement Type "event"constant`

    Object type. Always `event` for webhook payloads.
