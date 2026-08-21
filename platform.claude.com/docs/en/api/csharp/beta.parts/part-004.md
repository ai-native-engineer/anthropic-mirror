<!-- source: https://platform.claude.com/docs/en/api/csharp/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/csharp/beta -->

<!-- chunk-start -->

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

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

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

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

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

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

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

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Speed Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"Standard`

      - `"fast"Fast`

  - `required BetaOutputBehavior OutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `required Type Type`

        - `"create_new"CreateNew`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"update_existing"UpdateExisting`

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

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

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

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

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

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

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

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Speed Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"Standard`

      - `"fast"Fast`

  - `required BetaOutputBehavior OutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `required Type Type`

        - `"create_new"CreateNew`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"update_existing"UpdateExisting`

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

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

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

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Speed Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"Standard`

      - `"fast"Fast`

  - `required BetaOutputBehavior OutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `required Type Type`

        - `"create_new"CreateNew`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `required string MemoryStoreID`

      - `required Type Type`

        - `"update_existing"UpdateExisting`

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

  An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

  - `class BetaDreamMemoryStoreInput:`

    An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

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

  An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

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

    Model identifier, e.g. "claude-opus-5". 1-256 characters.

  - `Speed Speed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"Standard`

    - `"fast"Fast`

### Beta Dream Model Config Param

- `class BetaDreamModelConfigParam:`

  Model identifier and configuration applied to every pipeline stage.

  - `required string ID`

    Model identifier, e.g. "claude-opus-5". 1-256 characters.

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

### Beta Output Behavior

- `class BetaOutputBehavior: A class that can be one of several variants.union`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `class BetaOutputBehaviorCreateNew:`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `required Type Type`

      - `"create_new"CreateNew`

  - `class BetaOutputBehaviorUpdateExisting:`

    The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

    - `required string MemoryStoreID`

    - `required Type Type`

      - `"update_existing"UpdateExisting`

### Beta Output Behavior Create New

- `class BetaOutputBehaviorCreateNew:`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `required Type Type`

    - `"create_new"CreateNew`

### Beta Output Behavior Update Existing

- `class BetaOutputBehaviorUpdateExisting:`

  The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

  - `required string MemoryStoreID`

  - `required Type Type`

    - `"update_existing"UpdateExisting`

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

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

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

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

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

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

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

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

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

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

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

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

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

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

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

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

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

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

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

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

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
